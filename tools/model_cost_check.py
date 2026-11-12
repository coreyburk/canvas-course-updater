#!/usr/bin/env python3
"""Reprice real AI coding-agent usage (Claude Code, Codex, Antigravity) on every current model.

Reads the local session logs each tool writes, sums the tokens actually used in
a billing window, and recomputes what that exact token mix would cost on each
current model, using pricing fetched LIVE from the vendors' pricing pages at
run time (Anthropic, OpenAI, Google). Prices are never hardcoded: a stale table
is exactly how the wrong model got recommended (2026-11-10).

Sources (--source, default all):
  claude  ~/.claude/projects/<repo-slug>/**/*.jsonl  (exact per-request usage)
  codex   ~/.codex/sessions/**/*.jsonl               (exact per-request usage,
                                                      plus subscription rate-limit %)
  agy     ~/.gemini/antigravity-cli/conversations/*.db
          (per-request usage decoded from undocumented protobuf blobs - treat
           as an estimate; field meanings were inferred, see load_agy())

How each tool is paid for matters (Corey, 2026-11-12): Claude Code is metered
API (dollars are real), Codex is a ChatGPT Plus subscription and Antigravity is
a Google subscription/quota (dollars are API-equivalent, i.e. "what this would
cost metered"; the real constraint is limit headroom, reported where the logs
carry it).

Why cache reads matter: on Canvas work, cache reads are 70-85% of the bill, so
a model's headline input/output price ranks models wrongly.

Usage (repo root; ASCII output):
  python tools/model_cost_check.py                       # today, all sources, this repo
  python tools/model_cost_check.py --days 30 --all-projects
  python tools/model_cost_check.py --source codex --days 30
  python tools/model_cost_check.py --day 2026-11-09 --billed 62.37   # Claude only
  python tools/model_cost_check.py --include-mythos      # limited-availability models

Logs are per machine. Run this on every machine you work on; one run is a
partial picture. Days are UTC dates (the Claude console's usage chart is UTC).
Output is aggregate numbers only; no transcript content is printed. Reads local
files and three public docs pages. Touches nothing in Canvas.
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import sqlite3
import sys
import urllib.request

ANTHROPIC_URL = "https://platform.claude.com/docs/en/about-claude/pricing.md"
OPENAI_URL = "https://developers.openai.com/api/docs/pricing.md"
GEMINI_URL = "https://ai.google.dev/gemini-api/docs/pricing.md.txt"
HOME = os.path.expanduser("~")
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = dt.datetime.now(dt.timezone.utc).date()


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "model-cost-check/2.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.read().decode("utf-8")
    except Exception as e:  # fail loudly: never fall back to remembered prices
        sys.exit("Could not fetch live pricing (%s).\n  %s\nRefusing to use remembered "
                 "prices; fix the connection and rerun." % (url, e))


# ---------------------------------------------------------------- pricing --
# Every price entry: {"short": rec, "long": rec, "long_at": tokens or None,
#                     "provider": str, "retired": bool, "limited": bool}
# rec keys (USD per MTok): inp, read, w5, w1, out

def money(cell):
    n = re.search(r"\$([\d.]+)", re.sub(r"<sup>.*?</sup>", "", cell or ""))
    return float(n.group(1)) if n else None


def prices_anthropic():
    text = fetch(ANTHROPIC_URL)
    prices = {}
    for line in text.splitlines():
        if not line.startswith("| Claude"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        m = re.match(r"Claude [A-Za-z]+ [\d.]+", cells[0])
        nums = [money(c) for c in cells[1:6]]
        if not m or None in nums:
            continue
        rec = dict(zip(("inp", "w5", "w1", "read", "out"), nums))
        e = prices.setdefault(m.group(0), {"short": None, "long": None, "long_at": 100_000,
                                           "provider": "anthropic"})
        e["retired"] = "retired" in cells[0]
        e["limited"] = "limited availability" in cells[0]
        e["long" if "over 100,000" in cells[0] else "short"] = rec
    for e in prices.values():
        if e["long"] is None:
            e["long"], e["long_at"] = e["short"], None
    prices = {k: v for k, v in prices.items() if v["short"]}
    if len(prices) < 5:
        sys.exit("Parsed fewer than 5 Anthropic models from %s - page format changed. "
                 "Fix prices_anthropic() before trusting any output." % ANTHROPIC_URL)
    return prices


CODEX_MODEL = re.compile(r"^gpt-\d+(?:\.\d+)?(?:-(?:mini|nano|sol|terra|luna|astra))?$")


def prices_openai():
    """First occurrence of each model wins: the Standard tier is listed before Batch/Flex."""
    text = fetch(OPENAI_URL)
    prices, header = {}, None
    for line in text.splitlines():
        if not line.startswith("|"):
            header = None if not line.strip() else header
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] == "Model":
            header = [c.lower() for c in cells]
            continue
        if not header or cells[0].startswith("---"):
            continue
        name = re.sub(r"\s*\(.*?\)", "", cells[0]).strip()
        if not CODEX_MODEL.match(name) or name in prices:
            continue
        col = dict(zip(header, cells))

        def rec(prefix):
            inp = money(col.get(prefix + "input"))
            out = money(col.get(prefix + "output"))
            if inp is None or out is None:
                return None
            read = money(col.get(prefix + "cached input"))
            w = money(col.get(prefix + "30m write"))
            return {"inp": inp, "out": out, "read": read if read is not None else inp,
                    "w5": w if w is not None else inp, "w1": w if w is not None else inp}

        short = rec("short context ") or rec("")
        if not short:
            continue
        long_ = rec("long context ")
        m = re.search(r"<\s*([\d]+)K", cells[0])
        prices[name] = {"short": short, "long": long_ or short,
                        "long_at": int(m.group(1)) * 1000 if (m and long_) else (272_000 if long_ else None),
                        "provider": "openai", "retired": False, "limited": False}
    if len(prices) < 5:
        sys.exit("Parsed fewer than 5 OpenAI models from %s - page format changed. "
                 "Fix prices_openai() before trusting any output." % OPENAI_URL)
    return prices


GEMINI_TEXT_MODEL = re.compile(r"^Gemini (?:[\d.]+ (?:Pro|Flash|Flash-Lite)(?: Preview)?|4 [A-Z][a-z]+)$")


def gemini_amount(cell_text):
    """Return (short, long) current USD/MTok from a Gemini pricing cell, honoring
    'through <date>' / 'starting <date>' schedules and '<= 200k' / '> 200k' tiers."""
    parts = re.split(r"(?=\$[\d.]+)", cell_text)
    short = long_ = None
    for p in parts:
        amt = money(p)
        if amt is None or "per hour" in p or "storage" in p:
            continue
        m = re.search(r"(through|starting) ([A-Z][a-z]+ \d{1,2}, \d{4})", p)
        if m:
            d = dt.datetime.strptime(m.group(2), "%B %d, %Y").date()
            if (m.group(1) == "through" and TODAY > d) or (m.group(1) == "starting" and TODAY < d):
                continue
        if re.search(r">\s*200", p):
            long_ = long_ if long_ is not None else amt
        else:
            short = short if short is not None else amt
    return short, (long_ if long_ is not None else short)


def prices_gemini():
    text = fetch(GEMINI_URL)
    prices = {}
    for sec in re.split(r"\n## ", text)[1:]:
        name = re.sub(r"\s*\{%.*", "", sec.splitlines()[0]).strip()
        if not GEMINI_TEXT_MODEL.match(name):
            continue
        std = sec.split('{% tab title="Standard" %}', 1)
        if len(std) < 2:
            continue
        rows = std[1].split("{% /tab %}", 1)[0].split("\n  ---")
        found = {}
        for row in rows:
            cells = [c.strip() for c in re.split(r"\n\s*\* ", "\n" + row.strip()) if c.strip()]
            if len(cells) < 3:
                continue
            label = cells[0].lower()
            key = ("inp" if label.startswith("input price") else
                   "out" if label.startswith("output price") else
                   "read" if label.startswith("context caching price") else None)
            if key and key not in found:
                found[key] = gemini_amount(cells[2])
        if not all(k in found and found[k][0] is not None for k in ("inp", "out")):
            continue
        rd = found.get("read", (None, None))

        def rec(i):
            inp = found["inp"][i]
            return {"inp": inp, "out": found["out"][i], "w5": inp, "w1": inp,
                    "read": rd[i] if rd[i] is not None else inp}
        prices[name] = {"short": rec(0), "long": rec(1),
                        "long_at": 200_000 if found["inp"][1] != found["inp"][0] else None,
                        "provider": "google", "retired": False, "limited": False}
    if len(prices) < 3:
        sys.exit("Parsed fewer than 3 Gemini text models from %s - page format changed. "
                 "Fix prices_gemini() before trusting any output." % GEMINI_URL)
    return prices


# ------------------------------------------------------------ model names --

def canon_claude(mid):
    """claude-opus-5-5[-low|-20251001] -> 'Claude Opus 5.5'; 'Claude Opus 5.5 (Low)' -> same."""
    if mid and mid.startswith("Claude "):
        return re.sub(r"\s*\(.*?\)", "", mid).strip()
    m = re.match(r"^claude-([a-z]+)-(\d+(?:-\d{1,2})?)(?:-[a-z]+)?(?:-\d{8})?$", mid or "")
    if not m:
        return None
    return "Claude %s %s" % (m.group(1).capitalize(), m.group(2).replace("-", "."))


def lookup(prices, model):
    """Return (price name, entry, note) or (None, None, None)."""
    if model in prices:
        return model, prices[model], ""
    c = canon_claude(model)
    if c in prices:
        return c, prices[c], ""
    g = re.sub(r"\s*\(.*?\)", "", model or "").strip()
    if g in prices:
        return g, prices[g], ""
    base = re.sub(r"-codex(-\w+)?$", "", model or "")  # gpt-5.3-codex -> gpt-5.3
    for cand in (base, re.sub(r"\.\d+$", "", base)):
        if cand and cand != model and cand in prices:
            return cand, prices[cand], " (priced as %s)" % cand
    return None, None, None


# ---------------------------------------------------------------- sources --
# Normalized record: {day, model, inp (uncached input), read, w5, w1, out}

def repo_slug(path):
    return re.sub(r"[^A-Za-z0-9]", "-", path)


def load_claude(all_projects, project_dir):
    root = os.path.join(HOME, ".claude", "projects")
    pattern = (os.path.join(root, "*", "**", "*.jsonl") if all_projects else
               os.path.join(project_dir or os.path.join(root, repo_slug(REPO)), "**", "*.jsonl"))
    files = glob.glob(pattern, recursive=True)
    per_req = {}  # dedupe: streamed/forked sessions repeat entries, keep field-wise max
    for fn in files:
        try:
            fh = open(fn, encoding="utf-8")
        except OSError:
            continue
        with fh:
            for line in fh:
                if '"usage"' not in line:
                    continue
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                msg = d.get("message") or {}
                u = msg.get("usage")
                ts = d.get("timestamp") or ""
                if not u or not ts or not msg.get("model") or msg["model"].startswith("<"):
                    continue
                key = d.get("requestId") or msg.get("id") or (fn, d.get("uuid"))
                cc = u.get("cache_creation") or {}
                w1 = cc.get("ephemeral_1h_input_tokens") or 0
                w5 = cc.get("ephemeral_5m_input_tokens") or 0
                wtot = u.get("cache_creation_input_tokens") or 0
                if w5 + w1 < wtot:  # no breakdown present: treat the remainder as 5m
                    w5 += wtot - (w5 + w1)
                rec = {"day": ts[:10], "model": msg["model"],
                       "inp": u.get("input_tokens") or 0, "out": u.get("output_tokens") or 0,
                       "read": u.get("cache_read_input_tokens") or 0, "w1": w1, "w5": w5}
                old = per_req.get(key)
                if old is None:
                    per_req[key] = rec
                else:
                    for f in ("inp", "out", "read", "w1", "w5"):
                        old[f] = max(old[f], rec[f])
    return list(per_req.values()), len(files), {}


def same_repo(path):
    return bool(path) and os.path.normcase(os.path.normpath(path)) == os.path.normcase(REPO)


def load_codex(all_projects, _project_dir):
    files = glob.glob(os.path.join(HOME, ".codex", "sessions", "**", "*.jsonl"), recursive=True)
    recs, limits = [], {}
    for fn in files:
        model, cwd, last_total = None, None, None
        try:
            fh = open(fn, encoding="utf-8")
        except OSError:
            continue
        with fh:
            for line in fh:
                if '"turn_context"' not in line and '"token_count"' not in line \
                        and '"session_meta"' not in line:
                    continue
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                p = d.get("payload") or {}
                if d.get("type") in ("session_meta", "turn_context"):
                    model = p.get("model") or model
                    cwd = p.get("cwd") or cwd
                    continue
                if p.get("type") != "token_count":
                    continue
                ts = d.get("timestamp") or ""
                rl = p.get("rate_limits") or {}
                if rl:  # subscription headroom: keep the latest snapshot per window
                    for win in ("primary", "secondary"):
                        w = rl.get(win) or {}
                        if w.get("used_percent") is not None:
                            key = (rl.get("plan_type"), win, w.get("window_minutes"))
                            prev = limits.get(key)
                            if prev is None or ts > prev["ts"]:
                                limits[key] = {"ts": ts, "used": w["used_percent"]}
                            pk = limits[key]
                            pk["peak"] = max(pk.get("peak", 0), w["used_percent"])
                info = p.get("info") or {}
                u, tot = info.get("last_token_usage"), info.get("total_token_usage") or {}
                if not u or not ts or tot.get("total_tokens") == last_total:
                    continue  # repeated event with no new request
                last_total = tot.get("total_tokens")
                if not all_projects and not same_repo(cwd):
                    continue
                cached = u.get("cached_input_tokens") or 0
                recs.append({"day": ts[:10], "model": model or "unknown",
                             "inp": max((u.get("input_tokens") or 0) - cached, 0), "read": cached,
                             "w5": 0, "w1": 0, "out": u.get("output_tokens") or 0})
    return recs, len(files), limits


def _varint(b, i):
    r = s = 0
    while True:
        x = b[i]
        i += 1
        r |= (x & 0x7F) << s
        s += 7
        if x < 0x80:
            return r, i


def _pb(b):
    """One level of protobuf wire format -> [(field, wiretype, value)]. Raises on junk."""
    out, i = [], 0
    while i < len(b):
        key, i = _varint(b, i)
        f, wt = key >> 3, key & 7
        if wt == 0:
            v, i = _varint(b, i)
        elif wt == 2:
            n, i = _varint(b, i)
            v, i = b[i:i + n], i + n
        elif wt == 1:
            v, i = b[i:i + 8], i + 8
        elif wt == 5:
            v, i = b[i:i + 4], i + 4
        else:
            raise ValueError("bad wiretype")
        out.append((f, wt, v))
    return out


def load_agy(all_projects, _project_dir):
    """Antigravity stores one gen_metadata row per model request. Layout inferred
    2026-11-12 (undocumented, may change): row.1 = generation record;
    .1.21 = model display name ("Claude Opus 5.5 (Low)"); .1.9.4.1 = epoch secs;
    .1.4 = usage: 2 = uncached input, 5 = cache read, 3 = output (incl. thinking,
    which is 9). Field 1 is a small per-model constant and is ignored. Cache
    writes are not separated out, so Claude-in-AGY is priced with writes as plain
    input (slightly understated)."""
    files = glob.glob(os.path.join(HOME, ".gemini", "antigravity-cli", "conversations", "*.db"))
    recs, repo_uri = [], "file:///" + REPO.replace("\\", "/")
    for fn in files:
        try:
            con = sqlite3.connect("file:%s?mode=ro" % fn, uri=True)
            if not all_projects:
                blob = (con.execute("select data from trajectory_metadata_blob").fetchone() or [b""])[0]
                if repo_uri.lower().encode() not in (blob or b"").lower():
                    con.close()
                    continue
            rows = con.execute("select data from gen_metadata").fetchall()
            con.close()
        except sqlite3.Error:
            continue
        for (data,) in rows:
            try:
                gen = next(v for f, wt, v in _pb(data) if f == 1 and wt == 2)
                sub = _pb(gen)
                name = next((v.decode("utf-8", "replace") for f, wt, v in sub if f == 21 and wt == 2), None)
                usage = next(({f2: v2 for f2, w2, v2 in _pb(v) if w2 == 0}
                              for f, wt, v in sub if f == 4 and wt == 2), None)
                ts = None
                for f, wt, v in sub:
                    if f == 9 and wt == 2:
                        for g, w2, v2 in _pb(v):
                            if g == 4 and w2 == 2:
                                ts = dict((h, x) for h, w3, x in _pb(v2) if w3 == 0).get(1)
            except (StopIteration, ValueError, IndexError):
                continue
            ts = ts or int(os.path.getmtime(fn))
            if not usage or not ts or not name:
                continue
            recs.append({"day": dt.datetime.fromtimestamp(ts, dt.timezone.utc).date().isoformat(),
                         "model": name, "inp": usage.get(2, 0), "read": usage.get(5, 0),
                         "w5": 0, "w1": 0, "out": usage.get(3, 0)})
    return recs, len(files), {}


SOURCES = {
    "claude": ("Claude Code", load_claude, ("anthropic",), "metered API - dollars are real"),
    "codex": ("Codex", load_codex, ("openai",), "ChatGPT subscription - dollars are API-equivalent"),
    "agy": ("Antigravity", load_agy, ("anthropic", "google"),
            "Google subscription - dollars are API-equivalent; tokens decoded from undocumented logs"),
}


# ------------------------------------------------------------- arithmetic --

def new_bucket():
    return {"n": 0, "inp": 0, "out": 0, "read": 0, "w5": 0, "w1": 0}


def add(b, r):
    b["n"] += r.get("n", 1)
    for k in ("inp", "out", "read", "w5", "w1"):
        b[k] += r[k]


def cost_rec(entry, r):
    """Cost of one request (or a bucket of same-tier requests) on a price entry."""
    ctx = (r["inp"] + r["read"] + r["w5"] + r["w1"]) / max(r.get("n", 1), 1)
    p = entry["long"] if entry["long_at"] and ctx > entry["long_at"] else entry["short"]
    total = (r["inp"] * p["inp"] + r["out"] * p["out"] + r["w5"] * p["w5"]
             + r["w1"] * p["w1"] + r["read"] * p["read"]) / 1e6
    return total, r["read"] * p["read"] / 1e6


def tiered(recs):
    """Bucket requests by prompt size so per-request tiered pricing stays right
    after aggregation. Edges cover every tier boundary in use (100k/200k/272k)."""
    edges = (100_000, 200_000, 272_000)
    out = {}
    for r in recs:
        ctx = r["inp"] + r["read"] + r["w5"] + r["w1"]
        k = sum(ctx > e for e in edges)
        add(out.setdefault(k, new_bucket()), r)
    return list(out.values())


def cost_many(entry, buckets):
    t = rd = 0.0
    for b in buckets:
        c, r = cost_rec(entry, b)
        t, rd = t + c, rd + r
    return t, rd


# ------------------------------------------------------------------- main --

def report(label, note, recs, nfiles, limits, prices, candidates, args):
    print("\n" + "=" * 78)
    print("%s  (%s)" % (label, note))
    print("=" * 78)
    if not recs:
        print("No usage in the window across %d log files on this machine." % nfiles)
        return 0.0
    tot = new_bucket()
    for r in recs:
        add(tot, r)
    print("Requests: %d   uncached in: %.2fM   cache read: %.1fM   cache write: %.2fM   output: %.2fM"
          % (tot["n"], tot["inp"] / 1e6, tot["read"] / 1e6, (tot["w5"] + tot["w1"]) / 1e6, tot["out"] / 1e6))
    print("Avg context per request: %dk tokens    log files scanned: %d"
          % ((tot["inp"] + tot["read"] + tot["w5"] + tot["w1"]) / max(tot["n"], 1) / 1000, nfiles))

    print("\nWhat actually ran:")
    by_model = {}
    for r in recs:
        by_model.setdefault(r["model"], []).append(r)
    actual, unpriced, priced_recs = 0.0, [], []
    for model, rs in sorted(by_model.items(), key=lambda kv: -len(kv[1])):
        name, entry, why = lookup(prices, model)
        if entry:
            c, _ = cost_many(entry, tiered(rs))
            actual += c
            priced_recs.extend(rs)
            print("  %-34s %6d requests  $%9.2f%s" % (model[:34], len(rs), c, why))
        else:
            unpriced.append(model)
            print("  %-34s %6d requests  (no live price found)" % (model[:34], len(rs)))
    print("  %-34s %6s           $%9.2f" % ("TOTAL (priced models)", "", actual))
    if unpriced:
        print("  WARNING: no price for %s; totals exclude them." % ", ".join(unpriced))

    print("\nSame token mix repriced on each current model this tool can run (cheapest first):")
    print("  %-30s %10s %11s %10s %11s" % ("model", "cache rd $", "cost", "vs actual", "cache-rd %"))
    buckets, priced_buckets, rows = tiered(recs), tiered(priced_recs), []
    for name, e in prices.items():
        if e["provider"] not in candidates or e["retired"] or (e["limited"] and not args.include_mythos):
            continue
        c, rd = cost_many(e, buckets)
        cp, _ = cost_many(e, priced_buckets)
        rows.append((c, cp, name, e["short"]["read"], rd))
    for c, cp, name, rdp, rd in sorted(rows):
        delta = "%+d%%" % round((cp - actual) / actual * 100) if actual else "n/a"
        print("  %-30s %10s %11s %10s %10d%%" % (name, "$%.3f" % rdp, "$%.2f" % c, delta,
                                                round(rd / c * 100) if c else 0))

    if limits:
        print("\nSubscription headroom (latest snapshot in the logs, all projects):")
        for (plan, win, mins), v in sorted(limits.items(), key=lambda kv: kv[0][2] or 0):
            span = "%dh" % (mins // 60) if mins and mins < 1440 else "%dd" % (mins // 1440) if mins else "?"
            print("  plan=%-6s %-9s window=%-4s latest %5.1f%% used (%s)   peak seen %5.1f%%"
                  % (plan, win, span, v["used"], v["ts"][:16], v["peak"]))

    if len({r["day"] for r in recs}) > 1:
        print("\nPer day (on the model that ran):")
        days = {}
        for r in recs:
            days.setdefault(r["day"], {}).setdefault(r["model"], []).append(r)
        for day in sorted(days):
            c = 0.0
            for model, rs in days[day].items():
                _, entry, _ = lookup(prices, model)
                if entry:
                    c += cost_many(entry, tiered(rs))[0]
            print("  %s  $%9.2f   %d requests" % (day, c, sum(len(v) for v in days[day].values())))
    return actual


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--source", choices=["all"] + list(SOURCES), default="all")
    ap.add_argument("--day", help="UTC day YYYY-MM-DD (default: today UTC)")
    ap.add_argument("--days", type=int, default=1, help="window length ending at --day")
    ap.add_argument("--all-projects", action="store_true",
                    help="every repo on this machine, not just this one")
    ap.add_argument("--project-dir", help="Claude Code transcript directory (default: this repo's)")
    ap.add_argument("--include-mythos", action="store_true", help="include limited-availability models")
    ap.add_argument("--billed", type=float, help="Claude console dollar figure for the window")
    args = ap.parse_args()

    end = dt.date.fromisoformat(args.day) if args.day else TODAY
    days = {(end - dt.timedelta(days=i)).isoformat() for i in range(max(args.days, 1))}
    chosen = list(SOURCES) if args.source == "all" else [args.source]

    need = {p for s in chosen for p in SOURCES[s][2]}
    prices = {}
    if "anthropic" in need:
        prices.update(prices_anthropic())
    if "openai" in need:
        prices.update(prices_openai())
    if "google" in need:
        prices.update(prices_gemini())

    window = end.isoformat() if len(days) == 1 else "%s .. %s" % (min(days), end.isoformat())
    print("Window (UTC days): %s    scope: %s    machine logs only"
          % (window, "all projects" if args.all_projects else os.path.basename(REPO)))

    grand = {}
    for s in chosen:
        label, loader, candidates, note = SOURCES[s]
        recs, nfiles, limits = loader(args.all_projects, args.project_dir)
        recs = [r for r in recs if r["day"] in days]
        grand[label] = report(label, note, recs, nfiles, limits, prices, candidates, args)
        if s == "claude" and args.billed and grand[label]:
            print("  Billed figure given: $%.2f -> estimate/billed = %.2f"
                  % (args.billed, grand[label] / args.billed))

    if len(chosen) > 1:
        print("\n" + "=" * 78)
        print("Summary (dollars at live API prices; only Claude Code is actually metered):")
        for label, c in grand.items():
            print("  %-14s $%9.2f" % (label, c))

    print("\nNotes:")
    print("  - Prices fetched live: %s" % ", ".join(
        u for p, u in (("anthropic", ANTHROPIC_URL), ("openai", OPENAI_URL), ("google", GEMINI_URL)) if p in need))
    print("  - Repricing holds token counts fixed. Tokenizers and retry counts differ by model,")
    print("    so treat it as a ceiling on savings. Judge cost per finished task, not per request.")
    print("  - Logs are per machine. Run on every machine for the full picture.")
    if not args.all_projects:
        print("  - Only this repo. Add --all-projects to include every repo on this machine.")


if __name__ == "__main__":
    main()

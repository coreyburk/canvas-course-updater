#!/usr/bin/env python3
"""Reprice real Claude Code usage against every current model.

Reads the session transcripts Claude Code writes under ~/.claude/projects/,
sums the tokens actually used in a billing window, and recomputes what that
exact token mix would have cost on each current model, using pricing fetched
LIVE from Anthropic's pricing page at run time.

Why this exists: on Canvas work, cache reads are 70-85% of the bill, so a
model's headline input/output price ranks models wrongly. The cache-read
column is what matters, and it changes between model generations. Run this
when a new model ships, or whenever the monthly spend looks off. Prices are
fetched, never hardcoded, because a stale table is exactly how the wrong model
got recommended (2026-11-10).

Usage (from the repo root; output is plain ASCII so no encoding env var needed):
  python tools/model_cost_check.py                  # today (UTC billing day)
  python tools/model_cost_check.py --day 2026-11-09
  python tools/model_cost_check.py --days 7         # 7 days ending --day
  python tools/model_cost_check.py --all-projects   # every project, not just this repo
  python tools/model_cost_check.py --billed 62.37   # also print est-vs-billed ratio
  python tools/model_cost_check.py --include-mythos # limited-availability models

The usage chart in the Claude console dates days in UTC, so a billing day here
is a UTC date (5:00 PM to 5:00 PM MST in winter). Output is aggregate numbers
only; no transcript content is printed.

Reads local files and one public docs page. Touches nothing in Canvas.
"""
import argparse
import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.request

PRICING_URL = "https://platform.claude.com/docs/en/about-claude/pricing.md"
LONG_PROMPT_TOKENS = 100_000  # Haiku 5.5 bills a request at the higher tier above this


# ---------------------------------------------------------------- pricing --

def fetch_prices():
    """Return {model name: {'short': {...}, 'long': {...}, flags}} from the live page."""
    req = urllib.request.Request(PRICING_URL, headers={"User-Agent": "model-cost-check/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            text = r.read().decode("utf-8")
    except Exception as e:  # fail loudly: never fall back to remembered prices
        sys.exit("Could not fetch live pricing (%s).\n  %s\nRefusing to use remembered "
                 "prices; fix the connection and rerun." % (PRICING_URL, e))

    prices = {}
    for line in text.splitlines():
        if not line.startswith("| Claude"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6:
            continue
        m = re.match(r"Claude [A-Za-z]+ [\d.]+", cells[0])
        nums = []
        for c in cells[1:6]:
            c = re.sub(r"<sup>.*?</sup>", "", c)
            n = re.search(r"\$([\d.]+)", c)
            nums.append(float(n.group(1)) if n else None)
        if not m or None in nums:
            continue
        rec = dict(zip(("inp", "w5", "w1", "read", "out"), nums))
        entry = prices.setdefault(m.group(0), {"short": None, "long": None})
        entry["retired"] = "retired" in cells[0]
        entry["limited"] = "limited availability" in cells[0]
        if "over 100,000" in cells[0]:
            entry["long"] = rec
        else:
            entry["short"] = rec
    for e in prices.values():
        if e["long"] is None:
            e["long"] = e["short"]
    if sum(1 for e in prices.values() if e["short"]) < 5:
        sys.exit("Parsed fewer than 5 priced models from %s - the page format has "
                 "changed. Fix fetch_prices() before trusting any output." % PRICING_URL)
    return prices


def model_id_to_name(mid):
    """claude-opus-5-5 -> 'Claude Opus 5.5'; claude-haiku-4-5-20251001 -> 'Claude Haiku 4.5'."""
    m = re.match(r"^claude-([a-z]+)-(\d+(?:-\d{1,2})?)(?:-\d{8})?$", mid or "")
    if not m:
        return None
    return "Claude %s %s" % (m.group(1).capitalize(), m.group(2).replace("-", "."))


# ------------------------------------------------------------ transcripts --

def transcript_files(all_projects, project_dir):
    root = os.path.join(os.path.expanduser("~"), ".claude", "projects")
    if all_projects:
        pattern = os.path.join(root, "*", "**", "*.jsonl")
    else:
        pattern = os.path.join(project_dir, "**", "*.jsonl")  # includes subagents/
    return glob.glob(pattern, recursive=True)


def default_project_dir():
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    slug = re.sub(r"[^A-Za-z0-9]", "-", repo)
    return os.path.join(os.path.expanduser("~"), ".claude", "projects", slug)


def load_usage(files):
    """Deduplicate by request (streamed and forked sessions repeat entries), keeping
    the field-wise max, then return the per-request usage records."""
    per_req = {}
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
                rec = {
                    "day": ts[:10], "model": msg["model"],
                    "inp": u.get("input_tokens") or 0,
                    "out": u.get("output_tokens") or 0,
                    "read": u.get("cache_read_input_tokens") or 0,
                    "w1": cc.get("ephemeral_1h_input_tokens") or 0,
                    "w5": cc.get("ephemeral_5m_input_tokens") or 0,
                    "wtot": u.get("cache_creation_input_tokens") or 0,
                }
                old = per_req.get(key)
                if old is None:
                    per_req[key] = rec
                else:
                    for f in ("inp", "out", "read", "w1", "w5", "wtot"):
                        old[f] = max(old[f], rec[f])
    return per_req.values()


def new_bucket():
    return {"n": 0, "inp": 0, "out": 0, "read": 0, "w5": 0, "w1": 0}


def aggregate(records, days):
    """data[day][model_id][tier] -> bucket. Tier is by prompt length (Haiku 5.5 pricing)."""
    data = {}
    for r in records:
        if r["day"] not in days:
            continue
        w5, w1 = r["w5"], r["w1"]
        if w5 + w1 < r["wtot"]:  # no breakdown present: treat the remainder as 5m
            w5 += r["wtot"] - (w5 + w1)
        tier = "long" if r["inp"] + r["read"] + w5 + w1 > LONG_PROMPT_TOKENS else "short"
        b = data.setdefault(r["day"], {}).setdefault(r["model"], {}).setdefault(tier, new_bucket())
        b["n"] += 1
        b["inp"] += r["inp"]
        b["out"] += r["out"]
        b["read"] += r["read"]
        b["w5"] += w5
        b["w1"] += w1
    return data


def cost(p, b):
    return (b["inp"] * p["inp"] + b["out"] * p["out"] + b["w5"] * p["w5"]
            + b["w1"] * p["w1"] + b["read"] * p["read"]) / 1e6


def model_cost(entry, tiers):
    """Return (total cost, cache-read portion of it) for a {tier: bucket} mapping."""
    total = sum(cost(entry[t], b) for t, b in tiers.items())
    read = sum(b["read"] * entry[t]["read"] / 1e6 for t, b in tiers.items())
    return total, read


def merge_tiers(per_model_tiers):
    out = {}
    for tiers in per_model_tiers:
        for t, b in tiers.items():
            o = out.setdefault(t, new_bucket())
            for k in o:
                o[k] += b[k]
    return out


# ------------------------------------------------------------------- main --

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--day", help="UTC billing day YYYY-MM-DD (default: today UTC)")
    ap.add_argument("--days", type=int, default=1, help="window length ending at --day")
    ap.add_argument("--all-projects", action="store_true",
                    help="scan every project under ~/.claude/projects")
    ap.add_argument("--project-dir", help="transcript directory (default: this repo's)")
    ap.add_argument("--include-mythos", action="store_true",
                    help="include limited-availability models")
    ap.add_argument("--billed", type=float,
                    help="the console's dollar figure for the window, to print est/billed")
    args = ap.parse_args()

    end = dt.date.fromisoformat(args.day) if args.day else dt.datetime.now(dt.timezone.utc).date()
    days = {(end - dt.timedelta(days=i)).isoformat() for i in range(max(args.days, 1))}

    files = transcript_files(args.all_projects, args.project_dir or default_project_dir())
    if not files:
        sys.exit("No transcripts found. Use --project-dir or --all-projects.")
    prices = fetch_prices()
    data = aggregate(load_usage(files), days)
    if not data:
        sys.exit("No usage in the window %s..%s across %d transcript files."
                 % (min(days), max(days), len(files)))

    window = end.isoformat() if len(days) == 1 else "%s .. %s" % (min(days), end.isoformat())
    print("Window (UTC billing days): %s    transcript files: %d" % (window, len(files)))

    # --- actual usage, priced on the model that actually ran
    by_model = {}
    for day in data.values():
        for mid, tiers in day.items():
            for t, b in tiers.items():
                o = by_model.setdefault(mid, {}).setdefault(t, new_bucket())
                for k in o:
                    o[k] += b[k]
    total = merge_tiers(by_model.values())
    tot_read = sum(b["read"] for b in total.values())
    tot_w = sum(b["w5"] + b["w1"] for b in total.values())
    tot_out = sum(b["out"] for b in total.values())
    tot_n = sum(b["n"] for b in total.values())
    tot_ctx = sum(b["inp"] + b["read"] + b["w5"] + b["w1"] for b in total.values())
    print("Requests: %d   cache read: %.1fM   cache write: %.2fM   output: %.2fM"
          % (tot_n, tot_read / 1e6, tot_w / 1e6, tot_out / 1e6))
    print("Avg context per request: %dk tokens" % (tot_ctx / max(tot_n, 1) / 1000))

    print("\nWhat actually ran (estimated):")
    actual = 0.0
    unpriced = []
    order = sorted(by_model.items(), key=lambda kv: -sum(b["read"] for b in kv[1].values()))
    for mid, tiers in order:
        name = model_id_to_name(mid)
        n = sum(b["n"] for b in tiers.values())
        if name in prices and prices[name]["short"]:
            c, _ = model_cost(prices[name], tiers)
            actual += c
            print("  %-22s %5d requests  $%8.2f" % (name, n, c))
        else:
            unpriced.append(mid)
            print("  %-22s %5d requests  (no price found)" % (mid, n))
    print("  %-22s %5s           $%8.2f" % ("TOTAL", "", actual))
    if args.billed:
        print("  Billed figure given: $%.2f -> estimate/billed = %.2f"
              % (args.billed, actual / args.billed))
    if unpriced:
        print("  WARNING: no price for %s; totals exclude them." % ", ".join(unpriced))

    # --- same tokens, every candidate model
    print("\nSame token mix repriced on each current model (cheapest first):")
    print("  %-28s %10s %10s %9s %12s" % ("model", "cache rd $", "cost", "vs actual", "cache-rd %"))
    rows = []
    for name, e in prices.items():
        if e["retired"] or not e["short"] or (e["limited"] and not args.include_mythos):
            continue
        c, rd = model_cost(e, total)
        rows.append((c, name, e["short"]["read"], rd))
    for c, name, rdp, rd in sorted(rows):
        delta = "%+d%%" % round((c - actual) / actual * 100) if actual else "n/a"
        print("  %-28s %10s %10s %9s %11d%%" % (
            name, "$%.2f" % rdp, "$%.2f" % c, delta, round(rd / c * 100) if c else 0))

    if len(days) > 1:
        print("\nPer day (estimated, on the model that ran):")
        for day in sorted(data):
            c = 0.0
            for mid, tiers in data[day].items():
                name = model_id_to_name(mid)
                if name in prices and prices[name]["short"]:
                    c += model_cost(prices[name], tiers)[0]
            print("  %s  $%8.2f" % (day, c))

    print("\nNotes:")
    print("  - Prices fetched live from %s" % PRICING_URL)
    print("  - Repricing holds token counts fixed. A different model can use a different")
    print("    token count (tokenizer) and need more or fewer attempts; this is a ceiling")
    print("    on savings, not a promise. Judge cost per finished task, not per request.")
    print("  - Haiku 5.5 is priced per request by prompt length (>100k pays the higher tier).")
    if not args.all_projects:
        print("  - Only this repo's transcripts. Account-wide billing includes other projects,")
        print("    claude.ai chat, etc.; use --all-projects and --billed to reconcile.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Em dash sweep for Canvas courses.

CLAUDE.md standing rule: "No em dashes, ever - they render as &mdash; in Canvas.
Space-hyphen-space instead." This finds and optionally fixes literal U+2014 in
assignment names/descriptions and page bodies.

Why this exists: update_assignment and edit_page_content both do FULL replacement,
so fixing one character by hand means re-sending 8-12KB of HTML per item, with real
transcription risk in code blocks. This touches only the em dash character.

Granularity: hits are handled INDIVIDUALLY, not per item. An em dash sitting in
prose is fixed even when the same page has another one inside a <pre> block; the
one inside <pre> is reported and left alone. An earlier version skipped the whole
item, which stranded prose fixes behind unrelated code blocks.

Safety:
  * Dry run is the default. Nothing is written unless you pass --apply.
  * Every hit is reported with surrounding context, tagged [prose] or [CODE].
  * Content inside <pre> is NEVER altered unless you explicitly pass
    --include-pre, so shell/PowerShell/Python examples stay byte-identical.
  * After each write the item is re-fetched and its <pre> blocks are compared
    against the originals. Any drift is reported loudly as PRE CHANGED.
  * Page TITLES are never changed. Renaming a Canvas page alters its URL slug,
    which can break links. Fix those by hand, deliberately.

Usage:
    python tools/emdash_sweep.py --course 3644698                 # dry run
    python tools/emdash_sweep.py --course 3644698 --apply         # write prose only
    python tools/emdash_sweep.py --course 3644698 --include-pre   # show code hits
    python tools/emdash_sweep.py --course 3644698 --include-pre --apply

--include-pre rewrites em dashes INSIDE code blocks too. Only use it after
reading the [CODE] context lines from a dry run and confirming none of them is
part of an actual command.

Note: Canvas does not guarantee read-after-write consistency. A verification
re-fetch can return the pre-write copy, so a reported failure is worth
re-checking independently before you believe it.

On Windows, prefix with PYTHONIOENCODING=utf-8 so the console can print context.

Credentials are read from the canvas-mcp .env (CANVAS_API_URL, CANVAS_API_TOKEN).
"""

import argparse
import io
import json
import os
import re
import urllib.parse
import urllib.request

EM = "\u2014"
DEFAULT_ENV = r"C:\Users\cburk\canvas-mcp\.env"
PRE_RE = re.compile(r"<pre\b.*?</pre>", re.S | re.I)


def load_env(path):
    env = {}
    with io.open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


class Canvas:
    def __init__(self, base, token):
        base = base.rstrip("/")
        if base.endswith("/api/v1"):
            base = base[: -len("/api/v1")]
        self.base = base
        self.token = token

    def call(self, path, method="GET", payload=None):
        url = path if path.startswith("http") else self.base + "/api/v1" + path
        data = json.dumps(payload).encode("utf-8") if payload is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", "Bearer " + self.token)
        if data:
            req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.loads(r.read().decode("utf-8")), r.headers.get("Link", "")

    def paged(self, path):
        out, link = self.call(path)
        while link and 'rel="next"' in link:
            nxt = [p.split(";")[0].strip("<> ") for p in link.split(",") if 'rel="next"' in p]
            if not nxt:
                break
            more, link = self.call(nxt[0])
            out += more
        return out


def pre_blocks(text):
    """Every <pre> element, in order. Used to prove code survived a write."""
    return PRE_RE.findall(text or "")


def in_code_block(body, idx):
    """True if the character at idx sits inside a <pre> element."""
    return body.rfind("<pre", 0, idx) > body.rfind("</pre>", 0, idx)


def _sub(seg):
    return re.sub(r"\s*" + EM + r"\s*", " - ", seg)


def fix(text, include_pre=False):
    """Replace em dashes. Content inside <pre> is preserved unless include_pre.

    Returns (new_text, n_fixed, n_left_in_code).
    """
    if not text:
        return text, 0, 0
    if include_pre:
        return _sub(text), text.count(EM), 0

    out, last, fixed, left = [], 0, 0, 0
    for m in PRE_RE.finditer(text):
        seg = text[last:m.start()]
        fixed += seg.count(EM)
        out.append(_sub(seg))
        out.append(m.group(0))          # code block passes through untouched
        left += m.group(0).count(EM)
        last = m.end()
    tail = text[last:]
    fixed += tail.count(EM)
    out.append(_sub(tail))
    return "".join(out), fixed, left


def report(label, body, name, show_context):
    body = body or ""
    hits = [m.start() for m in re.finditer(EM, body)]
    name_hits = (name or "").count(EM)
    if not hits and not name_hits:
        return 0, 0, 0
    code = sum(1 for i in hits if in_code_block(body, i))
    prose = len(hits) - code
    print("  %-58s name:%d prose:%d code:%d" % (label[:58], name_hits, prose, code))
    if show_context:
        for i in hits:
            ctx = body[max(0, i - 55): i + 55].replace("\n", " ")
            tag = "[CODE] " if in_code_block(body, i) else "[prose]"
            print("     %s ...%s..." % (tag, ctx))
    return prose, code, name_hits


def verify(cv, path, original_pre, include_pre):
    """Re-fetch and report what survived. Canvas can serve a stale copy here."""
    chk, _ = cv.call(path)
    body = chk.get("body")
    if body is None:
        body = (chk.get("description") or "") + (chk.get("name") or "")
    now_pre = pre_blocks(body)
    ok = (now_pre == original_pre) or include_pre
    flag = "" if ok else "  *** PRE CHANGED, INSPECT THIS ITEM ***"
    print("     -> now %d em dashes | <pre> blocks %d%s"
          % (body.count(EM), len(now_pre), flag))
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True, help="Canvas numeric course ID")
    ap.add_argument("--apply", action="store_true", help="write changes (default is dry run)")
    ap.add_argument("--include-pre", action="store_true",
                    help="ALSO rewrite em dashes inside <pre> code blocks")
    ap.add_argument("--env", default=os.environ.get("CANVAS_ENV", DEFAULT_ENV))
    ap.add_argument("--quiet", action="store_true", help="suppress per-hit context")
    args = ap.parse_args()

    env = load_env(args.env)
    cv = Canvas(env["CANVAS_API_URL"], env["CANVAS_API_TOKEN"])
    course = args.course
    inc = args.include_pre
    f_prose = f_code = f_title = 0
    w_fixed = w_left = 0
    drift = []

    print("ASSIGNMENTS")
    for a in cv.paged("/courses/%s/assignments?per_page=100" % course):
        desc = a.get("description") or ""
        prose, code, nh = report(a.get("name") or "", desc, a.get("name") or "", not args.quiet)
        f_prose += prose
        f_code += code
        f_title += nh
        if not (prose or code or nh):
            continue
        if args.apply and (prose or nh or (code and inc)):
            orig_pre = pre_blocks(desc)
            new_desc, nfix, nleft = fix(desc, inc)
            payload = {"assignment": {"description": new_desc}}
            if nh:
                payload["assignment"]["name"] = _sub(a.get("name") or "")
            p = "/courses/%s/assignments/%s" % (course, a["id"])
            cv.call(p, "PUT", payload)
            if not verify(cv, p, orig_pre, inc):
                drift.append(a.get("name"))
            w_fixed += nfix + nh
            w_left += nleft

    print("PAGES")
    for pg in cv.paged("/courses/%s/pages?per_page=100" % course):
        slug = urllib.parse.quote(pg["url"], safe="")
        p = "/courses/%s/pages/%s" % (course, slug)
        full, _ = cv.call(p)
        body = full.get("body") or ""
        prose, code, nh = report(full.get("title") or pg["url"], body,
                                 full.get("title") or "", not args.quiet)
        f_prose += prose
        f_code += code
        f_title += nh
        if nh:
            print("     NOTE: em dash is in the PAGE TITLE. Not auto-fixed, because"
                  " renaming a page changes its URL slug. Fix by hand if you want it"
                  " changed.")
        if not (prose or (code and inc)):
            continue
        if args.apply:
            orig_pre = pre_blocks(body)
            new_body, nfix, nleft = fix(body, inc)
            cv.call(p, "PUT", {"wiki_page": {"body": new_body}})
            if not verify(cv, p, orig_pre, inc):
                drift.append(full.get("title"))
            w_fixed += nfix
            w_left += nleft

    print("-" * 78)
    print("Course %s | prose %d | in code blocks %d | in page titles %d"
          % (course, f_prose, f_code, f_title))
    if args.apply:
        note = " (none, --include-pre was set)" if inc else ""
        print("WROTE: %d fixed | %d left inside <pre>%s" % (w_fixed, w_left, note))
        if drift:
            print("*** <pre> CONTENT CHANGED IN %d ITEM(S): %s" % (len(drift), drift))
        else:
            print("All written items re-fetched with their <pre> blocks intact.")
    mode = "APPLY" if args.apply else "DRY RUN (no writes)"
    print("MODE:", mode + (" +include-pre" if inc else ""))


if __name__ == "__main__":
    main()

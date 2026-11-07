#!/usr/bin/env python3
"""
Em dash sweep for Canvas courses.

CLAUDE.md standing rule: "No em dashes, ever - they render as &mdash; in Canvas.
Space-hyphen-space instead." This finds and optionally fixes literal U+2014 in
assignment names/descriptions and page bodies.

Why this exists: update_assignment and edit_page_content both do FULL replacement,
so fixing one character by hand means re-sending 8-12KB of HTML per item, with real
transcription risk in code blocks. This touches only the em dash character.

Safety:
  * Dry run is the default. Nothing is written unless you pass --apply.
  * Every hit is reported with surrounding context before any write.
  * Hits inside <pre> code blocks are DETECTED AND SKIPPED, so shell/PowerShell/
    Python examples are never altered.
  * After each write the item is re-fetched: em dash count and <pre> open/close
    balance are printed so you can confirm nothing was damaged.
  * Page TITLES are never changed. Renaming a Canvas page alters its URL slug,
    which can break links. Fix those by hand, deliberately.

Usage:
    python emdash_sweep.py --course 3644698              # dry run
    python emdash_sweep.py --course 3644698 --apply      # write

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


def in_code_block(body, idx):
    """True if the character at idx sits inside a <pre> element."""
    return body.rfind("<pre", 0, idx) > body.rfind("</pre>", 0, idx)


def fix(text):
    """Collapse any whitespace around an em dash into a single space-hyphen-space."""
    return re.sub(r"\s*" + EM + r"\s*", " - ", text or "")


def report(label, body, name, show_context):
    body = body or ""
    hits = [m.start() for m in re.finditer(EM, body)]
    name_hits = (name or "").count(EM)
    if not hits and not name_hits:
        return 0, 0, False
    unsafe = any(in_code_block(body, i) for i in hits)
    print("  %-62s name:%d body:%d%s"
          % (label[:62], name_hits, len(hits), "   <<< INSIDE CODE BLOCK, SKIPPED" if unsafe else ""))
    if show_context:
        for i in hits:
            ctx = body[max(0, i - 55): i + 55].replace("\n", " ")
            print("     %s ...%s..." % ("[CODE]" if in_code_block(body, i) else "[prose]", ctx))
    return len(hits), name_hits, unsafe


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--course", required=True, help="Canvas numeric course ID")
    ap.add_argument("--apply", action="store_true", help="write changes (default is dry run)")
    ap.add_argument("--env", default=os.environ.get("CANVAS_ENV", DEFAULT_ENV))
    ap.add_argument("--quiet", action="store_true", help="suppress per-hit context")
    args = ap.parse_args()

    env = load_env(args.env)
    cv = Canvas(env["CANVAS_API_URL"], env["CANVAS_API_TOKEN"])
    course = args.course
    found = fixed = skipped = 0

    print("ASSIGNMENTS")
    for a in cv.paged("/courses/%s/assignments?per_page=100" % course):
        b, nh, unsafe = report(a.get("name") or "", a.get("description") or "",
                               a.get("name") or "", not args.quiet)
        found += b + nh
        if unsafe:
            skipped += b + nh
            continue
        if args.apply and (b or nh):
            payload = {"assignment": {"description": fix(a.get("description"))}}
            if nh:
                payload["assignment"]["name"] = fix(a.get("name"))
            cv.call("/courses/%s/assignments/%s" % (course, a["id"]), "PUT", payload)
            chk, _ = cv.call("/courses/%s/assignments/%s" % (course, a["id"]))
            d = chk.get("description") or ""
            print("     -> now %d em dashes | <pre> %d/%d balanced"
                  % (d.count(EM) + (chk.get("name") or "").count(EM), d.count("<pre"), d.count("</pre>")))
            fixed += b + nh

    print("PAGES")
    for p in cv.paged("/courses/%s/pages?per_page=100" % course):
        slug = urllib.parse.quote(p["url"], safe="")
        full, _ = cv.call("/courses/%s/pages/%s" % (course, slug))
        b, nh, unsafe = report(full.get("title") or p["url"], full.get("body") or "",
                               full.get("title") or "", not args.quiet)
        found += b + nh
        if nh:
            print("     NOTE: em dash is in the PAGE TITLE. Not auto-fixed, because renaming"
                  " a page changes its URL slug. Fix by hand if you want it changed.")
            skipped += nh
        if unsafe:
            skipped += b
            continue
        if args.apply and b:
            cv.call("/courses/%s/pages/%s" % (course, slug), "PUT",
                    {"wiki_page": {"body": fix(full.get("body"))}})
            chk, _ = cv.call("/courses/%s/pages/%s" % (course, slug))
            nb = chk.get("body") or ""
            print("     -> now %d em dashes | <pre> %d/%d balanced"
                  % (nb.count(EM), nb.count("<pre"), nb.count("</pre>")))
            fixed += b

    print("-" * 78)
    print("Course %s | found %d | fixed %d | skipped %d (code blocks and page titles)"
          % (course, found, fixed, skipped))
    print("MODE:", "APPLY" if args.apply else "DRY RUN (no writes)")


if __name__ == "__main__":
    main()

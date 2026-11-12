#!/usr/bin/env python3
"""Low-context Canvas REST sync tool for pages, assignments, and course-wide linting.

Why this exists:
  Passing 25-35 KB of inline-styled HTML through MCP tool calls (get_page_content,
  edit_page_content, update_assignment) puts 3-4 copies of the raw HTML into the
  LLM conversation history (~100k tokens per page edit). This tool moves HTML bodies
  directly between local disk (e.g. scratchpad/) and the Canvas REST API, printing
  only a compact 4-line summary to stdout.

Safety:
  * Every push runs canvas_lint.lint_html() BEFORE sending to Canvas and refuses
    to write if any ERROR is detected (override with --force).
  * Every push compares <pre> blocks before and after to catch code corruption.
  * Reads credentials from C:\\Users\\cburk\\canvas-mcp\\.env by default.

Usage:
  python tools/canvas_sync.py list-pages --course BIT360 [--filter "Week 1"]
  python tools/canvas_sync.py list-assignments --course BIT360
  python tools/canvas_sync.py pull-page --course BIT360 --page <slug> -o scratchpad/p1.html
  python tools/canvas_sync.py push-page --course BIT360 --page <slug> -i scratchpad/p1.html [--title "..."] [--publish|--unpublish]
  python tools/canvas_sync.py create-page --course BIT360 --title "Week 1 | Page 1" -i scratchpad/p1.html [--publish]
  python tools/canvas_sync.py pull-assignment --course BIT360 --assignment <id> -o scratchpad/a1.html
  python tools/canvas_sync.py push-assignment --course BIT360 --assignment <id> -i scratchpad/a1.html [--name "..."]
  python tools/canvas_sync.py lint-course --course BIT360
"""

import argparse
import io
import json
import os
import re
import sys
import urllib.parse
import urllib.request

from canvas_lint import lint_html, format_report, PRE_RE

DEFAULT_ENV = r"C:\Users\cburk\canvas-mcp\.env"

COURSES = {
    "BIT221": "3631198",
    "BIT281": "3631199",
    "BIT320": "3644698",
    "BIT351": "3631200",
    "BIT360": "3644702",
    "PRO221": "3631288",
    "PRO352": "3631317",
    "ITH216": "3646987",
}

HEADING_RE = re.compile(r"<h([1-3])\b[^>]*>(.*?)</h\1>", re.I | re.S)
TAG_STRIP_RE = re.compile(r"<[^>]+>")


def load_env(path):
    env = {}
    if os.path.exists(path):
        with io.open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    k, v = line.split("=", 1)
                    env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def resolve_course(course_arg):
    key = course_arg.strip().upper()
    return COURSES.get(key, course_arg.strip())


class CanvasClient:
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
        if data is not None:
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
            out.extend(more)
        return out


def extract_headings(html):
    out = []
    for m in HEADING_RE.finditer(html or ""):
        lvl = m.group(1)
        text = TAG_STRIP_RE.sub("", m.group(2))
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            out.append(f"H{lvl}: {text}")
    return out


def summarize_html(html):
    html = html or ""
    words = len(re.findall(r"\S+", TAG_STRIP_RE.sub(" ", html)))
    pres = len(PRE_RE.findall(html))
    headings = extract_headings(html)
    h_preview = " | ".join(headings[:6]) + (f" (+{len(headings) - 6} more)" if len(headings) > 6 else "")
    return f"{len(html):,} chars (~{words:,} words, {pres} <pre> blocks)\n  Headings: {h_preview or 'none'}"


def cmd_list_pages(cv, args):
    course = resolve_course(args.course)
    pages = cv.paged(f"/courses/{course}/pages?per_page=100")
    flt = (args.filter or "").lower()
    if flt:
        pages = [p for p in pages if flt in (p.get("title") or "").lower() or flt in (p.get("url") or "").lower()]
    print(f"Course {course}: {len(pages)} page(s)")
    for p in sorted(pages, key=lambda x: x.get("title") or ""):
        pub = "PUB  " if p.get("published") else "unpub"
        print(f"  [{pub}] id:{p.get('page_id', '-'):<8} slug:{p.get('url', '')}  title:{p.get('title', '')}")


def cmd_list_assignments(cv, args):
    course = resolve_course(args.course)
    asns = cv.paged(f"/courses/{course}/assignments?per_page=100")
    flt = (args.filter or "").lower()
    if flt:
        asns = [a for a in asns if flt in (a.get("name") or "").lower()]
    print(f"Course {course}: {len(asns)} assignment(s)")
    for a in asns:
        pub = "PUB  " if a.get("published") else "unpub"
        pts = a.get("points_possible")
        due = (a.get("due_at") or "none")[:10]
        print(f"  [{pub}] id:{a.get('id'):<9} pts:{str(pts):<5} due:{due}  {a.get('name', '')}")


def cmd_pull_page(cv, args):
    course = resolve_course(args.course)
    slug = urllib.parse.quote(args.page, safe="")
    data, _ = cv.call(f"/courses/{course}/pages/{slug}")
    body = data.get("body") or ""
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with io.open(args.output, "w", encoding="utf-8") as f:
        f.write(body)
    issues = lint_html(body, item_type="page", title=data.get("title") or "")
    print(f"PULLED PAGE -> {args.output}")
    print(f"  Title: {data.get('title')} | Slug: {data.get('url')} | Published: {data.get('published')}")
    print(f"  Size:  {summarize_html(body)}")
    print("  " + format_report(issues))


def cmd_push_page(cv, args, create=False):
    course = resolve_course(args.course)
    with io.open(args.input, "r", encoding="utf-8") as f:
        body = f.read()

    issues = lint_html(body, item_type="page", title=args.title or "")
    errors = [i for i in issues if i["severity"] == "ERROR"]
    if errors and not args.force:
        print(format_report(issues, label=args.input))
        sys.exit("ABORTED: Fix lint errors above before pushing (or pass --force).")

    wiki_page = {"body": body}
    if args.title:
        wiki_page["title"] = args.title
    if args.publish:
        wiki_page["published"] = True
    elif args.unpublish:
        wiki_page["published"] = False

    orig_pre = PRE_RE.findall(body)
    if create:
        if not args.title:
            sys.exit("ERROR: --title is required for create-page")
        if not args.publish and not args.unpublish:
            wiki_page["published"] = False
        res, _ = cv.call(f"/courses/{course}/pages", "POST", {"wiki_page": wiki_page})
    else:
        slug = urllib.parse.quote(args.page, safe="")
        res, _ = cv.call(f"/courses/{course}/pages/{slug}", "PUT", {"wiki_page": wiki_page})

    res_body = res.get("body") or ""
    now_pre = PRE_RE.findall(res_body)
    pre_status = "OK" if len(now_pre) == len(orig_pre) else f"MISMATCH ({len(orig_pre)} -> {len(now_pre)})"
    action = "CREATED" if create else "UPDATED"
    print(f"{action} PAGE: {res.get('title')} (slug: {res.get('url')}, page_id: {res.get('page_id')})")
    print(f"  Published: {res.get('published')} | Size: {len(res_body):,} chars | <pre> check: {pre_status}")
    if issues:
        print("  " + format_report(issues))


def cmd_pull_assignment(cv, args):
    course = resolve_course(args.course)
    data, _ = cv.call(f"/courses/{course}/assignments/{args.assignment}")
    desc = data.get("description") or ""
    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with io.open(args.output, "w", encoding="utf-8") as f:
        f.write(desc)
    issues = lint_html(desc, item_type="assignment", title=data.get("name") or "")
    print(f"PULLED ASSIGNMENT -> {args.output}")
    print(f"  Name: {data.get('name')} | ID: {data.get('id')} | Points: {data.get('points_possible')} | Published: {data.get('published')}")
    print(f"  Size: {summarize_html(desc)}")
    print("  " + format_report(issues))


def cmd_push_assignment(cv, args):
    course = resolve_course(args.course)
    with io.open(args.input, "r", encoding="utf-8") as f:
        desc = f.read()

    issues = lint_html(desc, item_type="assignment", title=args.name or "")
    errors = [i for i in issues if i["severity"] == "ERROR"]
    if errors and not args.force:
        print(format_report(issues, label=args.input))
        sys.exit("ABORTED: Fix lint errors above before pushing (or pass --force).")

    payload = {"description": desc}
    if args.name:
        payload["name"] = args.name
    if args.points is not None:
        payload["points_possible"] = args.points
    if args.publish:
        payload["published"] = True
    elif args.unpublish:
        payload["published"] = False

    orig_pre = PRE_RE.findall(desc)
    res, _ = cv.call(f"/courses/{course}/assignments/{args.assignment}", "PUT", {"assignment": payload})
    res_desc = res.get("description") or ""
    now_pre = PRE_RE.findall(res_desc)
    pre_status = "OK" if len(now_pre) == len(orig_pre) else f"MISMATCH ({len(orig_pre)} -> {len(now_pre)})"
    print(f"UPDATED ASSIGNMENT: {res.get('name')} (id: {res.get('id')})")
    print(f"  Published: {res.get('published')} | Points: {res.get('points_possible')} | Size: {len(res_desc):,} chars | <pre> check: {pre_status}")
    if issues:
        print("  " + format_report(issues))


def cmd_lint_course(cv, args):
    course = resolve_course(args.course)
    total_err = 0
    total_warn = 0
    flagged = 0

    asns = cv.paged(f"/courses/{course}/assignments?per_page=100")
    pages = cv.paged(f"/courses/{course}/pages?per_page=100")
    print(f"Auditing course {course}: {len(asns)} assignments, {len(pages)} pages...")

    for a in asns:
        issues = lint_html(a.get("description") or "", item_type="assignment", title=a.get("name") or "")
        if issues:
            flagged += 1
            total_err += sum(1 for i in issues if i["severity"] == "ERROR")
            total_warn += sum(1 for i in issues if i["severity"] == "WARN")
            print(format_report(issues, label=f"Assignment {a.get('id')}: {a.get('name')}"))

    for pg in pages:
        slug = urllib.parse.quote(pg["url"], safe="")
        full, _ = cv.call(f"/courses/{course}/pages/{slug}")
        issues = lint_html(full.get("body") or "", item_type="page", title=full.get("title") or "")
        if issues:
            flagged += 1
            total_err += sum(1 for i in issues if i["severity"] == "ERROR")
            total_warn += sum(1 for i in issues if i["severity"] == "WARN")
            print(format_report(issues, label=f"Page {pg.get('url')}: {full.get('title')}"))

    print("-" * 72)
    print(f"Course {course} lint summary: {flagged} item(s) flagged | {total_err} error(s) | {total_warn} warning(s)")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--env", default=os.environ.get("CANVAS_ENV", DEFAULT_ENV))
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_lp = sub.add_parser("list-pages")
    p_lp.add_argument("--course", required=True)
    p_lp.add_argument("--filter", help="Case-insensitive title/slug substring")

    p_la = sub.add_parser("list-assignments")
    p_la.add_argument("--course", required=True)
    p_la.add_argument("--filter", help="Case-insensitive name substring")

    p_pull_p = sub.add_parser("pull-page")
    p_pull_p.add_argument("--course", required=True)
    p_pull_p.add_argument("--page", required=True, help="Page URL slug or page_id")
    p_pull_p.add_argument("-o", "--output", required=True, help="Output HTML file path")

    p_push_p = sub.add_parser("push-page")
    p_push_p.add_argument("--course", required=True)
    p_push_p.add_argument("--page", required=True, help="Page URL slug or page_id")
    p_push_p.add_argument("-i", "--input", required=True, help="Input HTML file path")
    p_push_p.add_argument("--title", help="Optional new title")
    p_push_p.add_argument("--publish", action="store_true")
    p_push_p.add_argument("--unpublish", action="store_true")
    p_push_p.add_argument("--force", action="store_true", help="Push even if lint errors exist")

    p_create_p = sub.add_parser("create-page")
    p_create_p.add_argument("--course", required=True)
    p_create_p.add_argument("--title", required=True, help="New page title")
    p_create_p.add_argument("-i", "--input", required=True, help="Input HTML file path")
    p_create_p.add_argument("--publish", action="store_true")
    p_create_p.add_argument("--unpublish", action="store_true")
    p_create_p.add_argument("--force", action="store_true")

    p_pull_a = sub.add_parser("pull-assignment")
    p_pull_a.add_argument("--course", required=True)
    p_pull_a.add_argument("--assignment", required=True, help="Numeric assignment ID")
    p_pull_a.add_argument("-o", "--output", required=True, help="Output HTML file path")

    p_push_a = sub.add_parser("push-assignment")
    p_push_a.add_argument("--course", required=True)
    p_push_a.add_argument("--assignment", required=True, help="Numeric assignment ID")
    p_push_a.add_argument("-i", "--input", required=True, help="Input HTML file path")
    p_push_a.add_argument("--name", help="Optional new assignment name")
    p_push_a.add_argument("--points", type=float, help="Optional points_possible")
    p_push_a.add_argument("--publish", action="store_true")
    p_push_a.add_argument("--unpublish", action="store_true")
    p_push_a.add_argument("--force", action="store_true")

    p_lc = sub.add_parser("lint-course")
    p_lc.add_argument("--course", required=True)

    args = ap.parse_args()
    env = load_env(args.env)
    api_url = os.environ.get("CANVAS_API_URL") or env.get("CANVAS_API_URL", "https://lms.neumont.edu/api/v1")
    api_token = os.environ.get("CANVAS_API_TOKEN") or env.get("CANVAS_API_TOKEN", "")
    if not api_token:
        sys.exit(f"ERROR: CANVAS_API_TOKEN not found in environment or {args.env}")

    cv = CanvasClient(api_url, api_token)
    dispatch = {
        "list-pages": cmd_list_pages,
        "list-assignments": cmd_list_assignments,
        "pull-page": cmd_pull_page,
        "push-page": lambda c, a: cmd_push_page(c, a, create=False),
        "create-page": lambda c, a: cmd_push_page(c, a, create=True),
        "pull-assignment": cmd_pull_assignment,
        "push-assignment": cmd_push_assignment,
        "lint-course": cmd_lint_course,
    }
    dispatch[args.cmd](cv, args)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Query Canvas for all pages in a course and analyze weekly coverage.

Reads credentials from the canvas-mcp .env file (same as tools/emdash_sweep.py)
and accepts either a numeric Canvas course ID or a course code (e.g. BIT360, ITH216).

Usage:
    python tools/audit_canvas_pages.py --course BIT360
    python tools/audit_canvas_pages.py --course 3646987
"""

import argparse
import io
import json
import os
import re
import sys
import urllib.request

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
    return COURSES.get(key, course_arg.strip()), key if key in COURSES else course_arg


def fetch_paged(base_url, token, path):
    base = base_url.rstrip("/")
    if base.endswith("/api/v1"):
        base = base[: -len("/api/v1")]
    url = base + "/api/v1" + path
    out = []
    while url:
        req = urllib.request.Request(url, headers={"Authorization": "Bearer " + token})
        with urllib.request.urlopen(req, timeout=60) as r:
            out.extend(json.loads(r.read().decode("utf-8")))
            link = r.headers.get("Link", "")
        nxt = [p.split(";")[0].strip("<> ") for p in link.split(",") if 'rel="next"' in p]
        url = nxt[0] if nxt else None
    return out


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--course", default="3646987",
                    help="Canvas course ID or code (e.g. BIT360, ITH216, 3646987)")
    ap.add_argument("--weeks", type=int, default=10,
                    help="Number of weeks in the course (default: 10; use 5 for 5-week courses)")
    ap.add_argument("--env", default=os.environ.get("CANVAS_ENV", DEFAULT_ENV))
    args = ap.parse_args()

    env = load_env(args.env)
    api_url = os.environ.get("CANVAS_API_URL") or env.get("CANVAS_API_URL", "https://lms.neumont.edu/api/v1")
    api_token = os.environ.get("CANVAS_API_TOKEN") or env.get("CANVAS_API_TOKEN", "")
    if not api_token:
        sys.exit("ERROR: CANVAS_API_TOKEN not set in environment or %s" % args.env)

    course_id, label = resolve_course(args.course)
    print("=" * 80)
    print("Canvas Pages Audit - Course %s (ID: %s)" % (label, course_id))
    print("=" * 80)

    pages = fetch_paged(api_url, api_token, "/courses/%s/pages?per_page=100" % course_id)
    if not pages:
        print("No pages found.")
        return False

    weeks = {i: [] for i in range(1, args.weeks + 1)}
    navigation = []
    instructor = []
    older_ref = []
    other = []

    for page in pages:
        title = page.get("title", "Unknown")
        published = page.get("published", False)
        page_id = page.get("page_id", "unknown")
        slug = page.get("url", "")
        info = {"title": title, "published": published, "id": page_id, "url": slug}

        if any(x in title.lower() for x in ("instructor", "lecture notes", "teaching notes", "answer key", "code-along guide")):
            instructor.append(info)
            continue

        m = re.search(r"\bWeek\s+(\d+)\b", title, re.I)
        if m and int(m.group(1)) in weeks:
            weeks[int(m.group(1))].append(info)
        elif title in ("Home", "Remote Learning") or "Course Outline" in title:
            navigation.append(info)
        elif any(x in title for x in ("Definition", "Notes:", "Guide", "Cisco", "Troubleshoot", "RETIRED")):
            older_ref.append(info)
        else:
            other.append(info)

    print("\nSTUDENT PAGES BY WEEK")
    print("-" * 80)
    for w in range(1, args.weeks + 1):
        items = sorted(weeks[w], key=lambda x: x["title"])
        pub = sum(1 for p in items if p["published"])
        print("\nWeek %d (%d published / %d total):" % (w, pub, len(items)))
        for p in items:
            mark = "[PUB]  " if p["published"] else "[unpub]"
            print("  %s [id:%-8s] %s  (%s)" % (mark, p["id"], p["title"], p["url"]))

    for heading, bucket in (
        ("INSTRUCTOR / LECTURE NOTES", instructor),
        ("NAVIGATION / COURSE OUTLINE", navigation),
        ("OLDER / REFERENCE / RETIRED", older_ref),
        ("OTHER PAGES", other),
    ):
        if bucket:
            print("\n%s (%d)" % (heading, len(bucket)))
            print("-" * 80)
            for p in sorted(bucket, key=lambda x: x["title"]):
                mark = "[PUB]  " if p["published"] else "[unpub]"
                print("  %s [id:%-8s] %s  (%s)" % (mark, p["id"], p["title"], p["url"]))

    pub_count = sum(1 for p in pages if p.get("published"))
    print("\n" + "=" * 80)
    print("SUMMARY: %d total pages | %d published | %d unpublished"
          % (len(pages), pub_count, len(pages) - pub_count))
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)

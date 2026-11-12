#!/usr/bin/env python3
"""Set up the Participation Quizzes for any course, in one command.

For a course config (quizzes/participation/<CODE>.json) this creates, per week and
per class day (Mon-Fri):

  1. Quizzes     "Participation Quiz - Week N Day": ungraded survey, one question,
                 anonymous submissions off, one attempt, its own access code,
                 UNPUBLISHED.
  2. Modules     each quiz appended to its week's Canvas module.
  3. Instructor  an UNPUBLISHED page "Instructor - Participation Quiz Codes" listing
                 every quiz title, quiz ID and access code.

Every step is idempotent: existing quizzes are skipped (or re-coded with
--update-codes), quizzes already in a module are not re-added, and the instructor
page is updated in place. Re-running after a partial failure is safe.

Dry run by default. Nothing is written to Canvas without --apply.

Access codes live in <config>.codes.json (gitignored: the repo is public and the
codes are student-facing), keyed by quiz title. Each code is one word, 3-30 letters
or digits, unique within the course.

Config (<CODE>.json):
    {
      "course_code": "ITH216",
      "course_id": "3646987",
      "weeks": 10,
      "module_name": "Week {week}",            (optional; default shown)
      "weeks_data": [
        {"week": 1, "topic": "...", "question": "...", "options": ["a", "b", "c"]},
        ...
      ]
    }
  "weeks" must be 5 or 10 and weeks_data must cover weeks 1..N. Each entry needs
  2-6 options. Question and option text must not contain em dashes.

Usage:
  python tools/create_participation_quizzes.py --config quizzes/participation/<CODE>.json
  python tools/create_participation_quizzes.py --config quizzes/participation/<CODE>.json --apply
  python tools/create_participation_quizzes.py --config quizzes/participation/<CODE>.json --apply --only-week 1
  python tools/create_participation_quizzes.py --config quizzes/participation/<CODE>.json --apply --update-codes

--only-week limits quiz and module steps to one week and skips the instructor page
(which always lists the whole course). --skip-modules and --skip-page turn off those steps.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canvas_sync import CanvasClient, load_env, DEFAULT_ENV  # noqa: E402

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
TITLE_PREFIX = "Participation Quiz"
PAGE_TITLE = "Instructor Notes - Participation Quiz Codes"  # matches the course's "Instructor Notes - ..." convention
PAGE_TITLE_RE = re.compile(r"^Instructor( Notes)? - Participation Quiz Codes$")
CODE_RE = re.compile(r"^[A-Za-z0-9]{3,30}$")
DEFAULT_MODULE_NAME = "Week {week}"


# --------------------------------------------------------------------------- config

def quiz_title(week, day):
    return f"{TITLE_PREFIX} - Week {week} {day}"


def validate_config(cfg):
    errors = []
    for key in ("course_code", "course_id", "weeks", "weeks_data"):
        if key not in cfg:
            errors.append(f"missing '{key}'")
    if errors:
        return errors
    weeks = cfg["weeks"]
    data = cfg["weeks_data"]
    if weeks not in (5, 10):
        errors.append(f"'weeks' must be 5 or 10, got {weeks!r}")
    if len(data) != weeks:
        errors.append(f"'weeks' is {weeks} but weeks_data has {len(data)} entries")
    seen = set()
    for entry in data:
        w = entry.get("week")
        if w in seen:
            errors.append(f"duplicate week {w}")
        seen.add(w)
        opts = entry.get("options", [])
        if not 2 <= len(opts) <= 6:
            errors.append(f"week {w}: needs 2-6 options, has {len(opts)}")
        for text in [entry.get("question", "")] + opts:
            if "\u2014" in text or "&mdash;" in text:
                errors.append(f"week {w}: em dash found in question or option text")
    expected = set(range(1, weeks + 1)) if isinstance(weeks, int) else set()
    if seen != expected:
        errors.append(f"weeks_data must cover weeks {sorted(expected)}, has {sorted(seen)}")
    return errors


def plan(cfg):
    """(week, day, title, week_entry) for every quiz in calendar order."""
    by_week = {e["week"]: e for e in cfg["weeks_data"]}
    return [(w, day, quiz_title(w, day), by_week[w])
            for w in range(1, cfg["weeks"] + 1) for day in DAYS]


def validate_codes(codes, rows):
    """Every planned quiz needs its own code: one word, unique across the course."""
    errors = []
    by_code = {}
    for _, _, title, _ in rows:
        code = codes.get(title)
        if not code:
            errors.append(f"no access code for '{title}'")
            continue
        if not CODE_RE.match(code):
            errors.append(f"'{title}': code '{code}' must be 3-30 letters/digits, no spaces")
        by_code.setdefault(code.upper(), []).append(title)
    for code, titles in by_code.items():
        if len(titles) > 1:
            errors.append(f"code '{code}' is used by {len(titles)} quizzes; codes must be unique")
    return errors


# --------------------------------------------------------------------------- Canvas

def existing_quizzes(cv, cid):
    """title -> quiz dict, for participation quizzes already in the course."""
    quizzes = cv.paged(f"/courses/{cid}/quizzes?per_page=100")
    return {q["title"]: q for q in quizzes if q["title"].startswith(TITLE_PREFIX)}


def set_access_code(cv, cid, quiz_id, code):
    cv.call(f"/courses/{cid}/quizzes/{quiz_id}", method="PUT",
            payload={"quiz": {"access_code": code}})


def create_quiz(cv, cid, title, week_entry, code):
    description = (
        f"<p>Participation check for Week {week_entry['week']}. Answer the question below to "
        "record your attendance for today. This is an ungraded survey, so there is no "
        "correct answer.</p>"
    )
    payload = {
        "quiz": {
            "title": title,
            "quiz_type": "survey",
            "description": description,
            "access_code": code,
            "anonymous_submissions": False,
            "show_correct_answers": False,
            "allowed_attempts": 1,
            "shuffle_answers": False,
            "one_question_at_a_time": False,
            "published": False,
        }
    }
    quiz, _ = cv.call(f"/courses/{cid}/quizzes", method="POST", payload=payload)
    quiz_id = quiz["id"]
    try:
        q_payload = {
            "question": {
                "question_name": f"Week {week_entry['week']} participation question",
                "question_text": f"<p>{week_entry['question']}</p>",
                "question_type": "multiple_choice_question",
                "points_possible": 0,
                # Canvas forces one answer to weight 100 on multiple choice even in a survey.
                "answers": [{"answer_text": opt, "answer_weight": 0} for opt in week_entry["options"]],
            }
        }
        cv.call(f"/courses/{cid}/quizzes/{quiz_id}/questions", method="POST", payload=q_payload)
    except Exception:
        # Do not leave a half-built quiz behind; a re-run can then create it cleanly.
        cv.call(f"/courses/{cid}/quizzes/{quiz_id}", method="DELETE")
        raise
    return quiz_id


def course_modules(cv, cid):
    """casefolded module name -> module id."""
    modules = cv.paged(f"/courses/{cid}/modules?per_page=100")
    return {m["name"].strip().casefold(): m["id"] for m in modules}


def module_quiz_ids(cv, cid, module_id):
    items = cv.paged(f"/courses/{cid}/modules/{module_id}/items?per_page=100")
    return {i.get("content_id") for i in items if i.get("type") == "Quiz"}


def add_quiz_to_module(cv, cid, module_id, quiz_id, title):
    cv.call(f"/courses/{cid}/modules/{module_id}/items", method="POST",
            payload={"module_item": {"type": "Quiz", "content_id": quiz_id, "title": title}})


def find_page_slug(cv, cid):
    """Slug of the existing instructor code page, matched by title (any Instructor/Instructor Notes prefix)."""
    pages = cv.paged(f"/courses/{cid}/pages?search_term={urllib.parse.quote('Participation Quiz Codes')}&per_page=100")
    for p in pages:
        if PAGE_TITLE_RE.match(p.get("title", "")):
            return p.get("url")
    return None


def build_code_page(cfg, rows, quiz_ids, codes):
    """Instructor-only table of every quiz, its ID and its access code. Inline styles only."""
    body_rows = []
    for n, (_, _, title, _) in enumerate(rows):
        bg = "#ffffff" if n % 2 == 0 else "#F1EFE8"
        qid = quiz_ids[title]
        body_rows.append(
            f'<tr><td style="padding: 6px 8px; background-color: {bg};">{title}</td>'
            f'<td style="padding: 6px 8px; background-color: {bg};">{qid}</td>'
            f'<td style="padding: 6px 8px; background-color: {bg};"><code style="font-size: 15px;">{codes[title]}</code></td></tr>'
        )
    n_quizzes = len(rows)
    return f'''<h2 style="color: #2C2C2A;">Participation Quiz Access Codes (Instructor Only)</h2>
<p style="color: #2C2C2A;">Each Participation Quiz has its own access code, a course keyword for that day. Give students the code for the day in person during class. Do not post these codes anywhere students can see them.</p>
<p style="color: #2C2C2A;">All {n_quizzes} quizzes are ungraded surveys (no correct answer, no points), created unpublished. Publish each quiz manually on the day class is held, and share that day's code only then.</p>
<table style="width: 100%; border-collapse: collapse; border: 1px solid #B4B2A9;">
<thead>
<tr>
<th style="background-color: #444441; color: #ffffff; padding: 8px; text-align: left;">Quiz title</th>
<th style="background-color: #444441; color: #ffffff; padding: 8px; text-align: left;">Quiz ID</th>
<th style="background-color: #444441; color: #ffffff; padding: 8px; text-align: left;">Access code</th>
</tr>
</thead>
<tbody>
{chr(10).join(body_rows)}
</tbody>
</table>
'''


# --------------------------------------------------------------------------- main

def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--config", required=True, help="Course participation JSON config")
    ap.add_argument("--codes", help="Access code map (default: <config> with .codes.json suffix)")
    ap.add_argument("--apply", action="store_true", help="Write to Canvas (default: dry run)")
    ap.add_argument("--only-week", type=int, help="Limit quiz and module steps to one week")
    ap.add_argument("--update-codes", action="store_true",
                    help="Set access codes on quizzes that already exist")
    ap.add_argument("--skip-modules", action="store_true", help="Do not add quizzes to modules")
    ap.add_argument("--skip-page", action="store_true", help="Do not write the instructor code page")
    ap.add_argument("--env", default=os.environ.get("CANVAS_ENV", DEFAULT_ENV))
    args = ap.parse_args()

    with open(args.config, "r", encoding="utf-8") as f:
        cfg = json.load(f)
    errors = validate_config(cfg)
    if errors:
        sys.exit("Config errors:\n  " + "\n  ".join(errors))

    all_rows = plan(cfg)
    codes_path = args.codes or re.sub(r"\.json$", ".codes.json", args.config)
    if not os.path.exists(codes_path):
        sys.exit(f"ERROR: access code file not found: {codes_path} (gitignored; create it locally)")
    with open(codes_path, "r", encoding="utf-8") as f:
        codes = json.load(f)
    errors = validate_codes(codes, all_rows)  # always the whole course, even for --only-week
    if errors:
        sys.exit("Access code errors:\n  " + "\n  ".join(errors))

    rows = [r for r in all_rows if not args.only_week or r[0] == args.only_week]
    cid = str(cfg["course_id"])
    module_name_fmt = cfg.get("module_name", DEFAULT_MODULE_NAME)

    env = load_env(args.env)
    api_url = os.environ.get("CANVAS_API_URL") or env.get("CANVAS_API_URL", "https://lms.neumont.edu/api/v1")
    api_token = os.environ.get("CANVAS_API_TOKEN") or env.get("CANVAS_API_TOKEN", "")
    if not api_token:
        sys.exit(f"ERROR: CANVAS_API_TOKEN not found in environment or {args.env}")
    cv = CanvasClient(api_url, api_token)

    mode = "APPLY" if args.apply else "DRY RUN - nothing will be written"
    print(f"{cfg['course_code']} (course {cid}) - {mode}")

    # Preflight: resolve modules before any write, so a missing module stops the run early.
    modules = {}
    if not args.skip_modules:
        modules = course_modules(cv, cid)
        for w in sorted({r[0] for r in rows}):
            name = module_name_fmt.format(week=w)
            if name.strip().casefold() not in modules:
                sys.exit(f"ERROR: no Canvas module named '{name}' in course {cid}. "
                         "Create it or set 'module_name' in the config (use --skip-modules to skip).")

    failed = 0

    # Step 1: quizzes
    existing = existing_quizzes(cv, cid)
    print(f"\n[1] Quizzes: {len(rows)} planned, {len(existing)} participation quizzes already in Canvas")
    created = updated = skipped = 0
    for w, day, title, entry in rows:
        if title in existing:
            qid = existing[title]["id"]
            if args.update_codes:
                if args.apply:
                    try:
                        set_access_code(cv, cid, qid, codes[title])
                        print(f"  CODE    {title} (id {qid})")
                        updated += 1
                    except Exception as e:  # noqa: BLE001
                        print(f"  FAIL    {title}: {e}")
                        failed += 1
                else:
                    print(f"  PLAN    set code on {title} (id {qid})")
            else:
                print(f"  SKIP    {title} (exists, id {qid})")
                skipped += 1
            continue
        if not args.apply:
            print(f"  PLAN    create {title}")
            continue
        try:
            qid = create_quiz(cv, cid, title, entry, codes[title])
            print(f"  CREATE  {title} (id {qid}, unpublished)")
            created += 1
        except urllib.error.HTTPError as e:
            print(f"  FAIL    {title}: HTTP {e.code} {e.read().decode('utf-8', 'replace')[:300]}")
            failed += 1
        except Exception as e:  # noqa: BLE001 - report and continue with the rest
            print(f"  FAIL    {title}: {e}")
            failed += 1
    if args.apply:
        print(f"  => {created} created, {updated} re-coded, {skipped} skipped, {failed} failed")
        existing = existing_quizzes(cv, cid)  # pick up new IDs for later steps

    # Step 2: modules
    if args.skip_modules:
        print("\n[2] Modules: skipped (--skip-modules)")
    else:
        print("\n[2] Modules")
        added = already = 0
        for w, day, title, entry in rows:
            name = module_name_fmt.format(week=w)
            mid = modules[name.strip().casefold()]
            if title not in existing:
                print(f"  PLAN    {title} -> '{name}' (quiz not created yet)" if not args.apply
                      else f"  MISS    {title}: quiz not in Canvas, not added")
                if args.apply:
                    failed += 1
                continue
            qid = existing[title]["id"]
            if not args.apply:
                print(f"  PLAN    {title} -> '{name}'")
                continue
            try:
                if qid in module_quiz_ids(cv, cid, mid):
                    already += 1
                    continue
                add_quiz_to_module(cv, cid, mid, qid, title)
                print(f"  ADD     {title} -> '{name}'")
                added += 1
            except Exception as e:  # noqa: BLE001
                print(f"  FAIL    {title}: {e}")
                failed += 1
        if args.apply:
            print(f"  => {added} added, {already} already in module, {failed} failed so far")

    # Step 3: instructor code page (whole course; never with --only-week)
    if args.skip_page:
        print("\n[3] Instructor page: skipped (--skip-page)")
    elif args.only_week:
        print("\n[3] Instructor page: skipped (--only-week lists the whole course; run without it)")
    else:
        print("\n[3] Instructor page")
        missing = [t for _, _, t, _ in all_rows if t not in existing]
        if missing:
            print(f"  PLAN    {len(missing)} quizzes not created yet; page is written after creation" if not args.apply
                  else f"  SKIP    page: {len(missing)} quizzes missing from Canvas")
            if args.apply:
                failed += 1
        else:
            quiz_ids = {t: existing[t]["id"] for _, _, t, _ in all_rows}
            html = build_code_page(cfg, all_rows, quiz_ids, codes)
            slug = find_page_slug(cv, cid)
            if not args.apply:
                print(f"  PLAN    {'update' if slug else 'create'} unpublished page '{PAGE_TITLE}' ({len(all_rows)} rows)")
            else:
                try:
                    if slug:
                        cv.call(f"/courses/{cid}/pages/{slug}", method="PUT", payload={"wiki_page": {"body": html}})
                        print(f"  UPDATE  page '{PAGE_TITLE}' ({len(all_rows)} rows, unpublished)")
                    else:
                        cv.call(f"/courses/{cid}/pages", method="POST",
                                payload={"wiki_page": {"title": PAGE_TITLE, "body": html, "published": False}})
                        print(f"  CREATE  page '{PAGE_TITLE}' ({len(all_rows)} rows, unpublished)")
                except Exception as e:  # noqa: BLE001
                    print(f"  FAIL    page: {e}")
                    failed += 1

    print()
    if not args.apply:
        print("Dry run complete. Re-run with --apply to write.")
    elif failed:
        print(f"Finished with {failed} failure(s). Fix the cause and re-run; completed steps are skipped.")
    else:
        print("Finished. Quizzes are unpublished; publish each one on its class day.")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()

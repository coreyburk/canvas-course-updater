# Canvas Course Updater

Working repository for building and auditing Canvas LMS courses in the
Information Systems and Cybersecurity program at Neumont College of Computer
Science.

Courses in scope share a common set of Program Outcomes and a single
visual/structural standard, so most of the value here is in the **standards and
playbooks** rather than in code: templates for assignments and resource pages,
rubric conventions, and the repeatable procedures used to keep seven courses
consistent with one another.

## What this repo is not

It is not the courses. Canvas is the source of truth for all live content - page
bodies, assignment HTML, module ordering, publish state. Nothing here mirrors
that automatically. When a document in this repo disagrees with Canvas, Canvas
wins and the document gets corrected.

What lives here is the surrounding material: the standards content is held to,
the per-course status notes, and a few scripts for operations that are tedious
or risky to do by hand.

## Layout

| Path | Holds |
|---|---|
| `CLAUDE.md` | Standing rules: templates, conventions, known API limitations. |
| `CHANGELOG.md` | Session history, newest first. |
| `courses/{CODE}.md` | Per-course status, decisions, and pending work. |
| `courses/{CODE}/` | Per-course reference material: lab briefs, audits, training docs. |
| `.claude/skills/` | Playbooks for recurring authoring tasks. |
| `tools/` | Reusable scripts, safe to run against any course. |
| `archive/scripts/` | Spent one-off scripts, kept for reference. |
| `quizzes/{CODE}/` | Quiz XML for manual Canvas import. |

## Tools

```bash
python tools/emdash_sweep.py --course 3644698          # dry run, reports every hit
python tools/emdash_sweep.py --course 3644698 --apply  # write
```

Finds literal em dashes (U+2014) in assignment names, assignment descriptions,
and page bodies, and replaces them with space-hyphen-space. Canvas renders em
dashes as `&mdash;`, so they are banned in course content.

The sweep is deliberately conservative: it is a dry run unless you pass
`--apply`, it reports every hit with surrounding context first, it **skips any
item whose em dash sits inside a `<pre>` block** rather than risk altering a
code sample, and it never renames a page, because changing a page title changes
its URL slug and can break inbound links. After each write it re-fetches the
item and prints the remaining em dash count alongside a `<pre>` open/close
balance check, so damage to a code block would be visible immediately.

Hits are handled individually: prose is fixed even when the same item has
another em dash inside a code block, and that one is reported and left. Pass
`--include-pre` to rewrite code blocks too, but only after reading the `[CODE]`
context lines from a dry run and confirming none is part of a real command.

On Windows, prefix with `PYTHONIOENCODING=utf-8` or the console encoder fails
while printing context. Note that `python -I` ignores it, since isolated mode
implies `-E`.

```bash
python tools/test_emdash_sweep.py
```

Covers the behavior that matters: code blocks survive byte-for-byte unless
`--include-pre` is explicitly set.

## Setup

Scripts and the `canvas-api` MCP server read credentials from a `.env` in the
canvas-mcp install directory:

```
CANVAS_API_URL=https://<your-institution>.instructure.com
CANVAS_API_TOKEN=<token>
```

Credentials are never stored in this repo. `.env`, local Claude settings, and
course textbooks are gitignored.

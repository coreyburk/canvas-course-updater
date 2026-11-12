# Canvas Course Updater

Working repository for building and auditing Canvas LMS courses in the
Information Systems and Cybersecurity program at Neumont College of Computer
Science.

Courses in scope share a common set of Program Outcomes and two visual/structural
standards (Format 1 BIT221 standard and Format 2 Modern Minimal), plus a
standardized 3-box assignment template and 3-level rubric standard.

## What this repo is not

It is not the courses. Canvas is the source of truth for all live content - page
bodies, assignment HTML, module ordering, publish state. Nothing here mirrors
that automatically. When a document in this repo disagrees with Canvas, Canvas
wins and the document gets corrected.

What lives here is the surrounding material: the standards content is held to,
the per-course status notes, and a suite of low-context CLI tools that compile,
lint, and sync Canvas HTML without flooding LLM conversation context.

## Layout

| Path | Holds |
|---|---|
| `CLAUDE.md` / `AGENTS.md` | Standing rules: templates, conventions, known API limitations. |
| `CHANGELOG.md` | Session history, newest first. |
| `courses/{CODE}.md` | Concise per-course live status, IDs, decisions, and pending work. |
| `courses/{CODE}/` | Per-course reference material: lab briefs, audits, reference scripts. |
| `archive/courses/` | Full historical course build logs archived from `courses/{CODE}.md`. |
| `.claude/skills/` & `.agents/skills.json` | Playbooks for recurring authoring tasks (shared across Claude Code and Antigravity). |
| `tools/` | Reusable CLI scripts, safe to run against any course. |
| `archive/scripts/` | Spent one-off scripts, kept for reference. |
| `quizzes/{CODE}/` | Quiz XML for manual Canvas import. |

## Low-Context Tooling (`tools/`)

### 1. Build Canvas HTML from Markdown (`tools/canvas_build.py`)
Compiles structured Markdown into inline-styled Canvas HTML (`page-f1`, `page-f2`, `lecture`, `lab-notes`, or `assignment`) and runs `canvas_lint.py` automatically:
```bash
python tools/canvas_build.py scratchpad/page.md -o scratchpad/page.html --template page-f1
```

### 2. Sync Pages & Assignments Without Context Bloat (`tools/canvas_sync.py`)
Pulls and pushes pages and assignments via local files and prints a 3-4 line summary to stdout instead of echoing 30 KB HTML blobs through MCP tool calls:
```bash
python tools/canvas_sync.py list-pages --course BIT360
python tools/canvas_sync.py pull-page --course BIT360 --page <slug> -o scratchpad/page.html
python tools/canvas_sync.py push-page --course BIT360 --page <slug> -i scratchpad/page.html
python tools/canvas_sync.py lint-course --course BIT360
```

### 3. Lint & Auto-Fix Canvas HTML (`tools/canvas_lint.py`)
Checks mechanical and structural rules (no em dashes, no `<style>`/`<svg>`, `<pre>` `white-space: pre-wrap` and balance, Criteria box table structure, `<p>` before `<ul>`, no points in Criteria, no trailing elements after Criteria):
```bash
python tools/canvas_lint.py scratchpad/page.html
python tools/canvas_lint.py --fix scratchpad/page.html
```

### 4. Course-Wide Em Dash Sweep (`tools/emdash_sweep.py`)
```bash
python tools/emdash_sweep.py --course 3644698          # dry run, reports every hit
python tools/emdash_sweep.py --course 3644698 --apply  # write prose fixes, preserve <pre>
```

### 5. Page Coverage Audit & Model Cost Repricing
```bash
python tools/audit_canvas_pages.py --course BIT360 --weeks 10
python tools/model_cost_check.py --days 7
```

### 6. Unit Tests
```bash
python tools/test_emdash_sweep.py
python tools/test_canvas_tools.py -v
```

## Setup

Scripts and the `canvas-api` MCP server read credentials from a `.env` in the
canvas-mcp install directory (`C:\Users\cburk\canvas-mcp\.env`):

```
CANVAS_API_URL=https://<your-institution>.instructure.com
CANVAS_API_TOKEN=<token>
```

Credentials are never stored in this repo. `.env`, local settings, and course
textbooks are gitignored.

---
name: canvas-html-lint
description: Use when Corey asks to lint, scan, or fix Canvas HTML rule violations on a page, assignment, or across an entire course (e.g. "check for em dashes in BIT351", "lint this page", "scan the course for HTML issues before publishing"). Mechanical rule check, not a style/layout audit - pairs with visual-template-audit.
---

# Canvas HTML Lint

Checks Canvas page and assignment HTML against the mechanical rules in `CLAUDE.md` ("Non-negotiable standards" and "Canvas HTML rules"). Distinct from `visual-template-audit`: this catches markup-hygiene and structural violations that break rendering or get silently stripped by Canvas.

## Step 0 - Low-Context Automated Tooling
**Do NOT pull every page body into LLM context via `get_page_content` just to scan for lint issues.** Use the deterministic CLI linter (`tools/canvas_lint.py` and `tools/canvas_sync.py`):

- **Scan an entire Canvas course (all pages + all assignments) with zero HTML bloat in context:**
  ```bash
  python tools/canvas_sync.py lint-course --course <CODE_OR_ID>
  ```
- **Sweep and fix em dashes course-wide (with `<pre>` integrity verification):**
  ```bash
  python tools/emdash_sweep.py --course <ID>          # dry run
  python tools/emdash_sweep.py --course <ID> --apply  # write prose fixes
  ```
- **Lint (and optionally auto-fix) a local HTML file before pushing:**
  ```bash
  python tools/canvas_lint.py scratchpad/item.html --type auto
  python tools/canvas_lint.py --fix scratchpad/item.html
  ```

## Step 1 - Rules Enforced by `tools/canvas_lint.py`

| Rule ID | Detection | Why it matters |
|---|---|---|
| `NO_EM_DASH_PROSE` / `NO_EM_DASH_TITLE` / `NO_MDASH_ENTITY` | Literal Unicode `—` outside `<pre>` or `&mdash;` | Renders as literal `&mdash;` in Canvas; use ` - ` |
| `EM_DASH_IN_PRE` | Literal Unicode `—` inside `<pre>` | Flagged as warning: verify whether it is a prose comment inside code or a literal command before fixing |
| `NO_STYLE_TAG` | Any `<style>` block | Canvas strips `<style>` silently on save |
| `NO_INLINE_SVG` | Any `<svg>` block | Canvas strips `<svg>` silently; upload diagram as image and reference via `<img>` |
| `NO_FONT_WEIGHT` | Inline `font-weight:` on non-`<strong>`/`<th>`/`<h1-h6>` tags | Project convention uses `<strong>` |
| `PRE_WRAP` / `PRE_BALANCE` | `<pre>` without `white-space: pre-wrap;` or unbalanced `<pre>` tags | Long code lines overflow/clip without `pre-wrap` |
| `CSS_TYPO` | Typos like `14py` instead of `14px` | Silently breaks inline styling |
| `CRITERIA_TABLE` | Assignment Criteria for Success box using `<div>` instead of `<table>` | Canonical BIT351/BIT221 assignment template uses `<table>` |
| `CRITERIA_H3_UL` | `<h3>Criteria for Success</h3>` immediately followed by `<ul>` with no `<p>` | Breaks the table box border rendering in Canvas |
| `CRITERIA_POINTS` | Point values (`5 pts`, `10 points`) inside Criteria for Success box | Points belong only in the Canvas rubric |
| `CRITERIA_FINAL` | Any content after the Criteria for Success `</table>` | Criteria for Success must be the final element in an assignment |

## Step 2 - Manual Content Check (When Auditing Pages with Activities)
In addition to running `canvas_lint.py`, check one pedagogical rule if the page has an in-class activity or discussion section:
- **In-class activity answerable from page content:** Every discussion or activity question must be answerable from the page's own body text (found previously on BIT221 Week 1 Page 3 and BIT351 Week 1 Page 2).

## Step 3 - Fixing Flagged Items Without Context Bloat
1. Pull only the flagged item(s) to disk:
   ```bash
   python tools/canvas_sync.py pull-page --course <CODE> --page <slug> -o scratchpad/fix.html
   # or
   python tools/canvas_sync.py pull-assignment --course <CODE> --assignment <id> -o scratchpad/fix.html
   ```
2. Run `python tools/canvas_lint.py --fix scratchpad/fix.html` for mechanical fixes, or use `edit_file` on `scratchpad/fix.html` for structural fixes (e.g., adding the intro `<p>` before `<ul>` in a Criteria box or moving Deliverables above Criteria).
3. Push back via `python tools/canvas_sync.py push-page` or `push-assignment` (which re-runs `canvas_lint` automatically before writing).

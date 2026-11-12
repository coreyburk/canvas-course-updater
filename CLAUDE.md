# Canvas Course Updater - Standing Instructions

## Purpose
Corey is an instructor at Neumont University (cburk@neumont.edu), building and
auditing courses in an Information Systems and Cybersecurity degree program via
the Canvas MCP server (`canvas-api`). Courses in scope share the same Program
Outcomes and the BIT221 visual/structural standard.

## Courses
| Code | Canvas ID | Title | Status |
|---|---|---|---|
| BIT221 | 3631198 | Server Administration I - Windows Server 2025 | ✅ Complete (2026-09-08) |
| BIT281 | 3631199 | Hardware Systems | ✅ Complete (2026-09-03) |
| BIT320 | 3644698 | Shell and Administrative Scripting | ✅ Complete (2026-09-12) |
| BIT360 | 3644702 | Applied Systems Operations & Disaster Recovery | 🔧 Remediation in progress (Week 1 first, 2026-10-07) - see courses/BIT360-2026.md |
| PRO221 | 3631288 | Server Admin I - Project: Windows Server | ✅ Complete (2026-09-03) |
| BIT351 | 3631200 | Virtual Systems: Proxmox VE | ✅ Complete (2026-09-03) |
| PRO352 | 3631317 | Virtualization Project: Proxmox (Multi-cluster) | ✅ Complete (2026-09-03) |
| ITH216 | 3646987 | Networking II | ✅ Complete (2026-09-16) |

## Course Status

**⚠️ IMPORTANT:** Per-course status, decisions, pending work, and history live in `courses/{CODE}.md`
(e.g., `courses/BIT320.md`, `courses/PRO221.md`). Check the relevant file at the start of any session
touching that course. Do NOT duplicate course-specific information in CLAUDE.md.

**Session history** lives in [CHANGELOG.md](CHANGELOG.md), not in this file.
Log new work there, newest first. Durable technical findings (API behavior,
template rules, transport issues) belong in the relevant section below instead,
so they stay in context every session.

## Non-negotiable standards (all courses)
- **Canvas is the source of truth**, never an outline doc or prior memory.
  When they diverge, fix the doc to match Canvas, not the reverse.
- **Read actual source before writing.** Pull live page/assignment content
  with `get_page_content` / `get_assignment_details` before rewriting -
  never reconstruct from general knowledge.
- **Fix issues at the source**, not around them.
- **No em dashes, ever** - they render as `&mdash;` in Canvas. Space-hyphen-space instead.
  Scan for literal Unicode `—`, not the HTML entity.
- **No point values inside Criteria for Success boxes.**
- Bullet lists inside the Criteria for Success box: never let an `h3` be
  immediately followed by a `ul` with no paragraph between them (breaks the
  border). Add an intro sentence before each list. The box itself **is** a
  `<table>` (see Assignment template below) - don't swap it for a `div`, the
  intro paragraph alone is the fix.
- **Canvas HTML rules:** all styling inline (`<style>` tags are stripped);
  `<strong>` not `font-weight`; `<pre style="white-space: pre-wrap;">` for
  code; no inline SVG (stripped) - diagrams are uploaded image files
  referenced via `<img>`.
- **Don't fabricate Program Outcome language** - source it from verified
  Canvas content only.
- If a course has two competing page styles (old-style tables vs. current
  template) surface it and offer to merge/retire the old one rather than
  letting both persist silently.

## Assignment template (distinct from the page visual template below)
Assignments use `<table>`-based boxes, not the div-based page callouts.
Canonical structure is three boxes - Purpose, Task, Criteria for Success -
standardized 2026-07-21 on BIT351's implementation (the most complete of
three divergent forms found across courses: BIT221 had no Task box, BIT281
had an unstyled `<h3>Task</h3>` heading plus a div-based, not table-based,
Criteria box). Verified against live BIT221 (2B - Configure Active Directory
and DNS) and BIT351 (1A - Proxmox VE Setup and Configuration) content.

**HTML Table Structure (Correct Format - Updated 2026-09-13):**
All assignment boxes use proper table structure with `border-collapse: collapse;`
and `<td>` padding instead of `cellpadding`. This ensures consistent rendering
across browsers and Canvas versions:

```html
<table style="background-color: #eaf4fb; width: 100%; border-collapse: collapse; border: 2px solid #2980b9;">
    <tbody>
        <tr>
            <td style="padding: 20px;">
                <!-- Content here -->
            </td>
        </tr>
    </tbody>
</table>
```

**Box Specifications:**
- Purpose box: `<table style="background-color: #eaf4fb; width: 100%; border-collapse: collapse; border: 2px solid #2980b9;">`,
  `<h3 style="color: #1a5276; margin-top: 0;">Purpose</h3>` - scenario
  paragraph (real-world framing, not just a restatement of the task), then
  Course Learning Outcomes and Program Outcomes lists.
- Task box: `<table style="background-color: #fef9e7; width: 100%; border-collapse: collapse; margin-top: 15px; border: 2px solid #d4ac0d;">`,
  `<h3 style="color: #9a7d0a; margin-top: 0;">Task</h3>` - one concrete
  paragraph stating what the student will build/configure/produce, distinct
  from Purpose's why-it-matters framing and from the detailed step-by-step
  instructions that follow it. Keep it short even on trivial assignments
  (a single sentence is fine); the value is the scanability of a why/what
  pair before the procedural detail starts, not box length.
- Criteria for Success box: `<table style="background-color: #eafaf1; width: 100%; border-collapse: collapse; margin-top: 15px; border: 2px solid #27ae60;">`,
  `<h3 style="color: #1e8449; margin-top: 0;">Criteria for Success</h3>` - intro sentence,
  then one `<ul>` of grading criteria.
- Screenshot-required marker: `<img src="https://img.icons8.com/carbon-copy/2x/camera.png"
  alt="Screenshot required" width="25" height="25" loading="lazy">` after
  any step needing one.
- Inline hint: `<span style="background-color: #ffff00;"><strong>Hint:</strong></span>`.

## Visual template (BIT221 standard, reference for all courses - lecture/resource pages)
- Wrapper: `max-width: 860px`, `color: #2C2C2A`, system font stack.
- Header card: beige `#F1EFE8` / border `#B4B2A9`, 8px radius.
- Learning objectives: purple `#EEEDFE` / `#534AB7`, 2-col grid, checkmark tiles.
- Section headers: green `#E1F5EE` / `#0F6E56` left-border bars.
- Tables: dark header `#444441`, alternating `#ffffff` / `#F1EFE8` rows.
- Callouts: amber `#FAEEDA` / `#854F0B` (notes/best practice), blue
  `#E6F1FB` / `#185FA5` (info).
- Code blocks: dark `#2C2C2A` background, Catppuccin-style syntax colors.
- "Applied" section header (hands-on/code intro): dark variant, bg `#2C2C2A`,
  left-border `#5DCAA5`, title text `#9FE1CB` - distinct from the light green
  section-header bar above.
- In-class activity steps: numbered rows, dark `#444441` number marker,
  alternating `#ffffff` / `#F1EFE8` step backgrounds.
- Section dividers: `border-top: 0.5px solid #D3D1C7; margin: 2.5rem 0`.
- Page titles: topic-only, no "Week N |" prefix duplicated in the title bar
  (the breadcrumb subtitle carries that).

## Workflow & Low-Context HTML Authoring
- Confirm major structural decisions before executing (new page structures,
  deleting/merging content, rubric point changes).
- Keep new content unpublished until reviewed.
- Verify current Canvas state (`python tools/canvas_sync.py list-pages --course <CODE>`,
  `list-assignments`, or `get_course_structure`) before authoring in a session -
  don't assume prior session state still holds.
- **Never pass 20-35 KB HTML bodies through MCP tool arguments (`get_page_content`,
  `edit_page_content`, `create_page`, `update_assignment`).** Doing so puts 3-4
  copies of the raw inline-styled HTML into conversation scrollback (~100k
  tokens per page). Instead:
  1. **Pull to disk:** `python tools/canvas_sync.py pull-page` (or `pull-assignment`)
     writes the HTML to `scratchpad/` and prints a 4-line summary to stdout.
  2. **Author in Markdown, compile deterministically:** For new or rebuilt pages
     and assignments, write structured Markdown (`template: page-f1 | page-f2 | lecture | lab-notes | assignment`)
     and compile via `python tools/canvas_build.py <in.md> -o scratchpad/<out.html>`.
     This cuts LLM output tokens by ~65% and guarantees compliant inline CSS.
  3. **Push from disk:** `python tools/canvas_sync.py push-page` / `create-page` /
     `push-assignment` runs `tools/canvas_lint.py` automatically before writing
     to Canvas and verifies `<pre>` integrity afterward.
  4. **Isolate multi-page builds across subagents:** When building multiple pages
     for a week, spawn one subagent per page so HTML drafts die with the
     subagent's context rather than accumulating in the main session.
- Keep `courses/{CODE}.md` concise (~5-10 KB of live state, IDs, decisions, and
  pending work); archive completed multi-page build logs in `archive/courses/`.
- At the end of any session touching `CLAUDE.md`, `courses/`, or repo content,
  remind Corey to commit and suggest a commit message.
- **The GitHub repo is public** (https://github.com/coreyburk/canvas-course-updater).
  Never commit credentials, student data, or copyrighted course material.
  Textbooks live in `textbooks/`, which is gitignored.

## Session cost & context hygiene
Measured 2026-11-10 from the Claude Code session transcripts in
`~/.claude/projects/D--GitHub-Repos-Canvas-Course-Updater/`. Durable, not a
one-off: Canvas work is unusually expensive per request and the cause is
structural.

- **Cache reads are ~95% of the bill.** Every API call re-reads the whole
  conversation from cache and that read is billed. Cost therefore scales with
  *context size per request*, not with how many requests you make. Nov 10 used
  201 requests and cost ~$69; Sep 17 used 485 requests and cost ~$12.
- **Split sessions by task.** Average context per request was ~125k in
  September and ~580k on Nov 9-10, a 4.6x swing on the same kind of work. A
  session carrying 500k+ tokens is paying rent on scrollback it no longer
  needs. Start a fresh session (or `/clear`) between separable units - between
  two week pages, between a course audit and the rewrite it produced.
- **Why Canvas work bloats fast:** `edit_page_content` requires the complete
  page HTML in one call (see Known Canvas API limitations), `get_page_content`
  pulls full bodies, and the ~100 `canvas-api` tool definitions plus skills and
  memory files add roughly 45k of fixed overhead to every single request.
- **Rank models by cache-read price, not headline price.** Cache reads are
  70-85% of the bill on this workload, so the usual "$ per MTok input/output"
  comparison ranks models wrongly.
- **Pricing is only valid at the moment it is fetched.** Never rank models
  from a stored table, including the one below. Run
  `python tools/model_cost_check.py` for a current ranking; it fetches live
  prices from Anthropic, OpenAI, and Google every run. Stored figures are a
  historical usage record only.
- **How each coding agent is billed matters (2026-11-12):**
  - **Claude Code:** Metered API (`~/.claude/projects/`). Dollars are real out-of-pocket spend. Optimize for dollar cost per finished task.
  - **Codex:** ChatGPT Plus subscription (`~/.codex/sessions/`). Dollars are API-equivalent; the real constraint is subscription rate-limit headroom (5h primary and 7d secondary windows, reported directly by `model_cost_check.py`).
  - **Antigravity (AGY):** Google subscription/quota (`~/.gemini/antigravity-cli/conversations/*.db`). Dollars are API-equivalent; usage is decoded from `gen_metadata` protobuf records. Optimize for quota headroom while matching model capability to task complexity.
- **Transcripts are per machine and per repo.** Corey works across several
  computers and repositories. `model_cost_check.py` reads local logs for all
  three tools (`--source claude|codex|agy|all`, default `all`), and
  `--all-projects` widens to every repo on *this* machine, not other machines.
  A run on one machine is a partial picture; say so when reporting.
- **Historical snapshot (2026-11-10, one machine, `D:` repo path, not current
  pricing):** token mix 118.6M cache read / 0.73M write / 0.31M output:

  | Model | Cache read $/MTok | Cost for that day |
  |---|---|---|
  | Opus 5 | $0.50 | $71.67 |
  | Fable 5.2 | $0.20 | $43.49 |
  | Opus 5.5 | $0.20 | $33.61 |
  | Sonnet 5 | $0.20 | $28.67 |
  | Sonnet 5.5 | $0.10 | $16.80 |
  | Haiku 5.5 (>100k prompt) | $0.05 | $7.17 |

  **Cross-tool model recommendations (re-confirmed 2026-11-12 against live Anthropic, OpenAI, and Google pricing):**
  - **Claude Code (metered API):** **Never Opus 5** (or 4.x Opus) - Opus 5.5 is half the cost and better on every axis, and Fable 5.2's high cache-write/output rates make it more expensive than Opus 5.5 on this workload. Default to **Claude Sonnet 5.5** (`$0.10/MTok` cache read) for template-driven production work (page builds, HTML rewrites, em dash sweeps) and **Claude Haiku 5.5** (`$0.01/$0.05` cache read) for mechanical subagent scans. Reach for **Claude Opus 5.5** (`$0.20/MTok` cache read, ~2x Sonnet 5.5, `medium` effort) only when judgment matters more than volume (course structure decisions, multi-option pedagogical audits).
  - **Antigravity (subscription/quota):** Running Claude Opus 5.5 inside AGY consumes ~2x the API-equivalent weight of **Gemini 4 Argon / Gemini 4 Carbon** or **Claude Sonnet 5.5** (`$0.10/MTok` cache read, identical cost tier), and ~4.3x **Gemini 3.6 / 3.8 Flash** (`$0.075/MTok` cache read). Default to **Gemini 4 Argon (Medium)** or **Claude Sonnet 5.5** for general engineering and repo tasks, drop to **Gemini 3.8 Flash** for routine edits/git ops, and reserve **Claude Opus 5.5** or **Gemini 4 Carbon** for complex architectural or pedagogical design.
  - **Codex (ChatGPT Plus subscription):** Historical usage was dominated by `gpt-5.5` (`$0.50/MTok` cache read, 67% of API-equivalent spend, driving 5h window peak to 79%). Current generation **gpt-6.1-sol** (`$0.10/MTok` cache read) and **gpt-6.1-terra** (`$0.05/MTok` cache read) or **gpt-5.4-mini** (`$0.075/MTok`) are 3.5x-7x lighter than `gpt-5.5`. Default to **gpt-6.1-terra** / **gpt-5.4-mini** for routine coding and **gpt-6.1-sol** / **gpt-5.4** for heavier multi-file work; avoid `gpt-5.5` and `gpt-6-astra` (`$1.00/MTok` cache read) to preserve 5h/7d Plus window headroom.
- **Re-check the ranking when a new model ships, not on a calendar.** The
  cache-read *multiplier* has been improving per generation (0.1x of base input
  on Opus 5 and earlier, 0.05x on Opus 5.5 / Sonnet 5.5, 0.025x on Fable), so
  each release can reshuffle the order for this workload even when headline
  prices look similar. Live source:
  `https://platform.claude.com/docs/en/about-claude/pricing.md`. The pricing
  table bundled in the `claude-api` skill is a cached snapshot - fetch the page
  rather than trusting it. Haiku 5.5 is priced per request by prompt length;
  these sessions average ~120k, so most (not all) requests bill at the
  higher row.
- **The usage chart is dated in UTC**, so a billing day runs 5:00 PM MST to
  5:00 PM MST. Today's bar is mostly last night's work - check the hours before
  concluding a given day was expensive.

## Repo layout
| Path | Holds |
|---|---|
| `CLAUDE.md` / `AGENTS.md` | Standing rules (shared across Claude Code and Antigravity). |
| `CHANGELOG.md` | Session history, newest first. |
| `.claude/skills/` & `.agents/skills.json` | Reusable playbooks (11 skills, discovered by both Claude Code and Antigravity). |
| `courses/{CODE}.md` | Concise per-course live status, IDs, decisions, pending work (~5-10 KB). Authoritative. |
| `courses/{CODE}/` | Per-course reference material (lab briefs, audits, reference code, rubric specs). |
| `archive/courses/` | Archived historical build logs from `courses/{CODE}.md`. |
| `tools/` | Reusable low-context CLI tools, safe against any course. |
| `archive/scripts/` | Spent one-off scripts. Course IDs hardcoded, read before reuse. |
| `quizzes/{CODE}/` | Quiz XML for manual Canvas import. |
| `textbooks/` | Gitignored. Copyrighted, local only. |

### Tools
- `tools/canvas_build.py <input.md> -o <output.html> [--template page-f1|page-f2|lecture|lab-notes|assignment]` -
  compiles structured Markdown into Canvas-compliant inline-styled HTML and runs
  `canvas_lint.py` automatically. Eliminates hand-generating verbose inline CSS.
- `tools/canvas_sync.py <cmd> --course <CODE_OR_ID> ...` - low-context REST CLI
  for `list-pages`, `list-assignments`, `pull-page`, `push-page`, `create-page`,
  `pull-assignment`, `push-assignment`, and `lint-course`. Moves HTML bodies via
  local files (`scratchpad/`), runs `canvas_lint` before every write, checks
  `<pre>` block preservation after every write, and prints only a 3-4 line
  summary to stdout.
- `tools/canvas_lint.py [--fix] <file.html> [--type auto|page|assignment]` -
  mechanical and structural HTML linter checking em dashes (prose vs `<pre>`),
  `<style>`, `<svg>`, inline `font-weight`, `<pre>` `white-space: pre-wrap` and
  tag balance, CSS unit typos (`14py`), and assignment Criteria box rules
  (`<table>` container, intro `<p>` before `<ul>`, no point values, no trailing
  content after Criteria).
- `tools/emdash_sweep.py --course <id>` - finds and fixes literal em dashes in
  assignment names/descriptions and page bodies. Dry run by default, `--apply`
  writes. Hits are handled **individually**: prose is fixed even when the same
  item has another em dash inside a `<pre>` block, and the one inside `<pre>`
  is reported and left. After each write it re-fetches and compares the item's
  `<pre>` blocks against the originals (`PRE CHANGED` on drift). `--include-pre`
  also rewrites em dashes inside code blocks (only after verifying `[CODE]`
  context lines). Page titles are never auto-renamed, though note that a slug
  only moves if the NEW title normalizes differently (Canvas strips `—` and `-`
  identically).
- `tools/audit_canvas_pages.py --course <CODE_OR_ID> [--weeks 10]` - weekly page
  coverage audit across student, instructor, navigation, and legacy pages. Reads
  credentials from `canvas-mcp` `.env`.
- `tools/model_cost_check.py [--source all|claude|codex|agy] [--day YYYY-MM-DD] [--days N] [--all-projects] [--billed X]` -
  reprices the tokens actually used across Claude Code (`~/.claude/projects`),
  Codex (`~/.codex/sessions`, including Plus subscription rate-limit headroom),
  and Antigravity (`~/.gemini/antigravity-cli/conversations/*.db`) on every
  current model, with pricing fetched live from Anthropic, OpenAI, and Google.
  Read-only, no Canvas calls.

## Known Canvas API limitations
- `course_identifier` needs the numeric ID, not the course code string.
- **⚠️ CRITICAL: `edit_page_content` REPLACES ENTIRE PAGE** - Every call to `edit_page_content`
  completely replaces the page content. DO NOT send multiple partial updates expecting them
  to accumulate - only the last update persists, all previous content is lost. **ALWAYS build
  the complete page HTML as one monolithic block and send in a SINGLE API call.** Lesson learned
  2026-09-15 ITH216 expansion: sending 6+ incremental updates (thinking they'd stack) wasted
  tokens and subscription cost, resulting in only the final update persisting. Always verify
  the complete HTML includes all sections before sending.
- `update_assignment` / `edit_page_content` do full replacement - always
  carry forward the complete current HTML, never a partial patch.
- `points_possible` on quiz-backed assignments is derived from question
  totals - cannot be changed via API, must edit in the Canvas UI.
- Quiz titles/points/content: read-only via API, all edits manual.
- **Rubrics ARE writable via the API** (verified 2026-11-09 on a throwaway rubric, created, updated and deleted). Title, points, criterion descriptions, long descriptions and rating
  levels can all be changed with `PUT /courses/:id/rubrics/:rubric_id` using form-encoded
  `rubric[criteria][N][...]` parameters. The read-only rule above applies to quizzes, not
  rubrics; nothing had ever established that rubrics were read-only. Quiz **due dates** are
  also settable (`PUT /courses/:id/quizzes/:id` with `quiz[due_at]`), just not their titles,
  points or questions. Caveat: a rubric that already has assessments against it may refuse
  edits, so check for submissions before changing one mid-term.
- **A rubric PUT that omits criteria does NOT destroy them** (verified 2026-11-09 on a
  throwaway with three criteria: a title-only PUT left all three and the point total
  intact). So renaming a rubric is safe on its own. Changing one criterion is not proven
  safe as a partial send, so resend every criterion with its full ratings when editing one.
- Rubric `long_description` values are stored as HTML, so an apostrophe comes back as
  `&#39;`. That is correct and renders properly; it is not double-escaping.
- `add_module_item` needs the assignment's `content_id`, not the module item ID.
- Repositioning a module item: `update_module_item` with target position,
  plus a separate call on the item it displaced. Don't re-call
  `add_module_item` with a new position - creates a duplicate.
- **Module item repositioning is unreliable via `position`** (2026-11-07): Setting an item's `position` to a target index frequently reorders OTHER items unpredictably - in one case it moved the Quiz subheader above Resources. Setting several items to the same target position in sequence made it worse. **Reliable technique:** rebuild the tail of the module by setting each item's `position` to the LAST index, one call per item, in the desired final order. Every item lands at the end in turn, so the final sequence is exactly the order you issued the calls in. Always verify with `list_module_items` afterwards; do not assume the reorder did what you asked.
- **A post-write re-fetch can return stale content** (2026-11-09): reading an
  item back immediately after a successful PUT sometimes returns the PRE-write
  body, so a verification step can report a false failure. Seen on BIT360
  "Lecture Notes - Week 9.2": the re-fetch said 2 em dashes remained, while an
  independent read moments later showed 0 and the write had in fact landed.
  Re-check independently before treating a post-write verification as a failure.
- `delete_module` auto-removes its module items; `delete_module_item` only
  unlinks a page/assignment, doesn't delete the underlying content - use
  `delete_page` separately if the content itself should go.

## MCP transport & server (canvas-api)
- `canvas-api` runs via **stdio directly** from `C:\Users\cburk\canvas-mcp`.
  Each client (Claude Code, Claude Desktop) spawns its own canvas-mcp process.
- **Server code:** `C:\Users\cburk\canvas-mcp` - all MCP tools resolve from here.
- **Configuration:**
  - Claude Code: `.mcp.json` points to `C:\Users\cburk\canvas-mcp` with command
    `python -m canvas_mcp.server` (stdio transport, no HTTP).
  - Claude Desktop: `claude_desktop_config.json` points to `C:\Users\cburk\canvas-mcp`
    with same command.
- **Credentials:** Read from `.env` file in the canvas-mcp directory
  (`CANVAS_API_TOKEN`, `CANVAS_API_URL`). Credentials are NOT per-request headers.
- **If canvas-api tools are missing or fail to connect:**
  1. Verify `.env` exists in `C:\Users\cburk\canvas-mcp` with valid token and URL.
  2. Check that `.mcp.json` (Claude Code) and `claude_desktop_config.json`
     (Claude Desktop) point to the correct command and directory.
  3. Restart Claude Code or Claude Desktop.
  4. Do NOT use HTTP server mode (it is unreliable and was deprecated).

- **⚠️ CRITICAL: fastmcp version constraint (2026-09-16 discovery)**
  - canvas-mcp `pyproject.toml` specifies `fastmcp>=2.14.0,<3` (fastmcp 2.x only)
  - fastmcp 3.x is INCOMPATIBLE with canvas-mcp - causes `ImportError: cannot import name 'IdentityAssertionParams'` and CONNECTION_CLOSED in Claude Code
  - **Root cause:** `uv.lock` was generated with fastmcp 3.1.1, violating the <3 constraint. When the venv is recreated (or when Claude Code spawns the MCP server), it pulls from uv.lock which pins the broken version.
  - **Solution:** Delete `uv.lock` and regenerate with `uv sync` to respect the <3 constraint, OR manually reinstall with `pip install --force-reinstall 'fastmcp<3'`

- **⚠️ CRITICAL: Event loop closure during server startup (2026-09-23 discovery, FIX COMMITTED)**
  - **Symptom:** "Event loop is closed" error on Canvas API requests (often starting on the second tool call).
  - **Root cause:** `src/canvas_mcp/server.py` called `asyncio.run(_validate_token())` during startup, which created and immediately closed an event loop before FastMCP's `mcp.run()` initialized its own loop.
  - **Fix (committed 2026-09-23 b7905af):** Removed early token validation from `server.py` lines 276-290 so credentials validate on first request inside `mcp.run()`'s loop. **Never call `asyncio.run()` before `mcp.run()` in the same startup process.**

- **⚠️ ARCHITECTURAL LIMITATION: Concurrent Canvas API connections (2026-09-16 discovery)**
  - **Problem:** stdio MCP is 1:1 client-to-process. Running multiple Claude Code windows simultaneously spawns separate `canvas-mcp` subprocesses that conflict over the same token, causing `CONNECTION_CLOSED` errors (the same concurrency conflict that made deprecated HTTP mode unreliable).
  - **Workaround:** Keep only ONE active Claude Code window using `canvas-mcp` at a time, or use `tools/canvas_sync.py` for stateless CLI requests. Do NOT re-enable HTTP server mode. Keep `uv.lock` out of the repo if it violates `pyproject.toml` constraints.

## Working style
Corey doesn't want timeline estimates, sycophancy, or hedging. Be direct,
concise, and willing to push back. Confirm before big structural or
destructive actions; don't ask permission for routine, established-pattern work.

# Canvas Course Updater — Standing Instructions

## Purpose
Corey is an instructor at Neumont University (cburk@neumont.edu), building and
auditing courses in an Information Systems and Cybersecurity degree program via
the Canvas MCP server (`canvas-api`). Courses in scope share the same Program
Outcomes and the BIT221 visual/structural standard.

## Courses
| Code | Canvas ID | Title | Status |
|---|---|---|---|
| BIT221 | 3631198 | Server Administration I — Windows Server 2025 | Reference standard, largely built |
| BIT281 | 3631199 | Hardware Systems | Rebuild complete |
| PRO221 | 3631288 | Server Admin I — Project: Windows Server | Week 4 complete, 2C/4B flagged |
| BIT351 | 3631200 | Virtual Systems: Proxmox VE | Active build |

## PRO221 Current Status (as of 2026-07-23)
- **Week 4 audit complete:** Pages 3 & 4 created (RDS/MPIO, WSUS) and published
- **2C (DSC Pull Server):** Unpublished, flagged NOT WORKING — needs vet/repair/deletion
- **4B (WSUS):** Unpublished but complete — ready for publication decision
- **OT1:** Keeping Windows Server 2019 File Services (no 2025 replacement available yet)
- **Open decisions:** 2C status, 4B publish decision, optional Week 4 page reorder

Per-course status, decisions, and history live in `courses/{CODE}.md`. Check
the relevant file at the start of any session touching that course.

## Non-negotiable standards (all courses)
- **Canvas is the source of truth**, never an outline doc or prior memory.
  When they diverge, fix the doc to match Canvas, not the reverse.
- **Read actual source before writing.** Pull live page/assignment content
  with `get_page_content` / `get_assignment_details` before rewriting —
  never reconstruct from general knowledge.
- **Fix issues at the source**, not around them.
- **No em dashes, ever** — they render as `&mdash;` in Canvas. Space-hyphen-space instead.
  Scan for literal Unicode `—`, not the HTML entity.
- **No point values inside Criteria for Success boxes.**
- Bullet lists inside the Criteria for Success box: never let an `h3` be
  immediately followed by a `ul` with no paragraph between them (breaks the
  border). Add an intro sentence before each list. The box itself **is** a
  `<table>` (see Assignment template below) — don't swap it for a `div`, the
  intro paragraph alone is the fix.
- **Canvas HTML rules:** all styling inline (`<style>` tags are stripped);
  `<strong>` not `font-weight`; `<pre style="white-space: pre-wrap;">` for
  code; no inline SVG (stripped) — diagrams are uploaded image files
  referenced via `<img>`.
- **Don't fabricate Program Outcome language** — source it from verified
  Canvas content only.
- If a course has two competing page styles (old-style tables vs. current
  template) surface it and offer to merge/retire the old one rather than
  letting both persist silently.

## Assignment template (distinct from the page visual template below)
Assignments use `<table>`-based boxes, not the div-based page callouts.
Canonical structure is three boxes — Purpose, Task, Criteria for Success —
standardized 2026-07-21 on BIT351's implementation (the most complete of
three divergent forms found across courses: BIT221 had no Task box, BIT281
had an unstyled `<h3>Task</h3>` heading plus a div-based, not table-based,
Criteria box). Verified against live BIT221 (2B - Configure Active Directory
and DNS) and BIT351 (1A - Proxmox VE Setup and Configuration) content:
- Purpose box: `<table style="background-color: #eaf4fb; border: 2px solid
  #2980b9;">`, `<h3 style="color: #1a5276;">Purpose</h3>` — scenario
  paragraph (real-world framing, not just a restatement of the task), then
  Course Learning Outcomes and Program Outcomes lists.
- Task box: `<table style="background-color: #fef9e7; border: 2px solid
  #d4ac0d;">`, `<h3 style="color: #9a7d0a;">Task</h3>` — one concrete
  paragraph stating what the student will build/configure/produce, distinct
  from Purpose's why-it-matters framing and from the detailed step-by-step
  instructions that follow it. Keep it short even on trivial assignments
  (a single sentence is fine); the value is the scanability of a why/what
  pair before the procedural detail starts, not box length.
- Criteria for Success box: `<table style="background-color: #eafaf1;
  border: 2px solid #27ae60;">`, `<h3 style="color: #1e8449;">Criteria for
  Success</h3>` — intro sentence, then one `<ul>` of grading criteria.
- Screenshot-required marker: `<img src="https://img.icons8.com/carbon-copy/2x/camera.png"
  alt="Screenshot required" width="25" height="25" loading="lazy">` after
  any step needing one.
- Inline hint: `<span style="background-color: #ffff00;"><strong>Hint:</strong></span>`.

## Visual template (BIT221 standard, reference for all courses — lecture/resource pages)
- Wrapper: `max-width: 860px`, `color: #2C2C2A`, system font stack.
- Header card: beige `#F1EFE8` / border `#B4B2A9`, 8px radius.
- Learning objectives: purple `#EEEDFE` / `#534AB7`, 2-col grid, checkmark tiles.
- Section headers: green `#E1F5EE` / `#0F6E56` left-border bars.
- Tables: dark header `#444441`, alternating `#ffffff` / `#F1EFE8` rows.
- Callouts: amber `#FAEEDA` / `#854F0B` (notes/best practice), blue
  `#E6F1FB` / `#185FA5` (info).
- Code blocks: dark `#2C2C2A` background, Catppuccin-style syntax colors.
- "Applied" section header (hands-on/code intro): dark variant, bg `#2C2C2A`,
  left-border `#5DCAA5`, title text `#9FE1CB` — distinct from the light green
  section-header bar above.
- In-class activity steps: numbered rows, dark `#444441` number marker,
  alternating `#ffffff` / `#F1EFE8` step backgrounds.
- Section dividers: `border-top: 0.5px solid #D3D1C7; margin: 2.5rem 0`.
- Page titles: topic-only, no "Week N |" prefix duplicated in the title bar
  (the breadcrumb subtitle carries that).

## Workflow
- Confirm major structural decisions before executing (new page structures,
  deleting/merging content, rubric point changes).
- Keep new content unpublished until reviewed.
- Verify current Canvas state (`list_pages`, `list_assignments`,
  `get_course_structure`) before authoring in a session — don't assume prior
  session state still holds.
- Use `canvas-api` MCP tools for all direct edits, not HTML for manual pasting.

## Known Canvas API limitations
- `course_identifier` needs the numeric ID, not the course code string.
- `update_assignment` / `edit_page_content` do full replacement — always
  carry forward the complete current HTML, never a partial patch.
- `points_possible` on quiz-backed assignments is derived from question
  totals — cannot be changed via API, must edit in the Canvas UI.
- Quiz titles/points/content: read-only via API, all edits manual.
- `add_module_item` needs the assignment's `content_id`, not the module item ID.
- Repositioning a module item: `update_module_item` with target position,
  plus a separate call on the item it displaced. Don't re-call
  `add_module_item` with a new position — creates a duplicate.
- `delete_module` auto-removes its module items; `delete_module_item` only
  unlinks a page/assignment, doesn't delete the underlying content — use
  `delete_page` separately if the content itself should go.

## MCP transport & server (canvas-api)
- `canvas-api` runs as a **shared streamable-http server**, not per-client stdio.
  One long-lived process at `http://127.0.0.1:8819/mcp` serves every client
  (Claude Code + Claude Desktop) concurrently. Server code:
  `C:\Users\cburk\canvas-mcp` (`python -m canvas_mcp.server --transport streamable-http`).
- **Credentials are per-request via headers** in HTTP mode (`.env` token is
  ignored). Clients send `X-Canvas-Token` and `X-Canvas-URL`. Configs reference
  `${CANVAS_API_TOKEN}` (a machine env var) — never hardcode the token.
- **Auto-start:** Windows logon task `CanvasMcpHttpServer` runs
  `start_http_server_hidden.vbs` → `start_http_server.cmd` (windowless).
  Log: `C:\Users\cburk\canvas-mcp\http_server.log`.
- **Claude Code** connects via `.mcp.json` (`type: http`). **Claude Desktop**
  connects via the `mcp-remote` stdio→HTTP bridge (`cmd /c npx -y mcp-remote`)
  in `claude_desktop_config.json`. Restart Desktop after config changes.
- **Revert to stdio:** restore `*.stdio.bak` next to each config, disable the
  logon task (`schtasks /Change /TN CanvasMcpHttpServer /DISABLE`).
- If a client shows no canvas-api tools, first check the server is listening
  (`Get-NetTCPConnection -LocalPort 8819`); if not, run the logon task or the
  `.vbs` launcher. A one-off `Event loop is closed` on the very first call after
  a fresh stdio connect was the old failure mode — HTTP mode avoids it.

## Working style
Corey doesn't want timeline estimates, sycophancy, or hedging. Be direct,
concise, and willing to push back. Confirm before big structural or
destructive actions; don't ask permission for routine, established-pattern work.

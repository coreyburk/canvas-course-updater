# Canvas Course Updater — Standing Instructions

## Purpose
Corey is an instructor at Neumont University (cburk@neumont.edu), building and
auditing courses in an Information Systems and Cybersecurity degree program via
the Canvas MCP server (`canvas-api`). Courses in scope share the same Program
Outcomes and the BIT221 visual/structural standard.

## Courses
| Code | Canvas ID | Title | Status |
|---|---|---|---|
| BIT221 | 3631198 | Server Administration I — Windows Server 2025 | ✅ Complete (2026-09-08) |
| BIT281 | 3631199 | Hardware Systems | ✅ Complete (2026-09-03) |
| BIT320 | 3644698 | Shell and Administrative Scripting | ✅ Complete (2026-09-12) |
| PRO221 | 3631288 | Server Admin I — Project: Windows Server | ✅ Complete (2026-09-03) |
| BIT351 | 3631200 | Virtual Systems: Proxmox VE | ✅ Complete (2026-09-03) |
| PRO352 | 3631317 | Virtualization Project: Proxmox (Multi-cluster) | ✅ Complete (2026-09-03) |


<recent_updates>
- BIT320 (Course Complete, 2026-09-12): Fixed Canvas API stability (HTTP server on port 8819). Verified all 15 instructor lecture notes correctly aligned with sequential language mastery structure (Bash → PowerShell → Python → Tool Selection → Monitoring). Updated Week 2 lecture note titles to reflect PowerShell focus (were incorrectly labeled as Bash). Updated module week headers to match course structure. Cleaned stale PaymentService Crisis scenario from documentation. Updated Course Outline page to clearly describe sequential language mastery pedagogy. All 7 labs, 15 instructor lecture notes, 6+ student resource pages, 10 training assignments complete and aligned. Course ready for instruction.

- BIT320 (Lab Notes Complete, 2026-09-11): Created comprehensive Lab Notes Playbook (v1.0 SKILL) for BIT281-format student guidance pages. Published Lab 1.2 Notes (System Command Execution & Output Processing) with left-border boxes and language-specific HOW-TO patterns (bash, PowerShell, Python). Complete Lab Notes coverage: Lab 1.1 (no notes, setup-only), Lab 1.2 (published 2026-09-11), Lab 1.3 (bash patterns), Lab 2.1 (PowerShell objects), Lab 3.1 (Python data structures), Lab 4.1 (tool selection framework), Lab 5.1 (event log analysis). All follow BIT281 five-section format with 4px color-coded left-border boxes. See courses/BIT320.md for full status.

- Workflow: at the end of each Canvas Course Updater session (any work touching CLAUDE.md, courses/{CODE}.md, or repo content), remind Corey to commit changes and provide a suggested commit message. GitHub repo is public: https://github.com/coreyburk/canvas-course-updater, read via web_fetch (no write-back connector currently available on this Enterprise workspace).

- PRO221 (Week 4 Complete, 2026-07-23): All 4 pages published: iSCSI (Page 1), Failover Clustering (Page 2), RDS/MPIO (Page 3), WSUS (Page 4). 2C unpublished/flagged NOT WORKING—needs vet/repair or deletion. 4B unpublished/ready—awaiting publish decision. All assignments conform to 3-box template. OT1 keeping Windows Server 2019 File Services (no 2025 replacement available). courses/PRO221.md and CLAUDE.md updated and committed 2026-07-23.

- PRO221 (Instructor Module & Lecture Notes, 2026-07-27): Created unpublished "Course Outline and Lecture Notes (Not Published - Instructor Use Only)" module at position 1. Added PRO221 - Course Outline page (5-week overview with topics, assignments, training, quizzes per week, certification note). Created 5 comprehensive unpublished instructor lecture notes pages (Weeks 1-5) with teaching context, student misconceptions, lab setup guidance, and cross-week connections. All content grounded in published student-facing pages. Module structure follows BIT281 pattern. CLAUDE.md updated and committed 2026-07-27.

- BIT320 (Course Structure Pages, 2026-09-08): Created instructor-only module (position 1, unpublished) "Course Outline and Lecture Notes (Not Published - Instructor Use Only)" with 6 pages: (1) Course Outline (no point duplication—rubrics are authoritative source), (2-6) Five comprehensive unpublished Instructor Notes pages (Weeks 1-5) following v4.0 canonical format (header, learning objectives, key teaching points, course intro notes, lecture content sections, what's current, reference links). Created 6 published student resource pages: Week 1 (2 pages: Log File Fundamentals, Command Execution and Output Processing), Week 2 (Variables and Functions in Bash), Week 3 (sed and awk Text Processing), Week 4 (Error Handling in Python), Week 5 (Tool Selection and Performance Analysis). All pages 1500-2000 words, student-facing scope. Canvas API server verified running at port 8819. All pages follow BIT221 visual template and employ space-hyphen-space instead of em dashes. Target 7-10 student pages met at 6. See courses/BIT320.md for current status.

- PRO221 (Week 4 Complete, 2026-07-23): All 4 pages published: iSCSI (Page 1), Failover Clustering (Page 2), RDS/MPIO (Page 3), WSUS (Page 4). 2C unpublished/flagged NOT WORKING—needs vet/repair or deletion. 4B unpublished/ready—awaiting publish decision. All assignments conform to 3-box template. OT1 keeping Windows Server 2019 File Services (no 2025 replacement available). courses/PRO221.md and CLAUDE.md updated and committed 2026-07-23. See courses/PRO221.md for current status.
</recent_updates>

## Course Status

**⚠️ IMPORTANT:** Per-course status, decisions, pending work, and history live in `courses/{CODE}.md` 
(e.g., `courses/BIT320.md`, `courses/PRO221.md`). Check the relevant file at the start of any session 
touching that course. Do NOT duplicate course-specific information in CLAUDE.md.

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
- `canvas-api` runs via **stdio directly** from `C:\Users\cburk\canvas-mcp`.
  Each client (Claude Code, Claude Desktop) spawns its own canvas-mcp process.
- **Server code:** `C:\Users\cburk\canvas-mcp` — all MCP tools resolve from here.
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

## Working style
Corey doesn't want timeline estimates, sycophancy, or hedging. Be direct,
concise, and willing to push back. Confirm before big structural or
destructive actions; don't ask permission for routine, established-pattern work.

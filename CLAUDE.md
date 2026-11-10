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

## Workflow
- Confirm major structural decisions before executing (new page structures,
  deleting/merging content, rubric point changes).
- Keep new content unpublished until reviewed.
- Verify current Canvas state (`list_pages`, `list_assignments`,
  `get_course_structure`) before authoring in a session - don't assume prior
  session state still holds.
- Use `canvas-api` MCP tools for all direct edits, not HTML for manual pasting.
- At the end of any session touching `CLAUDE.md`, `courses/`, or repo content,
  remind Corey to commit and suggest a commit message.
- **The GitHub repo is public** (https://github.com/coreyburk/canvas-course-updater).
  Never commit credentials, student data, or copyrighted course material.
  Textbooks live in `textbooks/`, which is gitignored.

## Repo layout
| Path | Holds |
|---|---|
| `CLAUDE.md` | Standing rules. Durable findings belong here, not in the changelog. |
| `CHANGELOG.md` | Session history, newest first. |
| `courses/{CODE}.md` | Per-course status, decisions, pending work. Authoritative. |
| `courses/{CODE}/` | Per-course reference material (lab briefs, audits, training docs). |
| `tools/` | Reusable scripts, safe against any course. |
| `archive/scripts/` | Spent one-off scripts. Course IDs hardcoded, read before reuse. |
| `quizzes/{CODE}/` | Quiz XML for manual Canvas import. |
| `textbooks/` | Gitignored. Copyrighted, local only. |

### Tools
- `tools/emdash_sweep.py --course <id>` - finds and fixes literal em dashes in
  assignment names/descriptions and page bodies. Dry run by default, `--apply`
  writes. Hits are handled **individually**: prose is fixed even when the same
  item has another em dash inside a `<pre>` block, and the one inside `<pre>`
  is reported and left. After each write it re-fetches and compares the item's
  `<pre>` blocks against the originals, so damage to a code sample is reported
  as `PRE CHANGED` rather than discovered later.
  `--include-pre` also rewrites em dashes inside code blocks. Only use it after
  reading the `[CODE]` context lines from a dry run and confirming none is part
  of an actual command; it disables the `<pre>` integrity check by design, so
  verify separately. Page titles are never renamed, since a slug change breaks
  links - though note that a slug only moves if the NEW title normalizes
  differently. Canvas strips an em dash from a slug exactly as it does a
  hyphen, so swapping one for the other leaves the slug untouched; verified on
  BIT320's `quiz-specifications-to-be-created` (2026-11-09). Check the slug
  before assuming a rename is unsafe. On Windows prefix with
  `PYTHONIOENCODING=utf-8` - but note that
  `python -I` silently ignores that, because isolated mode implies `-E`. Reads
  credentials from the canvas-mcp `.env`.
- `tools/audit_canvas_pages.py` - page coverage audit. Course ID is hardcoded;
  edit before reuse.

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
  - **Symptom:** "Event loop is closed" error on ALL Canvas API requests (even simple list_courses)
  - **Root cause:** `src/canvas_mcp/server.py` called `asyncio.run(_validate_token())` during startup to validate Canvas credentials early. This creates a NEW event loop, runs the validation function, and IMMEDIATELY closes the loop when the function exits. When `mcp.run()` starts afterward, it tries to create/use the already-closed event loop, causing all requests to fail with "Event loop is closed."
  - **Why it appeared:** Validating credentials at startup seemed like a good safety check, but `asyncio.run()` by design creates and closes an event loop for that one function. FastMCP's `mcp.run()` creates and manages its OWN event loop - the early `asyncio.run()` closure corrupted this lifecycle.
  - **Fix (committed 2026-09-23 b7905af):** Removed early token validation from `server.py` lines 276-290. Let the server validate credentials on **first request** instead. This allows `mcp.run()` to initialize a fresh event loop without prior closure corruption. Trade-off: credential errors now surface on first API call (not startup), but this is acceptable - better a working server than one that fails on all requests.
  - **Prevention:** **Never call `asyncio.run()` before `mcp.run()` in the same startup process.** If startup validation is needed in future, do it WITHIN the event loop that `mcp.run()` creates, not before. FastMCP manages the event loop; external `asyncio.run()` calls will corrupt it.
  - **Debugging reference:** Symptom appears on the SECOND tool call (first one may succeed if it's simple enough), because the error propagates inconsistently depending on timing.

- **⚠️ ARCHITECTURAL LIMITATION: Concurrent Canvas API connections (2026-09-16 discovery)**
  - **Problem:** stdio MCP is designed for 1:1 client-to-process connections (NOT multiplexing). Running two Claude Code windows simultaneously causes both to spawn separate `canvas-mcp` processes that fight over the same Canvas API credentials.
  - **Symptom:** `CONNECTION_CLOSED` errors when multiple contexts are active
  - **Root cause:** Each context spawns its own subprocess; both attempt Canvas API calls using the same token; race conditions and credential conflicts result
  - **Why HTTP was "unreliable":** The HTTP server mode had the same problem - multiple simultaneous clients connecting to one server caused concurrency conflicts (race conditions, dropped connections, incomplete responses). When switched to stdio, the problem appeared "fixed" because single-context workflows eliminated the conflict scenario.
  - **Workaround:** Keep only ONE active Claude Code window using Canvas API at a time. Close extra windows before Canvas operations. Sequential (not concurrent) usage is the intended pattern.
  - **Do NOT attempt:** Running HTTP server mode to "fix" this - it's deprecated precisely because it had the same underlying issue.
  - **Future improvement:** Would require a proper connection pooling layer or API proxy with request serialization, but not worth the complexity for single-developer use.
  - **Prevention:** Keep `uv.lock` out of the repo if it can't be auto-enforced, or ensure any dependency updates respect the pyproject.toml constraint

## Working style
Corey doesn't want timeline estimates, sycophancy, or hedging. Be direct,
concise, and willing to push back. Confirm before big structural or
destructive actions; don't ask permission for routine, established-pattern work.

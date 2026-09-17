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
| BIT360 | 3644702 | Incident Response & Cyber Forensics | 🔄 In Progress (Weeks 1-6 complete, Weeks 7-10 pending) |
| PRO221 | 3631288 | Server Admin I — Project: Windows Server | ✅ Complete (2026-09-03) |
| BIT351 | 3631200 | Virtual Systems: Proxmox VE | ✅ Complete (2026-09-03) |
| PRO352 | 3631317 | Virtualization Project: Proxmox (Multi-cluster) | ✅ Complete (2026-09-03) |


<recent_updates>
- **BIT360 (Week 6 Complete — Incident Response Recovery & Post-Incident, 2026-09-17)**: Created all 6 comprehensive Week 6 instructor lecture notes pages for BIT360 (Incident Response & Cyber Forensics, Canvas ID 3644702). Pages created unpublished and ready for review. Week 6 covers final IR phases (Containment through Post-Incident Review): (1) Containment Strategies and Active Incident Isolation—network/host-level tactics, type-specific strategies, preventing counter-actions. (2) Eradication and System Remediation—three approaches (rebuild/patch/accept), malware checklist, persistence hunting, scale management. (3) Recovery and Business Continuity—RTO/RPO, recovery phases, backup/DR design, 3-2-1 rule. (4) Post-Incident Review and Lessons Learned—blameless culture, PIR components (timeline/root-cause/control assessment), actionable improvements, meeting facilitation. (5) Crisis Communication and Stakeholder Management—stakeholder map, internal/external communication, regulatory notification, war room coordination, six principles. (6) Real-World Recovery Cases and Current Incident Trends—case studies (Equifax/Exchange/Colonial Pipeline), current threats (RaaS/supply chain/cloud/AI/nation-state), staying current, IR maturity model. All pages follow v4.0 canonical format: purple objectives (6 checkmarks), color-coded sections, tables, 2-4K words, verified links. Created new courses/BIT360-IncidentResponse.md documenting course structure, completion status, and pending work (Weeks 7-10). **CRITICAL LESSON (from Week 4-5 recovery):** Canvas API `edit_page_content` REPLACES entire page; no partial updates. Empty parameter = total deletion. Prevention: all subsequent pages created with complete HTML in single API calls. Weeks 1-5 previously completed. Weeks 7-10 pending (estimated 24-30 additional pages). See courses/BIT360-IncidentResponse.md for full status.

- **ARCHITECTURAL DISCOVERY: Concurrent Canvas API Contexts Cause CONNECTION_CLOSED (2026-09-16)**: Diagnosed persistent CONNECTION_CLOSED errors when two Claude Code windows are open simultaneously. **Root cause:** stdio MCP design is 1:1 (single client per process), but multiple Claude sessions each spawn their own `canvas-mcp` subprocess. Both subprocesses attempt to use the same Canvas API credentials, causing race conditions and credential conflicts. **Why HTTP was "unreliable":** Same concurrent-connection issue—multiple clients → race conditions → intermittent failures. Switching to stdio didn't fix concurrency; it just eliminated the symptom by forcing single-client usage. **Workaround:** Close extra Claude Code windows; keep only ONE active session using Canvas API at a time. **Prevention:** Documented architectural limitation in CLAUDE.md "MCP transport & server" section with explanation and future-improvement notes. Sequential usage is the intended pattern.

- **CRITICAL FIX: Canvas API CONNECTION_CLOSED Root Cause Identified & Fixed (2026-09-16)**: Investigated persistent CONNECTION_CLOSED errors in canvas-api MCP server. **Root cause:** `uv.lock` file pinned fastmcp 3.1.1, which violates pyproject.toml constraint `fastmcp>=2.14.0,<3`. fastmcp 3.x is incompatible with canvas-mcp, causing ImportError on server startup. **Fix applied:** (1) Deleted uv.lock to remove bad dependency pin, (2) Recreated venv with `pip install --force-reinstall 'fastmcp<3'`, downgrading to fastmcp 2.14.7, (3) Verified Canvas API token validation passes. **Result:** CONNECTION_CLOSED should no longer occur. **Prevention:** Documented constraint issue in CLAUDE.md under "MCP transport & server" section. If uv.lock regenerates with fastmcp 3.x, the fix is to delete it and use pip to enforce the <3 constraint. **Note:** This was a recurring issue from yesterday's fix being undone by uv.lock every session.

- BIT320 (Lab 5.2 Resource Pages — Cleanup & Balance Restored, 2026-09-16): Fixed critical issues with three final-project resource pages (Options A/B/C). (1) Restored instructional content: learning objectives, detailed "What to Build" sections, language trade-offs tables, getting-started code examples (Bash/PowerShell/Python), common pitfalls, "What Excellent Looks Like" standards. (2) Deleted 15 unpublished duplicate pages created during iterations (5 per option: -2/-3/-4 versions + old "Week 5 |" naming). Now have ONE published version per option. Submission format remains lean: ONE Word document per option with script/output/screenshots/200-300-word reflection. Result: comprehensive student guidance + practical consolidated deliverables + clean Canvas structure. Lesson: "streamline submission requirements" ≠ "remove instructional content"; balance + cleanup both essential.

- ITH216 (Week 6 EIGRP Pages Prepared, 2026-09-15): Prepared two comprehensive Week 6 student resource pages (Format 2 Modern Minimal), ready for Canvas publication once API connection restored:
  - **Page 1 - EIGRP Fundamentals and Configuration** (1800+ words): EIGRP protocol overview, AS numbers, neighbor discovery (Hello/hold timers/K values), metric calculation, basic configuration, verification commands, troubleshooting Layer 1-3 diagnostics
  - **Page 2 - EIGRP Advanced Topics and Troubleshooting** (2100+ words): Named mode configuration, metric manipulation, path control, summarization, redistribution with loop prevention, neighbor formation diagnosis, DUAL algorithm, convergence optimization
  - Both pages prepared as HTML in scratchpad (week6_page1.html, week6_page2.html) ✅
  - **Blocker:** Canvas API MCP server CONNECTION_CLOSED despite process restart; retry publication when connection restored
  - **Estimated effort to publish:** 5 minutes once API reconnects (canvas-api create_page tool)

- BIT320 (Lab 5.2 Created — Final Project with Student Choice, 2026-09-16): Created NEW Lab 5.2 assignment offering three equal student-choice final project options (100 pts each, shared rubric). Lab 5.1 kept as original (Windows Event Log Analysis). Students complete EITHER Lab 5.1 OR Lab 5.2 (one assignment, not both). Lab 5.2 options: (A) Service Health Monitoring & Auto-Remediation (proactive operations—detects failures, attempts recovery), (B) Configuration Management & Compliance Auditing (infrastructure-as-code—audit against baseline configuration), (C) Windows Event Log Analysis (reactive analytics—same scenario as original Lab 5.1). All three graded on same rubric (Script Quality, Analysis/Reporting, Tool Selection, Documentation at 25 pts each). Created three comprehensive published resource pages (Option A, B, C) with detailed guidance, code examples, getting started sections, and "what excellent looks like." Lab 5.2 assignment (ID: 40341273) links to resource pages. Reinforces course theme: "choose the right tool for the task." Students select based on career interest. Canvas API verified working. courses/BIT320.md updated to reflect dual-assignment structure.

- ITH216 (Week 5 Page 2 Complete, 2026-09-15): Expanded Page 2 (PPP Configuration and WAN Link Management) from minimal to 3500+ words with all five enrichment areas: CHAP Authentication with MD5 hashing and real debug output, PAP vs. CHAP security comparison (real attack scenario showing 5-minute detection vs. never), Compression Algorithms (Predictor 60-70% text, Stacker 50-80% text) with real T1 email link calculation showing $7,200/year upgrade deferral savings, Multilink PPP (RFC 1990) fragmentation with automatic failover, Comprehensive Troubleshooting (Layer 1 physical, Layer 2 LCP/CHAP, Layer 3 IPCP), Security Hardening (key rotation, attack detection, syslog logging), Infrastructure Dependencies, Real-World Context, and seven RFC references. Page 2 now achieves parity with Page 1 depth. Formatted per Format 2 (Modern Minimal). IMPORTANT LESSON: Discovered critical Canvas API behavior—edit_page_content replaces entire page, does not append. Sending 6+ incremental updates wasted tokens thinking they'd accumulate; only last update persisted. Updated CLAUDE.md to document this limitation and prevent repeat waste.

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
and DNS) and BIT351 (1A - Proxmox VE Setup and Configuration) content.

**HTML Table Structure (Correct Format — Updated 2026-09-13):**
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
  `<h3 style="color: #1a5276; margin-top: 0;">Purpose</h3>` — scenario
  paragraph (real-world framing, not just a restatement of the task), then
  Course Learning Outcomes and Program Outcomes lists.
- Task box: `<table style="background-color: #fef9e7; width: 100%; border-collapse: collapse; margin-top: 15px; border: 2px solid #d4ac0d;">`, 
  `<h3 style="color: #9a7d0a; margin-top: 0;">Task</h3>` — one concrete
  paragraph stating what the student will build/configure/produce, distinct
  from Purpose's why-it-matters framing and from the detailed step-by-step
  instructions that follow it. Keep it short even on trivial assignments
  (a single sentence is fine); the value is the scanability of a why/what
  pair before the procedural detail starts, not box length.
- Criteria for Success box: `<table style="background-color: #eafaf1; width: 100%; border-collapse: collapse; margin-top: 15px; border: 2px solid #27ae60;">`, 
  `<h3 style="color: #1e8449; margin-top: 0;">Criteria for Success</h3>` — intro sentence, 
  then one `<ul>` of grading criteria.
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
- **⚠️ CRITICAL: `edit_page_content` REPLACES ENTIRE PAGE** — Every call to `edit_page_content` 
  completely replaces the page content. DO NOT send multiple partial updates expecting them 
  to accumulate — only the last update persists, all previous content is lost. **ALWAYS build 
  the complete page HTML as one monolithic block and send in a SINGLE API call.** Lesson learned 
  2026-09-15 ITH216 expansion: sending 6+ incremental updates (thinking they'd stack) wasted 
  tokens and subscription cost, resulting in only the final update persisting. Always verify 
  the complete HTML includes all sections before sending.
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

- **⚠️ CRITICAL: fastmcp version constraint (2026-09-16 discovery)**
  - canvas-mcp `pyproject.toml` specifies `fastmcp>=2.14.0,<3` (fastmcp 2.x only)
  - fastmcp 3.x is INCOMPATIBLE with canvas-mcp — causes `ImportError: cannot import name 'IdentityAssertionParams'` and CONNECTION_CLOSED in Claude Code
  - **Root cause:** `uv.lock` was generated with fastmcp 3.1.1, violating the <3 constraint. When the venv is recreated (or when Claude Code spawns the MCP server), it pulls from uv.lock which pins the broken version.
  - **Solution:** Delete `uv.lock` and regenerate with `uv sync` to respect the <3 constraint, OR manually reinstall with `pip install --force-reinstall 'fastmcp<3'`

- **⚠️ ARCHITECTURAL LIMITATION: Concurrent Canvas API connections (2026-09-16 discovery)**
  - **Problem:** stdio MCP is designed for 1:1 client-to-process connections (NOT multiplexing). Running two Claude Code windows simultaneously causes both to spawn separate `canvas-mcp` processes that fight over the same Canvas API credentials.
  - **Symptom:** `CONNECTION_CLOSED` errors when multiple contexts are active
  - **Root cause:** Each context spawns its own subprocess; both attempt Canvas API calls using the same token; race conditions and credential conflicts result
  - **Why HTTP was "unreliable":** The HTTP server mode had the same problem—multiple simultaneous clients connecting to one server caused concurrency conflicts (race conditions, dropped connections, incomplete responses). When switched to stdio, the problem appeared "fixed" because single-context workflows eliminated the conflict scenario.
  - **Workaround:** Keep only ONE active Claude Code window using Canvas API at a time. Close extra windows before Canvas operations. Sequential (not concurrent) usage is the intended pattern.
  - **Do NOT attempt:** Running HTTP server mode to "fix" this—it's deprecated precisely because it had the same underlying issue.
  - **Future improvement:** Would require a proper connection pooling layer or API proxy with request serialization, but not worth the complexity for single-developer use.
  - **Prevention:** Keep `uv.lock` out of the repo if it can't be auto-enforced, or ensure any dependency updates respect the pyproject.toml constraint

## Working style
Corey doesn't want timeline estimates, sycophancy, or hedging. Be direct,
concise, and willing to push back. Confirm before big structural or
destructive actions; don't ask permission for routine, established-pattern work.

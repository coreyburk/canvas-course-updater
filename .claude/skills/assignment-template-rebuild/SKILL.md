---
name: assignment-template-rebuild
description: Use when Corey asks to rebuild, fix, standardize, or bring an assignment up to the template (e.g. "rebuild assignment 2C to the standard template", "fix the formatting on 4B", "this assignment doesn't match BIT221's style"). Applies to individual Canvas assignments, not full pages or courses — pairs with canvas-html-lint for the mechanical rule set.
---

# Assignment Template Rebuild

Reference standard: the three-box Purpose/Task/Criteria structure, decided
2026-07-21 after comparing three divergent real implementations (BIT221: no
Task box; BIT281: unstyled `<h3>Task</h3>` heading, div-based Criteria box;
BIT351: styled Task box matching the Purpose/Criteria table pattern).
BIT351's form is canonical — see Step 2. BIT221 and BIT281 assignments still
need backfilling to this standard; treat any assignment missing the styled
Task box, or using a div instead of a table for Criteria, as out of date,
not as an acceptable alternate style.

## Step 0 — Gotchas
Resolve the numeric course ID first. Read the assignment's actual current
HTML with `get_assignment_details` before touching it — never rewrite from
memory or from what the assignment "probably" says. `update_assignment` is a
full replacement: the entire HTML body must be reconstructed, not patched.

## Step 1 — Diagnose before rebuilding
Compare the current assignment against the template below and list what's
missing or wrong:
- No Purpose box, missing CLOs/POs
- **Deliverables section is AFTER Criteria box instead of BEFORE** ← COMMON BUG
- **Point values embedded in Criteria box or criterion descriptions** like "(5 pts)" ← COMMON BUG
- **Separate "Success looks like" statement after Criteria box** ← COMMON BUG
- Broken bullet rendering
- Stale tech references (e.g. VMware where the course is Hyper-V-only, wrong Windows Server version)
- Missing prerequisite/troubleshooting sections

Report the diagnosis before rewriting if there's any ambiguity in scope or
intent — don't silently reinterpret what the assignment is testing. The three
common bugs above have happened repeatedly; check for them specifically.

## Step 2 — Template structure (exact order)
Assignments use a distinct `<table>`-based box style — **not** the div-based
lecture-page callouts from `visual-template-audit`, and not a bare `<div>`
either (BIT281's old Criteria box was a div — that's drift to fix, not a
variant to preserve). Confirmed against live BIT221 (2B - Configure Active
Directory and DNS) and BIT351 (1A - Proxmox VE Setup and Configuration)
content:

**CRITICAL: Element order is strict. Violations invalidate the assignment.**
```
1. Purpose box
2. Task box  
3. Detailed instructions
4. Deliverables section (if assignment has explicit deliverables to list)
5. Criteria for Success box ← FINAL ELEMENT (nothing comes after this)
```

1. **Purpose box** — a `<table style="background-color: #eaf4fb; border: 2px
   solid #2980b9;">` with an `<h3 style="color: #1a5276;">Purpose</h3>`
   heading, containing a scenario paragraph, then `<strong>Course Learning
   Outcomes:</strong>` and `<strong>Program Outcomes:</strong>` each followed
   by a `<ul>`. Never fabricate PO/CLO language — pull it from verified
   Canvas content (syllabus, other assignments in the course, or an explicit
   source Corey provides). The scenario paragraph should carry real-world
   framing, not just restate the task mechanically — BIT351's live Purpose
   boxes do this well already ("the exact steps a junior infrastructure
   engineer follows," "mirrors decisions real infrastructure engineers make
   every day") and are a good model to match when writing or rebuilding one.
2. **Task box** — a `<table style="background-color: #fef9e7; border: 2px
   solid #d4ac0d;">` with an `<h3 style="color: #9a7d0a;">Task</h3>`
   heading, containing one concrete paragraph stating what the student will
   build/configure/produce — distinct from Purpose's why-it-matters framing.
   Keep it short (a sentence or two is fine even for a trivial assignment);
   the value is giving the reader a why/what pair before the procedural
   detail starts, not box length. This box was missing from BIT221 and
   present only as an unstyled heading in BIT281 — add/restyle it as part of
   any rebuild, don't skip it because the assignment predates the standard.
3. **Detailed instructions** — step-by-step, grounded in the actual lab
   environment (VM names, IP scheme, tool versions) already established for
   this course. Include a prerequisites section if the task depends on prior
   assignments' state. Two recurring conventions found in live content:
   - A small camera-icon marker after any step requiring a screenshot:
     `<img src="https://img.icons8.com/carbon-copy/2x/camera.png" alt="Screenshot required" width="25" height="25" loading="lazy">`
   - Inline hints highlighted with `<span style="background-color:
     #ffff00;"><strong>Hint:</strong></span>` inside the relevant list item.
4. **Deliverables section** (plain HTML, not a box) — An optional section
   listing what the student must submit (e.g., "Submit a bash script named
   log_analyzer.sh, a CSV output file, and a README with setup notes"). This
   section comes BEFORE the Criteria box. Use a simple heading and bulleted
   list or paragraph. This is different from the Criteria box — it says what
   to turn in, not how it will be graded.
5. **Criteria for Success box** — a `<table style="background-color:
   #eafaf1; border: 2px solid #27ae60;">` with an `<h3 style="color:
   #1e8449;">Criteria for Success</h3>` heading, an intro sentence
   (`<p>`), then a single `<ul>` of grading criteria. **CRITICAL RULES:**
   - **NEVER list point values inside this box** — points belong ONLY in the
     Canvas rubric, never in assignment text
   - **NEVER embed points inline** — "(5 pts)", "(3 pts)" inside criterion
     descriptions are forbidden; describe WHAT is graded, not HOW MANY points
   - **NEVER add "Success looks like" or other text after this box** — the
     Criteria box itself is the success specification; don't duplicate it
   - **MUST be a `<table>`, not a `<div>`** — BIT281's pre-standardization
     assignments used a div here; convert it when rebuilding
   - **MUST be the FINAL element** — nothing comes after the Criteria box

## Step 3 — Known rendering bugs and structural violations to avoid
See `canvas-html-lint` for the complete mechanical rule set. These are the
highest-frequency violations specifically in assignment rebuilds:

**Structural Violations (found 2026-08-28 in BIT320):**
- ✗ Deliverables section placed AFTER Criteria box (should be BEFORE)
- ✗ Point values embedded in Criteria descriptions, e.g., "(5 pts)", "(3 pts)"
- ✗ Separate "Success looks like" statement added after Criteria box
→ These three bugs commonly appear together; check all three when auditing.

**Rendering Bugs:**
- If an `h3` is immediately followed by a `ul` with no paragraph between
  them, the bullet list breaks the box's rendering in Canvas. Live BIT221
  content always has an intro `<p>` between the `<h3>` and the `<ul>` inside
  both the Purpose and Criteria tables — keep that paragraph, don't drop it.
- No em dashes (literal Unicode `—`) — use comma, colon, or restructure the
  sentence. Space-hyphen-space (` - `) is the correct substitute and is what
  live content actually uses. Scan the **entire** assignment body, not just
  the Purpose/Criteria boxes — a BIT351 review (2026-07-21) found em dashes
  buried in step-by-step instructional prose (e.g. "why update /etc/hosts"
  explanatory paragraphs) that a scan limited to the styled callout boxes
  would have missed entirely.

**HTML/Styling Rules:**
All styling inline (`<style>` is stripped). `<strong>` not `font-weight`.
`<pre style="white-space: pre-wrap;">` for any full code/command blocks;
single inline commands can stay in `<code>` tags without the `<pre>` wrapper.

## Step 4 — Build and confirm
Draft the full new HTML. Present the diagnosis and draft for approval before
writing if this is the first rebuild in a session — subsequent rebuilds in
the same session, following the same established pattern, can proceed
without re-confirming each one. Keep unpublished if it's a new or
significantly restructured assignment; leave published status unchanged for
a like-for-like template fix. `update_assignment` with the complete HTML.

## Step 5 — Report
State what was kept, what was changed, and any gaps that still need Corey's
input (e.g. missing PO language, an unconfirmed prerequisite course).

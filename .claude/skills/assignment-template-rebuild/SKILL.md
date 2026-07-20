---
name: assignment-template-rebuild
description: Use when Corey asks to rebuild, fix, standardize, or bring an assignment up to the template (e.g. "rebuild assignment 2C to the standard template", "fix the formatting on 4B", "this assignment doesn't match BIT221's style"). Applies to individual Canvas assignments, not full pages or courses — pairs with canvas-html-lint for the mechanical rule set.
---

# Assignment Template Rebuild

Reference standard: any current BIT221 assignment (Purpose/Task/Criteria
structure). Used previously for PRO221 1A/1B and PRO221 4B (WSUS).

## Step 0 — Gotchas
Resolve the numeric course ID first. Read the assignment's actual current
HTML with `get_assignment_details` before touching it — never rewrite from
memory or from what the assignment "probably" says. `update_assignment` is a
full replacement: the entire HTML body must be reconstructed, not patched.

## Step 1 — Diagnose before rebuilding
Compare the current assignment against the template below and list what's
missing or wrong: no Purpose box, missing CLOs/POs, points listed inside the
Criteria for Success box, broken bullet rendering, stale tech references
(e.g. VMware where the course is Hyper-V-only, wrong Windows Server version),
missing prerequisite/troubleshooting sections. Report the diagnosis before
rewriting if there's any ambiguity in scope or intent — don't silently
reinterpret what the assignment is testing.

## Step 2 — Template structure (exact order)
1. **Purpose box** (blue callout, `#E6F1FB` / `#185FA5`) — Course Learning
   Outcomes + Program Outcomes this assignment maps to. Never fabricate
   PO/CLO language — pull it from verified Canvas content (syllabus, other
   assignments in the course, or an explicit source Corey provides).
2. **Task / Instructions** — step-by-step, grounded in the actual lab
   environment (VM names, IP scheme, tool versions) already established for
   this course. Include a prerequisites section if the task depends on prior
   assignments' state.
3. **Criteria for Success box** (green) — checklist of what's graded.
   **Never list point values inside this box.**

## Step 3 — Known rendering bugs to avoid
See `canvas-html-lint` for the complete mechanical rule set — these two are
the highest-frequency violations specifically in assignment rebuilds:
- If an `h3` is immediately followed by a `ul` with no paragraph between
  them inside the green box, the bullet list breaks the border in Canvas.
  Fix: wrap in a `div`, and add an intro sentence before every list inside
  that box.
- No em dashes (literal Unicode `—`) — use comma, colon, or restructure the
  sentence.

All styling inline (`<style>` is stripped). `<strong>` not `font-weight`.
`<pre style="white-space: pre-wrap;">` for any code/command blocks.

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

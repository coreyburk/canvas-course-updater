---
name: visual-template-audit
description: Use when Corey asks to check a page or course against the BIT221 visual/structural standard (e.g. "does this page match the template", "audit BIT351 pages for style consistency", "why does this page look different from the others"). Layout/palette compliance check, not a markup-hygiene lint — pairs with canvas-html-lint.
---

# Visual Template Audit

Checks page HTML against the exact BIT221-standard spec in CLAUDE.md "Visual
template" section — the shared look across all in-scope courses. Distinct
from `canvas-html-lint`: this catches style/layout drift (wrong color, missing
component, inconsistent structure), not markup that Canvas will strip or
silently break.

## Step 0 — Gotchas
Resolve the numeric course ID first. Pull live `get_page_content` — never
audit from a remembered description of the page. BIT221 is the reference
standard; when auditing another course, compare against the spec below, not
against BIT221's literal HTML (BIT221 itself may have drifted).

## Step 1 — Scope
One page, a set of pages (e.g. all weeks in a course), or a full course via
`list_pages`. Whole-course audits are most useful right before publishing a
week or at pre-semester QC.

## Step 2 — Pull ground truth
`get_page_content` for every page in scope.

## Step 3 — Check against spec

| Component | Spec | Check for |
|---|---|---|
| Wrapper | `max-width: 860px`, `color: #2C2C2A`, system font stack | Missing wrapper or wrong max-width/color |
| Header card | beige `#F1EFE8` / border `#B4B2A9`, 8px radius | Wrong colors, missing radius |
| Learning objectives | purple `#EEEDFE` / `#534AB7`, 2-col grid, checkmark tiles | Missing grid, wrong colors, no checkmarks |
| Section headers | green `#E1F5EE` / `#0F6E56` left-border bars | Missing left-border accent, wrong colors |
| Tables | dark header `#444441`, alternating `#ffffff` / `#F1EFE8` rows | No header contrast, no zebra striping |
| Callouts | amber `#FAEEDA` / `#854F0B` (notes/best practice), blue `#E6F1FB` / `#185FA5` (info) | Wrong callout type/color for the content, or missing callout styling entirely |
| Code blocks | dark `#2C2C2A` bg, Catppuccin-style syntax colors | Plain/unstyled `<pre>`, no syntax coloring |
| "Applied" section header | dark variant: bg `#2C2C2A`, left-border `#5DCAA5`, title text `#9FE1CB` | Hands-on/code-intro sections using the plain light-green bar instead of this dark variant |
| In-class activity steps | numbered rows: dark `#444441` number marker, alternating `#ffffff` / `#F1EFE8` step backgrounds | Activity/discussion steps not using the numbered-row layout (e.g. a plain `<ol>`) |
| Section dividers | `border-top: 0.5px solid #D3D1C7; margin: 2.5rem 0` | Missing or inconsistent spacing between sections |
| Page titles | topic-only, no "Week N \|" prefix | Redundant week prefix duplicating the breadcrumb subtitle |

Confirmed component-for-component against a live BIT221 page (Week 2 | Page 1
- Active Directory Domain Structure) — the spec above is not a reconstruction,
it's a direct match to that page's HTML.

## Step 4 — Report
Group by page. Distinguish **structural** deviations (missing component
entirely, e.g. no learning-objectives grid) from **stylistic** drift (right
component, wrong color/spacing) — structural issues usually mean the page
predates the current template and is a `legacy-page-merge` candidate, not a
simple restyle.

## Step 5 — Fix (on confirmation)
`edit_page_content` is full replacement — carry forward the complete current
HTML, restyling only the flagged components. If a page looks like it belongs
to an entirely different, older template (multiple structural deviations at
once), stop and flag it for `legacy-page-merge` instead of patching it in
place — per CLAUDE.md, competing page styles should be surfaced and
merged/retired, not left to silently coexist.

## Step 6 — Update course status
If fixes were applied, note it in `courses/{CODE}.md` under Status/Notes so
the next session doesn't re-audit the same pages from scratch.

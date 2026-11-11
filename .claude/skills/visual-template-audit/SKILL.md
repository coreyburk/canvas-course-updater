---
name: visual-template-audit
description: Use when Corey asks to check a page or course against the visual/structural standard (Format 1 BIT221 standard or Format 2 Modern Minimal) - e.g. "does this page match the template", "audit BIT351 pages for style consistency", "why does this page look different from the others". Pairs with canvas-html-lint.
---

# Visual Template Audit

Checks Canvas page HTML against the two sanctioned visual standards across all in-scope courses:
- **Format 1 (BIT221 Standard):** BIT221, BIT281, BIT320, BIT351, PRO221, PRO352 (plus Instructor Lecture Notes across courses)
- **Format 2 (Modern Minimal):** ITH216, BIT360 student resource pages

Distinct from `canvas-html-lint`: `tools/canvas_lint.py` catches mechanical markup-hygiene violations (`<style>`, `<svg>`, em dashes, `<pre>` missing `pre-wrap`, broken Criteria boxes), whereas `visual-template-audit` catches palette, component, and layout drift.

## Step 0 - Low-Context Workflow
Never pull dozens of full HTML pages into LLM context via `get_page_content`. Instead:
1. List pages with `python tools/canvas_sync.py list-pages --course <CODE>`.
2. Pull target page(s) to disk with `python tools/canvas_sync.py pull-page --course <CODE> --page <slug> -o scratchpad/<slug>.html`.
3. Inspect the local file or rebuild it from Markdown using `python tools/canvas_build.py` and push with `python tools/canvas_sync.py push-page`.

## Step 1 - Format 1 Spec (BIT221 Standard)

| Component | Spec | Check for |
|---|---|---|
| Wrapper | `max-width: 860px`, `color: #2C2C2A`, system font stack | Missing wrapper or wrong max-width/color |
| Header card | Beige `#F1EFE8` / border `1px solid #B4B2A9`, `border-radius: 8px`, `padding: 1.5rem 2rem` | Wrong colors, missing radius |
| Learning objectives | Purple `#EEEDFE` / border `#534AB7`, header bar `#ddd7f5`, 2-col grid of white `#ffffff` cards with `✓` checkmarks | Missing grid, wrong colors, no checkmarks |
| Why This Matters / Section bars | Green `#E1F5EE` / `#0F6E56` (or tan `#f5f0e8` / border `#d4a76a` with header bar `#e5dcc8`) | Missing section container or wrong palette |
| Tables | Dark header `#444441` (white text), alternating `#ffffff` / `#F1EFE8` rows | No header contrast, no zebra striping |
| Callouts | Amber `#FAEEDA` / `#854F0B` (notes/pro tips), Blue `#E6F1FB` / `#185FA5` (info) | Wrong callout color or unstyled callout |
| Code blocks | Dark `#2C2C2A` bg, light text `#f0ede8`, `<pre style="... white-space: pre-wrap;">` | Plain/unstyled `<pre>`, missing `pre-wrap` |
| "Applied" / Special section | Dark charcoal bg `#2C2C2A`, border `#5DCAA5`, header bar `#1a1a1a`, title/bold text `#9FE1CB` | Hands-on/mistakes section using light bar instead of dark variant |
| Numbered-row steps | Dark `#444441` number marker, alternating `#ffffff` / `#F1EFE8` step backgrounds | Sequential multi-step explanations using plain `<ol>` where numbered rows belong |
| Reference Links | Light blue `#e6f0f8` / border `#a8c5db`, header bar `#d6e0e8` | Missing reference container |
| Page titles | Topic-only in H1, no duplicated "Week N \|" prefix in H1 when the breadcrumb line above it already carries `Week N - Topic` | Redundant week prefix in H1 |

## Step 2 - Format 2 Spec (Modern Minimal)

| Component | Spec | Check for |
|---|---|---|
| Wrapper | `max-width: 900px`, `color: #1a1a1a`, `line-height: 1.65`, system font stack | Missing wrapper or wrong max-width |
| Header section | `padding: 32px 0 28px 0`, `border-bottom: 1px solid #e5e7eb`, H1 `2.0–2.2rem #1a1a1a`, subtitle `#6b6b6b` (no full background box) | Boxed header on a Format 2 course |
| Learning objectives | `background: #f9f9f9`, `border-left: 4px solid #2563eb`, `border-radius: 8px`, flat list with `#2563eb` `✓` checkmarks | Wrong accent color or missing left border |
| Section headers (H2) | `font-size: 1.5rem`, `color: #1a1a1a`, generous top margin (`40–48px`), no background box | Full-color boxes mixed into Format 2 |
| Callouts | Left-border only (`4px solid`): Blue info (`#eff6ff` / `#2563eb`), Amber warning (`#fef3c7` / `#d97706`) | Full-border callouts |
| Code blocks | `<pre>` with `background: #1e293b; color: #e2e8f0; line-height: 1.8; white-space: pre-wrap;` | Using `<div>` with `display:block` spans instead of `<pre>` for multi-line commands |
| Tables | `border-collapse: collapse`, `thead` bg `#f3f4f6` (`border-bottom: 2px solid #e5e7eb`), alternating `#ffffff` / `#f9f9f9` rows | Unstyled tables |

## Step 3 - Report & Fix
1. Group findings by page, distinguishing **structural** deviations (missing component or competing legacy template → flag for `legacy-page-merge`) from **stylistic** drift (wrong hex code or spacing).
2. Confirm before restyling if competing templates exist in the same course.
3. To fix a page cleanly, either edit the pulled HTML file locally or compile from Markdown with `python tools/canvas_build.py --template page-f1|page-f2`, then push with `python tools/canvas_sync.py push-page`.
4. Log completed audits in `courses/{CODE}.md`.

---
name: canvas-html-lint
description: Use when Corey asks to lint, scan, or fix Canvas HTML rule violations on a page or across a course (e.g. "check for em dashes in BIT351", "lint this page", "scan the course for HTML issues before publishing"). Mechanical rule check, not a style/layout audit — pairs with visual-template-audit.
---

# Canvas HTML Lint

Checks Canvas page/assignment HTML against the mechanical rules in CLAUDE.md
"Non-negotiable standards" and "Canvas HTML rules." Distinct from
`visual-template-audit`: this catches markup-hygiene violations (things that
break rendering or silently get stripped), not palette/layout drift.

## Step 0 — Gotchas
Resolve the numeric Canvas course ID first. Pull live content with
`get_page_content` / `get_assignment_details` — never lint from memory or a
prior session's understanding of a page. Canvas strips `<style>` tags and
`<svg>` silently on save, so a violation may not be visible until the page
next re-renders — flag it anyway.

## Step 1 — Scope
Ask (if not stated): one page, a list of pages, or the whole course? For
whole-course, `list_pages` + `list_assignments`, then pull content for each.

## Step 2 — Pull ground truth
`get_page_content` for pages, `get_assignment_details` for assignment
descriptions. Full HTML, not a summary — the rules below need the raw markup.

## Step 3 — Run checks

| Rule | Detection | Why it matters |
|---|---|---|
| No em dashes | Literal Unicode `—` in text (not `&mdash;`) | Renders as `&mdash;` literal text in Canvas |
| No `<style>` tags | Any `<style>` block | Canvas strips it silently — content loses all styling |
| No inline `<svg>` | Any `<svg` tag | Canvas strips it silently — diagrams must be uploaded images via `<img>` |
| `<strong>` not `font-weight` | Inline `style="font-weight:` on non-`<strong>` tags | Project convention — use the semantic tag |
| Code blocks | `<pre>` without `style="white-space: pre-wrap;"` | Long lines overflow/clip without wrapping |
| No point values in Criteria for Success boxes | Numbers/"pts"/"points" inside the green criteria box content | Points belong in the rubric, not duplicated in prose |
| Criteria box `h3`/`ul` adjacency | An `h3` immediately followed by a `ul` with no intervening `<p>` | Breaks the box's border rendering — needs an intro sentence between the `<h3>` and `<ul>`. Verified against live BIT221 content: the box itself is a `<table>`, not a `div` — the fix is the intro paragraph, not swapping the container element |

## Step 4 — Report
Group findings by page, each with the offending snippet and line/location
context so Corey can verify quickly. Note severity: `<style>`/`<svg>` are
silent-failure bugs (content is currently broken or will break), the rest are
standards violations.

## Step 5 — Fix (on confirmation)
`edit_page_content` / `update_assignment` do full replacement — always carry
forward the complete current HTML with only the violation corrected, never a
partial patch. Batch fixes per page, confirm before each page if changes are
non-trivial (e.g. restructuring a Criteria box needs a wrapping `div`).

## Step 6 — Re-scan
After fixes, re-pull and re-check the same pages to confirm clean before
reporting done.

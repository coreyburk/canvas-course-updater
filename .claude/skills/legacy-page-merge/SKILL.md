---
name: legacy-page-merge
description: Use when a course has two competing page styles (old-style tables vs. current BIT221 template) and Corey wants to merge or retire the old one — e.g. "merge the old Resources pages", "this course has old and new style pages, clean it up". Precedent set in BIT351 (Weeks 2-5 old Resources pages merged into current template).
---

# Legacy Page Merge

Merges an old-style page's unique content into its current-template
counterpart, then retires the old page. Follows the pattern already executed
for BIT351: old-style "Resources" pages (Weeks 2-5) merged into current-
template pages, with unique content (NTP, ha-manager/pmxcfs, dynamic DNS,
RPO/RTO) preserved.

## Step 0 — Gotchas
This is destructive (deletes a page) — confirm scope with Corey before
executing, not after drafting the merge. Pull `get_page_content` on **both**
the old and current-style pages before touching either — never assume overlap
or uniqueness from titles alone. `delete_module_item` only unlinks a page from
a module, it doesn't delete the page itself — use `delete_page` separately
once the module item is repointed or removed.

## Step 1 — Detect competing styles
Within a course, pull `get_page_content` across several weeks/pages and look
for two distinct signatures: current template (learning-objectives grid,
green section-header bars, zebra-striped tables per `visual-template-audit`)
vs. an older layout (plain tables, no color-coded sections, different
heading structure). If found, this is exactly the case CLAUDE.md flags:
"surface it and offer to merge/retire the old one rather than letting both
persist silently."

## Step 2 — Confirm scope
Present which weeks/pages are affected and which pair (old page, current
page) covers the same topic. Get sign-off on the merge plan before extracting
or writing anything.

## Step 3 — Extract unique content from the old page
Diff the old page's content against the current-template page's content by
topic, not by section title. Identify what exists in the old page and is
**not** already covered in the current page — this is the material that must
survive the merge (per the BIT351 precedent: specific technical content the
newer page hadn't covered).

## Step 4 — Merge into the current-template page
Integrate the unique content into the matching section of the current page,
written in the current template's voice and structure (not pasted verbatim
from the old page's formatting). Follow the full visual template — see
`visual-template-audit` for the spec.

## Step 5 — Rewire the module
Update the module item(s) that pointed at the old page so nothing in the
module structure still references it: remove/repoint via `update_module_item`
or `delete_module_item`, then confirm the current page is the one live in the
module.

## Step 6 — Delete the old page
`delete_page` on the old page once nothing references it. Confirm before
deleting — this is not reversible via the API.

## Step 7 — Update course status
Log the merge in `courses/{CODE}.md`: which old pages were retired, which
current pages absorbed them, and what specific unique content was preserved.
This is the record the next session needs — don't rely on git history or
memory to reconstruct it later.

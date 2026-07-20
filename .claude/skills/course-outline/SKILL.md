---
name: course-outline
description: Use when Corey asks to create, build, or refresh a Course Outline for a Canvas course (e.g. "Create a Course Outline for BIT351", "build the course outline for course X"). Produces an instructor-only pacing/content reference page.
---

# Canvas Course Outline Playbook

Reference standard: BIT221's `bit221-course-outline` page.

## Step 0 — Gotchas
Resolve the numeric Canvas course ID first — never trust the course code
string alone. Canvas is the source of truth: build from live content, never
fabricate topics or outcomes. Output is instructor-only: always unpublished,
always in its own dedicated module.

## Step 1 — Pull ground truth
- `list_assignments` — names, points, due dates
- `get_course_structure` — modules, weekly SubHeader groupings of
  Assignments / Training / Quizzes / Resources
- For each topic area, ground the Topics bullets in `get_page_content` of the
  matching lecture/resource page (preferred) or `get_assignment_details` of
  the matching training/lab assignment — not just titles
- Note any non-weekly items (capstones, course evals, practice quiz banks,
  follow-on-course sprints) to flag separately, not folded into a week

## Step 2 — Confirm weekly grouping
Short, topic-based week names (e.g. "Week 3 - Clustering and High
Availability"), one grounded outcome sentence per week.

## Step 3 — Per-week table
H2 header + intro sentence, then one Category/Items table with only the
applicable rows: Topics, Assignments, LinkedIn Learning (or other training,
linked), Quiz(zes).

## Step 4 — Exact visual template
- Top overview box: bg `#eaf4fb`, border `2px solid #2980b9`, h3 color `#1a5276`
- Week h2: `border-left: 4px solid #534AB7`, color `#26215C`, `margin-top: 2.5rem`
- Table: `border: 1px solid #ccc`, header row bg `#2C2C2A` / color `#fff`,
  alternating row bg `#f9f9f9` / white, Category column bold, ~18% width
- Closing note box(es): bg `#F1EFE8`, border `2px solid #5F5E5A` — one for
  non-weekly items, one for training-resource sourcing caveats

## Step 5 — Build and wire in
1. `create_page`, unpublished, titled `"{CODE} - Course Outline"`
2. `create_module` named exactly `"Course Outline (Not Published - Instructor
   Use Only)"`, position 1, `published: false`
3. `add_module_item` — the outline page, position 1, the ONLY item in that module

## Step 6 — Maintenance
The outline is a derived artifact. Re-sync it to Canvas whenever
assignments/points/structure change — never edit it as if it were the source
of truth Canvas has to match.

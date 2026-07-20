---
name: lecture-notes-playbook
description: Use when Corey asks to convert legacy lecture notes into Canvas pages, build new lecture/resource pages for a course, or audit existing Canvas lecture pages against the standard template.
---

# Canvas Lecture Notes Playbook

## Step 0 — Universal gotchas
Resolve the course to its numeric Canvas ID before any API call. Canvas
strips `<style>` tags and raw `<svg>` — all styling inline, diagrams as
uploaded images referenced via `<img>`. Pages created unpublished until
approved.

## Step 1 — Inventory the source material
Where do the notes live and how are they organized (by week/topic/section)?
Faithful conversion, full modernization, or skeleton-first? How are content
gaps handled — placeholders, drafted by Claude, or ignored? What's the
target version/scope?

## Step 2 — Propose page structure before building
One page per topic, grouped by week, or grouped by week + theme (usually
best — logical progression, but related topics consolidated). Get sign-off
before creating anything.

## Step 3 — Per-page template (six sections, every page)
1. Learning Objectives — checklist/card grid
2. Core Concept — main content, prose + supporting tables
3. What's Current/New — callout flagging anything version/standard-specific
4. Applied/Technical — code, commands, procedures, worked examples
5. In-Class Activity / Discussion Questions
6. Reference Links — prefer authoritative current sources over aggregators

## Step 4 — Visual design (see CLAUDE.md "Visual template" — BIT221 standard)
Zebra-striped tables, ≥7:1 contrast headers, `border-left` section accents,
`margin-top: 2.5rem` between sections, dark monospace code blocks, no
icons/emoji anywhere.

## Step 5 — Authoring standards
No em dashes. Never reconstruct content from memory — pull actual source
text first. Show 1-2 example pages, get sign-off on tone, then batch the
rest. Split a page only if topics are conceptually unrelated. Diagrams:
real uploaded images, never inline SVG.

## Step 6 — Per-page build loop
Pull source section → check against current standards/version and stated
course objectives → draft with the template → build/upload diagrams →
create/update the Canvas page unpublished → report kept/updated/gaps filled
→ on approval, next page, update status tracker.

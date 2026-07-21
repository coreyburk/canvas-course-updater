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

## Step 3 — Per-page template (eight sections, every page)
Pages must go beyond assignment-task support into real supporting/
foundational depth — not just what the assignment requires to complete it.
Precedent: BIT221 Week 4 pages (2026-07-21), rebuilt from an assignment-
task-only version after Corey flagged that pages were "heavily focused on
directly supporting the assignments" and needed to also cover why the topic
matters, real-world usage, dependencies, and security concerns.

1. **Learning Objectives** — checklist/card grid. Include objectives for the
   deeper content below (e.g. "identify how X is misused as an attack
   vector"), not just the mechanical task objectives.
2. **Core Concept** — main content, prose + supporting tables. Must include
   a **"Why this matters"** passage: who actually does this work in a real
   organization, why it matters more than the assignment's literal task, and
   any relevant real-world tension or debate (e.g. an assignment teaches a
   traditional practice that current industry guidance has since revised —
   surface that, don't just teach the traditional practice silently).
3. **Dependencies and Interactions** — what this topic requires to work at
   all (functional levels, other roles/services, prior-week infrastructure)
   and what it silently affects elsewhere. Tie back to specific earlier
   weeks/pages by name where applicable.
4. **Security Considerations** — real risks and mitigations tied to the
   topic, not just assignment-specific gotchas. Prefer citing a concrete,
   verifiable source (MITRE ATT&CK technique ID, NIST guidance, vendor
   security documentation) over a generic "be careful" statement.
5. **What's Current/New** — callout flagging anything version/standard-
   specific.
6. **Applied/Technical** — code, commands, procedures, worked examples.
7. **In-Class Activity / Discussion Questions** — include at least one
   question that probes the Security Considerations or Dependencies content,
   not only the mechanical task.
8. **Reference Links** — prefer authoritative current sources over
   aggregators. Any factual, security, or standards claim (a CVE, an
   attack technique, a guidance document) must be verified via WebSearch
   before it's written — never cite from memory, and never fabricate a URL.

## Step 4 — Visual design (see CLAUDE.md "Visual template" — BIT221 standard)
Zebra-striped tables, ≥7:1 contrast headers, `border-left` section accents,
`margin-top: 2.5rem` between sections, dark monospace code blocks, no
icons/emoji anywhere.

## Step 5 — Authoring standards
No em dashes. Never reconstruct content from memory — pull actual source
text first, and verify external facts/URLs via WebSearch rather than
trusting recall. Show 1-2 example pages, get sign-off on tone and depth,
then batch the rest. Split a page only if topics are conceptually unrelated.
Diagrams: real uploaded images, never inline SVG.

## Step 6 — Per-page build loop
Pull source section → check against current standards/version and stated
course objectives → draft with the template → build/upload diagrams →
create/update the Canvas page unpublished → report kept/updated/gaps filled
→ on approval, next page, update status tracker.

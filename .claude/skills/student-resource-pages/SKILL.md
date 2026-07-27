---
name: student-resource-pages
description: Use when building Canvas pages for student-facing lecture, reference, or concept documentation (published pages in weekly course modules). Distinct from instructor teaching notes.
---

# Canvas Student Resource Pages Playbook

**Version:** 1.0  
**Last Updated:** 2026-07-27

---

## Overview

Student resource pages are **published, student-facing** pages that support learning objectives and assignments. They differ fundamentally from instructor teaching notes in scope, audience, and content depth.

---

## Step 0 — Gotchas

- Resolve course to numeric Canvas ID first
- Always publish (unless explicitly marked instructor-only)
- Place in course module by week (positions 2+), never in instructor-only module
- No time estimates in headers
- No em dashes (space-hyphen-space only)
- Canvas strips `<style>` tags and inline SVG — all styling inline via `style=` attributes
- No point values, rubric references, or grading criteria in content

---

## Step 1 — Student-Focused Scope

Student pages are **1500–2000 words**, optimized for student comprehension and assignment support, NOT instructor preparation.

**Content must include:**
- Learning objectives (what students will do, not why instructors need to teach it)
- Core concepts grounded in student examples (not instructor troubleshooting)
- Practical procedures students can execute themselves
- Real examples from student context (assignments, labs, real tools)
- Security framed as "understand this risk," not "how to exploit this"

**Content must NOT include:**
- Why students struggle / instructor pedagogical notes
- Expected output values for grading purposes
- Common student errors (instructor reference, not student learning)
- Troubleshooting decision trees (instructor-facing)
- Grading rubrics or success criteria
- Facilitation guides or discussion answers

---

## Step 2 — Page Naming & Placement

**Naming convention:**
`Week [N] | Page [#] - [Topic]`

**Module placement:**
- Published in course module (positions 2 onward)
- Never in instructor-only module
- Grouped by week in course structure

---

## Step 3 — Per-Page Structure

Use the same canonical format as teaching notes (Header, Learning Objectives, Content Sections, Discussion Questions, References), but:

**Reduce scope by 40-50%:**
- Learning Objectives: Same (100–150 words, 4-8 objectives)
- Core Concepts: 400–600 words (vs. 600–900 for teaching notes)
- Applied/Technical: 600–900 words (vs. 800–1200 for teaching notes)
- Optional sections: Brief or omitted

**Reframe all content for students:**
- Examples: From student assignments, not grading scenarios
- Procedures: Steps students execute, not instructor scaffolding
- Security: "Understand why this matters" not "how to troubleshoot this"
- Tone: Clear, accessible, encouraging — not directive

**Skip these entirely:**
- Teaching Agenda (instructor-only)
- Why Students Struggle (instructor prep)
- Expected output walkthroughs with real data (grading reference)
- Troubleshooting decision trees
- Lab success criteria (belongs in assignment, not page)

---

## Step 4 — Content Standards

**Word count:** 1500–2000 total (tight, focused, readable)

**Breakdown:**
- Learning Objectives: 100–150 words
- Core Concepts: 400–600 words
- Applied/Technical: 600–900 words
- Optional sections (Discussion, References): 200–350 words combined

**Writing principles:**
- Every concept grounded in student-executable example
- Real data, never fabricated outputs
- Real command syntax students actually use (not placeholders)
- Direct, clear language (no instructor jargon unexplained)
- Encourage questions; frame as reference, not directive

**Visual standards:**
- Same header/objectives/content boxes as teaching notes
- Same color scheme (no modifications)
- All tables with solid 1px black borders on all cells
- No em dashes, no `<style>` tags, no inline SVG

---

## Step 5 — Optional Sections for Student Pages

**Discussion Questions** (rare, only if used in class):
- 2–3 questions students can discuss in pairs/groups
- Answerable from the page + prior knowledge
- No "correct" answer — open-ended

**What's Current** (if version-specific):
- Flag what technology/version this covers
- Example: "As of Windows Server 2025, the WindowsFeature resource..."

**Looking Ahead** (if connecting to next topic):
- Brief preview of how this connects to next week
- Do NOT assign homework here — that's the assignment's job

**Reference Links** (curated only):
- 3–5 links maximum
- Only resources that genuinely deepen understanding
- Prefer official docs, Microsoft Learn, or primary sources

---

## Step 6 — Authoring Workflow

1. **Extract learning objectives** from assignment and course outcomes
2. **Draft core concepts** with student-level examples (NOT instructor depth)
3. **Build applied/technical** section from actual CLI/UI outputs (run yourself, never fabricated)
4. **Add optional sections** only if they serve student learning (not instructor prep)
5. **Apply canonical styling** (same as teaching notes, Step 3)
6. **Publish** (place in course module, not instructor-only)

---

## Critical Rules (DO NOT VIOLATE)

### Must Have
- ✓ Header box (week/topic, title, no publication status needed)
- ✓ Learning Objectives (purple box with darker header background)
- ✓ Core Concepts section (green or tan box)
- ✓ Applied/Technical section (green or tan box, alternating color)
- ✓ References (if applicable)

### Must NOT Do
- ✗ Include "Instructor Use Only" indicator (pages are published, student-facing)
- ✗ Include Teaching Agenda (instructor-only)
- ✗ Include expected output values for grading
- ✗ Include common student errors (instructor reference)
- ✗ Include troubleshooting decision trees
- ✗ Include rubric alignment or grading criteria
- ✗ Exceed 2000 words (keep focused and readable)
- ✗ Use fabricated data or example outputs
- ✗ Assume instructor audience in writing tone

### Publishing
- ✓ Always publish (don't leave unpublished by default)
- ✓ Place in course module, position 2+
- ✓ Not in instructor-only module

---

## Distinction from Teaching Notes

| Aspect | Teaching Notes | Student Pages |
|--------|---|---|
| Audience | Instructors only | Students (primary) |
| Published | No | Yes |
| Module | Instructor-only | Course module by week |
| Length | 2500–3500 words | 1500–2000 words |
| Scope | Comprehensive, deep | Focused, essential only |
| Example focus | Grading/troubleshooting | Student executable |
| Common errors | Explained, listed | Not included |
| Expected outputs | Real grading data | Not included |
| Tone | Preparatory, diagnostic | Encouraging, accessible |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-27 | Initial specification — student resource pages distinct from instructor teaching notes. Focus on student learning, not instructor prep. Scope 1500–2000 words. No Teaching Agenda, no expected outputs for grading, no troubleshooting guides. |

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

Student pages are **1500–2000 words per topic**, optimized for student comprehension and assignment support, NOT instructor preparation.

**CRITICAL SCOPE NOTE (Updated 2026-09-17):**
- **DO NOT limit student resource pages to one page per week.** Create multiple pages per week by topic as needed.
- Pages should be organized by **topic granularity**, not by week alone.
- A single week may warrant **2-4+ comprehensive resource pages** depending on topic complexity and assignment scope.
- **Example:** Week 1 of BIT360 could span: InfoSec Overview (1 page), Process Explorer Guide (1 page), Network Monitoring with TCPView (1 page), Sysmon Event Logging (1 page), Virtualization Setup Guide (1 page).
- **Comprehensive coverage is the goal.** Each topic deserves depth sufficient for students to master it independently before attempting assignments.
- Pages within the same week should cross-reference each other naturally but remain independently readable.

**Content must include:**
- Learning objectives (what students will do, not why instructors need to teach it)
- "Why This Matters" section (motivation, relevance to career/assignments)
- Core concepts grounded in student examples (not instructor troubleshooting)
- Practical procedures students can execute themselves (step-by-step numbered tables)
- Real-world narratives with specific details (timestamps, process names, event IDs, incident timelines)
- Worked examples showing correct approach (before/after comparisons, code snippets, screenshots)
- Comparison tables (trade-offs between options: VirtualBox vs. Hyper-V, risk levels, approaches)
- Common mistakes section (3-5+ detailed mistakes with "Why It's Wrong" and "How to Fix" guidance)
- Troubleshooting tables for labs/procedures (Problem/Cause/Solution format)
- Security framed as "understand this risk" or "recognize this pattern," not "how to exploit this"

**Content must NOT include:**
- Why students struggle / instructor pedagogical notes
- Expected output values for grading purposes (only for learning context)
- Teaching Agenda or instructor facilitation guides
- Grading rubrics or success criteria (those belong in assignments)
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

**Word count:** 2500–4500+ total (matches assignment complexity — simple tools: 2500-3000, complex labs: 3500-4500+)

**Breakdown (for complex assignments):**
- Learning Objectives: 150–200 words (5-6 objectives)
- Why This Matters: 200–300 words (motivation/relevance)
- Core Concepts with procedures: 1500–2500 words (includes step-by-step tables, comparison tables, examples)
- Common Mistakes table: 500–800 words (3-5+ detailed mistakes with fixes)
- References: 200–300 words

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
- ✓ Learning Objectives (purple box with darker header background, 5-6 objectives)
- ✓ Why This Matters section (green header, student-focused motivation)
- ✓ Core Concepts section(s) with step-by-step procedures (tan boxes, 1500-2500 words)
- ✓ Real-world examples with specific details (timestamps, event IDs, process names)
- ✓ Common Mistakes section (3-5+ entries with fixes, table or narrative format)
- ✓ Troubleshooting section for labs/procedures (Problem/Cause/Solution table)
- ✓ References (curated, 3-5 links maximum)

### Must NOT Do
- ✗ Include "Instructor Use Only" indicator (pages are published, student-facing)
- ✗ Include Teaching Agenda (instructor-only)
- ✗ Include grading rubrics or success criteria (belongs in assignment)
- ✗ Include fabricated data or example outputs (use real tool output, real incident details)
- ✗ Use vague "students learn from mistakes" pedagogy (be specific about what/why/how)
- ✗ Assume instructor audience in writing tone
- ✗ Limit to 2000 words when assignment complexity warrants depth (see word count guidance above)

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
| Length | 2500–4000 words | 2500–4500+ words (matched to complexity) |
| Scope | Comprehensive, deep | Depth matched to assignment requirements |
| Procedures | Teaching approach | Step-by-step tables students execute |
| Examples | Industry case studies | Real-world narratives with specific details |
| Common mistakes | For instructor awareness | 3-5+ entries with "Why/How to Fix" |
| Troubleshooting | Decision trees (instructor) | Problem/Cause/Solution tables (student) |
| Expected outputs | Real grading data | Real tool/system outputs (learning context) |
| Tone | Preparatory, diagnostic | Encouraging, practical, accessible |

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.1 | 2026-09-17 | **MAJOR UPDATE based on BIT360 Week 1 creation.** Revised word count to 2500-4500+ (previously 1500-2000). Added required sections: "Why This Matters" (motivation), step-by-step procedure tables, comparison tables, real-world incident narratives with timestamps/event IDs, detailed common mistakes (3-5+ entries), troubleshooting tables (Problem/Cause/Solution). Shifted from prescriptive length limits to complexity-matched depth. Updated comparison table vs. Teaching Notes to reflect new depth parity. These changes reflect learnings from creating three 3500-4500 word pages that provide sufficient detail for independent student learning. |
| 1.0 | 2026-07-27 | Initial specification — student resource pages distinct from instructor teaching notes. Focus on student learning, not instructor prep. Scope 1500–2000 words. No Teaching Agenda, no expected outputs for grading, no troubleshooting guides. |

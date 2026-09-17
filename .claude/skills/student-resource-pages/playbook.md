# Canvas Student Resource Pages Playbook
**Version:** 1.0  
**Last Updated:** 2026-09-17  
**Canonical Example:** Week 1 | Student Page 1 - Log File Fundamentals (BIT320)  
**Status:** LIVE — BIT320 pages are the authoritative format for student-facing resources.

---
## Overview
This document defines the canonical format for **student resource pages** across Canvas courses. The format is grounded in BIT320's student pages: **practical, motivation-driven guidance** that helps students understand topics and complete assignments.

**Key principle:** Student pages should enable independent learning. They answer "Why does this matter?" and "How do I approach this?" rather than "Here's what I'll teach." Content clarity, worked examples, and actionable steps trump comprehensive coverage.

**CRITICAL SCOPE NOTE (Updated 2026-09-17):**
- **Student pages are DISTINCT from instructor lecture notes.** Instructor notes teach; student pages guide learners.
- Student pages focus on **assignment completion, concept clarity, and practice.**
- A single week may warrant 2-5 student pages depending on assignment scope and tool complexity.
- **Example:** Week 1 of BIT360 (IR Fundamentals) includes: (1) InfoSec Fundamentals & Risk Assessment (3,500+ words), (2) SysInternals Tools Hands-On (3,500+ words), (3) Lab Environment Setup (4,000+ words).
- **Practical guidance is the goal.** Worked examples, real-world narratives, step-by-step procedures, and detailed tables ensure students can learn independently and complete assignments.
- **Content depth scales with assignment complexity.** Pages supporting single tools/concepts: 2,500-3,000 words. Pages supporting multi-step assignments or complex labs: 3,500-4,500+ words.

---
## Step 0 — Universal Gotchas
- Resolve the course to its numeric Canvas ID before any API call
- Canvas strips `<style>` tags and raw `<svg>` — all styling inline via `style=` attributes
- Pages created unpublished until approved
- No em dashes (use space-hyphen-space instead)
- Never reconstruct content from memory — pull actual source/verify external facts via WebSearch
- Every student page is **self-contained and independent.** No references to other pages or cross-course links.
- **Tone:** Clear, encouraging, practical. Assume students are learning for the first time.

---
## Step 1 — Page Structure (CANONICAL FORMAT)
Every student resource page must follow this exact structure in this order.

### 1A. Header Card (Beige background) — REQUIRED
**Purpose:** Title, week/topic context, purpose statement.

```html
<div style="background-color: #f1efe8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #b4b2a9;">
  <div style="font-size: 0.8rem; color: #6b6960; margin-bottom: 0.25rem;">Week [N] - [Topic Area]</div>
  <h1 style="margin: 0 0 0.5rem 0; font-size: 1.6rem; color: #2c2c2a;">[Title]</h1>
</div>
```

**Rules:**
- Background: #f1efe8 (beige)
- Border: 1px solid #b4b2a9 (tan)
- Border-radius: 8px
- Padding: 1.5rem 2rem (generous)
- Margin-bottom: 2rem
- Week/topic line: 0.8rem, color #6b6960, margin-bottom 0.25rem
- Title (h1): 1.6rem, color #2c2c2a, no top margin, 0.5rem bottom margin
- **NO "Instructor Use Only" badge** — This is student-facing
- **NO cross-document references**

---
### 1B. Learning Objectives (Purple header, grid layout) — REQUIRED
**Purpose:** What students will be able to do after this page.

Use same format as instructor notes (purple #eeedfe, 2-column grid, checkmarks). Text should be student-centric: "Understand", "Apply", "Build", "Recognize" rather than "Master" or "Contextualize."

```html
<div style="background-color: #eeedfe; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #534ab7;">
  <div style="background-color: #ddd7f5; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #534ab7;">Learning Objectives</h2>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
    <div style="background-color: #ffffff; border-radius: 6px; padding: 0.75rem 1rem; display: flex; align-items: flex-start; gap: 0.5rem;">
      <span style="color: #534ab7; flex-shrink: 0;">✓</span>
      <span>[Objective 1]</span>
    </div>
    <!-- 3-6 total objectives -->
  </div>
</div>
```

**Rules:** Same as instructor notes (2-column grid, white cards, checkmarks, no intro paragraph).

---
### 1C. Why This Matters (Green header) — REQUIRED
**Purpose:** Motivate students — explain relevance to their career, assignments, or broader context.

```html
<div style="background-color: #e1f5ee; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #0F6E56;">
  <div style="background-color: #c8ddd5; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #0f6e56;">Why This Matters</h2>
  </div>
  <p style="margin: 0;">[1-2 paragraph explanation of relevance to student work or career]</p>
</div>
```

**Rules:**
- Background: #e1f5ee (light green)
- Border: 1px solid #0F6E56 (dark green)
- Header bar: background #c8ddd5, color #0f6e56
- **This is THE motivational section.** Answer: "Why should I care about this?"
- Tie to assignments, real-world scenarios, or career relevance
- Keep to 1-2 paragraphs (concise)
- **NOT instructor context** — Student perspective only

---
### 1D. Core Concepts / Getting Started (Tan header, content sections) — REQUIRED
Content organized into logical sections. Use light tan/amber (same as instructor lecture content sections).

```html
<div style="background-color: #f5f0e8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #d4a76a;">
  <div style="background-color: #e5dcc8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #6b5d4f;">[Section Title]</h2>
  </div>
  
  <h3 style="color: #6b5d4f; margin-top: 0;">[Subsection Heading]</h3>
  <p style="margin-bottom: 0.75rem;">Explanation paragraph...</p>
  <ul style="margin: 0 0 1rem 0; padding-left: 1.5rem;">
    <li>Bullet point</li>
    <li>Bullet point</li>
  </ul>
  
  <!-- Include step-by-step tables, comparison tables, examples, code blocks, etc. -->
  
  <div style="background-color: #FAEEDA; padding: 12px 16px; margin: 12px 0; border-radius: 4px;">
    <p style="margin: 0; font-size: 0.9rem;"><strong style="color: #854F0B;">Pro tip:</strong> [Practical advice for students]</p>
  </div>
</div>
```

**Rules:**
- Outer div: background #f5f0e8, border 1px solid #d4a76a, border-radius 8px, padding 1.5rem 2rem, margin-bottom 2rem
- Header bar: background #e5dcc8, padding 0.75rem 1rem, border-radius 4px, margin-bottom 1rem
- Header h2: 1.05rem, color #6b5d4f, margin 0
- h3 subsections: color #6b5d4f, margin-top 0
- Paragraphs: margin-bottom 0.75rem
- Pro tip boxes: background #FAEEDA, padding 12px 16px, margin 12px 0, border-radius 4px, color #854F0B for strong text
- **REQUIRED: Include worked examples, real-world scenarios, code snippets, or screenshots** — Don't just explain concepts
- **REQUIRED: Use step-by-step tables** — Numbered procedures with specific instructions
- **REQUIRED: Use comparison tables** — Show trade-offs, differences between approaches
- **REQUIRED: Use "Pro tip" and "Common mistake" boxes** — Practical student guidance embedded throughout
- **Length:** Develop sections fully. Simple concepts: 1-2 subsections. Complex procedures: 3-6 subsections with multiple examples each.

---
### 1E. Common Mistakes / Pitfalls (Dark charcoal background or table format) — REQUIRED
Can use either narrative format OR table format (preferred for complex assignments):

**Narrative format:**
```html
<div style="background-color: #2c2c2a; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; margin-top: 2.5rem; color: #f0ede8; border: 1px solid #5DCAA5;">
  <div style="background-color: #1a1a1a; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #9fe1cb;">Common Mistakes to Avoid</h2>
  </div>
  <p style="margin: 0 0 1rem 0;"><strong style="color: #9FE1CB;">❌ [Mistake title]:</strong> [Explanation of what students do wrong and why it fails]</p>
  <p style="margin: 0;"><strong style="color: #9FE1CB;">✓ Instead:</strong> [What students should do]</p>
</div>
```

**Table format (recommended for procedures/assignments):**
```html
<table style="width: 100%; border-collapse: collapse; background: white; margin-bottom: 48px;">
  <thead style="background: #f3f4f6; border-bottom: 2px solid #e5e7eb;">
    <tr>
      <th style="padding: 14px 16px; text-align: left; color: #1a1a1a; border-right: 1px solid #e5e7eb;">Mistake</th>
      <th style="padding: 14px 16px; text-align: left; color: #1a1a1a; border-right: 1px solid #e5e7eb;">Why It's Wrong</th>
      <th style="padding: 14px 16px; text-align: left; color: #1a1a1a;">How to Fix</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background: white; border-bottom: 1px solid #e5e7eb;">
      <td style="padding: 14px 16px; color: #1a1a1a; border-right: 1px solid #e5e7eb;">[Mistake title]</td>
      <td style="padding: 14px 16px; color: #6b6b6b; border-right: 1px solid #e5e7eb;">[Consequence/why it fails]</td>
      <td style="padding: 14px 16px; color: #6b6b6b;">[Correct approach with specific details]</td>
    </tr>
  </tbody>
</table>
```

**Rules:**
- For simple topics (1-3 mistakes): Use dark charcoal narrative format
- For complex assignments (4+ mistakes): Use table format with explicit "How to Fix" column
- List 3-5 common pitfalls students encounter (not just 2-4)
- Explain the consequence (why it's wrong)
- Provide specific corrective approach (not just "do it right")
- **Optional: Cross-reference to earlier sections** where students can review if they make these mistakes

---
### 1F. Reference Links (Light blue background) — REQUIRED
```html
<div style="background-color: #e6f0f8; border-radius: 8px; padding: 1.5rem 2rem; border: 1px solid #a8c5db;">
  <div style="background-color: #d6e0e8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <p style="margin: 0; font-size: 0.8rem; color: #5a6f7f;"><strong>Resources</strong></p>
  </div>
  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">
    <li><a style="color: #185fa5;" href="[URL]">[Title]</a> - [Brief description of what students will find there]</li>
  </ul>
</div>
```

**Rules:** Same as instructor notes (external links only, no Canvas cross-references).

---
## Step 2 — Student Page vs. Instructor Lecture Notes

| Aspect | Instructor Lecture Notes | Student Resource Pages |
|--------|------------------------|----------------------|
| **Audience** | Instructor prep/teaching | Student independent learning |
| **Purpose** | What instructor teaches | What student does/understands |
| **Tone** | Formal, comprehensive, context-rich | Conversational, practical, assignment-focused |
| **"Why" section** | Key Teaching Points (actionable) | Why This Matters (motivation) |
| **Content** | Breadth of knowledge, current trends | Depth in ONE topic, step-by-step guidance |
| **Examples** | Industry case studies, current news | Worked examples, real-world narratives, code snippets, screenshots |
| **Procedures** | Teaching approach | Step-by-step tables with specific instructions |
| **Troubleshooting** | Not included | Detailed problem/cause/solution tables |
| **Sections** | Learning Objectives, Teaching Points, Lecture Content, What's Current, Reference Links | Learning Objectives, Why This Matters, Core Concepts (with procedures/examples), Common Mistakes, Reference Links |
| **Length** | 2500-4000 words (comprehensive) | 2500-4500+ words (depth matches assignment complexity) |

---
## Step 3 — Inline Styles Only (Same as Instructor Notes)
- All styling via `style=""` attributes
- No `<style>` tags (Canvas strips them)
- No `<script>` tags
- All colors use hex codes from palette below
- Font families use system sans-serif
- No em dashes — use space-hyphen-space instead

---
## Step 4 — Color Palette (CANONICAL — Same as Instructor Notes)
Use exact same palette as instructor lecture notes (beige headers, purple objectives, green "Why This Matters", tan content, amber tips, charcoal special sections, blue reference links).

---
## Step 5 — Key Principles

1. **Self-contained and independent** — Students should understand this page without reading others.
2. **Motivation first** — "Why This Matters" appears early (after objectives) to keep students engaged.
3. **Depth over breadth** — One topic done thoroughly with multiple examples beats many topics done shallowly.
4. **Worked examples required** — Don't just explain concepts; show:
   - Real-world narratives with specific details (timestamps, process names, IP addresses, event IDs)
   - Step-by-step procedures in numbered tables with explicit instructions
   - Before/after comparisons showing correct vs. incorrect approaches
   - Code blocks, screenshots, or configuration examples
5. **Comparison tables for trade-offs** — Help students choose between options (VirtualBox vs. Hyper-V, risk levels, approaches)
6. **Assignment-aligned content** — Content directly supports the week's assignment(s) with enough detail to complete them independently.
7. **Troubleshooting sections for labs/procedures** — Table format with Problem/Cause/Solution for common failures.
8. **Encouraging tone** — Assume some students are struggling; be supportive and practical.
9. **No instructor context** — No "teaching notes," "common misconceptions," "what's current," or "for instructors only." Save those for instructor lectures.
10. **Common mistakes as learning tool** — 3-5+ detailed mistakes (not just 2-3). Explain WHY each is wrong and HOW to fix it specifically.
11. **Length = complexity** — Pages supporting simple tools (single learning objective): 2,500-3,000 words. Pages supporting multi-step labs or complex concepts: 3,500-4,500+ words.

---
## Step 6 — Examples (CANONICAL)

**BIT320 (Simpler assignment, single tool focus):**
- `Week 1 | Student Page 1 - Log File Fundamentals` — ~2,500 words, single Linux tool, basic procedures

**BIT360 Week 1 (Complex assignments, multiple topics):**
- `Week 1.1 Student Guide: InfoSec Fundamentals & Risk Assessment` — 3,500+ words, CIA triad, ACIO framework, risk matrix, assignment walkthrough with common mistakes table
- `Week 1.2 Student Guide: SysInternals Tools Hands-On` — 3,500+ words, three tools, detailed procedures, real incident narrative with timestamps, common mistakes table
- `Week 1.3 Student Guide: Lab Environment Setup` — 4,000+ words, hypervisor comparison table, step-by-step VM creation, snapshot strategy, troubleshooting table with 5 scenarios, optimization tips

**Key takeaway:** Pages supporting complex assignments that span multiple tools/concepts should be 3,500-4,500+ words with abundant tables, examples, and troubleshooting guidance.

---
## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.1 | 2026-09-17 | **Major update based on BIT360 Week 1 creation.** Updated length guidance to 2500-4500+ words (previously 1500-2500). Added requirement for step-by-step tables, comparison tables, real-world narratives with specific details, and troubleshooting sections. Changed common mistakes from optional to required (3-5+ entries in table format when possible). Emphasized worked examples: real incidents with timestamps, process names, event IDs. Added troubleshooting table format (Problem/Cause/Solution). Updated Key Principles to reflect depth-over-breadth approach and complexity-matched content length. |
| 1.0 | 2026-09-17 | Initial release based on BIT320 canonical format. Established clear distinction between instructor lecture notes (v4.0) and student resource pages. Added "Why This Matters" green section as student motivation anchor. Documented common mistakes/pitfalls section. Color palette identical to instructor notes but section purposes are distinct. |

---

## ARGUMENTS: Review and establish student resource page format for BIT360 Week 1 creation (2-5 pages per week, assignment-focused, practical examples)

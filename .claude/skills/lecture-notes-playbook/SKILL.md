---
name: lecture-notes-playbook
description: Use when Corey asks to convert legacy lecture notes into Canvas pages, build new lecture/resource pages for a course, or audit existing Canvas lecture pages against the standard template.
---

# Canvas Lecture Notes Playbook

**Version:** 4.0  
**Last Updated:** 2026-07-27  
**Based on:** PRO221 Week 1 Teaching Notes (canonical simple, clean format)

---

## Overview

This document defines the canonical format for **instructor lecture notes** across Canvas courses. The format is grounded in PRO221 Week 1's proven approach: **clean, minimal, non-busy styling** that keeps focus on content, not visual decoration.

**Key principle:** Instructor notes should be easy to scan, not decorated. Content clarity trumps visual polish.

---

## Step 0 — Universal Gotchas

- Resolve the course to its numeric Canvas ID before any API call
- Canvas strips `<style>` tags and raw `<svg>` — all styling inline via `style=` attributes
- Pages created unpublished until approved
- No em dashes (use space-hyphen-space instead)
- Never reconstruct content from memory — pull actual source/verify external facts via WebSearch

---

## Step 1 — Inventory the Source Material

- Where do the notes live and how are they organized (by week/topic/section)?
- Faithful conversion, full modernization, or skeleton-first?
- How are content gaps handled — placeholders, drafted by Claude, or ignored?
- What's the target version/scope?

---

## Step 2 — Propose Page Structure Before Building

- One page per topic, grouped by week, or grouped by week + theme (usually best — logical progression, but related topics consolidated)
- Get sign-off on scope and session time before creating anything

---

## Step 3 — Per-Page Structure (CANONICAL FORMAT)

Every lecture note page must follow this exact structure in this order:

### 3A. Header Card (Beige) — REQUIRED

**Purpose:** Title, course context, and brief scope.

```html
<div style="background: #F1EFE8; border: 2px solid #5F5E5A; border-radius: 8px; padding: 16px 20px; margin-bottom: 2.25rem;">
  <p style="color: #2C2C2A; font-size: 20px; margin: 0 0 4px;"><strong>Teaching Notes - Week [N] - [Topic]</strong></p>
  <p style="color: #5F5E5A; font-size: 13px; margin: 0;">[Course Code] Instructor Notes - [Brief scope: assignments covered, key themes]</p>
</div>
```

**Rules:**
- Beige background: #F1EFE8
- Medium-gray border: 2px solid #5F5E5A
- Padding: 16px vertical, 20px horizontal
- Title: 20px, strong, no top margin, 4px bottom margin
- Subtitle: 13px, color #5F5E5A, no margin
- Margin-bottom: 2.25rem (generous space before next section)

---

### 3B. Learning Objectives (Purple) — REQUIRED

**Purpose:** What students should understand by the end of the week/session.

```html
<div style="background: #EEEDFE; border-left: 4px solid #534AB7; padding: 10px 14px; margin-bottom: 1rem;">
  <p style="margin: 0; font-size: 16px; color: #26215C;"><strong>Learning Objectives</strong></p>
</div>

<p style="font-size: 13.5px; color: #2C2C2A; margin-bottom: 0.75rem;"><strong>By the end of this page, students should understand:</strong></p>

<ul style="font-size: 13.5px; color: #2C2C2A; margin: 0 0 1rem; padding-left: 20px;">
  <li style="margin-bottom: 6px;">Objective 1</li>
  <li style="margin-bottom: 6px;">Objective 2</li>
  <li style="margin-bottom: 6px;">Objective 3</li>
</ul>
```

**Rules:**
- Header bar: light purple background #EEEDFE, left border 4px solid #534AB7
- Header text: 16px, strong, color #26215C (dark purple)
- Intro paragraph: 13.5px, strong lead-in ("By the end of...")
- List: plain `<ul><li>` bullets, 13.5px, margin-bottom 6px per item
- **NO checkmarks, NO grid layout, NO icons** — simple bullet list
- Margin-bottom for entire section: 1rem

---

### 3C. Content Sections (Light Green or Dark) — REQUIRED

Content is organized into logical sections, each prefaced with a **left-border header bar**. Two color schemes:

#### Light Green (Conceptual/Fundamentals)

```html
<div style="background: #E1F5EE; border-left: 4px solid #0F6E56; padding: 10px 14px; margin-bottom: 1rem;">
  <p style="margin: 0; font-size: 16px; color: #04342C;"><strong>Section Title</strong></p>
</div>

<p style="font-size: 13.5px; color: #2C2C2A; margin-bottom: 0.75rem;"><strong>Subsection Heading</strong></p>
<p style="font-size: 13.5px; color: #2C2C2A; margin-bottom: 0.75rem;">Body text paragraph 1...</p>
<p style="font-size: 13.5px; color: #2C2C2A; margin-bottom: 0.75rem;">Body text paragraph 2...</p>
```

**Colors:**
- Header background: #E1F5EE (light green)
- Border-left: 4px solid #0F6E56 (dark green)
- Header text: 16px, strong, color #04342C (very dark green)
- Body text: 13.5px, color #2C2C2A, margin-bottom: 0.75rem per paragraph
- **No background on body content** — white background only

---

#### Dark (Technical Procedures & Lab Walkthrough)

```html
<div style="background: #2C2C2A; border-left: 4px solid #5DCAA5; padding: 10px 14px; margin-bottom: 1rem;">
  <p style="margin: 0; font-size: 16px; color: #9FE1CB;"><strong>Technical Procedures & Configuration</strong></p>
</div>

<div style="background: #2C2C2A; border-radius: 6px; padding: 16px; border: 0.5px solid #3a3a4a; margin-bottom: 1rem;">
  <p style="color: #9FE1CB; margin-bottom: 1rem;"><strong>Procedure: [Step-by-step title]</strong></p>
  <p style="color: #cdd6f4; font-size: 13px; margin-bottom: 0.75rem;"><strong>Step 1:</strong> Description...</p>
  <p style="color: #cdd6f4; font-size: 13px; margin-bottom: 0.75rem;"><strong>Step 2:</strong> Description...</p>
  
  <pre style="white-space: pre-wrap; background: #1a1a19; padding: 10px; border-radius: 4px; color: #cdd6f4; font-size: 12px; margin-top: 0.5rem;">Expected output or code example
goes here with literal formatting
preserved exactly as shown</pre>
</div>
```

**Colors:**
- Header background: #2C2C2A (charcoal/near-black)
- Border-left: 4px solid #5DCAA5 (teal/mint)
- Header text: 16px, strong, color #9FE1CB (light teal)
- Procedure block background: #2C2C2A (same as header)
- Procedure title: color #9FE1CB, margin-bottom: 1rem
- Step text: color #cdd6f4, font-size: 13px, margin-bottom: 0.75rem
- Code/pre block background: #1a1a19 (darker), color #cdd6f4, font-size: 12px, padding: 10px

---

### 3D. HR Dividers (Between Sections) — REQUIRED

```html
<hr style="border: none; border-top: 0.5px solid #D3D1C7; margin: 2.5rem 0 0;">
```

**Rules:**
- Border: none (removes default browser border)
- Border-top only: 0.5px solid #D3D1C7 (very light gray)
- Margin: 2.5rem top (generous space before next section), 0 left/right, 0 bottom
- Used between every major section to create visual breathing room

---

### 3E. Closing Summary Card (Beige) — OPTIONAL

```html
<div style="background: #F1EFE8; border: 2px solid #5F5E5A; border-radius: 8px; padding: 16px;">
  <p style="color: #2C2C2A; margin: 0 0 8px;"><strong>Summary: [Topic]</strong></p>
  <p style="font-size: 13.5px; color: #2C2C2A; margin: 0;">Summary text...</p>
</div>
```

**Rules:**
- Same styling as header card (beige, 2px border)
- Title: 0 top margin, 8px bottom margin
- Body text: 13.5px, no margin

---

## Step 4 — Color Reference (MINIMAL PALETTE)

| Element | Color | Usage |
|---------|-------|-------|
| Overall text | #2C2C2A | All body text, headers |
| Background (page) | white | Default |
| Header cards (beige) | #F1EFE8 | Title/summary cards |
| Header card border | #5F5E5A | 2px border on cards |
| Learning Objectives header | #EEEDFE | Background of LO header bar |
| Learning Objectives border | #534AB7 | Left border (4px) |
| Learning Objectives text | #26215C | Text in LO header |
| Conceptual section header bg | #E1F5EE | Light green background |
| Conceptual section border | #0F6E56 | Left border (4px) |
| Conceptual section text | #04342C | Text in header |
| Technical section header bg | #2C2C2A | Dark charcoal background |
| Technical section border | #5DCAA5 | Left border (4px, teal) |
| Technical section text | #9FE1CB | Text in header (light teal) |
| Code block bg | #1a1a19 | Pre/code block (darker) |
| Code block text | #cdd6f4 | Text in code blocks |
| HR divider | #D3D1C7 | Horizontal rule (very light gray) |
| Subtitle text | #5F5E5A | Secondary text (header subtitles) |

**Overall impression:** Limited, high-contrast palette. Beige/gray for structure, purple for objectives, green for concepts, dark charcoal for technical. No decorative colors.

---

## Step 5 — Authoring Standards

- No em dashes — use space-hyphen-space
- No decorative icons, checkmarks, or visual flourishes
- No background colors on body paragraphs (only section headers get color)
- No nested styling (keep structure flat and readable in HTML)
- All styling inline via `style=` attributes
- Generous whitespace: 2.5rem between major sections, 1rem between subsections, 6px between list items
- Body text: 13.5px, line-height: 1.7
- Section headers: 16px, strong weight
- Code/pre text: 12px, monospace, white-space: pre-wrap

**Operational Requirements (critical for instructor readiness):**
- **Always show expected outputs** — what success looks like, command results, step-by-step results
- **Document common student errors** with root causes and reproducible fix procedures
- **Include troubleshooting decision trees** — flowchart-style diagnostic paths with actual PowerShell commands
- **Include security/operational implications** — why certain approaches are risky, what could go wrong
- **Document resource behavior edge cases** — limitations of built-in resources, misconceptions, when to use Script resource escape-hatch
- **Include cross-week connections** — how prior weeks inform this week, how this week feeds forward
- **Include strategic context** — when different approaches are appropriate (e.g., on-premises vs. cloud, push vs. pull)
- **Include validation/testing procedures** — how to confirm assumptions (e.g., idempotence testing, connectivity verification)

---

## Step 6 — Word Count Target (Minimum, Not Maximum)

**Teaching Notes Pages:** Minimum 2000 words per page. **No maximum.** Complexity determines length.

**Guideline breakdown (minimums, not ceilings):**
- Learning Objectives: 100–150 words minimum
- Conceptual/Fundamentals: 600–900 words minimum
- Technical Procedures & Walkthroughs: 800–1200 words minimum
- Common Errors, Security, Decision Trees: 400–750 words minimum
- Optional (Closing Summary): 100–200 words

**Why this approach:**
- Instructors need depth to teach confidently and troubleshoot submissions
- 2000+ word minimum ensures content is grounded in specifics, not bullet points
- **If a topic is complex and needs more explanation, add all necessary detail**—don't truncate
- If 4000 or 5000 words are required to cover expected outputs, edge cases, security implications, and troubleshooting thoroughly, that's correct
- Completeness and clarity trump brevity
- Student-facing pages are shorter (1500–2000); teaching notes are richer by design

---

## Critical Rules (DO NOT VIOLATE)

### Must Have
- ✓ Header card (beige, 2px border)
- ✓ Learning Objectives (purple header bar with left border, plain bullet list)
- ✓ Content sections with left-border header bars (light green OR dark charcoal, never nested)
- ✓ HR dividers between major sections (2.5rem margin)
- ✓ Expected outputs and common errors documented
- ✓ All styling inline (no `<style>` tags)

### Must NOT Do
- ✗ Use nested divs for section headers (one header bar only, no "inner header")
- ✗ Use checkmarks, icons, or grid layouts in learning objectives
- ✗ Add background colors to body paragraphs (only section headers get color)
- ✗ Use em dashes or smart quotes
- ✗ Invent new color schemes (stick to palette above)
- ✗ Use `<style>` tags (all inline)
- ✗ **Truncate content due to word count** — if a topic needs 4000+ words to explain thoroughly with all necessary detail, use all 4000+ words

### Flexible Elements
- Number of sections (varies by topic)
- Use of closing summary card (optional)
- Whether to include both light green and dark sections (topic-dependent)
- Specific subheading text (adjust for content)

---

## Examples

### Simple Section (Conceptual)

```html
<div style="background: #E1F5EE; border-left: 4px solid #0F6E56; padding: 10px 14px; margin-bottom: 1rem;">
  <p style="margin: 0; font-size: 16px; color: #04342C;"><strong>Why This Matters for Instructors</strong></p>
</div>

<p style="font-size: 13.5px; color: #2C2C2A; margin-bottom: 0.75rem;"><strong>Conceptual Foundation</strong></p>
<p style="font-size: 13.5px; color: #2C2C2A; margin-bottom: 0.75rem;">Students often think of baselines as a single number ("the CPU should be 10%"). Reality is more nuanced...</p>
<p style="font-size: 13.5px; color: #2C2C2A; margin: 0;">Teaching moment: Show a real 10-minute baseline chart with normal variance...</p>

<hr style="border: none; border-top: 0.5px solid #D3D1C7; margin: 2.5rem 0 0;">
```

### Procedure Section (Technical)

```html
<div style="background: #2C2C2A; border-left: 4px solid #5DCAA5; padding: 10px 14px; margin-bottom: 1rem;">
  <p style="margin: 0; font-size: 16px; color: #9FE1CB;"><strong>Assignment 1A Walkthrough</strong></p>
</div>

<div style="background: #2C2C2A; border-radius: 6px; padding: 16px; border: 0.5px solid #3a3a4a; margin-bottom: 1rem;">
  <p style="color: #9FE1CB; margin-bottom: 1rem;"><strong>Procedure 1: Setting up DCS Data Collector Set</strong></p>
  <p style="color: #cdd6f4; font-size: 13px; margin-bottom: 0.75rem;"><strong>Step 1:</strong> Open Perfmon, create a new Data Collector Set...</p>
  <p style="color: #cdd6f4; font-size: 13px; margin-bottom: 0.75rem;"><strong>Step 2:</strong> Add the following counters: Processor \% Processor Time, Memory \% Committed Bytes In Use, PhysicalDisk \Disk Queue Length</p>
  
  <pre style="white-space: pre-wrap; background: #1a1a19; padding: 10px; border-radius: 4px; color: #cdd6f4; font-size: 12px; margin-top: 0.5rem;">Expected output when students submit DCS export CSV:
Timestamp,Processor,Memory,DiskQueue
2026-07-27 09:00:00,15.2,45.3,0
2026-07-27 09:00:10,18.5,46.1,1</pre>
</div>

<hr style="border: none; border-top: 0.5px solid #D3D1C7; margin: 2.5rem 0 0;">
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 4.0 | 2026-07-27 | **Complete rewrite: Simple, clean format based on PRO221 Week 1.** Removed complex nested divs, grid layouts, checkmarks. Restored left-border header bars, plain bullet lists, generous whitespace. Minimal color palette. Emphasis on content clarity over visual decoration. This is the canonical format going forward. |
| 3.2 | 2026-07-27 | Restructured Steps (moved teaching notes comparison, lab standards, word count to Steps 4-6). |
| 3.1 | 2026-07-27 | Added three new content standards subsections. |
| 3.0 | 2026-07-23 | Merged spec + process into single source of truth. |

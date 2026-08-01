---
name: lecture-notes-playbook
description: Use when Corey asks build new lecture/resource pages for a course, to convert legacy lecture notes into Canvas pages, or audit existing Canvas lecture pages against the standard template.
---
# Canvas Lecture Notes Playbook
**Version:** 4.0  
**Last Updated:** 2026-08-01  
**Canonical Example:** Lecture Notes - PC History (BIT281 Canvas course)
**Status:** LIVE — PC History is the authoritative format. All 21 BIT281 lecture notes will be remediated to this spec.

---
## Overview
This document defines the canonical format for **instructor lecture notes** across Canvas courses. The format is grounded in the PC History lecture note: **clean, minimal, non-busy styling** that keeps focus on content, not visual decoration.

**Key principle:** Instructor notes should be easy to scan, self-contained, and independent. Content clarity trumps visual polish. No cross-document references. No "Looking Ahead" sections.

---
## Step 0 — Universal Gotchas
- Resolve the course to its numeric Canvas ID before any API call
- Canvas strips `<style>` tags and raw `<svg>` — all styling inline via `style=` attributes
- Pages created unpublished until approved
- No em dashes (use space-hyphen-space instead)
- Never reconstruct content from memory — pull actual source/verify external facts via WebSearch
- Every lecture note is **independent and self-contained**. No references to other lecture notes or "Looking Ahead" sections.

---
## Step 1 — Page Structure (CANONICAL FORMAT)
Every lecture note page must follow this exact structure in this order.

### 1A. Header Card (Beige background) — REQUIRED
**Purpose:** Title, week/topic context, publication status.

```html
<div style="background-color: #f1efe8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #b4b2a9;">
  <div style="font-size: 0.8rem; color: #6b6960; margin-bottom: 0.25rem;">Week [N] - [Topic Area]</div>
  <h1 style="margin: 0 0 0.5rem 0; font-size: 1.6rem; color: #2c2c2a;">[Title]</h1>
  <div style="margin-top: 0.75rem; font-size: 0.85rem; color: #854f0b; background-color: #faeeda; display: inline-block; padding: 0.25rem 0.75rem; border-radius: 4px;">Instructor Use Only - Not Published</div>
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
- Status badge: inline-block, background #faeeda, color #854f0b, padding 0.25rem 0.75rem, border-radius 4px, font-size 0.85rem, margin-top 0.75rem
- **NO subtitle with course code or scope**
- **NO cross-document references**

---
### 1B. Learning Objectives (Purple header, grid layout) — REQUIRED
**Purpose:** What students should understand by the end of the week.

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
    <div style="background-color: #ffffff; border-radius: 6px; padding: 0.75rem 1rem; display: flex; align-items: flex-start; gap: 0.5rem;">
      <span style="color: #534ab7; flex-shrink: 0;">✓</span>
      <span>[Objective 2]</span>
    </div>
    <!-- repeat for each objective -->
  </div>
</div>
```

**Rules:**
- Outer div: background #eeedfe, border 1px solid #534ab7, border-radius 8px, padding 1.5rem 2rem, margin-bottom 2rem
- Header bar inside: background #ddd7f5, padding 0.75rem 1rem, border-radius 4px, margin-bottom 1rem
- Header h2: 1.05rem, color #534ab7, margin 0
- Grid: 2 columns, gap 0.75rem
- Grid items: white background, border-radius 6px, padding 0.75rem 1rem, display flex, align-items flex-start, gap 0.5rem
- Checkmark span: color #534ab7, flex-shrink 0 (checkmark ✓, not an icon)
- Objective text: no additional styling
- **NO intro paragraph ("By the end of...")**
- **NO numbered list**
- **Grid layout with white cards is REQUIRED**

---
### 1C. Key Teaching Points (Blue header, flat bullet list) — REQUIRED
**Purpose:** Actionable teaching points. Consolidation of old "Teaching Agenda" (CORE/DEPTH/HOMEWORK merged into one flat list).

```html
<div style="background-color: #E6F1FB; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #2980b9;">
  <div style="background-color: #d6e0f0; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #185FA5;">Key Teaching Points</h2>
  </div>
  <ul style="margin: 0; padding-left: 1.25rem;">
    <li>[Point 1]</li>
    <li>[Point 2]</li>
    <li>[Point 3]</li>
    <!-- merged from old CORE, DEPTH, HOMEWORK into single flat list -->
  </ul>
</div>
```

**Rules:**
- Outer div: background #E6F1FB, border 1px solid #2980b9, border-radius 8px, padding 1.5rem 2rem, margin-bottom 2rem
- Header bar inside: background #d6e0f0, padding 0.75rem 1rem, border-radius 4px, margin-bottom 1rem
- Header h2: 1.05rem, color #185FA5, margin 0
- List (ul): plain HTML `<ul><li>`, padding-left 1.25rem, margin 0
- List items: no extra styling, no subsection headers
- **NO "CORE (50 min)" or "DEPTH (If time permits)" subsections**
- **NO "HOMEWORK / Async" subsection**
- **Single flat bullet list only**
- **Time references completely removed** (no "50 min", no "if time permits", etc.)
- Merge CORE/DEPTH/HOMEWORK bullets into one consolidated list

---
### 1D. Optional: Course Intro Notes (Green header, if present in Week 1) — CONDITIONAL
**Purpose:** First-session housekeeping (Week 1 only, usually).

```html
<div style="background-color: #e1f5ee; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #0F6E56;">
  <div style="background-color: #c8ddd5; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #0f6e56;">Course Intro Notes</h2>
  </div>
  <p style="margin: 1rem 0;"><strong>Points to cover first session:</strong></p>
  <ul style="margin: 0 0 1.5rem 0; padding-left: 1.25rem;">
    <li>[Point 1]</li>
    <li>[Point 2]</li>
  </ul>
  <p>[Additional prose if needed]</p>
</div>
```

**Rules:**
- Background: #e1f5ee (light green)
- Border: 1px solid #0F6E56 (dark green)
- Header bar: background #c8ddd5, color #0f6e56
- **Only in Week 1 or week 1 of a new course**
- **Can be omitted if not relevant**

---
### 1E. Lecture Content Sections (Tan/amber or dark charcoal headers) — REQUIRED
Content organized into logical sections, each with a left-border header bar. Two color schemes depending on content type.

#### Light Tan/Amber (Conceptual/Fundamentals)
```html
<div style="background-color: #f5f0e8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #d4a76a;">
  <div style="background-color: #e5dcc8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #6b5d4f;">Lecture Content: [Section Title]</h2>
  </div>
  
  <h3 style="color: #6b5d4f; margin-top: 0;">[Subsection Heading]</h3>
  <p style="margin-bottom: 0.75rem;"><strong>Bold intro if needed</strong></p>
  <p style="margin-bottom: 0.75rem;">Body paragraph 1...</p>
  <p style="margin-bottom: 0.75rem;">Body paragraph 2...</p>
  
  <div style="background-color: #FAEEDA; padding: 12px 16px; margin: 12px 0; border-radius: 4px;">
    <p style="margin: 0; font-size: 0.9rem;"><strong style="color: #854F0B;">Teaching note:</strong> [Practical classroom advice or common student misconception]</p>
  </div>
</div>
```

**Rules:**
- Outer div: background #f5f0e8, border 1px solid #d4a76a, border-radius 8px, padding 1.5rem 2rem, margin-bottom 2rem
- Header bar: background #e5dcc8, padding 0.75rem 1rem, border-radius 4px, margin-bottom 1rem
- Header h2: 1.05rem, color #6b5d4f, margin 0
- h3 subsections: color #6b5d4f, margin-top 0, margin-bottom 0.75rem (implied by paragraph margins)
- Paragraphs: margin-bottom 0.75rem, no other styling
- Teaching note boxes: background #FAEEDA, padding 12px 16px, margin 12px 0, border-radius 4px, color #854F0B for strong text, font-size 0.9rem

#### Dark Charcoal (Technical Procedures, Discussion, Special Content)
```html
<div style="background-color: #2c2c2a; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; margin-top: 2.5rem; color: #f0ede8; border: 1px solid #5DCAA5;">
  <div style="background-color: #1a1a1a; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #9fe1cb;">The Story of Mel - Discussion Guide</h2>
  </div>
  
  <p style="margin: 0 0 1rem 0;"><strong style="color: #9FE1CB;">What it is:</strong> [Description]</p>
  <p style="margin: 0 0 1rem 0;"><strong style="color: #9FE1CB;">Why it matters:</strong> [Context]</p>
  
  <h3 style="color: #9FE1CB; border-top: 1px solid #444441; padding-top: 16px; margin-top: 16px; margin-bottom: 1rem;">Discussion Prompts</h3>
  
  <p style="margin: 0 0 0.5rem 0;"><strong style="color: #9FE1CB;">1. [Prompt question]?</strong></p>
  <p style="margin: 0 0 1rem 0;">Expected answer: [Response guidance]</p>
  
  <p style="margin: 0 0 0.5rem 0;"><strong style="color: #9FE1CB;">2. [Prompt question]?</strong></p>
  <p style="margin: 0;">[Response guidance]</p>
</div>
```

**Rules:**
- Outer div: background #2c2c2a, border 1px solid #5DCAA5, border-radius 8px, padding 1.5rem 2rem, margin-bottom 2rem, margin-top 2.5rem, color #f0ede8
- Inner header bar: background #1a1a1a, padding 0.75rem 1rem, border-radius 4px, margin-bottom 1rem
- Header h2: 1.05rem, color #9fe1cb, margin 0
- Bold text/labels: color #9FE1CB (light teal)
- Regular text: color #f0ede8 (light gray)
- h3 subsections: color #9FE1CB, border-top 1px solid #444441, padding-top 16px, margin-top 16px, margin-bottom 1rem
- Paragraphs: margin-bottom 1rem (or 0 for last), color #f0ede8

---
### 1F. What's Current (Amber background) — REQUIRED
**Purpose:** Instructor context on current market/technology state, relevant to the topic.

```html
<div style="background-color: #faeeda; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #854F0B;">
  <div style="background-color: #f0d4b8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <p style="margin: 0; font-size: 0.8rem; color: #854f0b;"><strong>What's Current</strong></p>
  </div>
  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">
    <li><strong>[Topic (year range)]:</strong> [Current state, e.g., "AMD's Ryzen lines are competitive with Intel"]</li>
    <li><strong>[Topic (year range)]:</strong> [Current state, e.g., "Apple's M-series processors are ARM-based"]</li>
  </ul>
</div>
```

**Rules:**
- Background: #faeeda (pale amber)
- Border: 1px solid #854F0B (amber)
- Header bar: background #f0d4b8, padding 0.75rem 1rem, border-radius 4px, margin-bottom 1rem
- Header p: 0.8rem, color #854f0b, no margin
- List: font-size 0.9rem, padding-left 1.25rem, margin 0
- List items: `<strong>[Topic (year range)]:</strong>` followed by description
- **Grounded in specific years and real developments**
- **Helps instructors answer "Is this still true?" and "What's changed?"**

---
### 1G. Reference Links (Light blue background) — REQUIRED
**Purpose:** External links only (Wikipedia, official docs, forums, etc.). No internal Canvas cross-references.

```html
<div style="background-color: #e6f0f8; border-radius: 8px; padding: 1.5rem 2rem; border: 1px solid #a8c5db;">
  <div style="background-color: #d6e0e8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <p style="margin: 0; font-size: 0.8rem; color: #5a6f7f;"><strong>Reference Links</strong></p>
  </div>
  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">
    <li><a style="color: #185fa5;" href="[URL]">[Title]</a> - [Brief description]</li>
    <li><a style="color: #185fa5;" href="[URL]">[Title]</a> - [Brief description]</li>
  </ul>
</div>
```

**Rules:**
- Background: #e6f0f8 (light blue)
- Border: 1px solid #a8c5db (blue)
- Header bar: background #d6e0e8, padding 0.75rem 1rem, border-radius 4px, margin-bottom 1rem
- Header p: 0.8rem, color #5a6f7f, no margin
- List: font-size 0.9rem, padding-left 1.25rem, margin 0
- Links: color #185fa5, no other styling
- **External links only** (Wikipedia, official documentation, external resources)
- **NO internal Canvas cross-references**
- **NO "See also" or "Next page" links**

---
## Step 2 — Sections to REMOVE (v4.0 → v5.0)

These sections must be **completely deleted** from all lecture notes:

- **"Connects to:" / "Leads to:" lines in header** — No document cross-references
- **"Student resource page:" references** — No cross-links to student-facing pages
- **Entire "Looking Ahead" section** — No forward references to other notes
- **"CORE (Must accomplish in 50 min)" subheader** — Merge into Key Teaching Points flat list
- **"DEPTH (If time and energy permit)" subheader** — Integrate substantive content into Key Teaching Points; omit fluff
- **"HOMEWORK / Async" subheader** — Remove entirely; assignments are in Canvas, not here
- **Any cross-document references** (e.g., "See the CPU Architecture lecture")
- **Any "Day 1", "Day 2", etc. time references** — No daily breakdown
- **Time-box language** — "50 min", "if time permits", "before class", "after class"

---
## Step 3 — Inline Styles Only

- All styling via `style=""` attributes
- No `<style>` tags (Canvas strips them)
- No `<script>` tags
- All colors use hex codes from the palette below
- Font families use system sans-serif: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- No em dashes — use space-hyphen-space instead (`-` surrounded by spaces)

---
## Step 4 — Color Palette (CANONICAL)

| Element | Background | Border/Text | Hex Codes |
|---------|-----------|-----------|-----------|
| Header card | Beige | Tan border | `#f1efe8` / `#b4b2a9` |
| Status badge | Pale amber | Amber text | `#faeeda` / `#854f0b` |
| Learning Objectives box | Light purple | Purple border | `#eeedfe` / `#534ab7` |
| LO header bar | Medium purple | — | `#ddd7f5` |
| LO objective cards | White | — | `#ffffff` |
| Key Teaching Points box | Light blue | Blue border | `#E6F1FB` / `#2980b9` |
| KTP header bar | Medium blue | — | `#d6e0f0` |
| Lecture Content box | Light tan | Tan border | `#f5f0e8` / `#d4a76a` |
| Content header bar | Tan | — | `#e5dcc8` |
| Teaching note box | Pale amber | Amber border | `#FAEEDA` / `#854F0B` |
| Discussion/Special box | Dark charcoal | Teal border | `#2c2c2a` / `#5DCAA5` |
| Discussion header bar | Darker charcoal | — | `#1a1a1a` |
| What's Current box | Pale amber | Amber border | `#faeeda` / `#854F0B` |
| Current header bar | Medium amber | — | `#f0d4b8` |
| Reference Links box | Light blue | Blue border | `#e6f0f8` / `#a8c5db` |
| Reference header bar | Medium blue | — | `#d6e0e8` |
| Body text | — | — | `#2c2c2a` (dark gray) |
| Secondary text | — | — | `#5F5E5A` (medium gray) |
| Light text (on dark) | — | — | `#f0ede8` (light gray) |
| Bright text (on dark) | — | — | `#9fe1cb` (light teal) |

---
## Step 5 — Key Principles (v5.0)

1. **Self-contained documents** — Each lecture note is independent. No cross-references to other notes.
2. **No time constraints** — Remove all references to class duration, pacing, or "if time permits". Instructors use notes at their own pace.
3. **Consolidated Key Teaching Points** — Merge old CORE/DEPTH/HOMEWORK into a single flat bullet list. No subsections or headers within the list.
4. **Canvas first** — Notes live in Canvas. Assignments, due dates, and learning pathways are documented in Canvas, not in lecture notes.
5. **Minimal decoration** — Clean, readable format. Content clarity trumps visual polish. No nested divs, no excessive color variation, no busy styling.
6. **Instructor-facing only** — These are reference/prep documents for the instructor. Not student-facing materials. Tone is direct and practical.
7. **No cross-document references** — No "See also", "Next page", "Looking Ahead", or "Connects to" lines. Each note stands alone.
8. **Current market context required** — "What's Current" section grounds the note in reality. Helps instructors answer "Is this still true?" and stay relevant.

---
## Step 6 — Example: PC History (Live v4.0 Canonical Format)

See `Lecture Notes - PC History` in BIT281 Canvas course for the authoritative example of v4.0 format.


---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 5.0 | 2026-08-01 | **Rewritten to match PC History canonical format.** Removed complex nested divs, time boxes (50 min), all cross-document references, "Looking Ahead" sections. Added Key Teaching Points (consolidated from old CORE/DEPTH/HOMEWORK). Added What's Current section (required). Cleaned up colors and simplified styling. Established absolute rule: no "Connects to", no "Student resource page", no time references, no daily breakdown. PC History is live example. |
| 4.0 | 2026-07-27 | **Complete rewrite: Simple, clean format based on PRO221 Week 1.** Removed complex nested divs, grid layouts, checkmarks. Restored left-border header bars, plain bullet lists, generous whitespace. Minimal color palette. Emphasis on content clarity over visual decoration. This is the canonical format going forward. |
| 3.2 | 2026-07-27 | Restructured Steps (moved teaching notes comparison, lab standards, word count to Steps 4-6). |
| 3.1 | 2026-07-27 | Added three new content standards subsections. |
| 3.0 | 2026-07-23 | Merged spec + process into single source of truth. |

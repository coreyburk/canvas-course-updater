---
name: lecture-notes-playbook
description: Use when Corey asks to convert legacy lecture notes into Canvas pages, build new lecture/resource pages for a course, or audit existing Canvas lecture pages against the standard template.
---

# Canvas Lecture Notes Playbook

**Version:** 3.1 
**Last Updated:** 2026-07-27

---

## Overview

This document defines the **standard format** (what pages should look like) and the **process workflow** (how to build/fix them) for all lecture note pages across Canvas courses using the BIT221 visual standard.

**Key principle:** Each lecture note page must be optimized for the actual class session length of that course, not a generic time estimate.

---

## Step 0 — Universal Gotchas

- Resolve the course to its numeric Canvas ID before any API call
- Canvas strips `<style>` tags and raw `<svg>` — all styling inline via `style=` attributes, diagrams as uploaded images referenced via `<img>`
- Pages created unpublished until approved
- **Verify the course's actual class session length** (50 min, 75 min, 2 hours, asynchronous, etc.) before structuring Teaching Agenda sections
- No em dashes (use space-hyphen-space instead)
- Never reconstruct content from memory — pull actual source/verify external facts via WebSearch

---

## Step 1 — Inventory the Source Material

- Where do the notes live and how are they organized (by week/topic/section)?
- Faithful conversion, full modernization, or skeleton-first?
- How are content gaps handled — placeholders, drafted by Claude, or ignored?
- What's the target version/scope?
- **What is the actual class session length for this course?** (Determines Teaching Agenda structure)

---

## Step 2 — Propose Page Structure Before Building

- One page per topic, grouped by week, or grouped by week + theme (usually best — logical progression, but related topics consolidated)
- Get sign-off on scope and session time before creating anything

---

## Step 3 — Per-Page Structure (CANONICAL FORMAT)

Every lecture note page must follow this exact structure in this order:

### 3A. Header Box (Beige) — REQUIRED

**Purpose:** Identifies the course, week, day/session, and brief context.

```html
<div style="background-color: #f1efe8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #b4b2a9;">
  <div style="font-size: 0.8rem; color: #6b6960; margin-bottom: 0.25rem;">Week X - Topic Name | Day Y / Session Name</div>
  <h1 style="margin: 0 0 0.5rem 0; font-size: 1.6rem; color: #2c2c2a;">Page Title</h1>
  <div style="font-size: 0.9rem; color: #5a5955;">Brief context or resource reference (optional)</div>
  <div style="margin-top: 0.75rem; font-size: 0.85rem; color: #854f0b; background-color: #faeeda; display: inline-block; padding: 0.25rem 0.75rem; border-radius: 4px;">Instructor Use Only - Not Published</div>
</div>
```

**Rules:**
- **DO NOT include** "Approx. X hours" or any time estimate in the header
- Include the actual week/day identifier if relevant
- Include publication status indicator if the page is instructor-only
- Keep the h1 title focused on the topic, no "Week X |" prefix (breadcrumb handles that)

---

### 3B. Today's Learning Objectives (Purple Box) — REQUIRED

**Purpose:** Clearly state what students will be able to do by the end of the session.

```html
<div style="background-color: #eeedfe; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #534ab7;">
  <div style="background-color: #ddd7f5; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #534ab7;">Today's Learning Objectives</h2>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
    <div style="background-color: #ffffff; border-radius: 6px; padding: 0.75rem 1rem; display: flex; align-items: flex-start; gap: 0.5rem;">
      <span style="color: #534ab7; flex-shrink: 0;">✓</span>
      <span>Learning objective 1</span>
    </div>
    <div style="background-color: #ffffff; border-radius: 6px; padding: 0.75rem 1rem; display: flex; align-items: flex-start; gap: 0.5rem;">
      <span style="color: #534ab7; flex-shrink: 0;">✓</span>
      <span>Learning objective 2</span>
    </div>
    <!-- More objectives as needed -->
  </div>
</div>
```

**Rules:**
- 2-column grid layout (4-6 objectives total, typical)
- Each objective is a complete action statement (starts with a verb: "Explain...", "Build...", "Compare...")
- Use the checkmark (✓) prefix for visual consistency
- Do NOT include point values
- Header wrapped in darker shade (#ddd7f5) — no left-border bars

---

### 3C. Teaching Agenda (Blue Box) — REQUIRED

**Purpose:** Break down the class session into three clearly scoped sections aligned to the actual session length.

#### Teaching Agenda Container

```html
<div style="background-color: #E6F1FB; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #2980b9;">
  <!-- Teaching Agenda header and CORE/DEPTH/HOMEWORK sections go inside this box -->
</div>
```

#### Teaching Agenda Header

```html
<div style="background-color: #d6e0f0; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
  <h2 style="margin: 0; font-size: 1.05rem; color: #185FA5;">Teaching Agenda</h2>
</div>
```

#### CORE / DEPTH / HOMEWORK Headers (Each inside the blue container)

```html
<div style="background-color: #d6e0f0; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
  <h3 style="margin: 0; font-size: 1.05rem; color: #185FA5;">SECTION TITLE</h3>
</div>
<ul style="margin: 0 0 2rem 0; padding-left: 1.25rem;">
  <li>Bullet point 1</li>
  <li>Bullet point 2</li>
  <li>Bullet point 3 (optional)</li>
</ul>
```

#### Section Definitions

**CORE (Must accomplish in [X minutes/hours])**
- 2–5 bullet points
- The **absolute essentials** that fit in the actual class session length
- Derived from the top 2–5 learning objectives
- Session time examples:
  - BIT281 (50 min): "CORE (Must accomplish in 50 min)"
  - 75-minute course: "CORE (Must accomplish in 75 min)"
  - 2-hour course: "CORE (Must accomplish in 2 hours)"
  - Asynchronous: "CORE (Primary focus)" or similar

**DEPTH (If time and energy permit)**
- 2–5 bullet points
- Extensions, deeper dives, or enrichment topics
- Included when session time allows but not required to complete core learning

**HOMEWORK / Async**
- 2–5 bullet points
- Pre-work, post-session reading, lab prep, or next-session preview
- Guides student independent study and preparation

---

### 3D. Content Sections — REQUIRED

**Purpose:** Deliver the lecture content, organized by topic.

Each major content section is wrapped in a full box. **Alternate colors** to distinguish adjacent sections.

#### Option A (Green)

```html
<div style="background-color: #e1f5ee; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #0F6E56;">
  <div style="background-color: #c8ddd5; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #0f6e56;">Section Title</h2>
  </div>
  <!-- Content goes here (paragraphs, lists, sub-headings, etc.) -->
</div>
```

#### Option B (Warm Tan) — Use alternately

```html
<div style="background-color: #f5f0e8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #d4a76a;">
  <div style="background-color: #e5dcc8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #6b5d4f;">Section Title</h2>
  </div>
  <!-- Content goes here -->
</div>
```

**Rules:**
- Each major content area gets its own full box with a color-matched border
- **Alternate colors between adjacent content sections** (green, then tan, then green, etc.)
- Headers wrapped in darker shade of box background (no left-border bars)
- Typical content sections:
  - A topic-specific deep dive (e.g., "HDD Mechanics: Platters, Heads, Seek Time")
  - A lab walkthrough or procedure guide
  - Visual tables or reference material
  - Discussion questions
- Use the BIT221 visual standard for all inline tables, callouts, and code blocks
- Do NOT nest content sections inside Teaching Agenda sections

---

#### 3D-1. Table Styling (Required for all tables)

**All tables must have solid 1-pixel borders on ALL cells.**

```html
<table style="border-collapse: collapse; width: 100%; border: 1px solid #000000;">
  <thead>
    <tr style="background-color: #444441; color: #ffffff;">
      <th style="padding: 0.75rem 1rem; text-align: left; border: 1px solid #000000;">Header 1</th>
      <th style="padding: 0.75rem 1rem; text-align: left; border: 1px solid #000000;">Header 2</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="padding: 0.75rem 1rem; border: 1px solid #000000;">Cell 1</td>
      <td style="padding: 0.75rem 1rem; border: 1px solid #000000;">Cell 2</td>
    </tr>
    <tr style="background-color: #f1efe8;">
      <td style="padding: 0.75rem 1rem; border: 1px solid #000000;">Cell 3</td>
      <td style="padding: 0.75rem 1rem; border: 1px solid #000000;">Cell 4</td>
    </tr>
  </tbody>
</table>
```

**Table requirements:**
- Border style: `solid 1px #000000` (black) on **all cells** (`<th>` and `<td>`)
- Use `border-collapse: collapse` on the `<table>` element
- Alternate row backgrounds: `#ffffff` (white) and `#f1efe8` (beige) in tbody
- Header row background: `#444441` (dark gray) with `color: #ffffff` (white text)
- Header border: `1px solid #000000` (same as body cells)

---

### 3E. Discussion Guide (Dark) — OPTIONAL but Recommended

**Purpose:** Provide instructor-facing questions for in-class discussion.

```html
<div style="background-color: #2c2c2a; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; margin-top: 2.5rem; color: #f0ede8; border: 1px solid #5DCAA5;">
  <div style="background-color: #1a1a1a; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <h2 style="margin: 0; font-size: 1.05rem; color: #9fe1cb;">Discussion Guide</h2>
  </div>
  <!-- Q&A pairs -->
</div>
```

**Structure:**
- A dark background box with teal accent (matching the "Applied" section style from BIT221)
- 2–4 discussion questions with sample answers
- Labeled clearly as "Discussion Guide"

---

### 3F. What's Current (Amber) — OPTIONAL

**Purpose:** Flag version-specific or standards-specific information relevant to the current course or term.

```html
<div style="background-color: #faeeda; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #854F0B;">
  <div style="background-color: #f0d4b8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <p style="margin: 0; font-size: 0.8rem; color: #854f0b;"><strong>What's Current</strong></p>
  </div>
  <p style="margin: 0 0 0.75rem 0;">Description of current technology/standards/versions relevant to the topic.</p>
  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">
    <li><strong>Item 1:</strong> Description and date/version context</li>
    <li><strong>Item 2:</strong> Description and date/version context</li>
  </ul>
</div>
```

---

### 3G. Looking Ahead (Beige) — OPTIONAL

**Purpose:** Preview the next session and maintain narrative continuity.

```html
<div style="background-color: #f1efe8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #b4b2a9;">
  <div style="background-color: #e5dcc8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <p style="margin: 0; font-size: 0.8rem; color: #6b6960;"><strong>Looking Ahead</strong></p>
  </div>
  <p style="margin: 0 0 0.5rem 0;"><strong>Day X</strong> - Description of next day's topic and how it connects.</p>
  <p style="margin: 0;"><strong>Week X</strong> - How this week's concepts feed into the next week.</p>
</div>
```

---

### 3H. Reference Links (Slate Blue) — OPTIONAL

**Purpose:** Provide curated external resources for deeper study.

```html
<div style="background-color: #e6f0f8; border-radius: 8px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #a8c5db;">
  <div style="background-color: #d6e0e8; padding: 0.75rem 1rem; margin-bottom: 1rem; border-radius: 4px;">
    <p style="margin: 0; font-size: 0.8rem; color: #5a6f7f;"><strong>Reference Links</strong></p>
  </div>
  <ul style="margin: 0; padding-left: 1.25rem; font-size: 0.9rem;">
    <li><a style="color: #185fa5;" href="https://example.com">Link title</a> - Brief description of what the resource covers</li>
    <li><a style="color: #185fa5;" href="https://example.com">Another link</a> - How it supports the day's learning</li>
  </ul>
</div>
```

**Note:** Reference Links uses **distinct light slate blue** (not beige like Looking Ahead) to avoid visual confusion.

---

### 3I. Teaching Notes vs. Student Pages — CRITICAL DISTINCTION

**Teaching Notes** are instructor-facing, unpublished pages grounding classroom prep, troubleshooting, and curriculum coherence.

**Student Pages** are published, student-facing resources for reference and self-study.

| Attribute | Teaching Notes | Student Pages |
|-----------|---|---|
| **Naming** | `Teaching Notes - Week [N] - [Topic]` | `Week [N] \| Page [#] - [Topic]` |
| **Publication** | Unpublished | Published |
| **Module** | Instructor-only module (position 1) | Course module by week (positions 2+) |
| **Audience** | Instructors only | Students + instructors |
| **Scope** | 2500+ words; deep, comprehensive | 1500-2000 words; focused on learning objectives |
| **Content** | Expected outputs, common errors, security implications, troubleshooting | Core concepts, procedures, examples, references |
| **Header Status** | Include "Instructor Use Only - Not Published" indicator | No publication status needed |

**When to create Teaching Notes:**
- Lab-heavy assignments with 4+ scenarios (document expected output per scenario)
- Topics with common misconceptions or failure modes (common student errors section)
- Content with security or operational risk implications (weave security context throughout)
- Synthesis or foundational weeks (teaching notes tie concepts together across multiple student pages)

**Module placement rule:**
- Create a dedicated unpublished instructor module at position 1: "Course Outline and Lecture Notes (Not Published - Instructor Use Only)"
- Place all teaching notes AND course outline in this module
- Keep student modules separate (position 2 onward)

---

### 3J. Lab Walkthrough Standards — REQUIRED for Assignment-Heavy Topics

**Purpose:** Prepare instructors to grade, troubleshoot, and guide student submissions with concrete expectations.

**Must include:**

1. **Assignment summary** (what students will submit)
   - Example: "A DCS export (CSV) showing at least 5-10 minutes of idle server performance data"

2. **Expected output values** (real data, not fabricated)
   - Source: Run the assignment yourself or document observed results from past student submissions
   - Example: "Idle Windows Server 2025 baseline: CPU 5-15%, RAM 5-7 GB, Disk Queue 0-1"
   - **CRITICAL:** Never invent values from general knowledge

3. **Success criteria** (clear pass/fail indicators)
   - Example: "DCS runs without errors, captures expected duration, shows idle-state values in CSV"

4. **Common student errors** (2-4 typical mistakes with fixes)
   - Format: **"Error: [What student does wrong]"** → **"Cause: [Why]"** → **"Fix: [Solution]"**
   - Example: **"DCS won't start - Access Denied"** → **Cause: DCS requires admin rights** → **Fix: Run Performance Monitor as administrator**

5. **Security/operational implications** (where applicable)
   - Connect assignment output to real-world anomaly detection
   - Example: "Cryptomining malware shows up as sustained CPU above baseline; a file server baseline of 10% that suddenly runs at 50% 24/7 is a red flag"

6. **In-class demo walkthrough** (optional but recommended)
   - Step-by-step of how you'd demonstrate the assignment in real-time
   - Example: "Open both Task Manager and Resource Monitor side-by-side during Prime95"

---

### 3K. Content Depth & Word Count Guidelines

**Teaching Notes Pages:** 2500–3500 words per page (comprehensive, instructor-focused)

**Breakdown by section:**
- **Learning Objectives:** 100–150 words (2–6 objectives, 1-2 sentences each)
- **Fundamentals & Conceptual Architecture:** 600–900 words (3–5 key concepts with context and "why it matters")
- **Technical Procedures & Configuration:** 800–1200 words (3–6 procedures with step-by-step clarity, real command/UI paths, not generic)
- **Lab Walkthrough & Troubleshooting:** 700–1000 words (all 4+ scenarios covered with expected outputs, common errors, decision trees)
- **Optional sections** (Discussion Guide, What's Current, Looking Ahead, Reference Links): 200–400 words combined

**Why this depth:**
- Instructors need enough detail to teach confidently, troubleshoot student submissions, and answer "why this matters" without leaving the page
- 2500+ words ensures content is grounded in specifics, not generic bullet points
- Student-facing pages stay tighter (1500–2000) to avoid cognitive overload; teaching notes provide the "teacher's expanded version"

**Content standards:**
- Every concept grounded in a concrete example or real-world scenario
- All command-line examples use actual paths and syntax (not `<placeholder>`)
- All expected outputs from actual lab runs (never fabricated)
- All procedures tested or verified from source (never reconstructed from memory)
- All tables have real data (not example placeholders)
- All security or version-specific notes dated or version-stamped

---

## Step 4 — Color Reference (CRITICAL)

| Element | Border | Background | Header BG | Text |
|---------|--------|------------|-----------|------|
| Header Box | `#b4b2a9` | `#f1efe8` | — | `#2c2c2a` |
| Learning Objectives | `#534ab7` | `#eeedfe` | `#ddd7f5` | `#534ab7` |
| **Teaching Agenda** | **`#2980b9`** | **`#E6F1FB`** | **`#d6e0f0`** | **`#185FA5`** |
| Content (Green) | `#0F6E56` | `#e1f5ee` | `#c8ddd5` | `#0f6e56` |
| Content (Tan) | `#d4a76a` | `#f5f0e8` | `#e5dcc8` | `#6b5d4f` |
| Discussion Guide | `#5DCAA5` | `#2c2c2a` | `#1a1a1a` | `#9fe1cb` |
| What's Current | `#854F0B` | `#faeeda` | `#f0d4b8` | `#854f0b` |
| Looking Ahead | `#b4b2a9` | `#f1efe8` | `#e5dcc8` | `#6b6960` |
| Reference Links | `#a8c5db` | `#e6f0f8` | `#d6e0e8` | `#5a6f7f` |

**Header styling:** All section headers wrapped in darker background shades (no left-border bars).

---

## Step 5 — Authoring Standards

- No em dashes — use space-hyphen-space
- No point values in Criteria boxes
- No `<style>` tags — all styling inline via `style=` attributes
- Never fabricate content — pull actual source and verify external facts via WebSearch
- Diagrams as images, never inline SVG
- Show 1-2 example pages and get sign-off before batching

---

## Step 6 — IDEMPOTENT Transformation Process

**CRITICAL: This process is IDEMPOTENT. Running it multiple times on the same page produces the IDENTICAL canonical result. Use this for all pages regardless of their current state.**

### 6A. Extract Components (Parse current format, ignore styling)

1. **Fetch** page from Canvas via `get_page_content`
2. **Parse and extract** from the existing HTML (regardless of current format/styling):
   - **Header:** Week, Day, Title, Context
   - **Learning Objectives:** Extract all objective texts
   - **Teaching Agenda:** Extract all CORE bullets, DEPTH bullets, HOMEWORK bullets
   - **Content sections:** Identify all section headers and content
   - **All tables:** Extract table data (headers and rows)
   - **Optional sections:** Discussion Guide, Looking Ahead, What's Current, Reference Links

### 6B. Reconstruct Page with CANONICAL Formatting

3. **Rebuild ENTIRE page** to the canonical format defined in Step 3:
   - **Header box:** Exact beige HTML, no time estimates
   - **Learning Objectives:** Exact purple 2-column grid HTML with checkmarks, header in darker background
   - **Teaching Agenda:** Full blue box with Teaching Agenda header and CORE/DEPTH/HOMEWORK subsections, all headers in darker background
   - **Content sections:** Alternating green/tan with darker header backgrounds (no left-border bars)
   - **All tables:** Reconstructed with `border-collapse: collapse; border: 1px solid #000000` on EVERY cell
   - **Optional sections:** Exact HTML per Step 3, with darker header backgrounds

### 6C. Apply ALL Styling Rules

4. **Verify all styling applied:**
   - No em dashes (space-hyphen-space only)
   - No "Approx. X hours" in header
   - Session time in CORE matches actual course length
   - All tables have solid 1px black borders on all cells
   - Alternating table row backgrounds: #ffffff and #f1efe8
   - Headers wrapped in darker backgrounds (no left-border bars)
   - Alternating content section colors (green, tan, green, tan, etc.)

### 6D. Update and Verify

5. **Update** page via `edit_page_content` with fully reconstructed HTML
6. **Verify** result matches spec exactly (all sections, colors, table borders, spacing)
7. **Report:** Transformation complete, all sections canonical, no manual fixes needed

---

## Critical Rules (DO NOT VIOLATE)

### Must Have
- ✓ Header box (week/day, title, publication status)
- ✓ Learning Objectives (purple box with darker header background)
- ✓ Teaching Agenda header (blue, must be present, darker header background)
- ✓ CORE section (blue, darker header background)
- ✓ DEPTH section (blue, darker header background)
- ✓ HOMEWORK section (blue, darker header background)
- ✓ All section headers wrapped in darker background shades

### Must NOT Do
- ✗ Include time estimates in page header
- ✗ Use green colors for Teaching Agenda sections (must be blue)
- ✗ Remove or rename Teaching Agenda header
- ✗ Invent new section names (only CORE, DEPTH, HOMEWORK)
- ✗ Change content section headers from assigned colors (green/tan alternate)
- ✗ Use left-border bars on section headers (headers wrapped in darker background instead)
- ✗ Use same color for adjacent content sections (must alternate green/tan)
- ✗ Use `<style>` tags (inline only)
- ✗ Include em dashes or smart quotes
- ✗ Use beige for Reference Links (must be light slate blue #e6f0f8)

### Flexible Elements
- Number of bullet points per section (2–5, depending on session length)
- Presence of Discussion Guide, Looking Ahead, What's Current, Reference Links (optional)
- Content section organization (varies by course/topic)
- Session time language (e.g., "50 min" vs. "75 min" vs. "2 hours" vs. "primary focus")

---

## Examples

### Example: 50-Minute Course (BIT281)

```
CORE (Must accomplish in 50 min)
- Understand concept A (15 min)
- Practice concept B (20 min)
- Apply to real-world example (15 min)

DEPTH (If time and energy permit)
- Explore extension concept C
- Discuss advanced application scenario
- Connect to Week N preview

HOMEWORK / Async
- Read chapter X
- Watch video Y
- Prepare Day N+1 lab
```

### Example: 75-Minute Course

```
CORE (Must accomplish in 75 min)
- Deep introduction to topic (25 min)
- Guided hands-on practice (30 min)
- Synthesis and wrap-up (20 min)

DEPTH (If time and energy permit)
- Advanced case study
- Peer discussion activity
- Connection to adjacent topic

HOMEWORK / Async
- Reflect on in-class activity
- Research extension topic
- Pre-read next session
```

### Example: Asynchronous/Self-Paced Course

```
CORE (Primary focus)
- Learning objective 1
- Learning objective 2
- Learning objective 3

DEPTH (For deeper understanding)
- Extension topic A
- Extension topic B

HOMEWORK / Async
- Suggested reading
- Optional challenge problem
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 3.1 | 2026-07-27 | Added three new content standards subsections: Teaching Notes vs. Student Pages (naming, placement, scope); Lab Walkthrough Standards (expected outputs, common errors, security implications); Content Depth & Word Count (2500+ words for teaching notes, breakdown by section) |
| 3.0 | 2026-07-23 | **MERGED spec + process into single source of truth** — eliminated duplication; comprehensive format definitions + workflow in one skill document |
| 1.3 | 2026-07-23 | Refined header styling: removed left-border bars; headers wrapped in darker background shades for visual hierarchy; alternating content colors (green + warm tan) to distinguish adjacent sections; Reference Links now distinct light slate blue |
| 1.2 | 2026-07-23 | Added full-box styling to ALL sections for visual consistency |
| 1.1 | 2026-07-23 | Added table styling requirement: solid 1px black borders on all cells; defined idempotent transformation process |
| 1.0 | 2026-07-23 | Initial specification; established Teaching Agenda blue headers, content headers green |

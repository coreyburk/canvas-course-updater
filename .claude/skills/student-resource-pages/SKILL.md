---
name: student-resource-pages
description: Use when building or updating Canvas student resource pages (student-facing lecture, reference, or concept documentation in weekly course modules). Distinct from instructor lecture notes and lab notes.
---

# Canvas Student Resource Pages Playbook

**Version:** 2.0  
**Last Updated:** 2026-11-11  
**Canonical Examples:**
- **Format 1 (BIT221 Standard):** `Week 1 | Student Page 1 - Log File Fundamentals` (BIT320) / `Week 2 | Page 1 - Active Directory Domain Structure` (BIT221)
- **Format 2 (Modern Minimal):** `Week 6 | Page 1 - IP Routing Fundamentals and Static Routing` (ITH216) / `Week 1.1: InfoSec Fundamentals & Risk Assessment` (BIT360)

---

## Overview

Student resource pages are **student-facing** pages placed in weekly course modules that enable independent learning and support weekly assignments. They answer **"Why does this matter?"** and **"How do I do this?"** rather than "Here's what the instructor will teach."

---

## Step 0 - Universal Gotchas & Low-Context Workflow

- **Keep new pages UNPUBLISHED until reviewed by Corey** (`CLAUDE.md` standing rule). Once approved, publish and verify module placement.
- **Never generate or pass 30 KB of raw inline HTML through MCP tool calls (`create_page` / `edit_page_content`).** Doing so puts 3-4 copies of the HTML into conversation history (~100k tokens per page).
- **Use the low-context build + sync pipeline:**
  1. Author the page in structured Markdown (`scratchpad/weekN_pageM.md`) with frontmatter `template: page-f1` (BIT221 style) or `template: page-f2` (Modern Minimal style).
  2. Compile to inline-styled HTML and run automatic lint checks:
     ```bash
     python tools/canvas_build.py scratchpad/weekN_pageM.md -o scratchpad/weekN_pageM.html
     ```
  3. Push to Canvas (runs `canvas_lint` automatically before writing and prints a 3-line summary):
     ```bash
     python tools/canvas_sync.py create-page --course <CODE> --title "Week N | Page M - Topic" -i scratchpad/weekN_pageM.html --unpublish
     # Or to update an existing page:
     python tools/canvas_sync.py push-page --course <CODE> --page <slug> -i scratchpad/weekN_pageM.html
     ```
- **When building multiple pages in one week, delegate each page to a separate subagent** (or split sessions between pages) so raw page drafts never accumulate in a single conversation context.
- **No em dashes** (space-hyphen-space ` - ` only), no `<style>` tags, no inline `<svg>`, no grading rubrics or point values.

---

## Step 1 - Scope & Granularity

- **Organize by topic granularity, not calendar week alone.** A single week typically warrants **2–4 resource pages** depending on assignment scope and technical depth.
- **Word count scales with topic complexity:**
  - Focused single-tool or single-concept pages (e.g., BIT320): **2,000–3,000 words**
  - Multi-step architecture, protocol, or lab-foundation pages (e.g., ITH216, BIT360): **2,800–4,500 words**
- **Must include:**
  - Learning Objectives (4–6 action-oriented student objectives)
  - "Why This Matters" motivation section tied to real-world operations and the week's assignment
  - Core concepts with worked examples, real command syntax, and realistic outputs
  - Step-by-step procedural tables and comparison tables (trade-offs between options)
  - Common Mistakes / Pitfalls (3–5+ specific mistakes with **"Why It's Wrong"** and **"How to Fix"**)
  - Troubleshooting table (`Problem | Cause | Solution`) where applicable
  - Curated external Reference Links / Resources (3–5 authoritative links)
- **Must NOT include:**
  - `"Instructor Use Only"` badges, Teaching Agendas, facilitation guides, or why-students-struggle notes
  - Direct copy-paste solutions or actual answers to graded assignment questions (teach the pattern/technique on different or generalized data, never spoil the lab answer)
  - Grading rubrics or point values

---

## Step 2 - Choosing Format 1 vs. Format 2

Check `courses/{CODE}.md` or inspect an existing page in the course before authoring:

| Aspect | Format 1 (`--template page-f1`) | Format 2 (`--template page-f2`) |
|---|---|---|
| **Courses using it** | BIT221, BIT281, BIT320, BIT351, PRO221, PRO352 | ITH216, BIT360 |
| **Wrapper** | `max-width: 860px`, `color: #2C2C2A` | `max-width: 900px`, `color: #1a1a1a` |
| **Header** | Beige card (`#f1efe8`, border `#b4b2a9`) | Minimal bottom border (`#e5e7eb`), blue week label (`#2563eb`) |
| **Learning Objectives** | Purple box (`#eeedfe` / `#534ab7`), 2-col grid of white checkmark cards | Light gray box (`#f9f9f9`), `4px solid #2563eb` left border, checkmark list |
| **Why This Matters** | Green box (`#e1f5ee` / `#0F6E56`, header `#c8ddd5`) | Clean H2 section |
| **Content Sections** | Tan boxes (`#f5f0e8` / `#d4a76a`, header `#e5dcc8`) | Clean H2 (`1.5rem`, `#1a1a1a`) with open whitespace |
| **Applied / Mistakes** | Dark charcoal box (`#2c2c2a`, border `#5DCAA5`, header `#1a1a1a`) | Clean H2 + dark code blocks (`#1e293b`) / tables |
| **Callouts** | Amber (`#FAEEDA` / `#854F0B`) or Blue (`#E6F1FB` / `#185FA5`) | Left-border Amber (`#fef3c7` / `#d97706`) or Blue (`#eff6ff` / `#2563eb`) |
| **Tables** | Dark header `#444441`, zebra rows `#ffffff` / `#F1EFE8` | Light gray header `#f3f4f6`, zebra rows `#ffffff` / `#f9f9f9` |

Never mix Format 1 and Format 2 within the same week.

---

## Step 3 - Markdown Authoring Template (`tools/canvas_build.py`)

Write the page in Markdown using this structure and compile with `python tools/canvas_build.py`:

```markdown
---
template: page-f1
title: Topic Title Without Week Prefix
week: Week N - Topic Area
---

## Learning Objectives
- Configure and verify ...
- Analyze and troubleshoot ...
- Compare trade-offs between ...
- Apply ...

## Why This Matters
1-2 paragraphs explaining why this skill matters in production and how it connects to this week's lab work.

## Core Concept Section 1
### Subsection Heading
Explanation grounded in concrete commands and real-world parameters.

| Option | Mechanism | When to Use |
|---|---|---|
| Option A | Description | Best for X |
| Option B | Description | Best for Y |

> **Pro tip:** Practical advice for students working through this concept.

```bash
# Multi-line commands automatically get <pre style="... white-space: pre-wrap;">
command --flag value
```

## Applied: Hands-On Walkthrough
Step-by-step worked example using non-graded sample data.

## Common Mistakes to Avoid
| Mistake | Why It's Wrong | How to Fix |
|---|---|---|
| Mistake 1 | Consequence | Specific corrective action |
| Mistake 2 | Consequence | Specific corrective action |
| Mistake 3 | Consequence | Specific corrective action |

## Resources
- [Official Documentation Title](https://example.com) - Brief description of what students will find here
```

---

## Step 4 - Module Wiring & Verification

1. Wire the created page into the weekly module under the `Resources` subheader (use the tail-rebuild technique documented in `CLAUDE.md` if reordering module items).
2. Keep the page **unpublished** until Corey reviews and approves it.
3. Update `courses/{CODE}.md` with the page ID, slug, and status.

---

## Changelog

| Version | Date | Changes |
|---|---|---|
| 2.0 | 2026-11-11 | Consolidated `SKILL.md` and `playbook.md` into a single source of truth. Fixed publishing contradiction (new pages stay **unpublished** until reviewed per `CLAUDE.md`). Unified word-count guidance (2,000–4,500 words scaled by complexity) and Format 1 vs. Format 2 specs. Integrated low-context Markdown compilation (`tools/canvas_build.py`) and REST sync (`tools/canvas_sync.py`). |
| 1.1 | 2026-09-17 | Updated word count and required sections (Why This Matters, step-by-step tables, Common Mistakes, Troubleshooting) based on BIT360 Week 1. |
| 1.0 | 2026-07-27 | Initial specification distinguishing student resource pages from instructor lecture notes. |

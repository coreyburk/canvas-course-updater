# Student Resource Page Style Formats

## Overview
Two distinct style formats for Canvas course resource pages. Each provides a complete visual system for consistency across pages.

---

## Format 1: BIT221 Template (Original)

**Status:** Reference standard for existing courses (BIT221, BIT281, BIT320, BIT351, PRO221, PRO352)  
**Use Case:** Established courses requiring visual continuity with existing materials

### Visual Characteristics
- **Primary approach:** Bordered boxes with full-color backgrounds
- **Layout style:** Structured, formal, componentized
- **Visual density:** Higher (more decorative elements)
- **Tone:** Academic, institutional

### Color Palette
| Element | Background | Border/Text | Hex Codes |
|---------|-----------|-----------|-----------|
| Header card | Beige | Tan border | `#F1EFE8` / `#B4B2A9` |
| Learning Objectives | Light purple | Purple border | `#EEEDFE` / `#534AB7` |
| Key Teaching Points | Light blue | Blue border | `#E6F1FB` / `#2980b9` |
| Lecture Content | Light tan | Tan border | `#f5f0e8` / `#d4a76a` |
| Teaching notes | Pale amber | Amber border | `#FAEEDA` / `#854F0B` |
| Info callout | Light blue | Blue border | `#e6f0f8` / `#a8c5db` |
| Discussion/Special | Dark charcoal | Teal border | `#2c2c2a` / `#5DCAA5` |
| What's Current | Pale amber | Amber border | `#faeeda` / `#854F0B` |
| Reference Links | Light blue | Blue border | `#e6f0f8` / `#a8c5db` |

### Key Components

**Header Card:**
```
background: #F1EFE8, border: 1px solid #B4B2A9
padding: 20px, border-radius: 8px
margin-bottom: 30px
```

**Learning Objectives Grid:**
```
background: #EEEDFE, border: 1px solid #534AB7
display: grid, grid-template-columns: 1fr 1fr, gap: 0.75rem
Purple header bar #ddd7f5 with h2 #534AB7
White grid item cards with ✓ checkmarks
```

**Section Headers with Left Border:**
```
Green left-border bars (#0F6E56) for main sections
Light tan/amber (#f5f0e8) for content sections
Dark charcoal (#2c2c2a) for special/discussion sections
```

**Callout Boxes:**
```
Full-color background with 1px border
Examples: #FAEEDA (amber), #E6F1FB (blue), #eafaf1 (green)
Left-border accent color matching theme
Padding: 15-20px, border-radius: 4-8px
```

### Typography
- **Font stack:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- **Body color:** `#2C2C2A` (dark gray)
- **Secondary text:** `#555` or `#6B6960`
- **Heading color:** `#2C2C2A`

### Layout
- **Max-width:** 860px
- **Margins:** Generous (2-2.5rem between sections)
- **Padding:** 20px standard, 30px on cards
- **Line-height:** 1.5-1.6

---

## Format 2: Modern Minimal (New)

**Status:** New contemporary standard  
**Use Case:** New courses, updated materials, emphasis on clean aesthetics

### Visual Characteristics
- **Primary approach:** Subtle borders with minimal backgrounds
- **Layout style:** Open, spacious, minimal decoration
- **Visual density:** Lower (focus on content)
- **Tone:** Contemporary, professional, SaaS-like

### Color Palette
| Element | Background | Border/Text | Hex Codes |
|---------|-----------|-----------|-----------|
| Primary accent | None | Blue text/border | `#2563eb` |
| Page background | White/off-white | Gray border | `#ffffff` / `#e5e7eb` |
| Light section bg | Minimal | Gray text | `#f9f9f9` / `#6b6b6b` |
| Objective list | Light gray bg | Blue accent | `#f9f9f9` / `#2563eb` |
| Info callout | Light blue | Blue left-border | `#eff6ff` / `#2563eb` |
| Warning callout | Light amber | Amber left-border | `#fef3c7` / `#d97706` |
| Code block | Dark charcoal | Light text | `#1e293b` / `#e2e8f0` |
| Body text | Default | Dark gray | `#1a1a1a` / `#6b6b6b` |
| Secondary text | Default | Medium gray | `#6b6b6b` |

### Key Components

**Header Section:**
```
padding: 40px 0, border-bottom: 1px solid #e5e5e5
h1: 2.2rem, font-weight: 700, color: #1a1a1a
p: 1.05rem, color: #6b6b6b
No background, minimal styling
```

**Objective List:**
```
padding: 32px, background: #f9f9f9
border-radius: 8px, border-left: 4px solid #2563eb
List items with ✓ checkmarks, padding-left: 24px
Subtle visual separation, no grid needed
```

**Section Headers:**
```
font-size: 1.5rem, font-weight: 700, color: #1a1a1a
margin: 48px 0 24px 0
No background color, simple typography hierarchy
```

**Subsection/Card Grid:**
```
display: grid, grid-template-columns: 1fr 1fr, gap: 20px
padding: 24px, background: #fafafa, border-radius: 6px
border-top: 3px solid #2563eb (colored accent only)
Simple, clean appearance
```

**Callout Boxes:**
```
Blue info: background #eff6ff, border-left: 4px solid #2563eb
Amber warning: background #fef3c7, border-left: 4px solid #d97706
Padding: 20px, border-radius: 4px
Left-border only, no full background decoration
```

**Code Blocks:**
```
background: #1e293b, color: #e2e8f0
padding: 16-20px, border-radius: 6px
font-family: 'Courier New', monospace, font-size: 0.85-0.9rem
line-height: 1.4-1.6, overflow-x: auto
Command prompts in #94a3b8 (muted color)
```

**Tables:**
```
border-collapse: collapse, background: white
thead: background #f3f4f6, border-bottom: 2px solid #e5e7eb
tbody rows: alternating white / #f9f9f9
padding: 14px 16px, color: #1a1a1a / #6b6b6b
Simple, clean separator lines
```

### Typography
- **Font stack:** `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif`
- **Body text:** `#1a1a1a` (dark)
- **Secondary text:** `#6b6b6b` (medium gray)
- **Accent color:** `#2563eb` (modern blue)
- **Heading color:** `#1a1a1a`

### Layout
- **Max-width:** 900px (slightly wider than Format 1)
- **Margins:** Very generous (48px between sections)
- **Padding:** 24px standard, 40px on headers
- **Line-height:** 1.65 (more spacious)
- **Whitespace:** Emphasis on breathing room

### Spacing System
- **Section top margin:** 48px
- **Card padding:** 24px
- **Header padding:** 40px
- **List item gap:** 12px
- **Grid gap:** 20px
- **Code block padding:** 16-20px

---

## Comparison

| Aspect | Format 1 (BIT221) | Format 2 (Modern) |
|--------|---------|---------|
| **Visual Style** | Bordered boxes, colorful | Minimal, subtle accents |
| **Color approach** | Full backgrounds | Selective, left-borders only |
| **Max-width** | 860px | 900px |
| **Section margins** | 30px | 48px |
| **Code blocks** | Dark with syntax | Dark #1e293b, simple |
| **Callouts** | Full-color backgrounds | Left-border + light fill |
| **Overall tone** | Formal, institutional | Contemporary, professional |
| **Learning objective style** | 2-col grid with cards | Flat list with checkmarks |
| **Typography weight** | Standard | Slightly bolder headings |

---

## Usage Guidelines

### Choose Format 1 (BIT221) if:
- Course is part of an established program with existing visual standards
- Continuity with existing materials is important
- Institutional/formal tone is desired
- Course already uses BIT221 template

### Choose Format 2 (Modern) if:
- Course is new or being completely redesigned
- Contemporary aesthetic is desired
- Less visual decoration is preferred
- Focus on readability and minimal design is valued

### Switching Formats
Both formats can coexist in the same course. New pages can use Format 2 while legacy pages maintain Format 1. Consider:
- Consistency within a course (all pages same format)
- Student experience (don't mix styles within Week)
- Update strategy (gradual migration vs. all-at-once)

---

## Implementation Notes

### Canvas Constraints (Both Formats)
- No `<style>` tags (Canvas strips them)
- All styling must be inline
- No SVG (Canvas strips it silently)
- `<strong>` tags for bold, not `font-weight` style
- Space-hyphen-space for dashes (no em dashes)
- Max-width wrapping div for all page content

### Code Block HTML Template (Format 2)
```html
<div style="background: #1e293b; color: #e2e8f0; padding: 20px; border-radius: 6px; 
            font-family: 'Courier New', monospace; font-size: 0.85rem; 
            line-height: 1.4; margin-bottom: 24px; overflow-x: auto;">
  <!-- code here, use <span style="color: #94a3b8;"> for prompts -->
</div>
```

### Callout Box Template (Format 2 - Blue)
```html
<div style="padding: 20px; background: #eff6ff; border-left: 4px solid #2563eb; 
            border-radius: 4px;">
  <p style="margin: 0; font-size: 0.95rem; color: #1e40af;">
    <strong>Label:</strong> Content here
  </p>
</div>
```

---

## References

**Format 1 Canonical Source:**
- BIT221 Course (Canvas ID: 3631198)
- Lecture Notes - PC History (authoritative example)
- lecture-notes-playbook SKILL (v4.0)

**Format 2 Canonical Source:**
- ITH216 Week 1 Pages (created 2026-09-15)
- Page 1: Network Cabling and Physical Connectivity
- Page 2: Cisco CLI Modes and Console Access

---

*Last updated: 2026-09-15*  
*Maintained by: Claude Code*

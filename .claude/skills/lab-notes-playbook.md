# Canvas Lab Notes Playbook

**Version:** 1.0  
**Last Updated:** 2026-09-11  
**Applies to:** BIT320 and other technical lab courses  
**Reference Example:** Lab 5.1 Notes - Windows Event Log Analysis (BIT320)

---

## Overview

Lab Notes are **published, student-facing** pages that scaffold learning for hands-on lab assignments without spoiling the answers. They bridge the gap between what students learned in training/lectures and what they need to accomplish in the lab.

**Key principle:** Teach the HOW-TO (techniques, syntax, patterns, algorithms) without teaching the ANSWER (specific results, exact output, interpretations of their data).

---

## Step 0 — Gotchas

- Lab Notes are **published and student-facing** (unlike instructor lecture notes)
- Place in the course module at the appropriate week, **not in instructor-only module**
- No em dashes — use space-hyphen-space instead
- Use left-border boxes (BIT281 style), not full-border boxes
- Code examples must be **generalizable** (show the pattern, not the answer)
- Never show expected output from actual student data
- Canvas strips `<style>` tags and inline SVG — all styling via `style=""` attributes

---

## Step 1 — Scope: Guidance, Not Answers

Lab Notes answer: **"How do I do this?"** not **"What's the answer?"**

### ✅ What to Include
- **Techniques and syntax:** Show code patterns students can adapt
- **Step-by-step HOW-TO:** "Extract column 2 using cut -d',' -f2"
- **Language-specific approaches:** Bash vs. PowerShell vs. Python patterns
- **Challenge areas:** Identify the hardest part and give scaffolding
- **Workflow:** Suggest sequence (start simple, add complexity)
- **Verification strategies:** How to manually check your work

### ❌ What NOT to Include
- Actual expected output from their lab data
- Answers to the lab questions
- Interpretation of what their results mean
- Complete, working solutions they can copy-paste
- Their actual numbers/counts/percentages
- Assumptions about what they'll find

---

## Step 2 — Structure: BIT281 Lab Notes Format

All Lab Notes follow this exact structure with left-border boxes:

```
1. "Why This Matters" (Blue border, #2980b9)
   └─ Real-world context and relevance

2. Core Concept/Questions (Purple border, #534AB7)
   └─ What they're learning, displayed in grid cards

3. Language-Specific HOW-TO (Light blue border, #185FA5)
   └─ Code patterns for each language with explanations

4. Key Challenge/Deep Dive (Amber border, #854F0B)
   └─ The hardest part of the lab with scaffolding

5. Workflow/Next Steps (Green border, #27ae60)
   └─ Suggested sequence to follow
```

---

## Step 3 — Visual Template (Left-Border Boxes)

All sections use left-border (not full border) styling:

```html
<div style="background-color: #eaf4fb; border-left: 4px solid #2980b9; padding: 1.5rem; margin-bottom: 2.5rem;">
    <h2 style="color: #1a5276; margin-top: 0;">Section Title</h2>
    <p style="margin: 0;">Content here...</p>
</div>
```

### Color Palette (Left-Border Only)

| Section | Background | Border | Border Color |
|---------|-----------|--------|--------------|
| Why This Matters | #eaf4fb | left 4px | #2980b9 (blue) |
| Core Concept | #eeedfe | left 4px | #534AB7 (purple) |
| HOW-TO Guidance | #e6f1fb | left 4px | #185FA5 (light blue) |
| Key Challenge | #fef9e7 | left 4px | #854F0B (amber) |
| Workflow/Next | #eafaf1 | left 4px | #27ae60 (green) |

### Nested Cards (for grid layouts)

```html
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
    <div style="background-color: #f8f6fe; border-radius: 6px; padding: 1rem; border-left: 3px solid #534AB7;">
        <h3 style="color: #534ab7; margin-top: 0; font-size: 1rem;">Card Title</h3>
        <p style="margin: 0; font-size: 0.95rem;">Card content</p>
    </div>
    <!-- Repeat for each card -->
</div>
```

### Code Blocks

```html
<pre style="background-color: #2c2c2a; color: #e8e8e8; padding: 0.75rem; border-radius: 3px; font-size: 0.9rem; margin: 0 0 0.75rem 0; overflow-x: auto; white-space: pre-wrap;">
# Your code here
cut -d',' -f2 system.csv | sort | uniq -c
</pre>
```

---

## Step 4 — Content Structure by Section

### Section 1: Why This Matters (Blue Border)

**Purpose:** Ground the lab in real-world context.

**Content:** 1-2 sentences explaining why this skill matters to professionals in this field.

**Example:** "System administrators live and die by logs. When something goes wrong, logs tell you what happened, when it happened, and which component caused it. In this capstone, you'll become fluent in reading and analyzing the story your system has been quietly telling all week."

**Length:** 50-100 words

---

### Section 2: Core Concept / What You're Investigating (Purple Border)

**Purpose:** Explain what the lab is asking students to do.

**Content:** Use grid cards (2-column layout) to break down each lab goal/question. Show what each one asks, but NOT the answer.

**Example:** 
- "Question 1: Event Type Distribution — How many errors, warnings, and information events occurred? This shows whether errors dominate your log."
- "Question 2: Percentage Breakdown — What percentage of events are errors vs. warnings? Percentages reveal whether your error rate is typical."

**Length:** 1-2 sentences per card; 6-8 cards total

---

### Section 3: Language-Specific HOW-TO (Light Blue Border)

**Purpose:** Teach the techniques and syntax students need to accomplish the lab in each language.

**Content:** For each language (Bash, PowerShell, Python):
1. Brief intro (1 sentence)
2. Generalized code examples (not their answers)
3. Key concepts explained
4. Pattern they can adapt

**Code Example (Bash):**
```bash
# Extract Level column (field 2, comma-delimited)
cut -d',' -f2 system.csv | sort | uniq -c

# Extract Source column (field 3) and count
cut -d',' -f3 system.csv | sort | uniq -c | sort -rn
```
**Not:** "In your system.csv file, you'll have 2145 errors, 1203 warnings..."

**Code Example (PowerShell):**
```powershell
$csv = Import-Csv system.csv
$csv | Group-Object Level | Select-Object Name, Count
```
**Not:** Expected output showing their actual counts

**Code Example (Python):**
```python
import csv
from collections import Counter
level_counts = Counter(event['Level'] for event in events)
```
**Not:** `Counter({'Error': 2145, 'Warning': 1203, ...})`

**Key Concepts:** Explain WHY this syntax works, what each part does, when to use it

**Length:** 400-600 words total across all three languages

---

### Section 4: Key Challenge / Deep Dive (Amber Border)

**Purpose:** Identify the hardest technical part and scaffold it.

**Content:**
1. Name the challenge explicitly
2. Explain why it's hard
3. Show the approach/strategy (not the answer)
4. Give syntax hints in each language
5. Suggest a manual verification step

**Example (Timestamp Parsing):**
> "The trickiest part of this lab is extracting the hour from the timestamp. Question 4 asks for error timing patterns. To answer it, you must extract the hour from timestamps like **9/11/2026 2:34:45 PM**."
>
> "**Strategy:** Your timestamp has both date and time. The hour is the first number after the space: **2**:34:45. Your job is to parse all timestamps, extract just the hour, and count how many events occurred in each hour."
>
> "**Bash approach:** Split on spaces to get the time portion, then split on colons to get the hour."

**Length:** 200-300 words

---

### Section 5: Workflow / Next Steps (Green Border)

**Purpose:** Give students a clear sequence to follow.

**Content:** Numbered steps from "run the script" through "test on all files"

**Example:**
1. Run the export script - confirms you can create the CSV files
2. Open system.csv in Notepad - verify the structure
3. Write code to answer Q1 (count by Level) - your first working script
4. Add Q2 (percentages) - extend your script
5. Add Q3 (top 5 sources) - reuse your pattern from Q1
6. Add Q4 (hourly timing) - write just the hour-extraction part first, test on 5 lines manually
7. Add Q5 (stability assessment) - look at your results and write a conclusion
8. Test on all three files - verify it works on different data

**Length:** 1-2 sentences per step; 8-12 steps total

---

## Step 5 — Writing Principles

### Teach the Pattern, Not the Answer

**BAD:** "Your system has 2,145 error events. Here's why..."  
**GOOD:** "Use cut -d',' -f2 to extract the Level column. Then pipe to sort | uniq -c to count occurrences of each level."

**BAD:** "Most errors come from Service Control Manager (847 events)..."  
**GOOD:** "To find the top 5 sources, use Group-Object Source | Sort-Object Count -Descending | Select -First 5"

**BAD:** "The error rate is 57%, which is elevated..."  
**GOOD:** "Calculate percentages using the formula: (error_count / total_count) × 100"

### Show Syntax, Not Results

Every code example should:
- Show how to write it
- Explain what it does
- Be generalizable to their data
- NOT show actual output from their CSV

### Use Real-World Language

- "Parse timestamps" not "split strings"
- "Group by hour" not "extract time component"
- "Rank top 5" not "sort in descending order"
- "Stability assessment" not "write your opinion"

### Verification Strategies

Suggest manual verification steps:
- "Open system.csv in Notepad and manually count one type of event. Then write the bash command to get the same count."
- "Run Import-Csv and pipe to Group-Object Level to see how it groups your data."
- "Write a script that opens your CSV, reads it into a list, and prints the length. Then extend it to count by Level."

---

## Step 6 — Alignment with Assignment

Before publishing Lab Notes, verify alignment:

**Checklist:**
- ✓ "Why This Matters" reflects the real-world context from the assignment's Purpose box
- ✓ "Core Concept" section explains every lab question/goal from the assignment's Task box
- ✓ "HOW-TO" section covers every technique mentioned in the assignment's Instructions
- ✓ "Key Challenge" identifies the hardest technical part of the assignment
- ✓ "Workflow" suggests a sequence that mirrors the assignment's step-by-step process
- ✓ No section spoils answers or shows expected output from student data

---

## Critical Rules (DO NOT VIOLATE)

### Must Have
- ✓ **Published and student-facing** (not unpublished, not instructor-only)
- ✓ **Left-border boxes only** (4px left border, no full borders)
- ✓ **Five sections** in order: Why/Core/HOW-TO/Challenge/Workflow
- ✓ **Generalized code examples** (patterns, not answers)
- ✓ **No expected output** from student data
- ✓ **Clear workflow** with 8-12 sequential steps
- ✓ **Language-specific guidance** (bash, PowerShell, Python) when relevant

### Must NOT Do
- ✗ Show actual numbers/counts/percentages from lab data
- ✗ Provide complete solutions students can copy-paste
- ✗ Spoil the answers to lab questions
- ✗ Use full-border boxes (must be left-border only)
- ✗ Include instructor lecture notes content
- ✗ Place in instructor-only module
- ✗ Use em dashes (use space-hyphen-space instead)
- ✗ Make assumptions about what students will find

---

## Examples

### Example 1: Lab 5.1 Notes - Windows Event Log Analysis

**Reference:** Lab 5.1 Notes: Windows Event Log Analysis (BIT320, Sept 2026)

**Structure:**
1. **Why This Matters** (blue) — Context on system administration and logs
2. **Five Investigation Questions** (purple grid) — What each question asks
3. **Language-Specific HOW-TO** (light blue) — Bash/PowerShell/Python patterns for CSV parsing
4. **Key Challenge** (amber) — Timestamp parsing with syntax hints
5. **Workflow** (green) — 8-step sequence from "run script" to "test all files"

**Key Feature:** Shows HOW to extract columns and parse timestamps without showing actual event counts

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-09-11 | Initial specification based on Lab 5.1 Notes creation. Five-section structure with left-border boxes. Emphasis on teaching HOW-TO without spoiling answers. Applicable to BIT320 and similar technical lab courses. |

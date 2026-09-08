---
name: rubrics
description: Use when creating, auditing, or rebuilding Canvas rubrics for all assignments across all courses. Defines universal point distribution standard (25/50/100 scale), 3-level performance format (Excellent/Good/Unacceptable), grading criteria patterns, and reusable rubric templates.
---

# Neumont Canvas Rubrics Standard

**Version:** 3.1  
**Last Updated:** 2026-08-28  
**Applies to:** All courses (BIT221, BIT281, BIT320, PRO221, BIT351, etc.)

---

## Overview

This document defines the **universal rubric format** for all assignments across all Neumont courses. All rubrics use two foundational standards:

1. **Point Allocation:** All assignments use the 25/50/100 scale (see assignment-standards SKILL)
   - Simple = 25 pts
   - Medium = 50 pts
   - Large = 100 pts

2. **Performance Levels:** All rubrics use a consistent **3-level standard** (Excellent/Good/Unacceptable) for simplicity, consistency, and ease of grading.

**Key principle:** 3 levels apply to ALL assignments. The same rubric structure works whether the assignment is 25 pts or 100 pts - only the point values and criterion emphasis change.

---

## Critical: Assignment Element Ordering & Point Placement

**ENFORCED STRUCTURE:** All Canvas assignments must follow this exact element sequence. Violations of this structure invalidate the assignment layout.

```
1. Purpose Box (Blue table)
   └─ Real-world scenario + learning outcomes
2. Task Box (Yellow table)
   └─ Concrete statement of deliverable
3. Instructions (Plain HTML, no box)
   └─ Step-by-step procedures with expected outputs
4. Deliverables (Plain HTML, no box)
   └─ Explicit list of what student must submit
5. Criteria for Success Box (Green table)
   └─ Grading criteria ONLY  -  NO point values
   └─ NO additional "Success looks like" statement after this box
   └─ THIS IS THE FINAL ELEMENT  -  nothing comes after this box
```

**Point Values Rule:**
- ✅ Point values BELONG: In the Canvas rubric ONLY
- ❌ Point values DO NOT BELONG: Anywhere in the assignment description
- ❌ Point values DO NOT BELONG: Inside Criteria box (neither as separate lines nor inline like "(5 pts)")
- ❌ Point values DO NOT BELONG: In separate "Success looks like" statements after Criteria box

**Criteria Box is FINAL:**
- ✅ Criteria for Success box must be the last element in the assignment
- ❌ No Deliverables section AFTER the Criteria box
- ❌ No "Success looks like" statement AFTER the Criteria box
- ❌ No additional text, headers, or callouts AFTER the Criteria box

**Why This Matters:**
- Canvas rubric points are the authoritative grading specification
- Assignment description should frame the task and criteria WITHOUT duplicating points
- Visual structure is clear to students: read why (Purpose) → what to do (Task) → how to do it (Instructions) → what to turn in (Deliverables) → how we'll grade (Criteria box)

---

## Critical Rules for Rubrics (Do Not Violate)

- ✅ **All rubrics use 3 performance levels:** Excellent, Good, Unacceptable
- ✅ **Point values match assignment totals:** 25 pts, 50 pts, or 100 pts only
- ✅ **Performance levels have clear descriptions** (not just names like "Excellent")
- ✅ **Rubrics align with assignment's Purpose/Task/Criteria boxes**
- ✅ **Good level = 65-75% of Excellent points** (enables partial credit while staying clean)
- ✅ **Rubrics marked "Reusable: Yes"** for consistency across similar assignments
- ❌ **NEVER put point values in the assignment's Criteria for Success box**  -  Points belong ONLY in the rubric, not in assignment text
- ❌ **NEVER embed points inline in criterion descriptions**  -  Examples: "(5 pts)", "(3 pts)", "(2 pts)" are forbidden. Criterion descriptions describe WHAT is graded, not HOW MANY points
- ❌ **NEVER place Deliverables AFTER the Criteria box**  -  Deliverables come BEFORE; Criteria box is final element
- ❌ **NEVER add "Success looks like" text after Criteria box**  -  The Criteria box itself is the success specification; don't duplicate it
- ❌ **Never use half-points** (10, 7, 0 is cleaner than 10, 6.5, 0)
- ❌ **Never use 4+ performance levels** (3-level standard is universal)
- ❌ **Never leave descriptions blank** (explain what each level looks like)

---

## Core Principle: Point Distribution = Effort Distribution

**Every criterion's point value should reflect the actual effort required to complete or assess that criterion.** This is a guideline, not a formula - each assignment is different, and effort varies by criterion type and context.

- A criterion representing 15% of the work gets ~15% of points
- A criterion representing 35% of the work gets ~35% of points  
- A criterion representing 25% of the work gets ~25% of points
- Use professional judgment; don't force-fit a model when the actual effort distribution differs

**Well Formatted Document (Criterion 1) receives elevated weight (15-20%) to reinforce documentation and professional communication skills.**

---

## Rubric Structure by Point Total

All rubrics use 3-5 criteria with Excellent/Good/Unacceptable levels. Point distribution varies by assignment, but follows this guidance:

### **25-Point Assignments (Simple)**
- **Number of criteria:** 3 (Well Formatted + 2 task-specific)
- **Well Formatted Document:** 3-4 pts (12-16%, typically 4 pts)
- **Primary task/verification:** 10-11 pts (40-44%)
- **Secondary task/verification:** 10-12 pts (40-48%)
- **Good level:** 65-75% of Excellent per criterion
- **Example:** Environment setup, simple verification, basic completion tasks

### **50-Point Assignments (Medium)**
- **Number of criteria:** 4 (Well Formatted + 3 task-specific)
- **Well Formatted Document:** 8 pts (16%, reinforces documentation importance)
- **Remaining criteria:** Distributed by actual effort (typically 14-16 pts each for 3-4 criteria)
- **Good level:** 65-75% of Excellent per criterion
- **Example:** Single-system labs, moderate analysis tasks, skill-building work

### **100-Point Assignments (Large)**
- **Number of criteria:** 5-6 (Well Formatted + 4-5 task-specific)
- **Well Formatted Document:** 15-16 pts (15-16%, reinforces documentation importance)
- **Remaining criteria:** Distributed by actual effort (typically 18-22 pts each for 4-5 criteria)
- **Good level:** 65-75% of Excellent per criterion
- **Example:** Multi-component labs, capstones, complex analysis with reflection

---

## Universal Rubric Template (All Assignments, All Sizes)

Every rubric follows this structure: **Well Formatted Document ALWAYS as Criterion 1**, followed by task-specific criteria. All use Excellent/Good/Unacceptable levels.

```
Rubric Name: [Assignment Name]
Total Points: [25/50/100]
Reusable: Yes

Criterion 1: Well Formatted Document (X points, 15-20% of total)
  Description: Submission is professionally formatted with clear identification, labeled deliverables, and organized sections.
  Excellent (X points)  -  Submission includes clear identification (name, course, assignment). All screenshots/outputs labeled. Professional formatting and organization.
  Good (X*0.70 points)  -  Submission includes most required information. Most screenshots labeled. Minor formatting issues.
  Unacceptable (0 points)  -  Missing identification or clear organization. Screenshots unlabeled. Unprofessional formatting.

Criterion 2: [Primary Task/Deliverable] (Y points, distributed by effort)
  Description: [What is being assessed? What skill or deliverable does this criterion measure?]
  Excellent (Y points)  -  [Complete, correct, demonstrates mastery of core skill]
  Good (Y*0.70 points)  -  [Mostly complete with minor gaps or minor issues]
  Unacceptable (0 points)  -  [Missing, broken, or demonstrates lack of understanding]

Criterion 3: [Secondary Component/Verification] (Z points, distributed by effort)
  Description: [What is being assessed?]
  [Same 3-level structure]

Criterion 4+ (Optional for 50/100-pt): [Additional component by effort] (W points, distributed by effort)
  Description: [What is being assessed?]
  [Same 3-level structure for additional criteria]
```

**Point calculation:**
- Well Formatted Document gets 15-20% of total (reinforces documentation skills)
- Remaining points distributed proportionally to actual criterion effort (not equal chunks)
- Good level = 65-75% of Excellent points per criterion (use 0.70 multiplier for clean numbers)
- Example: Excellent = 20 pts → Good = 14 pts
- Example: Excellent = 8 pts → Good = 5-6 pts (60-75% range)
- Example 25-pt breakdown: Well Formatted (4 pts, 16%) + Task 1 (10 pts, 40%) + Task 2 (11 pts, 44%)

---

## Examples by Point Total

### Example 1: 25-Point Assignment (Simple  -  Environment Setup)

```
Rubric: Lab 1.1  -  Infrastructure Setup
Total Points: 25
Reusable: Yes

Criterion 1: Well Formatted Document (4 points)
  Description: Document is professionally formatted with clear student/course identification, organized sections, and labeled screenshots.
  Excellent (4)  -  Document includes name, course code, assignment name clearly labeled; all sections organized with titles; every screenshot has descriptive label
  Good (3)  -  Mostly includes required info; sections mostly titled; most screenshots labeled
  Unacceptable (0)  -  Missing clear identification or labels; disorganized structure

Criterion 2: Environment Installation (10 points)
  Description: All three environments (Bash, Python, PowerShell) are successfully installed and operational.
  Excellent (10)  -  All three environments successfully installed and fully functional; versions match or exceed requirements
  Good (7)  -  Two or more environments working; minor installation issues resolved or workarounds documented
  Unacceptable (0)  -  One or more environments not installed or non-functional

Criterion 3: Verification & Testing (11 points)
  Description: Version checks and test commands confirm that all environments are properly configured and ready for use.
  Excellent (11)  -  All version checks pass; test commands produce correct output in all environments; testing evidence clear
  Good (8)  -  Version checks pass for most environments; test commands mostly work with minor issues
  Unacceptable (0)  -  Version checks fail or test commands don't work; insufficient testing evidence
```

### Example 2: 50-Point Assignment (Medium  -  Hands-On Lab)

```
Rubric: Lab 2.1  -  Log Summary Script
Total Points: 50
Reusable: Yes

Criterion 1: Well Formatted Document (8 points)
  Description: Submission is professionally formatted with complete identification, organized sections, and labeled screenshots/outputs.
  Excellent (8)  -  Complete identification (name, course, assignment date); all sections clearly titled; every screenshot and output labeled with descriptive captions; professional formatting
  Good (6)  -  Most identification info present; sections mostly titled; most screenshots labeled
  Unacceptable (0)  -  Missing identification or labels; unclear section organization; disorganized

Criterion 2: Script Functionality (15 points)
  Description: Script executes successfully and correctly processes log data to produce an accurate summary.
  Excellent (15)  -  Script runs without errors; correctly processes all log entries; produces accurate summary; handles edge cases
  Good (11)  -  Script runs with minor issues; processes most log entries; summary mostly accurate
  Unacceptable (0)  -  Script doesn't run or produces incorrect results

Criterion 3: Code Quality (14 points)
  Description: Code is well-organized, readable, and demonstrates understanding of bash idioms and best practices.
  Excellent (14)  -  Well-commented; clear variable names; demonstrates language idioms and best practices; logic is easy to follow
  Good (10)  -  Good comments; clear logic; adequate code organization; minor improvements possible
  Unacceptable (0)  -  Minimal or no comments; poor readability; unclear logic

Criterion 4: Deliverables & Output (13 points)
  Description: All required files and outputs are provided and demonstrate successful task completion.
  Excellent (13)  -  Script, output file, and documentation all provided; output is professional and demonstrates task completion
  Good (9)  -  All deliverables present; output is complete but formatting could be clearer
  Unacceptable (0)  -  Missing deliverables or output doesn't demonstrate task completion
```

### Example 3: 100-Point Assignment (Large  -  Complex Lab with Comparative Analysis)

```
Rubric: Lab 5.1  -  Performance Baseline & Trending Capstone
Total Points: 100
Reusable: Yes

Criterion 1: Well Formatted Document (16 points)
  Description: Submission includes professional formatting, complete identification, organized sections, and clearly labeled all deliverables and evidence.
  Excellent (16)  -  Complete cover page with name, course, assignment, date; all sections clearly titled and organized; every screenshot/output labeled with descriptive caption; professional formatting throughout
  Good (11)  -  Cover page present; sections mostly titled; most screenshots labeled; minor formatting inconsistencies
  Unacceptable (0)  -  Missing cover page or critical info; unclear section organization; most screenshots unlabeled

Criterion 2: Data Collection & Analysis (25 points)
  Description: Performance metrics are collected over sufficient time period and analyzed to identify trends and capacity risks.
  Excellent (25)  -  Performance metrics collected over 24+ hours; trend analysis is thorough and accurate; capacity risks clearly identified; methodology well documented
  Good (18)  -  Metrics collected; analysis mostly accurate with minor gaps; most trends identified
  Unacceptable (0)  -  Data collection incomplete or analysis missing/inaccurate

Criterion 3: Script Quality & Production Readiness (20 points)
  Description: Code demonstrates language mastery with robust error handling, comprehensive logging, and production-quality standards.
  Excellent (20)  -  Code demonstrates language mastery; error handling robust; logging comprehensive; suitable for production deployment
  Good (14)  -  Good code quality; most error cases handled; adequate logging; minor refinements needed
  Unacceptable (0)  -  Poor code quality; minimal error handling or logging

Criterion 4: Comparative Analysis (19 points)
  Description: Analysis clearly compares tool and language choices, justifies selection, and thoughtfully examines trade-offs against alternatives.
  Excellent (19)  -  Clear comparison of tool/language choices; explains why selected tool is appropriate; identifies trade-offs thoughtfully; alternatives considered
  Good (13)  -  Good comparison of approach; tool selection rationale clear; most trade-offs mentioned
  Unacceptable (0)  -  No comparison or superficial analysis

Criterion 5: Reflection & Insight (20 points)
  Description: Reflection demonstrates deep understanding of challenges, paradigm differences, and personal learning from the capstone project.
  Excellent (20)  -  Thoughtful reflection on challenges, paradigm differences, and learnings; 250+ words; demonstrates deep understanding
  Good (14)  -  Adequate reflection on approach and choices; 150-250 words; shows competency
  Unacceptable (0)  -  Missing or minimal reflection (under 150 words)
```

---

## Performance Level Descriptions (3-Level Standard)

Use these as templates when writing criterion descriptions. All criteria use three levels: Excellent, Good, and Unacceptable.

**Excellent Level:**
- All core requirements met and working correctly
- Demonstrates thorough understanding or mastery
- No significant gaps or errors
- Clearly documented with comprehensive evidence
- Shows competency in the criterion's focus area

**Good Level (65-75% of criterion points):**
- Most requirements met with minor gaps or issues
- Core functionality working; some refinement or edge cases unaddressed
- Mostly documented; 1-2 areas lack detail
- Demonstrates solid competency with room for improvement
- Acceptable work quality

**Unacceptable Level:**
- Requirements not met or fundamentally broken
- Does not work or not attempted/submitted
- Critical gaps or misunderstandings evident
- Insufficient evidence of competency
- Does not meet minimum threshold

---

## Code Quality Scoring Progression (BIT320 2-Credit Constraint)

Since BIT320 is only 2 credits with 20 contact hours, code quality must be scored **progressively**, not all-or-nothing. Build competency across 5 weeks rather than requiring mastery in Week 1.

### Progressive Rubric Addition: "Code Fundamentals" Criterion

**Add this criterion to every BIT320 lab rubric** (Labs 1.2 - 5.1) at 10-12% of points (independent from "Well Formatted Document"). Score on:

**Week 1-2: Functions & Loops Foundation**
- Excellent (10 pts): Script uses 2-3 functions to organize logic; loops used to iterate over data; code is not all procedural
- Good (7 pts): Functions present but could be better organized; loop present but basic; some procedural code remains
- Unacceptable (0 pts): No functions defined; no loops used; entirely procedural

**Week 3-4: Error Handling & Recovery**
- Excellent (10 pts): Functions + loops + try/except or error checks on all external calls; graceful failure; meaningful error messages
- Good (7 pts): Some error handling present; most external calls validated; 1-2 unchecked operations
- Unacceptable (0 pts): No error handling; crashes on input errors; silent failures

**Week 5: Production Patterns & Testing**
- Excellent (10 pts): Functions + loops + error handling + logging with timestamps + evidence of testing multiple scenarios; code is production-ready
- Good (7 pts): All elements present; logging minimal or incomplete; tested on happy path only
- Unacceptable (0 pts): Missing logging or testing; error handling incomplete

### Rubric Template (add to all BIT320 labs)

```
Criterion X: Code Fundamentals (10 points, 10-12% of total)
  Description: [Use description from week's progression above]
  Excellent (10) — [Week-appropriate standards met]
  Good (7) — [Week-appropriate, partial implementation]
  Unacceptable (0) — [Missing critical elements]
```

### Why Progressive, Not All-In-Week-1?

- **2-credit constraint:** Students can't master advanced error handling and testing while learning 3 new languages simultaneously
- **Building competency:** Functions first (Week 1-2) → error handling (Week 3-4) → production patterns (Week 5)
- **Rubric clarity:** Instructors know exactly what to score each week; students know expectations scale with their experience
- **Scaffolding:** Each week's new assignment builds on prior weeks' code fundamentals

### Implementation Note

When creating rubrics for BIT320 labs:
1. Keep "Well Formatted Document" as Criterion 1 (15-16 pts, 15-20%)
2. Add "Code Fundamentals" as Criterion 2 (10 pts, 10-12%)
3. Remaining criteria (3-5): Task-specific (60-70%)
4. Total should match assignment points (25, 50, or 100)

---

## Alignment with Assignment Content

Before finalizing a rubric, verify it aligns with the assignment's Purpose/Task/Criteria boxes:

**Checklist:**
- ✓ Well Formatted Document is always Criterion 1 (15-20% of points)
- ✓ All major criteria from assignment's "Criteria for Success" box appear in rubric
- ✓ Rubric doesn't grade on criteria NOT mentioned in the assignment
- ✓ Performance levels match what students can reasonably expect from assignment description
- ✓ Point distribution reflects actual effort for each criterion
- ✓ Partial-credit levels (Good level) are achievable with reasonable effort

---

## Critical Rules (DO NOT VIOLATE)

### Must Have
- ✓ **All rubrics use 3 levels:** Excellent, Good, Unacceptable (no exceptions)
- ✓ **"Well Formatted Document" is ALWAYS Criterion 1** (15-20% of total points, reinforces documentation skills)
- ✓ **Clear performance-level descriptions** (not just level names  -  explain what "Excellent" looks like, when work is "Good," when it's "Unacceptable")
- ✓ **Point values sum exactly to assignment total** (25, 50, or 100 only)
- ✓ **Point distribution matches actual criterion effort** (guideline, not formula; adjust per context)
- ✓ **Rubric marked "Reusable: Yes"** (identical assignments can share rubrics)
- ✓ **Good level at 65-75% of Excellent points** (enables partial credit cleanly; use 0.70 multiplier for simplicity)
- ✓ **Alignment with assignment's Criteria for Success box** (don't grade on criteria not mentioned in assignment)

### Must NOT Do
- ✗ Use 4 or more performance levels (3-level standard is universal)
- ✗ Use "Satisfactory," "Developing," or other 4+ level variants
- ✗ Put Well Formatted Document anywhere except Criterion 1
- ✗ Reduce Well Formatted Document below 15% (undoes documentation reinforcement goal)
- ✗ Leave performance-level descriptions blank or vague ("Good work" is insufficient)
- ✗ Create duplicate criterion "Documentation & Deliverables" (absorbed into Well Formatted Document)
- ✗ Grade on formatting more heavily than actual competency (Well Formatted is max 20%, not a majority)
- ✗ Mark rubrics as non-reusable if similar assignments could use them
- ✗ Use half-points unless unavoidable (10, 7, 0 is cleaner than 10, 6.5, 0)

### Flexible Elements
- **Number of criteria:** 3-5 is typical (Well Formatted + 2-4 task-specific)
- **Specific point values and percentages:** Follow structural guidelines but adjust to match actual criterion effort
- **Exact wording of performance levels:** Customize for technical accuracy and clarity to students
- **Criterion names and descriptions:** Adapt to assignment specifics, but structure always follows Well Formatted first

---

## Examples

### Example 1: Type A (Simple Training, Binary  -  Exception)
```
Rubric: LinkedIn Learning Training Submission
Total Points: 10
Reusable: Yes

Criterion 1: Training Completion (10 points)
  Full Credit (10)  -  Completion certificate or screenshot submitted showing course finished
  No Credit (0)  -  No certificate/screenshot or doesn't show completion
```

### Example 2: Type B+ (Research Paper, 3 Levels)
```
Rubric: "What Are Containers?" Research Paper
Total Points: 50
Reusable: Yes

Criterion 1: Well Formatted Document (5 points)
  Excellent (5)  -  Title page with name, course, assignment; clear sections with titles; professional formatting
  Good (3)  -  Title page present but incomplete; sections mostly clear; minor formatting issues
  Unacceptable (0)  -  Missing title page; unclear organization; poor formatting

Criterion 2: Content Depth & Accuracy (15 points)
  Excellent (15)  -  Covers isolation, images, registries, orchestration with accurate technical detail
  Good (11)  -  Covers most topics; minor accuracy or depth issues
  Unacceptable (0)  -  Incomplete or inaccurate treatment

Criterion 3: Organization & Clarity (15 points)
  Excellent (15)  -  Logical structure, clear paragraphs, flows naturally from topic to topic
  Good (11)  -  Mostly organized; some transitions could be smoother
  Unacceptable (0)  -  Confusing structure, hard to follow

Criterion 4: Critical Analysis & Insight (15 points)
  Excellent (15)  -  Analyzes when containers are useful, compares to alternatives, identifies trade-offs
  Good (11)  -  Good analysis of container benefits and use cases
  Unacceptable (0)  -  Mostly descriptive with no analysis
```

### Example 3: Type B+ (Single Lab, 3 Levels)  -  See Step 2 Example 1 above

### Example 4: Type B+ (Multi-Scenario Lab, 3 Levels)  -  See Step 2 Example 2 above

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 3.1 | 2026-08-28 | **REFINEMENT:** Elevated Well Formatted Document weight to 15-20% (from 8-10%) to reinforce documentation and professional communication skills. Rewrote Core Principle section to emphasize effort-based distribution (guideline, not formula). Simplified structure to remove old Step 3-6 sections. Updated all three examples (25/50/100-pt) to reflect new Well Formatted Document weighting. Clarified Critical Rules to remove Type A/B+ references and strengthen documentation requirement. |
| 3.0 | 2026-08-28 | **MAJOR REVISION:** Integrated 25/50/100 point allocation standard into rubric specification. Removed all Type A/B/C/D designations. Unified all assignments under single 3-level format (Excellent/Good/Unacceptable). Point distribution now tied to assignment complexity (25/50/100 pts). Simplified examples to align with new point scale. Applies to ALL courses (BIT221, BIT281, BIT320, PRO221, BIT351). |
| 2.0 | 2026-08-27 | Standardized on 3-level rubric format (Excellent/Good/Unacceptable) for most assignment types. Removed 4-level variants. Simplified point distribution to 65-75% scale for "Good" level. |
| 1.0 | 2026-07-27 | Initial specification based on PRO221 audit. Multiple assignment types with variable rubric structures. |

---
name: rubrics
description: Use when creating, auditing, or rebuilding Canvas rubrics for technical and research assignments in PRO221. Defines standard format, point distribution, performance levels, and reusable templates.
---

# Canvas Rubrics Playbook for PRO221

**Version:** 1.0  
**Last Updated:** 2026-07-27  
**Based on:** PRO221 course audit and engineering/research assignment best practices

---

## Overview

This document defines the **canonical rubric format** for PRO221 assignments across all weeks. Rubrics should provide clear, graduated feedback with appropriate partial-credit opportunities for complex technical and research work.

**Key principle:** Rubric structure matches assignment complexity. Simple assignments use binary rubrics; complex assignments use graduated scales with performance-level descriptions.

---

## Step 0 — Gotchas

- Rubrics must be reusable (enabled in Canvas) for consistency across similar assignment types
- Point values in rubric must match assignment's total points possible
- Performance levels must have clear descriptions (not just names like "Excellent")
- Minor criteria (formatting) should be 4-10% of total points; major technical criteria 30-60% each
- Never use half-points (like 7.5) unless explicitly necessary for the grading scale
- All rubrics must align with the assignment's Purpose/Task/Criteria boxes
- Rubrics are NOT stored in the SKILL itself—this SKILL defines the *format*, not the content

---

## Step 1 — Assignment Type Classification

Classify the assignment before designing its rubric:

### **Type A: Simple/Completion Assignments**
- **Examples:** Watch training video, submit screenshot, discussion post, quiz
- **Characteristics:** Pass/fail, no gradation needed
- **Rubric:** 1 criterion, binary (Full Credit or No Credit)
- **Point range:** Usually 5-15 points
- **Time to complete:** < 1 hour

### **Type B: Moderate Technical Assignments**
- **Examples:** Single lab (install/configure one service), small research question, short document
- **Characteristics:** Can be partially correct, but scope is limited
- **Rubric:** 3-5 criteria, 3 performance levels per criterion (Excellent, Good, Unacceptable)
- **Point range:** Usually 50-100 points
- **Time to complete:** 2-4 hours
- **Partial credit:** "Good" level captures 60-80% completion

### **Type C: Complex Technical Assignments**
- **Examples:** Multi-scenario labs (4+ distinct tasks), comprehensive research papers, multi-day projects
- **Characteristics:** Multiple sub-tasks, significant opportunity for partial work
- **Rubric:** 4-6 criteria (or grouped sub-criteria), 4 performance levels (Excellent, Good, Satisfactory, Unacceptable)
- **Point range:** Usually 100-150 points
- **Time to complete:** 4-8 hours or spread over days
- **Partial credit:** Clear gradation allows credit for 25%, 50%, 75%, 100% completion

### **Type D: Research/Analytical Assignments**
- **Examples:** What-Are-Containers research paper, design documentation, analysis reports
- **Characteristics:** Judgment-based grading (content depth, clarity, reasoning)
- **Rubric:** 4-5 criteria (Content Depth, Clarity, Critical Analysis, Organization, Writing Quality), 4 performance levels
- **Point range:** Usually 50-100 points
- **Time to complete:** 3-6 hours

---

## Step 2 — Rubric Structure Template by Type

### **Type A: Simple/Completion (Binary)**

```
Rubric Name: [Assignment Name]
Total Points: [X]
Reusable: Yes

Criterion 1: [Task Name] (X points)
  Level 1: Full Credit (X points) — Task completed and submitted
  Level 2: No Credit (0 points) — Task not completed or not submitted
```

**Example: Online Training Completion**
```
Total Points: 15
Reusable: Yes

Criterion 1: Training Completion Screenshot (15 points)
  Level 1: Full Credit (15 points) — Screenshot shows course completion
  Level 2: No Credit (0 points) — Screenshot missing or doesn't show completion
```

---

### **Type B: Moderate Technical (3 Levels)**

```
Rubric Name: [Assignment Name]
Total Points: [X] (typically 50-100)
Reusable: Yes

Criterion 1: [Minor element - Formatting/Documentation] (X points, 4-10% of total)
  Level 1: Excellent (X points) — Well-formatted, clear documentation
  Level 2: Good (X*0.6-0.8 points) — Mostly formatted, some documentation issues
  Level 3: Unacceptable (0 points) — Poorly formatted, missing documentation

Criterion 2: [Major technical element 1] (Y points, 30-45% of total)
  Level 1: Excellent (Y points) — [Specific description of full completion]
  Level 2: Good (Y*0.6-0.8 points) — [Specific description of 60-80% completion]
  Level 3: Unacceptable (0 points) — [Specific description of failure]

Criterion 3: [Major technical element 2] (Y points, 30-45% of total)
  [Same 3-level structure]

Criterion 4: [Major technical element 3] (optional, 20-30% of total)
  [Same 3-level structure]
```

**Example: Single IIS Configuration Lab**
```
Total Points: 75
Reusable: Yes

Criterion 1: Documentation (7 points)
  Level 1: Excellent (7 points) — Clear screenshots, step documentation
  Level 2: Good (5 points) — Some screenshots, minimal documentation
  Level 3: Unacceptable (0 points) — No documentation

Criterion 2: IIS Installation & Role (23 points)
  Level 1: Excellent (23 points) — IIS installed, Web Server role configured, default website running
  Level 2: Good (15 points) — IIS installed, role mostly configured, website has issues
  Level 3: Unacceptable (0 points) — IIS not installed or non-functional

Criterion 3: Website Configuration (23 points)
  Level 1: Excellent (23 points) — Custom website created, correct bindings, content deployed
  Level 2: Good (15 points) — Website created, bindings incomplete or content issues
  Level 3: Unacceptable (0 points) — No custom website or non-functional

Criterion 4: Verification & Testing (22 points)
  Level 1: Excellent (22 points) — Site accessible locally and remotely, all features working
  Level 2: Good (15 points) — Site accessible but with minor issues
  Level 3: Unacceptable (0 points) — Site not accessible or non-functional
```

---

### **Type C: Complex Technical (4 Levels with Sub-Criteria)**

```
Rubric Name: [Assignment Name]
Total Points: [X] (typically 100-150)
Reusable: Yes

Criterion 1: [Minor element] (X points, 4-10% of total)
  Level 1: Excellent (X points) — [Full description]
  Level 2: Good (X*0.75 points) — [75% completion description]
  Level 3: Satisfactory (X*0.5 points) — [50% completion description]
  Level 4: Unacceptable (0 points) — [Missing/failed description]

Criterion 2: [Scenario 1 or Major Element 1] (Y points, 25-30% of total)
  Level 1: Excellent (Y points) — [All requirements met, no gaps]
  Level 2: Good (Y*0.75 points) — [75% of requirements met, minor gaps]
  Level 3: Satisfactory (Y*0.5 points) — [50% of requirements met, major gaps]
  Level 4: Unacceptable (0 points) — [Not attempted or fundamentally broken]

Criterion 3: [Scenario 2 or Major Element 2] (Y points, 25-30% of total)
  [Same 4-level structure]

Criterion 4: [Scenario 3 or Major Element 3] (Y points, 25-30% of total)
  [Same 4-level structure]

Criterion 5: [Verification/Testing] (Z points, 10-15% of total)
  [Same 4-level structure]
```

**Example: 4-Scenario Performance Monitoring Lab (100 points)**
```
Total Points: 100
Reusable: Yes

Criterion 1: Documentation & Screenshots (10 points)
  Level 1: Excellent (10 points) — All 4 scenarios documented with clear screenshots
  Level 2: Good (7.5 points) — 3 scenarios documented, 1 missing or unclear
  Level 3: Satisfactory (5 points) — 2 scenarios documented, 2 incomplete
  Level 4: Unacceptable (0 points) — Minimal or no documentation

Criterion 2: Scenario 1 - CPU/RAM Baseline (23 points)
  Level 1: Excellent (23 points) — Baseline captured, documented, values reasonable for idle system
  Level 2: Good (17 points) — Baseline captured, documentation incomplete or values questionable
  Level 3: Satisfactory (11 points) — Baseline attempted but incomplete or inaccurate
  Level 4: Unacceptable (0 points) — No baseline or fundamentally incorrect

Criterion 3: Scenario 2 - Memory Pressure (23 points)
  Level 1: Excellent (23 points) — Stress test applied, memory usage elevated, data captured correctly
  Level 2: Good (17 points) — Stress test applied, data mostly correct with minor issues
  Level 3: Satisfactory (11 points) — Stress test attempted, data incomplete or questionable
  Level 4: Unacceptable (0 points) — No stress test or data captured

Criterion 4: Scenario 3 - Disk I/O (23 points)
  [Same 4-level structure as Scenario 2]

Criterion 5: Scenario 4 - Network Activity (21 points)
  [Same 4-level structure as Scenario 2]
```

---

### **Type D: Research/Analytical (4 Levels)**

```
Rubric Name: [Assignment Name]
Total Points: [X] (typically 50-100)
Reusable: Yes

Criterion 1: Content Depth & Accuracy (X*0.35 points)
  Level 1: Excellent (X*0.35 points) — Comprehensive coverage, accurate technical details, well-researched
  Level 2: Good (X*0.26 points) — Mostly complete, minor accuracy issues or gaps
  Level 3: Satisfactory (X*0.17 points) — Basic coverage, some accuracy issues, limited depth
  Level 4: Unacceptable (0 points) — Incomplete, inaccurate, or superficial treatment

Criterion 2: Clarity & Organization (X*0.25 points)
  Level 1: Excellent (X*0.25 points) — Logical flow, clear structure, easy to follow
  Level 2: Good (X*0.19 points) — Mostly clear, minor organizational issues
  Level 3: Satisfactory (X*0.12 points) — Understandable but hard to follow in places
  Level 4: Unacceptable (0 points) — Disorganized, confusing, or hard to read

Criterion 3: Critical Analysis (X*0.25 points)
  Level 1: Excellent (X*0.25 points) — Insightful analysis, questions assumptions, connects to broader context
  Level 2: Good (X*0.19 points) — Good analysis, some critical thinking, could go deeper
  Level 3: Satisfactory (X*0.12 points) — Surface-level analysis, mostly descriptive
  Level 4: Unacceptable (0 points) — No analysis, purely summary

Criterion 4: Writing Quality (X*0.15 points)
  Level 1: Excellent (X*0.15 points) — Professional writing, proper grammar, correct terminology
  Level 2: Good (X*0.11 points) — Minor grammar/spelling issues, mostly professional
  Level 3: Satisfactory (X*0.07 points) — Multiple errors but understandable
  Level 4: Unacceptable (0 points) — Poor writing, hard to understand
```

**Example: "What Are Containers?" Research Paper (50 points)**
```
Total Points: 50
Reusable: Yes

Criterion 1: Content Depth & Technical Accuracy (17 points)
  Level 1: Excellent (17 points) — Covers isolation, images, registries, orchestration; accurate details
  Level 2: Good (13 points) — Covers most topics, minor accuracy or depth issues
  Level 3: Satisfactory (8 points) — Basic coverage, some topics thin or inaccurate
  Level 4: Unacceptable (0 points) — Incomplete or inaccurate treatment

Criterion 2: Organization & Clarity (13 points)
  Level 1: Excellent (13 points) — Logical structure, clear paragraphs, easy to follow
  Level 2: Good (10 points) — Mostly organized, some transitions could be clearer
  Level 3: Satisfactory (6 points) — Readable but organization could be improved
  Level 4: Unacceptable (0 points) — Confusing structure, hard to follow

Criterion 3: Analysis & Critical Thinking (13 points)
  Level 1: Excellent (13 points) — Analyzes when containers are useful, compares to alternatives
  Level 2: Good (10 points) — Good analysis of container benefits and use cases
  Level 3: Satisfactory (6 points) — Mostly descriptive with limited analysis
  Level 4: Unacceptable (0 points) — No analysis

Criterion 4: Writing Quality (7 points)
  Level 1: Excellent (7 points) — Professional grammar, proper spelling, technical terms used correctly
  Level 2: Good (5 points) — Minor errors, overall professional
  Level 3: Satisfactory (3 points) — Multiple errors but understandable
  Level 4: Unacceptable (0 points) — Poor writing quality
```

---

## Step 3 — Performance Level Descriptions (Generic Templates)

Use these descriptions as starting points, customizing for your specific criteria:

### **Type B/C: Technical Assignments**

**Excellent Level:**
- "All requirements met and working correctly"
- "Thorough understanding demonstrated"
- "No significant gaps or errors"
- "Clearly documented with evidence"

**Good Level (Type B: 60-80% | Type C: 75%):**
- "Most requirements met with minor gaps"
- "Core functionality working but some edge cases missed"
- "Mostly documented, 1-2 items lack detail"
- "Demonstrates solid understanding with room for improvement"

**Satisfactory Level (Type C only: 50%):**
- "About half the requirements met"
- "Basic functionality present but significant gaps"
- "Partially documented"
- "Demonstrates understanding of core concepts but incomplete execution"

**Unacceptable Level:**
- "Requirements not met"
- "Doesn't work or fundamentally broken"
- "Not attempted or not submitted"
- "Critical misunderstandings or missing core elements"

### **Type D: Research/Analytical**

**Excellent:**
- "Comprehensive and well-researched"
- "Shows critical thinking and analysis"
- "Insightful connections and deeper understanding"

**Good:**
- "Thorough but could explore further"
- "Good analysis with some depth"
- "Minor gaps in coverage"

**Satisfactory:**
- "Covers basics adequately"
- "Mostly descriptive rather than analytical"
- "Could benefit from more research or depth"

**Unacceptable:**
- "Incomplete or inaccurate"
- "Lacks critical thinking"
- "Missing significant content"

---

## Step 4 — Point Distribution Standards

**Type A (Simple, binary):**
- Single criterion: 100% of total points

**Type B (Moderate, 3 levels):**
- Formatting/Documentation: 4-10% (4-10 pts on 100-pt assignment)
- Major criterion 1: 30-45%
- Major criterion 2: 30-45%
- Major criterion 3 (optional): 20-30%

**Type C (Complex, 4 levels):**
- Formatting/Documentation: 4-10%
- Scenario 1 / Major element 1: 23-30%
- Scenario 2 / Major element 2: 23-30%
- Scenario 3 / Major element 3: 23-30%
- Verification/Testing (optional): 10-15%

**Type D (Research, 4 levels):**
- Content Depth: 35%
- Clarity & Organization: 25%
- Critical Analysis: 25%
- Writing Quality: 15%

---

## Step 5 — Reusable Rubric Strategy

Templates for common assignment patterns that recur across weeks:

### **IaC Implementation Labs** (Type C, 4 levels)
- Documentation (10%)
- Installation/Setup (25%)
- Configuration (30%)
- Testing/Verification (35%)

### **Networking Labs** (Type C, 4 levels)
- Documentation (10%)
- Network Design/Planning (25%)
- Configuration (30%)
- Testing/Connectivity (35%)

### **Clustering/HA Labs** (Type C, 4 levels)
- Documentation (10%)
- Cluster Setup (25%)
- Failover Configuration (30%)
- Failover Testing (35%)

### **Research Papers** (Type D, 4 levels)
- Content Depth (35%)
- Organization (25%)
- Analysis (25%)
- Writing Quality (15%)

### **Multi-Scenario Labs** (Type C, 4 levels per scenario)
- Documentation (10%)
- Scenario 1 (23%)
- Scenario 2 (23%)
- Scenario 3 (23%)
- Verification (21%)

---

## Step 6 — Alignment with Assignment Content

Before finalizing a rubric, verify it aligns with the assignment's Purpose/Task/Criteria boxes:

**Checklist:**
- ✓ All major criteria from the assignment's "Criteria for Success" box appear in the rubric
- ✓ Rubric doesn't grade on criteria NOT mentioned in the assignment
- ✓ Performance levels match what students can reasonably expect to understand from assignment description
- ✓ Point distribution reflects the emphasis in the assignment instructions
- ✓ Partial-credit levels are achievable with the effort implied by the assignment scope

---

## Critical Rules (DO NOT VIOLATE)

### Must Have
- ✓ Clear performance-level descriptions (not just "Excellent/Good/Poor" with no detail)
- ✓ Point values that sum to the assignment's total points
- ✓ Rubric marked "Reusable: Yes" (except for one-time assignments)
- ✓ Alignment with assignment's Criteria for Success box
- ✓ Appropriate performance levels for assignment type (binary for Type A, 3+ levels for Types B-D)

### Must NOT Do
- ✗ Use half-points (7.5, 15.5) unless structurally necessary (like 3-level scale: 10, 5, 0)
- ✗ Create overly-detailed criteria that duplicate assignment instructions (rubric grades *how well*, instructions explain *what to do*)
- ✗ Leave performance-level descriptions blank or vague ("Good work")
- ✗ Use binary grading on Type C/D assignments (complex work deserves gradation)
- ✗ Grade on formatting as heavily as technical content (4-10% max)
- ✗ Mark rubrics as non-reusable if they could be reused on similar future assignments

### Flexible Elements
- Number of criteria (3-6 is typical)
- Specific point values (as long as distribution follows guidelines above)
- Exact wording of performance levels (customize for your context)
- Sub-criteria vs. flat structure (both work if clear)

---

## Examples

### Example 1: Type A (Simple Training, Binary)
```
Rubric: Online Training Submission
Total Points: 15
Reusable: Yes

Criterion 1: Training Completion (15 points)
  Excellent (15) — Completion screenshot submitted showing course finished
  Unacceptable (0) — No screenshot or screenshot doesn't show completion
```

### Example 2: Type B (Single IIS Lab, 3 Levels)
```
Rubric: IIS Configuration Lab
Total Points: 75
Reusable: Yes

Criterion 1: Documentation (7 points)
  Excellent (7) — Screenshots of each major step, clear explanations
  Good (5) — Most steps documented, explanations present but brief
  Unacceptable (0) — Little or no documentation

Criterion 2: IIS Installation (23 points)
  Excellent (23) — IIS installed, Web Server role enabled, default site running
  Good (15) — IIS installed with minor role/site issues
  Unacceptable (0) — IIS not installed or non-functional

Criterion 3: Custom Website (23 points)
  Excellent (23) — Website created with correct bindings, custom content deployed, functional
  Good (15) — Website created with partial bindings or content issues
  Unacceptable (0) — No website or non-functional

Criterion 4: Testing (22 points)
  Excellent (22) — Site verified as accessible locally and remotely, all features working
  Good (15) — Site accessible but with minor accessibility issues
  Unacceptable (0) — Site not accessible or major functionality broken
```

### Example 3: Type C (4-Scenario Lab, 4 Levels)
[See Performance Monitoring example above in Step 2]

### Example 4: Type D (Research Paper, 4 Levels)
[See Containers research example above in Step 2]

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-27 | Initial specification based on PRO221 audit. Four assignment types (Simple, Moderate, Complex, Research) with templates and guidelines. Performance-level descriptions, point distribution standards, reusable rubric strategy. Emphasizes graduated grading for complex work instead of binary pass/fail. |

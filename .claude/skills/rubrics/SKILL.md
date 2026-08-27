---
name: rubrics
description: Use when creating, auditing, or rebuilding Canvas rubrics for technical and research assignments in PRO221. Defines standard format, point distribution, performance levels, and reusable templates.
---

# Canvas Rubrics Playbook for PRO221

**Version:** 2.0  
**Last Updated:** 2026-08-27  
**Based on:** Established 3-level rubric standard across BIT221, BIT281, PRO221, BIT351

---

## Overview

This document defines the **canonical rubric format** for all assignments across the Information Systems curriculum. All rubrics use a consistent **3-level standard** (Excellent/Good/Unacceptable) for simplicity, consistency, and ease of grading.

**Key principle:** 3 levels apply to ALL assignment types. Simple assignments use binary (Full Credit/No Credit) only when pass/fail is the only meaningful distinction. All other assignments—regardless of complexity—use the 3-level scale with clear performance descriptions.

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

All assignments use **3 performance levels** (Excellent/Good/Unacceptable). Classify by complexity to determine number of criteria and point distribution:

### **Type A: Simple/Completion Assignments** (Exception: Binary only)
- **Examples:** Watch training video, submit screenshot, discussion post, quiz
- **Characteristics:** Pass/fail, no partial credit needed
- **Rubric:** 1 criterion, 2 levels (Full Credit or No Credit)
- **Point range:** Usually 5-15 points
- **Time to complete:** < 1 hour

### **Type B+: All Other Assignments** (3 Levels: Excellent/Good/Unacceptable)
- **Examples:** Single labs, multi-scenario labs, research papers, design documentation, analysis reports
- **Characteristics:** Any assignment where partial credit is meaningful
- **Rubric:** 3-6 criteria, 3 performance levels per criterion (Excellent, Good, Unacceptable)
- **Point range:** 15-150 points
- **Time to complete:** 1+ hours
- **Partial credit:** "Good" level captures 60-80% of criterion points; allows for partial work while maintaining clear expectations

---

## Step 2 — Rubric Structure Template by Type

### **Type A: Simple/Completion (Binary — Exception)**

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
  Full Credit (15 points) — Screenshot shows course completion
  No Credit (0 points) — Screenshot missing or doesn't show completion
```

---

### **Type B+: All Other Assignments (3 Levels — Standard)**

**ALWAYS structure with Well Formatted Document as Criterion 1:**

```
Rubric Name: [Assignment Name]
Total Points: [X]
Reusable: Yes

Criterion 1: Well Formatted Document (X points, 8-10% of total)
  Excellent (X points) — Cover page with name, course, assignment; all sections titled; all screenshots labeled
  Good (X*0.70 points) — Cover page present with minor gaps; sections mostly titled; most screenshots labeled
  Unacceptable (0 points) — Missing cover page; unclear organization; screenshots unlabeled

Criterion 2: [Major technical element or component 1] (Y points, 25-35% of total)
  Excellent (Y points) — [Full completion description]
  Good (Y*0.70 points) — [60-80% completion description]
  Unacceptable (0 points) — [Missing or failed description]

Criterion 3: [Major technical element or component 2] (Y points, 25-35% of total)
  [Same 3-level structure]

Criterion 4: [Major technical element, analysis, or verification] (Z points, 20-35% of total, optional)
  [Same 3-level structure]
```

**Example 1: Single IIS Configuration Lab (75 points)**
```
Total Points: 75
Reusable: Yes

Criterion 1: Well Formatted Document (8 points)
  Excellent (8) — Cover page with name, course, assignment; all sections titled; all screenshots labeled
  Good (6) — Cover page present with minor info missing; sections mostly titled; most screenshots labeled
  Unacceptable (0) — Missing cover page; unclear organization; screenshots unlabeled

Criterion 2: IIS Installation & Role (22 points)
  Excellent (22) — IIS installed, Web Server role configured, default website running
  Good (16) — IIS installed and role mostly configured, minor website issues
  Unacceptable (0) — IIS not installed or non-functional

Criterion 3: Website Configuration (22 points)
  Excellent (22) — Custom website created with correct bindings, custom content deployed, functional
  Good (16) — Website created with partial bindings or incomplete content
  Unacceptable (0) — No custom website or non-functional

Criterion 4: Verification & Testing (23 points)
  Excellent (23) — Site accessible locally and remotely, all features working correctly
  Good (17) — Site accessible with minor accessibility or functionality issues
  Unacceptable (0) — Site not accessible or major functionality broken
```

**Example 2: Multi-Scenario Lab - Proxmox Datacenter Manager (100 points)**
```
Total Points: 100
Reusable: Yes

Criterion 1: Well Formatted Document (10 points)
  Excellent (10) — Cover page complete; infrastructure diagram with labels; all sections titled; every screenshot captioned; troubleshooting log included
  Good (7) — Cover page present with minor gaps; diagram present but some labels missing; most sections titled; most screenshots captioned
  Unacceptable (0) — Missing cover page; no diagram; unclear organization; screenshots unlabeled

Criterion 2: PDM Deployment & Configuration (30 points)
  Excellent (30) — PDM deployed with correct specs; hostname, IP, DNS, gateway verified; updates applied; network communication verified; remotes added with proper authentication
  Good (22) — PDM deployed with minor config gaps; most verification completed; remotes added but 1-2 verification steps incomplete
  Unacceptable (0) — PDM not installed or non-functional; remotes not added; critical configuration missing

Criterion 3: Centralized Management & Operations (30 points)
  Excellent (30) — Dashboard displays combined resources; search tested and documented; custom view created with meaningful organization; lifecycle operations tested; management plane experiment completed
  Good (22) — Dashboard functional with most resources visible; search tested but sparse documentation; custom view basic; operations mostly tested; experiment partially completed
  Unacceptable (0) — Dashboard non-functional; search not tested; no custom view; operations not tested; experiment not attempted

Criterion 4: Analysis & Critical Thinking (30 points)
  Excellent (30) — Management plane questions answered with clear reasoning; comparison table complete with detailed functional differences; datacenter analysis addresses all dimensions and identifies thoughtful disadvantages
  Good (22) — Management plane questions answered with good understanding; comparison table mostly complete with some detail lacking; analysis covers most dimensions
  Unacceptable (0) — Questions not answered or inaccurate; comparison table superficial or missing; analysis missing or minimal critical thinking
```

---

## Step 3 — Performance Level Descriptions (3-Level Standard)

Use these descriptions as starting points, customizing for your specific criteria. All criteria use three levels: Excellent, Good, and Unacceptable.

**Excellent Level:**
- "All requirements met and working correctly"
- "Thorough understanding demonstrated"
- "No significant gaps or errors"
- "Clearly documented with comprehensive evidence"
- "Goes beyond basic requirements or shows exceptional depth"

**Good Level (65-80% of criterion points):**
- "Most requirements met with minor gaps"
- "Core functionality working but some refinement or edge cases missed"
- "Mostly documented, 1-2 items lack detail"
- "Demonstrates solid understanding with room for improvement"
- "Acceptable work with clear demonstration of competency"

**Unacceptable Level:**
- "Requirements not met"
- "Doesn't work or fundamentally broken"
- "Not attempted or not submitted"
- "Critical misunderstandings or missing core elements"
- "Insufficient evidence of competency in this criterion"

---

## Step 4 — Point Distribution Standards

**Type A (Simple, binary):**
- Single criterion: 100% of total points

**Type B+ (All others, 3 levels):**
- Documentation/Planning/Minor element: 4-15% of total points
- Major element 1: 20-40% of total points
- Major element 2: 20-40% of total points
- Major element 3 or Verification (optional): 15-35% of total points

**Good-level point calculation (65-75% scale):**
- For simplicity, use 70% of Excellent points for the Good level
- Example: Excellent = 20 points → Good = 14 points
- Example: Excellent = 30 points → Good = 21 points

---

## Step 5 — Reusable Rubric Strategy

### **Standard Criterion: Well Formatted Document** (Appears in most rubrics, 8-10% of total points)

**Criterion Description:** Submit a well formatted document which includes your name, course information, and assignment information on a cover page or title section. Your document must have clear sections with titles and descriptions and every screenshot must be labeled.

**Rating Descriptions:**
- **Excellent:** Document includes complete cover page with name, course code, assignment name, and date; all sections clearly titled and organized; every screenshot has descriptive caption or label
- **Good:** Cover page present but missing 1-2 pieces of info; sections mostly titled and organized with minor gaps; most screenshots labeled
- **Unacceptable:** Missing cover page or critical info; unclear section organization; screenshots not labeled or poorly labeled

---

### **Assignment Type Patterns** (all use 3 levels):

### **Single-Service Lab** (e.g., IIS, AD setup)
- Well Formatted Document (8-10%)
- Installation & Configuration (30-40%)
- Testing & Verification (25-35%)
- Optional: Advanced features or troubleshooting (15-25%)

### **Multi-Scenario Lab** (e.g., Proxmox, Performance Monitoring)
- Well Formatted Document (10%)
- Scenario/Component 1 (25-30%)
- Scenario/Component 2 (25-30%)
- Scenario/Component 3 or Analysis (25-35%)

### **Infrastructure/Clustering Labs** (IaC, HA, Clustering)
- Well Formatted Document (10%)
- Installation/Deployment (25-30%)
- Configuration (30-35%)
- Testing/Failover Verification (25-30%)

### **Research Papers** (Containers, architecture, analysis)
- Well Formatted Document (10%)
- Content Depth & Accuracy (25-35%)
- Organization & Clarity (20-25%)
- Critical Analysis & Insight (25-35%)

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
- ✓ **All rubrics use 3 levels** (Excellent/Good/Unacceptable) except Type A (binary)
- ✓ **"Well Formatted Document" is ALWAYS Criterion 1** (unless the assignment is Type A binary)
- ✓ Clear performance-level descriptions (not just level names — explain what "Excellent" looks like)
- ✓ Point values that sum exactly to the assignment's total points
- ✓ Rubric marked "Reusable: Yes" (assignments with identical expectations can share rubrics)
- ✓ Alignment with assignment's Criteria for Success box
- ✓ Good level at 65-75% of Excellent points (enables 60-80% partial credit)

### Must NOT Do
- ✗ Use 4 or more performance levels (3-level standard is binding)
- ✗ Use 4-level templates or "Satisfactory" level (removed in v2.0)
- ✗ Create overly-detailed criteria that duplicate assignment instructions (rubric grades *how well*, instructions explain *what to do*)
- ✗ Leave performance-level descriptions blank or vague ("Good work" is not specific enough)
- ✗ Grade on formatting as heavily as technical content (4-10% max unless assignment emphasizes it)
- ✗ Mark rubrics as non-reusable if similar assignments could use them
- ✗ Use half-points unless unavoidable (10, 7, 0 is cleaner than 10, 6.5, 0)

### Flexible Elements
- Number of criteria (3-5 is typical; 6 maximum)
- Specific point values and percentages (follow distribution guidelines but adapt to context)
- Exact wording of performance levels (customize for technical accuracy and clarity)
- Whether to break criteria into sub-criteria or keep them flat (both work if clear)

---

## Examples

### Example 1: Type A (Simple Training, Binary — Exception)
```
Rubric: LinkedIn Learning Training Submission
Total Points: 10
Reusable: Yes

Criterion 1: Training Completion (10 points)
  Full Credit (10) — Completion certificate or screenshot submitted showing course finished
  No Credit (0) — No certificate/screenshot or doesn't show completion
```

### Example 2: Type B+ (Research Paper, 3 Levels)
```
Rubric: "What Are Containers?" Research Paper
Total Points: 50
Reusable: Yes

Criterion 1: Well Formatted Document (5 points)
  Excellent (5) — Title page with name, course, assignment; clear sections with titles; professional formatting
  Good (3) — Title page present but incomplete; sections mostly clear; minor formatting issues
  Unacceptable (0) — Missing title page; unclear organization; poor formatting

Criterion 2: Content Depth & Accuracy (15 points)
  Excellent (15) — Covers isolation, images, registries, orchestration with accurate technical detail
  Good (11) — Covers most topics; minor accuracy or depth issues
  Unacceptable (0) — Incomplete or inaccurate treatment

Criterion 3: Organization & Clarity (15 points)
  Excellent (15) — Logical structure, clear paragraphs, flows naturally from topic to topic
  Good (11) — Mostly organized; some transitions could be smoother
  Unacceptable (0) — Confusing structure, hard to follow

Criterion 4: Critical Analysis & Insight (15 points)
  Excellent (15) — Analyzes when containers are useful, compares to alternatives, identifies trade-offs
  Good (11) — Good analysis of container benefits and use cases
  Unacceptable (0) — Mostly descriptive with no analysis
```

### Example 3: Type B+ (Single Lab, 3 Levels) — See Step 2 Example 1 above

### Example 4: Type B+ (Multi-Scenario Lab, 3 Levels) — See Step 2 Example 2 above

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-08-27 | **BREAKING CHANGE:** Standardized on 3-level rubric format (Excellent/Good/Unacceptable) for ALL assignment types except Type A (binary). Removed 4-level variants and "Satisfactory" level. Consolidated Type C and D into single Type B+ template. Simplified point distribution to 65-75% scale for "Good" level. Updated examples and reusable patterns. Type A remains binary (Full Credit/No Credit) for pass/fail assignments only. |
| 1.0 | 2026-07-27 | Initial specification based on PRO221 audit. Four assignment types (Simple, Moderate, Complex, Research) with templates and guidelines. Introduced variable level counts (2/3/4) based on complexity. |

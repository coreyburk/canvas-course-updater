---
name: course-structure-pages
description: Standard formats for Course Outline (instructor), Instructor Notes (5 weeks), and Student Resource Pages by topic. Based on BIT281/BIT221/PRO221 models.
---

# Course Structure Pages — Standard Formats

## Module Organization (BIT281 Model)

**Module 1 (Position 1): Instructor-Only Module**
- **Name:** "Course Outline and Lecture Notes (Not Published - Instructor Use Only)"
- **Published:** NO
- **Contents:**
  - 1 Course Outline page (unpublished)
  - 5 Instructor Notes pages (one per week, unpublished)
  - Optional: other instructor resources

**Modules 2-6+ (Positions 2+): Weekly Student Modules**
- **Name:** "Week N: [Topic]"
- **Published:** YES
- **Contents:**
  - Subheader: "Resources" (if topic pages exist)
  - 1-3 Student Resource Pages (by topic)
  - Subheader: "Assignments"
  - Lab assignments
  - Subheader: "Training"
  - LinkedIn Learning links or readings
  - Subheader: "Quiz"
  - Weekly quiz

---

## Page Type 1: Course Outline (Instructor-Only)

**Purpose:** Overview of the entire course for instructor reference. Not published; not student-facing.

**Format:**
- Single page summarizing:
  - Course learning outcomes (4-5 outcomes)
  - 5-week breakdown: topics, key assignments, learning focus per week
  - Assessment model: point totals, grading breakdown, weights
  - Key resources and infrastructure requirements
  - Cross-week dependencies and scaffolding strategy

**Visual Template:** BIT221 standard (no fancy styling required; plain, readable)

**Naming:** `[code]-course-outline` (e.g., `bit320-course-outline`)

**Publishing Status:** Unpublished

---

## Page Type 2: Instructor Notes (Per Week)

**Purpose:** Teaching context, student misconceptions, setup guidance, cross-week connections. For instructor reference only.

**One page per week. Format:**

### Week N — [Topic]

**Learning Objectives:**
- [Objective 1]
- [Objective 2]
- etc.

**Key Teaching Points:**
- [Concept 1: 2-3 sentence explanation]
- [Concept 2: 2-3 sentence explanation]
- etc.

**Common Student Misconceptions:**
- [Misconception 1 → Correction]
- [Misconception 2 → Correction]
- etc.

**Lab Setup & Scaffolding:**
- Prerequisites from prior weeks
- Infrastructure needed (VMs, WSL2, credentials, etc.)
- Expected time per assignment
- Common failure points and how to troubleshoot

**Cross-Week Connections:**
- How this week builds on prior weeks
- How this week scaffolds to future weeks
- Real-world relevance

**Resources:**
- LinkedIn Learning links relevant to this week
- Key documentation
- Common error solutions

**Depth Standard Applied:**
- Dependencies and Interactions section (how this topic connects to infrastructure, security, other systems)
- Security Considerations section (risks, mitigations, compliance)
- Modern Context section (what's changed, current best practices)

**Visual Template:** v4.0 canonical (left-border headers, plain lists, minimal color)

**Naming:** `lecture-notes-week-[N]-[topic]` (e.g., `lecture-notes-week-1-log-analysis-fundamentals`)

**Publishing Status:** Unpublished

---

## Page Type 3: Student Resource Pages (By Topic)

**Purpose:** Concepts, examples, troubleshooting, real-world context for students. Supports assignments and training.

**One or more per week, organized by topic. Format:**

### [Topic Name]

**Why This Matters:**
- 1-2 paragraph real-world context explaining when/why students will use this skill
- Connection to prior and future weeks

**Core Concepts:**
- [Concept 1: definition, explanation, visual diagram if needed]
- [Concept 2: definition, explanation]
- etc.

**Examples & Practice:**
- Code samples with expected output
- Walkthrough of a realistic scenario
- Step-by-step procedures where applicable

**Common Pitfalls & Troubleshooting:**
- [Error 1: what it means, how to fix it]
- [Error 2: what it means, how to fix it]
- etc.

**Dependencies and Interactions:**
- How this topic connects to related infrastructure
- Prerequisites needed
- Impact if this is done incorrectly

**Security Considerations:**
- Risks or vulnerabilities related to this topic
- Best practices for secure implementation
- Common mistakes that compromise security

**Real-World Context:**
- How this is used in production infrastructure
- Tools and practices in industry
- What changes vs. what stays the same

**Resources:**
- LinkedIn Learning links
- Documentation references
- Lab connections (which assignments use this)

**Visual Template:** v4.0 canonical (left-border headers, plain lists, code blocks with expected output, minimal color)

**Naming Convention:** `week-[N]-[topic]` (e.g., `week-1-log-analysis-fundamentals`, `week-2-bash-text-processing`)

**Publishing Status:** Published

---

## Implementation Checklist

- [ ] Course Outline page created (unpublished, position 1 module)
- [ ] Week 1 Instructor Notes page created (unpublished)
- [ ] Week 2 Instructor Notes page created (unpublished)
- [ ] Week 3 Instructor Notes page created (unpublished)
- [ ] Week 4 Instructor Notes page created (unpublished)
- [ ] Week 5 Instructor Notes page created (unpublished)
- [ ] 1-3 Student Resource Pages per week created (published)
- [ ] All pages follow v4.0 canonical visual template
- [ ] All pages include Dependencies/Security/Modern Context sections
- [ ] All pages wired into appropriate modules
- [ ] Instructor-only module at position 1, marked unpublished

---

## Examples

**BIT281 Structure (Reference):**
- Module 1: "Course Outline and Lecture Notes" (unpublished, 28 items)
  - Course Outline (unpublished)
  - 21 Lecture Notes pages (one per week, unpublished)
- Modules 2-6: Weekly modules (published, 10-15 items each)
  - Subheader: Resources
  - 2-3 Resource pages per week (published)
  - Subheader: Assignments
  - Subheader: Training
  - Subheader: Quiz

**BIT221 Structure (Reference):**
- Similar to BIT281
- 13 resource pages total (Weeks 1-5)
- All follow v4.0 visual template

**PRO221 Structure (Reference):**
- Module 1: Instructor module (unpublished)
  - Course Outline (unpublished)
  - 5 Instructor Notes pages (unpublished)
- Modules 2+: Weekly modules (published)
  - Resource pages per week
  - Assignments
  - Training
  - Quizzes

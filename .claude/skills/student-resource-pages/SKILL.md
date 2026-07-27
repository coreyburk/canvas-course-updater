# Skill: student-resource-pages

**Trigger:** When building Canvas course pages for student-facing lecture, reference, or concept documentation (published pages in weekly course modules)

**Scope:**
- Create polished, focused reference pages for student learning and assignment support
- Output: Published pages in student course modules (Week 1, Week 2, etc.)
- Audience: Students (instructors can access, but student comprehension is primary)
- NOT for: Instructor prep, troubleshooting guides, grading rubrics, facilitation notes

**Naming convention:**
`Week [N] | Page [#] - [Topic]`

**Module placement:**
- Published in course module (positions 2 onward)
- Never in instructor-only module
- Always indexed in course module structure

---

## Mandatory Sections

### 1. Learning Objectives (150-200 words)
- 4-8 objectives using checkmark card-grid format (not bullet lists)
- Each objective is a single, clear outcome: "students will be able to..."
- Specific to this page's topic, not the entire week
- Example: "Define Infrastructure as Code and explain why it replaces manual configuration at scale"

### 2. Core Concepts / Why This Matters (700-900 words)
- Grounded in student context: why does this matter to their role/career?
- 3-5 key concepts, each with concrete examples
- Use analogies students understand (relate to prior weeks or real-world scenarios they know)
- Include a "big picture" section explaining how this fits into the broader course
- Avoid jargon without definition
- Every concept supported by a real example (not hypothetical)

### 3. Applied / Technical (800-1200 words)
- Step-by-step procedures with actual commands, UI paths, real syntax
- Never use placeholders like `<server>` or `[example]` without a concrete instance nearby
- Include expected output (what the screen/console should show on success)
- Multiple examples: simple one first, then a more complex variant
- Code blocks in `<pre style="white-space: pre-wrap;">` with literal blank lines, not styled spacers
- Tables with real data, not example placeholders

### 4. Dependencies & Interactions (200-300 words)
- What must be true for this concept to work?
- What from prior weeks does this build on?
- What could go wrong if dependencies aren't met?
- Example: "Pushing a configuration to a remote node depends on PowerShell remoting already working"

### 5. Security Considerations (300-400 words)
- Framed as "understand this risk" not "how to exploit this"
- Connect to real-world threats (data exposure, lateral movement, persistence)
- Practical mitigations students can apply (encryption, access control, auditing)
- Avoid scaremongering; be specific about threat models
- Example: "DSC push mode rides on the same remoting channel that lateral movement attacks use"

### 6. Reference Links (3-6 curated resources)
- Microsoft Learn, official docs, MITRE ATT&CK (where relevant)
- Link cards in 2-column grid, each 50-80 characters max
- Only links that add significant value; don't pad with marginal resources

---

## Optional Sections

### In-Class Discussion Questions (3-5 questions)
- Numbered list format (not cards)
- Open-ended, encourages critical thinking
- Should be answerable from this page + prior knowledge
- Designed for 5-10 minute in-class discussion

### What's Current (50-100 words)
- Timestamp when written (e.g., "As of Windows Server 2025...")
- Note if content applies to older/newer versions
- Example: "The WindowsFeature resource taught here is fully supported in Windows Server 2016-2025"

---

## Content Standards

**Length:** 1500-2000 words total (tight, focused, student-readable)

**Audience lens:** Student preparing for assignment, lab, or certification. Not instructor prepping to teach. Not grader looking for rubric.

**Examples:** 
- All from student context (assignments, labs, real infrastructure)
- All real data, never fabricated
- All executable by students (use their tools, their access level)

**What NOT to include:**
- Teaching Agenda (instructor only)
- "Why Students Struggle" / common misconceptions (instructor prep)
- Expected output values for grading purposes
- Troubleshooting decision trees (too instructor-focused for students)
- Grading rubrics, rubric alignment, or success criteria (separate from learning content)
- Instructor facilitation notes

**Visual standards (per BIT221 canonical):**
- No em dashes (use space-hyphen-space)
- No inline SVG (upload as image if needed)
- No `<style>` tags in head (inline styles only)
- `<strong>` for bold (not font-weight)
- Learning Objectives in checkmark card-grid (2 columns)
- Tables: 1px solid borders on all cells, alternating row backgrounds
- Code blocks: `<pre style="white-space: pre-wrap;">` with literal blank lines

**Security framing:**
- "This capability can be used by attackers for [threat]" ✅
- "Here's how to exploit this" ❌
- "Understanding this risk helps you recognize..." ✅
- "Here's a step-by-step attack walkthrough" ❌

---

## Workflow

**Step 1:** Extract learning objectives from assignment, student context, and prior week content  
**Step 2:** Draft core concepts with student-level examples (avoid instructor-only depth)  
**Step 3:** Build applied/technical section from actual CLI/UI outputs (run it yourself)  
**Step 4:** Add dependencies and security (student-aware framing)  
**Step 5:** Curate reference links; remove marginal resources  
**Step 6:** Publish in student course module (not instructor module)  

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-07-27 | Initial skill definition — student-facing resource pages distinct from instructor teaching notes. Focus on student learning, not instructor prep. Mandatory sections: Learning Objectives, Core Concepts, Applied/Technical, Dependencies, Security, References. Optional: Discussion Questions, What's Current. |
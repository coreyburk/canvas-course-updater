# Training Assignment Playbook
**Version:** 1.0  
**Created:** 2026-09-18  
**Template Source:** ITH216 "Online Training 8A: Wireless Networking Essential Training" (assignment 40329330)  
**Status:** LIVE — Use for all LinkedIn Learning training assignments

---

## Overview

Training assignments bridge LinkedIn Learning videos to course learning objectives. They standardize:
- Purpose and learning context
- Video course selection and duration
- Deliverable requirements (proof of completion)
- Grading criteria

**Key Principle:** One video = one training assignment. Video duration typically 1-2 hours. Assignment points: 80-100 (significant but not labor-intensive).

---

## Template Structure (Fixed Order)

### 1. Purpose Box (Blue — #eaf4fb / #2980b9)

**HTML:**
```html
<table style="background-color: #eaf4fb; width: 100%; border-collapse: collapse; border: 2px solid #2980b9;">
    <tbody>
        <tr>
            <td style="padding: 20px;">
                <h3 style="color: #1a5276; margin-top: 0;">Purpose</h3>
                <p>[Real-world context: why this topic matters to the course/career]</p>
                <p><strong>Course Learning Outcomes:</strong></p>
                <ul>
                    <li>[CLO 1]</li>
                    <li>[CLO 2]</li>
                    <li>[CLO 3]</li>
                </ul>
                <p><strong>Program Outcomes:</strong></p>
                <ul>
                    <li>[PO 1]</li>
                    <li>[PO 2]</li>
                    <li>[PO 3]</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
```

**Rules:**
- **Background:** #eaf4fb (light blue)
- **Border:** 2px solid #2980b9 (blue)
- **Padding:** 20px
- **Header h3:** color #1a5276, margin-top 0
- **Purpose paragraph:** Real-world relevance (2-3 sentences)
- **CLOs:** 3 bullet points explaining course-level learning outcomes
- **POs:** 3 bullet points from program outcomes (source from Canvas course)
- **No point values** in this section

---

### 2. Task Box (Yellow — #fef9e7 / #d4ac0d)

**HTML:**
```html
<table style="background-color: #fef9e7; width: 100%; border-collapse: collapse; margin-top: 15px; border: 2px solid #d4ac0d;">
    <tbody>
        <tr>
            <td style="padding: 20px;">
                <h3 style="color: #9a7d0a; margin-top: 0;">Task</h3>
                <p>Complete the "[Video Course Title]" course ([X] hours, [Y] minutes) from LinkedIn Learning, covering [brief topics], and submit a screenshot demonstrating completion.</p>
            </td>
        </tr>
    </tbody>
</table>
```

**Rules:**
- **Background:** #fef9e7 (light yellow)
- **Border:** 2px solid #d4ac0d (yellow-brown)
- **Padding:** 20px
- **Margin-top:** 15px (space from Purpose box)
- **Header h3:** color #9a7d0a, margin-top 0
- **Task paragraph:** ONE sentence stating video title, duration, brief topics, and deliverable (screenshot)
- **Keep it concise** — this is the "what" not the "how"

---

### 3. Learning Objectives (Plain h3, Bullet List)

**HTML:**
```html
<h3 style="color: #2c2c2a; margin-top: 20px;">Learning Objectives</h3>
<ul>
    <li>[Objective 1]</li>
    <li>[Objective 2]</li>
    <li>[Objective 3]</li>
    <li>[Objective 4]</li>
    <li>[Objective 5]</li>
</ul>
```

**Rules:**
- **h3 color:** #2c2c2a (dark gray)
- **Margin-top:** 20px
- **Objectives:** 4-5 bullets, specific to video content
- **Format:** "Understand [topic]", "Analyze [concept]", "Apply [skill]"

---

### 4. Training Content Overview (Plain paragraph, no styling)

**HTML:**
```html
<h3 style="color: #2c2c2a;">Training Content Overview</h3>
<p>[1-2 sentences describing what the course covers, topics included, scope]</p>
```

**Rules:**
- **h3 color:** #2c2c2a (dark gray)
- **Content:** Describe breadth of topics, course structure, key learning areas
- **Length:** 1-2 sentences max
- **Purpose:** Gives students sense of what they'll learn before clicking the link

---

### 5. Training Course (Link + Topic Breakdown)

**HTML:**
```html
<h3 style="color: #2c2c2a;">Training Course</h3>
<ul>
    <li><a class="inline_disabled" href="[LinkedIn Learning URL]" target="_blank">[Course Title]</a> ([X] hours, [Y] minutes)
        <ul>
            <li>[Topic 1 covered in course]</li>
            <li>[Topic 2 covered in course]</li>
            <li>[Topic 3 covered in course]</li>
            <li>[Topic 4 covered in course]</li>
            <li>[Topic 5 covered in course]</li>
            <li>[Topic 6 covered in course]</li>
            <li>[Topic 7 covered in course]</li>
        </ul>
    </li>
</ul>
```

**Rules:**
- **h3 color:** #2c2c2a
- **Link:** Full LinkedIn Learning course URL
- **Link class:** `class="inline_disabled"` (Canvas style)
- **Link target:** `target="_blank"` (opens in new window)
- **Duration:** Include in parentheses after course title
- **Subtopics:** 6-7 bullet points of major topics covered
- **Nested list:** Use `<ul><li>` for topic hierarchy

---

### 6. Deliverables (Plain h3 + bullet list)

**HTML:**
```html
<h3 style="color: #2c2c2a;">Deliverables</h3>
<ul>
    <li>Screenshot showing LinkedIn Learning course completion status for "[Course Title]"</li>
    <li>Screenshot must clearly display:
        <ul>
            <li>Course title visible in browser or LinkedIn interface</li>
            <li>Progress indicator showing 100% completion or completion checkmark</li>
            <li>Your name or account information (partially visible is acceptable)</li>
        </ul>
    </li>
    <li>Image must be clear and readable (minimum 800x600 resolution recommended)</li>
</ul>
```

**Rules:**
- **h3 color:** #2c2c2a
- **Deliverables:** Always a screenshot of LinkedIn Learning completion
- **Screenshot requirements:** Specify what must be visible (title, progress, account info)
- **Image quality:** Minimum resolution guidance (800x600)
- **Nested requirements:** Use nested `<ul>` for detailed screenshot specs

---

### 7. Criteria for Success Box (Green — #eafaf1 / #27ae60)

**HTML:**
```html
<table style="background-color: #eafaf1; width: 100%; border-collapse: collapse; margin-top: 15px; border: 2px solid #27ae60;">
    <tbody>
        <tr>
            <td style="padding: 20px;">
                <h3 style="color: #1e8449; margin-top: 0;">Criteria for Success</h3>
                <p>Your submission will be evaluated on the following:</p>
                <ul>
                    <li>[Criterion 1]</li>
                    <li>[Criterion 2]</li>
                    <li>[Criterion 3]</li>
                    <li>[Criterion 4]</li>
                    <li>[Criterion 5]</li>
                    <li>[Criterion 6]</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
```

**Rules:**
- **Background:** #eafaf1 (light green)
- **Border:** 2px solid #27ae60 (green)
- **Padding:** 20px
- **Margin-top:** 15px
- **Header h3:** color #1e8449, margin-top 0
- **Intro sentence:** "Your submission will be evaluated on the following:"
- **Criteria:** 5-6 bullet points (specific, measurable)
- **No point values inside this box** (points appear in Canvas assignment settings, not HTML)
- **Format:** "Training module is fully completed...", "Screenshot clearly shows...", etc.

---

## Assignment Properties (Canvas Settings)

**All training assignments should use:**
- **Points Possible:** 80 (or 100 if significant effort, but 80 typical)
- **Submission Type:** Online upload (screenshot)
- **Due Date:** End of assigned week (usually Thursday 11:59 PM UTC)
- **Published:** False (unpublished until reviewed by instructor)

---

## Quick Checklist

- [ ] Purpose box: Real-world context + 3 CLOs + 3 POs
- [ ] Task box: One sentence with course title, duration, topics, deliverable
- [ ] Learning Objectives: 4-5 specific, measurable objectives
- [ ] Training Content Overview: 1-2 sentences on course scope
- [ ] Training Course: Linked video + 6-7 topic bullets
- [ ] Deliverables: Screenshot specs with quality requirements
- [ ] Criteria for Success: 5-6 measurable criteria (no points in box)
- [ ] No em dashes (use space-hyphen-space)
- [ ] All colors inline (no `<style>` tags)
- [ ] Links use `class="inline_disabled"` and `target="_blank"`

---

## Example Use Cases

**Week 1 BIT360:** IT Risk Management Essential Training (1h 38m) → Assignment "Week 1: Training 1A - Risk Management Fundamentals"

**Week 2 BIT360:** Business Impact Analysis course (TBD, ~1.5h) → Assignment "Week 2: Training 2A - Business Impact Analysis"

**Week 8 ITH216:** Wireless Networking Essential Training (1h 9m) → Assignment "Week 8: Online Training 8A - Wireless Networking Essential Training" ✅ (live example)

---

## Notes for Instructors

- **Timing:** Each training assignment typically takes 1h 40m - 2h 30m (video + screenshot time)
- **Reusability:** Once created, these assignments carry across course iterations (update due dates only)
- **LinkedIn Learning Dependency:** Assumes Neumont institutional subscription
- **Grading:** Usually straightforward (completion = 80-100 pts; no completion = 0 pts). Consider 10-20 pt deduction for unclear/low-quality screenshots
- **Backup Plan:** If LinkedIn Learning becomes unavailable, PDFs/recordings of courses can substitute (update HTML with new link)

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-09-18 | **Initial release.** Template based on ITH216 Assignment 40329330 (Wireless Networking Essential Training). Fixed structure: Purpose (CLO/PO) → Task → Learning Objectives → Overview → Course Link → Deliverables → Criteria. All colors inline, no em dashes. Requires screenshot proof of completion + measurable criteria. |


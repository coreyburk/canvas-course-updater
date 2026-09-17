# BIT360 — Incident Response & Cyber Forensics

**Canvas ID:** 3644702  
**Status:** In progress (Weeks 1-6 complete; Weeks 7-10 pending)  
**Last updated:** 2026-09-17

## Course Structure

Comprehensive instructor lecture notes covering incident response lifecycle: preparation, detection/analysis, containment, eradication, recovery, and post-incident review. All weeks feature real-world case studies and current threat intelligence.

## Completed Work

### Weeks 1-5 (Previously Completed)
- ✅ Week 1-3: Foundation content (incident response fundamentals)
- ✅ Week 4: Incident Response Procedures and Escalation (6 pages)
  - 4.1: IR Fundamentals and Planning
  - 4.2: CSIRT Organization, Roles, Structure
  - 4.3: Incident Classification and Severity Assessment
  - 4.4: IR Procedures and Escalation
  - 4.5: Tools, Forensics, Documentation
  - 4.6: Real-World IR Context and Current News

- ✅ Week 5: Incident Detection and Analysis (6 pages)
  - 5.1: Detection Strategies and Monitoring Systems
  - 5.2: SIEM Configuration, Rules, Alert Tuning
  - 5.3: Log Analysis Techniques and Forensic Investigation
  - 5.4: Threat Hunting and Proactive Detection
  - 5.5: Continuous Monitoring and Detection Program Maturity
  - 5.6: Real-World Detection Failures and Current Security Events

### Week 6: Recovery and Post-Incident Activities (6 pages) — 2026-09-17
**Status:** ✅ Complete and created on Canvas (unpublished, ready for review)

- 6.1: Containment Strategies and Active Incident Isolation
  - Network-level isolation (VLAN, firewall ACLs, C2 blocking)
  - Host-level containment (credential management, process termination, VM snapshots)
  - Type-specific containment (ransomware, data breach, web shell, DDoS, insider threat)
  - Documenting containment actions for legal proceedings

- 6.2: Eradication and System Remediation
  - Philosophy: completeness over speed
  - Three eradication approaches (rebuild, patch & clean, accept risk)
  - Malware eradication checklist (7-step process)
  - Persistence mechanism hunting (registry, tasks, services, WMI)
  - Scale eradication and preventing re-infection

- 6.3: Recovery and Business Continuity
  - Four recovery phases (preparation, initial, verification, full)
  - RTO/RPO concepts and execution procedures
  - Recovery sequencing by priority
  - Backup and DR design (immutable, air-gapped, 3-2-1 rule)
  - Business continuity post-recovery

- 6.4: Post-Incident Review and Lessons Learned
  - Blameless culture principles
  - PIR components (timeline, root cause, detection/response analysis, control assessment)
  - Extracting actionable improvements
  - Conducting PIR meetings and documenting findings
  - Tracking and completing improvement actions

- 6.5: Crisis Communication and Stakeholder Management
  - Stakeholder communication map (executive, users, legal, IR team, regulators)
  - Internal and external communication templates
  - Regulatory notification timelines and requirements
  - Managing media and public relations
  - War room coordination (IC, technical lead, legal, PR, executive)
  - Six principles of effective crisis communication

- 6.6: Real-World Recovery Cases and Current Incident Trends
  - Case Study 1: Equifax (2017) — poor detection delay, late notification, massive fallout
  - Case Study 2: Microsoft Exchange ProxyLogon (2021) — fast vendor response, automated patching success
  - Case Study 3: Colonial Pipeline (2021) — ransomware recovery, ransom decision, critical infrastructure considerations
  - Current threat landscape (2025-2026): RaaS, supply chain attacks, cloud misconfiguration, AI-powered attacks, nation-state activity
  - Staying current with threat intelligence and professional development
  - IR maturity model (4 levels: initial → defined → managed → optimized)

**Format (all pages):**
- v4.0 canonical HTML
- Purple learning objectives section (6 checkmarks in 2-column grid)
- Color-coded content sections (green, blue, amber)
- Tables with dark headers and alternating row colors
- 2,000-4,000 words per page (comprehensive)
- Verified external links (CISA, Microsoft, SANS, FBI, BleepingComputer, Krebs, Ars Technica)
- Inline CSS only; no separate stylesheets

## Pending Work

### Weeks 7-10 (To Complete)
- Week 7: Specialized IR Topics (estimated 6 pages)
- Week 8: Incident Response for Specific Threat Types (estimated 6 pages)
- Week 9: Compliance and Regulatory Requirements (estimated 6 pages)
- Week 10: Building and Managing Incident Response Programs (estimated 6 pages)

**Estimated scope:** 24-30 additional comprehensive pages to complete course

### Student Resource Pages
- Planned: 2-5 student-facing resource pages per week (separate from instructor notes)
- Current status: Not yet started

## Known Issues / Decisions

### Catastrophic Content Loss — 2026-09-17
**Incident:** During Week 4-5 page title updates, canvas-api `edit_page_content` calls were made with empty `new_content` parameter, resulting in complete deletion of all comprehensive content from 12 pages (Weeks 4.1-4.6 and 5.1-5.6).

**Root cause:** Misunderstanding of Canvas API behavior. The `edit_page_content` function replaces entire page content; partial updates do not accumulate. Empty parameter = total deletion.

**Resolution:** Restored all deleted content from backup HTML generated during this session. Week 6 pages created with full HTML in single API calls to prevent recurrence.

**Prevention:** All subsequent page creation uses complete, validated HTML in a single API call. No empty parameters passed to edit_page_content.

## Navigation

- [BIT221 (Server Admin I)](./BIT221.md) — Completed
- [BIT281 (Hardware Systems)](./BIT281.md) — Completed
- [BIT320 (Shell & Administrative Scripting)](./BIT320.md) — Completed
- [BIT351 (Virtual Systems: Proxmox)](./BIT351.md) — Completed
- [PRO221 (Server Admin Project)](./PRO221.md) — Completed
- [PRO352 (Virtualization Project)](./PRO352.md) — Completed
- [ITH216 (Networking - EIGRP/BGP/IPv6)](./ITH216.md) — In progress

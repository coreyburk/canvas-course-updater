# BIT360 Week 1 Evaluation Report and Remediation Plan

**Course:** BIT360 (Canvas ID 3644702)
**Evaluated:** 2026-10-07 against live Canvas content (module "Week 1", ID 10042419, published)
**Standards used:** assignment-template-rebuild, rubrics v3.1, student-resource-pages v1.1, canvas-html-lint rules, CLAUDE.md non-negotiables
**Scope:** read-only evaluation. Nothing in Canvas was changed.

---

## 1. Bottom line

Week 1 content is internally misaligned. The three new student guides and the training assignment were written for assignments that do not exist in Canvas (a "1B threat model and risk matrix", a "1A simulated infected system"). The real Week 1 work is Sysinternals tools on the student's own laptop (1A) and a Hyper-V / four-VM build on server blades (1B). The guides teach VirtualBox and ACIO threat modeling; the assignments need Sysmon, ProcDump/WinDbg, Hyper-V, VLANs, OPNsense/FortiGate, AD DS and iSCSI.

Per "Canvas is the source of truth", the pages and training get fixed to match the assignments, not the reverse. The assignments themselves also fail the template, and their rubrics disagree with their point values.

**Time-critical:** 1A is due 2026-10-10 (3 days) and is the assignment the guides support worst.

---

## 2. Inventory

| Type | Item | ID / slug | Pts | Due | Published |
|---|---|---|---|---|---|
| Assignment | 1A - SysInternals | 40244730 | 100 | 2026-10-10 | Yes |
| Assignment | 1B - Install and Configure Hyper-V and 4 Virtual Servers | 40244731 | 100 | 2026-10-24 | Yes |
| Assignment | NSA CodeBreaker Challenge - Extra Credit | 40244748 | 0 | 2026-10-30 | Yes |
| Assignment | Network and Firewall Installation and Configuration | 40244749 | 0 | none | Yes |
| Assignment | Participation: Week 1 | 40244750 | 10 | none | Yes |
| Training | Week 1: Training 1A - Risk Management Fundamentals | 40349945 | 80 | none | Yes |
| Reading | Reading: Module 1 | 40244761 | 0 | none | Yes |
| Quiz | Quiz: Module 1 | 9340591 | unknown | unknown | Yes |
| Page | Week 1.1 Student Guide: InfoSec Fundamentals & Risk Assessment | ...-risk-assessment-2 | - | - | Yes |
| Page | Week 1.2 Student Guide: SysInternals Tools Hands-On | ...-hands-on-2 | - | - | Yes |
| Page | Week 1.3 Student Guide: Lab Environment Setup | ...-environment-setup-2 | - | - | Yes |
| Page | ProcDump and WinDbg | procdump-and-windbg | - | - | Yes |
| Page | Monitoring Network Activity Using TCPView | monitoring-network-activity-using-tcpview | - | - | Yes |
| Page | InfoSec Overview | infosec-overview | - | - | Yes |

**Not evaluated:** the quiz. The Canvas API exposes quiz titles only, so questions, points and alignment need a manual look in the UI (see Open Items).

---

## 3. Findings by category

### 3.1 Cross-cutting alignment (highest severity)

| # | Finding | Evidence |
|---|---|---|
| A1 | Guides and training reference assignments that do not exist | 1.1 says "assignment 1B ... threat model and risk matrix"; training 1A says "Week 1B assignment". Live 1B is the Hyper-V build. |
| A2 | 1.2 describes 1A as "analyze a simulated infected system" using three tools | Live 1A has four tasks (Sysmon, TCPView, Process Explorer with VirusTotal, ProcDump crash dump) run on the student's own laptop, plus an optional PowerShell task. Sysmon is not covered by the guide beyond a log-table row. ProcDump/WinDbg is not covered. |
| A3 | 1.3 teaches a VirtualBox lab on a laptop | Live 1B uses assigned server blades, a VLAN on the IS Server Room switches, DBAN/GParted wipe, Windows Server 2025 bare metal, Hyper-V role, virtual switches, firewall VM, 2 DCs, file server, live migration, replication, SAN/LUN masking. None of that is taught. |
| A4 | Nothing teaches Week 1 hands-on topics the assignments require | Missing: VLAN and switch config, bare-metal install, Hyper-V virtual switches, AD DS/DNS/NTP, OPNsense or FortiGate setup, iSCSI/NFS to SAN, live migration and replication. |
| A5 | `courses/BIT360-2026.md` and CLAUDE.md describe the course as Incident Response and Cyber Forensics, but live Week 1 (and Week 3-4 titles: Hyper-V migration, Veeam) is a Server Admin / DR build course | Doc must be reconciled with Canvas, not the reverse. |
| A6 | "-2" slug suffix on all three guides | Suggests earlier duplicates existed. Confirm no orphan duplicates remain (`list_pages`). |

### 3.2 Assignments

**1A - SysInternals (100 pts)**
- No Purpose, Task or Criteria for Success boxes. Fails the three-box template entirely.
- Deliverables section exists but is plain prose mixed with task blocks; no Criteria box as the final element.
- Rubric (Sysinternals Rubric, 125 pts) does not match the 100-pt assignment: 4 + 24 + 24 + 24 + 24 = 100 plus a 25-pt extra credit task. Acceptable only if extra credit is intentional; it should be stated. Well Formatted Document is 4 pts (3.2%), below the 15-20% standard.
- Rubric uses 2 levels (Full Marks / No Marks). Standard is Excellent / Good / Unacceptable at roughly 70% for Good.
- Task 4 says "crashing application (e.g., Chrome)"; the published ProcDump page uses Notepad. Pick one and align.
- Contains `&nbsp;` spacer paragraphs and stray empty `<strong>` tags. Third-party links (Medium.com, PCWorld, Windows Central) should be verified.
- No Course Learning Outcomes or Program Outcomes.

**1B - Hyper-V and 4 VMs (100 pts)**
- No Purpose, Task or Criteria boxes. Deliverables section is present but the rubric criteria are not mirrored in a Criteria box.
- Content defects that will mislead students:
  - FS01 uses a hard-coded `192.168.113.12` and gateway `192.168.113.1`; every other address uses `[Your VLAN]`.
  - Domain name line reads `[first initial[[last name][.ninjas]` (bracket typo).
  - NTP: `pool.ntp.org` in one place, `pool.ntp.com` in another.
  - The Windows Server 2025 install bullet links a file titled `VMware-VMvisor-Installer-6.5.0...iso` (stale VMware reference in a Hyper-V course).
  - "Name: [first initial][last name]-hv[##]" is used for physical hosts, then "FW01" in the rubric versus `-fw` in the instructions.
  - Deliverables ask for screenshots of "Hyper-V Manager" and "Installation and Configuration of each VM" but never mention live migration, replication or the SAN/LUN-masking note that sits in a bold footer paragraph.
- Firewall build duplicates the separate "Network and Firewall" assignment (see below).
- Rubric "HyperV and VMs Rubric" is read-only in Canvas (graded submissions exist or it is locked). Rewriting needs the UI. Well Formatted Document is 5 pts (5%).
- Rubric has 2 levels only.

**UPDATE 2026-10-07 (Corey):** "Network and Firewall Installation and Configuration" (40244749) was imported from another course as reference material. It is not a real Week 1 deliverable. Its useful detail moves into 1B, and the item is then retired (confirm before unpublish or delete). FortiGate and Palo Alto are removed from the course because free student versions are unavailable. Approved options: OPNsense and pfSense. The findings below on that item stay as the record of what to carry over or discard.

**Network and Firewall Installation and Configuration (0 pts) - reference material, merge into 1B then retire**
- Assignment shows 0 points, but its rubric totals 50 pts. One of them is wrong. Submission type is `online_text_entry` while the deliverable is a document with three screenshots (should be `online_upload`).
- Hard-coded `https://192.168.113.1` link and "192.168.113" in the test step.
- Contradictory interface names: OPNsense steps use `hn0`/`hn1`, later "Assign Interfaces" uses `em0`/`em1`.
- Deliverables say "following two screenshots" then list three.
- Includes default credentials in plain text (acceptable for a lab, but state it is lab-only).
- No due date. It is unclear whether it is a prerequisite for 1B, a replacement for 1B's firewall step, or a standalone week item.
- No template boxes.

**NSA CodeBreaker - Extra Credit (0 pts)**
- Rubric is 10 pts (5 formatting + 5 completed tasks) on a 0-pt assignment. Decide whether this is a flat bonus or a points-bearing extra credit and align both.
- Description is bare links with no Purpose, Task or Criteria. Dates (Sept 25, 2026 to Jan 20, 2027) are in the description but the assignment due date is 2026-10-30, which will confuse students.

**Participation: Week 1 (10 pts)**
- Acceptable. Not part of the template (no submission). Skip the rebuild; consider a one-line grading note only if other weeks have one.

**Reading: Module 1 (0 pts)**
- Bare bullet list with a textbook PDF link. Fine as a reading item, but the topic list is thin and does not say which chapters to read. Low priority.

### 3.3 Training assignment (Week 1: Training 1A, 80 pts)

- Structure is correct: Purpose, Task, Learning Objectives, Training Content, Deliverables, Criteria for Success in the right order, table-based boxes, no points inside the Criteria box, no em dashes found.
- Content is aligned to the wrong assignment: Purpose, Learning Objectives and Training Overview all say the training supports "Week 1B" threat models and risk matrices. Live 1B does not use them.
- Points: 80 is off the 25/50/100 scale. Weeks 6-10 training uses 50-95, so the course is already inconsistent; decide one standard. (Rubrics skill carves out a 10-pt binary type for LinkedIn training; neither 80 nor the later weeks fit it.)
- Criteria includes "Submission is completed and uploaded before the assignment due date" but the assignment has no due date.
- Course/Program Outcome language needs verification against Canvas sources before keeping it ("don't fabricate Program Outcome language").
- The LinkedIn course title and 1h 38m duration were not verified here. Verify against LinkedIn Learning.
- No Canvas rubric attached (Week 6-10 trainings should be checked for the same).
- The course topic (IT and cybersecurity risk management) fits the textbook Module 1 reading (CIA triad, 12 threat categories, risk management) better than it fits the labs, so the training itself is probably right; the framing is wrong.

### 3.4 Student resource pages

**Week 1.1 InfoSec Fundamentals and Risk Assessment**
- Content accurate and well built for what it is, but it supports no live assignment (see A1). It does align with textbook Module 1 (CIA, threats, risk management) and the training.
- Em dashes: literal Unicode em dashes present (for example "Component 1: ACTOR — Who threatens you?", "Good—now", "concern—but", and similar). Violates the no em dash rule.
- Grading language: closing box says "Your assignment is graded on completeness and reasoning". Student pages must not carry grading criteria.
- Risk matrix internal inconsistencies: legend names four colors (Red, Yellow, Orange, Green) that do not match the cell labels; the worked "phishing = likely" example conflicts with the probability scale (phishing is 5 in one table row and 3 in another).
- "Scattered Spider ... targets mid-market SaaS" and "most common attack vector in 2025-2026" are unsourced claims. Verify or remove.
- No References section (required by the skill); no Troubleshooting section (not required here).
- Naming: "Week 1.1 Student Guide: ..." does not match `Week [N] | Page [#] - [Topic]`.
- Learning-objectives box is a light grey box with a blue border, not the purple objectives box the skill lists under Must Have. The course doc says Week 1.1 is the canonical "light grey with blue border" style. The skill and the doc disagree on this; pick one and update the other.

**Week 1.2 SysInternals Tools Hands-On**
- Em dashes present (for example "would—and detect", "Good—").
- Invalid CSS: `padding: 14py 16px` (typo for `px`) in the Application row of the Event Log table.
- Fabricated timeline: "2024-01-15 02:34 UTC ... 203.0.113.45" is invented data presented as a real narrative. The skill says "Real data, never fabricated outputs". 203.0.113.0/24 is a documentation range, which signals fabricated but should be labeled as an illustrative example.
- Unsupported thresholds ("Normal processes: 50-200 handles. Malware: 500+") present as fact. Soften or source.
- Says "Assignment 1A requires you to use all three" (it needs four tools) and tells students "this is what assignment 1A grades" (grading language).
- Missing: Sysmon install/config (assignment Task 1), VirusTotal integration in Process Explorer (Task 3), ProcDump/WinDbg (Task 4), PowerShell Get-Process (Task 5 EC).
- Unsupported claim that Process Explorer "ships in ProcessExplorer.zip" with TCPView ("contains Process Explorer and many other tools"). TCPView is a separate download.
- No References section.

**Week 1.3 Lab Environment Setup**
- Em dashes present (for example "Good—now create one", "by design—this").
- Same `14py` CSS typo (No network row).
- Misaligned with 1B (see A3). Also contradicts Week 1 guides elsewhere: recommends Windows 10/11 or Server 2022, while 1B requires Server 2025.
- Contains a "Critical" callout claiming assignment 1A requires malware snapshots; live 1A has no malware step.
- Advice to disable antivirus and updates is lab-specific and should be scoped to the isolated VM.
- No References section.

**ProcDump and WinDbg (legacy)**
- Pasted ChatGPT conversation including "ChatGPT Example:" header, "Copy code" buttons, and div/class markup from the chat UI. Contains "Notes for the Instructor" and a sample solution paragraph in a published student page. Needs replacement.
- Technical error: describes `procdump -e -ma -t` plus "End Task" in Task Manager as a crash with exception code 0xC0000005. Ending a task does not raise an unhandled exception; ProcDump `-e` will not fire and no 0xC0000005 will appear. The sample answer teaches something false.

**Monitoring Network Activity Using TCPView (legacy)**
- Pasted ChatGPT content ("ChatGPT Example:"), "Notes for the Instructor", a sample answer, and a generic "Further Steps" section. Student-facing page should not have instructor notes or sample answers.

**InfoSec Overview (legacy)**
- Raw textbook-slide notes with scraped citation chips ("Invenio IT", "iCorps Blog") and no structure. Stats are cited from third-party blog posts. This is old-style content competing with the new 1.1 guide on the same topic (CIA, threats, vulnerabilities).

**Competing styles (legacy-page-merge trigger):** Week 1 has two page generations: the "Student Guide" set (new) and three unstyled legacy pages. Per CLAUDE.md, surface and offer a merge.

### 3.5 Quiz

Not evaluable through the API. Needs a manual check of: question count and points, alignment to textbook Module 1 (CIA triad, 12 threat categories, contingency plans, policy, risk management), whether it assumes the 1.1 guide's "ACIO" framework (not in the textbook), and whether the quiz is published ahead of the content it tests.

### 3.6 Module structure

- Ordering inside "Assignments" is not by number: 1A, 1B, NSA, "Network and Firewall", Participation. "Network and Firewall" has no numeric code while others do.
- "Reading: Module 1" sits under Training, after the training assignment. Move before it if the reading is meant to precede the training.
- Resources list mixes the three new guides with three legacy pages in arbitrary order.

---

## 3.7 Collective alignment standard (set 2026-10-07)

Rule from Corey: resource pages must align with the assignments, the LinkedIn Learning training, and the reading topics together. Any topic a student needs for any of those three that no page supports is a gap to remedy. A page that supports one of the three is fine; a page that claims support for something that does not exist is a defect.

| Topic needed | Reading (Module 1) | Training 1A (risk mgmt) | Assignment | Current page coverage | Status |
|---|---|---|---|---|---|
| CIA triad, 12 threat categories, risk management, contingency plans, policy | Yes | Yes (risk ID, likelihood/impact, mitigation) | none | 1.1 (CIA, ACIO, risk matrix); InfoSec Overview (legacy) | Aligned in substance. Fix: remove false "1B" claims, cover the 12 threat categories, contingency plans and policy, drop ACIO unless sourced |
| Sysmon install and log analysis | - | - | 1A Task 1 | Table row only | GAP |
| TCPView | - | - | 1A Task 2 | 1.2 plus legacy TCPView page | Partial (consolidate) |
| Process Explorer + VirusTotal | - | - | 1A Task 3 | 1.2 (no VirusTotal setup) | Partial |
| ProcDump + WinDbg | - | - | 1A Task 4 | Legacy page, technically wrong | GAP (needs rewrite) |
| PowerShell Get-Process monitoring (EC) | - | - | 1A Task 5 | None | GAP (optional) |
| VLAN/switch config, addressing scheme | - | - | 1B | None | GAP |
| Bare-metal Server 2025, Hyper-V, vSwitches | - | - | 1B | 1.3 teaches VirtualBox | MISALIGNED |
| AD DS, DNS, NTP | - | - | 1B | None | GAP |
| SAN (iSCSI/NFS), LUN masking | - | - | 1B | None | GAP |
| Live migration, replication | - | - | 1B | None | GAP |
| OPNsense / FortiGate firewall VM | - | - | 1B, Network and Firewall | None | GAP |
| Backup of firewall config | - | - | Network and Firewall | None | GAP |

**Training check still needed:** the LinkedIn course outline (IT and Cybersecurity Risk Management Essential Training) must be confirmed against the guide topics. Only the title and bullets in the assignment were available; I did not verify the course contents on LinkedIn Learning. Do that before writing Page 1 so it reinforces rather than contradicts the videos.

**Reading check still needed:** the Module 1 reading lists only four bullets. The textbook PDF (Principles of Information Security, 4th ed.) should be skimmed for the actual chapter scope so the guide covers the same terms (threat, asset, vulnerability, exploit, control, trespass, 12 threat categories).

**Quiz:** if the quiz tests reading content, the same matrix applies to it.

---

## 4. Remediation plan (skills to apply, in order)

### 4.0 Firewall merge spec (decided 2026-10-07)

**Retired from 1B:** FortiGate (including the FortiGate .vhdx in course files and `FortiGate Setup.docx`, the FortiGate download link, "FortiGate Notes", the FortiGate Administration Guide link) and Palo Alto. Also reword the rubric criterion "NG Firewall" and the "FW01" label to match.

**Firewall choice:** OPNsense as the primary, pfSense CE as the permitted alternative.
- Recommend OPNsense: free with no account needed for the ISO, fully featured, FreeBSD-based with Hyper-V integration included, regular releases, and it is what the Windows Admin course already used (the 1B text says "use your documentation and notes from the Windows Admin class"). Keeping one primary path also keeps the guide and grading simple.
- pfSense CE is a reasonable alternative. Verify its current download path (account or mirror) before telling students to use it. I did not verify this here.
- I do not recommend adding a third option. Anything else (VyOS, IPFire) would need a new guide section with no reuse from the course.

**Carry over from 40244749 into 1B** (valuable detail 1B lacks):
- Firewall VM spec: Generation 1, 4 GB RAM, 10 GB IDE disk, two NICs (WAN and LAN).
- Install flow: boot ISO, `installer` account, UFS, install to disk, halt, eject ISO, reboot, `root` login.
- Console steps: assign interfaces (no LAGG, no VLAN), set WAN static `10.0.[VLAN].2/24`, LAN static `192.168.[VLAN].1/24`, no IPv6, no DHCP on WAN, keep HTTPS.
- Web UI services: LAN DHCP range `.200`-`.225`, DNS forwarding with DHCP lease registration, automatic outbound NAT, default LAN-to-WAN allow rule.
- Test: boot a Windows Server VM on the LAN, confirm DHCP lease, ping firewall, browse to the internet.
- Backup: System > Configuration > Backups, download the XML. Add as a 1B deliverable screenshot.
- Learning outcomes list (usable as verified CLO language, subject to your confirmation).

**Do not carry over:** hard-coded `192.168.113.x`, the `hn0`/`em0` contradiction (use `hn0`/`hn1` consistently as FreeBSD Hyper-V names, or confirm on a live build), the "two screenshots" count error, Windows client "Default Switch" (does not exist on Windows Server).

**Topology (decided 2026-10-07):** two physical servers (HV01, HV02), VMs spread across them, every VM must reach every other VM and the internet. The reference lab's Internal vSwitch is single-host only, so it cannot be used for the shared LAN. Internal and Private switches stay in 1B as a learning step only; no production VM attaches to them.

Proposed design (needs your confirmation of the NIC assumption below):

| Piece | HV01 | HV02 |
|---|---|---|
| Host management and WAN side | External vSwitch `External Network`, bound to physical NIC 1 (VLAN `[VLAN]` set on the NIC, as 1B already does). Host IP `10.0.[VLAN].[slot+10]` | Same switch name, same VLAN, host IP `10.0.[VLAN].[slot+10]` |
| Shared lab LAN | External vSwitch `Lab LAN`, bound to physical NIC 2, VLAN `[VLAN]` on the A2 fabric switch | Identical switch `Lab LAN` on NIC 2 |
| VMs | Firewall (WAN NIC on `External Network`, LAN NIC on `Lab LAN`), DC01 and FS01 (NIC on `Lab LAN`) | DC02 (NIC on `Lab LAN`) |

Traffic path: VM on `192.168.[VLAN].0/24` to firewall LAN `.1`, firewall NATs out its WAN `10.0.[VLAN].2` to the core switch gateway `10.0.[VLAN].1`. VM to VM across hosts rides the shared `Lab LAN` VLAN. The LAN carries no host management traffic, so replication and live migration use the `10.0.[VLAN]` side.

Rules to state in the assignment:
- Switch names must be identical on both hosts (required for live migration and replication).
- Create `Lab LAN` on both hosts before creating any VM; attach VMs to it with no VLAN ID on the vNIC unless the physical port is a trunk.
- Only the firewall bridges `External Network` and `Lab LAN`. Do not attach DCs or the file server to `External Network`. This replaces 1B's current "Connected to your External Virtual Switch" lines for VMs 2-4.
- DC DNS: DC01 primary self, DC02 secondary DC01; add a DNS forwarder on DC01 to the firewall LAN address (or a public resolver) so VMs resolve internet names.
- Verification steps (ping across hosts by IP then by name, `nslookup`, ping `8.8.8.8` and `www.google.com` from each VM, browse from FS01) with a labeled screenshot of each.
- Windows Firewall: allow ICMP echo on VMs or the cross-host ping test will fail for the wrong reason.

**Fallback if blades have only one usable NIC:** put the firewall LAN NIC and all VMs on the same `External Network` switch. Subnets `10.0.[VLAN].0/24` and `192.168.[VLAN].0/24` then share one broadcast domain. It works but leaks the lab LAN onto the host VLAN, so use it only if a second NIC is unavailable. The alternative is a trunked port with VLAN tags set per vNIC, which needs switch changes in the IS Server Room.

**Confirm before I write the rebuild:**
1. Do the blades have a second NIC cabled through the A2 fabric, and can the A2 switch carry your VLAN? (1B already tells students to configure A1 and A2, which suggests yes.)
2. The 1B text asks for live migration and replication "using Kerberos". Kerberos needs the hosts joined to the domain the DC VMs create. Are the hosts expected to join that domain (and is it acceptable that DC VMs run on hosts that depend on them), or should those steps use a different auth option? This is outside the firewall merge but affects the same section.
3. OPNsense Hyper-V interface names (`hn0`, `hn1`) should be confirmed on a live build before the steps go into the guide. I did not verify them here.

The guide Page 3 (Hyper-V lab build) and Page 4 (firewall VM) follow this topology.

### 4.0a Topology confirmed and refined (2026-10-07)

Corey confirmed: Dell blades in an M1000e chassis have 4 NICs connected to the A1 and A2 switches, and the hosts join the AD domain students create. So the two-NIC design stands, with these corrections to the earlier draft:

1. **Hosts need a management adapter on Lab LAN.** My earlier note said replication and live migration would use the `10.0.[VLAN]` side. That fails: the hosts join a domain whose DCs sit on `192.168.[VLAN].0/24`, and the firewall's WAN does not forward inbound traffic to the LAN (NAT, default block of private sources on WAN). So each host also gets an IP on Lab LAN (management OS adapter on the `Lab LAN` switch, "Allow management operating system to share this network adapter"). Suggested: HV01 `192.168.[VLAN].21`, HV02 `192.168.[VLAN].22` (outside the VM statics `.10-.12` and the `.200-.225` DHCP range), DNS = DC01 then DC02, no default gateway on this adapter (the `10.0.[VLAN]` adapter keeps the gateway). Domain join, Kerberos, live migration and replication all run over Lab LAN.
2. **NIC to fabric mapping.** Use NIC on A1 for `External Network` and NIC on A2 for `Lab LAN`, so the two networks sit on separate chassis switches. Students must configure the A2 switch ports for their VLAN as well as A1 (1B already references both). The blade-port to A1/A2 mapping depends on the NDC or mezzanine card; verify on the real blades and write the actual port names into the assignment instead of guessing.
3. **Bootstrap order matters** and must be explicit in the steps:
   1. Install Server 2025 and Hyper-V on both hosts, set host IPs, create both switches on both hosts.
   2. Build the firewall VM on HV01 and verify LAN and WAN reachability.
   3. Build DC01 (forest and DNS), then DC02, then FS01 (join domain).
   4. Join HV01 and HV02 to the domain (DNS pointed at the DCs over Lab LAN).
   5. Only then configure live migration and replication.
4. **Kerberos live migration needs more than domain membership.** In AD, each host's computer account needs constrained delegation for the `cifs` and `Microsoft Virtual System Migration Service` services on the other host, and Kerberos must be selected as the live-migration authentication protocol. Kerberos replication needs the hosts in the domain with replication enabled and port 80 allowed. These steps are missing from 1B today and must be added.
5. **DC dependency risk.** Hosts that run the DCs they authenticate against can be slow to come back after a full power cycle. Add: set the DC VMs to start automatically, and note that cached credentials let the host log on locally.
6. **Hyper-V host firewall rules** for replication (HTTP 80 inbound) and live migration should be stated.

**Authentication decision (2026-10-07, recommendation pending Corey's OK):**
- Replication: keep Kerberos. Once the hosts are domain joined it needs no extra AD work (enable replication on the hosts, allow HTTP 80).
- Live migration: use CredSSP (the Hyper-V default) as the required path. Students start the migration while signed in to the source host (RDP or console), so no delegation is needed. Kerberos with constrained delegation becomes an optional extension or extra credit, since it adds a multi-step AD configuration and a reboot-free but fiddly test that can eat lab time without teaching much beyond Kerberos delegation itself.
- Trade-off to state in the assignment: CredSSP is less secure and cannot be driven from a remote Hyper-V Manager session, which is why Kerberos is the production choice. This gives a short "why production differs" paragraph without making it a graded blocker.
- Update the 1B text, the 1B rubric criterion, and guide Page 3 accordingly. Item 4 in the list above becomes the optional extension.

**Confirmed by Corey:** `hn0` = NIC1 = A1 (External Network, firewall WAN), `hn1` = NIC2 = A2 (Lab LAN, firewall LAN). Note this is the firewall VM's virtual NIC order; students must add the WAN vNIC first so FreeBSD enumerates it as `hn0`.

Still unverified: that the A1/A2 blade-port names in the assignment text match what students see in iDRAC and the chassis; confirm when the 1B text is written.

### Decisions needed from Corey before work starts

1. ~~Network and Firewall source of truth.~~ Resolved: reference material, merge into 1B (see 4.0). Still to confirm: unpublish or delete the item and its 50-pt "Net and Firewall Rubric" after the merge, or keep it hidden for instructor reference.
2. **1A rubric.** Keep the 25-pt PowerShell extra credit inside a 125-pt rubric, or split it out so 1A is a clean 100?
3. **Training points.** Standardize on 50 pts (matching Weeks 7-10) or keep 80?
4. **Guide coverage.** Rewrite 1.1-1.3 to match 1A/1B (recommended), and keep the InfoSec/risk content as a compact Page 1 tied to the Module 1 reading and the training.
5. **Learning objectives box style.** Course doc says Week 1.1 grey/blue is canonical; the skill says purple. Choose one so Weeks 1-10 are consistent.

### Phase 0 - Immediate, before 2026-10-10 (1A due)

| Step | Skill | Action |
|---|---|---|
| 0.1 | assignment-template-rebuild | Rebuild 1A into Purpose / Task / Instructions (Tasks 1-5) / Deliverables / Criteria. Fix the Chrome vs Notepad mismatch. Keep it published (like-for-like template fix). Add CLOs/POs from verified Canvas sources. |
| 0.2 | canvas-html-lint | Lint 1A for em dashes, `&nbsp;` spacers, point values, bullet/h3 adjacency. |
| 0.3 | rubrics | Produce UI-ready 3-level rubric spec for 1A (Corey enters it manually; `create_rubric` is disabled). Well Formatted at 15-16 pts. |

### Phase 1 - Assignments

| Step | Skill | Action |
|---|---|---|
| 1.1 | assignment-template-rebuild | Rebuild 1B: fix the hard-coded `192.168.113.x` values, domain-name typo, NTP inconsistency, VMware ISO link, naming mismatch; add the SAN/LUN-masking note to Instructions; add live migration/replication to Deliverables. |
| 1.2 | assignment-template-rebuild | Merge the Network and Firewall detail into 1B per section 4.0 (OPNsense and pfSense only, FortiGate/Palo Alto removed, firewall config backup added as a deliverable). Then, after your confirmation, unpublish or remove 40244749 and its rubric. Do not rebuild it as a separate assignment. |
| 1.3 | assignment-template-rebuild | Rebuild NSA CodeBreaker boxes; clarify the 2026-10-30 due date vs the Jan 2027 challenge window. |
| 1.4 | rubrics | Rubric specs for 1B (read-only rubric must be replaced in the UI), Network and Firewall (reconcile 0 pts vs 50), CodeBreaker (reconcile 0 pts vs 10). |
| 1.5 | canvas-html-lint | Lint all four rebuilt assignments. |

### Phase 2 - Training and quiz

| Step | Skill | Action |
|---|---|---|
| 2.1 | assignment-template-rebuild | Edit Training 1A: remove the "Week 1B threat model" language, reframe to textbook Module 1 / risk management; drop the due-date criterion; verify LinkedIn course title and duration; verify outcome language; apply the chosen point total. |
| 2.2 | rubrics | 10-pt binary completion rubric or 3-level rubric per decision 3. |
| 2.3 | (manual) | Corey reviews Quiz: Module 1 in the UI against the checklist in section 3.5. |

### Phase 3 - Resource pages

| Step | Skill | Action |
|---|---|---|
| 3.1 | student-resource-pages | Rewrite as `Week 1 | Page 1 - InfoSec Fundamentals and Risk Management` (trim ACIO to what the textbook and training support; add References; remove grading language and em dashes; fix matrix legend). |
| 3.2 | student-resource-pages | New `Week 1 | Page 2 - Sysinternals for Incident Response`: Process Explorer + VirusTotal, TCPView, Sysmon install and config (real command and config steps), ProcDump + WinDbg with a valid crash method. Replace the fabricated 2024 timeline with labeled illustrative data or real captured output. |
| 3.3 | student-resource-pages | New `Week 1 | Page 3 - Hyper-V Lab Build` supporting 1B: VLAN/addressing scheme, bare-metal install, Hyper-V role and virtual switches, AD DS/DNS/NTP, SAN connection and LUN masking, live migration and replication. |
| 3.4 | student-resource-pages | New `Week 1 | Page 4 - Firewall VM Setup` (OPNsense primary, pfSense CE alternative; no FortiGate or Palo Alto) supporting the firewall section of 1B. Built from the carried-over detail in section 4.0. |
| 3.5 | legacy-page-merge | Merge ProcDump and WinDbg and TCPView content into Page 2; fold InfoSec Overview into Page 1 (keep only sourced stats); retire the three legacy pages after confirming nothing links to them. Needs Corey's go-ahead before any delete. |
| 3.6 | lecture-notes-playbook | Not needed for student pages. Check whether an instructor-only Week 1 lecture notes page exists in the course (not in this module); if absent, offer to create one later. |

### Phase 4 - Verification

| Step | Skill | Action |
|---|---|---|
| 4.1 | visual-template-audit | Audit rebuilt pages against the chosen canonical style. |
| 4.2 | canvas-html-lint | Course-wide pass on Week 1 for em dashes (literal Unicode), `<style>` tags, `14py`-style typos. |
| 4.3 | (docs) | Update `courses/BIT360-2026.md` and the CLAUDE.md table to match Canvas (A5). Commit with a suggested message. |

### Sequencing note

Phase 0 is the only phase with a hard deadline. Phases 1-3 can run per item. Per the session-efficiency guidance, run each phase in a fresh session (`/clear`) and use `list_*` calls for structure checks.

---

## 5. Open items

- Quiz: Module 1 contents, points, and publish state (UI only).
- LinkedIn course title and duration.
- Program Outcome and Course Learning Outcome source text for Week 1 assignments.
- Whether duplicate "Student Guide" pages (non "-2" slugs) still exist in the course.
- Why the 1B rubric is read-only (submissions exist or locked).
- Whether any Week 1 instructor-only notes page exists.
- Weeks 2-10 trainings and pages likely carry the same defect (written for assignments that may not exist). Recommend sampling Week 2 next.

---

## Appendix A: 1A rubric spec (enter in Canvas UI; delete this appendix once entered)

Replace "Sysinternals Rubric" (ID 3761630) on assignment 40244730. Name: 1A - SysInternals (125 pts, includes 25 pts extra credit). Reusable: Yes. Assignment stays at 100 points possible. Base check: 16 + 22 + 18 + 18 + 26 = 100.

1. **Well Formatted Document** - Excellent 16: cover page with name, course, assignment; one titled section per task; every screenshot captioned; professional formatting. Good 11: cover page incomplete; sections mostly titled; most screenshots labeled. Unacceptable 0: no cover page or identification; screenshots mostly unlabeled.
2. **Task 1 - Sysmon** - Excellent 22: command-line install and running service shown; log screenshot spans the capture window; report states start/end time, configuration, what was reviewed, key events or anomalies with event IDs. Good 15: install and log shown; window short or unstated; analysis thin or without event IDs. Unacceptable 0: not installed or no log evidence; no analysis.
3. **Task 2 - TCPView** - Excellent 18: clear screenshot; at least two unfamiliar connections documented (process, remote address and port, state); investigation steps explained; legitimate results justified. Good 13: some entries documented; fewer than two investigated or steps vague. Unacceptable 0: no screenshot or analysis.
4. **Task 3 - Process Explorer** - Excellent 18: VirusTotal column with results (and signature verification) shown; flagged or unsigned processes analyzed with name, parent, path, score, recommended action; if none flagged, explains what was examined and what would trigger action. Good 13: results shown; analysis incomplete or no recommendations. Unacceptable 0: VirusTotal not enabled or no analysis.
5. **Task 4 - ProcDump and WinDbg** - Excellent 26: dump submitted; ProcDump command and symbol setup shown; `!analyze -v`, call stack, module output shown; analysis identifies process, exception or termination reason, faulting module, and cause (or what the process was doing for an on-demand dump). Good 18: dump and output shown; analysis partly correct or missing stack/module interpretation. Unacceptable 0: no dump, no WinDbg analysis, or incorrect throughout.
6. **Task 5 - PowerShell Process Monitoring (Extra Credit)** - Excellent 25: script runs, samples at an interval, logs timestamp/name/ID/CPU/memory to CSV, summary of top processes. Good 18: runs and logs; summary missing or metrics incomplete. Unacceptable 0: no script or no output.

Then remove the old two-level rubric from the assignment and confirm the rubric total reads 125 while the assignment shows 100 points possible.

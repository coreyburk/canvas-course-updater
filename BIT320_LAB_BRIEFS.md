# BIT320 — Detailed Lab Briefs & Rubrics

**Course:** Shell and Administrative Scripting (2 credits, 5 weeks)  
**Canvas ID:** 3644698

---

## Lab Submission Standards (All Weeks)

**Format:**
- Code: Plain text files (.sh, .ps1, .py) OR inline in document
- Reports: CSV, JSON, or formatted text
- Documentation: Inline comments in code + brief reflection (100-200 words)

**Naming convention:** `lastname_bit320_lab_w#.extension`

**Late policy:** Per syllabus (typically -10% per day late)

---

# WEEK 1: Log Analysis Fundamentals

## Lab 1.1: "Log Analysis Starter" — Comparative Language Approaches

**Learning Objectives:**
- Outcome #1: Automate analysis of text-based system data
- Outcome #2: Extract structured insights from unstructured logs
- Outcome #3: Compare language paradigms for text processing (bash pipes vs object filtering vs libraries)

**Scenario:**

You're a junior system administrator tasked with analyzing application logs from three different environments:
- An Apache web server (access log)
- A Windows domain controller (Event Log export)
- A Linux application server (syslog)

Your goal: Extract meaningful patterns from each log type, generate a summary report, and reflect on which language was most natural for the task.

**Requirements:**

1. **Choose one log type** (your primary focus):
   - **Option A (Bash):** Apache access log
   - **Option B (PowerShell):** Windows Event Log (CSV export)
   - **Option C (Python):** Linux syslog

2. **Implement analysis in your primary language:**
   - Count total entries
   - Identify top 5 error/failure types (or most common entries)
   - Extract timeline (first entry, last entry, duration)
   - Generate summary report (CSV or JSON)
   - Add basic documentation (comments in code)

3. **Bonus: Comparative labs (optional, +25% credit each):**
   - Implement the same analysis in one or both other languages
   - Compare: lines of code, execution time, readability
   - Reflect: When would you use this language for this task?

**Deliverables:**

1. **Working script(s):**
   - Primary language: Fully functional, commented
   - Bonus languages: Also functional with comments

2. **Sample output:**
   - CSV/JSON report from each language implemented
   - Show data is the same across implementations

3. **Reflection document (100-200 words):**
   - Which language felt most natural? Why?
   - Which was fastest to code?
   - Which produces most readable output?
   - If you had to do this daily, which would you choose? Why?
   - What surprised you about each language?

4. **Test data provided:**
   - Sample Apache log: `sample_access.log` (100 entries)
   - Sample Event Log CSV: `sample_events.csv` (50 entries)
   - Sample syslog: `sample_syslog.log` (80 entries)

**Time Budget:**
- Primary language: 4-5 hours
- Each bonus language: +1.5-2 hours
- Reflection: 0.5 hours
- **Total: 4.5-5.5 hours (primary only), up to 9-10 hours with bonuses**

**Grading Rubric (40 points):**

| Criterion | Points | Expectations |
|-----------|--------|---|
| **Script functionality** | 15 | Script runs without errors; correctly parses chosen log format; generates accurate summary data |
| **Output accuracy** | 10 | Summary counts are correct; top items identified; timeline accurate; report is well-formatted |
| **Code quality** | 8 | Code is readable; variable names are clear; comments explain key logic; no unnecessary complexity |
| **Reflection** | 7 | Addresses all 5 reflection questions; shows thoughtful analysis; demonstrates language understanding |
| **Bonus: Comparative labs** | +10 each | Same criteria as primary; comparison analysis shows understanding of language trade-offs |

**Notes:**
- Focus on getting one language working well rather than rushing all three
- Sample data files will be provided in Canvas
- If you hit a language syntax issue, post in discussion forum or attend office hours—don't give up
- This lab foreshadows Week 3 (where you'll do deep security analysis); notice which language shines for text work

---

# WEEK 2: Scripting Fundamentals

## Lab 2.1: "Log Summary Script" — Process Data and Generate Reports

**Learning Objectives:**
- Outcome #1: Automate data processing workflows with scripts
- Outcome #2: Parse log data and extract meaningful summaries
- Outcome #3: Justify language choice based on task characteristics

**Scenario:**

Your organization's help desk receives tickets daily. They need an automated summary of application error logs—what types of errors occurred, how many, and which ones are priority. Right now they manually parse logs every morning (30 minutes per day).

Your task: Build a script that reads an error log, categorizes errors by type and severity, and generates a daily summary report they can email to stakeholders.

**Requirements:**

1. **Input:** Tab-separated error log file with columns:
   - Timestamp
   - Application name
   - Error level (INFO, WARNING, ERROR, CRITICAL)
   - Error message

2. **Processing:**
   - Count total errors by level (INFO, WARNING, ERROR, CRITICAL)
   - Identify top 5 error messages (by frequency)
   - Extract timeline (first error, last error, date range)
   - Flag any CRITICAL errors

3. **Output:** Formatted report (text or CSV) with:
   - Summary header (date, total errors, date range)
   - Error breakdown by level (count + %)
   - Top 5 errors with occurrence count
   - CRITICAL alert (if any)
   - Footer with generation timestamp

4. **Code quality:**
   - Add comments explaining key sections
   - Use meaningful variable names
   - Handle edge cases (empty file, missing columns, etc.)

5. **Primary language:** Your choice (bash, PowerShell, or Python)

**Deliverables:**

1. **Working script** (`lastname_bit320_lab_w2.sh/ps1/py`)
   - Fully functional
   - Includes comments for key logic
   - Error handling for missing/malformed data

2. **Sample outputs:**
   - Run script on provided test data
   - Show generated report (text or CSV)
   - Include script output (console/log)

3. **Brief reflection** (50-100 words):
   - Why did you choose this language?
   - What was challenging?
   - How would this be different in another language?

4. **Optional bonus: Comparative lab** (+15 points):
   - Implement same script in one other language
   - Compare outputs (should be identical data)
   - Document differences in approach

**Test Data Provided:**
- `sample_errors.log` — 500 entries, mixed levels, realistic error messages

**Time Budget:**
- Primary language: 3-4 hours
- Bonus language: +1.5-2 hours
- Testing + reflection: 0.5 hours
- **Total: 3.5-4.5 hours (primary), up to 6.5-7 hours with bonus**

**Grading Rubric (45 points):**

| Criterion | Points | Expectations |
|-----------|--------|---|
| **Script functionality** | 15 | Script runs without errors on provided test data; processes all entries correctly |
| **Output accuracy** | 12 | Report totals are correct; top errors accurately identified; formatting is clean and readable |
| **Code quality** | 10 | Code is well-commented; variables are clear; logic is straightforward; handles basic edge cases |
| **Error handling** | 5 | Script gracefully handles missing columns, empty files, or unexpected data; doesn't crash |
| **Reflection** | 3 | Addresses language choice, challenges, and language comparison |
| **Bonus: Comparative lab** | +15 | Same criteria as primary script; comparison shows understanding of language strengths/weaknesses |

**Notes:**
- This is your first real "data processing" script—the foundation for Week 3
- If you get stuck on data parsing, review the LinkedIn Learning resources for your chosen language
- Test with provided sample data; once working, you could use this on real logs
- Think about: "What would make this script more useful?" (This informs Week 4 planning)

---

# WEEK 3: Data Processing & Text Handling

## Lab 3.1: "Security Audit Report" — Deep Log Analysis & Reporting

**Learning Objectives:**
- Outcome #2: Process large datasets to extract security-relevant insights
- Outcome #3: Justify why bash excels at text processing (with comparisons)
- Outcome #1: Automate a realistic security workflow

**Scenario:**

Your organization's security team needs a daily report of suspicious login activity from the domain controller. They want:
1. Failed authentication attempts (by user, by time of day)
2. Unusual patterns (same user failed many times? attack pattern?)
3. Summary statistics (total failures, unique users affected, time range)
4. Alert for critical patterns (user locked out, repeated failures on admin account)

Right now, they manually review Event Log exports. You're building the automated version.

**Requirements:**

1. **Primary Implementation: Bash** (This is where bash shines—text processing is its native strength)
   - Read Windows Event Log export (CSV format) OR Linux auth log
   - Parse failure reasons, usernames, timestamps
   - Use grep/awk/sort/uniq for analysis (demonstrate bash power)
   - Generate formatted report with findings
   - Highlight patterns and anomalies

2. **Report must include:**
   - Header: Date range, total failed attempts, unique users affected
   - Failed attempts by user (count + percentage)
   - Failed attempts by hour of day (identify time patterns)
   - Top failure reasons (invalid credentials, account locked, etc.)
   - Red flags: Admin account failures, repeated failures from same IP/user
   - Footer: Report timestamp, data source

3. **Code quality:**
   - Use bash idioms (pipes, redirection, standard text tools)
   - Comments explaining each processing step
   - Variable names that describe what they hold
   - Handle edge cases (empty input, malformed lines)

4. **Comparison labs (optional, but encouraged):**
   - **PowerShell version:** Use Select-Object, Where-Object, Group-Object; show object-based approach
   - **Python version:** Use regex and dictionaries; show readability advantage for complex logic
   - Compare outputs; document when you'd use each

**Deliverables:**

1. **Primary Bash Script** (`lastname_bit320_lab_w3_bash.sh`)
   - Fully functional; well-commented
   - Demonstrates grep, awk, sort, uniq pipeline techniques
   - Handles provided test data without errors

2. **Security Audit Report** (generated output)
   - Formatted report (text or CSV)
   - All required sections present
   - Data is accurate
   - Findings are actionable

3. **Optional: PowerShell & Python versions**
   - Same output data as bash version
   - Demonstrate different paradigm for same problem
   - Side-by-side code comparison (see how each language approaches the task)

4. **Comparative analysis document** (if doing comparisons, 150-200 words):
   - Why bash dominates this task
   - Where PowerShell or Python might be easier
   - Real-world trade-offs (speed, readability, portability)
   - When you'd pick each language

**Test Data Provided:**
- Windows Event Log export (CSV): 1,000 authentication failure events
- OR Linux auth.log sample: 500 failed login attempts
- Data includes realistic patterns: brute-force attempts, legitimate lockouts, time-of-day variations

**Time Budget:**
- Bash primary implementation: 4-5 hours
- PowerShell comparison: +1.5-2 hours
- Python comparison: +1.5-2 hours
- Comparative analysis: +1 hour
- **Total: 4.5-5.5 hours (bash only), up to 9-10 hours with comparisons**

**Grading Rubric (50 points):**

| Criterion | Points | Expectations |
|-----------|--------|---|
| **Bash script functionality** | 15 | Script runs without errors; correctly parses log format; generates accurate summary data |
| **Report quality** | 15 | Report includes all required sections; findings are accurate and actionable; formatting is professional |
| **Bash code quality** | 12 | Uses appropriate text tools (grep/awk/sort/uniq); demonstrates bash idioms; well-commented; readable |
| **Security insights** | 8 | Analysis reveals meaningful patterns; flags are appropriate; report would be useful to security team |
| **Bonus: PowerShell version** | +12 | Script functional; demonstrates object-based approach; code quality comparable to bash |
| **Bonus: Python version** | +12 | Script functional; demonstrates readable logic; appropriate use of regex and data structures |
| **Bonus: Comparative analysis** | +10 | Thoughtful comparison; demonstrates understanding of when/why each language is appropriate |

**Notes:**
- This is the capstone of Weeks 1-2 skills; you're ready for this
- Bash is the right tool here—see why?
- Security insights matter: A good report reveals actionable patterns, not just stats
- If you add comparisons, you'll see how each language approaches the same problem differently
- This skillset is directly applicable: audit reports like this are real work in any infrastructure team

---

# WEEK 4: Server Automation & Error Handling

## Lab 4.1: "Service Health Monitoring & Restart Automation"

**Learning Objectives:**
- Outcome #1: Automate server administration workflows
- Outcome #4: Implement scripts with basic error handling and scheduling
- Outcome #3: Choose language based on target infrastructure

**Scenario:**

Your organization runs several critical services on their Windows Server VMs and Linux servers. If a service crashes, it might be hours before someone notices. You're building an automated health check: monitor key services, auto-restart if failed, and alert if restart fails.

The script will eventually be scheduled to run every 5 minutes (Week 4.2), but first, make it work on demand.

**Requirements:**

1. **Service monitoring:**
   - Check status of 3-5 critical services (your choice: web server, database, file service, etc.)
   - Report status: Running, Stopped, or Unknown
   - Identify any that are stopped/failed

2. **Auto-restart logic:**
   - If a service is down, attempt to restart it
   - Verify restart succeeded
   - Record the action (what was attempted, did it work?)

3. **Error handling (IMPORTANT):**
   - What if restart fails? Log it; don't keep trying forever
   - What if service is locked by another process? Graceful handling
   - What if you lack permissions? Report and continue
   - What if the service doesn't exist? Don't crash; note it

4. **Logging:**
   - Timestamp each action
   - Record what was checked, what was found, what was done
   - Include successes and failures
   - Log file format: one action per line (easy to parse later)

5. **Target infrastructure:**
   - **Bash option:** SSH into your Hyper-V Linux VM or WSL2; use systemctl to manage services
   - **PowerShell option:** Query your Hyper-V Windows Server VM or local Windows services
   - **Python option:** Remote monitoring via paramiko (SSH) or local psutil/subprocess

**Deliverables:**

1. **Functional script** (`lastname_bit320_lab_w4.sh/ps1/py`)
   - Monitors specified services
   - Attempts restart if needed
   - Handles errors gracefully
   - Generates log entries

2. **Test run documentation:**
   - Show script run on live or test infrastructure
   - Include console output + log file
   - Demonstrate: service was down → script restarted it → verified success
   - Demonstrate: error case (e.g., simulate permission denied; show graceful handling)

3. **Error handling documentation** (100-150 words):
   - List 3-5 error cases you anticipated
   - For each, explain how your script handles it
   - Example: "If restart fails, the script logs the failure and continues checking other services rather than crashing"

4. **Brief reflection** (50-100 words):
   - Why did you choose this language?
   - What error cases were tricky to handle?
   - How would scheduling this change the script?

**Time Budget:**
- Script development: 3-4 hours
- Testing & error simulation: 1 hour
- Documentation: 0.5 hours
- **Total: 4.5-5.5 hours**

**Grading Rubric (50 points):**

| Criterion | Points | Expectations |
|-----------|--------|---|
| **Script functionality** | 15 | Script runs without errors; correctly checks service status; restarts work as intended |
| **Restart logic** | 10 | Successfully restarts stopped services; verifies restart success; multiple services handled correctly |
| **Error handling** | 15 | Handles missing services, permission errors, restart failures gracefully; script doesn't crash; logs appropriate messages |
| **Logging** | 8 | Log entries are clear, timestamped, and actionable; record what was checked, found, and done |
| **Documentation** | 2 | Error handling and reflection are thoughtful; show understanding of real-world failure modes |

**Notes:**
- This is your first script with error handling—take it seriously
- Real services fail for real reasons; anticipate them
- Logging matters: Future you will need to know what happened and why
- Next week you'll schedule this; make sure it's robust enough for unattended execution

---

## Lab 4.2: "Add Error Handling & Alerting" (Supplemental, 3 hours)

**Extend Lab 4.1 with:**
1. Try/catch blocks (or equivalent error handling for bash/PS)
2. Email alert on repeated failures (e.g., restart fails twice)
3. Structured logging (JSON or key-value format for easy parsing)

**Grading:** +15 bonus points (or roll into 4.1 if you combine them)

---

# WEEK 5: Administration Automation Project

## Lab 5.1: "Administration Automation Project" — Capstone Integration

**Learning Objectives:**
- Outcome #1: Automate a complete, realistic server administration workflow
- Outcome #2: Process and report on system data meaningfully
- Outcome #3: Justify scripting approach; compare alternatives
- Outcome #4: Implement production-ready script with error handling, scheduling, documentation

**Scenario:**

Choose one real system administration task you've been thinking about in Weeks 1-4. Your task is to build a complete, usable automation script that could actually run in production.

**Available Scenarios:**

1. **Option A: Linux Server Maintenance Suite** (Bash-focused)
   - Log rotation (archive old logs, compress, clean up disk)
   - Disk space monitoring (alert if % usage exceeds threshold)
   - Service health check (ensure critical services are running)
   - Report generation (email summary to admin)

2. **Option B: Windows Server Automation Toolkit** (PowerShell-focused)
   - Patch status report (which servers need patches?)
   - User/group audit (compare AD groups to expected baseline; flag anomalies)
   - Certificate expiration tracking (SSL certs expiring soon?)
   - Backup verification (confirm backups completed successfully)

3. **Option C: Cross-Platform Infrastructure Automation** (Python-focused)
   - Provision a new VM on AWS or Azure (or simulate)
   - Configure with security baseline (firewall, agents, monitoring)
   - Register with monitoring system
   - Generate deployment report

4. **Option D: Custom scenario** (with instructor approval)
   - Propose your own automation task
   - Must integrate components from Weeks 1-4 (data processing, error handling, scheduling, etc.)

**Requirements:**

1. **Functional automation script:**
   - Solves a real problem (not contrived)
   - Works in your chosen language (bash, PowerShell, Python, or combination)
   - Handles at least 3 error scenarios gracefully
   - Produces useful output (report, log, or action taken)

2. **Production-ready quality:**
   - Comprehensive error handling (try/catch, exit codes, graceful degradation)
   - Clear logging (what ran, what succeeded/failed, why)
   - Clean, well-commented code (someone else could maintain it)
   - Runnable on-demand or via scheduler

3. **Documentation:**
   - README: What the script does, why it's useful, how to run it
   - Inline comments: Explain non-obvious logic
   - Error handling: Document anticipated failure modes and recovery
   - Configuration: Any parameters/settings that should be customized

4. **Reflection & Comparative Analysis (Capstone component):**
   - **Narrative (300-400 words):**
     - Why did you choose this automation task?
     - Why is your chosen language appropriate?
     - What language(s) would you *not* use for this? Why?
     - What was most challenging about error handling?
     - How would you test this in production?
   - **Comparison table:**
     - If written in each of the three languages, pros and cons (don't write all three; just analyze)

5. **Optional: Peer code review** (+10 bonus points)
   - Review another student's script
   - Document code quality, readability, error handling
   - Suggest 2-3 improvements
   - Sign off on review

**Deliverables:**

1. **Working automation script** (`lastname_bit320_capstone.sh/ps1/py`)
   - Fully functional on your infrastructure
   - Comprehensive error handling
   - Clean, commented code

2. **Documentation package:**
   - README.md (what, why, how)
   - Inline code comments
   - Example outputs (log files, reports)
   - Configuration guide (if applicable)

3. **Test run evidence:**
   - Script execution output (success case)
   - Error handling demonstration (triggered error; recovery shown)
   - Generated artifacts (reports, logs, etc.)

4. **Reflection & comparative analysis document** (300-400 words narrative + comparison table)

5. **Optional: Peer code review** (if participating in bonus)

**Time Budget:**
- Script development: 5-6 hours
- Testing + error scenarios: 1-1.5 hours
- Documentation: 1 hour
- Reflection: 1-1.5 hours
- Optional peer review: +1 hour
- **Total: 8-10 hours (primary), up to 11 hours with peer review**

**Grading Rubric (75 points):**

| Criterion | Points | Expectations |
|-----------|--------|---|
| **Script functionality** | 20 | Script runs without errors; solves stated problem; produces expected output; tested on real infrastructure |
| **Error handling** | 15 | Handles at least 3 error scenarios gracefully; logs errors; doesn't crash; recovery is sensible |
| **Code quality** | 15 | Well-commented; variable names are clear; logic is straightforward; maintainable by others |
| **Documentation** | 12 | README is clear; comments explain non-obvious logic; configuration is documented; examples provided |
| **Reflection & analysis** | 10 | Narrative addresses all questions; comparison table shows thoughtful language selection analysis; demonstrates learning |
| **Bonus: Peer code review** | +10 | Thorough review; constructive feedback; identifies 2-3 real improvements; thoughtful critique |

**Notes:**
- This is your capstone for BIT320—make it something you're proud of
- Real code, real problem, real solution
- If you want to use this in your job or portfolio, build it to that standard
- Peer review teaches you to think critically about code quality
- Office hours this week: bring your scripts, test edge cases, get feedback

---

## Grading Summary

| Week | Lab | Primary Points | Bonus Points | Total |
|------|-----|---|---|---|
| **1** | Log Analysis Starter | 40 | 20 (comps) | 60 |
| **2** | Log Summary Script | 45 | 15 (comp) | 60 |
| **3** | Security Audit Report | 50 | 34 (comps + analysis) | 84 |
| **4** | Service Monitoring | 50 | 15 (enhancement) | 65 |
| **5** | Capstone Project | 75 | 10 (peer review) | 85 |
| | | **260** | **94** | **354** |

**Grading scale:** 260-354 points (primary + bonuses)
- A: 315-354 (89-100%)
- B: 273-314 (77-88%)
- C: 234-272 (66-76%)
- D: 195-233 (55-65%)
- F: <195 (<55%)

**Recommendation:** Students should aim for primary work (~260 pts); bonuses are available for those curious about languages or wanting to go deeper.

---

## General Rubric Criteria Applied Across All Labs

### Code Quality (Applied to every graded script)
- **Excellent (90-100%):** Code is clean, well-organized, with clear variable names; comments explain logic; no unnecessary complexity
- **Good (80-89%):** Code works; mostly clear; adequate comments; minor inefficiencies
- **Adequate (70-79%):** Code works; some unclear sections; basic comments; could be more efficient
- **Poor (<70%):** Code runs but is hard to follow; minimal comments; inefficient or fragile

### Error Handling (Applied to weeks 4-5)
- **Excellent:** Anticipates 3+ error scenarios; handles gracefully; logs appropriately; script doesn't crash
- **Good:** Handles 2-3 common errors; mostly graceful; minimal logging gaps
- **Adequate:** Handles 1-2 errors; basic graceful handling; logging present but sparse
- **Poor:** Minimal error handling; script crashes on unexpected input; no logging

### Documentation Quality (Applied to all labs)
- **Excellent:** Clear inline comments; README is thorough; examples provided; easy for others to use/maintain
- **Good:** Adequate comments; README covers basics; examples helpful
- **Adequate:** Some comments; README present but basic; examples missing
- **Poor:** Sparse comments; README minimal or unclear; hard to understand purpose

---

## Tips for Success

1. **Start early:** These labs build on each other. Don't fall behind.
2. **Test incrementally:** Get one piece working, then add more. Don't try to build the whole thing at once.
3. **Use sample data:** Test with provided data before touching real logs/systems.
4. **Ask questions:** If stuck, post in discussion or attend office hours. Don't suffer in silence.
5. **Reflect seriously:** The reflection sections teach you to think critically about language choice. This is valuable.
6. **Document as you go:** Don't wait until the end to comment code or write documentation.
7. **Compare languages:** Bonus labs are optional, but they teach you a lot about when each language shines.


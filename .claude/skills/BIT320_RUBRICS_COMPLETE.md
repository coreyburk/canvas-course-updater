---
name: bit320-rubrics-complete
description: Complete rubric specifications for all 8 BIT320 labs (1.1-5.1). Includes criterion names, descriptions, and all rating levels. Ready for Canvas UI entry—no cross-referencing needed.
---

# BIT320 Complete Rubric Specifications

**How to use this document:**
Copy the criterion information directly into Canvas UI:
1. **Criterion Name** → Canvas "Criterion Name" field
2. **Canvas Description Field** → Canvas "Criterion Description" field
3. **Canvas Rating Levels** table → Create three rating levels with points and descriptions

---

## Lab 1.1: Infrastructure Setup (25 points)

**Status:** Keep existing rubric (no changes needed)

### Criterion 1: Well Formatted Document (5 pts, 20%)
**Canvas Description Field:** Submission is professionally formatted with clear identification, organized sections, and labeled deliverables.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 5 | Submission includes complete identification (name, course, assignment). All screenshots labeled with clear, descriptive captions. Setup notes well-organized, professional formatting. |
| Good | 3 | Submission includes most required identification. Most screenshots labeled. Setup notes present with minor formatting issues. |
| Unacceptable | 0 | Missing identification or clear organization. Screenshots unlabeled. Setup notes unclear or unprofessional. |

### Criterion 2: Environment Installation (10 pts, 40%)
**Canvas Description Field:** All three scripting environments (bash via WSL2, Python 3.10+, PowerShell) are successfully installed and functional.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 10 | All three environments (Bash via WSL2, Python 3.10+, PowerShell) successfully installed and fully functional. Installation process completed without errors or workarounds needed. |
| Good | 7 | All three environments installed and mostly functional. Minor installation issues encountered but resolved. Setup process followed correctly. |
| Unacceptable | 0 | One or more environments not installed or non-functional. Installation incomplete or process not followed. |

### Criterion 3: Verification & Testing (10 pts, 40%)
**Canvas Description Field:** Version checks and test commands confirm that all three environments are working correctly and ready for use.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 10 | All version checks pass for bash, Python, and PowerShell. Test commands produce correct output in all three environments. Screenshots clearly show version information and test results. |
| Good | 6 | Version checks pass for all three environments. Test commands work correctly with minor issues. Screenshots show outputs but may lack some clarity. |
| Unacceptable | 0 | Version checks fail for one or more environments. Test commands don't produce expected output. Screenshots unclear, missing, or don't demonstrate success. |

---

## Lab 1.2: System Command Execution (25 points)

**Status:** UPDATE REQUIRED - Add Code Fundamentals criterion

### Criterion 1: Well Formatted Document (4 pts, 16%)
**Canvas Description Field:** Submission is professionally formatted with clear identification, organized sections with titles, and labeled screenshots showing script output from each language.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 4 | Document includes name, course code, assignment name; all three scripts and outputs clearly organized with section titles; each screenshot has descriptive label; professional formatting. |
| Good | 2 | Most required info present; scripts and outputs organized; most screenshots labeled; minor formatting issues. |
| Unacceptable | 0 | Missing identification or labels; disorganized; unclear which screenshots correspond to which scripts. |

### Criterion 2: Code Fundamentals - Functions, Loops & Error Handling (8 pts, 32%)
**Canvas Description Field:** Code is organized with reusable functions, uses loops to process data, includes error handling to validate operations, and is well-commented.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 8 | Each script defines 2-3 functions to organize logic (not all procedural). Loops used to iterate over data collections. Error handling present: bash uses `|| exit` or error checks, PowerShell validates with error checks, Python includes try/except blocks. Comments on functions explaining purpose. |
| Good | 5 | Functions present but organization could be improved. Loop present but basic. Some error checking implemented; 1-2 commands lack validation. Most functions have comments. |
| Unacceptable | 0 | No functions defined (entirely procedural). No loops used. No error handling; scripts crash on errors. |

### Criterion 3: Script Functionality (7 pts, 28%)
**Canvas Description Field:** All three scripts (bash, PowerShell, Python) execute successfully and produce output demonstrating that each language can interact with the operating system.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 7 | All three scripts run without errors; each produces clear system information output; all three environments working reliably. |
| Good | 4 | All three scripts run; minor issues in one script resolved or documented; output generally correct. |
| Unacceptable | 0 | One or more scripts don't run; output missing or shows errors. |

### Criterion 4: Comparative Analysis & Language Understanding (6 pts, 24%)
**Canvas Description Field:** Analysis thoughtfully compares how each language handles system commands, demonstrates understanding of paradigm differences, and explains why languages have different approaches.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 6 | Analysis clearly compares how each language handles functions, loops, and error handling; notes language-specific strengths/differences; explains why error handling differs; 100-150+ words; demonstrates understanding of paradigm differences. |
| Good | 4 | Identifies differences in how functions/loops work; observations mostly accurate; discusses error handling approaches; 75-125 words. |
| Unacceptable | 0 | Missing analysis or generic observations; insufficient reflection (under 75 words); doesn't address functions/loops/error handling differences. |

---

## Lab 1.3: Log Analysis Starter (100 points)

### Criterion 1: Well Formatted Document (16 pts, 16%)
**Canvas Description Field:** Submission is professionally formatted with clear identification, organized sections, labeled screenshots and outputs, and a well-organized comparison table.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 16 | Complete identification (name, course, assignment, date). All sections clearly titled and organized. Every screenshot/output labeled with descriptive caption. Professional formatting throughout. Comparison table well-organized. |
| Good | 11 | Identification present; sections mostly titled; most screenshots labeled; minor formatting inconsistencies; comparison table present but could be clearer. |
| Unacceptable | 0 | Missing identification or organization. Screenshots unlabeled. Disorganized structure; difficult to follow. |

### Criterion 2: Code Fundamentals - Functions, Loops & Error Handling (10 pts, 10%)
**Canvas Description Field:** Code is organized with reusable functions, uses loops to process data, includes error handling to validate file operations, and is well-commented.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 10 | All three scripts use functions to organize analysis logic (not procedural). Loops iterate over data. Error handling validates file operations: bash includes error checks, PowerShell uses error handling, Python includes try/except. Comments explain function purpose. |
| Good | 7 | Functions present; loops used to process data; some error handling; most functions commented; organization could be stronger. |
| Unacceptable | 0 | Minimal or no functions. Limited error handling. No comments on functions. |

### Criterion 3: Script Implementation - All Three Languages (40 pts, 40%)
**Canvas Description Field:** All three scripts (bash, PowerShell, Python) execute successfully and correctly analyze log files, counting entries by severity level and identifying top error messages.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 40 | All three scripts (bash, PowerShell, Python) execute successfully without errors. Each correctly reads log file, counts entries by level, identifies top 5 errors, extracts timeline. Output matches expected format. Each script demonstrates appropriate language idioms. |
| Good | 28 | All three scripts run; minor issues in one script resolved. Output mostly accurate; log analysis is correct; one or two fields incomplete or slightly off format. |
| Unacceptable | 0 | One or more scripts don't run or produce incorrect output. Log analysis incomplete or significantly inaccurate. |

### Criterion 4: Comparative Analysis & Tool Selection (24 pts, 24%)
**Canvas Description Field:** Completed comparison table with thoughtful observations about differences in lines of code, readability, execution time, natural fit for the task, ease of understanding, and paradigm approach.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 24 | Completed comparison table with thoughtful observations on lines of code, readability, execution time, natural fit, ease of understanding, and paradigm approach. Identifies strengths/weaknesses of each language clearly. Explains why different languages suit different tasks. Demonstrates deep understanding of paradigm differences. |
| Good | 16 | Comparison table mostly complete. Identifies differences in languages; observations mostly accurate. Some insight into paradigm trade-offs; could be deeper. |
| Unacceptable | 0 | Comparison missing or incomplete. Generic observations; doesn't distinguish between languages or paradigms. |

### Criterion 5: Testing Evidence & Reflection (10 pts, 10%)
**Canvas Description Field:** Clear evidence of testing all three scripts successfully, with reflection addressing which language felt natural, fastest to write, most readable, and which you would use for different scenarios.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 10 | Clear evidence of testing all three scripts (screenshots of successful runs). Reflection thoughtfully addresses: which language felt natural, fastest to write, most readable, which would you use for one-off, which for daily jobs. 150-200+ words; demonstrates learning. |
| Good | 7 | Testing evidence present (screenshots showing output). Reflection addresses most questions; 100-150 words; adequate understanding shown. |
| Unacceptable | 0 | Missing testing evidence or reflection. Reflection under 100 words or doesn't address the questions. |

---

## Lab 2.1: Log Summary Script (50 points)

### Criterion 1: Well Formatted Document (8 pts, 16%)
**Canvas Description Field:** Submission is professionally formatted with clear identification, organized sections, labeled screenshots showing script output, and the script code clearly presented.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 8 | Complete identification. All sections clearly titled. Every screenshot labeled with descriptive caption. Script provided with syntax highlighting or clear formatting. Professional organization. |
| Good | 5 | Identification present; sections mostly titled; most screenshots labeled; script included but could be clearer. |
| Unacceptable | 0 | Missing identification or disorganized. Screenshots unlabeled. |

### Criterion 2: Code Fundamentals - Functions, Loops & Error Handling (8 pts, 16%)
**Canvas Description Field:** Code is organized with reusable functions, uses loops to iterate over error entries, includes error handling to validate file operations, and is well-commented.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 8 | Script uses 2-3 functions to organize analysis logic. Loops iterate over error entries or severity levels. Error handling validates file operations (checks file exists, handles read errors gracefully). Comments explain function purpose. |
| Good | 5 | Functions present; basic loop; some error checking; organization could be stronger. |
| Unacceptable | 0 | No functions or loops. No error handling. |

### Criterion 3: Bash Mastery & Text Processing (20 pts, 40%)
**Canvas Description Field:** Script demonstrates bash strength using grep, awk, sort, and uniq appropriately, with efficient pipelines that correctly categorize errors and identify top error messages.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 20 | Script demonstrates bash strength: uses grep, awk, sort, uniq appropriately. Pipelines are efficient and well-constructed. Correctly categorizes errors by severity, identifies top errors accurately. Output format is clear and accurate. |
| Good | 14 | Script uses text tools correctly; most results accurate; pipelines work but could be more efficient; minor formatting issues. |
| Unacceptable | 0 | Text tools used incorrectly or inefficiently. Results inaccurate or incomplete. |

### Criterion 4: Code Quality & Output (14 pts, 28%)
**Canvas Description Field:** Script is readable with clear variable names and comments, produces professional and actionable output with all required information, and executes reliably.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 14 | Script is readable with clear variable names and comments. Output is professional and actionable. All required information present (error counts, top errors, timeline). Execution is reliable. |
| Good | 10 | Script readable; output mostly complete; 1-2 items missing or unclear; minor code quality issues. |
| Unacceptable | 0 | Script hard to follow. Output incomplete or incorrect. |

---

## Lab 3.1: Windows Event Log Audit (100 points)

### Criterion 1: Well Formatted Document (16 pts, 16%)
**Canvas Description Field:** Submission is professionally formatted with clear identification, organized sections with titled areas, labeled screenshots and outputs, and a professional security audit report.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 16 | Complete identification and section titles. All screenshots/outputs labeled clearly. Report is professional and organized. Security findings clearly presented. |
| Good | 11 | Identification present; sections mostly titled; most screenshots labeled; report organized but could be clearer. |
| Unacceptable | 0 | Missing identification or organization. Disorganized report. |

### Criterion 2: Code Fundamentals - Functions, Loops & Error Handling (10 pts, 10%)
**Canvas Description Field:** Code is organized with reusable functions, uses loops to iterate over event collections, includes error handling to validate Get-EventLog calls, and is well-commented.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 10 | Script uses functions to organize event filtering/analysis logic. Loops iterate over event collections or grouping results. Error handling validates Get-EventLog calls and handles cases where events not found. Comments explain function purpose. |
| Good | 7 | Functions present; loops used; error checking present; most functions commented. |
| Unacceptable | 0 | Minimal functions/loops/error handling. |

### Criterion 3: PowerShell Object Pipeline Mastery (35 pts, 35%)
**Canvas Description Field:** Script correctly uses Get-EventLog, Where-Object, Group-Object, and Select-Object with efficient object pipelines to query and analyze Windows Security Event Log.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 35 | Script correctly uses Get-EventLog for Security log, Where-Object for filtering, Group-Object for grouping, Select-Object for selecting properties. Object pipelines are appropriate and efficient. Event ID 4625 (failed logins) correctly queried. |
| Good | 24 | PowerShell cmdlets used correctly; pipelines work; 1-2 queries could be more efficient; minor issues with object handling. |
| Unacceptable | 0 | PowerShell cmdlets misused. Pipelines don't work or produce incorrect results. |

### Criterion 4: Error Handling & Report Quality (24 pts, 24%)
**Canvas Description Field:** Script handles cases where events are not found, permissions are denied, or logs are unavailable, and generates a professional report with required sections and accurate, actionable findings.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 24 | Script handles cases where events not found, permissions denied, or logs unavailable. Report includes all required sections: header (date range, total attempts, affected users), failed attempts by user/hour, top failure reasons, red flags identified (admin failures, brute-force patterns), footer with timestamp. Findings are accurate and actionable. |
| Good | 16 | Most error handling present; report includes most required sections; findings mostly accurate; formatting could be professional. |
| Unacceptable | 0 | Limited error handling. Report incomplete or findings inaccurate. |

### Criterion 5: Security Analysis & Comparative Insight (15 pts, 15%)
**Canvas Description Field:** Red flags are correctly identified (admin failures, brute-force patterns, unusual activity), analysis demonstrates security understanding, and optional comparison explains why PowerShell excels for this task.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 15 | Red flags correctly identified (admin account failures, repeated failures from same user, unusual patterns). Analysis demonstrates understanding of security implications. Optional: Bonus comparison showing why PowerShell beats bash/Python for this task (15+ pts bonus possible). |
| Good | 10 | Most red flags identified; analysis shows security awareness; comparison attempted. |
| Unacceptable | 0 | Missing analysis or red flags not identified. |

---

## Lab 4.1: Service Monitoring in Python (50 points)

### Criterion 1: Well Formatted Document (8 pts, 16%)
**Canvas Description Field:** Submission is professionally formatted with clear identification, organized sections, labeled screenshots of test runs, and included log file excerpts.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 8 | Complete identification. Sections clearly titled. Screenshots of test runs labeled. Log file excerpts included. Professional formatting. |
| Good | 5 | Identification present; sections organized; screenshots/logs mostly present. |
| Unacceptable | 0 | Missing identification or disorganized. |

### Criterion 2: Code Fundamentals - Functions, Loops & Error Handling (8 pts, 16%)
**Canvas Description Field:** Code is organized with reusable functions for distinct tasks, uses loops to iterate over services, includes try/except blocks for all external operations, and is well-commented.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 8 | Script uses functions to organize: get_service_status, attempt_restart, log_action. Loops iterate over list of services to monitor. Try/except blocks wrap all external calls. Comments explain function purpose. |
| Good | 5 | Functions present; loops iterate; error handling present; could be better organized. |
| Unacceptable | 0 | Minimal functions/loops. No try/except blocks. |

### Criterion 3: Error Handling - Graceful Recovery (18 pts, 36%)
**Canvas Description Field:** Script handles multiple distinct error scenarios, uses try/except blocks appropriately, degrades gracefully without crashing, and provides meaningful error messages.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 18 | Handles at least 3 distinct error scenarios: permission denied, service not found, restart timeout. Uses try/except blocks appropriately. Graceful degradation: script doesn't crash; logs errors and continues. Meaningful error messages (not just "Error"). |
| Good | 12 | Handles 2 error scenarios; try/except present; most operations wrapped; error messages could be more meaningful. |
| Unacceptable | 0 | Minimal error handling; script crashes on errors. |

### Criterion 4: Structured Logging & Production Readiness (16 pts, 32%)
**Canvas Description Field:** Every action is logged with timestamps and status, log entries include service, status, and outcome, test evidence shows multiple runs, and script could run unattended in production.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 16 | Every action logged with timestamp and status (success/failure). Log entries include: service checked, status found, restart attempted, outcome. Testing evidence shows multiple runs demonstrating reliability. Script could run unattended. |
| Good | 11 | Most actions logged; timestamps present; test runs shown; minor gaps in logging. |
| Unacceptable | 0 | Minimal logging or test evidence. |

---

## Lab 4.2: Scheduled Automation (25 points)

### Criterion 1: Well Formatted Document (4 pts, 16%)
**Canvas Description Field:** Submission is professionally formatted with clear identification, organized sections, labeled screenshots of scheduling configuration and logs, and clear setup instructions.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 4 | Identification present and organized. Screenshots of scheduling configuration and logs clearly labeled. Setup instructions clear and reproducible. |
| Good | 2 | Identification and sections present; screenshots labeled; instructions adequate. |
| Unacceptable | 0 | Missing organization or unclear instructions. |

### Criterion 2: Code Fundamentals - Functions, Loops & Error Handling (5 pts, 20%)
**Canvas Description Field:** Lab 4.1 script is reused cleanly with error handling preserved, integration point is clear, and evidence shows script runs clean when invoked by scheduler.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 5 | Lab 4.1 script reused cleanly. Error handling from Lab 4.1 still in place. Comments explain integration point for scheduler. Evidence script runs clean when invoked by scheduler. |
| Good | 3 | Lab 4.1 script reused; minor cleanup; error handling mostly preserved. |
| Unacceptable | 0 | Script broken when integrated with scheduler. |

### Criterion 3: Scheduling Configuration (10 pts, 40%)
**Canvas Description Field:** Cron job (Linux) or Task Scheduler (Windows) is correctly configured with accurate syntax, correct frequency, and clear documentation showing the configuration.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 10 | Cron job (Linux) or Task Scheduler (Windows) entry correctly configured. Syntax is correct. Frequency is accurate (every 5 minutes as specified). Screenshot or export shows configuration clearly. |
| Good | 6 | Configuration present and mostly correct; minor syntax issues or frequency off. |
| Unacceptable | 0 | Configuration missing or broken; scheduler won't run script. |

### Criterion 4: Testing Evidence - Automatic Execution (6 pts, 24%)
**Canvas Description Field:** Log file shows multiple automatic runs with timestamps spaced appropriately, output is consistent across runs, and evidence proves script executes reliably on schedule.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 6 | Log file shows at least 3 automatic runs with timestamps proving unattended execution. Timestamps are spaced ~5 minutes apart. Output consistent across runs. Evidence proves script runs reliably on schedule. |
| Good | 4 | Log shows 2 automatic runs; timestamps mostly correct; output mostly consistent. |
| Unacceptable | 0 | Missing log evidence or only 1 run shown. |

---

## Lab 4.3: Production Hardening (50 points)

### Criterion 1: Well Formatted Document (8 pts, 16%)
**Canvas Description Field:** Submission is professionally formatted with clear identification, organized sections, labeled screenshots of alert firing and cross-platform output, and clear setup instructions.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 8 | Complete identification. All sections titled. Screenshots of alert firing, retry sequence, and cross-platform output labeled. Setup instructions clear. |
| Good | 5 | Identification present; sections organized; most screenshots labeled. |
| Unacceptable | 0 | Missing identification or disorganized. |

### Criterion 2: Code Fundamentals - Functions, Loops & Error Handling (8 pts, 16%)
**Canvas Description Field:** Code is organized with reusable functions, uses loops to iterate over services and retry attempts, includes comprehensive error handling, and is well-commented.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 8 | Script uses functions to organize: check_service, attempt_restart_with_backoff, send_alert, query_cross_platform. Loops iterate over services and retry attempts. Error handling comprehensive (try/except on all external calls). Comments explain function purpose. |
| Good | 5 | Functions present; loops used; error handling present; organization could be better. |
| Unacceptable | 0 | Minimal functions/loops/error handling. |

### Criterion 3: Escalating Alerts & Alerting Mechanism (15 pts, 30%)
**Canvas Description Field:** Alerts fire correctly after specified failure count, include service name and failure details with log context, testing evidence shows alerts fired during test run, and alerts integrate with email or Slack.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 15 | Alerts fire correctly after specified failure count (3 failures = first alert, 5+ = escalation). Alert includes service name, failure details, log context. Testing evidence shows alert fired during test run. Alerts go to email or Slack (documented). |
| Good | 10 | Alert mechanism present; fires after repeated failures; most context included; implementation could be cleaner. |
| Unacceptable | 0 | No alert mechanism or alerts don't fire. |

### Criterion 4: Cross-Platform Monitoring & Integration (12 pts, 24%)
**Canvas Description Field:** Script queries both Windows Server VMs and WSL2 Linux services, generates unified report showing status of both platforms, and handles platform-specific errors appropriately.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 12 | Script queries both Windows Server VMs (via WMI or remote PowerShell) and WSL2 Linux services (via subprocess/SSH). Generates unified report showing status of both platforms. Handles platform-specific errors appropriately. |
| Good | 8 | Both platforms queried; unified view attempted; 1-2 platform-specific issues; error handling mostly present. |
| Unacceptable | 0 | Only one platform monitored or cross-platform integration broken. |

### Criterion 5: Testing Evidence & Production Readiness (7 pts, 14%)
**Canvas Description Field:** Evidence shows testing of alert firing, retry sequences with backoff delays, and cross-platform output; script is documented as production-ready with explanation of production-grade additions.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 7 | Evidence of testing: alert fired (screenshot), retry sequence shown (log with backoff delays), cross-platform output shown (both Windows and Linux services). Script documented as production-ready. Documentation explains production-grade additions (150-200 words). |
| Good | 5 | Most testing evidence present; documentation partially complete. |
| Unacceptable | 0 | Missing testing evidence or documentation. |

---

## Lab 5.1: Performance Baseline & Trending (100 points)

### Criterion 1: Well Formatted Document (16 pts, 16%)
**Canvas Description Field:** Submission is professionally formatted with clear identification including date, organized sections with titles, included visualizations (graphs or tables) labeled and referenced, and professional presentation throughout.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 16 | Complete identification and date. All sections titled and organized. Visualizations (graphs/tables) included and labeled. Data file references clear. Professional formatting throughout. |
| Good | 11 | Identification present; sections mostly titled; visualizations present; minor formatting issues. |
| Unacceptable | 0 | Missing identification or disorganized. Visualizations missing. |

### Criterion 2: Code Fundamentals - Functions, Loops & Error Handling (12 pts, 12%)
**Canvas Description Field:** Collection scripts use functions to organize logic, loops iterate over time intervals and data collection cycles, error handling validates data collection, and code is well-commented.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 12 | Collection scripts use functions to organize collection logic (separate functions for CPU, memory, disk, network). Loops iterate over time intervals and data collection cycles. Error handling validates data collection (checks if commands succeeded before using output). Comments explain function purpose. |
| Good | 8 | Functions present; loops used for collection cycles; error handling on most calls; organization could be stronger. |
| Unacceptable | 0 | Minimal functions/loops. No error handling. |

### Criterion 3: Data Collection & Aggregation (25 pts, 25%)
**Canvas Description Field:** Metrics are collected over 24-48+ hours at regular intervals, include CPU, memory, disk, and network data in structured format (CSV, JSON), with complete and consistent collection showing no gaps.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 25 | Metrics collected over 24-48+ hours at regular intervals (5-10 minute samples). CPU, memory, disk, network data collected. Data stored in structured format (CSV, JSON). Collection consistent and complete. No gaps in data timeline. |
| Good | 17 | Metrics collected over 24 hours; most metrics present; data structured; 1-2 gaps or inconsistencies. |
| Unacceptable | 0 | Data collection incomplete, unstructured, or insufficient duration. |

### Criterion 4: Analysis Quality & Trend Identification (20 pts, 20%)
**Canvas Description Field:** Calculations are correct (average, min, max, trend), capacity risks are identified accurately, performance degradation is detected when present, visualizations clearly show trends, and recommendations are specific and justified.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 20 | Correct calculations: average, min, max, trend direction. Capacity risks identified correctly (approaching 80% thresholds). Performance degradation identified when present. Visualizations (graphs or tables) clearly show trends. Recommendations specific and justified. |
| Good | 14 | Most calculations correct; trends identified; visualizations present; recommendations could be more specific. |
| Unacceptable | 0 | Calculations incorrect or incomplete. Trends not identified. |

### Criterion 5: Tool Selection Documentation & Comparative Analysis (15 pts, 15%)
**Canvas Description Field:** For each component (collection, aggregation, analysis), explains language choice and rationale, documents trade-offs of each language, provides code examples of alternative approaches, and demonstrates deep understanding of when to use each tool.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 15 | For each component (collection, aggregation, analysis), explains which language chosen and why. Documents trade-offs: bash efficiency vs. limits, PowerShell Windows-native but verbose, Python readable but requires dependencies. Shows code examples for alternative approaches (even if not used). Comparison thoughtful and demonstrates deep understanding. |
| Good | 10 | Tool selection explained for most components. Trade-offs discussed. Some comparative code examples. Understanding evident. |
| Unacceptable | 0 | Tool selection not explained or incomplete. No trade-off discussion. |

### Criterion 6: Testing Evidence & Production Reflection (12 pts, 12%)
**Canvas Description Field:** Evidence shows successful data collection over required time period and accurate analysis output, with reflection addressing learning about tool selection, when to use each language, and how this relates to production infrastructure.

**Canvas Rating Levels:**

| Level | Points | Rating Description |
|-------|--------|-------------------|
| Excellent | 12 | Evidence of testing: data collection ran successfully over required time, analysis produced correct output. Reflection addresses: what you learned about tool selection for different jobs, when you'd use each language for similar work, how this relates to production infrastructure. 150-200+ words. |
| Good | 8 | Testing evidence present (screenshots, data, output). Reflection addresses most questions; 100-150 words. |
| Unacceptable | 0 | Missing testing evidence or reflection under 100 words. |

---

## Summary: Point Distribution Across All Labs

| Lab | Well Formatted | Code Fundamentals | Task-Specific | Total |
|-----|---|---|---|---|
| 1.1 | 5 (20%) | — | 20 (80%) | 25 |
| 1.2 | 4 (16%) | 8 (32%) | 13 (52%) | 25 |
| 1.3 | 16 (16%) | 10 (10%) | 74 (74%) | 100 |
| 2.1 | 8 (16%) | 8 (16%) | 34 (68%) | 50 |
| 3.1 | 16 (16%) | 10 (10%) | 74 (74%) | 100 |
| 4.1 | 8 (16%) | 8 (16%) | 34 (68%) | 50 |
| 4.2 | 4 (16%) | 5 (20%) | 16 (64%) | 25 |
| 4.3 | 8 (16%) | 8 (16%) | 34 (68%) | 50 |
| 5.1 | 16 (16%) | 12 (12%) | 72 (72%) | 100 |

---

## Canvas UI Entry Instructions

For EACH criterion:

1. **Criterion Name** (from section heading, e.g., "Well Formatted Document")
2. **Criterion Description** (from "Canvas Description Field" line)
3. **Points Possible** (from heading, e.g., "5 pts")
4. **Enable Range:** Check box
5. **Rating Levels:** Add three levels using the table:
   - **Display:** Start (e.g., "2" for Excellent 5-pt range)
   - **Point Range:** (e.g., ">3 to 5" for the range)
   - **Rating Name:** (e.g., "Excellent")
   - **Rating Description:** (from table column)

All information needed for one complete Canvas rubric criterion is on this page. No cross-referencing required.

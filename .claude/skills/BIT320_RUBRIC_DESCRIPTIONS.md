---
name: bit320-rubric-descriptions
description: Criterion descriptions for all BIT320 rubrics, formatted for Canvas UI "Criterion Description" field. Separate from rating-level descriptions.
---

# BIT320 Criterion Descriptions (Canvas UI Format)

Use these descriptions in the **"Criterion Description"** field when creating/editing rubrics in Canvas. They explain what each criterion measures overall.

---

## Lab 1.1: Infrastructure Setup

**Well Formatted Document:** Submission is professionally formatted with clear identification, organized sections, and labeled deliverables.

**Environment Installation:** All three scripting environments (bash via WSL2, Python 3.10+, PowerShell) are successfully installed and functional.

**Verification & Testing:** Version checks and test commands confirm that all three environments are working correctly and ready for use.

---

## Lab 1.2: System Command Execution

**Well Formatted Document:** Submission is professionally formatted with clear identification, organized sections with titles, and labeled screenshots showing script output from each language.

**Code Fundamentals - Functions, Loops & Error Handling:** Code is organized with reusable functions, uses loops to iterate over data, includes error handling to validate operations, and is well-commented.

**Script Functionality:** All three scripts (bash, PowerShell, Python) execute successfully and produce output demonstrating that each language can interact with the operating system.

**Comparative Analysis & Language Understanding:** Analysis thoughtfully compares how each language handles system commands, demonstrates understanding of paradigm differences, and explains why languages have different approaches.

---

## Lab 1.3: Log Analysis Starter

**Well Formatted Document:** Submission is professionally formatted with clear identification, organized sections, labeled screenshots and outputs, and a well-organized comparison table.

**Code Fundamentals - Functions, Loops & Error Handling:** Code is organized with reusable functions, uses loops to process data, includes error handling to validate file operations, and is well-commented.

**Script Implementation - All Three Languages:** All three scripts (bash, PowerShell, Python) execute successfully and correctly analyze log files, counting entries by severity level and identifying top error messages.

**Comparative Analysis & Tool Selection:** Completed comparison table with thoughtful observations about differences in lines of code, readability, execution time, natural fit for the task, ease of understanding, and paradigm approach.

**Testing Evidence & Reflection:** Clear evidence of testing all three scripts successfully, with reflection addressing which language felt natural, fastest to write, most readable, and which you would use for different scenarios.

---

## Lab 2.1: Log Summary Script

**Well Formatted Document:** Submission is professionally formatted with clear identification, organized sections, labeled screenshots showing script output, and the script code clearly presented.

**Code Fundamentals - Functions, Loops & Error Handling:** Code is organized with reusable functions, uses loops to iterate over error entries, includes error handling to validate file operations, and is well-commented.

**Bash Mastery & Text Processing:** Script demonstrates bash strength using grep, awk, sort, and uniq appropriately, with efficient pipelines that correctly categorize errors and identify top error messages.

**Code Quality & Output:** Script is readable with clear variable names and comments, produces professional and actionable output with all required information, and executes reliably.

---

## Lab 3.1: Windows Event Log Audit

**Well Formatted Document:** Submission is professionally formatted with clear identification, organized sections with titled areas, labeled screenshots and outputs, and a professional security audit report.

**Code Fundamentals - Functions, Loops & Error Handling:** Code is organized with reusable functions, uses loops to iterate over event collections, includes error handling to validate Get-EventLog calls, and is well-commented.

**PowerShell Object Pipeline Mastery:** Script correctly uses Get-EventLog, Where-Object, Group-Object, and Select-Object with efficient object pipelines to query and analyze Windows Security Event Log.

**Error Handling & Report Quality:** Script handles cases where events are not found, permissions are denied, or logs are unavailable, and generates a professional report with required sections and accurate, actionable findings.

**Security Analysis & Comparative Insight:** Red flags are correctly identified (admin failures, brute-force patterns, unusual activity), analysis demonstrates security understanding, and optional comparison explains why PowerShell excels for this task.

---

## Lab 4.1: Service Monitoring in Python

**Well Formatted Document:** Submission is professionally formatted with clear identification, organized sections, labeled screenshots of test runs, and included log file excerpts.

**Code Fundamentals - Functions, Loops & Error Handling:** Code is organized with reusable functions for distinct tasks, uses loops to iterate over services, includes try/except blocks for all external operations, and is well-commented.

**Error Handling - Graceful Recovery:** Script handles multiple distinct error scenarios (permission denied, service not found, timeout), uses try/except appropriately, degrades gracefully without crashing, and provides meaningful error messages.

**Structured Logging & Production Readiness:** Every action is logged with timestamps and status, log entries include service, status, and outcome, test evidence shows multiple runs, and script could run unattended in production.

---

## Lab 4.2: Scheduled Automation

**Well Formatted Document:** Submission is professionally formatted with clear identification, organized sections, labeled screenshots of scheduling configuration and logs, and clear setup instructions.

**Code Fundamentals - Functions, Loops & Error Handling:** Lab 4.1 script is reused cleanly with error handling preserved, integration point is clear, and evidence shows script runs cleanly when invoked by the scheduler.

**Scheduling Configuration:** Cron job (Linux) or Task Scheduler (Windows) is correctly configured with accurate syntax, correct frequency, and clear documentation showing the configuration.

**Testing Evidence - Automatic Execution:** Log file shows multiple automatic runs with timestamps spaced appropriately, output is consistent across runs, and evidence proves script executes reliably on schedule without manual intervention.

---

## Lab 4.3: Production Hardening

**Well Formatted Document:** Submission is professionally formatted with clear identification, organized sections with titles, labeled screenshots showing alert firing and cross-platform output, and clear setup instructions.

**Code Fundamentals - Functions, Loops & Error Handling:** Code is organized with reusable functions for specific tasks, uses loops to iterate over services and retry attempts, includes comprehensive error handling with try/except on all external calls, and is well-commented.

**Escalating Alerts & Alerting Mechanism:** Script fires alerts correctly after specified failure count, alerts include service name and failure details with log context, testing evidence shows alerts fired during test runs, and alerts integrate with email or Slack.

**Cross-Platform Monitoring & Integration:** Script queries both Windows Server VMs and WSL2 Linux services, generates a unified report showing status of both platforms, and handles platform-specific errors appropriately.

**Testing Evidence & Production Readiness:** Evidence shows testing of alert firing, retry sequences with backoff delays, and cross-platform output; script is documented as production-ready with explanation of production-grade additions.

---

## Lab 5.1: Performance Baseline & Trending

**Well Formatted Document:** Submission is professionally formatted with clear identification including date, organized sections with titles, included visualizations (graphs or tables) labeled and referenced, and professional presentation throughout.

**Code Fundamentals - Functions, Loops & Error Handling:** Collection scripts use functions to organize logic, loops iterate over time intervals and data collection cycles, error handling validates that data collection succeeded, and code is well-commented.

**Data Collection & Aggregation:** Metrics are collected over 24-48+ hours at regular intervals, include CPU, memory, disk, and network data in structured format (CSV, JSON), with complete and consistent collection showing no gaps.

**Analysis Quality & Trend Identification:** Calculations are correct (average, min, max, trend), capacity risks are identified accurately, performance degradation is detected when present, visualizations clearly show trends, and recommendations are specific and justified.

**Tool Selection Documentation & Comparative Analysis:** For each component (collection, aggregation, analysis), explains language choice and rationale, documents trade-offs of each language, provides code examples of alternative approaches, and demonstrates deep understanding of when to use each tool.

**Testing Evidence & Production Reflection:** Evidence shows successful data collection over required time period and accurate analysis output, reflection addresses learning about tool selection, when to use each language, and how this relates to production infrastructure.

---

## Implementation Instructions

When creating/editing each rubric criterion in Canvas UI:

1. **Criterion Name:** Copy the criterion name (e.g., "Well Formatted Document")
2. **Criterion Description:** Copy the description from this document
3. **Points Possible:** Enter the point value (5, 8, 10, etc.)
4. **Enable Range:** Check the "Enable Range" box
5. **Rating Levels:** Add three rating levels (Excellent, Good, Unacceptable) with point ranges and descriptions from BIT320_RUBRICS_COMPLETE.md

Example Canvas Entry:
- Name: "Code Fundamentals - Functions, Loops & Error Handling"
- Description: "Code is organized with reusable functions, uses loops to process data, includes error handling to validate operations, and is well-commented."
- Points: 8
- Ranges: 
  - Excellent: >6 to 8 [description from COMPLETE file]
  - Good: >3 to 6 [description from COMPLETE file]
  - Unacceptable: -- to 0 [description from COMPLETE file]

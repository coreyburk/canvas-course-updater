# Lab 5.1 Final Project - Instructor Reference Implementations

Lab 5.1 lets students pick one of three options and any of three languages, so
there are nine legitimate shapes a correct submission can take. These are not
the answer; they are one worked example per option, so a grader can see what
complete looks like. **Expect correct work that looks nothing like these.**

Published to the instructor-only module on 2026-11-09 as
"Lab 5.1 Answer Keys and Grading Guide - All Three Options".

| File | Option | Language |
|---|---|---|
| `Option_A_monitor.ps1` | Service health monitoring and auto-remediation | PowerShell |
| `Option_B_audit.ps1` | Configuration compliance auditing | PowerShell |
| `Option_C_analyze.py` | Windows event log analysis | Python |

`services.json` and `baseline.json` are the config files A and B read.

## Verified

All three were executed before publication.

- **Option A** ran against a real service list on Windows, correctly reporting
  two running services and flagging a non-existent one. Use `-DryRun` to
  exercise every path without touching a service. **Limit:** the recovery
  branch was exercised in dry run, not against a genuinely failed service.
- **Option B** audited a six-item baseline and reported 83.3 percent compliance
  with the one critical deviation named.
- **Option C** parsed three synthetic CSV exports and answered all five
  questions including the hourly error histogram.

## The one thing each option is really testing

- **A: the verify step.** A restart command returning without error does not
  mean the service came up. Re-checking afterwards is the requirement students
  most often miss.
- **B: that the baseline is data.** If changing the standard means editing the
  script, they wrote a checklist with extra steps rather than an audit tool.
- **C: timestamp parsing.** Windows exports dates in a locale-dependent format,
  so a format string that worked for one student may fail for another.

## Note on exit codes

`Option_A_monitor.ps1` exits non-zero when a service is left unhealthy. That is
deliberate and is what makes a monitor usable from Task Scheduler or cron. A
student script that always exits 0 is worth a comment.

## Structural issue flagged

Lab 5.1 Option C and Lab 5.2 are the same project: both Windows event log
analysis, both 100 points, both due 2026-12-10. Either retire Lab 5.2 or drop
Option C from Lab 5.1. Not resolved as of 2026-11-09.

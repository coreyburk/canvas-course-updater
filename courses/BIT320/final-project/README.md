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

## The duplicate final, resolved 2026-11-09

Lab 5.2 covered the same Windows event log analysis as Option C, for the same
100 points on the same due date. It is now renamed `RETIRED - Lab 5.2`, carries
a banner explaining why, and stays unpublished and in no module. Kept rather
than deleted so its history and rubric remain available.

**Its export script moved to the Option C page first, because Option C needed
it.** Option C asks which of System, Security and Application is most active,
but its own snippet exported only System and Application. That question was
unanswerable from the data students were told to collect.

`Export-EventLogs.ps1` here is the migrated script.

## The encoding bug in that script

As published it contained one tick character, U+2713, in a progress message.
Saved as UTF-8 without a byte order mark, which is the VS Code and Notepad
default, and run under Windows PowerShell 5.1, those bytes are read as the
system codepage and the tick becomes a left smart quote. PowerShell accepts
smart quotes as string delimiters, so the script opens a string that never
closes and fails with:

```
The string is missing the terminator: ".
```

pointing at a line that is perfectly fine. It works in PowerShell 7, which
assumes UTF-8, so it looks machine-dependent rather than wrong.

Verified: with a BOM it parses, without one it does not, and after replacing
the tick with `[OK]` it parses either way. The copy here is pure ASCII.

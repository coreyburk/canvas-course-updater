---
name: code-quality-checklist
description: One-page reference checklist for all BIT320 scripts. Required for Week 1-5 assignments to enforce production-ready code standards progressively.
---

# BIT320 Code Quality Checklist

**Use this checklist before submitting any script.** Your rubric includes scoring on these elements.

## ✓ Code Organization (All scripts)

- [ ] **Functions defined:** Code organized into reusable functions (not all procedural)
- [ ] **Function names clear:** Function names describe what they do (get_hostname, check_disk_usage, process_log_entry)
- [ ] **Single responsibility:** Each function does one thing well
- [ ] **DRY principle:** No copy-pasted code; repeated logic extracted to functions

## ✓ Error Handling (Progressive requirement)

**Week 1-2:** Basic checks
- [ ] Commands validated before using output (bash: `|| exit`, PowerShell: error checks, Python: try/except)
- [ ] Graceful failure: Script doesn't crash; errors are logged or reported

**Week 3-4:** Structured recovery
- [ ] Try/except blocks (Python) or error trapping (PowerShell/bash)
- [ ] Retry logic on transient failures (attempt twice before giving up)
- [ ] Meaningful error messages (not just "Error")

**Week 5:** Production patterns
- [ ] Logging: All actions logged with timestamps
- [ ] Escalation: Repeated failures trigger alerts
- [ ] Rollback: Failed operations don't leave system in bad state

## ✓ Readability & Maintenance

- [ ] Comments on functions explaining purpose (one line per function minimum)
- [ ] Variable names meaningful (not `x`, `temp`, `d1`)
- [ ] Consistent indentation (spaces or tabs, not mixed)
- [ ] No magic numbers: Use named constants instead of inline values

## ✓ Documentation

- [ ] Script header comment: Filename, purpose, author, date
- [ ] Usage comment if script accepts parameters (e.g., `./script.sh <hostname>`)
- [ ] Complex logic commented (why, not what)

## ✓ Testing Evidence

- [ ] Script runs without errors on your system
- [ ] Output is correct for typical input
- [ ] Error case tested (e.g., file doesn't exist, permission denied)
- [ ] Screenshot or log showing test run

## Quick Self-Review (Before Submitting)

```
Does my script have:
□ At least 2-3 functions? (organized, not procedural)
□ A loop to process data? (not hardcoded for one item)
□ Error handling for failure cases? (doesn't crash)
□ Comments on functions and complex logic?
□ Meaningful variable names?
□ Test evidence showing it works?
```

If all checked: Ready to submit.  
If any unchecked: Refactor before submitting.

---

**Why this matters:** Production scripts fail silently without error handling, duplicate code when not using functions, and break when environments change. This checklist prevents those problems.

**Progressive:** Week 1-2 focus on functions/loops/basic errors. Week 3-4 add structured recovery. Week 5 add logging/alerting.

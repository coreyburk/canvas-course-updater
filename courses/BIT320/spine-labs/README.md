# Spine Labs - Reference Solutions

The same log analysis, solved three times: Lab 1.3 (bash), Lab 2.1 (PowerShell),
Lab 3.1 (Python). These are the answer keys published to the instructor-only
module on 2026-11-09, kept here so the course content has a versioned source.

**These are instructor material.** The student assignments no longer contain
them; students compose the pipelines themselves from the named tools and the
week's teaching pages.

## Verified, not assumed

All three were executed against `analysis.log` in this folder before being
published. They agree:

| | Result |
|---|---|
| Total entries | 10 |
| ERROR entries | 6 (60%) |
| Components | auth-service 3, db-connector 2, scheduler 1 |

`analysis.log` is synthetic, built to the course's documented format
(`TIMESTAMP | LEVEL | COMPONENT | MESSAGE`) **with the space padding** that the
labs keep warning about, so a solution that forgets to trim will visibly produce
wrong counts against it.

Running all three against a student's own `analysis.log` is the quickest way to
settle a disputed number.

## One real trap, found by running them

`bc` is **not installed by default** on current Ubuntu images, including WSL2.
The bash solution uses it for the error percentage, so on a clean machine the
percentage silently prints as empty:

```
Total errors: 6 (%)
```

A student hitting this has an environment problem, not a code problem. Either:

```bash
sudo apt install bc
```

or compute it with awk, which is always present:

```bash
ERROR_PERCENTAGE=$(awk "BEGIN {printf \"%.1f\", ($TOTAL_ERRORS*100)/$TOTAL_LINES}")
```

The scripts here are left faithful to what the course taught rather than quietly
corrected, so they match the reference an instructor is grading against. The
answer key pages flag the issue prominently.

## Ties order differently between languages

On this data two messages both occur twice. bash and Python list one first,
PowerShell the other. Do not mark a student down for the ordering of equal
counts.

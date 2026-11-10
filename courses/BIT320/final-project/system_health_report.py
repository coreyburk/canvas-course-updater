#!/usr/bin/env python3
"""Lab 5.1 Option C - Windows Event Log Analysis
Instructor reference implementation.

Reads the three CSVs produced by Export-EventLogs.ps1 and answers the five
questions. Nothing here is Windows-specific beyond the column names, so it runs
anywhere for grading against a student's exported data.
"""

import csv
import os
import sys
from collections import Counter
from datetime import datetime

CSV_FILES = ["system.csv", "security.csv", "application.csv"]
REPORT = "event_log_report.txt"


def load_events(filenames):
    """Returns (events, problems). A missing or malformed file is reported
    rather than silently skipped, because a student grading question is often
    'why is my count low'."""
    events, problems = [], []

    for name in filenames:
        if not os.path.exists(name):
            problems.append("%s: not found" % name)
            continue
        try:
            with open(name, newline="", encoding="utf-8-sig") as f:
                rows = list(csv.DictReader(f))
        except Exception as err:
            problems.append("%s: unreadable (%s)" % (name, err))
            continue
        for row in rows:
            row["_log"] = name.replace(".csv", "")
            events.append(row)

    return events, problems


def get(row, *names):
    """Column names vary between exports. Try several, return '' if none fit."""
    for n in names:
        if row.get(n):
            return row[n].strip()
    return ""


def parse_hour(stamp):
    for fmt in ("%Y-%m-%d %H:%M:%S", "%m/%d/%Y %I:%M:%S %p", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(stamp[:19], fmt).hour
        except ValueError:
            continue
    return None


def main():
    events, problems = load_events(CSV_FILES)
    if not events:
        print("No events loaded. Problems:")
        for p in problems:
            print("  " + p)
        return 1

    levels = Counter(get(e, "Level", "LevelDisplayName") or "Unknown" for e in events)
    total = len(events)
    errors = levels.get("Error", 0)
    warnings = levels.get("Warning", 0)

    sources = Counter(get(e, "Source", "ProviderName", "Component")
                      for e in events
                      if get(e, "Level", "LevelDisplayName") == "Error")

    hours = Counter()
    undated = 0
    for e in events:
        if get(e, "Level", "LevelDisplayName") != "Error":
            continue
        h = parse_hour(get(e, "Timestamp", "TimeCreated"))
        if h is None:
            undated += 1
        else:
            hours[h] += 1

    pct = lambda n: (n / total * 100) if total else 0

    out = []
    out.append("=" * 40)
    out.append("Windows Event Log Analysis Report")
    out.append("=" * 40)
    out.append("Generated: %s" % datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    out.append("Logs read: %s" % ", ".join(sorted({e["_log"] for e in events})))
    if problems:
        out.append("")
        out.append("NOTE: %d input problem(s):" % len(problems))
        out.extend("  " + p for p in problems)
    out.append("")
    out.append("QUESTION 1: Event type distribution")
    for level, count in levels.most_common():
        out.append("  %-14s %5d  (%.1f%%)" % (level, count, pct(count)))
    out.append("  %-14s %5d" % ("TOTAL", total))
    out.append("")
    out.append("QUESTION 2: Error and warning rate")
    out.append("  Errors:   %d (%.1f%%)" % (errors, pct(errors)))
    out.append("  Warnings: %d (%.1f%%)" % (warnings, pct(warnings)))
    out.append("")
    out.append("QUESTION 3: Top 5 error sources")
    if sources:
        for i, (src, count) in enumerate(sources.most_common(5), 1):
            out.append("  %d. %-34s %d" % (i, (src or "(blank)")[:34], count))
    else:
        out.append("  No error events found.")
    out.append("")
    out.append("QUESTION 4: When do errors happen?")
    if hours:
        busiest = hours.most_common(1)[0]
        for h in sorted(hours):
            bar = "#" * min(hours[h], 40)
            out.append("  %02d:00  %3d  %s" % (h, hours[h], bar))
        out.append("  Busiest hour: %02d:00 with %d errors" % busiest)
    else:
        out.append("  No parseable error timestamps.")
    if undated:
        out.append("  (%d error events had an unrecognised timestamp format)" % undated)
    out.append("")
    out.append("QUESTION 5: Stability assessment")
    rate = pct(errors)
    verdict = ("stable" if rate < 5 else
               "some instability" if rate < 15 else "unstable")
    out.append("  Error rate of %.1f%% suggests: %s" % (rate, verdict))
    out.append("  [Student writes 50-100 words grounded in the numbers above]")
    out.append("")
    out.append("=" * 40)

    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("\n".join(out))
    print("\nReport saved to %s" % REPORT)
    return 0


if __name__ == "__main__":
    sys.exit(main())

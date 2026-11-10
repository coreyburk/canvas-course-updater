# Lab 5.1 Final Project - System Health Report

One project, three languages. Every student builds the same thing: a script
that reads their own exported Windows Event Logs and prints a system health
report. They choose bash, PowerShell or Python, and justify the choice.

| File | What it is |
|---|---|
| `Export-EventLogs.ps1` | Provided to students. Exports 7 days of System, Security and Application logs to three CSVs. Everyone runs this regardless of language. |
| `system_health_report.py` | Instructor reference implementation. Python, because it is shortest to read. |
| `retired/` | The two discarded options, kept for reference. |

## Why one project rather than three

The course's theme is choosing the right tool, and the **language** choice
delivers that. Students have written the same kind of script in all three
languages and justify their pick in the rubric's Tool Selection criterion.

A second axis of choice, between three different projects, added no pedagogical
value and created two problems:

1. **Unequal load.** Counting new interfaces, demands beyond the spine labs, and
   artefacts produced, the service-monitoring and compliance-auditing options
   carried roughly 2.3 times the event-log option's complexity. Only the
   event-log project was a slight progression from the spine labs.
2. **It was not a free choice.** Querying Windows services, firewall rules or
   security settings from WSL bash means shelling out to `powershell.exe`. The
   other two options quietly forced PowerShell, so a student who concluded in
   Lab 4.1 that Python suited them would have had to abandon that conclusion.

## Why this project is language-neutral, verified

The exported CSV has commas and quotes inside the Message column, so `awk -F,`
sees five or six fields on a row that should have four. That looks fatal for
bash, but **all five report items read fields 1 to 3** (Timestamp, Level,
Source) and the commas only appear in field 4. Plain awk extracts Source
correctly on every row, and the counting pipeline from the spine labs gives the
right answer. Tested, not assumed.

## The report the script must produce

1. Which log is busiest: System, Security or Application.
2. The error rate: errors, warnings and informational counts, with percentages.
3. The worst error sources, ranked.
4. Errors grouped by hour of the day.
5. Two or three sentences on whether the machine looks healthy.

The first four come out of the data. The fifth is the student's own, and it is
where you find out whether they understand what they built.

## Known trap in the export script

It is pure ASCII now, deliberately. It previously contained one `U+2713` tick,
which under Windows PowerShell 5.1 reading a BOM-less UTF-8 file decoded into a
left smart quote, which PowerShell treats as a string delimiter. The script
failed with "the string is missing the terminator" pointing at a line that was
fine, and worked in PowerShell 7, so it looked machine-specific. Keep it ASCII.

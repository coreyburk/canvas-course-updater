#!/usr/bin/env python3
# Log Analysis Script (Python)
# Analyzes a log file using Python data structures

import time
from collections import Counter

LOG_FILE = "analysis.log"
REPORT_FILE = "python_analysis_report.txt"

start_time = time.time()

def parse_log(filename):
    entries = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split('|')
            if len(parts) >= 4:
                entries.append({
                    'timestamp': parts[0].strip(),
                    'level': parts[1].strip(),
                    'component': parts[2].strip(),
                    'message': parts[3].strip()
                })
    return entries

log_entries = parse_log(LOG_FILE)

total_lines = len(log_entries)
total_errors = len([e for e in log_entries if e['level'] == 'ERROR'])
error_percentage = round((total_errors / total_lines) * 100, 1)

errors_by_component = {}
for entry in log_entries:
    if entry['level'] == 'ERROR':
        component = entry['component']
        errors_by_component[component] = errors_by_component.get(component, 0) + 1

sorted_components = sorted(errors_by_component.items(), key=lambda x: x[1], reverse=True)

error_messages = [e['message'] for e in log_entries if e['level'] == 'ERROR']
top_errors = Counter(error_messages).most_common(10)

first_entry = log_entries[0]['timestamp'] if log_entries else "N/A"
last_entry = log_entries[-1]['timestamp'] if log_entries else "N/A"

end_time = time.time()
elapsed = end_time - start_time

report = f"""========================================
Log Analysis Report
========================================
Analysis Date: {time.strftime('%Y-%m-%d %H:%M:%S')}

QUESTION 1: Total Entries and Errors
Total entries: {total_lines}
Total errors: {total_errors} ({error_percentage}%)

QUESTION 2: Components with Errors
"""

for component, count in sorted_components:
    report += f"\n  {component}: {count} errors"

report += "\n\nQUESTION 3: Most Common Error Messages\n"

for idx, (message, count) in enumerate(top_errors, 1):
    report += f"\n  {idx}. {message} ({count} times)"

report += f"""

QUESTION 4: Timeline
  Started: {first_entry}
  Ended: {last_entry}

QUESTION 5: Observations
  [Write 50-100 word observation about patterns in the data]

Script execution time: {elapsed:.3f} seconds
========================================
"""

with open(REPORT_FILE, 'w') as f:
    f.write(report)

print(f"Report saved to {REPORT_FILE}")

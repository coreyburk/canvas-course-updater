#!/bin/bash
# Log Analysis Script (Bash)
# Analyzes a log file using bash text pipelines

LOGFILE="analysis.log"
REPORTFILE="bash_analysis_report.txt"

START_TIME=$(date +%s.%N)

TOTAL_LINES=$(wc -l < "$LOGFILE")
TOTAL_ERRORS=$(grep -c " ERROR " "$LOGFILE")
ERROR_PERCENTAGE=$(echo "scale=1; ($TOTAL_ERRORS * 100) / $TOTAL_LINES" | bc)

ERRORS_BY_COMPONENT=$(grep " ERROR " "$LOGFILE" | awk -F'|' '{print $3}' | sed 's/^ *//;s/ *$//' | sort | uniq -c | sort -rn)

TOP_ERRORS=$(grep " ERROR " "$LOGFILE" | awk -F'|' '{print $4}' | sed 's/^ *//;s/ *$//' | sort | uniq -c | sort -rn | head -10)

FIRST_ENTRY=$(head -1 "$LOGFILE" | awk -F'|' '{print $1}' | sed 's/^ *//;s/ *$//')
LAST_ENTRY=$(tail -1 "$LOGFILE" | awk -F'|' '{print $1}' | sed 's/^ *//;s/ *$//')

END_TIME=$(date +%s.%N)
ELAPSED=$(echo "$END_TIME - $START_TIME" | bc)

{
    echo "========================================"
    echo "Log Analysis Report"
    echo "========================================"
    echo "Analysis Date: $(date '+%Y-%m-%d %H:%M:%S')"
    echo ""
    echo "QUESTION 1: Total Entries and Errors"
    echo "Total entries: $TOTAL_LINES"
    echo "Total errors: $TOTAL_ERRORS ($ERROR_PERCENTAGE%)"
    echo ""
    echo "QUESTION 2: Components with Errors"
    echo "$ERRORS_BY_COMPONENT" | awk '{printf "  %s: %s errors\n", $2, $1}'
    echo ""
    echo "QUESTION 3: Most Common Error Messages"
    echo "$TOP_ERRORS" | awk '{count=$1; $1=""; msg=$0; gsub(/^ +/, "", msg); printf "  %d. %s (%d times)\n", NR, msg, count}'
    echo ""
    echo "QUESTION 4: Timeline"
    echo "  Started: $FIRST_ENTRY"
    echo "  Ended: $LAST_ENTRY"
    echo ""
    echo "QUESTION 5: Observations"
    echo "  [Write 50-100 word observation about patterns in the data]"
    echo ""
    echo "Script execution time: $ELAPSED seconds"
    echo "========================================"
} > "$REPORTFILE"

echo "Report saved to $REPORTFILE"

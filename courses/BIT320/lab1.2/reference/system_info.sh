#!/bin/bash
# Lab 1.2 - System Information Report (bash)

# Returns the machine's hostname, or a clear message if the command fails.
get_hostname() {
    hostname 2>/dev/null || echo "UNKNOWN (hostname failed)"
}

# Returns the name of the user running this script.
get_user() {
    whoami 2>/dev/null || echo "UNKNOWN (whoami failed)"
}

# Checks every path in a list and reports whether it exists.
check_paths() {
    local paths=("$HOME" "/tmp" "/var/log" "/not/a/real/path")
    local path
    local count

    for path in "${paths[@]}"; do
        if [ -d "$path" ]; then
            count=$(ls -1 "$path" 2>/dev/null | wc -l)
            echo "  OK       $path ($count items)"
        else
            echo "  MISSING  $path"
        fi
    done
}

# Main report
echo "========================================"
echo "System Information Report"
echo "========================================"
echo "Hostname:          $(get_hostname)"
echo "Current User:      $(get_user)"
echo "Current Directory: $(pwd)"
echo ""
echo "Path Check:"
check_paths
echo ""
echo "========================================"
echo "Report Complete"
echo "========================================"

#!/bin/bash
# Lab 1.2 - System Information Report (bash)
# Fill in each TODO during class. Run the script after every change.

# Returns the machine's hostname, or a clear message if the command fails.
get_hostname() {
    # TODO: run hostname. If it fails, echo a clear fallback instead.
    echo "TODO"
}

# Returns the name of the user running this script.
get_user() {
    # TODO: run whoami, with the same kind of fallback.
    echo "TODO"
}

# Checks every path in a list and reports whether it exists.
check_paths() {
    # TODO 1: build an array of paths to check.
    #         Include one path that does NOT exist.
    # TODO 2: loop over the array.
    # TODO 3: if the path is a directory, print OK and how many items it holds.
    #         Otherwise print MISSING.
    echo "  TODO"
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

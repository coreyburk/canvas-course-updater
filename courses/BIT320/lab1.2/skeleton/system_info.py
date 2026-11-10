#!/usr/bin/env python3
"""Lab 1.2 - System Information Report (Python)
Fill in each TODO during class. Run the script after every change.
"""

import os
import platform
from pathlib import Path


# Returns the machine's hostname, or a clear message if the lookup fails.
def get_hostname():
    # TODO: return platform.node(), guarded with try/except.
    return "TODO"


# Returns the name of the user running this script.
def get_current_user():
    # TODO: read USERNAME or USER from the environment.
    return "TODO"


# Checks every path in a list and reports whether it exists.
def check_paths():
    # TODO 1: build a list of paths to check.
    #         Include one path that does NOT exist.
    # TODO 2: loop over the list.
    # TODO 3: if the path is a directory, print OK and how many items it holds.
    #         Otherwise print MISSING.
    print("  TODO")


# Main report
print("========================================")
print("System Information Report")
print("========================================")
print(f"Hostname:          {get_hostname()}")
print(f"Current User:      {get_current_user()}")
print(f"Current Directory: {os.getcwd()}")
print()
print("Path Check:")
check_paths()
print()
print("========================================")
print("Report Complete")
print("========================================")

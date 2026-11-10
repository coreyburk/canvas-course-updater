#!/usr/bin/env python3
"""Lab 1.2 - System Information Report (Python)"""

import os
import platform
from pathlib import Path


# Returns the machine's hostname, or a clear message if the lookup fails.
def get_hostname():
    try:
        return platform.node() or "UNKNOWN"
    except Exception as err:
        return f"UNKNOWN ({err})"


# Returns the name of the user running this script.
def get_current_user():
    return os.getenv("USERNAME") or os.getenv("USER") or "UNKNOWN"


# Checks every path in a list and reports whether it exists.
def check_paths():
    paths = [
        Path.home(),
        Path(os.getenv("TEMP", "/tmp")),
        Path("/not/a/real/path"),
    ]

    for path in paths:
        try:
            if path.is_dir():
                count = len(list(path.iterdir()))
                print(f"  OK       {path} ({count} items)")
            else:
                print(f"  MISSING  {path}")
        except PermissionError:
            print(f"  DENIED   {path} (no permission to read)")


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

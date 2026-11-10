# Lab 1.2 - System Information Report (PowerShell)
# Fill in each TODO during class. Run the script after every change.

# Returns the machine's hostname, or a clear message if the lookup fails.
function Get-SystemHostname {
    # TODO: return [System.Net.Dns]::GetHostName() inside try/catch.
    "TODO"
}

# Returns the name of the user running this script.
function Get-CurrentUser {
    # TODO: return $env:USERNAME, with a fallback if it is empty.
    "TODO"
}

# Checks every path in a list and reports whether it exists.
function Test-PathList {
    # TODO 1: build an array of paths to check.
    #         Include one path that does NOT exist.
    # TODO 2: loop over the array with foreach.
    # TODO 3: if Test-Path succeeds, print OK and how many items it holds.
    #         Otherwise print MISSING.
    Write-Host "  TODO"
}

# Main report
Write-Host "========================================"
Write-Host "System Information Report"
Write-Host "========================================"
Write-Host "Hostname:          $(Get-SystemHostname)"
Write-Host "Current User:      $(Get-CurrentUser)"
Write-Host "Current Directory: $(Get-Location)"
Write-Host ""
Write-Host "Path Check:"
Test-PathList
Write-Host ""
Write-Host "========================================"
Write-Host "Report Complete"
Write-Host "========================================"

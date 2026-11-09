# Lab 1.2 - System Information Report (PowerShell)

# Returns the machine's hostname, or a clear message if the lookup fails.
function Get-SystemHostname {
    try {
        [System.Net.Dns]::GetHostName()
    }
    catch {
        "UNKNOWN (hostname lookup failed)"
    }
}

# Returns the name of the user running this script.
function Get-CurrentUser {
    if ($env:USERNAME) { $env:USERNAME } else { "UNKNOWN" }
}

# Checks every path in a list and reports whether it exists.
function Test-PathList {
    $paths = @($env:USERPROFILE, $env:TEMP, "C:\Windows", "C:\not\a\real\path")

    foreach ($path in $paths) {
        if (Test-Path -Path $path) {
            $count = @(Get-ChildItem -Path $path -Force -ErrorAction SilentlyContinue).Count
            Write-Host "  OK       $path ($count items)"
        }
        else {
            Write-Host "  MISSING  $path"
        }
    }
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

# Lab 5.1 Option A - Service Health Monitoring and Auto-Remediation
# Instructor reference implementation.
#
# Demonstrates the full cycle the option asks for:
#   check -> fail -> recover -> verify -> log
#
# Run with -DryRun to exercise every path without touching a real service.
# That switch is not required of students, but a submission that has one is
# showing good judgement rather than padding.

param(
    [string]$ConfigFile = "services.json",
    [string]$LogFile    = "monitor.log",
    [int]$RestartWaitSeconds = 5,
    [switch]$DryRun
)

# Writes one timestamped line to the console and to the log file.
function Write-MonitorLog {
    param([string]$Service, [string]$Status, [string]$Detail = "")

    $stamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $line  = "{0} | {1,-9} | {2,-22} | {3}" -f $stamp, $Status, $Service, $Detail
    Write-Host $line
    Add-Content -Path $LogFile -Value $line
}

# Returns Running, Stopped, or Missing for one service name.
function Get-ServiceHealth {
    param([string]$Name)

    try {
        $svc = Get-Service -Name $Name -ErrorAction Stop
        return $svc.Status.ToString()
    }
    catch {
        return "Missing"
    }
}

# Attempts recovery, waits, then re-checks. Returns $true only if it is
# genuinely healthy afterwards, not just because the restart command returned.
function Invoke-Recovery {
    param([string]$Name)

    if ($DryRun) {
        Write-MonitorLog -Service $Name -Status "DRYRUN" -Detail "would attempt restart"
        return $false
    }

    try {
        Start-Service -Name $Name -ErrorAction Stop
    }
    catch {
        Write-MonitorLog -Service $Name -Status "FAILED" -Detail ("restart threw: " + $_.Exception.Message)
        return $false
    }

    Start-Sleep -Seconds $RestartWaitSeconds
    $after = Get-ServiceHealth -Name $Name

    if ($after -eq "Running") {
        Write-MonitorLog -Service $Name -Status "RECOVERED" -Detail "running after restart"
        return $true
    }

    Write-MonitorLog -Service $Name -Status "FAILED" -Detail "still $after after restart"
    return $false
}

# --- main ---------------------------------------------------------------

if (-not (Test-Path $ConfigFile)) {
    Write-MonitorLog -Service "-" -Status "ERROR" -Detail "config file not found: $ConfigFile"
    exit 1
}

try {
    $services = @((Get-Content $ConfigFile -Raw | ConvertFrom-Json).services)
}
catch {
    Write-MonitorLog -Service "-" -Status "ERROR" -Detail "config file is not valid JSON"
    exit 1
}

Write-MonitorLog -Service "-" -Status "START" -Detail ("checking " + $services.Count + " service(s)" + $(if ($DryRun) { " [dry run]" } else { "" }))

$unhealthy = 0
foreach ($name in $services) {
    $health = Get-ServiceHealth -Name $name

    if ($health -eq "Running") {
        Write-MonitorLog -Service $name -Status "OK" -Detail "running"
        continue
    }

    if ($health -eq "Missing") {
        Write-MonitorLog -Service $name -Status "ERROR" -Detail "no such service on this host"
        $unhealthy++
        continue
    }

    Write-MonitorLog -Service $name -Status "DOWN" -Detail "status is $health, attempting recovery"
    if (-not (Invoke-Recovery -Name $name)) {
        $unhealthy++
    }
}

Write-MonitorLog -Service "-" -Status "END" -Detail "$unhealthy service(s) left unhealthy"
exit $(if ($unhealthy -gt 0) { 1 } else { 0 })

#!/usr/bin/env pwsh
# Log Analysis Script (PowerShell)
# Analyzes a log file using PowerShell objects

$LogFile = "analysis.log"
$ReportFile = "powershell_analysis_report.txt"

$StartTime = [DateTime]::Now

$LogEntries = Get-Content $LogFile | ForEach-Object {
    $parts = $_ -split '\|'
    [PSCustomObject]@{
        Timestamp = $parts[0].Trim()
        Level     = $parts[1].Trim()
        Component = $parts[2].Trim()
        Message   = $parts[3].Trim()
    }
}

$TotalLines = @($LogEntries).Count
$TotalErrors = @($LogEntries | Where-Object { $_.Level -eq "ERROR" }).Count
$ErrorPercentage = [math]::Round(($TotalErrors / $TotalLines) * 100, 1)

$ErrorsByComponent = $LogEntries | Where-Object { $_.Level -eq "ERROR" } | Group-Object -Property Component | Select-Object Name, Count | Sort-Object Count -Descending

$TopErrors = $LogEntries | Where-Object { $_.Level -eq "ERROR" } | Group-Object -Property Message | Select-Object Count, Name | Sort-Object Count -Descending | Select-Object -First 10

$FirstEntry = $LogEntries[0].Timestamp
$LastEntry = $LogEntries[$LogEntries.Count - 1].Timestamp

$EndTime = [DateTime]::Now
$Elapsed = ($EndTime - $StartTime).TotalSeconds

$Report = @"
========================================
Log Analysis Report
========================================
Analysis Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')

QUESTION 1: Total Entries and Errors
Total entries: $TotalLines
Total errors: $TotalErrors ($ErrorPercentage%)

QUESTION 2: Components with Errors
"@

foreach ($item in $ErrorsByComponent) {
    $Report += "`n  $($item.Name): $($item.Count) errors"
}

$Report += "`n`nQUESTION 3: Most Common Error Messages`n"

$count = 0
foreach ($error in $TopErrors) {
    $count++
    $Report += "`n  $count. $($error.Name) ($($error.Count) times)"
}

$Report += "`n`nQUESTION 4: Timeline`n"
$Report += "`n  Started: $FirstEntry`n"
$Report += "`n  Ended: $LastEntry`n"

$Report += "`n`nQUESTION 5: Observations`n"
$Report += "`n  [Write 50-100 word observation about patterns in the data]`n"

$Report += "`n`nScript execution time: $Elapsed seconds`n"
$Report += "========================================`n"

$Report | Out-File -FilePath $ReportFile -Encoding UTF8
Write-Host "Report saved to $ReportFile"

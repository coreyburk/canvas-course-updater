# Export-EventLogs.ps1
# Lab 5.1: Windows Event Log Analysis - Final Project
# Usage: .\Export-EventLogs.ps1 (run in PowerShell as Administrator)

$days = 7
$startTime = (Get-Date).AddDays(-$days)
$outputPath = $PSScriptRoot

# Verify admin privileges
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "ERROR: Run as Administrator" -ForegroundColor Red
    exit 1
}

# Function to export a single event log to CSV
function Export-EventLogToCSV {
    param([string]$LogName, [datetime]$StartTime, [string]$OutputFile)
    try {
        Write-Host "Exporting $LogName events..." -ForegroundColor Cyan
        $events = Get-WinEvent -LogName $LogName -ErrorAction Stop | Where-Object { $_.TimeCreated -ge $StartTime }
        
        $csvData = $events | Select-Object -Property @{Name='Timestamp'; Expression={$_.TimeCreated}},
                                                       @{Name='Level'; Expression={$_.LevelDisplayName}},
                                                       @{Name='Source'; Expression={$_.ProviderName}},
                                                       @{Name='EventID'; Expression={$_.Id}},
                                                       @{Name='Message'; Expression={$_.Message}} |
                             ConvertTo-Csv -NoTypeInformation
        $csvData | Out-File -FilePath $OutputFile -Encoding UTF8 -Force
        $count = if ($events -is [array]) { $events.Count } else { if ($events) { 1 } else { 0 } }
        Write-Host "  [OK] Exported $count events to: $OutputFile" -ForegroundColor Green
        return $count
    }
    catch { 
        Write-Host "  ERROR: $($_.Exception.Message)" -ForegroundColor Red
        return 0 
    }
}

# Main execution
Write-Host "Windows Event Log Exporter - Lab 5.1" -ForegroundColor Cyan
$systemCount = Export-EventLogToCSV -LogName "System" -StartTime $startTime -OutputFile "$outputPath\system.csv"
$securityCount = Export-EventLogToCSV -LogName "Security" -StartTime $startTime -OutputFile "$outputPath\security.csv"
$appCount = Export-EventLogToCSV -LogName "Application" -StartTime $startTime -OutputFile "$outputPath\application.csv"

Write-Host ""
Write-Host "Summary: System=$systemCount, Security=$securityCount, Application=$appCount" -ForegroundColor Green
Write-Host "CSV files ready for analysis (system.csv, security.csv, application.csv)" -ForegroundColor Green

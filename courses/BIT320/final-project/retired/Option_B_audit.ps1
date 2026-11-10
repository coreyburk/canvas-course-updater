# Lab 5.1 Option B - Configuration Management and Compliance Auditing
# Instructor reference implementation.
#
# The point of this option is that the baseline is DATA, not code. Nothing
# below names a specific service or setting; everything is read from the
# baseline file, which is what makes the script reusable against a different
# machine or a different standard.

param(
    [string]$BaselineFile = "baseline.json",
    [string]$ReportFile   = "compliance_report.txt"
)

# Returns an object describing one check: compliant or not, with the detail a
# reader needs in order to act on it.
function Test-BaselineItem {
    param($Item)

    $actual = "unknown"
    $ok = $false

    switch ($Item.type) {
        "service" {
            try {
                $svc = Get-Service -Name $Item.name -ErrorAction Stop
                $actual = $svc.Status.ToString()
                $ok = ($actual -eq $Item.expected)
            }
            catch {
                $actual = "not installed"
            }
        }
        "process" {
            $proc = @(Get-Process -Name $Item.name -ErrorAction SilentlyContinue)
            $actual = $(if ($proc.Count -gt 0) { "running" } else { "absent" })
            $ok = ($actual -eq $Item.expected)
        }
        "path" {
            $actual = $(if (Test-Path $Item.name) { "present" } else { "absent" })
            $ok = ($actual -eq $Item.expected)
        }
        default {
            $actual = "unsupported check type"
        }
    }

    [PSCustomObject]@{
        Item      = $Item.name
        Type      = $Item.type
        Expected  = $Item.expected
        Actual    = $actual
        Compliant = $ok
        Impact    = $Item.impact
    }
}

# --- main ---------------------------------------------------------------

if (-not (Test-Path $BaselineFile)) {
    Write-Host "ERROR: baseline not found: $BaselineFile"
    exit 1
}

try {
    $baseline = @((Get-Content $BaselineFile -Raw | ConvertFrom-Json).items)
}
catch {
    Write-Host "ERROR: baseline is not valid JSON"
    exit 1
}

$results = foreach ($item in $baseline) { Test-BaselineItem -Item $item }

$total     = @($results).Count
$compliant = @($results | Where-Object { $_.Compliant }).Count
$percent   = if ($total -gt 0) { [math]::Round(($compliant / $total) * 100, 1) } else { 0 }
$deviations = @($results | Where-Object { -not $_.Compliant })

$lines = @()
$lines += "========================================"
$lines += "Configuration Compliance Report"
$lines += "========================================"
$lines += "Host:      $env:COMPUTERNAME"
$lines += "Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
$lines += "Baseline:  $BaselineFile ($total items)"
$lines += ""
$lines += "COMPLIANCE: $compliant of $total ($percent%)"
$lines += ""

if ($deviations.Count -eq 0) {
    $lines += "No deviations. Every baseline item matched."
}
else {
    foreach ($level in @("Critical", "Minor")) {
        $atLevel = @($deviations | Where-Object { $_.Impact -eq $level })
        if ($atLevel.Count -eq 0) { continue }
        $lines += "$($level.ToUpper()) DEVIATIONS ($($atLevel.Count))"
        foreach ($d in $atLevel) {
            $lines += ("  {0} [{1}] expected '{2}', found '{3}'" -f $d.Item, $d.Type, $d.Expected, $d.Actual)
        }
        $lines += ""
    }
}

$lines += "========================================"
$lines | Set-Content -Path $ReportFile -Encoding utf8
$lines | ForEach-Object { Write-Host $_ }
Write-Host ""
Write-Host "Report saved to $ReportFile"

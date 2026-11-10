# Retired final project options

These were options A and B when Lab 5.1 offered a choice of three projects.
Retired 2026-11-09 when the final collapsed to a single project in the
student's chosen language.

Both reference implementations were verified working before retirement:
`Option_A_monitor.ps1` ran against a real service list with a `-DryRun` switch
that exercises every path safely, and `Option_B_audit.ps1` reported 83.3 percent
compliance against the six-item `baseline.json`.

They were retired for two reasons rather than any defect in the work:

- **Load.** Each carried roughly 2.3 times the event-log project's complexity,
  measured by new interfaces, demands beyond the spine labs, and artefacts.
- **They forced a language.** Querying Windows services, firewall rules or
  security settings from WSL bash needs `powershell.exe`, so neither was
  genuinely open to a student who preferred bash or Python.

The corresponding Canvas pages are retained, unpublished and bannered, and have
been removed from the Week 5 module.

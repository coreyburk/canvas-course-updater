# Lab 1.2 - Code-Along Source Files

These are the files published to Canvas on 2026-11-09, kept here so the course
content has a versioned source rather than living only in Canvas HTML.

| Folder | Goes where | Audience |
|---|---|---|
| `skeleton/` | Lab 1.2 assignment description | Students, published |
| `reference/` | Lab 1.2 Code-Along Guide | Instructor only, unpublished |

## Why they are shaped this way

**The skeletons run as-given.** Each prints the report frame with `TODO` where the
answers belong, so a student can execute the scaffold before filling anything in.
An empty bash function body is a syntax error, which is why each stub contains a
placeholder command rather than only comments.

**The path list deliberately contains a path that does not exist.** The version
these replaced checked only paths that exist, so its error-handling branch never
ran and students could not demonstrate that it worked. The rubric now asks for
that missing-path line as evidence.

**Directory inspection is non-recursive on purpose.** The previous version summed
file sizes with `Get-ChildItem -Recurse` over the user profile and `rglob('*')`
over `Path.home()`, which takes minutes on a real machine. In a live code-along
that reads as a hang. All three now finish in roughly 0.3 seconds.

## Before changing the Canvas copy

Run all three first. They were verified by execution, not inspection:

```bash
bash reference/system_info.sh && python3 reference/system_info.py
```

PowerShell: `& ./reference/system_info.ps1`

Canvas is still the source of truth for what students see. If these files and
Canvas disagree, check Canvas and correct whichever is actually stale.

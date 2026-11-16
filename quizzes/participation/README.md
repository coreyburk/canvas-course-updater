# Participation Quizzes

Attendance tracking required for all classes: one Participation Quiz per class day.
This folder holds the per-course configs for the generator. The generator works for any course.

## One command

```bash
python tools/create_participation_quizzes.py --config quizzes/participation/<CODE>.json          # dry run
python tools/create_participation_quizzes.py --config quizzes/participation/<CODE>.json --apply  # write
```

A run does three things, in order. Each step is idempotent, so re-running after a partial failure is safe.

1. **Quizzes.** Creates `Participation Quiz - Week N Day` for every week and day (Mon-Fri). Existing titles are skipped.
2. **Modules.** Adds each quiz to its week's Canvas module. The module is found by name (default `Week {week}`). Quizzes already in the module are skipped.
3. **Instructor page.** Creates or updates an unpublished page, `Instructor Notes - Participation Quiz Codes`, listing every quiz title, quiz ID and access code.

Flags:

| Flag | Effect |
|---|---|
| `--apply` | Write to Canvas. Without it, nothing is written. |
| `--only-week N` | Quiz and module steps for one week only. Skips the instructor page, which always covers the whole course. |
| `--update-codes` | Set access codes on quizzes that already exist, e.g. after changing codes. |
| `--skip-modules` | Do not touch modules. |
| `--skip-page` | Do not write the instructor page. |

If a module named `Week N` does not exist, the run stops before writing anything. Set `"module_name"` in the config if a course names its modules differently.

## What each quiz is

- An **ungraded survey** (`quiz_type=survey`). No points, no correct answer.
- **One multiple-choice question** tied to that week's topics. The same question is used for all five days of the week.
- **Anonymous submissions off** and **one attempt**, so attendance is tied to the student.
- Its **own access code**, a topic keyword the instructor gives out in person during class.
- **Unpublished.** The instructor publishes each quiz by hand on its class day.
- No unlock or lock dates, because class times vary by course.

Quizzes for past weeks are not graded. The requirement started partway through the quarter.

## Files

| File | In git? | Purpose |
|---|---|---|
| `tools/create_participation_quizzes.py` | yes | The generator. Works for any course. |
| `quizzes/participation/<CODE>.json` | yes | Course ID, week count, week topics, weekly question and options. |
| `quizzes/participation/<CODE>.codes.json` | **no (gitignored)** | One access code per quiz, keyed by quiz title. |

The codes file is gitignored on purpose. The repo is public and the codes are student-facing. Keep it only on the machine that runs the script.

## Course config (`<CODE>.json`)

```json
{
  "course_code": "ITH216",
  "course_id": "3646987",
  "weeks": 10,
  "module_name": "Week {week}",
  "weeks_data": [
    {"week": 1, "topic": "...", "question": "...", "options": ["...", "...", "..."]}
  ]
}
```

- `course_id` is the numeric Canvas ID.
- `weeks` must be 5 or 10. `weeks_data` must have exactly that many entries, covering weeks 1 to N.
- Each entry needs 2 to 6 options.
- No em dashes in question or option text.
- `module_name` is optional. Default is `Week {week}`.

## Codes file (`<CODE>.codes.json`)

Keys are the exact quiz titles, for example `"Participation Quiz - Week 1 Monday": "EXAMPLE1"`. Values are one word, 3 to 30 letters or digits, no spaces. Use course or weekly topic keywords. Every code must be unique within the course. The script refuses to run if a quiz has no code or two quizzes share one.

The file must contain one entry per quiz: `weeks x 5` entries.

## Adding a new course

1. Create `<CODE>.json` with the course ID, week count, week topics and questions.
2. Create `<CODE>.codes.json` with `weeks x 5` unique codes, keyed by quiz title. Keep it out of git; it is already gitignored by name.
3. Dry run, check the output, then run with `--apply`.
4. Publish each quiz manually on its class day. Share that day's code in person.
5. Log the course in `courses/<CODE>.md` and `CHANGELOG.md`.

## Canvas behavior to know about

- Canvas requires one correct answer on every multiple-choice question. The script sets all weights to 0, but Canvas forces the first option to 100. The quiz is ungraded, so this does not affect students or grades. The instructor view shows that option as correct.
- Quiz titles and access codes can be changed later through the API (`PUT`).
- The script sets no due dates.

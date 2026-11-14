# ChatGPT desktop scheduled tasks

Use this path to run the kit from a local ChatGPT desktop project in Codex mode.
The task reads the released workflow files and runs their Python scripts. The
scheduled prompt describes the steps that need a model.

## Set up

1. Download and unzip the [kit](../README.md). Unzip the two files in its
   `plugins` folder into separate folders named `build-radar` and `talent-alpha`.
2. Install Python 3.10 or later. In ChatGPT desktop, open Codex and add the
   folder containing both helpers as a local project. Test each prompt below
   manually before saving it as a scheduled task.
3. In **Scheduled**, create a local task for each helper in that project. Use
   the same folder every run so the archive and seen-event file survive.
   Schedule Build Radar weekly and Talent Alpha daily. Keep the computer
   awake and the app running. Review the first result in **Scheduled**.

[OpenAI scheduling guide](https://learn.chatgpt.com/docs/automations)

## Windows test results

The November 14, 2026 test used kit v0.2.0 and two actual scheduler launches
per helper in the same local project. Build Radar read all 10 feeds, wrote
both HTML files, and left the 29-row archive unchanged on its same-day
rerun. Talent Alpha's live public-news scan returned no qualifying signals.
The released fictional fixture produced a validated card, and the next
scheduled run suppressed that event using the saved state. The fixture
supplied the test verdicts. A live positive Talent Alpha card and an
overnight rerun still need verification.

## Build Radar

Paste this as the task instructions. Replace the reader description and set
the source list during your manual run if you want something other than the
kit defaults.

```text
Run Build Radar for a reader who builds AI workflows and wants verifiable
releases and one practical experiment. Use standard sensitivity and the saved
sources, or build-radar/samples/sample-sources.json on the first run.

Read build-radar/skills/build-radar/SKILL.md and the bundled scorer,
synthesizer, and card-writer instructions. Resolve plugin paths inside the
extracted build-radar folder. Perform the model steps using those instructions
and use the shipped Python scripts for fetching, filtering, enforcing evidence
rules, archiving, and rendering. Keep HTML files in
build-radar-runs/<date>/ and the archive in build-radar-archive.csv, relative
to the project folder.

If today's digest and card both exist, report that the routine already ran.
If only one exists, report the partial run and leave the archive alone for
review. If fewer than half of the feeds return data, stop and list failures.
Report feed health, evidence-qualified movements, archive rows and both HTML
paths. Report a quiet week when the evidence gate finds no movements.
Keep results in the project and the run chat.
```

## Talent Alpha

In your local project chat, ask Codex to follow
`talent-alpha/skills/talent-alpha-setup/SKILL.md` with you. Answer its questions
and have it save `onepromptman-profile.md` in the project folder. Use a distinct
seen-event file per role, or keep each role in its own project folder.

```text
Run Talent Alpha for the saved role in onepromptman-profile.md. Read
talent-alpha/skills/talent-alpha/SKILL.md and its bundled scanner, Advocate,
Skeptic, and critic instructions. Resolve plugin paths inside the extracted
talent-alpha folder and use the current chat's web search. Stop if the role
profile or web search is missing.

Keep the saved role scope and source freshness windows. Use the shipped Python
scripts to deduplicate, join trusted source facts, build the checked HTML card
and record state. Keep the Advocate and Skeptic independent. Reuse the state
file from the profile every run.
Report counts, the card path if one was made, and a reason if no item cleared
the bar. Keep results in the project and the run chat. Include company-level
signals only.
```

# Scheduled recipes for Build Radar and Talent Alpha

Status: In prep. The Build Radar recipe ran once on 2026-11-09. The Talent Alpha recipe ran twice on 2026-11-10 but has not produced a card yet.

## For testers

Download the tester kit zip from this repository's [Releases](../../releases) page, unzip it, and open **Start here.html**. It walks you through installing both plugins and setting them up, in about 45 minutes, and includes a feedback form.

## Scheduled recipes

These recipes let the Claude desktop app run two OnePromptMan plugins for you on a timetable, so you do not have to remember to ask.

- **Build Radar** writes a short weekly briefing on what people building with AI shipped, plus a one-page card. Recipe: [build-radar.md](build-radar.md).
- **Talent Alpha** checks layoff and funding news every night and writes one ranked card of people who may now be open to a role you are hiring for. Recipe: [talent-alpha.md](talent-alpha.md). **Untested.**

Each recipe is a message you paste into the app, plus the timetable to pick. The plugins are not in this folder. Each recipe links to the plugin it needs.

## How a scheduled task works

The Claude desktop app has a page called Scheduled. A task there is a saved message plus a timetable. When the time comes, the app opens a new chat by itself, sends the saved message, and keeps the result in that chat and in a folder you choose.

These recipes run on your own computer, so:

- The computer has to be awake and the Claude app open at the scheduled time.
- If the computer was asleep, the app runs the task once when it wakes up. It does not repeat every missed time.
- Everything stays in a folder on your computer. Nothing is emailed or posted.

## What you need

- The Claude desktop app, version 1.1.5368 or later, signed in to your Claude account.
- The plugin named in the recipe, installed on your Claude account.
- Python 3.10 or later, from [python.org](https://www.python.org/downloads/).
- One new folder per recipe, where the plugin's setup has run once.

## The five steps

1. Install the plugin, and make a new, empty folder for it.
2. Open a chat in that folder and type the setup phrase from the recipe. Answer the questions once.
3. In the app's Code tab, click **Scheduled**, then **New task**. Fill in the name, the folder, the timetable and the message from the recipe.
4. Click **Run now** once and watch it. If the app asks for permission, pick the option that always allows it, so later runs do not stop and wait.
5. Compare the result with the recipe's first-run check.

## Why these run on your computer, not in the cloud

Claude can also run scheduled tasks in the cloud while your computer is off. These two plugins do not suit that today, for three reasons from Claude's documentation:

- A cloud run starts on a fresh machine with a copy of a GitHub repository. The documentation says plugins turned on in your settings do not load there, and it does not say that plugins on your account do ([cloud environments](https://code.claude.com/docs/en/cloud-environments)).
- A cloud run can only reach an approved list of websites. Eight of Build Radar's ten default news feeds are not on it ([default allowed domains](https://code.claude.com/docs/en/cloud-environments#default-allowed-domains)).
- A cloud run keeps no files from one run to the next unless it saves them to GitHub ([cloud scheduled tasks](https://code.claude.com/docs/en/routines)). Talent Alpha needs its memory file to survive from night to night.

Claude's page on [desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks) covers the local option in full.

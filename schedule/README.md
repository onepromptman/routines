# Run the kit on a schedule in Claude

For laptop-off scheduling, see the [ChatGPT Dot cloud guide](chatgpt-dot.md).
The [ChatGPT desktop recipes](chatgpt-desktop.md) run on your computer.

Status: In prep. The Build Radar recipe ran once on 2026-11-09. The Talent Alpha recipe ran twice on 2026-11-10 but has not produced a card yet.

These recipes let the Claude desktop app run the two kit plugins for you on a timetable, so you do not have to remember to ask.

You do not need this page to use the kit. Scheduling is optional, and it needs two things the main steps do not: Python installed on your computer, and the app's Code tab.

- **Build Radar** writes a short weekly briefing on what people building with AI shipped, plus a one-page card. Recipe: [build-radar.md](build-radar.md).
- **Talent Alpha** checks layoff and funding news every night and writes one ranked card of companies that may now have people open to a role you are hiring for. Recipe: [talent-alpha.md](talent-alpha.md). **Not yet proven.**

Each recipe is a message you paste into the app, plus the timetable to pick. The plugins come from the [kit download](../README.md).

## How a scheduled task works

The Claude desktop app has a page called Scheduled. A task there is a saved message plus a timetable. When the time comes, the app opens a new chat by itself, sends the saved message, and keeps the result in that chat and in a folder you choose.

These recipes run on your own computer, so:

- The computer has to be awake and the Claude app open at the scheduled time.
- If the computer was asleep, the app runs the task once when it wakes up. It does not repeat every missed time.
- Everything stays in a folder on your computer. Nothing is emailed or posted.

## What you need

- The Claude desktop app, version 1.1.5368 or later, signed in to your Claude account.
- The plugin named in the recipe, uploaded to your Claude account from the kit.
- Python 3.10 or later, from [python.org](https://www.python.org/downloads/). The Code tab runs the plugin's scripts on your computer.
- One new folder per recipe, where the plugin's setup has run once.

## The five steps

1. Upload the plugin from the kit, and make a new, empty folder for it.
2. Open a chat in that folder and type the setup phrase from the recipe. Confirm who the work is for and what it should look at. For Talent Alpha, repeat setup in a separate folder for each role you plan to schedule.
3. In the app's Code tab, click **Scheduled**, then **New task**. Fill in the name, the folder, the timetable and the message from the recipe.
4. Click **Run now** once and watch it. Review each permission request. Allow the chosen folder, Python scripts, and web access required by the recipe.
5. Compare the result with the recipe's first-run check.

To change the scope later, run the setup command in the same folder and
review the updated profile and one test result. Keep the history for that
role. A new role gets its own setup folder and schedule.

## Claude cloud scheduled tasks

Claude can run scheduled tasks while your computer is off. These local recipes need changes for that environment:

- Make the kit files and Python available in the cloud environment, and allow its required feed hosts. See [cloud environments](https://code.claude.com/docs/en/cloud-environments).
- Connect a durable storage service for the Build Radar archive, Talent Alpha's seen-event file, and the cards. Claude clones attached repositories on each new run and can use connected services. See [cloud scheduled tasks](https://code.claude.com/docs/en/routines).

The Claude cloud version is still in prep. The shipped recipes below the kit download use local storage.

Claude's page on [desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks) covers the local option in full.

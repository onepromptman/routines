# Recipe: Build Radar every Monday

**Tested once** on 2026-11-09, on a Windows PC, with a fictional company, Alder Pattern Labs. The run took about five minutes and needed no help.

| | |
|---|---|
| Plugin | AI Build Radar 1.2.2, from [onepromptman/build-radar](https://github.com/onepromptman/build-radar) |
| Runs | On your computer, as a local scheduled task in the Claude desktop app |
| Timetable | Weekly, Monday, 8:07 AM |
| Writes to | The folder you pick for the task |
| Sends | Nothing. No email and no posts |

## Before you start

1. Install the plugin by following the Get started steps in the [Build Radar README](https://github.com/onepromptman/build-radar#get-started).
2. Make sure Python 3.10 or later is installed.
3. Make a new, empty folder, for example `Documents\Build Radar`.
4. In the desktop app's Code tab, start a chat in that folder and type `set up build radar`. Answer the questions. This saves `onepromptman-profile.md` in the folder. A scheduled run cannot answer questions, so it needs this file first.

## Create the task

In the Code tab, click **Scheduled**, then **New task**. If a menu offers **Local** and **Cloud**, pick **Local**. If you see **Only on this computer**, turn it on.

- **Name:** `Build Radar weekly`
- **Folder:** the folder from step 3
- **Timetable:** Weekly, Monday, 8:07 AM. A few minutes past the hour starts closer to on time.
- **Permission mode:** Auto if your app offers it, otherwise Accept edits
- **Worktree:** leave it off
- **Instructions:** paste the message below, then replace `<your folder>` with the folder's full path

```text
You are running the weekly AI Build Radar. This is an unattended scheduled run, so nobody can answer questions. Do not use AskUserQuestion. Do exactly this and nothing else.

Working folder: <your folder>
Treat it as the working folder for every step.

These questions are already answered:
- Use onepromptman-profile.md in the working folder as it stands. Do not run setup or edit the profile.
- Run the full pipeline, and build the visual card.
- Keep the saved source list, whatever its review date.

1. If the working folder has no onepromptman-profile.md, or the file has no "## Kit: build-radar" block, report that and stop.
2. If build-radar-runs/<today>/digest.html already exists, report "already ran today" and stop, so the archive gets no duplicate rows.
3. Run the build-radar:build-radar skill, with that plugin prefix. If feed health is below 0.5, do not ask: stop before scoring and report every blocked host and failed feed.
4. If digest.html was written, run the build-radar:build-radar-card skill, with that plugin prefix, on today's run folder.
5. Send, post, publish and push nothing. Open no browser and no file in a window.
6. Report, in this order: the plugin version from its plugin.json; feed health as ok/total; each blocked host; items scored; movements shipped; rows archived; the full paths of digest.html and card.html; then the plain-text digest verbatim. If any step failed, name it and paste the error.
```

The skill names carry the `build-radar:` prefix on purpose. It makes the run use this plugin even if you have another skill with a similar name.

## First-run check

Click **Run now** on the task's page, then open the run from its **History** list. If a permission question appears, pick the option that always allows it.

The run ends with a short report. Check that:

- [ ] The plugin version is 1.2.2 or later.
- [ ] Feed health reads at least 5/10, and no host is listed as blocked. The test run read 10/10.
- [ ] `build-radar-runs\<date>\digest.html` and `card.html` exist in your folder. Open both in a browser.
- [ ] `build-radar-archive.csv` in your folder has new rows.

A week where nothing clears the quality bar is reported as a quiet week. That is a correct result, not a failure.

A second **Run now** on the same day reports "already ran today" and stops. That keeps the archive free of duplicate rows.

## Where the output lands

| File | What it is |
|---|---|
| `build-radar-runs\<date>\digest.html` | The briefing, ready to forward |
| `build-radar-runs\<date>\card.html` | The one-page card |
| `build-radar-archive.csv` | One row per useful item, every week, all in one file |
| The run's chat | The same briefing as plain text, under Scheduled in the sidebar |

## If something goes wrong

- **Feeds fail with HTTP 403.** Something on your network or computer is blocking those websites. The report names each blocked host. Allow those hosts, then run it again.
- **The run stopped on a question.** Open it from the task's History list and answer it. If the profile was incomplete, run `set up build radar` in the folder again.
- **Nothing ran on Monday.** The computer was asleep or the app was closed. The app runs the task once when it next wakes, if that is within seven days.

## Turn it off

- **Pause:** on the task's page, set Status to Paused. Nothing runs until you set it back to Active.
- **Remove:** on the task's page, click Delete. The app keeps the saved message in the `.claude\scheduled-tasks\build-radar-weekly` folder inside your home folder. Delete that folder yourself if you want it gone. Your briefings stay in your folder.

## What the test showed

- A local scheduled task loads a plugin installed on the Claude account. The test run used the account copy of Build Radar 1.2.2.
- The message above runs the whole job with no questions: fetch the feeds, score the items, group them, write the briefing, draw the card.
- The test run read all 10 feeds, scored 63 items, kept 2 trends and added 17 rows to the archive.
- Not tested yet: the weekly timetable firing on its own, and the catch-up run after the computer sleeps.

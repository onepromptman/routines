# Recipe: Talent Alpha every night

**Not yet proven.** Two manual runs on 2026-11-10, with plugin version 1.4.0, finished without errors but found no news recent enough to show, so no card or memory file was made yet. The kit ships 1.5.0, which this message has not run yet. The plugin itself says its memory between scheduled runs is unproven until two runs on different days pass.

| | |
|---|---|
| Plugin | Talent Alpha 1.5.0 or later, from the [kit download](../README.md). Source: [onepromptman/talent-alpha](https://github.com/onepromptman/talent-alpha) |
| Runs | On your computer, as a local scheduled task in the Claude desktop app |
| Timetable | Daily, 6:07 AM |
| Writes to | The folder you pick for the task |
| Sends | Nothing. It contacts no one |

Talent Alpha searches the web for layoff news and funding news. Its card names companies and job functions, never people. A person reads the card and decides before anyone is contacted.

## Before you start

1. Download the [kit](../README.md), unzip it, and upload `plugins\talent-alpha.zip` to the Claude desktop app: **Customize > Plugins > Add > Upload plugin**.
2. Make sure Python 3.10 or later is installed.
3. Make a new, empty folder for one open role, for example `Documents\Talent Alpha Test Engineer`.
4. In the desktop app's Code tab, start a chat in that folder and type `set up talent alpha`. Answer the questions. This saves `onepromptman-profile.md` in the folder.
5. Setup checks that the chat has web search, and says so if it is missing. The scan pulls all its news through web search, so it cannot run without it.

## Where its memory lives

The plugin keeps a memory file, `talent-alpha-state.json`, at the top of the folder. It lists every news item already handled, so each card shows only new events. Entries older than 30 days drop off by themselves.

To keep the memory working:

- Always run the task in the same folder.
- Do not move, rename or delete the memory file. Without it, the next card repeats old news.
- Leave **Worktree** off. A worktree run would write the memory into a copy that is thrown away.
- The plugin writes the memory only after a card passes its checks, so a failed night leaves it as it was.

## Create the task

In the Code tab, click **Scheduled**, then **New task**. If a menu offers **Local** and **Cloud**, pick **Local**. If you see **Only on this computer**, turn it on.

- **Name:** `Talent Alpha nightly`
- **Folder:** the folder from step 3
- **Timetable:** Daily, 6:07 AM
- **Permission mode:** Auto if your app offers it, otherwise Accept edits
- **Worktree:** leave it off
- **Instructions:** paste the message below, then replace `<your folder>` with the folder's full path

```text
You are running the nightly Talent Alpha scan. This is an unattended scheduled run, so nobody can answer questions. Do not use AskUserQuestion. Do exactly this and nothing else.

Working folder: <your folder>
Treat it as the working folder for every step.

These questions are already answered:
- Use onepromptman-profile.md in the working folder as it stands. Do not run setup or edit the profile.
- No extra context for this run. Treat the braindump invitation as "skip".
- Use max_shown and include_funding_distress from the profile.

1. If you cannot use the WebSearch tool, even after loading it with ToolSearch, report "no web search, scan did not run" and stop. Never report that as a quiet night.
2. If the profile has no "## Kit: talent-alpha" block, or the block carries setup_incomplete, report that and stop.
3. Run the talent-alpha:talent-alpha skill, with that plugin prefix. Use the state_file path from the profile, and never delete or move that file.
4. If an agent halts needing input, do not ask. Stop, list what it needed, and do not record state.
5. Contact nobody. Send, post, publish and push nothing. Open no browser and no file in a window.
6. Report, in this order: the plugin version from its plugin.json; events pulled; events dropped as already seen; events dropped as out of window; candidates shown and held; the state file's entry count; the full path of overnight_card.html; the hero company and its why-now. If no event was recent enough or new, say "nothing new to show" and give the reason.
```

## First-run check, over two days

**Day 1.** Click **Run now** on the task's page, then open the run from its **History** list. If a permission question appears, pick the option that always allows it. Check that:

- [ ] The plugin version is 1.5.0 or later.
- [ ] The report gives a count of events pulled and the path to `overnight_card.html`, or says "nothing new to show" with a reason.
- [ ] `talent-alpha-state.json` now exists in your folder.

**Day 2.** Let the timetable run it, or click **Run now** on a later day. Check that:

- [ ] The report counts some events as already seen, or says "nothing new to show" with a reason.
- [ ] No news story from day 1's card shows up again.

Once both days pass, replace **Not yet proven** at the top of this page with the two dates.

## Where the output lands

| File | What it is |
|---|---|
| `talent-alpha-runs\<date>\overnight_card.html` | The ranked card. A second run on the same day gets its own folder ending in `-2` |
| `talent-alpha-state.json` | The memory of news already handled |
| The run's chat | A short summary, under Scheduled in the sidebar |

## If something goes wrong

- **"no web search, scan did not run".** Turn on web search for the app, then run it again.
- **The run stopped because an agent needed input.** Open it from the task's History list to see what it needed. Usually the profile is missing a fact, so run `set up talent alpha` in the folder again.
- **Nothing ran overnight.** The computer was asleep or the app was closed. The app runs the task once when it next wakes. Layoff notices older than three days are skipped on purpose, so a computer that stays off for longer misses those.

## Turn it off

- **Pause:** on the task's page, set Status to Paused. Nothing runs until you set it back to Active.
- **Remove:** on the task's page, click Delete. The app keeps the saved message in the `.claude\scheduled-tasks\talent-alpha-nightly` folder inside your home folder. Delete that folder yourself if you want it gone. Your cards and the memory file stay in your folder.

<div align="center">

<h1>OnePromptMan kit</h1>

<h3>Less reading. Better timing.</h3>

<p>Two Claude plugins that read the news for you and hand back one card.<br><b>Talent Alpha</b> catches hiring moments while they are still fresh.<br><b>Build Radar</b> cuts a week of AI news down to what is worth trying.<br>Answer a few questions once. Then type <code>run talent alpha</code> or <code>run build radar</code> any time.</p>

<p><sub>NO CODE &nbsp;·&nbsp; NO API KEY &nbsp;·&nbsp; THE KIT NEVER CONTACTS ANYONE</sub><br><sub>Runs in the Claude desktop app, not in Claude chat on the web or your phone.</sub></p>

<a href="https://github.com/onepromptman/routines/releases/latest/download/OnePromptMan-kit.zip"><img src="docs/download-kit.svg" alt="Download the OnePromptMan kit ZIP" height="60"></a>

<br><br>

<table>
<tr>
<td align="center" width="50%">
<a href="docs/talent-alpha-sample.png"><img src="docs/talent-alpha-thumb.png" alt="A Talent Alpha card for a fictional role, with fictional companies graded S and A" width="100%"></a>
<br><br><sub>FOR PEOPLE WHO HIRE</sub><br><a href="#talent-alpha-timing-is-the-edge"><b>Talent Alpha</b></a><br>Timing is the edge
</td>
<td align="center" width="50%">
<a href="docs/build-radar-sample.png"><img src="docs/build-radar-thumb.png" alt="A Build Radar card made from fictional data, with one movement and one thing to try" width="100%"></a>
<br><br><sub>FOR PEOPLE WHO BUILD WITH AI</sub><br><a href="#build-radar-less-news-more-reps"><b>Build Radar</b></a><br>Less news, more reps
</td>
</tr>
</table>

<sub>Sample cards made from fictional companies and data.</sub>

</div>

## Why these exist

I scaled a startup's talent team from the back foot, always fighting for the best people. You learn to use every advantage you can find. Knowing about a layoff or a big shift in talent isn't enough. You need to know first. That's why I built Talent Alpha.

As a builder, I had the opposite problem: too much news, not enough focus. Build Radar filters the noise down to what's worth trying this week.

Routines is where I keep my scheduled agent tasks. These two are the first.

## At a glance

| | **Talent Alpha** | **Build Radar** |
|---|---|---|
| **It reads** | Layoff and funding news, by web search, plus your job criteria when you connect a sourcing platform | GitHub and the builder feeds you pick |
| **You get** | A ranked card of companies, why now, a first line, and an optional campaign in your sourcing platform | A short briefing, a one-page card, and one thing to try |
| **How often** | Whenever you ask | Weekly, or whenever you ask |
| **It never** | Names people or contacts anyone itself | Calls one source a trend without flagging it |

## Talent Alpha: timing is the edge

**The problem.** A layoff or a bad funding round can make good people open to a move. By the time everyone has heard, every recruiter is calling them.

**What it does.**

- Searches the web for layoff and funding-distress news.
- Grades each company **S, A, B or C** on how well the news fits your open role.
- Gives you **why now**, the **source links** and a **draft first line**.
- Stays fresh: layoff news counts for **3 days**, funding news for **7**. Run it again and you only see what is new.

**From card to campaign.** Connect your sourcing platform and Talent Alpha hands it the results. It loads your search criteria, copies the job into a new campaign and points it at the companies you ranked highest. Noon and Juicebox work today, with an account on that platform. Using something else? Tune it to connect the sourcing platform you already use.

**The line it does not cross.** The card names companies and job functions, never people. Talent Alpha contacts no one. A campaign only runs on its own if you have set it to auto-run inside your sourcing platform. Otherwise it waits for you.

Setup is a short conversation about the role you are hiring for:

![An illustration of the Talent Alpha setup conversation: the role, the skills and location, and which signals to prioritize](docs/talent-alpha-setup.svg)

## Build Radar: less news, more reps

**The problem.** Read everything and you learn nothing. Read nothing and you fall behind.

**What it does.**

- Scans GitHub and the builder feeds you choose.
- Throws out anything without evidence. Nothing counts as a trend without **two independent sources**, or a flag that it has only one.
- Groups what is left into **a few movements**, written for what you build.
- Ends every briefing with **one experiment to try** this week.

**You set the filter.** Tell it what you build and who you build for. It filters for your path, not the feed's.

Setup asks who the briefing is for and what to watch:

![An illustration of the Build Radar setup conversation: who it is for, which sources to watch, what to leave out and when to run](docs/build-radar-setup.svg)

## Get started in three steps

1. **Download** the kit and unzip it. Open **Start here.html** for the picture guide.
2. **Upload** `talent-alpha.zip` and `build-radar.zip` from the `plugins` folder in the Claude desktop app: **Customize > Plugins > Add > Upload plugin**. Do not unzip these two.
3. **Set up.** Make an empty folder, start a new Cowork task and pick that folder. Type `set up talent alpha` or `set up build radar` and answer a few questions.

Then type `run talent alpha` or `run build radar` whenever you want a fresh card.

![The kit in three steps: download the ZIP, upload both plugin files, then set up and run in a Cowork task](docs/quick-start.svg)

**You need:** the Claude desktop app (Windows or Mac) on a paid Claude plan. These do not run in Claude chat on the web or your phone. Talent Alpha also needs web search turned on. Build Radar may ask you to allow some websites; **Start here.html** shows where. No API key, no other account, no code.

## Your data

- What you type goes to Claude, like any chat.
- Your answers and cards stay in the folder you choose. Delete the folder to delete them.
- If you connect a sourcing platform, the role criteria and target companies go to that platform's account, under its own terms.
- The kit never emails or posts. A campaign you set to auto-run in your sourcing platform sends from that platform.

## Status

Tested on Windows before release. Mac not tried yet. Running them on a timetable is optional and still in prep: see [Run it on a schedule](schedule/README.md).

**Tell me what breaks.** [Open an issue](https://github.com/onepromptman/routines/issues), or message me on [LinkedIn](https://www.linkedin.com/in/bryanhong) if you don't have a GitHub account.

[Release notes](https://github.com/onepromptman/routines/releases/latest) · [Talent Alpha source](https://github.com/onepromptman/talent-alpha) · [Apache 2.0 license](LICENSE) · [Security reporting](SECURITY.md) · © 2026 OnePromptMan

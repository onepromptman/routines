<div align="center">

# OnePromptMan kit

**Two helpers for the Claude desktop app. No code, no API key.**

**Build Radar** tells you each week what people building with AI shipped.<br/>
**Talent Alpha** tells you which companies just had layoff or funding news that matters for the role you are hiring.

<br/>

<a href="https://github.com/onepromptman/routines/releases/latest/download/OnePromptMan-kit.zip">
  <img src="https://img.shields.io/badge/Download%20the%20kit-ZIP-black?style=for-the-badge&logo=github" alt="Download the kit (ZIP)" height="56">
</a>

<sub>Then unzip it and open <b>Start here.html</b>.</sub>

</div>

## Three steps

1. **Download** the ZIP above and unzip it.
2. **Upload** `build-radar.zip` and `talent-alpha.zip` from the `plugins` folder to the Claude desktop app: **Customize > Plugins > Add > Upload plugin**. Do not unzip these two.
3. **Set up.** Make an empty folder. In the app, start a new Cowork task and pick that folder. Type `set up build radar` or `set up talent alpha`. Claude asks a few questions and does the rest.

After that, type `run build radar` or `run talent alpha` whenever you want a fresh one.

**You need:** the Claude desktop app (Windows or Mac) on a paid Claude plan. Talent Alpha also needs web search turned on. Build Radar may ask you to allow some websites; **Start here.html** shows where. No API key, no other account, no code.

## What you get

| | |
|---|---|
| ![Build Radar sample card](docs/build-radar-sample.png) | ![Talent Alpha sample card](docs/talent-alpha-sample.png) |
| **Build Radar.** A short briefing and a one-page card. Every item links to its sources. | **Talent Alpha.** A ranked card of companies, why now, and a line to open with. It names companies, never people, and never contacts anyone. |

<sub>Sample cards made from fictional companies. The Talent Alpha sample shows official layoff filings as a source. The helper in this kit finds layoff news by web search instead.</sub>

## Your data

What you type goes to Claude, like any chat. Your answers and cards are saved only in the folder you choose. Delete the folder to delete them.

## More

- [Run it on a schedule](schedule/README.md) (optional)
- Source and details, for the curious. You do not need these to use the kit: [Talent Alpha](https://github.com/onepromptman/talent-alpha). Build Radar's source is inside the kit.
- Something broke or confused you? [Open an issue](https://github.com/onepromptman/routines/issues). You need a free GitHub account for that.

[License](LICENSE) · © 2026 OnePromptMan

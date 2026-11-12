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
2. **Upload** each file in the `plugins` folder to the Claude desktop app: **Customize > Plugins > Add > Upload plugin**.
3. **Type** `set up build radar` or `set up talent alpha` in a new Cowork task. Claude asks a few questions and does the rest.

After that, type `run build radar` or `run talent alpha` whenever you want a fresh one.

**You need:** the Claude desktop app (Windows or Mac), signed in to your Claude account. Nothing else.

## What you get

| | |
|---|---|
| ![Build Radar sample card](docs/build-radar-sample.png) | ![Talent Alpha sample card](docs/talent-alpha-sample.png) |
| **Build Radar.** A short briefing and a one-page card. Every item links to its sources. | **Talent Alpha.** A ranked card of companies, why now, and a line to open with. It names companies, never people, and never contacts anyone. |

<sub>Sample cards made from fictional companies.</sub>

## Your data

What you type goes to Claude, like any chat. Your answers and cards are saved only in the folder you choose. Delete the folder to delete them.

## More

- [Run it on a schedule](schedule/README.md) (optional)
- Source and details: [Talent Alpha](https://github.com/onepromptman/talent-alpha). Build Radar's source is inside the kit.
- Something broke or confused you? [Open an issue](../../issues).

[License](LICENSE) · © 2026 OnePromptMan

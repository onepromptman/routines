#!/usr/bin/env python3
"""Install the pinned OnePromptMan kit on a cloud computer with Python 3.10+."""

import argparse
import hashlib
import io
from pathlib import Path
import tempfile
from urllib.request import urlopen
from zipfile import ZipFile


VERSION = "v0.2.0"
ASSET = "OnePromptMan-kit.zip"
URL = f"https://github.com/onepromptman/routines/releases/download/{VERSION}/{ASSET}"
SHA256 = "50e54e84f81cdf045b706c94f40476c9c10b2103d246fa48416415334a33e3a9"
RUNTIME_FILES = {
    "build-radar": (
        "agents/card-writer.md",
        "agents/scorer.md",
        "agents/synthesizer.md",
        "skills/build-radar-setup/SKILL.md",
        "skills/build-radar/SKILL.md",
        "skills/build-radar/references/00_SHARED_CORE.md",
        "skills/build-radar/references/01_SCORING_MATRIX.md",
        "skills/build-radar/references/FEED_PACK.md",
        "skills/build-radar/references/content-schemas/card.content-schema.json",
        "skills/build-radar/references/content-schemas/movements.content-schema.json",
        "skills/build-radar/references/content-schemas/scores.content-schema.json",
        "skills/build-radar/references/radar-workflow.template.json",
        "skills/build-radar/references/templates/radar-card.html",
        "skills/build-radar/scripts/build_digest.py",
        "skills/build-radar/scripts/fetch_and_parse.py",
        "skills/build-radar/scripts/fill_workflow.py",
        "skills/build-radar/scripts/join_filter.py",
        "skills/build-radar/scripts/render_card.py",
    ),
    "talent-alpha": (
        "agents/advocate.md",
        "agents/critic.md",
        "agents/scanner.md",
        "agents/skeptic.md",
        "skills/talent-alpha-setup/SKILL.md",
        "skills/talent-alpha/SKILL.md",
        "skills/talent-alpha/references/00_SHARED_CORE.md",
        "skills/talent-alpha/references/02_SOURCING_MATRIX.md",
        "skills/talent-alpha/references/EVENT_PIPELINE_SCHEMA.md",
        "skills/talent-alpha/references/content-schemas/card.content-schema.json",
        "skills/talent-alpha/references/content-schemas/n8n-config.schema.json",
        "skills/talent-alpha/references/templates/overnight_card.template.html",
        "skills/talent-alpha/scripts/render.py",
        "skills/talent-alpha/scripts/runlog.py",
        "skills/talent-alpha/scripts/state.py",
        "skills/talent-alpha/scripts/targets.py",
        "skills/talent-alpha/scripts/validate_card.py",
    ),
}


def verify_installation(kit):
    marker = kit / ".release-sha256"
    if not marker.is_file() or marker.read_text(encoding="ascii").strip() != SHA256:
        raise ValueError(f"Unrecognized kit at {kit}. Move that kit folder aside and retry.")
    for helper, paths in RUNTIME_FILES.items():
        for path in paths:
            if not (kit / helper / path).is_file():
                raise ValueError(
                    f"Missing {helper}/{path} in {kit}. Move that kit folder aside and retry."
                )
    return kit


def install(root, archive_path):
    kit = root / "kit" / VERSION
    if kit.exists():
        return verify_installation(kit)

    if archive_path is None:
        with urlopen(URL, timeout=60) as response:
            archive = response.read()
    else:
        archive = archive_path.read_bytes()
    if hashlib.sha256(archive).hexdigest() != SHA256:
        raise ValueError(f"Release checksum mismatch for {ASSET}")

    kit.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=kit.parent) as temporary:
        staged = Path(temporary) / VERSION
        staged.mkdir()
        with ZipFile(io.BytesIO(archive)) as outer:
            for name in RUNTIME_FILES:
                data = outer.read(f"OnePromptMan kit/plugins/{name}.zip")
                with ZipFile(io.BytesIO(data)) as plugin:
                    plugin.extractall(staged / name)
        (staged / ".release-sha256").write_text(SHA256 + "\n", encoding="ascii")
        verify_installation(staged)
        try:
            staged.rename(kit)
        except OSError:
            if not kit.exists():
                raise
            return verify_installation(kit)
    return kit


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.home() / "onepromptman-routines")
    parser.add_argument("--archive", type=Path, help="Use a downloaded copy of the release ZIP.")
    args = parser.parse_args()
    try:
        kit = install(args.root.expanduser().resolve(), args.archive)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Kit setup stopped: {error}\n")
    print(kit)


if __name__ == "__main__":
    main()

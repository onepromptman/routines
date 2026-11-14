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
HELPERS = ("build-radar", "talent-alpha")


def install(root, archive_path):
    kit = root / "kit" / VERSION
    marker = kit / ".release-sha256"
    if kit.exists():
        if (
            marker.is_file()
            and marker.read_text(encoding="ascii").strip() == SHA256
            and all((kit / name / "skills" / name / "SKILL.md").is_file() for name in HELPERS)
        ):
            return kit
        raise ValueError(f"Existing installation is incomplete or unrecognized: {kit}")

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
            for name in HELPERS:
                data = outer.read(f"OnePromptMan kit/plugins/{name}.zip")
                with ZipFile(io.BytesIO(data)) as plugin:
                    plugin.extractall(staged / name)
        (staged / marker.name).write_text(SHA256 + "\n", encoding="ascii")
        staged.rename(kit)
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

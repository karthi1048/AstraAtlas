from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]


def run_step(title: str, command: list[str], cwd: Path) -> None:
    print()
    print("=" * 60)
    print(title)
    print("=" * 60)

    result = subprocess.run(
        command,
        cwd=cwd,
        check=False,
    )

    if result.returncode != 0:
        print(f"[FAIL] {title}")
        sys.exit(result.returncode)

    print(f"[PASS] {title}")


def staged_files(prefix: str, extensions: tuple[str, ...]) -> list[str]:
    """
    Returns staged files under 'prefix' with matching extensions.
    """

    result = subprocess.run(
        [
            "git",
            "diff",
            "--cached",
            "--name-only",
            "--diff-filter=ACMR",
        ],
        cwd=ROOT_DIR,
        capture_output=True,
        text=True,
        check=True,
    )

    files: list[str] = []

    for file in result.stdout.splitlines():
        if not file.startswith(prefix):
            continue

        if not file.endswith(extensions):
            continue

        files.append(file)

    return files
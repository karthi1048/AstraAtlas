from __future__ import annotations

import os
from pathlib import Path

from scripts.hooks.common import run_step, staged_files

ROOT_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIR = ROOT_DIR / "frontend"

NPM = "npm.cmd" if os.name == "nt" else "npm"


def main() -> None:
    print()
    print("=" * 60)
    print("Running Frontend Quality Checks")
    print("=" * 60)

    prettier_files = [
        file.removeprefix("frontend/")
        for file in staged_files(
            "frontend/",
            (
                ".ts",
                ".tsx",
                ".js",
                ".jsx",
                ".json",
                ".css",
                ".md",
                ".mjs",
            ),
        )
    ]

    if prettier_files:
        run_step(
            "Running Prettier",
            [
                NPM,
                "exec",
                "--",
                "prettier",
                "--check",
                *prettier_files,
            ],
            FRONTEND_DIR,
        )
    else:
        print()
        print("Skipping Prettier (no staged supported files).")

    eslint_files = [
        file.removeprefix("frontend/")
        for file in staged_files(
            "frontend/",
            (
                ".ts",
                ".tsx",
                ".js",
                ".jsx",
                ".mjs",
            ),
        )
    ]

    if eslint_files:
        run_step(
            "Running ESLint",
            [
                NPM,
                "exec",
                "--",
                "eslint",
                "--max-warnings=0",
                *eslint_files,
            ],
            FRONTEND_DIR,
        )
    else:
        print()
        print("Skipping ESLint (no staged JS/TS files).")

    run_step(
        "Running Jest",
        [NPM, "test"],
        FRONTEND_DIR,
    )

    print()
    print("=" * 60)
    print("All frontend quality checks passed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
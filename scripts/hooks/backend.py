from __future__ import annotations

from pathlib import Path

from scripts.hooks.common import run_step, staged_files

ROOT_DIR = Path(__file__).resolve().parents[2]
BACKEND_DIR = ROOT_DIR / "backend"


def main() -> None:
    print()
    print("=" * 60)
    print("Running Backend Quality Checks")
    print("=" * 60)

    python_files = [
        file.removeprefix("backend/")
        for file in staged_files("backend/", (".py",))
    ]

    if python_files:
        run_step(
            "Running Ruff",
            ["uv", "run", "ruff", "check", *python_files],
            BACKEND_DIR,
        )
    else:
        print()
        print("Skipping Ruff (no staged Python files).")

    run_step(
        "Running MyPy",
        ["uv", "run", "mypy", "."],
        BACKEND_DIR,
    )

    run_step(
        "Running Pytest",
        ["uv", "run", "pytest"],
        BACKEND_DIR,
    )

    print()
    print("=" * 60)
    print("All backend quality checks passed.")
    print("=" * 60)


if __name__ == "__main__":
    main()
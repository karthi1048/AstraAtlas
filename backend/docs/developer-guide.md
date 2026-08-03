# AstraAtlas Backend Developer Guide

**Version:** 0.1.0 (Draft)
**Last Updated:** August 2026


# Purpose

Welcome to the AstraAtlas backend.

This guide explains how to set up the development environment, run the application, execute quality checks, and contribute code while following the engineering standards adopted by the project.

The backend follows modern Python development practices and prioritizes maintainability, readability, and long-term reliability over rapid feature development.


# Technology Stack

| Component              | Technology     |
	
| Language               | Python 3.12    |
| Package Manager        | uv             |
| Web Framework          | FastAPI        |
| Testing                | pytest         |
| Coverage               | pytest-cov     |
| Linting & Formatting   | Ruff           |
| Type Checking          | mypy           |
| Git Hooks              | pre-commit     |
| Continuous Integration | GitHub Actions |


# Project Structure

```text
Backend/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── ...
│   └── __init__.py
│
├── tests/
│
├── docs/
│
├── pyproject.toml
├── uv.lock
├── .pre-commit-config.yaml
└── README.md
```

Every Python package in the backend should contain an `__init__.py` file.


# Prerequisites

Install the following before contributing:

* Python 3.12
* Git
* uv


# Initial Setup

Clone the repository.

Navigate into the backend directory.

Create the virtual environment:

```bash
Uv venv
```

Activate the virtual environment.

**Windows**

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
Uv sync
```


# Running the Backend

Start the development server:

```bash
Uv run uvicorn app.main:app –reload
```

The API will be available locally after startup.


# Running Tests

Execute the complete test suite:

```bash
Uv run pytest
```


# Running Test Coverage

Generate terminal coverage:

```bash
Uv run pytest
```

Generate HTML coverage:

```bash
Uv run pytest –cov-report=html
```

The report will be generated inside:

```text
Htmlcov/
```

Open `htmlcov/index.html` in a browser to inspect coverage details.


# Running Ruff

Check the code:

```bash
Uv run ruff check .
```

Automatically fix safe issues:

```bash
Uv run ruff check . –fix
```

Format the project:

```bash
Uv run ruff format .
```


# Running mypy

Run static type checking:

```bash
Uv run mypy .
```


# Running Pre-commit Hooks

Execute every configured hook manually:

```bash
Uv run pre-commit run –all-files
```

Install Git hooks:

```bash
Uv run pre-commit install
```

After installation, quality checks run automatically before every commit.


# Continuous Integration

Every push and pull request automatically runs:

* Ruff
* mypy
* pytest

A contribution should never intentionally bypass CI failures.


# Development Workflow

Recommended workflow:

1. Create a feature branch.
2. Implement the change.
3. Run Ruff.
4. Run mypy.
5. Run pytest.
6. Run pre-commit.
7. Commit.
8. Push.
9. Ensure GitHub Actions passes.


# Engineering Standards

## Code Quality

* Code must pass Ruff.
* Code must pass mypy.
* Code must pass all tests.
* New features should include appropriate tests.


## Architecture

* Keep business logic out of API routes.
* Use centralized configuration.
* Prefer dependency injection where appropriate.
* Keep modules focused on a single responsibility.
* Follow existing project structure.


## Logging

* Use the project’s logging configuration.
* Avoid `print()` for application logging.
* Log meaningful operational information.
* Avoid logging secrets or sensitive information.


## Error Handling

* Raise meaningful exceptions.
* Return consistent API responses.
* Avoid silently ignoring failures.


## Dependencies

Before introducing a dependency, ask:

* Does the standard library already solve this?
* Does it improve maintainability?
* Is it actively maintained?
* Is it necessary?

Every dependency should have a clear purpose.


# Git Commit Guidelines

Follow Conventional Commits whenever possible.

Examples:

```text
Feat: add launch service

Fix: correct parser logic

Docs: improve developer guide

Test: add unit tests for launch service

Refactor: simplify repository layer

Ci: update GitHub Actions workflow
```


# Common Issues

## mypy reports duplicate modules

Cause:

Missing `__init__.py`.

Solution:

Ensure every Python package contains an `__init__.py` file.


## pre-commit cannot locate project files

Cause:

Running hooks outside the backend project.

Solution:

Execute backend tooling from the backend directory.


## Build fails after dependency changes

Run:

```bash
Uv sync
```

To synchronize the environment with `uv.lock`.


# Project Philosophy

AstraAtlas values:

* Accuracy over speed.
* Official data over convenience.
* Simplicity over unnecessary complexity.
* Automation over manual repetition.
* Long-term maintainability over short-term shortcuts.

Every engineering decision should support these principles.


# Contributing

If you would like to contribute:

* Follow the coding standards.
* Keep pull requests focused.
* Write tests when adding functionality.
* Update documentation when behavior changes.
* Ask questions when unsure.

Good documentation and thoughtful discussion are valued as highly as good code.


# Final Note

The backend is intended to become a reliable foundation for the AstraAtlas platform. Every contribution should leave the codebase cleaner, more understandable, and easier to maintain than before.
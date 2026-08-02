# Development Standards

# 1. Coding Standards

### Language Principles

* Write code that is **clear before clever**.
* Prefer readability over micro-optimizations.
* Keep functions focused on a single responsibility.
* Favor composition over inheritance where appropriate.
* Avoid premature abstraction.


### Python Standards

* Use **type hints** for all public functions.
* Follow **PEP 8**.
* Format with **Black**.
* Lint with **Ruff**.
* Use **mypy** for static type checking.
* Prefer dataclasses or Pydantic models where appropriate.


### TypeScript Standards

* Enable strict mode.
* Avoid `any` unless there’s a compelling reason.
* Use descriptive types and interfaces.
* Keep components small and composable.


# 2. Git Workflow

We’ll use a lightweight but professional workflow.

### Main Branch

`main`

Always stable.


### Development Branch

Initially, we **don’t need a permanent `develop` branch**.

Feature branches can merge directly into `main` through pull requests, even if you’re the only contributor.

This keeps the workflow simple.


### Branch Naming

```
Feature/add-nasa-connector
Feature/trust-engine

Fix/api-timeout

Docs/update-readme

Refactor/data-pipeline

Test/connector-tests

Chore/update-dependencies
```

Clear and consistent.


# 3. Commit Messages

We’ll follow the **Conventional Commits** specification.

Examples:

```
Feat: add NASA connector

Fix: handle missing launch dates

Docs: update architecture overview

Test: add mission validation tests

Refactor: simplify trust engine

Chore: update dependencies
```

Benefits:

* Better release notes.
* Easier changelog generation.
* Clear project history.


# 4. Pull Requests

Even as a solo developer, every significant change should go through a pull request.

Why?

Because a PR is more than a merge mechanism.

It’s a review record.

Each PR should answer:

* What changed?
* Why?
* How was it tested?
* Does documentation need updates?
* Does this require a new ADR?


# 5. Testing Philosophy

Our testing pyramid:

```
           E2E
        Integration
           Unit
```

### Unit Tests

Every business rule.


### Integration Tests

Database.

Connectors.

API.


### End-to-End Tests

Critical user journeys.


# 6. Definition of Done

A task is complete only if:

* Feature works.
* Tests pass.
* Lint passes.
* Type checking passes.
* Documentation updated.
* Review completed.
* No known critical issues remain.


# 7. Logging Standards

Every log should be:

* Structured.
* Actionable.
* Free of sensitive information.

Examples:

Good:

```
Connector ‘NASA’ retrieved 42 missions.
```

Bad:

```
Something happened.
```


# 8. Error Handling

Rules:

* Never silently ignore exceptions.
* Raise meaningful errors.
* Log enough context for debugging.
* Avoid exposing internal details through public APIs.


# 9. Security Standards

This connects directly to **Trust by Design**.

Initial rules:

* Never commit secrets.
* Use environment variables.
* Validate all external input.
* Escape output where appropriate.
* Review dependencies regularly.
* Follow the principle of least privilege.

Future versions can add dependency scanning, secret scanning, and security audits.


# 10. Documentation Standards

Every significant feature should include:

* User-facing documentation (if applicable).
* Developer documentation (if applicable).
* Architecture updates (if needed).
* ADR (if it changes a major decision).


# 11. Code Review Principles

When reviewing code, ask:

1. Is it correct?
2. Is it understandable?
3. Is it maintainable?
4. Is it secure?
5. Does it align with ADR-0001?
6. Are tests sufficient?
7. Is documentation updated?


# 12. Release Standards

Before any release:

* CI passes.
* Tests pass.
* Documentation complete.
* CHANGELOG updated.
* Version bumped.
* Release notes written.
* Security review completed (for major releases).

This continues our philosophy that documentation is part of the release itself.


# 13. Contributor Values

Beyond technical rules, I’d like AstraAtlas to have cultural values:

* Be respectful.
* Be curious.
* Welcome questions.
* Explain decisions.
* Share knowledge.
* Accept constructive feedback.
* Prefer evidence over opinion.

These values help create a healthy open-source community.


## Engineering Checklists

Rather than relying on memory, we’ll create checklists for recurring work.

Examples:

* New Connector Checklist
* New API Endpoint Checklist
* Release Checklist
* Security Review Checklist
* Documentation Checklist

This reduces mistakes and makes onboarding easier.
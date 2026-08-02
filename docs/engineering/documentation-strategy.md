# Documentation Strategy

Before writing documents, let’s define **what kinds of knowledge** AstraAtlas needs to preserve.

I think there are six categories.

# 1. Project Documentation

This answers:

	**What is AstraAtlas?**

Audience:

* First-time visitors
* Contributors
* Potential users

Files:

```text
README.md
ROADMAP.md
CHANGELOG.md
LICENSE
```

# 2. Engineering Documentation

Answers:

	**Why is AstraAtlas built this way?**

Audience:

* Contributors
* Future maintainers

Contains:

```text
Architecture

ADRs

Technology decisions

Design rationale
```

This is the documentation engineers read.


# 3. Developer Documentation

Answers:

	**How do I develop AstraAtlas?**

Examples:

```text
Local setup

Running tests

Coding standards

Creating connectors

Release process
```


# 4. User Documentation

Answers:

	**How do I use AstraAtlas?**

Eventually includes:

* Search
* APIs
* Trust Cards
* Data explanations
* Tutorials


# 5. Operations Documentation

Answers:

	**How do we run AstraAtlas?**

Examples:

* Deployment
* Monitoring
* Backups
* Recovery
* Infrastructure
* Security


# 6. Historical Documentation

This category is often forgotten.

But it aligns perfectly with your legacy goal.

Examples:

```text
Release Notes

Migration Guides

Deprecated Features

Major Milestones
```

Future contributors should understand how AstraAtlas evolved.


# Documentation Hierarchy

I propose this structure:

```text
Docs/
│
├── adr/
├── architecture/
├── development/
├── api/
├── operations/
├── releases/
├── user-guide/
└── assets/
```

Every document has a clear home.


# Documentation Standards

Every document should answer four questions.

## Why?

Why does this exist?


## What?

What does it describe?


## Who?

Who should read it?


## When?

When should it be updated?

This keeps documentation purposeful rather than verbose.


# Versioning Documentation

Not all documentation changes at the same pace.

| Type          | Update Frequency        |
	
| Constitution  | Almost never            |
| ADRs          | When decisions are made |
| Architecture  | Occasionally            |
| API Docs      | Frequently              |
| User Guide    | As features grow        |
| Release Notes | Every release           |
| Roadmap       | Every milestone         |

This helps us understand which documents are stable and which are living.


# Documentation Review Policy

A feature is **not complete** until:

* Implementation is complete.
* Tests pass.
* Documentation is updated.

Documentation is part of the Definition of Done.


# ADR Index

As ADRs grow, I’d like to maintain an index.

For example:

```text
ADR-0001 Constitution

ADR-0002 Repository Structure

ADR-0003 Technology Stack

ADR-0004 Connector Architecture

ADR-0005 Trust Engine
```

This creates a chronological history of architectural decisions.


# Glossary

Space terminology can be confusing.

I’d like AstraAtlas to maintain a glossary explaining terms such as:

* Payload
* Launch Window
* Orbit
* LEO
* GEO
* Mission
* Vehicle
* Booster

This supports learners and educators, two of our core personas.


## Source Documentation

Remember our principle:

	Official Sources Only.

I think every connector deserves its own documentation.

Example:

```text
Docs/connectors/

NASA.md

ISRO.md

ESA.md

JAXA.md
```

Each file could describe:

* Official API or data source.
* Authentication (if any).
* Rate limits.
* Update frequency.
* Data fields.
* Known limitations.
* Links to official documentation.

This means every source we rely on is itself documented.

## Decision Logs

Not every decision deserves an ADR.

Some are small.

I’d like a lightweight log:

```text
Decision Log

2026-08-14

Changed launch status colors.

Reason:

Accessibility improvements.
```

This prevents ADRs from becoming cluttered with minor changes while still preserving history.


# Documentation Principles

### Documentation as Code

Documentation lives alongside code, is version-controlled, and reviewed like any other contribution.


### Documentation Before Complexity

When introducing a complex subsystem, document the design before implementing it.


### Explain the Why

Focus on the reasoning behind decisions, not just the mechanics.


### Keep It Discoverable

A contributor should know where to find the answer without searching through dozens of files.


### Evolve with the Project

Documentation is a living asset and should reflect the current state of AstraAtlas.
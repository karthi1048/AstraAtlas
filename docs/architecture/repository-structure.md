# Repository Structure

## First Decision: Monorepo vs Multiple Repositories

**Decision:** ✅ **Monorepo**


# Repository Philosophy

Every top-level directory should represent a **major capability**.

If someone clones the repository for the first time, they should immediately understand its organization.


# Proposed Repository Structure

```text
Astraatlas/
│
├── backend/                 # FastAPI application
│
├── frontend/                # Next.js application
│
├── docs/                    # Project documentation
│
├── infra/                   # Infrastructure & deployment
│
├── scripts/                 # Utility and maintenance scripts
│
├── tests/                   # Cross-project integration tests
│
├── .github/                 # GitHub workflows & templates
│
├── LICENSE
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CODE_OF_CONDUCT.md
└── ROADMAP.md
```


# Backend Structure

This is the heart of AstraAtlas.

```text
Backend/
│
├── app/
│   ├── api/
│   ├── domain/
│   ├── application/
│   ├── infrastructure/
│   ├── connectors/
│   ├── trust/
│   ├── scheduler/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── core/
│   └── main.py
│
├── migrations/
│
├── tests/
│
└── pyproject.toml
```

### Why these folders?

* **domain/** → Business concepts like Mission, Launch, Satellite.
* **application/** → Use cases and workflows.
* **connectors/** → NASA, ESA, ISRO, etc.
* **trust/** → Trust Engine and provenance logic.
* **infrastructure/** → Database, APIs, storage, external services.
* **scheduler/** → Background jobs.
* **core/** → Shared configuration and foundational utilities.


# Frontend Structure

We’ll keep it clean and scalable.

```text
Frontend/
│
├── app/
├── components/
├── features/
├── lib/
├── services/
├── hooks/
├── styles/
├── public/
└── tests/
```

# Documentation Structure

I think documentation deserves first-class treatment.

```text
Docs/
│
├── adr/
├── architecture/
├── api/
├── guides/
├── development/
├── operations/
├── releases/
└── assets/
```

# Infrastructure

```text
Infra/
│
├── docker/
├── compose/
├── nginx/
├── monitoring/
└── deployment/
```

# Scripts

Scripts should have a narrow purpose.

```text
Scripts/
│
├── setup/
├── maintenance/
├── data/
└── release/
```

# Tests

Testing should mirror the codebase.

```text
Tests/
│
├── integration/
├── e2e/
└── performance/
```

Unit tests stay close to the modules they test inside `backend/tests` or `frontend/tests`. 

## “No Junk Drawer” Rule

I would like AstraAtlas to avoid directories like:

* helpers/
* misc/
* temp/
* old/
* backup/

If we can’t explain why a folder exists, it shouldn’t exist.

Instead, we create folders based on responsibilities.


# Repository Growth Strategy

We don’t create every folder on Day 1.

We create them **when they’re needed**, but we already know where they belong.

This keeps the repository tidy while preserving a clear long-term structure.
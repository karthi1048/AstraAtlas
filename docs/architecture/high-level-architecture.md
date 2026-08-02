# High-Level Architecture

## Architecture Principle

	**”AstraAtlas is a platform composed of independent capabilities, not one large application.”**

This single decision will influence every directory, every module, every API, and every deployment.


```
                AstraAtlas Platform


         │         Web Frontend          │
	
                        │
                 REST API / Future GraphQL
                        │
	
        │         Application Layer      │
	
                        │
	
	
Connectors         Data Services      User Services
	
			

          Validation      Trust & Provenance
                   │
             PostgreSQL Database
                   │
         Background Scheduler/Workers
                   │
             Official Data Sources
```


# Architecture Layers

## Layer 1 – Presentation

Responsibilities:

* Website
* API documentation
* Public API
* Admin interface (future)

Knows nothing about NASA, ISRO, or databases.


## Layer 2 – Application

Coordinates workflows.

Example:

```
Fetch Launches

↓

Normalize

↓

Validate

↓

Store

↓

Update Search
```

No HTTP.

No SQL.

Only business workflows.


## Layer 3 – Domain

This is the heart.

Contains concepts like:

* Mission
* Satellite
* Launch
* Agency
* Trust Card
* Verification

This layer should survive even if we changed FastAPI tomorrow.


## Layer 4 – Infrastructure

Contains:

* PostgreSQL
* FastAPI
* Redis
* APScheduler
* Docker

Infrastructure serves the domain—not the other way around.


## Connector Architecture

Every source should implement a common interface.

For example:

```
OfficialSourceConnector

Fetch_agencies()

Fetch_missions()

Fetch_launches()

Fetch_satellites()
```

Then:

```
NASAConnector

ISROConnector

ESAConnector

JAXAConnector
```

Each one only knows how to communicate with *its* source.

The rest of AstraAtlas doesn’t need to care.


## Data Pipeline

Rather than:

```
Fetch

↓

Database
```

We prefer:

```
Official Source

↓

Connector

↓

Normalizer

↓

Validator

↓

Trust Engine

↓

Database

↓

API

↓

Frontend
```

Every step has one responsibility.


And AstraAtlas deserves its own **Trust Engine**.

Instead of every connector deciding whether data is trustworthy:

```
NASA Connector

↓

Raw Mission

↓

Trust Engine

↓

Trust Level

↓

Provenance

↓

Verification Metadata

↓

Database
```

That way, every source is evaluated consistently.

The Trust Engine becomes a central piece of AstraAtlas’s identity.


# Future Component

## Change Detection Engine

Imagine this:

NASA changes a launch date.

The connector retrieves new data.

Instead of simply updating the database:

```
Old Version

↓

New Version

↓

Compare

↓

Generate Change Event

↓

Store History

↓

Notify Users (future)
```

This capability could later power:

* History timelines
* Notifications
* Analytics
* Audit trails

Without redesigning the platform.


# Internal Communication

For now:

Simple Python method calls.

Later, if AstraAtlas grows significantly:

* Event bus
* Message queues

But not before there’s a real need.

Again:

	**Simplicity before scale.**


# Proposed Architectural Principles

### Domain First

Business concepts come before frameworks.


### Modular by Default

Each capability should have a clear boundary.


### Replaceable Infrastructure

Changing FastAPI, PostgreSQL, or Redis should not require rewriting the domain.


### Single Responsibility

Every module should have one clear purpose.


### Explicit Dependencies

Dependencies should point inward toward the domain, not outward.


### Testability

Every major capability should be testable in isolation.
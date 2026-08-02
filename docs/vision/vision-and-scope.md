# Vision & Scope

**Version:** 1.0
**Status:** Active
**Last Updated:** 2026-08-01


# 1. Purpose

This document defines the long-term vision, scope, intended audience, and boundaries of AstraAtlas.

Its purpose is to ensure every feature, architectural decision, and future roadmap aligns with the platform’s mission and constitutional principles.


# 2. Vision

	**To become the world’s most trusted open-source platform for verified space mission and satellite data, empowering learners, researchers, developers, educators, and space enthusiasts through transparency, reliability, and open access to official information, while inspiring future generations to build upon open knowledge, advance space information systems, and contribute to humanity’s understanding of space.**


# 3. Scope

## 3.1 Core Scope

These capabilities define AstraAtlas.

Without them, AstraAtlas would not fulfill its mission.

### Agencies

Maintain authoritative information about:

* Space agencies
* Launch providers
* Mission operators

Examples include (but are not limited to):

* NASA
* ESA
* ISRO
* JAXA
* SpaceX
* Rocket Lab
* ULA
* Arianespace

Support for additional organizations will grow over time.


### Missions

Maintain verified information including:

* Mission overview
* Status
* Objectives
* Timeline
* Official references
* Mission history


### Launches

Maintain:

* Upcoming launches
* Historical launches
* Launch vehicles
* Launch sites
* Launch status
* Launch history


### Satellites

Maintain:

* Satellite specifications
* Purpose
* Operators
* Orbit
* Launch mission
* Mission status


### Data Provenance

Every published record should identify:

* Source organization
* Official reference
* Retrieval timestamp
* Verification timestamp
* Data version


### Search

Users should be able to search across:

* Agencies
* Missions
* Launches
* Satellites


### Public API

The platform should expose documented APIs for developers and researchers.


# 3.2 Extended Scope

The following features support AstraAtlas’s long-term vision but are not required for the initial stable release.

Examples include:

* Launch countdowns
* Interactive mission timelines
* Satellite orbit visualization
* Mission comparison
* Historical analytics
* Notifications
* RSS feeds
* Email subscriptions
* Developer SDKs
* Data exports
* Interactive world maps
* Mobile applications
* AI-assisted summaries (strictly based on official information)
* Community-built integrations


# 3.3 Out of Scope

AstraAtlas intentionally does **not** aim to become:

* A rumor aggregation platform
* A speculative launch tracker
* A click-driven news website
* A social media platform
* A discussion forum
* A content farm
* A platform that republishes unofficial information as fact

These boundaries exist to preserve trust and maintain the project’s focus.


# 4. Trust Model

Trust is the defining characteristic of AstraAtlas.

Every published record should communicate not only **what** is known, but **how** it is known.

## Trust Levels

### 🟢 Official

Published directly by an official organization.


### 🔵 Verified

Confirmed by multiple official sources.


### 🟡 Historical

Archived official information preserved for historical reference.


### ⚪ Pending Verification

Information has been retrieved but is awaiting confirmation before being promoted to an official or verified state.


Information that cannot be verified through official sources should not be published as factual content.


# 5. Trust Card

Every mission, launch, satellite, or agency page should eventually provide a Trust Card containing metadata such as:

* Trust Level
* Source Organization
* Official References
* Retrieval Time
* Last Verification Time
* Data Version
* Verification Status

The Trust Card is intended to make data provenance visible and understandable to every user.


# 6. User Personas

## Learners

Need:

* Easy-to-understand information
* Official references
* Educational resources

Success means helping people discover and understand space exploration.


## Space Enthusiasts

Need:

* Upcoming launches
* Mission updates
* Historical information

Success means becoming a trusted daily reference.


## Researchers

Need:

* Reliable historical records
* Provenance
* Search
* Data consistency

Success means providing trustworthy data suitable for research and analysis.


## Developers

Need:

* Stable APIs
* Documentation
* Machine-readable data

Success means enabling others to build new tools on top of AstraAtlas.


## Educators

Need:

* Accurate information
* Historical context
* Official references

Success means making AstraAtlas a dependable educational resource.


# 7. Success Metrics

The platform measures success through quality rather than feature count.

Examples include:

* Every published record links to its official source.
* Every significant data change is traceable.
* Public APIs are documented.
* Core modules have automated tests.
* Continuous Integration passes before release.
* Documentation evolves alongside implementation.
* Major engineering decisions are recorded as ADRs.
* Core functionality remains buildable using open-source tools.


# 8. Guiding Question

Before implementing any significant feature, contributors should ask:

	**Does this make AstraAtlas more trustworthy, more useful, or more maintainable?**

If the answer is no, the feature should be reconsidered or deferred.


# 9. Long-Term Vision

AstraAtlas is intended to evolve from a data platform into a trusted ecosystem for open space information.

Potential future capabilities include:

* Public developer APIs
* Historical archives
* Educational content
* Analytics
* Open datasets
* Community contributions
* Research integrations
* New official data connectors
* Mobile applications

Growth should always preserve the principles established in ADR-0001.


# 10. Closing Statement

	**AstraAtlas is more than a software platform. It is a commitment to openness, transparency, engineering excellence, and trustworthy access to humanity’s journey into space. Every feature should strengthen that commitment, and every release should move the platform closer to becoming a lasting contribution to the global open-source and space communities.**
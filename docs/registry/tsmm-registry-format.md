---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.10.0
tier: 0
---

# TSMM Registry Format

The TSMM Registry Format is a portable publication format for TSMM artifacts. It is designed to answer a very practical question:

**How does an ecosystem publish its trust topology, profiles, and bindings in a way that tooling can consume?**

A machine-readable graph is useful. A binding file is useful. A profile is useful. A registry format is what lets them travel together without becoming a folder full of meaning-adjacent JSON.

## Purpose

The registry format provides a simple index over TSMM artifacts such as:

- graph instances
- ecosystem profiles
- ecosystem bindings
- policy or evidence artifacts
- registry service descriptors

## Core properties

A registry document contains:

- `registryId` — stable identifier for the published registry
- `label` — human-readable title
- `entries` — index of published artifacts
- `defaultProfile` — optional default profile name for consumers
- `publisher` and `version` — operational metadata

Each entry includes:

- `id`
- `kind`
- `label`
- `location`
- `status`
- optional profile or binding target metadata

## Why this matters

The registry format turns TSMM into something ecosystems can publish, not merely describe. That is an important strategic step. Once a model can be published, discovered, and consumed, it starts behaving less like a whitepaper and more like infrastructure.

## Related artifacts

- `schemas/tsmm-registry.schema.json`
- `examples/registries/tsmm-registry-example.json`
- `scripts/validate_tsmm_registry.py`

---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.24.0
tier: 1
title: TSMM Authority Graph
permalink: /model/authority-graph.html
parent: Model
grand_parent: Documentation
---

# TSMM Authority Graph

## Purpose

This document introduces a machine-readable authority graph for TSMM so authority origin, delegation edges, scope constraints, and revocation behavior can be described explicitly rather than left to prose.

## Why it matters

Many trust systems describe authority as if it were a static attribute. In practice, authority moves. It is granted, narrowed, delegated, suspended, revoked, and consumed by downstream verifiers. If the graph is not explicit, implementers end up guessing where legitimacy begins and where it ends.

## What the model captures

- authority origin
- delegated actors
- policy constraints
- registry publication surfaces
- verifier touchpoints
- revocation rules and propagation expectations

## Machine-readable artifact

- Model: `model/authority-graph.yaml`
- Schema: `schemas/tsmm-authority-graph.schema.json`

## Modeling note

The graph is intentionally compact. It does not try to reproduce every protocol step. It focuses on the governance-significant structure that downstream systems need in order to reason about authority.

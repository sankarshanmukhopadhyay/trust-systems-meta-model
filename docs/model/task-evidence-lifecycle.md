---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.24.0
tier: 0
title: Task Evidence Lifecycle Model
permalink: /model/task-evidence-lifecycle.html
parent: Model
grand_parent: Documentation
---


# Task Evidence Lifecycle Model

Task state is governance state when a task may produce an operational effect. TSMM v0.19.0 generalizes A2A's task lifecycle into a reusable evidence lifecycle that can be applied across agent protocols, workflow engines, registry operations, and delegated-action systems.

## Lifecycle states

| State | Governance significance | Minimum evidence expectation |
| --- | --- | --- |
| `submitted` | Attempted work begins | Request metadata |
| `working` | Execution has started | Execution trace or processing reference |
| `input-required` | Required facts are missing | Clarification request or missing-fact notice |
| `auth-required` | Authority boundary reached | Authorization checkpoint |
| `completed` | Output or effect produced | Artifact reference |
| `failed` | No effect or partial effect | Failure reason |
| `canceled` | Execution stopped | Cancellation authority or reason |
| `rejected` | Policy denied the task | Decision receipt |

## Normative requirements

- A task evidence lifecycle **MUST** identify task, context, provider, current state, and evidence policy.
- A transition to `auth-required` **MUST** include an authorization checkpoint reference.
- A transition to `completed` **MUST** include at least one artifact reference.
- A transition to `failed` **MUST** include a failure reason.
- A transition to `canceled` **MUST** include cancellation authority or equivalent reason.
- A transition to `rejected` **MUST** include a decision receipt reference.
- Evidence references **SHOULD** be independently dereferenceable in an evidence bundle, conformance report, or audit record.

## Schema and example

- Schema: `schemas/tsmm-task-evidence-lifecycle.schema.json`
- Example: `examples/task-evidence-lifecycle-instance.json`
- Valid vector: `validation/test_vectors/valid/task-evidence-lifecycle-valid.json`
- Invalid vectors:
  - `validation/test_vectors/invalid/task-evidence-lifecycle-missing-receipt.json`
  - `validation/test_vectors/invalid/task-evidence-lifecycle-invalid-transition.json`

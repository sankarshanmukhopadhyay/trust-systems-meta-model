---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: v0.21.0
tier: 0
---


# Task Evidence Pattern

## Intent

Use this pattern when a task, workflow, or agent action may produce an output or side effect that requires auditability.

## Pattern

1. Treat task state as a governance state machine.
2. Identify which state transitions cross authority, evidence, or user-awareness boundaries.
3. Require receipts or artifacts for trust-significant transitions.
4. Preserve evidence references for replay and audit.
5. Reject or downgrade tasks that cannot produce required evidence.

## Implementation artifacts

- `docs/model/task-evidence-lifecycle.md`
- `schemas/tsmm-task-evidence-lifecycle.schema.json`
- `examples/task-evidence-lifecycle-instance.json`

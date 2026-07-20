---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 0
---


# Governed A2A-Class Discovery Walkthrough

This walkthrough demonstrates how TSMM v0.19.0 generalizes A2A implementation patterns without becoming an A2A protocol specification.

## Scenario

An enterprise procurement agent needs to call a contract-review agent. The client discovers the provider through a curated enterprise registry, requests an authenticated extended descriptor, negotiates a traceability extension, and then starts a review task. The task pauses for secondary authorization before producing a bounded risk-summary artifact.

## Step 1: Discover the descriptor

Use `examples/agent-discovery-governance-instance.json` to record:

- descriptor source
- discovery mode
- freshness policy
- integrity verification
- failure behavior
- evidence references

## Step 2: Negotiate capability use

Use `examples/capability-negotiation-instance.json` to record:

- requested and accepted input/output modes
- required and optional extensions
- rejected extension rationale
- authorization scope
- policy decision reference

## Step 3: Track task evidence

Use `examples/task-evidence-lifecycle-instance.json` to record:

- task state transitions
- authorization checkpoint
- decision receipt
- output artifact reference
- audit outcome

## Step 4: Validate

Run:

```bash
python scripts/validate_examples.py
python scripts/validate_test_vectors.py
python scripts/check_schema_coverage.py
python scripts/check_docs.py
```

## Enterprise interpretation

This walkthrough turns a protocol interaction into an assurance trail. The important result is not that two agents exchanged messages. The important result is that discovery, capability negotiation, authorization, task progression, and output production are all captured as reviewable governance events.

---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
title: TIS Executable Artifact Walkthrough
permalink: /examples/tis-executable-artifact-walkthrough.html
parent: Examples
grand_parent: Documentation
---

# TIS Executable Artifact Walkthrough

This walkthrough demonstrates how TSMM semantics become executable Trust Infrastructure Schemas artifacts without losing governance meaning.

## Scenario

A relying-party verifier is asked to allow `Example Agent Beta` to submit a bounded status update. The verifier must not treat registry publication or identity-state evidence as automatic runtime authorization.

## Step 1: Model the system in TSMM

Use `examples/cross-repo/trust-decision-system.graph.json` to identify:

- the agent;
- the sponsor authority;
- the relying-party verifier;
- the registry;
- the policy;
- the evidence bundle;
- the decision receipt.

## Step 2: Project authority into a TIS boundary

The sponsor-to-agent authority edge is projected into `01-authority-boundary.example.json`. This constrains scope and requires revocation checks.

## Step 3: Package evidence

The evidence set is packaged in `02-evidence-bundle-manifest.example.json`. This makes evidence replayable and auditable.

## Step 4: Record verifier evaluation

The verifier records assessment output in `03-evaluation-envelope.example.json`. This captures controls checked, result, assurance level, semantic bindings, and authority boundary context.

## Step 5: Issue a decision receipt

The relying-party result is recorded in `04-decision-receipt.example.json`. This is the audit pivot because it binds policy, authority, evidence, result, effect, and timestamps.

## Step 6: Publish registry state

The discoverable registry state is published in `05-registry-entry.example.json`. The entry makes the artifact chain discoverable but does not authorize future runtime action by itself.

## Validation evidence

The TIS repository validates the composition artifacts through `tools/validate-conformance.js` and the artifact coverage manifest. TSMM validates the graph and binding artifacts through the repository validation scripts.

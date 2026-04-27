---
owner: maintainers
last_reviewed: 2026-04-27
applicable_version: v0.18.0
tier: 1
---

# TSMM to OASF Binding

## Purpose

This binding explains how **Open Agentic Schema Framework (OASF)** publication artifacts can be interpreted through TSMM.

OASF does not try to be a trust meta model. It provides a machine-readable schema system for describing agents, capabilities, interactions, and evaluation artifacts. TSMM sits one layer above that. It defines the semantics of trust-relevant entities, authority, policy, evidence, verification, and effect.

The practical integration point is therefore not substitution but **addressability**.

TSMM becomes assurance-addressable when an OASF record, module, or evaluation artifact can point to TSMM-relevant concepts in a stable way. That lets a downstream assurance system reason about what the described thing is, who is accountable for it, which controls apply, and what evidence can be replayed later.

## Binding posture

- **TSMM** supplies the semantic layer.
- **OASF** supplies a publication and extension surface for agent descriptions and evaluation outputs.
- **ANAB** can publish domain-specific naming and operator-binding expectations through an OASF-facing profile.
- **DCAS** can consume OASF-described records and produce evaluation outputs that remain traceable to TSMM abstractions.

## Core mappings

| OASF concept | TSMM concept | Binding strength | Why it matters |
| --- | --- | --- | --- |
| OASF record | ServiceDescriptor | approximate | Makes an agent publication surface legible to TSMM-aware assurance workflows. |
| OASF publisher | Operator | approximate | Preserves accountability for who stands behind a published record. |
| OASF module / extension | ExtensionContract | exact | Allows bounded ecosystem semantics, including assurance-facing modules, to travel with the record. |
| OASF a2a_data | InteractionContext | approximate | Connects OASF interaction metadata to TSMM interaction and trust-decision surfaces. |
| OASF evaluation_report | Assessment | exact | Lets evaluation output be interpreted as a structured assessment artifact. |
| OASF referred_evaluation | EvidenceArtifact | exact | Preserves references to reusable evidence for later review and contestability. |

## Publication guidance relationship

This binding is paired with [OASF publication guidance](../profiles/oasf-publication-guidance.md). The binding defines semantic equivalence and expected behavior. The publication guide shows how to package those semantics so a published profile stays useful to downstream evaluators, trust registries, or procurement review workflows.

## What this binding does not do

This binding does not redefine OASF terminology, and it does not require OASF to adopt TSMM classes directly in its core schema. The goal is narrower and more useful: **make OASF-described agents and evaluations portable into assurance workflows without semantic drift**.

## Implementation pattern

A practical three-repo composition looks like this:

1. **TSMM** supplies stable semantic anchors for entities, operator relationships, evidence, assessment, and trust effects.
2. **ANAB** defines a domain profile that says which controls and evidence pointers should be published for a named agent.
3. **DCAS** consumes the OASF-described record and attached references, evaluates the published controls, and emits an assessment artifact.

That pattern keeps the stack clean:

- OASF is the publication surface.
- TSMM is the semantic spine.
- ANAB is the domain baseline.
- DCAS is the evaluation method.

## Publication minimums

A TSMM-aware OASF publication should expose enough information to recover the following questions without bespoke interpretation:

- who is accountable for the publication surface
- what is being described or evaluated
- which trust profile, policy bundle, or baseline applies
- where the evidence or referred evaluation artifacts live
- how consumers discover revocation, expiry, or status change semantics

## Machine-readable artifact

See `bindings/oasf/tsmm-oasf-binding.json`.

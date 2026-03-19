---
owner: maintainers
last_reviewed: 2026-03-19
applicable_version: v0.12.0
tier: 1
---

# TSMM Attention Governance Model

## Purpose

TSMM is effect-centered. In many agentic systems, the effect in question is not only a database write, credential issuance, or policy decision. The effect may be **whether a signal is allowed to interrupt, reach, or shape a principal at all**.

v0.12.0 therefore adds an explicit attention-governance framing to help model systems where agents filter, prioritize, stage, or price inbound communication before it becomes actionable for a human principal.

## Core claim

Attention is not just a UX concern. In agent-mediated systems, attention routing is a trust decision surface.

A system that decides:

- which inbound items are admitted
- which are delayed
- which are escalated
- which are priced, filtered, or rejected
- which are routed to a proxy agent rather than the principal

is already participating in governance.

## TSMM alignment

Attention governance can be described with existing TSMM abstractions plus extension fields introduced in v0.12.0:

- **Entity / Agent** — the actor filtering or prioritizing signals
- **Delegation** — the principal’s grant allowing a gateway, twin, or assistant to act on their behalf
- **Policy** — the rules for interruption, urgency, sender reputation, and routing
- **Execution Context** — current mode, time sensitivity, user presence, workload, and risk tier
- **Action** — admit, defer, reject, summarize, escalate, or reroute a signal
- **Effect** — the actual delivery, suppression, or redirection outcome
- **Trace Record** — the evidence trail explaining why the signal path was handled that way
- **Attention Policy** — the extension object that describes interruption budget, delivery posture, and escalation behavior

## Typical patterns

### 1. Attention gateway

An attention-gateway agent screens inbound messages or requests and applies policy before the principal is interrupted.

### 2. Predictive side-car

A predictive agent stages likely next actions or likely next tabs without committing effects unless later approved or selected.

### 3. Identity proxy

A digital twin or representative agent receives requests, negotiates or deflects them, and routes only bounded, policy-compliant opportunities onward.

## Why this belongs in TSMM

Trust systems increasingly mediate not only identity, authority, and evidence, but also **which demands on a person’s time are judged legitimate enough to surface**. That makes attention governance a natural extension topic for TSMM, especially in agentic deployments.

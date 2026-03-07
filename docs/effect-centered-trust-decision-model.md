---
owner: maintainers
last_reviewed: 2026-03-07
applicable_version: v0.5.0
tier: 1
---

# TSMM Effect-Centered Trust Decision Model

## 1. Purpose

This document explains the trust-decision logic at the heart of TSMM.

The governing question is:

> Should a system allow a specific effect to occur right now, given the acting role, bounded authority, artifact state, governance context, policy, profile, requirements, controls, evidence, assessment, and verification results?

## 2. Why effect comes first

Traditional identity systems often ask who a participant is. TSMM centers the harder runtime question: should this specific action, signal, or artifact produce an effect under present conditions?

## 3. Trust decision inputs

A TSMM trust decision may take inputs from:

- acting entity and role
- bounded authority and scope
- relevant artifacts and claims
- governance context
- active policy
- applicable profile and requirements
- controls and threat model
- evidence available
- assessment results
- verification results
- lifecycle state such as suspension, revocation, expiry, or remediation

## 4. Decision outcomes

A TSMM trust decision can produce outcomes such as:

- accept
- reject
- warn
- downgrade
- quarantine
- defer to human review
- require stronger evidence

## 5. Decision-to-effect principle

A trust decision is not complete until it is tied to an effect.

Examples:

- display a result with warning
- deny an automated action
- require a higher-assurance path
- suppress a misleading trust signal
- route a delegated action to human review
- allow informational use but block rights-affecting action

## 6. Design implication

This is why TSMM centers effect rather than identity. Identity, claims, and controls are inputs. The governance-critical output is whether a defined effect should happen.

---
owner: maintainers
last_reviewed: 2026-04-27
applicable_version: v0.18.0
tier: 1
---

# Runtime Governance Walkthrough

This walkthrough shows how TSMM v0.18.0 models a delegated agent attempting to invoke a side-effecting financial tool.

## Scenario

An invoice-adjustment agent has delegated authority to submit bounded invoice adjustments. The agent attempts to call the Accounts Adjustment API. The system must decide whether the effect can happen before the call is executed.

## Step 1: Identify the actor and requested effect

The runtime governance envelope records:

- the requesting actor: `entity.agent`
- the role: `role.delegate`
- the requested effect: `effect.adjust-invoice`
- the target: `entity.tool`

## Step 2: Identify the trust boundary

The attempted tool call crosses from a delegated-agent runtime into a financial system of record.

Boundary:

```text
boundary.agent-to-accounts-api
```

This matters because boundary crossings are where local capability becomes governed effect.

## Step 3: Evaluate authority and delegation

The envelope references:

```text
auth.adjust-invoice
artifact.delegation.invoice-adjustment
```

The decision engine checks whether the authority is active, within scope, and linked to the requesting actor.

## Step 4: Apply policy and evidence

The envelope requires at least one policy reference and at least one evidence reference. In the example, the policy is:

```text
policy.pre-effect-financial-tool-use
```

Evidence includes the delegation signature and fresh revocation status.

## Step 5: Check revocation freshness

The revocation check is not optional. A stale or unavailable status cannot be treated as equivalent to active authority.

In the valid example, the revocation state is:

```text
fresh-active
```

In the revocation propagation example, the authority is revoked and the effect is blocked.

## Step 6: Admit or block the effect

The valid runtime envelope allows the effect because authority, policy, evidence, and revocation freshness align. The revocation propagation system blocks the effect because authority was revoked.

## Step 7: Emit a decision receipt

The decision receipt records the reason, evidence, authority basis, policy, boundary, revocation state, and effect admission. This turns the runtime action into an auditable governance event.

Relevant files:

```text
examples/runtime-governance-boundary-instance.json
examples/decision-receipt-runtime-example.json
examples/systems/revocation-propagation-system.json
```

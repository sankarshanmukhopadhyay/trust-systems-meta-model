---
owner: maintainers
last_reviewed: 2026-03-09
applicable_version: v0.6.0
tier: 1
---

# Multi-Agent Coordination Pattern

## Pattern summary

A principal agent delegates a bounded sub-task to one or more subordinate agents. Each subordinate agent operates under a separate delegation scoped to the sub-task. Policy evaluates each delegation independently before any agent produces an effect.

## TSMM mapping

- Actor: principal agent, one or more subordinate agents, originating principal
- Authority: chained delegations, each independently scoped and revocable
- Artifact: delegation artifacts, per-agent trace records
- Policy: coordination policy governing delegation depth, scope inheritance, and oversight mode escalation
- Evidence: aggregated trace records and per-agent execution logs
- Effect: allow, block, downgrade, or route the composite outcome

## Key structural rules

**Delegation does not chain implicitly.** A principal agent that has been delegated authority cannot re-delegate to a subordinate unless the originating delegation explicitly permits sub-delegation. Implicit scope inheritance is a governance failure mode.

**Each subordinate delegation must be independently evaluable.** Policy should be able to evaluate any single delegation in the chain without requiring the full chain to be resolved first. This prevents circular delegation and keeps revocation tractable.

**Oversight mode escalates to the strictest level present in the chain.** If any delegation in a coordination chain carries an `approval-gated` or `manual` oversight mode, the composite workflow inherits that constraint. Autonomous sub-agents do not override a more restrictive parent oversight setting.

**Trace records aggregate across agents.** A coordination-level trace record should reference all per-agent trace records to provide a single audit entry point for the composite effect.

## Sequence

```text
Originating principal
  -> grants delegation with sub-delegation permission
    -> principal agent receives delegation
      -> principal agent issues scoped sub-delegation to subordinate agent(s)
        -> each subordinate agent requests an action
          -> policy evaluates each delegation independently
            -> oversight mode check (escalate to strictest in chain)
              -> trust decision per agent
                -> effects produced (or blocked) per agent
                  -> per-agent trace records stored
                    -> coordination trace record aggregates all agent records
```

## Example scenario

A procurement workflow delegates to a `SummaryAgent`, which is permitted to sub-delegate a data-fetch sub-task to a `LookupAgent`. The `SummaryAgent` holds a delegation scoped to `prepare supplier risk summary` with `sub-delegation: permitted`. The `LookupAgent` holds a separate delegation scoped to `fetch supplier record` only. Policy evaluates each independently. The `SummaryAgent` operates under `sampled-review`. The `LookupAgent` operates under `autonomous`. The composite oversight mode escalates to `sampled-review` because that is the strictest mode present.

## TSMM core mappings

- Each agent maps to a TSMM **Entity** with `type: software-agent`
- Each delegation maps to the agentic extension **Delegation** object with an optional `subDelegationPermitted` flag
- Each action maps to the agentic extension **Action** object referencing the relevant delegation
- The coordination trace record maps to a TSMM **Evidence** object referencing all per-agent **Trace Records**
- The composite trust decision maps to a TSMM **Trust Decision** with multiple `effectRefs`

## Non-goals

This pattern does not define agent communication protocols, message formats, or orchestration APIs. It addresses the trust governance layer: what authority exists, how it was granted, how it is evaluated, and what effects it may produce.

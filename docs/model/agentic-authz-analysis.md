---
owner: maintainers
last_reviewed: 2026-03-14
applicable_version: v0.9.0
tier: 1
---

# Agentic AI and Dynamic Authorization: A Structural Analysis

## 1. Purpose

There is an emerging consensus in the agentic AI governance space that dynamic
authorization is *the* pattern for governing what agents are allowed to do.

This document examines that claim carefully using the TSMM vocabulary developed
across the core model, the agentic AI extension, the multi-agent coordination
pattern, and the dynamic authorization framing document.

The conclusion is precise: dynamic authorization is *a* pattern within agentic
systems — a necessary one — but it is not the complete governance architecture.
The governance envelope that makes a dynamic authorization decision trustworthy
rather than merely technically correct requires four additional elements that
dynamic authorization frameworks do not model.

Read `docs/model/dynamic-authorization-framing.md` before this document for
TSMM's base position on dynamic authorization. Read
`docs/extensions/agentic-ai-extension.md` for the agentic extension abstractions
referenced throughout.

---

## 2. Where the consensus is correct

The emerging consensus is not wrong. It identifies something real.

An agentic system makes many fine-grained, runtime decisions: which tool to call,
which resource to access, whether an action falls within scope, whether to proceed
or escalate. That decision structure maps directly onto the dynamic authorization
pattern. A Policy Enforcement Point intercepts an agent's intended action. A
Policy Decision Point evaluates the request against the agent's attributes, the
resource's attributes, the environment state, and the applicable policy. A
decision is produced. The action is permitted or blocked.

The agentic extension's evaluation flow confirms this mapping explicitly:

```text
Agent requests an action against a resource
  -> Policy evaluates delegation, capability, execution context, and risk tier
    -> Trust Decision produced
      -> Effect permitted, denied, downgraded, or routed
```

That is a PAP/PDP/PEP sequence. The `Execution Context` abstraction — capturing
session state, user presence, approval state, risk tier, and environment — is
recognizably the attribute bundle that makes a PDP evaluation dynamic rather than
static. Runtime context drives the decision. The policy is externalized. The
enforcement is separated from the evaluation.

So: yes, dynamic authorization is present and structurally correct in agentic
systems. The consensus identifies the right pattern for the right layer.

The problem is assuming that layer is the whole picture.

---

## 3. What dynamic authorization does not model

Examined against the full TSMM agentic architecture, four governance elements
are present in agentic systems that dynamic authorization frameworks do not
capture. Each is discussed in turn.

### 3.1 Delegation is not an authorization request

Dynamic authorization governs the moment of access: a subject requests an action
on a resource, and a PDP decides whether to permit it. But in agentic systems,
the governance problem starts earlier — at the moment a principal grants a
delegation to an agent.

That grant is not a PDP evaluation. It is a governed act with its own structure:

- a delegator with bounded authority to grant
- a delegate with a defined scope of what they may do
- obligations the delegate must fulfill
- revocation conditions that can terminate the grant
- sub-delegation rules that determine whether the authority can propagate further

The agentic extension's `Delegation` object models all of this explicitly. The
multi-agent coordination schema adds `chainDepth`, `subDelegationPermitted`, and
`parentDelegationRef` to make chained delegation auditable and revocation
tractable.

None of this appears in dynamic authorization's model. A dynamic authz framework
can evaluate whether an agent's current attributes satisfy a policy at the moment
of a request. It cannot govern whether the authority that produced those
attributes was legitimately granted, correctly scoped, or still valid.

An agentic system built on dynamic authorization alone has access control. It
does not have delegation governance.

### 3.2 Oversight mode has no dynamic authz equivalent

The agentic extension's `Oversight Mode` — autonomous, pre-approved,
approval-gated, sampled-for-review, manual, emergency-override — governs the
conditions under which a PDP evaluation may occur and what happens to its result.

This is a governance layer that wraps the authorization decision, not a component
of it.

Consider two examples from the multi-agent coordination schema:

The `LookupAgent` in the procurement example operates with `localOversightMode:
autonomous`. Left to its own delegation, a dynamic authz PDP would evaluate its
request, produce a permit, and the action would proceed. But the
`effectiveOversightMode` is `sampled-review` — inherited from the parent
delegation — which means the action proceeds but is subject to retrospective
audit. The dynamic authz decision produced `permit`. The governance architecture
requires something more: the action must be recorded in a way that supports later
review.

The `SummaryAgent` operates under `approvalState: required` in its execution
context. A dynamic authz PDP might produce `permit` based on the agent's
attributes. But the oversight mode means a human must confirm before the effect
is produced, regardless of what the PDP decided.

In both cases, oversight mode changes the governance meaning of a `permit`
decision. Dynamic authorization has no concept that plays this role. Its model
produces a decision and the PEP enforces it. Whether a human should be in the
loop, at what point, and under what conditions, is entirely outside the
PDP/PEP architecture.

In agentic governance — particularly in rights-affecting automation — oversight
mode is not a secondary concern. It is the primary mechanism for keeping humans
in a position to catch failures before they compound.

### 3.3 Trace records are evidence, not logs

Dynamic authorization systems produce access logs. Those logs can be stored and
audited. But the agentic extension's `Trace Record` is a TSMM `Evidence` object.

That elevation is not cosmetic. It has structural consequences:

A log records what happened. A TSMM `Evidence` object can be referenced by
`Assessment` and `Verification` activities. It can support a `Claim`. It can
trigger a `Lifecycle Event` — a suspension, a remediation, a re-evaluation of
the agent's delegation scope. It can be part of an `Assessment` that informs
whether a future trust decision should produce the same outcome or a different
one.

In the multi-agent coordination example, the `coordinationTraceRecord`
aggregates `agentTraceRefs` from every agent in the chain and carries a
`compositeEffectRef`. That record is not an audit log of what the PEP did. It is
structured evidence of what the entire governance chain produced — evidence that
can be consumed by an assurance framework, evaluated against requirements, and
used to inform whether the delegation should remain active.

Dynamic authorization frameworks produce no equivalent. Their logs are archives.
TSMM trace records are governance inputs.

### 3.4 Risk tier drives policy selection, not just evaluation

Dynamic authorization evaluates a request against a policy. The policy is
selected by the PAP based on the applicable context. In practice, the question of
*which* policy applies is often handled by policy matching rules within the PDP —
target conditions in XACML, rule ordering in OPA, Cedar's policy set selection.

The agentic extension handles this differently. `Risk Tier` is a first-class
attribute that governs which profile and policy apply to an agent's actions before
any evaluation occurs. A `moderate` risk tier agent operating on a `confidential`
resource in a `high` risk execution context does not simply land on a stricter
policy through PDP attribute matching. The risk tier triggers profile selection
at the governance layer — determining what the PDP is even permitted to evaluate
and what outcomes it may produce.

This distinction matters for agentic systems because agents are not static
subjects with fixed attributes. An agent's effective risk tier can change as it
accumulates actions, tools, and context across a session. An agent that began a
workflow at `low` risk tier may drift toward `high` by the time it attempts a
rights-affecting action. Dynamic authorization's attribute model captures the
instantaneous state. Risk tier-driven profile selection in TSMM captures the
governance response to that drift.

The agentic extension design principle states this directly: "A low-risk
informational agent should not silently drift into rights-affecting action simply
because it can call another tool." Dynamic authorization frameworks cannot
enforce that principle without a risk tier concept that governs policy selection
before the PDP fires.

---

## 4. The structural relationship

The four elements above form a governance envelope that surrounds the dynamic
authorization evaluation moment in an agentic system:

```text
Governance envelope
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  Delegation governance                                          │
│  (scope, obligations, sub-delegation rules, revocation)        │
│                                                                 │
│  Risk tier → profile selection → policy scope                  │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                         │   │
│  │   Dynamic authorization evaluation moment              │   │
│  │   PEP → PDP → permit/deny/indeterminate/notApplicable  │   │
│  │                                                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Oversight mode                                                 │
│  (autonomous / pre-approved / approval-gated /                 │
│   sampled-review / manual / emergency-override)                │
│                                                                 │
│  Trace record as structured evidence                           │
│  (substantiates claims, supports assessment,                   │
│   feeds lifecycle events, informs future decisions)            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Dynamic authorization is necessary. The governance envelope makes it
trustworthy.

A system that implements dynamic authorization without the governance envelope
can produce technically correct access control decisions. It cannot answer
questions that matter for agentic governance:

- Was the agent's authority legitimately granted and correctly scoped?
- Did the action occur under the correct oversight mode?
- Is there structured evidence that can be evaluated, not merely a log that
  can be searched?
- Did the agent's risk tier drift in ways that should have changed which policy
  applied?

---

## 5. Why the consensus understates the case

The framing of dynamic authorization as *the* agentic AI pattern understates
what agentic governance requires in a specific way: it conflates the
authorization evaluation layer with the full governance architecture.

This is an understandable error. Dynamic authorization frameworks are mature,
well-specified, and well-tooled. XACML, OPA, and Cedar give implementers
working infrastructure for the evaluation moment. The governance envelope
elements — delegation governance, oversight mode, risk-tier-driven profile
selection, trace-as-evidence — require more design work and are less
immediately tooled.

The risk is that implementers adopt dynamic authorization as their agentic
governance architecture and discover later that they have authorization
infrastructure but not governance: agents whose authority was never bounded by
a delegation model, whose actions were never subject to oversight mode
constraints, whose execution traces cannot substantiate an assessment, and whose
risk drift was never caught by policy selection logic.

That is the zombie credential problem applied to agents: a system that produces
live effects under authority that should have been constrained, reviewed, or
revoked, but was not, because the governance envelope was not built.

---

## 6. Implications for TSMM

This analysis has two practical implications for the model.

**6.1 The dynamic authorization framing document should be updated**

`docs/model/dynamic-authorization-framing.md` currently positions dynamic
authorization as a runtime evaluation pattern that operates within the TSMM
trust decision chain. That position remains correct and stable.

This document adds specificity: in the agentic AI domain in particular, the
governance envelope is where the non-trivial design work lives. A future revision
of the framing document should reference this analysis and make the agentic
context explicit.

**6.2 The experimental status of the dynamic authz pattern may warrant revision**

The crosswalk and pattern carry `status: experimental` because core promotion
is deferred pending implementation experience. This document constitutes one
form of that experience: a structural analysis showing that dynamic authorization
composes with TSMM's agentic extension correctly, that the two do not
contradict, and that the governance envelope abstractions in the agentic
extension are the necessary complement to the dynamic authz evaluation moment.

That is a meaningful data point for the promotion rule. It does not by itself
satisfy the rule — cross-domain implementation evidence beyond the analysis layer
is still required — but it advances the case.

---

## 7. Guidance for agentic system builders

If you are building an agentic system and want to apply both the dynamic
authorization pattern and the TSMM agentic governance model:

**Start with the governance envelope, not the PDP.**

Before designing your authorization policy, define:

1. The delegation model — what authority the agent holds, who granted it, what
   scope it covers, what obligations it carries, and under what conditions it
   can be revoked or propagated.
2. The oversight mode — for each class of action the agent may take, determine
   the oversight mode that applies. Default to the most restrictive mode
   consistent with the workflow's operational requirements.
3. The risk tier — classify each action type and resource type by risk tier.
   Bind policy selection to risk tier before the PDP fires.
4. The trace model — define what a trace record must contain to function as
   TSMM `Evidence`, not merely as a log.

Once those four elements are in place, the PDP/PEP evaluation layer operates
within a governance architecture rather than in front of one.

For the authorization evaluation itself, use `docs/patterns/dynamic-authz-pattern.md`
and `docs/crosswalks/xacml-abac-crosswalk.md`.

For the delegation model, use `docs/extensions/agentic-ai-extension.md` and
`docs/patterns/multi-agent-coordination-pattern.md`.

For the conformance checklist items that cover both layers, see
`docs/conformance/tsmm-conformance-checklist.md` — the Agentic AI Extension
checklist and the Dynamic Authorization Pattern checklist together describe what
a complete agentic governance implementation should satisfy.

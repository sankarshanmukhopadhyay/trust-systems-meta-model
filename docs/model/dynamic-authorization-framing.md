---
owner: maintainers
last_reviewed: 2026-03-11
applicable_version: v0.8.0
tier: 1
---

# Dynamic Authorization: Framing and Position

## 1. Purpose

This document establishes TSMM's position on dynamic authorization before the crosswalk and pattern documents are read.

It is not a tutorial on dynamic authorization. It is a framing document that explains why the concept is adjacent to TSMM, where the two framings are compatible, where they diverge, and what an implementer should and should not conclude from the materials that follow.

Read this document before reading `docs/crosswalks/xacml-abac-crosswalk.md` or `docs/patterns/dynamic-authz-pattern.md`.

## 2. What dynamic authorization is

Dynamic authorization is a family of approaches to access control in which authorization decisions are made at runtime, in response to a specific request, by evaluating rich contextual attributes against a policy that is maintained separately from the application enforcing it.

The canonical runtime question is:

> Given this subject, this action, this resource, and this environment state — should the request be permitted or denied?

The canonical architecture separates four concerns:

- **Policy Administration Point (PAP)** — where policies are authored, versioned, and managed
- **Policy Decision Point (PDP)** — where policy is evaluated against a specific request and a decision is produced
- **Policy Enforcement Point (PEP)** — where the decision is enforced, either permitting or blocking the requested effect
- **Policy Information Point (PIP)** — where contextual attribute data is retrieved to support PDP evaluation

This architecture is codified in XACML 3.0, implemented in systems like OPA, Cedar, and Axiomatics, and described in depth in the ABAC and NGAC literature. The Manning book *Dynamic Authorization* surveys this landscape comprehensively.

The central value of the approach is that policy is externalized from application logic, decisions are context-sensitive at the level of individual requests, and the authorization infrastructure can be audited, updated, and reasoned about independently of the systems it governs.

## 3. What TSMM asks

TSMM's governing question is:

> Under what bounded authority, policy, evidence, assessment, and verification conditions should a system allow a trust-relevant effect to occur?

This is a different question. It is not narrower or broader — it has a different center of gravity.

TSMM centers the **governance conditions** that legitimize an effect: the chain of authority that authorizes a role, the evidence that substantiates a claim, the assessment that evaluates a profile, the lifecycle state that determines whether an artifact is still valid. The trust decision emerges from that full chain.

Dynamic authorization centers the **runtime evaluation moment**: a request arrives, attributes are gathered, policy is evaluated, a decision is produced, an effect is permitted or denied. The governance conditions that produced the policy are largely out of scope for the PDP.

Both questions matter. They operate at different layers of a trust architecture. Conflating them produces systems that are technically well-authorized but insufficiently governed, or systems that are well-governed on paper but cannot make fine-grained runtime decisions efficiently.

## 4. Where the framings are compatible

The PDP/PEP/PAP architecture maps onto TSMM abstractions without contradiction:

| Dynamic authz concept | TSMM mapping |
|---|---|
| Policy Administration Point | Where TSMM `Policy` and `Profile` objects are defined and versioned |
| Policy Decision Point | The evaluation step within TSMM `Trust Decision` production |
| Policy Enforcement Point | The system component that acts on a `Trust Decision` to permit or block an `Effect` |
| Policy Information Point | The retrieval of `Evidence`, `Artifact` state, and `Lifecycle Event` data to inform evaluation |
| Authorization request | An implicit input to TSMM policy evaluation: the acting entity, role, authority scope, and requested effect |
| Authorization decision | The TSMM `Trust Decision` outcome |
| Obligation | A condition attached to an `Effect` that must be fulfilled after a permit decision |

This means that a TSMM-aligned system that implements dynamic authorization is not doing something outside the model. The PDP is a specialization of how `Policy` evaluates inputs to produce a `Trust Decision`. The PEP is how the system acts on that decision to produce or block an `Effect`.

## 5. Where the framings diverge

The divergence is not logical contradiction. It is frame drift — the risk that adopting the dynamic authorization vocabulary causes the model's center of gravity to shift in ways that undermine the governance architecture TSMM is designed to support.

Three specific risks:

**5.1 Policy reduced to a decision engine**

Dynamic authorization's primary framing treats policy as an evaluation function: inputs in, permit or deny out. The richer TSMM concept of policy — shaped by governance context, expressed through profiles, connected to requirements, controls, and threat models — can fade into background infrastructure when the PDP framing dominates. A policy that produces correct permit/deny decisions but is disconnected from its governance context is not a well-governed policy; it is an accurate but unaccountable one.

**5.2 Effect reduced to a permit/deny flag**

TSMM's `Effect` carries class, action, status, and optional subject and resource bindings. It is meant to represent the real operational consequence of a trust decision — allow informational use but block rights-affecting action, route to human review, downgrade a credential rather than reject it outright. Dynamic authorization's effect model collapses to permit/deny/indeterminate/notApplicable. That is sufficient for fine-grained access control but loses the governance expressiveness TSMM requires.

**5.3 Context narrowed to attributes**

Dynamic authorization treats context as a set of attributes available to the PDP at evaluation time. TSMM's context is broader: governance context shapes policy interpretation, lifecycle state can invalidate an otherwise valid authorization, evidence quality affects what decision the policy may produce. Attribute-based context is a subset of TSMM's context model, not a replacement for it.

## 6. TSMM's position

Dynamic authorization is a runtime evaluation pattern that can operate **within** the TSMM trust decision chain. It is not a replacement framing for the chain itself.

Specifically:

- The PAP/PDP/PEP separation is a useful architectural pattern for implementing the Policy → Trust Decision → Effect flow. It does not replace that flow.
- Fine-grained subject-action-resource-environment request evaluation is a valid specialization of TSMM policy evaluation. It does not displace the governance conditions that shape what policies may do.
- Obligations and advice in dynamic authorization map onto the conditions and obligations already expressible in TSMM Authority and Effect objects.

The crosswalk and pattern documents that accompany this framing carry `status: experimental`. That status does not mean the materials are incomplete or unreliable. It means that the promotion of dynamic authorization concepts into the TSMM core is deliberately deferred until implementation experience demonstrates that they are cross-domain, structurally necessary, and stable — per the promotion rule in `docs/extensions/index.md`.

The framing document itself is not experimental. The position it states is stable: dynamic authorization belongs in TSMM's orbit, positioned as a runtime evaluation specialization within the governance architecture the core model defines.

## 7. Guidance for implementers

If you are building a system that uses OPA, Cedar, XACML, or a similar policy engine and want to align it with TSMM:

- Map your PAP to TSMM `Policy` and `Profile` administration
- Map your PDP evaluation to the TSMM `Trust Decision` production step
- Map your PEP to the system that acts on an `Effect`
- Do not reduce `Policy` to a decision function — keep the governance context, profile, and requirement bindings
- Do not reduce `Effect` to a permit flag — preserve the class, action, and status distinctions
- Read `docs/patterns/dynamic-authz-pattern.md` for the TSMM-aligned sequence
- Read `docs/crosswalks/xacml-abac-crosswalk.md` for concept-by-concept mappings

If you find that TSMM's current abstractions are insufficient for your dynamic authz use case, document the gap precisely. That is the kind of implementation experience that will inform whether and how the promotion rule should be applied.

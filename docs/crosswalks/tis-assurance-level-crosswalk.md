---
owner: maintainers
last_reviewed: 2026-05-05
applicable_version: 0.23.0
tier: 1
---

# TIS Assurance Level Crosswalk

TSMM profile labels and TIS assurance levels solve different problems. This crosswalk prevents accidental conflation.

| TSMM posture | Meaning | TIS assurance interpretation |
| --- | --- | --- |
| minimal | Smallest useful model surface for comparison or onboarding. | Usually AL1 candidate. |
| operational | Model includes enough lifecycle, evidence, and authority structure for implementation use. | Usually AL2 candidate. |
| assured | Model is suitable for assurance review and evidence production. | Usually AL3 candidate. |
| agentic | The system involves agentic actors or delegated runtime effects. | Not an assurance level. Select AL based on effect risk. |

## Normative rule

When claiming assurance rigor, use TIS `AL1`, `AL2`, `AL3`, or `AL4`. When describing the character of the TSMM model, use TSMM profile language.

## Agentic systems

Agentic does not mean AL4. A low-risk agentic workflow may be AL2. A high-impact autonomous delegation workflow may require AL3 or AL4 controls. The assurance level must be justified by authority scope, revocation sensitivity, user impact, evidence requirements, and operational effect.

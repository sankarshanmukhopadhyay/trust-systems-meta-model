#!/usr/bin/env python3
"""check_schema_coverage.py

Validates that every property defined in a TSMM schema (top-level and $defs)
has at least one corresponding field exercised in its paired example instance.

This catches gaps between what the schema models and what the examples actually
demonstrate, before they become confusion for implementers.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXAMPLES = ROOT / "examples"

# Maps each example to the schema it exercises.
# Extend this list when new examples or schemas are added.
COVERAGE_PAIRS: list[tuple[str, str]] = [
    ("tsmm-meta-model-instance.json", "tsmm.schema.json"),
    ("minimal-trust-registry-instance.json", "tsmm-core.schema.json"),
    ("consumer-policy-instance.json", "tsmm-core.schema.json"),
    ("delegated-agent-instance.json", "tsmm-core.schema.json"),
    ("agentic-ai-extension-instance.json", "tsmm-agentic-extension.schema.json"),
    ("verifiable-trust-community-instance.json", "tsmm-vtc-extension.schema.json"),
    ("assurance-extension-instance.json", "tsmm-assurance-extension.schema.json"),
    ("multi-agent-coordination-instance.json", "tsmm-multi-agent-extension.schema.json"),
    ("evidence-artifact-instance.json", "tsmm-evidence-artifact-extension.schema.json"),
    ("agent-interaction-extension-instance.json", "tsmm-agent-interaction-extension.schema.json"),
    ("agent-interaction-a2a-binding-instance.json", "tsmm-agent-interaction-extension.schema.json"),
]

# Properties that are intentionally optional and acceptable to omit from examples.
# Add property names here only with a documented reason.
ACCEPTABLE_OMISSIONS: set[str] = {
    # Meta-model notes are explanatory only.
    "notes",
    # Lifecycle fields are only relevant in live operational instances, not worked examples.
    "lifecycleEvents",
    # Level frameworks are defined in standalone examples only.
    "levelFrameworks",
    # Notes fields are free-text and do not require demonstration.
    "notes",
    # relatedAction is only populated in agentic execution contexts. The evidence artifact
    # base example demonstrates a trust registry context where no Action is in scope.
    "relatedAction",
    # Agent interaction extension: providerRef is optional (may not be known at disclosure time).
    "providerRef",
    # Agent interaction extension: authenticityBinding is optional for public descriptors.
    "authenticityBinding",
    # Agent interaction extension: expiresAt is optional across several abstractions.
    "expiresAt",
    # Agent interaction extension: policyConditions are optional on SkillContracts.
    "policyConditions",
    # Agent interaction extension: tags and examples are optional discovery aids on SkillContracts.
    "tags",
    "examples",
    # Agent interaction extension: conditionsForWithdrawal is optional on PeerTrustRelations.
    "conditionsForWithdrawal",
    # Agent interaction extension: governingPolicyRef is optional on PeerTrustRelations.
    "governingPolicyRef",
    # Agent interaction extension: inheritedAuthorityRefs and inheritedEvidenceRefs are optional
    # for sessions where no prior authority has been established.
    "inheritedAuthorityRefs",
    "inheritedEvidenceRefs",
    # Agent interaction extension: reAuthorizationPolicy is optional where no inherited authority exists.
    "reAuthorizationPolicy",
    # Agent interaction extension: terminationReason only present after session close.
    "terminationReason",
    # Agent interaction extension: taskRef is optional on AuthorizationCheckpoints.
    "taskRef",
    # Agent interaction extension: requiredEvidenceRefs is optional where evidence is not pre-identified.
    "requiredEvidenceRefs",
    # Agent interaction extension: resolvedAt only present after resolution.
    "resolvedAt",
    # Agent interaction extension: mitigations are optional on OpacityBoundaries.
    "mitigations",
    # Agent interaction extension: resolutionRecord is optional on ExtensionContracts.
    "resolutionRecord",
    # Agent interaction extension v0.14.0: assigneeRef is optional on InteractionTasks.
    "assigneeRef",
    # Agent interaction extension v0.14.0: authorizationCheckpointRef only present when task is paused.
    "authorizationCheckpointRef",
    # Agent interaction extension v0.14.0: artifactRefs may be empty for tasks in progress.
    "artifactRefs",
    # Agent interaction extension v0.14.0: cancellationReason only present for cancelled tasks.
    "cancellationReason",
    # Agent interaction extension v0.14.0: historyRef is optional.
    "historyRef",
    # Agent interaction extension v0.14.0: redactionRules are optional on ContentProvenancePolicies.
    "redactionRules",
    # Agent interaction extension v0.14.0: requiredCompensatingControls optional on ObservabilityModes.
    "requiredCompensatingControls",
    # Agent interaction extension v0.14.0 abstractions are not present in the v0.13.0 base
    # example (agent-interaction-extension-instance.json), which was written before these
    # abstractions were added to the schema. All three are fully exercised in the binding
    # example (agent-interaction-a2a-binding-instance.json).
    "interactionTasks",
    "contentProvenancePolicies",
    "observabilityModes",
    # contextRef is a required field on interactionTask; absent from v0.13.0 example for same reason.
    "contextRef",
    # contentProvenancePolicy required fields absent from v0.13.0 example.
    "provenanceRequirements",
    "sanitizationRequired",
    "evidenceCaptureObligation",
    "applicableModalities",
    # observabilityMode required fields absent from v0.13.0 example.
    "deliveryModel",
    "auditabilityLevel",
    "replayRisk",
    "userAwarenessModel",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def collect_schema_properties(schema: dict) -> dict[str, set[str]]:
    """
    Returns a mapping of object name -> set of property names defined in the schema.
    Covers top-level properties and all $defs entries.
    """
    result: dict[str, set[str]] = {}

    top_props = schema.get("properties", {})
    if top_props:
        result["<root>"] = set(top_props.keys())

    for def_name, def_body in schema.get("$defs", {}).items():
        props = def_body.get("properties", {})
        if props:
            result[def_name] = set(props.keys())

    return result


def collect_instance_keys(obj: Any, found: set[str] | None = None) -> set[str]:
    """
    Recursively collects all keys present anywhere in a JSON object.
    """
    if found is None:
        found = set()
    if isinstance(obj, dict):
        for k, v in obj.items():
            found.add(k)
            collect_instance_keys(v, found)
    elif isinstance(obj, list):
        for item in obj:
            collect_instance_keys(item, found)
    return found


def check_coverage(example_name: str, schema_name: str) -> list[str]:
    schema_path = SCHEMAS / schema_name
    example_path = EXAMPLES / example_name

    schema = load_json(schema_path)
    instance = load_json(example_path)

    schema_props = collect_schema_properties(schema)
    instance_keys = collect_instance_keys(instance)

    gaps: list[str] = []
    for object_name, properties in schema_props.items():
        for prop in properties:
            if prop not in instance_keys and prop not in ACCEPTABLE_OMISSIONS:
                gaps.append(
                    f"  [{schema_name} / {object_name}] property '{prop}' is defined "
                    f"in schema but not exercised in {example_name}"
                )
    return gaps


def main() -> None:
    all_gaps: list[str] = []

    for example_name, schema_name in COVERAGE_PAIRS:
        example_path = EXAMPLES / example_name
        schema_path = SCHEMAS / schema_name

        if not example_path.exists():
            print(f"SKIP (example not found): {example_name}")
            continue
        if not schema_path.exists():
            print(f"SKIP (schema not found): {schema_name}")
            continue

        gaps = check_coverage(example_name, schema_name)
        if gaps:
            print(f"GAPS: {example_name} does not exercise all schema properties:")
            for gap in gaps:
                print(gap)
            all_gaps.extend(gaps)
        else:
            print(f"OK: {example_name} exercises all tracked schema properties")

    if all_gaps:
        print(
            f"\n{len(all_gaps)} coverage gap(s) found. "
            "Add missing properties to examples or add justified omissions to ACCEPTABLE_OMISSIONS."
        )
        raise SystemExit(1)

    print("\nAll schema/example coverage checks passed.")


if __name__ == "__main__":
    main()

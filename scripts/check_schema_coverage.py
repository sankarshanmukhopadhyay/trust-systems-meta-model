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
    ("minimal-trust-registry-instance.json", "tsmm-core.schema.json"),
    ("consumer-policy-instance.json", "tsmm-core.schema.json"),
    ("delegated-agent-instance.json", "tsmm-core.schema.json"),
    ("agentic-ai-extension-instance.json", "tsmm-agentic-extension.schema.json"),
    ("verifiable-trust-community-instance.json", "tsmm-vtc-extension.schema.json"),
    ("assurance-extension-instance.json", "tsmm-assurance-extension.schema.json"),
    ("multi-agent-coordination-instance.json", "tsmm-multi-agent-extension.schema.json"),
    ("evidence-artifact-instance.json", "tsmm-evidence-artifact-extension.schema.json"),
]

# Properties that are intentionally optional and acceptable to omit from examples.
# Add property names here only with a documented reason.
ACCEPTABLE_OMISSIONS: set[str] = {
    # Lifecycle fields are only relevant in live operational instances, not worked examples.
    "lifecycleEvents",
    # Level frameworks are defined in standalone examples only.
    "levelFrameworks",
    # Notes fields are free-text and do not require demonstration.
    "notes",
    # relatedAction is only populated in agentic execution contexts. The evidence artifact
    # base example demonstrates a trust registry context where no Action is in scope.
    "relatedAction",
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

#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "tsmm-graph.schema.json"
DEFAULT_TARGETS = [
    ROOT / "examples" / "tsmm-ecosystem-example.json",
    ROOT / "examples" / "profiles" / "ssi-ecosystem.json",
    ROOT / "examples" / "profiles" / "agent-trust-network.json",
    ROOT / "examples" / "profiles" / "trust-registry-federation.json",
    ROOT / "examples" / "profiles" / "dpi-trust-layer.json",
]

ALLOWED_RELATIONS: dict[str, set[tuple[str, str]]] = {
    "governs": {("GovernanceAuthority", "TrustDomain")},
    "defines": {
        ("GovernanceAuthority", "Policy"),
        ("GovernanceAuthority", "AssuranceProfile"),
    },
    "operates": {
        ("GovernanceAuthority", "TrustRegistry"),
        ("TrustRegistry", "RegistryService"),
    },
    "registers": {
        ("TrustRegistry", "Issuer"),
        ("TrustRegistry", "Verifier"),
        ("TrustRegistry", "Agent"),
        ("TrustRegistry", "TrustRegistry"),
    },
    "authorizes": {
        ("GovernanceAuthority", "Issuer"),
        ("GovernanceAuthority", "Verifier"),
        ("GovernanceAuthority", "Agent"),
        ("Policy", "Agent"),
    },
    "issues": {("Issuer", "Credential")},
    "verifies": {
        ("Verifier", "Credential"),
        ("Verifier", "Issuer"),
        ("Verifier", "Agent"),
    },
    "asserts": {("Credential", "Subject")},
    "delegates": {
        ("Agent", "Agent"),
        ("Issuer", "Agent"),
    },
    "constrains": {
        ("Policy", "Issuer"),
        ("Policy", "Verifier"),
        ("Policy", "Agent"),
        ("Policy", "TrustRegistry"),
    },
    "substantiates": {
        ("EvidenceBundle", "Issuer"),
        ("EvidenceBundle", "Verifier"),
        ("EvidenceBundle", "Agent"),
        ("EvidenceBundle", "TrustRegistry"),
        ("EvidenceBundle", "Assessment"),
    },
    "assesses": {
        ("Assessment", "AssuranceProfile"),
        ("Assessment", "Issuer"),
        ("Assessment", "Verifier"),
        ("Assessment", "TrustRegistry"),
        ("Assessment", "Agent"),
    },
    "informs": {
        ("Assessment", "TrustDecision"),
        ("EvidenceBundle", "TrustDecision"),
        ("AssuranceProfile", "TrustDecision"),
        ("Policy", "TrustDecision"),
    },
    "produces": {("TrustDecision", "Effect")},
    "reliesOn": {("RelyingParty", "TrustDecision")},
    "anchors": {
        ("TrustRegistry", "Credential"),
        ("TrustRegistry", "Issuer"),
    },
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def build_registry() -> Registry:
    schema = load_json(SCHEMA_PATH)
    registry = Registry()
    registry = registry.with_resource(schema["$id"], Resource.from_contents(schema))
    registry = registry.with_resource(SCHEMA_PATH.resolve().as_uri(), Resource.from_contents(schema))
    return registry


def validate_graph(path: Path) -> None:
    schema = load_json(SCHEMA_PATH)
    instance = load_json(path)
    validator = Draft202012Validator(schema, registry=build_registry())
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        print(f"FAILED schema validation: {path.relative_to(ROOT)}")
        for error in errors:
            loc = ".".join(str(p) for p in error.path) or "<root>"
            print(f"  - {loc}: {error.message}")
        raise SystemExit(1)

    nodes = instance["nodes"]
    edges = instance["edges"]
    node_map = {node["id"]: node for node in nodes}
    if len(node_map) != len(nodes):
        raise SystemExit(f"FAILED semantic validation: {path.relative_to(ROOT)} has duplicate node ids")

    edge_ids: set[str] = set()
    for edge in edges:
        if edge["id"] in edge_ids:
            raise SystemExit(f"FAILED semantic validation: {path.relative_to(ROOT)} has duplicate edge id {edge['id']}")
        edge_ids.add(edge["id"])
        if edge["from"] not in node_map or edge["to"] not in node_map:
            raise SystemExit(
                f"FAILED semantic validation: {path.relative_to(ROOT)} edge {edge['id']} references missing node"
            )
        pair = (node_map[edge["from"]]["type"], node_map[edge["to"]]["type"])
        allowed_pairs = ALLOWED_RELATIONS[edge["type"]]
        if pair not in allowed_pairs:
            raise SystemExit(
                f"FAILED semantic validation: {path.relative_to(ROOT)} edge {edge['id']} uses relation {edge['type']} "
                f"for disallowed pair {pair[0]} -> {pair[1]}"
            )
        for ref in edge.get("evidenceRefs", []):
            if ref not in node_map:
                raise SystemExit(
                    f"FAILED semantic validation: {path.relative_to(ROOT)} edge {edge['id']} references unknown evidenceRef {ref}"
                )
            if node_map[ref]["type"] != "EvidenceBundle":
                raise SystemExit(
                    f"FAILED semantic validation: {path.relative_to(ROOT)} edge {edge['id']} evidenceRef {ref} is not an EvidenceBundle"
                )

    print(f"OK: {path.relative_to(ROOT)}")


def main(argv: list[str]) -> None:
    targets = [Path(arg).resolve() for arg in argv] if argv else DEFAULT_TARGETS
    for target in targets:
        validate_graph(target)
    print("All TSMM graph validations passed.")


if __name__ == "__main__":
    main(sys.argv[1:])

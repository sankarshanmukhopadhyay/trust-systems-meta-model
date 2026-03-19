#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def load_graph(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def node_label(node: dict, annotate_profiles: bool) -> str:
    label = node.get("label", node["id"])
    profile = node.get("profile")
    if annotate_profiles and profile:
        return f"{label}\n[{profile}]"
    return label


def render_mermaid(graph: dict, cluster: bool = False, annotate_profiles: bool = False) -> str:
    lines = ["graph TD"]
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])

    if cluster:
        grouped: dict[str, list[dict]] = defaultdict(list)
        for node in nodes:
            grouped[node.get("profile") or node.get("trustDomain") or "unclassified"].append(node)
        for idx, (group, group_nodes) in enumerate(grouped.items(), start=1):
            safe = f"cluster_{idx}"
            lines.append(f"  subgraph {safe}[{group}]")
            for node in group_nodes:
                lines.append(f'    {node["id"]}["{node_label(node, annotate_profiles)}"]')
            lines.append("  end")
    else:
        for node in nodes:
            lines.append(f'  {node["id"]}["{node_label(node, annotate_profiles)}"]')

    for edge in edges:
        label = edge.get("type", "rel")
        lines.append(f'  {edge["from"]} -- "{label}" --> {edge["to"]}')
    return "\n".join(lines)


def render_dot(graph: dict, cluster: bool = False, annotate_profiles: bool = False) -> str:
    lines = ["digraph TSMM {"]
    nodes = graph.get("nodes", [])
    edges = graph.get("edges", [])

    if cluster:
        grouped: dict[str, list[dict]] = defaultdict(list)
        for node in nodes:
            grouped[node.get("profile") or node.get("trustDomain") or "unclassified"].append(node)
        for idx, (group, group_nodes) in enumerate(grouped.items()):
            lines.append(f'  subgraph cluster_{idx} {{')
            lines.append(f'    label="{group}";')
            for node in group_nodes:
                lines.append(f'    "{node["id"]}" [label="{node_label(node, annotate_profiles)}"];')
            lines.append("  }")
    else:
        for node in nodes:
            lines.append(f'  "{node["id"]}" [label="{node_label(node, annotate_profiles)}"];')

    for edge in edges:
        label = edge.get("type", "rel")
        lines.append(f'  "{edge["from"]}" -> "{edge["to"]}" [label="{label}"];')
    lines.append("}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a TSMM graph instance as Mermaid or Graphviz DOT.")
    parser.add_argument("input", help="Path to a TSMM graph JSON file")
    parser.add_argument("--format", choices=["mermaid", "dot"], default="mermaid")
    parser.add_argument("--cluster", action="store_true", help="Group nodes by profile or trust domain in the output.")
    parser.add_argument("--annotate-profiles", action="store_true", help="Append profile metadata to node labels where present.")
    args = parser.parse_args()

    graph = load_graph(Path(args.input))
    if args.format == "mermaid":
        print(render_mermaid(graph, cluster=args.cluster, annotate_profiles=args.annotate_profiles))
    else:
        print(render_dot(graph, cluster=args.cluster, annotate_profiles=args.annotate_profiles))


if __name__ == "__main__":
    main()

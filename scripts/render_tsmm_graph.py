#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_graph(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def to_mermaid(graph: dict) -> str:
    node_map = {node["id"]: node for node in graph["nodes"]}
    lines = ["flowchart TD"]
    for node in graph["nodes"]:
        label = f"{node['label']}\\n[{node['type']}]".replace('"', "'")
        lines.append(f'    {node["id"]}["{label}"]')
    for edge in graph["edges"]:
        lines.append(f'    {edge["from"]} -- {edge["type"]} --> {edge["to"]}')
    return "\n".join(lines) + "\n"


def to_dot(graph: dict) -> str:
    lines = [f'digraph "{graph["graphId"]}" {{']
    lines.append("  rankdir=LR;")
    for node in graph["nodes"]:
        label = f'{node["label"]}\\n[{node["type"]}]'.replace('"', "'")
        lines.append(f'  "{node["id"]}" [label="{label}"];')
    for edge in graph["edges"]:
        lines.append(f'  "{edge["from"]}" -> "{edge["to"]}" [label="{edge["type"]}"];')
    lines.append("}")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Render a TSMM graph as Mermaid or DOT.")
    parser.add_argument("input", help="Path to TSMM graph JSON")
    parser.add_argument("--format", choices=["mermaid", "dot"], default="mermaid")
    parser.add_argument("--output", help="Output path. Defaults to stdout.")
    args = parser.parse_args()

    graph = load_graph(Path(args.input).resolve())
    rendered = to_mermaid(graph) if args.format == "mermaid" else to_dot(graph)
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()

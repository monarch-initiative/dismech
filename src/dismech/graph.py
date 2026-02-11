"""
Build causal graphs from disorder data and generate Mermaid diagrams.

This module extracts nodes (named elements) and edges (downstream/sequelae relationships)
from disorder YAML data, performs referential integrity checks, and generates
Mermaid flowchart code for visualization.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class NodeInfo:
    """Information about a node in the causal graph."""

    name: str
    node_type: str  # pathophysiology, phenotype, environmental, genetic, treatment, biochemical
    description: str | None = None


@dataclass
class Edge:
    """An edge in the causal graph."""

    source: str
    target: str
    predicate: str  # causes, leads_to
    source_type: str


@dataclass
class CausalGraph:
    """A causal graph with nodes, edges, and integrity issues."""

    nodes: dict[str, NodeInfo] = field(default_factory=dict)
    edges: list[Edge] = field(default_factory=list)
    # targets with no matching node
    orphan_targets: set[str] = field(default_factory=set)
    integrity_issues: list[str] = field(default_factory=list)


# Node type to Mermaid fill color mapping
NODE_COLORS = {
    "pathophysiology": "#dbeafe",  # blue-100
    "phenotype": "#fef3c7",  # amber-100
    "environmental": "#dcfce7",  # green-100
    "genetic": "#f3e8ff",  # purple-100
    "treatment": "#fce7f3",  # pink-100
    "biochemical": "#e0e7ff",  # indigo-100
    "orphan": "#fee2e2",  # red-100 for unmatched targets
}


def _sanitize_node_id(name: str) -> str:
    """Convert a node name to a valid Mermaid node ID."""
    # Replace problematic characters with underscores
    sanitized = name.replace(" ", "_").replace(
        "-", "_").replace("(", "").replace(")", "")
    sanitized = sanitized.replace(",", "").replace("/", "_").replace("'", "")
    # Ensure it starts with a letter
    if sanitized and not sanitized[0].isalpha():
        sanitized = "N_" + sanitized
    return sanitized


def _escape_label(name: str) -> str:
    """Escape a node label for Mermaid."""
    # Escape quotes and other special characters in labels
    return name.replace('"', "'")


def build_causal_graph(disorder: dict[str, Any]) -> CausalGraph:
    """
    Build a causal graph from disorder data.

    Collects nodes from named elements in various sections and edges from
    downstream/sequelae relationships. Checks referential integrity.

    Args:
        disorder: Parsed disorder YAML data

    Returns:
        CausalGraph with nodes, edges, and any integrity issues
    """
    graph = CausalGraph()

    # Sections that contain named elements (potential nodes)
    node_sections = [
        ("pathophysiology", "pathophysiology"),
        ("phenotypes", "phenotype"),
        ("environmental", "environmental"),
        ("genetic", "genetic"),
        ("treatments", "treatment"),
        ("biochemical", "biochemical"),
    ]

    # Collect all nodes
    for section_key, node_type in node_sections:
        items = disorder.get(section_key, []) or []
        for item in items:
            if isinstance(item, dict) and "name" in item:
                name = item["name"]
                graph.nodes[name] = NodeInfo(
                    name=name,
                    node_type=node_type,
                    description=item.get("description"),
                )

    # Collect edges from pathophysiology downstream
    for item in disorder.get("pathophysiology", []) or []:
        if not isinstance(item, dict):
            continue
        source = item.get("name")
        if not source:
            continue

        downstream = item.get("downstream", []) or []
        for edge_item in downstream:
            if isinstance(edge_item, dict) and "target" in edge_item:
                target = edge_item["target"]
                graph.edges.append(
                    Edge(source=source, target=target, predicate="causes",
                         source_type="pathophysiology")
                )

    # Collect edges from phenotype sequelae
    for item in disorder.get("phenotypes", []) or []:
        if not isinstance(item, dict):
            continue
        source = item.get("name")
        if not source:
            continue

        sequelae = item.get("sequelae", []) or []
        for edge_item in sequelae:
            if isinstance(edge_item, dict) and "target" in edge_item:
                target = edge_item["target"]
                graph.edges.append(
                    Edge(source=source, target=target,
                         predicate="leads_to", source_type="phenotype")
                )

    # Check referential integrity
    for edge in graph.edges:
        if edge.target not in graph.nodes:
            graph.orphan_targets.add(edge.target)
            graph.integrity_issues.append(
                f"Target '{edge.target}' (from '{edge.source}') not found in named elements")

    return graph


def generate_mermaid(graph: CausalGraph) -> str:
    """
    Generate Mermaid flowchart code from a causal graph.

    Args:
        graph: CausalGraph with nodes and edges

    Returns:
        Mermaid diagram code as a string
    """
    if not graph.edges:
        return ""

    lines = ["graph LR"]

    # Track which nodes are actually used in edges
    used_nodes: set[str] = set()
    for edge in graph.edges:
        used_nodes.add(edge.source)
        used_nodes.add(edge.target)

    # Generate node definitions for used nodes
    node_ids: dict[str, str] = {}
    for name in used_nodes:
        node_id = _sanitize_node_id(name)
        node_ids[name] = node_id
        label = _escape_label(name)
        lines.append(f'    {node_id}["{label}"]')

    lines.append("")

    # Generate edges
    for edge in graph.edges:
        source_id = node_ids[edge.source]
        target_id = node_ids[edge.target]
        # Use dashed line for edges to orphan targets
        if edge.target in graph.orphan_targets:
            lines.append(f"    {source_id} -.-> {target_id}")
        else:
            lines.append(f"    {source_id} --> {target_id}")

    lines.append("")

    # Generate styles
    for name in used_nodes:
        node_id = node_ids[name]
        if name in graph.orphan_targets:
            color = NODE_COLORS["orphan"]
            lines.append(
                f"    style {node_id} fill:{color},stroke:#dc2626,stroke-dasharray: 5 5")
        elif name in graph.nodes:
            node_type = graph.nodes[name].node_type
            color = NODE_COLORS.get(node_type, "#f3f4f6")
            lines.append(f"    style {node_id} fill:{color}")

    return "\n".join(lines)


def validate_all_disorders(input_dir: Path) -> dict[str, list[str]]:
    """
    Validate causal graph integrity for all disorder files.

    Args:
        input_dir: Directory containing disorder YAML files

    Returns:
        Dict mapping disorder name to list of integrity issues
    """
    issues: dict[str, list[str]] = {}

    for yaml_path in sorted(input_dir.glob("*.yaml")):
        if yaml_path.name.endswith(".history.yaml"):
            continue
        with open(yaml_path) as f:
            disorder = yaml.safe_load(f)

        graph = build_causal_graph(disorder)
        if graph.integrity_issues:
            issues[disorder.get("name", yaml_path.stem)
                   ] = graph.integrity_issues

    return issues


def main():
    """CLI entry point for graph validation."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Validate causal graph integrity")
    parser.add_argument("--validate", "-v", metavar="DIR",
                        help="Validate all disorders in directory")
    parser.add_argument("--show", "-s", metavar="FILE",
                        help="Show Mermaid diagram for a single file")

    args = parser.parse_args()

    if args.validate:
        input_dir = Path(args.validate)
        issues = validate_all_disorders(input_dir)

        if issues:
            print(f"Found integrity issues in {len(issues)} disorders:\n")
            for disorder_name, disorder_issues in issues.items():
                print(f"{disorder_name}:")
                for issue in disorder_issues:
                    print(f"  - {issue}")
                print()
            exit(1)
        else:
            print("All disorders have valid causal graphs.")

    elif args.show:
        yaml_path = Path(args.show)
        with open(yaml_path) as f:
            disorder = yaml.safe_load(f)

        graph = build_causal_graph(disorder)
        mermaid_code = generate_mermaid(graph)

        if mermaid_code:
            print(mermaid_code)
            if graph.integrity_issues:
                print("\nIntegrity issues:")
                for issue in graph.integrity_issues:
                    print(f"  - {issue}")
        else:
            print("No causal relationships found in this disorder.")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()

"""
Build causal graphs from disorder data and generate Mermaid diagrams and
interactive D3.js pathograph JSON.

This module extracts nodes (named elements) and edges (downstream/sequelae relationships)
from disorder YAML data, performs referential integrity checks, and generates
Mermaid flowchart code and pathograph JSON for visualization.
"""

import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass
class NodeInfo:
    """Information about a node in the causal graph."""

    name: str
    node_type: str  # pathophysiology, phenotype, environmental, genetic, treatment, biochemical, experimental_model
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
    "experimental_model": "#ccfbf1",  # teal-100
    "orphan": "#fee2e2",  # red-100 for unmatched targets
}


def _sanitize_node_id(name: str) -> str:
    """Convert a node name to a valid Mermaid node ID."""
    # Replace problematic characters with underscores
    sanitized = (
        name.replace(" ", "_").replace("-", "_").replace("(", "").replace(")", "")
    )
    sanitized = sanitized.replace(",", "").replace("/", "_").replace("'", "")
    # Ensure it starts with a letter
    if sanitized and not sanitized[0].isalpha():
        sanitized = "N_" + sanitized
    return sanitized


def _escape_label(name: str) -> str:
    """Escape a node label for Mermaid."""
    # Escape quotes and other special characters in labels
    return name.replace('"', "'")


def _normalize_lookup_key(value: Any) -> str | None:
    """Normalize a lookup key for cross-section matching."""
    text = str(value).strip().lower() if value is not None else ""
    return text or None


def _descriptor_lookup_keys(descriptor: Any) -> set[str]:
    """Collect normalized lookup keys from a descriptor-like object."""
    if not isinstance(descriptor, dict):
        return set()

    term = descriptor.get("term")
    values = [descriptor.get("preferred_term")]
    if isinstance(term, dict):
        values.extend([term.get("label"), term.get("id")])

    keys = set()
    for value in values:
        key = _normalize_lookup_key(value)
        if key:
            keys.add(key)
    return keys


def _name_lookup_key(value: Any) -> set[str]:
    """Use compact, gene-like names as lookup keys when no structured term exists."""
    if not isinstance(value, str):
        return set()
    name = value.strip()
    if not name:
        return set()
    if len(name) > 20 or not all(ch.isalnum() or ch in {"-", "_"} for ch in name):
        return set()
    key = _normalize_lookup_key(name)
    return {key} if key else set()


def _gene_lookup_keys(
    item: dict[str, Any], *, allow_name_fallback: bool = False
) -> set[str]:
    """Collect structured gene identifiers from an item."""
    keys: set[str] = set()

    keys.update(_descriptor_lookup_keys(item.get("gene")))
    keys.update(_descriptor_lookup_keys(item.get("gene_term")))

    for gene in item.get("genes", []) or []:
        keys.update(_descriptor_lookup_keys(gene))

    if allow_name_fallback and not keys:
        keys.update(_name_lookup_key(item.get("name")))

    return keys


def _build_section_lookup(
    items: list[Any], descriptor_key: str | None = None
) -> dict[str, str]:
    """Build a normalized lookup from labels/term IDs to a canonical item name."""
    lookup: dict[str, str] = {}

    for item in items:
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        if not name:
            continue

        keys: set[str] = set()
        name_key = _normalize_lookup_key(name)
        if name_key:
            keys.add(name_key)
        if descriptor_key:
            keys.update(_descriptor_lookup_keys(item.get(descriptor_key)))

        for key in keys:
            lookup.setdefault(key, name)

    return lookup


def _resolve_descriptor_target(
    descriptor: dict[str, Any], lookup: dict[str, str]
) -> str | None:
    """Resolve a descriptor to a canonical named item if possible."""
    for key in _descriptor_lookup_keys(descriptor):
        if key in lookup:
            return lookup[key]
    return None


def _iter_variant_items(
    disorder: dict[str, Any],
) -> list[tuple[str | None, dict[str, Any]]]:
    """Iterate over disease-level and gene-nested variants."""
    items: list[tuple[str | None, dict[str, Any]]] = []

    for variant in disorder.get("variants", []) or []:
        if isinstance(variant, dict):
            items.append((None, variant))

    for genetic_item in disorder.get("genetic", []) or []:
        if not isinstance(genetic_item, dict):
            continue
        parent_name = genetic_item.get("name")
        for variant in genetic_item.get("variants", []) or []:
            if isinstance(variant, dict):
                items.append((parent_name, variant))

    return items


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
        ("experimental_models", "experimental_model"),
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

    for _parent_name, variant in _iter_variant_items(disorder):
        name = variant.get("name")
        if not name:
            continue
        graph.nodes[name] = NodeInfo(
            name=name,
            node_type="genetic",
            description=variant.get("description"),
        )

    phenotype_lookup = _build_section_lookup(
        disorder.get("phenotypes", []) or [], descriptor_key="phenotype_term"
    )

    pathophysiology_by_gene_key: dict[str, set[str]] = defaultdict(set)
    for item in disorder.get("pathophysiology", []) or []:
        if not isinstance(item, dict):
            continue
        source = item.get("name")
        if not source:
            continue
        for key in _gene_lookup_keys(item):
            pathophysiology_by_gene_key[key].add(source)

    genetic_nodes_by_gene_key: dict[str, set[str]] = defaultdict(set)
    for item in disorder.get("genetic", []) or []:
        if not isinstance(item, dict):
            continue
        source = item.get("name")
        if not source:
            continue
        for key in _gene_lookup_keys(item, allow_name_fallback=True):
            genetic_nodes_by_gene_key[key].add(source)

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
                    Edge(
                        source=source,
                        target=target,
                        predicate="causes",
                        source_type="pathophysiology",
                    )
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
                    Edge(
                        source=source,
                        target=target,
                        predicate="leads_to",
                        source_type="phenotype",
                    )
                )

    # Collect edges from treatment links
    for item in disorder.get("treatments", []) or []:
        if not isinstance(item, dict):
            continue
        source = item.get("name")
        if not source:
            continue

        for target_item in item.get("target_mechanisms", []) or []:
            if isinstance(target_item, dict) and "target" in target_item:
                graph.edges.append(
                    Edge(
                        source=source,
                        target=target_item["target"],
                        predicate="targets",
                        source_type="treatment",
                    )
                )

        for descriptor in item.get("target_phenotypes", []) or []:
            if not isinstance(descriptor, dict):
                continue
            target = _resolve_descriptor_target(descriptor, phenotype_lookup)
            if not target:
                continue
            graph.edges.append(
                Edge(
                    source=source,
                    target=target,
                    predicate="treats",
                    source_type="treatment",
                )
            )

    # Collect edges from experimental model links
    for item in disorder.get("experimental_models", []) or []:
        if not isinstance(item, dict):
            continue
        source = item.get("name")
        if not source:
            continue

        for link in item.get("modeled_mechanisms", []) or []:
            if isinstance(link, dict) and "target" in link:
                graph.edges.append(
                    Edge(
                        source=source,
                        target=link["target"],
                        predicate="models",
                        source_type="experimental_model",
                    )
                )

    # Collect edges from genetic factors to linked mechanisms
    for item in disorder.get("genetic", []) or []:
        if not isinstance(item, dict):
            continue
        source = item.get("name")
        if not source:
            continue

        targets: set[str] = set()
        for key in _gene_lookup_keys(item, allow_name_fallback=True):
            targets.update(pathophysiology_by_gene_key.get(key, set()))

        for target in sorted(targets):
            graph.edges.append(
                Edge(
                    source=source,
                    target=target,
                    predicate="contributes_to",
                    source_type="genetic",
                )
            )

    # Collect edges from variants to their genes or directly linked mechanisms
    for parent_name, variant in _iter_variant_items(disorder):
        source = variant.get("name")
        if not source:
            continue

        genetic_targets: set[str] = set()
        if parent_name:
            genetic_targets.add(parent_name)
        for key in _gene_lookup_keys(variant):
            genetic_targets.update(genetic_nodes_by_gene_key.get(key, set()))

        if genetic_targets:
            for target in sorted(genetic_targets):
                graph.edges.append(
                    Edge(
                        source=source,
                        target=target,
                        predicate="variant_of",
                        source_type="genetic",
                    )
                )
            continue

        mechanism_targets: set[str] = set()
        for key in _gene_lookup_keys(variant):
            mechanism_targets.update(pathophysiology_by_gene_key.get(key, set()))

        for target in sorted(mechanism_targets):
            graph.edges.append(
                Edge(
                    source=source,
                    target=target,
                    predicate="contributes_to",
                    source_type="genetic",
                )
            )

    # Check referential integrity
    for edge in graph.edges:
        if edge.target not in graph.nodes:
            graph.orphan_targets.add(edge.target)
            graph.integrity_issues.append(
                f"Target '{edge.target}' (from '{edge.source}') not found in named elements"
            )

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
                f"    style {node_id} fill:{color},stroke:#dc2626,stroke-dasharray: 5 5"
            )
        elif name in graph.nodes:
            node_type = graph.nodes[name].node_type
            color = NODE_COLORS.get(node_type, "#f3f4f6")
            lines.append(f"    style {node_id} fill:{color}")

    return "\n".join(lines)


def _extract_node_metadata(item: dict[str, Any]) -> dict[str, Any]:
    """Extract rich metadata from a disorder section item for pathograph tooltips."""
    meta: dict[str, Any] = {}

    # Evidence count
    evidence = item.get("evidence", []) or []
    if evidence:
        meta["evidence_count"] = len(evidence)

    # Cell types
    cell_types = item.get("cell_types", []) or []
    if cell_types:
        meta["cell_types"] = [
            label
            for ct in cell_types
            if isinstance(ct, dict)
            if (
                label := ct.get("preferred_term")
                or (ct.get("term", {}) or {}).get("label", "")
            )
        ]

    # Biological processes
    processes = item.get("biological_processes", []) or []
    if processes:
        meta["biological_processes"] = [
            label
            for bp in processes
            if isinstance(bp, dict)
            if (
                label := bp.get("preferred_term")
                or (bp.get("term", {}) or {}).get("label", "")
            )
        ]

    # Genes
    gene_labels: list[str] = []
    gene = item.get("gene")
    if isinstance(gene, dict):
        label = gene.get("preferred_term") or (gene.get("term", {}) or {}).get(
            "label", ""
        )
        if label:
            gene_labels.append(label)

    genes = item.get("genes", []) or []
    if genes:
        gene_labels.extend(
            label
            for g in genes
            if isinstance(g, dict)
            if (
                label := g.get("preferred_term")
                or (g.get("term", {}) or {}).get("label", "")
            )
        )

    gene_term = item.get("gene_term")
    if isinstance(gene_term, dict):
        label = gene_term.get("preferred_term") or (
            gene_term.get("term", {}) or {}
        ).get("label", "")
        if label:
            gene_labels.append(label)

    if gene_labels:
        meta["genes"] = list(dict.fromkeys(gene_labels))

    # Role (pathophysiology)
    if item.get("role"):
        meta["role"] = item["role"]

    # Frequency
    if item.get("frequency"):
        meta["frequency"] = item["frequency"]

    # Severity (phenotypes)
    if item.get("severity"):
        meta["severity"] = item["severity"]

    # Phenotype term
    pt = item.get("phenotype_term")
    if isinstance(pt, dict):
        term = pt.get("term")
        if isinstance(term, dict) and term.get("id"):
            meta["term_id"] = term["id"]

    # Locations
    locations = item.get("locations", []) or []
    if locations:
        meta["locations"] = [
            label
            for loc in locations
            if isinstance(loc, dict)
            if (
                label := loc.get("preferred_term")
                or (loc.get("term", {}) or {}).get("label", "")
            )
        ]

    # PDB structures (treatments)
    pdb_structures = item.get("pdb_structures", []) or []
    if pdb_structures:
        meta["pdb_structures"] = [
            {
                k: s[k]
                for k in (
                    "pdb_id",
                    "description",
                    "resolution_angstrom",
                    "method",
                    "ligand",
                    "target_protein",
                )
                if k in s and s[k] is not None
            }
            for s in pdb_structures
            if isinstance(s, dict) and s.get("pdb_id")
        ]

    # Treatment agents
    treatment_term = item.get("treatment_term")
    if isinstance(treatment_term, dict):
        therapeutic_agents = treatment_term.get("therapeutic_agent", []) or []
        if therapeutic_agents:
            meta["therapeutic_agents"] = [
                label
                for agent in therapeutic_agents
                if isinstance(agent, dict)
                if (
                    label := agent.get("preferred_term")
                    or (agent.get("term", {}) or {}).get("label", "")
                )
            ]

    # Experimental model metadata
    if item.get("experimental_model_type"):
        meta["model_type"] = item["experimental_model_type"]
    if item.get("namo_type"):
        meta["namo_type"] = item["namo_type"]
    conditions = item.get("conditions", []) or []
    if conditions:
        meta["conditions"] = [str(condition) for condition in conditions if condition]
    if item.get("publication"):
        meta["publication"] = item["publication"]

    # Genetic/variant metadata
    if item.get("association"):
        meta["association"] = item["association"]
    variants = item.get("variants", []) or []
    if variants:
        meta["variant_count"] = len(variants)
    if item.get("type"):
        meta["variant_type"] = item["type"]
    if item.get("clinical_significance"):
        meta["clinical_significance"] = item["clinical_significance"]
    if item.get("regulatory_category"):
        meta["regulatory_category"] = item["regulatory_category"]

    return meta


def _collect_experimental_model_links(
    disorder: dict[str, Any],
) -> dict[str, list[dict[str, Any]]]:
    """Collect experimental model links keyed by target pathophysiology node name."""
    links_by_target: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for model in disorder.get("experimental_models", []) or []:
        if not isinstance(model, dict):
            continue
        model_name = model.get("name")
        if not model_name:
            continue

        for link in model.get("modeled_mechanisms", []) or []:
            if not isinstance(link, dict):
                continue
            target = link.get("target")
            if not target:
                continue

            link_data: dict[str, Any] = {"name": model_name}
            if model.get("experimental_model_type"):
                link_data["model_type"] = model["experimental_model_type"]
            if model.get("namo_type"):
                link_data["namo_type"] = model["namo_type"]
            if link.get("description"):
                link_data["description"] = link["description"]
            links_by_target[str(target)].append(link_data)

    return links_by_target


def graph_to_json(graph: CausalGraph, disorder: dict[str, Any]) -> str:
    """
    Serialize a causal graph to JSON for the D3.js pathograph visualization.

    Enriches nodes with metadata from the disorder data (evidence counts,
    cell types, biological processes, genes, etc.) for interactive tooltips.

    Args:
        graph: CausalGraph with nodes and edges
        disorder: Full parsed disorder YAML data

    Returns:
        JSON string with {nodes: [...], edges: [...], orphan_targets: [...]}
    """
    if not graph.edges:
        return ""

    # Build a lookup from item name -> raw item dict for metadata extraction
    section_keys = [
        "pathophysiology",
        "phenotypes",
        "environmental",
        "genetic",
        "treatments",
        "biochemical",
        "experimental_models",
        "variants",
    ]
    item_lookup: dict[str, dict[str, Any]] = {}
    for section_key in section_keys:
        for item in disorder.get(section_key, []) or []:
            if isinstance(item, dict) and "name" in item:
                item_lookup[item["name"]] = item
    for _parent_name, variant in _iter_variant_items(disorder):
        if "name" in variant:
            item_lookup[variant["name"]] = variant
    model_links_by_target = _collect_experimental_model_links(disorder)

    # Build node list (only nodes used in edges)
    used_nodes: set[str] = set()
    for edge in graph.edges:
        used_nodes.add(edge.source)
        used_nodes.add(edge.target)

    nodes_json = []
    for name in sorted(used_nodes):
        node_info = graph.nodes.get(name)
        is_orphan = name in graph.orphan_targets
        node_type = (
            node_info.node_type if node_info else ("orphan" if is_orphan else "unknown")
        )
        description = node_info.description if node_info else None

        node_data: dict[str, Any] = {
            "id": name,
            "node_type": node_type,
            "color": NODE_COLORS.get(node_type, "#f3f4f6"),
            "is_orphan": is_orphan,
        }
        if description:
            node_data["description"] = description

        # Enrich with metadata from the raw disorder item
        raw_item = item_lookup.get(name)
        if raw_item:
            meta = _extract_node_metadata(raw_item)
            if meta:
                node_data["meta"] = meta
        if name in model_links_by_target:
            node_data.setdefault("meta", {})["experimental_models"] = (
                model_links_by_target[name]
            )

        nodes_json.append(node_data)

    edges_json = [
        {
            "source": edge.source,
            "target": edge.target,
            "predicate": edge.predicate,
            "is_orphan": edge.target in graph.orphan_targets,
        }
        for edge in graph.edges
    ]

    return json.dumps(
        {
            "nodes": nodes_json,
            "edges": edges_json,
            "orphan_targets": sorted(graph.orphan_targets),
        }
    )


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
            issues[disorder.get("name", yaml_path.stem)] = graph.integrity_issues

    return issues


def main():
    """CLI entry point for graph validation."""
    import argparse

    parser = argparse.ArgumentParser(description="Validate causal graph integrity")
    parser.add_argument(
        "--validate", "-v", metavar="DIR", help="Validate all disorders in directory"
    )
    parser.add_argument(
        "--show", "-s", metavar="FILE", help="Show Mermaid diagram for a single file"
    )

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

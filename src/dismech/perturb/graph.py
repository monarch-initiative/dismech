"""Build enriched causal graphs for perturbation analysis.

Wraps the base dismech.graph module and adds:
- Gene entries with HGNC IDs
- Biochemical marker mappings (LOINC, CHEBI)
- Computational model references
- Causal chain tracing
"""

from dataclasses import dataclass, field
from typing import Any

from dismech.graph import CausalGraph, build_causal_graph


@dataclass
class GeneEntry:
    """A genetic risk factor from the disorder YAML."""

    name: str
    hgnc_id: str | None = None
    description: str | None = None
    inheritance: str | None = None


@dataclass
class BiochemicalMapping:
    """A biochemical marker with ontology mappings."""

    name: str
    mappings: dict[str, str] = field(default_factory=dict)  # prefix -> ID


@dataclass
class CausalEdgeEnriched:
    """A causal edge with relationship type and mechanism."""

    source: str
    target: str
    relationship: str  # INCREASES, DECREASES, MEDIATES, etc.
    mechanism: str
    evidence: str = ""


@dataclass
class PerturbationGraph:
    """Enriched causal graph with data needed for perturbation analysis."""

    causal_graph: CausalGraph
    genes: list[GeneEntry] = field(default_factory=list)
    biochemical_mappings: list[BiochemicalMapping] = field(default_factory=list)
    computational_models: list[dict[str, Any]] = field(default_factory=list)


def build_perturbation_graph(disorder: dict[str, Any]) -> PerturbationGraph:
    """Build a perturbation-enriched causal graph from disorder YAML data.

    Args:
        disorder: Parsed disorder YAML data

    Returns:
        PerturbationGraph with causal graph, genes, biochemical mappings, and models
    """
    causal_graph = build_causal_graph(disorder)

    # Extract gene entries
    genes = []
    for item in disorder.get("genetic", []) or []:
        if not isinstance(item, dict):
            continue
        name = item.get("name", "")
        hgnc_id = None
        gene_term = item.get("gene_term")
        if isinstance(gene_term, dict):
            term = gene_term.get("term")
            if isinstance(term, dict):
                tid = term.get("id", "")
                if tid.startswith("HGNC:"):
                    hgnc_id = tid
        genes.append(
            GeneEntry(
                name=name,
                hgnc_id=hgnc_id,
                description=item.get("description"),
                inheritance=item.get("inheritance"),
            )
        )

    # Extract biochemical mappings
    biochem_mappings = []
    for item in disorder.get("biochemical", []) or []:
        if not isinstance(item, dict):
            continue
        name = item.get("name", "")
        mappings = {}
        for m in item.get("mappings_list", []) or []:
            if isinstance(m, dict):
                term = m.get("term")
                if isinstance(term, dict):
                    mid = term.get("id", "")
                else:
                    mid = ""
                prefix = mid.split(":")[0] if ":" in mid else ""
                if prefix:
                    mappings[prefix] = mid
        biochem_mappings.append(BiochemicalMapping(name=name, mappings=mappings))

    # Extract computational models
    models = []
    for item in disorder.get("computational_models", []) or []:
        if isinstance(item, dict):
            models.append(item)

    return PerturbationGraph(
        causal_graph=causal_graph,
        genes=genes,
        biochemical_mappings=biochem_mappings,
        computational_models=models,
    )


def trace_causal_paths(
    root: str,
    edges: list[CausalEdgeEnriched],
    max_depth: int = 8,
) -> list[list[CausalEdgeEnriched]]:
    """Trace all causal paths from a root node through the graph.

    Args:
        root: Starting node name
        edges: List of causal edges
        max_depth: Maximum path depth to prevent infinite traversal

    Returns:
        List of paths, where each path is a list of edges
    """
    paths: list[list[CausalEdgeEnriched]] = []
    visited: set[str] = set()

    def dfs(node: str, path: list[CausalEdgeEnriched], depth: int) -> None:
        if depth > max_depth:
            return
        visited.add(node)
        for edge in edges:
            if edge.source == node and edge.target not in visited:
                new_path = path + [edge]
                paths.append(new_path)
                dfs(edge.target, new_path, depth + 1)
        visited.discard(node)

    dfs(root, [], 0)
    return paths

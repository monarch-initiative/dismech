"""
Maximal KGX export: the whole KB as one knowledge graph, pathograph nodes included.

The biolink-conformant export (``kgx_export.py``) flattens each disorder's
mechanism layer away: pathophysiology nodes have no ontology identity, so their
constituents are re-attached to the disease and the ``downstream`` causal chain
survives only in the SEPIO sidecar. This module is the complementary
experiment: promote every entry-local causal-graph node to a first-class KG
node using the SEPIO id scheme (``dismech:<entry_stem>#<node_slug>``, minted by
:func:`dismech.export.sepio_export.pathophysiology_node_id` with the entry's
file stem as the base) and emit one graph covering:

- entry nodes: disorders (MONDO CURIE when bound, else ``dismech:<stem>``),
  modules and groupings (``dismech:<stem>`` / ``dismech:<name slug>``)
- ``dismech:has_graph_node`` membership edges (entry -> each causal-graph node)
- the causal layer itself: every :func:`dismech.graph.build_causal_graph` edge,
  with predicate ``dismech:<pathograph predicate>`` (causes, leads_to,
  triggers, models, ...); orphan targets are emitted as ``dismech:OrphanTarget``
  nodes rather than dropped, so fragmentation stays measurable
- grounding edges from local nodes to shared ontology term nodes
  (``dismech:grounded_to`` for identity descriptors such as ``phenotype_term``;
  per-slot predicates such as ``dismech:involves_cell_type`` for
  pathophysiology constituents)
- ``dismech:conforms_to`` edges into module graph nodes
- subtype nodes with ``dismech:subtype_of`` and grounding edges
- disease-level gene / inheritance / infectious-agent / MONDO-mapping edges
- comorbidity pair edges (``dismech:comorbid_with``) and grouping membership
  edges (``dismech:has_member``)

Node ``category`` distinguishes the two layers: ``dismech:*`` categories are
entry-local nodes (each exists in exactly one entry), ``biolink:*`` categories
are shared ontology term nodes — the only vertices through which two entries
can connect (besides comorbidity/grouping/mapping edges).

``kb/hypotheses`` and ``kb/surrogate_endpoints`` use different schemas and are
out of scope. Not wired into CI; run locally:

    uv run python -m dismech.export.maximal_kgx_export -o output/maximal_kgx
    uv run koza join -n "output/maximal_kgx/maximal_nodes.jsonl" \\
        -e "output/maximal_kgx/maximal_edges.jsonl" \\
        -o output/maximal_kgx/graph.duckdb
    uv run koza report graph-stats -d output/maximal_kgx/graph.duckdb
    uv run koza report connectivity -d output/maximal_kgx/graph.duckdb \\
        --output-dir output/maximal_kgx/connectivity
"""

import argparse
import json
from pathlib import Path
from typing import Any

from dismech import kb_cache
from dismech.export.sepio_export import _slug, pathophysiology_node_id
from dismech.graph import build_causal_graph

KNOWLEDGE_SOURCE = "infores:dismech"

# Pathophysiology constituent slots: slot -> (predicate, term-node category).
PATHO_TERM_SLOTS = {
    "cell_types": ("dismech:involves_cell_type", "biolink:Cell"),
    "biological_processes": ("dismech:involves_process", "biolink:BiologicalProcess"),
    "molecular_functions": (
        "dismech:involves_molecular_function",
        "biolink:MolecularActivity",
    ),
    "cellular_components": (
        "dismech:involves_cellular_component",
        "biolink:CellularComponent",
    ),
    "chemical_entities": ("dismech:involves_chemical", "biolink:ChemicalEntity"),
    "pathways": ("dismech:involves_pathway", "biolink:Pathway"),
    "protein_complexes": ("dismech:involves_complex", "biolink:MacromolecularComplex"),
    "locations": ("dismech:occurs_in", "biolink:AnatomicalEntity"),
    "triggers": ("dismech:triggered_by_exposure", "biolink:ExposureEvent"),
    "genes": ("dismech:involves_gene", "biolink:Gene"),
    "gene_products": ("dismech:involves_gene_product", "biolink:Gene"),
}

# Identity descriptor per section: the local node IS (approximately) this term.
# section -> (descriptor slot, term-node category)
IDENTITY_SLOTS = {
    "phenotypes": ("phenotype_term", "biolink:PhenotypicFeature"),
    "environmental": ("exposure_term", "biolink:ExposureEvent"),
    "genetic": ("gene_term", "biolink:Gene"),
    "biochemical": ("biomarker_term", "biolink:MolecularEntity"),
    "histopathology": ("finding_term", "biolink:PhenotypicFeature"),
}


def _term(descriptor: Any) -> tuple[str, str | None] | None:
    """Return (curie, label) from a descriptor's bound ``term:``, or None."""
    if not isinstance(descriptor, dict):
        return None
    term = descriptor.get("term")
    if not isinstance(term, dict):
        return None
    curie = term.get("id")
    if not isinstance(curie, str) or ":" not in curie:
        return None
    return curie, term.get("label")


def _local_category(node_type: str) -> str:
    """Map a causal-graph node_type to a dismech:* KGX category."""
    return (
        "dismech:"
        + "".join(part.capitalize() for part in node_type.split("_"))
        + "Node"
    )


class GraphAccumulator:
    """Deduplicating collector for KGX node and edge records."""

    def __init__(self) -> None:
        self.nodes: dict[str, dict[str, Any]] = {}
        self.edges: dict[tuple[str, str, str], dict[str, Any]] = {}

    def add_node(
        self, node_id: str, name: str | None, category: str, **extra: Any
    ) -> None:
        existing = self.nodes.get(node_id)
        if existing is not None:
            # Keep the first record; fill a missing name if a later one has it.
            if not existing.get("name") and name:
                existing["name"] = name
            return
        record: dict[str, Any] = {
            "id": node_id,
            "category": [category],
            "name": name or "",
            "provided_by": ["dismech"],
        }
        record.update({k: v for k, v in extra.items() if v})
        self.nodes[node_id] = record

    def add_edge(
        self,
        subject: str,
        predicate: str,
        obj: str,
        section: str,
        entry: str,
        **extra: Any,
    ) -> None:
        key = (subject, predicate, obj)
        if key in self.edges:
            return
        record: dict[str, Any] = {
            "id": f"{_slug(entry)}:{len(self.edges)}",
            "subject": subject,
            "predicate": predicate,
            "object": obj,
            "category": ["biolink:Association"],
            "knowledge_source": KNOWLEDGE_SOURCE,
            "dismech_entry": entry,
            "dismech_section": section,
        }
        record.update({k: v for k, v in extra.items() if v})
        self.edges[key] = record


def _entry_id(stem: str, record: dict[str, Any], kind: str) -> str:
    """Entry node id: the bound MONDO CURIE for disorders, else dismech:<stem>."""
    if kind == "disorder":
        got = _term(record.get("disease_term") or {})
        if got:
            return got[0]
    return f"dismech:{_slug(stem)}"


def _grounding_edges(
    acc: GraphAccumulator, stem: str, section: str, item: dict[str, Any], node_id: str
) -> None:
    """Emit grounding edges from one entry-local node to its ontology terms."""
    if section == "pathophysiology":
        for slot, (predicate, category) in PATHO_TERM_SLOTS.items():
            values = item.get(slot)
            if isinstance(values, dict):
                values = [values]
            for descriptor in values or []:
                got = _term(descriptor)
                if not got:
                    continue
                curie, label = got
                acc.add_node(curie, label, category)
                acc.add_edge(node_id, predicate, curie, f"pathophysiology.{slot}", stem)
        # single-valued gene descriptor
        got = _term(item.get("gene"))
        if got:
            curie, label = got
            acc.add_node(curie, label, "biolink:Gene")
            acc.add_edge(
                node_id, "dismech:involves_gene", curie, "pathophysiology.gene", stem
            )
        # genetic_context: the lesion behind this mechanism node. A distinct
        # predicate (not involves_gene) so germline vs somatic drivers stay
        # queryable — the variant origin and impact ride along as properties.
        context = item.get("genetic_context")
        if isinstance(context, dict):
            descriptors = [context.get("gene"), *(context.get("genes") or [])]
            for descriptor in descriptors:
                got = _term(descriptor)
                if not got:
                    continue
                curie, label = got
                acc.add_node(curie, label, "biolink:Gene")
                acc.add_edge(
                    node_id,
                    "dismech:has_causal_variant_in",
                    curie,
                    "pathophysiology.genetic_context",
                    stem,
                    variant_origin=context.get("variant_origin"),
                    functional_impact_category=context.get(
                        "functional_impact_category"
                    ),
                )
        return

    if section == "treatments":
        treatment_term = item.get("treatment_term") or {}
        got = _term(treatment_term)
        if got:
            curie, label = got
            acc.add_node(curie, label, "biolink:Treatment")
            acc.add_edge(
                node_id, "dismech:grounded_to", curie, "treatments.treatment_term", stem
            )
        for agent in treatment_term.get("therapeutic_agent") or []:
            got = _term(agent)
            if got:
                curie, label = got
                acc.add_node(curie, label, "biolink:ChemicalEntity")
                acc.add_edge(
                    node_id,
                    "dismech:has_therapeutic_agent",
                    curie,
                    "treatments.therapeutic_agent",
                    stem,
                )
        got = _term(item.get("regimen_term"))
        if got:
            curie, label = got
            acc.add_node(curie, label, "biolink:Treatment")
            acc.add_edge(
                node_id, "dismech:has_regimen", curie, "treatments.regimen_term", stem
            )
        return

    spec = IDENTITY_SLOTS.get(section)
    if not spec:
        return
    slot, category = spec
    got = _term(item.get(slot))
    if not got:
        return
    curie, label = got
    # MONDO-typed "phenotypes" are comorbid diseases (see kgx_export.py).
    if category == "biolink:PhenotypicFeature" and curie.startswith("MONDO:"):
        category = "biolink:Disease"
    acc.add_node(curie, label, category)
    acc.add_edge(node_id, "dismech:grounded_to", curie, f"{section}.{slot}", stem)


# Sections whose named items can be causal-graph nodes, walked for groundings.
GROUNDABLE_SECTIONS = (
    "pathophysiology",
    "phenotypes",
    "environmental",
    "genetic",
    "treatments",
    "biochemical",
    "histopathology",
)


def process_entry(
    acc: GraphAccumulator, stem: str, record: dict[str, Any], kind: str
) -> str:
    """Emit nodes/edges for one disorder or module entry. Returns the entry id."""
    entry_id = _entry_id(stem, record, kind)
    entry_category = (
        "biolink:Disease" if kind == "disorder" else "dismech:MechanismModule"
    )
    acc.add_node(entry_id, record.get("name"), entry_category, dismech_entry_kind=kind)

    graph = build_causal_graph(record)

    # Entry-local causal-graph nodes + membership edges.
    for name, info in graph.nodes.items():
        node_id = pathophysiology_node_id(stem, name)
        acc.add_node(node_id, name, _local_category(info.node_type))
        acc.add_edge(entry_id, "dismech:has_graph_node", node_id, info.node_type, stem)

    # Orphan targets: emit so fragmentation stays measurable, distinctly typed.
    for name in graph.orphan_targets:
        node_id = pathophysiology_node_id(stem, name)
        if node_id not in acc.nodes:
            acc.add_node(node_id, name, "dismech:OrphanTarget")

    # The causal layer.
    for edge in graph.edges:
        acc.add_edge(
            pathophysiology_node_id(stem, edge.source),
            f"dismech:{edge.predicate}",
            pathophysiology_node_id(stem, edge.target),
            f"causal.{edge.source_type}",
            stem,
            hypothesis_groups="|".join(edge.hypothesis_groups) or None,
            causal_link_type=edge.causal_link_type,
        )

    # Groundings + conforms_to, from the raw sections.
    for section in GROUNDABLE_SECTIONS:
        for item in record.get(section) or []:
            if not isinstance(item, dict):
                continue
            name = item.get("name")
            if not name:
                continue
            node_id = pathophysiology_node_id(stem, name)
            if node_id not in acc.nodes:
                # Named item that never entered the causal graph: emit it
                # anyway (maximal), typed by its section.
                section_type = {
                    "phenotypes": "phenotype",
                    "treatments": "treatment",
                }.get(
                    section,
                    section.rstrip("s")
                    if section != "pathophysiology"
                    else "pathophysiology",
                )
                acc.add_node(node_id, name, _local_category(section_type))
                acc.add_edge(entry_id, "dismech:has_graph_node", node_id, section, stem)
            _grounding_edges(acc, stem, section, item, node_id)

            if section == "pathophysiology" and item.get("conforms_to"):
                ref = str(item["conforms_to"])
                if "#" in ref:
                    module, target = ref.split("#", 1)
                    obj = pathophysiology_node_id(module, target)
                else:
                    obj = f"dismech:{_slug(ref)}"
                acc.add_edge(node_id, "dismech:conforms_to", obj, "conforms_to", stem)

    # Subtypes.
    for subtype in record.get("has_subtypes") or []:
        if not isinstance(subtype, dict) or not subtype.get("name"):
            continue
        subtype_id = pathophysiology_node_id(stem, subtype["name"])
        acc.add_node(
            subtype_id,
            subtype.get("display_name") or subtype["name"],
            "dismech:Subtype",
        )
        acc.add_edge(subtype_id, "dismech:subtype_of", entry_id, "has_subtypes", stem)
        got = _term(subtype.get("subtype_term"))
        if got:
            curie, label = got
            acc.add_node(curie, label, "biolink:Disease")
            acc.add_edge(
                subtype_id,
                "dismech:grounded_to",
                curie,
                "has_subtypes.subtype_term",
                stem,
            )
        for gene in subtype.get("genes") or []:
            got = _term(gene)
            if got:
                curie, label = got
                acc.add_node(curie, label, "biolink:Gene")
                acc.add_edge(
                    subtype_id, "dismech:has_gene", curie, "has_subtypes.genes", stem
                )

    # Disease-level term links.
    for inheritance in record.get("inheritance") or []:
        got = _term(
            inheritance.get("inheritance_term")
            if isinstance(inheritance, dict)
            else None
        )
        if got:
            curie, label = got
            acc.add_node(curie, label, "biolink:GeneticInheritance")
            acc.add_edge(
                entry_id, "dismech:has_inheritance", curie, "inheritance", stem
            )
    for agent in record.get("infectious_agent") or []:
        got = _term(
            agent.get("infectious_agent_term") if isinstance(agent, dict) else None
        )
        if got:
            curie, label = got
            acc.add_node(curie, label, "biolink:OrganismTaxon")
            acc.add_edge(
                entry_id,
                "dismech:has_infectious_agent",
                curie,
                "infectious_agent",
                stem,
            )
    for mapping in ((record.get("mappings") or {}).get("mondo_mappings")) or []:
        got = _term(mapping)
        if got and got[0] != entry_id:
            curie, label = got
            acc.add_node(curie, label, "biolink:Disease")
            acc.add_edge(
                entry_id,
                mapping.get("mapping_predicate") or "skos:relatedMatch",
                curie,
                "mappings.mondo_mappings",
                stem,
            )

    return entry_id


def process_comorbidity(
    acc: GraphAccumulator, stem: str, record: dict[str, Any]
) -> None:
    """Emit the disease-disease pair edge for one comorbidity entry."""
    got_a = _term(record.get("disease_a"))
    got_b = _term(record.get("disease_b"))
    if not got_a or not got_b:
        return
    for curie, label in (got_a, got_b):
        acc.add_node(curie, label, "biolink:Disease")
    acc.add_edge(
        got_a[0],
        "dismech:comorbid_with",
        got_b[0],
        "comorbidity",
        stem,
        directionality=record.get("directionality"),
        effect_direction=record.get("effect_direction"),
    )


def process_grouping(
    acc: GraphAccumulator,
    stem: str,
    record: dict[str, Any],
    disease_ids_by_name: dict[str, str],
    grouping_ids_by_name: dict[str, str],
) -> None:
    """Emit the grouping node and its membership edges."""
    grouping_id = grouping_ids_by_name[record["name"]]
    acc.add_node(
        grouping_id,
        record.get("display_name") or record.get("name"),
        "dismech:Grouping",
        dismech_entry_kind="grouping",
    )
    for member in record.get("members") or []:
        if not isinstance(member, dict):
            continue
        name = member.get("member")
        if not name:
            continue
        member_type = member.get("member_type") or "DISEASE"
        if member_type == "MODULE":
            member_id = f"dismech:{_slug(name)}"
        elif member_type == "GROUPING":
            member_id = grouping_ids_by_name.get(name) or f"dismech:{_slug(name)}"
        else:
            member_id = disease_ids_by_name.get(name)
            if member_id is None:
                member_id = f"dismech:{_slug(name)}"
                acc.add_node(member_id, name, "dismech:UnresolvedMember")
        acc.add_edge(grouping_id, "dismech:has_member", member_id, "members", stem)

    for mapping in ((record.get("mappings") or {}).get("mondo_mappings")) or []:
        got = _term(mapping)
        if got:
            curie, label = got
            acc.add_node(curie, label, "biolink:Disease")
            acc.add_edge(
                grouping_id,
                mapping.get("mapping_predicate") or "skos:relatedMatch",
                curie,
                "mappings.mondo_mappings",
                stem,
            )


def export_kb(kb_dir: Path, out_dir: Path) -> tuple[int, int]:
    """Walk the KB and write maximal_nodes.jsonl / maximal_edges.jsonl."""
    acc = GraphAccumulator()
    disease_ids_by_name: dict[str, str] = {}

    for path in sorted((kb_dir / "disorders").glob("*.yaml")):
        record = kb_cache.load_document(path)
        entry_id = process_entry(acc, path.stem, record, "disorder")
        if record.get("name"):
            disease_ids_by_name[record["name"]] = entry_id

    for path in sorted((kb_dir / "modules").glob("*.yaml")):
        process_entry(acc, path.stem, kb_cache.load_document(path), "module")

    for path in sorted((kb_dir / "comorbidities").glob("*.yaml")):
        process_comorbidity(acc, path.stem, kb_cache.load_document(path))

    grouping_paths = sorted((kb_dir / "groupings").glob("*.yaml"))
    grouping_records = [(p.stem, kb_cache.load_document(p)) for p in grouping_paths]
    grouping_ids_by_name = {
        record["name"]: f"dismech:{_slug(record['name'])}"
        for _, record in grouping_records
        if record.get("name")
    }
    for stem, record in grouping_records:
        if record.get("name"):
            process_grouping(
                acc, stem, record, disease_ids_by_name, grouping_ids_by_name
            )

    # Closure safety net: build_causal_graph does not guarantee every edge
    # endpoint appears in graph.nodes or graph.orphan_targets (e.g. unresolved
    # reports_on sources). Emit any missing endpoint as an orphan node so the
    # edge list is closed over the node list.
    for subject, _, obj in list(acc.edges):
        for endpoint in (subject, obj):
            if endpoint not in acc.nodes:
                name = endpoint.split("#", 1)[-1].replace("_", " ")
                acc.add_node(endpoint, name, "dismech:OrphanTarget")

    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / "maximal_nodes.jsonl").open("w", encoding="utf-8") as fh:
        for node in acc.nodes.values():
            fh.write(json.dumps(node, ensure_ascii=False) + "\n")
    with (out_dir / "maximal_edges.jsonl").open("w", encoding="utf-8") as fh:
        for edge in acc.edges.values():
            fh.write(json.dumps(edge, ensure_ascii=False) + "\n")
    return len(acc.nodes), len(acc.edges)


def main() -> None:
    # Single corpus walk: the parsed-KB cache would be pure cost (see kb_cache).
    kb_cache.default_off()
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("--kb-dir", type=Path, default=Path("kb"))
    parser.add_argument(
        "-o", "--out-dir", type=Path, default=Path("output/maximal_kgx")
    )
    args = parser.parse_args()
    n_nodes, n_edges = export_kb(args.kb_dir, args.out_dir)
    print(f"Wrote {n_nodes} nodes, {n_edges} edges to {args.out_dir}")


if __name__ == "__main__":
    main()

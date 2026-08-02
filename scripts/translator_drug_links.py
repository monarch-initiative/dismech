#!/usr/bin/env python3
"""Explore candidate disease-drug links via the NCATS Biomedical Translator.

This is a **lead-generation** tool, not an evidence source. It submits a
TRAPI creative-mode ("inferred") query to the Translator ARS -- the same
service behind https://ui.transltr.io/ -- asking *what chemicals may treat
this disease*, then renders the ranked answers as a curator-facing report
that flags which candidates are already covered by the dismech entry.

Translator answers are aggregated and partly model-inferred, so they are
treated exactly like deep-research output: leads to verify, never text to
paste into an entry. Nothing here writes KB YAML. The actionable payload is
the per-candidate list of PMIDs / NCT ids, which a curator then puts through
the normal `just fetch-reference` + `just validate-references` path.

Examples:
  uv run python scripts/translator_drug_links.py kb/disorders/Asthma.yaml
  uv run python scripts/translator_drug_links.py --mondo MONDO:0004979 --top 40
  uv run python scripts/translator_drug_links.py --name "Marfan syndrome"
  uv run python scripts/translator_drug_links.py kb/disorders/Asthma.yaml \
      --new-only --asserted-only --format tsv
  uv run python scripts/translator_drug_links.py --pk <ars-pk>   # re-render a past run
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections import deque
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import httpx
import yaml

DEFAULT_ARS_URL = "https://ars-prod.transltr.io"
CI_ARS_URL = "https://ars.ci.transltr.io"
ARS_UI_URL = "https://ui.transltr.io/main/results"
CI_UI_URL = "https://ui.ci.transltr.io/main/results"
NAME_RESOLVER_URL = "https://name-resolution-sri.renci.org/lookup"
NODE_NORM_URL = "https://nodenormalization-sri.renci.org/get_normalized_nodes"
HUMAN_TAXON = "NCBITaxon:9606"

DEFAULT_TIMEOUT_SECONDS = 900
DEFAULT_POLL_SECONDS = 15
# A single stuck ARA can keep an otherwise-finished run in "Running" for many
# minutes, so stop once the agent statuses have not moved for this long.
DEFAULT_STALL_SECONDS = 180
DEFAULT_TOP = 25
MAX_PUBLICATIONS_PER_CANDIDATE = 8
MAX_TRIALS_PER_CANDIDATE = 5

# Intermediate node types a mechanism path may run through, for --via.
VIA_CATEGORIES = {
    "gene": ["biolink:Gene"],
    "protein": ["biolink:Protein"],
    "gene-or-protein": ["biolink:Gene", "biolink:Protein"],
    "pathway": ["biolink:Pathway"],
    "process": ["biolink:BiologicalProcessOrActivity"],
    "phenotype": ["biolink:PhenotypicFeature"],
    "chemical": ["biolink:ChemicalEntity"],
    "any": ["biolink:NamedThing"],
}
DEFAULT_VIA = "gene"

# A node's `categories` list is frequently partial -- a drug often comes back as
# `biolink:MolecularEntity` with no `biolink:ChemicalEntity` -- so a route hopping
# through another drug can only be recognized by testing the whole family.
CHEMICAL_CATEGORIES = frozenset(
    {
        "biolink:ChemicalEntity",
        "biolink:ChemicalMixture",
        "biolink:Drug",
        "biolink:MolecularEntity",
        "biolink:MolecularMixture",
        "biolink:SmallMolecule",
    }
)

PUBLICATION_PATTERNS = (
    (re.compile(r"(?:^|/)(?:pubmed/|PMID[:_])(\d+)", re.IGNORECASE), "PMID:{}"),
    (re.compile(r"(?:^|/)PMC(\d+)", re.IGNORECASE), "PMC{}"),
    (re.compile(r"(NCT\d{8})", re.IGNORECASE), "{}"),
    (re.compile(r"(?:doi\.org/|DOI:)(10\.\S+)", re.IGNORECASE), "doi:{}"),
)


# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------


@dataclass
class Candidate:
    """One ranked chemical answer for the queried disease."""

    node_id: str
    name: str
    score: float | None = None
    knowledge_levels: set[str] = field(default_factory=set)
    sources: set[str] = field(default_factory=set)
    publications: list[str] = field(default_factory=list)
    trials: list[str] = field(default_factory=list)
    approval_status: str | None = None
    max_research_phase: float | None = None
    equivalent_ids: list[str] = field(default_factory=list)
    curated_as: str | None = None

    @property
    def asserted(self) -> bool:
        """True when at least one direct edge is a curated assertion, not a prediction."""
        return bool(self.knowledge_levels - {"prediction", ""})

    @property
    def status(self) -> str:
        return "CURATED" if self.curated_as else "NEW"


@dataclass
class Hop:
    """One edge of a mechanism path, in the direction the source asserts it."""

    subject: str
    subject_name: str
    predicate: str
    object: str
    object_name: str
    sources: list[str] = field(default_factory=list)
    publications: list[str] = field(default_factory=list)
    # True when the route traverses this edge against the direction it was asserted in.
    reverse: bool = False

    def render(self) -> str:
        """Render left-to-right along the route, but never flip the asserted direction.

        A route legitimately walks an edge backwards; rewriting `BCR -interacts_with-> SIN3A`
        as `SIN3A -interacts_with-> BCR` would misreport what the source actually claims,
        so a reversed hop keeps its subject on the right and points the arrow back.
        """
        predicate = self.predicate.replace("biolink:", "")
        if self.reverse:
            return f"{self.object_name} <--{predicate}-- {self.subject_name}"
        return f"{self.subject_name} --{predicate}--> {self.object_name}"


@dataclass
class PathCandidate:
    """A drug -> intermediate -> disease mechanism path proposed by Translator."""

    node_id: str
    name: str
    categories: list[str] = field(default_factory=list)
    score: float | None = None
    hops: list[Hop] = field(default_factory=list)
    sources: set[str] = field(default_factory=set)
    publications: list[str] = field(default_factory=list)
    equivalent_ids: list[str] = field(default_factory=list)
    curated_as: str | None = None
    # Pathfinder routes run through several intermediates; the two-hop query has one.
    intermediates: list[str] = field(default_factory=list)
    intermediate_names: list[str] = field(default_factory=list)

    @property
    def status(self) -> str:
        return "IN ENTRY" if self.curated_as else "NEW"

    def render(self) -> str:
        return " | ".join(hop.render() for hop in self.hops)


# --------------------------------------------------------------------------
# Query construction (pure)
# --------------------------------------------------------------------------


def build_query(disease_curie: str, *, predicate: str = "biolink:treats", inferred: bool = True) -> dict[str, Any]:
    """Build the TRAPI message asking which chemicals may treat `disease_curie`."""
    edge: dict[str, Any] = {
        "subject": "chem",
        "object": "disease",
        "predicates": [predicate],
    }
    if inferred:
        edge["knowledge_type"] = "inferred"
    return {
        "message": {
            "query_graph": {
                "nodes": {
                    "disease": {"ids": [disease_curie], "categories": ["biolink:Disease"]},
                    "chem": {"categories": ["biolink:ChemicalEntity"]},
                },
                "edges": {"e": edge},
            }
        }
    }


def build_path_query(
    disease_curie: str,
    drug_curie: str,
    *,
    via_categories: list[str] | None = None,
) -> dict[str, Any]:
    """Build a two-hop TRAPI lookup: drug -> intermediate -> disease.

    Both ends are pinned, so every answer is a candidate mechanism *path* rather
    than a ranked drug. Predicates are left open: constraining them drops real
    routes (`physically_interacts_with` vs `affects` vs `interacts_with` are all
    used for the same drug-target relation across knowledge providers).
    """
    return {
        "message": {
            "query_graph": {
                "nodes": {
                    "chem": {"ids": [drug_curie], "categories": ["biolink:ChemicalEntity"]},
                    "mid": {"categories": list(via_categories or VIA_CATEGORIES[DEFAULT_VIA])},
                    "disease": {"ids": [disease_curie], "categories": ["biolink:Disease"]},
                },
                "edges": {
                    "e1": {"subject": "chem", "object": "mid"},
                    "e2": {"subject": "mid", "object": "disease"},
                },
            }
        }
    }


def build_pathfinder_query(
    subject_curie: str,
    object_curie: str,
    *,
    intermediate_categories: list[str] | None = None,
) -> dict[str, Any]:
    """Build a TRAPI Pathfinder query — the UI's "how are these two related?" mode.

    Unlike the two-hop lookup this asks the ARS for arbitrary-length routes and
    lets it combine lookup and inferred reasoning. `predicates` on a QPath is an
    intent hint, not a filter; the real constraint is `intermediate_categories`,
    which every returned path must pass through.
    """
    path: dict[str, Any] = {
        "subject": "n0",
        "object": "n1",
        "predicates": ["biolink:related_to"],
    }
    if intermediate_categories:
        path["constraints"] = [{"intermediate_categories": list(intermediate_categories)}]
    return {
        "message": {
            "query_graph": {
                "nodes": {
                    "n0": {"ids": [subject_curie], "categories": ["biolink:ChemicalEntity"]},
                    "n1": {"ids": [object_curie], "categories": ["biolink:Disease"]},
                },
                "paths": {"p0": path},
            }
        }
    }


def build_regulation_query(
    *,
    gene_curie: str | None = None,
    chemical_curie: str | None = None,
    direction: str = "decreased",
    aspect: str = "activity_or_abundance",
) -> dict[str, Any]:
    """Build the UI's up/down-regulation template as a qualified creative query.

    Pin the gene to ask *which chemicals* regulate it; pin the chemical to ask
    *which genes* it regulates. The direction rides on the Biolink qualifier set
    rather than the predicate, which stays `biolink:affects`.
    """
    if bool(gene_curie) == bool(chemical_curie):
        raise ValueError("Pin exactly one of gene_curie or chemical_curie.")
    chem_node: dict[str, Any] = {"categories": ["biolink:ChemicalEntity"]}
    gene_node: dict[str, Any] = {"categories": ["biolink:Gene"]}
    if chemical_curie:
        chem_node["ids"] = [chemical_curie]
    if gene_curie:
        gene_node["ids"] = [gene_curie]
    return {
        "message": {
            "query_graph": {
                "nodes": {"chem": chem_node, "gene": gene_node},
                "edges": {
                    "e": {
                        "subject": "chem",
                        "object": "gene",
                        "predicates": ["biolink:affects"],
                        "qualifier_constraints": [
                            {
                                "qualifier_set": [
                                    {
                                        "qualifier_type_id": "biolink:object_aspect_qualifier",
                                        "qualifier_value": aspect,
                                    },
                                    {
                                        "qualifier_type_id": "biolink:object_direction_qualifier",
                                        "qualifier_value": direction,
                                    },
                                ]
                            }
                        ],
                        "knowledge_type": "inferred",
                    }
                },
            }
        }
    }


# --------------------------------------------------------------------------
# ARS client
# --------------------------------------------------------------------------


class ARSClient:
    def __init__(self, base_url: str, timeout: float = 120.0):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.Client(timeout=timeout, follow_redirects=True)

    def close(self) -> None:
        self.client.close()

    def submit(self, query: dict[str, Any]) -> str:
        response = self.client.post(f"{self.base_url}/ars/api/submit", json=query)
        response.raise_for_status()
        pk = response.json().get("pk")
        if not pk:
            raise SystemExit("ARS accepted the query but returned no pk.")
        return str(pk)

    def trace(self, pk: str) -> dict[str, Any]:
        response = self.client.get(f"{self.base_url}/ars/api/messages/{pk}", params={"trace": "y"})
        response.raise_for_status()
        return response.json()

    def message(self, pk: str) -> dict[str, Any]:
        response = self.client.get(f"{self.base_url}/ars/api/messages/{pk}")
        response.raise_for_status()
        return response.json()


def trace_signature(trace: dict[str, Any]) -> tuple[tuple[str, str, Any], ...]:
    """Per-agent (agent, status, result_count) tuple used to detect a stalled run."""
    return tuple(
        sorted(
            (
                (child.get("actor") or {}).get("agent", "?"),
                str(child.get("status")),
                child.get("result_count"),
            )
            for child in trace.get("children") or []
        )
    )


def pending_agents(trace: dict[str, Any]) -> list[str]:
    return [
        (child.get("actor") or {}).get("agent", "?")
        for child in trace.get("children") or []
        if child.get("status") == "Running"
    ]


def _clean_pk(value: Any) -> str | None:
    """The ARS returns a missing merged version as the string "None", not as null."""
    if not value or str(value).strip().lower() in {"none", "null"}:
        return None
    return str(value)


def summarize_trace(trace: dict[str, Any]) -> str:
    """One-line-per-agent status summary for the progress log."""
    parts = []
    for child in trace.get("children") or []:
        agent = (child.get("actor") or {}).get("agent", "?")
        count = child.get("result_count")
        suffix = f"({count})" if count else ""
        parts.append(f"{agent}:{child.get('status')}{suffix}")
    return " ".join(parts)


def poll_for_merged(
    client: ARSClient,
    pk: str,
    *,
    timeout_seconds: int,
    poll_seconds: int,
    stall_seconds: int = DEFAULT_STALL_SECONDS,
    verbose: bool = True,
) -> tuple[str, bool]:
    """Poll the ARS until the run settles. Returns (merged_pk, complete)."""
    deadline = time.monotonic() + timeout_seconds
    merged_pk: str | None = None
    signature: tuple[Any, ...] | None = None
    last_change = time.monotonic()
    while True:
        trace = client.trace(pk)
        merged_pk = _clean_pk(trace.get("merged_version")) or merged_pk
        status = trace.get("status")
        if verbose:
            print(f"  [{status}] {summarize_trace(trace)}", file=sys.stderr)
        if status and status != "Running":
            if not merged_pk:
                raise SystemExit(
                    f"ARS run {pk} finished with status {status} but produced no merged result set. "
                    "If this was a non-default --via, no ARA answers that intermediate type today "
                    "(only `gene` has broad support); try --via gene or --pathfinder."
                )
            return merged_pk, True

        current = trace_signature(trace)
        if current != signature:
            signature, last_change = current, time.monotonic()
        elif merged_pk and stall_seconds and time.monotonic() - last_change >= stall_seconds:
            stragglers = ", ".join(pending_agents(trace)) or "unknown agents"
            print(
                f"  no change for {stall_seconds}s while waiting on {stragglers}; "
                f"rendering what has merged so far (re-run with --pk {pk} for the rest)",
                file=sys.stderr,
            )
            return merged_pk, False

        if time.monotonic() >= deadline:
            if merged_pk:
                print(
                    f"  timeout after {timeout_seconds}s; rendering the partial merged set "
                    f"(re-run with --pk {pk} later for the complete answer)",
                    file=sys.stderr,
                )
                return merged_pk, False
            raise SystemExit(
                f"Timed out after {timeout_seconds}s with no merged results yet. "
                f"Re-run with --pk {pk} to pick the run back up."
            )
        time.sleep(poll_seconds)


# --------------------------------------------------------------------------
# Result extraction (pure)
# --------------------------------------------------------------------------


def _as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def normalize_publication(raw: Any) -> str | None:
    """Normalize a publication reference to a dismech-style CURIE, or None."""
    if not isinstance(raw, str) or not raw.strip():
        return None
    text = raw.strip()
    for pattern, template in PUBLICATION_PATTERNS:
        match = pattern.search(text)
        if match:
            return template.format(match.group(1).upper() if template == "{}" else match.group(1))
    return None


def _node_ids(result: dict[str, Any], key: str) -> set[str]:
    return {
        binding.get("id")
        for binding in (result.get("node_bindings") or {}).get(key, [])
        if binding.get("id")
    }


def _result_edge_ids(result: dict[str, Any]) -> list[str]:
    edge_ids: list[str] = []
    for analysis in result.get("analyses") or []:
        for bindings in (analysis.get("edge_bindings") or {}).values():
            for binding in bindings:
                if binding.get("id"):
                    edge_ids.append(binding["id"])
    return edge_ids


def _score(result: dict[str, Any]) -> float | None:
    scores = [
        analysis.get("score")
        for analysis in result.get("analyses") or []
        if isinstance(analysis.get("score"), int | float)
    ]
    return max(scores) if scores else None


def extract_candidates(
    message: dict[str, Any],
    *,
    answer_key: str = "chem",
    pinned_key: str = "disease",
) -> list[Candidate]:
    """Collapse TRAPI results into one Candidate per answer node, best score first.

    Only edges that directly connect the answer node to the pinned node
    contribute provenance; mechanism-path edges reached through support graphs
    describe *how* a prediction was made, not whether the claim holds. The two
    keys name the query-graph nodes: `chem`/`disease` for the treats template,
    `chem`/`gene` (or `gene`/`chem`) for the up/down-regulation templates.
    """
    knowledge_graph = message.get("knowledge_graph") or {}
    nodes = knowledge_graph.get("nodes") or {}
    edges = knowledge_graph.get("edges") or {}

    by_chem: dict[str, Candidate] = {}
    for result in message.get("results") or []:
        chem_ids = _node_ids(result, answer_key)
        disease_ids = _node_ids(result, pinned_key)
        if not chem_ids:
            continue
        primary = sorted(chem_ids)[0]
        candidate = by_chem.get(primary)
        if candidate is None:
            candidate = Candidate(node_id=primary, name=(nodes.get(primary) or {}).get("name") or primary)
            by_chem[primary] = candidate

        score = _score(result)
        if score is not None and (candidate.score is None or score > candidate.score):
            candidate.score = score

        for edge_id in _result_edge_ids(result):
            edge = edges.get(edge_id)
            if not edge:
                continue
            subject, obj = edge.get("subject"), edge.get("object")
            direct = (subject in chem_ids and obj in disease_ids) or (obj in chem_ids and subject in disease_ids)
            if not direct:
                continue

            for source in edge.get("sources") or []:
                if source.get("resource_role") == "primary_knowledge_source" and source.get("resource_id"):
                    candidate.sources.add(str(source["resource_id"]).replace("infores:", ""))

            for attribute in edge.get("attributes") or []:
                type_id = attribute.get("attribute_type_id")
                value = attribute.get("value")
                if type_id == "biolink:publications":
                    for item in _as_list(value):
                        reference = normalize_publication(item)
                        if reference and reference not in candidate.publications:
                            candidate.publications.append(reference)
                elif type_id == "biolink:supporting_study":
                    for item in _as_list(value):
                        trial = normalize_publication(item)
                        if trial and trial.startswith("NCT") and trial not in candidate.trials:
                            candidate.trials.append(trial)
                elif type_id == "biolink:knowledge_level" and isinstance(value, str):
                    candidate.knowledge_levels.add(value)
                elif type_id == "biolink:clinical_approval_status" and isinstance(value, str):
                    candidate.approval_status = value.replace("biolink:", "")
                elif type_id == "biolink:max_research_phase" and isinstance(value, int | float):
                    if candidate.max_research_phase is None or value > candidate.max_research_phase:
                        candidate.max_research_phase = float(value)

    return sorted(by_chem.values(), key=lambda c: (-(c.score or 0.0), c.name.lower()))


def _edge_provenance(edge: dict[str, Any]) -> tuple[list[str], list[str]]:
    """Primary knowledge sources and normalized publications for one KG edge."""
    sources = [
        str(source["resource_id"]).replace("infores:", "")
        for source in edge.get("sources") or []
        if source.get("resource_role") == "primary_knowledge_source" and source.get("resource_id")
    ]
    publications: list[str] = []
    for attribute in edge.get("attributes") or []:
        if attribute.get("attribute_type_id") != "biolink:publications":
            continue
        for item in _as_list(attribute.get("value")):
            reference = normalize_publication(item)
            if reference and reference not in publications:
                publications.append(reference)
    return sources, publications


def order_path_edges(
    edge_ids: list[str],
    edges: dict[str, Any],
    start: str,
    end: str,
) -> list[tuple[str, bool]]:
    """Order a Pathfinder auxiliary graph into a chain from `start` to `end`.

    Pathfinder returns each route as an unordered *bag* of edges, so it has to be
    walked back into a readable chain. Returns (edge_id, forward) pairs for the
    shortest traversal, treating edges as undirected — a route legitimately runs
    against edge direction (`gene <-interacts_with- drug`). Empty when the bag
    does not actually connect the two endpoints.
    """
    adjacency: dict[str, list[tuple[str, str, bool]]] = {}
    for edge_id in edge_ids:
        edge = edges.get(edge_id)
        if not edge:
            continue
        subject, obj = edge.get("subject"), edge.get("object")
        if not subject or not obj:
            continue
        adjacency.setdefault(subject, []).append((obj, edge_id, True))
        adjacency.setdefault(obj, []).append((subject, edge_id, False))

    queue: deque[tuple[str, list[tuple[str, bool]], set[str]]] = deque([(start, [], {start})])
    while queue:
        node, chain, seen = queue.popleft()
        if node == end:
            return chain
        for next_node, edge_id, forward in adjacency.get(node, []):
            if next_node in seen:
                continue
            queue.append((next_node, [*chain, (edge_id, forward)], seen | {next_node}))
    return []


def extract_pathfinder_paths(
    message: dict[str, Any],
    *,
    start: str,
    end: str,
    include_chemical_intermediates: bool = False,
) -> list[PathCandidate]:
    """Turn Pathfinder `path_bindings` into ordered, renderable mechanism chains.

    Routes through another drug are dropped by default. `intermediate_categories`
    only requires that a listed category appears *somewhere* on the route, so a
    gene-constrained Pathfinder query still returns drug > gene > rival-drug >
    disease routes -- co-prescription and shared-target artifacts that crowd out
    the mechanism the caller asked about.
    """
    knowledge_graph = message.get("knowledge_graph") or {}
    nodes = knowledge_graph.get("nodes") or {}
    edges = knowledge_graph.get("edges") or {}
    auxiliary = message.get("auxiliary_graphs") or {}

    def name_of(curie: str) -> str:
        return (nodes.get(curie) or {}).get("name") or curie

    paths: list[PathCandidate] = []
    seen_chains: set[tuple[str, ...]] = set()
    for result in message.get("results") or []:
        for analysis in result.get("analyses") or []:
            for bindings in (analysis.get("path_bindings") or {}).values():
                for binding in bindings:
                    graph_id = binding.get("id")
                    chain = order_path_edges(
                        list((auxiliary.get(graph_id) or {}).get("edges") or []), edges, start, end
                    )
                    if not chain:
                        continue

                    hops: list[Hop] = []
                    intermediates: list[str] = []
                    intermediate_names: list[str] = []
                    sources: set[str] = set()
                    publications: list[str] = []
                    for edge_id, forward in chain:
                        edge = edges[edge_id]
                        edge_sources, edge_publications = _edge_provenance(edge)
                        subject, obj = edge["subject"], edge["object"]
                        hops.append(
                            Hop(
                                subject=subject,
                                subject_name=name_of(subject),
                                predicate=edge.get("predicate", ""),
                                object=obj,
                                object_name=name_of(obj),
                                sources=edge_sources,
                                publications=edge_publications,
                                reverse=not forward,
                            )
                        )
                        sources.update(edge_sources)
                        for publication in edge_publications:
                            if publication not in publications:
                                publications.append(publication)
                        # The node the route arrives at, which is the edge's
                        # subject when the hop is traversed backwards.
                        arrival = obj if forward else subject
                        if arrival not in (start, end):
                            intermediates.append(arrival)
                            intermediate_names.append(name_of(arrival))

                    signature = tuple(intermediates)
                    if signature in seen_chains:
                        continue
                    # Routes that hop through another drug are co-target artifacts,
                    # not mechanism; the UI shows them, curation rarely wants them.
                    if not include_chemical_intermediates and any(
                        CHEMICAL_CATEGORIES.intersection((nodes.get(curie) or {}).get("categories") or [])
                        for curie in intermediates
                    ):
                        continue
                    seen_chains.add(signature)

                    score = analysis.get("score")
                    paths.append(
                        PathCandidate(
                            node_id=intermediates[0] if intermediates else str(graph_id),
                            name=" > ".join(intermediate_names) or str(graph_id),
                            score=float(score) if isinstance(score, int | float) else None,
                            hops=hops,
                            sources=sources,
                            publications=publications,
                            intermediates=intermediates,
                            intermediate_names=intermediate_names,
                        )
                    )

    return sorted(paths, key=lambda p: (-(p.score or 0.0), p.name.lower()))


def extract_paths(message: dict[str, Any], *, via_categories: list[str] | None = None) -> list[PathCandidate]:
    """Collapse two-hop TRAPI results into one PathCandidate per intermediate node.

    Each answer is a drug -> intermediate -> disease route. Answers are grouped by
    the intermediate, because the same gene is typically reached by several
    equivalent predicate spellings across knowledge providers.
    """
    knowledge_graph = message.get("knowledge_graph") or {}
    nodes = knowledge_graph.get("nodes") or {}
    edges = knowledge_graph.get("edges") or {}
    wanted = set(via_categories or [])

    by_node: dict[str, PathCandidate] = {}
    for result in message.get("results") or []:
        mid_ids = _node_ids(result, "mid")
        if not mid_ids:
            continue
        mid_id = sorted(mid_ids)[0]
        node = nodes.get(mid_id) or {}
        categories = list(node.get("categories") or [])
        # ARAs occasionally answer with an off-category intermediate (a biologic
        # returned for a Gene slot); keep the answer honest to what was asked.
        if wanted and categories and not wanted.intersection(categories):
            continue

        path = by_node.get(mid_id)
        if path is None:
            path = PathCandidate(
                node_id=mid_id,
                name=node.get("name") or mid_id,
                categories=categories,
                intermediates=[mid_id],
                intermediate_names=[node.get("name") or mid_id],
            )
            by_node[mid_id] = path

        for analysis in result.get("analyses") or []:
            score = analysis.get("score")
            if isinstance(score, int | float) and (path.score is None or score > path.score):
                path.score = float(score)

            hops: list[Hop] = []
            for edge_key in sorted((analysis.get("edge_bindings") or {}).keys()):
                for binding in (analysis.get("edge_bindings") or {})[edge_key]:
                    edge = edges.get(binding.get("id"))
                    if not edge:
                        continue
                    sources, publications = _edge_provenance(edge)
                    hops.append(
                        Hop(
                            subject=edge.get("subject", ""),
                            subject_name=(nodes.get(edge.get("subject")) or {}).get("name")
                            or edge.get("subject", ""),
                            predicate=edge.get("predicate", ""),
                            object=edge.get("object", ""),
                            object_name=(nodes.get(edge.get("object")) or {}).get("name") or edge.get("object", ""),
                            sources=sources,
                            publications=publications,
                        )
                    )
                    path.sources.update(sources)
                    for publication in publications:
                        if publication not in path.publications:
                            path.publications.append(publication)
                    break  # one representative edge per query-graph hop
            if len(hops) > len(path.hops):
                path.hops = hops

    return sorted(by_node.values(), key=lambda p: (-(p.score or 0.0), p.name.lower()))


# --------------------------------------------------------------------------
# dismech cross-reference (pure)
# --------------------------------------------------------------------------


def curated_agents(disease: dict[str, Any]) -> tuple[dict[str, str], dict[str, str]]:
    """Return (curie -> label, lowercased name -> label) for treatments already curated."""
    by_curie: dict[str, str] = {}
    by_name: dict[str, str] = {}
    for treatment in disease.get("treatments") or []:
        label = treatment.get("name") or ""
        if label:
            by_name.setdefault(label.strip().lower(), label)
        term = treatment.get("treatment_term") or {}
        for agent in term.get("therapeutic_agent") or []:
            agent_label = agent.get("preferred_term") or label
            curie = ((agent.get("term") or {}).get("id") or "").strip()
            if curie:
                by_curie.setdefault(curie, agent_label)
            if agent_label:
                by_name.setdefault(agent_label.strip().lower(), agent_label)
        regimen = (treatment.get("regimen_term") or {}).get("term") or {}
        if regimen.get("id"):
            by_curie.setdefault(regimen["id"], label)
    return by_curie, by_name


def _match_curated(
    curies: list[str],
    name: str,
    by_curie: dict[str, str],
    by_name: dict[str, str],
) -> str | None:
    """First CURIE hit (case-insensitive: dismech writes `hgnc:`, Translator `HGNC:`), else a name hit."""
    folded = {curie.lower(): label for curie, label in by_curie.items()}
    for curie in curies:
        match = folded.get(curie.lower())
        if match:
            return match
    return by_name.get(name.strip().lower())


def annotate_curated(candidates: list[Candidate], by_curie: dict[str, str], by_name: dict[str, str]) -> None:
    """Mark candidates already present in the entry, by equivalent CURIE or by name."""
    for candidate in candidates:
        candidate.curated_as = _match_curated(
            [candidate.node_id, *candidate.equivalent_ids], candidate.name, by_curie, by_name
        )


def curated_mechanism_index(disease: dict[str, Any]) -> tuple[dict[str, str], dict[str, str]]:
    """Return (curie -> where, lowercased name -> where) for mechanism entities the entry models.

    Covers the disease-level `genetic:` list and every gene, biological process,
    molecular function, and chemical entity bound on a pathophysiology node, so a
    Translator path can be reported as "already in your pathograph" vs new.
    """
    by_curie: dict[str, str] = {}
    by_name: dict[str, str] = {}

    def record(descriptor: Any, where: str) -> None:
        if not isinstance(descriptor, dict):
            return
        term = descriptor.get("term") or {}
        curie = (term.get("id") or "").strip()
        if curie:
            by_curie.setdefault(curie, where)
        for label in (descriptor.get("preferred_term"), term.get("label")):
            if label:
                by_name.setdefault(str(label).strip().lower(), where)

    for gene in disease.get("genetic") or []:
        where = f"genetic: {gene.get('name') or ''}".strip().rstrip(":")
        record(gene.get("gene_term"), where)
        if gene.get("name"):
            by_name.setdefault(str(gene["name"]).strip().lower(), where)

    for node in disease.get("pathophysiology") or []:
        where = f"pathophysiology: {node.get('name') or ''}".strip().rstrip(":")
        for slot in ("genes", "biological_processes", "molecular_functions", "chemical_entities", "gene_products"):
            for descriptor in node.get(slot) or []:
                record(descriptor, where)
        record(node.get("gene"), where)

    return by_curie, by_name


def annotate_paths(paths: list[PathCandidate], by_curie: dict[str, str], by_name: dict[str, str]) -> None:
    """Mark paths whose intermediates the entry already models."""
    for path in paths:
        path.curated_as = _match_curated(
            [path.node_id, *path.intermediates, *path.equivalent_ids], path.name, by_curie, by_name
        )
        if path.curated_as is None:
            for label in path.intermediate_names:
                match = by_name.get(label.strip().lower())
                if match:
                    path.curated_as = match
                    break


def drug_target_mechanisms(disease: dict[str, Any], curated_as: str | None) -> list[str]:
    """The pathophysiology nodes the entry already says this treatment acts on."""
    targets: list[str] = []
    for treatment in disease.get("treatments") or []:
        names = {str(treatment.get("name") or "").strip().lower()}
        for agent in (treatment.get("treatment_term") or {}).get("therapeutic_agent") or []:
            names.add(str(agent.get("preferred_term") or "").strip().lower())
        if curated_as and curated_as.strip().lower() not in names:
            continue
        for mechanism in treatment.get("target_mechanisms") or []:
            label = mechanism.get("target")
            effect = mechanism.get("treatment_effect")
            if label:
                targets.append(f"{label} ({effect})" if effect else str(label))
    return targets


# --------------------------------------------------------------------------
# Network helpers
# --------------------------------------------------------------------------


def resolve_disease_name(name: str, *, limit: int = 5) -> list[tuple[str, str]]:
    """Look a disease name up in the SRI name resolver, best match first."""
    response = httpx.get(
        NAME_RESOLVER_URL,
        params={"string": name, "biolink_type": "biolink:Disease", "limit": limit},
        timeout=60.0,
        follow_redirects=True,
    )
    response.raise_for_status()
    payload = response.json()
    rows = payload.get("results", payload) if isinstance(payload, dict) else payload
    resolved = []
    for row in rows or []:
        curie = row.get("curie")
        if curie:
            resolved.append((curie, row.get("label") or ""))
    return resolved


def normalize_curies(curies: list[str]) -> dict[str, dict[str, Any]]:
    """Batch-normalize chemical CURIEs via the SRI node normalizer.

    Returns `{queried_curie: {"id", "label", "equivalents"}}`. Enrichment is
    best-effort: an unreachable normalizer degrades to name-only matching.
    """
    normalized: dict[str, dict[str, Any]] = {}
    for start in range(0, len(curies), 100):
        chunk = curies[start : start + 100]
        try:
            response = httpx.post(
                NODE_NORM_URL,
                json={"curies": chunk, "conflate": True, "drug_chemical_conflate": True},
                timeout=90.0,
                follow_redirects=True,
            )
            response.raise_for_status()
            payload = response.json()
        except (httpx.HTTPError, json.JSONDecodeError) as error:  # non-fatal enrichment
            print(f"  node normalizer unavailable ({error}); falling back to name matching", file=sys.stderr)
            return normalized
        for curie, entry in (payload or {}).items():
            if not entry:
                continue
            identifier = entry.get("id") or {}
            normalized[curie] = {
                "id": identifier.get("identifier") or curie,
                "label": identifier.get("label") or "",
                "equivalents": [
                    item.get("identifier")
                    for item in entry.get("equivalent_identifiers") or []
                    if item.get("identifier")
                ],
            }
    return normalized


def merge_equivalents(candidates: list[Candidate], normalized: dict[str, dict[str, Any]]) -> list[Candidate]:
    """Collapse candidates that normalize to the same chemical (e.g. salt vs base forms)."""
    merged: dict[str, Candidate] = {}
    for candidate in candidates:
        entry = normalized.get(candidate.node_id) or {}
        key = entry.get("id") or candidate.node_id
        candidate.equivalent_ids = list(entry.get("equivalents") or [])
        target = merged.get(key)
        if target is None:
            candidate.node_id = key
            candidate.name = entry.get("label") or candidate.name
            merged[key] = candidate
            continue
        if candidate.score is not None and (target.score is None or candidate.score > target.score):
            target.score = candidate.score
        target.knowledge_levels |= candidate.knowledge_levels
        target.sources |= candidate.sources
        target.approval_status = target.approval_status or candidate.approval_status
        if candidate.max_research_phase is not None:
            target.max_research_phase = max(target.max_research_phase or 0.0, candidate.max_research_phase)
        for publication in candidate.publications:
            if publication not in target.publications:
                target.publications.append(publication)
        for trial in candidate.trials:
            if trial not in target.trials:
                target.trials.append(trial)
    return sorted(merged.values(), key=lambda c: (-(c.score or 0.0), c.name.lower()))


# --------------------------------------------------------------------------
# Rendering (pure)
# --------------------------------------------------------------------------


DISCLAIMER = (
    "Translator answers are aggregated across many knowledge providers and are "
    "partly model-inferred. Treat every row as a **lead, not evidence**: verify each "
    "PMID/NCT with `just fetch-reference` and quote only text that "
    "`just validate-references` confirms. Do not paste Translator output into a KB entry."
)


def _phase(candidate: Candidate) -> str:
    if candidate.max_research_phase is None:
        return ""
    return f"phase {candidate.max_research_phase:g}"


def render_markdown(
    candidates: list[Candidate],
    *,
    disease_curie: str,
    disease_label: str,
    pk: str,
    ui_url: str,
    complete: bool,
    entry_path: str | None,
    generated_at: str,
    title: str = "Translator drug-link leads",
    pinned_role: str = "Disease",
) -> str:
    lines = [
        f"# {title}: {disease_label or disease_curie}",
        "",
        f"- {pinned_role}: `{disease_curie}`" + (f" ({disease_label})" if disease_label else ""),
        f"- dismech entry: `{entry_path}`" if entry_path else "- dismech entry: (none supplied)",
        f"- ARS pk: `{pk}`",
        f"- Translator UI: {ui_url}",
        f"- Generated: {generated_at}",
        f"- Candidates: {len(candidates)}",
    ]
    if not complete:
        lines.append("- **Partial**: the ARS run had not fully settled when this report was rendered.")
    lines += [
        "",
        f"> {DISCLAIMER}",
        "",
        "| # | Status | Drug | CURIE | Score | Level | Evidence | Sources |",
        "| - | ------ | ---- | ----- | ----- | ----- | -------- | ------- |",
    ]
    for index, candidate in enumerate(candidates, start=1):
        evidence_bits = []
        if candidate.publications:
            evidence_bits.append(f"{len(candidate.publications)} pub")
        if candidate.trials:
            evidence_bits.append(f"{len(candidate.trials)} trial")
        if candidate.approval_status:
            evidence_bits.append(candidate.approval_status)
        phase = _phase(candidate)
        if phase:
            evidence_bits.append(phase)
        level = "asserted" if candidate.asserted else "predicted"
        score = f"{candidate.score:.2f}" if candidate.score is not None else ""
        sources = ", ".join(sorted(candidate.sources)[:3])
        lines.append(
            f"| {index} | {candidate.status} | {candidate.name} | `{candidate.node_id}` | "
            f"{score} | {level} | {', '.join(evidence_bits)} | {sources} |"
        )

    lines += ["", "## Candidate detail", ""]
    for index, candidate in enumerate(candidates, start=1):
        lines.append(f"### {index}. {candidate.name} (`{candidate.node_id}`) — {candidate.status}")
        if candidate.curated_as:
            lines.append(f"- Already curated as: **{candidate.curated_as}**")
        if candidate.score is not None:
            lines.append(f"- Translator score: {candidate.score:.3f}")
        lines.append(f"- Knowledge level: {', '.join(sorted(candidate.knowledge_levels)) or 'prediction'}")
        if candidate.approval_status or candidate.max_research_phase is not None:
            lines.append(
                "- Clinical status: "
                + ", ".join(part for part in (candidate.approval_status, _phase(candidate)) if part)
            )
        if candidate.sources:
            lines.append(f"- Primary knowledge sources: {', '.join(sorted(candidate.sources))}")
        publications = candidate.publications[:MAX_PUBLICATIONS_PER_CANDIDATE]
        if publications:
            lines.append(f"- Publications to verify: {', '.join(f'`{p}`' for p in publications)}")
            pmids = [p for p in publications if p.startswith("PMID:")]
            if pmids:
                lines.append(f"  - `just fetch-reference {pmids[0]}`")
        trials = candidate.trials[:MAX_TRIALS_PER_CANDIDATE]
        if trials:
            lines.append(f"- Trials to verify: {', '.join(f'`{t}`' for t in trials)}")
            lines.append(f"  - `just fetch-reference {trials[0]}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


PATH_DISCLAIMER = (
    "These paths are **machine-generated leads**, not curated mechanism. Each hop is a "
    "single knowledge-provider assertion — text-mined co-occurrence (`semmeddb`) sits "
    "beside curated pharmacology (`drugcentral`, `dgidb`) with no distinction in the "
    "ranking. A path is a hypothesis to check against primary literature, and every "
    "PMID below still has to go through `just fetch-reference` + "
    "`just validate-references` before it can support anything in an entry."
)


def render_paths_markdown(
    paths: list[PathCandidate],
    *,
    drug_curie: str,
    drug_label: str,
    disease_curie: str,
    disease_label: str,
    via: str,
    pk: str,
    ui_url: str,
    complete: bool,
    entry_path: str | None,
    curated_drug: str | None,
    curated_targets: list[str],
    generated_at: str,
) -> str:
    lines = [
        f"# Translator mechanism paths: {drug_label or drug_curie} -> {disease_label or disease_curie}",
        "",
        f"- Drug: `{drug_curie}`" + (f" ({drug_label})" if drug_label else ""),
        f"- Disease: `{disease_curie}`" + (f" ({disease_label})" if disease_label else ""),
        f"- Intermediate node type: `{via}`",
        f"- dismech entry: `{entry_path}`" if entry_path else "- dismech entry: (none supplied)",
    ]
    if curated_drug:
        lines.append(f"- Entry already curates this drug as: **{curated_drug}**")
        if curated_targets:
            lines.append(f"  - declared `target_mechanisms`: {'; '.join(curated_targets)}")
        else:
            lines.append("  - no `target_mechanisms` declared — the paths below are candidates for it")
    elif entry_path:
        lines.append("- Entry does not yet curate this drug.")
    lines += [
        f"- ARS pk: `{pk}`",
        f"- Translator UI: {ui_url}",
        f"- Generated: {generated_at}",
        f"- Paths: {len(paths)}",
    ]
    if not complete:
        lines.append("- **Partial**: the ARS run had not fully settled when this report was rendered.")
    lines += [
        "",
        f"> {PATH_DISCLAIMER}",
        "",
        "| # | Intermediate | In entry? | Score | Path | Sources |",
        "| - | ------------ | --------- | ----- | ---- | ------- |",
    ]
    for index, path in enumerate(paths, start=1):
        score = f"{path.score:.2f}" if path.score is not None else ""
        where = path.curated_as or "—"
        lines.append(
            f"| {index} | {path.name} (`{path.node_id}`) | {where} | {score} | "
            f"{path.render()} | {', '.join(sorted(path.sources)[:3])} |"
        )

    lines += ["", "## Path detail", ""]
    for index, path in enumerate(paths, start=1):
        lines.append(f"### {index}. via {path.name} (`{path.node_id}`) — {path.status}")
        if path.curated_as:
            lines.append(f"- Entry already models this as: **{path.curated_as}**")
        if path.score is not None:
            lines.append(f"- Translator score: {path.score:.3f}")
        for hop in path.hops:
            detail = f"- {hop.render()}"
            if hop.sources:
                detail += f"  \n  - asserted by: {', '.join(sorted(set(hop.sources)))}"
            if hop.publications:
                shown = hop.publications[:MAX_PUBLICATIONS_PER_CANDIDATE]
                detail += f"  \n  - publications: {', '.join(f'`{p}`' for p in shown)}"
            lines.append(detail)
        pmids = [p for p in path.publications if p.startswith("PMID:")]
        if pmids:
            lines.append(f"- Verify first: `just fetch-reference {pmids[0]}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_paths_tsv(paths: list[PathCandidate]) -> str:
    header = ["rank", "intermediate", "curie", "in_entry", "score", "path", "publications", "sources"]
    rows = ["\t".join(header)]
    for index, path in enumerate(paths, start=1):
        rows.append(
            "\t".join(
                [
                    str(index),
                    path.name,
                    path.node_id,
                    path.curated_as or "",
                    f"{path.score:.4f}" if path.score is not None else "",
                    path.render(),
                    "|".join(path.publications[:MAX_PUBLICATIONS_PER_CANDIDATE]),
                    "|".join(sorted(path.sources)),
                ]
            )
        )
    return "\n".join(rows) + "\n"


def render_paths_json(paths: list[PathCandidate], **meta: Any) -> str:
    payload = {
        **meta,
        "disclaimer": PATH_DISCLAIMER,
        "paths": [
            {
                "rank": index,
                "intermediate": path.name,
                "curie": path.node_id,
                "categories": path.categories,
                "in_entry": path.curated_as,
                "score": path.score,
                "hops": [
                    {
                        "subject": hop.subject,
                        "subject_name": hop.subject_name,
                        "predicate": hop.predicate,
                        "object": hop.object,
                        "object_name": hop.object_name,
                        "sources": hop.sources,
                        "publications": hop.publications,
                    }
                    for hop in path.hops
                ],
                "publications": path.publications[:MAX_PUBLICATIONS_PER_CANDIDATE],
                "sources": sorted(path.sources),
            }
            for index, path in enumerate(paths, start=1)
        ],
    }
    return json.dumps(payload, indent=2) + "\n"


def render_tsv(candidates: list[Candidate]) -> str:
    header = [
        "rank",
        "status",
        "drug",
        "curie",
        "score",
        "knowledge_level",
        "approval_status",
        "max_research_phase",
        "publications",
        "trials",
        "sources",
        "curated_as",
    ]
    rows = ["\t".join(header)]
    for index, candidate in enumerate(candidates, start=1):
        rows.append(
            "\t".join(
                [
                    str(index),
                    candidate.status,
                    candidate.name,
                    candidate.node_id,
                    f"{candidate.score:.4f}" if candidate.score is not None else "",
                    "asserted" if candidate.asserted else "predicted",
                    candidate.approval_status or "",
                    f"{candidate.max_research_phase:g}" if candidate.max_research_phase is not None else "",
                    "|".join(candidate.publications[:MAX_PUBLICATIONS_PER_CANDIDATE]),
                    "|".join(candidate.trials[:MAX_TRIALS_PER_CANDIDATE]),
                    "|".join(sorted(candidate.sources)),
                    candidate.curated_as or "",
                ]
            )
        )
    return "\n".join(rows) + "\n"


def render_json(candidates: list[Candidate], **meta: Any) -> str:
    payload = {
        **meta,
        "disclaimer": DISCLAIMER,
        "candidates": [
            {
                "rank": index,
                "status": candidate.status,
                "name": candidate.name,
                "curie": candidate.node_id,
                "score": candidate.score,
                "knowledge_levels": sorted(candidate.knowledge_levels),
                "asserted": candidate.asserted,
                "approval_status": candidate.approval_status,
                "max_research_phase": candidate.max_research_phase,
                "publications": candidate.publications[:MAX_PUBLICATIONS_PER_CANDIDATE],
                "trials": candidate.trials[:MAX_TRIALS_PER_CANDIDATE],
                "sources": sorted(candidate.sources),
                "curated_as": candidate.curated_as,
            }
            for index, candidate in enumerate(candidates, start=1)
        ],
    }
    return json.dumps(payload, indent=2) + "\n"


# --------------------------------------------------------------------------
# Hypothesis-provider output (kb/hypotheses/<Disease>/<hypothesis_id>/translator.md)
# --------------------------------------------------------------------------

PROVIDER_SLUG = "translator"
DEFAULT_HYPOTHESIS_ROOT = Path("kb/hypotheses")


def find_hypothesis(disease: dict[str, Any], hypothesis_group_id: str) -> dict[str, Any]:
    """Look up one `mechanistic_hypotheses` entry, listing the alternatives on a miss."""
    hypotheses = disease.get("mechanistic_hypotheses") or []
    for hypothesis in hypotheses:
        if str(hypothesis.get("hypothesis_group_id") or "").casefold() == hypothesis_group_id.casefold():
            return hypothesis
    available = ", ".join(str(h.get("hypothesis_group_id")) for h in hypotheses if h.get("hypothesis_group_id"))
    raise SystemExit(
        f"No mechanistic_hypotheses entry with hypothesis_group_id '{hypothesis_group_id}'. "
        f"Available: {available or '(none in this entry)'}"
    )


def hypothesis_report_paths(root: Path, disorder_slug: str, hypothesis_group_id: str) -> tuple[Path, Path]:
    """Report and citations paths, matching the deep-research provider convention."""
    directory = root / disorder_slug / hypothesis_group_id
    report = directory / f"{PROVIDER_SLUG}.md"
    return report, report.with_name(f"{report.name}.citations.md")


def build_hypothesis_frontmatter(
    *,
    hypothesis: dict[str, Any],
    disease_name: str,
    query: dict[str, Any],
    ars_url: str,
    pk: str,
    merged_pk: str,
    citation_count: int,
    started_at: str,
    ended_at: str,
    duration_seconds: float,
) -> dict[str, Any]:
    """Provenance frontmatter in the shape the provider pipeline already reads."""
    return {
        "provider": PROVIDER_SLUG,
        "model": "ncats-translator-ars",
        "cached": False,
        "start_time": started_at,
        "end_time": ended_at,
        "duration_seconds": round(duration_seconds, 2),
        "citation_count": citation_count,
        "template_variables": {
            "disease_name": disease_name,
            "hypothesis_group_id": hypothesis.get("hypothesis_group_id"),
            "hypothesis_label": hypothesis.get("hypothesis_label") or hypothesis.get("hypothesis_group_id"),
            "hypothesis_status": hypothesis.get("status"),
        },
        "provider_config": {
            "ars_url": ars_url,
            "ars_pk": pk,
            "merged_pk": merged_pk,
            "query_graph": query["message"]["query_graph"],
        },
    }


def render_citations(references: list[str], *, query_description: str) -> str:
    """Citations sidecar: the query, then the numbered references the paths rest on."""
    lines = [
        "# Citations for Translator path query",
        "",
        f"**Query:** {query_description}",
        "",
        "Every reference below is an unverified lead carried over from a knowledge-provider",
        "edge annotation. Fetch each with `just fetch-reference <ID>` before citing it.",
        "",
        "## Citations",
        "",
    ]
    lines += [f"{index}. {reference}" for index, reference in enumerate(references, start=1)] or ["(none)"]
    return "\n".join(lines) + "\n"


def write_hypothesis_report(
    report_path: Path,
    citations_path: Path,
    *,
    frontmatter: dict[str, Any],
    body: str,
    references: list[str],
    query_description: str,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    header = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).rstrip()
    report_path.write_text(f"---\n{header}\n---\n\n{body}", encoding="utf-8")
    citations_path.write_text(render_citations(references, query_description=query_description), encoding="utf-8")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("entry", nargs="?", help="Path to a kb/disorders/*.yaml entry (supplies the MONDO id).")
    parser.add_argument("--mondo", help="Disease CURIE to query instead of reading one from an entry.")
    parser.add_argument("--name", help="Disease name to resolve via the SRI name resolver.")
    parser.add_argument("--pk", help="Re-render an existing ARS run instead of submitting a new one.")
    parser.add_argument("--ars-url", default=DEFAULT_ARS_URL, help=f"ARS base URL (default {DEFAULT_ARS_URL}).")
    parser.add_argument("--ci", action="store_true", help=f"Use the CI instance ({CI_ARS_URL}).")
    parser.add_argument("--predicate", default="biolink:treats", help="Biolink predicate to query.")
    parser.add_argument("--no-inferred", action="store_true", help="Disable creative mode (lookup-only answers).")
    parser.add_argument("--top", type=int, default=DEFAULT_TOP, help=f"Candidates to report (default {DEFAULT_TOP}).")
    parser.add_argument("--asserted-only", action="store_true", help="Keep only candidates with a curated assertion.")
    parser.add_argument("--new-only", action="store_true", help="Keep only candidates absent from the entry.")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS, help="Seconds to wait for the ARS.")
    parser.add_argument("--poll-interval", type=int, default=DEFAULT_POLL_SECONDS, help="Seconds between polls.")
    parser.add_argument(
        "--stall-seconds",
        type=int,
        default=DEFAULT_STALL_SECONDS,
        help="Give up on stragglers after this long without any agent status change (0 disables).",
    )
    parser.add_argument("--format", choices=("markdown", "json", "tsv"), default="markdown", help="Output format.")
    parser.add_argument("--output", help="Write the report to this path instead of stdout.")
    parser.add_argument("--save-raw", help="Also save the merged TRAPI message to this path.")

    paths = parser.add_argument_group("mechanism paths (drug-disease pair)")
    paths.add_argument(
        "--drug",
        help="Switch to path mode: a chemical CURIE (CHEBI:45783) or name (imatinib). "
        "Returns drug -> intermediate -> disease mechanism paths instead of ranked drugs.",
    )
    paths.add_argument(
        "--via",
        choices=sorted(VIA_CATEGORIES),
        default=DEFAULT_VIA,
        help=f"Intermediate node type for path mode (default {DEFAULT_VIA}).",
    )
    paths.add_argument(
        "--pathfinder",
        action="store_true",
        help="Use the ARS Pathfinder query (the UI's 'how are these related?' mode) instead of the "
        "two-hop lookup: arbitrary-length routes, ARS-ordered. Only the CI ARS supports it, so "
        "this implies --ci.",
    )
    paths.add_argument(
        "--include-chemical-intermediates",
        action="store_true",
        help="Pathfinder only: keep routes that hop through another drug. These are co-target "
        "and co-prescription artifacts and are dropped by default, because they otherwise "
        "crowd out the mechanism routes entirely.",
    )
    paths.add_argument(
        "--hypothesis",
        help="Write the path report as a provider report for this mechanistic_hypotheses "
        "group id, under kb/hypotheses/<Disorder>/<id>/translator.md (implies path mode).",
    )
    paths.add_argument(
        "--hypothesis-root",
        default=str(DEFAULT_HYPOTHESIS_ROOT),
        help=f"Root for hypothesis provider reports (default {DEFAULT_HYPOTHESIS_ROOT}).",
    )
    regulation = parser.add_argument_group("regulation templates (chemical <-> gene)")
    regulation.add_argument(
        "--regulates",
        metavar="GENE",
        help="Ask which chemicals up/down-regulate this gene (CURIE or symbol).",
    )
    regulation.add_argument(
        "--regulated-by",
        metavar="CHEMICAL",
        help="Ask which genes this chemical up/down-regulates (CURIE or name).",
    )
    regulation.add_argument(
        "--direction",
        choices=("increased", "decreased"),
        default="decreased",
        help="Regulation direction (default decreased).",
    )
    return parser.parse_args(argv)


def resolve_gene_name(name: str, *, limit: int = 5) -> list[tuple[str, str]]:
    """Look a human gene symbol up in the SRI name resolver, best match first.

    `only_taxa` is not optional here: an unrestricted lookup for ABL1 returns the
    dog orthologue first, which would silently answer a different question.
    """
    response = httpx.get(
        NAME_RESOLVER_URL,
        params={
            "string": name,
            "biolink_type": "biolink:Gene",
            "only_taxa": HUMAN_TAXON,
            "limit": limit,
        },
        timeout=60.0,
        follow_redirects=True,
    )
    response.raise_for_status()
    payload = response.json()
    rows = payload.get("results", payload) if isinstance(payload, dict) else payload
    return [(row["curie"], row.get("label") or "") for row in rows or [] if row.get("curie")]


def resolve_chemical_name(name: str, *, limit: int = 5) -> list[tuple[str, str]]:
    """Look a drug name up in the SRI name resolver, best match first."""
    response = httpx.get(
        NAME_RESOLVER_URL,
        params={"string": name, "biolink_type": "biolink:ChemicalEntity", "limit": limit},
        timeout=60.0,
        follow_redirects=True,
    )
    response.raise_for_status()
    payload = response.json()
    rows = payload.get("results", payload) if isinstance(payload, dict) else payload
    return [(row["curie"], row.get("label") or "") for row in rows or [] if row.get("curie")]


def _load_entry(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def _disease_from_entry(entry: dict[str, Any], path: str) -> tuple[str, str]:
    term = (entry.get("disease_term") or {}).get("term") or {}
    curie = term.get("id")
    if not curie:
        raise SystemExit(f"{path} has no disease_term.term.id; pass --mondo explicitly.")
    return curie, term.get("label") or entry.get("name") or ""


def _run_query(client: ARSClient, args: argparse.Namespace, query: dict[str, Any] | None) -> tuple[str, str, bool]:
    """Submit (or replay) a query and poll to a merged result set."""
    if args.pk:
        pk = args.pk
    else:
        assert query is not None
        pk = client.submit(query)
        print(f"Submitted to {client.base_url} as pk {pk}", file=sys.stderr)
    merged_pk, complete = poll_for_merged(
        client,
        pk,
        timeout_seconds=args.timeout,
        poll_seconds=args.poll_interval,
        stall_seconds=args.stall_seconds,
    )
    return pk, merged_pk, complete


def _emit(rendered: str, output: str | None) -> None:
    if output:
        Path(output).write_text(rendered, encoding="utf-8")
        print(f"Wrote {output}", file=sys.stderr)
    else:
        sys.stdout.write(rendered)


def _resolve(value: str, resolver, label: str) -> tuple[str, str]:
    """Accept a CURIE as-is, otherwise resolve a name through the SRI resolver."""
    if ":" in value:
        return value, ""
    matches = resolver(value)
    if not matches:
        raise SystemExit(f"Could not resolve '{value}' to a {label} CURIE.")
    curie, resolved = matches[0]
    print(f"Resolved '{value}' -> {curie} ({resolved})", file=sys.stderr)
    for other, other_label in matches[1:]:
        print(f"  other candidate: {other} ({other_label})", file=sys.stderr)
    return curie, resolved


def run_regulation_mode(args: argparse.Namespace, entry: dict[str, Any] | None) -> int:
    """The UI's up/down-regulation templates: chemicals <-> gene, with a direction."""
    if args.regulates and args.regulated_by:
        raise SystemExit("Pass either --regulates (pin a gene) or --regulated-by (pin a chemical), not both.")

    if args.regulates:
        pinned_curie, pinned_label = _resolve(args.regulates, resolve_gene_name, "gene")
        query = build_regulation_query(gene_curie=pinned_curie, direction=args.direction)
        answer_key, pinned_key = "chem", "gene"
        question = f"chemicals that {args.direction} the activity/abundance of {pinned_label or pinned_curie}"
    else:
        pinned_curie, pinned_label = _resolve(args.regulated_by, resolve_chemical_name, "chemical")
        query = build_regulation_query(chemical_curie=pinned_curie, direction=args.direction)
        answer_key, pinned_key = "gene", "chem"
        question = f"genes whose activity/abundance is {args.direction} by {pinned_label or pinned_curie}"

    client = ARSClient(CI_ARS_URL if args.ci else args.ars_url)
    try:
        pk, merged_pk, complete = _run_query(client, args, query)
        message = (client.message(merged_pk).get("fields") or {}).get("data", {}).get("message") or {}
    finally:
        client.close()

    if args.save_raw:
        Path(args.save_raw).write_text(json.dumps(message, indent=2), encoding="utf-8")

    candidates = extract_candidates(message, answer_key=answer_key, pinned_key=pinned_key)
    if candidates:
        candidates = merge_equivalents(candidates, normalize_curies([c.node_id for c in candidates]))
    if entry is not None:
        # Chemicals check against curated treatments; genes against curated mechanism.
        index = curated_agents(entry) if answer_key == "chem" else curated_mechanism_index(entry)
        annotate_curated(candidates, *index)

    if args.asserted_only:
        candidates = [candidate for candidate in candidates if candidate.asserted]
    if args.new_only:
        candidates = [candidate for candidate in candidates if not candidate.curated_as]
    total = len(candidates)
    candidates = candidates[: args.top]
    if total > len(candidates):
        print(f"Showing top {len(candidates)} of {total} answers (raise with --top).", file=sys.stderr)

    ui_url = f"{CI_UI_URL if args.ci else ARS_UI_URL}?q={pk}"
    generated_at = datetime.now(UTC).isoformat()
    if args.format == "json":
        rendered = render_json(
            candidates,
            question=question,
            pinned=pinned_curie,
            direction=args.direction,
            ars_pk=pk,
            ui_url=ui_url,
            complete=complete,
            entry=args.entry,
            generated_at=generated_at,
        )
    elif args.format == "tsv":
        rendered = render_tsv(candidates)
    else:
        rendered = render_markdown(
            candidates,
            disease_curie=pinned_curie,
            disease_label=question,
            pk=pk,
            ui_url=ui_url,
            complete=complete,
            entry_path=args.entry,
            generated_at=generated_at,
            title="Translator regulation leads",
            pinned_role="Question",
        )
    _emit(rendered, args.output)
    return 0


def run_paths_mode(args: argparse.Namespace, entry: dict[str, Any] | None, disease: tuple[str, str]) -> int:
    """Pair mode: drug + disease -> ranked mechanism paths through an intermediate."""
    disease_curie, disease_label = disease
    drug_curie, drug_label = args.drug, ""
    if ":" not in drug_curie:
        matches = resolve_chemical_name(drug_curie)
        if not matches:
            raise SystemExit(f"Could not resolve '{args.drug}' to a chemical CURIE.")
        drug_curie, drug_label = matches[0]
        print(f"Resolved '{args.drug}' -> {drug_curie} ({drug_label})", file=sys.stderr)
        for curie, label in matches[1:]:
            print(f"  other candidate: {curie} ({label})", file=sys.stderr)

    hypothesis: dict[str, Any] | None = None
    if args.hypothesis:
        if entry is None:
            raise SystemExit("--hypothesis needs a disorder YAML path so the hypothesis id can be resolved.")
        hypothesis = find_hypothesis(entry, args.hypothesis)

    via_categories = VIA_CATEGORIES[args.via]
    if args.pathfinder:
        # Only the CI ARS answers Pathfinder today; prod ARAs reject the shape.
        args.ci = True
        query = build_pathfinder_query(
            drug_curie,
            disease_curie,
            intermediate_categories=None if args.via == "any" else via_categories,
        )
    else:
        query = build_path_query(disease_curie, drug_curie, via_categories=via_categories)
    started = datetime.now(UTC)
    client = ARSClient(CI_ARS_URL if args.ci else args.ars_url)
    try:
        pk, merged_pk, complete = _run_query(client, args, query)
        message = (client.message(merged_pk).get("fields") or {}).get("data", {}).get("message") or {}
    finally:
        client.close()
    ended = datetime.now(UTC)

    if args.save_raw:
        Path(args.save_raw).write_text(json.dumps(message, indent=2), encoding="utf-8")

    if args.pathfinder:
        paths = extract_pathfinder_paths(
            message,
            start=drug_curie,
            end=disease_curie,
            include_chemical_intermediates=args.include_chemical_intermediates,
        )
    else:
        paths = extract_paths(message, via_categories=via_categories)
    nodes = (message.get("knowledge_graph") or {}).get("nodes") or {}
    drug_label = drug_label or (nodes.get(drug_curie) or {}).get("name") or ""
    disease_label = disease_label or (nodes.get(disease_curie) or {}).get("name") or ""

    if paths:
        # A Pathfinder route has several intermediates; each is a cross-reference target.
        every_intermediate = sorted({curie for path in paths for curie in (path.intermediates or [path.node_id])})
        normalized = normalize_curies(every_intermediate)
        for path in paths:
            path.equivalent_ids = [
                equivalent
                for curie in (path.intermediates or [path.node_id])
                for equivalent in (normalized.get(curie) or {}).get("equivalents") or []
            ]

    curated_drug, curated_targets = None, []
    if entry is not None:
        annotate_paths(paths, *curated_mechanism_index(entry))
        agent_curie, agent_name = curated_agents(entry)
        drug_equivalents = list((normalize_curies([drug_curie]).get(drug_curie) or {}).get("equivalents") or [])
        curated_drug = _match_curated([drug_curie, *drug_equivalents], drug_label, agent_curie, agent_name)
        curated_targets = drug_target_mechanisms(entry, curated_drug)

    if args.new_only:
        paths = [path for path in paths if not path.curated_as]
    total = len(paths)
    paths = paths[: args.top]
    if total > len(paths):
        print(f"Showing top {len(paths)} of {total} paths (raise with --top).", file=sys.stderr)

    ui_url = f"{CI_UI_URL if args.ci else ARS_UI_URL}?q={pk}"
    meta = {
        "drug_curie": drug_curie,
        "drug_label": drug_label,
        "disease_curie": disease_curie,
        "disease_label": disease_label,
        "via": args.via,
        "pk": pk,
        "ui_url": ui_url,
        "complete": complete,
    }
    if args.format == "json":
        rendered = render_paths_json(paths, entry=args.entry, generated_at=ended.isoformat(), **meta)
    elif args.format == "tsv":
        rendered = render_paths_tsv(paths)
    else:
        rendered = render_paths_markdown(
            paths,
            entry_path=args.entry,
            curated_drug=curated_drug,
            curated_targets=curated_targets,
            generated_at=ended.isoformat(),
            **meta,
        )

    if hypothesis is not None:
        disorder_slug = Path(args.entry).stem
        report_path, citations_path = hypothesis_report_paths(
            Path(args.hypothesis_root), disorder_slug, str(hypothesis["hypothesis_group_id"])
        )
        references: list[str] = []
        for path in paths:
            for reference in path.publications:
                if reference not in references:
                    references.append(reference)
        write_hypothesis_report(
            report_path,
            citations_path,
            frontmatter=build_hypothesis_frontmatter(
                hypothesis=hypothesis,
                disease_name=str(entry.get("name") or disease_label) if entry else disease_label,
                query=query,
                ars_url=client.base_url,
                pk=pk,
                merged_pk=merged_pk,
                citation_count=len(references),
                started_at=started.isoformat(),
                ended_at=ended.isoformat(),
                duration_seconds=(ended - started).total_seconds(),
            ),
            body=rendered,
            references=references,
            query_description=(
                f"TRAPI two-hop lookup {drug_curie} -> {args.via} -> {disease_curie} "
                f"against the NCATS Translator ARS (pk {pk})."
            ),
        )
        print(f"Wrote {report_path} and {citations_path}", file=sys.stderr)
        return 0

    _emit(rendered, args.output)
    return 0


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not (args.entry or args.mondo or args.name or args.pk or args.regulates or args.regulated_by):
        raise SystemExit("Provide a disorder YAML path, --mondo, --name, --pk, --regulates, or --regulated-by.")

    entry: dict[str, Any] | None = None
    disease_curie = args.mondo
    disease_label = ""
    if args.entry:
        entry = _load_entry(args.entry)
        entry_curie, disease_label = _disease_from_entry(entry, args.entry)
        disease_curie = disease_curie or entry_curie
    if not disease_curie and args.name:
        matches = resolve_disease_name(args.name)
        if not matches:
            raise SystemExit(f"Could not resolve '{args.name}' to a disease CURIE.")
        disease_curie, disease_label = matches[0]
        print(f"Resolved '{args.name}' -> {disease_curie} ({disease_label})", file=sys.stderr)
        for curie, label in matches[1:]:
            print(f"  other candidate: {curie} ({label})", file=sys.stderr)
    if not disease_curie and not args.pk and not (args.regulates or args.regulated_by):
        raise SystemExit("No disease CURIE resolved; pass --mondo.")

    if args.regulates or args.regulated_by:
        return run_regulation_mode(args, entry)

    if args.drug or args.hypothesis:
        if not args.drug:
            raise SystemExit("--hypothesis is a path-mode option; pass --drug as well.")
        return run_paths_mode(args, entry, (disease_curie or "", disease_label))

    ui_base = CI_UI_URL if args.ci else ARS_UI_URL
    client = ARSClient(CI_ARS_URL if args.ci else args.ars_url)
    try:
        query = (
            None
            if args.pk
            else build_query(disease_curie, predicate=args.predicate, inferred=not args.no_inferred)
        )
        pk, merged_pk, complete = _run_query(client, args, query)
        message = (client.message(merged_pk).get("fields") or {}).get("data", {}).get("message") or {}
    finally:
        client.close()

    if args.save_raw:
        Path(args.save_raw).write_text(json.dumps(message, indent=2), encoding="utf-8")

    if not disease_curie:  # --pk without a disease: recover it from the replayed query graph
        query_nodes = (message.get("query_graph") or {}).get("nodes") or {}
        ids = (query_nodes.get("disease") or {}).get("ids") or []
        disease_curie = ids[0] if ids else "(unknown)"

    candidates = extract_candidates(message)
    if not disease_label:
        disease_label = ((message.get("knowledge_graph") or {}).get("nodes") or {}).get(disease_curie, {}).get(
            "name", ""
        )

    if candidates:
        candidates = merge_equivalents(candidates, normalize_curies([c.node_id for c in candidates]))
    if entry is not None:
        annotate_curated(candidates, *curated_agents(entry))

    if args.asserted_only:
        candidates = [candidate for candidate in candidates if candidate.asserted]
    if args.new_only:
        candidates = [candidate for candidate in candidates if not candidate.curated_as]
    total = len(candidates)
    candidates = candidates[: args.top]
    if total > len(candidates):
        print(f"Showing top {len(candidates)} of {total} candidates (raise with --top).", file=sys.stderr)

    generated_at = datetime.now(UTC).isoformat()
    ui_url = f"{ui_base}?q={pk}"
    if args.format == "json":
        rendered = render_json(
            candidates,
            disease=disease_curie,
            disease_label=disease_label,
            ars_pk=pk,
            ui_url=ui_url,
            complete=complete,
            entry=args.entry,
            generated_at=generated_at,
        )
    elif args.format == "tsv":
        rendered = render_tsv(candidates)
    else:
        rendered = render_markdown(
            candidates,
            disease_curie=disease_curie,
            disease_label=disease_label,
            pk=pk,
            ui_url=ui_url,
            complete=complete,
            entry_path=args.entry,
            generated_at=generated_at,
        )

    _emit(rendered, args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

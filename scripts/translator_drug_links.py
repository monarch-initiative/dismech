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

DEFAULT_TIMEOUT_SECONDS = 900
DEFAULT_POLL_SECONDS = 15
# A single stuck ARA can keep an otherwise-finished run in "Running" for many
# minutes, so stop once the agent statuses have not moved for this long.
DEFAULT_STALL_SECONDS = 180
DEFAULT_TOP = 25
MAX_PUBLICATIONS_PER_CANDIDATE = 8
MAX_TRIALS_PER_CANDIDATE = 5

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

    chem_id: str
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
        merged_pk = trace.get("merged_version") or merged_pk
        status = trace.get("status")
        if verbose:
            print(f"  [{status}] {summarize_trace(trace)}", file=sys.stderr)
        if status and status != "Running":
            if not merged_pk:
                raise SystemExit(f"ARS run {pk} finished with status {status} but produced no merged result set.")
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


def extract_candidates(message: dict[str, Any]) -> list[Candidate]:
    """Collapse TRAPI results into one Candidate per chemical, best score first.

    Only edges that directly connect the answer chemical to the queried disease
    contribute provenance; mechanism-path edges reached through support graphs
    describe *how* a prediction was made, not whether the drug treats the disease.
    """
    knowledge_graph = message.get("knowledge_graph") or {}
    nodes = knowledge_graph.get("nodes") or {}
    edges = knowledge_graph.get("edges") or {}

    by_chem: dict[str, Candidate] = {}
    for result in message.get("results") or []:
        chem_ids = _node_ids(result, "chem")
        disease_ids = _node_ids(result, "disease")
        if not chem_ids:
            continue
        primary = sorted(chem_ids)[0]
        candidate = by_chem.get(primary)
        if candidate is None:
            candidate = Candidate(chem_id=primary, name=(nodes.get(primary) or {}).get("name") or primary)
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


def annotate_curated(candidates: list[Candidate], by_curie: dict[str, str], by_name: dict[str, str]) -> None:
    """Mark candidates already present in the entry, by equivalent CURIE or by name."""
    for candidate in candidates:
        for curie in [candidate.chem_id, *candidate.equivalent_ids]:
            if curie in by_curie:
                candidate.curated_as = by_curie[curie]
                break
        else:
            match = by_name.get(candidate.name.strip().lower())
            if match:
                candidate.curated_as = match


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
        entry = normalized.get(candidate.chem_id) or {}
        key = entry.get("id") or candidate.chem_id
        candidate.equivalent_ids = list(entry.get("equivalents") or [])
        target = merged.get(key)
        if target is None:
            candidate.chem_id = key
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
) -> str:
    lines = [
        f"# Translator drug-link leads: {disease_label or disease_curie}",
        "",
        f"- Disease: `{disease_curie}`" + (f" ({disease_label})" if disease_label else ""),
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
            f"| {index} | {candidate.status} | {candidate.name} | `{candidate.chem_id}` | "
            f"{score} | {level} | {', '.join(evidence_bits)} | {sources} |"
        )

    lines += ["", "## Candidate detail", ""]
    for index, candidate in enumerate(candidates, start=1):
        lines.append(f"### {index}. {candidate.name} (`{candidate.chem_id}`) — {candidate.status}")
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
                    candidate.chem_id,
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
                "curie": candidate.chem_id,
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
    return parser.parse_args(argv)


def _load_entry(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def _disease_from_entry(entry: dict[str, Any], path: str) -> tuple[str, str]:
    term = (entry.get("disease_term") or {}).get("term") or {}
    curie = term.get("id")
    if not curie:
        raise SystemExit(f"{path} has no disease_term.term.id; pass --mondo explicitly.")
    return curie, term.get("label") or entry.get("name") or ""


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if not (args.entry or args.mondo or args.name or args.pk):
        raise SystemExit("Provide a disorder YAML path, --mondo, --name, or --pk.")

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
    if not disease_curie and not args.pk:
        raise SystemExit("No disease CURIE resolved; pass --mondo.")

    base_url = CI_ARS_URL if args.ci else args.ars_url
    ui_base = CI_UI_URL if args.ci else ARS_UI_URL
    client = ARSClient(base_url)
    try:
        if args.pk:
            pk = args.pk
            merged_pk, complete = poll_for_merged(
                client,
                pk,
                timeout_seconds=args.timeout,
                poll_seconds=args.poll_interval,
                stall_seconds=args.stall_seconds,
            )
        else:
            query = build_query(disease_curie, predicate=args.predicate, inferred=not args.no_inferred)
            pk = client.submit(query)
            print(f"Submitted {disease_curie} to {base_url} as pk {pk}", file=sys.stderr)
            merged_pk, complete = poll_for_merged(
                client,
                pk,
                timeout_seconds=args.timeout,
                poll_seconds=args.poll_interval,
                stall_seconds=args.stall_seconds,
            )
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
        candidates = merge_equivalents(candidates, normalize_curies([c.chem_id for c in candidates]))
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

    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
        print(f"Wrote {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

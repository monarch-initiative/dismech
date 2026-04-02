"""Compare G2P gene assertions against dismech disease coverage."""

from __future__ import annotations

import csv
import gzip
import io
import json
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any

import typer

from .compare_support import default_kb_dir as _default_kb_dir
from .compare_support import get_disease_term_id as _get_disease_term_id
from .compare_support import iter_disease_files as _iter_disease_files
from .compare_support import load_yaml_object as _load_disease_yaml
from .compare_support import normalize_hp_id as _normalize_hp_id

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_G2P_RELEASE_INDEX_URL = (
    "https://ftp.ebi.ac.uk/pub/databases/gene2phenotype/G2P_data_downloads/"
)
_RELEASE_DIR_RE = re.compile(r'href="(\d{4}_\d{2}_\d{2})/"')
_ALL_G2P_FILE_RE = re.compile(r'href="(allG2P_\d{4}-\d{2}-\d{2}\.csv\.gz)"')
_PMID_RE = re.compile(r"^PMID:(\d+)$")
_PARENTHETICAL_RE = re.compile(r"\(([^)]+)\)")

_MATCH_PRIORITY = {
    "causative": 0,
    "subtype_specific": 1,
    "secondary_genetic": 2,
    "pathophysiology_only": 3,
}
_DIRECT_MATCH_STRENGTHS = {"causative", "subtype_specific"}
_ROW_STATUS_PRIORITY = {
    "NO_DISMECH_MATCH": 0,
    "UNDERREPRESENTED_IN_DISMECH": 1,
    "SPLIT_ACROSS_DISMECH": 2,
    "EMBEDDED_NOT_ROOTED": 3,
    "ROOT_MATCH_PMID_GAP": 4,
    "ROOT_MATCH": 5,
}
_CURATION_PRIORITY_LABEL = {
    "NO_DISMECH_MATCH": "CRITICAL",
    "UNDERREPRESENTED_IN_DISMECH": "HIGH",
    "SPLIT_ACROSS_DISMECH": "HIGH",
    "EMBEDDED_NOT_ROOTED": "MEDIUM",
    "ROOT_MATCH_PMID_GAP": "MEDIUM",
    "ROOT_MATCH": "LOW",
}
_CURATION_PRIORITY_RANK = {
    "CRITICAL": 0,
    "HIGH": 1,
    "MEDIUM": 2,
    "LOW": 3,
}
_ROW_STATUS_COUNT_FIELDS = [
    ("ROOT_MATCH", "root_match_count"),
    ("ROOT_MATCH_PMID_GAP", "root_match_pmid_gap_count"),
    ("SPLIT_ACROSS_DISMECH", "split_across_dismech_count"),
    ("EMBEDDED_NOT_ROOTED", "embedded_not_rooted_count"),
    ("UNDERREPRESENTED_IN_DISMECH", "underrepresented_in_dismech_count"),
    ("NO_DISMECH_MATCH", "no_dismech_match_count"),
]

_TSV_COLUMNS = [
    "gene_symbol",
    "g2p_id",
    "g2p_disease_name",
    "g2p_disease_mondo",
    "g2p_confidence",
    "g2p_mechanism",
    "g2p_reviewed_pmid_count",
    "dismech_candidate_count",
    "dismech_direct_candidate_count",
    "best_dismech_match_class",
    "best_dismech_file",
    "best_dismech_disease_name",
    "best_dismech_disease_mondo",
    "best_match_reasons",
    "best_shared_hpo_count",
    "best_shared_section_reviewed_pmid_count",
    "best_shared_disease_reviewed_pmid_count",
    "related_direct_disorders",
    "related_direct_match_count",
    "row_status",
    "curation_priority",
    "curation_action",
    "curation_note",
]
_GENE_TSV_COLUMNS = [
    "gene_symbol",
    "g2p_row_count",
    "actionable_row_count",
    "highest_curation_priority",
    "worst_row_status",
    "primary_curation_action",
    "top_curation_note",
    "direct_dismech_match_count",
    "g2p_mondo_collision_count",
    "direct_section_pmid_overlap_count",
    "direct_section_pmid_missing_count",
    "root_match_count",
    "root_match_pmid_gap_count",
    "split_across_dismech_count",
    "embedded_not_rooted_count",
    "underrepresented_in_dismech_count",
    "no_dismech_match_count",
]

app = typer.Typer(help="Compare G2P gene assertions against dismech disease coverage.")

# ---------------------------------------------------------------------------
# G2P source loading
# ---------------------------------------------------------------------------


def _normalize_phrase(text: str | None) -> str:
    if not text:
        return ""
    normalized = text.casefold().replace("tumour", "tumor").replace("_", " ")
    normalized = re.sub(r"[^a-z0-9]+", " ", normalized)
    return " ".join(normalized.split())


def _g2p_name_forms(disease_name: str, gene_symbol: str) -> tuple[set[str], set[str]]:
    full = _normalize_phrase(disease_name)
    exact_forms = {full} if full else set()
    stripped_forms: set[str] = set()

    for part in _PARENTHETICAL_RE.findall(disease_name):
        alias = _normalize_phrase(part)
        if alias:
            exact_forms.add(alias)

    prefix = _normalize_phrase(f"{gene_symbol} related")
    if full.startswith(f"{prefix} "):
        stripped = full[len(prefix) + 1 :].strip()
        if stripped:
            stripped_forms.add(stripped)

    return exact_forms, stripped_forms


def _is_url(source: str) -> bool:
    return source.startswith("http://") or source.startswith("https://")


def _read_bytes(source: str) -> bytes:
    if _is_url(source):
        with urllib.request.urlopen(source) as response:
            return response.read()
    return Path(source).read_bytes()


def _resolve_latest_g2p_url() -> str:
    index_html = _read_bytes(_G2P_RELEASE_INDEX_URL).decode("utf-8", errors="replace")
    release_dirs = sorted(_RELEASE_DIR_RE.findall(index_html))
    if not release_dirs:
        raise ValueError("Could not resolve a latest G2P release directory")

    latest_dir = release_dirs[-1]
    release_url = f"{_G2P_RELEASE_INDEX_URL}{latest_dir}/"
    release_html = _read_bytes(release_url).decode("utf-8", errors="replace")
    match = _ALL_G2P_FILE_RE.search(release_html)
    if not match:
        raise ValueError(f"Could not find an allG2P export in {release_url}")

    return f"{release_url}{match.group(1)}"


def _read_text(source: str) -> str:
    raw = _read_bytes(source)
    if source.endswith(".gz"):
        raw = gzip.decompress(raw)
    return raw.decode("utf-8-sig")


def _split_semicolon_field(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split(";") if part.strip()]


def _iter_g2p_rows(source: str) -> list[dict[str, str]]:
    text = _read_text(source)
    reader = csv.DictReader(io.StringIO(text))
    return [dict(row) for row in reader]


def _summarize_g2p_row(row: dict[str, str]) -> dict[str, Any]:
    phenotypes = [
        normalized
        for item in _split_semicolon_field(row.get("phenotypes"))
        if (normalized := _normalize_hp_id(item))
    ]
    reviewed_pmids = _split_semicolon_field(row.get("publications"))
    return {
        "g2p_id": row.get("g2p id", ""),
        "gene_symbol": row.get("gene symbol", ""),
        "disease_name": row.get("disease name", ""),
        "disease_mondo": row.get("disease MONDO", ""),
        "allelic_requirement": row.get("allelic requirement", ""),
        "confidence": row.get("confidence", ""),
        "variant_consequence": row.get("variant consequence", ""),
        "variant_types": _split_semicolon_field(row.get("variant types")),
        "molecular_mechanism": row.get("molecular mechanism", ""),
        "molecular_mechanism_support": row.get("molecular mechanism support", ""),
        "molecular_mechanism_categorisation": row.get(
            "molecular mechanism categorisation", ""
        ),
        "molecular_mechanism_evidence": row.get("molecular mechanism evidence", ""),
        "phenotypes": phenotypes,
        "phenotype_count": len(phenotypes),
        "reviewed_pmids": reviewed_pmids,
        "reviewed_pmid_count": len(reviewed_pmids),
        "additional_mined_pmids": _split_semicolon_field(
            row.get("additional mined publications")
        ),
        "panel": _split_semicolon_field(row.get("panel")),
        "date_of_last_review": row.get("date of last review", ""),
        "review": row.get("review", ""),
    }


def load_g2p_index(
    source: str | None = None,
) -> tuple[str, dict[str, list[dict[str, Any]]]]:
    resolved_source = source or _resolve_latest_g2p_url()
    rows_by_gene: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in _iter_g2p_rows(resolved_source):
        gene_symbol = row.get("gene symbol")
        if gene_symbol:
            rows_by_gene[gene_symbol].append(_summarize_g2p_row(row))
    return resolved_source, dict(rows_by_gene)


def load_g2p_rows_for_gene(source: str, gene_symbol: str) -> list[dict[str, Any]]:
    _, rows_by_gene = load_g2p_index(source)
    return rows_by_gene.get(gene_symbol, [])


# ---------------------------------------------------------------------------
# dismech extraction
# ---------------------------------------------------------------------------


def _extract_pmids(obj: Any) -> set[str]:
    pmids: set[str] = set()
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == "reference" and isinstance(value, str):
                match = _PMID_RE.match(value)
                if match:
                    pmids.add(match.group(1))
            else:
                pmids.update(_extract_pmids(value))
    elif isinstance(obj, list):
        for item in obj:
            pmids.update(_extract_pmids(item))
    return pmids


def _descriptor_symbol(descriptor: dict[str, Any] | None) -> str | None:
    if not isinstance(descriptor, dict):
        return None
    preferred = descriptor.get("preferred_term")
    if preferred:
        return str(preferred)
    term = descriptor.get("term")
    if isinstance(term, dict) and term.get("label"):
        return str(term["label"])
    return None


def _pathophysiology_gene_symbols(node: dict[str, Any]) -> set[str]:
    symbols: set[str] = set()
    gene = node.get("gene")
    symbol = _descriptor_symbol(gene if isinstance(gene, dict) else None)
    if symbol:
        symbols.add(symbol)

    for item in node.get("genes") or []:
        if isinstance(item, dict):
            symbol = _descriptor_symbol(item)
            if symbol:
                symbols.add(symbol)

    return symbols


def _disorder_phenotype_ids(disorder: dict[str, Any]) -> list[str]:
    phenotype_ids: set[str] = set()
    for phenotype in disorder.get("phenotypes") or []:
        if not isinstance(phenotype, dict):
            continue
        phenotype_term = phenotype.get("phenotype_term")
        if not isinstance(phenotype_term, dict):
            continue
        raw_term = phenotype_term.get("term")
        if not isinstance(raw_term, dict):
            continue
        normalized = _normalize_hp_id(raw_term.get("id"))
        if normalized:
            phenotype_ids.add(normalized)
    return sorted(phenotype_ids)


def _classify_match_strength(
    genetic_matches: list[dict[str, Any]],
    pathophysiology_matches: list[dict[str, Any]],
) -> str:
    if genetic_matches:
        associations = [
            str(match.get("association", "")).casefold() for match in genetic_matches
        ]
        if any("causative" in association for association in associations):
            return "causative"
        if any(
            token in association
            for association in associations
            for token in ("subtype", "contiguous", "partner")
        ):
            return "subtype_specific"
        return "secondary_genetic"
    if pathophysiology_matches:
        return "pathophysiology_only"
    raise ValueError("At least one genetic or pathophysiology match is required")


def _match_reasons_for_row(
    row: dict[str, Any],
    disorder_name: str,
    disorder_mondo: str | None,
    gene_symbol: str,
) -> list[str]:
    reasons: list[str] = []
    row_mondo = row.get("disease_mondo")
    if row_mondo and disorder_mondo and row_mondo == disorder_mondo:
        reasons.append("exact_mondo")

    disorder_norm = _normalize_phrase(disorder_name)
    exact_forms, stripped_forms = _g2p_name_forms(row["disease_name"], gene_symbol)
    if disorder_norm and disorder_norm in exact_forms:
        reasons.append("name_or_parenthetical_alias")
    elif disorder_norm and disorder_norm in stripped_forms:
        reasons.append("gene_related_prefix_stripped")

    return reasons


def build_dismech_gene_index(kb_dir: Path) -> dict[str, list[dict[str, Any]]]:
    """Build a reusable dismech disease-match index keyed by gene symbol."""
    matches_by_gene: dict[str, list[dict[str, Any]]] = defaultdict(list)

    for path in _iter_disease_files(kb_dir):
        disorder = _load_disease_yaml(path)
        disorder_name = str(disorder.get("name", path.stem))
        disorder_mondo = _get_disease_term_id(disorder)
        disorder_phenotypes = _disorder_phenotype_ids(disorder)
        all_pmids = sorted(_extract_pmids(disorder))

        genetic_matches_by_gene: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for entry in disorder.get("genetic") or []:
            if not isinstance(entry, dict):
                continue
            descriptor = entry.get("gene_term")
            symbol = _descriptor_symbol(
                descriptor if isinstance(descriptor, dict) else None
            )
            symbol = symbol or str(entry.get("name", ""))
            if not symbol:
                continue
            genetic_matches_by_gene[symbol].append(
                {
                    "name": entry.get("name", symbol),
                    "association": entry.get("association", ""),
                    "subtype": entry.get("subtype", ""),
                    "pmids": sorted(_extract_pmids(entry)),
                }
            )

        pathophysiology_matches_by_gene: dict[str, list[dict[str, Any]]] = defaultdict(
            list
        )
        for node in disorder.get("pathophysiology") or []:
            if not isinstance(node, dict):
                continue
            symbols = _pathophysiology_gene_symbols(node)
            if not symbols:
                continue
            match = {
                "name": node.get("name", ""),
                "pmids": sorted(_extract_pmids(node)),
            }
            for symbol in symbols:
                pathophysiology_matches_by_gene[symbol].append(dict(match))

        gene_symbols = sorted(
            set(genetic_matches_by_gene.keys())
            | set(pathophysiology_matches_by_gene.keys())
        )
        if not gene_symbols:
            continue

        for gene_symbol in gene_symbols:
            genetic_matches = [
                dict(match) for match in genetic_matches_by_gene.get(gene_symbol, [])
            ]
            pathophysiology_matches = [
                dict(match)
                for match in pathophysiology_matches_by_gene.get(gene_symbol, [])
            ]
            matched_section_pmids = sorted(
                {
                    pmid
                    for match in genetic_matches + pathophysiology_matches
                    for pmid in match["pmids"]
                }
            )
            matches_by_gene[gene_symbol].append(
                {
                    "file": path.name,
                    "path": str(path),
                    "disorder_name": disorder_name,
                    "disease_mondo": disorder_mondo,
                    "match_strength": _classify_match_strength(
                        genetic_matches, pathophysiology_matches
                    ),
                    "genetic_matches": genetic_matches,
                    "pathophysiology_matches": pathophysiology_matches,
                    "top_level_phenotype_ids": disorder_phenotypes,
                    "matched_section_pmids": matched_section_pmids,
                    "all_pmids": list(all_pmids),
                }
            )

    for gene_symbol, matches in matches_by_gene.items():
        matches.sort(
            key=lambda match: (
                _MATCH_PRIORITY[match["match_strength"]],
                match["disorder_name"].casefold(),
            )
        )

    return dict(matches_by_gene)


def extract_dismech_gene_matches(
    kb_dir: Path,
    gene_symbol: str,
    g2p_rows: list[dict[str, Any]],
    *,
    dismech_matches_by_gene: dict[str, list[dict[str, Any]]] | None = None,
) -> list[dict[str, Any]]:
    match_templates = (
        dismech_matches_by_gene.get(gene_symbol, [])
        if dismech_matches_by_gene
        else None
    )
    if match_templates is None:
        dismech_matches_by_gene = build_dismech_gene_index(kb_dir)
        match_templates = dismech_matches_by_gene.get(gene_symbol, [])

    matches: list[dict[str, Any]] = []
    for template in match_templates:
        disorder_phenotypes = template["top_level_phenotype_ids"]
        linked_rows = []
        for row in g2p_rows:
            reasons = _match_reasons_for_row(
                row,
                disorder_name=template["disorder_name"],
                disorder_mondo=template["disease_mondo"],
                gene_symbol=gene_symbol,
            )
            if not reasons:
                continue
            shared_phenotypes = sorted(
                set(row["phenotypes"]) & set(disorder_phenotypes)
            )
            linked_rows.append(
                {
                    "g2p_id": row["g2p_id"],
                    "disease_name": row["disease_name"],
                    "match_reasons": reasons,
                    "shared_phenotype_count": len(shared_phenotypes),
                    "shared_phenotype_ids": shared_phenotypes,
                }
            )

        match = {
            **template,
            "genetic_matches": [dict(item) for item in template["genetic_matches"]],
            "pathophysiology_matches": [
                dict(item) for item in template["pathophysiology_matches"]
            ],
            "top_level_phenotype_ids": list(template["top_level_phenotype_ids"]),
            "matched_section_pmids": list(template["matched_section_pmids"]),
            "all_pmids": list(template["all_pmids"]),
            "linked_g2p_rows": linked_rows,
        }
        matches.append(match)

    return matches


# ---------------------------------------------------------------------------
# Comparison logic
# ---------------------------------------------------------------------------


def _direct_matches(dismech_matches: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        match
        for match in dismech_matches
        if match["match_strength"] in _DIRECT_MATCH_STRENGTHS
    ]


def _shared_pmid_values(
    row: dict[str, Any],
    dismech_match: dict[str, Any],
) -> tuple[list[str], list[str]]:
    reviewed_pmids = set(row["reviewed_pmids"])
    shared_sections = sorted(
        reviewed_pmids & set(dismech_match["matched_section_pmids"])
    )
    shared_disease = sorted(reviewed_pmids & set(dismech_match["all_pmids"]))
    return shared_sections, shared_disease


def _related_direct_matches_for_row(
    row: dict[str, Any],
    direct_matches: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    related = []
    row_phenotypes = set(row["phenotypes"])

    for match in direct_matches:
        shared_phenotypes = sorted(
            row_phenotypes & set(match["top_level_phenotype_ids"])
        )
        shared_sections, shared_disease = _shared_pmid_values(row, match)
        if not shared_phenotypes and not shared_sections and not shared_disease:
            continue
        related.append(
            {
                "disorder_name": match["disorder_name"],
                "file": match["file"],
                "match_strength": match["match_strength"],
                "shared_phenotype_count": len(shared_phenotypes),
                "shared_phenotype_ids": shared_phenotypes,
                "shared_reviewed_pmids_with_sections": shared_sections,
                "shared_reviewed_pmids_with_disease": shared_disease,
            }
        )

    related.sort(
        key=lambda match: (
            _MATCH_PRIORITY[match["match_strength"]],
            -match["shared_phenotype_count"],
            -len(match["shared_reviewed_pmids_with_sections"]),
            match["disorder_name"].casefold(),
        )
    )
    return related


def _classify_row_status(
    row: dict[str, Any],
    dismech_matches: list[dict[str, Any]],
) -> str:
    direct_candidates = [
        candidate
        for candidate in row["dismech_candidates"]
        if candidate["match_strength"] in _DIRECT_MATCH_STRENGTHS
    ]
    if direct_candidates:
        if direct_candidates[0]["shared_reviewed_pmids_with_sections"]:
            return "ROOT_MATCH"
        return "ROOT_MATCH_PMID_GAP"

    related_direct_matches = row["related_direct_matches"]
    if len(related_direct_matches) > 1:
        return "SPLIT_ACROSS_DISMECH"
    if len(related_direct_matches) == 1:
        return "EMBEDDED_NOT_ROOTED"

    direct_gene_matches = _direct_matches(dismech_matches)
    if len(direct_gene_matches) > 1:
        return "SPLIT_ACROSS_DISMECH"
    if len(direct_gene_matches) == 1:
        return "UNDERREPRESENTED_IN_DISMECH"
    if dismech_matches:
        return "EMBEDDED_NOT_ROOTED"
    return "NO_DISMECH_MATCH"


def _row_curation_action(row: dict[str, Any]) -> tuple[str, str, str]:
    row_status = row["row_status"]
    priority = _CURATION_PRIORITY_LABEL[row_status]

    if row_status == "ROOT_MATCH":
        best_candidate = row["dismech_candidates"][0]
        return (
            priority,
            "KEEP_EXISTING_ROOT",
            f"{best_candidate['file']} already provides a usable direct disease root.",
        )

    if row_status == "ROOT_MATCH_PMID_GAP":
        best_candidate = row["dismech_candidates"][0]
        missing_pmids = sorted(
            set(row["reviewed_pmids"])
            - set(best_candidate["shared_reviewed_pmids_with_sections"])
        )
        return (
            priority,
            "BACKFILL_G2P_PMIDS_TO_MATCHED_ROOT",
            f"Add {len(missing_pmids)} reviewed G2P PMIDs to {best_candidate['file']}.",
        )

    if row_status == "SPLIT_ACROSS_DISMECH":
        disorders = ", ".join(
            match["disorder_name"] for match in row["related_direct_matches"][:3]
        )
        return (
            priority,
            "RECONCILE_SPECTRUM_ROW_ACROSS_MULTIPLE_ROOTS",
            f"Map the row against multiple direct roots: {disorders}.",
        )

    if row_status == "EMBEDDED_NOT_ROOTED":
        if row["related_direct_matches"]:
            best_related = row["related_direct_matches"][0]
            return (
                priority,
                "DECIDE_IF_EMBEDDED_CONCEPT_NEEDS_ROOT",
                f"Concept is currently embedded under {best_related['file']} rather than rooted directly.",
            )
        return (
            priority,
            "REVIEW_NON_ROOT_GENE_MENTION",
            "Gene appears only in non-root mechanistic or secondary contexts.",
        )

    if row_status == "UNDERREPRESENTED_IN_DISMECH":
        return (
            priority,
            "ADD_MISSING_DISEASE_ROOT",
            "dismech has some direct roots for the gene, but this disease row is still missing.",
        )

    return (
        priority,
        "ADD_FIRST_GENE_DISEASE_ANCHOR",
        "No dismech disease anchor currently represents this G2P row.",
    )


def build_comparison_table(
    gene_symbol: str,
    g2p_rows: list[dict[str, Any]],
    dismech_matches: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    table: list[dict[str, Any]] = []

    for row in g2p_rows:
        best_candidate = (
            row["dismech_candidates"][0] if row["dismech_candidates"] else None
        )
        direct_candidate_count = sum(
            1
            for candidate in row["dismech_candidates"]
            if candidate["match_strength"] in _DIRECT_MATCH_STRENGTHS
        )
        table.append(
            {
                "gene_symbol": gene_symbol,
                "g2p_id": row["g2p_id"],
                "g2p_disease_name": row["disease_name"],
                "g2p_disease_mondo": row["disease_mondo"],
                "g2p_confidence": row["confidence"],
                "g2p_mechanism": row["molecular_mechanism"],
                "g2p_reviewed_pmid_count": row["reviewed_pmid_count"],
                "dismech_candidate_count": len(row["dismech_candidates"]),
                "dismech_direct_candidate_count": direct_candidate_count,
                "best_dismech_match_class": (
                    best_candidate["match_strength"] if best_candidate else ""
                ),
                "best_dismech_file": best_candidate["file"] if best_candidate else "",
                "best_dismech_disease_name": (
                    best_candidate["disorder_name"] if best_candidate else ""
                ),
                "best_dismech_disease_mondo": (
                    best_candidate["disease_mondo"] if best_candidate else ""
                ),
                "best_match_reasons": (
                    ";".join(best_candidate["match_reasons"]) if best_candidate else ""
                ),
                "best_shared_hpo_count": (
                    best_candidate["shared_phenotype_count"] if best_candidate else 0
                ),
                "best_shared_section_reviewed_pmid_count": (
                    len(best_candidate["shared_reviewed_pmids_with_sections"])
                    if best_candidate
                    else 0
                ),
                "best_shared_disease_reviewed_pmid_count": (
                    len(best_candidate["shared_reviewed_pmids_with_disease"])
                    if best_candidate
                    else 0
                ),
                "related_direct_disorders": ";".join(
                    match["disorder_name"] for match in row["related_direct_matches"]
                ),
                "related_direct_match_count": len(row["related_direct_matches"]),
                "row_status": row["row_status"],
                "curation_priority": row["curation_priority"],
                "curation_action": row["curation_action"],
                "curation_note": row["curation_note"],
            }
        )

    table.sort(
        key=lambda item: (
            _ROW_STATUS_PRIORITY[item["row_status"]],
            item["g2p_disease_name"].casefold(),
            item["g2p_id"],
        )
    )
    return table


def compute_comparison_summary(
    gene_symbol: str,
    g2p_source: str,
    g2p_rows: list[dict[str, Any]],
    dismech_matches: list[dict[str, Any]],
    mondo_collisions: list[dict[str, Any]],
    publication_coverage: dict[str, Any],
) -> dict[str, Any]:
    mapped_rows = sum(1 for row in g2p_rows if row["dismech_candidates"])
    actionable_rows = sum(1 for row in g2p_rows if row["row_status"] != "ROOT_MATCH")
    row_status_counts: dict[str, int] = {}
    for row in g2p_rows:
        row_status = row["row_status"]
        row_status_counts[row_status] = row_status_counts.get(row_status, 0) + 1
    row_status_counts = dict(sorted(row_status_counts.items()))

    if g2p_rows:
        top_row = min(
            g2p_rows,
            key=lambda row: (
                _ROW_STATUS_PRIORITY[row["row_status"]],
                row["disease_name"].casefold(),
                row["g2p_id"],
            ),
        )
        highest_curation_priority = top_row["curation_priority"]
        worst_row_status = top_row["row_status"]
        primary_curation_action = top_row["curation_action"]
        top_curation_note = top_row["curation_note"]
    else:
        highest_curation_priority = "LOW"
        worst_row_status = "ROOT_MATCH"
        primary_curation_action = "NO_G2P_ROWS"
        top_curation_note = "Gene does not appear in the resolved G2P source."

    direct_coverage = publication_coverage["direct_dismech_matched_sections"]
    summary = {
        "gene_symbol": gene_symbol,
        "g2p_source": g2p_source,
        "g2p_row_count": len(g2p_rows),
        "mapped_row_count": mapped_rows,
        "unmapped_row_count": len(g2p_rows) - mapped_rows,
        "actionable_row_count": actionable_rows,
        "dismech_match_count": len(dismech_matches),
        "direct_dismech_match_count": len(_direct_matches(dismech_matches)),
        "g2p_mondo_collision_count": len(mondo_collisions),
        "direct_section_pmid_overlap_count": direct_coverage["overlap_count"],
        "direct_section_pmid_missing_count": direct_coverage[
            "missing_from_dismech_count"
        ],
        "highest_curation_priority": highest_curation_priority,
        "worst_row_status": worst_row_status,
        "primary_curation_action": primary_curation_action,
        "top_curation_note": top_curation_note,
        "row_status_counts": row_status_counts,
    }
    for status, field_name in _ROW_STATUS_COUNT_FIELDS:
        summary[field_name] = row_status_counts.get(status, 0)
    return summary


def compare_gene(
    gene_symbol: str,
    *,
    kb_dir: Path = _default_kb_dir(),
    g2p_source: str | None = None,
    g2p_rows_by_gene: dict[str, list[dict[str, Any]]] | None = None,
    resolved_g2p_source: str | None = None,
    dismech_matches_by_gene: dict[str, list[dict[str, Any]]] | None = None,
) -> dict[str, Any]:
    if g2p_rows_by_gene is None:
        source, rows_by_gene = load_g2p_index(g2p_source)
    else:
        source = resolved_g2p_source or g2p_source or "<preloaded>"
        rows_by_gene = g2p_rows_by_gene

    g2p_rows = [dict(row) for row in rows_by_gene.get(gene_symbol, [])]
    dismech_matches = extract_dismech_gene_matches(
        kb_dir,
        gene_symbol,
        g2p_rows,
        dismech_matches_by_gene=dismech_matches_by_gene,
    )

    row_candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for disorder in dismech_matches:
        for linked_row in disorder["linked_g2p_rows"]:
            row = next(row for row in g2p_rows if row["g2p_id"] == linked_row["g2p_id"])
            shared_sections, shared_disease = _shared_pmid_values(row, disorder)
            row_candidates[linked_row["g2p_id"]].append(
                {
                    "disorder_name": disorder["disorder_name"],
                    "file": disorder["file"],
                    "disease_mondo": disorder["disease_mondo"],
                    "match_strength": disorder["match_strength"],
                    "match_reasons": linked_row["match_reasons"],
                    "shared_phenotype_count": linked_row["shared_phenotype_count"],
                    "shared_phenotype_ids": linked_row["shared_phenotype_ids"],
                    "shared_reviewed_pmids_with_sections": shared_sections,
                    "shared_reviewed_pmids_with_disease": shared_disease,
                }
            )

    for row in g2p_rows:
        row["dismech_candidates"] = sorted(
            row_candidates.get(row["g2p_id"], []),
            key=lambda candidate: (
                _MATCH_PRIORITY[candidate["match_strength"]],
                candidate["disorder_name"].casefold(),
            ),
        )
        row["related_direct_matches"] = _related_direct_matches_for_row(
            row, _direct_matches(dismech_matches)
        )
        row["row_status"] = _classify_row_status(row, dismech_matches)
        (
            row["curation_priority"],
            row["curation_action"],
            row["curation_note"],
        ) = _row_curation_action(row)

    g2p_rows_by_mondo: dict[str, set[str]] = defaultdict(set)
    for row in g2p_rows:
        if row["disease_mondo"]:
            g2p_rows_by_mondo[row["disease_mondo"]].add(row["disease_name"])

    mondo_collisions = [
        {
            "disease_mondo": mondo,
            "disease_names": sorted(names),
        }
        for mondo, names in sorted(g2p_rows_by_mondo.items())
        if len(names) > 1
    ]

    def _union_pmids(items: list[dict[str, Any]], key: str) -> list[str]:
        return sorted({pmid for item in items for pmid in item.get(key, [])})

    direct_matches = _direct_matches(dismech_matches)
    g2p_reviewed_pmids = sorted(
        {pmid for row in g2p_rows for pmid in row["reviewed_pmids"]}
    )
    all_dismech_section_pmids = _union_pmids(dismech_matches, "matched_section_pmids")
    all_dismech_disease_pmids = _union_pmids(dismech_matches, "all_pmids")
    direct_dismech_section_pmids = _union_pmids(direct_matches, "matched_section_pmids")
    direct_dismech_disease_pmids = _union_pmids(direct_matches, "all_pmids")

    def _coverage_summary(dismech_pmids: list[str]) -> dict[str, Any]:
        overlap = sorted(set(g2p_reviewed_pmids) & set(dismech_pmids))
        missing = sorted(set(g2p_reviewed_pmids) - set(dismech_pmids))
        extra = sorted(set(dismech_pmids) - set(g2p_reviewed_pmids))
        return {
            "g2p_reviewed_pmid_count": len(g2p_reviewed_pmids),
            "dismech_pmid_count": len(dismech_pmids),
            "overlap_count": len(overlap),
            "missing_from_dismech_count": len(missing),
            "extra_in_dismech_count": len(extra),
            "overlap_pmids": overlap,
            "missing_from_dismech_pmids": missing,
            "extra_in_dismech_pmids": extra,
        }

    publication_coverage = {
        "all_dismech_matched_sections": _coverage_summary(all_dismech_section_pmids),
        "all_dismech_matched_diseases": _coverage_summary(all_dismech_disease_pmids),
        "direct_dismech_matched_sections": _coverage_summary(
            direct_dismech_section_pmids
        ),
        "direct_dismech_matched_diseases": _coverage_summary(
            direct_dismech_disease_pmids
        ),
    }
    comparison_table = build_comparison_table(gene_symbol, g2p_rows, dismech_matches)
    summary = compute_comparison_summary(
        gene_symbol,
        source,
        g2p_rows,
        dismech_matches,
        mondo_collisions,
        publication_coverage,
    )

    return {
        "gene_symbol": gene_symbol,
        "g2p_source": source,
        "g2p_row_count": len(g2p_rows),
        "g2p_rows": g2p_rows,
        "g2p_mondo_collisions": mondo_collisions,
        "dismech_match_count": len(dismech_matches),
        "dismech_matches": dismech_matches,
        "direct_dismech_match_count": len(direct_matches),
        "direct_dismech_matches": [
            {
                "file": match["file"],
                "disorder_name": match["disorder_name"],
                "disease_mondo": match["disease_mondo"],
                "match_strength": match["match_strength"],
            }
            for match in direct_matches
        ],
        "publication_coverage": publication_coverage,
        "comparison_table": comparison_table,
        "summary": summary,
    }


def run_comparison(
    gene_symbol: str,
    *,
    kb_dir: Path = _default_kb_dir(),
    g2p_source: str | None = None,
    g2p_rows_by_gene: dict[str, list[dict[str, Any]]] | None = None,
    resolved_g2p_source: str | None = None,
) -> tuple[list[dict[str, Any]], dict[str, Any], str]:
    """Run the G2P-vs-dismech comparison pipeline for one gene."""
    report = compare_gene(
        gene_symbol,
        kb_dir=kb_dir,
        g2p_source=g2p_source,
        g2p_rows_by_gene=g2p_rows_by_gene,
        resolved_g2p_source=resolved_g2p_source,
    )
    return report["comparison_table"], report["summary"], report["gene_symbol"]


def build_release_row_table(reports: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows = [row for report in reports for row in report["comparison_table"]]
    rows.sort(
        key=lambda row: (
            _ROW_STATUS_PRIORITY[row["row_status"]],
            row["gene_symbol"].casefold(),
            row["g2p_disease_name"].casefold(),
            row["g2p_id"],
        )
    )
    return rows


def run_release_comparison(
    *,
    gene_symbols: list[str] | None = None,
    kb_dir: Path = _default_kb_dir(),
    g2p_source: str | None = None,
    all_genes: bool = False,
    actionable_only: bool = False,
) -> dict[str, Any]:
    """Run the G2P-vs-dismech comparison pipeline for a gene set or full release."""
    resolved_source, rows_by_gene = load_g2p_index(g2p_source)
    if all_genes:
        selected_gene_symbols = sorted(rows_by_gene)
    elif gene_symbols:
        selected_gene_symbols = gene_symbols
    else:
        raise ValueError("Provide gene symbols or set all_genes=True")

    dismech_matches_by_gene = build_dismech_gene_index(kb_dir)
    reports = [
        compare_gene(
            gene_symbol,
            kb_dir=kb_dir,
            g2p_source=resolved_source,
            g2p_rows_by_gene=rows_by_gene,
            resolved_g2p_source=resolved_source,
            dismech_matches_by_gene=dismech_matches_by_gene,
        )
        for gene_symbol in selected_gene_symbols
    ]
    gene_summaries = [report["summary"] for report in reports]
    gene_summaries.sort(
        key=lambda item: (
            _ROW_STATUS_PRIORITY[item["worst_row_status"]],
            -item["actionable_row_count"],
            -item["g2p_row_count"],
            item["gene_symbol"].casefold(),
        )
    )
    overview = compute_release_overview(reports, gene_summaries)
    row_table = build_release_row_table(reports)
    if actionable_only:
        row_table = [row for row in row_table if row["row_status"] != "ROOT_MATCH"]

    return {
        "g2p_source": resolved_source,
        "reports": reports,
        "overview": overview,
        "gene_summaries": gene_summaries,
        "row_table": row_table,
    }


def compute_release_overview(
    reports: list[dict[str, Any]],
    gene_summaries: list[dict[str, Any]],
) -> dict[str, Any]:
    row_status_counts: dict[str, int] = {}
    genes_by_highest_priority: dict[str, int] = {}
    genes_by_primary_action: dict[str, int] = {}

    total_rows = sum(report["g2p_row_count"] for report in reports)
    total_actionable_rows = sum(
        summary["actionable_row_count"] for summary in gene_summaries
    )
    genes_with_direct_matches = sum(
        1 for summary in gene_summaries if summary["direct_dismech_match_count"] > 0
    )
    genes_with_mondo_collisions = sum(
        1 for summary in gene_summaries if summary["g2p_mondo_collision_count"] > 0
    )

    for summary in gene_summaries:
        priority = summary["highest_curation_priority"]
        genes_by_highest_priority[priority] = (
            genes_by_highest_priority.get(priority, 0) + 1
        )
        action = summary["primary_curation_action"]
        genes_by_primary_action[action] = genes_by_primary_action.get(action, 0) + 1
        for status, count in summary["row_status_counts"].items():
            row_status_counts[status] = row_status_counts.get(status, 0) + count

    return {
        "total_genes": len(gene_summaries),
        "total_rows": total_rows,
        "total_actionable_rows": total_actionable_rows,
        "genes_with_direct_matches": genes_with_direct_matches,
        "genes_with_mondo_collisions": genes_with_mondo_collisions,
        "row_status_counts": dict(sorted(row_status_counts.items())),
        "genes_by_highest_priority": dict(
            sorted(
                genes_by_highest_priority.items(),
                key=lambda item: (_CURATION_PRIORITY_RANK[item[0]], item[0]),
            )
        ),
        "genes_by_primary_action": dict(
            sorted(
                genes_by_primary_action.items(),
                key=lambda item: (-item[1], item[0]),
            )
        ),
    }


def survey_genes(
    gene_symbols: list[str],
    *,
    kb_dir: Path = _default_kb_dir(),
    g2p_source: str | None = None,
) -> list[dict[str, Any]]:
    release_report = run_release_comparison(
        gene_symbols=gene_symbols,
        kb_dir=kb_dir,
        g2p_source=g2p_source,
    )
    return release_report["gene_summaries"]


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------


def _write_tsv(rows: list[dict[str, Any]], file=None) -> None:
    out = file or sys.stdout
    out.write("\t".join(_TSV_COLUMNS) + "\n")
    for row in rows:
        out.write("\t".join(str(row.get(column, "")) for column in _TSV_COLUMNS) + "\n")


def _write_json(report: dict[str, Any], file=None) -> None:
    out = file or sys.stdout
    json.dump(report, out, indent=2)
    out.write("\n")


def _write_gene_tsv(rows: list[dict[str, Any]], file=None) -> None:
    out = file or sys.stdout
    out.write("\t".join(_GENE_TSV_COLUMNS) + "\n")
    for row in rows:
        out.write(
            "\t".join(str(row.get(column, "")) for column in _GENE_TSV_COLUMNS) + "\n"
        )


def _write_summary(report: dict[str, Any], file=None) -> None:
    out = file or typer.get_text_stream("stdout")
    out.write(f"Gene: {report['gene_symbol']}\n")
    out.write(f"G2P source: {report['g2p_source']}\n")
    out.write(f"G2P rows: {report['g2p_row_count']}\n")
    for row in report["g2p_rows"]:
        out.write(
            f"- {row['g2p_id']}: {row['disease_name']} | MONDO {row['disease_mondo'] or '-'}"
            f" | confidence={row['confidence'] or '-'}"
            f" | reviewed_pmids={row['reviewed_pmid_count']}"
            f" | phenotypes={row['phenotype_count']}"
            f" | status={row['row_status']}\n"
        )
        if row["dismech_candidates"]:
            candidate_text = "; ".join(
                (
                    f"{candidate['disorder_name']} "
                    f"[{candidate['match_strength']}; {','.join(candidate['match_reasons'])}; "
                    f"shared_hpo={candidate['shared_phenotype_count']}; "
                    f"shared_section_pmids={len(candidate['shared_reviewed_pmids_with_sections'])}]"
                )
                for candidate in row["dismech_candidates"]
            )
            out.write(f"  dismech candidates: {candidate_text}\n")
        else:
            out.write("  dismech candidates: none\n")
        if row["related_direct_matches"]:
            related_text = "; ".join(
                (
                    f"{match['disorder_name']} "
                    f"[shared_hpo={match['shared_phenotype_count']}; "
                    f"shared_section_pmids={len(match['shared_reviewed_pmids_with_sections'])}]"
                )
                for match in row["related_direct_matches"]
            )
            out.write(f"  related direct matches: {related_text}\n")

    if report["g2p_mondo_collisions"]:
        out.write("G2P MONDO collisions:\n")
        for collision in report["g2p_mondo_collisions"]:
            names = "; ".join(collision["disease_names"])
            out.write(f"- {collision['disease_mondo']}: {names}\n")

    out.write(f"dismech gene matches: {report['dismech_match_count']}\n")
    for match in report["dismech_matches"]:
        association_text = (
            ", ".join(
                entry["association"] or "unspecified"
                for entry in match["genetic_matches"]
            )
            or "-"
        )
        out.write(
            f"- {match['disorder_name']} ({match['file']})"
            f" | strength={match['match_strength']}"
            f" | MONDO {match['disease_mondo'] or '-'}"
            f" | genetic_association={association_text}"
            f" | matched_section_pmids={len(match['matched_section_pmids'])}"
            f" | disease_pmids={len(match['all_pmids'])}\n"
        )

    out.write("Row status counts:\n")
    for status, count in sorted(report["summary"]["row_status_counts"].items()):
        out.write(f"- {status}: {count}\n")

    for label, coverage in report["publication_coverage"].items():
        out.write(
            f"{label}: g2p={coverage['g2p_reviewed_pmid_count']}, "
            f"dismech={coverage['dismech_pmid_count']}, "
            f"overlap={coverage['overlap_count']}, "
            f"missing_from_dismech={coverage['missing_from_dismech_count']}\n"
        )


def _write_batch_summary(
    overview: dict[str, Any],
    summaries: list[dict[str, Any]],
    *,
    g2p_source: str,
    top: int = 25,
    file=None,
) -> None:
    out = file or typer.get_text_stream("stdout")
    out.write("# G2P All-Gene Audit Summary\n\n")
    out.write(f"- G2P source: `{g2p_source}`\n")
    out.write(f"- Genes audited: {overview['total_genes']}\n")
    out.write(f"- G2P rows audited: {overview['total_rows']}\n")
    out.write(f"- Actionable rows: {overview['total_actionable_rows']}\n")
    out.write(
        f"- Genes with direct dismech matches: {overview['genes_with_direct_matches']}\n"
    )
    out.write(
        f"- Genes with G2P MONDO collisions: {overview['genes_with_mondo_collisions']}\n\n"
    )

    out.write("## Aggregate Row Status Counts\n\n")
    for status, count in overview["row_status_counts"].items():
        out.write(f"- {status}: {count}\n")

    out.write("\n## Genes By Highest Curation Priority\n\n")
    for priority, count in overview["genes_by_highest_priority"].items():
        out.write(f"- {priority}: {count}\n")

    out.write("\n## Most Common Primary Actions\n\n")
    for action, count in list(overview["genes_by_primary_action"].items())[:10]:
        out.write(f"- {action}: {count}\n")

    sections = [
        ("CRITICAL", "Critical Genes: new dismech anchors needed"),
        ("HIGH", "High-Priority Genes: split or underrepresented coverage"),
        ("MEDIUM", "Medium-Priority Genes: embedded concepts or PMID backfill"),
        ("LOW", "Low-Priority Genes: existing roots already usable"),
    ]
    for priority, heading in sections:
        priority_summaries = [
            summary
            for summary in summaries
            if summary["highest_curation_priority"] == priority
        ][:top]
        if not priority_summaries:
            continue

        out.write(f"\n## {heading} (top {min(top, len(priority_summaries))})\n\n")
        out.write(
            "| Gene | Priority | Actionable rows | Worst status | Primary action | Note |\n"
        )
        out.write("| --- | --- | ---: | --- | --- | --- |\n")
        for summary in priority_summaries:
            note = summary["top_curation_note"].replace("|", "/")
            out.write(
                f"| {summary['gene_symbol']} | {summary['highest_curation_priority']} | "
                f"{summary['actionable_row_count']} | {summary['worst_row_status']} | "
                f"{summary['primary_curation_action']} | {note} |\n"
            )


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------


@app.command()
def compare(
    gene_symbol: str = typer.Argument(help="HGNC gene symbol to compare."),
    g2p_source: str | None = typer.Option(
        None,
        "--g2p-source",
        help="Path or URL to a G2P CSV/CSV.GZ export. Defaults to the latest allG2P FTP release.",
    ),
    kb_dir: Path = typer.Option(
        _default_kb_dir(),
        "--kb-dir",
        help="Path to kb/disorders.",
    ),
    format: str = typer.Option(
        "summary",
        "--format",
        help="Output format: tsv, json, summary.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        help="Optional output file path. Defaults to stdout.",
    ),
) -> None:
    """Compare one G2P gene against dismech disease coverage."""
    report = compare_gene(gene_symbol, kb_dir=kb_dir, g2p_source=g2p_source)

    out_stream = output.open("w", encoding="utf-8") if output else None
    try:
        if format == "summary":
            _write_summary(report, file=out_stream)
        elif format == "json":
            _write_json(report, file=out_stream)
        elif format == "tsv":
            _write_tsv(report["comparison_table"], file=out_stream)
            _write_summary(report)
        else:
            raise typer.BadParameter("format must be one of: tsv, summary, json")
    finally:
        if out_stream:
            out_stream.close()


@app.command()
def compare_all(
    gene_symbols: list[str] | None = typer.Argument(
        None,
        help="Optional HGNC gene symbols. Use --all-genes to audit the full release.",
    ),
    g2p_source: str | None = typer.Option(
        None,
        "--g2p-source",
        help="Path or URL to a G2P CSV/CSV.GZ export. Defaults to the latest allG2P FTP release.",
    ),
    all_genes: bool = typer.Option(
        False,
        "--all-genes",
        help="Audit every gene present in the resolved G2P source.",
    ),
    kb_dir: Path = typer.Option(
        _default_kb_dir(),
        "--kb-dir",
        help="Path to kb/disorders.",
    ),
    format: str = typer.Option(
        "summary",
        "--format",
        help="Output format: tsv, gene-tsv, json, summary.",
    ),
    actionable_only: bool = typer.Option(
        False,
        "--actionable-only",
        help="For row-table outputs, omit fully resolved ROOT_MATCH rows.",
    ),
    top: int = typer.Option(
        25,
        "--top",
        min=1,
        help="For summary output, show only the top N genes by curation priority.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        help="Optional output file path. Defaults to stdout.",
    ),
) -> None:
    """Compare multiple G2P genes against dismech disease coverage."""
    try:
        release_report = run_release_comparison(
            gene_symbols=gene_symbols,
            kb_dir=kb_dir,
            g2p_source=g2p_source,
            all_genes=all_genes,
            actionable_only=actionable_only,
        )
    except ValueError as exc:
        raise typer.BadParameter(str(exc)) from exc

    resolved_source = release_report["g2p_source"]
    summaries = release_report["gene_summaries"]
    overview = release_report["overview"]
    row_table = release_report["row_table"]

    out_stream = output.open("w", encoding="utf-8") if output else None
    try:
        if format == "summary":
            _write_batch_summary(
                overview,
                summaries,
                g2p_source=resolved_source,
                top=top,
                file=out_stream,
            )
        elif format == "json":
            out = out_stream or typer.get_text_stream("stdout")
            json.dump(
                {
                    "overview": overview,
                    "gene_summaries": summaries,
                    "row_table": row_table,
                },
                out,
                indent=2,
            )
            out.write("\n")
        elif format == "gene-tsv":
            _write_gene_tsv(summaries, file=out_stream)
        elif format == "tsv":
            _write_tsv(row_table, file=out_stream)
        else:
            raise typer.BadParameter(
                "format must be one of: tsv, gene-tsv, summary, json"
            )
    finally:
        if out_stream:
            out_stream.close()


if __name__ == "__main__":
    app()

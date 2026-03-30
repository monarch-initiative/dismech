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


def extract_dismech_gene_matches(
    kb_dir: Path,
    gene_symbol: str,
    g2p_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []

    for path in _iter_disease_files(kb_dir):
        disorder = _load_disease_yaml(path)

        genetic_matches: list[dict[str, Any]] = []
        for entry in disorder.get("genetic") or []:
            if not isinstance(entry, dict):
                continue
            descriptor = entry.get("gene_term")
            symbol = _descriptor_symbol(
                descriptor if isinstance(descriptor, dict) else None
            )
            symbol = symbol or str(entry.get("name", ""))
            if symbol != gene_symbol:
                continue
            genetic_matches.append(
                {
                    "name": entry.get("name", gene_symbol),
                    "association": entry.get("association", ""),
                    "subtype": entry.get("subtype", ""),
                    "pmids": sorted(_extract_pmids(entry)),
                }
            )

        pathophysiology_matches: list[dict[str, Any]] = []
        for node in disorder.get("pathophysiology") or []:
            if not isinstance(node, dict):
                continue
            symbols = _pathophysiology_gene_symbols(node)
            if gene_symbol not in symbols:
                continue
            pathophysiology_matches.append(
                {
                    "name": node.get("name", ""),
                    "pmids": sorted(_extract_pmids(node)),
                }
            )

        if not genetic_matches and not pathophysiology_matches:
            continue

        disorder_name = str(disorder.get("name", path.stem))
        disorder_mondo = _get_disease_term_id(disorder)
        disorder_phenotypes = _disorder_phenotype_ids(disorder)

        linked_rows = []
        for row in g2p_rows:
            reasons = _match_reasons_for_row(
                row,
                disorder_name=disorder_name,
                disorder_mondo=disorder_mondo,
                gene_symbol=gene_symbol,
            )
            if reasons:
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

        matched_section_pmids = sorted(
            {
                pmid
                for match in genetic_matches + pathophysiology_matches
                for pmid in match["pmids"]
            }
        )

        matches.append(
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
                "all_pmids": sorted(_extract_pmids(disorder)),
                "linked_g2p_rows": linked_rows,
            }
        )

    matches.sort(
        key=lambda match: (
            _MATCH_PRIORITY[match["match_strength"]],
            match["disorder_name"].casefold(),
        )
    )
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
            }
        )

    table.sort(key=lambda item: item["g2p_id"])
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
    row_status_counts: dict[str, int] = {}
    for row in g2p_rows:
        row_status = row["row_status"]
        row_status_counts[row_status] = row_status_counts.get(row_status, 0) + 1
    row_status_counts = dict(sorted(row_status_counts.items()))

    direct_coverage = publication_coverage["direct_dismech_matched_sections"]
    return {
        "gene_symbol": gene_symbol,
        "g2p_source": g2p_source,
        "g2p_row_count": len(g2p_rows),
        "mapped_row_count": mapped_rows,
        "unmapped_row_count": len(g2p_rows) - mapped_rows,
        "dismech_match_count": len(dismech_matches),
        "direct_dismech_match_count": len(_direct_matches(dismech_matches)),
        "g2p_mondo_collision_count": len(mondo_collisions),
        "direct_section_pmid_overlap_count": direct_coverage["overlap_count"],
        "direct_section_pmid_missing_count": direct_coverage[
            "missing_from_dismech_count"
        ],
        "row_status_counts": row_status_counts,
    }


def compare_gene(
    gene_symbol: str,
    *,
    kb_dir: Path = _default_kb_dir(),
    g2p_source: str | None = None,
    g2p_rows_by_gene: dict[str, list[dict[str, Any]]] | None = None,
    resolved_g2p_source: str | None = None,
) -> dict[str, Any]:
    if g2p_rows_by_gene is None:
        source, rows_by_gene = load_g2p_index(g2p_source)
    else:
        source = resolved_g2p_source or g2p_source or "<preloaded>"
        rows_by_gene = g2p_rows_by_gene

    g2p_rows = [dict(row) for row in rows_by_gene.get(gene_symbol, [])]
    dismech_matches = extract_dismech_gene_matches(kb_dir, gene_symbol, g2p_rows)

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


def survey_genes(
    gene_symbols: list[str],
    *,
    kb_dir: Path = _default_kb_dir(),
    g2p_source: str | None = None,
) -> list[dict[str, Any]]:
    resolved_source, rows_by_gene = load_g2p_index(g2p_source)
    reports = [
        compare_gene(
            gene_symbol,
            kb_dir=kb_dir,
            g2p_source=resolved_source,
            g2p_rows_by_gene=rows_by_gene,
            resolved_g2p_source=resolved_source,
        )
        for gene_symbol in gene_symbols
    ]

    summaries = [report["summary"] for report in reports]
    summaries.sort(
        key=lambda item: (
            -item["direct_section_pmid_overlap_count"],
            item["unmapped_row_count"],
            item["gene_symbol"].casefold(),
        )
    )
    return summaries


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


def _write_batch_summary(summaries: list[dict[str, Any]], file=None) -> None:
    out = file or typer.get_text_stream("stdout")
    for summary in summaries:
        status_text = ", ".join(
            f"{status}={count}"
            for status, count in sorted(summary["row_status_counts"].items())
        )
        out.write(
            f"- {summary['gene_symbol']}: g2p_rows={summary['g2p_row_count']}, "
            f"mapped_rows={summary['mapped_row_count']}, "
            f"direct_dismech_matches={summary['direct_dismech_match_count']}, "
            f"mondo_collisions={summary['g2p_mondo_collision_count']}, "
            f"direct_section_pmid_overlap={summary['direct_section_pmid_overlap_count']}, "
            f"direct_section_pmid_missing={summary['direct_section_pmid_missing_count']}, "
            f"row_statuses={status_text}\n"
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
    gene_symbols: list[str] = typer.Argument(help="One or more HGNC gene symbols."),
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
    """Compare multiple G2P genes against dismech disease coverage."""
    resolved_source, rows_by_gene = load_g2p_index(g2p_source)
    reports = [
        compare_gene(
            gene_symbol,
            kb_dir=kb_dir,
            g2p_source=resolved_source,
            g2p_rows_by_gene=rows_by_gene,
            resolved_g2p_source=resolved_source,
        )
        for gene_symbol in gene_symbols
    ]
    summaries = [report["summary"] for report in reports]
    summaries.sort(
        key=lambda item: (
            -item["direct_section_pmid_overlap_count"],
            item["unmapped_row_count"],
            item["gene_symbol"].casefold(),
        )
    )

    out_stream = output.open("w", encoding="utf-8") if output else None
    try:
        if format == "summary":
            _write_batch_summary(summaries, file=out_stream)
        elif format == "json":
            out = out_stream or typer.get_text_stream("stdout")
            json.dump(
                {
                    "gene_summaries": summaries,
                    "reports": reports,
                },
                out,
                indent=2,
            )
            out.write("\n")
        elif format == "tsv":
            rows = [row for report in reports for row in report["comparison_table"]]
            _write_tsv(rows, file=out_stream)
        else:
            raise typer.BadParameter("format must be one of: tsv, summary, json")
    finally:
        if out_stream:
            out_stream.close()


if __name__ == "__main__":
    app()

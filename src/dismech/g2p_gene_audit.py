"""Audit G2P gene rows against dismech disease coverage."""

from __future__ import annotations

import csv
import gzip
import io
import json
import re
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any

import typer
import yaml

app = typer.Typer(help="Audit G2P gene rows against dismech disease coverage.")

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

_DEFAULT_KB_DIR = Path(__file__).resolve().parents[2] / "kb" / "disorders"


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


def load_g2p_rows_for_gene(source: str, gene_symbol: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for row in _iter_g2p_rows(source):
        if row.get("gene symbol") != gene_symbol:
            continue
        rows.append(
            {
                "g2p_id": row.get("g2p id", ""),
                "gene_symbol": row.get("gene symbol", ""),
                "disease_name": row.get("disease name", ""),
                "disease_mondo": row.get("disease MONDO", ""),
                "allelic_requirement": row.get("allelic requirement", ""),
                "confidence": row.get("confidence", ""),
                "variant_consequence": row.get("variant consequence", ""),
                "variant_types": _split_semicolon_field(row.get("variant types")),
                "molecular_mechanism": row.get("molecular mechanism", ""),
                "molecular_mechanism_support": row.get(
                    "molecular mechanism support", ""
                ),
                "molecular_mechanism_categorisation": row.get(
                    "molecular mechanism categorisation", ""
                ),
                "molecular_mechanism_evidence": row.get(
                    "molecular mechanism evidence", ""
                ),
                "phenotypes": _split_semicolon_field(row.get("phenotypes")),
                "phenotype_count": len(_split_semicolon_field(row.get("phenotypes"))),
                "reviewed_pmids": _split_semicolon_field(row.get("publications")),
                "reviewed_pmid_count": len(
                    _split_semicolon_field(row.get("publications"))
                ),
                "additional_mined_pmids": _split_semicolon_field(
                    row.get("additional mined publications")
                ),
                "panel": _split_semicolon_field(row.get("panel")),
                "date_of_last_review": row.get("date of last review", ""),
                "review": row.get("review", ""),
            }
        )

    return rows


def load_dismech_gene_matches(
    kb_dir: Path,
    gene_symbol: str,
    g2p_rows: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []

    for path in sorted(kb_dir.glob("*.yaml")):
        if path.name.endswith(".history.yaml"):
            continue

        with open(path) as stream:
            disorder = yaml.safe_load(stream) or {}
        if not isinstance(disorder, dict):
            continue

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

        disease_term = disorder.get("disease_term") or {}
        disease_term_term = (
            disease_term.get("term") if isinstance(disease_term, dict) else {}
        )
        disorder_mondo = (
            disease_term_term.get("id") if isinstance(disease_term_term, dict) else None
        )

        linked_rows = []
        for row in g2p_rows:
            reasons = _match_reasons_for_row(
                row,
                disorder_name=str(disorder.get("name", path.stem)),
                disorder_mondo=disorder_mondo,
                gene_symbol=gene_symbol,
            )
            if reasons:
                linked_rows.append(
                    {
                        "g2p_id": row["g2p_id"],
                        "disease_name": row["disease_name"],
                        "match_reasons": reasons,
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
                "disorder_name": disorder.get("name", path.stem),
                "disease_mondo": disorder_mondo,
                "match_strength": _classify_match_strength(
                    genetic_matches, pathophysiology_matches
                ),
                "genetic_matches": genetic_matches,
                "pathophysiology_matches": pathophysiology_matches,
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


def compare_gene(
    gene_symbol: str,
    *,
    kb_dir: Path = _DEFAULT_KB_DIR,
    g2p_source: str | None = None,
) -> dict[str, Any]:
    source = g2p_source or _resolve_latest_g2p_url()
    g2p_rows = load_g2p_rows_for_gene(source, gene_symbol)
    dismech_matches = load_dismech_gene_matches(kb_dir, gene_symbol, g2p_rows)

    row_candidates: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for disorder in dismech_matches:
        for linked_row in disorder["linked_g2p_rows"]:
            row_candidates[linked_row["g2p_id"]].append(
                {
                    "disorder_name": disorder["disorder_name"],
                    "file": disorder["file"],
                    "match_strength": disorder["match_strength"],
                    "match_reasons": linked_row["match_reasons"],
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

    direct_matches = [
        match
        for match in dismech_matches
        if match["match_strength"] in {"causative", "subtype_specific"}
    ]

    def _union_pmids(items: list[dict[str, Any]], key: str) -> list[str]:
        return sorted({pmid for item in items for pmid in item.get(key, [])})

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
        "publication_coverage": {
            "all_dismech_matched_sections": _coverage_summary(
                all_dismech_section_pmids
            ),
            "all_dismech_matched_diseases": _coverage_summary(
                all_dismech_disease_pmids
            ),
            "direct_dismech_matched_sections": _coverage_summary(
                direct_dismech_section_pmids
            ),
            "direct_dismech_matched_diseases": _coverage_summary(
                direct_dismech_disease_pmids
            ),
        },
    }


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
            f" | phenotypes={row['phenotype_count']}\n"
        )
        if row["dismech_candidates"]:
            candidate_text = "; ".join(
                (
                    f"{candidate['disorder_name']} "
                    f"[{candidate['match_strength']}; {','.join(candidate['match_reasons'])}]"
                )
                for candidate in row["dismech_candidates"]
            )
            out.write(f"  dismech candidates: {candidate_text}\n")
        else:
            out.write("  dismech candidates: none\n")

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

    for label, coverage in report["publication_coverage"].items():
        out.write(
            f"{label}: g2p={coverage['g2p_reviewed_pmid_count']}, "
            f"dismech={coverage['dismech_pmid_count']}, "
            f"overlap={coverage['overlap_count']}, "
            f"missing_from_dismech={coverage['missing_from_dismech_count']}\n"
        )


@app.command()
def audit(
    gene_symbol: str = typer.Argument(help="HGNC gene symbol to audit."),
    g2p_source: str | None = typer.Option(
        None,
        "--g2p-source",
        help="Path or URL to a G2P CSV/CSV.GZ export. Defaults to the latest allG2P FTP release.",
    ),
    kb_dir: Path = typer.Option(
        _DEFAULT_KB_DIR,
        "--kb-dir",
        help="Path to kb/disorders.",
    ),
    format: str = typer.Option(
        "summary",
        "--format",
        help="Output format: summary or json.",
    ),
    output: Path | None = typer.Option(
        None,
        "--output",
        help="Optional output file path. Defaults to stdout.",
    ),
) -> None:
    """Audit a single gene across G2P rows and dismech disease files."""
    report = compare_gene(gene_symbol, kb_dir=kb_dir, g2p_source=g2p_source)

    out_stream = output.open("w", encoding="utf-8") if output else None
    try:
        if format == "summary":
            _write_summary(report, file=out_stream)
        elif format == "json":
            out = out_stream or typer.get_text_stream("stdout")
            json.dump(report, out, indent=2)
            out.write("\n")
        else:
            raise typer.BadParameter("format must be one of: summary, json")
    finally:
        if out_stream:
            out_stream.close()


if __name__ == "__main__":
    app()

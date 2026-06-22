"""Compare dismech disease-to-phenotype annotations against external sources.

The comparison data come from the Monarch association API, split by primary
knowledge source into OMIM and Orphanet-backed phenotype records. The audit
commands turn those comparisons into a phenotype-completeness checklist:

* source-backed phenotypes absent from the local top-level phenotype list,
* source-backed phenotypes covered only by a broader local HPO term,
* local phenotypes without supporting evidence, and
* local phenotypes not causally linked into the rendered pathograph.
"""

from __future__ import annotations

import json
import re
import sys
from contextlib import nullcontext
from pathlib import Path
from typing import Any

import httpx
import typer
from oaklib import get_adapter

from dismech.qc_plugins import causal_inlink_coverage

from .support import default_kb_dir as _default_kb_dir
from .support import get_disease_term_id as _get_mondo_id
from .support import iter_disease_files as _iter_disease_files
from .support import load_yaml_object as _load_disease_yaml
from .support import normalize_hp_id as _normalize_hp_id

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_HP_ADAPTER_SPEC = "sqlite:obo:hp"
_MONARCH_ASSOC_URL = "https://api.monarchinitiative.org/v3/api/association"
_D2P_CATEGORY = "biolink:DiseaseToPhenotypicFeatureAssociation"
_PAGE_LIMIT = 500

_SOURCE_OMIM = "infores:omim"
_SOURCE_ORDO = "infores:orphanet"

_SOURCE_COLUMNS = ("omim", "ordo")
_SUPPORTING_EVIDENCE_VALUES = {"SUPPORT", "PARTIAL"}
_GENETIC_CATEGORY_KEYWORDS = ("mendelian", "genetic", "chromosomal")

app = typer.Typer(help="Compare dismech phenotypes against OMIM/Orphanet databases.")


# ---------------------------------------------------------------------------
# HPO closure resolver
# ---------------------------------------------------------------------------


class HPOClosureResolver:
    """Lazily loads OAK HP adapter and provides is-a ancestor lookups with caching."""

    def __init__(self) -> None:
        self._adapter = None
        self._ancestor_cache: dict[str, set[str]] = {}

    def _get_adapter(self):
        if self._adapter is None:
            self._adapter = get_adapter(_HP_ADAPTER_SPEC)
        return self._adapter

    def ancestors(self, term_id: str) -> set[str]:
        normalized = _normalize_hp_id(term_id)
        if not normalized:
            return set()
        if normalized in self._ancestor_cache:
            return self._ancestor_cache[normalized]

        adapter = self._get_adapter()
        try:
            anc = {
                a
                for a in adapter.ancestors(
                    normalized, predicates=["rdfs:subClassOf"], reflexive=True
                )
                if isinstance(a, str)
            }
        except Exception as exc:
            typer.echo(
                f"WARNING: could not resolve HPO ancestors for {normalized}: {exc}",
                err=True,
            )
            anc = set()

        self._ancestor_cache[normalized] = anc
        return anc

    def label(self, term_id: str) -> str | None:
        """Return the canonical label for an HPO term."""
        normalized = _normalize_hp_id(term_id)
        if not normalized:
            return None
        adapter = self._get_adapter()
        try:
            return adapter.label(normalized)
        except Exception as exc:
            typer.echo(
                f"WARNING: could not resolve HPO label for {normalized}: {exc}",
                err=True,
            )
            return None


# ---------------------------------------------------------------------------
# Monarch API fetching
# ---------------------------------------------------------------------------


def fetch_monarch_d2p(mondo_id: str) -> list[dict[str, Any]]:
    """Fetch disease-to-phenotype associations from the Monarch Initiative API.

    Returns the raw association records (all pages).
    """
    all_items: list[dict[str, Any]] = []
    offset = 0

    with httpx.Client(timeout=60) as client:
        while True:
            params = {
                "subject": mondo_id,
                "category": _D2P_CATEGORY,
                "limit": _PAGE_LIMIT,
                "offset": offset,
                "direct": "false",
            }
            resp = client.get(_MONARCH_ASSOC_URL, params=params)
            resp.raise_for_status()
            data = resp.json()
            items = data.get("items", [])
            all_items.extend(items)
            total = data.get("total", 0)
            offset += len(items)
            if not items or offset >= total:
                break

    return all_items


def _is_explicit_zero_frequency(item: dict[str, Any]) -> bool:
    """Return true for source rows that explicitly assert zero observed cases."""
    has_pct = item.get("has_percentage")
    if has_pct is not None:
        try:
            return float(has_pct) == 0.0
        except (TypeError, ValueError):
            return False

    has_count = item.get("has_count")
    if has_count is not None:
        try:
            return int(has_count) == 0
        except (TypeError, ValueError):
            return False

    return False


def _parse_monarch_associations(
    items: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Split Monarch associations into OMIM and Orphanet phenotype records.

    Returns (omim_phenos, ordo_phenos) where each entry is a dict with:
      - hp_id: normalized HP CURIE
      - label: phenotype label
      - frequency: frequency string (if available)
      - pmids: list of PMID strings (if available)
      - has_percentage: percentage string (if available)
    """
    omim: list[dict[str, Any]] = []
    ordo: list[dict[str, Any]] = []

    for item in items:
        source = item.get("primary_knowledge_source", "")
        obj = item.get("object", "")
        hp_id = _normalize_hp_id(obj)
        if not hp_id:
            continue
        if _is_explicit_zero_frequency(item):
            continue

        label = item.get("object_label", "")

        # Extract frequency qualifier
        freq_qual = item.get("frequency_qualifier")
        freq_label = item.get("frequency_qualifier_label", "")
        freq_str = freq_label if freq_label else (freq_qual or "")

        # Extract numeric frequency (has_percentage, has_count/has_total)
        has_pct = item.get("has_percentage")
        has_count = item.get("has_count")
        has_total = item.get("has_total")
        pct_str = ""
        if has_pct is not None:
            pct_str = f"{has_pct}%"
        elif has_count is not None and has_total is not None:
            try:
                pct_str = f"{int(has_count)}/{int(has_total)}"
            except (ValueError, TypeError):
                pass

        # Extract PMIDs from publications
        pmids: list[str] = []
        for pub in item.get("publications", []) or []:
            pub_id = pub if isinstance(pub, str) else pub.get("id", "")
            if pub_id.upper().startswith("PMID:"):
                pmids.append(pub_id)

        record = {
            "hp_id": hp_id,
            "label": label,
            "frequency": freq_str,
            "has_percentage": pct_str,
            "pmids": pmids,
        }

        if _SOURCE_OMIM in source:
            omim.append(record)
        elif _SOURCE_ORDO in source:
            ordo.append(record)

    return omim, ordo


# ---------------------------------------------------------------------------
# Dismech phenotype extraction
# ---------------------------------------------------------------------------


def extract_dismech_phenotypes(disease_data: dict[str, Any]) -> list[dict[str, Any]]:
    """Extract phenotype records from a dismech disease YAML dict.

    Returns list of dicts with: hp_id, label, name, frequency, pmids, and
    evidence-count metadata.
    """
    phenotypes = disease_data.get("phenotypes", [])
    if not isinstance(phenotypes, list):
        return []

    results: list[dict[str, Any]] = []
    for item in phenotypes:
        if not isinstance(item, dict):
            continue

        term_desc = item.get("phenotype_term")
        if not isinstance(term_desc, dict):
            continue
        raw_term = term_desc.get("term")
        if not isinstance(raw_term, dict):
            continue

        hp_id = _normalize_hp_id(raw_term.get("id"))
        if not hp_id:
            continue

        label = (
            raw_term.get("label")
            or term_desc.get("preferred_term")
            or item.get("name")
            or ""
        )
        frequency = str(item.get("frequency", "")) if item.get("frequency") else ""

        pmids: list[str] = []
        references: list[str] = []
        supporting_references: list[str] = []
        for ev in item.get("evidence", []) or []:
            if not isinstance(ev, dict):
                continue
            ref = ev.get("reference", "")
            if isinstance(ref, str) and ref.strip():
                references.append(ref)
            if ref.upper().startswith("PMID:"):
                pmids.append(ref)
            supports = str(ev.get("supports", "")).upper()
            if ref and supports in _SUPPORTING_EVIDENCE_VALUES:
                supporting_references.append(ref)

        results.append(
            {
                "hp_id": hp_id,
                "label": label,
                "name": item.get("name") or label,
                "frequency": frequency,
                "pmids": pmids,
                "references": references,
                "supporting_references": supporting_references,
                "evidence_count": len(references),
                "supporting_evidence_count": len(supporting_references),
            }
        )

    return results


# ---------------------------------------------------------------------------
# Completeness audit
# ---------------------------------------------------------------------------


_AUDIT_COLUMNS = [
    "issue_type",
    "priority",
    "disease_id",
    "disease_name",
    "phenotype_id",
    "phenotype_label",
    "phenotype_name",
    "dismech",
    "omim",
    "ordo",
    "source_evidence_refs",
    "local_evidence_refs",
    "pathograph_status",
    "recommendation",
]


def _cell_match_kind(cell: Any) -> str | None:
    if not isinstance(cell, str) or cell == "-":
        return None
    return cell.split(";", 1)[0]


def _has_source_backing(row: dict[str, Any]) -> bool:
    return any(row.get(column) != "-" for column in _SOURCE_COLUMNS)


def _local_phenotypes_by_hp(
    dismech_phenos: list[dict[str, Any]],
) -> dict[str, list[dict[str, Any]]]:
    by_hp: dict[str, list[dict[str, Any]]] = {}
    for rec in dismech_phenos:
        hp_id = rec.get("hp_id")
        if isinstance(hp_id, str):
            by_hp.setdefault(hp_id, []).append(rec)
    return by_hp


def _first_local_for_row(
    row: dict[str, Any], by_hp: dict[str, list[dict[str, Any]]]
) -> dict[str, Any] | None:
    phenotype_id = row.get("phenotype_id")
    if isinstance(phenotype_id, str) and phenotype_id in by_hp:
        return by_hp[phenotype_id][0]
    return None


def _iter_evidence_references(node: Any) -> list[str]:
    refs: list[str] = []
    if isinstance(node, dict):
        ref = node.get("reference")
        if isinstance(ref, str) and ref.strip():
            refs.append(ref.strip())
        for value in node.values():
            refs.extend(_iter_evidence_references(value))
    elif isinstance(node, list):
        for item in node:
            refs.extend(_iter_evidence_references(item))
    return refs


def _source_evidence_refs_for_row(
    row: dict[str, Any], disease_orpha_refs: list[str]
) -> list[str]:
    refs: list[str] = []
    for column in _SOURCE_COLUMNS:
        value = row.get(column)
        if not isinstance(value, str) or value == "-":
            continue
        refs.extend(re.findall(r"PMID:\d+", value))
        if column == "ordo":
            refs.extend(disease_orpha_refs)
    return sorted(set(refs))


def _audit_row(
    *,
    issue_type: str,
    priority: str,
    row: dict[str, Any],
    phenotype_name: str = "",
    source_evidence_refs: list[str] | None = None,
    local_evidence_refs: list[str] | None = None,
    pathograph_status: str = "",
    recommendation: str,
) -> dict[str, Any]:
    return {
        "issue_type": issue_type,
        "priority": priority,
        "disease_id": row.get("disease_id", ""),
        "disease_name": row.get("disease_name", ""),
        "phenotype_id": row.get("phenotype_id", ""),
        "phenotype_label": row.get("phenotype_label", ""),
        "phenotype_name": phenotype_name,
        "dismech": row.get("dismech", "-"),
        "omim": row.get("omim", "-"),
        "ordo": row.get("ordo", "-"),
        "source_evidence_refs": ";".join(source_evidence_refs or []),
        "local_evidence_refs": ";".join(local_evidence_refs or []),
        "pathograph_status": pathograph_status,
        "recommendation": recommendation,
    }


def build_completeness_audit(
    disease_data: dict[str, Any],
    comparison_table: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    """Build actionable phenotype-completeness audit rows for one disease.

    The audit is intentionally conservative: it does not add phenotypes. It
    identifies where a curator should inspect source-backed evidence and only
    then update the disease YAML.
    """
    audit_rows: list[dict[str, Any]] = []
    dismech_phenos = extract_dismech_phenotypes(disease_data)
    disease_orpha_refs = sorted(
        {
            ref
            for ref in _iter_evidence_references(disease_data)
            if ref.startswith("ORPHA:")
        }
    )
    by_hp = _local_phenotypes_by_hp(dismech_phenos)
    table_by_hp = {
        row.get("phenotype_id"): row
        for row in comparison_table
        if isinstance(row.get("phenotype_id"), str)
    }

    for row in comparison_table:
        if not _has_source_backing(row):
            continue

        dismech_cell = row.get("dismech")
        if dismech_cell == "-":
            audit_rows.append(
                _audit_row(
                    issue_type="source_phenotype_missing_locally",
                    priority="high",
                    row=row,
                    source_evidence_refs=_source_evidence_refs_for_row(
                        row, disease_orpha_refs
                    ),
                    pathograph_status="not_local",
                    recommendation=(
                        "Review the source-backed phenotype; add it as a top-level "
                        "phenotype only with exact supporting evidence, and link it "
                        "from the pathograph if the mechanism explains it."
                    ),
                )
            )
            continue

        match_kind = _cell_match_kind(dismech_cell)
        if match_kind and match_kind.startswith("broad:"):
            local = _first_local_for_row(row, by_hp)
            audit_rows.append(
                _audit_row(
                    issue_type="source_phenotype_covered_only_by_broader_local_term",
                    priority="medium",
                    row=row,
                    phenotype_name=str(local.get("name", "")) if local else "",
                    source_evidence_refs=_source_evidence_refs_for_row(
                        row, disease_orpha_refs
                    ),
                    local_evidence_refs=(
                        list(local.get("supporting_references", [])) if local else []
                    ),
                    pathograph_status="local_broader_match",
                    recommendation=(
                        "Review whether the local HPO assertion is too broad; add or "
                        "replace with the specific phenotype only after validating exact "
                        "evidence."
                    ),
                )
            )

    _connected, _total, unconnected = causal_inlink_coverage(disease_data)
    unconnected_names = set(unconnected)

    for local in dismech_phenos:
        hp_id = local["hp_id"]
        row = table_by_hp.get(hp_id) or {
            "disease_id": _get_mondo_id(disease_data) or "",
            "disease_name": disease_data.get("name", ""),
            "phenotype_id": hp_id,
            "phenotype_label": local.get("label", ""),
            "dismech": "exact",
            "omim": "-",
            "ordo": "-",
        }
        phenotype_name = str(local.get("name", ""))
        supporting_refs = list(local.get("supporting_references", []))

        if not supporting_refs:
            audit_rows.append(
                _audit_row(
                    issue_type="local_phenotype_missing_supporting_evidence",
                    priority="high",
                    row=row,
                    phenotype_name=phenotype_name,
                    source_evidence_refs=_source_evidence_refs_for_row(
                        row, disease_orpha_refs
                    ),
                    local_evidence_refs=list(local.get("references", [])),
                    pathograph_status=(
                        "unlinked" if phenotype_name in unconnected_names else "linked"
                    ),
                    recommendation=(
                        "Add exact SUPPORT/PARTIAL evidence for this phenotype or "
                        "remove the unsupported assertion."
                    ),
                )
            )

        if phenotype_name in unconnected_names:
            audit_rows.append(
                _audit_row(
                    issue_type="local_phenotype_unlinked_to_pathograph",
                    priority="medium",
                    row=row,
                    phenotype_name=phenotype_name,
                    source_evidence_refs=_source_evidence_refs_for_row(
                        row, disease_orpha_refs
                    ),
                    local_evidence_refs=supporting_refs,
                    pathograph_status="unlinked",
                    recommendation=(
                        "Review whether the phenotype is mechanistically explainable; "
                        "if so, add an evidence-backed downstream edge or intermediate "
                        "pathophysiology node."
                    ),
                )
            )

    priority_rank = {"high": 0, "medium": 1, "low": 2}
    audit_rows.sort(
        key=lambda item: (
            priority_rank.get(str(item["priority"]), 99),
            str(item["disease_name"]).casefold(),
            str(item["issue_type"]),
            str(item["phenotype_label"]).casefold(),
            str(item["phenotype_id"]),
        )
    )
    return audit_rows


def compute_audit_summary(audit_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Summarize audit rows by issue type and priority."""
    by_issue: dict[str, int] = {}
    by_priority: dict[str, int] = {}
    diseases: set[str] = set()
    for row in audit_rows:
        issue_type = str(row.get("issue_type", ""))
        priority = str(row.get("priority", ""))
        disease_name = str(row.get("disease_name", ""))
        if issue_type:
            by_issue[issue_type] = by_issue.get(issue_type, 0) + 1
        if priority:
            by_priority[priority] = by_priority.get(priority, 0) + 1
        if disease_name:
            diseases.add(disease_name)
    return {
        "total_issues": len(audit_rows),
        "disease_count": len(diseases),
        "by_issue_type": dict(sorted(by_issue.items())),
        "by_priority": dict(sorted(by_priority.items())),
    }


def _is_genetic_disease(disease_data: dict[str, Any]) -> bool:
    """Return whether a disease should be included in genetic-disease audits."""
    if disease_data.get("genetic"):
        return True
    category = disease_data.get("category")
    if not isinstance(category, str):
        return False
    category_text = category.casefold()
    return any(keyword in category_text for keyword in _GENETIC_CATEGORY_KEYWORDS)


# ---------------------------------------------------------------------------
# Comparison logic
# ---------------------------------------------------------------------------


def _match_type(
    target_hp: str,
    source_phenos: list[dict[str, Any]],
    resolver: HPOClosureResolver | None,
) -> tuple[str, dict[str, Any] | None]:
    """Determine how a target HP ID matches against a list of source phenotypes.

    Returns (match_string, matched_record) where match_string is one of:
      - "-" : no match
      - "exact" : exact HP ID match
      - "narrow:<HP_ID>" : source has a more specific descendant
      - "broad:<HP_ID>" : source has a more general ancestor
    """
    # Check exact match first
    for rec in source_phenos:
        if rec["hp_id"] == target_hp:
            return "exact", rec

    if resolver is None:
        return "-", None

    # Check closure matches
    target_ancestors = resolver.ancestors(target_hp)

    # Check if any source term is a descendant of target (source is narrower)
    for rec in source_phenos:
        src_hp = rec["hp_id"]
        src_ancestors = resolver.ancestors(src_hp)
        if target_hp in src_ancestors and src_hp != target_hp:
            return f"narrow:{src_hp}", rec

    # Check if any source term is an ancestor of target (source is broader)
    for rec in source_phenos:
        src_hp = rec["hp_id"]
        if src_hp in target_ancestors and src_hp != target_hp:
            return f"broad:{src_hp}", rec

    return "-", None


def _format_cell(match_str: str, record: dict[str, Any] | None) -> str:
    """Format a comparison cell with match type and metadata."""
    if match_str == "-" or record is None:
        return "-"

    parts = [match_str]

    # Add frequency info
    if record.get("has_percentage"):
        parts.append(record["has_percentage"])
    elif record.get("frequency"):
        parts.append(f"freq={record['frequency']}")

    # Add PMIDs
    for pmid in record.get("pmids", []):
        parts.append(pmid)

    return ";".join(parts)


def build_comparison_table(
    mondo_id: str,
    disease_name: str,
    dismech_phenos: list[dict[str, Any]],
    omim_phenos: list[dict[str, Any]],
    ordo_phenos: list[dict[str, Any]],
    resolver: HPOClosureResolver | None,
) -> list[dict[str, Any]]:
    """Build the comparison table across all three sources.

    Returns a list of row dicts, one per unique phenotype.
    """
    # Collect all unique HP IDs across sources
    all_hp_ids: dict[str, str] = {}  # hp_id -> best label

    for rec in dismech_phenos:
        hp = rec["hp_id"]
        if hp not in all_hp_ids or not all_hp_ids[hp]:
            all_hp_ids[hp] = rec.get("label", "")

    for rec in omim_phenos + ordo_phenos:
        hp = rec["hp_id"]
        if hp not in all_hp_ids or not all_hp_ids[hp]:
            all_hp_ids[hp] = rec.get("label", "")

    rows: list[dict[str, Any]] = []
    for hp_id in sorted(all_hp_ids.keys()):
        label = all_hp_ids[hp_id]
        # Try to get a better label from the resolver if we have one
        if resolver and not label:
            resolved_label = resolver.label(hp_id)
            if resolved_label:
                label = resolved_label

        dismech_match, dismech_rec = _match_type(hp_id, dismech_phenos, resolver)
        omim_match, omim_rec = _match_type(hp_id, omim_phenos, resolver)
        ordo_match, ordo_rec = _match_type(hp_id, ordo_phenos, resolver)

        rows.append(
            {
                "disease_id": mondo_id,
                "disease_name": disease_name,
                "phenotype_id": hp_id,
                "phenotype_label": label,
                "dismech": _format_cell(dismech_match, dismech_rec),
                "omim": _format_cell(omim_match, omim_rec),
                "ordo": _format_cell(ordo_match, ordo_rec),
            }
        )

    return rows


# ---------------------------------------------------------------------------
# Venn summary
# ---------------------------------------------------------------------------


def compute_venn_summary(table: list[dict[str, Any]]) -> dict[str, int]:
    """Compute N-way Venn counts from the comparison table."""
    counts = {
        "dismech_only": 0,
        "omim_only": 0,
        "ordo_only": 0,
        "dismech_omim": 0,
        "dismech_ordo": 0,
        "omim_ordo": 0,
        "all_three": 0,
        "total": 0,
    }

    for row in table:
        d = row["dismech"] != "-"
        o = row["omim"] != "-"
        r = row["ordo"] != "-"
        counts["total"] += 1

        if d and o and r:
            counts["all_three"] += 1
        elif d and o and not r:
            counts["dismech_omim"] += 1
        elif d and not o and r:
            counts["dismech_ordo"] += 1
        elif not d and o and r:
            counts["omim_ordo"] += 1
        elif d and not o and not r:
            counts["dismech_only"] += 1
        elif not d and o and not r:
            counts["omim_only"] += 1
        elif not d and not o and r:
            counts["ordo_only"] += 1

    return counts


# ---------------------------------------------------------------------------
# Disease resolution helpers
# ---------------------------------------------------------------------------


def _resolve_disease_ref(ref: str) -> tuple[str, Path]:
    """Resolve a disease reference to (slug, path)."""
    reference_text = str(ref).strip()
    if not reference_text:
        raise ValueError("Disease reference must not be empty")

    ref_path = Path(reference_text)
    if ref_path.exists():
        path = ref_path.resolve()
        if not path.is_file():
            raise ValueError(f"Disease reference path is not a file: {path}")
        slug = path.stem
        if slug.endswith(".history"):
            slug = slug[: -len(".history")]
        return slug, path

    disorder_dir = _default_kb_dir()
    if not disorder_dir.exists():
        raise FileNotFoundError(f"Disorder directory does not exist: {disorder_dir}")

    literal_candidates = [
        reference_text,
        f"{reference_text}.yaml",
        reference_text.replace(" ", "_"),
        f"{reference_text.replace(' ', '_')}.yaml",
    ]
    for candidate in literal_candidates:
        candidate_path = disorder_dir / candidate
        if candidate_path.exists() and candidate_path.is_file():
            slug = candidate_path.stem
            if slug.endswith(".history"):
                slug = slug[: -len(".history")]
            return slug, candidate_path.resolve()

    disease_files = _iter_disease_files(disorder_dir)

    if ":" in reference_text:
        ref_upper = reference_text.upper()
        matches: list[Path] = []
        for disease_file in disease_files:
            disease_model = _load_disease_yaml(disease_file)
            term_id = _get_mondo_id(disease_model)
            if term_id and term_id.upper() == ref_upper:
                matches.append(disease_file)
        if len(matches) == 1:
            return matches[0].stem, matches[0].resolve()
        if len(matches) > 1:
            raise ValueError(
                f"Disease reference '{reference_text}' matched multiple disease files: "
                + ", ".join(path.name for path in matches)
            )

    normalized_ref = _normalize_disease_lookup(reference_text)
    name_matches: list[Path] = []
    for disease_file in disease_files:
        disease_model = _load_disease_yaml(disease_file)
        disease_name = disease_model.get("name")
        if (
            _normalize_disease_lookup(str(disease_name) if disease_name else "")
            == normalized_ref
        ):
            name_matches.append(disease_file)
            continue
        if _normalize_disease_lookup(disease_file.stem) == normalized_ref:
            name_matches.append(disease_file)

    if len(name_matches) == 1:
        return name_matches[0].stem, name_matches[0].resolve()
    if len(name_matches) > 1:
        raise ValueError(
            f"Disease reference '{reference_text}' is ambiguous; matches: "
            + ", ".join(path.name for path in name_matches)
        )

    raise FileNotFoundError(
        f"Could not resolve disease reference '{reference_text}' as a path, slug, id, or name in {disorder_dir}"
    )


def _normalize_disease_lookup(value: str | None) -> str:
    """Normalize disease names/slugs for tolerant lookup."""
    if not value:
        return ""
    compact = value.casefold().replace("_", " ").replace("-", " ")
    return " ".join(compact.split())


# ---------------------------------------------------------------------------
# Output formatters
# ---------------------------------------------------------------------------

_TSV_COLUMNS = [
    "disease_id",
    "disease_name",
    "phenotype_id",
    "phenotype_label",
    "dismech",
    "omim",
    "ordo",
]


def _write_tsv(rows: list[dict[str, Any]], file=None) -> None:
    out = file or sys.stdout
    out.write("\t".join(_TSV_COLUMNS) + "\n")
    for row in rows:
        out.write("\t".join(str(row.get(c, "")) for c in _TSV_COLUMNS) + "\n")


def _write_json(rows: list[dict[str, Any]], venn: dict[str, int], file=None) -> None:
    out = file or sys.stdout
    json.dump({"table": rows, "venn_summary": venn}, out, indent=2)
    out.write("\n")


def _open_output(output: str | None):
    """Return a writable context manager for output or stdout."""
    if output:
        return open(output, "w", encoding="utf-8")
    return nullcontext(sys.stdout)


def _write_audit_tsv(rows: list[dict[str, Any]], file=None) -> None:
    out = file or sys.stdout
    out.write("\t".join(_AUDIT_COLUMNS) + "\n")
    for row in rows:
        out.write("\t".join(str(row.get(c, "")) for c in _AUDIT_COLUMNS) + "\n")


def _write_audit_json(
    rows: list[dict[str, Any]], summary: dict[str, Any], file=None
) -> None:
    out = file or sys.stdout
    json.dump({"summary": summary, "issues": rows}, out, indent=2)
    out.write("\n")


def build_disease_audit_payload(
    *,
    slug: str,
    source_file: str,
    disease_id: str,
    disease_name: str,
    rows: list[dict[str, Any]],
    status: str = "ok",
    error: str | None = None,
) -> dict[str, Any]:
    """Build the per-disease JSON payload used for checkpointed audit runs."""
    payload: dict[str, Any] = {
        "status": status,
        "slug": slug,
        "source_file": source_file,
        "disease_id": disease_id,
        "disease_name": disease_name,
        "summary": compute_audit_summary(rows),
        "issues": rows,
    }
    if error:
        payload["error"] = error
    return payload


def _write_disease_audit_payload(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _read_disease_audit_payload(path: Path) -> dict[str, Any]:
    with open(path, encoding="utf-8") as stream:
        payload = json.load(stream)
    if not isinstance(payload, dict):
        raise ValueError(f"Audit checkpoint {path} must contain a JSON object")
    return payload


def _write_summary(venn: dict[str, int], disease_name: str, file=None) -> None:
    out = file or sys.stderr
    out.write(f"\n--- Venn Summary for {disease_name} ---\n")
    out.write(f"  Total unique phenotypes: {venn['total']}\n")
    out.write(f"  dismech only:            {venn['dismech_only']}\n")
    out.write(f"  OMIM only:               {venn['omim_only']}\n")
    out.write(f"  Orphanet only:           {venn['ordo_only']}\n")
    out.write(f"  dismech + OMIM:          {venn['dismech_omim']}\n")
    out.write(f"  dismech + Orphanet:      {venn['dismech_ordo']}\n")
    out.write(f"  OMIM + Orphanet:         {venn['omim_ordo']}\n")
    out.write(f"  All three:               {venn['all_three']}\n")


# ---------------------------------------------------------------------------
# Core comparison workflow
# ---------------------------------------------------------------------------


def run_comparison(
    disease_ref: str,
    *,
    use_closure: bool = True,
) -> tuple[list[dict[str, Any]], dict[str, int], str]:
    """Run the full comparison pipeline for a single disease.

    Returns (table_rows, venn_summary, disease_name).
    """
    slug, path = _resolve_disease_ref(disease_ref)
    disease_data = _load_disease_yaml(path)
    disease_name = disease_data.get("name", slug)
    mondo_id = _get_mondo_id(disease_data)

    if not mondo_id:
        typer.echo(
            f"WARNING: {slug} has no disease_term with MONDO ID, skipping.", err=True
        )
        return [], {}, disease_name

    # Extract dismech phenotypes
    dismech_phenos = extract_dismech_phenotypes(disease_data)

    # Fetch Monarch data
    typer.echo(f"Fetching Monarch D2P for {mondo_id} ({disease_name})...", err=True)
    monarch_items = fetch_monarch_d2p(mondo_id)
    omim_phenos, ordo_phenos = _parse_monarch_associations(monarch_items)
    typer.echo(
        f"  Found: {len(dismech_phenos)} dismech, {len(omim_phenos)} OMIM, {len(ordo_phenos)} Orphanet phenotypes",
        err=True,
    )

    # Build resolver
    resolver = HPOClosureResolver() if use_closure else None

    # Build comparison table
    table = build_comparison_table(
        mondo_id, disease_name, dismech_phenos, omim_phenos, ordo_phenos, resolver
    )
    venn = compute_venn_summary(table)

    return table, venn, disease_name


def run_audit(
    disease_ref: str,
    *,
    use_closure: bool = True,
) -> tuple[list[dict[str, Any]], dict[str, Any], str]:
    """Run the phenotype-completeness audit for a single disease."""
    slug, path = _resolve_disease_ref(disease_ref)
    disease_data = _load_disease_yaml(path)
    disease_name = disease_data.get("name", slug)
    mondo_id = _get_mondo_id(disease_data)

    if not mondo_id:
        typer.echo(
            f"WARNING: {slug} has no disease_term with MONDO ID, skipping.", err=True
        )
        return [], {}, disease_name

    dismech_phenos = extract_dismech_phenotypes(disease_data)
    typer.echo(f"Fetching Monarch D2P for {mondo_id} ({disease_name})...", err=True)
    monarch_items = fetch_monarch_d2p(mondo_id)
    omim_phenos, ordo_phenos = _parse_monarch_associations(monarch_items)
    typer.echo(
        f"  Found: {len(dismech_phenos)} dismech, {len(omim_phenos)} OMIM, {len(ordo_phenos)} Orphanet phenotypes",
        err=True,
    )

    resolver = HPOClosureResolver() if use_closure else None
    table = build_comparison_table(
        mondo_id, disease_name, dismech_phenos, omim_phenos, ordo_phenos, resolver
    )
    audit_rows = build_completeness_audit(disease_data, table)
    return audit_rows, compute_audit_summary(audit_rows), disease_name


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------


@app.command()
def compare(
    disease_ref: str = typer.Argument(
        help="Disease slug, MONDO ID, name, or YAML path."
    ),
    output_format: str = typer.Option(
        "tsv", "--format", help="Output format: tsv, json, summary."
    ),
    output: str | None = typer.Option(None, help="Output file path (default: stdout)."),
    no_closure: bool = typer.Option(
        False, "--no-closure", help="Disable HPO closure matching."
    ),
) -> None:
    """Compare dismech phenotypes against OMIM/Orphanet for a single disease."""
    table, venn, disease_name = run_comparison(disease_ref, use_closure=not no_closure)

    if not table:
        raise typer.Exit(1)

    with _open_output(output) as out:
        if output_format == "tsv":
            _write_tsv(table, file=out)
            _write_summary(venn, disease_name)
        elif output_format == "json":
            _write_json(table, venn, file=out)
        elif output_format == "summary":
            _write_summary(venn, disease_name, file=out)
        else:
            typer.echo(f"Unknown format: {output_format}", err=True)
            raise typer.Exit(1)


@app.command()
def audit(
    disease_ref: str = typer.Argument(
        help="Disease slug, MONDO ID, name, or YAML path."
    ),
    output_format: str = typer.Option(
        "tsv", "--format", help="Output format: tsv, json."
    ),
    output: str | None = typer.Option(None, help="Output file path (default: stdout)."),
    no_closure: bool = typer.Option(
        False, "--no-closure", help="Disable HPO closure matching."
    ),
) -> None:
    """Audit one disease for phenotype completeness against OMIM/Orphanet."""
    rows, summary, disease_name = run_audit(disease_ref, use_closure=not no_closure)

    with _open_output(output) as out:
        if output_format == "tsv":
            _write_audit_tsv(rows, file=out)
            typer.echo(
                f"{disease_name}: {summary.get('total_issues', 0)} phenotype-completeness issues",
                err=True,
            )
        elif output_format == "json":
            _write_audit_json(rows, summary, file=out)
        else:
            typer.echo(f"Unknown format: {output_format}", err=True)
            raise typer.Exit(1)


@app.command()
def compare_all(
    output_format: str = typer.Option(
        "tsv", "--format", help="Output format: tsv, json."
    ),
    output: str | None = typer.Option(None, help="Output file path (default: stdout)."),
    no_closure: bool = typer.Option(
        False, "--no-closure", help="Disable HPO closure matching."
    ),
) -> None:
    """Compare all diseases in the KB against OMIM/Orphanet."""
    kb_dir = _default_kb_dir()
    disease_files = _iter_disease_files(kb_dir)

    all_rows: list[dict[str, Any]] = []
    all_venns: dict[str, dict[str, int]] = {}

    # Build a shared resolver for efficiency across diseases
    resolver = HPOClosureResolver() if not no_closure else None

    for disease_path in disease_files:
        slug = disease_path.stem
        disease_data = _load_disease_yaml(disease_path)
        disease_name = disease_data.get("name", slug)
        mondo_id = _get_mondo_id(disease_data)

        if not mondo_id:
            typer.echo(
                f"WARNING: {slug} has no disease_term with MONDO ID, skipping.",
                err=True,
            )
            continue

        dismech_phenos = extract_dismech_phenotypes(disease_data)

        typer.echo(f"Fetching Monarch D2P for {mondo_id} ({disease_name})...", err=True)
        try:
            monarch_items = fetch_monarch_d2p(mondo_id)
        except httpx.HTTPError as exc:
            typer.echo(f"  ERROR fetching {mondo_id}: {exc}", err=True)
            continue

        omim_phenos, ordo_phenos = _parse_monarch_associations(monarch_items)
        typer.echo(
            f"  Found: {len(dismech_phenos)} dismech, {len(omim_phenos)} OMIM, {len(ordo_phenos)} Orphanet",
            err=True,
        )

        table = build_comparison_table(
            mondo_id, disease_name, dismech_phenos, omim_phenos, ordo_phenos, resolver
        )
        venn = compute_venn_summary(table)

        all_rows.extend(table)
        all_venns[slug] = venn

    with _open_output(output) as out:
        if output_format == "tsv":
            _write_tsv(all_rows, file=out)
            # Print per-disease summaries to stderr
            for slug, venn in all_venns.items():
                _write_summary(venn, slug)
        elif output_format == "json":
            combined = {
                "diseases": all_venns,
                "table": all_rows,
                "total_diseases": len(all_venns),
                "total_phenotypes": len(all_rows),
            }
            json.dump(combined, out, indent=2)
            out.write("\n")
        else:
            typer.echo(f"Unknown format: {output_format}", err=True)
            raise typer.Exit(1)


@app.command()
def audit_all(
    output_format: str = typer.Option(
        "tsv", "--format", help="Output format: tsv, json."
    ),
    output: str | None = typer.Option(None, help="Output file path (default: stdout)."),
    no_closure: bool = typer.Option(
        False, "--no-closure", help="Disable HPO closure matching."
    ),
    genetic_only: bool = typer.Option(
        False,
        "--genetic-only",
        help="Only audit entries with a genetic section or genetic/Mendelian category.",
    ),
    limit: int | None = typer.Option(
        None, "--limit", help="Maximum number of disease files to fetch in this run."
    ),
    audit_dir: Path | None = typer.Option(
        None,
        "--audit-dir",
        help="Optional directory for one JSON checkpoint per audited disease.",
    ),
    resume: bool = typer.Option(
        False,
        "--resume",
        help="With --audit-dir, reuse existing per-disease JSON checkpoints.",
    ),
) -> None:
    """Audit all KB diseases for phenotype completeness against OMIM/Orphanet."""
    kb_dir = _default_kb_dir()
    disease_files = _iter_disease_files(kb_dir)

    all_rows: list[dict[str, Any]] = []
    audited = 0
    fetched = 0
    reused = 0
    skipped_non_genetic = 0
    skipped_no_mondo = 0
    errors: list[dict[str, str]] = []

    resolver = HPOClosureResolver() if not no_closure else None

    for disease_path in disease_files:
        slug = disease_path.stem
        disease_data = _load_disease_yaml(disease_path)
        disease_name = disease_data.get("name", slug)
        mondo_id = _get_mondo_id(disease_data)
        checkpoint_path = audit_dir / f"{slug}.json" if audit_dir else None

        if genetic_only and not _is_genetic_disease(disease_data):
            skipped_non_genetic += 1
            continue

        if checkpoint_path and resume and checkpoint_path.exists():
            try:
                payload = _read_disease_audit_payload(checkpoint_path)
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                typer.echo(
                    f"  ERROR reading checkpoint {checkpoint_path}: {exc}", err=True
                )
            else:
                status = str(payload.get("status", ""))
                if status == "ok":
                    all_rows.extend(payload.get("issues", []) or [])
                    audited += 1
                    reused += 1
                    typer.echo(
                        f"Reusing audit checkpoint for {disease_name} ({slug})",
                        err=True,
                    )
                    continue
                if status == "error":
                    errors.append(
                        {
                            "slug": slug,
                            "disease_name": str(
                                payload.get("disease_name", disease_name)
                            ),
                            "error": str(payload.get("error", "unknown error")),
                        }
                    )
                    reused += 1
                    typer.echo(
                        f"Reusing error checkpoint for {disease_name} ({slug})",
                        err=True,
                    )
                    continue

        if not mondo_id:
            skipped_no_mondo += 1
            typer.echo(
                f"WARNING: {slug} has no disease_term with MONDO ID, skipping.",
                err=True,
            )
            continue

        if limit is not None and fetched >= limit:
            continue

        dismech_phenos = extract_dismech_phenotypes(disease_data)
        typer.echo(f"Fetching Monarch D2P for {mondo_id} ({disease_name})...", err=True)
        try:
            monarch_items = fetch_monarch_d2p(mondo_id)
        except httpx.HTTPError as exc:
            typer.echo(f"  ERROR fetching {mondo_id}: {exc}", err=True)
            errors.append(
                {"slug": slug, "disease_name": str(disease_name), "error": str(exc)}
            )
            if checkpoint_path:
                _write_disease_audit_payload(
                    checkpoint_path,
                    build_disease_audit_payload(
                        slug=slug,
                        source_file=disease_path.name,
                        disease_id=mondo_id,
                        disease_name=str(disease_name),
                        rows=[],
                        status="error",
                        error=str(exc),
                    ),
                )
            fetched += 1
            continue

        omim_phenos, ordo_phenos = _parse_monarch_associations(monarch_items)
        typer.echo(
            f"  Found: {len(dismech_phenos)} dismech, {len(omim_phenos)} OMIM, {len(ordo_phenos)} Orphanet",
            err=True,
        )

        table = build_comparison_table(
            mondo_id, disease_name, dismech_phenos, omim_phenos, ordo_phenos, resolver
        )
        audit_rows = build_completeness_audit(disease_data, table)
        all_rows.extend(audit_rows)
        if checkpoint_path:
            _write_disease_audit_payload(
                checkpoint_path,
                build_disease_audit_payload(
                    slug=slug,
                    source_file=disease_path.name,
                    disease_id=mondo_id,
                    disease_name=str(disease_name),
                    rows=audit_rows,
                ),
            )
        audited += 1
        fetched += 1

    summary = compute_audit_summary(all_rows)
    summary["audited_diseases"] = audited
    summary["fetched_diseases"] = fetched
    summary["reused_checkpoints"] = reused
    summary["skipped_non_genetic_diseases"] = skipped_non_genetic
    summary["skipped_no_mondo_diseases"] = skipped_no_mondo
    summary["error_count"] = len(errors)
    summary["errors"] = errors

    with _open_output(output) as out:
        if output_format == "tsv":
            _write_audit_tsv(all_rows, file=out)
            typer.echo(
                f"Audited {audited} diseases ({fetched} fetched, {reused} reused); found {summary['total_issues']} phenotype-completeness issues.",
                err=True,
            )
        elif output_format == "json":
            _write_audit_json(all_rows, summary, file=out)
        else:
            typer.echo(f"Unknown format: {output_format}", err=True)
            raise typer.Exit(1)


if __name__ == "__main__":
    app()

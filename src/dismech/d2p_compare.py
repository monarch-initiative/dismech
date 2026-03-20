"""Compare dismech disease-to-phenotype annotations against OMIM and Orphanet via the Monarch API."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import httpx
import typer
import yaml
from oaklib import get_adapter

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

_HP_ADAPTER_SPEC = "sqlite:obo:hp"
_MONARCH_ASSOC_URL = "https://api.monarchinitiative.org/v3/api/association"
_D2P_CATEGORY = "biolink:DiseaseToPhenotypicFeatureAssociation"
_PAGE_LIMIT = 500

_SOURCE_OMIM = "infores:omim"
_SOURCE_ORDO = "infores:orphanet"

app = typer.Typer(help="Compare dismech phenotypes against OMIM/Orphanet databases.")

# ---------------------------------------------------------------------------
# Shared helpers (mirrors from phenoagent/matching.py to avoid import coupling)
# ---------------------------------------------------------------------------


def _normalize_hp_id(term_id: str | None) -> str | None:
    """Normalize HPO identifiers to uppercase CURIE form."""
    if not term_id:
        return None
    tid = str(term_id).strip()
    if not tid or ":" not in tid:
        return None
    prefix, local = tid.split(":", 1)
    if prefix.casefold() != "hp":
        return None
    local = local.strip()
    if not local:
        return None
    return f"HP:{local}"


def _default_kb_dir() -> Path:
    return Path(__file__).resolve().parents[2] / "kb" / "disorders"


def _iter_disease_files(kb_dir: Path) -> list[Path]:
    return sorted(p for p in kb_dir.glob("*.yaml") if not p.name.endswith(".history.yaml"))


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
                for a in adapter.ancestors(normalized, predicates=["rdfs:subClassOf"], reflexive=True)
                if isinstance(a, str)
            }
        except Exception:
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
        except Exception:
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

    Returns list of dicts with: hp_id, label, frequency, pmids.
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

        label = raw_term.get("label") or term_desc.get("preferred_term") or item.get("name") or ""
        frequency = str(item.get("frequency", "")) if item.get("frequency") else ""

        pmids: list[str] = []
        for ev in item.get("evidence", []) or []:
            if not isinstance(ev, dict):
                continue
            ref = ev.get("reference", "")
            if ref.upper().startswith("PMID:"):
                pmids.append(ref)

        results.append({
            "hp_id": hp_id,
            "label": label,
            "frequency": frequency,
            "pmids": pmids,
        })

    return results


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

        rows.append({
            "disease_id": mondo_id,
            "disease_name": disease_name,
            "phenotype_id": hp_id,
            "phenotype_label": label,
            "dismech": _format_cell(dismech_match, dismech_rec),
            "omim": _format_cell(omim_match, omim_rec),
            "ordo": _format_cell(ordo_match, ordo_rec),
        })

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


def _load_disease_yaml(path: Path) -> dict[str, Any]:
    with open(path) as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError(f"Disease YAML at {path} must be an object")
    return data


def _get_mondo_id(disease_data: dict[str, Any]) -> str | None:
    dt = disease_data.get("disease_term")
    if not isinstance(dt, dict):
        return None
    term = dt.get("term")
    if not isinstance(term, dict):
        return None
    tid = term.get("id")
    return str(tid) if tid else None


def _resolve_disease_ref(ref: str) -> tuple[str, Path]:
    """Resolve a disease reference to (slug, path), reusing phenoagent logic."""
    from phenoagent.matching import resolve_disease_reference

    return resolve_disease_reference(ref)


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
        typer.echo(f"WARNING: {slug} has no disease_term with MONDO ID, skipping.", err=True)
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


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------


@app.command()
def compare(
    disease_ref: str = typer.Argument(help="Disease slug, MONDO ID, name, or YAML path."),
    format: str = typer.Option("tsv", help="Output format: tsv, json, summary."),
    output: str | None = typer.Option(None, help="Output file path (default: stdout)."),
    no_closure: bool = typer.Option(False, "--no-closure", help="Disable HPO closure matching."),
) -> None:
    """Compare dismech phenotypes against OMIM/Orphanet for a single disease."""
    table, venn, disease_name = run_comparison(disease_ref, use_closure=not no_closure)

    if not table:
        raise typer.Exit(1)

    out_file = open(output, "w") if output else None
    try:
        if format == "tsv":
            _write_tsv(table, file=out_file)
            _write_summary(venn, disease_name)
        elif format == "json":
            _write_json(table, venn, file=out_file)
        elif format == "summary":
            _write_summary(venn, disease_name, file=out_file or sys.stdout)
        else:
            typer.echo(f"Unknown format: {format}", err=True)
            raise typer.Exit(1)
    finally:
        if out_file:
            out_file.close()


@app.command()
def compare_all(
    format: str = typer.Option("tsv", help="Output format: tsv, json."),
    output: str | None = typer.Option(None, help="Output file path (default: stdout)."),
    no_closure: bool = typer.Option(False, "--no-closure", help="Disable HPO closure matching."),
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
            typer.echo(f"WARNING: {slug} has no disease_term with MONDO ID, skipping.", err=True)
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

    out_file = open(output, "w") if output else None
    try:
        if format == "tsv":
            _write_tsv(all_rows, file=out_file)
            # Print per-disease summaries to stderr
            for slug, venn in all_venns.items():
                _write_summary(venn, slug)
        elif format == "json":
            combined = {
                "diseases": all_venns,
                "table": all_rows,
                "total_diseases": len(all_venns),
                "total_phenotypes": len(all_rows),
            }
            out = out_file or sys.stdout
            json.dump(combined, out, indent=2)
            out.write("\n")
        else:
            typer.echo(f"Unknown format: {format}", err=True)
            raise typer.Exit(1)
    finally:
        if out_file:
            out_file.close()


if __name__ == "__main__":
    app()

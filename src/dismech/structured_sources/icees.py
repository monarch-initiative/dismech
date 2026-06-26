"""ICEES KG structured-database source.

Ingests the **ICEES Knowledge Graph** — the KGX-packaged form of the
Integrated Clinical and Environmental Exposures Service (ICEES), a
regulatory-compliant open service from RENCI / UNC Chapel Hill that exposes
single-site EHR data integrated with environmental-exposure data. The KG is
distributed as gzipped KGX node/edge JSON-Lines and is a NCATS Biomedical
Data Translator "exposures provider" (``infores:automat-icees-kg``), the
sibling resource to Columbia Open Health Data (COHD).

This source emits one ``ICEES_<A>__<B>.md`` cache file per **disease/phenotype
pair**, so a comorbidity entry can cite ``ICEES:<A>__<B>`` and quote an
individual cohort chi-square row as an evidence ``snippet:`` — the same
flat-file-row pattern used by the Orphanet and ClinGen sources.

Scope: cache files are generated for pairs whose normalized identifiers are
**both MONDO or HP** (the vocabularies dismech disease/phenotype entries key
on). ICEES disease nodes carry ``equivalent_identifiers`` spanning
MONDO/HP/UMLS/etc., so a node whose primary id is UMLS is normalized to its
MONDO/HP equivalent when one exists. Pairs that cannot be normalized to
MONDO/HP on both sides remain in the index (so an explicit ``--id`` can still
serialize them) but are not emitted by default. Chemical/drug/exposure edges
are intentionally excluded — ``association_signals`` models disease-disease
comorbidity, not exposure-disease association.

Each correlation is symmetric, so subject/object order is dropped and the two
identifiers are sorted to form a single record per unordered pair; cohort
observations are merged and de-duplicated across both edge directions and
across the ``correlated_with`` / ``positively_correlated_with`` /
``negatively_correlated_with`` predicate variants.
"""

from __future__ import annotations

import gzip
import json
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar, Iterable, Iterator

from dismech.structured_sources.base import (
    BulkFile,
    ReferenceCacheEntry,
    StructuredSource,
)

logger = logging.getLogger(__name__)

_NODES_NAME = "nodes.jsonl.gz"
_EDGES_NAME = "edges.jsonl.gz"

# Biolink categories that mark a node as a disease/phenotype for our purposes.
_DISEASE_CATEGORIES = frozenset(
    {
        "biolink:Disease",
        "biolink:DiseaseOrPhenotypicFeature",
        "biolink:PhenotypicFeature",
    }
)

# Identifier prefixes we normalize toward, in priority order, and the prefixes
# a pair must use on both sides to be emitted as a cache file by default.
_PREFERRED_PREFIXES = ("MONDO:", "HP:")

_PREDICATE_SIGN = {
    "biolink:positively_correlated_with": "POSITIVE",
    "biolink:negatively_correlated_with": "NEGATIVE",
    "biolink:correlated_with": "UNSIGNED",
}


@dataclass(frozen=True)
class _CohortStat:
    """One ICEES cohort's chi-square contingency result for a pair."""

    cohort: str
    chi_square: str
    dof: str
    p_value: str
    sample_size: str

    def sort_key(self) -> tuple[str, str]:
        return (self.cohort, self.chi_square)


@dataclass
class _ICEESPairRecord:
    """One disease/phenotype pair with its merged cohort statistics."""

    reference_id: str
    a_id: str
    b_id: str
    a_name: str
    b_name: str
    a_raw: str
    b_raw: str
    predicates: set[str] = field(default_factory=set)
    cohorts: dict[tuple, _CohortStat] = field(default_factory=dict)

    @property
    def sign(self) -> str:
        signs = {_PREDICATE_SIGN.get(p, "UNSIGNED") for p in self.predicates}
        directional = signs - {"UNSIGNED"}
        if directional == {"POSITIVE"}:
            return "POSITIVE"
        if directional == {"NEGATIVE"}:
            return "NEGATIVE"
        if directional == {"POSITIVE", "NEGATIVE"}:
            return "MIXED"
        return "UNSIGNED"

    @property
    def both_mondo_hp(self) -> bool:
        return _is_preferred(self.a_id) and _is_preferred(self.b_id)


class ICEESSource(StructuredSource):
    """Structured source for ICEES KG disease/phenotype correlation pairs."""

    prefix: ClassVar[str] = "ICEES"
    id_pattern: ClassVar[re.Pattern] = re.compile(r"^ICEES:.+__.+$")
    bulk_files: ClassVar[tuple[BulkFile, ...]] = (
        BulkFile(name=_NODES_NAME, url="", sha256="", description="ICEES KG nodes (KGX)"),
        BulkFile(name=_EDGES_NAME, url="", sha256="", description="ICEES KG edges (KGX)"),
    )

    _manifest_snapshot_date: ClassVar[str] = ""
    _manifest_schema_tag: ClassVar[str] = ""
    _manifest_graph_version: ClassVar[str] = ""

    @classmethod
    def load_manifest(cls, manifest_path: Path) -> None:
        """Populate ``bulk_files`` and snapshot metadata from a manifest YAML."""
        from ruamel.yaml import YAML

        yaml = YAML(typ="safe")
        data = yaml.load(manifest_path)
        cls.bulk_files = tuple(
            BulkFile(
                name=entry["name"],
                url=entry.get("url", ""),
                sha256=entry.get("sha256", ""),
                description=entry.get("description", ""),
            )
            for entry in data.get("bulk_files", [])
        )
        cls._manifest_snapshot_date = str(data.get("snapshot_date", ""))
        cls._manifest_schema_tag = str(data.get("schema_tag", ""))
        cls._manifest_graph_version = str(data.get("graph_version", ""))

    # ----- indexing -----

    def _nodes_path(self) -> Path:
        path = self.data_dir / _NODES_NAME
        if path.exists():
            return path
        raise FileNotFoundError(f"{path} not found; run `just icees-refresh` first")

    def _edges_path(self) -> Path:
        path = self.data_dir / _EDGES_NAME
        if path.exists():
            return path
        raise FileNotFoundError(f"{path} not found; run `just icees-refresh` first")

    def _load_nodes(self) -> dict[str, dict]:
        """Map raw KG node id -> {name, is_disease, preferred}."""
        nodes: dict[str, dict] = {}
        with gzip.open(self._nodes_path(), "rt", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                n = json.loads(line)
                cats = n.get("category", [])
                nodes[n["id"]] = {
                    "name": n.get("name") or n["id"],
                    "is_disease": bool(_DISEASE_CATEGORIES.intersection(cats)),
                    "preferred": _preferred_id(
                        n["id"], n.get("equivalent_identifiers", [])
                    ),
                }
        return nodes

    def build_index(self) -> dict[str, _ICEESPairRecord]:
        nodes = self._load_nodes()
        records: dict[str, _ICEESPairRecord] = {}

        with gzip.open(self._edges_path(), "rt", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                edge = json.loads(line)
                subj, obj = edge.get("subject"), edge.get("object")
                s_node, o_node = nodes.get(subj), nodes.get(obj)
                if s_node is None or o_node is None:
                    continue
                if not (s_node["is_disease"] and o_node["is_disease"]):
                    continue
                a_pref, b_pref = s_node["preferred"], o_node["preferred"]
                if a_pref == b_pref:
                    continue

                # Sort the unordered pair so subject/object order does not matter.
                if a_pref <= b_pref:
                    (a_pref, a_raw, a_name), (b_pref, b_raw, b_name) = (
                        (a_pref, subj, s_node["name"]),
                        (b_pref, obj, o_node["name"]),
                    )
                else:
                    (a_pref, a_raw, a_name), (b_pref, b_raw, b_name) = (
                        (b_pref, obj, o_node["name"]),
                        (a_pref, subj, s_node["name"]),
                    )

                ref_id = _pair_reference_id(a_pref, b_pref)
                rec = records.get(ref_id)
                if rec is None:
                    rec = _ICEESPairRecord(
                        reference_id=ref_id,
                        a_id=a_pref,
                        b_id=b_pref,
                        a_name=a_name,
                        b_name=b_name,
                        a_raw=a_raw,
                        b_raw=b_raw,
                        predicates=set(),
                        cohorts={},
                    )
                    records[ref_id] = rec
                if edge.get("predicate"):
                    rec.predicates.add(edge["predicate"])
                for stat in _iter_cohort_stats(edge.get("attributes", [])):
                    key = (
                        stat.cohort,
                        stat.chi_square,
                        stat.dof,
                        stat.p_value,
                        stat.sample_size,
                    )
                    rec.cohorts.setdefault(key, stat)

        return records

    def identifiers(self) -> Iterable[str]:
        idx = self.index()
        return sorted(
            ref_id for ref_id, rec in idx.items() if rec.both_mondo_hp
        )

    @property
    def snapshot_date(self) -> str:
        return type(self)._manifest_snapshot_date

    @property
    def graph_version(self) -> str:
        return type(self)._manifest_graph_version

    # ----- serialization -----

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        ref_id = _normalize_identifier(identifier, self.index())
        rec = self.index().get(ref_id)
        if rec is None:
            raise KeyError(f"{ref_id} not found in ICEES KG index")
        body = "\n".join(self._render_body(rec)) + "\n"
        return ReferenceCacheEntry(
            reference_id=rec.reference_id,
            title=f"{rec.a_name} / {rec.b_name} (ICEES KG)"[:240],
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "ICEES KG"},
        )

    def _render_body(self, rec: _ICEESPairRecord) -> Iterator[str]:
        yield f"# {rec.reference_id}  {rec.a_name} ↔ {rec.b_name}"
        yield ""
        yield (
            f"**{rec.reference_id}** - EHR correlation between "
            f"{rec.a_name} ({rec.a_id}) and {rec.b_name} ({rec.b_id}) "
            "in ICEES KG."
        )
        yield ""

        yield "## Association"
        yield ""
        yield f"- Disorder A: {rec.a_name} ({rec.a_id})"
        if rec.a_raw != rec.a_id:
            yield f"  - ICEES KG node: {rec.a_raw}"
        yield f"- Disorder B: {rec.b_name} ({rec.b_id})"
        if rec.b_raw != rec.b_id:
            yield f"  - ICEES KG node: {rec.b_raw}"
        preds = ", ".join(
            p.removeprefix("biolink:") for p in sorted(rec.predicates)
        )
        yield f"- Predicate(s): {preds or '-'}"
        yield f"- Direction of correlation: {rec.sign}"
        yield ""

        yield "## Cohort statistics"
        yield ""
        yield (
            "Per-cohort chi-square contingency results. ICEES cohorts are "
            "condition-specific UNC Health patient sets (e.g. an asthma or "
            "primary-ciliary-dyskinesia cohort), so each statistic is "
            "conditioned on that base population, not a hospital-wide sample."
        )
        yield ""
        yield from _md_table(
            ["Cohort", "Chi-square", "dof", "p-value", "N"],
            [
                (s.cohort, s.chi_square, s.dof, s.p_value, s.sample_size)
                for s in sorted(rec.cohorts.values(), key=lambda s: s.sort_key())
            ],
        )
        yield ""

        yield "## Source"
        yield ""
        version = self.graph_version or self.snapshot_date or "unknown"
        yield (
            f"ICEES KG (Integrated Clinical and Environmental Exposures Service), "
            f"version **{version}**, provenance `infores:automat-icees-kg`. "
            "Single-site UNC Health EHR integrated with environmental-exposure data; "
            "correlations are not multiple-testing corrected and are computed within "
            "condition-specific cohorts."
        )
        yield ""
        yield (
            "License: ICEES terms "
            "(https://github.com/ExposuresProvider/icees-api-config/blob/master/terms.txt)."
        )
        yield ""
        yield (
            "[ICEES KG]"
            "(https://github.com/NCATSTranslator/Translator-All/wiki/Exposures-Provider-ICEES)"
        )


# ----- helpers -----


def _is_preferred(curie: str) -> bool:
    return curie.startswith(_PREFERRED_PREFIXES)


def _preferred_id(primary: str, equivalent_identifiers: list[str]) -> str:
    """Pick the MONDO (then HP) equivalent identifier, else the primary id."""
    for prefix in _PREFERRED_PREFIXES:
        if primary.startswith(prefix):
            return primary
        for eq in equivalent_identifiers:
            if eq.startswith(prefix):
                return eq
    return primary


def _pair_reference_id(a_curie: str, b_curie: str) -> str:
    """``ICEES:<A>__<B>`` with ``:`` replaced by ``_`` inside each CURIE."""
    a = a_curie.replace(":", "_")
    b = b_curie.replace(":", "_")
    return f"ICEES:{a}__{b}"


def _normalize_identifier(identifier: str, index: dict[str, _ICEESPairRecord]) -> str:
    """Accept a canonical ``ICEES:A__B`` id or a ``CURIE,CURIE`` pair."""
    ident = identifier.strip()
    if ident.startswith("ICEES:"):
        return ident
    # Allow "MONDO:0004907,MONDO:0007079" or whitespace-separated pairs.
    parts = [p for p in re.split(r"[,\s]+", ident) if p]
    if len(parts) == 2:
        a, b = sorted(parts)
        return _pair_reference_id(a, b)
    return ident


def _iter_cohort_stats(attributes: list) -> Iterator[_CohortStat]:
    """Yield one ``_CohortStat`` per ``icees_cohort_identifier`` attribute.

    Each KGX edge attribute is itself a JSON-encoded string; the cohort
    attributes carry a nested ``attributes`` list with the chi-square result.
    """
    for raw in attributes:
        attr = _load_attr(raw)
        if attr is None:
            continue
        if attr.get("attribute_type_id") != "icees_cohort_identifier":
            continue
        nested = {
            sub.get("attribute_type_id"): sub.get("value")
            for sub in attr.get("attributes", [])
            if isinstance(sub, dict)
        }
        yield _CohortStat(
            cohort=_cohort_label(str(attr.get("value", ""))),
            chi_square=_num(nested.get("chi_squared_statistic")),
            dof=_num(nested.get("chi_squared_dof")),
            p_value=_num(nested.get("chi_squared_p")),
            sample_size=_num(nested.get("total_sample_size")),
        )


def _load_attr(raw) -> dict | None:
    if isinstance(raw, dict):
        return raw
    if isinstance(raw, str):
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            return None
        return obj if isinstance(obj, dict) else None
    return None


def _cohort_label(value: str) -> str:
    """First ``|``-delimited segment of a cohort identifier (carries the year)."""
    return value.split("|", 1)[0].strip() or value.strip()


def _num(value) -> str:
    """Stable string rendering: drop a trailing ``.0`` from integral floats."""
    if value is None:
        return "-"
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def _md_table(headers: list[str], rows: list[tuple[str, ...]]) -> Iterator[str]:
    def _esc(cell: str) -> str:
        return cell.replace("|", "\\|") if cell else "-"

    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        yield "| " + " | ".join(_esc(cell) for cell in row) + " |"

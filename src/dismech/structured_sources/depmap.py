"""DepMap (Cancer Dependency Map) structured-database source.

Ingests **synthetic-lethality and selective-dependency relationships** derived
from the Broad Institute's Cancer Dependency Map (DepMap) — genome-scale CRISPR
knockout screens across ~1,000+ cancer cell lines. A gene's *dependency* (Chronos
gene-effect) score measures how essential that gene is for a model's fitness; a
gene that is essential **only in a specific genomic context** (a mutation, a
copy-number loss, a lost paralog, or a lineage) is a *selective dependency*, and
the context→dependency relationship is the functional-genomic definition of
synthetic lethality — the same logic the ``dna_repair_synthetic_lethality``
module already curates from the literature (BRCA-loss → PARP dependency).

This source emits one cache file per relationship so a disorder entry can cite
it as snippet-validated evidence (``evidence_source: IN_VITRO`` — pooled
cell-line CRISPR data, never the sole support for a human phenotype):

- ``DEPMAP:<SYMBOL>`` — a **selective dependency** of one gene, aggregating every
  context in which that gene is selectively essential
  (e.g. ``DEPMAP:PARP1`` selectively essential in BRCA1/2-mutant models).
- ``DEPMAP:<SYMBOL_A>__<SYMBOL_B>`` — a **gene-pair synthetic lethality**
  (paralog SL, collateral lethality, or co-dependency), with the two gene
  symbols sorted so the record is order-independent
  (e.g. ``DEPMAP:MTAP__PRMT5``, ``DEPMAP:SMARCA2__SMARCA4``). The HGNC CURIE for
  each gene is carried in the body as a quotable row for machine linkage.

Input format
------------
Like the CIViC source, the manifest pins a **derived, line-oriented TSV**
(``depmap_synthetic_lethality.tsv``) rather than the multi-hundred-MB
``CRISPRGeneEffect`` matrix. Each row is one observation of a
context-conditioned dependency; the columns are::

    gene_a_symbol  gene_a_hgnc  gene_b_symbol  gene_b_hgnc  relationship
    context  metric_type  metric_value  effect_size  n_models  release

``gene_b_*`` empty → a single-gene selective dependency (``DEPMAP:<A>``);
both present → a gene-pair record (``DEPMAP:<A>__<B>``). Multiple rows for the
same reference id (different contexts / metrics) are aggregated into one cache
file, mirroring how the ICEES source merges per-cohort chi-square rows.

The derivation of this TSV from a pinned DepMap release (differential dependency
between a genomic-feature-positive and -negative group of models) is a separate,
deliberately out-of-scope follow-up — see ``docs/depmap-source.md``. This module
is the ingestion/serialization half; it parses whatever the pinned TSV contains.
"""

from __future__ import annotations

import csv
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

_TSV_NAME = "depmap_synthetic_lethality.tsv"

# Canonical relationship vocabulary (free text is tolerated but normalized to
# upper-case for stable rendering).
_RELATIONSHIPS = frozenset(
    {
        "SELECTIVE_DEPENDENCY",
        "PARALOG_SYNTHETIC_LETHAL",
        "COLLATERAL_LETHAL",
        "CO_DEPENDENCY",
    }
)


@dataclass(frozen=True)
class _Observation:
    """One context-conditioned dependency observation for a record."""

    context: str
    metric_type: str
    metric_value: str
    effect_size: str
    n_models: str

    def sort_key(self) -> tuple[str, str, str]:
        return (self.context, self.metric_type, self.metric_value)


@dataclass
class _DepMapRecord:
    """One selective-dependency or gene-pair record with merged observations."""

    reference_id: str
    a_symbol: str
    a_hgnc: str
    b_symbol: str  # "" for a single-gene selective dependency
    b_hgnc: str
    relationships: set[str] = field(default_factory=set)
    releases: set[str] = field(default_factory=set)
    observations: dict[tuple, _Observation] = field(default_factory=dict)

    @property
    def is_pair(self) -> bool:
        return bool(self.b_symbol)

    def add_observation(self, obs: _Observation) -> None:
        key = (obs.context, obs.metric_type, obs.metric_value, obs.effect_size, obs.n_models)
        self.observations.setdefault(key, obs)


class DepMapSource(StructuredSource):
    """Structured source for DepMap synthetic-lethality / selective dependencies."""

    prefix: ClassVar[str] = "DEPMAP"
    # DEPMAP:SYMBOL or DEPMAP:SYMBOL_A__SYMBOL_B
    id_pattern: ClassVar[re.Pattern] = re.compile(r"^DEPMAP:[^_].*$")
    bulk_files: ClassVar[tuple[BulkFile, ...]] = (
        BulkFile(name=_TSV_NAME, url="", sha256="", description="DepMap synthetic-lethality TSV"),
    )

    _manifest_snapshot_date: ClassVar[str] = ""
    _manifest_schema_tag: ClassVar[str] = ""
    _manifest_release: ClassVar[str] = ""
    _manifest_license: ClassVar[str] = ""
    _manifest_doi: ClassVar[str] = ""

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
        cls._manifest_release = str(data.get("release", ""))
        cls._manifest_license = str(data.get("license", ""))
        cls._manifest_doi = str(data.get("doi", ""))

    # ----- indexing -----

    def _tsv_path(self) -> Path:
        path = self.data_dir / _TSV_NAME
        if path.exists():
            return path
        raise FileNotFoundError(f"{path} not found; run `just depmap-refresh` first")

    def build_index(self) -> dict[str, _DepMapRecord]:
        records: dict[str, _DepMapRecord] = {}
        with self._tsv_path().open("r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            for row in reader:
                a_sym = (row.get("gene_a_symbol") or "").strip()
                if not a_sym:
                    continue
                b_sym = (row.get("gene_b_symbol") or "").strip()
                a_hgnc = _norm_hgnc(row.get("gene_a_hgnc"))
                b_hgnc = _norm_hgnc(row.get("gene_b_hgnc"))

                ref_id, a_sym, a_hgnc, b_sym, b_hgnc = _record_identity(
                    a_sym, a_hgnc, b_sym, b_hgnc
                )
                rec = records.get(ref_id)
                if rec is None:
                    rec = _DepMapRecord(
                        reference_id=ref_id,
                        a_symbol=a_sym,
                        a_hgnc=a_hgnc,
                        b_symbol=b_sym,
                        b_hgnc=b_hgnc,
                    )
                    records[ref_id] = rec

                rel = (row.get("relationship") or "").strip().upper()
                if rel:
                    rec.relationships.add(rel)
                release = (row.get("release") or "").strip()
                if release:
                    rec.releases.add(release)
                rec.add_observation(
                    _Observation(
                        context=(row.get("context") or "").strip() or "-",
                        metric_type=(row.get("metric_type") or "").strip() or "-",
                        metric_value=_num(row.get("metric_value")),
                        effect_size=_num(row.get("effect_size")),
                        n_models=_num(row.get("n_models")),
                    )
                )
        return records

    def identifiers(self) -> Iterable[str]:
        return sorted(self.index().keys())

    @property
    def snapshot_date(self) -> str:
        return type(self)._manifest_snapshot_date

    @property
    def release(self) -> str:
        return type(self)._manifest_release

    # ----- serialization -----

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        ref_id = _normalize_identifier(identifier)
        rec = self.index().get(ref_id)
        if rec is None:
            raise KeyError(f"{ref_id} not found in DepMap index")
        body = "\n".join(self._render_body(rec)) + "\n"
        if rec.is_pair:
            title = f"{rec.a_symbol}-{rec.b_symbol} synthetic lethality (DepMap)"
        else:
            title = f"{rec.a_symbol} selective dependency (DepMap)"
        return ReferenceCacheEntry(
            reference_id=rec.reference_id,
            title=title[:240],
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "DepMap"},
        )

    def _render_body(self, rec: _DepMapRecord) -> Iterator[str]:
        rels = ", ".join(sorted(rec.relationships)) or "-"
        if rec.is_pair:
            yield f"# {rec.reference_id}  {rec.a_symbol} ↔ {rec.b_symbol}"
            yield ""
            yield (
                f"**{rec.reference_id}** - DepMap CRISPR gene-dependency "
                f"relationship between {rec.a_symbol} and {rec.b_symbol}."
            )
        else:
            yield f"# {rec.reference_id}  {rec.a_symbol} selective dependency"
            yield ""
            yield (
                f"**{rec.reference_id}** - DepMap CRISPR selective dependency "
                f"of {rec.a_symbol}."
            )
        yield ""

        yield "## Dependency"
        yield ""
        yield f"- Gene A: {rec.a_symbol}" + (f" ({rec.a_hgnc})" if rec.a_hgnc else "")
        if rec.is_pair:
            yield f"- Gene B: {rec.b_symbol}" + (f" ({rec.b_hgnc})" if rec.b_hgnc else "")
        yield f"- Relationship: {rels}"
        yield ""

        yield "## Selective dependency statistics"
        yield ""
        yield (
            "Per-context DepMap CRISPR gene-effect statistics. A more negative "
            "gene-effect (Chronos) score means stronger dependency; a "
            "differential-dependency metric compares the context-positive and "
            "context-negative model groups. Values are from pooled cancer "
            "cell-line screens (IN_VITRO), are not corrected for the number of "
            "genes/contexts tested, and require orthogonal validation before "
            "clinical inference."
        )
        yield ""
        yield from _md_table(
            ["Context", "Metric", "Value", "Effect size", "N models"],
            [
                (o.context, o.metric_type, o.metric_value, o.effect_size, o.n_models)
                for o in sorted(rec.observations.values(), key=lambda o: o.sort_key())
            ],
        )
        yield ""

        yield "## Source"
        yield ""
        release = self.release or self.snapshot_date or "unknown release"
        observed_releases = ", ".join(sorted(rec.releases))
        release_note = f" (observations from {observed_releases})" if observed_releases else ""
        license_ = type(self)._manifest_license or "CC BY 4.0"
        doi = type(self)._manifest_doi
        yield (
            f"Cancer Dependency Map (DepMap), Broad Institute, release "
            f"**{release}**{release_note}. Genome-scale CRISPR knockout "
            "dependency screens across cancer cell lines; selective "
            "dependencies and gene-pair synthetic lethality are derived by "
            "differential dependency analysis. License: "
            f"{license_}."
        )
        yield ""
        if doi:
            yield f"DOI: {doi}"
            yield ""
        yield "[DepMap portal](https://depmap.org/portal/)"


# ----- helpers -----


def _norm_hgnc(value) -> str:
    """Normalize an HGNC identifier to the repo's lowercase ``hgnc:NNN`` form."""
    s = (value or "").strip()
    if not s:
        return ""
    m = re.match(r"^hgnc:?(\d+)$", s, re.IGNORECASE)
    if m:
        return f"hgnc:{m.group(1)}"
    return s


def _record_identity(
    a_sym: str, a_hgnc: str, b_sym: str, b_hgnc: str
) -> tuple[str, str, str, str, str]:
    """Return ``(reference_id, a_sym, a_hgnc, b_sym, b_hgnc)``.

    For a gene pair the two genes are sorted by symbol so the record is
    order-independent; for a single-gene dependency ``b_*`` are empty.
    """
    if b_sym:
        if a_sym.upper() <= b_sym.upper():
            first, first_h, second, second_h = a_sym, a_hgnc, b_sym, b_hgnc
        else:
            first, first_h, second, second_h = b_sym, b_hgnc, a_sym, a_hgnc
        ref_id = f"DEPMAP:{first}__{second}"
        return ref_id, first, first_h, second, second_h
    return f"DEPMAP:{a_sym}", a_sym, a_hgnc, "", ""


def _normalize_identifier(identifier: str) -> str:
    """Accept ``DEPMAP:A``, ``DEPMAP:A__B``, ``A``, ``A,B``, or ``A__B``."""
    ident = identifier.strip()
    ident = ident.removeprefix("DEPMAP:")
    if "__" in ident:
        parts = ident.split("__", 1)
    elif "," in ident:
        parts = [p.strip() for p in ident.split(",", 1)]
    else:
        parts = [ident]
    parts = [p for p in parts if p]
    if len(parts) == 2:
        a, b = sorted(parts, key=str.upper)
        return f"DEPMAP:{a}__{b}"
    return f"DEPMAP:{parts[0]}" if parts else "DEPMAP:"


def _num(value) -> str:
    """Stable string rendering: drop a trailing ``.0`` from integral floats."""
    s = (str(value).strip() if value is not None else "")
    if not s:
        return "-"
    try:
        f = float(s)
    except ValueError:
        return s
    if f.is_integer():
        return str(int(f))
    return s


def _md_table(headers: list[str], rows: list[tuple[str, ...]]) -> Iterator[str]:
    def _esc(cell: str) -> str:
        return cell.replace("|", "\\|") if cell else "-"

    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        yield "| " + " | ".join(_esc(cell) for cell in row) + " |"

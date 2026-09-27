"""STRchive structured-database source.

Ingests **STRchive** (https://strchive.org) — a centralized, actively
maintained catalog of the tandem-repeat (TR / short-tandem-repeat, STR) loci
that cause human disease when they expand. STRchive consolidates locus-level
facts that were previously scattered across STRipy, GeneReviews, OMIM,
gnomAD, and the primary literature: the repeat motif, the benign /
intermediate / pathogenic repeat-count thresholds, the genomic coordinates on
three reference builds, the disease it causes, the inheritance mode, the
molecular mechanism (loss-of-function, gain-of-function, RNA toxicity,
methylation, …), age of onset, prevalence, and disease-ontology cross-
references (OMIM / MONDO / Orphanet / MedGen / GARD).

This source emits one ``STRCHIVE_<locus_id>.md`` cache file per locus (e.g.
``STRCHIVE_SCA3_ATXN3.md``), so a disorder entry can cite ``STRCHIVE:<locus>``
and quote an individual row — a pathogenic-repeat-count threshold, the repeat
motif, or a cross-reference — as an evidence ``snippet:`` that validates as an
exact substring of the cached body, the same flat-file-row pattern used by the
Orphanet, ClinGen, and ICEES sources.

The bulk source is the single ``STRchive-loci.json`` array published in the
STRchive GitHub repository; it is pinned by sha256 in
``data/strchive/MANIFEST.yaml`` and is gitignored. The high-volume
``additional_literature`` field (hundreds of tracking PMIDs per locus) is
intentionally excluded from the cache body — it is a bibliographic index, not
per-row citable evidence — while the curated ``references`` list is kept.

STRchive is distributed under CC BY 4.0.
"""

from __future__ import annotations

import json
import logging
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar

from dismech.structured_sources.base import (
    BulkFile,
    ReferenceCacheEntry,
    StructuredSource,
)

logger = logging.getLogger(__name__)

_LOCI_NAME = "STRchive-loci.json"

# Human-readable expansion of STRchive's terse inheritance codes.
_INHERITANCE_LABELS = {
    "AD": "Autosomal dominant",
    "AR": "Autosomal recessive",
    "XR": "X-linked recessive",
    "XD": "X-linked dominant",
    "XL": "X-linked",
    "MT": "Mitochondrial",
}


@dataclass
class _Locus:
    """One STRchive locus record (the raw JSON dict, wrapped)."""

    locus_id: str
    data: dict

    @property
    def reference_id(self) -> str:
        return f"STRCHIVE:{self.locus_id}"


class StrchiveSource(StructuredSource):
    """Structured source for STRchive tandem-repeat disease loci."""

    prefix: ClassVar[str] = "STRCHIVE"
    id_pattern: ClassVar[re.Pattern] = re.compile(r"^(STRCHIVE:)?[A-Za-z0-9_.-]+$")
    bulk_files: ClassVar[tuple[BulkFile, ...]] = (
        BulkFile(name=_LOCI_NAME, url="", sha256="", description="STRchive loci JSON"),
    )

    _manifest_snapshot_date: ClassVar[str] = ""
    _manifest_version: ClassVar[str] = ""

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
        cls._manifest_version = str(data.get("strchive_version", ""))

    # ----- indexing -----

    def _loci_path(self) -> Path:
        path = self.data_dir / _LOCI_NAME
        if path.exists():
            return path
        raise FileNotFoundError(f"{path} not found; run `just strchive-refresh` first")

    def build_index(self) -> dict[str, _Locus]:
        with self._loci_path().open(encoding="utf-8") as fh:
            records = json.load(fh)
        index: dict[str, _Locus] = {}
        for rec in records:
            locus_id = rec.get("id")
            if not locus_id:
                continue
            index[locus_id] = _Locus(locus_id=locus_id, data=rec)
        return index

    def identifiers(self) -> Iterable[str]:
        return sorted(f"STRCHIVE:{lid}" for lid in self.index())

    @property
    def snapshot_date(self) -> str:
        return type(self)._manifest_snapshot_date

    @property
    def version(self) -> str:
        return type(self)._manifest_version

    # ----- serialization -----

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        locus_id = identifier.split(":", 1)[1] if identifier.startswith("STRCHIVE:") else identifier
        rec = self.index().get(locus_id)
        if rec is None:
            raise KeyError(f"STRCHIVE:{locus_id} not found in STRchive index")
        d = rec.data
        title = f"{d.get('gene', '?')} — {d.get('disease', locus_id)}"
        body = "\n".join(self._render_body(rec)) + "\n"
        return ReferenceCacheEntry(
            reference_id=rec.reference_id,
            title=title[:240],
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "STRchive"},
        )

    def _render_body(self, rec: _Locus) -> Iterator[str]:
        d = rec.data
        gene = d.get("gene", "?")
        disease = d.get("disease", "")

        yield f"# {rec.reference_id}  {gene} — {disease}"
        yield ""
        yield (
            f"**{rec.reference_id}** — STRchive tandem-repeat disease locus "
            f"`{rec.locus_id}` ({gene}, {disease})."
        )
        yield ""

        # ----- Locus identity -----
        yield "## Locus"
        yield ""
        for label, value in [
            ("STRchive ID", rec.locus_id),
            ("Gene", gene),
            ("Gene strand", d.get("gene_strand")),
            ("Disease", disease),
            ("Disease abbreviation", d.get("disease_id")),
            ("Location type", d.get("type")),
            ("Location in gene", d.get("location_in_gene")),
            ("Inheritance", self._inheritance(d.get("inheritance"))),
            ("Mechanism", d.get("mechanism")),
        ]:
            if _present(value):
                yield f"- {label}: {value}"
        yield ""

        # ----- Repeat -----
        yield "## Repeat"
        yield ""
        yield from _md_table(
            ["Field", "Value"],
            [
                row
                for row in [
                    ("Reference motif (reference orientation)", _join(d.get("reference_motif_reference_orientation"))),
                    ("Pathogenic motif (reference orientation)", _join(d.get("pathogenic_motif_reference_orientation"))),
                    ("Pathogenic motif (gene orientation)", _join(d.get("pathogenic_motif_gene_orientation"))),
                    ("Benign motif (reference orientation)", _join(d.get("benign_motif_reference_orientation"))),
                    ("Motif length (bp)", _num(d.get("motif_len"))),
                    ("Locus structure", d.get("locus_structure")),
                    ("Reference copies", _num(d.get("ref_copies"))),
                ]
                if _present(row[1])
            ],
        )
        yield ""

        # ----- Repeat-count thresholds -----
        threshold_rows = [
            ("Benign", _num(d.get("benign_min")), _num(d.get("benign_max"))),
            ("Intermediate", _num(d.get("intermediate_min")), _num(d.get("intermediate_max"))),
            ("Pathogenic", _num(d.get("pathogenic_min")), _num(d.get("pathogenic_max"))),
        ]
        if any(_present(lo) or _present(hi) for _, lo, hi in threshold_rows):
            yield "## Repeat-count thresholds"
            yield ""
            yield (
                "Allele repeat counts (number of motif copies) by pathogenicity "
                "category. Bounds are inclusive as reported by STRchive; a blank "
                "bound is unbounded or not documented."
            )
            yield ""
            yield from _md_table(
                ["Category", "Min copies", "Max copies"],
                [
                    (cat, lo if _present(lo) else "-", hi if _present(hi) else "-")
                    for cat, lo, hi in threshold_rows
                ],
            )
            yield ""

        # ----- Genomic coordinates -----
        coord_rows = [
            ("hg38", d.get("chrom"), d.get("start_hg38"), d.get("stop_hg38")),
            ("hg19", d.get("chrom"), d.get("start_hg19"), d.get("stop_hg19")),
            ("T2T-chm13", d.get("chrom"), d.get("start_t2t"), d.get("stop_t2t")),
        ]
        if any(_present(s) for _, _, s, _ in coord_rows):
            yield "## Genomic coordinates"
            yield ""
            yield from _md_table(
                ["Build", "Chrom", "Start", "Stop"],
                [
                    (build, chrom or "-", _num(start), _num(stop))
                    for build, chrom, start, stop in coord_rows
                    if _present(start)
                ],
            )
            yield ""

        # ----- Disease description -----
        if _present(d.get("disease_description")):
            yield "## Disease description"
            yield ""
            yield str(d["disease_description"])
            yield ""

        # ----- Mechanism detail -----
        if _present(d.get("mechanism_detail")):
            yield "## Mechanism"
            yield ""
            yield str(d["mechanism_detail"])
            yield ""

        # ----- Onset -----
        if _present(d.get("age_onset")):
            yield "## Age of onset"
            yield ""
            yield str(d["age_onset"])
            yield ""

        # ----- Prevalence -----
        if _present(d.get("prevalence")) or _present(d.get("prevalence_details")):
            yield "## Prevalence"
            yield ""
            if _present(d.get("prevalence")):
                yield f"- Prevalence: {d['prevalence']}"
            if _present(d.get("prevalence_details")):
                yield f"- Details: {d['prevalence_details']}"
            yield ""

        # ----- Additional details -----
        if _present(d.get("details")):
            yield "## Details"
            yield ""
            yield str(d["details"])
            yield ""

        # ----- Tags -----
        locus_tags = d.get("locus_tags") or []
        disease_tags = d.get("disease_tags") or []
        if locus_tags or disease_tags:
            yield "## Tags"
            yield ""
            if locus_tags:
                yield f"- Locus tags: {', '.join(locus_tags)}"
            if disease_tags:
                yield f"- Disease tags: {', '.join(disease_tags)}"
            yield ""

        # ----- Cross-references -----
        xref_rows = list(self._xref_rows(d))
        if xref_rows:
            yield "## Cross-references"
            yield ""
            yield from _md_table(["Database", "ID"], xref_rows)
            yield ""

        # ----- References (curated list only, not additional_literature) -----
        refs = d.get("references") or []
        if refs:
            yield "## References"
            yield ""
            for ref in refs:
                yield f"- {ref}"
            yield ""

        # ----- Source -----
        yield "## Source"
        yield ""
        version = self.version or "unknown"
        date = self.snapshot_date or "unknown"
        yield (
            f"STRchive (https://strchive.org), version **{version}** "
            f"(snapshot {date}). A centralized catalog of tandem-repeat disease "
            "loci. Content is for research use and does not constitute medical "
            "guidance."
        )
        yield ""
        yield (
            "License: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). "
            "This record is a reformatted and field-subset rendering of one "
            "locus from the STRchive `STRchive-loci.json` catalog; the source "
            "data are unmodified in substance."
        )
        yield ""
        yield "[STRchive](https://strchive.org) · [source repository](https://github.com/hdashnow/STRchive)"

    # ----- helpers -----

    @staticmethod
    def _inheritance(codes) -> str:
        if not codes:
            return ""
        parts = []
        for code in codes:
            label = _INHERITANCE_LABELS.get(code)
            parts.append(f"{code} ({label})" if label else code)
        return ", ".join(parts)

    @staticmethod
    def _xref_rows(d: dict) -> Iterator[tuple[str, str]]:
        # (JSON key, display database, per-id CURIE prefix)
        specs = [
            ("mondo", "MONDO", "MONDO:"),
            ("omim", "OMIM", "OMIM:"),
            ("orphanet", "Orphanet", "ORPHA:"),
            ("medgen", "MedGen", ""),
            ("gard", "GARD", ""),
            ("malacard", "MalaCards", ""),
            ("genereviews", "GeneReviews", ""),
            ("gnomad", "gnomAD", ""),
            ("stripy", "STRipy", ""),
            ("tr_atlas", "TR-Atlas", ""),
        ]
        for key, db, curie_prefix in specs:
            for value in d.get(key) or []:
                yield (db, f"{curie_prefix}{value}")


def _present(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) > 0
    return True


def _join(value) -> str:
    if not value:
        return ""
    if isinstance(value, (list, tuple)):
        return ", ".join(str(v) for v in value)
    return str(value)


def _num(value) -> str:
    """Stable string rendering: drop a trailing ``.0`` from integral floats."""
    if value is None or value == "":
        return ""
    if isinstance(value, bool):
        return str(value)
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def _md_table(headers: list[str], rows: list[tuple[str, ...]]) -> Iterator[str]:
    def _esc(cell: str) -> str:
        cell = "" if cell is None else str(cell)
        return cell.replace("|", "\\|") if cell else "-"

    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        yield "| " + " | ".join(_esc(cell) for cell in row) + " |"

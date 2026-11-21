"""IMPC structured-database source.

Ingests three per-release reports from the **International Mouse Phenotyping
Consortium** (https://www.mousephenotype.org) and emits one cache record per
mouse gene, ``references_cache/IMPC_MGI_<n>.md``, citable as
``IMPC:MGI:<n>``. The record holds what IMPC found for that gene's knockout
lines, in three quotable tables:

- **Viability**: the primary viability call for each colony and zygosity
  (``viability.csv.gz``).
- **Phenotyping coverage**: for each colony, zygosity and life stage, which
  top-level MP systems were *tested* and which gave a *significant* call
  (``procedureCompletenessAndPhenotypeHits.csv.gz``). This is what separates
  "IMPC tested this system and found nothing" from "IMPC never tested it",
  which a list of significant calls alone cannot.
- **Significant phenotype calls**: every row of
  ``genotype-phenotype-assertions-ALL.csv.gz`` for the gene, one per MP term,
  procedure parameter, zygosity, sex and colony.

The reports are versioned by IMPC data release
(``all-data-releases/release-<n>/results/``), so unlike the rolling-URL
sources the pin in ``data/impc/MANIFEST.yaml`` names a release that does not
change underneath it. A new release is adopted by editing the manifest's URLs
and release number, then ``just impc-refresh --repin`` and ``just
impc-rebuild``.

Only genes a KB entry cites need a cache file: ``just fetch-reference
IMPC:MGI:<n>`` builds one on demand. Rebuilding every gene (~9,900) is
possible but is not what the committed cache is for.

IMPC content is licensed under CC BY 4.0.
"""

from __future__ import annotations

import csv
import gzip
import re
from collections import defaultdict
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar

from dismech.structured_sources.base import (
    BulkFile,
    MissingBulkDataError,
    ReferenceCacheEntry,
    StructuredSource,
)

_ASSERTIONS = "genotype-phenotype-assertions-ALL.csv.gz"
_COMPLETENESS = "procedureCompletenessAndPhenotypeHits.csv.gz"
_VIABILITY = "viability.csv.gz"

_GENE_PAGE = "https://www.mousephenotype.org/data/genes/"
_MGI_RE = re.compile(r"(?:MGI[:_])?(\d+)$", re.IGNORECASE)


@dataclass
class _Call:
    mp_id: str
    mp_name: str
    procedure: str
    parameter: str
    zygosity: str
    sex: str
    p_value: str
    effect_size: str
    center: str
    allele: str
    resource: str

    def row(self) -> str:
        cells = [
            self.mp_id,
            self.mp_name,
            self.procedure,
            self.parameter,
            self.zygosity,
            self.sex,
            self.p_value or "-",
            self.effect_size or "-",
            self.center,
            self.allele,
            self.resource,
        ]
        return "| " + " | ".join(_cell(c) for c in cells) + " |"

    def sort_key(self) -> tuple:
        return (
            self.mp_id,
            self.procedure,
            self.parameter,
            self.zygosity,
            self.sex,
            self.allele,
            self.center,
        )


@dataclass
class _Coverage:
    colony: str
    allele: str
    zygosity: str
    life_stage: str
    center: str
    tested: tuple[str, ...]
    significant: tuple[str, ...]
    procedures_tested: int
    procedures: tuple[str, ...] = ()

    def row(self) -> str:
        cells = [
            self.allele,
            self.colony,
            self.zygosity,
            self.life_stage,
            self.center,
            str(self.procedures_tested),
            "; ".join(self.procedures) or "none",
            "; ".join(self.tested) or "none",
            "; ".join(self.significant) or "none",
        ]
        return "| " + " | ".join(_cell(c) for c in cells) + " |"

    def sort_key(self) -> tuple:
        return (self.allele, self.zygosity, self.life_stage, self.colony, self.center)


@dataclass
class _Viability:
    allele: str
    colony: str
    zygosity: str
    call: str
    center: str
    pups: str
    hom_fraction: str

    def row(self) -> str:
        cells = [
            self.allele,
            self.colony,
            self.zygosity,
            self.call,
            self.pups or "-",
            _fraction(self.hom_fraction),
            self.center,
        ]
        return "| " + " | ".join(_cell(c) for c in cells) + " |"

    def sort_key(self) -> tuple:
        return (self.allele, self.zygosity, self.colony, self.center)


@dataclass
class _Gene:
    mgi: str
    symbol: str = ""
    calls: list[_Call] = field(default_factory=list)
    coverage: list[_Coverage] = field(default_factory=list)
    viability: list[_Viability] = field(default_factory=list)

    @property
    def reference_id(self) -> str:
        return f"IMPC:{self.mgi}"


class IMPCSource(StructuredSource):
    """Structured source for IMPC knockout phenotyping, one record per gene."""

    prefix: ClassVar[str] = "IMPC"
    id_pattern: ClassVar[re.Pattern] = re.compile(
        r"^(IMPC[:_])?(MGI[:_])?\d+$", re.IGNORECASE
    )
    bulk_files: ClassVar[tuple[BulkFile, ...]] = ()
    _manifest_release: ClassVar[str] = ""
    _manifest_snapshot_date: ClassVar[str] = ""

    @classmethod
    def load_manifest(cls, manifest_path: Path) -> None:
        from ruamel.yaml import YAML

        data = YAML(typ="safe").load(manifest_path)
        cls.bulk_files = tuple(
            BulkFile(
                name=entry["name"],
                url=entry["url"],
                sha256=entry.get("sha256", ""),
                description=entry.get("description", ""),
            )
            for entry in data.get("bulk_files", [])
        )
        cls._manifest_release = str(data.get("data_release", ""))
        cls._manifest_snapshot_date = str(data.get("snapshot_date", ""))

    @property
    def release(self) -> str:
        return type(self)._manifest_release

    @property
    def snapshot_date(self) -> str:  # type: ignore[override]
        return type(self)._manifest_snapshot_date

    # ----- indexing -----

    def _path(self, name: str) -> Path:
        return self.data_dir / name

    def build_index(self) -> dict[str, _Gene]:
        missing = [
            n
            for n in (_ASSERTIONS, _COMPLETENESS, _VIABILITY)
            if not self._path(n).exists()
        ]
        if missing:
            raise MissingBulkDataError(
                source="IMPC",
                data_dir=self.data_dir,
                missing=missing,
                remedy="just impc-refresh",
            )
        genes: dict[str, _Gene] = {}

        def gene(mgi: str, symbol: str) -> _Gene:
            g = genes.get(mgi)
            if g is None:
                g = genes[mgi] = _Gene(mgi=mgi)
            if symbol and not g.symbol:
                g.symbol = symbol
            return g

        for r in _read(self._path(_ASSERTIONS)):
            mgi = _clean(r.get("marker_accession_id"))
            if not mgi.startswith("MGI:"):
                continue
            gene(mgi, _clean(r.get("marker_symbol"))).calls.append(
                _Call(
                    mp_id=_clean(r.get("mp_term_id")),
                    mp_name=_clean(r.get("mp_term_name")),
                    procedure=_clean(r.get("procedure_name")),
                    parameter=_clean(r.get("parameter_name")),
                    zygosity=_clean(r.get("zygosity")),
                    sex=_clean(r.get("sex")),
                    p_value=_clean(r.get("p_value")),
                    effect_size=_clean(r.get("effect_size")),
                    center=_clean(r.get("phenotyping_center")),
                    allele=_clean(r.get("allele_symbol")),
                    resource=_clean(r.get("resource_name")),
                )
            )

        for r in _read(self._path(_COMPLETENESS)):
            mgi = _clean(r.get("Gene Accession Id"))
            if not mgi.startswith("MGI:"):
                continue
            gene(mgi, _clean(r.get("Gene Symbol"))).coverage.append(
                _Coverage(
                    colony=_clean(r.get("Colony Id")),
                    allele=_clean(r.get("Allele Symbol")),
                    zygosity=_clean(r.get("Zygosity")),
                    life_stage=_clean(r.get("Life Stage")),
                    center=_clean(r.get("Phenotyping Center")),
                    tested=_systems(r.get("Top-level MP Name: Successful")),
                    significant=_systems(r.get("Top-level MP Name: Significant")),
                    procedures_tested=_int(r.get("Procedure Count: Successful")),
                    procedures=_systems(r.get("Procedure Name: Successful")),
                )
            )

        for r in _read(self._path(_VIABILITY)):
            mgi = _clean(r.get("Gene Accession Id"))
            if not mgi.startswith("MGI:"):
                continue
            gene(mgi, _clean(r.get("Gene Symbol"))).viability.append(
                _Viability(
                    allele=_clean(r.get("Allele Symbol")),
                    colony=_clean(r.get("Colony Id")),
                    zygosity=_clean(r.get("Zygosity")),
                    call=_clean(r.get("Viability Phenotype HOMs/HEMIs"))
                    or _clean(r.get("Supporting Data")),
                    center=_clean(r.get("Phenotyping Center")),
                    pups=_clean(r.get("Total # Pups")),
                    hom_fraction=_clean(r.get("Percentage HOMs / HEMs")),
                )
            )
        return genes

    def identifiers(self) -> Iterable[str]:
        return sorted(
            (g.reference_id for g in self.index().values()),
            key=lambda ref: int(ref.rsplit(":", 1)[1]),
        )

    # ----- serialization -----

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        mgi = normalize_identifier(identifier)
        g = self.index().get(mgi)
        if g is None:
            raise KeyError(f"IMPC:{mgi} not found in IMPC release {self.release}")
        title = f"IMPC knockout phenotyping of {g.symbol} ({g.mgi})"
        body = "\n".join(self._body(g)) + "\n"
        return ReferenceCacheEntry(
            reference_id=g.reference_id,
            title=title,
            body=body,
            content_type="structured_record",
            extra_frontmatter={
                "database": "IMPC",
                "license": "CC BY 4.0",
                "source_snapshot": f"release-{self.release} ({self.snapshot_date})",
            },
        )

    def _body(self, g: _Gene) -> list[str]:
        lines = [
            f"# {g.reference_id}",
            "",
            f"**{g.reference_id}** — IMPC knockout phenotyping of {g.symbol}",
            "",
            "## Gene",
            "",
            f"- Symbol: {g.symbol}",
            f"- MGI: {g.mgi}",
            f"- IMPC gene page: {_GENE_PAGE}{g.mgi}",
            "",
            "## Viability",
            "",
        ]
        if g.viability:
            lines += [
                "| Allele | Colony | Zygosity | Viability call | Pups | Homozygote fraction | Centre |",
            ]
            for v in sorted(g.viability, key=lambda x: x.sort_key()):
                lines.append(v.row())
        else:
            lines.append("No viability record in this release.")
        lines += [
            "",
            "## Phenotyping coverage",
            "",
            "Procedures successfully run, top-level MP systems with at least one "
            "successfully processed parameter (tested) and with at least one "
            "significant call (significant), per colony, zygosity and life stage.",
            "",
        ]
        if g.coverage:
            lines.append(
                "| Allele | Colony | Zygosity | Life stage | Centre | Procedures tested | Procedures | Systems tested | Systems significant |"
            )
            for c in sorted(g.coverage, key=lambda x: x.sort_key()):
                lines.append(c.row())
        else:
            lines.append("No phenotyping-coverage record in this release.")
        lines += ["", "## Significant phenotype calls", ""]
        if g.calls:
            lines.append(
                "| MP term | MP name | Procedure | Parameter | Zygosity | Sex | p-value | Effect size | Centre | Allele | Resource |"
            )
            seen = set()
            for c in sorted(g.calls, key=lambda x: x.sort_key()):
                row = c.row()
                if row not in seen:
                    seen.add(row)
                    lines.append(row)
        else:
            lines.append("No significant phenotype call in this release.")
        lines += [
            "",
            "## Source",
            "",
            "- Database: International Mouse Phenotyping Consortium (IMPC)",
            f"- Data release: {self.release} ({self.snapshot_date})",
            f"- Reports: {_ASSERTIONS}, {_COMPLETENESS}, {_VIABILITY}",
            "- License: CC BY 4.0",
        ]
        return lines


def normalize_identifier(identifier: str) -> str:
    """Return ``MGI:<n>`` for any accepted spelling of an IMPC gene id."""
    value = identifier.strip()
    if value.upper().startswith("IMPC"):
        value = value[4:].lstrip(":_")
    m = _MGI_RE.match(value)
    if not m:
        raise ValueError(f"cannot parse IMPC identifier: {identifier}")
    return f"MGI:{m.group(1)}"


def _read(path: Path) -> Iterable[dict[str, str]]:
    with gzip.open(path, "rt", encoding="utf-8", newline="") as fh:
        yield from csv.DictReader(fh)


def _clean(value: str | None) -> str:
    return " ".join(str(value or "").split())


def _cell(value: str) -> str:
    return value.replace("|", "/")


def _systems(value: str | None) -> tuple[str, ...]:
    v = _clean(value)
    if not v or v == "None":
        return ()
    return tuple(sorted({s.strip() for s in v.split("|") if s.strip()}))


def _int(value: str | None) -> int:
    try:
        return int(_clean(value))
    except ValueError:
        return 0


def _fraction(value: str) -> str:
    try:
        return f"{float(value):.2f}"
    except ValueError:
        return value or "-"

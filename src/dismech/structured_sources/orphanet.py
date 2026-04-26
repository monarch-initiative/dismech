"""Orphanet structured-database source.

Ingests the public Orphadata XML products (CC-BY 4.0) and emits one
``ORPHA_<code>.md`` cache file per disorder. The body is a deterministic,
line-oriented rendering inspired by UniProt's flat-file format so curators
can quote individual rows as evidence ``snippet:`` values.

Products merged:

    en_product1.xml       — names, synonyms, definitions, external xrefs
    en_product4.xml       — HPO phenotype associations + frequency
    en_product6.xml       — gene-disease associations
    en_product9_prev.xml  — prevalence / epidemiology
    en_product9_ages.xml  — age of onset, inheritance, age of death

Filtering: only ``DisorderGroup ∈ {"Disorder", "Subtype of disorder"}`` is
emitted. Pure ontology scaffolding (``DisorderType = "Category"``) and
parent grouping nodes (``Group of disorders``) are skipped.
"""

from __future__ import annotations

import logging
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar, Iterable, Iterator

from dismech.structured_sources.base import (
    BulkFile,
    ReferenceCacheEntry,
    StructuredSource,
    format_columns,
)

logger = logging.getLogger(__name__)


# Disorder buckets we emit cache files for.
_LEAF_GROUPS = frozenset({"Disorder", "Subtype of disorder"})

# Mapping-relation short codes seen in product1.
# (Letters in parens come from Orphadata's relation labels.)
_MAPPING_RELATION_SHORT = {
    "E (Exact mapping: the two concepts are equivalent)": "E",
    "NTBT (ORPHAcode is narrower than the targeted code used to represent it)": "NTBT",
    "BTNT (ORPHAcode is broader than the targeted code used to represent it)": "BTNT",
    "ND (Not yet decided/unable to decide)": "ND",
    "W (ORPHAcode is wrongly used to represent the targeted code)": "W",
}

# Curator-friendly labels for the short codes above. Used by the renderer so
# the cross-reference block reads as English ("Exact"/"Narrower"/...) rather
# than as cryptic acronyms.
_RELATION_LABEL = {
    "E": "Exact",
    "NTBT": "Narrower",
    "BTNT": "Broader",
    "ND": "Not yet decided",
    "W": "Wrong",
    "": "",
}

# External-ref source -> CURIE prefix used in our XREF lines.
# Where Orphanet's "Source" string already matches the CURIE prefix, we leave it.
_XREF_PREFIX = {
    "ICD-10": "ICD-10",
    "ICD-11": "ICD-11",
    "OMIM": "OMIM",
    "MONDO": "MONDO",
    "UMLS": "UMLS",
    "MeSH": "MeSH",
    "MedDRA": "MedDRA",
    "GARD": "GARD",
    "SNOMEDCT": "SNOMEDCT",
}


@dataclass
class _DisorderRecord:
    """Aggregated data for one ORPHA disorder across all five products."""

    orpha_code: str
    name: str
    expert_link: str = ""
    disorder_type: str = ""
    disorder_group: str = ""
    synonyms: list[str] = field(default_factory=list)
    definition: str = ""
    xrefs: list[tuple[str, str, str]] = field(default_factory=list)
    # phenotypes: list of (hpo_id, hpo_label, frequency_label, diagnostic_criteria)
    phenotypes: list[tuple[str, str, str, str]] = field(default_factory=list)
    # genes: list of (symbol, name, hgnc_id, association_type, source_of_validation)
    genes: list[tuple[str, str, str, str, str]] = field(default_factory=list)
    # prevalence: list of (type, qualification, val_class, geographic, source)
    prevalence: list[tuple[str, str, str, str, str]] = field(default_factory=list)
    # inheritance modes
    inheritance: list[str] = field(default_factory=list)
    # age of onset categories
    age_of_onset: list[str] = field(default_factory=list)
    # age of death categories
    age_of_death: list[str] = field(default_factory=list)


class OrphanetSource(StructuredSource):
    """Structured-database source for Orphanet rare-disease records."""

    prefix: ClassVar[str] = "ORPHA"
    id_pattern: ClassVar[re.Pattern] = re.compile(r"^\d+$")

    # The canonical pin lives in `data/orphadata/MANIFEST.yaml`; ``bulk_files``
    # is populated lazily via :meth:`load_manifest`.
    bulk_files: ClassVar[tuple[BulkFile, ...]] = ()

    @classmethod
    def load_manifest(cls, manifest_path: Path) -> None:
        """Populate ``bulk_files`` and ``snapshot_date`` from a manifest YAML."""
        from ruamel.yaml import YAML

        yaml = YAML(typ="safe")
        data = yaml.load(manifest_path)
        bf = tuple(
            BulkFile(
                name=entry["name"],
                url=entry["url"],
                sha256=entry.get("sha256", ""),
                description=entry.get("description", ""),
            )
            for entry in data.get("bulk_files", [])
        )
        cls.bulk_files = bf
        cls._manifest_snapshot_date = str(data.get("snapshot_date", ""))

    # ----- indexing -----

    def build_index(self) -> dict[str, _DisorderRecord]:
        records: dict[str, _DisorderRecord] = {}
        snapshot = self._load_product1(records)
        self._snapshot_date = snapshot
        self._load_product4(records)
        self._load_product6(records)
        self._load_product9_prev(records)
        self._load_product9_ages(records)
        # Filter: keep only leaf-shape disorders.
        return {
            code: rec
            for code, rec in records.items()
            if rec.disorder_group in _LEAF_GROUPS
        }

    def identifiers(self) -> Iterable[str]:
        return sorted(self.index().keys(), key=lambda c: int(c))

    @property
    def snapshot_date(self) -> str:
        """Snapshot date — prefer manifest pin, fall back to product1 root attr."""
        manifest_date = getattr(type(self), "_manifest_snapshot_date", "")
        if manifest_date:
            return manifest_date
        if not getattr(self, "_snapshot_date", None):
            self.index()
        return self._snapshot_date or ""

    # ----- product loaders -----

    def _load_product1(self, records: dict[str, _DisorderRecord]) -> str:
        path = self.data_dir / "en_product1.xml"
        tree = ET.parse(path)
        root = tree.getroot()
        snapshot = root.attrib.get("date", "").split(" ")[0]  # YYYY-MM-DD
        for d in root.iter("Disorder"):
            code = _text(d.find("OrphaCode"))
            if not code:
                continue
            rec = records.setdefault(
                code,
                _DisorderRecord(orpha_code=code, name=_text(d.find("Name"))),
            )
            rec.name = _text(d.find("Name")) or rec.name
            rec.expert_link = _text(d.find("ExpertLink"))
            rec.disorder_type = _text(d.find("DisorderType/Name"))
            rec.disorder_group = _text(d.find("DisorderGroup/Name"))
            rec.synonyms = [
                s for s in (_text(syn) for syn in d.findall("SynonymList/Synonym")) if s
            ]
            # definition
            for ts in d.findall(
                "SummaryInformationList/SummaryInformation/TextSectionList/TextSection"
            ):
                tt = _text(ts.find("TextSectionType/Name"))
                if tt == "Definition":
                    rec.definition = _normalize_whitespace(_text(ts.find("Contents")))
                    break
            # external refs
            xrefs: list[tuple[str, str, str]] = []
            for x in d.findall("ExternalReferenceList/ExternalReference"):
                source = _text(x.find("Source"))
                ref = _text(x.find("Reference"))
                if not source or not ref:
                    continue
                relation_label = _text(x.find("DisorderMappingRelation/Name"))
                relation_short = _MAPPING_RELATION_SHORT.get(
                    relation_label, relation_label.split(" ", 1)[0] if relation_label else ""
                )
                xrefs.append((source, ref, relation_short))
            rec.xrefs = xrefs
        return snapshot

    def _load_product4(self, records: dict[str, _DisorderRecord]) -> None:
        path = self.data_dir / "en_product4.xml"
        if not path.exists():
            return
        tree = ET.parse(path)
        root = tree.getroot()
        for d in root.iter("Disorder"):
            code = _text(d.find("OrphaCode"))
            rec = records.get(code)
            if rec is None:
                continue
            phens: list[tuple[str, str, str, str]] = []
            for assoc in d.findall(
                "HPODisorderAssociationList/HPODisorderAssociation"
            ):
                hpo_id = _text(assoc.find("HPO/HPOId"))
                hpo_label = _text(assoc.find("HPO/HPOTerm"))
                freq = _text(assoc.find("HPOFrequency/Name"))
                diag = _text(assoc.find("DiagnosticCriteria"))
                if hpo_id:
                    phens.append((hpo_id, hpo_label, freq, diag))
            rec.phenotypes = phens

    def _load_product6(self, records: dict[str, _DisorderRecord]) -> None:
        path = self.data_dir / "en_product6.xml"
        if not path.exists():
            return
        tree = ET.parse(path)
        root = tree.getroot()
        for d in root.iter("Disorder"):
            code = _text(d.find("OrphaCode"))
            rec = records.get(code)
            if rec is None:
                continue
            genes: list[tuple[str, str, str, str, str]] = []
            for assoc in d.findall(
                "DisorderGeneAssociationList/DisorderGeneAssociation"
            ):
                gene = assoc.find("Gene")
                if gene is None:
                    continue
                symbol = _text(gene.find("Symbol"))
                name = _text(gene.find("Name"))
                hgnc = ""
                for x in gene.findall("ExternalReferenceList/ExternalReference"):
                    if _text(x.find("Source")) == "HGNC":
                        hgnc = _text(x.find("Reference"))
                        break
                assoc_type = _text(assoc.find("DisorderGeneAssociationType/Name"))
                source_val = _text(assoc.find("SourceOfValidation"))
                genes.append((symbol, name, hgnc, assoc_type, source_val))
            rec.genes = genes

    def _load_product9_prev(self, records: dict[str, _DisorderRecord]) -> None:
        path = self.data_dir / "en_product9_prev.xml"
        if not path.exists():
            return
        tree = ET.parse(path)
        root = tree.getroot()
        for d in root.iter("Disorder"):
            code = _text(d.find("OrphaCode"))
            rec = records.get(code)
            if rec is None:
                continue
            prevs: list[tuple[str, str, str, str, str]] = []
            for p in d.findall("PrevalenceList/Prevalence"):
                ptype = _text(p.find("PrevalenceType/Name"))
                qual = _text(p.find("PrevalenceQualification/Name"))
                pclass = _text(p.find("PrevalenceClass/Name"))
                geog = _text(p.find("PrevalenceGeographic/Name"))
                source = _text(p.find("Source"))
                prevs.append((ptype, qual, pclass, geog, source))
            rec.prevalence = prevs

    def _load_product9_ages(self, records: dict[str, _DisorderRecord]) -> None:
        path = self.data_dir / "en_product9_ages.xml"
        if not path.exists():
            return
        tree = ET.parse(path)
        root = tree.getroot()
        for d in root.iter("Disorder"):
            code = _text(d.find("OrphaCode"))
            rec = records.get(code)
            if rec is None:
                continue
            rec.age_of_onset = sorted({
                _text(a.find("Name"))
                for a in d.findall("AverageAgeOfOnsetList/AverageAgeOfOnset")
                if _text(a.find("Name"))
            })
            rec.age_of_death = sorted({
                _text(a.find("Name"))
                for a in d.findall("AverageAgeOfDeathList/AverageAgeOfDeath")
                if _text(a.find("Name"))
            })
            rec.inheritance = sorted({
                _text(t.find("Name"))
                for t in d.findall("TypeOfInheritanceList/TypeOfInheritance")
                if _text(t.find("Name"))
            })

    # ----- serialization -----

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        # Accept "ORPHA:558", "Orphanet:558", or bare "558". `removeprefix`
        # is used because `lstrip` removes a *character set*, not a literal
        # prefix — e.g. `"Orphanet:558".lstrip("ORPHA:")` would yield
        # `"rphanet:558"` (stops at lowercase `r`).
        for _prefix in ("ORPHA:", "Orphanet:"):
            if identifier.startswith(_prefix):
                identifier = identifier[len(_prefix):]
                break
        rec = self.index().get(identifier)
        if rec is None:
            raise KeyError(f"ORPHA:{identifier} not found in Orphanet index")

        body = "\n".join(self._render_body(rec)) + "\n"
        return ReferenceCacheEntry(
            reference_id=f"ORPHA:{rec.orpha_code}",
            title=rec.name,
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "Orphanet"},
        )

    def _render_body(self, rec: _DisorderRecord) -> Iterator[str]:
        """Render a Marfan-style mixed body: markdown for prose, fenced code
        blocks for tabular row data.

        Curators quote a definition sentence verbatim, or a single line from
        a fenced block (e.g. one ``HP:0001166  Arachnodactyly  Very frequent
        (99-80%)`` row). Both are stable substrings of the cached body.
        """
        yield f"# ORPHA:{rec.orpha_code}  {rec.name}"
        yield ""

        # Identification line — short prose, no fence needed.
        type_str = rec.disorder_type or "?"
        group_str = rec.disorder_group or "?"
        yield f"**ORPHA:{rec.orpha_code}** — {rec.name} ({type_str}, {group_str})"
        yield ""

        # Synonyms — bullets are friendlier than a fenced block for short lists.
        if rec.synonyms:
            yield "## Synonyms"
            yield ""
            for syn in sorted(rec.synonyms):
                yield f"- {syn}"
            yield ""

        # Definition — paragraph prose; the most-quoted block.
        if rec.definition:
            yield "## Definition"
            yield ""
            yield rec.definition
            yield ""

        # Inheritance — bullets.
        if rec.inheritance:
            yield "## Inheritance"
            yield ""
            for inh in rec.inheritance:
                yield f"- {inh}"
            yield ""

        # Age of onset / death — bullets.
        if rec.age_of_onset or rec.age_of_death:
            yield "## Natural history"
            yield ""
            for a in rec.age_of_onset:
                yield f"- Age of onset: {a}"
            for a in rec.age_of_death:
                yield f"- Age of death: {a}"
            yield ""

        # Epidemiology — fenced block, columns: class, region, type, source.
        if rec.prevalence:
            yield "## Epidemiology"
            yield ""
            yield "```"
            rows = sorted(
                rec.prevalence,
                key=lambda p: (p[3] or "", p[0] or "", p[2] or "", p[4] or ""),
            )
            cells: list[tuple[str, ...]] = []
            for ptype, _qual, pclass, geog, source in rows:
                cells.append(
                    (
                        pclass or "-",
                        geog or "-",
                        ptype or "-",
                        _clean_source(source) if source else "-",
                    )
                )
            for line in format_columns(cells, widths=[20, 16, 22]):
                yield line
            yield "```"
            yield ""

        # Genes — fenced block, columns: symbol, name, hgnc, association.
        if rec.genes:
            yield "## Genes"
            yield ""
            yield "```"
            rows_g = sorted(rec.genes, key=lambda g: (g[0] or "", g[3] or ""))
            cells_g = [
                (sym or "-", name or "-", _hgnc(hgnc), assoc or "-")
                for sym, name, hgnc, assoc, _src in rows_g
            ]
            for line in format_columns(cells_g, widths=[10, 50, 12]):
                yield line
            yield "```"
            yield ""

        # Phenotypes — fenced block, columns: HPO id, label, frequency.
        if rec.phenotypes:
            yield "## Phenotypes"
            yield ""
            yield "```"
            rows_p = sorted(rec.phenotypes, key=lambda p: (p[0] or ""))
            cells = [
                (hpo_id, label or "-", freq or "-")
                for hpo_id, label, freq, _diag in rows_p
            ]
            for line in format_columns(cells, widths=[12, 48]):
                yield line
            yield "```"
            yield ""

        # Cross-references — fenced block, columns: prefix:id, relation.
        if rec.xrefs:
            yield "## Cross-references"
            yield ""
            yield "```"
            seen: set[tuple[str, str, str]] = set()
            rows_x: list[tuple[str, str]] = []
            for source, ref, relation in sorted(rec.xrefs):
                key = (source, ref, relation)
                if key in seen:
                    continue
                seen.add(key)
                prefix = _XREF_PREFIX.get(source, source)
                rows_x.append((f"{prefix}:{ref}", _RELATION_LABEL.get(relation, relation)))
            for line in format_columns(rows_x, widths=[28]):
                yield line
            yield "```"
            yield ""

        # Provenance footer — prose.
        yield "## Source"
        yield ""
        yield (
            f"Orphadata snapshot **{self.snapshot_date or 'unknown'}** "
            f"(`en_product1+4+6+9_prev+9_ages`). "
            "Licensed under "
            "[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)."
        )
        if rec.expert_link:
            yield ""
            yield f"[Orpha.net entry]({rec.expert_link})"


# ----- helpers -----

def _text(el) -> str:
    if el is None:
        return ""
    return (el.text or "").strip()


def _normalize_whitespace(s: str) -> str:
    """Collapse interior whitespace so the definition is a single line."""
    return re.sub(r"\s+", " ", s).strip()


def _clean_source(s: str) -> str:
    """Compact the Orphadata 'Source' string for prevalence rows."""
    # Common pattern: "11389160[PMID]_9689990[PMID]_ [EXPERT]"
    parts = re.findall(r"(\d+)\[(\w+)\]|\[(\w+)\]", s)
    out: list[str] = []
    for pmid, kind, bare in parts:
        if pmid:
            out.append(f"PMID:{pmid}")
        elif bare:
            out.append(bare.upper())
    if not out:
        return s.strip().replace(" ", "")
    return ",".join(out)


def _hgnc(hgnc_id: str) -> str:
    if not hgnc_id:
        return "-"
    return f"hgnc:{hgnc_id}"

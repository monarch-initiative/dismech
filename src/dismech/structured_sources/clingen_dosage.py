"""ClinGen dosage sensitivity structured-database source.

Ingests the public ClinGen Dosage Sensitivity gene download and the GRCh38
curated-gene TSV, then emits one ``CGDS_<HGNC>.md`` cache file per gene. The
serialized body includes haploinsufficiency and triplosensitivity assertions,
disease identifiers, PMIDs, and optionally narrative evidence/comments scraped
from the public dosage report page.
"""

from __future__ import annotations

import csv
import logging
import re
from dataclasses import dataclass
from io import StringIO
from pathlib import Path
from typing import ClassVar, Iterable, Iterator
from urllib.parse import unquote, urlparse

import httpx
from bs4 import BeautifulSoup

from dismech.structured_sources.base import (
    BulkFile,
    ReferenceCacheEntry,
    StructuredSource,
)

logger = logging.getLogger(__name__)

CLINGEN_DOSAGE_GENE_TSV_GRCH38_URL = (
    "https://ftp.clinicalgenome.org/ClinGen_gene_curation_list_GRCh38.tsv"
)
CLINGEN_DOSAGE_GENE_CSV_URL = (
    "https://search.clinicalgenome.org/kb/gene-dosage/download"
)
CLINGEN_DOSAGE_REPORT_BASE_URL = "https://search.clinicalgenome.org/kb/gene-dosage"

_CSV_NAME = "gene_dosage.csv"
_TSV_NAME = "gene_dosage_grch38.tsv"
_CSV_HEADERS = [
    "GENE SYMBOL",
    "HGNC ID",
    "HAPLOINSUFFICIENCY",
    "TRIPLOSENSITIVITY",
    "ONLINE REPORT",
    "DATE",
]
_TSV_HEADERS = [
    "Gene Symbol",
    "Gene ID",
    "cytoBand",
    "Genomic Location",
    "Haploinsufficiency Score",
    "Haploinsufficiency Description",
    "Haploinsufficiency PMID1",
    "Haploinsufficiency PMID2",
    "Haploinsufficiency PMID3",
    "Haploinsufficiency PMID4",
    "Haploinsufficiency PMID5",
    "Haploinsufficiency PMID6",
    "Triplosensitivity Score",
    "Triplosensitivity Description",
    "Triplosensitivity PMID1",
    "Triplosensitivity PMID2",
    "Triplosensitivity PMID3",
    "Triplosensitivity PMID4",
    "Triplosensitivity PMID5",
    "Triplosensitivity PMID6",
    "Date Last Evaluated",
    "Haploinsufficiency Disease ID",
    "Triplosensitivity Disease ID",
]


@dataclass(frozen=True)
class _DosageEvidence:
    """One PubMed-backed evidence note from a dosage report."""

    pmid: str
    summary: str


@dataclass(frozen=True)
class _ClinGenDosageRecord:
    """One ClinGen gene dosage sensitivity curation."""

    reference_id: str
    gene_symbol: str
    hgnc_id: str
    entrez_id: str
    cytoband: str
    grch38_location: str
    haplo_score: str
    haplo_assertion: str
    haplo_scored_description: str
    haplo_pmids: tuple[str, ...]
    triplo_score: str
    triplo_assertion: str
    triplo_scored_description: str
    triplo_pmids: tuple[str, ...]
    date_last_evaluated: str
    haplo_disease_id: str
    triplo_disease_id: str
    report_url: str


@dataclass(frozen=True)
class _ClinGenDosageReportDetails:
    """Narrative details scraped from one ClinGen dosage report page."""

    dosage_id: str = ""
    curation_id: str = ""
    haplo_disease: tuple[str, ...] = ()
    triplo_disease: tuple[str, ...] = ()
    haplo_evidence: tuple[_DosageEvidence, ...] = ()
    triplo_evidence: tuple[_DosageEvidence, ...] = ()
    haplo_comments: tuple[str, ...] = ()
    triplo_comments: tuple[str, ...] = ()


class ClinGenDosageSource(StructuredSource):
    """Structured source for ClinGen Dosage Sensitivity gene curations."""

    prefix: ClassVar[str] = "CGDS"
    id_pattern: ClassVar[re.Pattern] = re.compile(
        r"^(CGDS:HGNC_\d+|HGNC:\d+|HGNC_\d+)$"
    )
    bulk_files: ClassVar[tuple[BulkFile, ...]] = (
        BulkFile(
            name=_CSV_NAME,
            url=CLINGEN_DOSAGE_GENE_CSV_URL,
            sha256="",
            description="ClinGen Dosage Sensitivity gene download",
        ),
        BulkFile(
            name=_TSV_NAME,
            url=CLINGEN_DOSAGE_GENE_TSV_GRCH38_URL,
            sha256="",
            description="ClinGen Dosage Sensitivity curated gene list, GRCh38",
        ),
    )

    def __init__(
        self,
        data_dir: Path,
        *,
        include_report_text: bool = True,
        timeout: float = 30.0,
    ) -> None:
        super().__init__(data_dir)
        self.include_report_text = include_report_text
        self.timeout = timeout
        self._report_cache: dict[str, _ClinGenDosageReportDetails | None] = {}

    @classmethod
    def load_manifest(cls, manifest_path: Path) -> None:
        """Populate ``bulk_files`` and snapshot metadata from a manifest YAML."""
        from ruamel.yaml import YAML

        yaml = YAML(typ="safe")
        data = yaml.load(manifest_path)
        cls.bulk_files = tuple(
            BulkFile(
                name=entry["name"],
                url=entry["url"],
                sha256=entry.get("sha256", ""),
                description=entry.get("description", ""),
            )
            for entry in data.get("bulk_files", [])
        )
        cls._manifest_snapshot_date = str(data.get("snapshot_date", ""))
        cls._manifest_schema_tag = str(data.get("schema_tag", ""))

    def build_index(self) -> dict[str, _ClinGenDosageRecord]:
        tsv_rows = self._load_tsv_rows()
        path = self._csv_path()
        text = path.read_text(encoding="utf-8-sig")
        reader = csv.reader(StringIO(text))

        header_seen = False
        records: dict[str, _ClinGenDosageRecord] = {}

        for row in reader:
            if not row:
                continue
            first = row[0].strip()
            if first.startswith("FILE CREATED:"):
                self._csv_file_created = first.split(":", 1)[1].strip()
                continue
            if first.startswith("WEBPAGE:"):
                self._webpage = first.split(":", 1)[1].strip()
                continue
            if row[: len(_CSV_HEADERS)] == _CSV_HEADERS:
                header_seen = True
                break

        if not header_seen:
            raise ValueError(f"{path} is missing the ClinGen dosage CSV header row")

        for row in reader:
            if not row or _is_separator_row(row):
                continue
            if len(row) < len(_CSV_HEADERS):
                continue

            data = dict(zip(_CSV_HEADERS, row))
            hgnc_id = _clean(data["HGNC ID"])
            if not hgnc_id.startswith("HGNC:"):
                continue

            gene_symbol = _clean(data["GENE SYMBOL"])
            tsv_data = tsv_rows.get(gene_symbol, {})
            rec = _ClinGenDosageRecord(
                reference_id=_reference_id_from_hgnc(hgnc_id),
                gene_symbol=gene_symbol,
                hgnc_id=hgnc_id,
                entrez_id=_clean(tsv_data.get("Gene ID", "")),
                cytoband=_clean(tsv_data.get("cytoBand", "")),
                grch38_location=_clean(tsv_data.get("Genomic Location", "")),
                haplo_score=_clean(tsv_data.get("Haploinsufficiency Score", "")),
                haplo_assertion=_clean(data["HAPLOINSUFFICIENCY"]),
                haplo_scored_description=_clean(
                    tsv_data.get("Haploinsufficiency Description", "")
                ),
                haplo_pmids=_pmids(tsv_data, "Haploinsufficiency PMID"),
                triplo_score=_clean(tsv_data.get("Triplosensitivity Score", "")),
                triplo_assertion=_clean(data["TRIPLOSENSITIVITY"]),
                triplo_scored_description=_clean(
                    tsv_data.get("Triplosensitivity Description", "")
                ),
                triplo_pmids=_pmids(tsv_data, "Triplosensitivity PMID"),
                date_last_evaluated=(
                    _clean(tsv_data.get("Date Last Evaluated", ""))
                    or _clean(data["DATE"])
                ),
                haplo_disease_id=_clean(
                    tsv_data.get("Haploinsufficiency Disease ID", "")
                ),
                triplo_disease_id=_clean(
                    tsv_data.get("Triplosensitivity Disease ID", "")
                ),
                report_url=_clean(data["ONLINE REPORT"])
                or f"{CLINGEN_DOSAGE_REPORT_BASE_URL}/{hgnc_id}",
            )
            records[rec.reference_id] = rec

        return records

    def _load_tsv_rows(self) -> dict[str, dict[str, str]]:
        path = self._tsv_path()
        text = path.read_text(encoding="utf-8-sig")
        reader = csv.reader(StringIO(text), delimiter="\t")

        header: list[str] | None = None
        rows: dict[str, dict[str, str]] = {}

        for row in reader:
            if not row:
                continue
            first = row[0].strip()
            if first.startswith("#") and header is None:
                if first.startswith("#Gene Symbol"):
                    header = [first.removeprefix("#"), *row[1:]]
                elif re.match(r"^#\d{1,2} [A-Za-z]+,\d{4}$", first):
                    self._tsv_file_created = _parse_snapshot_date(
                        first.removeprefix("#")
                    )
                continue
            if header is None:
                continue
            if len(row) < len(header):
                row = [*row, *([""] * (len(header) - len(row)))]
            data = dict(zip(header, row))
            gene_symbol = _clean(data["Gene Symbol"])
            if gene_symbol:
                rows[gene_symbol] = data

        if header != _TSV_HEADERS:
            raise ValueError(f"{path} has unexpected ClinGen dosage TSV headers")

        return rows

    def _csv_path(self) -> Path:
        path = self.data_dir / _CSV_NAME
        if path.exists():
            return path
        raise FileNotFoundError(
            f"{path} not found; run `just clingen-dosage-refresh` first"
        )

    def _tsv_path(self) -> Path:
        path = self.data_dir / _TSV_NAME
        if path.exists():
            return path
        raise FileNotFoundError(
            f"{path} not found; run `just clingen-dosage-refresh` first"
        )

    def identifiers(self) -> Iterable[str]:
        idx = self.index()
        return sorted(
            idx.keys(),
            key=lambda ident: (idx[ident].gene_symbol, idx[ident].hgnc_id),
        )

    @property
    def snapshot_date(self) -> str:
        """Snapshot date from manifest or source-file metadata."""
        manifest_date = getattr(type(self), "_manifest_snapshot_date", "")
        if manifest_date:
            return manifest_date
        if not getattr(self, "_csv_file_created", None):
            self.index()
        return getattr(self, "_csv_file_created", "") or getattr(
            self, "_tsv_file_created", ""
        )

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        normalized = _normalize_identifier(identifier)
        rec = self.index().get(normalized)
        if rec is None:
            raise KeyError(f"{normalized} not found in ClinGen dosage index")

        details = self._get_report_details(rec) if self.include_report_text else None
        body = "\n".join(self._render_body(rec, details)) + "\n"
        return ReferenceCacheEntry(
            reference_id=rec.reference_id,
            title=f"{rec.gene_symbol} dosage sensitivity",
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "ClinGen"},
        )

    def _get_report_details(
        self, rec: _ClinGenDosageRecord
    ) -> _ClinGenDosageReportDetails | None:
        cached = self._report_cache.get(rec.reference_id)
        if cached is not None:
            return cached
        if rec.reference_id in self._report_cache:
            return None

        try:
            with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
                response = client.get(rec.report_url)
                response.raise_for_status()
        except httpx.HTTPError as exc:
            logger.warning(
                "could not fetch ClinGen dosage report %s: %s", rec.report_url, exc
            )
            self._report_cache[rec.reference_id] = None
            return None

        details = _parse_report_details(response.text)
        self._report_cache[rec.reference_id] = details
        return details

    def _render_body(
        self,
        rec: _ClinGenDosageRecord,
        details: _ClinGenDosageReportDetails | None = None,
    ) -> Iterator[str]:
        yield f"# {rec.reference_id}  {rec.gene_symbol} dosage sensitivity"
        yield ""
        yield f"**{rec.reference_id}** - {rec.gene_symbol} ({rec.hgnc_id})"
        yield ""

        yield "## Dosage sensitivity summary"
        yield ""
        yield from _md_table(
            [
                "Gene",
                "HGNC",
                "Entrez",
                "Cytoband",
                "GRCh38",
                "Haploinsufficiency",
                "Triplosensitivity",
                "Last evaluated",
            ],
            [
                (
                    rec.gene_symbol,
                    rec.hgnc_id,
                    rec.entrez_id,
                    rec.cytoband,
                    rec.grch38_location,
                    _score_label(rec.haplo_score, rec.haplo_assertion),
                    _score_label(rec.triplo_score, rec.triplo_assertion),
                    rec.date_last_evaluated,
                )
            ],
        )
        yield ""

        yield "## Haploinsufficiency"
        yield ""
        yield f"- Score: {rec.haplo_score or '-'}"
        yield f"- Assertion: {rec.haplo_assertion or '-'}"
        if rec.haplo_scored_description:
            yield f"- Scored description: {rec.haplo_scored_description}"
        if rec.haplo_disease_id:
            yield f"- Disease ID: {rec.haplo_disease_id}"
        if details and details.haplo_disease:
            for disease in details.haplo_disease:
                yield f"- Disease: {disease}"
        if rec.haplo_pmids:
            yield "- PMIDs: " + ", ".join(f"PMID:{pmid}" for pmid in rec.haplo_pmids)
        yield ""
        if details:
            yield from _render_report_text(
                "Haploinsufficiency report text",
                details.haplo_evidence,
                details.haplo_comments,
            )

        yield "## Triplosensitivity"
        yield ""
        yield f"- Score: {rec.triplo_score or '-'}"
        yield f"- Assertion: {rec.triplo_assertion or '-'}"
        if rec.triplo_scored_description:
            yield f"- Scored description: {rec.triplo_scored_description}"
        if rec.triplo_disease_id:
            yield f"- Disease ID: {rec.triplo_disease_id}"
        if details and details.triplo_disease:
            for disease in details.triplo_disease:
                yield f"- Disease: {disease}"
        if rec.triplo_pmids:
            yield "- PMIDs: " + ", ".join(f"PMID:{pmid}" for pmid in rec.triplo_pmids)
        yield ""
        if details:
            yield from _render_report_text(
                "Triplosensitivity report text",
                details.triplo_evidence,
                details.triplo_comments,
            )

        yield "## Online report"
        yield ""
        if details and details.dosage_id:
            yield f"- Dosage ID: {details.dosage_id}"
        if details and details.curation_id:
            yield f"- Curation ID: {details.curation_id}"
        yield f"- Report URL: {rec.report_url}"
        yield ""

        yield "## Source"
        yield ""
        yield (
            "ClinGen Dosage Sensitivity gene download and curated gene list "
            f"GRCh38 snapshot **{self.snapshot_date or 'unknown'}** "
            f"(`{_CSV_NAME}`, `{_TSV_NAME}`)."
        )
        yield ""
        yield "[ClinGen dosage sensitivity downloads](https://search.clinicalgenome.org/kb/downloads)"


def _render_report_text(
    heading: str,
    evidence: tuple[_DosageEvidence, ...],
    comments: tuple[str, ...],
) -> Iterator[str]:
    if not evidence and not comments:
        return
    yield f"## {heading}"
    yield ""
    for item in evidence:
        yield f"- PMID:{item.pmid}: {item.summary}"
    for comment in comments:
        yield f"- Evidence comments: {comment}"
    yield ""


def _is_separator_row(row: list[str]) -> bool:
    return bool(row) and all(not cell or set(cell) == {"+"} for cell in row)


def _reference_id_from_hgnc(hgnc_id: str) -> str:
    return "CGDS:" + hgnc_id.replace(":", "_")


def _normalize_identifier(identifier: str) -> str:
    ident = identifier.strip()
    if ident.startswith(("http://", "https://")):
        segment = unquote(urlparse(ident).path.rstrip("/").rsplit("/", 1)[-1])
        if segment.startswith("HGNC:"):
            return _reference_id_from_hgnc(segment)
    for prefix in ("CLINGEN-DOSAGE:", "ClinGen-Dosage:", "CLINGEN_DOSAGE:"):
        if ident.startswith(prefix):
            ident = ident[len(prefix) :]
            break
    if ident.startswith("CGDS:"):
        return ident
    if ident.startswith("HGNC:"):
        return _reference_id_from_hgnc(ident)
    if ident.startswith("HGNC_"):
        return f"CGDS:{ident}"
    return ident


def _parse_report_details(html: str) -> _ClinGenDosageReportDetails:
    soup = BeautifulSoup(html, "html.parser")
    page_text = _clean(soup.get_text(" ", strip=True))

    dosage_id = ""
    dosage_match = re.search(r"\bISCA-\d+\b", page_text)
    if dosage_match:
        dosage_id = dosage_match.group(0)

    curation_id = ""
    curation_match = re.search(r"\bCCID:\d+\b", page_text)
    if curation_match:
        curation_id = curation_match.group(0)

    haplo = _extract_dosage_section(soup, "report_details_haploinsufficiency")
    triplo = _extract_dosage_section(soup, "report_details_triplosensitivity")

    return _ClinGenDosageReportDetails(
        dosage_id=dosage_id,
        curation_id=curation_id,
        haplo_disease=tuple(haplo["disease"]),
        triplo_disease=tuple(triplo["disease"]),
        haplo_evidence=tuple(haplo["evidence"]),
        triplo_evidence=tuple(triplo["evidence"]),
        haplo_comments=tuple(haplo["comments"]),
        triplo_comments=tuple(triplo["comments"]),
    )


def _extract_dosage_section(
    soup: BeautifulSoup, section_id: str
) -> dict[str, list[str] | list[_DosageEvidence]]:
    section = soup.find(id=section_id)
    if section is None:
        return {"disease": [], "evidence": [], "comments": []}

    disease: list[str] = []
    evidence: list[_DosageEvidence] = []
    comments: list[str] = []

    for row in section.select(".row"):
        children = row.find_all("div", recursive=False)
        if len(children) < 2:
            continue
        label = _clean(children[0].get_text(" ", strip=True)).rstrip(":")
        value = children[1]

        if label.endswith("Disease"):
            disease.extend(_extract_list_items(value))
        elif label.endswith("Evidence"):
            evidence.extend(_extract_evidence_items(value))
        elif label.endswith("Evidence Comments"):
            comment_text = _clean(value.get_text(" ", strip=True))
            if comment_text:
                comments.append(comment_text)

    return {"disease": disease, "evidence": evidence, "comments": comments}


def _extract_list_items(value_cell) -> list[str]:
    items = [_text_excluding_links(li) for li in value_cell.find_all("li")]
    if items:
        return [item for item in items if item]
    text = _text_excluding_links(value_cell)
    return [text] if text else []


def _text_excluding_links(tag) -> str:
    parts: list[str] = []
    for text in tag.find_all(string=True):
        if any(parent.name == "a" for parent in text.parents):
            continue
        parts.append(str(text))
    return _clean(" ".join(parts))


def _extract_evidence_items(value_cell) -> list[_DosageEvidence]:
    evidence: list[_DosageEvidence] = []
    for item in value_cell.find_all("li"):
        item_text = _clean(item.get_text(" ", strip=True))
        match = re.search(r"\bPUBMED:\s*(\d+)\b", item_text)
        if not match:
            continue
        summary_el = item.find(class_=re.compile(r"\bsummariesShow\b"))
        summary = (
            _clean(summary_el.get_text(" ", strip=True))
            if summary_el is not None
            else re.sub(r"^.*?\bPUBMED:\s*\d+\s*", "", item_text).strip()
        )
        evidence.append(_DosageEvidence(pmid=match.group(1), summary=summary))
    return evidence


def _pmids(data: dict[str, str], prefix: str) -> tuple[str, ...]:
    return tuple(
        _clean(data.get(f"{prefix}{i}", ""))
        for i in range(1, 7)
        if _clean(data.get(f"{prefix}{i}", ""))
    )


def _parse_snapshot_date(value: str) -> str:
    from datetime import datetime

    try:
        return datetime.strptime(value, "%d %B,%Y").date().isoformat()
    except ValueError:
        return value


def _score_label(score: str, description: str) -> str:
    if score and description:
        return f"{score} - {description}"
    return score or description or "-"


def _md_table(headers: list[str], rows: list[tuple[str, ...]]) -> Iterator[str]:
    def _esc(cell: str) -> str:
        return cell.replace("|", "\\|") if cell else "-"

    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        yield "| " + " | ".join(_esc(cell) for cell in row) + " |"


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()

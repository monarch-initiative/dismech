"""ClinGen gene-disease validity structured-database source.

Ingests the public ClinGen Gene-Disease Validity CSV download and emits one
``CGGV_<assertion>.md`` cache file per assertion. When enabled, the serializer
also fetches the assertion report page and includes ClinGen's narrative
evidence summary in that same cache file. The serialized body is a
deterministic, line-oriented markdown record so curators can cite a single
gene-disease validity row or summary sentence as an evidence ``snippet:``.
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

from dismech.clingen.client import CLINGEN_GDV_CSV_URL
from dismech.structured_sources.base import (
    BulkFile,
    ReferenceCacheEntry,
    StructuredSource,
)

logger = logging.getLogger(__name__)

_CSV_NAME = "gene_validity.csv"
_CSV_HEADERS = [
    "GENE SYMBOL",
    "GENE ID (HGNC)",
    "DISEASE LABEL",
    "DISEASE ID (MONDO)",
    "MOI",
    "SOP",
    "CLASSIFICATION",
    "ONLINE REPORT",
    "CLASSIFICATION DATE",
    "GCEP",
]


@dataclass(frozen=True)
class _ClinGenValidityRecord:
    """One ClinGen gene-disease validity assertion."""

    assertion_id: str
    gene_symbol: str
    gene_hgnc_id: str
    disease_label: str
    disease_mondo_id: str
    mode_of_inheritance: str
    sop: str
    classification: str
    report_url: str
    classification_date: str
    expert_panel: str


@dataclass(frozen=True)
class _ClinGenReportDetails:
    """Narrative and identifiers scraped from one ClinGen assertion report."""

    curation_id: str = ""
    evidence_summary: tuple[str, ...] = ()


class ClinGenSource(StructuredSource):
    """Structured source for ClinGen Gene-Disease Validity assertions."""

    prefix: ClassVar[str] = "CGGV"
    id_pattern: ClassVar[re.Pattern] = re.compile(
        r"^(CGGV:)?assertion_[A-Za-z0-9_.:-]+$"
    )
    bulk_files: ClassVar[tuple[BulkFile, ...]] = (
        BulkFile(
            name=_CSV_NAME,
            url=CLINGEN_GDV_CSV_URL,
            sha256="",
            description="ClinGen Gene-Disease Validity Curations CSV",
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
        self._report_cache: dict[str, _ClinGenReportDetails | None] = {}

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

    def build_index(self) -> dict[str, _ClinGenValidityRecord]:
        path = self._csv_path()

        records: dict[str, _ClinGenValidityRecord] = {}
        text = path.read_text(encoding="utf-8-sig")
        reader = csv.reader(StringIO(text))

        header_seen = False
        for row in reader:
            if not row:
                continue
            first = row[0].strip()
            if first.startswith("FILE CREATED:"):
                self._file_created = first.split(":", 1)[1].strip()
                continue
            if first.startswith("WEBPAGE:"):
                self._webpage = first.split(":", 1)[1].strip()
                continue
            if row[: len(_CSV_HEADERS)] == _CSV_HEADERS:
                header_seen = True
                break

        if not header_seen:
            raise ValueError(f"{path} is missing the ClinGen CSV header row")

        for row in reader:
            if not row or _is_separator_row(row):
                continue
            if len(row) < len(_CSV_HEADERS):
                continue

            data = dict(zip(_CSV_HEADERS, row))
            if not data["GENE SYMBOL"] or not data["DISEASE LABEL"]:
                continue

            assertion_id = _assertion_id_from_url(data["ONLINE REPORT"])
            if not assertion_id:
                continue

            rec = _ClinGenValidityRecord(
                assertion_id=assertion_id,
                gene_symbol=_clean(data["GENE SYMBOL"]),
                gene_hgnc_id=_clean(data["GENE ID (HGNC)"]),
                disease_label=_clean(data["DISEASE LABEL"]),
                disease_mondo_id=_clean(data["DISEASE ID (MONDO)"]),
                mode_of_inheritance=_clean(data["MOI"]),
                sop=_clean(data["SOP"]),
                classification=_clean(data["CLASSIFICATION"]),
                report_url=_clean(data["ONLINE REPORT"]),
                classification_date=_clean(data["CLASSIFICATION DATE"]),
                expert_panel=_clean(data["GCEP"]),
            )
            records[rec.assertion_id] = rec

        return records

    def _csv_path(self) -> Path:
        path = self.data_dir / _CSV_NAME
        if path.exists():
            return path

        # This repo already carries the ClinGen CSV used by the older GO
        # mapping tooling. Keep structured-source reads usable before a local
        # data/clingen refresh, while refresh() still writes to data/clingen.
        repo_root = Path(__file__).resolve().parents[3]
        fallback = repo_root / "cache" / "clingen" / _CSV_NAME
        if fallback.exists():
            return fallback

        raise FileNotFoundError(f"{path} not found; run `just refresh-clingen` first")

    def identifiers(self) -> Iterable[str]:
        idx = self.index()
        return sorted(
            idx.keys(),
            key=lambda ident: (
                idx[ident].gene_symbol,
                idx[ident].disease_label,
                idx[ident].mode_of_inheritance,
                ident,
            ),
        )

    @property
    def snapshot_date(self) -> str:
        """Snapshot date from manifest or CSV metadata."""
        manifest_date = getattr(type(self), "_manifest_snapshot_date", "")
        if manifest_date:
            return manifest_date
        if not getattr(self, "_file_created", None):
            self.index()
        return getattr(self, "_file_created", "")

    @property
    def webpage(self) -> str:
        """ClinGen gene validity landing page recorded in the CSV."""
        if not getattr(self, "_webpage", None):
            self.index()
        return getattr(self, "_webpage", "")

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        normalized = _normalize_identifier(identifier)
        rec = self.index().get(normalized)
        if rec is None:
            raise KeyError(f"{normalized} not found in ClinGen index")

        details = self._get_report_details(rec) if self.include_report_text else None
        body = "\n".join(self._render_body(rec, details)) + "\n"
        return ReferenceCacheEntry(
            reference_id=rec.assertion_id,
            title=f"{rec.gene_symbol} / {rec.disease_label} ({rec.classification})",
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "ClinGen"},
        )

    def _get_report_details(
        self, rec: _ClinGenValidityRecord
    ) -> _ClinGenReportDetails | None:
        cached = self._report_cache.get(rec.assertion_id)
        if cached is not None:
            return cached
        if rec.assertion_id in self._report_cache:
            return None

        if not rec.report_url:
            self._report_cache[rec.assertion_id] = None
            return None

        try:
            with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
                response = client.get(rec.report_url)
                response.raise_for_status()
        except httpx.HTTPError as exc:
            logger.warning("could not fetch ClinGen report %s: %s", rec.report_url, exc)
            self._report_cache[rec.assertion_id] = None
            return None

        details = _parse_report_details(response.text)
        self._report_cache[rec.assertion_id] = details
        return details

    def _render_body(
        self,
        rec: _ClinGenValidityRecord,
        details: _ClinGenReportDetails | None = None,
    ) -> Iterator[str]:
        yield f"# {rec.assertion_id}  {rec.gene_symbol} / {rec.disease_label}"
        yield ""
        yield (
            f"**{rec.assertion_id}** - {rec.gene_symbol} / "
            f"{rec.disease_label} ({rec.classification})"
        )
        yield ""

        if details and details.evidence_summary:
            yield "## Evidence summary"
            yield ""
            for paragraph in details.evidence_summary:
                yield paragraph
                yield ""

        yield "## Gene-disease validity"
        yield ""
        yield from _md_table(
            [
                "Gene",
                "HGNC",
                "Disease",
                "MONDO",
                "MOI",
                "Classification",
                "SOP",
                "GCEP",
                "Classification date",
            ],
            [
                (
                    rec.gene_symbol,
                    rec.gene_hgnc_id,
                    rec.disease_label,
                    rec.disease_mondo_id,
                    rec.mode_of_inheritance,
                    rec.classification,
                    rec.sop,
                    rec.expert_panel,
                    rec.classification_date,
                )
            ],
        )
        yield ""

        if rec.report_url:
            yield "## Online report"
            yield ""
            if details and details.curation_id:
                yield f"- Curation ID: {details.curation_id}"
            yield f"- Report URL: {rec.report_url}"
            yield ""

        yield "## Source"
        yield ""
        yield (
            "ClinGen Gene-Disease Validity Curations CSV snapshot "
            f"**{self.snapshot_date or 'unknown'}** (`{_CSV_NAME}`)."
        )
        if self.webpage:
            yield ""
            yield f"[ClinGen gene validity search]({self.webpage})"


def _is_separator_row(row: list[str]) -> bool:
    return bool(row) and all(not cell or set(cell) == {"+"} for cell in row)


def _assertion_id_from_url(url: str) -> str:
    if not url:
        return ""
    path = urlparse(url).path.rstrip("/")
    segment = unquote(path.rsplit("/", 1)[-1])
    if segment.startswith("CGGV:"):
        return segment
    if segment.startswith("assertion_"):
        return f"CGGV:{segment}"
    return ""


def _normalize_identifier(identifier: str) -> str:
    ident = identifier.strip()
    if ident.startswith(("http://", "https://")):
        url_id = _assertion_id_from_url(ident)
        if url_id:
            return url_id
    for prefix in ("CLINGEN:", "ClinGen:"):
        if ident.startswith(prefix):
            ident = ident[len(prefix) :]
            break
    if ident.startswith("CGGV:"):
        return ident
    if ident.startswith("assertion_"):
        return f"CGGV:{ident}"
    return ident


def _parse_report_details(html: str) -> _ClinGenReportDetails:
    soup = BeautifulSoup(html, "html.parser")
    curation_id = ""
    curation_id_text = soup.find(string=re.compile(r"\bCCID:\d+\b"))
    if curation_id_text:
        match = re.search(r"\bCCID:\d+\b", str(curation_id_text))
        if match:
            curation_id = match.group(0)

    return _ClinGenReportDetails(
        curation_id=curation_id,
        evidence_summary=tuple(_extract_labeled_paragraphs(soup, "Evidence Summary:")),
    )


def _extract_labeled_paragraphs(soup: BeautifulSoup, label: str) -> list[str]:
    normalized_label = label.rstrip(":")
    for cell in soup.find_all("td"):
        cell_text = _clean(cell.get_text(" ", strip=True)).rstrip(":")
        if cell_text != normalized_label:
            continue

        value_cell = cell.find_next_sibling("td")
        if value_cell is None:
            continue

        paragraphs = [
            _clean(paragraph.get_text(" ", strip=True))
            for paragraph in value_cell.find_all("p")
        ]
        return [paragraph for paragraph in paragraphs if paragraph]
    return []


def _md_table(headers: list[str], rows: list[tuple[str, ...]]) -> Iterator[str]:
    def _esc(cell: str) -> str:
        return cell.replace("|", "\\|") if cell else "-"

    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        yield "| " + " | ".join(_esc(cell) for cell in row) + " |"


def _clean(value: str) -> str:
    return re.sub(r"\s+", " ", value or "").strip()

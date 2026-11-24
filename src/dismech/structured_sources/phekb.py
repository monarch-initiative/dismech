"""PheKB (Phenotype KnowledgeBase) structured-database source.

Ingests a phenotype algorithm page from `PheKB <https://phekb.org/>`_ so a
disease entry's ``definitions`` can cite it as ``PHEKB:615`` and quote the
algorithm's own text as evidence.

PheKB has no documented API and publishes algorithms as attachments (PDF,
Word, SQL, spreadsheets) on a Drupal page, so each record is fetched per
identifier from ``https://phekb.org/node/<id>``. The cached body holds

* a ``## Record`` key/value table of the page's metadata fields (authors,
  institution, network, data modalities, status, demographics),
* the page's free-text ``## Description`` when it has one,
* ``## Files``, the attachment list, and
* ``## Attachment: <name>`` with the extracted text of each **PDF attachment
  that is an algorithm document** — the code tables and inclusion rules a
  curator needs to quote.

Two kinds of attachment are deliberately not transcribed:

* a PDF whose first page carries a DOI is a published journal article. It is
  cited by its PMID instead, and republishing a publisher's PDF here is not
  something a curation cache should do (:func:`is_journal_article`);
* Word, SQL, spreadsheet and archive attachments, which are listed but not
  extracted.

PheKB states no licence for its content. A transcribed algorithm document is
quoted as evidence with attribution, the same use as any other cited source.
"""

from __future__ import annotations

import io
import logging
import re
import ssl
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar
from urllib.parse import unquote

import httpx
import truststore
from bs4 import BeautifulSoup

from dismech.structured_sources.base import ReferenceCacheEntry, StructuredSource

logger = logging.getLogger(__name__)

SITE_ROOT = "https://phekb.org"

#: Drupal field labels lifted into the ``## Record`` table, in this order.
RECORD_FIELDS: tuple[str, ...] = (
    "Phenotype ID",
    "Date Created",
    "Status",
    "Authors",
    "Institution",
    "Network Associations",
    "Owner Phenotyping Groups",
    "Structured data",
    "Unstructured Data",
    "Data Source/clinical domain",
    "Data Model",
    "Phenotype Attributes",
    "Type of Phenotype",
    "Gender",
    "Age",
)

_DOI_RE = re.compile(
    r"\bdoi\b[\s:]*(?:https?://(?:dx\.)?doi\.org/)?10\.\d{4,}/", re.IGNORECASE
)


def normalize_identifier(identifier: str) -> str:
    """Strip a ``PHEKB:`` prefix; PheKB ids are Drupal node numbers.

    >>> normalize_identifier("PHEKB:615")
    '615'
    >>> normalize_identifier("phekb:1058")
    '1058'
    """
    identifier = identifier.strip()
    if identifier.upper().startswith("PHEKB:"):
        identifier = identifier[len("PHEKB:") :]
    identifier = identifier.strip()
    if not identifier.isdigit():
        raise KeyError(f"not a PheKB phenotype id: {identifier!r}")
    return identifier


def is_journal_article(first_page_text: str) -> bool:
    """True when a PDF's first page looks like a published article (carries a DOI).

    >>> is_journal_article("Arthritis Care & Research ... DOI 10.1002/acr.22989")
    True
    >>> is_journal_article("Computable Phenotype for Identification of Patients")
    False
    """
    return bool(_DOI_RE.search(first_page_text))


def clean_text(text: str) -> str:
    """Collapse runs of spaces in each line and drop blank-line runs.

    Line breaks are kept so a table row extracted from a PDF stays one line.

    >>> clean_text("a   b\\n\\n\\n  c ")
    'a b\\n\\nc'
    """
    lines = [" ".join(line.split()) for line in text.splitlines()]
    out: list[str] = []
    for line in lines:
        if not line and (not out or not out[-1]):
            continue
        out.append(line)
    return "\n".join(out).strip()


@dataclass
class PhenotypePage:
    """One parsed PheKB phenotype page."""

    node_id: str
    title: str
    fields: dict[str, str] = field(default_factory=dict)
    description: str = ""
    citation: str = ""
    pmids: list[str] = field(default_factory=list)
    files: list[tuple[str, str]] = field(default_factory=list)  # (name, url)
    attachments: dict[str, str] = field(default_factory=dict)  # name -> text
    skipped_articles: list[str] = field(default_factory=list)

    @property
    def url(self) -> str:
        return f"{SITE_ROOT}/node/{self.node_id}"


def parse_page(page: str, node_id: str | None = None) -> PhenotypePage:
    """Parse a PheKB phenotype page's HTML."""
    soup = BeautifulSoup(page, "html.parser")
    heading = soup.find("h1", class_="page-title")
    if heading is None:
        raise KeyError("no PheKB phenotype on this page")
    record = PhenotypePage(
        node_id=node_id or "", title=" ".join(heading.get_text().split())
    )
    article = soup.find("article") or soup
    for div in article.find_all("div", class_="field"):
        label_div = div.find("div", class_="field-label")
        items = div.find("div", class_="field-items")
        if label_div is None or items is None:
            continue
        label = (
            " ".join(label_div.get_text().replace("\xa0", " ").split())
            .rstrip(":")
            .strip()
        )
        values = [
            " ".join(item.get_text(" ").split())
            for item in items.find_all("div", class_="field-item", recursive=False)
        ]
        value = "; ".join(v for v in values if v)
        if label == "Files":
            for anchor in items.find_all("a", href=True):
                record.files.append(
                    (" ".join(anchor.get_text().split()), anchor["href"].strip())
                )
        elif value:
            record.fields.setdefault(label, value)
    body = article.find("div", class_="field-name-body")
    if body is not None:
        record.description = clean_text(body.get_text("\n"))
    if not record.node_id:
        record.node_id = record.fields.get("Phenotype ID", "")
    text = article.get_text("\n")
    citation = re.search(
        r"Suggested Citation\s*(.+?)(?:\n\s*PubMed References|\Z)", text, re.DOTALL
    )
    if citation:
        record.citation = " ".join(citation.group(1).split())
    refs = re.search(r"PubMed References\s*([\d\s,;]+)", text)
    if refs:
        record.pmids = re.findall(r"\d{6,9}", refs.group(1))
    return record


def pdf_text(data: bytes) -> tuple[str, str]:
    """Return ``(first_page_text, full_text)`` for a PDF."""
    from pypdf import PdfReader

    reader = PdfReader(io.BytesIO(data))
    pages = [page.extract_text() or "" for page in reader.pages]
    return (pages[0] if pages else ""), "\n".join(pages)


def render_body(record: PhenotypePage) -> str:
    """Render the cache body for a page (deterministic)."""
    return "\n".join(_render_lines(record)) + "\n"


def _render_lines(record: PhenotypePage) -> Iterator[str]:
    yield f"# PHEKB:{record.node_id}  {record.title}"
    yield ""
    yield f"**{record.title}** — phenotype algorithm page from PheKB (node {record.node_id})."
    yield ""
    yield "## Record"
    yield ""
    rows = [(k, record.fields[k]) for k in RECORD_FIELDS if record.fields.get(k)]
    if record.pmids:
        rows.append(("PubMed References", "; ".join(f"PMID:{p}" for p in record.pmids)))
    yield from _md_table(["Field", "Value"], rows)
    yield ""
    if record.description:
        yield "## Description"
        yield ""
        yield record.description
        yield ""
    if record.files:
        yield "## Files"
        yield ""
        for name, _url in record.files:
            note = (
                " (journal article; cited by PMID, not transcribed)"
                if name in record.skipped_articles
                else ""
            )
            yield f"- {name}{note}"
        yield ""
    for name, text in record.attachments.items():
        yield f"## Attachment: {name}"
        yield ""
        yield text
        yield ""
    if record.citation:
        yield "## Suggested citation"
        yield ""
        yield record.citation
        yield ""
    yield "## Source"
    yield ""
    yield (
        f"PheKB phenotype page {record.node_id}. PDF algorithm documents are "
        "transcribed by text extraction; journal articles and non-PDF "
        "attachments are listed only. PheKB states no licence for its content."
    )
    yield ""
    yield f"[PheKB record]({record.url})"


def _md_table(headers: list[str], rows: list[tuple[str, str]]) -> Iterator[str]:
    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        cells = [" ".join(str(cell).split()).replace("|", r"\|") for cell in row]
        yield "| " + " | ".join(cells) + " |"


class PheKBSource(StructuredSource):
    """Per-identifier reference source over PheKB phenotype pages."""

    prefix: ClassVar[str] = "PHEKB"
    id_pattern: ClassVar[re.Pattern] = re.compile(r"\d+")

    def __init__(
        self, data_dir: Path, cache_dir: Path | None = None, timeout: float = 90.0
    ) -> None:
        super().__init__(data_dir)
        self.cache_dir = cache_dir
        self.timeout = timeout

    def build_index(self) -> dict[str, object]:
        """No bulk file: pages are fetched per identifier on demand."""
        return {}

    def identifiers(self) -> Iterable[str]:
        if self.cache_dir is None or not self.cache_dir.is_dir():
            return []
        return sorted(
            p.stem.removeprefix("PHEKB_") for p in self.cache_dir.glob("PHEKB_*.md")
        )

    def fetch(self, identifier: str) -> PhenotypePage:  # pragma: no cover - network
        node_id = normalize_identifier(identifier)
        headers = {"User-Agent": "dismech-reference-cache"}
        # phekb.org omits its intermediate certificate; the OS trust store
        # (truststore) completes the chain, certifi's bundle cannot.
        verify = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        with httpx.Client(
            timeout=self.timeout, follow_redirects=True, headers=headers, verify=verify
        ) as client:
            response = client.get(f"{SITE_ROOT}/node/{node_id}")
            response.raise_for_status()
            record = parse_page(response.text, node_id=node_id)
            for name, url in record.files:
                if not unquote(url).lower().endswith(".pdf"):
                    continue
                data = client.get(url).raise_for_status().content
                first, full = pdf_text(data)
                if is_journal_article(first):
                    record.skipped_articles.append(name)
                    continue
                record.attachments[name] = clean_text(full)
        return record

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        return entry_for(self.fetch(identifier))


def entry_for(record: PhenotypePage) -> ReferenceCacheEntry:
    """The cache entry for a parsed page."""
    return ReferenceCacheEntry(
        reference_id=f"PHEKB:{record.node_id}",
        title=record.title,
        body=render_body(record),
        content_type="structured_record",
        extra_frontmatter={"database": "PheKB"},
    )

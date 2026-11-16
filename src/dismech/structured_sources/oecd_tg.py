"""OECD Test Guideline reference source.

An OECD Test Guideline is a primary source for *non-animal method* curation:
TG 442D defines the five in-vitro skin-sensitisation methods a disease entry
cites as ``experimental_models``, states which key event each addresses, and
states each one's applicability limits. None of that could be quoted.

The guideline resolves as a DOI and caches with no body. ``just fetch-reference
DOI:10.1787/9789264229822-en`` returns the right title and
``content_type: unavailable``, because the OECD iLibrary landing page carries no
abstract -- the content is in a PDF behind it. So an evidence item citing that
DOI has nothing for ``linkml-reference-validator`` to match a snippet against,
and a curator who wants to state what the guideline says has to quote some other
paper's introduction instead. ``Contact_Dermatitis`` already does exactly that:
the fact that KeratinoSens is accepted under TG 442D is cited to the LuSens
inter-laboratory paper, correctly marked ``quote_role: BACKGROUND``, because
there was no way to cite the guideline itself.

This source supplies the missing body from the committed paragraph index
(``data/oecd_tg/*-paragraphs.json``), so ``OECDTG:442D`` becomes an ordinary
quotable reference and a snippet is checked against the guideline's own words.

**It is not a second extraction, and it adds nothing.** The index is built by
``scripts/extract_oecd_tg.py`` from a sha256-pinned PDF and re-extracts
byte-identical; this module only renders it. Two consequences worth keeping in
mind:

- The body carries the paragraphs the index carries, which is the General
  Introduction plus each appendix's Initial Considerations and Principle of the
  Test. ``PROCEDURE``, ``DATA AND REPORTING`` and the annexes are deliberately
  out of scope, so a method's licence terms, its cell-line supplier and its nAA
  formula are **not** quotable here. That is the extraction's scope line, not a
  gap in this file; widening it means re-running the extractor with a wider
  section list.
- One file per guideline, with one section per paragraph, following
  ``OrphanetSource``: the citation is the guideline and the paragraph is the
  quoted row. A paragraph's text sits on a single line, so any sentence of it is
  a substring of the body.

Paragraph keys are ``<number>/<division>/<n>`` -- ``442D/IA/8``, ``442D/GI/2``
-- because the guideline restarts paragraph numbering in every appendix, so
"paragraph 8" alone names five different paragraphs.
"""

from __future__ import annotations

import json
import logging
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar

from dismech.structured_sources.base import ReferenceCacheEntry, StructuredSource

logger = logging.getLogger(__name__)

# "OECD TG 442D" -> "442D". The manifest writes the human form; the CURIE local
# part is the guideline number, which is what a curator cites and what the
# paragraph keys already use.
_ID_FROM_MANIFEST = re.compile(r"^OECD\s+TG\s+(?P<number>\S+)$", re.IGNORECASE)

PREFIX = "OECDTG"


@dataclass
class _Paragraph:
    """One in-scope paragraph of a guideline."""

    citation_key: str
    division: str
    number: int
    text: str
    section: str = ""
    subheading: str = ""
    pdf_pages: tuple[int, ...] = ()

    @property
    def page_range(self) -> str:
        """The PDF page or page span this paragraph was read from."""
        if not self.pdf_pages:
            return ""
        first, last = self.pdf_pages[0], self.pdf_pages[-1]
        return str(first) if first == last else f"{first}-{last}"


@dataclass
class _GuidelineRecord:
    """One guideline: its manifest metadata plus its indexed paragraphs."""

    reference_id: str
    number: str
    title: str
    citation: str
    doi: str
    adopted: str
    sha256: str
    pages: int | None
    section: str
    paragraphs: list[_Paragraph] = field(default_factory=list)
    division_titles: dict[str, str] = field(default_factory=dict)
    methods: list[dict] = field(default_factory=list)

    @property
    def divisions(self) -> list[str]:
        """Divisions in the order the index lists their paragraphs."""
        seen: list[str] = []
        for p in self.paragraphs:
            if p.division not in seen:
                seen.append(p.division)
        return seen


class OECDTestGuidelineSource(StructuredSource):
    """Serialize a committed OECD Test Guideline paragraph index as a reference.

    Unlike every other source here, there are no ``bulk_files``: the data is
    already in the repository. The guideline PDF is pinned by sha256 in
    ``data/oecd_tg/MANIFEST.yaml`` and deliberately **not** committed (OECD
    guidelines are CC BY 4.0, but a 3 MB PDF is not review material), while the
    index extracted from it is. So ``refresh()`` has nothing to download, and a
    rebuild is offline and deterministic.
    """

    prefix: ClassVar[str] = PREFIX
    id_pattern: ClassVar[re.Pattern] = re.compile(r"^OECDTG:[A-Za-z0-9.]+$")
    bulk_files: ClassVar[tuple] = ()

    _manifest: ClassVar[dict] = {}
    _manifest_path: ClassVar[Path | None] = None

    @classmethod
    def load_manifest(cls, manifest_path: Path) -> None:
        """Read the guideline manifest that pins each PDF and names its index."""
        import yaml

        if not manifest_path.exists():
            return
        with manifest_path.open(encoding="utf-8") as fh:
            cls._manifest = yaml.safe_load(fh) or {}
        cls._manifest_path = manifest_path

    # ----- indexing -----

    def build_index(self) -> dict[str, _GuidelineRecord]:
        guidelines = (type(self)._manifest or {}).get("guidelines") or []
        if not guidelines:
            raise FileNotFoundError(
                f"no guidelines in {type(self)._manifest_path or self.data_dir}; "
                "expected data/oecd_tg/MANIFEST.yaml with a `guidelines:` list"
            )
        index: dict[str, _GuidelineRecord] = {}
        for entry in guidelines:
            record = self._record_from_manifest_entry(entry)
            index[record.reference_id] = record
        return index

    def _record_from_manifest_entry(self, entry: dict) -> _GuidelineRecord:
        raw_id = str(entry.get("id", "")).strip()
        match = _ID_FROM_MANIFEST.match(raw_id)
        if match is None:
            raise ValueError(
                f"manifest guideline id {raw_id!r} is not of the form "
                '"OECD TG <number>", so its CURIE cannot be derived'
            )
        number = match.group("number")

        index_name = entry.get("index")
        if not index_name:
            raise ValueError(f"{raw_id} has no `index:` naming its paragraph index")
        index_path = self.data_dir / str(index_name)
        if not index_path.exists():
            raise FileNotFoundError(
                f"{raw_id}: paragraph index {index_path} is missing. Rebuild it "
                "with `just extract-oecd-tg <pdf>` against the PDF pinned in "
                f"{type(self)._manifest_path or 'data/oecd_tg/MANIFEST.yaml'}."
            )

        with index_path.open(encoding="utf-8") as fh:
            payload = json.load(fh)

        paragraphs: list[_Paragraph] = []
        division_titles: dict[str, str] = {}
        for p in payload.get("paragraphs", []):
            key = str(p["citation_key"])
            # The division is the middle field of the citation key, which is
            # also what makes the key unique: paragraph numbering restarts in
            # every appendix, so `442D/IA/8` and `442D/IB/8` are different
            # paragraphs. Deriving it from the key rather than from a separate
            # field keeps the two from disagreeing.
            parts = key.split("/")
            if len(parts) != 3:
                raise ValueError(
                    f"{raw_id}: citation key {key!r} is not "
                    "<number>/<division>/<paragraph>"
                )
            division = parts[1]
            paragraphs.append(
                _Paragraph(
                    citation_key=key,
                    division=division,
                    number=int(p.get("paragraph_number", 0)),
                    text=str(p.get("text", "")),
                    section=_title_case_section(str(p.get("section") or "")),
                    subheading=str(p.get("subheading") or ""),
                    pdf_pages=tuple(p.get("pdf_pages") or ()),
                )
            )
            division_titles.setdefault(
                division,
                _division_title(
                    division_id=str(p.get("division_id") or ""),
                    appendix=p.get("appendix"),
                ),
            )
        if not paragraphs:
            raise ValueError(
                f"{raw_id}: paragraph index {index_path} holds no paragraphs"
            )

        return _GuidelineRecord(
            reference_id=f"{PREFIX}:{number}",
            number=number,
            title=_collapse(str(entry.get("title", raw_id))),
            citation=_collapse(str(entry.get("citation", ""))),
            doi=str(entry.get("doi", "")),
            adopted=str(entry.get("adopted", "")),
            sha256=str(entry.get("sha256", "")),
            pages=entry.get("pages"),
            section=str(entry.get("section", "")),
            paragraphs=paragraphs,
            division_titles=division_titles,
            methods=list(entry.get("methods") or []),
        )

    def identifiers(self) -> Iterable[str]:
        return sorted(self.index())

    # ----- serialization -----

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        ref_id = _normalize_identifier(identifier)
        record = self.index().get(ref_id)
        if record is None:
            known = ", ".join(sorted(self.index())) or "(none)"
            raise KeyError(f"{ref_id} not found in the OECD TG index; have: {known}")
        body = "\n".join(self._render_body(record)) + "\n"
        extra = {"database": "OECD Guidelines for the Testing of Chemicals"}
        if record.adopted:
            extra["source_snapshot"] = record.adopted
        if record.sha256:
            extra["source_sha256"] = record.sha256
        if record.doi:
            extra["doi"] = record.doi
        return ReferenceCacheEntry(
            reference_id=record.reference_id,
            title=record.title[:240],
            body=body,
            content_type="structured_record",
            extra_frontmatter=extra,
        )

    def _render_body(self, rec: _GuidelineRecord) -> Iterator[str]:
        yield f"# {rec.reference_id}  {rec.title}"
        yield ""
        yield (
            f"OECD Test Guideline {rec.number}"
            + (f", adopted {rec.adopted}" if rec.adopted else "")
            + ". The paragraphs below are reproduced from the guideline."
        )
        yield ""
        yield (
            "**Scope of this record.** Only the General Introduction and each "
            "appendix's Initial Considerations and Principle of the Test are "
            "included. The PROCEDURE and DATA AND REPORTING sections and the "
            "annexes are not, so a method's procedural detail, its cell-line or "
            "tissue supplier, and its licence terms cannot be quoted from here."
        )
        yield ""

        if rec.methods:
            yield "## Test methods"
            yield ""
            yield from _md_table(
                ["Appendix", "Test method"],
                [(m.get("appendix", "-"), m.get("name", "-")) for m in rec.methods],
            )
            yield ""

        yield "## Divisions"
        yield ""
        yield (
            "The guideline restarts paragraph numbering in every appendix, so a "
            "paragraph is keyed by division as well as by number."
        )
        yield ""
        yield from _md_table(
            ["Key", "Division", "Paragraphs"],
            [
                (
                    f"{rec.number}/{division}",
                    rec.division_titles.get(division, division),
                    sum(1 for p in rec.paragraphs if p.division == division),
                )
                for division in rec.divisions
            ],
        )
        yield ""

        yield "## Paragraphs"
        yield ""
        for para in rec.paragraphs:
            yield f"### {para.citation_key}"
            yield ""
            # Where the paragraph sits, so a reader can tell an Initial
            # Considerations statement from a Principle of the Test one without
            # going back to the PDF, and can find it there if they want to.
            locators = [rec.division_titles.get(para.division, para.division)]
            if para.section:
                locators.append(para.section)
            if para.subheading:
                locators.append(para.subheading)
            if para.page_range:
                locators.append(f"PDF p. {para.page_range}")
            yield "*" + " · ".join(locators) + "*"
            yield ""
            yield para.text
            yield ""

        yield "## Source"
        yield ""
        if rec.citation:
            yield rec.citation
        yield ""
        details = []
        if rec.doi:
            details.append(f"DOI: https://doi.org/{rec.doi}")
        if rec.section:
            details.append(rec.section)
        if rec.pages:
            details.append(f"{rec.pages} pages")
        if rec.sha256:
            details.append(f"PDF sha256: `{rec.sha256}`")
        for line in details:
            yield f"- {line}"
        yield ""
        yield (
            "The DOI resolves to whichever edition is current, which is not "
            "necessarily the edition quoted here; the sha256 above is the durable "
            "identifier for the pinned PDF. The text was extracted by "
            "`scripts/extract_oecd_tg.py` and is committed under `data/oecd_tg/`, "
            "so this record is reproducible offline and byte-identical on "
            "re-extraction."
        )
        yield ""
        yield (
            "License: OECD Guidelines for the Testing of Chemicals are published "
            "under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). "
            "Quoted guideline text is attributed to the OECD; see NOTICE."
        )


# ----- helpers -----


def _collapse(text: str) -> str:
    """Collapse the whitespace a folded YAML scalar introduces."""
    return re.sub(r"\s+", " ", text).strip()


def _division_title(*, division_id: str, appendix: object) -> str:
    """A readable name for a division.

    The index records an appendix letter (``IA``) and a slug
    (``appendix-ia``, ``general-introduction``). The letter is authoritative
    where present; otherwise the slug title-cases cleanly, since the only
    non-appendix division is the General Introduction.
    """
    if appendix:
        return f"Appendix {appendix}"
    if division_id:
        return division_id.replace("-", " ").title()
    return ""


def _title_case_section(section: str) -> str:
    """Render an all-caps section heading as running text.

    The guideline prints section headings in capitals ("INITIAL
    CONSIDERATIONS, APPLICABILITY AND LIMITATIONS"), which reads as shouting in
    a locator line. Only the all-caps case is touched, so a heading that is
    already mixed case is left exactly as the guideline set it.
    """
    if not section or section != section.upper():
        return section
    titled = section.title()
    # `.title()` capitalises after every non-letter, so "AND" -> "And" is
    # wanted but a hyphenated or possessive word would come back wrong. Only
    # the small joining words need lowering back down.
    for word in (" And ", " Or ", " Of ", " The ", " To ", " For "):
        titled = titled.replace(word, word.lower())
    return titled


def _normalize_identifier(identifier: str) -> str:
    """Accept the spellings a curator or recipe might pass.

    ``OECDTG:442D``, ``oecdtg:442d`` and a bare ``442D`` all name one record.
    The guideline number is upper-cased because the suffix letter is part of it
    (``442D`` is a different guideline from ``442C``), and lower case would make
    two spellings of one identifier -- the ``CGGV:``/``cggv:`` confusion in the
    `fetch-reference` recipe's own comment.
    """
    raw = identifier.strip()
    if ":" in raw:
        prefix, _, local = raw.partition(":")
        if prefix.upper() != PREFIX:
            raise ValueError(
                f"{identifier!r} is not an {PREFIX}: identifier "
                f"(prefix {prefix!r})"
            )
        raw = local
    return f"{PREFIX}:{raw.strip().upper()}"


def _md_table(headers: list[str], rows: Iterable[tuple]) -> Iterator[str]:
    """Render a markdown table whose rows are stable quotable substrings."""
    yield "| " + " | ".join(headers) + " |"
    yield "| " + " | ".join("---" for _ in headers) + " |"
    for row in rows:
        yield "| " + " | ".join(str(cell) for cell in row) + " |"

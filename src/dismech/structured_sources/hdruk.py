"""HDR UK Phenotype Library structured-database source.

Ingests phenotype records from the `HDR UK Phenotype Library
<https://phenotypes.healthdatagateway.org/>`_ so a disease entry's
``definitions`` can cite a computable phenotype as ``HDRUK:PH304`` and quote
its definition text or individual codelist rows as evidence ``snippet:``
values.

The library exposes an open REST API, so records are fetched **per
identifier** on demand (the ICTRP posture): there is no bulk file to pin, and
``identifiers()`` reports what is already cached. Each record becomes one
``references_cache/HDRUK_<PHnnn>.md`` file holding

* a ``## Record`` key/value table (name, version, type, collections, coding
  systems, data sources, the library's own ontology tag),
* the library's free-text ``## Definition`` (and ``## Validation`` when the
  record has one), and
* a ``## Codes`` table, one row per code, ``| <CURIE> | <description> |
  <concept> |``, where the CURIE prefix is the dismech ``CodeSystemEnum``
  value for the library's coding system. A row is a stable quotable substring,
  and it is what ``just check-codelists`` compares a transcribed code list
  against.

Codes are taken from the library's resolved export
(``/export/codes/``), which has already applied each concept's include and
exclude rules, so every row is a code that qualifies.

The record's ``owner`` (a site username) is deliberately not cached.
"""

from __future__ import annotations

import logging
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import ClassVar

import httpx

from dismech.structured_sources.base import ReferenceCacheEntry, StructuredSource

logger = logging.getLogger(__name__)

API_ROOT = "https://phenotypes.healthdatagateway.org/api/v1"
SITE_ROOT = "https://phenotypes.healthdatagateway.org"

#: HDR UK coding-system name -> dismech ``CodeSystemEnum`` value (the CURIE
#: prefix of each code). Systems absent here have no dismech code system;
#: their codes are cached under the library's own system name with no CURIE.
CODE_SYSTEM_PREFIXES: dict[str, str] = {
    "ICD10 codes": "ICD10",
    "ICD9 codes": "ICD9CM",
    "ICD-10-CM": "ICD10CM",
    "SNOMED CT codes": "SNOMEDCT",
    "Read codes v2": "READ2",
    "Read codes v3": "CTV3",
    "CTV3 codes": "CTV3",
    "OPCS4 codes": "OPCS4",
}


def code_system_prefix(name: str) -> str | None:
    """Map an HDR UK coding-system name to a dismech code-system prefix.

    The library spells SNOMED with a double space, so whitespace is collapsed
    first.

    >>> code_system_prefix("SNOMED  CT codes")
    'SNOMEDCT'
    >>> code_system_prefix("ICD10 codes")
    'ICD10'
    >>> code_system_prefix("Med codes") is None
    True
    """
    return CODE_SYSTEM_PREFIXES.get(" ".join(name.split()))


def normalize_identifier(identifier: str) -> str:
    """Strip an ``HDRUK:`` prefix and upper-case the ``PH`` id.

    >>> normalize_identifier("HDRUK:ph304")
    'PH304'
    >>> normalize_identifier(" PH3024 ")
    'PH3024'
    """
    identifier = identifier.strip()
    if identifier.upper().startswith("HDRUK:"):
        identifier = identifier[len("HDRUK:") :]
    identifier = identifier.strip().upper()
    if not re.fullmatch(r"PH\d+", identifier):
        raise KeyError(f"not an HDR UK phenotype id: {identifier!r}")
    return identifier


@dataclass(frozen=True)
class Code:
    """One qualifying code of a phenotype."""

    system: str
    code: str
    description: str
    concept: str

    @property
    def prefix(self) -> str | None:
        return code_system_prefix(self.system)

    @property
    def curie(self) -> str | None:
        """``<prefix>:<code>``, or ``None`` when the system has no prefix.

        >>> Code("ICD10 codes", "D57.0", "Sickle-cell anaemia with crisis", "c").curie
        'ICD10:D57.0'
        """
        return f"{self.prefix}:{self.code}" if self.prefix else None


@dataclass
class PhenotypeRecord:
    """One parsed HDR UK phenotype version."""

    phenotype_id: str
    version_id: int
    name: str
    definition: str = ""
    validation: str = ""
    implementation: str = ""
    fields: dict[str, str] = field(default_factory=dict)
    publications: list[str] = field(default_factory=list)
    ontology: list[tuple[str, str]] = field(default_factory=list)
    codes: list[Code] = field(default_factory=list)
    doi: str = ""
    #: Codes deliberately left out, as ``{coding system name: count}``.
    omitted: dict[str, int] = field(default_factory=dict)

    @property
    def url(self) -> str:
        return f"{SITE_ROOT}/phenotypes/{self.phenotype_id}/version/{self.version_id}/detail/"

    def concepts(self) -> dict[tuple[str, str], list[Code]]:
        """Codes grouped by ``(concept, coding system)``, in first-seen order."""
        groups: dict[tuple[str, str], list[Code]] = {}
        for code in self.codes:
            groups.setdefault((code.concept, code.system), []).append(code)
        return groups


def omit_code_systems(record: PhenotypeRecord, prefixes: set[str]) -> PhenotypeRecord:
    """Drop every code whose dismech prefix is in ``prefixes``, counting them.

    The omission is recorded in ``record.omitted`` so the cache body and the
    converted definition can both say what was left out.

    >>> r = PhenotypeRecord("PH1", 1, "x", codes=[
    ...     Code("SNOMED  CT codes", "1", "a", "c"), Code("ICD10 codes", "D57.0", "b", "c")])
    >>> kept = omit_code_systems(r, {"SNOMEDCT"})
    >>> [c.curie for c in kept.codes], kept.omitted
    (['ICD10:D57.0'], {'SNOMED CT codes': 1})
    """
    kept: list[Code] = []
    omitted = dict(record.omitted)
    for code in record.codes:
        if code.prefix in prefixes:
            system = " ".join(code.system.split())
            omitted[system] = omitted.get(system, 0) + 1
        else:
            kept.append(code)
    return replace(record, codes=kept, omitted=omitted)


def _names(items: object) -> str:
    """Join the ``name`` of each item of an API list field.

    >>> _names([{"name": "CALIBER"}, {"name": "Phenotype Library"}])
    'CALIBER; Phenotype Library'
    >>> _names(None)
    ''
    """
    if not isinstance(items, list):
        return ""
    return "; ".join(
        " ".join(str(i.get("name", "")).split()) for i in items if i.get("name")
    )


def _clean(text: object) -> str:
    """Normalize a free-text field: drop markdown escapes, keep paragraphs.

    >>> _clean("Licence v3\\\\.0 (open\\\\-government)\\n\\n\\nNext   para")
    'Licence v3.0 (open-government)\\n\\nNext para'
    >>> _clean("taken from [OpenCodelists](https://www.opencodelists.org/)")
    'taken from OpenCodelists (https://www.opencodelists.org/)'
    """
    if not text:
        return ""
    text = re.sub(r"\\([.\-_*()\[\]#!+])", r"\1", str(text))
    # A markdown link becomes "text (url)": square brackets in a quoted
    # snippet read as editorial insertions to the reference validator.
    text = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r"\1 (\2)", text)
    paragraphs = [" ".join(p.split()) for p in re.split(r"\n\s*\n", text)]
    return "\n\n".join(p for p in paragraphs if p)


def parse_record(detail: dict | list, codes: list[dict]) -> PhenotypeRecord:
    """Build a :class:`PhenotypeRecord` from the API's detail and codes payloads."""
    if isinstance(detail, list):
        if not detail:
            raise KeyError("empty HDR UK detail payload")
        detail = detail[0]
    record = PhenotypeRecord(
        phenotype_id=detail["phenotype_id"],
        version_id=int(detail["phenotype_version_id"]),
        name=" ".join(detail["name"].split()),
        definition=_clean(detail.get("definition")),
        validation=_clean(detail.get("validation")),
        implementation=_clean(detail.get("implementation")),
        doi=detail.get("doi") or "",
    )
    record.fields = {
        "Phenotype ID": record.phenotype_id,
        "Version": str(record.version_id),
        "Name": record.name,
        "Type": _names(detail.get("type")),
        "Template": (detail.get("template") or {}).get("name", ""),
        "Author": " ".join(str(detail.get("author") or "").split()),
        "Organisation": (detail.get("organisation") or {}).get("name", ""),
        "Collections": _names(detail.get("collections")),
        "Coding systems": _names(detail.get("coding_system")),
        "Data sources": _names(detail.get("data_sources")),
        "Sex": _names(detail.get("sex")),
        "Event date range": detail.get("event_date_range") or "",
        "DOI": record.doi,
        "Phenoflow": detail.get("phenoflowid") or "",
    }
    for pub in detail.get("publications") or []:
        text = pub.get("details") if isinstance(pub, dict) else str(pub)
        if text:
            record.publications.append(" ".join(text.split()))
    for term in detail.get("ontology") or []:
        if term.get("reference_id"):
            record.ontology.append((term["reference_id"], term.get("name", "")))
    seen: set[tuple[str, str, str]] = set()
    for row in codes:
        system = " ".join(row["coding_system"]["name"].split())
        key = (row["concept_name"], system, row["code"])
        if key in seen:
            continue
        seen.add(key)
        record.codes.append(
            Code(
                system=system,
                code=str(row["code"]).strip(),
                description=" ".join(str(row.get("description") or "").split()),
                concept=" ".join(row["concept_name"].split()),
            )
        )
    record.codes = relabel_numeric_read_codes(record.codes)
    return record


#: System name given to a "Read codes v2" concept whose codes are all digits.
NUMERIC_READ_SYSTEM = "Read codes v2 (all numeric: CPRD medcodes or product codes)"


def relabel_numeric_read_codes(codes: list[Code]) -> list[Code]:
    """Relabel a Read v2 concept whose codes are all digits as unmapped.

    Some library records list CPRD medcodes or product codes (``10081``
    "Chronic uraemia", ``11536`` "Methylphenidate 20mg ...") under "Read codes
    v2". A Read v2 code has five characters drawn from digits, letters and
    dots, so a five-digit medcode passes a syntax check, but a whole concept
    with no letter or dot anywhere is not a Read list. Its codes keep their
    values and get a system name with no dismech prefix, so they are cached
    but not transcribed.

    >>> codes = [Code("Read codes v2", "10081", "Chronic uraemia", "CKD"),
    ...          Code("Read codes v2", "1803", "Nephrotic syndrome", "CKD"),
    ...          Code("Read codes v2", "21260", "Epilepsy resolved", "Epilepsy"),
    ...          Code("Read codes v2", "F25..", "Epilepsy", "Epilepsy")]
    >>> [(c.code, c.prefix) for c in relabel_numeric_read_codes(codes)]
    [('10081', None), ('1803', None), ('21260', 'READ2'), ('F25..', 'READ2')]
    """
    numeric: dict[str, bool] = {}
    for code in codes:
        if code.system == "Read codes v2":
            numeric[code.concept] = (
                numeric.get(code.concept, True) and code.code.isdigit()
            )
    return [
        replace(code, system=NUMERIC_READ_SYSTEM)
        if code.system == "Read codes v2" and numeric[code.concept]
        else code
        for code in codes
    ]


def render_body(record: PhenotypeRecord) -> str:
    """Render the cache body for a record (deterministic)."""
    return "\n".join(_render_lines(record)) + "\n"


def _render_lines(record: PhenotypeRecord) -> Iterator[str]:
    yield f"# HDRUK:{record.phenotype_id}  {record.name}"
    yield ""
    yield (
        f"**{record.phenotype_id}** version {record.version_id} — computable "
        "phenotype record from the HDR UK Phenotype Library."
    )
    yield ""
    yield "## Record"
    yield ""
    rows = [(k, v) for k, v in record.fields.items() if v]
    for curie, label in record.ontology:
        rows.append(("Ontology", f"{curie} {label}".strip()))
    yield from _md_table(["Field", "Value"], rows)
    yield ""
    for heading, text in (
        ("Definition", record.definition),
        ("Implementation", record.implementation),
        ("Validation", record.validation),
    ):
        if text:
            yield f"## {heading}"
            yield ""
            yield text
            yield ""
    if record.publications:
        yield "## Publications"
        yield ""
        for pub in record.publications:
            yield f"- {pub}"
        yield ""
    yield "## Codes"
    yield ""
    code_rows = []
    for (concept, system), codes in record.concepts().items():
        for code in sorted(codes, key=lambda c: c.code):
            code_rows.append(
                (code.curie or f"{code.code} ({system})", code.description, concept)
            )
    yield from _md_table(["Code", "Description", "Concept"], code_rows)
    yield ""
    if record.omitted:
        yield (
            "Not cached: "
            + "; ".join(f"{n} {system}" for system, n in sorted(record.omitted.items()))
            + ". See the library record for those codes."
        )
        yield ""
    yield "## Source"
    yield ""
    yield (
        f"HDR UK Phenotype Library record {record.phenotype_id} version "
        f"{record.version_id}, from the library's public API (resolved code "
        "export, include/exclude rules applied). User-submitted library content "
        "is CC BY-SA 4.0 for non-commercial use unless the Definition states a "
        "record-specific licence."
    )
    yield ""
    yield f"[HDR UK record]({record.url})"


def _md_table(headers: list[str], rows: list[tuple[str, ...]]) -> Iterator[str]:
    """Emit a markdown table whose rows are stable quotable substrings.

    >>> list(_md_table(["A", "B"], [("x|y", "z")]))
    ['| A | B |', '|---|---|', '| x\\\\|y | z |']
    """
    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        cells = [" ".join(str(cell).split()).replace("|", r"\|") for cell in row]
        yield "| " + " | ".join(cells) + " |"


class HDRUKSource(StructuredSource):
    """Per-identifier reference source over the HDR UK Phenotype Library API."""

    prefix: ClassVar[str] = "HDRUK"
    id_pattern: ClassVar[re.Pattern] = re.compile(r"PH\d+")

    def __init__(
        self,
        data_dir: Path,
        cache_dir: Path | None = None,
        timeout: float = 60.0,
    ) -> None:
        super().__init__(data_dir)
        self.cache_dir = cache_dir
        self.timeout = timeout

    def build_index(self) -> dict[str, object]:
        """No bulk file: records are fetched per identifier on demand."""
        return {}

    def identifiers(self) -> Iterable[str]:
        """Phenotype ids already present in the reference cache."""
        if self.cache_dir is None or not self.cache_dir.is_dir():
            return []
        return sorted(
            p.stem.removeprefix("HDRUK_") for p in self.cache_dir.glob("HDRUK_PH*.md")
        )

    def fetch_json(self, path: str) -> object:  # pragma: no cover - network
        with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
            response = client.get(f"{API_ROOT}/{path}", params={"format": "json"})
            response.raise_for_status()
            return response.json()

    def fetch(self, identifier: str) -> PhenotypeRecord:
        """Fetch and parse the latest *published* version of one phenotype.

        The unversioned endpoints serve the latest version, which is refused
        ("Entity version must be published") when that version is a draft,
        so the version is chosen from the record's version list first.
        """
        pid = normalize_identifier(identifier)
        versions = self.fetch_json(f"phenotypes/{pid}/get-versions/")
        version = latest_published_version(versions)
        if version is None:
            raise KeyError(f"HDR UK has no published version of {pid}")
        detail = self.fetch_json(f"phenotypes/{pid}/version/{version}/detail/")
        codes = self.fetch_json(f"phenotypes/{pid}/version/{version}/export/codes/")
        if not isinstance(codes, list):
            raise KeyError(f"HDR UK returned no code export for {pid}")
        return parse_record(detail, codes)

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        record = self.fetch(identifier)
        return entry_for(record)


def latest_published_version(versions: object) -> int | None:
    """The highest published version id in a ``get-versions`` payload.

    >>> latest_published_version([
    ...     {"version_id": 3704, "is_published": True},
    ...     {"version_id": 3900, "is_published": False}])
    3704
    >>> latest_published_version([]) is None
    True
    """
    if not isinstance(versions, list):
        return None
    published = [int(v["version_id"]) for v in versions if v.get("is_published")]
    return max(published) if published else None


def entry_for(record: PhenotypeRecord) -> ReferenceCacheEntry:
    """The cache entry for a parsed record."""
    return ReferenceCacheEntry(
        reference_id=f"HDRUK:{record.phenotype_id}",
        title=record.name,
        body=render_body(record),
        content_type="structured_record",
        extra_frontmatter={
            "database": "HDR UK Phenotype Library",
            "source_snapshot": f"{record.phenotype_id} version {record.version_id}",
        },
    )

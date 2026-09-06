"""WHO ICTRP structured-database source.

Ingests trial registration records from the **WHO International Clinical
Trials Registry Platform (ICTRP)** search portal so a ``clinical_trials``
entry can cite a trial that is *not* registered on ClinicalTrials.gov.

Why ICTRP rather than one registry at a time
--------------------------------------------
dismech's ``clinical_trials`` block was built around ClinicalTrials.gov: the
``name`` slot holds an ``NCT…`` identifier and evidence is validated against
the ClinicalTrials.gov API. Trials registered elsewhere — ChiCTR (China),
ISRCTN, EUCTR, jRCT/UMIN (Japan), CTRI (India), ANZCTR, IRCT, DRKS, and the
rest — had nowhere to go, so curators either dropped the identifier into free
text (``Registered as EudraCT 2013-004664-58``), wedged it into the trial
``name`` (``ML-DS 2006 (EudraCT 2007-006219-2)``), or wrote the bare registry
ID into ``name`` where nothing could check it. None of those forms is
machine-queryable and none is validated, which is how a nonexistent
``ChiCTR-2100045397`` survived in the knowledge base (see ``docs/ictrp.md``).

ICTRP is the WHO umbrella that aggregates every primary registry, including
ChiCTR, so **one** prefix and **one** fetch path cover all of them. It also
publishes a normalized record — the 24-element WHO Trial Registration Data
Set — which means a ChiCTR record and an ISRCTN record serialize to the same
shape. Fetching ChiCTR directly was rejected: ``chictr.org.cn`` answers
``405`` to a plain GET from outside China and exposes no documented API,
whereas the ICTRP record for the same trial is a plain ``GET`` away.

Each entry becomes one ``references_cache/ICTRP_<TrialID>.md`` file, so a
curator can cite ``ICTRP:ChiCTR2100045397`` and quote an individual row as an
evidence ``snippet:`` — the same flat-file-row pattern used by the Orphanet,
ClinGen, and ICEES sources.

No bulk file
------------
Unlike the other structured sources this one has no pinned bulk download: the
ICTRP full export is distributed under a separate data-use agreement, so
records are fetched **per identifier** on demand (the same posture as
ClinGen's report-page narrative). ``identifiers()`` therefore reports what is
already cached, which is what ``rebuild ictrp`` (no ``--id``) refreshes.

Personal contact data is deliberately dropped
---------------------------------------------
ICTRP records carry investigator names, postal addresses, telephone numbers,
and personal email addresses. Those are not evidence and republishing them
into a public git repository is not something a curation cache should do, so
:func:`parse_trial_page` keeps them out of the serialized body.
"""

from __future__ import annotations

import html
import logging
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar

import httpx

from dismech.structured_sources.base import (
    ReferenceCacheEntry,
    StructuredSource,
)

logger = logging.getLogger(__name__)

TRIAL_URL = "https://trialsearch.who.int/Trial2.aspx"

#: Registry ID prefixes ICTRP assigns, used to recognize a trial identifier in
#: free text. Note ICTRP re-keys some registries (UMIN records are
#: ``JPRN-UMIN…``; EUCTR records carry a country suffix, ``…-DE``).
REGISTRY_PREFIXES: tuple[str, ...] = (
    "ACTRN",
    "ChiCTR",
    "CTRI",
    "DRKS",
    "EUCTR",
    "IRCT",
    "ISRCTN",
    "ITMCTR",
    "JPRN",
    "KCT",
    "LBCTR",
    "NL",
    "NTR",
    "PACTR",
    "PER",
    "RBR",
    "REBEC",
    "RPCEC",
    "SLCTR",
    "TCTR",
)

_TAG = re.compile(r"(?s)<[^>]+>")
_SCRIPT = re.compile(r"(?is)<(script|style)\b.*?</\1>")
_ROW = re.compile(r"(?is)<tr\b[^>]*>(.*?)</tr>")
_CELL = re.compile(r"(?is)<td\b[^>]*>(.*?)</td>")
_DATALIST = re.compile(r'(?is)<table\b[^>]*\bid="DataList\d+"[^>]*>(.*?)</table>')
_BR = re.compile(r"(?i)<br\s*/?>")

# Field labels lifted from the portal's "Main" key/value table, in the order
# they are emitted into the ``## Registration`` table. The portal labels are
# used verbatim as row keys so a curator reading the cached record and a
# curator reading trialsearch.who.int see the same words.
_MAIN_FIELDS: tuple[str, ...] = (
    "Register",
    "Main ID",
    "Date of registration",
    "Prospective Registration",
    "Primary sponsor",
    "Date of first enrolment",
    "Target sample size",
    "Recruitment status",
    "Study type",
    "Study design",
    "Phase",
    "Countries of recruitment",
    "Date of completion",
    "Results available",
    "Date of first publication",
    "URL",
    "URL of the protocol",
    "Last refreshed on",
)

# Free-text section headings, mapped from the portal's own heading to the
# heading used in the cached body.
_SECTIONS: tuple[tuple[str, str], ...] = (
    (
        "Health Condition(s) or Problem(s) studied",
        "Health condition(s) or problem(s) studied",
    ),
    ("Intervention(s)", "Intervention(s)"),
    ("Key inclusion & exclusion criteria", "Key inclusion & exclusion criteria"),
    ("Primary Outcome(s)", "Primary outcome(s)"),
    ("Secondary Outcome(s)", "Secondary outcome(s)"),
    ("Secondary ID(s)", "Secondary ID(s)"),
    ("Source(s) of Monetary Support", "Source(s) of monetary support"),
    ("Results", "Results"),
)

# Labels naming investigator personal data. Registries do not agree on these
# ("Telephone" in a ChiCTR record, "Contact telephone" in a JPRN one), so the
# check below is deliberately broad — over-dropping loses a field nobody cites,
# while under-dropping republishes someone's phone number.
_CONTACT_LABELS = frozenset(
    {
        "Address",
        "Affiliation",
        "Email",
        "Name",
        "Telephone",
    }
)
_CONTACT_LABEL_RE = re.compile(r"(?i)^contact\b|e-?mail|telephone|address|affiliation")


def _is_contact_label(label: str) -> bool:
    """True for labels carrying investigator personal data."""
    return label in _CONTACT_LABELS or bool(_CONTACT_LABEL_RE.search(label))


class TrialNotFound(KeyError):
    """Raised when ICTRP has no record for the requested trial identifier."""


@dataclass
class TrialRecord:
    """One parsed ICTRP trial registration record."""

    trial_id: str
    fields: dict[str, str] = field(default_factory=dict)
    sections: dict[str, list[str]] = field(default_factory=dict)
    public_title: str = ""
    scientific_title: str = ""

    @property
    def register(self) -> str:
        return self.fields.get("Register", "")

    @property
    def title(self) -> str:
        return self.public_title or self.scientific_title or self.trial_id

    @property
    def registration_year(self) -> str | None:
        match = re.search(
            r"\b(1[89]|20)\d{2}\b", self.fields.get("Date of registration", "")
        )
        return match.group(0) if match else None


# ----- HTML parsing -----


def _text(fragment: str) -> str:
    """Flatten an HTML fragment to plain text, keeping ``<br>`` line breaks."""
    fragment = _SCRIPT.sub(" ", fragment)
    fragment = _BR.sub("\n", fragment)
    fragment = _TAG.sub(" ", fragment)
    fragment = html.unescape(fragment)
    fragment = fragment.replace("\xa0", " ")
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in fragment.splitlines()]
    return "\n".join(line for line in lines if line).strip()


def _join_label_lines(text: str) -> str:
    """Re-join a bare ``Label:`` line with the value on the line below it.

    Registries emit eligibility sub-fields as their own markup elements, which
    flatten to ``"Age minimum:\\n18"``. Joining them keeps a quotable snippet
    readable as ``Age minimum: 18``.
    """
    lines = text.splitlines()
    out: list[str] = []
    for line in lines:
        if out and out[-1].endswith(":"):
            out[-1] = f"{out[-1]} {line}"
        else:
            out.append(line)
    return "\n".join(out)


def _key_values(page: str) -> list[tuple[str, str]]:
    """Extract label/value pairs from the portal's two-cell ``Main`` rows."""
    pairs: list[tuple[str, str]] = []
    for row in _ROW.findall(page):
        cells = _CELL.findall(row)
        if len(cells) != 2:
            continue
        label = _text(cells[0]).rstrip(":").strip()
        value = _text(cells[1])
        if label and value:
            pairs.append((label, value))
    return pairs


def _datalist_sections(page: str) -> dict[str, list[str]]:
    """Extract the portal's ``DataListN`` sections as ``{heading: [values]}``.

    Each section table opens with a heading row and is followed by zero or
    more value rows. A section with no value rows (very common — most trials
    register no secondary IDs) is omitted rather than emitted empty.
    """
    sections: dict[str, list[str]] = {}
    for block in _DATALIST.findall(page):
        rows = _ROW.findall(block)
        if not rows:
            continue
        heading = _text(rows[0])
        if not heading:
            continue
        values: list[str] = []
        for row in rows[1:]:
            for cell in _CELL.findall(row):
                value = _join_label_lines(_text(cell))
                if value:
                    values.append(value)
        if values:
            sections.setdefault(heading, []).extend(values)
    return sections


def parse_trial_page(page: str) -> TrialRecord:
    """Parse an ICTRP ``Trial2.aspx`` page into a :class:`TrialRecord`.

    Raises :class:`TrialNotFound` when the portal returns its "record not
    found" shell — which it serves with HTTP 200 and empty section headings,
    so the status code cannot be used to detect absence.
    """
    main_id = re.search(r'TrialIDLabel"[^>]*>([^<]+)<', page)
    if not main_id:
        raise TrialNotFound("no trial record in ICTRP response")
    trial_id = html.unescape(main_id.group(1)).strip()
    if not trial_id:
        raise TrialNotFound("empty trial identifier in ICTRP response")

    record = TrialRecord(trial_id=trial_id)
    for label, value in _key_values(page):
        if _is_contact_label(label):
            # Investigator personal data — deliberately not cached.
            continue
        if label == "Public title":
            record.public_title = value
        elif label == "Scientific title":
            record.scientific_title = value
        record.fields.setdefault(label, value)

    sections = _datalist_sections(page)
    for portal_heading, out_heading in _SECTIONS:
        values = sections.get(portal_heading)
        if values:
            record.sections[out_heading] = values

    countries = sections.get("Countries of recruitment")
    if countries and "Countries of recruitment" not in record.fields:
        record.fields["Countries of recruitment"] = "; ".join(countries)

    return record


# ----- source -----


class ICTRPSource(StructuredSource):
    """Per-identifier reference source over the WHO ICTRP search portal."""

    prefix: ClassVar[str] = "ICTRP"
    # ICTRP identifiers are registry-assigned and irregular: CTRI uses
    # slashes (``CTRI/2021/05/033585``), EUCTR uses hyphens and a country
    # suffix, ISRCTN is alphanumeric.
    id_pattern: ClassVar[re.Pattern] = re.compile(
        r"[A-Za-z][A-Za-z0-9][A-Za-z0-9./_-]*"
    )

    def __init__(
        self,
        data_dir: Path,
        cache_dir: Path | None = None,
        timeout: float = 60.0,
    ) -> None:
        super().__init__(data_dir)
        self.cache_dir = cache_dir
        self.timeout = timeout

    # ----- indexing -----

    def build_index(self) -> dict[str, object]:
        """No bulk file: ICTRP records are fetched per identifier on demand."""
        return {}

    def identifiers(self) -> Iterable[str]:
        """Trial identifiers already present in the reference cache.

        This is what ``rebuild ictrp`` without ``--id`` refreshes. A new trial
        is added by naming it explicitly with ``--id``.
        """
        if self.cache_dir is None or not self.cache_dir.is_dir():
            return []
        found = set()
        for path in self.cache_dir.glob("ICTRP_*.md"):
            reference_id = _reference_id_from_cache(path)
            if reference_id:
                found.add(reference_id)
        return sorted(found)

    # ----- fetching -----

    def fetch_page(self, trial_id: str) -> str:
        """Fetch the raw ICTRP portal page for ``trial_id``."""
        with httpx.Client(timeout=self.timeout, follow_redirects=True) as client:
            response = client.get(TRIAL_URL, params={"TrialID": trial_id})
            response.raise_for_status()
            return response.text

    def fetch(self, trial_id: str) -> TrialRecord:
        """Fetch and parse one trial record."""
        try:
            page = self.fetch_page(trial_id)
        except httpx.HTTPError as exc:  # pragma: no cover - network dependent
            raise KeyError(f"ICTRP fetch failed for {trial_id}: {exc}") from exc
        try:
            return parse_trial_page(page)
        except TrialNotFound as exc:
            raise TrialNotFound(
                f"ICTRP has no record for trial identifier {trial_id!r}. "
                "Check the identifier against https://trialsearch.who.int — a "
                "registry ID transcribed from a paper is often malformed "
                "(ChiCTR IDs carry no hyphen after the registry name)."
            ) from exc

    # ----- serialization -----

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        trial_id = normalize_identifier(identifier)
        record = self.fetch(trial_id)
        body = "\n".join(self._render_body(record)) + "\n"
        extra: dict[str, object] = {"database": "WHO ICTRP"}
        year = record.registration_year
        if year:
            extra["year"] = year
        return ReferenceCacheEntry(
            reference_id=f"ICTRP:{record.trial_id}",
            title=record.title,
            body=body,
            content_type="structured_record",
            extra_frontmatter=extra,
        )

    def _render_body(self, record: TrialRecord) -> Iterator[str]:
        yield f"# ICTRP:{record.trial_id}  {record.title}"
        yield ""
        register = record.register or "an ICTRP primary registry"
        yield (
            f"**{record.trial_id}** — trial registration record from **{register}**, "
            "as normalized by the WHO International Clinical Trials Registry Platform "
            "(24-element WHO Trial Registration Data Set)."
        )
        yield ""

        yield "## Registration"
        yield ""
        rows = [
            (label, record.fields[label])
            for label in _MAIN_FIELDS
            if record.fields.get(label)
        ]
        yield from _md_table(["Field", "Value"], rows)
        yield ""

        if record.public_title or record.scientific_title:
            yield "## Titles"
            yield ""
            if record.public_title:
                yield f"- Public title: {_inline(record.public_title)}"
            if record.scientific_title:
                yield f"- Scientific title: {_inline(record.scientific_title)}"
            yield ""

        for _portal_heading, heading in _SECTIONS:
            values = record.sections.get(heading)
            if not values:
                continue
            yield f"## {heading}"
            yield ""
            for value in values:
                yield value
                yield ""

        yield "## Source"
        yield ""
        yield (
            "WHO International Clinical Trials Registry Platform (ICTRP) search "
            f"portal record for **{record.trial_id}**, sourced from the "
            f"{register} primary registry"
            + (
                f" and last refreshed by ICTRP on {record.fields['Last refreshed on']}."
                if record.fields.get("Last refreshed on")
                else "."
            )
        )
        yield ""
        yield (
            "Trials posted on the ICTRP search portal are not endorsed by WHO; they "
            "are provided as a service. Investigator contact details present in the "
            "source record are deliberately omitted here."
        )
        yield ""
        yield f"[ICTRP record]({TRIAL_URL}?TrialID={record.trial_id})"
        source_url = record.fields.get("URL")
        if source_url and source_url.startswith(("http://", "https://")):
            yield ""
            yield f"[Source register record]({source_url})"


# ----- helpers -----


def normalize_identifier(identifier: str) -> str:
    """Strip an ``ICTRP:`` prefix and surrounding whitespace."""
    identifier = identifier.strip()
    if identifier.upper().startswith("ICTRP:"):
        identifier = identifier[len("ICTRP:") :].strip()
    return identifier


def _inline(text: str) -> str:
    """Collapse a multi-line value onto one line (for bullet rendering)."""
    return " ".join(text.split())


def _reference_id_from_cache(path: Path) -> str | None:
    """Recover the trial identifier from a cache file's ``reference_id``."""
    for line in path.read_text(encoding="utf-8").splitlines()[:20]:
        match = re.match(r'\s*reference_id:\s*"?ICTRP:([^"\s]+)"?\s*$', line)
        if match:
            return match.group(1)
    return None


def _md_table(headers: list[str], rows: list[tuple[str, str]]) -> Iterator[str]:
    """Emit a markdown table whose rows are stable quotable substrings."""
    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        cells = [_inline(cell).replace("|", r"\|") for cell in row]
        yield "| " + " | ".join(cells) + " |"

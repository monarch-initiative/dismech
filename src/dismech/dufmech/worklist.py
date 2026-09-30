"""Build the first DUF/Pfam worklist from InterPro.

The DUFMech seed set starts with Pfam families whose public InterPro metadata
still looks like a domain or protein of unknown function. The InterPro
``search=DUF`` result is deliberately broad, so this module normalizes each
``entry/pfam`` record, drops text-search false positives, and marks families
whose DUF short name now looks historical rather than unknown.
"""

from __future__ import annotations

import csv
import io
import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import asdict, dataclass
from typing import Any

import httpx
from bs4 import BeautifulSoup

INTERPRO_PFAM_URL = "https://www.ebi.ac.uk/interpro/api/entry/pfam/"
EXTRA_FIELDS = "entry_id,short_name,description,counters"

PFAM_RE = re.compile(r"^PF\d{5}$")
DUF_SHORT_NAME_RE = re.compile(r"\bDUF\d+\b", re.IGNORECASE)
UNKNOWN_FUNCTION_RE = re.compile(
    r"\b(?:domain|protein)s? of unknown function\b|"
    r"\bfunction of (?:this|the) (?:domain|protein) is unknown\b|"
    r"\bfunction is unknown\b",
    re.IGNORECASE,
)

UNKNOWN_CANDIDATE = "UNKNOWN_CANDIDATE"
KNOWN_HISTORICAL_DUF = "KNOWN_HISTORICAL_DUF"
FALSE_POSITIVE_TEXT_HIT = "FALSE_POSITIVE_TEXT_HIT"

STATUS_ORDER = {
    UNKNOWN_CANDIDATE: 0,
    KNOWN_HISTORICAL_DUF: 1,
    FALSE_POSITIVE_TEXT_HIT: 2,
}


class InterProClientError(RuntimeError):
    """Raised when InterPro returns an invalid or failing response."""


@dataclass(frozen=True)
class DufFamilyRow:
    """One normalized Pfam family candidate from InterPro."""

    pfam_id: str
    short_name: str
    name: str
    interpro_id: str
    unknown_status: str
    candidate_reasons: tuple[str, ...]
    proteins: int | None
    matches: int | None
    proteomes: int | None
    taxa: int | None
    structures: int | None
    alphafold_models: int | None
    domain_architectures: int | None
    description: str

    @property
    def source_url(self) -> str:
        return f"https://www.ebi.ac.uk/interpro/api/entry/pfam/{self.pfam_id}"

    def tsv_row(self) -> dict[str, object]:
        row = asdict(self)
        row["candidate_reasons"] = ";".join(self.candidate_reasons)
        row["source_url"] = self.source_url
        return row


class InterProPfamClient:
    """Small client for the InterPro Pfam entry endpoint."""

    def __init__(
        self,
        *,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        self.timeout = timeout
        self.transport = transport

    def iter_entries(
        self,
        *,
        search: str = "DUF",
        page_size: int = 200,
    ) -> Iterable[Mapping[str, Any]]:
        params: dict[str, str] | None = {
            "search": search,
            "page_size": str(page_size),
            "extra_fields": EXTRA_FIELDS,
        }
        next_url: str | None = INTERPRO_PFAM_URL
        with httpx.Client(
            timeout=self.timeout,
            follow_redirects=True,
            transport=self.transport,
        ) as client:
            while next_url:
                response = client.get(next_url, params=params)
                try:
                    response.raise_for_status()
                    payload = response.json()
                except (httpx.HTTPError, ValueError) as exc:
                    raise InterProClientError(
                        f"could not fetch InterPro page {next_url}"
                    ) from exc
                if not isinstance(payload, dict):
                    raise InterProClientError(
                        f"InterPro page {next_url} was not a JSON object"
                    )
                results = payload.get("results")
                if not isinstance(results, list):
                    raise InterProClientError(
                        f"InterPro page {next_url} had no results list"
                    )
                for result in results:
                    if isinstance(result, Mapping):
                        yield result
                raw_next = payload.get("next")
                next_url = raw_next if isinstance(raw_next, str) and raw_next else None
                params = None


def collect_worklist(
    entries: Iterable[Mapping[str, Any]],
    *,
    include_false_positives: bool = False,
    limit: int | None = None,
) -> list[DufFamilyRow]:
    """Normalize InterPro records into sorted DUF-family rows."""

    rows: list[DufFamilyRow] = []
    seen: set[str] = set()
    for entry in entries:
        row = row_from_interpro_entry(entry)
        if row is None or row.pfam_id in seen:
            continue
        if (
            row.unknown_status == FALSE_POSITIVE_TEXT_HIT
            and not include_false_positives
        ):
            continue
        seen.add(row.pfam_id)
        rows.append(row)
        if limit is not None and len(rows) >= limit:
            break
    return sorted(rows, key=_sort_key)


def row_from_interpro_entry(entry: Mapping[str, Any]) -> DufFamilyRow | None:
    """Return a normalized Pfam row, or ``None`` for malformed entries."""

    metadata = _mapping(entry.get("metadata"))
    accession = str(metadata.get("accession", ""))
    if not PFAM_RE.fullmatch(accession):
        return None

    extra = _mapping(entry.get("extra_fields"))
    counters = _mapping(extra.get("counters"))
    structural_models = _mapping(counters.get("structural_models"))

    short_name = _string(extra.get("short_name") or metadata.get("entry_id"))
    name = _string(metadata.get("name"))
    description = _description_text(extra.get("description"))

    candidate_reasons = _candidate_reasons(short_name, name, description)
    return DufFamilyRow(
        pfam_id=accession,
        short_name=short_name,
        name=name,
        interpro_id=_string(metadata.get("integrated")),
        unknown_status=_unknown_status(candidate_reasons),
        candidate_reasons=candidate_reasons,
        proteins=_int(counters.get("proteins")),
        matches=_int(counters.get("matches")),
        proteomes=_int(counters.get("proteomes")),
        taxa=_int(counters.get("taxa")),
        structures=_int(counters.get("structures")),
        alphafold_models=_int(structural_models.get("alphafold")),
        domain_architectures=_int(counters.get("domain_architectures")),
        description=description,
    )


def load_interpro_fixture(payload: object) -> list[Mapping[str, Any]]:
    """Load InterPro records from one page, many pages, or a raw result list."""

    if isinstance(payload, Mapping):
        results = payload.get("results")
        if isinstance(results, list):
            return [r for r in results if isinstance(r, Mapping)]
    if isinstance(payload, list):
        rows: list[Mapping[str, Any]] = []
        for item in payload:
            if isinstance(item, Mapping) and isinstance(item.get("results"), list):
                rows.extend(r for r in item["results"] if isinstance(r, Mapping))
            elif isinstance(item, Mapping):
                rows.append(item)
        return rows
    raise ValueError("expected an InterPro page object, page list, or result list")


def render_tsv(rows: Iterable[DufFamilyRow]) -> str:
    """Render rows as deterministic TSV."""

    out = io.StringIO()
    writer = csv.DictWriter(
        out,
        fieldnames=[
            "pfam_id",
            "short_name",
            "name",
            "interpro_id",
            "unknown_status",
            "candidate_reasons",
            "proteins",
            "matches",
            "proteomes",
            "taxa",
            "structures",
            "alphafold_models",
            "domain_architectures",
            "description",
            "source_url",
        ],
        dialect="excel-tab",
        lineterminator="\n",
    )
    writer.writeheader()
    for row in rows:
        writer.writerow(row.tsv_row())
    return out.getvalue().rstrip("\n")


def render_json(rows: Iterable[DufFamilyRow]) -> str:
    """Render rows as stable JSON."""

    return json.dumps(
        [{**asdict(row), "source_url": row.source_url} for row in rows],
        indent=2,
        sort_keys=True,
    )


def _candidate_reasons(
    short_name: str,
    name: str,
    description: str,
) -> tuple[str, ...]:
    haystack = f"{short_name}\n{name}\n{description}"
    reasons: list[str] = []
    if DUF_SHORT_NAME_RE.search(short_name):
        reasons.append("short_name_matches_duf")
    if DUF_SHORT_NAME_RE.search(name) and "short_name_matches_duf" not in reasons:
        reasons.append("name_matches_duf")
    if UNKNOWN_FUNCTION_RE.search(name):
        reasons.append("name_says_unknown_function")
    if UNKNOWN_FUNCTION_RE.search(description):
        reasons.append("description_says_unknown_function")
    if "domain of unknown function" in haystack.lower():
        reasons.append("domain_of_unknown_function")
    return tuple(dict.fromkeys(reasons))


def _unknown_status(candidate_reasons: tuple[str, ...]) -> str:
    if not candidate_reasons:
        return FALSE_POSITIVE_TEXT_HIT
    if any(reason.endswith("unknown_function") for reason in candidate_reasons):
        return UNKNOWN_CANDIDATE
    return KNOWN_HISTORICAL_DUF


def _sort_key(row: DufFamilyRow) -> tuple[int, int, str]:
    return (
        STATUS_ORDER.get(row.unknown_status, 99),
        -(row.proteins or 0),
        row.pfam_id,
    )


def _description_text(value: object) -> str:
    if isinstance(value, list):
        text = " ".join(
            _string(item.get("text"))
            for item in value
            if isinstance(item, Mapping)
        )
    else:
        text = _string(value)
    if not text:
        return ""
    parsed = BeautifulSoup(text, "html.parser").get_text(" ", strip=True)
    return re.sub(r"\s+", " ", parsed).strip()


def _mapping(value: object) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _int(value: object) -> int | None:
    return value if type(value) is int else None


def _string(value: object) -> str:
    return value.strip() if isinstance(value, str) else ""

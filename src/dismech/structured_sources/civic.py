"""CIViC structured-database source.

Ingests pinned CIViC accepted assertion and accepted clinical evidence TSV
exports and emits one cache record per assertion or evidence item. The
serialized bodies are deterministic text records that disease YAML evidence
items can quote with exact ``snippet:`` values.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path
from typing import ClassVar, Iterable

from dismech.structured_sources.base import (
    BulkFile,
    ReferenceCacheEntry,
    StructuredSource,
)

_ASSERTIONS_NAME = "accepted_assertion_summaries.tsv"
_EVIDENCE_NAME = "accepted_clinical_evidence_summaries.tsv"

_ASSERTION_HEADERS = [
    "molecular_profile",
    "molecular_profile_id",
    "disease",
    "doid",
    "phenotypes",
    "therapies",
    "assertion_type",
    "assertion_direction",
    "significance",
    "acmg_codes",
    "amp_category",
    "clingen_codes",
    "nccn_guideline",
    "nccn_guideline_version",
    "regulatory_approval",
    "fda_companion_test",
    "assertion_summary",
    "assertion_description",
    "assertion_id",
    "evidence_item_ids",
    "last_review_date",
    "assertion_civic_url",
    "evidence_items_civic_url",
    "molecular_profile_civic_url",
    "is_flagged",
]

_EVIDENCE_HEADERS = [
    "molecular_profile",
    "molecular_profile_id",
    "disease",
    "doid",
    "phenotypes",
    "therapies",
    "therapy_interaction_type",
    "evidence_type",
    "evidence_direction",
    "evidence_level",
    "significance",
    "evidence_statement",
    "citation_id",
    "source_type",
    "asco_abstract_id",
    "citation",
    "nct_ids",
    "rating",
    "evidence_status",
    "evidence_id",
    "variant_origin",
    "last_review_date",
    "evidence_civic_url",
    "molecular_profile_civic_url",
    "is_flagged",
]


@dataclass(frozen=True)
class _CivicAssertionRecord:
    molecular_profile: str
    molecular_profile_id: str
    disease: str
    doid: str
    phenotypes: str
    therapies: str
    assertion_type: str
    assertion_direction: str
    significance: str
    acmg_codes: str
    amp_category: str
    clingen_codes: str
    nccn_guideline: str
    nccn_guideline_version: str
    regulatory_approval: str
    fda_companion_test: str
    assertion_summary: str
    assertion_description: str
    assertion_id: str
    evidence_item_ids: str
    last_review_date: str
    assertion_civic_url: str
    evidence_items_civic_url: str
    molecular_profile_civic_url: str
    is_flagged: str

    @property
    def reference_id(self) -> str:
        return f"CIVIC_ASSERTION:{self.assertion_id}"


@dataclass(frozen=True)
class _CivicEvidenceRecord:
    molecular_profile: str
    molecular_profile_id: str
    disease: str
    doid: str
    phenotypes: str
    therapies: str
    therapy_interaction_type: str
    evidence_type: str
    evidence_direction: str
    evidence_level: str
    significance: str
    evidence_statement: str
    citation_id: str
    source_type: str
    asco_abstract_id: str
    citation: str
    nct_ids: str
    rating: str
    evidence_status: str
    evidence_id: str
    variant_origin: str
    last_review_date: str
    evidence_civic_url: str
    molecular_profile_civic_url: str
    is_flagged: str

    @property
    def reference_id(self) -> str:
        return f"CIVIC_EID:{self.evidence_id}"


class CivicSource(StructuredSource):
    """Structured source for CIViC accepted assertions and evidence items."""

    prefix: ClassVar[str] = "CIViC"
    id_pattern: ClassVar[re.Pattern] = re.compile(
        r"^(CIViC_|CIVIC_|civic[._:-])?(ASSERTION|AID|EID)[:._-]?\d+$",
        re.IGNORECASE,
    )
    bulk_files: ClassVar[tuple[BulkFile, ...]] = (
        BulkFile(
            name=_ASSERTIONS_NAME,
            url=(
                "https://civicdb.org/downloads/01-May-2026/"
                "01-May-2026-AcceptedAssertionSummaries.tsv"
            ),
            sha256="e454e37d306a093306a2d3e8037697aa38bf70de15925dc5115134f0ffece06c",
            description="CIViC accepted assertion summaries TSV",
        ),
        BulkFile(
            name=_EVIDENCE_NAME,
            url=(
                "https://civicdb.org/downloads/01-May-2026/"
                "01-May-2026-AcceptedClinicalEvidenceSummaries.tsv"
            ),
            sha256="061d4bcef4eacdce708471300d8bf2db2246c258d3630f97cac2e87b8217d8ab",
            description="CIViC accepted clinical evidence summaries TSV",
        ),
    )

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

    def build_index(
        self,
    ) -> dict[str, _CivicAssertionRecord | _CivicEvidenceRecord]:
        records: dict[str, _CivicAssertionRecord | _CivicEvidenceRecord] = {}

        with self._required_path(_ASSERTIONS_NAME).open(encoding="utf-8-sig") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            _require_headers(reader.fieldnames, _ASSERTION_HEADERS, _ASSERTIONS_NAME)
            for row in reader:
                rec = _CivicAssertionRecord(
                    **{
                        field: _clean(row.get(field, ""))
                        for field in _ASSERTION_HEADERS
                    }
                )
                if rec.assertion_id:
                    records[rec.reference_id] = rec

        with self._required_path(_EVIDENCE_NAME).open(encoding="utf-8-sig") as fh:
            reader = csv.DictReader(fh, delimiter="\t")
            _require_headers(reader.fieldnames, _EVIDENCE_HEADERS, _EVIDENCE_NAME)
            for row in reader:
                rec = _CivicEvidenceRecord(
                    **{field: _clean(row.get(field, "")) for field in _EVIDENCE_HEADERS}
                )
                if rec.evidence_id:
                    records[rec.reference_id] = rec

        return records

    def _required_path(self, name: str) -> Path:
        path = self.data_dir / name
        if not path.exists():
            raise FileNotFoundError(f"{path} not found; run `just civic-refresh` first")
        return path

    def identifiers(self) -> Iterable[str]:
        idx = self.index()
        return sorted(
            idx.keys(),
            key=lambda ident: (_sort_group(ident), _sort_number(ident), ident),
        )

    @property
    def snapshot_date(self) -> str:
        """Pinned CIViC snapshot date from the manifest."""
        manifest_date = getattr(type(self), "_manifest_snapshot_date", "")
        return manifest_date or "2026-05-01"

    @property
    def schema_tag(self) -> str:
        """Pinned CIViC export tag from the manifest."""
        manifest_tag = getattr(type(self), "_manifest_schema_tag", "")
        return manifest_tag or "01-May-2026"

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        normalized = _normalize_identifier(identifier)
        rec = self.index().get(normalized)
        if rec is None:
            raise KeyError(f"{normalized} not found in CIViC index")

        if isinstance(rec, _CivicAssertionRecord):
            return self._serialize_assertion(rec)
        return self._serialize_evidence(rec)

    def _serialize_assertion(self, rec: _CivicAssertionRecord) -> ReferenceCacheEntry:
        body = "\n".join(self._render_assertion_body(rec)) + "\n"
        title = (
            f"{rec.molecular_profile} / {rec.disease} "
            f"({rec.assertion_type} {rec.significance})"
        )
        return ReferenceCacheEntry(
            reference_id=rec.reference_id,
            title=title,
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "CIViC"},
        )

    def _serialize_evidence(self, rec: _CivicEvidenceRecord) -> ReferenceCacheEntry:
        body = "\n".join(self._render_evidence_body(rec)) + "\n"
        title = (
            f"{rec.molecular_profile} / {rec.disease} "
            f"({rec.evidence_type} {rec.significance})"
        )
        return ReferenceCacheEntry(
            reference_id=rec.reference_id,
            title=title,
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": "CIViC"},
        )

    def _render_assertion_body(self, rec: _CivicAssertionRecord) -> list[str]:
        evidence_ids = ", ".join(
            f"CIVIC_EID:{x}" for x in _csv_values(rec.evidence_item_ids)
        )
        return [
            f"# {rec.reference_id}",
            "",
            f"**{rec.reference_id}** — {rec.molecular_profile} / {rec.disease}",
            "",
            "## Assertion",
            *_bullet_lines(
                [
                    (
                        "Molecular profile",
                        _profile_label(rec.molecular_profile, rec.molecular_profile_id),
                    ),
                    ("Disease", _disease_label(rec.disease, rec.doid)),
                    ("Phenotypes", _comma_label(rec.phenotypes)),
                    ("Therapies", _comma_label(rec.therapies)),
                    ("Assertion type", rec.assertion_type),
                    ("Assertion direction", rec.assertion_direction),
                    ("Significance", rec.significance),
                    ("AMP category", rec.amp_category),
                    ("ACMG codes", _comma_label(rec.acmg_codes)),
                    ("ClinGen codes", _comma_label(rec.clingen_codes)),
                    ("NCCN guideline", _nccn_label(rec)),
                    ("Regulatory approval", rec.regulatory_approval),
                    ("FDA companion test", rec.fda_companion_test),
                    ("Evidence item IDs", evidence_ids),
                    ("Last review date", rec.last_review_date),
                    ("Flagged", rec.is_flagged),
                    ("CIViC URL", rec.assertion_civic_url),
                    ("Molecular profile URL", rec.molecular_profile_civic_url),
                ]
            ),
            "",
            "## Summary",
            "",
            rec.assertion_summary,
            "",
            "## Description",
            "",
            rec.assertion_description,
            "",
            "## Source",
            "",
            "- Database: CIViC",
            f"- Snapshot: {self.schema_tag} ({self.snapshot_date})",
            "- Export: AcceptedAssertionSummaries.tsv",
        ]

    def _render_evidence_body(self, rec: _CivicEvidenceRecord) -> list[str]:
        return [
            f"# {rec.reference_id}",
            "",
            f"**{rec.reference_id}** — {rec.molecular_profile} / {rec.disease}",
            "",
            "## Evidence item",
            *_bullet_lines(
                [
                    (
                        "Molecular profile",
                        _profile_label(rec.molecular_profile, rec.molecular_profile_id),
                    ),
                    ("Disease", _disease_label(rec.disease, rec.doid)),
                    ("Phenotypes", _comma_label(rec.phenotypes)),
                    ("Therapies", _comma_label(rec.therapies)),
                    ("Therapy interaction type", rec.therapy_interaction_type),
                    ("Evidence type", rec.evidence_type),
                    ("Evidence direction", rec.evidence_direction),
                    ("Evidence level", rec.evidence_level),
                    ("Significance", rec.significance),
                    ("Variant origin", rec.variant_origin),
                    ("Citation", _citation_label(rec)),
                    ("NCT IDs", _comma_label(rec.nct_ids)),
                    ("Rating", rec.rating),
                    ("Evidence status", rec.evidence_status),
                    ("Last review date", rec.last_review_date),
                    ("Flagged", rec.is_flagged),
                    ("CIViC URL", rec.evidence_civic_url),
                    ("Molecular profile URL", rec.molecular_profile_civic_url),
                ]
            ),
            "",
            "## Evidence statement",
            "",
            rec.evidence_statement,
            "",
            "## Source",
            "",
            "- Database: CIViC",
            f"- Snapshot: {self.schema_tag} ({self.snapshot_date})",
            "- Export: AcceptedClinicalEvidenceSummaries.tsv",
        ]


def _require_headers(
    observed: list[str] | None, expected: list[str], filename: str
) -> None:
    if observed is None:
        raise ValueError(f"{filename} is missing a header row")
    missing = [field for field in expected if field not in observed]
    if missing:
        raise ValueError(
            f"{filename} is missing required columns: {', '.join(missing)}"
        )


def _clean(value: str | None) -> str:
    return " ".join(str(value or "").strip().split())


def _csv_values(value: str) -> list[str]:
    return [part.strip() for part in value.split(",") if part.strip()]


def _comma_label(value: str) -> str:
    return ", ".join(_csv_values(value))


def _profile_label(name: str, profile_id: str) -> str:
    if not profile_id:
        return name
    return f"{name} (CIViC molecular profile {profile_id})"


def _disease_label(name: str, doid: str) -> str:
    if not doid:
        return name
    return f"{name} (DOID:{doid})"


def _nccn_label(rec: _CivicAssertionRecord) -> str:
    if rec.nccn_guideline and rec.nccn_guideline_version:
        return f"{rec.nccn_guideline} v{rec.nccn_guideline_version}"
    return rec.nccn_guideline


def _citation_label(rec: _CivicEvidenceRecord) -> str:
    identifiers: list[str] = []
    if rec.source_type == "PubMed" and rec.citation_id:
        identifiers.append(f"PMID:{rec.citation_id}")
    elif rec.citation_id:
        identifiers.append(rec.citation_id)
    if rec.asco_abstract_id:
        identifiers.append(f"ASCO:{rec.asco_abstract_id}")

    suffix = f" ({', '.join(identifiers)})" if identifiers else ""
    return f"{rec.citation}{suffix}" if rec.citation else suffix.strip(" ()")


def _bullet_lines(rows: Iterable[tuple[str, str]]) -> list[str]:
    return [f"- {label}: {value}" for label, value in rows if value]


def _sort_group(identifier: str) -> int:
    return 0 if identifier.startswith("CIVIC_ASSERTION:") else 1


def _sort_number(identifier: str) -> int:
    return int(identifier.rsplit(":", 1)[1])


def _normalize_identifier(identifier: str) -> str:
    value = identifier.strip()
    if not value:
        raise ValueError("empty CIViC identifier")

    match = re.search(r"(\d+)$", value)
    if not match:
        raise ValueError(f"cannot parse CIViC identifier: {identifier}")
    number = match.group(1)

    upper = value.upper()
    if "ASSERTION" in upper or re.search(r"(^|[_:.-])AID[_:.-]?\d+$", upper):
        return f"CIVIC_ASSERTION:{number}"
    if "EID" in upper or "EVIDENCE" in upper:
        return f"CIVIC_EID:{number}"

    raise ValueError(f"unknown CIViC identifier type: {identifier}")

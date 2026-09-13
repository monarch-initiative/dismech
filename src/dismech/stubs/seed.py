"""Seed the stub queue from an external nomination list.

The first (and currently only) supported source is the Monarch
`rare-disease-identification` prioritised list — a human-curated YAML of rare
diseases nominated for phenotypic-characterization research:
https://github.com/monarch-initiative/rare-disease-identification

Seeding is a one-way import. Once a stub file exists it is repository content
that people edit by pull request, so re-running the seeder only fills gaps; it
never rewrites or deletes an existing stub.
"""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from dismech.yaml_io import safe_load

from .model import (
    OBSOLETE_LABEL_PATTERN,
    Stub,
    build_coverage_index,
    load_stubs,
    slugify_label,
    stub_filename,
)

RDI_SOURCE_NAME = "rare-disease-identification"
RDI_SOURCE_URL = "https://github.com/monarch-initiative/rare-disease-identification"


@dataclass
class SeedResult:
    nominated: int = 0
    already_curated: int = 0
    already_stubbed: int = 0
    obsolete: int = 0
    skipped: int = 0
    written: int = 0
    paths: list[Path] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.paths is None:
            self.paths = []


@dataclass
class Nomination:
    """One disease nominated for curation, normalized across source formats."""

    mondo_id: str
    label: str
    rationale: str | None = None
    synonyms: list[str] = None  # type: ignore[assignment]
    tags: list[str] = None  # type: ignore[assignment]
    source_identifier: str | None = None

    def __post_init__(self) -> None:
        if self.synonyms is None:
            self.synonyms = []
        if self.tags is None:
            self.tags = []


def _clean_str(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def parse_rare_disease_identification(payload: Any) -> list[Nomination]:
    """Read the `prioritised-rare-disease-list.yml` shape."""
    if isinstance(payload, dict):
        entries = payload.get("diseases") or []
    else:
        entries = payload or []

    nominations: list[Nomination] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        mondo_id = _clean_str(entry.get("mondo_id"))
        label = _clean_str(entry.get("mondo_label"))
        if not mondo_id or not label:
            continue

        justifications = [
            _clean_str(j) for j in (entry.get("justification_summary") or [])
        ]
        rationale = "; ".join(j for j in justifications if j) or None

        synonyms = [
            s for s in (_clean_str(x) for x in (entry.get("mondo_synonyms") or [])) if s
        ]

        tags = []
        for key in ("prioritization_category", "prevalence_category"):
            value = _clean_str(entry.get(key))
            if value:
                tags.append(f"{key}={value}")

        nominations.append(
            Nomination(
                mondo_id=mondo_id,
                label=label,
                rationale=rationale,
                synonyms=synonyms[:8],
                tags=tags,
                source_identifier=mondo_id,
            )
        )
    return nominations


_PARSERS = {
    RDI_SOURCE_NAME: parse_rare_disease_identification,
}

_SOURCE_URLS = {
    RDI_SOURCE_NAME: RDI_SOURCE_URL,
}


def render_stub(
    nomination: Nomination,
    source_name: str,
    source_url: str | None,
    added: str | None = None,
) -> dict[str, Any]:
    """Build the stub payload for one nomination.

    Seeded stubs are deliberately conservative: `entry_type` is UNDECIDED and
    `priority` is NORMAL for everything. Deciding whether a concept is a disease
    or a grouping, and whether it outranks its neighbours, is a curator's call
    recorded in a pull request — not something an importer can infer from a
    source list.
    """
    payload: dict[str, Any] = {
        "mondo_id": nomination.mondo_id,
        "label": nomination.label,
    }
    proposed = slugify_label(nomination.label)
    if proposed:
        payload["proposed_name"] = proposed
    payload["status"] = "OPEN"
    payload["entry_type"] = "UNDECIDED"
    payload["priority"] = "NORMAL"
    if nomination.rationale:
        payload["rationale"] = nomination.rationale
    if nomination.synonyms:
        payload["synonyms"] = nomination.synonyms

    source: dict[str, Any] = {"source_name": source_name}
    if source_url:
        source["source_url"] = source_url
    if nomination.source_identifier:
        source["source_identifier"] = nomination.source_identifier
    if nomination.tags:
        source["source_tags"] = nomination.tags
    payload["sources"] = [source]
    # UTC rather than the local date, matching the `creation_date` convention
    # in kb/ entries and keeping the seed reproducible across timezones.
    payload["added_date"] = added or datetime.now(UTC).date().isoformat()
    return payload


def yaml_scalar(value: Any) -> str:
    """Emit a value as a YAML scalar that reads back as the same string.

    Shared with `scripts/enrich_curation_stubs.py`, which writes into the same
    files and had its own copy of this with the same newline hole.

    Two failure modes this has to cover, both latent rather than theoretical:
    a control character (a newline in a label) emitted bare produces a file that
    will not parse at all, and a numeric-looking string (`22`, `3.5`) emitted
    bare reads back as a number, not the string that went in. The round-trip
    check at the end is the actual guarantee -- the conditions above it are a
    fast path, and the control-character guard covers what the round trip cannot
    (PyYAML refuses to load some of those at all, so it never gets to compare).
    """
    text = str(value)
    # Control characters and NEL: PyYAML either refuses these outright or treats
    # them as line breaks, so they can never go out bare.
    if any(ch < " " or ch in "\x7f\x85" for ch in text):
        return _quote(text)
    if (
        text == ""
        or text[0] in "!&*?|>%@`'\"[]{}#,-"
        or text[-1] in " :"
        or ": " in text
        or " #" in text
    ):
        return _quote(text)
    # The actual guarantee: anything that does not read back as this exact
    # string gets quoted. Covers bools, numbers, null and dates, and also a
    # string YAML resolves to a *different* string (` leading space`), which an
    # isinstance check would wave through.
    try:
        if safe_load(text) != text:
            return _quote(text)
    except Exception:
        return _quote(text)
    return text


_NAMED_ESCAPES = {"\\": "\\\\", '"': '\\"', "\n": "\\n", "\r": "\\r", "\t": "\\t"}


def _quote(text: str) -> str:
    """Double-quote a scalar, escaping everything YAML will not take raw.

    The five named escapes are not enough on their own: PyYAML *refuses* to read
    back a quoted scalar containing a raw control character (NUL, BEL, ESC), and
    NEL (\\x85) is a line break it would act on. Unreachable with real MONDO
    labels, but this is the emitter's last line of defence, so it covers the
    whole range rather than the characters that have happened to show up.
    """
    out = []
    for ch in text:
        if ch in _NAMED_ESCAPES:
            out.append(_NAMED_ESCAPES[ch])
        elif ch < " " or ch in "\x7f\x85":
            out.append(f"\\x{ord(ch):02x}")
        else:
            out.append(ch)
    return '"' + "".join(out) + '"'


def _dump(payload: dict[str, Any]) -> str:
    """Emit a stub as YAML by hand.

    Hand-rolled rather than `yaml.safe_dump` so key order is the schema's
    reading order and long prose does not get line-wrapped mid-word — these
    files are read and edited by people in pull-request diffs.
    """
    lines: list[str] = []

    for key in (
        "mondo_id",
        "label",
        "proposed_name",
        "status",
        "entry_type",
        "priority",
        "rationale",
    ):
        if key in payload:
            lines.append(f"{key}: {yaml_scalar(payload[key])}")
    if payload.get("synonyms"):
        lines.append("synonyms:")
        lines.extend(f"- {yaml_scalar(s)}" for s in payload["synonyms"])
    if payload.get("sources"):
        lines.append("sources:")
        for source in payload["sources"]:
            lines.append(f"- source_name: {yaml_scalar(source['source_name'])}")
            for key in ("source_url", "source_identifier"):
                if source.get(key):
                    lines.append(f"  {key}: {yaml_scalar(source[key])}")
            if source.get("source_tags"):
                lines.append("  source_tags:")
                lines.extend(f"  - {yaml_scalar(t)}" for t in source["source_tags"])
    # `claimed_by` and `issue` used to be emitted here. They were removed from
    # the schema when claiming moved to GitHub, and emitting them would now
    # produce a stub that fails validation.
    if payload.get("notes"):
        lines.append(f"notes: {yaml_scalar(payload['notes'])}")
    if payload.get("added_date"):
        # Quoted so YAML hands it back as a string, matching the `creation_date`
        # convention in kb/ entries. Unquoted, PyYAML resolves it to a
        # datetime.date and schema validation rejects it as a non-string.
        lines.append(f'added_date: "{payload["added_date"]}"')
    return "\n".join(lines) + "\n"


def _existing_stub_ids(stubs: Iterable[Stub]) -> set[str]:
    return {s.mondo_id for s in stubs if s.mondo_id}


def seed_stubs(
    source: Path,
    stub_dir: Path,
    source_format: str = RDI_SOURCE_NAME,
    dry_run: bool = False,
    limit: int | None = None,
    added: str | None = None,
) -> SeedResult:
    parser = _PARSERS.get(source_format)
    if parser is None:
        raise ValueError(
            f"Unknown source format {source_format!r}; known: {sorted(_PARSERS)}"
        )

    nominations = parser(safe_load(source.read_text(encoding="utf-8")))
    coverage = build_coverage_index()
    existing = load_stubs(stub_dir) if stub_dir.is_dir() else []
    existing_ids = _existing_stub_ids(existing)
    existing_names = {s.path.name for s in existing}

    result = SeedResult(nominated=len(nominations))
    stub_dir.mkdir(parents=True, exist_ok=True)

    for nomination in nominations:
        if OBSOLETE_LABEL_PATTERN.match(nomination.label):
            # MONDO marks a retired concept by prefixing its label. Nothing
            # downstream should ever ask a curator to model one.
            result.obsolete += 1
            continue
        if coverage.covered_by(nomination.mondo_id):
            result.already_curated += 1
            continue
        if nomination.mondo_id in existing_ids:
            result.already_stubbed += 1
            continue

        filename = stub_filename(nomination.label, nomination.mondo_id)
        if filename in existing_names:
            # Two MONDO concepts whose labels slug identically. Disambiguate
            # with the MONDO ID rather than silently dropping one.
            filename = (
                f"{slugify_label(nomination.label)}"
                f"__{nomination.mondo_id.replace(':', '_')}.yaml"
            )
        if filename in existing_names:
            result.skipped += 1
            continue

        payload = render_stub(
            nomination,
            source_name=source_format,
            source_url=_SOURCE_URLS.get(source_format),
            added=added,
        )
        path = stub_dir / filename
        if not dry_run:
            path.write_text(_dump(payload), encoding="utf-8")
        existing_ids.add(nomination.mondo_id)
        existing_names.add(filename)
        result.written += 1
        result.paths.append(path)
        if limit is not None and result.written >= limit:
            break

    return result

"""Generic ontology-edge structured-database source.

Most structured sources in this package ingest a single domain database
(Orphanet, ClinGen, ICEES). :class:`OntologyEdgeSource` is different: it is a
*generic* source that selects a small, curated set of **edges** (triples /
relationships) out of an arbitrary OAK-loadable ontology and renders them as
quotable evidence rows — without caching the whole ontology.

The motivating case is the NCI Thesaurus ``NCIT:P302``
(``Accepted_Therapeutic_Use_For``) annotation, which links a drug to a
free-text description of the disease/condition it is an accepted treatment for.
But the mechanism is deliberately ontology-agnostic: point it at any
``sqlite:obo:<name>`` adapter and give it a list of predicates, and it emits one
cache file per **subject** entity containing a unified edge table::

    | ID | LABEL | PRED | TARGET_ID | TARGET_LABEL | METADATA |

For an **annotation** predicate (literal value, e.g. P302) ``TARGET_ID`` /
``TARGET_LABEL`` are blank and the literal text lands in ``METADATA``. For a
**relation** predicate (object property, e.g. ``Has_Target``) the object CURIE
and its label fill ``TARGET_ID`` / ``TARGET_LABEL``. Either way each row is a
stable substring that a curator can quote as an evidence ``snippet:`` against a
``reference: <PREFIX>:<id>`` citation.

The ontology is read through OAK's managed SQLite download (so we never commit
the multi-hundred-MB ``.db``); only the selectively generated per-subject
cache files are committed. ``data/<source>/MANIFEST.yaml`` pins the ontology
version string for provenance and drift detection.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar, Iterable, Iterator, Optional

from dismech.structured_sources.base import (
    ReferenceCacheEntry,
    StructuredSource,
)

logger = logging.getLogger(__name__)

# semsql / OBO label predicate.
_LABEL_PREDICATE = "rdfs:label"

# SQLite has a default 999-variable limit on a single statement; chunk IN-lists
# well under it.
_SQL_CHUNK = 400


@dataclass(frozen=True)
class PredicateSpec:
    """One predicate selected from the ontology.

    ``kind`` is either ``"annotation"`` (a literal value lives in the
    ``statements.value`` column) or ``"relation"`` (an object CURIE lives in the
    ``statements.object`` column and is label-resolved).
    """

    id: str
    label: str
    kind: str = "annotation"

    @property
    def is_relation(self) -> bool:
        return self.kind == "relation"


@dataclass(frozen=True)
class _EdgeRow:
    """One rendered edge row for a subject."""

    predicate_id: str
    predicate_label: str
    target_id: str
    target_label: str
    metadata: str

    def sort_key(self) -> tuple[str, str, str, str]:
        return (self.predicate_id, self.target_id, self.metadata, self.target_label)


@dataclass
class _SubjectRecord:
    """One subject entity with its selected edges."""

    subject_id: str
    subject_label: str
    edges: list[_EdgeRow] = field(default_factory=list)


class OntologyEdgeSource(StructuredSource):
    """Select curated ontology edges and render them as quotable rows.

    Configured entirely from a manifest (see :meth:`load_manifest`); the class
    itself is ontology-agnostic. NCIT ``P302`` is the first configured user.
    """

    prefix: ClassVar[str] = "ONTOEDGE"
    id_pattern: ClassVar[re.Pattern] = re.compile(r"^[A-Za-z][A-Za-z0-9.]*:.+$")

    # Populated by load_manifest.
    _adapter_string: ClassVar[str] = ""
    _ontology_name: ClassVar[str] = ""
    _ontology_short: ClassVar[str] = ""
    _ontology_version: ClassVar[str] = ""
    _snapshot_date: ClassVar[str] = ""
    _homepage: ClassVar[str] = ""
    _license: ClassVar[str] = ""
    _predicates: ClassVar[tuple[PredicateSpec, ...]] = ()

    def __init__(self, data_dir: Path) -> None:
        super().__init__(data_dir)
        self._adapter_obj = None

    # ----- manifest -----

    @classmethod
    def load_manifest(cls, manifest_path: Path) -> None:
        """Populate the source configuration from a manifest YAML."""
        from ruamel.yaml import YAML

        yaml = YAML(typ="safe")
        data = yaml.load(manifest_path)
        cls.prefix = str(data["prefix"])
        cls._adapter_string = str(data["adapter"])
        cls._ontology_name = str(data.get("ontology_name", cls.prefix))
        cls._ontology_short = str(data.get("ontology_short", cls.prefix))
        cls._ontology_version = str(data.get("ontology_version", ""))
        cls._snapshot_date = str(data.get("snapshot_date", ""))
        cls._homepage = str(data.get("homepage", ""))
        cls._license = str(data.get("license", ""))
        cls._predicates = tuple(
            PredicateSpec(
                id=str(p["id"]),
                label=str(p.get("label", p["id"])),
                kind=str(p.get("kind", "annotation")),
            )
            for p in data.get("predicates", [])
        )
        cls.id_pattern = re.compile(rf"^{re.escape(cls.prefix)}:.+$")

    # ----- ontology access -----

    def _adapter(self):
        """Return (and memoize) the OAK adapter, triggering its DB download."""
        if self._adapter_obj is None:
            from oaklib import get_adapter

            if not self._adapter_string:
                raise RuntimeError(
                    "OntologyEdgeSource not configured; load a manifest first"
                )
            self._adapter_obj = get_adapter(self._adapter_string)
        return self._adapter_obj

    def refresh(self, *, force: bool = False) -> None:
        """Ensure the OAK-managed ontology SQLite is present.

        Unlike sha256-pinned bulk sources, the ontology download is delegated
        to OAK/semsql. We instantiate the adapter (which downloads on demand)
        and warn if the on-disk version differs from the pinned manifest
        version.
        """
        adapter = self._adapter()
        actual = self._read_ontology_version(adapter)
        if self._ontology_version and actual and actual != self._ontology_version:
            logger.warning(
                "ontology version drift for %s: on disk %s, manifest pins %s",
                self.prefix,
                actual,
                self._ontology_version,
            )
        else:
            logger.info("OK  %s ontology version %s", self.prefix, actual or "?")

    @staticmethod
    def _read_ontology_version(adapter) -> str:
        from sqlalchemy import text

        with adapter.engine.connect() as conn:
            row = conn.execute(
                text(
                    "SELECT value FROM statements "
                    "WHERE predicate='owl:versionInfo' AND value IS NOT NULL "
                    "LIMIT 1"
                )
            ).fetchone()
        return str(row[0]) if row else ""

    # ----- indexing -----

    def build_index(self) -> dict[str, _SubjectRecord]:
        from sqlalchemy import text

        if not self._predicates:
            raise RuntimeError("no predicates configured; load a manifest first")

        pred_map = {p.id: p for p in self._predicates}
        adapter = self._adapter()
        records: dict[str, _SubjectRecord] = {}
        target_ids: set[str] = set()

        # Collect raw statements for the selected predicates.
        raw: list[tuple[str, str, Optional[str], Optional[str]]] = []
        with adapter.engine.connect() as conn:
            for chunk in _chunked(list(pred_map), _SQL_CHUNK):
                placeholders = ",".join(f":p{i}" for i in range(len(chunk)))
                params = {f"p{i}": pid for i, pid in enumerate(chunk)}
                stmt = text(
                    "SELECT subject, predicate, value, object FROM statements "
                    f"WHERE predicate IN ({placeholders})"
                )
                raw.extend(conn.execute(stmt, params).fetchall())

        for subject, predicate, value, obj in raw:
            spec = pred_map.get(predicate)
            if spec is None or subject is None:
                continue
            if spec.is_relation:
                if not obj:
                    continue
                target_ids.add(obj)
                edge = _EdgeRow(spec.id, spec.label, str(obj), "", "")
            else:
                if value is None or value == "":
                    continue
                edge = _EdgeRow(spec.id, spec.label, "", "", _clean(value))
            rec = records.get(subject)
            if rec is None:
                rec = _SubjectRecord(subject_id=subject, subject_label="")
                records[subject] = rec
            rec.edges.append(edge)

        # Resolve labels for all subjects and relation targets in one pass.
        wanted = set(records) | target_ids
        labels = self._fetch_labels(adapter, wanted)
        for rec in records.values():
            rec.subject_label = labels.get(rec.subject_id, "")
            rec.edges = [
                e
                if not e.target_id
                else _EdgeRow(
                    e.predicate_id,
                    e.predicate_label,
                    e.target_id,
                    labels.get(e.target_id, ""),
                    e.metadata,
                )
                for e in rec.edges
            ]
            # Deterministic ordering for stable snippets across refreshes.
            rec.edges.sort(key=lambda e: e.sort_key())

        return records

    @staticmethod
    def _fetch_labels(adapter, ids: Iterable[str]) -> dict[str, str]:
        from sqlalchemy import text

        ids = [i for i in ids if i]
        out: dict[str, str] = {}
        with adapter.engine.connect() as conn:
            for chunk in _chunked(ids, _SQL_CHUNK):
                placeholders = ",".join(f":s{i}" for i in range(len(chunk)))
                params = {f"s{i}": cid for i, cid in enumerate(chunk)}
                stmt = text(
                    "SELECT subject, value FROM statements "
                    f"WHERE predicate='{_LABEL_PREDICATE}' "
                    f"AND subject IN ({placeholders})"
                )
                for subject, value in conn.execute(stmt, params).fetchall():
                    if value and subject not in out:
                        out[subject] = str(value)
        return out

    def identifiers(self) -> Iterable[str]:
        return sorted(self.index())

    # ----- serialization -----

    @property
    def snapshot_date(self) -> str:
        return type(self)._snapshot_date

    def serialize(self, identifier: str) -> ReferenceCacheEntry:
        rec = self.index().get(identifier)
        if rec is None:
            raise KeyError(f"{identifier} not found in {self.prefix} edge index")
        body = "\n".join(self._render_body(rec)) + "\n"
        title = rec.subject_label or rec.subject_id
        return ReferenceCacheEntry(
            reference_id=rec.subject_id,
            title=f"{title} ({self._ontology_short})"[:240],
            body=body,
            content_type="structured_record",
            extra_frontmatter={"database": self._ontology_name},
        )

    def _render_body(self, rec: _SubjectRecord) -> Iterator[str]:
        label = rec.subject_label or rec.subject_id
        yield f"# {rec.subject_id}  {label}"
        yield ""
        pred_labels = ", ".join(p.label for p in self._predicates)
        yield (
            f"**{rec.subject_id}** — {label}. Selected {self._ontology_short} "
            f"edges ({pred_labels})."
        )
        yield ""

        yield "## Edges"
        yield ""
        yield (
            "Each row is one selected ontology edge. For annotation predicates "
            "the literal value is in the METADATA column (TARGET_ID / "
            "TARGET_LABEL blank); for relation predicates the object term fills "
            "TARGET_ID / TARGET_LABEL."
        )
        yield ""
        yield from _md_table(
            ["ID", "LABEL", "PRED", "TARGET_ID", "TARGET_LABEL", "METADATA"],
            [
                (
                    rec.subject_id,
                    label,
                    e.predicate_label,
                    e.target_id,
                    e.target_label,
                    e.metadata,
                )
                for e in rec.edges
            ],
        )
        yield ""

        yield "## Source"
        yield ""
        version = self._ontology_version or self.snapshot_date or "unknown"
        provenance = (
            f"{self._ontology_name} version **{version}**, "
            f"predicate selection: {', '.join(p.id for p in self._predicates)}."
        )
        yield provenance
        if self._license:
            yield ""
            yield f"License: {self._license}"
        if self._homepage:
            yield ""
            yield f"[{self._ontology_name}]({self._homepage})"


# ----- helpers -----


def _chunked(items: list, n: int) -> Iterator[list]:
    for i in range(0, len(items), n):
        yield items[i : i + n]


def _clean(value: str) -> str:
    """Collapse internal whitespace/newlines so a value stays one table cell."""
    return re.sub(r"\s+", " ", str(value)).strip()


def _md_table(headers: list[str], rows: list[tuple[str, ...]]) -> Iterator[str]:
    def _esc(cell: str) -> str:
        return cell.replace("|", "\\|") if cell else "-"

    yield "| " + " | ".join(headers) + " |"
    yield "|" + "|".join(["---"] * len(headers)) + "|"
    for row in rows:
        yield "| " + " | ".join(_esc(cell) for cell in row) + " |"

"""
SEPIO evidence/provenance exporter for dismech.

The KGX export (:mod:`dismech.export.kgx_export`) flattens each dismech
``EvidenceItem`` into two parallel string lists on a Biolink ``Association``
(``publications`` and ``supporting_text``). That is lossy: the snippet, the
document it came from, the direction of support, the kind of evidence, and the
curator's interpretation of the snippet all end up concatenated into one blob.

This module emits the same evidence as a **SEPIO** graph, written as a sidecar
to the KGX export so the two can be joined. The SEPIO classes used here
(``Statement``, ``EvidenceLine``, ``DataItem``, ``Document``) are *not* part of
the Biolink Model, so they are not available from
``biolink_model.datamodel.pydanticmodel_v2`` and are defined here as a small
hand-written profile of the SEPIO core model — only the subset dismech needs.

The mapping from the dismech evidence model:

===============================  ====================================================
dismech                          SEPIO
===============================  ====================================================
the object carrying ``evidence`` ``Statement`` (subject / predicate / object)
``evidence[]``                   ``Statement.has_evidence_lines[]`` (one line per item)
``evidence[].evidence_source``   ``EvidenceLine.evidence_type``
``evidence[].supports``          ``EvidenceLine.direction_of_evidence_provided``
``evidence[].snippet``           ``DataItem.value`` (``data_type: TextSpan``)
``evidence[].reference``         ``Document.id`` (via ``DataItem.reported_in``)
``evidence[].reference_title``   ``Document.title``
``evidence[].explanation``       ``EvidenceLine.description``
===============================  ====================================================

``Document.document_type`` has no dismech counterpart; it is inferred from the
reference CURIE prefix (PMID/DOI are primary literature, ``clinicaltrials:`` is
a trial record, ``ORPHA:``/``CGGV:``/... are structured database records).

Statement identity
------------------

A statement that corresponds to a KGX edge reuses that edge's ``id``, so
``sepio.jsonl`` joins to ``*_edges.jsonl`` on ``id``. Statements that have no
KGX counterpart — pathophysiology node assertions and the causal (``downstream``)
edges between them, both of which the KGX export can only propagate as indirect
evidence — get a deterministic UUIDv5 minted from the disease and node names.

The two id families have **different stability guarantees**. KGX association ids
are random ``uuid4`` values minted per walk (:func:`dismech.export.kgx_export._make_edge_id`),
so a KGX-joined statement id is only meaningful *within one export artifact pair*
— it changes between releases, and statements produced by a separate walk of the
same record (see :func:`statements_from_record`) do not join to an
already-written ``*_edges.jsonl``. The pathophysiology UUIDv5 ids are stable
across runs and are the ones downstream consumers can cite.
"""

from __future__ import annotations

import json
import re
import uuid
from collections import Counter
from collections.abc import Iterable, Iterator
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict

# Namespace for deterministic (UUIDv5) statement and evidence identifiers.
DISMECH_UUID_NAMESPACE = uuid.uuid5(uuid.NAMESPACE_DNS, "dismech.monarchinitiative.org")

# Predicates for the assertions that have no Biolink/KGX counterpart.
HAS_PATHOPHYSIOLOGY = "dismech:has_pathophysiology"
CAUSALLY_UPSTREAM_OF = "dismech:causally_upstream_of"

# dismech has no document-type field; infer it from the reference prefix.
DOCUMENT_TYPE_BY_PREFIX = {
    "pmid": "PRIMARY_LITERATURE",
    "pmc": "PRIMARY_LITERATURE",
    "doi": "PRIMARY_LITERATURE",
    "ppr": "PREPRINT",
    "clinicaltrials": "CLINICAL_TRIAL_RECORD",
    "orpha": "DATABASE_RECORD",
    "cggv": "DATABASE_RECORD",
    "cgds": "DATABASE_RECORD",
    "icees": "DATABASE_RECORD",
    "ncit": "DATABASE_RECORD",
    "civic_assertion": "DATABASE_RECORD",
    "civic_eid": "DATABASE_RECORD",
    "geo": "DATASET_RECORD",
    "metabolights": "DATASET_RECORD",
    "url": "WEB_PAGE",
    "http": "WEB_PAGE",
    "https": "WEB_PAGE",
}

# The dismech EvidenceItemSupportEnum is mostly a direction-of-support enum, so
# its values pass through unchanged. NO_EVIDENCE is the exception: it asserts
# that the reference is silent on the claim, which is not a direction.
# WRONG_STATEMENT also has no distinct SEPIO direction and collapses onto REFUTE;
# the raw enum value is preserved on EvidenceLine.dismech_supports so the mapping
# round-trips rather than losing the distinction the schema draws.
SUPPORTS_TO_DIRECTION = {
    "SUPPORT": "SUPPORT",
    "PARTIAL": "PARTIAL",
    "REFUTE": "REFUTE",
    "WRONG_STATEMENT": "REFUTE",
    "NO_EVIDENCE": "NEUTRAL",
}


class SepioEntity(BaseModel):
    """Base for the SEPIO profile classes: forbid unmodelled fields, drop empties."""

    model_config = ConfigDict(extra="forbid")


class Document(SepioEntity):
    """The publication or record an evidence item was reported in."""

    id: str
    type: str = "Document"
    document_type: str | None = None
    title: str | None = None


class DataItem(SepioEntity):
    """The evidence itself. For dismech this is always a span of quoted text."""

    id: str
    type: str = "DataItem"
    data_type: str | None = None
    value: str | None = None
    # SEPIO allows many source documents per item; a dismech EvidenceItem
    # always quotes exactly one reference, so this stays single-valued.
    reported_in: Document | None = None


class EvidenceLine(SepioEntity):
    """The interpretation of one or more evidence items as bearing on a statement."""

    id: str
    type: str = "EvidenceLine"
    evidence_type: str | None = None
    direction_of_evidence_provided: str | None = None
    has_evidence_items: list[DataItem] = []
    description: str | None = None
    # dismech provenance, outside the SEPIO core model: the raw
    # EvidenceItemSupportEnum value, carried through because the SEPIO direction
    # is a lossy projection of it (WRONG_STATEMENT and REFUTE both map to REFUTE).
    dismech_supports: str | None = None


class Statement(SepioEntity):
    """The assertion the evidence is offered for."""

    id: str
    type: str = "Statement"
    subject: str
    predicate: str
    object: str
    subject_label: str | None = None
    object_label: str | None = None
    qualifiers: list[str] | None = None
    has_evidence_lines: list[EvidenceLine] = []
    # dismech provenance, outside the SEPIO core model: which KB file and
    # section the statement came from, the mechanistic-hypothesis groups a
    # causal edge belongs to, and — when the evidence was inherited from a
    # parent pathophysiology node rather than asserted on the object itself —
    # the id of the statement that owns it.
    source_disease: str | None = None
    dismech_section: str | None = None
    hypothesis_groups: list[str] | None = None
    evidence_inherited_from: str | None = None


def _slug(text: str) -> str:
    """Normalize a free-text dismech name into an id-safe fragment."""
    return re.sub(r"[^A-Za-z0-9]+", "_", (text or "").strip()).strip("_")


def _uuid5(*parts: str) -> str:
    """Mint a deterministic urn:uuid identifier from stable key parts."""
    key = "|".join(parts)
    return f"urn:uuid:{uuid.uuid5(DISMECH_UUID_NAMESPACE, key)}"


def _document_type(reference: str) -> str | None:
    """Infer a SEPIO document type from a dismech reference CURIE prefix."""
    prefix = reference.split(":", 1)[0].strip().lower() if ":" in reference else ""
    return DOCUMENT_TYPE_BY_PREFIX.get(prefix)


def evidence_item_to_line(evidence_item: dict[str, Any], statement_id: str, index: int) -> EvidenceLine | None:
    """
    Convert one dismech EvidenceItem into a SEPIO EvidenceLine.

    Args:
        evidence_item: An entry from a dismech ``evidence:`` list
        statement_id: Id of the statement this line is offered for
        index: Position of the item within its evidence list (for id minting)

    Returns:
        EvidenceLine, or None if the item has neither a reference nor a snippet
    """
    if not isinstance(evidence_item, dict):
        return None

    reference = (evidence_item.get("reference") or "").strip()
    snippet = evidence_item.get("snippet")
    if not reference and not snippet:
        return None

    document = None
    if reference:
        document = Document(
            id=reference,
            document_type=_document_type(reference),
            title=evidence_item.get("reference_title"),
        )
    # A text span's identity is the document it came from plus the exact quoted
    # text, so the same snippet cited twice resolves to one DataItem.
    data_item = DataItem(
        id=_uuid5("data-item", reference, snippet or ""),
        data_type="TextSpan" if snippet else None,
        value=snippet,
        reported_in=document,
    )

    supports = evidence_item.get("supports")
    return EvidenceLine(
        id=_uuid5("evidence-line", statement_id, str(index), reference, snippet or ""),
        evidence_type=evidence_item.get("evidence_source"),
        direction_of_evidence_provided=SUPPORTS_TO_DIRECTION.get(supports, supports) if supports else None,
        has_evidence_items=[data_item],
        description=evidence_item.get("explanation"),
        dismech_supports=supports or None,
    )


def evidence_to_lines(evidence_items: Iterable[dict[str, Any]] | None, statement_id: str) -> list[EvidenceLine]:
    """Convert a dismech ``evidence:`` list into SEPIO evidence lines."""
    lines = []
    for index, item in enumerate(evidence_items or []):
        line = evidence_item_to_line(item, statement_id, index)
        if line:
            lines.append(line)
    return lines


def statement_from_association(
    association: Any,
    evidence_items: Iterable[dict[str, Any]] | None,
    *,
    disease_name: str | None = None,
    section: str | None = None,
    inherited_from: str | None = None,
) -> Statement | None:
    """
    Build a SEPIO Statement for a KGX association.

    The statement reuses the association's ``id`` so the SEPIO sidecar joins to
    the KGX edge file on ``id``.

    Args:
        association: A Biolink Association emitted by the KGX transform
        evidence_items: The dismech evidence list the association was built from
        disease_name: ``name`` of the source disorder record
        section: The dismech section the association came from (e.g. "phenotypes")
        inherited_from: Id of the pathophysiology-node statement that owns the
            evidence, when the association only inherited it indirectly

    Returns:
        Statement, or None if the association carries no evidence
    """
    lines = evidence_to_lines(evidence_items, association.id)
    if not lines:
        return None

    # Carry the association's qualifiers across. Without this the sidecar
    # restates the bare triple and loses everything the qualifier encodes —
    # including the exposure polarity that keeps a deficiency entry from
    # reading as its own opposite (#8468), and the `direction:` qualifiers the
    # Disease→GO edges have always carried.
    qualifiers = getattr(association, "qualifiers", None)

    return Statement(
        id=association.id,
        subject=association.subject,
        predicate=association.predicate,
        object=association.object,
        qualifiers=list(qualifiers) if qualifiers else None,
        has_evidence_lines=lines,
        source_disease=disease_name,
        dismech_section=section,
        evidence_inherited_from=inherited_from,
    )


def _causal_link_curie(causal_link_type: str | None) -> str | None:
    """CURIE for a ``CausalLinkTypeEnum`` value, for the ``qualifiers`` list.

    Biolink types that slot as ``range: ontology class``, so a bare ``DIRECT``
    is not a legal entry any more than ``direction:increased`` was.
    ``CausalLinkTypeEnum`` binds none of its four values to an ontology term, so
    they take the dismech namespace -- ``dismech:`` is declared in the schema
    prefix map and is ``default_prefix``, making these resolvable CURIEs into
    our own model rather than invented ones.

    Qualified by the enum rather than flat: ``DIRECT`` is a very generic local
    name to plant at the root of a shared namespace, and 18 permissible-value
    names in this schema already belong to more than one enum. Matches the
    ``dismech:{...}#{...}`` fragment convention used by
    :func:`pathophysiology_node_id`.
    """
    if not causal_link_type:
        return None
    return f"dismech:CausalLinkTypeEnum#{causal_link_type}"


def pathophysiology_node_id(disease_name: str, node_name: str) -> str:
    """Local identifier for a pathophysiology node, which has no ontology term."""
    return f"dismech:{_slug(disease_name)}#{_slug(node_name)}"


def pathophysiology_statement_id(disease_name: str, node_name: str) -> str:
    """
    Deterministic statement id for a ``disease has_pathophysiology node`` assertion.

    This is the id of the *first* node in the disease whose name slugs to
    ``node_name``, which is also the one an inheriting child statement's
    ``evidence_inherited_from`` resolves to. A second node that slugged to the
    same value would be disambiguated by an occurrence counter inside
    :func:`pathophysiology_statements`; no such collision exists in ``kb/`` today.
    """
    return _uuid5("pathophysiology", _slug(disease_name), _slug(node_name))


def pathophysiology_statements(record: dict[str, Any]) -> Iterator[Statement]:
    """
    Emit SEPIO statements for the assertions the KGX export cannot represent.

    Two kinds, both drawn from ``pathophysiology[]``:

    1. The node assertion itself — *disease has_pathophysiology <node>* — whose
       evidence KGX only re-attaches to the node's ontology-bound children as
       indirect supporting text.
    2. Each ``downstream`` causal edge between two pathophysiology nodes, which
       the KGX export drops entirely.

    Args:
        record: A disorder dict loaded from YAML

    Yields:
        Statement objects, one per evidence-bearing node or causal edge
    """
    disease_id = _get_disease_id(record)
    disease_name = record.get("name")
    if not disease_id or not disease_name:
        return

    # A disease may assert two causal edges between the same pair of nodes when
    # they belong to competing mechanistic hypotheses. The hypothesis groups
    # normally tell them apart; this counter is the backstop that keeps two
    # otherwise-identical edges — or two node names that slug to the same value —
    # from minting one id. The first occurrence always keeps the plain
    # deterministic id, so `pathophysiology_statement_id` stays the public
    # answer for the common (collision-free) case.
    minted: Counter[str] = Counter()

    def _unique_id(*parts: str) -> str:
        key = "|".join(parts)
        occurrence = minted[key]
        minted[key] += 1
        return _uuid5(key) if occurrence == 0 else _uuid5(key, str(occurrence))

    for node in record.get("pathophysiology") or []:
        node_name = node.get("name")
        if not node_name:
            continue

        node_id = pathophysiology_node_id(disease_name, node_name)
        statement_id = _unique_id("pathophysiology", _slug(disease_name), _slug(node_name))
        lines = evidence_to_lines(node.get("evidence"), statement_id)
        if lines:
            yield Statement(
                id=statement_id,
                subject=disease_id,
                predicate=HAS_PATHOPHYSIOLOGY,
                object=node_id,
                subject_label=disease_name,
                object_label=node_name,
                has_evidence_lines=lines,
                source_disease=disease_name,
                dismech_section="pathophysiology",
            )

        for edge in node.get("downstream") or []:
            target = edge.get("target")
            if not target:
                continue
            hypothesis_groups = [group for group in edge.get("hypothesis_groups") or [] if group]
            edge_statement_id = _unique_id(
                "causal-edge",
                _slug(disease_name),
                _slug(node_name),
                _slug(target),
                ",".join(sorted(hypothesis_groups)),
            )
            edge_lines = evidence_to_lines(edge.get("evidence"), edge_statement_id)
            if not edge_lines:
                continue
            causal_link_type = _causal_link_curie(edge.get("causal_link_type"))
            yield Statement(
                id=edge_statement_id,
                subject=node_id,
                predicate=CAUSALLY_UPSTREAM_OF,
                object=pathophysiology_node_id(disease_name, target),
                subject_label=node_name,
                object_label=target,
                qualifiers=[causal_link_type] if causal_link_type else None,
                has_evidence_lines=edge_lines,
                source_disease=disease_name,
                dismech_section="pathophysiology.downstream",
                hypothesis_groups=hypothesis_groups or None,
            )


def _get_disease_id(record: dict[str, Any]) -> str | None:
    """Extract ``disease_term.term.id`` from a disorder record."""
    term = ((record.get("disease_term") or {}).get("term") or {}).get("id")
    return term if isinstance(term, str) else None


def statements_for_edges(edges: Iterable[Any], disease_name: str | None) -> Iterator[Statement]:
    """
    Build the SEPIO statements for a stream of KGX edges.

    Shared by :func:`statements_from_record` and the Koza transform that writes
    the sidecar, so the association-to-statement mapping — including the
    ``evidence_inherited_from`` back-reference for indirect evidence — has one
    implementation rather than two that must stay in sync.

    Args:
        edges: ``EdgeWithEvidence`` tuples from
            :func:`dismech.export.kgx_export.iter_edges_with_evidence`
        disease_name: ``name`` of the source disorder record

    Yields:
        Statement objects, skipping edges that carry no evidence
    """
    for edge in edges:
        inherited_from = None
        if edge.indirect and edge.source_node and disease_name:
            inherited_from = pathophysiology_statement_id(disease_name, edge.source_node)
        statement = statement_from_association(
            edge.association,
            edge.evidence,
            disease_name=disease_name,
            section=edge.section,
            inherited_from=inherited_from,
        )
        if statement:
            yield statement


def statements_from_record(record: dict[str, Any]) -> Iterator[Statement]:
    """
    Emit every SEPIO statement for one disorder record.

    Covers the KGX associations (joined to the KGX edge file by ``id``) plus the
    pathophysiology node and causal-edge assertions that have no KGX edge.

    .. warning::

       This function walks the record itself, and KGX association ids are random
       ``uuid4`` values minted per walk. Its KGX-derived statement ids therefore
       join only to associations yielded by *this same call* — never to an
       already-written ``*_edges.jsonl``. To get a sidecar that joins to an edge
       file, both must come from one transform run (which is what
       ``just export-kgx`` does). Only the pathophysiology statement ids, which
       are UUIDv5, are stable across calls and releases.

    Args:
        record: A disorder dict loaded from YAML

    Yields:
        Statement objects
    """
    # Imported lazily: kgx_export imports this module to write the sidecar.
    from dismech.export.kgx_export import iter_edges_with_evidence

    yield from statements_for_edges(iter_edges_with_evidence(record), record.get("name"))
    yield from pathophysiology_statements(record)


def dump_statement(statement: Statement) -> str:
    """Serialize a statement to a single JSON line."""
    return json.dumps(statement.model_dump(exclude_none=True), separators=(",", ":"))


def write_jsonl(statements: Iterable[Statement], path: str | Path) -> int:
    """
    Write statements to a JSON Lines file.

    Args:
        statements: Statements to write
        path: Destination file (parent directories are created)

    Returns:
        Number of statements written
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for statement in statements:
            handle.write(dump_statement(statement))
            handle.write("\n")
            count += 1
    return count

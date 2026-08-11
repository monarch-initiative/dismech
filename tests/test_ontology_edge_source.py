"""Tests for the generic OntologyEdgeSource.

These run fully offline against a tiny in-memory SQLite shaped like a semsql
``statements`` table, so no multi-hundred-MB OAK ontology is downloaded. (The
NCIT-against-real-data path is exercised by the ``just ncit-edges-rebuild``
workflow, not unit tests.)
"""

from __future__ import annotations

import types
from pathlib import Path

import pytest

from dismech.reference_cache_frontmatter import check_cache_file
from dismech.structured_sources.ontology_edges import (
    OntologyEdgeSource,
    PredicateSpec,
)


def _tiny_ncit_engine():
    """Build a semsql-shaped ``statements`` table with a couple of NCIT edges."""
    from sqlalchemy import create_engine, text

    engine = create_engine("sqlite:///:memory:")
    with engine.begin() as conn:
        conn.execute(
            text(
                "CREATE TABLE statements "
                "(subject TEXT, predicate TEXT, value TEXT, object TEXT)"
            )
        )
        rows = [
            ("NCIT:C1872", "rdfs:label", "Midostaurin", None),
            ("NCIT:C26202", "rdfs:label", "FLT3", None),
            # annotation predicate (literal value)
            (
                "NCIT:C1872",
                "NCIT:P302",
                "acute myeloid leukemia (AML) who are FLT3 mutation-positive",
                None,
            ),
            # relation predicate (object CURIE) — label-resolved to "FLT3"
            ("NCIT:C1872", "NCIT:A7", None, "NCIT:C26202"),
            ("obo:ncit.owl", "owl:versionInfo", "99.99z", None),
        ]
        for s, p, v, o in rows:
            conn.execute(
                text("INSERT INTO statements VALUES (:s, :p, :v, :o)"),
                {"s": s, "p": p, "v": v, "o": o},
            )
    return engine


@pytest.fixture()
def ontology_edge_source(tmp_path: Path) -> OntologyEdgeSource:
    src = OntologyEdgeSource(tmp_path)
    # Configure without a manifest file and inject a stub adapter so no
    # ontology is downloaded.
    OntologyEdgeSource.prefix = "NCIT"
    OntologyEdgeSource._ontology_name = "NCI Thesaurus"
    OntologyEdgeSource._ontology_short = "NCIT"
    OntologyEdgeSource._ontology_version = "99.99z"
    OntologyEdgeSource._predicates = (
        PredicateSpec("NCIT:P302", "Accepted_Therapeutic_Use_For", "annotation"),
        PredicateSpec("NCIT:A7", "Has_Target", "relation"),
    )
    src._adapter_obj = types.SimpleNamespace(engine=_tiny_ncit_engine())
    return src


def test_index_builds_annotation_and_relation(ontology_edge_source):
    idx = ontology_edge_source.index()
    assert set(idx) == {"NCIT:C1872"}
    rec = idx["NCIT:C1872"]
    assert rec.subject_label == "Midostaurin"
    by_pred = {e.predicate_id: e for e in rec.edges}
    # annotation: literal in metadata, no target
    ann = by_pred["NCIT:P302"]
    assert ann.target_id == "" and ann.target_label == ""
    assert "acute myeloid leukemia" in ann.metadata
    # relation: object CURIE label-resolved, no metadata literal
    rel = by_pred["NCIT:A7"]
    assert rel.target_id == "NCIT:C26202"
    assert rel.target_label == "FLT3"
    assert rel.metadata == ""


def test_serialize_renders_unified_table(ontology_edge_source):
    entry = ontology_edge_source.serialize("NCIT:C1872")
    text = entry.render()
    assert 'reference_id: "NCIT:C1872"' in text
    assert 'database: "NCI Thesaurus"' in text
    assert 'content_type: "structured_record"' in text
    assert "journal:" not in text
    assert "| ID | LABEL | PRED | TARGET_ID | TARGET_LABEL | METADATA |" in text
    assert (
        "| NCIT:C1872 | Midostaurin | Accepted_Therapeutic_Use_For | - | - | "
        "acute myeloid leukemia (AML) who are FLT3 mutation-positive |"
    ) in text
    assert (
        "| NCIT:C1872 | Midostaurin | Has_Target | NCIT:C26202 | FLT3 | - |"
    ) in text
    assert entry.filename() == "NCIT_C1872.md"


def test_serialize_is_byte_deterministic(ontology_edge_source):
    a = ontology_edge_source.serialize("NCIT:C1872").render()
    b = ontology_edge_source.serialize("NCIT:C1872").render()
    assert a == b


def test_cache_file_passes_frontmatter_contract(ontology_edge_source, tmp_path: Path):
    path = ontology_edge_source.write_cache_file("NCIT:C1872", tmp_path / "out")
    assert check_cache_file(path) is None

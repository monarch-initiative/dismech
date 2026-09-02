"""Relation predicates may live in `edge`, not in `statements`.

``OntologyEdgeSource`` was written for NCIT ``P302``, an *annotation* whose
literal value sits in ``statements.value``. NCIT's disease relations are a
different shape: ``Disease_Has_Normal_Cell_Origin`` and friends are object
properties asserted inside ``owl:equivalentClass`` intersections, so semsql
materializes them into the ``edge`` table while ``statements`` holds only the
blank-node scaffolding. Reading ``statements`` alone would silently return zero
cell-of-origin edges -- no error, just an empty cache.

These tests use a stub adapter over an in-memory SQLite so the merge is pinned
without downloading the multi-gigabyte NCIT database.
"""

import sys
from dataclasses import dataclass
from pathlib import Path

import pytest
from sqlalchemy import create_engine, text

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from dismech.structured_sources.ontology_edges import (  # noqa: E402
    OntologyEdgeSource,
    PredicateSpec,
)


@dataclass
class _StubAdapter:
    engine: object


def _make_db(*, with_edge_table: bool, edge_rows=(), statement_rows=()):
    engine = create_engine("sqlite://")
    with engine.begin() as conn:
        conn.execute(
            text(
                "CREATE TABLE statements "
                "(subject TEXT, predicate TEXT, value TEXT, object TEXT)"
            )
        )
        for row in statement_rows:
            conn.execute(
                text(
                    "INSERT INTO statements (subject, predicate, value, object) "
                    "VALUES (:s, :p, :v, :o)"
                ),
                {"s": row[0], "p": row[1], "v": row[2], "o": row[3]},
            )
        for curie, label in (
            ("NCIT:C8851", "Diffuse Large B-Cell Lymphoma"),
            ("NCIT:C12475", "Mature B-Lymphocyte"),
            ("NCIT:C37008", "Neoplastic Large B-Lymphocyte"),
        ):
            conn.execute(
                text(
                    "INSERT INTO statements (subject, predicate, value, object) "
                    "VALUES (:s, 'rdfs:label', :v, NULL)"
                ),
                {"s": curie, "v": label},
            )
        if with_edge_table:
            conn.execute(
                text("CREATE TABLE edge (subject TEXT, predicate TEXT, object TEXT)")
            )
            for row in edge_rows:
                conn.execute(
                    text(
                        "INSERT INTO edge (subject, predicate, object) "
                        "VALUES (:s, :p, :o)"
                    ),
                    {"s": row[0], "p": row[1], "o": row[2]},
                )
    return engine


@pytest.fixture
def source(monkeypatch, tmp_path):
    src = OntologyEdgeSource(tmp_path)
    monkeypatch.setattr(
        OntologyEdgeSource,
        "_predicates",
        (
            PredicateSpec("NCIT:P302", "Accepted_Therapeutic_Use_For", "annotation"),
            PredicateSpec("NCIT:R104", "Disease_Has_Normal_Cell_Origin", "relation"),
            PredicateSpec("NCIT:R105", "Disease_Has_Abnormal_Cell", "relation"),
        ),
    )
    return src


def _index(source, engine):
    source._adapter_obj = _StubAdapter(engine=engine)
    return source.build_index()


def test_relation_edges_are_read_from_the_edge_table(source):
    """The case that matters: NCIT states R104 only as a materialized edge."""
    engine = _make_db(
        with_edge_table=True,
        edge_rows=[
            ("NCIT:C8851", "NCIT:R104", "NCIT:C12475"),
            ("NCIT:C8851", "NCIT:R105", "NCIT:C37008"),
        ],
    )
    records = _index(source, engine)
    assert "NCIT:C8851" in records
    edges = {(e.predicate_label, e.target_id, e.target_label) for e in records["NCIT:C8851"].edges}
    assert (
        "Disease_Has_Normal_Cell_Origin",
        "NCIT:C12475",
        "Mature B-Lymphocyte",
    ) in edges
    assert (
        "Disease_Has_Abnormal_Cell",
        "NCIT:C37008",
        "Neoplastic Large B-Lymphocyte",
    ) in edges


def test_annotation_and_relation_predicates_merge_into_one_record(source):
    engine = _make_db(
        with_edge_table=True,
        edge_rows=[("NCIT:C8851", "NCIT:R104", "NCIT:C12475")],
        statement_rows=[("NCIT:C8851", "NCIT:P302", "lymphoma", None)],
    )
    records = _index(source, engine)
    edges = records["NCIT:C8851"].edges
    assert {e.predicate_id for e in edges} == {"NCIT:P302", "NCIT:R104"}
    # Annotation rows keep their literal in METADATA with a blank target.
    annotation = next(e for e in edges if e.predicate_id == "NCIT:P302")
    assert annotation.metadata == "lymphoma"
    assert annotation.target_id == ""


def test_a_relation_asserted_in_both_tables_is_not_duplicated(source):
    """An ontology stating a relation as a plain triple *and* an edge yields one row."""
    engine = _make_db(
        with_edge_table=True,
        edge_rows=[("NCIT:C8851", "NCIT:R104", "NCIT:C12475")],
        statement_rows=[("NCIT:C8851", "NCIT:R104", None, "NCIT:C12475")],
    )
    records = _index(source, engine)
    r104 = [e for e in records["NCIT:C8851"].edges if e.predicate_id == "NCIT:R104"]
    assert len(r104) == 1


def test_missing_edge_table_degrades_quietly(source):
    """An ontology whose relations are plain triples must still work."""
    engine = _make_db(
        with_edge_table=False,
        statement_rows=[("NCIT:C8851", "NCIT:R104", None, "NCIT:C12475")],
    )
    records = _index(source, engine)
    assert [e.target_id for e in records["NCIT:C8851"].edges] == ["NCIT:C12475"]


def test_rendered_rows_are_quotable_snippets(source):
    """A curator cites the row; it has to survive as a substring of the body."""
    engine = _make_db(
        with_edge_table=True,
        edge_rows=[("NCIT:C8851", "NCIT:R104", "NCIT:C12475")],
    )
    _index(source, engine)
    entry = source.serialize("NCIT:C8851")
    assert "Disease_Has_Normal_Cell_Origin | NCIT:C12475 | Mature B-Lymphocyte" in entry.body

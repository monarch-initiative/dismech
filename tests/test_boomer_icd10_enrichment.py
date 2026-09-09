"""Directional mappings, WHO identity, and safe updates of saved Boomer inputs."""

import csv
import importlib.util
import json
import sqlite3
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

SCRIPTS = Path(__file__).resolve().parents[1] / "analyses/boomer/scripts"
sys.path.insert(0, str(SCRIPTS))
from icd10_enrichment import ICD10Mappings, mapping_fact  # noqa: E402
from enrich_icd10_inputs import INDEX_FIELDNAMES, migrate, tsv  # noqa: E402
from prepare_icd10 import to_obo  # noqa: E402


@pytest.fixture
def importer():
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE statements (subject TEXT, predicate TEXT, object TEXT, value TEXT)"
    )
    connection.executemany(
        "INSERT INTO statements VALUES (?, ?, ?, ?)",
        [
            ("ORDO:1", "skos:broadMatch", None, "ICD-10:Q87.8"),
            ("ORDO:1", "skos:broadMatch", "ICD-10:Q87.8", None),
            ("ORDO:2", "skos:broadMatch", None, "ICD-10:Q87.8"),
            ("ORDO:2", "skos:narrowMatch", None, "ICD-10:Q87"),
            ("ORDO:2", "skos:exactMatch", None, "ICD-10:E85.4*"),
        ],
    )
    source = ICD10Mappings.__new__(ICD10Mappings)
    source.external = SimpleNamespace(
        con={"ORDO": connection},
        is_obsolete=lambda *_: False,
        label=lambda *_: "CM label",
        ancestors=lambda *_: set(),
    )
    source.priors = {
        "skos:exactMatch": 0.95,
        "skos:broadMatch": 0.9,
        "skos:narrowMatch": 0.9,
    }
    source.who = SimpleNamespace(
        label=lambda curie: {"ICD10:Q87.8": "WHO label", "ICD10:Q87": "WHO parent"}.get(
            curie
        ),
        ancestors=lambda terms, **_: ["ICD10:Q87"] if terms == ["ICD10:Q87.8"] else [],
    )
    source._mappings, source._ancestors, source._labels = {}, {}, {}
    yield source
    connection.close()


def input_kb():
    return {
        "name": "example",
        "facts": [
            {"fact_type": "MemberOfDisjointGroup", "sub": f"ORDO:{i}", "group": "ORDO"}
            for i in (1, 2)
        ],
        "pfacts": [
            {
                "fact": {
                    "fact_type": "EquivalentTo",
                    "sub": "MONDO:1",
                    "equivalent": "ORDO:1",
                },
                "prob": 0.95,
            }
        ],
        "labels": {"ORDO:1": "Existing curator label"},
    }


def test_directions_deduplication_and_review(importer):
    kb = input_kb()
    direct = [
        {
            "term": {"id": "ICD10CM:Q87.8"},
            "mapping_predicate": "skos:narrowMatch",
            "mapping_source": "ORPHA:1",
        },
        {
            "term": {"id": "ICD10CM:Q87.8"},
            "mapping_predicate": "skos:closeMatch",
            "mapping_source": "ICD-10-CM",
        },
    ]
    rows = importer.enrich(kb, "Example", direct)
    assert len(kb["pfacts"]) == 4  # one existing plus three distinct hypotheses
    assert mapping_fact("ORDO:1", "skos:broadMatch", "ICD10:Q87.8") in [
        p["fact"] for p in kb["pfacts"]
    ]
    assert mapping_fact("ORDO:2", "skos:narrowMatch", "ICD10:Q87") == {
        "fact_type": "ProperSubClassOf",
        "sub": "ICD10:Q87",
        "sup": "ORDO:2",
    }
    assert {
        "fact_type": "ProperSubClassOf",
        "sub": "ICD10:Q87.8",
        "sup": "ICD10:Q87",
    } in kb["facts"]
    assert not any(
        p["fact"].get("equivalent", "").startswith("ICD10:") for p in kb["pfacts"]
    )
    assert len([r for r in rows if r["status"] == "REVIEW"]) == 3
    assert kb["labels"]["ORDO:1"] == "Existing curator label"
    before = json.dumps(kb)
    assert importer.enrich(kb, "Example", direct) == rows
    assert json.dumps(kb) == before


def test_migration_preserves_solution_bytes_marks_stale_and_is_idempotent(
    tmp_path, importer
):
    base, diseases = tmp_path / "boomer", tmp_path / "diseases"
    folder = base / "disorders/Example"
    folder.mkdir(parents=True)
    diseases.mkdir()
    (diseases / "Example.yaml").write_text("category: Mendelian\n")
    (folder / "kb.yaml").write_text(yaml.safe_dump(input_kb(), sort_keys=False))
    (folder / "README.md").write_text("Previous result\n")
    for name in ("solution.yaml", "solution.md"):
        (folder / name).write_text("historical solution\n")
    row = dict.fromkeys(INDEX_FIELDNAMES, "0")
    row.update(
        slug="Example", name="Example", status="ALL_MAPPINGS_CONSISTENT", n_pfacts="1"
    )
    (base / "index.tsv").write_bytes(tsv([row], INDEX_FIELDNAMES, "\r\n"))
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}

    def invalid(_):
        raise ValueError("Invalid model")

    with pytest.raises(ValueError, match="Invalid model"):
        migrate(base, diseases, importer, invalid)
    assert all(p.read_bytes() == content for p, content in before.items())
    assert not (base / "icd10").exists()
    migrate(base, diseases, importer, lambda _: None)
    updated = next(csv.DictReader((base / "index.tsv").open(), delimiter="\t"))
    assert updated["status"] == "STALE_INPUT"
    assert updated["n_retracted"] == "NA"
    assert updated["n_pfacts"] == "4"
    for name in ("solution.yaml", "solution.md"):
        assert (folder / name).read_bytes() == before[folder / name]
    assert (folder / "README.md").read_text().startswith("> **STALE INPUT:")
    assert (
        json.loads((base / "icd10/updates.json").read_text())["Example"][
            "previous_index"
        ]
        == row
    )
    first = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    migrate(base, diseases, importer, lambda _: None)
    assert first == {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}


def test_who_projection_uses_only_asserted_superclasses(tmp_path):
    from oaklib import get_adapter

    xml = b"""<ClaML><Class code="Q87"><Rubric kind="preferred"><Label>Parent</Label></Rubric></Class>
    <Class code="Q87.8"><SuperClass code="Q87"/><Rubric kind="preferred"><Label>WHO child</Label></Rubric>
    <Rubric kind="exclusion"><Label>Not a subclass <Reference code="E75">E75</Reference></Label></Rubric></Class></ClaML>"""
    obo = tmp_path / "who.obo"
    obo.write_text(to_obo(xml, "test"))
    adapter = get_adapter(str(obo))
    assert adapter.label("ICD10:Q87.8") == "WHO child"
    assert set(adapter.ancestors(["ICD10:Q87.8"], predicates=["rdfs:subClassOf"])) == {
        "ICD10:Q87",
        "ICD10:Q87.8",
    }
    assert adapter.label("ICD10CM:Q87.8") is None


def test_crosssource_audit_keeps_who_and_cm_distinct():
    spec = importlib.util.spec_from_file_location(
        "crosssource_icd_test", SCRIPTS / "crosssource_audit.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.normalise("ICD-10:Q87.8") == module.normalise("ICD10:Q87.8")
    assert module.normalise("ICD10CM:Q87.8") != module.normalise("ICD10:Q87.8")


def test_directional_retractions_include_only_explicit_high_prior_rejections():
    from collections import namedtuple
    from build_analyses import retracted_mappings

    proper = namedtuple("ProperSubClassOf", "sub sup")
    equivalent = namedtuple("EquivalentTo", "sub equivalent")

    def solved(fact, truth, prior):
        return SimpleNamespace(
            pfact=SimpleNamespace(fact=fact, prob=prior), truth_value=truth
        )

    solution = SimpleNamespace(
        solved_pfacts=[
            solved(proper("ORDO:1", "ICD10:A00"), False, 0.9),
            solved(equivalent("MONDO:1", "ORDO:1"), False, 0.95),
            solved(proper("ORDO:2", "ICD10:A00"), None, 0.9),
            solved(proper("ORDO:3", "ICD10:A00"), False, 0.03),
        ]
    )
    assert retracted_mappings(solution) == [
        ("MONDO:1", "≡", "ORDO:1"),
        ("ORDO:1", "⊂", "ICD10:A00"),
    ]


def test_one_entry_regeneration_preserves_other_index_rows(tmp_path, monkeypatch):
    import build_analyses as builder

    records = []
    for slug in ("Example", "Other"):
        folder = tmp_path / slug
        folder.mkdir()
        (folder / "kb.yaml").write_text("name: previous\n")
        (folder / "README.md").write_text("previous report\n")
        row = dict.fromkeys(INDEX_FIELDNAMES, "0")
        row.update(slug=slug, name=slug, status="NOT_RUN", n_retracted="NA")
        records.append(row)
    index = tmp_path / "index.tsv"
    index.write_bytes(tsv(records, INDEX_FIELDNAMES))
    rec = dict(
        slug="Example",
        name="Example",
        parent_term="MONDO:1",
        parent_label="Example",
        parent_equivs={},
        pairs=[],
        curated_predicate=None,
    )
    monkeypatch.setattr(
        builder, "Mondo", lambda _: SimpleNamespace(disjoint_pairs=lambda _: [])
    )
    monkeypatch.setattr(builder, "collect", lambda *args: iter([rec]))
    builder.main(
        [
            "--out",
            str(tmp_path),
            "--index",
            str(index),
            "--only",
            "Example",
            "--oak-dir",
            str(tmp_path),
            "--inputs-only",
        ]
    )
    current = list(csv.DictReader(index.open(), delimiter="\t"))
    assert current[1] == records[1]
    assert current[0]["n_pfacts"] == "3"
    assert (tmp_path / "Other/kb.yaml").read_text() == "name: previous\n"

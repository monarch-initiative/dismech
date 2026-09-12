"""Labels can be added to saved Boomer inputs without changing the analysis."""

import importlib.util
import sqlite3
from pathlib import Path

import yaml

SCRIPT = (
    Path(__file__).resolve().parents[1] / "analyses/boomer/scripts/build_analyses.py"
)
spec = importlib.util.spec_from_file_location("build_boomer_analyses", SCRIPT)
boomer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(boomer)


def test_labels_only_preserves_analysis_and_is_idempotent(tmp_path, monkeypatch):
    db = tmp_path / "doid.db"
    with sqlite3.connect(db) as con:
        con.execute(
            "create table statements (subject text, predicate text, value text)"
        )
        con.executemany(
            "insert into statements values (?, 'rdfs:label', ?)",
            [
                ("DOID:1", "First label"),
                ("DOID:2", "Second label"),
            ],
        )
    folder = tmp_path / "Example"
    folder.mkdir()
    kb = {
        "name": "example",
        "facts": [{"fact_type": "ProperSubClassOf", "sub": "DOID:2", "sup": "DOID:1"}],
        "pfacts": [
            {
                "fact": {
                    "fact_type": "EquivalentTo",
                    "sub": "dismech:X",
                    "equivalent": "DOID:2",
                },
                "prob": 0.9,
            }
        ],
        "labels": {"dismech:X": "Curator label", "DOID:1": "Existing label"},
    }
    path = folder / "kb.yaml"
    original = yaml.safe_dump(kb, sort_keys=False)
    path.write_text(original)
    for name in ("solution.yaml", "solution.md", "README.md"):
        (folder / name).write_text("saved output\n")

    def no_solver(*args):
        raise AssertionError("Labels-only must not even load the solver")

    monkeypatch.setattr(boomer, "load_boomer", no_solver)
    args = ["--out", str(tmp_path), "--oak-dir", str(tmp_path), "--labels-only"]
    boomer.main(args)
    enriched = path.read_text()
    assert enriched == original + "  DOID:2: Second label\n"
    for name in ("solution.yaml", "solution.md", "README.md"):
        assert (folder / name).read_text() == "saved output\n"
    boomer.main(args)
    assert path.read_text() == enriched


def test_missing_snapshot_or_term_is_reported_without_inventing_label(tmp_path):
    external = boomer.External(oak_dir=tmp_path)
    kb = {"facts": [{"sub": "DOID:404", "sup": "NCIT:C404"}]}
    assert boomer.add_external_labels(kb, external) == ["DOID:404", "NCIT:C404"]
    assert kb["labels"] == {}
    assert not list(tmp_path.iterdir())  # no implicit ontology downloads


def test_mendelian_selection_and_zero_subtype_collection(tmp_path):
    from types import SimpleNamespace

    # Gene sections, inheritance and Mendelian subtypes alone do not turn a
    # Complex/Cancer/Genetic entry into an explicitly Mendelian entry.
    assert boomer.mendelian_reasons({"category": "Mendelian"}) == [
        "KB_CATEGORY_MENDELIAN"
    ]
    for category in ("Complex", "Cancer", "Genetic", None):
        assert not boomer.mendelian_reasons(
            {
                "category": category,
                "genetic": [{"relationship_type": "CAUSATIVE"}],
                "inheritance": [{"inheritance_term": {"term": {"id": "HP:0000006"}}}],
                "has_subtypes": [{"category": "Mendelian"}],
            }
        )
    (tmp_path / "Gene.yaml").write_text(
        yaml.safe_dump(
            {
                "name": "Gene",
                "category": "Mendelian",
                "disease_term": {"term": {"id": "MONDO:gene"}},
            }
        )
    )
    (tmp_path / "Ungrounded.yaml").write_text(
        yaml.safe_dump(
            {
                "name": "Ungrounded",
                "category": "Mendelian",
            }
        )
    )
    mondo = SimpleNamespace(
        confirmed_equivalents=lambda _: {},
        label=lambda x: x,
        disjoint_pairs=lambda _: [],
    )
    external = boomer.External(oak_dir=tmp_path)
    assert list(boomer.collect(str(tmp_path / "*.yaml"), mondo, external)) == []
    selection = []
    rows = list(
        boomer.collect(
            str(tmp_path / "*.yaml"), mondo, external, "mendelian", selection
        )
    )
    assert len(rows) == 1
    assert rows[0]["pairs"] == []
    assert [r["status"] for r in selection] == ["ELIGIBLE", "NO_MONDO_GROUNDING"]
    kb = boomer.build_kb_dict(mondo, external, rows[0])
    assert len(kb["pfacts"]) == 3
    assert not any(f["fact_type"] == "ProperSubClassOf" for f in kb["facts"])


def test_add_only_rejects_incomplete_existing_analysis(tmp_path, monkeypatch):
    import pytest

    index = tmp_path / "index.tsv"
    index.write_text("slug\tname\nExisting\tExisting\n")
    with pytest.raises(SystemExit):
        boomer.main(["--out", str(tmp_path), "--index", str(index), "--add-only"])
    assert index.read_text() == "slug\tname\nExisting\tExisting\n"


def test_input_expansion_marks_not_run_and_preserves_existing_files(
    tmp_path, monkeypatch
):
    import csv
    from types import SimpleNamespace

    rec = {
        "slug": "Example",
        "name": "Example",
        "parent_term": "MONDO:example",
        "parent_label": "Example",
        "parent_equivs": {},
        "pairs": [],
        "curated_predicate": None,
        "selection_reason": ["KB_CATEGORY_MENDELIAN"],
    }
    monkeypatch.setattr(
        boomer,
        "Mondo",
        lambda _: SimpleNamespace(disjoint_pairs=lambda _: [], versions=list),
    )
    monkeypatch.setattr(boomer, "collect", lambda *args: iter([rec]))

    def no_solver(*args):
        raise AssertionError("Input generation must not load the solver")

    monkeypatch.setattr(boomer, "load_boomer", no_solver)
    index = tmp_path / "index.tsv"
    index.write_text("\t".join(boomer.INDEX_FIELDNAMES) + "\n")
    args = [
        "--out",
        str(tmp_path),
        "--index",
        str(index),
        "--oak-dir",
        str(tmp_path),
        "--inputs-only",
        "--add-only",
    ]
    boomer.main(args)
    with index.open() as fh:
        row = next(csv.DictReader(fh, delimiter="\t"))
    assert row["status"] == "NOT_RUN"
    assert row["n_retracted"] == "NA"
    assert row["n_subtypes"] == "0"
    folder = tmp_path / "Example"
    assert {p.name for p in folder.iterdir()} == {
        "kb.yaml",
        "README.md",
        "proxy-merges.json",
    }
    readme = (folder / "README.md").read_text()
    assert "not been run" in readme
    assert "were accepted" not in readme
    before = {p: p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    boomer.main(args)
    assert all(p.read_bytes() == content for p, content in before.items())

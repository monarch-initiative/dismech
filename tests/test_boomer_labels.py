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

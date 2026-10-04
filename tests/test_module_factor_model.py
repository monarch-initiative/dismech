"""Tests for the anchored module-factor model (module_factor_model)."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

import importlib.util

_SPEC = importlib.util.spec_from_file_location(
    "module_factor_model",
    Path(__file__).resolve().parents[1] / "scripts" / "module_factor_model.py",
)
mfm = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(mfm)  # type: ignore[union-attr]


def _write(path: Path, obj) -> None:
    path.write_text(yaml.safe_dump(obj, sort_keys=False))


def _disorder(name: str, mondo: str, node: str, conforms: str | None) -> dict:
    patho = {"name": node}
    if conforms:
        patho["conforms_to"] = conforms
    return {
        "name": name,
        "disease_term": {"term": {"id": mondo, "label": name.lower()}},
        "pathophysiology": [patho],
        "phenotypes": [
            {"name": "Seizure",
             "phenotype_term": {"term": {"id": "HP:0001250", "label": "Seizure"}}},
            {"name": "Ataxia",
             "phenotype_term": {"term": {"id": "HP:0001251", "label": "Ataxia"}}},
        ],
    }


def _pathograph(path: Path, node: str) -> None:
    path.write_text(json.dumps({
        "nodes": [
            {"id": node, "node_type": "pathophysiology"},
            {"id": "Seizure", "node_type": "phenotype", "meta": {"term_id": "HP:0001250"}},
            {"id": "Ataxia", "node_type": "phenotype", "meta": {"term_id": "HP:0001251"}},
        ],
        "edges": [
            {"source": node, "target": "Seizure", "predicate": "causes"},
            {"source": node, "target": "Ataxia", "predicate": "causes"},
        ],
    }))


def _make_kb(tmp_path: Path) -> tuple[Path, Path, Path]:
    modules, disorders, pathographs = (tmp_path / p for p in ("modules", "disorders", "pathographs"))
    for d in (modules, disorders, pathographs):
        d.mkdir()
    _write(modules / "mymod.yaml", {"name": "My Mechanism", "pathophysiology": [{"name": "Node A"}]})
    # two conformers build the module's phenotype signature
    _write(disorders / "ConformerA.yaml", _disorder("ConformerA", "MONDO:0000001", "Local A", "mymod#Node A"))
    _write(disorders / "ConformerB.yaml", _disorder("ConformerB", "MONDO:0000002", "Local B", "mymod#Node A"))
    _pathograph(pathographs / "MONDO_0000001.json", "Local A")
    _pathograph(pathographs / "MONDO_0000002.json", "Local B")
    # a non-conformer whose phenotype profile matches the module -> candidate
    _write(disorders / "Candidate.yaml", _disorder("Candidate", "MONDO:0000003", "Something Else", None))
    return modules, disorders, pathographs


def test_candidate_conformance_detected_and_conformers_excluded(tmp_path: Path) -> None:
    modules, disorders, pathographs = _make_kb(tmp_path)
    result = mfm.build(modules, disorders, pathographs)

    cand_diseases = {c["disease"] for c in result["candidates"]}
    # The non-conformer that shares the module's phenotypes is surfaced...
    assert "Candidate" in cand_diseases
    # ...and the declared conformers are NOT proposed as candidates for mymod.
    assert not any(c["disease"] in {"ConformerA", "ConformerB"} and c["module"] == "mymod"
                   for c in result["candidates"])

    cand = next(c for c in result["candidates"] if c["disease"] == "Candidate")
    assert cand["module"] == "mymod"
    assert cand["shared"] >= mfm.MIN_SHARED


def test_recovery_ranks_declared_module(tmp_path: Path) -> None:
    modules, disorders, pathographs = _make_kb(tmp_path)
    result = mfm.build(modules, disorders, pathographs)
    s = result["summary"]
    assert s["n_modules"] == 1
    # both conformers recover their one declared module leave-one-out
    assert s["n_diseases_in_recovery_eval"] == 2
    assert s["recovery"]["recall_at_1"] == 1.0

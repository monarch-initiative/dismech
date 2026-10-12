"""Tests for module -> phenotype anchor attribution (module_phenotype_anchors)."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

from dismech.export import module_phenotype_anchors as mpa


def _write(path: Path, obj) -> None:
    path.write_text(yaml.safe_dump(obj, sort_keys=False))


def _make_kb(tmp_path: Path) -> tuple[Path, Path, Path]:
    modules = tmp_path / "modules"
    disorders = tmp_path / "disorders"
    pathographs = tmp_path / "pathographs"
    for d in (modules, disorders, pathographs):
        d.mkdir()

    _write(
        modules / "mymod.yaml",
        {"name": "My Mechanism", "pathophysiology": [{"name": "Node A"}]},
    )
    _write(
        disorders / "Good_Disease.yaml",
        {
            "name": "Good Disease",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "good"}},
            "pathophysiology": [{"name": "Local Node", "conforms_to": "mymod#Node A"}],
        },
    )
    # Pathograph: Local Node --causes--> a phenotype; an unreachable phenotype too.
    (pathographs / "MONDO_0000001.json").write_text(
        json.dumps(
            {
                "nodes": [
                    {"id": "Local Node", "node_type": "pathophysiology"},
                    {"id": "Downstream Sign", "node_type": "phenotype",
                     "meta": {"term_id": "HP:0001250"}},
                    {"id": "Unrelated Sign", "node_type": "phenotype",
                     "meta": {"term_id": "HP:0004322"}},
                ],
                "edges": [
                    {"source": "Local Node", "target": "Downstream Sign", "predicate": "causes"},
                ],
            }
        )
    )
    return modules, disorders, pathographs


def test_branch_attribution_credits_only_downstream_phenotypes(tmp_path: Path) -> None:
    modules, disorders, pathographs = _make_kb(tmp_path)
    result = mpa.build(modules, disorders, pathographs)

    anchors = result["modules"]["mymod"]
    hpo_ids = {r["hpo_id"] for r in anchors}
    # The downstream phenotype is credited; the unreachable one is not.
    assert "HP:0001250" in hpo_ids
    assert "HP:0004322" not in hpo_ids

    row = next(r for r in anchors if r["hpo_id"] == "HP:0001250")
    assert row["n_diseases"] == 1
    assert row["diseases"] == ["Good Disease"]
    assert row["label"] == "Downstream Sign"

    cov = result["coverage"]
    assert cov["resolved_edges"] == 1
    assert cov["edges_reached_phenotype"] == 1


def test_missing_pathograph_is_counted_not_crashed(tmp_path: Path) -> None:
    modules, disorders, pathographs = _make_kb(tmp_path)
    # Remove the pathograph so the one conforming edge has no graph.
    (pathographs / "MONDO_0000001.json").unlink()
    result = mpa.build(modules, disorders, pathographs)
    assert result["modules"] == {}
    assert result["coverage"]["edges_no_pathograph"] == 1

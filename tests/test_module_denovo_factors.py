"""Tests for learned de-novo factors (module_denovo_factors)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import module_denovo_factors as mdf  # noqa: E402


def _write(path: Path, obj) -> None:
    path.write_text(yaml.safe_dump(obj, sort_keys=False))


def _disorder(name, mondo, phenos, node=None, conforms=None):
    d = {
        "name": name,
        "disease_term": {"term": {"id": mondo, "label": name.lower()}},
        "phenotypes": [
            {"name": lbl, "phenotype_term": {"term": {"id": hp, "label": lbl}}}
            for hp, lbl in phenos
        ],
    }
    if node:
        patho = {"name": node}
        if conforms:
            patho["conforms_to"] = conforms
        d["pathophysiology"] = [patho]
    return d


def _pathograph(path, node, phenos):
    nodes = [{"id": node, "node_type": "pathophysiology"}]
    edges = []
    for hp, lbl in phenos:
        nodes.append({"id": lbl, "node_type": "phenotype", "meta": {"term_id": hp}})
        edges.append({"source": node, "target": lbl, "predicate": "causes"})
    path.write_text(json.dumps({"nodes": nodes, "edges": edges}))


def test_denovo_factor_recovers_uncovered_phenotype_cluster(tmp_path: Path) -> None:
    modules, disorders, pathographs = (tmp_path / p for p in ("modules", "disorders", "pathographs"))
    for d in (modules, disorders, pathographs):
        d.mkdir()

    anchored = [("HP:0001250", "Seizure"), ("HP:0001251", "Ataxia")]
    novel = [("HP:0004322", "Short stature"), ("HP:0001263", "Global developmental delay")]

    _write(modules / "mymod.yaml", {"name": "My Mechanism", "pathophysiology": [{"name": "Node A"}]})
    # two conformers anchor mymod on the {Seizure, Ataxia} signature
    for i, nm in enumerate(["ConformerA", "ConformerB"], start=1):
        _write(disorders / f"{nm}.yaml",
               _disorder(nm, f"MONDO:000000{i}", anchored, node=f"Local {i}", conforms="mymod#Node A"))
        _pathograph(pathographs / f"MONDO_000000{i}.json", f"Local {i}", anchored)
    # a cluster of non-conformers sharing a phenotype pair NO module covers
    for i in range(3, 9):
        _write(disorders / f"Novel{i}.yaml", _disorder(f"Novel{i}", f"MONDO:000001{i}", novel))

    result = mdf.build(modules, disorders, pathographs, k=3, iters=250, seed=0)

    # some de-novo factor should capture the uncovered {short stature, GDD} cluster,
    # and it should be flagged fully novel (neither phenotype is in any module).
    hit = None
    for fac in result["factors"]:
        hpos = {p["hpo_id"] for p in fac["top_phenotypes"]}
        if {"HP:0004322", "HP:0001263"} <= hpos:
            hit = fac
            break
    assert hit is not None, "no de-novo factor captured the uncovered phenotype cluster"
    assert hit["novelty"] == 1.0
    assert any(d["disease"].startswith("Novel") for d in hit["top_diseases"])

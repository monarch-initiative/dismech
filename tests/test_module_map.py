"""Tests for the mechanism-module map extractor (dismech.export.module_map)."""
from __future__ import annotations

from pathlib import Path

import yaml

from dismech.export import module_map


def _write(path: Path, obj: dict) -> None:
    path.write_text(yaml.safe_dump(obj, sort_keys=False))


def _make_kb(tmp_path: Path) -> tuple[Path, Path]:
    modules = tmp_path / "modules"
    disorders = tmp_path / "disorders"
    modules.mkdir()
    disorders.mkdir()

    _write(
        modules / "mymod.yaml",
        {
            "name": "My Mechanism",
            "description": "A test module.\nSecond line.",
            "pathophysiology": [
                {
                    "name": "Node A",
                    "cell_types": [{"term": {"id": "CL:0000057", "label": "fibroblast"}}],
                    "biological_processes": [
                        {"term": {"id": "GO:0006954", "label": "inflammatory response"}}
                    ],
                },
                {
                    "name": "Node B",
                    "biological_processes": [
                        {"term": {"id": "GO:0007179", "label": "TGF-beta signaling"}}
                    ],
                },
            ],
        },
    )
    # Second module sharing GO:0006954 with mymod (tests shared_terms).
    _write(
        modules / "othermod.yaml",
        {
            "name": "Other",
            "pathophysiology": [
                {
                    "name": "Only Node",
                    "biological_processes": [
                        {"term": {"id": "GO:0006954", "label": "inflammatory response"}}
                    ],
                }
            ],
        },
    )
    return modules, disorders


def test_module_signature_collects_cl_and_go(tmp_path: Path) -> None:
    modules, _ = _make_kb(tmp_path)
    sig = module_map.module_signature(modules / "mymod.yaml")
    assert sig["module"] == "mymod"
    assert sig["name"] == "My Mechanism"
    assert sig["node_names"] == ["Node A", "Node B"]
    assert sig["signature"]["CL"] == ["CL:0000057"]
    assert sig["signature"]["GO"] == ["GO:0006954", "GO:0007179"]
    assert sig["n_hp"] == 0  # modules encode mechanism, not phenotypes


def test_incidence_resolution_and_audit(tmp_path: Path) -> None:
    modules, disorders = _make_kb(tmp_path)
    _write(
        disorders / "Good_Disease.yaml",
        {
            "name": "Good Disease",
            "disease_term": {"term": {"id": "MONDO:0000001", "label": "good"}},
            "pathophysiology": [
                {"name": "Local Node", "conforms_to": "mymod#Node A"},
            ],
        },
    )
    _write(
        disorders / "Bad_Node.yaml",
        {
            "name": "Bad Node",
            "pathophysiology": [{"name": "X", "conforms_to": "mymod#No Such Node"}],
        },
    )
    _write(
        disorders / "Bad_Module.yaml",
        {
            "name": "Bad Module",
            "pathophysiology": [{"name": "Y", "conforms_to": "ghostmod#Node A"}],
        },
    )

    result = module_map.build(modules, disorders)
    audit = result["audit"]

    assert audit["n_modules"] == 2
    assert audit["n_conforms_edges"] == 3
    assert audit["n_edges_resolved"] == 1
    assert audit["n_diseases_conforming"] == 3

    good = next(r for r in result["incidence"] if r["disease"] == "Good Disease")
    assert good["resolves"] is True
    assert good["module"] == "mymod"
    assert good["module_node"] == "Node A"
    assert good["disorder_node"] == "Local Node"
    assert good["disease_mondo"] == "MONDO:0000001"

    reasons = {r["disease"]: r["reason"] for r in audit["unresolved_conforms"]}
    assert reasons["Bad Node"] == "unknown node"
    assert reasons["Bad Module"] == "unknown module"

    # GO:0006954 is carried by both modules -> reported as shared.
    assert result["shared_terms"]["GO:0006954"] == ["mymod", "othermod"]
    # othermod is defined but never conformed to -> unused.
    assert "othermod" in audit["modules_unused"]

"""Tests for curated mechanism-module collections."""

from pathlib import Path

from dismech.module_collections import (
    build_module_collection_tree,
    module_collection_reference_errors,
)


def _record(name: str, **values: object) -> tuple[Path, dict]:
    return Path(f"{name}.yaml"), {"name": name, **values}


def test_reference_checks_accept_valid_nested_collections() -> None:
    records = [
        _record(
            "Parent",
            module_members=[{"module": "alpha"}],
            child_collections=["Child"],
        ),
        _record("Child", module_members=[{"module": "beta"}]),
    ]

    assert not module_collection_reference_errors(records, {"alpha", "beta"})


def test_reference_checks_report_bad_modules_and_collection_cycles() -> None:
    records = [
        _record(
            "First",
            module_members=[
                {"module": "missing"},
                {"module": "alpha#Node"},
                {"module": "alpha"},
            ],
            child_collections=["Second", "Unknown"],
        ),
        _record(
            "Second",
            module_members=[{"module": "alpha"}, {"module": "alpha"}],
            child_collections=["First"],
        ),
    ]

    errors = module_collection_reference_errors(records, {"alpha"})

    assert any("no kb/modules/missing.yaml" in error for error in errors)
    assert any("node anchors are not allowed" in error for error in errors)
    assert any("duplicate module 'alpha'" in error for error in errors)
    assert any("unknown collection 'Unknown'" in error for error in errors)
    assert any("module collection cycle" in error for error in errors)


def test_collection_tree_preserves_explicit_nesting() -> None:
    collections = [
        {
            "name": "Parent",
            "href": "Parent.html",
            "module_count": 2,
            "child_collection_names": ["Child"],
        },
        {
            "name": "Child",
            "href": "Child.html",
            "module_count": 1,
            "child_collection_names": [],
        },
        {
            "name": "Independent",
            "href": "Independent.html",
            "module_count": 1,
            "child_collection_names": [],
        },
    ]

    tree = build_module_collection_tree(collections)

    assert tree["root_count"] == 2
    assert tree["edge_count"] == 1
    parent = next(node for node in tree["roots"] if node["name"] == "Parent")
    assert [child["name"] for child in parent["children"]] == ["Child"]

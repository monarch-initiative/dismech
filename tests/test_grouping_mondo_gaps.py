"""Tests for grouping MONDO gap reporting helpers."""

from pathlib import Path

import yaml

from scripts import grouping_mondo_gaps


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_grouping_mondo_terms_defaults_to_exact_mappings(
    tmp_path: Path, monkeypatch
) -> None:
    """Only exact mappings should drive default descendant-gap reports."""
    groupings_dir = tmp_path / "groupings"
    monkeypatch.setattr(grouping_mondo_gaps, "GROUPINGS_DIR", str(groupings_dir))

    _write_yaml(
        groupings_dir / "Exact.yaml",
        {
            "name": "Exact Group",
            "mappings": {
                "mondo_mappings": [
                    {
                        "term": {"id": "MONDO:0000001", "label": "exact concept"},
                        "mapping_predicate": "skos:exactMatch",
                    }
                ]
            },
        },
    )
    _write_yaml(
        groupings_dir / "Narrow.yaml",
        {
            "name": "Narrow Group",
            "mappings": {
                "mondo_mappings": [
                    {
                        "term": {"id": "MONDO:0000002", "label": "broad concept"},
                        "mapping_predicate": "skos:narrowMatch",
                    }
                ]
            },
        },
    )

    assert grouping_mondo_gaps.grouping_mondo_terms() == [
        ("Exact Group", "MONDO:0000001", "skos:exactMatch")
    ]
    assert grouping_mondo_gaps.grouping_mondo_terms(include_inexact=True) == [
        ("Exact Group", "MONDO:0000001", "skos:exactMatch"),
        ("Narrow Group", "MONDO:0000002", "skos:narrowMatch"),
    ]


def test_audit_recommendation_keeps_exactness_separate_from_coverage() -> None:
    """Incomplete DisMech coverage should not be a mapping-predicate downgrade."""
    assert (
        grouping_mondo_gaps._audit_recommendation("skos:closeMatch", outside_count=0)
        == "consider skos:exactMatch; partial DisMech coverage is not a downgrade reason"
    )
    assert grouping_mondo_gaps._audit_recommendation(
        "skos:exactMatch", outside_count=2
    ).startswith("keep exactMatch")
    assert (
        grouping_mondo_gaps._audit_recommendation("skos:narrowMatch", outside_count=0)
        == "keep skos:narrowMatch unless conceptual scope changes"
    )

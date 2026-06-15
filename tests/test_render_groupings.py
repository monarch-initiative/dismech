"""Tests for disease grouping page rendering."""

from pathlib import Path

import yaml

from dismech.render import render_all_groupings


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def test_render_all_groupings_builds_index_from_grouping_yaml(tmp_path: Path) -> None:
    """The grouping index should be generated from kb/groupings/*.yaml inputs."""
    input_dir = tmp_path / "kb" / "groupings"
    disorders_dir = tmp_path / "kb" / "disorders"
    output_dir = tmp_path / "pages" / "groupings"
    disorders_dir.mkdir(parents=True)

    _write_yaml(
        input_dir / "Beta_Group.yaml",
        {
            "name": "Beta_Group",
            "display_name": "Beta Group",
            "description": "Second test grouping.",
            "grouping_basis": ["SHARED_MECHANISM"],
            "mappings": {
                "mondo_mappings": [
                    {
                        "term": {
                            "id": "MONDO:7654321",
                            "label": "beta grouping",
                        },
                        "mapping_predicate": "skos:narrowMatch",
                        "mapping_source": "MONDO",
                    }
                ]
            },
            "membership_criteria": [
                {
                    "description": "Members share the beta mechanism.",
                    "criteria_semantics": "NECESSARY",
                    "logic": {
                        "criterion_predicate": "OTHER",
                        "description": "Test-only criterion.",
                    },
                }
            ],
            "members": [],
        },
    )
    _write_yaml(
        input_dir / "Alpha_Group.yaml",
        {
            "name": "Alpha_Group",
            "display_name": "Alpha Group",
            "description": "First test grouping.",
            "grouping_basis": ["SHARED_PATHWAY"],
            "mappings": {
                "mondo_mappings": [
                    {
                        "term": {
                            "id": "MONDO:1234567",
                            "label": "alpha grouping",
                        },
                        "mapping_predicate": "skos:exactMatch",
                        "mapping_source": "MONDO",
                    }
                ]
            },
            "membership_criteria": [],
            "members": [
                {
                    "member": "Alpha Disorder",
                    "member_type": "DISEASE",
                }
            ],
        },
    )
    _write_yaml(
        disorders_dir / "Beta_Disorder.yaml",
        {
            "name": "Beta Disorder",
            "disease_term": {
                "preferred_term": "Beta disorder",
                "term": {
                    "id": "MONDO:7654321",
                    "label": "beta disorder",
                },
            },
        },
    )
    beta_group = yaml.safe_load((input_dir / "Beta_Group.yaml").read_text())
    beta_group["members"] = [
        {
            "member": "Beta Disorder",
            "member_type": "DISEASE",
        }
    ]
    _write_yaml(input_dir / "Beta_Group.yaml", beta_group)
    _write_yaml(
        disorders_dir / "Alpha_Disorder.yaml",
        {
            "name": "Alpha Disorder",
            "disease_term": {
                "preferred_term": "Alpha disorder",
                "term": {
                    "id": "MONDO:1234567",
                    "label": "alpha disorder",
                },
            },
        },
    )

    output_paths = render_all_groupings(
        input_dir=input_dir,
        output_dir=output_dir,
        disorders_dir=disorders_dir,
    )

    assert output_dir / "Alpha_Group.html" in output_paths
    assert output_dir / "Beta_Group.html" in output_paths
    assert output_dir / "index.html" in output_paths

    html = (output_dir / "index.html").read_text()
    assert "2 groupings" in html
    assert 'href="Alpha_Group.html">Alpha Group</a>' in html
    assert 'href="Beta_Group.html">Beta Group</a>' in html
    assert "skos:exactMatch MONDO:1234567" in html
    assert 'href="http://purl.obolibrary.org/obo/MONDO_1234567"' in html
    assert "Coverage 1/1 (100.0%)" in html
    assert "Coverage not assessed" in html
    assert html.index("Alpha Group") < html.index("Beta Group")

    detail_html = (output_dir / "Alpha_Group.html").read_text()
    assert "Coverage and gaps" in detail_html
    assert "Alpha Disorder" in detail_html
    assert "MONDO:1234567" in detail_html
    assert "DisMech coverage of exact MONDO scope: 1/1 (100.0%)" in detail_html
    assert "listed in scope" in detail_html
    assert "In grouping MONDO" in detail_html

    beta_detail_html = (output_dir / "Beta_Group.html").read_text()
    assert "Exact MONDO scope not assessed" in beta_detail_html
    assert "listed with MONDO ID" in beta_detail_html
    assert "not assessed" in beta_detail_html

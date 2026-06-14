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
            "membership_criteria": [],
            "members": [],
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
    assert html.index("Alpha Group") < html.index("Beta Group")

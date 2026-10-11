"""Subtype inheritance pills render a label, never the raw inheritance record (#13773)."""

from pathlib import Path

import pytest
import yaml

from dismech.render import render_disorder


@pytest.mark.parametrize(
    ("inheritance", "expected"),
    [
        ({"name": "Autosomal Dominant"}, "Autosomal Dominant"),
        (
            {
                "name": "AD",
                "inheritance_term": {
                    "preferred_term": "Autosomal dominant",
                    "term": {
                        "id": "HP:0000006",
                        "label": "Autosomal dominant inheritance",
                    },
                },
            },
            "Autosomal dominant",
        ),
        (
            {
                "name": "AD",
                "inheritance_term": {
                    "term": {
                        "id": "HP:0000006",
                        "label": "Autosomal dominant inheritance",
                    }
                },
            },
            "Autosomal dominant inheritance",
        ),
    ],
)
def test_subtype_inheritance_pill_renders_label(
    tmp_path: Path, inheritance: dict, expected: str
) -> None:
    path = tmp_path / "Example_Disorder.yaml"
    path.write_text(
        yaml.safe_dump(
            {
                "name": "Example Disorder",
                "has_subtypes": [{"name": "Type 1", "inheritance": [inheritance]}],
            },
            sort_keys=False,
        )
    )
    output_path = tmp_path / "pages" / "disorders" / "Example_Disorder.html"
    render_disorder(path, output_path=output_path)

    html = output_path.read_text()
    assert f'<span class="subtype-inheritance-tag">{expected}</span>' in html
    assert "{&#39;name&#39;" not in html
    assert "{'name'" not in html

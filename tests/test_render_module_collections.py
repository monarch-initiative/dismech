"""Rendering integration tests for module collections and the module browser."""

from pathlib import Path

import yaml

from dismech.render import render_all_modules


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def _module(name: str, description: str) -> dict:
    return {
        "name": name,
        "category": "Module",
        "description": description,
        "pathophysiology": [
            {
                "name": f"{name} process",
                "description": "A test mechanism node.",
            }
        ],
    }


def test_render_all_modules_builds_collection_navigation_and_backlinks(
    tmp_path: Path,
) -> None:
    modules_dir = tmp_path / "kb" / "modules"
    collections_dir = tmp_path / "kb" / "module_collections"
    disorders_dir = tmp_path / "kb" / "disorders"
    output_dir = tmp_path / "pages" / "modules"
    collections_output_dir = tmp_path / "pages" / "module-collections"
    disorders_dir.mkdir(parents=True)

    _write_yaml(modules_dir / "alpha.yaml", _module("Alpha mechanism", "First."))
    _write_yaml(modules_dir / "beta.yaml", _module("Beta mechanism", "Second."))
    _write_yaml(
        collections_dir / "Framework.yaml",
        {
            "name": "Test Framework",
            "collection_type": "PUBLISHED_FRAMEWORK",
            "description": "A test scientific framework.",
            "module_members": [
                {
                    "module": "alpha",
                    "framework_terms": ["Framework alpha"],
                }
            ],
        },
    )

    rendered = render_all_modules(
        modules_dir,
        output_dir,
        disorders_dir=disorders_dir,
        collections_dir=collections_dir,
        collections_output_dir=collections_output_dir,
    )

    module_index = (output_dir / "index.html").read_text()
    alpha_page = (output_dir / "alpha.html").read_text()
    collection_page = (collections_output_dir / "Test_Framework.html").read_text()
    collection_index = (collections_output_dir / "index.html").read_text()

    assert "Module collections" in module_index
    assert 'id="collection-filter"' in module_index
    assert 'class="module-row"' in module_index
    assert "Not yet in a collection" in module_index
    assert "Test Framework" in module_index
    assert "Module Collections" in alpha_page
    assert "Framework alpha" in alpha_page
    assert "Alpha mechanism" in collection_page
    assert "Framework alpha" in collection_page
    assert "Test Framework" in collection_index
    assert output_dir / "beta.html" in rendered
    assert collections_output_dir / "Test_Framework.html" in rendered


def test_render_all_modules_rejects_unknown_collection_module(tmp_path: Path) -> None:
    modules_dir = tmp_path / "kb" / "modules"
    collections_dir = tmp_path / "kb" / "module_collections"
    disorders_dir = tmp_path / "kb" / "disorders"
    disorders_dir.mkdir(parents=True)
    _write_yaml(modules_dir / "alpha.yaml", _module("Alpha mechanism", "First."))
    _write_yaml(
        collections_dir / "Broken.yaml",
        {
            "name": "Broken",
            "collection_type": "OTHER",
            "module_members": [{"module": "not_real"}],
        },
    )

    try:
        render_all_modules(
            modules_dir,
            tmp_path / "pages" / "modules",
            disorders_dir=disorders_dir,
            collections_dir=collections_dir,
            collections_output_dir=tmp_path / "pages" / "module-collections",
        )
    except ValueError as error:
        assert "no kb/modules/not_real.yaml" in str(error)
    else:
        raise AssertionError("Unknown module reference should stop rendering")

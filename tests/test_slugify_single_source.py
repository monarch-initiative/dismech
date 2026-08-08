"""Pin ``slugify`` to a single implementation across renderer and exporters.

The renderer names page files on disk with ``slugify(name)``; the exporters
build the ``page_url`` values that point at those files with ``slugify(name)``
too. If those ever stop being the *same function*, the browser index links to
files that do not exist — and since ``scripts/check_browser_data_links.py`` is
fail-closed, that now stops the publish pipeline rather than producing quiet
404s. This used to be five byte-identical copies, three of which recorded the
coupling in a docstring instead of enforcing it (review on PR #7909).
"""

import ast
from pathlib import Path

import pytest

from dismech import render
from dismech.export import (
    browser_export,
    discussions_export,
    models_export,
    pathograph_export,
)
from dismech.export.utils import slugify

REPO_ROOT = Path(__file__).resolve().parents[1]

# Modules that must all share the canonical page-slug implementation.
PAGE_SLUG_MODULES = [
    render,
    browser_export,
    models_export,
    discussions_export,
    pathograph_export,
]


@pytest.mark.parametrize(
    "module", PAGE_SLUG_MODULES, ids=lambda m: m.__name__.split(".")[-1]
)
def test_module_uses_the_canonical_slugify(module):
    assert module.slugify is slugify, (
        f"{module.__name__}.slugify is not dismech.export.utils.slugify — "
        "a re-forked copy will drift and break page links"
    )


@pytest.mark.parametrize(
    "module", PAGE_SLUG_MODULES, ids=lambda m: m.__name__.split(".")[-1]
)
def test_module_does_not_redefine_slugify(module):
    """Import identity can be satisfied then shadowed; forbid the def outright."""
    source = Path(module.__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    defs = [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef) and node.name == "slugify"
    ]
    assert not defs, f"{module.__name__} redefines slugify; import it instead"


def test_hpoa_slugify_is_deliberately_different():
    """The HPOA slug is a separate, lowercase-hyphenated scheme — keep it apart."""
    from dismech.export import hpoa_export

    assert hpoa_export.slugify is not slugify
    assert hpoa_export.slugify("Marfan Syndrome") == "marfan-syndrome"
    assert slugify("Marfan Syndrome") == "Marfan_Syndrome"


def test_page_slug_behaviour_is_unchanged():
    """Byte-for-byte the behaviour of the five copies this replaced."""
    assert slugify("Holt-Oram syndrome") == "Holt-Oram_syndrome"
    assert slugify("Beta-Thalassemia (Cooley Anemia)") == "Beta-Thalassemia_Cooley_Anemia"
    assert slugify("22q11.2 Deletion Syndrome") == "22q11.2_Deletion_Syndrome"
    assert slugify("Aortic/Mitral Valve Disease") == "Aortic_Mitral_Valve_Disease"
    assert slugify("") == ""


def test_no_other_page_slug_copies_remain():
    """Guard against a sixth copy appearing in src/dismech/."""
    canonical_body = 'name.replace(" ", "_").replace("/", "_")'
    offenders = []
    for path in (REPO_ROOT / "src" / "dismech").rglob("*.py"):
        if path.name == "utils.py" and path.parent.name == "export":
            continue
        text = path.read_text(encoding="utf-8")
        if canonical_body in text or canonical_body.replace('"', "'") in text:
            offenders.append(str(path.relative_to(REPO_ROOT)))
    assert not offenders, (
        "page-slug logic re-inlined in: "
        + ", ".join(offenders)
        + " — import dismech.export.utils.slugify instead"
    )

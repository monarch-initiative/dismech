"""Generated per-model pages, pages/models/<model_id>.html (issue #13123).

Rendered from the real model folders, with a disorders directory holding only
the two disorder entries the models belong to, so the walk stays fast.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import pytest
import yaml

from dismech import model_registry
from dismech.model_pages import build_model_context, render_all_model_pages

REPO_ROOT = Path(__file__).resolve().parents[1]
MODELS_DIR = REPO_ROOT / "models"
MODULES_DIR = REPO_ROOT / "kb" / "modules"


@pytest.fixture(scope="module")
def pages(tmp_path_factory: pytest.TempPathFactory) -> dict[str, str]:
    tmp = tmp_path_factory.mktemp("model_pages")
    disorders = tmp / "disorders"
    disorders.mkdir()
    for name in ("Gout.yaml", "Rosacea.yaml"):
        shutil.copy(REPO_ROOT / "kb" / "disorders" / name, disorders / name)
    out = tmp / "pages" / "models"
    out.mkdir(parents=True)
    (out / "stale_model.html").write_text("left behind by a removed model")
    written = render_all_model_pages(
        MODELS_DIR, out, disorders_dir=disorders, modules_dir=MODULES_DIR
    )
    assert not (out / "stale_model.html").exists(), "a full render prunes orphans"
    return {path.stem: path.read_text() for path in written}


def test_one_page_per_model_folder_plus_index(pages: dict[str, str]) -> None:
    folders = {p.name for p in model_registry.iter_model_dirs(MODELS_DIR)}
    assert set(pages) == folders | {"index"}
    for model_id in folders:
        assert f'href="{model_id}.html"' in pages["index"]


def test_abm_page_runs_in_the_browser(pages: dict[str, str]) -> None:
    html = pages["neuronal_migration_abm"]
    assert 'id="run-in-browser"' in html
    # run.js inlined verbatim, and the spec it needs embedded as JSON.
    js = (MODELS_DIR / "neuronal_migration_abm" / "run.js").read_text()
    assert js.strip() in html
    assert "const SPEC = {" in html
    assert "NeuronalMigrationABM" in html


def test_abm_page_lists_scenarios_in_spec_order(pages: dict[str, str]) -> None:
    spec = yaml.safe_load(
        (MODELS_DIR / "neuronal_migration_abm" / "spec.yaml").read_text()
    )
    section = (
        pages["neuronal_migration_abm"].split('id="scenarios"')[1].split("</tbody>")[0]
    )
    order = re.findall(r"<td[^>]*><code>([a-z_]+)</code>", section)
    assert order == list(spec["scenarios"])


def test_abm_page_shows_rules_with_provenance(pages: dict[str, str]) -> None:
    html = pages["neuronal_migration_abm"]
    for rule in (
        "effective_perturbation",
        "arrest",
        "slowed_nucleokinesis",
        "inside_out_settling",
    ):
        assert f'<div class="rule-name">{rule}' in html
    # The one rule no curated edge states is flagged, not passed off as curated.
    assert re.search(r"inside_out_settling<span class=\"badge-assumption\">", html)
    # maps_to links land on the module page's node anchor.
    assert (
        'href="../modules/microtubule_dependent_neuronal_migration_failure.html'
        '#module-pathophysiology-microtubule-apparatus-perturbation"' in html
    )


def test_boolean_page_shows_the_intervention_scan(pages: dict[str, str]) -> None:
    html = pages["rosacea_innate_boolean"]
    assert 'id="interventions"' in html
    assert "Acaricide" in html
    assert 'id="run-in-browser"' not in html  # no run.js, so no runner


def test_perturb_page_shows_the_committed_run(pages: dict[str, str]) -> None:
    html = pages["urate_homeostasis"]
    assert "Simulation results" in html
    assert "Gene effects" in html
    # A scenario root links into the disorder page's node, not an in-page anchor.
    assert 'href="../disorders/Gout.html#pathophysiology-hyperuricemia"' in html
    assert "uv run python -m dismech.perturb" in html


def test_usage_links_to_the_card_on_the_entry_page(pages: dict[str, str]) -> None:
    html = pages["urate_homeostasis"]
    assert re.search(
        r'href="\.\./disorders/Gout\.html#computational-model-[a-z0-9-]+"', html
    )


def test_runner_refuses_to_inline_a_script_close_tag(tmp_path: Path) -> None:
    folder = tmp_path / "evil_model"
    folder.mkdir()
    (folder / "spec.yaml").write_text("model_id: evil_model\n")
    (folder / "run.js").write_text("const s = '</script><script>alert(1)';\n")
    with pytest.raises(ValueError, match="</script"):
        build_model_context(folder, [])

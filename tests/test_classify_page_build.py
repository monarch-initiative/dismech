"""Tests for the full-vs-incremental page-build classifier (issue #5507)."""

import hashlib
import importlib.util
import sys
from pathlib import Path

_SPEC = importlib.util.spec_from_file_location(
    "classify_page_build",
    Path(__file__).resolve().parents[1] / "scripts" / "classify_page_build.py",
)
classify_page_build = importlib.util.module_from_spec(_SPEC)
# Register before exec so the module's @dataclass can resolve its own module.
sys.modules[_SPEC.name] = classify_page_build
_SPEC.loader.exec_module(classify_page_build)
classify = classify_page_build.classify


def test_single_disorder_is_incremental():
    d = classify([("M", "kb/disorders/Asthma.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == ["kb/disorders/Asthma.yaml"]


def test_curation_pr_with_reference_cache_and_history_is_incremental():
    # The common curation PR shape: a disorder edit plus its cached references
    # and a history record. Neutral companions must NOT force a full rebuild.
    d = classify(
        [
            ("M", "kb/disorders/Marfan_Syndrome.yaml"),
            ("A", "references_cache/PMID_12345678.md"),
            ("A", "history/disorders/Marfan_Syndrome/2026-07-06T00Z-claude-code-a1.yaml"),
            ("M", "cache/hp/terms.csv"),
        ]
    )
    assert d.mode == "incremental"
    assert d.disorder_files == ["kb/disorders/Marfan_Syndrome.yaml"]


def test_template_change_forces_full():
    d = classify([("M", "src/dismech/templates/disorder.html.j2")])
    assert d.mode == "full"


def test_render_py_change_forces_full():
    d = classify([("M", "src/dismech/render.py")])
    assert d.mode == "full"


def test_graph_and_export_changes_force_full():
    assert classify([("M", "src/dismech/graph.py")]).mode == "full"
    assert classify([("M", "src/dismech/export/browser_export.py")]).mode == "full"


def test_schema_change_forces_full():
    d = classify([("M", "src/dismech/schema/dismech.yaml")])
    assert d.mode == "full"


def test_justfile_and_conf_force_full():
    assert classify([("M", "project.justfile")]).mode == "full"
    assert classify([("M", "conf/qc_config.yaml")]).mode == "full"


def test_disorder_deletion_forces_full():
    d = classify([("D", "kb/disorders/Old_Disease.yaml")])
    assert d.mode == "full"


def test_disorder_rename_forces_full():
    d = classify([("R100", "kb/disorders/New_Name.yaml")])
    assert d.mode == "full"


def test_comorbidity_only_is_incremental_with_no_disorder_files():
    # A changed comorbidity is re-rendered by the always-run aggregate pass, so
    # no individual disorder page needs rendering.
    d = classify([("M", "kb/comorbidities/com_A__B.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_module_change_is_incremental():
    d = classify([("M", "kb/modules/fibrotic_response.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_research_report_is_incremental():
    d = classify([("A", "research/Foo-deep-research-falcon.md")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_history_yaml_is_neutral():
    d = classify([("A", "kb/disorders/Asthma.history.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_grouping_change_is_neutral_for_this_workflow():
    # Grouping pages are handled by a separate workflow.
    d = classify([("M", "kb/groupings/Mucopolysaccharidoses.yaml")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_docs_only_is_incremental():
    d = classify([("M", "docs/history.md")])
    assert d.mode == "incremental"
    assert d.disorder_files == []


def test_unknown_path_fails_safe_to_full():
    d = classify([("A", "some/unexpected/module.py")])
    assert d.mode == "full"


def test_mixed_local_and_global_is_full():
    d = classify(
        [
            ("M", "kb/disorders/Asthma.yaml"),
            ("M", "src/dismech/templates/disorder.html.j2"),
        ]
    )
    assert d.mode == "full"


def test_multiple_disorders_sorted_and_deduped():
    d = classify(
        [
            ("M", "kb/disorders/Zed.yaml"),
            ("M", "kb/disorders/Asthma.yaml"),
            ("M", "kb/disorders/Asthma.yaml"),
        ]
    )
    assert d.mode == "incremental"
    assert d.disorder_files == ["kb/disorders/Asthma.yaml", "kb/disorders/Zed.yaml"]


# --- post-render page/KB drift detection (PR #7903 follow-up) ----------------

detect_page_drift = classify_page_build.detect_page_drift
detect_page_content_drift = classify_page_build.detect_page_content_drift
extract_page_revision = classify_page_build.extract_page_revision
plan_heal = classify_page_build.plan_heal


def _yaml_for(name):
    """Per-disorder source text.

    Deliberately unique per name: the content check matches pages to inputs by
    digest, so identical bodies would collide into a single entry and report a
    false drift that has nothing to do with the case under test.
    """
    return f"name: {name}\n"


def _page_html(yaml_text, *, stamped=True):
    """A minimal rendered page carrying the renderer's ``yamlRevision`` stamp.

    Mirrors what ``render`` embeds through ``disorder.html.j2``'s ``OS_CONFIG``
    block: ``sha256(source yaml)[:12]``. ``stamped=False`` yields a page with no
    stamp, standing in for one rendered before the stamp existed.
    """
    if not stamped:
        return "<html>no stamp here</html>"
    revision = hashlib.sha256(yaml_text.encode()).hexdigest()[:12]
    return (
        "<html><script>const OS_CONFIG = "
        f'{{"yamlRevision": "{revision}"}};</script></html>'
    )


def _make_tree(tmp_path, disorders, pages, *, stale=(), unstamped=()):
    """Build a disorder/page tree.

    By default every page is stamped with its same-named disorder's digest, so
    the tree is healthy. ``stale`` names pages stamped from *superseded* source
    (the mid-build-merge shape); ``unstamped`` names pages carrying no stamp.
    """
    disorders_dir = tmp_path / "kb" / "disorders"
    pages_dir = tmp_path / "pages" / "disorders"
    disorders_dir.mkdir(parents=True)
    pages_dir.mkdir(parents=True)
    for name in disorders:
        (disorders_dir / f"{name}.yaml").write_text(_yaml_for(name))
    for name in pages:
        if name in unstamped:
            body = _page_html("", stamped=False)
        elif name in stale:
            body = _page_html(f"{_yaml_for(name)}# an older revision\n")
        else:
            body = _page_html(_yaml_for(name))
        (pages_dir / f"{name}.html").write_text(body)
    return disorders_dir, pages_dir


def test_no_drift_when_counts_match(tmp_path):
    disorders_dir, pages_dir = _make_tree(
        tmp_path, ["Asthma", "Marfan_Syndrome"], ["Asthma", "Marfan_Syndrome"]
    )
    assert detect_page_drift(disorders_dir, pages_dir) is None


def test_unrendered_disorder_is_drift(tmp_path):
    # The PR #7903 shape: a collapsed run's disorder never got a page.
    disorders_dir, pages_dir = _make_tree(
        tmp_path, ["Asthma", "Marfan_Syndrome"], ["Asthma"]
    )
    reason = detect_page_drift(disorders_dir, pages_dir)
    assert reason is not None
    assert "+1" in reason


def test_stale_extra_page_is_drift(tmp_path):
    disorders_dir, pages_dir = _make_tree(tmp_path, ["Asthma"], ["Asthma", "Deleted"])
    reason = detect_page_drift(disorders_dir, pages_dir)
    assert reason is not None
    assert "-1" in reason


def test_history_yaml_is_not_counted_as_a_page_input(tmp_path):
    disorders_dir, pages_dir = _make_tree(tmp_path, ["Asthma"], ["Asthma"])
    (disorders_dir / "Asthma.history.yaml").write_text("x: 1\n")
    assert detect_page_drift(disorders_dir, pages_dir) is None


def test_missing_directories_fail_safe_to_drift(tmp_path):
    disorders_dir, pages_dir = _make_tree(tmp_path, ["Asthma"], ["Asthma"])
    assert detect_page_drift(disorders_dir, tmp_path / "nope") is not None
    assert detect_page_drift(tmp_path / "nope", pages_dir) is not None


def test_drift_check_does_not_affect_diff_classification():
    # Drift is a separate, post-render signal; classify() stays diff-only so a
    # normal curation push is still incremental.
    d = classify([("A", "kb/disorders/New_Disease.yaml")])
    assert d.mode == "incremental"


# --- content drift: the page is present but stale (#8033 / #8085 fallout) ----


def test_extract_page_revision_reads_the_stamp():
    yaml_text = _yaml_for("Asthma")
    revision = extract_page_revision(_page_html(yaml_text))
    assert revision == hashlib.sha256(yaml_text.encode()).hexdigest()[:12]


def test_extract_page_revision_returns_none_without_a_stamp():
    assert extract_page_revision(_page_html("", stamped=False)) is None


def test_stale_page_with_equal_counts_is_drift(tmp_path):
    """The 2026-08-07 shape: right number of pages, wrong content in one.

    A KB merge landing mid-build is absent from that build's checkout, so its
    page keeps older content while the file counts stay perfectly equal. This is
    precisely what the count check cannot see.
    """
    disorders_dir, pages_dir = _make_tree(
        tmp_path,
        ["Asthma", "Sarcoidosis"],
        ["Asthma", "Sarcoidosis"],
        stale=["Sarcoidosis"],
    )
    # Tier 1 alone is satisfied: the counts genuinely agree.
    assert classify_page_build.count_disorder_inputs(
        disorders_dir
    ) == classify_page_build.count_rendered_pages(pages_dir)

    reason = detect_page_drift(disorders_dir, pages_dir)
    assert reason is not None
    assert "content drift" in reason
    assert "Sarcoidosis.html" in reason
    # The healthy page must not be blamed alongside the stale one.
    assert "Asthma.html" not in reason


def test_content_drift_reports_both_directions(tmp_path):
    disorders_dir, pages_dir = _make_tree(
        tmp_path, ["Asthma", "Sarcoidosis"], ["Asthma", "Sarcoidosis"], stale=["Sarcoidosis"]
    )
    stale, unrendered = detect_page_content_drift(disorders_dir, pages_dir)
    assert stale == ["Sarcoidosis.html"]
    assert unrendered == ["Sarcoidosis.yaml"]


def test_healthy_tree_has_no_content_drift(tmp_path):
    disorders_dir, pages_dir = _make_tree(
        tmp_path, ["Asthma", "Sarcoidosis"], ["Asthma", "Sarcoidosis"]
    )
    assert detect_page_content_drift(disorders_dir, pages_dir) == ([], [])
    assert detect_page_drift(disorders_dir, pages_dir) is None


def test_unstamped_page_fails_safe_to_drift(tmp_path):
    # A page that cannot prove it is current is assumed stale: one full rebuild,
    # then it carries a stamp and the check settles.
    disorders_dir, pages_dir = _make_tree(
        tmp_path, ["Asthma"], ["Asthma"], unstamped=["Asthma"]
    )
    assert detect_page_drift(disorders_dir, pages_dir) is not None


def test_rename_keeping_counts_equal_is_content_drift(tmp_path):
    """The gap the workflow calls out: 'a rename that keeps the counts equal'."""
    disorders_dir, pages_dir = _make_tree(tmp_path, ["New_Name"], ["Old_Name"])
    # Counts agree, so tier 1 sees nothing...
    assert classify_page_build.count_disorder_inputs(
        disorders_dir
    ) == classify_page_build.count_rendered_pages(pages_dir)
    # ...but the orphan page's stamp matches no current input.
    reason = detect_page_drift(disorders_dir, pages_dir)
    assert reason is not None
    assert "Old_Name.html" in reason


def test_count_drift_is_reported_before_content_drift(tmp_path):
    # Cheapest signal wins the message; both escalate to the same full rebuild.
    disorders_dir, pages_dir = _make_tree(
        tmp_path, ["Asthma", "Sarcoidosis"], ["Asthma"], stale=["Asthma"]
    )
    reason = detect_page_drift(disorders_dir, pages_dir)
    assert reason is not None
    assert "page/KB drift" in reason


def test_index_page_is_not_treated_as_a_stale_disorder_page(tmp_path):
    # index.html carries no disorder YAML and is kept by _prune_orphan_pages;
    # counting it as stale would escalate every build to full forever.
    disorders_dir, pages_dir = _make_tree(tmp_path, ["Asthma"], ["Asthma"])
    (pages_dir / "index.html").write_text("<html>index</html>")
    assert detect_page_drift(disorders_dir, pages_dir) is None


def test_history_yaml_is_not_a_content_drift_input(tmp_path):
    disorders_dir, pages_dir = _make_tree(tmp_path, ["Asthma"], ["Asthma"])
    (disorders_dir / "Asthma.history.yaml").write_text("event: CREATE\n")
    assert detect_page_content_drift(disorders_dir, pages_dir) == ([], [])


# --- heal planning: repair drift without always paying for a full rebuild ----


def test_pure_staleness_heals_targeted(tmp_path):
    disorders_dir, pages_dir = _make_tree(
        tmp_path,
        ["Asthma", "Sarcoidosis"],
        ["Asthma", "Sarcoidosis"],
        stale=["Sarcoidosis"],
    )
    strategy, files = plan_heal(disorders_dir, pages_dir)
    assert strategy == "targeted"
    assert files == [str(disorders_dir / "Sarcoidosis.yaml")]


def test_healthy_tree_needs_no_heal(tmp_path):
    disorders_dir, pages_dir = _make_tree(tmp_path, ["Asthma"], ["Asthma"])
    assert plan_heal(disorders_dir, pages_dir) == ("targeted", [])


def test_orphan_page_from_rename_forces_full_heal(tmp_path):
    # Re-rendering cannot delete the orphan page; only a full build prunes.
    disorders_dir, pages_dir = _make_tree(tmp_path, ["New_Name"], ["Old_Name"])
    strategy, files = plan_heal(disorders_dir, pages_dir)
    assert strategy == "full"
    assert files == []


def test_count_mismatch_forces_full_heal(tmp_path):
    disorders_dir, pages_dir = _make_tree(
        tmp_path, ["Asthma", "Sarcoidosis"], ["Asthma"]
    )
    assert plan_heal(disorders_dir, pages_dir) == ("full", [])


def test_unstamped_page_heals_targeted(tmp_path):
    # Re-rendering it produces a stamped page, so the cheap repair does work.
    disorders_dir, pages_dir = _make_tree(
        tmp_path, ["Asthma"], ["Asthma"], unstamped=["Asthma"]
    )
    strategy, files = plan_heal(disorders_dir, pages_dir)
    assert strategy == "targeted"
    assert files == [str(disorders_dir / "Asthma.yaml")]


def test_missing_directory_forces_full_heal(tmp_path):
    disorders_dir, pages_dir = _make_tree(tmp_path, ["Asthma"], ["Asthma"])
    assert plan_heal(disorders_dir, tmp_path / "nope") == ("full", [])
    assert plan_heal(tmp_path / "nope", pages_dir) == ("full", [])

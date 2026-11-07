"""Modules resolve the checkout from the working directory, not ``__file__`` (#15109).

``Path(__file__).resolve().parents[N]`` names the tree the package was
installed from. With one virtualenv shared across git worktrees that is the
primary checkout, so a command run in a worktree read and wrote the primary
checkout and reported success (#15051). These tests run converted readers and
writers from a throwaway tree and check they stay in it, and keep new
``__file__``-relative checkout paths out of ``src/dismech/`` and
``src/phenoagent/``.
"""

from __future__ import annotations

import importlib
import json
import logging
import re
import subprocess
import sys
from pathlib import Path

import pytest

from dismech import repo_root as rr

SRC_DIR = Path(rr.__file__).resolve().parent
MODULE_TREE = SRC_DIR.parents[1]
#: Every package under src/ the lint scans. Each may resolve paths inside itself.
LINTED_PACKAGES = (SRC_DIR, SRC_DIR.parent / "phenoagent")


def _make_tree(root: Path) -> Path:
    """A minimal dismech-shaped tree: a justfile and kb/disorders/."""
    (root / "kb" / "disorders").mkdir(parents=True)
    (root / "justfile").write_text("", encoding="utf-8")
    return root.resolve()


@pytest.fixture()
def tree(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    root = _make_tree(tmp_path / "wt")
    monkeypatch.delenv(rr.ENV_VAR, raising=False)
    monkeypatch.chdir(root)
    return root


def test_pathograph_stats_writes_into_the_working_tree(tree: Path):
    from dismech import pathograph_stats

    module_copy = MODULE_TREE / "cache" / "pathograph_stats.json"
    before = module_copy.read_bytes() if module_copy.exists() else None

    assert pathograph_stats.main([]) == 0

    written = tree / "cache" / "pathograph_stats.json"
    assert json.loads(written.read_text())["mean_edge_count"] is None
    after = module_copy.read_bytes() if module_copy.exists() else None
    assert after == before


def test_last_pass_reports_on_the_working_tree(tree: Path):
    from dismech.last_pass import build_report

    entry = tree / "kb" / "disorders" / "Only_Entry.yaml"
    entry.write_text("name: Only Entry\n", encoding="utf-8")
    (tree / "history").mkdir()

    report = build_report()

    assert [t.slug for t in report.targets] == ["Only_Entry"]


def test_render_category_cache_follows_the_working_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    """A memoised reader must not keep serving the first checkout's file."""
    from dismech import render

    monkeypatch.delenv(rr.ENV_VAR, raising=False)
    for name, category in (("one", "Growth"), ("two", "Nervous System")):
        root = _make_tree(tmp_path / name)
        (root / "app").mkdir()
        (root / "app" / "hpo_category_cache.json").write_text(
            json.dumps({"HP:0001250": [category]}), encoding="utf-8"
        )
        monkeypatch.chdir(root)
        assert render._load_hpo_category_cache() == {"HP:0001250": [category]}


@pytest.mark.parametrize(
    ("module", "attribute", "relative"),
    [
        ("dismech.phenotype_distribution", "DEFAULT_CACHE_DIR", "references_cache"),
        (
            "dismech.pathograph_stats",
            "PATHOGRAPH_STATS_PATH",
            "cache/pathograph_stats.json",
        ),
        ("dismech.bookshelf", "DEFAULT_INDEX_DIR", "cache/bookshelf"),
        ("dismech.toxcast_assays", "DEFAULT_DATA_DIR", "data/toxcast"),
        (
            "dismech.export.browser_export",
            "HPO_CATEGORY_CACHE_PATH",
            "app/hpo_category_cache.json",
        ),
        ("dismech.groupings", "GROUPINGS_DIR", "kb/groupings"),
        ("dismech.groupings", "CLOSURE_CACHE_DIR", "cache/closure"),
        ("dismech.render", "MODELS_ROOT", "models"),
        ("dismech.render", "_REFERENCES_CACHE_DIR", "references_cache"),
    ],
)
def test_module_paths_follow_the_working_directory(
    tree: Path, module: str, attribute: str, relative: str
):
    value = getattr(importlib.import_module(module), attribute)
    assert value == tree / relative


def test_monkeypatch_undo_leaves_a_lazy_name_behind_until_cleared(
    tree: Path, tmp_path: Path
):
    """Pins the pytest behaviour behind #15396 and the fix ``conftest`` applies.

    Undoing a ``monkeypatch.setattr`` on a lazily served name writes the value
    read before the patch into the module's ``__dict__``. Without
    ``clear_all_overrides()`` that frozen value would shadow the lazy lookup for
    every later test in the worker.
    """
    from dismech.export import browser_export

    name = "HPO_CATEGORY_CACHE_PATH"
    patch = pytest.MonkeyPatch()
    patch.setattr(browser_export, name, tmp_path / "patched.json")
    patch.undo()
    assert name in vars(browser_export)

    rr.LazyRepoPaths.clear_all_overrides()
    assert name not in vars(browser_export)
    assert browser_export.HPO_CATEGORY_CACHE_PATH == (
        tree / "app" / "hpo_category_cache.json"
    )


def test_no_lazy_name_is_left_on_any_module_when_a_test_starts():
    """The autouse fixture in ``conftest`` clears leftovers before each test."""
    for paths in rr.LazyRepoPaths._instances:
        module = importlib.import_module(paths._module_name)
        leftover = set(paths._factories) & set(vars(module))
        assert not leftover, f"{paths._module_name}: {sorted(leftover)}"


def test_no_module_assigns_a_lazy_name_at_import():
    """A declared name assigned at import would make its factory dead code.

    The autouse fixture pops such an assignment before every test, so this is
    checked in a fresh interpreter that no fixture has touched.
    """
    modules = sorted(
        ".".join(path.relative_to(SRC_DIR.parent).with_suffix("").parts)
        for path in SRC_DIR.rglob("*.py")
        if path.name != "repo_root.py"
        and "LazyRepoPaths(" in path.read_text(encoding="utf-8")
    )
    assert modules, "no module declares LazyRepoPaths"
    script = (
        "import importlib, sys\n"
        "from dismech.repo_root import LazyRepoPaths\n"
        f"for name in {modules!r}:\n"
        "    importlib.import_module(name)\n"
        "for paths in LazyRepoPaths._instances:\n"
        "    module = sys.modules[paths._module_name]\n"
        "    for name in sorted(set(paths._factories) & set(vars(module))):\n"
        "        print(f'{paths._module_name}.{name}')\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.stdout == "", f"assigned at import:\n{result.stdout}"


@pytest.mark.parametrize(
    ("module", "function", "relative"),
    [
        ("dismech.stubs.model", "default_stub_dir", "stubs"),
        ("dismech.hierarchy_cache", "default_cache_root", "cache"),
        ("dismech.genes.slice", "default_kb_root", "kb"),
        ("dismech.compare.support", "default_kb_dir", "kb/disorders"),
    ],
)
def test_default_path_helpers_follow_the_working_directory(
    tree: Path,
    monkeypatch: pytest.MonkeyPatch,
    module: str,
    function: str,
    relative: str,
):
    monkeypatch.delenv("DISMECH_GENES_KB_ROOT", raising=False)
    assert getattr(importlib.import_module(module), function)() == tree / relative


def test_an_assigned_module_path_wins_over_the_working_directory(
    tree: Path, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    from dismech import groupings

    monkeypatch.setattr(groupings, "CLOSURE_CACHE_DIR", tmp_path)
    assert groupings.closure_cache_path("HP") == tmp_path / "hp.csv"


def test_fallback_warning_is_logged_once_per_working_directory(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, caplog: pytest.LogCaptureFixture
):
    monkeypatch.delenv(rr.ENV_VAR, raising=False)
    monkeypatch.chdir(tmp_path)
    rr._warn_fallback.cache_clear()
    with caplog.at_level(logging.WARNING, logger="dismech.repo_root"):
        for _ in range(3):
            assert rr.repo_root() == MODULE_TREE
    assert len([r for r in caplog.records if r.name == "dismech.repo_root"]) == 1


# --------------------------------------------------------------------------- lint

#: ``Path(__file__)`` walked up by ``.parents[N]`` or a ``.parent`` chain.
_FILE_RELATIVE = re.compile(
    r"Path\(__file__\)(?:\.resolve\(\))?"
    r"(?:\.parents\[(?P<index>\d+)\]|(?P<chain>(?:\.parent)+))"
)

#: Files allowed to resolve a path outside the package from ``__file__``, and why.
_ALLOWED_OUTSIDE_PACKAGE = {
    # The documented last resort of repo_root() itself, used only when the
    # working directory is in no checkout and $DISMECH_ROOT is unset.
    "repo_root.py",
}


def _file_relative_targets() -> list[tuple[Path, str, int, Path]]:
    hits = []
    for package in LINTED_PACKAGES:
        for path in sorted(package.rglob("*.py")):
            resolved = path.resolve()
            for lineno, line in enumerate(
                path.read_text(encoding="utf-8").splitlines(), 1
            ):
                for match in _FILE_RELATIVE.finditer(line):
                    if match.group("index") is not None:
                        depth = int(match.group("index"))
                    else:
                        depth = match.group("chain").count(".parent") - 1
                    rel = path.relative_to(package).as_posix()
                    hits.append((package, rel, lineno, resolved.parents[depth]))
    return hits


def test_the_lint_pattern_sees_both_spellings():
    assert _FILE_RELATIVE.search("Path(__file__).resolve().parents[2] / 'kb'")
    assert _FILE_RELATIVE.search("Path(__file__).parent.parent.parent")
    assert _FILE_RELATIVE.search("Path(__file__).parent / 'templates'")


def test_no_module_resolves_the_checkout_from_its_own_file():
    """A ``__file__``-relative path may point inside the package, never above it.

    Package-internal resources (``schema/``, ``templates/``) ship with the
    package, so locating them from ``__file__`` is right. A path that climbs
    out of its package (``src/dismech/``, ``src/phenoagent/``) is reaching for
    the checkout, and must go through ``dismech.repo_root`` instead.
    """
    hits = _file_relative_targets()
    assert hits, "the lint found no __file__-relative paths at all; is it broken?"
    offenders = [
        f"src/{package.name}/{rel}:{lineno} -> {target}"
        for package, rel, lineno, target in hits
        if not target.is_relative_to(package)
        and not (package == SRC_DIR and rel in _ALLOWED_OUTSIDE_PACKAGE)
    ]
    assert not offenders, (
        "These resolve a checkout path from the module's own location, which is "
        "the primary checkout when a virtualenv is shared across worktrees. Use "
        "dismech.repo_root.repo_root() (or LazyRepoPaths for a module-level "
        "constant) instead:\n  " + "\n  ".join(offenders)
    )

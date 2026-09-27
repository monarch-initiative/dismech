"""Tests for the ``Not4Curation`` binding audit (issue #8472).

The audit's only external dependency is an OAK adapter, so every test here
substitutes a fake one. That keeps the suite offline and deterministic while
still exercising the real question: does a term whose *synonym* says "do not
annotate with this" get caught, given that its existence, label and enum
reachability all check out?
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "not4curation_audit.py"
SPEC = importlib.util.spec_from_file_location("not4curation_audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


OAK_CONFIG = """ontology_adapters:
  XCO: sqlite:obo:xco
  HP: ols:hp
  hgnc: sqlite:obo:hgnc
  linkml: ""
"""

# XCO:0000294 is the term that started #8472: real, correctly labelled, reachable
# from the ExposureTerm enum roots -- and flagged by RGD as not for annotation.
FAKE_ONTOLOGY = {
    "XCO:0000294": ("estrogen/estrogen analog", ["Not4Curation", "estrogen analog"]),
    "XCO:0000013": ("controlled sound exposure", ["noise exposure"]),
    "XCO:0000512": ("dietary control", []),
    "HGNC:746": ("APOB", ["apolipoprotein B"]),
}


class FakeAdapter:
    """The two OAK calls the audit makes, over a dict."""

    def __init__(self, terms):
        self.terms = terms

    def entity_aliases(self, curie):
        return list(self.terms.get(str(curie), ("", []))[1])

    def label(self, curie):
        return self.terms.get(str(curie), ("", []))[0]

    def entities(self):
        return list(self.terms)


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """A miniature repo: an OAK config, a KB file slot, and a fake adapter."""
    (tmp_path / "conf").mkdir()
    (tmp_path / "conf" / "oak_config.yaml").write_text(OAK_CONFIG, encoding="utf-8")
    (tmp_path / "kb").mkdir()
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)

    import oaklib

    monkeypatch.setattr(oaklib, "get_adapter", lambda _: FakeAdapter(FAKE_ONTOLOGY))
    return tmp_path


def _entry(tmp_path: Path, curie: str, name: str = "Entry") -> Path:
    path = tmp_path / "kb" / f"{name}.yaml"
    path.write_text(
        "name: Entry\n"
        "environmental:\n"
        "- name: An exposure\n"
        "  exposure_term:\n"
        "    preferred_term: an exposure\n"
        "    term:\n"
        f"      id: {curie}\n"
        "      label: whatever\n",
        encoding="utf-8",
    )
    return path


def _audit(repo: Path, path: Path, **kwargs):
    return audit.audit(
        [path],
        oak_config=repo / "conf" / "oak_config.yaml",
        cache_dir=kwargs.pop("cache_dir", None),
        **kwargs,
    )


# --------------------------------------------------------------------------- #
# marker detection
# --------------------------------------------------------------------------- #


def test_flagged_term_in_use_is_reported(repo):
    report = _audit(repo, _entry(repo, "XCO:0000294"))

    assert [f.curie for f in report.in_use] == ["XCO:0000294"]
    flagged = report.in_use[0]
    assert flagged.label == "estrogen/estrogen analog"
    assert flagged.synonym == "Not4Curation"
    assert flagged.usages[0].location == "environmental[0].exposure_term.term.id"


def test_unflagged_term_passes(repo):
    report = _audit(repo, _entry(repo, "XCO:0000013"))

    assert report.in_use == []
    assert report.checked_prefixes == {"XCO": 1}
    assert report.synonym_hits == {"XCO": 1}


def test_term_without_synonyms_is_not_counted_as_checked(repo):
    """A marker *is* a synonym, so a term with none was not effectively checked."""
    report = _audit(repo, _entry(repo, "XCO:0000512"))

    assert report.checked_prefixes == {"XCO": 1}
    assert report.synonym_hits == {"XCO": 0}


@pytest.mark.parametrize(
    "synonym",
    [
        "Not4Curation",
        "not4curation",
        "NOT 4 CURATION",
        "not_recommended_for_annotation",
    ],
)
def test_marker_matching_ignores_case_and_separators(synonym):
    marker, hit = audit.marker_hit([synonym], audit.DEFAULT_MARKERS)

    assert marker
    assert hit == synonym


def test_ordinary_synonyms_are_not_markers():
    assert audit.marker_hit(
        ["estrogen analog", "curation note"], audit.DEFAULT_MARKERS
    ) == (
        "",
        "",
    )


# --------------------------------------------------------------------------- #
# scope
# --------------------------------------------------------------------------- #


def test_remote_prefixes_are_skipped_and_reported(repo):
    """OLS-served prefixes cost a round trip per term, so they are opt-in."""
    report = _audit(repo, _entry(repo, "HP:0002014"))

    assert "HP" in report.skipped_prefixes
    assert "remote" in report.skipped_prefixes["HP"]
    assert report.checked_prefixes == {}


def test_include_remote_checks_ols_prefixes(repo):
    report = _audit(repo, _entry(repo, "HP:0002014"), include_remote=True)

    assert "HP" not in report.skipped_prefixes
    assert report.checked_prefixes == {"HP": 1}


def test_lowercase_hgnc_is_looked_up_under_the_ontology_casing(repo):
    """The repo writes ``hgnc:746``; the ontology answers to ``HGNC:746``."""
    report = _audit(repo, _entry(repo, "hgnc:746"))

    assert report.checked_prefixes == {"hgnc": 1}
    assert report.synonym_hits == {"hgnc": 1}


def test_prefix_without_an_adapter_is_reported_not_silently_dropped(repo):
    report = _audit(repo, _entry(repo, "XCO:0000294"), prefixes=["XCO", "NOSUCH"])

    assert report.skipped_prefixes["NOSUCH"] == "no adapter in the OAK config"
    assert [f.curie for f in report.in_use] == ["XCO:0000294"]


def test_adapter_failure_is_reported_rather_than_passing_silently(repo, monkeypatch):
    import oaklib

    def boom(_):
        raise RuntimeError("no network")

    monkeypatch.setattr(oaklib, "get_adapter", boom)
    report = _audit(repo, _entry(repo, "XCO:0000294"))

    assert report.in_use == []
    assert "unavailable" in report.skipped_prefixes["XCO"]
    assert "XCO" not in report.checked_prefixes


# --------------------------------------------------------------------------- #
# what counts as a binding
# --------------------------------------------------------------------------- #


def test_curies_quoted_inside_prose_are_not_treated_as_bindings(repo):
    """An evidence snippet may quote a CURIE; only a whole-scalar value is a binding."""
    path = repo / "kb" / "Prose.yaml"
    path.write_text(
        "name: Entry\n"
        "evidence:\n"
        "- reference: PMID:12345678\n"
        '  snippet: "the row reads XCO:0000294 | estrogen/estrogen analog"\n',
        encoding="utf-8",
    )

    report = _audit(repo, path)

    assert report.in_use == []
    assert report.checked_prefixes == {}


# --------------------------------------------------------------------------- #
# the cache half of #8472
# --------------------------------------------------------------------------- #


def test_flagged_cached_curie_is_advisory_not_a_failure(repo):
    """A flagged row in the offline caches is why the gate has to exist at all."""
    cache = repo / "cache"
    (cache / "xco").mkdir(parents=True)
    (cache / "xco" / "terms.csv").write_text(
        "curie,label,retrieved_at\n"
        "XCO:0000294,estrogen/estrogen analog,2026-08-14T11:24:33.957907\n",
        encoding="utf-8",
    )
    (cache / "enums").mkdir()
    (cache / "enums" / "exposureterm_abc.csv").write_text(
        "curie\nXCO:0000294\n", encoding="utf-8"
    )

    report = _audit(repo, _entry(repo, "XCO:0000013"), cache_dir=cache)

    assert report.in_use == []
    assert [f.curie for f in report.cached_only] == ["XCO:0000294"]
    assert report.cached_only[0].cached_in == [
        "cache/xco/terms.csv",
        "cache/enums/exposureterm_abc.csv",
    ]


def test_curie_both_used_and_cached_is_reported_once_as_in_use(repo):
    cache = repo / "cache"
    (cache / "xco").mkdir(parents=True)
    (cache / "xco" / "terms.csv").write_text(
        "curie,label,retrieved_at\n"
        "XCO:0000294,estrogen/estrogen analog,2026-08-14T11:24:33.957907\n",
        encoding="utf-8",
    )

    report = _audit(repo, _entry(repo, "XCO:0000294"), cache_dir=cache)

    assert [f.curie for f in report.in_use] == ["XCO:0000294"]
    assert report.cached_only == []
    assert report.in_use[0].cached_in == ["cache/xco/terms.csv"]


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #


def test_cli_fails_on_a_flagged_binding(repo, capsys):
    path = _entry(repo, "XCO:0000294")

    exit_code = audit.main(
        [
            str(path),
            "--oak-config",
            str(repo / "conf" / "oak_config.yaml"),
            "--no-cache-scan",
        ]
    )

    assert exit_code == 1
    assert "XCO:0000294" in capsys.readouterr().err


def test_cli_warn_only_reports_without_failing(repo, capsys):
    path = _entry(repo, "XCO:0000294")

    exit_code = audit.main(
        [
            str(path),
            "--oak-config",
            str(repo / "conf" / "oak_config.yaml"),
            "--no-cache-scan",
            "--warn-only",
        ]
    )

    assert exit_code == 0
    assert "XCO:0000294" in capsys.readouterr().err


def test_cli_passes_on_a_clean_file(repo, capsys):
    path = _entry(repo, "XCO:0000013")

    exit_code = audit.main(
        [
            str(path),
            "--oak-config",
            str(repo / "conf" / "oak_config.yaml"),
            "--no-cache-scan",
        ]
    )

    assert exit_code == 0
    assert "OK:" in capsys.readouterr().out


def test_cli_reports_an_absolute_glob_that_matches_nothing(repo, capsys):
    """``Path.glob`` rejects an absolute pattern, so this used to raise."""
    exit_code = audit.main(
        [
            "/nonexistent/dir/*.yaml",
            "--oak-config",
            str(repo / "conf" / "oak_config.yaml"),
            "--no-cache-scan",
        ]
    )

    assert exit_code == 2
    assert "no YAML files matched" in capsys.readouterr().err


def test_absolute_glob_that_matches_is_expanded(repo):
    _entry(repo, "XCO:0000013")

    targets = audit.resolve_targets([str(repo / "kb" / "*.yaml")])

    assert [p.name for p in targets] == ["Entry.yaml"]


def test_history_records_are_never_scanned(repo):
    (repo / "kb" / "Entry.history.yaml").write_text("name: x\n", encoding="utf-8")

    assert audit.resolve_targets([str(repo / "kb")]) == []
    # Also when named outright -- these are not entries, however you reach them.
    assert audit.resolve_targets([str(repo / "kb" / "Entry.history.yaml")]) == []


def test_overlapping_arguments_yield_each_file_once(repo, monkeypatch):
    """A relative argument and a repo-root-expanded glob are different objects."""
    _entry(repo, "XCO:0000294")
    monkeypatch.chdir(repo)

    targets = audit.resolve_targets(["kb/Entry.yaml", "kb/*.yaml", str(repo / "kb")])

    assert len(targets) == 1


def test_duplicate_arguments_do_not_duplicate_usage_lines(repo):
    path = _entry(repo, "XCO:0000294")

    report = audit.audit(
        audit.resolve_targets([str(path), str(repo / "kb" / "*.yaml")]),
        oak_config=repo / "conf" / "oak_config.yaml",
        cache_dir=None,
    )

    assert len(report.in_use[0].usages) == 1


def test_default_targets_cover_every_kb_subtree_at_any_depth():
    """A kb/ subtree added later must not silently fall out of scope.

    Recursive matters: ``kb/hypotheses/`` nests three levels deep, so a
    ``kb/*/*.yaml`` pattern would miss it entirely.
    """
    assert "kb/**/*.yaml" in audit.DEFAULT_TARGETS


def test_directory_arguments_are_scanned_recursively(repo):
    nested = repo / "kb" / "hypotheses" / "Disease" / "model"
    nested.mkdir(parents=True)
    (nested / "assessment.yaml").write_text(
        "term:\n  id: XCO:0000294\n", encoding="utf-8"
    )

    report = audit.audit(
        audit.resolve_targets([str(repo / "kb")]),
        oak_config=repo / "conf" / "oak_config.yaml",
        cache_dir=None,
    )

    assert [f.curie for f in report.in_use] == ["XCO:0000294"]
    assert (
        report.in_use[0]
        .usages[0]
        .path.endswith("kb/hypotheses/Disease/model/assessment.yaml")
    )


# --------------------------------------------------------------------------- #
# inventory, extra markers, and output formats
# --------------------------------------------------------------------------- #


def test_list_flagged_reports_the_whole_deny_list_not_just_what_is_used(repo):
    report = _audit(
        repo, _entry(repo, "XCO:0000013"), prefixes=["XCO"], list_flagged=True
    )

    assert report.in_use == []
    assert [f.curie for f in report.inventory] == ["XCO:0000294"]
    assert report.inventory[0].label == "estrogen/estrogen analog"


def test_an_extra_marker_can_be_supplied(repo):
    report = _audit(
        repo,
        _entry(repo, "XCO:0000013"),
        markers=("locallyretired",),
    )

    assert report.in_use == []

    report = _audit(
        repo,
        _entry(repo, "XCO:0000013"),
        markers=("noiseexposure",),
    )

    assert [f.curie for f in report.in_use] == ["XCO:0000013"]


def test_cli_marker_flag_is_normalized_like_a_synonym(repo, capsys):
    """``--marker`` takes prose; it is folded the same way a synonym is."""
    path = _entry(repo, "XCO:0000013")

    exit_code = audit.main(
        [
            str(path),
            "--oak-config",
            str(repo / "conf" / "oak_config.yaml"),
            "--no-cache-scan",
            "--marker",
            "Noise Exposure",
        ]
    )

    assert exit_code == 1
    assert "XCO:0000013" in capsys.readouterr().err


def test_cli_json_output_is_machine_readable(repo, capsys):
    import json

    path = _entry(repo, "XCO:0000294")

    exit_code = audit.main(
        [
            str(path),
            "--oak-config",
            str(repo / "conf" / "oak_config.yaml"),
            "--no-cache-scan",
            "--format",
            "json",
        ]
    )
    payload = json.loads(capsys.readouterr().out)

    assert exit_code == 1
    assert [i["curie"] for i in payload["in_use"]] == ["XCO:0000294"]
    assert payload["checked_prefixes"] == {"XCO": 1}
    assert payload["synonym_hits"] == {"XCO": 1}
    assert payload["unavailable_prefixes"] == {}


def test_cli_tsv_output_has_one_row_per_usage(repo, capsys):
    path = _entry(repo, "XCO:0000294")

    audit.main(
        [
            str(path),
            "--oak-config",
            str(repo / "conf" / "oak_config.yaml"),
            "--no-cache-scan",
            "--format",
            "tsv",
        ]
    )
    rows = [line.split("\t") for line in capsys.readouterr().out.strip().splitlines()]

    assert rows[0] == ["state", "curie", "label", "marker_synonym", "location"]
    assert len(rows) == 2
    assert rows[1][:2] == ["IN_USE", "XCO:0000294"]


def test_unavailable_prefixes_are_recorded_structurally(repo, monkeypatch):
    """``--require-adapters`` must not depend on the wording of a reason string."""
    import oaklib

    def boom(_):
        raise RuntimeError("no network")

    monkeypatch.setattr(oaklib, "get_adapter", boom)
    report = _audit(repo, _entry(repo, "XCO:0000294"))

    assert set(report.unavailable_prefixes) == {"XCO"}
    assert set(report.skipped_prefixes) >= {"XCO", "HP"}
    # Out-of-scope by choice is not the same as could-not-be-checked.
    assert "HP" not in report.unavailable_prefixes


def test_cli_require_adapters_gates_a_degraded_run(repo, monkeypatch, capsys):
    import oaklib

    def boom(_):
        raise RuntimeError("no network")

    monkeypatch.setattr(oaklib, "get_adapter", boom)
    path = _entry(repo, "XCO:0000294")

    exit_code = audit.main(
        [
            str(path),
            "--oak-config",
            str(repo / "conf" / "oak_config.yaml"),
            "--no-cache-scan",
            "--require-adapters",
        ]
    )

    assert exit_code == 2
    assert "could not verify" in capsys.readouterr().err

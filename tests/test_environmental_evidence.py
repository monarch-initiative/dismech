"""Guard test: no NEW evidence-free `environmental:` exposures in kb/disorders/.

An `Environmental` entry with no `evidence:` block is an uncited causation
claim that every current validator (`just validate`, `validate-terms`,
`count-verified-snippets`) is structurally blind to, since `evidence` is
optional on the class. A baseline grandfathers the pre-existing backlog so
this test fails only on newly introduced ones.

See scripts/check_environmental_evidence.py and dismech issue #8296.
"""

import subprocess
from collections import Counter
from pathlib import Path

from scripts import check_environmental_evidence as cee
from scripts.check_environmental_evidence import (
    BASELINE_REF_ENV,
    _baseline_key,
    baseline_from_ref,
    find_violations,
    load_baseline,
    new_findings,
    resolve_baseline,
    scan_repo,
    write_baseline,
)

ROOT = Path(__file__).resolve().parents[1]


def _entry(name: str | None = "Smoking", evidence=None) -> dict:
    entry = {}
    if name is not None:
        entry["name"] = name
    if evidence is not None:
        entry["evidence"] = evidence
    return entry


def test_no_new_evidence_free_environmental_exposures():
    # resolve_baseline() grandfathers against origin/main when CI sets
    # ENVIRONMENTAL_EVIDENCE_BASELINE_REF (so the base branch is green by
    # construction and parallel merges cannot clobber the grandfather set),
    # and falls back to the committed baseline for local runs / shallow
    # checkouts.
    baseline = resolve_baseline()
    new = [
        f"{rel}:{location}: {name!r}"
        for rel, location, name in new_findings(scan_repo(), baseline)
    ]
    assert not new, (
        "New evidence-free `environmental:` exposure(s) detected. Every "
        "environmental entry is an uncited causation claim until it carries "
        "an `evidence:` block. Add a citable PMID/DOI with a verified "
        "snippet, or record provenance in `notes` if no citable source "
        "exists:\n  " + "\n  ".join(new)
    )


def test_flags_an_entry_with_no_evidence_key():
    findings = list(find_violations({"environmental": [_entry("Smoking")]}))
    assert findings == [("environmental[0]", "Smoking")]


def test_flags_an_entry_with_empty_evidence_list():
    findings = list(
        find_violations({"environmental": [_entry("Smoking", evidence=[])]})
    )
    assert findings == [("environmental[0]", "Smoking")]


def test_flags_an_entry_with_null_evidence():
    findings = list(
        find_violations({"environmental": [_entry("Smoking", evidence=None)]})
    )
    assert findings == [("environmental[0]", "Smoking")]


def test_accepts_an_entry_with_evidence():
    entry = _entry(
        "Smoking",
        evidence=[{"reference": "PMID:1", "snippet": "Smoking is a risk factor."}],
    )
    assert not list(find_violations({"environmental": [entry]}))


def test_flags_an_entry_whose_only_evidence_item_has_an_empty_snippet():
    # dismech#8550: `if entry.get("evidence")` only checked block presence, so
    # an evidence item that cites a real PMID but quotes nothing (snippet: '')
    # was silently treated as "cited". A block whose items are all
    # empty-snippet must still count as evidence-free.
    entry = _entry(
        "Smoking",
        evidence=[{"reference": "PMID:1", "supports": "SUPPORT", "snippet": ""}],
    )
    findings = list(find_violations({"environmental": [entry]}))
    assert findings == [("environmental[0]", "Smoking")]


def test_accepts_an_entry_with_one_quoted_item_among_empty_ones():
    entry = _entry(
        "Smoking",
        evidence=[
            {"reference": "PMID:1", "supports": "NO_EVIDENCE", "snippet": ""},
            {"reference": "PMID:2", "supports": "SUPPORT", "snippet": "Real quote."},
        ],
    )
    assert not list(find_violations({"environmental": [entry]}))


def test_missing_environmental_key_yields_no_findings():
    assert not list(find_violations({}))


def test_unnamed_entry_gets_a_placeholder_name():
    findings = list(find_violations({"environmental": [{"notes": "no name"}]}))
    assert findings == [("environmental[0]", "<unnamed>")]


def test_non_dict_entries_are_skipped():
    # Malformed YAML (not this check's job to gate) should not crash the scan.
    assert not list(find_violations({"environmental": ["not-a-dict"]}))


def test_scan_dir_is_the_kb_root_not_just_disorders():
    # Pins the module-level constant. The behavioural test below passes
    # scan_dir= explicitly, so on its own it would stay green if SCAN_DIR were
    # narrowed back to kb/disorders -- this is the assertion that actually
    # fails in that case.
    assert cee.SCAN_DIR == cee.ROOT / "kb"


def test_scan_covers_kb_beyond_disorders(tmp_path):
    # SCAN_DIR is kb/, not kb/disorders/. kb/modules/ and kb/comorbidities/
    # validate against the same `Disease` class, so an evidence-free
    # `environmental:` entry there is the same uncited causation claim and must
    # be found. This is a no-op on current content (nothing outside
    # kb/disorders/ carries `environmental:` today), so without this test
    # narrowing SCAN_DIR back would leave all other tests green and silently
    # restore the blind spot.
    for sub in ("modules", "comorbidities"):
        target = tmp_path / "kb" / sub
        target.mkdir(parents=True)
        (target / "X.yaml").write_text(
            "environmental:\n- name: Smoking\n  notes: uncited\n", encoding="utf-8"
        )
    findings = scan_repo(scan_dir=tmp_path / "kb", rel_to=tmp_path)
    assert sorted(rel for rel, _, _ in findings) == [
        "kb/comorbidities/X.yaml",
        "kb/modules/X.yaml",
    ]


def test_baseline_key_is_location_independent():
    # Locations shift whenever the environmental list above them grows; the
    # key must not.
    assert _baseline_key("kb/x.yaml", "Smoking") == _baseline_key(
        "kb/x.yaml", "Smoking"
    )


def test_baseline_does_not_grandfather_an_unrelated_exposure(tmp_path):
    baseline_path = tmp_path / "baseline.txt"
    write_baseline([("kb/disorders/X.yaml", "environmental[0]", "Smoking")], baseline_path)
    baseline = load_baseline(baseline_path)
    assert new_findings(
        [("kb/disorders/X.yaml", "environmental[1]", "Obesity")], baseline
    )
    # Same exposure name, different file: still a new finding.
    assert new_findings(
        [("kb/disorders/Y.yaml", "environmental[0]", "Smoking")], baseline
    )


def test_extra_reuse_of_a_baselined_exposure_is_a_new_finding(tmp_path):
    """Two grandfathered evidence-free 'Smoking' entries in one file stay quiet;
    a third does not."""
    known = [
        ("kb/disorders/X.yaml", "environmental[0]", "Smoking"),
        ("kb/disorders/X.yaml", "environmental[1]", "Smoking"),
    ]
    baseline_path = tmp_path / "baseline.txt"
    write_baseline(known, baseline_path)
    baseline = load_baseline(baseline_path)

    assert not new_findings(known, baseline)

    reused = [*known, ("kb/disorders/X.yaml", "environmental[2]", "Smoking")]
    extra = new_findings(reused, baseline)
    assert len(extra) == 1
    assert extra[0][1] == "environmental[2]"


def test_baseline_records_occurrence_counts(tmp_path):
    baseline_path = tmp_path / "baseline.txt"
    write_baseline(
        [
            ("kb/disorders/X.yaml", "environmental[0]", "Smoking"),
            ("kb/disorders/X.yaml", "environmental[1]", "Smoking"),
            ("kb/disorders/Y.yaml", "environmental[0]", "Obesity"),
        ],
        baseline_path,
    )
    baseline = load_baseline(baseline_path)

    assert baseline[_baseline_key("kb/disorders/X.yaml", "Smoking")] == 2
    assert baseline[_baseline_key("kb/disorders/Y.yaml", "Obesity")] == 1
    assert "count<TAB>path<TAB>name" in baseline_path.read_text()


def test_baseline_tolerates_the_pre_count_line_format(tmp_path):
    """An older `path<TAB>name` baseline still grandfathers its entries."""
    baseline_path = tmp_path / "baseline.txt"
    baseline_path.write_text(
        "# legacy header\nkb/disorders/X.yaml\tSmoking\n", encoding="utf-8"
    )
    baseline = load_baseline(baseline_path)

    assert not new_findings(
        [("kb/disorders/X.yaml", "environmental[0]", "Smoking")], baseline
    )


# --- ref-derived grandfather baseline (baseline_from_ref / resolve_baseline) ---


def _init_git_repo(path: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=path, check=True)


def test_baseline_from_ref_reads_kb_disorders_at_the_ref(tmp_path):
    disorders = tmp_path / "kb" / "disorders"
    disorders.mkdir(parents=True)
    (disorders / "X.yaml").write_text(
        "name: T\nenvironmental:\n- name: Smoking\n  notes: no evidence\n",
        encoding="utf-8",
    )
    _init_git_repo(tmp_path)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=tmp_path, check=True)

    counts = baseline_from_ref("HEAD", root=tmp_path)
    assert counts is not None
    assert counts[_baseline_key("kb/disorders/X.yaml", "Smoking")] == 1


def test_baseline_from_ref_returns_none_for_an_unknown_ref(tmp_path):
    _init_git_repo(tmp_path)
    assert baseline_from_ref("no-such-ref-deadbeef", root=tmp_path) is None


def test_resolve_baseline_prefers_the_explicit_ref_over_env_and_committed_file(monkeypatch):
    seen = {}
    sentinel = Counter({"kb/x.yaml\tfoo": 3})

    def fake(ref, **kw):
        seen["ref"] = ref
        return sentinel

    monkeypatch.setattr(cee, "baseline_from_ref", fake)
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline("origin/explicit") is sentinel
    assert seen["ref"] == "origin/explicit"


def test_resolve_baseline_reads_the_env_var(monkeypatch):
    seen = {}
    sentinel = Counter({"k": 1})

    def fake(ref, **kw):
        seen["ref"] = ref
        return sentinel

    monkeypatch.setattr(cee, "baseline_from_ref", fake)
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline() is sentinel
    assert seen["ref"] == "origin/from-env"


def test_resolve_baseline_falls_back_when_the_ref_is_unreadable(monkeypatch):
    monkeypatch.setattr(cee, "baseline_from_ref", lambda ref, **kw: None)
    monkeypatch.delenv(BASELINE_REF_ENV, raising=False)
    assert resolve_baseline("bad-ref") == load_baseline()

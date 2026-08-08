"""Guard test: no NEW degenerate (too-short) evidence snippets in kb/.

An evidence snippet of a word or two ('Strabismus') carries no propositional
content -- it cannot support or refute the claim it is attached to, and it is
usually lifted from a clinical-features table whose cells never survive text
extraction, so it is unverifiable by construction. A baseline grandfathers the
pre-existing backlog so this test fails only on newly introduced ones.

See scripts/check_snippet_length.py and dismech issue #7450.
"""

import subprocess
from collections import Counter
from pathlib import Path

import pytest

from scripts import check_snippet_length as csl
from scripts.check_snippet_length import (
    BASELINE_REF_ENV,
    MIN_SNIPPET_WORDS,
    _baseline_key,
    baseline_from_ref,
    count_words,
    find_violations,
    is_structured_row,
    load_baseline,
    new_findings,
    resolve_baseline,
    scan_repo,
    write_baseline,
)

ROOT = Path(__file__).resolve().parents[1]

EXCERPT_FIELDS = frozenset({"snippet"})
REFERENCE_FIELDS = frozenset({"reference"})


def _violations(data):
    return list(
        find_violations(Path("test.yaml"), data, EXCERPT_FIELDS, REFERENCE_FIELDS)
    )


def _entry(snippet: str, reference: str = "PMID:1") -> dict:
    return {"evidence": [{"reference": reference, "snippet": snippet}]}


def test_no_new_short_snippets():
    # resolve_baseline() grandfathers against origin/main when CI sets
    # SNIPPET_BASELINE_REF (so the base branch is green by construction and
    # parallel merges cannot clobber the grandfather set), and falls back to
    # the committed baseline for local runs / shallow checkouts.
    baseline = resolve_baseline()
    new = [
        f"{rel}:{location}: {words} word(s): {snippet!r}"
        for rel, location, words, snippet in new_findings(scan_repo(), baseline)
    ]
    assert not new, (
        "New evidence snippet(s) under "
        f"{MIN_SNIPPET_WORDS} words detected. A snippet should be the sentence "
        "from the source that makes the claim, not a bare term. Quote the "
        "sentence, or drop the evidence block and keep the description:\n  "
        + "\n  ".join(new)
    )


def test_flags_bare_term_snippet():
    findings = _violations(_entry("Strabismus"))
    assert findings, "a one-word snippet should be flagged"
    assert findings[0][1] == 1


def test_accepts_a_full_sentence():
    sentence = (
        "Affected individuals show agenesis of the corpus callosum and cataracts."
    )
    assert not _violations(_entry(sentence))


def test_structured_source_table_row_is_exempt():
    # Short in words, but a fully propositional row quoted from an ORPHA cache.
    row = "HP:0001987 | Hyperammonemia | Very frequent (99-80%)"
    assert is_structured_row(row)
    assert not _violations(_entry(row, reference="ORPHA:558"))


def test_pipeless_short_snippet_is_not_exempt():
    assert not is_structured_row("Hearing loss")
    assert _violations(_entry("Hearing loss"))


@pytest.mark.parametrize(
    ("snippet", "expected"),
    [
        ("Strabismus", 1),
        ("Hearing loss", 2),
        ("High-arched palate", 2),
        # Bare punctuation ('>') is not a word; 'c.142G' and 'MAP3K7' each are.
        ("c.142G > A in MAP3K7", 4),
        ("   spaced   out   words  ", 3),
        ("--- ...", 0),
    ],
)
def test_word_counting(snippet, expected):
    assert count_words(snippet) == expected


def test_snippet_without_a_reference_is_ignored():
    # A snippet only counts as evidence when it sits beside a reference.
    assert not _violations({"notes": [{"snippet": "Strabismus"}]})


def test_baseline_roundtrips_a_snippet_containing_a_newline(tmp_path):
    # The baseline file is line-oriented; a snippet carrying an embedded newline
    # must still match itself after a write/read cycle.
    findings = [
        (
            "kb/disorders/X.yaml",
            "phenotypes[0]",
            4,
            "complete female\nexternal genitalia",
        )
    ]
    baseline_path = tmp_path / "baseline.txt"
    write_baseline(findings, baseline_path)
    assert not new_findings(findings, load_baseline(baseline_path))


def test_baseline_does_not_grandfather_an_unrelated_snippet(tmp_path):
    baseline_path = tmp_path / "baseline.txt"
    write_baseline([("kb/disorders/X.yaml", "p[0]", 1, "Strabismus")], baseline_path)
    baseline = load_baseline(baseline_path)
    assert new_findings([("kb/disorders/X.yaml", "p[1]", 1, "Hypotonia")], baseline)
    # Same snippet, different file: still a new finding.
    assert new_findings([("kb/disorders/Y.yaml", "p[0]", 1, "Strabismus")], baseline)


def test_baseline_key_is_location_independent():
    # Locations shift whenever a list above them grows; the key must not.
    assert _baseline_key("kb/x.yaml", "Strabismus") == _baseline_key(
        "kb/x.yaml", "Strabismus"
    )


def test_extra_reuse_of_a_baselined_snippet_is_a_new_finding(tmp_path):
    """The motivating anti-pattern: one bare term cited for several claims.

    A set-of-keys baseline would wave the fourth paste of an already-known
    snippet straight through, which is exactly what this check exists to catch.
    """
    known = [
        ("kb/disorders/X.yaml", "phenotypes[0]", 2, "Hearing loss"),
        ("kb/disorders/X.yaml", "treatments[0]", 2, "Hearing loss"),
    ]
    baseline_path = tmp_path / "baseline.txt"
    write_baseline(known, baseline_path)
    baseline = load_baseline(baseline_path)

    # The two grandfathered uses stay quiet.
    assert not new_findings(known, baseline)

    # A third use of the same snippet in the same file does not.
    reused = [*known, ("kb/disorders/X.yaml", "treatments[1]", 2, "Hearing loss")]
    extra = new_findings(reused, baseline)
    assert len(extra) == 1
    assert extra[0][1] == "treatments[1]"


def test_baseline_records_occurrence_counts(tmp_path):
    baseline_path = tmp_path / "baseline.txt"
    write_baseline(
        [
            ("kb/disorders/X.yaml", "a", 1, "Strabismus"),
            ("kb/disorders/X.yaml", "b", 1, "Strabismus"),
            ("kb/disorders/Y.yaml", "c", 1, "Hypotonia"),
        ],
        baseline_path,
    )
    baseline = load_baseline(baseline_path)

    assert baseline[_baseline_key("kb/disorders/X.yaml", "Strabismus")] == 2
    assert baseline[_baseline_key("kb/disorders/Y.yaml", "Hypotonia")] == 1
    assert "count<TAB>path<TAB>snippet" in baseline_path.read_text()


def test_baseline_tolerates_the_pre_count_line_format(tmp_path):
    """An older `path<TAB>snippet` baseline still grandfathers its entries."""
    baseline_path = tmp_path / "baseline.txt"
    baseline_path.write_text(
        "# legacy header\nkb/disorders/X.yaml\tStrabismus\n", encoding="utf-8"
    )
    baseline = load_baseline(baseline_path)

    assert not new_findings(
        [("kb/disorders/X.yaml", "p[0]", 1, "Strabismus")], baseline
    )


# --- ref-derived grandfather baseline (baseline_from_ref / resolve_baseline) ---


def _init_git_repo(path: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=path, check=True)


def test_baseline_from_ref_reads_kb_at_the_ref(tmp_path):
    # A throwaway repo with one kb/ entry: baseline_from_ref should git-archive
    # kb/ at the ref, scan it, and key the finding relative to kb/ (via rel_to)
    # exactly as the working-tree scan does -- if that remap regresses, every
    # key mismatches and the whole backlog reads as "new".
    disorders = tmp_path / "kb" / "disorders"
    disorders.mkdir(parents=True)
    (disorders / "X.yaml").write_text(
        "name: T\n"
        "phenotypes:\n"
        "- name: X\n"
        "  evidence:\n"
        "  - reference: PMID:1\n"
        "    snippet: Strabismus\n",
        encoding="utf-8",
    )
    _init_git_repo(tmp_path)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=tmp_path, check=True)

    counts = baseline_from_ref("HEAD", root=tmp_path)
    assert counts is not None
    assert counts[_baseline_key("kb/disorders/X.yaml", "Strabismus")] == 1


def test_baseline_from_ref_returns_none_for_an_unknown_ref(tmp_path):
    _init_git_repo(tmp_path)
    assert baseline_from_ref("no-such-ref-deadbeef", root=tmp_path) is None


def test_resolve_baseline_prefers_the_explicit_ref_over_env_and_committed_file(monkeypatch):
    seen = {}
    sentinel = Counter({"kb/x.yaml\tfoo": 3})

    def fake(ref, **kw):
        seen["ref"] = ref
        return sentinel

    monkeypatch.setattr(csl, "baseline_from_ref", fake)
    # An explicit argument must win over the env var (opposite direction from
    # test_resolve_baseline_reads_the_env_var) and the *right* ref must be used.
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline("origin/explicit") is sentinel
    assert seen["ref"] == "origin/explicit"


def test_resolve_baseline_reads_the_env_var(monkeypatch):
    seen = {}
    sentinel = Counter({"k": 1})

    def fake(ref, **kw):
        seen["ref"] = ref
        return sentinel

    monkeypatch.setattr(csl, "baseline_from_ref", fake)
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline() is sentinel
    assert seen["ref"] == "origin/from-env"


def test_resolve_baseline_falls_back_when_the_ref_is_unreadable(monkeypatch):
    monkeypatch.setattr(csl, "baseline_from_ref", lambda ref, **kw: None)
    monkeypatch.delenv(BASELINE_REF_ENV, raising=False)
    # Unreadable ref -> the committed baseline, identical to a no-ref call.
    assert resolve_baseline("bad-ref") == load_baseline()

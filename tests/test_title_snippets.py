"""Guard test: no NEW title-quoting evidence snippets in kb/.

An evidence snippet that repeats the cited paper's title records *that a
question was examined, not what was found* -- and it passes every other check we
have, because the text is genuine, attributed and over the word minimum. A
baseline grandfathers the pre-existing backlog so this fails only on newly
introduced ones.

See scripts/check_title_snippets.py and dismech issue #8374.
"""

import subprocess
from collections import Counter
from pathlib import Path

import pytest

from scripts import check_title_snippets as cts
from scripts.check_title_snippets import (
    BASELINE_REF_ENV,
    _baseline_key,
    baseline_from_ref,
    classify,
    find_violations,
    load_baseline,
    new_findings,
    normalize,
    resolve_baseline,
    scan_repo,
    title_of,
    write_baseline,
)

ROOT = Path(__file__).resolve().parents[1]

EXCERPT_FIELDS = frozenset({"snippet"})
REFERENCE_FIELDS = frozenset({"reference"})

TITLE = "Risk factors for multiple sclerosis: decreased vitamin D level."


def _cache(tmp_path: Path, reference_id: str, title: str, body: str = "abstract text") -> Path:
    """A minimal reference cache file with frontmatter, as the fetcher writes it."""
    # `/` is legal in a DOI but not in a filename; the real cache sanitises too.
    path = tmp_path / f"{reference_id.replace(':', '_').replace('/', '_')}.md"
    path.write_text(
        f'---\nreference_id: "{reference_id}"\ntitle: "{title}"\n'
        f"content_type: abstract_only\n---\n\n## Content\n{body}\n",
        encoding="utf-8",
    )
    return path


class _Index:
    """Stand-in for CachedReferenceIndex over a dict of id -> path."""

    def __init__(self, mapping):
        self._mapping = mapping

    def resolve_cache_path(self, reference_id):
        return self._mapping.get(reference_id)


def _violations(data, index):
    return list(
        find_violations(
            Path("test.yaml"), data, EXCERPT_FIELDS, REFERENCE_FIELDS, index
        )
    )


# --- the repository gate -----------------------------------------------------


@pytest.fixture(scope="module")
def repo_findings():
    """One scan of kb/ shared by both repository-wide assertions.

    Scanning 110k snippet pairs and resolving each against references_cache/
    costs ~45s, and the two checks below differ only in what they compare the
    result against -- running it twice doubled the cost of this file for
    nothing. CI additionally runs the script itself, so the CLI path is
    exercised there rather than by paying for a third scan here.
    """
    return scan_repo()


def test_no_new_title_snippets(repo_findings):
    """The gate itself: nothing outside the grandfathered backlog."""
    new = new_findings(repo_findings, resolve_baseline())
    assert not new, "\n".join(
        f"{rel}:{location}: {kind}: {snippet!r}" for rel, location, kind, snippet in new[:10]
    )


# --- what counts as quoting the title ----------------------------------------


def test_flags_a_snippet_that_is_the_title(tmp_path):
    index = _Index({"PMID:1": _cache(tmp_path, "PMID:1", TITLE)})
    data = {"evidence": [{"reference": "PMID:1", "snippet": TITLE}]}
    (location, kind, _snippet), = _violations(data, index)
    assert kind == "title"
    assert location.endswith("snippet")


def test_flags_a_snippet_that_is_a_fragment_of_the_title(tmp_path):
    index = _Index({"PMID:1": _cache(tmp_path, "PMID:1", TITLE)})
    data = {"evidence": [{"reference": "PMID:1", "snippet": "decreased vitamin D level"}]}
    (_location, kind, _snippet), = _violations(data, index)
    assert kind == "fragment"


def test_accepts_a_sentence_from_the_abstract(tmp_path):
    """The quoting this check exists to encourage."""
    index = _Index({"PMID:1": _cache(tmp_path, "PMID:1", TITLE)})
    data = {
        "evidence": [
            {
                "reference": "PMID:1",
                "snippet": (
                    "Serum 25-hydroxyvitamin D was 15 nmol/l lower in cases than "
                    "in matched controls five years before onset."
                ),
            }
        ]
    }
    assert _violations(data, index) == []


def test_a_sentence_that_merely_restates_the_title_is_not_flagged(tmp_path):
    """Near-matches are deliberately out of scope -- they are usually the
    abstract's own conclusion sentence, which is exactly what we want quoted."""
    index = _Index(
        {"PMID:1": _cache(tmp_path, "PMID:1", "Expression of ROS1 predicts ROS1 gene rearrangement.")}
    )
    data = {
        "evidence": [
            {
                "reference": "PMID:1",
                "snippet": "Expression of ROS1 correlates with ROS1 gene rearrangement.",
            }
        ]
    }
    assert _violations(data, index) == []


@pytest.mark.parametrize(
    "snippet",
    [
        TITLE.upper(),
        TITLE.rstrip("."),
        f'  "{TITLE}"  ',
        TITLE.replace(" ", "\n  "),
    ],
)
def test_matching_survives_case_quotes_punctuation_and_wrapping(tmp_path, snippet):
    """A curator's transcription varies in ways that do not change the claim."""
    index = _Index({"PMID:1": _cache(tmp_path, "PMID:1", TITLE)})
    data = {"evidence": [{"reference": "PMID:1", "snippet": snippet}]}
    assert len(_violations(data, index)) == 1


def test_fragment_matching_respects_word_boundaries(tmp_path):
    """'cell' must not match inside 'sclerosis' -- or any other longer word."""
    index = _Index({"PMID:1": _cache(tmp_path, "PMID:1", "Risk factors for sclerosis")})
    data = {"evidence": [{"reference": "PMID:1", "snippet": "sclero"}]}
    assert _violations(data, index) == []


def test_structured_source_row_is_exempt(tmp_path):
    """A ClinGen/ORPHA row resembles its record's title but is a data row."""
    title = "ACADSB / 2-methylbutyryl-CoA dehydrogenase deficiency (Definitive)"
    index = _Index({"CGGV:1": _cache(tmp_path, "CGGV:1", title)})
    data = {
        "evidence": [
            {
                "reference": "CGGV:1",
                "snippet": "ACADSB | HGNC:91 | 2-methylbutyryl-CoA dehydrogenase deficiency | Definitive",
            }
        ]
    }
    assert _violations(data, index) == []


def test_dataset_accession_is_exempt(tmp_path):
    """A dataset record's cached body is often its title verbatim, so the
    remedy this guard advises -- quote the abstract sentence -- cannot be done."""
    index = _Index({"GEO:GSE1": _cache(tmp_path, "GEO:GSE1", TITLE)})
    data = {"evidence": [{"reference": "GEO:GSE1", "snippet": TITLE}]}
    assert _violations(data, index) == []


def test_doi_is_still_checked(tmp_path):
    """DOI is in the validator's skip_prefixes because it cannot be *fetched*,
    not because it is not literature -- a DOI record is a real paper."""
    index = _Index({"DOI:10.1/x": _cache(tmp_path, "DOI:10.1/x", TITLE)})
    data = {"evidence": [{"reference": "DOI:10.1/x", "snippet": TITLE}]}
    assert len(_violations(data, index)) == 1


def test_dataset_prefixes_come_from_the_validator_config():
    prefixes = cts.dataset_prefixes()
    assert "geo" in prefixes and "morphic" in prefixes
    assert "doi" not in prefixes, "a DOI names a paper; its title must stay checked"


def test_doi_stays_checked_however_the_config_spells_it(tmp_path):
    """The config lists prefixes in both cases; a lowercase `doi` must not
    silently exempt the one prefix the carve-out exists to protect."""
    config = tmp_path / "reference_validator_config.yaml"
    config.write_text(
        "skip_prefixes:\n  - GEO\n  - geo\n  - DOI\n  - doi\n", encoding="utf-8"
    )
    prefixes = cts.dataset_prefixes(config)
    assert "geo" in prefixes
    assert "doi" not in prefixes


def test_literature_prefixes_are_folded_at_construction():
    """The set is compared against case-folded config values, so it must hold
    only folded entries however a future entry is spelled."""
    assert cts._LITERATURE_PREFIXES == {p.casefold() for p in cts._LITERATURE_PREFIXES}


def test_dataset_prefixes_survives_a_missing_config(tmp_path):
    assert cts.dataset_prefixes(tmp_path / "absent.yaml") == frozenset()


def test_folded_scalar_title_is_a_miss_not_a_false_positive(tmp_path):
    """`title: >-` captures the fold marker, which normalises away. A miss is
    the safe direction, and no cache file is in that shape today."""
    path = tmp_path / "PMID_4.md"
    path.write_text(
        '---\nreference_id: "PMID:4"\ntitle: >-\n  A wrapped title\n---\n\n## Content\nbody\n',
        encoding="utf-8",
    )
    assert classify("A wrapped title", title_of(path) or "") is None


def test_uncached_reference_is_skipped(tmp_path):
    index = _Index({})
    data = {"evidence": [{"reference": "PMID:404", "snippet": TITLE}]}
    assert _violations(data, index) == []


def test_cache_without_a_title_is_skipped(tmp_path):
    path = tmp_path / "PMID_2.md"
    path.write_text('---\nreference_id: "PMID:2"\n---\n\n## Content\nbody\n', encoding="utf-8")
    index = _Index({"PMID:2": path})
    data = {"evidence": [{"reference": "PMID:2", "snippet": "anything at all here"}]}
    assert _violations(data, index) == []


def test_title_is_read_only_from_frontmatter(tmp_path):
    """A `title:` line inside the abstract body must not be mistaken for it."""
    path = tmp_path / "PMID_3.md"
    path.write_text(
        '---\nreference_id: "PMID:3"\ntitle: "Real frontmatter title"\n---\n\n'
        "## Content\ntitle: A decoy line in the body\n",
        encoding="utf-8",
    )
    assert title_of(path) == "Real frontmatter title"


def test_snippet_without_a_reference_is_ignored(tmp_path):
    index = _Index({"PMID:1": _cache(tmp_path, "PMID:1", TITLE)})
    assert _violations({"evidence": [{"snippet": TITLE}]}, index) == []


def test_classify_returns_none_for_empty_input():
    assert classify("", "a title") is None
    assert classify("a snippet", "") is None
    # Punctuation-only normalises away to nothing, and must not match everything.
    assert classify("---", "a title") is None


def test_normalize_folds_the_things_that_vary():
    assert normalize('  "A Title: with punctuation."  ') == "a title with punctuation"


# --- baseline ratchet --------------------------------------------------------


def test_baseline_key_is_location_independent():
    assert _baseline_key("kb/x.yaml", "the  title") == _baseline_key("kb/x.yaml", "the title")


def test_baseline_roundtrips_a_snippet_containing_a_newline(tmp_path):
    findings = [("kb/x.yaml", "a.b", "title", "wrapped\ntitle text")]
    path = tmp_path / "baseline.txt"
    write_baseline(findings, path)
    assert load_baseline(path) == Counter({_baseline_key("kb/x.yaml", "wrapped title text"): 1})


def test_baseline_records_occurrence_counts(tmp_path):
    findings = [
        ("kb/x.yaml", "a", "title", TITLE),
        ("kb/x.yaml", "b", "title", TITLE),
    ]
    path = tmp_path / "baseline.txt"
    write_baseline(findings, path)
    assert load_baseline(path)[_baseline_key("kb/x.yaml", TITLE)] == 2


def test_extra_reuse_of_a_baselined_snippet_is_a_new_finding(tmp_path):
    """One title pasted across more claims than the baseline records is new."""
    path = tmp_path / "baseline.txt"
    write_baseline([("kb/x.yaml", "a", "title", TITLE)], path)
    baseline = load_baseline(path)
    findings = [
        ("kb/x.yaml", "a", "title", TITLE),
        ("kb/x.yaml", "b", "title", TITLE),
    ]
    assert len(new_findings(findings, baseline)) == 1


def test_baseline_does_not_grandfather_an_unrelated_snippet(tmp_path):
    path = tmp_path / "baseline.txt"
    write_baseline([("kb/x.yaml", "a", "title", TITLE)], path)
    other = [("kb/y.yaml", "a", "title", TITLE)]
    assert len(new_findings(other, load_baseline(path))) == 1


def test_baseline_tolerates_the_pre_count_line_format(tmp_path):
    path = tmp_path / "baseline.txt"
    path.write_text(f"# header\n{_baseline_key('kb/x.yaml', TITLE)}\n", encoding="utf-8")
    assert load_baseline(path)[_baseline_key("kb/x.yaml", TITLE)] == 1


def test_baseline_from_ref_returns_none_for_an_unknown_ref(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    assert baseline_from_ref("no-such-ref", root=tmp_path) is None


def test_resolve_baseline_prefers_the_explicit_ref_over_env(monkeypatch):
    sentinel = Counter({"kb/x.yaml\tfoo": 3})
    seen = {}

    def fake(ref, **_kw):
        seen["ref"] = ref
        return sentinel

    monkeypatch.setattr(cts, "baseline_from_ref", fake)
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline("origin/explicit") is sentinel
    assert seen["ref"] == "origin/explicit"


def test_resolve_baseline_reads_the_env_var(monkeypatch):
    sentinel = Counter({"k": 1})
    monkeypatch.setattr(cts, "baseline_from_ref", lambda ref, **_kw: sentinel)
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline() is sentinel


def test_resolve_baseline_falls_back_when_the_ref_is_unreadable(monkeypatch):
    monkeypatch.setattr(cts, "baseline_from_ref", lambda ref, **_kw: None)
    monkeypatch.delenv(BASELINE_REF_ENV, raising=False)
    assert resolve_baseline("bad-ref") == load_baseline()


# --- the committed backlog ---------------------------------------------------


def _baseline_drift(repo_findings):
    """Return ``(stale, missing)`` between the committed baseline and the tree.

    ``stale``   -- baselined entries no longer present (the backlog shrank).
    ``missing`` -- violations in the tree that the baseline does not grandfather.
    """
    committed = load_baseline()
    current = Counter(_baseline_key(rel, snippet) for rel, _, _, snippet in repo_findings)
    stale = {k: committed[k] for k in committed if current.get(k, 0) < committed[k]}
    missing = {k: current[k] for k in current if committed.get(k, 0) < current[k]}
    return stale, missing


def test_baseline_drift_separates_a_new_violation_from_a_fixed_one(monkeypatch):
    """The split above is only worth having if it still catches a new violation.

    Loosening a guard so it tolerates progress is one edit away from loosening it
    so it tolerates everything, and the repository-wide checks cannot demonstrate
    the failing case (kb/ is, correctly, clean of new violations). So drive
    ``_baseline_drift`` directly in both directions.
    """
    fixed = "kb/disorders/Fixed.yaml\tA title that has since been replaced."
    monkeypatch.setattr(
        "tests.test_title_snippets.load_baseline", lambda *_a, **_k: Counter({fixed: 1})
    )

    # A violation in the tree that the baseline does not cover -> `missing`.
    findings = [("kb/disorders/New.yaml", "evidence[0].snippet", "title", "A brand new title snippet.")]
    stale, missing = _baseline_drift(findings)
    assert list(missing) == ["kb/disorders/New.yaml\tA brand new title snippet."]
    assert list(stale) == [fixed]  # and the baselined one is simultaneously gone

    # An empty tree is pure shrinkage: stale, but nothing new to gate on.
    stale, missing = _baseline_drift([])
    assert list(stale) == [fixed]
    assert not missing


def test_committed_baseline_grandfathers_every_current_violation(repo_findings):
    """The committed snapshot is the local fallback; keep it honest.

    CI grandfathers against the base branch and never reads this file, so it can
    drift silently. This is the half of that honesty check worth gating on: a
    violation present in the tree but absent from the baseline would show up as
    a spurious "new" finding on someone else's unrelated branch later.

    Deliberately says nothing about baselined entries that have since been
    *fixed* -- see the companion advisory check below for why.
    """
    _stale, missing = _baseline_drift(repo_findings)
    assert not missing, (
        f"{len(missing)} title-quoting snippet(s) in kb/ are not grandfathered by "
        f"{cts.BASELINE_PATH.relative_to(ROOT)}; if they are genuinely new, fix "
        "the snippets (see issue #8374) rather than baselining them"
    )


def test_committed_baseline_carries_no_fixed_entries(repo_findings):
    """Advisory only: a shrinking backlog is progress, not a defect (#8434).

    This used to be asserted together with the check above, which meant fixing a
    title snippet in kb/ turned a *passing* suite red on the next unrelated
    branch that touched src/ or tests/. It fired exactly that way within a day
    of the baseline being created: #8334 and #8346 each correctly replaced
    title-only snippets, neither regenerated the file, and the bill landed on a
    dependency bump.

    An over-full baseline cannot hide a new violation -- it can only
    over-grandfather entries that no longer exist -- and CI does not read the
    file at all. So this skips rather than fails, and the
    `title-snippet-baseline` workflow regenerates the file on merge to main.
    """
    stale, _missing = _baseline_drift(repo_findings)
    if stale:
        pytest.skip(
            f"{len(stale)} baselined entr(y/ies) no longer present -- the backlog "
            "shrank. Harmless; the title-snippet-baseline workflow refreshes this "
            "on merge, or run `just update-title-snippet-baseline` to do it now."
        )

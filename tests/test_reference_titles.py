"""Guard test: no NEW mismatched `reference_title` values in kb/.

An evidence item can carry an invented title for a real, correctly-cited paper
whose snippet verifies perfectly -- every gate in the stack checks a different
field, so nothing looks at the title. A baseline grandfathers the pre-existing
backlog so this fails only on newly introduced ones.

See scripts/check_reference_titles.py and dismech issue #9138.
"""

import subprocess
from collections import Counter
from pathlib import Path

from scripts import check_reference_titles as crt
from scripts.check_reference_titles import (
    BASELINE_REF_ENV,
    MIN_SIMILARITY,
    _baseline_key,
    baseline_from_ref,
    contains,
    exempt_prefix_set,
    find_violations,
    iter_title_pairs,
    load_baseline,
    new_findings,
    normalize,
    resolve_baseline,
    scan_repo,
    similarity,
    write_baseline,
)

import pytest

ROOT = Path(__file__).resolve().parents[1]
CACHE_DIR = ROOT / "references_cache"


@pytest.fixture(scope="module")
def kb_findings():
    """One whole-KB scan shared by the tests that need it (~90s otherwise each)."""
    return scan_repo()

REFERENCE_FIELDS = frozenset({"reference"})

#: The three fabricated titles a reviewer caught on PR #9111 (CFEOM), paired
#: with the real title sitting in each PMID's cache frontmatter the whole time.
#: Two were written by an agent that had just verified the adjacent snippets.
CFEOM_9111 = {
    "PMID:27513105": (
        "Identification of a recurrent mutation in KIF21A in two Chinese "
        "families with congenital fibrosis of the extraocular muscles.",
        "KIF21A mutation in two Chinese families with congenital fibrosis of "
        "the extraocular muscles type 1 and 3.",
    ),
    "PMID:34081534": (
        "Congenital cranial dysinnervation disorders: a concept in evolution.",
        "Axonal Growth Abnormalities Underlying Ocular Cranial Nerve Disorders.",
    ),
    "PMID:39033378": (
        "Novel variants in the oculomotor and trochlear nerve development "
        "pathways in congenital cranial dysinnervation disorders.",
        "Expanding the genetics and phenotypes of ocular congenital cranial "
        "dysinnervation disorders.",
    ),
}


def _cache(tmp_path: Path, reference_id: str, title: str) -> Path:
    """A minimal reference cache file with frontmatter, as the fetcher writes it."""
    # `/` is legal in a DOI but not in a filename; the real cache sanitises too.
    path = tmp_path / f"{reference_id.replace(':', '_').replace('/', '_')}.md"
    path.write_text(
        f'---\nreference_id: "{reference_id}"\ntitle: "{title}"\n'
        "content_type: abstract_only\n---\n\n## Content\nabstract text\n",
        encoding="utf-8",
    )
    return path


class _Index:
    """Stand-in for CachedReferenceIndex over a dict of id -> path."""

    def __init__(self, mapping):
        self._mapping = mapping

    def resolve_cache_path(self, reference_id):
        return self._mapping.get(reference_id)


def _doc(reference_id="PMID:1", title="A title", field="reference_title"):
    return {"evidence": [{"reference": reference_id, field: title}]}


def _violations(data, mapping):
    return list(
        find_violations(data, REFERENCE_FIELDS, _Index(mapping), exempt_prefixes=frozenset())
    )


# --- the guard itself -------------------------------------------------------


def test_no_new_mismatched_reference_titles(kb_findings):
    # resolve_baseline() grandfathers against origin/main when CI sets
    # REFERENCE_TITLE_BASELINE_REF (so the base branch is green by construction
    # and parallel merges cannot clobber the grandfather set), and falls back to
    # the committed baseline for local runs / shallow checkouts.
    baseline = resolve_baseline()
    new = [
        f"{rel}:{location}: {reference} -- wrote {title!r}, cache says {cached!r}"
        for rel, location, reference, title, cached, _ratio in new_findings(
            kb_findings, baseline
        )
    ]
    assert not new, (
        "Reference title(s) that do not match the cited reference detected. "
        "`reference_title`/`title` is the title of the paper you cited, and the "
        "correct value is already in that reference's cache frontmatter -- copy "
        "it from there. A verified snippet does not vouch for the citation "
        "written beside it:\n  " + "\n  ".join(new)
    )


# --- the motivating case (#9111) -------------------------------------------


def test_flags_the_known_cfeom_fabrications(tmp_path):
    """The three PR #9111 titles are caught, against their real cache files.

    This is the regression this guard exists for, so it runs against the
    *committed* references_cache/ rather than a fixture -- a synthetic cache
    would prove only that the comparison works, not that it works on the data
    that actually shipped.
    """
    index = crt.CachedReferenceIndex(CACHE_DIR)
    for reference_id, (fabricated, expected_cached) in CFEOM_9111.items():
        findings = list(
            find_violations(
                _doc(reference_id, fabricated),
                REFERENCE_FIELDS,
                index,
                exempt_prefixes=frozenset(),
            )
        )
        assert len(findings) == 1, f"{reference_id} was not flagged"
        _location, ref, wrote, cached, ratio = findings[0]
        assert ref == reference_id
        assert wrote == fabricated
        # The failure message must carry the correct title so the fix is a
        # copy-paste; assert on the cache's own value, not a paraphrase of it.
        assert cached == expected_cached
        assert ratio < MIN_SIMILARITY


def test_accepts_the_corrected_cfeom_titles(tmp_path):
    """The values PR #9111 fixed them *to* must pass, or the guard is useless."""
    index = crt.CachedReferenceIndex(CACHE_DIR)
    for reference_id, (_fabricated, corrected) in CFEOM_9111.items():
        assert not list(
            find_violations(
                _doc(reference_id, corrected),
                REFERENCE_FIELDS,
                index,
                exempt_prefixes=frozenset(),
            )
        ), f"{reference_id} false-positived on its own cached title"


# --- comparison semantics ---------------------------------------------------


def test_exact_title_passes(tmp_path):
    mapping = {"PMID:1": _cache(tmp_path, "PMID:1", "A study of things.")}
    assert not _violations(_doc("PMID:1", "A study of things."), mapping)


def test_trailing_period_difference_passes(tmp_path):
    mapping = {"PMID:1": _cache(tmp_path, "PMID:1", "A study of things.")}
    assert not _violations(_doc("PMID:1", "A study of things"), mapping)


def test_dash_and_smart_quote_differences_pass(tmp_path):
    mapping = {
        "PMID:1": _cache(tmp_path, "PMID:1", "Wolff–Parkinson–White “syndrome”")
    }
    assert not _violations(_doc("PMID:1", 'Wolff-Parkinson-White "syndrome"'), mapping)


def test_diacritic_difference_passes(tmp_path):
    # A curator transcribing 'Guillain-Barre' for a cached 'Guillain-Barré' has
    # not misidentified the paper. Without folding, the accent alone costs
    # enough similarity to push an otherwise clean pair under the threshold.
    mapping = {
        "PMID:1": _cache(
            tmp_path, "PMID:1", "Pain determinants in Guillain-Barré syndrome"
        )
    }
    assert not _violations(
        _doc("PMID:1", "Pain determinants in Guillain-Barre syndrome"), mapping
    )


def test_source_xml_markup_in_the_cached_title_passes(tmp_path):
    # Crossref titles arrive carrying JATS runs. The angle brackets fold to
    # spaces on their own, but the tag *names* would survive as words.
    mapping = {
        "PMID:1": _cache(
            tmp_path, "PMID:1", "<scp>FIGO</scp> staging of <i>endometrial</i> cancer"
        )
    }
    assert not _violations(
        _doc("PMID:1", "FIGO staging of endometrial cancer"), mapping
    )


def test_a_different_paper_is_flagged(tmp_path):
    mapping = {"PMID:1": _cache(tmp_path, "PMID:1", "Axonal growth abnormalities.")}
    findings = _violations(_doc("PMID:1", "A concept in evolution."), mapping)
    assert len(findings) == 1
    assert findings[0][3] == "Axonal growth abnormalities."


def test_similarity_is_symmetric_and_bounded():
    assert similarity("", "anything") == 0.0
    assert similarity("same", "same") == 1.0
    assert 0.0 <= similarity("a study of things", "a study of stuff") <= 1.0


# --- exemptions -------------------------------------------------------------


def test_an_appended_source_annotation_passes(tmp_path):
    # The `X (Orphanet structured-database record)` convention accounts for the
    # overwhelming majority of raw findings and is a convention being FOLLOWED.
    # Exempted generically via containment, not by matching that literal string.
    mapping = {"ORPHA:1": _cache(tmp_path, "ORPHA:1", "Marfan syndrome")}
    assert not _violations(
        _doc("ORPHA:1", "Marfan syndrome (Orphanet structured-database record)"), mapping
    )


def test_a_title_truncated_at_its_subtitle_passes(tmp_path):
    mapping = {
        "PMID:1": _cache(
            tmp_path, "PMID:1", "Pain and quality of life: a prospective cohort study."
        )
    }
    assert not _violations(_doc("PMID:1", "Pain and quality of life"), mapping)


def test_containment_is_word_bounded():
    # A short title must not match mid-word inside a longer one.
    assert contains("a study of things", "study of")
    assert not contains("a study of things", "tud")


def test_uncached_reference_is_skipped():
    # Reporting uncached references is `just fetch-reference`'s job.
    assert not _violations(_doc("PMID:404", "Anything at all."), {})


def test_cache_file_without_a_title_is_skipped(tmp_path):
    path = tmp_path / "PMID_1.md"
    path.write_text("---\nreference_id: PMID:1\n---\n\nbody\n", encoding="utf-8")
    assert not _violations(_doc("PMID:1", "Anything at all."), {"PMID:1": path})


def test_blank_title_is_skipped(tmp_path):
    # find_missing_reference_titles.py is the check for *absent* titles.
    mapping = {"PMID:1": _cache(tmp_path, "PMID:1", "A study of things.")}
    assert not _violations(_doc("PMID:1", "   "), mapping)


def test_url_prefixed_references_are_exempt(tmp_path):
    # A url: cache file's title is a scraped page title or the first section
    # heading of a full-text XML fetch ('Abstract', 'Introduction'), not a
    # publication title, so comparing against it says nothing.
    assert "url" in exempt_prefix_set()
    reference = "url:https://example.org/paper"
    path = tmp_path / "url_x.md"
    path.write_text(
        '---\nreference_id: "x"\ntitle: "Introduction"\n---\n\nbody\n', encoding="utf-8"
    )
    assert not list(
        find_violations(
            _doc(reference, "A completely unrelated paper title."),
            REFERENCE_FIELDS,
            _Index({reference: path}),
        )
    )


def test_dataset_prefixes_are_exempt():
    # Sourced from the reference validator's own skip_prefixes, minus DOI.
    exempt = exempt_prefix_set()
    assert "geo" in exempt
    assert "doi" not in exempt


# --- walking ----------------------------------------------------------------


def test_walks_top_level_references_using_the_title_slot():
    # PublicationReference uses `title`; EvidenceItem uses `reference_title`.
    data = {"references": [{"reference": "PMID:1", "title": "A study."}]}
    pairs = list(iter_title_pairs(data, REFERENCE_FIELDS))
    assert pairs == [("references[0].title", "title", "PMID:1", "A study.")]


def test_walks_nested_evidence_items():
    data = {
        "pathophysiology": [
            {"downstream": [{"evidence": [{"reference": "PMID:2", "reference_title": "T"}]}]}
        ]
    }
    pairs = list(iter_title_pairs(data, REFERENCE_FIELDS))
    assert pairs == [
        (
            "pathophysiology[0].downstream[0].evidence[0].reference_title",
            "reference_title",
            "PMID:2",
            "T",
        )
    ]


def test_a_title_without_a_reference_is_ignored():
    # `title` is a common slot name; without a sibling reference there is
    # nothing to compare it against and it is not a citation.
    assert not list(iter_title_pairs({"title": "Some section heading"}, REFERENCE_FIELDS))


def test_non_string_values_are_skipped():
    data = {"evidence": [{"reference": "PMID:1", "reference_title": 42}]}
    assert not list(iter_title_pairs(data, REFERENCE_FIELDS))


def test_scan_dir_is_the_kb_root_not_just_disorders():
    # Pins the module constant: kb/modules/, kb/comorbidities/ and
    # kb/groupings/ carry evidence items too, and a fabricated title there is
    # the same defect.
    assert crt.SCAN_DIR == crt.ROOT / "kb"


def test_scan_covers_kb_beyond_disorders(tmp_path):
    cache = tmp_path / "cache"
    cache.mkdir()
    _cache(cache, "PMID:1", "The real title of the paper.")
    for sub in ("modules", "comorbidities", "groupings"):
        target = tmp_path / "kb" / sub
        target.mkdir(parents=True)
        (target / "X.yaml").write_text(
            "evidence:\n- reference: PMID:1\n"
            "  reference_title: Something else entirely, invented.\n",
            encoding="utf-8",
        )
    findings = scan_repo(scan_dir=tmp_path / "kb", rel_to=tmp_path, cache_dir=cache)
    assert sorted(rel for rel, *_ in findings) == [
        "kb/comorbidities/X.yaml",
        "kb/groupings/X.yaml",
        "kb/modules/X.yaml",
    ]


# --- baseline ---------------------------------------------------------------


def _finding(rel="kb/disorders/X.yaml", loc="evidence[0]", ref="PMID:1", title="T"):
    return (rel, loc, ref, title, "Cached title.", 0.3)


def test_baseline_key_is_location_independent():
    assert _baseline_key("kb/x.yaml", "PMID:1", "T") == _baseline_key(
        "kb/x.yaml", "PMID:1", "T"
    )


def test_baseline_does_not_grandfather_an_unrelated_title(tmp_path):
    baseline_path = tmp_path / "baseline.txt"
    write_baseline([_finding()], baseline_path)
    baseline = load_baseline(baseline_path)
    # Different title, same reference: still new.
    assert new_findings([_finding(title="Other")], baseline)
    # Same title, different reference: still new.
    assert new_findings([_finding(ref="PMID:2")], baseline)
    # Same title, different file: still new.
    assert new_findings([_finding(rel="kb/disorders/Y.yaml")], baseline)


def test_extra_reuse_of_a_baselined_title_is_a_new_finding(tmp_path):
    """One grandfathered wrong title stays quiet; pasting it a second time does not."""
    known = [_finding()]
    baseline_path = tmp_path / "baseline.txt"
    write_baseline(known, baseline_path)
    baseline = load_baseline(baseline_path)

    assert not new_findings(known, baseline)
    extra = new_findings([*known, _finding(loc="evidence[1]")], baseline)
    assert len(extra) == 1
    assert extra[0][1] == "evidence[1]"


def test_baseline_records_occurrence_counts(tmp_path):
    baseline_path = tmp_path / "baseline.txt"
    write_baseline(
        [_finding(), _finding(loc="evidence[1]"), _finding(rel="kb/disorders/Y.yaml")],
        baseline_path,
    )
    baseline = load_baseline(baseline_path)
    assert baseline[_baseline_key("kb/disorders/X.yaml", "PMID:1", "T")] == 2
    assert baseline[_baseline_key("kb/disorders/Y.yaml", "PMID:1", "T")] == 1
    assert "count<TAB>path<TAB>reference<TAB>title" in baseline_path.read_text()


def test_baseline_key_collapses_wrapped_whitespace(tmp_path):
    # The baseline file is line-oriented; YAML titles wrap freely.
    baseline_path = tmp_path / "baseline.txt"
    write_baseline([_finding(title="A long\n  wrapped title")], baseline_path)
    baseline = load_baseline(baseline_path)
    assert not new_findings([_finding(title="A long wrapped title")], baseline)


def test_baseline_tolerates_the_pre_count_line_format(tmp_path):
    baseline_path = tmp_path / "baseline.txt"
    baseline_path.write_text(
        "# legacy header\nkb/disorders/X.yaml\tPMID:1\tT\n", encoding="utf-8"
    )
    assert not new_findings([_finding()], load_baseline(baseline_path))


def test_committed_baseline_covers_the_committed_kb(kb_findings):
    """No mismatch in kb/ escapes the grandfather baseline.

    Uses :func:`resolve_baseline` rather than :func:`load_baseline` so the
    ``REFERENCE_TITLE_BASELINE_REF`` env var the workflow sets is honoured here
    too. Reading the committed file unconditionally made this red on any branch
    where ``main`` had gained unbaselined mismatches since the file was written
    -- which is exactly what happened while PR #9141 sat, and it would have
    stayed red on ``main`` after merge.
    """
    assert not new_findings(kb_findings, resolve_baseline())


def test_committed_baseline_carries_no_stale_entries(kb_findings):
    """Advisory only: a shrinking backlog is progress, not a defect (#8434).

    Mirrors ``test_committed_baseline_carries_no_fixed_entries`` in
    ``tests/test_title_snippets.py``. An over-full baseline cannot hide a new
    violation -- it can only over-grandfather entries that no longer exist --
    and CI grandfathers against the base branch rather than reading this file,
    so a curator who fixes a title without regenerating the baseline should not
    turn someone else's later branch red.
    """
    baseline = load_baseline()
    live = crt.count_by_key(kb_findings)
    stale = {key: n for key, n in baseline.items() if live[key] < n}
    if stale:
        pytest.skip(
            f"{len(stale)} baseline entry/entries no longer occur in kb/; "
            "regenerate with `just update-reference-title-baseline` "
            "(the reference-title-baseline workflow does this on merge to main)"
        )


# --- ref-derived grandfather baseline --------------------------------------


def _init_git_repo(path: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.email", "t@example.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=path, check=True)


def test_baseline_from_ref_reads_kb_at_the_ref(tmp_path, monkeypatch):
    cache = tmp_path / "cache"
    cache.mkdir()
    _cache(cache, "PMID:1", "The real title of the paper.")
    monkeypatch.setattr(crt, "CACHE_DIR", cache)

    disorders = tmp_path / "kb" / "disorders"
    disorders.mkdir(parents=True)
    (disorders / "X.yaml").write_text(
        "evidence:\n- reference: PMID:1\n  reference_title: Invented, unrelated.\n",
        encoding="utf-8",
    )
    _init_git_repo(tmp_path)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=tmp_path, check=True)

    counts = baseline_from_ref("HEAD", root=tmp_path)
    assert counts is not None
    assert counts[
        _baseline_key("kb/disorders/X.yaml", "PMID:1", "Invented, unrelated.")
    ] == 1


def test_baseline_from_ref_returns_none_for_an_unknown_ref(tmp_path):
    _init_git_repo(tmp_path)
    assert baseline_from_ref("no-such-ref-deadbeef", root=tmp_path) is None


def test_resolve_baseline_prefers_the_explicit_ref_over_env_and_committed_file(
    monkeypatch,
):
    seen = {}
    sentinel = Counter({"kb/x.yaml\tPMID:1\tfoo": 3})

    def fake(ref, **kw):
        seen["ref"] = ref
        return sentinel

    monkeypatch.setattr(crt, "baseline_from_ref", fake)
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline("origin/explicit") is sentinel
    assert seen["ref"] == "origin/explicit"


def test_resolve_baseline_reads_the_env_var(monkeypatch):
    seen = {}
    sentinel = Counter({"k": 1})

    def fake(ref, **kw):
        seen["ref"] = ref
        return sentinel

    monkeypatch.setattr(crt, "baseline_from_ref", fake)
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline() is sentinel
    assert seen["ref"] == "origin/from-env"


def test_resolve_baseline_falls_back_when_the_ref_is_unreadable(monkeypatch):
    monkeypatch.setattr(crt, "baseline_from_ref", lambda ref, **kw: None)
    monkeypatch.delenv(BASELINE_REF_ENV, raising=False)
    assert resolve_baseline("bad-ref") == load_baseline()


def test_normalize_is_idempotent():
    once = normalize("The <i>FOO</i> Study: Guillain-Barré syndrome.")
    assert normalize(once) == once

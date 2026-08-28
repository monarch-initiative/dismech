"""Guard test: one quoted sentence must not carry two `evidence_source` values.

`evidence_source` describes the cited publication, not the block the quote was
pasted into, so quoting the same sentence from the same reference twice in one
file and grading it two different ways is a contradiction the file contains. A
baseline grandfathers the pre-existing backlog so this fails only on newly
introduced divergences.

See scripts/check_snippet_grading.py and dismech issue #8184.
"""

import subprocess
from collections import Counter
from pathlib import Path

from scripts import check_snippet_grading as csg
from scripts.check_snippet_grading import (
    BASELINE_REF_ENV,
    GATED_FIELDS,
    GRADING_DEFAULTS,
    MIN_OVERLAP_WORDS,
    _baseline_key,
    _resolve_fields,
    baseline_from_ref,
    find_violations,
    format_finding,
    load_baseline,
    new_findings,
    resolve_baseline,
    scan_repo,
    write_baseline,
)

ROOT = Path(__file__).resolve().parents[1]

EXCERPT_FIELDS = frozenset({"snippet"})
REFERENCE_FIELDS = frozenset({"reference"})


def _violations(data, fields=GATED_FIELDS):
    return list(
        find_violations(data, EXCERPT_FIELDS, REFERENCE_FIELDS, fields=fields)
    )


def _item(snippet, reference="PMID:1", **gradings):
    return {"reference": reference, "snippet": snippet, **gradings}


def _doc(*items):
    """One disorder-shaped document whose evidence items are *items*."""
    return {"name": "T", "pathophysiology": [{"name": "N", "evidence": list(items)}]}


SENTENCE = "HAGH functions in a pathway to detoxify methylglyoxal in the brain."


def test_no_new_snippet_grading_divergences():
    # resolve_baseline() grandfathers against origin/main when CI sets
    # SNIPPET_GRADING_BASELINE_REF (so the base branch is green by construction
    # and parallel merges cannot clobber the grandfather set), and falls back to
    # the committed baseline for local runs / shallow checkouts.
    baseline = resolve_baseline()
    new = [format_finding(finding) for finding in new_findings(scan_repo(), baseline)]
    assert not new, (
        "New snippet-grading divergence(s) detected. `evidence_source` describes "
        "the cited publication, not the block the quote sits in, so one sentence "
        "cannot carry two values in one file. Grade the quote once, or quote the "
        "sentence that actually makes each claim:\n  " + "\n  ".join(new)
    )


# --- the invariant ------------------------------------------------------------


def test_same_sentence_with_two_evidence_sources_is_flagged():
    findings = _violations(
        _doc(
            _item(SENTENCE, evidence_source="COMPUTATIONAL"),
            _item(SENTENCE, evidence_source="HUMAN_CLINICAL"),
        )
    )
    assert len(findings) == 1
    field, reference, left, right, quote, loc_a, loc_b = findings[0]
    assert field == "evidence_source"
    assert reference == "PMID:1"
    assert {left, right} == {"COMPUTATIONAL", "HUMAN_CLINICAL"}
    assert quote == SENTENCE
    assert loc_a != loc_b


def test_same_sentence_with_one_evidence_source_is_fine():
    assert not _violations(
        _doc(
            _item(SENTENCE, evidence_source="IN_VITRO"),
            _item(SENTENCE, evidence_source="IN_VITRO"),
        )
    )


def test_absent_evidence_source_counts_as_human_clinical():
    """The COPD shape from #8182: an `OTHER` twin beside one that omits the field.

    CLAUDE.md documents HUMAN_CLINICAL as the value an absent `evidence_source`
    means, so the omission is an assertion -- not an abstention.
    """
    assert _violations(_doc(_item(SENTENCE), _item(SENTENCE, evidence_source="OTHER")))
    # ... and the same omission beside an explicit HUMAN_CLINICAL agrees.
    assert not _violations(
        _doc(_item(SENTENCE), _item(SENTENCE, evidence_source="HUMAN_CLINICAL"))
    )


def test_one_paper_may_carry_two_sources_on_two_different_sentences():
    """The correction that killed the per-PMID formulation of #8184.

    PMID:15496428 is cited five times in Paroxysmal_Dyskinesia.yaml and
    legitimately grades its homology argument COMPUTATIONAL and its clinical
    cohort HUMAN_CLINICAL -- CLAUDE.md tells curators to split mixed-source
    papers exactly that way.
    """
    assert not _violations(
        _doc(
            _item(
                "Bioinformatic analysis reveals that the MR-1 gene is homologous "
                "to hydroxyacylglutathione hydrolase.",
                evidence_source="COMPUTATIONAL",
            ),
            _item(
                "We report mutations in the MR-1 gene causing PNKD in 50 "
                "individuals from eight families.",
                evidence_source="HUMAN_CLINICAL",
            ),
        )
    )


def test_overlapping_extents_of_one_passage_are_compared():
    """#8293's actual shape: one item quoted a shorter extent of the same passage.

    An exact-match-only check would have missed it, which is why containment is
    compared and why the *shared* extent is what the finding reports.
    """
    long_quote = (
        "Bioinformatic analysis reveals homology; HAGH functions in a pathway "
        "to detoxify methylglyoxal in the brain."
    )
    short_quote = "HAGH functions in a pathway to detoxify methylglyoxal in the brain."
    findings = _violations(
        _doc(
            _item(long_quote, evidence_source="COMPUTATIONAL"),
            _item(short_quote, evidence_source="HUMAN_CLINICAL"),
        )
    )
    assert len(findings) == 1
    assert findings[0][4] == short_quote  # the shared extent, not the longer quote


def test_a_short_fragment_inside_a_longer_quote_is_not_treated_as_a_requote():
    """Below MIN_OVERLAP_WORDS a containment is likelier coincidence than a quote."""
    fragment = " ".join(["word"] * (MIN_OVERLAP_WORDS - 1))
    assert not _violations(
        _doc(
            _item(f"prefix {fragment} suffix text here", evidence_source="IN_VITRO"),
            _item(fragment, evidence_source="HUMAN_CLINICAL"),
        )
    )


def test_whitespace_and_case_differences_do_not_hide_a_divergence():
    # YAML plain scalars wrap, so the same sentence routinely differs in
    # whitespace between two blocks.
    wrapped = SENTENCE.replace(" a pathway ", "\n  a  pathway\n  ")
    assert _violations(
        _doc(
            _item(SENTENCE, evidence_source="IN_VITRO"),
            _item(wrapped.upper(), evidence_source="MODEL_ORGANISM"),
        )
    )


def test_different_references_are_not_compared():
    # Two papers can of course say the same thing with different evidence types.
    assert not _violations(
        _doc(
            _item(SENTENCE, reference="PMID:1", evidence_source="IN_VITRO"),
            _item(SENTENCE, reference="PMID:2", evidence_source="HUMAN_CLINICAL"),
        )
    )


def test_a_snippet_without_a_reference_is_ignored():
    assert not _violations({"notes": [{"snippet": SENTENCE}]})


def test_divergence_is_found_across_unrelated_sections():
    """The motivating cases straddle sections, so the walk must not be per-block."""
    data = {
        "name": "T",
        "pathophysiology": [
            {"name": "N", "evidence": [_item(SENTENCE, evidence_source="COMPUTATIONAL")]}
        ],
        "environmental": [
            {
                "name": "E",
                "influences_mechanisms": [
                    {"target": "N", "evidence": [_item(SENTENCE)]}
                ],
            }
        ],
    }
    findings = _violations(data)
    assert len(findings) == 1
    assert findings[0][2:4] == ("COMPUTATIONAL", "HUMAN_CLINICAL")


# --- `supports` is scanned on request, never gated ----------------------------


def test_supports_divergence_is_not_gated_by_default():
    """`supports` is claim-relative by design, so it is measured, not enforced.

    The same sentence legitimately reads SUPPORT for one claim and PARTIAL for
    another; across kb/ that shape outnumbers the evidence_source signal ~11:1.
    """
    data = _doc(
        _item(SENTENCE, supports="SUPPORT"),
        _item(SENTENCE, supports="PARTIAL"),
    )
    assert not _violations(data)
    assert _violations(data, fields=("supports",))


def test_absent_supports_is_not_compared():
    # Unlike evidence_source, `supports` has no documented default, so an item
    # that omits it must not be read as asserting anything.
    assert not _violations(
        _doc(_item(SENTENCE), _item(SENTENCE, supports="REFUTE")),
        fields=("supports",),
    )


def test_field_selection():
    assert _resolve_fields("evidence_source") == ("evidence_source",)
    assert _resolve_fields("supports") == ("supports",)
    assert set(_resolve_fields("all")) == set(GRADING_DEFAULTS)
    assert GATED_FIELDS == ("evidence_source",)


# --- baseline ratchet ---------------------------------------------------------


def _finding(
    rel="kb/disorders/X.yaml",
    reference="PMID:1",
    left="HUMAN_CLINICAL",
    right="OTHER",
    quote=SENTENCE,
    loc_a="a",
    loc_b="b",
):
    return (rel, "evidence_source", reference, left, right, quote, loc_a, loc_b)


def test_baseline_key_ignores_location_and_value_order():
    # Locations shift whenever a list above them grows; and which item was
    # written first is not a property of the divergence.
    assert _baseline_key(_finding(loc_a="p[9]", loc_b="t[3]")) == _baseline_key(
        _finding(left="OTHER", right="HUMAN_CLINICAL")
    )


def test_baseline_roundtrips_a_quote_containing_a_newline(tmp_path):
    # The baseline file is line-oriented; a wrapped quote must still match
    # itself after a write/read cycle.
    findings = [_finding(quote="complete female\nexternal genitalia and gonads")]
    path = tmp_path / "baseline.txt"
    write_baseline(findings, path)
    assert not new_findings(findings, load_baseline(path))


def test_baseline_does_not_grandfather_an_unrelated_divergence(tmp_path):
    path = tmp_path / "baseline.txt"
    write_baseline([_finding()], path)
    baseline = load_baseline(path)

    # Different quote, same file.
    assert new_findings([_finding(quote="A wholly different sentence entirely.")], baseline)
    # Same quote, different file.
    assert new_findings([_finding(rel="kb/disorders/Y.yaml")], baseline)
    # Same quote and file, but now disagreeing about a different pair of values:
    # that is a divergence nobody signed off on.
    assert new_findings([_finding(right="IN_VITRO")], baseline)


def test_extra_repeat_of_a_baselined_divergence_is_a_new_finding(tmp_path):
    """A set-of-keys baseline would wave a third contradicting copy through."""
    known = [_finding(loc_b="b"), _finding(loc_b="c")]
    path = tmp_path / "baseline.txt"
    write_baseline(known, path)
    baseline = load_baseline(path)

    assert not new_findings(known, baseline)
    extra = new_findings([*known, _finding(loc_b="d")], baseline)
    assert len(extra) == 1
    assert extra[0][7] == "d"


def test_baseline_records_occurrence_counts(tmp_path):
    path = tmp_path / "baseline.txt"
    write_baseline([_finding(loc_b="b"), _finding(loc_b="c")], path)
    assert load_baseline(path)[_baseline_key(_finding())] == 2
    assert "count<TAB>path<TAB>field<TAB>reference<TAB>a|b<TAB>quote" in path.read_text()


def test_baseline_tolerates_the_pre_count_line_format(tmp_path):
    path = tmp_path / "baseline.txt"
    path.write_text(
        f"# legacy header\n{_baseline_key(_finding())}\n", encoding="utf-8"
    )
    assert not new_findings([_finding()], load_baseline(path))


def test_committed_baseline_holds_only_the_gated_field():
    # `--update-baseline` pins the gated field regardless of --fields; if that
    # regresses, a `--fields all` run would silently enshrine 7,960 correct
    # `supports` divergences as grandfathered findings.
    for line in csg.BASELINE_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("#") or not line:
            continue
        assert line.split("\t")[2] == "evidence_source", line


# --- ref-derived grandfather baseline ----------------------------------------


def _init_git_repo(path: Path) -> None:
    subprocess.run(["git", "init", "-q"], cwd=path, check=True)
    subprocess.run(
        ["git", "config", "user.email", "t@example.com"], cwd=path, check=True
    )
    subprocess.run(["git", "config", "user.name", "Test"], cwd=path, check=True)


def test_baseline_from_ref_reads_kb_at_the_ref(tmp_path):
    # A throwaway repo with one divergent entry: baseline_from_ref should
    # git-archive kb/ at the ref, scan it, and key the finding relative to kb/
    # (via rel_to) exactly as the working-tree scan does -- if that remap
    # regresses, every key mismatches and the whole backlog reads as "new".
    disorders = tmp_path / "kb" / "disorders"
    disorders.mkdir(parents=True)
    (disorders / "X.yaml").write_text(
        "name: T\n"
        "pathophysiology:\n"
        "- name: N\n"
        "  evidence:\n"
        "  - reference: PMID:1\n"
        "    evidence_source: OTHER\n"
        f"    snippet: {SENTENCE}\n"
        "  - reference: PMID:1\n"
        f"    snippet: {SENTENCE}\n",
        encoding="utf-8",
    )
    _init_git_repo(tmp_path)
    subprocess.run(["git", "add", "."], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "seed"], cwd=tmp_path, check=True)

    counts = baseline_from_ref("HEAD", root=tmp_path)
    assert counts is not None
    assert counts[_baseline_key(_finding(right="OTHER"))] == 1


def test_baseline_from_ref_returns_none_for_an_unknown_ref(tmp_path):
    _init_git_repo(tmp_path)
    assert baseline_from_ref("no-such-ref-deadbeef", root=tmp_path) is None


def test_resolve_baseline_prefers_the_explicit_ref_over_env(monkeypatch):
    seen = {}
    sentinel = Counter({"kb/x.yaml\tfoo": 3})

    def fake(ref, **kw):
        seen["ref"] = ref
        return sentinel

    monkeypatch.setattr(csg, "baseline_from_ref", fake)
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline("origin/explicit") is sentinel
    assert seen["ref"] == "origin/explicit"


def test_resolve_baseline_reads_the_env_var(monkeypatch):
    seen = {}
    sentinel = Counter({"k": 1})

    def fake(ref, **kw):
        seen["ref"] = ref
        return sentinel

    monkeypatch.setattr(csg, "baseline_from_ref", fake)
    monkeypatch.setenv(BASELINE_REF_ENV, "origin/from-env")
    assert resolve_baseline() is sentinel
    assert seen["ref"] == "origin/from-env"


def test_resolve_baseline_falls_back_when_the_ref_is_unreadable(monkeypatch):
    monkeypatch.setattr(csg, "baseline_from_ref", lambda ref, **kw: None)
    monkeypatch.delenv(BASELINE_REF_ENV, raising=False)
    assert resolve_baseline("bad-ref") == load_baseline()

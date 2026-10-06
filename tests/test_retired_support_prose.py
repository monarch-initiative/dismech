"""Guard test: no NEW prose arguing for a retired ``supports`` grade in kb/.

``supports: PARTIAL`` was retired in #7439 and its values migrated in #10003,
but the explanations written to justify it were not. A baseline grandfathers
that backlog, and only ever shrinks.

See scripts/check_retired_support_prose.py and dismech issue #12805.
"""

from collections import Counter

import pytest

from scripts.check_retired_support_prose import (
    BASELINE_PATH,
    _baseline_key,
    count_by_key,
    find_violations,
    iter_kb_files,
    load_baseline,
    new_findings,
    resolve_baseline,
    scan_repo,
    sentences,
    shrink_baseline,
    write_baseline,
)


def _hits(data):
    return list(find_violations(data))


# --- the repository gate -----------------------------------------------------


@pytest.fixture(scope="module")
def repo_findings():
    return scan_repo()


@pytest.mark.ci_step_twin("scripts/check_retired_support_prose.py")
def test_no_new_retired_support_prose(repo_findings):
    """The gate itself: nothing outside the grandfathered backlog."""
    new = new_findings(repo_findings, resolve_baseline())
    assert not new, "\n".join(
        f"{rel}:{location}: {sentence}" for rel, location, sentence in new[:10]
    )


def test_committed_baseline_is_well_formed():
    """Every non-comment line parses, so a hand edit cannot silently drop one."""
    lines = [
        line
        for line in BASELINE_PATH.read_text(encoding="utf-8").splitlines()
        if line and not line.startswith("#")
    ]
    assert len(load_baseline()) == len(lines)


# --- what counts as a retired-grade mention ----------------------------------


def test_flags_an_explanation_arguing_for_partial():
    data = {
        "evidence": [
            {
                "supports": "SUPPORT",
                "explanation": "Graded PARTIAL because the model is murine.",
            }
        ]
    }
    ((location, sentence),) = _hits(data)
    assert location == "evidence[0].explanation"
    assert sentence == "Graded PARTIAL because the model is murine."


def test_flags_every_prose_field_not_just_explanation():
    data = {
        "notes": "Curated as PARTIAL here.",
        "rationale": "Hence PARTIAL.",
        "review_notes": "Kept PARTIAL.",
    }
    assert {loc for loc, _ in _hits(data)} == {"notes", "rationale", "review_notes"}


def test_flags_wrong_statement_too():
    assert _hits({"explanation": "Marked WRONG_STATEMENT by the curator."})


@pytest.mark.parametrize(
    "text",
    [
        "relationship: PARTIALLY_RECAPITULATES the node.",
        "Functional impact is PARTIAL_LOSS_OF_FUNCTION.",
        "The source gives partial support for the claim.",
        "Only a partially penetrant phenotype.",
    ],
)
def test_ignores_enum_stems_and_lowercase(text):
    assert _hits({"explanation": text}) == []


@pytest.mark.parametrize(
    "text",
    [
        "Four explanations still argued for the retired supports: PARTIAL grade.",
        "This item previously named PARTIAL (see #7439).",
        "PARTIAL was migrated in #10003.",
    ],
)
def test_exempts_sentences_about_the_retirement(text):
    assert _hits({"notes": text}) == []


def test_retirement_exemption_is_per_sentence():
    """A note about the retirement does not excuse a stale grade beside it."""
    text = (
        "The retired PARTIAL grade is gone (#7439). "
        "Graded PARTIAL because only one family was studied."
    )
    ((_location, sentence),) = _hits({"notes": text})
    assert sentence.startswith("Graded PARTIAL")


def test_narrowing_is_not_a_retirement_marker():
    """A real stale grade from the KB that used the word 'narrowing'."""
    text = "Graded PARTIAL because it is a negative result narrowing the claim."
    assert _hits({"explanation": text})


def test_counts_each_mention():
    assert len(_hits({"explanation": "PARTIAL, and PARTIAL again."})) == 2


def test_sentences_collapse_folded_whitespace():
    assert sentences("One\n  two.  Three   four.") == ["One two.", "Three four."]


def test_hypotheses_directory_is_excluded(tmp_path):
    (tmp_path / "hypotheses").mkdir()
    (tmp_path / "disorders").mkdir()
    (tmp_path / "hypotheses" / "a.yaml").write_text("x: PARTIAL\n")
    (tmp_path / "disorders" / "b.yaml").write_text("x: PARTIAL\n")
    assert [p.name for p in iter_kb_files(tmp_path)] == ["b.yaml"]


# --- the ratchet -------------------------------------------------------------

F = ("kb/disorders/X.yaml", "evidence[0].explanation", "Graded PARTIAL.")
G = ("kb/disorders/X.yaml", "evidence[1].explanation", "Hence PARTIAL.")


def test_a_copied_sentence_is_new_even_if_baselined_once():
    baseline = count_by_key([F])
    copy = (F[0], "evidence[5].explanation", F[2])
    assert new_findings([F, copy], baseline) == [copy]


def test_moving_a_sentence_within_a_file_is_free():
    moved = (F[0], "pathophysiology[3].evidence[0].explanation", F[2])
    assert new_findings([moved], count_by_key([F])) == []


def test_shrink_drops_fixed_entries_and_lowers_counts():
    baseline = Counter({_baseline_key(F[0], F[2]): 3, _baseline_key(G[0], G[2]): 1})
    shrunk = shrink_baseline(baseline, [F])
    assert shrunk == Counter({_baseline_key(F[0], F[2]): 1})


def test_shrink_never_adds_or_raises():
    baseline = Counter({_baseline_key(F[0], F[2]): 1})
    shrunk = shrink_baseline(baseline, [F, F, F, G])
    assert shrunk == baseline


def test_baseline_round_trips(tmp_path):
    path = tmp_path / "baseline.txt"
    counts = count_by_key([F, F, G])
    write_baseline(counts, path)
    assert load_baseline(path) == counts


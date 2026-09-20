"""Guard test: no NEW YAML folded-scalar compound-word splits in kb/.

A line inside a YAML folded ('>' / '>-') block scalar that ends in a hyphen is
folded into 'word- next', silently breaking a hyphenated compound (e.g.
'relapsing-remitting' -> 'relapsing- remitting'). A baseline grandfathers the
pre-existing backlog so this test fails only on newly introduced splits.

See scripts/check_folded_hyphens.py and dismech PR #4799.
"""
from pathlib import Path

from scripts.check_folded_hyphens import (
    _baseline_key,
    find_violations_in_text,
    is_status_marker,
    load_baseline,
    scan_repo,
)

ROOT = Path(__file__).resolve().parents[1]


def test_no_new_folded_scalar_hyphen_splits():
    baseline = load_baseline()
    new = [
        f"{rel}:{lineno}: {line}"
        for rel, lineno, line in scan_repo()
        if _baseline_key(rel, line) not in baseline
    ]
    assert not new, (
        "New YAML folded-scalar compound-word split(s) detected. A line inside "
        "a '>'/'>-' folded scalar ends in a hyphen, so folding inserts an "
        "unwanted space mid-compound. Reflow so the compound stays on one "
        "line:\n  " + "\n  ".join(new)
    )


def test_detector_catches_split_and_ignores_suspended_and_literal():
    bug = "d: >-\n  range from relapsing-\n  remitting forms.\n"
    suspended = "d: >-\n  in low-\n  and middle-income areas.\n"
    literal = "d: |\n  a code-\n  block line\n"
    assert list(find_violations_in_text(bug)), "should flag a folded split"
    assert not list(find_violations_in_text(suspended)), "suspended hyphen is OK"
    assert not list(find_violations_in_text(literal)), "literal block is not folded"


def test_detector_edge_cases():
    # Nested folded scalar under a list item (the common kb/ pattern).
    nested = "items:\n  - d: >-\n      pro-\n      inflammatory\n"
    assert list(find_violations_in_text(nested)), "should flag nested folded split"

    # Block-final hyphen: the next content line de-indents out of the block, so
    # folding inserts no space and this is NOT a bug.
    end_of_block = "d: >-\n  some word-\nnext_key: value\n"
    assert not list(find_violations_in_text(end_of_block)), \
        "block-final hyphen is not folded"

    # Multiple distinct splits within one block scalar.
    multi = "d: >-\n  relapsing-\n  remitting and chronic-\n  progressive\n"
    assert len(list(find_violations_in_text(multi))) == 2


# --- Status-marker guard (dismech#11820) -----------------------------------
#
# `is_status_marker` exempts a trailing hyphen that is a negativity marker
# rather than a split compound. Its failure mode is the opposite of the rest of
# this checker's: a false positive here is a MISSED finding, which is silent,
# where COORD_RE's is a noisy one a curator sees. So these tests pin the
# boundary in both directions -- what must stay exempt, and what must stay
# reportable -- because a later regex tweak could widen the exemption without
# anything going red.
#
# The three exempt cases are verbatim from lines the #4800 sweep wrongly
# joined before review caught them (PR #11760). The checker's own docstring
# says "four" because it counts source lines; these are three representative
# cases, one per rule.

EXEMPT = [
    # Rule 1: a '+' inside the token itself.
    "PI3K alpha-selective inhibitor approved for PIK3CA-mutated ER+/HER2-",
    # Rule 2: a '+'-suffixed sibling of the same stem on the line.
    "Biochemical control with fg-SRL treatment was similar in gsp+ and gsp-",
    # Rule 3: an all-uppercase run of >=3 short segments.
    "metabolic toxicity affects all lymphoid lineages, producing a T-B-NK-",
]

REPORTABLE = [
    # A genuine compound that MARKER_RUN_RE excludes twice over -- two segments
    # AND a digit -- so it pins neither half of the constraint on its own. Kept
    # because it is the ordinary shape this exemption must never swallow, and
    # because test_status_marker_guard_reaches_the_detector drives it end to end.
    "pharmacological blockade of IL-6-",
    # Three segments WITH a digit: `IL-2-R-mediated` is a genuine compound, and
    # it is the letters-only half of MARKER_RUN_RE that keeps it reportable --
    # the segment count alone does not. Without a case of this shape, relaxing
    # `[A-Z]` to `[A-Z0-9]` passes every other test in this file.
    "cytokine signaling through IL-2-R-",
    # A '+' elsewhere on the line is not marker notation. `cancer` never
    # appears '+'-suffixed, so the sibling rule must not fire.
    "Pediatric+adult WB-MRI surveillance trial that anchors the cancer-",
    # Two segments of bare uppercase letters. This is the only case here that
    # relaxing `{3,}` to `{2,}` would exempt, so it alone pins the segment count;
    # a two-segment case containing a digit cannot, being excluded by the
    # letters-only half regardless.
    "an otherwise unremarkable T-B-",
    # Digits in both segments as well as being two segments -- excluded twice
    # over, like `IL-6-` above, so likewise a reportable case rather than a pin.
    "receptor subunit CD8-1-",
    # The ordinary case the whole checker exists for.
    "Clinical courses range from relapsing-",
]


# Recording the trade-off this pins, so the IL-2-R- case is not misread: because
# MARKER_RUN_RE is letters-only, a genuine triple-negative immunophenotype written
# `CD3-CD4-CD8-` is NOT exempt and is reported as a folding bug. That is the safe
# direction -- a visible false positive rather than a silent miss -- and matches the
# module's stated trade-off. These tests pin current behaviour; they do not assert
# that digit-bearing marker runs are compounds.


def test_status_marker_exempts_negativity_markers():
    for line in EXEMPT:
        assert is_status_marker(line), f"should be exempt: {line!r}"


def test_status_marker_leaves_real_compounds_reportable():
    for line in REPORTABLE:
        assert not is_status_marker(line), f"should stay reportable: {line!r}"


def test_status_marker_rules_are_independently_pinned():
    """Each rule alone, so a change to one does not silently rest on another."""
    # Rule 1 without any sibling or uppercase run.
    assert is_status_marker("approved for ER+/HER2-")
    # Rule 2 without a '+' in the trailing token itself.
    assert is_status_marker("similar in gsp+ and gsp-")
    # Rule 3 without any '+' anywhere.
    assert is_status_marker("producing a T-B-NK-")


def test_plus_suffixed_sibling_respects_word_boundaries():
    """A stem that merely occurs *inside* a '+'-suffixed token must not exempt.

    `CD4+` contains the characters `D4+`, so a sibling rule without the `\\b`
    would wrongly exempt a line whose trailing token is `D4-`.
    """
    assert not is_status_marker("markers CD4+ and the unrelated D4-")


def test_status_marker_guard_reaches_the_detector():
    """The exemption must apply through find_violations_in_text, not just alone."""
    marker = "d: >-\n  approved for PIK3CA-mutated ER+/HER2-\n  metastatic breast cancer.\n"
    compound = "d: >-\n  pharmacological blockade of IL-6-\n  mediated signaling.\n"
    assert not list(find_violations_in_text(marker)), \
        "negativity marker should not be reported as a folding bug"
    assert list(find_violations_in_text(compound)), \
        "IL-6-mediated is a real split and must still be reported"

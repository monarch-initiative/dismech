"""Guard test: no NEW YAML folded-scalar compound-word splits in kb/.

A line inside a YAML folded ('>' / '>-') block scalar that ends in a hyphen is
folded into 'word- next', silently breaking a hyphenated compound (e.g.
'relapsing-remitting' -> 'relapsing- remitting'). A baseline grandfathers the
pre-existing backlog so this test fails only on newly introduced splits.

See scripts/check_folded_hyphens.py and dismech PR #4799.
"""
from pathlib import Path

from scripts.check_folded_hyphens import (
    find_violations_in_text,
    load_baseline,
    scan_repo,
    _baseline_key,
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

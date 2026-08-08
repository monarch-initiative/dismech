"""Tests for the reference-cache YAML-quoting normalization (PR #8203).

The `fix-references-cache` sweep runs before most reference-validation recipes,
so it must be a no-op on the committed cache. Before PR #8203 the predicate
quoted any value containing a colon and re-quoted ~9.9k of ~35.6k files on every
run (all `reference_id:`/`doi:` lines), which are valid unquoted plain scalars.
These tests pin the corrected predicate and guard the no-op invariant.
"""

import doctest
from pathlib import Path

import pytest

from dismech import reference_cache_quote
from dismech.reference_cache_quote import (
    files_needing_requote,
    needs_quoting,
    requote_frontmatter,
)

ROOT_DIR = Path(__file__).resolve().parents[1]
REFERENCES_CACHE_DIR = ROOT_DIR / "references_cache"


@pytest.mark.parametrize(
    "value",
    [
        "PMID:11390973",  # bare PREFIX:LOCALID colon
        "ORPHA:558",
        "10.1023/a:1022935115323",  # DOI with an embedded colon
        "Structural basis for FGFR2 activation.",
        "green",
        "-5 degrees",  # '-' not followed by whitespace
        "a/b/c",
    ],
)
def test_plain_scalars_are_left_unquoted(value):
    assert needs_quoting(value) is False


@pytest.mark.parametrize(
    "value",
    [
        "Title: a subtitle",  # ": " mapping ambiguity
        "ends with colon:",
        "[Cholera].",  # leading flow indicator
        "{braced}",
        "*star",
        "&anchor",
        "!tag",
        "@at",
        "#hash",
        "- dashspace",  # block-sequence marker
        "word #comment",  # inline comment start
        "trailing ",  # trailing whitespace
    ],
)
def test_ambiguous_values_are_quoted(value):
    assert needs_quoting(value) is True


def test_module_doctests_execute():
    # testpaths = ["tests"] means pytest never runs the module's own doctests;
    # execute them here so the `needs_quoting` examples stay load-bearing.
    results = doctest.testmod(reference_cache_quote, verbose=False)
    assert results.attempted > 0
    assert results.failed == 0


def test_mid_scalar_indicators_are_not_quoted():
    # Flow indicators are excluded from ns-plain-first but legal mid-scalar in
    # block context, so they must not trigger quoting when not leading.
    assert needs_quoting("Foo [bar] {baz} & qux * quux") is False


def test_requote_frontmatter_only_touches_ambiguous_lines():
    frontmatter = "\nreference_id: PMID:1\ntitle: Foo: bar\ndoi: 10.1/a:b\n"
    new, modified = requote_frontmatter(frontmatter)
    assert modified is True
    assert "reference_id: PMID:1" in new  # untouched
    assert "doi: 10.1/a:b" in new  # untouched
    assert 'title: "Foo: bar"' in new  # quoted


def test_already_quoted_values_are_left_as_is():
    frontmatter = '\nreference_id: "PMID:1"\n'
    new, modified = requote_frontmatter(frontmatter)
    assert modified is False
    assert new == frontmatter


@pytest.mark.skipif(
    not REFERENCES_CACHE_DIR.exists(), reason="references_cache/ not present"
)
def test_sweep_is_a_noop_on_the_committed_cache():
    """The whole-cache sweep must rewrite zero committed files (read-only check)."""
    offenders = files_needing_requote(REFERENCES_CACHE_DIR)
    assert offenders == [], (
        f"{len(offenders)} committed cache file(s) would be re-quoted by "
        f"fix-references-cache. The usual cause is a freshly fetched reference "
        f"whose title contains ': ' -- the fetcher writes it unquoted -- so the "
        f"fix is to run `just fix-references-cache` and stage the requoted "
        f"file(s), NOT to hand-edit them. If instead the quoting predicate in "
        f"dismech.reference_cache_quote was changed, that reintroduces the "
        f"normalization churn this guard exists to prevent -- revert it. "
        f"First few: {offenders[:10]}"
    )

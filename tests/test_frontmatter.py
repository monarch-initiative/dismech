"""Tests for delimiter-aware YAML frontmatter splitting (issue #7697).

The two titles exercised here are real, and they are the two distinct failure
modes: PMID:20881935 (quoted, MMWR ``Disease---Location, Year``) crashed the
reference validator outright, while PMID:1899320 (unquoted, pre-1996 NLM ASCII
arrow ``A----G(8344)``) parsed silently as truncated YAML and is committed on
``main``.
"""

from __future__ import annotations

from dismech.frontmatter import (
    contains_frontmatter_delimiter,
    naive_frontmatter_text,
    split_frontmatter,
)

# Quoted title: the naive split cuts inside the quoted scalar, so YAML raises.
MMWR_CACHE = (
    "---\n"
    'reference_id: "PMID:20881935"\n'
    'title: "Human rabies---Virginia, 2009."\n'
    "authors:\n"
    "- Centers for Disease Control and Prevention (CDC)\n"
    "journal: MMWR Morb Mortal Wkly Rep\n"
    "year: '2010'\n"
    "content_type: abstract_only\n"
    "---\n"
    "\n"
    "# Human rabies---Virginia, 2009.\n"
    "\n"
    "## Content\n"
    "\n"
    "The patient died on November 20.\n"
)

# Unquoted title: the naive split yields *valid* YAML, so nothing errors and the
# truncation is silent.
NLM_ARROW_CACHE = (
    "---\n"
    'reference_id: "PMID:1899320"\n'
    "title: Rapid detection of the A----G(8344) mutation of mtDNA.\n"
    "authors:\n"
    "- Zeviani M\n"
    "journal: Am J Hum Genet\n"
    "year: '1991'\n"
    "keywords:\n"
    "- Humans\n"
    "content_type: abstract_only\n"
    "---\n"
    "\n"
    "## Content\n"
    "\n"
    "Our study corroborates the idea that the mutation is widespread.\n"
)


def test_split_frontmatter_keeps_quoted_triple_hyphen_title_intact():
    split = split_frontmatter(MMWR_CACHE)
    assert split is not None
    assert 'title: "Human rabies---Virginia, 2009."' in split.frontmatter
    # Every field after the title survives.
    assert "content_type: abstract_only" in split.frontmatter
    assert split.body.lstrip().startswith("# Human rabies---Virginia, 2009.")


def test_split_frontmatter_keeps_unquoted_triple_hyphen_title_intact():
    split = split_frontmatter(NLM_ARROW_CACHE)
    assert split is not None
    assert "A----G(8344) mutation of mtDNA." in split.frontmatter
    for field in ("authors:", "journal:", "year:", "keywords:", "content_type:"):
        assert field in split.frontmatter
    assert "## Content" in split.body


def test_naive_split_is_the_thing_we_are_fixing():
    """Pin the broken behaviour so the fix cannot silently regress."""
    naive_mmwr = naive_frontmatter_text(MMWR_CACHE)
    assert naive_mmwr is not None
    # Cut mid-title, leaving an unterminated quote and dropping later fields.
    assert naive_mmwr.rstrip().endswith('title: "Human rabies')
    assert "content_type" not in naive_mmwr

    naive_arrow = naive_frontmatter_text(NLM_ARROW_CACHE)
    assert naive_arrow is not None
    assert naive_arrow.rstrip().endswith("title: Rapid detection of the A")
    assert "authors" not in naive_arrow

    # ... and both disagree with the correct reading, which is what the advisory
    # consumer-compatibility check keys on.
    assert naive_mmwr != split_frontmatter(MMWR_CACHE).frontmatter
    assert naive_arrow != split_frontmatter(NLM_ARROW_CACHE).frontmatter


def test_split_frontmatter_matches_only_a_delimiter_on_its_own_line():
    text = "---\ntitle: a---b\n---\nbody\n"
    split = split_frontmatter(text)
    assert split is not None
    assert split.frontmatter == "title: a---b"
    assert split.body == "body\n"


def test_split_frontmatter_tolerates_crlf_and_trailing_space():
    text = "--- \r\ntitle: x\r\n---\t\r\nbody\r\n"
    split = split_frontmatter(text)
    assert split is not None
    assert split.frontmatter == "title: x"
    assert split.body == "body\r\n"


def test_split_frontmatter_returns_none_without_frontmatter():
    assert split_frontmatter("# just a heading\n") is None
    assert split_frontmatter("---\nunterminated: true\n") is None
    assert naive_frontmatter_text("# just a heading\n") is None


def test_split_frontmatter_handles_closing_delimiter_at_eof():
    split = split_frontmatter("---\ntitle: x\n---")
    assert split is not None
    assert split.frontmatter == "title: x"
    assert split.body == ""


def test_split_frontmatter_handles_empty_block():
    split = split_frontmatter("---\n---\nbody\n")
    assert split is not None
    assert split.frontmatter == ""
    assert split.body == "body\n"


def test_split_frontmatter_does_not_close_on_a_value_ending_in_hyphens():
    """The empty-block allowance must not let a trailing ``---`` close the block.

    ``title: a---`` ends a *line* with the delimiter text. A regex that merely
    made the newline optional would accept that as the closing delimiter and
    drop every field after it -- the original bug, reintroduced.
    """
    split = split_frontmatter("---\ntitle: a---\nyear: '1991'\n---\nbody\n")
    assert split is not None
    assert split.frontmatter == "title: a---\nyear: '1991'"
    assert split.body == "body\n"


def test_contains_frontmatter_delimiter_walks_containers():
    assert contains_frontmatter_delimiter("A----G")
    assert not contains_frontmatter_delimiter("A--G")
    assert contains_frontmatter_delimiter(["fine", "not---fine"])
    assert contains_frontmatter_delimiter({"k": ["a", {"n": "x---y"}]})
    assert not contains_frontmatter_delimiter({"k": ["a", {"n": "xy"}]})
    assert not contains_frontmatter_delimiter(None)
    assert not contains_frontmatter_delimiter(1991)

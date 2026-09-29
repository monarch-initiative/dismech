"""The written title must survive linkml-reference-validator's own comparison.

lrv compares ``normalize_text(<yaml title>)`` against ``normalize_text(<RAW
frontmatter title>)``. Its ``normalize_text`` maps ``[^\\w\\s]`` to a *space*
rather than deleting it, so markup and HTML entities survive normalization as
words — ``<italic>TUBA1A</italic>`` becomes ``italic tuba1a italic``, not
``tuba1a``.

That makes the tidied form of a markup-bearing cached title a value lrv rejects.
These tests pin the invariant that keeps the title scripts and lrv agreeing:
whatever is written must normalize to the same thing as the raw cached title.

Regression guard for the defect found reviewing PR #9462, where the scripts
wrote ``clean_title(raw)`` unconditionally and measured drift with the same
tidied yardstick — which both hid 8 real mismatches and introduced 13 new ones.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from backfill_reference_titles import clean_title, resolve_title
from linkml_reference_validator.validation.supporting_text_validator import (
    SupportingTextValidator,
)

normalize = SupportingTextValidator.normalize_text

#: Real cached titles, taken verbatim from references_cache/ frontmatter.
MARKUP_BEARING = [
    # PMID:41171976 — the case that regressed TUBA1A-related_Tubulinopathy
    (
        "Prenatal Diagnosis of Tubulinopathy: Case Report of Neurosonographic "
        "Features and a Novel <italic>TUBA1A</italic> Variant."
    ),
    # PMID:35382378 — <em>, a different tag
    (
        "Association of <em>TNFAIP3</em> gene polymorphism (<em>rs5029939</em>) with "
        "susceptibility and clinical phenotype of systemic lupus erythematosus."
    ),
    # PPR:PPR1278294 — <i> plus doubled spaces
    (
        "An integrated computational, clinical, and functional framework for "
        "assessing  <i>PTPN11</i>  (SHP2) variant effects on ERK signaling"
    ),
    # an HTML entity rather than a tag: &amp; normalizes to the word "amp"
    "Guidance for Clinicians &amp; Laboratories",
]

PLAIN = [
    "Diagnosis and management of Guillain-Barré syndrome in ten steps.",
    "Abetalipoproteinemia",
    "Inborn errors in the metabolism of glutathione.",
]


@pytest.mark.parametrize("raw", MARKUP_BEARING + PLAIN)
def test_resolved_title_normalizes_to_the_raw_cached_title(raw):
    """The invariant lrv actually enforces. If this breaks, validation breaks."""
    assert normalize(resolve_title(raw)) == normalize(raw)


@pytest.mark.parametrize("raw", MARKUP_BEARING)
def test_markup_bearing_titles_are_written_raw(raw):
    """Tidying these would change what lrv sees, so the raw value must win."""
    assert resolve_title(raw) == raw
    # ...and the tidy really would have been rejected, i.e. the guard is load-bearing.
    assert normalize(clean_title(raw)) != normalize(raw)


@pytest.mark.parametrize("raw", PLAIN)
def test_plain_titles_keep_the_readable_tidy(raw):
    """Where tidying is equivalent, prefer it — accents and spacing still normalise."""
    assert resolve_title(raw) == clean_title(raw)


def test_frontmatter_is_read_the_way_lrv_reads_it(tmp_path):
    """A title lrv can read must not look title-less here.

    PubMed titles occasionally carry U+2028 / U+2029, which the fetcher writes
    into an unquoted scalar. ruamel (what lrv uses) accepts that; PyYAML treats
    them as line breaks and raises. Reading with PyYAML made PMID:27951541 look
    like it had no cached title, so its seven KB titles were skipped here while
    lrv was checking them.

    Built from a synthetic cache file rather than that live entry, so the pin
    survives a refetch of any one reference.
    """
    import yaml
    from backfill_reference_titles import build_title_index

    raw = "Pubertal Development in\u202817Beta-Hydroxysteroid Deficiency\u2029."
    (tmp_path / "PMID_1.md").write_text(
        f'---\nreference_id: "PMID:1"\ntitle: {raw}\n---\n\nbody\n',
        encoding="utf-8",
    )

    # The frontmatter really is PyYAML-hostile, so the assertion below is not vacuous.
    with pytest.raises(yaml.YAMLError):
        yaml.safe_load(f'reference_id: "PMID:1"\ntitle: {raw}\n')

    index = build_title_index(cache_dir=tmp_path)
    assert index.get("PMID:1") == raw


def test_unreadable_cache_entries_are_reported_not_swallowed(tmp_path, capsys):
    """An unreadable cache entry must announce itself, not look title-less.

    This is the tripwire for the next PMID:27951541. The failure mode it guards
    is a silent skip that is indistinguishable from a normal absence, so the
    guard is only worth having if it actually speaks up — pin all three branches.
    """
    from backfill_reference_titles import build_title_index, report_unreadable

    (tmp_path / "NO_BLOCK.md").write_text("no frontmatter here\n", encoding="utf-8")
    (tmp_path / "BAD_YAML.md").write_text(
        '---\nreference_id: "PMID:1"\ntitle: a: b: c\n  - nope\n---\n\nbody\n',
        encoding="utf-8",
    )
    (tmp_path / "NOT_A_MAP.md").write_text(
        "---\n- just\n- a list\n---\n\nbody\n", encoding="utf-8"
    )
    (tmp_path / "GOOD.md").write_text(
        '---\nreference_id: "PMID:2"\ntitle: A perfectly fine title\n---\n\nbody\n',
        encoding="utf-8",
    )

    unreadable: list[str] = []
    index = build_title_index(cache_dir=tmp_path, unreadable=unreadable)

    # The readable entry still lands; the three broken ones are named, not dropped.
    assert index == {"PMID:2": "A perfectly fine title"}
    assert len(unreadable) == 3
    reported = " ".join(unreadable)
    assert "NO_BLOCK.md" in reported and "no frontmatter block" in reported
    assert "BAD_YAML.md" in reported
    assert "NOT_A_MAP.md" in reported and "not a mapping" in reported

    report_unreadable(unreadable)
    err = capsys.readouterr().err
    assert "3 cache file(s) have unreadable frontmatter" in err
    assert "NO_BLOCK.md" in err

    # ...and it stays quiet when there is nothing to say.
    report_unreadable([])
    assert capsys.readouterr().err == ""


def test_cached_titles_in_repo_all_satisfy_the_invariant():
    """Every real cache entry must round-trip, not just the pinned samples."""
    from backfill_reference_titles import build_title_index

    offenders = [
        ref
        for ref, raw in build_title_index().items()
        if normalize(resolve_title(raw)) != normalize(raw)
    ]
    assert not offenders, f"resolve_title breaks lrv equality for: {offenders[:10]}"

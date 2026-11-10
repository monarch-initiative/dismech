"""Guard tests for abstract headings welded onto the next word (#16621).

See scripts/check_reference_cache_welded_headings.py for why a weld such as
``AbstractCastleman`` makes an accurate quote fail whole-word matching.
"""
from scripts.check_reference_cache_welded_headings import (
    CACHE_DIR,
    load_baseline,
    new_findings,
    shrunk_baseline,
    welded_headings,
)

FRONTMATTER = "---\nreference_id: DOI:10.1/x\ntitle: AbstractTitle Only\n---\n\n## Content\n\n"


def _write(tmp_path, name, body):
    path = tmp_path / name
    path.write_text(FRONTMATTER + body, encoding="utf-8")
    return path


def test_no_new_welded_headings_in_reference_cache():
    found = new_findings(welded_headings(), load_baseline())
    assert not found, "\n".join(
        f"{path.relative_to(CACHE_DIR.parent)}: {welds[:3]}" for path, welds in found.items()
    )


def test_baseline_lists_only_files_that_still_have_welds():
    found = welded_headings()
    assert shrunk_baseline(found, load_baseline()) == load_baseline(), (
        "baseline lists fixed files or overstated counts; run "
        "`just check-reference-cache-welded-headings --update-baseline`"
    )


def test_finds_the_reported_crossref_weld(tmp_path):
    path = _write(tmp_path, "DOI_1.md", "AbstractCastleman disease (CD) describes a group.")
    assert welded_headings(tmp_path) == {path: ["AbstractCa"]}


def test_finds_welds_after_a_sentence_end_and_a_label(tmp_path):
    path = _write(
        tmp_path,
        "DOI_2.md",
        "ImportanceThe question.ObjectiveTo test it. MethodsWe enrolled. Aim: ResultsAll.",
    )
    assert welded_headings(tmp_path)[path] == [
        "ImportanceTh",
        "ObjectiveTo",
        "MethodsWe",
        "ResultsAl",
    ]


def test_multi_word_headings_match_whole(tmp_path):
    path = _write(tmp_path, "DOI_3.md", "Conclusions and RelevanceIn this cohort.")
    assert welded_headings(tmp_path)[path] == ["Conclusions and RelevanceIn"]


def test_leaves_separated_and_mid_sentence_headings_alone(tmp_path):
    # The shapes a fresh fetch writes, an ordinary mid-sentence use, an all-caps
    # weld and a weld after a bracket (both of which upstream also leaves), and
    # the title in the frontmatter, which the check must not read.
    _write(
        tmp_path,
        "DOI_4.md",
        "Abstract\n\nCastleman disease.\n\nResults: The cohort. The Results were striking. "
        "Methodsical work. RESULTSThe cohort. exposures)Conclusions follow.",
    )
    assert welded_headings(tmp_path) == {}


def test_baseline_grandfathers_a_file_up_to_its_listed_count(tmp_path):
    path = _write(tmp_path, "PMID_5.md", "End. MethodsEnzymol 1. End. MethodsEnzymol 2.")
    found = welded_headings(tmp_path)
    root = path.parent.parent
    rel = str(path.relative_to(root))
    assert new_findings(found, {rel: 2}, root) == {}
    assert new_findings(found, {rel: 1}, root) == found
    assert new_findings(found, {}, root) == found


def test_baseline_only_shrinks(tmp_path):
    path = _write(tmp_path, "PMID_6.md", "End. MethodsEnzymol 1.")
    found = welded_headings(tmp_path)
    root = path.parent.parent
    rel = str(path.relative_to(root))
    # A fixed file drops out, an overstated count is lowered, and a file with
    # welds that the baseline never listed is not added.
    assert shrunk_baseline(found, {rel: 3, "gone.md": 1}, root) == {rel: 1}
    assert shrunk_baseline(found, {}, root) == {}

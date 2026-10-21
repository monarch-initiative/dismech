"""Guard test: no YAML structure swallowed into a string value in kb/ or src/.

An evidence item inserted inside a ``notes: >-`` block scalar parses as prose,
so the entry validates and the snippet count silently leaves the item out
(dismech #11230, hit on #11169). There is no baseline: every finding fails.

See scripts/check_folded_yaml.py.
"""

import pytest

from scripts.check_folded_yaml import (
    find_violations_in_text,
    main,
    scan_repo,
)

SWALLOWED = """\
name: Example
phenotypes:
- name: Intrauterine growth retardation
  evidence:
  - reference: PMID:20301283
    supports: SUPPORT
notes: >-
  Disease-level notes that run on for long enough to be a real paragraph,
  checked before the band is set.

  - reference: PMID:18074387
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "Almost 70% of patients weighed <or=2,500 g."
"""


@pytest.mark.ci_step_twin("scripts/check_folded_yaml.py")
def test_no_swallowed_yaml_structure():
    findings, _ = scan_repo()
    found = [f"{rel}: {path}: {line}" for rel, path, line in findings]
    assert not found, (
        "YAML structure swallowed into a string value. A string contains a "
        "line opening with a KB key, which usually means a block was inserted "
        "inside a block scalar. Move it out:\n  " + "\n  ".join(found)
    )


def test_swallowed_evidence_item_is_flagged():
    found = find_violations_in_text(SWALLOWED)
    assert found, "a swallowed evidence item must be flagged"
    assert {path for path, _ in found} == {"notes"}
    assert ("notes", "- reference: PMID:18074387") in found
    # The real evidence item on the phenotype is parsed structure, not prose.
    assert not any(path.startswith("phenotypes") for path, _ in found)


def test_swallowed_item_folded_onto_one_line_is_flagged():
    # Same indentation as the prose and no blank line: ``>-`` folds the whole
    # item into the paragraph, so no key opens a line.
    text = (
        "notes: >-\n"
        "  Prose long enough to count as a real paragraph of disease notes.\n"
        "  - reference: PMID:1\n"
        "  supports: SUPPORT\n"
        '  snippet: "x"\n'
    )
    assert find_violations_in_text(text) == [("notes", "- reference: PMID:1 supports:")]


def test_folded_item_led_by_reference_title_is_flagged():
    # In the KB the key after ``reference:`` is almost always
    # ``reference_title:``, so that is the commonest folded shape.
    text = (
        "notes: >-\n"
        "  Prose long enough to count as a real paragraph of disease notes.\n"
        "  - reference: PMID:1\n"
        "  reference_title: A study\n"
        "  supports: SUPPORT\n"
    )
    assert find_violations_in_text(text) == [
        ("notes", "- reference: PMID:1 reference_title:")
    ]


def test_prose_naming_a_reference_is_not_flagged():
    text = (
        "notes: >-\n"
        "  The reference: PMID:12345678 is a case series; it supports the\n"
        "  claim only indirectly, as the explanation on that item says.\n"
    )
    assert find_violations_in_text(text) == []


def test_swallowed_item_in_literal_scalar_is_flagged():
    text = (
        "description: |\n"
        "  A long literal description that keeps going past sixty characters.\n"
        '  snippet: "exact quote"\n'
    )
    assert find_violations_in_text(text) == [("description", 'snippet: "exact quote"')]


def test_key_mentioned_mid_line_is_not_flagged():
    text = (
        "description: >-\n"
        "  A long description that merely mentions the snippet: field and the\n"
        "  supports: SUPPORT grade in passing, and - reference: inline too.\n"
    )
    assert find_violations_in_text(text) == []


def test_short_values_are_not_flagged():
    assert find_violations_in_text('notes: "snippet: short"\n') == []


def test_nested_path_is_reported():
    text = (
        "phenotypes:\n"
        "- name: Seizures\n"
        "  notes: |\n"
        "    Some notes about this phenotype that are long enough to count.\n"
        "    - name: Another phenotype\n"
    )
    assert find_violations_in_text(text) == [
        ("phenotypes[0].notes", "- name: Another phenotype")
    ]


def test_exit_codes(tmp_path, capsys):
    bad = tmp_path / "bad.yaml"
    bad.write_text(SWALLOWED, encoding="utf-8")
    good = tmp_path / "good.yaml"
    good.write_text("name: Example\nnotes: >-\n  Plain prose only.\n", encoding="utf-8")

    assert main([str(bad)]) == 1
    assert main([str(good)]) == 0
    assert main(["--all", str(bad)]) == 0
    assert main(["--count", str(bad)]) == 0
    out = capsys.readouterr().out
    assert "notes: - reference: PMID:18074387" in out

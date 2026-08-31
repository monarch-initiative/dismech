"""Guard test: no KB value sits outside the permissible values of its slot's enum.

This is the schema-narrowing twin of the duplicate-key guard. Both catch a
defect that arrives by merge rather than by authoring: #10003 narrowed
``EvidenceItemSupportEnum`` while ~15 curation PRs carrying the retired
``PARTIAL`` were already open and green against their own base (issue #10061).

See scripts/check_enum_values.py for why the check is ungated and whole-KB, and
for what it deliberately skips (dynamic ontology enums, slots that are free text
in some class, other schemas' trees).
"""
from pathlib import Path

import pytest

from scripts.check_enum_values import (
    SCHEMA_DIR,
    TARGETS,
    _files_for,
    find_violations,
    tracked_slots,
)

pytestmark = pytest.mark.kb_data

ROOT = Path(__file__).resolve().parents[1]


def _scan() -> list[str]:
    findings: list[str] = []
    for schema_name, patterns in TARGETS:
        tracked = tracked_slots(SCHEMA_DIR / schema_name)
        for path in _files_for(patterns):
            from dismech.yaml_io import safe_load

            data = safe_load(path.read_text(encoding="utf-8"))
            for location, _slot, value in find_violations(data, tracked):
                findings.append(f"{path.relative_to(ROOT)}: {location} = {value!r}")
    return findings


def test_no_out_of_enum_values_in_kb():
    findings = _scan()
    assert not findings, (
        "KB value(s) outside their slot's enum. A value legal when written and "
        "illegal now means an enum was narrowed while the file was in flight; "
        "fix the value or restore the permissible value:\n  "
        + "\n  ".join(findings)
    )


def test_detector_fires_on_a_retired_value():
    """The shape of issue #10061: a retired enum value on an evidence item."""
    tracked = tracked_slots(SCHEMA_DIR / "dismech.yaml")
    assert "supports" in tracked, "supports must be tracked for this guard to matter"
    assert "PARTIAL" not in tracked["supports"], "PARTIAL was retired by #10003"

    broken = {
        "prevalence": [
            {"evidence": [{"reference": "PMID:1", "supports": "PARTIAL"}]},
        ]
    }
    assert list(find_violations(broken, tracked)) == [
        ("prevalence[0].evidence[0].supports", "supports", "PARTIAL")
    ]

    ok = {"prevalence": [{"evidence": [{"reference": "PMID:1", "supports": "SUPPORT"}]}]}
    assert not list(find_violations(ok, tracked))


def test_dynamic_ontology_enums_are_not_tracked():
    """reachable_from enums have no static values; they are term-validator's job."""
    tracked = tracked_slots(SCHEMA_DIR / "dismech.yaml")
    assert "disease_term" not in tracked
    assert "phenotype_term" not in tracked


def test_free_text_slots_are_not_tracked():
    """A slot name that is enum-bound in one class and free text in another is skipped.

    ``severity`` is enum-backed on descriptors but tolerated as free text on
    legacy phenotype summaries, so tracking the name would flag correct prose.
    """
    tracked = tracked_slots(SCHEMA_DIR / "dismech.yaml")
    assert "severity" not in tracked


def test_hypothesis_trees_are_checked_against_their_own_schema():
    """kb/hypotheses/ is not dismech.yaml's; the wrong schema invents 5 findings."""
    dismech_tracked = tracked_slots(SCHEMA_DIR / "dismech.yaml")
    assessment_tracked = tracked_slots(SCHEMA_DIR / "hypothesis_assessment.yaml")

    # `status: REPORTED_ONLY` is legal in an assessment and unknown to dismech.yaml.
    doc = {"claims": [{"status": "REPORTED_ONLY"}]}
    assert list(find_violations(doc, dismech_tracked)), "wrong schema would flag it"
    assert not list(find_violations(doc, assessment_tracked)), "own schema accepts it"

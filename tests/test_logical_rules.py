"""Unit tests for the pathophysiology logical-rule engine (cell/process coherence).

The rules answer a question no other gate asks: are the ontology bindings on a
single node consistent with *each other*? Two properties of the formulation are
load-bearing and easy to regress, so they are pinned here explicitly:

* a rule fires only when **every** cell type is disqualifying, so a node
  annotating both ends of a transition stays clean; and
* the rule is stated over *disqualifying* classes rather than a required one,
  so a gap in the Cell Ontology's is_a graph costs a missed finding rather than
  a false accusation. ``test_thin_is_a_chain_does_not_produce_a_finding``
  covers that with the two real terms that motivated it.
"""

from __future__ import annotations

import pathlib

import pytest

from dismech.logical_rules import (
    WAIVER_MIN_WORDS,
    WAIVER_PREFIX,
    Closures,
    Rule,
    RuleConfigError,
    closure_filename,
    evaluate_entry,
    evaluate_node,
    load_closures,
    load_rules,
    unusable_rules,
    waiver_error,
)

ROOT = pathlib.Path(__file__).resolve().parents[1]
PATH = pathlib.Path("kb/disorders/Test.yaml")

EMT_RULE = Rule(
    id="emt-without-epithelial-substrate",
    summary="",
    processes=("GO:0001837",),
    except_processes=("GO:0060317",),
    disqualifying_cell_classes=("CL:0002320", "CL:0000115"),
)

CLOSURES = Closures(
    members={
        "GO:0001837": {"GO:0001837", "GO:0060317", "GO:0003198"},
        "GO:0060317": {"GO:0060317", "GO:0003198"},
        "CL:0002320": {"CL:0002320", "CL:0000057", "CL:0000186"},
        "CL:0000115": {"CL:0000115", "CL:0000132"},
    },
    labels={
        "GO:0001837": "epithelial to mesenchymal transition",
        "CL:0000057": "fibroblast",
    },
)


def node(cells, processes, **extra):
    return {
        "name": "A Node",
        "cell_types": [{"term": {"id": c, "label": c}} for c in cells],
        "biological_processes": [{"term": {"id": p, "label": p}} for p in processes],
        **extra,
    }


def run(n, rule=EMT_RULE):
    return evaluate_node(n, [rule], CLOSURES, PATH)


def test_every_cell_type_disqualifying_is_a_finding():
    findings = run(node(["CL:0000057", "CL:0000186"], ["GO:0001837"]))
    assert [f.rule_id for f in findings] == ["emt-without-epithelial-substrate"]
    assert "CL:0000057" in findings[0].detail


def test_one_qualifying_cell_type_clears_the_node():
    """Both ends of a transition on one node is good curation, not a defect."""
    findings = run(node(["CL:0000322", "CL:0000186"], ["GO:0001837"]))
    assert findings == []


def test_thin_is_a_chain_does_not_produce_a_finding():
    """A cell CL cannot classify is silent, never accused.

    ``CL:0000646 basal cell`` and ``CL:0008036 extravillous trophoblast`` are
    textbook EMT substrates that CL does not assert under ``CL:0000066
    epithelial cell``. A requires-an-epithelial-cell rule would report both.
    """
    for cell in ("CL:0000646", "CL:0008036"):
        findings = run(node([cell], ["GO:0001837"]))
        assert findings == [], cell


def test_descendant_process_triggers_the_rule():
    findings = run(
        node(["CL:0000057"], ["GO:0003198"]),
        rule=Rule(
            id="r",
            summary="",
            processes=("GO:0001837",),
            disqualifying_cell_classes=("CL:0002320",),
        ),
    )
    assert len(findings) == 1


def test_except_processes_exempts_the_cardiac_subtree():
    """GO itself files endocardial-cushion EMT under EMT; that is not an error."""
    findings = run(node(["CL:0000132"], ["GO:0003198"]))
    assert findings == []


def test_node_without_cell_types_makes_no_substrate_claim():
    findings = run(node([], ["GO:0001837"]))
    assert findings == []


def test_unbound_cell_type_is_ignored():
    """A free-text cell type with no `term:` cannot be classified either way."""
    n = node(["CL:0000057"], ["GO:0001837"])
    n["cell_types"].append({"preferred_term": "some cell"})
    findings = run(n)
    assert len(findings) == 1


def test_missing_closure_is_reported_rather_than_passing_silently():
    """A rule that cannot run must not read as a clean node."""
    findings = evaluate_node(
        node(["CL:0000057"], ["GO:0001837"]), [EMT_RULE], Closures(), PATH
    )
    assert findings == []
    problems = unusable_rules([EMT_RULE], Closures())
    assert problems and "refresh-logical-rule-closures" in problems[0]


def test_unusable_rules_is_empty_when_every_closure_is_present():
    assert unusable_rules([EMT_RULE], CLOSURES) == []


def test_evaluate_entry_walks_every_node():
    entry = {
        "pathophysiology": [
            node(["CL:0000057"], ["GO:0001837"]),
            node(["CL:0000322"], ["GO:0001837"]),
            "not a mapping",
        ]
    }
    findings = evaluate_entry(entry, [EMT_RULE], CLOSURES, PATH)
    assert len(findings) == 1


class TestWaivers:
    def test_a_good_waiver_clears_the_finding(self):
        text = (
            f"{WAIVER_PREFIX} emt-without-epithelial-substrate. "
            + "word " * WAIVER_MIN_WORDS
        )
        findings = run(node(["CL:0000057"], ["GO:0001837"], review_notes=text))
        assert findings == []

    def test_absent_waiver_yields_the_ordinary_finding(self):
        findings = run(node(["CL:0000057"], ["GO:0001837"]))
        assert "every cell type" in findings[0].detail

    def test_waiver_for_a_different_rule_does_not_transfer(self):
        text = f"{WAIVER_PREFIX} some-other-rule. " + "word " * WAIVER_MIN_WORDS
        findings = run(node(["CL:0000057"], ["GO:0001837"], review_notes=text))
        assert len(findings) == 1
        assert "not 'emt-without-epithelial-substrate'" in findings[0].detail

    def test_sentinel_alone_does_not_waive(self):
        text = f"{WAIVER_PREFIX} emt-without-epithelial-substrate. Because."
        findings = run(node(["CL:0000057"], ["GO:0001837"], review_notes=text))
        assert len(findings) == 1
        assert "below the" in findings[0].detail

    def test_prose_merely_mentioning_the_phrase_does_not_waive(self):
        text = f"See the discussion of {WAIVER_PREFIX} elsewhere. " + "word " * 40
        findings = run(node(["CL:0000057"], ["GO:0001837"], review_notes=text))
        assert len(findings) == 1

    def test_notes_cannot_waive(self):
        """`notes:` is disease content; only `review_notes:` disposes of a rule."""
        text = (
            f"{WAIVER_PREFIX} emt-without-epithelial-substrate. "
            + "word " * WAIVER_MIN_WORDS
        )
        findings = run(node(["CL:0000057"], ["GO:0001837"], notes=text))
        assert len(findings) == 1

    def test_waiver_error_reports_absent_distinctly(self):
        assert waiver_error(None, "r") == "absent"
        assert waiver_error("", "r") == "absent"


class TestConfig:
    def test_shipped_config_parses(self):
        rules = load_rules()
        assert {r.id for r in rules} >= {"emt-without-epithelial-substrate"}
        for rule in rules:
            assert rule.summary, f"{rule.id} has no summary"
            assert rule.remediation, f"{rule.id} tells a curator nothing to do"

    def test_every_shipped_closure_root_is_cached(self):
        """A rule whose closure is missing is a check that silently cannot run."""
        rules = load_rules()
        roots = [root for rule in rules for root in rule.closure_roots]
        closures = load_closures(roots)
        missing = [root for root in roots if not closures.has_root(root)]
        assert not missing, f"run `just refresh-logical-rule-closures`: {missing}"

    def test_closures_are_reflexive(self):
        closures = load_closures(["GO:0001837"])
        assert closures.is_descendant("GO:0001837", "GO:0001837")

    def test_closure_files_are_not_named_terms_csv(self):
        """`term_cache_integrity` scans `cache/*/terms.csv` and would choke."""
        assert closure_filename("CL:0002320") == "CL_0002320.csv"
        assert not (ROOT / "cache" / "closure" / "terms.csv").exists()

    @pytest.mark.parametrize(
        "raw, expected",
        [
            ({}, "non-empty `rules:` list"),
            ({"rules": [{"summary": "x"}]}, "has no `id`"),
            (
                {
                    "rules": [
                        {
                            "id": "a",
                            "processes": ["GO:1"],
                            "disqualifying_cell_classes": ["CL:1"],
                        },
                        {
                            "id": "a",
                            "processes": ["GO:2"],
                            "disqualifying_cell_classes": ["CL:2"],
                        },
                    ]
                },
                "duplicate rule id",
            ),
            (
                {"rules": [{"id": "a", "disqualifying_cell_classes": ["CL:1"]}]},
                "names no `processes`",
            ),
            (
                {"rules": [{"id": "a", "processes": ["GO:1"]}]},
                "names no `disqualifying_cell_classes`",
            ),
        ],
    )
    def test_bad_config_is_rejected(self, tmp_path, raw, expected):
        import yaml

        path = tmp_path / "rules.yaml"
        path.write_text(yaml.safe_dump(raw))
        with pytest.raises(RuleConfigError, match=expected):
            load_rules(path)

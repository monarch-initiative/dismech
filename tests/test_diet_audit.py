"""Tests for the diet representation audit (both causal and intervention tracks)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SCRIPT_PATH = ROOT / "scripts" / "diet_audit.py"
SPEC = importlib.util.spec_from_file_location("diet_audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


def _write(tmp_path: Path, slug: str, body: str) -> Path:
    kb = tmp_path / "kb" / "disorders"
    kb.mkdir(parents=True, exist_ok=True)
    (kb / f"{slug}.yaml").write_text(
        f"name: {slug.replace('_', ' ')}\n{body}", encoding="utf-8"
    )
    return tmp_path


# --- evidence tiers -------------------------------------------------------


def test_human_clinical_support_with_snippet_is_the_top_tier():
    items = [
        {
            "reference": "PMID:1",
            "supports": "SUPPORT",
            "evidence_source": "HUMAN_CLINICAL",
            "snippet": "quoted finding",
        }
    ]
    assert audit._evidence_tier(items) == audit._TIER_HUMAN


def test_support_from_a_non_human_source_is_the_middle_tier():
    items = [
        {
            "reference": "PMID:1",
            "supports": "SUPPORT",
            "evidence_source": "MODEL_ORGANISM",
            "snippet": "quoted finding",
        }
    ]
    assert audit._evidence_tier(items) == audit._TIER_CITED


def test_support_without_a_snippet_does_not_count_as_cited():
    items = [{"reference": "PMID:1", "supports": "SUPPORT", "snippet": "  "}]
    assert audit._evidence_tier(items) == audit._TIER_UNCITED


def test_refute_alone_gets_its_own_tier_not_uncited():
    # A REFUTE item is real evidence and must not read as "uncited", but it
    # argues against the link, so it must not reach a SUPPORT tier either.
    items = [
        {
            "reference": "PMID:1",
            "supports": "REFUTE",
            "evidence_source": "HUMAN_CLINICAL",
            "snippet": "quoted finding",
        }
    ]
    assert audit._evidence_tier(items) == audit._TIER_REFUTE


def test_support_outranks_refute_on_the_same_entry():
    items = [
        {"supports": "REFUTE", "evidence_source": "HUMAN_CLINICAL", "snippet": "a"},
        {"supports": "SUPPORT", "evidence_source": "HUMAN_CLINICAL", "snippet": "b"},
    ]
    assert audit._evidence_tier(items) == audit._TIER_HUMAN


def test_refute_only_link_is_not_the_inverse_defect(tmp_path):
    # NELABA's real shape: lipoic acid recorded as INEFFECTIVE against the
    # mechanism it targets, with two snippet-backed REFUTE items. That is
    # correct curation -- flagging it would send a curator to fix a good entry.
    _write(
        tmp_path,
        "NELABA",
        """treatments:
- name: Lipoic acid supplementation (ineffective)
  target_mechanisms:
  - target: Lipoic Acid Synthesis Failure
  evidence:
  - reference: PMID:1
    supports: REFUTE
    evidence_source: HUMAN_CLINICAL
    snippet: supplementation did not improve outcomes
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.tier == audit._TIER_REFUTE
    assert item.linked
    assert not item.unevidenced_link  # the bug this guards
    assert not item.gap  # refuting evidence is not a reason to add a link


def test_missing_evidence_block_is_uncited():
    assert audit._evidence_tier(None) == audit._TIER_UNCITED
    assert audit._evidence_tier([]) == audit._TIER_UNCITED


# --- the two tracks stay independent --------------------------------------


def test_causal_and_intervention_are_counted_separately_for_the_same_food(tmp_path):
    # Phenylketonuria's real shape: meat as an exposure AND avoid-meat as a
    # prescription, both on FOODON:00001006. Two claims, not one duplicated.
    _write(
        tmp_path,
        "Phenylketonuria",
        """environmental:
- name: Mammalian Meat Intake
  food_source:
    preferred_term: mammalian meat food product
    term:
      id: FOODON:00001006
      label: mammalian meat food product
treatments:
- name: Protein-restricted diet
  treatment_term:
    preferred_term: dietary intervention
    term:
      id: NCIT:C15447
      label: Dietary Intervention
    dietary_modifications:
    - action: RESTRICT
      food:
        preferred_term: mammalian meat food product
        term:
          id: FOODON:00001006
          label: mammalian meat food product
""",
    )
    items = audit.collect(tmp_path)
    tracks = sorted(i.track for i in items)
    assert tracks == ["causal", "intervention"]
    # The shared CURIE must not collapse the two into one row.
    assert all(i.curies == ["FOODON:00001006"] for i in items)


# --- the gap the audit exists to find -------------------------------------


def test_cited_but_unlinked_entry_is_the_gap(tmp_path):
    _write(
        tmp_path,
        "Gout",
        """environmental:
- name: Beer Intake
  food_source:
    preferred_term: beer beverage
    term:
      id: FOODON:00001260
      label: beer beverage
  evidence:
  - reference: PMID:15014182
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: beer consumption confers a larger risk
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.tier == audit._TIER_HUMAN
    assert not item.linked
    assert item.gap
    assert not item.unevidenced_link


def test_linked_and_cited_entry_is_not_a_gap(tmp_path):
    _write(
        tmp_path,
        "Gout",
        """environmental:
- name: Beer Intake
  influences_mechanisms:
  - target: Hyperuricemia
  evidence:
  - reference: PMID:15014182
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: beer consumption confers a larger risk
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.linked and not item.gap and not item.unevidenced_link


def test_evidence_on_the_link_counts_as_cited(tmp_path):
    """The regression the reviewer caught: link evidence was never read.

    CLAUDE.md makes the link's own evidence the recommended place for
    "this exposure acts on this node", so an entry can be fully cited with no
    entry-level evidence block at all. Reading only the entry level called 17
    such edges unevidenced.
    """
    _write(
        tmp_path,
        "Chronic_Kidney_Disease",
        """environmental:
- name: High Sodium Diet
  influences_mechanisms:
  - target: Glomerular Hyperfiltration
    evidence:
    - reference: PMID:1
      supports: SUPPORT
      evidence_source: HUMAN_CLINICAL
      snippet: sodium loading raised single-nephron filtration
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.tier == audit._TIER_HUMAN
    assert item.linked
    assert not item.unevidenced_link  # the bug this guards


def test_intervention_link_evidence_also_counts(tmp_path):
    _write(
        tmp_path,
        "Dravet_syndrome",
        """treatments:
- name: Ketogenic Diet
  target_mechanisms:
  - target: Seizure Threshold
    evidence:
    - reference: PMID:2
      supports: SUPPORT
      evidence_source: HUMAN_CLINICAL
      snippet: seizure frequency fell on the ketogenic diet
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.tier == audit._TIER_HUMAN
    assert not item.unevidenced_link


def test_entry_with_evidence_nowhere_is_still_the_inverse_defect(tmp_path):
    _write(
        tmp_path,
        "Example",
        """environmental:
- name: Diet
  influences_mechanisms:
  - target: Barrier Dysfunction
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.unevidenced_link


def test_linked_but_uncited_entry_is_the_inverse_defect(tmp_path):
    # Already rendering in the mechanism graph with nothing behind it.
    _write(
        tmp_path,
        "Crohn_Disease",
        """environmental:
- name: Diet
  influences_mechanisms:
  - target: Barrier Dysfunction
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.unevidenced_link and not item.gap


# --- binding states -------------------------------------------------------


def test_a_food_block_with_no_term_is_partial_not_free_text(tmp_path):
    _write(
        tmp_path,
        "Example",
        """environmental:
- name: Dietary Copper
  food_source:
    preferred_term: copper-rich food
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.state == audit._STATE_PARTIAL


def test_unbound_food_component_is_free_text_not_an_error(tmp_path):
    # Gluten sits outside the FoodTerm root, so free text is the correct
    # outcome here, and the audit must classify rather than fail it.
    _write(
        tmp_path,
        "Celiac_Disease",
        """environmental:
- name: Gluten Exposure
  evidence:
  - reference: PMID:37332011
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: requiring genetic susceptibility and gluten exposure
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.state == audit._STATE_FREE_TEXT
    assert item.gap  # still a pathograph candidate despite being unbound


# --- match provenance and false positives ---------------------------------


def test_diet_word_only_in_a_treatment_description_does_not_match(tmp_path):
    # The regression this guards: ACE inhibitors matched on "sodium", and cleft
    # palate repair on "feeding", when descriptions were searched.
    _write(
        tmp_path,
        "Heart_Failure",
        """treatments:
- name: ACE Inhibitors
  description: Reduces afterload and promotes sodium excretion.
""",
    )
    assert audit.collect(tmp_path) == []


def test_ethanol_as_a_sclerosant_is_excluded(tmp_path):
    _write(
        tmp_path,
        "Hypertrophic_Cardiomyopathy",
        """treatments:
- name: Alcohol Septal Ablation
""",
    )
    assert audit.collect(tmp_path) == []


def test_description_only_causal_match_is_flagged_weak(tmp_path):
    _write(
        tmp_path,
        "Ependymoma",
        """environmental:
- name: High-dose ionizing radiation
  description: Unrelated to dietary factors.
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.matched_in == "description"
    assert item.weak_match


def test_causal_match_on_the_entry_name_is_strong(tmp_path):
    _write(
        tmp_path,
        "Coronary_Artery_Disease",
        """environmental:
- name: High-Fat Diet
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.matched_in == "name"
    assert not item.weak_match


def test_food_source_block_wins_over_a_prose_match(tmp_path):
    _write(
        tmp_path,
        "Gout",
        """environmental:
- name: Shellfish Intake
  food_source:
    preferred_term: shellfish food product
    term:
      id: FOODON:00001293
      label: shellfish food product
""",
    )
    (item,) = audit.collect(tmp_path)
    assert item.matched_in == "food_source"


# --- CLI ------------------------------------------------------------------


def test_audit_is_advisory_by_default(monkeypatch, capsys):
    monkeypatch.setattr(audit, "_REPO_ROOT", ROOT)
    assert audit.main([]) == 0
    assert "CAUSAL track" in capsys.readouterr().out


def test_strict_honours_the_track_filter(monkeypatch, tmp_path, capsys):
    # An unevidenced link on the intervention track only. `--track causal
    # --strict` must not fail on a defect the caller asked not to be shown.
    _write(
        tmp_path,
        "Example",
        """treatments:
- name: Ketogenic Diet
  target_mechanisms:
  - target: Seizure Threshold
""",
    )
    monkeypatch.setattr(audit, "_REPO_ROOT", tmp_path)
    assert audit.main(["--track", "causal", "--strict"]) == 0
    capsys.readouterr()
    assert audit.main(["--track", "intervention", "--strict"]) == 1
    assert "STRICT: 1" in capsys.readouterr().err

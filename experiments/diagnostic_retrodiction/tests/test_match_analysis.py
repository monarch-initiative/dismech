"""Tests for match.py and analysis.py on synthetic candidates (no model output involved)."""
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE))
import analysis  # noqa: E402
import match  # noqa: E402


def rubric(cid):
    return yaml.safe_load((HERE / "rubrics" / f"{cid}.yaml").read_text(encoding="utf-8"))


def cand(**kw):
    base = dict(analyte="", analyte_type="AUTOANTIBODY", specimen="serum", target="", mechanism="", rationale="",
                confidence=0.5, rank=1)
    return {**base, **kw}


def test_mcnemar_matches_readme_table():
    assert analysis.mcnemar_exact(5, 0) > 0.05          # 5 or fewer discordant: never significant
    assert analysis.mcnemar_exact(6, 0) < 0.05          # 6 needs 6:0
    assert analysis.mcnemar_exact(5, 1) > 0.05
    assert analysis.mcnemar_exact(9, 1) < 0.05          # 10 needs >= 9:1
    assert analysis.mcnemar_exact(8, 2) > 0.05
    assert analysis.mcnemar_exact(15, 5) < 0.05         # 20 needs >= 15:5
    assert analysis.mcnemar_exact(14, 6) > 0.05


def test_clopper_pearson_known_value():
    lo, hi = analysis.clopper_pearson(5, 10)
    assert abs(lo - 0.187) < 0.002 and abs(hi - 0.813) < 0.002


def test_auroc():
    assert analysis.auroc([0.9, 0.8], [0.1, 0.2]) == 1.0
    assert analysis.auroc([0.5], [0.5]) == 0.5


def test_t2_and_t4_for_pla2r():
    r = rubric("C029")
    s = match.score(r, [cand(analyte="anti-PLA2R antibodies", target="PLA2R1"),
                        cand(analyte="anti-podocyte antibody", target="nephrin"),
                        cand(analyte="anti-PLA2R antibodies", target="PLA2R1", specimen="urine")])
    assert [x["tier_auto"] for x in s] == ["T4", "none", "none"]


def test_copeptin_t2_and_avp_flagged_clinical():
    r = rubric("C057")
    s = match.score(r, [cand(analyte="copeptin", analyte_type="PROTEIN_LEVEL", specimen="plasma",
                             target="copeptin (C-terminal glycopeptide of pre-pro-vasopressin)"),
                        cand(analyte="arginine vasopressin (AVP)", analyte_type="PROTEIN_LEVEL", specimen="plasma",
                             target="AVP")])
    assert s[0]["T2"] is True
    assert s[1]["T2"] is False and "CLINICAL_T1_ONLY" in s[1]["needs_adjudication"]


def test_unreachable_t4_raises_alarm():
    r = rubric("C037")  # readiness no
    s = match.score(r, [cand(analyte="NMO-IgG", target="AQP4", specimen="serum")])
    assert "T4_UNREACHABLE" in s[0]["alarms"]


def test_negative_rubric_marks_false_positive():
    r = yaml.safe_load((HERE / "rubrics" / "N02.yaml").read_text(encoding="utf-8"))
    s = match.score(r, [cand(analyte="ESR")])
    assert s[0]["false_positive"] is True


def test_final_tier_ladder():
    assert match.final_tier({"T2": True, "tier_auto": "T2"}, {"T1": True, "T3": True}) == "T3"
    assert match.final_tier({"T2": False, "tier_auto": "none"}, {"T1": True}) == "T1"
    assert match.final_tier({"T2": True, "tier_auto": "T4"}, {"CLINICAL_T1_ONLY": True}) == "T1"


def test_case_outcome_aggregation():
    rows = []
    for rep in (1, 2):
        for run in (1, 2, 3):
            hit = (rep, run) in {(1, 1), (1, 2), (2, 1), (2, 2)}
            rows.append({"case_id": "C1", "arm": "A2", "replicate": rep, "run": run, "rank": 1,
                         "tier": "T2" if hit else "none"})
    o = analysis.case_outcomes(rows, "A2")["C1"]
    assert o["hit"] is True and o["any"] is True and abs(o["mean"] - 4 / 6) < 1e-9

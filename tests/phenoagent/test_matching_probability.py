"""Unit tests for diagnosis probability derivation."""

from phenoagent.matching import calculate_pr_is_diagnosis


def test_pr_is_diagnosis_multiplies_unique_explanations_only():
    run = {
        "explanations": [
            {
                "explanation_id": "NO_EXPLANATION",
                "estimated_probability": 0.0,
                "description": "default placeholder",
            },
            {
                "explanation_id": "EXP_A",
                "estimated_probability": 0.8,
                "description": "A",
            },
            {
                "explanation_id": "EXP_B",
                "estimated_probability": 0.5,
                "description": "B",
            },
        ],
        "matches": [
            {"explanation_for_no_match": "EXP_A"},
            {"explanation_for_no_match": "EXP_A"},  # reused explanation should only count once
            {"explanation_for_no_match": "EXP_B"},
            {"exact": True, "similarity_percent": 100.0},  # no explanation pointer, ignored
        ],
    }
    assert calculate_pr_is_diagnosis(run) == 0.4


def test_pr_is_diagnosis_is_one_when_no_explanations_are_referenced():
    run = {
        "explanations": [
            {
                "explanation_id": "NO_EXPLANATION",
                "estimated_probability": 0.0,
                "description": "default placeholder",
            }
        ],
        "matches": [
            {"exact": True, "similarity_percent": 100.0},
            {"exact": False, "case_is_broader": True, "similarity_percent": 75.0},
        ],
    }
    assert calculate_pr_is_diagnosis(run) == 1.0

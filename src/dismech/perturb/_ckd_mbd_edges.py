"""Hardcoded CKD-MBD causal edges.

These should eventually be extracted from the YAML's pathophysiology[].downstream
fields. For now they encode the causal graph from the proof-of-concept.
"""

from dismech.perturb.graph import CausalEdgeEnriched

CKD_MBD_CAUSAL_EDGES = [
    CausalEdgeEnriched("GFR_decline", "ECCPhos", "INCREASES", "Phosphate Retention"),
    CausalEdgeEnriched(
        "GFR_decline", "CYP27B1_activity", "DECREASES", "Calcitriol Deficiency"
    ),
    CausalEdgeEnriched("GFR_decline", "sKlotho", "DECREASES", "FGF23 Axis"),
    CausalEdgeEnriched("ECCPhos", "FGF23", "INCREASES", "FGF23 Axis"),
    CausalEdgeEnriched(
        "FGF23", "CYP27B1_activity", "DECREASES", "Calcitriol Deficiency"
    ),
    CausalEdgeEnriched("FGF23", "phosphaturia", "INCREASES", "FGF23 Axis"),
    CausalEdgeEnriched("sKlotho", "FGF23_signaling", "DECREASES", "FGF23 Axis"),
    CausalEdgeEnriched(
        "CYP27B1_activity", "Calcitriol", "DECREASES", "Calcitriol Deficiency"
    ),
    CausalEdgeEnriched(
        "Calcitriol", "Ca_absorption", "DECREASES", "Calcitriol Deficiency"
    ),
    CausalEdgeEnriched("Ca_absorption", "serum_Ca", "DECREASES", "Secondary HPT"),
    CausalEdgeEnriched("serum_Ca", "PTH", "INCREASES", "Secondary HPT"),
    CausalEdgeEnriched("ECCPhos", "PTH", "INCREASES", "Secondary HPT"),
    CausalEdgeEnriched("Calcitriol", "PTH", "INCREASES", "Secondary HPT"),
    CausalEdgeEnriched("PTH", "RANKL", "INCREASES", "RANKL/OPG Imbalance"),
    CausalEdgeEnriched("PTH", "OPG", "DECREASES", "RANKL/OPG Imbalance"),
    CausalEdgeEnriched("RANKL", "osteoclasts", "INCREASES", "RANKL/OPG Imbalance"),
    CausalEdgeEnriched(
        "osteoclasts", "bone_resorption", "INCREASES", "RANKL/OPG Imbalance"
    ),
    CausalEdgeEnriched("bone_resorption", "BMD", "DECREASES", "RANKL/OPG Imbalance"),
    CausalEdgeEnriched("ECCPhos", "VascCa", "INCREASES", "Vascular Calcification"),
    CausalEdgeEnriched("serum_Ca", "VascCa", "INCREASES", "Vascular Calcification"),
    CausalEdgeEnriched("sKlotho", "VascCa", "DECREASES", "Vascular Calcification"),
    CausalEdgeEnriched("VascCa", "SOST", "INCREASES", "Bone-Vascular Paradox"),
    CausalEdgeEnriched(
        "SOST", "osteoblast_activity", "DECREASES", "Bone-Vascular Paradox"
    ),
    CausalEdgeEnriched("CASR_variant", "PTH", "INCREASES", "Secondary HPT"),
    CausalEdgeEnriched(
        "CYP27B1_variant", "CYP27B1_activity", "DECREASES", "Calcitriol Deficiency"
    ),
    CausalEdgeEnriched(
        "CYP24A1_variant", "Calcitriol", "INCREASES", "Calcitriol Deficiency"
    ),
    CausalEdgeEnriched("KLOTHO_variant", "sKlotho", "DECREASES", "FGF23 Axis"),
    CausalEdgeEnriched(
        "SLC20A1_variant", "VascCa", "INCREASES", "Vascular Calcification"
    ),
    CausalEdgeEnriched("SOST_variant", "SOST", "DECREASES", "Bone-Vascular Paradox"),
    CausalEdgeEnriched("GPD1_variant", "FGF23", "DECREASES", "FGF23 Axis"),
]

"""Build a small, deliberately paired smoke test from real cached quotations.

Run from the repository root. Labels/rationales are agent-assessed expectations,
not independent curator ground truth. Altered claims/annotations are explicit.
"""

import json
from pathlib import Path

from dismech.classifier.evidence import iter_evidence
from dismech.reference_snippet_audit import (
    CachedReferenceIndex,
    PairOutcome,
    SnippetPair,
    check_pair,
    load_literal_bracket_patterns,
    DEFAULT_CONFIG,
)
from dismech.yaml_io import safe_load_path

OUT = Path("experiments/claim_evidence/2026-09-18/cases.jsonl")
CASES = []


def quote(slug, reference, contains):
    path = Path(f"kb/disorders/{slug}.yaml")
    for row in iter_evidence(safe_load_path(path)):
        if row["reference"] == reference and contains in row["input"]["snippet"]:
            return row["input"]["snippet"], f"{path}:{row['id']}"
    raise ValueError((slug, reference, contains))


def add(
    id,
    disease,
    claim,
    snippet,
    reference,
    origin,
    expected,
    reason,
    supports="SUPPORT",
    directness="DIRECT",
    explanation=None,
    kind="constructed_claim",
):
    CASES.append(
        {
            "id": id,
            "reference": reference,
            "origin": origin,
            "kind": kind,
            "expected": expected,
            "rationale": reason,
            "input": {
                "claim": {"description": claim},
                "context": {"disease": disease},
                "snippet": snippet,
                "supports": supports,
                "directness": directness,
                "explanation": explanation,
            },
        }
    )


def pair(prefix, disease, claim, snippet, reference, origin, reason):
    add(
        prefix + "_support", disease, claim, snippet, reference, origin, "MATCH", reason
    )
    add(
        prefix + "_wrong_refute",
        disease,
        claim,
        snippet,
        reference,
        origin,
        "MISMATCH",
        "Same supporting quotation, but direction deliberately changed to REFUTE.",
        supports="REFUTE",
    )


ref = "PMID:29776671"
text = " ".join(Path("references_cache/PMID_29776671.md").read_text().split())
start = text.index("Diabetic retinopathy (DR) is a major complication")
vision = text[start : text.index(". Vision loss", start) + 1]
start = text.index("Vision loss from DR can be prevented")
generic = text[start : text.index(". Designing", start) + 1]
origin = "docs/reports/eye-disorder-claim-evidence-review-2026-07-25.md (reconstructed claim)"
pair(
    "dr_vision",
    "Diabetic retinopathy",
    "Diabetic retinopathy causes vision loss in working middle-aged adults.",
    vision,
    ref,
    origin,
    "The snippet states the disease-phenotype association.",
)
for id, claim in [
    (
        "dr_laser",
        "Panretinal laser photocoagulation is a cost-effective treatment for diabetic retinopathy.",
    ),
    (
        "dr_progression",
        "Severe nonproliferative diabetic retinopathy progresses to proliferative disease in approximately 50% of patients within one year.",
    ),
    ("dr_vitrectomy", "Vitrectomy is a treatment for diabetic retinopathy."),
]:
    add(
        id,
        "Diabetic retinopathy",
        claim,
        generic,
        ref,
        origin,
        "MISMATCH",
        "Generic prevention statement does not establish this specific treatment or progression claim.",
        kind="review_reconstruction",
    )
add(
    "dr_no_evidence",
    "Diabetic retinopathy",
    "Vitrectomy is a treatment for diabetic retinopathy.",
    generic,
    ref,
    origin,
    "MATCH",
    "NO_EVIDENCE correctly states that the snippet does not bear on the specific claim.",
    supports="NO_EVIDENCE",
    directness=None,
)
add(
    "dr_laser_persuasive_explanation",
    "Diabetic retinopathy",
    "Panretinal laser photocoagulation is a cost-effective treatment for diabetic retinopathy.",
    generic,
    ref,
    origin,
    "MISMATCH",
    "An assertive curator explanation does not supply missing evidence.",
    explanation="This guideline explicitly confirms that panretinal photocoagulation is cost-effective.",
)

ref = "PMID:30391351"
snip, origin = quote(
    "IKK2_Deficiency", ref, "T-cell receptor excision circles were normal"
)
pair(
    "ikk_trec",
    "IKK2 deficiency (IKBKB)",
    "TREC newborn screening misses IKBKB deficiency cases.",
    snip,
    ref,
    origin,
    "The quoted sentence explicitly states that screening misses cases.",
)
add(
    "ikk_trec_valid_refute",
    "IKK2 deficiency (IKBKB)",
    "TREC newborn screening detects IKBKB deficiency cases.",
    snip,
    ref,
    origin,
    "MATCH",
    "The negative finding directly refutes the positive claim.",
    supports="REFUTE",
)
add(
    "ikk_trec_wrong_support",
    "IKK2 deficiency (IKBKB)",
    "TREC newborn screening detects IKBKB deficiency cases.",
    snip,
    ref,
    origin,
    "MISMATCH",
    "Snippet says screening misses cases, but annotation asserts support.",
)
text = Path("references_cache/PMID_30391351.md").read_text()
start = text.index("LikeIKBKBimmune deficiency")
comparator = text[start : text.index(" Similarly,", start)]
for disease, expected in [("IKBKB", "MISMATCH"), ("NFKBIA", "MATCH")]:
    add(
        "comparator_" + disease.lower(),
        disease + " immune deficiency",
        f"Pneumocystis pneumonitis was reported in patients with {disease} mutations.",
        comparator,
        ref,
        "https://github.com/monarch-initiative/dismech/issues/10751 (reconstruction)",
        expected,
        "The detailed infection list describes NFKBIA patients; the introductory comparison does not transfer every infection to IKBKB.",
        kind="review_reconstruction",
    )

ref = "PMID:33394739"
snip, origin = quote("Wilms_Tumor", ref, "Combined LOH 1p and 16q")
pair(
    "wilms_frequency",
    "Wilms tumor",
    "Combined LOH 1p and 16q occurs in only 5% of favorable-histology Wilms tumors.",
    snip,
    ref,
    origin,
    "The quote gives exactly this frequency and population.",
)
add(
    "wilms_inflated_frequency",
    "Wilms tumor",
    "Combined LOH 1p and 16q occurs in 70% of favorable-histology Wilms tumors.",
    snip,
    ref,
    origin,
    "MISMATCH",
    "The claimed 70% contradicts the quoted 5%.",
)

ref = "PMID:19796257"
snip, origin = quote("Brugada_Syndrome", ref, "Lead I electrocardiograms")
for directness, expected in [
    ("INDIRECT", "MATCH"),
    ("DIRECT", "MISMATCH"),
    (None, "MATCH"),
]:
    add(
        "scn3b_" + str(directness).lower(),
        "Brugada syndrome",
        "Loss of SCN3B function can impair cardiac conduction in humans.",
        snip,
        ref,
        origin,
        expected,
        "Mouse loss-of-function conduction findings provide an inferential mechanistic link, not direct observation in humans.",
        directness=directness,
    )
pair(
    "scn3b_mouse",
    "Scn3b knockout mouse model",
    "Scn3b knockout mice have slower heart rates than wild-type mice.",
    snip,
    ref,
    origin,
    "The quoted mouse result directly states this comparison.",
)

ref = "PMID:29959160"
snip, origin = quote("Brugada_Syndrome", ref, "Two curated genes in this study")
add(
    "scn3b_refute_indirect",
    "Brugada syndrome",
    "SCN3B L10P is a highly penetrant monogenic cause of Brugada syndrome.",
    snip,
    ref,
    origin,
    "MATCH",
    "Population frequency at or above disease prevalence argues against high penetrance by inference.",
    supports="REFUTE",
    directness="INDIRECT",
)
add(
    "scn3b_wrong_support",
    "Brugada syndrome",
    "SCN3B L10P is a highly penetrant monogenic cause of Brugada syndrome.",
    snip,
    ref,
    origin,
    "MISMATCH",
    "The frequency finding argues against rather than for the annotated causal claim.",
    directness="INDIRECT",
)

# Unmodified real KB evidence objects: check the extraction path too.
for slug, name in [
    ("IKK2_Deficiency", "Agammaglobulinemia"),
    ("Diabetic_Retinopathy", "Visual Impairment"),
]:
    for row in iter_evidence(safe_load_path(Path(f"kb/disorders/{slug}.yaml"))):
        if row["input"]["claim"].get("name") == name:
            CASES.append(
                {
                    **row,
                    "id": "original_" + slug.lower(),
                    "kind": "unmodified_kb",
                    "origin": f"kb/disorders/{slug}.yaml:{row['id']}",
                    "expected": "MATCH",
                    "rationale": "The quotation directly describes the named phenotype.",
                }
            )
            break
    else:
        raise ValueError(name)

index = CachedReferenceIndex(
    Path("references_cache"),
    literal_bracket_patterns=load_literal_bracket_patterns(DEFAULT_CONFIG),
)
for case in CASES:
    result = check_pair(
        index, SnippetPair(OUT, case["id"], case["reference"], case["input"]["snippet"])
    )
    assert result in {PairOutcome.VERIFIED, PairOutcome.VERIFIED_RELAXED}, (
        case["id"],
        result,
    )
    case["quote_check"] = result.value
OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in CASES))
print(f"Wrote {len(CASES)} cases; every quotation verified against the existing cache.")

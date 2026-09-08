# Severe Combined Immunodeficiency

Boomer grounding analysis for [`kb/disorders/Severe_Combined_Immunodeficiency.yaml`](../../../../kb/disorders/Severe_Combined_Immunodeficiency.yaml).

- **Entry term:** [`MONDO:0015974`](http://purl.obolibrary.org/obo/MONDO_0015974) severe combined immunodeficiency
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6
- **Mendelian selection:** KB_CATEGORY_MENDELIAN

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| X-linked SCID | `MONDO:0010315` | T-B+ severe combined immunodeficiency due to gamma chain deficiency | `AGREES` | ✓ DOID, NCIT, ORDO |
| ADA deficiency | `MONDO:0007064` | severe combined immunodeficiency, autosomal recessive, T cell-negative, B cell-negative, NK cell-negative, due to adenosine deaminase deficiency | `AGREES` | ✓ DOID, NCIT, ORDO |
| RAG1/RAG2 deficiency | `MONDO:0011086` | severe combined immunodeficiency, autosomal recessive, T cell-negative, B cell-negative, NK cell-positive | `AGREES` | ✓ DOID, ORDO |
| IL7R deficiency | `MONDO:0015701` | T-B+ severe combined immunodeficiency due to IL-7Ralpha deficiency | `AGREES` | ✓ ORDO |
| JAK3 deficiency | `MONDO:0010938` | T-B+ severe combined immunodeficiency due to JAK3 deficiency | `AGREES` | ✓ ORDO |
| Artemis deficiency | `MONDO:0011225` | severe combined immunodeficiency due to DCLRE1C deficiency | `AGREES` | ✓ DOID, ORDO |

## What boomer did

The solver has **not been run** for this input. No mapping acceptance,
retraction, posterior probability or global-consistency result is asserted.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

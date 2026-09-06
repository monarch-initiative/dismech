# Idiopathic Interstitial Pneumonia

Boomer grounding analysis for [`kb/disorders/Idiopathic_Interstitial_Pneumonia.yaml`](../../../../kb/disorders/Idiopathic_Interstitial_Pneumonia.yaml).

- **Entry term:** [`MONDO:0002429`](http://purl.obolibrary.org/obo/MONDO_0002429) idiopathic interstitial pneumonia
- **Grounded subtypes:** 8
- **Verdicts:** AGREES 8

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| IPF | `MONDO:0800504` | idiopathic pulmonary fibrosis | `AGREES` | ✓ ICD10CM, MESH, ORDO |
| iNSIP | `MONDO:0019622` | non-specific interstitial pneumonia | `AGREES` | ✓ DOID, NCIT, ORDO |
| COP | `MONDO:0015264` | cryptogenic organizing pneumonia | `AGREES` | ✓ DOID, ICD10CM, MESH, ORDO |
| AIP | `MONDO:0019203` | acute interstitial pneumonia | `AGREES` | ✓ DOID, ICD10CM, NCIT, ORDO |
| RB-ILD | `MONDO:0019204` | respiratory bronchiolitis-interstitial lung disease syndrome | `AGREES` | ✓ ORDO |
| DIP | `MONDO:0009887` | desquamative interstitial pneumonia | `AGREES` | ✓ DOID, ICD10CM, NCIT, ORDO |
| LIP | `MONDO:0009537` | lymphoid interstitial pneumonia | `AGREES` | ✓ DOID, NCIT, ORDO |
| IPPFE | `MONDO:0044633` | idiopathic pleuroparenchymal fibroelastosis | `AGREES` | ✓ ORDO |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

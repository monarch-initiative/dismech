# Centronuclear Myopathy

Boomer grounding analysis for [`kb/disorders/Centronuclear_Myopathy.yaml`](../../../../kb/disorders/Centronuclear_Myopathy.yaml).

- **Entry term:** [`MONDO:0018947`](http://purl.obolibrary.org/obo/MONDO_0018947) centronuclear myopathy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| XLMTM | `MONDO:0010683` | X-linked myotubular myopathy | `AGREES` | ✓ DOID, ICD10CM, ORDO |
| AD-CNM | `MONDO:0008048` | autosomal dominant centronuclear myopathy | `AGREES` | ✓ DOID, ORDO |
| AR-CNM | `MONDO:0009709` | myopathy, centronuclear, 2 | `AGREES` | ✓ DOID |
| RYR1-CNM | `MONDO:0015705` | autosomal recessive centronuclear myopathy | `AGREES` | ✓ DOID, ORDO, icd11f |
| SPEG-CNM | `MONDO:0014418` | myopathy, centronuclear, 5 | `AGREES` | ✓ DOID |

## What boomer did

**Status: `TIMED_OUT`**

The full joint search reached its time limit. Any assignment and posterior
below are provisional; this is not a completed consistency verdict.

High-prior rejections in the provisional candidate:

- `MONDO:0008048` ≡ `DOID:0111217`

## Files

- [`kb.yaml`](kb.yaml): unchanged input.
- [`solution.yaml`](solution.yaml): current machine-readable solver output.
- [`solution.md`](solution.md): rendered solver output.
- [`solve.json`](solve.json): input hash, configuration, and run status.

The search used the entire KB, with no hypothesis-dropping clique limit.

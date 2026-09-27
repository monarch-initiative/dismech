# Isolated Woolly Hair

Boomer grounding analysis for [`kb/disorders/Isolated_Woolly_Hair.yaml`](../../../../kb/disorders/Isolated_Woolly_Hair.yaml).

- **Entry term:** [`MONDO:0008686`](http://purl.obolibrary.org/obo/MONDO_0008686) isolated familial wooly hair disorder
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 2, SAME_TERM 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| ARWH1 | `MONDO:0800312` | wooly hair, autosomal recessive 1, with or without hypotrichosis | `AGREES` | — no shared vocabulary |
| ARWH2 | `MONDO:0008686` | isolated familial wooly hair disorder | `SAME_TERM` | ✓ DOID, ORDO |
| ADWH | `MONDO:0020717` | autosomal dominant wooly hair | `AGREES` | ✓ DOID |

## What boomer did

**Status: `TIMED_OUT`**

The full joint search reached its time limit. Any assignment and posterior
below are provisional; this is not a completed consistency verdict.

High-prior rejections in the provisional candidate:

- `dismech:Isolated_Woolly_Hair` ≡ `MONDO:0008686`

## Files

- [`kb.yaml`](kb.yaml): unchanged input.
- [`solution.yaml`](solution.yaml): current machine-readable solver output.
- [`solution.md`](solution.md): rendered solver output.
- [`solve.json`](solve.json): input hash, configuration, and run status.

The search used the entire KB, with no hypothesis-dropping clique limit.

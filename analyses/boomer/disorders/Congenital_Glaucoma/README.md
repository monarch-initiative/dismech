# Congenital Glaucoma

Boomer grounding analysis for [`kb/disorders/Congenital_Glaucoma.yaml`](../../../../kb/disorders/Congenital_Glaucoma.yaml).

- **Entry term:** [`MONDO:0020366`](http://purl.obolibrary.org/obo/MONDO_0020366) congenital glaucoma
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PCG | `MONDO:0000365` | primary congenital glaucoma | `AGREES` | ⚠ contradicted by DOID |
| GLC3A | `MONDO:0009277` | glaucoma 3A | `AGREES` | ✓ DOID, NCIT |
| GLC3B | `MONDO:0010968` | glaucoma 3, primary infantile, B | `AGREES` | silent (MESH) |
| GLC3C | `MONDO:0013121` | glaucoma 3, primary congenital, C | `AGREES` | — no shared vocabulary |
| GLC3D | `MONDO:0013122` | glaucoma 3, primary congenital, D | `AGREES` | silent (MESH) |
| GLC3E | `MONDO:0014998` | glaucoma 3, primary congenital, E | `AGREES` | — no shared vocabulary |

## What boomer did

**Status: `TIMED_OUT`**

The full joint search reached its time limit. Any assignment and posterior
below are provisional; this is not a completed consistency verdict.

High-prior rejections in the provisional candidate:

- `MONDO:0020366` ≡ `DOID:11212`

## Files

- [`kb.yaml`](kb.yaml): unchanged input.
- [`solution.yaml`](solution.yaml): current machine-readable solver output.
- [`solution.md`](solution.md): rendered solver output.
- [`solve.json`](solve.json): input hash, configuration, and run status.

The search used the entire KB, with no hypothesis-dropping clique limit.

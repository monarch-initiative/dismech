# Inherited Retinal Dystrophy

Boomer grounding analysis for [`kb/disorders/Inherited_Retinal_Dystrophy.yaml`](../../../../kb/disorders/Inherited_Retinal_Dystrophy.yaml).

- **Entry term:** [`MONDO:0019118`](http://purl.obolibrary.org/obo/MONDO_0019118) inherited retinal dystrophy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| RP | `MONDO:0019200` | retinitis pigmentosa | `AGREES` | ✓ MESH, NCIT, ORDO |
| LCA | `MONDO:0018998` | Leber congenital amaurosis | `AGREES` | ✓ ORDO |
| Cone-Rod Dystrophy | `MONDO:0015993` | cone-rod dystrophy | `AGREES` | ✓ MESH, ORDO |
| Choroideremia | `MONDO:0010557` | choroideremia | `AGREES` | silent (DOID, ICD10CM, MESH, NCIT, ORDO) |

MONDO proxy-merge exceptions: [annotations and decisions](proxy-merges.json).

## What boomer did

**Status: `TIMED_OUT`**

The full joint search reached its time limit. Any assignment and posterior
below are provisional; this is not a completed consistency verdict.

High-prior rejections in the provisional candidate:

- `MONDO:0019118` ≡ `NCIT:C35194`

## Files

- [`kb.yaml`](kb.yaml): unchanged input.
- [`solution.yaml`](solution.yaml): current machine-readable solver output.
- [`solution.md`](solution.md): rendered solver output.
- [`solve.json`](solve.json): input hash, configuration, and run status.

The search used the entire KB, with no hypothesis-dropping clique limit.

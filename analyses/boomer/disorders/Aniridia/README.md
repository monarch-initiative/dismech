# Aniridia

Boomer grounding analysis for [`kb/disorders/Aniridia.yaml`](../../../../kb/disorders/Aniridia.yaml).

- **Entry term:** [`MONDO:0019172`](http://purl.obolibrary.org/obo/MONDO_0019172) aniridia
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Isolated aniridia | `MONDO:0007119` | isolated aniridia | `AGREES` | — no shared vocabulary |
| WAGR | `MONDO:0008681` | WAGR syndrome | `SILENT` | ✓ MESH |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **WAGR** — MESH (MESH:D017624)

## What boomer did

**Status: `TIMED_OUT`**

The full joint search reached its time limit. Any assignment and posterior
below are provisional; this is not a completed consistency verdict.

## Files

- [`kb.yaml`](kb.yaml): unchanged input.
- [`solution.yaml`](solution.yaml): current machine-readable solver output.
- [`solution.md`](solution.md): rendered solver output.
- [`solve.json`](solve.json): input hash, configuration, and run status.

The search used the entire KB, with no hypothesis-dropping clique limit.

# Glycogen Storage Disease Type IX

Boomer grounding analysis for [`kb/disorders/Glycogen_Storage_Disease_Type_IX.yaml`](../../../../kb/disorders/Glycogen_Storage_Disease_Type_IX.yaml).

- **Entry term:** [`MONDO:0700291`](http://purl.obolibrary.org/obo/MONDO_0700291) glycogen storage disease IX
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| IXa1 | `MONDO:0010598` | glycogen storage disease IXa1 | `AGREES` | ✓ DOID |
| IXa2 | `MONDO:0100439` | glycogen storage disease IXa2 | `AGREES` | — no shared vocabulary |
| IXb | `MONDO:0009868` | glycogen storage disease IXb | `AGREES` | ✓ DOID, ORDO |
| IXc | `MONDO:0013091` | glycogen storage disease IXc | `AGREES` | ✓ DOID |
| IXd | `MONDO:0010362` | glycogen storage disease IXd | `SILENT` | ✓ DOID, ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **IXd** — DOID (DOID:0111040), ORDO (ORDO:715)

MONDO proxy-merge exceptions: [annotations and decisions](proxy-merges.json).

## What boomer did

**Status: `TIMED_OUT`**

The full joint search reached its time limit. Any assignment and posterior
below are provisional; this is not a completed consistency verdict.

High-prior rejections in the provisional candidate:

- `MONDO:0010598` ≡ `DOID:0111042`

## Files

- [`kb.yaml`](kb.yaml): unchanged input.
- [`solution.yaml`](solution.yaml): current machine-readable solver output.
- [`solution.md`](solution.md): rendered solver output.
- [`solve.json`](solve.json): input hash, configuration, and run status.

The search used the entire KB, with no hypothesis-dropping clique limit.

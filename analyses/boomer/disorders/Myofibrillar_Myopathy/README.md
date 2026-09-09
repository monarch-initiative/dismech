# Myofibrillar Myopathy

Boomer grounding analysis for [`kb/disorders/Myofibrillar_Myopathy.yaml`](../../../../kb/disorders/Myofibrillar_Myopathy.yaml).

- **Entry term:** [`MONDO:0018943`](http://purl.obolibrary.org/obo/MONDO_0018943) myofibrillar myopathy
- **Grounded subtypes:** 10
- **Verdicts:** AGREES 9, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MFM1 | `MONDO:0011076` | myofibrillar myopathy 1 | `AGREES` | ✓ DOID, ORDO |
| MFM2 | `MONDO:0012130` | myofibrillar myopathy 2 | `SILENT` | ✓ DOID, ORDO |
| MFM3 | `MONDO:0012215` | myofibrillar myopathy 3 | `AGREES` | ✓ DOID, ORDO |
| MFM4 | `MONDO:0012277` | myofibrillar myopathy 4 | `AGREES` | ✓ DOID, ORDO |
| MFM5 | `MONDO:0012289` | myofibrillar myopathy 5 | `AGREES` | ✓ DOID, ORDO |
| MFM6 | `MONDO:0013061` | myofibrillar myopathy 6 | `AGREES` | ✓ DOID, ORDO |
| MFM7 | `MONDO:0014922` | myofibrillar myopathy 7 | `AGREES` | ✓ DOID |
| MFM8 | `MONDO:0014993` | myofibrillar myopathy 8 | `AGREES` | ✓ DOID |
| MFM10 | `MONDO:0033620` | myofibrillar myopathy 10 | `AGREES` | ✓ DOID |
| MFM11 | `MONDO:0030927` | myofibrillar myopathy 11 | `AGREES` | ✓ DOID |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **MFM2** — DOID (DOID:0080093), ORDO (ORDO:399058)

## What boomer did

**Status: `TIMED_OUT`**

The full joint search reached its time limit. Any assignment and posterior
below are provisional; this is not a completed consistency verdict.

High-prior rejections in the provisional candidate:

- `MONDO:0012215` ≡ `MESH:C000598645`
- `MONDO:0012215` ≡ `MESH:C535906`
- `MONDO:0012215` ≡ `ORDO:268129`

## Files

- [`kb.yaml`](kb.yaml): unchanged input.
- [`solution.yaml`](solution.yaml): current machine-readable solver output.
- [`solution.md`](solution.md): rendered solver output.
- [`solve.json`](solve.json): input hash, configuration, and run status.

The search used the entire KB, with no hypothesis-dropping clique limit.

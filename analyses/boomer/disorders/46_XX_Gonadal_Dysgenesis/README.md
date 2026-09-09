# 46,XX Gonadal Dysgenesis

Boomer grounding analysis for [`kb/disorders/46_XX_Gonadal_Dysgenesis.yaml`](../../../../kb/disorders/46_XX_Gonadal_Dysgenesis.yaml).

- **Entry term:** [`MONDO:0009299`](http://purl.obolibrary.org/obo/MONDO_0009299) 46 XX gonadal dysgenesis
- **Grounded subtypes:** 11
- **Verdicts:** AGREES 10, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| ODG1 | `MONDO:0024463` | ovarian dysgenesis 1 | `AGREES` | ✓ DOID |
| ODG2 | `MONDO:0010349` | ovarian dysgenesis 2 | `AGREES` | ✓ DOID |
| ODG3 | `MONDO:0013689` | ovarian dysgenesis 3 | `AGREES` | ✓ DOID |
| ODG4 | `MONDO:0014520` | 46,XX ovarian dysgenesis-short stature syndrome | `SILENT` | ✓ DOID |
| ODG5 | `MONDO:0054666` | ovarian dysgenesis 5 | `AGREES` | ✓ DOID |
| ODG6 | `MONDO:0054850` | ovarian dysgenesis 6 | `AGREES` | ✓ DOID |
| ODG7 | `MONDO:0020857` | ovarian dysgenesis 7 | `AGREES` | ✓ DOID |
| ODG8 | `MONDO:0032590` | ovarian dysgenesis 8 | `AGREES` | ✓ DOID |
| ODG9 | `MONDO:0030506` | ovarian dysgenesis 9 | `AGREES` | ✓ DOID |
| ODG10 | `MONDO:0030736` | ovarian dysgenesis 10 | `AGREES` | ✓ DOID |
| ODG11 | `MONDO:0971176` | ovarian dysgenesis 11 | `AGREES` | — no shared vocabulary |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **ODG4** — DOID (DOID:0080496)

## What boomer did

**Status: `TIMED_OUT`**

The full joint search reached its time limit. Any assignment and posterior
below are provisional; this is not a completed consistency verdict.

High-prior rejections in the provisional candidate:

- `MONDO:0010349` ≡ `DOID:0080494`

## Files

- [`kb.yaml`](kb.yaml): unchanged input.
- [`solution.yaml`](solution.yaml): current machine-readable solver output.
- [`solution.md`](solution.md): rendered solver output.
- [`solve.json`](solve.json): input hash, configuration, and run status.

The search used the entire KB, with no hypothesis-dropping clique limit.

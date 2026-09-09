# Congenital Insensitivity to Pain

Boomer grounding analysis for [`kb/disorders/Congenital_Insensitivity_to_Pain.yaml`](../../../../kb/disorders/Congenital_Insensitivity_to_Pain.yaml).

- **Entry term:** [`MONDO:0015364`](http://purl.obolibrary.org/obo/MONDO_0015364) hereditary sensory and autonomic neuropathy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| HSAN IV | `MONDO:0009746` | hereditary sensory and autonomic neuropathy type 4 | `AGREES` | ✓ DOID, ORDO, icd11f |
| HSAN V | `MONDO:0012092` | hereditary sensory and autonomic neuropathy type 5 | `AGREES` | ✓ DOID, ORDO, icd11f |
| SCN9A AR-CIP | `MONDO:0009459` | channelopathy-associated congenital insensitivity to pain, autosomal recessive | `SILENT` | ✓ ORDO |
| HSAN VII | `MONDO:0014244` | hereditary sensory and autonomic neuropathy type 7 | `AGREES` | ✓ DOID, ORDO |
| HSAN VIII | `MONDO:0014662` | congenital insensitivity to pain-hypohidrosis syndrome | `AGREES` | ✓ DOID, ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **SCN9A AR-CIP** — ORDO (ORDO:88642)

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

# PTEN Hamartoma Tumor Syndrome

Boomer grounding analysis for [`kb/disorders/PTEN_Hamartoma_Tumor_Syndrome.yaml`](../../../../kb/disorders/PTEN_Hamartoma_Tumor_Syndrome.yaml).

- **Entry term:** [`MONDO:0017623`](http://purl.obolibrary.org/obo/MONDO_0017623) PTEN hamartoma tumor syndrome
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 3, SILENT 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Cowden syndrome | `MONDO:0016063` | Cowden disease | `SILENT` | ✓ NCIT, ORDO |
| Bannayan-Riley-Ruvalcaba syndrome | `MONDO:0007924` | Bannayan-Riley-Ruvalcaba syndrome | `AGREES` | ✓ NCIT, ORDO |
| Proteus-like syndrome | `MONDO:0017571` | Proteus-like syndrome | `AGREES` | ✓ NCIT, ORDO |
| Lhermitte-Duclos disease | `MONDO:0019002` | Lhermitte-Duclos disease | `SILENT` | ✓ ORDO |
| SOLAMEN syndrome | `MONDO:0015293` | segmental outgrowth-lipomatosis-arteriovenous malformation-epidermal nevus syndrome | `AGREES` | ✓ ORDO |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **Cowden syndrome** — NCIT (NCIT:C3076), ORDO (ORDO:201)
- **Lhermitte-Duclos disease** — ORDO (ORDO:65285)

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

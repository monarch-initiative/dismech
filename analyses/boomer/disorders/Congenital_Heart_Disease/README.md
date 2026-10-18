# Congenital Heart Disease

Boomer grounding analysis for [`kb/disorders/Congenital_Heart_Disease.yaml`](../../../../kb/disorders/Congenital_Heart_Disease.yaml).

- **Entry term:** [`MONDO:0005453`](http://purl.obolibrary.org/obo/MONDO_0005453) congenital heart disease
- **Grounded subtypes:** 4
- **Verdicts:** SILENT 2, AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CTD | `MONDO:0016581` | conotruncal heart malformations | `SILENT` | — no shared vocabulary |
| AVSD | `MONDO:0859565` | atrioventricular septal defect | `AGREES` | — no shared vocabulary |
| HTX | `MONDO:0018677` | visceral heterotaxy | `SILENT` | ✓ icd11f |
| APVR | `MONDO:0017705` | congenital pulmonary venous return anomaly | `AGREES` | — no shared vocabulary |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **HTX** — icd11f (icd11f:780273165)

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0018677` ≡ `ORDO:157769`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

2 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

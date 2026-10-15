# Congenital Hydrocephalus

Boomer grounding analysis for [`kb/disorders/Congenital_Hydrocephalus.yaml`](../../../../kb/disorders/Congenital_Hydrocephalus.yaml).

- **Entry term:** [`MONDO:0016349`](http://purl.obolibrary.org/obo/MONDO_0016349) congenital hydrocephalus
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| HSAS | `MONDO:0010611` | X-linked hydrocephalus with stenosis of the aqueduct of Sylvius | `AGREES` | ✓ icd11f |
| HYC1 | `MONDO:0009360` | hydrocephalus, nonsyndromic, autosomal recessive 1 | `AGREES` | — no shared vocabulary |
| HYC2 | `MONDO:0014085` | hydrocephalus, nonsyndromic, autosomal recessive 2 | `AGREES` | — no shared vocabulary |
| HYC3 | `MONDO:0054794` | hydrocephalus, congenital, 3, with brain anomalies | `AGREES` | — no shared vocabulary |
| Dandy-Walker-associated | `MONDO:0017110` | isolated Dandy-Walker malformation with hydrocephalus | `SILENT` | silent (ORDO) |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
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

# Pyruvate Dehydrogenase Deficiency

Boomer grounding analysis for [`kb/disorders/Pyruvate_Dehydrogenase_Deficiency.yaml`](../../../../kb/disorders/Pyruvate_Dehydrogenase_Deficiency.yaml).

- **Entry term:** [`MONDO:0019169`](http://purl.obolibrary.org/obo/MONDO_0019169) pyruvate dehydrogenase deficiency
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| E1-alpha deficiency | `MONDO:0010717` | pyruvate dehydrogenase E1-alpha deficiency | `AGREES` | ✓ ORDO |
| E1-beta deficiency | `MONDO:0013580` | pyruvate dehydrogenase E1-beta deficiency | `AGREES` | ✓ ORDO |
| E2 deficiency | `MONDO:0009502` | pyruvate dehydrogenase E2 deficiency | `AGREES` | ✓ ORDO |
| E3 deficiency | `MONDO:0009529` | pyruvate dehydrogenase E3 deficiency | `AGREES` | ✓ ORDO |
| E3-binding protein deficiency | `MONDO:0009503` | pyruvate dehydrogenase E3-binding protein deficiency | `AGREES` | ✓ ORDO |
| PDH phosphatase deficiency | `MONDO:0012120` | pyruvate dehydrogenase phosphatase deficiency | `AGREES` | ✓ ORDO, icd11f |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

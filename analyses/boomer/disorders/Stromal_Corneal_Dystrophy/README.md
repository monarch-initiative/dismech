# Stromal Corneal Dystrophy

Boomer grounding analysis for [`kb/disorders/Stromal_Corneal_Dystrophy.yaml`](../../../../kb/disorders/Stromal_Corneal_Dystrophy.yaml).

- **Entry term:** [`MONDO:0020213`](http://purl.obolibrary.org/obo/MONDO_0020213) stromal corneal dystrophy
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MCD | `MONDO:0009020` | macular corneal dystrophy | `AGREES` | ✓ DOID, ORDO, icd11f |
| SCCD | `MONDO:0007374` | Schnyder corneal dystrophy | `AGREES` | ✓ DOID, ORDO |
| CSCD | `MONDO:0012401` | congenital stromal corneal dystrophy | `AGREES` | ✓ DOID, ORDO, icd11f |
| GCD1 | `MONDO:0007377` | granular corneal dystrophy type I | `AGREES` | ✓ ORDO |
| GCD2 | `MONDO:0011855` | granular corneal dystrophy type II | `AGREES` | ✓ ORDO |
| LCD1 | `MONDO:0007380` | lattice corneal dystrophy type I | `AGREES` | ✓ ORDO |

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

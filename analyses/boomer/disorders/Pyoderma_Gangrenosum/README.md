# Pyoderma Gangrenosum

Boomer grounding analysis for [`kb/disorders/Pyoderma_Gangrenosum.yaml`](../../../../kb/disorders/Pyoderma_Gangrenosum.yaml).

- **Entry term:** [`MONDO:0018824`](http://purl.obolibrary.org/obo/MONDO_0018824) pyoderma gangrenosum
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Ulcerative | `MONDO:0035235` | classic pyoderma gangrenosum | `AGREES` | ✓ ORDO |
| Bullous | `MONDO:0035237` | bullous pyoderma gangrenosum | `AGREES` | ✓ ORDO |
| Pustular | `MONDO:0035236` | pustular pyoderma gangrenosum | `AGREES` | ✓ ORDO |
| Vegetative | `MONDO:0035238` | vegetative pyoderma gangrenosum | `AGREES` | ✓ ORDO |

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

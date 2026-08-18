# Meier-Gorlin syndrome

Boomer grounding analysis for [`kb/disorders/Meier-Gorlin_Syndrome.yaml`](../../../../kb/disorders/Meier-Gorlin_Syndrome.yaml).

- **Entry term:** [`MONDO:0016817`](http://purl.obolibrary.org/obo/MONDO_0016817) Meier-Gorlin syndrome
- **Grounded subtypes:** 9
- **Verdicts:** AGREES 9

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MGORS1 | `MONDO:0009143` | Meier-Gorlin syndrome 1 | `AGREES` | ✓ DOID |
| MGORS2 | `MONDO:0013428` | Meier-Gorlin syndrome 2 | `AGREES` | ✓ DOID |
| MGORS3 | `MONDO:0013430` | Meier-Gorlin syndrome 3 | `AGREES` | ✓ DOID |
| MGORS4 | `MONDO:0013431` | Meier-Gorlin syndrome 4 | `AGREES` | ✓ DOID |
| MGORS5 | `MONDO:0013432` | Meier-Gorlin syndrome 5 | `AGREES` | ✓ DOID |
| MGORS6 | `MONDO:0014794` | Meier-Gorlin syndrome 6 | `AGREES` | ✓ DOID |
| MGORS7 | `MONDO:0014894` | Meier-Gorlin syndrome 7 | `AGREES` | ✓ DOID |
| MGORS8 | `MONDO:0033046` | Meier-Gorlin syndrome 8 | `AGREES` | ✓ DOID |
| MGORS9 | `MONDO:0980992` | Meier-Gorlin syndrome 9 | `AGREES` | silent (DOID) |

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

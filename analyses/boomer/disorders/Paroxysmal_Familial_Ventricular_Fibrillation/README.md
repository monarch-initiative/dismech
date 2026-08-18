# Paroxysmal Familial Ventricular Fibrillation

Boomer grounding analysis for [`kb/disorders/Paroxysmal_Familial_Ventricular_Fibrillation.yaml`](../../../../kb/disorders/Paroxysmal_Familial_Ventricular_Fibrillation.yaml).

- **Entry term:** [`MONDO:0100234`](http://purl.obolibrary.org/obo/MONDO_0100234) paroxysmal familial ventricular fibrillation
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type 1 | `MONDO:0011376` | ventricular fibrillation, paroxysmal familial, type 1 | `AGREES` |
| Type 2 | `MONDO:0013063` | ventricular fibrillation, paroxysmal familial, 2 | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

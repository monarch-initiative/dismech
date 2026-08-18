# Maple Syrup Urine Disease

Boomer grounding analysis for [`kb/disorders/Maple_Syrup_Urine_Disease.yaml`](../../../../kb/disorders/Maple_Syrup_Urine_Disease.yaml).

- **Entry term:** [`MONDO:0009563`](http://purl.obolibrary.org/obo/MONDO_0009563) maple syrup urine disease
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type IA | `MONDO:0023691` | maple syrup urine disease type 1A | `AGREES` |
| Type IB | `MONDO:0023692` | maple syrup urine disease type 1B | `AGREES` |
| Type II | `MONDO:0023693` | maple syrup urine disease type 2 | `AGREES` |

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

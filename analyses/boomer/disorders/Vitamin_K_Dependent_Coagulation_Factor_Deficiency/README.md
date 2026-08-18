# Vitamin K-Dependent Coagulation Factor Deficiency

Boomer grounding analysis for [`kb/disorders/Vitamin_K_Dependent_Coagulation_Factor_Deficiency.yaml`](../../../../kb/disorders/Vitamin_K_Dependent_Coagulation_Factor_Deficiency.yaml).

- **Entry term:** [`MONDO:0015722`](http://purl.obolibrary.org/obo/MONDO_0015722) congenital vitamin K-dependent coagulation factors deficiency
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| VKCFD1 | `MONDO:0010187` | vitamin K-dependent clotting factors, combined deficiency of, type 1 | `AGREES` |
| VKCFD2 | `MONDO:0011837` | vitamin K-dependent clotting factors, combined deficiency of, type 2 | `AGREES` |

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

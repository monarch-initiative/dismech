# Hyperinsulinemic Hypoglycemia

Boomer grounding analysis for [`kb/disorders/Hyperinsulinemic_Hypoglycemia.yaml`](../../../../kb/disorders/Hyperinsulinemic_Hypoglycemia.yaml).

- **Entry term:** [`MONDO:0005803`](http://purl.obolibrary.org/obo/MONDO_0005803) hyperinsulinemic hypoglycemia
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Diffuse HI | `MONDO:0015625` | diazoxide-resistant diffuse hyperinsulinism | `AGREES` |
| Focal HI | `MONDO:0019265` | diazoxide-resistant focal hyperinsulinism | `AGREES` |
| HI/HA Syndrome | `MONDO:0011717` | hyperinsulinism-hyperammonemia syndrome | `AGREES` |
| Diazoxide-Unresponsive HI | `MONDO:0017186` | diazoxide-resistant hyperinsulinism | `AGREES` |

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

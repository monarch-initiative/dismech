# Diabetic Retinopathy

Boomer grounding analysis for [`kb/disorders/Diabetic_Retinopathy.yaml`](../../../../kb/disorders/Diabetic_Retinopathy.yaml).

- **Entry term:** [`MONDO:0005266`](http://purl.obolibrary.org/obo/MONDO_0005266) diabetic retinopathy
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Nonproliferative Diabetic Retinopathy | `MONDO:0001661` | background diabetic retinopathy | `AGREES` |
| Severe Nonproliferative Diabetic Retinopathy | `MONDO:0004687` | severe nonproliferative diabetic retinopathy | `AGREES` |
| Proliferative Diabetic Retinopathy | `MONDO:0001660` | proliferative diabetic retinopathy | `AGREES` |

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

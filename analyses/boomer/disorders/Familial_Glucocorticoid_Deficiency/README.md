# Familial Glucocorticoid Deficiency

Boomer grounding analysis for [`kb/disorders/Familial_Glucocorticoid_Deficiency.yaml`](../../../../kb/disorders/Familial_Glucocorticoid_Deficiency.yaml).

- **Entry term:** [`MONDO:0008733`](http://purl.obolibrary.org/obo/MONDO_0008733) familial glucocorticoid deficiency
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| FGD1 | `MONDO:0024536` | glucocorticoid deficiency 1 | `AGREES` | ✓ DOID |
| FGD2 | `MONDO:0011826` | glucocorticoid deficiency 2 | `AGREES` | ✓ NCIT |
| FGD3 | `MONDO:0012214` | glucocorticoid deficiency 3 | `AGREES` | silent (MESH) |
| FGD4 | `MONDO:0013874` | glucocorticoid deficiency 4 | `AGREES` | ✓ NCIT |
| FGD5 | `MONDO:0040502` | glucocorticoid deficiency 5 | `AGREES` | silent (DOID) |

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

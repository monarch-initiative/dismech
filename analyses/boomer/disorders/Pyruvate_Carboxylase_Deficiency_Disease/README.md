# Pyruvate Carboxylase Deficiency Disease

Boomer grounding analysis for [`kb/disorders/Pyruvate_Carboxylase_Deficiency_Disease.yaml`](../../../../kb/disorders/Pyruvate_Carboxylase_Deficiency_Disease.yaml).

- **Entry term:** [`MONDO:0009949`](http://purl.obolibrary.org/obo/MONDO_0009949) pyruvate carboxylase deficiency disease
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type A | `MONDO:0018141` | pyruvate carboxylase deficiency, infantile form | `AGREES` | ✓ ORDO |
| Type B | `MONDO:0018142` | pyruvate carboxylase deficiency, severe neonatal type | `AGREES` | ✓ ORDO |
| Type C | `MONDO:0018143` | pyruvate carboxylase deficiency, benign type | `AGREES` | ✓ ORDO |

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

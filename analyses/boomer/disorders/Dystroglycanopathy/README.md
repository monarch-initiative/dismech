# Dystroglycanopathy

Boomer grounding analysis for [`kb/disorders/Dystroglycanopathy.yaml`](../../../../kb/disorders/Dystroglycanopathy.yaml).

- **Entry term:** [`MONDO:0018276`](http://purl.obolibrary.org/obo/MONDO_0018276) muscular dystrophy-dystroglycanopathy
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type A (Walker-Warburg syndrome / Muscle-Eye-Brain disease) | `MONDO:0000171` | muscular dystrophy-dystroglycanopathy, type A | `AGREES` |
| Type B (Congenital muscular dystrophy with intellectual disability) | `MONDO:0000172` | muscular dystrophy-dystroglycanopathy, type B | `AGREES` |
| Type C (Limb-girdle muscular dystrophy) | `MONDO:0000173` | muscular dystrophy-dystroglycanopathy, type C | `AGREES` |

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

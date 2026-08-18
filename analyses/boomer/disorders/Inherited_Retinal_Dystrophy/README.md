# Inherited Retinal Dystrophy

Boomer grounding analysis for [`kb/disorders/Inherited_Retinal_Dystrophy.yaml`](../../../../kb/disorders/Inherited_Retinal_Dystrophy.yaml).

- **Entry term:** [`MONDO:0019118`](http://purl.obolibrary.org/obo/MONDO_0019118) inherited retinal dystrophy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| RP | `MONDO:0019200` | retinitis pigmentosa | `AGREES` |
| LCA | `MONDO:0018998` | Leber congenital amaurosis | `AGREES` |
| Cone-Rod Dystrophy | `MONDO:0015993` | cone-rod dystrophy | `AGREES` |
| Choroideremia | `MONDO:0010557` | choroideremia | `AGREES` |

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

# Central Areolar Choroidal Dystrophy

Boomer grounding analysis for [`kb/disorders/Central_Areolar_Choroidal_Dystrophy.yaml`](../../../../kb/disorders/Central_Areolar_Choroidal_Dystrophy.yaml).

- **Entry term:** [`MONDO:0008982`](http://purl.obolibrary.org/obo/MONDO_0008982) central areolar choroidal dystrophy
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| CACD1 | `MONDO:0024539` | choroidal dystrophy, central areolar, 1 | `AGREES` |
| CACD2 | `MONDO:0013137` | choroidal dystrophy, central areolar 2 | `AGREES` |
| CACD3 | `MONDO:0013151` | choroidal dystrophy, central areolar, 3 | `AGREES` |

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

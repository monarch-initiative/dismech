# Facioscapulohumeral Muscular Dystrophy

Boomer grounding analysis for [`kb/disorders/Facioscapulohumeral_Muscular_Dystrophy.yaml`](../../../../kb/disorders/Facioscapulohumeral_Muscular_Dystrophy.yaml).

- **Entry term:** [`MONDO:0001347`](http://purl.obolibrary.org/obo/MONDO_0001347) facioscapulohumeral muscular dystrophy
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| FSHD1 | `MONDO:0008030` | facioscapulohumeral muscular dystrophy 1 | `AGREES` |
| FSHD2 | `MONDO:0008031` | facioscapulohumeral muscular dystrophy 2 | `AGREES` |

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

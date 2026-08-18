# Ullrich congenital muscular dystrophy

Boomer grounding analysis for [`kb/disorders/Ullrich_Congenital_Muscular_Dystrophy.yaml`](../../../../kb/disorders/Ullrich_Congenital_Muscular_Dystrophy.yaml).

- **Entry term:** [`MONDO:0000355`](http://purl.obolibrary.org/obo/MONDO_0000355) Ullrich congenital muscular dystrophy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| UCMD1A | `MONDO:0009681` | Ullrich congenital muscular dystrophy 1A | `AGREES` |
| UCMD1B | `MONDO:0958235` | Ullrich congenital muscular dystrophy 1B | `AGREES` |
| UCMD1C | `MONDO:0958236` | Ullrich congenital muscular dystrophy 1C | `AGREES` |
| UCMD2 | `MONDO:0014654` | Ullrich congenital muscular dystrophy 2 | `AGREES` |

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

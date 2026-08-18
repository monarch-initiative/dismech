# Emery-Dreifuss Muscular Dystrophy

Boomer grounding analysis for [`kb/disorders/Emery_Dreifuss_Muscular_Dystrophy.yaml`](../../../../kb/disorders/Emery_Dreifuss_Muscular_Dystrophy.yaml).

- **Entry term:** [`MONDO:0016830`](http://purl.obolibrary.org/obo/MONDO_0016830) Emery-Dreifuss muscular dystrophy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| EDMD1 | `MONDO:0100531` | Emery-Dreifuss muscular dystrophy 1, X-linked | `AGREES` |
| EDMD2 | `MONDO:0021569` | Emery-Dreifuss muscular dystrophy 2, autosomal dominant | `AGREES` |
| EDMD4-5 | `MONDO:0013071` | Emery-Dreifuss muscular dystrophy 4, autosomal dominant | `AGREES` |
| EDMD6 | `MONDO:0800318` | Emery-Dreifuss muscular dystrophy 6, X-linked | `AGREES` |
| EDMD7 | `MONDO:0013677` | Emery-Dreifuss muscular dystrophy 7, autosomal dominant | `AGREES` |

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

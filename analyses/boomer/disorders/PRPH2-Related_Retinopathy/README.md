# PRPH2-Related Retinopathy

Boomer grounding analysis for [`kb/disorders/PRPH2-Related_Retinopathy.yaml`](../../../../kb/disorders/PRPH2-Related_Retinopathy.yaml).

- **Entry term:** [`MONDO:1040055`](http://purl.obolibrary.org/obo/MONDO_1040055) PRPH2-related retinopathy
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Retinitis pigmentosa 7 | `MONDO:0011974` | retinitis pigmentosa 7 | `AGREES` |
| Vitelliform macular dystrophy 3 | `MONDO:0024561` | vitelliform macular dystrophy 3 | `AGREES` |
| Patterned macular dystrophy 1 | `MONDO:0008210` | patterned macular dystrophy 1 | `AGREES` |
| Choroidal dystrophy, central areolar 2 | `MONDO:0013137` | choroidal dystrophy, central areolar 2 | `AGREES` |
| Leber congenital amaurosis 18 | `MONDO:1060145` | Leber congenital amaurosis 18 | `AGREES` |
| Retinitis pigmentosa 7, digenic | `MONDO:1060144` | retinitis pigmentosa 7, digenic | `AGREES` |

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

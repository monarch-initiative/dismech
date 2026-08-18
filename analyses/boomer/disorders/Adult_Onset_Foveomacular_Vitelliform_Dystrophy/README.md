# Adult-Onset Foveomacular Vitelliform Dystrophy

Boomer grounding analysis for [`kb/disorders/Adult_Onset_Foveomacular_Vitelliform_Dystrophy.yaml`](../../../../kb/disorders/Adult_Onset_Foveomacular_Vitelliform_Dystrophy.yaml).

- **Entry term:** [`MONDO:0011979`](http://purl.obolibrary.org/obo/MONDO_0011979) adult-onset foveomacular vitelliform dystrophy
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PRPH2-related | `MONDO:0024561` | vitelliform macular dystrophy 3 | `AGREES` | — no shared vocabulary |
| IMPG1-related | `MONDO:0014508` | vitelliform macular dystrophy 4 | `AGREES` | — no shared vocabulary |
| IMPG2-related | `MONDO:0014509` | vitelliform macular dystrophy 5 | `AGREES` | — no shared vocabulary |

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

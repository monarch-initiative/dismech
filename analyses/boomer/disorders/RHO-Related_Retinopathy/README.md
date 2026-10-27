# RHO-Related Retinopathy

Boomer grounding analysis for [`kb/disorders/RHO-Related_Retinopathy.yaml`](../../../../kb/disorders/RHO-Related_Retinopathy.yaml).

- **Entry term:** [`MONDO:0700380`](http://purl.obolibrary.org/obo/MONDO_0700380) RHO-related retinopathy
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| RP4 | `MONDO:0013395` | retinitis pigmentosa 4 | `AGREES` | — no shared vocabulary |
| CSNBAD1 | `MONDO:0012498` | congenital stationary night blindness autosomal dominant 1 | `AGREES` | — no shared vocabulary |

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

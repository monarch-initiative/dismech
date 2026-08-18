# RNU12-related minor spliceopathy

Boomer grounding analysis for [`kb/disorders/RNU12-related_Minor_Spliceopathy.yaml`](../../../../kb/disorders/RNU12-related_Minor_Spliceopathy.yaml).

- **Entry term:** [`MONDO:1060223`](http://purl.obolibrary.org/obo/MONDO_1060223) RNU12-related minor spliceopathy disorder
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| CDAGS | `MONDO:0011287` | craniosynostosis-anal anomalies-porokeratosis syndrome | `AGREES` |
| SCAR33 | `MONDO:0859360` | spinocerebellar ataxia, autosomal recessive 33 | `AGREES` |

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

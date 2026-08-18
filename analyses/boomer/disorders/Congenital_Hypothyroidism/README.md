# Congenital Hypothyroidism

Boomer grounding analysis for [`kb/disorders/Congenital_Hypothyroidism.yaml`](../../../../kb/disorders/Congenital_Hypothyroidism.yaml).

- **Entry term:** [`MONDO:0018612`](http://purl.obolibrary.org/obo/MONDO_0018612) congenital hypothyroidism
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Permanent Primary | `MONDO:0016408` | permanent congenital hypothyroidism | `AGREES` |
| Transient | `MONDO:0015792` | transient congenital hypothyroidism | `AGREES` |
| Central | `MONDO:0016410` | central congenital hypothyroidism | `AGREES` |
| Dyshormonogenesis | `MONDO:0010132` | familial thyroid dyshormonogenesis | `AGREES` |

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

# 46,XX testicular disorder of sex development

Boomer grounding analysis for [`kb/disorders/46_XX_Testicular_DSD.yaml`](../../../../kb/disorders/46_XX_Testicular_DSD.yaml).

- **Entry term:** [`MONDO:0100249`](http://purl.obolibrary.org/obo/MONDO_0100249) 46,XX testicular disorder of sex development
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| SRY-positive | `MONDO:0100250` | 46,XX sex reversal 1 | `AGREES` |
| SRXX2 | `MONDO:0010218` | 46,XX sex reversal 2 | `AGREES` |
| SRXX3 | `MONDO:0010442` | 46,XX sex reversal 3 | `AGREES` |
| SRXX4 | `MONDO:0060489` | 46,XX sex reversal 4 | `AGREES` |

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

# Bethlem myopathy

Boomer grounding analysis for [`kb/disorders/Bethlem_Myopathy.yaml`](../../../../kb/disorders/Bethlem_Myopathy.yaml).

- **Entry term:** [`MONDO:0008029`](http://purl.obolibrary.org/obo/MONDO_0008029) Bethlem myopathy
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| BTHLM1A | `MONDO:0024530` | Bethlem myopathy 1A | `AGREES` |
| BTHLM1B | `MONDO:0958233` | Bethlem myopathy 1B | `AGREES` |
| BTHLM1C | `MONDO:0958234` | Bethlem myopathy 1C | `AGREES` |

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

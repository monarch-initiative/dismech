# Short QT Syndrome

Boomer grounding analysis for [`kb/disorders/Short_QT_Syndrome.yaml`](../../../../kb/disorders/Short_QT_Syndrome.yaml).

- **Entry term:** [`MONDO:0000453`](http://purl.obolibrary.org/obo/MONDO_0000453) short QT syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| SQTS1 | `MONDO:0012312` | short QT syndrome type 1 | `AGREES` |
| SQTS2 | `MONDO:0012313` | short QT syndrome type 2 | `AGREES` |
| SQTS3 | `MONDO:0012314` | short QT syndrome type 3 | `AGREES` |
| SLC4A3-Related | `MONDO:0859368` | short QT syndrome 7 | `AGREES` |

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

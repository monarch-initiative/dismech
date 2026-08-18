# Anauxetic dysplasia

Boomer grounding analysis for [`kb/disorders/Anauxetic_Dysplasia.yaml`](../../../../kb/disorders/Anauxetic_Dysplasia.yaml).

- **Entry term:** [`MONDO:0011773`](http://purl.obolibrary.org/obo/MONDO_0011773) anauxetic dysplasia
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| AD1 | `MONDO:0054560` | anauxetic dysplasia 1 | `AGREES` |
| AD2 | `MONDO:0054561` | anauxetic dysplasia 2 | `AGREES` |
| AD3 | `MONDO:0030019` | anauxetic dysplasia 3 | `AGREES` |

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

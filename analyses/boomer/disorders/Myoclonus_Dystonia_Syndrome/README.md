# Myoclonus-Dystonia Syndrome

Boomer grounding analysis for [`kb/disorders/Myoclonus_Dystonia_Syndrome.yaml`](../../../../kb/disorders/Myoclonus_Dystonia_Syndrome.yaml).

- **Entry term:** [`MONDO:0000903`](http://purl.obolibrary.org/obo/MONDO_0000903) myoclonus-dystonia syndrome
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| SGCE-related myoclonus-dystonia | `MONDO:0008044` | myoclonic dystonia 11 | `AGREES` |

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

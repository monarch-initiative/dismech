# Lafora_Disease

Boomer grounding analysis for [`kb/disorders/Lafora_Disease.yaml`](../../../../kb/disorders/Lafora_Disease.yaml).

- **Entry term:** [`MONDO:0009697`](http://purl.obolibrary.org/obo/MONDO_0009697) Lafora disease
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| EPM2A-related Lafora disease | `MONDO:0958199` | myoclonic epilepsy of Lafora 1 | `AGREES` |
| NHLRC1-related Lafora disease | `MONDO:0800306` | myoclonic epilepsy of Lafora 2 | `AGREES` |

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

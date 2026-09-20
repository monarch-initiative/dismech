# 3MC Syndrome

Boomer grounding analysis for [`kb/disorders/3MC_Syndrome.yaml`](../../../../kb/disorders/3MC_Syndrome.yaml).

- **Entry term:** [`MONDO:0017398`](http://purl.obolibrary.org/obo/MONDO_0017398) 3MC syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| 3MC1 | `MONDO:0009770` | 3MC syndrome 1 | `AGREES` | ✓ DOID |
| 3MC2 | `MONDO:0009927` | 3MC syndrome 2 | `AGREES` | ✓ DOID |
| 3MC3 | `MONDO:0009554` | 3MC syndrome 3 | `AGREES` | ✓ DOID |

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

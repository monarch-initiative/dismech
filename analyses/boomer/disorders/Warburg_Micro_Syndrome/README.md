# Warburg micro syndrome

Boomer grounding analysis for [`kb/disorders/Warburg_Micro_Syndrome.yaml`](../../../../kb/disorders/Warburg_Micro_Syndrome.yaml).

- **Entry term:** [`MONDO:0016649`](http://purl.obolibrary.org/obo/MONDO_0016649) Warburg micro syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| WARBM1 | `MONDO:0010822` | Warburg micro syndrome 1 | `AGREES` |
| WARBM2 | `MONDO:0013641` | Warburg micro syndrome 2 | `AGREES` |
| WARBM3 | `MONDO:0013638` | Warburg micro syndrome 3 | `AGREES` |
| WARBM4 | `MONDO:0014296` | Warburg micro syndrome 4 | `AGREES` |

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

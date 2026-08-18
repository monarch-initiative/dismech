# Familial Partial Lipodystrophy

Boomer grounding analysis for [`kb/disorders/Familial_Partial_Lipodystrophy.yaml`](../../../../kb/disorders/Familial_Partial_Lipodystrophy.yaml).

- **Entry term:** [`MONDO:0020088`](http://purl.obolibrary.org/obo/MONDO_0020088) familial partial lipodystrophy
- **Grounded subtypes:** 7
- **Verdicts:** AGREES 7

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| FPLD1 | `MONDO:0012072` | familial partial lipodystrophy, Kobberling type | `AGREES` |
| FPLD2 | `MONDO:0007906` | familial partial lipodystrophy, Dunnigan type | `AGREES` |
| FPLD3 | `MONDO:0011448` | PPARG-related familial partial lipodystrophy | `AGREES` |
| FPLD4 | `MONDO:0013478` | PLIN1-related familial partial lipodystrophy | `AGREES` |
| FPLD5 | `MONDO:0014098` | CIDEC-related familial partial lipodystrophy | `AGREES` |
| FPLD6 | `MONDO:0014431` | LIPE-related familial partial lipodystrophy | `AGREES` |
| AKT2 | `MONDO:0019192` | AKT2-related familial partial lipodystrophy | `AGREES` |

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

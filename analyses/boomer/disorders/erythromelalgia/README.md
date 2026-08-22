# erythromelalgia

Boomer grounding analysis for [`kb/disorders/erythromelalgia.yaml`](../../../../kb/disorders/erythromelalgia.yaml).

- **Entry term:** [`MONDO:0016028`](http://purl.obolibrary.org/obo/MONDO_0016028) erythromelalgia
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Primary erythromelalgia | `MONDO:0007571` | primary erythermalgia | `AGREES` | ✓ NCIT, icd11f |
| Secondary erythromelalgia | `MONDO:0035149` | secondary erythromelalgia | `AGREES` | ✓ icd11f |

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

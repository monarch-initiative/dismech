# Mabry Syndrome

Boomer grounding analysis for [`kb/disorders/Mabry_Syndrome.yaml`](../../../../kb/disorders/Mabry_Syndrome.yaml).

- **Entry term:** [`MONDO:0016596`](http://purl.obolibrary.org/obo/MONDO_0016596) hyperphosphatasia-intellectual disability syndrome
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| HPMRS1 | `MONDO:0009398` | hyperphosphatasia with intellectual disability syndrome 1 | `AGREES` | ✓ DOID |
| HPMRS2 | `MONDO:0013882` | hyperphosphatasia with intellectual disability syndrome 2 | `AGREES` | ✓ DOID |
| HPMRS3 | `MONDO:0013628` | hyperphosphatasia with intellectual disability syndrome 3 | `AGREES` | ✓ DOID |
| HPMRS4 | `MONDO:0014318` | hyperphosphatasia with intellectual disability syndrome 4 | `AGREES` | ✓ DOID |
| HPMRS5 | `MONDO:0014457` | hyperphosphatasia with intellectual disability syndrome 5 | `AGREES` | ✓ DOID |
| HPMRS6 | `MONDO:0014780` | hyperphosphatasia with intellectual disability syndrome 6 | `AGREES` | ✓ DOID |

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

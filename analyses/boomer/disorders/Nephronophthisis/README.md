# Nephronophthisis

Boomer grounding analysis for [`kb/disorders/Nephronophthisis.yaml`](../../../../kb/disorders/Nephronophthisis.yaml).

- **Entry term:** [`MONDO:0019005`](http://purl.obolibrary.org/obo/MONDO_0019005) nephronophthisis
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| NPHP1-related | `MONDO:0009728` | nephronophthisis 1 | `AGREES` | ✓ DOID, NCIT, ORDO |
| CEP164-related | `MONDO:0013917` | nephronophthisis 15 | `AGREES` | ✓ DOID |

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

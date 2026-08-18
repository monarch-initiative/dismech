# Optic Neuritis

Boomer grounding analysis for [`kb/disorders/Optic_Neuritis.yaml`](../../../../kb/disorders/Optic_Neuritis.yaml).

- **Entry term:** [`MONDO:0005885`](http://purl.obolibrary.org/obo/MONDO_0005885) optic neuritis
- **Grounded subtypes:** 3
- **Verdicts:** SILENT 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Isolated optic neuritis | `MONDO:0044688` | isolated optic neuritis | `SILENT` |
| Single isolated optic neuritis | `MONDO:0971049` | single isolated optic neuritis | `SILENT` |
| Relapsing isolated optic neuritis | `MONDO:0971050` | relapsing isolated optic neuritis | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

3 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

# 3-Phosphoglycerate Dehydrogenase Deficiency

Boomer grounding analysis for [`kb/disorders/3-Phosphoglycerate_Dehydrogenase_Deficiency.yaml`](../../../../kb/disorders/3-Phosphoglycerate_Dehydrogenase_Deficiency.yaml).

- **Entry term:** [`MONDO:0011152`](http://purl.obolibrary.org/obo/MONDO_0011152) PHGDH deficiency
- **Grounded subtypes:** 1
- **Verdicts:** SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Neu-Laxova | `MONDO:0009736` | Neu-Laxova syndrome 1 | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

# Autoimmune Retinopathy

Boomer grounding analysis for [`kb/disorders/Autoimmune_Retinopathy.yaml`](../../../../kb/disorders/Autoimmune_Retinopathy.yaml).

- **Entry term:** [`MONDO:0100014`](http://purl.obolibrary.org/obo/MONDO_0100014) autoimmune retinopathy
- **Grounded subtypes:** 2
- **Verdicts:** SILENT 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CAR | `MONDO:0019112` | cancer-associated retinopathy | `SILENT` | silent (icd11f) |
| MAR | `MONDO:0023868` | melanoma associated retinopathy | `SILENT` | silent (icd11f) |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

2 subtype(s) are `SILENT`: MONDO asserts no path between the
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

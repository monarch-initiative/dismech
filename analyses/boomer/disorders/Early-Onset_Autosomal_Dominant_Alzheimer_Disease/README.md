# Early-Onset Autosomal Dominant Alzheimer Disease

Boomer grounding analysis for [`kb/disorders/Early-Onset_Autosomal_Dominant_Alzheimer_Disease.yaml`](../../../../kb/disorders/Early-Onset_Autosomal_Dominant_Alzheimer_Disease.yaml).

- **Entry term:** [`MONDO:0015140`](http://purl.obolibrary.org/obo/MONDO_0015140) early-onset autosomal dominant Alzheimer disease
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 3, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| PSEN1 | `MONDO:0011913` | Alzheimer disease 3 | `AGREES` |
| APP | `MONDO:0007088` | Alzheimer disease type 1 | `AGREES` |
| APP Duplication | `MONDO:1060190` | APP-related brain and vascular amyloidosis | `SILENT` |
| PSEN2 | `MONDO:0011743` | Alzheimer disease 4 | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

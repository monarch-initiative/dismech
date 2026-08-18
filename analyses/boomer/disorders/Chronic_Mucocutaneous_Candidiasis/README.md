# Chronic Mucocutaneous Candidiasis

Boomer grounding analysis for [`kb/disorders/Chronic_Mucocutaneous_Candidiasis.yaml`](../../../../kb/disorders/Chronic_Mucocutaneous_Candidiasis.yaml).

- **Entry term:** [`MONDO:0015279`](http://purl.obolibrary.org/obo/MONDO_0015279) chronic mucocutaneous candidiasis
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 5, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| STAT1 GOF | `MONDO:0013599` | autoimmune enteropathy and endocrinopathy - susceptibility to chronic infections syndrome | `AGREES` |
| IL17RA deficiency | `MONDO:0013500` | immunodeficiency 51 | `AGREES` |
| IL17RC deficiency | `MONDO:0014642` | candidiasis, familial, 9 | `AGREES` |
| IL17F deficiency | `MONDO:0013503` | candidiasis, familial, 6 | `AGREES` |
| ACT1 deficiency | `MONDO:0014230` | candidiasis, familial, 8 | `AGREES` |
| APECED | `MONDO:0009411` | autoimmune polyendocrine syndrome type 1 | `SILENT` |

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
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

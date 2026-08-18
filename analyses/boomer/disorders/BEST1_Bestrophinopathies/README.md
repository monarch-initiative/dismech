# BEST1 Bestrophinopathies

Boomer grounding analysis for [`kb/disorders/BEST1_Bestrophinopathies.yaml`](../../../../kb/disorders/BEST1_Bestrophinopathies.yaml).

- **Entry term:** [`MONDO:0000390`](http://purl.obolibrary.org/obo/MONDO_0000390) vitelliform macular dystrophy
- **Grounded subtypes:** 5
- **Verdicts:** SILENT 4, AGREES 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| BVMD | `MONDO:0007931` | vitelliform macular dystrophy 2 | `AGREES` |
| ARB | `MONDO:0012733` | autosomal recessive bestrophinopathy | `SILENT` |
| ADVIRC | `MONDO:0008662` | autosomal dominant vitreoretinochoroidopathy | `SILENT` |
| MRCS | `MONDO:0033644` | microcornea, rod-cone dystrophy, cataract, and posterior staphyloma 1 | `SILENT` |
| BEST1-RP | `MONDO:0019200` | retinitis pigmentosa | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

4 subtype(s) are `SILENT`: MONDO asserts no path between the
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

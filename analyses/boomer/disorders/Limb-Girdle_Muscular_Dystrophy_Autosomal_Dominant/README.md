# Limb-Girdle Muscular Dystrophy, Autosomal Dominant

Boomer grounding analysis for [`kb/disorders/Limb-Girdle_Muscular_Dystrophy_Autosomal_Dominant.yaml`](../../../../kb/disorders/Limb-Girdle_Muscular_Dystrophy_Autosomal_Dominant.yaml).

- **Entry term:** [`MONDO:0015151`](http://purl.obolibrary.org/obo/MONDO_0015151) muscular dystrophy, limb-girdle, autosomal dominant
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| LGMD-D1 | `MONDO:0021018` | autosomal dominant limb-girdle muscular dystrophy type 1D (DNAJB6) | `AGREES` |
| LGMD-D2 | `MONDO:0012034` | autosomal dominant limb-girdle muscular dystrophy type 1F | `AGREES` |
| LGMD-D3 | `MONDO:0012193` | autosomal dominant limb-girdle muscular dystrophy type 1G | `AGREES` |
| LGMD-D4 | `MONDO:0029133` | muscular dystrophy, limb-girdle, autosomal dominant 4 | `AGREES` |

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

# Centronuclear Myopathy

Boomer grounding analysis for [`kb/disorders/Centronuclear_Myopathy.yaml`](../../../../kb/disorders/Centronuclear_Myopathy.yaml).

- **Entry term:** [`MONDO:0018947`](http://purl.obolibrary.org/obo/MONDO_0018947) centronuclear myopathy
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| XLMTM | `MONDO:0010683` | X-linked myotubular myopathy | `AGREES` |
| AD-CNM | `MONDO:0008048` | autosomal dominant centronuclear myopathy | `AGREES` |
| AR-CNM | `MONDO:0009709` | myopathy, centronuclear, 2 | `AGREES` |
| RYR1-CNM | `MONDO:0015705` | autosomal recessive centronuclear myopathy | `AGREES` |
| SPEG-CNM | `MONDO:0014418` | myopathy, centronuclear, 5 | `AGREES` |

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

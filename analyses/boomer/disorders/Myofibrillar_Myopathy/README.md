# Myofibrillar Myopathy

Boomer grounding analysis for [`kb/disorders/Myofibrillar_Myopathy.yaml`](../../../../kb/disorders/Myofibrillar_Myopathy.yaml).

- **Entry term:** [`MONDO:0018943`](http://purl.obolibrary.org/obo/MONDO_0018943) myofibrillar myopathy
- **Grounded subtypes:** 10
- **Verdicts:** AGREES 9, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| MFM1 | `MONDO:0011076` | myofibrillar myopathy 1 | `AGREES` |
| MFM2 | `MONDO:0012130` | myofibrillar myopathy 2 | `SILENT` |
| MFM3 | `MONDO:0012215` | myofibrillar myopathy 3 | `AGREES` |
| MFM4 | `MONDO:0012277` | myofibrillar myopathy 4 | `AGREES` |
| MFM5 | `MONDO:0012289` | myofibrillar myopathy 5 | `AGREES` |
| MFM6 | `MONDO:0013061` | myofibrillar myopathy 6 | `AGREES` |
| MFM7 | `MONDO:0014922` | myofibrillar myopathy 7 | `AGREES` |
| MFM8 | `MONDO:0014993` | myofibrillar myopathy 8 | `AGREES` |
| MFM10 | `MONDO:0033620` | myofibrillar myopathy 10 | `AGREES` |
| MFM11 | `MONDO:0030927` | myofibrillar myopathy 11 | `AGREES` |

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

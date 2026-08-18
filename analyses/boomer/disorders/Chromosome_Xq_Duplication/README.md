# Chromosome Xq Duplication

Boomer grounding analysis for [`kb/disorders/Chromosome_Xq_Duplication.yaml`](../../../../kb/disorders/Chromosome_Xq_Duplication.yaml).

- **Entry term:** [`MONDO:0017010`](http://purl.obolibrary.org/obo/MONDO_0017010) partial duplication of the long arm of chromosome X
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 2, SILENT 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Xq28 (MECP2) | `MONDO:0010283` | syndromic X-linked intellectual disability Lubs type | `AGREES` |
| Xq26.3-q27.1 (SOX3) | `MONDO:0010712` | panhypopituitarism, X-linked | `SILENT` |
| Xq25 (STAG2) | `MONDO:0010507` | Xq25 microduplication syndrome | `AGREES` |
| Xq25-q26 | `MONDO:0010252` | intellectual disability, X-linked, with panhypopituitarism | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

2 subtype(s) are `SILENT`: MONDO asserts no path between the
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

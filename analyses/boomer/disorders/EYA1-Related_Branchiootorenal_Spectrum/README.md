# EYA1-Related Branchiootorenal Spectrum Disorder

Boomer grounding analysis for [`kb/disorders/EYA1-Related_Branchiootorenal_Spectrum.yaml`](../../../../kb/disorders/EYA1-Related_Branchiootorenal_Spectrum.yaml).

- **Entry term:** [`MONDO:0011258`](http://purl.obolibrary.org/obo/MONDO_0011258) branchiootic syndrome 1
- **Grounded subtypes:** 2
- **Verdicts:** SAME_TERM 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| BOS1 | `MONDO:0011258` | branchiootic syndrome 1 | `SAME_TERM` | ✓ DOID, OMIM |
| BOR1 | `MONDO:0007236` | branchiootorenal syndrome 1 | `SILENT` | silent (DOID, OMIM) |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.
- **`SAME_TERM`** - Subtype and entry are grounded to the same MONDO term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

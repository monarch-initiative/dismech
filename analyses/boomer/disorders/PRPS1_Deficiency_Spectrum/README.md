# PRPS1 Deficiency Spectrum

Boomer grounding analysis for [`kb/disorders/PRPS1_Deficiency_Spectrum.yaml`](../../../../kb/disorders/PRPS1_Deficiency_Spectrum.yaml).

- **Entry term:** [`MONDO:0100061`](http://purl.obolibrary.org/obo/MONDO_0100061) PRPS1 deficiency disorder
- **Grounded subtypes:** 3
- **Verdicts:** SILENT 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Arts Syndrome | `MONDO:0010533` | Arts syndrome | `SILENT` |
| CMTX5 | `MONDO:0010699` | Charcot-Marie-Tooth disease X-linked recessive 5 | `SILENT` |
| DFN2 | `MONDO:0010577` | hearing loss, X-linked 1 | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

3 subtype(s) are `SILENT`: MONDO asserts no path between the
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

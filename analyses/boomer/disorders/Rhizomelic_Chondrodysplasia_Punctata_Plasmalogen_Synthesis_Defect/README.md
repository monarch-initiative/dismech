# Rhizomelic Chondrodysplasia Punctata, Plasmalogen-Synthesis Defect

Boomer grounding analysis for [`kb/disorders/Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect.yaml`](../../../../kb/disorders/Rhizomelic_Chondrodysplasia_Punctata_Plasmalogen_Synthesis_Defect.yaml).

- **Entry term:** [`MONDO:0015776`](http://purl.obolibrary.org/obo/MONDO_0015776) rhizomelic chondrodysplasia punctata
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 2, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| RCDP2 | `MONDO:0009112` | rhizomelic chondrodysplasia punctata type 2 | `AGREES` |
| RCDP3 | `MONDO:0010823` | rhizomelic chondrodysplasia punctata type 3 | `AGREES` |
| RCDP4 | `MONDO:0014510` | fatty acyl-CoA reductase 1 deficiency | `SILENT` |

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

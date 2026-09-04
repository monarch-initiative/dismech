# Hereditary Hemorrhagic Telangiectasia

Boomer grounding analysis for [`kb/disorders/Hereditary_Hemorrhagic_Telangiectasia.yaml`](../../../../kb/disorders/Hereditary_Hemorrhagic_Telangiectasia.yaml).

- **Entry term:** [`MONDO:0019180`](http://purl.obolibrary.org/obo/MONDO_0019180) hereditary hemorrhagic telangiectasia
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| HHT1 | `MONDO:0008535` | telangiectasia, hereditary hemorrhagic, type 1 | `AGREES` | — no shared vocabulary |
| HHT2 | `MONDO:0010880` | telangiectasia, hereditary hemorrhagic, type 2 | `AGREES` | — no shared vocabulary |
| HHT4 | `MONDO:0012532` | hereditary hemorrhagic telangiectasia type 4 | `AGREES` | silent (MESH) |
| SMAD4-associated juvenile polyposis/HHT overlap | `MONDO:0008278` | juvenile polyposis/hereditary hemorrhagic telangiectasia syndrome | `SILENT` | silent (DOID, MESH) |
| GDF2-related HHT-like disease | `MONDO:0014217` | telangiectasia, hereditary hemorrhagic, type 5 | `AGREES` | — no shared vocabulary |

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

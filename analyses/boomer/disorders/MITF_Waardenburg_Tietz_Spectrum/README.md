# MITF Waardenburg-Tietz Spectrum

Boomer grounding analysis for [`kb/disorders/MITF_Waardenburg_Tietz_Spectrum.yaml`](../../../../kb/disorders/MITF_Waardenburg_Tietz_Spectrum.yaml).

- **Entry term:** [`MONDO:0018094`](http://purl.obolibrary.org/obo/MONDO_0018094) Waardenburg syndrome
- **Grounded subtypes:** 3
- **Verdicts:** SILENT 2, AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| WS2A | `MONDO:0008671` | Waardenburg syndrome type 2A | `AGREES` | ✓ DOID, NCIT |
| Tietz | `MONDO:0007077` | Tietz syndrome | `SILENT` | silent (DOID, MESH, ORDO) |
| COMMAD | `MONDO:0015014` | coloboma, osteopetrosis, microphthalmia, macrocephaly, albinism, and deafness | `SILENT` | silent (ORDO) |

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
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

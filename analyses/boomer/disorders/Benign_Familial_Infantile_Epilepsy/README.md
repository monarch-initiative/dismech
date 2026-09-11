# Benign Familial Infantile Epilepsy

Boomer grounding analysis for [`kb/disorders/Benign_Familial_Infantile_Epilepsy.yaml`](../../../../kb/disorders/Benign_Familial_Infantile_Epilepsy.yaml).

- **Entry term:** [`MONDO:0017615`](http://purl.obolibrary.org/obo/MONDO_0017615) benign familial infantile epilepsy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 3, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PRRT2-related BFIE | `MONDO:0011593` | seizures, benign familial infantile, 2 | `AGREES` | ✓ DOID |
| ICCA | `MONDO:0011178` | infantile convulsions and choreoathetosis | `SILENT` | silent (ORDO) |
| SCN2A-related BFNIS | `MONDO:0011904` | seizures, benign familial infantile, 3 | `AGREES` | ✓ DOID |
| SCN8A-related BFIS | `MONDO:0014903` | seizures, benign familial infantile, 5 | `AGREES` | ✓ DOID |

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

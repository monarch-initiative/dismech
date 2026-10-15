# Primary Cutaneous Amyloidosis

Boomer grounding analysis for [`kb/disorders/Primary_Cutaneous_Amyloidosis.yaml`](../../../../kb/disorders/Primary_Cutaneous_Amyloidosis.yaml).

- **Entry term:** [`MONDO:0015301`](http://purl.obolibrary.org/obo/MONDO_0015301) primary cutaneous amyloidosis
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Lichen Amyloidosis | `MONDO:0018856` | lichen amyloidosis | `AGREES` | ✓ ORDO |
| Macular Amyloidosis | `MONDO:0015303` | macular amyloidosis | `AGREES` | ✓ ORDO |
| Nodular Amyloidosis | `MONDO:0015302` | nodular cutaneous amyloidosis | `AGREES` | ✓ ORDO |
| Amyloidosis Cutis Dyschromica | `MONDO:0017906` | amyloidosis cutis dyschromia | `AGREES` | ✓ DOID, ORDO |
| Familial PLCA | `MONDO:0007101` | familial primary localized cutaneous amyloidosis | `AGREES` | ✓ ORDO |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

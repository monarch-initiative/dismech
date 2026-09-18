# Familial Hemiplegic Migraine

Boomer grounding analysis for [`kb/disorders/Familial_Hemiplegic_Migraine.yaml`](../../../../kb/disorders/Familial_Hemiplegic_Migraine.yaml).

- **Entry term:** [`MONDO:0000700`](http://purl.obolibrary.org/obo/MONDO_0000700) familial hemiplegic migraine
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| FHM1 | `MONDO:0020756` | migraine, familial hemiplegic, 1 | `AGREES` | ✓ DOID, icd11f |
| FHM2 | `MONDO:0011232` | migraine, familial hemiplegic, 2 | `AGREES` | ✓ DOID |
| FHM3 | `MONDO:0012320` | migraine, familial hemiplegic, 3 | `AGREES` | ✓ DOID |

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

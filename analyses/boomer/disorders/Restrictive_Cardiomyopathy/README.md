# Restrictive Cardiomyopathy

Boomer grounding analysis for [`kb/disorders/Restrictive_Cardiomyopathy.yaml`](../../../../kb/disorders/Restrictive_Cardiomyopathy.yaml).

- **Entry term:** [`MONDO:0005201`](http://purl.obolibrary.org/obo/MONDO_0005201) restrictive cardiomyopathy
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| RCM1 | `MONDO:0007270` | cardiomyopathy, familial restrictive, 1 | `AGREES` | ✓ DOID |
| RCM3 | `MONDO:0012900` | cardiomyopathy, familial restrictive, 3 | `AGREES` | ✓ DOID |

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

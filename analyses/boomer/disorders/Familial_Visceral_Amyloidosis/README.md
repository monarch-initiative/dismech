# Familial Visceral Amyloidosis

Boomer grounding analysis for [`kb/disorders/Familial_Visceral_Amyloidosis.yaml`](../../../../kb/disorders/Familial_Visceral_Amyloidosis.yaml).

- **Entry term:** [`MONDO:0007099`](http://purl.obolibrary.org/obo/MONDO_0007099) familial visceral amyloidosis
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| AApoAI | `MONDO:0019731` | AApoAI amyloidosis | `AGREES` | ✓ ORDO |
| AApoAII | `MONDO:0016533` | apolipoprotein A-II amyloidosis | `AGREES` | ✓ ORDO |
| AFib | `MONDO:0019733` | AFib amyloidosis | `AGREES` | ✓ ORDO |
| ALys | `MONDO:0019732` | ALys amyloidosis | `AGREES` | ✓ ORDO |

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

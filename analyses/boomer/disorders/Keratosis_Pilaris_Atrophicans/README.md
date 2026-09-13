# Keratosis Pilaris Atrophicans

Boomer grounding analysis for [`kb/disorders/Keratosis_Pilaris_Atrophicans.yaml`](../../../../kb/disorders/Keratosis_Pilaris_Atrophicans.yaml).

- **Entry term:** [`MONDO:0018855`](http://purl.obolibrary.org/obo/MONDO_0018855) keratosis pilaris atrophicans
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Keratosis Pilaris Atrophicans Faciei | `MONDO:0859588` | keratosis pilaris atrophicans faciei | `AGREES` | ✓ DOID |
| Atrophoderma Vermiculatum | `MONDO:0008849` | atrophoderma vermiculata | `AGREES` | ✓ DOID, ORDO |
| Keratosis Follicularis Spinulosa Decalvans | `MONDO:0000136` | keratosis follicularis spinulosa decalvans | `AGREES` | ✓ DOID, ORDO, icd11f |

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

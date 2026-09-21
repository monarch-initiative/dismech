# Spina Bifida Cystica

Boomer grounding analysis for [`kb/disorders/Spina_Bifida_Cystica.yaml`](../../../../kb/disorders/Spina_Bifida_Cystica.yaml).

- **Entry term:** [`MONDO:0017069`](http://purl.obolibrary.org/obo/MONDO_0017069) spina bifida cystica
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Meningocele | `MONDO:0017076` | posterior meningocele | `AGREES` | ✓ ORDO, icd11f |
| Myelomeningocele | `MONDO:0019773` | myelomeningocele | `AGREES` | ✓ ORDO |

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

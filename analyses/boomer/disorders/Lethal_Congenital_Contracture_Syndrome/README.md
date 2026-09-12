# Lethal Congenital Contracture Syndrome

Boomer grounding analysis for [`kb/disorders/Lethal_Congenital_Contracture_Syndrome.yaml`](../../../../kb/disorders/Lethal_Congenital_Contracture_Syndrome.yaml).

- **Entry term:** [`MONDO:0017436`](http://purl.obolibrary.org/obo/MONDO_0017436) lethal congenital contracture syndrome
- **Grounded subtypes:** 12
- **Verdicts:** AGREES 12

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| LCCS1 | `MONDO:0009670` | lethal congenital contracture syndrome 1 | `AGREES` | ✓ DOID, ORDO |
| LCCS2 | `MONDO:0011868` | lethal congenital contracture syndrome 2 | `AGREES` | ✓ DOID, ORDO |
| LCCS3 | `MONDO:0012656` | lethal congenital contracture syndrome 3 | `AGREES` | ✓ DOID, ORDO |
| LCCS4 | `MONDO:0013965` | lethal congenital contracture syndrome 4 | `AGREES` | ✓ DOID |
| LCCS5 | `MONDO:0014149` | fetal akinesia-cerebral and retinal hemorrhage syndrome | `AGREES` | silent (DOID, ORDO) |
| LCCS6 | `MONDO:0014549` | lethal congenital contracture syndrome 6 | `AGREES` | silent (DOID) |
| LCCS7 | `MONDO:0014569` | lethal congenital contracture syndrome 7 | `AGREES` | silent (DOID) |
| LCCS8 | `MONDO:0014570` | lethal congenital contracture syndrome 8 | `AGREES` | silent (DOID) |
| LCCS9 | `MONDO:0014670` | lethal congenital contracture syndrome 9 | `AGREES` | silent (DOID) |
| LCCS10 | `MONDO:0014870` | NEK9-related lethal skeletal dysplasia | `AGREES` | silent (DOID, ORDO) |
| LCCS11 | `MONDO:0014965` | lethal congenital contracture syndrome 11 | `AGREES` | silent (DOID) |
| LCCS12 | `MONDO:0981031` | lethal congenital contracture syndrome 12 | `AGREES` | silent (DOID) |

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

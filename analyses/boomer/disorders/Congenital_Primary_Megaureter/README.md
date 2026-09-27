# Congenital Primary Megaureter

Boomer grounding analysis for [`kb/disorders/Congenital_Primary_Megaureter.yaml`](../../../../kb/disorders/Congenital_Primary_Megaureter.yaml).

- **Entry term:** [`MONDO:0018960`](http://purl.obolibrary.org/obo/MONDO_0018960) congenital primary megaureter
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Obstructed | `MONDO:0016550` | congenital primary megaureter, obstructed form | `AGREES` | ✓ ORDO, icd11f |
| Refluxing | `MONDO:0016551` | congenital primary megaureter, refluxing form | `AGREES` | ✓ ORDO, icd11f |
| Non-obstructed Non-refluxing | `MONDO:0016552` | congenital primary megaureter, nonrefluxing and unobstructed form | `AGREES` | ✓ ORDO, icd11f |
| Combined Obstructed and Refluxing | `MONDO:0035295` | congenital primary megaureter, refluxing and obstructed form | `AGREES` | ✓ ORDO |

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

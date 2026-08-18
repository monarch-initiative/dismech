# Polycystic Kidney Disease

Boomer grounding analysis for [`kb/disorders/Polycystic_Kidney_Disease.yaml`](../../../../kb/disorders/Polycystic_Kidney_Disease.yaml).

- **Entry term:** [`MONDO:0020642`](http://purl.obolibrary.org/obo/MONDO_0020642) polycystic kidney disease
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Autosomal Dominant PKD (ADPKD) | `MONDO:0004691` | autosomal dominant polycystic kidney disease | `AGREES` |
| Autosomal Recessive PKD (ARPKD) | `MONDO:0009889` | autosomal recessive polycystic kidney disease | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

# Acute Respiratory Distress Syndrome

Boomer grounding analysis for [`kb/disorders/Acute_Respiratory_Distress_Syndrome.yaml`](../../../../kb/disorders/Acute_Respiratory_Distress_Syndrome.yaml).

- **Entry term:** [`MONDO:0006502`](http://purl.obolibrary.org/obo/MONDO_0006502) acute respiratory distress syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Adult ARDS | `MONDO:0100130` | adult acute respiratory distress syndrome | `AGREES` | ✓ icd11f |
| Pediatric ARDS | `MONDO:0100131` | pediatric acute respiratory distress syndrome | `AGREES` | — no shared vocabulary |

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

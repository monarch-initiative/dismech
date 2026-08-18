# Laryngotracheoesophageal Cleft

Boomer grounding analysis for [`kb/disorders/Laryngotracheoesophageal_Cleft.yaml`](../../../../kb/disorders/Laryngotracheoesophageal_Cleft.yaml).

- **Entry term:** [`MONDO:0016060`](http://purl.obolibrary.org/obo/MONDO_0016060) laryngotracheoesophageal cleft
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type 0 (interarytenoid cleft) | `MONDO:0017220` | laryngotracheoesophageal cleft type 0 | `AGREES` |
| Type I | `MONDO:0019761` | laryngotracheoesophageal cleft type 1 | `AGREES` |
| Type II | `MONDO:0019762` | laryngotracheoesophageal cleft type 2 | `AGREES` |
| Type III | `MONDO:0019763` | laryngotracheoesophageal cleft type 3 | `AGREES` |
| Type IV | `MONDO:0019764` | laryngotracheoesophageal cleft type 4 | `AGREES` |

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

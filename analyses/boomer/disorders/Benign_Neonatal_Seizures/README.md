# Benign Neonatal Seizures

Boomer grounding analysis for [`kb/disorders/Benign_Neonatal_Seizures.yaml`](../../../../kb/disorders/Benign_Neonatal_Seizures.yaml).

- **Entry term:** [`MONDO:0016027`](http://purl.obolibrary.org/obo/MONDO_0016027) benign neonatal seizures
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| KCNQ2-BFNS | `MONDO:0007365` | seizures, benign familial neonatal, 1 | `AGREES` |
| KCNQ3-BFNS | `MONDO:0007366` | seizures, benign familial neonatal, 2 | `AGREES` |

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

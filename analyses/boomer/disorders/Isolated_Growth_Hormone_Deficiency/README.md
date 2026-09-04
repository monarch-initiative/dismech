# Isolated Growth Hormone Deficiency

Boomer grounding analysis for [`kb/disorders/Isolated_Growth_Hormone_Deficiency.yaml`](../../../../kb/disorders/Isolated_Growth_Hormone_Deficiency.yaml).

- **Entry term:** [`MONDO:0000050`](http://purl.obolibrary.org/obo/MONDO_0000050) isolated congenital growth hormone deficiency
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type IA | `MONDO:0009876` | isolated growth hormone deficiency type IA | `AGREES` | ✓ DOID, ORDO |
| Type IB | `MONDO:0013006` | isolated growth hormone deficiency type IB | `AGREES` | ✓ DOID, ORDO |
| Type II | `MONDO:0008250` | isolated growth hormone deficiency type II | `AGREES` | ✓ DOID, ORDO |
| Type III | `MONDO:0010615` | isolated growth hormone deficiency type III | `AGREES` | ✓ DOID, ORDO |

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

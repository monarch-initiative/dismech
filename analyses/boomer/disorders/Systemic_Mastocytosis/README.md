# Systemic Mastocytosis

Boomer grounding analysis for [`kb/disorders/Systemic_Mastocytosis.yaml`](../../../../kb/disorders/Systemic_Mastocytosis.yaml).

- **Entry term:** [`MONDO:0016586`](http://purl.obolibrary.org/obo/MONDO_0016586) systemic mastocytosis
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Indolent SM | `MONDO:0020331` | indolent systemic mastocytosis | `AGREES` | ✓ DOID, NCIT, ORDO, icd11f |
| Smouldering SM | `MONDO:0015557` | Smouldering systemic mastocytosis | `AGREES` | ✓ NCIT, ORDO, icd11f |
| Aggressive SM | `MONDO:0020333` | aggressive systemic mastocytosis | `AGREES` | ✓ DOID, NCIT, ORDO, icd11f |
| SM-AHN | `MONDO:0020332` | systemic mastocytosis with an associated clonal hematologic non-mast cell lineage disease | `AGREES` | ✓ DOID, NCIT, ORDO |
| Mast Cell Leukemia | `MONDO:0020334` | mast cell leukemia | `AGREES` | ✓ NCIT, ORDO, icd11f |

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

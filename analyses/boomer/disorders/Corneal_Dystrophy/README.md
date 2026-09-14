# Corneal Dystrophy

Boomer grounding analysis for [`kb/disorders/Corneal_Dystrophy.yaml`](../../../../kb/disorders/Corneal_Dystrophy.yaml).

- **Entry term:** [`MONDO:0018102`](http://purl.obolibrary.org/obo/MONDO_0018102) corneal dystrophy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Epithelial and Subepithelial | `MONDO:0000763` | epithelial and subepithelial corneal dystrophy | `AGREES` | ✓ DOID |
| Epithelial-Stromal TGFBI | `MONDO:0000764` | epithelial-stromal TGFBI dystrophy | `AGREES` | ✓ DOID |
| Stromal | `MONDO:0020213` | stromal corneal dystrophy | `AGREES` | ✓ DOID, ORDO, icd11f |
| Endothelial | `MONDO:0000766` | corneal endothelial dystrophy | `AGREES` | ✓ DOID |

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

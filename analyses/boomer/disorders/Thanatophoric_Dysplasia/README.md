# Thanatophoric Dysplasia

Boomer grounding analysis for [`kb/disorders/Thanatophoric_Dysplasia.yaml`](../../../../kb/disorders/Thanatophoric_Dysplasia.yaml).

- **Entry term:** [`MONDO:0017042`](http://purl.obolibrary.org/obo/MONDO_0017042) thanatophoric dysplasia
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| TD1 | `MONDO:0008546` | thanatophoric dysplasia type 1 | `AGREES` | ✓ NCIT, ORDO |
| TD2 | `MONDO:0008547` | thanatophoric dysplasia type 2 | `AGREES` | ✓ NCIT, ORDO |

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

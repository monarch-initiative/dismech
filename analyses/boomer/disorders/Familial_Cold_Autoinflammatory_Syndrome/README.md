# Familial Cold Autoinflammatory Syndrome

Boomer grounding analysis for [`kb/disorders/Familial_Cold_Autoinflammatory_Syndrome.yaml`](../../../../kb/disorders/Familial_Cold_Autoinflammatory_Syndrome.yaml).

- **Entry term:** [`MONDO:0018768`](http://purl.obolibrary.org/obo/MONDO_0018768) familial cold autoinflammatory syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| FCAS1 | `MONDO:0007349` | familial cold autoinflammatory syndrome 1 | `AGREES` | ✓ DOID |
| FCAS2 | `MONDO:0012724` | familial cold autoinflammatory syndrome 2 | `AGREES` | ✓ DOID |
| FCAS3 | `MONDO:0013766` | familial cold autoinflammatory syndrome 3 | `AGREES` | ✓ DOID |
| FCAS4 | `MONDO:0014498` | familial cold autoinflammatory syndrome 4 | `AGREES` | ✓ DOID |

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

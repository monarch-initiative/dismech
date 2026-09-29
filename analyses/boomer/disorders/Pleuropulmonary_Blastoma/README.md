# Pleuropulmonary Blastoma

Boomer grounding analysis for [`kb/disorders/Pleuropulmonary_Blastoma.yaml`](../../../../kb/disorders/Pleuropulmonary_Blastoma.yaml).

- **Entry term:** [`MONDO:0011014`](http://purl.obolibrary.org/obo/MONDO_0011014) pleuropulmonary blastoma
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type I | `MONDO:0020555` | pleuropulmonary blastoma type 1 | `AGREES` | ✓ NCIT, ORDO |
| Type II | `MONDO:0020556` | pleuropulmonary blastoma type 2 | `AGREES` | ✓ NCIT, ORDO |
| Type III | `MONDO:0020557` | pleuropulmonary blastoma type 3 | `AGREES` | ✓ NCIT, ORDO |

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

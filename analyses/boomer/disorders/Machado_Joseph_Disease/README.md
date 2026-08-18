# Machado-Joseph Disease

Boomer grounding analysis for [`kb/disorders/Machado_Joseph_Disease.yaml`](../../../../kb/disorders/Machado_Joseph_Disease.yaml).

- **Entry term:** [`MONDO:0007182`](http://purl.obolibrary.org/obo/MONDO_0007182) Machado-Joseph disease
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type 1 | `MONDO:0017174` | Machado-Joseph disease type 1 | `AGREES` |
| Type 2 | `MONDO:0017175` | Machado-Joseph disease type 2 | `AGREES` |
| Type 3 | `MONDO:0017176` | Machado-Joseph disease type 3 | `AGREES` |
| Type 4 | `MONDO:0042964` | Machado-Joseph disease type 4 | `AGREES` |

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

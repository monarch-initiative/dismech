# Sandhoff Disease

Boomer grounding analysis for [`kb/disorders/Sandhoff_Disease.yaml`](../../../../kb/disorders/Sandhoff_Disease.yaml).

- **Entry term:** [`MONDO:0010006`](http://purl.obolibrary.org/obo/MONDO_0010006) Sandhoff disease
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Infantile Sandhoff disease | `MONDO:0017721` | Sandhoff disease, infantile form | `AGREES` |
| Juvenile Sandhoff disease | `MONDO:0017722` | Sandhoff disease, juvenile form | `AGREES` |
| Adult Sandhoff disease | `MONDO:0017723` | Sandhoff disease, adult form | `AGREES` |

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

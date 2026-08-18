# Gaucher Disease

Boomer grounding analysis for [`kb/disorders/Gaucher_Disease.yaml`](../../../../kb/disorders/Gaucher_Disease.yaml).

- **Entry term:** [`MONDO:0018150`](http://purl.obolibrary.org/obo/MONDO_0018150) Gaucher disease
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type 1 | `MONDO:0009265` | Gaucher disease type I | `AGREES` |
| Type 2 | `MONDO:0009266` | Gaucher disease type II | `AGREES` |
| Type 3 | `MONDO:0009267` | Gaucher disease type III | `AGREES` |

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

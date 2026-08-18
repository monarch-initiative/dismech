# Feingold Syndrome

Boomer grounding analysis for [`kb/disorders/Feingold_Syndrome.yaml`](../../../../kb/disorders/Feingold_Syndrome.yaml).

- **Entry term:** [`MONDO:0015267`](http://purl.obolibrary.org/obo/MONDO_0015267) Feingold syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type 1 | `MONDO:0008115` | Feingold syndrome type 1 | `AGREES` |
| Type 2 | `MONDO:0013691` | Feingold syndrome type 2 | `AGREES` |

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

# Citrullinemia Type I

Boomer grounding analysis for [`kb/disorders/Citrullinemia_Type_I.yaml`](../../../../kb/disorders/Citrullinemia_Type_I.yaml).

- **Entry term:** [`MONDO:0008988`](http://purl.obolibrary.org/obo/MONDO_0008988) citrullinemia type I
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Acute neonatal | `MONDO:0016600` | acute neonatal citrullinemia type I | `AGREES` |
| Late-onset | `MONDO:0016601` | adult-onset citrullinemia type I | `AGREES` |

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

# Tuberous Sclerosis Complex

Boomer grounding analysis for [`kb/disorders/Tuberous_Sclerosis_Complex.yaml`](../../../../kb/disorders/Tuberous_Sclerosis_Complex.yaml).

- **Entry term:** [`MONDO:0001734`](http://purl.obolibrary.org/obo/MONDO_0001734) tuberous sclerosis
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| TSC2 | `MONDO:0013199` | tuberous sclerosis 2 | `AGREES` |
| TSC1 | `MONDO:0008612` | tuberous sclerosis 1 | `AGREES` |

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

# Toxoplasmosis

Boomer grounding analysis for [`kb/disorders/Toxoplasmosis.yaml`](../../../../kb/disorders/Toxoplasmosis.yaml).

- **Entry term:** [`MONDO:0005989`](http://purl.obolibrary.org/obo/MONDO_0005989) toxoplasmosis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Congenital | `MONDO:0005715` | congenital toxoplasmosis | `AGREES` |
| Ocular | `MONDO:0005879` | ocular toxoplasmosis | `AGREES` |
| Reactivation | `MONDO:0005697` | cerebral toxoplasmosis | `AGREES` |

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

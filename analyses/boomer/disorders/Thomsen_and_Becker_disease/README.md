# Thomsen and Becker disease

Boomer grounding analysis for [`kb/disorders/Thomsen_and_Becker_disease.yaml`](../../../../kb/disorders/Thomsen_and_Becker_disease.yaml).

- **Entry term:** [`MONDO:0009710`](http://purl.obolibrary.org/obo/MONDO_0009710) Thomsen and Becker disease
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Thomsen disease | `MONDO:0008055` | myotonia congenita, autosomal dominant | `AGREES` |

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

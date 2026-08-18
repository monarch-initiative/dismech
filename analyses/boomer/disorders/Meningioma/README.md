# Meningioma

Boomer grounding analysis for [`kb/disorders/Meningioma.yaml`](../../../../kb/disorders/Meningioma.yaml).

- **Entry term:** [`MONDO:0016642`](http://purl.obolibrary.org/obo/MONDO_0016642) meningioma
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| WHO Grade I | `MONDO:0003054` | benign meningioma | `AGREES` |
| WHO Grade II | `MONDO:0045056` | grade II meningioma | `AGREES` |
| WHO Grade III | `MONDO:0020635` | anaplastic meningioma | `AGREES` |

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

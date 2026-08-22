# Anaplastic Large Cell Lymphoma

Boomer grounding analysis for [`kb/disorders/Anaplastic_Large_Cell_Lymphoma.yaml`](../../../../kb/disorders/Anaplastic_Large_Cell_Lymphoma.yaml).

- **Entry term:** [`MONDO:0020325`](http://purl.obolibrary.org/obo/MONDO_0020325) anaplastic large cell lymphoma
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Systemic ALK-Positive | `MONDO:0017602` | ALK-positive anaplastic large cell lymphoma | `AGREES` | ✓ NCIT, ORDO |
| Systemic ALK-Negative | `MONDO:0017603` | ALK-negative anaplastic large cell lymphoma | `AGREES` | ✓ NCIT, ORDO |
| Primary Cutaneous | `MONDO:0017598` | primary cutaneous anaplastic large cell lymphoma | `AGREES` | ✓ NCIT |

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

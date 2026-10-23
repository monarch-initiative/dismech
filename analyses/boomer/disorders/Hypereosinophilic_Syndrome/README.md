# Hypereosinophilic syndrome

Boomer grounding analysis for [`kb/disorders/Hypereosinophilic_Syndrome.yaml`](../../../../kb/disorders/Hypereosinophilic_Syndrome.yaml).

- **Entry term:** [`MONDO:0015691`](http://purl.obolibrary.org/obo/MONDO_0015691) hypereosinophilic syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Primary HES | `MONDO:0017833` | primary hypereosinophilic syndrome | `AGREES` | ✓ ORDO |
| Lymphocytic HES | `MONDO:0017835` | lymphocytic hypereosinophilic syndrome | `AGREES` | ✓ ORDO, icd11f |
| Idiopathic HES | `MONDO:0011895` | idiopathic hypereosinophilic syndrome | `AGREES` | ✓ ICD10CM, ORDO |

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

# Ocular Melanoma

Boomer grounding analysis for [`kb/disorders/Ocular_Melanoma.yaml`](../../../../kb/disorders/Ocular_Melanoma.yaml).

- **Entry term:** [`MONDO:0006325`](http://purl.obolibrary.org/obo/MONDO_0006325) ocular melanoma
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Uveal Melanoma | `MONDO:0006486` | uveal melanoma | `AGREES` |
| Choroidal Melanoma | `MONDO:0003878` | malignant choroid melanoma | `AGREES` |
| Ciliary Body Melanoma | `MONDO:0003912` | malignant ciliary body melanoma | `AGREES` |
| Iris Melanoma | `MONDO:0004064` | iris melanoma | `AGREES` |
| Conjunctival Melanoma | `MONDO:0002096` | malignant conjunctival melanoma | `AGREES` |

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

# Familial Nonmedullary Thyroid Carcinoma

Boomer grounding analysis for [`kb/disorders/Familial_Nonmedullary_Thyroid_Carcinoma.yaml`](../../../../kb/disorders/Familial_Nonmedullary_Thyroid_Carcinoma.yaml).

- **Entry term:** [`MONDO:0017896`](http://purl.obolibrary.org/obo/MONDO_0017896) familial nonmedullary thyroid carcinoma
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| TCO | `MONDO:0011312` | thyroid carcinoma, nonmedullary, with or without cell oxyphilia | `AGREES` |
| fPTC-PRN | `MONDO:0011578` | familial papillary thyroid carcinoma with renal papillary neoplasia | `AGREES` |
| NMTC1 | `MONDO:0008567` | thyroid cancer, nonmedullary, 1 | `AGREES` |

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

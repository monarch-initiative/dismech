# Pituitary Tumor

Boomer grounding analysis for [`kb/disorders/Pituitary_Tumor.yaml`](../../../../kb/disorders/Pituitary_Tumor.yaml).

- **Entry term:** [`MONDO:0017611`](http://purl.obolibrary.org/obo/MONDO_0017611) pituitary tumor
- **Grounded subtypes:** 7
- **Verdicts:** AGREES 7

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Lactotroph | `MONDO:0003430` | prolactin producing pituitary tumor | `AGREES` | — no shared vocabulary |
| Somatotroph | `MONDO:0006238` | growth hormone-producing pituitary gland adenoma | `AGREES` | ✓ NCIT, ORDO |
| Corticotroph | `MONDO:0006068` | ACTH-producing pituitary gland adenoma | `AGREES` | ✓ NCIT |
| Thyrotroph | `MONDO:0003837` | TSH producing pituitary tumor | `AGREES` | ✓ NCIT |
| Non-Functioning | `MONDO:0003603` | non-functioning pituitary gland neoplasm | `AGREES` | — no shared vocabulary |
| Posterior Pituitary | `MONDO:0003257` | posterior pituitary gland neoplasm | `AGREES` | ✓ NCIT |
| Pituitary Carcinoma | `MONDO:0002109` | pituitary cancer | `AGREES` | ✓ NCIT |

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

# Large Cell Neuroendocrine Carcinoma

Boomer grounding analysis for [`kb/disorders/Large_Cell_Neuroendocrine_Carcinoma.yaml`](../../../../kb/disorders/Large_Cell_Neuroendocrine_Carcinoma.yaml).

- **Entry term:** [`MONDO:0005057`](http://purl.obolibrary.org/obo/MONDO_0005057) large cell neuroendocrine carcinoma
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Pulmonary LCNEC | `MONDO:0003960` | pulmonary large cell neuroendocrine carcinoma | `AGREES` | ✓ NCIT |
| Combined Pulmonary LCNEC | `MONDO:0004142` | lung combined large cell neuroendocrine carcinoma | `AGREES` | ✓ NCIT |
| Thymic LCNEC | `MONDO:0003047` | thymic large cell neuroendocrine carcinoma | `AGREES` | ✓ NCIT |
| Cervical LCNEC | `MONDO:0006138` | cervical large cell neuroendocrine carcinoma | `AGREES` | ✓ NCIT |
| Pancreatic LCNEC | `MONDO:0006347` | pancreatic large cell neuroendocrine carcinoma | `AGREES` | ✓ NCIT |
| Breast LCNEC | `MONDO:0003959` | breast large cell neuroendocrine carcinoma | `AGREES` | ✓ NCIT |

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

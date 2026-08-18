# Thymic Neuroendocrine Carcinoma

Boomer grounding analysis for [`kb/disorders/Thymic_Neuroendocrine_Carcinoma.yaml`](../../../../kb/disorders/Thymic_Neuroendocrine_Carcinoma.yaml).

- **Entry term:** [`MONDO:0020516`](http://purl.obolibrary.org/obo/MONDO_0020516) thymic neuroendocrine carcinoma
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Typical carcinoid | `MONDO:0016976` | well-differentiated thymic neuroendocrine carcinoma | `AGREES` |
| Atypical carcinoid | `MONDO:0016977` | moderately-differentiated thymic neuroendocrine carcinoma | `AGREES` |
| LCNEC | `MONDO:0003047` | thymic large cell neuroendocrine carcinoma | `AGREES` |
| Small cell carcinoma | `MONDO:0004122` | thymus small cell carcinoma | `AGREES` |

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

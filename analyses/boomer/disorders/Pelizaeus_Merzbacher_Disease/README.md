# Pelizaeus-Merzbacher Disease

Boomer grounding analysis for [`kb/disorders/Pelizaeus_Merzbacher_Disease.yaml`](../../../../kb/disorders/Pelizaeus_Merzbacher_Disease.yaml).

- **Entry term:** [`MONDO:0010714`](http://purl.obolibrary.org/obo/MONDO_0010714) Pelizaeus-Merzbacher spectrum disorder
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Classic Pelizaeus-Merzbacher Disease | `MONDO:0017222` | Pelizaeus-Merzbacher disease, classic form | `AGREES` | ✓ ORDO, icd11f |
| Connatal Pelizaeus-Merzbacher Disease | `MONDO:0017221` | Pelizaeus-Merzbacher disease, connatal form | `AGREES` | ✓ ORDO, icd11f |
| Transitional Pelizaeus-Merzbacher Disease | `MONDO:0017223` | Pelizaeus-Merzbacher disease, transitional form | `AGREES` | ✓ ORDO, icd11f |
| Female Carrier Pelizaeus-Merzbacher Disease | `MONDO:0017224` | Pelizaeus-Merzbacher disease in female carriers | `AGREES` | ✓ ORDO, icd11f |

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

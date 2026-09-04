# Embryonal Carcinoma

Boomer grounding analysis for [`kb/disorders/Embryonal_Carcinoma.yaml`](../../../../kb/disorders/Embryonal_Carcinoma.yaml).

- **Entry term:** [`MONDO:0005440`](http://purl.obolibrary.org/obo/MONDO_0005440) embryonal carcinoma
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Testicular EC | `MONDO:0006446` | testicular embryonal carcinoma | `AGREES` | ✓ DOID, NCIT |
| Ovarian EC | `MONDO:0003581` | ovarian embryonal carcinoma | `AGREES` | ✓ DOID, NCIT |
| CNS EC | `MONDO:0018843` | embryonal carcinoma of the central nervous system | `AGREES` | ✓ DOID, NCIT, ORDO |
| Non-CNS-localized EC | `MONDO:0017328` | non-central nervous system-localized embryonal carcinoma | `AGREES` | ✓ ORDO |

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

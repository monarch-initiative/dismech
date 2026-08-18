# Coronary Artery Congenital Malformation

Boomer grounding analysis for [`kb/disorders/Coronary_Artery_Congenital_Malformation.yaml`](../../../../kb/disorders/Coronary_Artery_Congenital_Malformation.yaml).

- **Entry term:** [`MONDO:0015203`](http://purl.obolibrary.org/obo/MONDO_0015203) coronary artery congenital malformation
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| AAOCA | `MONDO:0020426` | malposition of the coronary ostium | `AGREES` |
| ALCAPA | `MONDO:0000811` | anomalous left coronary artery from the pulmonary artery | `AGREES` |
| Coronary Artery Fistula | `MONDO:0016081` | coronary arterial fistulas | `AGREES` |
| Congenital Coronary Atresia | `MONDO:0020423` | stenosis or atrophy of the coronary ostium | `AGREES` |

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

# Vulvar Adenocarcinoma

Boomer grounding analysis for [`kb/disorders/Vulvar_Adenocarcinoma.yaml`](../../../../kb/disorders/Vulvar_Adenocarcinoma.yaml).

- **Entry term:** [`MONDO:0024336`](http://purl.obolibrary.org/obo/MONDO_0024336) vulvar adenocarcinoma
- **Grounded subtypes:** 9
- **Verdicts:** AGREES 9

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Bartholin Gland Adenocarcinoma | `MONDO:0003853` | Bartholin gland adenocarcinoma | `AGREES` |
| Paget-Associated | `MONDO:0002207` | vulval Paget disease | `AGREES` |
| Vulvar Sebaceous Carcinoma | `MONDO:0003636` | vulvar sebaceous carcinoma | `AGREES` |
| Vulvar Eccrine Adenocarcinoma | `MONDO:0003861` | vulvar eccrine adenocarcinoma | `AGREES` |
| Vulvar Eccrine Porocarcinoma | `MONDO:0004281` | vulvar eccrine porocarcinoma | `AGREES` |
| Vulvar Apocrine Adenocarcinoma | `MONDO:0003881` | vulvar apocrine adenocarcinoma | `AGREES` |
| Skene Gland Origin | `MONDO:0004173` | adenocarcinoma of skene gland origin | `AGREES` |
| Vulvar Clear Cell Hidradenocarcinoma | `MONDO:0004283` | vulvar clear cell hidradenocarcinoma | `AGREES` |
| Bartholin Gland Adenoid Cystic Carcinoma | `MONDO:0003187` | Bartholin gland adenoid cystic carcinoma | `AGREES` |

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

# Malignant Germ Cell Tumor of Ovary

Boomer grounding analysis for [`kb/disorders/Malignant_Germ_Cell_Tumor_of_Ovary.yaml`](../../../../kb/disorders/Malignant_Germ_Cell_Tumor_of_Ovary.yaml).

- **Entry term:** [`MONDO:0018171`](http://purl.obolibrary.org/obo/MONDO_0018171) malignant germ cell tumor of ovary
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Dysgerminoma | `MONDO:0003481` | dysgerminoma of ovary | `AGREES` |
| Yolk Sac Tumor | `MONDO:0006344` | ovarian yolk sac tumor | `AGREES` |
| Immature Teratoma | `MONDO:0018369` | immature ovarian teratoma | `AGREES` |
| Embryonal Carcinoma | `MONDO:0003581` | ovarian embryonal carcinoma | `AGREES` |
| Non-Gestational Choriocarcinoma | `MONDO:0004322` | non-gestational ovarian choriocarcinoma | `AGREES` |
| Mixed Malignant Germ Cell Tumor | `MONDO:0003710` | ovarian mixed germ cell neoplasm | `AGREES` |

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

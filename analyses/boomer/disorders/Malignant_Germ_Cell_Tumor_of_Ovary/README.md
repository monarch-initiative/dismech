# Malignant Germ Cell Tumor of Ovary

Boomer grounding analysis for [`kb/disorders/Malignant_Germ_Cell_Tumor_of_Ovary.yaml`](../../../../kb/disorders/Malignant_Germ_Cell_Tumor_of_Ovary.yaml).

- **Entry term:** [`MONDO:0018171`](http://purl.obolibrary.org/obo/MONDO_0018171) malignant germ cell tumor of ovary
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Dysgerminoma | `MONDO:0003481` | dysgerminoma of ovary | `AGREES` | ✓ NCIT |
| Yolk Sac Tumor | `MONDO:0006344` | ovarian yolk sac tumor | `AGREES` | ✓ DOID, NCIT |
| Immature Teratoma | `MONDO:0018369` | immature ovarian teratoma | `AGREES` | ✓ DOID, NCIT |
| Embryonal Carcinoma | `MONDO:0003581` | ovarian embryonal carcinoma | `AGREES` | ✓ NCIT |
| Non-Gestational Choriocarcinoma | `MONDO:0004322` | non-gestational ovarian choriocarcinoma | `AGREES` | ✓ DOID, NCIT |
| Mixed Malignant Germ Cell Tumor | `MONDO:0003710` | ovarian mixed germ cell neoplasm | `AGREES` | ✓ DOID, NCIT |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0018369` ≡ `NCIT:C8111`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

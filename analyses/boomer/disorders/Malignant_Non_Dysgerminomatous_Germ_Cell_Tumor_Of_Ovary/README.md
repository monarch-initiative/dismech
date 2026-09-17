# Malignant Non-Dysgerminomatous Germ Cell Tumor Of Ovary

Boomer grounding analysis for [`kb/disorders/Malignant_Non_Dysgerminomatous_Germ_Cell_Tumor_Of_Ovary.yaml`](../../../../kb/disorders/Malignant_Non_Dysgerminomatous_Germ_Cell_Tumor_Of_Ovary.yaml).

- **Entry term:** [`MONDO:0016096`](http://purl.obolibrary.org/obo/MONDO_0016096) malignant non-dysgerminomatous germ cell tumor of ovary
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Embryonal Carcinoma | `MONDO:0003581` | ovarian embryonal carcinoma | `AGREES` | ✓ NCIT |

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

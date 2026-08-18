# Mixed Neuronal-Glial Tumor

Boomer grounding analysis for [`kb/disorders/Mixed_Neuronal-Glial_Tumor.yaml`](../../../../kb/disorders/Mixed_Neuronal-Glial_Tumor.yaml).

- **Entry term:** [`MONDO:0016729`](http://purl.obolibrary.org/obo/MONDO_0016729) mixed neuronal-glial tumor
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Ganglioglioma | `MONDO:0016733` | ganglioglioma | `AGREES` |
| Gangliocytoma | `MONDO:0016730` | gangliocytoma | `AGREES` |
| DNET | `MONDO:0005505` | dysembryoplastic neuroepithelial tumor | `AGREES` |
| Papillary Glioneuronal Tumor | `MONDO:0016735` | papillary glioneuronal tumor | `AGREES` |
| Rosette-forming Glioneuronal Tumor | `MONDO:0016736` | rosette-forming glioneuronal tumor of fourth ventricule | `AGREES` |
| Desmoplastic Infantile Ganglioglioma | `MONDO:0022965` | desmoplastic infantile ganglioglioma | `AGREES` |

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

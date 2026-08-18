# Malignant Peripheral Nerve Sheath Tumor

Boomer grounding analysis for [`kb/disorders/Malignant_Peripheral_Nerve_Sheath_Tumor.yaml`](../../../../kb/disorders/Malignant_Peripheral_Nerve_Sheath_Tumor.yaml).

- **Entry term:** [`MONDO:0017827`](http://purl.obolibrary.org/obo/MONDO_0017827) malignant peripheral nerve sheath tumor
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Epithelioid | `MONDO:0004540` | epithelioid malignant peripheral nerve sheath tumor | `AGREES` | ✓ DOID, NCIT |
| Malignant Triton Tumor | `MONDO:0016757` | malignant triton tumor | `AGREES` | ✓ DOID, NCIT, ORDO |

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

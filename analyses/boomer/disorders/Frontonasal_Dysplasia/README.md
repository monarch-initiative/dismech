# Frontonasal Dysplasia

Boomer grounding analysis for [`kb/disorders/Frontonasal_Dysplasia.yaml`](../../../../kb/disorders/Frontonasal_Dysplasia.yaml).

- **Entry term:** [`MONDO:0016643`](http://purl.obolibrary.org/obo/MONDO_0016643) frontonasal dysplasia
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Frontorhiny | `MONDO:0007636` | frontorhiny | `AGREES` | ✓ DOID, ORDO |
| Frontonasal dysplasia with alopecia and genital anomaly | `MONDO:0013268` | frontonasal dysplasia with alopecia and genital anomaly | `AGREES` | ✓ DOID, ORDO |
| Frontonasal dysplasia - severe microphthalmia - severe facial clefting syndrome | `MONDO:0013271` | frontonasal dysplasia - severe microphthalmia - severe facial clefting syndrome | `AGREES` | ✓ DOID, ORDO |

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

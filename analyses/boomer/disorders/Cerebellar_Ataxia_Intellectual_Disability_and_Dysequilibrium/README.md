# Cerebellar Ataxia, Intellectual Disability, and Dysequilibrium Syndrome

Boomer grounding analysis for [`kb/disorders/Cerebellar_Ataxia_Intellectual_Disability_and_Dysequilibrium.yaml`](../../../../kb/disorders/Cerebellar_Ataxia_Intellectual_Disability_and_Dysequilibrium.yaml).

- **Entry term:** [`MONDO:0009133`](http://purl.obolibrary.org/obo/MONDO_0009133) cerebellar ataxia, intellectual disability, and dysequilibrium
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| CAMRQ1 | `MONDO:0024542` | cerebellar ataxia, intellectual disability, and dysequilibrium syndrome 1 | `AGREES` | ✓ DOID |
| CAMRQ2 | `MONDO:0012430` | cerebellar ataxia, intellectual disability, and dysequilibrium syndrome 2 | `AGREES` | ✓ DOID |
| CAMRQ3 | `MONDO:0013188` | cerebellar ataxia, intellectual disability, and dysequilibrium syndrome 3 | `AGREES` | silent (DOID, MESH) |
| CAMRQ4 | `MONDO:0014104` | cerebellar ataxia, intellectual disability, and dysequilibrium syndrome 4 | `AGREES` | ✓ DOID |

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

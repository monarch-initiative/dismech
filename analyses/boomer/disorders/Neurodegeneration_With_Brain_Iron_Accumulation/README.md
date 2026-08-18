# Neurodegeneration With Brain Iron Accumulation

Boomer grounding analysis for [`kb/disorders/Neurodegeneration_With_Brain_Iron_Accumulation.yaml`](../../../../kb/disorders/Neurodegeneration_With_Brain_Iron_Accumulation.yaml).

- **Entry term:** [`MONDO:0018307`](http://purl.obolibrary.org/obo/MONDO_0018307) neurodegeneration with brain iron accumulation
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| PKAN | `MONDO:0009319` | pantothenate kinase-associated neurodegeneration | `AGREES` |
| PLAN | `MONDO:0017998` | PLA2G6-associated neurodegeneration | `AGREES` |
| BPAN | `MONDO:0010476` | neurodegeneration with brain iron accumulation 5 | `AGREES` |
| MPAN | `MONDO:0013674` | neurodegeneration with brain iron accumulation 4 | `AGREES` |
| Aceruloplasminemia | `MONDO:0011426` | aceruloplasminemia | `AGREES` |
| Neuroferritinopathy | `MONDO:0011638` | neuroferritinopathy | `AGREES` |

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

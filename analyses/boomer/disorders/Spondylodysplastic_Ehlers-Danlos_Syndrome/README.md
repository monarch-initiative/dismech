# Spondylodysplastic Ehlers-Danlos Syndrome

Boomer grounding analysis for [`kb/disorders/Spondylodysplastic_Ehlers-Danlos_Syndrome.yaml`](../../../../kb/disorders/Spondylodysplastic_Ehlers-Danlos_Syndrome.yaml).

- **Entry term:** [`MONDO:0007526`](http://purl.obolibrary.org/obo/MONDO_0007526) Ehlers-Danlos syndrome, spondylodysplastic type
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| spEDS-B4GALT7 | `MONDO:0020682` | Ehlers-Danlos syndrome, spondylodysplastic type, 1 | `AGREES` | silent (DOID) |
| spEDS-B3GALT6 | `MONDO:0014139` | Ehlers-Danlos syndrome, spondylodysplastic type, 2 | `AGREES` | silent (ORDO) |
| spEDS-SLC39A13 | `MONDO:0012873` | Ehlers-Danlos syndrome, spondylocheirodysplastic type | `AGREES` | silent (DOID, MESH, ORDO) |

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

# Multiple Epiphyseal Dysplasia

Boomer grounding analysis for [`kb/disorders/Multiple_Epiphyseal_Dysplasia.yaml`](../../../../kb/disorders/Multiple_Epiphyseal_Dysplasia.yaml).

- **Entry term:** [`MONDO:0016648`](http://purl.obolibrary.org/obo/MONDO_0016648) multiple epiphyseal dysplasia
- **Grounded subtypes:** 7
- **Verdicts:** AGREES 7

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| EDM1 | `MONDO:0007561` | multiple epiphyseal dysplasia type 1 | `AGREES` |
| EDM2 | `MONDO:0010844` | epiphyseal dysplasia, multiple, 2 | `AGREES` |
| EDM3 | `MONDO:0010964` | epiphyseal dysplasia, multiple, 3 | `AGREES` |
| EDM5 | `MONDO:0011765` | multiple epiphyseal dysplasia type 5 | `AGREES` |
| EDM6 | `MONDO:0013591` | epiphyseal dysplasia, multiple, 6 | `AGREES` |
| rMED | `MONDO:0009189` | multiple epiphyseal dysplasia type 4 | `AGREES` |
| EDM7 | `MONDO:0054680` | epiphyseal dysplasia, multiple, 7 | `AGREES` |

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

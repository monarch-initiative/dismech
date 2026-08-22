# Split Hand-Foot Malformation

Boomer grounding analysis for [`kb/disorders/Split_Hand_Foot_Malformation.yaml`](../../../../kb/disorders/Split_Hand_Foot_Malformation.yaml).

- **Entry term:** [`MONDO:0016576`](http://purl.obolibrary.org/obo/MONDO_0016576) split hand-foot malformation
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| SHFM1 | `MONDO:0008464` | split hand-foot malformation 1 | `AGREES` | ✓ DOID, NCIT |
| SHFM3 | `MONDO:0009525` | split hand-foot malformation 3 | `AGREES` | ✓ DOID, NCIT |
| SHFM4 | `MONDO:0011535` | split hand-foot malformation 4 | `AGREES` | ✓ DOID |
| SHFM5 | `MONDO:0011709` | split hand-foot malformation 5 | `AGREES` | ✓ DOID, NCIT |
| SHFM6 | `MONDO:0009157` | split hand-foot malformation 6 | `AGREES` | ✓ DOID |

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

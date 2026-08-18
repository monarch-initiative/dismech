# familial hyperaldosteronism

Boomer grounding analysis for [`kb/disorders/Familial_Hyperaldosteronism.yaml`](../../../../kb/disorders/Familial_Hyperaldosteronism.yaml).

- **Entry term:** [`MONDO:0016525`](http://purl.obolibrary.org/obo/MONDO_0016525) familial hyperaldosteronism
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type I | `MONDO:0007080` | glucocorticoid-remediable aldosteronism | `AGREES` |
| Type II | `MONDO:0011576` | familial hyperaldosteronism type II | `AGREES` |
| Type III | `MONDO:0013359` | familial hyperaldosteronism type III | `AGREES` |
| Type IV | `MONDO:0014875` | hyperaldosteronism, familial, type IV | `AGREES` |

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

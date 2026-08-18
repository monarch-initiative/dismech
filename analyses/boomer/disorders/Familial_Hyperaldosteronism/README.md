# familial hyperaldosteronism

Boomer grounding analysis for [`kb/disorders/Familial_Hyperaldosteronism.yaml`](../../../../kb/disorders/Familial_Hyperaldosteronism.yaml).

- **Entry term:** [`MONDO:0016525`](http://purl.obolibrary.org/obo/MONDO_0016525) familial hyperaldosteronism
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type I | `MONDO:0007080` | glucocorticoid-remediable aldosteronism | `AGREES` | ✓ ORDO |
| Type II | `MONDO:0011576` | familial hyperaldosteronism type II | `AGREES` | ✓ NCIT, ORDO |
| Type III | `MONDO:0013359` | familial hyperaldosteronism type III | `AGREES` | ✓ ORDO |
| Type IV | `MONDO:0014875` | hyperaldosteronism, familial, type IV | `AGREES` | ✓ ORDO |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0016525` ≡ `ORDO:235936`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

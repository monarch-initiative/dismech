# Familial Renal Glucosuria

Boomer grounding analysis for [`kb/disorders/Familial_Renal_Glucosuria.yaml`](../../../../kb/disorders/Familial_Renal_Glucosuria.yaml).

- **Entry term:** [`MONDO:0009297`](http://purl.obolibrary.org/obo/MONDO_0009297) familial renal glucosuria
- **Grounded subtypes:** 2
- **Verdicts:** SAME_TERM 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| SLC5A2-Related | `MONDO:0009297` | familial renal glucosuria | `SAME_TERM` |
| PDZK1IP1-Related | `MONDO:0009297` | familial renal glucosuria | `SAME_TERM` |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Familial_Renal_Glucosuria` ≡ `MONDO:0009297`
- `dismech:Familial_Renal_Glucosuria#SLC5A2-Related` ≡ `MONDO:0009297`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`SAME_TERM`** - Subtype and entry are grounded to the same MONDO term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

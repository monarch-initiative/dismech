# GABRG2-Related Epilepsy

Boomer grounding analysis for [`kb/disorders/GABRG2-Related_Epilepsy.yaml`](../../../../kb/disorders/GABRG2-Related_Epilepsy.yaml).

- **Entry term:** [`MONDO:0032725`](http://purl.obolibrary.org/obo/MONDO_0032725) developmental and epileptic encephalopathy, 74
- **Grounded subtypes:** 1
- **Verdicts:** SAME_TERM 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| DEE74 | `MONDO:0032725` | developmental and epileptic encephalopathy, 74 | `SAME_TERM` |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:GABRG2-Related_Epilepsy` ≡ `MONDO:0032725`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`SAME_TERM`** - Subtype and entry are grounded to the same MONDO term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

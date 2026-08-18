# GNAO1-Related Developmental and Epileptic Encephalopathy

Boomer grounding analysis for [`kb/disorders/GNAO1-Related_Developmental_and_Epileptic_Encephalopathy.yaml`](../../../../kb/disorders/GNAO1-Related_Developmental_and_Epileptic_Encephalopathy.yaml).

- **Entry term:** [`MONDO:0014199`](http://purl.obolibrary.org/obo/MONDO_0014199) developmental and epileptic encephalopathy, 17
- **Grounded subtypes:** 2
- **Verdicts:** SAME_TERM 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| DEE17 | `MONDO:0014199` | developmental and epileptic encephalopathy, 17 | `SAME_TERM` |
| NEDIM | `MONDO:0060491` | neurodevelopmental disorder with involuntary movements | `SILENT` |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:GNAO1-Related_Developmental_and_Epileptic_Encephalopathy` ≡ `MONDO:0014199`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.
- **`SAME_TERM`** - Subtype and entry are grounded to the same MONDO term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

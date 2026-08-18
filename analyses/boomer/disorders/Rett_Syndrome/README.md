# Rett Syndrome

Boomer grounding analysis for [`kb/disorders/Rett_Syndrome.yaml`](../../../../kb/disorders/Rett_Syndrome.yaml).

- **Entry term:** [`MONDO:0010726`](http://purl.obolibrary.org/obo/MONDO_0010726) Rett syndrome
- **Grounded subtypes:** 2
- **Verdicts:** SAME_TERM 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Classic Rett Syndrome | `MONDO:0010726` | Rett syndrome | `SAME_TERM` |
| Atypical Rett Syndrome | `MONDO:0017746` | atypical Rett syndrome | `SILENT` |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Rett_Syndrome` ≡ `MONDO:0010726`

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
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

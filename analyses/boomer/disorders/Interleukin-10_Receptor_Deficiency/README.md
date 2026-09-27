# Interleukin-10 Receptor Deficiency

Boomer grounding analysis for [`kb/disorders/Interleukin-10_Receptor_Deficiency.yaml`](../../../../kb/disorders/Interleukin-10_Receptor_Deficiency.yaml).

- **Entry term:** [`MONDO:0013153`](http://purl.obolibrary.org/obo/MONDO_0013153) inflammatory bowel disease 28
- **Grounded subtypes:** 2
- **Verdicts:** SAME_TERM 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| IL10RA deficiency | `MONDO:0013153` | inflammatory bowel disease 28 | `SAME_TERM` | ✓ DOID, NCIT, OMIM |
| IL10RB deficiency | `MONDO:0012941` | inflammatory bowel disease 25 | `SILENT` | silent (DOID, MESH, OMIM) |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Interleukin-10_Receptor_Deficiency#IL10RA deficiency` ≡ `MONDO:0013153`

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

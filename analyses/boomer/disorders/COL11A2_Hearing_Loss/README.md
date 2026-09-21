# COL11A2-Related Hearing Loss

Boomer grounding analysis for [`kb/disorders/COL11A2_Hearing_Loss.yaml`](../../../../kb/disorders/COL11A2_Hearing_Loss.yaml).

- **Entry term:** [`MONDO:0011159`](http://purl.obolibrary.org/obo/MONDO_0011159) autosomal dominant nonsyndromic hearing loss 13
- **Grounded subtypes:** 2
- **Verdicts:** SAME_TERM 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| DFNA13 | `MONDO:0011159` | autosomal dominant nonsyndromic hearing loss 13 | `SAME_TERM` | ✓ DOID, OMIM |
| DFNB53 | `MONDO:0012333` | autosomal recessive nonsyndromic hearing loss 53 | `SILENT` | silent (DOID, MESH, OMIM) |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:COL11A2_Hearing_Loss#DFNA13` ≡ `MONDO:0011159`

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

# Hypotrichosis with Juvenile Macular Dystrophy

Boomer grounding analysis for [`kb/disorders/Hypotrichosis_with_Juvenile_Macular_Dystrophy.yaml`](../../../../kb/disorders/Hypotrichosis_with_Juvenile_Macular_Dystrophy.yaml).

- **Entry term:** [`MONDO:0011107`](http://purl.obolibrary.org/obo/MONDO_0011107) congenital hypotrichosis with juvenile macular dystrophy
- **Grounded subtypes:** 2
- **Verdicts:** SAME_TERM 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| HJMD | `MONDO:0011107` | congenital hypotrichosis with juvenile macular dystrophy | `SAME_TERM` | ✓ DOID, OMIM, ORDO |
| EEM | `MONDO:0009155` | EEM syndrome | `SILENT` | silent (DOID, MESH, OMIM, ORDO) |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Hypotrichosis_with_Juvenile_Macular_Dystrophy#HJMD` ≡ `MONDO:0011107`

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

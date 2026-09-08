# Developmental and Epileptic Encephalopathy 14

Boomer grounding analysis for [`kb/disorders/Developmental_And_Epileptic_Encephalopathy_14.yaml`](../../../../kb/disorders/Developmental_And_Epileptic_Encephalopathy_14.yaml).

- **Entry term:** [`MONDO:0013989`](http://purl.obolibrary.org/obo/MONDO_0013989) developmental and epileptic encephalopathy, 14
- **Grounded subtypes:** 1
- **Verdicts:** SILENT 1
- **Mendelian selection:** KB_CATEGORY_MENDELIAN

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| ADSHE | `MONDO:0014002` | autosomal dominant nocturnal frontal lobe epilepsy 5 | `SILENT` | silent (DOID, OMIM) |

## What boomer did

The solver has **not been run** for this input. No mapping acceptance,
retraction, posterior probability or global-consistency result is asserted.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

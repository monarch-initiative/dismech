# SPOP-Related Neurodevelopmental Disorder

Boomer grounding analysis for [`kb/disorders/SPOP-Related_Neurodevelopmental_Disorder.yaml`](../../../../kb/disorders/SPOP-Related_Neurodevelopmental_Disorder.yaml).

- **Entry term:** [`MONDO:0032942`](http://purl.obolibrary.org/obo/MONDO_0032942) neurodevelopmental disorder with microcephaly and dysmorphic facies
- **Grounded subtypes:** 2
- **Verdicts:** SAME_TERM 1, SILENT 1
- **Mendelian selection:** KB_CATEGORY_MENDELIAN

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Type 1 | `MONDO:0032942` | neurodevelopmental disorder with microcephaly and dysmorphic facies | `SAME_TERM` | ✓ OMIM, ORDO |
| Type 2 | `MONDO:0032943` | neurodevelopmental disorder with relative macrocephaly and with or without cardiac or endocrine anomalies | `SILENT` | silent (OMIM, ORDO) |

## What boomer did

The solver has **not been run** for this input. No mapping acceptance,
retraction, posterior probability or global-consistency result is asserted.

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

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

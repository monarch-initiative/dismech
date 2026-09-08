# Dyskeratosis Congenita

Boomer grounding analysis for [`kb/disorders/Dyskeratosis_Congenita.yaml`](../../../../kb/disorders/Dyskeratosis_Congenita.yaml).

- **Entry term:** [`MONDO:0015780`](http://purl.obolibrary.org/obo/MONDO_0015780) dyskeratosis congenita
- **Grounded subtypes:** 1
- **Verdicts:** SILENT 1
- **Mendelian selection:** KB_CATEGORY_MENDELIAN

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PFBMFT8 | `MONDO:0957263` | pulmonary fibrosis and/or bone marrow failure syndrome, telomere-related, 8 | `SILENT` | — no shared vocabulary |

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

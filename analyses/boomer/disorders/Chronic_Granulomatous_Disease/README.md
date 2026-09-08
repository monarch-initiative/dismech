# Chronic Granulomatous Disease

Boomer grounding analysis for [`kb/disorders/Chronic_Granulomatous_Disease.yaml`](../../../../kb/disorders/Chronic_Granulomatous_Disease.yaml).

- **Entry term:** [`MONDO:0018305`](http://purl.obolibrary.org/obo/MONDO_0018305) chronic granulomatous disease
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6
- **Mendelian selection:** KB_CATEGORY_MENDELIAN

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| X-linked CYBB | `MONDO:0010600` | granulomatous disease, chronic, X-linked | `AGREES` | ✓ DOID |
| AR p47phox NCF1 | `MONDO:0009309` | granulomatous disease, chronic, autosomal recessive, cytochrome b-positive, type 1 | `AGREES` | ✓ DOID |
| AR p22phox CYBA | `MONDO:0009308` | granulomatous disease, chronic, autosomal recessive, cytochrome b-negative | `AGREES` | ✓ DOID |
| AR p67phox NCF2 | `MONDO:0009310` | granulomatous disease, chronic, autosomal recessive, cytochrome b-positive, type 2 | `AGREES` | ✓ DOID |
| AR p40phox NCF4 | `MONDO:0013507` | granulomatous disease, chronic, autosomal recessive, cytochrome b-positive, type 3 | `AGREES` | ✓ DOID |
| AR CYBC1 EROS | `MONDO:0030066` | granulomatous disease, chronic, autosomal recessive, 5 | `AGREES` | ✓ DOID |

## What boomer did

The solver has **not been run** for this input. No mapping acceptance,
retraction, posterior probability or global-consistency result is asserted.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

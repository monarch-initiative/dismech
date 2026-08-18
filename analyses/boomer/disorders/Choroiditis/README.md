# Choroiditis

Boomer grounding analysis for [`kb/disorders/Choroiditis.yaml`](../../../../kb/disorders/Choroiditis.yaml).

- **Entry term:** [`MONDO:0001280`](http://purl.obolibrary.org/obo/MONDO_0001280) choroiditis
- **Grounded subtypes:** 8
- **Verdicts:** SILENT 6, AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Ocular Toxoplasmosis | `MONDO:0005879` | ocular toxoplasmosis | `SILENT` |
| Tubercular Choroiditis | `MONDO:0006876` | ocular tuberculosis | `SILENT` |
| Presumed Ocular Histoplasmosis Syndrome | `MONDO:0001263` | histoplasmosis retinitis | `SILENT` |
| Birdshot Chorioretinopathy | `MONDO:0011599` | birdshot chorioretinopathy | `SILENT` |
| Multifocal Choroiditis with Panuveitis | `MONDO:0023833` | multifocal choroiditis | `AGREES` |
| Punctate Inner Choroidopathy | `MONDO:0035584` | punctate inner choroidopathy | `SILENT` |
| Serpiginous Choroiditis | `MONDO:0018152` | serpiginous choroiditis | `AGREES` |
| Sympathetic Ophthalmia | `MONDO:0019198` | sympathetic ophthalmia | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

6 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

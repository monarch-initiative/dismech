# Uveitis

Boomer grounding analysis for [`kb/disorders/Uveitis.yaml`](../../../../kb/disorders/Uveitis.yaml).

- **Entry term:** [`MONDO:0020283`](http://purl.obolibrary.org/obo/MONDO_0020283) uveitis
- **Grounded subtypes:** 8
- **Verdicts:** AGREES 7, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Anterior Uveitis | `MONDO:0006651` | anterior uveitis | `AGREES` | ✓ DOID, MESH, NCIT, ORDO |
| Intermediate Uveitis | `MONDO:0006806` | intermediate uveitis | `AGREES` | ✓ DOID, MESH, NCIT, ORDO |
| Pars Planitis | `MONDO:0011644` | pars planitis | `AGREES` | ✓ MESH |
| Posterior Uveitis | `MONDO:0006918` | posterior uveitis | `AGREES` | ✓ DOID, MESH |
| Choroiditis | `MONDO:0001280` | choroiditis | `AGREES` | ✓ MESH, NCIT, ORDO |
| Ocular Toxoplasmosis | `MONDO:0005879` | ocular toxoplasmosis | `SILENT` | silent (EFO, MESH) |
| Cytomegalovirus Retinitis | `MONDO:0000878` | cytomegalovirus retinitis | `AGREES` | silent (DOID, EFO, MESH, NCIT) |
| Panuveitis | `MONDO:0017255` | panuveitis | `AGREES` | ✓ DOID, MESH, NCIT, ORDO |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
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

# Paroxysmal Dyskinesia

Boomer grounding analysis for [`kb/disorders/Paroxysmal_Dyskinesia.yaml`](../../../../kb/disorders/Paroxysmal_Dyskinesia.yaml).

- **Entry term:** [`MONDO:0015427`](http://purl.obolibrary.org/obo/MONDO_0015427) paroxysmal dyskinesia
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 4, SILENT 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PKD | `MONDO:0044202` | episodic kinesigenic dyskinesia | `AGREES` | ✓ ORDO |
| PNKD | `MONDO:0700088` | paroxysmal nonkinesigenic dyskinesia | `AGREES` | ✓ ORDO |
| PED | `MONDO:0012805` | childhood onset GLUT1 deficiency syndrome 2 | `AGREES` | ✓ ORDO |
| PNKD3 | `MONDO:0012276` | generalized epilepsy-paroxysmal dyskinesia syndrome | `SILENT` | silent (ORDO) |
| ADCY5 | `MONDO:0800028` | dyskinesia with orofacial involvement, autosomal dominant | `SILENT` | silent (ORDO) |
| ICCA | `MONDO:0011178` | infantile convulsions and choreoathetosis | `AGREES` | ✓ ORDO |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

2 subtype(s) are `SILENT`: MONDO asserts no path between the
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

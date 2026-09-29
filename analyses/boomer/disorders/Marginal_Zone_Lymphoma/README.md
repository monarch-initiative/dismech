# Marginal Zone Lymphoma

Boomer grounding analysis for [`kb/disorders/Marginal_Zone_Lymphoma.yaml`](../../../../kb/disorders/Marginal_Zone_Lymphoma.yaml).

- **Entry term:** [`MONDO:0017604`](http://purl.obolibrary.org/obo/MONDO_0017604) marginal zone lymphoma
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Extranodal MZL | `MONDO:0007650` | MALT lymphoma | `AGREES` | ✓ DOID, NCIT, ORDO |
| Splenic MZL | `MONDO:0019462` | splenic marginal zone lymphoma | `AGREES` | ✓ DOID, NCIT, ORDO |
| Nodal MZL | `MONDO:0019465` | nodal marginal zone B-cell lymphoma | `AGREES` | ✓ DOID, NCIT, ORDO |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

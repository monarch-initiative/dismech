# Cerebral Palsy

Boomer grounding analysis for [`kb/disorders/Cerebral_Palsy.yaml`](../../../../kb/disorders/Cerebral_Palsy.yaml).

- **Entry term:** [`MONDO:0006497`](http://purl.obolibrary.org/obo/MONDO_0006497) cerebral palsy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Spastic | `MONDO:0000396` | spastic cerebral palsy | `AGREES` | ✓ DOID, NCIT, icd11f |
| Dyskinetic | `MONDO:0022697` | athetoid cerebral palsy | `AGREES` | ✓ DOID, ICD10CM, NCIT |
| Ataxic | `MONDO:0000397` | ataxic cerebral palsy | `AGREES` | ✓ DOID, ICD10CM, NCIT, icd11f |
| Mixed | `MONDO:0000400` | mixed cerebral palsy | `AGREES` | ✓ DOID, NCIT, icd11f |

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

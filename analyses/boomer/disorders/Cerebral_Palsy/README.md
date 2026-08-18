# Cerebral Palsy

Boomer grounding analysis for [`kb/disorders/Cerebral_Palsy.yaml`](../../../../kb/disorders/Cerebral_Palsy.yaml).

- **Entry term:** [`MONDO:0006497`](http://purl.obolibrary.org/obo/MONDO_0006497) cerebral palsy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Spastic | `MONDO:0000396` | spastic cerebral palsy | `AGREES` |
| Dyskinetic | `MONDO:0022697` | athetoid cerebral palsy | `AGREES` |
| Ataxic | `MONDO:0000397` | ataxic cerebral palsy | `AGREES` |
| Mixed | `MONDO:0000400` | mixed cerebral palsy | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

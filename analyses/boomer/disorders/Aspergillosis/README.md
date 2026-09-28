# Aspergillosis

Boomer grounding analysis for [`kb/disorders/Aspergillosis.yaml`](../../../../kb/disorders/Aspergillosis.yaml).

- **Entry term:** [`MONDO:0005657`](http://purl.obolibrary.org/obo/MONDO_0005657) aspergillosis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Invasive | `MONDO:0000240` | invasive aspergillosis | `AGREES` | ✓ DOID, icd11f |
| Aspergilloma | `MONDO:0000266` | pulmonary aspergilloma | `AGREES` | ✓ DOID, MESH |
| ABPA | `MONDO:0015243` | allergic bronchopulmonary aspergillosis | `AGREES` | ✓ DOID, ICD10CM, MESH, NCIT, icd11f |

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

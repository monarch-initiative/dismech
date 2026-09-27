# Neurofibromatosis

Boomer grounding analysis for [`kb/disorders/Neurofibromatosis.yaml`](../../../../kb/disorders/Neurofibromatosis.yaml).

- **Entry term:** [`MONDO:0021061`](http://purl.obolibrary.org/obo/MONDO_0021061) neurofibromatosis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| NF1 | `MONDO:0018975` | neurofibromatosis type 1 | `AGREES` | ✓ DOID, ICD10CM, MESH, NCIT |
| NF2 | `MONDO:0007039` | NF2-related schwannomatosis | `AGREES` | ✓ ICD10CM, NCIT |
| Schwannomatosis | `MONDO:0008075` | schwannomatosis | `AGREES` | ✓ ICD10CM |

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

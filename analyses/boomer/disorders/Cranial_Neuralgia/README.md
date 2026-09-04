# Cranial Neuralgia

Boomer grounding analysis for [`kb/disorders/Cranial_Neuralgia.yaml`](../../../../kb/disorders/Cranial_Neuralgia.yaml).

- **Entry term:** [`MONDO:0016374`](http://purl.obolibrary.org/obo/MONDO_0016374) cranial neuralgia
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Trigeminal | `MONDO:0008599` | trigeminal neuralgia | `AGREES` | ✓ ORDO |
| Glossopharyngeal | `MONDO:0016372` | glossopharyngeal neuralgia | `AGREES` | ✓ ORDO |

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

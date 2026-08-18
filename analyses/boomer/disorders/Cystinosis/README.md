# Cystinosis

Boomer grounding analysis for [`kb/disorders/Cystinosis.yaml`](../../../../kb/disorders/Cystinosis.yaml).

- **Entry term:** [`MONDO:0016239`](http://purl.obolibrary.org/obo/MONDO_0016239) cystinosis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Nephropathic infantile cystinosis | `MONDO:0100151` | nephropathic cystinosis | `AGREES` |
| Nephropathic juvenile cystinosis | `MONDO:0009066` | juvenile nephropathic cystinosis | `AGREES` |
| Non-nephropathic ocular cystinosis | `MONDO:0009064` | ocular cystinosis | `AGREES` |

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

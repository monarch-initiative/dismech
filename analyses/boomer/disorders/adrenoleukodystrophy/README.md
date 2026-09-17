# adrenoleukodystrophy

Boomer grounding analysis for [`kb/disorders/adrenoleukodystrophy.yaml`](../../../../kb/disorders/adrenoleukodystrophy.yaml).

- **Entry term:** [`MONDO:0018544`](http://purl.obolibrary.org/obo/MONDO_0018544) adrenoleukodystrophy
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Childhood cerebral adrenoleukodystrophy | `MONDO:0010247` | X-linked cerebral adrenoleukodystrophy | `AGREES` | ✓ ORDO, icd11f |
| Adrenomyeloneuropathy | `MONDO:0015339` | adrenomyeloneuropathy | `AGREES` | ✓ ORDO, icd11f |

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

# Growth Hormone Insensitivity Syndrome

Boomer grounding analysis for [`kb/disorders/Growth_Hormone_Insensitivity_Syndrome.yaml`](../../../../kb/disorders/Growth_Hormone_Insensitivity_Syndrome.yaml).

- **Entry term:** [`MONDO:0015892`](http://purl.obolibrary.org/obo/MONDO_0015892) growth hormone insensitivity syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Laron Syndrome | `MONDO:0009877` | Laron syndrome | `AGREES` |
| IGF1 Deficiency | `MONDO:0012110` | growth delay due to insulin-like growth factor type 1 deficiency | `AGREES` |

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

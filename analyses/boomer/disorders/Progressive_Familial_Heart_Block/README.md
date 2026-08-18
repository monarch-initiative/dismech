# Progressive Familial Heart Block

Boomer grounding analysis for [`kb/disorders/Progressive_Familial_Heart_Block.yaml`](../../../../kb/disorders/Progressive_Familial_Heart_Block.yaml).

- **Entry term:** [`MONDO:0019490`](http://purl.obolibrary.org/obo/MONDO_0019490) progressive familial heart block
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type 1A | `MONDO:0007240` | progressive familial heart block, type 1A | `AGREES` |
| Type 1B | `MONDO:0011474` | progressive familial heart block type IB | `AGREES` |

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

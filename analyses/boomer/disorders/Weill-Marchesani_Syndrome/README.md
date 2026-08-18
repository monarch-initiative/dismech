# Weill-Marchesani syndrome

Boomer grounding analysis for [`kb/disorders/Weill-Marchesani_Syndrome.yaml`](../../../../kb/disorders/Weill-Marchesani_Syndrome.yaml).

- **Entry term:** [`MONDO:0018096`](http://purl.obolibrary.org/obo/MONDO_0018096) Weill-Marchesani syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| WMS1 | `MONDO:0010194` | Weill-Marchesani syndrome 1 | `AGREES` |
| WMS2 | `MONDO:0012013` | Weill-Marchesani syndrome 2, dominant | `AGREES` |
| WMS3 | `MONDO:0013899` | Weill-Marchesani syndrome 3 | `AGREES` |
| WMS4 | `MONDO:0013176` | Weill-Marchesani 4 syndrome, recessive | `AGREES` |

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

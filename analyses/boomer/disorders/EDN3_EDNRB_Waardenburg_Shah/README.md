# EDN3/EDNRB Waardenburg-Shah

Boomer grounding analysis for [`kb/disorders/EDN3_EDNRB_Waardenburg_Shah.yaml`](../../../../kb/disorders/EDN3_EDNRB_Waardenburg_Shah.yaml).

- **Entry term:** [`MONDO:0019518`](http://purl.obolibrary.org/obo/MONDO_0019518) Waardenburg-Shah syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Waardenburg Syndrome Type 4A | `MONDO:0010192` | Waardenburg syndrome type 4A | `AGREES` |
| Waardenburg Syndrome Type 4B | `MONDO:0013201` | Waardenburg syndrome type 4B | `AGREES` |

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

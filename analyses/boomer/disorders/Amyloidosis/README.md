# Amyloidosis

Boomer grounding analysis for [`kb/disorders/Amyloidosis.yaml`](../../../../kb/disorders/Amyloidosis.yaml).

- **Entry term:** [`MONDO:0019065`](http://purl.obolibrary.org/obo/MONDO_0019065) amyloidosis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| AL | `MONDO:0019438` | AL amyloidosis | `AGREES` |
| ATTRwt | `MONDO:0018018` | wild type ATTR amyloidosis | `AGREES` |
| AA | `MONDO:0019439` | AA amyloidosis | `AGREES` |

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

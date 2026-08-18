# COFS Syndrome

Boomer grounding analysis for [`kb/disorders/COFS_Syndrome.yaml`](../../../../kb/disorders/COFS_Syndrome.yaml).

- **Entry term:** [`MONDO:0008926`](http://purl.obolibrary.org/obo/MONDO_0008926) COFS syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| COFS1 | `MONDO:0008955` | cerebrooculofacioskeletal syndrome 1 | `AGREES` |
| COFS2 | `MONDO:0012553` | cerebrooculofacioskeletal syndrome 2 | `AGREES` |
| COFS3 | `MONDO:0014696` | cerebrooculofacioskeletal syndrome 3 | `AGREES` |
| COFS4 | `MONDO:0012554` | cerebrooculofacioskeletal syndrome 4 | `AGREES` |

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

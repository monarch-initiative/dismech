# Kleefstra Syndrome

Boomer grounding analysis for [`kb/disorders/Kleefstra_Syndrome.yaml`](../../../../kb/disorders/Kleefstra_Syndrome.yaml).

- **Entry term:** [`MONDO:0012455`](http://purl.obolibrary.org/obo/MONDO_0012455) Kleefstra syndrome
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Kleefstra syndrome 1 | `MONDO:0027407` | Kleefstra syndrome 1 | `AGREES` |
| Kleefstra syndrome due to 9q34 microdeletion | `MONDO:0019896` | Kleefstra syndrome due to 9q34 microdeletion | `AGREES` |
| Kleefstra syndrome due to a point mutation | `MONDO:0016865` | Kleefstra syndrome due to a point mutation | `AGREES` |
| Kleefstra syndrome 2 | `MONDO:0054701` | Kleefstra syndrome 2 | `AGREES` |

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

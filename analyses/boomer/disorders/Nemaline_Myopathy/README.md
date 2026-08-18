# Nemaline Myopathy

Boomer grounding analysis for [`kb/disorders/Nemaline_Myopathy.yaml`](../../../../kb/disorders/Nemaline_Myopathy.yaml).

- **Entry term:** [`MONDO:0018958`](http://purl.obolibrary.org/obo/MONDO_0018958) nemaline myopathy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Severe Congenital Nemaline Myopathy | `MONDO:0015735` | severe congenital nemaline myopathy | `AGREES` |
| Typical Nemaline Myopathy | `MONDO:0015737` | typical nemaline myopathy | `AGREES` |
| Childhood-Onset Nemaline Myopathy | `MONDO:0015738` | childhood-onset nemaline myopathy | `AGREES` |
| Adult-Onset Nemaline Myopathy | `MONDO:0015739` | adult-onset nemaline myopathy | `AGREES` |

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

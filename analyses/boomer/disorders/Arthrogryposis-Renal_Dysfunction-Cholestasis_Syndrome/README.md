# Arthrogryposis-Renal Dysfunction-Cholestasis Syndrome

Boomer grounding analysis for [`kb/disorders/Arthrogryposis-Renal_Dysfunction-Cholestasis_Syndrome.yaml`](../../../../kb/disorders/Arthrogryposis-Renal_Dysfunction-Cholestasis_Syndrome.yaml).

- **Entry term:** [`MONDO:0017123`](http://purl.obolibrary.org/obo/MONDO_0017123) arthrogryposis-renal dysfunction-cholestasis syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| ARCS1 | `MONDO:0008822` | arthrogryposis, renal dysfunction, and cholestasis 1 | `AGREES` |
| ARCS2 | `MONDO:0013255` | arthrogryposis, renal dysfunction, and cholestasis 2 | `AGREES` |

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

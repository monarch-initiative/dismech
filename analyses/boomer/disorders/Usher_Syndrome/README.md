# Usher Syndrome

Boomer grounding analysis for [`kb/disorders/Usher_Syndrome.yaml`](../../../../kb/disorders/Usher_Syndrome.yaml).

- **Entry term:** [`MONDO:0019501`](http://purl.obolibrary.org/obo/MONDO_0019501) Usher syndrome
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| USH1 | `MONDO:0010168` | Usher syndrome type 1 | `AGREES` |
| USH2 | `MONDO:0016484` | Usher syndrome type 2 | `AGREES` |
| USH3 | `MONDO:0016485` | Usher syndrome type 3 | `AGREES` |

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

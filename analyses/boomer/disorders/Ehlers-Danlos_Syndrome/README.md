# Ehlers-Danlos Syndrome

Boomer grounding analysis for [`kb/disorders/Ehlers-Danlos_Syndrome.yaml`](../../../../kb/disorders/Ehlers-Danlos_Syndrome.yaml).

- **Entry term:** [`MONDO:0020066`](http://purl.obolibrary.org/obo/MONDO_0020066) Ehlers-Danlos syndrome
- **Grounded subtypes:** 1
- **Verdicts:** AGREES 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Classical EDS | `MONDO:0007522` | Ehlers-Danlos syndrome, classic type | `AGREES` | ✓ ORDO |

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

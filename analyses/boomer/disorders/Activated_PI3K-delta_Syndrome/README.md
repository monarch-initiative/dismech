# Activated PI3K-delta syndrome

Boomer grounding analysis for [`kb/disorders/Activated_PI3K-delta_Syndrome.yaml`](../../../../kb/disorders/Activated_PI3K-delta_Syndrome.yaml).

- **Entry term:** [`MONDO:0018338`](http://purl.obolibrary.org/obo/MONDO_0018338) activated PI3K-delta syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| APDS1 | `MONDO:0014222` | immunodeficiency 14 | `AGREES` | ✓ ORDO |
| APDS2 | `MONDO:0014453` | immunodeficiency 36 with lymphoproliferation | `AGREES` | ✓ ORDO |

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

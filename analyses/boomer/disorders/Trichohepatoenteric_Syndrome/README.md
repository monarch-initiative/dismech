# Trichohepatoenteric Syndrome

Boomer grounding analysis for [`kb/disorders/Trichohepatoenteric_Syndrome.yaml`](../../../../kb/disorders/Trichohepatoenteric_Syndrome.yaml).

- **Entry term:** [`MONDO:0009105`](http://purl.obolibrary.org/obo/MONDO_0009105) trichohepatoenteric syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| THES type 1 | `MONDO:0024541` | trichohepatoenteric syndrome 1 | `AGREES` | ✓ DOID |
| THES type 2 | `MONDO:0013818` | trichohepatoenteric syndrome 2 | `AGREES` | ✓ DOID |

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

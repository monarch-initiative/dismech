# POLR-Related Leukodystrophy

Boomer grounding analysis for [`kb/disorders/POLR-Related_Leukodystrophy.yaml`](../../../../kb/disorders/POLR-Related_Leukodystrophy.yaml).

- **Entry term:** [`MONDO:0100605`](http://purl.obolibrary.org/obo/MONDO_0100605) POLR-related leukodystrophy
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| POLR3A | `MONDO:0011897` | leukodystrophy, hypomyelinating, 7, with or without oligodontia and/or hypogonadotropic hypogonadism | `AGREES` |
| POLR3B | `MONDO:0013722` | hypomyelinating leukodystrophy 8 with or without oligodontia and-or hypogonadotropic hypogonadism | `AGREES` |
| POLR1C | `MONDO:0014666` | hypomyelinating leukodystrophy 11 | `AGREES` |

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

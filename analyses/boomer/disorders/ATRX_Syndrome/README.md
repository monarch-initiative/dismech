# ATR-X-Related Syndrome

Boomer grounding analysis for [`kb/disorders/ATRX_Syndrome.yaml`](../../../../kb/disorders/ATRX_Syndrome.yaml).

- **Entry term:** [`MONDO:0016980`](http://purl.obolibrary.org/obo/MONDO_0016980) ATR-X-related syndrome
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Alpha-Thalassemia X-Linked Intellectual Disability Syndrome | `MONDO:0010519` | alpha thalassemia-X-linked intellectual disability syndrome | `AGREES` | — no shared vocabulary |
| Intellectual Disability-Hypotonic Facies Syndrome, X-Linked 1 | `MONDO:0010663` | intellectual disability-hypotonic facies syndrome, X-linked, 1 | `AGREES` | — no shared vocabulary |

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

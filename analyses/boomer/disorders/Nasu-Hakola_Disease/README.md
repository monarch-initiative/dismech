# Nasu-Hakola Disease

Boomer grounding analysis for [`kb/disorders/Nasu-Hakola_Disease.yaml`](../../../../kb/disorders/Nasu-Hakola_Disease.yaml).

- **Entry term:** [`MONDO:0009092`](http://purl.obolibrary.org/obo/MONDO_0009092) polycystic lipomembranous osteodysplasia with sclerosing leukoencephaly
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PLOSL1 | `MONDO:0020749` | polycystic lipomembranous osteodysplasia with sclerosing leukoencephalopathy 1 | `AGREES` | — no shared vocabulary |
| PLOSL2 | `MONDO:0020750` | polycystic lipomembranous osteodysplasia with sclerosing leukoencephalopathy 2 | `AGREES` | — no shared vocabulary |

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

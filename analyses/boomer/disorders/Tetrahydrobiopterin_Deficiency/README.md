# Tetrahydrobiopterin Deficiency

Boomer grounding analysis for [`kb/disorders/Tetrahydrobiopterin_Deficiency.yaml`](../../../../kb/disorders/Tetrahydrobiopterin_Deficiency.yaml).

- **Entry term:** [`MONDO:0016543`](http://purl.obolibrary.org/obo/MONDO_0016543) hyperphenylalaninemia due to tetrahydrobiopterin deficiency
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 4, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| PTPS Deficiency | `MONDO:0009863` | BH4-deficient hyperphenylalaninemia A | `AGREES` |
| DHPR Deficiency | `MONDO:0009862` | dihydropteridine reductase deficiency | `AGREES` |
| GTPCH Deficiency | `MONDO:0100186` | GTP cyclohydrolase I deficiency with hyperphenylalaninemia | `AGREES` |
| PCD Deficiency | `MONDO:0009908` | pterin-4 alpha-carbinolamine dehydratase 1 deficiency | `AGREES` |
| SPR Deficiency | `MONDO:0012994` | dopa-responsive dystonia due to sepiapterin reductase deficiency | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

# Joubert syndrome

Boomer grounding analysis for [`kb/disorders/Joubert_syndrome.yaml`](../../../../kb/disorders/Joubert_syndrome.yaml).

- **Entry term:** [`MONDO:0018772`](http://purl.obolibrary.org/obo/MONDO_0018772) Joubert syndrome
- **Grounded subtypes:** 39
- **Verdicts:** AGREES 38, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Joubert syndrome 1 | `MONDO:0008944` | Joubert syndrome 1 | `AGREES` |
| Joubert syndrome 2 | `MONDO:0011963` | Joubert syndrome 2 | `AGREES` |
| Joubert syndrome 3 | `MONDO:0012078` | Joubert syndrome 3 | `AGREES` |
| Joubert syndrome with renal defect | `MONDO:0012308` | Joubert syndrome with renal defect | `AGREES` |
| Joubert syndrome with oculorenal defect | `MONDO:0009480` | Joubert syndrome with oculorenal defect | `SILENT` |
| Joubert syndrome 5 | `MONDO:0012432` | Joubert syndrome 5 | `AGREES` |
| Joubert syndrome 6 | `MONDO:0012539` | Joubert syndrome 6 | `AGREES` |
| Joubert syndrome 7 | `MONDO:0012694` | Joubert syndrome 7 | `AGREES` |
| Joubert syndrome 9 | `MONDO:0012849` | Joubert syndrome 9 | `AGREES` |
| Joubert syndrome 8 | `MONDO:0012855` | Joubert syndrome 8 | `AGREES` |
| Joubert syndrome 13 | `MONDO:0013608` | Joubert syndrome 13 | `AGREES` |
| Joubert syndrome 14 | `MONDO:0013745` | Joubert syndrome 14 | `AGREES` |
| Joubert syndrome 15 | `MONDO:0013763` | Joubert syndrome 15 | `AGREES` |
| Joubert syndrome 16 | `MONDO:0013764` | Joubert syndrome 16 | `AGREES` |
| Joubert syndrome 17 | `MONDO:0013824` | Joubert syndrome 17 | `AGREES` |
| Joubert syndrome 18 | `MONDO:0013896` | Joubert syndrome 18 | `AGREES` |
| Joubert syndrome 20 | `MONDO:0013994` | Joubert syndrome 20 | `AGREES` |
| Joubert syndrome 21 | `MONDO:0014288` | Joubert syndrome 21 | `AGREES` |
| Joubert syndrome 22 | `MONDO:0014297` | Joubert syndrome 22 | `AGREES` |
| Joubert syndrome 23 | `MONDO:0014664` | Joubert syndrome 23 | `AGREES` |
| Joubert syndrome 24 | `MONDO:0014724` | Joubert syndrome 24 | `AGREES` |
| Joubert syndrome 25 | `MONDO:0014770` | Joubert syndrome 25 | `AGREES` |
| Joubert syndrome 26 | `MONDO:0014771` | Joubert syndrome 26 | `AGREES` |
| Joubert syndrome 27 | `MONDO:0014927` | Joubert syndrome 27 | `AGREES` |
| Joubert syndrome 28 | `MONDO:0014928` | Joubert syndrome 28 | `AGREES` |
| Joubert syndrome 38 | `MONDO:0030353` | Joubert syndrome 38 | `AGREES` |
| Joubert syndrome 39 | `MONDO:0030454` | Joubert syndrome 39 | `AGREES` |
| Joubert syndrome 40 | `MONDO:0030462` | Joubert syndrome 40 | `AGREES` |
| Joubert syndrome 37 | `MONDO:0030933` | Joubert syndrome 37 | `AGREES` |
| Joubert syndrome 35 | `MONDO:0032570` | Joubert syndrome 35 | `AGREES` |
| Joubert syndrome 36 | `MONDO:0032902` | Joubert syndrome 36 | `AGREES` |
| Joubert syndrome 30 | `MONDO:0033308` | Joubert syndrome 30 | `AGREES` |
| Joubert syndrome 32 | `MONDO:0033309` | Joubert syndrome 32 | `AGREES` |
| Joubert syndrome 31 | `MONDO:0033310` | Joubert syndrome 31 | `AGREES` |
| Joubert syndrome 33 | `MONDO:0033311` | Joubert syndrome 33 | `AGREES` |
| Joubert syndrome 19 | `MONDO:0800363` | Joubert syndrome 19 | `AGREES` |
| Joubert syndrome 29 | `MONDO:0800372` | Joubert syndrome 29 | `AGREES` |
| Joubert syndrome 11 | `MONDO:0800382` | Joubert syndrome 11 | `AGREES` |
| Joubert syndrome 34 | `MONDO:0800383` | Joubert syndrome 34 | `AGREES` |

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

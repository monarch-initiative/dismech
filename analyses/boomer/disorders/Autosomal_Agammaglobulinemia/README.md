# Autosomal Agammaglobulinemia

Boomer grounding analysis for [`kb/disorders/Autosomal_Agammaglobulinemia.yaml`](../../../../kb/disorders/Autosomal_Agammaglobulinemia.yaml).

- **Entry term:** [`MONDO:0011096`](http://purl.obolibrary.org/obo/MONDO_0011096) autosomal agammaglobulinemia
- **Grounded subtypes:** 12
- **Verdicts:** AGREES 8, SILENT 4

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| AGM1 | `MONDO:0020729` | autosomal recessive agammaglobulinemia 1 | `AGREES` |
| AGM2 | `MONDO:0013287` | agammaglobulinemia 2, autosomal recessive | `AGREES` |
| AGM3 | `MONDO:0013288` | agammaglobulinemia 3, autosomal recessive | `AGREES` |
| AGM4 | `MONDO:0013289` | agammaglobulinemia 4, autosomal recessive | `AGREES` |
| AGM5 | `MONDO:0013290` | agammaglobulinemia 5, autosomal dominant | `AGREES` |
| AGM6 | `MONDO:0012987` | agammaglobulinemia 6, autosomal recessive | `AGREES` |
| AGM7 | `MONDO:0014083` | agammaglobulinemia 7, autosomal recessive | `AGREES` |
| AGM8 | `MONDO:0014840` | agammaglobulinemia 8, autosomal dominant | `AGREES` |
| AGM8B | `MONDO:0859234` | agammaglobulinemia 8b, autosomal recessive | `SILENT` |
| AGM9 | `MONDO:0030519` | agammaglobulinemia 9, autosomal recessive | `SILENT` |
| AGM10 | `MONDO:0030529` | agammaglobulinemia 10, autosomal dominant | `SILENT` |
| FNIP1 | `MONDO:0100432` | FNIP1-associated syndrome | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

4 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.
- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

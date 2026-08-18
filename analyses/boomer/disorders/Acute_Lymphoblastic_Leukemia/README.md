# Acute Lymphoblastic Leukemia

Boomer grounding analysis for [`kb/disorders/Acute_Lymphoblastic_Leukemia.yaml`](../../../../kb/disorders/Acute_Lymphoblastic_Leukemia.yaml).

- **Entry term:** [`MONDO:0004967`](http://purl.obolibrary.org/obo/MONDO_0004967) acute lymphoblastic leukemia
- **Grounded subtypes:** 5
- **Verdicts:** SILENT 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Ph-positive | `MONDO:0035940` | B-lymphoblastic leukemia/lymphoma with t(9;22)(q34.1;q11.2) | `SILENT` |
| KMT2A-rearranged | `MONDO:0035941` | B-lymphoblastic leukemia/lymphoma with t(v;11q23.3) | `SILENT` |
| ETV6-RUNX1 | `MONDO:0035942` | B-lymphoblastic leukemia/lymphoma with t(12;21)(p13.2;q22.1) | `SILENT` |
| High hyperdiploidy | `MONDO:0035943` | B-lymphoblastic leukemia/lymphoma with hyperdiploidy | `SILENT` |
| Hypodiploidy | `MONDO:0035944` | B-lymphoblastic leukemia/lymphoma with hypodiploidy | `SILENT` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

5 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

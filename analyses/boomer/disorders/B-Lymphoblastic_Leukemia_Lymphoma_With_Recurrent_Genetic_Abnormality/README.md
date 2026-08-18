# B-Lymphoblastic Leukemia/Lymphoma With Recurrent Genetic Abnormality

Boomer grounding analysis for [`kb/disorders/B-Lymphoblastic_Leukemia_Lymphoma_With_Recurrent_Genetic_Abnormality.yaml`](../../../../kb/disorders/B-Lymphoblastic_Leukemia_Lymphoma_With_Recurrent_Genetic_Abnormality.yaml).

- **Entry term:** [`MONDO:0035605`](http://purl.obolibrary.org/obo/MONDO_0035605) B-lymphoblastic leukemia/lymphoma with recurrent genetic abnormality
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Ph-positive | `MONDO:0035940` | B-lymphoblastic leukemia/lymphoma with t(9;22)(q34.1;q11.2) | `AGREES` |
| KMT2A-rearranged | `MONDO:0035941` | B-lymphoblastic leukemia/lymphoma with t(v;11q23.3) | `AGREES` |
| ETV6-RUNX1 | `MONDO:0035942` | B-lymphoblastic leukemia/lymphoma with t(12;21)(p13.2;q22.1) | `AGREES` |
| High hyperdiploidy | `MONDO:0035943` | B-lymphoblastic leukemia/lymphoma with hyperdiploidy | `AGREES` |
| Hypodiploidy | `MONDO:0035944` | B-lymphoblastic leukemia/lymphoma with hypodiploidy | `AGREES` |
| IGH-IL3 | `MONDO:0035945` | B-lymphoblastic leukemia/lymphoma with t(5;14)(q31.1;q32.3) | `AGREES` |

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

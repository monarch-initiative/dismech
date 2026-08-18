# Spondylocostal Dysostosis

Boomer grounding analysis for [`kb/disorders/Spondylocostal_Dysostosis.yaml`](../../../../kb/disorders/Spondylocostal_Dysostosis.yaml).

- **Entry term:** [`MONDO:0000359`](http://purl.obolibrary.org/obo/MONDO_0000359) spondylocostal dysostosis
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| SCDO1 | `MONDO:0020692` | spondylocostal dysostosis 1, autosomal recessive | `AGREES` |
| SCDO2 | `MONDO:0012097` | spondylocostal dysostosis 2, autosomal recessive | `AGREES` |
| SCDO3 | `MONDO:0012349` | spondylocostal dysostosis 3, autosomal recessive | `AGREES` |
| SCDO4 | `MONDO:0013366` | spondylocostal dysostosis 4, autosomal recessive | `AGREES` |
| SCDO5 | `MONDO:0007389` | spondylocostal dysostosis 5 | `AGREES` |
| SCDO6 | `MONDO:0014694` | spondylocostal dysostosis 6, autosomal recessive | `AGREES` |

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

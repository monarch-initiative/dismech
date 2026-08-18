# Pilocytic Astrocytoma

Boomer grounding analysis for [`kb/disorders/Pilocytic_Astrocytoma.yaml`](../../../../kb/disorders/Pilocytic_Astrocytoma.yaml).

- **Entry term:** [`MONDO:0016691`](http://purl.obolibrary.org/obo/MONDO_0016691) pilocytic astrocytoma
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Childhood | `MONDO:0004000` | childhood pilocytic astrocytoma | `AGREES` |
| Cerebellar | `MONDO:0003168` | cerebellar pilocytic astrocytoma | `AGREES` |
| Pilomyxoid | `MONDO:0016692` | pilomyxoid astrocytoma | `AGREES` |

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

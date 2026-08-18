# Inherited Ichthyosis

Boomer grounding analysis for [`kb/disorders/Inherited_Ichthyosis.yaml`](../../../../kb/disorders/Inherited_Ichthyosis.yaml).

- **Entry term:** [`MONDO:0015947`](http://purl.obolibrary.org/obo/MONDO_0015947) inherited ichthyosis
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Ichthyosis Vulgaris | `MONDO:0024304` | ichthyosis vulgaris | `AGREES` |
| X-Linked Ichthyosis | `MONDO:0010622` | recessive X-linked ichthyosis | `AGREES` |
| Autosomal Recessive Congenital Ichthyosis | `MONDO:0017265` | autosomal recessive congenital ichthyosis | `AGREES` |
| Keratinopathic Ichthyosis | `MONDO:0017266` | keratinopathic ichthyosis | `AGREES` |
| Netherton Syndrome | `MONDO:0009735` | Netherton syndrome | `AGREES` |

## What boomer did

All identity mappings were accepted together - dismech's subtype hierarchy, the
mappings, and MONDO's hierarchy are jointly consistent for this entry.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

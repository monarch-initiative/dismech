# Small Intestine Cancer

Boomer grounding analysis for [`kb/disorders/Small_Intestine_Cancer.yaml`](../../../../kb/disorders/Small_Intestine_Cancer.yaml).

- **Entry term:** [`MONDO:0000956`](http://purl.obolibrary.org/obo/MONDO_0000956) small intestine cancer
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 3, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Adenocarcinoma | `MONDO:0003198` | small intestine adenocarcinoma | `AGREES` |
| Neuroendocrine Tumor | `MONDO:0002995` | small intestine neuroendocrine tumor, well differentiated, low or intermediate grade | `SILENT` |
| Lymphoma | `MONDO:0001852` | small intestine lymphoma | `AGREES` |
| Sarcoma | `MONDO:0003360` | small intestine leiomyosarcoma | `AGREES` |

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
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

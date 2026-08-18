# Frontotemporal Dementia

Boomer grounding analysis for [`kb/disorders/Frontotemporal_Dementia.yaml`](../../../../kb/disorders/Frontotemporal_Dementia.yaml).

- **Entry term:** [`MONDO:0017276`](http://purl.obolibrary.org/obo/MONDO_0017276) frontotemporal dementia
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 3, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Behavioral Variant FTD | `MONDO:0017160` | behavioral variant of frontotemporal dementia | `AGREES` |
| Semantic Variant PPA | `MONDO:0010857` | semantic dementia | `AGREES` |
| Nonfluent Variant PPA | `MONDO:0015059` | progressive non-fluent aphasia | `AGREES` |
| FTD with Motor Neuron Disease | `MONDO:0017161` | frontotemporal dementia with motor neuron disease | `SILENT` |

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

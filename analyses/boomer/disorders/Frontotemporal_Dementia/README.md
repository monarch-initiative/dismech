# Frontotemporal Dementia

Boomer grounding analysis for [`kb/disorders/Frontotemporal_Dementia.yaml`](../../../../kb/disorders/Frontotemporal_Dementia.yaml).

- **Entry term:** [`MONDO:0017276`](http://purl.obolibrary.org/obo/MONDO_0017276) frontotemporal dementia
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 3, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Behavioral Variant FTD | `MONDO:0017160` | behavioral variant of frontotemporal dementia | `AGREES` | ✓ ORDO |
| Semantic Variant PPA | `MONDO:0010857` | semantic dementia | `AGREES` | ✓ DOID, ORDO |
| Nonfluent Variant PPA | `MONDO:0015059` | progressive non-fluent aphasia | `AGREES` | ✓ DOID, ORDO |
| FTD with Motor Neuron Disease | `MONDO:0017161` | frontotemporal dementia with motor neuron disease | `SILENT` | ✓ icd11f |

### Corroborated elsewhere

MONDO asserts no relation for these, but at least one other ontology that
MONDO confirms an equivalency into does place the subtype under the parent.
That makes them evidenced MONDO gaps rather than open questions:

- **FTD with Motor Neuron Disease** — icd11f (icd11f:1171850356)

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0010857` ≡ `DOID:0081391`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

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

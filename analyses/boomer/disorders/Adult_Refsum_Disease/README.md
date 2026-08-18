# Adult Refsum Disease

Boomer grounding analysis for [`kb/disorders/Adult_Refsum_Disease.yaml`](../../../../kb/disorders/Adult_Refsum_Disease.yaml).

- **Entry term:** [`MONDO:0009958`](http://purl.obolibrary.org/obo/MONDO_0009958) adult Refsum disease
- **Grounded subtypes:** 2
- **Verdicts:** REVERSED 1, SILENT 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Type 1 | `MONDO:0100258` | phytanoyl-CoA hydroxylase deficiency | `REVERSED` |
| Type 2 | `MONDO:0100307` | adult Refsum disease due to PEX7 defect | `SILENT` |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Adult_Refsum_Disease` ≡ `MONDO:0009958`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

1 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.
- **`REVERSED`** - MONDO has the entry's term as a descendant of this subtype's term - backwards from dismech.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

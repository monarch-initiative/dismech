# SOX10 Neurocristopathy Spectrum

Boomer grounding analysis for [`kb/disorders/SOX10_Neurocristopathy_Spectrum.yaml`](../../../../kb/disorders/SOX10_Neurocristopathy_Spectrum.yaml).

- **Entry term:** [`MONDO:0013202`](http://purl.obolibrary.org/obo/MONDO_0013202) Waardenburg syndrome type 4C
- **Grounded subtypes:** 3
- **Verdicts:** SILENT 2, SAME_TERM 1

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Waardenburg Syndrome Type 2E | `MONDO:0012698` | Waardenburg syndrome type 2E | `SILENT` |
| Waardenburg Syndrome Type 4C | `MONDO:0013202` | Waardenburg syndrome type 4C | `SAME_TERM` |
| PCWH Syndrome | `MONDO:0012198` | PCWH syndrome | `SILENT` |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:SOX10_Neurocristopathy_Spectrum` ≡ `MONDO:0013202`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

2 subtype(s) are `SILENT`: MONDO asserts no path between the
terms in either direction. That is consistent (nothing is violated) but
uncorroborated, and generally indicates a missing `is_a` edge in MONDO rather
than a dismech error. These are candidate MONDO enrichment proposals.

## Verdict meanings

- **`SILENT`** - MONDO relates the two terms in neither direction - usually a missing MONDO `is_a` edge.
- **`SAME_TERM`** - Subtype and entry are grounded to the same MONDO term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

# Hypobetalipoproteinemia

Boomer grounding analysis for [`kb/disorders/Hypobetalipoproteinemia.yaml`](../../../../kb/disorders/Hypobetalipoproteinemia.yaml).

- **Entry term:** [`MONDO:0017774`](http://purl.obolibrary.org/obo/MONDO_0017774) hypobetalipoproteinemia
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| FHBL1 Heterozygous | `MONDO:0014252` | familial hypobetalipoproteinemia 1 | `AGREES` | ✓ DOID |
| FHBL1 Homozygous | `MONDO:0014252` | familial hypobetalipoproteinemia 1 | `AGREES` | ✓ DOID |
| ANGPTL3 Deficiency | `MONDO:0011505` | familial hypobetalipoproteinemia 2 | `AGREES` | ✓ DOID |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Hypobetalipoproteinemia#FHBL1 Heterozygous` ≡ `MONDO:0014252`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60 -C 6`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

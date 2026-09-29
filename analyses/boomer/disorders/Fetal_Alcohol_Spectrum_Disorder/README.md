# Fetal Alcohol Spectrum Disorder

Boomer grounding analysis for [`kb/disorders/Fetal_Alcohol_Spectrum_Disorder.yaml`](../../../../kb/disorders/Fetal_Alcohol_Spectrum_Disorder.yaml).

- **Entry term:** [`MONDO:0000408`](http://purl.obolibrary.org/obo/MONDO_0000408) fetal alcohol spectrum disorder
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| FAS | `MONDO:0016011` | fetal alcohol syndrome | `AGREES` | ✓ DOID |
| pFAS | `MONDO:0000393` | partial fetal alcohol syndrome | `AGREES` | ✓ DOID |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0016011` ≡ `DOID:0050665`

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

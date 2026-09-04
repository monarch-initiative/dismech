# Spotted fever rickettsiosis

Boomer grounding analysis for [`kb/disorders/Spotted_Fever_Rickettsiosis.yaml`](../../../../kb/disorders/Spotted_Fever_Rickettsiosis.yaml).

- **Entry term:** [`MONDO:0001195`](http://purl.obolibrary.org/obo/MONDO_0001195) spotted fever
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| RMSF | `MONDO:0019359` | Rocky mountain spotted fever | `AGREES` | ✓ DOID, ICD10CM, ORDO, icd11f |
| MSF | `MONDO:0024472` | boutonneuse fever | `AGREES` | ✓ DOID, ORDO, icd11f |
| ATBF | `MONDO:0000227` | African tick-bite fever | `AGREES` | ✓ DOID |
| Rickettsialpox | `MONDO:0019360` | rickettsialpox | `AGREES` | ✓ DOID, ORDO |
| QTT | `MONDO:0001118` | Queensland tick typhus | `AGREES` | ✓ DOID, ICD10CM, icd11f |
| NATT | `MONDO:0001154` | Siberian tick typhus | `AGREES` | ✓ DOID, ICD10CM, icd11f |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0024472` ≡ `ORDO:101334`

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

# Myiasis

Boomer grounding analysis for [`kb/disorders/Myiasis.yaml`](../../../../kb/disorders/Myiasis.yaml).

- **Entry term:** [`MONDO:0019147`](http://purl.obolibrary.org/obo/MONDO_0019147) myiasis
- **Grounded subtypes:** 9
- **Verdicts:** AGREES 9

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Furuncular | `MONDO:0018941` | furuncular myiasis | `AGREES` | ✓ ORDO, icd11f |
| Creeping | `MONDO:0018857` | creeping myiasis | `AGREES` | ✓ ORDO, icd11f |
| Wound | `MONDO:0015622` | wound myiasis | `AGREES` | ✓ ICD10CM, ORDO, icd11f |
| Ophthalmic | `MONDO:0000301` | ophthalmomyiasis | `AGREES` | ✓ DOID, icd11f |
| Nasopharyngeal | `MONDO:0015623` | cavitary myiasis | `AGREES` | ✓ ORDO |
| Oral | `MONDO:0015623` | cavitary myiasis | `AGREES` | ✓ ORDO |
| Aural | `MONDO:0015623` | cavitary myiasis | `AGREES` | ✓ ORDO |
| Intestinal | `MONDO:0015623` | cavitary myiasis | `AGREES` | ✓ ORDO |
| Urogenital | `MONDO:0015623` | cavitary myiasis | `AGREES` | ✓ ORDO |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Myiasis#Aural` ≡ `MONDO:0015623`
- `dismech:Myiasis#Nasopharyngeal` ≡ `MONDO:0015623`
- `dismech:Myiasis#Oral` ≡ `MONDO:0015623`
- `dismech:Myiasis#Urogenital` ≡ `MONDO:0015623`

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

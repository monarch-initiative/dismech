# Leishmaniasis

Boomer grounding analysis for [`kb/disorders/Leishmaniasis.yaml`](../../../../kb/disorders/Leishmaniasis.yaml).

- **Entry term:** [`MONDO:0011989`](http://purl.obolibrary.org/obo/MONDO_0011989) leishmaniasis
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Visceral leishmaniasis | `MONDO:0005445` | visceral leishmaniasis | `AGREES` | ✓ DOID, ICD10CM, MESH, NCIT, icd11f |
| Cutaneous leishmaniasis | `MONDO:0005446` | cutaneous leishmaniasis | `AGREES` | ✓ DOID, ICD10CM, MESH, NCIT, icd11f |
| Mucocutaneous leishmaniasis | `MONDO:0005859` | mucocutaneous leishmaniasis | `AGREES` | ✓ DOID, ICD10CM, MESH, NCIT, icd11f |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0005446` ≡ `NCIT:C34770`

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

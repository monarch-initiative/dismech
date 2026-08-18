# Autosomal dominant polycystic liver disease

Boomer grounding analysis for [`kb/disorders/Autosomal_Dominant_Polycystic_Liver_Disease.yaml`](../../../../kb/disorders/Autosomal_Dominant_Polycystic_Liver_Disease.yaml).

- **Entry term:** [`MONDO:0000447`](http://purl.obolibrary.org/obo/MONDO_0000447) autosomal dominant polycystic liver disease
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PCLD1 | `MONDO:0008265` | polycystic liver disease 1 | `AGREES` | ✓ DOID |
| PCLD2 | `MONDO:0014860` | polycystic liver disease 2 | `AGREES` | ✓ DOID |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0000447` ≡ `icd11f:423904268`

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

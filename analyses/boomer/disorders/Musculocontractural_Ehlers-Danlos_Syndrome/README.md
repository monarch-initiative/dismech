# Musculocontractural Ehlers-Danlos Syndrome

Boomer grounding analysis for [`kb/disorders/Musculocontractural_Ehlers-Danlos_Syndrome.yaml`](../../../../kb/disorders/Musculocontractural_Ehlers-Danlos_Syndrome.yaml).

- **Entry term:** [`MONDO:0011142`](http://purl.obolibrary.org/obo/MONDO_0011142) Ehlers-Danlos syndrome, musculocontractural type
- **Grounded subtypes:** 2
- **Verdicts:** AGREES 2

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| mcEDS-CHST14 | `MONDO:0020681` | Ehlers-Danlos syndrome, musculocontractural type 1 | `AGREES` | — no shared vocabulary |
| mcEDS-DSE | `MONDO:0014236` | Ehlers-Danlos syndrome, musculocontractural type 2 | `AGREES` | — no shared vocabulary |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0014236` ≡ `DOID:0080737`

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

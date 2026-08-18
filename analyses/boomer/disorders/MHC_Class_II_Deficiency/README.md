# MHC class II deficiency

Boomer grounding analysis for [`kb/disorders/MHC_Class_II_Deficiency.yaml`](../../../../kb/disorders/MHC_Class_II_Deficiency.yaml).

- **Entry term:** [`MONDO:0008855`](http://purl.obolibrary.org/obo/MONDO_0008855) MHC class II deficiency
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| MHC class II deficiency 1 | `MONDO:0971005` | MHC class II deficiency 1 | `AGREES` | — no shared vocabulary |
| MHC class II deficiency 2 | `MONDO:0971013` | MHC class II deficiency 2 | `AGREES` | — no shared vocabulary |
| MHC class II deficiency 3 | `MONDO:0971014` | MHC class II deficiency 3 | `AGREES` | — no shared vocabulary |
| MHC class II deficiency 4 | `MONDO:0971015` | MHC class II deficiency 4 | `AGREES` | — no shared vocabulary |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0008855` ≡ `NCIT:C3895`

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

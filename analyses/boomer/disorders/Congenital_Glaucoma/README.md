# Congenital Glaucoma

Boomer grounding analysis for [`kb/disorders/Congenital_Glaucoma.yaml`](../../../../kb/disorders/Congenital_Glaucoma.yaml).

- **Entry term:** [`MONDO:0020366`](http://purl.obolibrary.org/obo/MONDO_0020366) congenital glaucoma
- **Grounded subtypes:** 6
- **Verdicts:** AGREES 6

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| PCG | `MONDO:0000365` | primary congenital glaucoma | `AGREES` | ⚠ contradicted by DOID |
| GLC3A | `MONDO:0009277` | glaucoma 3A | `AGREES` | ✓ DOID, NCIT |
| GLC3B | `MONDO:0010968` | glaucoma 3, primary infantile, B | `AGREES` | silent (MESH) |
| GLC3C | `MONDO:0013121` | glaucoma 3, primary congenital, C | `AGREES` | — no shared vocabulary |
| GLC3D | `MONDO:0013122` | glaucoma 3, primary congenital, D | `AGREES` | silent (MESH) |
| GLC3E | `MONDO:0014998` | glaucoma 3, primary congenital, E | `AGREES` | — no shared vocabulary |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0020366` ≡ `DOID:11212`

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

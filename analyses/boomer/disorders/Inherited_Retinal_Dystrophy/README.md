# Inherited Retinal Dystrophy

Boomer grounding analysis for [`kb/disorders/Inherited_Retinal_Dystrophy.yaml`](../../../../kb/disorders/Inherited_Retinal_Dystrophy.yaml).

- **Entry term:** [`MONDO:0019118`](http://purl.obolibrary.org/obo/MONDO_0019118) inherited retinal dystrophy
- **Grounded subtypes:** 4
- **Verdicts:** AGREES 4

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| RP | `MONDO:0019200` | retinitis pigmentosa | `AGREES` | ✓ MESH, NCIT, ORDO |
| LCA | `MONDO:0018998` | Leber congenital amaurosis | `AGREES` | ✓ ORDO |
| Cone-Rod Dystrophy | `MONDO:0015993` | cone-rod dystrophy | `AGREES` | ✓ MESH, ORDO |
| Choroideremia | `MONDO:0010557` | choroideremia | `AGREES` | silent (DOID, ICD10CM, MESH, NCIT, ORDO) |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0019118` ≡ `DOID:8501`
- `MONDO:0019118` ≡ `NCIT:C35625`

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

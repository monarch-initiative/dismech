# Thymus Neoplasm

Boomer grounding analysis for [`kb/disorders/Thymus_Neoplasm.yaml`](../../../../kb/disorders/Thymus_Neoplasm.yaml).

- **Entry term:** [`MONDO:0005197`](http://purl.obolibrary.org/obo/MONDO_0005197) thymus neoplasm
- **Grounded subtypes:** 3
- **Verdicts:** AGREES 3

## Subtypes

| Subtype | MONDO term | Label | MONDO | Other sources |
|---|---|---|---|---|
| Thymoma | `MONDO:0006456` | thymoma | `AGREES` | ✓ NCIT, ORDO |
| Thymic carcinoma | `MONDO:0006451` | thymic carcinoma | `AGREES` | ✓ NCIT, ORDO |
| Thymic neuroendocrine tumors | `MONDO:0019964` | thymic neuroendocrine tumor | `AGREES` | ✓ NCIT, ORDO |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `MONDO:0006451` ≡ `DOID:3284`
- `MONDO:0006451` ≡ `NCIT:C7569`

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

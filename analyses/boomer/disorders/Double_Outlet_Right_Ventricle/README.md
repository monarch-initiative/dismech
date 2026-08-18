# Double Outlet Right Ventricle

Boomer grounding analysis for [`kb/disorders/Double_Outlet_Right_Ventricle.yaml`](../../../../kb/disorders/Double_Outlet_Right_Ventricle.yaml).

- **Entry term:** [`MONDO:0018089`](http://purl.obolibrary.org/obo/MONDO_0018089) double outlet right ventricle
- **Grounded subtypes:** 5
- **Verdicts:** AGREES 5

## Subtypes

| Subtype | MONDO term | Label | Verdict |
|---|---|---|---|
| Subaortic VSD | `MONDO:0018498` | double outlet right ventricle with subaortic or doubly committed ventricular septal defect | `AGREES` |
| DORV-Fallot | `MONDO:0020386` | double outlet right ventricle with subaortic or doubly committed ventricular septal defect with pulmonary stenosis | `AGREES` |
| Subpulmonary VSD | `MONDO:0020387` | double outlet right ventricle with subpulmonary ventricular septal defect | `AGREES` |
| Doubly committed VSD | `MONDO:0018498` | double outlet right ventricle with subaortic or doubly committed ventricular septal defect | `AGREES` |
| Non-committed VSD | `MONDO:0020388` | double outlet right ventricle with non-committed subpulmonary ventricular septal defect | `AGREES` |

## What boomer did

Boomer could **not** accept every mapping at once and retracted the following
identity claim(s) to restore consistency:

- `dismech:Double_Outlet_Right_Ventricle#Subaortic VSD` ≡ `MONDO:0018498`

A retraction means these assertions are jointly unsatisfiable, not that the
retracted mapping is necessarily the wrong one. Which assertion to give up is a
curation decision.

## Verdict meanings

- **`AGREES`** - MONDO has this subtype's term as a descendant of the entry's term.

## Files

| File | What |
|---|---|
| [`kb.yaml`](kb.yaml) | Boomer input. Run with `pyboomer solve kb.yaml -t 60`. |
| [`solution.yaml`](solution.yaml) | Boomer output, machine-readable. |
| [`solution.md`](solution.md) | Boomer output, rendered. |

Regenerate with [`../../scripts/build_analyses.py`](../../scripts/build_analyses.py).

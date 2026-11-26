# waldenstrom: ORDO and ICD source additions

The curated disease scope and baseline constraints are held fixed across variants.
Absent or unqualified mappings are recorded explicitly, not promoted to equivalence.

## Source entities

| Entity | Canonical label | Definition |
|---|---|---|
| ICD10CM:C88.0 | Waldenström macroglobulinemia | Not retrieved |
| ORDO:33226 | Waldenström macroglobulinemia | A rare indolent B-cell non-Hodgkin lymphoma, characterized by the infiltration of monoclonal lymphoplasmacytic cells in the bone marrow and the production of serum immunoglobulin&nbsp;M (IgM) monoclonal protein. |

## Results

| Variant | Hypotheses | Normal search | Enumeration | Confidence | Best whole-assignment posterior |
|---|---:|---|---|---:|---:|
| [baseline](baseline/audit.json) | 2 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](baseline/enumeration.json) | 0.9 | 0.855 |
| [ordo](ordo/audit.json) | 3 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](ordo/enumeration.json) | 0.9 | 0.81225 |
| [icd10cm](icd10cm/audit.json) | 3 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](icd10cm/enumeration.json) | 0.9 | 0.81225 |
| [icd11f](icd11f/audit.json) | 2 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](icd11f/enumeration.json) | 0.9 | 0.855 |
| [all](all/audit.json) | 4 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](all/enumeration.json) | 0.9 | 0.7716375 |

Confidence compares the two best distinct complete assignments; it is not a
mapping marginal or a clinical accuracy score. Compare decisions, not the
whole-assignment posteriors of models with different numbers of hypotheses.

## baseline: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.855; B = 0.095.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| Waldenstrom Macroglobulinemia (dismech:Waldenstrom_Macroglobulinemia) ≡ Waldenstrom macroglobulinemia (MONDO:0100280) | 0.9 | accept | reject | 0.9 |

## ordo: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.81225; B = 0.09025.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| Waldenstrom Macroglobulinemia (dismech:Waldenstrom_Macroglobulinemia) ≡ Waldenstrom macroglobulinemia (MONDO:0100280) | 0.9 | accept | reject | 0.9 |

## icd10cm: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.81225; B = 0.09025.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| Waldenstrom Macroglobulinemia (dismech:Waldenstrom_Macroglobulinemia) ≡ Waldenstrom macroglobulinemia (MONDO:0100280) | 0.9 | accept | reject | 0.9 |

## icd11f: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.855; B = 0.095.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| Waldenstrom Macroglobulinemia (dismech:Waldenstrom_Macroglobulinemia) ≡ Waldenstrom macroglobulinemia (MONDO:0100280) | 0.9 | accept | reject | 0.9 |

## all: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.7716375; B = 0.0857375.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| Waldenstrom Macroglobulinemia (dismech:Waldenstrom_Macroglobulinemia) ≡ Waldenstrom macroglobulinemia (MONDO:0100280) | 0.9 | accept | reject | 0.9 |

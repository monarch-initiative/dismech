# gorlin: ORDO and ICD source additions

The curated disease scope and baseline constraints are held fixed across variants.
Absent or unqualified mappings are recorded explicitly, not promoted to equivalence.

## Source entities

| Entity | Canonical label | Definition |
|---|---|---|
| ICD10CM:Q87.8 | Other specified congenital malformation syndromes, not elsewhere classified | Not retrieved |
| ORDO:377 | Gorlin syndrome | A rare hereditary disorder due to autosomal dominant transmission with hamartosis characterized by multiple early-onset basal cell carcinoma (BCC), multiple jaw keratocysts and skeletal abnormalities. |
| icd11f:1012745138 | Gorlin syndrome | Gorlin syndrome, also known as naevoid basal cell carcinoma syndrome (NBCCS), is a hereditary condition characterised by a wide range of developmental abnormalities (odontogenic keratocysts of the jaws, hyperkeratosis of palms and soles, skeletal abnormalities, intracranial ectopic calcifications, and facial dysmorphism) and a predisposition to develop malignant neoplasms (such as multiple basal cell carcinomas or medulloblastoma), and benign neoplasms in the jaw, heart, or ovaries. |

## Results

| Variant | Hypotheses | Normal search | Enumeration | Confidence | Best whole-assignment posterior |
|---|---:|---|---|---:|---:|
| [baseline](baseline/audit.json) | 6 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](baseline/enumeration.json) | 0.95 | 0.844892743403 |
| [ordo](ordo/audit.json) | 7 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](ordo/enumeration.json) | 0.95 | 0.802648106233 |
| [icd10cm](icd10cm/audit.json) | 6 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](icd10cm/enumeration.json) | 0.95 | 0.844892743403 |
| [icd11f](icd11f/audit.json) | 7 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](icd11f/enumeration.json) | 0.95 | 0.802648106233 |
| [all](all/audit.json) | 8 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](all/enumeration.json) | 0.95 | 0.762515700921 |

Confidence compares the two best distinct complete assignments; it is not a
mapping marginal or a clinical accuracy score. Compare decisions, not the
whole-assignment posteriors of models with different numbers of hypotheses.

## baseline: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.844892743403; B = 0.044468039126.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| nevoid basal cell carcinoma syndrome (MONDO:0007187) ≡ nevoid basal cell carcinoma syndrome (DOID:2512) | 0.95 | accept | reject | 0.95 |

## ordo: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.802648106233; B = 0.04224463717.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| nevoid basal cell carcinoma syndrome (MONDO:0007187) ≡ nevoid basal cell carcinoma syndrome (DOID:2512) | 0.95 | accept | reject | 0.95 |

## icd10cm: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.844892743403; B = 0.044468039126.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| nevoid basal cell carcinoma syndrome (MONDO:0007187) ≡ nevoid basal cell carcinoma syndrome (DOID:2512) | 0.95 | accept | reject | 0.95 |

Mappings not imported:

- MONDO:0007187 → ICD10CM:Q87.8: EXCLUDE_UNQUALIFIED

## icd11f: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.802648106233; B = 0.04224463717.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| nevoid basal cell carcinoma syndrome (MONDO:0007187) ≡ nevoid basal cell carcinoma syndrome (DOID:2512) | 0.95 | accept | reject | 0.95 |

## all: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.762515700921; B = 0.040132405312.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| nevoid basal cell carcinoma syndrome (MONDO:0007187) ≡ nevoid basal cell carcinoma syndrome (DOID:2512) | 0.95 | accept | reject | 0.95 |

Mappings not imported:

- MONDO:0007187 → ICD10CM:Q87.8: EXCLUDE_UNQUALIFIED

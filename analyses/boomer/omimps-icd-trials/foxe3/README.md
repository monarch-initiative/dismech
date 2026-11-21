# foxe3: ORDO and ICD source additions

The curated disease scope and baseline constraints are held fixed across variants.
Absent or unqualified mappings are recorded explicitly, not promoted to equivalence.

## Source entities

| Entity | Canonical label | Definition |
|---|---|---|
| ICD10CM:Q12.0 | Congenital cataract | Not retrieved |
| ICD10CM:Q12.3 | Congenital aphakia | Not retrieved |
| ICD10CM:Q13.8 | Other congenital malformations of anterior segment of eye | Not retrieved |
| ORDO:83461 | Congenital primary aphakia | A rare developmental defect during embryogenesis characterised by an absence of the lens. CPAK can be associated with variable secondary ocular defects. |
| ORDO:88632 | Anterior segment developmental anomaly | Not retrieved |
| icd11f:1182282997 | Anterior segment dysgenesis | A condition caused by failure of the anterior structures of the eye to correctly develop during the antenatal period. This condition may present with iris hypoplasia, irregular and misplaced pupils, hazy corneas, or attachments of the iris to the cornea. |
| icd11f:885383581 | Congenital aphakia | Congenital primary aphakia is a developmental eye defect characterised by an absence of the lens, and can be associated with variable secondary ocular defects (including aplasia/dysplasia of the anterior segment of the eye, microphthalmia, and in some cases absence of the iris, retinal dysplasia, or sclerocornea). |
| icd11f:943599144 | Structural developmental anomalies of the anterior segment of eye | Any condition caused by failure of the anterior segment of the eye to correctly develop during the antenatal period. |

## Results

| Variant | Hypotheses | Normal search | Enumeration | Confidence | Best whole-assignment posterior |
|---|---:|---|---|---:|---:|
| [baseline](baseline/audit.json) | 6 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](baseline/enumeration.json) | 0.9 | 0.625026375 |
| [ordo](ordo/audit.json) | 8 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](ordo/enumeration.json) | 0.9 | 0.564086303437 |
| [icd10cm](icd10cm/audit.json) | 7 | ALL_MAPPINGS_CONSISTENT | [VERIFIED](icd10cm/enumeration.json) | 0.9 | 0.59377505625 |
| [icd11f](icd11f/audit.json) | 9 | RETRACTED | [VERIFIED](icd11f/enumeration.json) | 0.5 | 0.289275027404 |
| [all](all/audit.json) | 12 | TIMED_OUT | [EXHAUSTIVELY_ENUMERATED](all/enumeration.json) | 0.5 | 0.24801717662 |
| [repair](repair/audit.json) | 12 | TIMED_OUT | [EXHAUSTIVELY_ENUMERATED](repair/enumeration.json) | 0.9 | 0.482364115159 |

Confidence compares the two best distinct complete assignments; it is not a
mapping marginal or a clinical accuracy score. Compare decisions, not the
whole-assignment posteriors of models with different numbers of hypotheses.

## baseline: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.625026375; B = 0.069447375.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| Primary Aphakia (dismech:FOXE3_Anterior_Segment_Dysgenesis#Primary Aphakia) ≡ congenital primary aphakia (MONDO:0012456) | 0.9 | accept | reject | 0.9 |

## ordo: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.564086303437; B = 0.062676255937.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| Primary Aphakia (dismech:FOXE3_Anterior_Segment_Dysgenesis#Primary Aphakia) ≡ congenital primary aphakia (MONDO:0012456) | 0.9 | accept | reject | 0.9 |

## icd10cm: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.59377505625; B = 0.06597500625.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| Primary Aphakia (dismech:FOXE3_Anterior_Segment_Dysgenesis#Primary Aphakia) ≡ congenital primary aphakia (MONDO:0012456) | 0.9 | accept | reject | 0.9 |

Mappings not imported:

- MONDO:0013067 → ICD10CM:Q12.0: EXCLUDE_UNQUALIFIED
- MONDO:0019503 → ICD10CM:Q13.8: EXCLUDE_UNQUALIFIED

## icd11f: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.289275027404; B = 0.289275027404.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| anterior segment dysgenesis (MONDO:0019503) ≡ Anterior segment dysgenesis (icd11f:1182282997) | 0.95 | accept | reject | 0.487179487179 |
| anterior segment dysgenesis (MONDO:0019503) ≡ Structural developmental anomalies of the anterior segment of eye (icd11f:943599144) | 0.95 | reject | accept | 0.487179487179 |

## all: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.24801717662; B = 0.24801717662.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| anterior segment dysgenesis (MONDO:0019503) ≡ Anterior segment dysgenesis (icd11f:1182282997) | 0.95 | reject | accept | 0.487179487179 |
| anterior segment dysgenesis (MONDO:0019503) ≡ Structural developmental anomalies of the anterior segment of eye (icd11f:943599144) | 0.95 | accept | reject | 0.487179487179 |

Mappings not imported:

- MONDO:0013067 → ICD10CM:Q12.0: EXCLUDE_UNQUALIFIED
- MONDO:0019503 → ICD10CM:Q13.8: EXCLUDE_UNQUALIFIED

## repair: differing choices in the best two assignments

Whole-assignment posteriors: A = 0.482364115159; B = 0.053596012795.

| Hypothesis | Prior | A | B | Marginal |
|---|---:|---|---|---:|
| Primary Aphakia (dismech:FOXE3_Anterior_Segment_Dysgenesis#Primary Aphakia) ≡ congenital primary aphakia (MONDO:0012456) | 0.9 | accept | reject | 0.9 |

Mappings not imported:

- MONDO:0013067 → ICD10CM:Q12.0: EXCLUDE_UNQUALIFIED
- MONDO:0019503 → ICD10CM:Q13.8: EXCLUDE_UNQUALIFIED

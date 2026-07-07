# IEMbase 0001: PAH-related Phenylalanine hydroxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 1 |
| Nosology | 1.4.01.01 |
| Gene | PAH |
| External IDs | OMIM:261600 |
| Generated mapping | MAPPED by `identifier:OMIM:261600` |
| DisMech target | `kb/disorders/Phenylketonuria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

Characteristic clinical features are hypopigmentation, intellectual disability,
microcephaly, musty urine/body odor, and the expected untreated neurologic
presentation. Additional clinical features include anxiety, autism, abnormal
brain MRI, depression, reduced head circumference or height, limb hypertonia,
axial hypotonia, irritability, seizures, skin rash, and vomiting.

The biochemical signature is strong hyperphenylalaninemia in plasma and CSF,
urinary phenylpyruvic acid, normal BH4 loading test, and secondary CSF biogenic
amine changes. IEMbase also lists urine pterins, which appear to be diagnostic
context rather than core PAH-deficiency biomarkers.

Treatments listed by IEMbase include phenylalanine-restricted medical diet,
large neutral amino acids, sapropterin, pegvaliase, fatty acids, and medical
formula/glycomacropeptide.

## DisMech phenotype coverage

DisMech captures the central PKU phenotype well: intellectual disability,
seizures, microcephaly, hypertonia, hypopigmentation, eczema, musty odor,
phenylalaninuria, hyperphenylalaninemia, abnormal cerebral white matter,
developmental delay, atypical behavior, learning disability, growth delay,
ataxia, tremor, anxiety, depression, encephalopathy, lower-limb spasticity, and
visual impairment.

DisMech also models the major biochemical and monitoring dimensions: blood
phenylalanine, treatment-induced phenylalanine reduction, blood tyrosine,
phenylalanine/tyrosine ratio, phenylpyruvic acid, prealbumin, and bone mineral
density. Treatments cover phenylalanine-restricted diet, medical formula,
sapropterin, pegvaliase, and large neutral amino acids.

## Concordance and completeness

Judgement: high concordance. The generated mapping is correct, and DisMech is
at least as complete as IEMbase for core clinical phenotype coverage.

Main IEMbase-only details worth considering are vomiting, irritability, axial
hypotonia, and the explicit normal BH4 loading test. IEMbase also names fatty
acid supplementation, but this needs independent clinical justification before
becoming a DisMech treatment.

## Curation actions

- No mapping correction needed.
- Consider adding vomiting, irritability, and axial hypotonia only if supported
  by accepted phenotype evidence.
- Consider whether normal BH4 loading belongs under diagnosis for distinguishing
  PAH deficiency from BH4 defects.

# IEMbase 0057: MCCC1-related 3-methylcrotonyl-CoA carboxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 57 |
| Nosology | 1.2.1.01 |
| Gene | MCCC1 |
| External IDs | OMIM:210200 |
| Generated mapping | CANDIDATE by `fuzzy_alias_gene` |
| Candidate DisMech targets | `3-Methylcrotonyl-CoA_Carboxylase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive MCCC1-related
3-methylcrotonyl-CoA carboxylase 1 deficiency, also called
3-methylcrotonylglycinuria type 1 or MCC A. Treatability is marked yes and the
listed prevalence range is 1:50,000-1:30,000 in Europe.

The biochemical signal includes high urinary 3-methylcrotonylglycine, high or
normal-high 3-methylcrotonylcarnitine, high C5-OH acylcarnitine in dried blood
spot or plasma, normal-high esterified carnitine, low-normal free carnitine,
low fibroblast MCCC activity, increased urinary 3-hydroxyisovaleric acid, and
possible hyperammonemia, glucose depression, positive anion gap, or base-excess
abnormality.

IEMbase does not list a characteristic clinical feature set, but the additional
clinical section includes cardiomyopathy, cerebral atrophy, infection-triggered
acute encephalopathy, failure to thrive, highly variable expressivity including
asymptomatic individuals, hypo- or hypertonia, hypoglycemia, ketoacidosis,
metabolic acidosis, metabolic stroke, muscle pain or weakness, neutropenia,
acrid urine odor, psychomotor delay, thrombocytopenia, and white-matter MRI
changes. Treatments are avoidance of fasting and L-carnitine supplements.

## DisMech phenotype coverage

The candidate mapping is correct. DisMech models 3-methylcrotonyl-CoA
carboxylase deficiency as a leucine-catabolism disorder caused by MCCC1 or
MCCC2 molecular-function deficiency, with accumulation of
3-hydroxyisovaleric acid, 3-methylcrotonylglycine, and C5-OH acylcarnitine.

DisMech covers MCCC1 and MCCC2 genetic causes, newborn-screening biomarker
coverage, secondary carnitine deficiency, low penetrance and asymptomatic
newborn-screening cases, stress-triggered metabolic decompensation, hypoglycemia,
metabolic acidosis, ketoacidosis, hyperammonemia, coma, hypotonia, failure to
thrive, developmental regression, movement abnormality, and selected vascular or
respiratory complications. Treatments include moderate dietetic modification,
carnitine supplementation, and biotin supplementation.

## Concordance and completeness

Judgement: generated `CANDIDATE` should be accepted as the manual mapping to
`3-Methylcrotonyl-CoA_Carboxylase_Deficiency.yaml`.

The main nuance is granularity: IEMbase is specifically MCCC1/MCC A, while the
DisMech file intentionally covers the combined MCCC1/MCCC2 disorder. That is
consistent with the project scope unless future subtype anchors are introduced.
IEMbase adds some additional candidate phenotype rows, including cardiomyopathy,
metabolic stroke, neutropenia, thrombocytopenia, and white-matter MRI changes,
but DisMech is broader for mechanism, penetrance, and management.

## Curation actions

- Promote this candidate to a correct file-level mapping.
- Keep MCCC1-specific identity as a gene-level note rather than creating a
  standalone disease file.
- Consider whether the local entry should add an explicit MCCC1/MCC A subtype
  anchor if downstream crosswalks require gene-specific subtype resolution.

# IEMbase 0059: TAZ-related Barth syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 59 |
| Nosology | 19.1.03.01 |
| Gene | TAZ |
| External IDs | OMIM:302060 |
| Generated mapping | MAPPED by `alias_exact:barth syndrome` |
| Candidate DisMech targets | `Barth_Syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as X-linked TAZ-related Barth syndrome, with alternate
label MGA2. Treatability is marked unknown and the listed prevalence is
1:454,000.

The biochemical signal includes low-normal free carnitine, normal-high creatine
kinase, normal-high 2-ethylhydracrylic acid, increased urinary
3-methylglutaconic acid, increased urinary 3-methylglutaric acid, variable
ammonia, cholesterol, glucose, lactate, and uric-acid findings, an abnormal
cardiolipin profile, and low cardiolipin in general and in fibroblasts.

The characteristic clinical signal includes cardiomyopathy, growth retardation,
myopathy, and neutropenia. Additional features include arrhythmia, dilated
cardiomyopathy, cherubic face, chronic aphthous ulceration, clot or stroke
risk, exercise intolerance, feeding difficulty, heart failure, hypoglycemia,
axial hypotonia, left ventricular noncompaction, metabolic acidosis, mild
dysmorphic features, occasional cerebral atrophy, respiratory distress, sepsis,
and vomiting. No treatment rows are present in the cached IEMbase record.

## DisMech phenotype coverage

The generated mapping to `Barth_Syndrome.yaml` is correct. DisMech models Barth
syndrome as an ultra-rare X-linked mitochondrial disorder caused by TAZ/TAFAZZIN
variants that disrupt cardiolipin remodeling, increase monolysocardiolipin,
decrease mature cardiolipin, and impair mitochondrial membrane structure,
oxidative phosphorylation, and metabolic flexibility.

DisMech covers cardiomyopathy, dilated cardiomyopathy, left ventricular
noncompaction, arrhythmia vulnerability, skeletal myopathy, exercise
intolerance, growth delay, recurrent bacterial infections, neutropenia through
impaired myeloid maturation, lactic acidosis, and 3-methylglutaconic aciduria.
It is substantially richer for cardiolipin remodeling and mitochondrial
mechanism.

## Concordance and completeness

Judgement: correct mapping and high concordance.

IEMbase adds several granular phenotype or lab reminders that are not all
central in the DisMech summary: urinary 3-methylglutaric acid, free carnitine,
cholesterol/glucose/uric-acid fields, cherubic face, aphthous ulcers,
clot/stroke, respiratory distress, and sepsis. DisMech is much stronger for
tafazzin/cardiolipin mechanism, MLCL/cardiolipin interpretation, cardiac and
skeletal muscle pathophysiology, and neutropenia biology.

## Curation actions

- Keep the generated mapping to `Barth_Syndrome.yaml`.
- Do not use generic 3-methylglutaconic aciduria alone to map other MGA records
  to Barth syndrome.
- Consider IEMbase-only facial, oral-ulcer, sepsis, and clot/stroke rows as
  possible future phenotype-enrichment checks.

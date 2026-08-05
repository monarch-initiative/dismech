# IEMbase 0286: HEXA-related Beta-hexosaminidase subunit alpha deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 286 |
| Nosology | 20.1.05.01 |
| Gene | HEXA |
| External IDs | OMIM:272800; ORPHA:309192 |
| Generated mapping | MAPPED; `Tay-Sachs_Disease.yaml` |
| Candidate DisMech targets | `Tay-Sachs_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents Tay-Sachs disease / GM2 gangliosidosis B variant due to HEXA
alpha-subunit deficiency. Inheritance is autosomal recessive, treatability is
unknown, and prevalence is listed as 1:320,000 overall and 1:3,900 in Jewish
populations.

The clinical rows span the Tay-Sachs age spectrum: ataxia, psychotic behavior,
dystonia, hepatosplenomegaly, macrocephaly, psychiatric disturbance,
spasticity, and urinary incontinence. Biochemical rows list decreased
beta-hexosaminidase A, normal-to-increased beta-hexosaminidase A+B activity,
increased urinary oligosaccharides, and increased serum LysoGM2.

## DisMech phenotype coverage

`Tay-Sachs_Disease.yaml` is the correct local target. The entry models HEXA
pathogenic variants, beta-hexosaminidase A deficiency, residual enzyme activity
in late-onset disease, GM2 ganglioside accumulation, neuronal lysosomal storage,
and infantile, juvenile, and late-onset subtypes.

Local phenotypes include developmental regression, cherry-red spot,
exaggerated startle response, hypotonia, seizures, macrocephaly, blindness,
visual impairment, ataxia, muscle weakness, skeletal muscle atrophy, proximal
muscle weakness, psychosis, progressive spasticity, dysarthria, dysphagia, GM2
ganglioside accumulation, hypomyelination, cerebellar atrophy, and tremor.
Local biochemical coverage includes hexosaminidase A activity and GM2
ganglioside. Treatments include supportive care, genetic counseling, HSCT
context, substrate reduction therapy, pharmacological chaperone therapy, and
investigational gene therapy.

## Concordance and completeness

Judgement: correct mapping with high phenotype concordance.

IEMbase and DisMech agree on HEXA/Tay-Sachs identity, autosomal recessive
inheritance, reduced hexosaminidase A, preserved total A+B activity, GM2
storage logic, ataxia, dystonia/extrapyramidal disease, macrocephaly,
psychiatric or psychotic late-onset manifestations, and spasticity. DisMech is
broader for subtype structure, neuro-ophthalmic findings, treatment landscape,
and mechanism.

IEMbase adds review prompts for urinary incontinence, urinary oligosaccharides,
LysoGM2, and hepatosplenomegaly. The hepatosplenomegaly row should be treated
cautiously before import, because visceral involvement is more typical of
Sandhoff disease and other lysosomal disorders than classic Tay-Sachs.

## Curation actions

- Keep this record mapped to `Tay-Sachs_Disease.yaml`.
- Use IEMbase's LysoGM2 and urinary oligosaccharide rows as biomarker review
  prompts.
- Review hepatosplenomegaly and urinary incontinence against Tay-Sachs-specific
  sources before adding them locally.

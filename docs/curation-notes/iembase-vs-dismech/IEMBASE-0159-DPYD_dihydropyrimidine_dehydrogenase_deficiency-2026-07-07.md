# IEMbase 0159: DPYD-related dihydropyrimidine dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 159 |
| Nosology | 16.1.01.01 |
| Gene | DPYD |
| External IDs | OMIM:274270; OMIM:612779; ORPHA:1675 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | None |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as DPYD-related dihydropyrimidine dehydrogenase
deficiency, with alternate labels thymine-uraciluria and DPD. Treatability is
marked unknown.

The biochemical rows show decreased WBC dihydropyrimidine dehydrogenase and
increased 5-OH-methyluracil, plasma and urinary thymine, and plasma and
urinary uracil. The clinical rows are variable and include cerebral atrophy,
cerebellar white-matter MRI abnormalities, epilepsy/seizures, abnormal eye
movements, nystagmus, optic atrophy, coloboma, microcephaly, feeding
difficulties, hypotonia, hypertonia, hyperactivity, psychomotor retardation,
intellectual disability, autism, and severe 5-fluorouracil toxicity in affected
individuals and heterozygotes.

## DisMech phenotype coverage

There is no local standalone DPYD/dihydropyrimidine dehydrogenase deficiency
entry.

`Chemotherapy_Induced_Diarrhea.yaml` contains DPYD pharmacogenomic
susceptibility to fluoropyrimidine toxicity and DPYD-guided dosing context.
That is clinically relevant to the IEMbase 5-fluorouracil toxicity rows, but
it is not the inherited DPYD deficiency disease target and does not model the
thymine/uracil biochemical phenotype or neurodevelopmental presentation.

## Concordance and completeness

Judgement: true local gap with pharmacogenetic overlap.

DisMech currently covers DPYD as a modifier of fluoropyrimidine toxicity, not
as a monogenic inborn error of pyrimidine catabolism. The IEMbase disease has a
distinct biochemical signature, clinical neurodevelopmental spectrum, and
toxicity-risk implication that should not be collapsed into chemotherapy-induced
diarrhea.

## Curation actions

- Leave IEMbase 159 unmapped for now.
- Future curation should decide whether DPYD deficiency is represented as a
  metabolic disease entry, a pharmacogenetic/toxicity entry, or both with clear
  scope boundaries.
- If curated, include WBC DPD activity, thymine/uracil accumulation,
  neurodevelopmental features, and severe fluoropyrimidine toxicity risk.

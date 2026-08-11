# IEMbase 0698: NDUFA10-related NADH dehydrogenase alpha subcomplex subunit 10 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 698 |
| Nosology | 7.1.13.01 |
| Nosology code | IEM0425 |
| Gene | NDUFA10 |
| External IDs | OMIM:618243; ORPHA:255241 |
| Generated mapping | CANDIDATE to `COX16-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFA10 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFA10-related NADH dehydrogenase alpha
subcomplex subunit 10 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 22.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate in neonatal and infantile windows. Clinical rows include lactic
acidosis, psychomotor retardation, basal ganglia MRI abnormalities,
hypertrophic cardiomyopathy, hypotonia, and Leigh syndrome.

## DisMech phenotype coverage

No exact NDUFA10 or MC1DN22 local target was identified.

`Leigh_Syndrome.yaml` covers the shared complex I/Leigh phenotype space,
including lactate elevation, basal ganglia lesions, hypotonia, and
cardiomyopathy-associated Leigh presentations, but it lacks an NDUFA10-specific
gene or disease model.

The generated `COX16-Related_COX_Deficiency.yaml` candidate is a complex IV
assembly-factor disorder. It shares the nuclear-type number 22 but not the gene,
respiratory-chain complex, or disease mechanism.

## Concordance and completeness

Judgement: true local gap with broad Leigh overlap only.

The IEMbase row is a gene-specific complex I disease with neonatal/infantile
lactate and enzyme findings plus cardiomyopathy and basal-ganglia Leigh
features. `COX16-Related_COX_Deficiency.yaml` is a wrong-complex
number-collision candidate.

## Curation actions

- Add a dedicated NDUFA10/MC1DN22 target if curated.
- Reject COX16-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  lactic acidosis, psychomotor retardation, basal ganglia MRI abnormalities,
  hypertrophic cardiomyopathy, hypotonia, and Leigh syndrome.

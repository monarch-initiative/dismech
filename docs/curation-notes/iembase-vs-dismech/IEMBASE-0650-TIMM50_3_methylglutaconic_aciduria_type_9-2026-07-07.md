# IEMbase 0650: TIMM50-related 3-methylglutaconic aciduria type 9

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 650 |
| Nosology | 11.2.04.01 |
| Gene | TIMM50 |
| External IDs | OMIM:607381; ORPHA:505216 |
| Generated mapping | UNMAPPED; weak candidate `Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | False exact candidate; possible future 3-methylglutaconic aciduria grouping |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents TIMM50-related 3-methylglutaconic aciduria type 9 as an
autosomal recessive disorder also described as intellectual disability and
seizure disorder due to TIMM50 variant.

Biochemical rows include increased urinary 3-methylglutaconic acid, increased
urinary 3-methylglutaric acid, normal urinary 3-hydroxyisovaleric acid,
increased plasma lactate, and normal-to-increased CSF lactate. Clinical rows
include developmental delay, epilepsy, failure to thrive, hypotonia,
hypsarrhythmia on EEG, optic atrophy, optional aggressive behavior, optional
white-matter atrophy, and optional bilateral symmetric lesions in the globus
pallidus and brainstem.

## DisMech phenotype coverage

`Glutaryl-CoA_Dehydrogenase_Deficiency.yaml` is a lexical/metabolic false
candidate. It models GCDH-related glutaric aciduria type 1, with lysine /
hydroxylysine / tryptophan catabolism, glutaric acid, 3-hydroxyglutaric acid,
glutarylcarnitine, and striatal injury. It does not model TIMM50, mitochondrial
protein import, 3-methylglutaconic aciduria type 9, hypsarrhythmia, optic
atrophy, or lactate/3-methylglutaconic acid readouts.

Local entries such as Barth syndrome and Sengers syndrome include
3-methylglutaconic aciduria in other gene-specific contexts, but there is no
local TIMM50 disease anchor and no general grouping that would make this row
covered.

## Concordance and completeness

Judgement: true local TIMM50 / 3-methylglutaconic aciduria type 9 gap.

The generated candidate should be rejected as exact because the biochemical
label overlap is not the same disorder or mechanism. IEMbase supplies a
distinct mitochondrial/neurodevelopmental phenotype package that is not
captured by existing DisMech entries.

## Curation actions

- Do not map to glutaryl-CoA dehydrogenase deficiency.
- Curate TIMM50-related 3-methylglutaconic aciduria type 9 separately if
  selected.
- Consider a future grouping for gene-specific 3-methylglutaconic aciduria
  disorders.
- Preserve 3-methylglutaconic and 3-methylglutaric acid, lactate, epilepsy,
  hypsarrhythmia, developmental delay, hypotonia, failure to thrive, optic
  atrophy, white-matter/basal-ganglia/brainstem imaging, and behavior prompts.

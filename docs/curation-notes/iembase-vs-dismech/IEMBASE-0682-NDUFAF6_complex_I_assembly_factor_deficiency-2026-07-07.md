# IEMbase 0682: NDUFAF6-related complex I assembly factor 6 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 682 |
| Nosology | 7.1.06.01 |
| Nosology code | IEM0442 |
| Gene | NDUFAF6 |
| External IDs | OMIM:618239; ORPHA:255241 |
| Generated mapping | UNMAPPED; best candidate `Fanconi_Renotubular_Syndrome.yaml` |
| Candidate DisMech targets | Partial gene-level coverage in `Fanconi_Renotubular_Syndrome.yaml#FRTS5`; exact MC1DN17/Leigh phenotype gap |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFAF6-related complex I assembly factor
6 deficiency, also labeled mitochondrial complex I deficiency, nuclear type 17.

Biochemical rows include decreased fibroblast complex I activity and increased
plasma lactate from neonatal through adolescent ages. Clinical rows include
basal ganglia MRI abnormalities, bilateral striatal necrosis, epilepsy, Leigh
syndrome, psychomotor retardation, and characteristic ataxia, dystonia, and
lactic acidosis.

## DisMech phenotype coverage

`Fanconi_Renotubular_Syndrome.yaml` contains real NDUFAF6 coverage under FRTS5,
the Acadian variant of Fanconi syndrome. That local subtype describes a
homozygous non-coding NDUFAF6 splicing variant causing loss of the
mitochondria-localized isoform, respiratory-chain complex I deficiency,
generalized proximal tubular dysfunction from birth, progressive chronic kidney
disease, and pulmonary interstitial fibrosis.

This is not complete coverage for the IEMbase row. IEMbase is focused on
MC1DN17/Leigh-like complex I disease with basal ganglia lesions, bilateral
striatal necrosis, epilepsy, psychomotor retardation, ataxia, dystonia, and
lactic acidosis. The cached IEMbase rows do not describe the Fanconi
proximal-tubulopathy phenotype.

`Leigh_Syndrome.yaml` provides broad neurologic and complex I context, but not
NDUFAF6 disease-level completeness.

## Concordance and completeness

Judgement: partial gene-level/pathway coverage only. Do not treat the FRTS5
Fanconi subtype as complete coverage for this IEMbase complex I deficiency row.

The local KB correctly knows that NDUFAF6 can cause complex I deficiency, but
the represented phenotype is a specific proximal tubulopathy/fibrosis subtype,
whereas IEMbase emphasizes Leigh/striatal-necrosis neurologic disease.

## Curation actions

- Keep `Fanconi_Renotubular_Syndrome.yaml#FRTS5` as real but partial NDUFAF6
  context.
- Add or extend NDUFAF6/MC1DN17 coverage if DisMech wants the IEMbase row fully
  represented.
- Preserve bilateral striatal necrosis, basal ganglia MRI abnormalities,
  epilepsy, psychomotor retardation, ataxia, dystonia, lactic acidosis, elevated
  lactate, and decreased complex I activity.
- Do not infer Fanconi syndrome features from this IEMbase row without source
  review.

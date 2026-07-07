# IEMbase 0420: POLG-related spinocerebellar ataxia with epilepsy, included

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 420 |
| Nosology | 9.2.01.02 |
| Gene | POLG |
| External IDs | OMIM:607459; ORPHA:402082; ORPHA:70595; ORPHA:254881 |
| Generated mapping | MAPPED; `Sensory_Ataxic_Neuropathy_Dysarthria_Ophthalmoparesis.yaml` |
| Candidate DisMech targets | `Sensory_Ataxic_Neuropathy_Dysarthria_Ophthalmoparesis.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents a POLG ataxia-neuropathy spectrum record with alternate name
sensory ataxic neuropathy, dysarthria, and ophthalmoparesis (SANDO). It records
autosomal dominant inheritance in the source row. Clinical rows include adult
axonal sensory ataxic neuropathy, dysarthria, ophthalmoparesis/ophthalmoplegia,
muscle mtDNA depletion, epileptic seizures, cognitive impairment, headache, and
migraine. There are no treatment rows.

## DisMech phenotype coverage

The generated mapping is correct. Local
`Sensory_Ataxic_Neuropathy_Dysarthria_Ophthalmoparesis.yaml` directly models
SANDO as a POLG-related mitochondrial DNA maintenance disorder with mtDNA
depletion and multiple deletions, respiratory-chain deficiency in post-mitotic
tissues, sensory ataxic neuropathy, dysarthria, ophthalmoparesis/progressive
external ophthalmoplegia, myopathy, ragged-red/COX-negative muscle pathology,
and seizure risk within the broader POLG spectrum.

Local DisMech is stronger for mechanism and for management cautions, including
avoidance of valproate in POLG-related disorders. IEMbase adds migraine,
headache, cognitive impairment, and explicit muscle mtDNA depletion prompts.

## Concordance and completeness

Judgement: correct high-concordance mapping to
`Sensory_Ataxic_Neuropathy_Dysarthria_Ophthalmoparesis.yaml`.

The disease name, SANDO synonym, POLG gene, mtDNA-maintenance mechanism, sensory
ataxic neuropathy, dysarthria, ophthalmoparesis/ophthalmoplegia, and epilepsy
context align well.

## Curation actions

- Retain the mapping to
  `Sensory_Ataxic_Neuropathy_Dysarthria_Ophthalmoparesis.yaml`.
- Consider reviewing the inheritance row because local DisMech models SANDO as
  typically autosomal recessive, while IEMbase lists autosomal dominant.
- Consider adding IEMbase's headache, migraine, cognitive impairment, and muscle
  mtDNA-depletion prompts after source verification.

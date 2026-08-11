# IEMbase 0471: MT-RNR1-related mitochondrial ribosomal RNA 12S deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 471 |
| Nosology | 6.2.07.01 |
| Gene | MT-RNR1 |
| External IDs | OMIM:580000; ORPHA:90641 |
| Generated mapping | UNMAPPED; low candidate `Mitochondrial_Trifunctional_Protein_Deficiency.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents MT-RNR1-related mitochondrial ribosomal RNA 12S deficiency,
with alternate labels streptomycin ototoxicity and aminoglycoside-induced
deafness. It records mitochondrial inheritance. The cached phenotype signal is
sparse and consists of characteristic deafness across age ranges. There are no
biochemical or treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for MT-RNR1-related aminoglycoside-induced
deafness. Local modules and disease entries mention aminoglycoside ototoxicity
as a general hair-cell injury or medication-safety context, and mitochondrial
disease entries may warn against aminoglycosides, but those contexts do not
model MT-RNR1 12S rRNA susceptibility as a disease entity.

The generated `Mitochondrial_Trifunctional_Protein_Deficiency.yaml` candidate is
a false positive. Local MTP deficiency is a HADHA/HADHB long-chain fatty-acid
oxidation disorder with long-chain hydroxyacylcarnitines, hypoglycemia,
cardiomyopathy, rhabdomyolysis, neuropathy, and liver disease. It is not a
mitochondrial 12S rRNA aminoglycoside-susceptibility disorder.

## Concordance and completeness

Judgement: true MT-RNR1 aminoglycoside-induced deafness local gap; reject
mitochondrial trifunctional protein deficiency as an exact mapping.

The candidate shares mitochondrial wording only. The gene, inheritance,
triggered ototoxicity mechanism, and phenotype focus differ.

## Curation actions

- Keep this record unmapped until an MT-RNR1 mitochondrial 12S rRNA
  aminoglycoside-induced deafness target exists.
- Do not map to `Mitochondrial_Trifunctional_Protein_Deficiency.yaml`.
- Use generic aminoglycoside ototoxicity and sensorineural-hair-cell-loss
  modules only as context if a future MT-RNR1 entry is created.
- If curated, include MT-RNR1, mitochondrial inheritance, aminoglycoside or
  streptomycin-triggered ototoxicity, and sensorineural deafness.

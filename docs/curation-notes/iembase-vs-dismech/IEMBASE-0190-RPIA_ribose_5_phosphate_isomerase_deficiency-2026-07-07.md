# IEMbase 0190: RPIA-related ribose-5-phosphate isomerase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 190 |
| Nosology | 3.5.02.01 |
| Gene | RPIA |
| External IDs | OMIM:608611; ORPHA:440706 |
| Generated mapping | UNMAPPED; best candidate `Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency.yaml` |
| Candidate DisMech targets | None valid; generated G6PD candidate is false |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as RPIA-related ribose-5-phosphate isomerase
deficiency, with RPIA as the alternate label. Treatability is marked unknown.

The biochemical rows emphasize markedly increased arabitol and ribitol in CSF,
plasma, and urine, increased urinary xylulose, and increased polyols by magnetic
resonance spectroscopy from childhood through adulthood. Characteristic clinical
rows include abnormal brain MRI, nonprogressive cerebellar ataxia, epilepsy,
leukoencephalopathy, neuropathy, optic atrophy, psychomotor retardation, and
spasticity. Additional clinical rows include behavioral disorder, coarse facial
features, deeply set eyes, dolichocephaly, dysmorphism, flat nasal bridge,
hearing loss, high-arched palate, hyperpigmentation, hypotonia, large ears,
micrognathia, nystagmus, psychomotor regression, retinitis pigmentosa, tented
upper lip, and visual impairment. No treatment rows are listed.

## DisMech phenotype coverage

No valid local RPIA disease target was found. The generated best candidate,
`Glucose-6-Phosphate_Dehydrogenase_G6PD_Deficiency.yaml`, is a pentose phosphate
pathway neighbor but models an erythrocyte oxidative-phase G6PD disorder, not
RPIA-related nonoxidative pentose phosphate metabolism disease.
`Transaldolase_Deficiency.yaml` is also pathway-adjacent but TALDO1-specific and
should not absorb this record.

## Concordance and completeness

Judgement: true local disease gap; generated G6PD candidate is false.

IEMbase provides a distinct RPIA profile centered on polyol accumulation across
CSF/plasma/urine, leukoencephalopathy, seizures, neuropathy, optic atrophy,
spasticity, and neurodevelopmental impairment. Current DisMech coverage of
other pentose phosphate pathway disorders does not capture the RPIA entity.

## Curation actions

- Do not map this record to G6PD deficiency or transaldolase deficiency.
- Add a future RPIA/ribose-5-phosphate isomerase deficiency entry if this
  disease is in scope.
- Seed that entry with arabitol/ribitol/xylulose polyol markers,
  leukoencephalopathy, epilepsy, neuropathy, optic atrophy, ataxia, spasticity,
  and dysmorphic/neurodevelopmental features.

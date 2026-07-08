# IEMbase 0741: MT-ATP6-related mitochondrial ATP synthase subunit 6 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 741 |
| Nosology | 6.1.04.01 |
| Nosology code | IEM0484 |
| Gene | MT-ATP6 |
| External IDs | OMIM:516060; ORPHA:397750 |
| Generated mapping | UNMAPPED; weak candidate `Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml` |
| Candidate DisMech targets | `NARP_syndrome.yaml` is the strongest MT-ATP6/NARP-spectrum target; `Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml` is partial MLASA3 context |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents mitochondrial MT-ATP6-related ATP synthase F0 subunit 6
deficiency, with alternate name neuropathy, ataxia, and retinitis pigmentosa.
The cached rows are broad across the NARP/MILS/complex V spectrum: elevated CSF
lactate in infancy/childhood, plasma lactate from neonatal life onward,
infantile sideroblastic anemia, blindness, burst-suppression EEG,
hypertrophic cardiomyopathy, cerebellar atrophy, cognitive decline,
developmental delay, dystonia, failure to thrive, feeding difficulty,
sensorineural hearing loss, hyperreflexia, hypotonia, Leigh-like MRI lesions,
regression, night blindness, nystagmus, ophthalmoplegia, optic atrophy,
perinatal death, ptosis, spasticity, stroke-like episodes, ataxia, epilepsy,
muscle weakness, peripheral neuropathy, and retinitis pigmentosa.

## DisMech phenotype coverage

`NARP_syndrome.yaml` is the correct local MT-ATP6/NARP-spectrum target even
though the generated mapper missed it. It models maternally inherited MT-ATP6
ATP synthase dysfunction, impaired complex V assembly/ATP production, NARP and
MILS overlap, and core neuroretinal phenotypes including neuropathy, ataxia,
retinitis pigmentosa, hearing impairment, and related biochemical readouts.

The generated `Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml`
candidate is partial context only. It contains an MLASA3 subtype and MT-ATP6
complex V respiratory defect, which explains the IEMbase sideroblastic anemia
prompt, but it does not represent the primary NARP-spectrum disease identity.

## Concordance and completeness

Judgement: false negative for `NARP_syndrome.yaml`, with MLASA as secondary
context.

DisMech covers the central MT-ATP6/NARP mechanism and many characteristic
neuroretinal features. IEMbase is broader for age-banded severity and adds or
emphasizes sideroblastic anemia, burst-suppression EEG, hypertrophic
cardiomyopathy, Leigh-like lesions, perinatal death, stroke-like episodes,
ptosis, night blindness, spasticity, and detailed lactate bands.

## Curation actions

- Treat `NARP_syndrome.yaml` as the primary local target for this IEMbase
  record.
- Keep `Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml` as MLASA3
  context, not as the primary mapping.
- Preserve IEMbase prompts for sideroblastic anemia, cardiomyopathy, EEG,
  Leigh/MILS overlap, regression, stroke-like episodes, ocular/retinal features,
  and age-banded lactate.

# IEMbase 0282: DNM1L-related Dynamin-like protein 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 282 |
| Nosology | 19.2.01.01 |
| Gene | DNM1L |
| External IDs | OMIM:614388; ORPHA:98673 |
| Generated mapping | UNMAPPED; weak candidate `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | None valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents DNM1L-related defective mitochondrial and peroxisomal fission
encephalopathy. The alternate label in the cache is "Encephalopahty, lethal,
due to defective mitochondrial peroxisomal fission" with the spelling preserved
from IEMbase. Inheritance is listed as autosomal dominant and autosomal
recessive. Treatability is unknown.

The phenotype signal is a severe early neurologic disorder: neonatal abnormal
gyral pattern, delayed myelination, hypotonia, microcephaly, muscle weakness,
areflexia, optic atrophy, failure to thrive, later cerebral atrophy, oculomotor
apraxia, psychomotor delay, pyramidal signs, neurologic regression, and
seizures. The biochemical rows list increased plasma lactate and increased
plasma very-long-chain fatty acids.

## DisMech phenotype coverage

There is no local DisMech disease entry for DNM1L-related mitochondrial and
peroxisomal fission defect. Repository search finds DNM1L mentioned only as
context in unrelated entries such as obesity, while other dynamin-family or
mitochondrial-dynamics entries involve different genes and disease entities.

The generated weak candidate, `Pyruvate_Dehydrogenase_Deficiency.yaml`, is not
a valid target. PDH deficiency can share lactic acidosis and neurologic
features, but it does not model the DNM1L/DRP1 fission mechanism, the combined
mitochondrial-peroxisomal dynamics defect, or the associated VLCFA abnormality.

## Concordance and completeness

Judgement: true local gap; do not map to the weak PDH candidate.

IEMbase provides a compact but coherent DNM1L phenotype profile centered on
early encephalopathy, abnormal brain development/myelination, optic atrophy,
regression, seizures, hypotonia, lactate elevation, and VLCFA elevation.
DisMech currently lacks a corresponding disease-level entry, and the existing
mitochondrial/peroxisomal entries do not cover this fission-dynamics disorder.

This is a useful future curation target because it crosses organelle
biogenesis/dynamics and peroxisomal metabolic readouts. Any future entry should
distinguish DNM1L from MFF and other mitochondrial fission genes, and should
separate primary fission biology from secondary lactic acidosis or peroxisomal
fatty-acid abnormalities.

## Curation actions

- Leave this record unmapped for now.
- Reject `Pyruvate_Dehydrogenase_Deficiency.yaml` as a false-positive metabolic
  encephalopathy candidate.
- Consider a future standalone DNM1L entry or a mitochondrial/peroxisomal
  dynamics grouping that can also accommodate later MFF-related records.

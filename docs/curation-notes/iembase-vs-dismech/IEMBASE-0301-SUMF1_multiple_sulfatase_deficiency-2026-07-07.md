# IEMbase 0301: SUMF1-related Formyl-glycine generating enzyme deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 301 |
| Nosology | 20.1.12.01 |
| Gene | SUMF1 |
| External IDs | OMIM:272200; ORPHA:585 |
| Generated mapping | AMBIGUOUS; `Multiple_Sulfatase_Deficiency.yaml` and subtypes |
| Candidate DisMech targets | `Multiple_Sulfatase_Deficiency.yaml#Neonatal`; `#Infantile`; `#Juvenile`; file-level `Multiple_Sulfatase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents multiple sulfatase deficiency / mucosulfatidosis due to
SUMF1 formylglycine-generating enzyme deficiency. Inheritance is autosomal
recessive and treatability is unknown.

Clinical rows include coarse facial features, gait disturbance, CNS
hypomyelination, intellectual disability, leukodystrophy, slow nerve conduction
velocity, cardiopulmonary failure, cortical atrophy, dysostosis multiplex,
gingival hyperplasia, growth retardation, hepatosplenomegaly, hydrocephalus,
axial hypotonia, ichthyosis, neurologic deterioration, ophthalmologic anomalies,
psychomotor retardation, seizures, spasticity, and speech disturbance. The
cached record does not include biochemical rows, despite the disease being
defined by multiple sulfatase activity loss.

## DisMech phenotype coverage

`Multiple_Sulfatase_Deficiency.yaml` is the correct local target. The generated
ambiguity arises because the file has Neonatal, Infantile, and Juvenile
subtypes in addition to the disease-level match; this is not a true mapping
conflict.

The local entry models SUMF1/FGE deficiency, impaired post-translational
sulfatase activation, reduced multiple sulfatase activities, glycosaminoglycan
and sulfatide storage, neuroglial lysosomal dysfunction, neurodegeneration,
retinal/auditory degeneration, and skeletal/joint manifestations. Local
phenotype coverage is broad and includes hydrocephalus, leukodystrophy,
microcephaly, macrocephaly, coarse facial features, sensorineural hearing
impairment, visual impairment, cataract, optic atrophy, intellectual
disability, seizure, global developmental delay, neonatal hypotonia, joint
stiffness, hepatosplenomegaly, developmental regression, abnormal peripheral
nerve conduction, short stature, rapid neurologic deterioration, retinal
pigmentary abnormality, corneal opacity, ichthyosis, mucopolysacchariduria,
broad hallux, and broad thumb.

## Concordance and completeness

Judgement: correct mapping to file-level `Multiple_Sulfatase_Deficiency.yaml`;
the generated subtype ambiguity is expected.

IEMbase and DisMech agree on SUMF1 identity, recessive inheritance, MSD scope,
leukodystrophy/hypomyelination, peripheral nerve conduction abnormality,
developmental and neurologic deterioration, seizures, spasticity/hypotonia,
coarse facial features, hepatosplenomegaly, ichthyosis, hydrocephalus,
ophthalmologic involvement, dysostosis, growth impairment, and
cardiopulmonary disease. DisMech is stronger for biochemical mechanism,
subtype structure, sulfatase activation biology, storage substrates, ocular and
auditory detail, and experimental treatment context.

IEMbase adds concrete rows for cortical atrophy, cardiopulmonary failure,
gingival hyperplasia, speech disturbance, and gait disturbance. Conversely,
IEMbase lacks the local biochemical rows for reduced multiple sulfatase
activities and GAG/sulfatide accumulation.

## Curation actions

- Resolve the generated ambiguity to file-level `Multiple_Sulfatase_Deficiency.yaml`.
- Use subtype rows only when a source phenotype is explicitly neonatal,
  infantile, or juvenile.
- Review IEMbase cortical atrophy, cardiopulmonary failure, gingival
  hyperplasia, speech, and gait rows as possible local additions.

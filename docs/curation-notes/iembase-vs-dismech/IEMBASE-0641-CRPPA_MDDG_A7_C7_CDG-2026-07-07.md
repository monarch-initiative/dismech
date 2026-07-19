# IEMbase 0641: CRPPA-related muscular dystrophy-dystroglycanopathy types A7 and C7

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 641 |
| Nosology | 18.2.07.02 |
| Gene | CRPPA |
| External IDs | OMIM:614643; OMIM:616052; ORPHA:899 |
| Generated mapping | UNMAPPED; weak candidate `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents CRPPA-CDG as autosomal recessive muscular
dystrophy-dystroglycanopathy covering the severe type A7 and milder type C7
ends of the spectrum.

Biochemical rows include normal-to-increased plasma creatine kinase, normal
serum sialotransferrins, and abnormal matriglycan-specific antibody signal.
Clinical rows span Walker-Warburg / muscle-eye-brain territory: agyria,
pachygyria, cerebellar dysplasia, brain vascular anomalies, brainstem and
cerebellar hypoplasia, corpus callosum agenesis, cobblestone lissencephaly,
hydrocephalus, neural tube defect, microphthalmia, anterior chamber anomalies,
corneal clouding, cataract, chorioretinal degeneration, persistent
hyperplastic primary vitreous, optic nerve hypoplasia, limb deformities, calf
pseudohypertrophy, cardiac dysfunction, gonadal dysgenesis, hypotonia, and
muscular dystrophy.

## DisMech phenotype coverage

`Dystroglycanopathy.yaml` already represents CRPPA as `MDDG7 (CRPPA)`,
describing CRPPA/ISPD as the CDP-ribitol synthase donor pathway for fukutin and
FKRP and noting documented severity types A7 and C7. It also captures the
shared disease mechanism, type A and type C severity framework, abnormal
alpha-dystroglycan glycosylation / matriglycan readout, elevated CK, muscular
dystrophy, proximal weakness, cobblestone lissencephaly, retinal dysplasia,
intellectual disability, seizures, hydrocephalus, and neonatal hypotonia.

The local entry is less explicit for several IEMbase CRPPA-specific findings,
including brain vascular anomalies, anterior chamber anomalies, persistent
hyperplastic primary vitreous, optic nerve hypoplasia, gonadal dysgenesis, and
limb deformities.

## Concordance and completeness

Judgement: broad local coverage, but not exact IEMbase row-level coverage.

The generated `UNMAPPED` status under-calls current DisMech coverage because
CRPPA is already embedded in `Dystroglycanopathy.yaml`. The remaining gap is
not a missing disease-family anchor; it is the absence of a structured CRPPA
A7/C7 cross-product subtype with the richer eye/brain/limb phenotype profile.

## Curation actions

- Map to `Dystroglycanopathy.yaml` as covered broadly.
- If precise MONDO/OMIM row coverage is needed, add a CRPPA A7/C7 subtype or
  cross-reference under the existing CRPPA gene subtype.
- Preserve normal sialotransferrins, abnormal matriglycan antibody, CK
  variability, severe brain/eye malformation, cardiac, limb, gonadal,
  hypotonia, and muscular dystrophy prompts.

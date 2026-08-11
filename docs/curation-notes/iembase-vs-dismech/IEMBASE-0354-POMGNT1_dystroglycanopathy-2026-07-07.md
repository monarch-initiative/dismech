# IEMbase 0354: POMGNT1-related muscular dystrophy-dystroglycanopathy

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 354 |
| Nosology | 18.2.03.03 |
| Gene | POMGNT1 |
| External IDs | OMIM:253280; OMIM:613151; OMIM:613157; ORPHA:899 |
| Generated mapping | UNMAPPED; low candidate `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml#MDDG3/POMGNT1` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents POMGNT1-CDG/muscular dystrophy-dystroglycanopathy type A3,
type B3, and type C3, an autosomal recessive O-mannosylation disorder.
Characteristic rows include buphthalmos, cerebral cortical malformations,
increased creatine kinase, epilepsy, exophthalmia, glaucoma, megalocornea,
microphthalmia, muscle-eye-brain disease, muscular dystrophy, psychomotor
delay, and normal sialotransferrins.

Additional clinical rows include corpus callosum agenesis on MRI, cataract,
cerebellar abnormalities, cobblestone lissencephaly, dysmorphic features,
encephalocele, hydrocephalus, myopia, and pigmentary retinopathy. Biochemical
rows include creatine kinase, matriglycan-specific monoclonal antibody, and
sialotransferrins. No treatment rows are present.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. DisMech has a
Dystroglycanopathy file that explicitly covers muscular
dystrophy-dystroglycanopathy types A/B/C and the POMGNT1/MDDG3 subtype. Local
mechanism describes defective O-mannosyl glycosylation of alpha-dystroglycan;
POMGNT1 catalyzes addition of GlcNAc to the O-mannose M1 branch and can produce
the full type A/B/C severity spectrum.

Local coverage includes muscular dystrophy, proximal weakness, neonatal
hypotonia, elevated serum CK, cobblestone lissencephaly, intellectual
disability, retinal dysplasia, hydrocephalus, seizures, reduced
alpha-dystroglycan glycosylation, reduced laminin binding, supportive
rehabilitation, genetic counseling, and emerging ribitol/AAV therapeutic
context.

## Concordance and completeness

Judgement: false negative; resolve to the local dystroglycanopathy POMGNT1
subtype.

The resources agree on POMGNT1 identity, autosomal recessive inheritance,
O-mannosylation/alpha-dystroglycan biology, muscle-eye-brain/type A severe
spectrum, muscular dystrophy, elevated CK, cortical/cobblestone brain
malformations, hydrocephalus, seizures, ocular involvement, and psychomotor
delay.

## Curation actions

- Map this record to `Dystroglycanopathy.yaml`, specifically the POMGNT1/MDDG3
  subtype context.
- Consider future enrichment with buphthalmos, megalocornea, microphthalmia,
  cataract, glaucoma, exophthalmia, myopia, pigmentary retinopathy, corpus
  callosum agenesis, encephalocele, muscle-eye-brain labeling, and matriglycan
  antibody testing after source verification.
- Treat absent IEMbase treatment rows as incomplete IEMbase coverage rather
  than a contradiction of local supportive and investigational therapy context.

# IEMbase 0352: POMT1-related muscular dystrophy-dystroglycanopathy

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 352 |
| Nosology | 18.2.01.06 |
| Gene | POMT1 |
| External IDs | OMIM:236670; OMIM:613555; OMIM:609308; ORPHA:86812 |
| Generated mapping | UNMAPPED; low candidate `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml#MDDG1/POMT1` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents POMT1-CDG/muscular dystrophy-dystroglycanopathy type A1,
type B1, and type C1, an autosomal recessive O-mannosylation disorder.
Characteristic rows include buphthalmos, cataract, increased creatine kinase,
glaucoma, megalocornea, microphthalmia, pigmentary retinopathy, psychomotor
delay, normal sialotransferrins, and Walker-Warburg syndrome.

Additional clinical rows include corpus callosum agenesis on MRI, cerebellar
abnormalities, cerebral cortical malformations, cobblestone lissencephaly,
dysmorphic features, encephalocele, epilepsy, exophthalmia, fatal evolution
before 1 year, hydrocephalus, and muscular dystrophy. Biochemical rows include
creatine kinase, matriglycan-specific monoclonal antibody, and
sialotransferrins. No treatment rows are present.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. DisMech has a
Dystroglycanopathy file that explicitly covers muscular
dystrophy-dystroglycanopathy types A/B/C and the POMT1/MDDG1 subtype. Local
mechanism describes defective O-mannosyl glycosylation of alpha-dystroglycan,
with POMT1 catalyzing the first O-mannosylation step and producing the full
severity spectrum from Walker-Warburg syndrome to limb-girdle muscular
dystrophy.

Local coverage includes muscular dystrophy, proximal weakness, neonatal
hypotonia, elevated serum CK, cobblestone lissencephaly, intellectual
disability, retinal dysplasia, hydrocephalus, seizures, reduced
alpha-dystroglycan glycosylation, reduced laminin binding, supportive
rehabilitation, genetic counseling, and emerging ribitol/AAV therapeutic
context.

## Concordance and completeness

Judgement: false negative; resolve to the local dystroglycanopathy POMT1
subtype.

The resources agree on POMT1 identity, autosomal recessive inheritance,
O-mannosylation/alpha-dystroglycan biology, Walker-Warburg/type A severe
spectrum, muscular dystrophy, elevated CK, cobblestone/cortical brain
malformations, hydrocephalus, seizures, ocular involvement, psychomotor delay,
and early lethality in the severe end.

## Curation actions

- Map this record to `Dystroglycanopathy.yaml`, specifically the POMT1/MDDG1
  subtype context.
- Consider future enrichment with buphthalmos, megalocornea, microphthalmia,
  cataract, glaucoma, pigmentary retinopathy, corpus callosum agenesis,
  encephalocele, fatal-before-1-year wording, and matriglycan antibody testing
  after source verification.
- Treat absent IEMbase treatment rows as incomplete IEMbase coverage rather
  than a contradiction of local supportive and investigational therapy context.

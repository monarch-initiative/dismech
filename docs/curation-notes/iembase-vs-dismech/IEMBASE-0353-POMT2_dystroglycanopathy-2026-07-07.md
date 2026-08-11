# IEMbase 0353: POMT2-related muscular dystrophy-dystroglycanopathy

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 353 |
| Nosology | 18.2.02.02 |
| Gene | POMT2 |
| External IDs | OMIM:613150; OMIM:613156; OMIM:613158; ORPHA:899 |
| Generated mapping | UNMAPPED; low candidate `Dystroglycanopathy.yaml` |
| Candidate DisMech targets | `Dystroglycanopathy.yaml#MDDG2/POMT2` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents POMT2-CDG/muscular dystrophy-dystroglycanopathy type A2,
type B2, and type C2, an autosomal recessive O-mannosylation disorder.
Characteristic rows include buphthalmos, cerebral cortical malformations,
increased creatine kinase, glaucoma, megalocornea, microphthalmia, muscular
dystrophy, pigmentary retinopathy, psychomotor delay, normal sialotransferrins,
and Walker-Warburg syndrome.

Additional clinical rows include corpus callosum agenesis on MRI, cataract,
cerebellar abnormalities, cobblestone lissencephaly, dysmorphic features,
encephalocele, epilepsy, exophthalmia, fatal evolution before 1 year, and
hydrocephalus. Biochemical rows include creatine kinase,
matriglycan-specific monoclonal antibody, and sialotransferrins. No treatment
rows are present.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. DisMech has a
Dystroglycanopathy file that explicitly covers muscular
dystrophy-dystroglycanopathy types A/B/C and the POMT2/MDDG2 subtype. Local
mechanism describes defective O-mannosyl glycosylation of alpha-dystroglycan;
POMT2 forms the POMT1-POMT2 enzyme complex required for the first
O-mannosylation step and can produce the full type A/B/C severity spectrum.

Local coverage includes muscular dystrophy, proximal weakness, neonatal
hypotonia, elevated serum CK, cobblestone lissencephaly, intellectual
disability, retinal dysplasia, hydrocephalus, seizures, reduced
alpha-dystroglycan glycosylation, reduced laminin binding, supportive
rehabilitation, genetic counseling, and emerging ribitol/AAV therapeutic
context.

## Concordance and completeness

Judgement: false negative; resolve to the local dystroglycanopathy POMT2
subtype.

The resources agree on POMT2 identity, autosomal recessive inheritance,
O-mannosylation/alpha-dystroglycan biology, Walker-Warburg/type A severe
spectrum, muscular dystrophy, elevated CK, cortical/cobblestone brain
malformations, hydrocephalus, seizures, ocular involvement, psychomotor delay,
and early lethality in the severe end.

## Curation actions

- Map this record to `Dystroglycanopathy.yaml`, specifically the POMT2/MDDG2
  subtype context.
- Consider future enrichment with buphthalmos, megalocornea, microphthalmia,
  cataract, glaucoma, pigmentary retinopathy, corpus callosum agenesis,
  encephalocele, fatal-before-1-year wording, and matriglycan antibody testing
  after source verification.
- Treat absent IEMbase treatment rows as incomplete IEMbase coverage rather
  than a contradiction of local supportive and investigational therapy context.

# IEMbase 0273: ACOX1-related peroxisomal acyl-CoA oxidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 273 |
| Nosology | 14.2.02.01 |
| Gene | ACOX1 |
| External IDs | OMIM:264470; ORPHA:2971 |
| Generated mapping | UNMAPPED; weak candidate `Peroxisomal_Acyl-CoA_Oxidase_Deficiency.yaml` |
| Candidate DisMech targets | `Peroxisomal_Acyl-CoA_Oxidase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive peroxisomal straight-chain acyl-CoA
oxidase deficiency, also labeled pseudo-neonatal adrenoleukodystrophy or SCOX.
Treatability is marked unknown and the cached JSON has no treatment rows.

Characteristic clinical rows include sensorineural deafness, defective visual
acuity, diminished ERG response, and osteopenia. Additional clinical rows
include developmental delay, ataxia, diminished brain auditory evoked
potentials, cataract, retinitis pigmentosa, cerebral cortical dysplasia,
cerebral white-matter involvement, hypotonia, intellectual disability,
seizures, spastic paresis, peripheral neuropathy, dysmorphic features,
clubfoot, epiphyseal and periarticular calcific stippling, hepatomegaly,
jaundice, portal hypertension, renal cysts, failure to thrive, diarrhea, and
glaucoma.

The biochemical signal includes elevated very-long-chain fatty acids,
phytanic acid, pipecolic acid, AST/ALT, and fat-soluble vitamin abnormalities,
with low or low-normal coagulation factors, DHA, and plasmalogens.

## DisMech phenotype coverage

`Peroxisomal_Acyl-CoA_Oxidase_Deficiency.yaml` is the correct local target.
The entry is ACOX1-specific and covers the straight-chain acyl-CoA oxidase
block, impaired peroxisomal VLCFA beta-oxidation, VLCFA accumulation,
inflammatory signaling, neurodegenerative white-matter disease, infantile
hypotonia, seizures, psychomotor delay, developmental regression, visual and
hearing impairment, retinitis pigmentosa, facial dysmorphism, hepatic
dysfunction, adrenal insufficiency, peripheral neuropathy, and the expected
distinction from broader peroxisome biogenesis defects.

## Concordance and completeness

Judgement: false negative mapping; resolve to the local ACOX1 file.

IEMbase and DisMech agree on ACOX1 identity, autosomal recessive inheritance,
VLCFA accumulation, infantile neurodegenerative/leukodystrophy framing, visual
and auditory involvement, hypotonia, seizures, developmental delay/regression,
and peripheral neuropathy. DisMech is richer for mechanism and for the
important differential point that isolated ACOX1 deficiency is not a generalized
peroxisome biogenesis defect.

Some IEMbase lab rows should be imported cautiously. The local ACOX1 entry
explicitly distinguishes isolated ACOX1 beta-oxidation disease from generalized
PBD by normal phytanic/pristanic oxidation and normal plasmalogen synthesis in
reported biochemical testing, whereas IEMbase lists low-normal plasmalogens and
normal-to-increased phytanic/pristanic/pipecolic rows. Those rows may reflect a
generic peroxisomal-disorder panel rather than ACOX1-specific findings.

## Curation actions

- Resolve this record to `Peroxisomal_Acyl-CoA_Oxidase_Deficiency.yaml`.
- Use IEMbase's ocular-test, osteopenia, portal-hypertension, renal-cyst, and
  skeletal rows only as review prompts.
- Do not import IEMbase plasmalogen/phytanic/pristanic directionality without
  ACOX1-specific evidence review.

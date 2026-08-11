# IEMbase 0272: PEX1-related peroxin 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 272 |
| Nosology | 19.3.01.01 |
| Gene | PEX1 |
| External IDs | OMIM:234580; OMIM:214100; OMIM:601539; ORPHA:772 |
| Generated mapping | CANDIDATE to `Peroxisome_Biogenesis_Disorder.yaml` |
| Candidate DisMech targets | `Peroxisome_Biogenesis_Disorder.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PEX1-related peroxisome biogenesis disorder, spanning
Zellweger spectrum disease 1A, neonatal adrenoleukodystrophy/infantile Refsum
disease spectrum labels, and Heimler syndrome type 1. Inheritance is autosomal
recessive. Treatability is marked unknown and there are no treatment rows in
the cached JSON.

Characteristic clinical rows are sensorineural deafness, defective visual
acuity, and developmental delay. The broader clinical checklist includes
ataxia, diminished brain auditory evoked potentials, diminished ERG response,
cataract, retinitis pigmentosa, glaucoma, cerebral neocortical dysplasia,
cerebral white-matter involvement, hypotonia, intellectual disability,
seizures, hypsarrhythmia, spastic paresis, peripheral neuropathy, dysmorphic
features, clubfoot, delayed tooth eruption, epiphyseal and periarticular
calcific stippling, hepatomegaly, jaundice, portal hypertension, renal cysts,
failure to thrive, diarrhea, and osteopenia.

The biochemical panel is the generalized PBD/ZSD pattern: increased
very-long-chain fatty acids, phytanic acid, pristanic acid, pipecolic acid,
bile-acid intermediates, and AST/ALT; low or low-normal coagulation factors,
DHA, fat-soluble vitamins, and plasmalogens; and reduced adrenocortical
reserve in later age groups.

## DisMech phenotype coverage

`Peroxisome_Biogenesis_Disorder.yaml` is the correct file-level target. It
models PEX-gene peroxisome assembly and matrix-import failure, includes PEX1 in
the genetic/pathophysiology coverage, and captures VLCFA and bile-acid
intermediate accumulation, phytanic acid, plasmalogen and DHA deficiency,
neurologic dysfunction, hepatic dysfunction, skeletal involvement, retinopathy,
hearing loss, adrenal insufficiency, and supportive or dietary management.

The local entry is an umbrella PBD/ZSD entry rather than a PEX1-only subtype,
so it is broader than this IEMbase record.

## Concordance and completeness

Judgement: accept the generated candidate as the correct current target.

IEMbase and DisMech strongly agree on PEX1/ZSD identity, autosomal recessive
inheritance, generalized peroxisomal biochemical disruption, neurologic,
hepatic, retinal, auditory, skeletal, and adrenal involvement. DisMech is
richer for mechanism and cross-PEX context. IEMbase adds useful PEX1-specific
review prompts, especially Heimler-spectrum framing, dental eruption, BAEP/ERG,
portal hypertension, renal cysts, osteopenia, glaucoma, and detailed
age-stratified lab rows.

## Curation actions

- Resolve this record to `Peroxisome_Biogenesis_Disorder.yaml`.
- Treat the mapping as file-level PEX1 coverage, not proof that every PBD
  phenotype applies uniformly to every PEX1 presentation.
- Use IEMbase's Heimler, dental, ocular-test, renal, and portal-hypertension
  rows as enrichment prompts.

# IEMbase 0319: CTSA-related cathepsin A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 319 |
| Nosology | 20.3.02.01 |
| Gene | CTSA |
| External IDs | OMIM:256540; ORPHA:351 |
| Generated mapping | MAPPED; `Galactosialidosis.yaml` |
| Candidate DisMech targets | `Galactosialidosis.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents CTSA-related cathepsin A deficiency as galactosialidosis.
Characteristic rows include ataxia, cardiomyopathy, coarse facial features,
dysostosis multiplex, fetal hydrops, foam cells, hepatosplenomegaly,
intellectual deterioration, myoclonus, renal failure, telangiectasia, and
vacuolated lymphocytes.

Additional clinical rows include angiokeratoma, cherry-red spot, corneal
clouding, edema, growth retardation, hernias, proteinuria, seizures,
spasticity, valvular thickening, and impaired vision.

The biochemical rows include alpha-neuraminidase activity, beta-galactosidase,
urinary sialic acid-rich oligosaccharide, and cathepsin A activity. No
treatment rows are present.

## DisMech phenotype coverage

`Galactosialidosis.yaml` is the correct local target. It models CTSA/PPCA
deficiency with secondary NEU1 and GLB1 deficiency and covers cherry-red spot
of the macula, coarse facial features, dysostosis multiplex, angiokeratoma,
hepatosplenomegaly, intellectual disability, ataxia, short stature, abnormal
vertebral morphology, hearing impairment, seizure, corneal opacity, and
supportive care.

The local entry has strong genetic and mechanistic CTSA coverage, but its
structured biochemical section is sparse relative to IEMbase's enzyme and
oligosaccharide rows.

## Concordance and completeness

Judgement: correct high-confidence mapping to `Galactosialidosis.yaml`.

Concordance is high for CTSA identity, galactosialidosis scope, coarse facial
features, dysostosis multiplex, hepatosplenomegaly, angiokeratoma, ataxia,
cherry-red spot, seizure, corneal opacity/clouding, intellectual involvement,
and supportive-care context.

IEMbase adds review prompts for fetal hydrops, foam cells, myoclonus, renal
failure, telangiectasia, vacuolated lymphocytes, edema, hernias, proteinuria,
spasticity, valvular thickening, impaired vision, and the combined enzyme and
urinary oligosaccharide diagnostic profile.

## Curation actions

- Keep the generated galactosialidosis mapping.
- Consider adding structured biochemical rows for cathepsin A activity,
  alpha-neuraminidase activity, beta-galactosidase activity, and urinary
  sialic acid-rich oligosaccharides if source-backed.
- Review renal, cardiac-valvular, telangiectasia, vacuolated-lymphocyte, and
  fetal-hydrops rows for possible phenotype enrichment.

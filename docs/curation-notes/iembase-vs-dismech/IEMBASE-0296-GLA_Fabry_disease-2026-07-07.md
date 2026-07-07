# IEMbase 0296: GLA-related Alpha-galactosidase A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 296 |
| Nosology | 20.1.13.01 |
| Gene | GLA |
| External IDs | OMIM:301500; ORPHA:324 |
| Generated mapping | MAPPED; `Fabry_Disease.yaml` |
| Candidate DisMech targets | `Fabry_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents Fabry disease / alpha-galactosidase A deficiency. Inheritance
is marked X-linked, treatability is yes, and prevalence is listed as 1:40,000.

Clinical rows include the core Fabry pattern: angiokeratoma, cornea
verticillata, sensorineural hearing loss, proteinuria, stroke-like
encephalopathy, abdominal pain, hypertrophic cardiomyopathy, cerebral
infarction, neuropathic pain, chronic renal failure, and upper-airway or airway
obstruction. IEMbase also adds coarser review prompts such as pulmonary
fibrosis, malignant neoplasia, thyroid dysfunction, coarse facial features,
bulbous/prominent nose, thick eyebrows, thick lips, recessed forehead, and an
ear-lobule dysmorphism row with a source spelling typo. Biochemical rows show
increased globotriaosylceramide and globotriaosylsphingosine. Treatment rows
list agalsidase alfa, agalsidase beta, and migalastat.

## DisMech phenotype coverage

`Fabry_Disease.yaml` is the correct local target. It models GLA deficiency,
lysosomal Gb3 and lyso-Gb3 accumulation, tissue-specific renal, cardiac,
vascular, autonomic, peripheral nerve, ocular, and cutaneous storage, and
classic and late-onset cardiac subtypes.

Local phenotype coverage is broad: acroparesthesia, neuropathic pain,
hypohidrosis, heat intolerance, abdominal pain, nausea/vomiting, angiokeratoma,
proteinuria, chronic kidney disease, left ventricular hypertrophy, arrhythmia,
stroke, transient ischemic attack, hearing impairment, tinnitus, cornea
verticillata, cataract, elevated Gb3, reduced alpha-galactosidase A activity,
nephrotic syndrome, heart failure, and conjunctival telangiectasia. Treatment
coverage includes enzyme replacement therapy, pharmacological chaperone
therapy, investigational substrate reduction, gene therapy, and supportive care.

## Concordance and completeness

Judgement: correct high-concordance mapping to `Fabry_Disease.yaml`.

IEMbase and DisMech agree on GLA identity, X-linked inheritance, Gb3/lyso-Gb3
storage, renal disease, hypertrophic cardiomyopathy, cerebrovascular disease,
neuropathic pain, angiokeratoma, cornea verticillata, hearing involvement, and
the ERT/chaperone treatment landscape. DisMech is substantially richer for
mechanism, subtype structure, renal/cardiac/autonomic pathophysiology, and
therapy classes.

IEMbase adds specific review prompts for airway obstruction, pulmonary fibrosis,
malignancy, thyroid dysfunction, and dysmorphic facial/ear rows. These should be
handled cautiously before import because some may be nonspecific, secondary, or
rare rather than core Fabry features.

## Curation actions

- Keep this record mapped to `Fabry_Disease.yaml`.
- Use the IEMbase treatment rows to check whether local ERT/chaperone entries
  should explicitly name agalsidase alfa, agalsidase beta, and migalastat.
- Review the IEMbase airway, pulmonary fibrosis, malignancy, thyroid, and
  dysmorphic rows before adding them locally.

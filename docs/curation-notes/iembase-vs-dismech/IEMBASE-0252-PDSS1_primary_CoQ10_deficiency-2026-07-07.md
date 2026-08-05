# IEMbase 0252: PDSS1-related Prenyl diphosphate synthase subunit 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 252 |
| Nosology | 8.1.01.01 |
| Gene | PDSS1 |
| External IDs | OMIM:607429; OMIM:607426; ORPHA:254898 |
| Generated mapping | MAPPED; `Primary_Coenzyme_Q10_Deficiency.yaml#PDSS1` |
| Candidate DisMech targets | `Primary_Coenzyme_Q10_Deficiency.yaml#PDSS1` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as PDSS1-related prenyl diphosphate synthase subunit 1
deficiency, with alternate labels primary coenzyme Q10 deficiency type 2 and
trans-prenyl transferase deficiency. The record is autosomal recessive and
treatability is marked unknown, with no treatment rows in the cached JSON.

Biochemical rows include abnormal CoQ10 in fibroblasts, urinary
3-methylglutaconic acid, and plasma lactate. Clinical rows include pulmonary
hypertension, intellectual disability, livedo reticularis, nephrotic syndrome,
peripheral neuropathy, obesity, and phalangeal erythema. Characteristic rows
include cardiomyopathy, deafness, macrocephaly, and optic atrophy.

## DisMech phenotype coverage

`Primary_Coenzyme_Q10_Deficiency.yaml#PDSS1` is the correct local target. The
local file covers autosomal recessive primary CoQ10 biosynthesis disorders and
includes a PDSS1 subtype for decaprenyl diphosphate synthase subunit
dysfunction in the first enzyme/polyisoprenoid side-chain step. The umbrella
entry covers reduced tissue CoQ10, impaired electron transport between
complexes I/II and III, oxidative phosphorylation defects, antioxidant/redox
effects, and renal, neurologic, cardiac, and sensorineural disease with
high-dose oral CoQ10 as disease-targeted therapy.

## Concordance and completeness

Judgement: correct subtype-level mapping, with IEMbase providing more
PDSS1-specific phenotype granularity.

IEMbase and DisMech agree on primary CoQ10 deficiency identity, PDSS1
subtype placement, CoQ10 deficiency, mitochondrial energy failure, neurologic,
renal, cardiac, and hearing/optic involvement. The local umbrella is strong
mechanistically but does not currently spell out several PDSS1-specific rows
from IEMbase, including pulmonary hypertension, livedo reticularis, phalangeal
erythema, obesity, macrocephaly, peripheral neuropathy, and
3-methylglutaconic acid.

## Curation actions

- Keep this record mapped to `Primary_Coenzyme_Q10_Deficiency.yaml#PDSS1`.
- No mapping correction is needed.
- Use IEMbase's PDSS1-specific renal, vascular, skin, optic, neuropathy, and
  biomarker rows as enrichment prompts if the subtype is expanded.

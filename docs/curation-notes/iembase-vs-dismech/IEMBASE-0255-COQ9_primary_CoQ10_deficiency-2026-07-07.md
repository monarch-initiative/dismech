# IEMbase 0255: COQ9-related Coenzyme 9 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 255 |
| Nosology | 8.1.09.01 |
| Gene | COQ9 |
| External IDs | OMIM:614654; ORPHA:319678 |
| Generated mapping | MAPPED; `Primary_Coenzyme_Q10_Deficiency.yaml#COQ9` |
| Candidate DisMech targets | `Primary_Coenzyme_Q10_Deficiency.yaml#COQ9` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as COQ9-related coenzyme 9 deficiency, with alternate
labels primary coenzyme Q1 deficiency type 5 and COQ9. The record is autosomal
recessive and treatability is marked unknown, with no treatment rows in the
cached JSON. The cached alternate label appears to use "Q1" where primary
coenzyme Q10 deficiency type 5 is expected.

Biochemical rows include abnormal CoQ10 in fibroblasts and muscle and plasma
lactate. Clinical rows include cardiomyopathy, epilepsy, and psychomotor
regression. Characteristic rows include feeding difficulties, hypothermia,
lactic acidosis, and renal tubulopathy.

## DisMech phenotype coverage

`Primary_Coenzyme_Q10_Deficiency.yaml#COQ9` is the correct local target. The
local subtype includes COQ9-related neonatal encephalomyopathy, while the
umbrella file covers primary CoQ10 biosynthesis defects, respiratory-chain
energy failure, lactic acidosis, encephalopathy/seizures, cardiomyopathy,
renal disease, and CoQ10 supplementation. The current COQ9 subtype is thinner
than the umbrella and includes less human phenotype detail than IEMbase.

## Concordance and completeness

Judgement: correct subtype-level mapping, with IEMbase useful for human
phenotype enrichment.

IEMbase and DisMech agree on COQ9 primary CoQ10 deficiency, reduced CoQ10,
mitochondrial energy disease, lactic acidosis, epilepsy, cardiomyopathy,
psychomotor regression/encephalopathy, and renal involvement. IEMbase adds
feeding difficulties, hypothermia, and renal tubulopathy as explicit subtype
rows and flags a likely alternate-label typo for metadata review.

## Curation actions

- Keep this record mapped to `Primary_Coenzyme_Q10_Deficiency.yaml#COQ9`.
- Review the cached/source alternate label "primary coenzyme Q1 deficiency type
  5" before reusing it in curated metadata.
- Use IEMbase's feeding, temperature, renal tubulopathy, and biomarker rows if
  the COQ9 subtype is expanded.

# IEMbase 0591: SAMD9-related MIRAGE syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 591 |
| Nosology | 25.1.3.01 |
| Gene | SAMD9 |
| External IDs | OMIM:617053; ORPHA:494433 |
| Generated mapping | UNMAPPED; best candidate `CHARGE_Syndrome.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SAMD9-related MIRAGE syndrome, expanded as myelodysplasia,
infection, restriction of growth, adrenal hypoplasia, genital phenotypes, and
enteropathy syndrome. The record is autosomal dominant, classified as
unclassified, has unknown treatability, and has no treatment rows.

Biochemical rows include increased renin activity, very increased plasma
corticotropin, normal aldosterone, and decreased plasma cortisol. Clinical rows
include chronic diarrhea, external genital abnormality, myelodysplasia,
recurrent bacterial infections, adrenal insufficiency, developmental delay, and
thrombocytopenia.

## DisMech phenotype coverage

`CHARGE_Syndrome.yaml` is a false-positive generated candidate. CHARGE models
CHD7 haploinsufficiency with neural-crest and placode developmental mechanisms,
coloboma, heart defects, choanal atresia, growth/developmental delay, genital
anomalies, and ear anomalies. It does not represent SAMD9, MIRAGE syndrome,
adrenal hypoplasia/insufficiency, myelodysplasia, thrombocytopenia, or the
enteropathy-infection phenotype bundle.

The local knowledge base mentions SAMD9/SAMD9L only as broad marrow-failure
context elsewhere; no exact MIRAGE syndrome target was identified.

## Concordance and completeness

Judgement: true local gap; reject CHARGE syndrome as an exact target.

The generated candidate is explainable by overlapping growth, developmental,
and genital-anomaly language, but the disease identity is different. IEMbase
centers a SAMD9 adrenal-marrow-immune-enteropathy syndrome, not a CHD7
developmental-malformation syndrome.

## Curation actions

- Create or identify an exact SAMD9 / MIRAGE syndrome target before import.
- Reject `CHARGE_Syndrome.yaml` as an exact mapping.
- Preserve adrenal-axis biomarkers, myelodysplasia, thrombocytopenia,
  recurrent infection, chronic diarrhea, genital anomaly, and developmental
  delay as source-review prompts.

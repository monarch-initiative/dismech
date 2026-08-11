# IEMbase 0258: AGA-related Aspartylglucosaminidase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 258 |
| Nosology | 20.3.07.01 |
| Gene | AGA |
| External IDs | OMIM:208400; ORPHA:93 |
| Generated mapping | MAPPED; `Aspartylglucosaminuria.yaml` |
| Candidate DisMech targets | `Aspartylglucosaminuria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as AGA-related aspartylglucosaminidase deficiency, with
alternate labels aspartylglucosaminuria and AGU. The record is autosomal
recessive and treatability is marked yes.

The treatment section lists hematopoietic stem cell transplant as a stem-cell
strategy with level 4-5 evidence and PMID 15316370. Biochemical rows include
decreased aspartylglucosaminidase activity in fibroblasts, lymphocytes, and
white blood cells, plus increased urinary aspartylglucosamine. Clinical rows
include angiokeratoma, clubfoot, axial muscular hypotonia, and vacuolated
lymphocytes.

## DisMech phenotype coverage

`Aspartylglucosaminuria.yaml` is the correct local target. The local entry
covers biallelic AGA pathogenic variants, deficient lysosomal
aspartylglucosaminidase/glycosylasparaginase activity, glycoasparagine and
aspartylglucosamine accumulation, urinary aspartylglucosamine, progressive
neurodevelopmental and behavioral disease, seizures, speech impairment, systemic
connective-tissue and skeletal findings, recurrent infections, hepatosplenic
involvement, enzyme testing, molecular testing, supportive care, hematopoietic
stem cell transplantation with lack-of-benefit caveats, preclinical enzyme
replacement, and preclinical AAV9/AGA therapy.

## Concordance and completeness

Judgement: correct mapping with high biochemical concordance and a treatment
interpretation caveat.

IEMbase and DisMech agree on AGA/AGU identity, autosomal recessive inheritance,
reduced aspartylglucosaminidase activity, and urinary aspartylglucosamine
elevation. IEMbase adds concise rows for angiokeratoma, clubfoot, axial
hypotonia, and vacuolated lymphocytes. DisMech is much broader clinically and
mechanistically. The treatment rows need nuance: IEMbase lists transplant as a
treatment, whereas DisMech explicitly records that limited transplant attempts
have not shown clear benefit.

## Curation actions

- Keep this record mapped to `Aspartylglucosaminuria.yaml`.
- Do not import the transplant row as unqualified effective therapy without the
  local lack-of-benefit caveat.
- Use IEMbase's angiokeratoma, clubfoot, axial hypotonia, and vacuolated
  lymphocyte rows as future phenotype review prompts.

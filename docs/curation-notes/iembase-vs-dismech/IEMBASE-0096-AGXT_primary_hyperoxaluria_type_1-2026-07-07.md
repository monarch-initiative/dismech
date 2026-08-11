# IEMbase 0096: AGXT-related alanine-glyoxylate aminotransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 96 |
| Nosology | 13.1.04.01 |
| Gene | AGXT |
| External IDs | OMIM:259900 |
| Generated mapping | UNMAPPED; best fuzzy candidate `ornithine_aminotransferase_deficiency.yaml` |
| Candidate DisMech targets | `Primary_Hyperoxaluria_Type_1.yaml`; `Disorders_of_Glyoxylate_and_Oxalate_Metabolism.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive peroxisomal
alanine-glyoxylate aminotransferase deficiency, with alternate labels primary
hyperoxaluria type 1, AGT, and PH1. Treatability is marked unknown, and
prevalence is listed near 1:500,000.

The characteristic biochemical rows are plasma and urinary oxalic acid and
plasma and urinary glycolic acid. The wider panel also includes plasma
creatinine and urea.

The characteristic clinical rows include failure to thrive, growth retardation,
nephrocalcinosis, nephrolithiasis, radiolucent metaphyseal bands, renal colic,
and chronic renal failure.

Treatment rows include lumasiran, kidney transplantation, liver
transplantation, hyperhydration, potassium citrate, and pyridoxine.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. The best local disease target
is `Primary_Hyperoxaluria_Type_1.yaml`, with
`Disorders_of_Glyoxylate_and_Oxalate_Metabolism.yaml` as grouping context.

DisMech models PH1 as biallelic AGXT deficiency of hepatic peroxisomal
alanine-glyoxylate aminotransferase, impaired glyoxylate-to-glycine conversion,
glyoxylate diversion to oxalate, urinary calcium oxalate supersaturation,
nephrolithiasis, nephrocalcinosis, chronic kidney disease, and systemic
oxalosis after kidney failure. The grouping explicitly distinguishes the AGXT
mechanism from GRHPR/PH2 and other glyoxylate-oxalate pathway members.

`ornithine_aminotransferase_deficiency.yaml` is an aminotransferase-name false
positive and should not be used for this IEMbase record.

## Concordance and completeness

Judgement: false-negative mapping with high local mechanistic coverage.

DisMech currently lacks much of the IEMbase treatment list for PH1 and does not
separately capture glycolic acid, creatinine, urea, renal colic, growth failure,
or radiolucent metaphyseal bands in the disease entry. IEMbase is therefore
useful as a treatment and phenotype-gap checklist.

## Curation actions

- Update the mapping logic or manual crosswalk to resolve this record to
  `Primary_Hyperoxaluria_Type_1.yaml`.
- Keep `Disorders_of_Glyoxylate_and_Oxalate_Metabolism.yaml` as grouping
  context, not the primary disease target.
- Consider adding PH1 treatment coverage for lumasiran, pyridoxine,
  hyperhydration/citrate, and liver/kidney transplantation with evidence.

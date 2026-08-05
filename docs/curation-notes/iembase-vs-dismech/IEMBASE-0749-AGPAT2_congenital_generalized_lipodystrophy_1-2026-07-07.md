# IEMbase 0749: AGPAT2-related lysophosphatidic acid acyltransferase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 749 |
| Nosology | 14.4.02.01 |
| Nosology code | IEM0656 |
| Gene | AGPAT2 |
| External IDs | OMIM:608594; ORPHA:528 |
| Generated mapping | MAPPED; `Berardinelli_Seip_Congenital_Lipodystrophy.yaml` |
| Candidate DisMech targets | `Berardinelli_Seip_Congenital_Lipodystrophy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as AGPAT2-related
lysophosphatidic acid acyltransferase deficiency, with alternate names
congenital generalized lipodystrophy type 1 and Berardinelli-Seip syndrome. The
phenotype and biochemical rows emphasize high serum triglycerides, abnormal
subcutaneous fat distribution, hepatomegaly, hepatic steatosis, and
insulin-dependent diabetes mellitus across childhood through adulthood, with
some neonatal or infantile flags.

## DisMech phenotype coverage

`Berardinelli_Seip_Congenital_Lipodystrophy.yaml` is the exact local target.
It carries the ORPHA:528 disease identity and includes congenital generalized
lipodystrophy type 1 / AGPAT2 as a subtype. The entry models AGPAT2
acylglycerol synthesis dysfunction, decreased triglyceride biosynthesis,
adipocyte storage failure, generalized adipose tissue loss, ectopic
triglyceride accumulation, hypoleptinemia, and severe insulin resistance.

Phenotype coverage is strong for the IEMbase signal: lipodystrophy/adipose
tissue loss, insulin resistance or diabetes, hypertriglyceridemia,
hepatomegaly, and hepatic steatosis are all represented locally.

## Concordance and completeness

Judgement: correct exact mapping with high concordance.

IEMbase is subtype-specific for AGPAT2 / CGL1, while the DisMech entry is a
broader Berardinelli-Seip congenital lipodystrophy target that includes this
subtype explicitly. The main wording difference is that IEMbase says
insulin-dependent diabetes mellitus, whereas DisMech models diabetes and severe
insulin resistance more generally.

## Curation actions

- Keep `Berardinelli_Seip_Congenital_Lipodystrophy.yaml` as the exact mapping.
- Preserve the AGPAT2 / CGL1 subtype identity when using this note for future
  phenotype curation.
- Consider whether insulin-dependent diabetes wording should be normalized or
  captured as source-specific detail.

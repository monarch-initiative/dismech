# IEMbase 0754: PNPLA2-related adipose triglyceride lipase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 754 |
| Nosology | 14.4.07.01 |
| Nosology code | IEM0661 |
| Gene | PNPLA2 |
| External IDs | OMIM:610717; ORPHA:98908 |
| Generated mapping | MAPPED; `Neutral_Lipid_Storage_Myopathy.yaml` |
| Candidate DisMech targets | `Neutral_Lipid_Storage_Myopathy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as PNPLA2-related adipose
triglyceride lipase deficiency, with alternate name neutral lipid storage
disease with myopathy. The source rows include elevated creatine kinase,
myopathy, muscle atrophy, muscle lipid droplets, muscle vacuoles, lipid
deposition, Jordans anomaly, cardiomyopathy, hepatomegaly, hepatic steatosis,
and insulin-dependent diabetes mellitus. Many features are possible in
childhood or adolescence and present in adulthood.

## DisMech phenotype coverage

`Neutral_Lipid_Storage_Myopathy.yaml` is the exact local target. It carries the
ORPHA:98908 disease identity and PNPLA2 / ATGL gene context, and models
impaired triglyceride hydrolysis with cytoplasmic triglyceride droplets
especially affecting skeletal and cardiac muscle.

DisMech coverage is strong for the core PNPLA2 / NLSDM identity, including
myopathy, hyperCKemia, cardiomyopathy, muscle fatty infiltration, limb muscle
atrophy, easy fatigability, and absence of ichthyosis as a key contrast with
ABHD5-related disease.

## Concordance and completeness

Judgement: correct exact mapping with partial phenotype-completeness gaps.

The local entry covers the central disease mechanism and neuromuscular/cardiac
phenotypes well. IEMbase adds or emphasizes hepatic and metabolic prompts that
are less explicit locally, including hepatomegaly, hepatic steatosis,
insulin-dependent diabetes, and Jordans anomaly as a source phenotype row.

## Curation actions

- Keep `Neutral_Lipid_Storage_Myopathy.yaml` as the exact mapping.
- Consider adding or checking explicit phenotype coverage for hepatomegaly,
  hepatic steatosis, insulin-dependent diabetes, muscle lipid droplets or
  vacuoles, and Jordans anomaly.
- Preserve the adult-predominant but childhood/adolescent-possible age pattern
  from IEMbase.

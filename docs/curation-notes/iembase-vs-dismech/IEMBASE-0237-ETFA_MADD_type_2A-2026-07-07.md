# IEMbase 0237: ETFA-related Electron transfer flavoprotein alpha subunit deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 237 |
| Nosology | 4.2.06.01 |
| Gene | ETFA |
| External IDs | OMIM:231680 |
| Generated mapping | CANDIDATE; `Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml` |
| Candidate DisMech targets | `Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ETFA-related electron transfer flavoprotein alpha
subunit deficiency, with alternate labels glutaric aciduria type 2A and multiple
acyl-CoA dehydrogenase deficiency type 2A. The record is autosomal recessive and
treatability is marked yes.

Treatment rows include beta-hydroxybutyrate, carnitine, and riboflavin.
Biochemical rows include broad acylglycine elevations, sarcosine in plasma and
urine, C4 through C18 acylcarnitine elevations, low or normal free carnitine,
creatine kinase and transaminase elevations, low ketones during hypoglycemia,
multiple dicarboxylic and organic acids including ethylmalonic, glutaric,
adipic, sebacic, suberic, and D-2-hydroxyglutaric acids, and low-normal
glucose. Clinical and characteristic rows include congenital brain and kidney
anomalies, metabolic acidosis, renal cysts, cardiomyopathy, coma, hypotonia,
lethargy, liver dysfunction, exercise-induced rhabdomyolysis, and skeletal
myopathy.

## DisMech phenotype coverage

`Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml` covers ETFA, ETFB, and ETFDH
as causative genes for MADD. It represents the shared electron-transfer defect,
blocked transfer of reducing equivalents from multiple flavoprotein
dehydrogenases, broad acylcarnitine and organic-acid abnormalities, glutaric and
dicarboxylic aciduria, hypoketotic hypoglycemia, metabolic acidosis,
hyperammonemia, cardiomyopathy, coma/encephalopathy, hepatic involvement,
myopathy/rhabdomyolysis, congenital anomalies, renal cystic dysplasia, and
riboflavin-responsive treatment context.

## Concordance and completeness

Judgement: accept the generated candidate as the correct file-level target.

IEMbase is subtype-specific for ETFA/MADD type 2A. DisMech currently represents
MADD as a shared disease file with gene-specific sections rather than separate
ETFA, ETFB, and ETFDH subtype files. That is sufficient for a correct mapping:
the gene, mechanism, biomarker pattern, neonatal-congenital spectrum, myopathic
features, and treatment context align.

IEMbase adds useful granular prompts for sarcosine, D-2-hydroxyglutaric acid,
specific acylglycines, and beta-hydroxybutyrate treatment context.

## Curation actions

- Keep this mapped to `Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml`.
- If subtype granularity is later added, record this as ETFA-related MADD type
  2A/electron transfer flavoprotein alpha subunit deficiency.
- Consider IEMbase's granular analyte list when refreshing MADD diagnostic
  markers.

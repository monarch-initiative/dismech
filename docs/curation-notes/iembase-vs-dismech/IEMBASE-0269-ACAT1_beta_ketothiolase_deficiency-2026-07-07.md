# IEMbase 0269: ACAT1-related mitochondrial acetoacetyl-CoA thiolase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 269 |
| Nosology | 4.3.13.01 |
| Gene | ACAT1 |
| External IDs | OMIM:203750; ORPHA:134 |
| Generated mapping | MAPPED to `Beta-Ketothiolase_Deficiency.yaml` |
| Candidate DisMech targets | `Beta-Ketothiolase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents classic autosomal recessive mitochondrial acetoacetyl-CoA
thiolase deficiency, also called beta-ketothiolase T2 deficiency and
alpha-methylacetoacetic aciduria. Treatability is marked yes.

Characteristic clinical rows include ketoacidosis and T2 hyperintensities of
the globus pallidus on MRI. Additional clinical rows include metabolic
acidosis, basal-ganglia MRI abnormalities, coma and lethargy during
ketoacidotic episodes, tachypnea during crises, failure to thrive,
hepatomegaly, psychomotor delay, and seizures.

The biochemical signature is broad and well aligned with ACAT1 disease:
increased C5-OH and C5:1 acylcarnitines, tiglylcarnitine, urinary
tiglylglycine, 2-methylacetoacetic acid, 3-hydroxybutyric acid,
3-hydroxy-3-methylglutaric acid, acetoacetate, and ketones, with variable
glycine, carnitine, ammonia, glucose, and anion-gap rows. The cached treatment
rows list fasting avoidance, sick-day management, protein-defined diet, and
isoleucine restriction.

## DisMech phenotype coverage

`Beta-Ketothiolase_Deficiency.yaml` is the correct local target. It covers
biallelic ACAT1 disease, impaired isoleucine catabolism, impaired ketone-body
metabolism, isoleucine-derived organic acid accumulation, episodic metabolic
decompensation, acute ketoacidotic crisis syndrome, variable glycemic response,
basal-ganglia and neurologic complications, the major organic-acid and
acylcarnitine markers, catabolic-trigger avoidance, dietary management,
acute dextrose therapy, carnitine supplementation, newborn screening, and
genetic counseling.

## Concordance and completeness

Judgement: correct mapping with high concordance.

IEMbase and DisMech agree on ACAT1 identity, autosomal recessive inheritance,
the crisis phenotype, basal-ganglia involvement, ketone and isoleucine-derived
organic-acid markers, and nutritional prevention. DisMech is richer for
mechanistic chain, crisis management, newborn-screening caveats, and prognosis.
IEMbase adds useful specimen-level prompts, especially globus-pallidus T2 MRI
wording and granular C5-OH/C5:1/ketone rows.

## Curation actions

- Keep the mapping to `Beta-Ketothiolase_Deficiency.yaml`.
- Use IEMbase's globus-pallidus MRI and specimen-specific analyte rows as
  enrichment prompts if the local entry is expanded.
- Treat the IEMbase enzyme-activity row as ACAT1/T2 activity context, not as a
  methionine-cycle MAT finding.

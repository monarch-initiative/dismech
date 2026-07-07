# IEMbase 0062: HMGCL-related HMG-CoA lyase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 62 |
| Nosology | 4.3.16.01 |
| Gene | HMGCL |
| External IDs | OMIM:246450 |
| Generated mapping | MAPPED by `alias_exact:hmgcld` |
| Candidate DisMech targets | `3-Hydroxy-3-Methylglutaric_Aciduria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive HMGCL-related
3-hydroxy-3-methylglutaryl-CoA lyase deficiency, with alternate labels
hydroxymethylglutaric aciduria and HMGCLD. Treatability is marked yes.

The biochemical signal includes high C5-OH and C6DC acylcarnitines in dried
blood spot or plasma, low-normal free carnitine, very low fibroblast HMGCL
activity, normal-high transaminases, low plasma ketones, normal-high urinary
ketones/acetoacetate/3-hydroxybutyrate, normal-high free fatty acids, high
urinary 3-hydroxy-3-methylglutaric acid, 3-hydroxyisovaleric acid,
3-methylglutaconic acid, and 3-methylglutaric acid, normal-high dicarboxylic
acids, possible hyperammonemia, low-normal glucose, and normal-high lactate.

The characteristic clinical signal includes coma during ketoacidotic episodes,
hypoketotic hypoglycemia, and lethargy during crisis. Additional features
include dilated cardiomyopathy, cerebellar white-matter abnormalities, cerebral
infarction, hepatomegaly, neonatal seizures, pancreatitis, seizures, and
stroke-like encephalopathy. Treatments are avoidance of fasting,
protein-defined diet, and sick-day management.

## DisMech phenotype coverage

The generated mapping to `3-Hydroxy-3-Methylglutaric_Aciduria.yaml` is correct.
DisMech models HMGCLD as a disorder of both ketogenesis and leucine degradation
caused by biallelic HMGCL variants. It covers failure of ketone-body production
during fasting, leucine-derived organic-acid accumulation, hypoketotic or
nonketotic hypoglycemia, metabolic acidosis, hyperammonemia, lethargy, vomiting,
seizures, leukoencephalopathy, hepatomegaly, cerebral atrophy, cardiomyopathy,
and acute liver failure.

DisMech also covers the diagnostic urinary organic-acid pattern, C5-OH
acylcarnitine, ketone-body deficiency, secondary hyperammonemia through
acetyl-CoA/N-acetylglutamate biology, HMG-mediated neurotoxicity, and treatments
including protein/leucine restriction, fasting avoidance, carnitine, exogenous
ketone therapy, acute decompensation management, newborn screening, genetic
counseling, and carglumic acid for hyperammonemia.

## Concordance and completeness

Judgement: correct mapping and high concordance.

IEMbase adds granular panel detail for C6DC acylcarnitine, fibroblast enzyme
activity, urinary ketone subfractions, free fatty acids, dicarboxylic acids,
cerebellar white-matter abnormalities, cerebral infarction, pancreatitis, and
stroke-like encephalopathy. DisMech is stronger for the dual ketogenesis/leucine
mechanism, secondary hyperammonemia, organic-acid neurotoxicity, and management
mechanisms.

## Curation actions

- Keep the generated mapping to `3-Hydroxy-3-Methylglutaric_Aciduria.yaml`.
- Consider whether C6DC and crisis-specific neuroimaging features should be
  added later as diagnostic/phenotype refinements.
- Do not use HMGCLD as a generic sink for AUH/MGA1 or OPA3/MGA3 records; those
  are distinct methylglutaconic aciduria disorders.

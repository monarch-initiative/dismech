# IEMbase 0069: MMUT-related methylmalonic aciduria due to methylmalonyl-CoA mutase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 69 |
| Nosology | 1.2.21.01 |
| Gene | MMUT |
| External IDs | OMIM:251000 |
| Generated mapping | MAPPED by `alias_exact:mma` |
| Candidate DisMech targets | `Methylmalonic_Acidemia.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive MMUT-related methylmalonic
aciduria due to methylmalonyl-CoA mutase deficiency, abbreviated MMA.
Treatability is marked yes.

The characteristic biochemical signal includes high methylmalonic acid in plasma
and urine, high C3 propionylcarnitine in blood or plasma, high C4-DC
methylmalonylcarnitine in dried blood spot or urine, high urinary
3-hydroxypropionic acid and methylcitric acid, high glycine in plasma or urine,
high urinary lactate, and low fibroblast methylmalonyl-CoA mutase activity.
Additional rows include fibroblast 14C-propionate incorporation, ammonia, anion
gap, carnitine, glucose, glutamine, ketones, lactate, and MRS
N-acetyl-aspartate.

Characteristic clinical rows include ketoacidotic coma, infection-triggered
acute encephalopathy, feeding difficulty, axial hypotonia, lethargy during
ketoacidotic episodes, progressive renal impairment, psychomotor delay, and
reduced glomerular filtration rate. Additional rows include anemia, ataxia,
basal ganglia MRI abnormalities and lesions, brain edema, cardiomyopathy,
cerebral atrophy, delayed myelination, dystonia, choreoathetosis,
extrapyramidal signs, failure to thrive, hepatomegaly, hyperglycemia,
hypothermia during crisis, metabolic acidosis, metabolic stroke, neonatal
seizures, neutropenia, optic neuropathy, osteopenia, pancreatitis, renal
tubulopathy, respiratory insufficiency, seizures, thrombocytopenia,
tubulointerstitial nephritis, vomiting, and white-matter MRI changes.

Treatment rows include avoidance of fasting, carnitine, protein-defined diet,
sick-day management, antibiotics, hemodialysis, liver and/or kidney
transplantation, carglumic acid, peritoneal dialysis, and sodium benzoate.

## DisMech phenotype coverage

The generated mapping to `Methylmalonic_Acidemia.yaml` is correct. DisMech
models methylmalonic acidemia as an autosomal recessive inborn error of
propionate metabolism caused by MMUT deficiency or by adenosylcobalamin
cofactor-handling defects. It has explicit MMUT genetic coverage, including
mut0 and mut- variant classes.

DisMech covers methylmalonyl-CoA mutase deficiency, methylmalonyl-CoA to
succinyl-CoA block, methylmalonic acid, propionyl-CoA and 2-methylcitrate
accumulation, mitochondrial dysfunction, metabolic decompensation,
hyperammonemia, chronic kidney disease, neurological injury including basal
ganglia injury, cardiomyopathy, lipodystrophy-like disease, elevated C3,
newborn screening, and biomarkers such as FGF21, GDF15, and LCN2.

Treatment coverage includes protein-restricted diet, hydroxocobalamin for
responsive genotypes, carnitine supplementation, acute decompensation
management, liver or combined liver-kidney transplantation, genetic counseling,
and investigational MMUT mRNA therapy.

## Concordance and completeness

Judgement: correct mapping and high concordance.

IEMbase is specifically MMUT/mutase deficiency, while DisMech covers isolated
MMA as an umbrella with explicit MMUT, MMAA, and MMAB genetic sections. This is
appropriate because the local entry models the broader isolated MMA disease
spectrum and already contains the MMUT-specific mechanism.

IEMbase adds granular rows for fibroblast mutase activity, 14C-propionate
incorporation, C4-DC methylmalonylcarnitine compartments, reduced GFR,
tubulointerstitial nephritis, renal tubulopathy, crisis hypothermia,
respiratory insufficiency, delayed myelination, and selected blood-count
abnormalities. DisMech is stronger for disease mechanism, renal and cardiac
pathophysiology, treatment rationale, trial context, and subtype framing.

## Curation actions

- Keep the generated mapping to `Methylmalonic_Acidemia.yaml`.
- No separate MMUT-only file is needed unless future curation policy splits
  mut0/mut- from other isolated MMA subtypes.
- Consider IEMbase's enzyme-assay and renal-feature rows as future diagnostic
  and phenotype enrichments.

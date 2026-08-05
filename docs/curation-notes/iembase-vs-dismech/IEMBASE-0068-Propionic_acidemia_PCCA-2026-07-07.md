# IEMbase 0068: PCCA-related propionic acidemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 68 |
| Nosology | 1.2.18.01 |
| Gene | PCCA |
| External IDs | OMIM:232000 |
| Generated mapping | MAPPED by `alias_exact:propionic acidemia` |
| Candidate DisMech targets | `Propionic_Acidemia.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive PCCA-related propionic acidemia
(PAA). Treatability is marked yes, with a reported prevalence of 1:100,000.

The characteristic biochemical signal includes high C3 propionylcarnitine in
blood or plasma, increased C3/C0, C3/C2, and C3/C4DC acylcarnitine ratios,
high urinary 3-hydroxypropionic acid, methylcitric acid, propionylglycine, and
tiglylglycine, elevated glycine in plasma, urine, or CSF, high urinary lactate,
high MRS glutamine/glutamate ratio, and low propionyl-CoA carboxylase activity
in fibroblasts or white blood cells. Broader rows include ammonia, anion gap,
glucose, ketones, plasma lactate, and carnitine.

Characteristic clinical rows include ketoacidotic coma, infection-triggered
acute encephalopathy, feeding difficulty, axial hypotonia, ketoacidosis,
lethargy during ketoacidotic episodes, metabolic acidosis, psychomotor delay,
and thrombocytopenia. Additional clinical rows include anemia, arrhythmia,
ataxia, basal ganglia MRI abnormalities and lesions, brain edema,
cardiomyopathy including dilated cardiomyopathy, cerebral atrophy, delayed
myelination, dystonia, choreoathetosis, extrapyramidal signs, failure to
thrive, sensorineural hearing loss, hepatomegaly, hypoglycemia, liver
dysfunction, metabolic stroke, neonatal seizures, neutropenia, optic atrophy,
osteopenia, pancreatitis, prolonged QT interval, chronic renal failure,
respiratory insufficiency, seizures, vomiting, and white-matter MRI changes.

The treatment rows are avoidance of fasting, carnitine, protein-defined diet,
sick-day management, antibiotics, hemodialysis, liver and/or kidney
transplantation, carglumic acid, peritoneal dialysis, and sodium benzoate.

## DisMech phenotype coverage

The generated mapping to `Propionic_Acidemia.yaml` is correct. DisMech models
propionic acidemia as an autosomal recessive organic acidemia caused by
deficient propionyl-CoA carboxylase due to PCCA or PCCB pathogenic variants.

DisMech covers the PCCA and PCCB genetic bases, propionyl-CoA carboxylase
deficiency, toxic propionyl-CoA-derived metabolite burden, metabolic acidosis,
hyperammonemia, secondary NAG deficiency, cardiac oxidative stress, renal
mitochondrial quality-control impairment, dilated cardiomyopathy, prolonged QT,
intellectual disability, autism spectrum disorder, seizures, basal ganglia
necrosis, pancreatitis, chronic kidney disease, optic atrophy, hearing
impairment, rhabdomyolysis, C3 propionylcarnitine, 3-hydroxypropionate,
propionylglycine, 2-methylcitrate, tiglylglycine, glycine, lactic acid, FGF21,
GDF15, and newborn screening.

Treatment coverage is also strong: protein-restricted diet, carnitine,
carglumic acid, ammonia-lowering therapy, acute decompensation management, liver
transplantation, cardiac pharmacotherapy, genetic counseling, and newborn
screening.

## Concordance and completeness

Judgement: correct mapping and high concordance.

IEMbase is gene-specific for PCCA, whereas DisMech appropriately covers the
PCCA/PCCB disease spectrum in one propionic acidemia entry and includes a
PCCA-specific genetic block. IEMbase adds granular rows for fibroblast and white
blood cell enzyme testing, acylcarnitine ratios, ketoacidotic coma/lethargy,
comb-like rhythm, hemophagocytosis, female hypergonadotropic hypogonadism,
myelodysplasia, low body temperature during crisis, transient renal impairment,
brain edema, delayed myelination, and respiratory insufficiency.

DisMech is stronger for causal mechanism, secondary hyperammonemia, cardiac and
renal pathophysiology, treatment rationale, and evidence grounding.

## Curation actions

- Keep the generated mapping to `Propionic_Acidemia.yaml`.
- No separate PCCA-only disorder file is needed; the current disease-level entry
  already covers PCCA and PCCB genetic forms.
- Consider IEMbase's enzyme-compartment rows and selected neurologic/imaging
  features as future completeness enrichments.

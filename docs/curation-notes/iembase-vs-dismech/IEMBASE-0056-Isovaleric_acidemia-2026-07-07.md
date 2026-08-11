# IEMbase 0056: IVD-related isovaleric acidemia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 56 |
| Nosology | 1.2.07.01 |
| Gene | IVD |
| External IDs | OMIM:243500 |
| Generated mapping | MAPPED by `alias_exact:isovaleric acidemia` |
| Candidate DisMech targets | `Isovaleric_Acidemia.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive IVD-related isovaleryl-CoA
dehydrogenase deficiency, with alternate labels "Isovaleric acidemia" and
"IVA". Treatability is marked yes and the listed prevalence range is
1:100,000-9:100,000.

The biochemical signal includes high urinary isovalerylglycine, high blood or
plasma C5 acylcarnitine and C5 isovalerylcarnitine, high C5/C2 ratio, high
esterified carnitine, low free carnitine, low fibroblast IVD activity, high
urinary 3-hydroxyisovaleric acid, high plasma isovaleric acid, and possible
hyperammonemia, positive anion gap, low calcium or glucose, and increased
lactate or uric acid. The clinical signal emphasizes coma during ketoacidotic
episodes, acute encephalopathic crisis, feeding difficulty, lethargy,
sweaty-feet odor, and episodic vomiting, with additional cytopenias, seizures,
hypotonia, hepatomegaly, hypoglycemia, metabolic acidosis, pancreatitis, globus
pallidus abnormalities, and white-matter changes.

IEMbase treatments are avoidance of fasting, carnitine, protein-defined diet,
sick-day management, and N-carbamyl-L-glutamate/carglumic acid.

## DisMech phenotype coverage

The generated mapping to `Isovaleric_Acidemia.yaml` is correct. DisMech models
IVA as an autosomal recessive leucine-catabolism disorder caused by IVD
deficiency, with accumulation of isovaleric acid, 3-hydroxyisovaleric acid,
isovalerylcarnitine C5, and isovalerylglycine.

DisMech covers the core severe neonatal crisis phenotype and attenuated
newborn-screening phenotype, including ketoacidosis, metabolic acidosis,
hyperammonemia, encephalopathy, vomiting, lethargy, seizures, intellectual
disability risk, growth impairment, characteristic odor, secondary carnitine
depletion, and pancytopenia. It also models secondary hyperammonemia through
NAGS inhibition by isovaleryl-CoA and includes leucine/protein restriction,
carnitine, glycine, carglumic acid, and acute catabolic-episode management.

## Concordance and completeness

Judgement: correct mapping and high concordance.

IEMbase adds useful diagnostic-panel granularity, especially C5/C2 ratio,
compartment-specific free and esterified carnitine values, fibroblast enzyme
activity, MRS lactate/N-acetylaspartate ratio, calcium, and selected imaging
and hematologic features. DisMech is stronger for mechanistic explanation,
detoxification through carnitine and glycine conjugation, secondary
hyperammonemia, and treatment rationale.

## Curation actions

- Keep the generated mapping to `Isovaleric_Acidemia.yaml`.
- Preserve C5-isomer caution when comparing IVA to ACADSB/SBCADD records; C5
  alone is not disease-specific without follow-up testing.
- Consider IEMbase's globus pallidus, white-matter, and ratio-marker details as
  possible future diagnostic or phenotype enrichments.

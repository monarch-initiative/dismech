# IEMbase 0177: MLYCD-related malonic aciduria

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 177 |
| Nosology | 1.2.23.01 |
| Gene | MLYCD |
| External IDs | OMIM:248360; ORPHA:943 |
| Generated mapping | MAPPED to `Migraine_with_Aura.yaml` by alias `MA` |
| Candidate DisMech targets | None valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as MLYCD-related malonyl-CoA decarboxylase
deficiency, with alternate labels malonic aciduria and MA. Treatability is
marked unknown, and there are no treatment rows in the extracted JSON.

The biochemical rows include increased C3-DC malonylcarnitine, increased
urine C4-DC methylmalonylcarnitine, decreased to normal free carnitine,
decreased malonyl-CoA decarboxylase activity, normal to increased plasma and
urinary ketones, increased urinary malonic acid as the characteristic organic
acid, increased to markedly increased malonic acid with additional urinary
organic-acid abnormalities including 3-hydroxybutyric, adipic, ethylmalonic,
fumaric, glutaric, malic, methylmalonic, sebacic, suberic, and succinic acids,
decreased urine methylmalonic-acid/malonic-acid ratio, normal to increased
ammonia, variable base excess, low to normal cholesterol, low to normal
glucose, and normal to increased lactate. Clinical rows include basal ganglia
lesions, cerebellar white matter abnormalities, dystonia, infection-triggered
acute encephalopathy, epilepsy, frontotemporal atrophy, hepatomegaly,
hypoglycemia, axial hypotonia, metabolic acidosis, neonatal seizures,
cardiomyopathy, developmental delay, and vomiting.

## DisMech phenotype coverage

No valid local DisMech target was found. The generated mapping to
`Migraine_with_Aura.yaml` is a false positive caused by the short alias `MA`.
The local migraine entry models cortical spreading depolarization, aura, and
headache biology; it has no MLYCD, malonyl-CoA decarboxylase activity,
malonic aciduria, malonylcarnitine, metabolic acidosis, cardiomyopathy, or
developmental encephalopathy coverage.

Local search found `Combined_Malonic_and_Methylmalonic_Aciduria.yaml`, but that
entry models ACSF3-related CMAMMA, not MLYCD-related isolated malonic
aciduria.

## Concordance and completeness

Judgement: generated mapping is false; this is a true local gap.

IEMbase points to a distinct monogenic malonic aciduria with neurologic,
cardiac, and metabolic decompensation features. The alias `MA` is too broad to
support automated exact matching.

## Curation actions

- Do not map this record to `Migraine_with_Aura.yaml`.
- Add a future MLYCD/malonyl-CoA decarboxylase deficiency entry.
- Treat `MA` as an unsafe short alias in mapping.
- Expected future coverage: MLYCD, reduced malonyl-CoA decarboxylase activity,
  malonic aciduria, malonylcarnitine, low methylmalonic-acid/malonic-acid
  ratio, cardiomyopathy, developmental delay, epilepsy/seizures, basal ganglia
  and white matter changes, metabolic acidosis, hypoglycemia, hepatomegaly,
  and infection-triggered encephalopathy.

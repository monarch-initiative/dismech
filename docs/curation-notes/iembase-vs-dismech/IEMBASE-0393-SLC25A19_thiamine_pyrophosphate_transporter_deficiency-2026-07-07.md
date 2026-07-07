# IEMbase 0393: SLC25A19-related Mitochondrial thiamine pyrophosphate transporter deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 393 |
| Nosology | 21.2.04.01 |
| Gene | SLC25A19 |
| External IDs | OMIM:606521; ORPHA:99742 |
| Generated mapping | UNMAPPED; low candidate `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SLC25A19-related mitochondrial thiamine
pyrophosphate transporter deficiency, also listed as mitochondrial thiamine
pyrophosphate carrier deficiency, Amish microcephaly, and bilateral striatal
necrosis.

Characteristic clinical rows include basal ganglia MRI lesions, dystonia,
infection-precipitated acute encephalopathy, and polyneuropathy. Biochemical
rows include normal-to-increased CSF lactate and increased urinary
2-ketoglutaric acid. The treatment row lists thiamine.

## DisMech phenotype coverage

There is no exact local DisMech target for SLC25A19 deficiency. The generated
`Glycogen_Storage_Disease_Type_I.yaml` candidate is a false positive: GSD I
models G6PC1/SLC37A4 glucose-6-phosphatase-system disease with fasting
hypoglycemia, hepatomegaly, nephromegaly, lactic acidosis, hyperlipidemia, and
hyperuricemia, not mitochondrial thiamine pyrophosphate transport.

`Biotin_Thiamine_Responsive_Basal_Ganglia_Disease.yaml` is better
pathway/phenotype context than GSD I because both disorders involve thiamine
biology and basal ganglia injury, but it is SLC19A3 transporter disease and is
not an exact SLC25A19 target.

## Concordance and completeness

Judgement: true SLC25A19 local gap; reject the GSD I candidate.

The IEMbase record is a mitochondrial thiamine pyrophosphate carrier disorder
with basal-ganglia/striatal necrosis and infection-triggered encephalopathy.
The generated candidate differs in gene, organellar compartment, pathway, and
phenotype.

## Curation actions

- Keep this record unmapped until an SLC25A19 thiamine pyrophosphate transporter
  deficiency target exists.
- Do not map to `Glycogen_Storage_Disease_Type_I.yaml`.
- Use SLC19A3/BTBGD only as differential thiamine/basal-ganglia context.
- If curated, include Amish microcephaly/bilateral striatal necrosis naming,
  CSF lactate, urinary 2-ketoglutaric acid, dystonia, polyneuropathy,
  infection-triggered encephalopathy, and thiamine treatment prompts.

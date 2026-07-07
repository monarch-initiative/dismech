# IEMbase 0490: PYGL-related liver glycogen phosphorylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 490 |
| Nosology | 3.4.09.01 |
| Gene | PYGL |
| External IDs | OMIM:232700; ORPHA:369 |
| Generated mapping | CANDIDATE; MEDIUM; `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | `Glycogen_Storage_Disease_Type_I.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive PYGL-related liver glycogen
phosphorylase deficiency as glycogen storage disease type VI / Hers disease.
No treatments are listed. Biochemical rows include normal-to-increased
ASAT/ALAT and biotinidase, decreased liver glycogen phosphorylase, increased
fasted plasma and urine ketones, normal-to-markedly increased liver glycogen,
normal-to-increased cholesterol, low-to-normal fasting plasma glucose, normal
fasting plasma and urine lactate, increased triglycerides, and normal plasma and
urine uric acid. The listed clinical row is doll-like facial adiposity.

## DisMech phenotype coverage

`Glycogen_Storage_Disease_Type_I.yaml` is not the correct target. It covers GSD
I due to G6PC1/SLC37A4 glucose-6-phosphatase system defects and explicitly
models lactic acidosis, hyperuricemia, and the GSD Ia/Ib subtype structure. It
does not model PYGL, hepatic glycogen phosphorylase deficiency, Hers disease,
or the normal lactate/normal uric-acid profile that distinguishes GSD VI from
classic GSD I.

## Concordance and completeness

Judgement: false-positive candidate; true PYGL/Hers disease local gap.

Both IEMbase and the candidate DisMech file concern hepatic glycogen storage
and fasting hypoglycemia, but the mechanism and biochemical profile differ.
IEMbase points to liver phosphorylase deficiency with ketotic fasting
hypoglycemia, preserved lactate, preserved uric acid, and mild hepatic lipid /
transaminase changes. The GSD I file represents a different final common
pathway in glucose release and should not be treated as coverage.

## Curation actions

- Do not map this record to `Glycogen_Storage_Disease_Type_I.yaml`.
- Track PYGL-related Hers disease / GSD VI as a local curation gap.
- Preserve IEMbase prompts for normal lactate, normal uric acid, liver
  phosphorylase activity, liver glycogen, ketones, biotinidase, and doll-like
  adiposity for a future exact entry.

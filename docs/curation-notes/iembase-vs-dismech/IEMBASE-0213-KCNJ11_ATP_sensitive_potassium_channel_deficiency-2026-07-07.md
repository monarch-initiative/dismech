# IEMbase 0213: KCNJ11-related ATP-sensitive potassium channel pore-forming subunit deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 213 |
| Nosology | 24.1.03.01 |
| Gene | KCNJ11 |
| External IDs | OMIM:601820; ORPHA:99886 |
| Generated mapping | UNMAPPED; best candidate `Congenital_Isolated_Hyperinsulinism.yaml` |
| Candidate DisMech targets | `Congenital_Isolated_Hyperinsulinism.yaml#KATP-HI Diffuse`; KCNJ11/HHF2 gene section |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as KCNJ11-related ATP-sensitive potassium channel
pore-forming subunit deficiency, with alternate labels persistent
hyperinsulinemic hypoglycemia of infancy, hyperinsulinism of infancy 2, and
HHF2. The record is autosomal recessive and treatability is marked yes.

The biochemical rows capture the congenital hyperinsulinism pattern: low
plasma glucose, high insulin during hypoglycemia, suppressed free fatty acids,
and suppressed ketones during hypoglycemia. Characteristic clinical rows include
hyperinsulinism, hypoketotic hypoglycemia, and convulsions, with additional
rows for macrosomia and possible later diabetes. Treatments listed by IEMbase
include diazoxide, glucagon, glucose infusion, high-carbohydrate feeding,
lanreotide or octreotide, and nifedipine.

## DisMech phenotype coverage

`Congenital_Isolated_Hyperinsulinism.yaml` is the correct local target despite
the generated UNMAPPED status. The entry explicitly covers ABCC8/KCNJ11
K-ATP-channel disease, diffuse and focal KATP hyperinsulinism subtypes,
KCNJ11 variants as HHF2, unregulated beta-cell depolarization and insulin
secretion, hyperinsulinemic hypoglycemia, suppressed ketogenesis, seizures,
neurodevelopmental risk, macrosomia, maturity-onset diabetes in relevant
subtypes, diazoxide, octreotide/lanreotide, glucose support, and surgical
management for focal/diffuse disease.

## Concordance and completeness

Judgement: generated false negative; resolve to
`Congenital_Isolated_Hyperinsulinism.yaml`, preferably the KATP/HHF2 coverage.

IEMbase and DisMech agree on KCNJ11 as the ATP-sensitive potassium-channel pore
subunit, hyperinsulinemic hypoglycemia, suppressed ketones and fatty acids,
seizure risk, macrosomia, possible later diabetes, and several acute/chronic
treatments. DisMech is richer for the causal beta-cell membrane-depolarization
mechanism, K-ATP channel biology, focal versus diffuse histology, and surgery.

## Curation actions

- Correct the generated UNMAPPED status to local coverage in
  `Congenital_Isolated_Hyperinsulinism.yaml`.
- Prefer subtype resolution to KATP hyperinsulinism/HHF2 rather than a generic
  congenital hyperinsulinism-only match.
- No new standalone KCNJ11 disease file is needed unless the project later
  chooses to split every congenital hyperinsulinism gene subtype into a separate
  disorder.

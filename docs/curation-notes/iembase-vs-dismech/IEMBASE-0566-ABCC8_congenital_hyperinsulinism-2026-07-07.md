# IEMbase 0566: ABCC8-related congenital hyperinsulinism

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 566 |
| Nosology | 24.1.01.01 |
| Gene | ABCC8 |
| External IDs | OMIM:256450; ORPHA:99886 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Congenital_Isolated_Hyperinsulinism.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ABCC8-related ATP-sensitive potassium channel regulatory
subunit deficiency, with alternate label persistent hyperinsulinemic
hypoglycemia of infancy and abbreviation HHF1. The record lists autosomal
dominant and autosomal recessive inheritance, diffuse and focal form subtype,
treatability yes, and no treatment rows.

Biochemical rows include very low serum free fatty acids during hypoglycemia,
very low ketones during hypoglycemia, low plasma glucose, and high insulin
during hypoglycemia. Clinical rows include optional diabetes or diabetes
mellitus, macrosomia, convulsions, hyperinsulinism, and hypoketotic
hypoglycemia.

## DisMech phenotype coverage

`Congenital_Isolated_Hyperinsulinism.yaml` is the correct local target. It
models congenital isolated hyperinsulinism as dysregulated glucose-independent
insulin secretion from pancreatic beta cells. The entry explicitly includes
diffuse and focal KATP hyperinsulinism caused by ABCC8 or KCNJ11, ABCC8/SUR1
as the K-ATP channel regulatory subunit, dominant and recessive forms,
unregulated beta-cell depolarization, inappropriate insulin secretion,
hyperinsulinemic hypoglycemia, suppressed ketogenesis, seizures, macrosomia,
and genotype-sensitive treatment such as diazoxide or surgery.

## Concordance and completeness

Judgement: generated false negative; resolve to
`Congenital_Isolated_Hyperinsulinism.yaml#KATP-HI/ABCC8`.

IEMbase and DisMech agree on ABCC8 identity, K-ATP channel biology, dominant
and recessive inheritance, diffuse and focal forms, hyperinsulinism, low
glucose, hypoketotic hypoglycemia, suppressed free fatty acids and ketones,
macrosomia, and convulsions/seizures. DisMech is stronger for the beta-cell
depolarization and treatment mechanism.

IEMbase adds a useful HHF1-specific source row set and should be reconciled
with the broader local ABCC8/KCNJ11 KATP-HI subtype.

## Curation actions

- Promote the IEMbase match to `Congenital_Isolated_Hyperinsulinism.yaml`,
  specifically the ABCC8/HHF1 KATP-HI branch.
- Verify that PHHI and HHF1 aliases are visible enough for future matcher
  runs.
- Review IEMbase diabetes, free-fatty-acid, ketone, glucose, insulin,
  macrosomia, and treatment-scope prompts before importing phenotype detail.

# IEMbase 0568: GCK-related glucokinase hyperinsulinism

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 568 |
| Nosology | 3.3.05.01 |
| Gene | GCK |
| External IDs | OMIM:602485; ORPHA:99885 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Congenital_Isolated_Hyperinsulinism.yaml#GCK-HI`; `Diabetes_Mellitus.yaml` as monogenic diabetes context |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GCK-related glucokinase superactivity, with alternate labels
familial hyperinsulinemic hypoglycemia and HHF3. The record is autosomal
dominant, idiopathic subtype, of unknown treatability, and has no treatment
rows. The IEMbase alternate-name field also includes a MODY label, which should
be source-reviewed because activating GCK disease is the hypoglycemic branch
whereas other GCK variant classes sit in monogenic diabetes.

Biochemical rows include decreased serum free fatty acids, decreased ketones
during hypoglycemia, very low to low plasma glucose, and increased plasma
insulin. Clinical and characteristic rows include diabetes mellitus type 2,
epilepsy, hypoglycemia, intellectual disability, hyperinsulinism, and
hypoketotic hypoglycemia.

## DisMech phenotype coverage

`Congenital_Isolated_Hyperinsulinism.yaml` contains an explicit GCK-HI subtype:
dominant activating glucokinase variants lower the beta-cell glucose threshold
for insulin secretion, producing hyperinsulinemic hypoglycemia of variable
severity. `Diabetes_Mellitus.yaml` also contains GCK under the monogenic
diabetes spectrum, but that broader diabetes context is not the best target for
the hyperinsulinemic GCK superactivity record.

## Concordance and completeness

Judgement: generated false negative; resolve the hyperinsulinism aspect to
`Congenital_Isolated_Hyperinsulinism.yaml#GCK-HI`.

IEMbase and DisMech agree on GCK identity, dominant inheritance, hyperinsulinism,
low glucose, suppressed ketones/free fatty acids, and inappropriate insulin
secretion. DisMech is stronger for the glucose-sensor threshold mechanism.
IEMbase is more explicit about epilepsy, intellectual disability, type 2
diabetes wording, and compartment-specific biochemical rows.

## Curation actions

- Promote this record to `Congenital_Isolated_Hyperinsulinism.yaml#GCK-HI`.
- Keep `Diabetes_Mellitus.yaml` only as monogenic-diabetes context, not as the
  primary mapping for GCK superactivity.
- Review the IEMbase MODY/type 2 diabetes wording against GCK activating versus
  inactivating variant mechanisms before importing aliases or phenotypes.

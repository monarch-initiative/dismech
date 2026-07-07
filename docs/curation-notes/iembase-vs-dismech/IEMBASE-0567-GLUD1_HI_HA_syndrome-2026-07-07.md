# IEMbase 0567: GLUD1-related hyperinsulinism-hyperammonemia syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 567 |
| Nosology | 1.1.01.02 |
| Gene | GLUD1 |
| External IDs | OMIM:606762; ORPHA:35878 |
| Generated mapping | MAPPED; `Congenital_Isolated_Hyperinsulinism.yaml#HI/HA Syndrome` |
| Candidate DisMech targets | `Congenital_Isolated_Hyperinsulinism.yaml#HI/HA Syndrome` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GLUD1-related glutamate dehydrogenase superactivity, with
alternate labels hyperinsulinism-hyperammonemia syndrome and familial
hyperinsulinemic hypoglycemia type 6. The record is autosomal dominant,
idiopathic subtype, treatable, and lists diazoxide as a treatment.

Biochemical rows include decreased serum free fatty acids, decreased plasma and
urinary ketones, normal-to-increased urinary 2-ketoglutaric acid, increased
fasting ammonia, low plasma glucose, and increased plasma insulin. Clinical and
characteristic rows include convulsions, abnormal EEG, intellectual disability,
seizures, generalized epilepsy, hyperinsulinism, hypoglycemia, hypoketotic
hypoglycemia, and leucine sensitivity causing hypoglycemia.

## DisMech phenotype coverage

`Congenital_Isolated_Hyperinsulinism.yaml#HI/HA Syndrome` is the correct local
target. The local subtype explicitly models dominant activating GLUD1 variants,
glutamate dehydrogenase dysregulation, leucine/protein-sensitive hypoglycemia,
persistent hyperammonemia, increased insulin secretion through beta-cell
metabolic signaling, neurologic sequelae from hypoglycemia, and typical
diazoxide responsiveness.

## Concordance and completeness

Judgement: correct high-concordance subtype mapping to
`Congenital_Isolated_Hyperinsulinism.yaml#HI/HA Syndrome`.

IEMbase and DisMech agree on GLUD1 identity, dominant inheritance, HI/HA scope,
GDH superactivity, leucine sensitivity, hyperammonemia, hyperinsulinism,
hypoketotic hypoglycemia, seizures/epilepsy, and diazoxide relevance. DisMech
is stronger for the amino-acid-driven beta-cell mechanism and the convergence
on insulin secretion.

IEMbase adds useful prompts for 2-ketoglutaric acid, EEG abnormality,
generalized epilepsy, intellectual disability, and compartment-specific free
fatty acid and ketone suppression.

## Curation actions

- Keep this record mapped to `Congenital_Isolated_Hyperinsulinism.yaml#HI/HA
  Syndrome`.
- Consider reviewing IEMbase 2-ketoglutaric acid, EEG, generalized epilepsy,
  intellectual-disability, and compartment-specific ketone/free-fatty-acid rows
  for possible future phenotype or biochemical additions.
- Preserve GLUD1/HHF6 aliases for matcher visibility.

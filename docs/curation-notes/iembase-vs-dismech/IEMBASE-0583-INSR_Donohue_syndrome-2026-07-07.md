# IEMbase 0583: INSR-related insulin receptor dysregulation, Donohue syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 583 |
| Nosology | 24.1.11.01 |
| Gene | INSR |
| External IDs | OMIM:609968; ORPHA:769 |
| Generated mapping | UNMAPPED; best candidate `IPEX_Syndrome.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents INSR-related insulin receptor dysregulation / Donohue
syndrome, with alternate label familial hyperinsulinemic hypoglycemia type 5
/ HHF5. The record is classified under disorders of insulin metabolism, lists
autosomal dominant inheritance, has unknown treatability, and has no treatment
rows.

Biochemical rows include decreased serum free fatty acids, decreased plasma or
urinary ketones during hypoglycemia, decreased plasma glucose, and increased
insulin during hypoglycemia. Clinical rows include hyperinsulinism and
hyperpigmentation.

## DisMech phenotype coverage

`IPEX_Syndrome.yaml` is a false-positive candidate. IPEX models FOXP3-related
immune dysregulation with enteropathy, endocrinopathy, and eczema; it does not
represent INSR, severe insulin receptoropathy, hyperinsulinemic hypoglycemia,
suppressed ketogenesis, or free-fatty-acid suppression.

The local knowledge base has broad insulin-resistance, diabetes, and congenital
hyperinsulinism context, and Donohue syndrome appears only as differential
context elsewhere. No exact INSR/Donohue syndrome target was identified.

## Concordance and completeness

Judgement: true local gap; reject IPEX syndrome as an exact mapping.

The IEMbase record is a receptor-signaling disorder centered on insulin action,
hyperinsulinemia, hypoglycemia, suppressed ketone/free-fatty-acid physiology,
and hyperpigmentation. It should not be merged into immune dysregulation or
generic hyperinsulinism without preserving the INSR mechanism.

The IEMbase inheritance field should be source-reviewed during import because
severe Donohue syndrome is commonly curated as a biallelic insulin-receptor
disorder.

## Curation actions

- Create or identify an exact INSR severe insulin-receptoropathy / Donohue
  syndrome target before import.
- Reject `IPEX_Syndrome.yaml` as an exact mapping.
- Preserve the IEMbase hypoglycemia, high insulin, suppressed ketones,
  decreased free-fatty-acid, and hyperpigmentation prompts.
- Source-review the IEMbase inheritance assertion before promoting it into
  DisMech.

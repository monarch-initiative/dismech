# IEMbase 0580: MTHFS-related 5,10-methenyltetrahydrofolate synthetase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 580 |
| Nosology | 21.8.07.01 |
| Gene | MTHFS |
| External IDs | OMIM:604197 |
| Generated mapping | UNMAPPED; best candidate `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents MTHFS-related 5,10-methenyltetrahydrofolate synthetase
deficiency, with alternate label 5-formyltetrahydrofolate cycloligase. The
record is autosomal recessive, classified under disorders of folate metabolism,
has unknown treatability, and lists 5-methyltetrahydrofolate plus
methylcobalamin.

The characteristic biochemical row is very decreased CSF 5-MTHF. Clinical rows
include feeding difficulties, hyperthermia, intellectual disability, recurrent
infections, and short stature.

## DisMech phenotype coverage

`Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` is a false-positive
candidate. It models CPS1-related urea-cycle failure with hyperammonemia, low
citrulline, and urea-cycle decompensation rather than MTHFS-related folate
one-carbon metabolism.

The local knowledge base has related folate/remethylation and cerebral-folate
context, but no exact MTHFS / 5-formyltetrahydrofolate cycloligase disease
target was identified.

## Concordance and completeness

Judgement: true local gap; reject CPS1 deficiency as an exact target.

The distinguishing IEMbase signal is a folate-metabolism disorder with low CSF
5-MTHF and folate-directed treatment rows. The generated CPS1 candidate shares
only broad metabolic-disease neighborhood and does not match gene, pathway,
biomarker, or treatment.

## Curation actions

- Create or identify an exact MTHFS deficiency target before import.
- Reject `Carbamoyl_Phosphate_Synthetase_I_Deficiency.yaml` as an exact mapping.
- Preserve the CSF 5-MTHF, folate/cobalamin treatment, recurrent-infection,
  hyperthermia, feeding, growth, and intellectual-disability prompts.

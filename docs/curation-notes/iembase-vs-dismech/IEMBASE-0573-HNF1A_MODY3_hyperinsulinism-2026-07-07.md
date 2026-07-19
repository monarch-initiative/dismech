# IEMbase 0573: HNF1A-related MODY3 with hyperinsulinism

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 573 |
| Nosology | 24.1.06.01 |
| Gene | HNF1A |
| External IDs | OMIM:142410; ORPHA:552 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Congenital_Isolated_Hyperinsulinism.yaml#HNF4A/HNF1A-HI`; `Diabetes_Mellitus.yaml#HNF1A` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents HNF1A-related MODY3. The record is autosomal dominant,
idiopathic subtype, of unknown treatability, and has no treatment rows.

Biochemical rows include decreased free fatty acids during hypoglycemia,
decreased ketones during hypoglycemia, low plasma glucose, and increased
insulin during hypoglycemia. Characteristic rows include MODY3 diabetes,
hyperinsulinism, and hypoketotic hypoglycemia.

## DisMech phenotype coverage

`Congenital_Isolated_Hyperinsulinism.yaml` contains a combined HNF4A/HNF1A
transcription-factor hyperinsulinism subtype, describing hyperinsulinism in the
newborn period followed by MODY later in life. `Diabetes_Mellitus.yaml` includes
HNF1A as a causative monogenic diabetes gene and explicitly notes MODY3 context.
There is no standalone HNF1A/MODY3 disease entry.

## Concordance and completeness

Judgement: generated false negative to local partial coverage; resolve the
hyperinsulinism aspect to
`Congenital_Isolated_Hyperinsulinism.yaml#HNF4A/HNF1A-HI` and the diabetes
aspect to `Diabetes_Mellitus.yaml#HNF1A`.

IEMbase agrees with local CHI context on HNF1A-related hyperinsulinism,
hypoketotic hypoglycemia, low glucose, and suppressed ketone/free-fatty-acid
signals. It agrees with the broad diabetes entry on HNF1A/MODY3 monogenic
diabetes. The missing local content is a standalone HNF1A/MODY3 subtype entry
that unifies both signals.

## Curation actions

- Promote this record to the HNF4A/HNF1A transcription-factor hyperinsulinism
  context in `Congenital_Isolated_Hyperinsulinism.yaml`.
- Retain `Diabetes_Mellitus.yaml#HNF1A` as monogenic-diabetes context.
- Consider a future HNF1A/MODY3-specific entry or subtype if DisMech wants
  gene-specific MODY coverage outside broad diabetes.

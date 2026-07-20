# IEMbase 0072: MTHFR-related 5,10-methylenetetrahydrofolate reductase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 72 |
| Nosology | 21.8.03.01 |
| Gene | MTHFR |
| External IDs | OMIM:236250 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Inborn_Disorder_of_Methionine_Cycle_and_Sulfur_Amino_Acid_Metabolism.yaml#MTHFR deficiency`; also covered in `Homocystinuria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive MTHFR-related
5,10-methylenetetrahydrofolate reductase deficiency, with alternate labels
homocystinuria due to deficiency of MTHFR activity and MTHFR. Treatability is
marked yes.

The characteristic biochemical signal includes abnormal plasma homocysteine and
abnormal CSF 5-methyltetrahydrofolic acid. Additional rows include plasma
methionine and CSF biogenic amine metabolites such as 5-HIAA and HVA.

Characteristic clinical rows include developmental regression and intellectual
disability. Additional rows include apnea, ataxia, psychotic behavior,
behavioral disorder, depression, feeding difficulty, gait disturbance,
hydrocephalus, infantile spasms, microcephaly, muscle weakness, peripheral
neuropathy, ovarian insufficiency, psychiatric disturbance, myoclonic and
tonic-clonic seizures, thromboembolic episodes, and selected endocrine rows.

Treatment rows include betaine, carnitine, folate, and methionine.

## DisMech phenotype coverage

The generated mapping is a false negative rather than a true absence. DisMech
contains local MTHFR coverage in two places:

- `Inborn_Disorder_of_Methionine_Cycle_and_Sulfur_Amino_Acid_Metabolism.yaml`
  has a `MTHFR deficiency` subtype and a `MTHFR Remethylation Deficiency`
  pathophysiology node.
- `Homocystinuria.yaml` contains an explicit MTHFR remethylation pathway
  deficiency branch and an MTHFR genetic block.

Together these cover biallelic MTHFR variants, reduced
methylenetetrahydrofolate reductase activity, abnormal folate-dependent
remethylation, elevated homocysteine, low or low-normal methionine, nonclassical
homocystinuria, autosomal recessive inheritance, and genetic counseling. The
methionine-cycle entry also covers pathway-level diagnosis and betaine-based
remethylation support.

## Concordance and completeness

Judgement: false negative; local subtype/branch coverage exists.

The best canonical mapping depends on desired mapping granularity. If IEMbase
records can map to pathway-group subtypes, use
`Inborn_Disorder_of_Methionine_Cycle_and_Sulfur_Amino_Acid_Metabolism.yaml#MTHFR deficiency`.
If disease-level clinical coverage is preferred, `Homocystinuria.yaml` is the
most detailed local target for MTHFR-deficiency homocystinuria.

IEMbase adds granular neurologic and psychiatric rows, CSF 5-MTHF, CSF biogenic
amine metabolites, carnitine and methionine treatment rows, and endocrine
features that are not central in the local entries. DisMech is stronger for the
remethylation mechanism and shared homocystinuria context.

## Curation actions

- Treat the generated UNMAPPED status as a false negative.
- Prefer a subtype-level mapping to
  `Inborn_Disorder_of_Methionine_Cycle_and_Sulfur_Amino_Acid_Metabolism.yaml#MTHFR deficiency`,
  with `Homocystinuria.yaml` as a detailed secondary local target.
- Consider IEMbase's neurologic, psychiatric, CSF 5-MTHF, and treatment detail
  as future enrichment for the MTHFR branch.

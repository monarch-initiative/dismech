# IEMbase 0091: LMBRD1-related methylmalonic aciduria and homocystinuria, cblF type

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 91 |
| Nosology | 21.9.07.01 |
| Gene | LMBRD1 |
| External IDs | OMIM:277380 |
| Generated mapping | MAPPED to `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblF` |
| Candidate DisMech targets | `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblF` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive LMBRD1-related cblF disease,
with alternate labels lysosomal membrane cobalamin transporter deficiency and
cblF. Treatability is marked yes.

The characteristic clinical rows include megaloblastic anemia, failure to
thrive, life-threatening illness, neurologic dysfunction, and impaired vision.

The biochemical panel matches combined methylmalonic aciduria and
homocystinuria: elevated urinary and plasma methylmalonic acid, urinary
methylcitric acid, urinary 3-hydroxypropionic acid, C3 propionylcarnitine in
blood or plasma, urinary and plasma homocysteine, low-to-normal methionine, and
reduced S-adenosylmethionine in CSF or plasma.

Treatment rows include hydroxocobalamin and betaine.

## DisMech phenotype coverage

The generated mapping is correct. The best local target is
`Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblF`.

DisMech's cblF subtype describes LMBRD1 deficiency as impaired lysosomal export
of cobalamin producing combined methylmalonic acidemia and homocystinuria. The
umbrella pathophysiology explicitly includes LMBRD1 in defective cobalamin
absorption, transport, and cellular uptake, leading to impaired intracellular
cobalamin cofactor synthesis, remethylation failure, and methylmalonyl-CoA
mutase dysfunction.

## Concordance and completeness

Judgement: high concordance at the umbrella subtype level.

The main local gaps are cblF-specific presentation detail and lab-compartment
granularity. IEMbase is more explicit about the cblF clinical row set and
S-adenosylmethionine markers, while DisMech carries stronger generalized
cobalamin-transport mechanism and treatment rationale.

## Curation actions

- Keep the generated mapping to
  `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblF`.
- Consider adding cblF-specific clinical and biochemical notes if the umbrella
  entry is expanded.
- Preserve spelling-normalization handling: the IEMbase name currently contains
  "LMBRD1-relasted" while the intended label is LMBRD1-related.

# IEMbase 0373: PCSK9-related proprotein convertase deficiency with low LDL

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 373 |
| Nosology | 15.1.06.01 |
| Gene | PCSK9 |
| External IDs | OMIM:607786; OMIM:613589; ORPHA:391665 |
| Generated mapping | UNMAPPED; no candidate |
| Candidate DisMech targets | No exact local target; `Familial_Hypercholesterolemia.yaml` is opposite-direction PCSK9 context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PCSK9 loss-of-function with low LDL, also listed as PCSK9
deficiency and hypobetalipoproteinemia due to PCSK9 loss of function.
Inheritance is listed as autosomal recessive.

The cached record is sparse and states no clinical significance. Biochemical
rows include plasma HDL cholesterol, plasma LDL cholesterol, serum
triglyceride, and plasma Apo B. There are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech disease target. `Familial_Hypercholesterolemia.yaml`
has extensive PCSK9 content, but it is centered on gain-of-function PCSK9
causing increased LDLR degradation, elevated LDL-C, and FH. The file also notes
that PCSK9 loss-of-function variants are associated with lower LDL-C and reduced
cardiovascular risk, but that is protective/opposite-direction context rather
than a curated disease mechanism.

General `Hyperlipidemia.yaml` also contains PCSK9 pathway context, again in
lipid-risk and LDL-raising contexts rather than a PCSK9 deficiency disease.

## Concordance and completeness

Judgement: true local gap or scope-review item; do not map this record to
familial hypercholesterolemia.

The IEMbase record is mechanistically opposite to PCSK9 gain-of-function FH:
reduced PCSK9 activity lowers LDLR degradation and lowers LDL. If represented
in DisMech, it should be a PCSK9 loss-of-function hypobetalipoproteinemia or
low-LDL entry, with explicit clinical-significance review.

## Curation actions

- Keep this record unmapped for now.
- Do not map to `Familial_Hypercholesterolemia.yaml` except as pathway context
  for the opposite-direction PCSK9 mechanism.
- Review whether PCSK9 loss-of-function low-LDL states are in project scope,
  given the IEMbase "no clinical significance" signal.
- If curated, create a distinct PCSK9 loss-of-function/low-LDL target rather
  than reusing PCSK9 gain-of-function FH.

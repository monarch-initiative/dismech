# IEMbase 0090: MMACHC-related methylmalonic aciduria and homocystinuria, cblC type

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 90 |
| Nosology | 21.9.09.01 |
| Gene | MMACHC |
| External IDs | OMIM:277400 |
| Generated mapping | MAPPED to `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblC` |
| Candidate DisMech targets | `MMACHC-related_Methylmalonic_Aciduria_and_Homocystinuria_cblC_Type.yaml`; `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblC` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive MMACHC-related cblC disease,
with alternate labels B12-responsive MMA and homocystinuria and cblC.
Treatability is marked yes.

The characteristic clinical rows include megaloblastic anemia, failure to
thrive, life-threatening illness, neurologic dysfunction, and impaired vision.

The biochemical panel includes elevated urinary and plasma methylmalonic acid,
urinary methylcitric acid, urinary 3-hydroxypropionic acid, C3
propionylcarnitine in blood or plasma, urinary and plasma homocysteine,
low-to-normal methionine, and reduced S-adenosylmethionine in CSF or plasma.

Treatment rows include betaine, hydroxycobalamin, and carnitine.

## DisMech phenotype coverage

The generated mapping to the cobalamin umbrella's cblC subtype is biologically
correct, but the best canonical DisMech target is the standalone
`MMACHC-related_Methylmalonic_Aciduria_and_Homocystinuria_cblC_Type.yaml`
entry.

The standalone cblC entry has direct MMACHC pathophysiology, methylcobalamin
and adenosylcobalamin branch failure, homocysteine and methylmalonic acid
accumulation, early- and late-onset subtypes, neurologic and ocular injury,
renal and vascular complications, and hydroxocobalamin plus betaine treatment.
The cobalamin umbrella also covers cblC as a subtype and is useful secondary
context, but it is less specific than the standalone disease file.

## Concordance and completeness

Judgement: correct disease-level coverage with a canonical-target ambiguity.

IEMbase adds some compact panel details, especially S-adenosylmethionine and
C3/3-hydroxypropionate/methylcitric-acid rows. DisMech is richer for mechanism,
genotype, vascular and renal complications, and treatment rationale.

## Curation actions

- Prefer `MMACHC-related_Methylmalonic_Aciduria_and_Homocystinuria_cblC_Type.yaml`
  as the canonical target for this record.
- Keep `Inborn_Disorder_of_Cobalamin_Metabolism_and_Transport.yaml#cblC` as
  umbrella context rather than the primary mapping.
- Consider aligning duplicate cblC coverage so future crosswalks consistently
  prefer the standalone file when a distinct MONDO disease entry exists.

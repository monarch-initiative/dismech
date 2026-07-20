# IEMbase 0532: ETFDH-related myopathic CoQ10 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 532 |
| Nosology | 4.2.08.02 |
| Gene | ETFDH |
| External IDs | OMIM:231675; ORPHA:394529 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml#ETFDH` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents an ETFDH-related myopathic form of CoQ10 deficiency. The
record is autosomal recessive, subtype is marked idiopathic, treatability is
marked unknown, and no treatment rows are listed.

The biochemical rows include normal-to-increased C4-C18 acylcarnitines in dried
blood spot and plasma, low or normal free carnitine, normal-to-increased plasma
creatine kinase, normal-to-increased urinary C6-C10 dicarboxylic acids, and
normal-to-increased urinary glutaric acid. Clinical rows include episodic
encephalopathy, liver dysfunction, vomiting, and characteristic muscle weakness.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. The best local target is
`Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml`, not the primary CoQ10
deficiency umbrella. The MADD file explicitly covers ETFDH as a definitive
disease gene, late-onset riboflavin-responsive MADD, broad acylcarnitine
abnormalities, glutaric and dicarboxylic aciduria, elevated CK, lipid storage
myopathy, proximal muscle weakness, episodic decompensation, liver involvement,
vomiting, riboflavin, carnitine, and CoQ10 adjunctive context.

The local file also captures newer ETFDH-CoQ biology through ETFDH-driven
mitochondrial redox/metabolon disruption, which explains why an IEMbase label
can foreground CoQ10 while the disease target remains ETFDH/MADD.

## Concordance and completeness

Judgement: false negative; resolve to `Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml`
with ETFDH/myopathic late-onset context.

IEMbase and DisMech agree on ETFDH identity, autosomal recessive inheritance,
acylcarnitine and dicarboxylic-organic-acid abnormalities, glutaric acid,
elevated CK, muscle weakness, and episodic systemic involvement. IEMbase is a
compact myopathic-facet row; DisMech already has richer ETFDH/MADD mechanism and
treatment coverage.

## Curation actions

- Map this record to `Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml#ETFDH`.
- Do not create a separate primary CoQ10 deficiency mapping unless the scope is
  intentionally split from ETFDH/MADD.
- Preserve the CoQ10-deficiency label as a synonym/facet prompt, plus CK,
  acylcarnitine, dicarboxylic-acid, glutaric-acid, liver, vomiting, episodic
  encephalopathy, and muscle-weakness rows.

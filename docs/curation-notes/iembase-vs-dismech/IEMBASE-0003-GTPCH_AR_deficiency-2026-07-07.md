# IEMbase 0003: GCH1-related GTP cyclohydrolase I deficiency, autosomal recessive

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 3 |
| Nosology | 21.1.02.01 |
| Gene | GCH1 |
| External IDs | OMIM:233910 |
| Generated mapping | UNMAPPED |
| Likely DisMech targets | `Tetrahydrobiopterin_Deficiency.yaml#GTPCH Deficiency`; `Disorder_of_Catecholamine_Synthesis.yaml#Autosomal recessive GTP cyclohydrolase I deficiency` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase presents the recessive GCH1 disorder as an early neurometabolic disease
with dystonia, feeding difficulty, limb hypertonia, axial hypotonia,
microcephaly, swallowing difficulty, and tremor as characteristic clinical
features. Additional features include attention disorder, aggressive behavior,
drooling, intellectual disability, ptosis, myoclonic seizures, and temperature
instability.

The biochemical profile is BH4-deficiency-like: increased plasma phenylalanine,
low CSF homovanillic acid and 5-HIAA, reduced GTPCH activity, strong BH4 loading
test response, and low biopterin and neopterin in CSF, dried blood spot, and
urine.

Treatments include 5-hydroxytryptophan, folinic acid, levodopa/carbidopa,
phenylalanine-reduced diet, and sapropterin.

## DisMech phenotype coverage

The generated crosswalk missed a real local home. `Tetrahydrobiopterin
Deficiency` has a `GTPCH Deficiency` subtype with GCH1 genetics and a BH4
biosynthesis mechanism. `Disorder of Catecholamine Synthesis` also has an
autosomal recessive GTP cyclohydrolase I deficiency subtype and covers the
monoamine-deficiency axis.

At the umbrella level, DisMech covers hyperphenylalaninemia, developmental
delay, intellectual disability, hypotonia, dystonia, parkinsonism, oculogyric
crisis, seizures, speech delay, gait ataxia, low CSF neurotransmitter
metabolites, sapropterin, levodopa/carbidopa, 5-hydroxytryptophan, folinic acid,
and phenylalanine restriction.

## Concordance and completeness

Judgement: mapping false negative; phenotype coverage is moderate once the
manual target is selected.

DisMech captures the shared BH4/catecholamine mechanism but not the
IEMbase-specific clinical pattern of swallowing difficulty, feeding difficulty,
ptosis, temperature instability, tremor, and microcephaly. It also lacks a
subtype-specific pterin pattern for recessive GCH1 deficiency.

## Curation actions

- Add aliases or mapper normalization so IEMbase GTPCH autosomal recessive maps
  to the existing local subtype.
- Decide whether `Tetrahydrobiopterin Deficiency` or `Disorder of Catecholamine
  Synthesis` should be the canonical crosswalk target; the other can remain a
  secondary umbrella context.
- Consider subtype-specific biochemical entries for low neopterin/biopterin and
  reduced GTPCH activity if evidence is available.

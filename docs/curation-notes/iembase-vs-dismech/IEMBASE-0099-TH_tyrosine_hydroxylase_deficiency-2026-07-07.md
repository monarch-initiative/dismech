# IEMbase 0099: TH-related tyrosine hydroxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 99 |
| Nosology | 23.1.01.01 |
| Gene | TH |
| External IDs | OMIM:191290 |
| Generated mapping | AMBIGUOUS |
| Candidate DisMech targets | `Autosomal_Recessive_Dopa_Responsive_Dystonia.yaml`; `Disorder_of_Catecholamine_Synthesis.yaml#Tyrosine hydroxylase deficiency`; `Dopa_Responsive_Dystonia.yaml#AR-DRD` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive TH-related tyrosine hydroxylase
deficiency, with alternate labels L-dopa responsive dystonia and TH.
Treatability is marked yes.

The characteristic biochemical rows are CSF MHPG,
CSF HVA/5-HIAA ratio, and CSF homovanillic acid. The wider panel also includes
CSF 5-HIAA, urinary dopamine, urinary homovanillic acid, urinary
norepinephrine, urinary VMA, and plasma prolactin.

The characteristic clinical rows include bradykinesia, dystonia, hypokinesia,
hypotonia, intellectual disability, oculogyric crisis, ptosis, rigidity,
tremor, feeding difficulties, drooling, irritability and lethargy crises,
sweating, temperature instability, sleep disturbance, growth retardation,
epileptic seizures, and complicated perinatal course.

Treatment is L-dopa plus carbidopa.

## DisMech phenotype coverage

The generated AMBIGUOUS status is understandable, but the canonical local target
should be `Autosomal_Recessive_Dopa_Responsive_Dystonia.yaml`.

That file has the exact MONDO concept for TH-deficient dopa-responsive dystonia,
TH biallelic pathogenic variants, tyrosine hydroxylase enzymatic deficiency,
central dopamine biosynthesis impairment, infantile parkinsonism and
progressive infantile encephalopathy subtypes, low CSF homovanillic acid,
bradykinesia, hypokinesia, hypotonia, oculogyric crises, ptosis, rigidity,
tremor, feeding difficulties, drooling/excessive salivation, sweating/night
sweats, and levodopa with a decarboxylase inhibitor.

`Dopa_Responsive_Dystonia.yaml#AR-DRD` is useful group-level context.
`Disorder_of_Catecholamine_Synthesis.yaml#Tyrosine hydroxylase deficiency` is
useful pathway-umbrella context. Neither is as specific as the standalone
TH-deficient AR DRD entry.

## Concordance and completeness

Judgement: ambiguous generated mapping with high local disease-level coverage
once the specific target is selected.

IEMbase is richer for neurotransmitter-panel detail, especially MHPG,
HVA/5-HIAA ratio, urinary catecholamines, VMA, and prolactin. DisMech is richer
for disease scope, subtype structure, pathophysiology, genetic evidence, and
levodopa-response rationale.

## Curation actions

- Resolve this record to `Autosomal_Recessive_Dopa_Responsive_Dystonia.yaml` as
  the canonical target.
- Keep `Dopa_Responsive_Dystonia.yaml#AR-DRD` and
  `Disorder_of_Catecholamine_Synthesis.yaml#Tyrosine hydroxylase deficiency` as
  secondary umbrella contexts.
- Consider adding additional neurotransmitter biomarkers from IEMbase if the
  TH entry is expanded.

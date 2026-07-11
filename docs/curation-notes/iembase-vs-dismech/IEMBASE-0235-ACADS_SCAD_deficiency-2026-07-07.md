# IEMbase 0235: ACADS-related Short-chain acyl CoA dehydrogenase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 235 |
| Nosology | 4.2.01.01 |
| Gene | ACADS |
| External IDs | OMIM:201470; ORPHA:26792 |
| Generated mapping | MAPPED; `Idiopathic_Spontaneous_Coronary_Artery_Dissection.yaml` |
| Candidate DisMech targets | `SCAD_Deficiency.yaml`; generated false target `Idiopathic_Spontaneous_Coronary_Artery_Dissection.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as ACADS-related short-chain acyl-CoA dehydrogenase
deficiency, with alternate labels ethylmalonic aciduria and SCAD. The record is
autosomal recessive and treatability is marked unknown.

The biochemical rows include urinary butyrylglycine, blood/plasma/dried-blood
spot C4 butyrylcarnitine, reduced short-chain acyl-CoA dehydrogenase enzyme
activity in fibroblasts, ethylmalonic acid, methylsuccinic acid, and low-normal
glucose in early life. Clinical rows include behavioral disorder, exercise
intolerance, hypoglycemia, predisposition to symptomatic disease, secondary
mitochondrial dysfunction, short nose, and small mouth. Characteristic rows
include developmental delay, dysmorphic features, epilepsy, failure to thrive,
and hypotonia.

## DisMech phenotype coverage

`SCAD_Deficiency.yaml` is the correct target. The local entry covers biallelic
ACADS disease, reduced SCAD activity, impaired short-chain fatty-acid
beta-oxidation, accumulation of butyrylcarnitine/C4, ethylmalonic acid,
methylsuccinic acid, and butyrylglycine, and the current interpretive caution
that SCAD deficiency is often a biochemical phenotype with debated clinical
significance. It also explicitly distinguishes SCAD deficiency from MCAD and
long-chain fatty-acid oxidation disorders by noting that classic hypoketotic
hypoglycemia, recurrent rhabdomyolysis, and cardiomyopathy are generally absent.

The generated target, `Idiopathic_Spontaneous_Coronary_Artery_Dissection.yaml`,
is unrelated cardiovascular SCAD. It matched through the shared SCAD acronym,
not through disease biology.

## Concordance and completeness

Judgement: generated mapping is a false positive; correct local target is
`SCAD_Deficiency.yaml`.

IEMbase and DisMech agree strongly on ACADS/SCAD identity and the core
biochemical diagnostic markers. The main interpretive difference is clinical
weighting: IEMbase lists several reported symptomatic features, while DisMech
emphasizes that pathogenicity and clinical significance are debated and that
many newborn-screening individuals remain asymptomatic. This difference should
be preserved as curation nuance rather than treated as disagreement.

## Curation actions

- Replace the generated coronary-artery-dissection mapping with
  `SCAD_Deficiency.yaml`.
- Keep the SCAD acronym collision as a regression-test case for acronym-only
  exact-alias matching.
- Use IEMbase as a compact checklist for the C4, ethylmalonic acid,
  methylsuccinic acid, butyrylglycine, and enzyme-activity markers.

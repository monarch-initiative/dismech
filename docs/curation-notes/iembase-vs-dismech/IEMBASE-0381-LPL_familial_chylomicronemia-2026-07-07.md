# IEMbase 0381: LPL-related Lipoprotein lipase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 381 |
| Nosology | 15.2.16.01 |
| Gene | LPL |
| External IDs | OMIM:609708; OMIM:238600; ORPHA:411 |
| Generated mapping | UNMAPPED; no candidate |
| Candidate DisMech targets | `Familial_Chylomicronemia_Syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive LPL-related lipoprotein lipase
deficiency, with alternate names hyperlipoproteinemia type 1, familial
hyperchylomicronemia, and HLP type 1.

Clinical rows include lipemia retinalis, pancreatitis, eruptive xanthomas, and
abdominal pain. Biochemical rows include low post-heparin lipoprotein lipase
activity, increased cholesterol, very low HDL cholesterol, and very high serum
triglyceride. Treatment rows include volanesorsen, low-fat diet, and
plasmapheresis.

## DisMech phenotype coverage

The generated unmapped status is a false negative. Local
`Familial_Chylomicronemia_Syndrome.yaml` models a rare autosomal recessive
monogenic lipid disorder with extreme sustained hypertriglyceridemia caused by
absent or markedly impaired lipoprotein lipase activity. The file explicitly
includes biallelic LPL variants and the relevant phenotype cluster of recurrent
acute pancreatitis, eruptive xanthomas, hepatosplenomegaly, lipemia retinalis,
and abdominal pain.

Local DisMech is broader than IEMbase because it treats familial
chylomicronemia syndrome as a multi-gene disorder that can also involve APOC2,
APOA5, GPIHBP1, or LMF1, and it has stronger coverage of very-low-fat diet and
apoC-III-targeting therapies.

## Concordance and completeness

Judgement: false negative; resolve to `Familial_Chylomicronemia_Syndrome.yaml`.

The resources agree on LPL-related familial hyperchylomicronemia, autosomal
recessive inheritance, severe hypertriglyceridemia, low LPL activity,
pancreatitis, lipemia retinalis, eruptive xanthomas, abdominal pain, and
dietary/pharmacologic triglyceride-lowering management.

## Curation actions

- Map this record to `Familial_Chylomicronemia_Syndrome.yaml`, with the LPL
  branch as the relevant subtype context.
- Consider adding IEMbase's post-heparin LPL activity, HDL cholesterol,
  cholesterol directionality, and plasmapheresis row as future enrichment after
  source verification.
- Preserve the distinction between LPL-specific deficiency and broader
  multi-gene familial chylomicronemia syndrome when adding subtype anchors.

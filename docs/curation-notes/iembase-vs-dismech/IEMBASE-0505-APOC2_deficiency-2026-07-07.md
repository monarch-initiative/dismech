# IEMbase 0505: APOC2-related apolipoprotein C-II deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 505 |
| Nosology | 15.2.17.01 |
| Gene | APOC2 |
| External IDs | OMIM:608083; OMIM:207750; ORPHA:309020 |
| Generated mapping | UNMAPPED; no candidate |
| Candidate DisMech targets | `Familial_Chylomicronemia_Syndrome.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive APOC2-related apolipoprotein C-II
deficiency. Treatment rows include plasmapheresis, docosahexaenoic acid,
fibrates, low-fat diet, medium-chain triglycerides, and niacin. Biochemical
rows include decreased post-heparin lipoprotein lipase activity, increased
serum cholesterol, decreased HDL cholesterol, and increased serum triglyceride.
Clinical rows include lipemia retinalis, pancreatitis, eruptive xanthomas, and
abdominal pain.

## DisMech phenotype coverage

The generated unmapped status is a false negative. Local
`Familial_Chylomicronemia_Syndrome.yaml` explicitly models familial
chylomicronemia syndrome as an autosomal recessive multi-gene disorder caused
by biallelic pathogenic variants in LPL or in APOC2, APOA5, GPIHBP1, or LMF1.
The entry includes APOC2 as an FCS gene, notes that apolipoprotein C-II is an
essential cofactor for LPL activation, and models the shared downstream
mechanism of functional LPL deficiency, chylomicronemia, severe
hypertriglyceridemia, pancreatitis, eruptive xanthomas, hepatosplenomegaly,
lipemia retinalis, and abdominal pain.

DisMech is stronger on the unified FCS mechanism and contemporary apoC-III
targeted therapies. IEMbase is more APOC2-specific in listing older or acute
management prompts such as plasmapheresis, niacin, fibrates, DHA, and
medium-chain triglycerides.

## Concordance and completeness

Judgement: false negative; resolve to `Familial_Chylomicronemia_Syndrome.yaml`
with APOC2 branch context.

The resources agree on recessive APOC2-related chylomicronemia biology,
functional LPL deficiency, severe hypertriglyceridemia, low HDL, pancreatitis,
lipemia retinalis, eruptive xanthomas, abdominal pain, and low-fat diet as a
central management concept.

## Curation actions

- Map this record to `Familial_Chylomicronemia_Syndrome.yaml`, using the APOC2
  genetic branch rather than the LPL branch.
- Consider adding APOC2-specific treatment rows only after source review,
  especially where IEMbase marks fibrates, niacin, and docosahexaenoic acid as
  no-change for triglycerides.
- Consider adding post-heparin LPL activity, serum cholesterol, and HDL
  directionality as future biochemical readouts for FCS.

# IEMbase 0668: SI-related sucrase-isomaltase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 668 |
| Nosology | 3.6.04.01 |
| Nosology code | IEM0318 |
| Gene | SI |
| External IDs | OMIM:222900; ORPHA:306486 |
| Generated mapping | MAPPED to `Congenital_Sucrase-Isomaltase_Deficiency.yaml` |
| Candidate DisMech targets | `Congenital_Sucrase-Isomaltase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive SI-related sucrase-isomaltase deficiency,
also labeled congenital sucrase-isomaltase deficiency, disaccharide intolerance
I, and congenital sucrose intolerance.

Biochemical rows include markedly decreased mucosal sucrase activity, decreased
to very low mucosal isomaltase activity, normal stool reducing sugars, and
normal to low plasma sodium. Clinical rows include malabsorption, failure to
thrive, diarrhea, profuse osmotic diarrhea, dehydration, and possible
urolithiasis from infancy onward.

## DisMech phenotype coverage

`Congenital_Sucrase-Isomaltase_Deficiency.yaml` is an exact local target. It
models biallelic SI variants, brush-border sucrase-isomaltase deficiency,
impaired digestion of sucrose and starch, osmotic diarrhea, bloating,
flatulence, abdominal pain, vomiting, failure to thrive, malnutrition, and
diagnostic sucrase/isomaltase enzyme testing.

The local entry also captures dietary treatment and sacrosidase-relevant
management context.

## Concordance and completeness

Judgement: exact high-concordance mapping.

IEMbase and DisMech agree on the intestinal brush-border enzyme defect,
decreased sucrase/isomaltase activity, carbohydrate malabsorption, osmotic
diarrhea, and growth/nutrition consequences. IEMbase adds several row-level
prompts that are thinner locally: sodium directionality, normal reducing sugars,
dehydration, and urolithiasis.

## Curation actions

- Keep `Congenital_Sucrase-Isomaltase_Deficiency.yaml` as the disease-level
  target.
- Preserve decreased mucosal sucrase and isomaltase activities as diagnostic
  anchors.
- Review dehydration, sodium abnormalities, normal stool reducing sugars, and
  urolithiasis as possible enrichment prompts.
- Maintain the distinction from other disaccharidase deficiencies and generalized
  malabsorption syndromes.

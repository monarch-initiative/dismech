# IEMbase 0451: SDHA-related succinate dehydrogenase subunit A deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 451 |
| Nosology | 7.2.01.01 |
| Gene | SDHA |
| External IDs | OMIM:252011; ORPHA:44890 |
| Generated mapping | UNMAPPED; low candidate `Pyruvate_Dehydrogenase_Deficiency.yaml` / E1-beta deficiency |
| Candidate DisMech targets | No exact local target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents SDHA-related succinate dehydrogenase subunit A deficiency,
also called mitochondrial complex II deficiency. It records autosomal recessive
inheritance. Biochemical rows include decreased complex II activity in
fibroblasts and increased lactate. Clinical rows include Leigh syndrome,
Kearns-Sayre syndrome, hypertrophic cardiomyopathy, dementia, encephalopathy,
myopathy, and short stature. There are no treatment rows.

## DisMech phenotype coverage

There is no exact local DisMech target for AR SDHA mitochondrial complex II
deficiency. Local SDHA context exists in
`Pheochromocytoma_Paraganglioma.yaml` as part of SDHx cancer predisposition, but
that is not the metabolic complex II deficiency entity. `Leigh_Syndrome.yaml`
provides broad phenotype context for Leigh syndrome and oxidative
phosphorylation disease, but it does not name SDHA or provide an SDHA/complex II
subtype.

The generated `Pyruvate_Dehydrogenase_Deficiency.yaml` E1-beta candidate is a
false positive. Local PDH deficiency involves PDHA1, PDHB, PDHX, DLD, PDP1, or
related pyruvate dehydrogenase complex biology, not succinate dehydrogenase
complex II deficiency.

## Concordance and completeness

Judgement: true SDHA/complex II deficiency local gap; reject pyruvate
dehydrogenase E1-beta deficiency as an exact mapping.

The candidate shares lactic acidosis and neurologic mitochondrial disease
vocabulary, but the enzyme complex, gene, proximal biochemical lesion, and
expected modeling target are different.

## Curation actions

- Keep this record unmapped until an SDHA-related mitochondrial complex II
  deficiency target exists, or until an explicit Leigh-syndrome subtype decision
  includes SDHA.
- Do not map to `Pyruvate_Dehydrogenase_Deficiency.yaml`.
- Do not map metabolic SDHA deficiency to SDHx cancer-predisposition coverage.
- If curated, include SDHA, autosomal recessive inheritance, succinate
  dehydrogenase complex II deficiency, decreased fibroblast complex II activity,
  lactate elevation, Leigh syndrome, cardiomyopathy, encephalopathy, myopathy,
  dementia, short stature, and Kearns-Sayre-like presentation only if source
  evidence supports that row.

# IEMbase 0174: FH-related fumarase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 174 |
| Nosology | 5.2.06.01 |
| Gene | FH |
| External IDs | OMIM:606812; ORPHA:24 |
| Generated mapping | MAPPED to `Familial_Hyperaldosteronism_Type_I.yaml` by alias `FH1` |
| Candidate DisMech targets | None valid |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as FH-related fumarate hydratase deficiency, with
alternate labels fumarase deficiency, fumaric aciduria, and FH1. Treatability
is marked unknown, and the extracted JSON does not list treatment rows.

The biochemical rows include markedly increased urinary fumaric acid,
increased plasma lactate, normal to increased CSF lactate, normal to increased
urinary 2-ketoglutaric acid and succinic acid, variable bilirubin, and normal
to increased ASAT/ALAT. Clinical rows include altered consciousness, athetosis,
autism, coarse facial features, dysmorphic features, dystonia, abnormal EEG,
fetal hydrops, hepatosplenomegaly, hypertelorism, lactic acidosis,
microcephaly, neutropenia, optic atrophy, pyramidal signs, motor regression,
seizures, speech abnormality or absence, impaired vision, cerebral palsy,
episodic course, failure to thrive, feeding difficulties, gastroesophageal
reflux, hypotonia, irritability, chronic malnutrition, metabolic acidosis,
neurologic symptoms, psychomotor retardation, and sudden death.

## DisMech phenotype coverage

No valid local DisMech target was found. The generated mapping to
`Familial_Hyperaldosteronism_Type_I.yaml` is a false positive caused by the
short alias `FH1`. The local hyperaldosteronism entry models a
CYP11B1/CYP11B2 chimeric gene, ACTH-regulated aldosterone synthase expression,
low-renin hypertension, hypokalemia, and glucocorticoid-remediable
aldosteronism. That is unrelated to FH/fumarate hydratase deficiency and
fumaric aciduria.

## Concordance and completeness

Judgement: generated high-confidence mapping is false; this is a true local
gap.

IEMbase describes a severe fumarase-deficiency metabolic encephalopathy with
fumaric aciduria and lactic/metabolic acidosis. DisMech does not currently
have a metabolic FH/fumarase deficiency entry, and the alias collision with
familial hyperaldosteronism type I should be blocked in future mapping logic.

## Curation actions

- Do not map this record to `Familial_Hyperaldosteronism_Type_I.yaml`.
- Add a future FH/fumarase deficiency/fumaric aciduria entry.
- Treat `FH1` as an unsafe short alias unless the disease context confirms
  fumarate hydratase deficiency rather than familial hyperaldosteronism.
- Future entry should separate the severe metabolic enzyme-deficiency disease
  from FH-related tumor-predisposition contexts if those are later curated.

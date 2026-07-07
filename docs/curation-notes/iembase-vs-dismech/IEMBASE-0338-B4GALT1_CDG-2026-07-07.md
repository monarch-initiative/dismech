# IEMbase 0338: B4GALT1-related beta-1,4-galactosyltransferase 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 338 |
| Nosology | 18.1.29.01 |
| Gene | B4GALT1 |
| External IDs | OMIM:607091; ORPHA:79332 |
| Generated mapping | UNMAPPED; low-score candidate `GM1_Gangliosidosis_Type_1.yaml` |
| Candidate DisMech targets | Reject `GM1_Gangliosidosis_Type_1.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents B4GALT1-CDG/CDG-IId, a type II congenital disorder of
glycosylation. Characteristic rows include axial hypotonia, facial dysmorphism,
and myopia. Additional clinical rows include recurrent diarrhea, hypertelorism,
long philtrum, low-set ears, perinatal bleeding diathesis, prominent forehead,
and thin upper lip.

The biochemical rows include increased ASAT, cholinesterase, and creatine
kinase; asialotransferrin, disialotransferrin, monosialotransferrin,
trisialotransferrin, tetrasialotransferrin, hypogalactosylated transferrin
glycans, and type II sialotransferrins; fibrinogen/APTT; and antithrombin III
and factor XI. No treatment rows are present.

## DisMech phenotype coverage

The generated GM1 gangliosidosis candidate is a lexical false positive around
"beta-galactosyl" wording. GM1 gangliosidosis type 1 is a GLB1 lysosomal
beta-galactosidase storage disorder with GM1 ganglioside accumulation,
neurodegeneration, hepatosplenomegaly, dysostosis multiplex, coarse facies, and
cherry-red macula. It is not B4GALT1-CDG and does not model a Golgi
galactosyltransferase defect.

No standalone B4GALT1-CDG entry exists locally. The CDG module and grouping
provide only family-level context.

## Concordance and completeness

Judgement: true local disease gap; reject the GM1 candidate.

The IEMbase record is a type II glycosylation-processing disorder with
hypogalactosylated transferrin and coagulation-protein signals. That is
mechanistically distinct from lysosomal beta-galactosidase deficiency and GM1
ganglioside storage.

## Curation actions

- Add a standalone B4GALT1-CDG target before treating this IEMbase record as
  mapped.
- Do not map to GM1 gangliosidosis based on the shared galactose-related
  wording.
- Preserve hypogalactosylated transferrin, type II glycan fractions,
  bleeding/coagulation, diarrhea, myopia, dysmorphism, and CK/transaminase rows
  as future-curation prompts.

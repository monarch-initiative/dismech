# IEMbase 0285: HEXB-related Beta-hexosaminidase subunit beta deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 285 |
| Nosology | 20.1.06.01 |
| Gene | HEXB |
| External IDs | OMIM:268800; ORPHA:796 |
| Generated mapping | UNMAPPED; weak candidate `Sandhoff_Disease.yaml` |
| Candidate DisMech targets | `Sandhoff_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents Sandhoff disease / GM2 gangliosidosis O variant due to HEXB
beta-subunit deficiency. Inheritance is autosomal recessive, treatability is
unknown, and prevalence is listed as 1:130,000 in Europe.

Clinical rows include ataxia, brain atrophy, choreoathetosis, dystonia, foam
cells, hepatosplenomegaly, macrocephaly, muscle weakness, seizures, exaggerated
startle response, urinary incontinence, and abnormal VEP. Biochemical rows list
markedly decreased beta-hexosaminidase A, decreased beta-hexosaminidase B
activity, increased urinary oligosaccharides, and increased serum LysoGM2.

## DisMech phenotype coverage

`Sandhoff_Disease.yaml` is the correct local target despite the generated
UNMAPPED status. The local entry models biallelic HEXB variants, deficient beta
subunit shared by hexosaminidase A and B, combined beta-hexosaminidase
deficiency, GM2 and GA2 glycosphingolipid storage, lysosomal dysfunction in
neurons and glia, and subtype distinctions for infantile, juvenile, and adult
Sandhoff disease.

Local phenotypes include developmental regression, exaggerated startle
response, hypotonia, seizures, cherry-red spot, and coarse facial features.
Local biochemical coverage includes total hexosaminidase A+B activity, GM2
ganglioside storage, and GA2 glycolipid storage. Treatments include supportive
care, investigational gene therapy, and 4-phenylbutyric acid.

## Concordance and completeness

Judgement: false negative mapping; resolve to `Sandhoff_Disease.yaml`.

IEMbase and DisMech agree on HEXB/Sandhoff identity, autosomal recessive
inheritance, combined hexosaminidase A and B deficiency, GM2 storage logic,
startle response, seizures, hypotonia/muscle weakness, and neurologic
progression. DisMech is stronger for mechanistic chain, subtype framing, GM2
and GA2 substrate interpretation, and treatment hypotheses.

IEMbase adds useful phenotype and biomarker prompts not yet explicit locally:
brain atrophy, choreoathetosis, dystonia, foam cells, hepatosplenomegaly,
macrocephaly, urinary incontinence, abnormal VEP, urinary oligosaccharides, and
LysoGM2. The separate enzyme rows for beta-hexosaminidase A and B also provide a
more granular assay view than the local total-activity entry.

## Curation actions

- Resolve this record to `Sandhoff_Disease.yaml`.
- Treat the generated weak candidate as a true target; the low score is a
  crosswalk failure, not a biological mismatch.
- Consider future enrichment for brain atrophy, movement-disorder terms, VEP,
  urinary incontinence, oligosaccharides, LysoGM2, and separate Hex A / Hex B
  enzyme assay rows.

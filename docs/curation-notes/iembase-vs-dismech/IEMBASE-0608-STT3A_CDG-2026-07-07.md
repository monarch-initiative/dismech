# IEMbase 0608: STT3A-related congenital disorder of glycosylation

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 608 |
| Nosology | 18.1.17.01 |
| Gene | STT3A |
| External IDs | OMIM:615596; OMIM:601134; ORPHA:370921 |
| Generated mapping | CANDIDATE; `ALG12_Congenital_Disorder_of_Glycosylation.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents STT3A-related congenital disorder of glycosylation, labelled
STT3A-CDG. The record is autosomal recessive, classified under N-glycosylation
disorders, has unknown treatability, and has no treatment rows.

Biochemical rows include increased serum N-glycans, normal-to-increased
asialotransferrin and disialotransferrin, decreased-to-normal
tetrasialotransferrin, and decreased-to-normal factor VIII and von Willebrand
factor. Clinical rows include developmental delay, intellectual disability,
seizures, hypotonia, gastrointestinal dysmotility, failure to thrive,
microcephaly, and cerebellar atrophy on MRI.

## DisMech phenotype coverage

`ALG12_Congenital_Disorder_of_Glycosylation.yaml` is a false-positive CDG-class
candidate. It models ALG12 mannosyltransferase deficiency, not STT3A, the
catalytic subunit of the oligosaccharyltransferase complex responsible for
co-translational N-glycosylation. Although both records share type I CDG
features, neurodevelopmental involvement, and coagulation-related clues, the
gene, enzymatic step, and disease identity differ.

No exact STT3A-CDG target was identified locally.

## Concordance and completeness

Judgement: true local gap; reject ALG12-CDG as exact coverage.

The generated candidate is useful only as neighboring CDG biology. IEMbase 0608
needs a distinct STT3A/oligosaccharyltransferase CDG target before any phenotype
import.

## Curation actions

- Create or identify an exact STT3A-CDG target before import.
- Reject `ALG12_Congenital_Disorder_of_Glycosylation.yaml` as an exact mapping.
- Preserve N-glycan and transferrin isoform readouts, factor VIII, von
  Willebrand factor, seizures, hypotonia, developmental delay, intellectual
  disability, gastrointestinal dysmotility, failure to thrive, microcephaly, and
  cerebellar-atrophy prompts.

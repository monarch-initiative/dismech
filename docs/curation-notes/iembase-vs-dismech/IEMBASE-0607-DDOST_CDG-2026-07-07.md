# IEMbase 0607: DDOST-related congenital disorder of glycosylation

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 607 |
| Nosology | 18.1.28.01 |
| Gene | DDOST |
| External IDs | OMIM:614507; OMIM:602202; ORPHA:300536 |
| Generated mapping | CANDIDATE; `ALG12_Congenital_Disorder_of_Glycosylation.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents DDOST-related congenital disorder of glycosylation, labelled
DDOST-CDG and CDG-Ir. The record is autosomal recessive, classified under
N-glycosylation disorders, has unknown treatability, and has no treatment rows.

Biochemical rows include increased asialotransferrin, disialotransferrin, and
monosialotransferrin, decreased tetrasialotransferrin, and decreased
antithrombin, factor XI, protein C, and protein S. Clinical rows include
neonatal liver dysfunction, oromotor dysfunction, strabismus, developmental
delay, hypotonia, failure to thrive, gastroesophageal reflux, constipation,
intellectual disability, delayed myelination, ear infections, and osteopenia.

## DisMech phenotype coverage

`ALG12_Congenital_Disorder_of_Glycosylation.yaml` is a false-positive CDG-class
candidate. It models ALG12 mannosyltransferase deficiency in lipid-linked
oligosaccharide assembly with type I transferrin hypoglycosylation and
coagulation abnormalities. IEMbase 0607 instead concerns DDOST, an
oligosaccharyltransferase subunit, with a different gene and disease identity.

The local CDG entries provide useful N-glycosylation context, but no exact
DDOST-CDG / CDG-Ir target was identified.

## Concordance and completeness

Judgement: true local gap; reject ALG12-CDG as exact coverage.

The candidate captures shared type I CDG/coagulation-protein logic, but gene and
enzymatic complex differ. DDOST-CDG should not be imported into ALG12-CDG without
source-specific support.

## Curation actions

- Create or identify an exact DDOST-CDG / CDG-Ir target before import.
- Reject `ALG12_Congenital_Disorder_of_Glycosylation.yaml` as an exact mapping.
- Preserve transferrin isoforms, antithrombin, factor XI, protein C/S,
  neonatal liver dysfunction, oromotor dysfunction, strabismus, reflux,
  constipation, delayed myelination, ear infections, osteopenia, failure to
  thrive, hypotonia, and neurodevelopmental prompts.

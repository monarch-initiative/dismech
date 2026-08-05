# IEMbase 0609: STT3B-related congenital disorder of glycosylation

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 609 |
| Nosology | 18.1.27.01 |
| Gene | STT3B |
| External IDs | OMIM:615597; ORPHA:370924 |
| Generated mapping | CANDIDATE; `ALG12_Congenital_Disorder_of_Glycosylation.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents STT3B-CDG as an autosomal recessive N-glycosylation disorder
with unknown treatability and no treatment rows. Biochemical rows show a type I
transferrin pattern: increased serum asialotransferrin and disialotransferrin,
with decreased serum tetrasialotransferrin in the neonatal period.

Clinical rows emphasize neonatal-onset multisystem disease: developmental
delay, hypotonia, failure to thrive, gastrointestinal dysmotility, hepatopathy,
respiratory failure, seizures, microcephaly, cerebral atrophy on MRI, optic
atrophy, thrombocytopenia, intellectual disability, undescended testes,
hypoplastic scrotum, and broader external-genital abnormality.

## DisMech phenotype coverage

`ALG12_Congenital_Disorder_of_Glycosylation.yaml` is a false-positive CDG-class
candidate. ALG12-CDG is an ER lipid-linked oligosaccharide assembly disorder
caused by ALG12 mannosyltransferase deficiency, whereas STT3B encodes an
oligosaccharyltransferase catalytic subunit involved in N-glycan transfer.

No exact STT3B-CDG target was identified locally.

## Concordance and completeness

Judgement: true local gap; reject ALG12-CDG as exact coverage.

The generated candidate is useful only as neighboring N-glycosylation biology.
IEMbase 0609 needs a distinct STT3B/oligosaccharyltransferase CDG target before
phenotype import.

## Curation actions

- Create or identify an exact STT3B-CDG target before import.
- Reject `ALG12_Congenital_Disorder_of_Glycosylation.yaml` as an exact mapping.
- Preserve transferrin type I pattern, neonatal respiratory/hepatic/coagulation,
  neurodevelopmental, optic-atrophy, and genital-phenotype prompts.

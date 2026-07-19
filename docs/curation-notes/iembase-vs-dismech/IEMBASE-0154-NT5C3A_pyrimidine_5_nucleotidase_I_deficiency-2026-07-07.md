# IEMbase 0154: NT5C3A-related pyrimidine-5'-nucleotidase I deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 154 |
| Nosology | 16.1.04.02 |
| Gene | NT5C3A |
| External IDs | OMIM:266120; OMIM:606224; OMIM:191720; ORPHA:35120 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Hereditary_Orotic_Aciduria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as NT5C3A-related pyrimidine-5'-nucleotidase I
deficiency, with the alternate label uridine 5'-monophosphate hydrolase 1
deficiency. Treatability is marked unknown.

The biochemical profile is erythrocyte-centered: decreased RBC
pyrimidine-5'-nucleotidase I activity across age groups, increased RBC
pyrimidine nucleotides, and RBC glutathione reported as decreased to normal.
The clinical signal is nonspherocytic hemolytic anemia with basophilic
stippling, plus basophilic stippling as a separate row, myoglobinuria, and
splenomegaly.

## DisMech phenotype coverage

There is no valid standalone DisMech target for inherited NT5C3A-related
pyrimidine-5'-nucleotidase I deficiency.

`Hereditary_Orotic_Aciduria.yaml` is a lexical/pathway neighbor but is not the
right disease. It is UMPS-related de novo pyrimidine synthesis deficiency with
orotic acid accumulation, megaloblastic anemia, immunodeficiency, and uridine
replacement therapy. That is mechanistically different from an erythrocyte
pyrimidine nucleotide catabolism defect caused by NT5C3A deficiency.

`Lead_Poisoning.yaml` contains an acquired erythrocyte pyrimidine
5'-nucleotidase deficiency mechanism, but that reflects lead toxicity rather
than inherited NT5C3A disease and should not be used as the disease target.

## Concordance and completeness

Judgement: true local gap.

The generated hereditary orotic aciduria candidate should be rejected. The
IEMbase profile points to RBC enzyme deficiency, RBC pyrimidine nucleotide
accumulation, and hemolytic anemia with basophilic stippling. No current
DisMech disease entry captures that inherited NT5C3A phenotype.

## Curation actions

- Leave IEMbase 154 unmapped for now.
- Future curation should create a standalone NT5C3A/pyrimidine-5'-nucleotidase
  I deficiency entry if this condition is in scope.
- Do not map this to hereditary orotic aciduria or to the acquired lead
  poisoning mechanism.

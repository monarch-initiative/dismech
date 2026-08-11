# IEMbase 0160: UPB1-related beta-ureidopropionase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 160 |
| Nosology | 16.1.03.02 |
| Gene | UPB1 |
| External IDs | OMIM:613161; OMIM:606673; ORPHA:65287 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Beta-Ketothiolase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as UPB1-related beta-ureidopropionase deficiency.
Treatability is marked unknown.

The biochemical rows are pyrimidine catabolism markers: increased plasma and
urinary dihydrothymine, increased plasma and urinary dihydrouracil, increased
plasma and urinary N-carbamyl-beta-alanine, and increased plasma
N-carbamyl-beta-aminoisobutyric acid. The clinical rows are variable and
include psychomotor delay, seizures, dystonia, hypotonia, speech disturbances,
dysmorphic features, hypertelorism, and strabismus.

## DisMech phenotype coverage

There is no local standalone UPB1/beta-ureidopropionase deficiency entry.

`Beta-Ketothiolase_Deficiency.yaml` is a false candidate. It is an ACAT1
disorder of isoleucine catabolism and ketone-body handling, with ketoacidotic
crises and isoleucine-derived organic acid markers. It does not model UPB1,
dihydropyrimidine catabolism, N-carbamyl-beta-alanine, dihydrothymine, or
dihydrouracil accumulation.

## Concordance and completeness

Judgement: true local gap.

The generated candidate appears to be a broad organic-acid/neurologic neighbor
rather than a disease match. IEMbase 160 is specifically a pyrimidine
catabolism disorder with UPB1 and beta-ureidopropionase biochemical markers.
Current DisMech coverage does not capture it.

## Curation actions

- Leave IEMbase 160 unmapped for now.
- Future curation should create a UPB1/beta-ureidopropionase deficiency entry
  if this disease is in scope.
- Use the IEMbase N-carbamyl-beta-alanine, N-carbamyl-beta-aminoisobutyric
  acid, dihydrothymine, dihydrouracil, seizures, hypotonia, dystonia, and
  psychomotor-delay rows as primary leads.

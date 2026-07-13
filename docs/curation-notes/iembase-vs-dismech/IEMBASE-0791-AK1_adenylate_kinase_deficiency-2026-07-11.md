# IEMbase 0791: AK1-related adenylate kinase 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 791 |
| Nosology | 16.2.13.01 |
| Nosology code | IEM0019 |
| Gene | AK1 |
| External IDs | OMIM:612631; ORPHA:86817 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | No exact local target; reject `Adenosine_Kinase_Deficiency.yaml` neighbor |
| Review date | 2026-07-11 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as AK1-related adenylate kinase
1 deficiency, with alternate name hemolytic anemia due to adenylate kinase
deficiency. The signal includes very low RBC adenylate kinase activity,
non-spherocytic hemolytic anemia with basophilic stippling, basophilic
stippling as a smear finding, and possible psychomotor delay.

## DisMech phenotype coverage

No exact DisMech target was found. Local hemolytic-anemia entries cover many
other etiologies, and `Lead_Poisoning.yaml` includes basophilic stippling and
acquired pyrimidine 5'-nucleotidase effects, but those are not AK1 deficiency.
The generated adenosine kinase deficiency neighbor is an enzyme-name/purine
metabolism neighbor, not a match.

## Concordance and completeness

Judgement: true local gap.

The local knowledge base lacks AK1, adenylate kinase 1 activity, and the
specific inherited nonspherocytic hemolytic anemia phenotype. General hemolytic
anemia, lead toxicity, or adenosine kinase deficiency should not be used as
coverage.

## Curation actions

- Keep IEMbase 0791 unmapped.
- Reject `Adenosine_Kinase_Deficiency.yaml`, lead poisoning, and generic
  hemolytic anemia entries as exact coverage.
- Future curation should preserve RBC adenylate kinase activity, basophilic
  stippling, nonspherocytic hemolytic anemia, and the possible psychomotor
  delay prompt.

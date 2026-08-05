# IEMbase 0318: CYP51A1-related lanosterol demethylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 318 |
| Nosology | 14.7.19.01 |
| Gene | CYP51A1 |
| External IDs | OMIM:601637 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Fuzzy candidate `COA3-Related_COX_Deficiency.yaml` rejected |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive CYP51A1-related lanosterol
demethylase deficiency. Alternate labels include CYP51 deficiency and
cytochrome P450 family 51 deficiency.

Characteristic rows include cataract, erythema, hypopigmentation, self injury,
and short stature. Additional clinical rows include developmental delay and
microcephaly. No biochemical or treatment rows are present in the cached
record.

## DisMech phenotype coverage

The generated fuzzy candidate is `COA3-Related_COX_Deficiency.yaml`, but this
is a lexical false positive. The local COA3 file covers COA3-related
mitochondrial complex IV deficiency with peripheral neuropathy, exercise
intolerance, obesity, short stature, and supportive metabolic care. It does not
share the CYP51A1 gene, lanosterol demethylase mechanism, or sterol pathway
scope.

There is no valid local CYP51A1 lanosterol demethylase deficiency target.

## Concordance and completeness

Judgement: true local disease gap.

The current local candidate has only a nonspecific short-stature overlap and
should not be used. IEMbase provides the initial review prompt set for future
curation: cataract, erythema, hypopigmentation, self-injury, short stature,
developmental delay, and microcephaly.

## Curation actions

- Do not map this record to COA3-related COX deficiency.
- Add a standalone CYP51A1 lanosterol demethylase deficiency target if this
  sterol-biosynthesis disease is prioritized.
- Look for source-backed biochemical sterol markers before modeling the entry,
  since the cached record has no biochemical rows.

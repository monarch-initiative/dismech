# IEMbase 0342: DOLK-related dolichol kinase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 342 |
| Nosology | 18.4.04.02 |
| Gene | DOLK |
| External IDs | OMIM:610768 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `DK1-congenital_disorder_of_glycosylation.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents DOLK-CDG/DK1-CDG, an autosomal recessive dolichol kinase
deficiency. Characteristic rows include early death. Additional clinical rows
include broad forehead, dilated cardiomyopathy, distal digital necrosis,
epilepsy, facial dysmorphism, failure to thrive, flat nose, hair abnormality,
hypertelorism, hypotonia, ichthyosiform erythroderma, large earlobe, low-set
ears, microcephaly, nystagmus, and delayed puberty.

The biochemical rows include increased transaminases, lipid-linked
oligosaccharide in fibroblasts, and type I sialotransferrins. No treatment rows
are present.

## DisMech phenotype coverage

The generated UNMAPPED status is a false negative. DisMech has a dedicated
`DK1-congenital_disorder_of_glycosylation.yaml` entry for DOLK-CDG with
biallelic DOLK causation, reduced dolichol kinase activity, compromised
dolichol phosphate biosynthesis, impaired N-linked glycosylation, abnormal
alpha-dystroglycan O-mannosylation, and multisystem disease.

Local phenotype coverage includes dilated cardiomyopathy, ichthyosis,
hypotonia, seizures, early death, abnormal transferrin/N-linked glycosylation,
and the characteristic connection between dolichol phosphate supply and
glycosylation. DisMech is stronger for mechanism and cardiomyopathy biology;
IEMbase adds granular dysmorphism, digital necrosis, delayed puberty, and named
biochemical rows.

## Concordance and completeness

Judgement: false negative; resolve to the local DK1/DOLK-CDG entry.

The resources agree on DOLK/DK1 identity, autosomal recessive inheritance,
dolichol phosphate/glycosylation biology, type I transferrin abnormality,
cardiomyopathy, ichthyotic skin disease, hypotonia/seizures, failure to thrive,
and early lethality.

## Curation actions

- Map this record to `DK1-congenital_disorder_of_glycosylation.yaml`.
- Consider future enrichment with digital necrosis, delayed puberty, nystagmus,
  hair/ear/forehead dysmorphism, transaminases, and granular
  lipid-linked-oligosaccharide rows after source verification.
- Treat absent IEMbase treatment rows as incomplete IEMbase coverage rather
  than a contradiction of local supportive/cardiac management.

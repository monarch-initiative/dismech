# IEMbase vs DisMech phenotype comparisons

These notes compare cached IEMbase disease JSON records against the current
local DisMech entries. They are manual curation notes, not evidence sources.
Use them as worklist triage for mapping corrections, phenotype gaps, and
subtype-placement decisions.

Source inputs for these batches:

- IEMbase cache: `data/iembase/disease_index.json` and
  `data/iembase/diseases/*.json`
- Generated crosswalk: `data/iembase/dismech_mapping.tsv`
- DisMech entries: `kb/disorders/*.yaml`
- Review date: 2026-07-07

## Batch 1

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 1 | PAH-related Phenylalanine hydroxylase deficiency | MAPPED | High concordance with `Phenylketonuria.yaml`; minor IEMbase-only lab and clinical detail. |
| 3 | GCH1-related GTP cyclohydrolase I deficiency, autosomal recessive | UNMAPPED | False negative; local subtype coverage exists under BH4 and catecholamine-synthesis umbrellas. |
| 4 | PTS-related 6-pyruvoyl-tetrahydropterin synthase deficiency | MAPPED | Correct subtype mapping; local coverage is good at umbrella level but lacks subtype-specific pterin/enzyme detail. |
| 5 | QDPR-related dihydropteridine reductase deficiency | MAPPED | Correct subtype mapping; local coverage is good but DHPR-specific imaging/EEG and pterin details are sparse. |
| 6 | PCBD1-related pterin carbinolamine-4a-dehydratase deficiency | UNMAPPED | False negative; local `PCD Deficiency` subtype exists, with phenotype/biochemical gaps. |
| 7 | GCH1-related GTP cyclohydrolase I deficiency, autosomal dominant | UNMAPPED | False negative; local AD dopa-responsive dystonia entry is the best target. |
| 8 | SPR-related sepiapterin reductase deficiency | AMBIGUOUS | Both local umbrellas are defensible; choose one canonical mapping and keep the other as secondary context. |
| 9 | SLC22A5-related primary carnitine deficiency | MAPPED | High concordance; local DisMech is broader clinically, IEMbase is richer for acylcarnitine panels. |
| 11 | CPS1-related carbamoyl phosphate synthetase I deficiency | AMBIGUOUS | Standalone disease is the curation target; umbrella subtype causes duplicate exact match. |
| 12 | NAGS-related N-acetylglutamate synthase deficiency | AMBIGUOUS | Standalone disease is the curation target; umbrella subtype causes duplicate exact match. |

## Batch 2

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 13 | OTC-related ornithine transcarbamylase deficiency | AMBIGUOUS | Standalone OTC deficiency is canonical; umbrella UCD subtype causes duplicate match. |
| 14 | ASS1-related argininosuccinate synthetase deficiency | AMBIGUOUS | Standalone citrullinemia type I is canonical; umbrella UCD subtype causes duplicate match. |
| 15 | ASL-related argininosuccinate lyase deficiency | AMBIGUOUS | Standalone argininosuccinic aciduria is canonical; umbrella UCD subtype causes duplicate match. |
| 16 | ARG1-related arginase 1 deficiency | MAPPED | Correct mapping; high concordance, with DisMech richer for chronic neurologic sequelae and pegzilarginase. |
| 17 | SLC25A15-related mitochondrial ornithine transporter deficiency | MAPPED | Correct HHH mapping; high concordance, with IEMbase adding fibroblast assay, factor, and dialysis detail. |
| 18 | SLC25A13-related citrin deficiency | MAPPED | Correct mapping; high concordance, with IEMbase richer for neonatal labs and diet-avoidance details. |
| 19 | FAH-related fumarylacetoacetase deficiency | MAPPED | Correct HT1 mapping; high concordance, with IEMbase adding ocular, renal, and lab-compartment detail. |
| 20 | TAT-related tyrosine aminotransferase deficiency | CANDIDATE | False positive to HT1; local standalone tyrosinemia type II/TAT deficiency is missing. |
| 21 | HPD-related 4-hydroxyphenylpyruvate dioxygenase deficiency | UNMAPPED | Local standalone tyrosinemia type III/HPD deficiency is missing; alkaptonuria candidate is false positive. |
| 22 | HPD-related Hawkinsinuria | UNMAPPED | Local standalone Hawkinsinuria is missing; alkaptonuria candidate is false positive. |

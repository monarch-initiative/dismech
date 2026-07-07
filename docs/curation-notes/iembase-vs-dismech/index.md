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

## Batch 3

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 23 | HGD-related homogentisic acid oxidase deficiency | MAPPED | Correct alkaptonuria mapping; high concordance, with DisMech substantially richer overall. |
| 24 | MAT1A-related methionine adenosyltransferase I-III deficiency | MAPPED | Correct MAT I/III subtype mapping; IEMbase adds granular neurologic and ratio-marker detail. |
| 25 | GNMT-related glycine N-methyltransferase deficiency | UNMAPPED | No valid local target; GAMT deficiency is a false-positive fuzzy candidate. |
| 26 | AHCY-related S-adenosylhomocysteine hydrolase deficiency | UNMAPPED | No valid local target; CESD is a false-positive fuzzy candidate. |
| 27 | CBS-related cystathionine beta-synthase deficiency | MAPPED | Correct homocystinuria mapping; high concordance, with IEMbase adding selected diagnostic markers. |
| 28 | CTH-related cystathionine gamma-lyase deficiency | UNMAPPED | No valid local target; homocystinuria is a misleading pathway-neighbor candidate. |
| 29 | SUOX-related isolated sulfite oxidase deficiency | UNMAPPED | No valid local target; SCO1-related COX deficiency is a false-positive fuzzy candidate. |
| 30 | MTR-related methionine synthase deficiency | MAPPED | Correct cblG subtype mapping; DisMech covers the umbrella but lacks some cblG-specific labs/imaging. |
| 31 | MTRR-related methionine synthase reductase deficiency, cblE | MAPPED | Correct cblE subtype mapping; DisMech covers the umbrella but lacks some cblE-specific labs/imaging. |
| 32 | GLDC-related nonketotic hyperglycinemia | MAPPED | Correct NKH mapping; high concordance, with IEMbase richer for specific EEG and MRI subfeatures. |

## Batch 4

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 33 | PHGDH-related 3-phosphoglycerate dehydrogenase deficiency | UNMAPPED | No valid local target; missing serine-biosynthesis disorder, not a NKH or PHGDH-cancer-metabolism match. |
| 34 | PSPH-related phosphoserine phosphatase deficiency | UNMAPPED | No valid local target; PDH phosphatase deficiency is a lexical false-positive candidate. |
| 35 | PSAT1-related phosphoserine aminotransferase deficiency | UNMAPPED | No valid local target; ornithine aminotransferase deficiency is a false-positive aminotransferase candidate. |
| 36 | ABAT-related GABA transaminase deficiency | UNMAPPED | No valid local target; GEFS+ and SSADH are GABA-related but mechanistically distinct. |
| 37 | ALDH5A1-related succinic semialdehyde dehydrogenase deficiency | MAPPED | Correct SSADH mapping; high concordance, with IEMbase adding granular EEG/MRI detail and DisMech adding vigabatrin cautions. |
| 38 | ALDH4A1-related pyrroline-5-carboxylate dehydrogenase deficiency | UNMAPPED | No valid local target; PDH deficiency and ALDH18A1 P5CS deficiency are false-positive neighbors. |
| 39 | SLC36A2/SLC6A20/SLC6A19-related iminoglycinuria | UNMAPPED | No valid local target; not Hartnup disease despite partial SLC6A19 overlap. |
| 40 | PRODH-related proline dehydrogenase deficiency | UNMAPPED | No valid local target; benign hyperprolinemia type I should not map to 22q11.2 deletion syndrome. |
| 41 | GLUL-related glutamine synthetase deficiency | UNMAPPED | No valid local target; LIAS deficiency is a false-positive synthetase/encephalopathy candidate. |
| 42 | ALDH18A1-related pyrroline-5-carboxylate synthetase deficiency, SPG9A | AMBIGUOUS | Resolve to `ALDH18A1_De_Barsy_Spectrum.yaml#SPG9A`; parent spectrum remains context. |

## Batch 5

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 43 | AASS-related alpha-aminoadipic semialdehyde synthase deficiency | UNMAPPED | No valid local target; primary AASS hyperlysinemia/saccharopinuria is not SSADH deficiency or NADK2-related DECR deficiency. |
| 45 | HAL-related histidine ammonia-lyase deficiency | UNMAPPED | No valid local target; HMGCL deficiency is a false-positive aciduria/ketone neighbor. |
| 46 | UROC1-related urocanase deficiency | UNMAPPED | No valid local target; urocanic aciduria should not map to UMPS hereditary orotic aciduria. |
| 47 | FTCD-related formimidoyltransferase cyclodeaminase deficiency | UNMAPPED | No valid local target; FIGLU/formiminoglutamic aciduria should not map to hereditary orotic aciduria. |
| 48 | SLC3A1-related cystinuria type A | MAPPED | Correct cystinuria mapping; prefer `Cystinuria.yaml#Cystinuria type A` if subtype anchors are supported. |
| 49 | SLC1A1-related dicarboxylic aminoaciduria | UNMAPPED | No valid local target; distinct from Hartnup neutral aminoaciduria and cystinuria dibasic/cystine transport disease. |
| 50 | SLC6A19-related Hartnup disorder | MAPPED | Correct Hartnup mapping; high concordance, with DisMech richer for mechanism, biomarkers, and management. |
| 51 | SLC7A7-related lysinuric protein intolerance | UNMAPPED | No valid local target; high-priority future curation, and not Hartnup or cystinuria. |
| 52 | PEPD-related prolidase deficiency | UNMAPPED | No valid local target; future standalone PEPD/iminodipeptiduria curation would be clinically rich. |
| 53 | CNDP1-related carnosine dipeptidase 1 deficiency | UNMAPPED | No valid local target; benign/minimal biochemical carnosinemia and homocarnosinosis record. |

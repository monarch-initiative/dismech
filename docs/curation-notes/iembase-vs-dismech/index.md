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

## Batch 6

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 55 | BCKDHA-related branched-chain ketoacid dehydrogenase E1-alpha deficiency | UNMAPPED | False negative; resolve to `Maple_Syrup_Urine_Disease.yaml#Type IA` when subtype anchors are supported. |
| 56 | IVD-related isovaleryl-CoA dehydrogenase deficiency | MAPPED | Correct IVA mapping; high concordance, with IEMbase adding granular lab, MRI, and cytopenia detail. |
| 57 | MCCC1-related 3-methylcrotonyl-CoA carboxylase 1 deficiency | CANDIDATE | Accept candidate as correct file-level mapping to `3-Methylcrotonyl-CoA_Carboxylase_Deficiency.yaml`; local file covers MCCC1/MCCC2 jointly. |
| 58 | AUH-related 3-methylglutaconyl-CoA hydratase deficiency | UNMAPPED | No valid local target; GA1/GCDH is a false-positive fuzzy neighbor for AUH/MGA1. |
| 59 | TAZ-related Barth syndrome | MAPPED | Correct Barth syndrome mapping; high concordance, with IEMbase adding selected facial, oral-ulcer, sepsis, and clot/stroke detail. |
| 60 | OPA3-related methylglutaconic aciduria type 3 | UNMAPPED | No valid local target; GA1/GCDH is a false-positive fuzzy neighbor for OPA3/Costeff syndrome. |
| 62 | HMGCL-related 3-hydroxy-3-methylglutaryl-CoA lyase deficiency | MAPPED | Correct HMGCLD mapping; high concordance, with IEMbase adding C6DC, enzyme-assay, and crisis-imaging detail. |
| 63 | ACADSB-related 2-methylbutyryl-CoA dehydrogenase deficiency | MAPPED | Correct SBCADD mapping; high concordance, with explicit C5-isomer distinction from IVA. |
| 64 | HSD17B10-related 17-beta-hydroxysteroid dehydrogenase type 10 deficiency | UNMAPPED | False negative; local `HSD10_Mitochondrial_Disease.yaml` is the correct target despite low fuzzy score. |
| 66 | HIBCH-related 3-hydroxyisobutyryl-CoA hydrolase deficiency | MAPPED | Correct HIBCH mapping; high concordance, with IEMbase adding fibroblast assay and granular valine-pathway markers. |

## Batch 7

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 67 | HIBADH-related 3-hydroxyisobutyrate dehydrogenase deficiency | CANDIDATE | False positive to SSADH deficiency; local standalone HIBADH/3-hydroxyisobutyric aciduria target is missing. |
| 68 | PCCA-related Propionic acidemia | MAPPED | Correct propionic acidemia mapping; high concordance, with PCCA covered inside the PCCA/PCCB disease entry. |
| 69 | MMUT-related Methylmalonic aciduria due to methylmalonyl-CoA mutase deficiency | MAPPED | Correct MMA mapping; high concordance, with MMUT mut0/mut- coverage inside the isolated MMA entry. |
| 70 | SLC46A1-related Proton-coupled folate transporter deficiency | UNMAPPED | No valid local target; primary carnitine deficiency is a false-positive transporter/treatability neighbor. |
| 71 | FOLR1-related Folate receptor alpha deficiency | UNMAPPED | No valid local target; PDH deficiency and secondary DHPR cerebral folate deficiency are not primary FOLR1 disease. |
| 72 | MTHFR-related 5,10-methylenetetrahydrofolate reductase deficiency | UNMAPPED | False negative; local MTHFR subtype/branch coverage exists under methionine-cycle disorder and homocystinuria entries. |
| 73 | DHFR-related Dihydrofolate reductase deficiency | UNMAPPED | No valid local target; DHPR/QDPR deficiency and antimicrobial DHFR modules are false-positive folate/acronym neighbors. |
| 75 | ALDH7A1-related Alpha-amino adipic semialdehyde dehydrogenase deficiency | UNMAPPED | No valid local target; SSADH deficiency is a false-positive semialdehyde dehydrogenase neighbor. |
| 76 | PNPO-related Pyridoxamine 5-phosphate oxidase deficiency | UNMAPPED | No valid local target; COA3-related COX deficiency is a false-positive mitochondrial/deficiency neighbor. |
| 77 | MOCS1-related Molybdenum cofactor deficiency A | UNMAPPED | No valid local target; Fanconi anemia FA-A is a false-positive complementation-group acronym collision. |

## Batch 8

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 78 | MOCS2-related Molybdopterin synthase deficiency | UNMAPPED | No valid local target; PTPS/tetrahydrobiopterin deficiency is a false-positive pterin-neighbor candidate. |
| 79 | GPHN-related Molybdenum cofactor deficiency C | UNMAPPED | No valid MoCo-C target; local GPHN hyperekplexia content is a gene collision, not molybdenum cofactor disease. |
| 80 | CBLIF-related Intrinsic factor deficiency | MAPPED | Correct intrinsic factor deficiency mapping; high concordance, with DisMech stronger for mechanism and treatment rationale. |
| 82 | CUBN-related Cubilin deficiency | UNMAPPED | No valid Imerslund-Grasbeck target; hereditary orotic aciduria is a false-positive megaloblastic-anemia neighbor. |
| 83 | AMN-related Amnionless deficiency | UNMAPPED | No valid Imerslund-Grasbeck target; hereditary orotic aciduria is a false-positive megaloblastic-anemia neighbor. |
| 84 | TCN1-related Haptocorrin deficiency | UNMAPPED | No valid TCN1/haptocorrin target; PDH E3-binding protein deficiency is a false positive, and disease-entry scope needs review. |
| 85 | TCN2-related Transcobalamin 2 deficiency | MAPPED | Correct TCN2 subtype mapping; high concordance, with IEMbase adding chronic diarrhea, apathy, and cyanocobalamin detail. |
| 86 | MMAA-related Methylmalonic aciduria, cblA type | MAPPED | Correct cblA subtype mapping; use methylmalonic acidemia as secondary phenotype/treatment context. |
| 87 | MMAB-related Methylmalonic aciduria, cblB type | MAPPED | Correct cblB subtype mapping; use methylmalonic acidemia as secondary phenotype/treatment context. |
| 88 | MMADHC-related Methylmalonic aciduria, cblDv2 type | UNMAPPED | False negative; resolve to the cobalamin umbrella's cblD subtype, with optional future cblD-v2 subtype split. |

## Batch 9

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 89 | MMADHC-related Homocystinuria, cblDv1 type | UNMAPPED | False negative; resolve to the cobalamin umbrella's cblD subtype, with optional future cblD-HC subtype split. |
| 90 | MMACHC-related Methylmalonic aciduria and homocystinuria, cblC type | MAPPED | Mapped to the cobalamin umbrella, but the standalone cblC entry is the better canonical target. |
| 91 | LMBRD1-relasted Methylmalonic aciduria and homocystinuria, cblF type | MAPPED | Correct cblF subtype mapping; high concordance, with IEMbase adding cblF-specific lab-compartment detail. |
| 92 | CD320-related Transcobalamin receptor defect | UNMAPPED | No valid local target; methylmalonic acidemia is a false-positive fuzzy candidate and the cobalamin umbrella lacks CD320. |
| 93 | BTD-related Biotinidase deficiency | MAPPED | Correct biotinidase deficiency mapping; high concordance, with IEMbase adding selected oral and mitral-valve clinical rows. |
| 94 | HLCS-related Holocarboxylase synthetase deficiency | MAPPED | Correct HLCS mapping; high concordance, with IEMbase adding ataxia and mitral valvulitis as phenotype review targets. |
| 95 | SLC19A2-related Thiamine transporter 1 deficiency | UNMAPPED | No valid local TRMA/Rogers syndrome target; SLC19A2 appears only as secondary monogenic-diabetes context. |
| 96 | AGXT-related Alanine-glyoxylate aminotransferase deficiency (peroxisomal) | UNMAPPED | False negative; resolve to `Primary_Hyperoxaluria_Type_1.yaml`, not the ornithine aminotransferase false-positive candidate. |
| 97 | GRHPR-related Glyoxylate reductase/hydroxypyruvate reductase deficiency | UNMAPPED | False negative; resolve to `Primary_Hyperoxaluria_Type_2.yaml`, not the pyruvate dehydrogenase false-positive candidate. |
| 99 | TH-related Tyrosine hydroxylase deficiency | AMBIGUOUS | Resolve to `Autosomal_Recessive_Dopa_Responsive_Dystonia.yaml`; catecholamine synthesis and DRD umbrellas are secondary context. |

## Batch 10

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 100 | DDC-related Aromatic L-amino acid decarboxylase deficiency | AMBIGUOUS | Standalone AADC deficiency is canonical; catecholamine-synthesis umbrella subtype is secondary context. |
| 101 | DBH-related Dopamine beta-hydroxylase deficiency | UNMAPPED | No valid local target; congenital adrenal hyperplasia 11B-OHD is a beta-hydroxylase lexical false positive. |
| 102 | MAOA-related Monoamine oxidase A deficiency | UNMAPPED | No valid local target; needs future MAOA/monoamine catabolism scope, not catecholamine synthesis or chronic granulomatous disease. |
| 103 | SLC6A3-related Dopamine transporter deficiency | MAPPED | Correct infantile parkinsonism-dystonia mapping; high concordance, with DisMech richer for mechanism and treatment caveats. |
| 104 | GAMT-related Guanidinoacetate methyltransferase deficiency | MAPPED | Correct GAMT mapping; high concordance, with IEMbase adding specimen-compartment detail and osteoporosis as a review target. |
| 105 | GATM-related Arginine:glycine amidinotransferase deficiency | MAPPED | Correct AGAT mapping; high concordance, with IEMbase adding urinary creatine/creatinine ratio and compartment-specific GAA rows. |
| 106 | SLC6A8-related Creatine transporter deficiency | CANDIDATE | Generated AGAT candidate is false; correct target is `Creatine_Transporter_Deficiency.yaml`. |
| 107 | FECH-related Ferrochelatase deficiency | MAPPED | Correct current target is inherited porphyria's EPP subtype; IEMbase adds FECH-specific iron/ferritin and microcytosis detail. |
| 108 | ALAS2-related Erythroid 5-aminolevulinate synthase superactivity | UNMAPPED | False negative to inherited porphyria EPP/X-linked protoporphyria branch; future XLP split may be warranted. |
| 109 | PPOX-related Protoporphyrinogen oxidase deficiency | UNMAPPED | False negative; resolve to inherited porphyria's variegate porphyria subtype, with future standalone VP curation possible. |

## Batch 11

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 110 | ALAS2-related Erythroid 5-aminolevulinate synthase deficiency | UNMAPPED | True gap; do not conflate ALAS2 deficiency/X-linked sideroblastic anemia with ALAS2 superactivity/X-linked protoporphyria. |
| 111 | UROS-related Uroporphyrinogen III synthase deficiency | MAPPED | Correct CEP subtype mapping; DisMech stronger for mechanism and complications, IEMbase adds type I porphyrin isomers and dental/urine signs. |
| 112 | HMBS-related Porphobilinogen deaminase deficiency | MAPPED | Correct standalone AIP mapping; high concordance, with IEMbase adding renal, hepatic, cancer-risk, and broader neuropsychiatric review targets. |
| 113 | CPOX-related Coproporphyrinogen oxidase deficiency | MAPPED | Correct HCP subtype mapping; IEMbase adds HCP-specific stool coproporphyrin III and attack-detail granularity. |
| 114 | UROD-related Hepatic uroporphyrinogen decarboxylase deficiency | UNMAPPED | False negative to UROD-related PCT/HEP subtypes, but the IEMbase label spans multiple UROD-related categories. |
| 115 | ALAD-related Delta-aminolevulinate dehydratase deficiency | MAPPED | Correct standalone ADP mapping; high biochemical concordance, with IEMbase adding autonomic/renal/severe-attack details. |
| 116 | STAR-related Steroidogenic acute regulatory protein deficiency | UNMAPPED | False negative to `Congenital_Adrenal_Hyperplasia.yaml#Lipoid CAH`; needs STAR-specific biochemical and 46,XY undervirilization detail. |
| 117 | CYP17A1-related 17-alpha-Hydroxylase deficiency | MAPPED | Correct `17A-OHD` subtype mapping; IEMbase adds steroid/mineralocorticoid precursor profile granularity. |
| 118 | HSD3B2-related 3-beta-Hydroxysteroid dehydrogenase deficiency | MAPPED | Correct `3B-HSD` subtype mapping, but local subtype-specific mechanism/biochemical coverage is thin. |
| 119 | CYP21A2-related 21-Hydroxylase deficiency | MAPPED | Correct CAH/21-OHD mapping with strong local coverage; IEMbase adds granular ACTH/renin/electrolyte/androgen biomarkers. |

## Batch 12

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 120 | CYP11B1-related 11-beta-Hydroxylase type 1 deficiency | MAPPED | Correct CAH mapping, with subtype resolution to `Congenital_Adrenal_Hyperplasia.yaml#11B-OHD`; IEMbase adds CYP11B1 steroid/electrolyte detail. |
| 122 | CYP11B1-related 11-beta-Hydroxylase superactivity | MAPPED | Correct standalone familial hyperaldosteronism type I mapping; high concordance for aldosterone, 18-oxocortisol, hypokalemia, and dexamethasone suppression. |
| 123 | HSD11B2-related 11-beta-Hydroxysteroid dehydrogenase 2 deficiency | CANDIDATE | False-positive HSD17B3 DSD candidate; HSD11B2 apparent mineralocorticoid excess is a true local disease gap. |
| 124 | H6PD-related Hexose-6-phosphate dehydrogenase deficiency | MAPPED | Correct cortisone reductase deficiency mapping, specifically the H6PD/apparent CRD subtype; IEMbase adds THF/THE-ratio and ACTH/androgen detail. |
| 125 | CYP17A1-related 17,20-Lyase deficiency | UNMAPPED | Partial false negative to the local CYP17A1 CAH branch, but isolated 17,20-lyase deficiency should remain distinct from combined 17A-OHD coverage. |
| 126 | HSD17B3-related 17-beta-Hydroxysteroid dehydrogenase deficiency | MAPPED | Correct 46,XY HSD17B3 DSD mapping; DisMech is clinically richer and IEMbase adds explicit gonadotropin elevation. |
| 127 | SRD5A2-related Steroid 5-alpha-reductase type 2 deficiency | CANDIDATE | Accept generated candidate as correct SRD5A2 DSD mapping; IEMbase adds urinary 5-alpha/5-beta metabolite-ratio detail. |
| 128 | CYP19A1-related Aromatase deficiency | MAPPED | Correct aromatase deficiency mapping; DisMech is richer for estrogen deficiency, androgen excess, bone, metabolic, and treatment coverage. |
| 129 | AR-related Androgen receptor deficiency | MAPPED | Correct current CAIS target, with a broader AIS label-scope caveat; IEMbase adds normal DHT as a useful differentiator. |
| 130 | ESR1-related Estrogen receptor deficiency | UNMAPPED | True local disease gap; do not map estrogen resistance to aromatase deficiency, ESR1 cancer contexts, PMDD, or osteoporosis-risk content. |

## Batch 13

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 131 | PGR-related Progesterone receptor deficiency | UNMAPPED | True local gap; PGR mentions in tumors/endometriosis are signaling context, not monogenic progesterone receptor deficiency. |
| 132 | NR3C1-related Glucocorticoid receptor deficiency | UNMAPPED | True local gap; do not map glucocorticoid resistance to familial hyperaldosteronism or CSCR glucocorticoid-risk context. |
| 133 | NR3C2-related Mineralocorticoid receptor deficiency | UNMAPPED | True local gap for pseudohypoaldosteronism type 1; high renin/aldosterone with salt wasting is not familial hyperaldosteronism. |
| 134 | BCAT2-related Branched-chain aminotransferase 2 deficiency | UNMAPPED | True local gap; MSUD is pathway context only and ornithine aminotransferase deficiency is a false lexical candidate. |
| 135 | ACAD8-related Isobutyryl-CoA dehydrogenase deficiency | MAPPED | Correct IBDD mapping with strong local coverage; IEMbase reinforces C4 acylcarnitine, isobutyrylglycine, free carnitine, asymptomatic course, anemia, and cardiomyopathy. |
| 136 | ALDH6A1-related Methylmalonate semialdehyde dehydrogenase deficiency | UNMAPPED | True local gap; SSADH/ALDH5A1 is a false semialdehyde-dehydrogenase neighbor and HIBCH is only valine-pathway context. |
| 137 | LTC4S-related Leukotriene C4 synthase deficiency | UNMAPPED | True local gap; generated HMG-CoA synthase neighbor is a synthase lexical false positive, not leukotriene biosynthesis disease. |
| 139 | DPEP1-related Dipeptidase deficiency | UNMAPPED | True local gap for cystinylglycinuria; do not map to cystinuria or other cystine-transporter disease. |
| 140 | ADSL-related Adenylosuccinate lyase deficiency | MAPPED | Correct ADSL mapping with strong local coverage; IEMbase adds specimen-specific SAICA riboside/succinyladenosine detail and cerebellar hypoplasia wording to review. |
| 141 | ATIC-related AICAR transformylase-IMP cyclohydrolase deficiency | UNMAPPED | True local gap; ADSL is purine-pathway context only, and the catecholamine-synthesis candidate is false. |

## Batch 14

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 142 | ADA-related Adenosine deaminase deficiency | MAPPED | Correct ADA-SCID subtype mapping under severe combined immunodeficiency; IEMbase adds skeletal and compartment-specific biomarker detail. |
| 143 | DGUOK-related Mitochondrial deoxyguanosine kinase deficiency | CANDIDATE | False-positive TWNK/MTDPS7 candidate; no valid local DGUOK/MTDPS3 target exists. |
| 144 | AMPD1-related Myoadenylate deaminase deficiency | UNMAPPED | True local gap; ADA deficiency is a false purine-pathway neighbor. |
| 145 | HPRT1-related Hypoxanthine guanine phosphoribosyltransferase deficiency | MAPPED | Correct Lesch-Nyhan/HPRT1 mapping; IEMbase adds granular hypoxanthine, xanthine, and AICA riboside biomarker leads. |
| 146 | APRT-related Adenine phosphoribosyl transferase deficiency | MAPPED | Correct APRT deficiency mapping with high concordance for enzyme defect, 2,8-DHA, urolithiasis, and renal injury. |
| 147 | PRPS1-related Phosphoribosyl pyrophosphate synthetase 1 deficiency | MAPPED | Correct Arts syndrome leaf mapping, with `PRPS1_Deficiency_Spectrum.yaml` as broader context for the CMTX5/DFN continuum. |
| 149 | PNP-related Purine nucleoside phosphorylase deficiency | UNMAPPED | True local gap; IKBKG/IMD33 is an immunodeficiency-label false positive. |
| 150 | RRM2B-related Mitochondrial ribonucleotide reductase subunit 2 deficiency | UNMAPPED | Partial false negative: local RRM2B MNGIE-like subtype exists, but no canonical MTDPS8A/8B target. |
| 151 | TPMT-related Thiopurine S-methyltransferase deficiency | UNMAPPED | Unmapped scope-review item; pharmacogenetic thiopurine intolerance should not map to GAMT deficiency. |
| 152 | UMPS-related Uridine monophosphate synthase deficiency | MAPPED | Correct hereditary orotic aciduria mapping; IEMbase adds plasma orotic acid, smear terms, and renal-row review targets. |

## Batch 15

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 154 | NT5C3A-related Pyrimidine-5'-nucleotidase I deficiency | UNMAPPED | True local gap; hereditary orotic aciduria is a UMPS false neighbor and lead poisoning is acquired mechanism context only. |
| 155 | DHODH-related Dihydroorotate dehydrogenase deficiency | UNMAPPED | True local gap for Miller syndrome/POADS; pyruvate dehydrogenase deficiency is a broad metabolic false candidate. |
| 156 | NT5C3A-related Pyrimidine 5'-nucleotidase superactivity | UNMAPPED | True local gap distinct from NT5C3A deficiency; hereditary orotic aciduria does not cover low PRPP/increased UMP hydrolase. |
| 157 | TYMP-related Thymidine phosphorylase deficiency | AMBIGUOUS | Resolve to standalone `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml`; CIPO mitochondrial subtype is secondary context. |
| 158 | TK2-related Mitochondrial thymidine kinase 2 deficiency | CANDIDATE | False-positive MNGIE candidate; no valid local TK2/MTDPS2 target, and local TK2 SCA31 repeat context is unrelated. |
| 159 | DPYD-related Dihydropyrimidine dehydrogenase deficiency | UNMAPPED | True local gap with pharmacogenetic overlap; chemotherapy-induced diarrhea covers DPYD toxicity risk, not DPYD deficiency. |
| 160 | UPB1-related Beta-Ureidopropionase deficiency | UNMAPPED | True local gap; beta-ketothiolase deficiency is an ACAT1 isoleucine/ketolysis false candidate. |
| 163 | GCDH-related Glutaryl-CoA dehydrogenase deficiency | MAPPED | Correct GA1 mapping; high concordance, with IEMbase adding glutaconic acid and several rare phenotype review targets. |
| 164 | ASPA-related Aspartoacylase deficiency | MAPPED | Correct Canavan mapping; high concordance, with IEMbase adding CSF/plasma NAA and specific MRI/posture review targets. |
| 165 | L2HGDH-related L-2-Hydroxyglutarate dehydrogenase deficiency | MAPPED | Correct L2HGA mapping; high concordance, with IEMbase adding lysine, neonatal ammonia/lactate, CSF protein, and choreoathetosis leads. |

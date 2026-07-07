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

## Batch 16

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 166 | D2HGDH-related D-2-Hydroxyglutarate dehydrogenase deficiency | MAPPED | Correct D-2-HGA mapping; high concordance for type I D2HGDH disease, with subtype-specific absence of cardiomyopathy noted. |
| 167 | IDH2-related mitochondrial NADP+-dependent isocitrate dehydrogenase 2 superactivity | MAPPED | Correct D-2-HGA mapping; high concordance for type II IDH2 disease, including D-2-HG accumulation and cardiomyopathy. |
| 170 | SARDH-related sarcosine dehydrogenase deficiency | UNMAPPED | True local gap; isovaleric acidemia is a false pathway-neighbor candidate. |
| 172 | ETHE1-related mitochondrial sulfur dioxygenase deficiency | UNMAPPED | True local gap; chronic traumatic encephalopathy is a lexical false candidate, not ethylmalonic encephalopathy. |
| 173 | OGDH-related alpha-ketoglutarate dehydrogenase deficiency | UNMAPPED | True local gap; D-2-HGA is an alpha-ketoglutarate pathway-neighbor false candidate. |
| 174 | FH-related fumarate hydratase deficiency | MAPPED | Generated mapping to familial hyperaldosteronism type I is false via `FH1`; local fumarase deficiency target is missing. |
| 175 | OXCT1-related succinyl-CoA:3-oxoacid CoA transferase deficiency | UNMAPPED | True local gap; lipoyl transferase 1 deficiency is not a SCOT/ketolysis target. |
| 176 | HMGCS2-related 3-hydroxy-3-methylglutaryl-CoA synthase deficiency | MAPPED | Correct HMGCS2 mapping; high concordance, with IEMbase adding crotonylglycine and differential acylcarnitine details. |
| 177 | MLYCD-related malonyl-CoA decarboxylase deficiency | MAPPED | Generated mapping to migraine with aura is false via `MA`; local MLYCD/malonic aciduria target is missing. |
| 179 | HSD3B7-related 3beta-hydroxy-Delta5-C27-steroid dehydrogenase-isomerase deficiency | UNMAPPED | False negative; resolve to `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 1`. |

## Batch 17

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 180 | AKR1D1-related Delta4-3-oxosteroid-5beta-reductase deficiency | CANDIDATE | Accept candidate as correct BASD type 2 subtype; high concordance, with IEMbase adding granular allocholic/3-oxo bile acids and CDCA/UDCA treatment rows. |
| 181 | CYP7B1-related oxysterol 7alpha-hydroxylase deficiency | CANDIDATE | Accept candidate as correct BASD type 3 subtype; high concordance, with IEMbase adding 27-hydroxycholesterol, glucose/vitamin E, ocular, and MRI detail. |
| 182 | CYP7A1-related cholesterol 7alpha-hydroxylase deficiency | CANDIDATE | False positive to BASD type 3; CYP7A1 adult dyslipidemia/gallstone disease is a true local gap. |
| 183 | CYP27A1-related sterol 27-hydroxylase deficiency | MAPPED | Correct CTX mapping; high concordance, with IEMbase adding endocrine, cardiovascular, gallstone, and cholestane pentol glucuronide details. |
| 184 | SLC27A5-related bile acid-CoA ligase deficiency | UNMAPPED | Partial local umbrella coverage, but no valid SLC27A5 subtype; BAAT conjugation defect candidate is related but not equivalent. |
| 185 | ATP8B1-related progressive familial intrahepatic cholestasis type 1 | UNMAPPED | True local gap; progressive familial heart block candidate is a lexical false positive. |
| 186 | ABCB11-related progressive familial intrahepatic cholestasis type 2 | UNMAPPED | True local gap; progressive familial heart block candidate is a lexical false positive. |
| 187 | BAAT-related bile acid-CoA:aminoacid N-acyltransferase deficiency | UNMAPPED | False negative; resolve to `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#Bile acid conjugation defect 1`. |
| 188 | AMACR-related alpha-methylacyl-CoA racemase deficiency | MAPPED | Correct BASD type 4 mapping; high concordance, with IEMbase adding granular bile acid/fatty acid analytes and neurologic/retinal details. |
| 189 | TALDO1-related transaldolase deficiency | MAPPED | Correct transaldolase deficiency mapping; high concordance, with IEMbase adding erythronic acid, respiratory-chain/ferritin/glucose, and genital/endocrine details. |

## Batch 18

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 190 | RPIA-related ribose-5-phosphate isomerase deficiency | UNMAPPED | True local gap; G6PD deficiency is a pentose-phosphate pathway-neighbor false candidate. |
| 191 | MVK-related mevalonate kinase deficiency (mild) | MAPPED | Correct HIDS subtype mapping; high concordance, with DisMech much richer for inflammasome mechanism and IL-1-targeted treatment. |
| 192 | DHCR7-related Smith-Lemli-Opitz syndrome | MAPPED | Correct SLOS mapping; high concordance, with IEMbase adding 8-DHC, dental/digital-whorl/photosensitivity, and renal/GI/pulmonary detail. |
| 193 | EBP-related chondrodysplasia punctata 2 | UNMAPPED | True local gap; RCDP1 and tibial-metacarpal chondrodysplasia punctata are distinct from EBP/CDPX2. |
| 194 | NSDHL-related CHILD syndrome | UNMAPPED | True local gap; congenital ichthyosis is only a partial skin-overlap false candidate. |
| 195 | DHCR24-related desmosterolosis | UNMAPPED | True local gap; CAH 3B-HSD is a lexical false candidate driven by 3beta wording. |
| 196 | SC5D-related lathosterolosis | UNMAPPED | True local gap; CTX is a sterol/bile-acid pathway neighbor but not SC5D lathosterolosis. |
| 197 | LBR-related Greenberg skeletal dysplasia | UNMAPPED | True local gap; sepiapterin reductase deficiency is an unrelated false candidate. |
| 198 | POR-related cytochrome P450 oxidoreductase deficiency | MAPPED | Generated amniotic band syndrome mapping is false via ABS acronym; local HRS file is only partial Antley-Bixler/POR context. |
| 199 | ATP7A-related Menkes disease | MAPPED | Correct Menkes mapping; high concordance, with IEMbase adding copper-compartment, hypothermia, cytopenia, ocular, and arterial-rupture details. |

## Batch 19

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 200 | ATP7A-related occipital horn syndrome | MAPPED | Correct OHS subtype mapping under Menkes disease; high concordance, with IEMbase adding diarrhea, orthostatic hypotension, and urinary-infection leads. |
| 201 | ATP7B-related Wilson disease | MAPPED | Correct Wilson disease mapping; high concordance, with IEMbase adding selected granular lab and clinical rows. |
| 202 | SLC39A4-related acrodermatitis enteropathica | UNMAPPED | True local gap; unrelated zinc-associated entries are not valid SLC39A4 disease targets. |
| 203 | HFE-related hereditary hemochromatosis type 1 | UNMAPPED | False negative; resolve to `Hemochromatosis.yaml#Type 1`. |
| 204 | HJV-related hemojuvelin deficiency | CANDIDATE | Accept candidate as correct hemochromatosis type 2A subtype coverage. |
| 205 | Neonatal hemochromatosis | UNMAPPED | True local gap; do not conflate congenital alloimmune neonatal liver disease with hereditary hemochromatosis. |
| 206 | TF-related hereditary transferrin deficiency | UNMAPPED | True local gap; atransferrinemia is mechanistically distinct from hepcidin-deficient hemochromatosis. |
| 208 | BCS1L-related GRACILE syndrome | UNMAPPED | True local gap; CALFAN syndrome is a false-positive liver/neurodevelopmental neighbor. |
| 209 | PANK2-related pantothenate kinase 2 deficiency | MAPPED | Correct PKAN mapping; high concordance, with IEMbase adding brain-iron, eye-movement, and spiculated-red-cell review leads. |
| 210 | FMO3-related primary trimethylaminuria | UNMAPPED | True local gap; erythromelalgia is a lexical false positive and DMGDH deficiency is only a fish-odor differential. |

## Batch 20

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 211 | DMGDH-related dimethylglycine dehydrogenase deficiency | MAPPED | Correct DMGDH mapping; high concordance, with an OMIM cross-reference discrepancy noted for later metadata review. |
| 213 | KCNJ11-related ATP-sensitive potassium channel pore-forming subunit deficiency | UNMAPPED | False negative; resolve to `Congenital_Isolated_Hyperinsulinism.yaml`, preferably KATP/HHF2 subtype coverage. |
| 214 | GGT1-related gamma-glutamyl transpeptidase deficiency | UNMAPPED | True local gap; LIPT1 deficiency is a mitochondrial lipoylation false candidate. |
| 215 | OPLAH-related 5-oxoprolinase deficiency | MAPPED | Correct OPLAH mapping; high concordance, with IEMbase adding renal colic and urolithiasis review leads. |
| 216 | GCLC-related gamma-glutamylcysteine synthetase deficiency | UNMAPPED | True local gap; CPS1 deficiency is a synthetase-word false candidate. |
| 217 | GSS-related glutathione synthetase deficiency, mild | UNMAPPED | True local gap; hereditary orotic aciduria is a lexical/metabolite-neighbor false candidate and OPLAH is differential context only. |
| 218 | PC-related pyruvate carboxylase deficiency | UNMAPPED | False negative; resolve to `Pyruvate_Carboxylase_Deficiency_Disease.yaml`. |
| 220 | PDHA1-related pyruvate dehydrogenase E1 alpha deficiency | MAPPED | Correct PDH mapping, with subtype resolution to `Pyruvate_Dehydrogenase_Deficiency.yaml#E1-alpha deficiency`. |
| 221 | PDHB-related pyruvate dehydrogenase E1 beta deficiency | MAPPED | Correct PDH mapping, with subtype resolution to `Pyruvate_Dehydrogenase_Deficiency.yaml#E1-beta deficiency`. |
| 222 | DLAT-related dihydrolipoyl transacetylase deficiency | MAPPED | Correct subtype-level PDH E2 mapping with high concordance. |

## Batch 21

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 223 | DLD-related dihydrolipoyl dehydrogenase deficiency | MAPPED | Correct subtype-level PDH E3 mapping with high concordance. |
| 224 | PDHX-related pyruvate dehydrogenase E3-binding protein deficiency | MAPPED | Correct subtype-level PDH E3-binding protein mapping with high concordance. |
| 225 | PDP1-related pyruvate dehydrogenase phosphatase deficiency | MAPPED | Correct subtype-level PDH phosphatase mapping with high concordance. |
| 228 | CPT1A-related carnitine palmitoyltransferase 1A deficiency | CANDIDATE | Generated CPT II candidate is false; correct local target is `Carnitine_Palmitoyltransferase_1A_Deficiency.yaml`. |
| 229 | SLC25A20-related carnitine acylcarnitine translocase deficiency | MAPPED | Correct CACT mapping with high concordance, including severe cardiac and treatment overlap. |
| 230 | CPT2-related carnitine palmitoyltransferase 2 deficiency | CANDIDATE | Accept generated candidate as correct CPT II mapping with high concordance. |
| 231 | ACADVL-related very long-chain acyl-CoA dehydrogenase deficiency | MAPPED | Correct VLCAD mapping with high concordance; IEMbase adds C14:1 ratios and bezafibrate prompts. |
| 232 | HADHA-related trifunctional protein subunit alpha deficiency | UNMAPPED | False negative to local MTP/LCHAD coverage, but IEMbase label spans complete MTPD and isolated HADHA/LCHAD scopes. |
| 233 | HADHB-related isolated deficiency of long-chain 3-ketoacyl-CoA thiolase | UNMAPPED | Partial false negative to MTPD umbrella coverage; exact isolated HADHB/LKAT subtype remains a gap. |
| 234 | ACADM-related medium-chain acyl-CoA dehydrogenase deficiency | MAPPED | Correct MCAD mapping with high concordance and granular IEMbase biomarker detail. |

## Batch 22

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 235 | ACADS-related short-chain acyl CoA dehydrogenase deficiency | MAPPED | Generated coronary-artery-dissection mapping is false via SCAD acronym collision; correct local target is `SCAD_Deficiency.yaml`. |
| 236 | HADH-related short-chain 3-hydroxyacyl-CoA dehydrogenase deficiency | UNMAPPED | False negative to `Congenital_Isolated_Hyperinsulinism.yaml#SCHAD-HI` subtype coverage. |
| 237 | ETFA-related electron transfer flavoprotein alpha subunit deficiency | CANDIDATE | Accept candidate as correct MADD file-level mapping; subtype is ETFA/MADD type 2A. |
| 239 | ETFDH-related multiple acyl-CoA dehydrogenase deficiency | MAPPED | Correct MADD mapping with high concordance, especially for ETFDH/riboflavin-responsive MADD context. |
| 241 | IDUA-related alpha-iduronidase deficiency | MAPPED | Correct high-concordance MPS I mapping to `Hurler_syndrome.yaml`, with spectrum scope spanning Hurler-Scheie and Scheie noted. |
| 242 | IDS-related iduronate 2-sulfatase deficiency | MAPPED | Correct Hunter syndrome/MPS II mapping with high concordance. |
| 243 | SGSH-related heparan N-sulfatase deficiency | MAPPED | Correct subtype-level Sanfilippo A/MPS IIIA mapping. |
| 244 | NAGLU-related N-acetylglucosaminidase deficiency | MAPPED | Correct subtype-level Sanfilippo B/MPS IIIB mapping. |
| 245 | HGSNAT-related heparan-alpha-glucosaminide N-acetyltransferase deficiency | MAPPED | Correct subtype-level Sanfilippo C/MPS IIIC mapping, with RP73/attenuated retinal-label nuance noted. |
| 246 | GNS-related N-acetylglucosamine 6-sulfatase deficiency | MAPPED | Correct subtype-level Sanfilippo D/MPS IIID mapping. |

## Batch 23

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 247 | GALNS-related N-acetylgalactosamine 6-sulfatase deficiency | MAPPED | Correct subtype-level Morquio A/MPS IVA mapping with high concordance. |
| 248 | GLB1-related beta-galactosidase 1 deficiency, Morquio B | UNMAPPED | False negative; resolve to `Morquio_syndrome.yaml#Type B` with high concordance. |
| 249 | ARSB-related N-acetylgalactosamine 4-sulfatase deficiency | MAPPED | Correct Maroteaux-Lamy/MPS VI mapping with high concordance. |
| 250 | GUSB-related beta-glucuronidase deficiency | MAPPED | Correct Sly syndrome/MPS VII mapping with high concordance and treatment-row agreement. |
| 251 | HYAL1-related hyaluronidase deficiency | MAPPED | Correct MPS IX/HYAL1 mapping; IEMbase reinforces hyaluronidase, hyaluronic acid, and normal total-GAG rows. |
| 252 | PDSS1-related prenyl diphosphate synthase subunit 1 deficiency | MAPPED | Correct PDSS1 primary CoQ10 subtype mapping, with IEMbase adding granular renal, vascular, skin, optic, and neuropathy detail. |
| 253 | PDSS2-related prenyl diphosphate synthase subunit 2 deficiency | MAPPED | Correct PDSS2 primary CoQ10 subtype mapping with high concordance. |
| 254 | COQ2-related coenzyme Q2 polyprenyltranferase deficiency | MAPPED | Correct COQ2 primary CoQ10 subtype mapping with high concordance and IEMbase-only retinal/stroke-like prompts. |
| 255 | COQ9-related coenzyme 9 deficiency | MAPPED | Correct COQ9 primary CoQ10 subtype mapping; IEMbase adds human clinical and biomarker detail plus an alternate-label typo to review. |
| 256 | COQ8A-related coenzyme Q8A (ADCK3) deficiency | MAPPED | Correct dedicated COQ8A ubiquinone-deficiency ataxia mapping; the primary CoQ10 umbrella subtype remains secondary context. |

## Batch 24

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 257 | APTX-related aprataxin deficiency | MAPPED | Correct AOA1 subtype mapping, but IEMbase is sparse and its serum-albumin direction needs review. |
| 258 | AGA-related aspartylglucosaminidase deficiency | MAPPED | Correct aspartylglucosaminuria mapping; transplant treatment row needs local lack-of-benefit caveat. |
| 259 | FUCA1-related alpha-L-fucosidase deficiency | MAPPED | Correct fucosidosis mapping with high concordance. |
| 260 | MAN2B1-related alpha-mannosidase B deficiency | MAPPED | Correct alpha-mannosidosis mapping with high concordance. |
| 261 | MANBA-related beta-mannosidase deficiency | MAPPED | Correct beta-mannosidosis mapping; IEMbase adds granular neurologic, skeletal, ocular, and cellular prompts. |
| 262 | Alpha-N-acetylgalactosaminidase deficiency, Schindler disease type I | MAPPED | Generated type 3 target is wrong; resolve to `Schindler_Disease.yaml`. |
| 263 | NAGA-related alpha-N-acetylgalactosaminidase deficiency, Kanzaki disease | MAPPED | Correct Kanzaki disease/type II mapping with high concordance. |
| 264 | Alpha-N-acetylgalactosaminidase deficiency, Schindler disease type III | MAPPED | Correct `NAGA_Deficiency_Type_3.yaml` mapping with high concordance. |
| 265 | NEU1-related alpha-neuraminidase deficiency | MAPPED | Correct sialidosis type 1 mapping, with caution for IEMbase-only systemic rows that may reflect broader sialidosis spectrum. |
| 267 | SLC17A5-related sialin deficiency, severe | AMBIGUOUS | Resolve to `Free_Sialic_Acid_Storage_Disease.yaml#Infantile Free Sialic Acid Storage Disease`; standalone Salla disease is secondary context. |

## Batch 25

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 268 | DPYS-related dihydropyrimidinase deficiency | UNMAPPED | True local gap; do not conflate with DPYD deficiency or other pyrimidine-metabolism neighbors. |
| 269 | ACAT1-related mitochondrial acetoacetyl-CoA thiolase deficiency | MAPPED | Correct beta-ketothiolase mapping with high concordance and granular IEMbase crisis-marker detail. |
| 270 | ACAT2-related cytosolic acetoacetyl-CoA thiolase deficiency | UNMAPPED | Reject weak beta-ketothiolase candidate; ACAT2/cytosolic thiolase is distinct from ACAT1/T2 disease. |
| 272 | PEX1-related peroxin 1 deficiency | CANDIDATE | Accept candidate as correct file-level `Peroxisome_Biogenesis_Disorder.yaml` coverage, with PEX1-specific enrichment prompts. |
| 273 | ACOX1-related peroxisomal acyl-CoA oxidase deficiency | UNMAPPED | False negative; resolve to `Peroxisomal_Acyl-CoA_Oxidase_Deficiency.yaml`, while reviewing generic peroxisomal lab rows before import. |
| 274 | HSD17B4-related D-bifunctional protein deficiency | MAPPED | Correct DBP mapping with high concordance; IEMbase adds ocular, skeletal, renal, and portal-hypertension prompts. |
| 277 | PEX7-related RCDP type 1 | MAPPED | Correct RCDP1 mapping with high concordance; IEMbase adds cervical, infection, hearing, cardiac, and skin prompts. |
| 278 | GNPAT-related RCDP type 2 | MAPPED | Correct RCDP2 subtype mapping; review IEMbase phytanic-acid directionality before import. |
| 279 | AGPS-related RCDP type 3 | MAPPED | Correct RCDP3 subtype mapping; review IEMbase phytanic-acid directionality before import. |
| 280 | ABCD1-related X-linked adrenoleukodystrophy and adrenomyeloneuropathy | UNMAPPED | False negative; resolve to `adrenoleukodystrophy.yaml` with high concordance. |

## Batch 26

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 281 | PHYH-related Phytanoyl-CoA hydroxylase deficiency | MAPPED | Correct Adult Refsum mapping; DisMech is stronger for treatment and mechanism, while IEMbase adds pristanic/pipecolic and craniofacial/renal review prompts. |
| 282 | DNM1L-related Dynamin-like protein 1 deficiency | UNMAPPED | True local gap; reject the weak PDH candidate because DNM1L mitochondrial-peroxisomal fission disease is mechanistically distinct. |
| 284 | GLB1-related Beta-galactosidase-1 deficiency, GM1 gangliosidosis | UNMAPPED | False negative to local GLB1 GM1 spectrum coverage; map across GM1 types 1, 2, and 3 rather than only the infantile file. |
| 285 | HEXB-related Beta-hexosaminidase subunit beta deficiency | UNMAPPED | False negative; resolve to `Sandhoff_Disease.yaml`, with IEMbase adding VEP, urinary incontinence, movement-disorder, LysoGM2, and oligosaccharide prompts. |
| 286 | HEXA-related Beta-hexosaminidase subunit alpha deficiency | MAPPED | Correct Tay-Sachs mapping; high concordance, with IEMbase adding LysoGM2/oligosaccharide prompts and hepatosplenomegaly needing caution. |
| 287 | GM2A-related GM2 activator protein deficiency | MAPPED | Correct AB variant mapping; IEMbase reinforces the preserved Hex A activity distinction and adds sparse spasticity/urinary/psychiatric prompts. |
| 288 | GBA-related Glucocerebrosidase deficiency | MAPPED | Correct Gaucher mapping with high concordance; IEMbase adds specific ERT/SRT agents and pulmonary, malignancy, hemophagocytosis, and cirrhosis prompts. |
| 289 | GALC-related Beta-galactosylceramidase deficiency | UNMAPPED | False negative; resolve to `Krabbe_Disease.yaml`, with IEMbase adding CSF protein, deafness, fever, and later-onset ataxia prompts. |
| 290 | ARSA-related Arylsulfatase A deficiency | MAPPED | Correct MLD mapping; IEMbase OTL-200 aligns with local atidarsagene autotemcel and adds psychiatric/gait/dysarthria/spasticity review prompts. |
| 291 | PSAP-related Combined saposin deficiency | MAPPED | Correct combined saposin deficiency mapping; note the cached IEMbase label has a source typo and treat hydrolase-assay rows as downstream cofactor-loss readouts. |

## Batch 27

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 292 | PSAP-related Krabbe disease-like disorder due to saposin A deficiency | MAPPED | Correct saposin A/Krabbe-like mapping; IEMbase adds sensory, fever, feeding, CSF-protein, and lysogalactosylceramide prompts. |
| 293 | PSAP-related Metachromatic leukodystrophy-like disorder due to saposin B deficiency | CANDIDATE | Reject saposin C candidate; local MLD file is partial phenotype context, but a saposin B/PSAP-specific target is still missing. |
| 294 | PSAP-related Gaucher disease-like disorder due to saposin C deficiency | MAPPED | Correct saposin C/Gaucher-like mapping; IEMbase reinforces normal beta-D-glucosidase with elevated glucosylsphingosine and chitotriosidase. |
| 296 | GLA-related Alpha-galactosidase A deficiency | MAPPED | Correct Fabry mapping with high concordance; IEMbase adds agent-specific treatment rows and airway/pulmonary/malignancy/thyroid review prompts. |
| 297 | ASAH1-related Acid ceramidase deficiency, inflammatory phenotype | MAPPED | Correct Farber mapping with high concordance; IEMbase adds hepatosplenic, reflex, lung, lymph-node, CSF-protein, and C26-ceramide prompts. |
| 298 | SMPD1-related Acid sphingomyelinase deficiency | CANDIDATE | Generated type A candidate is valid but incomplete; split spectrum record across local Niemann-Pick type A and type B entries. |
| 299 | GNPTAB-related UDP-N-acetylglucosamine-1-phosphotransferase subunit alpha/beta deficiency | MAPPED | Correct mucolipidosis II mapping; IEMbase adds neuroimaging, otitis, hepatosplenic, and compartment-specific enzyme/GAG/oligosaccharide prompts. |
| 300 | GNPTG-related UDP-N-acetylglucosamine-1-phosphotransferase subunit gamma deficiency | UNMAPPED | False negative; resolve to `GNPTG-Mucolipidosis.yaml`, with IEMbase adding serum/leukocyte assay and urinary substrate prompts. |
| 301 | SUMF1-related Formyl-glycine generating enzyme deficiency | AMBIGUOUS | Resolve generated subtype ambiguity to file-level `Multiple_Sulfatase_Deficiency.yaml`; IEMbase adds selected MRI, cardiopulmonary, gingival, speech, and gait prompts. |
| 302 | LIPA-related Lysosomal acid lipase deficiency | MAPPED | Generated CESD mapping is incomplete; split spectrum record across `Wolman_Disease.yaml` and `Cholesteryl_Ester_Storage_Disease.yaml`. |

## Batch 28

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 303 | NPC1-related Niemann-Pick disease type C1 | MAPPED | Correct NPC1 subtype mapping; local coverage is strong, with IEMbase adding chitotriosidase, cholestane-triol, filipin-test, hemophagocytosis, and rare liver-tumor review prompts. |
| 304 | NPC2-related Niemann-Pick disease type C2 | MAPPED | Correct NPC2 subtype mapping; local coverage is strong, with IEMbase adding diagnostic biomarker rows and no NPC2-specific HPbCD treatment signal. |
| 305 | PPT1-related Palmitoyl-protein thioesterase 1 deficiency | MAPPED | Correct NCL1 mapping; local mechanism coverage is strong but lacks PPT1 enzyme assay and granular MRI/electrophysiology/retinal rows. |
| 306 | TPP1-related Tripeptidyl-peptidase 1 deficiency | MAPPED | Correct NCL2 mapping; high concordance for phenotype and cerliponase alfa, with IEMbase adding TPP1 assay and granular imaging/electrophysiology prompts. |
| 307 | CLN3-related Lysosomal transmembrane protein deficiency | MAPPED | Correct NCL3 mapping; DisMech covers core juvenile Batten disease while IEMbase adds psychiatric, movement, cardiac, cytologic, and electrophysiology review prompts. |
| 308 | CLN6-related Kufs disease | MAPPED | Correct adult NCL/Kufs mapping; local CLN6 adult coverage is strong, with IEMbase adding extrapyramidal, behavioral, and spasticity prompts. |
| 309 | DNAJC5-related Kufs disease | MAPPED | Correct adult NCL/Kufs mapping; DNAJC5 is covered genetically and mechanistically, but future gene-specific CLN4 subtype resolution could improve precision. |
| 310 | CLN5-related Lysosomal protein deficiency | UNMAPPED | True missing standalone NCL5 target; broad NCL umbrella provides only partial shared context. |
| 311 | CLN6-related Lysosomal protein deficiency | UNMAPPED | True missing CLN6 late-infantile target; do not map to adult CLN6 Kufs disease despite shared gene. |
| 312 | MFSD8-related CLN7 Turkish variant | MAPPED | Correct NCL7 mapping with high concordance, including Milasen; IEMbase adds granular MRI, optic, retinal, speech, and electrophysiology prompts. |

## Batch 29

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 313 | CLN8-related Lysosomal protein deficiency | UNMAPPED | True missing standalone NCL8/CLN8 target; broad NCL umbrella has CLN8 gene and shared phenotype context only. |
| 315 | CTSD-related Cathepsin D deficiency | UNMAPPED | True missing standalone NCL10/CTSD target; broad NCL umbrella has CTSD context but lacks CTSD enzyme-assay and congenital phenotype detail. |
| 316 | MMADHC-related Methylmalonic aciduria and homocystinuria, cblD type | UNMAPPED | False negative; resolve to the cobalamin umbrella's cblD subtype, with combined cblD-MMA/HC biochemical detail as enrichment. |
| 317 | MSMO1-related Sterol C4-methyloxidase deficiency | UNMAPPED | True local gap; cerebrotendinous xanthomatosis is a false sterol-pathway neighbor. |
| 318 | CYP51A1-related Lanosterol demethylase deficiency | UNMAPPED | True local gap; COA3-related COX deficiency is a lexical false-positive candidate. |
| 319 | CTSA-related Cathepsin A deficiency | MAPPED | Correct galactosialidosis mapping; local coverage is strong but IEMbase adds enzyme, oligosaccharide, renal, cardiac, and cellular review prompts. |
| 320 | SCARB2-related Glucocerebrosidase receptor deficiency | UNMAPPED | True missing SCARB2/AMRF target; reject Gaucher disease despite glucocerebrosidase-adjacent terminology and preserve normal beta-D-glucosidase as differential detail. |
| 321 | PMM2-related Phosphomannomutase 2 deficiency (CDG) | UNMAPPED | True PMM2-CDG gap; other gene-specific CDG files are context only, not valid targets. |
| 322 | MPI-related Phosphomannose isomerase deficiency (CDG) | UNMAPPED | True MPI-CDG gap with distinctive protein-losing enteropathy, hypoglycemia, liver, thrombosis, and coagulation-marker signals. |
| 323 | ALG6-related Glucosyltransferase 1 deficiency (CDG) | UNMAPPED | True ALG6-CDG gap; do not map to ALG12/ALG9 or other CDG entries based only on shared type I CDG features. |

## Batch 30

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 324 | ALG3-related Mannosyltransferase 6 deficiency (CDG) | CANDIDATE | Reject ALG12-CDG candidate; true ALG3-CDG gap with Man5GlcNAc2, hypoglycemia, and coagulation/protein biochemical prompts. |
| 325 | ALG12-related Mannosyltransferase 8 deficiency (CDG) | MAPPED | Correct ALG12-CDG mapping; IEMbase adds granular imaging, ocular/hearing, GI, endocrine, prenatal, and Man7 review prompts. |
| 326 | ALG8-related Glucosyltransferase 2 deficiency (CDG) | UNMAPPED | Reject ALG8-related ADPLD gene-collision candidate; true recessive ALG8-CDG gap. |
| 327 | ALG2-related Mannosyltransferase 2 deficiency (CDG) | CANDIDATE | Reject ALG12-CDG candidate; true ALG2-CDG gap, with local CMS glycosylation context only for the neuromuscular branch. |
| 328 | DPAGT1-related UDP-GlcNAc:Dol-P-GlcNac-P transferase deficiency (CDG) | UNMAPPED | Local CMS covers DPAGT1 neuromuscular context, but canonical multisystem DPAGT1-CDG remains a disease gap. |
| 329 | ALG1-related Mannosyltransferase 1 deficiency (CDG) | CANDIDATE | Reject ALG12-CDG candidate; true ALG1-CDG gap with early GlcNAc2 lipid-linked and renal/cardiac prompts. |
| 330 | ALG9-related Mannosyltransferase 7-9 deficiency (CDG) | MAPPED | Correct ALG9-CDG mapping with high concordance, including type I transferrin and Man6/Man8 lipid-linked biochemical signals. |
| 331 | RFT1-related Flippase of Man5GlcNAc2-PP-Dol deficiency (CDG) | UNMAPPED | Reject X-linked SCID candidate; true RFT1-CDG gap with Man5GlcNAc2, sensory, thrombotic, and coagulation prompts. |
| 332 | MGAT2-related N-acetylglucosaminyltransferase 2 deficiency (CDG) | UNMAPPED | False negative; low-score MGAT2-CDG candidate is the correct local target, with IEMbase adding granular dysmorphism, GI, and coagulation prompts. |
| 333 | GCS1-related Glucosidase 1 deficiency (CDG) | UNMAPPED | Reject Gaucher disease lexical candidate; true MOGS/GCS1-CDG gap with tetraglucoside, immunoglobulin, respiratory, and neurologic prompts. |

## Batch 31

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 334 | TUSC3-related oligosaccharyltransferase subunit deficiency (CDG) | UNMAPPED | True TUSC3-CDG gap; reject GHIS/IGFALS candidate because short stature is not enough to map across mechanisms. |
| 335 | SRD5A3-related steroid 5-alpha-reductase 3 deficiency (CDG) | CANDIDATE | Reject SRD5A2 46,XY DSD candidate; true SRD5A3-CDG gap with ocular, skin, brain, dolichol, and coagulation prompts. |
| 336 | DPM1-related GDP-Man:Dol-P mannosyltransferase deficiency (CDG) | UNMAPPED | Dystroglycanopathy has partial DPM1 pathway context, but standalone DPM1-CDG remains a local disease gap. |
| 337 | MPDU1-related Dol-P-Man utilization 1 deficiency (CDG) | MAPPED | Correct MPDU1-CDG mapping with high concordance; IEMbase adds growth-hormone, cerebral-atrophy, antithrombin, and Man5/Man9 prompts. |
| 338 | B4GALT1-related beta-1,4-galactosyltransferase 1 deficiency (CDG) | UNMAPPED | Reject GM1 gangliosidosis lexical candidate; true B4GALT1-CDG gap with hypogalactosylated transferrin and coagulation prompts. |
| 339 | GNE-related UDP-GlcNAc epimerase-kinase deficiency (CDG) | UNMAPPED | Reject Galactosemia/epimerase candidate; true GNE myopathy/CDG gap with rimmed-vacuole and N-acetylmannosamine prompts. |
| 340 | SLC35A1-related CMP-sialic acid transporter deficiency (CDG) | UNMAPPED | Reject SLC35A2-CDG family-neighbor candidate; true SLC35A1-CDG gap with macrothrombocytopenia and platelet-sialylation prompts. |
| 341 | SLC35C1-related GDP-fucose transporter deficiency (CDG) | UNMAPPED | Reject SLC35A2 and fucosidosis neighbors; true SLC35C1-CDG/LAD-II gap with neutrophil-rolling and fucose-treatment prompts. |
| 342 | DOLK-related dolichol kinase deficiency (CDG) | UNMAPPED | False negative; resolve to `DK1-congenital_disorder_of_glycosylation.yaml`, with IEMbase adding digital-necrosis and delayed-puberty prompts. |
| 343 | COG7-related conserved oligomeric Golgi complex subunit 7 deficiency (CDG) | MAPPED | Correct COG7-CDG mapping with high concordance; IEMbase adds renal/urinary, bilirubin/CK, and detailed glycan-fraction prompts. |

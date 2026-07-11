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

## Batch 32

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 344 | COG1-related conserved oligomeric Golgi complex subunit 1 deficiency (CDG) | MAPPED | Correct COG1-CDG mapping with high concordance; IEMbase adds cardiomyopathy, hearing, hepatic/splenic, platelet, and glycan-fraction prompts. |
| 345 | COG8-related conserved oligomeric Golgi complex subunit 8 deficiency (CDG) | CANDIDATE | Reject COG1-CDG fuzzy candidate; true COG8-CDG gap despite shared COG-complex/type II CDG biology. |
| 346 | ATP6V0A2-related cutis laxa type IIA (CDG) | UNMAPPED | True ATP6V0A2-CDG/cutis laxa gap; reject Peeling Skin Syndrome and preserve the source spelling variant ATP6VOA2. |
| 347 | EXT1-related exostosin 1 deficiency (CDG) | UNMAPPED | True EXT1 multiple cartilaginous exostoses gap; reject Multiple Synostoses Syndrome and treat chondrosarcoma as downstream context only. |
| 348 | EXT2-related exostosin 2 deficiency (CDG) | UNMAPPED | True EXT2 multiple cartilaginous exostoses gap; reject Multiple Synostoses Syndrome and verify sparse neurodevelopmental rows before import. |
| 349 | B4GALT7-related beta-1,4-galactosyltransferase 7 deficiency (CDG) | UNMAPPED | False negative; resolve to the local spEDS-B4GALT7 subtype under spondylodysplastic Ehlers-Danlos syndrome. |
| 350 | GALNT3-related hyperphosphatemic familial tumoral calcinosis | UNMAPPED | True GALNT3 tumoral calcinosis gap; reject brain-calcification candidate and retain phosphate-lowering treatment prompts. |
| 351 | SLC35D1-related UDP-glucuronic acid/UDP-GalNAc transporter deficiency (CDG) | MAPPED | Correct Schneckenbecken dysplasia mapping with high concordance; IEMbase adds CDG framing and normal sialotransferrins. |
| 352 | POMT1-related O-mannosyltransferase 1 deficiency (CDG) | UNMAPPED | False negative; resolve to the POMT1/MDDG1 context in `Dystroglycanopathy.yaml`. |
| 353 | POMT2-related O-mannosyltransferase 2 deficiency (CDG) | UNMAPPED | False negative; resolve to the POMT2/MDDG2 context in `Dystroglycanopathy.yaml`. |

## Batch 33

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 354 | POMGNT1-related O-Mannose beta-1,2-N-acetyglucosaminyltransferase deficiency (CDG) | UNMAPPED | False negative; resolve to the POMGNT1/MDDG3 context in `Dystroglycanopathy.yaml`. |
| 358 | LFNG-rerlated O-Fucose-specific beta-1,3-N-acetylglucosaminyltransferase deficiency (CDG) | UNMAPPED | False negative; resolve to `Spondylocostal_Dysostosis.yaml` LFNG/SCDO3 context and preserve the source-label typo only as source metadata. |
| 359 | B3GALTL-related O-Fucose-specific beta-1,3-N-glucosyltransferase deficiency (CDG) | UNMAPPED | True B3GLCT/Peters plus syndrome gap; reject Gaucher disease and phenotype-only anterior-segment neighbors. |
| 360 | ST3GAL5-related Lactosylceramide alpha-2,3-sialyltransferase deficiency (CDG) | MAPPED | Correct GM3 synthase deficiency mapping with high concordance; review IEMbase ORPHA:370938 versus local ORPHA:370933. |
| 361 | PIGM-related Phosphatidylinositolglycan, class M, deficiency (CDG) | UNMAPPED | True PIGM-CDG/GPI anchor deficiency gap; reject MHC class II deficiency and retain thrombosis/GPI-flow/sodium phenylbutyrate prompts. |
| 362 | PRPS1-related Phosphoribosyl pyrophosphate synthetase 1 superactivity | CANDIDATE | Accept the PRPS1 Superactivity candidate as the correct local target with high concordance. |
| 363 | IMPDH1-related Inosine-5'-monophosphate dehydrogenase deficiency | CANDIDATE | Reject GUCY2D retinopathy candidate; true IMPDH1 RP10/LCA11 gap despite shared retinal dystrophy phenotype. |
| 364 | XDH-related Xanthine oxidase deficiency | UNMAPPED | True XDH xanthinuria type I gap; reject chronic granulomatous disease and preserve xanthine/hypoxanthine/uric-acid prompts. |
| 367 | LDLR-related Familial hypercholesterolemia heterozygous (LDLR) | UNMAPPED | False negative; resolve to `Familial_Hypercholesterolemia.yaml`, heterozygous FH/LDLR branch. |
| 368 | APOB-related Familial defective apolipoprotein B | UNMAPPED | False negative; resolve to `Familial_Hypercholesterolemia.yaml`, APOB-LDLR binding-defect branch, and verify fibrates before import. |

## Batch 34

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 369 | PCSK9-related Proprotein convertase superactivity | UNMAPPED | False negative; resolve to `Familial_Hypercholesterolemia.yaml`, PCSK9 gain-of-function branch. |
| 370 | LDLRAP1-related Autosomal recessive hypercholesterolemia (ARH) | UNMAPPED | False negative; resolve to `Familial_Hypercholesterolemia.yaml`, LDLRAP1-related LDL uptake defect/autosomal recessive FH branch. |
| 371 | MTTP-related Microsomal triglyceride transfer protein deficiency | MAPPED | Correct abetalipoproteinemia mapping with high concordance; IEMbase adds biopsy, prothrombin-ratio, HDL, and reflex wording prompts. |
| 372 | APOB-related Apolipoprotein B deficiency | MAPPED | Generated abetalipoproteinemia mapping is over-broad; APOB familial hypobetalipoproteinemia type 1 is a separate local gap. |
| 373 | PCSK9-related Proprotein convertase deficiency with low LDL | UNMAPPED | True local gap or scope-review item; do not map opposite-direction PCSK9 loss-of-function disease to FH gain-of-function coverage. |
| 374 | ANGPTL3-related Angiopoietin-like 3 deficiency | MAPPED | Generated abetalipoproteinemia mapping is a false positive; ANGPTL3 combined familial hypolipidemia is a separate local gap. |
| 375 | CETP-related Cholesteryl ester transfer protein deficiency | UNMAPPED | True CETP deficiency gap; reject cholesteryl ester storage disease lexical candidate. |
| 376 | LIPC-related Hepatic lipase deficiency | UNMAPPED | True LIPC hepatic lipase deficiency gap; reject hepatic veno-occlusive disease lexical candidate. |
| 377 | SCARB1-related Scavenger receptor B1 deficiency | UNMAPPED | True SCARB1/SR-BI deficiency gap; reject triple-negative breast cancer candidate. |
| 378 | ABCA1-related Tangier disease | MAPPED | Correct Tangier disease mapping with high concordance; IEMbase adds concise orange tonsil, HDL, triglyceride, and ApoA-I prompts. |

## Batch 35

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 379 | APOA1-related Apolipoprotein A-I deficiency | UNMAPPED | True APOA1 deficiency gap; do not reuse Tangier disease just because low HDL/ApoA-I vocabulary overlaps. |
| 380 | LCAT-related Familial lecithin cholesterol acyl transferase deficiency | UNMAPPED | True LCAT deficiency gap; reject lipoyl transferase 1 as a lexical false-positive candidate. |
| 381 | LPL-related Lipoprotein lipase deficiency | UNMAPPED | False negative; resolve to `Familial_Chylomicronemia_Syndrome.yaml`, with LPL/familial hyperchylomicronemia as the relevant branch. |
| 382 | CLN8-related Northern epilepsy variant | UNMAPPED | True CLN8-EPMR subtype gap; broad NCL context is useful but not an exact Northern epilepsy target. |
| 383 | ALG11-related Mannosyltransferase 4-5 deficiency (CDG) | UNMAPPED | True ALG11-CDG gap; reject ALG12-CDG as a type I CDG family-neighbor candidate. |
| 384 | MAGT1-related Magnesium transporter 1 deficiency (CDG) | UNMAPPED | True MAGT1/XMEN-CDG gap; reject GSD I/GSD Ib and keep EBV-susceptibility mentions as differential context only. |
| 385 | CHSY1-related Chondroitin sulfate synthase 1 deficiency (CDG) | MAPPED | Correct Temtamy preaxial brachydactyly mapping with high concordance; preserve the source spelling variant as source metadata. |
| 386 | PIGY-related Phosphatidylinositolglycan, class V, deficiency (CDG) | UNMAPPED | True PIGY GPI-anchor deficiency gap; reject CHIME/PIGL as a pathway-neighbor candidate. |
| 387 | DPM3-related GDP-Man:Dol-P mannosyltransferase 3 deficiency (CDG) | UNMAPPED | False negative; resolve to `Dystroglycanopathy.yaml#DPM3-related dystroglycanopathy`, with CDG biochemical enrichment prompts. |
| 388 | COG5-related Conserved oligomeric Golgi complex subunit 5 deficiency (CDG) | CANDIDATE | Reject COG1-CDG candidate; true COG5-CDG gap, with COG-complex/type II CDG context only. |

## Batch 36

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 389 | COG6-related Component of COG complex 6 deficiency (CDG) | UNMAPPED | True COG6-CDG gap; reject COX14-related COX deficiency and use COG-complex/type II CDG files only as context. |
| 390 | TRIP11-related Achondrogenesis type IA (CDG) | UNMAPPED | True TRIP11/GMAP210-CDG gap; reject COL2A1 achondrogenesis type II despite lethal skeletal overlap. |
| 391 | SEC23B-related Congenital dyserythropoietic anemia type 2 (CDG) | CANDIDATE | Accept candidate as correct subtype mapping to `Congenital_Dyserythropoietic_Anemia.yaml#CDA II`. |
| 392 | SLC19A3-related Thiamine transporter 2 deficiency | MAPPED | Correct biotin-thiamine-responsive basal ganglia disease mapping with high concordance. |
| 393 | SLC25A19-related Mitochondrial thiamine pyrophosphate transporter deficiency | UNMAPPED | True SLC25A19 gap; reject GSD I and keep SLC19A3/BTBGD only as thiamine/basal-ganglia context. |
| 395 | ALDH18A1-related Delta-1-pyrroline-5-carboxylate synthase deficiency, cutis laxa phenotype | MAPPED | Correct ALDH18A1/P5CS spectrum mapping; IEMbase adds ARCL3A-specific skeletal, ocular, vascular, and brain prompts. |
| 397 | NOGENE-related Pearson Syndrome | UNMAPPED | False negative; resolve to `Pearson_Syndrome.yaml`, not pancreatic agenesis. |
| 398 | NOGENE-related Kearns Sayre Syndrome | UNMAPPED | False negative; resolve to `Kearns-Sayre_Syndrome.yaml`. |
| 402 | PRICKLE3-related Leber Hereditary Optic Neuropathy, LHON | UNMAPPED | True PRICKLE3-LHON gap; reject congenital insensitivity to pain and do not substitute Leber congenital amaurosis files. |
| 406 | MT-TT-related Mitochondrial tRNA(Thr) deficiency | UNMAPPED | True MT-TT/LIMM gap; reject reversible MT-TE infantile COX deficiency as a tRNA-neighbor candidate. |

## Batch 37

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 407 | MT-TE-related Mitochondrial Myopathy with Diabetes Mellitus | UNMAPPED | True MT-TE m.14709T>C diabetes-myopathy gap; reject reversible infantile MT-TE/COX deficiency despite shared gene. |
| 408 | MT-TE-related Mitochondrial tRNA(Glu) deficiency | UNMAPPED | False negative; resolve to `Reversible_Infantile_Cytochrome_c_Oxidase_Deficiency.yaml`. |
| 411 | POLG-related Mitochondrial DNA polymerase gamma catalytic subunit deficiency 4A | CANDIDATE | True POLG Alpers-Huttenlocher/MTDPS4A gap; reject MNGIE and use SANDO only as POLG-spectrum context. |
| 416 | OPA1-related Childhood-onset optic atrophy type 1 | UNMAPPED | Partial OPA1 context in DOA-plus file, but pure childhood/juvenile OPA1 optic atrophy remains an exact gap or lump/split decision. |
| 420 | POLG-related Spinocerebellar Ataxia with Epilepsy, included (SCAE, included) | MAPPED | Correct SANDO mapping with high concordance; review inheritance discordance before import. |
| 421 | OPA1-related Optic Atrophy 1 and Deafness | UNMAPPED | False negative; resolve to `Autosomal_Dominant_Optic_Atrophy_Plus.yaml`, with Behr/recessive subtype caveats. |
| 425 | LRPPRC-related Leigh Syndrome with French-Canadian Ethnicity | UNMAPPED | False negative; resolve to the French-Canadian LRPPRC subtype in `Leigh_Syndrome.yaml`. |
| 426 | ISCU-related Hereditary Myopathy with Lactic Acidosis | UNMAPPED | True ISCU/HML Fe-S myopathy gap; reject CMT/HNPP neuropathy candidate. |
| 436 | GFM1-related Mitochondrial elongation factor G1 deficiency | UNMAPPED | True GFM1/COXPD1 mitoribosome/translation gap; reject mitochondrial trifunctional protein deficiency. |
| 437 | MRPS16-related Mitochondrial ribosomal small subunit 16 deficiency | UNMAPPED | True MRPS16/COXPD2 neonatal combined-OXPHOS gap; reject HMG-CoA synthase deficiency. |

## Batch 38

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 438 | ACAD9-related Acyl-CoA Dehydrogenase 9 deficiency | UNMAPPED | False negative; resolve to `ACAD9_Deficiency.yaml` and reject glutaric acidemia type 1. |
| 439 | TSFM-related Mitochondrial elongation factor Ts deficiency | UNMAPPED | True TSFM/COXPD3 local gap; reject beta-ketothiolase deficiency. |
| 440 | TUFM-related Mitochondrial elongation factor Tu deficiency | UNMAPPED | True TUFM/COXPD4 local gap; reject mitochondrial trifunctional protein deficiency. |
| 441 | MRPS22-related Mitochondrial ribosomal small subunit 22 deficiency | UNMAPPED | True MRPS22/COXPD5 neonatal combined-OXPHOS gap; reject HMG-CoA synthase deficiency. |
| 442 | AIFM1-related X-Linked Mitochondrial Myopathy | UNMAPPED | True AIFM1 COXPD6 mitochondrial myopathy gap; reject DFNX hearing loss as an exact mapping. |
| 443 | C12ORF65-related Mitochondrial release factor deficiency | UNMAPPED | True C12ORF65/MTRFR COXPD7/SPG55 gap; reject ALDH18A1 spastic-paraplegia neighbor. |
| 444 | PUS1-related Pseudouridine synthase 1 deficiency | MAPPED | Correct PUS1/MLASA1 mapping with high concordance; IEMbase adds mtDNA depletion and dysmorphic-feature prompts. |
| 445 | TRMU-related tRNA 5-methylaminomethyl-2-thiouridylate-methyltransferase deficiency | UNMAPPED | Partial false negative/context case: local RIRCD captures TRMU/cysteine context, but dedicated TRMU transient infantile liver failure remains a gap. |
| 446 | DARS2-related Mitochondrial aspartyl-tRNA synthetase deficiency | UNMAPPED | True DARS2/LBSL gap; reject HMG-CoA synthase deficiency and do not substitute EIF2B leukodystrophy. |
| 451 | SDHA-related Succinate dehydrogenase subunit A deficiency | UNMAPPED | True SDHA/complex II deficiency gap; reject pyruvate dehydrogenase E1-beta and keep Leigh syndrome as phenotype context only. |

## Batch 39

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 463 | SLC25A3-related Mitochondrial phosphate carrier deficiency | UNMAPPED | True SLC25A3 mitochondrial phosphate carrier gap; reject HMG-CoA synthase deficiency. |
| 466 | SLC25A38-related Mitochondrial glycine transporter deficiency | UNMAPPED | True SLC25A38 sideroblastic anemia type 2 gap; reject primary carnitine deficiency and do not substitute MLASA/Pearson context. |
| 467 | TIMM8A-related Mohr-Tranebjaerg syndrome | UNMAPPED | True TIMM8A/Mohr-Tranebjaerg deafness-dystonia gap; ignore unrelated MTS acronym hits. |
| 468 | UCP1-3-related Uncoupling protein deficiency | UNMAPPED | True UCP1-3 uncoupling-protein gap or scope-review item; reject PDH E3-binding protein deficiency. |
| 471 | MT-RNR1-related Mitochondrial ribosomal RNA 12S deficiency | UNMAPPED | True MT-RNR1 aminoglycoside-induced deafness gap; reject mitochondrial trifunctional protein deficiency. |
| 473 | GALT-related Galactose-1-phosphate uridyltransferase deficiency (CDG) | MAPPED | Correct classic galactosemia/GALT mapping with high concordance; verify several extra urinary, imaging, and liver-tumor prompts before import. |
| 474 | GALK1-related Galactokinase deficiency (CDG) | UNMAPPED | False negative; resolve to `Galactosemia.yaml#Galactokinase Deficiency`. |
| 475 | GALE-related Galactose epimerase deficiency (CDG) | UNMAPPED | False negative; resolve to `Galactosemia.yaml#Epimerase Deficiency`. |
| 476 | KHK-related Hepatic fructokinase deficiency | UNMAPPED | True KHK essential fructosuria gap or low-priority scope-review item; reject essential thrombocythemia and do not map to ALDOB HFI. |
| 477 | ALDOB-related Aldolase B deficiency (CDG) | MAPPED | Correct hereditary fructose intolerance mapping with high concordance; IEMbase adds glycan, coagulation, electrolyte, lipid, uric-acid, and urinary glycerol prompts. |

## Batch 40

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 478 | LAMP2-related Lysosome-associated membrane protein 2 deficiency | MAPPED | Correct Danon disease mapping with high concordance; IEMbase adds Pompe-differentiating normal alpha-glucosidase rows plus EEG/ocular/lymphocyte prompts. |
| 479 | SLC5A2-related Sodium-glucose cotransporter 2 deficiency | UNMAPPED | False negative; resolve to `Familial_Renal_Glucosuria.yaml#SLC5A2-Related`, reject GSD I, and preserve the inheritance discrepancy for review. |
| 480 | SLC2A1-related Glucose transporter 1 deficiency | UNMAPPED | False negative; resolve to `GLUT1_Deficiency_Syndrome.yaml`, reject SLC35A2-CDG, and review triheptanoin/hemolytic-anemia additions. |
| 481 | SLC2A2-related Glucose transporter 2 deficiency | UNMAPPED | False negative; resolve to `Fanconi-Bickel_Syndrome.yaml`, reject SLC35A2-CDG, and review renal/hepatic complication enrichments. |
| 482 | SLC5A1-related Intestinal sodium-glucose cotransporter 1 deficiency | UNMAPPED | False negative; resolve to `Glucose-Galactose_Malabsorption.yaml` and reject GSD I as a carbohydrate-metabolism neighbor. |
| 483 | FBP1-related Fructose-1,6-bisphosphatase deficiency | UNMAPPED | True FBP1 deficiency gap; reject hereditary fructose intolerance despite fructose/hypoglycemia overlap. |
| 484 | G6PC-related Glucose-6-phosphatase deficiency | MAPPED | Correct subtype mapping to `Glycogen_Storage_Disease_Type_I.yaml#GSD Ia (glucose-6-phosphatase deficiency)`. |
| 485 | SLC37A4-related Glucose-6-phosphate transporter deficiency (CDG) | CANDIDATE | Accept as covered by `Glycogen_Storage_Disease_Type_I.yaml#GSD Ib (glucose-6-phosphate transporter deficiency)` rather than only broad GSD I. |
| 486 | GAA-related Alpha-glucosidase deficiency | MAPPED | Correct Pompe disease mapping with high concordance; IEMbase adds EEG, orthopnea, taurodontism, and compartment-specific enzyme-assay prompts. |
| 487 | AGL-related Amylo-1,6-glucosidase (debrancher) deficiency | UNMAPPED | False negative; resolve to `Cori_Forbes_Disease.yaml` and improve alias matching for GSD III / Cori-Forbes / limit dextrinosis. |

## Batch 41

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 488 | GBE1-related Glycogen branching enzyme deficiency | MAPPED | Correct GSD IV mapping with high concordance; review compartment-specific enzyme testing, coagulation, diet wording, and ORPHA identifier differences before import. |
| 489 | PYGM-related Muscle glycogen phosphorylase deficiency | CANDIDATE | Reject GSD I candidate; true PYGM/McArdle disease / GSD V gap, with exercise-test lactate, second wind, myoglobinuria, creatine, and sucrose prompts. |
| 490 | PYGL-related Liver glycogen phosphorylase deficiency | CANDIDATE | Reject GSD I candidate; true PYGL/Hers disease / GSD VI gap, with normal lactate/uric acid and liver phosphorylase prompts. |
| 491 | PFKM-related Muscle phosphofructokinase deficiency | MAPPED | Correct Tarui disease / GSD VII mapping with high concordance; review gallstones, jaundice, second wind, and ammonia-profile wording before import. |
| 492 | PHKA2-related Hepatic phosphorylase kinase alpha-2 subunit deficiency | CANDIDATE | Reject GSD I candidate; true X-linked PHKA2/GSD IXa gap, with liver phosphorylase kinase and normal lactate/uric acid prompts. |
| 493 | PGAM2-related Muscle phosphoglycerate mutase deficiency | CANDIDATE | Reject GSD I candidate; true PGAM2/DiMauro disease / GSD X gap, with muscle phosphoglycerate mutase, CK, glycogen, and myoglobin prompts. |
| 494 | SLC2A10-related L-Dehydroascorbate transporter deficiency | MAPPED | Correct arterial tortuosity syndrome mapping with high concordance; IEMbase adds arachnodactyly, facial stigmata, arterial hypertension, and joint-laxity prompts. |
| 496 | GYG1-related Muscle glycogenin 1 deficiency | CANDIDATE | Accept as covered by `Glycogen_Storage_Disease_XV.yaml`; consider promoting GYG1/GSD XV aliases from candidate to exact. |
| 497 | GYS2-related Hepatic glycogen synthase deficiency | CANDIDATE | Reject GSD I candidate; true GYS2/GSD 0a gap, with depleted liver glycogen, absent hepatomegaly, fasting avoidance, and protein-rich diet prompts. |
| 498 | GYS1-related Muscle glycogen synthase deficiency | CANDIDATE | Reject GSD I candidate; true GYS1/GSD 0b gap, distinct from both GSD I and GYS1-overactivity Lafora disease context. |

## Batch 42

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 499 | LDHA-related Lactate dehydrogenase A deficiency | CANDIDATE | Reject GSD I candidate; true LDHA/GSD XI gap with LDH activity, exercise-test lactate/ammonia, myoglobinuria, and pregnancy uterine-stiffness prompts. |
| 500 | ALDOA-related Aldolase A deficiency | CANDIDATE | Reject GSD I candidate; true ALDOA/GSD XII gap with aldolase activity, hemolytic anemia, bilirubin/reticulocyte, rhabdomyolysis, and dysmorphic-feature prompts. |
| 501 | ENO3-related Enolase beta deficiency | CANDIDATE | Reject GSD I candidate; true ENO3/GSD XIII gap with muscle beta-enolase, CK, muscle glycogen, exercise intolerance, cramps, pain, and weakness prompts. |
| 502 | PGK1-related Phosphoglycerate kinase deficiency | UNMAPPED | True PGK1 phosphoglycerate kinase deficiency gap; reject GSD VII neighbor despite shared glycolytic myopathy and hemolysis features. |
| 503 | SUCLA2-related ATP-specific succinyl-CoA synthetase beta subunit deficiency | CANDIDATE | Reject MTDPS7/TWNK candidate; true SUCLA2/MTDPS5 gap with methylmalonic aciduria, succinylcarnitine, lactate, Leigh, deafness, and dystonia prompts. |
| 504 | HOGA1-related Mitochondrial 4-hydroxy-2-oxoglutarate aldolase 1 deficiency | UNMAPPED | False negative; resolve to `Primary_Hyperoxaluria_Type_3.yaml`, with systemic oxalosis prompts needing source review before import. |
| 505 | APOC2-related Apolipoprotein C-II deficiency | UNMAPPED | False negative; resolve to `Familial_Chylomicronemia_Syndrome.yaml` with APOC2 branch context and review APOC2-specific treatment rows. |
| 506 | USF1-related Familial combined hyperlipidemia | MAPPED | Correct FCHL subtype mapping to `Hyperlipidemia.yaml`; DisMech lacks visible USF1/Apo B-specific coverage. |
| 507 | APOE-related Apolipoprotein E deficiency | UNMAPPED | Partial hyperlipidemia and sea-blue histiocyte context only; exact APOE dysbetalipoproteinemia / type III hyperlipoproteinemia remains a local gap. |
| 508 | ABCG5-related Sitosterolemia | UNMAPPED | True ABCG5 sitosterolemia / phytosterolemia gap; do not substitute broad hyperlipidemia for plant-sterol transporter disease. |

## Batch 43

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 509 | LPA-related elevated lipoprotein(a) | UNMAPPED | True LPA/elevated lipoprotein(a) gap; reject Tangier disease and use vascular/lipid entries only as context. |
| 510 | CYP11A1-related side-chain cleavage enzyme deficiency | UNMAPPED | True CYP11A1/P450scc steroidogenesis gap; reject nonketotic hyperglycinemia and use CAH/adrenal insufficiency only as context. |
| 512 | GSS-related glutathione synthetase deficiency, severe | UNMAPPED | True severe GSS gap; hereditary orotic aciduria is a false metabolite-neighbor candidate and OPLAH is differential context only. |
| 513 | MVK-related mevalonate kinase deficiency, severe | MAPPED | Correct mevalonic aciduria subtype mapping to `Mevalonate_Kinase_Deficiency.yaml#Mevalonic Aciduria`; IEMbase adds leukotriene E4 and respiratory/cytopenia prompts. |
| 514 | EBP-related chondrodysplasia punctata 2, recessive | UNMAPPED | True EBP/MEND syndrome gap; reject PEX7-related RCDP1 despite chondrodysplasia punctata/cataract overlap. |
| 515 | NSDHL-related CK syndrome | UNMAPPED | True NSDHL CK syndrome gap; reject ZC4H2-related Wieacker-Wolff syndrome as a neurodevelopmental false candidate. |
| 521 | SLC1A3-related glutamate aspartate transporter deficiency | CANDIDATE | Reject CACNA1A episodic ataxia type 2 as exact; true SLC1A3/EAAT1/EA6 transporter gap. |
| 522 | SLC6A5-related glycine transporter 2 deficiency | MAPPED | Correct hereditary hyperekplexia mapping with SLC6A5/GlyT2 concordance; IEMbase adds head-retraction and SIDS-related prompts. |
| 523 | SLC25A12-related mitochondrial aspartate-glutamate carrier deficiency | UNMAPPED | True SLC25A12/Aralar deficiency gap; reject CACNA1A-DEE42 and preserve mitochondrial biomarker/treatment prompts. |
| 524 | SLC25A22-related mitochondrial glutamate transporter deficiency | UNMAPPED | True SLC25A22/EIEE3 gap; broad undetermined EOEE is context only, not an exact gene-specific target. |

## Batch 44

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 525 | CTNS-related nephropathic cystinosis | AMBIGUOUS | Correct local `Cystinosis.yaml` target; resolve to nephropathic infantile/juvenile context rather than ocular-only cystinosis. |
| 527 | LDLR-related homozygous familial hypercholesterolemia | UNMAPPED | False negative; resolve to `Familial_Hypercholesterolemia.yaml#Homozygous Familial Hypercholesterolemia`. |
| 528 | LCAT-related fish-eye disease | UNMAPPED | True partial LCAT / fish-eye disease gap; reject carnitine palmitoyltransferase II as a fatty-acid-oxidation false candidate. |
| 529 | SLC52A3-related Brown-Vialetto-Van Laere syndrome | CANDIDATE | Accept candidate; resolve to `Brown-Vialetto-Van_Laere_Syndrome.yaml#SLC52A3/BVVL1`. |
| 530 | SLC52A3-related Fazio-Londe syndrome | UNMAPPED | False negative; use `Brown-Vialetto-Van_Laere_Syndrome.yaml` as the riboflavin-transporter spectrum target while preserving deafness-absent scope. |
| 531 | COQ6-related coenzyme Q6 monooxygenase deficiency | UNMAPPED | False negative; resolve to `Primary_Coenzyme_Q10_Deficiency.yaml#COQ6` with oto-renal CoQ10 deficiency context. |
| 532 | ETFDH-related myopathic form of CoQ10 deficiency | UNMAPPED | False negative; resolve to `Multiple_Acyl-CoA_Dehydrogenase_Deficiency.yaml#ETFDH` rather than a separate primary CoQ10 entry. |
| 533 | ATP7A-related distal spinal muscular atrophy type 3 | UNMAPPED | False negative at spectrum level; resolve to `Menkes_Disease.yaml#ATP7A-related distal motor neuropathy`, not classic Menkes disease. |
| 537 | SUGCT-related glutaric aciduria type 3 | CANDIDATE | Reject GCDH/GA1 candidate; true SUGCT/GA3 benign-form gap with normal 3-hydroxyglutaric acid. |
| 542 | GK-related isolated glycerol kinase deficiency | UNMAPPED | True GK/hyperglycerolemia gap; reject BCKDK as a lexical kinase-deficiency false candidate. |

## Batch 45

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 544 | MCEE-related methylmalonic aciduria due to methylmalonyl-CoA epimerase deficiency | CANDIDATE | Broad MMA context only; do not treat as an exact MCEE mapping until an MMAE subtype or standalone MCEE target exists. |
| 548 | ABCD4-related methylmalonic aciduria and homocystinuria, cblJ type | MAPPED | Correct cblJ subtype mapping with high concordance; IEMbase adds SAM, renal/HUS, hypersegmented-neutrophil, myelopathy, and ocular prompts. |
| 549 | ADK-related adenosine kinase deficiency | MAPPED | Correct ADK mapping with high concordance; IEMbase adds adenosine, SAM/SAH, liver, coagulation, glucose, uric-acid, hearing, and neuroimaging prompts. |
| 550 | SLC33A1-related acetyl-CoA transporter deficiency | MAPPED | Correct Huppke-Brendel syndrome mapping with high concordance; IEMbase adds cerebral/cerebellar atrophy and axial-hypotonia detail. |
| 551 | MTHFD1-related 5,10-methylene-tetrahydrofolate dehydrogenase deficiency | UNMAPPED | True MTHFD1 folate one-carbon metabolism gap; reject CAH 3B-HSD as a dehydrogenase-name false candidate. |
| 552 | ABCB4-related progressive familial intrahepatic cholestasis type 3 | UNMAPPED | True PFIC3 gap; reject progressive familial heart block and preserve high-GGT cholestasis, bile-acid, fibrosis, and transplant prompts. |
| 553 | SLCO1B1/SLCO1B3-related Rotor syndrome | UNMAPPED | True digenic Rotor syndrome gap; reject Bartter/porphyria context and preserve organic-anion transport and coproporphyrin I prompts. |
| 554 | ABCC2-related Dubin-Johnson syndrome | UNMAPPED | True ABCC2/Dubin-Johnson gap; reject Stevens-Johnson and porphyria candidates. |
| 555 | AKR1C2-related 3-alpha-hydroxysteroid dehydrogenase type 3 deficiency | UNMAPPED | True AKR1C2 backdoor pathway gap; reject HSD3B2 CAH despite steroid/DSD phenotype overlap. |
| 556 | GNPTAB-related mucolipidosis III alpha/beta | MAPPED | Correct ML III alpha/beta mapping with high concordance; IEMbase adds enzyme-directionality, urinary GAG/oligosaccharide, hernia, hip, and foam-cell prompts. |

## Batch 46

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 557 | GRN-related progranulin deficiency | UNMAPPED | False negative for the recessive CLN11/NCL aspect; resolve to `Neuronal_Ceroid_Lipofuscinosis.yaml#GRN`, while dominant GRN-FTLD/TDP-43 remains separate context. |
| 558 | ATP13A2-related lysosomal type 5 P-type ATPase deficiency | UNMAPPED | False negative; resolve to `Kufor-Rakeb_syndrome.yaml` with CLN12/PARK9 alias review. |
| 559 | CTSF-related cathepsin F deficiency | UNMAPPED | False negative; resolve to `Adult_Neuronal_Ceroid_Lipofuscinosis.yaml#CTSF` for CLN13 / Type B Kufs disease. |
| 560 | KCTD7-related CLN14 disease | UNMAPPED | Broad PME/NCL group context only; exact KCTD7/CLN14/EPM3 coverage remains a local gap. |
| 561 | ALPL-related tissue-nonspecific alkaline phosphatase deficiency | MAPPED | Correct hypophosphatasia mapping with high concordance; review dental, respiratory, calcium/phosphate, and asfotase alfa scope. |
| 562 | OAT-related ornithine aminotransferase deficiency | MAPPED | Correct OAT/gyrate atrophy mapping with high concordance; IEMbase adds creatine/GAA, treatment, neuromuscular, imaging, and neuropathy prompts. |
| 563 | PHKA1-related muscle phosphorylase kinase deficiency | CANDIDATE | Reject GSD I candidate; true PHKA1/GSD IXd gap with muscle phosphorylase kinase, exercise-test, second-wind, CK, and myoglobin prompts. |
| 564 | PRKAG2-related phosphorylase kinase deficiency, AMP-activated | UNMAPPED | Reject MNGIE candidate; true PRKAG2 glycogen-storage cardiomyopathy / AMPK disease gap. |
| 565 | GLYCTK-related D-glycerate kinase deficiency | UNMAPPED | Reject mevalonate kinase candidate; true GLYCTK/D-glyceric acidemia gap with D-glycerate, acidosis, and severe neurodevelopmental prompts. |
| 566 | ABCC8-related ATP-sensitive potassium channel regulatory subunit deficiency | UNMAPPED | False negative; resolve to `Congenital_Isolated_Hyperinsulinism.yaml#KATP-HI/ABCC8`. |

## Batch 47

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 567 | GLUD1-related glutamate dehydrogenase superactivity | MAPPED | Correct HI/HA subtype mapping to `Congenital_Isolated_Hyperinsulinism.yaml#HI/HA Syndrome`; IEMbase adds 2-ketoglutaric acid, EEG, and generalized-epilepsy prompts. |
| 568 | GCK-related glucokinase superactivity | UNMAPPED | False negative; resolve to `Congenital_Isolated_Hyperinsulinism.yaml#GCK-HI`, while source-reviewing IEMbase MODY/type 2 diabetes wording. |
| 570 | HNF4A-related MODY1 / hyperinsulinism | UNMAPPED | False negative to CHI/monogenic-diabetes context; reject FRTS4 as exact unless renal Fanconi variant-specific phenotype is present. |
| 571 | SLC16A1-related monocarboxylate transporter 1 superactivity | UNMAPPED | Broad CHI context only; reject PRPS1 superactivity and treat exact SLC16A1/HHF7 exercise-induced hyperinsulinism as a local gap. |
| 572 | UCP2-related uncoupling protein 2 deficiency | UNMAPPED | Broad CHI context only; reject pyruvate dehydrogenase deficiency and treat exact UCP2-HI as a local gap. |
| 573 | HNF1A-related MODY3 | UNMAPPED | False negative to partial local coverage in `Congenital_Isolated_Hyperinsulinism.yaml#HNF4A/HNF1A-HI` and `Diabetes_Mellitus.yaml#HNF1A`; no standalone HNF1A/MODY3 entry. |
| 574 | SUCLG1-related mitochondrial DNA depletion syndrome type 9 | CANDIDATE | Reject mitochondrial CIPO/MNGIE candidate; true SUCLG1/MTDPS9 gap with methylmalonic acid, lactate, Leigh, deafness, and early-death prompts. |
| 575 | SERAC1-related MEGDEL syndrome | UNMAPPED | Reject COX8A candidate; true SERAC1/MEGDEL gap with 3-methylglutaconic aciduria, deafness, Leigh-like lesions, regression, and filipin prompts. |
| 576 | TMEM70-related complex V deficiency | UNMAPPED | Reject COX11 candidate; true TMEM70 complex V assembly deficiency gap with cardiomyopathy, WPW, acidosis, pulmonary, renal, and neuroimaging prompts. |
| 577 | ACSF3-related combined malonic and methylmalonic aciduria | UNMAPPED | False negative; resolve to `Combined_Malonic_and_Methylmalonic_Aciduria.yaml` and reject HMG-CoA synthase candidate. |

## Batch 48

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 578 | AP1S1-related MEDNIK syndrome | MAPPED | Correct exact mapping to `MEDNIK_syndrome.yaml`; IEMbase adds low serum copper/ceruloplasmin, high ASAT/ALAT and bile-acid, very-long-chain fatty-acid, cerebral-atrophy, hyperkeratosis, and intestinal pseudo-obstruction prompts. |
| 579 | SLC18A2-related vesicular monoamine transporter 2 deficiency | UNMAPPED | Reject primary carnitine deficiency; true SLC18A2/VMAT2 monoamine-vesicular-transport gap, with no exact local target identified. |
| 580 | MTHFS-related 5,10-methenyltetrahydrofolate synthetase deficiency | UNMAPPED | Reject CPS1 deficiency; true MTHFS / 5-formyltetrahydrofolate cycloligase gap, with only broad folate/remethylation/cerebral-folate context. |
| 581 | HAMP-related hepcidin deficiency | MAPPED | Correct subtype-level mapping to `Hemochromatosis.yaml#Type 2B`; IEMbase adds concise ferritin, glucose, transferrin-saturation, and liver-iron prompts. |
| 582 | TFR2-related transferrin receptor 2 deficiency | MAPPED | Correct subtype-level mapping to `Hemochromatosis.yaml#Type 3`; IEMbase adds normal-to-high iron-index staging plus abdominal-pain and hyperpigmentation prompts. |
| 583 | INSR-related Donohue syndrome | UNMAPPED | Reject IPEX syndrome; true INSR severe insulin-receptoropathy gap; source-review IEMbase inheritance while preserving hyperinsulinemic hypoglycemia, ketone, and free-fatty-acid prompts. |
| 584 | SMS-related Snyder-Robinson syndrome | UNMAPPED | Reject GM3 synthase deficiency; true spermine-synthase/polyamine gap; source-review IEMbase inheritance/OMIM pairing and preserve N-acetylspermidine, epileptic-encephalopathy, and intellectual-disability prompts. |
| 585 | PHEX-related X-linked hypophosphatemia | MAPPED | Correct exact mapping to `X-Linked_Hypophosphatemia.yaml`; IEMbase adds alkaline-phosphatase, urinary-phosphate, normal-calcium, tinnitus, muscle-weakness, and waddling-gait prompts. |
| 587 | VPS11-related hypomyelinating leukodystrophy type 12 | UNMAPPED | Reject HLD7/POLR3 candidate; true VPS11/HLD12 gap with urinary glycosphingolipid/sulfatide and MRI/sensory/autonomic prompts. |
| 588 | DNAJC12-related hyperphenylalaninemia | UNMAPPED | False negative; resolve to `Disorder_of_Catecholamine_Synthesis.yaml#DNAJC12-related monoamine synthesis disorder`, with pterin, CSF HVA/5-HIAA, treatment, autism, and dystonia prompts. |

## Batch 49

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 589 | KCNA4-related potassium channelopathy | UNMAPPED | Reject CACNA1A calcium-channel candidate; true KCNA4 potassium-channelopathy gap with striatal-necrosis, cataract, dystonia, microcephaly, growth, and attention prompts. |
| 590 | PPA2-related mitochondrial inorganic pyrophosphatase 2 deficiency | UNMAPPED | Partial PPA2 coverage exists in `Dilated_Cardiomyopathy.yaml`; exact PPA2 mitochondrial pyrophosphatase / infantile sudden cardiac failure remains a local gap. |
| 591 | SAMD9-related MIRAGE syndrome | UNMAPPED | Reject CHARGE syndrome; true SAMD9/MIRAGE gap with adrenal-axis, myelodysplasia, thrombocytopenia, infection, enteropathy, and genital-phenotype prompts. |
| 592 | NANS-related N-acetylneuraminic acid synthase deficiency | UNMAPPED | Reject AIFM1/Bieganski SEMD candidate; true NANS-CDG / sialic-acid-biosynthesis gap with N-acetyl-D-mannosamine and skeletal/facial/neurodevelopmental prompts. |
| 593 | CCDC115-related congenital disorder of glycosylation | CANDIDATE | Reject ALG12-CDG as exact; true CCDC115-CDG / CDG-IIo gap with type 2 glycosylation, liver, lipid, ceruloplasmin, and neurodevelopmental prompts. |
| 594 | TANGO2-related recurrent metabolic encephalomyopathic crises | UNMAPPED | Reject PKAN candidate; true TANGO2/MECRCN gap with metabolic-crisis, rhabdomyolysis, arrhythmia, hypoglycemia, lactate, CK, and acylcarnitine prompts. |
| 595 | SLC39A8-related congenital disorder of glycosylation | CANDIDATE | Reject ALG12-CDG as exact; true SLC39A8-CDG / manganese-transporter gap with low manganese, zinc, type 2 sialotransferrin, and nutritional-treatment prompts. |
| 596 | SLC25A26-related S-adenosylmethionine carrier deficiency | UNMAPPED | Reject HHH syndrome as an SLC25-family false candidate; true SLC25A26/COXPD28 gap with respiratory-chain, pyruvate, lactic-acidosis, hydrops, and perinatal-failure prompts. |
| 597 | HAO1-related hydroxyacid oxidase 1 deficiency | UNMAPPED | False negative; resolve to `HAO1-Related_Glycolate_Oxidase_Deficiency.yaml` and source-review IEMbase oxalate/nephrolithiasis and achalasia/alacrima prompts before import. |
| 598 | GMPPA-related GDP-mannose pyrophosphorylase B deficiency | UNMAPPED | Reject CHIME syndrome; true GMPPA/AAMR gap with normal sialotransferrins, achalasia, alacrima, postural-hypotension, hearing, swallowing, and facial prompts. |

## Batch 50

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 599 | GMPPB-related muscular dystrophy-dystroglycanopathy | CANDIDATE | Accept `Dystroglycanopathy.yaml#MDDG14 (GMPPB)` as subtype-level coverage, with `Congenital_Myasthenic_Syndrome.yaml#GMPPB` as secondary CMS context; preserve CK, alpha-dystroglycan, cataract, CMS, myoglobinuria, seizure, and neurodevelopmental prompts. |
| 600 | PGM1-related phosphoglucomutase 1 deficiency | CANDIDATE | Reject GSD I as exact; true PGM1-CDG / GSD XIV gap with D-galactose, transferrin, antithrombin, nonketotic hypoglycemia, hyperinsulinism, cardiomyopathy, rhabdomyolysis, hepatopathy, endocrine, clefting, thrombosis, and malignant-hyperthermia prompts. |
| 601 | PGM3-related phosphoglucomutase 3 deficiency | CANDIDATE | Reject IKBKG/IMD33 as exact; true PGM3-CDG / immunodeficiency-23 gap with N/O-glycan, normal sialotransferrin, CD19 B-cell, IgE, T-cell immunodeficiency, neutropenia, infection, atopy, skeletal, facial, growth, and neurodevelopmental prompts. |
| 602 | DHDDS-related dehydrodolichyl diphosphate synthase deficiency | CANDIDATE | Reject EYS-related RP as exact; true DHDDS-CDG / RP59 gap with normal sialotransferrins, retinitis pigmentosa, epilepsy, intellectual disability, ataxia, dystonia, hypotonia, micropenis, and acute renal-failure prompts. |
| 603 | NUS1-related Nogo-B receptor deficiency | UNMAPPED | Reject GABRD/GEFS+ as a seizure-only false candidate; true NUS1 / NgBR-CDG gap with cortical atrophy, retinitis pigmentosa, epilepsy, microcephaly, axial hypotonia, acral spasticity, scoliosis, developmental delay, and failure-to-thrive prompts. |
| 604 | DPM2-related dolichol-P-mannose synthase-2 deficiency | UNMAPPED | False negative; resolve to `Dystroglycanopathy.yaml#DPM2-related dystroglycanopathy` while preserving DPM2-CDG biochemical and systemic prompts including type 1 sialotransferrin, dolichol-linked Man5GlcNAc2, hepatomegaly, infections, respiratory, joint, scoliosis, strabismus, cerebral, seizure, and muscular-dystrophy rows. |
| 605 | ALG13-related UDP-N-acetylglucosamine transferase deficiency | UNMAPPED | Reject generic DEE13 as exact; true ALG13-CDG / EIEE36 gap with transferrin, thromboplastin, refractory epilepsy, regression, extrapyramidal/pyramidal, visual, feeding, microcephaly, hepatomegaly, and facial prompts. |
| 606 | ALG14-related congenital myasthenic syndrome 15 | UNMAPPED | Partial broad context in `Congenital_Myasthenic_Syndrome.yaml#Glycosylation`, but exact ALG14-CDG / CMS15 remains a local gap; preserve normal CK, possible type 1 sialotransferrin, fetal hydrops, contractures, hypotonia, epilepsy, developmental delay, behavioral, and CMS-without-tubular-aggregates prompts. |
| 607 | DDOST-related congenital disorder of glycosylation | CANDIDATE | Reject ALG12-CDG as exact; true DDOST-CDG / CDG-Ir gap with transferrin, antithrombin, factor XI, protein C/S, neonatal liver, oromotor, strabismus, reflux, constipation, myelination, ear infection, osteopenia, failure-to-thrive, hypotonia, and neurodevelopmental prompts. |
| 608 | STT3A-related congenital disorder of glycosylation | CANDIDATE | Reject ALG12-CDG as exact; true STT3A-CDG gap with N-glycan, transferrin, factor VIII, von Willebrand factor, seizure, hypotonia, neurodevelopmental, gastrointestinal dysmotility, growth, microcephaly, and cerebellar-atrophy prompts. |

## Batch 51

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 609 | STT3B-related congenital disorder of glycosylation | CANDIDATE | Reject ALG12-CDG as exact; true STT3B-CDG gap with neonatal transferrin type I pattern, respiratory/hepatic/coagulation, neurodevelopmental, optic-atrophy, and genital-phenotype prompts. |
| 610 | SSR4-related congenital disorder of glycosylation | CANDIDATE | Reject ALG12-CDG as exact; true X-linked SSR4-CDG gap with transferrin, abnormal fat distribution, neurodevelopmental, dysmorphic, strabismus, skeletal, and genital prompts. |
| 611 | MAN1B1-related mannosyl-oligosaccharide alpha-1,2-mannosidase deficiency | UNMAPPED | True MAN1B1-CDG gap; reject generic DYRK1A/intellectual-disability overlap and preserve transferrin, transaminase, speech, behavior, obesity, hypotonia, seizure, strabismus, and facial prompts. |
| 612 | SLC35A2-related early infantile epileptic encephalopathy-22 / CDG | MAPPED | Correct exact `SLC35A2-CDG.yaml` mapping with high concordance; review IEMbase prompts for infections, visual/retinal findings, limb/hand abnormalities, corpus-callosum/cerebellar imaging, and galactose evidence wording. |
| 613 | TMEM165-related congenital disorder of glycosylation | CANDIDATE | Reject ALG12-CDG as exact; true TMEM165-CDG / CDG-IIk gap with type II sialotransferrin, CK/transaminase, growth hormone, skeletal, osteoporosis, hepatomegaly, joint-laxity, and treatability-review prompts. |
| 614 | COG2-related conserved oligomeric Golgi complex deficiency | CANDIDATE | Reject COG1-CDG as exact; true COG2-CDG gap with transferrin, copper/ceruloplasmin, coagulopathy, pituitary, thin-corpus-callosum, spasticity, seizure, hepatic, and neurodevelopmental prompts. |
| 615 | COG4-related conserved oligomeric Golgi complex deficiency | CANDIDATE | Reject COG1-CDG as exact; true COG4-CDG gap with transferrin, apolipoprotein CIII, liver-enzyme, AFP, ammonia, LDL, cerebral-atrophy, developmental-delay, and intellectual-disability prompts. |
| 616 | PLPBP-related pyridoxal 5-prime-phosphate binding protein deficiency | UNMAPPED | True treatable PLPBP / vitamin B6-dependent epilepsy gap; reject PDH/E3-binding candidate and source-review vitamin B6 evidence before import. |
| 617 | WDR45-related neurodegeneration with brain iron accumulation 5 | MAPPED | Correct subtype mapping to `Neurodegeneration_With_Brain_Iron_Accumulation.yaml#BPAN`; preserve BPAN-specific dementia, cerebral atrophy, movement disorder, seizure, and age-banded brain-iron prompts. |
| 618 | TDO2-related hypertryptophanemia | UNMAPPED | True local gap but scope-review needed because IEMbase is biochemical-only; reject alkaptonuria and preserve tryptophan/serotonin biomarker prompts if curated. |

## Batch 52

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 619 | SLC16A1-related monocarboxylate transporter-1 deficiency | UNMAPPED | True MCT1 deficiency gap; reject primary carnitine deficiency and keep distinct from earlier SLC16A1/HHF7 superactivity. |
| 620 | COASY-related coenzyme A synthase deficiency | CANDIDATE | Broad NBIA/PKAN differential context only; reject BPAN as exact and curate COASY/NBIA6/CoPAN as its own NBIA subtype or disease if selected. |
| 621 | TPK1-related thiamine pyrophosphokinase deficiency | CANDIDATE | Reject SLC19A3 biotin-thiamine-responsive basal ganglia disease as exact; true TPK1/THMD5 gap with thiamine, lactate, 2-ketoglutarate, and globus-pallidus prompts. |
| 622 | PCYT1A-related retinoskeletal phosphocholine cytidylyltransferase deficiency | UNMAPPED | Reject SED congenita; true PCYT1A/SMDCRD gap with hypolipidemia, cone-rod dystrophy, retinopathy, and skeletal prompts. |
| 623 | CAD-related trifunctional protein deficiency | CANDIDATE | Reject mitochondrial trifunctional protein deficiency as a lexical false candidate; true CAD/CAD-CDG/EIEE50 gap with uridine, epilepsy/regression, anemia, and normal biochemical-caveat prompts. |
| 625 | POGLUT1-related Dowling-Degos disease 4 | UNMAPPED | Reject EBS Dowling-Meara lexical collision; true POGLUT1/DDD4 gap with dermatologic and normal sialotransferrin prompts. |
| 626 | GANAB-related alpha glucosidase II deficiency | AMBIGUOUS | Covered at ADPKD disease-family level via GANAB pathogenic variants; prefer `Autosomal_Dominant_Polycystic_Kidney_Disease.yaml` and preserve GANAB/PKD3 subtype and normal sialotransferrin caveats. |
| 627 | PIGW-related hyperphosphatasia with mental retardation syndrome 5 | UNMAPPED | Reject PIGL/CHIME as exact; true PIGW/HPMRS5 GPI-anchor gap with alkaline phosphatase, decreased GPI markers, epilepsy, hypotonia, and developmental-delay prompts. |
| 628 | PIGC-related developmental disability with drug-responsive epilepsy | UNMAPPED | Reject IRX5 craniofacial/ID candidate; true PIGC-CDG gap with decreased GPI markers, seizures, intellectual disability, ataxia, cerebellar, hypotonia, and facial prompts. |
| 629 | PIGG-related glycosylphosphatidylinositol biosynthesis defect 13 | UNMAPPED | True PIGG/GPIBD13 gap; keep separate from Wolf-Hirschhorn PIGG haploinsufficiency context and preserve normal GPI-marker caveat. |

## Batch 53

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 630 | PGAP1-related GPI deacylase deficiency | UNMAPPED | True PGAP1/GPI-deacylase gap; keep separate from chromosome 2q32-q33 deletion PGAP1 haploinsufficiency context and preserve neurodevelopmental, epilepsy, MRI, hypotonia, movement, apnea, hand, and facial prompts. |
| 631 | PGAP3-related hyperphosphatasia with mental retardation syndrome 4 | UNMAPPED | Reject PIGL/CHIME as exact; true PGAP3/HPMRS4 GPI-anchor maturation gap with alkaline phosphatase, decreased GPI markers, hypotonia, epilepsy, intellectual disability, ataxia, cleft-palate, and micrognathia prompts. |
| 632 | TRAPPC11-related limb-girdle muscular dystrophy 2S | UNMAPPED | Reject autosomal dominant LGMD as exact; true recessive TRAPPC11/LGMD2S-CDG gap with CK, weakness/myopathy, cholestasis, neurodevelopmental, cerebral atrophy, hip, skeletal, and facial prompts. |
| 633 | VPS13B-related Cohen syndrome | UNMAPPED | Reject GM3 synthase deficiency; true VPS13B/Cohen syndrome gap with transferrin glycoforms, myopia, chorioretinal degeneration, neutropenia, obesity, microcephaly, ID, and joint-laxity prompts. |
| 634 | TMEM199-related congenital disorder of glycosylation | CANDIDATE | Reject ALG12-CDG as exact; true TMEM199-CDG/CDG-IIp gap with alkaline phosphatase, transaminase, type 2 sialotransferrin, apolipoprotein CIII, low ceruloplasmin, and hepatomegaly prompts. |
| 635 | ATP6AP1-related immunodeficiency 47 and hepatopathy | UNMAPPED | Reject IKBKG immunodeficiency and somatic ATP6AP1 granular-cell-tumor context; true inherited ATP6AP1-CDG gap with glycosylation, copper/ceruloplasmin, immunoglobulin, liver, infection, pancreatic, neurologic, and cutis-laxa prompts. |
| 636 | ATP6V1A-related autosomal recessive cutis laxa type IID | UNMAPPED | Reject EDAR HED and somatic ATP6V1A tumor context; true ATP6V1A cutis-laxa/CDG gap with sialotransferrin, cutis laxa, seizures, hypotonia, cardiovascular, brain MRI, contracture, kyphoscoliosis, ocular, and facial prompts. |
| 637 | ATP6V1E1-related autosomal recessive cutis laxa type IIC | UNMAPPED | Reject chronic granulomatous disease; true ATP6V1E1 cutis-laxa/CDG gap with type 2 sialotransferrin, cutis laxa, hypotonia, cardiovascular, skeletal/contracture, cleft-palate, ocular, dental, and facial prompts. |
| 638 | XYLT1-related Desbuquois dysplasia 2 | UNMAPPED | Reject FBN1-related geleophysic dysplasia 2 and CANT1/Desbuquois mentions as exact; true XYLT1/Desbuquois dysplasia 2 gap with brachydactyly, femoral, patellar, coronal-cleft, joint-laxity, short-stature, craniofacial, and clubfoot prompts. |
| 639 | XYLT2-related spondyloocular syndrome | UNMAPPED | True XYLT2/spondyloocular syndrome gap; preserve combined bone-density/fracture, vertebral, cataract, retinal-detachment, hearing-loss, cardiac, stature, kyphosis, and ID prompts. |

## Batch 54

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 640 | RXYLT1-related muscular dystrophy-dystroglycanopathy type A | MAPPED | Correct disease-level target is `Dystroglycanopathy.yaml`, not lissencephaly spectrum alone; broadly covered via RXYLT1/MDDG10 and type A dystroglycanopathy, with gonadal and neural-tube prompts still thin. |
| 641 | CRPPA-related muscular dystrophy-dystroglycanopathy types A7 and C7 | UNMAPPED | Broadly covered by `Dystroglycanopathy.yaml` through CRPPA/MDDG7 and type A/C framework; missing exact A7/C7 cross-product subtype and some eye/brain/limb detail. |
| 642 | FKTN-related muscular dystrophy-dystroglycanopathy type A | UNMAPPED | Broadly covered by `Dystroglycanopathy.yaml` through FKTN/MDDG4 and type A/Fukuyama continuum; missing exact FKTN type A row and several ocular, regression, contracture, respiratory, and cardiac prompts. |
| 643 | FKTN-related muscular dystrophy-dystroglycanopathy type B | UNMAPPED | Broadly covered by FKTN and type B dystroglycanopathy; preserve narrow no-intellectual-disability row nuance with CK, normal sialotransferrin, hypotonia, and muscular dystrophy prompts. |
| 644 | FKTN-related muscular dystrophy-dystroglycanopathy type C | UNMAPPED | Broadly covered by `Dystroglycanopathy.yaml`; not yet represented as an FKTN limb-girdle subtype in AR LGMD, so preserve rigid-spine and cardiomyopathy prompts. |
| 645 | FKRP-related muscular dystrophy-dystroglycanopathy type A | UNMAPPED | Broadly covered by `Dystroglycanopathy.yaml` through FKRP/MDDG5 and type A framework; missing exact FKRP type A row and detailed Walker-Warburg eye/brain/regression prompts. |
| 646 | FKRP-related muscular dystrophy-dystroglycanopathy type B | UNMAPPED | Broadly covered by FKRP and type B dystroglycanopathy; missing exact FKRP type B row with nodular heterotopia, cerebellar white-matter, feeding, microcephaly, and spinal prompts. |
| 647 | FKRP-related muscular dystrophy-dystroglycanopathy type C | UNMAPPED | Covered locally by both `Dystroglycanopathy.yaml` and FKRP/LGMDR9 in AR LGMD; preserve myoglobinuria and tongue-hypertrophy prompts not clearly captured locally. |
| 648 | VPS33A-related mucopolysaccharidosis-plus syndrome | UNMAPPED | Reject Hurler syndrome as exact; true VPS33A MPS-plus gap with GAG/oligosaccharide, hematologic, renal, cardiac, respiratory, infection, neurodevelopmental, and storage-phenotype prompts. |
| 650 | TIMM50-related 3-methylglutaconic aciduria type 9 | UNMAPPED | Reject glutaryl-CoA dehydrogenase deficiency as exact; true TIMM50/3-methylglutaconic aciduria type 9 gap with lactate, 3-MGA, epilepsy, hypsarrhythmia, optic atrophy, and brain-imaging prompts. |

## Batch 55

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 651 | HAAO-related 3-hydroxyanthranilic acid 3,4-dioxygenase deficiency | UNMAPPED | Reject alkaptonuria; true HAAO/VCRL1 gap with 3-hydroxyanthranilic acid, NAD+, cardiac, renal, limb, hearing, stature, and ID prompts. |
| 652 | KYNU-related 3-hydroxykynureninase deficiency | UNMAPPED | Reject hereditary orotic aciduria; true KYNU/VCRL2/xanthurenic aciduria gap with kynurenine-pathway metabolites, NAD+, cardiac, renal, limb, stature, and speech prompts. |
| 653 | TPI1-related triosephosphate isomerase deficiency | UNMAPPED | Reject intrinsic factor deficiency; true TPI1 glycolytic hemolytic-anemia gap with red-cell TPI/DHAP, infections, neuromuscular, cardiac, seizure, and stroke prompts. |
| 655 | DHTKD1-related 2-aminoadipic 2-oxoadipic aciduria | UNMAPPED | Reject D-2-hydroxyglutaric aciduria as exact; true DHTKD1/AMOXAD gap with adipic/ketoadipic organic-acid, ketone, acidosis, developmental, and seizure prompts. |
| 656 | CA5A-related carbonic anhydrase VA deficiency | UNMAPPED | Broad hyperammonemia/UCD context only; true CA5A gap with ammonia, lactate, glucose, amino-acid, organic-acid, acylglycine, encephalopathy, coma, and feeding prompts. |
| 657 | ALDH3A2-related fatty aldehyde dehydrogenase deficiency | UNMAPPED | Reject Sjogren autoimmune disease as an eponym collision; true ALDH3A2/Sjogren-Larsson gap with enzyme, ichthyosis, spasticity, ID, leukoencephalopathy, and macular prompts. |
| 658 | TTPA-related alpha-tocopherol transfer protein deficiency | MAPPED | Correct exact AVED mapping to `Familial_Isolated_Vitamin_E_Deficiency.yaml`; IEMbase adds lipid, broad-beta electrophoresis, brain MRI, and xanthoma prompts. |
| 659 | ABCD3-related congenital bile acid synthesis defect | MAPPED | Broad bile-acid umbrella context only; exact ABCD3/PMP70 subtype gap with THCA/C27 bile acids, normal peroxisomal lipid markers, liver, anemia, and hepatosplenomegaly prompts. |
| 660 | ACOX2-related congenital bile acid synthesis defect | MAPPED | Broad bile-acid umbrella context only; exact ACOX2/CBAS6 subtype gap with C24/C27 bile-acid directionality, vitamin D, cholesterol, ataxia, cognition, steatorrhea, and fibrosis prompts. |
| 661 | UGT1A1-related UDP-glucuronosyltransferase A1 deficiency | MAPPED | Partial Gilbert-only coverage; severe Crigler-Najjar/bilirubin-neurotoxicity scope remains under-covered, including convulsions, abnormal eye movements, hearing, and neonatal instability. |

## Batch 56

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 662 | NR1H4-related progressive familial intrahepatic cholestasis 5 | UNMAPPED | True NR1H4/FXR/PFIC5 gap; reject progressive familial heart block and use bile-acid/cholestasis files only as broad context for normal-GGT neonatal cholestasis and liver failure. |
| 663 | PPM1K-related branched-chain ketoacid dehydrogenase phosphatase deficiency | UNMAPPED | Partial MSUD pathway coverage in `Maple_Syrup_Urine_Disease.yaml`; no standalone PPM1K mild-variant subtype/file, so preserve the phosphatase mechanism and mild elevated-BCAA signal. |
| 664 | BCKDK-related branched-chain ketoacid dehydrogenase kinase deficiency | MAPPED | Correct exact mapping to `BCKDK_Deficiency.yaml`; IEMbase adds speech and stereotyped-hand-movement prompts on top of the low-BCAA autism/ID/seizure phenotype. |
| 665 | ECHS1-related mitochondrial short-chain enoyl-CoA hydratase 1 deficiency | UNMAPPED | False negative from stale mapping; resolve to exact `ECHS1_Deficiency.yaml` and reject beta-ketothiolase deficiency while preserving neonatal metabolite, cardiomyopathy, hearing, optic, and apnea prompts. |
| 666 | UQCRC2-related mitochondrial complex III deficiency, nuclear type 5 | CANDIDATE | Reject COX8A complex IV candidate; true UQCRC2/complex III gap with neonatal lactate, hypoglycemia, hyperammonemia, metabolic acidosis, transaminase, and developmental-delay prompts. |
| 667 | SLC45A1-related neuronal glucose transporter deficiency | UNMAPPED | False negative from stale mapping; resolve to exact `SLC45A1-Related_Neuronal_Glucose_Transporter_Deficiency.yaml` and preserve normal CSF/plasma glucose plus dysmorphology prompts. |
| 668 | SI-related sucrase-isomaltase deficiency | MAPPED | Correct exact mapping to `Congenital_Sucrase-Isomaltase_Deficiency.yaml`; IEMbase adds sodium, normal reducing-sugar, dehydration, and urolithiasis prompts. |
| 669 | TREH-related trehalase deficiency | UNMAPPED | False negative from stale mapping; resolve to exact `Trehalase_Deficiency.yaml` and reject galactosemia while preserving normal stool reducing sugars and adolescent/adult GI timing. |
| 671 | CRAT-related carnitine acetyltransferase deficiency | UNMAPPED | True CRAT gap; reject CPT2/CPT1A carnitine-shuttle context and preserve childhood ataxia, oculomotor apraxia, consciousness disturbance, hypotonia, and ID prompts. |
| 673 | CPT1C-related autosomal dominant spastic paraplegia type 73 | CANDIDATE | Reject CPT2 deficiency and CPT1A isoform context; true CPT1C/SPG73 gap with adult spastic paraplegia, hyperreflexia, weakness/atrophy, loss of ambulation, and evoked-potential prompts. |

## Batch 57

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 674 | PMVK-related phosphomevalonate kinase deficiency | UNMAPPED | True PMVK/POROK1 gap; reject MVK-related mevalonate kinase deficiency and unrelated RNU12 porokeratosis context while preserving adolescent/adult actinic porokeratosis and keratotic lesions. |
| 675 | MVD-related mevalonate pyrophosphate decarboxylase deficiency | UNMAPPED | True MVD/POROK7 gap; reject hereditary orotic aciduria and use mevalonate-pathway content only as broad context for adolescent/adult porokeratosis. |
| 676 | FDPS-related farnesylpyrophosphate synthetase deficiency | UNMAPPED | True FDPS/POROK9 gap; reject CPS1 deficiency and preserve the dominant porokeratosis/keratotic-lesion phenotype. |
| 677 | NDUFAF1-related complex I assembly factor 1 deficiency | CANDIDATE | Reject COX20 complex IV candidate; true NDUFAF1/MC1DN11 gap with decreased complex I activity, lactate, cardiomyopathy, failure-to-thrive, hypotonia, lactic-acidosis, and MELAS-like prompts. |
| 678 | NDUFAF2-related complex I assembly factor 2 deficiency | CANDIDATE | Reject COX14 complex IV candidate; true NDUFAF2/MC1DN10 gap with renal tubular acidosis, respiratory insufficiency, basal-ganglia, nystagmus, optic-atrophy, ataxia, and encephalopathy prompts. |
| 679 | NDUFAF3-related complex I assembly factor 3 deficiency | CANDIDATE | Reject COX6A2 complex IV candidate; true NDUFAF3/MC1DN18 gap with neonatal/infantile complex I deficiency, lactate, leukomalacia, perinatal death, respiratory failure, hypotonia, and optic atrophy. |
| 680 | NDUFAF4-related complex I assembly factor 4 deficiency | CANDIDATE | Reject COX8A complex IV candidate; true NDUFAF4/MC1DN15 gap with neonatal/infantile complex I deficiency, lactate, Leigh syndrome, cardiomyopathy, and encephalomyopathy. |
| 681 | NDUFAF5-related complex I assembly factor 5 deficiency | CANDIDATE | Reject COX4I1 complex IV candidate; true NDUFAF5/MC1DN16 gap with broad Leigh/complex I overlap plus CSF lactate, dysmorphology, IUGR, hair/toe, sacral-pit, and movement-disorder prompts. |
| 682 | NDUFAF6-related complex I assembly factor 6 deficiency | UNMAPPED | Partial gene-level coverage in `Fanconi_Renotubular_Syndrome.yaml#FRTS5`, but exact MC1DN17 Leigh/striatal-necrosis phenotype remains under-covered. |
| 683 | FOXRED1-related mitochondrial complex I deficiency, nuclear type 19 | CANDIDATE | Reject PET117 complex IV candidate; true FOXRED1/MC1DN19 gap with decreased complex I activity, lactate, Leigh syndrome, hypertrophic cardiomyopathy, cerebellar atrophy, and pulmonary hypertension. |

## Batch 58

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 684 | TMEM126B-related transmembrane protein 126B deficiency | CANDIDATE | Reject COX11 complex IV candidate; true TMEM126B/MC1DN29 gap with decreased complex I activity, hypertrophic cardiomyopathy, myopathy, renal tubular acidosis, and exercise intolerance. |
| 685 | NDUFV1-related NADH dehydrogenase flavoprotein 1 deficiency | UNMAPPED | Partial gene-level coverage in `Leigh_Syndrome.yaml`, but no standalone NDUFV1/MC1DN4 target; preserve lactate, brainstem/basal-ganglia lesions, cardiomyopathy, ophthalmoplegia, microcephaly, and regression prompts. |
| 686 | NDUFV2-related NADH dehydrogenase flavoprotein 2 deficiency | CANDIDATE | Reject COX6B1 complex IV candidate; true NDUFV2/MC1DN7 gap with leukodystrophy, liver dysfunction, myopathy, optic neuropathy, parkinsonism, and hypertrophic cardiomyopathy prompts. |
| 687 | NDUFS1-related NADH dehydrogenase iron-sulfur protein 1 deficiency | CANDIDATE | Reject COX8A complex IV candidate; true NDUFS1/MC1DN5 gap with lactate, cardiomyopathy, encephalopathy, hypotonia, liver dysfunction, myopathy, leukodystrophy, and optic neuropathy. |
| 688 | NDUFS2-related NADH dehydrogenase iron-sulfur protein 2 deficiency | CANDIDATE | Reject COX4I1 complex IV candidate; true NDUFS2/MC1DN6 gap with lactate, encephalopathy, hypotonia, Leigh syndrome, liver dysfunction, parkinsonism, cardiomyopathy, and myopathy. |
| 689 | NDUFS3-related NADH dehydrogenase iron-sulfur protein 3 deficiency | CANDIDATE | Reject TACO1 complex IV candidate; true NDUFS3/MC1DN8 gap with decreased complex I activity, lactate, developmental delay, encephalopathy, Leigh syndrome, and myopathy. |
| 690 | NDUFS4-related NADH dehydrogenase iron-sulfur protein 4 deficiency | UNMAPPED | Partial gene-level coverage in `Leigh_Syndrome.yaml`, but no standalone NDUFS4/MC1DN1 target; preserve complex I/III activity, glucose, lactate, basal-ganglia, failure-to-thrive, hypotonia, cardiomyopathy, and Leigh prompts. |
| 691 | NDUFS6-related NADH dehydrogenase iron-sulfur protein 6 deficiency | CANDIDATE | Reject PET117 complex IV candidate; true NDUFS6/MC1DN9 gap with severe multisystem complex I disease, cardiomyopathy, basal-ganglia, hypotonia, lactic-acidosis, and failure-to-thrive prompts. |
| 692 | NDUFS7-related NADH dehydrogenase iron-sulfur protein 7 deficiency | CANDIDATE | Reject COX10 complex IV candidate; true NDUFS7/MC1DN3 gap with lactate, ataxia, epilepsy, feeding difficulty, liver dysfunction, myopathy, cardiomyopathy, encephalopathy, and Leigh prompts. |
| 693 | NDUFS8-related NADH dehydrogenase iron-sulfur protein 8 deficiency | CANDIDATE | Reject COX11 complex IV candidate; true NDUFS8/MC1DN2 gap with decreased complex I activity, Leigh syndrome, ataxia, dysarthria, hypotonia, cardiomyopathy, myopathy, and progressive external ophthalmoplegia. |

## Batch 59

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 694 | NDUFA1-related NADH dehydrogenase alpha subcomplex subunit 1 deficiency | CANDIDATE | Reject PET100 complex IV candidate; true NDUFA1/MC1DN12 gap with X-linked inheritance, decreased complex I activity, lactate, epilepsy, hypotonia, lactic acidosis, psychomotor retardation, basal-ganglia MRI abnormalities, and Leigh syndrome. |
| 695 | NDUFA2-related NADH dehydrogenase alpha subcomplex subunit 2 deficiency | CANDIDATE | Reject COX10 complex IV candidate; true NDUFA2/MC1DN13 gap with decreased complex I activity, lactate, lactic acidosis, Leigh syndrome, and leukoencephalopathy; source OMIM:256000 should be reviewed against expected OMIM:618235. |
| 696 | NDUFA4-related cytochrome c oxidase subunit NDUFA4 (COXFA4) deficiency | MAPPED | Correct exact mapping to `COXFA4-Related_COX_Deficiency.yaml`; DisMech is strong for corrected complex IV mechanism and lactate/Leigh identity, while IEMbase adds alanine, CSF lactate, FTT, regression, neuropathy, optic, renal, respiratory, dystonia, and hypertension prompts. |
| 697 | NDUFA9-related NADH dehydrogenase alpha subcomplex subunit 9 deficiency | CANDIDATE | Reject COX11 complex IV candidate; true NDUFA9/MC1DN26 gap with decreased complex I activity, lactate, brain/brainstem MRI disease, dysarthria, dysphagia, lactic acidosis, Leigh syndrome, dystonia, and retinitis pigmentosa; source OMIM:256000 should be reviewed against expected OMIM:618247. |
| 698 | NDUFA10-related NADH dehydrogenase alpha subcomplex subunit 10 deficiency | CANDIDATE | Reject COX16 complex IV candidate; true NDUFA10/MC1DN22 gap with decreased complex I activity, lactate, lactic acidosis, psychomotor retardation, basal-ganglia MRI abnormalities, hypertrophic cardiomyopathy, hypotonia, and Leigh syndrome. |
| 699 | NDUFA11-related NADH dehydrogenase alpha subcomplex subunit 11 deficiency | CANDIDATE | Reject COA3 complex IV candidate; true NDUFA11/MC1DN14 gap with decreased complex I activity, lactate, cardiomyopathy, encephalopathy, and a source lactic-acidosis marker anomaly. |
| 700 | NDUFA12-related NADH dehydrogenase alpha subcomplex subunit 12 deficiency | CANDIDATE | Reject COX11 complex IV candidate; true NDUFA12/MC1DN23 gap with decreased complex I activity, growth retardation, Leigh syndrome, psychomotor retardation, dystonia, and hypotonia. |
| 701 | NDUFA13-related NADH dehydrogenase alpha subcomplex subunit 13 deficiency | CANDIDATE | Reject TACO1 complex IV candidate; true NDUFA13/MC1DN28 gap with decreased complex I activity, lactate, cerebellar atrophy, developmental delay, encephalopathy, feeding difficulties, lactic acidosis, and hypotonia. |
| 702 | NDUFB3-related NADH dehydrogenase beta subcomplex subunit 3 deficiency | CANDIDATE | Reject COX18 complex IV candidate; true NDUFB3/MC1DN25 gap with decreased complex I activity, lactate, developmental delay, encephalopathy, hypotonia, myopathy, and lactic acidosis; source OMIM:252010 should be reviewed against expected OMIM:618246. |
| 703 | NDUFB9-related NADH dehydrogenase beta subcomplex subunit 9 deficiency | CANDIDATE | Reject FASTKD5 complex IV candidate; true NDUFB9/MC1DN24 gap with decreased complex I activity, lactate, perinatal death, hypotonia, and lactic acidosis; source OMIM:252010 should be reviewed against expected OMIM:618245. |

## Batch 60

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 704 | NDUFB11-related NADH dehydrogenase beta subcomplex subunit 11 deficiency | CANDIDATE | Reject COX10 complex IV candidate; true NDUFB11/MC1DN30 or NDUFB11/LSDMCA3 gap with decreased complex I activity, lactate, sideroblastic anemia, cardiomyopathy, microphthalmia, perinatal death, and lactic acidosis; source OMIM:252010 should be reviewed against MONDO's NDUFB11/LSDMCA3 OMIM:300952 context. |
| 705 | MT-ND1-related NADH dehydrogenase core subunit 1 deficiency | UNMAPPED | True MT-ND1 complex I gap with decreased complex I activity, lactate, exercise intolerance, LHON, hypertrophic cardiomyopathy, dystonia, MELAS-like features, myopathy, and spasticity; reject weak PDH E1-beta candidate. |
| 706 | MT-ND2-related NADH dehydrogenase core subunit 2 deficiency | UNMAPPED | True MT-ND2 complex I gap with decreased complex I activity, lactate, low-to-normal glucose, exercise intolerance, LHON, Leigh syndrome, and ragged red fibers; reject weak PDH E1-beta candidate. |
| 707 | MT-ND3-related NADH dehydrogenase core subunit 3 deficiency | UNMAPPED | True MT-ND3 complex I gap with decreased complex I activity, lactate, dystonia, epilepsy, abnormal eye movements, LHON, neuropathy, encephalopathy, Leigh syndrome, myopathy, and optic atrophy; reject weak PDH E1-beta candidate. |
| 708 | MT-ND4-relatedNADH dehydrogenase core subunit 4 deficiency | UNMAPPED | True MT-ND4 complex I gap with decreased complex I activity, lactate, dystonia, LHON, adult MELAS-like features, and Leigh syndrome; reject weak PDH E1-beta candidate and preserve the source-label spacing anomaly. |
| 709 | MT-ND4L-related NADH dehydrogenase core subunit 4L deficiency | UNMAPPED | True MT-ND4L complex I/LHON gap with decreased complex I activity and adolescent/adult LHON; reject weak PDH E1-beta candidate. |
| 710 | MT-ND5-related NADH dehydrogenase core subunit 5 deficiency | UNMAPPED | Partial MT-ND5 context exists in Leigh and MELAS entries, but exact MT-ND5 complex I deficiency remains missing; preserve complex I activity, lactate, LHON, Leigh, MELAS-like, source-spelled MERFF-like, renal failure, and myopathy prompts. |
| 711 | MT-ND6-related NADH dehydrogenase core subunit 6 deficiency | UNMAPPED | True MT-ND6 complex I gap with decreased complex I activity, lactate, dystonia, lactic acidosis, LHON, MELAS-like features, stroke-like episodes, epilepsy, Leigh syndrome, and optic atrophy; reject weak PDH E1-beta candidate. |
| 712 | TTC19-related Mitochondrial complex III deficiency, nuclear type 2 | CANDIDATE | Reject COX11 complex IV candidate; true TTC19/MC3DN2 complex III gap with lactate, low-to-normal glucose, hypoglycemia, metabolic acidosis, basal ganglia MRI abnormalities, developmental delay, and gait ataxia. |
| 714 | UQCC3-related Mitochondrial complex III deficiency, nuclear type 9 | CANDIDATE | Reject PET117 complex IV candidate; true UQCC3/MC3DN9 complex III gap with lactate, developmental delay, and short stature. |

## Batch 61

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 715 | LYRM7-related Mitochondrial complex III deficiency, nuclear type 8 | CANDIDATE | Reject TACO1 complex IV candidate; true LYRM7/MC3DN8 complex III gap with lactate, cavitating leukodystrophy, developmental delay, episodic encephalopathy, hypotonia, and possible perinatal death. |
| 716 | UQCRB-related Mitochondrial complex III deficiency, nuclear type 3 | CANDIDATE | Reject COX10 complex IV candidate; true UQCRB/MC3DN3 complex III gap with decreased complex III activity, lactate, epilepsy, growth retardation, intellectual disability, cardiomyopathy, encephalopathy, exercise intolerance, lactic acidosis, and myopathy. |
| 717 | UQCRQ-related Mitochondrial complex III deficiency, nuclear type 4 | CANDIDATE | Reject SCO1 complex IV candidate; true UQCRQ/MC3DN4 complex III gap with low-to-normal glucose, lactate, basal ganglia MRI abnormalities, intellectual disability, loss of speech, and extrapyramidal signs. |
| 719 | COA3-related Cytochrome c oxidase assembly factor 3 deficiency | UNMAPPED | False negative; resolve to exact `COA3-Related_COX_Deficiency.yaml`, with IEMbase adding developmental delay on top of local neuropathy, exercise intolerance, obesity, short stature, and COX1-coupling mechanism. |
| 720 | COA5-related Cytochrome c oxidase assembly factor 5 deficiency | CANDIDATE | Reject COX15/type 2 candidate; true COA5 fatal infantile COX deficiency type 3 gap with neonatal cardiomyopathy and perinatal death. |
| 721 | COA6-related Cytochrome c oxidase assembly factor 6 deficiency | CANDIDATE | Reject COX15/type 2 candidate; true COA6 fatal infantile COX deficiency type 4 gap with neonatal/infantile lactate elevation, cardiomyopathy, and perinatal death. |
| 722 | COA7-related Cytochrome c oxidase assembly factor 7 deficiency | UNMAPPED | Reject COA3 as exact; true COA7 complex IV assembly gap with ataxia, developmental delay, peripheral neuropathy, and leukodystrophy. |
| 723 | COX10-related Cytochrome c oxidase assembly factor 10 deficiency | UNMAPPED | False negative; resolve to exact `COX10-Related_COX_Deficiency.yaml`, preserving source alternate-name anomaly and IEMbase glucose, hemoglobin/anemia, cardiomyopathy, renal, developmental, and hypotonia prompts. |
| 724 | COX14-related Cytochrome c oxidase assembly factor 14 deficiency | UNMAPPED | False negative; resolve to exact `COX14-Related_COX_Deficiency.yaml`, with IEMbase adding explicit cardiomyopathy and perinatal-death prompts to local fatal neonatal lactic acidosis and COX I assembly mechanism. |
| 725 | COX15-related Cytochrome c oxidase assembly factor 15 deficiency | MAPPED | Correct exact mapping to `COX15-Related_COX_Deficiency.yaml`; IEMbase adds age-banded lactate, basal ganglia MRI, hypotonia, Leigh, perinatal-death, developmental-delay, and epilepsy prompts. |

## Batch 62

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 726 | COX20-related Cytochrome c oxidase assembly factor 20 deficiency | UNMAPPED | False negative; resolve to exact `COX20-Related_COX_Deficiency.yaml`, with IEMbase adding age-banded normal-to-high lactate to local ataxia, hypotonia, dystonia, dysarthria, areflexia, sensory neuropathy, and COX2-maturation mechanism. |
| 727 | SCO1-related Mitochondrial complex IV deficiency | MAPPED | Correct exact mapping to `SCO1-Related_COX_Deficiency.yaml`; IEMbase adds alanine, dicarboxylic acids, CSF/plasma/urine lactate, brain atrophy, hypertrophic cardiomyopathy, neonatal hepatic/respiratory/feeding features, and perinatal-death prompts. |
| 728 | SCO2-related Myopia 6 | MAPPED | Correct for the fatal infantile cardioencephalomyopathy alternate identity, but preserve the source primary-label caveat; IEMbase adds detailed neurologic, neuromuscular, respiratory, ocular-motor, and age-banded lactate prompts. |
| 729 | SURF1-related COX IV deficiency | UNMAPPED | False negative; resolve to exact `SURF1-Related_Leigh_Syndrome.yaml`, with IEMbase adding basal-ganglia/brainstem MRI, hypertrichosis, ophthalmoplegia, tremor, nystagmus, feeding/vomiting, cardiomyopathy, optic, respiratory, and perinatal-death prompts. |
| 730 | COX4I2-related Cytochrome c oxidase subunit 4I2 deficiency | MAPPED | Correct exact EPIDACH mapping to `COX4I2-Related_Pancreatic_Insufficiency-Anemia-Hyperostosis_Syndrome.yaml`; IEMbase adds hepatomegaly, splenomegaly, and failure-to-thrive prompts while local captures anemia, hyperostosis, malabsorption, and mechanism. |
| 731 | COX6A1 related Cytochrome c oxidase subunit 6A1 deficiency | UNMAPPED | Reject COX6A2 as exact; true COX6A1/recessive intermediate Charcot-Marie-Tooth disease type D gap with hearing loss and progressive polyneuropathy. |
| 732 | COX6B1-related Cytochrome c oxidase subunit 6B1 deficiency | UNMAPPED | False negative; resolve to exact `COX6B1-Related_COX_Deficiency.yaml`, with IEMbase adding lactate, leukodystrophy, myopathy, and epilepsy prompts to local encephalopathy, hydrocephalus, cardiomyopathy, and structural-subunit mechanism. |
| 733 | COX7B-related Cytochrome c oxidase subunit 7B deficiency | UNMAPPED | Reject COX6B1 as exact; true COX7B/linear skin defects with multiple congenital anomalies 2 gap with X-linked inheritance, microcephaly, short stature, and linear skin defects. |
| 734 | COX8A-related Cytochrome c oxidase subunit 8A deficiency | UNMAPPED | False negative; resolve to exact `COX8A-Related_COX_Deficiency.yaml`, with IEMbase adding microcephaly, developmental delay, and pulmonary hypertension prompts to local epilepsy, leukodystrophy, Leigh-like syndrome, and structural-subunit mechanism. |
| 735 | MT-CO1-related Cytochrome c oxidase subunit 1 deficiency | UNMAPPED | Reject COX4I1 as exact; true MT-CO1 mtDNA-encoded complex IV gap with alanine, rhabdomyolysis, stroke-like episodes, epilepsy, and muscle weakness; review source inheritance before modeling. |

## Batch 63

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 736 | MT-CO2-related Cytochrome c oxidase subunit 2 deficiency | UNMAPPED | Reject COX4I1 as exact; true MT-CO2 mtDNA-encoded complex IV gap with age-banded lactate, myopathy, muscle weakness, cardiomyopathy, developmental delay, and retinopathy prompts. |
| 737 | MT-CO3-related Cytochrome c oxidase subunit 3 deficiency | UNMAPPED | Reject COX4I1 as exact; true MT-CO3 mtDNA-encoded complex IV gap with lactate, myopathy, weakness, possible Leigh syndrome, and psychomotor-delay prompts. |
| 738 | ATPAF2-related Mitochondrial ATP synthase F1 assembly factor 2 deficiency | CANDIDATE | Reject SURF1 complex IV candidate; true ATPAF2 complex V assembly gap with neonatal organic acids, lactate, neuroimaging, renal/hepatic, dysmorphology, seizure, feeding/FTT, and perinatal-death prompts. |
| 739 | ATP5F1A-related Mitochondrial ATP synthase F1 subunit alpha deficiency | CANDIDATE | Reject SCO1 complex IV candidate; true ATP5F1A complex V gap with alanine, asymmetric white matter lesions, irritability, nystagmus, hypotonia, microcephaly, and perinatal-death prompts. |
| 740 | ATP5F1E-related Mitochondrial ATP synthase F1 subunit epsilon deficiency | CANDIDATE | Reject COX10 complex IV candidate; true ATP5F1E complex V gap with adult lactate, hypertrophic cardiomyopathy, hypotonia, polyneuropathy, and psychomotor-delay prompts. |
| 741 | MT-ATP6-related Mitochondrial ATP synthase F0 subunit 6 deficiency | UNMAPPED | False negative; resolve primarily to `NARP_syndrome.yaml`, with `Myopathy_Lactic_Acidosis_and_Sideroblastic_Anemia.yaml` as MLASA3 context and IEMbase adding broad NARP/MILS, sideroblastic anemia, cardiomyopathy, EEG, stroke-like, ocular, retinal, neuropathy, and lactate prompts. |
| 742 | MT-ATP8-related Mitochondrial ATP synthase F0 subunit 8 deficiency | UNMAPPED | Reject HMGCS candidate; true MT-ATP8 complex V gap with partial MT-ATP6/8 context in `NARP_syndrome.yaml`, preserving adolescent neurologic, visual, neuropathy, cardiomyopathy, and lactate prompts. |
| 744 | MT-CYB-related Mitochondrial cytochrome b deficiency | UNMAPPED | Reject HMGCS candidate; true MT-CYB mtDNA-encoded complex III gap with lactate, 3-methylglutaconic acid, CK/transaminases, exercise intolerance, proximal weakness, neuropathy, seizures, neuroimaging, ocular/auditory, gastrointestinal, and cardiomyopathy prompts. |
| 745 | CYC1-related Mitochondrial cytochrome c1 deficiency | CANDIDATE | Reject COX4I1 complex IV candidate; true CYC1 complex III nuclear type 6 gap with lactate, hyperammonemia, lactic acidosis, episodic encephalopathy, seizures, liver failure, FTT, and hyperglycemia prompts. |
| 746 | CYCS-related Mitochondrial cytochrome c deficiency | UNMAPPED | False negative; resolve to exact `CYCS-Related_Thrombocytopenia.yaml`, preserving the source label caveat and low thrombocytes/thrombocytopenia phenotype while local adds CYCS respiratory/apoptosis and megakaryocyte-release mechanism. |

## Batch 64

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 747 | HCCS-related Holocytochrome c synthase deficiency | UNMAPPED | Reject HMGCS2 ketogenesis candidate; true HCCS / linear skin defects with multiple congenital anomalies type 1 gap with ocular, skin, neurologic, cardiac, growth, and severe survival prompts. |
| 748 | ACSL4-related Long-chain fatty acid-CoA ligase 4 deficiency | UNMAPPED | Reject VLCAD candidate; true ACSL4 / X-linked intellectual disability 63 gap with decreased enzyme activity in fibroblasts and white blood cells plus intellectual disability. |
| 749 | AGPAT2-related Lysophosphatidic acid acyltransferase deficiency | MAPPED | Correct exact mapping to `Berardinelli_Seip_Congenital_Lipodystrophy.yaml`; local CGL1/AGPAT2 coverage captures lipodystrophy, insulin resistance/diabetes, hypertriglyceridemia, hepatomegaly, steatosis, and acylglycerol mechanism. |
| 750 | LPIN1-related Lipin 1 deficiency | UNMAPPED | Reject multiple pterygium candidate; true LPIN1 recurrent rhabdomyolysis gap with very high CK, myoglobinuria, muscle cramps, episodic/exercise-induced rhabdomyolysis, acute renal failure, and possible death. |
| 751 | LPIN2-related Lipin 2 deficiency | UNMAPPED | True LPIN2 / Majeed syndrome gap with inflammatory bone disease, recurrent fever, psoriasiform dermatitis, microcytic/dyserythropoietic anemia, neutropenia, hepatosplenomegaly, jaundice, ESR, and transaminase prompts. |
| 752 | DGAT1-related Diacylglycerol acyltransferase deficiency | UNMAPPED | Reject Travelers' diarrhea candidate; true DGAT1 / congenital diarrhea type 7 gap with chronic diarrhea, protein-losing enteropathy, hypoalbuminemia, low IgG, immunodeficiency, recurrent infection, anemia, acidosis, FTT, and transaminase prompts. |
| 753 | ABHD5-related 1-Acylglycerol-3-phosphate O-acyltransferase deficiency | AMBIGUOUS | Exact local coverage exists, best resolved to `Dorfman_Chanarin_Disease.yaml`; `Triglyceride_Storage_Disease_Type_1.yaml` appears duplicate/synonymous and should be reconciled while preserving leukocyte vacuole, short stature, and ID prompts. |
| 754 | PNPLA2-related Adipose triglyceride lipase deficiency | MAPPED | Correct exact mapping to `Neutral_Lipid_Storage_Myopathy.yaml`; local core PNPLA2/NLSDM coverage is strong for myopathy, hyperCKemia, lipid storage, cardiomyopathy, and ATGL mechanism, with hepatic/metabolic/Jordans prompts to check. |
| 755 | PLIN1-related Perilipin 1 deficiency | UNMAPPED | False negative/partial coverage via `Familial_Partial_Lipodystrophy.yaml` FPLD4 subtype; local group-level FPLD coverage captures core lipodystrophy/metabolic features but lacks PLIN1-specific cholesterol, low BMI, cushingoid, ovarian failure, and stroke prompts. |
| 756 | LIPE-related Hormone-sensitive lipase deficiency | UNMAPPED | False negative/partial coverage via `Familial_Partial_Lipodystrophy.yaml` FPLD6 subtype; local group-level FPLD coverage captures core lipodystrophy/metabolic features but needs LIPE-specific CK, cholesterol, low BMI, and adult-onset prompts. |

## Batch 65

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 759 | PTDSS1-related Phosphatidylserine synthase 1 superactivity | AMBIGUOUS | Exact disease-file coverage in `Lenz-Majewski_hyperostotic_dwarfism.yaml`; ambiguity reflects local Classic/Attenuated subtype matches, while IEMbase adds detailed skeletal, craniofacial, genitourinary, gastrointestinal, and neurodevelopmental prompts. |
| 760 | PLA2G6-related Phospholipase A2 group 6 deficiency | MAPPED | Correct mapping to `Neurodegeneration_With_Brain_Iron_Accumulation.yaml` PLAN subtype, with `Adult_Onset_Dystonia_Parkinsonism.yaml` as narrower spectrum context; IEMbase adds ocular, electrophysiology, seizure, peripheral nerve, and neuroaxonal-dystrophy prompts. |
| 761 | DDHD1-related Phosphatidic acid-preferring phospholipase 1 deficiency | UNMAPPED | Reject SCYL1/CALFAN candidate; true DDHD1/SPG28 gap with spastic paraparesis, ataxia, polyneuropathy, retinal/cone-rod dystrophy, optic atrophy, intellectual disability, basal-ganglia, and brain-iron prompts. |
| 762 | DDHD2-related Phosphatidic acid-preferring phospholipase 2 deficiency | UNMAPPED | Reject ALDH18A1/SPG9 candidate; true DDHD2/SPG54 gap with developmental delay, behavioral disorder, microcephaly, spastic paraparesis, pyramidal signs, bulbar dysfunction, abnormal eye movements, brainstem/cerebellar/corpus-callosum MRI prompts, and source OMIM review needed. |
| 763 | PNPLA6-related Spastic paraplegia type 39 | UNMAPPED | False negative/partial coverage via `Boucher-Neuhauser_Syndrome.yaml`, which is locally curated as a PNPLA6 spectrum entry including SPG39; preserve GH deficiency, hypothyroidism, chorioretinal degeneration, hypogonadotropic hypogonadism, neuropathy, spasticity, and ataxia prompts. |
| 764 | CYP2U1-related Spastic paraplegia 56 | CANDIDATE | Reject GBA2/SPG46 candidate; true CYP2U1/SPG56 gap with CSF 5-MTHF, basal-ganglia calcification, pigmentary maculopathy, thin corpus callosum, dystonia, neuropathy, intellectual disability, psychomotor regression, and spastic paraplegia prompts. |
| 765 | ABHD12-related Polyneuropathy, hearing loss, ataxia, retinitis pigmentosa, and cataract syndrome | UNMAPPED | False negative; exact local coverage exists in `PHARC_syndrome.yaml`, which covers ABHD12, lysophosphatidylserine mechanism, peripheral neuropathy, hearing loss, ataxia, retinitis pigmentosa, and cataract. |
| 766 | TBXAS1-related Thromboxane synthase deficiency | UNMAPPED | Reject HMGCS2 ketogenesis candidate; true TBXAS1/Ghosal hematodiaphyseal syndrome gap with diaphyseal/metaphyseal thickening, anemia, bone pain/swelling, thrombocytopenia, leukocytosis, splenomegaly, and cutis verticis gyrata prompts. |
| 767 | HPGD-related 15-Hydroxy-prostaglandin dehydrogenase deficiency | CANDIDATE | Accept `Primary_Hypertrophic_Osteoarthropathy.yaml` PHOAR1 subtype as exact local coverage; concordant for HPGD/PGE2 mechanism and PHO triad, with IEMbase normal PGE-M conflicting with local decreased PHOAR1 PGE-M evidence and needing review. |
| 768 | SLCO2A1-related Prostaglandin transporter deficiency | CANDIDATE | Accept `Primary_Hypertrophic_Osteoarthropathy.yaml` PHOAR2 subtype as exact local coverage; concordant for SLCO2A1, high urinary PGE2/PGE-M, PHO triad, anemia, myelofibrosis, and peptic ulcer, with chronic gastritis as a completeness prompt. |

## Batch 66

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 769 | TREX1-related 3-prime repair exonuclease 1 deficiency | AMBIGUOUS | Exact subtype coverage in `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 1; ambiguity reflects disease-level plus subtype match, with CSF neopterin, feeding, sleep, startle, platelet, and optional cardiopulmonary/ocular rows as prompts. |
| 770 | RNASEH2B-related ribonuclease H2 subunit B deficiency | AMBIGUOUS | Exact subtype coverage in `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 2; preserve local RNASEH2B IFN-negative nuance while treating IEMbase CSF neopterin, feeding, sleep, startle, and platelet rows as prompts. |
| 773 | RNASET2-related ribonuclease T2 deficiency | UNMAPPED | Reject `COA8-Related_COX_Deficiency.yaml`; true RNASET2 cystic leukoencephalopathy gap with congenital cystic leukoencephalopathy without megalencephaly, calcifications, microcephaly, spasticity, psychomotor delay, seizures, movement disorder, and hearing-loss prompts. |
| 774 | SAMHD1-related stenosis, aneurysm, moyamoya and stroke association | AMBIGUOUS | Exact subtype coverage in `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 5; local captures SAMHD1 vasculopathy mostly in mechanism/prose, while IEMbase adds explicit stenosis, aneurysm, moyamoya, and stroke prompts. |
| 775 | ADAR-related RNA-specific adenosine deaminase deficiency | AMBIGUOUS | Exact subtype coverage in `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 6; IEMbase usefully highlights bilateral striatal degeneration as an ADAR-specific phenotype prompt. |
| 776 | IFIH1-related MDA5 superactivity | AMBIGUOUS | Exact subtype coverage in `Aicardi_Goutieres_Syndrome.yaml` subtype Aicardi-Goutieres syndrome 7; concordant for dominant IFIH1 gain-of-function AGS, with isolated spastic paraparesis and CSF neopterin as prompts. |
| 777 | TMEM173-related STING superactivity | MAPPED | Correct exact mapping to `STING_Associated_Vasculopathy_with_Onset_in_Infancy.yaml`; local captures STING1/TMEM173 gain-of-function, interferonopathy, ILD, vasculopathy, arthritis, and JAK context, while IEMbase adds immune-lab, recurrent infection, lymphadenopathy, nail, and gangrenous vasculopathy prompts. |
| 778 | OAS1-related 2-prime,5-prime-oligoadenylate synthetase 1 deficiency | UNMAPPED | Reject `Holocarboxylase_Synthetase_Deficiency.yaml` and do not collapse into CSF2RA/CSF2RB hereditary PAP; true OAS1/PAPHG gap with pulmonary alveolar proteinosis, hypogammaglobulinemia, viral susceptibility, leukocyte-count ambiguity, small non-foamy macrophages, and early-death prompts. |
| 779 | ABCC6-related generalized arterial calcification of infancy type 2 | AMBIGUOUS | Exact subtype coverage in `Arterial_Calcification_of_Infancy.yaml` subtype ABCC6-related; preserve ABCC6-vs-ENPP1 distinction and review renal/coronary/valve/joint calcification, myocardial infarction, nephrocalcinosis, and low-frequency ABCC6 rickets prompts. |
| 780 | ENPP1-related ectonucleotide pyrophosphatase-phosphodiesterase 1 deficiency | AMBIGUOUS | Exact subtype coverage in `Arterial_Calcification_of_Infancy.yaml` subtype ENPP1-related; local captures PPi/FGF23/rickets/hearing-loss mechanism, while IEMbase adds prenatal, dental, angioid-streak, renal/coronary/valve, myocardial infarction, and joint-calcification prompts. |

## Batch 67

| IEMbase ID | IEMbase disease | Generated mapping status | Manual conclusion |
|---:|---|---|---|
| 781 | ENPP1-related Ectonucleotide pyrophosphatase-phosphodiesterase 1 dimerization deficiency | UNMAPPED | True local gap for autosomal dominant Cole disease; reject ENPP1-related GACI because local ENPP1 coverage is recessive arterial calcification/rickets rather than dimerization-defect palmoplantar keratoderma, hypopigmented macules, calcinosis, and tendinopathy. |
| 782 | NT5E-related Ecto-5'-nucleotidase deficiency | MAPPED | Correct exact mapping to `Hereditary_Arterial_and_Articular_Multiple_Calcification_Syndrome.yaml`; local captures CD73/adenosine/TNAP/PPi mechanism, arterial and periarticular calcification, claudication, joint disease, etidronate, and support care; IEMbase adds tendon and valve/aortic-ring prompts. |
| 783 | SLC29A1-related Equilibrative nucleoside transporter 1 deficiency | UNMAPPED | True local gap for SLC29A1/ENT1 Augustine-null blood type with ectopic mineralization; reject `SLC35A2-CDG.yaml` and incidental ENT1 transporter mentions. |
| 784 | SLC29A3-related Equilibrative nucleoside transporter 3 deficiency | UNMAPPED | Partial local context exists in `Rosai-Dorfman_Disease.yaml` for familial RDD/Faisalabad histiocytosis and SLC29A3, but no exact broad H-syndrome/SLC29A3-spectrum target exists; IEMbase adds endocrine, skeletal, pigmentary, deafness, and inflammatory prompts. |
| 785 | AICDA-related Activation-induced cytidine deaminase deficiency | UNMAPPED | True local gap for AICDA/HIGM2; reject ADA-SCID and generic hyper-IgM-like neighbors because local entries do not capture AICDA class-switch failure, giant germinal centers, low IgG/IgA/IgE, normal B-cell counts, and normal-to-high IgM. |
| 786 | UNG-related Uracil-DNA glycosylase deficiency | UNMAPPED | True local gap for UNG/HIGM5; reject IKBKG and other hyper-IgM-like neighbors because they have different genes and mechanisms despite overlapping class-switch phenotypes. |
| 788 | AMPD2-related Adenosine monophosphate deaminase 3 deficiency | CANDIDATE | Reject generated `Pontocerebellar_Hypoplasia.yaml#PCH2` candidate; broad PCH context exists but no AMPD2/PCH9 subtype is modeled locally, so preserve microcephaly, seizures, psychomotor delay, and dysmorphic craniofacial prompts as a gap. |
| 789 | AMPD3-related Erythrocyte adenosine monophosphate deaminase 3 deficiency | UNMAPPED | True local gap and likely low-priority trait; IEMbase reports no clinical significance, so do not over-map to hereditary orotic aciduria or symptomatic purine/red-cell disorders. |
| 790 | ADA2-related Adenosine deaminase 2 deficiency | UNMAPPED | False negative; exact local coverage exists in `Deficiency_of_Adenosine_Deaminase_2.yaml`, with concordant ADA2/CECR1, low enzyme activity, recessive inheritance, and polyarteritis-nodosa vasculopathy; Sneddon-like disease is a phenotype prompt, not a separate mapping. |
| 791 | AK1-related Adenylate kinase 1 deficiency | UNMAPPED | True local gap for AK1 nonspherocytic hemolytic anemia with low RBC adenylate kinase activity and basophilic stippling; reject adenosine kinase deficiency, lead poisoning, and generic hemolytic anemia entries as exact coverage. |

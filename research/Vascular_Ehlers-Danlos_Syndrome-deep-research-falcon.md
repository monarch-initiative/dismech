---
title: Vascular Ehlers-Danlos Syndrome deep research
keywords:
- disease
- ehlers-danlos
- vascular
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-13T17:03:21.278578'
end_time: '2026-06-13T17:24:03.143793'
duration_seconds: 1241.87
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_tokens: 12000
    max_embedded_images: 8
citation_count: 54
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Vascular_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Vascular_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

Prepare a focused, citation-rich deep research report for a dismech Disease entry called 'Vascular Ehlers-Danlos Syndrome'. Research objectives: define disease boundary and synonyms; summarize COL3A1/type III collagen genetics, autosomal dominant inheritance, dominant-negative versus haploinsufficiency genotype-phenotype differences, vascular wall and hollow-organ fragility mechanisms, fibroblast/collagen fibrillogenesis evidence, key phenotypes including arterial rupture/dissection, thin translucent skin, easy bruising, intestinal and uterine rupture, pneumothorax or pulmonary manifestations where relevant; summarize surveillance and treatment evidence including celiprolol, beta-blocker/ARB observational evidence, avoidance of invasive procedures, and emergency care; identify MONDO, HPO, HGNC, GO, and MAXO terms suitable for dismech YAML; include primary literature, GeneReviews, and authoritative reviews with PMID identifiers; flag evidence limitations and model-system caveats. Do not invent citations; provide exact PMID identifiers for key claims and prefer PubMed-indexed sources.

## Output

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

Prepare a focused, citation-rich deep research report for a dismech Disease entry called 'Vascular Ehlers-Danlos Syndrome'. Research objectives: define disease boundary and synonyms; summarize COL3A1/type III collagen genetics, autosomal dominant inheritance, dominant-negative versus haploinsufficiency genotype-phenotype differences, vascular wall and hollow-organ fragility mechanisms, fibroblast/collagen fibrillogenesis evidence, key phenotypes including arterial rupture/dissection, thin translucent skin, easy bruising, intestinal and uterine rupture, pneumothorax or pulmonary manifestations where relevant; summarize surveillance and treatment evidence including celiprolol, beta-blocker/ARB observational evidence, avoidance of invasive procedures, and emergency care; identify MONDO, HPO, HGNC, GO, and MAXO terms suitable for dismech YAML; include primary literature, GeneReviews, and authoritative reviews with PMID identifiers; flag evidence limitations and model-system caveats. Do not invent citations; provide exact PMID identifiers for key claims and prefer PubMed-indexed sources.

## Vascular Ehlers–Danlos Syndrome (vEDS) — Deep Research Report (dismech Disease Entry)

### Executive summary
Vascular Ehlers–Danlos syndrome (vEDS; “EDS type IV”) is a monogenic connective-tissue disorder defined by *generalized tissue fragility* with disproportionate risk of **arterial dissection/aneurysm/rupture** and **hollow-organ rupture** (especially sigmoid colon and gravid uterus), plus characteristic external clues such as **thin translucent skin** and **easy bruising**. Diagnosis is established by identifying a **heterozygous pathogenic/likely pathogenic variant in COL3A1** (type III procollagen). Contemporary management emphasizes (i) avoidance of high-risk invasive procedures, (ii) structured vascular surveillance, and (iii) rapid emergency evaluation for sudden pain suggestive of dissection/rupture. Drug-prevention evidence is dominated by celiprolol (trial-era data plus heterogeneous real-world cohorts), while observational cohorts suggest possible benefit of beta-blocker and/or ARB therapy; overall evidence remains limited by small samples, retrospective designs, and variant heterogeneity. (byers2025vascularehlersdanlossyndrome pages 1-3, bowen2023diagnosisandmanagement pages 8-11, buso2024currentevidenceand pages 1-2)


## 1) Key concepts, disease boundary, and synonyms (current understanding)

### Disease definition / boundary
GeneReviews defines vEDS as a disorder marked by **arterial, intestinal, and/or uterine fragility**, **thin translucent skin**, **easy bruising**, characteristic facial features, and acrogeric/aged-appearing extremities. Diagnosis is *molecular*: a **heterozygous COL3A1 pathogenic variant** establishes the diagnosis. (byers2025vascularehlersdanlossyndrome pages 1-3)

Key boundary points that separate vEDS from other EDS types in practice:
- vEDS is dominated by **vascular and hollow-organ catastrophes** rather than generalized large-joint hypermobility (which can be mild or absent). (pepin2014survivalisaffected pages 1-2, bowen2023diagnosisandmanagement pages 1-2)
- Confirmatory genetic testing is considered necessary to distinguish vEDS from overlapping presentations in other heritable aortopathies/fragility syndromes. (bowen2023diagnosisandmanagement pages 1-2, byers2025vascularehlersdanlossyndrome pages 1-3)

### Synonyms (for dismech normalization)
- “Vascular Ehlers–Danlos syndrome” (vEDS) (byers2025vascularehlersdanlossyndrome pages 1-3)
- “Ehlers–Danlos syndrome type IV” / “EDS type IV” (schwarze2001haploinsufficiencyforone pages 1-2, pepin2014survivalisaffected pages 1-2)
- “Vascular-type EDS” / “vascular EDS” (ishikawa2023clinicalfeaturesand pages 1-2)

### Core identifiers available from retrieved sources
- **OMIM**: vEDS / EDS type IV = **OMIM 130050** (schwarze2001haploinsufficiencyforone pages 1-2, byers2025vascularehlersdanlossyndrome pages 1-3)
- **PMID (explicitly present in retrieved text)**: GeneReviews is cited with **PMID: 20301667** (foehr2025vascularehlersdanlossyndrome pages 3-4)

*Limitation:* MONDO, HGNC, HPO, GO, and MAXO *numeric identifiers* were not present in the retrieved texts and therefore cannot be reported “exactly” here without external ontology lookup; terms are provided with “needs lookup” flags below. (byers2025vascularehlersdanlossyndrome pages 1-3)


## 2) COL3A1 / type III collagen genetics (inheritance, dominant-negative vs haploinsufficiency)

### COL3A1 biology and why it matters
Type III collagen is a fibrillar collagen enriched in **blood-vessel walls and hollow organs**, consistent with the tissue distribution of fragility in vEDS. (omar2021fourdecadesin pages 2-4, chiarelli2018transcriptomeanalysisof pages 1-2)

### Inheritance and de novo rate
vEDS is **autosomal dominant**, and approximately **half of affected individuals may lack an apparent family history**, consistent with de novo pathogenic variants being common. (byers2025vascularehlersdanlossyndrome pages 1-3, schwarze2001haploinsufficiencyforone pages 1-2)

### Variant classes and molecular mechanisms
Two broad, clinically useful mechanisms are consistently described:

1) **Dominant-negative (DN) mechanisms** (typical for glycine substitutions and many splice variants)
- Collagen III is a **homotrimer**; with equal mutant and wild-type chain production, **7/8 of trimers are expected to be abnormal** (dominant-negative burden), a classic explanation for severity. (omar2021fourdecadesin pages 4-5)
- Dominant-negative variants disrupt triple helix folding, causing **misfolding in the endoplasmic reticulum (ER)** and **retention of misfolded procollagen trimers** (described as retention of “seven eighths” of misfolded trimers), consistent with ER stress phenotypes. (chiarelli2018transcriptomeanalysisof pages 1-2)
- In a large adult cohort, **80.6%** of variants were classified as DN by predicted functional consequence. (adham2022assessmentofarterial pages 1-2)

2) **Haploinsufficiency (HI) / loss-of-function** mechanisms
- Frameshift and some nonsense variants can produce **premature termination codons**, triggering **nonsense-mediated mRNA decay (NMD)** and functional haploinsufficiency. (schwarze2001haploinsufficiencyforone pages 1-2)
- A terminal-exon nonsense mutation can yield stable mRNA but a **truncated chain that does not incorporate into mature procollagen**, still producing reduced functional collagen III. (schwarze2001haploinsufficiencyforone pages 1-2)
- In the Adham 2022 cohort, **19.4%** of variants were classified as HI. (adham2022assessmentofarterial pages 1-2)

### Genotype–phenotype: DN vs HI and other correlations
**Across cohorts and reviews, DN variants correlate with earlier/more severe disease**, while **HI (null) variants trend milder with later onset**:
- Adham 2022: DN variants associated with **earlier onset/more severe course** and higher prevalence of **medium-sized artery lesions**, especially supra-aortic trunks and renal arteries. (adham2022assessmentofarterial pages 1-2)
- Omar 2021: null variants (~5%) yield ~50% collagen III and are described as **milder**, with older median age at diagnosis (~46 years in the excerpted review), whereas **in-frame exon-skipping splice variants** are associated with earlier onset and severe outcomes; glycine substitutions are more severe when glycine is replaced by bulky/charged residues. (omar2021fourdecadesin pages 4-5, omar2021fourdecadesin pages 2-4)
- Buso 2024 (Vascular Medicine cohort summary) states HI is linked to a **milder phenotype with almost two-decade delayed onset**. (buso2024despiteceliprololtherapy pages 1-2)

**Natural history varies by mutation type and sex** in a very large assembled cohort (1,231 individuals), with **median survival 51 years** and survival influenced by gender and mutation type. (pepin2014survivalisaffected pages 1-2)


## 3) Mechanisms of vascular wall and hollow-organ fragility

### Vascular and hollow-organ fragility as a type III collagen disorder
At the tissue level, the dominant clinical problem is mechanical failure (dissection/rupture/perforation) in collagen III–rich tissues including arteries and bowel/uterus. (byers2025vascularehlersdanlossyndrome pages 1-3, ishikawa2023clinicalfeaturesand pages 1-2)

### Fibroblast / ECM evidence (fibrillogenesis and matrix remodeling)
**Patient-derived dermal fibroblasts (dominant-negative COL3A1)** show coordinated disturbances that extend beyond type III collagen itself:
- Transcriptome profiling highlights changes in pathways involving **ER homeostasis**, collagen folding, and **ECM organization**. (chiarelli2018transcriptomeanalysisof pages 1-2)
- Protein-level changes include disassembly/reduction of multiple ECM constituents (e.g., **fibrillins, EMILINs, elastin**) and proteoglycans (**perlecan, decorin, versican**) important for vascular integrity, consistent with secondary ECM destabilization. (chiarelli2018transcriptomeanalysisof pages 1-2)

### Ultrastructural fibrillogenesis evidence (human tissue)
In a 2023 electron microscopy study of skin samples, collagen fibrils in vEDS showed significantly increased **irregularity of fibril size** versus controls, supporting disturbed fibrillogenesis at the tissue-architecture level; variability between patients was noted, and ER stress was proposed as a contributor to phenotypic variability (e.g., via effects on fibril-associated proteins such as COMP). (ishikawa2023clinicalfeaturesand pages 1-2)

### Model systems and caveats (mouse models)
Animal models support a causal role of collagen III deficiency/mutation in vascular catastrophe, but also illustrate translation limitations:
- **Homozygous Col3a1 knockout**: severe perinatal mortality and catastrophic vessel/intestinal rupture; this extreme phenotype is not typical of most human vEDS (where complete absence of collagen III is rare). (vroman2021animalmodelsof pages 13-14)
- **Heterozygous haploinsufficient** models: may appear grossly normal early but show age-dependent aortic pathology and reduced wall strength; sex effects (male bias) are reported. (vroman2021animalmodelsof pages 13-14)
- **In-frame deletion or glycine-substitution models**: can show sudden aortic dissection/rupture with incomplete penetrance; some models lack prominent skin/GI defects, i.e., partial phenocopy. (vroman2021animalmodelsof pages 13-14, omar2021fourdecadesin pages 5-6)
- Overexpression transgenic models may introduce artifacts due to supra-physiological collagen III levels. (omar2021fourdecadesin pages 5-6)

**Interpretation caveat:** vEDS is strongly variant-class dependent; model selection should match the human mutation mechanism (DN vs HI) and consider penetrance/sex differences. (omar2021fourdecadesin pages 13-14, omar2021fourdecadesin pages 5-6)


## 4) Phenotypes and recent quantitative data (prioritizing 2023–2024)

### Hallmark phenotypes (clinical spectrum)
Core phenotypes across authoritative sources include:
- **Arterial**: aneurysm, arteriovenous fistulae, dissection, spontaneous rupture (byers2025vascularehlersdanlossyndrome pages 1-3)
- **Skin/soft tissue**: thin translucent skin, easy bruising, acrogeria/aged extremities, facial features; small-joint hypermobility may occur (byers2025vascularehlersdanlossyndrome pages 1-3, adham2022assessmentofarterial pages 1-2)
- **Hollow organ**: sigmoid colon rupture/perforation; uterine rupture in pregnancy (byers2025vascularehlersdanlossyndrome pages 1-3)
- **Pulmonary/pleural**: spontaneous/recurrent pneumothorax; hemothorax/hemopneumothorax; hemoptysis is reported (byers2025vascularehlersdanlossyndrome pages 1-3)
- **Other suggestive vascular presentations**: carotid–cavernous sinus fistula (byers2025vascularehlersdanlossyndrome pages 5-7)

### Recent quantitative complication rates (2023 systematic review)
A 2023 systematic review of extracutaneous features across EDS subtypes reported for vEDS:
- **Cerebrovascular events:** 25/153 (16.3%) (doolan2023extracutaneousfeaturesand pages 1-2)
- **Aneurysm:** 77/245 (31.4%) (doolan2023extracutaneousfeaturesand pages 1-2)
- **Arterial dissection/rupture:** 89/250 (35.5%) (doolan2023extracutaneousfeaturesand pages 1-2)
- “Pneumothorax/hemothorax” and bowel perforation were described as almost entirely exclusive to vEDS; mean age at first **pneumothorax/hemothorax 25.6 ± 9.0 years** and mean age at first **bowel perforation 26.6 ± 10.9 years** (doolan2023extracutaneousfeaturesand pages 3-4)

*Interpretation caveat:* denominators vary by complication, implying heterogeneous reporting rather than a single prospective cohort frequency. (doolan2023extracutaneousfeaturesand pages 1-2)

### GeneReviews quantitative features (selected)
- **GI perforation:** ~15% of individuals with COL3A1 pathogenic variants; seldom seen with null variants. (byers2025vascularehlersdanlossyndrome pages 5-7)
- **Carotid–cavernous sinus fistula:** as many as ~10% (female preponderance). (byers2025vascularehlersdanlossyndrome pages 5-7)
- **Arterial rupture location distribution:** thorax/abdomen 66%, head/neck 17%, extremities 17%. (byers2025vascularehlersdanlossyndrome pages 5-7)
- **Pregnancy risk:** ~5% maternal mortality per pregnancy. (byers2025vascularehlersdanlossyndrome pages 1-3)

### Natural history statistics from recent cohorts/reviews
- A 2024 prevention-focused review summarizes: historical median survival ~50 years; arterial complication rate ~1.3 events per 5 years; overall organ complication rate ~1.6 events per 5 years; up to 85% have major complications by age 43. (buso2024currentevidenceand pages 1-2)
- A 2023 EM-based clinical series states most patients have a first major complication in early 20s and >80% have ≥1 complication by age 40, with mean life expectancy ~48 years. (ishikawa2023clinicalfeaturesand pages 1-2)


## 5) Current applications and real-world implementations (surveillance, avoidance, emergency care)

### Surveillance strategies
GeneReviews recommends **periodic arterial imaging** (ultrasound, MRA, CTA with/without venous contrast) and regular blood pressure monitoring. (byers2025vascularehlersdanlossyndrome pages 1-3)

A UK national service describes a concrete, implementable protocol:
- **Annual MRA** from thoracic/abdominal aorta through cervical vessels (including circle of Willis) down to pelvis/upper legs; **CTA used sparingly**, targeted to MRA abnormalities. (bowen2023diagnosisandmanagement pages 8-11)

*A key evidence gap:* the direct mortality benefit of surveillance intervals is uncertain; practice varies by center and genotype (e.g., shorter intervals for DN variants are suggested in a vascular-surgery perspective piece). (schonherr2024diagnosisofvascular pages 2-3)

### Avoidance of invasive procedures and procedure planning
GeneReviews and specialty cohorts emphasize avoiding or limiting:
- **Arteriography** except for life-threatening bleeding (byers2025vascularehlersdanlossyndrome pages 1-3)
- **Routine colonoscopy** without symptoms/indication (byers2025vascularehlersdanlossyndrome pages 1-3)
- Elective surgery when benefit is limited (byers2025vascularehlersdanlossyndrome pages 1-3)

The UK service operationalizes this with bowel-specific practice:
- Colonoscopy is avoided where possible given perforation risk; after perforation, total colectomy with ileostomy may be considered to reduce re-perforation, and colostomies are often not reversed. (bowen2023diagnosisandmanagement pages 8-11)

### Emergency care implementation
GeneReviews stresses practical emergency readiness: carry documentation of the genetic diagnosis and seek prompt evaluation for **sudden unexplained pain** (a potential sentinel symptom of dissection/rupture). (byers2025vascularehlersdanlossyndrome pages 1-3)
The UK service uses emergency information cards and electronic record alerts to mitigate delays/mismanagement in emergency departments. (bowen2023diagnosisandmanagement pages 8-11)


## 6) Treatment and prevention evidence (celiprolol; beta-blockers/ARBs)

### Celiprolol
- A 2024 narrative review summarizes the BBEST trial signal as a **64% reduction in risk of arterial rupture/dissection** with celiprolol versus controls, while noting the overall evidence base remains limited. (buso2024currentevidenceand pages 1-2)
- Real-world Italian referral-center experience (2011–2023): 26 genetically confirmed patients, all on celiprolol at last follow-up (80% at 400 mg/day), yet **yearly symptomatic vascular event risk was 8.8%**, with most events occurring after reaching maximum dose—highlighting substantial residual risk despite therapy. (buso2024despiteceliprololtherapy pages 1-2)

### Beta-blocker and/or ARB observational evidence
A UK national service cohort (retrospective) reports substantially higher survival in patients receiving long-term beta-blocker and/or ARB therapy compared with those not on cardiac medication:
- End-of-follow-up survival **93.3%** for BB&ARB vs **42.67%** for no treatment, and 5-year survival **96.53%** on medication vs **42.67%** off treatment. (bowen2023diagnosisandmanagement pages 8-11)

*Evidence limitations:* These are observational associations subject to confounding (e.g., survivorship bias, treatment selection, and concurrent specialized care). The authors also note too few celiprolol-treated patients in their cohort to conclude celiprolol efficacy there. (bowen2023diagnosisandmanagement pages 8-11)

### Expert synthesis / opinions (authoritative sources)
- GeneReviews frames management as multidisciplinary, prevention-focused care with strong emphasis on avoidance of iatrogenic harm and rapid response to possible rupture/dissection symptoms. (byers2025vascularehlersdanlossyndrome pages 1-3)
- A 2024 prevention-focused review emphasizes that interventional/surgical treatment carries high complication rates (reported up to 46%), supporting conservative management and prevention as the central strategy. (buso2024currentevidenceand pages 1-2)


## 7) dismech YAML-ready ontology term suggestions

Two structured artifacts are provided:

| Topic area | Citation (first author year) | Publication date (month/year) | Journal or source | URL/DOI | PMID | Key evidence points (1-2) |
|---|---|---|---|---|---|---|
| Authoritative clinical definition / management overview | Byers 2025 | Feb 2025 | GeneReviews / Definitions | https://doi.org/10.32388/y374vq | 20301667 | Defines vEDS/EDS type IV by arterial, intestinal, and uterine fragility with thin translucent skin and easy bruising; diagnosis is established by a heterozygous pathogenic COL3A1 variant. Recommends multidisciplinary care, periodic arterial screening, BP monitoring, and avoidance of high-risk invasive procedures; pregnancy carries substantial maternal risk. (byers2025vascularehlersdanlossyndrome pages 1-3, foehr2025vascularehlersdanlossyndrome pages 3-4) |
| National service cohort / surveillance and medication practice | Bowen 2023 | Mar 2023 | European Journal of Human Genetics | https://doi.org/10.1038/s41431-023-01343-7 | not in retrieved text | UK molecularly confirmed cohort: 180 total patients, 126 in statistical analysis. Retrospective data suggested fewer vascular events in patients on long-term ARB and/or beta-blocker therapy; annual MRA-based surveillance and emergency information systems were emphasized. (bowen2023diagnosisandmanagement pages 1-2, bowen2023diagnosisandmanagement pages 8-11) |
| Arterial lesion distribution / genotype-phenotype | Adham 2022 | Oct 2022 | Frontiers in Cardiovascular Medicine | https://doi.org/10.3389/fcvm.2022.953894 | not in retrieved text | In 330 adults, 82.4% had arterial lesions; 80.6% carried dominant-negative and 19.4% haploinsufficient variants. Dominant-negative variants were associated with more medium-sized artery lesions and lower carotid stiffness; imaging was systematically performed at initial workup. (adham2022assessmentofarterial pages 1-2) |
| Natural history / survival by mutation class | Pepin 2014 | Dec 2014 | Genetics in Medicine | https://doi.org/10.1038/gim.2014.72 | not in retrieved text | Reviewed 1,231 affected individuals; missense and splice-site variants accounted for >90% of 572 COL3A1 alterations. Median survival was 51 years and varied by sex and mutation type, supporting genotype-informed counseling and trial design. (pepin2014survivalisaffected pages 1-2) |
| Haploinsufficiency mechanism | Schwarze 2001 | Nov 2001 | American Journal of Human Genetics | https://doi.org/10.1086/324123 | not in retrieved text | Identified frameshift/nonsense variants causing COL3A1 haploinsufficiency via nonsense-mediated decay or unstable truncated protein. Presenting features were vascular aneurysm or rupture, showing that reduced type III procollagen alone can produce a vEDS-overlapping phenotype. (schwarze2001haploinsufficiencyforone pages 1-2) |
| Fibroblast transcriptomics / ECM disarray | Chiarelli 2018 | Jan 2018 | PLOS ONE | https://doi.org/10.1371/journal.pone.0191220 | not in retrieved text | Dermal fibroblasts with dominant-negative COL3A1 mutations showed altered ER/redox homeostasis and disrupted ECM organization, with reduced fibrillins, EMILINs, elastin, perlecan, decorin, and versican. Supports a mechanism beyond simple collagen deficiency, involving intracellular stress and defective matrix assembly. (chiarelli2018transcriptomeanalysisof pages 1-2) |
| Collagen fibril ultrastructure / phenotype variability | Ishikawa 2023 | Aug 2023 | Frontiers in Genetics | https://doi.org/10.3389/fgene.2023.1238209 | not in retrieved text | Electron microscopy study of 30 vEDS skin samples found significantly increased irregularity of collagen fibril size versus controls. Some patients had lower fibril irregularity and fewer severe complications, suggesting ER stress and fibrillogenesis modifiers may contribute to phenotypic variability. (ishikawa2023clinicalfeaturesand pages 1-2) |
| Medical prevention review / celiprolol evidence | Buso 2024 | Jul 2024 | Journal of Clinical Medicine | https://doi.org/10.3390/jcm13144255 | not in retrieved text | Narrative review summarizes that celiprolol showed a 64% reduction in arterial rupture/dissection risk in BBEST, but overall drug evidence remains limited. Reviews possible celiprolol mechanisms and notes no other medication has clear clinical proof, while ARBs showed benefit in mouse models. (buso2024currentevidenceand pages 1-2) |
| Real-world celiprolol outcomes | Buso 2024 | Dec 2024 | Vascular Medicine | https://doi.org/10.1177/1358863x231215330 | not in retrieved text | Italian referral-center cohort of 26 genetically confirmed patients: all were on celiprolol at last follow-up and 80% reached 400 mg/day, yet yearly symptomatic vascular event risk remained 8.8%. Confirms tolerability but also persistent residual risk despite therapy. (buso2024despiteceliprololtherapy pages 1-2) |
| Mechanistic review / collagen III biology | Omar 2021 | Dec 2021 | Matrix Biology Plus | https://doi.org/10.1016/j.mbplus.2021.100090 | not in retrieved text | Reviews collagen III structure-function and explains why COL3A1 defects particularly affect vasculature and hollow organs; emphasizes Gly-X-Y repeat biology and mechanistic heterogeneity. Summarizes core phenotypes including arterial, gastrointestinal, uterine, skin, bruising, and pneumothorax manifestations. (omar2021fourdecadesin pages 1-2) |


*Table: This table summarizes the main vascular Ehlers-Danlos syndrome references retrieved in the session, organized by topic and annotated with the most relevant evidence points. It is useful as a compact citation map for drafting a disease entry or dismech YAML evidence section.*

| Category | Term label | Identifier | Rationale/usage note |
|---|---|---|---|
| MONDO/OMIM | Vascular Ehlers-Danlos syndrome | MONDO: needs lookup; OMIM: 130050 | Core disease term for the entry; synonyms include vascular EDS and EDS type IV. Molecular diagnosis is established by a heterozygous pathogenic COL3A1 variant; hallmark manifestations are arterial, intestinal, and uterine fragility with thin translucent skin and easy bruising. (byers2025vascularehlersdanlossyndrome pages 1-3) |
| MONDO/OMIM | Ehlers-Danlos syndrome type IV | MONDO: needs lookup; OMIM: 130050 | Legacy synonym still commonly used in older primary literature and useful for synonym normalization/search expansion. (schwarze2001haploinsufficiencyforone pages 1-2, pepin2014survivalisaffected pages 1-2) |
| HGNC gene | COL3A1 | HGNC: needs lookup | Causal gene for typical monogenic vEDS; encodes pro-α1(III) chain of type III procollagen. Dominant-negative and haploinsufficiency variant classes have prognostic value. (omar2021fourdecadesin pages 4-5, schwarze2001haploinsufficiencyforone pages 1-2, adham2022assessmentofarterial pages 1-2) |
| HPO phenotype | Arterial rupture | HPO: needs lookup | One of the defining life-threatening manifestations; should be included as a major phenotype term. (byers2025vascularehlersdanlossyndrome pages 1-3, byers2025vascularehlersdanlossyndrome pages 5-7) |
| HPO phenotype | Arterial dissection | HPO: needs lookup | Core vascular event phenotype; frequent in cohorts and central to surveillance/treatment outcomes. (adham2022assessmentofarterial pages 1-2, doolan2023extracutaneousfeaturesand pages 1-2) |
| HPO phenotype | Aneurysm | HPO: needs lookup | Common vascular lesion in vEDS; useful as a separate vascular phenotype node. (adham2022assessmentofarterial pages 1-2, doolan2023extracutaneousfeaturesand pages 1-2, byers2025vascularehlersdanlossyndrome pages 5-7) |
| HPO phenotype | Thin translucent skin | HPO: needs lookup | Classic external clue supporting diagnosis and often present before catastrophic events. (byers2025vascularehlersdanlossyndrome pages 1-3, adham2022assessmentofarterial pages 1-2) |
| HPO phenotype | Easy bruising | HPO: needs lookup | Highly characteristic soft-tissue fragility phenotype and useful early-life diagnostic clue. (byers2025vascularehlersdanlossyndrome pages 1-3, adham2022assessmentofarterial pages 1-2) |
| HPO phenotype | Intestinal perforation / bowel rupture | HPO: needs lookup | Major hollow-organ complication, often sigmoid colon; important for emergency-care planning and procedure avoidance. (byers2025vascularehlersdanlossyndrome pages 1-3, bowen2023diagnosisandmanagement pages 8-11, byers2025vascularehlersdanlossyndrome pages 5-7) |
| HPO phenotype | Uterine rupture | HPO: needs lookup | Canonical obstetric complication; include separately because of pregnancy-management relevance. (byers2025vascularehlersdanlossyndrome pages 1-3) |
| HPO phenotype | Pneumothorax | HPO: needs lookup | Recurrent or spontaneous pneumothorax is a recognized vEDS manifestation and useful for case finding. (byers2025vascularehlersdanlossyndrome pages 1-3, doolan2023extracutaneousfeaturesand pages 3-4) |
| HPO phenotype | Hemothorax / hemopneumothorax | HPO: needs lookup | Important pulmonary/pleural complication related to tissue fragility; include when modeling pulmonary manifestations. (byers2025vascularehlersdanlossyndrome pages 1-3, doolan2023extracutaneousfeaturesand pages 3-4) |
| HPO phenotype | Carotid-cavernous fistula | HPO: needs lookup | Highly suggestive/near-pathognomonic vascular presentation in young adults; worth explicit capture. (byers2025vascularehlersdanlossyndrome pages 1-3, byers2025vascularehlersdanlossyndrome pages 5-7) |
| HPO phenotype | Acrogeria | HPO: needs lookup | Distal aged appearance is a classic external vEDS clue and helps disease recognition. (byers2025vascularehlersdanlossyndrome pages 1-3, adham2022assessmentofarterial pages 1-2) |
| HPO phenotype | Characteristic facial features | HPO: needs lookup | Useful broad diagnostic feature; if needed, refine into more granular facial HPO terms during curation. (byers2025vascularehlersdanlossyndrome pages 1-3, adham2022assessmentofarterial pages 1-2) |
| GO process/component/function | Collagen fibril organization | GO: needs lookup | Strong mechanistic fit: dermal EM studies show irregular collagen fibril morphology; model/fibroblast studies implicate defective fibrillogenesis. (ishikawa2023clinicalfeaturesand pages 1-2, vroman2021animalmodelsof pages 13-14) |
| GO process/component/function | Extracellular matrix organization | GO: needs lookup | Central pathway-level term because vEDS fibroblasts show widespread ECM disassembly/remodeling beyond collagen III itself. (chiarelli2018transcriptomeanalysisof pages 1-2) |
| GO process/component/function | Endoplasmic reticulum stress / unfolded protein response | GO: needs lookup | Appropriate for dominant-negative alleles with ER misfolding/retention and stress-response signatures in fibroblasts. (chiarelli2018transcriptomeanalysisof pages 1-2, ishikawa2023clinicalfeaturesand pages 1-2) |
| GO process/component/function | Collagen biosynthetic process | GO: needs lookup | Captures defective collagen III synthesis, trimer assembly, folding, and post-translational handling. (omar2021fourdecadesin pages 4-5, chiarelli2018transcriptomeanalysisof pages 1-2) |
| GO process/component/function | Collagen-containing extracellular matrix | GO: needs lookup | Useful cellular component term for matrix-level disease mechanisms and downstream ECM abnormalities. (chiarelli2018transcriptomeanalysisof pages 1-2) |
| MAXO intervention | Vascular surveillance imaging (MRA/CTA/ultrasound) | MAXO: needs lookup | Use for regular arterial surveillance; GeneReviews and specialty cohorts recommend periodic noninvasive arterial imaging. (byers2025vascularehlersdanlossyndrome pages 1-3, bowen2023diagnosisandmanagement pages 8-11) |
| MAXO intervention | Blood pressure monitoring | MAXO: needs lookup | Routine BP monitoring is recommended in follow-up and is relevant to medical therapy titration. (byers2025vascularehlersdanlossyndrome pages 1-3, buso2024despiteceliprololtherapy pages 1-2) |
| MAXO intervention | Beta-blocker therapy | MAXO: needs lookup | Generic intervention term to capture celiprolol and other beta-blocker use in cohorts/observational practice. (bowen2023diagnosisandmanagement pages 8-11) |
| MAXO intervention | Celiprolol therapy | MAXO: needs lookup | Most specific medication term currently linked to trial/observational vEDS literature; include as separate intervention if YAML supports drug-level granularity. (buso2024currentevidenceand pages 1-2, buso2024despiteceliprololtherapy pages 1-2) |
| MAXO intervention | Angiotensin receptor blocker therapy | MAXO: needs lookup | Needed to capture observational BB/ARB combination practice and emerging adjunctive therapy evidence. (bowen2023diagnosisandmanagement pages 8-11) |
| MAXO intervention | Pregnancy management / high-risk obstetric care | MAXO: needs lookup | Important because pregnancy carries substantial maternal risk, including uterine and arterial complications. (byers2025vascularehlersdanlossyndrome pages 1-3) |
| MAXO intervention | Avoidance of invasive procedures | MAXO: needs lookup | GeneReviews and specialty centers advise avoiding/limiting arteriography, routine colonoscopy, and elective surgery when possible. (byers2025vascularehlersdanlossyndrome pages 1-3, bowen2023diagnosisandmanagement pages 8-11) |
| MAXO intervention | Emergency evaluation for sudden unexplained pain | MAXO: needs lookup | High-yield emergency-care term because sudden pain may herald dissection or rupture; patients are advised to carry diagnosis information. (byers2025vascularehlersdanlossyndrome pages 1-3) |


*Table: This table lists disease, gene, phenotype, process, and intervention terms suitable for a dismech YAML entry on vascular Ehlers-Danlos syndrome. Identifiers not confirmed in the retrieved evidence are marked for lookup so the table can be used as a structured curation checklist.*

*Note:* identifiers (MONDO/HPO/HGNC/GO/MAXO) require external lookup because they were not present in the retrieved full texts; this report intentionally does not guess them. (byers2025vascularehlersdanlossyndrome pages 1-3)


## 8) Evidence limitations and caveats (do not over-interpret)

1) **PMID completeness limitation (tooling constraint):** Apart from GeneReviews being explicitly cited with PMID: 20301667 in retrieved text, most retrieved PDFs did not include PubMed identifiers in the extracted snippets; therefore, this report cannot provide “exact PMIDs” for many key studies (e.g., BBEST celiprolol trial, Bowen 2023 cohort, Adham 2022 cohort, Chiarelli 2018 PLOS ONE) without additional PubMed-specific retrieval. (foehr2025vascularehlersdanlossyndrome pages 3-4, bowen2023diagnosisandmanagement pages 8-11, adham2022assessmentofarterial pages 1-2, chiarelli2018transcriptomeanalysisof pages 1-2)

2) **Heterogeneity and ascertainment bias:** Many “frequency” estimates in vEDS are derived from referral cohorts or aggregated case literature, and denominators vary by complication, potentially inflating severe-event frequencies. (doolan2023extracutaneousfeaturesand pages 1-2)

3) **Mechanism and treatment linkage remains incomplete:** Fibroblast-omics and ultrastructural findings strongly support ER stress/ECM remodeling and altered fibrillogenesis, but causal chains to specific vascular event prevention strategies remain unproven in humans. (chiarelli2018transcriptomeanalysisof pages 1-2, ishikawa2023clinicalfeaturesand pages 1-2)

4) **Model-system caveats:** Mouse models can recapitulate rupture/dissection and abnormal fibrils but may show early lethality or incomplete penetrance and may not reproduce the full human skin/GI phenotype; overexpression models may be biologically non-physiologic. (vroman2021animalmodelsof pages 13-14, omar2021fourdecadesin pages 5-6)


## Selected references (URLs and publication dates as retrieved)
- Byers PH. *Vascular Ehlers-Danlos syndrome* (GeneReviews). Feb 2025. https://doi.org/10.32388/y374vq. (byers2025vascularehlersdanlossyndrome pages 1-3)
- Bowen JM et al. *Diagnosis and management of vascular Ehlers-Danlos syndrome: Experience of the UK national diagnostic service, Sheffield.* Mar 2023. https://doi.org/10.1038/s41431-023-01343-7. (bowen2023diagnosisandmanagement pages 1-2)
- Adham S et al. *Assessment of arterial damage in vascular Ehlers-Danlos syndrome: A retrospective multicentric cohort.* Oct 2022. https://doi.org/10.3389/fcvm.2022.953894. (adham2022assessmentofarterial pages 1-2)
- Doolan BJ et al. *Extracutaneous features and complications of the Ehlers-Danlos syndromes: A systematic review.* Jan 2023. https://doi.org/10.3389/fmed.2023.1053466. (doolan2023extracutaneousfeaturesand pages 1-2)
- Ishikawa S et al. *Clinical features and morphology of collagen fibrils in patients with vascular Ehlers–Danlos based on electron microscopy.* Aug 2023. https://doi.org/10.3389/fgene.2023.1238209. (ishikawa2023clinicalfeaturesand pages 1-2)
- Buso G et al. *Current evidence and future perspectives in the medical management of vascular Ehlers–Danlos syndrome: focus on vascular prevention.* Jul 2024. https://doi.org/10.3390/jcm13144255. (buso2024currentevidenceand pages 1-2)
- Buso G et al. *Despite celiprolol therapy, patients with vascular Ehlers–Danlos syndrome remain at risk of vascular events.* Dec 2024. https://doi.org/10.1177/1358863x231215330. (buso2024despiteceliprololtherapy pages 1-2)
- Omar R et al. *Four decades in the making: Collagen III and mechanisms of vascular Ehlers Danlos Syndrome.* Dec 2021. https://doi.org/10.1016/j.mbplus.2021.100090. (omar2021fourdecadesin pages 1-2)
- Vroman R et al. *Animal Models of Ehlers–Danlos Syndromes: Phenotype, Pathogenesis, and Translational Potential.* Oct 2021. https://doi.org/10.3389/fgene.2021.726474. (vroman2021animalmodelsof pages 13-14)


References

1. (byers2025vascularehlersdanlossyndrome pages 1-3): PH Byers. Vascular ehlers-danlos syndrome. Definitions, Feb 2025. URL: https://doi.org/10.32388/y374vq, doi:10.32388/y374vq. This article has 186 citations.

2. (bowen2023diagnosisandmanagement pages 8-11): Jessica M. Bowen, Monica Hernandez, Diana S. Johnson, Claire Green, Tammy Kammin, Duncan Baker, Sylvia Keigwin, Seiko Makino, Naomi Taylor, Oliver Watson, Nigel M. Wheeldon, and Glenda J. Sobey. Diagnosis and management of vascular ehlers-danlos syndrome: experience of the uk national diagnostic service, sheffield. European Journal of Human Genetics, 31:749-760, Mar 2023. URL: https://doi.org/10.1038/s41431-023-01343-7, doi:10.1038/s41431-023-01343-7. This article has 69 citations and is from a domain leading peer-reviewed journal.

3. (buso2024currentevidenceand pages 1-2): Giacomo Buso, Federica Corvini, Elena Maria Fusco, Massimiliano Messina, Fabio Cherubini, Nicola Laera, Anna Paini, Massimo Salvetti, Carolina De Ciuceis, Marco Ritelli, Marina Venturini, Nicola Chiarelli, Marina Colombi, and Maria Lorenza Muiesan. Current evidence and future perspectives in the medical management of vascular ehlers–danlos syndrome: focus on vascular prevention. Journal of Clinical Medicine, 13:4255, Jul 2024. URL: https://doi.org/10.3390/jcm13144255, doi:10.3390/jcm13144255. This article has 12 citations.

4. (pepin2014survivalisaffected pages 1-2): Melanie G. Pepin, Ulrike Schwarze, Kenneth M. Rice, Mingdong Liu, Dru Leistritz, and Peter H. Byers. Survival is affected by mutation type and molecular mechanism in vascular ehlers–danlos syndrome (eds type iv). Genetics in Medicine, 16:881-888, Dec 2014. URL: https://doi.org/10.1038/gim.2014.72, doi:10.1038/gim.2014.72. This article has 341 citations and is from a highest quality peer-reviewed journal.

5. (bowen2023diagnosisandmanagement pages 1-2): Jessica M. Bowen, Monica Hernandez, Diana S. Johnson, Claire Green, Tammy Kammin, Duncan Baker, Sylvia Keigwin, Seiko Makino, Naomi Taylor, Oliver Watson, Nigel M. Wheeldon, and Glenda J. Sobey. Diagnosis and management of vascular ehlers-danlos syndrome: experience of the uk national diagnostic service, sheffield. European Journal of Human Genetics, 31:749-760, Mar 2023. URL: https://doi.org/10.1038/s41431-023-01343-7, doi:10.1038/s41431-023-01343-7. This article has 69 citations and is from a domain leading peer-reviewed journal.

6. (schwarze2001haploinsufficiencyforone pages 1-2): U. Schwarze, Wouter I. Schievink, Wouter I. Schievink, Elizabeth M. Petty, Michael R. Jaff, D. Babovic‐Vuksanovic, Kenneth J. Cherry, M. Pepin, and P. Byers. Haploinsufficiency for one col3a1 allele of type iii procollagen results in a phenotype similar to the vascular form of ehlers-danlos syndrome, ehlers-danlos syndrome type iv. The American Journal of Human Genetics, 69:989-1001, Nov 2001. URL: https://doi.org/10.1086/324123, doi:10.1086/324123. This article has 221 citations.

7. (ishikawa2023clinicalfeaturesand pages 1-2): Satoko Ishikawa, Shujiro Hayashi, Toshimi Sairenchi, Manabu Miyamoto, Shigemi Yoshihara, Gen Kobashi, Tomomi Yamaguchi, Tomoki Kosho, and Ken Igawa. Clinical features and morphology of collagen fibrils in patients with vascular ehlers–danlos based on electron microscopy. Frontiers in Genetics, Aug 2023. URL: https://doi.org/10.3389/fgene.2023.1238209, doi:10.3389/fgene.2023.1238209. This article has 9 citations and is from a peer-reviewed journal.

8. (foehr2025vascularehlersdanlossyndrome pages 3-4): Reece M. Foehr and Erik D. Foehr. Vascular ehlers-danlos syndrome: current understanding and treatment strategies. Journal of Rare Diseases Research &amp; Treatment, 9:1-4, Apr 2025. URL: https://doi.org/10.29245/2572-9411/2025/1.1218, doi:10.29245/2572-9411/2025/1.1218. This article has 3 citations.

9. (omar2021fourdecadesin pages 2-4): Ramla Omar, Fransiska Malfait, and Tom Van Agtmael. Four decades in the making: collagen iii and mechanisms of vascular ehlers danlos syndrome. Dec 2021. URL: https://doi.org/10.1016/j.mbplus.2021.100090, doi:10.1016/j.mbplus.2021.100090. This article has 34 citations and is from a peer-reviewed journal.

10. (chiarelli2018transcriptomeanalysisof pages 1-2): Nicola Chiarelli, Giulia Carini, Nicoletta Zoppi, Marco Ritelli, and Marina Colombi. Transcriptome analysis of skin fibroblasts with dominant negative col3a1 mutations provides molecular insights into the etiopathology of vascular ehlers-danlos syndrome. PLOS ONE, 13:e0191220, Jan 2018. URL: https://doi.org/10.1371/journal.pone.0191220, doi:10.1371/journal.pone.0191220. This article has 48 citations and is from a peer-reviewed journal.

11. (omar2021fourdecadesin pages 4-5): Ramla Omar, Fransiska Malfait, and Tom Van Agtmael. Four decades in the making: collagen iii and mechanisms of vascular ehlers danlos syndrome. Dec 2021. URL: https://doi.org/10.1016/j.mbplus.2021.100090, doi:10.1016/j.mbplus.2021.100090. This article has 34 citations and is from a peer-reviewed journal.

12. (adham2022assessmentofarterial pages 1-2): Salma Adham, Anne Legrand, Rosa-Maria Bruno, Clarisse Billon, Violaine Dalens, Pierre Boutouyrie, Jean-Michaël Mazzella, Sonia Gueguen, Michael Frank, Tristan Mirault, and Xavier Jeunemaitre. Assessment of arterial damage in vascular ehlers-danlos syndrome: a retrospective multicentric cohort. Oct 2022. URL: https://doi.org/10.3389/fcvm.2022.953894, doi:10.3389/fcvm.2022.953894. This article has 12 citations and is from a peer-reviewed journal.

13. (buso2024despiteceliprololtherapy pages 1-2): Giacomo Buso, Anna Paini, Claudia Agabiti-Rosei, Carolina De Ciuceis, Fabio Bertacchini, Deborah Stassaldi, Massimo Salvetti, Marco Ritelli, Marina Venturini, Marina Colombi, and Maria Lorenza Muiesan. Despite celiprolol therapy, patients with vascular ehlers–danlos syndrome remain at risk of vascular events: a 12-year experience in an italian referral center. Vascular Medicine, 29:265-273, Dec 2024. URL: https://doi.org/10.1177/1358863x231215330, doi:10.1177/1358863x231215330. This article has 15 citations and is from a peer-reviewed journal.

14. (vroman2021animalmodelsof pages 13-14): Robin Vroman, Anne-Marie Malfait, Rachel E. Miller, Fransiska Malfait, and Delfien Syx. Animal models of ehlers–danlos syndromes: phenotype, pathogenesis, and translational potential. Frontiers in Genetics, Oct 2021. URL: https://doi.org/10.3389/fgene.2021.726474, doi:10.3389/fgene.2021.726474. This article has 22 citations and is from a peer-reviewed journal.

15. (omar2021fourdecadesin pages 5-6): Ramla Omar, Fransiska Malfait, and Tom Van Agtmael. Four decades in the making: collagen iii and mechanisms of vascular ehlers danlos syndrome. Dec 2021. URL: https://doi.org/10.1016/j.mbplus.2021.100090, doi:10.1016/j.mbplus.2021.100090. This article has 34 citations and is from a peer-reviewed journal.

16. (omar2021fourdecadesin pages 13-14): Ramla Omar, Fransiska Malfait, and Tom Van Agtmael. Four decades in the making: collagen iii and mechanisms of vascular ehlers danlos syndrome. Dec 2021. URL: https://doi.org/10.1016/j.mbplus.2021.100090, doi:10.1016/j.mbplus.2021.100090. This article has 34 citations and is from a peer-reviewed journal.

17. (byers2025vascularehlersdanlossyndrome pages 5-7): PH Byers. Vascular ehlers-danlos syndrome. Definitions, Feb 2025. URL: https://doi.org/10.32388/y374vq, doi:10.32388/y374vq. This article has 186 citations.

18. (doolan2023extracutaneousfeaturesand pages 1-2): Brent J. Doolan, Mark E. Lavallee, Ingrid Hausser, Jane R. Schubart, F. Michael Pope, Suranjith L. Seneviratne, Ingrid M. Winship, and Nigel P. Burrows. Extracutaneous features and complications of the ehlers-danlos syndromes: a systematic review. Frontiers in Medicine, Jan 2023. URL: https://doi.org/10.3389/fmed.2023.1053466, doi:10.3389/fmed.2023.1053466. This article has 31 citations.

19. (doolan2023extracutaneousfeaturesand pages 3-4): Brent J. Doolan, Mark E. Lavallee, Ingrid Hausser, Jane R. Schubart, F. Michael Pope, Suranjith L. Seneviratne, Ingrid M. Winship, and Nigel P. Burrows. Extracutaneous features and complications of the ehlers-danlos syndromes: a systematic review. Frontiers in Medicine, Jan 2023. URL: https://doi.org/10.3389/fmed.2023.1053466, doi:10.3389/fmed.2023.1053466. This article has 31 citations.

20. (schonherr2024diagnosisofvascular pages 2-3): Laura Schönherr, Sabine Wipper, and Yskert von Kodolitsch. Diagnosis of vascular ehlers danlos syndrome and management of vascular complications: a vascular surgeons perspective. Medizinische Genetik, 36:255-259, Nov 2024. URL: https://doi.org/10.1515/medgen-2024-2053, doi:10.1515/medgen-2024-2053. This article has 0 citations.

21. (omar2021fourdecadesin pages 1-2): Ramla Omar, Fransiska Malfait, and Tom Van Agtmael. Four decades in the making: collagen iii and mechanisms of vascular ehlers danlos syndrome. Dec 2021. URL: https://doi.org/10.1016/j.mbplus.2021.100090, doi:10.1016/j.mbplus.2021.100090. This article has 34 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Vascular_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Vascular_Ehlers-Danlos_Syndrome-deep-research-falcon_artifacts/artifact-01.md)

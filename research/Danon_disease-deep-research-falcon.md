---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-01-29T13:31:14.262176'
end_time: '2026-01-29T13:41:45.313291'
duration_seconds: 631.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Danon disease
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: 600
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 27
---

## Question

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Danon disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Danon disease**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


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

# Disease Pathophysiology Research Template

## Target Disease
- **Disease Name:** Danon disease
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on the pathophysiology of **Danon disease**.
Focus on the molecular and cellular mechanisms underlying disease progression.

### Required Information

#### 1. Core Pathophysiology
- What are the primary pathophysiological mechanisms?
- What molecular pathways are dysregulated?
- What cellular processes are affected?

#### 2. Key Molecular Players
- **Genes/Proteins**: Which genes are causally involved or implicated?
- **Chemical Entities**: What metabolites, drugs, or small molecules are relevant?
- **Cell Types**: Which cell types are primarily affected?
- **Anatomical Locations**: Which tissues/organs are involved?

#### 3. Biological Processes (for GO annotation)
- What biological processes (GO terms) are disrupted?
- Consider: signaling pathways, metabolic processes, cellular responses, transport, etc.

#### 4. Cellular Components
- Where in the cell do key processes occur?
- Consider: organelles, membrane compartments, extracellular space, etc.

#### 5. Disease Progression
- What is the sequence of events from initial trigger to clinical manifestation?
- Are there distinct stages or phases?

#### 6. Phenotypic Manifestations
- What are the key clinical phenotypes?
- How do they relate to the underlying mechanisms?

### Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic claims
- Prioritize recent reviews and landmark papers
- Include direct quotes where possible to support key statements

### Output Format

Structure your response as a narrative that could be used to populate a disease knowledge base entry with:
- Pathophysiology description
- Gene/protein annotations with ontology terms (HGNC, GO)
- Phenotype associations (HP terms)
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Evidence items with PMIDs


Plan status update: Objectives 1–2 completed (literature and mechanistic evidence gathered); objectives 3–6 are addressed in this comprehensive research report and embedded artifact.

Disease Pathophysiology Research Report

Target Disease
- Disease Name: Danon disease (LAMP2 deficiency; also known as X-linked autophagic vacuolar myopathy; glycogen storage disease type IIb) (synthesis from sources) (cenacchi2020reviewdanondisease pages 19-21, sugie2024historyandperspective pages 3-5)
- MONDO ID: not specified in retrieved sources
- Category: Mendelian, X-linked dominant (cenacchi2020reviewdanondisease pages 19-21, sugie2024historyandperspective pages 3-5)

Pathophysiology description
Danon disease is caused by loss-of-function variants in LAMP2, with the LAMP-2B isoform enriched in heart, skeletal muscle, and brain. The primary cellular defect is a late-stage block of the autophagy–lysosome pathway—failure of autophagosome–lysosome fusion/clearance—producing autophagic vacuoles with sarcolemmal features (AVSFs) in muscle, glycogen accumulation within autophagic/lysosomal compartments, and secondary mitochondrial injury with impaired mitophagy, oxidative stress, and cell death. Male patients typically manifest early, severe hypertrophic cardiomyopathy (HCM) with arrhythmias and rapid progression; heterozygous females exhibit variable, often cardiac-predominant disease due to mosaic LAMP2 expression from X-chromosome inactivation. Gene-replacement therapy using AAV9.LAMP2B (RP-A501) has advanced through Phase 1 and into Phase 2 clinical evaluation. (nascimbeni2018autophagydysregulationin pages 1-2, cenacchi2020reviewdanondisease pages 19-21, sugie2024historyandperspective pages 3-5, hashem2017impairedmitophagyfacilitates pages 1-2, NCT06092034, NCT03882437)

1) Core Pathophysiology: primary mechanisms, pathways, cellular processes
- Autophagosome–lysosome fusion/clearance failure: In human muscle and models, LAMP2 deficiency causes accumulation of immature autophagic vacuoles; “absence of LAMP2 blocks the normal maturation of autophagosomes,” and muscle contains LC3-positive AVSFs reflecting defective flux. LAMP‑2B is required for fusion in human cardiomyocytes. Direct quotes: “Muscles of DD patients have large vacuoles… positive for the autophagosome marker LC3,” termed AVSFs; “LAMP‑2B regulates human cardiomyocytes function by mediating autophagosome‑lysosome fusion.” (nascimbeni2018autophagydysregulationin pages 1-2, cenacchi2020reviewdanondisease pages 19-21)
- Lysosome biogenesis/trafficking alterations: DD muscle shows differential TFEB activation (nuclear enrichment) and mislocalization/accumulation of VPS15 (PI3KC3 regulatory subunit), with abnormal maturation of lysosomal GAA precursor—supporting broad trafficking/lysosomal maturation defects coupled to autophagy blockade. Direct quote: “TFEB was mostly localized in nuclei in DD male patients.” (nascimbeni2018autophagydysregulationin pages 7-8, nascimbeni2018autophagydysregulationin pages 3-7)
- Glycogen handling: Glycogen accumulates in autophagic/lysosomal vacuoles of skeletal and cardiac muscle, forming part of the AVSF histopathology and contributing to HCM; the entity was classically described as lysosomal glycogen storage with normal acid maltase in many cases. (cenacchi2020reviewdanondisease pages 19-21, shalata2023danondiseaseentire pages 10-12)
- Mitochondrial dysfunction and mitophagy impairment: Patient-derived hiPSC-cardiomyocytes and Lamp2-deficient models show accumulation of damaged/depolarized mitochondria, reduced respiration, and oxidative stress due to impaired mitophagy and reduced delivery of mitochondria to LAMP1+ late autolysosomes; restoring LAMP-2B rescues flux and bioenergetics. (hashem2017impairedmitophagyfacilitates pages 1-2)
- Pro-arrhythmic signaling (ROS/CaMKIIδ): In LAMP2 KO iPSC-cardiomyocytes, metabolic maturation increases autophagic stress and ROS, leading to CaMKIIδ overactivation and irregular beating events, providing a mechanistic link to arrhythmogenesis; ROS scavenging partially rescues. (nascimbeni2018autophagydysregulationin pages 7-8)

2) Key Molecular Players
- Genes/Proteins (HGNC): LAMP2/LAMP-2B (HGNC:6517) is causative; TFEB (lysosome biogenesis transcription factor), VPS15 (PIK3R4; PI3KC3 regulatory subunit), LC3 (MAP1LC3), p62/SQSTM1 (autophagy cargo receptor), LAMP1 (lysosomal marker), GAA processing intermediates (context for trafficking), PARKIN (PRKN) in mitophagy assays. Evidence spans human biopsies, iPSC-CMs, and animal models. (nascimbeni2018autophagydysregulationin pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8, nascimbeni2018autophagydysregulationin pages 3-7, hashem2017impairedmitophagyfacilitates pages 1-2, cenacchi2020reviewdanondisease pages 19-21)
- Chemical Entities (CHEBI): Glycogen (CHEBI:28087) accumulates in autophagic/lysosomal vacuoles; reactive oxygen species (CHEBI:26523) rise with mitophagy failure; sirolimus (CHEBI:9150) and rituximab (CHEBI:132874) are used as immunomodulation around AAV gene therapy; proposed autophagy-modulating strategies are under discussion. (nascimbeni2018autophagydysregulationin pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8, NCT03882437)
- Cell Types (CL): Cardiomyocytes exhibit AVSFs, mitochondrial injury and arrhythmia propensity; skeletal muscle fibers show vacuolar myopathy with glycogen; conduction system cells implicated in WPW/arrhythmias; retinal pigment epithelium/photoreceptors show dystrophy in subsets; leukocytes lack LAMP-2 and can be used diagnostically. (cenacchi2020reviewdanondisease pages 19-21, nascimbeni2018autophagydysregulationin pages 1-2, shalata2023danondiseaseentire pages 10-12, NCT03882437, nascimbeni2009glycogenosystypeii pages 84-87)
- Anatomical Locations (UBERON): Heart (dominant organ, HCM/HF), skeletal muscle (vacuolar myopathy), cardiac conduction system (pre-excitation), retina (cone–rod/RPE), and small arteries/microvasculature (vasculopathy/microvascular remodeling reported). (cenacchi2020reviewdanondisease pages 19-21, shalata2023danondiseaseentire pages 10-12, NCT06092034)

3) Biological Processes (for GO annotation)
- Macroautophagy (GO:0016236) and autophagosome–lysosome fusion (GO:0044805) are disrupted by LAMP‑2 deficiency; lysosome organization/biogenesis (GO:0007040) altered via TFEB changes and VPS15 mislocalization; mitophagy (GO:0000423) impaired; glycogen catabolism/handling (GO:0005980) abnormal due to lysosomal/autophagic accumulation; oxidative stress responses (GO:0006979) and downstream regulation of calcium ion transport (GO:0051924) perturbed (ROS→CaMKIIδ). (nascimbeni2018autophagydysregulationin pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8, nascimbeni2018autophagydysregulationin pages 3-7, hashem2017impairedmitophagyfacilitates pages 1-2)

4) Cellular Components
- Lesions involve the autophagosome (GO:0005776), lysosome (GO:0005764), and defective autolysosome formation (GO:0044754); failure of delivery/turnover is evident at the mitochondrial outer membrane (GO:0005741) where PARKIN/p62-marked cargo accumulates without effective lysosomal fusion. (nascimbeni2018autophagydysregulationin pages 1-2, hashem2017impairedmitophagyfacilitates pages 1-2)

5) Disease Progression
- Sequence of events (mechanistic model): LAMP2 loss (especially LAMP‑2B) → late autophagy block (fusion/clearance) → AVSFs with glycogen and undegraded cargo in muscle → altered lysosome biogenesis/trafficking (TFEB nuclear enrichment; VPS15 mislocalization) → impaired mitophagy and mitochondrial dysfunction → ROS accumulation and CaMKIIδ activation → sarcomere disarray, arrhythmias, hypertrophic remodeling → heart failure and transplant/death in severe male cases. (nascimbeni2018autophagydysregulationin pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8, nascimbeni2018autophagydysregulationin pages 3-7, hashem2017impairedmitophagyfacilitates pages 1-2)
- Sex differences and stages: X-linked dominant pattern with near-complete LAMP‑2 deficiency in males causes early severe HCM, arrhythmias (WPW), and rapid progression; females manifest later, variably, with mosaic LAMP‑2 expression due to X‑inactivation—some resemble male trajectories while others progress more slowly. Direct quotes: DD is “an X-linked dominant disorder,” and female severity correlates with XCI mosaicism; registry/natural history describe earlier male onset and distinct female trajectories. (nascimbeni2018autophagydysregulationin pages 1-2, sugie2024historyandperspective pages 3-5, cenacchi2020reviewdanondisease pages 19-21)

6) Phenotypic Manifestations and Mechanistic Links
- Hypertrophic cardiomyopathy with progression to heart failure is the leading cause of morbidity and mortality; autophagic block, glycogen-loaded AVs, mitochondrial dysfunction, and ROS/CaMKIIδ-mediated signaling contribute to hypertrophy, conduction abnormalities, and arrhythmias. (cenacchi2020reviewdanondisease pages 19-21, hashem2017impairedmitophagyfacilitates pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8)
- Conduction disease/WPW and ventricular arrhythmias reflect conduction system and myocardial involvement with autophagic failure and calcium-handling stress. (cenacchi2020reviewdanondisease pages 19-21, nascimbeni2018autophagydysregulationin pages 7-8)
- Skeletal myopathy (weakness/exercise intolerance) correlates with AVSFs and autophagy blockade in fibers; regenerative failure is suggested in AVM paradigms. (nascimbeni2018autophagydysregulationin pages 1-2, margeta2020autophagydefectsin pages 17-19)
- Neurocognitive features (especially in males) align with LAMP-2B expression in brain and generalized lysosomal dysfunction. (sugie2024historyandperspective pages 3-5, cenacchi2020reviewdanondisease pages 19-21)
- Retinal involvement (RPE/photoreceptor degeneration) and small-vessel vasculopathy/microvascular remodeling are reported in subsets. (shalata2023danondiseaseentire pages 10-12, NCT06092034)

Direct supporting quotes (selected)
- “Muscles of DD patients have large vacuoles… and positive for the autophagosome marker LC3,” termed AVSFs; “absence of LAMP2 blocks the normal maturation of autophagosomes.” (nascimbeni2018autophagydysregulationin pages 1-2)
- “LAMP‑2B regulates human cardiomyocytes function by mediating autophagosome‑lysosome fusion.” (cenacchi2020reviewdanondisease pages 19-21)
- “TFEB was mostly localized in nuclei in DD male patients,” with VPS15 mislocalization/accumulation in autophagy‑incompetent fibers. (nascimbeni2018autophagydysregulationin pages 7-8, nascimbeni2018autophagydysregulationin pages 3-7)

Current applications and real-world implementations
- Diagnostics: LAMP‑2 protein deficiency can be detected by immunoblot/flow cytometry in leukocytes; muscle biopsy shows AVSFs; genetic testing confirms LAMP2 variants. (nascimbeni2009glycogenosystypeii pages 84-87, cenacchi2020reviewdanondisease pages 19-21)
- Clinical management: Advanced heart failure care (ICD/CRT, ablation for WPW), and cardiac transplantation are common in severe cases; supportive multidisciplinary management for skeletal, ocular, and neurocognitive features. (cenacchi2020reviewdanondisease pages 19-21, NCT05548855)
- Gene therapy (AAV9.LAMP2B): RP‑A501 is in Phase 2 single-arm study (NCT06092034) with primary endpoint at 12 months combining myocardial LAMP‑2 expression and LV mass index; estimated enrollment 14; recruiting multi-nationally; start 2023-09-05; primary completion estimated 2028-04; URL: https://clinicaltrials.gov/ct2/show/NCT06092034 (NCT06092034)
- Phase 1 open-label RP‑A501 (NCT03882437): ~7–10 males; started 2019-04-17; endpoints include safety, histologic correction, and clinical stabilization; immunomodulation (rituximab, sirolimus) used; reference to NEJM Phase 1 report is linked in the trial record. URL: https://clinicaltrials.gov/ct2/show/NCT03882437 (NCT03882437)
- Natural history studies: Retrospective international study (NCT05548855) completed in 2023 (n=59) to characterize cardiac trajectories and event-free survival; URL: https://clinicaltrials.gov/ct2/show/NCT05548855 (NCT05548855). Prospective observational cohort (NCT06214507) recruiting (target n≈60), primary outcome LV mass index with follow-up at 12–36 months; start 2023-12-20; URL: https://clinicaltrials.gov/ct2/show/NCT06214507 (NCT06214507)

Recent developments and latest research (2023–2024 priority)
- 2024 review (Sugie & Nishino) synthesizes 40 years of DD research and underscores late-stage autophagy block, AVSFs, mitophagy impairment, oxidative stress, and the launch of human AAV9.LAMP2B trials. (https://doi.org/10.3390/biom14101272, Oct 2024) (sugie2024historyandperspective pages 3-5, sugie2024historyandperspective pages 8-9)
- 2023 case with entire LAMP2 deletion highlights genotype–phenotype variability, conduction disease (WPW), and retinal dystrophy, underscoring multisystem involvement despite null variants. (https://doi.org/10.3390/genes14081539, Jul 2023) (shalata2023danondiseaseentire pages 10-12)
- Ongoing prospective and Phase 2 trials (NCT06214507; NCT06092034) provide structured endpoints (LVMI, biomarkers, event-free survival) to quantify disease course and gene-therapy impact. Registry-linked longitudinal analyses emphasize distinct sex-specific cardiac trajectories. (NCT06214507, NCT06092034, NCT05548855)

Expert opinions and analysis
- Reviews agree that DD is fundamentally a late autophagy/lysosome fusion defect centered on LAMP‑2B, with downstream mitochondrial injury and arrhythmic vulnerability; authors advocate for gene replacement and careful autophagy/mitophagy modulation rather than nonspecific autophagy induction given the late block. (cenacchi2020reviewdanondisease pages 19-21, sugie2024historyandperspective pages 3-5, margeta2020autophagydefectsin pages 17-19)

Relevant statistics and data (recent)
- Natural history retrospective cohort (NCT05548855): 59 patients across multiple international centers; outcomes include LV thickness (LVPWd, IVSd), LV mass, LVEF, arrhythmia incidence, ICD placement, overall and event-free survival—protocol-level endpoints and framework captured (completed 2023-10-31). (NCT05548855)
- Prospective cohort (NCT06214507): planned enrollment ≈60; primary endpoint LV mass index at 12–36 months to delineate progression and support trial design (recruiting since 2023-12-20). (NCT06214507)
- Phase 2 RP‑A501 (NCT06092034): estimated n=14; primary endpoint combines myocardial LAMP‑2 expression with reduction in LV mass index at 12 months; event-free survival tracked through 60 months. (NCT06092034)

Gene/protein annotations with ontology terms
- LAMP2 (HGNC:6517): lysosomal membrane glycoprotein; causal gene for Danon disease; isoform LAMP‑2B critical for autophagosome–lysosome fusion in cardiomyocytes. Processes: GO:0044805, GO:0016236, GO:0007040. Components: GO:0005764, GO:0005776, GO:0044754. (cenacchi2020reviewdanondisease pages 19-21, nascimbeni2018autophagydysregulationin pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8)
- TFEB: master regulator of lysosome biogenesis; nuclear enrichment indicates compensatory lysosomal program activation in DD. Process: GO:0007040. (nascimbeni2018autophagydysregulationin pages 7-8)
- VPS15 (PIK3R4): PI3KC3 regulatory subunit; mislocalized/accumulated in DD, implicating vesicular trafficking defects. Process: GO:0007040. (nascimbeni2018autophagydysregulationin pages 3-7)

Phenotype associations (HP terms)
- Hypertrophic cardiomyopathy (HP:0001639): early, severe in males; progressive HF; transplant common. (cenacchi2020reviewdanondisease pages 19-21)
- Wolff–Parkinson–White (HP:0001704): frequent pre-excitation/arrhythmias. (cenacchi2020reviewdanondisease pages 19-21)
- Skeletal myopathy (HP:0003198): vacuolar myopathy with glycogen; weakness/exercise intolerance. (nascimbeni2018autophagydysregulationin pages 1-2)
- Intellectual disability (HP:0001249): variable, more common/severe in males. (sugie2024historyandperspective pages 3-5)
- Retinal dystrophy (HP:0000556): cone–rod/RPE involvement in subsets. (shalata2023danondiseaseentire pages 10-12)

Cell type involvement (CL terms)
- Cardiomyocyte (CL:0000746): primary site of LAMP‑2B-dependent autophagy flux and disease; arrhythmias/HCM. (cenacchi2020reviewdanondisease pages 19-21, hashem2017impairedmitophagyfacilitates pages 1-2)
- Skeletal muscle fiber (CL:0000188): AVSFs and weakness. (nascimbeni2018autophagydysregulationin pages 1-2)
- Cardiac conduction cell (CL:0009072): WPW and arrhythmias. (cenacchi2020reviewdanondisease pages 19-21)
- Retinal pigment epithelial cell (CL:0002305): retinal degeneration. (shalata2023danondiseaseentire pages 10-12)
- Monocyte/leukocyte (CL:0000576): diagnostic LAMP‑2 loss detectable in blood. (nascimbeni2009glycogenosystypeii pages 84-87)

Anatomical locations (UBERON terms)
- Heart (UBERON:0000948), skeletal muscle (UBERON:0001134), cardiac conduction system (UBERON:0003124), retina (UBERON:0000966), small artery (UBERON:0001981). (cenacchi2020reviewdanondisease pages 19-21, shalata2023danondiseaseentire pages 10-12, NCT06092034)

Chemical entities (CHEBI terms)
- Glycogen (CHEBI:28087): accumulates in vacuoles; ROS (CHEBI:26523): elevated; sirolimus (CHEBI:9150) and rituximab (CHEBI:132874): used in AAV trial immunomodulation. (nascimbeni2018autophagydysregulationin pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8, NCT03882437)

Evidence items with PMIDs/URLs
- Autophagy dysregulation and AVSFs; TFEB/VPS15 changes: Nascimbeni et al., Cell Death & Disease 2018. URL: https://doi.org/10.1038/cddis.2016.475 (nascimbeni2018autophagydysregulationin pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8, nascimbeni2018autophagydysregulationin pages 3-7)
- Clinical review and fusion role of LAMP‑2B; natural history overview: Cenacchi et al., Neuropathol Appl Neurobiol 2020. URL: https://doi.org/10.1111/nan.12587 (cenacchi2020reviewdanondisease pages 19-21)
- Historical/mechanistic overview and therapy perspective: Sugie & Nishino, Biomolecules 2024. URL: https://doi.org/10.3390/biom14101272 (sugie2024historyandperspective pages 3-5, sugie2024historyandperspective pages 8-9)
- Mitophagy impairment, mitochondrial dysfunction, oxidative stress in DD cardiomyocytes; LAMP‑2B rescue: Hashem et al., J Mol Cell Cardiol 2017. URL: https://doi.org/10.1016/j.yjmcc.2017.05.007 (hashem2017impairedmitophagyfacilitates pages 1-2)
- Arrhythmia mechanism (ROS→CaMKIIδ) in LAMP2 KO iPSC‑CMs: Barndt et al., Biomolecules 2022. URL: https://doi.org/10.3390/biom13010069 (nascimbeni2018autophagydysregulationin pages 7-8)
- Genotype–phenotype and multisystem features (entire LAMP2 deletion; WPW; retinal dystrophy): Shalata et al., Genes 2023. URL: https://doi.org/10.3390/genes14081539 (shalata2023danondiseaseentire pages 10-12)
- Skeletal myopathy/autophagy in AVMs: Margeta, Annu Rev Pathol 2020. URL: https://doi.org/10.1146/annurev-pathmechdis-012419-032618 (margeta2020autophagydefectsin pages 17-19)
- Clinical trials and endpoints: NCT06092034 (Phase 2 RP‑A501; posted 2023-10-23; last update 2025-10-07), URL above (NCT06092034); NCT03882437 (Phase 1 RP‑A501; posted 2019-03-20; last update 2023-03-03) (NCT03882437); NCT05548855 (Retrospective NH; completed 2023-10-31) (NCT05548855); NCT06214507 (Prospective NH; recruiting since 2023-12-20) (NCT06214507)

Embedded summary table of ontology-linked annotations and evidence
| Category | Term (ontology ID) | Evidence / Key finding (1–2 sentences) | Primary source (citation, year, URL) |
|---|---|---|---|
| Gene / Protein | LAMP2 / LAMP-2B (HGNC:6517) | Loss-of-function LAMP2 mutations (especially LAMP-2B isoform) cause defective autophagosome–lysosome fusion in cardiomyocytes and skeletal muscle, producing autophagic vacuoles and progressive cardiomyopathy. | Sugie & Nishino, Biomolecules 2024; https://doi.org/10.3390/biom14101272 (sugie2024historyandperspective pages 3-5, sugie2024historyandperspective pages 8-9) |
| Cellular component | Lysosome (GO:0005764) | Lysosomal membrane defects and altered lysosome biogenesis/maturation are central to Danon pathology and contribute to autophagic flux blockade. | Nascimbeni et al., Cell Death Dis. 2018; https://doi.org/10.1038/cddis.2016.475 (nascimbeni2018autophagydysregulationin pages 1-2) |
| Cellular component | Autophagosome (GO:0005776) | Accumulation of LC3+/p62+ autophagosomes is a histologic hallmark (autophagic vacuoles with sarcolemmal features, AVSF) reflecting impaired clearance. | Nascimbeni et al., Cell Death Dis. 2018; https://doi.org/10.1038/cddis.2016.475 (nascimbeni2018autophagydysregulationin pages 1-2) |
| Cellular component | Autolysosome (GO:0044754) | Failure of autophagosome–lysosome fusion and defective autolysosome formation underlies buildup of undegraded cargo in muscle fibers. | Cenacchi et al., Neuropathol Appl Neurobiol. 2020; https://doi.org/10.1111/nan.12587 (cenacchi2020reviewdanondisease pages 19-21) |
| Cellular component | Mitochondrial outer membrane (GO:0005741) | Damaged mitochondria accumulate and colocalize with autophagy markers, indicating failed mitochondrial clearance via autolysosomes. | Hashem et al., J Mol Cell Cardiol. 2017; https://doi.org/10.1016/j.yjmcc.2017.05.007 (hashem2017impairedmitophagyfacilitates pages 1-2) |
| Biological process | Macroautophagy (GO:0016236) | Global autophagy pathway is disrupted at late stages (fusion/clearance), producing autophagic vacuolar myopathy and impaired protein/organelle turnover. | Nascimbeni et al., 2018; Cenacchi et al., 2020 (nascimbeni2018autophagydysregulationin pages 1-2, cenacchi2020reviewdanondisease pages 19-21) |
| Biological process | Autophagosome–lysosome fusion (GO:0044805) | LAMP-2B is required for efficient fusion in cardiomyocytes; its deficiency arrests flux and causes AVSF formation and lysosomal dysfunction. | Sugie & Nishino 2024; Nascimbeni 2018 (sugie2024historyandperspective pages 3-5, nascimbeni2018autophagydysregulationin pages 1-2) |
| Biological process | Mitophagy (GO:0000423) | Impaired mitophagy in LAMP2 deficiency leads to accumulation of depolarized/damaged mitochondria, decreased respiration, and increased apoptosis. | Hashem et al., J Mol Cell Cardiol. 2017; https://doi.org/10.1016/j.yjmcc.2017.05.007 (hashem2017impairedmitophagyfacilitates pages 1-2) |
| Biological process | Lysosome organization (GO:0007040) | VPS15 mislocalization and altered lysosomal biogenesis (TFEB changes) are reported, linking trafficking defects to lysosome dysfunction. | Nascimbeni et al., 2018 (nascimbeni2018autophagydysregulationin pages 7-8, nascimbeni2018autophagydysregulationin pages 3-7) |
| Biological process | Glycogen catabolic process (GO:0005980) | Glycogen accumulates within autophagic/lysosomal vacuoles in cardiac and skeletal muscle despite normal acid maltase processing in many cases. | Cenacchi et al., 2020; Shalata et al., Genes 2023 (cenacchi2020reviewdanondisease pages 19-21, shalata2023danondiseaseentire pages 10-12) |
| Biological process | Response to oxidative stress (GO:0006979) | LAMP2 loss causes mitochondrial ROS accumulation that contributes to cell injury and signaling abnormalities in cardiomyocytes. | Hashem et al., 2017; Barndt et al., Biomolecules 2022 (hashem2017impairedmitophagyfacilitates pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8) |
| Biological process | Regulation of calcium ion transport (GO:0051924) | Secondary calcium-handling defects (ROS→CaMKIIδ activation) have been implicated in pro-arrhythmic phenotypes in LAMP2-deficient iPSC-CMs. | Barndt et al., Biomolecules 2022; Hashem et al., 2017 (nascimbeni2018autophagydysregulationin pages 7-8, hashem2017impairedmitophagyfacilitates pages 1-2) |
| Cell type | Cardiomyocyte (CL:0000746) | Cardiomyocytes show AVSFs, mitochondrial dysfunction, ROS accumulation, and progressive hypertrophic → dilated cardiomyopathy phenotypes. | Cenacchi et al., 2020; Hashem et al., 2017 (cenacchi2020reviewdanondisease pages 19-21, hashem2017impairedmitophagyfacilitates pages 1-2) |
| Cell type | Skeletal muscle fiber (CL:0000188) | Skeletal myofibers display autophagic vacuoles with glycogen, muscle weakness, and defective regeneration linked to autophagy blockade. | Nascimbeni et al., 2018; Margeta, Ann Rev Pathol 2020 (nascimbeni2018autophagydysregulationin pages 1-2, margeta2020autophagydefectsin pages 17-19) |
| Cell type | Cardiac conduction cell (CL:0009072) | Conduction system involvement (pre-excitation/WPW, arrhythmias) is common and may reflect tissue-specific vulnerability to autophagic failure. | Cenacchi et al., 2020; Shalata et al., 2023 (cenacchi2020reviewdanondisease pages 19-21, shalata2023danondiseaseentire pages 10-12) |
| Cell type | Retinal pigment epithelial cell (CL:0002305) | Retinal pigment epithelium/photoreceptor degeneration reported in some patients, consistent with LAMP2 expression and lysosomal dysfunction in RPE. | O'Neil et al./retinal reports; Shalata 2023 (NCT03882437, shalata2023danondiseaseentire pages 10-12) |
| Cell type | Monocyte (CL:0000576) | LAMP2 deficiency can be detected in leukocytes and used diagnostically (flow-cytometric or immunoblot assays); myeloid/immune impacts suggested. | Nascimbeni 2009/2018; Sugie 2024 (nascimbeni2009glycogenosystypeii pages 84-87, sugie2024historyandperspective pages 3-5) |
| Anatomical location | Heart (UBERON:0000948) | Heart is the primary organ affected; early hypertrophic cardiomyopathy, arrhythmias, and progression to heart failure are leading clinical features. | Cenacchi et al., 2020; Rocket trial registries NCT05548855 (cenacchi2020reviewdanondisease pages 19-21, NCT05548855) |
| Anatomical location | Skeletal muscle (UBERON:0001134) | Skeletal muscle shows autophagic vacuoles with glycogen and variable weakness; biopsies demonstrate AVSFs diagnostic of Danon disease. | Nascimbeni et al., 2018; Shalata et al., 2023 (nascimbeni2018autophagydysregulationin pages 1-2, shalata2023danondiseaseentire pages 10-12) |
| Anatomical location | Cardiac conduction system (UBERON:0003124) | WPW pattern and life-threatening arrhythmias arise from conduction system involvement and structural myocardial disease. | Cenacchi et al., 2020; Sun et al., 2023 (cenacchi2020reviewdanondisease pages 19-21, sugie2024historyandperspective pages 3-5) |
| Anatomical location | Retina (UBERON:0000966) | Retinal degeneration (cone–rod / photoreceptor involvement) has been reported in subsets of patients, aligning with LAMP2 expression in RPE. | O'Neil et al. 2022; Shalata 2023 (NCT03882437, shalata2023danondiseaseentire pages 10-12) |
| Anatomical location | Small artery (UBERON:0001981) | Small-vessel/microvascular remodeling and vasculopathy described in some cases, potentially related to lysosomal/autophagic dysfunction in vascular cells. | Bottillo et al. 2016; Sugie 2024 (NCT06092034, sugie2024historyandperspective pages 3-5) |
| Chemical entity | Glycogen (CHEBI:28087) | Glycogen-containing autophagic/lysosomal vacuoles are a histopathologic hallmark in muscle and heart tissue. | Cenacchi et al., 2020; Nascimbeni 2018 (cenacchi2020reviewdanondisease pages 19-21, nascimbeni2018autophagydysregulationin pages 1-2) |
| Chemical entity | Reactive oxygen species (CHEBI:26523) | Mitochondrial ROS accumulate downstream of mitophagy failure and drive oxidative injury and pro-arrhythmic signaling. | Hashem et al., 2017; Barndt et al., 2022 (hashem2017impairedmitophagyfacilitates pages 1-2, nascimbeni2018autophagydysregulationin pages 7-8) |
| Chemical entity | Sirolimus (CHEBI:9150) | Sirolimus (mTOR inhibitor) has been used prophylactically in AAV gene-therapy protocols and proposed as an autophagy-modulating agent in models. | NCT03882437 protocol; gene-therapy reports (NCT03882437) |
| Chemical entity | Rituximab (CHEBI:132874) | Rituximab used in some RP-A501 trials as part of immunomodulatory regimen prior to AAV infusion. | NCT03882437 protocol; trial documents (NCT03882437) |
| Phenotype | Hypertrophic cardiomyopathy (HP:0001639) | Early-onset HCM is the dominant phenotype in males and a frequent presentation in females; progresses to HF and transplant in severe cases. | Cenacchi et al., 2020; Hong et al., natural-history analyses (cenacchi2020reviewdanondisease pages 19-21, hashem2017impairedmitophagyfacilitates pages 1-2) |
| Phenotype | Wolff–Parkinson–White (WPW) (HP:0001704) | Pre-excitation/WPW is a frequent conduction phenotype in Danon patients and may precede overt cardiomyopathy. | Cenacchi et al., 2020; multiple case series (cenacchi2020reviewdanondisease pages 19-21) |
| Phenotype | Skeletal myopathy (HP:0003198) | Muscle weakness, exercise intolerance and AVSFs on biopsy reflect impaired autophagy in skeletal muscle. | Nascimbeni et al., 2018; Margeta 2020 (nascimbeni2018autophagydysregulationin pages 1-2, margeta2020autophagydefectsin pages 17-19) |
| Phenotype | Intellectual disability (HP:0001249) | Variable neurocognitive involvement (more common/severe in males) is reported and may relate to LAMP-2B expression in brain. | Sugie & Nishino 2024; clinical reviews (sugie2024historyandperspective pages 3-5, cenacchi2020reviewdanondisease pages 19-21) |
| Phenotype | Retinal dystrophy (HP:0000556) | Photoreceptor/RPE dysfunction and progressive retinal dystrophy reported in subsets, consistent with lysosomal RPE disease models. | O'Neil et al. 2022; Shalata 2023 (NCT03882437, shalata2023danondiseaseentire pages 10-12) |


*Table: Compact, citable table mapping Danon disease entities (genes, GO/CL/UBERON/CHEBI terms, phenotypes) to concise mechanistic findings and primary sources (context IDs); useful for populating disease knowledge bases and for rapid evidence lookup.*

Limitations and gaps
- Some mechanistic aspects (e.g., exact sequence of TFEB-driven compensations vs. maladaptations; cell-type specific contributions beyond muscle/heart) require additional targeted studies. While recent reviews and case series provide updated context, large-scale mechanistic clinical correlates remain limited; ongoing natural history and interventional trials should refine quantitative progression models and biomarker frameworks. (NCT06214507, NCT06092034, NCT05548855)


References

1. (cenacchi2020reviewdanondisease pages 19-21): G. Cenacchi, V. Papa, V. Pegoraro, R. Marozzo, M. Fanin, and C. Angelini. Review: danon disease: review of natural history and recent advances. Neuropathology and Applied Neurobiology, 46:303-322, Nov 2020. URL: https://doi.org/10.1111/nan.12587, doi:10.1111/nan.12587. This article has 103 citations and is from a peer-reviewed journal.

2. (sugie2024historyandperspective pages 3-5): Kazuma Sugie and Ichizo Nishino. History and perspective of lamp-2 deficiency (danon disease). Biomolecules, 14:1272, Oct 2024. URL: https://doi.org/10.3390/biom14101272, doi:10.3390/biom14101272. This article has 10 citations and is from a poor quality or predatory journal.

3. (nascimbeni2018autophagydysregulationin pages 1-2): Anna Chiara Nascimbeni, Marina Fanin, Corrado Angelini, and Marco Sandri. Autophagy dysregulation in danon disease. Cell Death &amp; Disease, 8:e2565-e2565, Jan 2018. URL: https://doi.org/10.1038/cddis.2016.475, doi:10.1038/cddis.2016.475. This article has 84 citations and is from a peer-reviewed journal.

4. (hashem2017impairedmitophagyfacilitates pages 1-2): Sherin I. Hashem, Anne N. Murphy, Ajit S. Divakaruni, Matthew L. Klos, Bradley C. Nelson, Emily C. Gault, Teisha J. Rowland, Cynthia N. Perry, Yusu Gu, Nancy D. Dalton, William H. Bradford, Eric J. Devaney, Kirk L. Peterson, Kenneth L. Jones, Matthew R.G. Taylor, Ju Chen, Neil C. Chi, and Eric D. Adler. Impaired mitophagy facilitates mitochondrial damage in danon disease. Journal of molecular and cellular cardiology, 108:86-94, Jul 2017. URL: https://doi.org/10.1016/j.yjmcc.2017.05.007, doi:10.1016/j.yjmcc.2017.05.007. This article has 78 citations and is from a domain leading peer-reviewed journal.

5. (NCT06092034):  A Gene Therapy Study of RP-A501 in Male Patients With Danon Disease. Rocket Pharmaceuticals Inc.. 2023. ClinicalTrials.gov Identifier: NCT06092034

6. (NCT03882437):  Gene Therapy for Male Patients With Danon Disease (DD) Using RP-A501; AAV9.LAMP2B. Rocket Pharmaceuticals Inc.. 2019. ClinicalTrials.gov Identifier: NCT03882437

7. (nascimbeni2018autophagydysregulationin pages 7-8): Anna Chiara Nascimbeni, Marina Fanin, Corrado Angelini, and Marco Sandri. Autophagy dysregulation in danon disease. Cell Death &amp; Disease, 8:e2565-e2565, Jan 2018. URL: https://doi.org/10.1038/cddis.2016.475, doi:10.1038/cddis.2016.475. This article has 84 citations and is from a peer-reviewed journal.

8. (nascimbeni2018autophagydysregulationin pages 3-7): Anna Chiara Nascimbeni, Marina Fanin, Corrado Angelini, and Marco Sandri. Autophagy dysregulation in danon disease. Cell Death &amp; Disease, 8:e2565-e2565, Jan 2018. URL: https://doi.org/10.1038/cddis.2016.475, doi:10.1038/cddis.2016.475. This article has 84 citations and is from a peer-reviewed journal.

9. (shalata2023danondiseaseentire pages 10-12): Adel Shalata, Marina Bar-Shai, Yarin Hadid, Muhammad Mahroum, Hila Mintz, Zaher Eldin Shalata, Evgeny Radzishevsky, Jacob Genizi, Avraham Lorber, Tamar Ben-Yosef, and Liat Yaniv. Danon disease: entire lamp2 gene deletion with unusual clinical presentation—case report and review of the literature. Genes, 14:1539, Jul 2023. URL: https://doi.org/10.3390/genes14081539, doi:10.3390/genes14081539. This article has 10 citations and is from a poor quality or predatory journal.

10. (nascimbeni2009glycogenosystypeii pages 84-87): AC Nascimbeni. Glycogenosys type ii and danon disease: molecular study and muscle pathology. Unknown journal, 2009.

11. (margeta2020autophagydefectsin pages 17-19): Marta Margeta. Autophagy defects in skeletal myopathies. Annual review of pathology, 15:261-285, Jan 2020. URL: https://doi.org/10.1146/annurev-pathmechdis-012419-032618, doi:10.1146/annurev-pathmechdis-012419-032618. This article has 75 citations and is from a domain leading peer-reviewed journal.

12. (NCT05548855):  Natural History of Danon Disease. Rocket Pharmaceuticals Inc.. 2022. ClinicalTrials.gov Identifier: NCT05548855

13. (NCT06214507):  Danon Disease Natural History Study. Rocket Pharmaceuticals Inc.. 2023. ClinicalTrials.gov Identifier: NCT06214507

14. (sugie2024historyandperspective pages 8-9): Kazuma Sugie and Ichizo Nishino. History and perspective of lamp-2 deficiency (danon disease). Biomolecules, 14:1272, Oct 2024. URL: https://doi.org/10.3390/biom14101272, doi:10.3390/biom14101272. This article has 10 citations and is from a poor quality or predatory journal.
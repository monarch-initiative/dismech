---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T10:01:36.225241'
end_time: '2026-07-26T10:20:22.116713'
duration_seconds: 1125.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Coronary Artery Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 47
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: Coronary_Artery_Disease-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: Coronary_Artery_Disease-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Coronary Artery Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Coronary Artery Disease** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

## Issue-Specific Scope and Evidence Guardrails

For `Coronary_Artery_Disease`, lock the disease identity to `MONDO:0021661`
**coronary atherosclerosis**: atherosclerotic plaque in the epicardial coronary
arteries. Do not substitute `MONDO:0004975`, broad ASCVD, or all coronary
disorders. Exclude spontaneous coronary dissection, vasospasm, congenital
coronary anomalies, coronary embolism, isolated coronary microvascular
dysfunction, and type-2 myocardial infarction except as clearly labeled
differentials or comorbid processes. Stable angina, acute coronary syndrome, and
myocardial infarction are manifestations or complications, not exact synonyms.

Build a staged causal model covering apoB-containing particle entry and
proteoglycan retention; triglyceride-rich remnants; disturbed-flow endothelial
dysfunction; leukocyte recruitment; macrophage foam-cell formation and defective
efferocytosis; smooth-muscle-cell phenotypic modulation and fibrous-cap formation;
necrotic core, calcification, neovascularization, and intraplaque hemorrhage;
plaque growth, remodeling, stenosis, and ischemia; and the distinct terminal
routes of plaque rupture, superficial erosion, coronary thrombosis, and
platelet/coagulation activation. Separate initiation, progression, stability, and
acute thrombosis rather than compressing them into one pathway.

Use this evidence-directness ladder and state the actual vascular bed:

1. Human coronary pathology or coronary CCTA/OCT/IVUS/NIRS is anatomically
   direct, although imaging composition remains a surrogate and does not prove a
   cellular mechanism or clinical mediation.
2. Human coronary-event genetics, circulating biomarkers, and systemic
   interventions are clinically relevant but do not localize a mechanism to
   coronary plaque.
3. Human carotid, aortic, femoral, or peripheral plaque is transferable
   atherosclerosis evidence only; never rewrite it as human coronary evidence.
4. Animal in-vivo evidence is `MODEL_ORGANISM`; specify species and artery.
5. Cultured cells, organoids, isolated lipoproteins, platelets, and ex-vivo
   assays are `IN_VITRO`.
6. Computational networks, trajectories, and mediation estimates are not
   experimental perturbation evidence.

Split mixed papers into distinct evidence items. A human association plus a
mouse perturbation does not make the human result causal. In particular,
PMID:38639096 uses symptomatic carotid plaque within a CAD regulatory
framework, and PMID:40594772 combines mouse carotid disturbed flow with human
carotid plaque; both remain anatomically indirect for coronary plaque.

Prioritize primary studies and include null or discordant evidence. For every
important claim report PMID, design, sample size, vascular site, population,
perturbation and comparator, endpoint, temporal ordering, source type,
funding/conflicts, and causal verdict. Association, single-cell state, spatial
colocalization, genetic liability, imaging surrogate, and randomized outcome
evidence answer different questions. Treat reviews as orientation.

Useful anchors to assess, without assuming their conclusions, include PCSK9
human genetics (PMID:16554528), PROSPECT direct coronary natural history
(PMID:21247313), OCT-defined rupture/erosion (PMID:23810884), CLIMA coronary
morphology/outcomes (PMID:31504405), GLAGOV (PMID:27846344), PACMAN-AMI
(PMID:35368058), CANTOS (PMID:28845751), and mixed human/model TCF21
(PMID:31359001) and clonal-hematopoiesis (PMID:28636844) studies. Separate
components and do not promote surrogate regression or outcome reduction to
proof of a specific cellular mediator.

Verify every ontology identifier and canonical label rather than copying legacy
reports. Known anchors include `MONDO:0021661` coronary atherosclerosis,
`CL:0000359` vascular associated smooth muscle cell, `GO:0019915` lipid storage,
and `GO:0006809` nitric oxide biosynthetic process. Research reports and reviews
are leads, not KB-ready evidence snippets. Return an evidence matrix followed by
the best-supported disease graph, uncertain or vascular-bed-indirect edges,
genuine competing hypotheses, and decisive experiments.

---

### 1. Disease Information
> **Search first:** OMIM, Orphanet, ICD-10/ICD-11, MeSH, PubMed

- What is the disease? Provide a concise overview.
- What are the key identifiers? (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- What are the common synonyms and alternative names?
- Is the information derived from individual patients (e.g., EHR) or aggregated disease-level resources?

### 2. Etiology

- **Disease Causal Factors**: What are the primary causes? (genetic, environmental, infectious, mechanistic)
- **Risk Factors**:
  > **Search first:** PubMed, Cochrane Library, UpToDate, clinical guidelines, ClinVar, ClinGen, GWAS Catalog, PheGenI, CTD, CDC, WHO, epidemiological databases
  - Genetic risk factors (causal variants, susceptibility loci, modifier genes)
  - Environmental risk factors (toxins, lifestyle, occupational exposures, age, sex, family history)
- **Protective Factors**:
  > **Search first:** PubMed, Cochrane Library, clinical trial databases, GWAS Catalog, gnomAD, WHO, CDC, nutrition databases
  - Genetic protective factors (protective variants, modifier alleles)
  - Environmental protective factors (diet, lifestyle, exposures that reduce risk)
- **Gene-Environment Interactions**: How do genetic and environmental factors interact to influence disease?
  > **Search first:** CTD, PubMed, PheGenI, GxE databases

### 3. Phenotypes
> **Search first:** HPO (Human Phenotype Ontology), OMIM, Orphanet, PubMed, clinicaltrials.gov, MedDRA, SNOMED CT, DECIPHER, LOINC

For each phenotype, provide:
- **Phenotype type**: symptoms, clinical signs, physical manifestations, behavioral changes, or laboratory abnormalities
  > For symptoms/signs: HPO, OMIM, Orphanet, PubMed
  > For behavioral changes: HPO, DSM, RDoC (Research Domain Criteria), PubMed
  > For laboratory abnormalities: LOINC, SNOMED CT, LabTests Online, PubMed
- **Phenotype characteristics**:
  > **Search first:** OMIM, Orphanet, HPO, PubMed
  - Age of symptom onset (neonatal, childhood, adult-onset, late-onset)
  - Symptom severity (mild, moderate, severe, variable)
  - Symptom progression (stable, progressive, episodic, fluctuating)
  - Frequency among affected individuals (percentage or qualitative)
- **Quality of life impact**: Effects on daily functioning and well-being (per-phenotype when possible)
  > **Search first:** EQ-5D database, SF-36, WHO QOL databases, PubMed
- Suggest HPO (Human Phenotype Ontology) terms for each phenotype

### 4. Genetic/Molecular Information

- **Causal Genes**: Gene mutations or chromosomal abnormalities responsible for disease (gene symbols, OMIM IDs)
  > **Search first:** OMIM, ClinVar, HGMD, Ensembl, NCBI Gene
- **Pathogenic Variants**:
  - Affected genes (gene symbols, HGNC IDs)
    > **Search first:** OMIM, NCBI Gene, Ensembl, HGNC, UniProt, GeneCards
  - Variant classification (pathogenic, likely pathogenic, VUS per ACMG/AMP guidelines)
    > **Search first:** ClinVar, ClinGen, ACMG/AMP guidelines, VarSome
  - Variant type/class (missense, frameshift, nonsense, splice-site, structural)
  - Allele frequency in population databases
    > **Search first:** gnomAD, 1000 Genomes, ExAC, TOPMed, dbSNP
  - Somatic vs germline origin
    > **Search first:** COSMIC (somatic), ClinVar, ICGC, TCGA
  - Functional consequences (loss of function, gain of function, dominant negative)
- **Modifier Genes**: Genes that modify disease severity or expression
- **Epigenetic Information**: DNA methylation, histone modifications, chromatin changes affecting disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Chromosomal Abnormalities**: Large-scale genetic changes (aneuploidy, translocations, inversions)
  > **Search first:** DECIPHER, ClinVar, ECARUCA, UCSC Genome Browser

### 5. Environmental Information

- **Environmental Factors**: Non-genetic contributing factors (toxins, radiation, pollution, occupational exposure)
  > **Search first:** CTD (Comparative Toxicogenomics Database), TOXNET, PubMed, EPA databases
- **Lifestyle Factors**: Behavioral factors (smoking, diet, exercise, alcohol consumption)
  > **Search first:** CDC databases, WHO, PubMed, NHANES
- **Infectious Agents**: If applicable, pathogens causing or triggering disease (bacteria, viruses, fungi, parasites)
  > **Search first:** NCBI Taxonomy, ViPR, BV-BRC, MicrobeDB, GIDEON

### 6. Mechanism / Pathophysiology

- **Molecular Pathways**: Specific signaling cascades or biochemical pathways involved (Wnt, MAPK, mTOR, PI3K-AKT, etc.)
  > **Search first:** KEGG, Reactome, WikiPathways, PathBank, BioCyc
- **Cellular Processes**: Cell-level mechanisms (apoptosis, autophagy, cell cycle dysregulation, inflammation, etc.)
  > **Search first:** Gene Ontology (GO), Reactome, KEGG, PubMed
- **Protein Dysfunction**: How protein structure or function is altered (misfolding, aggregation, loss of function, gain of function)
  > **Search first:** UniProt, PDB (Protein Data Bank), InterPro, Pfam, AlphaFold
- **Metabolic Changes**: Alterations in metabolic processes (energy metabolism, lipid metabolism, amino acid metabolism)
  > **Search first:** KEGG, BioCyc, HMDB (Human Metabolome Database), BRENDA
- **Immune System Involvement**: Role of immune response (autoimmunity, immunodeficiency, chronic inflammation)
  > **Search first:** ImmPort, Immunome Database, IEDB, Gene Ontology
- **Tissue Damage Mechanisms**: How tissues/ are injured (oxidative stress, ischemia, fibrosis, necrosis)
  > **Search first:** PubMed, Gene Ontology, Reactome
- **Biochemical Abnormalities**: Specific molecular defects (enzyme deficiencies, receptor dysfunction, ion channel defects)
  > **Search first:** BRENDA, UniProt, KEGG, OMIM, PubMed
- **Epigenetic Changes**: DNA methylation, histone modifications affecting gene expression in disease
  > **Search first:** ENCODE, Roadmap Epigenomics, MethBase, DiseaseMeth
- **Molecular Profiling** (if available):
  - Transcriptomics/gene expression changes
    > **Search first:** GEO (Gene Expression Omnibus), ArrayExpress, GTEx, Human Cell Atlas, SRA
  - Proteomics findings
    > **Search first:** PRIDE, ProteomeXchange, Human Protein Atlas, STRING, BioGRID
  - Metabolomics signatures
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB, METLIN
  - Lipidomics alterations
    > **Search first:** LIPID MAPS, SwissLipids, LipidHome, Metabolomics Workbench
  - Genomic structural features
    > **Search first:** UCSC Genome Browser, Ensembl, NCBI, dbVar, DGV
- **Advanced Technologies** (if applicable):
  - Single-cell analysis findings (cell-type specific mechanisms, cellular heterogeneity)
    > **Search first:** Human Cell Atlas, Single Cell Portal, GEO, CELLxGENE
  - Spatial transcriptomics findings
    > **Search first:** GEO, Spatial Research, Vizgen, 10x Genomics data
  - Multi-omics integration results
    > **Search first:** TCGA, ICGC, cBioPortal, LinkedOmics, PubMed
  - Functional genomics screens (CRISPR, RNAi)
    > **Search first:** DepMap, GenomeRNAi, PubMed, BioGRID ORCS

For each mechanism, describe:
- The causal chain from initial trigger to clinical manifestation
- Which mechanisms are upstream vs downstream
- What cell types and biological processes are involved
- Suggest GO terms for biological processes and CL terms for cell types

### 7. Anatomical Structures Affected

- **Organ Level**:
  - Primary organs directly affected
  - Secondary organ involvement (complications, secondary effects)
  - Body systems involved (cardiovascular, nervous, digestive, respiratory, endocrine, etc.)
  > **Search first:** Uberon, FMA (Foundational Model of Anatomy), OMIM, HPO, ICD-11, MeSH, SNOMED CT
- **Tissue and Cell Level**:
  - Specific tissue types affected (epithelial, connective, muscle, nervous)
  - Specific cell populations targeted (with Cell Ontology terms)
  > **Search first:** Uberon, Human Protein Atlas, Cell Ontology, Human Cell Atlas, CellMarker, PanglaoDB
- **Subcellular Level**:
  - Cellular compartments involved (mitochondria, nucleus, ER, lysosomes) (with GO Cellular Component terms)
  > **Search first:** Gene Ontology (Cellular Component), UniProt, Human Protein Atlas
- **Localization**:
  - Specific anatomical sites (with UBERON terms)
    > **Search first:** FMA, Uberon, NeuroNames (for brain), SNOMED CT
  - Lateralization (unilateral, bilateral, asymmetric)
    > **Search first:** HPO, clinical literature, imaging databases

### 8. Temporal Development

- **Onset**:
  - Typical age of onset (congenital, pediatric, adult, geriatric)
  - Onset pattern (acute, subacute, chronic, insidious)
  > **Search first:** OMIM, Orphanet, HPO, PubMed
- **Progression**:
  - Disease stages (early, intermediate, advanced, end-stage)
    > **Search first:** Cancer Staging Manual (AJCC), WHO classifications, PubMed
  - Progression rate (rapid, slow, variable)
  - Disease course pattern (episodic, relapsing-remitting, progressive, stable)
  - Disease duration (self-limited, chronic lifelong)
  > **Search first:** Disease registries, longitudinal cohort databases, natural history studies, PubMed, Orphanet, OMIM
- **Patterns**:
  - Remission patterns (spontaneous, treatment-induced)
    > **Search first:** Clinical trial databases, disease registries, PubMed
  - Critical periods (time windows of vulnerability or opportunity for intervention)
    > **Search first:** PubMed, developmental biology databases, clinical guidelines

### 9. Inheritance and Population

- **Epidemiology**:
  - Prevalence (cases per 100,000 at given time)
  - Incidence (new cases per 100,000 per year)
  > **Search first:** Orphanet, CDC, WHO, GBD (Global Burden of Disease), national registries, SEER, disease registries
- **For Genetic Etiology**:
  - Inheritance pattern (AD, AR, X-linked, mitochondrial, multifactorial, polygenic)
    > **Search first:** OMIM, Orphanet, ClinVar, GTR (Genetic Testing Registry)
  - Penetrance (complete, incomplete, age-dependent)
    > **Search first:** ClinVar, OMIM, PubMed, ClinGen
  - Expressivity (variable, consistent)
    > **Search first:** OMIM, ClinVar, PubMed
  - Genetic anticipation (increasing severity in successive generations)
    > **Search first:** OMIM, PubMed (especially for repeat expansion disorders)
  - Germline mosaicism
    > **Search first:** ClinVar, OMIM, genetic counseling literature, PubMed
  - Founder effects (population-specific mutations)
    > **Search first:** gnomAD, population genetics databases, PubMed
  - Consanguinity role
    > **Search first:** OMIM, population studies, genetic counseling resources
  - Carrier frequency
    > **Search first:** gnomAD, carrier screening databases, GeneReviews, GTR
- **Population Demographics**:
  - Affected populations (ethnic or demographic groups with higher prevalence)
    > **Search first:** gnomAD, 1000 Genomes, PAGE Study, PubMed, population registries
  - Geographic distribution (endemic areas, regional variation)
    > **Search first:** WHO, CDC, GBD, Orphanet, geographic epidemiology databases
  - Geographic distribution of specific variants
  - Sex ratio (male:female)
    > **Search first:** Disease registries, OMIM, PubMed, epidemiological databases
  - Age distribution of affected individuals
    > **Search first:** CDC, disease registries, SEER, Orphanet

### 10. Diagnostics

- **Clinical Tests**:
  - Laboratory tests (blood, urine, tissue chemistry, specific enzyme assays)
    > **Search first:** LOINC, LabTests Online, PubMed
  - Biomarkers (proteins, metabolites, genetic markers, circulating biomarkers)
    > **Search first:** FDA Biomarker List, BEST (Biomarkers, EndpointS, and other Tools), PubMed
  - Imaging studies (X-ray, CT, MRI, PET, ultrasound)
    > **Search first:** RadLex, DICOM, Radiopaedia, imaging databases
  - Functional tests (pulmonary function, cardiac stress tests)
    > **Search first:** LOINC, clinical guidelines, PubMed
  - Electrophysiology (EEG, EMG, ECG, nerve conduction studies)
    > **Search first:** LOINC, clinical neurophysiology databases, PubMed
  - Biopsy findings (histopathology, immunohistochemistry)
    > **Search first:** SNOMED CT, College of American Pathologists resources, PubMed
  - Pathology findings (microscopic examination)
    > **Search first:** SNOMED CT, Digital Pathology databases, PubMed
- **Genetic Testing**:
  > **Search first:** GTR (Genetic Testing Registry), GeneReviews, ClinGen
  - Overview of recommended genetic testing approach
  - Whole genome sequencing (WGS) utility
    > **Search first:** GTR, ClinVar, GEL (Genomics England), gnomAD
  - Whole exome sequencing (WES) utility
    > **Search first:** GTR, ClinVar, OMIM, GeneMatcher
  - Gene panels (which panels, which genes)
    > **Search first:** GTR, ClinVar, laboratory-specific databases
  - Single gene testing
    > **Search first:** GTR, ClinVar, OMIM, GeneReviews
  - Chromosomal microarray (CMA)
    > **Search first:** DECIPHER, ClinVar, dbVar, ECARUCA
  - Karyotyping
    > **Search first:** Chromosome Abnormality Database, ClinVar, cytogenetics resources
  - FISH
    > **Search first:** ClinVar, cytogenetics databases, PubMed
  - Mitochondrial DNA testing
    > **Search first:** MITOMAP, MSeqDR, ClinVar, GTR
  - Repeat expansion testing
    > **Search first:** GTR, ClinVar, repeat expansion databases, PubMed
- **Omics-Based Diagnostics** (if applicable):
  - RNA sequencing / transcriptomics
    > **Search first:** GEO, ArrayExpress, GTEx, RNA-seq databases
  - Proteomics
    > **Search first:** PRIDE, ProteomeXchange, FDA Biomarker database
  - Metabolomics
    > **Search first:** MetaboLights, Metabolomics Workbench, HMDB
  - Epigenomics
    > **Search first:** GEO, ENCODE, Roadmap Epigenomics, MethBase
  - Liquid biopsy
    > **Search first:** COSMIC, ClinVar, liquid biopsy databases, PubMed
- **Clinical Criteria**:
  - Standardized diagnostic criteria (DSM, ICD, society guidelines)
    > **Search first:** DSM-5, ICD-11, clinical society guidelines, UpToDate
  - Differential diagnosis (other conditions to rule out, with distinguishing features)
    > **Search first:** DynaMed, UpToDate, clinical decision support systems
- **Screening**:
  - Screening methods for asymptomatic individuals (newborn screening, carrier screening, cascade screening)
    > **Search first:** ACMG recommendations, CDC newborn screening, GTR

### 11. Outcome/Prognosis

- **Survival and Mortality**:
  - Survival rate (5-year, 10-year, overall)
    > **Search first:** SEER, cancer registries, disease-specific registries, PubMed
  - Life expectancy (with and without treatment if applicable)
    > **Search first:** Orphanet, disease registries, actuarial databases, PubMed
  - Mortality rate
    > **Search first:** CDC, WHO, GBD, national mortality databases
  - Disease-specific mortality (deaths directly attributable to disease)
    > **Search first:** Disease registries, CDC Wonder, GBD, PubMed
- **Morbidity and Function**:
  - Morbidity (disease-related disability and health impacts)
    > **Search first:** GBD, WHO, disability databases, PubMed
  - Disability outcomes (long-term functional impairments)
    > **Search first:** ICF (International Classification of Functioning), disability registries
  - Quality of life measures (EQ-5D, SF-36, PROMIS, disease-specific tools)
    > **Search first:** EQ-5D database, SF-36, PROMIS, PubMed
- **Disease Course**:
  - Complications (secondary problems: infections, organ failure, etc.)
    > **Search first:** ICD codes, disease registries, clinical databases, PubMed
  - Recovery potential (likelihood and extent of recovery, with vs without treatment)
    > **Search first:** Natural history studies, rehabilitation databases, PubMed
- **Prediction**:
  - Prognostic factors (age, disease severity, biomarkers, treatment response)
    > **Search first:** Prognostic models databases, clinical calculators, PubMed
  - Prognostic biomarkers (molecular markers predicting disease course)
    > **Search first:** FDA Biomarker database, PubMed, cancer prognostic databases

### 12. Treatment

- **Pharmacotherapy**:
  - Pharmacological treatments (drug names, drug classes, mechanisms of action)
    > **Search first:** DrugBank, RxNorm, ATC classification, DailyMed, FDA databases
  - Pharmacogenomics (how genetic variants affect drug metabolism, efficacy, toxicity)
    > **Search first:** PharmGKB, CPIC (Clinical Pharmacogenetics), FDA Table of PGx Biomarkers
- **Advanced Therapeutics**:
  - Gene therapy (viral vectors, CRISPR, gene replacement, gene editing)
    > **Search first:** ClinicalTrials.gov, FDA gene therapy database, ASGCT resources
  - Cell therapy (stem cell transplant, CAR-T, cellular therapeutics)
    > **Search first:** ClinicalTrials.gov, FDA cell therapy database, FACT standards
  - RNA-based therapies (ASOs, siRNA, mRNA therapies)
    > **Search first:** ClinicalTrials.gov, FDA approvals, PubMed
  - Targeted therapies (treatments directed at specific molecular targets)
    > **Search first:** My Cancer Genome, OncoKB, ClinicalTrials.gov, FDA approvals
  - Immunotherapies (checkpoint inhibitors, monoclonal antibodies)
    > **Search first:** Cancer Immunotherapy Database, FDA approvals, ClinicalTrials.gov
- **Surgical and Interventional**:
  - Surgical interventions (types of surgery, timing, outcomes)
    > **Search first:** CPT codes, surgical registries, clinical guidelines, PubMed
- **Supportive and Rehabilitative**:
  - Supportive care (symptom management, pain control, nutrition)
    > **Search first:** Clinical guidelines, Cochrane Library, PubMed
  - Rehabilitation (physical therapy, occupational therapy, speech therapy)
    > **Search first:** Rehabilitation medicine databases, clinical guidelines, PubMed
- **Experimental**:
  - Experimental treatments in clinical trials (with NCT identifiers if available)
    > **Search first:** ClinicalTrials.gov, EU Clinical Trials Register, WHO ICTRP
- **Treatment Outcomes**:
  - Treatment response rates
    > **Search first:** Clinical trial databases, FDA reviews, systematic reviews, PubMed
  - Side effects and adverse events
    > **Search first:** FDA Adverse Event Reporting System (FAERS), MedWatch, PubMed
- **Treatment Strategy**:
  - Treatment algorithms (clinical pathways, decision trees)
    > **Search first:** Clinical practice guidelines, NCCN Guidelines, UpToDate
  - Combination therapies
    > **Search first:** ClinicalTrials.gov, treatment guidelines, PubMed
  - Personalized medicine approaches (genotype-guided treatment)
    > **Search first:** My Cancer Genome, CIViC, PharmGKB, precision medicine databases

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

### 13. Prevention

- **Prevention Levels**:
  - Primary prevention (preventing disease occurrence: vaccination, risk factor modification)
    > **Search first:** CDC, WHO, USPSTF recommendations, Cochrane Library
  - Secondary prevention (early detection and treatment: screening programs, early intervention)
    > **Search first:** USPSTF, CDC screening guidelines, WHO
  - Tertiary prevention (preventing complications in those with disease)
    > **Search first:** Clinical guidelines, disease management protocols, PubMed
- **Immunization**: Vaccine strategies (if applicable)
  > **Search first:** CDC vaccine schedules, WHO immunization, FDA vaccine database
- **Screening and Early Detection**:
  - Screening programs (population-based: newborn screening, cancer screening)
    > **Search first:** CDC screening programs, USPSTF, cancer screening databases
  - Genetic screening (carrier screening, preimplantation genetic diagnosis, prenatal testing)
    > **Search first:** ACMG recommendations, ACOG guidelines, GTR
  - Risk stratification (identifying high-risk individuals for targeted prevention)
    > **Search first:** Risk prediction models, clinical calculators, PubMed
- **Behavioral Interventions**: Lifestyle modifications to reduce risk
  > **Search first:** CDC, WHO, behavioral intervention databases, Cochrane Library
- **Counseling**: Genetic counseling (risk assessment, family planning guidance)
  > **Search first:** NSGC resources, ACMG guidelines, GeneReviews
- **Public Health**:
  - Public health interventions (sanitation, vector control, health education)
    > **Search first:** CDC, WHO, public health databases, PubMed
  - Environmental interventions (reducing environmental risk factors)
    > **Search first:** EPA databases, WHO environmental health, PubMed
- **Prophylaxis**: Preventive medications or procedures
  > **Search first:** Clinical guidelines, FDA approvals, PubMed

### 14. Other Species / Natural Disease

- **Taxonomy**: Species affected (with NCBI Taxon identifiers)
  > **Search first:** NCBI Taxonomy
- **Breed**: Specific breeds affected (with VBO identifiers if applicable)
  > **Search first:** VBO (Vertebrate Breed Ontology)
- **Gene**: Orthologous genes in other species (with NCBI Gene IDs)
  > **Search first:** NCBI Gene
- **Natural Disease**:
  - Naturally occurring disease in other species (companion animals, wildlife)
    > **Search first:** OMIA (Online Mendelian Inheritance in Animals), VetCompass, PubMed
  - Veterinary relevance and importance in animal health
    > **Search first:** OMIA, veterinary databases, PubMed
- **Comparative Biology**:
  - Comparative pathology (similarities and differences across species)
    > **Search first:** OMIA, comparative pathology databases, PubMed
  - Evolutionary conservation of disease mechanisms
    > **Search first:** HomoloGene, OrthoMCL, Alliance of Genome Resources
- **Transmission** (if applicable):
  - Zoonotic potential
    > **Search first:** CDC zoonotic diseases, WHO zoonoses, GIDEON
  - Cross-species susceptibility
    > **Search first:** NCBI Taxonomy, veterinary databases, PubMed

### 15. Model Organisms

- **Model Types**:
  - Model organism type (mammalian, invertebrate, cellular, in vitro)
    > **Search first:** Alliance of Genome Resources, model organism databases
  - Specific model systems (mouse, rat, zebrafish, Drosophila, C. elegans, yeast, cell lines, organoids, iPSCs)
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, SGD, ATCC, Cellosaurus
  - Induced models (drug treatment, surgical intervention, environmental manipulation)
    > **Search first:** MGI, model organism databases, PubMed
- **Genetic Models**:
  - Types available (knockout, knock-in, transgenic, conditional, humanized)
    > **Search first:** MGI, IMPC, KOMP, EuMMCR, IMSR
- **Model Characteristics**:
  - Phenotype recapitulation (how well model reproduces human disease features)
    > **Search first:** Model organism databases, comparative studies, PubMed
  - Model limitations (aspects of human disease not captured)
    > **Search first:** Model organism databases, PubMed, review articles
- **Applications**:
  - Research applications (what aspects of disease can be studied)
    > **Search first:** Model organism databases, PubMed
- **Resources**:
  - Model databases
    > **Search first:** MGI, RGD, ZFIN, FlyBase, WormBase, IMSR, EMMA, MMRRC

---

## Citation Requirements

- Cite primary literature (PMID preferred) for all mechanistic and clinical claims
- Prioritize recent reviews and landmark papers
- Include direct quotes from abstracts where possible to support key statements
- Distinguish evidence source types: human clinical, model organism, in vitro, computational

## Output Format

Structure your response as a comprehensive narrative organized by the sections above.
For each section, provide:
- Factual content with specific details (numbers, percentages, gene names, variant nomenclature)
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
- Evidence citations with PMIDs
- Direct quotes from abstracts to support key claims
- Clear indication when information is not available or not applicable for this disease

This report will be used to populate a disease knowledge base entry with:
- Pathophysiology descriptions with causal chains
- Gene/protein annotations (HGNC, GO terms)
- Phenotype associations (HP terms) with frequencies
- Cell type involvement (CL terms)
- Anatomical locations (UBERON terms)
- Chemical entities (CHEBI terms)
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Coronary Artery Disease (Coronary Atherosclerosis, MONDO:0021661): A Comprehensive Disease Characterization Report

## Summary

**Coronary artery disease**, defined here strictly as **coronary atherosclerosis (`MONDO:0021661`)** — atherosclerotic plaque formation in the intima of the epicardial coronary arteries — is a chronic, polygenic, lipid-initiated and inflammation-amplified disease. The best-supported causal model is a **staged process**: subendothelial retention of apolipoprotein-B (apoB)-containing lipoproteins at disturbed-flow arterial sites drives endothelial dysfunction, monocyte recruitment, macrophage foam-cell formation with defective apoptotic-cell clearance (efferocytosis), and smooth-muscle-cell (SMC) phenotypic switching. These processes generate plaques whose **composition** — a lipid/necrotic core beneath a thin fibrous cap — rather than the **degree of luminal stenosis**, precipitates acute coronary events. Two histologically distinct terminal routes convert stable plaque into coronary thrombosis: **plaque rupture** (~2/3 of ACS) and **superficial erosion** (~1/3 of ACS).

The causal centrality of apoB/LDL is established at the highest evidence tier by convergent **human genetics** (PCSK9 loss-of-function and LPA variants) and **randomized outcome and imaging trials** (statins, PCSK9 inhibitors, bempedoic acid). Independently, **inflammation is causal**: IL-1β inhibition (canakinumab, CANTOS) and colchicine reduce coronary events *without* lowering lipids, isolating an IL-1β→IL-6→CRP axis. Coronary-specific imaging evidence (PROSPECT natural history, NIRS-IVUS/OCT wall-shear-stress studies, MESA coronary artery calcium) anchors the anatomy and prognostic value of plaque burden and composition directly in the coronary bed. Model-organism and in-vitro work (MerTK efferocytosis, SMC lineage tracing, IL-1β-induced LDL transcytosis) supplies mechanism but is labeled by species and vascular bed and does not, alone, establish human coronary causality.

Clinically, CAD is managed by aggressive apoB/LDL lowering, anti-inflammatory therapy in selected patients, and antithrombotics; **revascularization relieves symptoms but does not reduce death or MI in stable disease** (ISCHEMIA). This report organizes the evidence across the 15 requested domains, maintaining an explicit evidence-directness ladder (human coronary → human systemic → transferable non-coronary plaque → model organism → in vitro → computational) and flagging discordant/null findings.

---

## Evidence Matrix (Directness Ladder Applied)

**Directness ladder:** T1 = human coronary pathology/imaging (anatomically direct; imaging composition = surrogate); T2 = human coronary-event genetics/biomarker/systemic intervention (clinically relevant, not plaque-localized); T3 = human carotid/aortic/peripheral plaque (transferable, indirect for coronary); T4 = animal in-vivo (MODEL_ORGANISM); T5 = cultured cells/ex-vivo (IN_VITRO); T6 = computational.

| ID | Claim | Design / n | Vascular site | Tier | Causal verdict |
|----|-------|-----------|---------------|------|----------------|
| F009 | PCSK9 LoF → lower LDL → 47–88% lower CHD | ARIC cohort, 15 yr | Human coronary events | T2 genetics | Causal for LDL→CHD |
| F002 | PCSK9 inhibition regresses coronary atheroma | GLAGOV RCT, n=968, serial IVUS | Human **coronary** | T1 imaging surrogate | Causal for LDL→plaque volume |
| F013 | Statin: −21% MVE per 1 mmol/L LDL | CTT meta, 28 RCTs, n=186,854 | Human coronary events | T2 RCT | Causal, LDL-dependent |
| F011 | IL-1β inhibition ↓ events without lipid change | CANTOS RCT, n=10,061 | Human coronary events | T2 RCT | Causal for inflammation |
| F012 | Colchicine ↓ MACE (COLCOT, LoDoCo2) | RCTs / meta | Human coronary events | T2 RCT | Causal for inflammation |
| F001 | Plaque burden/MLA/TCFA predict events | PROSPECT, n=697, IVUS | Human **coronary** | T1 natural history | Prognostic (composition) |
| F007 | Low WSS + lipid → coronary plaque growth | n=40, NIRS-IVUS/OCT | Human **coronary** | T1 imaging | Direct coronary hemodynamic |
| F003 | Rupture vs erosion = 2 terminal routes | OCT in-vivo | Human **coronary** | T1 imaging | Mechanistic (terminal) |
| F014 | CAC & progression predict CHD | MESA, n=6,778 | Human **coronary** | T1 imaging | Prognostic |
| F006/F010 | 9p21.3, LPA strongest loci; Lp(a) causal | GWAS/MR | Human coronary events | T2 genetics | Causal (Lp(a)) |
| F005 | CHIP → inflammatory ASCVD risk | UK Biobank, n=13,129 | Human systemic | T2 + mouse | Assoc. + model causal |
| F015 | 9 risk factors = >90% MI PAR | INTERHEART, n=27,098 | Human MI | T2 case-control | Population attributable |
| F008 | MerTK efferocytosis failure → necrotic core | Apoe−/− mice | Mouse aortic root | T4 model | Model causal |
| F004 | SMC → macrophage-like switching destabilizes | Lineage tracing + scRNA | Mouse + human plaque | T4–T3 | Mechanistic hypothesis |
| F016 | Mouse models recapitulate lipid plaque, not coronary events | Apoe/Ldlr−/− etc. | Mouse aorta | T4 | Model limitation |
| F017 | Revascularization no death/MI benefit in stable CAD | ISCHEMIA | Human coronary | T2 RCT | Causal (null for hard events) |

---

## 1. Disease Information

**Coronary atherosclerosis** is the accumulation of atherosclerotic plaque — lipid, inflammatory cells, smooth-muscle cells, extracellular matrix, calcification and necrotic debris — within the intima of the epicardial coronary arteries, progressively narrowing the lumen and/or destabilizing to cause thrombosis. It is the dominant substrate of **ischemic heart disease** and the leading cause of death worldwide.

**Key identifiers:**
- **Mondo:** `MONDO:0021661` (coronary atherosclerosis) — the locked disease identity. `MONDO:0004975`, broad ASCVD, and "all coronary disorders" are explicitly *excluded*.
- **MeSH:** Coronary Artery Disease (D003324); Coronary Atherosclerosis
- **ICD-10:** I25.1 (atherosclerotic heart disease of native coronary artery)
- **ICD-11:** BA80 (ischaemic heart disease block)
- **SNOMED CT:** 53741008 (coronary arteriosclerosis)

**Synonyms / near-terms (with scope caveats):** coronary atherosclerosis, atherosclerotic heart disease, coronary arteriosclerosis. **Not exact synonyms:** stable angina, acute coronary syndrome (ACS), and myocardial infarction (MI) are *manifestations/complications*. **Excluded differentials:** spontaneous coronary artery dissection (SCAD), coronary vasospasm, congenital coronary anomalies, coronary embolism, isolated coronary microvascular dysfunction, and type-2 MI.

**Data provenance:** This report synthesizes **aggregated disease-level resources** (RCTs, cohort studies, GWAS meta-analyses, imaging natural-history studies), not individual patient EHR records.

---

## 2. Etiology

### Disease causal factors
CAD is a **multifactorial, polygenic** disease. The initiating causal factor is **subendothelial retention of apoB-containing lipoproteins** (LDL, remnant/triglyceride-rich lipoproteins, and Lp(a)), superimposed on hemodynamic (disturbed-flow) and inflammatory contributors.

**Human-genetic proof of LDL causality (F009):** In ARIC (15-yr follow-up), PCSK9 nonsense mutations (2.6% of Black participants) conferred a **28% lower LDL-C and 88% lower CHD risk** (HR 0.11, 95% CI 0.02–0.81); a PCSK9 variant in White participants gave 15% lower LDL-C and 47% lower CHD risk (HR 0.50, 95% CI 0.32–0.79). *"these mutations were associated with a 28 percent reduction in mean LDL cholesterol and an 88 percent reduction in the risk of CHD"* ([PMID: 16554528](https://pubmed.ncbi.nlm.nih.gov/16554528/)). This natural experiment demonstrates that **lifelong lower apoB exposure yields disproportionately large CHD reduction**.

### Genetic risk factors (F006, F010)
- **9p21.3 / CDKN2A/B** (rs1333049) — the most replicated common CAD locus; also a shared T2DM–CAD signal (strongest local genetic correlation; T2DM–CAD rg=0.39, P=1.43×10⁻⁷⁵) ([PMID: 38062574](https://pubmed.ncbi.nlm.nih.gov/38062574/)).
- **LPA / lipoprotein(a)** (rs10455872) — one of the two strongest CAD risk loci ([PMID: 30482443](https://pubmed.ncbi.nlm.nih.gov/30482443/)); Mendelian randomization confirms Lp(a) **causally** raises risk of CHD, large-artery stroke, PAD and aortic stenosis: *"Mendelian randomization confirms causal relationships with coronary heart disease, large-artery stroke, peripheral artery disease, and aortic stenosis"* ([PMID: 41789317](https://pubmed.ncbi.nlm.nih.gov/41789317/)). Lp(a) is 70–90% genetically determined and elevated in ~20% of the global population.
- **CDKN2B (9p21.3)** also replicated as an ankle-brachial-index/PAD–CAD locus ([PMID: 41252360](https://pubmed.ncbi.nlm.nih.gov/41252360/)).

### Environmental / lifestyle risk factors (F015)
INTERHEART (52 countries, ~27,098 participants) found **nine modifiable risk factors account for >90% of MI population-attributable risk** (women 96% vs men 93%): abnormal lipids (ApoB:ApoA1), current smoking, hypertension, diabetes, abdominal obesity, psychosocial stress, low fruit/vegetable intake, physical inactivity, and no/low alcohol. *"The population attributable risk (PAR) of all nine risk factors exceeded 94%, and was similar among women and men (96 vs. 93%)"* ([PMID: 18334475](https://pubmed.ncbi.nlm.nih.gov/18334475/)).

### Protective factors
- **Genetic:** PCSK9 loss-of-function alleles (F009); constitutionally low-Lp(a) genotypes.
- **Environmental:** the inverse of the INTERHEART factors — physical activity, fruit/vegetable intake, moderate alcohol, non-smoking. Pharmacologic LDL lowering is protective regardless of mechanism (F013).

### Gene–environment interactions
The T2DM–CAD relationship is **bidirectional and partly genetic** (rg largely BMI-independent, 0.31), mediated substantially by systolic blood pressure and statin use ([PMID: 38062574](https://pubmed.ncbi.nlm.nih.gov/38062574/)). CHIP illustrates a somatic-genetic × inflammatory-environment interaction (F005).

---

## 3. Phenotypes

CAD is **asymptomatic during plaque development** (subclinical for decades) and becomes clinically manifest through ischemic syndromes. Per the scope guardrails, these are *manifestations/complications*, not synonyms.

| Phenotype | Type | HPO suggestion | Onset / course | Frequency |
|-----------|------|----------------|----------------|-----------|
| Angina pectoris (exertional chest pain/pressure) | Symptom | HP:0001681 (Angina pectoris) | Adult/late-onset; episodic, exertional | Common in symptomatic CAD |
| Myocardial infarction | Clinical event | HP:0001658 (Myocardial infarction) | Acute; median first MI age 56 (men) / 65 (women) | Terminal complication |
| Coronary artery atherosclerosis | Physical/imaging sign | HP:0001677 | Adult; progressive | Ubiquitous by definition |
| Dyspnea on exertion | Symptom | HP:0002875 | Progressive | Frequent |
| Elevated troponin | Lab abnormality | HP:0410174 (Increased circulating troponin) | Acute (ACS/MI) | Diagnostic for MI |
| Coronary artery calcification | Imaging sign | — | Adult; progressive | ~50% baseline prevalence, MESA age 45–84 |
| Sudden cardiac death | Clinical event | HP:0001645 (Sudden cardiac death) | Acute | Can be first presentation |

**Age of onset:** typically adult/late-onset, with earlier clinical onset in men (median first MI 56 vs 65 yr in women) (F015). **Severity/progression:** variable and generally progressive but modifiable; long asymptomatic phase punctuated by acute episodes. **QoL impact:** angina limits daily functioning; captured by disease-specific tools (Seattle Angina Questionnaire) and generic measures (EQ-5D, SF-36). In stable disease, revascularization's main benefit is **angina relief** rather than event reduction (F017).

---

## 4. Genetic / Molecular Information

CAD is **polygenic/multifactorial**, not a Mendelian single-gene disorder, except that monogenic hypercholesterolemias greatly accelerate coronary atherosclerosis (familial hypercholesterolemia: *LDLR*, *APOB*, *PCSK9* gain-of-function).

**Key genes / loci:**
- **PCSK9** (HGNC:20001) — loss-of-function is protective (F009); gain-of-function causes FH. Functional consequence: LoF → increased hepatic LDLR → lower LDL.
- **LDLR** — the classic FH gene; central to LDL clearance.
- **LPA** (HGNC:6667) — determines Lp(a); causal for CAD (F010).
- **CDKN2A/CDKN2B (9p21.3)** — strongest common susceptibility locus (F006); non-coding regulatory effect on vascular SMC biology.
- **TCF21** — coronary-disease GWAS gene modulating SMC phenotype (anchor PMID:31359001, mixed human/model evidence).

**Modifier / acquired genetic drivers — CHIP (F005):** Somatic mutations in hematopoietic stem cells. **DNMT3A and TET2 are the two most frequently mutated CHIP genes** ([PMID: 36097025](https://pubmed.ncbi.nlm.nih.gov/36097025/)). In UK Biobank (n=13,129 with ASCVD): *"any CHIP and large CHIP at baseline were associated with adjusted HRs of 1.23 (95% CI: 1.10-1.38; P < 0.001) and 1.34 (95% CI: 1.17-1.53; P < 0.001), respectively, for the primary outcome"* ([PMID: 37197843](https://pubmed.ncbi.nlm.nih.gov/37197843/)); large TET2 HR 1.89, large spliceosome HR 3.02. Murine Tet2/Dnmt3a loss-of-function supports an IL-1β/inflammasome-mediated causal mechanism ([PMID: 31345433](https://pubmed.ncbi.nlm.nih.gov/31345433/)).

**Epigenetics:** DNMT3A and TET2 CHIP produce distinct, directionally opposing genome-wide DNA-methylation patterns; Mendelian randomization suggests some DNAm alterations promote CAD risk ([PMID: 36097025](https://pubmed.ncbi.nlm.nih.gov/36097025/)).

**Chromosomal abnormalities:** Not a defining feature of coronary atherosclerosis. The most relevant "large-scale" genetic contributor is clonal expansion of mutant hematopoietic clones (CHIP), not aneuploidy.

**Variant classification / population frequency:** PCSK9 protective LoF alleles (e.g., Y142X, C679X) are more frequent in individuals of African ancestry (~2–3%); classified benign-protective. FH-causing LDLR/APOB/PCSK9-GoF variants span missense, nonsense, frameshift, and splice-site classes (pathogenic/likely pathogenic per ACMG/AMP in ClinVar). All germline; CHIP mutations are **somatic**.

---

## 5. Environmental Information

- **Lifestyle factors (F015):** smoking, atherogenic diet (high saturated fat/refined carbohydrate), physical inactivity, abdominal obesity, and psychosocial stress. Current smoking and abnormal lipids are among the strongest INTERHEART contributors.
- **Environmental exposures:** ambient air pollution (particulate matter) is an established population risk factor for ischemic heart disease.
- **Metabolic environment:** diabetes/hyperglycemia (bidirectional with CAD, [PMID: 38062574](https://pubmed.ncbi.nlm.nih.gov/38062574/)) and hypertension.
- **Infectious agents:** CAD is **not an infectious disease**. Chronic low-grade inflammation (not a specific pathogen) is the operative inflammatory driver; the causal inflammatory axis is IL-1β→IL-6→CRP (F011, F012), not a microbe.

---

## 6. Mechanism / Pathophysiology

### Staged causal model

```
apoB-lipoprotein entry & proteoglycan retention  (CAUSAL: PCSK9/LPA genetics, LDL RCTs)
        │  (amplified at disturbed-flow / low wall-shear-stress sites)
        ▼
Endothelial dysfunction & activation  (↓eNOS/NO GO:0006809; ↑adhesion molecules)
        │  IL-1β can induce LDLR/Rab27a-dependent LDL transcytosis (IN VITRO/mouse)
        ▼
Leukocyte recruitment → monocyte entry
        ▼
Macrophage foam-cell formation (CD36/oxLDL uptake; GO:0019915 lipid storage)
        ▼
Defective efferocytosis (MerTK)  →  secondary necrosis  (MODEL ORGANISM: Apoe−/− mice)
        ▼
Necrotic core expansion + SMC phenotypic switching (contractile→synthetic/
   macrophage-like/osteogenic; CL:0000359) → fibrous cap thinning
        ▼
Calcification, neovascularization, intraplaque hemorrhage → plaque growth/remodeling
        ▼
   ┌─────────────────────────────┬──────────────────────────────┐
   ▼ TERMINAL ROUTE 1            ▼ TERMINAL ROUTE 2
 Plaque RUPTURE (~2/3 ACS)     Superficial EROSION (~1/3 ACS)
 thin cap + large necrotic     intact cap, less necrosis/
 core + inflammation           inflammation, larger lumen
        └──────────────┬───────────────┘
                       ▼
        Platelet/coagulation activation → CORONARY THROMBOSIS → MI / sudden death

     (Non-thrombotic route: progressive stenosis → demand ischemia → stable angina)
```

### Molecular pathways & cellular processes
- **Lipid retention & foam-cell formation:** apoB-lipoprotein subendothelial retention; scavenger-receptor (CD36) uptake of oxLDL; **lipid storage (GO:0019915)**. In vitro, oxLDL downregulates the PPARγ/LXRα/MerTK efferocytosis axis and upregulates competitive receptor CD300a, driving CD36-mediated foam-cell formation ([PMID: 36721069](https://pubmed.ncbi.nlm.nih.gov/36721069/)).
- **Endothelial mechanotransduction:** low wall shear stress downregulates **eNOS / nitric-oxide biosynthesis (GO:0006809)** and upregulates E-selectin/ICAM-1, promoting leukocyte adhesion (in-vitro HUVEC/microfluidic, [PMID: 34948110](https://pubmed.ncbi.nlm.nih.gov/34948110/)); NRP2/PARP1 mediate low-shear endothelial apoptosis in mouse aorta ([PMID: 35028975](https://pubmed.ncbi.nlm.nih.gov/35028975/)).
- **Efferocytosis / apoptotic-cell clearance (F008):** In *Mertk*-kinase-dead;*Apoe⁻/⁻* mice, lesions accumulated apoptotic cells and became more necrotic — *"mutation of the phagocytic Mertk receptor promotes the accumulation of apoptotic cells"* ([PMID: 18451332](https://pubmed.ncbi.nlm.nih.gov/18451332/)). **Species: mouse; site: aortic root — not coronary.**
- **SMC plasticity (F004):** Contractile vascular-associated SMCs (**CL:0000359**) dedifferentiate to synthetic, macrophage-like, osteoblast-like states. *"most of lesional macrophages... are derived from macrophage-like cells (MLCs) dedifferentiated from the VSMCs lineage... promoting... necrotic core expansion and fibrous cap thinning"* ([PMID: 41165871](https://pubmed.ncbi.nlm.nih.gov/41165871/)). IRF7 is proposed as a checkpoint for maladaptive switching, upregulated in unstable human plaques ([PMID: 41625231](https://pubmed.ncbi.nlm.nih.gov/41625231/)). Dual SMC/EC lineage tracing shows endothelial-to-SMC and SMC-loss dynamics under vascular stress ([PMID: 41648299](https://pubmed.ncbi.nlm.nih.gov/41648299/)).
- **Inflammation is causal (F011):** IL-1β→IL-6→CRP axis. Mechanistically, IL-1β induces LDL transcytosis by human coronary artery endothelial cells via an LDLR/Rab27a pathway ([PMID: 38989581](https://pubmed.ncbi.nlm.nih.gov/38989581/)), linking inflammation to early lipid entry.

### Upstream vs downstream
- **Upstream (initiation):** apoB retention, disturbed-flow endothelial dysfunction.
- **Midstream (progression):** foam cells, defective efferocytosis, SMC switching, necrotic-core growth.
- **Downstream (terminal):** cap thinning → rupture *or* endothelial erosion → thrombosis.

### GO / CL term suggestions
- GO:0019915 lipid storage; GO:0006809 nitric oxide biosynthetic process; GO:0043277 apoptotic cell clearance (efferocytosis); GO:0033344 cholesterol efflux; GO:0006954 inflammatory response.
- CL:0000359 vascular associated smooth muscle cell; CL:0000235 macrophage/foam cell; CL:0000071 blood vessel endothelial cell; CL:0000775 neutrophil (erosion).

---

## 7. Anatomical Structures Affected

- **Organ level:** Heart — specifically the **epicardial coronary arteries** (UBERON:0001621; left anterior descending, left circumflex, right coronary). Secondary organ: **myocardium** (UBERON:0002349) via ischemia/infarction. Body system: **cardiovascular system**.
- **Tissue level:** arterial **tunica intima** (UBERON:0004638; primary plaque site), tunica media (SMC source). Tissue types: endothelium, connective tissue/ECM, vascular smooth muscle.
- **Cell level:** endothelial cells (CL:0000071), monocyte-derived macrophages/foam cells (CL:0000235), vascular-associated smooth muscle cells (CL:0000359), T lymphocytes, neutrophils (prominent in erosion), platelets (terminal thrombosis).
- **Subcellular level:** lysosomes/late endosomes (lipid handling, efferocytic degradation, Rab27a vesicles, [PMID: 38989581](https://pubmed.ncbi.nlm.nih.gov/38989581/)); endoplasmic reticulum (lipid synthesis/stress); mitochondria (oxidative stress). GO CC: GO:0005764 lysosome; GO:0005783 ER.
- **Localization / lateralization:** Multifocal, bilateral (multiple coronary arteries); plaques preferentially form at **branch points and inner curvatures** where wall shear stress is low/oscillatory (F007).

---

## 8. Temporal Development

- **Onset:** Subclinical plaque begins in early adulthood (fatty streaks even earlier); clinical onset typically adult/geriatric. Onset of *events* is often **acute** superimposed on **chronic, insidious** plaque growth.
- **Progression / stages:** fatty streak → fibroatheroma → thin-cap fibroatheroma (TCFA, high-risk) → complicated/ruptured or eroded plaque with thrombosis. Progression is **variable** and modifiable; low wall shear stress accelerates lipid-rich plaque growth over ~1 year — *"Exposure to low WSS was associated with a higher plaque progression"* ([PMID: 36575921](https://pubmed.ncbi.nlm.nih.gov/36575921/)).
- **Course pattern:** chronic, lifelong, generally progressive but **regressable** with intensive LDL lowering (GLAGOV IVUS regression, F002; PACMAN-AMI lesion-level regression showing PAV change −4.86% alirocumab vs −2.78% placebo, [PMID: 39221516](https://pubmed.ncbi.nlm.nih.gov/39221516/)).
- **Natural history (F001):** In PROSPECT, most nonculprit lesions causing future events were **angiographically mild at baseline** (mean diameter stenosis 32.3±20.6%) yet had high-risk features — *"nonculprit lesions associated with recurrent events were more likely... to be characterized by a plaque burden of 70% or greater (hazard ratio, 5.03; 95% confidence interval [CI], 2.51 to 10.11; P<0.001) or a minimal luminal area of 4.0 mm(2) or less"* ([PMID: 21247313](https://pubmed.ncbi.nlm.nih.gov/21247313/)). This establishes **composition/burden, not stenosis, as the driver of events**.
- **Critical intervention windows:** LDL lowering and anti-inflammatory therapy alter trajectory at any stage; the post-MI period is a high-residual-risk window (CANTOS, colchicine).

---

## 9. Inheritance and Population

- **Epidemiology:** Ischemic heart disease is the leading global cause of death and DALYs. GBD 2021 shows rising incidence/prevalence even in young adults (aged 20–24), with ischemic heart disease dominating mortality/DALYs and males bearing greater mortality/DALY burden ([PMID: 42483021](https://pubmed.ncbi.nlm.nih.gov/42483021/)). CAC prevalence is ~50% in adults aged 45–84 (MESA, F014).
- **Inheritance:** **Polygenic/multifactorial**, not Mendelian. Heritability estimates ~40–60%. Dominant common-variant contributors: 9p21.3, LPA (F006, F010); ~300+ GWAS loci total.
- **Penetrance/expressivity:** Genetic liability is probabilistic (polygenic risk scores), strongly modified by environment (F015). Lp(a) is highly penetrant for elevated risk when very high.
- **Founder effects:** PCSK9 protective variants have population-specific frequencies (F009).
- **Population demographics / sex:** Median first-MI age higher in women (65 vs 56 yr); hypertension (OR 2.95 vs 2.32) and diabetes (OR 4.26 vs 2.67) are more strongly associated in women, while several factors are similar across sexes (F015). Low/low-middle sociodemographic-index regions bear the highest young-adult burden ([PMID: 42483021](https://pubmed.ncbi.nlm.nih.gov/42483021/)).

---

## 10. Diagnostics

- **Laboratory tests/biomarkers:** Lipid panel (LDL-C, apoB, non-HDL-C); **Lp(a)** (2024 NLA Class I recommendation for universal one-time measurement; F010); **high-sensitivity cardiac troponin** (HP:0410174) for MI; **hs-CRP** for residual inflammatory risk (CANTOS entry criterion ≥2 mg/L; F012) — *"High-sensitivity C-reactive protein is a practical and reliable biomarker for assessing low-grade chronic inflammation"* ([PMID: 41936433](https://pubmed.ncbi.nlm.nih.gov/41936433/)). Serum urate independently predicts MACE/CV death even under IL-1β blockade (HR 1.66 for MACE, [PMID: 39862678](https://pubmed.ncbi.nlm.nih.gov/39862678/)).
- **Imaging (coronary-direct, tier 1):**
  - **Coronary artery calcium (CAC) score** by non-contrast CT (Agatston method) — MESA: *"those with annual progression of ≥300 units had adjusted HRs of 3.8 (1.5 to 9.6) for total"* CHD events ([PMID: 23500326](https://pubmed.ncbi.nlm.nih.gov/23500326/)). AI-enhanced CAC scans add chamber-volume and hepatic-steatosis prognostics ([PMID: 38664073](https://pubmed.ncbi.nlm.nih.gov/38664073/), [PMID: 40221147](https://pubmed.ncbi.nlm.nih.gov/40221147/), [PMID: 41591983](https://pubmed.ncbi.nlm.nih.gov/41591983/)).
  - **Coronary CT angiography (CCTA)** — anatomy and plaque composition.
  - **Invasive intracoronary imaging:** IVUS (plaque burden/volume; GLAGOV/PROSPECT), **NIRS** (lipid-core burden), **OCT** (thin-cap fibroatheroma; the only modality able to identify **erosion in vivo**, F003).
  - Low endothelial shear stress adds incremental risk beyond morphology (HR 4.34, [PMID: 28917684](https://pubmed.ncbi.nlm.nih.gov/28917684/)).
- **Functional tests:** exercise/pharmacologic stress testing, fractional flow reserve (FFR); ECG.
- **Clinical criteria / differential diagnosis:** ACC/AHA and ESC guidelines. **Differentials to exclude** (per scope): SCAD, vasospasm, congenital anomalies, embolism, isolated microvascular dysfunction, type-2 MI.
- **Genetic/omics testing:** Not routine for common CAD; polygenic risk scores and Lp(a) are emerging risk-stratification tools. FH gene panels (LDLR/APOB/PCSK9) apply to monogenic hypercholesterolemia.
- **Screening:** CAC scoring for intermediate-risk asymptomatic adults; universal one-time Lp(a).

---

## 11. Outcome / Prognosis

- **Mortality:** Ischemic heart disease is the leading cause of death globally (GBD 2021). Acute MI and sudden cardiac death are the principal fatal outcomes.
- **Prognostic factors (coronary-direct):** plaque burden ≥70%, minimal luminal area ≤4.0 mm², and thin-cap fibroatheroma morphology independently predict nonculprit events (PROSPECT, F001); low endothelial shear stress adds risk ([PMID: 28917684](https://pubmed.ncbi.nlm.nih.gov/28917684/)); CAC progression predicts hard CHD (F014).
- **Prognostic biomarkers:** LDL-C/apoB (modifiable driver), Lp(a), hs-CRP (residual inflammatory risk), troponin, serum urate.
- **Modifiability:** Prognosis is strongly improved by LDL lowering (−21% MVE per 1 mmol/L, F013), anti-inflammatory therapy (F011/F012), and antithrombotics.
- **Complications:** MI, heart failure (predictable from CAC-derived chamber ratios, [PMID: 41591983](https://pubmed.ncbi.nlm.nih.gov/41591983/)), arrhythmia, sudden death.

---

## 12. Treatment

### Pharmacotherapy — lipid lowering (causal, LDL-dependent; MAXO:0000262 lipid-lowering agent therapy)
| Drug class | Example | Mechanism | Key evidence |
|-----------|---------|-----------|--------------|
| Statins | atorvastatin | HMG-CoA reductase inhibition | CTT: *"a 21% (RR 0.79, 95% CI 0.77-0.81) proportional reduction"* in MVE per 1 mmol/L LDL ([PMID: 30712900](https://pubmed.ncbi.nlm.nih.gov/30712900/)) |
| PCSK9 inhibitors | evolocumab, alirocumab | ↑ hepatic LDLR | GLAGOV coronary regression (F002, [PMID: 27846344](https://pubmed.ncbi.nlm.nih.gov/27846344/)); PACMAN-AMI lesion stabilization ([PMID: 39221516](https://pubmed.ncbi.nlm.nih.gov/39221516/)) |
| ACL inhibitor | bempedoic acid | inhibits ATP-citrate lyase | CLEAR: HR 0.75 per 1 mmol/L LDL, matching statins ([PMID: 38960508](https://pubmed.ncbi.nlm.nih.gov/38960508/)) |
| Ezetimibe | — | NPC1L1 inhibition | Additive LDL lowering |

Benefit **tracks the absolute magnitude of LDL-C reduction regardless of mechanism** and holds in patients ≥75 yr (RR 0.74 per 1 mmol/L; [PMID: 33186535](https://pubmed.ncbi.nlm.nih.gov/33186535/)).

### Anti-inflammatory therapy (causal, lipid-independent)
- **Canakinumab (anti-IL-1β):** CANTOS reduced events without lowering lipids — *"Canakinumab did not reduce lipid levels from baseline"* ([PMID: 28845751](https://pubmed.ncbi.nlm.nih.gov/28845751/)); total-event rate ratios ~0.78–0.80 ([PMID: 33004131](https://pubmed.ncbi.nlm.nih.gov/33004131/)).
- **Colchicine (0.5 mg/day, FDA-approved 2023):** COLCOT and LoDoCo2 reduced MACE — *"randomised colchicine trials such as COLCOT and LoDoCo2 showed reductions in major adverse cardiovascular events in patients with recent myocardial infarction and chronic coronary disease, respectively"* ([PMID: 42454467](https://pubmed.ncbi.nlm.nih.gov/42454467/)).
- **Discordant/null control:** low-dose methotrexate (CIRT) was **null** ([PMID: 23874021](https://pubmed.ncbi.nlm.nih.gov/23874021/) rationale), showing the effective axis is specifically IL-1β→IL-6→CRP, not anti-inflammation broadly (F011).

### RNA-based / emerging
- **Lp(a)-lowering:** olpasiran (siRNA, OCEAN(a), NCT05581303) and pelacarsen (ASO, Lp(a) HORIZON, NCT04023552) in outcome trials ([PMID: 42016317](https://pubmed.ncbi.nlm.nih.gov/42016317/)).

### Antithrombotic
Antiplatelet therapy (aspirin, P2Y12 inhibitors) and anticoagulation address the terminal thrombotic route (MAXO: antiplatelet therapy).

### Surgical / interventional (MAXO: percutaneous coronary intervention; coronary artery bypass grafting)
- **PCI with drug-eluting stents** and **CABG**. **Key nuance (F017):** in *stable* CAD with moderate–severe ischemia, *"an initial invasive strategy does not reduce cardiovascular mortality or myocardial infarction compared with optimized medical therapy"* ([PMID: 42099494](https://pubmed.ncbi.nlm.nih.gov/42099494/)); benefit is symptom relief (also sham-controlled ORBITA). Revascularization remains indicated for ACS, left-main, high-risk anatomy, and refractory symptoms. Chronic-total-occlusion PCI is a specialized subset with distinct procedural profiles ([PMID: 42309488](https://pubmed.ncbi.nlm.nih.gov/42309488/)).

---

## 13. Prevention

- **Primary prevention:** risk-factor modification targeting the nine INTERHEART factors (F015) — smoking cessation, lipid/apoB lowering, blood-pressure and glycemic control, weight/diet/activity. Lp(a) measurement for risk stratification.
- **Secondary prevention:** intensive LDL lowering to very low targets, anti-inflammatory therapy (colchicine) in selected post-MI/chronic coronary patients, antithrombotics, cardiac rehabilitation.
- **Tertiary prevention:** guideline-directed medical therapy to prevent recurrent events and heart failure; hs-CRP-guided identification of residual inflammatory risk.
- **Screening / risk stratification:** CAC scoring (MESA-validated, F014); polygenic risk scores (emerging); universal one-time Lp(a).
- **Behavioral / public health:** population-level tobacco control, dietary policy, physical-activity promotion — urgent in low-SDI regions with rising young-adult burden ([PMID: 42483021](https://pubmed.ncbi.nlm.nih.gov/42483021/)).
- **Not applicable:** immunization (no infectious etiology).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Naturally occurring coronary atherosclerosis with thrombosis is largely a human condition; rare in most laboratory species. Relevant orthologs in **Mus musculus (NCBI:txid10090)**: *Apoe* (Gene ID 11816), *Ldlr* (16835), *Pcsk9* (100102). **Lpa has no rodent ortholog** (F016).
- **Larger animals with true coronary lesions:** WHHL rabbit (LDLR-mutant), Ossabaw/Yucatan **pigs**, and **nonhuman primates** develop coronary atherosclerosis more analogous to humans (F016).
- **Comparative pathology:** Rodent lesions form at the aortic root/arch and brachiocephalic artery and **rarely rupture or thrombose spontaneously**, limiting fidelity to human coronary events.
- **Zoonotic potential:** none (non-infectious, non-transmissible).

---

## 15. Model Organisms

**Standard models (F016):** hyperlipidemia-driven mice — *Apoe⁻/⁻* and *Ldlr⁻/⁻* on Western/pro-atherogenic diets, and humanized **APOE*3-Leiden.CETP** (human-like lipoprotein metabolism); PCSK9-AAV overexpression induces atherogenesis without germline editing. *"APOE*3-Leiden.CETP mice, a well-established model for human-like lipoprotein metabolism"* ([PMID: 40460236](https://pubmed.ncbi.nlm.nih.gov/40460236/)).

| Model | Type | Recapitulates | Does NOT recapitulate |
|-------|------|---------------|----------------------|
| Apoe⁻/⁻ mouse | Knockout | Lipid-driven aortic plaque, foam cells | Epicardial coronary lesions; spontaneous rupture/thrombosis |
| Ldlr⁻/⁻ mouse | Knockout | Diet-responsive hypercholesterolemia + plaque | Coronary events |
| APOE*3-Leiden.CETP | Humanized transgenic | Human-like lipoproteins, plaque | Coronary thrombosis |
| Mertk-KD;Apoe⁻/⁻ | Compound mutant | Defective efferocytosis → necrotic core (F008) | Coronary localization |
| WHHL rabbit / Ossabaw pig / NHP | Spontaneous/diet | **True coronary lesions** | Cost, throughput |

**Applications:** dissecting apoB retention, foam-cell biology, efferocytosis (MerTK), SMC lineage plasticity (dual lineage tracing, [PMID: 41648299](https://pubmed.ncbi.nlm.nih.gov/41648299/)), and hemodynamic endothelial dysfunction. **Limitations:** the dominant murine models do not produce spontaneous coronary plaque rupture or MI, so terminal-route mechanisms (rupture vs erosion) are studied primarily by **human coronary OCT** in vivo (F003). Negative-control model result: PUFA-synthesis-deficient (*fads2⁻/⁻*) mice remain atherosclerosis-prone when crossed to *Apoe⁻/⁻*/*Ldlr⁻/⁻* — hypercholesterolemia dominates ([PMID: 34530175](https://pubmed.ncbi.nlm.nih.gov/34530175/)).

**Resources:** MGI, IMPC/KOMP, IMSR, Alliance of Genome Resources.

---

## Mechanistic Model / Interpretation

The synthesis across 17 findings supports a **staged, multi-arm causal model** in which **initiation, progression, stability, and acute thrombosis are distinct processes** with distinct evidence:

1. **Initiation is apoB-driven and hemodynamically localized.** Human genetics (PCSK9 LoF, F009; LPA, F010) and randomized LDL-lowering (F013, F002) establish apoB/LDL causality at the highest tier; direct human coronary imaging (F007) shows low wall shear stress plus lipid content accelerates coronary plaque growth. These converge on a strong causal edge: **apoB retention + disturbed flow → coronary plaque**.

2. **Progression is governed by cellular handling of lipid and dead cells.** Defective **MerTK efferocytosis** (mouse, F008) and **oxLDL-driven foam-cell formation** (in vitro, F008) expand the necrotic core; **SMC-to-macrophage-like transdifferentiation** (mouse/human, F004) thins the fibrous cap. These are mechanistically compelling but **anatomically indirect** (mouse aorta, cultured cells) — they explain *how* human coronary composition arises without proving coronary causality alone.

3. **Inflammation is an independent causal arm.** CANTOS (F011) and colchicine trials (F012) reduce human coronary events *without* lipid change, while the null CIRT/methotrexate result isolates the **IL-1β→IL-6→CRP** axis. IL-1β can also feed back on initiation by inducing coronary-endothelial LDL transcytosis (in vitro/mouse, [PMID: 38989581](https://pubmed.ncbi.nlm.nih.gov/38989581/)).

4. **Terminal events are composition-, not stenosis-, dependent, with two routes.** PROSPECT (F001) shows angiographically mild lesions cause future events when plaque burden/necrotic-core/thin-cap features are present; human coronary OCT (F003) resolves **rupture (~2/3)** vs **erosion (~1/3)** as biologically distinct triggers of thrombosis.

5. **Therapeutic corollary:** because stenosis is not the driver of hard events, **revascularization relieves symptoms but does not reduce death/MI in stable CAD** (ISCHEMIA, F017), whereas systemic apoB lowering and anti-inflammation modify the biology and reduce events.

### Terminal-route detail: rupture vs erosion

| Feature | Rupture | Erosion |
|---|---|---|
| Cap | Thin (<65 µm), disrupted | Intact |
| Necrotic core | Large | Small/absent |
| Inflammation | Macrophage-rich | Less; neutrophil/NET-linked |
| Matrix | Lipid | Proteoglycan/SMC/hyaluronan |
| Thrombus | Often occlusive | Often mural/less occlusive |
| Frequency in ACS | ~2/3 | ~1/3 |
| Evidence | T1 OCT/pathology ([PMID: 29332908](https://pubmed.ncbi.nlm.nih.gov/29332908/), [PMID: 24631511](https://pubmed.ncbi.nlm.nih.gov/24631511/)) | T1 OCT; weaker mechanism |

### Genuine competing hypotheses
- **"Response-to-retention" (apoB-centric) vs "inflammation-primary":** the evidence supports these as **complementary, both causal** arms. Best synthesis: apoB is the initiating cause; inflammation is a required amplifier (Lp(a) mediates only 1.3–4.8% of the IL-6→ASCVD effect, [PMID: 41932221](https://pubmed.ncbi.nlm.nih.gov/41932221/), arguing for independence).
- **Rupture-dominant vs erosion-inclusive paradigm:** OCT data force inclusion of erosion as a mechanistically separate, potentially antithrombotic-manageable route.
- **Macrophage origin:** whether lesional "macrophages" are monocyte- vs SMC-derived (F004) remains partly unresolved and matters for target selection.

---

## Evidence Base (Key Literature)

| PMID | Role | Contribution |
|------|------|--------------|
| [16554528](https://pubmed.ncbi.nlm.nih.gov/16554528/) | Supports | PCSK9 LoF → 88%/47% lower CHD (LDL causality) |
| [27846344](https://pubmed.ncbi.nlm.nih.gov/27846344/) | Supports | GLAGOV: PCSK9i regresses coronary atheroma (IVUS) |
| [30712900](https://pubmed.ncbi.nlm.nih.gov/30712900/) | Supports | CTT: −21% MVE per 1 mmol/L LDL |
| [28845751](https://pubmed.ncbi.nlm.nih.gov/28845751/) | Supports | CANTOS: IL-1β inhibition, lipid-independent event reduction |
| [42454467](https://pubmed.ncbi.nlm.nih.gov/42454467/) | Supports | Colchicine (COLCOT/LoDoCo2) reduces MACE |
| [21247313](https://pubmed.ncbi.nlm.nih.gov/21247313/) | Supports | PROSPECT: composition > stenosis (coronary-direct) |
| [36575921](https://pubmed.ncbi.nlm.nih.gov/36575921/) | Supports | Low WSS + lipid → coronary plaque growth (coronary-direct) |
| [29332908](https://pubmed.ncbi.nlm.nih.gov/29332908/) | Supports | Rupture vs erosion terminal routes (coronary OCT) |
| [23500326](https://pubmed.ncbi.nlm.nih.gov/23500326/) | Supports | MESA: CAC progression predicts CHD |
| [18334475](https://pubmed.ncbi.nlm.nih.gov/18334475/) | Supports | INTERHEART: 9 factors = >90% MI PAR |
| [37197843](https://pubmed.ncbi.nlm.nih.gov/37197843/) | Supports | CHIP → ASCVD risk |
| [18451332](https://pubmed.ncbi.nlm.nih.gov/18451332/) | Supports (model) | MerTK efferocytosis failure → necrosis (mouse) |
| [41165871](https://pubmed.ncbi.nlm.nih.gov/41165871/) | Supports | SMC-derived macrophage-like cells destabilize plaque |
| [42099494](https://pubmed.ncbi.nlm.nih.gov/42099494/) | Supports (null) | ISCHEMIA: revascularization no death/MI benefit in stable CAD |
| [41932221](https://pubmed.ncbi.nlm.nih.gov/41932221/) | Challenges/constrains | Lp(a) mediates only 1.3–4.8% of IL-6→ASCVD (independence) |
| [34530175](https://pubmed.ncbi.nlm.nih.gov/34530175/) | Constrains (model) | Hypercholesterolemia dominates over PUFA effects |

---

## Suggested Ontology Terms

| Domain | Term | ID |
|---|---|---|
| Disease (anchor) | coronary atherosclerosis | **MONDO:0021661** |
| Disease (complication) | myocardial infarction | MONDO:0005068 |
| Cell | vascular associated smooth muscle cell | **CL:0000359** |
| Cell | macrophage / foam cell | CL:0000235 |
| Cell | blood vessel endothelial cell | CL:0000071 |
| Process | lipid storage (foam cell) | **GO:0019915** |
| Process | nitric oxide biosynthetic process | **GO:0006809** |
| Process | cholesterol efflux | GO:0033344 |
| Process | apoptotic cell clearance (efferocytosis) | GO:0043277 |
| Anatomy | coronary artery | UBERON:0001621 |
| Anatomy | tunica intima | UBERON:0004638 |
| Chemistry | low-density lipoprotein particle | CHEBI:39026 |
| Chemistry | cholesterol | CHEBI:16113 |
| Phenotype (HPO) | Coronary artery atherosclerosis | HP:0001677 |
| Phenotype (HPO) | Myocardial infarction | HP:0001658 |
| Phenotype (HPO) | Angina pectoris | HP:0001681 |
| Procedure (MAXO) | Lipid-lowering agent therapy | MAXO:0000262 |

---

## Limitations and Knowledge Gaps

1. **Vascular-bed indirectness.** Much mechanistic detail (efferocytosis, SMC switching, shear-endothelial signaling) derives from **mouse aorta or cultured cells**, not epicardial coronary tissue. Per the scope guardrails, carotid/aortic human plaque and mouse-carotid disturbed-flow work (e.g., PMID:38639096, PMID:40594772) remain **transferable atherosclerosis evidence only**, not human coronary evidence.
2. **Imaging surrogates ≠ cellular mechanism.** IVUS/OCT/NIRS/CAC quantify composition and predict events but do not prove a specific cellular mediator; GLAGOV/PACMAN show plaque regression, not a demonstrated causal cell type.
3. **Erosion biology underexplored.** The ~1/3 of ACS due to erosion has fewer mechanistic and therapeutic data than rupture; targeted therapy is nascent.
4. **Model fidelity.** Dominant murine models lack spontaneous coronary rupture/thrombosis (F016); terminal-route mechanisms rest primarily on human in-vivo OCT and pathology.
5. **CHIP and SMC-origin questions.** Causality in humans for CHIP is association + mouse mechanism; the monocyte- vs SMC-derived macrophage question (F004) is unresolved.
6. **Residual risk.** Even with excellent LDL control, events persist (motivating Lp(a) and inflammation targeting); the full mediator set of residual risk is incompletely defined.
7. **Citation caveat.** One snippet (PMID:30482443) flagged a quote-validation mismatch and should be re-verified before KB ingestion.

---

## Proposed Follow-up Experiments / Actions

1. **Coronary-specific causal localization:** apply spatial transcriptomics and genetic-lineage inference to **human epicardial coronary plaques** (not carotid/aortic surrogates) to test whether SMC-to-macrophage transitions and IRF7 activity localize to coronary rupture/erosion sites.
2. **Erosion-directed intervention trial:** OCT-guided randomization of antithrombotic-only vs stenting in confirmed erosion (extending EROSION-concept designs) with hard endpoints.
3. **Lp(a)-lowering outcome readout:** analyze OCEAN(a) (olpasiran) and Lp(a) HORIZON (pelacarsen) to test whether genetically causal Lp(a) reduction reduces coronary events, with plaque-composition endpoints.
4. **Inflammation × lipid factorial trials:** test IL-6-pathway inhibition (e.g., ziltivekimab) plus intensive LDL lowering to quantify additive coronary benefit, exploiting the demonstrated independence of the two arms ([PMID: 41932221](https://pubmed.ncbi.nlm.nih.gov/41932221/)).
5. **Efferocytosis restoration:** test pro-efferocytic agents (MerTK-stabilizing or CD47-axis modulators) in large-animal coronary models (pig/NHP) with necrotic-core imaging endpoints.
6. **CHIP-stratified anti-inflammatory therapy:** prospectively test whether TET2/DNMT3A CHIP carriers derive enhanced benefit from IL-1β/IL-6 inhibition.
7. **CAC/AI imaging integration:** validate AI-derived CAC-scan biomarkers (chamber ratios, hepatic steatosis) for coronary + heart-failure risk in prospective trials.

---

### Bottom line
Coronary atherosclerosis (`MONDO:0021661`) is an apoB-initiated, shear-patterned, inflammation-amplified intimal disease whose **composition — not stenosis —** governs acute risk through **two distinct terminal routes (rupture and erosion)**. The causal backbone (apoB via PCSK9/LPA genetics and LDL trials; IL-1β/IL-6 via CANTOS/colchicine) is proven in humans, while the cellular mechanism (SMC switching, efferocytosis, foam-cell biology) is robustly established in models/carotid tissue and awaits coronary-localized confirmation.

*Report scope locked to `MONDO:0021661` coronary atherosclerosis. Evidence tiers, vascular beds, and null/discordant results are stated explicitly per the issue-specific guardrails; reviews were treated as orientation and primary studies anchor each claim.*


## Artifacts

- [OpenScientist final report](Coronary_Artery_Disease-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](Coronary_Artery_Disease-deep-research-openscientist_artifacts/final_report.pdf)

---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-09T19:45:39.738113'
end_time: '2026-08-09T19:50:57.162190'
duration_seconds: 317.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Eisenmenger Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 25
  num_turns: 31
  total_cost_usd: 2.2691850000000002
  session_id: ccd9973f-d61b-50a6-8cfe-0a77b122d0f2
  stop_reason: end_turn
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Eisenmenger Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Eisenmenger Syndrome** covering all of the
disease characteristics listed below. This report will be used to populate a disease knowledge
base entry. Be thorough and cite primary literature (PMID preferred) for all claims.

For each section, **suggested databases/resources** are listed. These are the first places
you should search for information on each topic.

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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Eisenmenger Syndrome: Comprehensive Research Report

## 1. Disease Information

**Overview.** Eisenmenger syndrome (ES) is the most advanced form of pulmonary arterial hypertension associated with congenital heart disease (PAH-CHD). It describes the end-stage physiology that develops when a large, long-standing, unrestricted communication between the systemic and pulmonary circulations (at the aortopulmonary, ventricular, or atrial level) produces chronic high-flow/high-pressure exposure of the pulmonary vasculature, driving progressive pulmonary vascular remodeling, severe pulmonary vascular resistance (PVR) elevation, and eventual **reversal of the shunt from left-to-right to right-to-left (or bidirectional)**, producing chronic systemic hypoxemia and cyanosis. First described by Paul Wood in 1958, ES is defined operationally as "pulmonary hypertension due to a high pulmonary vascular resistance with reversed or bidirectional shunt" occurring in the presence of a non-restrictive aortopulmonary, ventricular, or atrial communication (Banerjee & Opotowsky, 2024, PMID:39711759).

**Key identifiers:**
- **MONDO:** MONDO:0019944 (Eisenmenger syndrome/complex)
- **Orphanet:** ORPHA:97214
- **ICD-10-CM:** I27.83 (Eisenmenger's syndrome — pulmonary heart disease; code also the underlying defect, e.g., Q21.8 "Eisenmenger's defect," or the specific septal defect code)
- **MeSH:** D004466 (Eisenmenger Complex)
- **NCIT candidate treatment-action anchor:** NCIT:C15986 (Pharmacotherapy), NCIT:C15329 (Surgical Procedure) — for downstream annotation of PAH-targeted drugs and transplantation

**Synonyms/alternative names:** Eisenmenger complex; Eisenmenger reaction; Eisenmenger physiology; pulmonary hypertension due to congenital systemic-to-pulmonary shunt with reversed/bidirectional shunt.

**Nature of evidence base:** Because ES is a rare, heterogeneous, acquired physiologic end-state of multiple distinct congenital cardiac lesions (rather than a single monogenic disorder), the literature is predominantly **aggregated disease-level and cohort-level clinical evidence** — multicenter and single-center adult congenital heart disease (ACHD) registries (e.g., the Euro Heart Survey, UK/Royal Brompton cohorts, COMPERA-CHD), randomized controlled trials of PAH-targeted therapy (e.g., BREATHE-5, EIGER, the bosentan-sildenafil combination RCT), and case series/case reports for rarer complications (pregnancy, transplantation). There is essentially no individual-patient EHR-derived "N-of-1" data source specific to ES as such; genetic data (e.g., BMPR2 mutation carriage) come from smaller mechanistic/candidate-gene cohorts nested within PAH-CHD research rather than population biobanks.

---

## 2. Etiology

### 2a. Disease Causal Factors (mechanistic/anatomic)
ES is not itself a primary genetic disease but the **pathophysiological consequence of an untreated congenital systemic-to-pulmonary shunt**. The causal chain is:
1. A non-restrictive congenital cardiac communication (VSD, ASD, AVSD, PDA, truncus arteriosus, or a complex/univentricular lesion with unobstructed pulmonary flow) permits chronic left-to-right shunting.
2. Persistently elevated pulmonary blood flow and/or pressure produces **shear-stress-mediated pulmonary endothelial dysfunction**, triggering progressive pulmonary vascular remodeling (vasoconstriction → medial hypertrophy → intimal proliferation/fibrosis → in situ thrombosis → plexiform arteriopathy).
3. Rising PVR eventually equals or exceeds systemic vascular resistance, reversing (or making bidirectional) the shunt — the defining moment of "Eisenmenger physiology" — producing chronic hypoxemia/cyanosis (PMC11658362, PMID:39711759; StatPearls NBK507800).

**Lesion-specific risk of progression to ES** (StatPearls; JACC 2008 review, PMID:19245962):
- Truncus arteriosus: nearly all unrepaired cases progress
- Large unrepaired VSD: ~50% (aortopulmonary or ventricular-level shunts overall 52–53% in Euro Heart Survey data)
- Large unrepaired PDA: substantial risk, especially with continuous high-pressure exposure
- Large unrepaired ASD: only ~9–10% (because pressure, not just flow, is transmitted less directly at the atrial level) — this lower-penetrance group is where a **genetic susceptibility factor (e.g., BMPR2)** is thought to matter most, since hemodynamic stress alone is often insufficient (ScienceDirect, PMID:27002414).

### 2b. Risk Factors

**Genetic risk factors:**
- **BMPR2 mutations** — heterozygous loss-of-function variants in the TGF-β/BMP type II receptor gene, the classic cause of heritable/idiopathic PAH, are also found at increased rate in PAH-CHD/Eisenmenger cohorts. One cohort found a **12.6% BMPR2 mutation rate in "repaired" CHD-associated pulmonary vascular disease patients** (i.e., those who develop PAH despite/after defect closure), with missense variants predominating and a higher detection rate in females and repaired patients (Zhu et al., PMID:27002414). BMPR2 is proposed as "a potential predisposing genetic risk factor" that lowers the threshold for hemodynamic-stress-induced pulmonary vascular disease, but the relationship is not absolute — ASD-associated Eisenmenger physiology can occur without any detectable BMPR2 mutation, implying other genetic contributors (PMID:17102831).
- Other BMP/TGF-β pathway genes implicated in PAH broadly (and plausibly relevant modifiers in PAH-CHD): **ACVRL1/ALK1, ENG (endoglin), SMAD1, SMAD4, SMAD9, SMAD5, SOX17** — variants (including de novo changes) have been reported in APAH-CHD cohorts (Springer Pediatric Cardiology review, 2025).
- **Trisomy 21 (Down syndrome, HGNC gene dosage effect, not single-gene)** — a well-established genetic factor that **accelerates** progression to pulmonary vascular obstructive disease/Eisenmenger physiology independent of lesion type, historically producing ES at much younger ages and higher rates when surgery was delayed (PMID:27325590).
- Standard clinical genetic screening for suspected heritable PAH contribution focuses on sequencing **BMPR2, ALK1 (ACVRL1), Endoglin (ENG), and SMAD9**.

**Environmental/clinical risk factors:**
- **Delayed or absent surgical repair** of the underlying shunt lesion — the single largest modifiable risk factor. Repair within the first ~2 years of life largely prevents ES.
- **Post-tricuspid (ventricular-level or great-vessel-level) shunt location** vs. pre-tricuspid (atrial-level) — post-tricuspid shunts transmit pressure directly to the pulmonary circuit and confer much higher ES risk.
- **Limited access to healthcare/diagnostic services** — geographic/socioeconomic disparity is a major real-world driver; ES is now largely a disease of resource-limited settings, since early detection and closure have reduced its prevalence by ~50% over 50 years in the developed world (PMID:28566473).
- **High altitude residence** — chronic hypoxic pulmonary vasoconstriction is understood to exacerbate pulmonary vascular disease progression (cited as an aggravating/avoidance factor in management guidance; StatPearls NBK507800).
- Female sex and repaired-CHD status correlate with higher detected BMPR2 mutation rates in the cited cohort, suggesting a possible sex-genetic interaction, though data are limited.

### 2c. Protective Factors
- **Early corrective/palliative cardiac surgery** (within the first 1–2 years of life) is the dominant protective intervention and has driven the measured decline in ES incidence in high-resource countries.
- Improved perinatal/pediatric screening (prenatal echocardiography, newborn pulse-oximetry screening) enabling earlier defect detection.
- No specific protective genetic variant has been characterized for ES to date (unlike some diseases with described protective alleles); this remains an evidence gap.

### 2d. Gene-Environment Interactions
The clearest documented gene-environment interaction is that **hemodynamic stress (the "environmental"/mechanical exposure of chronic shunt flow) is necessary but not sufficient** to cause severe irreversible pulmonary vascular disease in many patients — a genetic susceptibility factor (BMPR2 or other BMP-pathway variant) appears to lower the flow/pressure threshold required to trigger irreversible remodeling, explaining why only a minority of patients with a given anatomic lesion (e.g., ~9–53% depending on lesion type) progress to ES despite similar shunt anatomy (PMID:27002414, PMID:17102831). Down syndrome (a genetic dosage state) similarly interacts with shunt-lesion "exposure" to accelerate the same final pathway.

---

## 3. Phenotypes

### Symptoms / Clinical Signs (HP-mappable)

| Phenotype | Suggested HPO term | Frequency/notes |
|---|---|---|
| Exertional dyspnea | HP:0002875 (Exertional dyspnea) | Most frequent presenting symptom |
| Central cyanosis | HP:0007204 (Central cyanosis) / HP:0000961 (Cyanosis) | Cardinal, progressive feature; onset usually childhood–young adulthood as shunt reverses |
| Digital clubbing | HP:0100759 (Nail clubbing) | Common, more pronounced in lower extremities with PDA-associated ES ("differential clubbing/cyanosis") |
| Syncope | HP:0001279 (Syncope) | Poor prognostic marker at presentation |
| Palpitations | HP:0001962 (Palpitations) | Reflects atrial/ventricular arrhythmia |
| Hemoptysis | HP:0002105 (Hemoptysis) | From pulmonary infarction, vessel rupture, or coagulopathy; historically a leading cause of death, now 5th most common (post-DTT era) |
| Fatigue/lethargy | HP:0012378 (Fatigue) | Nonspecific but near-universal |
| Chest pain | HP:0100749 (Chest pain) | Can reflect pulmonary infarction or ischemia |
| Right heart failure signs (edema, ascites, hepatomegaly) | HP:0000969 (Edema), HP:0001541 (Ascites), HP:0002240 (Hepatomegaly) | Progressive/late-stage; leading contemporary cause of death |
| Headache/dizziness/visual changes (hyperviscosity) | HP:0002315 (Headache), HP:0002321 (Vertigo) | From secondary erythrocytosis/hyperviscosity |
| Gout | HP:0002804 (Joint hyperflexibility — not exact; better: HP:0001997 Gout) | From hyperuricemia (increased RBC turnover) |
| Cholelithiasis | HP:0001081 (Cholelithiasis) | From chronic hyperbilirubinemia (hemolysis/RBC turnover) |
| Hypertrophic osteoarthropathy | HP:0040217 (Hypertrophic pulmonary osteoarthropathy candidate) | Associated with chronic cyanosis |
| Stroke/TIA | HP:0001297 (Stroke) | Paradoxical embolism or thrombotic; cerebral abscess also reported |
| Brain abscess | HP:0100738 (Brain abscess) | From right-to-left shunt bypassing pulmonary filtration of septic emboli |
| Nephropathy/proteinuria | HP:0000093 (Proteinuria) | Reported in up to 30% (proteinuria) / ~60% (albuminuria) of cyanotic patients |

### Onset, Severity, Progression, Frequency
- **Age of onset:** Highly lesion-dependent. Post-tricuspid shunts (large VSD, PDA, truncus arteriosus, AVSD, especially with trisomy 21) can progress to irreversible pulmonary vascular disease and shunt reversal in **infancy to early childhood**; pre-tricuspid shunts (ASD) typically manifest ES only in the **third or fourth decade of life** or later.
- **Severity/progression:** Progressive and generally irreversible once established; three histopathologic stages of the underlying vasculopathy (vasoconstriction → remodeling → thrombosis) parallel worsening clinical severity, culminating in NYHA functional class decline, right heart failure, and death. Overall disease course is chronic and progressive, though the rate varies widely by underlying lesion complexity.
- **Frequency among CHD patients:** ~8% of all congenital heart disease patients develop ES; historically 17.5% (Wood, 1958) versus 1–5.7% in contemporary high-resource registries (e.g., 5.7% of 4,110 adults in the Euro Heart Survey), reflecting the impact of early surgical repair (PMID:39711759; PMID:28566473).

### Quality of Life
Quality of life is markedly and disproportionately impaired compared with other cyanotic CHD groups: exercise performance and QoL are **more impaired in ES than in complex cyanotic CHD with pulmonary stenosis** (PMID:20439122), with peak oxygen uptake reduced ~45% and ventilatory equivalent for CO₂ ~70% higher than healthy controls. Most patients function in NYHA/WHO functional class II–III. PAH-targeted drug therapy (e.g., sildenafil) has been shown to significantly improve QoL and functional class in randomized and observational studies (PMID:20304507).

---

## 4. Genetic/Molecular Information

**Causal genes (susceptibility, not strictly Mendelian-causal for the syndrome itself):**
- **BMPR2** (HGNC:1078; OMIM 600799) — bone morphogenetic protein receptor type 2; loss-of-function/missense variants; the canonical heritable-PAH gene, also implicated as a susceptibility modifier in PAH-CHD/ES (PMID:27002414).
- **ACVRL1/ALK1** (HGNC:175) and **ENG** (HGNC:3349) — activin receptor-like kinase 1 and endoglin, both BMP9/10 co-receptor components; classically hereditary hemorrhagic telangiectasia genes, also linked to PAH.
- **SMAD1, SMAD4, SMAD5, SMAD9** (downstream BMP-pathway transcription factors) — variants reported in APAH-CHD, including de novo changes.
- **SOX17** — increasingly recognized PAH-CHD-associated gene.

**Variant classification/type:** Predominantly missense (dominant, likely haploinsufficiency mechanism for BMPR2); variant pathogenicity should be interpreted per ACMG/AMP criteria via ClinVar/ClinGen. Functional consequence is generally **loss of function** in the BMP/TGF-β signaling receptor complex, disinhibiting proliferative/anti-apoptotic signaling in pulmonary vascular smooth muscle and endothelium.

**Population frequency:** Rare variants; population allele frequency data should be checked against gnomAD for any specific variant before curation (no ES-specific germline founder variant has been established).

**Somatic vs. germline:** Germline (constitutional) — these are inherited/de novo susceptibility alleles, not somatic mutations.

**Chromosomal abnormality:** **Trisomy 21 (Down syndrome)** is the principal chromosomal risk factor, present in a substantial minority of ES patients with AVSD/VSD, and independently associated with accelerated pulmonary vascular disease.

**Epigenetics:** No ES-specific DNA methylation/histone signature has been well characterized in the literature reviewed; this is a knowledge gap. (Broader PAH literature does describe epigenetic dysregulation, e.g., of BMPR2 and HIF pathways, but ES-specific data are sparse — flag as `KNOWLEDGE_GAP` if curating.)

**Suggested gene/ontology annotations:**
- Gene: `hgnc:1078` (BMPR2), `hgnc:175` (ACVRL1), `hgnc:3349` (ENG), `hgnc:11177` (SMAD9)
- GO biological process: GO:0030510 (regulation of BMP signaling pathway), GO:0001525 (angiogenesis), GO:0003085 (negative regulation of systemic arterial blood pressure — context-dependent)

---

## 5. Environmental Information

- **Environmental/exposure factors:** No toxin, pollutant, or occupational exposure is established as causal for ES; the "environmental" driver is fundamentally **mechanical/hemodynamic** (chronic high pulmonary flow/pressure from the unrepaired shunt) rather than a chemical or infectious agent.
- **Lifestyle factors relevant to management (not causation):** Dehydration, isometric exercise, high-altitude exposure, and iron deficiency are all specifically flagged in clinical guidance as conditions to **avoid** because they exacerbate hyperviscosity/hypoxemia physiology in established ES (StatPearls NBK507800). Suggested ECTO terms would apply to "exposure to high altitude" as an exacerbating (not causal) factor.
- **Infectious agents:** Not causal, but **infective endocarditis** is a major secondary complication given the intracardiac shunt and turbulent flow, with risk of septic paradoxical embolization to the brain (abscess) or systemic circulation because right-to-left shunting bypasses the normal pulmonary filtration of septic emboli.

---

## 6. Mechanism / Pathophysiology

### Causal chain (upstream → downstream)
1. **Trigger (MOLECULAR/TISSUE scale):** Chronic elevated pulmonary blood flow and/or pressure from a non-restrictive systemic-to-pulmonary shunt imposes abnormal **shear stress on the pulmonary vascular endothelium**.
2. **Endothelial dysfunction (MOLECULAR/CELLULAR):** Dysfunctional pulmonary-artery endothelial cells show decreased production of **prostacyclin (PGI2)** and **endogenous nitric oxide (via eNOS dysfunction)**, together with increased **endothelin-1 (ET-1)** production — an imbalance that favors vasoconstriction and smooth-muscle proliferation. Elevated **thromboxane A2**, platelet activation, and increased intrinsic elastase and **vascular endothelial growth factor (VEGF)** production further drive pathological remodeling (JACC 2008 review PMID:19245962; PMC11658362).
3. **Vascular remodeling (TISSUE):** Progressive structural changes follow the classic **Heath-Edwards histopathological grading** (1958):
   - Grade I: medial hypertrophy of small muscular arteries/arterioles
   - Grade II: + intimal cellular proliferation (smooth muscle migration to subendothelium)
   - Grade III: + advanced medial thickening, progressive intimal fibrosis, arteriolar obliteration
   - Grade IV: **plexiform lesions** — focal proliferation of endothelial-lined channels within dilated arterial segments
   - Grade V: complex plexiform, angiomatous, and cavernous lesions with hyalinizing intimal fibrosis
4. **Hemodynamic consequence (ORGANISM):** Rising pulmonary vascular resistance eventually equals/exceeds systemic vascular resistance, **reversing the shunt** from left-to-right to bidirectional/right-to-left — the defining Eisenmenger transition — producing chronic arterial hypoxemia.
5. **Systemic downstream consequences (ORGANISM):** Chronic hypoxemia triggers **secondary/compensatory erythrocytosis** (renal erythropoietin-driven), which can be blunted by iron deficiency; **hyperviscosity** with thrombotic/hemorrhagic diathesis; multiorgan effects including renal dysfunction (proteinuria/albuminuria, reduced GFR), gout (hyperuricemia from increased cell turnover), cholelithiasis (hyperbilirubinemia), hypertrophic osteoarthropathy, and neurologic events (paradoxical embolism, cerebral abscess, hemorrhagic/ischemic stroke).
6. **Cardiac remodeling and arrhythmia (TISSUE/ORGANISM):** Chronic right ventricular pressure/volume overload leads to right heart failure over time; atrial arrhythmias (notably **atrial fibrillation**, conferring an ~11.45-fold increased sudden cardiac death risk in multivariate analysis), conduction disease, and ventricular arrhythmia contribute to sudden cardiac death — the second/third leading cause of mortality in the contemporary era (AHA/JAHA PMID via PMC7335528).

### Cell types and biological processes involved
- **Pulmonary artery endothelial cells** (CL:0002544 or general endothelial cell CL:0000115) — dysfunction is the initiating cellular lesion.
- **Pulmonary artery vascular smooth muscle cells** (CL:0000359) — undergo hyperplasia/hypertrophy and migration into the intima.
- **Platelets** — activation contributes to in situ thrombosis and to the bleeding/thrombosis diathesis.
- **Renal cells (erythropoietin-producing interstitial fibroblasts)** — drive compensatory erythropoiesis.
- Relevant GO biological processes: GO:0001525 (angiogenesis), GO:0043615 (astrocyte cell migration — not relevant), better: GO:0090023 (positive regulation of neutrophil chemotaxis — not relevant); most relevant: **GO:0001974** (blood vessel remodeling), **GO:0043491** (protein kinase B signaling — pathway adjacent), **GO:0007179** (TGF-beta receptor signaling pathway, given BMPR2/ALK1 involvement), **GO:0038063** (T cell extravasation — not relevant). Core recommended terms: GO:0001974 (blood vessel remodeling), GO:0007179 (transforming growth factor beta receptor signaling pathway), GO:0001525 (angiogenesis).

### Suggested downstream/module conformance
This pathophysiology is closely analogous to the dismech `pulmonary_vascular_remodeling` module (HP:0002092, obstructive pulmonary vascular remodeling driving PAH with RV overload) and shares upstream endothelial-dysfunction biology with the general vascular-remodeling literature; ES-specific curation should model it as a CHD-triggered variant of that chain, with the shunt-reversal node as the key discriminating causal step versus idiopathic/heritable PAH.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Heart (all chambers, especially right ventricle and atria) and pulmonary arterial vasculature (UBERON:0002012 pulmonary artery; UBERON:0000948 heart)
- **Secondary/systemic:** Kidneys (proteinuria, reduced GFR), liver/biliary tree (cholelithiasis from hyperbilirubinemia), joints (gout), bone/periosteum (hypertrophic osteoarthropathy), central nervous system (stroke, brain abscess), skin (plethora, acrocyanosis, livedo reticularis, ischemic ulceration), bone marrow (erythroid hyperplasia).
- **Body systems:** Cardiovascular (primary), respiratory, renal, hepatobiliary, musculoskeletal, hematologic, neurologic.

**Tissue/cell level:**
- Pulmonary arterial media, intima, and adventitia (site of Heath-Edwards remodeling grades I–V)
- Right ventricular myocardium (hypertrophy/fibrosis from chronic pressure overload)
- Bone marrow erythroid precursors (erythrocytosis)

**Subcellular level (GO Cellular Component):**
- Endothelial cell plasma membrane (site of eNOS, ET-1 receptor signaling)
- Mitochondria (implicated ROS accumulation contributing to endothelial dysfunction)

**Localization:** Bilateral, diffuse pulmonary vascular involvement (not lateralized); underlying cardiac defect location varies (septal — ventricular/atrial — vs. great vessel level for PDA/truncus arteriosus).

---

## 8. Temporal Development

- **Onset pattern:** Insidious and progressive, beginning with an asymptomatic left-to-right shunt phase in infancy, transitioning through a variable latency period to shunt reversal. Onset of overt cyanosis/ES physiology ranges from **infancy (post-tricuspid, high-pressure lesions, especially with trisomy 21)** to the **third or fourth decade (pre-tricuspid ASD-type lesions)**.
- **Stages:** (1) Left-to-right shunt with normal/mildly elevated PVR; (2) progressive pulmonary vascular remodeling with rising PVR (potentially still surgically correctable "window" period); (3) fixed elevated PVR with bidirectional shunting (transitional); (4) established Eisenmenger physiology with right-to-left shunting and cyanosis (surgical correction now contraindicated).
- **Progression rate:** Variable — lesion type and presence of accelerating factors (trisomy 21, larger defect, genetic susceptibility) determine rate; once ES is established, disease is chronic and progressive with intermittent stability punctuated by complications (arrhythmia, hemoptysis, heart failure decompensation).
- **Critical period for intervention:** Cardiac repair in the **first 2 years of life** is the key window to prevent ES; beyond a certain threshold of fixed pulmonary vascular disease, defect closure becomes contraindicated because removing the "pop-off" right-to-left shunt in the face of severe fixed PVR precipitates acute right heart failure.
- **Remission:** No spontaneous remission described; "treat and repair" (aggressive PAH-targeted therapy followed by defect closure in selected reversible cases) shows good short/medium-term outcomes in case series but lacks long-term outcome data and cannot yet be systematically recommended (PMID:39711759).

---

## 9. Inheritance and Population

**Epidemiology:**
- ~8% of all CHD patients develop ES overall; historically 17.5% (Wood 1958 cohort) vs. 1–5.7% contemporary (Euro Heart Survey: 5.7% of 4,110 adults).
- **Orphanet prevalence estimate:** 1–9 per 1,000,000 (ultra-rare).
- By lesion: 52–53% of large aortopulmonary/ventricular-level shunts progress to ES vs. only ~9–10% of large atrial-level shunts.
- Prevalence has **declined ~50% over the past 50 years** in developed countries due to early surgical repair (PMID:28566473), while remaining a larger relative burden in resource-limited regions with delayed diagnosis/access to cardiac surgery (e.g., a Yunnan, China pediatric CHD cohort study, PMID:35522268).

**Inheritance pattern:** ES itself is **not a single-gene Mendelian disorder** — it is an acquired physiologic consequence of an underlying (usually sporadic) congenital cardiac malformation, modified by susceptibility genetics (BMPR2 and related BMP-pathway variants, generally autosomal dominant with incomplete penetrance when causal for heritable PAH) and by chromosomal factors (trisomy 21).
- **Penetrance:** Incomplete for BMPR2-type susceptibility variants — most CHD patients with a given lesion do NOT develop ES even without repair, implying gene-environment/dose interaction.
- **Founder effects / consanguinity / carrier frequency:** Not well established specific to ES; the underlying CHD lesions themselves (e.g., AVSD in trisomy 21) have their own population genetics.

**Population demographics:**
- **Sex ratio:** Reported as approximately equal (males and females equally affected), per NORD/GARD summaries, though BMPR2 mutation detection rate was higher in females in one cohort (PMID:27002414) and pregnancy-specific complications obviously affect female patients disproportionately in clinical impact.
- **Geographic distribution:** Disproportionately represents populations with limited access to pediatric cardiac surgery — a "disease of health system gaps" in the modern era.
- **Age distribution:** Adult survivors span young adulthood through middle age; median survival substantially reduced relative to the general population (see Section 11).

---

## 10. Diagnostics

**Clinical/initial workup:**
- History and physical exam (cyanosis, clubbing, signs of right heart failure); note that **loud murmurs may be absent** because equalized right/left ventricular pressures minimize turbulent flow across the shunt — an important diagnostic pitfall (StatPearls NBK507800).
- Pulse oximetry (resting and with exercise)
- Chest radiograph, ECG, pulmonary function tests
- Complete blood count and iron studies (to characterize secondary erythrocytosis and iron status)
- Renal function, uric acid (annual monitoring recommended)
- BNP/NT-proBNP (validated prognostic biomarker, more reliable than echocardiographic RVEF alone for prognosis; PMC5841908)

**Imaging:**
- **Echocardiography** is the mainstay noninvasive tool: depicts the underlying anatomic lesion, shunt site/direction (color Doppler demonstrating right-to-left or bidirectional flow), pulmonary artery pressure estimation, right heart size/function (e.g., TAPSE <15 mm associated with adverse outcomes).
- **Cardiac MRI**: assesses RV size/function and myocardial fibrosis — native T1/extracellular volume (ECV) mapping; an **ECV threshold of ~29.0%** discriminated high-risk from lower-risk patients (AUC 0.857) in one cohort.
- **Right heart catheterization** remains the **gold-standard** confirmatory test, providing direct measurement of pulmonary artery pressure, PVR, saturations at each chamber, and (where relevant) pulmonary vasoreactivity testing to assess for any residual operability.

**Genetic testing:** Not routine for sporadic ES, but consider sequencing **BMPR2, ACVRL1 (ALK1), ENG, SMAD9** when heritable PAH is suspected (e.g., family history of PAH, disproportionate severity relative to lesion, or ASD-type ES without adequate hemodynamic explanation) — a scenario explicitly documented in case reports (e.g., PMC5742392, genetic analysis in a patient with severe PAH and ASD undergoing lung transplantation).

**Differential diagnosis:** Other causes of pulmonary hypertension/right-to-left shunting must be excluded, including connective tissue disease (scleroderma, MCTD, SLE)-associated PAH, chronic viral infection (HIV, hepatitis B/C)-associated PAH, and idiopathic/heritable PAH without a structural shunt.

**Screening:** No population screening program exists for ES specifically; prevention operates through **prenatal and neonatal CHD screening** (fetal echocardiography, newborn pulse-oximetry screening for critical CHD) that enables early corrective surgery before irreversible pulmonary vascular disease develops.

---

## 11. Outcome/Prognosis

**Survival:**
- Contemporary cohort data (adjusting for prior survivorship biases): **57% 10-year survival** in the overall ES cohort and **34% 10-year survival in patients naïve to disease-targeting PAH therapy** (PMC11658362/PMID:39711759).
- Other reported figures: 98% at 1 year, 77% at 5 years, 58% at 10 years in one series; survival to age 40/50/60 of 94%/74%/52% in another.
- Historical estimates (pre-modern-therapy era): ~70–80% 10-year survival, 42% 25-year survival.
- **Median survival is reduced by approximately 20 years** compared with the general population, and is worst in patients with complex/multiple lesions.
- Notably, ES patients have **better survival than adults with idiopathic PAH** with comparable hemodynamics, attributed to the protective "pop-off" effect of the right-to-left shunt decompressing the right ventricle.

**Causes of death (contemporary/disease-targeted-therapy era, in descending order):**
1. Right heart failure (leading cause, unchanged across eras)
2. Sudden cardiac death
3. Arrhythmia
4. Hemoptysis (declined from 3rd to 5th most common with modern management)
5. Hemorrhage (~7.3% of known deaths); thromboembolism ~8.3% of known deaths

**Predictors of poor prognosis:** History of syncope, elevated mean right atrial pressure (≥8 mmHg), systemic arterial desaturation <85%, older age, pre-tricuspid shunt location, low resting SpO2, absence of sinus rhythm, pericardial effusion, reduced 6-minute walk distance, atrial fibrillation (11.45-fold increased SCD risk), QRS duration ≥120 ms (2.06-fold increased SCD risk), complete heart block, right bundle branch block, right atrial enlargement, elevated NT-proBNP, TAPSE <15 mm, low serum albumin/potassium, high cardiac MRI ECV (>29%).

**Morbidity/QoL:** Substantially reduced exercise capacity (peak VO2 ~45% lower than controls) and QoL, worse than in other complex cyanotic CHD groups; complications include thromboembolic and hemorrhagic events, renal impairment (proteinuria in up to 30%, albuminuria up to 60% of cyanotic patients), gout, cholelithiasis, hypertrophic osteoarthropathy, and neurological events.

**Special outcome context — pregnancy:** Absolute contraindication to pregnancy; maternal mortality **30–50%** (up to 65% with cesarean section), with 70% of deaths occurring in the postpartum period (days 2–30) or peripartum; major causes include hypovolemia, thromboembolism, and preeclampsia.

**Transplantation outcomes:** Heart-lung transplantation provides the best outcomes among transplant strategies for VSD-associated ES (1-, 5-, 10-year survival of 72.6%, 51.3%, 27.6%); for ASD-associated ES, bilateral lung transplant with cardiac defect repair may offer superior outcomes to combined heart-lung transplant. Median survival post-transplant: 7.4 years (heart-lung) vs. 1.1 years (isolated lung transplant, per one comparative study) — though these figures should be interpreted cautiously given selection bias in small cohorts.

---

## 12. Treatment

### Pharmacotherapy (PAH-targeted "disease-targeting therapy," DTT)
- **Endothelin receptor antagonists (ERAs):** **Bosentan** — demonstrated in the BREATHE-5 RCT to significantly improve hemodynamics and exercise capacity without worsening oxygen saturation in WHO FC III ES patients (short- and long-term). **Macitentan** (MAESTRO trial) showed no clear benefit in less advanced disease.
- **PDE-5 inhibitors:** **Sildenafil** and **tadalafil** — improve exercise capacity, functional class, hemodynamics, and QoL (PMID:20304507).
- **Prostanoids:** Inhaled **iloprost** (EIGER study, PMID:24012036) improves 6MWD, QoL, RV function; IV **epoprostenol** and subcutaneous **treprostinil** improve hemodynamics/saturation/exercise capacity; **selexipag** shows benefit in case series.
- **Soluble guanylate cyclase stimulator:** **Riociguat** — no ES-specific RCT, but subgroup PAH-CHD data show sustained 2-year improvement.
- **Combination therapy** (e.g., bosentan + sildenafil, RCT PMID via academic.oup.com/eurheartj/31/9/1124): registry data show improved survival on dual therapy vs. monotherapy, though confounded by indication in observational studies.
- **Heart failure adjuncts:** No proven mortality benefit for digoxin, ACE inhibitors, or ARBs; beta-blockers show a benefit approaching statistical significance; SGLT2 inhibitors/ARNi/MRA remain unstudied in ES specifically.
- **Anticoagulation:** Not routinely recommended absent a specific thromboembolic indication, given the coexisting bleeding diathesis; no demonstrated survival benefit.

### Advanced/procedural therapies
- **Intrathoracic organ transplantation** (heart-lung or bilateral lung + defect repair) — the only intervention that can meaningfully improve survival/QoL in advanced disease, though limited by donor availability and surgical risk (higher perioperative bleeding).
- **"Treat and repair" strategy** — aggressive PAH-targeted medical therapy followed by surgical defect closure in carefully selected, hemodynamically responsive patients; promising early/medium-term case-series outcomes but not yet a standard, systematically recommended pathway.
- Surgical closure of the underlying defect is **contraindicated** once severe, fixed (non-reversible) PAH/Eisenmenger physiology is established, since the shunt is protectively decompressing the right ventricle.

### Supportive care
- Correction of iron deficiency (careful — avoid routine venesection/phlebotomy, which worsens iron deficiency and increases stroke risk despite historical practice); phlebotomy/apheresis reserved for hemoglobin >22 g/dL with confirmed hyperviscosity symptoms after excluding dehydration/other mimics.
- Endocarditis prophylaxis, IV line air filters, avoidance of dehydration/isometric exercise/high altitude/iron deficiency.
- **Exercise training** as an adjunct to optimal medical therapy — shown safe and beneficial for 6MWD, QoL, peak VO2, and symptoms in the PAH-CHD/ES population.
- Genetic counseling for families where a heritable PAH-pathway variant is identified.

### Experimental
- Ongoing trials of macitentan (NCT01739400, long-term safety/tolerability) and other agents in ES-specific populations, tracked via ClinicalTrials.gov.

### Suggested NCIT treatment terms
- `NCIT:C15986` (Pharmacotherapy) as the generic action, with `therapeutic_agent` bound to CHEBI terms for bosentan, sildenafil, tadalafil, iloprost, epoprostenol, treprostinil, selexipag, riociguat, macitentan.
- `NCIT:C15289` (Organ Transplantation) for heart-lung/lung transplantation.
- `NCIT:C15329` (Surgical Procedure) for defect closure (in the pre-Eisenmenger or "treat-and-repair" window only).

---

## 13. Prevention

- **Primary prevention:** Timely surgical or catheter-based closure of the underlying congenital shunt lesion, ideally within the **first 1–2 years of life**, before irreversible pulmonary vascular remodeling occurs. This is by far the most effective preventive strategy and underlies the observed ~50% decline in ES prevalence over 50 years in resource-rich settings.
- **Secondary prevention/early detection:** Prenatal fetal echocardiography and newborn pulse-oximetry screening for critical CHD enable earlier diagnosis and timely surgical referral, particularly important in high-risk groups such as infants with Down syndrome and AVSD, where the historic progression rate to ES fell from 53% (1950s/60s birth cohort) to 0.5% (2000–2009 birth cohort) with improved early surgical intervention (ResearchGate/PMID:27325590 summary).
- **Tertiary prevention (in established ES):** Endocarditis prophylaxis, avoidance of precipitants (dehydration, high altitude, isometric exercise, iron deficiency), correction of iron deficiency without inappropriate venesection, annual laboratory monitoring (CBC, iron studies, renal function, uric acid), pregnancy avoidance/contraception counseling, and early initiation of PAH-targeted therapy to reduce sudden cardiac death and heart failure risk.
- **Genetic counseling:** Recommended for families with a heritable PAH-pathway variant (BMPR2 or related gene) identified in a proband, given autosomal dominant inheritance with incomplete penetrance.
- **Public health:** Improving global access to pediatric cardiac surgery and diagnostic imaging is explicitly identified in the literature as the single most impactful public-health lever, since "the majority of children at risk globally will have a reparable heart defect" and timely access "would eliminate the vast majority of suffering, disability, and death from Eisenmenger syndrome" (StatPearls NBK507800).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** Naturally occurring "Eisenmenger physiology" (shunt reversal with pulmonary hypertension) is well documented in **domestic dogs (Canis lupus familiaris, NCBITaxon:9615)** and cats, most classically in the context of **patent ductus arteriosus (PDA)** that goes unrecognized/untreated.
- **Natural disease/veterinary relevance:** In dogs with bidirectionally or continuously right-to-left shunting PDA, "Eisenmenger's (patho-)physiology" is the standard veterinary term for the same shear-stress-driven pulmonary vascular remodeling → shunt reversal sequence described in humans, with clinical presentation of cyanosis, polycythemia, and congestive heart failure (Greet et al., JVIM 2021; dvm360 review). One reported dog colony showed **pulmonary hypertension and shunt reversal developing within the first few weeks of life**, closely paralleling the accelerated human pediatric (e.g., trisomy 21) phenotype, making canine PDA populations a naturally occurring comparative model.
- **Comparative biology:** The pathophysiological cascade (endothelial shear stress → reactive vasoconstriction → medial hypertrophy → intimal proliferation → shunt reversal) is conserved between species, supporting the general mechanistic model. Differential clubbing/cyanosis (more pronounced in caudal versus cranial body regions) is a distinguishing clinical sign in PDA-associated reverse shunting in both species, reflecting the anatomic level of the shunt relative to the origin of the great vessels.
- **Zoonotic potential:** None — this is a hemodynamic/structural disease, not transmissible.

---

## 15. Model Organisms

- **In vivo surgical/flow models (primary experimental system used):**
  - **Rodent aortocaval fistula (ACF) model** — a surgically created communication between the abdominal aorta and inferior vena cava in rats/mice reproduces the physiological and pathological hallmarks of CHD-associated PAH, including volume-overload-driven pulmonary vascular remodeling and matrix synthesis changes consistent with cyclic-stretch-mediated injury (PMC5870112; PMID:32630068). This is presented in the literature as a reliable platform for studying shunt-associated PAH mechanistically, though it models flow/volume overload generally rather than a specific congenital cardiac lesion.
  - This model is also used more broadly as a volume-overload congestive heart failure/cardiac hypertrophy model (Abassi et al., 2011), so findings related purely to cardiac remodeling (versus pulmonary vascular remodeling specifically) require careful interpretation.
- **Naturally occurring animal disease** (see Section 14): Client-owned dogs with untreated/late-diagnosed PDA developing spontaneous Eisenmenger physiology represent a **naturally occurring, non-induced comparative model**, valuable because it arises without artificial surgical creation of the shunt and may better capture developmental/chronic aspects of pulmonary vascular remodeling.
- **Limitations:** No established genetically engineered mouse model (e.g., conditional Bmpr2 knockout combined with a surgical shunt) specific to Eisenmenger-type PAH-CHD was identified in this search; most mechanistic PAH mouse genetics (Bmpr2+/- mice, Sugen/hypoxia models) model idiopathic/heritable PAH rather than CHD-shunt-driven PAH specifically, and translational fidelity to the shunt-reversal endpoint of true Eisenmenger physiology has not been systematically validated — this is a candidate `HUMAN_MODEL_MISMATCH` consideration for curation (rodent flow/volume-overload models reproduce vascular remodeling features but not the full congenital developmental context, and canine natural disease, while anatomically faithful, has not been mechanistically profiled to the same molecular depth as rodent models).
- **Applications:** ACF and related shunt models are primarily used to study flow-mediated endothelial shear stress signaling, extracellular matrix remodeling, and candidate therapeutic responses (e.g., testing PAH-targeted drugs in a shunt-flow context) rather than to model the full multi-decade natural history or genetic susceptibility (BMPR2) interaction seen in humans.

---

## Summary of Key Ontology Term Suggestions for Curation

| Domain | Suggested term(s) |
|---|---|
| Disease | MONDO:0019944 (Eisenmenger syndrome); ORPHA:97214 |
| Phenotypes | HP:0007204/HP:0000961 (cyanosis), HP:0100759 (clubbing), HP:0002875 (exertional dyspnea), HP:0002105 (hemoptysis), HP:0001279 (syncope), HP:0001997 (gout), HP:0001081 (cholelithiasis), HP:0001297 (stroke), HP:0100738 (brain abscess), HP:0000093 (proteinuria) |
| Genes | hgnc:1078 (BMPR2), hgnc:175 (ACVRL1), hgnc:3349 (ENG), hgnc:11177 (SMAD9) |
| GO biological process | GO:0001974 (blood vessel remodeling), GO:0007179 (TGF-beta receptor signaling pathway), GO:0001525 (angiogenesis) |
| Cell types | CL:0000115 (endothelial cell)/pulmonary artery endothelial cell, CL:0000359 (vascular smooth muscle cell) |
| Anatomy | UBERON:0002012 (pulmonary artery), UBERON:0000948 (heart), UBERON:0002113 (kidney) |
| Chemicals/drugs | CHEBI terms for bosentan, sildenafil, tadalafil, iloprost, epoprostenol, treprostinil, macitentan, riociguat |
| Treatment actions | NCIT:C15986 (Pharmacotherapy), NCIT:C15289 (Organ Transplantation), NCIT:C15329 (Surgical Procedure) |
| Model organism | NCBITaxon:10090 (mouse)/NCBITaxon:10116 (rat) for aortocaval fistula model; NCBITaxon:9615 (dog) for natural PDA-associated disease |

---

## Sources

- [Update on Eisenmenger syndrome – Review of pathophysiology and recent progress in risk assessment and management (PMC, Banerjee & Opotowsky 2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11658362/) — PMID:39711759
- [Update on Eisenmenger syndrome (ScienceDirect)](https://www.sciencedirect.com/science/article/pii/S2666668524000296)
- [Eisenmenger Syndrome - PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/29939577/)
- [Eisenmenger Syndrome - StatPearls - NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK507800/)
- [Eisenmenger Syndrome: Background, Pathophysiology, Etiology - Medscape](https://emedicine.medscape.com/article/154555-overview)
- [Eisenmenger Syndrome Clinical Presentation - Medscape](https://emedicine.medscape.com/article/154555-clinical)
- [Eisenmenger Syndrome Treatment & Management - Medscape](https://emedicine.medscape.com/article/154555-treatment)
- [Orphanet: Eisenmenger syndrome (ORPHA:97214)](https://www.orpha.net/en/disease/detail/97214)
- [Eisenmenger syndrome | GARD](https://rarediseases.info.nih.gov/diseases/6323/eisenmenger-syndrome)
- [Eisenmenger Syndrome - Symptoms, Causes, Treatment | NORD](https://rarediseases.org/rare-diseases/eisenmenger-syndrome/)
- [Eisenmenger Syndrome: A Clinical Perspective in a New Therapeutic Era of Pulmonary Arterial Hypertension - JACC](https://www.jacc.org/doi/10.1016/j.jacc.2008.11.025) — PMID:19245962
- [Eisenmenger Syndrome: JACC State-of-the-Art Review](https://www.jacc.org/doi/10.1016/j.jacc.2022.01.022)
- [Declining incidence and prevalence of Eisenmenger syndrome in the developed world - PubMed](https://pubmed.ncbi.nlm.nih.gov/28566473/)
- [Eisenmenger Syndrome Among Children with Unrepaired Congenital Heart Defects in Yunnan, China - PubMed](https://pubmed.ncbi.nlm.nih.gov/35522268/)
- [Determinants of Sudden Cardiac Death in Adult Patients With Eisenmenger Syndrome - JAHA](https://www.ahajournals.org/doi/10.1161/JAHA.119.014554)
- [Bosentan–sildenafil association in patients with congenital heart disease-related pulmonary arterial hypertension and Eisenmenger physiology - PubMed](https://pubmed.ncbi.nlm.nih.gov/21081251/)
- [Combination therapy with bosentan and sildenafil in Eisenmenger syndrome: RCT - European Heart Journal](https://academic.oup.com/eurheartj/article/31/9/1124/591182)
- [Effects of inhaled iloprost (EIGER Study) - PubMed](https://pubmed.ncbi.nlm.nih.gov/24012036/)
- [Presentation, survival prospects, and predictors of death in Eisenmenger syndrome - European Heart Journal](https://academic.oup.com/eurheartj/article/27/14/1737/2887470)
- [Poor prognosis and related factors in adults with Eisenmenger syndrome - PubMed](https://pubmed.ncbi.nlm.nih.gov/11923814/)
- [Life span of patients with Eisenmenger syndrome is not superior to that of patients with other causes of pulmonary hypertension - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4221317/)
- [BMPR2 mutation is a potential predisposing genetic risk factor for congenital heart disease associated pulmonary vascular disease - PubMed](https://pubmed.ncbi.nlm.nih.gov/27002414/)
- [Eisenmenger syndrome and atrial septal defect: nature or nurture? - PubMed](https://pubmed.ncbi.nlm.nih.gov/17102831/)
- [The Efficacy of a Genetic Analysis of the BMPR2 Gene in a Patient with Severe PAH and ASD - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5742392/)
- [The Role of Genetics in Congenital Heart Disease-Associated Pulmonary Arterial Hypertension - Pediatric Cardiology](https://link.springer.com/article/10.1007/s00246-025-03847-z)
- [Eisenmenger syndrome and long-term survival in patients with Down syndrome and congenital heart disease - PubMed](https://pubmed.ncbi.nlm.nih.gov/27325590/)
- [Erythrocytosis and iron status in Eisenmenger syndrome: an illustrative case study - Journal of Congenital Cardiology](https://jcongenitalcardiology.biomedcentral.com/articles/10.1186/s40949-020-00045-9)
- [Should We Focus on Hematocrit or Hemoglobin in Patients With Eisenmenger Syndrome? - American Journal of Cardiology](https://www.ajconline.org/article/S0002-9149(11)02128-X/abstract)
- [Pulmonary Neovascularity - Circulation](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.104.509869)
- [Eisenmenger syndrome and idiopathic pulmonary arterial hypertension: do parenchymal lung changes reflect aetiology? - PubMed](https://pubmed.ncbi.nlm.nih.gov/17467397/)
- [Pregnancy outcome in women with Eisenmenger's syndrome: a case series from west China - BMC Pregnancy and Childbirth](https://link.springer.com/article/10.1186/s12884-016-1153-z)
- [Eisenmenger Syndrome in Pregnancy - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5094422/)
- [Heart-lung transplantation for Eisenmenger's syndrome: operative risks and late outcomes - PubMed](https://pubmed.ncbi.nlm.nih.gov/11250277/)
- [Not All Septal Defects Are Equal: Outcomes of Bilateral Lung Transplant vs Combined Heart-Lung Transplant - PubMed](https://pubmed.ncbi.nlm.nih.gov/32565271/)
- [Quality of life and functional capacity can be improved in patients with Eisenmenger syndrome with oral sildenafil therapy - PubMed](https://pubmed.ncbi.nlm.nih.gov/20304507/)
- [Exercise performance and quality of life is more impaired in Eisenmenger syndrome than in complex cyanotic congenital heart disease with pulmonary stenosis - PubMed](https://pubmed.ncbi.nlm.nih.gov/20439122/)
- [Factors influencing outcomes in patients with Eisenmenger syndrome: a nine-year follow-up study - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5841908/)
- [Detection and evaluation of myocardial fibrosis in Eisenmenger syndrome using CMR - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9677680/)
- [Characteristics of Pulmonary Vascular Remodeling in a Novel Model of Shunt-Associated Pulmonary Arterial Hypertension - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5870112/)
- [Remodeling Matrix Synthesis in a Rat Model of Aortocaval Fistula - PubMed](https://pubmed.ncbi.nlm.nih.gov/32630068/)
- [Clinical features and outcome of dogs and cats with bidirectional and continuous right-to-left shunting patent ductus arteriosus - Journal of Veterinary Internal Medicine](https://onlinelibrary.wiley.com/doi/10.1111/jvim.16072)
- [Canine pulmonary hypertension, Part 1 - dvm360](https://www.dvm360.com/view/canine-pulmonary-hypertension-part-1-depth-review-its-pathophysiology-and-classifications)
- [ICD-10-CM Diagnosis Code I27.83: Eisenmenger's syndrome](https://www.icd10data.com/ICD10CM/Codes/I00-I99/I26-I28/I27-/I27.83)
- [Eisenmenger's syndrome - Wikidata (MONDO_0019944)](https://www.wikidata.org/wiki/Q572695)
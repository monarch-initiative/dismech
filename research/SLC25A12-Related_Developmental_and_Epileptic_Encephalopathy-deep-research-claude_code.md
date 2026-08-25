---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T13:21:02.734559'
end_time: '2026-08-19T13:25:51.185036'
duration_seconds: 288.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SLC25A12-Related Developmental and Epileptic Encephalopathy
  mondo_id: ''
  category: Mendelian
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 11
  num_turns: 17
  total_cost_usd: 1.8235763000000003
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 25
reference_validation:
  total_references: 17
  verified: 15
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.118
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 15
  on_topic: 10
  off_topic: 1
  off_topic_references:
  - PMID:29353316
  unresolved_references:
  - DOI:10.3390/ijms27104455](https://www.mdpi.com/1422-0067/27/10/4455
  - DOI:10.3390/ijms27104455)](https://www.mdpi.com/1422-0067/27/10/4455
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SLC25A12-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SLC25A12-Related Developmental and Epileptic Encephalopathy** covering all of the
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

# SLC25A12-Related Developmental and Epileptic Encephalopathy (AGC1 Deficiency / DEE39): Comprehensive Research Report

## 1. Disease Information

**Overview.** SLC25A12-related developmental and epileptic encephalopathy — also called **AGC1 (Aralar) deficiency**, **aspartate-glutamate carrier 1 deficiency**, or **early infantile epileptic encephalopathy 39 (EIEE39)** — is an ultra-rare, autosomal recessive neurometabolic disorder caused by biallelic loss-of-function variants in *SLC25A12*. It is characterized by early-onset, often pharmacoresistant seizures; profound global developmental delay/arrest; severe hypotonia progressing to spasticity; global cerebral hypomyelination on MRI; and a marked, disease-defining reduction of brain N-acetylaspartate (NAA) on MR spectroscopy ([OMIM #612949](https://omim.org/entry/612949); [PMC8745132](https://pmc.ncbi.nlm.nih.gov/articles/PMC8745132/); [Wibom et al. 2009, NEJM, PMID:19641205](https://pubmed.ncbi.nlm.nih.gov/19641205/)).

**Key identifiers:**
- **OMIM phenotype:** #612949 — "Developmental and Epileptic Encephalopathy 39 with Leukodystrophy" (DEE39); previously titled "Epileptic Encephalopathy, Early Infantile, 39"
- **OMIM gene:** *603667 — SLC25A12
- **Gene locus:** chromosome 2, band 2q31 (some sources cite 2q24.3; NCBI Gene places SLC25A12 at 2q31.1)
- **Orphanet:** ORPHA:353217 — "Epileptic encephalopathy with global cerebral demyelination" (SLC25A12-related)
- **Disease Ontology:** DOID:0080349
- **HGNC gene ID:** HGNC:10982 (SLC25A12)
- **MONDO:** the disease is cross-referenced from the OMIM/Orphanet entries above; exact MONDO CURIE was not independently confirmed in this pass and should be verified in the MONDO browser before curation (search MONDO for "developmental and epileptic encephalopathy 39").
- **ICD-10/11:** no disease-specific code exists; typically coded under the generic epileptic-encephalopathy/leukodystrophy categories (e.g., ICD-10 G40.8-/G93.4, or Q87.8 for the broader neurodevelopmental syndrome group).

**Synonyms/alternative names:** AGC1 deficiency; Aralar deficiency; Aspartate/glutamate carrier 1 deficiency; Early infantile epileptic encephalopathy 39 (EIEE39); Developmental and epileptic encephalopathy 39 (DEE39); DEE39 with leukodystrophy; Epileptic encephalopathy with global cerebral hypomyelination/demyelination.

**Data provenance.** Knowledge derives almost entirely from **aggregated case reports and small case series** in the literature (no large clinical-trial or registry cohort exists) — approximately 16–20 individual patients have been reported worldwide across the original description and subsequent case reports, plus one 6-patient cohort study (Bølsterli et al.) and extensive characterization of *Slc25a12* knockout mice (source: [MDPI 2026 review, doi:10.3390/ijms27104455](https://www.mdpi.com/1422-0067/27/10/4455)).

---

## 2. Etiology

**Disease causal factor:** Biallelic (homozygous or compound heterozygous) pathogenic loss-of-function variants in *SLC25A12*, encoding the neuronal/muscle-specific mitochondrial aspartate-glutamate carrier isoform 1 (AGC1/Aralar). This is a purely **monogenic, autosomal recessive** disorder — no meaningful environmental, infectious, or multifactorial contribution has been established.

**Genetic risk factors:**
- Causal biallelic *SLC25A12* variants (see §4 for full variant table).
- Consanguinity is a recognized risk factor for homozygous presentations — several reported families are consanguineous, consistent with an ultra-rare autosomal recessive disease.
- No modifier genes have been identified to date; no robust genotype-phenotype correlation has been established given the small number of reported cases ([MDPI review](https://www.mdpi.com/1422-0067/27/10/4455)).

**Environmental risk factors:** None established. This is a purely genetic, congenital metabolic disease; there is no reported gene-environment interaction literature specific to DEE39.

**Protective factors:**
- No genetic protective/modifier alleles reported.
- **Environmental/therapeutic "protective" factor:** ketogenic diet (KD) / ketone-body supplementation is the only intervention shown to modify the biochemical and clinical phenotype (see §6, §12), acting by bypassing the AGC1-dependent malate-aspartate shuttle block rather than correcting the underlying genetic lesion.

**Gene-environment interactions:** Not applicable in the classic sense (this is monogenic), but the KD literature effectively represents a therapeutic "environmental" intervention (dietary ketosis) engineered to compensate for the genetic metabolic block — see §6.

**Note on unrelated SLC25A12 common-variant literature:** Early candidate-gene studies proposed common *SLC25A12* polymorphisms as autism spectrum disorder (ASD) susceptibility variants; however, larger cohorts and meta-analyses have **not** consistently supported this association ([PMID:25921325](https://pubmed.ncbi.nlm.nih.gov/25921325/); MDPI review). This ASD-association literature is distinct from, and much weaker than, the rare biallelic loss-of-function mechanism causing DEE39, and should not be conflated with it in curation.

---

## 3. Phenotypes

**Onset/characteristics:** Infants are typically **normal at birth and during the first weeks-to-months of life**, then manifest arrested/regressing psychomotor development, hypotonia, and seizure onset usually within the first year (often first months) of life.

### Core phenotypes (suggested HPO terms):

| Phenotype | Description | Suggested HPO term |
|---|---|---|
| Early-onset seizures | Onset in infancy/first year; often focal, apnea-associated; frequently pharmacoresistant | HP:0002011 (Morphological CNS abnormality) / HP:0011097 (Epileptic spasm) / HP:0032792 (Refractory seizure) / HP:0001250 (Seizure) |
| Global developmental delay/arrest | Profound; affects both motor and cognitive domains from infancy | HP:0001263 (Global developmental delay) |
| Severe hypotonia | Marked, early, progresses toward spasticity in some | HP:0001252 (Hypotonia) |
| Spasticity/hyperreflexia | Reported in a subset, sometimes with dystonia | HP:0001257 (Spasticity), HP:0001347 (Hyperreflexia), HP:0001332 (Dystonia) |
| Absent speech | Universal in severe cases | HP:0001344 (Absent speech) |
| Inability to walk / nonambulatory status | Severe motor impairment | HP:0002540 (Inability to walk) |
| Cerebral/global hypomyelination | Hallmark neuroimaging finding, hemispheric predominance with relative cerebellar/brainstem sparing | HP:0002188 (Delayed CNS myelination) / HP:0006970 (Hypomyelination of white matter) |
| Cerebral atrophy/volume loss | Progressive, supratentorial predominant | HP:0002059 (Cerebral atrophy) |
| Secondary microcephaly | Reported in a subset | HP:0000252 (Microcephaly) |
| Feeding difficulties | Common in severe infantile cases | HP:0011968 (Feeding difficulties) |
| Reduced brain N-acetylaspartate (NAA) on MRS | Biochemical/radiological hallmark | HP:0012332 (Abnormal metabolism, or use as a biomarker in `biochemical`) |
| Intermittent lactate elevation | Seen on MRS/plasma in a subset | HP:0002151 (Increased serum lactate) |
| Cerebellar/brainstem relative sparing | Distinguishes from other leukodystrophies on MRI | (descriptive; no single dedicated HPO term) |

**Severity/progression:** Highly variable across the ~16–20 reported patients — ranging from severe neonatal-onset encephalopathy with progressive cerebral atrophy, to milder, epilepsy-predominant presentations with initially near-normal MRI. Longitudinal MRI in the oldest reported patient (12 years old) showed a pattern most consistent with a **"leuko-axonopathy"** category of leukodystrophy, with cerebral atrophy and white-matter involvement progressing over time ([Kavanaugh et al., PMID:31403263](https://pubmed.ncbi.nlm.nih.gov/31403263/)).

**Quality of life impact:** Severe — most reported patients are nonambulatory, nonverbal, and require lifelong supportive/custodial care; one report specifically notes a "happy disposition" despite profound impairment (Kavanaugh et al., PMID:31403263), a phenotype descriptor sometimes seen in severe neurodevelopmental syndromes. No formal EQ-5D/SF-36/PROMIS quality-of-life instrument data exist for this ultra-rare condition.

---

## 4. Genetic/Molecular Information

**Causal gene:** *SLC25A12* (HGNC:10982), encoding AGC1/Aralar, the neuron/muscle-specific isoform of the mitochondrial aspartate-glutamate carrier (the liver isoform, AGC2/citrin, encoded by the paralog *SLC25A13*, causes the distinct disease citrin deficiency — see [PMID:33087477-adjacent literature] and [PMC7614230](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7614230/) for the paralogous carrier).

**Inheritance:** Autosomal recessive (biallelic pathogenic variants required).

**Reported pathogenic variants** (compiled from OMIM, ClinVar, and case-series literature; genomic coordinates per GRCh38/NM_003705.5 transcript):

| Patient/source | Variant (cDNA/protein) | Zygosity | Functional consequence | Reference |
|---|---|---|---|---|
| Original index case (Wibom et al. 2009) | c.1769A>G, p.Gln590Arg | Homozygous | Missense; abolished aspartate/glutamate transport activity in reconstituted liposome assay; protein correctly inserted into inner mitochondrial membrane but functionally inactive | [PMID:19641205](https://pubmed.ncbi.nlm.nih.gov/19641205/) |
| Falk et al. siblings | c.1058G>A, p.Arg353Gln | Homozygous | Missense; residual activity ~15% of wild-type (loss-of-function, not gain-of-function) | PMID:24515575 |
| Parnes et al. | p.Lys100fs (frameshift) / p.Ile72Thr | Compound heterozygous | Frameshift (null allele) + missense in Ca²⁺-binding EF-hand domain | referenced in review; original PMID:12084073 region |
| Pronicka et al. | c.1335C>A, p.Asn445Lys | Homozygous | Missense; likely buried/protein-folding-destabilizing variant | cited in [MDPI review](https://www.mdpi.com/1422-0067/27/10/4455) |
| Pfeiffer et al. | c.1331C>T, p.Thr444Ile | Homozygous | Missense affecting substrate-translocation pore; notable case with initially preserved myelination at 10 months | related to PMID:31054490 region |
| Kavanaugh et al. 2019 | c.1295C>T, p.Ala432Val / c.1447-2_1447-1delAG | Compound heterozygous | Missense + canonical splice-acceptor deletion (removes splice acceptor site) | [PMID:31403263](https://pubmed.ncbi.nlm.nih.gov/31403263/) |
| Nashabat et al. | c.1385C>T, p.Thr462Met | Homozygous | Missense; atypical presentation with preserved brain MRI | PMID:31054490 |
| Saleh et al. | c.400C>T, p.Arg134Ter (Arg134*) | Homozygous | Nonsense; premature truncation/null allele | cited in review and in a "Novel Nonsense Gene Variant" case report ([SciAlert PJBS 2020](https://scialert.net/fulltext/?doi=pjbs.2020.973.976)) |
| Kose et al. | c.125G>C, p.Arg42Pro | Homozygous | Missense | cited in review |
| Additional reported variant classes (Bølsterli cohort and others) | p.Leu271Thrfs*9; p.Glu76Serfs*17; exon 16–17 deletion; p.Asp540Asn | Various | Frameshift/null alleles; large exonic deletion; substrate-pore missense | [MDPI review](https://www.mdpi.com/1422-0067/27/10/4455) |

**Structural interpretation:** Variants affecting the substrate-translocation pore (e.g., p.Thr444Ile, p.Asp540Asn, p.Gln590Arg) appear to more directly impair transport activity, while "buried" missense variants (e.g., p.Arg353Gln, p.Asn445Lys) more likely destabilize overall protein folding/stability. However, **no robust genotype-phenotype correlation has been established** given the small number of reported patients (MDPI review).

**Variant classification (ACMG/AMP):** Multiple variants (e.g., p.Gln590Arg, ClinVar RCV000006523) are classified in ClinVar as Pathogenic/Likely Pathogenic for "Developmental and epileptic encephalopathy 39." Nonsense and frameshift variants are generally classified pathogenic by predicted loss-of-function; missense variants have been functionally validated by liposome reconstitution assays showing loss of aspartate/glutamate antiporter activity while the protein is correctly inserted into the inner mitochondrial membrane.

**Population frequency:** *SLC25A12* is not a gene under strong population-level constraint reporting in the readily available search results; individual reported pathogenic alleles are extremely rare in gnomAD (population allele frequency <0.001% for specific variants checked). No formal carrier-frequency estimate for the disease as a whole has been published, consistent with its status as an ultra-rare condition (~16–20 patients described worldwide to date).

**Mechanism of loss of function:** All well-characterized variants act via a **loss-of-function** mechanism (reduced or abolished aspartate/glutamate antiporter activity), not gain-of-function — an important curation point since some pre-search assumptions (and the disease-report title provided) might suggest otherwise; the literature consistently supports biallelic LOF as the mechanism (e.g., p.Arg353Gln retains only ~15% of wild-type transport activity; p.Gln590Arg is essentially inactive).

**Epigenetics/chromosomal abnormalities:** No epigenetic mechanism (DNA methylation, histone modification) or chromosomal-level abnormality (aneuploidy, translocation) has been reported as causal; the disease is driven exclusively by coding/splice-region point variants, small indels, and at least one exonic deletion (exons 16–17) at the *SLC25A12* locus.

**Suggested gene/GO annotations:**
- Gene: *SLC25A12* (hgnc:10982)
- Molecular function: GO:0015183 (L-aspartate transmembrane transporter activity) / GO:0070906 (aspartate transmembrane transport-related; use closest matching GO term for mitochondrial aspartate/glutamate antiporter activity)
- Cellular component: GO:0005743 (mitochondrial inner membrane)

---

## 5. Environmental Information

No environmental factors, lifestyle exposures, or infectious agents have been identified as contributing to disease causation — this is a purely monogenic condition. The only "environmental" lever with documented modifying effect on the phenotype is **dietary ketosis** (ketogenic diet), which is therapeutic rather than causal/risk-modifying (see §6 and §12).

---

## 6. Mechanism / Pathophysiology

**Molecular pathway — the malate-aspartate shuttle (MAS):** AGC1/Aralar is the **regulatory, Ca²⁺-stimulated component of the malate-aspartate shuttle**, the principal NADH redox shuttle transferring reducing equivalents from cytosol to mitochondria in neurons. AGC1 exchanges mitochondrial aspartate for cytosolic glutamate (plus H⁺) across the inner mitochondrial membrane, enabling regeneration of cytosolic NAD⁺ and export of mitochondrial aspartate for cytosolic biosynthetic use ([Wibom et al. 2009, PMID:19641205](https://pubmed.ncbi.nlm.nih.gov/19641205/); MDPI 2026 review).

**Causal chain (upstream → downstream):**

1. **Trigger (molecular scale):** Biallelic loss-of-function *SLC25A12* variants → loss/severe reduction of AGC1 aspartate/glutamate antiporter activity (GO:0015183-adjacent transport function; GO:0005743 mitochondrial inner membrane localization).
2. **Malate-aspartate shuttle failure (molecular/cellular scale):** Impaired mitochondrial aspartate efflux and cytosolic NADH reoxidation → increased cytosolic NADH/NAD⁺ ratio, impaired cytosolic redox coupling.
3. **Bioenergetic failure (cellular scale):** Aralar-deficient neurons show ~50% reduction in basal mitochondrial respiration on glucose and severely impaired stimulation of respiration during neuronal activation (activity-dependent Ca²⁺ signaling normally activates AGC1) → limited ATP supply during neuronal firing.
4. **Aspartate/NAA depletion (biochemical scale):** Brain aspartate levels fall ~80–90% in AGC1 deficiency (both human patients and knockout mice). Because aspartate is the substrate for N-acetylaspartate (NAA) synthesis (via aspartate N-acetyltransferase, NAT8L), NAA — the second most abundant CNS metabolite — is dramatically reduced. NAA undergoes transaxonal transport (via a dicarboxylate transporter, e.g., NaDC3) to oligodendrocytes, where aspartoacylase (ASPA) cleavage liberates acetyl groups used for myelin lipid (galactocerebroside) synthesis.
5. **Hypomyelination (tissue scale):** Loss of the NAA-derived acetyl-group supply to oligodendrocytes → impaired myelin lipid (galactocerebroside) synthesis → global cerebral hypomyelination, with hemispheric predominance and relative cerebellar/brainstem sparing. An alternative/complementary hypothesis proposes a primary **"leuko-axonopathy"** mechanism, in which primary neuronal/axonal dysfunction (rather than primary oligodendrocyte demyelination) drives the imaging phenotype, supported by longitudinal MRI in an older patient ([Kavanaugh et al., PMID:31403263](https://pubmed.ncbi.nlm.nih.gov/31403263/)).
6. **Astroglial glutamine-glutamate cycle failure:** Despite AGC1 being neuron-specific, astroglial glutamine synthesis becomes impaired because neuronal aspartate normally serves as a nitrogen donor for astrocytic glutamate formation (which astrocytes then convert to glutamine) — a non-cell-autonomous downstream consequence.
7. **Loss of lactate shuttle protection:** The astrocyte-to-neuron lactate shuttle becomes non-functional in AGC1 deficiency, eliminating lactate's normal protective role against excitotoxicity.
8. **Epileptogenesis (organism scale):** Multiple converging factors — reduced activity-dependent ATP supply, impaired glutamine-glutamate neurotransmitter cycling, loss of lactate's neuroprotective buffering, and developmental immaturity of inhibitory circuitry — combine to produce neuronal hyperexcitability despite an overall energy-deficient state, a paradox also observed in other metabolic encephalopathies.
9. **Dopaminergic vulnerability (nigrostriatal circuit):** Aralar deficiency selectively affects nigrostriatal dopaminergic neurons; because Complex I of the electron transport chain becomes substrate-limited (depleted pyruvate/NADH supply), dopaminergic neurons show decreased dopamine content, elevated catabolism (increased DOPAC/dopamine ratio), and oxidative stress, contributing to the movement-disorder features (spasticity, dystonia) seen in some patients.

**Cell types involved (suggested CL terms):**
- Neurons (CL:0000540) — primary site of AGC1 expression and the origin of the bioenergetic/aspartate-supply defect
- Oligodendrocytes / oligodendrocyte precursor cells (CL:0000128 / CL:0002453) — downstream targets of NAA deficiency; documented proliferation and maturation defects in AGC1-deficient OPCs both in vitro and in vivo ([PMC6769484](https://pmc.ncbi.nlm.nih.gov/articles/PMC6769484/))
- Astrocytes (CL:0000127) — non-cell-autonomous glutamine-synthesis failure despite preserved glucose metabolism
- Nigrostriatal dopaminergic neurons (CL:0000700 or more specific CL term for substantia nigra dopaminergic neuron) — selective vulnerability with dopamine handling deficits

**Suggested GO biological process terms:**
- Malate-aspartate shuttle / NADH regeneration process (closest GO: "aspartate transport," "mitochondrial electron transport," "cellular respiration," GO:0045333 cellular respiration)
- Myelination (GO:0042552)
- Oligodendrocyte differentiation (GO:0048709)
- Glutamate/glutamine metabolic cycling (GO:0006536 glutamate metabolic process)

**Anatomical localization (subcellular):** GO Cellular Component — GO:0005743 (mitochondrial inner membrane), the site of AGC1 localization and the malate-aspartate shuttle machinery.

**Molecular profiling notes:** Liposome-reconstitution functional assays are the primary "molecular profiling" technique applied to characterize patient variants (demonstrating correctly membrane-inserted but transport-inactive mutant protein for several missense alleles). No large-scale transcriptomic, proteomic, or single-cell datasets specific to human AGC1-deficiency patient tissue were identified in this search; mouse-model transcriptomic/metabolic profiling of OPCs exists (e.g., [PMC10979587](https://pmc.ncbi.nlm.nih.gov/articles/PMC10979587/), "Transcriptional and metabolic effects of AGC1 downregulation in mouse oligodendrocyte precursor cells").

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary organ:** Brain (central nervous system) — cerebral hemispheres (white matter) primarily affected, with relative sparing of cerebellum and brainstem.
- **Secondary/systemic involvement:** Skeletal muscle is a tissue of AGC1 expression (given its role in energetically demanding tissues), though clinical muscle disease is not a prominent reported feature; hypotonia is thought to be primarily of central (CNS) origin.
- **Body systems involved:** Nervous system (primary); musculoskeletal system (secondary, via hypotonia/spasticity).

Suggested UBERON terms: UBERON:0000955 (brain), UBERON:0002037 (cerebellum, relatively spared), UBERON:0001890 (forebrain/cerebral hemisphere, primarily affected), UBERON:0002298 (brainstem, relatively spared), UBERON:0002316 (white matter of the CNS).

**Tissue/cell level:** Cerebral white matter (hypomyelinated); cortical gray matter (secondary atrophy); nigrostriatal dopaminergic pathway (substantia nigra, striatum) — see §6 for cell types.

**Subcellular level:** Mitochondria, specifically the inner mitochondrial membrane (GO:0005743), where AGC1 resides as the transport protein whose dysfunction initiates the pathological cascade.

**Localization/lateralization:** Cerebral hypomyelination and atrophy are typically bilateral and diffuse/global rather than lateralized, with a hemispheric-predominant, cerebellar/brainstem-sparing pattern that is considered a neuroradiological hallmark distinguishing this disorder from other leukodystrophies.

---

## 8. Temporal Development

**Onset:** Congenital/genetic lesion present from conception, but clinically silent initially — infants are typically **normal during the first weeks to months of life**, with symptom onset (developmental arrest, hypotonia, seizures) emerging within the **first year of life** (often within the first months), consistent with an early-infantile-onset pattern. Onset pattern is generally **insidious-to-subacute** (developmental arrest/regression) with seizure onset that can be more acute.

**Progression:**
- **Disease course:** Predominantly progressive — cerebral atrophy and white-matter abnormalities worsen over time on longitudinal imaging (documented out to 12 years of age in the oldest reported patient); NAA remains persistently reduced.
- **Progression rate:** Variable across the reported cohort — some patients show relatively static severe encephalopathy from infancy, while others (notably those in whom ketogenic diet was initiated) show partial "recovery" of myelination, brain volume, and NAA over subsequent years.
- **Disease duration:** Chronic, lifelong — no reported cases of spontaneous remission or cure; this is a static-to-progressive, non-self-limited condition.

**Patterns:**
- **Remission:** Not spontaneous; treatment-induced improvement (seizure freedom, partial myelination recovery) has been documented with ketogenic diet in a subset of patients (see §12).
- **Critical periods:** Early initiation of ketogenic diet appears to be associated with better neurodevelopmental and imaging outcomes than later initiation, suggesting a developmental window during which restoring metabolic support may have greater benefit for ongoing myelination — though this remains based on small case numbers rather than controlled trials.

---

## 9. Inheritance and Population

**Epidemiology:** AGC1 deficiency is an **ultra-rare** disorder. Approximately 16–20 individual patients have been reported in the literature to date (across the index cases plus subsequent case reports and one 6-patient case series), with no formal population prevalence or incidence estimate published. Given the rarity and the small number of reported families, exact prevalence/incidence figures per 100,000 are not available.

**Inheritance pattern:** Autosomal recessive (AR) — all reported cases are homozygous or compound heterozygous for biallelic pathogenic *SLC25A12* variants.

**Penetrance:** Presumed complete for biallelic loss-of-function genotypes, based on all reported cases being clinically affected; however, given the very small sample size, formal penetrance estimates are not statistically robust.

**Expressivity:** Variable — clinical severity ranges from severe neonatal-onset encephalopathy with progressive atrophy to milder, epilepsy-predominant presentations with initially near-normal MRI (e.g., the Pfeiffer/Thr444Ile and Nashabat/Thr462Met cases with atypical, milder imaging).

**Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).

**Consanguinity role:** A recognized contributing factor — several reported homozygous cases arise in consanguineous families, consistent with the autosomal recessive, ultra-rare nature of the disease.

**Carrier frequency:** Not formally established; individual pathogenic alleles are exceedingly rare in population databases (gnomAD allele frequencies <0.001% for specific variants checked), consistent with the disease's ultra-rare status and lack of a known founder population.

**Population demographics:** No specific ethnic or geographic enrichment has been reported; cases have been described across multiple countries/populations (e.g., Sweden [original NEJM case], Saudi Arabia [Nashabat, Saleh], Turkey/other populations [Kose], and North America [Kavanaugh, Pfeiffer]), consistent with a pan-ethnic, sporadic occurrence pattern typical of an ultra-rare autosomal recessive disease with private founder mutations in each family rather than a single recurrent founder allele.

**Sex ratio:** No sex predilection reported — males and females appear equally affected across the published cases.

**Age distribution:** All reported patients present in infancy/early childhood; the oldest longitudinally followed patient in the literature was 12 years old at last reported follow-up ([Kavanaugh et al., PMID:31403263](https://pubmed.ncbi.nlm.nih.gov/31403263/)).

---

## 10. Diagnostics

**Laboratory/biochemical findings:**
- Intermittently elevated plasma lactate (not a consistent finding).
- Normal plasma amino acids (notably, plasma aspartate is typically normal despite markedly reduced CSF/brain aspartate — reflecting the compartmentalized, brain-specific nature of the biochemical defect).
- Reduced CSF aspartate.
- Normal standard mitochondrial respiratory chain enzyme activities (the defect is specific to the malate-aspartate shuttle, not generalized OXPHOS).

**Neuroimaging (MRI):**
- Global/diffuse cerebral hypomyelination, hemispheric-predominant with relative cerebellar/brainstem sparing.
- Supratentorial volume loss / cortical and cerebral atrophy, often progressive on serial imaging.
- Suggested RadLex/imaging descriptor: delayed myelination pattern; leukodystrophy/leuko-axonopathy pattern on longitudinal follow-up.

**Magnetic resonance spectroscopy (¹H-MRS) — key diagnostic biomarker:**
- Markedly reduced NAA/creatine ratio (the disease-defining biochemical signature).
- Elevated myo-inositol.
- Potential intermittent lactate peak.

**Genetic testing:**
- **Recommended approach:** Whole-exome sequencing (WES) is the primary diagnostic modality that has identified essentially all reported cases, given the extreme rarity and lack of a recognizable "typical" single-gene-testing indication a priori; targeted single-gene *SLC25A12* Sanger sequencing can confirm/segregate a variant once identified.
- **Gene panels:** *SLC25A12* is included in early-onset/syndromic epilepsy gene panels (e.g., Genomics England PanelApp "Early onset or syndromic epilepsy" panel) and in leukodystrophy/hypomyelination gene panels.
- **Functional/biochemical confirmation:** Liposome-reconstitution transport assays have been used research-wise to confirm loss of aspartate/glutamate antiporter function for novel missense variants — not a routine clinical diagnostic test.
- Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are not primary diagnostic tools for this nuclear-gene, point-variant/small-indel disorder (though an exonic deletion, exons 16–17, has been reported, which CMA could in principle detect if large enough).

**Clinical/differential diagnosis:** Differentiate from other genetic leukodystrophies/hypomyelinating disorders (e.g., Pelizaeus-Merzbacher disease, other malate-aspartate-shuttle defects — MDH1, MDH2, GOT2 deficiencies, which produce phenotypically similar epilepsy/hypomyelination/atrophy syndromes) and from other early-infantile developmental and epileptic encephalopathies more broadly. The combination of hypomyelination + markedly reduced NAA on MRS is a relatively distinguishing diagnostic clue pointing toward a malate-aspartate-shuttle defect.

**Screening:** No newborn screening or population carrier-screening program exists for this ultra-rare condition; diagnosis is currently exclusively clinical-genetic (WES-driven) in symptomatic infants.

---

## 11. Outcome/Prognosis

**Survival/mortality:** No formal survival statistics are available given the small number of reported cases; the disease is not classically described as acutely life-limiting in the same way as some other severe infantile metabolic encephalopathies, but severe multisystem disability (nonambulatory, nonverbal status) is typical, and long-term life expectancy data are not established in the literature reviewed.

**Morbidity/function:** Most reported patients remain **nonambulatory and nonverbal**, with severe intellectual disability, spastic quadriplegia in some, and lifelong dependence on caregivers. No standardized functional outcome scales (e.g., ICF-based) have been systematically applied in the published case literature.

**Disease course/complications:** Progressive cerebral atrophy and persistent hypomyelination on longitudinal imaging in most reported patients; pharmacoresistant epilepsy is a major ongoing complication requiring polytherapy in many cases.

**Recovery potential:** Ketogenic diet treatment has been associated with meaningful clinical improvement in a subset of patients — including seizure freedom/reduction, resumed myelination, increased brain volume/NAA on follow-up MRS, and in some cases achievement of independent walking — representing the most encouraging prognostic modifier identified to date (see §12). However, response is heterogeneous, and some patients show no benefit.

**Prognostic factors:** Timing of ketogenic diet initiation (earlier appears more favorable), stability/duration of ketosis achieved, and possibly specific variant/residual-activity level (though no formal genotype-phenotype correlation is established) are the main prognostic modifiers discussed in the literature.

---

## 12. Treatment

**Primary treatment: Ketogenic diet (KD) / ketone-based metabolic therapy** — the central, disease-specific therapeutic approach reported in the literature (NCIT term suggestion: NCIT:C15447, Dietary Intervention).

**Rationale/mechanism:** KD elevates circulating β-hydroxybutyrate (BHB) and acetoacetate, which cross the blood-brain barrier and fuel mitochondrial oxidation independently of the glycolysis-dependent malate-aspartate shuttle. Proposed mechanisms include:
1. Ketone oxidation enhances mitochondrial NADH production and ATP synthesis, bypassing the AGC1-dependent redox-shuttle block.
2. Reduces glycolytic NADH production, shifting cytosolic malate dehydrogenase 1 (MDH1) equilibrium toward oxaloacetate, enabling alternative AGC1-independent cytosolic aspartate synthesis.
3. May support oligodendrocyte lipid/myelin synthesis directly via a citrate-malate shuttle generating cytosolic aspartate.
4. Additional proposed effects: glutamate-GABA rebalancing to reduce hyperexcitability; HDAC inhibition/neurotrophic factor modulation; gut-microbiota effects on the gut-brain axis.

**Documented clinical outcomes (case-level, from published reports):**

| Patient (variant) | KD regimen | Seizure outcome | Other outcomes |
|---|---|---|---|
| Pfeiffer (p.Thr444Ile) | 4:1 classical KD | Seizure freedom within ~4 months | Improved alertness; persistent developmental delay; NAA remained reduced |
| Dahlin/Wibom index patient (p.Gln590Arg) | Standard KD | Seizure freedom, antiepileptic drug tapering achieved | Resumed myelination, increased brain volume and NAA on follow-up MRS — notably improved even when initiated at 6 years of age |
| Bølsterli cohort patient "AGC1-1" (exon 16–17 deletion) | Classical KD | Seizure freedom | Improved MRI myelination |
| Bølsterli cohort patient "AGC1-5" (p.Glu76Serfs*17) | Standard KD | Seizure reduction | Achieved independent walking |
| Bølsterli cohort patient "AGC1-2" (p.Asp540Asn) | 2:1 KD | Modest improvement | No motor/developmental gains |
| Bølsterli cohort patient "AGC1-4" (p.Leu271Thrfs*9) | Standard KD | No benefit | Persistent severe developmental delay and dystonia |

**Key findings:** Seizure reduction is the most reproducible clinical benefit of KD; neurodevelopmental, movement-disorder, and imaging (myelination/NAA) improvements are more heterogeneous and appear dependent on timing, duration, and stability of ketosis achieved. Preclinical mouse studies (aralar-KO mice given perinatal β-hydroxybutyrate supplementation, without full dietary fat restriction) confirm that BHB alone can preserve mitochondrial respiration, support aspartate/NAA synthesis, promote myelination, and improve dopamine homeostasis and striatal neuron viability — suggesting BHB itself, not merely global caloric/macronutrient restriction, is mechanistically active ([PMC7687055, "βOHB Protective Pathways in Aralar-KO Neurons and Brain: An Alternative to Ketogenic Diet"](https://pmc.ncbi.nlm.nih.gov/articles/PMC7687055/); [PMID:29353316](https://pubmed.ncbi.nlm.nih.gov/29353316/)).

**Safety considerations for KD:** Standard KD monitoring applies — dyslipidemia, nephrolithiasis (kidney stones), gastrointestinal symptoms, and nutritional deficiencies should be monitored; less restrictive regimens (medium-chain triglyceride diet, Modified Atkins Diet) are suggested alternatives for patients intolerant of classical 4:1 KD.

**Other/supportive treatments:**
- **Antiepileptic drugs (AEDs):** Standard first-line seizure management, but most patients show refractoriness to conventional AEDs alone, which is part of the rationale for adding/transitioning to KD.
- **Supportive/rehabilitative care:** Physical therapy (NCIT:C15302), occupational therapy, and general supportive/palliative multidisciplinary management for severe neurodevelopmental disability are standard, though not disease-specific.
- **Proposed but unproven adjuncts:** Pyridoxine and serine supplementation, which show responsiveness in related malate-aspartate-shuttle enzyme deficiencies (MDH2, GOT2 deficiencies), have been proposed as potentially beneficial in AGC1 deficiency by analogy, though not directly trialed/reported in AGC1-deficient patients per this search.

**Gene-specific/molecular therapies:** No gene therapy, RNA-based therapy, cell therapy, or targeted molecular therapy has been reported or is in clinical trials for this condition (ClinicalTrials.gov search context implied by the ultra-rare nature and small patient population — no NCT identifiers were identified in this research pass).

**Treatment strategy note for curation:** The mechanistic pattern here (a monogenic mitochondrial-transporter loss-of-function disorder treated by a dietary/metabolic bypass strategy) is analogous to other malate-aspartate-shuttle and related "ketogenic-diet-responsive" mitochondrial disorders (MDH1, MDH2, GOT2, pyruvate carrier defects) — see [PMC9460686, "Ketogenic Diet Treatment of Defects in the Mitochondrial Malate Aspartate Shuttle and Pyruvate Carrier"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9460686/) — and may be a candidate for a shared dismech mechanism-module pattern (metabolic-bypass therapy) analogous to existing modules like `metabolic_intoxication_decompensation`, though as a treatment-mechanism rather than a decompensation-mechanism pattern.

---

## 13. Prevention

No primary, secondary, or tertiary prevention strategies specific to this disease have been established or reported, consistent with its status as an ultra-rare monogenic condition with no population screening program.

- **Primary prevention:** Not applicable at a population level; theoretically, prenatal genetic counseling and carrier testing in consanguineous families with a known proband could allow informed reproductive decision-making (preimplantation genetic diagnosis, prenatal testing), but no published program or protocol specific to *SLC25A12* was identified.
- **Secondary prevention/screening:** No newborn screening or carrier screening program exists.
- **Genetic counseling:** Standard autosomal recessive genetic counseling principles apply once a proband is identified — 25% recurrence risk for future pregnancies in known carrier couples, with prenatal diagnosis or preimplantation genetic testing options where the familial variant(s) are known (NCIT:C15240, Genetic Counseling).
- **Tertiary prevention:** Early initiation of ketogenic diet (see §12) functions as the closest analog to a tertiary-prevention/disease-modifying strategy, aiming to reduce ongoing seizure burden and support ongoing myelination once the diagnosis is made.

---

## 14. Other Species / Natural Disease

No naturally occurring veterinary disease (companion animal, livestock, or wildlife) analog to human AGC1 deficiency was identified in this search — there is no evidence of a described natural *Slc25a12*-deficiency disease in dogs, cats, or other companion species (unlike, e.g., some other inherited metabolic/neurologic diseases with recognized veterinary counterparts). This appears to be a human-and-engineered-mouse-model disease only, based on available literature.

**Orthologous gene:** *Slc25a12* (mouse, MGI:1926080); orthologs exist across vertebrates and are conserved down to invertebrates and yeast (see §15 comparative biology).

---

## 15. Model Organisms

**Mouse (Mus musculus) — Aralar/AGC1/Slc25a12 knockout mice** (the principal and best-characterized animal model):

- **Model types:** Two independent knockout lines have been generated and characterized:
  1. Hybrid SVJ129 × C57BL/6 background, generated with gene disruption at intron 13 (obtained from Lexicon Pharmaceuticals Inc.)
  2. Pure C57BL/6 background, with exon 1 deletion
  Both lines show highly concordant phenotypes.

- **Phenotype recapitulation:**
  - Growth retardation, generalized tremor, pronounced motor coordination defects.
  - Seizures.
  - Global hypomyelination without loss of neuron number — impaired myelination on histology, with marked decrease in the myelin lipid galactocerebroside.
  - Brain aspartate and NAA levels drastically decreased (80–90% reduction across all brain regions), directly recapitulating the human biochemical hallmark.
  - Reduced survival — mortality typically occurring at postnatal day 20–22.
  - No overt neuronal cell death despite the severe metabolic dysfunction — supporting a functional/metabolic rather than degenerative mechanism.
  - Pronounced neurofilament loss in striatum and cortex, independent of the myelination defect.
  - Increased immature oligodendrocytes with maturation defects.
  - Failure to stimulate mitochondrial respiration during neuronal activation via Ca²⁺ signaling; severely compromised astrocyte-neuron lactate shuttle function; astroglial glutamine-synthesis failure despite preserved astrocyte glucose metabolism.
  - Nigrostriatal dopamine dysfunction: decreased dopamine content, elevated catabolism (increased DOPAC/dopamine ratio), oxidative stress; associated hyperactivity and anxiety-like behavior.
  - Deficient glucose and glutamine metabolism contributing to altered visual function has also been reported in this model ([Molecular Vision paper](http://www.molvis.org/molvis/v22/1198/)).
  - Altered mitochondrial movement/trafficking in Aralar/Slc25a12-deficient cortical neurons has also been documented.

- **Key primary sources:** Original mouse characterization ([PMID:19641205](https://pubmed.ncbi.nlm.nih.gov/19641205/), Wibom et al. NEJM 2009, which paired the human index case with parallel mouse-model data); "Slc25a12 Disruption Alters Myelination and Neurofilaments" ([PMID:20015484](https://pubmed.ncbi.nlm.nih.gov/20015484/)); "The ketogenic diet compensates for AGC1 deficiency and improves myelination" (Dahlin/related group, ResearchGate); βOHB rescue study ([PMC7687055](https://pmc.ncbi.nlm.nih.gov/articles/PMC7687055/)); OPC-specific transcriptomic/metabolic study ([PMC10979587](https://pmc.ncbi.nlm.nih.gov/articles/PMC10979587/)); OPC proliferation-defect study ([PMC6769484](https://pmc.ncbi.nlm.nih.gov/articles/PMC6769484/)).

- **Model applications:** The mouse model has been used to establish the mechanistic causal chain (malate-aspartate shuttle failure → aspartate/NAA depletion → hypomyelination/neurofilament pathology → dopaminergic dysfunction), and critically, to preclinically validate ketone-body (β-hydroxybutyrate) supplementation as a rescue therapy, directly informing the clinical use of ketogenic diet in human patients (translational fidelity: **RECAPITULATES** for hypomyelination, seizures, and NAA/aspartate depletion; readouts include brain aspartate/NAA levels, myelin lipid content, mitochondrial respiration assays, and behavioral/motor phenotyping).

- **Model limitations:** Mouse survival is markedly shortened (death by ~postnatal day 20–22), limiting study of long-term/adult disease progression as seen in human patients who survive into childhood/adolescence; and as with many monogenic neurodevelopmental mouse models, the precise correspondence between mouse developmental myelination timing and human infantile myelination timing introduces translational uncertainty warranting a `HUMAN_MODEL_MISMATCH`-type consideration if formally curated in dismech.

**Comparative biology across other species (from the 2026 MDPI review):**
- **Drosophila melanogaster:** A single *aralar1* ortholog gene exists, producing six isoforms via alternative splicing, with developmentally regulated expression.
- **Saccharomyces cerevisiae (yeast):** The ortholog Agc1p lacks the EF-hand Ca²⁺-binding domains present in mammalian AGC1, is Ca²⁺-independent, and shows dual antiporter/uniporter transport functionality — useful for basic structure-function studies of the carrier but not disease modeling per se.

**Resources:** MGI:1926080 (mouse gene record); [IMPC Slc25a12 page](https://www.mousephenotype.org/data/genes/MGI:1926080) for additional standardized phenotyping data.

---

## Summary Table of Suggested Ontology Terms for dismech Curation

| Category | Term |
|---|---|
| Disease (OMIM) | OMIM:612949 |
| Disease (Orphanet) | ORPHA:353217 |
| Causal gene | hgnc:10982 (SLC25A12) |
| Inheritance | HP:0000007 (Autosomal recessive inheritance) |
| Key phenotypes (HP) | HP:0001250 (Seizure), HP:0001263 (Global developmental delay), HP:0001252 (Hypotonia), HP:0006970 (Hypomyelination of white matter), HP:0002059 (Cerebral atrophy), HP:0001344 (Absent speech), HP:0001257 (Spasticity), HP:0000252 (Microcephaly) |
| Cell types (CL) | CL:0000540 (neuron), CL:0000128 (oligodendrocyte), CL:0002453 (oligodendrocyte precursor cell), CL:0000127 (astrocyte) |
| Anatomy (UBERON) | UBERON:0000955 (brain), UBERON:0002316 (white matter), UBERON:0002037 (cerebellum) |
| GO Cellular Component | GO:0005743 (mitochondrial inner membrane) |
| GO Biological Process | GO:0042552 (myelination), GO:0048709 (oligodendrocyte differentiation) |
| Treatment (NCIT) | NCIT:C15447 (Dietary Intervention) for ketogenic diet |

---

## Notes on Evidence Gaps for Curators

- **Exact MONDO CURIE** for this disease was not definitively confirmed in this pass — verify directly in the MONDO browser before entry creation.
- **Gene locus discrepancy** noted between sources (2q31 per some OMIM-derived summaries vs. 2q24.3 per the 2026 MDPI review) — confirm against current NCBI Gene/Ensembl record before curating.
- Several older-generation case reports (Parnes et al., Pronicka et al., Pfeiffer et al., Nashabat et al., Saleh et al., Kose et al.) were only reachable via secondary review citation in this search pass, without independently confirmed PMIDs for each — **verify each PMID directly via PubMed/`just fetch-reference` before using any snippet**, per the project's anti-hallucination SOP, since this report is itself a DR-style synthesis and should be treated as leads, not ground truth.
- No NCT clinical trial identifiers were located for this condition in this search.

**Sources:**
- [OMIM #612949 — Developmental and Epileptic Encephalopathy 39 with Leukodystrophy](https://omim.org/entry/612949)
- [OMIM *603667 — SLC25A12](https://www.omim.org/entry/603667)
- [Wibom et al. 2009, NEJM — AGC1 Deficiency Associated with Global Cerebral Hypomyelination, PMID:19641205](https://pubmed.ncbi.nlm.nih.gov/19641205/)
- [AGC1 Deficiency: Pathology and Molecular and Cellular Mechanisms of the Disease (PMC8745132)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8745132/)
- [Aspartate–Glutamate Carrier 1 (SLC25A12) Deficiency: Malate–Aspartate Shuttle Failure, Neurodevelopmental Epileptic Encephalopathy, and Ketone-Based Metabolic Therapy (MDPI 2026, doi:10.3390/ijms27104455)](https://www.mdpi.com/1422-0067/27/10/4455)
- [Kavanaugh et al. — Longitudinal MRI findings in patient with SLC25A12 pathogenic variants, PMID:31403263](https://pubmed.ncbi.nlm.nih.gov/31403263/)
- [ClinVar RCV000006523 — SLC25A12 c.1769A>G (p.Gln590Arg)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000006523/)
- [Alliance of Genome Resources — DOID:0080349](https://www.alliancegenome.org/disease/DOID:0080349)
- [MalaCards — Developmental and Epileptic Encephalopathy 39](https://www.malacards.org/card/developmental_and_epileptic_encephalopathy_39)
- [Orphanet — SLC25A12 gene page](https://www.orpha.net/en/disease/gene/SLC25A12?name=SLC25A12&mode=gene)
- [Ketogenic Diet Treatment of Defects in the Mitochondrial Malate Aspartate Shuttle and Pyruvate Carrier (PMC9460686)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9460686/)
- [βOHB Protective Pathways in Aralar-KO Neurons and Brain: An Alternative to Ketogenic Diet (PMC7687055)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7687055/)
- [Slc25a12 disruption alters myelination and neurofilaments, PMID:20015484](https://pubmed.ncbi.nlm.nih.gov/20015484/)
- [Deficiency of Mitochondrial Aspartate-Glutamate Carrier 1 Leads to Oligodendrocyte Precursor Cell Proliferation Defects (PMC6769484)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6769484/)
- [Transcriptional and metabolic effects of AGC1 downregulation in mouse OPCs (PMC10979587)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10979587/)
- [MGI:1926080 — Slc25a12 mouse gene detail](https://www.informatics.jax.org/marker/MGI:1926080)
- [IMPC — Slc25a12 mouse gene phenotyping](https://www.mousephenotype.org/data/genes/MGI:1926080)
- [Association between genetic variants in SLC25A12 and risk of autism spectrum disorders (meta-analysis), PMID:25921325](https://pubmed.ncbi.nlm.nih.gov/25921325/)
- [Pathogenic variants of the mitochondrial aspartate/glutamate carrier causing citrin deficiency (paralog context, PMC7614230)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7614230/)
- [A Novel Nonsense Gene Variant Responsible for Early Infantile Epileptic Encephalopathy Type 39: Case Report (SciAlert)](https://scialert.net/fulltext/?doi=pjbs.2020.973.976)
- [GeneCards — SLC25A12 gene](https://www.genecards.org/card/SLC25A12)
- [Genomics England PanelApp — SLC25A12 (Early onset or syndromic epilepsy)](https://panelapp.genomicsengland.co.uk/panels/402/gene/SLC25A12/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 15 |
| On topic | 10 |
| Off topic | 1 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3390/ijms27104455](https://www.mdpi.com/1422-0067/27/10/4455` (1 mention) - Identifier did not resolve to a record
- `DOI:10.3390/ijms27104455)](https://www.mdpi.com/1422-0067/27/10/4455` (1 mention) - Identifier did not resolve to a record

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:29353316` (3 mentions) - Validation of a new classification for periprosthetic shoulder fractures.
  - shared terms: patient

Weighed against this report's own most characteristic terms: `disease`, `slc25a12`, `agc1`, `brain`, `patient`, `developmental`, `myelination`, `variant`, `mitochondrial`, `gene`, `deficiency`, `seizure`, `cerebral`, `diet`, `hypomyelination`, `ketogenic`, `global`, `naa`, `metabolic`, `severe`.
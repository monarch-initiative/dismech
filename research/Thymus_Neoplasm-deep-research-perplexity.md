---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-14T13:09:18.348797'
end_time: '2026-08-14T13:13:51.866862'
duration_seconds: 273.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Thymus Neoplasm
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 21
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thymus Neoplasm
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Thymus Neoplasm** covering all of the
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

# Thymus Neoplasms: Comprehensive Characterization of Thymic Epithelial Tumors and Related Entities

Thymus neoplasms comprise a heterogeneous group of rare tumors arising in or around the thymus gland, of which thymic epithelial tumors—encompassing thymomas, thymic carcinomas, and thymic neuroendocrine tumors—are the most clinically significant in adults.[2][7] These tumors occupy a distinctive position at the intersection of oncology and clinical immunology, because the thymus is central to T‑cell development and self‑tolerance, and thymic tumors are strongly associated with paraneoplastic autoimmune syndromes such as myasthenia gravis, pure red cell aplasia, and hypogammaglobulinemia.[10][8][20] Despite their rarity, thymic epithelial tumors (TETs) have been the subject of increasingly sophisticated molecular, immunologic, and multi‑omics investigations, revealing a relatively quiet mutational landscape in thymomas dominated by a single recurrent GTF2I L424H driver mutation, contrasted with a more diverse, higher‑burden spectrum of TP53, CDKN2A/B, KIT, CYLD, and epigenetic regulator mutations in thymic carcinoma.[6][9][15] Epidemiologic studies indicate an incidence of approximately 0.13–0.32 per 100,000 person‑years in the general population, with higher rates in certain ethnic groups and geographic regions, and a typical age at diagnosis between 45 and 65 years.[3][1][2] Clinically, early‑stage thymomas are often curable with complete surgical resection, achieving 5‑year overall survival exceeding 90%, whereas invasive or metastatic thymomas and thymic carcinomas have significantly worse outcomes and require multimodality treatment including surgery, radiotherapy, systemic chemotherapy, and, increasingly, targeted and immunologic approaches.[2][1][18][16][4][9] At the mechanistic level, recent single‑cell and spatial transcriptomic studies have elaborated how thymoma‑associated myasthenia gravis arises from neuromuscular antigen expression in a specialized subset of medullary thymic epithelial cells (neuromuscular mTECs), ectopic germinal centers, and altered T‑ and B‑cell microenvironments within MG‑type thymomas.[20][8] This review synthesizes current knowledge across disease definition and nosology, etiology and risk, clinical phenotypes, molecular genetics and epigenetics, pathophysiology, anatomy, epidemiology, diagnostics, prognosis, treatment, prevention, comparative biology, and model systems, to provide a richly annotated, ontology‑linked description of thymus neoplasms suitable for disease knowledge base integration.

## 1. Disease Information

### 1.1 Definition and Scope of “Thymus Neoplasm”

In contemporary clinical and research practice, the term “thymus neoplasm” most commonly refers to primary tumors of the thymus gland, particularly thymic epithelial tumors (TETs), which include thymomas, thymic carcinomas, and neuroendocrine tumors of the thymus (NETTs).[2][7][1] Thymomas and thymic carcinomas arise from thymic epithelial cells and constitute the majority of thymus neoplasms in adult patients, while NETTs represent rare neuroendocrine variants that share an epithelial origin and anterior mediastinal localization.[2][5] Other neoplasms that may occur in the thymic region include lymphomas, germ cell tumors, and metastatic lesions; however, these are usually classified under their respective hematologic or germ cell entities rather than as “thymus neoplasms” per se. The National Library of Medicine’s MeSH descriptor “Thymus Neoplasms” defines the term broadly as “tumors or cancer of the thymus gland,” encompassing thymic cancer, thymic tumors, and thymic neoplasms as synonymous entry terms.[11] Clinically, the most frequent thymus neoplasms are thymomas and thymic carcinomas, which together account for less than 1% of all solid tumors but constitute the predominant primary tumors of the anterior mediastinum in adults.[3][15]

Orphanet describes thymoma as a “thymic epithelial neoplasm (TEN), a rare malignancy that arises from the epithelium of the thymic gland,” emphasizing its rarity and adult onset.[7] The Cleveland Clinic patient information similarly notes that thymomas and thymic carcinomas are “forms of cancer that start in a gland called your thymus,” located behind the breastbone in the anterior mediastinum, and that they represent the most frequently occurring tumors of the thymus despite being rare overall, with an estimated 400 diagnoses per year in the United States.[1] Taken together, “thymus neoplasm” in a disease knowledge base context is best conceptualized as an umbrella category (aligned to MONDO and MeSH) under which thymic epithelial tumors—thymoma, thymic carcinoma, and NETTs—are the primary entities, with explicit cross‑links to lymphoid and germ cell tumors that may secondarily involve the thymus.

### 1.2 Nosology, Classification, and Key Identifiers

Thymus neoplasms are richly annotated in major biomedical ontologies and classification systems, reflecting their recognized though rare status in oncology and clinical immunology. Orphanet lists thymoma under Orphanet disease number 99867, with ICD‑10 codes D15.0 (“benign neoplasm of thymus”) and D38.4 (“neoplasm of uncertain or unknown behavior of mediastinum”), and ICD‑11 code 2C27.Y (“Other specified malignant neoplasms of thymus”).[7] The associated OMIM entry for thymoma (OMIM: 274230) highlights the thymic epithelial origin and the lack of defined inheritance, consistent with a sporadic somatic neoplasm.[7] The MeSH heading “Thymus Neoplasms” (MeSH ID D013953) is placed in the neoplasms tree under C04.588.894.949 and in the respiratory system diseases tree under C15.604.861, with entry terms including “Thymic Cancer,” “Thymic Neoplasms,” “Thymic Tumors,” “Thymus Cancer,” and “Thymus Tumors.”[11] These identifiers provide robust semantic anchors for integrating thymus neoplasm knowledge across databases.

The 2021 World Health Organization (WHO) Classification of Tumors of the Thymus and Mediastinum provides a detailed histopathologic classification of thymic epithelial tumors.[5] Thymomas are categorized as type A, AB, and B thymomas, with type B further subdivided into B1, B2, and B3 subtypes based on the proportion and morphology of neoplastic epithelial cells and associated immature T lymphocytes.[5][15] Type A thymomas feature spindle or oval epithelial cells with few lymphocytes; type AB combine type A‑like areas with lymphocyte‑rich regions; type B1 resembles normal thymic cortex; type B2 displays more prominent epithelial cells among abundant lymphocytes; and type B3 consists predominantly of epithelial cells with only scattered lymphocytes.[5] Thymic carcinoma—historically designated “type C thymoma”—is now classified separately and encompasses several histologic variants, most commonly squamous cell carcinoma, as well as lymphoepithelioma‑like carcinoma, sarcomatoid carcinoma, and others.[5][15] Neuroendocrine tumors of the thymus (NETTs) include typical and atypical carcinoid tumors and large‑cell neuroendocrine carcinoma.[2][5]

The International Association for the Study of Lung Cancer (IASLC), in collaboration with other thoracic oncology groups, introduced a TNM‑based staging system for all types of thymic epithelial tumors in the eighth edition of the TNM classification of thoracic malignancies, harmonizing thymic tumor staging with other thoracic cancers.[14] Historically, the Masaoka–Koga staging system, based on local invasion and metastasis patterns, has been widely used; the TNM system refines these categories into T (tumor extent), N (nodal involvement), and M (metastatic spread), with specific definitions for pleural, pericardial, and pulmonary metastases.[14][18] These classification and staging systems are essential for defining disease stages, prognosis, and treatment algorithms.

Within the MONDO disease ontology, thymus neoplasm is represented as a distinct neoplastic entity under the broader neoplasm hierarchy, often linked to subterms such as “thymoma,” “thymic carcinoma,” and “thymic neuroendocrine tumor.” Although specific MONDO IDs are not provided in the search results, MONDO includes cross‑references to MeSH D013953, OMIM:274230, Orphanet:99867, and ICD codes, enabling semantic integration across resources. In a knowledge base implementation, “Thymus Neoplasm” would be mapped to this MONDO concept and further subclassed into thymoma, thymic carcinoma, and NETTs, with links to SNOMED CT concepts such as “Thymus gland carcinoma (disorder)” and “Thymoma (disorder),” and to NCIT terms like NCIT:C3008 (Thymoma) and NCIT:C4872 (Thymic Carcinoma).

### 1.3 Synonyms, Terminology, and Data Source Characteristics

Common synonyms and alternative names for thymus neoplasms include “thymic epithelial tumors,” “thymic tumors,” “thymoma,” “thymic carcinoma,” “thymus cancer,” and “cancer of the thymus.”[2][11][1] In the clinical literature, “TETs” is often used as a shorthand for thymic epithelial tumors, encompassing thymomas, thymic carcinomas, and thymic neuroendocrine tumors.[2][17][10] Patient‑facing resources frequently use “thymus cancer” or “thymoma” interchangeably when discussing thymic tumors, although technically thymoma and thymic carcinoma differ substantially in histology, biology, and clinical behavior.[1][2] The Orphanet entry emphasizes “thymoma” as the archetypal thymic epithelial neoplasm.[7] The MeSH descriptor “Thymus Neoplasms” notes entry terms such as “Thymic Neoplasms,” “Thymic Tumors,” “Thymus Cancer,” and “Cancer of the Thymus,” reflecting variation in everyday usage.[11]

Most information on thymus neoplasms in the scientific literature is derived from aggregated disease‑level resources rather than individual electronic health records, owing to the rarity of the disease and the need to combine cases across institutions and time periods. Epidemiologic data, such as incidence and survival statistics, come primarily from national cancer registries like the U.S. Surveillance, Epidemiology, and End Results (SEER) program, pan‑European registries, and large retrospective cohort studies.[3][2] Clinical management recommendations derive from consensus guidelines such as the National Comprehensive Cancer Network (NCCN) Guidelines for Thymomas and Thymic Carcinomas (Version 2.2025) and national expert consensus statements (e.g., the 2023 Chinese expert consensus).[4][15] Mechanistic insights into autoimmunity, immunopathology, and molecular drivers derive from laboratory‑based studies using tumor specimens, single‑cell transcriptomics, spatial transcriptomics, and experimental models.[6][20][8][12][19] Collectively, these aggregated data sources provide robust evidence for disease‑level knowledge models, although individual variability remains significant and must be considered in clinical decision support applications.

## 2. Etiology, Risk, and Protective Factors

### 2.1 Current Understanding of Etiology

The etiology of thymus neoplasms, and thymic epithelial tumors in particular, remains incompletely understood. Orphanet explicitly states that the etiology of thymoma is unknown and that no clear genetic or environmental factors have been identified as causative.[7] The Cleveland Clinic similarly notes that there are “no known genetic or environmental risk factors for thymoma,” and that research is ongoing to look for links to viruses, heredity, and other cancers.[1] A 2020 epidemiologic review emphasizes that thymoma is a rare malignancy representing only 0.2–1.5% of all malignancies and that environmental exposures such as tobacco, radiation, alcohol, or diet appear to be irrelevant based on current evidence.[3] This review further notes that there does not appear to be a significant increased likelihood of thymoma following other malignancies, and that, conversely, survival from thymoma does not entail a markedly increased risk of subsequent malignancies except possibly non‑Hodgkin lymphoma.[3]

At the mechanistic level, thymic epithelial tumors are largely characterized by somatic, rather than germline, genetic and epigenetic alterations that arise in thymic epithelial cells and confer neoplastic transformation.[2][6][9][12][19] Thymomas typically exhibit a relatively low somatic mutational burden, with the exception of a recurrent missense mutation (L424H) in the GTF2I gene, which appears to function as a lineage‑specific oncogene.[6][15] Thymic carcinomas, by contrast, harbor a more complex mutational landscape, with frequent alterations in tumor suppressors such as TP53 and CDKN2A/B, the signaling regulator CYLD, the receptor tyrosine kinase KIT, and multiple epigenetic regulators including TET2, SETD2, BAP1, and ASXL1.[9][15] Epigenetic dysregulation, including promoter hypermethylation and global hypomethylation, and non‑coding RNA changes, notably miR‑145‑5p, also appear to play important roles in thymic epithelial tumorigenesis.[12][19] Infectious agents, particularly Epstein–Barr virus (EBV), have been implicated in thymic carcinomas with lymphoepithelioma‑like morphology, although the causal role of EBV in thymoma remains controversial.[3][13]

Thus, thymus neoplasms—especially thymic epithelial tumors—are best conceptualized as sporadic, somatically driven cancers arising in thymic epithelial cells in adults, with no established germline predisposition syndrome and limited evidence for direct environmental causation. Molecular studies increasingly point to specific somatic drivers and epigenetic patterns that define tumor subtypes and influence clinical behavior, whereas epidemiologic studies suggest modest demographic patterns but no strong modifiable risk factors.

### 2.2 Genetic Risk Factors and Somatic Driver Mutations

No Mendelian germline genetic syndromes have been firmly established as causal for thymoma or thymic carcinoma, and familial clustering of thymic epithelial tumors appears rare. Most genetic risk information for thymus neoplasms therefore relates to somatic driver mutations within the tumor, which are critical for pathogenesis but do not necessarily translate into inherited susceptibility. In thymomas, multiple studies have shown that somatic mutations are generally infrequent, with the exception of GTF2I, which is common particularly in type A and AB thymomas.[6][15][12] A 2023 somatic mutation study focusing on thymic epithelial tumors associated with myasthenia gravis reported that GTF2I was the only significantly recurrent mutation identified in their cohort, with 14 GTF2I mutations in 6 type A, 5 AB, and 2 B2 thymomas, and one thymoma of unspecified histology.[6] The most common mutation was the missense L424H variant, which is described as “unique to this type of neoplasm” and has been functionally validated as an oncogene using CRISPR/Cas9 knock‑in in murine thymic epithelial cells, which acquire tumor‑forming ability in nude mice.[6]

In a larger compilation, the most commonly mutated genes across thymic epithelial tumors included GTF2I (55 patients), TP53 (31), HRAS (18), TTN (11), and BAP1, CDKN2A, and CYLD (10 each), reflecting a spectrum that differs between thymomas and thymic carcinomas.[6] GTF2I mutations are more frequently seen in A and AB thymomas, whereas TP53 mutations are more typical of thymic carcinomas and B3 thymomas.[6] The allele frequency of GTF2I mutations is reported to range from 4% to 22% in sequencing assays, due to dilution by non‑tumoral thymocytes and stromal cells in thymoma specimens.[6] Studies demonstrate that thymomas express only specific GTF2I isoforms (2 and 4), consistent with a lineage‑restricted functional role.[6]

Thymic carcinomas exhibit a distinct somatic mutation profile compared with thymomas, characterized by higher tumor mutational burden (TMB) and a greater prevalence of mutations in TP53, CDKN2A/B, CYLD, KIT, and epigenetic regulators.[9][15] A genomic profiling review compiling multiple whole‑exome sequencing and targeted sequencing studies found that the most frequently reported genes in thymic carcinoma were TP53, CDKN2A, CDKN2B, CYLD, KIT, TET2, SETD2, BAP1, ASXL1, and FGFR3.[9] The largest targeted sequencing cohort of thymic epithelial tumors suggested that CDKN2A, CDKN2B, and TP53 alterations were significantly more frequent in thymic carcinoma than in thymoma.[9][15] Copy‑number analyses from The Cancer Genome Atlas (TCGA) project revealed that chromosome 16q loss is more common in thymic carcinoma than in thymoma, whereas chromosome 1q amplification and 6p/6q loss are shared across both entities.[9] Thymic carcinomas also exhibit higher TMB than thymomas, with reported elevated TMB in approximately 6–7% of thymic carcinoma cases, occasionally reflecting mismatch repair deficiency, as in a TCGA patient with a pathogenic MLH1 nonsense mutation and high TMB resembling COSMIC signature 6.[9]

While these somatic mutations do not generally represent inherited risk factors, their presence has prognostic and therapeutic relevance. TP53 and CDKN2A mutations in thymic carcinoma are correlated with poor prognosis, reflecting aggressive tumor biology.[9] KIT mutations may enable targeted therapy with tyrosine kinase inhibitors, although clinical responses in thymic carcinoma have been variable.[9][15] CYLD, a negative regulator of NF‑κB signaling that also interacts with AIRE expression and T‑cell development, has been proposed as a biomarker of immunotherapy response, linking molecular pathogenesis to immune mechanisms.[9] Epigenetic regulator mutations suggest widespread disruption of chromatin and DNA methylation landscapes in thymic carcinoma, which may underlie genomic instability and altered gene expression.[9][12]

In summary, genetic risk for thymus neoplasms is primarily embodied in somatic driver and modifier mutations in thymic epithelial cells, especially GTF2I in indolent thymomas and TP53/CDKN2A/B/CYLD/KIT/epigenetic regulators in thymic carcinoma. Knowledge bases should therefore distinguish between germline risk (currently minimal) and somatic pathogenic variants (central to disease definition and management).

### 2.3 Environmental, Infectious, and Lifestyle Risk Factors

Epidemiologic studies have found no robust associations between thymus neoplasms and common environmental or lifestyle exposures, such as tobacco smoking, alcohol use, diet, or occupational hazards. The 2020 epidemiology review explicitly states that environmental exposures including tobacco, radiation, alcohol, or diet “seem to be irrelevant,” and that there are no published data demonstrating a link between tobacco, alcohol, diet, and thymoma.[3] Similarly, there are no clear occupational exposures or geographic environmental factors consistently associated with increased thymoma risk.[3] The absence of coherent environmental risk signals is striking compared with many other solid tumors and reinforces the view of thymic epithelial tumors as primarily sporadic neoplasms without established modifiable etiologic factors.

Age is a significant non‑modifiable risk factor, as thymic epithelial tumors are predominantly diseases of middle‑aged and older adults, with incidence peaking between 45 and 75 years depending on cohort.[3][2][1][7] Thymomas and thymic carcinomas are rare in young adults, and pediatric cases are exceptional and may represent distinct biological entities.[3] Sex does not appear to strongly influence thymoma risk; most evidence suggests no significant sex difference, although some series report slight male or female predominance.[3] By contrast, paraneoplastic autoimmune syndromes such as myasthenia gravis are more common in women with thymoma, reflecting the general sex bias of autoimmune diseases.[10]

Race and ethnicity exhibit modest but reproducible differences in thymoma incidence. Using SEER data from 1973–1998, Engels and colleagues reported higher incidence of thymic cancers among Black and “Other” ethnic groups compared with Caucasians, with rates of 0.2 per 100,000 in Blacks, 0.29 per 100,000 in other races, and 0.13 per 100,000 in Caucasians.[3] Subsequent analyses demonstrated an incidence of 0.25 per 100,000 in Asian and Pacific Islanders, with variation among Japanese, Vietnamese, Filipino, Chinese, and Korean subgroups.[3] These SEER data also indicated that the age at diagnosis varies with ethnicity, with Black patients presenting earlier (median age 48 years) than Caucasians (58 years) or Asian/Pacific Islanders.[3] Geographic variation within Europe has also been described, with higher incidence rates in Central (1.9 per million per year) and Southern Europe (2.3 per million per year) compared with Northern (0.9 per million), Eastern Europe (1.2 per million), and the UK/Ireland (1.1 per million).[3] These patterns suggest complex interactions between genetic background, healthcare access, and possibly environmental factors, although specific causal exposures have not been identified.

Infectious agents, particularly Epstein–Barr virus (EBV), have been extensively studied in relation to thymic epithelial tumors. EBV is well known to be associated with several tumors, including Burkitt lymphoma, nasopharyngeal carcinoma, EBV‑associated gastric carcinoma, and lymphoepithelioma‑like carcinomas in different organs.[13] The association between EBV and thymic epithelial tumors has been controversial, with earlier studies, often using in situ hybridization (ISH), concluding that EBV was associated with thymic carcinoma but not thymoma.[13][3] A 2023 study using nested PCR and EBER ISH tested 15 thymic carcinomas and multiple thymomas and found that 14 of 15 (93.3%) thymic carcinomas were positive for EBV by nested PCR, with three showing weak nuclear signals within tumor cells by EBER ISH.[13] The authors observed that as the malignancy of thymoma increased, the rate of EBV infection became higher, and concluded that “thymic carcinomas were well associated with the Epstein–Barr virus,” with a significant association between EBV infection rate and thymoma type.[13] However, the role of EBV in thymic tumor oncogenesis remains unsettled, with potential geographic and methodological differences influencing study results.[13][3] In knowledge base terms, EBV infection should be recognized as a strong association for thymic carcinoma, particularly lymphoepithelioma‑like variants, but not yet as a proven causal factor for thymoma.

Lifestyle factors such as smoking, alcohol, and diet, as noted, have no established influence on thymus neoplasm risk, and no preventive lifestyle recommendations can be specifically made for thymoma or thymic carcinoma beyond general cancer prevention guidelines.[3][1][15] Similarly, ionizing radiation exposure has not been clearly linked to thymic epithelial tumors, although thymic lymphoma risk may be increased by mediastinal radiation in other contexts. Thus, environmental and lifestyle data on thymus neoplasms are largely negative, reinforcing their characterization as rare sporadic tumors with limited modifiable risk factors.

### 2.4 Protective Factors and Gene–Environment Interactions

Because clear environmental or lifestyle risk factors for thymus neoplasms have not been identified, it follows that empirically defined protective factors are also lacking. There is no evidence that specific diets, physical activity patterns, or avoidance of particular exposures reduce the risk of developing thymoma or thymic carcinoma beyond general cancer prevention recommendations.[3][1][15] No genetic “protective variants” have been reported that confer reduced risk of thymic epithelial tumors in population‑level studies, and genome‑wide association studies have not yet defined common susceptibility or protective loci specific to thymic tumors.

One intriguing and somewhat paradoxical observation is that paraneoplastic autoimmune syndromes in thymic epithelial tumor patients—especially myasthenia gravis and related PN/AI syndromes—are associated with certain favorable tumor features. A 2017 study by Padda et al. examining paraneoplastic autoimmune (PN/AI) syndromes in thymic malignancies found that PN/AI syndromes were associated with younger age, female sex, type B1 thymoma, earlier stage, and an increased rate of total thymectomy and complete resection.[10] They reported a significantly lower cumulative incidence of recurrence in the PN/AI‑positive group compared to the PN/AI‑negative group (10‑year recurrence 17.3% vs. higher in PN/AI‑negative), and noted that PN/AI status was not an independent prognostic factor for recurrence‑free survival or overall survival, but nonetheless was associated with more favorable tumor characteristics.[10] These findings suggest that the presence of autoimmune manifestations may serve as a “sentinel” of certain thymoma subtypes that are more likely to be detected earlier and completely resected, indirectly improving outcomes. However, PN/AI syndromes also impose substantial morbidity and are not protective in any intentional sense.

Gene–environment interactions in thymus neoplasms have not been systematically characterized. It is plausible that host genetic factors influencing immune regulation, thymic epithelial cell biology, or viral responses could modulate the impact of environmental exposures such as EBV infection or other infections on thymic tumor risk, but direct evidence is limited. The CYLD gene, which regulates NF‑κB signaling and interacts with AIRE expression and T‑cell development, has been highlighted as a candidate mediator of immunotherapy response in thymic carcinoma and as a link between tumor genomic status and immune microenvironment.[9] Similarly, genome‑wide association studies in myasthenia gravis have implicated medullary thymic epithelial cell (mTEC) genes and T‑cell regulatory pathways in autoimmune susceptibility,[8][20] suggesting that host genetic background may influence the development of thymoma‑associated autoimmunity. Nonetheless, explicit gene–environment interactions in thymic epithelial tumor initiation remain an open research area.

From a knowledge base perspective, thymus neoplasms should thus be annotated as sporadic neoplastic diseases with unknown primary causation; somatic driver mutations (GTF2I, TP53, CDKN2A/B, etc.) and EBV infection in thymic carcinoma are key molecular and infectious features rather than “risk factors” per se; and protective factors and gene–environment interactions are currently speculative and not suitable for evidence‑based risk modeling.

## 3. Clinical Phenotypes and Paraneoplastic Syndromes

### 3.1 Primary Tumor‑Related Phenotypes: Symptoms, Signs, and Course

The clinical phenotypes of thymus neoplasms arise from three interrelated domains: local mass effects of the anterior mediastinal tumor, systemic effects of paraneoplastic autoimmunity, and manifestations of advanced metastatic disease. Primary tumor‑related symptoms and signs reflect the location of the thymus in the anterior mediastinum, just behind the sternum, and the tendency of thymic epithelial tumors to grow slowly and remain asymptomatic until they reach a size sufficient to compress adjacent structures. The Cleveland Clinic notes that thymomas and thymic carcinomas “usually don’t cause symptoms at first,” and that when symptoms are present they may include chest pressure or chest pain.[1] Other common mass‑effect symptoms, though not explicitly listed in the search results, typically include cough, dyspnea, and, less often, hoarseness or superior vena cava syndrome if the tumor compresses the airway, lungs, or major vessels. Many thymomas are discovered incidentally on imaging performed for other reasons, reflecting their indolent growth and mediastinal location.[2][15]

Imaging phenotypes are central to the recognition of thymus neoplasms. The 2023 Chinese expert consensus recommends enhanced chest computed tomography (CT) with mediastinal windows as the preferred imaging modality for thymic tumors, noting that CT can examine the extent of tumor lesions, detect peripheral tissue infiltration and distant metastasis, and predict tumor stage.[15] On CT, thymomas typically appear as well‑circumscribed anterior mediastinal masses, sometimes with lobulated contours or calcifications; thymic carcinomas more often show invasive borders, necrosis, or heterogeneous enhancement, reflecting their more aggressive biology.[15] Magnetic resonance imaging (MRI) is valuable in cases where CT diagnosis is unclear, especially for evaluating invasion into surrounding fat and distinguishing malignant thymic tumors from thymic cysts or thymic hyperplasia.[15] Positron emission tomography/CT (PET‑CT) demonstrates relatively higher accuracy in differentiating benign from malignant thymic masses and can predict malignancy to an extent based on standardized uptake values, while also evaluating distant and systemic metastases in advanced tumors.[15] These imaging features correspond to Human Phenotype Ontology (HPO) terms such as “Anterior mediastinal mass” (HP:0005260), “Chest pain” (HP:0100749), and “Dyspnea” (HP:0002094).

The age of symptom onset typically falls in adulthood, most often between 40 and 75 years, consistent with epidemiologic distributions.[1][2][3][7] Symptom severity and progression are variable, depending largely on tumor size, growth rate, and invasion into adjacent structures. Indolent thymomas may remain stable for years and cause minimal symptoms, whereas invasive thymomas and thymic carcinomas can progress relatively rapidly, producing worsening dyspnea, chest pain, and systemic effects. Symptoms generally progress in a chronic, insidious pattern rather than having an acute onset, except in cases of sudden complications such as pericardial tamponade or large pleural effusions. The frequency of specific symptoms among affected individuals varies across cohorts and subtypes; approximately 30–50% of thymoma patients may present with symptoms related to paraneoplastic autoimmunity (especially myasthenia gravis), while others present with mass effect symptoms or incidentally.[10][8][1]

Quality of life impact from primary tumor‑related phenotypes includes limitations in physical functioning due to dyspnea or chest pain, anxiety related to malignancy diagnosis, and postoperative pain and recovery after thymectomy. While formal quality‑of‑life studies specific to thymic tumors are limited, analogies with other thoracic malignancies suggest that SF‑36 domains such as physical functioning, role physical, and vitality may be significantly affected during active disease and treatment, with improvement after complete resection in early‑stage thymomas. HPO terms relevant to quality‑of‑life impact include “Fatigue” (HP:0012378), “Exercise intolerance” (HP:0003546), and “Anxiety” (HP:0000739).

### 3.2 Autoimmune and Paraneoplastic Phenotypes

Thymic epithelial tumors are remarkable for their strong association with paraneoplastic autoimmune syndromes arising from dysregulated T‑cell development and self‑tolerance in the tumor‑affected thymus. Myasthenia gravis (MG) is the most common paraneoplastic autoimmune syndrome associated with thymomas and thymic carcinomas.[10][8][20] Padda et al. summarize that 10–20% of patients with MG have a thymoma, and approximately 30% of patients with thymoma either present with or eventually develop MG.[10] MG results from autoantibodies against neuromuscular junction components, most commonly acetylcholine receptor (AChR) antibodies, leading to fluctuating muscle weakness and fatigability.[10][8][20] Other paraneoplastic autoimmune and hematologic syndromes associated with thymic epithelial tumors include pure red cell aplasia (PRCA), hypogammaglobulinemia (Good’s syndrome), and a spectrum of systemic autoimmune diseases such as systemic lupus erythematosus, polymyositis, and others, often reported in case series.[10]

The frequency of MG varies by thymoma histologic subtype. A narrative review of thymoma‑associated MG notes that MG is rare in type A thymomas but relatively common in type B thymomas, especially type B2, with reported frequencies ranging from 24% to 71% of cases.[8] Type B1 and B3 thymomas show MG frequencies of 7–70% and 25–65%, respectively, in different series.[8] These patterns reflect differences in thymic epithelial cell architecture, T‑cell maturation, and antigen presentation across subtypes. The pathogenesis of thymoma‑associated MG involves multiple mechanisms, including ectopic expression of neuromuscular antigens (e.g., neurofilament proteins), production of immature T cells lacking sufficient self‑tolerance, decreased regulatory T cells (Tregs), and impaired negative selection due to AIRE deficiency, reduced human leukocyte antigen (HLA) expression, and CTLA‑4 overexpression.[8][20] Yasumizu et al. used bulk and single‑cell RNA sequencing with spatial transcriptomics to construct a comprehensive atlas of MG‑type thymoma, identifying a distinct subpopulation of medullary thymic epithelial cells—neuromuscular mTECs (nmTECs)—that ectopically express neuromuscular molecules such as NEFM, RYR3, and GABRA5 and reside within microenvironments dedicated to autoantibody production, including ectopic germinal centers, T follicular helper cell aggregates, and migrating type 2 conventional dendritic cells.[20][8]

In their abstract, Yasumizu and colleagues state:

> “Here, by constructing a comprehensive atlas of thymoma using bulk and single‑cell RNA‑sequencing, we identify ectopic expression of neuromuscular molecules in MG‑type thymoma. These molecules are found within a distinct subpopulation of medullary thymic epithelial cells (mTECs), which we name neuromuscular mTECs (nmTECs). MG‑thymoma also exhibits microenvironments dedicated to autoantibody production, including ectopic germinal center formation, T follicular helper cell accumulation, and type 2 conventional dendritic cell migration.”[20]

This mechanistic insight provides a causal chain linking thymic epithelial tumor architecture, antigen expression, immune cell recruitment, and autoantibody production, explaining how thymoma‑associated MG emerges from the altered thymic microenvironment.

Paraneoplastic autoimmune syndromes have major quality‑of‑life impacts. MG causes fluctuating weakness affecting ocular, bulbar, and limb muscles, often limiting daily activities and requiring chronic immunosuppressive treatment, acetylcholinesterase inhibitors, and, in severe cases, plasmapheresis or intravenous immunoglobulin.[10][8] Pure red cell aplasia leads to severe anemia and fatigue due to selective erythroid lineage suppression.[10] Hypogammaglobulinemia predisposes to recurrent infections and requires immunoglobulin replacement. These syndromes correspond to HPO terms such as “Myasthenia gravis” (HP:0003258), “Autoimmune hemolytic anemia” (HP:0001890) or “Pure red cell aplasia” (HP:0004810), and “Hypogammaglobulinemia” (HP:0004313). The presence of PN/AI syndromes often complicates oncologic management because immunosuppressive therapy may interact with chemotherapy or immunotherapy, and treatments such as immune checkpoint inhibitors may exacerbate autoimmunity.

Interestingly, Padda et al. found that PN/AI syndromes were associated with favorable thymic tumor features, including earlier stage and higher rates of complete resection, but that PN/AI status was not an independent predictor of overall survival.[10] They concluded:

> “We found PN/AI syndromes to be associated with favorable features such as younger age, type B1 thymoma, earlier stage, and increased rate of complete resection status. However, the presence of PN/AI syndrome was not an independent prognostic factor for TETs for either RFS or OS. Importantly, our study confirms prior national database studies that PN/AI syndrome status (represented by MG in these studies) is not an independent factor associated with OS.”[10]

These conclusions underscore the need to treat autoimmunity and tumor disease as partially separable domains, albeit interconnected through thymic pathophysiology.

### 3.3 Laboratory and Imaging Phenotypes, Including Paraneoplastic Abnormalities

Laboratory phenotypes in thymus neoplasms reflect both paraneoplastic autoimmune manifestations and general tumor‑related effects. In MG‑associated thymoma, serologic detection of AChR antibodies is common, and anti‑AChR titers often correlate with disease activity.[10][8][20] Other autoantibodies, such as anti‑MuSK or anti‑LRP4, may be present in seronegative MG, but their specific association with thymoma is less clear. In PRCA, laboratory findings include severe normocytic anemia with markedly reduced reticulocyte counts and near‑absence of erythroid precursors in bone marrow. Hypogammaglobulinemia manifests as low immunoglobulin G, A, and/or M levels, often with reduced vaccine responses and increased infection frequency.[10] These phenotypes map to HPO terms such as “Autoantibodies” (HP:0002976), “Anemia” (HP:0001903), “Decreased serum IgG” (HP:0004315), and “Recurrent infections” (HP:0002719).

Imaging phenotypes have been discussed in Section 3.1 but are also important in the context of paraneoplastic syndromes. For example, thymic hyperplasia in MG without thymoma can present as a diffuse enlargement of the thymus on imaging but lacks the discrete mass of a thymoma. The 2023 Chinese consensus notes that MRI can accurately distinguish malignant thymic tumors from thymic cysts or thymic hyperplasia, thus avoiding unnecessary thymectomy in MG patients without thymoma.[15] PET‑CT may help differentiate hypermetabolic thymic carcinoma or invasive thymoma from less active benign lesions, and can detect pleural or pericardial nodules and distant metastases, corresponding to TNM M1a and M1b stages.[15][17] These imaging features correspond to HPO terms such as “Abnormality of the anterior mediastinum” (HP:0005260) and “Pulmonary nodules” (HP:0006528).

Electrophysiologic phenotypes are relevant in MG: repetitive nerve stimulation and single‑fiber electromyography (EMG) demonstrate decrements in compound muscle action potentials and increased jitter consistent with neuromuscular transmission failure. Although these tests are not specific for thymoma, their correlation with AChR antibody status and thymic pathology is clinically important. Functional tests such as pulmonary function testing may demonstrate restrictive ventilatory defects due to mediastinal mass effect or MG‑related respiratory muscle weakness.

### 3.4 Quality of Life Impact Across Phenotypes

The quality of life impact of thymus neoplasms is multimodal, arising from tumor burden, treatment effects, and co‑existing autoimmunity. Early‑stage thymomas treated with complete thymectomy may result in relatively preserved long‑term quality of life, although surgical sternotomy, postoperative pain, and potential long‑term pulmonary or cardiac effects from radiotherapy can impair physical functioning.[18][1] Advanced thymomas and thymic carcinomas, requiring multimodality therapy with chemotherapy, radiotherapy, and sometimes repeated surgeries, can significantly reduce physical and role functioning, increase fatigue, and cause psychological distress.

Myasthenia gravis in thymoma patients is particularly impactful. Fluctuating muscle weakness, diplopia, ptosis, dysphagia, and respiratory compromise can severely limit daily activities, work capacity, and social participation. Chronic immunosuppressive therapy with corticosteroids, azathioprine, or other agents, as well as repeated courses of plasmapheresis or IVIG, impose additional burdens. Hypogammaglobulinemia necessitating regular IVIG infusions, and PRCA requiring repeated blood transfusions, add to treatment intensity. These factors align with quality‑of‑life instruments such as EQ‑5D, SF‑36, and disease‑specific MG scales, which would likely show impairments in mobility, self‑care, usual activities, pain/discomfort, and anxiety/depression domains, as well as decreased physical and social functioning scores.

From a knowledge base standpoint, HPO terms such as “Chronic fatigue” (HP:0012378), “Asthenia” (HP:000 asthenia), “Exercise intolerance” (HP:0003546), and “Depressed mood” (HP:0000716) should be associated with thymus neoplasm entities via paraneoplastic syndromes. On the intervention side, NCIT terms for supportive care, physical rehabilitation, and psychotherapy can be linked to amelioration of these quality‑of‑life impacts.

## 4. Genetic and Molecular Landscape

### 4.1 Somatic Mutational Spectrum in Thymomas

The molecular profile of thymomas is characterized by a relatively low somatic mutational burden and a striking prevalence of a single recurrent driver mutation in the GTF2I gene, particularly in type A and AB thymomas. A 2023 study investigating somatic mutations in thymic epithelial tumors associated with myasthenia gravis found that “only GTF2I mutations were found to be significantly recurrent” in their cohort, highlighting the dominant role of this gene in thymoma pathogenesis.[6] They reported 14 GTF2I mutations distributed among 6 type A, 5 AB, 2 B2 thymomas, and one thymoma of unspecified histology.[6] The most common mutation observed was the missense L424H variant, which was described as “unique to this type of neoplasm” in the reviewed literature.[6] GTF2I mutation was present in 21% of analyzed thymic epithelial tumors overall, with 50% of type A thymomas and 38% of AB thymomas harboring this mutation.[6]

Functionally, the L424H mutation in GTF2I, located on chromosome 7, leads to a leucine‑to‑histidine substitution in the second conserved TFII‑I repeat domain of the protein, near the DNA binding site.[6] There are six known isoforms of GTF2I, but thymomas express only isoforms 2 (Beta) and 4 (Delta), according to RNA sequencing.[6] CRISPR/Cas9 knock‑in of the Gtf2i L424H mutation into murine immortalized thymic epithelial cells resulted in neoplastic transformation, with cells acquiring the ability to form tumors when transplanted subcutaneously in nude mice, demonstrating that L424H‑mutated GTF2I functions as an oncogene.[6] These findings position GTF2I as a pivotal molecular driver in thymoma, akin to lineage‑defining oncogenes in other cancers.

Beyond GTF2I, thymomas exhibit occasional somatic mutations in genes such as HRAS, TP53, and others, but these are less frequent than in thymic carcinoma.[6][15] The Chinese consensus summarizes that type AB thymomas may harbor chromosomal deletions (e.g., 5q21–22, 6p21, 6q25.2–25.3, 7p15.3, 8p, 13q14.3, 16q, 18) and mutations in genes such as GTF2I, TP53, HRAS, EGFR, STK11, SMARCB1, TET2, PDGFRA, and RUNX1.[15] However, the overall mutational load in thymomas remains low compared with many solid tumors, and many thymomas have relatively “quiet” genomes with few recurrent mutations beyond GTF2I.

The biological consequences of GTF2I mutation likely involve altered transcriptional regulation of genes controlling thymic epithelial cell proliferation, differentiation, and interactions with thymocytes. Gene Ontology (GO) terms relevant to GTF2I function include “DNA‑binding transcription factor activity” (GO:0003700), “regulation of transcription by RNA polymerase II” (GO:0006357), and “response to growth factor stimulus” (GO:0070848). The presence of GTF2I mutations correlates with indolent clinical behavior and favorable prognosis; GTF2I‑mutated tumors often display low stage and low recurrence rates, and surgery is curative in most cases.[6] Currently, there is no drug able to inhibit mutated GTF2I, and targeted therapies against this specific oncogene are not available.[6]

Knowledge bases should thus annotate GTF2I L424H as a somatic, pathogenic, gain‑of‑function variant in thymoma, with HGNC ID for GTF2I and appropriate ClinVar classification when available. Variant type is missense; functional consequence is gain of function; origin is somatic; and clinical significance includes diagnostic value (distinguishing thymoma from other mediastinal tumors) and prognostic association with indolent disease.

### 4.2 Genomic Features of Thymic Carcinoma

Thymic carcinoma differs markedly from thymoma in its genomic landscape, displaying higher tumor mutational burden, more frequent chromosomal aberrations, and a broader array of driver and modifier mutations. The genomic profiling review by Zhao et al. synthesizes multiple whole‑exome and targeted sequencing studies and concludes that “thymic carcinoma demonstrates a unique genomic landscape, suggesting a molecular pathogenesis distinct from that of thymoma.”[9] They identify TP53, CDKN2A, CDKN2B, CYLD, KIT, TET2, SETD2, BAP1, ASXL1, and FGFR3 as the most frequently reported genes in thymic carcinoma across studies.[9] TP53 and CDKN2A alterations are particularly noteworthy, as they correlate with poor prognosis and likely reflect disruptions in cell‑cycle control and DNA damage responses.[9]

Several studies in their compilation highlight specific mutation patterns. For example, Saito et al. (2017) reported TET2, ARID1B, CYLD, and SETD2 mutations in a cohort of Japanese thymic carcinomas using whole‑exome sequencing.[9] Radovich et al. (2018) identified TP53 and NRAS mutations in a small U.S. cohort.[9] Wang et al. (2014) reported TP53, BAP1, CYLD, KIT, DNMT3A, SETD2, and TET3 mutations in 42 thymic carcinoma cases using targeted sequencing.[9] Moreira et al. (2015) found TP53, KDM6A, SMAD4, CYLD, SETD2, KMT2C, and KMT2D mutations in 15 thymic carcinoma patients.[9] Later studies up to 2023 continue to refine this spectrum, with recurrent emphasis on TP53, CDKN2A/B, CYLD, KIT, and epigenetic regulators.[9][15]

Copy‑number aberrations in thymic carcinoma include frequent chromosome 16q loss, more common than in thymoma, and shared aberrations with thymoma such as 1q amplification and 6p/6q loss.[9][15] TMB is consistently higher in thymic carcinoma than in thymoma, with several reports indicating elevated TMB in 6–7% of thymic carcinoma cases.[9] One TCGA case demonstrated an unusually high TMB with a mutational pattern similar to COSMIC signature 6, associated with mismatch repair deficiency, and carried a pathogenic MLH1 nonsense mutation with loss of MLH1 expression.[9] These features suggest that a subset of thymic carcinomas may arise via hypermutator pathways and could potentially respond to immune checkpoint blockade, although clinical evidence is still emerging.

The functional roles of key thymic carcinoma genes include: TP53 (tumor suppressor controlling cell cycle arrest and apoptosis; GO:0008285 “negative regulation of cell proliferation”), CDKN2A/B (cyclin‑dependent kinase inhibitors regulating G1/S transition; GO:0000082 “G1/S transition of mitotic cell cycle”), CYLD (deubiquitinase inhibiting NF‑κB signaling and modulating immune responses; GO:0061187 “regulation of NF‑κB transcription factor activity”), KIT (receptor tyrosine kinase mediating cell proliferation and survival via MAPK and PI3K pathways; GO:0007169 “transmembrane receptor protein tyrosine kinase signaling pathway”), and epigenetic regulators TET2, SETD2, BAP1, ASXL1 (which modulate DNA methylation and histone modification). Mutations in these genes confer growth advantages, resistance to apoptosis, and possibly altered interactions with the immune microenvironment.

From a clinical and knowledge base perspective, these thymic carcinoma mutations have distinct implications. TP53 and CDKN2A/B mutations should be annotated as somatic, pathogenic, loss‑of‑function variants associated with poor prognosis. KIT mutations may be flagged as potential targets for tyrosine kinase inhibitors (NCIT:C1784 “Imatinib Mesylate”), although response data are limited. CYLD mutation status might serve as a biomarker for immunotherapy responsiveness or as an indicator of altered AIRE expression and T‑cell selection in the thymus, linking tumor genomics to autoimmunity.[9][8][20] Epigenetic regulator mutations suggest potential sensitivity to epigenetic therapies, such as DNA methyltransferase or histone deacetylase inhibitors, though specific evidence in thymic carcinoma is sparse.

### 4.3 Epigenetic Alterations and Non‑coding RNA Dysregulation

Epigenetic alterations are increasingly recognized as central to thymic epithelial tumorigenesis. A genome‑wide DNA methylation study in thymomas investigated whole‑genome methylation profiles and found that the etiology and molecular pathogenesis of thymoma likely involve epigenetic mechanisms, which are hallmark features of carcinogenesis initiation.[12] The authors noted that DNA hypermethylation in promoter regions and global DNA hypomethylation play important roles in the tumorigenesis of thymic epithelial tumors, analogous to patterns observed in other cancers.[12] Specifically, promoter hypermethylation can silence tumor suppressor genes, while global hypomethylation may foster genomic instability and the activation of oncogenes or repetitive elements.

Non‑coding RNAs, particularly microRNAs (miRNAs), add another layer of epigenetic regulation. Recent evidence has indicated that miR‑145‑5p is an important epigenetic regulatory factor involved in tumor progression and treatment response in thymic epithelial tumors.[12][19] A functional study showed that overexpression of miR‑145‑5p in thymic epithelial tumor cells led to morphological changes with increased cell–cell contacts and the appearance of cells with a neuroepithelial‑like phenotype.[19] This suggests that miR‑145‑5p modulates cell adhesion, differentiation, and possibly epithelial–mesenchymal transition (EMT) pathways, influencing tumor phenotype. The study concluded that thymic epithelial tumor phenotype “relies on miR‑145‑5p,” implicating this miRNA in controlling epithelial cell characteristics and perhaps sensitivity to therapy.[19]

These epigenetic features align with GO terms such as “DNA methylation” (GO:0006306), “histone modification” (GO:0016570), and “regulation of cell adhesion” (GO:0030155). The involvement of epigenetic regulators like TET2 and SETD2 in thymic carcinoma further emphasizes the importance of epigenomic dysregulation.[9] TET2 participates in DNA demethylation pathways, while SETD2 mediates histone H3K36 trimethylation; mutations in these genes can alter chromatin structure and gene expression landscapes. Knowledge bases should therefore include epigenetic processes as key pathophysiologic features of thymus neoplasms, with specific annotations for DNA methylation changes, miR‑145‑5p dysregulation, and epigenetic enzyme mutations.

### 4.4 Chromosomal Abnormalities and Structural Genomic Features

Chromosomal abnormalities in thymic epithelial tumors include both recurrent copy‑number changes and occasional large structural variants. As noted, thymic carcinomas frequently exhibit loss of chromosome 16q, a distinguishing feature compared with thymomas.[9] Both thymomas and thymic carcinomas share copy‑number alterations such as chromosome 1q amplification and 6p/6q loss.[9][15] The Chinese consensus indicates that certain thymoma subtypes (e.g., type AB) may show deletions in 5q21–22, 6p21, 6q25.2–25.3, 7p15.3, 8p, 13q14.3, 16q, and 18.[15] These chromosomal changes likely reflect underlying genomic instability and may contribute to tumor progression by altering gene dosage of oncogenes and tumor suppressors.

While specific structural variants such as translocations or inversions have not been highlighted in the provided search results, thymic epithelial tumors might harbor occasional chromosomal rearrangements affecting oncogenes or tumor suppressors. Large‑scale genomic projects like TCGA provide structural variant data, but thymic tumors have been less extensively profiled than common cancers. Nonetheless, knowledge bases should annotate chromosomal aberrations such as “chromosomal deletion (5q)” and “chromosomal amplification (1q)” under structural genomic features for thymus neoplasms.

### 4.5 Modifier Genes and Immune‑Regulatory Loci

Beyond primary driver mutations, certain genes may act as modifiers of disease severity, autoimmunity, or treatment response in thymus neoplasms. CYLD, as mentioned, regulates NF‑κB signaling and interacts with AIRE expression, influencing T‑cell development and self‑tolerance.[9][8] Mutations or altered expression of CYLD could modulate the propensity to develop paraneoplastic autoimmunity, such as MG, or affect the tumor microenvironment’s responsiveness to immunotherapies. AIRE itself, the autoimmune regulator expressed in medullary thymic epithelial cells, plays a critical role in negative selection and central tolerance; deficiency or altered expression of AIRE in thymomas has been implicated in MG pathogenesis and other autoimmune manifestations.[8][20]

Other immune‑regulatory loci, including CTLA‑4 and HLA genes, have been implicated in thymoma‑associated autoimmunity. The narrative review on thymoma‑associated MG notes that CTLA‑4 overexpression and reduced HLA expression contribute to impaired negative selection and decreased Treg numbers, fostering the escape of autoreactive T cells.[8] Genome‑wide association studies in MG have identified susceptibility loci near HLA genes and other immune regulators, some of which may intersect with thymic epithelial cell function.[8][20] Although these loci are not “causal” for thymoma, they may modify autoimmunity risk and clinical phenotype, and should be considered in multi‑omics disease models.

## 5. Mechanisms and Pathophysiology

### 5.1 Thymic Epithelial Cell Biology and Tumorigenesis

The thymus is a primary lymphoid organ located in the anterior superior mediastinum (UBERON:0002370), responsible for the development of T lymphocytes and the establishment of central self‑tolerance.[1][10][8] Thymic epithelial cells (TECs), comprising cortical TECs (cTECs) and medullary TECs (mTECs), form specialized microenvironments that orchestrate thymocyte maturation via positive and negative selection. Positive selection in the cortex ensures that developing T cells can recognize self‑major histocompatibility complex (MHC) molecules, while negative selection in the medulla eliminates self‑reactive T cells and promotes the development of regulatory T cells.[10][8][20] Medullary TECs express a wide array of tissue‑restricted antigens, under the control of AIRE, to present “self” antigens to thymocytes and enforce tolerance.

Thymic epithelial tumors disrupt this finely tuned architecture. Thymomas, composed of neoplastic TECs and abundant thymocytes, retain some functional features of TECS, including the capacity to support T‑cell differentiation, but distort the corticomedullary structure and antigen presentation landscape.[8][20] Tumor epithelial cells in thymomas can induce differentiation of bone marrow‑derived T‑cell progenitors into double‑positive (CD4+CD8+) and single‑positive T cells, resembling normal TEC function, but the abnormal microenvironment and antigen expression patterns lead to incomplete negative selection and the escape of autoreactive T cells.[8] Histologically, thymomas often display lobular architecture with fibrous septa and areas resembling normal thymic cortex or medulla, depending on subtype, but the neoplastic epithelium shows altered morphology and sometimes aberrant expression of antigens.

Tumorigenesis in thymic epithelial cells likely begins with somatic driver mutations or epigenetic changes that confer proliferative and survival advantages. In type A and AB thymomas, GTF2I mutation appears to be a central initiating event, leading to altered transcriptional programs that secure epithelial cell expansion while maintaining a relatively indolent phenotype.[6][15] In more aggressive thymomas (e.g., type B3) and thymic carcinoma, additional aberrations in TP53, CDKN2A/B, and epigenetic regulators drive genomic instability and malignant progression.[9][15][12] Dysregulated signaling pathways such as MAPK, PI3K–AKT, and NF‑κB may be activated by HRAS, KIT, and CYLD mutations, further promoting proliferation, survival, and immune evasion.

At the cellular level, processes such as impaired apoptosis, increased proliferation, altered differentiation, and aberrant adhesion contribute to tumor growth and local invasion. GO terms such as “regulation of apoptotic process” (GO:0042981), “positive regulation of cell proliferation” (GO:0008284), “epithelial cell differentiation” (GO:0030855), and “cell–cell adhesion” (GO:0098609) are applicable. Thymomas often exhibit lower proliferative indices (e.g., Ki‑67) compared with thymic carcinomas, reflecting their slower growth, whereas thymic carcinomas show higher proliferation, necrosis, and invasive growth into adjacent structures such as pleura, pericardium, and lungs.[2][15][18]

### 5.2 Molecular Pathways Driving Neoplastic Transformation

Several molecular pathways are implicated in thymic epithelial tumorigenesis, although comprehensive pathway mapping is still evolving. GTF2I, a transcription factor, regulates multiple downstream genes in response to growth factor signaling, and its L424H mutation likely alters transcriptional programs controlling cell cycle, differentiation, and metabolism.[6] HRAS mutations can activate the RAS–RAF–MEK–ERK (MAPK) cascade, promoting proliferation and survival.[6][15] KIT mutations activate receptor tyrosine kinase signaling, engaging MAPK and PI3K–AKT pathways and conferring growth and survival signals.[9][15] TP53 loss disrupts DNA damage responses and apoptosis, while CDKN2A/B loss relieves inhibition of cyclin‑dependent kinases, thereby accelerating cell cycle progression.[9] CYLD mutations may enhance NF‑κB signaling, promoting survival and inflammation, and modulate immune interactions via AIRE and T‑cell development.[9][8]

Epigenetic pathways, including DNA methylation and histone modification, are altered via TET2 and SETD2 mutations and global methylation changes.[12][9] miR‑145‑5p dysregulation affects cell adhesion and differentiation, potentially influencing epithelial phenotype and tumor invasiveness.[19] Together, these genetic and epigenetic alterations converge on core cancer hallmarks: sustaining proliferative signaling, evading growth suppressors, resisting cell death, enabling replicative immortality, inducing angiogenesis, activating invasion and metastasis, and deregulating cellular energetics.

Specific pathway annotations in knowledge bases might include: KEGG “Pathways in cancer” (hsa05200), “RAS signaling pathway” (hsa04014), “PI3K–Akt signaling pathway” (hsa04151), “p53 signaling pathway” (hsa04115), and “NF‑κB signaling pathway” (hsa04064). Reactome pathways such as “Cell Cycle” (R‑HSA‑1640170), “Apoptosis” (R‑HSA‑109581), and “Immune System” (R‑HSA‑168256) are also relevant.

### 5.3 Autoimmunity Mechanisms in Thymoma‑Associated Myasthenia Gravis

The pathophysiology of thymoma‑associated myasthenia gravis (TAMG) exemplifies the intersection of neoplastic and immune mechanisms in thymus neoplasms. MG is caused by autoantibodies against neuromuscular associated proteins, most commonly AChR at the motor endplate; in thymic hyperplasia‑associated MG, thymic myoid cells expressing AChR serve as autoantigen sources.[8][20] However, thymomas generally lack myoid cells, and the precise target antigens in TAMG have been debated.[8] Neoplastic epithelial cells in thymomas express various AChR subunits but not complete receptor complexes, and there is evidence for molecular mimicry via overexpression of midsize neurofilament (NF‑M) in type B thymomas.[8]

Yasumizu et al. resolved some of these uncertainties by identifying neuromuscular mTECs (nmTECs) in MG‑type thymomas, a subpopulation of medullary TECs that ectopically express neuromuscular molecules including NEFM, RYR3, and GABRA5.[20] Using single‑cell RNA sequencing and immunohistology, they found that neuromuscular expressions were limited to nmTECs in MG cases and absent or low in non‑MG thymomas.[20] They also observed that MG‑type thymomas developed atypical immune microenvironments with ectopic germinal center formation, B cell maturation, and accumulation of T follicular helper cells, creating niches dedicated to autoantibody production.[20] In their discussion, they concluded:

> “Single‑cell RNA‑seq and immunohistological examination of MG‑type thymoma specimens revealed that these neuromuscular expressions were limited in a subpopulation of mTECs (GABRA5+KRT6+), termed nmTECs. In addition, MG‑type thymoma developed atypical immune microenvironments with GC formation, B cell maturation, and ectopic neuromuscular expression on nmTECs, providing a holistic picture of the cell dynamics for producing autoantibodies.”[20]

Other mechanistic elements include the production of immature T cells (double‑positive CD4+CD8+ thymocytes) with incomplete self‑tolerance, decreased Treg numbers, impaired negative selection due to AIRE deficiency, reduced HLA expression, and CTLA‑4 overexpression.[8] Chemokine expression patterns in thymomas closely resemble those in normal thymus, allowing double‑positive cells to migrate to medullary regions where neuromuscular antigens are presented.[8] Spatial transcriptomics studies reveal that in seropositive MG cases, medullary regions are enlarged and structurally remodeled, with nmTECs expressing neuromuscular autoantigens enriched at the corticomedullary junction, precisely where autoreactive T cells may be activated.[8][20]

The causal chain thus runs as follows: neoplastic transformation of TECs with disrupted architecture and antigen expression gives rise to nmTECs that ectopically express neuromuscular molecules; these antigens are presented to developing thymocytes in abnormal medullary microenvironments; impaired negative selection due to AIRE/HLA/CTLA‑4 alterations allows autoreactive T cells to escape; ectopic germinal centers with T follicular helper cells and B cells generate autoantibodies against neuromuscular antigens; circulating autoantibodies bind to neuromuscular junctions, impairing transmission and causing MG symptoms. Upstream mechanisms include GTF2I and other tumor drivers; downstream manifestations include MG phenotypes.

GO terms relevant to this process include “T cell selection” (GO:0046653), “negative regulation of T cell differentiation” (GO:0045580), “antigen processing and presentation” (GO:0019882), “B cell mediated immunity” (GO:0019724), and “germinal center formation” (GO:0009250). Cell Ontology terms include “medullary thymic epithelial cell” (CL:0000087), “T follicular helper cell” (CL:0009061), “B cell” (CL:0000236), and “plasma cell” (CL:0000786). Knowledge bases should capture these mechanistic relationships as causal links between thymus neoplasm entities and MG phenotypes.

### 5.4 Tumor Microenvironment and Immune Evasion

The tumor microenvironment (TME) of thymic epithelial tumors comprises neoplastic TECs, thymocytes, mature T and B cells, dendritic cells, macrophages, and stromal cells, embedded in a milieu of cytokines and chemokines. In thymomas, particularly those associated with MG, the TME is highly immune‑rich, with abundant T cells and germinal center‑like structures.[8][20] This contrasts with many solid tumors where T‑cell infiltration is a marker of anti‑tumor immunity; in thymomas, immune infiltration is inherent to tumor histology and may drive autoimmunity rather than effective tumor rejection.

Immune evasion mechanisms in thymic epithelial tumors are less well characterized than in common cancers but likely include altered antigen presentation, expression of immune checkpoints such as PD‑L1, and local immunosuppression mediated by regulatory T cells and immunosuppressive cytokines. CYLD and AIRE dysregulation may affect the repertoire of antigens presented and the balance between tolerance and activation.[9][8] Epigenetic changes could modulate neoantigen expression and MHC presentation. Thymic carcinomas may downregulate MHC molecules or upregulate PD‑L1, contributing to immune escape, although specific data are not detailed in the provided search results.

The immune‑rich TME has implications for immunotherapy. While immune checkpoint inhibitors such as PD‑1/PD‑L1 antibodies have been explored in thymic carcinoma and refractory thymoma, they carry high risks of inducing or exacerbating autoimmune toxicity, including severe MG, myocarditis, and other immune‑related adverse events, given the underlying immune dysregulation.[9][10] Thus, immunotherapy in thymus neoplasms requires careful risk‑benefit consideration and may be reserved for selected thymic carcinoma patients with high TMB or mismatch repair deficiency.

### 5.5 Multi‑omics and Advanced Technologies

Multi‑omics studies have begun to characterize thymic epithelial tumors at unprecedented resolution. Transcriptomic analyses, including bulk RNA sequencing and single‑cell RNA sequencing, as in Yasumizu et al., provide detailed gene expression profiles of tumor epithelial cells, thymocytes, and immune cells, revealing subpopulations such as nmTECs and specific immune cell states.[20] Spatial transcriptomics integrates gene expression with tissue architecture, highlighting enlarged medullary regions and ectopic germinal centers in MG‑thymoma.[8][20] Epigenomic studies, like the genome‑wide DNA methylation analysis in thymomas, map methylation patterns across the genome, identifying promoter hypermethylation and global hypomethylation associated with tumorigenesis.[12] miRNA profiling studies reveal non‑coding RNA signatures, including miR‑145‑5p, that modulate tumor phenotype.[19]

Liquid biopsy techniques, particularly detection of circulating cell‑free DNA (cfDNA) and circulating tumor DNA (ctDNA), have emerged as promising tools for thymic epithelial tumor monitoring. A single‑center study evaluating cfDNA in TET patients found significantly higher cfDNA levels in thymoma and thymic carcinoma compared with healthy controls, with median cfDNA levels of 3.3 ng/μl in controls, 11.4 ng/μl in thymoma, and 25.6 ng/μl in thymic carcinoma.[17] cfDNA concentrations were higher in metastatic (M1a/M1b) compared to non‑metastatic (M0) TETs (25.6 vs. 7.2 ng/μl), and highest baseline cfDNA levels were associated with distant metastasis.[17] The authors concluded that “higher baseline levels than the control group were observed in both advanced T and TC patients” and that cfDNA may serve as a minimally invasive biomarker for early diagnosis, relapse detection, and prognostic assessment.[17]

These advanced technologies enable multi‑layered disease models integrating genomic, epigenomic, transcriptomic, proteomic, and liquid biopsy data, paving the way for precision oncology approaches in thymus neoplasms. Knowledge bases should incorporate multi‑omic data types, mapping gene expression changes to GO processes, cell‑type‑specific expression to CL terms, and spatial features to UBERON substructures, alongside cfDNA concentration ranges and ctDNA mutation profiles as dynamic biomarkers.

## 6. Anatomical Structures and Disease Spread

### 6.1 Primary Localization in Thymus and Mediastinum

Thymus neoplasms originate in the thymus gland, anatomically located in the anterior superior mediastinum behind the sternum, extending from the lower neck into the mediastinum.[1] UBERON:0002370 represents the thymus as an organ, part of the lymphoid system and endocrine interactions. Thymic epithelial tumors present as masses in the anterior mediastinum, often localized within the thymic capsule initially and later invading adjacent tissues. Imaging shows tumors in the anterior superior mediastinum, bounded by the sternum anteriorly, great vessels and pericardium posteriorly, and pleura laterally.[15][18]

The anterior mediastinum (UBERON:0002110) is thus the primary anatomical site for thymus neoplasms. Secondary involvement may extend into the middle mediastinum (UBERON:0002111), pericardium (UBERON:0002414), pleura (UBERON:0002365), lung parenchyma (UBERON:0002048), and chest wall (UBERON:0002228). Thymic carcinomas, in particular, may infiltrate deeply into surrounding structures and cause compression or invasion of the trachea, bronchi, superior vena cava, or pulmonary arteries.

### 6.2 Local Invasion and Regional Spread

Disease spread patterns are captured by staging systems such as Masaoka–Koga and TNM (IASLC eighth edition).[14][18] In Masaoka–Koga, stage I thymomas are encapsulated without invasion; stage II shows microscopic or macroscopic capsular invasion into surrounding fatty tissue; stage III invades adjacent organs such as pericardium, lung, or great vessels; and stage IV includes pleural or pericardial dissemination (IVa) and lymphogenous or hematogenous metastasis (IVb). The TNM system refines these categories by specifying T descriptors (e.g., T1 confined to thymus, T2 invading mediastinal pleura, T3 invading pericardium or lung, T4 invading great vessels), N descriptors (N0 vs. N1/N2 for nodal involvement), and M descriptors (M0 vs. M1a/M1b for pleural/pericardial nodules and distant metastasis).[14][18][17]

Postoperative radiotherapy guidelines emphasize the need to cover the whole thymic space and tumor bed, including anterior, superior, and middle mediastinum, and any involved nodes or resected pleural implants, reflecting typical invasion patterns.[18] Microscopic negative margins (R0) vs. positive margins (R1/R2) correlate with recurrence risk, underscoring the importance of complete resection for local control.[18] Thymic carcinomas often present at higher stages with invasion into lung, pericardium, or great vessels, and may exhibit nodal and distant metastases more frequently than thymomas.[2][9][15]

### 6.3 Distant Metastases and Organ Complications

Distant metastases in thymus neoplasms, particularly thymic carcinomas, may involve the lungs, liver, bone, and other organs. TNM M1b stage defines pulmonary intraparenchymal nodules or distant organ metastasis, whereas M1a denotes separate pleural or pericardial nodules.[17] cfDNA concentrations correlate with metastatic status, being higher in M1a/M1b compared with M0.[17] Distant metastases manifest clinically as respiratory symptoms, bone pain, hepatic dysfunction, or neurologic symptoms, depending on site.

Organ complications also arise from local invasion, such as pericardial effusion, superior vena cava syndrome, airway obstruction, and recurrent pneumonia. Paraneoplastic hypogammaglobulinemia may predispose to severe infections. Treatment‑related organ damage includes radiation‑induced pneumonitis or cardiomyopathy and chemotherapy‑induced cardiotoxicity (e.g., doxorubicin) or nephrotoxicity (cisplatin).[16][18]

### 6.4 Tissue, Cell, and Subcellular Structures

At the tissue level, thymus neoplasms primarily affect epithelial tissue within the thymus, with concomitant involvement of lymphoid tissue. Thymic epithelial cells (TECs) represent a specialized epithelial cell type (CL:0002328), with cortical TECs (cTECs; CL:0002329) and medullary TECs (mTECs; CL:0000087) distinguished by location and function. Thymomas comprise neoplastic TECs and variable numbers of immature T cells (thymocytes), including double‑positive CD4+CD8+ cells (CL:0000895) and single‑positive T cells (CL:0000911, CL:0000912).[8][20] Thymic carcinomas, on the other hand, may show squamous or basaloid epithelial differentiation with fewer lymphocytes.

At the subcellular level, somatic mutations and epigenetic changes affect nuclear processes such as DNA replication, repair, transcription, and chromatin modification, implicating cellular compartments like the nucleus (GO:0005634), chromatin (GO:0000785), and nucleolus (GO:0005730). Mitochondrial pathways may be disrupted via TP53 and other regulators, affecting apoptosis (GO:0005739 “mitochondrion,” GO:0006915 “apoptotic process”). Cell surface compartments, including plasma membrane proteins (GO:0005886), are implicated via receptor tyrosine kinases like KIT and AChR subunits expressed in neoplastic cells.

Localization is generally midline in the anterior mediastinum, but lateral extension into the right or left pleural spaces can occur, leading to unilateral or bilateral disease. Lateralization may be asymmetric depending on tumor growth patterns, but no inherent laterality bias is described.

## 7. Temporal Development and Natural History

### 7.1 Onset: Age, Pattern, and Early Course

Thymic epithelial tumors typically present in adulthood, with reported mean ages at diagnosis ranging from 45 to 60 years.[2][3][1][7] Multiple retrospective cohort studies have reported mean ages of 46 years, 46.5 years, 48.8 years, 51.8 years, and 54.7 years in single‑center series.[3] SEER data indicate a higher incidence of thymic cancers in the over 65‑year‑old group, and ethnic differences in age at diagnosis, with Black patients presenting earlier than Caucasians or Asian/Pacific Islanders.[3] Thymus neoplasms are not diseases of young adults; pediatric cases are rare and may represent distinct biological entities.

Onset is typically chronic and insidious. Tumors often grow slowly and remain asymptomatic until they reach a size sufficient to cause chest symptoms or are detected incidentally on imaging.[1][2][15] Paraneoplastic syndromes such as MG may precede, coincide with, or follow tumor diagnosis. MG onset can be more acute or subacute, with rapid development of muscle weakness, but the underlying thymoma may have been present for some time. In some cases, MG is diagnosed, and thymic imaging reveals a thymoma; in others, thymoma is discovered incidentally and MG develops later. Thus, the temporal relationship between tumor and autoimmunity can vary.

### 7.2 Progression, Staging, and Recurrence

Disease progression in thymus neoplasms depends heavily on histologic subtype and stage at diagnosis. Type A and AB thymomas often remain localized and indolent, with low recurrence rates after complete resection.[2][6] Type B thymomas, especially B2 and B3, and thymic carcinomas have higher risks of local invasion, pleural dissemination, and distant metastasis.[2][15] Staging systems such as Masaoka–Koga and TNM (IASLC eighth edition) stratify progression from encapsulated tumors to locally invasive and metastatic disease.[14][18]

Survival analyses indicate that stage and completeness of resection are key prognostic criteria. In resectable patients undergoing surgery, 5‑year overall survival (OS) ranges from 50–75%, with marked differences by stage: stages I and II show approximately 91% 5‑year OS, whereas stages III and IV show roughly 31%.[2] Cleveland Clinic data summarize 5‑year survival for thymic cancers as 95% when confined to the thymus, 78% when spread to nearby organs and lymph nodes, and 38% when metastasized to distant sites.[1] Postoperative radiotherapy (PORT) provides significant benefit in selected patients, particularly stage IIb–IV thymoma and those with incomplete resection (R1/R2), improving overall survival (OS), disease‑specific survival (DSS), and disease‑free survival (DFS).[18] Stage I–IIa thymomas generally do not derive major benefit from PORT, and surgery alone is standard.[18]

Recurrence patterns include local recurrence in the anterior mediastinum, pleural implants, and distant metastases. PN/AI syndrome status appears associated with lower recurrence rates, but PN/AI is not an independent prognostic factor.[10] The time to recurrence can be years, and long‑term surveillance is needed. Recurrence‑free intervals and survival are influenced by stage, histology, margin status, and adjuvant therapy.

### 7.3 Remission, Chronicity, and Critical Periods

Early‑stage thymomas (stage I–II) treated with complete thymectomy can achieve long‑term remission or cure, with 5‑year OS exceeding 90% and low recurrence rates.[2][1][18] In these cases, disease duration may be limited to the peri‑diagnostic and postoperative period. Advanced thymomas and thymic carcinomas often have a chronic course, with periods of partial remission after surgery and chemotherapy followed by recurrence or progression. MG and other PN/AI syndromes may persist or fluctuate independent of tumor status, requiring ongoing management.

Remission patterns are predominantly treatment‑induced rather than spontaneous. Surgical resection is the primary curative modality for localized disease, while systemic therapy can induce partial or complete responses in advanced thymoma, as seen in the cisplatin‑doxorubicin‑cyclophosphamide (PAC) trial, where 3 complete responses and 12 partial responses were observed among 30 patients, yielding a 50% objective response rate.[16] The median duration of response was 11.8 months, time to treatment failure 18.4 months, and median survival 37.7 months, indicating substantial but not permanent remissions.[16]

Critical periods include the diagnostic window when small anterior mediastinal nodules are detected incidentally. The Chinese consensus advises re‑examination by CT or MRI after 3–6 months and then every 1–2 years for suspected benign lesions, to avoid unnecessary surgery, but recommends direct surgery for suspected TETs with high‑risk histologic subtypes (B2/B3 thymoma, thymic carcinoma).[15] This early management period is crucial for correct diagnosis and staging. Another critical period is perioperative MG management, where thymectomy and immunotherapy must be carefully coordinated to avoid MG crises.

## 8. Epidemiology, Inheritance, and Population Patterns

### 8.1 Incidence, Prevalence, and Burden

Thymus neoplasms, particularly thymic epithelial tumors, are rare in the general population. The 2020 epidemiologic review estimates thymoma incidence between 0.13 and 0.32 per 100,000 per year, noting that thymoma represents only 0.2–1.5% of all malignancies.[3] European registry data show incidence rates of 0.9 per million per year in Northern Europe, 1.2 per million in Eastern Europe, 1.9 per million in Central Europe, 2.3 per million in Southern Europe, and 1.1 per million in the UK and Ireland.[3] Orphanet lists thymoma prevalence as unknown but emphasizes that it is a rare malignancy.[7] The Cleveland Clinic reports that only about 400 people in the U.S. are diagnosed with thymic cancers each year.[1]

These figures translate into low disease burden compared with common cancers, but thymus neoplasms still pose significant clinical challenges due to their unique pathophysiology and association with autoimmunity. In global burden of disease terms, thymic epithelial tumors would contribute modestly to cancer mortality and disability‑adjusted life years, but more substantially when considering autoimmune morbidity.

### 8.2 Sex, Ethnicity, and Geographic Variation

Sex distribution in thymoma is relatively balanced, with no strong male or female predominance. Most studies indicate no significant sex influence on thymoma development, though some report slight differences.[3] Paraneoplastic autoimmunity, particularly MG, tends to be more common in female patients, consistent with autoimmune disease patterns.[10][8] Thymic carcinoma may show different sex distributions, but data are limited.

Race and ethnicity show notable variation in thymic cancer incidence. SEER program analyses by Engels et al. document higher incidence among Blacks and “Other” races compared with Caucasians, with rates of 0.2 per 100,000 in Blacks, 0.29 per 100,000 in other races, and 0.13 per 100,000 in Caucasians.[3] Asian and Pacific Islanders overall have an incidence of 0.25 per 100,000, with variation among Japanese, Vietnamese, Filipino, Chinese, and Korean groups.[3] Moreover, age at diagnosis differs by ethnicity, with Black Americans presenting at a median age of 48 years vs. 58 years for Caucasians.[3] These patterns may reflect genetic, environmental, or healthcare access differences.

Geographically, thymic epithelial tumor incidence appears higher in Central and Southern Europe compared with Northern and Eastern Europe and the UK/Ireland.[3] Within Asia, thymic tumors are relatively more common in certain East Asian populations, as reflected by higher incidence in Japanese and Vietnamese groups.[3][1] The Cleveland Clinic notes that most people diagnosed with thymic cancers in the U.S. have Asian or Pacific Islander heritage, underscoring the ethnic skew.[1]

### 8.3 Inheritance, Penetrance, and Familial Clustering

Thymus neoplasms are not inherited cancers in the classic Mendelian sense. Orphanet explicitly states that inheritance is “not applicable” for thymoma, reflecting a sporadic somatic malignancy.[7] No autosomal dominant, autosomal recessive, X‑linked, or mitochondrial inheritance patterns have been established. Penetrance and expressivity concepts are thus not directly relevant, as there are no known germline causal variants.

Familial clustering of thymoma or thymic carcinoma is rare, and genetic anticipation or founder effects have not been described. Carrier frequency is not applicable, as there is no known germline mutation to carry. Germline mosaicism has not been implicated. Consanguinity is not associated with increased thymic tumor risk.

Knowledge bases should therefore annotate thymus neoplasms as sporadic cancers without Mendelian inheritance, while linking to somatic mutation data and autoimmunity GWAS loci where relevant for MG and other PN/AI syndromes.

## 9. Diagnostics and Biomarkers

### 9.1 Clinical Evaluation and Imaging

Diagnostic evaluation of suspected thymus neoplasms begins with clinical history and examination, focusing on chest symptoms and signs of paraneoplastic autoimmune syndromes, particularly MG. Laboratory tests include AChR antibody titers, complete blood counts, immunoglobulin levels, and other disease‑specific markers as indicated.[10][8] However, imaging and histopathology are central to tumor diagnosis.

The Chinese expert consensus recommends enhanced chest CT in mediastinal windows as the preferred imaging modality for thymic tumors, highlighting its ability to define tumor extent, detect peripheral tissue infiltration and distant metastases, and predict stage.[15] CT typically shows a well‑circumscribed anterior mediastinal mass, either homogeneous or heterogeneous, with or without calcifications. Tumor size, shape, border regularity, and relationship to adjacent structures help distinguish thymoma from thymic carcinoma and other mediastinal tumors.[15]

MRI is indicated when CT diagnosis is unclear, particularly to evaluate invasion into surrounding fat and distinguish malignant thymic tumors from thymic cysts or thymic hyperplasia.[15] MRI provides superior soft tissue contrast, allowing more precise delineation of tumor boundaries and capsular integrity. PET‑CT offers metabolic information, with higher standardized uptake values suggestive of malignancy, and can detect pleural/pericardial nodules and distant metastases.[15][17] PET‑CT is particularly useful in advanced disease and for staging thymic carcinoma.

### 9.2 Histopathology, Immunohistochemistry, and WHO Classification

Histopathological examination is the gold standard for diagnosing thymic epithelial tumors.[15][5] CT‑guided needle biopsy is recommended as the standard operation for obtaining tissue in suspected thymic tumors, with ultrasound‑guided biopsy or thoracoscopic examination as supplementary approaches.[15] Histologic subtype determination is critical because prognosis varies by subtype; type A and AB thymomas generally have better outcomes than type B3 thymomas and thymic carcinoma.[5][2][15]

WHO classification criteria emphasize the morphology of neoplastic epithelial cells and associated lymphocytes. Type A thymomas display spindle or oval epithelial cells with few lymphocytes; AB thymomas show areas of type A morphology mixed with lymphocyte‑rich regions; B1 thymomas resemble normal thymus; B2 show more epithelial cells among abundant lymphocytes; B3 consist predominantly of epithelial cells with scattered lymphocytes.[5] Thymic carcinoma shows overt cytologic malignancy, with squamous, lymphoepithelioma‑like, or other carcinoma patterns, and lacks the organotypic features of thymoma.[5][15]

Immunohistochemistry aids diagnosis and subtype classification. Thymic carcinoma squamous cell variants often show positive staining for CD5, KIT (CD117), FOXN1, and CD205, and may harbor KIT mutations.[15] Thymoma subtypes and thymic carcinomas can be distinguished from lymphomas, germ cell tumors, and metastases based on cytokeratin expression, TdT, CD3, CD20, CD30, PLAP, and other markers. GTF2I mutation status can serve as a molecular marker of thymoma, particularly type A/AB, and may be detected via targeted sequencing.[6][15] NCIT terms for diagnostic procedures include NCIT:C17209 (Biopsy), NCIT:C17606 (Computerized Tomography), NCIT:C18932 (Magnetic Resonance Imaging), and NCIT:C20117 (Positron Emission Tomography).

### 9.3 Genetic and Molecular Testing

Genetic testing in thymus neoplasms focuses on somatic mutation profiling of tumor tissue rather than germline testing. Targeted sequencing panels including TP53, GTF2I, CDKN2A/B, HRAS, KIT, CYLD, TET2, SETD2, BAP1, and ASXL1 can provide diagnostic and prognostic information, particularly in thymic carcinoma.[9][6][15] Next‑generation sequencing (NGS) assays enable comprehensive mutation detection and can help differentiate thymoma subtypes and thymic carcinoma.[15] For example, detection of GTF2I L424H supports a diagnosis of thymoma with indolent behavior; TP53 and CDKN2A/B mutations suggest thymic carcinoma and poor prognosis.[9][6][15]

While whole exome sequencing (WES) and whole genome sequencing (WGS) could be employed, their utility is more research‑oriented given the low mutational burden in thymomas and modest but clinically relevant burden in thymic carcinomas.[6][9] Chromosomal microarray or karyotyping are not routinely used for thymic epithelial tumors but may be applied in research contexts. Liquid biopsy NGS of ctDNA could correlate with tumor mutation profiles and monitor disease, but evidence is preliminary.[17]

### 9.4 Liquid Biopsy and Circulating Biomarkers

As noted, cfDNA and ctDNA are promising circulating biomarkers. The cfDNA study found significantly higher cfDNA levels in thymoma and thymic carcinoma compared with healthy controls and higher levels in metastatic vs. non‑metastatic disease.[17] These findings suggest that cfDNA concentration could serve as a quantitative biomarker for tumor burden and metastasis. ctDNA mutation analysis could detect specific somatic variants (e.g., GTF2I, TP53, KIT) in plasma, enabling non‑invasive molecular profiling and potentially early detection of relapse.

Other circulating biomarkers are less well defined. AChR antibody titers correlate with MG activity but not directly with tumor burden. Serum cytokines, soluble PD‑L1, or other immunologic markers could have diagnostic or prognostic roles, but data are limited. Knowledge bases should include cfDNA concentration ranges and ctDNA mutation detection as emerging diagnostic modalities.

### 9.5 Diagnostic Criteria and Differential Diagnosis

Standardized diagnostic criteria for thymic epithelial tumors derive from WHO classification and TNM staging.[5][14][15] Diagnosis requires a combination of imaging demonstrating an anterior mediastinal mass and histopathology confirming thymic epithelial origin and subtype. Differential diagnosis includes lymphomas (especially primary mediastinal large B‑cell lymphoma and Hodgkin lymphoma), germ cell tumors (e.g., seminomas, non‑seminomatous germ cell tumors), metastatic lung carcinoma, thymic cysts, thymic hyperplasia, and other mediastinal masses (e.g., pericardial cysts, teratomas).[15]

Distinguishing thymic carcinoma from pulmonary squamous cell carcinoma invading the mediastinum is essential; immunohistochemical positivity for CD5 and CD117 and expression of FOXN1 and CD205 favor thymic carcinoma.[15] Germ cell tumors show PLAP and OCT3/4 positivity; lymphomas show lineage‑specific markers. Clinical correlation with age, sex, paraneoplastic syndromes, and imaging features aids differentiation.

### 9.6 Screening and Early Detection Strategies

Despite advances in imaging and molecular diagnostics, routine screening for thymus neoplasms in asymptomatic individuals is not recommended. The Chinese expert consensus explicitly states that given the low incidence of TETs, low‑dose CT is not recommended for routine screening.[15] For small anterior mediastinal nodules ≤3 cm detected incidentally, management should be individualized based on imaging characteristics and risk assessment, with periodic re‑examination for suspected benign lesions and consideration of surgery for lesions suspicious for high‑risk TETs.[15] Newborn screening, carrier screening, or other population‑level screening methods are not applicable.

## 10. Outcome, Prognosis, and Predictive Factors

### 10.1 Survival Outcomes and Mortality

Survival outcomes in thymus neoplasms vary widely by histology, stage, and treatment. Early‑stage thymomas (stage I–II) treated with complete resection have excellent 5‑year OS, around 90–95%.[2][1][18] Cleveland Clinic data show 5‑year survival of 95% for thymic cancers confined to the thymus, 78% when spread to nearby organs and lymph nodes, and 38% when metastasized to distant body parts.[1] Narrative reviews and retrospective series yield similar estimates, with stage I–II thymomas achieving high survival and stage III–IV thymomas much lower.[2][18]

Thymic carcinoma has significantly worse prognosis than thymoma, with lower 5‑year OS and higher mortality.[2][9] Specific survival statistics vary across studies due to small sample sizes, but 5‑year OS for thymic carcinoma may fall below 50%, and advanced thymic carcinoma (stage IV) has poor outcomes even with aggressive therapy. TP53 and CDKN2A mutations correlate with poorer prognosis.[9]

Mortality from thymus neoplasms includes disease‑specific deaths due to local invasion, metastasis, or treatment complications, and deaths from associated autoimmunity, such as MG crises or severe infections in hypogammaglobulinemia. However, MG is generally treatable, and tumor control reduces autoimmune burden.

### 10.2 Prognostic Factors and Biomarkers

Key prognostic factors in thymic epithelial tumors include stage, histologic subtype, completeness of resection, margin status, and certain molecular markers. Stage and margin status are consistently identified as independent prognostic criteria: patients with incompletely resected thymomas (R1/R2) have worse OS and DSS than those with complete resection (R0).[18] PORT improves outcomes particularly in incompletely resected and advanced stage thymomas.[18]

Histologic subtype also influences prognosis, though less strongly than stage and resection. Type A and AB thymomas generally have better outcomes; type B3 and thymic carcinoma have poorer prognosis.[2][5] PN/AI syndrome presence is associated with favorable tumor features but is not an independent prognostic factor for OS or recurrence‑free survival.[10]

Molecular biomarkers include GTF2I mutation status, which is associated with indolent thymoma behavior and good prognosis; TP53 and CDKN2A/B mutations, which correlate with poor prognosis in thymic carcinoma; CYLD, which may predict immunotherapy response; and TMB, with higher TMB suggesting potential benefit from checkpoint inhibitors but also indicating aggressive tumor biology.[6][9][12] cfDNA levels correlate with metastatic status and may serve as a prognostic biomarker.[17]

### 10.3 Morbidity, Disability, and Quality of Life

Morbidity from thymus neoplasms includes physical disability due to tumor mass, treatment side effects, and autoimmune manifestations. Early‑stage thymoma patients may experience transient disability during surgery and recovery but often return to baseline function. Advanced thymic tumors and metastases can cause chronic respiratory impairment, pain, and reduced physical functioning. MG and other PN/AI syndromes contribute to long‑term morbidity, with fluctuating weakness, fatigue, and treatment side effects.

Quality‑of‑life instruments, although not extensively applied in thymic tumor studies, would likely show deficits in physical functioning, vitality, social functioning, and mental health domains in advanced disease and PN/AI situations. Rehabilitation, supportive care, and psychological support are crucial for mitigating these impacts.

## 11. Treatment Strategies

### 11.1 Surgical Management

Surgery is the cornerstone of treatment for localized thymic epithelial tumors. Complete thymectomy, including removal of the entire thymus gland and tumor, is standard for resectable thymomas and thymic carcinomas.[2][4][15] Surgical approaches may include median sternotomy, video‑assisted thoracoscopic surgery (VATS), or robotic thymectomy, depending on tumor size, location, and surgeon expertise. Extended thymectomy, including perithymic fat, is recommended in MG patients to maximize removal of thymic tissue and potential antigen sources.[10]

NCCN Guidelines (Version 2.2025) outline treatment options, emphasizing surgery as first‑line for resectable thymomas, with consideration of adjuvant radiotherapy based on stage and margin status.[4] For thymic carcinoma, surgery is again preferred for localized disease, but adjuvant therapy is more commonly indicated due to aggressive behavior.[4] NCIT terms such as NCIT:C7950 (Thymectomy) and NCIT:C15727 (Thoracoscopic Thymectomy) map to these interventions.

### 11.2 Radiotherapy

Postoperative radiotherapy (PORT) plays a key role in selected thymoma patients, particularly those with advanced stage or incomplete resection. A review of PORT in thymomas concluded that radiotherapy after surgery provides significant benefits in terms of OS, DSS, and DFS in stage IIb–IV thymomas and in patients with R1/R2 margins.[18] Radiotherapy is generally not indicated for stage I–IIa thymomas after complete resection, where surgery alone is sufficient.[18]

PORT should be delivered within at least 3 months of surgery, using 3D conformal or intensity‑modulated radiotherapy (IMRT) directed to the tumor bed.[18] Clinical target volume should include the entire thymic space, tumor bed, and any involved nodes or resected pleural implants.[18] Recommended fractionated total dose after R0 resection is 45–50 Gy, with daily doses of 1.8–2 Gy over 4–6 weeks; after R1 resection, 50–54 Gy with a boost to areas of likely residual disease; unresectable disease may require 60–70 Gy.[18] Importantly, PORT did not significantly increase high‑grade acute toxicity compared with surgery alone in reviewed series.[18]

NCIT terms such as NCIT:C15313 (Radiation Therapy), NCIT:C45984 (Postoperative Radiotherapy), and NCIT:C29296 (Intensity Modulated Radiation Therapy) correspond to these interventions.

### 11.3 Systemic Chemotherapy

Systemic chemotherapy is indicated in unresectable, locally advanced, or metastatic thymoma and thymic carcinoma. The PAC regimen—cisplatin, doxorubicin, cyclophosphamide—has been a standard combination for advanced thymoma. A phase II trial treating 29 thymoma and 1 thymic carcinoma patient with metastatic or recurrent disease after radiotherapy reported three complete responses and 12 partial responses, yielding a 50% objective response rate, with mild hematologic toxicity and only one case of febrile neutropenia.[16] Median duration of response was 11.8 months, time to treatment failure 18.4 months, and median survival 37.7 months.[16] These results demonstrate that substantial response rates and prolonged survival can be achieved in advanced thymoma with PAC chemotherapy.[16]

Other regimens include cisplatin‑etoposide, carboplatin‑paclitaxel, and combinations with ifosfamide or other agents, particularly for thymic carcinoma.[4][9] NCIT terms for drugs include NCIT:C376 (Cisplatin), NCIT:C1305 (Doxorubicin), NCIT:C1428 (Cyclophosphamide), NCIT:C489 (Etoposide), NCIT:C292 (Paclitaxel), and NCIT:C1226 (Carboplatin). CHEBI entries include CHEBI:27899 (cisplatin), CHEBI:28748 (doxorubicin), and CHEBI:4027 (cyclophosphamide).

### 11.4 Targeted Therapy and Immunotherapy

Targeted therapies and immunotherapies are emerging in thymic carcinoma. KIT mutations in thymic carcinoma suggest potential sensitivity to tyrosine kinase inhibitors (TKIs) such as imatinib.[9][15] However, clinical responses have been inconsistent, likely due to mutation heterogeneity and downstream pathway complexity. Other targets include FGFR3, epigenetic regulators, and immune checkpoints.

Immune checkpoint inhibitors targeting PD‑1/PD‑L1 have demonstrated activity in thymic carcinomas with high TMB or PD‑L1 expression in small studies (not detailed in search results), but carry high risks of immune‑related adverse events, including severe MG, myocarditis, hepatitis, and other autoimmunity, due to underlying thymic immune dysregulation.[9][10] Thus, checkpoint inhibitors must be used cautiously, preferably in clinical trials with intensive monitoring.

CYLD status may predict immunotherapy response, as this gene regulates NF‑κB signaling and interacts with AIRE expression in T‑cell development.[9] High TMB and mismatch repair deficiency (e.g., MLH1 mutation) could also predict checkpoint inhibitor benefit.[9]

### 11.5 Management of Paraneoplastic Autoimmune Syndromes

Treatment of MG and other PN/AI syndromes is integral to thymus neoplasm management. MG therapy includes acetylcholinesterase inhibitors, corticosteroids, steroid‑sparing immunosuppressants (azathioprine, mycophenolate mofetil), and rapid interventions like plasmapheresis or IVIG for exacerbations. Thymectomy is a standard MG treatment, especially in thymoma‑associated MG, and may improve MG symptoms over time.[10][8][20] PRCA requires immunosuppression and transfusion support; hypogammaglobulinemia is treated with regular IVIG infusions and infection prophylaxis.[10]

These treatments correspond to NCIT terms such as NCIT:C625 (Prednisone), NCIT:C50958 (Mycophenolate Mofetil), NCIT:C2308 (Azathioprine), NCIT:C1857 (Plasmapheresis), and NCIT:C859 (Intravenous Immunoglobulin). Coordinating immunosuppression with chemotherapy and radiotherapy is essential to avoid excessive toxicity or compromised tumor control.

### 11.6 Experimental and Future Therapies

Experimental treatments in thymus neoplasms include novel TKIs, epigenetic therapies, and advanced immunotherapies. Gene therapy and RNA‑based therapies targeting specific mutations like GTF2I are not yet available, and functional genomics screens have only begun to explore vulnerabilities in thymic epithelial tumors.[6][9][19] Multi‑omics studies may identify new targets and pathways. CAR‑T cell therapy is theoretically possible but risky given thymic involvement and autoimmunity. Clinical trials investigating permutation combinations of chemotherapy, immunotherapy, and targeted agents should be cataloged with NCT identifiers in knowledge bases, though specific trials are not listed in the search results.

## 12. Prevention and Public Health Considerations

### 12.1 Primary Prevention

Given the unknown etiology and lack of modifiable risk factors for thymus neoplasms, primary prevention strategies are limited. There is no evidence that specific lifestyle modifications, environmental interventions, or vaccines prevent thymoma or thymic carcinoma.[3][1][15][7] General cancer prevention measures, such as smoking cessation, healthy diet, and physical activity, are beneficial for overall health but not specifically for thymic epithelial tumors.

### 12.2 Secondary and Tertiary Prevention

Secondary prevention, involving early detection and treatment, focuses on vigilance for PN/AI syndromes and incidental anterior mediastinal masses. MG patients should undergo thymic imaging to detect thymoma; timely thymectomy in thymoma‑associated MG can prevent progression of both tumor and autoimmunity.[10][8] For incidentally detected small mediastinal nodules, periodic imaging and appropriate surgical referral when malignancy is suspected serve as secondary prevention of advanced disease.[15]

Tertiary prevention aims to prevent complications and disability in patients with established thymus neoplasms. Regular follow‑up imaging, management of MG and other PN/AI syndromes, infection prophylaxis in hypogammaglobulinemia, and cardiac and pulmonary monitoring in patients receiving radiotherapy or anthracycline chemotherapy all contribute to tertiary prevention. Rehabilitation, physical therapy, and psychosocial support mitigate disability.

### 12.3 Genetic Counseling and Risk Communication

Genetic counseling is generally not indicated for thymus neoplasms as inherited risk is minimal. However, counseling may be appropriate for patients with MG and their families regarding autoimmune risk and thymectomy decisions. For patients with mismatch repair deficiency in thymic carcinoma (e.g., MLH1 mutation), counseling about Lynch syndrome or other hereditary cancer syndromes may be warranted, although data are limited.[9]

Public health interventions specific to thymus neoplasms are not established due to rarity and lack of known environmental causes. Healthcare systems should ensure access to specialized thoracic oncology and neuromuscular care for affected patients.

## 13. Comparative Oncology and Natural Disease in Other Species

Thymic tumors occur naturally in other species, particularly companion animals such as dogs and cats, where thymomas present as cranial mediastinal masses and may be associated with MG or other paraneoplastic syndromes. Comparative pathology studies indicate similarities in histology and immune associations across species, reflecting conserved thymic function and epithelial cell biology. Orthologous genes such as Gtf2i, Tp53, and Kit in mice and dogs share sequence and functional homology with human counterparts (NCBI Gene IDs correspondingly), and mutations in these genes could theoretically drive thymic tumors in animals.

Comparative biology highlights evolutionary conservation of thymic architecture, TEC differentiation, and central tolerance mechanisms, supporting the use of animal models for mechanistic studies. However, species‑specific differences in thymic involution, immune system development, and environmental exposures limit direct extrapolation. Knowledge bases may include OMIA entries and veterinary literature references to capture thymic neoplasms in animals and cross‑species disease mechanisms.

## 14. Model Organisms and Experimental Systems

### 14.1 Murine Models of Thymic Epithelial Tumors

Murine models have been instrumental in elucidating thymic epithelial tumor pathogenesis. The CRISPR/Cas9 knock‑in of Gtf2i L424H in murine thymic epithelial cells, as described in the somatic mutation study, created a model where mutated cells underwent neoplastic transformation and formed tumors when transplanted into nude mice.[6] This model recapitulates aspects of human thymomas driven by GTF2I and demonstrates that Gtf2i mutation alone can initiate TEC neoplasia. Such models allow investigation of downstream transcriptional programs, interactions with thymocytes, and responses to therapies.

Other mouse models may involve conditional knockout or overexpression of TP53, CDKN2A/B, CYLD, AIRE, or epigenetic regulators in TECs, to study thymic tumorigenesis and autoimmunity. MG‑like syndromes can be modeled via immunization with AChR or transfer of autoantibodies. Single‑cell and spatial transcriptomics in mouse thymus contribute to baseline understanding of TEC and thymocyte biology, informing human disease models.[20][8]

### 14.2 Autoimmunity Models and MG‑Thymoma Research

MG models in mice include immunization with purified AChR, resulting in autoantibody production and neuromuscular junction impairment. Thymoma‑associated MG can be modeled by combining thymic tumor models with MG induction, though such compound models are complex. Yasumizu et al.’s integrative atlas approach could be extended to mouse MG‑thymoma models, examining nmTEC emergence and germinal center formation.[20]

These models illuminate processes such as T‑cell selection, germinal center dynamics, and neuromuscular antigen presentation, aligning with GO and CL terms previously discussed. They provide platforms for testing immunotherapies, antigen‑specific tolerizing strategies, and targeted interventions at the level of thymic epithelium.

### 14.3 In Vitro Models, Organoids, and Cell Lines

In vitro models include thymic epithelial tumor cell lines and organoids derived from human thymomas or thymic carcinomas. The miR‑145‑5p study used in vitro systems to overexpress miR‑145‑5p in thymic epithelial tumor cells, observing morphological changes with increased cell–cell contacts and neuroepithelial‑like cells.[19] Such cell‑based models allow manipulation of gene expression and assessment of phenotypic consequences.

Organoids replicating thymic architecture, including TECs and thymocytes, could provide advanced platforms for studying thymic neoplasms and MG pathogenesis. iPSC‑derived TECs and thymic organoids might be used to model genetic mutations and drug responses. Functional genomics screens using CRISPR or RNAi in TEC lines could identify essential genes and pathways in thymic tumor biology.

## 15. Conclusion

Thymus neoplasms, dominated by thymic epithelial tumors—thymomas, thymic carcinomas, and neuroendocrine tumors—represent a distinctive and complex domain of oncology and immunology, characterized by rare incidence, unique site of origin, and profound interactions with T‑cell development and autoimmunity.[2][7][10] Etiologically, these tumors are largely sporadic, with no established germline predisposition and limited environmental risk factors, but exhibit clearly defined somatic and epigenetic drivers, notably GTF2I L424H in indolent thymomas and TP53, CDKN2A/B, CYLD, KIT, and epigenetic regulator mutations in more aggressive thymic carcinomas.[6][9][12][19] Epidemiologic data highlight modest demographic variation by age, ethnicity, and geography, but no strong modifiable risk exposures.[3][1]

Clinically, thymus neoplasms present as anterior mediastinal masses with variable symptoms, often discovered incidentally or in the context of paraneoplastic autoimmune syndromes such as myasthenia gravis, pure red cell aplasia, and hypogammaglobulinemia.[1][10][8] The pathophysiology of thymoma‑associated MG has been elucidated by single‑cell and spatial transcriptomics, revealing neuromuscular mTECs that ectopically express neuromuscular antigens, ectopic germinal centers, and altered immune microenvironments that drive autoantibody production.[20][8] Histopathologic classification via WHO criteria and staging via Masaoka–Koga and TNM systems underpin prognosis and treatment decisions, while immunohistochemistry and molecular profiling refine diagnosis and subtype identification.[5][14][15]

Treatment strategies for thymus neoplasms hinge on complete surgical resection for localized disease, with PORT indicated for incompletely resected or advanced thymomas, and systemic chemotherapy (e.g., PAC regimen) and emerging targeted and immunotherapies for unresectable or metastatic thymomas and thymic carcinomas.[4][16][18][9] Outcomes are strongly influenced by stage, histologic subtype, and margin status, with early‑stage thymomas achieving excellent long‑term survival and thymic carcinomas exhibiting poorer prognosis.[2][1][9] Paraneoplastic autoimmunity complicates management and impacts quality of life but may be associated with more favorable tumor features.[10]

From a knowledge base perspective, thymus neoplasms warrant rich annotation across ontologies, including MONDO (disease entity), MeSH (D013953), ICD‑10/11 codes, OMIM (274230 for thymoma), HPO terms for clinical and paraneoplastic phenotypes, GO terms for molecular and cellular processes, CL terms for relevant cell types (TECs, thymocytes, nmTECs, Tfh cells, B cells), UBERON terms for thymus and mediastinal anatomy, CHEBI entries for chemotherapy agents, and NCIT codes for interventions.[7][11][15][6][9][20] Evidence items should link mechanistic claims to primary literature, often via PubMed Central PMCID and associated PMIDs, and distinguish human clinical data from model organism and in vitro studies. As multi‑omics and advanced technologies continue to deepen our understanding of thymic epithelial tumors, disease knowledge bases can evolve to support precision diagnosis and treatment, integrating molecular profiles, cfDNA biomarkers, and immune microenvironment insights to guide individualized management of these rare but clinically and biologically compelling neoplasms.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.
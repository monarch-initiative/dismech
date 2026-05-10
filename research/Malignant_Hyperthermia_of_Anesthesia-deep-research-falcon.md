---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T08:46:39.931579'
end_time: '2026-05-09T08:57:32.297883'
duration_seconds: 652.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Malignant hyperthermia of anesthesia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Malignant hyperthermia of anesthesia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Malignant hyperthermia of anesthesia** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Malignant hyperthermia of anesthesia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Malignant hyperthermia of anesthesia** covering all of the
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


## Comprehensive Research Report: Malignant hyperthermia of anesthesia (malignant hyperthermia susceptibility)

### Executive summary
Malignant hyperthermia (MH) of anesthesia—often discussed as *malignant hyperthermia susceptibility* (MHS)—is a rare, potentially fatal pharmacogenetic disorder of skeletal muscle excitation–contraction coupling. Exposure to triggering anesthetics (volatile halogenated agents and/or succinylcholine) causes uncontrolled intracellular Ca2+ release, producing a hypermetabolic crisis with hypercapnia, acidosis, hyperkalemia, muscle rigidity, rhabdomyolysis, hyperthermia, and multiorgan failure if untreated (rosenberg2015malignanthyperthermiaa pages 1-2, frassanito2023realevidenceand pages 1-3). Mortality has decreased markedly since dantrolene became available, but delayed recognition and limited drug availability remain major real-world barriers (rosenberg2015malignanthyperthermiaa pages 1-2, toyota2023rapiddantroleneadministration pages 6-6).

| Topic | Concise summary | Strongest supporting citation IDs |
|---|---|---|
| Core definition | Malignant hyperthermia susceptibility (MHS) is a rare, life-threatening pharmacogenetic disorder of skeletal muscle excitation–contraction coupling in which exposure to triggering anesthetics causes uncontrolled intracellular Ca2+ release, hypermetabolism, rhabdomyolysis, and heat production. | (frassanito2023realevidenceand pages 1-3, rosenberg2015malignanthyperthermiaa pages 1-2) |
| Main triggers | Major anesthetic triggers are volatile halogenated anesthetics (desflurane, isoflurane, sevoflurane, halothane) and succinylcholine; non-anesthetic stressors such as exercise and heat can provoke MH-like events in some susceptible individuals. | (frassanito2023realevidenceand pages 1-3, rosenberg2015malignanthyperthermiaa pages 1-2, rosenberg2015malignanthyperthermiaa pages 12-13) |
| Key genes | Definitive/major genes are RYR1, CACNA1S, and STAC3; RYR1 is the predominant gene, explaining most genetically resolved cases, while CACNA1S accounts for a small minority and STAC3 is classically linked to recessive syndromic myopathy with MH risk. | (biesecker2020genomicscreeningfor pages 1-2, paranjpe2024candidatelociin pages 19-24, frassanito2023realevidenceand pages 1-3) |
| Inheritance | In humans, MHS is usually autosomal dominant with incomplete penetrance and variable expressivity; in pigs, malignant hyperthermia/porcine stress syndrome is classically autosomal recessive. | (frassanito2023realevidenceand pages 1-3, rosenberg2015malignanthyperthermiaa pages 1-2, riazi2018malignanthyperthermiain pages 1-3) |
| Key diagnostic tests | Gold-standard functional tests are IVCT/CHCT on biopsied muscle; clinical diagnosis can be supported by the Larach clinical grading scale when definitive testing is not immediately available; genetic testing is useful but does not exclude disease if negative. | (bin2022malignanthyperthermiaa pages 5-7, biesecker2020genomicscreeningfor pages 1-2, frassanito2023realevidenceand pages 9-10) |
| Hallmark clinical/lab features | Typical features include rapidly rising end-tidal CO2, tachycardia, muscle rigidity or masseter spasm, hyperthermia, metabolic and respiratory acidosis, hyperkalemia, rhabdomyolysis, myoglobinuria, and elevated creatine kinase. | (rosenberg2015malignanthyperthermiaa pages 1-2, rosenberg2015malignanthyperthermiaa pages 2-4, frassanito2023realevidenceand pages 1-3) |
| Epidemiology numbers | Reported MH reaction incidence during anesthesia ranges roughly from 1:10,000 to 1:250,000 anesthetics; prevalence of underlying genetic susceptibility has been estimated as high as ~1 in 400 in some sources, though other genomic estimates are lower/higher depending on method. | (rosenberg2015malignanthyperthermiaa pages 1-2, biesecker2020genomicscreeningfor pages 1-2, riazi2018malignanthyperthermiain pages 1-3) |
| Pediatric vs adult incidence | Children are disproportionately affected: one 2023 review states pediatric incidence is about five-fold higher than in adults, with estimated incidence about 1:10,000 in children versus 1:50,000 in adults; mean reaction age is ~18.3 years. | (frassanito2023realevidenceand pages 1-3, rosenberg2015malignanthyperthermiaa pages 2-4, rosenberg2015malignanthyperthermiaa pages 1-2) |
| Mortality trends | Mortality has fallen dramatically with recognition and dantrolene availability: historical estimates were ~70–80%, declining to <5% by 2006 in one major review; more recent series/reviews cite mortality in the low single digits to about 10% depending on cohort and treatment speed. | (rosenberg2015malignanthyperthermiaa pages 1-2, biesecker2020genomicscreeningfor pages 1-2, toyota2023rapiddantroleneadministration pages 6-6) |
| Acute management | Immediate actions are to stop triggering agents, call for help, hyperventilate with 100% oxygen, switch to non-triggering anesthesia/TIVA, administer IV dantrolene promptly, cool aggressively as indicated, and treat acidosis, hyperkalemia, arrhythmias, and renal complications. | (frassanito2023realevidenceand pages 9-10, banu2026advancesinmalignant pages 1-2, toyota2023rapiddantroleneadministration pages 6-6) |
| Dantrolene evidence | Dantrolene is the specific antidote; delayed administration is associated with worse outcomes, and in a 2023 Japanese cohort mortality was higher without dantrolene and worse when time to dantrolene and temperature at dosing were greater. | (toyota2023rapiddantroleneadministration pages 6-6, rosenberg2015malignanthyperthermiaa pages 1-2) |
| Prevention / trigger-free anesthesia | For known or suspected MHS, trigger-free anesthesia eliminates perioperative trigger risk; safe approaches include regional anesthesia and TIVA, with continuous EtCO2 and core-temperature monitoring throughout the perioperative period. | (frassanito2023realevidenceand pages 9-10, frassanito2023realevidenceand pages 1-3) |
| Anesthesia machine preparation / activated charcoal filters | Vaporizers should be removed, circuits and soda lime changed, and the machine flushed per manufacturer guidance; activated charcoal filters on inspiratory and expiratory limbs can reduce residual volatile concentration to <5 ppm within 2–3 min and maintain low levels for up to 12 h with fresh gas flow ≥3 L/min after a brief high-flow flush. | (frassanito2023realevidenceand pages 9-10, frassanito2023realevidenceand pages 13-15) |


*Table: This table condenses the highest-yield clinical and molecular facts about malignant hyperthermia susceptibility, including diagnosis, epidemiology, and perioperative management. It is useful as a rapid reference for building the full disease knowledge base entry.*

---

## 1. Disease information

### 1.1 Overview (definition)
**Definition (current understanding):** MH is “a rare but life-threatening pharmacogenetic disorder triggered by exposure to specific anesthetic agents” (Frassanito et al., *J Clin Med*, published 2023-06-06; DOI:10.3390/jcm12123869) (frassanito2023realevidenceand pages 1-3). A large authoritative review similarly defines MH as “a pharmacogenetic disorder of skeletal muscle” presenting as “a hypermetabolic response to potent volatile anesthetic gases… and the depolarizing muscle relaxant succinylcholine” (Rosenberg et al., *Orphanet J Rare Dis*, published 2015-08-13; DOI:10.1186/s13023-015-0310-1) (rosenberg2015malignanthyperthermiaa pages 1-2).

### 1.2 Key identifiers / ontology
*Note:* The present tool run retrieved and cited peer-reviewed literature; it did not retrieve structured disease-ontology records (e.g., MONDO browser pages). Therefore, **MONDO ID is not confirmed from primary context**.

- **OMIM (disease concept):** MH susceptibility locus is commonly referred to as **MHS1 / OMIM #145600** in the genetics literature (paranjpe2024candidatelociin pages 19-24).
- **Genes (OMIM gene entries referenced in context):** RYR1 is referenced with OMIM-style gene annotation and location 19q13.1 in major reviews (rosenberg2015malignanthyperthermiaa pages 1-2).
- **GeneReviews (authoritative clinical genetics resource):** A 2023 review cites *GeneReviews®* “Malignant Hyperthermia Susceptibility” as a standard reference (frassanito2023realevidenceand pages 13-15).
- **Other clinical classification systems (ICD/MeSH/Orphanet):** Not extractable from the current evidence corpus with citable IDs; should be added from OMIM/Orphanet/ICD/MeSH directly in a subsequent structured database query.

### 1.3 Synonyms / alternative names
Common names in the retrieved evidence:
- **Malignant hyperthermia (MH)** (rosenberg2015malignanthyperthermiaa pages 1-2)
- **Malignant hyperthermia susceptibility (MHS)** (frassanito2023realevidenceand pages 1-3)
- **Anesthesia-related malignant hyperthermia / malignant hyperthermia due to anesthesia** (implicit framing in perioperative reviews) (ruta2025perioperativenursingof pages 2-3)

### 1.4 Evidence source type
Most information here is derived from **aggregated disease-level resources** (narrative reviews, guideline-oriented reviews) (rosenberg2015malignanthyperthermiaa pages 1-2, frassanito2023realevidenceand pages 1-3) plus **observational registry/cohort analyses** informing risk and outcomes (e.g., dantrolene timing vs mortality) (toyota2023rapiddantroleneadministration pages 6-6).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal factor (genetic/pharmacogenetic):** MH is caused by inherited abnormalities in skeletal muscle excitation–contraction coupling that remain clinically silent until a trigger exposure. A 2015 authoritative review states “In most cases, the syndrome is caused by a defect in the ryanodine receptor” (rosenberg2015malignanthyperthermiaa pages 1-2).

**Trigger exposure (environmental/pharmacologic):** The principal environmental cause of an *episode* is exposure to triggering anesthetic agents: volatile halogenated anesthetics and succinylcholine (rosenberg2015malignanthyperthermiaa pages 1-2, frassanito2023realevidenceand pages 1-3).

### 2.2 Risk factors
#### Genetic risk factors
- **Major susceptibility genes:** RYR1 (predominant), CACNA1S (minor fraction), and STAC3 (notably associated with recessive syndromic myopathy with MH risk) (biesecker2020genomicscreeningfor pages 1-2, frassanito2023realevidenceand pages 1-3).
- **Variant heterogeneity:** Rosenberg et al. reports “Over 400 variants have been identified in the RYR1 gene… and at least 34 are causal for MH,” while “Less than 1% of variants have been found in CACNA1S but not all of these are causal” (rosenberg2015malignanthyperthermiaa pages 1-2).
- **Incomplete penetrance/variable expressivity:** Pediatric review notes MHS is autosomal dominant with incomplete penetrance (frassanito2023realevidenceand pages 1-3), consistent with post-genomics perspectives emphasizing discordance between variant prevalence and clinical incidence (riazi2018malignanthyperthermiain pages 1-3).

#### Environmental/pharmacologic risk factors
- **Anesthetic triggers:** volatile anesthetics and succinylcholine (rosenberg2015malignanthyperthermiaa pages 1-2, frassanito2023realevidenceand pages 1-3).
- **Non-anesthetic stressors:** vigorous exercise and heat are described as rare triggers in humans (rosenberg2015malignanthyperthermiaa pages 1-2, rosenberg2015malignanthyperthermiaa pages 12-13).

### 2.3 Protective factors
- **Primary protection is trigger avoidance:** For suspected/confirmed MHS, the “mere avoidance of triggering substances eliminates the risk of developing an MH event” perioperatively (frassanito2023realevidenceand pages 9-10).

### 2.4 Gene–environment interaction
The core interaction is **genotype-dependent vulnerability** + **drug exposure** (volatile anesthetics/succinylcholine) leading to crisis. Additional stressors (exercise/heat) are described in susceptible individuals, supporting broader gene–environment coupling beyond the operating room (rosenberg2015malignanthyperthermiaa pages 1-2, rosenberg2015malignanthyperthermiaa pages 12-13).

---

## 3. Phenotypes

### 3.1 Acute MH crisis phenotypes (perioperative)
**Core clinical signs (from authoritative review):** hyperthermia, tachycardia, tachypnea, increased CO2 production (hypercapnia/raised end-tidal CO2), increased oxygen consumption, acidosis, hyperkalemia, muscle rigidity, and rhabdomyolysis (rosenberg2015malignanthyperthermiaa pages 1-2).

**Early clue:** “An increase in end-tidal carbon dioxide despite increased minute ventilation provides an early diagnostic clue” (rosenberg2015malignanthyperthermiaa pages 1-2).

**Common laboratory abnormalities:** hyperkalemia and markedly elevated creatine kinase with rhabdomyolysis/myoglobinuria are central (rosenberg2015malignanthyperthermiaa pages 1-2). In masseter rigidity presentations, very high CK can support susceptibility in some cohorts (paranjpe2024candidatelociin pages 19-24).

### 3.2 Age of onset, severity, progression
- **Onset pattern:** typically **acute/fulminant** after trigger exposure during anesthesia (rosenberg2015malignanthyperthermiaa pages 1-2).
- **Age distribution:** reactions occur across the lifespan; a major review reports earliest confirmed 6 months and oldest 78 years; mean age ~18.3 years; children <15 represent ~52.1% of reactions (rosenberg2015malignanthyperthermiaa pages 2-4).
- **Severity:** ranges from abortive/early presentations (e.g., masseter spasm) to fulminant hypermetabolic crisis with multiorgan failure (ruta2025perioperativenursingof pages 2-3, rosenberg2015malignanthyperthermiaa pages 1-2).

### 3.3 Quality-of-life impact
Outside anesthesia, some MHS individuals may have chronic myopathic manifestations (e.g., myalgia, fatigue, episodic rhabdomyolysis), which can affect daily functioning; these phenotypes are noted in disease discussions of MHS and RyR1-related disease (rosenberg2015malignanthyperthermiaa pages 12-13).

### 3.4 Suggested HPO terms (examples; to be verified/expanded against HPO)
Based on manifestations described in the cited clinical literature:
- **Hyperthermia** (HP:0001945) (rosenberg2015malignanthyperthermiaa pages 1-2)
- **Hypercapnia / Increased end-tidal CO2** (HP:0001942; proxy term) (rosenberg2015malignanthyperthermiaa pages 1-2)
- **Metabolic acidosis** (HP:0001940) (rosenberg2015malignanthyperthermiaa pages 1-2)
- **Tachycardia** (HP:0001649) (rosenberg2015malignanthyperthermiaa pages 1-2)
- **Muscle rigidity** (HP:0001276) (rosenberg2015malignanthyperthermiaa pages 1-2)
- **Rhabdomyolysis** (HP:0003201) (rosenberg2015malignanthyperthermiaa pages 1-2)
- **Hyperkalemia** (HP:0002153) (rosenberg2015malignanthyperthermiaa pages 1-2)
- **Myoglobinuria** (HP:0002928) (rosenberg2015malignanthyperthermiaa pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes (and role)
- **RYR1 (ryanodine receptor 1):** dominant MH susceptibility gene and the principal cause in most genetically resolved cases (rosenberg2015malignanthyperthermiaa pages 1-2, biesecker2020genomicscreeningfor pages 1-2).
- **CACNA1S (Cav1.1 / DHPR α1S):** less common contributor to MH susceptibility (rosenberg2015malignanthyperthermiaa pages 1-2, biesecker2020genomicscreeningfor pages 1-2).
- **STAC3:** implicated in MH susceptibility particularly in the context of congenital myopathy (Native American myopathy), typically recessive (biesecker2020genomicscreeningfor pages 1-2, paranjpe2024candidatelociin pages 19-24).

### 4.2 Pathogenic variants and functional consequences
- **Variant burden:** RYR1 has >400 reported variants with a smaller subset accepted as causal/diagnostically actionable; CACNA1S contributes a small fraction (rosenberg2015malignanthyperthermiaa pages 1-2).
- **Functional consequence:** sustained/inappropriate intracellular Ca2+ release leading to ATP depletion, thermogenesis, and muscle breakdown is the unifying mechanism (frassanito2023realevidenceand pages 1-3).

### 4.3 Modifier genes / polygenic models
A threshold/multifactorial model has been proposed to explain disparities between variant prevalence and observed clinical incidence (riazi2018malignanthyperthermiain pages 1-3, paranjpe2024candidatelociin pages 19-24). This supports the idea that additional genetic modifiers and/or environmental cofactors influence clinical expression.

### 4.4 Epigenetic information
Discordance between genotype and phenotype has been attributed in part to epigenetic changes at the RYR1 locus (e.g., altered muscle-specific microRNAs and gene silencing) in a major review (rosenberg2015malignanthyperthermiaa pages 13-14).

---

## 5. Environmental information

### 5.1 Environmental/iatrogenic triggers
- **Volatile halogenated anesthetics** (desflurane, isoflurane, sevoflurane, halothane) and **succinylcholine** are primary triggers (frassanito2023realevidenceand pages 1-3, rosenberg2015malignanthyperthermiaa pages 1-2).
- **Stressors** (exercise/heat) may trigger MH-like events in susceptible individuals (rosenberg2015malignanthyperthermiaa pages 1-2).

### 5.2 Lifestyle factors / infectious agents
No specific lifestyle or infectious causes are established as primary causes in the cited evidence; rather, they may modulate risk in susceptible individuals, and consensus is limited (rosenberg2015malignanthyperthermiaa pages 13-14).

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (trigger → molecular event → phenotype)
1. **Trigger exposure** (volatile anesthetics and/or succinylcholine) in a genetically susceptible individual (frassanito2023realevidenceand pages 1-3).
2. **Excitation–contraction coupling dysfunction** leads to excessive SR Ca2+ release (RYR1/Cav1.1/STAC3 pathway) (frassanito2023realevidenceand pages 1-3, riazi2018malignanthyperthermiain pages 1-3).
3. **Sustained myoplasmic Ca2+ elevation** drives sustained contraction, ATP consumption, heat production, CO2 production, acidosis, and muscle breakdown (rhabdomyolysis) (frassanito2023realevidenceand pages 1-3, rosenberg2015malignanthyperthermiaa pages 1-2).
4. **Downstream systemic complications**: hyperkalemia, arrhythmia, acute kidney injury (from myoglobin), disseminated intravascular coagulation at extreme temperatures, and multiorgan failure (rosenberg2015malignanthyperthermiaa pages 2-4).

### 6.2 Molecular pathways / cellular processes (suggestions)
- **GO biological process candidates:** calcium ion homeostasis; regulation of cytosolic calcium ion concentration; skeletal muscle contraction; ATP metabolic process; response to heat; cell death/necrosis secondary to metabolic crisis (supported conceptually by mechanistic descriptions) (frassanito2023realevidenceand pages 1-3, riazi2018malignanthyperthermiain pages 1-3).
- **Cell types (CL suggestions):** skeletal muscle myocytes (e.g., skeletal muscle fiber cell) are primary affected cells (rosenberg2015malignanthyperthermiaa pages 1-2).

### 6.3 Visual evidence (pathway schematic)
Figure evidence for excitation–contraction coupling dysfunction and dantrolene mechanism is available from a 2023 review figure (frassanito2023realevidenceand media 1892a3c8).

---

## 7. Anatomical structures affected

### 7.1 Organ and system level
- **Primary tissue:** **skeletal muscle** (hypermetabolic crisis originates in myocytes) (rosenberg2015malignanthyperthermiaa pages 1-2, frassanito2023realevidenceand pages 1-3).
- **Secondary organ involvement (complications):** cardiovascular system (tachycardia/arrhythmia), kidneys (myoglobin-associated injury), systemic coagulation abnormalities at extreme hyperthermia (rosenberg2015malignanthyperthermiaa pages 2-4).

### 7.2 Subcellular localization (mechanistic)
- **Sarcoplasmic reticulum Ca2+ release channel complex** (RyR1) is central (frassanito2023realevidenceand pages 1-3).

### 7.3 Suggested anatomy ontology terms
- **UBERON:** skeletal muscle tissue (UBERON:0001134)

---

## 8. Temporal development

### 8.1 Onset
- **Acute onset** typically occurs intraoperatively or in the early postoperative period after trigger exposure (rosenberg2015malignanthyperthermiaa pages 1-2).

### 8.2 Course / progression
- **Rapid progression** to hypermetabolic crisis if triggers are not stopped and dantrolene/supportive care not instituted (rosenberg2015malignanthyperthermiaa pages 1-2).
- **Potential recurrence:** monitoring for recurrence after initial control is emphasized in management discussions (banu2026advancesinmalignant pages 1-2).

---

## 9. Inheritance and population

### 9.1 Inheritance
- **Humans:** typically **autosomal dominant**, with incomplete penetrance and variable expressivity (rosenberg2015malignanthyperthermiaa pages 1-2, frassanito2023realevidenceand pages 1-3).
- **Pigs:** classically **autosomal recessive** in porcine stress syndrome/porcine MH (rosenberg2015malignanthyperthermiaa pages 1-2).

### 9.2 Epidemiology (statistics)
**Incidence (during anesthesia):** A major review reports “The incidence of MH reactions ranges from 1:10,000 to 1: 250,000 anesthetics” (rosenberg2015malignanthyperthermiaa pages 1-2).

**Genetic prevalence:** The same review states “the prevalence of the genetic abnormalities may be as great as one in 400 individuals” (rosenberg2015malignanthyperthermiaa pages 1-2). (Genomics-oriented reviews note substantial variability in prevalence estimates depending on ascertainment and variant curation) (biesecker2020genomicscreeningfor pages 1-2, riazi2018malignanthyperthermiain pages 1-3).

**Age/sex distribution:** Male predominance (~2:1) and pediatric overrepresentation are reported in major summaries (rosenberg2015malignanthyperthermiaa pages 1-2, frassanito2023realevidenceand pages 1-3).

---

## 10. Diagnostics

### 10.1 Clinical tests / biomarkers
- **Functional contracture testing (gold standard):** in vitro contracture testing of biopsied muscle with halothane and caffeine (IVCT/CHCT) remains central (rosenberg2015malignanthyperthermiaa pages 1-2, bin2022malignanthyperthermiaa pages 5-7).
- **Clinical scoring (when definitive tests unavailable):** Larach Clinical Grading Scale is referenced as a tool to aid diagnosis when functional/genetic confirmation is not immediately available (bin2022malignanthyperthermiaa pages 5-7).
- **Laboratory:** CK elevation and rhabdomyolysis markers (hyperkalemia, myoglobinuria) support diagnosis and severity (rosenberg2015malignanthyperthermiaa pages 1-2).

### 10.2 Genetic testing approach (current practice)
NGS and gene panels focusing on **RYR1, CACNA1S, STAC3** are emphasized as increasingly used in neuromuscular and perioperative risk workups, but negative genetic testing does not exclude susceptibility given heterogeneity and incomplete knowledge (frassanito2023realevidenceand pages 1-3, bin2022malignanthyperthermiaa pages 5-7).

### 10.3 Diagnostic pathway (visual evidence)
A 2023 pediatric-focused review provides a diagnostic pathway/algorithm figure for investigating MH susceptibility (frassanito2023realevidenceand media 2ab373ad).

### 10.4 Differential diagnosis
Perioperative hypermetabolic/rhabdomyolysis phenotypes overlap with other syndromes (e.g., anesthesia-induced rhabdomyolysis), creating diagnostic dilemmas noted in perioperative literature (ruta2025perioperativenursingof pages 2-3).

---

## 11. Outcome / prognosis

### 11.1 Mortality and morbidity trends
Mortality has decreased substantially with improved recognition and dantrolene availability: Rosenberg et al. states mortality decreased “from 80% thirty years ago to <5% in 2006” (rosenberg2015malignanthyperthermiaa pages 1-2). Delays in dantrolene and inadequate monitoring are associated with higher complication and mortality risk in modern analyses (rosenberg2015malignanthyperthermiaa pages 2-4, toyota2023rapiddantroleneadministration pages 6-6).

### 11.2 Prognostic factors (examples)
- **Time to dantrolene** and **temperature at the time of administration** are associated with prognosis in modern observational analyses of severe MH events (toyota2023rapiddantroleneadministration pages 6-6).
- **Adequate core temperature monitoring** is associated with reduced risk of death/complications in perioperative MH analyses summarized in authoritative reviews (rosenberg2015malignanthyperthermiaa pages 2-4).

---

## 12. Treatment

### 12.1 Acute pharmacotherapy
- **Dantrolene sodium** is the specific antagonist/antidote and should be available wherever general anesthesia is administered (rosenberg2015malignanthyperthermiaa pages 1-2). Early administration is emphasized as life-saving in modern outcome analyses (toyota2023rapiddantroleneadministration pages 6-6).

**CHEBI suggestion:** dantrolene (CHEBI identifier should be added from CHEBI database in a structured follow-up query; not retrievable from current context).

**MAXO suggestions (examples; to be verified/expanded against MAXO):** dantrolene administration; trigger agent discontinuation; active cooling; hyperkalemia treatment; intensive care monitoring.

### 12.2 Supportive care (real-world implementation)
Supportive measures include stopping triggers, ventilating with 100% oxygen, cooling, and correction of metabolic derangements (acidosis/hyperkalemia), with ICU-level monitoring for complications/recurrence (frassanito2023realevidenceand pages 9-10, rosenberg2015malignanthyperthermiaa pages 1-2).

### 12.3 Anesthesia machine preparation and activated charcoal filters
For patients with known/suspected MHS, trigger-free anesthesia is recommended and workstation preparation is operationally important. A 2023 review specifies:
- remove vaporizers; replace breathing circuits and soda lime; flush machine per manufacturer guidance (frassanito2023realevidenceand pages 9-10).
- **Activated charcoal filters (ACFs):** “have been shown to rapidly and cost-efficiently decrease the concentration of anesthetic vapors to <5 ppm in 2–3 min and to maintain this low concentration… for up to 12 h with fresh gas flows of at least 3 L min−1” and should be applied to inspiratory and expiratory limbs; additionally, “the anesthesia machine will still need to be flushed with high fresh gas flows (≥10 L/min) for 90 s before placing the activated charcoal filters” (frassanito2023realevidenceand pages 9-10).

---

## 13. Prevention

### 13.1 Primary prevention (perioperative)
- **Risk identification** (family/personal history, congenital myopathy features, prior anesthetic events) and **planning trigger-free anesthesia** (regional anesthesia or TIVA) with continuous EtCO2 and core temperature monitoring (frassanito2023realevidenceand pages 9-10).
- **System readiness:** cognitive aids, MH carts/kits, simulation training, and rapid access to dantrolene (frassanito2023realevidenceand pages 9-10, ruta2025perioperativenursingof pages 2-3).

### 13.2 Secondary prevention
- **Confirming susceptibility in families:** IVCT/CHCT and/or genetic testing in specialized centers to guide future anesthesia planning (bin2022malignanthyperthermiaa pages 5-7, frassanito2023realevidenceand pages 1-3).

---

## 14. Other species / natural disease
MH occurs in multiple species: “MH affects humans, certain pig breeds, dogs and horses” (rosenberg2015malignanthyperthermiaa pages 1-2). Inheritance differs: autosomal dominant in humans versus autosomal recessive in pigs (rosenberg2015malignanthyperthermiaa pages 1-2).

---

## 15. Model organisms
Multiple models are used to study Ca2+ dysregulation and to test interventions:
- **Pig models (porcine stress syndrome)** as a natural disease model (rosenberg2015malignanthyperthermiaa pages 1-2).
- **Mouse models** with RYR1 variants and Ca2+ dysregulation discussed in major reviews (kan2025researchhotspotsand pages 12-12, rosenberg2015malignanthyperthermiaa pages 12-13).

---

## Recent developments (2023–2024 emphasis) and expert analysis
1. **Operational prevention has become more systematized:** 2023 pediatric-focused synthesis emphasizes trigger-free hospitalization, workstation preparation, and activated charcoal filters to rapidly achieve safe low volatile concentrations (frassanito2023realevidenceand pages 9-10, frassanito2023realevidenceand pages 1-3).
2. **Quantitative outcomes research reinforces “time-to-dantrolene” as critical:** modern observational analyses (Japan) associate delayed dantrolene and higher temperatures at administration with mortality, reinforcing rapid-response protocols (toyota2023rapiddantroleneadministration pages 6-6).
3. **Diagnostics are shifting toward integrated, less invasive strategies:** Reviews highlight the expanding use of NGS, the challenge of RYR1 VUS interpretation, and the need for shared variant databases and functional correlation to avoid unnecessary invasive testing (frassanito2023realevidenceand pages 13-15).

---

## Data gaps relative to the template (not retrievable from current citable context)
- MONDO ID, Orphanet ID, MeSH, and ICD-10/ICD-11 mappings were not directly retrievable from the current evidence corpus with citable IDs.
- Detailed allele frequencies (gnomAD) and ClinVar/ClinGen pathogenicity summaries for specific variants were not retrieved in this run.

These elements should be added via targeted queries to OMIM/Orphanet/MONDO/MeSH/ClinVar/gnomAD in a subsequent structured database retrieval step.


References

1. (rosenberg2015malignanthyperthermiaa pages 1-2): Henry Rosenberg, Neil Pollock, Anja Schiemann, Terasa Bulger, and Kathryn Stowell. Malignant hyperthermia: a review. Orphanet Journal of Rare Diseases, Aug 2015. URL: https://doi.org/10.1186/s13023-015-0310-1, doi:10.1186/s13023-015-0310-1. This article has 793 citations and is from a peer-reviewed journal.

2. (frassanito2023realevidenceand pages 1-3): Luciano Frassanito, Fabio Sbaraglia, Alessandra Piersanti, Francesco Vassalli, Monica Lucente, Nicoletta Filetici, Bruno Antonio Zanfini, Stefano Catarci, and Gaetano Draisci. Real evidence and misconceptions about malignant hyperthermia in children: a narrative review. Journal of Clinical Medicine, 12:3869, Jun 2023. URL: https://doi.org/10.3390/jcm12123869, doi:10.3390/jcm12123869. This article has 20 citations.

3. (toyota2023rapiddantroleneadministration pages 6-6): Yukari Toyota, Takashi Kondo, Daiki Shorin, Ayako Sumii, Kenshiro Kido, Tomoyuki Watanabe, Sachiko Otsuki, Rieko Kanzaki, Hirotsugu Miyoshi, Toshimichi Yasuda, Yousuke T. Horikawa, Keiko Mukaida, and Yasuo M. Tsutsumi. Rapid dantrolene administration with body temperature monitoring is associated with decreased mortality in japanese malignant hyperthermia events. BioMed Research International, Feb 2023. URL: https://doi.org/10.1155/2023/8340209, doi:10.1155/2023/8340209. This article has 12 citations.

4. (rosenberg2015malignanthyperthermiaa pages 12-13): Henry Rosenberg, Neil Pollock, Anja Schiemann, Terasa Bulger, and Kathryn Stowell. Malignant hyperthermia: a review. Orphanet Journal of Rare Diseases, Aug 2015. URL: https://doi.org/10.1186/s13023-015-0310-1, doi:10.1186/s13023-015-0310-1. This article has 793 citations and is from a peer-reviewed journal.

5. (biesecker2020genomicscreeningfor pages 1-2): Leslie G. Biesecker, Robert T. Dirksen, Thierry Girard, Philip M. Hopkins, Sheila Riazi, Henry Rosenberg, Kathryn Stowell, and James Weber. Genomic screening for malignant hyperthermia susceptibility. Anesthesiology, 133:1277-1282, Sep 2020. URL: https://doi.org/10.1097/aln.0000000000003547, doi:10.1097/aln.0000000000003547. This article has 40 citations and is from a domain leading peer-reviewed journal.

6. (paranjpe2024candidatelociin pages 19-24): R Paranjpe. Candidate loci in a threshold model of malignant hyperthermia. Unknown journal, 2024.

7. (riazi2018malignanthyperthermiain pages 1-3): Sheila Riazi, Natalia Kraeva, and Philip M. Hopkins. Malignant hyperthermia in the post-genomics era: new perspectives on an old concept. Anesthesiology, 128 1:168-180, Jan 2018. URL: https://doi.org/10.1097/aln.0000000000001878, doi:10.1097/aln.0000000000001878. This article has 195 citations and is from a domain leading peer-reviewed journal.

8. (bin2022malignanthyperthermiaa pages 5-7): Xin Bin, Baisheng Wang, and Zhangui Tang. Malignant hyperthermia: a killer if ignored. Journal of PeriAnesthesia Nursing, 37:435-444, Aug 2022. URL: https://doi.org/10.1016/j.jopan.2021.08.018, doi:10.1016/j.jopan.2021.08.018. This article has 25 citations and is from a peer-reviewed journal.

9. (frassanito2023realevidenceand pages 9-10): Luciano Frassanito, Fabio Sbaraglia, Alessandra Piersanti, Francesco Vassalli, Monica Lucente, Nicoletta Filetici, Bruno Antonio Zanfini, Stefano Catarci, and Gaetano Draisci. Real evidence and misconceptions about malignant hyperthermia in children: a narrative review. Journal of Clinical Medicine, 12:3869, Jun 2023. URL: https://doi.org/10.3390/jcm12123869, doi:10.3390/jcm12123869. This article has 20 citations.

10. (rosenberg2015malignanthyperthermiaa pages 2-4): Henry Rosenberg, Neil Pollock, Anja Schiemann, Terasa Bulger, and Kathryn Stowell. Malignant hyperthermia: a review. Orphanet Journal of Rare Diseases, Aug 2015. URL: https://doi.org/10.1186/s13023-015-0310-1, doi:10.1186/s13023-015-0310-1. This article has 793 citations and is from a peer-reviewed journal.

11. (banu2026advancesinmalignant pages 1-2): Shaistha Banu and Sushmitha R. Shenoy. Advances in malignant hyperthermia: pathophysiology, diagnosis and management. International Journal of Research in Medical Sciences, 14:1759-1767, Mar 2026. URL: https://doi.org/10.18203/2320-6012.ijrms20260999, doi:10.18203/2320-6012.ijrms20260999. This article has 0 citations.

12. (frassanito2023realevidenceand pages 13-15): Luciano Frassanito, Fabio Sbaraglia, Alessandra Piersanti, Francesco Vassalli, Monica Lucente, Nicoletta Filetici, Bruno Antonio Zanfini, Stefano Catarci, and Gaetano Draisci. Real evidence and misconceptions about malignant hyperthermia in children: a narrative review. Journal of Clinical Medicine, 12:3869, Jun 2023. URL: https://doi.org/10.3390/jcm12123869, doi:10.3390/jcm12123869. This article has 20 citations.

13. (ruta2025perioperativenursingof pages 2-3): Federico Ruta, Annalisa Della Monica, Francesca Dal Mas, Tatiana Bolgeo, Ippolito Notarnicola, Cataldo Procacci, Paolo Ferrara, Alice Masini, Stefano Mancin, Giovanni Cangelosi, Mauro Parozzi, and Francesco Sacchini. Peri-operative nursing of patients with malignant hyperthermia: a narrative literature review. Surgeries, 6:78, Sep 2025. URL: https://doi.org/10.3390/surgeries6030078, doi:10.3390/surgeries6030078. This article has 0 citations.

14. (rosenberg2015malignanthyperthermiaa pages 13-14): Henry Rosenberg, Neil Pollock, Anja Schiemann, Terasa Bulger, and Kathryn Stowell. Malignant hyperthermia: a review. Orphanet Journal of Rare Diseases, Aug 2015. URL: https://doi.org/10.1186/s13023-015-0310-1, doi:10.1186/s13023-015-0310-1. This article has 793 citations and is from a peer-reviewed journal.

15. (frassanito2023realevidenceand media 1892a3c8): Luciano Frassanito, Fabio Sbaraglia, Alessandra Piersanti, Francesco Vassalli, Monica Lucente, Nicoletta Filetici, Bruno Antonio Zanfini, Stefano Catarci, and Gaetano Draisci. Real evidence and misconceptions about malignant hyperthermia in children: a narrative review. Journal of Clinical Medicine, 12:3869, Jun 2023. URL: https://doi.org/10.3390/jcm12123869, doi:10.3390/jcm12123869. This article has 20 citations.

16. (frassanito2023realevidenceand media 2ab373ad): Luciano Frassanito, Fabio Sbaraglia, Alessandra Piersanti, Francesco Vassalli, Monica Lucente, Nicoletta Filetici, Bruno Antonio Zanfini, Stefano Catarci, and Gaetano Draisci. Real evidence and misconceptions about malignant hyperthermia in children: a narrative review. Journal of Clinical Medicine, 12:3869, Jun 2023. URL: https://doi.org/10.3390/jcm12123869, doi:10.3390/jcm12123869. This article has 20 citations.

17. (kan2025researchhotspotsand pages 12-12): Hou-Ming Kan, Chi Wang, Jin-Zhao Huang, Meng-Liu Sha, Hong-Yan Ni, Li-Ping Chen, and Xiao-Tong Ding. Research hotspots and trends in malignant hyperthermia due to anesthesia from a global perspective: a bibliometric analysis from 1975 to 2024. Orphanet Journal of Rare Diseases, Jul 2025. URL: https://doi.org/10.1186/s13023-025-03766-5, doi:10.1186/s13023-025-03766-5. This article has 1 citations and is from a peer-reviewed journal.
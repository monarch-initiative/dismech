---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:37:58.038499'
end_time: '2026-05-09T11:54:45.275481'
duration_seconds: 1007.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Malignant Mesothelioma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Malignant Mesothelioma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Malignant Mesothelioma** covering all of the
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
- **Disease Name:** Malignant Mesothelioma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Malignant Mesothelioma** covering all of the
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


## Comprehensive Research Report: Malignant Mesothelioma (MM)

### Target Disease
- **Disease name:** Malignant mesothelioma (MM)
- **MONDO ID:** *Not found in retrieved sources (must be filled from MONDO)* (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2)
- **Category:** Malignant neoplasm of mesothelial-lined serosal surfaces (pleura, peritoneum, etc.) (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2)

### Executive summary (current understanding; 2023–2024 prioritized)
Malignant mesothelioma is a rare, aggressive cancer arising from mesothelial linings, most commonly the pleura (about 80–85% of cases) and less commonly the peritoneum. It is strongly associated with asbestos exposure and is characterized by long latency (often decades), late presentation, and poor overall survival (population 5-year OS frequently reported around ~10–12%). Over 2023–2024, the major clinical development is consolidation of immune checkpoint blockade as a first-line option for unresectable pleural mesothelioma (notably nivolumab + ipilimumab, supported by CheckMate 743), alongside continuing chemotherapy backbones (platinum + pemetrexed) and targeted diagnostic innovation (BAP1 and MTAP immunohistochemistry; CDKN2A/p16 FISH). Current authoritative guidelines (NCCN 2023 for peritoneal; ASCO update 2025 for pleural) emphasize careful surgical selection, routine consideration of germline testing (especially BAP1), and algorithmic first-line systemic therapy selection. (cedres2023currentstateofthearttherapy pages 1-2, chiec2024immunotherapyfortreatment pages 1-2, jain2024malignantpleuralmesothelioma pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2, kindler2025treatmentofpleural pages 2-3)

| Concept | Value | Source (paper/guideline + year) | URL | Notes |
|---|---|---|---|---|
| Preferred disease name | Malignant mesothelioma | Zahiu et al. 2025; NCCN Peritoneal Mesothelioma 2023 | https://doi.org/10.3390/diagnostics15111323; https://doi.org/10.6004/jnccn.2023.0045 | General disease term used across pleural, peritoneal, and other mesothelial sites; NCCN notes the term “malignant” is no longer used for classification because all mesotheliomas are now defined as malignant. (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2) |
| Major subtype/site-specific name | Malignant pleural mesothelioma (MPM) | Cedres et al. 2023; Jain et al. 2024 | https://doi.org/10.3390/cancers15245787; https://doi.org/10.3390/jcm13195837 | Pleural form is described as the most common presentation. (cedres2023currentstateofthearttherapy pages 1-2, jain2024malignantpleuralmesothelioma pages 1-2) |
| Major subtype/site-specific name | Pleural mesothelioma (PM) | Lewandowska & Kowalski 2024 | https://doi.org/10.5603/ocp.100725 | Used in recent review/guideline-style literature as shorthand for pleural mesothelioma. (lewandowska2024diagnosisandtreatment pages 1-2) |
| Major subtype/site-specific name | Peritoneal mesothelioma (PeM) | NCCN Peritoneal Mesothelioma 2023 | https://doi.org/10.6004/jnccn.2023.0045 | NCCN guideline abbreviation for the peritoneal form. (ettinger2023mesotheliomaperitonealversion pages 1-2) |
| Synonym/related term in context | Pleural mesothelioma | Chiec & Bruno 2024 | https://doi.org/10.3390/ijms251910861 | Used without “malignant” in WHO-style histologic classification discussion. (chiec2024immunotherapyfortreatment pages 1-2) |
| Synonym/related term in context | Mesothelioma | NCCN Peritoneal Mesothelioma 2023 | https://doi.org/10.6004/jnccn.2023.0045 | Broad term used in NCCN overview for cancers arising from mesothelial surfaces. (ettinger2023mesotheliomaperitonealversion pages 1-2) |
| Anatomical descriptor | Pleura (most common site) | Zahiu et al. 2025 | https://doi.org/10.3390/diagnostics15111323 | Review states pleura is affected in 80–85% of cases. (zahiu2025molecularinsightsinto pages 1-2) |
| Anatomical descriptor | Peritoneum | NCCN Peritoneal Mesothelioma 2023 | https://doi.org/10.6004/jnccn.2023.0045 | Recognized less common site compared with pleura. (ettinger2023mesotheliomaperitonealversion pages 1-2) |
| Histologic subtype | Epithelioid | Chiec & Bruno 2024; Lewandowska & Kowalski 2024 | https://doi.org/10.3390/ijms251910861; https://doi.org/10.5603/ocp.100725 | One of the three major histologic subtypes. (chiec2024immunotherapyfortreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2) |
| Histologic subtype | Sarcomatoid | Chiec & Bruno 2024; Lewandowska & Kowalski 2024 | https://doi.org/10.3390/ijms251910861; https://doi.org/10.5603/ocp.100725 | One of the three major histologic subtypes. (chiec2024immunotherapyfortreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2) |
| Histologic subtype | Biphasic / mixed | Chiec & Bruno 2024; Lewandowska & Kowalski 2024 | https://doi.org/10.3390/ijms251910861; https://doi.org/10.5603/ocp.100725 | Biphasic is also described as mixed in some sources. (chiec2024immunotherapyfortreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2) |
| MONDO ID | Not found in retrieved sources | Not reported in retrieved context |  | Should be filled from MONDO directly. (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2) |
| MeSH ID/term | Not found in retrieved sources | Not reported in retrieved context |  | Should be filled from MeSH directly. (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2) |
| ICD-10 code | Not found in retrieved sources | Not reported in retrieved context |  | Should be filled from ICD-10 resources directly. (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2) |
| ICD-11 code | Not found in retrieved sources | Not reported in retrieved context |  | Should be filled from ICD-11 resources directly. (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2) |
| Orphanet ID | Not found in retrieved sources | Not reported in retrieved context |  | Should be filled from Orphanet directly. (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2) |
| OMIM ID | Not found in retrieved sources | Not reported in retrieved context |  | Disease-level OMIM identifier was not present in the retrieved sources; gene-level OMIM resources may still be relevant for predisposition syndromes such as BAP1-related disease. (kindler2025treatmentofpleural pages 2-3, lewandowska2024diagnosisandtreatment pages 1-2) |


*Table: This table summarizes disease names, related synonyms, and identifier availability for malignant mesothelioma using only the retrieved context. It also flags key ontology/code fields that were not present and should be completed from primary terminology resources.*

---

## 1. Disease Information

### 1.1 Definition and overview
- **Definition:** MM is a malignant tumor arising from mesothelial lining cells of serosal membranes (pleura most commonly; also peritoneum and other sites). (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2)
- **Site distribution:** Pleura is affected in **~80–85%** of cases; peritoneum is less common. (zahiu2025molecularinsightsinto pages 1-2)
- **Terminology evolution:** NCCN notes that the term **“malignant” is no longer used to classify mesotheliomas because all mesotheliomas are now defined as malignant**. (ettinger2023mesotheliomaperitonealversion pages 1-2)

### 1.2 Key identifiers (ontology/coding)
The retrieved full texts did **not** contain MONDO/MeSH/ICD/Orphanet codes. These should be populated directly from those terminology resources.
- **MONDO:** not found in retrieved sources (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2)
- **MeSH:** not found in retrieved sources (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2)
- **ICD-10 / ICD-11:** not found in retrieved sources (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2)
- **Orphanet:** not found in retrieved sources (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2)

### 1.3 Synonyms / alternative names (common in practice)
- “Malignant pleural mesothelioma (MPM)” (cedres2023currentstateofthearttherapy pages 1-2, jain2024malignantpleuralmesothelioma pages 1-2)
- “Pleural mesothelioma (PM)” (lewandowska2024diagnosisandtreatment pages 1-2)
- “Peritoneal mesothelioma (PeM)” (ettinger2023mesotheliomaperitonealversion pages 1-2)

### 1.4 Evidence provenance (patient-level vs aggregated)
- The information summarized here is primarily from **aggregated disease-level resources**: narrative/systematic reviews and clinical practice guidelines, as well as registry-based epidemiology. (cedres2023currentstateofthearttherapy pages 1-2, chiec2024immunotherapyfortreatment pages 1-2, jain2024malignantpleuralmesothelioma pages 1-2, bertin2023thecurrenttreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2, OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma)

---

## 2. Etiology

### 2.1 Primary causal factors
**Environmental/occupational exposure**
- Asbestos exposure is repeatedly identified as the dominant causal factor for pleural mesothelioma, with some reviews stating **>80%** of pleural cases are linked to asbestos. (bertin2023thecurrenttreatment pages 1-2, cedres2023currentstateofthearttherapy pages 1-2)
- A dose–response relationship is emphasized in pleural mesothelioma: cumulative exposure, duration, and long latency increase risk. (zahiu2025molecularinsightsinto pages 1-2)

**Genetic predisposition**
- **Germline BAP1** pathogenic variants are highlighted as an important inherited risk factor; ASCO notes mesothelioma patients “often have germline mutations, most commonly in…BAP1,” supporting offering germline testing broadly. (kindler2025treatmentofpleural pages 2-3)

### 2.2 Risk factors (genetic + environmental)
- **Environmental:** inhalational asbestos exposure with latency often **15–40 years** (reported for pleural mesothelioma). (chiec2024immunotherapyfortreatment pages 1-2)
- **Demographic:** male predominance (~70% male in one 2025 review summary; similar directionality in other sources). (zahiu2025molecularinsightsinto pages 1-2)
- **Histology and stage** influence prognosis and are part of risk stratification rather than causal risk (epithelioid vs sarcomatoid). (chiec2024immunotherapyfortreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors were explicitly identified in the retrieved sources.

### 2.4 Gene–environment interaction
A clinically important interaction is suggested by the co-occurrence of strong environmental exposure (asbestos) with genetic susceptibility (BAP1). While detailed gene–environment quantitative interaction models were not present in the retrieved excerpts, the guideline-level emphasis on universal germline testing implies that inherited susceptibility can meaningfully alter risk and counseling, especially in asbestos-exposed populations. (kindler2025treatmentofpleural pages 2-3, lewandowska2024diagnosisandtreatment pages 1-2)

---

## 3. Phenotypes

### 3.1 Key symptoms/signs (with suggested HPO mapping)
Common pleural presentations include dyspnea, pleural effusion, chest pain, cough, and weight loss. Jain et al. (2024) reports **pleural effusion in ~90%** of patients and lists dyspnea, chest pain, cough, weight loss, and chest wall masses as common presenting features. (jain2024malignantpleuralmesothelioma pages 1-2)

| Phenotype (plain language) | Suggested HPO term label | HPO ID | Frequency/notes | Typical context (pleural vs peritoneal) | Evidence type (human clinical/review) |
|---|---|---|---|---|---|
| Shortness of breath / dyspnea | Dyspnea |  | Common presenting symptom; reported among common features and in one review as part of symptoms occurring in ~90% with pain | Pleural | Human clinical/review (jain2024malignantpleuralmesothelioma pages 1-2, tyagi2024germlinebap1mutation pages 14-17) |
| Pleural effusion | Pleural effusion |  | ~90% of patients in one review; right-sided in ~60% in another source | Pleural | Human clinical/review (jain2024malignantpleuralmesothelioma pages 1-2, tyagi2024germlinebap1mutation pages 14-17) |
| Chest pain / chest wall pain | Chest pain |  | Common; grouped with dyspnea/pain among major presenting symptoms; adverse prognostic factor in one source | Pleural | Human clinical/review (jain2024malignantpleuralmesothelioma pages 1-2, tyagi2024germlinebap1mutation pages 14-17, tyagi2024germlinebap1mutation pages 11-14) |
| Cough | Cough |  | Common presenting symptom; can be unproductive in pleural mesothelioma | Pleural | Human clinical/review (jain2024malignantpleuralmesothelioma pages 1-2, tyagi2024germlinebap1mutation pages 11-14, tyagi2024germlinebap1mutation pages 14-17) |
| Weight loss | Weight loss |  | Common presenting feature | Pleural | Human clinical/review (jain2024malignantpleuralmesothelioma pages 1-2) |
| Chest wall mass | Thoracic mass |  | Reported as a presenting manifestation | Pleural | Human clinical/review (jain2024malignantpleuralmesothelioma pages 1-2) |
| Abdominal distension | Abdominal distension |  | Reported for peritoneal mesothelioma presentations | Peritoneal | Human clinical/review (tyagi2024germlinebap1mutation pages 14-17) |
| Abdominal pain | Abdominal pain |  | Reported for peritoneal mesothelioma presentations | Peritoneal | Human clinical/review (tyagi2024germlinebap1mutation pages 14-17) |
| Disseminated malignant process at diagnosis | Neoplasm of the pleura |  | Often disseminated at diagnosis because of long latency and late presentation | Mainly pleural | Human clinical/review (lewandowska2024diagnosisandtreatment pages 1-2) |
| Poor performance status / functional decline | Reduced performance status |  | Reported as a negative prognostic feature rather than a diagnostic symptom | Pleural/peritoneal | Human clinical/review (lewandowska2024diagnosisandtreatment pages 1-2, tyagi2024germlinebap1mutation pages 11-14) |
| Hyperleukocytosis / elevated white blood cell count | Leukocytosis |  | Negative prognostic factor; one source specifies WBC ≥8.3×10^9/L | Pleural/peritoneal | Human clinical/review (lewandowska2024diagnosisandtreatment pages 1-2, tyagi2024germlinebap1mutation pages 11-14) |
| Elevated C-reactive protein | Increased circulating C-reactive protein concentration |  | Negative prognostic factor in pleural mesothelioma | Pleural | Human clinical/review (lewandowska2024diagnosisandtreatment pages 1-2) |
| Thrombocytosis | Thrombocytosis |  | Negative prognostic factor; one source specifies platelet count >400,000/µL | Pleural/peritoneal | Human clinical/review (tyagi2024germlinebap1mutation pages 11-14, tyagi2024germlinebap1mutation pages 14-17) |
| Elevated lactate dehydrogenase | Increased circulating lactate dehydrogenase concentration |  | Negative prognostic factor; one source specifies LDH >500 IU/L | Pleural/peritoneal | Human clinical/review (tyagi2024germlinebap1mutation pages 11-14, tyagi2024germlinebap1mutation pages 14-17) |
| Low hemoglobin / anemia | Anemia |  | Reported as a poor prognostic feature in one source | Pleural/peritoneal | Human clinical/review (tyagi2024germlinebap1mutation pages 14-17) |


*Table: This table summarizes key clinical symptoms, signs, and laboratory abnormalities reported in the retrieved mesothelioma sources, organized by likely HPO mapping and disease context. It is useful for populating phenotype fields in a disease knowledge base while retaining source-linked evidence.*

### 3.2 Onset, severity, progression
- **Latency/onset:** symptom onset often occurs decades after exposure; latency estimates include **15–40 years** (pleural; Chiec 2024), **~30 years on average** (Lewandowska 2024), and **10–50 years** (Jain 2024). (chiec2024immunotherapyfortreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2, jain2024malignantpleuralmesothelioma pages 1-2)
- **Progression:** typically insidious with frequent late-stage dissemination at diagnosis. (lewandowska2024diagnosisandtreatment pages 1-2)

### 3.3 Quality of life impact
The ASCO guideline update indicates that quality-of-life domains were key outcomes in trials informing recommendations, and that in MARS2 multiple QOL domains favored chemotherapy alone versus surgery + chemo in a randomized comparison. (kindler2025treatmentofpleural pages 3-5)

---

## 4. Genetic / Molecular Information

### 4.1 Key genes and alterations (current consensus)
Mesothelioma genomic landscapes are dominated by **tumor suppressor loss-of-function** rather than recurrent activating oncogenes.
- Commonly altered genes cited in recent reviews include **BAP1, CDKN2A, NF2**. (cedres2023currentstateofthearttherapy pages 1-2, jain2024malignantpleuralmesothelioma pages 1-2, bertin2023thecurrenttreatment pages 1-2)
- OpenTargets disease–target association evidence also links MM/MPM with **WT1, BAP1, CDKN2A, SETD2, TP53, LATS1/2, PDCD1**, among others, reflecting both diagnostic markers and therapeutic target biology. (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma)

### 4.2 Somatic vs germline
- **Germline:** BAP1 is emphasized as a recurrent germline predisposition gene; ASCO highlights germline mutation prevalence as clinically relevant and supports offering germline testing broadly. (kindler2025treatmentofpleural pages 2-3)
- **Somatic:** BAP1, CDKN2A, NF2 recurrently altered in tumor tissue. (cedres2023currentstateofthearttherapy pages 1-2, jain2024malignantpleuralmesothelioma pages 1-2)

### 4.3 Diagnostic molecular pathology markers
- **BAP1 IHC:** loss of nuclear expression is a key marker; one 2024 review notes BAP1 loss by IHC in **~70% of epithelioid** pleural mesotheliomas. (chiec2024immunotherapyfortreatment pages 1-2)
- **CDKN2A (p16) deletion:** FISH for p16/CDKN2A deletion is described as a gold-standard ancillary diagnostic approach; MTAP is discussed as a practical surrogate. (zahiu2025molecularinsightsinto pages 1-2, chiec2024immunotherapyfortreatment pages 1-2)
- **MTAP IHC surrogate:** MTAP loss described as an “almost ideal surrogate” for p16/CDKN2A deletion testing. (zahiu2025molecularinsightsinto pages 1-2)

| Gene/marker | Alteration type (somatic/germline; LOF/deletion etc.) | Clinical use (diagnosis/prognosis/therapy selection) | Assay (IHC/FISH/seq) | Notes | Key citation (author year, PMID if given in context—otherwise leave blank) |
|---|---|---|---|---|---|
| **BAP1** | Frequent loss/inactivation; tumor suppressor alteration; includes **germline** pathogenic variants and **somatic** loss | Diagnosis, hereditary risk assessment, prognosis | IHC; sequencing | Loss of nuclear BAP1 expression is highlighted as a key diagnostic marker; ~70% of epithelioid pleural mesotheliomas show BAP1 loss by IHC; germline BAP1 is associated with younger age and better prognosis in some series; ASCO notes mesothelioma often has germline mutations, most commonly **BAP1**, supporting routine germline testing discussions (chiec2024immunotherapyfortreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2, kindler2025treatmentofpleural pages 2-3) | Chiec 2024; Lewandowska 2024; Kindler 2025 |
| **MTAP** | Loss, often reflecting adjacent **CDKN2A** deletion biology | Diagnosis | IHC | MTAP loss is described as an almost ideal surrogate for gold-standard **p16/CDKN2A FISH** deletion testing; especially useful when tissue is limited (zahiu2025molecularinsightsinto pages 1-2, chiec2024immunotherapyfortreatment pages 1-2) | Zahiu 2025; Chiec 2024 |
| **CDKN2A / p16** | Homozygous deletion; recurrent chromosomal loss at 9p21 | Diagnosis; adverse biology/prognostic context | FISH; MTAP IHC surrogate | >90% of sarcomatoid pleural mesotheliomas reportedly have **CDKN2A homozygous deletion or MTAP loss**; p16/CDKN2A FISH is treated as the gold-standard ancillary diagnostic approach in retrieved sources (chiec2024immunotherapyfortreatment pages 1-2, zahiu2025molecularinsightsinto pages 1-2, tyagi2024germlinebap1mutation pages 14-17) | Chiec 2024; Zahiu 2025 |
| **NF2** | Recurrent tumor suppressor loss/inactivation | Molecular characterization; prognostic/biologic relevance | Sequencing | One of the most frequently altered genes in pleural mesothelioma; part of the recurrent chromosome 22q loss pattern described in reviews (cedres2023currentstateofthearttherapy pages 1-2, jain2024malignantpleuralmesothelioma pages 1-2, tyagi2024germlinebap1mutation pages 14-17, OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Cedres 2023; Jain 2024 |
| **TP53** | Tumor suppressor alteration (subset) | Molecular characterization | Sequencing | Listed among recurrently altered genes/targets in disease-target evidence; less emphasized diagnostically than BAP1/MTAP/CDKN2A in retrieved context (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Open Targets context |
| **SETD2** | Tumor suppressor / epigenetic regulator alteration | Molecular characterization | Sequencing | Included among associated targets in disease-target evidence and recent mesothelioma molecular reviews; supports chromatin dysregulation theme (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Open Targets context |
| **LATS1 / LATS2** | Tumor suppressor loss/inactivation | Molecular characterization | Sequencing | Included in disease-target associations and reflects Hippo pathway disruption noted in mesothelioma molecular landscapes (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Open Targets context |
| **WT1** | Disease-associated marker/target (not framed here as recurrent genomic driver) | Diagnostic immunophenotyping context; disease association | IHC (typical clinical use), not specified in retrieved text | Open Targets lists WT1 among associated targets for malignant mesothelioma; retrieved context does not provide detailed assay-performance claims for this report (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Open Targets context |
| **PD-L1** | Protein expression biomarker | Prognosis; possible therapy-response exploration | IHC | PD-L1 expression occurs in ~20–40% of patients and is associated with poorer prognosis, but predictive value for immunotherapy response remains unconfirmed in retrieved reviews (cedres2023currentstateofthearttherapy pages 1-2) | Cedres 2023 |
| **Tumor mutational burden (TMB)** | Generally low genomic mutation burden | Therapy-selection research biomarker | NGS / sequencing | Pleural mesothelioma is described as having low TMB, often <2 nonsynonymous mutations/Mb in most samples, contributing to biomarker challenges for immunotherapy (chiec2024immunotherapyfortreatment pages 1-2, bertin2023thecurrenttreatment pages 1-2) | Chiec 2024; Bertin 2023 |
| **BAP1 + MTAP panel** | Combined loss-marker strategy | Diagnostic refinement / cost-effectiveness | IHC panel | Recent review emphasizes combined BAP1 and MTAP IHC as a practical, cost-effective adjunct for difficult mesothelioma diagnosis (zahiu2025molecularinsightsinto pages 17-19) | Zahiu 2025 |
| **Broad germline cancer predisposition testing** | Germline pathogenic variants, especially **BAP1** | Hereditary cancer risk assessment; family counseling; prognosis | Germline sequencing / panel testing | ASCO update states mesothelioma patients often harbor germline mutations, most commonly BAP1, and notes universal germline testing should be offered; this is a current implementation-oriented recommendation rather than a single-marker assay claim (kindler2025treatmentofpleural pages 2-3) | Kindler 2025 |


*Table: This table summarizes the key molecular and diagnostic markers for mesothelioma retrieved from the available context, including their alteration types, clinical uses, and typical assays. It is useful for knowledge-base population because it distinguishes diagnostic markers from broader molecular features and hereditary risk genes.*

### 4.4 Tumor immune microenvironment / biomarkers
- The pleural mesothelioma microenvironment is described as relatively immunosuppressive, and PD-L1 expression occurs in **~20–40%** of patients and is associated with worse prognosis, though predictive value for immunotherapy response remains unconfirmed. (cedres2023currentstateofthearttherapy pages 1-2)

### 4.5 Epigenetics and chromatin regulation
- Evidence of epigenetic/chromatin regulator involvement is supported by recurrent alterations in genes such as **SETD2** (OpenTargets association) and the emphasis on tumor suppressor/epigenetic regulator alterations in molecular overviews. (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma)

---

## 5. Environmental Information

### 5.1 Environmental/occupational factors
- Asbestos remains central in contemporary accounts of pleural mesothelioma pathogenesis and continuing incidence. (lewandowska2024diagnosisandtreatment pages 1-2, bertin2023thecurrenttreatment pages 1-2)
- A regional Italian surveillance study (Emilia-Romagna, 1996–2023; n=3513 cases) found **occupational exposure accounted for 82%** of cases overall and increased to 88% in the most recent period; most cases were male (72%) and >65 years (79%). (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma)

### 5.2 Lifestyle factors
No lifestyle protective or causal factors (e.g., smoking, diet) were specifically extracted from the retrieved sources.

### 5.3 Infectious agents
No infectious etiologies were identified in retrieved sources.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
- **Trigger:** Asbestos exposure (inhalational for pleural disease) with prolonged latency. (chiec2024immunotherapyfortreatment pages 1-2, zahiu2025molecularinsightsinto pages 1-2)
- **Intermediate processes:** chronic pleural inflammation and tissue injury, with downstream genomic and cellular dysregulation; Jain (2024) describes free radical generation and disruption of cell division among mechanisms in asbestos-related pleural mesothelioma. (jain2024malignantpleuralmesothelioma pages 1-2)
- **Genomic state:** predominance of tumor suppressor losses (BAP1, CDKN2A, NF2), low tumor mutational burden; these features contribute to therapeutic resistance and challenges for biomarker development. (chiec2024immunotherapyfortreatment pages 1-2, bertin2023thecurrenttreatment pages 1-2)

### 6.2 Immune involvement
- Immunosuppressive tumor microenvironment described in recent treatment-focused reviews (regulatory immune populations; macrophage/MDSC emphasis in Cedres 2023), potentially contributing to variable immunotherapy response. (cedres2023currentstateofthearttherapy pages 1-2)

### 6.3 Suggested ontology terms (mechanisms)
*GO biological process (suggested; IDs not provided in retrieved text):*
- inflammatory response; response to oxidative stress; apoptotic process; DNA damage response; chromatin organization

*CL cell types (suggested; IDs not provided in retrieved text):*
- mesothelial cell; tumor-associated macrophage; CD8-positive T cell; regulatory T cell

---

## 7. Anatomical Structures Affected

### 7.1 Primary anatomic sites
- **Pleura** (dominant site; 80–85%) (zahiu2025molecularinsightsinto pages 1-2)
- **Peritoneum** (less common but major clinical subtype) (ettinger2023mesotheliomaperitonealversion pages 1-2)

### 7.2 Suggested anatomy ontology mapping
*UBERON terms are suggested conceptually but IDs were not present in retrieved sources.*
- pleura; peritoneum

---

## 8. Temporal Development

### 8.1 Onset pattern
- Typically adult-onset with a long latency from asbestos exposure. (chiec2024immunotherapyfortreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2)

### 8.2 Progression and staging
- Many patients present with advanced/disseminated disease at diagnosis, limiting surgical options. (lewandowska2024diagnosisandtreatment pages 1-2)
- Standard staging uses TNM for pleural disease; Lewandowska (2024) reproduces TNM categories and indicates surgery is considered mainly for stages I–IIIa. (lewandowska2024diagnosisandtreatment pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent statistics)
- US annual cases reported as **~3,500/year** in NCCN overview. (ettinger2023mesotheliomaperitonealversion pages 1-2)
- Another review cites **~2,500–3,200** new U.S. cases annually and **~38,400 worldwide**. (zahiu2025molecularinsightsinto pages 1-2)

### 9.2 Demographics
- Male predominance (~70% male reported in one review). (zahiu2025molecularinsightsinto pages 1-2)

### 9.3 Geographic disparities and real-world data (SEER example)
A SEER analysis (2004–2021; 8519 cases) reported a decline in metropolitan incidence (1.4 to 0.8) and later decline in nonmetropolitan incidence (to 0.5 by 2021), with marked survival disparities: by 2020, **1-year cancer-specific survival 50.3% (metropolitan) vs 27.7% (nonmetropolitan)** and **HR 1.18** for nonmetropolitan hazard of death. (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma)

| Metric | Value | Population/region | Year(s) | Source | Notes |
|---|---:|---|---|---|---|
| New cases per year | ~2,500–3,200 | United States | Not specified in excerpt | Zahiu et al., 2025 (zahiu2025molecularinsightsinto pages 1-2) | Review cites annual U.S. case burden for malignant mesothelioma/pleural mesothelioma. |
| New cases per year | ~3,500 | United States | Not specified in excerpt | NCCN Peritoneal Mesothelioma Guidelines, 2023 (ettinger2023mesotheliomaperitonealversion pages 1-2) | NCCN overview states mesothelioma is estimated to occur in approximately 3,500 people in the U.S. every year; includes pleural, peritoneal, and other sites. |
| New cases | ~38,400 | Worldwide | Not specified in excerpt | Zahiu et al., 2025 (zahiu2025molecularinsightsinto pages 1-2) | Global annual burden cited in review. |
| Sex distribution | ~70% male | Mesothelioma overall | Not specified in excerpt | Zahiu et al., 2025 (zahiu2025molecularinsightsinto pages 1-2) | Other sources in context also note male predominance. |
| Cases by primary site | Pleura 80–85% | Mesothelioma overall | Not specified in excerpt | Zahiu et al., 2025 (zahiu2025molecularinsightsinto pages 1-2) | Pleura is the dominant site; peritoneum and other serosal sites are less common. |
| Latency from asbestos exposure to disease | 15–40 years | Pleural mesothelioma | Not specified in excerpt | Chiec & Bruno, 2024 (chiec2024immunotherapyfortreatment pages 1-2) | Same context describes disease as primarily caused by inhalational asbestos exposure. |
| Latency from asbestos exposure to symptoms | 10–50 years | Malignant pleural mesothelioma | Not specified in excerpt | Jain et al., 2024 (jain2024malignantpleuralmesothelioma pages 1-2) | Broad latency range in review; consistent with long natural history. |
| Average latency | ~30 years | Pleural mesothelioma | Not specified in excerpt | Lewandowska & Kowalski, 2024 (lewandowska2024diagnosisandtreatment pages 1-2) | Average latency reported in state-of-the-art review. |
| 5-year overall survival | ~12% | Pleural mesothelioma | Not specified in excerpt | Chiec & Bruno, 2024 (chiec2024immunotherapyfortreatment pages 1-2); Bertin et al., 2023 (bertin2023thecurrenttreatment pages 1-2) | Chiec review abstract cites 5-year OS of 12%; Bertin review states 5-year survival of only 12%. |
| 5-year overall survival | ~10% | Malignant pleural mesothelioma | Not specified in excerpt | Jain et al., 2024 (jain2024malignantpleuralmesothelioma pages 1-2) | Slightly lower estimate from another review; likely reflects cohort/case-mix differences. |
| Untreated median survival | 4–8 months | Malignant pleural mesothelioma | Not specified in excerpt | Cedres et al., 2023 (cedres2023currentstateofthearttherapy pages 1-2) | Review describes untreated patients as having very poor prognosis. |
| Untreated median survival | 7–10 months | Pleural mesothelioma / malignant mesothelioma | Not specified in excerpt | Zahiu et al., 2025 (zahiu2025molecularinsightsinto pages 1-2) | Another review provides a somewhat higher untreated median survival estimate. |
| Overall survival range | 9–18 months | Malignant pleural mesothelioma | Not specified in excerpt | Cedres et al., 2023 (cedres2023currentstateofthearttherapy pages 1-2) | Review-level estimate across treated populations/settings. |
| Life expectancy without radical treatment | 9 months | Pleural mesothelioma | Not specified in excerpt | Lewandowska & Kowalski, 2024 (lewandowska2024diagnosisandtreatment pages 1-2) | Context states life expectancy for patients not treated with radical intent. |
| Survival by histology after resection | ~19 months epithelioid vs ~4 months sarcomatoid | Pleural mesothelioma | Not specified in excerpt | Chiec & Bruno, 2024 (chiec2024immunotherapyfortreatment pages 1-2) | Strong prognostic effect of histologic subtype. |
| Median survival by histology | ~17 months epithelioid vs <7 months sarcomatoid | Pleural mesothelioma | Not specified in excerpt | Lewandowska & Kowalski, 2024 (lewandowska2024diagnosisandtreatment pages 1-2) | Histology-associated prognosis in review article. |
| Metropolitan incidence rate | 1.4 to 0.8 per 100,000 | U.S. metropolitan areas | 2004 to 2021 | Didier et al., 2025 (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | SEER-based pleural mesothelioma incidence declined over study period. |
| Nonmetropolitan incidence rate | Stable until 2017, then declined to 0.5 per 100,000 | U.S. nonmetropolitan areas | 2004 to 2021 | Didier et al., 2025 (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Indicates later decline outside metropolitan areas. |
| 1-year cancer-specific survival | 50.3% | U.S. metropolitan areas | By 2020 | Didier et al., 2025 (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Pleural mesothelioma; better outcomes than nonmetropolitan areas. |
| 1-year cancer-specific survival | 27.7% | U.S. nonmetropolitan areas | By 2020 | Didier et al., 2025 (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Marked disparity versus metropolitan populations. |
| Relative hazard of death | HR 1.18 | U.S. nonmetropolitan vs metropolitan | 2004 to 2021 cohort | Didier et al., 2025 (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Multivariable analysis showed higher hazard of death in nonmetropolitan areas. |
| Regional registry cases | 3,513 total cases; 72% male; 79% age >65 years | Emilia-Romagna, Italy | 1996–2023 | Giacomino et al., 2024 (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma) | Occupational exposure accounted for 82% overall and increased from 71% to 88% over periods studied. |


*Table: This table compiles key epidemiology and prognosis statistics for malignant mesothelioma from the retrieved context, including incidence, survival, latency, sex/site distribution, and geographic disparities. It is useful as a concise evidence summary for knowledge base population and comparative review.*

### 9.4 Inheritance
- Germline susceptibility is clinically relevant, especially **BAP1**, motivating guideline support for germline testing. (kindler2025treatmentofpleural pages 2-3, lewandowska2024diagnosisandtreatment pages 1-2)

---

## 10. Diagnostics

### 10.1 Imaging and tissue diagnosis (current practice)
- Jain (2024) describes diagnostic work-up including contrast-enhanced thoracic CT, thoracoscopic pleural biopsy, thoracentesis with cytology, MRI for diaphragmatic invasion assessment, and PET for metastasis evaluation. (jain2024malignantpleuralmesothelioma pages 1-2)
- Chiec (2024) emphasizes the difficulty of diagnosis from pleural fluid/small biopsies and supports VATS surgical biopsy and invasive staging approaches (e.g., EBUS) when appropriate. (chiec2024immunotherapyfortreatment pages 1-2)

### 10.2 Biomarkers and molecular pathology
- **BAP1 IHC** and **MTAP IHC** (surrogate for **CDKN2A/p16 FISH**) are highlighted as high-value diagnostic adjuncts. (zahiu2025molecularinsightsinto pages 1-2, chiec2024immunotherapyfortreatment pages 1-2)

### 10.3 Germline testing
- ASCO guideline update explicitly frames germline mutation prevalence (often BAP1) as rationale that **universal germline testing should be offered** to patients with mesothelioma. (kindler2025treatmentofpleural pages 2-3)

---

## 11. Outcome / Prognosis

### 11.1 Survival (recently reported values)
- Untreated median survival: **4–8 months** (Cedres 2023) and **7–10 months** (Zahiu 2025 review excerpt). (cedres2023currentstateofthearttherapy pages 1-2, zahiu2025molecularinsightsinto pages 1-2)
- Population 5-year OS frequently cited around **~12%** (Bertin 2023; Chiec 2024 abstract). (bertin2023thecurrenttreatment pages 1-2, chiec2024immunotherapyfortreatment pages 1-2)
- Histology strongly influences outcomes (e.g., epithelioid better than sarcomatoid). (chiec2024immunotherapyfortreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2)

### 11.2 Prognostic factors
Recent review-level prognostic factors include older age, stage, poor performance status, and inflammatory markers (e.g., CRP, leukocytosis). (lewandowska2024diagnosisandtreatment pages 1-2)

---

## 12. Treatment

### 12.1 Standard systemic therapy (real-world implementation)
- **Chemotherapy backbone:** platinum + pemetrexed remains a longstanding standard systemic therapy. (cedres2023currentstateofthearttherapy pages 1-2, chiec2024immunotherapyfortreatment pages 1-2, bertin2023thecurrenttreatment pages 1-2)
- **Bevacizumab addition:** Cedres (2023) reports adding bevacizumab to platinum–pemetrexed adds **~2 months** to median survival. (cedres2023currentstateofthearttherapy pages 1-2)

### 12.2 Immunotherapy (major recent development; 2023–2024 emphasis)
- Cedres (2023) reports first-line nivolumab + ipilimumab improved OS versus chemotherapy in CheckMate-743 with **median OS 18.1 months**, leading to FDA and EMA approval and a new standard-of-care position. (cedres2023currentstateofthearttherapy pages 1-2)

### 12.3 Surgery and multimodality therapy
- Lewandowska (2024) describes tri-modal therapy (surgery + chemotherapy + radiotherapy) as a standard for radical management, but notes stage at diagnosis commonly precludes surgery. (lewandowska2024diagnosisandtreatment pages 1-2)
- ASCO (2025 update) includes randomized evidence (MARS2) showing aggressive surgery (EPD + adjuvant chemo) did not improve outcomes versus chemotherapy alone, with higher early mortality (30-day 4%, 90-day 9%). (kindler2025treatmentofpleural pages 3-5)

### 12.4 Guideline algorithms (visual evidence)
The ASCO 2025 update provides structured algorithms for surgical selection and first-line systemic therapy selection (immunotherapy vs chemotherapy based on histology). (kindler2025treatmentofpleural media fd734332, kindler2025treatmentofpleural media c1e908f8, kindler2025treatmentofpleural media 9d842ba2, kindler2025treatmentofpleural media 39f509f9, kindler2025treatmentofpleural media 0889009a)

### 12.5 Clinical trials (selected; NCT IDs)
- **NCT02899299 (CheckMate 743):** Phase 3 randomized open-label trial; nivolumab + ipilimumab vs pemetrexed + cisplatin/carboplatin in unresectable pleural malignant mesothelioma; primary endpoint OS; enrollment 605; includes PD-L1 stratified analyses. (NCT02899299 chunk 1)
- **NCT03918252:** Neoadjuvant nivolumab ± ipilimumab for 3 cycles followed by surgery and adjuvant nivolumab for 12 months (phase I/II; active not recruiting per excerpt). (cecchi2025perioperativetreatmentsin pages 9-10)
- Additional identified trials from clinicaltrials.gov search results (metadata only in this run; full protocol/outcomes not extracted here): **NCT04334759** (durvalumab + chemotherapy; phase 3), **NCT06097728** (MEDI5752 + carboplatin/pemetrexed; phase 3), **NCT04287829** (pembrolizumab + lenvatinib; phase 2). (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma)

### 12.6 Suggested MAXO terms (treatments)
MAXO IDs were not present in retrieved sources; suggested concepts:
- immune checkpoint inhibitor therapy; combination immunotherapy; platinum-based chemotherapy; surgical cytoreduction; radiotherapy; genetic counseling / germline testing

| Setting (1L unresectable, perioperative, peritoneal etc.) | Modality/regimen | Key evidence/trial or guideline | Reported outcome metrics in context (median OS etc.) | Regulatory/real-world implementation notes | Suggested MAXO term |
|---|---|---|---|---|---|
| 1L unresectable pleural mesothelioma | Nivolumab + ipilimumab | CheckMate-743; summarized in 2023/2024 reviews and ASCO guideline update (cedres2023currentstateofthearttherapy pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2, kindler2025treatmentofpleural media fd734332) | Median OS 18.1 months; superior to chemotherapy in CheckMate-743 (cedres2023currentstateofthearttherapy pages 1-2) | Described as FDA/EMA approved and a new standard of care; implemented in routine practice/guidelines, including availability in Poland irrespective of histology (cedres2023currentstateofthearttherapy pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2, kindler2025treatmentofpleural media fd734332) |  |
| 1L unresectable pleural mesothelioma | Platinum + pemetrexed | Historical standard systemic therapy in reviews/guidelines (cedres2023currentstateofthearttherapy pages 1-2, chiec2024immunotherapyfortreatment pages 1-2, bertin2023thecurrenttreatment pages 1-2, kindler2025treatmentofpleural media fd734332) | Extends survival only by months; comparator arm to immunotherapy in modern algorithms (bertin2023thecurrenttreatment pages 1-2, kindler2025treatmentofpleural media fd734332) | Remains standard chemotherapy backbone in guidelines and clinical practice (cedres2023currentstateofthearttherapy pages 1-2, kindler2025treatmentofpleural media fd734332) |  |
| 1L unresectable pleural mesothelioma | Platinum + pemetrexed + bevacizumab | Review summary of established regimen (cedres2023currentstateofthearttherapy pages 1-2) | Addition of bevacizumab adds about 2 months to median survival (cedres2023currentstateofthearttherapy pages 1-2) | Used as an intensified chemotherapy-based option where appropriate; discussed as pre-immunotherapy standard intensification (cedres2023currentstateofthearttherapy pages 1-2) |  |
| 1L pleural mesothelioma, histology-directed decision making | Systemic therapy algorithm: immunotherapy versus chemotherapy based on histology | ASCO 2025 Figure 5 / Tables 4-5 (kindler2025treatmentofpleural media fd734332) | Figure summarizes selection of ipilimumab+nivolumab versus pemetrexed+platinum based on epithelioid vs nonepithelioid histology; no additional numeric outcome quoted in image summary (kindler2025treatmentofpleural media fd734332) | ASCO algorithm indicates first-line implementation in routine practice; nivolumab+ipilimumab especially emphasized for nonepithelioid disease (kindler2025treatmentofpleural media fd734332) |  |
| Radical/localized pleural mesothelioma | Tri-modal therapy (surgery + chemotherapy + radiotherapy) | 2024 state-of-the-art review (lewandowska2024diagnosisandtreatment pages 1-2) | Presented as standard for radical management; no pooled OS number in retrieved excerpt (lewandowska2024diagnosisandtreatment pages 1-2) | Stage at diagnosis usually precludes surgery in many patients (lewandowska2024diagnosisandtreatment pages 1-2) |  |
| Resectable stage I-IIIa pleural mesothelioma | Surgery: EPP or PD/EPD | 2024 review; ASCO surgical algorithm (lewandowska2024diagnosisandtreatment pages 1-2, kindler2025treatmentofpleural media fd734332) | No single survival number for surgery alone in these excerpts; surgery is for selected patients with early-stage disease (lewandowska2024diagnosisandtreatment pages 1-2, kindler2025treatmentofpleural media fd734332) | EPD/PD currently favored as lung-sparing approaches in guideline algorithms (kindler2025treatmentofpleural media fd734332) |  |
| Pleural mesothelioma surgery comparison | Extended pleurectomy/decortication (EPD) + adjuvant chemotherapy versus chemotherapy alone | MARS2, summarized in ASCO update (kindler2025treatmentofpleural pages 3-5) | Median OS 19.3 months with surgery arm versus 24.8 months with chemotherapy alone; HR for death 1.28; 30-day mortality 4%, 90-day mortality 9% (kindler2025treatmentofpleural pages 3-5) | Supports caution with aggressive surgery; guideline context favors careful patient selection and lung-sparing approaches (kindler2025treatmentofpleural pages 3-5, kindler2025treatmentofpleural media fd734332) |  |
| Advanced/recurrent pleural mesothelioma | Immune checkpoint inhibitors (class effect) | 2024 immunotherapy review / emerging strategies (chiec2024immunotherapyfortreatment pages 1-2) | Review notes recent dual-checkpoint and chemo-immunotherapy trials changed outcomes, but no specific salvage OS quoted in retrieved excerpt (chiec2024immunotherapyfortreatment pages 1-2) | Incorporated into modern pleural mesothelioma treatment landscape; biomarker-guided selection remains unresolved (chiec2024immunotherapyfortreatment pages 1-2) |  |
| Previously treated pleural mesothelioma | No approved systemic option after 1L (as of 2023 review context) | 2023 review (cedres2023currentstateofthearttherapy pages 1-2) | Explicitly notes no approved systemic options after first-line treatment in that review excerpt (cedres2023currentstateofthearttherapy pages 1-2) | Reflects therapeutic gap and rationale for ongoing trials (cedres2023currentstateofthearttherapy pages 1-2) |  |
| Peritoneal mesothelioma | NCCN-guided workup/diagnosis/treatment pathways | NCCN Peritoneal Mesothelioma v2.2023 (ettinger2023mesotheliomaperitonealversion pages 1-2) | No regimen-specific OS in retrieved excerpt (ettinger2023mesotheliomaperitonealversion pages 1-2) | NCCN notes rarity and encourages clinical trial participation; “malignant” terminology dropped because all mesotheliomas are now defined as malignant (ettinger2023mesotheliomaperitonealversion pages 1-2) |  |


*Table: This table summarizes current mesothelioma treatment approaches and outcome data available in the retrieved context, emphasizing first-line systemic therapy, surgery, and guideline implementation. It is useful for quickly comparing standard regimens, landmark evidence, and practice implications.*

---

## 13. Prevention

- Primary prevention is centered on eliminating asbestos exposure; ongoing incidence is consistent with long latency and historical exposure. (lewandowska2024diagnosisandtreatment pages 1-2, zahiu2025molecularinsightsinto pages 1-2)
- No specific screening program guidance for asymptomatic individuals was extracted from the retrieved excerpts.

---

## 14. Other Species / Natural Disease

No other-species naturally occurring disease data were present in the retrieved sources.

---

## 15. Model Organisms

No model organism systems were detailed in the retrieved excerpts.

---

## Recent developments (2023–2024) and expert analysis (authoritative synthesis)

1. **First-line immunotherapy became practice-defining.** A 2023 state-of-the-art review summarizes CheckMate-743, highlighting nivolumab + ipilimumab median OS **18.1 months** and regulatory approval, marking a new standard; subsequent 2024 reviews emphasize broad clinical implementation and ongoing biomarker uncertainty. (cedres2023currentstateofthearttherapy pages 1-2, chiec2024immunotherapyfortreatment pages 1-2, lewandowska2024diagnosisandtreatment pages 1-2)
2. **Diagnostic adjuncts are converging on practical IHC strategies.** 2024–2025 reviews highlight BAP1 and MTAP IHC, with MTAP as an “almost ideal surrogate” for CDKN2A deletion testing via p16/CDKN2A FISH, potentially improving diagnostic efficiency where tissue is limited. (zahiu2025molecularinsightsinto pages 1-2, chiec2024immunotherapyfortreatment pages 1-2)
3. **Surgery is being re-evaluated with randomized evidence.** ASCO’s guideline update incorporates MARS2 results showing no OS advantage for EPD + chemo vs chemo alone and QOL/cost favoring chemo, supporting more conservative, carefully selected multimodality surgery in specialized centers. (kindler2025treatmentofpleural pages 3-5, kindler2025treatmentofpleural media fd734332)
4. **Hereditary genetics is increasingly guideline-relevant.** ASCO emphasizes germline mutations (especially BAP1) in mesothelioma, supporting offering germline testing broadly to guide patient/family risk management. (kindler2025treatmentofpleural pages 2-3)

---

## Required direct quotes from abstracts (supporting key statements)

- Cedres et al. 2023 (Cancers; Dec 2023): “*Malignant pleural mesothelioma (MPM) is a locally aggressive disease related to asbestos exposure with a median survival for untreated patients of 4–8 months… Recently, in first-line treatment, immunotherapy combining nivolumab with ipilimumab has been shown to be superior to chemotherapy in the CheckMate-743 study in terms of overall survival (18.1 months)* …” https://doi.org/10.3390/cancers15245787 (cedres2023currentstateofthearttherapy pages 1-2)
- NCCN Peritoneal Mesothelioma v2.2023 (Sep 2023): “*Mesothelioma is a rare cancer originating in mesothelial surfaces of the peritoneum, pleura, and other sites.*” and “*The term ‘malignant’ is no longer used to classify mesotheliomas, because all mesotheliomas are now defined as malignant.*” https://doi.org/10.6004/jnccn.2023.0045 (ettinger2023mesotheliomaperitonealversion pages 1-2)
- Chiec & Bruno 2024 (IJMS; Oct 2024): “*Pleural mesothelioma is a rare malignancy associated with asbestos exposure and very poor prognosis, with a 5-year overall survival of 12%.*” https://doi.org/10.3390/ijms251910861 (chiec2024immunotherapyfortreatment pages 1-2)

---

## Notes on evidence limitations and gaps
- **Ontology codes (MONDO, MeSH, ICD-10/ICD-11, Orphanet, OMIM)** were not present in the retrieved full-text excerpts; these should be filled by directly querying those coding/ontology resources rather than inferred. (zahiu2025molecularinsightsinto pages 1-2, ettinger2023mesotheliomaperitonealversion pages 1-2)
- Several clinical trials were identified by NCT number, but detailed protocol fields/outcome fields were only retrieved in this run for NCT02899299 and NCT03918252. (NCT02899299 chunk 1, cecchi2025perioperativetreatmentsin pages 9-10)



References

1. (zahiu2025molecularinsightsinto pages 1-2): Teodora Zahiu, Carmen Mihaela Mihu, Bianca A. Bosca, Mariana Mărginean, Lavinia Patricia Mocan, Roxana-Adelina Ștefan, Rada Teodora Suflețel, Carina Mihu, and Carmen Stanca Melincovici. Molecular insights into pleural mesothelioma: unveiling pathogenic mechanisms and therapeutic opportunities. Diagnostics, 15:1323, May 2025. URL: https://doi.org/10.3390/diagnostics15111323, doi:10.3390/diagnostics15111323. This article has 4 citations.

2. (ettinger2023mesotheliomaperitonealversion pages 1-2): David S. Ettinger, Douglas E. Wood, James Stevenson, Dara L. Aisner, Wallace Akerley, Jessica R. Bauman, Ankit Bharat, Debora S. Bruno, Joe Y. Chang, Lucian R. Chirieac, Malcolm DeCamp, Thomas J. Dilling, Jonathan Dowell, Gregory A. Durm, Scott Gettinger, Travis E. Grotz, Matthew A. Gubens, Aparna Hegde, Rudy P. Lackner, Michael Lanuti, Jules Lin, Billy W. Loo, Christine M. Lovly, Fabien Maldonado, Erminia Massarelli, Daniel Morgensztern, Trey C. Mullikin, Thomas Ng, Gregory A. Otterson, Sandip P. Patel, Tejas Patil, Patricio M. Polanco, Gregory J. Riely, Jonathan Riess, Theresa A. Shapiro, Aditi P. Singh, Alda Tam, Tawee Tanvetyanon, Jane Yanagawa, Stephen C. Yang, Edwin Yau, Kristina M. Gregory, and Miranda Hughes. Mesothelioma: peritoneal, version 2.2023, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 21 9:961-979, Sep 2023. URL: https://doi.org/10.6004/jnccn.2023.0045, doi:10.6004/jnccn.2023.0045. This article has 35 citations.

3. (cedres2023currentstateofthearttherapy pages 1-2): Susana Cedres, Augusto Valdivia, Patricia Iranzo, Ana Callejo, Nuria Pardo, Alejandro Navarro, Alex Martinez-Marti, Juan David Assaf-Pastrana, Enriqueta Felip, and Pilar Garrido. Current state-of-the-art therapy for malignant pleural mesothelioma and future options centered on immunotherapy. Cancers, 15:5787, Dec 2023. URL: https://doi.org/10.3390/cancers15245787, doi:10.3390/cancers15245787. This article has 11 citations.

4. (chiec2024immunotherapyfortreatment pages 1-2): Lauren Chiec and Debora S. Bruno. Immunotherapy for treatment of pleural mesothelioma: current and emerging therapeutic strategies. International Journal of Molecular Sciences, 25:10861, Oct 2024. URL: https://doi.org/10.3390/ijms251910861, doi:10.3390/ijms251910861. This article has 8 citations.

5. (jain2024malignantpleuralmesothelioma pages 1-2): Molly Jain, Morgan Kay Crites, Patricia Rich, and Bharat Bajantri. Malignant pleural mesothelioma: a comprehensive review. Journal of Clinical Medicine, 13:5837, Sep 2024. URL: https://doi.org/10.3390/jcm13195837, doi:10.3390/jcm13195837. This article has 30 citations.

6. (lewandowska2024diagnosisandtreatment pages 1-2): Zofia Lewandowska and Dariusz M. Kowalski. Diagnosis and treatment of pleural mesothelioma. state of the art 2024. Oncology in Clinical Practice, Oct 2024. URL: https://doi.org/10.5603/ocp.100725, doi:10.5603/ocp.100725. This article has 1 citations.

7. (kindler2025treatmentofpleural pages 2-3): MD Hedy L. Kindler, M. M. No ﬁ sat Ismaila, MD Lyudmila Bazhenova, MD Quincy Chu, MD Jane E. Churpek, MD Ibiayi Dagogo-Jack, MD Darren S. Bryan, MD PhD Michael W. Drazer, MD Patrick Forde, MD Aliya N. Husain, MD Jennifer L. Sauter, MD Valerie Rusch, MB BCh Penelope A. Bradbury, MD PhD B.C. John Cho, MD MSc Marc de Perrot, MD Azam Ghafoor, MD David L. Graham, MD PhD Ola Khorshid, MS Cgc Alexandra Lebensohn, Bsn RN Ocn Julie White, and MD Raf ﬁ t Hassan. Treatment of pleural mesothelioma: asco guideline update. Journal of Clinical Oncology, 43:1006-1038, Jan 2025. URL: https://doi.org/10.1200/jco-24-02425, doi:10.1200/jco-24-02425. This article has 58 citations and is from a highest quality peer-reviewed journal.

8. (bertin2023thecurrenttreatment pages 1-2): Beatriz Bertin, Miguel Zugman, and Gustavo Schvartsman. The current treatment landscape of malignant pleural mesothelioma and future directions. Cancers, 15:5808, Dec 2023. URL: https://doi.org/10.3390/cancers15245808, doi:10.3390/cancers15245808. This article has 18 citations.

9. (OpenTargets Search: malignant mesothelioma,malignant pleural mesothelioma): Open Targets Query (malignant mesothelioma,malignant pleural mesothelioma, 39 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (tyagi2024germlinebap1mutation pages 14-17): G Tyagi. Germline bap1 mutation alter the tumor immune microenvironment and impact the progression of malignant mesothelioma (mm). Unknown journal, 2024.

11. (tyagi2024germlinebap1mutation pages 11-14): G Tyagi. Germline bap1 mutation alter the tumor immune microenvironment and impact the progression of malignant mesothelioma (mm). Unknown journal, 2024.

12. (kindler2025treatmentofpleural pages 3-5): MD Hedy L. Kindler, M. M. No ﬁ sat Ismaila, MD Lyudmila Bazhenova, MD Quincy Chu, MD Jane E. Churpek, MD Ibiayi Dagogo-Jack, MD Darren S. Bryan, MD PhD Michael W. Drazer, MD Patrick Forde, MD Aliya N. Husain, MD Jennifer L. Sauter, MD Valerie Rusch, MB BCh Penelope A. Bradbury, MD PhD B.C. John Cho, MD MSc Marc de Perrot, MD Azam Ghafoor, MD David L. Graham, MD PhD Ola Khorshid, MS Cgc Alexandra Lebensohn, Bsn RN Ocn Julie White, and MD Raf ﬁ t Hassan. Treatment of pleural mesothelioma: asco guideline update. Journal of Clinical Oncology, 43:1006-1038, Jan 2025. URL: https://doi.org/10.1200/jco-24-02425, doi:10.1200/jco-24-02425. This article has 58 citations and is from a highest quality peer-reviewed journal.

13. (zahiu2025molecularinsightsinto pages 17-19): Teodora Zahiu, Carmen Mihaela Mihu, Bianca A. Bosca, Mariana Mărginean, Lavinia Patricia Mocan, Roxana-Adelina Ștefan, Rada Teodora Suflețel, Carina Mihu, and Carmen Stanca Melincovici. Molecular insights into pleural mesothelioma: unveiling pathogenic mechanisms and therapeutic opportunities. Diagnostics, 15:1323, May 2025. URL: https://doi.org/10.3390/diagnostics15111323, doi:10.3390/diagnostics15111323. This article has 4 citations.

14. (kindler2025treatmentofpleural media fd734332): MD Hedy L. Kindler, M. M. No ﬁ sat Ismaila, MD Lyudmila Bazhenova, MD Quincy Chu, MD Jane E. Churpek, MD Ibiayi Dagogo-Jack, MD Darren S. Bryan, MD PhD Michael W. Drazer, MD Patrick Forde, MD Aliya N. Husain, MD Jennifer L. Sauter, MD Valerie Rusch, MB BCh Penelope A. Bradbury, MD PhD B.C. John Cho, MD MSc Marc de Perrot, MD Azam Ghafoor, MD David L. Graham, MD PhD Ola Khorshid, MS Cgc Alexandra Lebensohn, Bsn RN Ocn Julie White, and MD Raf ﬁ t Hassan. Treatment of pleural mesothelioma: asco guideline update. Journal of Clinical Oncology, 43:1006-1038, Jan 2025. URL: https://doi.org/10.1200/jco-24-02425, doi:10.1200/jco-24-02425. This article has 58 citations and is from a highest quality peer-reviewed journal.

15. (kindler2025treatmentofpleural media c1e908f8): MD Hedy L. Kindler, M. M. No ﬁ sat Ismaila, MD Lyudmila Bazhenova, MD Quincy Chu, MD Jane E. Churpek, MD Ibiayi Dagogo-Jack, MD Darren S. Bryan, MD PhD Michael W. Drazer, MD Patrick Forde, MD Aliya N. Husain, MD Jennifer L. Sauter, MD Valerie Rusch, MB BCh Penelope A. Bradbury, MD PhD B.C. John Cho, MD MSc Marc de Perrot, MD Azam Ghafoor, MD David L. Graham, MD PhD Ola Khorshid, MS Cgc Alexandra Lebensohn, Bsn RN Ocn Julie White, and MD Raf ﬁ t Hassan. Treatment of pleural mesothelioma: asco guideline update. Journal of Clinical Oncology, 43:1006-1038, Jan 2025. URL: https://doi.org/10.1200/jco-24-02425, doi:10.1200/jco-24-02425. This article has 58 citations and is from a highest quality peer-reviewed journal.

16. (kindler2025treatmentofpleural media 9d842ba2): MD Hedy L. Kindler, M. M. No ﬁ sat Ismaila, MD Lyudmila Bazhenova, MD Quincy Chu, MD Jane E. Churpek, MD Ibiayi Dagogo-Jack, MD Darren S. Bryan, MD PhD Michael W. Drazer, MD Patrick Forde, MD Aliya N. Husain, MD Jennifer L. Sauter, MD Valerie Rusch, MB BCh Penelope A. Bradbury, MD PhD B.C. John Cho, MD MSc Marc de Perrot, MD Azam Ghafoor, MD David L. Graham, MD PhD Ola Khorshid, MS Cgc Alexandra Lebensohn, Bsn RN Ocn Julie White, and MD Raf ﬁ t Hassan. Treatment of pleural mesothelioma: asco guideline update. Journal of Clinical Oncology, 43:1006-1038, Jan 2025. URL: https://doi.org/10.1200/jco-24-02425, doi:10.1200/jco-24-02425. This article has 58 citations and is from a highest quality peer-reviewed journal.

17. (kindler2025treatmentofpleural media 39f509f9): MD Hedy L. Kindler, M. M. No ﬁ sat Ismaila, MD Lyudmila Bazhenova, MD Quincy Chu, MD Jane E. Churpek, MD Ibiayi Dagogo-Jack, MD Darren S. Bryan, MD PhD Michael W. Drazer, MD Patrick Forde, MD Aliya N. Husain, MD Jennifer L. Sauter, MD Valerie Rusch, MB BCh Penelope A. Bradbury, MD PhD B.C. John Cho, MD MSc Marc de Perrot, MD Azam Ghafoor, MD David L. Graham, MD PhD Ola Khorshid, MS Cgc Alexandra Lebensohn, Bsn RN Ocn Julie White, and MD Raf ﬁ t Hassan. Treatment of pleural mesothelioma: asco guideline update. Journal of Clinical Oncology, 43:1006-1038, Jan 2025. URL: https://doi.org/10.1200/jco-24-02425, doi:10.1200/jco-24-02425. This article has 58 citations and is from a highest quality peer-reviewed journal.

18. (kindler2025treatmentofpleural media 0889009a): MD Hedy L. Kindler, M. M. No ﬁ sat Ismaila, MD Lyudmila Bazhenova, MD Quincy Chu, MD Jane E. Churpek, MD Ibiayi Dagogo-Jack, MD Darren S. Bryan, MD PhD Michael W. Drazer, MD Patrick Forde, MD Aliya N. Husain, MD Jennifer L. Sauter, MD Valerie Rusch, MB BCh Penelope A. Bradbury, MD PhD B.C. John Cho, MD MSc Marc de Perrot, MD Azam Ghafoor, MD David L. Graham, MD PhD Ola Khorshid, MS Cgc Alexandra Lebensohn, Bsn RN Ocn Julie White, and MD Raf ﬁ t Hassan. Treatment of pleural mesothelioma: asco guideline update. Journal of Clinical Oncology, 43:1006-1038, Jan 2025. URL: https://doi.org/10.1200/jco-24-02425, doi:10.1200/jco-24-02425. This article has 58 citations and is from a highest quality peer-reviewed journal.

19. (NCT02899299 chunk 1):  Study of Nivolumab Combined With Ipilimumab Versus Pemetrexed and Cisplatin or Carboplatin as First Line Therapy in Unresectable Pleural Mesothelioma Patients. Bristol-Myers Squibb. 2016. ClinicalTrials.gov Identifier: NCT02899299

20. (cecchi2025perioperativetreatmentsin pages 9-10): Luigi Giovanni Cecchi, Marta Aliprandi, Fabio De Vincenzo, Matteo Perrino, Nadia Cordua, Federica Borea, Alessandro Bertocchi, Antonio Federico, Giuseppe Marulli, Armando Santoro, Giovanni Luca Ceresoli, and Paolo Andrea Zucali. Perioperative treatments in pleural mesothelioma: state of the art and future directions. Cancers, 17:3199, Sep 2025. URL: https://doi.org/10.3390/cancers17193199, doi:10.3390/cancers17193199. This article has 4 citations.

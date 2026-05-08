---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:50:55.182494'
end_time: '2026-05-08T13:06:09.273924'
duration_seconds: 914.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chronic Lymphocytic Leukemia
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chronic Lymphocytic Leukemia
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Chronic Lymphocytic Leukemia** covering all of the
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
- **Disease Name:** Chronic Lymphocytic Leukemia
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Chronic Lymphocytic Leukemia** covering all of the
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


# Chronic Lymphocytic Leukemia (CLL): Disease Characteristics Research Report (2023–2024 emphasis)

## Target disease
- **Disease name:** Chronic lymphocytic leukemia (CLL)
- **Category:** Mature B-cell neoplasm / leukemia-lymphoma spectrum (blood and lymphoid tissues)
- **MONDO ID:** Not retrieved in the available evidence corpus (should be added from MONDO/OLS in a subsequent curation step).

---

## 1. Disease information

### 1.1 Concise overview (current understanding)
Chronic lymphocytic leukemia (CLL) is a clonal, typically **CD5-positive mature B-cell** neoplasm with accumulation of malignant B cells in **blood, bone marrow, lymph nodes, and spleen**. (hallek2019chroniclymphocyticleukemia pages 1-2)

A widely used operational definition is based on peripheral blood involvement: the **iwCLL (International Workshop on CLL) 2018 guidelines** state that the diagnosis of CLL requires **≥5 × 10^9/L clonal B lymphocytes in peripheral blood**, sustained for **at least 3 months**, with clonality confirmed by light-chain restriction on flow cytometry. (hallek2018iwcllguidelinesfor pages 1-2)

Direct abstract quote (iwCLL 2018): “**The diagnosis of CLL requires the presence of ≥5 × 10^9/L B lymphocytes in the peripheral blood, sustained for at least 3 months. The clonality of these B lymphocytes needs to be confirmed** … using flow cytometry.” (hallek2018iwcllguidelinesfor pages 1-2)

Direct abstract quote (JAMA 2023): “**Chronic lymphocytic leukemia (CLL), defined by a minimum of 5 × 10^9/L monoclonal B cells in the blood** …” (shadman2023diagnosisandtreatment pages 1-2)

### 1.2 Key identifiers and terminologies (available)
From the iwCLL guideline text, the World Health Organization (WHO) classification is referenced conceptually: CLL is described as a “leukemic … lymphoma,” distinguishable from **small lymphocytic lymphoma (SLL)** largely by leukemic (blood) manifestation. (hallek2018iwcllguidelinesfor pages 1-2)

- **ICD/MeSH/Orphanet/MONDO/OMIM IDs:** Not directly retrievable from the current tool evidence; should be added from ontology resources (OMIM/Orphanet/MeSH/MONDO) in a follow-on pass.

### 1.3 Synonyms / alternative names
- Chronic lymphocytic leukemia (CLL)
- CLL/SLL when emphasizing the continuum with **small lymphocytic lymphoma** (SLL) (hallek2018iwcllguidelinesfor pages 1-2, zhou2024improvedefficacyand pages 1-2)

### 1.4 Evidence source type
Most content here derives from **aggregated, disease-level resources** (international consensus guidelines and peer-reviewed reviews) rather than individual EHR-derived patient records. (hallek2018iwcllguidelinesfor pages 1-2, shadman2023diagnosisandtreatment pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (genetic + environmental; current evidence)
CLL etiology is multifactorial, involving inherited susceptibility plus acquired somatic lesions and microenvironmental signals.

**Familial/genetic susceptibility:** A 2024 expert review on CLL risk factors (JNCCN) concludes that “**CLL is one of the most familial of all cancers**” and that “**Genome-wide association studies have identified many common variants with low relative risks, whereas exome-wide rare variant analysis has implicated ATM in CLL causation**.” (brown2024clinicalrisksfor pages 1-2)

Direct abstract quote (Brown 2024, JNCCN): “**CLL is one of the most familial of all cancers, yet common high-penetrance risk alleles have not been identified. Genome-wide association studies have identified many common variants with low relative risks, whereas exome-wide rare variant analysis has implicated ATM in CLL causation.**” (brown2024clinicalrisksfor pages 1-2)

**Environmental factors:** The same 2024 expert review highlights limitations of exposure ascertainment but notes: “**Agent Orange and glyphosate herbicides have perhaps the most data to support their role**.” (brown2024clinicalrisksfor pages 1-2)

**Precursor condition:** The review emphasizes that CLL is preceded by monoclonal B-cell lymphocytosis (MBL): “**CLL is preceded by a precursor condition called monoclonal B-cell lymphocytosis (MBL)** … Although virtually all people with CLL have a preceding MBL phase, most people with MBL will not develop CLL.” (brown2024clinicalrisksfor pages 1-2)

### 2.2 Risk factors
- **Family history:** Brown (2024) reports that “**up to 10%** of individuals with CLL” have a first-degree relative with CLL, and summarizes large epidemiologic studies estimating a “**5- to 8-fold** increase in risk” with one affected first-degree relative and “**27-times** increase” with two affected first-degree relatives. (brown2024clinicalrisksfor pages 1-2)
- **Polygenic susceptibility:** GWAS have identified “**41 independent SNPs**” with odds ratios “**1.13 to 1.65**,” accounting for “**~25% of CLL heritability**” in aggregate; a polygenic risk score has odds ratios “**2.4 to 3.0**” for CLL development, but effect sizes are too low for clinical screening utility. (brown2024clinicalrisksfor pages 1-2)
- **Rare germline variants (ATM):** Brown (2024) describes exome-wide case-control evidence implicating rare germline variation in **ATM**; rare germline ATM variants were enriched in cases and correlated with somatic “11q deletion or somatic ATM mutation” and loss of the wild-type allele, consistent with tumor suppressor behavior. (brown2024clinicalrisksfor pages 1-2)

### 2.3 Protective factors
No protective genetic or environmental factors were directly extractable from the available evidence.

### 2.4 Gene–environment interactions
Not directly extractable from the available evidence.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with frequencies where available)
From a 2023 JAMA clinical review:
- **Asymptomatic at diagnosis:** ~**70–80%** (shadman2023diagnosisandtreatment pages 1-2)
- **Incidental lymphocytosis:** ~**70%** (shadman2023diagnosisandtreatment pages 1-2)
- **Symptomatic at presentation:** ~**30%** (shadman2023diagnosisandtreatment pages 1-2)
- **Enlarged lymph nodes:** ~**50%** (shadman2023diagnosisandtreatment pages 1-2)
- **Hepatosplenomegaly-related symptoms:** ~**20–50%** (shadman2023diagnosisandtreatment pages 1-2)
- **B symptoms (fever, drenching night sweats, weight loss ≥10%/6 months):** ~**5–10%** (shadman2023diagnosisandtreatment pages 1-2)
- **Autoimmune cytopenias:** hemolytic anemia up to **10%**, immune thrombocytopenia up to **2%** (shadman2023diagnosisandtreatment pages 1-2)
- **Hypogammaglobulinemia with frequent infections:** up to **10%** (shadman2023diagnosisandtreatment pages 1-2)

### 3.2 Age of onset and course
- **Median age at diagnosis:** ~**70 years** (shadman2023diagnosisandtreatment pages 1-2)
- **Clinical heterogeneity:** one-third may never require CLL therapy; for asymptomatic patients, “clinical observation is the standard of care.” (shadman2023diagnosisandtreatment pages 1-2)

### 3.3 Suggested HPO mappings (curation suggestions; not exhaustive)
(These are ontology suggestions and require mapping/validation against HPO.)
- Lymphocytosis (HP:0001974)
- Lymphadenopathy (HP:0002716)
- Splenomegaly (HP:0001744)
- Hepatomegaly (HP:0002240)
- Fever (HP:0001945)
- Night sweats (HP:0030166)
- Weight loss (HP:0001824)
- Anemia (HP:0001903)
- Thrombocytopenia (HP:0001873)
- Hypogammaglobulinemia (HP:0004313)
- Recurrent infections (HP:0002719)

---

## 4. Genetic / molecular information

### 4.1 Major cytogenetic abnormalities (common clinical biomarkers)
A widely used risk stratification approach in CLL includes interphase FISH and key recurrent lesions. A 2019 American Journal of Hematology update summarizes approximate frequencies:
- **del(13q14): ~55%** (hallek2019chroniclymphocyticleukemia pages 1-2)
- **Trisomy 12: ~10–20%** (hallek2019chroniclymphocyticleukemia pages 1-2)
- **del(17p) in chemo-naïve patients: ~5–8%** (often implicating **TP53**) (hallek2019chroniclymphocyticleukemia pages 1-2)

Additionally, a large multicenter cohort (ERIC/HARMONY; 4580 patients) reported baseline cytogenetics frequencies: **del(13q) 42%, trisomy 12 13%, del(11q) 11%, del(17p) 5%**. (mansouri2023differentprognosticimpact pages 1-2)

### 4.2 Somatic driver genes and prognostic mutations
A large 2023 Leukemia study (ERIC in HARMONY) assessed nine recurrent genes (BIRC3, EGR2, MYD88, NFKBIE, NOTCH1, POT1, SF3B1, TP53, XPO1) in **4580** pre-treatment samples:
- Mutations detected in **34.7%** of patients; frequencies across genes ranged **2.3–9.8%**; **NOTCH1** was most frequent. (mansouri2023differentprognosticimpact pages 1-2)
- Mutations in all genes except **MYD88** were associated with significantly shorter time-to-first-treatment (TTFT) in multivariable analysis. (mansouri2023differentprognosticimpact pages 1-2)
- Prognostic impact differed by IGHV SHM status: **SF3B1** and **XPO1** were adverse in both IGHV-mutated and unmutated CLL; **TP53/BIRC3/EGR2** adverse in unmutated CLL only; **NOTCH1/NFKBIE** adverse in IGHV-mutated CLL only. (mansouri2023differentprognosticimpact pages 1-2)

Direct abstract quote (Mansouri 2023): “**Mutations were detected in 1588 (34.7%) patients … In both univariate and multivariate analyses, mutations in all genes except MYD88 were associated with a significantly shorter TTFT.**” (mansouri2023differentprognosticimpact pages 1-2)

### 4.3 Microenvironment-selected lesions and therapy interaction (example)
A 2024 Leukemia mechanistic study reports that **loss-of-function NFKBIE mutations** are selected by microenvironmental NF-κB-activating signals and promote immune escape (exhausted CD8+ T cells; increased PD-L1 on malignant B cells) and are associated with **inferior outcomes to ibrutinib** in NFKBIE-mutated patients. (bonato2024nfkbiemutationsare pages 1-2)

Direct abstract quote (Bonato 2024): “**NFKBIE-mutated CLL cells are selected by microenvironmental signals that activate the NF-κB pathway** … allowing for immune escape, including **expansion of CD8+ T-cells with an exhausted phenotype and increased PD-L1 expression on the malignant B-cells**.” (bonato2024nfkbiemutationsare pages 1-2)

### 4.4 Suggested ontology mappings (examples)
- **Genes (HGNC symbols):** TP53, ATM, BIRC3, SF3B1, NOTCH1, NFKBIE, XPO1, POT1, MYD88 (hallek2019chroniclymphocyticleukemia pages 1-2, mansouri2023differentprognosticimpact pages 1-2, brown2024clinicalrisksfor pages 1-2, bonato2024nfkbiemutationsare pages 1-2)
- **Cytogenetic features:** del(17p), del(11q), trisomy 12, del(13q) (hallek2019chroniclymphocyticleukemia pages 1-2, mansouri2023differentprognosticimpact pages 1-2)

---

## 5. Environmental information

### 5.1 Environmental exposures
Evidence summary from an authoritative 2024 risk-factor review indicates environmental risks are difficult to quantify retrospectively, but **Agent Orange** and **glyphosate herbicides** have the strongest current supporting data among exposures discussed. (brown2024clinicalrisksfor pages 1-2)

### 5.2 Infectious agents
No infectious causation was supported by the retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Core upstream-to-downstream causal chain (high-level)
1. **Inherited susceptibility** (polygenic common variants; rare germline ATM variants in a subset) increases probability of developing precursor clonal expansions such as MBL. (brown2024clinicalrisksfor pages 1-2)
2. **Acquired genetic lesions** (e.g., TP53 disruption; del(17p); del(11q)/ATM; NOTCH1, SF3B1, BIRC3, NFKBIE) promote impaired apoptosis, altered DNA damage response, and survival advantages. (hallek2019chroniclymphocyticleukemia pages 1-2, mansouri2023differentprognosticimpact pages 1-2, bonato2024nfkbiemutationsare pages 1-2)
3. **Microenvironmental signaling** (BCR and inflammatory/NF-κB signaling) fosters growth/survival and can select for subclones adapted to these cues (example: NFKBIE-mutant selection by NF-κB-activating signals). (bonato2024nfkbiemutationsare pages 1-2)
4. **Immune dysfunction and immune escape**: CLL is associated with immunocompromise, increased infection complications, and tumor-induced immune suppression (e.g., PD-1/PD-L1 axis, exhausted T cells). (shadman2023diagnosisandtreatment pages 1-2, bonato2024nfkbiemutationsare pages 1-2)

### 6.2 Tumor microenvironment–immune dysfunction (recent primary evidence)
**Soluble factor–mediated T-cell suppression (IL-9):** A 2024 Cell Death & Disease paper provides direct evidence that soluble factors secreted by CLL cells can drive PD-1 upregulation and functional impairment of cytotoxic T lymphocytes (CTLs), including in the Eμ-TCL1 model.

Direct abstract quote (Boncompagni 2024): “**healthy CTLs cultured in media conditioned by leukemic cells from CLL patients or Eμ-TCL1 mice upregulate the exhaustion marker PD-1 and become unable to form functional [immune synapses] and kill target cells**.” (boncompagni2024leukemiccellsecretedinterleukin9 pages 1-3)

It further identifies IL-9 as a key mediator: “**IL-9, but not IL-10, mediates both the enhancement in PD-1 expression and the suppression of effector functions** … highlighting a new suppressive mechanism and a novel potential therapeutical target in CLL.” (boncompagni2024leukemiccellsecretedinterleukin9 pages 1-3)

**Microbiome diversity and CLL aggressiveness:** A 2024 Haematologica study links gut microbiome diversity with clinical course in humans and disease kinetics in Eμ-TCL1 mice.

Direct abstract quote (Faitová 2024): “**CLL patients with lower microbiome diversity … suffered from a more advanced or aggressive form of CLL. In the Eµ-TCL1 mouse model … we observed a faster course of disease when mice were housed in high hygiene conditions** … associated with a lower microbiome diversity …” (faitova2024thediversityof pages 1-2)

### 6.3 Suggested GO biological process terms (examples; require formal curation)
- B cell receptor signaling pathway (GO:0050853)
- NF-kappaB signaling (e.g., GO:0043122)
- Regulation of apoptotic process (GO:0042981)
- Immune effector process / T cell activation / T cell exhaustion-related programs (requires specific GO mapping)

### 6.4 Suggested Cell Ontology (CL) terms (examples)
- B cell (CL:0000236); malignant CLL B cell (needs specific disease-cell mapping)
- Cytotoxic T cell (CL:0000910)
- CD8-positive T cell (CL:0000625)

---

## 7. Anatomical structures affected

CLL involves:
- **Peripheral blood** (leukemic manifestation used in diagnostic definition). (hallek2018iwcllguidelinesfor pages 1-2)
- **Bone marrow** (cytopenias from marrow failure are key treatment indications in iwCLL). (hallek2018iwcllguidelinesfor media 86780099)
- **Lymph nodes** (lymphadenopathy is common). (shadman2023diagnosisandtreatment pages 1-2)
- **Spleen and liver** (hepatosplenomegaly). (shadman2023diagnosisandtreatment pages 1-2)

Suggested UBERON mappings (examples):
- Blood (UBERON:0000178)
- Bone marrow (UBERON:0002371)
- Lymph node (UBERON:0000029)
- Spleen (UBERON:0002106)
- Liver (UBERON:0002107)

---

## 8. Temporal development

### 8.1 Onset
- Predominantly a disease of older adults: median age at diagnosis ~70 years. (shadman2023diagnosisandtreatment pages 1-2)

### 8.2 Progression and staging
iwCLL 2018 emphasizes Rai and Binet staging systems (clinical exam + labs) and integrated prognostic models. The CLL-IPI includes clinical stage, age, IGHV status, β2-microglobulin, and del(17p)/TP53. (hallek2018iwcllguidelinesfor pages 4-5)

Direct guideline text quote: “**the CLL-IPI consists of … clinical stage, age, IGHV mutational status, serum β2-microglobulin, and the presence of del(17p) and/or TP53 mutations**.” (hallek2018iwcllguidelinesfor pages 4-5)

---

## 9. Inheritance and population

### 9.1 Epidemiology (selected, evidence-based)
From a 2023 JAMA review:
- **>200,000** people living with CLL in the US
- **~4,410 deaths/year** in the US
- **Male predominance ~1.7:1**
- Approximate survival: **~90% 5-year**, **~82% 10-year**
(shadman2023diagnosisandtreatment pages 1-2)

### 9.2 Inheritance pattern
No single Mendelian inheritance pattern dominates; evidence supports polygenic susceptibility and rare germline risk variants in specific genes (e.g., ATM), with strong familial clustering but no common high-penetrance allele identified. (brown2024clinicalrisksfor pages 1-2)

---

## 10. Diagnostics

### 10.1 Diagnostic testing (guideline-based)
**Required blood criterion:** iwCLL requires **≥5 × 10^9/L clonal B lymphocytes** for ≥3 months, with flow cytometry confirmation. (hallek2018iwcllguidelinesfor pages 1-2)

**Immunophenotyping panel:** iwCLL notes a “panel of CD19, CD5, CD20, CD23, κ, and λ” is usually sufficient to establish diagnosis, with additional markers (CD43, CD79b, CD81, CD200, CD10, ROR1) for borderline cases. (hallek2018iwcllguidelinesfor pages 1-2)

### 10.2 Indications to start therapy (iwCLL “active disease” concept)
iwCLL 2018 provides treatment-indication logic based on stage and “active disease,” including progressive marrow failure and symptomatic bulky disease; the guideline’s table/criteria were retrieved as an image (see cited figure region). (hallek2018iwcllguidelinesfor media 86780099)

**Visual evidence:** Cropped guideline table/criteria region from iwCLL 2018 is available. (hallek2018iwcllguidelinesfor media 86780099)

---

## 11. Outcomes / prognosis

### 11.1 Variable clinical course
- A large proportion is asymptomatic at diagnosis, and “one-third will never require treatment.” (shadman2023diagnosisandtreatment pages 1-2)

### 11.2 Prognostic biomarkers (modern)
- Core prognostic markers include IGHV mutational status, del(17p)/TP53 disruption, and additional recurrent mutations with TTFT impact (SF3B1, XPO1, NOTCH1, NFKBIE, etc.). (hallek2018iwcllguidelinesfor pages 4-5, mansouri2023differentprognosticimpact pages 1-2)

### 11.3 Richter transformation (complication)
A 2023 JAMA review notes Richter transformation occurs “up to 10% … (0.5–1%/yr)” and is associated with poor median overall survival (OS) in heavily pretreated disease. (shadman2023diagnosisandtreatment pages 12-13)

---

## 12. Treatment

### 12.1 Current standard approaches (frontline)
A 2023 JAMA review states that first-line therapy for symptomatic disease consists of either:
- a **covalent BTK inhibitor** (acalabrutinib, zanubrutinib, ibrutinib), or
- a **BCL2 inhibitor** regimen based on venetoclax (commonly venetoclax + obinutuzumab)
with no evidence that sequencing one class before the other improves outcomes. (shadman2023diagnosisandtreatment pages 1-2)

Direct abstract quote (JAMA 2023): “**first-line treatment consists of a regimen containing either a covalent Bruton tyrosine kinase (BTK) inhibitor … or a … BCL2 inhibitor (venetoclax). There is no evidence that starting either class before the other improves outcomes.**” (shadman2023diagnosisandtreatment pages 1-2)

### 12.2 Fixed-duration venetoclax + obinutuzumab: long-term outcomes (2023 primary trial follow-up)
The CLL14 5-year analysis (Nature Communications 2023) reports:
- Median follow-up **65.4 months**
- PFS superior for Ven-Obi vs Clb-Obi: **HR 0.35 (95% CI 0.26–0.46), p<0.0001**
- **5-year PFS 62.6%** (Ven-Obi) vs **27.0%** (Clb-Obi)
(alsawaf2023transcriptomicprofilesand pages 1-2)

Direct abstract quote: “**At 5 years after randomization, the estimated PFS rate is 62.6% after Ven-Obi and 27.0% after Clb-Obi.**” (alsawaf2023transcriptomicprofilesand pages 1-2)

### 12.3 Relapsed/refractory implementation example (2024): ALPINE subgroup (China)
In relapsed/refractory CLL/SLL, a 2024 Annals of Hematology report (ALPINE China subgroup) found:
- ORR **80.9%** zanubrutinib vs **72.1%** ibrutinib
- PFS improved with zanubrutinib: **HR 0.34 (95% CI 0.15–0.77)**
- Lower discontinuation due to AEs: **6.4% vs 14.0%**
(zhou2024improvedefficacyand pages 1-2)

### 12.4 Non-covalent BTK inhibitor (pirtobrutinib) after BTKi intolerance (BRUIN)
In BTKi-intolerant patients (BRUIN phase I/II), pirtobrutinib produced in CLL/SLL:
- ORR **76.9%** (78 patients)
- Median PFS **28.4 months**
- Median follow-up **17.4 months**
with notable tolerability signals (e.g., no discontinuations for the same AE that caused prior BTKi discontinuation). (shah2024pirtobrutinibmonotherapyin pages 1-2)

### 12.5 Cellular therapy
CAR-T therapy with lisocabtagene maraleucel in multiply relapsed CLL was associated with **45% complete response** in the JAMA summary. (shadman2023diagnosisandtreatment pages 1-2)

### 12.6 MAXO suggestions (examples)
- Antineoplastic agent therapy (MAXO:0000014)
- Monoclonal antibody therapy (anti-CD20) (MAXO:0000647)
- Small molecule therapy (BTK inhibitor; BCL2 inhibitor) (requires specific MAXO term mapping)
- Chimeric antigen receptor T-cell therapy (MAXO term required)
- Allogeneic hematopoietic cell transplantation (MAXO term required)

### 12.7 Summary table of modern therapies
| Setting | Regimen / class | Key efficacy stats | Key safety notes | Duration strategy | Publication date | URL | Citations |
|---|---|---|---|---|---|---|---|
| Frontline, treatment-naive CLL requiring therapy | Acalabrutinib (covalent BTK inhibitor) | Survival rate approximately **88% at 4 years** in first-line use; guideline-level summary identifies covalent BTKi as a standard first-line option (shadman2023diagnosisandtreatment pages 1-2) | Second-generation BTKi generally has fewer discontinuations and less atrial fibrillation than ibrutinib in comparative data summarized in the review; BTKi are used with attention to class toxicities including cardiac events, bleeding, arthralgia, rash, and infection risk (shadman2023diagnosisandtreatment pages 4-5, shadman2023diagnosisandtreatment pages 1-2) | Continuous / indefinite | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | (shadman2023diagnosisandtreatment pages 4-5, shadman2023diagnosisandtreatment pages 1-2) |
| Frontline, treatment-naive CLL requiring therapy | Zanubrutinib (covalent BTK inhibitor) | Survival rate approximately **94% at 2 years** in first-line use; listed as a standard first-line covalent BTKi option (shadman2023diagnosisandtreatment pages 1-2) | Review summary indicates lower atrial fibrillation than ibrutinib, though neutropenia may be more frequent in some comparisons; newer BTKi generally favored over ibrutinib for safety (shadman2023diagnosisandtreatment pages 12-13, shadman2023diagnosisandtreatment pages 1-2) | Continuous / indefinite | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | (shadman2023diagnosisandtreatment pages 12-13, shadman2023diagnosisandtreatment pages 1-2) |
| Frontline, treatment-naive CLL requiring therapy | Ibrutinib (covalent BTK inhibitor) | Survival rate approximately **78% at 7 years** in first-line use; remains an effective frontline BTKi option in review summaries (shadman2023diagnosisandtreatment pages 1-2) | Notable toxicity burden in review summary: arthralgia, atrial fibrillation, rash, bleeding/infection concerns; higher discontinuation than acalabrutinib in summarized comparisons (shadman2023diagnosisandtreatment pages 4-5, shadman2023diagnosisandtreatment pages 1-2) | Continuous / indefinite | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | (shadman2023diagnosisandtreatment pages 4-5, shadman2023diagnosisandtreatment pages 1-2) |
| Frontline, previously untreated CLL with coexisting conditions | Venetoclax + obinutuzumab (BCL2 inhibitor + anti-CD20) | **CLL14**: after **median follow-up 65.4 months**, PFS superior vs chlorambucil-obinutuzumab, **HR 0.35 (95% CI 0.26-0.46; p<0.0001)**; **5-year PFS 62.6% vs 27.0%**. JAMA review summarizes **overall survival 82% at 5-year follow-up** (alsawaf2023transcriptomicprofilesand pages 1-2, shadman2023diagnosisandtreatment pages 1-2) | End-of-treatment MRD positivity associated with shorter PFS; inflammatory response pathways enriched in MRD-positive patients in Ven-Obi arm. Requires venetoclax-specific monitoring in practice, including tumor lysis risk management (efficacy paper plus review context) (alsawaf2023transcriptomicprofilesand pages 1-2, shadman2023diagnosisandtreatment pages 1-2) | Fixed-duration, **1 year** | 2023-04-13 | https://doi.org/10.1038/s41467-023-37648-w | (alsawaf2023transcriptomicprofilesand pages 1-2, shadman2023diagnosisandtreatment pages 1-2) |
| Relapsed/refractory CLL/SLL, China subgroup of ALPINE | Zanubrutinib vs ibrutinib (head-to-head covalent BTKi comparison) | With **median follow-up 25.3 months**, **ORR 80.9% vs 72.1%**; **PFS HR 0.34 (95% CI 0.15-0.77)** favoring zanubrutinib; OS HR 0.45 (95% CI 0.14-1.50) (zhou2024improvedefficacyand pages 1-2) | Lower rates with zanubrutinib vs ibrutinib of **grade ≥3 TEAEs 64.4% vs 72.1%**, **AEs leading to discontinuation 6.4% vs 14.0%**, and **serious TEAEs 35.6% vs 51.2%** (zhou2024improvedefficacyand pages 1-2) | Continuous until progression or unacceptable toxicity | 2024-06-18 | https://doi.org/10.1007/s00277-024-05823-8 | (zhou2024improvedefficacyand pages 1-2) |
| Relapsed/refractory B-cell malignancies; BTKi-intolerant CLL/SLL subset in BRUIN | Pirtobrutinib (non-covalent BTK inhibitor) | In **78 CLL/SLL** patients intolerant to prior BTKi, **ORR 76.9%**; **median PFS 28.4 months**; median follow-up **17.4 months** (shah2024pirtobrutinibmonotherapyin pages 1-2) | Most common prior BTKi-discontinuation reason was cardiac disorders, especially atrial fibrillation. On pirtobrutinib, frequent TEAE were **fatigue 39.4%** and **neutropenia 37.0%**; among patients who stopped prior BTKi for a cardiac issue, **75% had no recurrence** of that cardiac AE; **no patient discontinued pirtobrutinib for the same AE** that caused prior BTKi discontinuation (shah2024pirtobrutinibmonotherapyin pages 1-2) | Continuous | Early view 2024-10-03; journal issue 2025-01 | https://doi.org/10.3324/haematol.2024.285754 | (shah2024pirtobrutinibmonotherapyin pages 1-2) |
| Multiply relapsed / heavily pretreated CLL | Lisocabtagene maraleucel CAR-T (cellular therapy) | JAMA review summary: CAR-T with lisocabtagene maraleucel associated with **45% complete response rate**; separate review summary also notes TRANSCEND overall response **82%** with durable MRD-negative remissions in blood and marrow in some patients (shadman2023diagnosisandtreatment pages 1-2, shadman2023diagnosisandtreatment pages 12-13) | Cytokine release syndrome and neurologic events are major toxicities highlighted in review summaries (shadman2023diagnosisandtreatment pages 12-13) | Finite cellular therapy | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | (shadman2023diagnosisandtreatment pages 12-13, shadman2023diagnosisandtreatment pages 1-2) |


*Table: This table summarizes major contemporary CLL therapies across frontline and relapsed/refractory settings using only extracted evidence from the cited sources. It highlights efficacy, safety, treatment duration strategy, and publication metadata for rapid comparison.*

---

## 13. Prevention

### 13.1 Primary prevention
No proven primary prevention strategy is established; risk-factor identification remains incomplete. (brown2024clinicalrisksfor pages 1-2)

### 13.2 Secondary prevention / early detection
Routine population screening is not supported by the evidence provided; many patients are managed with watchful waiting. (shadman2023diagnosisandtreatment pages 1-2, brown2024clinicalrisksfor pages 1-2)

### 13.3 Infection prevention (supportive care)
CLL is associated with immunocompromise and infection complications. The 2023 JAMA review recommends vaccination against **influenza, pneumococcus, COVID-19, and varicella zoster** for CLL patients, and notes IVIG can benefit those with hypogammaglobulinemia and recurrent infections. (shadman2023diagnosisandtreatment pages 4-5, shadman2023diagnosisandtreatment pages 1-2)

---

## 14. Other species / natural disease
Direct evidence for naturally occurring CLL-like disease in non-human species was not retrieved in the current corpus.

---

## 15. Model organisms

### 15.1 Eμ-TCL1 mouse model (widely used; recent examples)
Multiple 2024 primary studies explicitly used **Eμ-TCL1** mice as an in vivo model of CLL pathophysiology:
- Microbiome diversity influences CLL development kinetics in Eμ-TCL1 mice. (faitova2024thediversityof pages 1-2)
- Conditioned media from leukemic cells from Eμ-TCL1 mice induce PD-1 upregulation and CTL dysfunction; IL-9 mediates immune suppression. (boncompagni2024leukemiccellsecretedinterleukin9 pages 1-3)
- NFKBIE-mutant functional studies use Eμ-TCL1-derived murine leukemia lines and in vivo models to link microenvironmental selection, immune escape, and BTKi response. (bonato2024nfkbiemutationsare pages 1-2)

Evidence types include **in vivo murine models** and **human patient sample analyses** (microbiome cohort of 59 CLL patients; immune suppression studies include human CLL patient-derived leukemic cells and mouse). (faitova2024thediversityof pages 1-2, boncompagni2024leukemiccellsecretedinterleukin9 pages 1-3)

---

## Summary artifact: definition, epidemiology, presentation, cytogenetics
| Domain | Item | Key data / finding | Publication date | URL | Evidence type | PaperQA citation IDs |
|---|---|---|---|---|---|---|
| Definition / diagnosis | Core CLL diagnostic threshold | CLL requires **\>=5 × 10^9/L clonal B lymphocytes in peripheral blood**, sustained for **at least 3 months**; clonality confirmed by light-chain restriction on flow cytometry | 2018-06-21 | https://doi.org/10.1182/blood-2017-09-806398 | Guideline / consensus criteria | (hallek2018iwcllguidelinesfor pages 1-2, hallek2018iwcllguidelinesfor media 015ffd7a) |
| Guideline source | iwCLL guidelines for diagnosis, indications for treatment, response assessment, and supportive management of CLL | International consensus guideline updating diagnosis, MRD, prognostic genetics, response criteria, and supportive management | 2018-06-21 | https://doi.org/10.1182/blood-2017-09-806398 | Guideline / consensus statement | (hallek2018iwcllguidelinesfor pages 1-2, hallek2018iwcllguidelinesfor pages 4-5) |
| Guideline source | JAMA review: Diagnosis and Treatment of Chronic Lymphocytic Leukemia | High-level clinical review summarizing modern diagnosis, prognosis, treatment indications, and targeted therapies | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Peer-reviewed clinical review | (shadman2023diagnosisandtreatment pages 1-2) |
| Epidemiology | People living with CLL in the US | **>200,000** people in the US living with a CLL diagnosis | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review citing US epidemiology | (shadman2023diagnosisandtreatment pages 1-2) |
| Epidemiology | Annual US deaths | Approximately **4,410 deaths/year** in the US | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review citing US epidemiology | (shadman2023diagnosisandtreatment pages 1-2) |
| Epidemiology | Median age at diagnosis | **70 years** | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review / clinical summary | (shadman2023diagnosisandtreatment pages 1-2) |
| Epidemiology / presentation | Asymptomatic at diagnosis | Approximately **70%–80%** asymptomatic at diagnosis | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review / clinical summary | (shadman2023diagnosisandtreatment pages 1-2) |
| Presenting features | Incidental lymphocytosis | Asymptomatic incidental lymphocytosis in about **70%** at presentation | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review (Box 1) | (shadman2023diagnosisandtreatment pages 1-2) |
| Presenting features | Enlarged lymph nodes | Approximately **50%** | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review (Box 1) | (shadman2023diagnosisandtreatment pages 1-2) |
| Presenting features | Enlarged spleen or liver | Approximately **20%–50%** | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review (Box 1) | (shadman2023diagnosisandtreatment pages 1-2) |
| Presenting features | Constitutional/B symptoms | Fever / drenching night sweats / \>=10% weight loss within 6 months in about **5%–10%** | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review (Box 1) | (shadman2023diagnosisandtreatment pages 1-2) |
| Presenting features | Autoimmune hemolytic anemia | Up to **10%** | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review (Box 1) | (shadman2023diagnosisandtreatment pages 1-2) |
| Presenting features | Immune thrombocytopenia | Up to **2%** | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review (Box 1) | (shadman2023diagnosisandtreatment pages 1-2) |
| Presenting features | Hypogammaglobulinemia with frequent infections | Up to **10%** | 2023-03-21 | https://doi.org/10.1001/jama.2023.1946 | Review (Box 1) | (shadman2023diagnosisandtreatment pages 1-2) |
| Prognostic genetics / cytogenetics | del(13q14) | Most common cytogenetic lesion, about **55%** | 2019-11 | https://doi.org/10.1002/ajh.25595 | Review / risk-stratification summary | (hallek2019chroniclymphocyticleukemia pages 1-2) |
| Prognostic genetics / cytogenetics | Trisomy 12 | Approximately **10%–20%** | 2019-11 | https://doi.org/10.1002/ajh.25595 | Review / risk-stratification summary | (hallek2019chroniclymphocyticleukemia pages 1-2) |
| Prognostic genetics / cytogenetics | del(17p) in untreated / chemo-naive disease | Approximately **5%–8%** in chemo-naive patients; usually implicates **TP53** loss/disruption and predicts poor response to chemoimmunotherapy | 2019-11 | https://doi.org/10.1002/ajh.25595 | Review / prognostic genetics summary | (hallek2019chroniclymphocyticleukemia pages 1-2) |


*Table: This table condenses core CLL definition, guideline sources, epidemiology, presenting features, and major prognostic cytogenetic frequencies into a single quick-reference artifact. It is designed to support knowledge-base population with directly citable evidence and URLs.*

---

## Visual evidence (guideline figure/table)
A cropped image region from iwCLL 2018 capturing the **diagnostic threshold** and **treatment-indication framework** (“active disease” criteria) was retrieved. (hallek2018iwcllguidelinesfor media 015ffd7a, hallek2018iwcllguidelinesfor media 86780099)

---

## Limitations of this tool-based report
- Ontology identifiers (MONDO/MeSH/ICD/Orphanet/OMIM) were not directly retrievable from the available documents; they should be added from dedicated ontology resources.
- Several key areas requested (e.g., comprehensive differential diagnosis lists, detailed MRD assay standards, and broad real-world effectiveness datasets) would benefit from additional targeted retrieval beyond the current evidence set.

---

## Key source URLs (with publication dates)
- iwCLL guidelines (Blood) — 2018-06-21 — https://doi.org/10.1182/blood-2017-09-806398 (hallek2018iwcllguidelinesfor pages 1-2)
- Shadman (JAMA review) — 2023-03-21 — https://doi.org/10.1001/jama.2023.1946 (shadman2023diagnosisandtreatment pages 1-2)
- Al-Sawaf et al., CLL14 5-year follow-up (Nature Communications) — 2023-04-13 — https://doi.org/10.1038/s41467-023-37648-w (alsawaf2023transcriptomicprofilesand pages 1-2)
- Brown (JNCCN) CLL risk factors — 2024-04 — https://doi.org/10.6004/jnccn.2024.7020 (brown2024clinicalrisksfor pages 1-2)
- Mansouri et al. ERIC/HARMONY prognostic mutations (Leukemia) — 2023-12 — https://doi.org/10.1038/s41375-022-01802-y (mansouri2023differentprognosticimpact pages 1-2)
- Zhou et al. ALPINE China subgroup (Annals of Hematology) — 2024-06-18 — https://doi.org/10.1007/s00277-024-05823-8 (zhou2024improvedefficacyand pages 1-2)
- Boncompagni et al. IL-9 immune suppression (Cell Death & Disease) — 2024-02 — https://doi.org/10.1038/s41419-024-06528-6 (boncompagni2024leukemiccellsecretedinterleukin9 pages 1-3)
- Faitová et al. microbiome diversity (Haematologica) — 2024-05-09 (early view) — https://doi.org/10.3324/haematol.2023.284693 (faitova2024thediversityof pages 1-2)
- Bonato et al. NFKBIE and immune escape (Leukemia) — 2024-03 — https://doi.org/10.1038/s41375-024-02224-8 (bonato2024nfkbiemutationsare pages 1-2)
- Shah et al. pirtobrutinib intolerance cohort (Haematologica early view) — 2024-10-03 — https://doi.org/10.3324/haematol.2024.285754 (shah2024pirtobrutinibmonotherapyin pages 1-2)

References

1. (hallek2019chroniclymphocyticleukemia pages 1-2): Michael Hallek. Chronic lymphocytic leukemia: 2020 update on diagnosis, risk stratification and treatment. American Journal of Hematology, 94:1266-1287, Nov 2019. URL: https://doi.org/10.1002/ajh.25595, doi:10.1002/ajh.25595. This article has 750 citations and is from a domain leading peer-reviewed journal.

2. (hallek2018iwcllguidelinesfor pages 1-2): Michael Hallek, Bruce D. Cheson, Daniel Catovsky, Federico Caligaris-Cappio, Guillermo Dighiero, Hartmut Döhner, Peter Hillmen, Michael Keating, Emili Montserrat, Nicholas Chiorazzi, Stephan Stilgenbauer, Kanti R. Rai, John C. Byrd, Barbara Eichhorst, Susan O’Brien, Tadeusz Robak, John F. Seymour, and Thomas J. Kipps. Iwcll guidelines for diagnosis, indications for treatment, response assessment, and supportive management of cll. Blood, 131 25:2745-2760, Jun 2018. URL: https://doi.org/10.1182/blood-2017-09-806398, doi:10.1182/blood-2017-09-806398. This article has 2326 citations and is from a highest quality peer-reviewed journal.

3. (shadman2023diagnosisandtreatment pages 1-2): Mazyar Shadman. Diagnosis and treatment of chronic lymphocytic leukemia: a review. JAMA, 329 11:918-932, Mar 2023. URL: https://doi.org/10.1001/jama.2023.1946, doi:10.1001/jama.2023.1946. This article has 270 citations.

4. (zhou2024improvedefficacyand pages 1-2): Keshu Zhou, Tingyu Wang, Ling Pan, Wei Xu, Jie Jin, Wei Zhang, Yu Hu, Jianda Hu, Ru Feng, Ping Li, Zhougang Liu, Peng Liu, Hongmei Jing, Sujun Gao, Huilai Zhang, Kang Yu, Zhao Wang, Xiongpeng Zhu, Zimin Sun, Fei Li, Dongmei Yan, Jianyu Weng, Lina Fu, Liping Wang, Tommi Salmi, Kenneth Wu, and Lugui Qiu. Improved efficacy and safety of zanubrutinib versus ibrutinib in patients with relapsed/refractory chronic lymphocytic leukemia (r/r cll) in china: a subgroup of alpine. Annals of Hematology, 103:4183-4191, Jun 2024. URL: https://doi.org/10.1007/s00277-024-05823-8, doi:10.1007/s00277-024-05823-8. This article has 8 citations and is from a peer-reviewed journal.

5. (brown2024clinicalrisksfor pages 1-2): Jennifer R. Brown. Clinical risks for chronic lymphocytic leukemia. Journal of the National Comprehensive Cancer Network : JNCCN, Apr 2024. URL: https://doi.org/10.6004/jnccn.2024.7020, doi:10.6004/jnccn.2024.7020. This article has 7 citations.

6. (mansouri2023differentprognosticimpact pages 1-2): Larry Mansouri, Birna Thorvaldsdottir, Lesley-Ann Sutton, Georgios Karakatsoulis, Manja Meggendorfer, Helen Parker, Ferran Nadeu, Christian Brieghel, Stamatia Laidou, Riccardo Moia, Davide Rossi, Mark Catherwood, Jana Kotaskova, Julio Delgado, Ana E. Rodríguez-Vicente, Rocío Benito, Gian Matteo Rigolin, Silvia Bonfiglio, Lydia Scarfo, Mattias Mattsson, Zadie Davis, Ajay Gogia, Lata Rani, Panagiotis Baliakas, Hassan Foroughi-Asl, Cecilia Jylhä, Aron Skaftason, Inmaculada Rapado, Fatima Miras, Joaquín Martinez-Lopez, Javier de la Serna, Jesús María Hernández Rivas, Patrick Thornton, María José Larráyoz, María José Calasanz, Viktória Fésüs, Zoltán Mátrai, Csaba Bödör, Karin E. Smedby, Blanca Espinet, Anna Puiggros, Ritu Gupta, Lars Bullinger, Francesc Bosch, Bárbara Tazón-Vega, Fanny Baran-Marszak, David Oscier, Florence Nguyen-Khac, Thorsten Zenz, Maria Jose Terol, Antonio Cuneo, María Hernández-Sánchez, Sarka Pospisilova, Ken Mills, Gianluca Gaidano, Carsten U. Niemann, Elias Campo, Jonathan C. Strefford, Paolo Ghia, Kostas Stamatopoulos, and Richard Rosenquist. Different prognostic impact of recurrent gene mutations in chronic lymphocytic leukemia depending on ighv gene somatic hypermutation status: a study by eric in harmony. Leukemia, 37:339-347, Dec 2023. URL: https://doi.org/10.1038/s41375-022-01802-y, doi:10.1038/s41375-022-01802-y. This article has 73 citations and is from a highest quality peer-reviewed journal.

7. (bonato2024nfkbiemutationsare pages 1-2): Alice Bonato, Supriya Chakraborty, Riccardo Bomben, Giulia Canarutto, Giulia Felician, Claudio Martines, Antonella Zucchetto, Federico Pozzo, Marija Vujovikj, Jerry Polesel, Annalisa Chiarenza, Maria Ilaria Del Principe, Giovanni Del Poeta, Giovanni D’Arena, Roberto Marasca, Agostino Tafuri, Luca Laurenti, Silvano Piazza, Aleksandar J. Dimovski, Valter Gattei, and Dimitar G. Efremov. Nfkbie mutations are selected by the tumor microenvironment and contribute to immune escape in chronic lymphocytic leukemia. Leukemia, 38:1511-1521, Mar 2024. URL: https://doi.org/10.1038/s41375-024-02224-8, doi:10.1038/s41375-024-02224-8. This article has 20 citations and is from a highest quality peer-reviewed journal.

8. (boncompagni2024leukemiccellsecretedinterleukin9 pages 1-3): Gioia Boncompagni, Vanessa Tatangelo, Ludovica Lopresti, Cristina Ulivieri, Nagaja Capitani, Carmela Tangredi, Francesca Finetti, Giuseppe Marotta, Federica Frezzato, Andrea Visentin, Sara Ciofini, Alessandro Gozzetti, Monica Bocchia, Diego Calzada-Fraile, Noa B. Martin Cofreces, Livio Trentin, Laura Patrussi, and Cosima T. Baldari. Leukemic cell-secreted interleukin-9 suppresses cytotoxic t cell-mediated killing in chronic lymphocytic leukemia. Cell Death &amp; Disease, Feb 2024. URL: https://doi.org/10.1038/s41419-024-06528-6, doi:10.1038/s41419-024-06528-6. This article has 10 citations and is from a peer-reviewed journal.

9. (faitova2024thediversityof pages 1-2): Tereza Faitova, Mariana Coelho, Caspar Da Cunha-Bang, Selcen Ozturk, Ece Kartal, Peer Bork, Martina Seiffert, and Carsten U. Niemann. The diversity of the microbiome impacts chronic lymphocytic leukemia development in mice and humans. Haematologica, 109:3237-3250, May 2024. URL: https://doi.org/10.3324/haematol.2023.284693, doi:10.3324/haematol.2023.284693. This article has 12 citations.

10. (hallek2018iwcllguidelinesfor media 86780099): Michael Hallek, Bruce D. Cheson, Daniel Catovsky, Federico Caligaris-Cappio, Guillermo Dighiero, Hartmut Döhner, Peter Hillmen, Michael Keating, Emili Montserrat, Nicholas Chiorazzi, Stephan Stilgenbauer, Kanti R. Rai, John C. Byrd, Barbara Eichhorst, Susan O’Brien, Tadeusz Robak, John F. Seymour, and Thomas J. Kipps. Iwcll guidelines for diagnosis, indications for treatment, response assessment, and supportive management of cll. Blood, 131 25:2745-2760, Jun 2018. URL: https://doi.org/10.1182/blood-2017-09-806398, doi:10.1182/blood-2017-09-806398. This article has 2326 citations and is from a highest quality peer-reviewed journal.

11. (hallek2018iwcllguidelinesfor pages 4-5): Michael Hallek, Bruce D. Cheson, Daniel Catovsky, Federico Caligaris-Cappio, Guillermo Dighiero, Hartmut Döhner, Peter Hillmen, Michael Keating, Emili Montserrat, Nicholas Chiorazzi, Stephan Stilgenbauer, Kanti R. Rai, John C. Byrd, Barbara Eichhorst, Susan O’Brien, Tadeusz Robak, John F. Seymour, and Thomas J. Kipps. Iwcll guidelines for diagnosis, indications for treatment, response assessment, and supportive management of cll. Blood, 131 25:2745-2760, Jun 2018. URL: https://doi.org/10.1182/blood-2017-09-806398, doi:10.1182/blood-2017-09-806398. This article has 2326 citations and is from a highest quality peer-reviewed journal.

12. (shadman2023diagnosisandtreatment pages 12-13): Mazyar Shadman. Diagnosis and treatment of chronic lymphocytic leukemia: a review. JAMA, 329 11:918-932, Mar 2023. URL: https://doi.org/10.1001/jama.2023.1946, doi:10.1001/jama.2023.1946. This article has 270 citations.

13. (alsawaf2023transcriptomicprofilesand pages 1-2): Othman Al-Sawaf, Can Zhang, Hyun Yong Jin, Sandra Robrecht, Yoonha Choi, Sandhya Balasubramanian, Alex Kotak, Yi Meng Chang, Anna Maria Fink, Eugen Tausch, Christof Schneider, Matthias Ritgen, Karl-Anton Kreuzer, Brenda Chyla, Joseph N. Paulson, Christian P. Pallasch, Lukas P. Frenzel, Martin Peifer, Barbara Eichhorst, Stephan Stilgenbauer, Yanwen Jiang, Michael Hallek, and Kirsten Fischer. Transcriptomic profiles and 5-year results from the randomized cll14 study of venetoclax plus obinutuzumab versus chlorambucil plus obinutuzumab in chronic lymphocytic leukemia. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37648-w, doi:10.1038/s41467-023-37648-w. This article has 124 citations and is from a highest quality peer-reviewed journal.

14. (shah2024pirtobrutinibmonotherapyin pages 1-2): Nirav N. Shah, Michael Wang, Lindsey E. Roeker, Krish Patel, Jennifer A. Woyach, William G. Wierda, Chaitra S. Ujjani, Toby A. Eyre, Pier Luigi Z Inzani, Alvaro J. Alencar, Paolo Ghia, Nicole Lamanna, Marc S. Hoffmann, Manish R. Patel, Ian Flinn, James N. Gerson, Shuo Ma, Catherine C. Coombs, Chan Y. Cheah, Ewa Lech-Maranda, Bita Fakhri, Won Seog Kim, Minal A. Barve, Jonathon B. Cohen, Wojciech Jurczak, Talha Munir, Meghan C. Thompson, Donald E. Tsai, Katherine Bao, Nicholas A. Cangemi, Jennifer F. Kherani, Richard A. Walgren, Hongmei Han, Amy S. Ruppert, and Jennifer R. Brown. Pirtobrutinib monotherapy in bruton tyrosine kinase inhibitor-intolerant patients with b-cell malignancies: results of the phase i/ii bruin trial. Haematologica, 110:92-102, Oct 2024. URL: https://doi.org/10.3324/haematol.2024.285754, doi:10.3324/haematol.2024.285754. This article has 21 citations.

15. (shadman2023diagnosisandtreatment pages 4-5): Mazyar Shadman. Diagnosis and treatment of chronic lymphocytic leukemia: a review. JAMA, 329 11:918-932, Mar 2023. URL: https://doi.org/10.1001/jama.2023.1946, doi:10.1001/jama.2023.1946. This article has 270 citations.

16. (hallek2018iwcllguidelinesfor media 015ffd7a): Michael Hallek, Bruce D. Cheson, Daniel Catovsky, Federico Caligaris-Cappio, Guillermo Dighiero, Hartmut Döhner, Peter Hillmen, Michael Keating, Emili Montserrat, Nicholas Chiorazzi, Stephan Stilgenbauer, Kanti R. Rai, John C. Byrd, Barbara Eichhorst, Susan O’Brien, Tadeusz Robak, John F. Seymour, and Thomas J. Kipps. Iwcll guidelines for diagnosis, indications for treatment, response assessment, and supportive management of cll. Blood, 131 25:2745-2760, Jun 2018. URL: https://doi.org/10.1182/blood-2017-09-806398, doi:10.1182/blood-2017-09-806398. This article has 2326 citations and is from a highest quality peer-reviewed journal.

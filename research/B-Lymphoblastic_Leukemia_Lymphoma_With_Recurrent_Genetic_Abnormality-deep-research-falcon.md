---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T16:13:01.936081'
end_time: '2026-05-10T16:22:39.007989'
duration_seconds: 577.07
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: B-Lymphoblastic Leukemia/Lymphoma With Recurrent Genetic Abnormality
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** B-Lymphoblastic Leukemia/Lymphoma With Recurrent Genetic Abnormality
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **B-Lymphoblastic Leukemia/Lymphoma With Recurrent Genetic Abnormality** covering all of the
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
- **Disease Name:** B-Lymphoblastic Leukemia/Lymphoma With Recurrent Genetic Abnormality
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **B-Lymphoblastic Leukemia/Lymphoma With Recurrent Genetic Abnormality** covering all of the
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


# Comprehensive Research Report: B‑Lymphoblastic Leukemia/Lymphoma (B‑LBL/ALL) With Recurrent Genetic Abnormality

## Scope note
The user’s target entry corresponds to the modern WHO‑HAEM5 (WHO 2022/2023) and ICC (2022; published 2023) concept that **B‑lymphoblastic leukemia/lymphoma is best classified by recurrent genetic abnormalities** (“B‑ALL/LBL with recurrent genetic abnormalities”). The retrieved evidence set is strong for **classification, molecular subtypes, diagnostic genomics, MRD concepts, and some pediatric immunotherapy outcomes**, but is **incomplete for**: standardized ontology identifiers (MONDO/MeSH/ICD), full epidemiology incidence/prevalence, environmental risk factors, prevention, and animal model catalogs.

---

## 1. Disease Information

### 1.1 Definition and overview
**B‑lymphoblastic leukemia/lymphoma (B‑ALL/LBL)** is a precursor B‑cell neoplasm characterized by proliferation of lymphoblasts in bone marrow/blood (leukemia) and/or mass lesions (lymphoma). Contemporary classifications emphasize that **recurrent genetic abnormalities define biologically and clinically meaningful subtypes that drive risk stratification and, in select cases, targeted therapy**. This framing is explicit in both the ICC and recent WHO-aligned summaries emphasizing that childhood B‑ALL is “characterised by recurrent genetic abnormalities that drive risk‑directed treatment strategies.” (ryan2023wholegenomesequencing pages 1-2).

### 1.2 Classification context (WHO‑HAEM5 and ICC)
The **ICC** article on ALL/LBL (peer‑reviewed; Nov 2023; URL https://doi.org/10.1007/s00428-022-03448-8) outlines multiple recurrent genetic B‑ALL entities and explicitly subdivides BCR::ABL1‑like (Ph‑like) ALL into mechanistically actionable categories (ABL‑class vs JAK‑STAT–activated vs NOS) with corresponding diagnostic requirements (duffield2023internationalconsensusclassification pages 3-4, duffield2023internationalconsensusclassification pages 4-6).

A WHO‑HAEM5‑aligned review notes that WHO‑HAEM5 upgraded some 2017 “provisional” entities (e.g., BCR::ABL1‑like, iAMP21) and added newer types such as ETV6::RUNX1‑like and a category of “B‑ALL with other defined genetic features,” and recommends use of “B‑ALL/LBL, not further classified” when comprehensive genomic testing is not feasible (kansal2023diagnosisandmolecular pages 5-7).

### 1.3 Synonyms / alternative names
Commonly used names in the literature include:
- **B‑ALL**; **B‑cell acute lymphoblastic leukemia**
- **B‑LBL**; **B‑lymphoblastic lymphoma**
- **B‑lymphoblastic leukemia/lymphoma with recurrent genetic abnormalities** (ICC/WHO framing) (duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 5-7)

### 1.4 Key identifiers (ICD/MeSH/MONDO/Orphanet/OMIM)
Not determinable from the retrieved evidence set. The provided materials were not ontology/registry entries and did not list ICD‑10/11, MeSH, Orphanet, OMIM, or MONDO identifiers.

### 1.5 Evidence source type
The classification and mechanistic information here is derived from **aggregated disease‑level resources (WHO/ICC‑aligned reviews and consensus classifications)** and large cohort studies (e.g., WGS diagnostic validation; COG relapse analysis) rather than single‑patient EHR data (ryan2023wholegenomesequencing pages 1-2, rheingold2024determinantsofsurvival pages 2-3).

---

## 2. Etiology

### 2.1 Primary causal factors
The defining “causal factors” for this knowledge‑base entry are **recurrent genetic alterations** that initiate or sustain leukemogenesis (chromosomal aneuploidy, translocations/fusions, focal copy‑number changes, and subtype‑defining point mutations) (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 4-6, duffield2023internationalconsensusclassification pages 3-4).

### 2.2 Risk factors
**Germline predisposition / inherited risk**: In ICC, **low hypodiploid B‑ALL** is highlighted as frequently involving **TP53 mutations**, with an important clinical point that ~50% of pediatric TP53 mutations in this setting may be germline (Li‑Fraumeni syndrome implication) (duffield2023internationalconsensusclassification pages 3-4).

**Age-related risk**: Favorable genetic subtypes (high hyperdiploidy; ETV6::RUNX1) are common in childhood but become rare in older adults; an excerpt gives approximate distribution across age strata (kansal2023diagnosisandmolecular pages 7-8).

**Environmental/infectious risk factors**: Not supported by the retrieved evidence set.

### 2.3 Protective factors and gene–environment interactions
Not supported by the retrieved evidence set.

---

## 3. Phenotypes

### 3.1 Clinical presentation (general)
The retrieved evidence focuses on classification and diagnostics rather than detailed symptom prevalence. However, clinically relevant phenotypes documented include:
- **Bone marrow–dominant relapse** and **CNS relapse** patterns in pediatric ALL: isolated bone marrow relapse 58.7%; any bone marrow involvement 72.5%; isolated CNS relapse 21.7%; overall CNS involvement 32.9% (COG analysis) (rheingold2024determinantsofsurvival pages 2-3).

### 3.2 Age of onset
Childhood B‑ALL is dominated by specific favorable genetic subtypes; in one WHO‑aligned summary, ~90% of childhood ALL is B‑ALL and favorable subtypes contribute a large proportion of standard‑risk disease (kansal2023diagnosisandmolecular pages 5-7, kansal2023diagnosisandmolecular pages 7-8).

### 3.3 Suggested HPO terms (high-level; limited by evidence)
Because symptom-level data were not extracted in the current evidence set, only broad, high-confidence phenotype terms are suggested:
- **Abnormality of the bone marrow** (HP:0005560)
- **Leukemia** (HP:0001909)
- **Central nervous system involvement** (HP:0001310) — supported by CNS relapse frequency patterns (rheingold2024determinantsofsurvival pages 2-3)

---

## 4. Genetic / Molecular Information (core of this entity)

### 4.1 Current understanding: recurrent genetic subtypes
Modern WHO/ICC frameworks partition B‑ALL/LBL into multiple recurrent genetic subtypes; the ICC provides detailed diagnostic/prognostic notes for several recently recognized entities (DUX4‑r, ZNF384‑r, MEF2D‑r, NUTM1‑r, MYC‑r, CDX2/UBTF, HLF‑r), as well as single-gene mutant entities (PAX5 P80R; IKZF1 N159Y) (duffield2023internationalconsensusclassification pages 4-6, duffield2023internationalconsensusclassification pages 6-8).

A WHO‑aligned review highlights that WHO‑HAEM5 expanded the list beyond classic cytogenetic categories and that many new subtypes require advanced genomic methods (expression profiling, WGS, improved copy-number analysis) (kansal2023diagnosisandmolecular pages 5-7).

### 4.2 Subtype catalog (structured)
A structured table of major subtypes, frequencies (when available), prognosis notes, and detection methods is provided below.

| Subtype | Hallmark alteration | Typical age group | Approx. frequency | Prognosis notes | Recommended detection method |
|---|---|---|---|---|---|
| High hyperdiploidy | 51–65 chromosomes / high hyperdiploidy | Predominantly childhood; common pediatric subtype (kansal2023diagnosisandmolecular pages 7-8) | ~25–35% of B-ALL; ~30% in childhood cohorts (mahdaoui2025areviewof pages 2-3, ryan2023wholegenomesequencing pages 1-2) | Very favorable / excellent prognosis; long-term survival often >90% in summary review sources (mahdaoui2025areviewof pages 2-3, kansal2023diagnosisandmolecular pages 5-7) | Karyotype, copy-number analysis/WGS; standard cytogenetics generally sufficient (kansal2023diagnosisandmolecular pages 5-7, ryan2023wholegenomesequencing pages 1-2) |
| ETV6::RUNX1 | t(12;21)(p13;q22), ETV6::RUNX1 fusion | Childhood; often initiates in utero (kansal2023diagnosisandmolecular pages 7-8) | ~21–25% of childhood B-ALL (kansal2023diagnosisandmolecular pages 5-7, ryan2023wholegenomesequencing pages 1-2) | Favorable / excellent prognosis (kansal2023diagnosisandmolecular pages 5-7, kansal2023diagnosisandmolecular pages 7-8) | FISH, RT-PCR/RNA-based testing, WGS (kansal2023diagnosisandmolecular pages 5-7, ryan2023wholegenomesequencing pages 1-2) |
| BCR::ABL1 | t(9;22)(q34;q11.2), BCR::ABL1 fusion | More common in adults, also seen in children (kansal2023diagnosisandmolecular pages 5-7) | Not consistently stated in gathered evidence | Historically poor-risk, now therapeutically targetable with TKIs (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 3-4) | Karyotype, FISH, RT-PCR/RNA-seq, WGS (kansal2023diagnosisandmolecular pages 5-7, ryan2023wholegenomesequencing pages 1-2) |
| BCR::ABL1-like (Ph-like) | Kinase/cytokine receptor alterations; ABL-class, JAK-STAT, CRLF2, EPOR, FLT3/FGFR1/NTRK3/PTK2B lesions | Children, AYA, adults; clinically important across ages (duffield2023internationalconsensusclassification pages 3-4) | Not consistently stated in gathered evidence | Poor outcome; therapeutically relevant because ABL-class lesions may respond to TKIs (duffield2023internationalconsensusclassification pages 3-4, kansal2023diagnosisandmolecular pages 5-7) | GEP plus fusion/mutation testing; FISH for some lesions; targeted transcriptome sequencing/NGS; WGS (duffield2023internationalconsensusclassification pages 3-4, kansal2023diagnosisandmolecular pages 5-7, ryan2023wholegenomesequencing pages 1-2) |
| KMT2A-rearranged | KMT2A (MLL) rearrangements | Infant-predominant but also seen beyond infancy (kansal2023diagnosisandmolecular pages 5-7, kansal2023diagnosisandmolecular pages 15-16) | Not consistently stated in gathered evidence | Poor prognosis; clinically important and menin-pathway targeted therapy is emerging (kansal2023diagnosisandmolecular pages 5-7, kansal2023diagnosisandmolecular pages 15-16) | Karyotype/FISH for classic lesions; RNA-seq/NGS/WGS for comprehensive definition (kansal2023diagnosisandmolecular pages 5-7, kansal2023diagnosisandmolecular pages 15-16) |
| TCF3::PBX1 | t(1;19)(q23;p13), TCF3::PBX1 fusion | Mostly pediatric/AYA (ryan2023wholegenomesequencing pages 1-2) | ~5% in childhood cohorts (ryan2023wholegenomesequencing pages 1-2) | Recognized recurrent subtype; prognosis not explicitly quantified in gathered subtype summaries here (ryan2023wholegenomesequencing pages 1-2) | Karyotype, FISH, RT-PCR/RNA-seq, WGS (ryan2023wholegenomesequencing pages 1-2) |
| iAMP21 | Intrachromosomal amplification of chromosome 21 | Pediatric (kansal2023diagnosisandmolecular pages 5-7, kansal2023diagnosisandmolecular pages 15-16) | ~2% of pediatric B-ALL (mahdaoui2025areviewof pages 2-3, ryan2023wholegenomesequencing pages 1-2) | Upgraded to definite entity in WHO-HAEM5; adverse-risk subtype in modern classification context (kansal2023diagnosisandmolecular pages 5-7) | FISH/copy-number methods; WGS can detect; targeted RNA-seq alone may miss iAMP21 (ryan2023wholegenomesequencing pages 1-2) |
| Hypodiploid B-ALL | Low hypodiploid (32–39 chr) or near-haploid (24–31 chr); TP53/IKZF2 associations | Children and adults (duffield2023internationalconsensusclassification pages 3-4) | ~1% low hypodiploid and ~1% near-haploid in childhood cohort summary (ryan2023wholegenomesequencing pages 1-2) | Poor outcome; masked hypodiploidy is a diagnostic pitfall (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 3-4) | Karyotype plus SNP/copy-number analysis or WGS to detect masked hypodiploidy (duffield2023internationalconsensusclassification pages 3-4, ryan2023wholegenomesequencing pages 1-2) |
| DUX4-rearranged | DUX4 rearrangement, often IGH::DUX4; DUX4 overexpression | Relatively common in AYA; also pediatric (duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 15-16) | ~5–10% overall in ICC summary; ~4% pediatric B-ALL / ~16% of B-other (duffield2023internationalconsensusclassification pages 3-4, kansal2023diagnosisandmolecular pages 15-16) | Excellent/favorable prognosis despite high early MRD (duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 15-16) | RNA-seq/GEP, DUX4 RNA or protein overexpression, CD371 by flow; WGS may outperform transcriptome sequencing for some cases (duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 15-16, ryan2023wholegenomesequencing pages 1-2) |
| ZNF384-rearranged | ZNF384 rearrangements with multiple partners (e.g., EP300, TCF3, TAF15) | Children and young adults; also adults (duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 15-16) | ~5–10% overall; ~5% childhood and ~10% adult in summary sources (duffield2023internationalconsensusclassification pages 3-4, kansal2023diagnosisandmolecular pages 15-16) | Prognosis depends on fusion partner; may show lineage ambiguity / MPAL overlap (duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 15-16) | FISH break-apart, transcriptome sequencing/RNA-seq, genomic sequencing/WGS (duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 15-16) |
| MEF2D-rearranged | MEF2D rearrangement, commonly MEF2D::BCL9 | Children/young adults; median age around adolescence in some series (duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 15-16) | Small subset; ~5% of pediatric cases without other recurrent abnormalities (kansal2023diagnosisandmolecular pages 15-16) | Relatively poor prognosis (duffield2023internationalconsensusclassification pages 4-6) | Fusion probes/FISH, transcriptome sequencing/RNA-seq, NGS/WGS (duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 15-16) |
| NUTM1-rearranged | NUTM1 rearrangement | Infant-predominant (duffield2023internationalconsensusclassification pages 4-6) | Rare (duffield2023internationalconsensusclassification pages 4-6) | Favorable prognosis in available summaries (duffield2023internationalconsensusclassification pages 4-6) | NUTM1 FISH and NUT immunohistochemistry; RNA-seq/NGS may also define fusion (duffield2023internationalconsensusclassification pages 4-6) |
| MYC-rearranged | IG::MYC or other MYC rearrangement | More often adult B-ALL (duffield2023internationalconsensusclassification pages 4-6) | ~4% of adult B-ALL (duffield2023internationalconsensusclassification pages 4-6) | Very poor prognosis; distinction from mature B-cell lymphoma/Burkitt-type disease is essential (duffield2023internationalconsensusclassification pages 4-6) | FISH/karyotype; somatic hypermutation analysis and immunophenotype support distinction; RNA-seq/NGS may assist (duffield2023internationalconsensusclassification pages 4-6) |
| PAX5 P80R | PAX5 p.P80R point mutation | More common in adults (duffield2023internationalconsensusclassification pages 6-8) | ~2–5% of B-ALL (duffield2023internationalconsensusclassification pages 6-8) | Relatively good prognosis (duffield2023internationalconsensusclassification pages 6-8) | NGS for point mutation; broader genomic testing for associated lesions (duffield2023internationalconsensusclassification pages 6-8) |
| PAX5alt | Diverse PAX5 alterations / fusions / CNAs defining PAX5-altered subtype | Childhood and adults; many formerly “B-other” cases (kansal2023diagnosisandmolecular pages 15-16, ryan2023wholegenomesequencing pages 1-2) | ~7.5% in review summary (mahdaoui2025areviewof pages 2-3) | Intermediate outcomes in cohort/review summaries (duffield2023internationalconsensusclassification pages 6-8) | Integrated RNA-seq, copy-number analysis, NGS/WGS; expanded genomic profiling improves recognition (duffield2023internationalconsensusclassification pages 6-8, ryan2023wholegenomesequencing pages 1-2) |
| IKZF1 N159Y | IKZF1 N159Y point mutation | More common in adults (duffield2023internationalconsensusclassification pages 6-8) | <1% of cases (duffield2023internationalconsensusclassification pages 6-8) | Intermediate prognosis (duffield2023internationalconsensusclassification pages 6-8) | NGS for point mutation (duffield2023internationalconsensusclassification pages 6-8) |
| HLF-rearranged | TCF3::HLF or TCF4::HLF | Exceptionally rare, largely pediatric (duffield2023internationalconsensusclassification pages 4-6, duffield2023internationalconsensusclassification pages 6-8) | Exceptionally rare (duffield2023internationalconsensusclassification pages 6-8) | Very poor prognosis (duffield2023internationalconsensusclassification pages 4-6, duffield2023internationalconsensusclassification pages 6-8) | Fusion testing by FISH/RNA-seq/NGS; WGS can detect structural event (duffield2023internationalconsensusclassification pages 6-8, ryan2023wholegenomesequencing pages 1-2) |
| CDX2/UBTF | UBTF::ATXN7L3 fusion plus FLT3-upstream deletion causing CDX2 deregulation | Female adolescents and young adults (duffield2023internationalconsensusclassification pages 4-6, duffield2023internationalconsensusclassification pages 6-8) | Rare (duffield2023internationalconsensusclassification pages 4-6, duffield2023internationalconsensusclassification pages 6-8) | Poor prognosis (duffield2023internationalconsensusclassification pages 4-6, duffield2023internationalconsensusclassification pages 6-8) | Genomic structural testing with RNA-seq/WGS/NGS; specialized assays may be required (duffield2023internationalconsensusclassification pages 4-6, duffield2023internationalconsensusclassification pages 6-8) |
| ETV6::RUNX1-like | ETV6::RUNX1-like gene-expression profile without classic t(12;21) | Pediatric-predominant in modern profiling studies (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 6-8) | Not stated in gathered evidence | Newly added/provisional subtype in WHO-HAEM5/ICC context; prognosis not quantified here (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 6-8) | GEP/RNA-seq and comprehensive genomic profiling/WGS (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 6-8, ryan2023wholegenomesequencing pages 1-2) |


*Table: This table compacts the major recurrent genetic subtypes recognized in modern WHO-HAEM5/ICC-aligned B-lymphoblastic leukemia/lymphoma classification, using only the gathered evidence. It highlights subtype-defining lesions, age distribution, approximate frequencies, prognosis, and the molecular methods most useful for detection.*

### 4.3 Key subtype-specific highlights (examples)
- **BCR::ABL1‑like (Ph‑like) B‑ALL**: ICC subdivides into **ABL‑class rearranged** vs **JAK‑STAT–activated** vs **NOS**; ABL‑class lesions are clinically important because they may respond to ABL1‑targeting TKIs (imatinib, dasatinib), and detection may use FISH and targeted transcriptome sequencing, but definitive assignment requires genetic studies including gene expression and fusion/mutation testing (duffield2023internationalconsensusclassification pages 3-4).
- **DUX4‑rearranged B‑ALL**: ICC notes excellent prognosis and technical pitfalls (IGH::DUX4 can be missed by targeted sequencing/FISH); diagnosis can rely on DUX4 RNA/protein overexpression or CD371 by flow cytometry (duffield2023internationalconsensusclassification pages 4-6). WHO‑aligned summary notes favorable outcome despite high MRD and association with ERG alterations/IKZF1 deletions; NGS (RNA or DNA) is typically required (kansal2023diagnosisandmolecular pages 15-16).
- **Hypodiploid B‑ALL**: ICC distinguishes **near‑haploid** from **low hypodiploid** and emphasizes masked hypodiploidy; low hypodiploidy associates with TP53 mutations (with germline implication) (duffield2023internationalconsensusclassification pages 3-4).

### 4.4 Molecular diagnostic yield (WGS as a comprehensive test)
Whole genome sequencing (WGS) in a 210‑patient childhood B‑ALL cohort detected **294 subtype‑defining genetic abnormalities in 96% (202/210)** and showed concordance with standard-of-care methods and WTS, supporting WGS as a “standalone, reliable genetic test” for identifying subtype-defining abnormalities (Jan 2023; URL https://doi.org/10.1038/s41375-022-01806-8) (ryan2023wholegenomesequencing pages 1-2). A tightly cropped image of the paper’s subtype-frequency table is available (ryan2023wholegenomesequencing media 2101e72e).

---

## 5. Environmental Information
Not supported by the retrieved evidence set.

---

## 6. Mechanism / Pathophysiology

### 6.1 Conceptual model (current understanding)
Across subtypes, leukemogenesis generally follows a **driver-lesion → altered transcription/signaling → aberrant B‑cell precursor differentiation/proliferation → clinical leukemia/lymphoma** chain. ICC emphasizes pathway-based classes particularly for Ph‑like ALL, in which lesions activate **ABL‑class kinase signaling** or **JAK‑STAT signaling**, creating a rationale for targeted kinase inhibition (duffield2023internationalconsensusclassification pages 3-4).

### 6.2 Examples of subtype-linked mechanisms
- **ABL‑class rearranged Ph‑like ALL**: oncogenic ABL-family signaling; potential sensitivity to ABL1 TKIs (duffield2023internationalconsensusclassification pages 3-4).
- **JAK‑STAT–activated Ph‑like ALL**: lesions such as CRLF2 rearrangements, EPOR rearrangements, JAK fusions/mutations (duffield2023internationalconsensusclassification pages 3-4).
- **IKZF1 N159Y**: ICC notes abnormal nuclear localization and enhanced cell–cell adhesion phenotypes, consistent with a distinct biology compared with deletion-driven IKZF1 alterations (duffield2023internationalconsensusclassification pages 6-8).

### 6.3 Suggested ontology terms (high-level)
Because mechanistic detail in the retrieved evidence is subtype‑overview rather than pathway experiments, only broad mapping is suggested:
- GO: **B cell differentiation** (GO:0030183)
- GO: **JAK‑STAT cascade** (GO:0007259) (Ph‑like JAK‑STAT–activated group) (duffield2023internationalconsensusclassification pages 3-4)
- GO: **protein tyrosine kinase signaling pathway** (GO:0007169) (ABL‑class group) (duffield2023internationalconsensusclassification pages 3-4)
- CL: **B cell** (CL:0000236)
- CL: **B cell precursor** (CL:0000816) (conceptual target cell)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- **Bone marrow** is the principal disease compartment and the dominant site of relapse; in a large pediatric dataset, isolated bone marrow relapse accounted for 58.7%, and any bone marrow involvement for 72.5% (rheingold2024determinantsofsurvival pages 2-3).
- **Central nervous system** involvement is clinically important; isolated CNS relapse 21.7% and overall CNS involvement 32.9% at relapse in the same cohort (rheingold2024determinantsofsurvival pages 2-3).

### 7.2 Suggested UBERON terms
- Bone marrow: **UBERON:0002371**
- Central nervous system: **UBERON:0001016**

---

## 8. Temporal Development

### 8.1 Onset
The evidence set supports that favorable genetic subtypes are predominantly pediatric and may arise early (including prenatal initiation for ETV6::RUNX1 and high hyperdiploidy) (kansal2023diagnosisandmolecular pages 7-8).

### 8.2 Relapse timing patterns
In the COG analysis of 16,115 patients treated on 12 frontline trials, late relapse was common: ~50% of B‑ALL relapses occurred ≥36 months after diagnosis, and ~16% occurred >5 years (rheingold2024determinantsofsurvival pages 2-3). Relapse timing varies by subtype: ETV6::RUNX1 and trisomy 4+10 have later median time-to-relapse (~43 months), whereas hypodiploid and KMT2A‑rearranged relapse earlier (median ~12.5–18 months) (rheingold2024determinantsofsurvival pages 2-3).

---

## 9. Inheritance and Population

### 9.1 Population epidemiology
Incidence/prevalence estimates were not retrievable from the current evidence set.

### 9.2 Germline predisposition and inheritance
A clinically actionable inheritance-relevant point is the **potential germline origin of TP53 mutations** in low hypodiploid B‑ALL (Li‑Fraumeni syndrome context), highlighted by ICC (duffield2023internationalconsensusclassification pages 3-4).

---

## 10. Diagnostics

### 10.1 Diagnostic criteria and classification
The ICC emphasizes that accurate classification of B‑ALL with recurrent genetic abnormalities requires **genetic studies**, and some groups require **gene-expression profiling (GEP)** for assignment; CRLF2 rearrangement is one immunophenotypic clue for Ph‑like ALL but otherwise immunophenotypes may be non-distinctive (duffield2023internationalconsensusclassification pages 3-4, duffield2023internationalconsensusclassification pages 6-8).

### 10.2 Recommended testing modalities (current implementations)
**Cytogenetics/FISH/RT‑PCR** remain core for classic alterations, while **RNA‑seq, WGS, and broader NGS** increasingly enable complete assignment of emerging entities and “B‑other” cases (kansal2023diagnosisandmolecular pages 5-7, ryan2023wholegenomesequencing pages 1-2).

**WGS in diagnostics**: WGS can detect aneuploidies, structural variants, and focal copy-number changes and allocate many B‑other cases to emerging genomic groups; a WGS diagnostic feasibility study reported 100% concordance with standard-of-care and high yield for assigning emerging subgroups (concept supported in WHO‑aligned review; and WGS cohort data show 96% classification success) (ryan2023wholegenomesequencing pages 1-2, kansal2023diagnosisandmolecular pages 5-7).

### 10.3 Measurable residual disease (MRD)
The ELN 2024 adult ALL recommendations emphasize MRD’s central prognostic role and discuss standardization and validation initiatives for molecular/NGS-based MRD, including EuroClonality NGS standardization efforts and specific guidance for Ph+ ALL MRD by qRT‑PCR (Blood May 2024; URL https://doi.org/10.1182/blood.2023020794) (gokbuget2024diagnosisprognosticfactors pages 13-14).

In pediatric relapse analyses, MRD by COG flow cytometry had typical sensitivity 10−4, and end‑of‑induction MRD ≥0.01% was associated with increased relapse risk (p < 0.0001) (rheingold2024determinantsofsurvival pages 2-3).

### 10.4 Differential diagnosis
Not supported by the retrieved evidence set.

---

## 11. Outcome / Prognosis

### 11.1 Prognostic stratification by genetics
WHO/ICC-aligned summaries maintain classic prognostic groupings (favorable: high hyperdiploidy; ETV6::RUNX1; adverse: hypodiploidy; BCR::ABL1; KMT2A rearranged), while newly defined subtypes show distinct outcomes (e.g., DUX4‑r favorable; MEF2D‑r relatively poor) (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 4-6, kansal2023diagnosisandmolecular pages 15-16).

### 11.2 Post‑relapse survival and subtype-specific outcomes (pediatric)
A large COG analysis reported 2053 relapses among 16,115 pediatric patients (12.7%); the **5‑year OS post‑relapse** was **48.9 ± 1.2%** overall and **52.5 ± 1.3% for B‑ALL**. The abstract also reports cytogenetic‑specific post‑relapse OS: **ETV6::RUNX1 74.4 ± 3.1%**, **Trisomy 4+10 70.2 ± 3.6%**, versus poor outcomes for **hypodiploidy 14.2 ± 6.1%**, **KMT2A‑rearranged 31.9 ± 7.7%**, and **TCF3::PBX1 36.8 ± 6.6%** (Sep 2024; URL https://doi.org/10.1038/s41375-024-02395-4) (rheingold2024determinantsofsurvival pages 2-3).

**Direct abstract quote (COG relapse study):** “The 5-year OS post-relapse for the entire cohort was 48.9 ± 1.2%; B-ALL:52.5 ± 1.3%…” and “Patients with hypodiploidy, KMT2A-rearrangement, and TCF3::PBX1 had short median time-to-relapse (12.5-18 months) and poor OS post-relapse (14.2 ± 6.1%, 31.9 ± 7.7%, 36.8 ± 6.6%).” (rheingold2024determinantsofsurvival pages 2-3).

---

## 12. Treatment

### 12.1 Current applications and real-world implementations (selected)

#### 12.1.1 Blinatumomab (CD19×CD3 BiTE)
A 2024 pediatric immunotherapy review summarizes multiple use-cases and randomized relapse settings:
- In early single-agent studies at RP2D, **overall response rate 39%**, and **52% of responders achieved MRD negativity** (brivio2024nakedantibodiesand pages 3-4).
- In randomized pediatric first marrow relapse settings, post‑reinduction blinatumomab improved **2‑year DFS 54.4% vs 39.0%** versus chemotherapy and improved **2‑year EFS 66.2% vs 27.1%** in high‑risk first relapse BCP‑ALL (brivio2024nakedantibodiesand pages 3-4).
- For bone marrow relapses, blinatumomab produced superior **4‑year DFS/OS 72.7%/97.1%** vs chemotherapy **53.7%/84.8%**; outcomes were similarly poor for isolated extramedullary relapse (4‑year DFS ~36–39%) (brivio2024nakedantibodiesand pages 3-4).

**Direct abstract quote (review):** “With the novel therapeutic options introduced in the last years, including immunotherapies and targeted antibodies, the treatment of ALL is undergoing major changes.” (Haematologica May 2024 review; abstract statement) (brivio2024nakedantibodiesand pages 3-4).

#### 12.1.2 Targeted therapy linkage (genotype → therapy)
ICC explicitly connects **ABL‑class Ph‑like lesions** (ABL1/ABL2/CSF1R/PDGFRB fusions) to potential responsiveness to **ABL1-targeting TKIs** and indicates that identifying these lesions is clinically actionable (duffield2023internationalconsensusclassification pages 3-4).

### 12.2 Treatment strategy and expert opinion (authoritative sources)
The ELN 2024 adult recommendations are an authoritative expert-panel source emphasizing that adult ALL management requires **comprehensive biologic characterization and MRD-driven risk stratification**, with MRD methodology standardization and genomic high-risk groups (e.g., Ph-like ALL, IKZF1 deletions) considered in risk assessment (gokbuget2024diagnosisprognosticfactors pages 13-14).

### 12.3 Suggested MAXO terms (high level)
- **Chemotherapy** (MAXO:0000058)
- **Tyrosine kinase inhibitor therapy** (for ABL‑class or BCR::ABL1‑positive disease) (duffield2023internationalconsensusclassification pages 3-4)
- **Blinatumomab therapy / bispecific antibody therapy** (MAXO term depends on local MAXO implementation) (brivio2024nakedantibodiesand pages 3-4)
- **Measurable residual disease monitoring** (diagnostic action; MAXO not always used for monitoring)

---

## 13. Prevention
Not supported by the retrieved evidence set.

---

## 14. Other Species / Natural Disease
Not supported by the retrieved evidence set.

---

## 15. Model Organisms
Not supported by the retrieved evidence set.

---

# High-value, recent sources used (with dates and URLs)
- Duffield AS, Mullighan CG, Borowitz MJ. **International consensus classification of acute lymphoblastic leukemia/lymphoma.** Virchows Archiv. **Nov 2023.** https://doi.org/10.1007/s00428-022-03448-8 (duffield2023internationalconsensusclassification pages 4-6, duffield2023internationalconsensusclassification pages 3-4, duffield2023internationalconsensusclassification pages 6-8)
- Ryan S et al. **Whole genome sequencing provides comprehensive genetic testing in childhood B‑cell acute lymphoblastic leukaemia.** Leukemia. **Jan 2023.** https://doi.org/10.1038/s41375-022-01806-8 (ryan2023wholegenomesequencing pages 1-2, ryan2023wholegenomesequencing media 2101e72e)
- Gökbuget N et al. **Diagnosis, prognostic factors, and assessment of ALL in adults: 2024 ELN recommendations.** Blood. **May 2024.** https://doi.org/10.1182/blood.2023020794 (gokbuget2024diagnosisprognosticfactors pages 13-14)
- Rheingold SR et al. **Determinants of survival after first relapse of ALL: a COG study.** Leukemia. **Sep 2024.** https://doi.org/10.1038/s41375-024-02395-4 (rheingold2024determinantsofsurvival pages 2-3)
- Brivio E et al. **Naked antibodies and antibody‑drug conjugates: targeted therapy for childhood ALL.** Haematologica. **May 2024.** https://doi.org/10.3324/haematol.2023.283815 (brivio2024nakedantibodiesand pages 3-4)

---

## Limitations of this report (evidence gaps)
1) Standard ontology identifiers (MONDO/MeSH/ICD/Orphanet/OMIM) were not present in the retrieved sources.
2) Environmental risk factors, prevention strategies, and gene–environment interaction evidence were not retrieved.
3) Model organism and other-species data were not retrieved.
4) Several clinically important modern outcomes (e.g., adult frontline chemo‑immunotherapy, inotuzumab and CAR‑T quantitative outcomes, and population incidence/prevalence) require additional targeted retrieval beyond the present evidence set.


References

1. (ryan2023wholegenomesequencing pages 1-2): Sarra Ryan, John Peden, Zoya Kingsbury, Claire Schwab, Terena James, Petri Polonen, Martina Mijuskovic, Jennifer Becq, Richard Yim, Ruth Cranston, Dale Hedges, Kathryn Roberts, Charles Mullighan, Ajay Vora, Lisa Russell, Anthony Moorman, David Bentley, Christine Harrison, and Mark Ross. Whole genome sequencing provides comprehensive genetic testing in childhood b-cell acute lymphoblastic leukaemia. Leukemia, 37:518-528, Jan 2023. URL: https://doi.org/10.1038/s41375-022-01806-8, doi:10.1038/s41375-022-01806-8. This article has 89 citations and is from a highest quality peer-reviewed journal.

2. (duffield2023internationalconsensusclassification pages 3-4): Amy S. Duffield, Charles G. Mullighan, and Michael J. Borowitz. International consensus classification of acute lymphoblastic leukemia/lymphoma. Virchows Archiv, 482:11-26, Nov 2023. URL: https://doi.org/10.1007/s00428-022-03448-8, doi:10.1007/s00428-022-03448-8. This article has 226 citations and is from a peer-reviewed journal.

3. (duffield2023internationalconsensusclassification pages 4-6): Amy S. Duffield, Charles G. Mullighan, and Michael J. Borowitz. International consensus classification of acute lymphoblastic leukemia/lymphoma. Virchows Archiv, 482:11-26, Nov 2023. URL: https://doi.org/10.1007/s00428-022-03448-8, doi:10.1007/s00428-022-03448-8. This article has 226 citations and is from a peer-reviewed journal.

4. (kansal2023diagnosisandmolecular pages 5-7): Rina Kansal. Diagnosis and molecular pathology of lymphoblastic leukemias and lymphomas in the era of genomics and precision medicine: historical evolution and current concepts—part 2: b-/t-cell acute lymphoblastic leukemias. Lymphatics, 1:118-154, Jul 2023. URL: https://doi.org/10.3390/lymphatics1020011, doi:10.3390/lymphatics1020011. This article has 12 citations.

5. (rheingold2024determinantsofsurvival pages 2-3): Susan R. Rheingold, Deepa Bhojwani, Lingyun Ji, Xinxin Xu, Meenakshi Devidas, John A. Kairalla, Mary Shago, Nyla A. Heerema, Andrew J. Carroll, Heather Breidenbach, Michael Borowitz, Brent L. Wood, Anne L. Angiolillo, Barbara L. Asselin, W. Paul Bowman, Patrick Brown, ZoAnn E. Dreyer, Kimberly P. Dunsmore, Joanne M. Hilden, Eric Larsen, Kelly Maloney, Yousif Matloub, Leonard A. Mattano, Stuart S. Winter, Lia Gore, Naomi J. Winick, William L. Carroll, Stephen P. Hunger, Elizabeth A. Raetz, and Mignon L. Loh. Determinants of survival after first relapse of acute lymphoblastic leukemia: a children’s oncology group study. Leukemia, 38:2382-2394, Sep 2024. URL: https://doi.org/10.1038/s41375-024-02395-4, doi:10.1038/s41375-024-02395-4. This article has 81 citations and is from a highest quality peer-reviewed journal.

6. (kansal2023diagnosisandmolecular pages 7-8): Rina Kansal. Diagnosis and molecular pathology of lymphoblastic leukemias and lymphomas in the era of genomics and precision medicine: historical evolution and current concepts—part 2: b-/t-cell acute lymphoblastic leukemias. Lymphatics, 1:118-154, Jul 2023. URL: https://doi.org/10.3390/lymphatics1020011, doi:10.3390/lymphatics1020011. This article has 12 citations.

7. (duffield2023internationalconsensusclassification pages 6-8): Amy S. Duffield, Charles G. Mullighan, and Michael J. Borowitz. International consensus classification of acute lymphoblastic leukemia/lymphoma. Virchows Archiv, 482:11-26, Nov 2023. URL: https://doi.org/10.1007/s00428-022-03448-8, doi:10.1007/s00428-022-03448-8. This article has 226 citations and is from a peer-reviewed journal.

8. (mahdaoui2025areviewof pages 2-3): Chaimae EL MAHDAOUI, Hind Dehbi, and Siham Cherkaoui. A review of the latest updates in cytogenetic and molecular classification and emerging approaches in identifying abnormalities in acute lymphoblastic leukemia. Lymphatics, Aug 2025. URL: https://doi.org/10.3390/lymphatics3030023, doi:10.3390/lymphatics3030023. This article has 1 citations.

9. (kansal2023diagnosisandmolecular pages 15-16): Rina Kansal. Diagnosis and molecular pathology of lymphoblastic leukemias and lymphomas in the era of genomics and precision medicine: historical evolution and current concepts—part 2: b-/t-cell acute lymphoblastic leukemias. Lymphatics, 1:118-154, Jul 2023. URL: https://doi.org/10.3390/lymphatics1020011, doi:10.3390/lymphatics1020011. This article has 12 citations.

10. (ryan2023wholegenomesequencing media 2101e72e): Sarra Ryan, John Peden, Zoya Kingsbury, Claire Schwab, Terena James, Petri Polonen, Martina Mijuskovic, Jennifer Becq, Richard Yim, Ruth Cranston, Dale Hedges, Kathryn Roberts, Charles Mullighan, Ajay Vora, Lisa Russell, Anthony Moorman, David Bentley, Christine Harrison, and Mark Ross. Whole genome sequencing provides comprehensive genetic testing in childhood b-cell acute lymphoblastic leukaemia. Leukemia, 37:518-528, Jan 2023. URL: https://doi.org/10.1038/s41375-022-01806-8, doi:10.1038/s41375-022-01806-8. This article has 89 citations and is from a highest quality peer-reviewed journal.

11. (gokbuget2024diagnosisprognosticfactors pages 13-14): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Diagnosis, prognostic factors, and assessment of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1891-1902, May 2024. URL: https://doi.org/10.1182/blood.2023020794, doi:10.1182/blood.2023020794. This article has 99 citations and is from a highest quality peer-reviewed journal.

12. (brivio2024nakedantibodiesand pages 3-4): Erica Brivio, Francisco Bautista, and C. Michel Zwaan. Naked antibodies and antibody-drug conjugates: targeted therapy for childhood acute lymphoblastic leukemia. Haematologica, 109:1700-1712, May 2024. URL: https://doi.org/10.3324/haematol.2023.283815, doi:10.3324/haematol.2023.283815. This article has 19 citations.
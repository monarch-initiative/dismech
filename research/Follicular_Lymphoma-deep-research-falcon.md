---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T16:18:48.913971'
end_time: '2026-05-08T16:36:36.871015'
duration_seconds: 1067.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Follicular Lymphoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Follicular Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Follicular Lymphoma** covering all of the
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
- **Disease Name:** Follicular Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Follicular Lymphoma** covering all of the
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


# Follicular Lymphoma (FL): Disease Characteristics Research Report (2023–2024 prioritized)

## Target Disease
- **Disease name:** Follicular lymphoma (FL)
- **MONDO ID:** Not found in the retrieved sources (requires lookup in MONDO/OLS; not present in the accessed literature excerpts).
- **Category:** Indolent mature B‑cell non‑Hodgkin lymphoma; germinal center (GC) B‑cell–derived neoplasm (xu2023advancesinthe pages 1-2, zinzani2024currentandfuture pages 1-2).

---

## 1. Disease Information

### Concise overview (current understanding)
Follicular lymphoma is an indolent, GC B‑cell–derived lymphoid neoplasm characterized by a follicular (nodular) architecture composed of centrocytes and centroblasts, typically presenting with diffuse lymphadenopathy and frequent bone marrow involvement, with a long relapsing–remitting course (jacobsen2022follicularlymphoma2023 pages 1-2, xu2023advancesinthe pages 1-2, kurz2023follicularlymphomain pages 2-4).

**Abstract quote (definition/heterogeneity):** “Follicular lymphoma (FL) is the most common indolent lymphoma originating from germinal center B cells. FL represents a clinically and biologically heterogeneous disease.” (Xu et al., published 2023‑03‑27; doi:10.7150/ijbs.80401) (xu2023advancesinthe pages 1-2).

### Key identifiers (available in retrieved sources)
- **ICD‑9‑CM:** **202.0** (used to identify FL in an Italian administrative-database real‑world evidence study) (Ferreri et al., published 2023‑09‑02; doi:10.3390/cancers15174403) (ferreri2023burdenofillness pages 2-3).
- **ICD‑10/ICD‑11, MeSH, Orphanet, MONDO:** Not explicitly provided in the retrieved texts; these require direct database queries (OMIM/Orphanet/MeSH/MONDO/ICD) outside the accessed excerpts.

### Synonyms / alternative names (from classification context)
- **Classic follicular lymphoma (cFL)** (WHO‑HAEM5 term encompassing prior FL grades 1–2–3A) (Kurz et al., 2023‑01; doi:10.3390/cancers15030785) (kurz2023follicularlymphomain pages 2-4, kurz2023follicularlymphomain pages 4-6).
- **Follicular large B‑cell lymphoma (FLBCL)** (WHO‑HAEM5 term replacing former grade 3B FL) (kurz2023follicularlymphomain pages 1-2, laurent2023follicularlymphomaand pages 1-2).
- **BCL2‑rearrangement–negative, CD23‑positive follicle center lymphoma** (ICC provisional entity; overlaps with predominantly diffuse FL) (kurz2023follicularlymphomain pages 8-10, chadburn2023classificationofbcell pages 2-5, laurent2023follicularlymphomaand pages 1-2).

### Evidence sources (patient-level vs aggregated)
The report draws from both **aggregated disease-level resources** (WHO‑HAEM5/ICC classification reviews; multi‑omics review; therapy landscape reviews) and **patient-level cohorts/registries** including SEER registry analyses and administrative real‑world evidence (RWE) datasets (kurz2023follicularlymphomain pages 1-2, xu2023advancesinthe pages 1-2, vaughn2023survivalofpatients pages 1-2, ferreri2023burdenofillness pages 1-2).

---

## 2. Etiology

### Disease causal factors (mechanistic)
FL pathogenesis is widely described as a **multistep process** where an initiating lesion (often IGH::BCL2 t(14;18)) provides a survival advantage, followed by accumulation of additional genetic/epigenetic and microenvironment‑mediated events (xu2023advancesinthe pages 1-2, kurz2023follicularlymphomain pages 4-6).

### Genetic risk factors (susceptibility)
The retrieved sources note **familial aggregation**: “The incidence is slightly increased among relatives of persons with FL.” (Jacobsen, 2022‑10; doi:10.1002/ajh.26737) (jacobsen2022follicularlymphoma2023 pages 1-2).

No GWAS loci or germline pathogenic variants were captured in the retrieved excerpts; these would require dedicated searches (GWAS Catalog/ClinVar/ClinGen).

### Environmental / infectious risk factors
No validated environmental or infectious *causal* factors for FL were provided in the retrieved excerpts. (Some literature exists for pesticides/immune dysregulation, but it was not accessible in the current evidence set.)

### Protective factors / gene–environment interactions
Not identified in the retrieved evidence.

---

## 3. Phenotypes (clinical features)

### Common presentation and manifestations
- **Lymphadenopathy** and often **bone marrow involvement**; **splenomegaly** is also common (jacobsen2022follicularlymphoma2023 pages 1-2, kurz2023follicularlymphomain pages 2-4).
- **Cytopenias** can occur, while classic “B symptoms” are less common **unless transformation occurs** (as summarized in Jacobsen’s clinical overview) (jacobsen2022follicularlymphoma2023 pages 1-2).
- **Transformation to DLBCL** can present with rapid progression of lymphadenopathy, extranodal disease, B symptoms, hypercalcemia, and elevated LDH (jacobsen2022follicularlymphoma2023 pages 1-2).

### Temporal features
- Typical diagnosis in older adults: **median age ~65 years** (jacobsen2022follicularlymphoma2023 pages 1-2).
- Transformation risk reported as about **2% per year** in classification and clinical updates (jacobsen2022follicularlymphoma2023 pages 1-2, kurz2023follicularlymphomain pages 2-4).

### Quality of life (QoL) impact (real-world data)
In an international RWE survey using **EORTC QLQ‑C30**, QoL worsened with later lines of therapy (LOT): mean global health status/QoL declined from **56.5** in 1L to **50.4** in 3L+ (Johnson et al., received 2024‑02‑23; published online 2024‑07‑08; doi:10.1007/s12325-024-02882-1) (johnson2024qualityoflife pages 1-2).

### Suggested HPO terms (non-exhaustive; mapped to evidence above)
- **Lymphadenopathy** (HP:0002716)
- **Splenomegaly** (HP:0001744)
- **Bone marrow infiltration** (HP:0005528) / **Abnormal bone marrow morphology** (HP:0005560)
- **Cytopenia** (HP:0001875) (use specific: anemia HP:0001903, thrombocytopenia HP:0001873, neutropenia HP:0001875)
- **Fever** (HP:0001945), **Night sweats** (HP:0030156), **Weight loss** (HP:0001824) — especially in transformation context
- **Elevated LDH** (HP:0003077)

(Frequency estimates for specific phenotypes were not captured in the retrieved excerpts.)

---

## 4. Genetic / Molecular Information

### Core disease-defining lesion
**IGH::BCL2 t(14;18)(q32;q21)** is the molecular hallmark of classic FL and is described as the initiating event in most cases (xu2023advancesinthe pages 1-2, kurz2023follicularlymphomain pages 4-6, zinzani2024currentandfuture pages 1-2).

### Recurrent somatic alterations (multi-omics/genomics)
High-frequency events involve **epigenetic modifiers** and immune–microenvironment modulators; examples include **KMT2D**, **CREBBP**, **EZH2**, **EP300**, and **TNFRSF14** (xu2023advancesinthe pages 1-2, kurz2023follicularlymphomain pages 4-6).

### Variant biology (t(14;18)-negative, CD23+/STAT6)
WHO‑HAEM5 and ICC recognize variant subtypes, including a predominantly diffuse pattern often **t(14;18)-negative**, frequently **CD23‑associated**, and enriched for **STAT6** mutations and 1p36 alterations involving **TNFRSF14** (kurz2023follicularlymphomain pages 1-2, kurz2023follicularlymphomain pages 8-10, chadburn2023classificationofbcell pages 2-5).

### Somatic vs germline
The alterations summarized here are described in the literature as **somatic** tumor events; germline predisposition variants were not provided in the retrieved excerpts.

### Artifact: consolidated alteration table
The following table is structured for direct knowledge-base ingestion.

| Alteration/Gene (HGNC symbol) | Type (translocation/mutation/CNA/epigenetic) | Approx frequency (with range) | Functional role/pathway | Clinical relevance (diagnostic/prognostic/therapeutic) | Notes on subtype specificity (classic FL vs predominantly diffuse/CD23+ STAT6-mut, transformation) | Key supporting sources (include DOI and year) |
|---|---|---|---|---|---|---|
| **IGH::BCL2** / **t(14;18)(q32;q21)** | Translocation | ~65–90%; ~85% in classic FL | Deregulated **BCL2** anti-apoptotic signaling; founding lesion in germinal-center B cells | Hallmark diagnostic lesion for classic FL; helps distinguish classic FL from several t(14;18)-negative variants; biologic rationale for FL pathogenesis | Enriched in classic FL; usually absent in predominantly diffuse/CD23+ FL and other t(14;18)-negative variants; present in ISFN; pre-existing BCL2 translocation constrains some transformed aggressive lymphomas | Xu 2023 doi:10.7150/ijbs.80401; Kurz 2023 doi:10.3390/cancers15030785; Jacobsen 2022 doi:10.1002/ajh.26737 (xu2023advancesinthe pages 1-2, kurz2023follicularlymphomain pages 2-4, kurz2023follicularlymphomain pages 4-6, jacobsen2022follicularlymphoma2023 pages 1-2) |
| **BCL2** | Mutation / overexpression | Mutated ~40% in one genomic cohort; protein expression ~80–90% in classic FL | Anti-apoptotic mitochondrial pathway | Diagnostic support via BCL2 protein expression in classic FL; central pathogenic driver; potential relevance to therapy resistance biology | Strong expression typical of classic FL; lower expression in FLBCL/former grade 3B; predominantly diffuse FL can be BCL2+ despite lacking IGH::BCL2 | Mozas 2023 doi:10.1002/hon.3132; Kurz 2023 doi:10.3390/cancers15030785 (kurz2023follicularlymphomain pages 4-6, kurz2023follicularlymphomain pages 8-10) |
| **KMT2D** | Mutation (epigenetic modifier) | ~70–90%; 79% in one cohort | Histone methylation/chromatin regulation in GC B cells | Very early driver lesion; part of core FL genomic profile; potential biomarker for clonal origin and early detection/monitoring | Common in classic FL and early precursor cells; identified as an early stable event longitudinally; also implicated in transformed/aggressive evolution broadly but not specific for diffuse/CD23+ subtype | Xu 2023 doi:10.7150/ijbs.80401; Mozas 2023 doi:10.1002/hon.3132; Bai 2024 doi:10.1038/s41408-024-01124-5; Friedberg 2023 doi:10.1002/hon.3138 (xu2023advancesinthe pages 1-2, kurz2023follicularlymphomain pages 4-6, friedberg2023updateonfollicular pages 1-3) |
| **CREBBP** | Mutation / loss-of-function (epigenetic modifier) | ~50–70%; 67% in one cohort | Histone acetylation/transcriptional control; epigenetic regulation and immune interaction | Very early driver lesion; part of core FL genomic profile; mechanistically linked to pathogenesis and risk stratification research | Common in classic FL and precursor cells; also frequent in t(14;18)-negative predominantly diffuse/CD23+ FL; longitudinal data identify it as an early event, with KAT-domain-mutant cases showing lower transformation risk in one 2024 study | Xu 2023 doi:10.7150/ijbs.80401; Mozas 2023 doi:10.1002/hon.3132; Bai 2024 doi:10.1038/s41408-024-01124-5; Kurz 2023 doi:10.3390/cancers15030785 (xu2023advancesinthe pages 1-2, kurz2023follicularlymphomain pages 4-6, kurz2023follicularlymphomain pages 8-10) |
| **EZH2** | Gain-of-function mutation (epigenetic modifier) | ~20–30%; ~25% often cited | PRC2/H3K27 methylation; germinal-center epigenetic program | Therapeutically actionable: basis for **tazemetostat** use; core FL biology and biomarker testing in relapsed disease | Seen in classic FL; EZH2-mutant tumors show altered histone gene expression/H3K27me3 patterns; not a defining lesion of diffuse/CD23+ STAT6-mut subtype | Xu 2023 doi:10.7150/ijbs.80401; Romero 2024 doi:10.1038/s41467-024-47701-x; Friedberg 2023 doi:10.1002/hon.3138; Zinzani 2024 doi:10.1186/s40164-024-00551-1 (xu2023advancesinthe pages 1-2, friedberg2023updateonfollicular pages 1-3, zinzani2024currentandfuture pages 1-2) |
| **EP300** | Mutation (epigenetic modifier) | ~20–30% | Histone acetylation/co-activator function | Recurrent lesion supporting epigenetic dysregulation model; potential future therapeutic relevance | Present across classic FL; may occur in common precursor cells; not highlighted as subtype-defining for diffuse/CD23+ disease in gathered evidence | Xu 2023 doi:10.7150/ijbs.80401; Bai 2024 doi:10.1038/s41408-024-01124-5 (xu2023advancesinthe pages 1-2) |
| **TNFRSF14** | Mutation / 1p36 loss-associated lesion | ~46% altered in one cohort | Microenvironment modulation / immune-stromal interaction | Recurrent early lesion; may inform biology of FL–microenvironment crosstalk and subtype assignment | Common in classic FL precursor cells; particularly relevant in t(14;18)-negative predominantly diffuse/CD23+ FL where 1p36 deletion/TNFRSF14 alteration is characteristic | Mozas 2023 doi:10.1002/hon.3132; Kurz 2023 doi:10.3390/cancers15030785 (kurz2023follicularlymphomain pages 4-6, kurz2023follicularlymphomain pages 8-10, kurz2023follicularlymphomain pages 1-2) |
| **STAT6** | Mutation | Frequent in t(14;18)-negative CD23+ diffuse FL; exact range not uniformly given in gathered evidence | JAK/STAT signaling; linked to nuclear phospho-STAT6 and anti-apoptotic targets such as **BCL2L1/BCL-xL** | Useful subtype-defining biomarker for BCL2-rearrangement-negative, CD23-positive follicle center lymphoma / predominantly diffuse FL | Characteristic of predominantly diffuse inguinal-region, CD23+ FL; more frequent in BCL2-negative / t(14;18)-negative variants than classic FL | Kurz 2023 doi:10.3390/cancers15030785; Chadburn 2023 doi:10.3390/hemato4010003; Laurent 2023 doi:10.1007/s00428-022-03432-2 (kurz2023follicularlymphomain pages 8-10, kurz2023follicularlymphomain pages 1-2, chadburn2023classificationofbcell pages 2-5, laurent2023follicularlymphomaand pages 1-2) |
| **1p36 deletion / CN-LOH** | Copy-number alteration | Recurrent; exact overall frequency not uniform, but highlighted as characteristic in diffuse FL | Often spans **TNFRSF14**; contributes to immune/microenvironment dysregulation | Helpful in subtype recognition for predominantly diffuse/t(14;18)-negative FL; may have prognostic implications in variant disease | Characteristic of predominantly diffuse/CD23+ STAT6-mut FL; less emphasized as defining lesion in classic FL | Kurz 2023 doi:10.3390/cancers15030785 (kurz2023follicularlymphomain pages 8-10, kurz2023follicularlymphomain pages 1-2, kurz2023follicularlymphomain pages 4-6) |
| **16p13 loss / CN-LOH** | Copy-number alteration | Recurrent in diffuse FL; no uniform cohort-wide percentage in gathered evidence | Region includes **CREBBP**, **CIITA**, **SOCS1**; epigenetic and immune-regulatory consequences | Supports molecular classification of t(14;18)-negative predominantly diffuse FL | Highlighted in predominantly diffuse/CD23+ FL rather than classic FL | Kurz 2023 doi:10.3390/cancers15030785 (kurz2023follicularlymphomain pages 8-10) |
| **Chromosome 18q21 gain / chromosome 18 gain** | Copy-number alteration | 14% localized FL vs 36% systemic FL in one study; chromosome 18 gain identified as early stable event in longitudinal series | May increase dosage of 18q genes including **BCL2/TCF4**-region–related drivers | Potential prognostic marker; 18q21 gains associated with inferior PFS in localized FL | More frequent in systemic than localized FL; early stable CNA in disease evolution | Ott 2023 doi:10.21203/rs.3.rs-3073791/v1; Bai 2024 doi:10.1038/s41408-024-01124-5 (xu2023advancesinthe pages 1-2) |
| **6q loss** | Copy-number alteration | Recurrent early stable CNA; exact frequency not uniform in gathered evidence | Tumor-suppressor region loss | Candidate marker of early clonal architecture and disease monitoring | Early and stable across longitudinal FL evolution; not specifically subtype-restricted in gathered evidence | Bai 2024 doi:10.1038/s41408-024-01124-5 (xu2023advancesinthe pages 1-2) |
| **BCL6** rearrangement | Translocation | ~10–20% in classic FL; ~20% MYC translocations noted in FLBCL, not BCL6 | Germinal-center transcriptional control | Supports molecular heterogeneity; may complicate differential diagnosis with aggressive B-cell lymphomas | Present in subset of classic FL; variant/transformed cases may carry additional aggressive-genotype features | Kurz 2023 doi:10.3390/cancers15030785 (kurz2023follicularlymphomain pages 4-6) |
| **ARID1A** | Mutation | 29% systemic FL vs 6% localized FL in one 2023 study | Chromatin remodeling (SWI/SNF) | Candidate marker of systemic disease biology; may relate to more advanced disease state | Enriched in systemic vs localized FL; not a classic hallmark but useful for biologic stratification | Ott 2023 doi:10.21203/rs.3.rs-3073791/v1 (xu2023advancesinthe pages 1-2) |
| **FOXO1 / PIM1 / TMEM30A** | Mutations | Adverse-behavior associations reported in small cohort; no stable population frequency established | Signaling, proliferation, membrane biology | Possible adverse prognostic markers, but evidence remains preliminary | Associated with early relapse/POD24 or refractory behavior in a small genomic study; not yet established as subtype-defining | Mozas 2023 doi:10.1002/hon.3132 (xu2023advancesinthe pages 1-2) |
| **CARD11 / CD79B** | Mutations | Recurrent but lower-frequency; exact range not uniform in gathered evidence | B-cell receptor/NF-κB signaling | Support activation of oncogenic signaling pathways; potential future targeted-therapy relevance | Part of broader signaling lesions in FL; not emphasized as variant-specific in gathered evidence | Xu 2023 doi:10.7150/ijbs.80401 (xu2023advancesinthe pages 1-2) |
| **IGHV N-glycosylation motif acquisition** | Somatic hypermutation-related molecular feature | ~80% | Promotes microenvironmental interactions and B-cell receptor biology | Pathobiologic hallmark rather than routine diagnostic biomarker; may help explain dependence on microenvironment | Associated mainly with classic FL biology and germinal-center origin | Xu 2023 doi:10.7150/ijbs.80401; Kurz 2023 doi:10.3390/cancers15030785 (xu2023advancesinthe pages 1-2, kurz2023follicularlymphomain pages 2-4) |


*Table: This table summarizes the principal genomic and molecular abnormalities reported for follicular lymphoma in the gathered evidence, including frequencies, pathways, clinical relevance, and subtype specificity. It is designed for direct use in a disease knowledge base and emphasizes distinctions between classic FL and t(14;18)-negative diffuse/CD23+/STAT6-mutant variants.*

---

## 5. Environmental Information
No specific environmental/lifestyle/infectious contributors were established in the retrieved excerpts for FL onset or progression. The biology-focused reviews emphasize **tumor microenvironment dependence** rather than an infectious etiology (xu2023advancesinthe pages 1-2).

---

## 6. Mechanism / Pathophysiology

### Multi-step lymphomagenesis and microenvironment
FL development is described as a multistep process in which BCL2-overexpressing precursor B cells accumulate additional lesions through repeated GC re‑entry; disease progression and immune escape are strongly shaped by tumor–microenvironment crosstalk (xu2023advancesinthe pages 1-2).

**Abstract quote (microenvironment role):** multi‑omics analyses provide “a comprehensive profile of microenvironmental components… unveiling the crosstalk between tumor and microenvironment that induce FL progression and facilitate immune escape.” (Xu et al., 2023‑03‑27; doi:10.7150/ijbs.80401) (xu2023advancesinthe pages 1-2).

### Key molecular pathways highlighted
- **Apoptosis evasion via BCL2 overexpression** after IGH::BCL2 translocation (xu2023advancesinthe pages 1-2, zinzani2024currentandfuture pages 1-2).
- **Epigenetic dysregulation** via frequent mutations in histone modifiers/acetyltransferases (KMT2D, CREBBP, EZH2, EP300) (xu2023advancesinthe pages 1-2, zinzani2024currentandfuture pages 1-2).
- **B‑cell receptor signaling pathway activation** (PI3K/BTK/SYK noted as frequently activated and therapeutic targets) (zinzani2024currentandfuture pages 1-2).
- **JAK/STAT signaling** in STAT6‑mutant, CD23‑associated t(14;18)-negative diffuse FL variant (kurz2023follicularlymphomain pages 8-10).

### Suggested GO biological process terms (examples)
- **Regulation of apoptotic process** (GO:0042981)
- **Chromatin organization** (GO:0006325)
- **Histone modification** (GO:0016570)
- **B cell receptor signaling pathway** (GO:0050853)
- **T cell activation** (GO:0042110)
- **Antigen processing and presentation** (GO:0019882) (relevant to immunotherapy biology)

### Suggested Cell Ontology (CL) terms for key cell types in FL microenvironment
- **Germinal center B cell** (CL:0002633)
- **T follicular helper cell** (CL:0002038)
- **Regulatory T cell** (CL:0000815)
- **CD8-positive, alpha-beta T cell** (CL:0000625)
- **Macrophage** (CL:0000235)
- **Follicular dendritic cell** (CL:0000447)

---

## 7. Anatomical Structures Affected

### Organ/tissue distribution
- **Lymph nodes** (primary; often disseminated) (xu2023advancesinthe pages 1-2).
- **Bone marrow** involvement commonly noted (xu2023advancesinthe pages 1-2, jacobsen2022follicularlymphoma2023 pages 1-2).
- **Spleen** involvement occurs (kurz2023follicularlymphomain pages 2-4).

### Suggested UBERON terms (examples)
- **Lymph node** (UBERON:0000029)
- **Bone marrow** (UBERON:0002371)
- **Spleen** (UBERON:0002106)

---

## 8. Temporal Development

### Onset
FL is typically **adult/older adult onset**, with a reported median diagnostic age of ~65 years (jacobsen2022follicularlymphoma2023 pages 1-2).

### Progression patterns
- Indolent course with repeated remissions/relapses (johnson2024qualityoflife pages 1-2).
- **POD24** (progression within 24 months of frontline therapy) is emphasized as a high-risk temporal pattern with markedly worse OS (Zinzani et al., 2024‑08; doi:10.1186/s40164-024-00551-1) (zinzani2024currentandfuture pages 1-2).

### Staging/progression to transformation
Histologic transformation to DLBCL is a key adverse event; one registry study identified biopsy‑confirmed transformation in **4.7%** of FL patients at median follow-up 6.3 years (SEER 2010–2018) (Vaughn & Epperla, 2023‑09; doi:10.1186/s40364-023-00525-1) (vaughn2023survivalofpatients pages 1-2).

---

## 9. Inheritance and Population

### Epidemiology (recent reviews)
- FL is described as the **second most common** NHL subtype in Western settings (zinzani2024currentandfuture pages 1-2, xu2023advancesinthe pages 1-2).
- Incidence: **2–4 per 100,000/year** in Western countries (Zinzani et al., 2024‑08; doi:10.1186/s40164-024-00551-1) (zinzani2024currentandfuture pages 1-2).
- Incidence (alternate estimate): **3–5 per 100,000/year** (Xu et al., 2023‑03‑27; doi:10.7150/ijbs.80401) (xu2023advancesinthe pages 1-2).

### Survival statistics
- In rituximab era cohorts: 10‑year OS in French and US cohorts reported as **79.8%** and **76.6%** (Zinzani et al., 2024‑08) (zinzani2024currentandfuture pages 1-2).
- Swedish registry (2003–2010): 10‑year OS by age group 18–49: **92%**, 50–59: **83%**, 60–69: **78%**, ≥70: **64%** (Jacobsen, 2022‑10; doi:10.1002/ajh.26737) (jacobsen2022follicularlymphoma2023 pages 1-2).

### POD24 as a high-risk subgroup
Patients with POD24 had **2-year/5-year OS 68%/50%** vs **97%/90%** without POD24 (zinzani2024currentandfuture pages 1-2).

---

## 10. Diagnostics

### Diagnostic approach (core elements)
- **Tissue biopsy** with morphology showing closely packed neoplastic follicles is central, with WHO‑HAEM5/ICC emphasizing integration of morphologic, immunophenotypic, and molecular features (kurz2023follicularlymphomain pages 4-6, laurent2023follicularlymphomaand pages 1-2).
- **Immunophenotype (classic FL):** pan‑B markers (CD19, CD20, PAX5) and GC markers (CD10, BCL6, HGAL); BCL2 protein expression in ~80–90% (often due to t(14;18)) (Kurz et al., 2023‑01; doi:10.3390/cancers15030785) (kurz2023follicularlymphomain pages 4-6).
- **Variant diagnostic hints:** t(14;18)-negative, CD23-associated/diffuse-pattern FL variant enriched for STAT6 mutations and 1p36 lesions (kurz2023follicularlymphomain pages 8-10, kurz2023follicularlymphomain pages 1-2).

### Classification visual evidence (WHO‑HAEM5 subtype list)
Table showing the WHO‑HAEM5 subtype schema was retrieved from Kurz et al. (2023) (kurz2023follicularlymphomain media 04784bfd).

### Suggested molecular tests (based on current practice implications in retrieved sources)
- FISH/NGS for **IGH::BCL2** (t(14;18)) and sequencing of key epigenetic modifiers when clinically relevant (diagnosis/subtyping and targeted therapy decisions) (kurz2023follicularlymphomain pages 4-6, izutsu2024tazemetostatforrelapsedrefractory pages 1-2).

(Detailed imaging criteria, ctDNA/liquid biopsy validation, and differential diagnosis algorithms were not captured in the accessible excerpts.)

---

## 11. Outcome / Prognosis

### Transformation prognosis (population data)
In a SEER analysis (2010–2018), transformed FL (t‑FL) had inferior outcomes compared with de novo DLBCL:
- 5‑year relative survival **54%** (t‑FL) vs **67%** (de novo DLBCL)
- 5‑year OS **49%** vs **57%
- Median OS **4.6 years** vs **8.8 years**
(Vaughn & Epperla, 2023‑09; doi:10.1186/s40364-023-00525-1) (vaughn2023survivalofpatients pages 1-2).

### R/R FL outcomes benchmark
For patients with R/R FL after ≥2 prior therapies, a later-line benchmark reported median **PFS 17 months** and **5‑year OS 75%** (Zinzani et al., 2024‑08) (zinzani2024currentandfuture pages 1-2).

### Real-world mortality and cost burden (late-line RWE)
In an Italian administrative dataset of patients reaching ≥3 lines of therapy, **34% died** at median 3‑year follow‑up; mean annual costs increased from **€14,508** pre-inclusion to **€21,081** at 1‑year follow-up (Ferreri et al., 2023‑09‑02; doi:10.3390/cancers15174403) (ferreri2023burdenofillness pages 1-2).

---

## 12. Treatment

### Standard paradigms (high-level)
- Many patients can be observed initially; systemic therapy can be deferred until symptoms or high tumor burden. Common systemic options include anti‑CD20–based regimens (rituximab ± chemotherapy) and chemo‑free immunomodulatory combinations (lenalidomide‑rituximab) (jacobsen2022follicularlymphoma2023 pages 1-2, ferreri2023burdenofillness pages 1-2).

### 2023–2024 advances and implementations in R/R FL
Novel immunotherapies (CD20×CD3 bispecific antibodies, CAR‑T) and targeted epigenetic therapy (EZH2 inhibition) are emphasized as major developments, with high response rates in later-line settings and expanding real-world uptake considerations (friedberg2023updateonfollicular pages 4-6, maurer2023matchingadjustedindirectcomparison pages 1-2, izutsu2024tazemetostatforrelapsedrefractory pages 1-2).

**Artifact: therapy landscape summary table (quantitative)**

| Therapy (generic; target/class) | Regulatory status (FDA/EMA/Japan approval year as stated) | Key supporting study and design (trial name/NCT; publication year) | Population/line | Key efficacy (ORR, CR, PFS) and follow-up | Key safety signals | Real-world/health economics notes if present |
|---|---|---|---|---|---|---|
| Mosunetuzumab (CD20×CD3 bispecific antibody) | FDA and European approvals in 2022 for R/R FL after ≥2 prior lines; FDA approval noted in Dec 2022 (friedberg2023updateonfollicular pages 4-6, jacobsen2022follicularlymphoma2023 pages 9-9) | GO29781, pivotal international phase 2; phase I/II program; NCT02500407; reported in 2023–2024 contextual sources (friedberg2023updateonfollicular pages 4-6, maurer2023matchingadjustedindirectcomparison pages 1-2) | R/R FL after ≥2 prior systemic therapies including alkylator and anti-CD20 therapy; high-risk subgroups included double-refractory and POD24 patients (friedberg2023updateonfollicular pages 4-6, maurer2023matchingadjustedindirectcomparison pages 1-2) | Phase 2: ORR 80%, CR 60%, median PFS 17.9 months in GO29781; Friedberg update cites median follow-up >18 months, median PFS 21 months, median DOR 22 months; phase I data showed CR rates >50% in double-refractory and POD24 patients (maurer2023matchingadjustedindirectcomparison pages 1-2, friedberg2023updateonfollicular pages 4-6) | CRS 44% in phase 2, almost all low grade; only one grade 3 and one grade 4 CRS event reported; phase I included neutropenia and CRS with fever, 7% hospitalization, neurologic AEs uncommon (friedberg2023updateonfollicular pages 4-6, jacobsen2022follicularlymphoma2023 pages 9-9) | MAIC versus LEO CReWE: weighted real-world cohort ORR 73%, CR 53%, 12-month PFS 60% vs mosunetuzumab trial 58%; Bayesian long-term modeling estimated median survival 11.6–17.0 years; US budget model found per-patient cumulative cost about $202,039 and small 3-year payer impact (maurer2023matchingadjustedindirectcomparison pages 1-2) |
| Epcoritamab (subcutaneous CD20×CD3 bispecific antibody) | Not stated as approved in the specific evidence set used here; described as in development/clinical advance in Jacobsen 2022 snippet (jacobsen2022follicularlymphoma2023 pages 9-9) | Phase I/II study; Jacobsen update cites early epcoritamab data (publication context 2022/2023) (jacobsen2022follicularlymphoma2023 pages 9-9) | R/R FL, later-line setting (jacobsen2022follicularlymphoma2023 pages 9-9) | ORR 90%, CR 50% in the cited phase I/II experience (jacobsen2022follicularlymphoma2023 pages 9-9) | CRS 59%, all grade 1–2 in cited snippet (jacobsen2022follicularlymphoma2023 pages 9-9) | No direct RWE or health-economic data in the provided evidence set (jacobsen2022follicularlymphoma2023 pages 9-9) |
| Glofitamab (CD20×CD3 bispecific antibody) | No approval status stated in the selected evidence set (jacobsen2022follicularlymphoma2023 pages 9-9) | Phase I/II study with obinutuzumab pre-treatment; cited in Jacobsen update (jacobsen2022follicularlymphoma2023 pages 9-9) | FL in relapsed/refractory setting (jacobsen2022follicularlymphoma2023 pages 9-9) | ORR 70.5%, CR 47.7% in FL (jacobsen2022follicularlymphoma2023 pages 9-9) | Low incidence of grade 3 CRS/neurologic events (jacobsen2022follicularlymphoma2023 pages 9-9) | No direct RWE or economic data in the provided evidence set (jacobsen2022follicularlymphoma2023 pages 9-9) |
| Axicabtagene ciloleucel / axi-cel (autologous anti-CD19 CAR-T) | Approved in the United States for relapsed/refractory FL based on ZUMA-5; approval noted by 2023 update sources (friedberg2023updateonfollicular pages 4-6) | ZUMA-5 phase 2; mature results summarized in 2023 review (friedberg2023updateonfollicular pages 4-6) | R/R FL, generally after failure of monoclonal antibody and alkylator therapy; considered for high-risk situations including selected POD24 patients (friedberg2023updateonfollicular pages 4-6) | In primary FL analysis: CR 79%; estimated 18-month PFS 66%; durable responses reported (friedberg2023updateonfollicular pages 4-6) | AEs similar to prior CAR-T experience; some decrease in severity of CRS and neurologic toxicity versus aggressive lymphoma histologies (friedberg2023updateonfollicular pages 4-6) | Propensity-matched comparison favored CAR-T over matched cohort, with median PFS not reached vs 12 months in comparator cohort; US cost-effectiveness model estimated +1.89 QALY vs mosunetuzumab and ICER $108,307/QALY (friedberg2023updateonfollicular pages 4-6) |
| Tisagenlecleucel / tisa-cel (autologous anti-CD19 CAR-T) | Approved by the United States FDA for FL based on trial cited in 2023 review (friedberg2023updateonfollicular pages 4-6) | ELARA-related experience summarized in 2023 review (friedberg2023updateonfollicular pages 4-6) | FL patients who received CAR-T infusion in relapsed/refractory setting (friedberg2023updateonfollicular pages 4-6) | CR 69%; 12-month PFS 67% (friedberg2023updateonfollicular pages 4-6) | Safety profile consistent with prior experience; nearly 20% treated outpatient in the cited trial summary (friedberg2023updateonfollicular pages 4-6) | No direct FL-specific cost data in the selected evidence set; sequencing relative to bispecific antibodies remains unresolved (friedberg2023updateonfollicular pages 4-6) |
| Tazemetostat (EZH2 inhibitor; oral epigenetic therapy) | US accelerated approval in 2020 for EZH2-mutated R/R FL after ≥2 prior therapies, or EZH2 wild-type without satisfactory alternatives; Japan approval in 2021 for EZH2-mutated R/R FL (izutsu2024tazemetostatforrelapsedrefractory pages 1-2) | Global phase II NCT01897571 and Japanese phase II NCT03456726; 3-year follow-up published 2024 (izutsu2024tazemetostatforrelapsedrefractory pages 1-2) | EZH2-mutated R/R FL, generally third line or later (izutsu2024tazemetostatforrelapsedrefractory pages 1-2) | Global phase II: ORR 69% in EZH2-mut cohort and 35% in wild-type cohort; Japanese 3-year follow-up: FL cohort ORR 70.6%, median PFS not reached, 24-month PFS 72.1%, 36-month PFS 64.1%, median follow-up 35.0 months (izutsu2024tazemetostatforrelapsedrefractory pages 1-2) | Long-term safety favorable; newly emerged grade 1–2 urinary tract infection, peripheral motor neuropathy, hypogammaglobulinemia; no unexpected grade ≥3 treatment-related AEs (izutsu2024tazemetostatforrelapsedrefractory pages 1-2) | Oral, time-continuous targeted option; useful for biomarker-selected EZH2-mutated patients; no direct RWE cost data in selected evidence set (izutsu2024tazemetostatforrelapsedrefractory pages 1-2) |
| Later-line R/R FL prognosis benchmark (context for novel therapies, not a therapy) | Not applicable (zinzani2024currentandfuture pages 1-2) | LEO CReWE real-world benchmark cited in 2024 review (zinzani2024currentandfuture pages 1-2) | Patients with R/R FL after ≥2 prior therapies (zinzani2024currentandfuture pages 1-2) | Median PFS 17 months and 5-year OS 75% in R/R FL after ≥2 prior therapies; POD24 subgroup had 2-year/5-year OS 68%/50% vs 97%/90% without POD24 (zinzani2024currentandfuture pages 1-2) | Not applicable | Useful comparator showing unmet need that newer bispecifics, CAR-T, and EZH2-targeted therapy aim to address (zinzani2024currentandfuture pages 1-2) |


*Table: This table summarizes major 2022-2024 therapeutic advances for relapsed/refractory follicular lymphoma using only the cited context, with trial-level efficacy, safety, and selected real-world or economic context. It is useful for comparing bispecific antibodies, CAR-T products, and EZH2-targeted therapy against the poor-outcome benchmark of later-line FL.*

### Example MAXO terms (suggestions)
- **Anti-CD20 monoclonal antibody therapy** (MAXO:0000013; general antibody therapy category—exact MAXO mapping may need verification)
- **Chimeric antigen receptor T-cell therapy** (CAR‑T; MAXO term should be selected from MAXO hierarchy)
- **Bispecific antibody therapy** (MAXO mapping required)
- **Radiotherapy** (MAXO mapping required)

(MAXO IDs require ontology lookup; not explicitly present in retrieved evidence.)

---

## 13. Prevention

### Current state
No established primary prevention strategy was identified in the retrieved literature excerpts. Current “prevention” is largely **tertiary** (preventing relapse/complications via optimized therapy sequencing and supportive care) and **secondary** (monitoring for progression/transformation), but specific evidence-based screening programs for asymptomatic individuals were not captured in the retrieved excerpts.

---

## 14. Other Species / Natural Disease
Not addressed in the retrieved excerpts; would require targeted searches in OMIA/veterinary oncology and comparative pathology resources.

---

## 15. Model Organisms
No specific FL model organism systems were extracted from the retrieved excerpts (despite the general recognition that microenvironment modeling is a research focus). Dedicated searches for genetically engineered mouse models (e.g., BCL2 transgenic GC models), xenografts, and 3D co-culture systems are needed.

---

# WHO‑HAEM5 Subtype Schema (visual evidence)
The WHO‑HAEM5 subtype list is shown in Kurz et al. Table 1 (kurz2023follicularlymphomain media 04784bfd).

---

# Limitations of this report (evidence availability)
1. **Ontology identifiers (MONDO/MeSH/Orphanet/ICD‑10/ICD‑11)** were not present in the accessed excerpts; only ICD‑9‑CM 202.0 was captured from an RWE study (ferreri2023burdenofillness pages 2-3).
2. **Etiology (environmental/infectious), protective factors, and gene–environment interactions** were not covered by the accessible evidence set.
3. **Model organisms and non-human natural disease** information was not retrieved.
4. Some claims that typically require primary trial publications (e.g., full GO29781 paper) were supported here via accessible abstracts/reviews and an RWE comparator study; deeper extraction from full primary reports would strengthen a knowledge base entry (friedberg2023updateonfollicular pages 4-6, maurer2023matchingadjustedindirectcomparison pages 1-2).


References

1. (xu2023advancesinthe pages 1-2): Tianyuan Xu, Zhong Zheng, and Weili Zhao. Advances in the multi-omics landscape of follicular lymphoma. International Journal of Biological Sciences, 19:1955-1967, Mar 2023. URL: https://doi.org/10.7150/ijbs.80401, doi:10.7150/ijbs.80401. This article has 10 citations and is from a peer-reviewed journal.

2. (zinzani2024currentandfuture pages 1-2): Pier Luigi Zinzani, Javier Muñoz, and Judith Trotman. Current and future therapies for follicular lymphoma. Experimental Hematology & Oncology, Aug 2024. URL: https://doi.org/10.1186/s40164-024-00551-1, doi:10.1186/s40164-024-00551-1. This article has 28 citations and is from a peer-reviewed journal.

3. (jacobsen2022follicularlymphoma2023 pages 1-2): Eric Jacobsen. Follicular lymphoma: 2023 update on diagnosis and management. American Journal of Hematology, 97:1638-1651, Oct 2022. URL: https://doi.org/10.1002/ajh.26737, doi:10.1002/ajh.26737. This article has 159 citations and is from a domain leading peer-reviewed journal.

4. (kurz2023follicularlymphomain pages 2-4): Katrin S. Kurz, Sabrina Kalmbach, Michaela Ott, Annette M. Staiger, German Ott, and Heike Horn. Follicular lymphoma in the 5th edition of the who-classification of haematolymphoid neoplasms—updated classification and new biological data. Cancers, 15:785, Jan 2023. URL: https://doi.org/10.3390/cancers15030785, doi:10.3390/cancers15030785. This article has 53 citations.

5. (ferreri2023burdenofillness pages 2-3): Andrés J. M. Ferreri, Pier Luigi Zinzani, Carlo Messina, Diletta Valsecchi, Maria Chiara Rendace, Eleonora Premoli, Elisa Giacomini, Chiara Veronesi, Luca Degli Esposti, and Paola Di Matteo. Burden of illness in follicular lymphoma with multiple lines of treatment, italian rwe analysis. Cancers, 15:4403, Sep 2023. URL: https://doi.org/10.3390/cancers15174403, doi:10.3390/cancers15174403. This article has 5 citations.

6. (kurz2023follicularlymphomain pages 4-6): Katrin S. Kurz, Sabrina Kalmbach, Michaela Ott, Annette M. Staiger, German Ott, and Heike Horn. Follicular lymphoma in the 5th edition of the who-classification of haematolymphoid neoplasms—updated classification and new biological data. Cancers, 15:785, Jan 2023. URL: https://doi.org/10.3390/cancers15030785, doi:10.3390/cancers15030785. This article has 53 citations.

7. (kurz2023follicularlymphomain pages 1-2): Katrin S. Kurz, Sabrina Kalmbach, Michaela Ott, Annette M. Staiger, German Ott, and Heike Horn. Follicular lymphoma in the 5th edition of the who-classification of haematolymphoid neoplasms—updated classification and new biological data. Cancers, 15:785, Jan 2023. URL: https://doi.org/10.3390/cancers15030785, doi:10.3390/cancers15030785. This article has 53 citations.

8. (laurent2023follicularlymphomaand pages 1-2): Camille Laurent, James R. Cook, Tadashi Yoshino, Leticia Quintanilla-Martinez, and Elaine S. Jaffe. Follicular lymphoma and marginal zone lymphoma: how many diseases? Virchows Archiv, 482:149-162, Nov 2023. URL: https://doi.org/10.1007/s00428-022-03432-2, doi:10.1007/s00428-022-03432-2. This article has 70 citations and is from a peer-reviewed journal.

9. (kurz2023follicularlymphomain pages 8-10): Katrin S. Kurz, Sabrina Kalmbach, Michaela Ott, Annette M. Staiger, German Ott, and Heike Horn. Follicular lymphoma in the 5th edition of the who-classification of haematolymphoid neoplasms—updated classification and new biological data. Cancers, 15:785, Jan 2023. URL: https://doi.org/10.3390/cancers15030785, doi:10.3390/cancers15030785. This article has 53 citations.

10. (chadburn2023classificationofbcell pages 2-5): Amy Chadburn, Annunziata Gloghini, and Antonino Carbone. Classification of b-cell lymphomas and immunodeficiency-related lymphoproliferations: what’s new? Hemato, 4:26-41, Jan 2023. URL: https://doi.org/10.3390/hemato4010003, doi:10.3390/hemato4010003. This article has 6 citations.

11. (vaughn2023survivalofpatients pages 1-2): John L. Vaughn and Narendranath Epperla. Survival of patients with transformed follicular lymphoma in the united states: a multiple cohort study. Biomarker Research, Sep 2023. URL: https://doi.org/10.1186/s40364-023-00525-1, doi:10.1186/s40364-023-00525-1. This article has 15 citations and is from a peer-reviewed journal.

12. (ferreri2023burdenofillness pages 1-2): Andrés J. M. Ferreri, Pier Luigi Zinzani, Carlo Messina, Diletta Valsecchi, Maria Chiara Rendace, Eleonora Premoli, Elisa Giacomini, Chiara Veronesi, Luca Degli Esposti, and Paola Di Matteo. Burden of illness in follicular lymphoma with multiple lines of treatment, italian rwe analysis. Cancers, 15:4403, Sep 2023. URL: https://doi.org/10.3390/cancers15174403, doi:10.3390/cancers15174403. This article has 5 citations.

13. (johnson2024qualityoflife pages 1-2): Patrick Connor Johnson, Abigail Bailey, Qiufei Ma, Neil Milloy, Emilia Biondi, Ruben G. W. Quek, Sarah Weatherby, and Sophie Barlow. Quality of life evaluation in patients with follicular cell lymphoma: a real-world study in europe and the united states. Advances in Therapy, 41:3342-3361, Jul 2024. URL: https://doi.org/10.1007/s12325-024-02882-1, doi:10.1007/s12325-024-02882-1. This article has 13 citations and is from a peer-reviewed journal.

14. (friedberg2023updateonfollicular pages 1-3): Jonathan W. Friedberg. Update on follicular lymphoma. Hematological Oncology, 41:43-47, Jun 2023. URL: https://doi.org/10.1002/hon.3138, doi:10.1002/hon.3138. This article has 32 citations and is from a peer-reviewed journal.

15. (kurz2023follicularlymphomain media 04784bfd): Katrin S. Kurz, Sabrina Kalmbach, Michaela Ott, Annette M. Staiger, German Ott, and Heike Horn. Follicular lymphoma in the 5th edition of the who-classification of haematolymphoid neoplasms—updated classification and new biological data. Cancers, 15:785, Jan 2023. URL: https://doi.org/10.3390/cancers15030785, doi:10.3390/cancers15030785. This article has 53 citations.

16. (izutsu2024tazemetostatforrelapsedrefractory pages 1-2): Koji Izutsu, Kiyoshi Ando, Momoko Nishikori, Hirohiko Shibayama, Hideki Goto, Junya Kuroda, Koji Kato, Yoshitaka Imaizumi, Kisato Nosaka, Rika Sakai, Maho Abe, Seiichiro Hojo, Tadashi Nakanishi, and Shinya Rai. Tazemetostat for relapsed/refractory b-cell non-hodgkin lymphoma with ezh2 mutation in japan: 3-year follow-up for a phase ii study. International Journal of Hematology, 120:621-630, Aug 2024. URL: https://doi.org/10.1007/s12185-024-03834-9, doi:10.1007/s12185-024-03834-9. This article has 10 citations and is from a peer-reviewed journal.

17. (friedberg2023updateonfollicular pages 4-6): Jonathan W. Friedberg. Update on follicular lymphoma. Hematological Oncology, 41:43-47, Jun 2023. URL: https://doi.org/10.1002/hon.3138, doi:10.1002/hon.3138. This article has 32 citations and is from a peer-reviewed journal.

18. (maurer2023matchingadjustedindirectcomparison pages 1-2): Matthew J. Maurer, Carla Casulo, Melissa C. Larson, Thomas M. Habermann, Izidore S. Lossos, Yucai Wang, Loretta J. Nastoupil, Christopher Strouse, Dai Chihara, Peter Martin, Jonathon B. Cohen, Brad S. Kahl, W Richard Burack, Jean L. Koff, Yong Mun, Anthony Masaquel, Mei Wu, Michael C. Wei, Ashwini Shewade, Jia Li, James R. Cerhan, Brian K. Link, and Christopher R. Flowers. Matching-adjusted indirect comparison from the lymphoma epidemiology of outcomes consortium for real world evidence (leo crewe) study to a clinical trial of mosunetuzumab in relapsed or refractory follicular lymphoma. Haematologica, 109:2177-2185, Nov 2023. URL: https://doi.org/10.3324/haematol.2023.283737, doi:10.3324/haematol.2023.283737. This article has 9 citations.

19. (jacobsen2022follicularlymphoma2023 pages 9-9): Eric Jacobsen. Follicular lymphoma: 2023 update on diagnosis and management. American Journal of Hematology, 97:1638-1651, Oct 2022. URL: https://doi.org/10.1002/ajh.26737, doi:10.1002/ajh.26737. This article has 159 citations and is from a domain leading peer-reviewed journal.

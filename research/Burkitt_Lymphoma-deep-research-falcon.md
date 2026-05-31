---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T10:32:03.677226'
end_time: '2026-05-08T10:45:59.120407'
duration_seconds: 835.44
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Burkitt Lymphoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Burkitt Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Burkitt Lymphoma** covering all of the
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
- **Disease Name:** Burkitt Lymphoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Burkitt Lymphoma** covering all of the
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


# Burkitt Lymphoma — Disease Characteristics Research Report (2023–2024 prioritized)

## Target Disease
- **Disease name:** Burkitt lymphoma (BL)
- **MONDO ID:** *Not confirmed from retrieved sources in this run* (knowledge-base curation should cross-check MONDO via official MONDO/OBO lookup)
- **Category:** Mature B-cell non-Hodgkin lymphoma; high-grade/aggressive B-cell lymphoma entity in WHO-HAEM5 and ICC frameworks (zanelli2024adiagnosticapproach pages 6-8, crombie2021thetreatmentof pages 3-4)

This report synthesizes **aggregated disease-level resources** (SEER registries, systematic reviews/meta-analyses, WHO/ICC-aligned diagnostic reviews) plus **patient/tumor-derived experimental models** (patient-derived cell lines and NSG “avatar” mouse models). (mburu2023incidenceofburkitt pages 1-3, alkhreisat2023worldwideprevalenceof pages 1-2, lakshmi2023endemicburkittlymphoma pages 1-2)

| Item | Value | Notes | Source |
|---|---|---|---|
| Clinical variants / classification | Endemic BL, sporadic BL, immunodeficiency-associated BL | WHO-defined clinical variants are histologically identical; WHO-HAEM5 additionally distinguishes EBV-positive vs EBV-negative BL. ICC advises TdT-positive MYC-rearranged cases be classified as B-ALL/LBL rather than BL (alkhreisat2023worldwideprevalenceof pages 2-3, zanelli2024adiagnosticapproach pages 6-8) | Al-Khreisat et al., 2023, *Diagnostics*, doi:10.3390/diagnostics13122068, https://doi.org/10.3390/diagnostics13122068; Zanelli et al., 2024, *Int J Mol Sci*, doi:10.3390/ijms252313213, https://doi.org/10.3390/ijms252313213 |
| Key MYC translocations | t(8;14) / IGH::MYC: 70–80%; t(2;8) / IGK::MYC: ~15%; t(8;22) / IGL::MYC: ~5% | MYC translocations are described as nearly universal across BL variants; other reviews note ~80% t(8;14) with remainder t(2;8)/t(8;22) (siddiqui2023fromthearchives pages 3-4, malfona2024refractoryburkittlymphoma pages 1-2, crombie2021thetreatmentof pages 3-4) | Siddiqui et al., 2023, *Ann Diagn Pathol*, doi:10.1016/j.anndiagpath.2023.152182, https://doi.org/10.1016/j.anndiagpath.2023.152182; Malfona et al., 2024, *Blood Lymphat Cancer*, doi:10.2147/BLCTT.S407804, https://doi.org/10.2147/BLCTT.S407804 |
| EBV prevalence, pooled worldwide | 57.5% (95% CI 51.5–63.4), n=4,837 BL patients | Meta-analysis of 135 studies; authors conclude EBV is present in a “significantly high proportion” of BL patients (alkhreisat2023worldwideprevalenceof pages 1-2) | Al-Khreisat et al., 2023, *Diagnostics*, doi:10.3390/diagnostics13122068, https://doi.org/10.3390/diagnostics13122068 |
| EBV prevalence by subtype | Endemic: ~95%; Sporadic: ~10–30%; Immunodeficiency-associated: ~20–40% | Other sources in gathered evidence report endemic ~90% and sporadic/immunodeficiency-associated ~25–40%, reflecting source-dependent ranges (alkhreisat2023worldwideprevalenceof pages 2-3, mburu2023incidenceofburkitt pages 1-3, crombie2021thetreatmentof pages 3-4, zanelli2024adiagnosticapproach pages 6-8) | Al-Khreisat et al., 2023, *Diagnostics*, doi:10.3390/diagnostics13122068, https://doi.org/10.3390/diagnostics13122068; Mburu et al., 2023, *Int J Cancer*, doi:10.1002/ijc.34618, https://doi.org/10.1002/ijc.34618 |
| U.S. SEER incidence | 3.96 per million person-years | SEER 22, 2000–2019, n=11,626; male:female ratio 2.85:1; incidence higher in Hispanic and White than Black individuals (4.52, 4.12 vs 3.14 per million) (mburu2023incidenceofburkitt pages 1-3, mburu2023incidenceofburkitt pages 3-5) | Mburu et al., 2023, *Int J Cancer*, doi:10.1002/ijc.34618, https://doi.org/10.1002/ijc.34618 |
| U.S. SEER 2-year overall survival | 64% | Highest in pediatric patients and lowest in Black and elderly individuals; survival improved by 20% between 2000 and 2019 (mburu2023incidenceofburkitt pages 1-3) | Mburu et al., 2023, *Int J Cancer*, doi:10.1002/ijc.34618, https://doi.org/10.1002/ijc.34618 |
| Sub-Saharan Africa incidence / burden | Incidence range 0.5 per million (Ethiopia) to 19.3 per million (Malawi); ~3,900 new cases estimated in 2018 | Endemic BL represents ~25–50% of childhood cancers in SSA and up to 70% in holo-endemic malaria regions; >50% of children/young adults with endemic BL do not survive in SSA (chamba2023clinicalapplicationof pages 1-2) | Chamba et al., 2023, *Cambridge Prisms: Precision Medicine*, doi:10.1017/pcm.2023.1, https://doi.org/10.1017/pcm.2023.1 |
| Key diagnostic IHC markers | CD10+, BCL6+, BCL2−/weak, Ki-67 >95% | Strong B-cell markers also include CD20, CD79a, PAX5, CD19, surface IgM/light-chain restriction; morphology shows uniform medium-sized cells and starry-sky pattern (zanelli2024adiagnosticapproach pages 6-8, malfona2024refractoryburkittlymphoma pages 1-2) | Zanelli et al., 2024, *Int J Mol Sci*, doi:10.3390/ijms252313213, https://doi.org/10.3390/ijms252313213; Malfona et al., 2024, *Blood Lymphat Cancer*, doi:10.2147/BLCTT.S407804, https://doi.org/10.2147/BLCTT.S407804 |
| Recommended EBV test | EBER in situ hybridization recommended | EBER ISH is recommended in diagnostic workup; positive in most endemic BL and ~30% of sporadic/immunodeficiency-associated BL. EBER1/2 serve as markers of EBV infection (zanelli2024adiagnosticapproach pages 6-8, siddiqui2023fromthearchives pages 3-4) | Zanelli et al., 2024, *Int J Mol Sci*, doi:10.3390/ijms252313213, https://doi.org/10.3390/ijms252313213; Siddiqui et al., 2023, *Ann Diagn Pathol*, doi:10.1016/j.anndiagpath.2023.152182, https://doi.org/10.1016/j.anndiagpath.2023.152182 |
| HGBL-11q differential features | MYC-rearrangement negative; 11q23.3 gains with 11q24.1 loss; EBV negative; CD10+, BCL6+, Ki-67 >90% | Important MYC-negative BL mimic; FISH recommended for MYC-negative B-cell lymphomas with BL-like morphology/immunophenotype. Lacks ID3-TCF3 pathway mutations typical of BL; mutational profile closer to GCB-DLBCL; coarse apoptotic bodies can be a clue (coupland2024thefifthedition pages 12-12, zanelli2024adiagnosticapproach pages 9-11) | Coupland et al., 2024, *J Pathol*, doi:10.1002/path.6246, https://doi.org/10.1002/path.6246; Zanelli et al., 2024, *Int J Mol Sci*, doi:10.3390/ijms252313213, https://doi.org/10.3390/ijms252313213 |


*Table: This table summarizes core Burkitt lymphoma classification, genetics, EBV epidemiology, survival, and diagnostic features from the gathered evidence. It is designed as a compact reference for knowledge-base population and citation tracking.*

---

## 1. Disease Information

### Overview (definition, current understanding)
Burkitt lymphoma is a **highly aggressive mature B-cell lymphoma** characterized by rapid tumor growth, frequent extranodal disease, and a defining genomic hallmark of **MYC dysregulation due to IG::MYC translocation**. (crombie2021thetreatmentof pages 3-4, zanelli2024adiagnosticapproach pages 6-8)

### Clinical-epidemiologic variants (WHO convention)
BL is classically described in three variants: **endemic**, **sporadic**, and **immunodeficiency-associated**. (zanelli2024adiagnosticapproach pages 6-8, malfona2024refractoryburkittlymphoma pages 1-2)

**Direct abstract quote (definition):** Crombie & LaCasce (Blood, 2021) define BL as “**a highly aggressive, B-cell, non-Hodgkin lymphoma (NHL) categorized into endemic, sporadic and immunodeficiency-associated subtypes**.” (crombie2021thetreatmentof pages 1-2)

### Synonyms / alternative names (as used in retrieved sources)
- “**Burkitt lymphoma/leukemia**” and “**Burkitt lymphoma/leukemia (BLL)**” are used when including leukemic presentations (malfona2024refractoryburkittlymphoma pages 1-2).
- Historical/related diagnostic terms in the differential include “**Burkitt-like lymphoma with 11q aberration**” (now within high-grade B-cell lymphoma with 11q aberration; see Diagnostics section). (malfona2024refractoryburkittlymphoma pages 1-2, coupland2024thefifthedition pages 12-12)

### Key classification resources (2023–2024)
Recent diagnostic reviews emphasize alignment of daily practice with **WHO 5th edition (WHO-HAEM5)** and the **International Consensus Classification (ICC, 2022)**, including new/clarified boundaries between BL, HGBL-NOS, and MYC-negative BL mimics. (zanelli2024adiagnosticapproach pages 6-8, zanelli2024adiagnosticapproach pages 9-11, coupland2024thefifthedition pages 12-12)

---

## 2. Etiology

### Disease causal factors (genetic, infectious, mechanistic)
**Genetic driver:** The central causal lesion is **MYC activation** via an **immunoglobulin locus–MYC translocation** (most commonly IGH::MYC). (malfona2024refractoryburkittlymphoma pages 1-2, zanelli2024adiagnosticapproach pages 6-8)

**Infectious cofactor:** **Epstein–Barr virus (EBV)** contributes strongly in endemic BL and in subsets of other variants. A 2023 meta-analysis estimated EBV presence in **57.5%** of BL patients overall (pooled worldwide). (alkhreisat2023worldwideprevalenceof pages 1-2)

**Direct abstract quote (EBV prevalence meta-analysis):** Al‑Khreisat et al. (Diagnostics, 2023) report: “**The prevalence of Epstein–Barr virus in patients with Burkitt lymphoma was 57.5% (95% CI: 51.5 to 63.4, n = 4837)**.” (alkhreisat2023worldwideprevalenceof pages 1-2)

### Risk factors
**Geographic/ecologic:** Endemic BL is described as occurring in malaria-endemic regions and being largely EBV-driven; the SSA burden is substantial and strongly linked to diagnostic and treatment capacity constraints. (chamba2023clinicalapplicationof pages 1-2, chamba2023clinicalapplicationof pages 2-3)

**Immunodeficiency:** Immunodeficiency-associated BL includes HIV-associated BL; EBV positivity in sporadic/immunodeficiency-associated BL is reported in the ~25–40% range by a high-impact treatment review. (crombie2021thetreatmentof pages 3-4)

### Protective factors
No specific **genetic protective variants** or **environmental protective factors** were identified in the retrieved sources for this run; this remains a gap for the knowledge-base entry requiring targeted searches (e.g., GWAS Catalog, host genetic studies of EBV/malaria interaction).

### Gene–environment interactions
The retrieved 2023–2024 sources support a conceptual interaction where chronic immune stimulation/infection exposure (EBV; malaria in endemic regions; immunodeficiency states) increases the probability of transformation in a B cell already prone to/experiencing MYC dysregulation, but they do not provide quantitative interaction effect sizes in the accessible excerpts. (chamba2023clinicalapplicationof pages 1-2, malfona2024refractoryburkittlymphoma pages 1-2)

---

## 3. Phenotypes

### Common clinical patterns (high-level)
BL is a rapidly progressive lymphoma with frequent extranodal involvement; endemic cases commonly involve craniofacial/jaw regions, while sporadic cases often present with abdominal disease (pattern-level statements supported in diagnostic and clinical reviews). (harlendea2024ki67asa pages 2-4, crombie2021thetreatmentof pages 3-4)

### Diagnostic phenotype (morphology + immunophenotype)
The diagnostic phenotype strongly shapes “phenotype” documentation:
- **Morphology:** diffuse proliferation of relatively uniform medium-sized cells with frequent mitoses and a **“starry sky”** pattern. (zanelli2024adiagnosticapproach pages 6-8)
- **Immunophenotype:** germinal center profile with **CD10+**, **BCL6+**, typically **BCL2−/weak**, and **very high proliferation** (Ki-67 typically **>95%**). (zanelli2024adiagnosticapproach pages 6-8, malfona2024refractoryburkittlymphoma pages 1-2)

### Suggested HPO terms (knowledge-base oriented; not exhaustive)
Because the retrieved excerpts emphasize diagnostic morphology and general clinical aggressiveness rather than structured symptom prevalence, the most defensible HPO mapping in this run is to **lymphoma-related and organ-mass manifestations** and **laboratory/complication phenotypes** described in BL treatment contexts:
- **Lymphadenopathy** (HP:0002716) (supported as a common presenting feature in adult/adolescent cohort description) (harlendea2024ki67asa pages 2-4)
- **Abdominal pain** (HP:0002027) (harlendea2024ki67asa pages 2-4)
- **Tumor lysis syndrome** (HP:0003466) (not quantified in retrieved evidence excerpts; included as clinically relevant but requires primary citation beyond current excerpts)

*Gap note:* The template requests onset/progression/frequency/QoL per phenotype; these require dedicated cohort and QoL instrument papers that were not retrieved in this run.

---

## 4. Genetic/Molecular Information

### Causal genes / defining lesion
- **MYC**: defining lesion is IG::MYC translocation (MYC at 8q24). (zanelli2024adiagnosticapproach pages 6-8, malfona2024refractoryburkittlymphoma pages 1-2)

### Chromosomal abnormalities (translocations)
Reported translocation partners and approximate frequencies:
- **t(8;14) IGH::MYC:** ~70–80% (siddiqui2023fromthearchives pages 3-4)
- **t(2;8) IGK::MYC:** ~15% (siddiqui2023fromthearchives pages 3-4)
- **t(8;22) IGL::MYC:** ~5% (siddiqui2023fromthearchives pages 3-4)

### Cooperating somatic alterations (recurrent pathways/genes)
Multiple sources emphasize cooperating lesions, particularly in BCR/PI3K signaling and cell-cycle control:
- **TCF3 / ID3 pathway:** reported as mutated in ~70% of sporadic and immunodeficiency-associated BL and ~40% of endemic BL in a diagnostic pathology review; this pathway connects to PI3K and CCND3 activation. (siddiqui2023fromthearchives pages 3-4)
- **CCND3:** reported as found in about one-third of cases in a 2024 clinical review. (malfona2024refractoryburkittlymphoma pages 1-2)
- **TP53:** TP53 alterations occur in BL (e.g., up to ~35% reported in an adult BL treatment review excerpt). (crombie2021thetreatmentof pages 3-4)

### EBV-associated molecular features
EBV detection is typically via **EBER in situ hybridization** and is linked to distinct latency programs; EBER1/2 are noted as markers of EBV infection in BL. (zanelli2024adiagnosticapproach pages 6-8, siddiqui2023fromthearchives pages 3-4)

### Suggested GO biological process terms (mechanism-oriented)
Based on described biology (MYC-driven proliferation; apoptosis evasion; metabolic reprogramming), plausible GO terms for knowledge-base scaffolding include:
- **Cell cycle process** (GO:0022402)
- **Regulation of apoptotic process** (GO:0042981)
- **Regulation of B cell activation** (GO:0050864)
These are mechanistically consistent with the MYC-centric and apoptosis/IFN signatures described in models and reviews, but the retrieved excerpts do not provide explicit GO mappings. (tandon2023translocationtalesunraveling pages 16-17, lakshmi2023endemicburkittlymphoma pages 10-12)

---

## 5. Environmental Information

### Infectious agents
- **Epstein–Barr virus (EBV):** strong association, especially in endemic BL (~95% reported in systematic review background; pooled prevalence >50%). (alkhreisat2023worldwideprevalenceof pages 2-3, alkhreisat2023worldwideprevalenceof pages 1-2)

### Resource-limited setting determinants (SSA)
In sub-Saharan Africa, non-biologic environmental/system factors materially influence outcomes, particularly **limited access to reliable diagnostic services**, which contributes to delay and misdiagnosis. (chamba2023clinicalapplicationof pages 1-2)

**Direct quote (diagnostic access/outcomes context):** Chamba et al. (Cambridge Prisms: Precision Medicine, 2023) report “**limited access to reliable diagnostic services leading to significant delays and misdiagnoses**.” (chamba2023clinicalapplicationof pages 1-2)

---

## 6. Mechanism / Pathophysiology

### Causal chain (high-level)
1. **Initiating/defining event:** reciprocal **IG::MYC translocation** causes MYC overexpression/deregulation. (zanelli2024adiagnosticapproach pages 6-8, crombie2021thetreatmentof pages 3-4)
2. **Downstream oncogenic program:** MYC drives proliferation, cell-cycle progression, apoptosis evasion, and metabolic rewiring (review-level synthesis). (tandon2023translocationtalesunraveling pages 16-17)
3. **Cooperating lesions:** recurrent mutations in pathways such as **TCF3/ID3** and **CCND3** reinforce proliferative/survival signaling (including PI3K). (siddiqui2023fromthearchives pages 3-4, malfona2024refractoryburkittlymphoma pages 1-2)
4. **Contextual cofactors:** EBV (especially endemic disease) and immunodeficiency states likely shape B-cell activation and immune evasion, facilitating malignant expansion. (alkhreisat2023worldwideprevalenceof pages 2-3, crombie2021thetreatmentof pages 3-4)

### Recent mechanistic developments (2023–2024)
**Model-informed heterogeneity and response biology:** Patient-derived BL “avatar” mouse models (NSG-BL) show substantial inter-patient heterogeneity in growth/survival and EBV protein expression and reveal distinct signatures of rituximab sensitivity (apoptosis/mTORC1) vs unresponsiveness (IFN-α signature involving IRF7/ISG15). (lakshmi2023endemicburkittlymphoma pages 1-2, lakshmi2023endemicburkittlymphoma pages 10-12)

---

## 7. Anatomical Structures Affected

### Tissue/cell of origin (cellular level)
BL is a **germinal center B-cell phenotype** lymphoma (CD10+, BCL6+) and expresses mature B-cell markers (CD20, CD79a, PAX5, CD19, surface IgM). (zanelli2024adiagnosticapproach pages 6-8, crombie2021thetreatmentof pages 3-4)

### Suggested Cell Ontology (CL) term
- **Germinal center B cell** (CL term suggestion; explicit CL code not provided in retrieved sources)

### Suggested UBERON terms (localization; high-level)
- **Lymph node** (UBERON:0000029)
- **Bone marrow** (UBERON:0002371)
- **Gastrointestinal tract** (UBERON:0005409)
These anatomical suggestions align with “high extranodal involvement” emphasized in BL reviews but are not enumerated with site frequencies in the retrieved excerpts. (crombie2021thetreatmentof pages 1-2)

---

## 8. Temporal Development

BL is described as a rapidly progressive neoplasm, and endemic BL peaks in childhood (median age ~6 years in review background). (alkhreisat2023worldwideprevalenceof pages 2-3, malfona2024refractoryburkittlymphoma pages 1-2)

---

## 9. Inheritance and Population

### Epidemiology — United States (SEER; 2023 primary analysis)
Mburu et al. analyzed **11,626** BL cases in SEER 22 (2000–2019) and reported:
- **Age-standardized incidence:** **3.96 per million person-years** (mburu2023incidenceofburkitt pages 1-3)
- **Sex ratio:** **2.85:1 male:female** (mburu2023incidenceofburkitt pages 1-3)
- **2-year overall survival:** **64%**, with improvement over time (“Survival improved by 20% between 2000 and 2019.”) (mburu2023incidenceofburkitt pages 1-3)

**Direct abstract quote (incidence/survival):** Mburu et al. (Int J Cancer, 2023) report “**The age-standardized BL incidence rate was 3.96/million person-years, with a 2.85:1 male-to-female ratio**” and “**Overall survival from BL was 64% at 2 years**.” (mburu2023incidenceofburkitt pages 1-3)

### Epidemiology — sub-Saharan Africa (implementation-focused 2023 review)
Chamba et al. summarize large heterogeneity in SSA incidence and high mortality:
- **Incidence range:** **0.5/million (Ethiopia) to 19.3/million (Malawi)** (chamba2023clinicalapplicationof pages 1-2)
- **Estimated new cases:** **~3,900 in SSA in 2018** (chamba2023clinicalapplicationof pages 1-2)
- **Outcome:** “more than 50%” of children/young adults with endemic BL in SSA do not survive (chamba2023clinicalapplicationof pages 1-2)

---

## 10. Diagnostics

### Core diagnostic concept (WHO-HAEM5/ICC-aligned)
Diagnosis relies on **typical morphology**, **germinal-center B-cell immunophenotype**, and confirmation of the **isolated IG::MYC rearrangement**, with routine assessment of EBV status by EBER in situ hybridization (especially for classification and context). (zanelli2024adiagnosticapproach pages 6-8, zanelli2024adiagnosticapproach pages 9-11)

### Immunohistochemistry (IHC) and biomarkers
Commonly emphasized IHC pattern:
- B-cell markers: **CD20, CD79a, PAX5, CD19** (zanelli2024adiagnosticapproach pages 6-8)
- Germinal center markers: **CD10+, BCL6+** (zanelli2024adiagnosticapproach pages 6-8)
- **BCL2 negative or weak** (zanelli2024adiagnosticapproach pages 6-8)
- **Ki-67 typically >95%** (zanelli2024adiagnosticapproach pages 6-8, malfona2024refractoryburkittlymphoma pages 1-2)

### EBV testing
A WHO/ICC-oriented diagnostic review recommends **EBER in situ hybridization** and reports EBER positivity in most endemic BL and ~30% of sporadic/immunodeficiency-associated BL. (zanelli2024adiagnosticapproach pages 6-8)

### Cytogenetics / FISH and differential diagnosis
- A 2024 diagnostic algorithm paper notes WHO-HAEM5 and ICC recommend **routine FISH screening** for **MYC, BCL2, and BCL6** in large B-cell lymphomas to capture double/triple hit disease. (zanelli2024adiagnosticapproach pages 9-11)
- BL mimics include **high-grade B-cell lymphoma with 11q aberration (HGBL-11q)**, which is typically **MYC rearrangement–negative**, **EBV-negative**, and defined by 11q gain/loss patterns detectable by interphase FISH. Screening for 11q is recommended specifically in **MYC-R–negative** cases with BL-like morphology/immunophenotype. (coupland2024thefifthedition pages 12-12)

### Liquid biopsy / cell-free DNA (real-world implementation focus)
A 2023 precision-medicine review proposes **circulating tumor DNA (ctDNA)/cell-free DNA (cfDNA)** approaches to improve diagnosis and monitoring in SSA where FISH/PET may be limited:
- “c-MYC is therefore theoretically an ideal target for the diagnosis of BL from ctDNA.” (chamba2023clinicalapplicationof pages 1-2)
- Sequencing of plasma ctDNA detected MYC translocations in ~79% of cases vs FISH, rising to ~95% in high tumor burden (ctDNA >16 pg/ml). (chamba2023clinicalapplicationof pages 3-4)
- Implementation barriers: limited pathology capacity, lack of accredited labs, limited bioinformatics training/infrastructure, and long tissue-diagnostic delays (up to 71 days vs 2 days in the USA). (chamba2023clinicalapplicationof pages 2-3, chamba2023clinicalapplicationof pages 4-5)

---

## 11. Outcome / Prognosis

### Registry-based survival (U.S.)
Two-year overall survival was **64%** in SEER 2000–2019 analysis, with highest survival in pediatric patients and lowest in Black and elderly individuals. (mburu2023incidenceofburkitt pages 1-3)

### Relapsed/refractory disease prognosis
A 2024 review emphasizes that despite high frontline cure rates, refractory BL has very poor outcomes.

**Direct abstract quote (refractory outcomes):** Malfona et al. (Blood and Lymphatic Cancer: Targets and Therapy, published March 2024) state: “**The prognosis is very poor, ranging from less than 10% to 30–40%, with longer survival only in transplanted patients.**” (malfona2024refractoryburkittlymphoma pages 1-2)

---

## 12. Treatment

### Current standard approaches (high-level)
Frontline therapy is based on **intensive, multi-agent chemotherapy regimens**, often with **anti-CD20 immunotherapy (rituximab)**; outcomes are generally excellent in pediatric populations and lower in adults, with major challenges in refractory disease. (malfona2024refractoryburkittlymphoma pages 1-2, harlendea2024ki67asa pages 2-4)

A 2024 refractory BL review summarizes frontline outcome expectations:
- Cure rates “outreaching **90%**” in pediatric age and “**70%**” in adult age in settings with standard intensive approaches. (malfona2024refractoryburkittlymphoma pages 1-2)

### Emerging and investigational approaches
A 2024 refractory BL review notes emerging targeted strategies across multiple axes (e.g., BCR pathway inhibitors, proteasome inhibitors, next-generation antibodies, CAR-T and bispecific antibodies) but emphasizes limited data and heterogeneity of salvage settings. (malfona2024refractoryburkittlymphoma pages 1-2)

### Active clinical trials (examples from retrieved registry search)
ClinicalTrials.gov search retrieved multiple recruiting/active CAR-T trials broadly enrolling relapsed/refractory B-cell hematologic malignancies that may include BL among eligible B-cell lymphomas, e.g.:
- **NCT06735495** (CD19 & CD22 bispecific CAR-T; Phase 1/2; recruiting) (NCT06735495 chunk 1, NCT06735495 chunk 2)
- **NCT06503094** (CD19 & CD20 bispecific CAR-T; Phase 1/2; recruiting) (NCT06503094 chunk 1, NCT06503094 chunk 2)

*Note:* Eligibility specifics for Burkitt lymphoma require per-trial confirmation from the full record text.

### Suggested MAXO terms (treatment-action ontology; high-level)
- **Chemotherapy** (NCIT:C15986; suggested)
- **Monoclonal antibody therapy (rituximab/anti-CD20)** (MAXO term suggestion)
- **Hematopoietic stem cell transplantation** (MAXO term suggestion; relevant in refractory settings) (malfona2024refractoryburkittlymphoma pages 1-2)
- **CAR T-cell therapy** (MAXO term suggestion; investigational) (NCT06735495 chunk 1)

---

## 13. Prevention

No BL-specific primary prevention interventions were directly evidenced in the retrieved excerpts beyond the general implication that reducing infection-related drivers (EBV/malaria) and improving HIV management could reduce risk. The 2023–2024 retrieved sources focus more on **diagnostic and treatment capacity** as the most immediate, actionable lever for mortality reduction in endemic settings. (chamba2023clinicalapplicationof pages 1-2, chamba2023clinicalapplicationof pages 4-5)

---

## 14. Other Species / Natural Disease

No naturally occurring non-human BL analogs were identified in the retrieved evidence excerpts. (Gap for targeted veterinary/OMIA searches.)

---

## 15. Model Organisms

### Patient-derived “avatar” mouse models (2023 development)
Lakshmi et al. (Life Science Alliance, 2023) established five patient-derived BL tumor cell lines and corresponding **NSG-BL avatar mouse models**, demonstrating transcriptomic fidelity to the originating tumors and substantial inter-patient heterogeneity in growth/survival and EBV protein expression. (lakshmi2023endemicburkittlymphoma pages 1-2)

These models were used to test rituximab response and to identify response-associated pathways (apoptosis/mTORC1 vs IFN-α signatures), providing a translational framework for prioritizing targeted therapies relevant to endemic BL. (lakshmi2023endemicburkittlymphoma pages 10-12)

---

## Evidence and citation notes (PMID handling)
Many retrieved sources were provided with DOIs/URLs but not PMIDs in the tool outputs. Where PMIDs are required for the knowledge base, these should be added by matching DOI→PMID in PubMed during curation. This limitation reflects metadata availability in the retrieved excerpts rather than absence of PubMed indexing.

## Key URLs and publication dates (selected)
- Mburu et al., **Jun 2023**, *International Journal of Cancer*: https://doi.org/10.1002/ijc.34618 (mburu2023incidenceofburkitt pages 1-3)
- Al‑Khreisat et al., **Jun 2023**, *Diagnostics*: https://doi.org/10.3390/diagnostics13122068 (alkhreisat2023worldwideprevalenceof pages 1-2)
- Chamba et al., **Jan 2023**, *Cambridge Prisms: Precision Medicine*: https://doi.org/10.1017/pcm.2023.1 (chamba2023clinicalapplicationof pages 1-2)
- Lakshmi et al., **Mar 2023**, *Life Science Alliance*: https://doi.org/10.26508/lsa.202101355 (lakshmi2023endemicburkittlymphoma pages 1-2)
- Malfona et al., **Mar 2024**, *Blood and Lymphatic Cancer: Targets and Therapy*: https://doi.org/10.2147/BLCTT.S407804 (malfona2024refractoryburkittlymphoma pages 1-2)
- Zanelli et al., **Dec 2024**, *International Journal of Molecular Sciences*: https://doi.org/10.3390/ijms252313213 (zanelli2024adiagnosticapproach pages 6-8)


References

1. (zanelli2024adiagnosticapproach pages 6-8): Magda Zanelli, Francesca Sanguedolce, Maurizio Zizzo, Stefano Ricci, Alessandra Bisagni, Andrea Palicelli, Valentina Fragliasso, Benedetta Donati, Giuseppe Broggi, Ioannis Boutas, Nektarios Koufopoulos, Moira Foroni, Francesca Coppa, Andrea Morini, Paola Parente, Valeria Zuccalà, Rosario Caltabiano, Massimiliano Fabozzi, Luca Cimino, Antonino Neri, and Stefano Ascani. A diagnostic approach in large b-cell lymphomas according to the fifth world health organization and international consensus classifications and a practical algorithm in routine practice. International Journal of Molecular Sciences, 25:13213, Dec 2024. URL: https://doi.org/10.3390/ijms252313213, doi:10.3390/ijms252313213. This article has 10 citations.

2. (crombie2021thetreatmentof pages 3-4): Jennifer Crombie and Ann LaCasce. The treatment of burkitt lymphoma in adults. Blood, 137:743-750, Feb 2021. URL: https://doi.org/10.1182/blood.2019004099, doi:10.1182/blood.2019004099. This article has 160 citations and is from a highest quality peer-reviewed journal.

3. (mburu2023incidenceofburkitt pages 1-3): Waruiru Mburu, Susan S. Devesa, David Check, Meredith S. Shiels, and Sam M. Mbulaiteye. Incidence of burkitt lymphoma in the united states during 2000 to 2019. International Journal of Cancer, 153:1182-1191, Jun 2023. URL: https://doi.org/10.1002/ijc.34618, doi:10.1002/ijc.34618. This article has 18 citations and is from a domain leading peer-reviewed journal.

4. (alkhreisat2023worldwideprevalenceof pages 1-2): Mutaz Jamal Al-Khreisat, Nor Hayati Ismail, Abedelmalek Tabnjh, Faezahtul Arbaeyah Hussain, Abdul Aziz Mohamed Yusoff, Muhammad Farid Johan, and Md Asiful Islam. Worldwide prevalence of epstein–barr virus in patients with burkitt lymphoma: a systematic review and meta-analysis. Diagnostics, 13:2068, Jun 2023. URL: https://doi.org/10.3390/diagnostics13122068, doi:10.3390/diagnostics13122068. This article has 22 citations.

5. (lakshmi2023endemicburkittlymphoma pages 1-2): Priya Saikumar Lakshmi, Cliff I Oduor, Catherine S Forconi, Viriato M’Bana, Courtney Bly, Rachel M Gerstein, Juliana A Otieno, John M Ong’echa, Christian Münz, Micah A Luftig, Michael A Brehm, Jeffrey A Bailey, and Ann M Moormann. Endemic burkitt lymphoma avatar mouse models for exploring inter-patient tumor variation and testing targeted therapies. Life Science Alliance, 6:e202101355, Mar 2023. URL: https://doi.org/10.26508/lsa.202101355, doi:10.26508/lsa.202101355. This article has 11 citations and is from a peer-reviewed journal.

6. (alkhreisat2023worldwideprevalenceof pages 2-3): Mutaz Jamal Al-Khreisat, Nor Hayati Ismail, Abedelmalek Tabnjh, Faezahtul Arbaeyah Hussain, Abdul Aziz Mohamed Yusoff, Muhammad Farid Johan, and Md Asiful Islam. Worldwide prevalence of epstein–barr virus in patients with burkitt lymphoma: a systematic review and meta-analysis. Diagnostics, 13:2068, Jun 2023. URL: https://doi.org/10.3390/diagnostics13122068, doi:10.3390/diagnostics13122068. This article has 22 citations.

7. (siddiqui2023fromthearchives pages 3-4): Saima Haleem Siddiqui, Beenu Thakral, FNU Aakash, Chi Young Ok, Zhenya Tang, and L. Jeffrey Medeiros. From the archives of md anderson cancer center: sporadic burkitt lymphoma with a complex karyotype and sox11 expression. Annals of Diagnostic Pathology, 66:152182, Oct 2023. URL: https://doi.org/10.1016/j.anndiagpath.2023.152182, doi:10.1016/j.anndiagpath.2023.152182. This article has 6 citations and is from a peer-reviewed journal.

8. (malfona2024refractoryburkittlymphoma pages 1-2): Francesco Malfona, Anna Maria Testi, Sabina Chiaretti, and Maria Luisa Moleti. Refractory burkitt lymphoma: diagnosis and interventional strategies. Blood and Lymphatic Cancer: Targets and Therapy, 14:1-15, Mar 2024. URL: https://doi.org/10.2147/blctt.s407804, doi:10.2147/blctt.s407804. This article has 19 citations.

9. (mburu2023incidenceofburkitt pages 3-5): Waruiru Mburu, Susan S. Devesa, David Check, Meredith S. Shiels, and Sam M. Mbulaiteye. Incidence of burkitt lymphoma in the united states during 2000 to 2019. International Journal of Cancer, 153:1182-1191, Jun 2023. URL: https://doi.org/10.1002/ijc.34618, doi:10.1002/ijc.34618. This article has 18 citations and is from a domain leading peer-reviewed journal.

10. (chamba2023clinicalapplicationof pages 1-2): Clara Chamba, Sam M. Mbulaiteye, Emmanuel Balandya, and Anna Schuh. Clinical application of circulating cell-free lymphoma dna for fast and precise diagnosis of burkitt lymphoma: precision medicine for sub-saharan africa. Cambridge Prisms: Precision Medicine, Jan 2023. URL: https://doi.org/10.1017/pcm.2023.1, doi:10.1017/pcm.2023.1. This article has 15 citations.

11. (coupland2024thefifthedition pages 12-12): Sarah E Coupland, Ming‐Qing Du, Judith A Ferry, Daphne de Jong, Joseph D Khoury, Lorenzo Leoncini, Kikkeri N Naresh, German Ott, Reiner Siebert, and Luc Xerri. The fifth edition of the who classification of mature b‐cell neoplasms: open questions for research. The Journal of Pathology, 262:255-270, Jan 2024. URL: https://doi.org/10.1002/path.6246, doi:10.1002/path.6246. This article has 23 citations.

12. (zanelli2024adiagnosticapproach pages 9-11): Magda Zanelli, Francesca Sanguedolce, Maurizio Zizzo, Stefano Ricci, Alessandra Bisagni, Andrea Palicelli, Valentina Fragliasso, Benedetta Donati, Giuseppe Broggi, Ioannis Boutas, Nektarios Koufopoulos, Moira Foroni, Francesca Coppa, Andrea Morini, Paola Parente, Valeria Zuccalà, Rosario Caltabiano, Massimiliano Fabozzi, Luca Cimino, Antonino Neri, and Stefano Ascani. A diagnostic approach in large b-cell lymphomas according to the fifth world health organization and international consensus classifications and a practical algorithm in routine practice. International Journal of Molecular Sciences, 25:13213, Dec 2024. URL: https://doi.org/10.3390/ijms252313213, doi:10.3390/ijms252313213. This article has 10 citations.

13. (crombie2021thetreatmentof pages 1-2): Jennifer Crombie and Ann LaCasce. The treatment of burkitt lymphoma in adults. Blood, 137:743-750, Feb 2021. URL: https://doi.org/10.1182/blood.2019004099, doi:10.1182/blood.2019004099. This article has 160 citations and is from a highest quality peer-reviewed journal.

14. (chamba2023clinicalapplicationof pages 2-3): Clara Chamba, Sam M. Mbulaiteye, Emmanuel Balandya, and Anna Schuh. Clinical application of circulating cell-free lymphoma dna for fast and precise diagnosis of burkitt lymphoma: precision medicine for sub-saharan africa. Cambridge Prisms: Precision Medicine, Jan 2023. URL: https://doi.org/10.1017/pcm.2023.1, doi:10.1017/pcm.2023.1. This article has 15 citations.

15. (harlendea2024ki67asa pages 2-4): Nicyela J Harlendea and Kent Harlendo. Ki-67 as a marker to differentiate burkitt lymphoma and diffuse large b-cell lymphoma: a literature review. Cureus, Oct 2024. URL: https://doi.org/10.7759/cureus.72190, doi:10.7759/cureus.72190. This article has 11 citations.

16. (tandon2023translocationtalesunraveling pages 16-17): Amol Tandon, Jissy Akkarapattiakal Kuriappan, and Vaibhav Dubey. Translocation tales: unraveling the myc deregulation in burkitt lymphoma for innovative therapeutic strategies. Lymphatics, 1:97-117, Jul 2023. URL: https://doi.org/10.3390/lymphatics1020010, doi:10.3390/lymphatics1020010. This article has 6 citations.

17. (lakshmi2023endemicburkittlymphoma pages 10-12): Priya Saikumar Lakshmi, Cliff I Oduor, Catherine S Forconi, Viriato M’Bana, Courtney Bly, Rachel M Gerstein, Juliana A Otieno, John M Ong’echa, Christian Münz, Micah A Luftig, Michael A Brehm, Jeffrey A Bailey, and Ann M Moormann. Endemic burkitt lymphoma avatar mouse models for exploring inter-patient tumor variation and testing targeted therapies. Life Science Alliance, 6:e202101355, Mar 2023. URL: https://doi.org/10.26508/lsa.202101355, doi:10.26508/lsa.202101355. This article has 11 citations and is from a peer-reviewed journal.

18. (chamba2023clinicalapplicationof pages 3-4): Clara Chamba, Sam M. Mbulaiteye, Emmanuel Balandya, and Anna Schuh. Clinical application of circulating cell-free lymphoma dna for fast and precise diagnosis of burkitt lymphoma: precision medicine for sub-saharan africa. Cambridge Prisms: Precision Medicine, Jan 2023. URL: https://doi.org/10.1017/pcm.2023.1, doi:10.1017/pcm.2023.1. This article has 15 citations.

19. (chamba2023clinicalapplicationof pages 4-5): Clara Chamba, Sam M. Mbulaiteye, Emmanuel Balandya, and Anna Schuh. Clinical application of circulating cell-free lymphoma dna for fast and precise diagnosis of burkitt lymphoma: precision medicine for sub-saharan africa. Cambridge Prisms: Precision Medicine, Jan 2023. URL: https://doi.org/10.1017/pcm.2023.1, doi:10.1017/pcm.2023.1. This article has 15 citations.

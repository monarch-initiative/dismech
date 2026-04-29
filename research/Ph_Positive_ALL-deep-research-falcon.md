---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T21:25:15.135105'
end_time: '2026-04-05T21:32:57.007423'
duration_seconds: 461.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Philadelphia Chromosome-Positive Acute Lymphoblastic Leukemia
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Philadelphia Chromosome-Positive Acute Lymphoblastic Leukemia
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Philadelphia Chromosome-Positive Acute Lymphoblastic Leukemia** covering all of the
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
- **Disease Name:** Philadelphia Chromosome-Positive Acute Lymphoblastic Leukemia
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Philadelphia Chromosome-Positive Acute Lymphoblastic Leukemia** covering all of the
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


# Philadelphia Chromosome–Positive Acute Lymphoblastic Leukemia (Ph+ ALL): Disease Characteristics Research Report (2026-04-06)

## Target Disease
- **Disease name:** Philadelphia chromosome–positive acute lymphoblastic leukemia (Ph+ ALL)
- **Category:** Hematologic malignancy; B-lymphoblastic leukemia/lymphoma subtype defined by **BCR::ABL1** fusion
- **Key molecular definition:** Presence of the **t(9;22)(q34;q11)** translocation producing the **BCR::ABL1** fusion tyrosine kinase (chiaretti2025howitreat pages 1-2, luskin2024ph+allnew pages 1-2).

---

## 1. Disease information
### 1.1 Concise overview (current understanding)
Philadelphia chromosome–positive ALL is a molecularly defined subtype of acute lymphoblastic leukemia characterized by constitutive ABL1 kinase signaling driven by the **BCR::ABL1** fusion (luskin2024ph+allnew pages 1-2, foa2025phpositiveacutelymphoblastic pages 1-2). It is the **most common genetic subgroup in adult ALL** and becomes more frequent with increasing age (luskin2024ph+allnew pages 1-2, foa2025phpositiveacutelymphoblastic pages 1-2).

**Abstract-supported definitions (direct quotes)**
- Luskin (ASH Education Program, 2024-12; DOI: https://doi.org/10.1182/hematology.2024000532) states: **“Ph+ ALL is characterized by the constitutively active ABL1 kinase”** (luskin2024ph+allnew pages 1-2).
- Chiaretti & Foà (Blood, 2025-01; DOI: https://doi.org/10.1182/blood.2023023152) describe this as a causal lesion with proven causality and note that Ph+ ALL is a major adult ALL subgroup with improved outcomes due to TKIs and immunotherapy (chiaretti2025howitreat pages 1-2).

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
Using the currently retrieved full-text sources, **specific OMIM/Orphanet/ICD-10/ICD-11/MeSH/MONDO IDs were not explicitly provided** in the accessible excerpts (chiaretti2025howitreat pages 1-2, luskin2024ph+allnew pages 1-2, foa2025phpositiveacutelymphoblastic pages 1-2, gokbuget2024diagnosisprognosticfactors pages 6-7).

**Pragmatic mapping (commonly used in clinical systems; not verified in-tool here):**
- ICD-10 for ALL is commonly **C91.0** (Acute lymphoblastic leukemia) and Ph+ status is typically captured as a molecular/cytogenetic qualifier rather than a separate ICD-10 code; however, this report **does not assert a specific Ph+ ALL ICD subcode** without direct source evidence.

### 1.3 Synonyms / alternative names
Commonly used synonyms in the retrieved literature include:
- **Ph-positive ALL / Ph+ ALL** (foa2024longtermresultsof pages 2-3, foa2025phpositiveacutelymphoblastic pages 1-2)
- **BCR::ABL1-positive ALL** (luskin2024ph+allnew pages 1-2, gokbuget2024diagnosisprognosticfactors pages 6-7)
- **Philadelphia chromosome (Ph)–positive B-cell precursor ALL** (kantarjian2024resultsofthe pages 3-4)

### 1.4 Evidence provenance
Most information here is derived from:
- **Aggregated disease-level resources** (expert reviews and consensus recommendations) (foa2025phpositiveacutelymphoblastic pages 1-2, gokbuget2024diagnosisprognosticfactors pages 8-9)
- **Prospective clinical trials** (frontline targeted/immunotherapy combinations) (kantarjian2024resultsofthe pages 1-3, foa2024longtermresultsof pages 2-3, chiaretti2025howitreat pages 1-2)
- **ClinicalTrials.gov registry records** (trial design and endpoints) (NCT04722848 chunk 1, NCT06308588 chunk 1, NCT06061094 chunk 1)

---

## 2. Etiology
### 2.1 Primary causal factors
- **Genetic driver:** The defining causal lesion is **t(9;22)(q34;q11)** leading to **BCR::ABL1** fusion (chiaretti2025howitreat pages 1-2, luskin2024ph+allnew pages 1-2).
- **Fusion isoforms:** BCR::ABL1 can produce **p190** (typical in Ph+ ALL) and **p210** (more typical of CML), with rarer p230 (chiaretti2025howitreat pages 1-2, luskin2024ph+allnew pages 1-2).

### 2.2 Risk factors
- **Age:** Incidence increases with age; Ph+ ALL is rare in childhood and can be detected in **>50% of patients >50 years** in at least one expert perspective (chiaretti2025howitreat pages 1-2), and a NEJM review reports ~50% of B-lineage ALL in patients >50 years (foa2025phpositiveacutelymphoblastic pages 1-2).

### 2.3 Protective factors
No protective genetic variants or environmental protective factors were identified in the retrieved excerpts.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence specific to Ph+ ALL was identified in the retrieved excerpts.

---

## 3. Phenotypes (clinical presentation)
The retrieved excerpts focus primarily on molecular definition, response assessment, and outcomes; detailed symptom frequency tables were not present in the captured text. Ph+ ALL clinically presents as an acute leukemia syndrome, and key disease features relevant to knowledge-base entry include:

### 3.1 Common clinical/laboratory phenotypes (with suggested HPO terms)
1. **Elevated white blood cell count (leukocytosis)**
   - Prognostic relevance: high WBC is a risk feature; in ponatinib+blinatumomab, WBC >75×10^9/L correlated with more systemic/CNS relapse (kantarjian2024resultsofthe pages 3-4).
   - HPO: **HP:0001909 (Leukocytosis)**

2. **Central nervous system (CNS) involvement / relapse**
   - CNS relapse was prominent in chemo-free regimens: isolated CNS relapses occurred in 4/7 relapses with ponatinib+blinatumomab (kantarjian2024resultsofthe pages 1-3).
   - ELN risk factors include CNS involvement (gokbuget2024diagnosisprognosticfactors pages 7-8).
   - HPO: **HP:0002060 (CNS involvement)** (broad), **HP:0002315 (Headache)** (if symptomatic; not quantified here)

3. **Bone marrow blasts / acute leukemia morphology**
   - Response definitions emphasize marrow evaluation and enumeration (gokbuget2024diagnosisprognosticfactors pages 23-24).
   - HPO: **HP:0005528 (Increased blast cells in bone marrow)**

4. **Measurable residual disease (MRD) positivity/negativity as a laboratory phenotype**
   - HPO does not standardly encode MRD, but a KB entry can model MRD status as a disease monitoring attribute.

### 3.2 Quality of life impact
Not directly quantified in retrieved sources; however, the field motivation includes minimizing chemotherapy and transplant morbidity through chemo-free/chemo-light regimens (luskin2024ph+allnew pages 1-2, foa2025phpositiveacutelymphoblastic pages 1-2).

---

## 4. Genetic / molecular information
### 4.1 Causal genes and chromosomal abnormalities
- **Chromosomal abnormality:** **t(9;22)(q34;q11)** (Philadelphia chromosome) (chiaretti2025howitreat pages 1-2, luskin2024ph+allnew pages 1-2)
- **Causal fusion:** **BCR::ABL1** (BCR + ABL1) (luskin2024ph+allnew pages 1-2)
- **Mechanistic consequence:** constitutively active **ABL1 tyrosine kinase** (luskin2024ph+allnew pages 1-2, foa2025phpositiveacutelymphoblastic pages 1-2)

### 4.2 Co-operating lesions / prognostic genomics
- **IKZF1 deletions** are frequent in Ph+ and Ph-like cases (~80% noted in ELN excerpt) (gokbuget2024diagnosisprognosticfactors pages 6-7).
- **IKZF1-plus genotype** (IKZF1 deletion plus CDKN2A/B and/or PAX5 deletions) is a recognized adverse category used in some trials and associated with worse outcomes in D-ALBA (foa2024longtermresultsof pages 2-3, gokbuget2024diagnosisprognosticfactors pages 6-7).
- Additional recurrent copy-number losses include **CDKN2A/B** and **PAX5** (luskin2024ph+allnew pages 1-2, gokbuget2024diagnosisprognosticfactors pages 6-7).

### 4.3 Resistance mutations
- **ABL1 kinase domain mutations** can emerge at relapse; examples reported include **T315I** and **E255K/E255V** (foa2024longtermresultsof pages 2-3, kantarjian2024resultsofthe pages 3-4).
- Ponatinib is highlighted as active against **T315I** in the review context (luskin2024ph+allnew pages 1-2).

### 4.4 Suggested ontology annotations
- **HGNC genes:** ABL1, BCR, IKZF1, CDKN2A, CDKN2B, PAX5
- **GO biological processes (suggested):**
  - GO:0007169 (transmembrane receptor protein tyrosine kinase signaling pathway) (proximal concept)
  - GO:0008283 (cell population proliferation)
  - GO:0006915 (apoptotic process) (downstream dysregulation)
- **Cell Ontology (suggested):**
  - CL:0000236 (B cell)
  - CL:0000946 (B lymphoblast)
  - CL:0000051 (hematopoietic stem cell) (for multilineage involvement discussion)

---

## 5. Mechanism / pathophysiology
### 5.1 Causal chain (high-level)
1. **Initiating event:** t(9;22) creates **BCR::ABL1** fusion (chiaretti2025howitreat pages 1-2, luskin2024ph+allnew pages 1-2).
2. **Upstream driver:** constitutive **ABL1 kinase activity** (luskin2024ph+allnew pages 1-2, foa2025phpositiveacutelymphoblastic pages 1-2).
3. **Downstream effects:** enhanced proliferation/survival of lymphoid progenitors, altered differentiation, and treatment resistance to conventional chemotherapy (luskin2024ph+allnew pages 1-2).
4. **Clinical manifestation:** acute leukemia with high blast burden; measurable disease in marrow/blood and risk for extramedullary disease including CNS (kantarjian2024resultsofthe pages 1-3, kantarjian2024resultsofthe pages 3-4).

### 5.2 Key mechanistic concepts relevant to therapy
- TKIs directly inhibit the fusion kinase and have “markedly improved the prognosis” and enabled high CR rates even with limited chemotherapy (foa2025phpositiveacutelymphoblastic pages 1-2, shanmuganathan2026acriticalreview pages 1-2).
- The modern strategy emphasizes deep molecular remission (CMR/MRD negativity) as a goal and as a major prognostic factor (foa2025phpositiveacutelymphoblastic pages 1-2, gokbuget2024diagnosisprognosticfactors pages 9-10).

---

## 6. Anatomical structures affected (with UBERON suggestions)
- **Primary:** bone marrow (UBERON:0002371), peripheral blood (UBERON:0000178) (implied in ALL diagnostics and MRD sampling) (gokbuget2024diagnosisprognosticfactors pages 23-24, gokbuget2024diagnosisprognosticfactors pages 9-10).
- **Secondary/extramedullary:** CNS (UBERON:0001017) given observed isolated CNS relapses in chemo-free regimens (kantarjian2024resultsofthe pages 1-3).

---

## 7. Temporal development
- **Onset pattern:** acute (typical of ALL; implied by diagnostic response timepoints and induction frameworks) (gokbuget2024diagnosisprognosticfactors pages 9-10).
- **Response dynamics:** MRD thresholds are assessed early (weeks 4–6 end of induction; weeks ~10–16 post-consolidation) and integrated into risk stratification (gokbuget2024diagnosisprognosticfactors pages 8-9).

---

## 8. Inheritance and population
### 8.1 Inheritance
Ph+ ALL is a **somatic** malignancy driven by an acquired chromosomal translocation (t(9;22)) rather than classic Mendelian inheritance (chiaretti2025howitreat pages 1-2, luskin2024ph+allnew pages 1-2).

### 8.2 Epidemiology / demographics
- Ph+ ALL is **the most frequent genetic subgroup in adult ALL** (chiaretti2025howitreat pages 1-2).
- Incidence increases with age; NEJM review notes about **50% of B-lineage ALL in patients >50 years** (foa2025phpositiveacutelymphoblastic pages 1-2).

Registry-derived incidence/prevalence (SEER/GBD) was not directly retrievable from the current tool evidence set and is therefore not reported here.

---

## 9. Diagnostics
### 9.1 Diagnostic testing for BCR::ABL1
The 2024 ELN recommendations explicitly list the conventional modalities used for genetic characterization:
- **Conventional cytogenetics (karyotype)**
- **FISH**
- **RT-PCR**, with emphasis on rapid detection of **t(9;22)/BCR::ABL1** (gokbuget2024diagnosisprognosticfactors pages 6-7).

### 9.2 MRD testing (methods, definitions, and thresholds)
The ELN 2024 recommendations emphasize **universal MRD testing** and specify major methods and performance characteristics:
- **Multiparameter flow cytometry (MFC):** sensitivity ~0.1–0.01% (10^-3 to 10^-4), applicable to >90% cases (gokbuget2024diagnosisprognosticfactors pages 7-8).
- **Fusion-gene molecular monitoring (e.g., BCR::ABL1 by RQ-PCR):** sensitivity ~0.01% and standardization via EuroMRD (gokbuget2024diagnosisprognosticfactors pages 7-8).
- **Complete MRD response definition:** **“no detectable MRD with a minimum sensitivity of 0.01%”** at that timepoint (gokbuget2024diagnosisprognosticfactors pages 9-10).
- **Recommended timing thresholds (typical in studies):** <0.1% to <0.01% at end of induction (weeks 4–6) and <0.01% after 1–3 early consolidation courses (weeks ~10–16) (gokbuget2024diagnosisprognosticfactors pages 8-9).
- For **Ph+ ALL**, ELN advises using **BCR::ABL1-based MRD together with an additional method (MFC or IG/TR PCR)** when making MRD-based treatment decisions (gokbuget2024diagnosisprognosticfactors pages 10-11).

### 9.3 Differential diagnosis
Not systematically extractable from current excerpts; clinically, differential includes Ph-like ALL and other B-ALL genetic subtypes (Ph-like mentioned as an adverse-risk subgroup in modern classifications) (gokbuget2024diagnosisprognosticfactors pages 8-9, gokbuget2024diagnosisprognosticfactors pages 6-7).

---

## 10. Outcomes / prognosis
### 10.1 Historical vs contemporary prognosis (expert synthesis)
The introduction of TKIs and subsequent integration of immunotherapy has shifted Ph+ ALL from historically poor outcomes to long-term survival in many patients.
- NEJM review indicates that chemo-free TKI induction can achieve **94–100% hematologic complete responses** and that addition of blinatumomab improved molecular responses and survival, with long-term survival ~75–80% (foa2025phpositiveacutelymphoblastic pages 1-2).
- A Blood “How I treat” perspective similarly reports long-term survival rates **“currently ranging between 75 and 80%”** in the modern era (chiaretti2025howitreat pages 1-2).

### 10.2 Recent statistics from prospective frontline studies (2023–2024 prioritized)
- **Ponatinib + blinatumomab (JCO 2024-12-20, DOI: https://doi.org/10.1200/JCO.24.00272):**
  - CMR (RT-PCR) 83% overall; NGS MRD negativity 98%; **3-year OS 91%**, **3-year EFS 77%**; low transplant utilization (2 patients) (kantarjian2024resultsofthe pages 1-3, kantarjian2024resultsofthe pages 3-4).
- **Dasatinib + blinatumomab (D-ALBA; JCO 2024-03-10, DOI: https://doi.org/10.1200/JCO.23.01075):**
  - At median follow-up 53 months: **OS 80.7%**, **DFS 75.8%**, **EFS 74.6%**; significantly worse outcomes in IKZF1plus patients (foa2024longtermresultsof pages 2-3).
- **Older adults (>=65) dasatinib/prednisone → blinatumomab/dasatinib (Blood Advances 2023-03-xx, DOI: https://doi.org/10.1182/bloodadvances.2022008216):**
  - **3-year OS 87%** and **3-year DFS 77%**; feasible with CNS prophylaxis (chiaretti2025howitreat pages 1-2).

---

## 11. Treatment
### 11.1 Current treatment concepts (real-world implementation)
The contemporary approach increasingly uses **TKI + immunotherapy (blinatumomab)** to reduce or omit intensive chemotherapy and to reduce reliance on allogeneic transplant in first remission, particularly for deep molecular responders (foa2025phpositiveacutelymphoblastic pages 1-2, foa2024longtermresultsof pages 2-3).

### 11.2 Key drug classes and mechanisms
- **TKIs (target BCR::ABL1 kinase):** imatinib (1st gen), dasatinib/nilotinib (2nd gen), ponatinib (3rd gen; active vs T315I) (luskin2024ph+allnew pages 1-2, chiaretti2025howitreat pages 1-2).
- **Blinatumomab:** CD3×CD19 bispecific T-cell engager, used in frontline chemo-free regimens and in relapsed/refractory disease (csizmar2025antibodybasedandother pages 16-18, kantarjian2024resultsofthe pages 1-3).
- **Inotuzumab ozogamicin:** anti-CD22 antibody-drug conjugate used in R/R settings (subgroup data summarized) (csizmar2025antibodybasedandother pages 16-18).

### 11.3 Frontline regimens (2023–2024 evidence prioritized)
| Regimen | Study/design | N | Population | Key efficacy endpoints | Survival / follow-up | Notable relapse patterns | Key safety notes | Year | URL / DOI | Citation |
|---|---|---:|---|---|---|---|---|---:|---|---|
| Ponatinib + blinatumomab (simultaneous, chemotherapy-free; with intrathecal CNS prophylaxis) | MD Anderson prospective phase II update in newly diagnosed Ph+ ALL | 60 | Newly diagnosed adult Ph+ ALL; only 2 patients proceeded to HSCT | CR 97% among untreated patients; RT-PCR complete molecular response (CMR) 83% overall, 67% by end of course 1; NGS MRD negativity 98% overall, 45% by end of course 1 | 3-year OS 91%; 3-year EFS 77%; median follow-up 24 months | 7 relapses: 2 systemic, 4 isolated CNS, 1 extramedullary Ph-negative/CRLF2-positive pre-B ALL; high presenting WBC associated with more CNS relapse | Blinatumomab discontinued in 3; ponatinib discontinued in 9 for vascular/organ toxicities; CRS mostly grade 1-2; neurotoxicity mostly grade 1-2 | 2024 | https://doi.org/10.1200/JCO.24.00272 | (kantarjian2024resultsofthe pages 1-3, kantarjian2024resultsofthe pages 3-4) |
| Dasatinib induction/consolidation + blinatumomab (D-ALBA) | GIMEMA LAL2116 frontline trial, long-term update | 63 | Adult Ph+ ALL, all ages enrolled | Early molecular responders had no subsequent events; in a no-chemo/no-transplant subgroup, 27/29 (93.1%) achieved molecular response after dasatinib/blinatumomab; 20 after 2 blinatumomab cycles, 7 after additional cycles | DFS 75.8%; OS 80.7%; EFS 74.6%; median follow-up 53 months | 9 relapses overall; worse outcome in IKZF1plus patients; ABL1 mutations detected in 7 cases; recurrence earlier in p190 than p210 in reported subgroup analysis | Transplant-related mortality 12.5% in patients transplanted in first CHR; overall regimen described as effective and durable with many patients avoiding chemotherapy/transplant | 2024 | https://doi.org/10.1200/JCO.23.01075 | (foa2024longtermresultsof pages 2-3) |
| Dasatinib/prednisone induction followed by blinatumomab + dasatinib; maintenance dasatinib/prednisone | Multicenter trial in older patients (SWOG backbone) | 24 | Newly diagnosed Ph+ ALL in patients age >=65 years; median age 73 years | Regimen reported as safe and feasible; response assessed serially with centralized MRD by 8-color flow at day 28 | 3-year OS 87%; 3-year DFS 77%; median follow-up 2.7 years | Relapse pattern not detailed in extracted evidence | CNS prophylaxis with 8 doses intrathecal methotrexate; safety described as encouraging/feasible in older adults | 2023 | https://doi.org/10.1182/bloodadvances.2022008216 | (chiaretti2025howitreat pages 1-2) |
| Ponatinib vs imatinib with reduced-intensity chemotherapy (PhALLCON endpoint summary) | Randomized frontline comparison summarized in Hematology review | Not stated in extracted evidence | Newly diagnosed adult Ph+ ALL | Composite primary endpoint met: CR + MRD negativity (BCR::ABL1 MR4) by 3 months 34.4% with ponatinib vs 16.7% with imatinib (p=0.002) | At 20.1 months, EFS trended in favor of ponatinib (HR 0.65); no OS difference reported in extracted summary | Resistance concern centered on kinase-domain mutations such as T315I; ponatinib retains activity against T315I | Vascular toxicity remains an important ponatinib concern | 2024 | https://doi.org/10.1182/hematology.2024000532 | (luskin2024ph+allnew pages 1-2) |
| Sequential ponatinib followed by blinatumomab vs chemotherapy + imatinib (ALL2820) | Randomized open-label multicenter phase III trial, 2:1 randomization | 236 planned | Newly diagnosed adult B-precursor Ph+ ALL | Primary endpoint: event-free survival rate at 5 months; experimental arm gives ponatinib then minimum 2 to maximum 5 blinatumomab cycles | Ongoing; no mature efficacy results in extracted registry evidence | Control-arm crossover permitted for lack of CHR/MRD negativity or emergence of ABL1 mutations | Eligibility requires adequate organ function and no CNS leukemia at blinatumomab start | 2021 registry / ongoing | https://clinicaltrials.gov/study/NCT04722848 | (NCT04722848 chunk 1) |
| Blinatumomab + ponatinib + intrathecal methotrexate/cytarabine | MD Anderson phase II single-group trial | 90 planned | Adults with newly diagnosed or relapsed/refractory Ph+/BCR-ABL1+ ALL | Primary endpoints include CMR rate at 18 weeks in newly diagnosed Ph+ ALL and ORR (CR+CRi) at 12 weeks in relapsed/refractory disease; secondary endpoints include RFS, EFS, OS | Ongoing in registry; mature published frontline update reported separately above | Exploratory objectives include ABL1 kinase-domain mutations, genomic predictors of relapse, NGS MRD | Eligibility excludes uncontrolled infection and major cardiac/CNS comorbidity | 2017 registry / ongoing | https://clinicaltrials.gov/study/NCT03263572 | (NCT03263572 chunk 1, NCT03263572 chunk 2) |
| Blinatumomab + asciminib | Phase I/II single-group trial | 40 planned | Adults with newly diagnosed/minimally pretreated Ph+ ALL not fit for intensive chemotherapy, or patients >=12 years with relapsed/refractory Ph+ ALL | Phase I: define safe/biologically effective asciminib dose with blinatumomab; Phase II: NGS MRD negativity by clonoSEQ in newly diagnosed cohort and CR+CRi in relapsed/refractory cohort; secondary endpoints include CMR, CR, RFS, OS | Ongoing; no mature efficacy results in extracted registry evidence | Relapse patterns not yet available | Primary focus includes AE assessment per CTCAE v5.0; key cardiac/infectious exclusions apply | 2024 registry | https://clinicaltrials.gov/study/NCT06308588 | (NCT06308588 chunk 1) |
| Asciminib + dasatinib + prednisone + methotrexate induction; blinatumomab/dasatinib-based re-induction-post-remission; asciminib/dasatinib/prednisone maintenance | SWOG phase II non-randomized sequential trial | 55 planned | Adults with newly diagnosed Ph+ ALL | Primary endpoint: major molecular remission (MMR/MR3.0; BCR-ABL <=0.1% by PCR) at day 85; secondary endpoints include CR/CRi, DFS, OS, MRD by flow, MR4.0 duration, EFS | Ongoing; no mature efficacy results in extracted registry evidence | Translational endpoints include mutation spectrum and response pathways | AE incidence/severity tracked across induction, post-remission, and long maintenance | 2026 registry entry | https://clinicaltrials.gov/study/NCT06773936 | (NCT06773936 chunk 1) |
| Ponatinib vs imatinib, each with low-dose chemotherapy; blinatumomab added for molecular failure/intermediate response and for some molecular CR patients | GMALL-EVOLVE randomized open-label phase II | 220 planned | Adults age 18-65 with de novo Ph+/BCR-ABL1+ ALL | Primary endpoint in molecular CR patients: OS up to 4 years comparing TKI+chemo+blinatumomab vs end-of-therapy with indication for SCT; secondary endpoints include molecular CR rate at week 11, MRD kinetics/log reduction, relapse incidence, RFS | Ongoing; no mature efficacy results in extracted registry evidence | Designed to study MRD-directed allocation, relapse incidence, and the role of SCT | AE incidence/severity and TKI dose modifications captured prospectively | 2023 registry | https://clinicaltrials.gov/study/NCT06061094 | (NCT06061094 chunk 1) |


*Table: This table summarizes key 2023-2024 frontline treatment evidence and active trial designs for Philadelphia chromosome-positive acute lymphoblastic leukemia, emphasizing chemo-free or chemo-light regimens, molecular response depth, survival outcomes, relapse patterns, and safety.*

**Visual evidence (Kaplan–Meier curves and response table):** In the JCO 2024 ponatinib+blinatumomab update, Figures 2A/2B show EFS/OS and Table 2 summarizes molecular response metrics and survival estimates (kantarjian2024resultsofthe media aadc8e08, kantarjian2024resultsofthe media b753f7a6, kantarjian2024resultsofthe media 5938646a).

### 11.4 Selected adverse events (treatment trade-offs)
- Ponatinib discontinuations due to vascular/organ toxicities were reported in the JCO 2024 update (kantarjian2024resultsofthe pages 1-3).
- Chemo + TKI regimens historically carried toxic death risks (reported as 1–5% in a narrative context) (chiaretti2025howitreat pages 1-2).

### 11.5 Suggested MAXO terms (examples)
- **Tyrosine kinase inhibitor therapy** (MAXO: drug therapy category; suggest “tyrosine kinase inhibitor therapy”)
- **Blinatumomab therapy / bispecific antibody therapy**
- **Allogeneic hematopoietic stem cell transplantation**
- **Intrathecal chemotherapy prophylaxis** (for CNS prophylaxis)

---

## 12. Prevention
- **Primary prevention:** No established primary prevention strategies are supported in the retrieved excerpts (somatic oncogenic event).
- **Secondary/tertiary prevention:** MRD monitoring to enable early therapeutic escalation and CNS prophylaxis are central implementation concepts (gokbuget2024diagnosisprognosticfactors pages 8-9, kantarjian2024resultsofthe pages 1-3).

---

## 13. Recent developments and ongoing clinical trials (2023–2024 prioritized)
Key ongoing or recently launched trials emphasize **chemo-free/chemo-light** regimens and **next-generation ABL inhibition (asciminib)**:
- **NCT04722848 (ALL2820; Phase 3):** ponatinib → blinatumomab vs chemotherapy+imatinib; primary endpoint EFS at 5 months (ClinicalTrials.gov; first posted 2021; URL: https://clinicaltrials.gov/study/NCT04722848) (NCT04722848 chunk 1).
- **NCT06308588 (Phase I/II):** blinatumomab + asciminib; Phase II includes NGS MRD negativity by clonoSEQ in newly diagnosed cohort (ClinicalTrials.gov; 2024; URL: https://clinicaltrials.gov/study/NCT06308588) (NCT06308588 chunk 1).
- **NCT03263572 (Phase II):** blinatumomab + ponatinib with intrathecal MTX/cytarabine; endpoints include CMR at 18 weeks, EFS/OS up to 6 years (ClinicalTrials.gov; 2017; URL: https://clinicaltrials.gov/study/NCT03263572) (NCT03263572 chunk 1, NCT03263572 chunk 2).
- **NCT06061094 (GMALL-EVOLVE; Phase 2):** ponatinib vs imatinib with low-dose chemotherapy; blinatumomab add-on driven by molecular response (ClinicalTrials.gov; 2023; URL: https://clinicaltrials.gov/study/NCT06061094) (NCT06061094 chunk 1).
- **NCT06773936 (SWOG; Phase 2):** adds asciminib to a dasatinib/blinatumomab-containing backbone; primary endpoint MMR (MR3.0) at day 85 (ClinicalTrials.gov; 2026 listing; URL: https://clinicaltrials.gov/study/NCT06773936) (NCT06773936 chunk 1).

---

## 14. Model organisms and model systems
Ph+ ALL has been modeled extensively in mice using BCR-ABL isoforms.
- **Transgenic mouse models:** BCR/ABL **p210 and p190 cause distinct leukemia** in transgenic mice, supporting isoform-specific biology and disease phenotypes (Blood, 1995; DOI: https://doi.org/10.1182/blood.v86.12.4603.bloodjournal86124603) (not evidence-extracted in detail here due to tool focus, but retrieved in corpus).
- Reviews of murine acute leukemia models emphasize that transgenic p190 BCR-ABL expression has been used to model ALL, with strengths/limitations versus xenografts (pqac context: model-systems retrieval occurred but no focused evidence ID was generated beyond retrieval; therefore not cited as a mechanistic claim here).

---

## Limitations of this report (evidence availability)
1. **Ontology identifiers (MONDO/MeSH/ICD/Orphanet/OMIM):** not present in retrieved excerpts; this report cannot provide verified IDs without additional database queries or documents explicitly listing them.
2. **Population incidence/prevalence statistics:** registry-based numbers (SEER/GBD) were not retrieved by the current tool calls.
3. **Symptom frequencies and quality-of-life instruments:** not present in the accessible excerpts of the retrieved papers.

---

## Key sources (URLs and publication dates)
- Kantarjian et al. *J Clin Oncol* (2024-12). “Ponatinib + blinatumomab” update. https://doi.org/10.1200/JCO.24.00272 (kantarjian2024resultsofthe pages 1-3, kantarjian2024resultsofthe pages 3-4)
- Foà et al. *J Clin Oncol* (2024-03). D-ALBA long-term results. https://doi.org/10.1200/JCO.23.01075 (foa2024longtermresultsof pages 2-3)
- Advani et al. *Blood Advances* (2023-03). Dasatinib/prednisone → blinatumomab/dasatinib in older adults; NCT02143414. https://doi.org/10.1182/bloodadvances.2022008216 (chiaretti2025howitreat pages 1-2)
- Gökbuget et al. *Blood* (2024-05). ELN recommendations: diagnosis, prognostic factors, MRD. https://doi.org/10.1182/blood.2023020794 (gokbuget2024diagnosisprognosticfactors pages 6-7, gokbuget2024diagnosisprognosticfactors pages 9-10)
- Foà. *N Engl J Med* (2025-05). “25 years of progress” review. https://doi.org/10.1056/NEJMra2405573 (foa2025phpositiveacutelymphoblastic pages 1-2)
- ClinicalTrials.gov: NCT04722848, NCT06308588, NCT03263572, NCT06061094, NCT06773936 (NCT04722848 chunk 1, NCT06308588 chunk 1, NCT03263572 chunk 1, NCT06061094 chunk 1, NCT06773936 chunk 1)


References

1. (chiaretti2025howitreat pages 1-2): Sabina Chiaretti and Robin Foà. How i treat adult ph+ all. Blood, 145:11-19, Jan 2025. URL: https://doi.org/10.1182/blood.2023023152, doi:10.1182/blood.2023023152. This article has 8 citations and is from a highest quality peer-reviewed journal.

2. (luskin2024ph+allnew pages 1-2): Marlise R. Luskin. Ph+ all: new approaches for upfront therapy. Hematology, 2024:78-85, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000532, doi:10.1182/hematology.2024000532. This article has 9 citations and is from a peer-reviewed journal.

3. (foa2025phpositiveacutelymphoblastic pages 1-2): Robin Foà. Ph-positive acute lymphoblastic leukemia - 25 years of progress. The New England journal of medicine, 392 19:1941-1952, May 2025. URL: https://doi.org/10.1056/nejmra2405573, doi:10.1056/nejmra2405573. This article has 14 citations and is from a highest quality peer-reviewed journal.

4. (gokbuget2024diagnosisprognosticfactors pages 6-7): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Diagnosis, prognostic factors, and assessment of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1891-1902, May 2024. URL: https://doi.org/10.1182/blood.2023020794, doi:10.1182/blood.2023020794. This article has 95 citations and is from a highest quality peer-reviewed journal.

5. (foa2024longtermresultsof pages 2-3): Robin Foà, Renato Bassan, Loredana Elia, Alfonso Piciocchi, Stefano Soddu, Monica Messina, Felicetto Ferrara, Monia Lunghi, Antonino Mulè, Massimiliano Bonifacio, Nicola Fracchiolla, Prassede Salutari, Paola Fazi, Anna Guarini, Alessandro Rambaldi, and Sabina Chiaretti. Long-term results of the dasatinib-blinatumomab protocol for adult philadelphia-positive all. Journal of Clinical Oncology, 42:881-885, Mar 2024. URL: https://doi.org/10.1200/jco.23.01075, doi:10.1200/jco.23.01075. This article has 162 citations and is from a highest quality peer-reviewed journal.

6. (kantarjian2024resultsofthe pages 3-4): Hagop Kantarjian, Nicholas J. Short, Fadi G. Haddad, Nitin Jain, Xuelin Huang, Guillermo Montalban-Bravo, Rashmi Kanagal-Shamanna, Tapan M. Kadia, Naval Daver, Kelly Chien, Yesid Alvarado, Guillermo Garcia-Manero, Ghayas C. Issa, Rebecca Garris, Cedric Nasnas, Lewis Nasr, Farhad Ravandi, and Elias Jabbour. Results of the simultaneous combination of ponatinib and blinatumomab in philadelphia chromosome-positive all. Journal of Clinical Oncology, 42:4246-4251, Dec 2024. URL: https://doi.org/10.1200/jco.24.00272, doi:10.1200/jco.24.00272. This article has 74 citations and is from a highest quality peer-reviewed journal.

7. (gokbuget2024diagnosisprognosticfactors pages 8-9): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Diagnosis, prognostic factors, and assessment of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1891-1902, May 2024. URL: https://doi.org/10.1182/blood.2023020794, doi:10.1182/blood.2023020794. This article has 95 citations and is from a highest quality peer-reviewed journal.

8. (kantarjian2024resultsofthe pages 1-3): Hagop Kantarjian, Nicholas J. Short, Fadi G. Haddad, Nitin Jain, Xuelin Huang, Guillermo Montalban-Bravo, Rashmi Kanagal-Shamanna, Tapan M. Kadia, Naval Daver, Kelly Chien, Yesid Alvarado, Guillermo Garcia-Manero, Ghayas C. Issa, Rebecca Garris, Cedric Nasnas, Lewis Nasr, Farhad Ravandi, and Elias Jabbour. Results of the simultaneous combination of ponatinib and blinatumomab in philadelphia chromosome-positive all. Journal of Clinical Oncology, 42:4246-4251, Dec 2024. URL: https://doi.org/10.1200/jco.24.00272, doi:10.1200/jco.24.00272. This article has 74 citations and is from a highest quality peer-reviewed journal.

9. (NCT04722848 chunk 1):  Sequential Treatment With Ponatinib and Blinatumomab vs Chemotherapy and Imatinib in Newly Diagnosed Adult Ph+ ALL. Gruppo Italiano Malattie EMatologiche dell'Adulto. 2021. ClinicalTrials.gov Identifier: NCT04722848

10. (NCT06308588 chunk 1):  Phase I/II Study of the Combination of Blinatumomab and Asciminib in Patients With Philadelphia Chromosome-Positive Acute Lymphoblastic Leukemia. M.D. Anderson Cancer Center. 2024. ClinicalTrials.gov Identifier: NCT06308588

11. (NCT06061094 chunk 1): Nicola Goekbuget. Randomized Trial in Adult de Novo Ph Positive ALL With Chemotherapy, Imatinib or Ponatinib, Blinatumomab and SCT. Goethe University. 2023. ClinicalTrials.gov Identifier: NCT06061094

12. (gokbuget2024diagnosisprognosticfactors pages 7-8): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Diagnosis, prognostic factors, and assessment of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1891-1902, May 2024. URL: https://doi.org/10.1182/blood.2023020794, doi:10.1182/blood.2023020794. This article has 95 citations and is from a highest quality peer-reviewed journal.

13. (gokbuget2024diagnosisprognosticfactors pages 23-24): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Diagnosis, prognostic factors, and assessment of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1891-1902, May 2024. URL: https://doi.org/10.1182/blood.2023020794, doi:10.1182/blood.2023020794. This article has 95 citations and is from a highest quality peer-reviewed journal.

14. (shanmuganathan2026acriticalreview pages 1-2): Naranie Shanmuganathan and Andrew Grigg. A critical review of management of allogeneic transplant-eligible adults with ph+ acute lymphoblastic leukaemia. British journal of haematology, Sep 2026. URL: https://doi.org/10.1111/bjh.19682, doi:10.1111/bjh.19682. This article has 3 citations and is from a domain leading peer-reviewed journal.

15. (gokbuget2024diagnosisprognosticfactors pages 9-10): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Diagnosis, prognostic factors, and assessment of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1891-1902, May 2024. URL: https://doi.org/10.1182/blood.2023020794, doi:10.1182/blood.2023020794. This article has 95 citations and is from a highest quality peer-reviewed journal.

16. (gokbuget2024diagnosisprognosticfactors pages 10-11): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Diagnosis, prognostic factors, and assessment of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1891-1902, May 2024. URL: https://doi.org/10.1182/blood.2023020794, doi:10.1182/blood.2023020794. This article has 95 citations and is from a highest quality peer-reviewed journal.

17. (csizmar2025antibodybasedandother pages 16-18): Clifford M. Csizmar, Mark R. Litzow, and Antoine N. Saliba. Antibody-based and other novel agents in adult b-cell acute lymphoblastic leukemia. Cancers, 17:779, Feb 2025. URL: https://doi.org/10.3390/cancers17050779, doi:10.3390/cancers17050779. This article has 1 citations.

18. (NCT03263572 chunk 1):  Blinatumomab, Methotrexate, Cytarabine, and Ponatinib in Treating Patients With Philadelphia Chromosome-Positive, or BCR-ABL Positive, or Relapsed/Refractory, Acute Lymphoblastic Leukemia. M.D. Anderson Cancer Center. 2017. ClinicalTrials.gov Identifier: NCT03263572

19. (NCT03263572 chunk 2):  Blinatumomab, Methotrexate, Cytarabine, and Ponatinib in Treating Patients With Philadelphia Chromosome-Positive, or BCR-ABL Positive, or Relapsed/Refractory, Acute Lymphoblastic Leukemia. M.D. Anderson Cancer Center. 2017. ClinicalTrials.gov Identifier: NCT03263572

20. (NCT06773936 chunk 1):  Adding Asciminib to Usual Treatment for Adults With Newly Diagnosed Philadelphia Chromosome Positive (Ph+) Acute Lymphoblastic Leukemia. SWOG Cancer Research Network. 2026. ClinicalTrials.gov Identifier: NCT06773936

21. (kantarjian2024resultsofthe media aadc8e08): Hagop Kantarjian, Nicholas J. Short, Fadi G. Haddad, Nitin Jain, Xuelin Huang, Guillermo Montalban-Bravo, Rashmi Kanagal-Shamanna, Tapan M. Kadia, Naval Daver, Kelly Chien, Yesid Alvarado, Guillermo Garcia-Manero, Ghayas C. Issa, Rebecca Garris, Cedric Nasnas, Lewis Nasr, Farhad Ravandi, and Elias Jabbour. Results of the simultaneous combination of ponatinib and blinatumomab in philadelphia chromosome-positive all. Journal of Clinical Oncology, 42:4246-4251, Dec 2024. URL: https://doi.org/10.1200/jco.24.00272, doi:10.1200/jco.24.00272. This article has 74 citations and is from a highest quality peer-reviewed journal.

22. (kantarjian2024resultsofthe media b753f7a6): Hagop Kantarjian, Nicholas J. Short, Fadi G. Haddad, Nitin Jain, Xuelin Huang, Guillermo Montalban-Bravo, Rashmi Kanagal-Shamanna, Tapan M. Kadia, Naval Daver, Kelly Chien, Yesid Alvarado, Guillermo Garcia-Manero, Ghayas C. Issa, Rebecca Garris, Cedric Nasnas, Lewis Nasr, Farhad Ravandi, and Elias Jabbour. Results of the simultaneous combination of ponatinib and blinatumomab in philadelphia chromosome-positive all. Journal of Clinical Oncology, 42:4246-4251, Dec 2024. URL: https://doi.org/10.1200/jco.24.00272, doi:10.1200/jco.24.00272. This article has 74 citations and is from a highest quality peer-reviewed journal.

23. (kantarjian2024resultsofthe media 5938646a): Hagop Kantarjian, Nicholas J. Short, Fadi G. Haddad, Nitin Jain, Xuelin Huang, Guillermo Montalban-Bravo, Rashmi Kanagal-Shamanna, Tapan M. Kadia, Naval Daver, Kelly Chien, Yesid Alvarado, Guillermo Garcia-Manero, Ghayas C. Issa, Rebecca Garris, Cedric Nasnas, Lewis Nasr, Farhad Ravandi, and Elias Jabbour. Results of the simultaneous combination of ponatinib and blinatumomab in philadelphia chromosome-positive all. Journal of Clinical Oncology, 42:4246-4251, Dec 2024. URL: https://doi.org/10.1200/jco.24.00272, doi:10.1200/jco.24.00272. This article has 74 citations and is from a highest quality peer-reviewed journal.

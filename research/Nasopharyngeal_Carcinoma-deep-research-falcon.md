---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T06:26:05.198384'
end_time: '2026-05-10T06:48:48.525943'
duration_seconds: 1363.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Nasopharyngeal Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nasopharyngeal Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Nasopharyngeal Carcinoma** covering all of the
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
- **Disease Name:** Nasopharyngeal Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Nasopharyngeal Carcinoma** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Nasopharyngeal Carcinoma (NPC)

### Target Disease
- **Disease name:** Nasopharyngeal carcinoma (NPC)
- **MONDO ID:** **MONDO:0015459** (nasopharyngeal carcinoma) (OpenTargets Search: Nasopharyngeal carcinoma,Nasopharyngeal cancer)
- **Category:** Head and neck cancer; epithelial malignancy of the nasopharyngeal mucosa (jiang2024recentadvancesin pages 1-2, zhou2026shiftingburdenof pages 1-2)

A quantitative snapshot of high-value evidence is provided first as a structured artifact.

| Domain | Metric | Value(s) | Population/Design | Source (year; DOI) |
|---|---|---|---|---|
| Global epidemiology | Global incident cases and deaths (2020) | 133,354 cases; 80,008 deaths | GLOBOCAN 2020, 185 countries/territories | Zhang et al. 2024; 10.1136/bmjopen-2024-091087 (zhang2024globalepidemiologicalprofile pages 1-1, zhang2024globalepidemiologicalprofile pages 2-3) |
| Global epidemiology | East Asia share of global burden (2020) | 49.39% of cases (65,866/133,354); 45.56% of deaths (36,453/80,008) | GLOBOCAN 2020 regional analysis | Zhang et al. 2024; 10.1136/bmjopen-2024-091087 (zhang2024globalepidemiologicalprofile pages 1-1) |
| Global epidemiology | Projected annual burden (2040) | 179,476 cases (+34.58% vs 2020); 113,851 deaths (+42.29% vs 2020) | Projection study using UN population forecasts | Zhang et al. 2024; 10.1136/bmjopen-2024-091087 (zhang2024globalepidemiologicalprofile pages 1-1, zhang2024globalepidemiologicalprofile pages 4-5) |
| Stage at diagnosis / prognosis | Advanced-stage presentation | Up to 80% diagnosed at stage III–IV; 10% with distant metastases | Review of clinical epidemiology/early detection literature | Jiang et al. 2024; 10.1007/s12672-024-01242-3 (jiang2024recentadvancesin pages 1-2) |
| Stage at diagnosis / prognosis | Example survival for earlier-stage disease | 5-year disease-specific survival rate for stage II: 97.3% | Review summarizing NPC outcomes | Jiang et al. 2024; 10.1007/s12672-024-01242-3 (jiang2024recentadvancesin pages 1-2) |
| Stage at diagnosis / prognosis | Stage-dependent overall survival | 5-year OS as high as 94% in early stage vs 73.7% in late-stage (III–IV) NPC | Review summarizing stage-stratified outcomes | Su et al. 2023; 10.3389/fmicb.2023.1116143 (su2023theroleof pages 1-2) |
| EBV screening | EBV IgA serology at 1 year | Sensitivity 93%; specificity 97%; PPV ~4.4%; early-stage detection ~68% | Population screening studies summarized by expert consensus | Lam et al. 2023; 10.1093/jnci/djad012 (lam2023recommendationsforepsteinbarr pages 4-4, lam2023recommendationsforepsteinbarr pages 1-2) |
| EBV screening | Plasma EBV DNA at 1 year | Sensitivity ~97%; specificity ~99%; PPV ~11.0%; early-stage detection ~70% | Population screening studies summarized by expert consensus | Lam et al. 2023; 10.1093/jnci/djad012 (lam2023recommendationsforepsteinbarr pages 4-4, lam2023recommendationsforepsteinbarr pages 1-2) |
| Diagnostic biomarkers | NPS EBV DNA qPCR performance | AUC 0.97; sensitivity 92.00%; specificity 98.67% | Case-control study, 150 newly diagnosed NPC cases vs 150 controls, southern China | Li et al. 2025; 10.1186/s12885-025-14539-5 (li2025diagnosticperformanceof pages 2-4) |
| Diagnostic biomarkers | Plasma EBV DNA qPCR performance | AUC 0.93; sensitivity 85.33%; specificity 98.67% | Same paired-specimen case-control study | Li et al. 2025; 10.1186/s12885-025-14539-5 (li2025diagnosticperformanceof pages 2-4) |
| Diagnostic biomarkers | Anti-EBV seropositivity in case-control study | 94.67% of NPC cases vs 10.00% of controls seropositive (P score >0.65) | Case-control ELISA for VCA-IgA and EBNA1-IgA | Li et al. 2025; 10.1186/s12885-025-14539-5 (li2025diagnosticperformanceof pages 2-4) |
| Gene–virus interaction | High-risk EBV subtype effect | EBV variant 163364 associated with 6.86-fold increased NPC risk | Population-based case-control study in endemic southern China | Xu et al. 2024; 10.1016/j.xgen.2023.100474 (xu2024hostgeneticvariants pages 1-3, xu2024hostgeneticvariants pages 5-6) |
| Gene–virus interaction | Host HLA susceptibility variants | rs2860580 OR 1.72; rs2894207 OR 1.64 | GWAS/prior association evidence integrated into interaction analysis | Xu et al. 2024; 10.1016/j.xgen.2023.100474 (xu2024hostgeneticvariants pages 3-4) |
| Gene–virus interaction | Additive interaction effect sizes | RERI 4.08 (95% CI 2.03–6.14) for rs2860580 × EBV variant 163364; RERI 3.37 (95% CI 1.59–5.15) for rs2894207 × variant 163364 | Interaction/mediation analysis in original + replication + pooled datasets | Xu et al. 2024; 10.1016/j.xgen.2023.100474 (xu2024hostgeneticvariants pages 1-3, xu2024hostgeneticvariants pages 5-6) |


*Table: This table compiles key quantitative findings for nasopharyngeal carcinoma across epidemiology, stage at diagnosis, EBV-based screening/diagnostics, and host–virus genetic interaction. It is useful as a compact evidence summary for knowledge-base curation and report drafting.*

---

## 1. Disease Information

### 1.1 Overview / definition
Nasopharyngeal carcinoma is an epithelial head-and-neck malignancy originating from the mucosal lining of the nasopharynx (zhou2026shiftingburdenof pages 1-2). It is notable for pronounced geographic clustering (endemic regions in Southern China and parts of Southeast Asia and North Africa) and for a strong association with Epstein–Barr virus (EBV), particularly in endemic non-keratinizing forms (jiang2024recentadvancesin pages 1-2, su2023theroleof pages 1-2).

### 1.2 Key identifiers and ontology alignment (available in retrieved sources)
- **MONDO:** MONDO:0015459 (nasopharyngeal carcinoma) (OpenTargets Search: Nasopharyngeal carcinoma,Nasopharyngeal cancer)
- **Related disease entities in OpenTargets results:** “nasopharyngeal neoplasm” (EFO:0004252), “nasopharyngeal squamous cell carcinoma” (EFO:1000058) (OpenTargets Search: Nasopharyngeal carcinoma,Nasopharyngeal cancer)

**Not retrieved in the available corpus (therefore not asserted):** ICD-10/ICD-11 codes, MeSH ID, Orphanet ID, OMIM disease ID.

### 1.3 Synonyms / alternative names
- Nasopharyngeal cancer; nasopharynx cancer; nasopharyngeal neoplasm (OpenTargets Search: Nasopharyngeal carcinoma,Nasopharyngeal cancer)

### 1.4 Evidence source type
This report synthesizes **aggregated disease-level resources** (expert recommendations, reviews, global burden datasets) and **primary human studies** (screening/diagnostic accuracy, case-control host–virus genetics) plus **experimental models** (organoid-initiated murine orthotopic models). (lam2023recommendationsforepsteinbarr pages 4-4, li2025diagnosticperformanceof pages 2-4, xu2024hostgeneticvariants pages 5-6, wan2024primaryandorthotopic pages 9-12)

---

## 2. Etiology

### 2.1 Primary causal factors
**EBV as principal etiologic driver in endemic NPC.** Reviews and expert sources emphasize that endemic NPC is EBV-associated and that EBV–host and tumor–immune interactions are central to its pathogenesis. For example, a 2023 review states that “EBV is the primary causative agent of NPC” and highlights EBV immune interactions as defining pathology (undifferentiated carcinoma with extensive lymphocyte infiltration). (yoshizaki2023recentadvancesin pages 8-9)

### 2.2 Risk factors

#### Infectious (EBV)
NPC is “closely associated with the Epstein–Barr virus (EBV)” and EBV-associated biomarkers have been leveraged for mass screening in endemic regions (su2023theroleof pages 1-2).

#### Host genetics (genetic susceptibility; gene–virus interaction)
A 2024 population-based case-control study in endemic southern China (Cell Genomics; **published Feb 2024**; URL https://doi.org/10.1016/j.xgen.2023.100474) quantified a strong **host HLA × EBV subtype interaction**. The authors reported GWAS evidence that “HLA genes have the most consistent and prominent evidence for the association with NPC,” citing rs2860580 (OR 1.72) and rs2894207 (OR 1.64) (xu2024hostgeneticvariants pages 3-4). They found that an EBV subtype defined by variant 163364 was associated with a **6.86-fold** increased NPC risk and demonstrated substantial additive interaction (RERI 4.08 and 3.37 for the two HLA SNPs), implying that a large fraction of inherited susceptibility manifests in the presence of high-risk EBV (xu2024hostgeneticvariants pages 5-6).

#### Environmental / lifestyle / occupational
Recent synthesis sources highlight:
- **Salt-preserved foods** (nitrosamines and EBV-reactivating chemicals). A 2024 early-detection review reports preserved-food intake associated with relative risks spanning roughly **1.4–3.2** (weekly) and **1.8–7.5** (daily) across Chinese studies (jiang2024recentadvancesin pages 2-5).
- **Smoking** and **occupational exposures** including dusts/formaldehyde are repeatedly described as contributing to NPC risk and geographic heterogeneity (zhang2024globalepidemiologicalprofile pages 1-1, jiang2024recentadvancesin pages 2-5).

### 2.3 Protective factors
Robust protective genetic or environmental factors were **not** directly supported in the retrieved primary corpus and are therefore not asserted.

### 2.4 Gene–environment / gene–virus interactions
The most clearly quantified interaction in the retrieved 2023–2024 primary literature is **host HLA × EBV subtype** (gene–virus). The Cell Genomics study concluded that targeting high-risk EBV carriers and/or high-risk viral lineages could substantially reduce risk in endemic settings (xu2024hostgeneticvariants pages 1-3, xu2024hostgeneticvariants pages 5-6).

---

## 3. Phenotypes

### 3.1 Common presenting symptoms and signs
Clinical presentation can be non-specific, contributing to delayed diagnosis. A 2023 review lists common symptoms including **“headache, epistaxis, and facial pain”** (su2023theroleof pages 1-2).

**Candidate HPO terms (suggestions):**
- Epistaxis — **HP:0000421**
- Headache — **HP:0002315**
- Facial pain — **HP:0000337**

### 3.2 Histologic subtypes (WHO categories)
A 2023 review describes WHO histologic categories: **keratinizing squamous cell carcinoma (type 1), non-keratinizing squamous cell carcinoma (type 2), and undifferentiated carcinoma (type 3)**, noting EBV prevalence is “100% in type 2 and type 3 NPC” in endemic areas (su2023theroleof pages 1-2). A 2024 review similarly emphasizes that endemic NPC is dominated by EBV-associated non-keratinizing tumors (“accounting for over 95% of cases” in endemic areas) (jiang2024recentadvancesin pages 1-2).

### 3.3 Age of onset, progression, and frequency
NPC has strong sex and age patterns: a 2024 review states men are “two to three times more likely” than women to develop NPC and that the “peak age of disease occurrence” is ~45 years (jiang2024recentadvancesin pages 1-2). A key clinical pattern is late presentation: “up to 80%” diagnosed at stage III–IV and “10%” with distant metastases (jiang2024recentadvancesin pages 1-2).

### 3.4 Quality of life impact
Direct QoL instrument data (e.g., EORTC QLQ-H&N, EQ-5D) were not retrieved. Indirectly, advanced-stage disease requires more intensive multimodality therapy and has worse outcomes than early-stage disease (su2023theroleof pages 1-2, yoshizaki2023recentadvancesin pages 8-9).

---

## 4. Genetic / Molecular Information

### 4.1 Key genes and molecular themes (somatic + viral)
**EBV latent and lytic gene programs.** A 2023 review highlights EBV–host and tumor–immune interactions and notes key EBV genes including **LMP1** (oncogene) and **BZLF1** (lytic induction) (yoshizaki2023recentadvancesin pages 8-9). Reviews also emphasize that elevated anti-EBV antibodies and plasma EBV DNA are clinically used biomarkers for EBV-associated NPC (yoshizaki2023recentadvancesin pages 8-9, yoshizaki2023recentadvancesin pages 9-11).

**Pathway-level concepts (review-synthesized).** EBV latent proteins are described to influence oncogenic signaling and immune evasion; authoritative reviews cite involvement of immune checkpoints and immunosuppressive tumor microenvironment (yoshizaki2023recentadvancesin pages 8-9, su2023theroleof pages 1-2).

### 4.2 Host susceptibility variants (primary human evidence)
The Cell Genomics 2024 study provides primary, quantitative evidence that common HLA-associated SNPs (rs2860580; rs2894207) confer modest risk (OR ~1.6–1.7) but interact strongly with a high-risk EBV subtype (variant 163364), indicating that host genetics and EBV strain jointly drive NPC risk (xu2024hostgeneticvariants pages 3-4, xu2024hostgeneticvariants pages 5-6).

### 4.3 Epigenetic information
Recent reviews emphasize aberrant DNA methylation as an early and important molecular theme (e.g., tumor suppressor methylation in NPC) (jiang2024recentadvancesin pages 2-5).

### 4.4 Experimental functional genetics (model systems)
A 2024 Advanced Science study (published Jul 2024; URL https://doi.org/10.1002/advs.202403161) developed organoid-initiated murine models: “we created a serial of primary, orthotopic, and genetic driver-defined NPC mouse models initiated with gene-edited normal nasopharyngeal organoids.” (wan2024primaryandorthotopic pages 9-12). In these models, the authors “experimentally validated TP53 and CDKN2A as bona fide tumor suppressors of NPC” and reported that **TGFBR2 loss promoted progression and lung metastasis** and **LMP1 promoted distal metastasis** (wan2024primaryandorthotopic pages 9-12, wan2024primaryandorthotopic pages 6-7).

**Suggested GO Biological Process terms (examples):**
- EBV infection / host–virus interaction — “viral process” (GO:0016032)
- Immune evasion / immune checkpoint signaling — “negative regulation of T cell activation” (GO:0050868)
- DNA methylation — “DNA methylation” (GO:0006306)
- EMT and metastasis — “epithelial to mesenchymal transition” (GO:0001837)

**Suggested CL (cell type) terms (examples):**
- Nasopharyngeal epithelial cell / squamous epithelial cell (epithelial lineage; CL suggestions)
- Tumor-infiltrating lymphocytes (T cell; B cell; macrophage)

---

## 5. Environmental Information

NPC’s geographic clustering is attributed to a combination of EBV, host genetics, and environmental/lifestyle risks. A GLOBOCAN-based epidemiology analysis explicitly lists etiologic contributors including “Epstein-Barr virus (EBV) infection, smoking, consumption of salted fish and other preserved foods and occupational exposure to wood dust” (zhang2024globalepidemiologicalprofile pages 1-1).

---

## 6. Mechanism / Pathophysiology (causal chain; current understanding)

### 6.1 High-level causal chain
1) **EBV infection of nasopharyngeal epithelium** with persistence/latency and tumor–immune interactions (yoshizaki2023recentadvancesin pages 8-9, su2023theroleof pages 1-2).
2) **Host susceptibility** (notably HLA-region variation) shapes immune recognition of EBV and—together with high-risk viral lineages—markedly increases cancer risk (xu2024hostgeneticvariants pages 5-6).
3) **Oncogenic signaling + epigenetic reprogramming** (including methylation patterns) support malignant transformation and immune escape (jiang2024recentadvancesin pages 2-5).
4) **Progression and metastasis** are promoted by viral oncogenes (e.g., LMP1) and by loss of tumor suppressors / microenvironmental remodeling (TP53/CDKN2A/TGFBR2 in murine orthotopic models) (wan2024primaryandorthotopic pages 9-12).

### 6.2 Upstream vs downstream
- Upstream: EBV strain and host HLA genotype; environmental carcinogens facilitating EBV reactivation/DNA damage (xu2024hostgeneticvariants pages 5-6, jiang2024recentadvancesin pages 2-5).
- Downstream: immune evasion and metastatic spread, late-stage presentation, treatment intensification (wan2024primaryandorthotopic pages 9-12, jiang2024recentadvancesin pages 1-2).

---

## 7. Anatomical Structures Affected

### 7.1 Primary site
- **Nasopharynx mucosal epithelium** (anatomic origin) (zhou2026shiftingburdenof pages 1-2)

**Suggested UBERON term (example):**
- Nasopharynx — **UBERON:0001736** (suggested; ontology mapping not directly retrieved in sources)

### 7.2 Secondary involvement
- Regional lymph nodes and distant metastases are common in advanced disease; a review reports ~10% present with distant metastases (jiang2024recentadvancesin pages 1-2).

---

## 8. Temporal Development

### 8.1 Onset and course
NPC often has an insidious course with non-specific symptoms; late-stage diagnosis is common (su2023theroleof pages 1-2, jiang2024recentadvancesin pages 1-2).

### 8.2 Staging
The TNM system is the primary framework for risk evaluation and treatment stratification (jiang2024recentadvancesin pages 1-2).

---

## 9. Inheritance and Population

### 9.1 Epidemiology and demographics (recent quantitative evidence)
A 2024 BMJ Open prediction study using **GLOBOCAN 2020** reports **133,354** NPC cases and **80,008** deaths globally in 2020, with East Asia as the “epicentre” accounting for **49.39%** of cases and **45.56%** of deaths (published Dec 2024; URL https://doi.org/10.1136/bmjopen-2024-091087) (zhang2024globalepidemiologicalprofile pages 1-1). The study projects growth to **179,476** cases and **113,851** deaths by 2040 under demographic change assumptions (zhang2024globalepidemiologicalprofile pages 4-5).

A 2024 review highlights extreme regional variation (incidence >15/100,000 person-years in some Southeast Asian communities vs <1/100,000 in the United States) and endemic concentration in Southern China, Southeast Asia, and Northern Africa (published Aug 2024; URL https://doi.org/10.1007/s12672-024-01242-3) (jiang2024recentadvancesin pages 1-2).

### 9.2 Inheritance pattern
NPC is best characterized as **multifactorial** (polygenic susceptibility interacting with EBV and environment). The strongest quantified 2024 human evidence is a host HLA × EBV subtype interaction (xu2024hostgeneticvariants pages 5-6).

---

## 10. Diagnostics

### 10.1 Clinical diagnostic workflow (current understanding)
Nasopharyngeal endoscopy with pathologic examination remains the diagnostic gold standard (yoshizaki2023recentadvancesin pages 8-9). Screening-positive individuals can undergo confirmatory evaluation with endoscopy and, per expert recommendations, MRI to improve sensitivity (lam2023recommendationsforepsteinbarr pages 1-2).

### 10.2 EBV-related biomarkers (screening and diagnosis)
**Expert recommendations (2023).** A 2023 JNCI expert meeting report concluded that serum EBV antibody testing and plasma EBV DNA testing “were found to have favorable performance characteristics and to be cost-effective in high-risk populations,” and that MRI use in evaluation of screen-positive individuals increases sensitivity (published Feb 2023; URL https://doi.org/10.1093/jnci/djad012) (lam2023recommendationsforepsteinbarr pages 1-2).

**Screening performance metrics (Table evidence).** The same JNCI report tabulated 1-year screening metrics: EBV IgA serology sensitivity 93%, specificity 97%, PPV 4.4%; plasma EBV DNA sensitivity 97%, specificity 99%, PPV 11.0% (lam2023recommendationsforepsteinbarr pages 4-4). The table is captured as an image (lam2023recommendationsforepsteinbarr media a09887fa).

**Specimen-based EBV DNA diagnostic accuracy (2025 case-control).** In a paired-specimen case-control study (150 NPC cases vs 150 controls), EBV DNA in nasopharyngeal swabs had higher AUC (0.97) than plasma (0.93); at specified cutoffs, swab sensitivity 92.0% and specificity 98.67%, plasma sensitivity 85.33% and specificity 98.67% (published Jul 2025; URL https://doi.org/10.1186/s12885-025-14539-5) (li2025diagnosticperformanceof pages 2-4).

### 10.3 Differential diagnosis
Detailed differential diagnosis lists were not comprehensively retrieved. However, expert recommendations discuss advanced MRI approaches to distinguish early NPC from benign hyperplasia in diagnostic evaluation contexts (lam2023recommendationsforepsteinbarr pages 9-10).

---

## 11. Outcome / Prognosis

Stage at diagnosis strongly influences survival. A 2023 review reports a “5-year overall survival (OS) rate… as high as 94%” for early-stage NPC and “73.7%” for late-stage (III–IV) disease (su2023theroleof pages 1-2). In a 2024 review, stage II 5-year disease-specific survival is cited as 97.3% (jiang2024recentadvancesin pages 1-2). These figures underscore the importance of earlier detection and screening in high-risk populations.

---

## 12. Treatment

### 12.1 Standard modalities (real-world practice)
A 2023 review states early-stage NPC is treated with radiotherapy alone, whereas advanced-stage disease typically requires combined chemotherapy and radiotherapy (yoshizaki2023recentadvancesin pages 8-9). Locoregionally advanced disease is commonly approached with induction chemotherapy and concurrent chemoradiotherapy in contemporary practice (jin2024theefficacyand pages 1-3).

### 12.2 Immunotherapy (PD-1 blockade) and real-world implementation
**Regulatory implementation (United States).** A 2025 commentary letter reports that **toripalimab** was approved by the US FDA on **10/27/2023** for first-line treatment of locally advanced/recurrent/metastatic NPC in combination with cisplatin + gemcitabine, and as monotherapy after progression on platinum therapy (published Jan 2025; URL https://doi.org/10.47391/jpma.20757) (siddiqui2025toripalimabanew pages 1-1).

**Clinical evidence base (summarized).** Systematic and consensus sources describe multiple phase III trials adding PD-1 inhibitors to gemcitabine/cisplatin chemotherapy in recurrent/metastatic NPC (e.g., JUPITER-02 and CAPTAIN-1st) (qiu2025efficacysafetyand pages 1-3, manoharan2025efficacyandsafety pages 6-7). In locoregionally advanced NPC, a 2024 real-world propensity score-matched analysis reported improved complete response and cfEBV DNA clearance and numerically improved 3-year DFS (84% to 95%) with added PD-1 blockade, with comparable grade 3–4 toxicity (published May 2024; URL https://doi.org/10.1007/s00262-024-03698-2) (jin2024theefficacyand pages 1-3).

### 12.3 Experimental/ongoing trials (ClinicalTrials.gov)
Examples of ongoing/registered immunotherapy trials from retrieved ClinicalTrials.gov records:
- **NCT04376866** (Phase 3; recruiting): toripalimab + concurrent cisplatin chemoradiotherapy vs chemoradiotherapy alone for locoregionally recurrent NPC; primary outcome overall survival (5-year) (NCT04376866 chunk 1).
- **NCT05211232**: neoadjuvant and adjuvant tislelizumab in stage III–IVA nonkeratinizing NPC; toxicity outcomes include CTCAE v5.0 acute/late radiation toxicity (NCT05211232 chunk 2).

**Suggested MAXO treatment action terms (examples; ontology suggestions):**
- Radiotherapy — MAXO:0000017 (suggested)
- Chemotherapy — MAXO:0000010 (suggested)
- Immune checkpoint inhibitor therapy — MAXO:0001023 (suggested)

---

## 13. Prevention

### 13.1 Primary prevention
No licensed EBV vaccine exists; reviews note this as an unmet need (yoshizaki2023recentadvancesin pages 8-9). Risk-factor modification efforts focus on reducing preserved-food exposures, smoking, and occupational carcinogen exposures (zhang2024globalepidemiologicalprofile pages 1-1, jiang2024recentadvancesin pages 2-5).

### 13.2 Secondary prevention (screening)
A 2023 expert panel recommended EBV-based screening (serology or plasma EBV DNA) in high- and intermediate-risk regions, with endoscopy and MRI used for assessment of screen-positive individuals (published Feb 2023; URL https://doi.org/10.1093/jnci/djad012) (lam2023recommendationsforepsteinbarr pages 1-2). The panel reported 1-year screening metrics (Table 1) consistent with high specificity and improved PPV for plasma EBV DNA relative to serology (lam2023recommendationsforepsteinbarr media a09887fa).

---

## 14. Other Species / Natural Disease

No evidence for naturally occurring nasopharyngeal carcinoma in non-human species was retrieved in the current tool-based corpus.

---

## 15. Model Organisms

A major 2024 advance is the availability of organoid-initiated, orthotopic murine models. Wan et al. reported creation of “the first primary and orthotopic NPC models” from gene-edited nasopharyngeal organoids and used these to establish functional roles for **TP53, CDKN2A, TGFBR2**, and EBV oncoprotein **LMP1** in initiation/progression/metastasis (published Jul 2024; URL https://doi.org/10.1002/advs.202403161) (wan2024primaryandorthotopic pages 9-12). They explicitly note the limitation that “it is impossible to directly study EBV infection in mice,” highlighting the need for complementary in vitro/humanized systems (wan2024primaryandorthotopic pages 9-12).

---

## Notes on evidence gaps (transparency)
Within the retrieved corpus, ICD/MeSH/Orphanet identifiers, detailed differential diagnosis lists, and QoL instrument statistics were not directly accessible; these are therefore not asserted and should be filled from dedicated ontology/registry resources in a follow-on curation pass.


References

1. (OpenTargets Search: Nasopharyngeal carcinoma,Nasopharyngeal cancer): Open Targets Query (Nasopharyngeal carcinoma,Nasopharyngeal cancer, 21 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (jiang2024recentadvancesin pages 1-2): Wen Jiang, Bohao Zheng, and Hongquan Wei. Recent advances in early detection of nasopharyngeal carcinoma. Discover Oncology, Aug 2024. URL: https://doi.org/10.1007/s12672-024-01242-3, doi:10.1007/s12672-024-01242-3. This article has 18 citations.

3. (zhou2026shiftingburdenof pages 1-2): Enhui Zhou, Feifei Xu, Tianjiao Zhou, Jingyu Zhang, Fan Song, Jianxiang Li, Hongliang Yi, Qingliang Wang, and Weijun Huang. Shifting burden of nasopharyngeal carcinoma: global patterns and forecasts to 2050 from the gbd 2021. Frontiers in Oncology, Jan 2026. URL: https://doi.org/10.3389/fonc.2025.1687320, doi:10.3389/fonc.2025.1687320. This article has 1 citations.

4. (zhang2024globalepidemiologicalprofile pages 1-1): Yuna Zhang, Shanshan Gu, Hongxia Deng, and Zhisen Shen. Global epidemiological profile in nasopharyngeal carcinoma: a prediction study. BMJ Open, 14:e091087, Dec 2024. URL: https://doi.org/10.1136/bmjopen-2024-091087, doi:10.1136/bmjopen-2024-091087. This article has 27 citations and is from a peer-reviewed journal.

5. (zhang2024globalepidemiologicalprofile pages 2-3): Yuna Zhang, Shanshan Gu, Hongxia Deng, and Zhisen Shen. Global epidemiological profile in nasopharyngeal carcinoma: a prediction study. BMJ Open, 14:e091087, Dec 2024. URL: https://doi.org/10.1136/bmjopen-2024-091087, doi:10.1136/bmjopen-2024-091087. This article has 27 citations and is from a peer-reviewed journal.

6. (zhang2024globalepidemiologicalprofile pages 4-5): Yuna Zhang, Shanshan Gu, Hongxia Deng, and Zhisen Shen. Global epidemiological profile in nasopharyngeal carcinoma: a prediction study. BMJ Open, 14:e091087, Dec 2024. URL: https://doi.org/10.1136/bmjopen-2024-091087, doi:10.1136/bmjopen-2024-091087. This article has 27 citations and is from a peer-reviewed journal.

7. (su2023theroleof pages 1-2): Zhi Yi Su, Pui Yan Siak, Chee-Onn Leong, and Shiau-Chuen Cheah. The role of epstein–barr virus in nasopharyngeal carcinoma. Frontiers in Microbiology, Feb 2023. URL: https://doi.org/10.3389/fmicb.2023.1116143, doi:10.3389/fmicb.2023.1116143. This article has 167 citations and is from a peer-reviewed journal.

8. (lam2023recommendationsforepsteinbarr pages 4-4): W K Jacky Lam, Ann D King, Jacob A Miller, Zhiwei Liu, Kelly J Yu, Melvin L K Chua, Brigette B Y Ma, Ming Yuan Chen, Benjamin A Pinsky, Pei-Jen Lou, John K S Woo, Wan-Lun Hsu, Julia Simon, Denise L Doolan, Tim Waterboer, Edwin P Hui, Hui Li, Raymond K Tsang, Kenneth C W Wong, Julian P Goh, Alexander C Vlantis, Qi Yong Ai, Lun M Wong, Victor Abdullah, Jin Ching Lin, Chien-Jen Chen, Ruth M Pfeiffer, Quynh-Thu Le, Anne W M Lee, Mingfang Ji, Sumei Cao, Jun Ma, Anthony T C Chan, K C Allen Chan, and Allan Hildesheim. Recommendations for epstein-barr virus–based screening for nasopharyngeal cancer in high- and intermediate-risk regions. JNCI: Journal of the National Cancer Institute, 115:355-364, Feb 2023. URL: https://doi.org/10.1093/jnci/djad012, doi:10.1093/jnci/djad012. This article has 53 citations.

9. (lam2023recommendationsforepsteinbarr pages 1-2): W K Jacky Lam, Ann D King, Jacob A Miller, Zhiwei Liu, Kelly J Yu, Melvin L K Chua, Brigette B Y Ma, Ming Yuan Chen, Benjamin A Pinsky, Pei-Jen Lou, John K S Woo, Wan-Lun Hsu, Julia Simon, Denise L Doolan, Tim Waterboer, Edwin P Hui, Hui Li, Raymond K Tsang, Kenneth C W Wong, Julian P Goh, Alexander C Vlantis, Qi Yong Ai, Lun M Wong, Victor Abdullah, Jin Ching Lin, Chien-Jen Chen, Ruth M Pfeiffer, Quynh-Thu Le, Anne W M Lee, Mingfang Ji, Sumei Cao, Jun Ma, Anthony T C Chan, K C Allen Chan, and Allan Hildesheim. Recommendations for epstein-barr virus–based screening for nasopharyngeal cancer in high- and intermediate-risk regions. JNCI: Journal of the National Cancer Institute, 115:355-364, Feb 2023. URL: https://doi.org/10.1093/jnci/djad012, doi:10.1093/jnci/djad012. This article has 53 citations.

10. (li2025diagnosticperformanceof pages 2-4): Xue-Qi Li, Dong-Feng Lin, Yu-Cong Cai, Shang-Hang Xie, Ke-Na Lin, Hang-Ning Zhou, Zhi-Cong Wu, Jun-Ping Ye, Yi-Nan Peng, Zheng Ma, Ling Guo, Wei Lin, and Su-Mei Cao. Diagnostic performance of ebv dna load testing for nasopharyngeal carcinoma in nasopharyngeal swab outperforms the approach in other specimens. BMC Cancer, Jul 2025. URL: https://doi.org/10.1186/s12885-025-14539-5, doi:10.1186/s12885-025-14539-5. This article has 2 citations and is from a peer-reviewed journal.

11. (xu2024hostgeneticvariants pages 1-3): Miao Xu, Ruimei Feng, Zhonghua Liu, Xiang Zhou, Yanhong Chen, Yulu Cao, Linda Valeri, Zilin Li, Zhiwei Liu, Su-Mei Cao, Qing Liu, Shang-Hang Xie, Ellen T. Chang, Wei-Hua Jia, Jincheng Shen, Youyuan Yao, Yong-Lin Cai, Yuming Zheng, Zhe Zhang, Guangwu Huang, Ingemar Ernberg, Minzhong Tang, Weimin Ye, Hans-Olov Adami, Yi-Xin Zeng, and Xihong Lin. Host genetic variants, epstein-barr virus subtypes, and the risk of nasopharyngeal carcinoma: assessment of interaction and mediation. Cell Genomics, 4:100474, Feb 2024. URL: https://doi.org/10.1016/j.xgen.2023.100474, doi:10.1016/j.xgen.2023.100474. This article has 28 citations and is from a peer-reviewed journal.

12. (xu2024hostgeneticvariants pages 5-6): Miao Xu, Ruimei Feng, Zhonghua Liu, Xiang Zhou, Yanhong Chen, Yulu Cao, Linda Valeri, Zilin Li, Zhiwei Liu, Su-Mei Cao, Qing Liu, Shang-Hang Xie, Ellen T. Chang, Wei-Hua Jia, Jincheng Shen, Youyuan Yao, Yong-Lin Cai, Yuming Zheng, Zhe Zhang, Guangwu Huang, Ingemar Ernberg, Minzhong Tang, Weimin Ye, Hans-Olov Adami, Yi-Xin Zeng, and Xihong Lin. Host genetic variants, epstein-barr virus subtypes, and the risk of nasopharyngeal carcinoma: assessment of interaction and mediation. Cell Genomics, 4:100474, Feb 2024. URL: https://doi.org/10.1016/j.xgen.2023.100474, doi:10.1016/j.xgen.2023.100474. This article has 28 citations and is from a peer-reviewed journal.

13. (xu2024hostgeneticvariants pages 3-4): Miao Xu, Ruimei Feng, Zhonghua Liu, Xiang Zhou, Yanhong Chen, Yulu Cao, Linda Valeri, Zilin Li, Zhiwei Liu, Su-Mei Cao, Qing Liu, Shang-Hang Xie, Ellen T. Chang, Wei-Hua Jia, Jincheng Shen, Youyuan Yao, Yong-Lin Cai, Yuming Zheng, Zhe Zhang, Guangwu Huang, Ingemar Ernberg, Minzhong Tang, Weimin Ye, Hans-Olov Adami, Yi-Xin Zeng, and Xihong Lin. Host genetic variants, epstein-barr virus subtypes, and the risk of nasopharyngeal carcinoma: assessment of interaction and mediation. Cell Genomics, 4:100474, Feb 2024. URL: https://doi.org/10.1016/j.xgen.2023.100474, doi:10.1016/j.xgen.2023.100474. This article has 28 citations and is from a peer-reviewed journal.

14. (wan2024primaryandorthotopic pages 9-12): Xudong Wan, Yuantao Liu, Yiman Peng, Jian Wang, Shu‐mei Yan, Lu Zhang, Wanchun Wu, Lei Zhao, Xuelan Chen, Kexin Ren, Haicheng Long, Yiling Luo, Qin Yan, Lele Zhang, Dengzhi Lei, Pengpeng Liu, Shujun Li, Lihui Liu, Linjie Guo, Jiajia Du, Mengsha Zhang, Siqi Dai, Yi Yang, Hongyu Liu, Nianyong Chen, Jinxin Bei, Lin Feng, Yu Liu, Mu‐sheng Zeng, Chong Chen, and Qian Zhong. Primary and orthotopic murine models of nasopharyngeal carcinoma reveal molecular mechanisms underlying its malignant progression. Advanced Science, Jul 2024. URL: https://doi.org/10.1002/advs.202403161, doi:10.1002/advs.202403161. This article has 9 citations and is from a peer-reviewed journal.

15. (yoshizaki2023recentadvancesin pages 8-9): Tomokazu Yoshizaki, Satoru Kondo, Hirotomo Dochi, Eiji Kobayashi, Harue Mizokami, Shigetaka Komura, and Kazuhira Endo. Recent advances in assessing the clinical implications of epstein-barr virus infection and their application to the diagnosis and treatment of nasopharyngeal carcinoma. Microorganisms, 12:14, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010014, doi:10.3390/microorganisms12010014. This article has 18 citations.

16. (jiang2024recentadvancesin pages 2-5): Wen Jiang, Bohao Zheng, and Hongquan Wei. Recent advances in early detection of nasopharyngeal carcinoma. Discover Oncology, Aug 2024. URL: https://doi.org/10.1007/s12672-024-01242-3, doi:10.1007/s12672-024-01242-3. This article has 18 citations.

17. (yoshizaki2023recentadvancesin pages 9-11): Tomokazu Yoshizaki, Satoru Kondo, Hirotomo Dochi, Eiji Kobayashi, Harue Mizokami, Shigetaka Komura, and Kazuhira Endo. Recent advances in assessing the clinical implications of epstein-barr virus infection and their application to the diagnosis and treatment of nasopharyngeal carcinoma. Microorganisms, 12:14, Dec 2023. URL: https://doi.org/10.3390/microorganisms12010014, doi:10.3390/microorganisms12010014. This article has 18 citations.

18. (wan2024primaryandorthotopic pages 6-7): Xudong Wan, Yuantao Liu, Yiman Peng, Jian Wang, Shu‐mei Yan, Lu Zhang, Wanchun Wu, Lei Zhao, Xuelan Chen, Kexin Ren, Haicheng Long, Yiling Luo, Qin Yan, Lele Zhang, Dengzhi Lei, Pengpeng Liu, Shujun Li, Lihui Liu, Linjie Guo, Jiajia Du, Mengsha Zhang, Siqi Dai, Yi Yang, Hongyu Liu, Nianyong Chen, Jinxin Bei, Lin Feng, Yu Liu, Mu‐sheng Zeng, Chong Chen, and Qian Zhong. Primary and orthotopic murine models of nasopharyngeal carcinoma reveal molecular mechanisms underlying its malignant progression. Advanced Science, Jul 2024. URL: https://doi.org/10.1002/advs.202403161, doi:10.1002/advs.202403161. This article has 9 citations and is from a peer-reviewed journal.

19. (lam2023recommendationsforepsteinbarr media a09887fa): W K Jacky Lam, Ann D King, Jacob A Miller, Zhiwei Liu, Kelly J Yu, Melvin L K Chua, Brigette B Y Ma, Ming Yuan Chen, Benjamin A Pinsky, Pei-Jen Lou, John K S Woo, Wan-Lun Hsu, Julia Simon, Denise L Doolan, Tim Waterboer, Edwin P Hui, Hui Li, Raymond K Tsang, Kenneth C W Wong, Julian P Goh, Alexander C Vlantis, Qi Yong Ai, Lun M Wong, Victor Abdullah, Jin Ching Lin, Chien-Jen Chen, Ruth M Pfeiffer, Quynh-Thu Le, Anne W M Lee, Mingfang Ji, Sumei Cao, Jun Ma, Anthony T C Chan, K C Allen Chan, and Allan Hildesheim. Recommendations for epstein-barr virus–based screening for nasopharyngeal cancer in high- and intermediate-risk regions. JNCI: Journal of the National Cancer Institute, 115:355-364, Feb 2023. URL: https://doi.org/10.1093/jnci/djad012, doi:10.1093/jnci/djad012. This article has 53 citations.

20. (lam2023recommendationsforepsteinbarr pages 9-10): W K Jacky Lam, Ann D King, Jacob A Miller, Zhiwei Liu, Kelly J Yu, Melvin L K Chua, Brigette B Y Ma, Ming Yuan Chen, Benjamin A Pinsky, Pei-Jen Lou, John K S Woo, Wan-Lun Hsu, Julia Simon, Denise L Doolan, Tim Waterboer, Edwin P Hui, Hui Li, Raymond K Tsang, Kenneth C W Wong, Julian P Goh, Alexander C Vlantis, Qi Yong Ai, Lun M Wong, Victor Abdullah, Jin Ching Lin, Chien-Jen Chen, Ruth M Pfeiffer, Quynh-Thu Le, Anne W M Lee, Mingfang Ji, Sumei Cao, Jun Ma, Anthony T C Chan, K C Allen Chan, and Allan Hildesheim. Recommendations for epstein-barr virus–based screening for nasopharyngeal cancer in high- and intermediate-risk regions. JNCI: Journal of the National Cancer Institute, 115:355-364, Feb 2023. URL: https://doi.org/10.1093/jnci/djad012, doi:10.1093/jnci/djad012. This article has 53 citations.

21. (jin2024theefficacyand pages 1-3): Ya-Nan Jin, Meng-Yun Qiang, Ying Wang, Yu-Jing Lin, Ren-Wei Jiang, Wan-Wei Cao, Wang-Jian Zhang, Si-Yang Wang, Hong-Yu Zhang, and Ji-Jin Yao. The efficacy and safety of adding pd-1 blockade to induction chemotherapy and concurrent chemoradiotherapy (ic-ccrt) for locoregionally advanced nasopharyngeal carcinoma: an observational, propensity score-matched analysis. Cancer Immunology, Immunotherapy : CII, May 2024. URL: https://doi.org/10.1007/s00262-024-03698-2, doi:10.1007/s00262-024-03698-2. This article has 20 citations.

22. (siddiqui2025toripalimabanew pages 1-1): Taha Ahmad Siddiqui, Aamrah Wakil, and Maham Imran. Toripalimab: a new age in fighting nasopharyngeal carcinoma. Journal of the Pakistan Medical Association, 75:349-349, Jan 2025. URL: https://doi.org/10.47391/jpma.20757, doi:10.47391/jpma.20757. This article has 1 citations.

23. (qiu2025efficacysafetyand pages 1-3): Lei Qiu, Qiran Wei, Yachun Hu, Jinling Yuan, Mengxing Wu, Yurong Li, Yuting Xu, Xin Guan, Yuandong Cao, Juan Pu, Zhou Ding, Yinjiao Fei, Weilin Xu, and Shu Zhou. Efficacy, safety and cost-effectiveness of chemo-immunotherapy combinations for recurrent or metastatic nasopharyngeal carcinoma: an updated systematic review and cost-effectiveness analysis. Translational Cancer Research, 14:7102-7118, Oct 2025. URL: https://doi.org/10.21037/tcr-2025-415, doi:10.21037/tcr-2025-415. This article has 2 citations.

24. (manoharan2025efficacyandsafety pages 6-7): Sivananthan Manoharan and Lee Ying Ying. Efficacy and safety of immune checkpoint inhibitors for locoregionally advanced, recurrent and metastatic nasopharyngeal carcinoma: a systematic review of phase iii randomised controlled trials. Naunyn-Schmiedeberg's Archives of Pharmacology, 399:1987-1998, Sep 2025. URL: https://doi.org/10.1007/s00210-025-04572-3, doi:10.1007/s00210-025-04572-3. This article has 2 citations.

25. (NCT04376866 chunk 1): Song Qu. Toripalimab for Local-regional Recurrent Nasopharyngeal Carcinoma. Cancer Hospital of Guangxi Medical University. 2020. ClinicalTrials.gov Identifier: NCT04376866

26. (NCT05211232 chunk 2): Hai-Qiang Mai,MD,PhD. Neoadjuvant and Adjuvant Tislelizumab for Nasopharyngeal Carcinoma. Sun Yat-sen University. 2022. ClinicalTrials.gov Identifier: NCT05211232

---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:27:33.797538'
end_time: '2026-05-08T12:50:52.421142'
duration_seconds: 1398.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chemotherapy-Induced Nausea and Vomiting
  mondo_id: ''
  category: Iatrogenic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chemotherapy-Induced Nausea and Vomiting
- **MONDO ID:**  (if available)
- **Category:** Iatrogenic

## Research Objectives

Please provide a comprehensive research report on **Chemotherapy-Induced Nausea and Vomiting** covering all of the
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
- **Disease Name:** Chemotherapy-Induced Nausea and Vomiting
- **MONDO ID:**  (if available)
- **Category:** Iatrogenic

## Research Objectives

Please provide a comprehensive research report on **Chemotherapy-Induced Nausea and Vomiting** covering all of the
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


# Chemotherapy-Induced Nausea and Vomiting (CINV): Comprehensive Disease Characteristics Report

## Target disease metadata
- **Disease name:** Chemotherapy-induced nausea and vomiting (CINV)
- **Category:** Iatrogenic (treatment-related adverse event)
- **MONDO ID / MeSH / ICD-10 / ICD-11:** Not retrievable from the provided tool-derived corpus; therefore not asserted here.
- **Common synonyms/alternative names:** CINV; acute CINV; delayed CINV; long-delayed/persistent CINV; anticipatory CINV; breakthrough CINV; refractory CINV. (jeryczynski2026antiemetictherapy pages 1-2, montes2026ttdexpertconsensus pages 3-5, rapoport20242023updatedmasccesmo pages 5-6)
- **Evidence source types used in this report:** Aggregated guideline resources (MASCC/ESMO), expert consensus, randomized-trial synthesis, and real-world observational data. (herrstedt20242023updatedmasccesmo pages 1-2, rapoport20242023updatedmasccesmo pages 1-2, sun2024theevolvinglandscape pages 1-2, uchiike2023olanzapinetreatmenteffectively pages 1-2)

## 1. Disease information (overview and current understanding)
CINV is a common, distressing adverse effect of antineoplastic therapy characterized by nausea and/or vomiting that occurs temporally in relation to chemotherapy exposure, with clinically relevant subtypes defined by timing and response to prophylaxis. Acute CINV occurs in the first 24 hours, delayed CINV occurs from 24–120 hours, and some sources additionally describe long-delayed/persistent symptoms beyond 120 hours; these later phases remain a major clinical challenge. (jeryczynski2026antiemetictherapy pages 1-2)

### Key contemporary definitions/classifications (clinical phenotypes)
Definitions supported by guideline and expert consensus sources include:
- **Acute CINV:** within 0–24 h after chemotherapy. (jeryczynski2026antiemetictherapy pages 1-2, uchiike2023olanzapinetreatmenteffectively pages 1-2)
- **Delayed CINV:** 24–120 h after chemotherapy; one consensus also highlights a common window of 24–72 h. (jeryczynski2026antiemetictherapy pages 1-2, montes2026ttdexpertconsensus pages 3-5)
- **Long-delayed/persistent CINV:** >120 h after chemotherapy. (jeryczynski2026antiemetictherapy pages 1-2)
- **Anticipatory CINV:** conditioned response occurring before treatment (linked to prior negative experiences). (montes2026ttdexpertconsensus pages 3-5, dhabhar2025expertconsensusguidance pages 5-6)
- **Breakthrough CINV:** nausea/vomiting occurring despite guideline-directed prophylaxis; MASCC/ESMO explicitly defines it as occurring “during chemotherapy regardless of prophylaxis with guideline-directed antiemetics.” (rapoport20242023updatedmasccesmo pages 5-6)
- **Refractory CINV:** symptoms recurring in subsequent cycles despite management in prior cycles. (montes2026ttdexpertconsensus pages 3-5)

A structured subtype table with suggested HPO mappings is provided in **Artifact 00**.

| Phenotype/subtype | Definition/time window | Putative dominant mediator(s) | Suggested HPO term(s) |
|---|---|---|---|
| Acute CINV | Nausea/vomiting occurring within 0–24 h after chemotherapy; may peak at ~5–6 h (jeryczynski2026antiemetictherapy pages 1-2, montes2026ttdexpertconsensus pages 3-5) | Predominantly serotonin signaling via 5-HT3 receptors (montes2026ttdexpertconsensus pages 3-5) | Nausea (HP:0002018); Vomiting (HP:0002013) |
| Delayed CINV | Nausea/vomiting occurring 24–120 h after chemotherapy; Montes notes delayed phase commonly 24–72 h (jeryczynski2026antiemetictherapy pages 1-2, montes2026ttdexpertconsensus pages 3-5) | Predominantly substance P signaling via NK1 receptors (montes2026ttdexpertconsensus pages 3-5) | Nausea (HP:0002018); Vomiting (HP:0002013) |
| Long-delayed / persistent CINV | Symptoms persisting beyond 120 h after chemotherapy (jeryczynski2026antiemetictherapy pages 1-2) | Not specifically assigned in provided snippets; likely mixed/uncertain | Nausea (HP:0002018) candidate; Vomiting (HP:0002013) candidate |
| Anticipatory CINV | Conditioned nausea/vomiting occurring before treatment, typically in anticipation of chemotherapy (montes2026ttdexpertconsensus pages 3-5) | Conditioned/behavioral response; specific neurotransmitter not defined in provided snippets | Nausea (HP:0002018) candidate; Vomiting (HP:0002013) candidate; Anticipatory nausea candidate |
| Breakthrough CINV | Nausea/vomiting occurring despite guideline-directed prophylaxis during/after chemotherapy; one source also describes it as arising beyond the fifth day despite prophylaxis (rapoport20242023updatedmasccesmo pages 5-6, montes2026ttdexpertconsensus pages 3-5) | Not specifically assigned in provided snippets; likely mixed/uncertain | Nausea (HP:0002018) candidate; Vomiting (HP:0002013) candidate; Breakthrough vomiting candidate |
| Refractory CINV | Nausea/vomiting occurring in subsequent chemotherapy cycles despite prior antiemetic management (montes2026ttdexpertconsensus pages 3-5) | Not specifically assigned in provided snippets; likely mixed/uncertain | Nausea (HP:0002018) candidate; Vomiting (HP:0002013) candidate; Refractory nausea/vomiting candidate |


*Table: This table summarizes the clinically recognized temporal and response-pattern subtypes of chemotherapy-induced nausea and vomiting, along with the dominant mediators supported by the cited evidence. It also suggests best-effort HPO mappings for structured phenotype annotation.*

## 2. Etiology and risk/protective factors
### 2.1 Primary causal factors (mechanistic)
CINV is caused by chemotherapy-triggered activation of peripheral and central emetic pathways, including gastrointestinal mucosal injury with neurotransmitter release and central chemoreceptor trigger zone/vomiting center activation. (aher2025aretrospectivedrug pages 1-3, montes2026ttdexpertconsensus pages 3-5)

### 2.2 Treatment-related risk factors
**Emetogenicity of the antineoplastic regimen** is a key determinant.
- High-emetic-risk chemotherapy (HEC) is defined as **>90% risk of vomiting in the first 24 h without prophylaxis** and includes cisplatin and the anthracycline–cyclophosphamide (AC) combination (in women with breast cancer), among others. (herrstedt20242023updatedmasccesmo pages 1-2)
- MASCC/ESMO updated the **classification of newer antineoplastic agents** (FDA/EMA approvals 2015–2023), revising oral-agent classification to **two categories (minimal–low vs moderate–high)** to align with ASCO, while retaining the four-category schema for IV agents; the panel emphasized large heterogeneity and imprecision for oral agents. (jordan2024emeticriskclassification pages 1-2)

### 2.3 Patient-related risk factors
Expert consensus and meta-analytic evidence highlight:
- **Female sex** and **younger age (e.g., <50)** as major risk factors. (montes2026ttdexpertconsensus pages 3-5)
- **Prior CINV** predicting subsequent cycles; MASCC/ESMO notes prior history significantly predicts later-cycle CINV. (rapoport20242023updatedmasccesmo pages 5-6)
- **History of pregnancy emesis** and **motion sickness** as additional risk factors. (montes2026ttdexpertconsensus pages 3-5)
- **Anxiety** and **fatigue** as risk factors in platinum-based chemotherapy meta-analysis (OR 1.689 and OR 1.413, respectively). (suzukichiba2024comparisonofolanzapine pages 5-7)

### 2.4 Pharmacogenomics / genetic susceptibility
A clinically relevant pharmacogenomic point is that **CYP2D6 ultra-rapid metabolizers may be undertreated with standard 5-HT3 receptor antagonist dosing**, implying reduced antiemetic efficacy for some patients. (montes2026ttdexpertconsensus pages 3-5)

### 2.5 Environmental/clinical co-factors
Concomitant exposures and clinical context can modulate risk, including **opioids/NSAIDs** and **radiotherapy site/dose**. (montes2026ttdexpertconsensus pages 3-5)

### 2.6 Protective factors (evidence-supported)
Protective “factors” are largely iatrogenic/behavioral (preventive pharmacotherapy and implementation):
- **Guideline-concordant primary prophylaxis** (prophylaxis before chemotherapy rather than rescue) is emphasized as key for preventing CINV and reducing later problems such as anticipatory CINV. (jeryczynski2026antiemetictherapy pages 1-2, dhabhar2025expertconsensusguidance pages 5-6)

A structured risk/protective/implementation table is provided in **Artifact 02**.

| Category | Factor or metric | Effect/notes | Population/setting | Source context IDs |
|---|---|---|---|---|
| Risk | High emetogenic chemotherapy (HEC) | Defined as >90% risk of vomiting within 24 h without prophylaxis; includes cisplatin, carmustine, dacarbazine, mechlorethamine, streptozocin, high-dose cyclophosphamide, and anthracycline-cyclophosphamide in women with breast cancer | Guideline classification for IV antineoplastic agents | (herrstedt20242023updatedmasccesmo pages 1-2) |
| Risk | Moderate/low/minimal emetogenicity classification | IV agents remain classified in 4 categories; oral agents revised to 2 categories (minimal-low, moderate-high); emetogenicity for oral agents is less precise and heterogeneous across studies | MASCC/ESMO emetogenicity classification update | (jordan2024emeticriskclassification pages 1-2, jordan2024emeticriskclassification pages 4-5) |
| Risk | Female sex | Repeatedly identified as a major patient-related risk factor for CINV; meta-analysis in platinum-treated patients found OR 2.363 (95% CI 1.363-4.096) | General CINV risk; platinum-based chemotherapy | (montes2026ttdexpertconsensus pages 3-5, suzukichiba2024comparisonofolanzapine pages 5-7) |
| Risk | Younger age / age <50 | Reported as a risk factor in expert guidance and risk models; younger age is repeatedly incorporated into prediction tools | General adult oncology populations | (montes2026ttdexpertconsensus pages 3-5, suzukichiba2024comparisonofolanzapine pages 5-7) |
| Risk | Prior CINV / prior vomiting during chemotherapy | Strong predictor of subsequent-cycle CINV; prior history significantly predicts later-cycle events; history of vomiting during chemotherapy OR 2.728 in platinum meta-analysis | Subsequent chemotherapy cycles; platinum-based chemotherapy | (rapoport20242023updatedmasccesmo pages 5-6, suzukichiba2024comparisonofolanzapine pages 5-7) |
| Risk | History of pregnancy-related emesis | Listed as a patient-related risk factor | General CINV risk assessment | (montes2026ttdexpertconsensus pages 3-5) |
| Risk | Motion sickness history | Listed as a patient-related risk factor; platinum meta-analysis OR 1.816 (95% CI 1.266-2.605) | General and platinum-based chemotherapy | (montes2026ttdexpertconsensus pages 3-5, suzukichiba2024comparisonofolanzapine pages 5-7) |
| Risk | Anxiety | Included in risk models and meta-analysis; platinum meta-analysis OR 1.689 (95% CI 1.057-2.700) | General and platinum-based chemotherapy | (suzukichiba2024comparisonofolanzapine pages 5-7) |
| Risk | Fatigue | Associated with increased platinum-related CINV risk; meta-analysis OR 1.413 (95% CI 1.145-1.744) | Platinum-based chemotherapy | (suzukichiba2024comparisonofolanzapine pages 5-7) |
| Risk | Concomitant opioids, NSAIDs, radiotherapy site/dose | Co-medications and concomitant radiotherapy may increase emesis burden and modify risk | Clinical practice risk stratification | (montes2026ttdexpertconsensus pages 3-5) |
| Risk | Gastric mucosa retained / no gastrectomy | Review notes gastric mucosa as a primary site of toxicity and that patients without gastrectomy may have higher symptom burden | Gastric cancer/supportive care context | (jeryczynski2026antiemetictherapy pages 1-2) |
| Risk | CYP2D6 ultrarapid metabolizer status | Pharmacogenomic risk factor: may be undertreated with standard 5-HT3 receptor antagonist dosing, implying reduced efficacy in some patients | Precision antiemetic selection / dosing consideration | (montes2026ttdexpertconsensus pages 3-5) |
| Protective | Lower-risk chemotherapy regimens | Receiving lower or minimal emetogenic regimens confers lower baseline CINV risk compared with HEC/MEC | Regimen-level protection by exposure class | (jeryczynski2026antiemetictherapy pages 1-2, jordan2024emeticriskclassification pages 1-2) |
| Protective | Guideline-concordant primary prophylaxis | Prevention before chemotherapy is emphasized as superior to rescue; using recommended 5-HT3 RA/NK1 RA/dexamethasone/olanzapine combinations reduces CINV burden | Across emetogenic risk groups, especially HEC and multiple-day cisplatin | (jeryczynski2026antiemetictherapy pages 1-2, herrstedt20242023updatedmasccesmo pages 1-2, rapoport20242023updatedmasccesmo pages 5-6, herrstedt20242023updatedmasccesmo media aa8b3b03) |
| Protective | Optimal control in cycle 1 | Good control of acute/delayed CINV in the first cycle may help prevent anticipatory CINV in later cycles | Longitudinal supportive care strategy | (dhabhar2025expertconsensusguidance pages 5-6) |
| Implementation | Guideline-consistent prophylaxis use | Review reports only ~50% guideline-consistent use in more recent real-world data; older studies showed only 11-29% appropriate prophylaxis | Real-world oncology practice | (jeryczynski2026antiemetictherapy pages 1-2) |
| Implementation | Physician risk-factor assessment gaps | 11% of surveyed oncologists did not discuss additional personal CINV risk factors with patients | Multinational THRIVE survey, 446 patients | (jeryczynski2026antiemetictherapy pages 1-2) |
| Implementation | MEC prophylaxis underuse of NK1 RA | In patients with additional risk factors on MEC, 39% of surveyed physicians did not include an NK1 RA | Multinational THRIVE survey | (jeryczynski2026antiemetictherapy pages 1-2) |
| Implementation | Delayed CINV assessment gap | 35% of physicians relied only on spontaneous patient reports for delayed CINV assessment | Multinational THRIVE survey | (jeryczynski2026antiemetictherapy pages 1-2) |
| Implementation | Pharmacist intervention | Improved adherence to prophylaxis pharmacotherapy and significantly decreased CINV incidence after pharmacist intervention | Practice-improvement / supportive oncology programs | (suzukichiba2024comparisonofolanzapine pages 1-2) |
| Effectiveness | Breakthrough CINV prevalence despite prophylaxis | Guideline review cites a prospective Japanese multicenter study in which almost half of 1,910 patients experienced breakthrough nausea/vomiting despite prophylactic antiemetics | Patients receiving MEC or HEC | (rapoport20242023updatedmasccesmo pages 5-6) |
| Effectiveness | Olanzapine for breakthrough CINV: overall response | In 127 real-world patients, olanzapine 2.5/5/10 mg/day improved symptoms in 83% and achieved complete response in 33% | Retrospective real-world breakthrough CINV cohort | (uchiike2023olanzapinetreatmenteffectively pages 1-2) |
| Effectiveness | Olanzapine for breakthrough CINV: adverse effects | 27% had olanzapine-related adverse events, mainly somnolence; no grade >=3 adverse events observed | Same breakthrough cohort | (uchiike2023olanzapinetreatmenteffectively pages 1-2) |
| Effectiveness | Olanzapine dose comparison in prophylaxis | Nationwide Japanese database study found 2.5 mg associated with more additional antiemetic use than 5 mg (36% vs 31%, p<0.001) | Patients with lung cancer receiving HEC | (suzukichiba2024comparisonofolanzapine pages 2-4) |
| Effectiveness | Dexamethasone-sparing in AC chemotherapy | Network meta-analysis found essentially no difference in delayed-phase complete response between multiple vs single dexamethasone doses when combined with palonosetron and NK1 RA (difference 0.1%, 95% CI -12.4 to 12.5) | Anthracycline-cyclophosphamide breast cancer regimens | (suzukichiba2024comparisonofolanzapine pages 8-9, herrstedt20242023updatedmasccesmo pages 1-2) |
| Effectiveness | Pediatric antiemetic optimization | In children, NK1 antagonists with ondansetron plus dexamethasone ranked highest for complete/partial response; post hoc analysis suggested added benefit from olanzapine | Pediatric MEC/HEC, 16 RCTs and 3,115 patients | (suzukichiba2024comparisonofolanzapine pages 7-8) |
| Burden | Persistent real-world burden despite advances | Review states that despite advances, over 40% of patients in clinical practice still experience CINV | Clinical practice, especially cisplatin-based settings | (walker2024antiemeticmedicationsfor pages 1-2) |


*Table: This table summarizes evidence-backed CINV risk factors, limited protective factors, and real-world implementation/effectiveness findings, including pharmacogenomic risk, adherence gaps, and olanzapine outcomes. It is useful for knowledge-base curation and risk-stratified supportive care planning.*

## 3. Phenotypes (symptoms/signs), frequencies, and QoL implications
### 3.1 Core phenotypes
- **Nausea** and **vomiting** are the defining symptoms; nausea is repeatedly highlighted as the persistent unmet need even as emesis control improves. (herrstedt20242023updatedmasccesmo pages 7-8, rapoport20242023updatedmasccesmo pages 5-6)
- Suggested HPO:
  - Nausea: **HP:0002018** (candidate mapping based on standard HPO usage)
  - Vomiting: **HP:0002013** (candidate mapping)

### 3.2 Frequencies/data points from recent studies and guideline-cited cohorts
- **Breakthrough CINV burden:** MASCC/ESMO cites a prospective multicenter Japanese study (n=1910 MEC/HEC patients) in which **“almost half of the patients experienced breakthrough nausea and vomiting despite prophylactic use of antiemetics.”** (rapoport20242023updatedmasccesmo pages 5-6)
- **Real-world breakthrough treatment outcomes (olanzapine):** In 127 patients treated for breakthrough CINV refractory to standard therapy, baseline severity was grade 1 (18%), grade 2 (69%), grade 3 (13%); after olanzapine (2.5/5/10 mg/day), **improvement occurred in 83% and complete response in 33%**, with somnolence the most common adverse effect (27%) and no grade ≥3 AEs. (uchiike2023olanzapinetreatmenteffectively pages 1-2)

### 3.3 Quality of life impact
CINV is described as one of the most distressing adverse effects of chemotherapy and a contributor to interruptions/discontinuation in cancer therapy; persistent nausea is emphasized as a key residual problem. (jeryczynski2026antiemetictherapy pages 1-2, herrstedt20242023updatedmasccesmo pages 7-8)

## 4. Genetic / molecular information
CINV is not a monogenic disorder and does not have “causal genes” in the Mendelian sense. Evidence in the provided corpus supports a **pharmacogenomic modifier** concept (e.g., CYP2D6 affecting 5-HT3 receptor antagonist exposure/effect), but does not provide specific variants/allele frequencies suitable for ClinVar-style annotation. (montes2026ttdexpertconsensus pages 3-5)

## 5. Environmental information
For CINV, “environmental” contributors are best conceptualized as **clinical context exposures**:
- Concomitant medications (opioids, NSAIDs) and radiation parameters can influence emesis risk. (montes2026ttdexpertconsensus pages 3-5)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (current mechanistic understanding)
1. **Chemotherapy exposure** damages GI mucosa and/or activates central chemoreceptor pathways.
2. **Peripheral neurotransmitter release** (notably serotonin from enterochromaffin cells) activates vagal afferents and central pathways.
3. **Central integration** in brainstem/emetic circuitry produces nausea/vomiting.

Specific mediator timing:
- **Acute CINV**: linked to **serotonin → 5-HT3 receptor** signaling (GI tract and CNS), with vagal and splanchnic afferent involvement. (montes2026ttdexpertconsensus pages 3-5, aher2025aretrospectivedrug pages 1-3)
- **Delayed CINV**: linked to **substance P → NK1 receptor** signaling. (montes2026ttdexpertconsensus pages 3-5, aher2025aretrospectivedrug pages 1-3)
- **Inflammation/cytokines:** IL-1β, TNF-α, IL-6 can sensitize vagal afferents; IL-33 may stimulate serotonin release, connecting inflammation to emesis. (montes2026ttdexpertconsensus pages 3-5, montes2026ttdexpertconsensus pages 2-3)

### 6.2 Anatomical structures and cell types implicated
- **GI tract / gastric mucosa** (injury/toxicity site). (jeryczynski2026antiemetictherapy pages 1-2)
- **Enterochromaffin cells** (serotonin source). (aher2025aretrospectivedrug pages 1-3, montes2026ttdexpertconsensus pages 2-3)
- **Vagus nerve / vagal afferents**; **afferent splanchnic pathways**. (montes2026ttdexpertconsensus pages 3-5)
- **Chemoreceptor trigger zone (CTZ)** in **area postrema** of the **medulla**; **vomiting center/brainstem**. (aher2025aretrospectivedrug pages 1-3, montes2026ttdexpertconsensus pages 2-3)

Ontology suggestions (candidates; not exhaustively validated in this corpus):
- **UBERON:** stomach, gastrointestinal tract, medulla oblongata, area postrema; vagus nerve.
- **CL:** enterochromaffin cell.
- **GO biological process:** emesis; regulation of neurotransmitter secretion; inflammatory response; vagus nerve signaling.

## 7. Anatomical structures affected
Primary “affected” systems are functional emesis circuits spanning:
- **Digestive system** (gastric mucosa, GI tract). (aher2025aretrospectivedrug pages 1-3, jeryczynski2026antiemetictherapy pages 1-2)
- **Nervous system** (vagus nerve, brainstem/medullary emetic circuitry). (aher2025aretrospectivedrug pages 1-3, montes2026ttdexpertconsensus pages 3-5)

## 8. Temporal development
- Onset is **acute/subacute** and linked to chemotherapy dosing episodes.
- Time-anchored phases are central to management: acute (0–24 h), delayed (24–120 h), and long-delayed (>120 h). (jeryczynski2026antiemetictherapy pages 1-2)

## 9. Inheritance and population
CINV is not inherited in a Mendelian pattern. Population differences may arise from treatment distributions and pharmacogenomics (e.g., CYP2D6 metabolizer phenotypes), but detailed population genetics are not present in the provided corpus. (montes2026ttdexpertconsensus pages 3-5)

## 10. Diagnostics / assessment
CINV is clinically diagnosed and monitored using symptom grading and patient-reported measures.

### 10.1 Clinical assessment tools and endpoints
- **CTCAE grading** is used to classify severity and define improvement (e.g., “downgrade in CINV symptoms”); used in real-world olanzapine study. (uchiike2023olanzapinetreatmenteffectively pages 1-2)
- **Complete response (CR)** commonly defined as **no emetic episodes and no rescue medication**. (rapoport20242023updatedmasccesmo pages 5-6)
- **Visual analog scale (VAS) for nausea**: 0 (no nausea) to 100 mm (worst possible nausea), used as an exploratory nausea endpoint in some studies. (rapoport20242023updatedmasccesmo pages 5-6)

### 10.2 Differential diagnosis (important in breakthrough/persistent symptoms)
MASCC/ESMO emphasizes considering non-chemotherapy causes of persistent nausea/vomiting, including:
- Gastrointestinal: constipation, mucositis, hepatic metastases.
- Neurological: CNS metastases.
- Metabolic: electrolyte abnormalities.
- Drug-related: narcotics, antibiotics.
- Psychophysiological causes. (rapoport20242023updatedmasccesmo pages 5-6)

## 11. Outcomes / prognosis
CINV rarely affects long-term survival directly but substantially impacts tolerability and supportive-care burden.

### 11.1 Persistent burden despite prophylaxis
In clinical practice, **“over 40%”** of patients still experience CINV despite major antiemetic advances. (sun2024theevolvinglandscape pages 1-2)

### 11.2 Quantitative trial-level improvements (cisplatin RCT landscape)
A 2024 analysis of 156 cisplatin-based RCTs reported stepwise improvements in vomiting control aligned with major antiemetic eras:
- No-vomiting improved from **40.30% → 54.18%** after 5-HT3RA-based doublets and then to **66.01%** after NK1RA-based triplets. (sun2024theevolvinglandscape pages 2-5)
- Acute-phase no-vomiting improved from **50.46% → 76.98%** with 5-HT3RA+glucocorticoid vs 5-HT3RA alone, and to **91.30%** after adding an NK1RA. (sun2024theevolvinglandscape pages 2-5)
However, nausea control improvements were modest and nausea outcomes were frequently underreported in antiemetic trials. (sun2024theevolvinglandscape pages 1-2, sun2024theevolvinglandscape pages 2-5)

## 12. Treatment (and real-world implementation)
### 12.1 Guideline-based pharmacologic prophylaxis (2023 MASCC/ESMO updates; published online 2023, in 2024 journal issue)
The MASCC/ESMO 2023 update for high-emetic-risk chemotherapy emphasizes:
- **Olanzapine as a fixed component of a four-drug prophylactic regimen** for both AC and non-AC HEC. (herrstedt20242023updatedmasccesmo pages 1-2)
- **Steroid-sparing for AC HEC:** “no need to prescribe steroids (dexamethasone) beyond day 1 after AC HEC,” while non-AC HEC retains a multi-day dexamethasone regimen. (herrstedt20242023updatedmasccesmo pages 1-2, herrstedt20242023updatedmasccesmo pages 7-8)
Visual evidence from the guideline summary table is provided in **Table 2 image** (MASCC/ESMO high-risk update). (herrstedt20242023updatedmasccesmo media aa8b3b03)

A structured regimen summary is provided in **Artifact 01**.

| Setting | Recommended prophylaxis/rescue regimen components | Dexamethasone schedule notes | Olanzapine notes | Evidence/remarks |
|---|---|---|---|---|
| High-emetic-risk chemotherapy (HEC), anthracycline-cyclophosphamide (AC) | 4-drug prophylaxis: 5-HT3 receptor antagonist + NK1 receptor antagonist + dexamethasone + olanzapine (herrstedt20242023updatedmasccesmo pages 1-2, herrstedt20242023updatedmasccesmo media aa8b3b03) | No need to prescribe dexamethasone beyond day 1 after AC HEC; day-1-only steroid approach supported in the 2023 update (herrstedt20242023updatedmasccesmo pages 1-2, herrstedt20242023updatedmasccesmo media aa8b3b03) | Olanzapine is now a fixed part of the 4-drug regimen; Table 2 notes dosing before chemotherapy on day 1 then daily on days 2-4, with 5 mg a starting option if sedation is a concern (herrstedt20242023updatedmasccesmo pages 7-8, herrstedt20242023updatedmasccesmo media aa8b3b03) | MASCC/ESMO 2023 high-risk update identified 46 relevant references and concluded olanzapine should be incorporated into both AC and non-AC HEC prophylaxis (herrstedt20242023updatedmasccesmo pages 1-2) |
| High-emetic-risk chemotherapy (HEC), non-AC (e.g., cisplatin-based) | 4-drug prophylaxis: 5-HT3 receptor antagonist + NK1 receptor antagonist + dexamethasone + olanzapine (herrstedt20242023updatedmasccesmo pages 1-2, herrstedt20242023updatedmasccesmo media aa8b3b03) | For non-AC HEC, a 4-day dexamethasone regimen is recommended; evidence for limiting dexamethasone after cisplatin/non-AC HEC was considered inconclusive (herrstedt20242023updatedmasccesmo pages 1-2, herrstedt20242023updatedmasccesmo pages 7-8, herrstedt20242023updatedmasccesmo media aa8b3b03) | Olanzapine is recommended as a fixed part of prophylaxis; Table 2 indicates administration before chemotherapy on day 1 and daily on days 2-4, commonly 10 mg with 5 mg reasonable if sedation risk is important (herrstedt20242023updatedmasccesmo pages 7-8, herrstedt20242023updatedmasccesmo media aa8b3b03) | The guideline found no major differences between 5-HT3 receptor antagonists or between NK1 receptor antagonists for HEC prophylaxis (herrstedt20242023updatedmasccesmo pages 1-2) |
| Multiple-day cisplatin chemotherapy | 5-HT3 receptor antagonist once daily on chemotherapy days + dexamethasone once daily from day 1 until 2 days post-chemotherapy + aprepitant 125 mg day 1 then 80 mg daily from day 2 until 2 days post-chemotherapy + olanzapine 5 mg once daily from day 1 until 2 days post-chemotherapy (rapoport20242023updatedmasccesmo pages 1-2, rapoport20242023updatedmasccesmo pages 5-6) | Continue dexamethasone daily from day 1 through 2 days after chemotherapy; concern about late corticosteroid toxicity is specifically noted in the discussion (rapoport20242023updatedmasccesmo pages 5-6) | Olanzapine 5 mg once daily from day 1 until 2 days post-chemotherapy; note recommends giving olanzapine at bedtime (rapoport20242023updatedmasccesmo pages 5-6) | Recommendation graded I/A overall, but II/B for number of days; palonosetron may be used on days 1, 3, and 5 if chemotherapy lasts 5 days (rapoport20242023updatedmasccesmo pages 5-6) |
| High-dose chemotherapy with stem cell transplant / HSCT | 5-HT3 receptor antagonist + dexamethasone + aprepitant recommended; olanzapine may be considered as part of the regimen (rapoport20242023updatedmasccesmo pages 1-2) | Specific dexamethasone day-by-day schedule not detailed in the extracted evidence; recommendation is to include dexamethasone in combination prophylaxis (rapoport20242023updatedmasccesmo pages 1-2) | Olanzapine is not mandatory in the extracted wording but may be considered; guideline notes it as an important advance for improving prevention in high-dose chemotherapy/autologous transplant settings (rapoport20242023updatedmasccesmo pages 1-2) | The 2023 update reviewed literature from 2015-2023 and updated recommendations for HDC/HSCT patients, emphasizing persistent clinical significance of nausea in this population (rapoport20242023updatedmasccesmo pages 1-2) |
| Breakthrough CINV | Use olanzapine if not used for primary prophylaxis; evidence supports a single daily dose for 3 days (rapoport20242023updatedmasccesmo pages 1-2, rapoport20242023updatedmasccesmo pages 5-6) | No dexamethasone rescue schedule recommendation identified in the extracted guideline evidence (rapoport20242023updatedmasccesmo pages 1-2, rapoport20242023updatedmasccesmo pages 5-6) | Some evidence supports olanzapine 10 mg once daily for 3 days; meta-analytic evidence favored olanzapine in the breakthrough setting, and 5 mg may be considered to reduce side effects although optimal dose remains unsettled (rapoport20242023updatedmasccesmo pages 1-2, rapoport20242023updatedmasccesmo pages 5-6) | Breakthrough CINV is defined as nausea/vomiting during chemotherapy despite guideline-directed prophylaxis; guideline recommendation level reported as II/B (rapoport20242023updatedmasccesmo pages 5-6) |


*Table: This table summarizes the key 2023-2024 MASCC/ESMO guideline-update recommendations for major CINV settings supported by the retrieved evidence. It highlights regimen components, dexamethasone duration, and where olanzapine is fixed, optional, or recommended for rescue.*

### 12.2 Multiple-day cisplatin prophylaxis (MASCC/ESMO 2023 update)
For multiple-day cisplatin, MASCC/ESMO recommends **5-HT3RA + dexamethasone + aprepitant + olanzapine**, with explicit dosing schedules and bedtime olanzapine suggested. (rapoport20242023updatedmasccesmo pages 5-6)

### 12.3 HSCT / high-dose chemotherapy
For high-dose chemotherapy with stem cell transplantation, MASCC/ESMO recommends **5-HT3RA + dexamethasone + aprepitant**, with olanzapine as a consideration. (rapoport20242023updatedmasccesmo pages 1-2)

### 12.4 Breakthrough CINV (rescue)
MASCC/ESMO recommends olanzapine for breakthrough CINV if it was not used in prophylaxis, with evidence supporting daily dosing for 3 days. (rapoport20242023updatedmasccesmo pages 1-2, rapoport20242023updatedmasccesmo pages 5-6)

### 12.5 Dose optimization and real-world effectiveness
- **Breakthrough treatment effectiveness:** real-world cohort showed 83% improvement and 33% complete response with olanzapine. (uchiike2023olanzapinetreatmenteffectively pages 1-2)
- **Prophylaxis dose comparison (Japan 2024):** 2.5 mg olanzapine was associated with higher additional antiemetic use than 5 mg (36% vs 31%, p<0.001) with similar length of stay (8 days) and similar hospitalization cost (5061 vs 5160 USD, p=0.07). (suzukichiba2024comparisonofolanzapine pages 1-2)

### 12.6 Pediatric antiemetics (2024 systematic review and Bayesian network meta-analysis)
A 2024 pediatric NMA (16 RCTs; 3115 patients) found that, when given with dexamethasone, **NK1 antagonists with ondansetron ranked highest** for several complete/partial response outcomes; palonosetron performed better than ondansetron for delayed/overall CR and nausea prevention; and post hoc analysis suggested benefit from **adding olanzapine** to aprepitant+ondansetron regimens. (walker2024antiemeticmedicationsfor pages 1-2)

### 12.7 Implementation science: adherence gaps and pharmacist interventions
- Reviews note guideline adherence is often suboptimal (historically 11–29% appropriate prophylaxis; more recently ~50% guideline-consistent use). (jeryczynski2026antiemetictherapy pages 1-2)
- A pharmacist-led intervention increased delayed-phase guideline adherence from **6.6% to 89%** and improved delayed complete protection from **54% to 74%** (P<0.05) in an mCRC MEC setting, illustrating real-world implementation gains. (fujii2024pharmacistinterventionand pages 2-5)

### Suggested MAXO terms (candidates)
- Antiemetic prophylaxis
- Administration of 5-HT3 receptor antagonist
- Administration of NK1 receptor antagonist
- Administration of corticosteroid therapy (dexamethasone)
- Administration of olanzapine

### Suggested CHEBI entities (candidates)
- Dexamethasone
- Olanzapine
- Aprepitant / fosaprepitant
- Palonosetron / ondansetron / granisetron
- Netupitant (as NEPA when combined with palonosetron)

## 13. Prevention
Primary prevention is largely **pharmacologic prophylaxis matched to emetogenic risk**, emphasizing correct upfront regimens over rescue therapy. (jeryczynski2026antiemetictherapy pages 1-2, rapoport20242023updatedmasccesmo pages 5-6)

A key prevention concept is that optimal control in cycle 1 helps prevent **anticipatory CINV** in later cycles. (dhabhar2025expertconsensusguidance pages 5-6)

## 14. Other species / natural disease
Not applicable as a naturally occurring disease entity; this is iatrogenic and treatment-triggered.

## 15. Model organisms
Not represented in the retrieved corpus; mechanistic understanding in these sources is primarily human clinical/pharmacologic.

---

## Direct abstract quotes supporting key statements (selected)
- MASCC/ESMO multiple-day/high-dose/breakthrough update: “CINV, particularly nausea, remains a clinically significant side effect for patients receiving high-dose chemotherapy.” (rapoport20242023updatedmasccesmo pages 1-2)
- Sun 2024 cisplatin RCT landscape (abstract-level): “Despite the significant advancements in antiemetic regimens… over 40% of cancer patients undergoing chemotherapy still experience CINV in clinical practice.” (sun2024theevolvinglandscape pages 1-2)
- Pharmacist intervention review: “After intervention by pharmacists, the rate of adherence to prophylaxis pharmacotherapy for these AEs was significantly improved, and the incidence of CINV… was significantly decreased.” (fujii2024pharmacistinterventionand pages 1-2)

---

## Notes on evidence limitations for knowledge-base population
- Ontology identifiers (MONDO/MeSH/ICD) were not recoverable from the retrieved documents and should be sourced from dedicated ontology resources (e.g., MeSH Browser, ICD-10/ICD-11, MONDO) before final KB ingestion.
- Genetic variant-level annotations (ClinVar-style) are not supported by the current evidence set; only a high-level CYP2D6 pharmacogenomic effect is available.


References

1. (jeryczynski2026antiemetictherapy pages 1-2): Georg Jeryczynski. Antiemetic therapy. memo - Magazine of European Medical Oncology, Jan 2026. URL: https://doi.org/10.1007/s12254-025-01098-5, doi:10.1007/s12254-025-01098-5. This article has 0 citations.

2. (montes2026ttdexpertconsensus pages 3-5): Ana Fernández Montes, Ismael Macías Declara, Nieves Martínez Lago, Virginia Arrazubi, Beatriz García Paredes, and Paula Jiménez Fonseca. Ttd expert consensus on emesis in gastric cancer: evidence-based strategies for prevention and treatment. Clinical & translational oncology : official publication of the Federation of Spanish Oncology Societies and of the National Cancer Institute of Mexico, Jul 2026. URL: https://doi.org/10.1007/s12094-025-03982-2, doi:10.1007/s12094-025-03982-2. This article has 0 citations.

3. (rapoport20242023updatedmasccesmo pages 5-6): Bernardo Leon Rapoport, Jørn Herrstedt, Rebecca Clark Snow, Venkatraman Radhakrishnan, Mitsue Saito, Rudolph M. Navari, and Teresa Smit. 2023 updated mascc/esmo consensus recommendations: prevention of nausea and vomiting following multiple-day chemotherapy, high-dose chemotherapy, and breakthrough nausea and vomiting. Supportive Care in Cancer, Dec 2024. URL: https://doi.org/10.1007/s00520-023-08224-1, doi:10.1007/s00520-023-08224-1. This article has 23 citations and is from a peer-reviewed journal.

4. (herrstedt20242023updatedmasccesmo pages 1-2): J. Herrstedt, L. Celio, P. Hesketh, L. Zhang, R. Navari, A. Chan, M. Saito, R. Chow, and M. Aapro. 2023 updated mascc/esmo consensus recommendations: prevention of nausea and vomiting following high-emetic-risk antineoplastic agents. Supportive Care in Cancer, Dec 2024. URL: https://doi.org/10.1007/s00520-023-08221-4, doi:10.1007/s00520-023-08221-4. This article has 36 citations and is from a peer-reviewed journal.

5. (rapoport20242023updatedmasccesmo pages 1-2): Bernardo Leon Rapoport, Jørn Herrstedt, Rebecca Clark Snow, Venkatraman Radhakrishnan, Mitsue Saito, Rudolph M. Navari, and Teresa Smit. 2023 updated mascc/esmo consensus recommendations: prevention of nausea and vomiting following multiple-day chemotherapy, high-dose chemotherapy, and breakthrough nausea and vomiting. Supportive Care in Cancer, Dec 2024. URL: https://doi.org/10.1007/s00520-023-08224-1, doi:10.1007/s00520-023-08224-1. This article has 23 citations and is from a peer-reviewed journal.

6. (sun2024theevolvinglandscape pages 1-2): Ya Sun, Yalan Wang, Gang Chen, Yaxiong Zhang, Li Zhang, and Xi Chen. The evolving landscape of antiemetic prophylaxis for chemotherapy-induced nausea and vomiting: inspiration from cisplatin-based antiemetic and non-antiemetic trials. Supportive Care in Cancer, Nov 2024. URL: https://doi.org/10.1007/s00520-024-09035-8, doi:10.1007/s00520-024-09035-8. This article has 2 citations and is from a peer-reviewed journal.

7. (uchiike2023olanzapinetreatmenteffectively pages 1-2): Akihiro Uchiike, Haruka Kono, Katsuhiro Miura, Tatsuya Hayama, Daisuke Tsutsumi, Shinya Tsuboi, Susumu Ohtsuka, and Shinji Hidaka. Olanzapine treatment effectively relieves breakthrough chemotherapy-induced nausea and vomiting: a real-world experience. Journal of Pharmaceutical Health Care and Sciences, Aug 2023. URL: https://doi.org/10.1186/s40780-023-00293-y, doi:10.1186/s40780-023-00293-y. This article has 3 citations.

8. (dhabhar2025expertconsensusguidance pages 5-6): Boman Dhabhar, Prabrajya N Mahapatra, Vamshi M Krishna, Jatin Sarin, Tara Chand Gupta, Aseem Samar, Bivas Biswas, Aditya Murli, Rajesh Kota, Suyash Bharat, and Richa Tripathi. Expert consensus guidance on the management of chemotherapy-induced nausea and vomiting: an indian perspective. Cureus, May 2025. URL: https://doi.org/10.7759/cureus.84070, doi:10.7759/cureus.84070. This article has 0 citations.

9. (aher2025aretrospectivedrug pages 1-3): Ashwini A. Aher, S. U. Razvi, and M. S. Baig. A retrospective drug utilization study in chemotherapy-induced nausea and vomiting. International Journal of Research in Medical Sciences, 13:2010-2017, Apr 2025. URL: https://doi.org/10.18203/2320-6012.ijrms20251304, doi:10.18203/2320-6012.ijrms20251304. This article has 0 citations.

10. (jordan2024emeticriskclassification pages 1-2): Karin Jordan, Alexandre Chan, Richard J. Gralla, Franziska Jahn, Bernardo Rapoport, Christina H. Ruhlmann, Paula Sayegh, and Paul J. Hesketh. Emetic risk classification and evaluation of the emetogenicity of antineoplastic agents—updated mascc/esmo consensus recommendation. Supportive Care in Cancer, Dec 2024. URL: https://doi.org/10.1007/s00520-023-08220-5, doi:10.1007/s00520-023-08220-5. This article has 32 citations and is from a peer-reviewed journal.

11. (suzukichiba2024comparisonofolanzapine pages 5-7): Hiroe Suzuki-Chiba, Takaaki Konishi, Shotaro Aso, Kanako Makito, Hiroki Matsui, Taisuke Jo, Kiyohide Fushimi, and Hideo Yasunaga. Comparison of olanzapine 2.5 mg and 5 mg in the prevention of chemotherapy-induced nausea and vomiting: a japanese nationwide database study. International Journal of Clinical Oncology, 29:1762-1773, Aug 2024. URL: https://doi.org/10.1007/s10147-024-02603-2, doi:10.1007/s10147-024-02603-2. This article has 2 citations and is from a peer-reviewed journal.

12. (jordan2024emeticriskclassification pages 4-5): Karin Jordan, Alexandre Chan, Richard J. Gralla, Franziska Jahn, Bernardo Rapoport, Christina H. Ruhlmann, Paula Sayegh, and Paul J. Hesketh. Emetic risk classification and evaluation of the emetogenicity of antineoplastic agents—updated mascc/esmo consensus recommendation. Supportive Care in Cancer, Dec 2024. URL: https://doi.org/10.1007/s00520-023-08220-5, doi:10.1007/s00520-023-08220-5. This article has 32 citations and is from a peer-reviewed journal.

13. (herrstedt20242023updatedmasccesmo media aa8b3b03): J. Herrstedt, L. Celio, P. Hesketh, L. Zhang, R. Navari, A. Chan, M. Saito, R. Chow, and M. Aapro. 2023 updated mascc/esmo consensus recommendations: prevention of nausea and vomiting following high-emetic-risk antineoplastic agents. Supportive Care in Cancer, Dec 2024. URL: https://doi.org/10.1007/s00520-023-08221-4, doi:10.1007/s00520-023-08221-4. This article has 36 citations and is from a peer-reviewed journal.

14. (suzukichiba2024comparisonofolanzapine pages 1-2): Hiroe Suzuki-Chiba, Takaaki Konishi, Shotaro Aso, Kanako Makito, Hiroki Matsui, Taisuke Jo, Kiyohide Fushimi, and Hideo Yasunaga. Comparison of olanzapine 2.5 mg and 5 mg in the prevention of chemotherapy-induced nausea and vomiting: a japanese nationwide database study. International Journal of Clinical Oncology, 29:1762-1773, Aug 2024. URL: https://doi.org/10.1007/s10147-024-02603-2, doi:10.1007/s10147-024-02603-2. This article has 2 citations and is from a peer-reviewed journal.

15. (suzukichiba2024comparisonofolanzapine pages 2-4): Hiroe Suzuki-Chiba, Takaaki Konishi, Shotaro Aso, Kanako Makito, Hiroki Matsui, Taisuke Jo, Kiyohide Fushimi, and Hideo Yasunaga. Comparison of olanzapine 2.5 mg and 5 mg in the prevention of chemotherapy-induced nausea and vomiting: a japanese nationwide database study. International Journal of Clinical Oncology, 29:1762-1773, Aug 2024. URL: https://doi.org/10.1007/s10147-024-02603-2, doi:10.1007/s10147-024-02603-2. This article has 2 citations and is from a peer-reviewed journal.

16. (suzukichiba2024comparisonofolanzapine pages 8-9): Hiroe Suzuki-Chiba, Takaaki Konishi, Shotaro Aso, Kanako Makito, Hiroki Matsui, Taisuke Jo, Kiyohide Fushimi, and Hideo Yasunaga. Comparison of olanzapine 2.5 mg and 5 mg in the prevention of chemotherapy-induced nausea and vomiting: a japanese nationwide database study. International Journal of Clinical Oncology, 29:1762-1773, Aug 2024. URL: https://doi.org/10.1007/s10147-024-02603-2, doi:10.1007/s10147-024-02603-2. This article has 2 citations and is from a peer-reviewed journal.

17. (suzukichiba2024comparisonofolanzapine pages 7-8): Hiroe Suzuki-Chiba, Takaaki Konishi, Shotaro Aso, Kanako Makito, Hiroki Matsui, Taisuke Jo, Kiyohide Fushimi, and Hideo Yasunaga. Comparison of olanzapine 2.5 mg and 5 mg in the prevention of chemotherapy-induced nausea and vomiting: a japanese nationwide database study. International Journal of Clinical Oncology, 29:1762-1773, Aug 2024. URL: https://doi.org/10.1007/s10147-024-02603-2, doi:10.1007/s10147-024-02603-2. This article has 2 citations and is from a peer-reviewed journal.

18. (walker2024antiemeticmedicationsfor pages 1-2): R. Walker, S. Dias, and R. S. Phillips. Antiemetic medications for preventing chemotherapy-induced nausea and vomiting in children: a systematic review and bayesian network meta-analysis. Supportive Care in Cancer, Oct 2024. URL: https://doi.org/10.1007/s00520-024-08939-9, doi:10.1007/s00520-024-08939-9. This article has 1 citations and is from a peer-reviewed journal.

19. (herrstedt20242023updatedmasccesmo pages 7-8): J. Herrstedt, L. Celio, P. Hesketh, L. Zhang, R. Navari, A. Chan, M. Saito, R. Chow, and M. Aapro. 2023 updated mascc/esmo consensus recommendations: prevention of nausea and vomiting following high-emetic-risk antineoplastic agents. Supportive Care in Cancer, Dec 2024. URL: https://doi.org/10.1007/s00520-023-08221-4, doi:10.1007/s00520-023-08221-4. This article has 36 citations and is from a peer-reviewed journal.

20. (montes2026ttdexpertconsensus pages 2-3): Ana Fernández Montes, Ismael Macías Declara, Nieves Martínez Lago, Virginia Arrazubi, Beatriz García Paredes, and Paula Jiménez Fonseca. Ttd expert consensus on emesis in gastric cancer: evidence-based strategies for prevention and treatment. Clinical & translational oncology : official publication of the Federation of Spanish Oncology Societies and of the National Cancer Institute of Mexico, Jul 2026. URL: https://doi.org/10.1007/s12094-025-03982-2, doi:10.1007/s12094-025-03982-2. This article has 0 citations.

21. (sun2024theevolvinglandscape pages 2-5): Ya Sun, Yalan Wang, Gang Chen, Yaxiong Zhang, Li Zhang, and Xi Chen. The evolving landscape of antiemetic prophylaxis for chemotherapy-induced nausea and vomiting: inspiration from cisplatin-based antiemetic and non-antiemetic trials. Supportive Care in Cancer, Nov 2024. URL: https://doi.org/10.1007/s00520-024-09035-8, doi:10.1007/s00520-024-09035-8. This article has 2 citations and is from a peer-reviewed journal.

22. (fujii2024pharmacistinterventionand pages 2-5): Hironori Fujii. Pharmacist intervention and identification of adverse events related to treatment efficacy in cancer chemotherapy to improve clinical outcomes. Journal of Pharmaceutical Health Care and Sciences, Dec 2024. URL: https://doi.org/10.1186/s40780-024-00403-4, doi:10.1186/s40780-024-00403-4. This article has 5 citations.

23. (fujii2024pharmacistinterventionand pages 1-2): Hironori Fujii. Pharmacist intervention and identification of adverse events related to treatment efficacy in cancer chemotherapy to improve clinical outcomes. Journal of Pharmaceutical Health Care and Sciences, Dec 2024. URL: https://doi.org/10.1186/s40780-024-00403-4, doi:10.1186/s40780-024-00403-4. This article has 5 citations.

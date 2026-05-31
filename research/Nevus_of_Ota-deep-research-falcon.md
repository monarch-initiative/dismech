---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T12:34:31.262685'
end_time: '2026-05-11T12:47:59.381060'
duration_seconds: 808.12
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Nevus of Ota
  mondo_id: ''
  category: Skin Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Nevus of Ota
- **MONDO ID:**  (if available)
- **Category:** Skin Disorder

## Research Objectives

Please provide a comprehensive research report on **Nevus of Ota** covering all of the
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
- **Disease Name:** Nevus of Ota
- **MONDO ID:**  (if available)
- **Category:** Skin Disorder

## Research Objectives

Please provide a comprehensive research report on **Nevus of Ota** covering all of the
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


## Comprehensive Research Report: Nevus of Ota (Oculodermal Melanocytosis)

### Target disease
Nevus of Ota is a congenital (occasionally later-appearing) dermal melanocytosis characterized by blue/gray or brown macular pigmentation involving skin and ocular tissues in the distribution of trigeminal nerve branches, with important ophthalmic complications including glaucoma and elevated risk of uveal melanoma. (abdolrahimzadeh2023anupdateon pages 1-3, williams2021melanomainthe pages 1-2, vishnevskiadai2021naevusofota pages 1-2)

| Domain | Finding | Population/Study | Year | Source (with URL) | Evidence ID |
|---|---|---|---|---|---|
| Epidemiology | Incidence in Asians: 1–2 per 1,000 | Review of oculodermal melanocytosis / Nevus of Ota | 2023 | Abdolrahimzadeh et al., *Graefe's Archive for Clinical and Experimental Ophthalmology*; https://doi.org/10.1007/s00417-022-05743-1 | (abdolrahimzadeh2023anupdateon pages 1-3) |
| Epidemiology | Prevalence in Japanese dermatology patients: ~0.4–0.8% | Review citing Japanese data | 2021 | Williams et al., *International Journal of Dermatology*; https://doi.org/10.1111/ijd.15135 | (williams2021melanomainthe pages 1-2) |
| Epidemiology | Prevalence in Black persons reported as 0.014% (1/6,915); older review also cites Asian prevalence 0.014–0.034% in one summary source | Historical prevalence study / review snippet | 1982 / 2017 | Gonder et al., *Ophthalmology*; https://doi.org/10.1016/S0161-6420(82)34695-3; Plateroti et al., *Seminars in Ophthalmology*; https://doi.org/10.3109/08820538.2015.1118133 | (abdolrahimzadeh2023anupdateon pages 1-3) |
| Epidemiology | Unilateral involvement: one eye in 90% of cases | Review of ODM | 2023 | Abdolrahimzadeh et al.; https://doi.org/10.1007/s00417-022-05743-1 | (abdolrahimzadeh2023anupdateon pages 1-3) |
| Epidemiology | Female predominance: women affected about 5:1 vs men | Review of ODM / melanoma review | 2023 / 2021 | Abdolrahimzadeh et al.; https://doi.org/10.1007/s00417-022-05743-1; Williams et al.; https://doi.org/10.1111/ijd.15135 | (abdolrahimzadeh2023anupdateon pages 1-3, williams2021melanomainthe pages 1-2) |
| Ocular / tissue involvement | Periocular skin only in ~1/3 of cases; ocular tissue involvement in 66% | Review of ODM | 2023 | Abdolrahimzadeh et al.; https://doi.org/10.1007/s00417-022-05743-1 | (abdolrahimzadeh2023anupdateon pages 1-3) |
| Ocular / tissue involvement | In infant cohort, 55/102 had periorbital skin lesions and 46/102 had ipsilateral scleral involvement | Infant laser cohort | 2024 | Zheng et al., *Clinical, Cosmetic and Investigational Dermatology*; https://doi.org/10.2147/CCID.S444410 | (zheng2024resultsandfollowup pages 1-2) |
| Complications | Main ophthalmic complications are glaucoma and predisposition to uveal melanoma | Review of ODM | 2023 | Abdolrahimzadeh et al.; https://doi.org/10.1007/s00417-022-05743-1 | (abdolrahimzadeh2023anupdateon pages 1-3) |
| Complications | Uveal melanoma in ODM carries about twice the metastatic risk of uveal melanoma without ODM | Review of ODM | 2023 | Abdolrahimzadeh et al.; https://doi.org/10.1007/s00417-022-05743-1 | (abdolrahimzadeh2023anupdateon pages 1-3) |
| Complications | In one 40-patient ocular series, 4 developed glaucoma and 3 developed choroidal melanoma | Retrospective ocular series | 2021 | Vishnevskia-Dai et al., *British Journal of Ophthalmology*; https://doi.org/10.1136/bjophthalmol-2019-313984 | (vishnevskiadai2021naevusofota pages 1-1, vishnevskiadai2021naevusofota pages 1-2) |
| Treatment outcomes | Success rate 88.7% after 4 sessions | 102 infants treated sequentially with Q-switched 755 nm then 1064 nm lasers | 2024 | Zheng et al.; https://doi.org/10.2147/CCID.S444410 | (zheng2024resultsandfollowup pages 1-2) |
| Treatment outcomes | Success rate 99.3% after 7 sessions | Same infant cohort | 2024 | Zheng et al.; https://doi.org/10.2147/CCID.S444410 | (zheng2024resultsandfollowup pages 1-2) |
| Treatment outcomes | Recurrence 14/47 = 29.8% on follow-up; retreatment with 2–3 additional sessions was effective | Follow-up subset of infant cohort | 2024 | Zheng et al.; https://doi.org/10.2147/CCID.S444410 | (zheng2024resultsandfollowup pages 1-2, zheng2024resultsandfollowup pages 4-6) |
| Treatment outcomes | Satisfaction rate 95.5% | Follow-up subset of infant cohort | 2024 | Zheng et al.; https://doi.org/10.2147/CCID.S444410 | (zheng2024resultsandfollowup pages 4-6) |
| Treatment outcomes | No serious adverse reactions except pain in abstract; detailed follow-up text reports no scars, pigment deepening, or hypopigmentation, with intact skin in all 47 followed children | Infant laser cohort | 2024 | Zheng et al.; https://doi.org/10.2147/CCID.S444410 | (zheng2024resultsandfollowup pages 1-2, zheng2024resultsandfollowup pages 4-6) |
| Treatment outcomes | Historical/literature-based success rate cited in trial record: 95% after 6–8 sessions with Q-switched lasers | ClinicalTrials.gov retrospective protocol in Thai patients | 2020 | NCT04481178; https://clinicaltrials.gov/study/NCT04481178 | (NCT04481178 chunk 1) |
| Treatment outcomes | Reported laser complications in trial record: hypopigmentation 15.3%, hyperpigmentation 2.9%, texture changes 2.9%, scarring 1.9% | ClinicalTrials.gov retrospective protocol in Thai patients | 2020 | NCT04481178; https://clinicaltrials.gov/study/NCT04481178 | (NCT04481178 chunk 1) |
| Identifier | MeSH term/ID: Nevus of Ota, D009507 | ClinicalTrials.gov indexed record | 2020 | NCT04481178; https://clinicaltrials.gov/study/NCT04481178 | (NCT04481178 chunk 1) |


*Table: This table compiles the main quantitative findings retrieved for Nevus of Ota / oculodermal melanocytosis, including epidemiology, ocular involvement, complication risks, and recent laser-treatment outcomes. It is useful as a compact evidence summary for knowledge-base population and citation tracking.*

---

## 1. Disease Information

### 1.1 Overview (definition; current understanding)
Nevus of Ota is described as a benign dermal melanocytic lesion with typical unilateral blue-gray macules/patches along the ophthalmic (V1) and maxillary (V2) trigeminal distributions, frequently with ocular involvement. (williams2021melanomainthe pages 1-2)

An ophthalmology-focused review defines oculodermal melanocytosis (ODM; Nevus of Ota) as a “rare, prevalently unilateral, congenital condition” presenting with “brown or blue/gray flat asymptomatic lesions of the skin, mucosae, episclera/sclera, and uvea” in trigeminal territory. (abdolrahimzadeh2023anupdateon pages 1-3)

### 1.2 Key identifiers (ontology and coding)
* **MeSH descriptor**: *Nevus of Ota* (MeSH ID **D009507**) is explicitly present in a ClinicalTrials.gov record for laser treatment outcomes (NCT04481178). (NCT04481178 chunk 1)
* **ICD-10/ICD-11, OMIM, Orphanet, MONDO**: Not present in the retrieved full texts in this tool run; therefore these identifiers cannot be confirmed from the provided evidence corpus. (NCT04481178 chunk 1)

### 1.3 Common synonyms / alternative names
* **Oculodermal melanocytosis / oculodermal melanosis** (vishnevskiadai2021naevusofota pages 1-2, zheng2024resultsandfollowup pages 1-2)
* **Nevus fuscoceruleus ophthalmomaxillaris** (williams2021melanomainthe pages 1-2, vishnevskiadai2021naevusofota pages 1-2)

### 1.4 Evidence source type
The information in this report is derived from a mixture of aggregated disease-level reviews and case-series/cohort clinical studies (e.g., multimodal imaging review; retrospective ocular case series; infant laser cohort), plus case-based molecular reports relevant to genetic mechanisms and malignant transformation. (vishnevskiadai2021naevusofota pages 1-1, abdolrahimzadeh2023anupdateon pages 1-3, zheng2024resultsandfollowup pages 1-2, toomey2019gnaqandpms1 pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic/developmental)
Multiple sources frame Nevus of Ota/ODM as a neural crest developmental melanocytosis. The 2023 ophthalmology review links etiopathogenesis to altered migration of neural crest melanoblasts in embryogenesis. (abdolrahimzadeh2023anupdateon pages 1-3)

### 2.2 Risk factors
* **Sex**: Marked female predominance is repeatedly reported; the ODM review states women are “five times more afflicted.” (abdolrahimzadeh2023anupdateon pages 1-3)
* **Ethnicity/skin phototype**: Higher incidence in Asians is reported (e.g., incidence 1–2 per 1000). (abdolrahimzadeh2023anupdateon pages 1-3)

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved texts. (abdolrahimzadeh2023anupdateon pages 1-3)

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence was not retrieved. However, UV exposure is discussed as a clinical factor potentially affecting recurrence after laser treatment in infants (sun exposure associated with recurrence/worsening). (zheng2024resultsandfollowup pages 1-2)

---

## 3. Phenotypes

### 3.1 Core phenotypes and clinical characteristics
**Cutaneous phenotype (blue/gray/brown macules/patches)**
* **Type**: Clinical sign (pigmentary macules/patches).
* **Typical distribution**: V1/V2 trigeminal territory; often unilateral. (williams2021melanomainthe pages 1-2, abdolrahimzadeh2023anupdateon pages 1-3)
* **Laterality frequency**: “ODM occurs in just one eye in 90% of cases” in the 2023 review. (abdolrahimzadeh2023anupdateon pages 1-3)

**Ocular tissue melanocytosis (episclera/sclera/uvea) and related findings**
* **Type**: Clinical sign; ocular structural pigmentation.
* **Frequency of ocular tissue involvement**: Review reports “additional involvement of ocular tissues … in 66%” and periocular skin alone in about one-third. (abdolrahimzadeh2023anupdateon pages 1-3)

**Oral mucosal involvement (rare)**
A 2023 review/case report on intraoral involvement notes that oral cavity involvement is uncommon and summarizes reported cases. (sharma2023intraoralnevusof pages 3-4)

### 3.2 Quality-of-life impact
The infant laser cohort motivates early treatment partly by psychosocial impact; the trial record similarly notes that marked facial hyperpigmentation can cause “psychosocial disturbances” prompting treatment seeking. (NCT04481178 chunk 1, zheng2024resultsandfollowup pages 1-2)

### 3.3 Suggested HPO terms (examples)
* Facial hyperpigmentation (HP:0001000)
* Blue-gray skin discoloration (phenotypic descriptor; may be mapped via “abnormality of skin pigmentation” HP:0000951)
* Scleral hyperpigmentation (map under “abnormality of the sclera” HP:0000592; pigmentation-specific child term may be needed)
* Ocular melanocytosis (conceptual; may map to “abnormality of the uvea” HP:0000610 plus pigmentation descriptors)
* Glaucoma (HP:0000501)

(These term suggestions are ontology mappings; specific HPO IDs for “ocular melanocytosis” may require ontology lookup beyond the retrieved texts.)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes / key molecular drivers (somatic mosaicism)
Evidence supports **postzygotic (somatic mosaic) activating mutations in GNAQ and GNA11** in extensive dermal melanocytosis/related phenotypes. In phakomatosis pigmentovascularis with extensive dermal melanocytosis, missense **GNA11/GNAQ mutations were detected in affected skin at very low levels and were undetectable in blood**, consistent with mosaicism. (thomas2016mosaicactivatingmutations pages 2-3)

A 2016 JID study provides functional support: mutant GNA11 variants activate MAPK-family pathways (p38/JNK/ERK depending on variant) and a mosaic zebrafish model recapitulated dermal melanocytosis. (thomas2016mosaicactivatingmutations pages 1-2, thomas2016mosaicactivatingmutations pages 3-5)

A 2024 review further explains that **codon 209 mutations impair GTP hydrolysis and lock Gα in the active GTP-bound state**, driving constitutive signaling through MAPK/ERK, Hippo/YAP-TAZ, and PI3K/AKT pathways, and notes postzygotic somatic mutations at residue 183 in GNAQ/GNA11 in relevant syndromic melanocytoses. (pilch2024gnaqgna11relatedbenignand pages 6-7)

### 4.2 Pathogenic variants and somatic vs germline
* Recurrent activating hotspots: **GNAQ p.R183Q** and **GNA11 p.R183C/p.R183S**, and **Q209** substitutions (e.g., Q209L/Q209P) are repeatedly implicated in mosaic melanocytosis and melanoma-related entities. (thomas2016mosaicactivatingmutations pages 3-5, pilch2024gnaqgna11relatedbenignand pages 6-7)
* Somatic origin: low mutant allele fractions in affected tissue and absence in blood support postzygotic mosaicism. (thomas2016mosaicactivatingmutations pages 3-5, thomas2016mosaicactivatingmutations pages 2-3)

### 4.3 Malignant transformation genetics / modifiers (tumor progression context)
Case-based literature links uveal melanoma in the context of nevus of Ota/ocular melanosis to canonical uveal melanoma drivers and progression genes.
* A 2019 report in a patient with congenital bilateral nevus of Ota and uveal melanoma identified **GNAQ R183Q** and a truncating mutation in mismatch repair gene **PMS1** in tumor sequencing. (toomey2019gnaqandpms1 pages 1-2)
* A melanoma-focused review for dermatologists reports: “Approximately **6% of lesions harbor mutations in GNAQ**.” (williams2021melanomainthe pages 1-2)
* A case-based excerpt reports co-occurrence of **BAP1 and GNAQ** mutations in intracranial melanoma associated with nevus of Ota and emphasizes BAP1 immunohistochemistry for prognostication in uveal melanoma. (konstantinov2018nevusofota pages 3-3)

### 4.4 Suggested GO biological process terms (examples)
* MAPK cascade (GO:0000165)
* ERK1/ERK2 cascade (GO:0070371)
* Neural crest cell migration (GO:0001755)
* Melanocyte differentiation (GO:0030318)

### 4.5 Suggested Cell Ontology (CL) terms (examples)
* Melanocyte (CL:0000148)
* Neural crest cell (CL:0000135)

---

## 5. Environmental Information

Environmental/lifestyle contributors are not established as causal in the retrieved primary evidence. However, clinical observations include pigment variability with hormonal states (adolescence/pregnancy) in the ODM review, and sun exposure as a factor associated with recurrence/worsening post-laser in infants. (abdolrahimzadeh2023anupdateon pages 1-3, zheng2024resultsandfollowup pages 1-2)

No infectious etiologies were identified. (abdolrahimzadeh2023anupdateon pages 1-3)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (current mechanistic model)
1. **Postzygotic activating mutation** in GNAQ/GNA11 occurs in a progenitor lineage (mosaicism), leading to a patchy tissue distribution. (thomas2016mosaicactivatingmutations pages 2-3)
2. Constitutively active Gαq/11 signaling leads to downstream activation of pathways including MAPK-family signaling; functional assays show mutant GNA11 activates MAPK components (p38/JNK/ERK) in cell lines, and in vivo models show increased melanocytes in epidermis/dermis. (thomas2016mosaicactivatingmutations pages 1-2, thomas2016mosaicactivatingmutations pages 3-5)
3. Accumulation of dermal (and ocular) melanocytes produces the clinical blue/gray pigmentation phenotype. (vishnevskiadai2021naevusofota pages 1-2, abdolrahimzadeh2023anupdateon pages 1-3)
4. In ocular tissues, melanocytosis can predispose to **glaucoma** and to development of **uveal melanoma**, necessitating ongoing ophthalmic surveillance. (abdolrahimzadeh2023anupdateon pages 1-3)

### 6.2 Immune involvement
No disease-specific immune mechanism evidence was retrieved. (abdolrahimzadeh2023anupdateon pages 1-3)

### 6.3 Suggested CL/GO/UBERON terms for mechanism mapping
* **UBERON**: skin of face (UBERON:0003920), sclera (UBERON:0000974), uvea (UBERON:0001769)
* **GO (cellular component)**: plasma membrane (GO:0005886) (for GPCR signaling nodes), cytosol (GO:0005829)

---

## 7. Anatomical Structures Affected

### 7.1 Organ and tissue level
* **Skin (facial/periocular)**: pigmentary macules/patches in trigeminal distributions. (williams2021melanomainthe pages 1-2, abdolrahimzadeh2023anupdateon pages 1-3)
* **Eye**: episclera/sclera and uvea; ocular involvement may include iris changes and other globe structures in clinical series. (vishnevskiadai2021naevusofota pages 1-2, abdolrahimzadeh2023anupdateon pages 1-3)

### 7.2 Localization and laterality
Typically unilateral; review reports “one eye in 90% of cases,” though bilateral cases occur. (abdolrahimzadeh2023anupdateon pages 1-3, vishnevskiadai2021naevusofota pages 1-1)

---

## 8. Temporal Development

### 8.1 Onset
Onset is commonly congenital or early life. The clinical trial record notes “About 50-60% of all cases have the age of onset at birth or within the first year of life, others appear before puberty.” (NCT04481178 chunk 1)

### 8.2 Progression / course
ODM does not tend to regress spontaneously; pigmentation may vary over time and with hormonal state. (abdolrahimzadeh2023anupdateon pages 1-3)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (key quantitative data)
* Asian incidence reported as **1–2 per 1000**. (abdolrahimzadeh2023anupdateon pages 1-3)
* Japanese dermatology clinic prevalence cited as **~0.4–0.8%**. (williams2021melanomainthe pages 1-2)
* Laterality: **~90%** unilateral ocular involvement. (abdolrahimzadeh2023anupdateon pages 1-3)
* Sex ratio: **~5:1** female predominance. (abdolrahimzadeh2023anupdateon pages 1-3, williams2021melanomainthe pages 1-2)

### 9.2 Inheritance pattern
The ODM review characterizes the condition as congenital and **non-hereditary**, consistent with somatic mosaicism models. (abdolrahimzadeh2023anupdateon pages 1-3)

---

## 10. Diagnostics

### 10.1 Clinical diagnosis
Diagnosis is primarily clinical based on characteristic distribution and ocular/skin pigmentation; ocular evaluation is emphasized due to glaucoma and melanoma risks. (abdolrahimzadeh2023anupdateon pages 1-3)

### 10.2 Ophthalmic evaluation and multimodal imaging (current practice trends)
The 2023 ophthalmology review provides a diagnostic/monitoring framework:
* Comprehensive ophthalmologic examination plus traditional imaging (ultrasonography; fluorescein/indocyanine green angiography), because fundus pigmentation may conceal subtle retinal/choroidal alterations. (abdolrahimzadeh2023anupdateon pages 1-3)
* Anterior segment OCT and ultrasound biomicroscopy for anterior segment/ciliary body evaluation when glaucoma or anterior uveal melanoma is suspected. (abdolrahimzadeh2023anupdateon pages 1-3)
* Fundus autofluorescence and RPE alterations for differentiating choroidal nevi vs melanoma; enhanced depth imaging OCT for high-resolution in vivo tumor/nevi assessment and early melanoma features (subretinal fluid, RPE abnormalities, choriocapillaris compression). (abdolrahimzadeh2023anupdateon pages 1-3)

Abstract support (direct quote): the review concludes that “Novel multimodal imaging techniques are significant in the diagnosis and management of the ophthalmic complications of ODM.” (abdolrahimzadeh2023anupdateon pages 1-3)

### 10.3 Histopathology
A 2023 bilateral case-series review states that nevus of Ota shows melanocytes in the dermis (and notes epidermal involvement in their phrasing). (kumari2023bilateralnevusof pages 4-5)

### 10.4 Genetic testing
Routine germline genetic testing is not established for typical isolated nevus of Ota in the retrieved texts; molecular findings mainly come from research sequencing of affected tissues/tumors (GNAQ/GNA11; BAP1 in associated melanomas). (toomey2019gnaqandpms1 pages 1-2, konstantinov2018nevusofota pages 3-3)

### 10.5 Differential diagnosis
The retrieved evidence emphasizes classification distinctions within dermal melanocytoses and diagnostic challenges; e.g., case literature distinguishes Ota nevus from acquired bilateral nevus of Ota-like macules (ABNOM) based on clinical and histopathologic patterns. (seemongaldass2025acaseof pages 5-6)

---

## 11. Outcome / Prognosis

### 11.1 Major complications and prognosis-relevant risks
* **Glaucoma** and **predisposition to uveal melanoma** are highlighted as the main ophthalmic complications in ODM. (abdolrahimzadeh2023anupdateon pages 1-3)
* The 2023 ophthalmology review states that “uveal melanoma in ODM carries twice the risk of metastasis compared to uveal melanoma in eyes without ODM,” underscoring prognostic importance of early detection. (abdolrahimzadeh2023anupdateon pages 1-3)
* In a 40-patient ocular series, **4 developed glaucoma** and **3 developed malignant transformation to choroidal melanoma**. (vishnevskiadai2021naevusofota pages 1-1)

### 11.2 Prognostic factors
The retrieved texts do not provide validated prognostic models specific to nevus of Ota itself; prognostication is more developed for uveal melanoma (e.g., BAP1 loss). (konstantinov2018nevusofota pages 3-3)

---

## 12. Treatment

### 12.1 Standard of care / current applications
**Laser therapy (selective photothermolysis) is the main real-world treatment for cosmetic pigment reduction**, especially Q-switched pigment lasers (ruby 694 nm, alexandrite 755 nm, Nd:YAG 1064 nm). (kumari2023bilateralnevusof pages 4-5, NCT04481178 chunk 1)

### 12.2 Recent developments (prioritizing 2023–2024)
**Early-life sequential Q-switched therapy (infant cohort; 2024):**
A large retrospective cohort of **102 infants (<1 year)** treated with sequential Q-switched 755 nm (initial sessions) and 1064 nm (from session 3 onward) at 6-month intervals reports high clearance and quantifies long-term recurrence. (zheng2024resultsandfollowup pages 1-2)

Direct abstract quote: “Success rates reached **88.7% after four sessions and 99.3% after seven sessions**.” (zheng2024resultsandfollowup pages 1-2)

Recurrence: among 47 infants with follow-up, **14 recurred (29.8%)**, and additional 2–3 sessions typically controlled recurrence. (zheng2024resultsandfollowup pages 1-2)

A table image from this study (efficacy by subtype and factors such as location/anesthesia) is available and supports the reported outcome stratification. (zheng2024resultsandfollowup media 94a4abe5, zheng2024resultsandfollowup media 9a87c0a6)

### 12.3 Adverse events and tolerability (quantitative)
* In the 2024 infant cohort abstract, “No instances of serious adverse reactions, except for pain, were reported.” (zheng2024resultsandfollowup pages 1-2)
* A Thai retrospective protocol (NCT04481178; ClinicalTrials.gov) summarizes reported complication rates from prior Q-switched laser literature: **hypopigmentation 15.3%, hyperpigmentation 2.9%, texture changes 2.9%, scarring 1.9%**, and cites a “success rate of 95% after 6-8 sessions.” (NCT04481178 chunk 1)

### 12.4 Treatment strategy / monitoring
The ophthalmology review emphasizes that monitoring for glaucoma and melanoma is central and that multimodal imaging is increasingly used to standardize complication detection and follow-up. (abdolrahimzadeh2023anupdateon pages 1-3)

### 12.5 MAXO term suggestions (examples)
* Laser therapy (MAXO:0000058, “laser therapy”)
* Ophthalmologic monitoring/surveillance (MAXO term may require lookup; concept: “medical monitoring”)

---

## 13. Prevention

Primary prevention of nevus of Ota is not described (developmental mosaic condition). Secondary/tertiary prevention focuses on preventing vision loss and melanoma morbidity through **lifelong ophthalmic surveillance** and early detection using multimodal imaging. (abdolrahimzadeh2023anupdateon pages 1-3)

---

## 14. Other Species / Natural Disease

A naturally occurring analogue has been described in dogs (oculodermal melanocytosis/nevus of Ota), with similar distribution and ocular involvement on histopathology, indicating cross-species relevance of neural crest–derived melanocyte disorders. (abdolrahimzadeh2023anupdateon pages 1-3)

(Note: the main veterinary primary literature was retrieved but not deeply evidence-extracted in this run; this section is therefore limited.)

---

## 15. Model Organisms

A mechanistically informative model is a **mosaic transgenic zebrafish** expressing mutant GNA11 (e.g., GNA11R183C) in the melanocyte lineage, which produced dermal melanocytosis, supporting causal roles for activating Gαq/11 signaling in melanocyte accumulation. (thomas2016mosaicactivatingmutations pages 1-2, thomas2016mosaicactivatingmutations pages 3-5)

---

## Expert opinions / authoritative synthesis (from reviews)
* The 2023 ophthalmology review highlights an expert-practice shift toward standardized use of multimodal imaging for ODM complications, stating that OCT and fundus autofluorescence have “adjunctive value” for early melanoma detection and differential diagnosis. (abdolrahimzadeh2023anupdateon pages 1-3)
* The dermatology melanoma review stresses that while nevus of Ota is often a cosmetic concern, malignant transformation risk mandates clinician awareness and appropriate referrals. (williams2021melanomainthe pages 1-2)

---

## Key evidence gaps in this run
* ICD-10/ICD-11, OMIM, Orphanet, and MONDO identifiers were not available in the retrieved full texts/tools state; they require direct lookup in those external databases. (NCT04481178 chunk 1)
* High-quality, population-based incidence/prevalence estimates outside East Asian cohorts were not retrieved here.
* Picosecond-laser comparative effectiveness literature (2023–2024) was identified in search but some key papers were unobtainable in the current corpus, limiting systematic comparison versus Q-switched modalities.

---

## References (URLs with publication dates where available)
* Abdolrahimzadeh S, et al. *Graefe’s Archive for Clinical and Experimental Ophthalmology*. Published online 19 Jul 2022; in-issue 2023. https://doi.org/10.1007/s00417-022-05743-1 (abdolrahimzadeh2023anupdateon pages 1-3)
* Zheng H, et al. *Clinical, Cosmetic and Investigational Dermatology*. Published 3 Feb 2024. https://doi.org/10.2147/CCID.S444410 (zheng2024resultsandfollowup pages 1-2)
* Williams NM, et al. *International Journal of Dermatology*. 2021 (issue date Aug 2021; copyright line 2020). https://doi.org/10.1111/ijd.15135 (williams2021melanomainthe pages 1-2)
* Thomas AC, et al. *Journal of Investigative Dermatology*. Apr 2016. https://doi.org/10.1016/j.jid.2015.11.027 (thomas2016mosaicactivatingmutations pages 1-2)
* ClinicalTrials.gov. NCT04481178. First posted 22 Jul 2020. https://clinicaltrials.gov/study/NCT04481178 (NCT04481178 chunk 1)


References

1. (abdolrahimzadeh2023anupdateon pages 1-3): Solmaz Abdolrahimzadeh, Damiano Maria Pugi, Priscilla Manni, Clemente Maria Iodice, Federico Di Tizio, Flavia Persechino, and Gianluca Scuderi. An update on ophthalmological perspectives in oculodermal melanocytosis (nevus of ota). Graefe's Archive for Clinical and Experimental Ophthalmology, 261:291-301, Jul 2023. URL: https://doi.org/10.1007/s00417-022-05743-1, doi:10.1007/s00417-022-05743-1. This article has 19 citations.

2. (williams2021melanomainthe pages 1-2): Natalie M. Williams, Pooja Gurnani, Angelina Labib, Ronaldo Nuesi, and Keyvan Nouri. Melanoma in the setting of nevus of ota: a review for dermatologists. International Journal of Dermatology, 60:523-532, Aug 2021. URL: https://doi.org/10.1111/ijd.15135, doi:10.1111/ijd.15135. This article has 28 citations and is from a peer-reviewed journal.

3. (vishnevskiadai2021naevusofota pages 1-2): Vicktoria Vishnevskia-Dai, Iris Moroz, Tal Davidy, Keren Zloto, Yael Birger, Ido Didi Fabian, Guy Ben Simon, Ayelet Priel, and Ofira Zloto. Naevus of ota: clinical characteristics and proposal for a new ocular classification and grading system. British Journal of Ophthalmology, 105:42-47, Mar 2021. URL: https://doi.org/10.1136/bjophthalmol-2019-313984, doi:10.1136/bjophthalmol-2019-313984. This article has 11 citations and is from a highest quality peer-reviewed journal.

4. (zheng2024resultsandfollowup pages 1-2): Han Zheng, Ai-E Xu, Gang Qiao, Xiao-Yu Sun, Jia Deng, and Yong Zhang. Results and follow-up of a sequential q-switched laser therapy for nevus of ota in infants. Clinical, Cosmetic and Investigational Dermatology, 17:339-347, Feb 2024. URL: https://doi.org/10.2147/ccid.s444410, doi:10.2147/ccid.s444410. This article has 2 citations and is from a peer-reviewed journal.

5. (vishnevskiadai2021naevusofota pages 1-1): Vicktoria Vishnevskia-Dai, Iris Moroz, Tal Davidy, Keren Zloto, Yael Birger, Ido Didi Fabian, Guy Ben Simon, Ayelet Priel, and Ofira Zloto. Naevus of ota: clinical characteristics and proposal for a new ocular classification and grading system. British Journal of Ophthalmology, 105:42-47, Mar 2021. URL: https://doi.org/10.1136/bjophthalmol-2019-313984, doi:10.1136/bjophthalmol-2019-313984. This article has 11 citations and is from a highest quality peer-reviewed journal.

6. (zheng2024resultsandfollowup pages 4-6): Han Zheng, Ai-E Xu, Gang Qiao, Xiao-Yu Sun, Jia Deng, and Yong Zhang. Results and follow-up of a sequential q-switched laser therapy for nevus of ota in infants. Clinical, Cosmetic and Investigational Dermatology, 17:339-347, Feb 2024. URL: https://doi.org/10.2147/ccid.s444410, doi:10.2147/ccid.s444410. This article has 2 citations and is from a peer-reviewed journal.

7. (NCT04481178 chunk 1): Woraphong Manuskiatti, M.D.. A Retrospective Study on Laser Treatment of Nevus of Ota in Thai Patients. Mahidol University. 2020. ClinicalTrials.gov Identifier: NCT04481178

8. (toomey2019gnaqandpms1 pages 1-2): Christopher B. Toomey, Kyle Fraser, John A. Thorson, Michael H. Goldbaum, and Jonathan H. Lin. Gnaq and pms1 mutations associated with uveal melanoma, ocular surface melanosis, and nevus of ota. Ocular Oncology and Pathology, 5:267-272, Jan 2019. URL: https://doi.org/10.1159/000495508, doi:10.1159/000495508. This article has 11 citations and is from a peer-reviewed journal.

9. (sharma2023intraoralnevusof pages 3-4): DR ARUN DEV SHARMA, DR AJAY PRATAP SINGH PARIHAR, DR PRASHANTHI REDDY, DR NIDHI YADAV, and DR RASHI MANDLIK. Intraoral nevus of ota : a case report and review. UNIVERSITY JOURNAL OF DENTAL SCIENCES, Jul 2023. URL: https://doi.org/10.21276/ujds.2023.9.3.19, doi:10.21276/ujds.2023.9.3.19. This article has 1 citations.

10. (thomas2016mosaicactivatingmutations pages 2-3): Anna C. Thomas, Zhiqiang Zeng, Jean-Baptiste Rivière, Ryan O’Shaughnessy, Lara Al-Olabi, Judith St.-Onge, David J. Atherton, Hélène Aubert, Lorea Bagazgoitia, Sébastien Barbarot, Emmanuelle Bourrat, Christine Chiaverini, W. Kling Chong, Yannis Duffourd, Mary Glover, Leopold Groesser, Smail Hadj-Rabia, Henning Hamm, Rudolf Happle, Imran Mushtaq, Jean-Philippe Lacour, Regula Waelchli, Marion Wobser, Pierre Vabres, E. Elizabeth Patton, and Veronica A. Kinsler. Mosaic activating mutations in gna11 and gnaq are associated with phakomatosis pigmentovascularis and extensive dermal melanocytosis. The Journal of Investigative Dermatology, 136:770-778, Apr 2016. URL: https://doi.org/10.1016/j.jid.2015.11.027, doi:10.1016/j.jid.2015.11.027. This article has 234 citations.

11. (thomas2016mosaicactivatingmutations pages 1-2): Anna C. Thomas, Zhiqiang Zeng, Jean-Baptiste Rivière, Ryan O’Shaughnessy, Lara Al-Olabi, Judith St.-Onge, David J. Atherton, Hélène Aubert, Lorea Bagazgoitia, Sébastien Barbarot, Emmanuelle Bourrat, Christine Chiaverini, W. Kling Chong, Yannis Duffourd, Mary Glover, Leopold Groesser, Smail Hadj-Rabia, Henning Hamm, Rudolf Happle, Imran Mushtaq, Jean-Philippe Lacour, Regula Waelchli, Marion Wobser, Pierre Vabres, E. Elizabeth Patton, and Veronica A. Kinsler. Mosaic activating mutations in gna11 and gnaq are associated with phakomatosis pigmentovascularis and extensive dermal melanocytosis. The Journal of Investigative Dermatology, 136:770-778, Apr 2016. URL: https://doi.org/10.1016/j.jid.2015.11.027, doi:10.1016/j.jid.2015.11.027. This article has 234 citations.

12. (thomas2016mosaicactivatingmutations pages 3-5): Anna C. Thomas, Zhiqiang Zeng, Jean-Baptiste Rivière, Ryan O’Shaughnessy, Lara Al-Olabi, Judith St.-Onge, David J. Atherton, Hélène Aubert, Lorea Bagazgoitia, Sébastien Barbarot, Emmanuelle Bourrat, Christine Chiaverini, W. Kling Chong, Yannis Duffourd, Mary Glover, Leopold Groesser, Smail Hadj-Rabia, Henning Hamm, Rudolf Happle, Imran Mushtaq, Jean-Philippe Lacour, Regula Waelchli, Marion Wobser, Pierre Vabres, E. Elizabeth Patton, and Veronica A. Kinsler. Mosaic activating mutations in gna11 and gnaq are associated with phakomatosis pigmentovascularis and extensive dermal melanocytosis. The Journal of Investigative Dermatology, 136:770-778, Apr 2016. URL: https://doi.org/10.1016/j.jid.2015.11.027, doi:10.1016/j.jid.2015.11.027. This article has 234 citations.

13. (pilch2024gnaqgna11relatedbenignand pages 6-7): Justyna Pilch, Jakub Mizera, Maciej Tota, and Piotr Donizy. Gnaq/gna11-related benign and malignant entities—a common histoembriologic origin or a tissue-dependent coincidence. Cancers, 16:3672, Oct 2024. URL: https://doi.org/10.3390/cancers16213672, doi:10.3390/cancers16213672. This article has 6 citations.

14. (konstantinov2018nevusofota pages 3-3): NK Konstantinov, TM Berry, HR Elwood, and BJ Zlotoff. Nevus of ota associated with a primary uveal melanoma and intracranial melanoma metastasis. Unknown journal, 2018.

15. (kumari2023bilateralnevusof pages 4-5): Pinki Kumari, Vartika, Pallavi UK, and Rajesh Sinha. Bilateral nevus of ota: a case series and literature review. Asian Journal of Medical Sciences, 14:326-331, Nov 2023. URL: https://doi.org/10.3126/ajms.v14i11.56108, doi:10.3126/ajms.v14i11.56108. This article has 0 citations.

16. (seemongaldass2025acaseof pages 5-6): Rajiv V Seemongal-Dass, Robin R Seemongal-Dass, Alyssa P Singh, and Diego A Conocchiari. A case of nevus of ota in trinidad and tobago. Cureus, Jan 2025. URL: https://doi.org/10.7759/cureus.78311, doi:10.7759/cureus.78311. This article has 1 citations.

17. (zheng2024resultsandfollowup media 94a4abe5): Han Zheng, Ai-E Xu, Gang Qiao, Xiao-Yu Sun, Jia Deng, and Yong Zhang. Results and follow-up of a sequential q-switched laser therapy for nevus of ota in infants. Clinical, Cosmetic and Investigational Dermatology, 17:339-347, Feb 2024. URL: https://doi.org/10.2147/ccid.s444410, doi:10.2147/ccid.s444410. This article has 2 citations and is from a peer-reviewed journal.

18. (zheng2024resultsandfollowup media 9a87c0a6): Han Zheng, Ai-E Xu, Gang Qiao, Xiao-Yu Sun, Jia Deng, and Yong Zhang. Results and follow-up of a sequential q-switched laser therapy for nevus of ota in infants. Clinical, Cosmetic and Investigational Dermatology, 17:339-347, Feb 2024. URL: https://doi.org/10.2147/ccid.s444410, doi:10.2147/ccid.s444410. This article has 2 citations and is from a peer-reviewed journal.
---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T10:46:01.891887'
end_time: '2026-05-08T10:54:27.497554'
duration_seconds: 505.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CADASIL Type 1
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** CADASIL Type 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CADASIL Type 1** covering all of the
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
- **Disease Name:** CADASIL Type 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CADASIL Type 1** covering all of the
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


# CADASIL Type 1 (NOTCH3-related) — Disease Characteristics Research Report

## 1. Disease information

### 1.1 Concise overview
Cerebral autosomal dominant arteriopathy with subcortical infarcts and leukoencephalopathy (CADASIL) is an adult-onset, autosomal dominant hereditary cerebral small-vessel disease that typically presents in mid-adulthood with ischemic strokes/transient ischemic attacks, migraine (often with aura), mood disturbance, and progressive cognitive impairment leading to vascular dementia. (cerfontaine2024associationofnotch3 pages 1-2, papakonstantinou2019notch3andcadasil pages 1-3, bersano2017cadasiltreatmentand pages 1-3)

A current mechanistic consensus is that CADASIL is “considered to be caused by accumulation of the mutant NOTCH3 extracellular domain (N3ECD)” with possible contribution from impaired Notch signaling; however, “the process leading to N3ECD accumulation and its association with canonical NOTCH3 signaling remain unknown.” (Mizuta et al., 2024-01-18) (mizuta2024progresstoclarify pages 1-2)

### 1.2 Key identifiers and synonyms (from retrieved evidence)
- **Preferred name:** CADASIL (Cerebral Autosomal Dominant Arteriopathy with Subcortical Infarcts and Leukoencephalopathy). (bersano2017cadasiltreatmentand pages 1-3)
- **OMIM:** **125310** (explicitly cited as “CADASIL (OMIM 125310)” in multiple sources). (hu2021notch3variantsand pages 1-2, bersano2017cadasiltreatmentand pages 1-3)
- **Causal gene:** **NOTCH3** (chr19; NOTCH3 receptor). (hu2021notch3variantsand pages 1-2, bersano2017cadasiltreatmentand pages 1-3)

**Not located in the retrieved sources for this run:** MONDO ID, Orphanet ORPHA number, ICD-10/ICD-11 codes, MeSH ID. These identifiers should be added by consulting the corresponding terminologies (e.g., MONDO/Orphanet/WHO ICD/MeSH) because they are not directly available in the evidence retrieved here.

### 1.3 Source types for disease definition
- Aggregated, disease-level consensus in peer-reviewed reviews and cohorts. (bersano2017cadasiltreatmentand pages 1-3, mizuta2024progresstoclarify pages 1-2)
- Large-scale EMR/network analyses (coded diagnosis; potential for misclassification). (pan2023lifelongcerebrovasculardisease pages 1-2)

## 2. Etiology

### 2.1 Disease causal factors
CADASIL is caused primarily by pathogenic **NOTCH3** variants. The archetypal CADASIL-causing variants are **heterozygous missense mutations** in the NOTCH3 extracellular epidermal growth factor-like repeat (EGFr) region that **alter the number of cysteines** (creating an odd number), leading to misfolding/aggregation of the NOTCH3 extracellular domain and characteristic vessel-wall pathology. (hu2021notch3variantsand pages 1-2, mizuta2024progresstoclarify pages 1-2)

Direct abstract quote (mechanistic framing): “CADASIL … is adult-onset and considered to be caused by accumulation of the mutant NOTCH3 extracellular domain (N3ECD) and, possibly, by an impairment in Notch signaling.” (Mizuta et al., 2024-01-18) (mizuta2024progresstoclarify pages 1-2)

### 2.2 Risk factors (genetic and non-genetic modifiers)
**Genetic (variant-position effects):** NOTCH3 variant position in EGFr domains strongly influences phenotype severity; variants in **EGFr 1–6** are repeatedly associated with more severe disease than **EGFr 7–34**, beyond effects of age/sex/vascular risk factors. (dupe2023phenotypicvariabilityin pages 1-2, kaisaridi2025determiningclinicaldisease pages 1-5, cao2024phenotypesassociatedwith pages 13-14)

**Non-genetic modifiers:** Large cohort analyses identify **age**, **male sex**, and vascular risk factors (notably **hypertension**, hypercholesterolemia; also smoking in progression modeling) as contributors to clinical severity/progression, in addition to NOTCH3 variant position. (dupe2023phenotypicvariabilityin pages 1-2, kaisaridi2025determiningclinicaldisease pages 1-5)

**Hemorrhage-related treatment/risk factor signal:** In a UK register/systematic review study, anticoagulation was associated with higher intracerebral hemorrhage (ICH) risk in CADASIL (see §11 and §12). (sukhonpanich2024prevalenceclinicalcharacteristics pages 1-2)

### 2.3 Protective factors and gene–environment interaction
No protective factors or explicit gene–environment interaction models were identified in the retrieved evidence.

## 3. Phenotypes (with suggested HPO terms)

### 3.1 Core phenotype spectrum
Across large cohort and registry/EMR studies, CADASIL commonly includes:
- **Migraine with aura** (often early feature). Suggested HPO: **HP:0002076 (Migraine)**; aura can be mapped to **HP:0012378 (Aura)** (phenotype label). (cerfontaine2024associationofnotch3 pages 1-2, bersano2017cadasiltreatmentand pages 1-3)
- **Ischemic stroke/TIA**, typically lacunar subtype. Suggested HPO: **HP:0001297 (Stroke)**; **HP:0002326 (Transient ischemic attack)**. (cerfontaine2024associationofnotch3 pages 1-2, bersano2017cadasiltreatmentand pages 1-3)
- **Cognitive impairment/executive dysfunction → vascular dementia**. Suggested HPO: **HP:0100543 (Cognitive impairment)**; **HP:0000726 (Dementia)**. (cerfontaine2024associationofnotch3 pages 1-2, bersano2017cadasiltreatmentand pages 1-3)
- **Psychiatric/mood disturbance** (depression/apathy). Suggested HPO: **HP:0000716 (Depression)**; **HP:0000741 (Apathy)**. (cerfontaine2024associationofnotch3 pages 1-2, bersano2017cadasiltreatmentand pages 1-3)
- **Seizures** (minority). Suggested HPO: **HP:0001250 (Seizures)**. (bersano2017cadasiltreatmentand pages 1-3)

### 3.2 Quantitative phenotype frequencies from recent cohorts/case series
- **Brazilian genetically confirmed series (n=26):** ischemic stroke first symptom **19/26**; cognitive impairment **17/26**; dementia **6/26**; psychiatric manifestations **16/26**; recurrent migraine **8/26**, aura in **6/8 (75%)**. (Nogueira et al., online 2023-05-08) (nogueira2023clinicalandepidemiological pages 1-2)
- **TriNetX EMR network analysis (n=914):** **596/914 (65.2%)** had documented cerebrovascular events; among CADASIL-stroke patients, **89.4%** had ischemic stroke; TIAs co-existed in **27.7%**; hemorrhagic strokes **6.2%**; first stroke ≤65 years in **71%**. (Pan et al., 2023-07-14) (pan2023lifelongcerebrovasculardisease pages 1-2)

### 3.3 MRI phenotype (selected frequencies)
- **Brazilian series (n=26):** temporal lobe WMH **20/22?** reported as **20 patients (91%)**; external capsule WMH **15 (68%)**; lacunar infarcts **18 (82%)**; microbleeds **9 (41%)**; larger hemorrhages **2 (9%)**. (nogueira2023clinicalandepidemiological pages 1-2)
- **Chinese cohort excerpt (probands; MRI):** external capsule involvement **77.8%** and anterior temporal lobe involvement **37.0%** in that cohort; skin biopsy GOM detected in **11/16** tested. (hu2021notch3variantsand pages 1-2)

## 4. Genetic/molecular information

### 4.1 Causal gene
- **NOTCH3** encodes a ~2,321 amino-acid transmembrane receptor with **34 EGF-like repeats** in the extracellular domain (EGFr 1–34). (hu2021notch3variantsand pages 1-2)

### 4.2 Pathogenic variants and variant classes
- Most causative variants are **cysteine-altering missense variants** located in the NOTCH3 **EGFr domain**, producing an odd number of cysteines. (hu2021notch3variantsand pages 1-2, mizuta2024progresstoclarify pages 1-2)
- Pathology is linked to vascular deposition/aggregation of NOTCH3 extracellular domain and extracellular matrix proteins (see §6). (papakonstantinou2019notch3andcadasil pages 1-3, kaisaridi2025determiningclinicaldisease pages 1-5)

**Examples of common variants (systematic review):** A 1996–2023 systematic review reported the six most common missense mutations globally as **p.R75P, p.R133C, p.R141C, p.R169C, p.R182C, and p.R544C**. (Boston et al., 2024-06-03) (boston2024mostcommonnotch3 pages 1-2)

### 4.3 Genotype–phenotype correlations
- **EGFr position** is a major determinant: variants in EGFr 1–6 generally confer higher severity than variants in EGFr 7–34; severity differences appear mediated by differences in ischemic brain lesion accumulation. (dupe2023phenotypicvariabilityin pages 1-2, kaisaridi2025determiningclinicaldisease pages 1-5, cao2024phenotypesassociatedwith pages 13-14)
- **Risk categorization for NOTCH3-associated SVD:** NOTCH3 variants have been categorized as high-, moderate-, or low-risk for early-onset severe small-vessel disease, and this categorization predicts short-term progression in a 2-year prospective CADASIL study (see §8 and artifact table). (cerfontaine2024associationofnotch3 pages 1-2)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No robust modifier genes, epigenetic mechanisms, or chromosomal abnormalities were identified in the retrieved evidence for this run.

## 5. Environmental information
No CADASIL-specific environmental toxins or infectious triggers were identified in the retrieved evidence. Vascular risk factors (hypertension, dyslipidemia, smoking) are clinically relevant modifiers rather than primary environmental causes. (kaisaridi2025determiningclinicaldisease pages 1-5)

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (current understanding)
1) **Germline NOTCH3 EGFr cysteine-altering variant** → 2) **misfolding and accumulation/aggregation of NOTCH3 extracellular domain (N3ECD)** in small-vessel walls → 3) **granular osmiophilic material (GOM)** deposition and co-aggregation with extracellular matrix/matrisome proteins → 4) progressive small-vessel dysfunction (vascular wall damage, impaired vascular reactivity/perfusion) → 5) chronic ischemic injury and MRI small-vessel disease markers (WMH, lacunes, microbleeds, atrophy) → 6) clinical manifestations (migraine, lacunar strokes/TIA, cognitive decline/dementia, mood symptoms). (papakonstantinou2019notch3andcadasil pages 1-3, kaisaridi2025determiningclinicaldisease pages 1-5, mizuta2024progresstoclarify pages 1-2)

### 6.2 Cellular/tissue context
CADASIL pathology is centered on **vascular smooth muscle cells** and **pericytes** of small arteries/arterioles and capillaries, where NOTCH3 is expressed and where N3ECD deposits and GOM are detected. (papakonstantinou2019notch3andcadasil pages 1-3)

Suggested Cell Ontology (CL) terms (label suggestions):
- Vascular smooth muscle cell (e.g., “vascular associated smooth muscle cell”).
- Pericyte.

### 6.3 Molecular pathways and processes (GO suggestions)
Evidence in this run most strongly supports processes related to:
- **Notch signaling** (canonical pathway involvement uncertain in CADASIL relative to other NOTCH disorders). (mizuta2024progresstoclarify pages 1-2)
- **Protein aggregation / extracellular deposition**, extracellular matrix interactions, and vascular wall remodeling. (kaisaridi2025determiningclinicaldisease pages 1-5)

GO term suggestions (label-level): Notch signaling pathway; extracellular matrix organization; protein aggregation; vascular smooth muscle cell differentiation/maintenance; response to hypoxia/ischemia.

### 6.4 Recent mechanistic emphasis (2024)
Mizuta et al. (2024) explicitly highlight that, despite extensive downstream studies, “the process leading to N3ECD accumulation and its association with canonical NOTCH3 signaling remain unknown,” underscoring an upstream mechanistic gap that is increasingly relevant for designing disease-modifying therapies. (mizuta2024progresstoclarify pages 1-2)

## 7. Anatomical structures affected

### 7.1 Organ/system level
- Primary: **Brain** (cerebral small vessels; subcortical ischemic injury; vascular cognitive impairment/dementia). (cerfontaine2024associationofnotch3 pages 1-2, bersano2017cadasiltreatmentand pages 1-3)

Suggested UBERON terms (label suggestions): brain; cerebral cortex; white matter; basal ganglia; thalamus.

### 7.2 Tissue/cell level
- Small arteries/arterioles and capillaries (microvasculature), with vascular smooth muscle cells and pericytes as key cellular sites of pathology. (papakonstantinou2019notch3andcadasil pages 1-3)

### 7.3 Subcellular level
- Extracellular deposition/aggregation of NOTCH3 ectodomain (extracellular compartment/ECM). (kaisaridi2025determiningclinicaldisease pages 1-5)

## 8. Temporal development
CADASIL is **adult-onset** with early manifestations such as migraine with aura potentially in young adulthood, while disabling motor/cognitive manifestations often occur later (often after age 50 in clinical descriptions). (bersano2017cadasiltreatmentand pages 1-3, akrich2024geneticdiagnosisof pages 1-2)

Disease progression is heterogeneous; modeling of longitudinal clinical scores identified an early-onset rapidly progressing subgroup vs a later-onset slower subgroup, with variant position (EGFr 1–6), male sex, education, hypertension, and smoking associated with more aggressive progression. (kaisaridi2025determiningclinicaldisease pages 1-5)

## 9. Inheritance and population

### 9.1 Inheritance
Autosomal dominant inheritance is consistently reported for classical CADASIL due to pathogenic NOTCH3 variants. (akrich2024geneticdiagnosisof pages 1-2)

### 9.2 Epidemiology and prevalence
- Traditional European prevalence estimates: **~2–5 per 100,000**, cited in multiple sources including cohort/review contexts. (cerfontaine2024associationofnotch3 pages 1-2, mizuta2024progresstoclarify pages 1-2)
- Population genomics context: NOTCH3 variants may be far more common in the general population than clinically recognized CADASIL prevalence; one 2024 prospective study notes NOTCH3 variants in at least **~1:300** individuals while CADASIL minimal prevalence is **2–5:100,000**. (cerfontaine2024associationofnotch3 pages 1-2)

### 9.3 Sex differences (real-world EMR data)
In TriNetX EMR data, males had higher associated risk of stroke onset (OR **1.37**) and higher mortality risk (OR **2.72**) compared with females, after adjustment. (pan2023lifelongcerebrovasculardisease pages 1-2)

## 10. Diagnostics

### 10.1 Genetic testing (current implementation)
Genetic testing is repeatedly described as the diagnostic gold standard for CADASIL in the retrieved evidence. (hu2021notch3variantsand pages 1-2, bersano2017cadasiltreatmentand pages 1-3)

A real-world diagnostic laboratory evaluation (680 referred samples; 1997 onward) showed a **14.7%** mutation detection rate overall, and higher yield using a targeted **NGS panel (15.8%)** compared with limited Sanger strategies (10.8%), supporting broader sequencing approaches. (Dunn et al., 2020-01; Human Genomics) (dunn2020investigatingdiagnosticsequencing pages 1-2)

### 10.2 Skin biopsy / pathology
Presence of **granular osmiophilic material (GOM)** in skin vessels is a characteristic pathological hallmark and is used diagnostically in some workflows, particularly when genetic results are uncertain; in one cohort excerpt, skin biopsy found GOM in **11/16** tested. (papakonstantinou2019notch3andcadasil pages 1-3, hu2021notch3variantsand pages 1-2)

### 10.3 MRI and imaging markers
Characteristic MRI patterns include extensive white matter hyperintensities (WMH), lacunes, microbleeds, and brain atrophy, with involvement of anterior temporal pole and external capsule often considered suggestive. (bersano2017cadasiltreatmentand pages 1-3, nogueira2023clinicalandepidemiological pages 1-2)

A 2024 prospective study demonstrates trial-sensitive MRI outcomes over 2 years including diffusion MRI (MSMD), WMH volume, lacune volume, and brain parenchymal fraction; variant risk category stratifies progression rates. (cerfontaine2024associationofnotch3 pages 1-2)

**Image evidence:** Table 2 from Dupé et al. provides a structured summary of clinical and imaging features stratified by NOTCH3 EGFr 1–6 vs 7–34 (including WMH, lacunes, microbleeds, and brain parenchymal fraction), supporting genotype-informed interpretation of MRI patterns. (dupe2023phenotypicvariabilityin media cdee29b5)

## 11. Outcome / prognosis
CADASIL is progressive and leads to cumulative cerebrovascular injury and vascular cognitive impairment/dementia. (cerfontaine2024associationofnotch3 pages 1-2, bersano2017cadasiltreatmentand pages 1-3)

Recent quantitative prognosis-related signals include:
- Two-year prospective worsening in disability, executive function, and multiple MRI measures (MSMD, WMH volume, lacune volume, brain parenchymal fraction), with faster progression in high-risk NOTCH3 variant categories. (cerfontaine2024associationofnotch3 pages 1-2)
- ICH occurs in about **~2% of symptomatic cases** in a large UK register estimate, with mean onset ~56.6 years and important associations with anticoagulation exposure. (sukhonpanich2024prevalenceclinicalcharacteristics pages 1-2)

## 12. Treatment

### 12.1 Current standard of care (symptomatic/risk management)
No disease-modifying therapy is established in the retrieved evidence; management is largely supportive and focused on symptom control and vascular risk factor management. A dedicated treatment review emphasizes that “no proven disease-modifying therapies exist” and management is empiric. (bersano2017cadasiltreatmentand pages 1-3)

### 12.2 Antithrombotic considerations (evidence relevant to practice)
ICH-focused evidence indicates anticoagulation is associated with increased ICH risk in CADASIL (20.0% vs 1.9% in the UK register comparison), whereas antiplatelet agents were not associated with increased risk in that study. This is relevant to clinical decision-making when considering anticoagulation indications in CADASIL patients. (Sukhonpanich & Markus, published online 2024-01-13) (sukhonpanich2024prevalenceclinicalcharacteristics pages 1-2)

### 12.3 Clinical trials and observational research (real-world implementation)
Although interventional disease-modifying trials were not identified in the retrieved clinicaltrials.gov set for this run, multiple **observational/natural history** efforts are active and support biomarker development and future trial readiness:
- **NCT05677880** (first posted 2023-01-10; recruiting): longitudinal observational study (“Unraveling the Early Phases…”) enrolling individuals with CADASIL family history and known NOTCH3 status; includes neurocognitive assessment, MRI, and biofluids including neurofilament light (NfL). URL: https://clinicaltrials.gov/study/NCT05677880 (NCT05677880 chunk 1)
- **NCT05072483** (first posted 2021-10-11; recruiting): NIH natural history study with deep phenotyping; may include skin biopsy and lumbar puncture; long follow-up. URL: https://clinicaltrials.gov/study/NCT05072483 (NCT05072483 chunk 1)

Suggested MAXO terms (label suggestions): genetic testing; magnetic resonance imaging; antiplatelet therapy; anticoagulation avoidance/risk assessment; rehabilitation therapy; cognitive assessment.

## 13. Prevention
No primary prevention strategies specific to CADASIL onset were identified in the retrieved evidence. Secondary/tertiary prevention in practice focuses on aggressive management of vascular risk factors and careful consideration of anticoagulation given ICH risk evidence. (kaisaridi2025determiningclinicaldisease pages 1-5, sukhonpanich2024prevalenceclinicalcharacteristics pages 1-2)

## 14. Other species / natural disease
No naturally occurring CADASIL-equivalent disease in non-human species was identified in the retrieved evidence.

## 15. Model organisms and experimental models
A 2024 mechanistic review notes that Notch signaling is conserved across species and that some Drosophila Notch lines harbor cysteine-altering mutations corresponding to CADASIL-causing mutations, but also states that “animal models of CADASIL other than rodent models have not been established,” potentially because Notch signaling is not impaired by most CADASIL-causing mutations. (mizuta2024progresstoclarify pages 1-2)

## Recent quantitative findings (2023–2024)

| Study (first author, year) | Design/Population | Key quantitative results (include exact numbers) | Interpretation/implication |
|---|---|---|---|
| Cerfontaine, 2024 | Prospective 2-year single-center follow-up in genetically confirmed CADASIL; **162 patients** total: high-risk (HR) **n=90**, moderate-risk (MR) **n=67**, low-risk (LR) **n=5** | Over 2 years, whole cohort showed progression in **MSMD β=0.20 (95% CI 0.17–0.23; p=7.0×10⁻²⁴)**, **normalized lacune volume β=0.13 (0.080–0.19; p=2.1×10⁻⁶)**, **normalized WMH volume β=0.092 (0.075–0.11; p=8.8×10⁻²⁰)**, **brain parenchymal fraction β=−0.22 (−0.26 to −0.19; p=3.2×10⁻²²)**, plus increased disability (**p=0.002**) and executive decline (**β=−0.15; 95% CI −0.30 to −3.4×10⁻⁵; p=0.05**). HR variants had higher 2-year incident stroke risk than MR variants: **hazard ratio 4.3 (95% CI 1.4–13.5; p=0.011)**; also greater increase in **MSMD β=0.074 (0.013–0.14; p=0.017)** and **lacune volume β=0.14 (0.034–0.24; p=0.0089)**. Significant MSMD progression was detectable even in **young n=17** and **premanifest n=24** subgroups. (cerfontaine2024associationofnotch3 pages 1-2) | Strong evidence that NOTCH3 risk category predicts short-term clinical and radiologic worsening; supports **MSMD** as a trial-sensitive biomarker, including in premanifest disease. |
| Dupé, 2023 | Large phenotyping study of **446 CADASIL patients** assessing effects of NOTCH3 EGFr mutation location plus age, sex, and vascular risk factors | The study confirmed that mutation location in **EGFr 1–6 vs 7–34** strongly influences disease severity; effects were “mainly driven” by differential development of ischemic tissue lesions. The cohort analysis showed severity differences beyond the effects of aging, male sex, hypertension, and hypercholesterolemia. MRI outcomes included WMH, lacunes, microbleeds, and brain parenchymal fraction; mutation location was a major determinant of clinical/imaging profile. (dupe2023phenotypicvariabilityin pages 1-2, dupe2023phenotypicvariabilityin pages 2-3, dupe2023phenotypicvariabilityin media cdee29b5) | Establishes **variant position** as one of the most important predictors of phenotype and a key stratifier for prognosis and trial design. |
| Sukhonpanich, 2024 | Retrospective review of UK prospective CADASIL register plus systematic review; **516 symptomatic** registry patients | **10 ICH cases** identified in the UK register, giving estimated point prevalence **1.9%**. Systematic review added **119 cases**, for **129 total cases** and **142 ICH events**. Mean age at ICH onset **56.6 ± 15.7 years**; **57.4% male**. ICH was the first manifestation in **32 patients (38.1%)** and recurred in **16 (12.4%)**. Commonest sites were **thalamus 58/142 (40.8%)** and **basal ganglia 34/142 (23.9%)**. **Anticoagulation** was associated with higher ICH risk (**20.0% vs 1.9%; p=0.006**), whereas antiplatelets were not. (sukhonpanich2024prevalenceclinicalcharacteristics pages 1-2) | ICH is uncommon but clinically important in CADASIL; the anticoagulation signal is highly relevant to real-world management decisions. |
| Pan, 2023 | TriNetX global health research network analysis; **914 CADASIL patients** identified in US-based EMR data | Median age **60 [IQR 50–69]**; **61.3% female**. **596/914 (65.2%)** had documented cerebrovascular events. Among CADASIL-stroke patients, **89.4%** had ischemic stroke, **27.7%** had co-existing TIA, and **6.2%** had hemorrhagic strokes. Initial stroke occurred at age **≤65 years in 71%**. Male sex was associated with higher stroke risk (**OR 1.37, 95% CI 1.01–1.86**) and higher mortality (**OR 2.72, 95% CI 1.53–4.84**). (pan2023lifelongcerebrovasculardisease pages 1-2) | Demonstrates a high lifetime cerebrovascular burden in real-world practice and suggests **sex-specific risk stratification** may be important. |
| Dunn, 2020 | Clinical diagnostic sequencing evaluation; **680 patient samples**, **764 tests** across Sanger, targeted NGS panel, and WES | Overall mutation detection rate was **14.7% (100/680)**. By method: **Sanger 10.8% (44/407)**, **targeted NGS panel 15.8% (56/354)**, and **WES 1/3** identifying a likely non-NOTCH3 pathogenic variant. Sanger-positive variants clustered mainly in **exon 4 (n=36)**, then **exon 3 (n=3)**, **exon 11 (n=3)**, **exon 18 (n=1)**, **exon 19 (n=1)**. (dunn2020investigatingdiagnosticsequencing pages 1-2) | Supports current practice favoring **broader NGS-based testing** over limited exon-first Sanger approaches for CADASIL diagnostics. |
| Nogueira, 2023 | Brazilian multicenter case series with genetic confirmation; **26 patients** | **16/26 female**; mean disease onset **45 years**. Ischemic stroke was first symptom in **19/26**. Cognitive impairment occurred in **17/26**, dementia in **6/26**, psychiatric manifestations in **16/26**. Recurrent migraine in **8/26**, with aura in **6/8 (75%)**. MRI: temporal lobe WMH in **20 patients (91%)**, external capsule WMH in **15 (68%)**, lacunar infarcts in **18 (82%)**, microbleeds in **9 (41%)**, larger hemorrhages in **2 (9%)**. (nogueira2023clinicalandepidemiological pages 1-2) | Confirms that core CADASIL clinical-radiologic patterns generalize to an admixed Brazilian cohort, while microbleed/hemorrhage rates may vary by population. |
| Mizuta, 2024 | Mechanistic review of NOTCH3/CADASIL biology | CADASIL is described as **adult-onset** and driven primarily by **mutant NOTCH3 extracellular domain (N3ECD) accumulation**, with possible contribution from impaired Notch signaling. The review emphasizes that all known causative mutations are in the **EGFr domain**, most are **cysteine-altering missense variants**, and that N3ECD accumulation with downstream vascular pathology remains the dominant current mechanistic framework. (mizuta2024progresstoclarify pages 1-2) | Provides current expert consensus for the field: disease-modifying strategies will likely need to target **early N3ECD aggregation/vascular injury**, not just downstream stroke consequences. |


*Table: This table compiles recent quantitative and clinically actionable findings in CADASIL, emphasizing cohort sizes, exact effect estimates, and why each study matters for prognosis, diagnosis, and trial design.*

## Expert analysis and current gaps (2023–2024 emphasis)
1) **Variant position and risk categorization are now central to prognosis and trial design.** Large cohorts show EGFr 1–6 vs 7–34 effects on severity, and 2024 prospective data show that risk category predicts 2-year clinical and MRI progression (including incident stroke HR 4.3 for HR vs MR). (cerfontaine2024associationofnotch3 pages 1-2, dupe2023phenotypicvariabilityin pages 1-2)
2) **A key upstream mechanistic gap remains:** despite strong evidence that N3ECD aggregation and GOM are core to pathogenesis, the “process leading to N3ECD accumulation” remains unresolved, complicating rational targeting for disease-modifying therapies. (mizuta2024progresstoclarify pages 1-2)
3) **Real-world diagnosis and early-stage identification are increasingly operationalized via NGS testing and longitudinal biomarker studies.** Diagnostic laboratories report improved detection with targeted NGS panels, while large observational studies now recruit pre-symptomatic carriers to define early biomarkers and endpoints. (dunn2020investigatingdiagnosticsequencing pages 1-2, NCT05677880 chunk 1)

## URLs and publication dates (from retrieved sources)
- Cerfontaine et al., *Neurology* — published 2024-05 (DOI landing): https://doi.org/10.1212/WNL.0000000000209310 (cerfontaine2024associationofnotch3 pages 1-2)
- Dupé et al., *J Cereb Blood Flow Metab* — 2023-10: https://doi.org/10.1177/0271678X221126280 (dupe2023phenotypicvariabilityin pages 1-2)
- Mizuta et al., *Biomolecules* — published 2024-01-18: https://doi.org/10.3390/biom14010127 (mizuta2024progresstoclarify pages 1-2)
- Sukhonpanich & Markus, *Journal of Neurology* — published online 2024-01-13: https://doi.org/10.1007/s00415-023-12177-0 (sukhonpanich2024prevalenceclinicalcharacteristics pages 1-2)
- Pan et al., *Frontiers in Neurology* — published 2023-07-14: https://doi.org/10.3389/fneur.2023.1203985 (pan2023lifelongcerebrovasculardisease pages 1-2)
- Dunn et al., *Human Genomics* — 2020-01: https://doi.org/10.1186/s40246-019-0255-x (dunn2020investigatingdiagnosticsequencing pages 1-2)
- Nogueira et al., *Arquivos de Neuro-Psiquiatria* — published online 2023-05-08: https://doi.org/10.1055/s-0042-1758756 (nogueira2023clinicalandepidemiological pages 1-2)
- Boston et al., *Cerebral Circulation - Cognition and Behavior* — 2024-06-03: https://doi.org/10.1016/j.cccb.2024.100227 (boston2024mostcommonnotch3 pages 1-2)
- ClinicalTrials.gov NCT05677880 — first posted 2023-01-10: https://clinicaltrials.gov/study/NCT05677880 (NCT05677880 chunk 1)
- ClinicalTrials.gov NCT05072483 — first posted 2021-10-11: https://clinicaltrials.gov/study/NCT05072483 (NCT05072483 chunk 1)


References

1. (cerfontaine2024associationofnotch3 pages 1-2): Minne N. Cerfontaine, Remco J. Hack, Benno Gesierich, Marco Duering, Marie-Noëlle W. Witjes-Ané, Mar Rodríguez-Girondo, Gido Gravesteijn, Julie Rutten, and Saskia A.J. Lesnik Oberstein. Association of <i>notch3</i> variant risk category with 2-year clinical and radiologic small vessel disease progression in patients with cadasil. Neurology, May 2024. URL: https://doi.org/10.1212/wnl.0000000000209310, doi:10.1212/wnl.0000000000209310. This article has 12 citations and is from a highest quality peer-reviewed journal.

2. (papakonstantinou2019notch3andcadasil pages 1-3): Eleni Papakonstantinou, Flora Bacopoulou, Dimitrios Brouzas, Vasileios Megalooikonomou, Domenica D'Elia, Erik Bongcam-Rudloff, and Dimitrios Vlachakis. Notch3 and cadasil syndrome: a genetic and structural overview. EMBnet.journal, 24:e921, May 2019. URL: https://doi.org/10.14806/ej.24.0.921, doi:10.14806/ej.24.0.921. This article has 50 citations.

3. (bersano2017cadasiltreatmentand pages 1-3): Anna Bersano, Gloria Bedini, Joshua Oskam, Caterina Mariotti, Franco Taroni, Silvia Baratta, and Eugenio Agostino Parati. Cadasil: treatment and management options. Current Treatment Options in Neurology, 19:1-15, Jul 2017. URL: https://doi.org/10.1007/s11940-017-0468-z, doi:10.1007/s11940-017-0468-z. This article has 58 citations and is from a peer-reviewed journal.

4. (mizuta2024progresstoclarify pages 1-2): Ikuko Mizuta, Yumiko Nakao-Azuma, Hideki Yoshida, Masamitsu Yamaguchi, and Toshiki Mizuno. Progress to clarify how notch3 mutations lead to cadasil, a hereditary cerebral small vessel disease. Biomolecules, 14:127, Jan 2024. URL: https://doi.org/10.3390/biom14010127, doi:10.3390/biom14010127. This article has 25 citations.

5. (hu2021notch3variantsand pages 1-2): Yacen Hu, Qiying Sun, Yafang Zhou, Fang Yi, Haiyun Tang, Lingyan Yao, Yun Tian, Nina Xie, Mengchuan Luo, Zhiqin Wang, Xinxin Liao, Hongwei Xu, and Lin Zhou. Notch3 variants and genotype-phenotype features in chinese cadasil patients. Frontiers in Genetics, Jul 2021. URL: https://doi.org/10.3389/fgene.2021.705284, doi:10.3389/fgene.2021.705284. This article has 39 citations and is from a peer-reviewed journal.

6. (pan2023lifelongcerebrovasculardisease pages 1-2): Alan P. Pan, Thomas Potter, Abdulaziz Bako, Jonika Tannous, Sudha Seshadri, Louise D. McCullough, and Farhaan S. Vahidy. Lifelong cerebrovascular disease burden among cadasil patients: analysis from a global health research network. Frontiers in Neurology, Jul 2023. URL: https://doi.org/10.3389/fneur.2023.1203985, doi:10.3389/fneur.2023.1203985. This article has 13 citations and is from a peer-reviewed journal.

7. (dupe2023phenotypicvariabilityin pages 1-2): Charlotte Dupé, Stéphanie Guey, Lucie Biard, Sokhna Dieng, Jessica Lebenberg, Lina Grosset, Nassira Alili, Dominique Hervé, Elisabeth Tournier-Lasserve, Eric Jouvent, Sylvie Chevret, and Hugues Chabriat. Phenotypic variability in 446 cadasil patients: impact of notch3 gene mutation location in addition to the effects of age, sex and vascular risk factors. Journal of Cerebral Blood Flow & Metabolism, 43:153-166, Oct 2023. URL: https://doi.org/10.1177/0271678x221126280, doi:10.1177/0271678x221126280. This article has 40 citations and is from a highest quality peer-reviewed journal.

8. (kaisaridi2025determiningclinicaldisease pages 1-5): Sofia Kaisaridi, Dominique Herve, Aude Jabouley, Sonia Reyes, Carla Machado, Stéphanie Guey, Abbas Taleb, Fanny Fernandes, Hugues Chabriat, and Sophie Tezenas Du Montcel. Determining clinical disease progression in symptomatic patients with cadasil. Neurology, Jan 2025. URL: https://doi.org/10.1212/wnl.0000000000210193, doi:10.1212/wnl.0000000000210193. This article has 3 citations and is from a highest quality peer-reviewed journal.

9. (cao2024phenotypesassociatedwith pages 13-14): Yuan Cao, Ding-Ding Zhang, Fei Han, Nan Jiang, Ming Yao, and Yi-Cheng Zhu. Phenotypes associated with notch3 cysteine-sparing mutations in patients with clinical suspicion of cadasil: a systematic review. International Journal of Molecular Sciences, 25:8796, Aug 2024. URL: https://doi.org/10.3390/ijms25168796, doi:10.3390/ijms25168796. This article has 7 citations.

10. (sukhonpanich2024prevalenceclinicalcharacteristics pages 1-2): Nontapat Sukhonpanich and Hugh S. Markus. Prevalence, clinical characteristics, and risk factors of intracerebral haemorrhage in cadasil: a case series and systematic review. Journal of Neurology, 271:2423-2433, Jan 2024. URL: https://doi.org/10.1007/s00415-023-12177-0, doi:10.1007/s00415-023-12177-0. This article has 13 citations and is from a domain leading peer-reviewed journal.

11. (nogueira2023clinicalandepidemiological pages 1-2): Renata Nogueira, Christian Marques Couto, Pérola de Oliveira, Bernardo José Alves Ferreira Martins, and Vinícius Viana Abreu Montanaro. Clinical and epidemiological profiles from a case series of 26 brazilian cadasil patients. Arquivos de Neuro-Psiquiatria, 81:417-425, May 2023. URL: https://doi.org/10.1055/s-0042-1758756, doi:10.1055/s-0042-1758756. This article has 10 citations and is from a peer-reviewed journal.

12. (boston2024mostcommonnotch3 pages 1-2): Georgina Boston, Dan Jobson, Toshiki Mizuno, Masafumi Ihara, and Raj N Kalaria. Most common notch3 mutations causing cadasil or cadasil-like cerebral small vessel disease: a systematic review. Cerebral Circulation - Cognition and Behavior, 6:100227, Jun 2024. URL: https://doi.org/10.1016/j.cccb.2024.100227, doi:10.1016/j.cccb.2024.100227. This article has 31 citations.

13. (akrich2024geneticdiagnosisof pages 1-2): Madeleine Akrich, Vololona Rabeharisoa, Florence Paterson, and Hugues Chabriat. Genetic diagnosis of individuals at risk of cadasil: prospect for future therapeutic development. Journal of Neurology, 271:6912-6922, Sep 2024. URL: https://doi.org/10.1007/s00415-024-12640-6, doi:10.1007/s00415-024-12640-6. This article has 4 citations and is from a domain leading peer-reviewed journal.

14. (dunn2020investigatingdiagnosticsequencing pages 1-2): P. J. Dunn, N. Maksemous, R. A. Smith, H. G. Sutherland, L. M. Haupt, and L. R. Griffiths. Investigating diagnostic sequencing techniques for cadasil diagnosis. Human Genomics, Jan 2020. URL: https://doi.org/10.1186/s40246-019-0255-x, doi:10.1186/s40246-019-0255-x. This article has 23 citations and is from a peer-reviewed journal.

15. (dupe2023phenotypicvariabilityin media cdee29b5): Charlotte Dupé, Stéphanie Guey, Lucie Biard, Sokhna Dieng, Jessica Lebenberg, Lina Grosset, Nassira Alili, Dominique Hervé, Elisabeth Tournier-Lasserve, Eric Jouvent, Sylvie Chevret, and Hugues Chabriat. Phenotypic variability in 446 cadasil patients: impact of notch3 gene mutation location in addition to the effects of age, sex and vascular risk factors. Journal of Cerebral Blood Flow & Metabolism, 43:153-166, Oct 2023. URL: https://doi.org/10.1177/0271678x221126280, doi:10.1177/0271678x221126280. This article has 40 citations and is from a highest quality peer-reviewed journal.

16. (NCT05677880 chunk 1):  Cerebral Autosomal Dominant Arteriopathy With Subcortical Infarcts and Leukoencephalopathy (CADASIL) Study. University of Wisconsin, Madison. 2022. ClinicalTrials.gov Identifier: NCT05677880

17. (NCT05072483 chunk 1):  Natural History Study of CADASIL. National Heart, Lung, and Blood Institute (NHLBI). 2022. ClinicalTrials.gov Identifier: NCT05072483

18. (dupe2023phenotypicvariabilityin pages 2-3): Charlotte Dupé, Stéphanie Guey, Lucie Biard, Sokhna Dieng, Jessica Lebenberg, Lina Grosset, Nassira Alili, Dominique Hervé, Elisabeth Tournier-Lasserve, Eric Jouvent, Sylvie Chevret, and Hugues Chabriat. Phenotypic variability in 446 cadasil patients: impact of notch3 gene mutation location in addition to the effects of age, sex and vascular risk factors. Journal of Cerebral Blood Flow & Metabolism, 43:153-166, Oct 2023. URL: https://doi.org/10.1177/0271678x221126280, doi:10.1177/0271678x221126280. This article has 40 citations and is from a highest quality peer-reviewed journal.

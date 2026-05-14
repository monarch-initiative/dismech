---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T10:42:24.489428'
end_time: '2026-05-09T10:55:45.184681'
duration_seconds: 800.7
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Seckel syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Seckel syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Seckel syndrome** covering all of the
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
- **Disease Name:** Seckel syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Seckel syndrome** covering all of the
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


# Seckel syndrome (microcephalic primordial dwarfism): disease characteristics report

## Target disease
- **Disease name:** Seckel syndrome
- **Category:** Mendelian (autosomal recessive microcephalic primordial dwarfism)
- **Core concept:** A genetically heterogeneous syndrome in which impaired genome maintenance (DNA damage response/replication stress) and/or centrosome–centriole dysfunction leads to profound prenatal-onset growth failure with severe microcephaly and neurodevelopmental impairment. (farcy2023geneticprimarymicrocephalies pages 2-4, zhang2023twonovelvariants pages 1-2, mcintyre2012disruptionofmouse pages 1-2)

---

## 1. Disease information

### 1.1 Definition and overview (current understanding)
Seckel syndrome is classically defined by **symmetrical intrauterine growth restriction (IUGR) and postnatal proportionate short stature**, **severe microcephaly**, **intellectual disability**, and characteristic craniofacial features often described as “**bird-headed**” (prominent nose/beaked nose and micrognathia). (zhang2023twonovelvariants pages 1-2, farcy2023geneticprimarymicrocephalies pages 2-4, kelana2023caseofseckel pages 1-2)

A recent review of centrosome-related microcephalies places Seckel syndrome within **microcephalic primordial dwarfism (MPD)** and summarizes diagnostic “threshold-like” anthropometrics, including childhood short stature around **−6 to −8 SD** and adult height around **~120 cm**, with markedly reduced head circumference (adult **~39–42 cm**, newborn **~27 cm** in the cited clinical criteria). (farcy2023geneticprimarymicrocephalies pages 2-4)

**Source types:** The overview above is derived from **aggregated disease-level resources and reviews** plus **patient-level case reports** (e.g., variant discovery and stroke case report). (zhang2023twonovelvariants pages 1-2, mudassir2023microcephalyshortstature pages 1-2, alavi2024arterialstrokein pages 3-4)

### 1.2 Key identifiers (as available in retrieved evidence)
- **OMIM:** **Seckel syndrome (OMIM #210600)** (farcy2023geneticprimarymicrocephalies pages 2-4)
- **Orphanet:** **ORPHA:808** (jentcy2021seckelsyndrome pages 1-1)
- **MeSH-like identifiers in ClinicalTrials.gov records:** “Seckel syndrome 1” (**C537533**) appears in an observational study record. (NCT03139903 chunk 1)

**Not found in the retrieved sources (therefore not asserted here):** MONDO ID, ICD-10/ICD-11 code(s), and canonical MeSH descriptor ID for Seckel syndrome.

### 1.3 Common synonyms / alternative names
- “Seckel syndrome” is frequently discussed as a **Seckel syndrome spectrum** within MPD and in historical nosology (e.g., “Primary autosomal recessive microcephalies and Seckel syndrome spectrum disorders”). (jurca2024clinicalchallengesin pages 1-2, zhang2023twonovelvariants pages 8-8)
- “Microcephalic primordial dwarfism” is often used as the broader clinical grouping. (jentcy2021seckelsyndrome pages 1-1, jurca2024clinicalchallengesin pages 1-2)

---

## 2. Etiology

### 2.1 Primary causal factors
**Genetic (germline) biallelic pathogenic variants** are the primary causal factor, consistent with autosomal recessive inheritance. (kelana2023caseofseckel pages 1-2, jurca2024clinicalchallengesin pages 4-6)

Seckel syndrome is **genetically heterogeneous**. For example, a 2023 gene-discovery-oriented case report states: “**Forty cases of Seckel syndrome have been reported to date in the literature due to mutations in the ATR, TRAIP, RBBP8, NSMCE2, NIN, CENPJ, DNA2, CEP152 and CEP63 genes**,” while also presenting RTTN as an additional cause in their family. (mudassir2023microcephalyshortstature pages 1-2)

### 2.2 Risk factors
- **Major risk factor:** Having **biallelic (recessive) pathogenic variants** in one of multiple causal genes (see Section 4). (mudassir2023microcephalyshortstature pages 1-2, zhang2023twonovelvariants pages 1-2)
- **Family history/consanguinity:** Many gene-discovery case reports are from consanguineous families (e.g., RTTN and CEP152 reports), supporting a recessive architecture but without population-level quantification in the retrieved excerpts. (mudassir2023microcephalyshortstature pages 1-2, zhang2023twonovelvariants pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No protective factors or specific gene–environment interactions were identified in the retrieved evidence. Given the congenital Mendelian etiology, environmental modifiers are plausible but not established here.

---

## 3. Phenotypes

### 3.1 Core phenotypes (with ontology suggestions)
Below are high-frequency, defining features. Frequency data are limited in the retrieved sources; where quantitative estimates exist, they are provided.

1) **Prenatal-onset growth restriction / primordial dwarfism**
- **Typical onset:** prenatal (IUGR) with persistent postnatal growth restriction. (farcy2023geneticprimarymicrocephalies pages 2-4, kelana2023caseofseckel pages 1-2)
- **HPO suggestions:** HP:0001511 (Intrauterine growth restriction), HP:0004322 (Short stature), HP:0000252 (Microcephaly).

2) **Severe microcephaly with neurodevelopmental impairment**
- **Phenotype type:** clinical sign (microcephaly), symptom domain (intellectual disability). (farcy2023geneticprimarymicrocephalies pages 2-4, zhang2023twonovelvariants pages 1-2)
- **HPO suggestions:** HP:0000252 (Microcephaly), HP:0001249 (Intellectual disability).

3) **Craniofacial dysmorphology (“bird-headed” facies)**
- **Reported features:** prominent/beaked nose, narrow face, micrognathia, prominent eyes. (kelana2023caseofseckel pages 1-2, alavi2024arterialstrokein pages 2-3)
- **HPO suggestions:** HP:0000365 (Low-set ears), HP:0000347 (Micrognathia), HP:0000411 (Prominent nose) [or equivalent HPO term], HP:0000520 (Proptosis) (as applicable).

4) **Congenital anomalies / multisystem involvement (variable)**
- Reviews and case series note possible **cardiovascular anomalies** and **myelodysplasia** among additional features in some patients. (zhang2023twonovelvariants pages 1-2)
- **HPO suggestions:** HP:0001627 (Abnormality of the cardiovascular system), HP:0001875 (Neutropenia)/HP:0001890 (Thrombocytopenia) if myelodysplasia manifests.

### 3.2 Notable complications with quantitative data: CNS vasculopathy / stroke
A 2024 case report (with literature synthesis) reports that **CNS vasculopathy** occurs in **3.16% (8/253)** of Seckel syndrome patients and that **moyamoya disease** accounts for **1.97%**; reported mean age **13.5 years** (range **6–19**) with equal sex distribution. (alavi2024arterialstrokein pages 4-4)

Clinical presentations can include headache, seizures, weakness/coma, and imaging findings such as carotid narrowing/obliteration, collateral formation, aneurysms, infarcts, and hemorrhage. (alavi2024arterialstrokein pages 4-4)

**HPO suggestions:** HP:0001297 (Stroke), HP:0001344 (Cerebral aneurysm), HP:0001324 (Hemiplegia), HP:0002073 (Cerebral infarction).

### 3.3 Quality of life / function (reported intervention outcomes)
A single-case rehabilitation report using proprioceptive neuromuscular facilitation (PNF/Kabat) in an 18-year-old describes objective functional changes: **Short Physical Performance Battery (SPPB) improved from 4 to 8**, **Timed Up and Go (TUG) improved from 28.0 s to 19.9 s**, and grip strength increased **23.4% (right)** and **27.4% (left)**, while ADL scale and DASH did not show significant improvements. (souza2022seckelsyndromecase pages 8-11, souza2022seckelsyndromecase pages 11-12)

---

## 4. Genetic / molecular information

### 4.1 Causal genes (examples supported in retrieved evidence)
Evidence supports biallelic pathogenic variants across multiple modules:

**DNA damage response / replication stress genes** (ATR pathway and partners):
- **ATR**, **RBBP8 (CtIP)**, **DNA2**, **TRAIP**, **NSMCE2** (listed across review/case sources as Seckel/MPD-associated). (mudassir2023microcephalyshortstature pages 1-2, mcintyre2012disruptionofmouse pages 1-2, patrick2017atrisa pages 58-61)

**Centrosome/centriole and mitotic spindle genes**:
- **CENPJ**, **CEP152**, **CEP63**, **NIN**, **CDK5RAP2**, **RTTN**. (mcintyre2012disruptionofmouse pages 1-2, zhang2023twonovelvariants pages 1-2, mudassir2023microcephalyshortstature pages 1-2)

A 2023 study notes that Seckel syndrome 5 (**SCKL5; MIM#613823**) is caused by pathogenic variants in **CEP152**, which encodes a centrosomal protein involved in centrosome duplication and genome integrity / DNA damage responses. (zhang2023twonovelvariants pages 1-2)

### 4.2 Pathogenic variants (explicit examples from 2023–2024 literature in this corpus)
- **CEP152:** c.1060C>T (**p.Arg354\***, nonsense) and c.1414-14A>G (non-canonical splice variant) were identified by trio-WES; RT-PCR showed **exon 12 skipping** for the splice variant. (zhang2023twonovelvariants pages 1-2)
- **RTTN:** NM_173630.4:c.57G>T (**p.Glu19Asp**, missense) reported in a consanguineous Pakistani family with Seckel syndrome features and cataract; discovered by WES. (mudassir2023microcephalyshortstature pages 1-2)

**Variant interpretation framework:** The CEP152 paper explicitly used confirmatory molecular approaches (qPCR/RT-PCR/Sanger) consistent with clinical variant interpretation practices. (zhang2023twonovelvariants pages 1-2)

### 4.3 Functional consequences (high-level)
Across the gene set above, a convergent theme is impaired:
- DNA replication-stress response and checkpoint signaling (ATR pathway), and/or
- centrosome/centriole integrity and spindle assembly
leading to genomic instability, mitotic failure, and cell loss during development. (patrick2017atrisa pages 58-61, mcintyre2012disruptionofmouse pages 1-2)

**Population allele frequencies:** Not extractable from the retrieved evidence excerpts; therefore not asserted.

---

## 5. Environmental information
No specific environmental, lifestyle, or infectious contributors were identified in the retrieved evidence; Seckel syndrome is presented as a congenital Mendelian disorder. (kelana2023caseofseckel pages 1-2, mudassir2023microcephalyshortstature pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Mechanistic model (causal chain)
A practical synthesis supported by primary and review literature:

1) **Upstream trigger:** biallelic loss-of-function or hypomorphic variants in genes controlling DNA damage response/replication stress (e.g., ATR module) and/or centrosome–centriole biogenesis/spindle function (e.g., CENPJ/CEP152/RTTN module). (patrick2017atrisa pages 58-61, mcintyre2012disruptionofmouse pages 1-2, mudassir2023microcephalyshortstature pages 1-2)
2) **Cellular consequence:** defective checkpoint/repair and/or abnormal centriole number/structure → abnormal mitoses, aneuploidy/micronuclei, replication-associated DNA damage, and increased apoptosis. (mcintyre2012disruptionofmouse pages 1-2, mcintyre2012disruptionofmouse pages 6-8)
3) **Tissue/developmental consequence:** impaired proliferation/survival of neural progenitors and other growth-critical lineages during embryogenesis → severe microcephaly and proportionate primordial dwarfism. (farcy2023geneticprimarymicrocephalies pages 2-4, mcintyre2012disruptionofmouse pages 1-2)

A key mechanistic statement from the Cenpj mouse model study is that “**increased cell death due to mitotic failure during embryonic development is likely to contribute to the proportionate dwarfism**.” (mcintyre2012disruptionofmouse pages 1-2)

### 6.2 Pathways, processes, cell types (ontology suggestions)

**GO Biological Process (examples):**
- DNA replication checkpoint / response to replication stress (GO terms associated with ATR module)
- DNA damage response, signal transduction by p53 class mediator (for downstream apoptosis)
- Centrosome duplication / centriole assembly
- Mitotic spindle organization

**CL Cell types (examples, mechanistically relevant):**
- Neural progenitor cell (radial glia) (primary microcephaly mechanism context) (farcy2023geneticprimarymicrocephalies pages 2-4)

**Note:** Specific GO and CL identifiers are not explicitly enumerated in the retrieved text excerpts; the above are mechanistically aligned suggestions based on the described biology.

### 6.3 Visual evidence (genes/pathways summary)
Cropped figures/tables from a 2023 review summarize Seckel/MPD genes and their functional localization at the centrosome/spindle and DNA repair pathways. (farcy2023geneticprimarymicrocephalies media eb9668c0, farcy2023geneticprimarymicrocephalies media 1a99a141, farcy2023geneticprimarymicrocephalies media 0b042e40, farcy2023geneticprimarymicrocephalies media c608a08c)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level (high-level)
- **Central nervous system:** microcephaly and neurodevelopmental impairment are core; cerebrovascular involvement (moyamoya/non-moyamoya vasculopathy, aneurysms, infarcts/hemorrhage) is a clinically important complication in a minority. (farcy2023geneticprimarymicrocephalies pages 2-4, alavi2024arterialstrokein pages 4-4, alavi2024arterialstrokein pages 3-4)
- **Craniofacial skeleton:** characteristic craniofacial dysmorphology is typical. (kelana2023caseofseckel pages 1-2)

### 7.2 Tissue/cell level
- Developmentally critical proliferative compartments (especially neural progenitors) are implicated by the primary microcephaly/MPD framework and the cited centrosome/DDR mechanisms. (farcy2023geneticprimarymicrocephalies pages 2-4, mcintyre2012disruptionofmouse pages 1-2)

### 7.3 Subcellular level (GO Cellular Component suggestions)
- **Centrosome/centriole** and **mitotic spindle** compartments are repeatedly implicated across causal genes (e.g., CEP152, CENPJ, RTTN). (zhang2023twonovelvariants pages 1-2, mcintyre2012disruptionofmouse pages 1-2, mudassir2023microcephalyshortstature pages 1-2)

---

## 8. Temporal development

- **Onset:** typically **congenital/prenatal** (IUGR, congenital microcephaly). (farcy2023geneticprimarymicrocephalies pages 2-4, kelana2023caseofseckel pages 1-2)
- **Course:** lifelong short stature and microcephaly; neurodevelopmental impairments are persistent. Rare but serious later complications include cerebrovascular events in childhood/adolescence. (alavi2024arterialstrokein pages 4-4, alavi2024arterialstrokein pages 1-2)

---

## 9. Inheritance and population

### 9.1 Inheritance
- Predominantly **autosomal recessive**. (kelana2023caseofseckel pages 1-2, jurca2024clinicalchallengesin pages 4-6)

### 9.2 Epidemiology (statistics from recent sources; interpret cautiously)
Epidemiologic data are limited and inconsistent across sources:
- A 2024 review/case study states Seckel syndrome affects **“1 in 10,000 children”** and that **~100 cases** have been reported. (jurca2024clinicalchallengesin pages 4-6)
- A 2022 rehabilitation case report cites Orphanet (2021) and reports an estimated prevalence/incidence of **0.2 per 100,000 live births** and also notes the rarity of published families. (souza2022seckelsyndromecase pages 2-4)

Because Seckel syndrome is genetically heterogeneous and historically variably defined within MPD, differences in ascertainment and labeling likely contribute to discrepant estimates. (alkuraya2015primordialdwarfisman pages 1-2, jurca2024clinicalchallengesin pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical diagnosis
Clinical suspicion is based on the primordial dwarfism pattern (prenatal-onset growth restriction), severe microcephaly, characteristic facial features, and neurodevelopmental delay/intellectual disability. (farcy2023geneticprimarymicrocephalies pages 2-4, kelana2023caseofseckel pages 1-2)

### 10.2 Genetic testing strategies (real-world workflows)
A 2023 molecularly solved CEP152 case illustrates a practical diagnostic ladder:
- **Karyotype analysis** and **CNV-seq** were normal.
- **Trio whole-exome sequencing (WES)** identified compound heterozygous CEP152 variants.
- **qRT-PCR and RT-PCR** demonstrated reduced expression and aberrant splicing (exon skipping), with **Sanger sequencing** confirmation. (zhang2023twonovelvariants pages 1-2)

A 2023 RTTN case similarly used **WES** to discover a novel biallelic missense variant. (mudassir2023microcephalyshortstature pages 1-2)

### 10.3 Imaging and complication screening
In the context of neurologic symptoms, a 2024 pediatric case used MRI (DWI/ADC) to confirm acute MCA territory infarction and vascular imaging (MRA/CTA) showing internal carotid narrowing/obliteration and collateralization. (alavi2024arterialstrokein pages 1-2, alavi2024arterialstrokein pages 4-5)

The same report recommends **early neuroimaging** for children with Seckel syndrome/related MPD when stroke is suspected, and highlights consideration of medical therapy and potential revascularization in moyamoya-like disease (noting evidence remains limited). (alavi2024arterialstrokein pages 4-4)

### 10.4 Differential diagnosis
Clinical overlap exists with other primordial dwarfism syndromes and short stature disorders; one case-oriented discussion lists alternatives such as Hallermann–Streiff, Dyggve–Melchior–Clausen, and Cockayne syndrome and emphasizes that definitive diagnosis often requires genetic testing. (kelana2023caseofseckel pages 4-5)

---

## 11. Outcome / prognosis
Evidence in the retrieved sources is limited and largely case-based. A clinical case report notes that life expectancy can be prolonged and states patients “can live up to **75 years**,” but this should be interpreted cautiously given the lack of cohort-level survival analyses in the excerpted evidence. (kelana2023caseofseckel pages 4-5)

A major morbidity driver for a subset of patients is cerebrovascular disease (ischemic stroke, aneurysm, hemorrhage), which—while uncommon—can produce long-term neurological deficits requiring rehabilitation. (alavi2024arterialstrokein pages 3-4, alavi2024arterialstrokein pages 4-4)

---

## 12. Treatment

### 12.1 Disease-modifying therapy
No disease-specific curative pharmacotherapy is established in the retrieved evidence; management is described as supportive. (kelana2023caseofseckel pages 1-2, kelana2023caseofseckel pages 4-5)

### 12.2 Supportive and rehabilitative care (real-world implementations)
- A case-based clinical discussion recommends **physiotherapy** to maintain mobility and balance, reduce bony deformities, and improve independence, as well as family counseling. (kelana2023caseofseckel pages 4-5)
- A PNF/Kabat rehabilitation case (20 sessions over 10 weeks) reported objective improvements in balance/strength/agility measures but not broad ADL scores. (souza2022seckelsyndromecase pages 8-11, souza2022seckelsyndromecase pages 11-12)

### 12.3 Management of cerebrovascular complications
In a 2024 pediatric stroke case with intracranial vasculopathy, management included **aspirin 5 mg/kg**; surgical revascularization was not performed due to lack of consent, and the patient received inpatient rehabilitation and ongoing physiotherapy, with residual weakness at 10 months. (alavi2024arterialstrokein pages 3-4, alavi2024arterialstrokein pages 4-5)

**MAXO term suggestions (examples):**
- Supportive care / multidisciplinary management; physical therapy/rehabilitation; antiplatelet therapy (for secondary stroke prevention when indicated).

---

## 13. Prevention
Primary prevention of Seckel syndrome is not applicable in the conventional sense because it is congenital genetic disease; prevention focuses on **genetic counseling and reproductive planning**, which is explicitly referenced in the context of solved molecular diagnoses (e.g., improving pregnancy plans after defining CEP152 variants). (zhang2023twonovelvariants pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in the retrieved evidence.

---

## 15. Model organisms
A landmark mouse model study shows that disruption of **Cenpj** (a centriole biogenesis regulator) can **phenocopy aspects of Seckel syndrome**, including growth defects and cellular genomic instability.

Quantitative examples from Cenpj hypomorphic mice include altered glucose response (e.g., **20.5±0.7 mmol/L vs 30.7±1.60 mmol/L at 15 minutes; P = 2.6×10−5**) and increased micronucleated erythrocytes (P = 4×10−6), consistent with spontaneous genomic instability. (mcintyre2012disruptionofmouse pages 6-8)

Mechanistically, the authors argue the instability is linked to centriole/centrosome defects rather than defective ATR/ATM DNA damage signaling in that model, supporting mechanistic heterogeneity across Seckel genes. (mcintyre2012disruptionofmouse pages 6-8, mcintyre2012disruptionofmouse pages 1-2)

---

## Recent developments (2023–2024 highlights)

1) **2023—CEP152 variant spectrum expansion in Seckel syndrome 5:** A Chinese family was solved by trio-WES and functional RNA assays, identifying **CEP152 c.1060C>T (p.Arg354\*)** and **c.1414-14A>G** with exon skipping, extending knowledge of non-canonical splice variation. (Published Jan 2023; https://doi.org/10.3389/fgene.2022.1052915) (zhang2023twonovelvariants pages 1-2)

2) **2023—RTTN as a Seckel-spectrum gene in a consanguineous family:** A novel biallelic missense RTTN variant **c.57G>T (p.Glu19Asp)** was reported with microcephaly, short stature, severe intellectual disability, absent speech, and cataracts, broadening the phenotype spectrum. (Published Jun 2023; https://doi.org/10.3390/children10061027) (mudassir2023microcephalyshortstature pages 1-2)

3) **2024—Quantified cerebrovascular risk and stroke phenotype:** A 2024 stroke case report summarizes a systematic review reporting CNS vasculopathy **3.16%** and moyamoya **1.97%** in Seckel syndrome and provides detailed vascular imaging patterns (carotid narrowing/obliteration with collaterals). (Published May 2024; https://doi.org/10.1002/ccr3.8871) (alavi2024arterialstrokein pages 4-4, alavi2024arterialstrokein pages 4-5)

---

## Current applications and real-world implementations

- **Genomic diagnostics:** Trio-WES with reflex transcript assays can solve clinically suspected Seckel syndrome when karyotype/CNV testing is normal, enabling family planning and variant-specific counseling. (zhang2023twonovelvariants pages 1-2)
- **Natural history and risk surveillance:** Observational studies/registries collect longitudinal phenotype, imaging, and genetic data to refine prognosis and management (notably vascular screening).
  - **NCT03139903** (completed; enrollment 30) included **cerebral angio-MRI**, cognitive testing (WISC-IV), visual acuity, and multidisciplinary evaluations with initiation of supportive care (speech therapy/psychomotricity). (NCT03139903 chunk 1)
  - **NCT04569149** (registry; target ~200; chart review) collects specialist evaluations, surgeries, labs, genetic tests, and imaging (including CT/MRI/MRA) to define natural history and risk factors. (NCT04569149 chunk 1)

---

## Expert opinions / authoritative analysis (as supported by evidence)

- A review on primordial dwarfism emphasizes that “Seckel syndrome” has historically been a **loosely used label** within primordial dwarfism and cautions clinicians to use broader “primordial dwarfism” terminology until specialist subtyping is performed, reflecting genuine phenotypic/genetic overlap within MPD. (alkuraya2015primordialdwarfisman pages 1-2)
- A 2024 case report synthesizes available evidence on cerebrovascular anomalies and supports proactive neurovascular evaluation in symptomatic children with Seckel/MPD due to the risk of infarction/hemorrhage. (alavi2024arterialstrokein pages 4-4)

---

## Evidence-backed summary table (knowledge-base ready)

| Topic | Key facts (with numbers where available) | Example evidence/quote | Source (first author year, journal) | PMID/DOI/URL if available |
|---|---|---|---|---|
| Definition / core features | Seckel syndrome is a rare **autosomal recessive** microcephalic primordial dwarfism characterized by **intrauterine and postnatal growth restriction**, **severe/proportionate microcephaly**, **intellectual disability**, and a characteristic **“bird-headed” facies**; adult height is reported around **120 cm**, childhood short stature about **−6 to −8 SD**, and newborn OFC about **27 cm** with adult HC **39–42 cm** in one review (zhang2023twonovelvariants pages 1-2, farcy2023geneticprimarymicrocephalies pages 2-4, jentcy2021seckelsyndrome pages 1-1). | “rare autosomal recessive inherited disorder… mainly characterized by intrauterine and postnatal growth restrictions, microcephaly, intellectual disability, and a typical ‘bird-head’ facial appearance” (zhang2023twonovelvariants pages 1-2) | Zhang 2023, *Frontiers in Genetics*; Farcy 2023, *Cells* | DOI: 10.3389/fgene.2022.1052915; https://doi.org/10.3389/fgene.2022.1052915 ; DOI: 10.3390/cells12131807; https://doi.org/10.3390/cells12131807 |
| Identifiers | Curated identifiers directly supported in gathered evidence: **OMIM #210600** for Seckel syndrome; **ORPHA:808**; a trial record also lists **“Seckel syndrome 1” C537533** as a MeSH-like term (farcy2023geneticprimarymicrocephalies pages 2-4, jentcy2021seckelsyndrome pages 1-1, NCT03139903 chunk 1). | “OMIM # 210600” and “ORPHA:808” (farcy2023geneticprimarymicrocephalies pages 2-4, jentcy2021seckelsyndrome pages 1-1) | Farcy 2023, *Cells*; Jentcy 2021, *Definitions/Qeios*; ClinicalTrials.gov | DOI: 10.3390/cells12131807; https://doi.org/10.3390/cells12131807 ; DOI: 10.32388/9UTNHS; https://doi.org/10.32388/9utnhs ; NCT03139903 |
| Inheritance / nosology | Inheritance is predominantly **autosomal recessive**; Seckel syndrome is classified within **primordial dwarfism**, specifically **microcephalic primordial dwarfism (MPD)** / “Seckel syndrome spectrum disorders” in historical nosology (kelana2023caseofseckel pages 1-2, farcy2023geneticprimarymicrocephalies pages 2-4, jurca2024clinicalchallengesin pages 1-2). | “Seckel syndrome is an extremely rare syndrome with autosomal recessive inheritance” (jurca2024clinicalchallengesin pages 4-6) | Kelana 2023, *Open Access Macedonian Journal of Medical Sciences*; Farcy 2023, *Cells*; Jurca 2024, *Medicina* | DOI: 10.3889/oamjms.2023.10988; https://doi.org/10.3889/oamjms.2023.10988 ; DOI: 10.3390/cells12131807; https://doi.org/10.3390/cells12131807 ; DOI: 10.3390/medicina60111906; https://doi.org/10.3390/medicina60111906 |
| Epidemiology | Evidence is sparse and inconsistent. Reported figures include **~100 cases** in the literature/worldwide and estimates of **1 in 10,000 children/births**; an Orphanet-derived figure cited in a rehab case report gives **0.2 per 100,000 live births** (jurca2024clinicalchallengesin pages 4-6, souza2022seckelsyndromecase pages 2-4, kelana2023caseofseckel pages 1-2). | “Approximately 100 cases have been reported in the literature” and “affecting 1 in 10,000 children” (jurca2024clinicalchallengesin pages 4-6); “estimated prevalence/incidence of 0.2 per 100,000 live births” (souza2022seckelsyndromecase pages 2-4) | Jurca 2024, *Medicina*; Souza 2022, *Research, Society and Development*; Kelana 2023, *OAMJMS* | DOI: 10.3390/medicina60111906; https://doi.org/10.3390/medicina60111906 ; DOI: 10.33448/rsd-v11i2.25080; https://doi.org/10.33448/rsd-v11i2.25080 ; DOI: 10.3889/oamjms.2023.10988; https://doi.org/10.3889/oamjms.2023.10988 |
| Major causal genes | Gathered evidence supports substantial genetic heterogeneity. Recurrently cited genes include **ATR, RBBP8, CENPJ, CEP152, CEP63, NIN, DNA2, TRAIP, NSMCE2, CDK5RAP2**, and newer spectrum associations including **RTTN** (zhang2023twonovelvariants pages 1-2, patrick2017atrisa pages 58-61, mudassir2023microcephalyshortstature pages 1-2, mcintyre2012disruptionofmouse pages 1-2). | “Forty cases of Seckel syndrome have been reported to date… due to mutations in the ATR, TRAIP, RBBP8, NSMCE2, NIN, CENPJ, DNA2, CEP152 and CEP63 genes” (mudassir2023microcephalyshortstature pages 1-2) | Mudassir 2023, *Children*; Zhang 2023, *Frontiers in Genetics*; Yigit 2015, *Molecular Genetics & Genomic Medicine* | DOI: 10.3390/children10061027; https://doi.org/10.3390/children10061027 ; DOI: 10.3389/fgene.2022.1052915; https://doi.org/10.3389/fgene.2022.1052915 ; DOI: 10.1002/mgg3.158; https://doi.org/10.1002/mgg3.158 |
| Example pathogenic variants | Specific variants documented in gathered evidence include **CEP152 c.1060C>T (p.Arg354\*)**, **CEP152 c.1414-14A>G** causing **exon 12 skipping**, and **RTTN NM_173630.4:c.57G>T (p.Glu19Asp)**; the CEP152 case had normal karyotype/CNV-seq with pathogenic findings only on trio-WES plus transcript studies (zhang2023twonovelvariants pages 1-2, mudassir2023microcephalyshortstature pages 1-2). | “Two novel variants in CEP152, c.1060C>T (p.Arg354*) and c.1414-14A>G, were identified” (zhang2023twonovelvariants pages 1-2); “Whole-exome sequencing discovered… c.57G > T (p.Glu19Asp)” (mudassir2023microcephalyshortstature pages 1-2) | Zhang 2023, *Frontiers in Genetics*; Mudassir 2023, *Children* | DOI: 10.3389/fgene.2022.1052915; https://doi.org/10.3389/fgene.2022.1052915 ; DOI: 10.3390/children10061027; https://doi.org/10.3390/children10061027 |
| Mechanisms / pathways | Two major mechanistic modules emerge: **DNA damage response / replication stress** (ATR–ATRIP, RBBP8/CtIP, DNA2, TRAIP) and **centrosome / centriole biogenesis and mitotic spindle dysfunction** (CENPJ, CEP152, CEP63, NIN, CDK5RAP2, RTTN). Downstream consequences include **genomic instability, mitotic failure, apoptosis**, and impaired growth/neurodevelopment (patrick2017atrisa pages 58-61, mcintyre2012disruptionofmouse pages 6-8, mcintyre2012disruptionofmouse pages 1-2). | “increased cell death due to mitotic failure during embryonic development is likely to contribute to the proportionate dwarfism” (mcintyre2012disruptionofmouse pages 1-2) | McIntyre 2012, *PLoS Genetics*; O’Driscoll 2012, *Cold Spring Harbor Perspectives in Biology*; Farcy 2023, *Cells* | DOI: 10.1371/journal.pgen.1003022; https://doi.org/10.1371/journal.pgen.1003022 ; DOI: 10.1101/cshperspect.a012773; https://doi.org/10.1101/cshperspect.a012773 ; DOI: 10.3390/cells12131807; https://doi.org/10.3390/cells12131807 |
| Diagnostics / testing approach | Diagnosis often begins clinically but increasingly relies on **molecular testing**. Reported workflows include **karyotype**, **CNV-seq**, **trio-WES**, **Sanger confirmation**, and **RNA studies (qRT-PCR/RT-PCR)**; in one CEP152 case, **karyotype and CNV-seq were normal** and **trio-WES** solved the case (zhang2023twonovelvariants pages 1-2, kelana2023caseofseckel pages 1-2, NCT03139903 chunk 1). | “The karyotype analysis and CNV-seq were normal in the proband… Two novel variants in CEP152… were identified… through trio-WES” (zhang2023twonovelvariants pages 1-2) | Zhang 2023, *Frontiers in Genetics*; Kelana 2023, *OAMJMS*; ClinicalTrials.gov NCT03139903 | DOI: 10.3389/fgene.2022.1052915; https://doi.org/10.3389/fgene.2022.1052915 ; DOI: 10.3889/oamjms.2023.10988; https://doi.org/10.3889/oamjms.2023.10988 ; NCT03139903 |
| Complications: CNS vasculopathy / stroke | CNS vasculopathy is uncommon but clinically important. A 2024 case report cites a systematic-review estimate of **3.16% (8/253)** of Seckel syndrome patients with CNS vasculopathy, with **moyamoya disease in 1.97%**; mean age was **13.5 years (range 6–19)**. Reported lesions include carotid narrowing/obliteration, aneurysms, infarction, subarachnoid hemorrhage, and moyamoya/non-moyamoya collateral patterns (alavi2024arterialstrokein pages 4-4, alavi2024arterialstrokein pages 1-2). | “CNS vasculopathy in 3.16% (8/253) of SS patients, with moyamoya disease (MMD) comprising 1.97% of cases” (alavi2024arterialstrokein pages 4-4) | Alavi 2024, *Clinical Case Reports* | DOI: 10.1002/ccr3.8871; https://doi.org/10.1002/ccr3.8871 |
| Management / treatment | No disease-specific curative therapy is established; management is **supportive**, including developmental intervention, nutrition/growth monitoring, family counseling, and physiotherapy. A real-world PNF/Kabat rehab case (20 sessions over 10 weeks) improved **SPPB 4→8**, **TUG 28.0→19.9 s**, and grip strength by **23.4% (right)** and **27.4% (left)**, though ADLs did not significantly improve. In the 2024 pediatric stroke case, **aspirin 5 mg/kg** was used when revascularization was not performed (souza2022seckelsyndromecase pages 2-4, souza2022seckelsyndromecase pages 11-12, kelana2023caseofseckel pages 4-5, alavi2024arterialstrokein pages 3-4). | “There is no specific treatment” (kelana2023caseofseckel pages 1-2); “the plan was to continue aspirin to reduce recurrent stroke risk” (alavi2024arterialstrokein pages 4-5) | Souza 2022, *Research, Society and Development*; Kelana 2023, *OAMJMS*; Alavi 2024, *Clinical Case Reports* | DOI: 10.33448/rsd-v11i2.25080; https://doi.org/10.33448/rsd-v11i2.25080 ; DOI: 10.3889/oamjms.2023.10988; https://doi.org/10.3889/oamjms.2023.10988 ; DOI: 10.1002/ccr3.8871; https://doi.org/10.1002/ccr3.8871 |
| Trials / registries | **NCT03139903**: completed French multicenter observational study, **30 participants**, designed to define morphological/epidemiologic parameters and identify new symptoms; included **cerebral angio-MRI**, specialty assessments, cognitive testing, and supportive-care planning. **NCT04569149**: recruiting **Primordial Dwarfism Registry**, target **~200**, chart-review based, collecting longitudinal specialist notes, surgery reports, labs, genetic testing, and imaging to define natural history/risk factors and improve care/QoL (NCT03139903 chunk 1, NCT04569149 chunk 1). | “Primary objective/outcome: to visualize any vascular abnormalities via cerebral angiography‑MRI” (NCT03139903 chunk 1); “support preventative treatments and improved quality of life” (NCT04569149 chunk 1) | ClinicalTrials.gov NCT03139903; ClinicalTrials.gov NCT04569149 | https://clinicaltrials.gov/study/NCT03139903 ; https://clinicaltrials.gov/study/NCT04569149 |


*Table: This table summarizes high-yield, citation-backed facts on Seckel syndrome for knowledge-base use, including identifiers, genetics, mechanisms, diagnostics, complications, management, and relevant observational studies/registries.*

---

## Key evidence gaps (for knowledge-base completeness)
Within the retrieved corpus, ICD-10/ICD-11 codes, MONDO ID, canonical MeSH descriptor ID, robust penetrance/expressivity estimates by gene, and population allele frequencies (gnomAD) were not available; these would require direct querying of OMIM/Orphanet/MeSH/MONDO/ClinVar/gnomAD or dedicated GeneReviews text beyond the excerpts captured here.


References

1. (farcy2023geneticprimarymicrocephalies pages 2-4): Sarah Farcy, Hassina Hachour, Nadia Bahi-Buisson, and Sandrine Passemard. Genetic primary microcephalies: when centrosome dysfunction dictates brain and body size. Cells, 12:1807, Jul 2023. URL: https://doi.org/10.3390/cells12131807, doi:10.3390/cells12131807. This article has 26 citations.

2. (zhang2023twonovelvariants pages 1-2): Li Zhang, Yanling Teng, Haoran Hu, Huimin Zhu, Juan Wen, Desheng Liang, Zhuo Li, and Lingqian Wu. Two novel variants in cep152 caused seckel syndrome 5 in a chinese family. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2022.1052915, doi:10.3389/fgene.2022.1052915. This article has 2 citations and is from a peer-reviewed journal.

3. (mcintyre2012disruptionofmouse pages 1-2): Rebecca E. McIntyre, Pavithra Lakshminarasimhan Chavali, Ozama Ismail, Damian M. Carragher, Gabriela Sanchez-Andrade, Josep V. Forment, Beiyuan Fu, Martin Del Castillo Velasco-Herrera, Andrew Edwards, Louise van der Weyden, Fengtang Yang, Ramiro Ramirez-Solis, Jeanne Estabel, Ferdia A. Gallagher, Darren W. Logan, Mark J. Arends, Stephen H. Tsang, Vinit B. Mahajan, Cheryl L. Scudamore, Jacqueline K. White, Stephen P. Jackson, Fanni Gergely, and David J. Adams. Disruption of mouse cenpj, a regulator of centriole biogenesis, phenocopies seckel syndrome. PLoS Genetics, 8:e1003022, Nov 2012. URL: https://doi.org/10.1371/journal.pgen.1003022, doi:10.1371/journal.pgen.1003022. This article has 109 citations and is from a domain leading peer-reviewed journal.

4. (kelana2023caseofseckel pages 1-2): Andreas Dhymas Dhyna Martha Kelana, Gusti Ayu Trisna Windiani, Made Arimbawa, Gusti Agung Ngurah Sugitha Adnyana, Made Darma Yuda, Ni Luh Sukma Pratiwi Murti, and Soetjiningsih Soetjiningsih. Case of seckel syndrome in a 9-month-old girl. Open Access Macedonian Journal of Medical Sciences, 11:6-10, Jan 2023. URL: https://doi.org/10.3889/oamjms.2023.10988, doi:10.3889/oamjms.2023.10988. This article has 0 citations.

5. (mudassir2023microcephalyshortstature pages 1-2): Behjat Ul Mudassir and Zehra Agha. Microcephaly, short stature, intellectual disability, speech absence and cataract are associated with novel bi-allelic missense variant in rttn gene: a seckel syndrome case report. Children, 10:1027, Jun 2023. URL: https://doi.org/10.3390/children10061027, doi:10.3390/children10061027. This article has 10 citations.

6. (alavi2024arterialstrokein pages 3-4): Samin Alavi, Mitra Khalili, Paniz Mirmoghaddam, Sharareh Kamfar, and Negar Shams. Arterial stroke in a child with seckel syndrome with a pattern of non‐moyamoya vasculopathy. Clinical Case Reports, May 2024. URL: https://doi.org/10.1002/ccr3.8871, doi:10.1002/ccr3.8871. This article has 1 citations.

7. (jentcy2021seckelsyndrome pages 1-1): M Jentcy and VV Vanniaperumal. Seckel syndrome. Definitions, Feb 2021. URL: https://doi.org/10.32388/9utnhs, doi:10.32388/9utnhs. This article has 0 citations.

8. (NCT03139903 chunk 1):  The Primordial Dwarfisms: Diagnosis, Identification of the Molecular Basis of Seckel Syndrome and Microcephalic Osteodysplastic Primordial Dwarfism Type II. Assistance Publique - Hôpitaux de Paris. 2010. ClinicalTrials.gov Identifier: NCT03139903

9. (jurca2024clinicalchallengesin pages 1-2): Alexandru Daniel Jurca, Codruța Diana Petchesi, Sânziana Jurca, Emilia Severin, Aurora Alexandra Jurca, and Claudia Maria Jurca. Clinical challenges in diagnosing primordial dwarfism: insights from a mopd ii case study. Medicina, 60:1906, Nov 2024. URL: https://doi.org/10.3390/medicina60111906, doi:10.3390/medicina60111906. This article has 4 citations.

10. (zhang2023twonovelvariants pages 8-8): Li Zhang, Yanling Teng, Haoran Hu, Huimin Zhu, Juan Wen, Desheng Liang, Zhuo Li, and Lingqian Wu. Two novel variants in cep152 caused seckel syndrome 5 in a chinese family. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2022.1052915, doi:10.3389/fgene.2022.1052915. This article has 2 citations and is from a peer-reviewed journal.

11. (jurca2024clinicalchallengesin pages 4-6): Alexandru Daniel Jurca, Codruța Diana Petchesi, Sânziana Jurca, Emilia Severin, Aurora Alexandra Jurca, and Claudia Maria Jurca. Clinical challenges in diagnosing primordial dwarfism: insights from a mopd ii case study. Medicina, 60:1906, Nov 2024. URL: https://doi.org/10.3390/medicina60111906, doi:10.3390/medicina60111906. This article has 4 citations.

12. (alavi2024arterialstrokein pages 2-3): Samin Alavi, Mitra Khalili, Paniz Mirmoghaddam, Sharareh Kamfar, and Negar Shams. Arterial stroke in a child with seckel syndrome with a pattern of non‐moyamoya vasculopathy. Clinical Case Reports, May 2024. URL: https://doi.org/10.1002/ccr3.8871, doi:10.1002/ccr3.8871. This article has 1 citations.

13. (alavi2024arterialstrokein pages 4-4): Samin Alavi, Mitra Khalili, Paniz Mirmoghaddam, Sharareh Kamfar, and Negar Shams. Arterial stroke in a child with seckel syndrome with a pattern of non‐moyamoya vasculopathy. Clinical Case Reports, May 2024. URL: https://doi.org/10.1002/ccr3.8871, doi:10.1002/ccr3.8871. This article has 1 citations.

14. (souza2022seckelsyndromecase pages 8-11): Jeferson de Lima Souza, Miburge Bolivar Gois Júnior, Diogo Costa Garção, Elenilton Correia de Souza, Isaac Rafael Silva Lima, and Olga Sueli Marques Moreira. Seckel syndrome: case report of functional motor recovery using proprioceptive neuromuscular facilitation/kabat method. Research, Society and Development, 11:e37111225080, Jan 2022. URL: https://doi.org/10.33448/rsd-v11i2.25080, doi:10.33448/rsd-v11i2.25080. This article has 0 citations.

15. (souza2022seckelsyndromecase pages 11-12): Jeferson de Lima Souza, Miburge Bolivar Gois Júnior, Diogo Costa Garção, Elenilton Correia de Souza, Isaac Rafael Silva Lima, and Olga Sueli Marques Moreira. Seckel syndrome: case report of functional motor recovery using proprioceptive neuromuscular facilitation/kabat method. Research, Society and Development, 11:e37111225080, Jan 2022. URL: https://doi.org/10.33448/rsd-v11i2.25080, doi:10.33448/rsd-v11i2.25080. This article has 0 citations.

16. (patrick2017atrisa pages 58-61): Patrick Lang. Atr is a novel therapeutic target for medulloblastoma identified by its role in cerebellar development. Text, 2017. URL: https://doi.org/10.17615/zwrt-bm16, doi:10.17615/zwrt-bm16. This article has 0 citations and is from a peer-reviewed journal.

17. (mcintyre2012disruptionofmouse pages 6-8): Rebecca E. McIntyre, Pavithra Lakshminarasimhan Chavali, Ozama Ismail, Damian M. Carragher, Gabriela Sanchez-Andrade, Josep V. Forment, Beiyuan Fu, Martin Del Castillo Velasco-Herrera, Andrew Edwards, Louise van der Weyden, Fengtang Yang, Ramiro Ramirez-Solis, Jeanne Estabel, Ferdia A. Gallagher, Darren W. Logan, Mark J. Arends, Stephen H. Tsang, Vinit B. Mahajan, Cheryl L. Scudamore, Jacqueline K. White, Stephen P. Jackson, Fanni Gergely, and David J. Adams. Disruption of mouse cenpj, a regulator of centriole biogenesis, phenocopies seckel syndrome. PLoS Genetics, 8:e1003022, Nov 2012. URL: https://doi.org/10.1371/journal.pgen.1003022, doi:10.1371/journal.pgen.1003022. This article has 109 citations and is from a domain leading peer-reviewed journal.

18. (farcy2023geneticprimarymicrocephalies media eb9668c0): Sarah Farcy, Hassina Hachour, Nadia Bahi-Buisson, and Sandrine Passemard. Genetic primary microcephalies: when centrosome dysfunction dictates brain and body size. Cells, 12:1807, Jul 2023. URL: https://doi.org/10.3390/cells12131807, doi:10.3390/cells12131807. This article has 26 citations.

19. (farcy2023geneticprimarymicrocephalies media 1a99a141): Sarah Farcy, Hassina Hachour, Nadia Bahi-Buisson, and Sandrine Passemard. Genetic primary microcephalies: when centrosome dysfunction dictates brain and body size. Cells, 12:1807, Jul 2023. URL: https://doi.org/10.3390/cells12131807, doi:10.3390/cells12131807. This article has 26 citations.

20. (farcy2023geneticprimarymicrocephalies media 0b042e40): Sarah Farcy, Hassina Hachour, Nadia Bahi-Buisson, and Sandrine Passemard. Genetic primary microcephalies: when centrosome dysfunction dictates brain and body size. Cells, 12:1807, Jul 2023. URL: https://doi.org/10.3390/cells12131807, doi:10.3390/cells12131807. This article has 26 citations.

21. (farcy2023geneticprimarymicrocephalies media c608a08c): Sarah Farcy, Hassina Hachour, Nadia Bahi-Buisson, and Sandrine Passemard. Genetic primary microcephalies: when centrosome dysfunction dictates brain and body size. Cells, 12:1807, Jul 2023. URL: https://doi.org/10.3390/cells12131807, doi:10.3390/cells12131807. This article has 26 citations.

22. (alavi2024arterialstrokein pages 1-2): Samin Alavi, Mitra Khalili, Paniz Mirmoghaddam, Sharareh Kamfar, and Negar Shams. Arterial stroke in a child with seckel syndrome with a pattern of non‐moyamoya vasculopathy. Clinical Case Reports, May 2024. URL: https://doi.org/10.1002/ccr3.8871, doi:10.1002/ccr3.8871. This article has 1 citations.

23. (souza2022seckelsyndromecase pages 2-4): Jeferson de Lima Souza, Miburge Bolivar Gois Júnior, Diogo Costa Garção, Elenilton Correia de Souza, Isaac Rafael Silva Lima, and Olga Sueli Marques Moreira. Seckel syndrome: case report of functional motor recovery using proprioceptive neuromuscular facilitation/kabat method. Research, Society and Development, 11:e37111225080, Jan 2022. URL: https://doi.org/10.33448/rsd-v11i2.25080, doi:10.33448/rsd-v11i2.25080. This article has 0 citations.

24. (alkuraya2015primordialdwarfisman pages 1-2): Fowzan S. Alkuraya. Primordial dwarfism: an update. Current Opinion in Endocrinology & Diabetes and Obesity, 22:55–64, Feb 2015. URL: https://doi.org/10.1097/med.0000000000000121, doi:10.1097/med.0000000000000121. This article has 25 citations.

25. (alavi2024arterialstrokein pages 4-5): Samin Alavi, Mitra Khalili, Paniz Mirmoghaddam, Sharareh Kamfar, and Negar Shams. Arterial stroke in a child with seckel syndrome with a pattern of non‐moyamoya vasculopathy. Clinical Case Reports, May 2024. URL: https://doi.org/10.1002/ccr3.8871, doi:10.1002/ccr3.8871. This article has 1 citations.

26. (kelana2023caseofseckel pages 4-5): Andreas Dhymas Dhyna Martha Kelana, Gusti Ayu Trisna Windiani, Made Arimbawa, Gusti Agung Ngurah Sugitha Adnyana, Made Darma Yuda, Ni Luh Sukma Pratiwi Murti, and Soetjiningsih Soetjiningsih. Case of seckel syndrome in a 9-month-old girl. Open Access Macedonian Journal of Medical Sciences, 11:6-10, Jan 2023. URL: https://doi.org/10.3889/oamjms.2023.10988, doi:10.3889/oamjms.2023.10988. This article has 0 citations.

27. (NCT04569149 chunk 1): Angela Duker. Primordial Dwarfism Registry. Nemours Children's Clinic. 2008. ClinicalTrials.gov Identifier: NCT04569149
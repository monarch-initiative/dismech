---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T08:36:57.549609'
end_time: '2026-05-08T08:50:57.133618'
duration_seconds: 839.58
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alzheimer Disease
  mondo_id: ''
  category: Neurodegenerative Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alzheimer Disease
- **MONDO ID:**  (if available)
- **Category:** Neurodegenerative Disorder

## Research Objectives

Please provide a comprehensive research report on **Alzheimer Disease** covering all of the
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
- **Disease Name:** Alzheimer Disease
- **MONDO ID:**  (if available)
- **Category:** Neurodegenerative Disorder

## Research Objectives

Please provide a comprehensive research report on **Alzheimer Disease** covering all of the
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


# Alzheimer Disease (AD) — Comprehensive Disease Characteristics Research Report (2023–2024 emphasis)

## Executive summary
Alzheimer disease (AD) is increasingly framed as a **biologically defined** neurodegenerative disease characterized by **amyloid-β (Aβ) plaque** pathology and **phosphorylated tau (p-tau) neurofibrillary tangle** pathology, with neurodegeneration and clinical syndromes (e.g., mild cognitive impairment and dementia) occurring variably along this continuum. The most influential 2024 development is the **Alzheimer’s Association (AA) Workgroup revised criteria** proposing that an abnormal “Core 1” biomarker (amyloid PET, approved CSF assays, or sufficiently accurate plasma assays) can be sufficient to establish a biological diagnosis of AD, enabling treatment selection and staging across symptomatic and asymptomatic phases. (jack2024revisedcriteriafor pages 1-2)

A major applied 2023–2024 trend is the rapid maturation of **blood-based biomarkers (BBMs)**, especially **plasma p-tau217**, with multiple studies reporting **AUCs ≈0.9 or higher** for detecting AD-related Aβ pathology and workflows that may reduce invasive testing in specialist memory services. (dyer2024performanceofplasma pages 10-11, niimi2024combiningplasmaaβ pages 7-8)

## High-value recent sources (quick reference)
| Topic | Source (first author, journal) | Publication date (month year) | URL/DOI | Key quantitative finding(s) extracted from evidence | Evidence type (human clinical / cohort / guideline / omics) |
|---|---|---|---|---|---|
| Biological definition and staging criteria for AD | Jack et al., *Alzheimer's & Dementia* | June 2024 | https://doi.org/10.1002/alz.13859 | 2024 AA workgroup defines AD biologically; an abnormal Core 1 biomarker can establish AD. For standalone plasma use, Core 1 blood biomarkers should achieve **≥90% accuracy** versus amyloid PET. Florbetapir PET visual reads showed **96% sensitivity / 100% specificity** versus CERAD neuritic plaque reference; approved CSF assays showed about **88%/93%** and **85%/94%** sensitivity/specificity versus amyloid PET visual reads. Neuropathology concordance: among symptomatic individuals with moderate/frequent plaques, **4390/4637 (95%)** were Braak III–VI; among cognitively unimpaired decedents with moderate/frequent plaques, **107/123 (87%)** were Braak III–VI; in a larger NACC sample, **186/252 (74%)** were Braak III–VI and **226/252 (91%)** were Braak II–VI (jack2024revisedcriteriafor pages 8-9, jack2024revisedcriteriafor pages 1-2) | Guideline |
| Plasma p-tau217 in real-world memory clinic diagnosis | Dyer et al., *Alzheimer's Research & Therapy* | August 2024 | https://doi.org/10.1186/s13195-024-01555-z | In a symptomatic memory-clinic cohort, plasma p-tau217 detected Aβ pathology with **AUC 0.91** and outperformed plasma p-tau181 (**AUC 0.73**). A two-threshold strategy suggested confirmatory lumbar puncture could potentially be avoided in **68%** of cases at **95% sensitivity / 95% specificity**, or **58%** at **97.5% / 97.5%** (dyer2024performanceofplasma pages 10-11) | Human clinical / cohort |
| Combined plasma Aβ and p-tau217 models for Aβ-PET prediction | Niimi et al., *Alzheimer's Research & Therapy* | May 2024 | https://doi.org/10.1186/s13195-024-01469-w | In non-demented Japanese J-TRC participants, the best total-cohort model reached **AUC 0.936** for **p-tau217/Aβ42 + APOE + age + sex**; in **CDR 0** the best model reached **AUC 0.948** for **p-tau217 + Aβ42/40 + APOE + age + sex**; in **CDR 0.5** the best model reached **AUC 0.955** for **p-tau217/Aβ42 + APOE + age + sex**. Individual p-tau217 AUCs were **0.913** (total), **0.889** (CDR 0), and **0.925** (CDR 0.5) (niimi2024combiningplasmaaβ pages 7-8) | Cohort |
| Variant-aware single-nucleus transcriptomics in AD | Brase et al., *Nature Communications* | April 2023 | https://doi.org/10.1038/s41467-023-37437-5 | snRNA-seq of nearly **300,000 nuclei** from parietal cortex of autosomal-dominant AD and risk-variant carriers identified variant-specific cell states: **TREM2 oligodendrocytes** showed dysregulated **autophagy-lysosomal** pathways; **MS4A microglia** showed dysregulated **complement cascade** genes; **APOE ε4 inhibitory neurons** showed signatures of **ferroptosis**. The paper also reports dose-dependent enrichment of an **MS4A rs1582763-A** pro-inflammatory microglial state and astrocyte activation trends in carriers (brase2023singlenucleusrnasequencingof pages 7-8) | Omics |
| Modifiable risk factors and prevention potential | Parums, *Medical Science Monitor* | May 2024 | https://doi.org/10.12659/msm.945091 | Summarizing Lancet Commission prevention evidence, the review states **12 modifiable risk factors** (education, hypertension, hearing impairment, obesity, smoking, depression, physical inactivity, social isolation, diabetes, alcohol, traumatic brain injury, air pollution) may account for **up to 40%** of dementia cases worldwide (parums2024areviewof pages 4-6) | Review / public health synthesis |
| Real-world implementation of anti-amyloid therapy | Jessen et al., *Journal of Prevention of Alzheimer's Disease* | October 2024 | https://doi.org/10.14283/jpad.2024.153 | EADC position statement argues anti-amyloid antibodies have meaningful though modest effects and manageable adverse effects, and recommends clinical use in **selected patients with treatment documentation in registries**. It emphasizes that the number eventually treated will be only a **fraction of all early AD patients** because of narrow eligibility and access barriers; cited meta-analysis estimate indicates **40%** of dementia population-attributable risk relates to modifiable factors (jessen2024progressinthe pages 1-2) | Guideline / expert consensus |


*Table: This table compiles high-yield 2023–2024 Alzheimer disease sources with the most decision-relevant quantitative findings for diagnosis, biomarkers, omics, prevention, and implementation. It is useful as a quick-reference evidence map for a disease knowledge base.*

---

## 1. Disease information
### 1.1 Concise overview
The AA Workgroup (2024) defines AD as beginning with **AD neuropathologic change (ADNPC)** and emphasizes that AD pathology can be present **before symptoms**. The Workgroup’s intent is to provide **objective diagnostic and staging criteria** that bridge research and clinical care (not step-by-step clinical workflow protocols). (jack2024revisedcriteriafor pages 1-2)

### 1.2 Key identifiers and ontology codes
* **MONDO ID:** Open Targets lists **MONDO_0004975** for Alzheimer disease. (OpenTargets Search: Alzheimer disease)
* **Other identifiers (ICD-10/ICD-11/MeSH/OMIM/Orphanet):** Not extracted from the retrieved primary sources in this run; should be populated from OMIM/MeSH/ICD registries directly.

### 1.3 Common synonyms / alternative names
Within the retrieved sources, AD is discussed both as a **clinical syndrome** (e.g., mild dementia) and as **“biological AD”** defined by biomarkers/pathology. (jack2024revisedcriteriafor pages 1-2, jessen2024progressinthe pages 1-2)

### 1.4 Evidence source type
The evidence in this report is derived from:
* **Aggregated disease-level resources and consensus criteria** (AA Workgroup). (jack2024revisedcriteriafor pages 1-2)
* **Human observational cohorts** and real-world memory clinic studies for plasma biomarkers. (dyer2024performanceofplasma pages 10-11, niimi2024combiningplasmaaβ pages 7-8)
* **Human multi-omic / single-nucleus transcriptomics** in postmortem brain. (brase2023singlenucleusrnasequencingof pages 7-8)
* **Expert position statements / reviews** for implementation and prevention. (jessen2024progressinthe pages 1-2, parums2024areviewof pages 4-6)

---

## 2. Etiology
### 2.1 Disease causal factors (current understanding)
**Biological drivers** emphasized across authoritative sources include Aβ deposition and tau aggregation. The EADC investigators summarize AD biologically as extracellular **β-amyloid plaques** plus intraneuronal **phosphorylated tau** with ensuing neurodegeneration, detectable by CSF and PET biomarkers (often already at the MCI stage). (jessen2024progressinthe pages 1-2)

### 2.2 Genetic risk factors (selected; recent mechanistic emphasis)
The 2023 single-nucleus atlas of autosomal dominant AD and risk-variant carriers highlights that AD genetic architecture maps to **cell-type–specific transcriptional states** and pathways (microglia, astrocytes, oligodendrocytes, neurons), supporting a view that genetic risk influences AD through **neuroimmune, lysosomal/autophagy, complement, and neuronal stress-death programs**. (brase2023singlenucleusrnasequencingof pages 7-8)

**Ontology suggestions (genes):** APP, PSEN1, PSEN2, APOE, TREM2, MS4A locus genes (HGNC symbols).

### 2.3 Protective factors
The centenarian resilience study was retrieved but the extractable quantitative protective-allele statistics were not captured in the evidence snippets returned by the tools in this run; this remains a gap for this report’s citation-backed content.

### 2.4 Gene–environment interactions
Not directly quantified in the retrieved evidence.

---

## 3. Phenotypes
### 3.1 Core clinical phenotypes (high-level)
The clinical syndrome is described in the retrieved literature as **progressive cognitive decline** with functional impairment, and trials/biomarker studies commonly focus on early symptomatic phases (MCI/mild dementia). (dyer2024performanceofplasma pages 10-11, jessen2024progressinthe pages 1-2, niimi2024combiningplasmaaβ pages 7-8)

### 3.2 HPO term suggestions (non-exhaustive; for knowledge base structuring)
* Memory impairment: **HP:0002354**
* Cognitive impairment: **HP:0100543**
* Dementia: **HP:0000726**
* Executive dysfunction: **HP:0000726** (or more specific executive-function terms as needed)

**Frequency/severity/progression statistics:** Not systematically extracted from primary clinical phenotype cohorts in the current evidence set.

---

## 4. Genetic / molecular information
### 4.1 Molecular hallmarks
AD’s defining lesions include Aβ plaques and tau pathology; the AA Workgroup uses biomarker mapping to these lesions to define biological AD. (jack2024revisedcriteriafor pages 1-2)

### 4.2 Pathogenic variants and variant classes
Pathogenic-variant details (specific amino-acid changes, allele frequencies, ClinVar classifications) were not captured in the available evidence. Open Targets lists major AD-associated targets (e.g., APP, PSEN1, PSEN2, APOE, SORL1) but does not provide variant-level detail in the retrieved snapshot. (OpenTargets Search: Alzheimer disease)

### 4.3 Epigenetic information and chromosomal abnormalities
Not extracted in the retrieved evidence.

---

## 5. Environmental information
### 5.1 Lifestyle and environmental risk factors (modifiable)
A prevention-oriented synthesis reports the 2020 Lancet Commission’s **12 modifiable risk factors** (education, hypertension, hearing impairment, obesity, smoking, depression, physical inactivity, social isolation, diabetes, alcohol, traumatic brain injury, air pollution) and states these can account for **up to ~40% of dementia cases worldwide**. (parums2024areviewof pages 4-6)

**CHEBI suggestions (exposures):** nitrogen dioxide (NO2), ethanol.

### 5.2 Infectious agents
No evidence in retrieved sources supporting a specific infectious etiology for typical AD.

---

## 6. Mechanism / pathophysiology
### 6.1 Updated causal chain (biomarker-informed)
The AA Workgroup positions AD as starting with **ADNPC** (biological disease), detectable by **Core 1 biomarkers**, with later biomarkers providing prognostic staging and increasing confidence that AD pathology contributes to symptoms. (jack2024revisedcriteriafor pages 1-2)

**Core 1 biomarkers include** amyloid PET, approved CSF biomarkers, and sufficiently accurate plasma biomarkers (notably plasma p-tau217 in some assays). (jack2024revisedcriteriafor pages 1-2)

### 6.2 Microglia/astrocyte/neuron/oligodendrocyte programs (single-nucleus evidence)
In a large snRNA-seq study of autosomal dominant AD and risk-variant carriers, variant-specific states were reported, including:
* **TREM2 oligodendrocytes** with dysregulated **autophagy–lysosomal** pathway.
* **MS4A microglia** with dysregulated **complement cascade** genes.
* **APOE ε4 inhibitory neurons** showing signatures consistent with **ferroptosis**.
These findings support a multi-cell-type mechanistic model in which glial activation states and neuronal stress-death programs interact with genetic risk architecture. (brase2023singlenucleusrnasequencingof pages 7-8)

### 6.3 Pathways / ontology suggestions
**GO Biological Process (examples):**
* Amyloid-beta metabolic process
* Tau protein binding / tau protein phosphorylation (as appropriate)
* Microglial phagocytosis
* Complement activation
* Autophagy / lysosome organization
* Ferroptosis

**Cell Ontology (CL) suggestions:**
* Microglial cell
* Astrocyte
* Oligodendrocyte
* Cortical inhibitory neuron

**GO Cellular Component suggestions:**
* Lysosome
* Endosome
* Synapse
* Mitochondrion

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
Primary system: **central nervous system**. Biomarker and transcriptomic studies emphasize cortical involvement (e.g., parietal cortex; dorsolateral prefrontal cortex resources and repositories are referenced in omics work). (brase2023singlenucleusrnasequencingof pages 7-8, green2024cellularcommunitiesreveal pages 1-2)

### 7.2 UBERON suggestions
* Brain (UBERON:0000955)
* Cerebral cortex (UBERON:0000956)

---

## 8. Temporal development
The AA Workgroup explicitly incorporates **asymptomatic biological AD** and proposes an integrated biological–clinical staging approach across the continuum. (jack2024revisedcriteriafor pages 1-2)

Blood biomarkers are being positioned to enable earlier detection and staging—e.g., plasma biomarker performance for detecting brain Aβ pathology in non-demented cohorts. (niimi2024combiningplasmaaβ pages 7-8)

---

## 9. Inheritance and population
### 9.1 Epidemiology
This run did not retrieve a primary global epidemiology paper with prevalence/incidence rates for AD specifically; therefore, numeric prevalence/incidence statements are not provided here.

### 9.2 Genetic architecture / inheritance patterns
The retrieved omics study includes **autosomal dominant** AD carriers and late-onset risk-variant carriers, consistent with AD’s mixed architecture (rare Mendelian forms plus common polygenic susceptibility). (brase2023singlenucleusrnasequencingof pages 7-8)

---

## 10. Diagnostics
### 10.1 AA Workgroup revised diagnostic and staging criteria (2024)
Key definitions and performance anchors include:
* AD can be defined biologically; ADNPC can exist without symptoms. (jack2024revisedcriteriafor pages 1-2)
* **Core 1 biomarkers** (amyloid PET, approved CSF, accurate plasma biomarkers) are intended to map to plaques/tangles and support biological diagnosis. (jack2024revisedcriteriafor pages 1-2)
* **Core 1 plasma benchmark:** the Workgroup proposes **≥90% accuracy vs amyloid PET** for a standalone plasma biomarker used to establish amyloid pathology. (jack2024revisedcriteriafor pages 8-9)
* Example reference performance: florbetapir PET visual reads showed **96% sensitivity / 100% specificity** vs CERAD neuritic plaques; approved CSF assays showed approximately **88%/93%** and **85%/94%** sensitivity/specificity vs amyloid PET visual reads. (jack2024revisedcriteriafor pages 8-9)

### 10.2 Blood biomarkers (2023–2024 emphasis): plasma p-tau217
**Real-world memory clinic performance**: plasma p-tau217 (ECL immunoassay) detected CSF-defined Aβ pathology with **AUC 0.91** and outperformed plasma p-tau181 (**AUC 0.73**). A two-threshold triage approach suggested that confirmatory lumbar puncture might be avoided in **~58–68%** of cases depending on chosen sensitivity/specificity operating points. (dyer2024performanceofplasma pages 10-11)

**Non-demented trial-ready / research cohorts**: combining plasma Aβ measures and p-tau217 can yield AUCs approaching **~0.93–0.95** for predicting abnormal Aβ-PET, with best-performing models depending on clinical stage (CDR 0 vs 0.5) and inclusion of age/sex/APOE. (niimi2024combiningplasmaaβ pages 7-8)

### 10.3 Imaging and CSF biomarkers
The AA Workgroup uses amyloid PET and CSF assays as Core 1 standards and provides reference sensitivity/specificity anchors (see above). (jack2024revisedcriteriafor pages 8-9)

---

## 11. Outcome / prognosis
Evidence in the current retrieved set is insufficient to provide robust, citation-backed survival estimates, stage durations, or validated prognostic models.

---

## 12. Treatment
### 12.1 Current applications and real-world implementation (2023–2024)
Anti-amyloid monoclonal antibodies are described as the first generation of causal (pathology-targeting) therapies but with modest clinical effect sizes, safety/monitoring burdens, and eligibility constraints. The EADC investigators recommend **selected patient use** with **treatment documentation in registries** to inform real-world effectiveness and system readiness. (jessen2024progressinthe pages 1-2)

### 12.2 Safety considerations (ARIA)
A review summarizing aducanumab reports that while amyloid was reduced on PET, there was “no apparent improvement in cognitive function,” and **ARIA occurred in ~40% of high-dose aducanumab-treated patients**. (parums2024areviewof pages 4-6)

### 12.3 MAXO term suggestions
* Anti-amyloid beta immunotherapy (monoclonal antibody therapy)
* Magnetic resonance imaging monitoring
* Lumbar puncture (confirmatory diagnostics)

**Note:** Detailed lecanemab/donanemab trial effect sizes and ARIA rates for those agents were not extractable from the currently captured evidence snippets.

---

## 13. Prevention
The prevention evidence emphasized in retrieved sources is consistent with a substantial preventable fraction of dementia via risk factor modification. A synthesis citing the Lancet Commission reports that a set of modifiable factors can account for **up to ~40%** of dementia cases. (parums2024areviewof pages 4-6)

---

## 14. Other species / natural disease
Not covered in the retrieved evidence.

---

## 15. Model organisms
Not covered in the retrieved evidence.

---

## 16. Notable 2023–2024 developments (concise analysis)
1. **Shift toward biological diagnosis**: 2024 AA criteria explicitly formalize “biological AD” as diagnosable via biomarkers even without symptoms, motivated by the need to select patients for disease-modifying therapies. (jack2024revisedcriteriafor pages 1-2)
2. **Blood-based biomarker operationalization**: Multiple 2024 studies support p-tau217 as a leading BBM with AUCs around 0.9 and plausible clinical triage workflows to reduce lumbar punctures and expand access. (dyer2024performanceofplasma pages 10-11, niimi2024combiningplasmaaβ pages 7-8)
3. **Systems and cell-state view of AD mechanisms**: snRNA-seq studies in 2023–2024 strengthen the view that variant-associated microglial/astrocytic/oligodendroglial/neuron states are central to disease heterogeneity, suggesting multi-target and combination-therapy rationales. (brase2023singlenucleusrnasequencingof pages 7-8)

---

## 17. Evidence gaps / limitations of this report
Despite extensive retrieval, several template-required elements were not available as citation-backed facts in the captured evidence snippets:
* ICD/MeSH/OMIM/Orphanet identifiers (should be filled from authoritative registries).
* Quantitative prevalence/incidence statistics and survival estimates from primary epidemiologic cohorts.
* Comprehensive phenotype frequencies mapped to HPO with percentages.
* Detailed variant nomenclature, allele frequencies, and ClinVar classifications.
* Detailed lecanemab/donanemab trial efficacy/safety metrics (beyond class-level summaries and aducanumab ARIA estimate).

These can be completed by targeted retrieval of (i) epidemiology (GBD dementia/AD-specific tables), (ii) GeneReviews/OMIM/ClinVar summaries for causative variants, and (iii) primary phase 3 trial publications for lecanemab and donanemab.


References

1. (jack2024revisedcriteriafor pages 1-2): Clifford R. Jack, J. Scott Andrews, Thomas G. Beach, Teresa Buracchio, Billy Dunn, Ana Graf, Oskar Hansson, Carole Ho, William Jagust, Eric McDade, Jose Luis Molinuevo, Ozioma C. Okonkwo, Luca Pani, Michael S. Rafii, Philip Scheltens, Eric Siemers, Heather M. Snyder, Reisa Sperling, Charlotte E. Teunissen, and Maria C. Carrillo. Revised criteria for diagnosis and staging of alzheimer's disease: alzheimer's association workgroup. Alzheimer's & Dementia, 20:5143-5169, Jun 2024. URL: https://doi.org/10.1002/alz.13859, doi:10.1002/alz.13859. This article has 2357 citations and is from a highest quality peer-reviewed journal.

2. (dyer2024performanceofplasma pages 10-11): Adam H. Dyer, Helena Dolphin, Antoinette O’Connor, Laura Morrison, Gavin Sedgwick, Conor Young, Emily Killeen, Conal Gallagher, Aoife McFeely, Eimear Connolly, Naomi Davey, Paul Claffey, Paddy Doyle, Shane Lyons, Christine Gaffney, Ruth Ennis, Cathy McHale, Jasmine Joseph, Graham Knight, Emmet Kelly, Cliona O’Farrelly, Aoife Fallon, Sean O’Dowd, Nollaig M. Bourke, and Sean P. Kennelly. Performance of plasma p-tau217 for the detection of amyloid-β positivity in a memory clinic cohort using an electrochemiluminescence immunoassay. Alzheimer's Research & Therapy, Aug 2024. URL: https://doi.org/10.1186/s13195-024-01555-z, doi:10.1186/s13195-024-01555-z. This article has 33 citations and is from a domain leading peer-reviewed journal.

3. (niimi2024combiningplasmaaβ pages 7-8): Yoshiki Niimi, Shorena Janelidze, Kenichiro Sato, Naoki Tomita, Tadashi Tsukamoto, Takashi Kato, Kenji Yoshiyama, Hisatomo Kowa, Atsushi Iwata, Ryoko Ihara, Kazushi Suzuki, Kensaku Kasuga, Takeshi Ikeuchi, Kenji Ishii, Kengo Ito, Akinori Nakamura, Michio Senda, Theresa A. Day, Samantha C. Burnham, Leonardo Iaccarino, Michael J. Pontecorvo, Oskar Hansson, and Takeshi Iwatsubo. Combining plasma aβ and p-tau217 improves detection of brain amyloid in non-demented elderly. Alzheimer's Research & Therapy, May 2024. URL: https://doi.org/10.1186/s13195-024-01469-w, doi:10.1186/s13195-024-01469-w. This article has 68 citations and is from a domain leading peer-reviewed journal.

4. (jack2024revisedcriteriafor pages 8-9): Clifford R. Jack, J. Scott Andrews, Thomas G. Beach, Teresa Buracchio, Billy Dunn, Ana Graf, Oskar Hansson, Carole Ho, William Jagust, Eric McDade, Jose Luis Molinuevo, Ozioma C. Okonkwo, Luca Pani, Michael S. Rafii, Philip Scheltens, Eric Siemers, Heather M. Snyder, Reisa Sperling, Charlotte E. Teunissen, and Maria C. Carrillo. Revised criteria for diagnosis and staging of alzheimer's disease: alzheimer's association workgroup. Alzheimer's & Dementia, 20:5143-5169, Jun 2024. URL: https://doi.org/10.1002/alz.13859, doi:10.1002/alz.13859. This article has 2357 citations and is from a highest quality peer-reviewed journal.

5. (brase2023singlenucleusrnasequencingof pages 7-8): Logan Brase, Shih-Feng You, Ricardo D’Oliveira Albanus, Jorge L. Del-Aguila, Yaoyi Dai, Brenna C. Novotny, Carolina Soriano-Tarraga, Taitea Dykstra, Maria Victoria Fernandez, John P. Budde, Kristy Bergmann, John C. Morris, Randall J. Bateman, Richard J. Perrin, Eric McDade, Chengjie Xiong, Alison M. Goate, Martin Farlow, Greg T. Sutherland, Jonathan Kipnis, Celeste M. Karch, Bruno A. Benitez, and Oscar Harari. Single-nucleus rna-sequencing of autosomal dominant alzheimer disease and risk variant carriers. Nature Communications, Apr 2023. URL: https://doi.org/10.1038/s41467-023-37437-5, doi:10.1038/s41467-023-37437-5. This article has 95 citations and is from a highest quality peer-reviewed journal.

6. (parums2024areviewof pages 4-6): Dinah V. Parums. A review of the current status of disease-modifying therapies and prevention of alzheimer’s disease. Medical Science Monitor, 30:e945091-1-e945091-7, May 2024. URL: https://doi.org/10.12659/msm.945091, doi:10.12659/msm.945091. This article has 39 citations and is from a peer-reviewed journal.

7. (jessen2024progressinthe pages 1-2): Frank Jessen, M.G. Kramberger, D. Angioni, D. Aarsland, M. Balasa, K. Bennys, M. Boada, M. Boban, A. Chincarini, L. Exalto, A. Felbecker, K. Fliessbach, G.B. Frisoni, A.J. Garza-Martínez, T. Grimmer, B. Hanseeuw, J. Hort, A. Ivanoiu, S. Klöppel, L. Krajcovicova, B. McGuinness, P. Mecocci, A. de Mendonca, A. Nous, P.-J. Ousset, C. Paquet, R. Perneczky, O. Peters, M. Tabuas-Pereira, F. Piazza, D. Plantone, M. Riverol, A. Ruiz, G. Sacco, I. Santana, N. Scarmeas, E. Solje, E. Stefanova, S. Sutovsky, W. van der Flier, T. Welsh, A. Wimo, B. Winblad, L. Frölich, and S. Engelborghs. Progress in the treatment of alzheimer's disease is needed – position statement of european alzheimer's disease consortium (eadc) investigators. The Journal of Prevention of Alzheimer's Disease, 11:1212-1218, Oct 2024. URL: https://doi.org/10.14283/jpad.2024.153, doi:10.14283/jpad.2024.153. This article has 23 citations and is from a peer-reviewed journal.

8. (OpenTargets Search: Alzheimer disease): Open Targets Query (Alzheimer disease, 39 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

9. (green2024cellularcommunitiesreveal pages 1-2): Gilad Sahar Green, Masashi Fujita, Hyun-Sik Yang, Mariko Taga, Anael Cain, Cristin McCabe, Natacha Comandante-Lou, Charles C. White, Anna K. Schmidtner, Lu Zeng, Alina Sigalov, Yangling Wang, Aviv Regev, Hans-Ulrich Klein, Vilas Menon, David A. Bennett, Naomi Habib, and Philip L. De Jager. Cellular communities reveal trajectories of brain ageing and alzheimer's disease. Nature, 633:634-645, Aug 2024. URL: https://doi.org/10.1038/s41586-024-07871-6, doi:10.1038/s41586-024-07871-6. This article has 177 citations and is from a highest quality peer-reviewed journal.

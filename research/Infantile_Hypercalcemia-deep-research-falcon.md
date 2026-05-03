---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-03T02:14:08.171092'
end_time: '2026-05-03T02:20:19.413698'
duration_seconds: 371.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Infantile Hypercalcemia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infantile Hypercalcemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile Hypercalcemia** covering all of the
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
- **Disease Name:** Infantile Hypercalcemia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile Hypercalcemia** covering all of the
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


# Infantile Hypercalcemia (Idiopathic Infantile Hypercalcemia, IIH): Disease Characteristics Research Report

## Executive summary
Infantile hypercalcemia (also called idiopathic infantile hypercalcemia, IIH) is a rare genetic disorder classically presenting in infancy with parathyroid hormone (PTH)-independent hypercalcemia, hypercalciuria, and nephrocalcinosis; it is most often caused by defects in vitamin D catabolism (CYP24A1; “infantile hypercalcemia type 1”) or renal phosphate handling (SLC34A1; “infantile hypercalcemia type 2”). (wang2024biallelicandmonoallelic pages 1-2, bizereamoga2023phenotypeofidiopathic pages 1-2)

Recent (2023–2024) literature emphasizes: (i) broader genotype–phenotype spectra including symptomatic monoallelic carriers; (ii) the utility of next-generation sequencing (NGS) for diagnosis; (iii) antenatal presentations in SLC34A1-related disease; and (iv) the need for long-term renal surveillance because chronic kidney disease (CKD) can develop in survivors. (wang2024biallelicandmonoallelic pages 1-2, khan2023acaseof pages 2-4, verjans2024antenatalpresentationand pages 6-9)

---

## 1. Disease information

### 1.1 Definition and overview
Idiopathic infantile hypercalcemia (IIH) is described as a “rare disorder of PTH-independent hypercalcemia.” (wang2024biallelicandmonoallelic pages 1-2)

A 2023 review/case series explicitly states: “Idiopathic infantile hypercalcemia (IIH) is a rare genetic disease, also called hypersensitivity to vitamin D3.” (bizereamoga2023phenotypeofidiopathic pages 1-2)

Clinically, IIH is classically characterized by hypercalcemia with suppressed PTH and associated renal and systemic manifestations such as hypercalciuria and nephrocalcinosis, often accompanied by nonspecific infant symptoms (poor feeding, vomiting, failure to thrive, dehydration). (bizereamoga2023phenotypeofidiopathic pages 1-2, khan2023acaseof pages 2-4)

**Evidence source type:** aggregated disease-level resources and case series/reviews, plus individual case reports and cohorts. (wang2024biallelicandmonoallelic pages 1-2, bizereamoga2023phenotypeofidiopathic pages 1-2, khan2023acaseof pages 2-4)

### 1.2 Key identifiers and synonyms
**Synonyms/aliases used in recent literature** include: infantile hypercalcemia / infantile hypercalcaemia, idiopathic infantile hypercalcemia (IIH), hypersensitivity to vitamin D3, infantile hypercalcemia type 1 / type 2, IIH type 1 / IIH type 2, and HCINF1 (for type 1). (bizereamoga2023phenotypeofidiopathic pages 1-2, janiec2021longtermoutcomeof pages 1-2)

**OMIM identifiers (supported by primary literature):**
- **Infantile hypercalcemia type 1 (CYP24A1-related): OMIM phenotype 143880**; **CYP24A1 OMIM gene *126065**. (janiec2021longtermoutcomeof pages 1-2, cappellani2022hypercalcemiadueto pages 1-2)
- **Infantile hypercalcemia type 2 (SLC34A1-related): OMIM phenotype 616963**; **SLC34A1 OMIM gene *182309**. (janiec2021longtermoutcomeof pages 1-2, bizereamoga2023phenotypeofidiopathic pages 6-7)

**Orphanet / ICD-10/ICD-11 / MeSH / MONDO:** these identifiers were not found in the retrieved full-text evidence set; therefore they cannot be stated with source-backed certainty here. (wang2024biallelicandmonoallelic pages 1-2, janiec2021longtermoutcomeof pages 1-2)

**Artifact (identifiers & synonyms):**
| Entity | Synonyms/aliases | Gene(s) | OMIM phenotype ID | OMIM gene ID | Key notes | Key citation IDs |
|---|---|---|---|---|---|---|
| Infantile hypercalcemia | Infantile hypercalcaemia; idiopathic infantile hypercalcemia; idiopathic infantile hypercalcaemia; IIH; hypersensitivity to vitamin D3 | CYP24A1, SLC34A1 | General disease term used across subtype literature; specific phenotype IDs below | — | Rare genetic disorder of PTH-independent hypercalcemia; common features include hypercalcemia, hypercalciuria, nephrocalcinosis, suppressed PTH, and elevated/inappropriately normal 1,25(OH)2D3 | (wang2024biallelicandmonoallelic pages 1-2, bizereamoga2023phenotypeofidiopathic pages 1-2) |
| Infantile hypercalcemia type 1 | IIH type 1; idiopathic infantile hypercalcemia type 1; infantile hypercalcaemia-1; HCINF1 | CYP24A1 | 143880 | CYP24A1 *126065 | Caused by loss-of-function variants in CYP24A1 encoding vitamin D 24-hydroxylase; impaired vitamin D catabolism leads to increased active vitamin D and hypercalcemia | (wang2024biallelicandmonoallelic pages 1-2, janiec2021longtermoutcomeof pages 1-2) |
| Infantile hypercalcemia type 2 | IIH type 2; idiopathic infantile hypercalcemia type 2; infantile hypercalcaemia-2; IH subtype 2 | SLC34A1 | 616963 | SLC34A1 *182309 | Caused by variants in SLC34A1 encoding renal proximal tubular NaPi-IIa; phosphate wasting can drive increased 1,25(OH)2D3 and hypercalcemia/hypercalciuria | (bizereamoga2023phenotypeofidiopathic pages 6-7, janiec2021longtermoutcomeof pages 1-2) |
| CYP24A1-related infantile hypercalcemia | 24-hydroxylase deficiency; vitamin D catabolism defect–related infantile hypercalcemia | CYP24A1 | 143880 | CYP24A1 *126065 | CYP24A1 deficiency is the canonical molecular basis of IIH type 1; may also present later with nephrolithiasis/nephrocalcinosis | (khan2023acaseof pages 2-4, janiec2021longtermoutcomeof pages 1-2, cappellani2022hypercalcemiadueto pages 1-2) |
| SLC34A1-related infantile hypercalcemia | NaPi-IIa deficiency–related infantile hypercalcemia; phosphate-wasting infantile hypercalcemia | SLC34A1 | 616963 | SLC34A1 *182309 | SLC34A1-related disease overlaps with nephrocalcinosis/urolithiasis phenotypes and may respond to phosphate supplementation | (bizereamoga2023phenotypeofidiopathic pages 6-7, verjans2024antenatalpresentationand pages 6-9) |
| SLC34A1 gene disease context | Fanconi renotubular syndrome 2; dominant hypophosphatemic nephrolithiasis/osteoporosis; infantile hypercalcemia 2 | SLC34A1 | 613388 (Fanconi renotubular syndrome 2); 612286 (dominant hypophosphatemic nephrolithiasis/osteoporosis); 616963 (infantile hypercalcemia 2) | SLC34A1 *182309 | Useful differential/allelic context for interpreting SLC34A1 findings in suspected IIH | (bizereamoga2023phenotypeofidiopathic pages 6-7) |


*Table: This table summarizes the core naming conventions and OMIM mappings for infantile hypercalcemia and its major Mendelian subtypes. It is useful for harmonizing disease labels across literature and knowledge-base records.*

---

## 2. Etiology

### 2.1 Disease causal factors (genetic, mechanistic)
IIH is primarily genetic and mechanistically related to disturbed vitamin D metabolism or renal phosphate transport.

**CYP24A1 (Infantile hypercalcemia type 1):**
- CYP24A1 encodes vitamin D 24-hydroxylase, which inactivates 25(OH)D and 1,25(OH)2D; loss-of-function (LOF) variants reduce catabolism and drive vitamin D-dependent hypercalcemia. (wang2024biallelicandmonoallelic pages 1-2, khan2023acaseof pages 2-4)

**SLC34A1 (Infantile hypercalcemia type 2):**
- SLC34A1 encodes the renal proximal tubule sodium–phosphate cotransporter NaPi-IIa; variants cause phosphate wasting that can increase 1,25(OH)2D and drive hypercalcemia/hypercalciuria. (wang2024biallelicandmonoallelic pages 1-2, bizereamoga2023phenotypeofidiopathic pages 6-7)

### 2.2 Risk factors

#### Genetic risk factors
- **Biallelic pathogenic variants** in CYP24A1 or SLC34A1 are canonical causes of IIH types 1 and 2. (wang2024biallelicandmonoallelic pages 1-2, janiec2021longtermoutcomeof pages 1-2)
- **Monoallelic variants may be clinically relevant**: a 2024 series concluded that “A monoallelic variant of CYP24A1 or SLC34A1 gene contributes to symptomatic hypercalcemia, hypercalciuria and nephrocalcinosis.” (wang2024biallelicandmonoallelic pages 1-2)
- A 2022 systematic review of CYP24A1-related hypercalcemia reported monoallelic carrier rates of nephrolithiasis (19.4%), nephrocalcinosis (4.9%), and symptomatic hypercalcemia (5.6%). (cappellani2022hypercalcemiadueto pages 1-2)

#### Environmental/iatrogenic triggers
- Vitamin D exposure is a clinically important trigger in susceptible individuals: IIH is referred to as “hypersensitivity to vitamin D3,” and infant presentations are often discussed in the context of supplementation. (bizereamoga2023phenotypeofidiopathic pages 1-2)
- Case-based evidence supports that hypercalcemia crises are managed by discontinuing vitamin D and calcium inputs; multiple sources describe stopping vitamin D/calcium and avoiding sunlight as part of management. (wang2024biallelicandmonoallelic pages 4-7, wang2022cyp24a1andslc34a1 pages 4-6)

### 2.3 Protective factors
No robust genetic “protective variants” or environmental protective factors were identified in the retrieved evidence set for IIH specifically.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum
Across sources, common disease features include:
- **Laboratory abnormalities:** hypercalcemia, suppressed PTH, hypercalciuria, and elevated or inappropriately normal 1,25(OH)2D3. (bizereamoga2023phenotypeofidiopathic pages 1-2, khan2023acaseof pages 2-4)
- **Kidney manifestations:** nephrocalcinosis and/or nephrolithiasis; renal medullary nephrocalcinosis is frequently noted. (wang2024biallelicandmonoallelic pages 1-2, khan2023acaseof pages 2-4)
- **Infant symptoms/signs:** failure to thrive, poor feeding, vomiting, dehydration, hypotonia, lethargy/irritability. A review of neonatal/infant hypercalcemia states hypercalcemia may present with “failure to thrive, poor feeding, constipation, polyuria, irritability, lethargy, seizures and hypotonia.” (gurevich2023idiopathicinfantilehypercalcemia pages 1-2)

### 3.2 Typical age of onset and course
- Presentation is often in the **first year of life**: a systematic review found “Acute hypercalcemia was the typical presentation during the first year of life (76%).” (cappellani2022hypercalcemiadueto pages 1-2)
- However, disease can manifest beyond infancy (e.g., nephrolithiasis/nephrocalcinosis later in childhood/adulthood), and the 2024 Orphanet Journal of Rare Diseases series emphasizes that “Hypercalcemia may not necessarily present after infancy” and IIH should be considered in older patients with nephrolithiasis/nephrocalcinosis. (wang2024biallelicandmonoallelic pages 1-2)

### 3.3 Frequency statistics for selected phenotypes
- In a 2021 long-term follow-up cohort of genetically confirmed infantile hypercalcemia survivors, nephrocalcinosis persisted in **16/18 (88%)** on ultrasound. (janiec2021longtermoutcomeof pages 1-2)
- In the same cohort, **GFR <90 mL/min/1.73m² occurred in 77%**, and **GFR <60 mL/min/1.73m² in 28%**; two CYP24A1 patients developed ESRD requiring transplantation. (janiec2021longtermoutcomeof pages 1-2)

### 3.4 Suggested HPO terms (examples)
The following Human Phenotype Ontology (HPO) terms are consistent with the phenotypes repeatedly described in the retrieved evidence:
- Hypercalcemia (HP:0003072)
- Hypercalciuria (HP:0002150)
- Nephrocalcinosis (HP:0000121)
- Nephrolithiasis (HP:0000787)
- Suppressed PTH / Hypoparathyroidism (context: low PTH in setting of hypercalcemia; often represented by “Decreased circulating parathyroid hormone level” if available)
- Failure to thrive (HP:0001508)
- Vomiting (HP:0002013)
- Dehydration (HP:0001944)
- Hypotonia (HP:0001252)

(bizereamoga2023phenotypeofidiopathic pages 1-2, khan2023acaseof pages 2-4)

**Quality of life impact:** Not systematically quantified in the retrieved evidence. However, long-term renal morbidity (nephrocalcinosis/CKD) implies substantial chronic health impact. (janiec2021longtermoutcomeof pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
- **CYP24A1** (vitamin D 24-hydroxylase): causal for infantile hypercalcemia type 1 (OMIM 143880). (janiec2021longtermoutcomeof pages 1-2, cappellani2022hypercalcemiadueto pages 1-2)
- **SLC34A1** (NaPi-IIa): causal for infantile hypercalcemia type 2 (OMIM 616963). (janiec2021longtermoutcomeof pages 1-2, bizereamoga2023phenotypeofidiopathic pages 6-7)

### 4.2 Inheritance
- Classically **autosomal recessive** for the defined subtypes (biallelic LOF). (bizereamoga2023phenotypeofidiopathic pages 4-6, janiec2021longtermoutcomeof pages 1-2)
- **Symptomatic heterozygosity** is increasingly recognized (monoallelic CYP24A1 or SLC34A1 variants associated with hypercalcemia/hypercalciuria/nephrocalcinosis in some individuals). (wang2024biallelicandmonoallelic pages 1-2, cappellani2022hypercalcemiadueto pages 1-2)

### 4.3 Pathogenic variants and recent variant discoveries (2023–2024 emphasis)
- A 2024 Chinese case series identified **novel variants** in both genes: “Four novel CYP24A1 variants … and three novel SLC34A1 variants … were found.” (wang2024biallelicandmonoallelic pages 1-2)
- Antenatal/early-life presentations and hypomorphic alleles: a 2024 report discusses the relatively common SLC34A1 Val91_Ala97del allele and its population frequency (gnomAD European reference data 5.2%), supporting a model of hypomorphic alleles contributing in trans with pathogenic variants in some cases. (verjans2024antenatalpresentationand pages 6-9)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes or epigenetic signatures specific to IIH were identified in the retrieved evidence.

---

## 5. Environmental information

The dominant non-genetic contributors discussed are **iatrogenic/environmental exposures that increase vitamin D signaling or calcium load**, including vitamin D supplementation and dietary calcium intake; clinical management commonly includes stopping supplementation and reducing exogenous vitamin D and calcium during acute episodes. (wang2024biallelicandmonoallelic pages 4-7, wang2022cyp24a1andslc34a1 pages 4-6)

No specific toxins/pollution/infectious agents were identified as causal in the retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Core causal chains

#### (A) CYP24A1 LOF → increased active vitamin D → hypercalcemia/hypercalciuria → nephrocalcinosis/CKD
Mechanistic description from 2024: CYP24A1 variants “impair catabolism of 25(OH)D3 and 1,25(OH)2D3, leading to accumulation of active vitamin D,” driving increased intestinal calcium absorption/bone resorption and causing hypercalcemia, hypercalciuria, nephrocalcinosis and suppressed PTH. (wang2024biallelicandmonoallelic pages 1-2)

#### (B) SLC34A1 dysfunction → renal phosphate wasting → increased 1,25(OH)2D3 → hypercalcemia/hypercalciuria
A 2024 mechanistic summary states SLC34A1 mutations cause renal phosphate wasting and downstream hormonal changes that raise 1,25(OH)2D3, producing hypercalcemia and hypercalciuria. (wang2024biallelicandmonoallelic pages 1-2)

### 6.2 Biochemical hallmarks
Across reports, the characteristic biochemical signature is PTH-independent hypercalcemia with inappropriate vitamin D metabolite patterns. For example, a 2023 report notes typical features including “raised serum calcium, suppressed PTH, mildly elevated levels of 1,25-dihydroxyvitamin D3, and hypercalciuria.” (khan2023acaseof pages 2-4)

### 6.3 Suggested GO, CL, and pathway annotations (high-level)
Because the retrieved evidence is primarily clinical genetics, pathway annotations are inferred from the described biology:
- **GO Biological Process:** vitamin D metabolic process; calcium ion homeostasis; phosphate ion homeostasis; regulation of renal tubular transport
- **Primary cell types (CL):** renal proximal tubule epithelial cell (SLC34A1 context); intestinal epithelial cell/enterocyte (for calcium absorption as downstream physiology)
- **Key organs (UBERON):** kidney (renal medulla/proximal tubule), small intestine

(wang2024biallelicandmonoallelic pages 1-2, khan2023acaseof pages 2-4)

---

## 7. Anatomical structures affected

### 7.1 Organ and system involvement
- **Kidney:** nephrocalcinosis and nephrolithiasis are core manifestations; long-term CKD/ESRD risk is documented in survivors. (janiec2021longtermoutcomeof pages 1-2, khan2023acaseof pages 2-4)
- **Gastrointestinal system:** vomiting/feeding problems/poor weight gain are common presenting manifestations. (wang2024biallelicandmonoallelic pages 1-2, bizereamoga2023phenotypeofidiopathic pages 1-2)

### 7.2 Suggested UBERON terms (examples)
- Kidney (UBERON:0002113)
- Renal medulla (UBERON:0001224)
- Proximal convoluted tubule (UBERON:0001289)
- Small intestine (UBERON:0002108)

---

## 8. Temporal development

### 8.1 Onset
- Typically **neonatal/infant** onset, often during the first year. (cappellani2022hypercalcemiadueto pages 1-2)
- May present later (older child/adult) with nephrolithiasis/nephrocalcinosis, sometimes after years of diagnostic delay. (khan2023acaseof pages 2-4)

### 8.2 Progression and remission
- Hypercalcemia can be episodic or transient in some cohorts, but renal calcification and CKD risk may persist. (janiec2021longtermoutcomeof pages 1-2, gurevich2023idiopathicinfantilehypercalcemia pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology
Disease-level epidemiology is limited in the retrieved evidence. One 2024 report provides an **incidence estimate**: “an estimated incidence of 1:33,000 live births.” (wang2024biallelicandmonoallelic pages 1-2)

A separate 2023 cohort study in children with kidney hypodysplasia used biochemical criteria for IIH (PTH ≤14 pg/mL and 1,25(OH)2D ≥160 pmol/L) and found **16/139 (11.5%)** met these criteria, suggesting a notable contribution of IIH-like physiology in this selected CKD population (without genetic confirmation). (gurevich2023idiopathicinfantilehypercalcemia pages 1-2)

### 9.2 Penetrance/expressivity
Evidence supports **variable expressivity** and **possible incomplete penetrance**, including symptomatic monoallelic carriers. (cappellani2022hypercalcemiadueto pages 1-2, wang2024biallelicandmonoallelic pages 1-2)

### 9.3 Population genetics / founder or common alleles
The SLC34A1 Val91_Ala97del allele is discussed as common in European ancestry populations (~5.2% in gnomAD European reference), raising the possibility of hypomorphic alleles contributing to disease in trans with a pathogenic variant. (verjans2024antenatalpresentationand pages 6-9)

---

## 10. Diagnostics

### 10.1 Clinical laboratory evaluation
A comprehensive neonatal/infant hypercalcemia evaluation includes calcium and phosphate measurements, PTH, vitamin D metabolites, and urinary indices. A review states diagnosis requires “biochemical measurements, including total and ionised serum calcium, serum phosphate, creatinine and albumin, intact parathyroid hormone (PTH), vitamin D metabolites and urinary calcium, phosphate and creatinine.” (gurevich2023idiopathicinfantilehypercalcemia pages 1-2)

In IIH, a typical diagnostic signature includes hypercalcemia with suppressed PTH and hypercalciuria; 1,25(OH)2D may be elevated or inappropriately normal. (bizereamoga2023phenotypeofidiopathic pages 1-2, khan2023acaseof pages 2-4)

### 10.2 Imaging
Renal ultrasonography is frequently used to identify nephrocalcinosis and to monitor renal status over time. Persistent nephrocalcinosis is common in long-term follow-up. (janiec2021longtermoutcomeof pages 1-2)

### 10.3 Genetic testing strategy
Because IIH can be difficult to diagnose clinically, multiple sources emphasize genetic testing. A 2023 case report notes IIH historically was a diagnosis of exclusion but “can now… be diagnosed using CYP24A1 genetic testing.” (khan2023acaseof pages 2-4)

Practical approach: targeted gene panel for hypercalcemia/nephrocalcinosis/nephrolithiasis (including CYP24A1 and SLC34A1) or exome/genome sequencing in complex/antenatal cases. (verjans2024antenatalpresentationand pages 6-9, khan2023acaseof pages 2-4)

### 10.4 Differential diagnosis
Neonatal/infant hypercalcemia differentials include high-PTH disorders (e.g., neonatal severe hyperparathyroidism, familial hypocalciuric hypercalcemia) vs low-PTH disorders (including IIH and Williams-Beuren syndrome). (gurevich2023idiopathicinfantilehypercalcemia pages 1-2)

---

## 11. Outcome / prognosis

### 11.1 Renal outcomes (key quantitative study)
A 2021 long-term outcome study of genetically confirmed survivors (CYP24A1 or SLC34A1) found substantial CKD burden:
- Mean GFR 72 mL/min/1.73m² (range 15–105)
- **GFR <90 mL/min/1.73m² in 77%**
- **GFR <60 mL/min/1.73m² in 28%**
- **Nephrocalcinosis in 88%**
- Two patients developed ESRD and underwent renal transplantation (CYP24A1). (janiec2021longtermoutcomeof pages 1-2)

### 11.2 Prognostic factors
Genotype (biallelic LOF) and degree/duration of hypercalcemia/hypercalciuria and nephrocalcinosis are plausible prognostic indicators, but robust prognostic models were not found in the retrieved evidence.

---

## 12. Treatment

### 12.1 Acute management of severe hypercalcemia (real-world implementations)
Across case series and reviews, acute therapy is consistent with general hypercalcemia management:
- **Hydration (saline loading)** and **loop diuretics (e.g., furosemide)**. (khan2023acaseof pages 2-4, wang2022cyp24a1andslc34a1 pages 4-6)
- Escalation strategies include **calcitonin**, **bisphosphonates**, and **hemodialysis** in refractory/life-threatening cases. (wang2024biallelicandmonoallelic pages 4-7, wang2022cyp24a1andslc34a1 pages 4-6)

### 12.2 Disease-directed / chronic management
- **Stop vitamin D and calcium supplementation; reduce dietary calcium and sun exposure** during management of vitamin D-driven hypercalcemia. (wang2024biallelicandmonoallelic pages 4-7, wang2022cyp24a1andslc34a1 pages 4-6)
- **Phosphate supplementation** is particularly relevant in SLC34A1-related disease and can reduce hypercalcemia through correction of phosphate wasting and downstream calcitriol excess. (bizereamoga2023phenotypeofidiopathic pages 6-7, verjans2024antenatalpresentationand pages 6-9)
- **Azole antifungals (ketoconazole/fluconazole)** have been used off-label to suppress vitamin D activation; a 2023 case report describes normalization of calcium after “fluconazole 50mg once a day and cinacalcet 30mg twice.” (khan2023acaseof pages 2-4)

### 12.3 Treatment outcomes and evidence strength
- A 2022 systematic review found that the “effect size of the most-used medications administered to control hypercalcemia ranged from 18 to 29%,” and concluded therapeutic approaches were variable and did not allow selection of a preferred regimen. (cappellani2022hypercalcemiadueto pages 1-2)

### 12.4 Suggested MAXO terms (examples)
- Intravenous fluid therapy / hyperhydration
- Loop diuretic therapy
- Bisphosphonate therapy
- Calcitonin therapy
- Hemodialysis
- Dietary calcium restriction
- Vitamin D supplementation avoidance/cessation
- Phosphate supplementation
- Genetic counseling

(wang2024biallelicandmonoallelic pages 4-7, khan2023acaseof pages 2-4, verjans2024antenatalpresentationand pages 6-9)

### 12.5 Clinical trials
No IIH-specific interventional clinical trials were identified in the retrieved evidence set.

---

## 13. Prevention

Because IIH is Mendelian, prevention is largely **secondary/tertiary**:
- **Avoidance of triggering exposures** (particularly vitamin D and excess calcium) in genetically susceptible individuals. (wang2024biallelicandmonoallelic pages 4-7, bizereamoga2023phenotypeofidiopathic pages 1-2)
- **Genetic counseling** for affected families is recommended in case series. (bizereamoga2023phenotypeofidiopathic pages 4-6)
- **Long-term surveillance** with early preventive measures has been recommended due to CKD risk; the long-term outcome study emphasizes monitoring and “early implementation of preventive measures.” (janiec2021longtermoutcomeof pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring veterinary disease analogs were identified in the retrieved evidence set.

---

## 15. Model organisms
No model organism studies specific to IIH were included in the retrieved evidence set used for citation; therefore, this section cannot be populated with tool-supported primary evidence here.

---

## 2023–2024 “latest research” highlights (selected)
- **Genotype expansion and monoallelic effects:** 2024 case series reporting both biallelic and monoallelic pathogenic variants in CYP24A1 and SLC34A1 causing IIH-like disease. Publication date: Mar 2024. URL: https://doi.org/10.1186/s13023-024-03135-8 (wang2024biallelicandmonoallelic pages 1-2)
- **Antenatal presentation / hypomorphic allele interpretation:** 2024 report describing antenatal findings and postnatal phosphate therapy in infantile hypercalcemia type 2; includes gnomAD frequency data supporting hypomorphic allele models. Publication date: May 2024. URL: https://doi.org/10.1007/s00467-024-06403-8 (verjans2024antenatalpresentationand pages 6-9)
- **Clinical phenotype emphasis in heterozygotes:** 2023 paper describing IIH phenotypes associated with heterozygous variants and reinforcing the importance of genetic diagnosis. Publication date: Oct 2023. URL: https://doi.org/10.3390/children10101701 (bizereamoga2023phenotypeofidiopathic pages 1-2)
- **Selected high-risk population observation:** 2023 cohort showing transient IIH-like biochemistry in kidney hypodysplasia infants (biochemical definition), suggesting broader clinical contexts where IIH physiology may be encountered. Publication date: Sep 2023. URL: https://doi.org/10.1007/s00467-022-05740-w (gurevich2023idiopathicinfantilehypercalcemia pages 1-2)

---

## Notes on evidence gaps and constraints
- The tool-accessible corpus used here did not contain explicit Orphanet, ICD-10/11, MeSH, or MONDO identifiers for IIH; these may exist in external ontology resources (OMIM/Orphanet/MONDO), but cannot be asserted without retrieved-citation support.
- Model organism evidence, transcriptomics/proteomics/metabolomics signatures, and formal quality-of-life instruments were not found in the retrieved evidence set.


References

1. (wang2024biallelicandmonoallelic pages 1-2): Qiao Wang, Jia-jia Chen, Li-ya Wei, Yuan Ding, Min Liu, Wen-jing Li, Chang Su, and Chun-xiu Gong. Biallelic and monoallelic pathogenic variants in cyp24a1 and slc34a1 genes cause idiopathic infantile hypercalcemia. Orphanet Journal of Rare Diseases, Mar 2024. URL: https://doi.org/10.1186/s13023-024-03135-8, doi:10.1186/s13023-024-03135-8. This article has 10 citations and is from a peer-reviewed journal.

2. (bizereamoga2023phenotypeofidiopathic pages 1-2): Teofana Otilia Bizerea-Moga, Flavia Chisavu, Cristina Ilies, Orsolya Olah, Otilia Marginean, Mihai Gafencu, Gabriela Doros, and Ramona Stroescu. Phenotype of idiopathic infantile hypercalcemia associated with the heterozygous pathogenic variant of slc34a1 and cyp24a1. Children, 10:1701, Oct 2023. URL: https://doi.org/10.3390/children10101701, doi:10.3390/children10101701. This article has 8 citations.

3. (khan2023acaseof pages 2-4): Zahid Khan, Gideon Mlawa, Yu-Hsuen Yang, and Bashir Mahamud. A case of delayed diagnosis of idiopathic infantile hypercalcemia due to cyp24a1 mutation: a 10-year journey. Cureus, Aug 2023. URL: https://doi.org/10.7759/cureus.42811, doi:10.7759/cureus.42811. This article has 2 citations.

4. (verjans2024antenatalpresentationand pages 6-9): Marcelien Verjans, An Hindryckx, Karen Rosier, Koen Devriendt, Djalila Mekahli, and Detlef Bockenhauer. Antenatal presentation and early postnatal treatment of infantile hypercalcemia type 2. Pediatric nephrology, 39:2911-2913, May 2024. URL: https://doi.org/10.1007/s00467-024-06403-8, doi:10.1007/s00467-024-06403-8. This article has 2 citations and is from a domain leading peer-reviewed journal.

5. (janiec2021longtermoutcomeof pages 1-2): Agnieszka Janiec, Paulina Halat-Wolska, Łukasz Obrycki, Elżbieta Ciara, Marek Wójcik, Paweł Płudowski, Aldona Wierzbicka, Ewa Kowalska, Janusz B Książyk, Zbigniew Kułaga, Ewa Pronicka, and Mieczysław Litwin. Long-term outcome of the survivors of infantile hypercalcaemia with cyp24a1 and slc34a1 mutations. Nephrology Dialysis Transplantation, 36:1484-1492, Oct 2021. URL: https://doi.org/10.1093/ndt/gfaa178, doi:10.1093/ndt/gfaa178. This article has 39 citations and is from a domain leading peer-reviewed journal.

6. (cappellani2022hypercalcemiadueto pages 1-2): Daniele Cappellani, Alessandro Brancatella, Riccardo Morganti, Simona Borsari, Fulvia Baldinotti, Maria Adelaide Caligo, Martin Kaufmann, Glenville Jones, Claudio Marcocci, and Filomena Cetani. Hypercalcemia due to cyp24a1 mutations: a systematic descriptive review. European Journal of Endocrinology, 186:137-149, Feb 2022. URL: https://doi.org/10.1530/eje-21-0713, doi:10.1530/eje-21-0713. This article has 55 citations and is from a highest quality peer-reviewed journal.

7. (bizereamoga2023phenotypeofidiopathic pages 6-7): Teofana Otilia Bizerea-Moga, Flavia Chisavu, Cristina Ilies, Orsolya Olah, Otilia Marginean, Mihai Gafencu, Gabriela Doros, and Ramona Stroescu. Phenotype of idiopathic infantile hypercalcemia associated with the heterozygous pathogenic variant of slc34a1 and cyp24a1. Children, 10:1701, Oct 2023. URL: https://doi.org/10.3390/children10101701, doi:10.3390/children10101701. This article has 8 citations.

8. (wang2024biallelicandmonoallelic pages 4-7): Qiao Wang, Jia-jia Chen, Li-ya Wei, Yuan Ding, Min Liu, Wen-jing Li, Chang Su, and Chun-xiu Gong. Biallelic and monoallelic pathogenic variants in cyp24a1 and slc34a1 genes cause idiopathic infantile hypercalcemia. Orphanet Journal of Rare Diseases, Mar 2024. URL: https://doi.org/10.1186/s13023-024-03135-8, doi:10.1186/s13023-024-03135-8. This article has 10 citations and is from a peer-reviewed journal.

9. (wang2022cyp24a1andslc34a1 pages 4-6): Qiao Wang, Jia-jia Chen, Li-ya Wei, Min Liu, Wen-jing Li, Chang Su, and Chunxiu Gong. Cyp24a1 and slc34a1 mutations in five cases with idiopathic infantile hypercalcemia. SSRN Electronic Journal, Oct 2022. URL: https://doi.org/10.2139/ssrn.4257523, doi:10.2139/ssrn.4257523. This article has 0 citations.

10. (gurevich2023idiopathicinfantilehypercalcemia pages 1-2): Evgenia Gurevich, Yael Borovitz, Shelli Levi, Sharon Perlman, and Daniel Landau. Idiopathic infantile hypercalcemia in children with chronic kidney disease due to kidney hypodysplasia. Pediatric Nephrology, 38:1067-1073, Sep 2023. URL: https://doi.org/10.1007/s00467-022-05740-w, doi:10.1007/s00467-022-05740-w. This article has 0 citations and is from a domain leading peer-reviewed journal.

11. (bizereamoga2023phenotypeofidiopathic pages 4-6): Teofana Otilia Bizerea-Moga, Flavia Chisavu, Cristina Ilies, Orsolya Olah, Otilia Marginean, Mihai Gafencu, Gabriela Doros, and Ramona Stroescu. Phenotype of idiopathic infantile hypercalcemia associated with the heterozygous pathogenic variant of slc34a1 and cyp24a1. Children, 10:1701, Oct 2023. URL: https://doi.org/10.3390/children10101701, doi:10.3390/children10101701. This article has 8 citations.

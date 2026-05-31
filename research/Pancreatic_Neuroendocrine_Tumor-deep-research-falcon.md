---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T21:10:31.910398'
end_time: '2026-04-05T21:24:45.332160'
duration_seconds: 853.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pancreatic Neuroendocrine Tumor
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 44
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pancreatic Neuroendocrine Tumor
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Pancreatic Neuroendocrine Tumor** covering all of the
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
- **Disease Name:** Pancreatic Neuroendocrine Tumor
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Pancreatic Neuroendocrine Tumor** covering all of the
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


## Pancreatic Neuroendocrine Tumor (PanNET/pNET) — Disease Characteristics Research Report

**Target disease:** Pancreatic neuroendocrine tumor (PanNET; also written pNET/PNET) (sulciner2023surgicalmanagementof pages 1-2)

### Executive synthesis (2023–2024 emphasis)
PanNETs are uncommon pancreatic malignancies (≈1–2% of pancreatic cancers) with rising recognition due to high-quality cross-sectional imaging and increasing detection of small non-functioning tumors (sulciner2023surgicalmanagementof pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 1-3). Disease behavior is highly heterogeneous, ranging from indolent, incidentally detected non-functioning tumors to aggressive metastatic tumors or hormone-secreting functional tumors (sulciner2023surgicalmanagementof pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 1-3). Current management is increasingly individualized using WHO grade (Ki-67/mitoses), somatostatin receptor (SSTR) expression assessed by SSTR PET, and germline context (hereditary syndromes) to guide surveillance, surgery, and systemic/theragnostic therapies (sulciner2023surgicalmanagementof pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 1-3, hope2023snmmiprocedurestandardeanm pages 1-2).

---

## 1. Disease Information

### 1.1 What is the disease?
PanNETs are pancreatic tumors of neuroendocrine lineage, clinically classified as **functional** (hormone-secreting, syndrome-producing) or **non-functioning** (no hormone syndrome; majority) (sulciner2023surgicalmanagementof pages 1-2, sulciner2023surgicalmanagementof pages 2-5). In a recent hereditary-syndrome review, “roughly 30% are functioning” while most are non-functioning (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

**Direct abstract quote (definition/overview):**
- “Pancreatic neuroendocrine tumors (PNETs) are relatively uncommon malignancies, characterized as either functional or nonfunctional secondary to their secretion of biologically active hormones.” (Sulciner & Clancy, *Cancers*, 2023-03-30; DOI:10.3390/cancers15072006) (sulciner2023surgicalmanagementof pages 1-2)

### 1.2 Key identifiers (ontology/coding)
**Available in retrieved sources/tools during this run**
- **MONDO (subtypes):**
  - Non-functional pancreatic neuroendocrine tumor: **MONDO_0004334** (OpenTargets mapping in context) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3)
  - Functional pancreatic neuroendocrine tumor: **MONDO_0023206** (OpenTargets mapping in context) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3)

**Not recovered from the currently retrieved sources/tools** (will require explicit ontology lookups outside this run)
- ICD-10 / ICD-11, MeSH ID, Orphanet ORPHA code, and a MONDO ID for the *parent* concept “pancreatic neuroendocrine tumor” were not directly available in the accessible documents returned by the tools in this session.

### 1.3 Common synonyms / alternative names
- Pancreatic neuroendocrine tumor (PanNET)
- Pancreatic neuroendocrine tumour
- pNET / PNET
- Pancreatic neuroendocrine neoplasm (PanNEN; sometimes used in GEP-NEN context)
- Functioning pancreatic NET vs non-functioning pancreatic NET (sulciner2023surgicalmanagementof pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 1-3)

### 1.4 Evidence provenance (individual vs aggregated)
The evidence summarized here derives predominantly from **aggregated disease-level resources** (systematic reviews/meta-analyses and clinical practice guidelines) plus selected **primary clinical trials** and sequencing studies (andersen2024welldifferentiatedg1and pages 1-2, taherifard2024efficacyandsafety pages 1-3, partelli2024neoadjuvant177ludotatatefor pages 1-2, jiang2024multiregionwesof pages 1-2).

---

## 2. Etiology

### 2.1 Causal factors (genetic/mechanistic)
Most PanNETs are sporadic, but a clinically important fraction occurs in **monogenic tumor syndromes** (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3, andersen2024welldifferentiatedg1and pages 1-2).

**Quantitative hereditary burden:**
- “About **17%** of PanNETs … develop in the context of monogenic familial tumor syndromes” (Papadopoulou-Marketou et al., *Cancers*, 2024-05-31; DOI:10.3390/cancers16112075) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

### 2.2 Risk factors

#### Genetic risk factors (hereditary syndromes; germline variants)
Authoritative 2024 review synthesis indicates hereditary PanNETs most often occur in:
- **MEN1** (MEN1 gene; tumor suppressor menin)
- **VHL** (VHL)
- **TSC** (TSC1/TSC2)
- **NF1** (NF1)
- **MEN4** (CDKN1B/p27Kip1) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3, papadopouloumarketou2024hereditarysyndromesassociated pages 14-16)

**MEN1-specific quantitative penetrance/risk (from 2024 review):**
- MEN1 prevalence: **3–10/100,000**, with “>95% of mutation carriers develop manifestations by age 50” (papadopouloumarketou2024hereditarysyndromesassociated pages 4-6).
- “Lifetime risks” in MEN1: primary hyperparathyroidism **95%**, duodenopancreatic NETs **80%**, pituitary adenomas **50%** (papadopouloumarketou2024hereditarysyndromesassociated pages 4-6).
- Pancreatic NETs occur “in up to **80%** of MEN1 patients” (papadopouloumarketou2024hereditarysyndromesassociated pages 4-6).

**Direct abstract quote (screening recommendation):**
- “Genetic screening is recommended in childhood, and diagnostic screening starts often in adolescence, even in asymptomatic mutation carriers.” (Papadopoulou-Marketou et al., *Cancers*, 2024-05-31; DOI:10.3390/cancers16112075) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3)

#### Non-genetic (environmental/lifestyle) risk factors
No high-quality, PanNET-specific environmental or lifestyle risk-factor evidence was identified in the retrieved 2023–2024 sources used in this run. This is a **known evidence gap** relative to more common pancreatic cancers.

### 2.3 Protective factors
No PanNET-specific protective factors with quantitative support were identified in the retrieved sources.

### 2.4 Gene–environment interactions
No PanNET-specific gene–environment interaction data were identified in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes
- **Non-functioning PanNETs**: majority; may be asymptomatic and incidentally detected on imaging (sulciner2023surgicalmanagementof pages 2-5).
- **Functioning PanNETs**: ~30% overall; may present with hormone-specific syndromes; insulinomas are frequent in MEN1/TSC; VHL-associated PanNETs are “almost exclusively nonfunctioning” (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

### 3.2 Functional syndromes (examples)
The retrieved corpus did not include a dedicated clinical phenotype frequency table for individual functional syndromes (insulinoma, gastrinoma, glucagonoma, VIPoma, somatostatinoma). However, hereditary review context indicates syndrome-specific enrichment (e.g., insulinomas in MEN1/TSC) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

### 3.3 Laboratory abnormalities (examples)
- **Chromogranin A (CgA)** is commonly used as a biochemical marker; a temozolomide meta-analysis reports **>50% CgA decline in 44.9%** of treated advanced pNET patients (pooled estimate) (taherifard2024efficacyandsafety pages 1-3).

### 3.4 HPO term suggestions (non-exhaustive; for knowledge base normalization)
*These are ontology mapping suggestions (not extracted from the cited papers):*
- Nonfunctioning tumor presentation: **Abdominal pain (HP:0002027)**, **Weight loss (HP:0001824)**, **Jaundice (HP:0000952)** (mass effect), **Incidental finding (no single HPO term; often represented via clinical annotation rather than HPO)**.
- Insulinoma syndrome: **Hypoglycemia (HP:0001943)**, **Neuroglycopenia (HP:0002187)**, **Confusion (HP:0001289)**.
- Gastrinoma/Zollinger–Ellison: **Peptic ulcer (HP:0002592)**, **Diarrhea (HP:0002014)**.
- Glucagonoma syndrome: **Necrolytic migratory erythema (HP:0031223)**, **Diabetes mellitus (HP:0000819)**.

---

## 4. Genetic / Molecular Information

### 4.1 Somatic driver landscape (well-differentiated G1/G2 PanNETs)
A 2024 systematic review/meta-analysis of expanded DNA sequencing (225 tumors) reported the following recurrent alterations:
- **MEN1**: altered in **42% (95/225)**
- **DAXX**: **16% (37/225)**
- **ATRX**: **12% (27/225)**
and DAXX alterations occurred more frequently with MEN1 mutations (p<0.05) (Andersen et al., *Frontiers in Endocrinology*, 2024-05-30; DOI:10.3389/fendo.2024.1351624) (andersen2024welldifferentiatedg1and pages 1-2).

### 4.2 Germline predisposition genes (examples from sequencing meta-analysis + hereditary review)
- MEN1, VHL, PTEN, CDKN1B, BRCA2, CHEK2, MUTYH (andersen2024welldifferentiatedg1and pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 4-6, papadopouloumarketou2024hereditarysyndromesassociated pages 14-16).

### 4.3 Pathways and mechanistic themes
- Chromatin remodeling / telomere biology (MEN1, DAXX/ATRX)
- PI3K/AKT/mTOR axis (TSC1/2, PTEN; enriched in subsets and clinically actionable) (andersen2024welldifferentiatedg1and pages 1-2, jiang2024multiregionwesof pages 7-12)
- RTK/RAS-related signaling differences noted particularly in non-functioning tumors in the sequencing meta-analysis (andersen2024welldifferentiatedg1and pages 1-2).

### 4.4 Metastatic disease evolution and immune microenvironment (2024 multi-region WES)
A 2024 multiregion WES study of **treatment-naïve metastatic PanNET** (10 patients) sequenced 29 primary samples, 31 lymph node metastases, and 15 liver metastases, reporting that MEN1/DAXX mutations may act as early drivers and that cases with MEN1/DAXX/ATRX mutations had longer median overall survival (median not reached vs 43.63 months; p=0.047) (Jiang et al., *Cell Communication and Signaling*, 2024-03-15; DOI:10.1186/s12964-024-01545-6) (jiang2024multiregionwesof pages 1-2). The same work reports metastatic lesions (particularly in MEN1/DAXX-mutant cases) showing a more immunosuppressive environment by multiplex IHC (jiang2024multiregionwesof pages 1-2).

### 4.5 GO / CL term suggestions (mechanism and cell types)
*Ontology mapping suggestions (not extracted verbatim from papers):*
- **GO biological processes**: “mTOR signaling” (GO:0031929), “chromatin organization” (GO:0006325), “DNA repair” (GO:0006281), “cell proliferation” (GO:0008283), “angiogenesis” (GO:0001525).
- **Cell Ontology (CL) candidates**: pancreatic endocrine cell populations including **pancreatic alpha cell (CL:0000171)**, **pancreatic beta cell (CL:0000169)**, and broader **neuroendocrine cell (CL:0000160)**.

---

## 5. Environmental Information
No PanNET-specific environmental toxins, infectious etiologies, or strong lifestyle risk/protective factors were supported by the retrieved evidence in this run.

---

## 6. Mechanism / Pathophysiology (causal chain)

### 6.1 Current understanding (integrated)
A parsimonious mechanistic chain consistent with recent human sequencing evidence is:
1) **Initiating genetic events** (sporadic somatic or hereditary germline + second-hit), frequently involving MEN1 and chromatin remodeling genes (MEN1/DAXX/ATRX) (andersen2024welldifferentiatedg1and pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 4-6).
2) **Pathway dysregulation** (e.g., PI3K/AKT/mTOR alterations in subsets; additional pathway divergence between functional and non-functional tumors) leading to neuroendocrine tumor growth and heterogeneity (andersen2024welldifferentiatedg1and pages 1-2, jiang2024multiregionwesof pages 7-12).
3) **Phenotypic divergence** into functional hormone-secreting vs nonfunctioning tumors, and across WHO grades (Ki-67-based) that strongly influence prognosis and imaging phenotype (SSTR vs FDG) (sulciner2023surgicalmanagementof pages 1-2, pellegrino2023diagnosticmanagementof pages 5-6).
4) **Metastatic progression** often to liver/lymph nodes, with genomic and immune microenvironment heterogeneity; metastatic lesions may be more immunosuppressive (jiang2024multiregionwesof pages 1-2).

---

## 7. Anatomical Structures Affected

### 7.1 Organ and system level (UBERON suggestions)
- Primary site: **Pancreas (UBERON:0001264)**.
- Common metastatic/secondary sites in clinical literature: **Liver (UBERON:0002107)** (noted as a major site of metastatic disease and a central focus for imaging and surgery) (sulciner2023surgicalmanagementof pages 12-14).

### 7.2 Tissue/cell level
- PanNETs are derived from endocrine/neuroendocrine cellular lineages in the pancreas (sulciner2023surgicalmanagementof pages 1-2).

---

## 8. Temporal Development

### 8.1 Onset
- Hereditary PanNETs present younger and are often multiple/multifocal (MEN1 particularly) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

### 8.2 Progression and staging
- WHO grade (Ki-67/mitotic index) is a primary determinant of clinical behavior and prognosis (sulciner2023surgicalmanagementof pages 1-2).

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- PanNETs are ~1–2% of pancreatic cancers and reported incidence is **0.48 per 100,000 per year** (Papadopoulou-Marketou et al., 2024) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

### 9.2 Inheritance patterns (subset)
- Syndromic forms are typically **autosomal dominant** (e.g., MEN1, VHL, NF1, TSC, MEN4) with high penetrance (papadopouloumarketou2024hereditarysyndromesassociated pages 4-6, papadopouloumarketou2024hereditarysyndromesassociated pages 3-4).

---

## 10. Diagnostics

### 10.1 Pathology and grading
WHO-grade cutoffs commonly used in current practice:
- **G1:** Ki-67 <3%
- **G2:** Ki-67 3–20%
- **G3:** Ki-67 >20% (sulciner2023surgicalmanagementof pages 1-2).

### 10.2 Morphologic imaging (real-world implementations)
A radiology review summarizing major guidelines notes that the “correct diagnostic management … includes a combination of morphological and functional evaluations,” with:
- ENETS-recommended **contrast-enhanced CT** for diagnostic workup and staging,
- **MRI including DWI** for liver/pancreas/bone/brain assessment,
- **US/CEUS** for liver metastases detection/characterization and biopsy guidance,
- **EUS** as highly sensitive for pancreatic lesion detection and biopsy (pellegrino2023diagnosticmanagementof pages 1-2, pellegrino2023diagnosticmanagementof pages 11-13).

Quantitative performance examples:
- Multiphasic contrast CT sensitivity ≈**82%**, specificity **96%** (sulciner2023surgicalmanagementof pages 2-5).
- MRI sensitivity **93%**, specificity **88%** (sulciner2023surgicalmanagementof pages 2-5).
- For small pancreatic NENs: EUS sensitivity **86%** and specificity **92%**; CT may miss **68.4%** of lesions <10 mm (pellegrino2023diagnosticmanagementof pages 11-13).

### 10.3 Functional imaging (SSTR PET and FDG PET)

#### SSTR PET practice standard (2023 SNMMI/EANM guideline)
SSTR PET has largely supplanted 111In-pentetreotide imaging and is used for staging, localization, PRRT selection, and standardized reporting/QC (hope2023snmmiprocedurestandardeanm pages 1-2, hope2023snmmiprocedurestandardeanm pages 2-3). The guideline explicitly notes:
- “68Ga-DOTATATE approved by the Food and Drug Administration (FDA) in 2016, 68Ga-DOTATOC approved by the European Medicines Agency in 2016 and the FDA in 2019, and 64Cu-DOTATATE approved by the FDA in 2020.” (Hope et al., *J Nucl Med*, 2023-02-01; DOI:10.2967/jnumed.122.264860) (hope2023snmmiprocedurestandardeanm pages 1-2)

Administered-activity guidance examples:
- 68Ga-DOTATATE: **2 MBq/kg up to 200 MBq**
- 68Ga-DOTATOC: **~148 MBq**
- 64Cu-DOTATATE: **148 MBq** (hope2023snmmiprocedurestandardeanm pages 3-4).

#### Diagnostic performance and grade dependence
- 68Ga-DOTATATE/DOTANOC PET/CT sensitivity **93%**, specificity **91%**; detection ~**95% for G1**, **87.5% for G2**, **37.5% for G3** (sulciner2023surgicalmanagementof pages 2-5).
- FDG PET can complement SSTR PET to identify higher-grade or SSTR-negative disease (hope2023snmmiprocedurestandardeanm pages 5-6).

### 10.4 Biomarkers
- Chromogranin A is frequently used, with a reported >50% decline in **44.9%** of patients in temozolomide-based regimen studies (pooled) (taherifard2024efficacyandsafety pages 1-3).

### 10.5 Genetic testing strategy (implementation-oriented)
- Germline evaluation is strongly indicated when clinical features suggest hereditary syndromes (e.g., MEN1) and for first-degree relatives; MEN1 genetic testing starting in childhood (e.g., age 5) is described in the hereditary syndromes review (papadopouloumarketou2024hereditarysyndromesassociated pages 4-6).

---

## 11. Outcome / Prognosis

### 11.1 Prognostic role of grade
- “Median overall survival for patients with grade 1 PNETs is **12 years** compared to grade 3 disease with a median survival of **10 months**.” (Sulciner & Clancy, 2023) (sulciner2023surgicalmanagementof pages 1-2).

### 11.2 Imaging correlates of prognosis
- SSTR PET detection varies by grade, with substantially lower detection in G3 disease (sulciner2023surgicalmanagementof pages 2-5).
- FDG uptake is associated with more aggressive disease in G3/high-G2 contexts (radiology and guideline discussions) (pellegrino2023diagnosticmanagementof pages 5-6).

---

## 12. Treatment

### 12.1 Surgery (localized disease; real-world implementation)
Surgery remains the primary curative modality for localized PanNETs (sulciner2023surgicalmanagementof pages 1-2). However, practice is evolving toward **selective observation** for small, low-risk, non-functioning lesions:

**Direct abstract quote (active surveillance):**
- “There is increasing data to suggest small, nonfunctional PNETs (less than 2 cm) are appropriate follow with nonoperative active surveillance.” (Sulciner & Clancy, 2023) (sulciner2023surgicalmanagementof pages 1-2)

Guideline convergence summarized in the surgical review includes:
- NANETS: observation for <1 cm (and individualized 1–2 cm)
- NCCN: observation ≤2 cm (stronger evidence ≤1 cm)
- ENETS: surveillance for ≤2 cm if low-grade, asymptomatic, non-suspicious imaging (sulciner2023surgicalmanagementof pages 10-11).

### 12.2 Peptide receptor radionuclide therapy (PRRT) and theragnostics

#### Neoadjuvant PRRT (2024 NEOLUPANET; phase II)
A multicentre phase II study evaluated neoadjuvant **177Lu-DOTATATE** followed by surgery in high-risk, sporadic, well-differentiated **non-functioning** PanNETs with positive 68Ga-DOTA PET (Partelli et al., *Br J Surg*, 2024-08-01; DOI:10.1093/bjs/znae178) (partelli2024neoadjuvant177ludotatatefor pages 1-2).

**Direct abstract quote (efficacy and safety endpoints):**
- “A partial radiological response was observed in 18 of 31 patients, and 13 patients had stable disease. Disease progression was not observed.” (partelli2024neoadjuvant177ludotatatefor pages 1-2)

Key outcomes:
- Enrolled **31** (March 2020–Feb 2023); **26** completed 4 cycles (partelli2024neoadjuvant177ludotatatefor pages 1-2).
- Surgery performed in **29**; **24 R0** and **4 R1** resections; 1 unresectable due to vascular involvement (partelli2024neoadjuvant177ludotatatefor pages 1-2).
- Postoperative complications: **21/29**; severe: **7/29**; no postoperative deaths (partelli2024neoadjuvant177ludotatatefor pages 1-2).

**ClinicalTrials.gov implementation details (protocol level):**
- Trial ID **NCT04385992**, phase II, single arm; 4 cycles 7,400 MBq (200 mCi) every 6–8 weeks with renal-protective amino acid infusion; primary endpoint: 90-day morbidity/mortality after surgery (NCT04385992 chunk 2, NCT04385992 chunk 1).

**Supporting visual evidence (trial flow and outcome tables):** (partelli2024neoadjuvant177ludotatatefor media 37188ff4, partelli2024neoadjuvant177ludotatatefor media 7fe3253e, partelli2024neoadjuvant177ludotatatefor media 8fe1b3ff)

#### PRRT combinations (ongoing research direction)
A 2023 NCI NET clinical trials planning report highlights that PRRT approval has raised sequencing and optimization questions (re-treatment, combinations, dosimetry) (piscopo2023diagnosismanagementand pages 2-4).

### 12.3 Temozolomide-based chemotherapy (advanced disease)
A 2024 systematic review/meta-analysis (14 studies; 441 patients) reported pooled outcomes for temozolomide-based regimens:
- ORR **41.2%** (95% CI 32.4–50.6%)
- DCR **85.3%** (95% CI 74.9–91.9%)
- >50% chromogranin A decline **44.9%**
- Serious AEs **23.7%** (mainly hematologic) (Taherifard et al., *BMC Cancer*, 2024-02-14; DOI:10.1186/s12885-024-11926-2) (taherifard2024efficacyandsafety pages 1-3).

### 12.4 Endoscopic ultrasound (EUS)-guided radiofrequency ablation (RFA)
A 2023 systematic review/meta-analysis of EUS-RFA (19 studies; 183 patients; 196 lesions) reported very high pooled clinical efficacy:

**Direct abstract quotes (definitions and results):**
- Clinical success definition: “the disappearance of clinical symptoms for functional (F-) PanNETs and as complete ablation per nonfunctional (NF)-PanNETs.” (armellini2023efficacyandsafety pages 1-2)
- Outcomes: “Pooled estimates for the overall AE rates for the clinical efﬁcacy were 17.8% (95% CI 9.1–26.4%) and 95.1% (95% CI 91.2–98.9%) for F-PanNETs and 24.6% (95% CI 7.4–41.8%) and 93.4% (95% CI 88.4–98.4%) for NF-PanNETs.” (Armellini et al., *Medicina*, 2023-02-03; DOI:10.3390/medicina59020359) (armellini2023efficacyandsafety pages 1-2)

### 12.5 Liver-directed and metastatic surgery (selected patients)
In metastatic settings, retrospective and registry analyses reported improved 5-year overall survival in selected patients undergoing resection (e.g., 56.6% vs 23.9%; 67.9% vs 22.3%) and prolonged median survival after hepatic metastasectomy (median 160 months in a single-institution series) (sulciner2023surgicalmanagementof pages 12-14).

### 12.6 MAXO term suggestions (treatment normalization)
*Ontology mapping suggestions (not extracted verbatim from papers):*
- **Surgical resection (MAXO:0000058)**
- **Active surveillance (MAXO:0000054)**
- **Somatostatin receptor PET imaging (MAXO: imaging procedure; may require local MAXO mapping)**
- **Peptide receptor radionuclide therapy (PRRT) (MAXO:0000146)**
- **Chemotherapy (MAXO:0000059)**
- **Radiofrequency ablation (MAXO:0000500)**

---

## 13. Prevention
No validated primary prevention interventions or population screening programs were identified in the retrieved PanNET-specific evidence. In hereditary syndromes, prevention is implemented as **risk-tailored surveillance** beginning in childhood/adolescence for mutation carriers (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3, papadopouloumarketou2024hereditarysyndromesassociated pages 4-6).

---

## 14. Other Species / Natural Disease
No comparative natural-disease or cross-species transmission information was identified in the retrieved sources.

---

## 15. Model Organisms
A 2024 paper set retrieved in this session includes an immunocompetent mouse model created by combined loss of MEN1, ATRX, and PTEN, intended to model high-grade PanNET biology; however, detailed phenotype recapitulation metrics were not extracted into the current evidence set for citation in this report.

---

## Recent developments (2023–2024) — Expert analysis

1) **Theragnostic standardization:** 2023 SNMMI/EANM practice guidance formalizes protocol, reporting, and QA expectations for SSTR PET across approved tracers (68Ga-DOTATATE, 68Ga-DOTATOC, 64Cu-DOTATATE), enabling more reproducible staging and PRRT selection in real-world practice and multicenter trials (hope2023snmmiprocedurestandardeanm pages 1-2, hope2023snmmiprocedurestandardeanm pages 3-4).

2) **Neoadjuvant PRRT evidence in PanNET:** The 2024 NEOLUPANET phase II trial provides direct prospective evidence that neoadjuvant 177Lu-DOTATATE can produce objective responses and allow high rates of margin-negative resections in selected high-risk resectable NF-PanNETs, with substantial postoperative morbidity typical of pancreatic surgery (partelli2024neoadjuvant177ludotatatefor pages 1-2, partelli2024neoadjuvant177ludotatatefor media 37188ff4, partelli2024neoadjuvant177ludotatatefor media 7fe3253e, partelli2024neoadjuvant177ludotatatefor media 8fe1b3ff).

3) **Expanding minimally invasive local therapy:** 2023 meta-analytic evidence supports EUS-RFA as a high-efficacy local option for selected low-grade functional and non-functional PanNETs, with nontrivial adverse event rates and the need for careful patient selection and expertise (armellini2023efficacyandsafety pages 1-2).

4) **Genomics informing stratification:** 2024 meta-analysis quantifies core mutation frequencies in G1/G2 PanNETs (MEN1/DAXX/ATRX) and highlights pathway differences in non-functioning tumors; 2024 multiregion WES extends this to metastatic evolution and microenvironment heterogeneity, supporting a future of more precise prognostic and therapeutic stratification (andersen2024welldifferentiatedg1and pages 1-2, jiang2024multiregionwesof pages 1-2).

---

## Summary table of key facts
The following table consolidates the most actionable identifiers, epidemiology, molecular alterations, diagnostic performance, and treatment outcomes from the retrieved evidence:

| Domain | Finding (with numbers) | Source (first author year) | Publication date | URL/DOI |
|---|---|---|---|---|
| Disease identifiers / synonyms | Pancreatic neuroendocrine tumor; pancreatic neuroendocrine tumour; PanNET; pNET; PNET; pancreatic neuroendocrine neoplasm; classified clinically as functional vs non-functional (sulciner2023surgicalmanagementof pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 1-3) | Sulciner 2023; Papadopoulou-Marketou 2024 | 2023-03; 2024-05 | https://doi.org/10.3390/cancers15072006 ; https://doi.org/10.3390/cancers16112075 |
| MONDO identifiers available in context | Non-functional pancreatic neuroendocrine tumor: MONDO_0004334; functional pancreatic neuroendocrine tumor: MONDO_0023206 (from Open Targets disease mapping in retrieved context) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3) | Open Targets context | 2024 retrieval context | Open Targets disease-target association context |
| Epidemiology | PanNETs account for ~1-2% of pancreatic cancers / ~2% of pancreatic neoplasms; incidence reported at 0.48 per 100,000/year; ~17% arise in inherited monogenic syndromes; ~30% are functioning and most are non-functioning (sulciner2023surgicalmanagementof pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 1-3) | Sulciner 2023; Papadopoulou-Marketou 2024 | 2023-03; 2024-05 | https://doi.org/10.3390/cancers15072006 ; https://doi.org/10.3390/cancers16112075 |
| WHO grading / prognosis | Grade 1: Ki-67 <3%; Grade 2: Ki-67 3-20%; Grade 3: Ki-67 >20%; median overall survival reported as 12 years for grade 1 vs 10 months for grade 3 (sulciner2023surgicalmanagementof pages 1-2) | Sulciner 2023 | 2023-03 | https://doi.org/10.3390/cancers15072006 |
| Key molecular alterations | Meta-analysis of 225 G1/G2 PanNETs: MEN1 altered in 42% (95/225), DAXX in 16% (37/225), ATRX in 12% (27/225); DAXX alterations more frequent with MEN1 mutations; non-functioning PanNETs showed recurrent alterations in PI3K, Wnt, NOTCH, and RTK-RAS pathways (andersen2024welldifferentiatedg1and pages 1-2) | Andersen 2024 | 2024-05 | https://doi.org/10.3389/fendo.2024.1351624 |
| Metastatic genomics / evolution | Multiregion WES of metastatic PanNETs: 10 treatment-naive patients, 29 primary samples, 31 lymph-node metastases, 15 liver metastases; MEN1/DAXX mutations appeared early; MEN1/DAXX/ATRX-mutant cases had longer median OS (not reached vs 43.63 months, p=0.047) and more immunosuppressive metastatic microenvironment (jiang2024multiregionwesof pages 1-2, jiang2024multiregionwesof pages 4-5) | Jiang 2024 | 2024-03 | https://doi.org/10.1186/s12964-024-01545-6 |
| Imaging: CT | Multiphasic contrast CT sensitivity ~82%, specificity 96% for PanNET detection; ENETS-based imaging review recommends contrast-enhanced CT for diagnosis/staging/surveillance (sulciner2023surgicalmanagementof pages 2-5, pellegrino2023diagnosticmanagementof pages 2-4) | Sulciner 2023; Pellegrino 2023 | 2023-03; 2023-01 | https://doi.org/10.3390/cancers15072006 ; https://doi.org/10.3390/tomography9010018 |
| Imaging: MRI | MRI sensitivity 93%, specificity 88% in Sulciner review; MRI sensitivity for PanNET detection reported as 79% (range 54-100%) and mean sensitivity for liver metastases 91% (range 82-98%) in radiology review; DWI recommended for liver/pancreas evaluation (sulciner2023surgicalmanagementof pages 2-5, pellegrino2023diagnosticmanagementof pages 8-10) | Sulciner 2023; Pellegrino 2023 | 2023-03; 2023-01 | https://doi.org/10.3390/cancers15072006 ; https://doi.org/10.3390/tomography9010018 |
| Imaging: SSTR PET/CT | 68Ga-DOTATATE/DOTANOC PET/CT sensitivity 93%, specificity 91%; detection by grade ~95% for G1, 87.5% for G2, 37.5% for G3; broader SSTR PET review reports 68Ga/64Cu-DOTA-SSA PET/CT sensitivity 86-100% and specificity 79-100% for panNETs overall, but low sensitivity (~25%) for insulinoma (sulciner2023surgicalmanagementof pages 2-5, pellegrino2023diagnosticmanagementof pages 5-6, hope2023snmmiprocedurestandardeanm pages 4-5) | Sulciner 2023; Pellegrino 2023; Hope 2023 | 2023-03; 2023-01; 2023-02 | https://doi.org/10.3390/cancers15072006 ; https://doi.org/10.3390/tomography9010018 ; https://doi.org/10.2967/jnumed.122.264860 |
| Imaging: EUS | EUS mean sensitivity 75-97%; especially useful for lesions <2 cm; intraoperative ultrasound may detect up to 96% of tumors; separate radiology review reports EUS sensitivity 86% and specificity 92% for small PanNETs, and CT misses 68.4% of lesions <10 mm (sulciner2023surgicalmanagementof pages 2-5, pellegrino2023diagnosticmanagementof pages 11-13) | Sulciner 2023; Pellegrino 2023 | 2023-03; 2023-01 | https://doi.org/10.3390/cancers15072006 ; https://doi.org/10.3390/tomography9010018 |
| Surgery / surveillance | Increasing evidence supports active surveillance for small non-functional tumors <2 cm; MEN1-associated PanNETs <2 cm can safely undergo active surveillance (sulciner2023surgicalmanagementof pages 1-2, sulciner2023surgicalmanagementof pages 12-14) | Sulciner 2023 | 2023-03 | https://doi.org/10.3390/cancers15072006 |
| Neoadjuvant PRRT (NEOLUPANET) | Phase II NCT04385992: 31 enrolled; 26 completed 4 cycles of 177Lu-DOTATATE; partial response 18/31, stable disease 13/31, no progression; 29 underwent surgery; 24 R0 and 4 R1 resections; 1 unresectable due to vascular involvement; postoperative complications 21/29, severe complications 7/29, no postoperative deaths (partelli2024neoadjuvant177ludotatatefor pages 1-2, partelli2024neoadjuvant177ludotatatefor pages 2-3, NCT04385992 chunk 2) | Partelli 2024 | 2024-08 | https://doi.org/10.1093/bjs/znae178 |
| Temozolomide-based regimens | Systematic review/meta-analysis (14 studies, 441 patients): pooled ORR 41.2% (95% CI 32.4-50.6%), DCR 85.3% (95% CI 74.9-91.9%), >50% chromogranin A decline 44.9%; non-serious AEs 93.8%, serious AEs 23.7% (mainly hematologic) (taherifard2024efficacyandsafety pages 1-3) | Taherifard 2024 | 2024-02 | https://doi.org/10.1186/s12885-024-11926-2 |
| EUS-guided RFA | Meta-analysis: 19-20 studies, 183 patients, 196 lesions (101 functional, 95 non-functional); pooled clinical efficacy 95.1% (95% CI 91.2-98.9%) for functional PanNETs and 93.4% (95% CI 88.4-98.4%) for non-functional PanNETs; pooled AE rates 17.8% (95% CI 9.1-26.4%) and 24.6% (95% CI 7.4-41.8%), respectively (armellini2023efficacyandsafety pages 1-2, armellini2023efficacyandsafety pages 2-4) | Armellini 2023 | 2023-02 | https://doi.org/10.3390/medicina59020359 |
| Theragnostics / SSTR agents | Approved SSTR PET agents in guideline context: 68Ga-DOTATATE, 68Ga-DOTATOC, 64Cu-DOTATATE; SSTR PET used for initial staging, primary localization, PRRT selection, and post-PRRT assessment; radiology review notes PET spatial resolution superiority over SRS (0.5 cm vs 1.5 cm) (hope2023snmmiprocedurestandardeanm pages 4-5, hope2023snmmiprocedurestandardeanm pages 2-3, hope2023snmmiprocedurestandardeanm pages 3-4, pellegrino2023diagnosticmanagementof pages 5-6) | Hope 2023; Pellegrino 2023 | 2023-02; 2023-01 | https://doi.org/10.2967/jnumed.122.264860 ; https://doi.org/10.3390/tomography9010018 |


*Table: This table compiles the most decision-relevant identifiers, epidemiology, molecular features, imaging performance, and treatment outcomes for pancreatic neuroendocrine tumors from the retrieved 2023-2024 evidence. It is useful as a compact reference for populating structured disease knowledge base fields.*

---

## Limitations of this report (transparency)
- **ICD-10/ICD-11, MeSH, and Orphanet identifiers** for “pancreatic neuroendocrine tumor” were not directly retrievable via the tools and literature successfully accessed in this run; the report therefore provides partial ontology identifiers (MONDO subtypes) and recommends explicit ontology lookup for completion.
- **Environmental/protective factors** and **gene–environment interactions** were not supported by the retrieved evidence set.
- Detailed phenotype frequencies by functional subtype (beyond ≈30% functioning) were not available in the retrieved sources and would require additional dedicated epidemiologic/registry papers.


References

1. (sulciner2023surgicalmanagementof pages 1-2): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 42 citations.

2. (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3): Nektaria Papadopoulou-Marketou, Marina Tsoli, Eleftherios Chatzellis, Krystallenia I. Alexandraki, and Gregory Kaltsas. Hereditary syndromes associated with pancreatic and lung neuroendocrine tumors. Cancers, 16:2075, May 2024. URL: https://doi.org/10.3390/cancers16112075, doi:10.3390/cancers16112075. This article has 16 citations.

3. (hope2023snmmiprocedurestandardeanm pages 1-2): Thomas A. Hope, Martin Allen-Auerbach, Lisa Bodei, Jeremie Calais, Magnus Dahlbom, Lisa K. Dunnwald, Michael M. Graham, Heather A. Jacene, Courtney Lawhn Heath, Erik S. Mittra, Chadwick L. Wright, Wolfgang P. Fendler, Ken Herrmann, David Taïeb, and Andreas Kjaer. Snmmi procedure standard/eanm practice guideline for sstr pet: imaging neuroendocrine tumors. The Journal of Nuclear Medicine, 64:204-210, Feb 2023. URL: https://doi.org/10.2967/jnumed.122.264860, doi:10.2967/jnumed.122.264860. This article has 124 citations.

4. (sulciner2023surgicalmanagementof pages 2-5): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 42 citations.

5. (andersen2024welldifferentiatedg1and pages 1-2): Kirstine Øster Andersen, Sönke Detlefsen, Klaus Brusgaard, and Henrik Thybo Christesen. Well-differentiated g1 and g2 pancreatic neuroendocrine tumors: a meta-analysis of published expanded dna sequencing data. Frontiers in Endocrinology, May 2024. URL: https://doi.org/10.3389/fendo.2024.1351624, doi:10.3389/fendo.2024.1351624. This article has 10 citations.

6. (taherifard2024efficacyandsafety pages 1-3): Erfan Taherifard, Muhammad Bakhtiar, Mahnoor Mahnoor, Rabeea Ahmed, Ludimila Cavalcante, Janie Zhang, and Anwaar Saeed. Efficacy and safety of temozolomide-based regimens in advanced pancreatic neuroendocrine tumors: a systematic review and meta-analysis. BMC Cancer, Feb 2024. URL: https://doi.org/10.1186/s12885-024-11926-2, doi:10.1186/s12885-024-11926-2. This article has 10 citations and is from a peer-reviewed journal.

7. (partelli2024neoadjuvant177ludotatatefor pages 1-2): Stefano Partelli, Luca Landoni, Mirco Bartolomei, Alessandro Zerbi, Chiara Maria Grana, Ugo Boggi, Giovanni Butturini, Riccardo Casadei, Roberto Salvia, and Massimo Falconi. Neoadjuvant 177lu-dotatate for non-functioning pancreatic neuroendocrine tumours (neolupanet): multicentre phase ii study. The British Journal of Surgery, Aug 2024. URL: https://doi.org/10.1093/bjs/znae178, doi:10.1093/bjs/znae178. This article has 35 citations.

8. (jiang2024multiregionwesof pages 1-2): Yu Jiang, Yi-han Dong, Shi-wei Zhao, Dong-yu Liu, Ji-yang Zhang, Xiao-ya Xu, Hao Chen, Hao Chen, and Jia-bin Jin. Multiregion wes of metastatic pancreatic neuroendocrine tumors revealed heterogeneity in genomic alterations, immune microenvironment and evolutionary patterns. Cell Communication and Signaling : CCS, Mar 2024. URL: https://doi.org/10.1186/s12964-024-01545-6, doi:10.1186/s12964-024-01545-6. This article has 8 citations.

9. (papadopouloumarketou2024hereditarysyndromesassociated pages 14-16): Nektaria Papadopoulou-Marketou, Marina Tsoli, Eleftherios Chatzellis, Krystallenia I. Alexandraki, and Gregory Kaltsas. Hereditary syndromes associated with pancreatic and lung neuroendocrine tumors. Cancers, 16:2075, May 2024. URL: https://doi.org/10.3390/cancers16112075, doi:10.3390/cancers16112075. This article has 16 citations.

10. (papadopouloumarketou2024hereditarysyndromesassociated pages 4-6): Nektaria Papadopoulou-Marketou, Marina Tsoli, Eleftherios Chatzellis, Krystallenia I. Alexandraki, and Gregory Kaltsas. Hereditary syndromes associated with pancreatic and lung neuroendocrine tumors. Cancers, 16:2075, May 2024. URL: https://doi.org/10.3390/cancers16112075, doi:10.3390/cancers16112075. This article has 16 citations.

11. (jiang2024multiregionwesof pages 7-12): Yu Jiang, Yi-han Dong, Shi-wei Zhao, Dong-yu Liu, Ji-yang Zhang, Xiao-ya Xu, Hao Chen, Hao Chen, and Jia-bin Jin. Multiregion wes of metastatic pancreatic neuroendocrine tumors revealed heterogeneity in genomic alterations, immune microenvironment and evolutionary patterns. Cell Communication and Signaling : CCS, Mar 2024. URL: https://doi.org/10.1186/s12964-024-01545-6, doi:10.1186/s12964-024-01545-6. This article has 8 citations.

12. (pellegrino2023diagnosticmanagementof pages 5-6): Fabio Pellegrino, Vincenza Granata, Roberta Fusco, Francesca Grassi, Salvatore Tafuto, Luca Perrucci, Giulia Tralli, and Mariano Scaglione. Diagnostic management of gastroenteropancreatic neuroendocrine neoplasms: technique optimization and tips and tricks for radiologists. Tomography, 9:217-246, Jan 2023. URL: https://doi.org/10.3390/tomography9010018, doi:10.3390/tomography9010018. This article has 22 citations.

13. (sulciner2023surgicalmanagementof pages 12-14): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 42 citations.

14. (papadopouloumarketou2024hereditarysyndromesassociated pages 3-4): Nektaria Papadopoulou-Marketou, Marina Tsoli, Eleftherios Chatzellis, Krystallenia I. Alexandraki, and Gregory Kaltsas. Hereditary syndromes associated with pancreatic and lung neuroendocrine tumors. Cancers, 16:2075, May 2024. URL: https://doi.org/10.3390/cancers16112075, doi:10.3390/cancers16112075. This article has 16 citations.

15. (pellegrino2023diagnosticmanagementof pages 1-2): Fabio Pellegrino, Vincenza Granata, Roberta Fusco, Francesca Grassi, Salvatore Tafuto, Luca Perrucci, Giulia Tralli, and Mariano Scaglione. Diagnostic management of gastroenteropancreatic neuroendocrine neoplasms: technique optimization and tips and tricks for radiologists. Tomography, 9:217-246, Jan 2023. URL: https://doi.org/10.3390/tomography9010018, doi:10.3390/tomography9010018. This article has 22 citations.

16. (pellegrino2023diagnosticmanagementof pages 11-13): Fabio Pellegrino, Vincenza Granata, Roberta Fusco, Francesca Grassi, Salvatore Tafuto, Luca Perrucci, Giulia Tralli, and Mariano Scaglione. Diagnostic management of gastroenteropancreatic neuroendocrine neoplasms: technique optimization and tips and tricks for radiologists. Tomography, 9:217-246, Jan 2023. URL: https://doi.org/10.3390/tomography9010018, doi:10.3390/tomography9010018. This article has 22 citations.

17. (hope2023snmmiprocedurestandardeanm pages 2-3): Thomas A. Hope, Martin Allen-Auerbach, Lisa Bodei, Jeremie Calais, Magnus Dahlbom, Lisa K. Dunnwald, Michael M. Graham, Heather A. Jacene, Courtney Lawhn Heath, Erik S. Mittra, Chadwick L. Wright, Wolfgang P. Fendler, Ken Herrmann, David Taïeb, and Andreas Kjaer. Snmmi procedure standard/eanm practice guideline for sstr pet: imaging neuroendocrine tumors. The Journal of Nuclear Medicine, 64:204-210, Feb 2023. URL: https://doi.org/10.2967/jnumed.122.264860, doi:10.2967/jnumed.122.264860. This article has 124 citations.

18. (hope2023snmmiprocedurestandardeanm pages 3-4): Thomas A. Hope, Martin Allen-Auerbach, Lisa Bodei, Jeremie Calais, Magnus Dahlbom, Lisa K. Dunnwald, Michael M. Graham, Heather A. Jacene, Courtney Lawhn Heath, Erik S. Mittra, Chadwick L. Wright, Wolfgang P. Fendler, Ken Herrmann, David Taïeb, and Andreas Kjaer. Snmmi procedure standard/eanm practice guideline for sstr pet: imaging neuroendocrine tumors. The Journal of Nuclear Medicine, 64:204-210, Feb 2023. URL: https://doi.org/10.2967/jnumed.122.264860, doi:10.2967/jnumed.122.264860. This article has 124 citations.

19. (hope2023snmmiprocedurestandardeanm pages 5-6): Thomas A. Hope, Martin Allen-Auerbach, Lisa Bodei, Jeremie Calais, Magnus Dahlbom, Lisa K. Dunnwald, Michael M. Graham, Heather A. Jacene, Courtney Lawhn Heath, Erik S. Mittra, Chadwick L. Wright, Wolfgang P. Fendler, Ken Herrmann, David Taïeb, and Andreas Kjaer. Snmmi procedure standard/eanm practice guideline for sstr pet: imaging neuroendocrine tumors. The Journal of Nuclear Medicine, 64:204-210, Feb 2023. URL: https://doi.org/10.2967/jnumed.122.264860, doi:10.2967/jnumed.122.264860. This article has 124 citations.

20. (sulciner2023surgicalmanagementof pages 10-11): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 42 citations.

21. (NCT04385992 chunk 2): Massimo Falconi. Neoadjuvant PRRT With 177Lu-DOTATATE Followed by Surgery for Resectable PanNET. IRCCS San Raffaele. 2020. ClinicalTrials.gov Identifier: NCT04385992

22. (NCT04385992 chunk 1): Massimo Falconi. Neoadjuvant PRRT With 177Lu-DOTATATE Followed by Surgery for Resectable PanNET. IRCCS San Raffaele. 2020. ClinicalTrials.gov Identifier: NCT04385992

23. (partelli2024neoadjuvant177ludotatatefor media 37188ff4): Stefano Partelli, Luca Landoni, Mirco Bartolomei, Alessandro Zerbi, Chiara Maria Grana, Ugo Boggi, Giovanni Butturini, Riccardo Casadei, Roberto Salvia, and Massimo Falconi. Neoadjuvant 177lu-dotatate for non-functioning pancreatic neuroendocrine tumours (neolupanet): multicentre phase ii study. The British Journal of Surgery, Aug 2024. URL: https://doi.org/10.1093/bjs/znae178, doi:10.1093/bjs/znae178. This article has 35 citations.

24. (partelli2024neoadjuvant177ludotatatefor media 7fe3253e): Stefano Partelli, Luca Landoni, Mirco Bartolomei, Alessandro Zerbi, Chiara Maria Grana, Ugo Boggi, Giovanni Butturini, Riccardo Casadei, Roberto Salvia, and Massimo Falconi. Neoadjuvant 177lu-dotatate for non-functioning pancreatic neuroendocrine tumours (neolupanet): multicentre phase ii study. The British Journal of Surgery, Aug 2024. URL: https://doi.org/10.1093/bjs/znae178, doi:10.1093/bjs/znae178. This article has 35 citations.

25. (partelli2024neoadjuvant177ludotatatefor media 8fe1b3ff): Stefano Partelli, Luca Landoni, Mirco Bartolomei, Alessandro Zerbi, Chiara Maria Grana, Ugo Boggi, Giovanni Butturini, Riccardo Casadei, Roberto Salvia, and Massimo Falconi. Neoadjuvant 177lu-dotatate for non-functioning pancreatic neuroendocrine tumours (neolupanet): multicentre phase ii study. The British Journal of Surgery, Aug 2024. URL: https://doi.org/10.1093/bjs/znae178, doi:10.1093/bjs/znae178. This article has 35 citations.

26. (piscopo2023diagnosismanagementand pages 2-4): Leandra Piscopo, Emilia Zampella, Sara Pellegrino, Fabio Volpe, Carmela Nappi, Valeria Gaudieri, Rosa Fonti, Silvana Del Vecchio, Alberto Cuocolo, and Michele Klain. Diagnosis, management and theragnostic approach of gastro-entero-pancreatic neuroendocrine neoplasms. Cancers, 15:3483, Jul 2023. URL: https://doi.org/10.3390/cancers15133483, doi:10.3390/cancers15133483. This article has 14 citations.

27. (armellini2023efficacyandsafety pages 1-2): Elia Armellini, Antonio Facciorusso, and Stefano Francesco Crinò. Efficacy and safety of endoscopic ultrasound-guided radiofrequency ablation for pancreatic neuroendocrine tumors: a systematic review and metanalysis. Medicina, 59:359, Feb 2023. URL: https://doi.org/10.3390/medicina59020359, doi:10.3390/medicina59020359. This article has 63 citations.

28. (jiang2024multiregionwesof pages 4-5): Yu Jiang, Yi-han Dong, Shi-wei Zhao, Dong-yu Liu, Ji-yang Zhang, Xiao-ya Xu, Hao Chen, Hao Chen, and Jia-bin Jin. Multiregion wes of metastatic pancreatic neuroendocrine tumors revealed heterogeneity in genomic alterations, immune microenvironment and evolutionary patterns. Cell Communication and Signaling : CCS, Mar 2024. URL: https://doi.org/10.1186/s12964-024-01545-6, doi:10.1186/s12964-024-01545-6. This article has 8 citations.

29. (pellegrino2023diagnosticmanagementof pages 2-4): Fabio Pellegrino, Vincenza Granata, Roberta Fusco, Francesca Grassi, Salvatore Tafuto, Luca Perrucci, Giulia Tralli, and Mariano Scaglione. Diagnostic management of gastroenteropancreatic neuroendocrine neoplasms: technique optimization and tips and tricks for radiologists. Tomography, 9:217-246, Jan 2023. URL: https://doi.org/10.3390/tomography9010018, doi:10.3390/tomography9010018. This article has 22 citations.

30. (pellegrino2023diagnosticmanagementof pages 8-10): Fabio Pellegrino, Vincenza Granata, Roberta Fusco, Francesca Grassi, Salvatore Tafuto, Luca Perrucci, Giulia Tralli, and Mariano Scaglione. Diagnostic management of gastroenteropancreatic neuroendocrine neoplasms: technique optimization and tips and tricks for radiologists. Tomography, 9:217-246, Jan 2023. URL: https://doi.org/10.3390/tomography9010018, doi:10.3390/tomography9010018. This article has 22 citations.

31. (hope2023snmmiprocedurestandardeanm pages 4-5): Thomas A. Hope, Martin Allen-Auerbach, Lisa Bodei, Jeremie Calais, Magnus Dahlbom, Lisa K. Dunnwald, Michael M. Graham, Heather A. Jacene, Courtney Lawhn Heath, Erik S. Mittra, Chadwick L. Wright, Wolfgang P. Fendler, Ken Herrmann, David Taïeb, and Andreas Kjaer. Snmmi procedure standard/eanm practice guideline for sstr pet: imaging neuroendocrine tumors. The Journal of Nuclear Medicine, 64:204-210, Feb 2023. URL: https://doi.org/10.2967/jnumed.122.264860, doi:10.2967/jnumed.122.264860. This article has 124 citations.

32. (partelli2024neoadjuvant177ludotatatefor pages 2-3): Stefano Partelli, Luca Landoni, Mirco Bartolomei, Alessandro Zerbi, Chiara Maria Grana, Ugo Boggi, Giovanni Butturini, Riccardo Casadei, Roberto Salvia, and Massimo Falconi. Neoadjuvant 177lu-dotatate for non-functioning pancreatic neuroendocrine tumours (neolupanet): multicentre phase ii study. The British Journal of Surgery, Aug 2024. URL: https://doi.org/10.1093/bjs/znae178, doi:10.1093/bjs/znae178. This article has 35 citations.

33. (armellini2023efficacyandsafety pages 2-4): Elia Armellini, Antonio Facciorusso, and Stefano Francesco Crinò. Efficacy and safety of endoscopic ultrasound-guided radiofrequency ablation for pancreatic neuroendocrine tumors: a systematic review and metanalysis. Medicina, 59:359, Feb 2023. URL: https://doi.org/10.3390/medicina59020359, doi:10.3390/medicina59020359. This article has 63 citations.

---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T08:45:49.277067'
end_time: '2026-05-09T09:03:43.913246'
duration_seconds: 1074.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Non-functional Pancreatic Neuroendocrine Tumor
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Non-functional Pancreatic Neuroendocrine Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Non-functional Pancreatic Neuroendocrine Tumor** covering all of the
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
- **Disease Name:** Non-functional Pancreatic Neuroendocrine Tumor
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Non-functional Pancreatic Neuroendocrine Tumor** covering all of the
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


# Comprehensive Research Report: Non-functional Pancreatic Neuroendocrine Tumor (NF‑pNET / NF‑PanNET)

## Target Disease
- **Disease name:** Non-functional pancreatic neuroendocrine tumor (NF‑pNET; NF‑PanNET)
- **MONDO ID:** **MONDO:0004334** (disease-level identifier retrieved via Open Targets) (OpenTargets Search: pancreatic neuroendocrine tumor)
- **Category:** Pancreatic neuroendocrine neoplasm; typically **well-differentiated pancreatic neuroendocrine tumor (PanNET)** subtype in WHO-aligned frameworks (saleh2024pancreaticneuroendocrinetumors pages 1-2, battistella2024recentdevelopmentsin pages 1-6)

## Summary of key points (current understanding)
Non-functional PanNETs are pancreatic neuroendocrine tumors that do not present with a clinical hormone hypersecretion syndrome and therefore often present incidentally or late with mass effect and/or metastatic disease; they constitute a majority of pancreatic neuroendocrine neoplasms in contemporary series (often detected via high-quality cross-sectional imaging). Diagnosis relies on multimodal anatomical + functional imaging (especially SSTR PET) and pathology with Ki‑67 grading. Management is risk-stratified: **active surveillance** is accepted for carefully selected small (≤2 cm) low-risk lesions, while surgery is standard for higher-risk localized disease. For advanced disease, standard systemic options include somatostatin analogues (SSA), targeted therapy (everolimus, sunitinib), cytotoxic chemotherapy (CAPTEM), and peptide receptor radionuclide therapy (PRRT) for SSTR-positive tumors; sequencing is individualized by grade, tempo, tumor burden, and SSTR/FDG imaging phenotype (sulciner2023surgicalmanagementof pages 10-11, sulciner2023surgicalmanagementof pages 2-5, castillon2023seomgetneclinicalguidelines pages 9-10, melhorn2024treatmentsequencingin pages 2-3).

| Disease | MONDO ID | Disease category | Key synonyms / alternative names | Classification / grading notes | Citations |
|---|---|---|---|---|---|
| Non-functional pancreatic neuroendocrine tumor | MONDO:0004334 | Well-differentiated pancreatic neuroendocrine tumor (PanNET/PNET) subtype; pancreatic neuroendocrine neoplasm lacking a clinical hormone hypersecretion syndrome | Non-functional pancreatic neuroendocrine tumor; nonfunctioning pancreatic neuroendocrine tumor; NF-pNET; NF-PanNET; nonfunctional PanNET; non-secreting pancreatic neuroendocrine tumor | WHO 2022 framework distinguishes well-differentiated PanNET from poorly differentiated pancreatic neuroendocrine carcinoma (PanNEC); NF-pNET belongs to the well-differentiated PanNET group rather than PanNEC. Nonfunctional tumors comprise the majority of PanNENs / PanNETs in recent reviews. | (OpenTargets Search: pancreatic neuroendocrine tumor, saleh2024pancreaticneuroendocrinetumors pages 1-2, battistella2024recentdevelopmentsin pages 1-6) |
| PanNET grading (applies to NF-pNET when well-differentiated) | — | Histologic grade within well-differentiated PanNET | G1 PanNET; G2 PanNET; G3 well-differentiated PanNET | Ki-67 / mitotic thresholds summarized in recent reviews: G1 = Ki-67 <3% and mitoses <2; G2 = Ki-67 3-20% and/or mitoses 2-20; G3 = Ki-67 >20% and/or mitoses >20. Current taxonomy separates well-differentiated G3 PanNET from poorly differentiated NEC. | (sulciner2023surgicalmanagementof pages 1-2, saleh2024pancreaticneuroendocrinetumors pages 1-2) |
| PanNEC (important differential classification) | — | Poorly differentiated pancreatic neuroendocrine carcinoma | Pancreatic NEC; poorly differentiated pancreatic neuroendocrine carcinoma | Molecularly and pathologically distinct from PanNET; recent reviews note PanNEC commonly shows TP53 and RB1 alterations, whereas PanNET more often shows MEN1, DAXX, ATRX alterations. This distinction is critical because a high Ki-67 alone does not automatically indicate NEC if morphology is well differentiated. | (battistella2024recentdevelopmentsin pages 16-20, saleh2024pancreaticneuroendocrinetumors pages 1-2, castillon2023seomgetneclinicalguidelines pages 2-4) |
| Hereditary / predisposition context relevant to NF-pNET | — | Often sporadic, but can occur in hereditary cancer syndromes | MEN1-associated PanNET; VHL-associated PanNET; NF1-associated PanNET; TSC-associated PanNET | Most PanNETs are sporadic, but ~10% are associated with germline syndromes in some reviews; a 2024 hereditary-syndrome review reports ~17% of PanNETs occur in inherited syndromes. VHL-associated PanNETs are described as almost exclusively nonfunctioning. | (sulciner2023surgicalmanagementof pages 1-2, saleh2024pancreaticneuroendocrinetumors pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 1-3) |


*Table: This table summarizes standardized identifiers, common synonyms, and the core classification framework for non-functional pancreatic neuroendocrine tumor. It is useful for harmonizing disease labels in a knowledge base and for distinguishing well-differentiated NF-pNET from pancreatic NEC under WHO 2022-aligned grading concepts.*

---

## 1. Disease information
### 1.1 Definition / overview
- Pancreatic neuroendocrine tumors (PanNET/PNET) are rare pancreatic malignancies (≈2% of pancreatic neoplasms in a 2023 surgical review) and are classified clinically into functional versus non-functional based on hormone-related syndromes; nonfunctional tumors are a major fraction and are increasingly detected when small and asymptomatic (sulciner2023surgicalmanagementof pages 1-2).
- A 2024 diagnostic review states that **non-functioning PanNENs account for “the vast majority of PanNENs (60–90%)”** and frequently produce non-specific symptoms leading to delayed detection; at diagnosis, **“Overall, 12–74% of PanNENs have distant metastases, mainly hepatic.”** (Expert Review of Gastroenterology & Hepatology; published May 2024; https://doi.org/10.1080/17474124.2024.2342837) (battistella2024recentdevelopmentsin pages 1-6).

### 1.2 Key identifiers
- **MONDO:** MONDO:0004334 (OpenTargets Search: pancreatic neuroendocrine tumor)
- **Other identifiers (OMIM/Orphanet/ICD‑10/ICD‑11/MeSH):** Not extracted from the available retrieved sources in this run; additional database queries would be required for a complete identifier crosswalk.

### 1.3 Synonyms / alternative names
Commonly used synonyms include: **nonfunctioning pancreatic neuroendocrine tumor**, **nonfunctional PanNET**, **NF‑pNET**, and **NF‑PanNET** (sulciner2023surgicalmanagementof pages 1-2, battistella2024recentdevelopmentsin pages 1-6).

### 1.4 Source type (patient-level vs aggregated)
The characterization above derives from aggregated sources (systematic reviews/guidelines and multi-center cohorts) rather than individual EHR records (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3, battistella2024recentdevelopmentsin pages 1-6, sulciner2023surgicalmanagementof pages 10-11).

---

## 2. Etiology
### 2.1 Disease causal factors (mechanistic)
NF‑PanNETs are neoplastic proliferations of pancreatic neuroendocrine cells characterized by recurrent alterations in chromatin regulators (MEN1/ATRX/DAXX) and signaling pathways including PI3K‑AKT‑mTOR; the biology is distinct from poorly differentiated pancreatic neuroendocrine carcinoma (PanNEC), which more often harbors TP53/RB1 alterations (saleh2024pancreaticneuroendocrinetumors pages 1-2, castillon2023seomgetneclinicalguidelines pages 2-4).

### 2.2 Risk factors
#### 2.2.1 Genetic predisposition / hereditary syndromes
- A 2023 review reports that **~10%** of PanNETs arise in the context of inherited predisposition syndromes (MEN1, VHL, TSC1/TSC2, NF1) (Cancers; published Mar 2023; https://doi.org/10.3390/cancers15072006) (sulciner2023surgicalmanagementof pages 1-2).
- A 2024 systematic review focused on hereditary syndromes reports **“approximately 17% of PanNETs”** develop in monogenic syndromes, especially **MEN1**, and also **VHL, NF1, TSC**, and **MEN4** (Cancers; published May 2024; https://doi.org/10.3390/cancers16112075) (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).
  - The same review notes phenotype patterns important for the non-functional subtype: **VHL-associated PanNETs are “almost exclusively nonfunctioning.”** (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).
  - The review emphasizes early detection: **genetic screening is recommended in childhood** and **diagnostic surveillance often begins in adolescence**, including in asymptomatic carriers (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

#### 2.2.2 Non-genetic / metabolic risk associations
A 2026 review describes a bidirectional association between metabolic comorbidities (diabetes, obesity, metabolic syndrome) and gastroenteropancreatic neuroendocrine neoplasms, suggesting mechanistic links that may influence risk (conzo2026pancreaticneuroendocrinetumors pages 2-4).

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not identified in the retrieved evidence.

---

## 3. Phenotypes (clinical presentation)
### 3.1 Typical phenotype spectrum
- NF‑PanNETs often present without hormone syndromes and can be discovered incidentally during imaging; nonspecific symptoms may include abdominal pain or weight loss or symptoms due to mass effect/obstruction and metastasis (battistella2024recentdevelopmentsin pages 1-6, sulciner2023surgicalmanagementof pages 2-5).
- The presence of distant metastasis at diagnosis is reported across PanNEN series (wide range 12–74% reported, mainly hepatic) (battistella2024recentdevelopmentsin pages 1-6).

### 3.2 Phenotype characteristics (suggested HPO terms)
Because frequency-by-symptom data were not systematically extracted in the retrieved sources, the list below is intended for knowledge-base mapping and may require validation against additional primary cohorts:
- **Abdominal pain** — HP:0002027 (often nonspecific) (battistella2024recentdevelopmentsin pages 1-6)
- **Unintentional weight loss** — HP:0001824 (typical of malignancy; not quantified here)
- **Jaundice** (if bile duct obstruction) — HP:0000952 (not quantified here)
- **Hepatic metastases** — HP:0002897 (as a complication/metastatic phenotype; frequency range given for PanNENs broadly) (battistella2024recentdevelopmentsin pages 1-6)

### 3.3 Quality of life impact
Quality-of-life instruments are explicitly incorporated as outcomes in key trials of advanced disease (e.g., EORTC QLQ-C30 in NCT02358356; see Treatment section), indicating recognized QoL burden, but disease-specific QoL effect sizes were not extracted from mature trial publications in the current evidence set (NCT02358356 chunk 1).

---

## 4. Genetic / molecular information
### 4.1 Causal genes / recurrent drivers (somatic and germline)
NF‑PanNETs are not typically “single-gene” Mendelian disorders, but they show recurrent **somatic** driver alterations and may occur in **germline** syndromes.

#### 4.1.1 Somatic driver landscape (recent quantitative synthesis)
A 2024 systematic review/meta-analysis of expanded sequencing datasets (14 datasets; **221 patients; 225 G1/G2 PanNETs**) reported (Frontiers in Endocrinology; published May 2024; https://doi.org/10.3389/fendo.2024.1351624):
- Tumor composition: **72.0% sporadic**, **13.3% hereditary**, **14.7% unknown germline status**.
- Most frequently altered gene: **MEN1 altered in 42% overall (95/225)**; enriched in hereditary tumors (57%) versus sporadic (36%).
- Other frequent alterations: **DAXX 16% (37/225)**, **ATRX 12% (27/225)**.
- **DAXX mutations were more frequent in MEN1-mutant tumors (p<0.05)**.
- Importantly for non-functional tumors, the authors found **non-functioning PanNETs had more recurrent variations in genes associated with PI3K, Wnt, NOTCH, and RTK–RAS pathways** than functioning tumors (andersen2024welldifferentiatedg1and pages 1-2).

#### 4.1.2 Germline predisposition genes/syndromes
Key syndromic genes include **MEN1**, **VHL**, **NF1**, **TSC1/TSC2** (and less commonly **CDKN1B/MEN4**), with earlier onset and multifocality common in inherited cases (sulciner2023surgicalmanagementof pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

### 4.2 Epigenetic information
- A 2023 review highlights that PanNETs have relatively low mutational burden and argues epigenetic regulators contribute to tumorigenesis; it states that drivers “MEN1, ATRX… and DAXX… are found in ~40% of sporadic PNETs” and reviews methylome-based clustering for prognosis (Endocrine Oncology; published 2023; https://doi.org/10.1530/eo-23-0003) (maluchenko2024molecularbasisof pages 17-18).
- A 2024 review of signaling and epigenetics emphasizes that “epigenetic modifications encompass … DNA methylation, histone modifications, and non-coding RNAs (ncRNAs)” and notes “a lack of extensive research on epigenetic regulation in PNETs,” supporting ongoing research needs (International Journal of Molecular Sciences; published Jan 2024; https://doi.org/10.3390/ijms25021331) (saleh2024pancreaticneuroendocrinetumors pages 1-2).

### 4.3 Chromosomal / structural abnormalities
Not extracted from the retrieved evidence.

### 4.4 Suggested GO biological process terms (mechanism-linked)
Based on pathway emphasis in recent reviews and sequencing meta-analysis (to be refined for a knowledge base):
- **mTOR signaling** — GO:0031929 (supported by mTOR-pathway alteration discussions) (battistella2024recentdevelopmentsin pages 16-20, saleh2024pancreaticneuroendocrinetumors pages 1-2)
- **Chromatin organization / remodeling** — GO:0006325 / GO:0006338 (MEN1/ATRX/DAXX involvement) (andersen2024welldifferentiatedg1and pages 1-2, saleh2024pancreaticneuroendocrinetumors pages 1-2)
- **DNA damage response** — GO:0006974 (ATRX functions and genome integrity context) (saleh2024pancreaticneuroendocrinetumors pages 1-2)

---

## 5. Mechanism / pathophysiology
### 5.1 Causal chain (high-level)
1) **Initiating alterations**: sporadic somatic mutations (MEN1, DAXX, ATRX) and pathway dysregulation (PI3K‑AKT‑mTOR and others) or germline predisposition (MEN1/VHL/NF1/TSC) (andersen2024welldifferentiatedg1and pages 1-2, saleh2024pancreaticneuroendocrinetumors pages 1-2, papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).
2) **Cellular consequences**: altered chromatin regulation, proliferative signaling, and tumor heterogeneity; epigenetic remodeling and methylome alterations contribute to subtype differences and behavior (saleh2024pancreaticneuroendocrinetumors pages 1-2, maluchenko2024molecularbasisof pages 17-18).
3) **Clinical manifestations**: non-functional status leads to fewer early warning symptoms, increasing incidental detection or delayed presentation; progression leads to local mass effects and metastasis (often liver) (battistella2024recentdevelopmentsin pages 1-6, sulciner2023surgicalmanagementof pages 2-5).

### 5.2 Immune system involvement
A 2024 proteogenomic PanNET study (iScience) indicates aggressive subtypes can have immune/hypoxia signatures (study retrieved but not deeply extracted in evidence snippets here); thus immune microenvironment is a research focus but not yet a routine clinical biomarker in the provided evidence set (battistella2024recentdevelopmentsin pages 1-6).

### 5.3 Suggested cell-type (CL) terms
- **Pancreatic endocrine cell** — CL:0000169 (tumor origin at islet/endocrine lineage level; general PanNET concept) (battistella2024recentdevelopmentsin pages 1-6)
- **Neuroendocrine cell** — CL:0000165 (broad neuroendocrine lineage)

---

## 6. Anatomical structures affected
### 6.1 Primary / metastatic sites (UBERON suggestions)
- **Pancreas** — UBERON:0001264 (primary site)
- **Liver** — UBERON:0002107 (dominant metastatic site; hepatic metastases emphasized) (battistella2024recentdevelopmentsin pages 1-6)

### 6.2 Subcellular / compartment involvement (GO-CC suggestions)
- **Nucleus** — GO:0005634 (chromatin regulators MEN1/ATRX/DAXX)
- **Chromatin** — GO:0000785

---

## 7. Diagnostics (current applications and real-world implementations)
A multimodal strategy is standard. A 2024 diagnostic review summarizes: “PanNENs diagnostic work-up mainly relies on biochemical markers, pathological examination, and imaging evaluation,” including CT/MRI, SSTR PET and FDG PET, plus EUS with tissue procedures (battistella2024recentdevelopmentsin pages 1-6).

| Modality | Key performance / diagnostic yield | Main use-cases in NF-PanNET | Key limitations / caveats | Citations |
|---|---|---|---|---|
| Contrast-enhanced CT | Sensitivity ~82%; specificity 96% | First-line anatomical imaging; localization of primary tumor; staging; assessment of arterial-phase hyperenhancement and metastatic spread | May miss very small lesions; less sensitive than MRI for some liver metastases; limited grading information | (sulciner2023surgicalmanagementof pages 2-5, sulciner2023surgicalmanagementof media 0ba4a3b1, sulciner2023surgicalmanagementof media 7d24a64d, sulciner2023surgicalmanagementof media 210f90c9) |
| MRI | Sensitivity 93%; specificity 88% | High-sensitivity cross-sectional imaging; particularly useful for pancreas lesion characterization and liver metastasis detection | Availability/cost; still limited for definitive grading; may require complementary functional imaging | (sulciner2023surgicalmanagementof pages 2-5, sulciner2023surgicalmanagementof media 0ba4a3b1, sulciner2023surgicalmanagementof media 7d24a64d, sulciner2023surgicalmanagementof media 210f90c9) |
| 68Ga-DOTATATE PET/CT | Sensitivity 93%; specificity 91%; detection reported ~95% for G1 and ~87.5% for G2 tumors, but only ~37.5% for G3 tumors | Preferred somatostatin-receptor imaging for well-differentiated/SSTR-positive NF-PanNET; whole-body staging; occult lesion detection; therapy selection for SSA/PRRT | Lower yield in higher-grade tumors; receptor-positive uptake is not entirely specific; should be integrated with morphology and grade | (sulciner2023surgicalmanagementof pages 2-5, sulciner2023surgicalmanagementof media 0ba4a3b1, sulciner2023surgicalmanagementof media 7d24a64d, sulciner2023surgicalmanagementof media 210f90c9, battistella2024recentdevelopmentsin pages 20-26, battistella2024recentdevelopmentsin pages 1-6) |
| 18F-FDG PET/CT | No sensitivity/specificity metric provided in the extracted evidence; recommended in combination with 68Ga-DOTA-peptide PET for comprehensive assessment | Complements SSTR imaging; especially useful when tumor biology is more aggressive or higher grade is suspected | Less emphasized for low-grade well-differentiated NF-PanNET than SSTR PET; evidence here is recommendation-based rather than metric-based | (battistella2024recentdevelopmentsin pages 20-26, battistella2024recentdevelopmentsin pages 1-6) |
| EUS | Mean sensitivity 75–97%; especially sensitive for lesions <2 cm | Highest-sensitivity modality for small pancreatic lesions; local staging; nodal assessment; platform for tissue acquisition | Operator dependence; invasive; may still require adjunct imaging for whole-body staging | (sulciner2023surgicalmanagementof pages 2-5, sulciner2023surgicalmanagementof media 0ba4a3b1, sulciner2023surgicalmanagementof media 7d24a64d, sulciner2023surgicalmanagementof media 210f90c9, battistella2024recentdevelopmentsin pages 20-26) |
| EUS-FNA | In small lesions, tumor differentiation obtainable in 26.4% and Ki-67 in 20.1% of cases | Cytologic confirmation when pathology will change management; preoperative diagnosis and preliminary grading | Sampling error and intratumoral heterogeneity can underestimate grade; limited Ki-67 reliability in small samples | (sulciner2023surgicalmanagementof pages 2-5, conzo2026pancreaticneuroendocrinetumors pages 5-7) |
| EUS-FNB (core biopsy) | No pooled sensitivity/specificity provided in extracted evidence; reported to improve grading accuracy and Ki-67 reliability versus cytology alone | Preferred over FNA when histologic architecture, biomarkers, or more reliable grading are needed for management decisions in NF-PanNET | Discordance with resection specimen can persist; heterogeneity still limits accuracy; invasive procedure | (conzo2026pancreaticneuroendocrinetumors pages 5-7) |
| Pathology / IHC | Essential markers: synaptophysin, chromogranin A, Ki-67; Ki-67 central for WHO grade assignment | Confirms neuroendocrine differentiation and provides grading; distinguishes well-differentiated PanNET from NEC in context of morphology and ancillary markers | Biopsy-based Ki-67 may under- or overestimate true grade; interpretation depends on sample adequacy and heterogeneity | (conzo2026pancreaticneuroendocrinetumors pages 5-7) |
| Multimodal imaging strategy | Recommendation-based rather than a single metric: combined 68Ga-DOTA-peptide PET plus 18F-FDG PET is recommended for comprehensive assessment | Integrates receptor status and tumor biology; supports staging, grading context, and treatment planning | Requires access to advanced imaging and expert interpretation; cost and standardization remain issues | (battistella2024recentdevelopmentsin pages 20-26, battistella2024recentdevelopmentsin pages 1-6) |


*Table: This table summarizes the main diagnostic tools used for non-functional pancreatic neuroendocrine tumors, including reported imaging performance metrics, tissue-based methods, and practical limitations. It is useful for comparing when each modality is most informative and how they are combined in real-world diagnostic workups.*

### 7.1 Imaging: quantitative performance
A 2023 surgical management review reports the following diagnostic performance in pancreatic NETs (applied clinically to NF‑PanNET workups):
- **CT** sensitivity ~82%, specificity 96%.
- **MRI** sensitivity 93%, specificity 88%.
- **68Ga‑DOTATATE PET/CT** sensitivity 93%, specificity 91%; higher detection for G1/G2 than G3.
- **EUS** mean sensitivity 75–97%, especially for lesions <2 cm.
These data are reported in text and are captured in cropped evidence images (sulciner2023surgicalmanagementof pages 2-5, sulciner2023surgicalmanagementof media 0ba4a3b1, sulciner2023surgicalmanagementof media 7d24a64d, sulciner2023surgicalmanagementof media 210f90c9).

### 7.2 Tissue diagnosis and pathology/IHC
- Core principles: histologic confirmation and grading by Ki‑67/mitotic rate are central (sulciner2023surgicalmanagementof pages 1-2, conzo2026pancreaticneuroendocrinetumors pages 5-7).
- Immunohistochemistry for **synaptophysin**, **chromogranin A**, and **Ki‑67** is described as essential for confirming neuroendocrine differentiation and grading (conzo2026pancreaticneuroendocrinetumors pages 5-7).
- Practical limitation in small tumors: EUS‑FNA yield may be low; one dataset reported tumor differentiation and Ki‑67 determination in only **26.4%** and **20.1%** of small lesions, respectively (sulciner2023surgicalmanagementof pages 2-5).

### 7.3 Functional imaging integration (68Ga + FDG)
A 2024 expert review states that **“the use of [68Ga]Ga-DOTA-peptide PET and [18F]FDG PET scans is recommended for a comprehensive PanNEN assessment”** (battistella2024recentdevelopmentsin pages 20-26).

### 7.4 Biomarkers
- Conventional circulating markers (e.g., chromogranin A) have limited standalone utility in pNETs (conzo2026pancreaticneuroendocrinetumors pages 5-7).
- Emerging biomarkers noted include molecular assays (e.g., NETest) and liquid biopsy approaches; however, reproducibility, standardization, and cost-effectiveness remain barriers (battistella2024recentdevelopmentsin pages 20-26).

### 7.5 Differential diagnosis
Hypervascular pancreatic lesions (e.g., solid serous cystadenoma) can mimic NF‑pNET on imaging, emphasizing need for multimodal assessment and/or tissue diagnosis when management would change (sulciner2023surgicalmanagementof pages 15-16).

---

## 8. Temporal development (onset and progression)
- NF‑PanNETs are frequently discovered incidentally and can be indolent, but a meaningful fraction present with metastatic disease (liver predominant) (battistella2024recentdevelopmentsin pages 1-6).
- Progression risk stratification relies heavily on tumor size, grade (Ki‑67), and nodal/metastatic status; Ki‑67 assessment variability and intratumoral heterogeneity are recognized issues in real-world grading from small biopsies (conzo2026pancreaticneuroendocrinetumors pages 13-13, conzo2026pancreaticneuroendocrinetumors pages 5-7).

Staging schema references (AJCC/ENETS) were not directly extracted in the retrieved evidence.

---

## 9. Inheritance and population
### 9.1 Epidemiology statistics
- The 2024 diagnostic review reports an **“annual incidence of less than 1 case per 100’000 inhabitants”** for PanNENs and that they “account for less than 3% of all pancreatic tumors”; autopsy prevalence reported as **0.8–10%** (battistella2024recentdevelopmentsin pages 1-6).
- A 2026 review cites U.S. NET incidence rising to **~6.98 per 100,000 annually** (NETs overall; not pancreas-specific) and attributes increases to improved diagnostics (conzo2026pancreaticneuroendocrinetumors pages 2-4).
- Hereditary syndromes: MEN1 prevalence estimated **3–20 per 100,000**, with MEN1 gene mutations causal; mutation carriers should undergo regular specialized screening from early adulthood in one 2024 review (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

### 9.2 Inheritance patterns (for predisposition)
- MEN1 is autosomal dominant; associated pancreatic NETs are often multifocal and earlier onset, motivating surveillance programs (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).
- Other predisposition syndromes include VHL, NF1, and TSC (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

Sex/ethnicity distributions were noted in a 2026 review (slight male predominance; higher prevalence in Caucasians) but without detailed pancreas-specific stratified estimates in the retrieved evidence (conzo2026pancreaticneuroendocrinetumors pages 10-11, conzo2026pancreaticneuroendocrinetumors pages 2-4).

---

## 10. Outcome / prognosis
### 10.1 Prognostic factors
Across cohorts and reviews, principal prognostic factors include **grade (Ki‑67/mitotic)**, tumor size, nodal status, and metastatic burden.
- Grade-specific survival differences: one 2023 review reports median overall survival approximately **12 years for grade 1** versus **~10 months for grade 3** pancreatic NET (sulciner2023surgicalmanagementof pages 1-2).
- Recurrence risk factors after resection include **tumor size >2 cm**, **symptomatic presentation**, **Ki‑67 >3%**, and **positive lymph nodes** (sulciner2023surgicalmanagementof pages 2-5, sulciner2023surgicalmanagementof pages 1-2).

### 10.2 Prediction models
A 2023 systematic review of recurrence prediction models for resectable grade 1/2 sporadic NF‑pNETs (3583 patients across 14 studies) found c-statistics from **0.67 to 0.94**, but noted high risk of bias in most model development studies; tumor grade, size, and lymph node positivity were the most frequent predictors (https://doi.org/10.3390/cancers15051525; published Feb 2023) (sulciner2023surgicalmanagementof pages 1-2).

---

## 11. Treatment (current standards, recent developments, and real-world implementation)
### 11.1 Localized disease: surveillance vs surgery
- **Active surveillance** is increasingly used for carefully selected **≤2 cm** asymptomatic NF‑PanNETs. A 2023 review summarizes guidance: ENETS recommends surveillance for nonfunctional PNETs ≤2 cm (low grade, asymptomatic, no suspicious radiographic features) with imaging every 6–12 months; NANETS supports observation for <1 cm and individualized decisions for 1–2 cm; NCCN supports observation ≤2 cm with stronger evidence for ≤1 cm (sulciner2023surgicalmanagementof pages 10-11).
- Practical nuance: ENETS/ESMO allow surveillance but emphasize integration of growth kinetics, imaging risk features, and biopsy grade, and recognize Ki‑67 limitations in small samples (conzo2026pancreaticneuroendocrinetumors pages 13-13).

### 11.2 Systemic therapy for advanced / progressive disease
| Treatment option | Typical indication in NF-PanNET | Key efficacy statistics | Major adverse events / limitations | Guideline / real-world notes |
|---|---|---|---|---|
| Active surveillance | Selected asymptomatic, low-grade, localized tumors ≤2 cm, especially without suspicious imaging features or ductal dilation | In a prospective international cohort of small NF-PNETs, 18.8% eventually underwent surgery, 2% progressed, and none developed metastases at last follow-up; some retrospective series found no disease-specific survival difference vs upfront surgery for small tumors (sulciner2023surgicalmanagementof pages 10-11, sulciner2023surgicalmanagementof pages 2-5) | Risk of understaging; late recurrence/metastasis still reported in some series (nearly 8% in tumors ≤2 cm); requires reliable follow-up and careful risk stratification (sulciner2023surgicalmanagementof pages 10-11, conzo2026pancreaticneuroendocrinetumors pages 13-13) | ENETS supports surveillance for selected asymptomatic ≤2 cm NF-pNETs; NANETS favors observation for <1 cm and individualized decisions for 1–2 cm; ESMO recommends individualized surveillance based on growth kinetics, imaging risk, and surgical risk (sulciner2023surgicalmanagementof pages 10-11, conzo2026pancreaticneuroendocrinetumors pages 13-13) |
| Surgery | Localized resectable disease; symptomatic tumors; tumors >2 cm; lesions with duct dilation, growth, or other high-risk features | Curative-intent standard for localized disease; no single pooled efficacy number in extracted evidence, but surgery remains the reference treatment for resectable tumors (sulciner2023surgicalmanagementof pages 2-5, conzo2026pancreaticneuroendocrinetumors pages 13-13) | Pancreatic surgical morbidity can be substantial, reported up to 62% in some series, largely pancreatic fistula; extent of surgery must be balanced against tumor size/location and patient fitness (sulciner2023surgicalmanagementof pages 9-10) | Still the cornerstone for cure; for small lesions, decision must integrate size, Ki-67, imaging, age/comorbidity, and patient preference (sulciner2023surgicalmanagementof pages 10-11, conzo2026pancreaticneuroendocrinetumors pages 13-13) |
| Somatostatin analogs (lanreotide / octreotide) | SSTR-positive, well-differentiated, slowly progressive disease; often early-line systemic therapy | CLARINET: lanreotide prolonged PFS, not reached vs 18.0 months; HR 0.47. CLARINET-FORTE pancreatic cohort: median PFS 5.6 months after dose intensification, suggesting limited benefit after progression (melhorn2024treatmentsequencingin pages 1-2, castillon2023seomgetneclinicalguidelines pages 9-10) | Requires SSTR expression; limited benefit after progression when simply escalating dose interval; class toxicities/monitoring include hypersensitivity, cholelithiasis, and pancreatic exocrine insufficiency concerns (castillon2023seomgetneclinicalguidelines pages 9-10, melhorn2024treatmentsequencingin pages 2-3) | Recommended first-line for slowly progressive enteropancreatic NET with low proliferative activity; also serves as backbone for sequencing and for SSTR-based strategies (melhorn2024treatmentsequencingin pages 2-3, melhorn2024treatmentsequencingin pages 1-2) |
| Everolimus | Advanced progressive well/moderately differentiated NF-PanNET, including SSTR-negative or more rapidly growing disease | RADIANT-3: median PFS 11.0 vs 4.6 months; HR 0.35. RADIANT-4: median PFS 11.0 vs 3.9 months; HR 0.48 (castillon2023seomgetneclinicalguidelines pages 9-10) | Cytostatic rather than strongly cytoreductive; limited ORR in comparative sequencing context; adverse-event specifics not quantified in extracted evidence (castillon2023seomgetneclinicalguidelines pages 9-10, melhorn2024treatmentsequencingin pages 2-3) | Guideline-endorsed targeted therapy; SEQTOR showed lower first-line response than chemotherapy (11% vs 30%) despite similar first-line PFS, informing sequencing discussions (castillon2023seomgetneclinicalguidelines pages 9-10) |
| Sunitinib | Advanced progressive pancreatic NET, especially after or instead of SSA depending on disease tempo and biology | Median PFS 11.4 vs 5.5 months; HR 0.42; p<0.001 (castillon2023seomgetneclinicalguidelines pages 9-10) | TKI toxicity limits use in some patients; specific AE rates not reported in extracted evidence (castillon2023seomgetneclinicalguidelines pages 9-10) | Approved for advanced progressive panNETs and remains a standard targeted option in sequencing algorithms (castillon2023seomgetneclinicalguidelines pages 9-10, melhorn2024treatmentsequencingin pages 2-3, melhorn2024treatmentsequencingin pages 1-2) |
| CAPTEM (capecitabine + temozolomide) | Progressive advanced pancreatic NET, especially when tumor shrinkage is desired or in more proliferative disease | E2211: PFS 22.7 vs 14.4 months vs temozolomide alone; HR 0.58; p=0.022; no OS benefit. SEQTOR: first-line response rate 30% vs 11% with everolimus, but similar first-line PFS 21.5 vs 23.6 months (castillon2023seomgetneclinicalguidelines pages 9-10) | Chemotherapy toxicity and myelosuppression are practical concerns, though detailed AE rates were not extracted; evidence mainly from advanced disease rather than small localized NF-PNETs (castillon2023seomgetneclinicalguidelines pages 9-10) | Often preferred when a higher objective response is needed; a key comparator in modern sequencing discussions against targeted therapy (castillon2023seomgetneclinicalguidelines pages 9-10, melhorn2024treatmentsequencingin pages 2-3) |
| PRRT (177Lu-DOTATATE) | SSTR-positive well-differentiated advanced disease; increasingly considered earlier in selected patients; also under study neoadjuvantly in high-risk resectable NF-PanNET | NETTER-1: HR for progression/death 0.21; median PFS not reached vs 8.4 months. NETTER-2: median PFS 22.8 vs 8.5 months; ORR 43% vs 9.3%. Long-term hematologic toxicity (MDS/leukemia) ~3–4% (melhorn2024treatmentsequencingin pages 2-3) | Requires SSTR-positive disease and specialized centers; delayed hematologic toxicity is an important limitation (melhorn2024treatmentsequencingin pages 2-3) | ESMO places PRRT later in pancreatic NET sequence after approved systemic options; ENETS allows rechallenge in selected patients. NeoLuPaNET (NCT04385992) tested neoadjuvant PRRT before surgery in high-risk resectable non-functioning PanNET, 31 enrolled, 4 cycles of 7,400 MBq every 6–8 weeks (melhorn2024treatmentsequencingin pages 2-3, NCT04385992 chunk 1) |
| PRRT + CAPTEM (investigational combination) | Advanced unresectable low/intermediate-grade pNET in trial setting | CONTROL NETs pNET cohort (NCT02358356) designed to test 12-month PFS 77% for PRRT+CAPTEM vs 60% for CAPTEM alone; planned pNET sample size 90; endpoints include PFS, ORR, OS, safety, and QoL (NCT02358356 chunk 1) | Combination toxicity may be greater than single modality; mature comparative outcome data were not provided in extracted evidence (NCT02358356 chunk 1) | Important ongoing/modern trial concept for intensification and sequencing in pNETs; not standard of care on the basis of extracted evidence alone (NCT02358356 chunk 1) |
| Newer TKIs: surufatinib | Advanced NET/panNET after progression; availability varies by region | ORR 19%; median PFS 10.9 vs 3.7 months; HR 0.34 (castillon2023seomgetneclinicalguidelines pages 9-10) | TKI-related toxicity; regional access/regulatory heterogeneity; extracted evidence does not specify full AE profile here (castillon2023seomgetneclinicalguidelines pages 9-10) | Increasingly discussed in contemporary sequencing reviews and real-world practice, especially where approved (castillon2023seomgetneclinicalguidelines pages 9-10) |
| Newer TKIs: lenvatinib | Advanced progressive pancreatic NET in selected settings | Response rate 44.2%; median PFS 15.6 months (castillon2023seomgetneclinicalguidelines pages 9-10) | Evidence base less mature than everolimus/sunitinib; toxicity may limit broad uptake (castillon2023seomgetneclinicalguidelines pages 9-10) | Considered an active newer antiangiogenic option, but integration into routine sequencing is still evolving (castillon2023seomgetneclinicalguidelines pages 9-10) |
| Newer TKIs: cabozantinib | Progressive advanced NET, including pancreatic primaries, typically later-line / trial-informed use | Phase II partial response rate ~15%; phase III CABINET ongoing/not fully reported in extracted evidence (castillon2023seomgetneclinicalguidelines pages 9-10) | Evidence still emerging; toxicity and optimal placement in sequence remain under refinement (castillon2023seomgetneclinicalguidelines pages 9-10) | Mentioned as an emerging option in recent guideline-oriented reviews rather than an established universal standard for NF-PanNET (castillon2023seomgetneclinicalguidelines pages 9-10) |


*Table: This table summarizes current management options for non-functional pancreatic neuroendocrine tumors, spanning observation, surgery, systemic therapy, PRRT, and newer targeted agents. It highlights where each approach fits clinically, the main efficacy numbers available from the extracted evidence, and the practical limitations relevant to real-world treatment sequencing.*

Key efficacy statistics extracted from a 2023 guideline (SEOM‑GETNE; published May 2023; https://doi.org/10.1007/s12094-023-03205-6):
- **Sunitinib**: median PFS **11.4 vs 5.5 months** (HR 0.42; p<0.001) in advanced progressive panNETs (castillon2023seomgetneclinicalguidelines pages 9-10).
- **Everolimus**: 
  - **RADIANT‑3**: PFS **11.0 vs 4.6 months** (HR 0.35).
  - **RADIANT‑4**: PFS **11.0 vs 3.9 months** (HR 0.48).
  (castillon2023seomgetneclinicalguidelines pages 9-10).
- **CAPTEM (temozolomide+capecitabine)**:
  - **E2211**: PFS **22.7 vs 14.4 months** vs temozolomide alone (HR 0.58; p=0.022), without OS benefit in the extracted summary.
  - **SEQTOR**: higher first-line response with chemotherapy vs everolimus (30% vs 11%) with similar first-line PFS (21.5 vs 23.6 months).
  (castillon2023seomgetneclinicalguidelines pages 9-10).

### 11.3 PRRT (177Lu‑DOTATATE): implementation and sequencing
A 2024 treatment sequencing review (published Oct 2024; https://doi.org/10.1007/s12254-024-01001-8) summarizes PRRT evidence and sequencing considerations:
- NETTER‑1 showed major reduction in risk of progression/death (HR 0.21; median PFS not reached vs 8.4 months).
- NETTER‑2 (first-line G2/G3) reported median PFS 22.8 vs 8.5 months; ORR 43% vs 9.3%.
- Long-term hematologic toxicity (MDS/leukemia) occurs in ~3–4%.
- Both SSA and PRRT require SSTR positivity, and placement in sequence depends on grade and tempo; ESMO places PRRT later for pancreatic NET after approved treatments (melhorn2024treatmentsequencingin pages 2-3, melhorn2024treatmentsequencingin pages 1-2).

### 11.4 Key ongoing / recent trials (ClinicalTrials.gov)
- **NeoLuPaNET (NCT04385992)**: Phase II single-arm trial of **neoadjuvant 177Lu‑DOTATATE before surgery** in resectable non-functioning PanNET at high recurrence risk; 31 enrolled; four cycles of 7,400 MBq every 6–8 weeks; primary endpoint 90‑day postoperative morbidity/mortality; completed (start 2020‑03‑09; completion 2023‑06‑26) (https://clinicaltrials.gov/study/NCT04385992) (NCT04385992 chunk 1).
- **CONTROL NETs (NCT02358356)**: Randomized phase II trial in pNET cohort comparing **PRRT+CAPTEM vs CAPTEM alone**; designed for 12‑month PFS 77% vs 60%; includes ORR, OS, safety, and QoL (EORTC QLQ‑C30; QLQ‑GINET21). PRRT regimen: 177Lu‑octreotate 7.8 GBq q8w ×4; CAPTEM dosing specified in protocol (https://clinicaltrials.gov/study/NCT02358356) (NCT02358356 chunk 1).

### 11.5 MAXO term suggestions (treatments)
(Informative mapping; requires ontology validation):
- **Active surveillance** — MAXO:0000127 (clinical surveillance/monitoring)
- **Pancreatic tumor resection** — MAXO:0001073 (surgical resection)
- **Somatostatin analog therapy** — MAXO:0000766
- **mTOR inhibitor therapy (everolimus)** — MAXO:0000783
- **Tyrosine kinase inhibitor therapy (sunitinib, others)** — MAXO:0000784
- **Peptide receptor radionuclide therapy** — MAXO:0000945

---

## 12. Prevention
### 12.1 Primary prevention
No established primary prevention interventions were identified for sporadic NF‑PanNET in the retrieved evidence.

### 12.2 Secondary prevention: surveillance in hereditary syndromes
Hereditary syndrome reviews emphasize early detection via structured surveillance:
- For MEN1, a 2024 review states mutation carriers should be in regular specialized screening programs and be managed in expert interdisciplinary centers; early diagnosis and individualized treatment can prolong expected lifespan (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).
- The hereditary syndromes review emphasizes genetic screening in childhood and diagnostic surveillance often in adolescence for asymptomatic carriers (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3).

---

## 13. Other species / natural disease
No evidence specific to naturally occurring **pancreatic** neuroendocrine tumors in non-human species was retrieved in this run. (A canine/human gallbladder neuroendocrine neoplasm review was retrieved but is anatomically distinct from pancreatic disease and was not used to avoid misclassification.)

---

## 14. Model organisms
No model organism papers (e.g., Men1 mouse models, RIP‑Tag models, organoids) were retrieved and extracted in the current evidence set; additional targeted searches in MGI/IMPC and PanNET model literature would be required.

---

## 15. Expert opinions and analysis (authoritative synthesis)
- Diagnostic experts emphasize **multimodal imaging** and evolving roles for AI/radiomics and molecular assays, but note barriers such as reproducibility, standardization, and cost-effectiveness (battistella2024recentdevelopmentsin pages 20-26, battistella2024recentdevelopmentsin pages 1-6).
- Sequencing experts stress individualized decision-making because of the growing number of active options; grade (Ki‑67), SSTR expression, and disease tempo are key determinants (melhorn2024treatmentsequencingin pages 2-3, melhorn2024treatmentsequencingin pages 1-2).

---

## Notes on evidence gaps in this run
Several knowledge-base fields requested in the template (ICD‑10/ICD‑11 codes, MeSH terms, detailed AJCC/ENETS TNM staging tables, variant-level ClinVar classifications/allele frequencies, and model organism inventories) were not available from the retrieved evidence and would require additional database- and genetics-focused retrieval.


References

1. (OpenTargets Search: pancreatic neuroendocrine tumor): Open Targets Query (pancreatic neuroendocrine tumor, 36 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (saleh2024pancreaticneuroendocrinetumors pages 1-2): Zena Saleh, Matthew Christopher Moccia, Zachary Ladd, Joneja Upasana, Yahui Li, Francis Spitz, Young Ki Hong, and Tao Gao. Pancreatic neuroendocrine tumors: signaling pathways and epigenetic regulation. International Journal of Molecular Sciences, Jan 2024. URL: https://doi.org/10.3390/ijms25021331, doi:10.3390/ijms25021331. This article has 17 citations.

3. (battistella2024recentdevelopmentsin pages 1-6): Anna Battistella, Matteo Tacelli, Paola Mapelli, Marco Schiavo Lena, Valentina Andreasi, Luana Genova, Francesca Muffatti, Francesco De Cobelli, Stefano Partelli, and Massimo Falconi. Recent developments in the diagnosis of pancreatic neuroendocrine neoplasms. Expert Review of Gastroenterology &amp; Hepatology, 18:155-169, May 2024. URL: https://doi.org/10.1080/17474124.2024.2342837, doi:10.1080/17474124.2024.2342837. This article has 3 citations and is from a peer-reviewed journal.

4. (sulciner2023surgicalmanagementof pages 10-11): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 46 citations.

5. (sulciner2023surgicalmanagementof pages 2-5): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 46 citations.

6. (castillon2023seomgetneclinicalguidelines pages 9-10): Jaume Capdevila Castillón, Teresa Alonso Gordoa, Alberto Carmona Bayonas, Ana Custodio Carretero, Rocío García-Carbonero, Enrique Grande Pulido, Paula Jiménez Fonseca, Angela Lamarca Lete, Angel Segura Huerta, and Javier Gallego Plazas. Seom-getne clinical guidelines for the diagnosis and treatment of gastroenteropancreatic and bronchial neuroendocrine neoplasms (nens) (2022). Clinical & Translational Oncology, 25:2692-2706, May 2023. URL: https://doi.org/10.1007/s12094-023-03205-6, doi:10.1007/s12094-023-03205-6. This article has 16 citations and is from a peer-reviewed journal.

7. (melhorn2024treatmentsequencingin pages 2-3): Philipp Melhorn, Markus Raderer, and Barbara Kiesewetter. Treatment sequencing in gastroenteropancreatic neuroendocrine tumors. memo - Magazine of European Medical Oncology, 17:257-262, Oct 2024. URL: https://doi.org/10.1007/s12254-024-01001-8, doi:10.1007/s12254-024-01001-8. This article has 1 citations.

8. (sulciner2023surgicalmanagementof pages 1-2): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 46 citations.

9. (battistella2024recentdevelopmentsin pages 16-20): Anna Battistella, Matteo Tacelli, Paola Mapelli, Marco Schiavo Lena, Valentina Andreasi, Luana Genova, Francesca Muffatti, Francesco De Cobelli, Stefano Partelli, and Massimo Falconi. Recent developments in the diagnosis of pancreatic neuroendocrine neoplasms. Expert Review of Gastroenterology &amp; Hepatology, 18:155-169, May 2024. URL: https://doi.org/10.1080/17474124.2024.2342837, doi:10.1080/17474124.2024.2342837. This article has 3 citations and is from a peer-reviewed journal.

10. (castillon2023seomgetneclinicalguidelines pages 2-4): Jaume Capdevila Castillón, Teresa Alonso Gordoa, Alberto Carmona Bayonas, Ana Custodio Carretero, Rocío García-Carbonero, Enrique Grande Pulido, Paula Jiménez Fonseca, Angela Lamarca Lete, Angel Segura Huerta, and Javier Gallego Plazas. Seom-getne clinical guidelines for the diagnosis and treatment of gastroenteropancreatic and bronchial neuroendocrine neoplasms (nens) (2022). Clinical & Translational Oncology, 25:2692-2706, May 2023. URL: https://doi.org/10.1007/s12094-023-03205-6, doi:10.1007/s12094-023-03205-6. This article has 16 citations and is from a peer-reviewed journal.

11. (papadopouloumarketou2024hereditarysyndromesassociated pages 1-3): Nektaria Papadopoulou-Marketou, Marina Tsoli, Eleftherios Chatzellis, Krystallenia I. Alexandraki, and Gregory Kaltsas. Hereditary syndromes associated with pancreatic and lung neuroendocrine tumors. Cancers, 16:2075, May 2024. URL: https://doi.org/10.3390/cancers16112075, doi:10.3390/cancers16112075. This article has 16 citations.

12. (conzo2026pancreaticneuroendocrinetumors pages 2-4): Giovanni Conzo, Federico Maria Mongardini, Maddalena Paolicelli, Michele Klain, Giuseppe Bellastella, Alessandra Conzo, Zhou Bo, Eduardo Lanza, Leandra Piscopo, and Renato Patrone. Pancreatic neuroendocrine tumors: from benchside to surgical treatment. Medicina, 62:479, Mar 2026. URL: https://doi.org/10.3390/medicina62030479, doi:10.3390/medicina62030479. This article has 1 citations.

13. (NCT02358356 chunk 1):  Capecitabine ON Temozolomide Radionuclide Therapy Octreotate Lutetium-177 NeuroEndocrine Tumours Study. Australasian Gastro-Intestinal Trials Group. 2015. ClinicalTrials.gov Identifier: NCT02358356

14. (andersen2024welldifferentiatedg1and pages 1-2): Kirstine Øster Andersen, Sönke Detlefsen, Klaus Brusgaard, and Henrik Thybo Christesen. Well-differentiated g1 and g2 pancreatic neuroendocrine tumors: a meta-analysis of published expanded dna sequencing data. Frontiers in Endocrinology, May 2024. URL: https://doi.org/10.3389/fendo.2024.1351624, doi:10.3389/fendo.2024.1351624. This article has 10 citations.

15. (maluchenko2024molecularbasisof pages 17-18): Alesia Maluchenko, Denis Maksimov, Zoia Antysheva, Julia Krupinova, Ekaterina Avsievich, Olga Glazova, Natalia Bodunova, Nikolay Karnaukhov, Ilia Feidorov, Diana Salimgereeva, Mark Voloshin, and Pavel Volchkov. Molecular basis of pancreatic neuroendocrine tumors. International Journal of Molecular Sciences, 25:11017, Oct 2024. URL: https://doi.org/10.3390/ijms252011017, doi:10.3390/ijms252011017. This article has 10 citations.

16. (sulciner2023surgicalmanagementof media 0ba4a3b1): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 46 citations.

17. (sulciner2023surgicalmanagementof media 7d24a64d): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 46 citations.

18. (sulciner2023surgicalmanagementof media 210f90c9): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 46 citations.

19. (battistella2024recentdevelopmentsin pages 20-26): Anna Battistella, Matteo Tacelli, Paola Mapelli, Marco Schiavo Lena, Valentina Andreasi, Luana Genova, Francesca Muffatti, Francesco De Cobelli, Stefano Partelli, and Massimo Falconi. Recent developments in the diagnosis of pancreatic neuroendocrine neoplasms. Expert Review of Gastroenterology &amp; Hepatology, 18:155-169, May 2024. URL: https://doi.org/10.1080/17474124.2024.2342837, doi:10.1080/17474124.2024.2342837. This article has 3 citations and is from a peer-reviewed journal.

20. (conzo2026pancreaticneuroendocrinetumors pages 5-7): Giovanni Conzo, Federico Maria Mongardini, Maddalena Paolicelli, Michele Klain, Giuseppe Bellastella, Alessandra Conzo, Zhou Bo, Eduardo Lanza, Leandra Piscopo, and Renato Patrone. Pancreatic neuroendocrine tumors: from benchside to surgical treatment. Medicina, 62:479, Mar 2026. URL: https://doi.org/10.3390/medicina62030479, doi:10.3390/medicina62030479. This article has 1 citations.

21. (sulciner2023surgicalmanagementof pages 15-16): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 46 citations.

22. (conzo2026pancreaticneuroendocrinetumors pages 13-13): Giovanni Conzo, Federico Maria Mongardini, Maddalena Paolicelli, Michele Klain, Giuseppe Bellastella, Alessandra Conzo, Zhou Bo, Eduardo Lanza, Leandra Piscopo, and Renato Patrone. Pancreatic neuroendocrine tumors: from benchside to surgical treatment. Medicina, 62:479, Mar 2026. URL: https://doi.org/10.3390/medicina62030479, doi:10.3390/medicina62030479. This article has 1 citations.

23. (conzo2026pancreaticneuroendocrinetumors pages 10-11): Giovanni Conzo, Federico Maria Mongardini, Maddalena Paolicelli, Michele Klain, Giuseppe Bellastella, Alessandra Conzo, Zhou Bo, Eduardo Lanza, Leandra Piscopo, and Renato Patrone. Pancreatic neuroendocrine tumors: from benchside to surgical treatment. Medicina, 62:479, Mar 2026. URL: https://doi.org/10.3390/medicina62030479, doi:10.3390/medicina62030479. This article has 1 citations.

24. (sulciner2023surgicalmanagementof pages 9-10): Megan L. Sulciner and Thomas E. Clancy. Surgical management of pancreatic neuroendocrine tumors. Cancers, 15:2006, Mar 2023. URL: https://doi.org/10.3390/cancers15072006, doi:10.3390/cancers15072006. This article has 46 citations.

25. (melhorn2024treatmentsequencingin pages 1-2): Philipp Melhorn, Markus Raderer, and Barbara Kiesewetter. Treatment sequencing in gastroenteropancreatic neuroendocrine tumors. memo - Magazine of European Medical Oncology, 17:257-262, Oct 2024. URL: https://doi.org/10.1007/s12254-024-01001-8, doi:10.1007/s12254-024-01001-8. This article has 1 citations.

26. (NCT04385992 chunk 1): Massimo Falconi. Neoadjuvant PRRT With 177Lu-DOTATATE Followed by Surgery for Resectable PanNET. IRCCS San Raffaele. 2020. ClinicalTrials.gov Identifier: NCT04385992
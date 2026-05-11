---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T09:01:02.161298'
end_time: '2026-05-11T09:23:07.543451'
duration_seconds: 1325.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Myeloid Leukemia with CEBPA Somatic Mutations
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 59
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Myeloid Leukemia with CEBPA Somatic Mutations
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia with CEBPA Somatic Mutations** covering all of the
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
- **Disease Name:** Acute Myeloid Leukemia with CEBPA Somatic Mutations
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Acute Myeloid Leukemia with CEBPA Somatic Mutations** covering all of the
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


# Disease Characteristics Research Report: Acute Myeloid Leukemia (AML) with CEBPA Somatic Mutations

## Target Disease
- **Disease name:** Acute Myeloid Leukemia with CEBPA somatic mutations (often operationalized as AML with *CEBPA* mutation, especially *bZIP* in-frame)
- **Category:** Hematologic malignancy (myeloid neoplasm), genetically defined AML subgroup (classification-dependent)
- **MONDO / MeSH / ICD-10/ICD-11 / OMIM / Orphanet identifiers:** Not explicitly retrievable from the full-text sources available in this run; therefore not reported here (knowledge-base curation step would require direct ontology lookup outside the retrieved literature corpus).

## 1. Disease Information
### 1.1 Concise overview
AML is a clonal hematopoietic malignancy characterized by expansion of immature myeloid blasts in bone marrow and blood, resulting in marrow failure and ineffective hematopoiesis (cytopenias and related complications). (debnath2024prognosisandtreatment pages 1-2)

A clinically important genetically defined subset is AML with somatic mutation(s) in the transcription factor **CEBPA** (CCAAT/enhancer-binding protein alpha), whose altered function disrupts myeloid differentiation and is associated with characteristic prognostic and classification features, especially when mutations are **in-frame insertions/deletions in the basic leucine zipper (bZIP) domain**. (sargas2023comparisonofthe pages 1-2, mrozek2023outcomepredictionby pages 1-2)

### 1.2 Synonyms and alternative names used in recent authoritative sources
Recent classification/guideline literature uses multiple labels for overlapping but non-identical sets of cases:
- “**AML with CEBPA mutation**” (WHO 2022 label in comparative reviews). (park2024whatisnew pages 1-2, park2024whatisnew pages 2-3)
- “**AML with mutated bZIP CEBPA**” (ICC 2022 label). (park2024whatisnew pages 1-2)
- **biCEBPA** (biallelic), **smbZIP-CEBPA** (single bZIP mutation) in WHO/ICC comparisons. (salman2024comparativeanalysisof pages 2-4, park2024whatisnew pages 1-2)
- **CEBPAdm** (double-mutant/biallelic), **CEBPAsm** (single-mutant/monoallelic), **CEBPAbZIP-inf** (bZIP in-frame) in clinical/prognostic studies. (tien2024dysregulatedimmuneand pages 1-2, yuan2023sporadicandfamilial pages 5-6)

### 1.3 Classification context (WHO 2022 vs ICC 2022 vs ELN 2022)
- **WHO 2022:** includes both **biallelic** *CEBPA* and **single bZIP-region mutations** (smbZIP-CEBPA) under “AML with CEBPA mutation” in comparative descriptions; a ≥20% blast threshold is described for AML with CEBPA mutation in a classification comparison review. (park2024whatisnew pages 1-2, park2024whatisnew pages 2-3)
- **ICC 2022:** emphasizes **in-frame bZIP CEBPA** mutations and applies a **≥10% blast cutoff** for AML with recurrent genetic abnormalities (including CEBPA-defined AML). (salman2024comparativeanalysisof pages 2-4, park2024whatisnew pages 1-2)
- **ELN 2022 (risk stratification):** revised favorable-risk criterion from **biallelic CEBPA** (ELN 2017) to **in-frame bZIP CEBPA mutations**, regardless of monoallelic vs biallelic state. (sargas2023comparisonofthe pages 1-2, mrozek2023outcomepredictionby pages 1-2)

Visual evidence summarizing WHO vs ICC differences is available in a WHO/ICC comparison figure. (salman2024comparativeanalysisof media e167dd0e)

## 2. Etiology
### 2.1 Primary causal factors
- **Somatic driver mutations in CEBPA**: AML in this entity is primarily driven/defined by acquired mutations affecting *CEBPA*—often involving N-terminal transactivation domain (TAD) and/or C-terminal bZIP domain, with specific mutation classes carrying distinct prognostic implications. (georgi2024prognosticimpactof pages 1-2, faisal2023locationlocationlocation pages 1-3)

### 2.2 Risk factors
#### Genetic risk factors (germline predisposition vs somatic)
- A minority of patients with CEBPA-mutated AML carry **germline CEBPA variants**; one review estimates ~10% of CEBPA-mutated AML may have germline CEBPA. (yuan2023sporadicandfamilial pages 4-5)
- For germline predisposition, N-terminal germline variants have been described with high penetrance and earlier onset; familial cases often acquire a second somatic C-terminal mutation. (yuan2023sporadicandfamilial pages 4-5, tawana2017familialcebpamutatedacute pages 1-4)

#### Environmental/occupational and therapy-related factors for AML broadly
Recent reviews summarize established AML risk contexts:
- Ionizing radiation exposure and chemical exposures including **benzene** and other solvents are explicitly described as AML risk factors, along with tobacco use; therapy-related AML after prior radiation/cytotoxic agents is also described. (marrero2023currentlandscapeof pages 1-2)
- A systematic review/meta-analysis notes radiation increases leukemia risk and that aromatic compounds (benzene, toluene, xylene) have a strong association with AML; it also notes significantly elevated risk of therapy-related AML following chemotherapy. (shen2023associationbetweenmetal(loid)s pages 1-2)
- A mechanistic review details benzene metabolism (notably via **CYP2E1**) producing reactive metabolites that contribute to hematopoietic/bone-marrow injury relevant to leukemogenesis. (sandoval2023anupdatedoverview pages 7-9)

### 2.3 Protective factors
No specific protective genetic variants or modifiable protective exposures were identified in the retrieved full texts for this entity.

### 2.4 Gene–environment interactions
Evidence in AML broadly (not specific to CEBPA-mutated AML) indicates that polymorphisms in xenobiotic-metabolism genes can modify leukemia/cancer risk; examples reported include CYP2E1, GSTM1, NQO1, NAT2, MDR1 and broader CYP450 SNPs. (sandoval2023anupdatedoverview pages 7-9)

## 3. Phenotypes
### 3.1 Core clinical presentation (AML overall)
AML frequently presents with bone marrow failure manifestations and may also show extramedullary involvement.
- Cytopenia-related symptoms and complications include anemia, bleeding, and infections. (rivera2023mutationsinthe pages 2-2, leoni2025…genemutationsby pages 11-15)
- Organ infiltration can involve spleen, liver, skin, gums, and sometimes CNS. (rivera2023mutationsinthe pages 2-2, leoni2025…genemutationsby pages 11-15)

### 3.2 CEBPA-mutated AML clinical correlates
- Morphologic subtypes commonly reported include **FAB M1, M2, or M4**; karyotype is often **normal or intermediate-risk**. (yuan2023sporadicandfamilial pages 4-5)
- Familial CEBPA AML may present **without preceding abnormal blood counts or myelodysplasia**. (yuan2023sporadicandfamilial pages 4-5, tawana2017familialcebpamutatedacute pages 1-4)

### 3.3 Suggested HPO terms (examples)
(Representative mapping for knowledge-base use; frequency data are limited in retrieved texts.)
- **Cytopenias / marrow failure**: Anemia (HP:0001903), Thrombocytopenia (HP:0001873), Neutropenia (HP:0001875), Pancytopenia (HP:0001876). (leoni2025…genemutationsby pages 11-15, debnath2024prognosisandtreatment pages 1-2)
- **Bleeding manifestations**: Epistaxis (HP:0000421), Purpura (HP:0000979), Gingival bleeding (HP:0000225). (leoni2025…genemutationsby pages 11-15)
- **Infection susceptibility**: Recurrent infections (HP:0002719), Fever (HP:0001945). (leoni2025…genemutationsby pages 11-15)
- **Extramedullary disease**: Hepatomegaly (HP:0002240), Splenomegaly (HP:0001744), Cutaneous infiltration (suggest: Skin infiltration, HP:0001031 as a broad proxy), Central nervous system involvement (HP:0001298 for encephalopathy as proxy; CNS leukemia lacks a perfect single HPO term in this corpus). (rivera2023mutationsinthe pages 2-2, leoni2025…genemutationsby pages 11-15)

## 4. Genetic / Molecular Information
### 4.1 Causal gene
- **CEBPA** (CCAAT/enhancer-binding protein alpha), a myeloid transcription factor; produces p42 and p30 isoforms. (brown2020secondaryleukemiain pages 10-11)

### 4.2 Pathogenic somatic variant classes (current understanding)
Authoritative 2023–2024 sources emphasize that *where* and *what type* of CEBPA mutation occurs matters for classification and prognosis:
- **bZIP in-frame insertions/deletions (bZIPInDel / CEBPAbZIP-inf):** central favorable-risk driver class in ELN 2022. (sargas2023comparisonofthe pages 1-2, mrozek2023outcomepredictionby pages 1-2)
- **Other bZIP lesions:** missense substitutions (bZIPms) and truncating/stop-inducing lesions (bZIPSTOP) are less favorable as a group than bZIPInDel in pooled analyses. (georgi2024prognosticimpactof pages 1-2, georgi2024prognosticimpactof pages 2-3)
- **N-terminal TAD mutations** and combinations with bZIP changes define classic “double-mutant” patterns; prognostic implications are heterogeneous and refined by domain/type. (georgi2024prognosticimpactof pages 1-2, rivera2023mutationsinthe pages 3-4)

### 4.3 Allelic state (monoallelic vs biallelic)
CEBPAdm (double-mutant/biallelic) and CEBPAsm (single-mutant) are widely used categories, but recent analyses suggest that **bZIP in-frame genotype** is more prognostically determinant than “biallelic” status alone. (georgi2024prognosticimpactof pages 1-2, sargas2023comparisonofthe pages 1-2)

### 4.4 Co-mutation patterns
- In one 2023 review synthesis, **CEBPAdm** commonly co-mutates with **GATA2, WT1, ASXL1, TET2, NRAS**, whereas **CEBPAsm** more often co-mutates with **FLT3, NPM1, IDH1/2, RUNX1** (also ASXL1, TET2). (yuan2023sporadicandfamilial pages 4-5)
- In an ELN-favorable bZIP-inframe cohort, **WT1** or **DNMT3A** co-mutation was associated with worse survival. (tien2024dysregulatedimmuneand pages 1-2)

### 4.5 Molecular profiling signals (recent 2024 work)
A 2024 transcriptomic study of CEBPAbZIP-inf AML linked poor outcomes to:
- Enrichment of **interferon (IFN) signaling** and **metabolic/mitochondrial pathways** (e.g., mitochondrial complex genes) in patients with shorter event-free survival. (tien2024dysregulatedimmuneand pages 1-2)

## 5. Mechanism / Pathophysiology
### 5.1 Causal chain (from mutation to phenotype)
A convergent mechanistic model supported by human and model-organism data:
1. **CEBPA alteration** (domain-specific mutation or isoform imbalance) perturbs transcriptional programs essential for granulocytic differentiation and normal myeloid maturation. (tawana2017familialcebpamutatedacute pages 1-4, brown2020secondaryleukemiain pages 10-11)
2. Disruption impairs the transition from **common myeloid progenitor (CMP) to granulocyte–macrophage progenitor (GMP)**, contributing to differentiation block and accumulation of blasts. (tawana2017familialcebpamutatedacute pages 1-4)
3. In some experimental settings, CEBPA alterations promote **HSPC expansion/self-renewal**, creating a substrate for leukemogenesis and clinical AML. (chen2024cebpaisrequired pages 1-2, chen2024cebpaisrequired pages 11-11)

### 5.2 Downstream targets and pathways
- CEBPA p42 drives myeloid differentiation by inducing targets including **SPI1, CSF3R, IL6R, GFI1B, KLF1, KLF5**; p30 can inhibit p42 activity. (brown2020secondaryleukemiain pages 10-11)
- In CEBPAbZIP-inf AML, poor-outcome signatures include IFN signaling and mitochondrial metabolic programs. (tien2024dysregulatedimmuneand pages 1-2)

### 5.3 Suggested ontology terms
- **GO Biological Process (examples):** granulocyte differentiation; myeloid cell differentiation; regulation of transcription by RNA polymerase II; hematopoietic stem cell proliferation; interferon signaling pathway; oxidative phosphorylation/mitochondrial electron transport (as pathway proxies for the transcriptomic signals). (tien2024dysregulatedimmuneand pages 1-2, tawana2017familialcebpamutatedacute pages 1-4, brown2020secondaryleukemiain pages 10-11, chen2024cebpaisrequired pages 1-2)
- **CL cell types (examples):** hematopoietic stem cell; common myeloid progenitor; granulocyte–macrophage progenitor; myeloblast. (tawana2017familialcebpamutatedacute pages 1-4, chen2024cebpaisrequired pages 1-2)

## 6. Anatomical Structures Affected
- **Primary site:** Bone marrow (hematopoietic tissue) with spillover of blasts into peripheral blood. (debnath2024prognosisandtreatment pages 1-2)
- **Secondary/extramedullary sites:** spleen, liver, skin, gums, CNS may be infiltrated. (rivera2023mutationsinthe pages 2-2, leoni2025…genemutationsby pages 11-15)

Suggested anatomy terms:
- **UBERON:** bone marrow; peripheral blood; spleen; liver; skin; central nervous system. (rivera2023mutationsinthe pages 2-2, leoni2025…genemutationsby pages 11-15, debnath2024prognosisandtreatment pages 1-2)

## 7. Temporal Development
- AML is generally acute/subacute in presentation, often with symptoms over weeks to months and complications of marrow failure. (leoni2025…genemutationsby pages 11-15)
- For familial/germline CEBPA predisposition (important differential when “somatic CEBPA AML” is suspected), N-terminal germline variants were reported with high penetrance and median onset ~25 years (range ~1.75–46), with most frequent presentation ages 21–30. (yuan2023sporadicandfamilial pages 4-5)

## 8. Inheritance and Population
### 8.1 Epidemiology
- General AML incidence reported as ~3–5 per 100,000 with average age ~65 years. (rivera2023mutationsinthe pages 2-2)
- CEBPA mutations are reported in ~5–14% of AML. (rivera2023mutationsinthe pages 2-2)
- In a uniformly treated adult cohort, 142/887 (16%) had CEBPA mutations and 113/887 (12.7%) had CEBPAbZIP-inf. (tien2024dysregulatedimmuneand pages 1-2)

### 8.2 Germline predisposition (distinct but clinically relevant)
- Familial CEBPA AML is autosomal dominant; onset can range from childhood to adulthood; familial cases may relapse as independent episodes and have high recurrence. (tawana2017familialcebpamutatedacute pages 1-4)
- Germline CEBPA predisposition frequency was reported as rare in AML (on the order of <1% in one review of germline TF predisposition). (brown2020secondaryleukemiain pages 10-11)

## 9. Diagnostics
### 9.1 Recommended molecular testing strategy for CEBPA
- **Full-length sequencing of CEBPA** (single exon) is recommended as the most comprehensive approach; targeted NGS panels are favored over Sanger due to higher sensitivity (~5% vs ~15–20%). (yuan2023sporadicandfamilial pages 4-5)
- **Capture-based NGS** is preferred over amplicon-based approaches for CEBPA because indels are common and the locus is GC-rich; fragment analysis can screen indels (analytic sensitivity ~5%) but cannot detect point mutations or precisely define indels. (yuan2023sporadicandfamilial pages 5-6)

### 9.2 Determining allelic state and excluding germline
- Routine short-read sequencing may not reliably determine cis/trans configuration for distant N- and C-terminal mutations. (yuan2023sporadicandfamilial pages 5-6)
- Germline testing requires non-hematopoietic tissue (cultured skin fibroblasts preferred in the reviewed guidance); persistence of a CEBPA variant at complete remission should trigger germline evaluation. (yuan2023sporadicandfamilial pages 5-6, yuan2023sporadicandfamilial pages 4-5)

### 9.3 MRD assessment
- Multiparameter flow cytometry (MFC) MRD is in clinical use; MRD positivity during consolidation predicted higher relapse and worse relapse-free survival in CEBPA-mutated AML in a review synthesis. (yuan2023sporadicandfamilial pages 5-6)

## 10. Outcome / Prognosis
### 10.1 Key prognostic concept (2023–2024 update)
A major 2022–2024 refinement is that favorable outcomes are best associated with **in-frame bZIP mutations** rather than “biallelic CEBPA” broadly. (sargas2023comparisonofthe pages 1-2, mrozek2023outcomepredictionby pages 1-2)

### 10.2 Recent statistics (prioritizing 2023–2024)
- **PETHEMA registry (2024, intensively treated):** CEBPA-bZIP-inframe patients had estimated **3-year OS 83.3%** (95% CI 58.3–100). (torre2024validationofmutated pages 1-2)
- **CEBPAbZIP-inf heterogeneity (2024):** in a cohort study, despite ELN-2022 favorable classification, **5-year EFS was <50% and cumulative relapse ~40%**, with worse survival in those co-mutated for **WT1 or DNMT3A**. (tien2024dysregulatedimmuneand pages 1-2)
- **Normal karyotype AML multivariable (2023):** bZIP in-frame CEBPA mutation was independently favorable (e.g., OS HR 0.49). (ahn2023clinicalsignificanceof pages 4-5)

### 10.3 Abstract-supported statements (direct quotes)
- ELN 2022 favorable-risk framing: “Acute myeloid leukemia (AML) with CEBPA bZIP in-frame mutations (CEBPAbZIP-inf) is classified within the favorable-risk group by the 2022 European LeukemiaNet (ELN-2022). However, heterogeneous clinical outcomes are still observed in these patients.” (tien2024dysregulatedimmuneand pages 1-2)
- Molecular findings linked to poor outcome: “Concurrent WT1 or DNMT3A mutations significantly predicted worse survival…” (tien2024dysregulatedimmuneand pages 1-2)

## 11. Treatment
### 11.1 Standard of care (real-world implementation)
- A recent review notes AML-CEBPA is chemosensitive and commonly treated with **anthracycline + cytarabine induction** and consolidation. (yuan2023sporadicandfamilial pages 5-6)

### 11.2 Allogeneic HSCT considerations
- For germline/familial CEBPA AML, relapse can be frequent and may represent independent episodes; allogeneic HSCT is considered in recurrent/high-risk settings (also to avoid transplanting from a related donor who may carry the germline variant). (tawana2017familialcebpamutatedacute pages 1-4)
- In bZIP-inframe AML with poor-outcome biology (e.g., adverse co-mutations or transcriptomic risk states), authors have suggested that upfront allo-transplant may improve long-term control. (tien2024dysregulatedimmuneand pages 1-2)

### 11.3 Clinical trials (examples from ClinicalTrials.gov)
- **NCT06458257:** observational study evaluating allogeneic HSCT in “high-relapse-risk CEBPA mutant AML.” (rivera2023mutationsinthe pages 3-4)
- **NCT06529250 / NCT04415008:** HAD-based intensified cytarabine regimens for CEBPA double-mutated AML. (rivera2023mutationsinthe pages 3-4)
- **NCT07451912:** venetoclax + hypomethylating agents + subcutaneous cytarabine for CEBPA-mutated AML. (rivera2023mutationsinthe pages 3-4)

### 11.4 Suggested MAXO terms (examples)
- Induction chemotherapy; Consolidation chemotherapy; Allogeneic hematopoietic stem cell transplantation; Measurable residual disease monitoring; Targeted therapy with BCL2 inhibitor (venetoclax-based regimen). (tien2024dysregulatedimmuneand pages 1-2, rivera2023mutationsinthe pages 3-4, yuan2023sporadicandfamilial pages 5-6)

## 12. Prevention
- **Primary prevention (AML overall):** reduction of exposure to established leukemogens (e.g., benzene) and avoiding unnecessary ionizing radiation where feasible; these are supported as risk factors in AML review literature, but specific prevention trials for this entity were not found in the retrieved corpus. (shen2023associationbetweenmetal(loid)s pages 1-2, marrero2023currentlandscapeof pages 1-2)
- **Secondary prevention:** no population screening specific to CEBPA somatic AML; however, in suspected hereditary contexts (familial AML), genetic counseling and constitutional testing can guide surveillance and donor selection. (yuan2023sporadicandfamilial pages 5-6, tawana2017familialcebpamutatedacute pages 1-4)

## 13. Other Species / Natural Disease
No naturally occurring non-human “CEBPA-mutated AML” entity was identified in the retrieved texts; mechanistic insights rely primarily on engineered or experimentally induced models (see Model Organisms).

## 14. Model Organisms
### 14.1 Zebrafish
- Zebrafish cebpa mutants were used to define roles of Cebpa in HSPC generation and myeloid differentiation; complete loss reduced early HSPC generation and increased apoptosis; epistasis placed Cebpa downstream of Runx1. (chen2024cebpaisrequired pages 1-2, chen2024cebpaisrequired pages 6-7)

### 14.2 Mouse
- CEBPA knockout mice demonstrate granulopoiesis defects (“lack mature granulocytes”), supporting CEBPA’s essential role in granulocyte development. (faisal2023locationlocationlocation pages 1-3)
- A knock-in model with C-terminal/bZIP in-frame mutation (CEBPAK313KK) has been described as promoting intrinsic HSPC expansion and accelerating AML progression in a mutant background. (chen2024cebpaisrequired pages 11-11)

## Evidence Map (2022–2024 classification/prognosis/diagnostics)
The following table consolidates high-yield evidence items (classification criteria, prognosis statistics, diagnostics/MRD notes, and example clinical trials) for rapid knowledge-base extraction.

| Topic | Key points | Study/source (author year journal) | PMID | URL | Evidence context ID(s) |
|---|---|---|---|---|---|
| WHO 2022 classification | WHO 2022 entity is “AML with CEBPA mutation”; includes both biallelic CEBPA and single mutations in the basic leucine zipper (bZIP) region; blast threshold described as ≥20% for this context in comparative reviews. | Park 2024 *Blood Research* |  | https://doi.org/10.1007/s44313-024-00016-8 | (park2024whatisnew pages 1-2, park2024whatisnew pages 2-3) |
| ICC 2022 classification | ICC 2022 entity is “AML with mutated bZIP CEBPA”; focuses on in-frame bZIP CEBPA mutations and uses a ≥10% blast threshold for recurrent genetic abnormality-defined AML. | Salman 2024 *Cancers*; Park 2024 *Blood Research* |  | https://doi.org/10.3390/cancers16162915 ; https://doi.org/10.1007/s44313-024-00016-8 | (salman2024comparativeanalysisof pages 2-4, park2024whatisnew pages 1-2, salman2024comparativeanalysisof pages 4-6) |
| ELN 2022 risk definition | ELN 2022 favorable-risk category replaced “biallelic CEBPA” with in-frame bZIP CEBPA mutations, irrespective of monoallelic vs biallelic status. | Sargas 2023 *Blood Cancer Journal*; Huber 2023 *Leukemia*; Mrózek 2023 *Leukemia* |  | https://doi.org/10.1038/s41408-023-00835-5 ; https://doi.org/10.1038/s41375-023-01909-w ; https://doi.org/10.1038/s41375-023-01846-8 | (sargas2023comparisonofthe pages 1-2, huber2023amlclassificationin pages 1-2, mrozek2023outcomepredictionby pages 1-2) |
| Prognostic subgroup refinement | In pooled analysis of 1,010 adult CEBPA-mutant AML cases, only bZIP in-frame insertion/deletion (bZIPInDel) cases had significantly higher CR rates and longer relapse-free and overall survival than other CEBPA-mutant subgroups; bZIPSTOP, bZIP missense, and TAD-mutant groups were less favorable. | Georgi 2024 *Leukemia* |  | https://doi.org/10.1038/s41375-024-02140-x | (georgi2024prognosticimpactof pages 1-2, georgi2024prognosticimpactof pages 2-3) |
| Prognosis in CEBPAbZIP-inf with co-mutations | In 887 non-M3 AML patients, 142/887 (16%) had CEBPA mutations and 113/887 (12.7%) had CEBPAbZIP-inf; 96/113 (85.0%) biallelic. Despite favorable ELN assignment, 5-year EFS was reported as <50% and cumulative relapse near 40%; concurrent WT1 or DNMT3A predicted worse survival. | Tien 2024 *Blood Cancer Journal* |  | https://doi.org/10.1038/s41408-023-00975-8 | (tien2024dysregulatedimmuneand pages 1-2) |
| PETHEMA registry outcomes | In 696 intensively treated AML patients, 82 (11.8%) had CEBPA mutations; 45 had bZIP mutations and 40 had CEBPA-bZIP-inf (5.7%). Estimated 3-year OS was 83.3% (95% CI 58.3–100) for CEBPA-bZIP-inf vs 54.3% for other CEBPA mutations and 47.2% for CEBPA wild type; historical relapse risk cited ~40% for CEBPAdm vs ~60% for CEBPAsm. | De la Torre 2024 *Haematologica* |  | https://doi.org/10.3324/haematol.2023.284601 | (torre2024validationofmutated pages 1-2) |
| Normal-karyotype AML multivariable outcomes | In normal-karyotype AML, bZIP in-frame CEBPA mutation was an independent favorable factor: CR OR 3.97 (95% CI 1.16–13.50, p=0.028), OS HR 0.49 (0.30–0.81, p=0.006), RFS HR 0.56 (0.35–0.91, p=0.019), CIR HR 0.49 (0.25–0.96, p=0.036). FLT3-ITD remained adverse. | Ahn 2023 *Cancer Research and Treatment* |  | https://doi.org/10.4143/crt.2022.1407 | (ahn2023clinicalsignificanceof pages 4-5) |
| Mini-review summary of older cohorts | Review summarized favorable outcomes for biallelic and monoallelic in-frame bZIP groups: median OS 103.2 months for CEBPAbi vs 21.9 months for CEBPAmono vs 19.3 months for CEBPAwt; pediatric series showed CR 87.7% vs 76.9% and MRD-negative CR 83.4% vs 70.5% for CEBPAm vs CEBPAwt; 5-year EFS/OS around 64%/81–89% for CEBPAbi and CEBPAsmbZIP in cited cohorts. | Faisal 2023 *Leukemia Research Reports* |  | https://doi.org/10.1016/j.lrr.2023.100386 | (faisal2023locationlocationlocation pages 1-3) |
| Diagnostic testing: sequencing strategy | Full-length sequencing of the single-exon CEBPA gene is recommended; routine NGS panels are favored over Sanger because of higher sensitivity (~5% for NGS vs ~15–20% for Sanger). Capture-based NGS is preferred over amplicon-based approaches for CEBPA because indels are common and GC-rich sequence complicates testing. | Yuan 2023 *Current Hematologic Malignancy Reports* |  | https://doi.org/10.1007/s11899-023-00699-3 | (yuan2023sporadicandfamilial pages 5-6, yuan2023sporadicandfamilial pages 4-5) |
| Diagnostic testing: fragment analysis | Fragment analysis can be used pragmatically to screen for indels in resource-limited settings with analytic sensitivity around 5%, but it cannot detect point mutations or precisely define indel sequence/size. | Yuan 2023 *Current Hematologic Malignancy Reports* |  | https://doi.org/10.1007/s11899-023-00699-3 | (yuan2023sporadicandfamilial pages 5-6) |
| Diagnostic testing: allelic status/germline caveat | Standard Sanger or short-read routine NGS cannot reliably establish cis/trans configuration for distant N- and C-terminal mutations; constitutional non-hematopoietic tissue (cultured skin fibroblasts preferred) is required to confirm germline status. Persistence of CEBPA mutation in remission should prompt germline evaluation. | Yuan 2023 *Current Hematologic Malignancy Reports* |  | https://doi.org/10.1007/s11899-023-00699-3 | (yuan2023sporadicandfamilial pages 5-6, yuan2023sporadicandfamilial pages 4-5) |
| MRD notes | Multiparametric flow cytometry (MFC) MRD is in clinical use; MRD positivity during consolidation (rather than necessarily after induction) predicts higher relapse and worse RFS. “Low-risk MRD” was defined as negative MRD after at least two consolidation cycles and associated with better RFS/OS. | Yuan 2023 *Current Hematologic Malignancy Reports* |  | https://doi.org/10.1007/s11899-023-00699-3 | (yuan2023sporadicandfamilial pages 5-6) |
| Clinical trial example | NCT06458257: “The Efficacy of Allogeneic Hematopoietic Stem Cell Transplantation in Newly Diagnosed High-relapse-risk CEBPA Mutant Acute Myeloid Leukemia”; recruiting observational study; target enrollment 50. | ClinicalTrials.gov record |  | https://clinicaltrials.gov/study/NCT06458257 | (rivera2023mutationsinthe pages 3-4) |
| Clinical trial example | NCT06529250: “Intermediate-dose HAD Regimen for CEBPA Double-mutated AML”; recruiting interventional study; phase NA; enrollment 148. | ClinicalTrials.gov record |  | https://clinicaltrials.gov/study/NCT06529250 | (rivera2023mutationsinthe pages 3-4) |
| Clinical trial example | NCT04415008: “Efficacy of HAD Induction With Intensified Cytarabine in Newly-diagnosed CEBPA Double Mutated Acute Myeloid Leukemia”; active, not recruiting; phase 2; enrollment 61. | ClinicalTrials.gov record |  | https://clinicaltrials.gov/study/NCT04415008 | (rivera2023mutationsinthe pages 3-4) |
| Clinical trial example | NCT07451912: “Venetoclax Plus Hypomethylating Agents and Subcutaneous Cytarabine for CEBPA-Mutated AML”; recruiting interventional study; phase 1/2; enrollment 29. | ClinicalTrials.gov record |  | https://clinicaltrials.gov/study/NCT07451912 | (rivera2023mutationsinthe pages 3-4) |


*Table: This table consolidates classification criteria, prognosis, diagnostics/MRD, and example clinical trials for AML with CEBPA mutations. It is useful as a compact evidence map for populating a disease knowledge base entry with recent, citable findings.*

## Key limitations of this evidence snapshot
1. Ontology identifiers (MONDO/MeSH/ICD/Orphanet/OMIM) for the specific “AML with CEBPA somatic mutations” entity were not present in the retrieved full texts and therefore could not be cited here.
2. Many phenotype frequencies for the somatic (non-familial) CEBPA-mutated AML subgroup are not consistently reported in the retrieved 2023–2024 sources; most symptom frequencies derive from AML-wide literature.
3. Variant-level population allele frequencies (gnomAD) and clinical variant assertions (ClinVar/COSMIC IDs) were not retrieved in this run.


References

1. (debnath2024prognosisandtreatment pages 1-2): Ankita Debnath and Sukanta Nath. Prognosis and treatment in acute myeloid leukemia: a comprehensive review. Egyptian Journal of Medical Human Genetics, Aug 2024. URL: https://doi.org/10.1186/s43042-024-00563-w, doi:10.1186/s43042-024-00563-w. This article has 21 citations and is from a peer-reviewed journal.

2. (sargas2023comparisonofthe pages 1-2): Claudia Sargas, Rosa Ayala, María J. Larráyoz, María C. Chillón, Eduardo Rodriguez-Arboli, Cristina Bilbao, Esther Prados de la Torre, David Martínez-Cuadrón, Rebeca Rodríguez-Veiga, Blanca Boluda, Cristina Gil, Teresa Bernal, Juan Bergua, Lorenzo Algarra, Mar Tormo, Pilar Martínez-Sánchez, Elena Soria, Josefina Serrano, Juan M. Alonso-Dominguez, Raimundo García, María Luz Amigo, Pilar Herrera-Puente, María J. Sayas, Esperanza Lavilla-Rubira, Joaquín Martínez-López, María J. Calasanz, Ramón García-Sanz, José A. Pérez-Simón, María T. Gómez Casares, Joaquín Sánchez-García, Eva Barragán, Pau Montesinos, and Esther Prados de la Torre. Comparison of the 2022 and 2017 european leukemianet risk classifications in a real-life cohort of the pethema group. Blood Cancer Journal, May 2023. URL: https://doi.org/10.1038/s41408-023-00835-5, doi:10.1038/s41408-023-00835-5. This article has 40 citations and is from a domain leading peer-reviewed journal.

3. (mrozek2023outcomepredictionby pages 1-2): Krzysztof Mrózek, Jessica Kohlschmidt, James S. Blachly, Deedra Nicolet, Andrew J. Carroll, Kellie J. Archer, Alice S. Mims, Karilyn T. Larkin, Shelley Orwick, Christopher C. Oakes, Jonathan E. Kolitz, Bayard L. Powell, William G. Blum, Guido Marcucci, Maria R. Baer, Geoffrey L. Uy, Wendy Stock, John C. Byrd, and Ann-Kathrin Eisfeld. Outcome prediction by the 2022 european leukemianet genetic-risk classification for adults with acute myeloid leukemia: an alliance study. Leukemia, 37:788-798, Feb 2023. URL: https://doi.org/10.1038/s41375-023-01846-8, doi:10.1038/s41375-023-01846-8. This article has 85 citations and is from a highest quality peer-reviewed journal.

4. (park2024whatisnew pages 1-2): Hee Sue Park. What is new in acute myeloid leukemia classification? Blood Research, Apr 2024. URL: https://doi.org/10.1007/s44313-024-00016-8, doi:10.1007/s44313-024-00016-8. This article has 39 citations.

5. (park2024whatisnew pages 2-3): Hee Sue Park. What is new in acute myeloid leukemia classification? Blood Research, Apr 2024. URL: https://doi.org/10.1007/s44313-024-00016-8, doi:10.1007/s44313-024-00016-8. This article has 39 citations.

6. (salman2024comparativeanalysisof pages 2-4): Huda Salman. Comparative analysis of aml classification systems: evaluating the who, icc, and eln frameworks and their distinctions. Cancers, 16:2915, Aug 2024. URL: https://doi.org/10.3390/cancers16162915, doi:10.3390/cancers16162915. This article has 10 citations.

7. (tien2024dysregulatedimmuneand pages 1-2): Feng-Ming Tien, Chi-Yuan Yao, Xavier Cheng-Hong Tsai, Min-Yen Lo, Chien-Yuan Chen, Wan-Hsuan Lee, Chien-Chin Lin, Yuan-Yeh Kuo, Yen-Ling Peng, Mei-Hsuan Tseng, Yu-Sin Wu, Ming-Chih Liu, Liang-In Lin, Ming-Kai Chuang, Bor-Sheng Ko, Ming Yao, Jih-Luh Tang, Wen-Chien Chou, Hsin-An Hou, and Hwei-Fang Tien. Dysregulated immune and metabolic pathways are associated with poor survival in adult acute myeloid leukemia with cebpa bzip in-frame mutations. Blood Cancer Journal, Jan 2024. URL: https://doi.org/10.1038/s41408-023-00975-8, doi:10.1038/s41408-023-00975-8. This article has 16 citations and is from a domain leading peer-reviewed journal.

8. (yuan2023sporadicandfamilial pages 5-6): Ji Yuan, Rong He, and Hassan B. Alkhateeb. Sporadic and familial acute myeloid leukemia with cebpa mutations. Current Hematologic Malignancy Reports, 18:121-129, Jun 2023. URL: https://doi.org/10.1007/s11899-023-00699-3, doi:10.1007/s11899-023-00699-3. This article has 12 citations.

9. (salman2024comparativeanalysisof media e167dd0e): Huda Salman. Comparative analysis of aml classification systems: evaluating the who, icc, and eln frameworks and their distinctions. Cancers, 16:2915, Aug 2024. URL: https://doi.org/10.3390/cancers16162915, doi:10.3390/cancers16162915. This article has 10 citations.

10. (georgi2024prognosticimpactof pages 1-2): Julia-Annabell Georgi, Sebastian Stasik, Michael Kramer, Manja Meggendorfer, Christoph Röllig, Torsten Haferlach, Peter Valk, David Linch, Tobias Herold, Nicolas Duployez, Franziska Taube, Jan Moritz Middeke, Uwe Platzbecker, Hubert Serve, Claudia D. Baldus, Carsten Muller-Tidow, Claudia Haferlach, Sarah Koch, Wolfgang E. Berdel, Bernhard J. Woermann, Utz Krug, Jan Braess, Wolfgang Hiddemann, Karsten Spiekermann, Emma L. Boertjes, Robert K. Hills, Alan Burnett, Gerhard Ehninger, Klaus Metzeler, Maja Rothenberg-Thurley, Annika Dufour, Hervé Dombret, Cecile Pautas, Claude Preudhomme, Laurene Fenwarth, Martin Bornhäuser, Rosemary Gale, and Christian Thiede. Prognostic impact of cebpa mutational subgroups in adult aml. Leukemia, 38:281-290, Jan 2024. URL: https://doi.org/10.1038/s41375-024-02140-x, doi:10.1038/s41375-024-02140-x. This article has 32 citations and is from a highest quality peer-reviewed journal.

11. (faisal2023locationlocationlocation pages 1-3): Muhammad Salman Faisal and Pamela J. Sung. Location, location, location: a mini-review of cebpa variants in patients with acute myeloid leukemia. Leukemia Research Reports, 20:100386, Jan 2023. URL: https://doi.org/10.1016/j.lrr.2023.100386, doi:10.1016/j.lrr.2023.100386. This article has 3 citations.

12. (yuan2023sporadicandfamilial pages 4-5): Ji Yuan, Rong He, and Hassan B. Alkhateeb. Sporadic and familial acute myeloid leukemia with cebpa mutations. Current Hematologic Malignancy Reports, 18:121-129, Jun 2023. URL: https://doi.org/10.1007/s11899-023-00699-3, doi:10.1007/s11899-023-00699-3. This article has 12 citations.

13. (tawana2017familialcebpamutatedacute pages 1-4): Kiran Tawana, Ana Rio-Machin, Claude Preudhomme, and Jude Fitzgibbon. Familial cebpa-mutated acute myeloid leukemia. Seminars in hematology, 54 2:87-93, Apr 2017. URL: https://doi.org/10.1053/j.seminhematol.2017.04.001, doi:10.1053/j.seminhematol.2017.04.001. This article has 76 citations and is from a peer-reviewed journal.

14. (marrero2023currentlandscapeof pages 1-2): Richard J. Marrero and Jatinder K. Lamba. Current landscape of genome-wide association studies in acute myeloid leukemia: a review. Cancers, 15:3583, Jul 2023. URL: https://doi.org/10.3390/cancers15143583, doi:10.3390/cancers15143583. This article has 14 citations.

15. (shen2023associationbetweenmetal(loid)s pages 1-2): Chengchen Shen, Kui Zhang, Jingxuan Yang, Jingyi Shi, Chan Yang, Yanan Sun, and Wenxing Yang. Association between metal(loid)s in serum and leukemia: a systematic review and meta-analysis. Journal of Environmental Health Science and Engineering, 21:201-213, Feb 2023. URL: https://doi.org/10.1007/s40201-023-00853-2, doi:10.1007/s40201-023-00853-2. This article has 14 citations.

16. (sandoval2023anupdatedoverview pages 7-9): Cristian Sandoval, Yolanda Calle, Karina Godoy, and Jorge Farías. An updated overview of the role of cyp450 during xenobiotic metabolization in regulating the acute myeloid leukemia microenvironment. International Journal of Molecular Sciences, 24:6031, Mar 2023. URL: https://doi.org/10.3390/ijms24076031, doi:10.3390/ijms24076031. This article has 7 citations.

17. (rivera2023mutationsinthe pages 2-2): Juan Carlos Rivera, Daniel Nuñez, Elizabet Millar, Kimberly Ramirez, Mauricio Chandía, and Claudio Aguayo. Mutations in the bzip region of the cebpa gene: a novel prognostic factor in patients with acute myeloid leukemia. International Journal of Laboratory Hematology, 45:833-838, Aug 2023. URL: https://doi.org/10.1111/ijlh.14157, doi:10.1111/ijlh.14157. This article has 3 citations and is from a peer-reviewed journal.

18. (leoni2025…genemutationsby pages 11-15): A Leoni. … gene-mutations by digital (dpcr) ngs driven in patients with acute myeloid leukemias (amls) and high-risk myelodysplastic syndromes (hr-mdss)-“dpcr-ngs …. Unknown journal, 2025.

19. (brown2020secondaryleukemiain pages 10-11): Anna L. Brown, Christopher N. Hahn, and Hamish S. Scott. Secondary leukemia in patients with germline transcription factor mutations (runx1, gata2, cebpa). Blood, 136:24-35, Jul 2020. URL: https://doi.org/10.1182/blood.2019000937, doi:10.1182/blood.2019000937. This article has 100 citations and is from a highest quality peer-reviewed journal.

20. (georgi2024prognosticimpactof pages 2-3): Julia-Annabell Georgi, Sebastian Stasik, Michael Kramer, Manja Meggendorfer, Christoph Röllig, Torsten Haferlach, Peter Valk, David Linch, Tobias Herold, Nicolas Duployez, Franziska Taube, Jan Moritz Middeke, Uwe Platzbecker, Hubert Serve, Claudia D. Baldus, Carsten Muller-Tidow, Claudia Haferlach, Sarah Koch, Wolfgang E. Berdel, Bernhard J. Woermann, Utz Krug, Jan Braess, Wolfgang Hiddemann, Karsten Spiekermann, Emma L. Boertjes, Robert K. Hills, Alan Burnett, Gerhard Ehninger, Klaus Metzeler, Maja Rothenberg-Thurley, Annika Dufour, Hervé Dombret, Cecile Pautas, Claude Preudhomme, Laurene Fenwarth, Martin Bornhäuser, Rosemary Gale, and Christian Thiede. Prognostic impact of cebpa mutational subgroups in adult aml. Leukemia, 38:281-290, Jan 2024. URL: https://doi.org/10.1038/s41375-024-02140-x, doi:10.1038/s41375-024-02140-x. This article has 32 citations and is from a highest quality peer-reviewed journal.

21. (rivera2023mutationsinthe pages 3-4): Juan Carlos Rivera, Daniel Nuñez, Elizabet Millar, Kimberly Ramirez, Mauricio Chandía, and Claudio Aguayo. Mutations in the bzip region of the cebpa gene: a novel prognostic factor in patients with acute myeloid leukemia. International Journal of Laboratory Hematology, 45:833-838, Aug 2023. URL: https://doi.org/10.1111/ijlh.14157, doi:10.1111/ijlh.14157. This article has 3 citations and is from a peer-reviewed journal.

22. (chen2024cebpaisrequired pages 1-2): Kemin Chen, Jieyi Wu, Yuxian Zhang, Wei Liu, Xiaohui Chen, Wenqing Zhang, and Zhibin Huang. Cebpa is required for haematopoietic stem and progenitor cell generation and maintenance in zebrafish. Open Biology, Nov 2024. URL: https://doi.org/10.1098/rsob.240215, doi:10.1098/rsob.240215. This article has 2 citations and is from a peer-reviewed journal.

23. (chen2024cebpaisrequired pages 11-11): Kemin Chen, Jieyi Wu, Yuxian Zhang, Wei Liu, Xiaohui Chen, Wenqing Zhang, and Zhibin Huang. Cebpa is required for haematopoietic stem and progenitor cell generation and maintenance in zebrafish. Open Biology, Nov 2024. URL: https://doi.org/10.1098/rsob.240215, doi:10.1098/rsob.240215. This article has 2 citations and is from a peer-reviewed journal.

24. (torre2024validationofmutated pages 1-2): Esther Prados De la Torre, Josefina Serrano, David Martínez-Cuadrón, Laura Torres, Claudia Sargas, Rosa Ayala, Cristina Bilbao-Sieyro, María Carmen Chillón, María José Larráyoz, Elena Soria, Clara Aparicio-Pérez, Juan M. Bergua, Teresa Bernal, Cristina Gil, Mar Tormo, Lorenzo Algarra, Juan M. Alonso-Domínguez, Eduardo Rodriguez-Arbolí, Pilar Martínez-Sanchez, Ana Oliva, Ana M. Colorado-Araujo, Carlos Rodríguez-Medina, Susana Vives, Lourdes Hermosín, Joaquín Martínez-López, Ramón García-Sanz, José A. Pérez-Simón, María José Calasanz, María Teresa Gómez-Casares, Eva Barragán, Joaquín Sánchez-García J, and Pau Montesinos. Validation of mutated cebpa bzip as a distinct prognosis entity in acute myeloid leukemia: a study by the spanish pethema registry. Haematologica, 109:2682-2687, Apr 2024. URL: https://doi.org/10.3324/haematol.2023.284601, doi:10.3324/haematol.2023.284601. This article has 8 citations.

25. (ahn2023clinicalsignificanceof pages 4-5): Seo-Yeon Ahn, TaeHyung Kim, Mihee Kim, Ga-Young Song, Sung-Hoon Jung, Deok-Hwan Yang, Je-Jung Lee, Mi Yeon Kim, Chul Won Jung, Jun-Ho Jang, Hee Je Kim, Joon Ho Moon, Sang Kyun Sohn, Jong-Ho Won, Sung-Hyun Kim, Hyeoung-Joon Kim, Jae-Sook Ahn, and Dennis Dong Hwan Kim. Clinical significance of bzip in-frame cebpa-mutated normal karyotype acute myeloid leukemia. Cancer Research and Treatment, 55:1011-1022, Jul 2023. URL: https://doi.org/10.4143/crt.2022.1407, doi:10.4143/crt.2022.1407. This article has 8 citations and is from a peer-reviewed journal.

26. (chen2024cebpaisrequired pages 6-7): Kemin Chen, Jieyi Wu, Yuxian Zhang, Wei Liu, Xiaohui Chen, Wenqing Zhang, and Zhibin Huang. Cebpa is required for haematopoietic stem and progenitor cell generation and maintenance in zebrafish. Open Biology, Nov 2024. URL: https://doi.org/10.1098/rsob.240215, doi:10.1098/rsob.240215. This article has 2 citations and is from a peer-reviewed journal.

27. (salman2024comparativeanalysisof pages 4-6): Huda Salman. Comparative analysis of aml classification systems: evaluating the who, icc, and eln frameworks and their distinctions. Cancers, 16:2915, Aug 2024. URL: https://doi.org/10.3390/cancers16162915, doi:10.3390/cancers16162915. This article has 10 citations.

28. (huber2023amlclassificationin pages 1-2): Sandra Huber, Constance Baer, Stephan Hutter, Frank Dicker, Manja Meggendorfer, Christian Pohlkamp, Wolfgang Kern, Torsten Haferlach, Claudia Haferlach, and Gregor Hoermann. Aml classification in the year 2023: how to avoid a babylonian confusion of languages. Leukemia, 37:1413-1420, Apr 2023. URL: https://doi.org/10.1038/s41375-023-01909-w, doi:10.1038/s41375-023-01909-w. This article has 95 citations and is from a highest quality peer-reviewed journal.
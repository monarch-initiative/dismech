---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:54:48.016789'
end_time: '2026-05-09T12:11:05.283581'
duration_seconds: 977.27
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Medulloblastoma, SHH-Activated
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Medulloblastoma, SHH-Activated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Medulloblastoma, SHH-Activated** covering all of the
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
- **Disease Name:** Medulloblastoma, SHH-Activated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Medulloblastoma, SHH-Activated** covering all of the
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


# Medulloblastoma, SHH-Activated — Disease Characteristics Research Report (2026-05-09)

## Target Disease
- **Disease name:** Medulloblastoma, SHH-Activated (Sonic Hedgehog pathway–activated medulloblastoma)
- **Category:** Malignant embryonal tumor of the cerebellum/posterior fossa; molecularly defined medulloblastoma subgroup.
- **MONDO / OMIM / Orphanet / ICD / MeSH identifiers:** Not reliably retrievable with the available tool corpus in this run; recommended to cross-map in MONDO/Orphanet/MeSH/ICD using the term *“Medulloblastoma, SHH-activated”* and *WHO CNS5* entity names.

---

## 1. Disease Information
### 1.1 Overview and current definition
SHH-activated medulloblastoma is a molecularly defined subgroup of medulloblastoma characterized by activation of Sonic Hedgehog signaling and recognized in the **WHO 2021 (WHO CNS5)** integrated classification framework. WHO CNS5 further separates SHH-activated medulloblastoma into **TP53-wildtype** and **TP53-mutant** types, reflecting major prognostic differences. (koch2025thecurrentlandscape pages 2-4)

### 1.2 Common synonyms / alternative names
- “SHH medulloblastoma”
- “Sonic Hedgehog medulloblastoma”
- “Hedgehog pathway–activated medulloblastoma”
- “SHH-activated medulloblastoma, TP53-wildtype”
- “SHH-activated medulloblastoma, TP53-mutant” (koch2025thecurrentlandscape pages 2-4)

### 1.3 Evidence source types
The evidence supporting disease definition and subclassification here is derived from **aggregated disease-level resources** (reviews and multi-institutional cohorts) and **clinical trial registries** (ClinicalTrials.gov), not EHR data. (koch2025thecurrentlandscape pages 2-4, NCT01708174 chunk 1, NCT00939484 chunk 1)

---

## 2. Etiology
### 2.1 Primary causal/mechanistic factors
SHH-activated medulloblastoma is driven by genomic events that activate Hedgehog signaling at the level of pathway repressors and transducers (e.g., **PTCH1**, **SMO**, **SUFU**) and downstream effectors (e.g., **GLI2** amplification), often in age-dependent patterns. (koch2025thecurrentlandscape pages 2-4, kim2025advancingmedulloblastomatherapy pages 4-6)

### 2.2 Risk factors
#### Genetic risk factors
- **Germline predisposition** is enriched in SHH tumors compared with other medulloblastoma groups and includes:
  - **Gorlin syndrome** (classically **PTCH1**; also **SUFU**) (koch2025thecurrentlandscape pages 2-4, kim2025advancingmedulloblastomatherapy pages 4-6)
  - **Li–Fraumeni syndrome** (**TP53**) (koch2025thecurrentlandscape pages 2-4)

#### Environmental risk factors
No specific, well-supported environmental exposures were identified in the retrieved sources for SHH-activated medulloblastoma.

### 2.3 Protective factors
Protective factors were not identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No SHH-specific gene–environment interaction evidence was identified in the retrieved corpus.

---

## 3. Phenotypes
### 3.1 Clinical presentation (typical)
SHH-activated medulloblastoma commonly presents with symptoms and signs attributable to a posterior fossa mass and/or hydrocephalus. In adolescents/young adults (AYAs), reported presenting symptoms include nausea/vomiting, headache, and ataxia, with potential diagnostic delay. (ruggiero2026medulloblastomainadolescents pages 2-4)

### 3.2 Age distribution and anatomic tendencies
- SHH tumors show a **bimodal** age distribution enriched in **infants (<3 years)** and **adults**. (ruggiero2026medulloblastomainadolescents pages 2-4, koch2025thecurrentlandscape pages 2-4)
- In adults, SHH molecular signature is common among medulloblastomas (reported ~70% in an adult series context statement). (korshunov2021integratedmolecularanalysis pages 1-2)

### 3.3 HPO term suggestions (non-exhaustive)
Common clinical manifestations to map:
- Headache — **HP:0002315**
- Nausea — **HP:0002018**
- Vomiting — **HP:0002013**
- Ataxia — **HP:0001251**
- Hydrocephalus — **HP:0000238**
- Increased intracranial pressure — **HP:0002516**

*(Ontology suggestions are provided for KB normalization; frequencies were not consistently extractable from the retrieved SHH-specific sources.)*

---

## 4. Genetic / Molecular Information
### 4.1 Key causal/driver genes and alterations
Common SHH-pathway drivers and subgroup modifiers include:
- **PTCH1** (loss-of-function; germline or somatic), **SMO** (activating), **SUFU** (loss-of-function), **GLI2/GLI1 amplification**, **MYCN amplification**, **TP53** alteration (esp. high-risk childhood), and **TERT promoter** mutation in adult-associated SHH subtypes. (koch2025thecurrentlandscape pages 2-4, kim2025advancingmedulloblastomatherapy pages 4-6, ruggiero2026medulloblastomainadolescents pages 2-4)

A review table summarizing major SHH alterations lists **TP53, TERT, PTCH1** and also **GLI2, SMO, SUFU** as commonly reported alterations in SHH medulloblastoma. (slika2023theneurodevelopmentaland pages 1-2)

### 4.2 DNA methylation / transcriptomic subclasses
Two widely used frameworks appear in the retrieved evidence:
1) **SHH-α / SHH-β / SHH-γ / SHH-δ** (Cavalli-style) subclasses with age associations (infant vs child vs adult) and distinct genomics including **TERT promoter** enrichment in adult-associated classes. (korshunov2021integratedmolecularanalysis pages 2-3, ruggiero2026medulloblastomainadolescents pages 2-4, kim2025advancingmedulloblastomatherapy pages 4-6)
2) **WHO 2021 early-childhood SHH methylation classes**: **SHH-1, SHH-2, SHH-3**, with evidence that **SHH-2** can be further divided into **SHH-2a** and **SHH-2b** with distinct relapse risk in radiation-avoiding cohorts. (tonn2023riskpredictionin pages 1-2)

### 4.3 Somatic vs germline
Both germline and somatic alterations contribute:
- Germline: PTCH/SUFU (Gorlin), TP53 (Li–Fraumeni). (koch2025thecurrentlandscape pages 2-4, kim2025advancingmedulloblastomatherapy pages 4-6)
- Somatic: PTCH1/SMO/SUFU mutations and amplifications (e.g., GLI2, MYCN). (kim2025advancingmedulloblastomatherapy pages 4-6, ruggiero2026medulloblastomainadolescents pages 2-4)

### 4.4 Epigenetics
Genome-wide DNA methylation signatures are clinically leveraged for medulloblastoma subgrouping and SHH subclassification (e.g., Heidelberg classifier use in cohorts and trials). (tonn2023riskpredictionin pages 3-5, NCT01708174 chunk 1)

---

## 5. Mechanism / Pathophysiology
### 5.1 Core pathway mechanism (causal chain)
A simplified causal chain consistent with retrieved clinical/translational sources:
1) **Genomic activation of the SHH pathway** via loss of negative regulation (PTCH1/SUFU) or activation of transduction (SMO) (kim2025advancingmedulloblastomatherapy pages 4-6, ruggiero2026medulloblastomainadolescents pages 2-4)
2) **GLI transcription factor program activation** (downstream of SMO/SUFU axis) promoting proliferation/survival programs in cerebellar developmental lineages (kim2025advancingmedulloblastomatherapy pages 4-6)
3) Emergence of SHH medulloblastoma with subgroup-specific patterns of chromosomal alterations and oncogene amplification (e.g., MYCN/GLI2) that influence aggressiveness and treatment response (kim2025advancingmedulloblastomatherapy pages 4-6, ruggiero2026medulloblastomainadolescents pages 2-4)

### 5.2 Cell(s) of origin / lineage context
SHH tumors are described as arising from cerebellar granule neuron precursor lineage / granule lineage precursors (broadly consistent across review and AYA-focused summaries). (ruggiero2026medulloblastomainadolescents pages 2-4, charton2024modellingtheeffects pages 13-17)

### 5.3 Suggested GO biological process terms
- Hedgehog signaling pathway — **GO:0007224**
- Regulation of cell proliferation — **GO:0042127**
- DNA damage response (relevant to TP53-mutant biology) — **GO:0006974**

### 5.4 Suggested Cell Ontology (CL) terms
- Cerebellar granule cell precursor — (candidate CL term; exact CL ID should be confirmed in CL/UBERON crosswalk)

---

## 6. Inheritance and Population
### 6.1 Inheritance patterns (predisposition)
Inheritance applies primarily to **tumor predisposition syndromes**:
- **Autosomal dominant** predisposition syndromes such as Gorlin (PTCH1/SUFU) and Li–Fraumeni (TP53). (koch2025thecurrentlandscape pages 2-4)

### 6.2 Epidemiology and subgroup proportions
- SHH-activated medulloblastoma accounts for ~**25–30%** of medulloblastomas overall in multiple summaries. (koch2025thecurrentlandscape pages 2-4, slika2023theneurodevelopmentaland pages 1-2)
- In an adult SHH cohort study context statement, SHH signature is more frequent in adult medulloblastoma (~70%) than pediatric (~30%). (korshunov2021integratedmolecularanalysis pages 1-2)

**Note:** Population-based incidence rates specific to SHH-activated medulloblastoma (e.g., CBTRUS molecular subtype incidence) were not extractable from the retrieved CBTRUS text segments during this run.

---

## 7. Diagnostics
### 7.1 Integrated diagnosis approach
Modern diagnostic practice is layered/integrated: histopathology plus molecular subgroup assignment, increasingly via genome-wide methylation profiling. A molecular pathology review states WHO CNS5 recognizes four major medulloblastoma molecular subgroups by DNA methylation profiling and notes defining the molecular subgroup by methylation profiling as standard-of-care framing in contemporary practice. (koch2025thecurrentlandscape pages 2-4)

### 7.2 DNA methylation profiling (practical implementation)
A major early-childhood cohort used Illumina 450K/EPIC methylation arrays and referenced a Heidelberg Brain Tumor Classifier version (v12.5) in subclass assignment and risk modeling; this illustrates real-world feasibility of methylation-driven SHH subclassification in cooperative cohorts. (tonn2023riskpredictionin pages 3-5)

### 7.3 Sequencing
Targeted sequencing and/or exome sequencing is used to identify actionable/pathway-defining variants (PTCH1/SMO/SUFU; TP53; amplifications) and to interpret resistance (e.g., acquired SMO mutations after SMO inhibitor exposure). (pereira2021clinicalandmolecular pages 2-3)

### 7.4 Differential diagnosis
Differential diagnosis in posterior fossa pediatric tumors includes other medulloblastoma molecular groups (WNT, Group 3, Group 4) and other embryonal tumors; subgrouping by methylation profiling is a central discriminator in current practice. (koch2025thecurrentlandscape pages 2-4)

---

## 8. Outcome / Prognosis
### 8.1 Prognostic stratifiers
- **TP53 mutation status** in SHH medulloblastoma is repeatedly highlighted as a major adverse prognostic factor, with approximate 5-year survival differences on the order of ~80% (TP53-wildtype) vs ~40% (TP53-mutant) in one molecular pathology review summary. (koch2025thecurrentlandscape pages 2-4)

### 8.2 Early-childhood SHH prognosis under radiation-avoiding therapy (key statistics)
A large cohort of **144** children <5 years with SHH desmoplastic/nodular MB or MBEN treated with radiation-sparing chemotherapy reported (overall cohort):
- **5-year PFS 78%** and **5-year OS 93%** (tonn2023riskpredictionin pages 3-5)
- Histology/age effects: **MBEN 5-year PFS 93%** vs **DMB 71%**; age >3 years associated with **5-year PFS 47%** vs 84–85% for younger age bands. (tonn2023riskpredictionin pages 1-2)

Subgroup-level risk differences were identified with methylation subclassing:
- **5-year PFS** in the primary cohort: **SHH-2a 95%**, **SHH-1 83%**, **SHH-2b 58%**. (tonn2023riskpredictionin pages 1-2)

A key figure (hierarchical clustering and Kaplan–Meier) additionally summarizes combined-cohort differences (5-year PFS **SHH-2a 87%**, **SHH-1 68%**, **SHH-2b 48%**). (tonn2023riskpredictionin media 3b1240bb)

### 8.3 Adult SHH molecular subsets and prognosis
In a study of 96 adult SHH medulloblastomas, two epigenetic subsets were defined with markedly different outcomes:
- Favorable subset aSHH-MBI: **5-year PFS 80%**, **OS 92%**
- Unfavorable subset aSHH-MBII: **5-year PFS 24%**, **OS 45%**

Direct abstract quote: “We defined two aSHH-MB numerically comparable epigenetic subsets…” with the unfavorable subset showing “5-year PFS = 24% and OS = 45%”. (korshunov2021integratedmolecularanalysis pages 1-2)

---

## 9. Treatment
### 9.1 Current standard backbone (real-world implementation)
Multimodal therapy is generally based on maximal safe resection plus risk-adapted radiotherapy and multiagent chemotherapy; however, in **infants/very young children**, craniospinal irradiation is often delayed/avoided, and SHH infant tumors may be cured with chemotherapy-only approaches in selected contexts. (tonn2023riskpredictionin pages 1-2, kim2025advancingmedulloblastomatherapy pages 10-12)

### 9.2 Targeted therapy: SMO inhibitors (vismodegib, sonidegib)
#### Clinical activity and predictive biomarkers
A retrospective series of young patients treated with SMO inhibitors for recurrent SHH medulloblastoma reported:
- “All patients with a somatic PTCH1 mutation responded to SMOi (6/8), including 2 prolonged complete responses.” (pereira2021clinicalandmolecular pages 1-2)
- “One patient was free of disease 8.2 years after treatment.” (pereira2021clinicalandmolecular pages 1-2)
- Overall **6/8 (75%) objective responses** (4 PR, 2 CR) in detailed excerpted reporting. (pereira2021clinicalandmolecular pages 2-3)

#### Toxicities (key safety considerations)
Severe or clinically limiting toxicities included “myalgia and growth plate fusion with metaphyseal sclerosis” in the SMO inhibitor series; the authors highlight developmental toxicity as a key limitation for pediatric use. (pereira2021clinicalandmolecular pages 1-2)

#### Resistance mechanisms
Resistance can emerge via acquired SMO mutations:
- Clinical relapse biopsies after SMO inhibitor treatment showed “SMO resistance mutations”. (pereira2021clinicalandmolecular pages 1-2)
- This is supported by preclinical modeling where sonidegib-resistant PDX lines frequently developed SMO missense mutations (mechanistic corroboration). (pereira2021clinicalandmolecular pages 1-2)

### 9.3 Selected ClinicalTrials.gov implementations (NCTs)
Clinical trial registry records show how SHH activation is operationalized and which endpoints are used.

**Vismodegib in recurrent/refractory medulloblastoma (adults)**
- **NCT00939484** (Phase II, completed; N=31). Stratified by PTCH/SHH pathway activation; primary endpoint objective response sustained ≥8 weeks. (NCT00939484 chunk 1)
- URL: https://clinicaltrials.gov/study/NCT00939484 (start: 2009-06; completion: 2015-08 per record excerpt). (NCT00939484 chunk 1)

**Vismodegib + temozolomide vs temozolomide alone (adults, SHH activation required)**
- **NCT01601184** (Phase I/II, randomized, open-label; terminated early). Required “activation of the Sonic Hedgehog Pathway” by IHC; Phase II primary endpoint: “6-month progression-free rate.” (NCT01601184 chunk 1)
- URL: https://clinicaltrials.gov/study/NCT01601184 (first posted 2012). (NCT01601184 chunk 1)

**Sonidegib (LDE225) in pediatric/adult recurrent tumors with Hh dependence**
- **NCT01125800** (Phase I/II, single-group; N=76). Pediatric dose escalation; ORR assessed by Hh signaling status (Hh-positive vs Hh-negative). (NCT01125800 chunk 1)
- URL: https://clinicaltrials.gov/study/NCT01125800 (first posted 2011). (NCT01125800 chunk 1)

**Sonidegib in Hh-pathway activated relapsed medulloblastoma**
- **NCT01708174** (Phase II; completed; N=22). Eligibility required “Hh-pathway activation by the 5-gene Hh signature assay”; primary endpoint ORR by independent review. (NCT01708174 chunk 1)
- URL: https://clinicaltrials.gov/study/NCT01708174 (start date 2013-05-06 per record excerpt). (NCT01708174 chunk 1)

### 9.4 MAXO (Medical Action Ontology) term suggestions
- Surgical tumor resection — MAXO (surgical excision; confirm exact MAXO ID)
- Craniospinal irradiation — MAXO (radiotherapy)
- Combination chemotherapy — MAXO (chemotherapy)
- Smoothened inhibitor therapy (vismodegib/sonidegib) — MAXO (targeted small-molecule therapy)
- High-dose chemotherapy with autologous stem cell rescue — MAXO (hematopoietic stem cell transplantation adjunct)

---

## 10. Prevention
### 10.1 Primary prevention
No validated primary prevention measures were identified.

### 10.2 Secondary/tertiary prevention: predisposition recognition and therapy modification
Given non-trivial germline predisposition in SHH tumors, an actionable prevention-like strategy is early identification of tumor predisposition syndromes and therapy adaptation. For example, reviews note radiotherapy should be used cautiously in germline predisposition settings (e.g., Gorlin/Li–Fraumeni) due to risk of secondary neoplasms. (koch2025thecurrentlandscape pages 2-4)

---

## 11. Other Species / Natural Disease
No naturally occurring non-human SHH-medulloblastoma evidence was retrieved in this run.

---

## 12. Model Organisms / Experimental Models
Multiple translational approaches underpin SHH biology and drug discovery, including:
- **Patient-derived xenograft (PDX)** models for studying SMO inhibitor resistance (generated sonidegib-resistant lines). (pereira2021clinicalandmolecular pages 1-2)
- Early developmental-lineage modeling to interpret differentiation blockade in SHH medulloblastoma (reviewed at high level in modeling-focused sources). (charton2024modellingtheeffects pages 13-17)

Suggested model annotations (non-exhaustive):
- Mouse SHH pathway models (Ptch1/Sufu/Sm o alterations)
- Orthotopic xenografts (PDX)

---

## Recent developments and “latest research” highlights (prioritizing 2023–2024)
1) **Risk prediction refinement within early-childhood SHH** under radiotherapy-avoiding regimens: SHH-2 subdivides into SHH-2a vs SHH-2b with markedly different relapse risk (5-year PFS differences). (tonn2023riskpredictionin pages 1-2, tonn2023riskpredictionin media 3b1240bb)
2) **Growing clinical operationalization of methylation classes** in cooperative cohorts via Heidelberg classifier versions (e.g., v12.5). (tonn2023riskpredictionin pages 3-5)
3) **Clinical translation of pathway-targeted therapy** remains focused on SMO inhibitors with known pediatric skeletal toxicity and resistance mutations, emphasizing the need for combination strategies and biomarker-driven selection (e.g., PTCH1-mutated responders). (pereira2021clinicalandmolecular pages 1-2, NCT01601184 chunk 1)

---

## Evidence summary table
The following table consolidates the key classification, molecular features, outcomes, and targeted-therapy evidence retrieved in this run.

| Topic | Key facts (with numbers) | Evidence type (review/clinical cohort/trial) | Primary source (short citation with year) | URL | Pub date | Citation ID |
|---|---|---|---|---|---|---|
| Definition / WHO CNS5 types | SHH-activated medulloblastoma is one of 4 principal medulloblastoma molecular groups and WHO CNS5 separates it into **SHH-activated, TP53-wildtype** and **SHH-activated, TP53-mutant** entities; SHH tumors comprise about **25–30%** of medulloblastomas overall (koch2025thecurrentlandscape pages 2-4, slika2023theneurodevelopmentaland pages 1-2) | Review / classification summary | Koch et al., 2025 | https://doi.org/10.3390/jmp6020011 | 2025-06 | (koch2025thecurrentlandscape pages 2-4) |
| Age distribution / localization | SHH tumors show a **bimodal** age distribution, enriched in **infants (<3 years)** and **adults/AYA**, and are often **lateral/cerebellar hemisphere** tumors; in adults SHH accounts for about **~65–70%** of medulloblastoma, versus ~30% in pediatric cohorts (korshunov2021integratedmolecularanalysis pages 1-2, ruggiero2026medulloblastomainadolescents pages 2-4, kim2025advancingmedulloblastomatherapy pages 4-6) | Review + molecular cohort | Korshunov et al., 2021 | https://doi.org/10.1093/neuonc/noab031 | 2021-02 | (korshunov2021integratedmolecularanalysis pages 1-2) |
| Core driver pathway lesions | Canonical SHH-pathway alterations include **PTCH1, SMO, SUFU** mutations and downstream **GLI2/GLI1 amplification**; pediatric high-risk SHH often also shows **MYCN amplification** and **TP53** alteration; adult SHH is enriched for **PTCH1/SMO** mutations (koch2025thecurrentlandscape pages 2-4, kim2025advancingmedulloblastomatherapy pages 4-6) | Review | Kim et al., 2025 | https://doi.org/10.3390/brainsci15080896 | 2025-08 | (kim2025advancingmedulloblastomatherapy pages 4-6) |
| Predisposition syndromes | Major germline predisposition syndromes are **Gorlin syndrome** (**PTCH1** or **SUFU**) and **Li-Fraumeni syndrome** (**TP53**); SHH has the highest rate of tumor-predisposition among medulloblastoma groups, and radiation requires caution in Gorlin/LFS because of secondary neoplasm risk (koch2025thecurrentlandscape pages 2-4, kim2025advancingmedulloblastomatherapy pages 4-6) | Review / hereditary risk summary | Koch et al., 2025 | https://doi.org/10.3390/jmp6020011 | 2025-06 | (koch2025thecurrentlandscape pages 2-4) |
| Methylation subtypes (broad) | SHH can be subclassified by methylation/transcriptomics into **SHH-α, SHH-β, SHH-γ, SHH-δ**. **SHH-α**: older children, enriched for **TP53**, **MYCN**, **GLI2**; poorer prognosis. **SHH-β/γ**: infant-predominant. **SHH-δ**: adult-predominant and enriched for **TERT promoter** mutation (korshunov2021integratedmolecularanalysis pages 2-3, ruggiero2026medulloblastomainadolescents pages 2-4, kim2025advancingmedulloblastomatherapy pages 4-6) | Molecular cohort + review | Korshunov et al., 2021 | https://doi.org/10.1093/neuonc/noab031 | 2021-02 | (korshunov2021integratedmolecularanalysis pages 2-3) |
| Early-childhood methylation classes | In children **<5 years** treated with radiation-sparing chemotherapy, tumors were reclassified into **SHH-1 (n=39), SHH-2 (n=38), SHH-3 (n=1)**; hierarchical clustering further split **SHH-2** into **SHH-2a (n=19)** and **SHH-2b (n=19)** (tonn2023riskpredictionin pages 1-2, tonn2023riskpredictionin pages 2-3) | Clinical cohort | Tonn et al., 2023 | https://doi.org/10.1093/neuonc/noad027 | 2023-01 | (tonn2023riskpredictionin pages 1-2) |
| Early-childhood subgroup biology | **SHH-2a** was enriched for **MBEN histology** and correlated with **SMO mutations**; **SHH-2b** occurred in older DMB patients, more often lateral tumors, and showed more **9q loss** with higher relapse risk (tonn2023riskpredictionin pages 1-2, tonn2023riskpredictionin media 3b1240bb) | Clinical cohort + image-supported figure summary | Tonn et al., 2023 | https://doi.org/10.1093/neuonc/noad027 | 2023-01 | (tonn2023riskpredictionin pages 1-2) |
| Early-childhood chemo-only outcomes | In 144 early-childhood SHH DMB/MBEN patients managed with radiation-avoiding therapy, overall **5-year PFS 78%** and **5-year OS 93%**; **MBEN** had **5-year PFS 93%** vs **71%** for DMB; age >3 years had worse **5-year PFS 47%** vs **85% (<1 y)** and **84% (1–3 y)** (tonn2023riskpredictionin pages 1-2, tonn2023riskpredictionin pages 3-5) | Clinical cohort | Tonn et al., 2023 | https://doi.org/10.1093/neuonc/noad027 | 2023-01 | (tonn2023riskpredictionin pages 3-5) |
| Early-childhood subgroup prognosis | In the primary early-childhood cohort, **5-year PFS** was **95% for SHH-2a**, **83% for SHH-1**, and **58% for SHH-2b**; in the combined-cohort figure, corresponding 5-year PFS was **87%**, **68%**, and **48%** respectively (tonn2023riskpredictionin pages 1-2, tonn2023riskpredictionin media 3b1240bb) | Clinical cohort | Tonn et al., 2023 | https://doi.org/10.1093/neuonc/noad027 | 2023-01 | (tonn2023riskpredictionin pages 1-2, tonn2023riskpredictionin media 3b1240bb) |
| TP53 effect on prognosis | TP53 status is a major prognostic discriminator: approximately **5-year survival ~80%** for **TP53-wildtype** SHH versus about **~40%** for **TP53-mutant** SHH; in AYA-focused summaries, **5-year OS ~70–80%** for TP53-wildtype vs **~40–50%** for TP53-mutant (koch2025thecurrentlandscape pages 2-4, ruggiero2026medulloblastomainadolescents pages 2-4) | Review | Koch et al., 2025 | https://doi.org/10.3390/jmp6020011 | 2025-06 | (koch2025thecurrentlandscape pages 2-4) |
| Adult SHH molecular subsets | In 96 adult SHH tumors, two clinically relevant epigenetic subsets were identified: **aSHH-MBI** with **PTCH1/SMO mutations** and favorable outcome (**5-year PFS 80%, OS 92%**), versus **aSHH-MBII** with **GLI2 amplification (8%)**, **10q loss (22%)**, angiogenesis/VEGFA program, and poor outcome (**5-year PFS 24%, OS 45%**) (korshunov2021integratedmolecularanalysis pages 1-2) | Molecular clinical cohort | Korshunov et al., 2021 | https://doi.org/10.1093/neuonc/noab031 | 2021-02 | (korshunov2021integratedmolecularanalysis pages 1-2) |
| Diagnostic standard | Modern diagnosis is integrated histology + molecular testing; **genome-wide DNA methylation profiling** is described as standard of care / cornerstone for subgroup assignment, including SHH, and Heidelberg methylation classifier versions (e.g., **v12.5/v12.8**) are used in clinical/research workflows (koch2025thecurrentlandscape pages 2-4, tonn2023riskpredictionin pages 3-5) | Review + clinical cohort methods | Koch et al., 2025 | https://doi.org/10.3390/jmp6020011 | 2025-06 | (koch2025thecurrentlandscape pages 2-4) |
| SMO inhibitor activity | In a recurrent SHH series of **8** patients treated with **vismodegib** or **sonidegib**, there were **6/8 (75%) objective responses** (**4 PR, 2 CR**); all evaluable tumors with **somatic PTCH1 mutation responded** and one patient remained disease-free **8.2 years** after treatment (pereira2021clinicalandmolecular pages 1-2, pereira2021clinicalandmolecular pages 2-3) | Clinical series | Pereira et al., 2021 | https://doi.org/10.1093/noajnl/vdab097 | 2021-07 | (pereira2021clinicalandmolecular pages 1-2, pereira2021clinicalandmolecular pages 2-3) |
| SMO inhibitor treatment details | In the same series, **vismodegib** was used in **3** patients and **sonidegib** in **5**; median age at start was **11.1 years** (range **3.3–25.5**) and median treatment duration was **7 months** (range **1.2–9.4 months**) (pereira2021clinicalandmolecular pages 2-3) | Clinical series | Pereira et al., 2021 | https://doi.org/10.1093/noajnl/vdab097 | 2021-07 | (pereira2021clinicalandmolecular pages 2-3) |
| SMO inhibitor toxicities | Key toxicities include **myalgia** and especially **growth plate fusion / metaphyseal sclerosis**; this skeletal toxicity is a major limitation in children and has led to preference for use in skeletally mature patients or carefully selected salvage settings (pereira2021clinicalandmolecular pages 1-2, kim2025advancingmedulloblastomatherapy pages 12-14) | Clinical series + review | Pereira et al., 2021 | https://doi.org/10.1093/noajnl/vdab097 | 2021-07 | (pereira2021clinicalandmolecular pages 1-2) |
| SMO inhibitor resistance | Resistance commonly arises through acquired **SMO missense mutations**; in a resistant PDX model, **8/9** sonidegib-resistant lines developed **SMO missense mutations** and **1/9** acquired an inactivating **MEGF8** mutation downstream of SMO. Relapse biopsies from treated patients also showed **SMO resistance mutations** (pereira2021clinicalandmolecular pages 1-2, pereira2021clinicalandmolecular pages 2-3) | Preclinical model + clinical series | Krausert et al., 2022 | https://doi.org/10.1093/noajnl/vdac026 | 2022-03 | (pereira2021clinicalandmolecular pages 1-2, pereira2021clinicalandmolecular pages 2-3) |
| Practical therapeutic implication | SHH inhibitors are most compelling in **PTCH1-mutated** recurrent SHH medulloblastoma; combination strategies with **temozolomide** or **local therapy (surgery/radiotherapy)** were associated with prolonged disease control in selected patients (pereira2021clinicalandmolecular pages 1-2) | Clinical series | Pereira et al., 2021 | https://doi.org/10.1093/noajnl/vdab097 | 2021-07 | (pereira2021clinicalandmolecular pages 1-2) |


*Table: This table condenses the highest-yield classification, molecular, prognostic, and treatment evidence for SHH-activated medulloblastoma. It is designed to support a structured disease report with recent reviews plus key primary cohort and therapy data.*

---

## Notes on gaps / limitations of this run
- **Ontology identifiers (MONDO/OMIM/Orphanet/ICD/MeSH)** and **population incidence rates from registry reports** were not reliably extractable from the retrieved texts using the current tool outputs; filling these fields will require targeted retrieval from dedicated ontology resources or explicit registry sections not captured here.
- Several core statements are supported by **reviews** rather than **primary genomic discovery papers** due to corpus constraints; nevertheless, key numerical outcomes and trial design details were sourced from primary cohorts and ClinicalTrials.gov where possible. (tonn2023riskpredictionin pages 1-2, NCT00939484 chunk 1, NCT01708174 chunk 1)


References

1. (koch2025thecurrentlandscape pages 2-4): Alayna Koch, Ashley Childress, Emma Vallee, Alyssa Steller, and Scott Raskin. The current landscape of molecular pathology for the diagnosis and treatment of pediatric medulloblastoma. Journal of Molecular Pathology, 6:11, Jun 2025. URL: https://doi.org/10.3390/jmp6020011, doi:10.3390/jmp6020011. This article has 3 citations.

2. (NCT01708174 chunk 1):  A Phase II Study of Oral LDE225 in Patients With Hedge-Hog (Hh)-Pathway Activated Relapsed Medulloblastoma (MB). Novartis Pharmaceuticals. 2013. ClinicalTrials.gov Identifier: NCT01708174

3. (NCT00939484 chunk 1):  Vismodegib in Treating Patients With Recurrent or Refractory Medulloblastoma. National Cancer Institute (NCI). 2009. ClinicalTrials.gov Identifier: NCT00939484

4. (kim2025advancingmedulloblastomatherapy pages 4-6): David T. Kim, Michaela Uloho-Okundaye, Stephen C. Frederico, Santosh Guru, Min J. Kim, and Steven D. Chang. Advancing medulloblastoma therapy in pediatrics: integrative molecular classification and emerging treatments. Brain Sciences, 15:896, Aug 2025. URL: https://doi.org/10.3390/brainsci15080896, doi:10.3390/brainsci15080896. This article has 6 citations.

5. (ruggiero2026medulloblastomainadolescents pages 2-4): Antonio Ruggiero, Marco Gessi, Antonio d’Amati, Alessio Albanese, and Giorgio Attinà. Medulloblastoma in adolescents and young adults: molecular subgroups, prognostic biomarkers, and age-specific therapeutic challenges. Current Issues in Molecular Biology, 48:297, Mar 2026. URL: https://doi.org/10.3390/cimb48030297, doi:10.3390/cimb48030297. This article has 0 citations.

6. (korshunov2021integratedmolecularanalysis pages 1-2): Andrey Korshunov, Konstantin Okonechnikov, Damian Stichel, Marina Ryzhova, Daniel Schrimpf, Felix Sahm, Philipp Sievers, Oksana Absalyamova, Olga Zheludkova, Andrey Golanov, David T W Jones, Stefan M Pfister, Andreas von Deimling, and Marcel Kool. Integrated molecular analysis of adult sonic hedgehog (shh)-activated medulloblastomas reveals two clinically relevant tumor subsets with vegfa as potent prognostic indicator. Neuro-Oncology, 23:1576-1585, Feb 2021. URL: https://doi.org/10.1093/neuonc/noab031, doi:10.1093/neuonc/noab031. This article has 13 citations and is from a domain leading peer-reviewed journal.

7. (slika2023theneurodevelopmentaland pages 1-2): Hasan Slika, Paolo Alimonti, Divyaansh Raj, Chad Caraway, Safwan Alomari, Eric M. Jackson, and Betty Tyler. The neurodevelopmental and molecular landscape of medulloblastoma subgroups: current targets and the potential for combined therapies. Cancers, 15:3889, Jul 2023. URL: https://doi.org/10.3390/cancers15153889, doi:10.3390/cancers15153889. This article has 25 citations.

8. (korshunov2021integratedmolecularanalysis pages 2-3): Andrey Korshunov, Konstantin Okonechnikov, Damian Stichel, Marina Ryzhova, Daniel Schrimpf, Felix Sahm, Philipp Sievers, Oksana Absalyamova, Olga Zheludkova, Andrey Golanov, David T W Jones, Stefan M Pfister, Andreas von Deimling, and Marcel Kool. Integrated molecular analysis of adult sonic hedgehog (shh)-activated medulloblastomas reveals two clinically relevant tumor subsets with vegfa as potent prognostic indicator. Neuro-Oncology, 23:1576-1585, Feb 2021. URL: https://doi.org/10.1093/neuonc/noab031, doi:10.1093/neuonc/noab031. This article has 13 citations and is from a domain leading peer-reviewed journal.

9. (tonn2023riskpredictionin pages 1-2): Svenja Tonn, Andrey Korshunov, Denise Obrecht, Martin Sill, Michael Spohn, Katja von Hoff, Till Milde, Torsten Pietsch, Tobias Goschzik, Brigitte Bison, Björn-Ole Juhnke, Nina Struve, Dominik Sturm, Felix Sahm, Michael Bockmayr, Carsten Friedrich, André O von Bueren, Nicolas U Gerber, Martin Benesch, David T W Jones, Marcel Kool, Annika K Wefers, Ulrich Schüller, Stefan M Pfister, Stefan Rutkowski, and Martin Mynarek. Risk prediction in early childhood shh medulloblastoma treated with radiation-avoiding chemotherapy: evidence for more than two subgroups. Neuro-oncology, 25:1518-1529, Jan 2023. URL: https://doi.org/10.1093/neuonc/noad027, doi:10.1093/neuonc/noad027. This article has 8 citations and is from a domain leading peer-reviewed journal.

10. (tonn2023riskpredictionin pages 3-5): Svenja Tonn, Andrey Korshunov, Denise Obrecht, Martin Sill, Michael Spohn, Katja von Hoff, Till Milde, Torsten Pietsch, Tobias Goschzik, Brigitte Bison, Björn-Ole Juhnke, Nina Struve, Dominik Sturm, Felix Sahm, Michael Bockmayr, Carsten Friedrich, André O von Bueren, Nicolas U Gerber, Martin Benesch, David T W Jones, Marcel Kool, Annika K Wefers, Ulrich Schüller, Stefan M Pfister, Stefan Rutkowski, and Martin Mynarek. Risk prediction in early childhood shh medulloblastoma treated with radiation-avoiding chemotherapy: evidence for more than two subgroups. Neuro-oncology, 25:1518-1529, Jan 2023. URL: https://doi.org/10.1093/neuonc/noad027, doi:10.1093/neuonc/noad027. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (charton2024modellingtheeffects pages 13-17): C Charton. Modelling the effects of pediatric sonic hedgehog medulloblastoma driver mutations on granule lineage development. Unknown journal, 2024.

12. (pereira2021clinicalandmolecular pages 2-3): Victor Pereira, Jacob Torrejon, Dulanjalee Kariyawasam, Pablo Berlanga, Léa Guerrini-Rousseau, Olivier Ayrault, Pascale Varlet, Arnault Tauziède-Espariat, Stéphanie Puget, Stéphanie Bolle, Kevin Beccaria, Thomas Blauwblomme, Laurence Brugières, Jacques Grill, Birgit Geoerger, Christelle Dufour, and Samuel Abbou. Clinical and molecular analysis of smoothened inhibitors in sonic hedgehog medulloblastoma. Neuro-oncology Advances, Jul 2021. URL: https://doi.org/10.1093/noajnl/vdab097, doi:10.1093/noajnl/vdab097. This article has 26 citations and is from a peer-reviewed journal.

13. (tonn2023riskpredictionin media 3b1240bb): Svenja Tonn, Andrey Korshunov, Denise Obrecht, Martin Sill, Michael Spohn, Katja von Hoff, Till Milde, Torsten Pietsch, Tobias Goschzik, Brigitte Bison, Björn-Ole Juhnke, Nina Struve, Dominik Sturm, Felix Sahm, Michael Bockmayr, Carsten Friedrich, André O von Bueren, Nicolas U Gerber, Martin Benesch, David T W Jones, Marcel Kool, Annika K Wefers, Ulrich Schüller, Stefan M Pfister, Stefan Rutkowski, and Martin Mynarek. Risk prediction in early childhood shh medulloblastoma treated with radiation-avoiding chemotherapy: evidence for more than two subgroups. Neuro-oncology, 25:1518-1529, Jan 2023. URL: https://doi.org/10.1093/neuonc/noad027, doi:10.1093/neuonc/noad027. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (kim2025advancingmedulloblastomatherapy pages 10-12): David T. Kim, Michaela Uloho-Okundaye, Stephen C. Frederico, Santosh Guru, Min J. Kim, and Steven D. Chang. Advancing medulloblastoma therapy in pediatrics: integrative molecular classification and emerging treatments. Brain Sciences, 15:896, Aug 2025. URL: https://doi.org/10.3390/brainsci15080896, doi:10.3390/brainsci15080896. This article has 6 citations.

15. (pereira2021clinicalandmolecular pages 1-2): Victor Pereira, Jacob Torrejon, Dulanjalee Kariyawasam, Pablo Berlanga, Léa Guerrini-Rousseau, Olivier Ayrault, Pascale Varlet, Arnault Tauziède-Espariat, Stéphanie Puget, Stéphanie Bolle, Kevin Beccaria, Thomas Blauwblomme, Laurence Brugières, Jacques Grill, Birgit Geoerger, Christelle Dufour, and Samuel Abbou. Clinical and molecular analysis of smoothened inhibitors in sonic hedgehog medulloblastoma. Neuro-oncology Advances, Jul 2021. URL: https://doi.org/10.1093/noajnl/vdab097, doi:10.1093/noajnl/vdab097. This article has 26 citations and is from a peer-reviewed journal.

16. (NCT01601184 chunk 1):  Study of Vismodegib in Combination With Temozolomide Versus Temozolomide Alone in Patients With Medulloblastomas With an Activation of the Sonic Hedgehog Pathway. Centre Leon Berard. 2012. ClinicalTrials.gov Identifier: NCT01601184

17. (NCT01125800 chunk 1):  A Phase I Dose Finding and Safety Study of Oral LDE225 in Children and a Phase II Portion to Assess Preliminary Efficacy in Recurrent or Refractory MB. Novartis Pharmaceuticals. 2011. ClinicalTrials.gov Identifier: NCT01125800

18. (tonn2023riskpredictionin pages 2-3): Svenja Tonn, Andrey Korshunov, Denise Obrecht, Martin Sill, Michael Spohn, Katja von Hoff, Till Milde, Torsten Pietsch, Tobias Goschzik, Brigitte Bison, Björn-Ole Juhnke, Nina Struve, Dominik Sturm, Felix Sahm, Michael Bockmayr, Carsten Friedrich, André O von Bueren, Nicolas U Gerber, Martin Benesch, David T W Jones, Marcel Kool, Annika K Wefers, Ulrich Schüller, Stefan M Pfister, Stefan Rutkowski, and Martin Mynarek. Risk prediction in early childhood shh medulloblastoma treated with radiation-avoiding chemotherapy: evidence for more than two subgroups. Neuro-oncology, 25:1518-1529, Jan 2023. URL: https://doi.org/10.1093/neuonc/noad027, doi:10.1093/neuonc/noad027. This article has 8 citations and is from a domain leading peer-reviewed journal.

19. (kim2025advancingmedulloblastomatherapy pages 12-14): David T. Kim, Michaela Uloho-Okundaye, Stephen C. Frederico, Santosh Guru, Min J. Kim, and Steven D. Chang. Advancing medulloblastoma therapy in pediatrics: integrative molecular classification and emerging treatments. Brain Sciences, 15:896, Aug 2025. URL: https://doi.org/10.3390/brainsci15080896, doi:10.3390/brainsci15080896. This article has 6 citations.

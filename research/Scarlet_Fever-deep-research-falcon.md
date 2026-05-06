---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T18:23:22.161358'
end_time: '2026-05-06T18:40:49.252614'
duration_seconds: 1047.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Scarlet Fever
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 45
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Scarlet Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Scarlet Fever** covering all of the
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
- **Disease Name:** Scarlet Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Scarlet Fever** covering all of the
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


# Scarlet Fever (Infectious disease) — Comprehensive Disease Characteristics Report

## Target Disease
- **Disease name:** Scarlet fever
- **Category:** Infectious (bacterial toxin–mediated exanthematous illness secondary to *Streptococcus pyogenes* [Group A Streptococcus, GAS])
- **MONDO ID:** Not retrieved from the available sources in this run (evidence gap; should be filled from MONDO/OLS).

---

## Executive summary (current understanding)
Scarlet fever is a GAS disease classically characterized by fever, pharyngitis/tonsillopharyngitis, a sandpaper-like erythematous exanthem, and mucosal findings such as “strawberry tongue.” (bergsten2024theintricatepathogenicity pages 2-3, leung2025groupaβhemolytic pages 1-2) The modern resurgence of GAS illnesses after COVID-19 nonpharmaceutical interventions has been linked to changes in circulating GAS lineages and toxin profiles, including expansion of the toxigenic **emm1 M1UK** lineage with increased **SpeA** superantigen expression. (rumke2024nationwideupsurgein pages 1-2, rumke2024nationwideupsurgein pages 2-4, bergsten2024theintricatepathogenicity pages 3-4)

---

## 1. Disease Information
### 1.1 Concise overview
Scarlet fever is a clinical syndrome caused by GAS strains producing streptococcal pyrogenic exotoxins/superantigens, presenting with fever and pharyngitis and a diffuse erythematous rash with rough “sandpaper” texture, often accompanied by strawberry tongue and later desquamation. (bergsten2024theintricatepathogenicity pages 2-3, inamadar2018thestrawberrytongue pages 1-2, wu2024epidemiologicalchangesof pages 1-2)

### 1.2 Key identifiers (ontology/terminology)
- **ICD-10:** A38 (standard coding; not explicitly quoted in the retrieved texts—needs confirmation from ICD-10 dataset).
- **ICD-11 / MeSH / SNOMED CT / MONDO:** Not retrieved in the accessible full texts here; recommended to populate directly from authoritative terminologies.

### 1.3 Common synonyms / alternative names
- “Scarlatina” (common synonym; not explicitly shown in the retrieved evidence set)
- “Streptococcal scarlet fever” (clinical synonym)

### 1.4 Evidence provenance
Evidence used here is largely from **aggregated disease-level resources** (surveillance studies and reviews) plus **case reports/series** for phenotype details (e.g., oral findings and timing of desquamation). (wu2024epidemiologicalchangesof pages 1-2, slebioda2020scarletfever– pages 3-5, inamadar2018thestrawberrytongue pages 1-2)

---

## 2. Etiology
### 2.1 Disease causal factors
- **Infectious cause:** *Streptococcus pyogenes* (GAS) infection (most often pharyngotonsillitis) with toxin production. (wu2024epidemiologicalchangesof pages 1-2, bergsten2024theintricatepathogenicity pages 2-3)
- **Mechanistic cause (toxin-mediated):** Scarlet fever is associated with GAS expression of **pyrogenic exotoxins / superantigens**, including **SpeA** and prophage-encoded factors such as **SSA**, with epidemiologic relevance of **emm1/emm12** lineages. (bergsten2024theintricatepathogenicity pages 3-4, bergsten2024theintricatepathogenicity pages 8-10)

### 2.2 Risk factors (host/environment)
- **Age:** Predominantly children (e.g., under 10 in Chongqing surveillance; 3–7 years highest burden). (wu2024epidemiologicalchangesof pages 1-2)
- **Crowding/contact networks:** Transmission facilitated in kindergartens/schools and households; household transmission ~35% for GAS pharyngitis. (leung2025groupaβhemolytic pages 1-2)
- **Seasonality:** Peaks reported in winter/early spring for GAS pharyngitis and bimodal seasonal peaks for scarlet fever in Chongqing (Apr–Jun; Nov–Dec). (wu2024epidemiologicalchangesof pages 1-2, leung2025groupaβhemolytic pages 1-2)

### 2.3 Protective factors
Not well characterized in the retrieved sources. Conceptually, immunity accumulates with age; a comprehensive GAS review notes immunity development over time and long-lived antibodies, but protective factors specific to scarlet fever (e.g., correlates of protection) are not quantified here. (bergsten2024theintricatepathogenicity pages 8-10)

### 2.4 Gene–environment / host–pathogen interaction
A GAS pathogenicity review highlights **HLA–superantigen (SpeA) interactions**, noting associations of HLA-DQA1/HLA-DQ with increased infection risk and nasal colonization. (bergsten2024theintricatepathogenicity pages 3-4)

---

## 3. Phenotypes
### 3.1 Core clinical phenotype set (with characteristics)
**Typical timing**
- **Incubation:** 2–5 days for GAS pharyngitis. (leung2025groupaβhemolytic pages 1-2)
- **Rash timing:** Often follows pharyngeal symptoms within ~1–2 days (case-based/clinical descriptions). (m.2026araremanifestation pages 1-2)
- **Desquamation:** May occur during convalescence, including palm/sole peeling within ~2 weeks in classic descriptions and case reports. (m.2026araremanifestation pages 1-2, slebioda2020scarletfever– pages 3-5)

**Common manifestations**
- Fever, headache, sore throat, lymphadenopathy, sandpaper-like erythematous rash, and post-rash peeling/desquamation are listed as characteristic clinical features in a large surveillance study. (wu2024epidemiologicalchangesof pages 1-2)
- “Strawberry tongue”: a “white strawberry tongue” early with loss of coating in 1–2 days, exposing hypertrophic papillae (red strawberry tongue). (leung2025groupaβhemolytic pages 1-2, inamadar2018thestrawberrytongue pages 1-2)
- **Pastia lines** and **circumoral pallor (Filatov mask)** are included in clinical descriptions of scarlet fever exanthem variants. (m.2026araremanifestation pages 2-4)

**Quality of life / functional impact**
A contemporary review of GAS pharyngitis reports short-term functional burden: children missed a mean 1.9 days of daycare/school and 42% of parents missed a mean 1.8 workdays. (leung2025groupaβhemolytic pages 6-7)

### 3.2 Suggested HPO terms (examples)
(These are ontology suggestions; the IDs should be verified against the HPO database.)
- Fever — **HP:0001945**
- Pharyngitis / sore throat — **HP:0025421** (pharyngitis) / **HP:0033050** (sore throat; verify)
- Exanthem / rash — **HP:0000988**
- Desquamation — **HP:0000977**
- Strawberry tongue — term exists in HPO (verify exact ID)
- Cervical lymphadenopathy — **HP:0000450**

---

## 4. Genetic / Molecular Information
### 4.1 Causal genes (human)
Not applicable in the Mendelian sense: scarlet fever is not a monogenic inherited disorder.

### 4.2 Host genetic susceptibility (non-Mendelian)
Evidence indicates host HLA class II variation can modulate susceptibility via SpeA interactions (HLA-DQA1/HLA-DQ). (bergsten2024theintricatepathogenicity pages 3-4)

### 4.3 Pathogen molecular determinants (primary molecular “genetics” for this disease)
- **emm types / lineages:** Surveillance and molecular studies emphasize the role of emm type distributions and emergence of toxigenic sublineages.
  - Netherlands iGAS surge coincided with expansion of emm1.0 and dominance of M1UK. (rumke2024nationwideupsurgein pages 1-2)
  - Shanghai scarlet fever surveillance shows dominance of **emm12** and **emm1**, with detection of **M1UK** isolates and shifting sequence types post-COVID. (cai2025ongoingepidemicof pages 1-2)
- **Toxins / superantigens:** Scarlet fever is linked to GAS superantigens (SpeA, SpeC, SSA) and differential expression levels.
  - M1UK is defined by 27 SNPs and associated with increased SpeA expression in vitro; review-level evidence indicates ~10-fold higher SpeA expression in M1UK compared to prior lineages. (rumke2024nationwideupsurgein pages 2-4, bergsten2024theintricatepathogenicity pages 3-4)
  - In pediatric Bulgarian cases (2023), superantigen profiles included SpeA+SpeJ (45%) and others (SpeC; SpeI+SpeH 27.5% each). (keuleyan2025characterizationofstreptococcus pages 1-2)

### 4.4 Epigenetics / chromosomal abnormalities
Not applicable for the human host in typical clinical usage; pathogen regulatory and mobile-element effects exist (prophage-encoded toxins) but were not comprehensively extracted here beyond toxin carriage/expression. (rumke2024nationwideupsurgein pages 2-4, bergsten2024theintricatepathogenicity pages 3-4)

---

## 5. Environmental Information
- **Primary “environmental” drivers** in this evidence set are **contact structure** (schools/households), **crowding**, and **seasonality**, rather than chemical/toxic exposures. (wu2024epidemiologicalchangesof pages 1-2, leung2025groupaβhemolytic pages 1-2)
- **Transmission routes:** Droplet/close contact and fomites are described in surveillance descriptions. (wu2024epidemiologicalchangesof pages 1-2)

---

## 6. Mechanism / Pathophysiology
### 6.1 Causal chain (upstream → downstream)
1) **Colonization/infection** of upper respiratory tract by GAS, with potential asymptomatic carriage in children (~8% school-age carriage cited in a review). (bergsten2024theintricatepathogenicity pages 2-3)
2) **Expression and/or increased expression** of **superantigens/toxins** (SpeA, SSA, SpeC), influenced by lineage (e.g., M1UK) and prophage acquisition. (rumke2024nationwideupsurgein pages 2-4, bergsten2024theintricatepathogenicity pages 3-4)
3) **Immune activation**: superantigen-mediated T-cell hyperactivation through TCR–HLA interactions; clinical immune signatures in acute illness include elevated inflammatory cytokines (IFN-γ, IL-6) alongside regulatory IL-10, with reduced IL-17A reported in one pediatric cohort. (bergsten2024theintricatepathogenicity pages 3-4, keuleyan2025characterizationofstreptococcus pages 1-2)
4) **Clinical phenotype**: systemic symptoms (fever) and mucocutaneous inflammation resulting in rash and strawberry tongue; later epidermal desquamation/peeling. (wu2024epidemiologicalchangesof pages 1-2, inamadar2018thestrawberrytongue pages 1-2)
5) **Downstream immune sequelae risk**: GAS infection can be followed by acute rheumatic fever (ARF) and post-streptococcal glomerulonephritis (PSGN) in susceptible settings/populations. (bergsten2024theintricatepathogenicity pages 2-3)

### 6.2 Suggested GO biological process terms (examples)
(Verify exact GO IDs against GO.)
- T cell activation
- Cytokine-mediated signaling pathway
- Inflammatory response
- Response to bacterium

### 6.3 Suggested Cell Ontology (CL) terms (examples)
- CD4-positive T cell
- Neutrophil
- Dendritic cell / antigen-presenting cell

---

## 7. Anatomical Structures Affected
### 7.1 Organ/system level
- **Primary:** Oropharynx/tonsils (pharyngotonsillitis), skin (exanthem), tongue/oral mucosa (strawberry tongue). (leung2025groupaβhemolytic pages 1-2, inamadar2018thestrawberrytongue pages 1-2)
- **Secondary/complications:** Cardiovascular system (rheumatic heart disease via ARF pathway), kidney (PSGN), and invasive soft-tissue/systemic involvement in severe GAS disease. (bergsten2024theintricatepathogenicity pages 2-3, keuleyan2025characterizationofstreptococcus pages 1-2)

### 7.2 Suggested UBERON terms (examples)
- Oropharynx; palatine tonsil; tongue; skin; kidney glomerulus; heart valve (verify IDs in Uberon).

---

## 8. Temporal Development
- **Onset pattern:** Acute (incubation ~2–5 days; abrupt fever/sore throat described in GAS pharyngitis). (leung2025groupaβhemolytic pages 1-2)
- **Course:** Generally self-limited with appropriate treatment; rash and mucocutaneous findings may persist longer than systemic symptoms, with peeling over ~2 weeks in classic descriptions and cases. (m.2026araremanifestation pages 1-2, slebioda2020scarletfever– pages 3-5)

---

## 9. Inheritance and Population
### 9.1 Epidemiology (recent data prioritized)
**Chongqing, China (19-year surveillance; publication Sep 2024)**
- 2005–2023: 9,593 cases; annual average incidence 1.6694 per 100,000; children 3–7 highest burden; kindergarteners 54.32% of cases; male:female incidence ratio 1.51. (wu2024epidemiologicalchangesof pages 1-2)
- Predicted 2024–2025 burden: 675 and 705 cases, respectively, using SARIMA. (wu2024epidemiologicalchangesof pages 1-2)
- Visual evidence of long-term incidence and 2024–2025 predictions is available in extracted figures. (wu2024epidemiologicalchangesof media b02e46ec, wu2024epidemiologicalchangesof media e239d009)

**UK resurgence snapshot (review citing UK surveillance; publication Jun 2023)**
- Reported “27,486 confirmed scarlet fever cases and 94 deaths from September 2022 to December 2022” (as cited in the review). (matsubara2023recrudescenceofscarlet pages 1-2)

**Global burden estimates (review; publication Nov 2024)**
- Review-level estimates list scarlet fever incidence as 186 per 100,000 children and 33 per 100,000 across all ages. (bergsten2024theintricatepathogenicity pages 2-3)

### 9.2 Demographics
- Pediatric predominance: Under 10 years in surveillance; key risk window 3–7 years in Chongqing. (wu2024epidemiologicalchangesof pages 1-2)

---

## 10. Diagnostics
### 10.1 Clinical diagnosis
Scarlet fever is often diagnosed clinically by the combination of pharyngitis/fever and characteristic rash plus oral findings (strawberry tongue), with confirmatory microbiologic testing where appropriate. (leung2025groupaβhemolytic pages 1-2, matsubara2023recrudescenceofscarlet pages 2-4)

### 10.2 Laboratory confirmation and current implementations
**Rapid antigen detection test (RADT), NAAT, and culture**
- Belgium (Nov 2022–Feb 2023; n=82 swabs): RADT sensitivity 80.76% and specificity 100%; NAAT sensitivity 100% and specificity 96.42% vs culture. (panahandeh2024moleculardiagnosticsfor pages 1-2, panahandeh2024moleculardiagnosticsfor pages 2-4)

**PCR implementation / operational performance**
- New Zealand (from Sep 2023; n=1,093 swabs): culture detected 24.0% vs PCR 29.2%; median turnaround time decreased from 44 to 16 hours after introducing PCR. (lucas2024alaboratorydevelopedextraction pages 1-2)

### 10.3 Differential diagnosis
Differentials discussed in clinical case literature include viral exanthems, measles, rubella, Kawasaki disease, infectious mononucleosis, hand-foot-and-mouth disease, and drug eruptions; strawberry tongue is not specific and appears in other toxin-mediated or inflammatory conditions. (slebioda2020scarletfever– pages 3-5, inamadar2018thestrawberrytongue pages 1-2)

---

## 11. Outcome / Prognosis
- With appropriate treatment, prognosis for scarlet fever itself is generally excellent; however, GAS infections can lead to post-infectious immune sequelae (ARF, PSGN) and severe invasive disease in other clinical contexts. (bergsten2024theintricatepathogenicity pages 2-3, leung2025groupaβhemolytic pages 6-7)
- Severe GAS disease (iGAS) has high mortality; a review notes iGAS burden and fatality considerations, and outbreak dynamics may require public health interventions. (esposito2025recentchangesin pages 1-2)

---

## 12. Treatment
### 12.1 Pharmacotherapy (first-line and alternatives)
Management largely follows GAS pharyngitis treatment principles to eradicate GAS, reduce transmission, and prevent complications.
- **First-line:** Oral **penicillin V** for 10 days; **amoxicillin** commonly used in children (e.g., 50 mg/kg/day, max 1200 mg/day) for 10 days. (leung2025groupaβhemolytic pages 6-7)
- **Contagiousness after therapy:** Patients are “usually not contagious 24 hours after initiating appropriate antimicrobial therapy.” (leung2025groupaβhemolytic pages 1-2)
- **Alternatives (penicillin allergy):** Oral cephalosporins for non-anaphylactic allergy; clindamycin/azithromycin/clarithromycin for immediate-type hypersensitivity, with regimen details provided in the review. (leung2025groupaβhemolytic pages 6-7)

### 12.2 MAXO term suggestions (examples)
(Verify exact MAXO IDs.)
- Antibiotic therapy
- Penicillin administration
- Throat swab diagnostic testing
- Patient isolation / infection control

---

## 13. Prevention
- **Primary prevention:** No vaccine for scarlet fever itself; control relies on prompt diagnosis and treatment, and infection control in schools/households. (wu2024epidemiologicalchangesof pages 1-2, matsubara2023recrudescenceofscarlet pages 2-4)
- **Transmission reduction:** Emphasized measures include isolation during acute illness, hand hygiene, respiratory etiquette, and early antibiotics to reduce spread and complications. (matsubara2023recrudescenceofscarlet pages 2-4, leung2025groupaβhemolytic pages 1-2)

---

## 14. Other Species / Natural Disease
Not addressed in retrieved sources; GAS is described as primarily human-adapted/human-restricted in major reviews, implying limited natural animal disease relevance for scarlet fever per se. (bergsten2024theintricatepathogenicity pages 2-3)

---

## 15. Model Organisms
Not systematically extracted in this run (evidence gap). GAS pathogenesis research commonly uses in vitro and animal models, but model details specific to scarlet fever manifestations were not captured in the retrieved evidence.

---

## Recent developments (2023–2024 prioritized) and expert analysis
- **Post-pandemic resurgence & lineage effects:** Molecular surveillance in the Netherlands shows the 2022–2023 iGAS upsurge coincided with a sharp rise in emm1.0 invasive isolates and dominance of M1UK (72% → 96% among invasive emm1 from Q1 2022 to Q1 2023), supporting expert interpretations that lineage fitness/virulence changes contributed to post-COVID increases. (rumke2024nationwideupsurgein pages 1-2)
- **Mechanistic expert synthesis:** A 2024 GAS virulence review links scarlet fever resurgence to toxin/superantigen biology and emphasizes airborne transmission potential in schools and outbreaks with increased asymptomatic carriage. (bergsten2024theintricatepathogenicity pages 2-3)
- **Diagnostics shift to molecular:** 2024 evaluations show NAAT/PCR can increase detection and shorten turnaround time vs culture/RADT, supporting real-world implementation and antimicrobial stewardship. (panahandeh2024moleculardiagnosticsfor pages 2-4, lucas2024alaboratorydevelopedextraction pages 1-2)

---

## Quantitative findings summary table
| Domain (Epidemiology/Resurgence/Transmission/Diagnostics/Treatment) | Setting/Population | Time period | Key quantitative results (incidence, counts, %) | Interpretation/notes | Source (first author year, journal) | URL | Citation context ID |
|---|---|---|---|---|---|---|---|
| Epidemiology | Chongqing, China; reported scarlet fever cases | 2005–2023 | 9,593 cases; annual average incidence 1.6694 per 100,000 | Long-term surveillance shows persistent pediatric burden | Wu 2024, *BMC Public Health* | https://doi.org/10.1186/s12889-024-20116-5 | (wu2024epidemiologicalchangesof pages 1-2) |
| Epidemiology | Chongqing, China; children 3–7 years | 2005–2023 | Highest average incidence at age 6: 5.0002 per 100,000; kindergarten children 54.32% of cases; students 34.09%; male incidence 1.51× female | Young school/daycare-aged boys were the highest-risk group | Wu 2024, *BMC Public Health* | https://doi.org/10.1186/s12889-024-20116-5 | (wu2024epidemiologicalchangesof pages 1-2) |
| Epidemiology | Chongqing, China | 2005–2023 | Bimodal seasonal peaks: Apr–Jun and Nov–Dec; incidence increased by 106.54% in 2015–2019 and 39.33% in 2020–2022 vs 2005–2014 | Supports seasonality and post-2011/2015 resurgence pattern | Wu 2024, *BMC Public Health* | https://doi.org/10.1186/s12889-024-20116-5 | (wu2024epidemiologicalchangesof pages 1-2) |
| Epidemiology | Chongqing, China | 2020–2025 | During zero-COVID period, incidence decreased by 68.61% (2020), 25.66% (2021), and 10.59% (2022) vs predicted; 2023 incidence 1.5168 per 100,000; predicted 675 cases in 2024 and 705 in 2025 | NPIs suppressed transmission; burden expected to rebound | Wu 2024, *BMC Public Health* | https://doi.org/10.1186/s12889-024-20116-5 | (wu2024epidemiologicalchangesof pages 1-2, wu2024epidemiologicalchangesof media b02e46ec, wu2024epidemiologicalchangesof media e239d009) |
| Epidemiology | Global/summary burden estimates | Contemporary review (published 2024) | Scarlet fever incidence estimated at 186 per 100,000 children and 33 per 100,000 all ages | Review-level estimate; useful for broad burden comparison | Bergsten 2024, *Virulence* | https://doi.org/10.1080/21505594.2024.2412745 | (bergsten2024theintricatepathogenicity pages 2-3) |
| Resurgence | Shanghai, China; scarlet fever surveillance | 2011–2024 | 25,539 cases; incidence fell from pre-COVID mean 17.1/100,000 (95% CI 9.7–24.3) to post-COVID 4.8/100,000 (95% CI 2.0–10.1); children 4–9 years = 85.6% of cases | No major post-COVID rebound in Shanghai, but substantial ongoing burden in children | Cai 2025, *Lancet Regional Health – Western Pacific* | https://doi.org/10.1016/j.lanwpc.2025.101576 | (cai2025ongoingepidemicof pages 1-2) |
| Resurgence | Shanghai, China; molecular epidemiology | 2011–2024 | 16 emm types; emm12 66.4%, emm1 29.8%; emm1 ST1274 increased from 10.5% pre-COVID to 73.7% post-COVID; 4 novel M1UK isolates identified | Strain replacement and emergence of M1UK may alter future epidemiology | Cai 2025, *Lancet Regional Health – Western Pacific* | https://doi.org/10.1016/j.lanwpc.2025.101576 | (cai2025ongoingepidemicof pages 1-2) |
| Resurgence | Netherlands; invasive *S. pyogenes* isolates | Q1 2022 to Q1 2023 | emm1.0 among invasive isolates rose from 18% (18/100) to 58% (388/670), P<0.0001; M1UK among invasive emm1 rose from 72% to 96% | Strong evidence that recent iGAS surge was driven by expansion of toxigenic M1UK rather than increased carriage | Rümke 2024, *Journal of Clinical Microbiology* | https://doi.org/10.1128/jcm.00766-24 | (rumke2024nationwideupsurgein pages 1-2, rumke2024nationwideupsurgein pages 2-4) |
| Resurgence | Netherlands; genomic surveillance | 2009–2023 | 2,698 invasive isolates, 351 carriage isolates, WGS of 497 emm1 isolates; DNase Spd1 and SpeC acquired in 9% (46/497) of emm1 isolates | Large-scale molecular surveillance supports increased virulence/fitness of emergent clades | Rümke 2024, *Journal of Clinical Microbiology* | https://doi.org/10.1128/jcm.00766-24 | (rumke2024nationwideupsurgein pages 1-2) |
| Resurgence | Australia; tertiary hospital GAS isolate collection | 2021–2022 | 17 non-emm1 clinical isolates; 9 emm types; emm22, emm12, emm3 each 18% (3/17); 82% (14/17) carried at least one scarlet-fever–associated superantigen gene | Superantigen carriage was common and not confined to one emm type | Shaw 2024, *Pathogens* | https://doi.org/10.3390/pathogens13110956 | (shaw2024clinicalsnapshotof pages 1-2) |
| Resurgence | UK surveillance cited in review | Sep–Dec 2022 | 27,486 confirmed scarlet fever cases and 94 deaths; compared with 3,287 infections in the same period of 2017–2018 | Illustrates magnitude of 2022–2023 resurgence in a high-income setting | Matsubara 2023, *International Dental Journal* | https://doi.org/10.1016/j.identj.2023.03.009 | (matsubara2023recrudescenceofscarlet pages 1-2) |
| Transmission | Household spread of GAS pharyngitis/scarlet fever-related infection | General clinical epidemiology | Approximate household transmission rate 35%; incubation period 2–5 days; usually not contagious 24 h after appropriate antimicrobial therapy | Key operational figures for case management and school exclusion advice | Leung 2025, *Current Pediatric Reviews* | https://doi.org/10.2174/1573396320666230726145436 | (leung2025groupaβhemolytic pages 1-2) |
| Transmission | Pharyngeal carriage; adults and school-age children | Contemporary review (published 2024) | Asymptomatic carriage ~3% of adults and 8% of school-age children; school outbreaks may involve up to 50% asymptomatic carriage of outbreak strain | Carriage reservoir helps explain classroom spread and difficulty of control | Bergsten 2024, *Virulence* | https://doi.org/10.1080/21505594.2024.2412745 | (bergsten2024theintricatepathogenicity pages 2-3) |
| Diagnostics | Belgium; 82 throat swabs, culture reference | Nov 2022–Feb 2023 | RADT sensitivity 80.76%, specificity 100%; NAAT sensitivity 100%, specificity 96.42%; 28/82 (34.14%) positive for pathogens, 92.85% of positives were *S. pyogenes* | NAAT outperformed RADT on sensitivity while maintaining high specificity | Panahandeh 2024, *Journal of Clinical Medicine* | https://doi.org/10.3390/jcm13216627 | (panahandeh2024moleculardiagnosticsfor pages 1-2, panahandeh2024moleculardiagnosticsfor pages 2-4, panahandeh2024moleculardiagnosticsfor pages 5-7, panahandeh2024moleculardiagnosticsfor pages 4-5) |
| Diagnostics | Belgium; contingency counts | Nov 2022–Feb 2023 | RADT: 21 true positives, 5 false negatives, 0 false positives, 56 true negatives; NAAT: 26 true positives, 0 false negatives, 2 false positives, 54 true negatives | Useful for direct comparison of missed cases by test modality | Panahandeh 2024, *Journal of Clinical Medicine* | https://doi.org/10.3390/jcm13216627 | (panahandeh2024moleculardiagnosticsfor pages 2-4) |
| Diagnostics | New Zealand; prospective throat swab PCR validation | From 4 Sep 2023; publication 2024 | 1,093 throat swabs; culture positive 262/1,093 (24.0%) vs PCR 319/1,093 (29.2%); overall agreement 94.2%, positive agreement 98.9%, negative agreement 92.8%; median turnaround time improved from 44 h to 16 h | PCR detected more GAS and substantially shortened reporting time | Lucas 2024, *New Zealand Medical Journal* | https://doi.org/10.26635/6965.6676 | (lucas2024alaboratorydevelopedextraction pages 1-2) |
| Diagnostics | The Gambia; children with pharyngitis | Jun 9, 2021–Sep 26, 2022 | 376 participants; culture positive 37/376 (9.8%); LFT positive 119/376 (31.6%); PCR positive 122/376 (32.4%); ID NOW positive 122/366 (33.3%) | Highlights discordance between molecular tests and culture in a high-carriage setting | Armitage 2025, thesis/report | N/A | (armitage2025epidemiologyofstreptococcus pages 76-78, armitage2025epidemiologyofstreptococcus pages 74-76) |
| Diagnostics | The Gambia; diagnostic accuracy vs culture | Jun 2021–Sep 2022 | LFT sensitivity 83.8%, specificity 74.0%; PCR sensitivity 94.6%, specificity 74.3%; ID NOW sensitivity 94.6%, specificity 73.6% | NAAT/PCR were more sensitive than lateral-flow antigen testing in this cohort | Armitage 2025, thesis/report | N/A | (armitage2025epidemiologyofstreptococcus pages 78-81, armitage2025epidemiologyofstreptococcus pages 76-78) |
| Treatment | GAS pharyngitis/scarlet-fever–relevant management | Contemporary review (published 2025) | Antibiotics started within 48 h shorten recovery by 12–24 h; penicillin V 10 days standard; amoxicillin 50 mg/kg/day (max 1200 mg/day); patients generally noncontagious after 24 h of therapy | Supports current first-line treatment and return-to-school timing | Leung 2025, *Current Pediatric Reviews* | https://doi.org/10.2174/1573396320666230726145436 | (leung2025groupaβhemolytic pages 6-7, leung2025groupaβhemolytic pages 1-2) |
| Treatment | Comparative antibiotic outcomes | Review evidence | Cephalosporins reduced relapse vs penicillin: children OR 0.55 (95% CI 0.30–0.99), adults OR 0.42 (95% CI 0.20–0.88) | Suggests alternative agents may modestly improve relapse outcomes, though penicillin remains standard first-line therapy | Leung 2025, *Current Pediatric Reviews* | https://doi.org/10.2174/1573396320666230726145436 | (leung2025groupaβhemolytic pages 7-7) |
| Treatment | Childhood carriage/eradication context | Review evidence | GAS carriage estimated at 5–13% of children; clindamycin for carriage eradication when indicated: 20–30 mg/kg/day, max 900 mg/day, divided TID for 10 days | Routine treatment of carriers is not generally recommended | Leung 2025, *Current Pediatric Reviews* | https://doi.org/10.2174/1573396320666230726145436 | (leung2025groupaβhemolytic pages 7-7) |
| Epidemiology/Impact | Daycare/school and parent work loss from GAS pharyngitis | Review evidence | Children missed mean 1.9 days of daycare/school; 42% of parents missed mean 1.8 workdays | Indicates nontrivial short-term quality-of-life and economic burden | Leung 2025, *Current Pediatric Reviews* | https://doi.org/10.2174/1573396320666230726145436 | (leung2025groupaβhemolytic pages 6-7) |


*Table: This table summarizes the main quantitative findings extracted from the gathered literature on scarlet fever and related group A streptococcal disease. It highlights recent epidemiology, resurgence patterns, transmission estimates, diagnostic performance, and treatment-related figures useful for a disease knowledge base.*

---

## Visual epidemiology evidence
- Extracted figures showing Chongqing annual incidence (2005–2023) and monthly predictions for 2024–2025 are available from the BMC Public Health surveillance report. (wu2024epidemiologicalchangesof media b02e46ec, wu2024epidemiologicalchangesof media e239d009)

---

## Notes on evidence limitations and missing items
1) **PMIDs**: Many retrieved sources in this run did not include PMIDs in the extracted metadata; PMIDs should be added during curation by cross-referencing PubMed using the DOI/metadata.
2) **Ontology identifiers (MONDO/MeSH/SNOMED/ICD-11)**: Not retrieved from dedicated ontology resources here; these should be populated from OLS/MONDO/MeSH browser.
3) **Protective factors**: Not well quantified in the retrieved literature snippets.
4) **Model organisms**: Not extracted; requires targeted searching in GAS pathogenesis literature.


References

1. (bergsten2024theintricatepathogenicity pages 2-3): Helena Bergsten and Victor Nizet. The intricate pathogenicity of group a <i>streptococcus</i> : a comprehensive update. Virulence, Nov 2024. URL: https://doi.org/10.1080/21505594.2024.2412745, doi:10.1080/21505594.2024.2412745. This article has 22 citations and is from a peer-reviewed journal.

2. (leung2025groupaβhemolytic pages 1-2): Alexander K.C. Leung, Joseph M. Lam, Benjamin Barankin, Kin F. Leong, and Kam L. Hon. Group a β-hemolytic streptococcal pharyngitis: an updated review. Current Pediatric Reviews, 21:2-17, Jan 2025. URL: https://doi.org/10.2174/1573396320666230726145436, doi:10.2174/1573396320666230726145436. This article has 14 citations and is from a peer-reviewed journal.

3. (rumke2024nationwideupsurgein pages 1-2): Lidewij W. Rümke, Matthew A. Davies, Stefan M. T. Vestjens, Boas C. L. van der Putten, Wendy C. M. Bril-Keijzers, Marlies A. van Houten, Nynke Y. Rots, Alienke J. Wijmenga-Monsuur, Arie van der Ende, Brechje de Gier, Bart J. M. Vlaminckx, and Nina M. van Sorge. Nationwide upsurge in invasive disease in the context of longitudinal surveillance of carriage and invasive <i>streptococcus pyogenes</i> 2009–2023, the netherlands: a molecular epidemiological study. Journal of Clinical Microbiology, Oct 2024. URL: https://doi.org/10.1128/jcm.00766-24, doi:10.1128/jcm.00766-24. This article has 38 citations and is from a peer-reviewed journal.

4. (rumke2024nationwideupsurgein pages 2-4): Lidewij W. Rümke, Matthew A. Davies, Stefan M. T. Vestjens, Boas C. L. van der Putten, Wendy C. M. Bril-Keijzers, Marlies A. van Houten, Nynke Y. Rots, Alienke J. Wijmenga-Monsuur, Arie van der Ende, Brechje de Gier, Bart J. M. Vlaminckx, and Nina M. van Sorge. Nationwide upsurge in invasive disease in the context of longitudinal surveillance of carriage and invasive <i>streptococcus pyogenes</i> 2009–2023, the netherlands: a molecular epidemiological study. Journal of Clinical Microbiology, Oct 2024. URL: https://doi.org/10.1128/jcm.00766-24, doi:10.1128/jcm.00766-24. This article has 38 citations and is from a peer-reviewed journal.

5. (bergsten2024theintricatepathogenicity pages 3-4): Helena Bergsten and Victor Nizet. The intricate pathogenicity of group a <i>streptococcus</i> : a comprehensive update. Virulence, Nov 2024. URL: https://doi.org/10.1080/21505594.2024.2412745, doi:10.1080/21505594.2024.2412745. This article has 22 citations and is from a peer-reviewed journal.

6. (inamadar2018thestrawberrytongue pages 1-2): ArunC Inamadar, KeshavmurthyA Adya, and Aparna Palit. The strawberry tongue: what, how and where? Indian Journal of Dermatology, Venereology and Leprology, 84:500-505, Jul 2018. URL: https://doi.org/10.4103/ijdvl.ijdvl\_57\_17, doi:10.4103/ijdvl.ijdvl\_57\_17. This article has 28 citations.

7. (wu2024epidemiologicalchangesof pages 1-2): Rui Wu, Yu Xiong, Ju Wang, Baisong Li, Lin Yang, Han Zhao, Jule Yang, Tao Yin, Jun Sun, Li Qi, Jiang Long, Qin Li, Xiaoni Zhong, Wenge Tang, Yaokai Chen, and Kun Su. Epidemiological changes of scarlet fever before, during and after the covid-19 pandemic in chongqing, china: a 19-year surveillance and prediction study. BMC Public Health, Sep 2024. URL: https://doi.org/10.1186/s12889-024-20116-5, doi:10.1186/s12889-024-20116-5. This article has 9 citations and is from a peer-reviewed journal.

8. (slebioda2020scarletfever– pages 3-5): Zuzanna Ślebioda, Agnieszka Mania-Końsko, and Barbara Dorocka-Bobkowska. Scarlet fever – a diagnostic challenge for dentists and physicians: a report of 2 cases with diverse symptoms. Dental and Medical Problems, 57:455-459, Dec 2020. URL: https://doi.org/10.17219/dmp/125574, doi:10.17219/dmp/125574. This article has 6 citations and is from a peer-reviewed journal.

9. (bergsten2024theintricatepathogenicity pages 8-10): Helena Bergsten and Victor Nizet. The intricate pathogenicity of group a <i>streptococcus</i> : a comprehensive update. Virulence, Nov 2024. URL: https://doi.org/10.1080/21505594.2024.2412745, doi:10.1080/21505594.2024.2412745. This article has 22 citations and is from a peer-reviewed journal.

10. (m.2026araremanifestation pages 1-2): Kavyadeepu R. M. and Mohnish Sekar. A rare manifestation of scarlet fever with a staphylococcal abscess. International Journal of Research in Dermatology, 12:173-177, Feb 2026. URL: https://doi.org/10.18203/issn.2455-4529.intjresdermatol20260378, doi:10.18203/issn.2455-4529.intjresdermatol20260378. This article has 0 citations.

11. (m.2026araremanifestation pages 2-4): Kavyadeepu R. M. and Mohnish Sekar. A rare manifestation of scarlet fever with a staphylococcal abscess. International Journal of Research in Dermatology, 12:173-177, Feb 2026. URL: https://doi.org/10.18203/issn.2455-4529.intjresdermatol20260378, doi:10.18203/issn.2455-4529.intjresdermatol20260378. This article has 0 citations.

12. (leung2025groupaβhemolytic pages 6-7): Alexander K.C. Leung, Joseph M. Lam, Benjamin Barankin, Kin F. Leong, and Kam L. Hon. Group a β-hemolytic streptococcal pharyngitis: an updated review. Current Pediatric Reviews, 21:2-17, Jan 2025. URL: https://doi.org/10.2174/1573396320666230726145436, doi:10.2174/1573396320666230726145436. This article has 14 citations and is from a peer-reviewed journal.

13. (cai2025ongoingepidemicof pages 1-2): Jiehao Cai, Xingyu Zhou, Chi Zhang, Yue Jiang, Panpan Lv, Yibin Zhou, Mingliang Chen, and Mei Zeng. Ongoing epidemic of scarlet fever in shanghai and the emergence of m1uk lineage group a streptococcus: a 14-year surveillance study across the covid-19 pandemic period. The Lancet Regional Health - Western Pacific, 58:101576, May 2025. URL: https://doi.org/10.1016/j.lanwpc.2025.101576, doi:10.1016/j.lanwpc.2025.101576. This article has 13 citations.

14. (keuleyan2025characterizationofstreptococcus pages 1-2): Emma Keuleyan, Theodor Todorov, Deyan Donchev, Ani Kevorkyan, Radoslava Vazharova, Alexander Kukov, Georgi Todorov, Boriana Georgieva, Iskra Altankova, and Yordanka Uzunova. Characterization of streptococcus pyogenes strains from tonsillopharyngitis and scarlet fever resurgence, 2023—first detection of m1uk in bulgaria. Microorganisms, 13:179, Jan 2025. URL: https://doi.org/10.3390/microorganisms13010179, doi:10.3390/microorganisms13010179. This article has 2 citations.

15. (wu2024epidemiologicalchangesof media b02e46ec): Rui Wu, Yu Xiong, Ju Wang, Baisong Li, Lin Yang, Han Zhao, Jule Yang, Tao Yin, Jun Sun, Li Qi, Jiang Long, Qin Li, Xiaoni Zhong, Wenge Tang, Yaokai Chen, and Kun Su. Epidemiological changes of scarlet fever before, during and after the covid-19 pandemic in chongqing, china: a 19-year surveillance and prediction study. BMC Public Health, Sep 2024. URL: https://doi.org/10.1186/s12889-024-20116-5, doi:10.1186/s12889-024-20116-5. This article has 9 citations and is from a peer-reviewed journal.

16. (wu2024epidemiologicalchangesof media e239d009): Rui Wu, Yu Xiong, Ju Wang, Baisong Li, Lin Yang, Han Zhao, Jule Yang, Tao Yin, Jun Sun, Li Qi, Jiang Long, Qin Li, Xiaoni Zhong, Wenge Tang, Yaokai Chen, and Kun Su. Epidemiological changes of scarlet fever before, during and after the covid-19 pandemic in chongqing, china: a 19-year surveillance and prediction study. BMC Public Health, Sep 2024. URL: https://doi.org/10.1186/s12889-024-20116-5, doi:10.1186/s12889-024-20116-5. This article has 9 citations and is from a peer-reviewed journal.

17. (matsubara2023recrudescenceofscarlet pages 1-2): Victor Haruo Matsubara, Janina Christoforou, and Lakshman Samaranayake. Recrudescence of scarlet fever and its implications for dental professionals. International Dental Journal, 73:331-336, Jun 2023. URL: https://doi.org/10.1016/j.identj.2023.03.009, doi:10.1016/j.identj.2023.03.009. This article has 12 citations and is from a peer-reviewed journal.

18. (matsubara2023recrudescenceofscarlet pages 2-4): Victor Haruo Matsubara, Janina Christoforou, and Lakshman Samaranayake. Recrudescence of scarlet fever and its implications for dental professionals. International Dental Journal, 73:331-336, Jun 2023. URL: https://doi.org/10.1016/j.identj.2023.03.009, doi:10.1016/j.identj.2023.03.009. This article has 12 citations and is from a peer-reviewed journal.

19. (panahandeh2024moleculardiagnosticsfor pages 1-2): Mohammad Hossein Panahandeh, Reza Soleimani, Yasmine Nezzar, Hector Rodriguez-Villalobos, Benoît Kabamba-Mukadi, Alexandre Grimmelprez, and Patricia Schatt. Molecular diagnostics for group a streptococcal pharyngitis: clinical and economic benefits in the belgian healthcare context. Journal of Clinical Medicine, 13:6627, Nov 2024. URL: https://doi.org/10.3390/jcm13216627, doi:10.3390/jcm13216627. This article has 1 citations.

20. (panahandeh2024moleculardiagnosticsfor pages 2-4): Mohammad Hossein Panahandeh, Reza Soleimani, Yasmine Nezzar, Hector Rodriguez-Villalobos, Benoît Kabamba-Mukadi, Alexandre Grimmelprez, and Patricia Schatt. Molecular diagnostics for group a streptococcal pharyngitis: clinical and economic benefits in the belgian healthcare context. Journal of Clinical Medicine, 13:6627, Nov 2024. URL: https://doi.org/10.3390/jcm13216627, doi:10.3390/jcm13216627. This article has 1 citations.

21. (lucas2024alaboratorydevelopedextraction pages 1-2): Rebecca Lucas, Emma Tapp, Rumbi Chimwayange, Luiza Hermoso, and Matthew Blakiston. A laboratory-developed extraction free real-time pcr for group a streptococcus in throat swabs: greater detection and faster results. The New Zealand medical journal, 137 1607:34-38, Dec 2024. URL: https://doi.org/10.26635/6965.6676, doi:10.26635/6965.6676. This article has 0 citations.

22. (esposito2025recentchangesin pages 1-2): Susanna Esposito, Marco Masetti, Carolina Calanca, Nicolò Canducci, Sonia Rasmi, Alessandra Fradusco, and Nicola Principi. Recent changes in the epidemiology of group a streptococcus infections: observations and implications. Microorganisms, 13:1871, Aug 2025. URL: https://doi.org/10.3390/microorganisms13081871, doi:10.3390/microorganisms13081871. This article has 6 citations.

23. (shaw2024clinicalsnapshotof pages 1-2): Phoebe K. Shaw, Andrew J. Hayes, Maree Langton, Angela Berkhout, Keith Grimwood, Mark R. Davies, Mark J. Walker, and Stephan Brouwer. Clinical snapshot of group a streptococcal isolates from an australian tertiary hospital. Pathogens, 13:956, Nov 2024. URL: https://doi.org/10.3390/pathogens13110956, doi:10.3390/pathogens13110956. This article has 1 citations.

24. (panahandeh2024moleculardiagnosticsfor pages 5-7): Mohammad Hossein Panahandeh, Reza Soleimani, Yasmine Nezzar, Hector Rodriguez-Villalobos, Benoît Kabamba-Mukadi, Alexandre Grimmelprez, and Patricia Schatt. Molecular diagnostics for group a streptococcal pharyngitis: clinical and economic benefits in the belgian healthcare context. Journal of Clinical Medicine, 13:6627, Nov 2024. URL: https://doi.org/10.3390/jcm13216627, doi:10.3390/jcm13216627. This article has 1 citations.

25. (panahandeh2024moleculardiagnosticsfor pages 4-5): Mohammad Hossein Panahandeh, Reza Soleimani, Yasmine Nezzar, Hector Rodriguez-Villalobos, Benoît Kabamba-Mukadi, Alexandre Grimmelprez, and Patricia Schatt. Molecular diagnostics for group a streptococcal pharyngitis: clinical and economic benefits in the belgian healthcare context. Journal of Clinical Medicine, 13:6627, Nov 2024. URL: https://doi.org/10.3390/jcm13216627, doi:10.3390/jcm13216627. This article has 1 citations.

26. (armitage2025epidemiologyofstreptococcus pages 76-78): EP Armitage. Epidemiology of streptococcus pyogenes in the gambia: investigating carriage and disease burden, transmission dynamics and diagnostic accuracy. Unknown journal, 2025.

27. (armitage2025epidemiologyofstreptococcus pages 74-76): EP Armitage. Epidemiology of streptococcus pyogenes in the gambia: investigating carriage and disease burden, transmission dynamics and diagnostic accuracy. Unknown journal, 2025.

28. (armitage2025epidemiologyofstreptococcus pages 78-81): EP Armitage. Epidemiology of streptococcus pyogenes in the gambia: investigating carriage and disease burden, transmission dynamics and diagnostic accuracy. Unknown journal, 2025.

29. (leung2025groupaβhemolytic pages 7-7): Alexander K.C. Leung, Joseph M. Lam, Benjamin Barankin, Kin F. Leong, and Kam L. Hon. Group a β-hemolytic streptococcal pharyngitis: an updated review. Current Pediatric Reviews, 21:2-17, Jan 2025. URL: https://doi.org/10.2174/1573396320666230726145436, doi:10.2174/1573396320666230726145436. This article has 14 citations and is from a peer-reviewed journal.
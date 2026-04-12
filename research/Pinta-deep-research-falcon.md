---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T15:57:40.870042'
end_time: '2026-04-04T16:04:33.674447'
duration_seconds: 412.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pinta
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pinta
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pinta** covering all of the
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
- **Disease Name:** Pinta
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Pinta** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Pinta (Infectious Disease)

### Executive summary
Pinta is a chronic, nonvenereal (non-sexually transmitted) endemic treponematosis limited to the skin, classically causing scaly plaques that evolve into persistent dyschromic (hyper-/hypopigmented or achromic) patches. It is caused by the spirochete *Treponema carateum* and historically occurred in tropical Latin America, but modern surveillance is sparse and the current burden is uncertain; the U.S. CDC notes it is rare and found in tropical areas of Latin America. Pinta is curable with single-dose long-acting penicillin, but late pigmentary changes may persist even after microbiologic cure. (stamm2015pintalatinamericas pages 1-3, stamm2015pintalatinamericas pages 3-5, papp2024cdclaboratoryrecommendations pages 3-4)

| Item | Value | Evidence | URL | Publication date |
|---|---|---|---|---|
| Preferred name | Pinta | (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1111/ijd.15264 | 2015-11; 2021-11 |
| Synonyms / alternative names | Mal del pinto; carate | (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1111/ijd.15264 | 2015-11; 2021-11 |
| Causal agent | *Treponema carateum* | (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3, papp2024cdclaboratoryrecommendations pages 3-4) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1371/journal.pntd.0002283; https://doi.org/10.15585/mmwr.rr7301a1 | 2015-11; 2013-10; 2024-02 |
| Transmission type | Nonvenereal; mainly direct skin-to-skin contact | (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3, papp2024cdclaboratoryrecommendations pages 3-4) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1371/journal.pntd.0002283; https://doi.org/10.15585/mmwr.rr7301a1 | 2015-11; 2013-10; 2024-02 |
| Geographic distribution | Historically endemic in Latin America; tropical areas of Latin America/Central and South America; possible persistence in remote regions | (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3, papp2024cdclaboratoryrecommendations pages 3-4) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1371/journal.pntd.0002283; https://doi.org/10.15585/mmwr.rr7301a1 | 2015-11; 2013-10; 2024-02 |
| Taxonomy note | Often discussed with endemic treponematoses; recent review states pinta is caused by a different species, *T. carateum*, while yaws/bejel are *T. pallidum* subspecies | (avilanieto2023syphilisvaccinechallenges pages 1-2, stamm2015pintalatinamericas pages 3-5) | https://doi.org/10.3389/fimmu.2023.1126170; https://doi.org/10.4269/ajtmh.15-0329 | 2023-04; 2015-11 |
| Diagnostic cross-reactivity note | Serology cannot distinguish pinta from other endemic treponematoses or venereal syphilis; *T. carateum* is morphologically/serologically indistinguishable from *T. pallidum* treponemes | (mitja2013advancesinthe pages 3-5, stamm2015pintalatinamericas pages 1-3) | https://doi.org/10.1371/journal.pntd.0002283; https://doi.org/10.4269/ajtmh.15-0329 | 2013-10; 2015-11 |


*Table: This table compiles core naming and identification facts for Pinta, including synonyms, causative agent, transmission, geography, and key taxonomy/diagnostic caveats. It is useful as a compact reference for knowledge-base normalization and evidence tracking.*

---

## 1. Disease Information

### 1.1 Definition and overview (current understanding)
Pinta is a neglected chronic skin disease and the most benign of the endemic treponematoses, in that it is classically described as involving only the skin (without the destructive bone/cartilage manifestations typical of late yaws). It has been described historically in Latin America for centuries and is also referred to as “mal del pinto” and “carate.” (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2)

### 1.2 Key identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO)
Within the retrieved full-text evidence set, explicit ontology/coding identifiers (MONDO, MeSH descriptor IDs, ICD-10/ICD-11 codes, Orphanet, OMIM) were not directly stated, and therefore cannot be asserted here with citations. The most authoritative retrieved recent resource is the CDC’s 2024 laboratory recommendations, which provide organism-level taxonomy and a brief epidemiologic locator but do not provide ICD/MeSH/MONDO mappings. (papp2024cdclaboratoryrecommendations pages 3-4, papp2024cdclaboratoryrecommendations pages 25-26)

### 1.3 Synonyms / alternative names
Common synonyms reported in peer-reviewed literature include “mal del pinto” and “carate.” (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2)

### 1.4 Evidence source type
Most of the disease-level information for pinta in the retrieved set is aggregated from reviews/perspectives and clinical microbiology/dermatology references, with limited modern case-based literature (e.g., a 2021 case report). (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** infection with the spirochete *Treponema carateum*. (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3, papp2024cdclaboratoryrecommendations pages 3-4)

**Taxonomic framing (current debate):** Recent immunology review articles emphasize that the treponemal diseases are genetically and antigenically highly similar and historically were considered related; one 2023 review explicitly states that pinta is caused by “a different species … namely *Treponema carateum*.” (avilanieto2023syphilisvaccinechallenges pages 1-2)

### 2.2 Risk factors (human clinical/epidemiologic)
**Transmission route:** nonvenereal direct skin-to-skin contact with infectious lesions. (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3, papp2024cdclaboratoryrecommendations pages 3-4)

**Sociodemographic/environmental context:** classically described in poor rural tropical communities, often acquired in childhood or adolescence. (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2)

**Geography as a risk determinant:** tropical Latin America/Central and South America (including persistence in remote settings). CDC 2024 states: “*Treponema carateum* infection results in pinta which, although rare, is found in tropical areas of Latin America.” (papp2024cdclaboratoryrecommendations pages 3-4)

### 2.3 Protective factors
No pinta-specific protective genetic variants, host factors, or environmental protective factors were identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
No host gene–environment interaction evidence was identified in the retrieved evidence set.

---

## 3. Phenotypes

### 3.1 Clinical spectrum and staging
Pinta is commonly described as a staged cutaneous illness:
- **Primary stage:** papules/erythematous scaly plaques at the inoculation site appearing after infection (classically around weeks). (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3)
- **Secondary stage:** disseminated lesions (“pintids”) with pigmentary changes developing months after infection; lesions may persist and remain infectious for years. (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3)
- **Late/tertiary stage:** dyschromia/achromia and cutaneous atrophy occurring years after infection (e.g., 2–5 years in one classic description). (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 3-5)

A 2021 dermatology case report similarly emphasizes a three-stage evolution with early localized lesions, later generalized rash with hyper-/hypopigmented lesions, and late pigmentary change that can resemble vitiligo. (rosa2021maldepinta pages 1-2)

### 3.2 Differential diagnosis
Because late pinta can manifest as dyschromic patches, key differentials include tinea versicolor, vitiligo, melasma, leprosy, and other dermatoses. (mitja2013advancesinthe pages 2-3)

### 3.3 Histopathology (biopsy phenotypes)
Mitjà et al. summarize stage-linked pathology, including early “loss of melanin in basal cells and liquefaction degeneration” and late “epidermal atrophy and the presence of many melanophages in the dermis.” (mitja2013advancesinthe pages 3-5)

### 3.4 Suggested HPO terms
A staged phenotype-to-HPO mapping based on the retrieved literature is provided below.

| Stage/phenotype | Description | Timing | Suggested HPO terms | Evidence (citation IDs) | URL | Publication date |
|---|---|---|---|---|---|---|
| Primary lesion | Initial pruritic, erythematous, scaly papule or plaque at inoculation site; enlarges and typically does **not** ulcerate | ~3 weeks after infection; alternatively reported as 1–8 weeks after infection | Pruritus (HP:0000989); Erythema (HP:0010783); Papule (HP:0200034); Plaque of skin (HP:0032316); Scaly skin (HP:0000958) | (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2, mitja2013advancesinthe pages 2-3, mitja2013advancesinthe pages 3-5) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1111/ijd.15264; https://doi.org/10.1371/journal.pntd.0002283 | 2015-11; 2021-11; 2013-10 |
| Secondary disseminated lesions (“pintids”) | Months to years after primary lesion, disseminated skin lesions develop with generalized rash and pigmentary change; lesions may remain active/infectious for years | Months after infection in classic staging; generalized rash reported over 2–4 years | Rash (HP:0000988); Abnormal skin pigmentation (HP:0000953); Hyperpigmentation of the skin (HP:0000952); Hypopigmentation of the skin (HP:0001010); Acral dyschromia (suggested, mapped broadly to abnormal skin pigmentation) | (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2, mitja2013advancesinthe pages 2-3) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1111/ijd.15264; https://doi.org/10.1371/journal.pntd.0002283 | 2015-11; 2021-11; 2013-10 |
| Late pigmentary disease | Late/tertiary pinta characterized by dyschromia, achromic or hypochromic lesions, and persistent depigmentation; cosmetic disfigurement may remain despite cure | Usually 2–5 years after infection; other reports describe 3–10 years for late changes | Dyschromia (suggested, mapped to Abnormal skin pigmentation HP:0000953); Achromia/Hypopigmentation of the skin (HP:0001010); Hyperpigmentation of the skin (HP:0000952); Vitiligo-like depigmentation (suggested, mapped to HP:0001010) | (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2, mitja2013advancesinthe pages 2-3) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1111/ijd.15264; https://doi.org/10.1371/journal.pntd.0002283 | 2015-11; 2021-11; 2013-10 |
| Skin atrophy | Chronic late lesions may show cutaneous thinning/atrophy accompanying pigment loss | Late stage, usually years after untreated infection | Skin atrophy (HP:0000962) | (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 3-5) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1371/journal.pntd.0002283 | 2015-11; 2013-10 |
| Histopathologic early lesion correlate | Early lesions show loss of melanin in basal cells and liquefaction degeneration | Early/primary stage biopsy finding | Decreased skin pigmentation (suggested, mapped to Hypopigmentation of the skin HP:0001010) | (mitja2013advancesinthe pages 3-5) | https://doi.org/10.1371/journal.pntd.0002283 | 2013-10 |
| Histopathologic late lesion correlate | Late lesions show epidermal atrophy and numerous dermal melanophages | Late stage biopsy finding | Skin atrophy (HP:0000962); Abnormality of skin pigmentation (HP:0000953) | (mitja2013advancesinthe pages 3-5) | https://doi.org/10.1371/journal.pntd.0002283 | 2013-10 |
| Disease distribution/severity pattern | Pinta is generally the most benign endemic treponematosis and is limited to the skin, without the ulcerative or destructive bone disease typical of some other treponematoses | Chronic, slowly progressive if untreated | Cutaneous abnormality (HP:0011121) | (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3, mitja2013advancesinthe pages 3-5) | https://doi.org/10.4269/ajtmh.15-0329; https://doi.org/10.1371/journal.pntd.0002283 | 2015-11; 2013-10 |
| Prognostic note on treatment response | Early lesions heal over months after treatment, but late pigmentary changes may be irreversible or only partially reversible | After therapy; chronic untreated disease worsens cosmetically over years | Abnormal skin pigmentation (HP:0000953) | (rosa2021maldepinta pages 1-2, stamm2015pintalatinamericas pages 3-5) | https://doi.org/10.1111/ijd.15264; https://doi.org/10.4269/ajtmh.15-0329 | 2021-11; 2015-11 |


*Table: This table summarizes the main clinical stages and phenotypes of pinta, with suggested HPO mappings, timing, and severity/progression notes. It is useful for phenotype annotation and natural-history curation in a disease knowledge base.*

### 3.5 Quality of life impact
The retrieved evidence emphasizes disfigurement/cosmetic persistence of late pigmentary changes even after cure, implying psychosocial and quality-of-life impact; however, no quantitative QoL instruments (e.g., SF-36, EQ-5D) were identified for pinta in the retrieved set. (rosa2021maldepinta pages 1-2, stamm2015pintalatinamericas pages 3-5)

---

## 4. Genetic / Molecular Information

### 4.1 Human causal genes and pathogenic variants
Not applicable as a primary genetic disorder. No host genetic susceptibility loci were identified in the retrieved evidence set.

### 4.2 Pathogen molecular data and taxonomy (what is known; key gaps)
- **Not-yet-cultivable / no extant isolates in common use:** The 2015 pinta perspective notes that *T. carateum* is “not-yet-cultivable” and that isolates are not available for study, limiting experimentation and genomic characterization. (stamm2015pintalatinamericas pages 1-3, stamm2015pintalatinamericas pages 3-5)
- **Serologic and morphologic indistinguishability:** *T. carateum* is described as morphologically and serologically indistinguishable from *T. pallidum* subspecies agents of syphilis/yaws/bejel, which contributes to diagnostic ambiguity. (stamm2015pintalatinamericas pages 1-3)
- **Insufficient genomic knowledge for confident subspecies placement:** Both Mitjà et al. and Stamm emphasize that molecular knowledge is insufficient to confidently classify *T. carateum* as a *T. pallidum* subspecies, and that genomic differentiation methods used for *T. pallidum* subspecies have not been applied due to lack of isolates/genomic data. (mitja2013advancesinthe pages 3-5, stamm2015pintalatinamericas pages 1-3)

### 4.3 Suggested ontology terms (molecular/cellular)
Because pinta is a skin-limited treponemal infection with pigmentary pathology:
- **GO (Biological Process) suggestions (inferred from histology/clinical pathology):** inflammatory response; immune response; melanin biosynthetic process (as a downstream phenotype driver); response to bacterium. (mitja2013advancesinthe pages 3-5)
- **CL (Cell Ontology) suggestions:** melanocyte; macrophage (consistent with dermal melanophages); plasma cell (reported in biopsy infiltrates in a 2021 case). (rosa2021maldepinta pages 1-2, mitja2013advancesinthe pages 3-5)

---

## 5. Environmental Information

### 5.1 Non-genetic contributing factors
The evidence emphasizes exposure in tropical rural environments and direct skin contact transmission, rather than toxins/radiation/pollution. (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3)

### 5.2 Infectious agents
Primary agent: *Treponema carateum*. (stamm2015pintalatinamericas pages 1-3, papp2024cdclaboratoryrecommendations pages 3-4)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (clinical mechanism summary)
1) **Initial infection** via direct skin-to-skin contact introduces *T. carateum* into skin. (stamm2015pintalatinamericas pages 1-3, papp2024cdclaboratoryrecommendations pages 3-4)
2) **Primary localized lesion** develops (scaly papule/plaque) without typical ulceration. (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3, mitja2013advancesinthe pages 3-5)
3) **Dissemination within skin** produces secondary lesions (“pintids”) and pigmentary change. (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3)
4) **Chronic inflammatory and pigmentary remodeling** results in long-lasting dyschromia/achromia and possible skin atrophy, with histology including melanophages in dermis and epidermal atrophy in late lesions. (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 3-5)

### 6.2 Upstream vs downstream mechanisms
- **Upstream:** bacterial infection and persistence in skin; local immune response. (mitja2013advancesinthe pages 2-3)
- **Downstream:** pigment loss/redistribution and structural skin changes (atrophy; melanophages). (mitja2013advancesinthe pages 3-5)

### 6.3 Molecular profiling / omics
No pinta-specific transcriptomic/proteomic/metabolomic datasets were identified in the retrieved evidence set.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
Primary affected organ: **skin** (cutaneous-only disease emphasized in multiple sources). (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3)

### 7.2 Tissue/cell level
Affected tissues/cell processes include epidermis/dermis with pigmentary abnormalities; histology in late lesions includes melanophages. (mitja2013advancesinthe pages 3-5)

### 7.3 Suggested UBERON / GO CC
- **UBERON:** skin of body.
- **GO Cellular Component suggestions:** epidermis; dermis; melanosome (as a pigment-related cellular component inference). (mitja2013advancesinthe pages 3-5)

---

## 8. Temporal Development (Natural History)

### 8.1 Onset and course
- **Onset:** classically weeks after infection (papules/plaques), often in childhood/adolescence in endemic settings. (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2)
- **Progression:** chronic evolution over years, with late pigmentary sequelae developing years after initial infection if untreated. (stamm2015pintalatinamericas pages 1-3, rosa2021maldepinta pages 1-2)

### 8.2 Remission patterns
- **Treatment-induced remission:** single-dose penicillin can halt infection and render lesions noninfectious rapidly; however, pigmentary changes may persist. (stamm2015pintalatinamericas pages 3-5, rosa2021maldepinta pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (best-available quantitative data)
Modern surveillance data are limited; however, the retrieved literature provides several quantitative historical/field observations:
- **Historical burden:** an estimated **~1 million cases** occurred in Mexico, Central America, and northern South America in the 1950s (historical estimate cited in a 2015 perspective). (stamm2015pintalatinamericas pages 1-3)
- **Field prevalence example:** a Panama village survey (1982–83) reported **~20%** of the population with clinical evidence of pinta (active/inactive), cited in both a 2015 perspective and the 2013 PLoS NTD review. (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3)
- **Current burden:** the 2015 perspective emphasizes that the “current prevalence … is unknown due to the lack of surveillance data.” (stamm2015pintalatinamericas pages 1-3)

### 9.2 Demographics
A 2013 review reports peak incidence in adults (15–50 years), while other sources emphasize acquisition in children/adolescents; these differences may reflect heterogeneous data sources and limited modern surveillance. (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 2-3)

### 9.3 Geographic distribution
Pinta is primarily associated with tropical areas of Latin America/Central and South America; CDC 2024 characterizes it as rare in tropical Latin America. (mitja2013advancesinthe pages 2-3, papp2024cdclaboratoryrecommendations pages 3-4)

---

## 10. Diagnostics

### 10.1 Clinical diagnosis
Diagnosis relies on compatible clinical lesions (scaly plaques progressing to dyschromic patches) plus epidemiologic context (residence/travel in historically endemic regions) and exclusion of mimics such as tinea versicolor or vitiligo. (mitja2013advancesinthe pages 2-3)

### 10.2 Serologic testing (standard approach; key limitation)
Across endemic treponematoses, diagnostics generally follow syphilis paradigms using both nontreponemal and treponemal tests:
- Nontreponemal tests: RPR, VDRL.
- Treponemal tests: TPHA/TPPA, FTA-Abs, ELISA.
A core limitation is repeatedly emphasized: **serology cannot distinguish pinta from other endemic treponematoses or venereal syphilis.** (mitja2013advancesinthe pages 3-5, stamm2015pintalatinamericas pages 1-3)

A 2021 pinta case report illustrates this diagnostic approach with very high VDRL titer and positive FTA-Abs IgM/IgG in a compatible clinical context. (rosa2021maldepinta pages 1-2)

### 10.3 Direct detection / microscopy / molecular methods
Mitjà et al. emphasize that direct methods are constrained by inability to culture treponemes and the impracticality/low sensitivity of some direct tests in field settings; they note increasing use of PCR and genomic fingerprinting for endemic treponematoses in general, but definitive molecular diagnosis remains limited by availability. (mitja2013advancesinthe pages 1-2, mitja2013advancesinthe pages 3-5)

**Recent (2024) authoritative diagnostic context:** The CDC laboratory recommendations (2024) describe that direct detection is evolving toward molecular methods while serology remains central; the report also notes there are no FDA-cleared molecular tests marketed in the U.S. for *T. pallidum* (which has implications for distinguishing among treponematoses when patients have relevant travel histories). (papp2024cdclaboratoryrecommendations pages 25-26)

### 10.4 Differential diagnosis
Important differentials include tinea versicolor, vitiligo, melasma, leprosy, and other dermatoses causing pigmentary change. (mitja2013advancesinthe pages 2-3)

---

## 11. Outcome / Prognosis

### 11.1 Mortality/survival
No mortality or survival statistics specific to pinta were identified in the retrieved evidence set; pinta is generally characterized as skin-limited and “benign” relative to other treponematoses. (stamm2015pintalatinamericas pages 1-3)

### 11.2 Morbidity and complications
The main long-term morbidity described is chronic pigmentary change (dyschromia/achromia) and possible skin atrophy, which may be persistent despite cure. (stamm2015pintalatinamericas pages 3-5, rosa2021maldepinta pages 1-2)

---

## 12. Treatment

### 12.1 First-line therapy (real-world standard)
**Long-acting intramuscular benzathine penicillin** is widely described as curative across stages:
- A 2015 perspective reports that a single intramuscular dose can render lesions noninfectious in <24 hours and provides dosing guidance (adults 1.2 million units; children 0.6 million units). (stamm2015pintalatinamericas pages 3-5)
- A 2021 case report describes treatment with benzathine penicillin 2.4 million units IM and similarly notes rapid loss of infectiousness (within ~24 hours). (rosa2021maldepinta pages 1-2)

### 12.2 Alternatives / mass drug administration implications
A key implementation-relevant point is that mass azithromycin campaigns for yaws eradication **could also affect pinta** if *T. carateum* is azithromycin-sensitive (not directly proven in the retrieved evidence, but proposed as plausible). (stamm2015pintalatinamericas pages 3-5)

### 12.3 Treatment outcomes
Early lesions may heal over months after treatment; late pigmentary changes may persist. (stamm2015pintalatinamericas pages 3-5, rosa2021maldepinta pages 1-2)

### 12.4 Suggested MAXO terms (treatment actions)
- Intramuscular benzathine penicillin therapy.
- Antibiotic therapy (systemic).
- Public health mass drug administration (azithromycin-based), as a plausible co-benefit when targeting yaws in co-endemic settings. (stamm2015pintalatinamericas pages 3-5)

### 12.5 Clinical trials
No pinta-specific interventional clinical trials were identified in the retrieved evidence set.

---

## 13. Prevention

### 13.1 Primary prevention
No vaccine exists for pinta. Prevention is primarily via reducing skin-to-skin exposure to infectious lesions and through community-level detection and treatment strategies. (stamm2015pintalatinamericas pages 1-3, papp2024cdclaboratoryrecommendations pages 3-4)

### 13.2 Public health control (historical and current implementation)
- **Historical implementation:** mass penicillin campaigns in the 1950s–1960s markedly reduced endemic treponematoses and nearly eradicated them in many regions, but resurgence occurred where political commitment/resources waned. (mitja2013advancesinthe pages 1-2, stamm2015pintalatinamericas pages 3-5)
- **Modern implementation opportunity (indirect):** yaws eradication strategies using azithromycin may have spillover benefits for pinta where co-endemic, contingent on antimicrobial susceptibility. (stamm2015pintalatinamericas pages 3-5)

---

## 14. Other Species / Natural Disease
No evidence for a non-human animal reservoir or naturally occurring pinta in other species was identified in the retrieved evidence set. (Note: other treponematoses have been discussed in non-human primates in general literature, but pinta-specific evidence was not retrieved here.)

---

## 15. Model Organisms
Pinta-specific experimental models are extremely limited in contemporary literature because *T. carateum* is not available as an isolate and is not cultivable in standard systems; this limits the feasibility of modern animal models, in vitro systems, and functional genomics. (stamm2015pintalatinamericas pages 3-5, stamm2015pintalatinamericas pages 1-3)

---

## Recent developments and latest research (prioritizing 2023–2024)

1) **Updated authoritative guidance acknowledging pinta in laboratory diagnostic context (2024):** The CDC’s 2024 syphilis laboratory recommendations explicitly remind laboratorians and clinicians that nonvenereal treponematoses exist, and state: “*Treponema carateum* infection results in pinta which, although rare, is found in tropical areas of Latin America,” emphasizing travel/endemic-area context when interpreting serology and treponemal testing. URL: https://doi.org/10.15585/mmwr.rr7301a1 (Published Feb 2024). (papp2024cdclaboratoryrecommendations pages 3-4, papp2024cdclaboratoryrecommendations pages 1-3)

2) **Modern immunology framing of treponemal disease relatedness (2023):** A 2023 Frontiers in Immunology review on syphilis vaccines explicitly distinguishes pinta’s etiologic agent at the species level (“*Treponema carateum*”) while emphasizing the broader high similarity of pathogenic treponemes, reinforcing why serology alone cannot reliably separate treponemal syndromes and why genomic methods are central to treponemal taxonomy. URL: https://doi.org/10.3389/fimmu.2023.1126170 (Published Apr 2023). (avilanieto2023syphilisvaccinechallenges pages 1-2)

3) **Genomics advances inform the broader treponemal complex but not pinta directly (2024 evidence set):** Recent paleogenomic work on *T. pallidum* subspecies emphasizes very high sequence identity among syphilis/yaws/bejel genomes and the importance of ancient DNA to resolve evolutionary history; pinta is generally referenced as part of the treponemal disease complex, but the retrieved 2024 ancient-genome evidence does not provide pinta-specific genomes, highlighting the ongoing gap in *T. carateum* genomic characterization. (barquera2024ancientgenomesrevealb pages 1-4)

---

## Expert interpretation and analysis (authoritative sources)

- **Diagnostic ambiguity is intrinsic to biology, not just test choice:** Multiple sources converge that *T. carateum* infection produces serologic patterns indistinguishable from syphilis and other endemic treponematoses, so clinical epidemiology and careful differential diagnosis are essential to avoid misclassification (e.g., labeling pinta as sexually transmitted syphilis). (stamm2015pintalatinamericas pages 1-3, mitja2013advancesinthe pages 3-5)

- **The major bottleneck for “modernizing” pinta knowledge is lack of isolates/genomes:** Reviews repeatedly emphasize that absence of *T. carateum* isolates and genomic data limits taxonomic certainty, molecular diagnostics, antimicrobial resistance surveillance, and vaccine-relevant antigen discovery, in contrast to accelerating genomics in syphilis/yaws/bejel research. (stamm2015pintalatinamericas pages 3-5, stamm2015pintalatinamericas pages 1-3)

---

## Key abstract quotes (for evidence anchoring)

- From Mitjà et al. (PLoS Negl Trop Dis, 2013) abstract on endemic treponematoses diagnosis: “Traditionally, the human treponematoses have been differentiated based upon their clinical manifestations and epidemiologic characteristics because the etiologic agents are indistinguishable in the laboratory.” URL: https://doi.org/10.1371/journal.pntd.0002283 (Published Oct 2013). (mitja2013advancesinthe pages 1-2)

---

## Limitations of this report (evidence gaps)
- Explicit MONDO/MeSH/ICD identifiers for pinta were not found in the retrieved full-text evidence set and therefore are not provided with citations.
- Pinta-specific modern surveillance estimates (incidence/prevalence post-2000), antimicrobial susceptibility data (e.g., azithromycin MICs), and pathogen genome sequences were not identified in the retrieved evidence set.
- No pinta-specific clinical trials were identified.

These gaps likely reflect the rarity of modern cases and limited laboratory material availability for *T. carateum*. (stamm2015pintalatinamericas pages 1-3, papp2024cdclaboratoryrecommendations pages 25-26)

References

1. (stamm2015pintalatinamericas pages 1-3): Lola V. Stamm. Pinta: latin america's forgotten disease? The American journal of tropical medicine and hygiene, 93 5:901-3, Nov 2015. URL: https://doi.org/10.4269/ajtmh.15-0329, doi:10.4269/ajtmh.15-0329. This article has 20 citations.

2. (stamm2015pintalatinamericas pages 3-5): Lola V. Stamm. Pinta: latin america's forgotten disease? The American journal of tropical medicine and hygiene, 93 5:901-3, Nov 2015. URL: https://doi.org/10.4269/ajtmh.15-0329, doi:10.4269/ajtmh.15-0329. This article has 20 citations.

3. (papp2024cdclaboratoryrecommendations pages 3-4): John R. Papp, Ina U. Park, Yetunde Fakile, Lara Pereira, Allan Pillay, and Gail A. Bolan. Cdc laboratory recommendations for syphilis testing, united states, 2024. MMWR Recommendations and Reports, 73:1-32, Feb 2024. URL: https://doi.org/10.15585/mmwr.rr7301a1, doi:10.15585/mmwr.rr7301a1. This article has 199 citations.

4. (rosa2021maldepinta pages 1-2): Ralph Vighi da Rosa, Daniele Damares Rodrigues de Souza, André Cartell, and Paulo Ricardo Martins Souza. Mal de pinta, first autochthonous case from south of brazil. International Journal of Dermatology, Nov 2021. URL: https://doi.org/10.1111/ijd.15264, doi:10.1111/ijd.15264. This article has 1 citations and is from a peer-reviewed journal.

5. (mitja2013advancesinthe pages 2-3): Oriol Mitjà, David Šmajs, and Quique Bassat. Advances in the diagnosis of endemic treponematoses: yaws, bejel, and pinta. PLoS Neglected Tropical Diseases, 7:e2283, Oct 2013. URL: https://doi.org/10.1371/journal.pntd.0002283, doi:10.1371/journal.pntd.0002283. This article has 88 citations and is from a domain leading peer-reviewed journal.

6. (avilanieto2023syphilisvaccinechallenges pages 1-2): Carlos Ávila-Nieto, Núria Pedreño-López, Oriol Mitjà, Bonaventura Clotet, Julià Blanco, and Jorge Carrillo. Syphilis vaccine: challenges, controversies and opportunities. Frontiers in Immunology, Apr 2023. URL: https://doi.org/10.3389/fimmu.2023.1126170, doi:10.3389/fimmu.2023.1126170. This article has 54 citations and is from a peer-reviewed journal.

7. (mitja2013advancesinthe pages 3-5): Oriol Mitjà, David Šmajs, and Quique Bassat. Advances in the diagnosis of endemic treponematoses: yaws, bejel, and pinta. PLoS Neglected Tropical Diseases, 7:e2283, Oct 2013. URL: https://doi.org/10.1371/journal.pntd.0002283, doi:10.1371/journal.pntd.0002283. This article has 88 citations and is from a domain leading peer-reviewed journal.

8. (papp2024cdclaboratoryrecommendations pages 25-26): John R. Papp, Ina U. Park, Yetunde Fakile, Lara Pereira, Allan Pillay, and Gail A. Bolan. Cdc laboratory recommendations for syphilis testing, united states, 2024. MMWR Recommendations and Reports, 73:1-32, Feb 2024. URL: https://doi.org/10.15585/mmwr.rr7301a1, doi:10.15585/mmwr.rr7301a1. This article has 199 citations.

9. (mitja2013advancesinthe pages 1-2): Oriol Mitjà, David Šmajs, and Quique Bassat. Advances in the diagnosis of endemic treponematoses: yaws, bejel, and pinta. PLoS Neglected Tropical Diseases, 7:e2283, Oct 2013. URL: https://doi.org/10.1371/journal.pntd.0002283, doi:10.1371/journal.pntd.0002283. This article has 88 citations and is from a domain leading peer-reviewed journal.

10. (papp2024cdclaboratoryrecommendations pages 1-3): John R. Papp, Ina U. Park, Yetunde Fakile, Lara Pereira, Allan Pillay, and Gail A. Bolan. Cdc laboratory recommendations for syphilis testing, united states, 2024. MMWR Recommendations and Reports, 73:1-32, Feb 2024. URL: https://doi.org/10.15585/mmwr.rr7301a1, doi:10.15585/mmwr.rr7301a1. This article has 199 citations.

11. (barquera2024ancientgenomesrevealb pages 1-4): R Barquera, TL Sitter, CL Kirkpatrick, and DA Ramirez. Ancient genomes reveal a deep history of treponemal disease in the americas. Unknown journal, 2024.

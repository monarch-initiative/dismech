---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T13:51:55.274284'
end_time: '2026-05-11T14:08:08.594605'
duration_seconds: 973.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Craniopharyngioma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 48
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Craniopharyngioma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Craniopharyngioma** covering all of the
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
- **Disease Name:** Craniopharyngioma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Craniopharyngioma** covering all of the
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


## Craniopharyngioma — Disease Characteristics Research Report (focus on 2023–2024 literature)

### Target Disease
- **Disease name:** Craniopharyngioma (CP) (campanini2023themolecularpathogenesis pages 1-2, jannelli2023currentadvancesin pages 1-2)
- **Category:** Rare epithelial intracranial tumor of the sellar/suprasellar (pituitary–hypothalamic) region; histologically benign but locally aggressive (neto2025recentadvancesin pages 1-2, campanini2023themolecularpathogenesis pages 1-2, neubecker2026systemicmolecularlytargeted pages 1-2)
- **MONDO / Orphanet / OMIM / MeSH / ICD-10/11 identifiers:** Not retrievable with the current tool configuration (which searches primarily scholarly literature and ClinicalTrials.gov records rather than ontology/coding databases). This report therefore emphasizes peer‑reviewed primary literature and trial records.

---

## 1. Disease Information

### 1.1 Overview / definition (current understanding)
Craniopharyngiomas are rare epithelial intracranial neoplasms that arise along the craniopharyngeal duct / from remnants of **Rathke’s pouch**, typically in the **sellar and suprasellar** region, often extending toward the third ventricle (neto2025recentadvancesin pages 1-2, campanini2023themolecularpathogenesis pages 1-2, campanini2023themolecularpathogenesis pages 2-3). Their clinical impact is largely due to proximity to the **optic apparatus**, **pituitary gland**, and **hypothalamus**, causing visual and endocrine morbidity (biswas2024practicalapplicationof pages 1-2, brastianos2023brafmekinhibitionin pages 1-4).

The WHO classifies craniopharyngiomas as **histologically benign WHO grade 1** tumors, but they can behave aggressively via adherence/invasion of adjacent critical structures (campanini2023themolecularpathogenesis pages 1-2, neto2025recentadvancesin pages 1-2).

### 1.2 Key synonyms / alternative names
Commonly used names include **adamantinomatous craniopharyngioma (ACP)** and **papillary craniopharyngioma (PCP)**, which the 2021 WHO CNS classification treats as **separate tumor entities** (biswas2024practicalapplicationof pages 1-2, jannelli2023currentadvancesin pages 1-2).

### 1.3 Source type note
Most information in this report is derived from **aggregated disease-level resources** (systematic reviews, narrative reviews, population registries) and **clinical trials**; some mechanistic claims are supported by primary molecular studies using human tissue and model systems (brastianos2023brafmekinhibitionin pages 1-4, apps2018tumourcompartmenttranscriptomics pages 1-2, wang2024multiomicsanalysisof pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary causal factors are molecular drivers that define two biologically distinct entities:**
- **Adamantinomatous craniopharyngioma (ACP):** driven by somatic **CTNNB1** mutations (β‑catenin), with Wnt/β‑catenin pathway activation and β‑catenin accumulation in characteristic cell clusters (campanini2023themolecularpathogenesis pages 1-2, campanini2023themolecularpathogenesis pages 4-6).
- **Papillary craniopharyngioma (PCP):** driven by **BRAF p.(V600E)** in ~90–95% (or higher) of cases, activating MAPK/ERK signaling (jannelli2023currentadvancesin pages 1-2, campanini2023themolecularpathogenesis pages 1-2, campanini2023themolecularpathogenesis pages 2-3).

### 2.2 Risk factors
No clear environmental or lifestyle risk factors were identified in the retrieved evidence; CPs are generally considered sporadic tumors with age‑related incidence peaks (an2025molecularsubtypesof pages 1-2, javidialsaadi2025advancesinthe pages 2-4).

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes (clinical presentation)

### 3.1 Common symptoms and signs (with frequencies where available)
Craniopharyngiomas typically have **insidious onset** with symptoms driven by mass effect and hypothalamic–pituitary involvement (javidialsaadi2025advancesinthe pages 4-6, alboqami2024craniopharyngiomaacomprehensive pages 2-5).

Frequent manifestations include:
- **Headache**: reported as 83.6% in one synthesis, and commonly 50–80% across reviews (javidialsaadi2025advancesinthe pages 4-6, gonzalezgallego2025moderntreatmentof pages 2-4).
- **Visual deficits**: reported as 81.6% in one synthesis; classic **bitemporal hemianopia** due to optic chiasm compression, and decreased visual acuity (javidialsaadi2025advancesinthe pages 4-6, alboqami2024craniopharyngiomaacomprehensive pages 2-5, gonzalezgallego2025moderntreatmentof pages 2-4).
- **Endocrine dysfunction** (pituitary axis deficits): endocrine deficits are common (e.g., 75–90% in one review synthesis), including central hypothyroidism, hypogonadism, adrenal insufficiency, and diabetes insipidus (gonzalezgallego2025moderntreatmentof pages 2-4, alboqami2024craniopharyngiomaacomprehensive pages 2-5).
- **Hydrocephalus / raised intracranial pressure**: obstruction of the third ventricle can cause hydrocephalus; reported ranges include 10–30% for obstructive hydrocephalus in one synthesis (alboqami2024craniopharyngiomaacomprehensive pages 2-5, gonzalezgallego2025moderntreatmentof pages 2-4).

Additional phenotype frequencies reported in one review synthesis include endocrine deficit subtypes such as growth hormone deficiency (~85%), gonadotroph deficiency (~40%), ACTH (~25%), TSH (~25%), and diabetes insipidus (~20%) (javidialsaadi2025advancesinthe pages 6-8).

### 3.2 Quality-of-life impact
High overall survival contrasts with long‑term morbidity, driven by visual loss, neuroendocrine deficits, and hypothalamic dysfunction (brastianos2023brafmekinhibitionin pages 1-4, biswas2024practicalapplicationof pages 1-2).

### 3.3 Suggested HPO terms (examples)
- Visual field defect / bitemporal hemianopia: **HP:0001137** (visual field defect), **HP:0000605** (hemianopia)
- Headache: **HP:0002315**
- Hydrocephalus: **HP:0000238**
- Hypopituitarism: **HP:0000871**; Diabetes insipidus: **HP:0000873**
- Hypothyroidism (central): **HP:0000821**; Hypogonadism: **HP:0000135**
- Obesity / hypothalamic obesity: **HP:0001513** (obesity)

(HPO identifiers are provided as ontology suggestions; specific term mapping may be refined for local database standards.)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and hallmark alterations
- **ACP:** CTNNB1 exon 3 mutations (β‑catenin stabilization) and Wnt/β‑catenin pathway activation; β‑catenin‑accumulating clusters are a hallmark (an2025molecularsubtypesof pages 1-2, campanini2023themolecularpathogenesis pages 4-6, campanini2023themolecularpathogenesis pages 1-2).
- **PCP:** BRAF p.(V600E) mutation in ~90–95% (or higher) of tumors (jannelli2023currentadvancesin pages 1-2, campanini2023themolecularpathogenesis pages 1-2, campanini2023themolecularpathogenesis pages 2-3).

### 4.2 Molecular subgroups (recent development: 2024 multi‑omics)
A 2024 multi‑omics study profiled a large cohort (119 ACP and 23 PCP among 142 cases) using WES/RNA‑seq/DNA methylation and defined **three ACP molecular subgroups**—**WNT**, **ImA**, and **ImB**—with distinct pathway activation and imaging/histologic correlates (wang2024multiomicsanalysisof pages 1-2). The **WNT** subgroup showed stronger Wnt/β‑catenin activity and more epithelial/solid tumors, whereas **ImA/ImB** showed inflammatory and interferon responses with more cystic tumors and immune infiltration (wang2024multiomicsanalysisof pages 1-2). Prognostically, WNT had better event‑free survival than ImB, and ImA/ImB were predicted more likely to respond to immune checkpoint blockade than WNT (wang2024multiomicsanalysisof pages 1-2, wang2024multiomicsanalysisof pages 8-10).

### 4.3 Inflammation and tumor microenvironment
Mechanistic tissue studies support that ACP contains a prominent inflammatory microenvironment; tumor clusters are surrounded by gliosis/inflammatory reaction, and inflammatory programs (including inflammasome activation) have been described in transcriptomic/proteomic studies (campanini2023themolecularpathogenesis pages 4-6, apps2018tumourcompartmenttranscriptomics pages 1-2).

### 4.4 Suggested GO biological process terms (examples)
- Wnt signaling pathway: **GO:0016055**
- MAPK cascade: **GO:0000165**
- Inflammatory response: **GO:0006954**
- Cytokine-mediated signaling pathway: **GO:0019221**
- Epithelial to mesenchymal transition: **GO:0001837**

---

## 5. Environmental Information
No specific environmental, lifestyle, or infectious causal agents were identified in the retrieved evidence.

---

## 6. Mechanism / Pathophysiology

### 6.1 Subtype-specific upstream drivers → downstream disease features (causal chains)
**ACP causal chain (simplified):**
Somatic **CTNNB1** mutation → stabilization/nuclear accumulation of **β‑catenin** in discrete tumor clusters → Wnt/β‑catenin hyperactivation with cluster cells acting as signaling centers → secretion of growth factors/cytokines/chemokines and remodeling of surrounding tissue with gliosis/inflammation → locally invasive behavior with cyst formation and adherence to hypothalamus/optic pathways → clinical syndrome of visual deficits and endocrine/hypothalamic dysfunction (campanini2023themolecularpathogenesis pages 4-6, apps2018tumourcompartmenttranscriptomics pages 1-2, alboqami2024craniopharyngiomaacomprehensive pages 2-5).

**PCP causal chain (simplified):**
BRAF p.(V600E) mutation → MAPK/ERK pathway activation → growth of predominantly solid suprasellar tumor mass → optic chiasm compression and pituitary stalk/gland dysfunction → visual field loss and hypopituitarism; importantly, the dominant oncogenic driver yields high sensitivity to BRAF/MEK inhibitors (campanini2023themolecularpathogenesis pages 2-3, brastianos2023brafmekinhibitionin pages 1-4).

### 6.2 MAPK/ERK activity in ACP and therapeutic implications
Although ACP is classically Wnt‑driven, MAPK/ERK pathway activation has been observed in compartments of ACP, and MEK inhibition with **trametinib** in ex vivo ACP tissue reduced pERK1/2, increased apoptosis, and decreased proliferation (campanini2023themolecularpathogenesis pages 4-6). This provides biological rationale for MEK‑inhibitor trials in ACP (NCT05286788 chunk 1).

### 6.3 Advanced technologies (recent)
- **Single-cell and spatial sequencing** have been applied to ACP (70,682 cells profiled in one 2024 study) to refine tumor-cell states including senescence‑associated secretory phenotype (SASP) programs and immune infiltration ().
- **Multi‑omics clustering** (WES/RNA‑seq/DNAm) is being used to derive prognostic and predicted treatment-response subgroups (wang2024multiomicsanalysisof pages 1-2).

### 6.4 Suggested Cell Ontology (CL) terms (examples)
- Pituitary stem/progenitor cell (for mechanistic models): **CL:0002371** (pituitary gland stem cell; exact label may vary by ontology version)
- T cell: **CL:0000084**
- Macrophage / microglia: **CL:0000235** (macrophage), **CL:0000129** (microglial cell)
- Astrocyte (astrogliosis): **CL:0000127**

---

## 7. Anatomical Structures Affected

### 7.1 Primary sites
Craniopharyngiomas arise in the **sellar/suprasellar** region, near the pituitary–hypothalamic axis (campanini2023themolecularpathogenesis pages 1-2, brastianos2023brafmekinhibitionin pages 1-4).

### 7.2 Secondary structures commonly involved (by local extension)
Commonly impacted structures include the **optic chiasm/optic apparatus**, **pituitary stalk**, **hypothalamus**, and sometimes the **third ventricle** (alboqami2024craniopharyngiomaacomprehensive pages 2-5, campanini2023themolecularpathogenesis pages 2-3).

### 7.3 Suggested UBERON terms (examples)
- Pituitary gland: **UBERON:0000007**
- Hypothalamus: **UBERON:0001898**
- Optic chiasm: **UBERON:0000969**
- Third ventricle: **UBERON:0002673**

---

## 8. Temporal Development

### 8.1 Onset
Craniopharyngiomas show a **bimodal age distribution** with a pediatric peak (~5–14/15 years) and an adult peak (variously reported ~45–60 or ~50–74 years) (an2025molecularsubtypesof pages 1-2, javidialsaadi2025advancesinthe pages 2-4, neto2025recentadvancesin pages 1-2).

### 8.2 Progression/course
They are slow-growing but often chronic due to recurrence and long-term morbidity after treatment in this anatomically constrained region (brastianos2023brafmekinhibitionin pages 1-4, neto2025recentadvancesin pages 1-2).

---

## 9. Inheritance and Population

### 9.1 Epidemiology (key statistics)
- CPs constitute ~1.2–4.6% of all brain tumors in one review synthesis (biswas2024practicalapplicationof pages 1-2).
- Incidence estimates vary across sources; one precision-oncology review gives **0.5–2.5 new cases per 1 million people** (biswas2024practicalapplicationof pages 1-2), while other reviews report incidence ranges including **0.13–2 per 100,000** (neto2025recentadvancesin pages 1-2).
- In a nationwide registry study of adolescents/young adults (France, 15–39 years), craniopharyngioma incidence was reported as an age-standardized rate of **0.14 per 100,000 person‑years** (ASR adjusted to US population) (ng2020anepidemiologyreport pages 8-9).

### 9.2 Sex ratio / demographics
Some reviews report no gender predilection overall (neto2025recentadvancesin pages 1-2). Subtype distribution is age-skewed: ACP occurs in both children and adults; PCP is largely adult (neto2025recentadvancesin pages 1-2, jannelli2023currentadvancesin pages 1-2).

---

## 10. Diagnostics

### 10.1 Imaging
Diagnosis is suggested by a sellar/suprasellar mass with cystic and/or solid components on MRI/CT; CT is particularly useful for calcifications, while MRI delineates soft tissue, cystic components, and relationships to the optic chiasm, pituitary stalk/gland, and hypothalamus (gonzalezgallego2025moderntreatmentof pages 2-4, javidialsaadi2025advancesinthe pages 6-8).

Calcifications are emphasized as frequent (reported ~90% in one review synthesis) (alboqami2024craniopharyngiomaacomprehensive pages 2-5).

### 10.2 Histopathology (ACP vs PCP)
- **ACP:** palisading epithelium, stellate reticulum, “wet keratin,” calcifications, xanthogranulomatous reaction; β‑catenin nuclear/cytoplasmic accumulation in clusters (javidialsaadi2025advancesinthe pages 6-8, campanini2023themolecularpathogenesis pages 4-6).
- **PCP:** mature squamous epithelium with fibrovascular cores; lacks ACP features (palisading/stellate reticulum/calcification); driven by BRAF V600E and can be supported by mutant‑specific immunostaining (javidialsaadi2025advancesinthe pages 6-8, campanini2023themolecularpathogenesis pages 1-2).

### 10.3 Molecular testing
Molecular testing is clinically actionable in PCP: identifying **BRAF V600E** enables use of BRAF/MEK inhibition (brastianos2023brafmekinhibitionin pages 1-4, NCT05525273 chunk 1).

### 10.4 Differential diagnosis
Differential diagnosis is not comprehensively extracted from the available evidence snippets in this run; however, in practice it typically includes other sellar/suprasellar masses (e.g., pituitary adenomas, Rathke cleft cyst, germ cell tumors). A dedicated diagnostic radiology/pathology source would be needed for a fully cited differential list.

---

## 11. Outcome / Prognosis

### 11.1 Survival
Overall survival is generally favorable compared with malignant brain tumors, but long-term morbidity is high due to location and treatment effects (brastianos2023brafmekinhibitionin pages 1-4, biswas2024practicalapplicationof pages 1-2). A narrative review reports wide 10‑year survival ranges (40–95%) reflecting heterogeneity and treatment era differences (javidialsaadi2025advancesinthe pages 4-6).

### 11.2 Morbidity and quality-of-life outcomes
Major long-term morbidities include persistent endocrine deficits and hypothalamic dysfunction; hypothalamic injury is a key driver of severe sequelae (gonzalezgallego2025moderntreatmentof pages 2-4, brastianos2023brafmekinhibitionin pages 1-4).

---

## 12. Treatment

### 12.1 Surgery and radiotherapy (standard-of-care backbone)
Standard management historically relies on maximal safe resection with adjuvant radiotherapy when necessary, balanced against risk of hypothalamic/optic injury (brastianos2023brafmekinhibitionin pages 1-4, biswas2024practicalapplicationof pages 1-2).

### 12.2 Targeted therapy — major 2023–2024 development (PCP)
A pivotal 2023 phase II study (papillary CP, BRAF‑mutant, no prior radiation) treated 16 patients with **vemurafenib + cobimetinib** and reported: **15/16 (94%)** durable partial response or better, median tumor volume reduction **91%**, and 12‑month PFS **87%** (24‑month PFS 58%) (brastianos2023brafmekinhibitionin pages 1-4).

Direct abstract quotes supporting this include:
- “**Genotyping has shown that more than 90% of papillary craniopharyngiomas carry BRAF V600E mutations**” (Brastianos et al., 2023) (brastianos2023brafmekinhibitionin pages 1-4).
- “**15 (94% …) had a durable objective partial response or better**… The median reduction in the volume of the tumor was **91%**” (brastianos2023brafmekinhibitionin pages 1-4).

A 2024 systematic review summarizing neoadjuvant/adjuvant BRAF±MEK inhibitor use in PCP found volumetric reductions ranging **24–100%**, with ≥80% reductions reported in **64%** of adjuvant cases, and near‑complete responses common in neoadjuvant settings (cossu2024updateonneoadjuvant pages 1-2).

**Real-world implementation pattern:** targeted therapy is increasingly used to de‑escalate morbid surgery/radiation in BRAF‑mutant PCP, while emphasizing multidisciplinary planning and close toxicity monitoring (biswas2024practicalapplicationof pages 2-3, NCT05525273 chunk 1).

### 12.3 MEK inhibition / inflammatory targeting — emerging for ACP
- A phase 2 clinical trial is evaluating **binimetinib (MEKTOVI®)** in pediatric/young adult ACP (NCT05286788) (NCT05286788 chunk 1).
- Preclinical evidence supports MEK/MAPK pathway involvement in subsets of ACP and sensitivity to MEK inhibition ex vivo (campanini2023themolecularpathogenesis pages 4-6).

### 12.4 Intracystic therapy (cystic CP)
A 2024 retrospective case series evaluated **intracystic peginterferon alfa‑2a** delivered weekly ×6 via Ommaya reservoir in 5 patients with cystic CP, reporting cyst shrinkage in all five and good tolerability ().

### 12.5 Brachytherapy for cystic CP (meta-analysis)
A 2024 systematic review/meta-analysis of brachytherapy in cystic CP (6 trials, 266 patients; ≥5-year follow-up) reported pooled PFS: **75% at 1 year**, **62% at 2–3 years**, and **57% at 5 years** (zhang2024brachytherapyincraniopharyngiomas pages 1-2).

### 12.6 Suggested MAXO terms (examples)
- Surgical resection: **MAXO:0001041** (surgical procedure; refine locally)
- Radiotherapy: **MAXO:0000558**
- Targeted molecular therapy (BRAF/MEK inhibitors): **MAXO:0001035** (drug therapy; refine)
- Intracystic therapy via reservoir: **MAXO:0001176** (intrathecal/intralesional administration; refine)

(MAXO identifiers are provided as ontology suggestions; mapping may require local curation.)

---

## 13. Prevention
No established primary prevention strategies exist because CPs are not linked to modifiable exposures in the retrieved evidence. Secondary/tertiary “prevention” in practice centers on early diagnosis and hypothalamus/optic-sparing treatment strategies to reduce long-term morbidity (brastianos2023brafmekinhibitionin pages 1-4).

---

## 14. Other Species / Natural Disease
No naturally occurring non-human species disease evidence was retrieved in this run.

---

## 15. Model Organisms / Experimental Models

### 15.1 Genetically engineered mouse models (ACP)
Mouse genetic models targeting oncogenic β‑catenin to pituitary embryonic precursors or adult stem cells have been used to model ACP tumorigenesis and support a **paracrine** mechanism in which cluster cells act as signaling centers (apps2017geneticallyengineeredmouse pages 3-5, apps2018tumourcompartmenttranscriptomics pages 1-2).

### 15.2 Ex vivo explant models and translational testing
Human and mouse ACP explant cultures treated with the MEK inhibitor **trametinib** showed reduced proliferation and increased apoptosis, providing a preclinical platform for therapy development (apps2018tumourcompartmenttranscriptomics pages 1-2, campanini2023themolecularpathogenesis pages 4-6).

### 15.3 Suggested resources
Open pediatric cancer multi‑omics initiatives (e.g., OpenPBTA/OpenPedCan) are expanding integrated diagnoses and methylation-based subtyping for pediatric brain tumors including craniopharyngioma ().

---

# Subtype summary table (evidence-linked)

| Subtype | Relative frequency | Key driver mutation(s) | Typical age distribution | Imaging / histopathology | Therapy implications |
|---|---:|---|---|---|---|
| Adamantinomatous craniopharyngioma (ACP) | ~90% of craniopharyngiomas (jannelli2023currentadvancesin pages 1-2, campanini2023themolecularpathogenesis pages 2-3, campanini2023themolecularpathogenesis pages 1-2) | Somatic **CTNNB1** exon 3 mutation; reported prevalence ranges include ~60%, 59%, and ~69-100% across studies/reviews; causes nuclear/cytoplasmic **β-catenin** accumulation and Wnt/β-catenin activation (an2025molecularsubtypesof pages 1-2, neubecker2026systemicmolecularlytargeted pages 1-2, campanini2023themolecularpathogenesis pages 1-2, wang2024multiomicsanalysisof pages 3-5) | Bimodal peaks in childhood and later adulthood: **5-15 years** and **45-60 years**; other reviews report **5-14** and **55-74** years (an2025molecularsubtypesof pages 1-2, neto2025recentadvancesin pages 1-2, campanini2023themolecularpathogenesis pages 2-3, javidialsaadi2025advancesinthe pages 2-4) | Often **multicystic** or mixed solid-cystic; **calcifications common (~90%)**; CT often shows hypodense cystic uni-/multilocular lesion; cyst fluid may resemble “motor oil.” Histology: palisading epithelium, stellate reticulum, finger-like infiltrative protrusions, wet keratin, epithelial whorls, gliosis/inflammation (alboqami2024craniopharyngiomaacomprehensive pages 2-5, javidialsaadi2025advancesinthe pages 6-8, gonzalezgallego2025moderntreatmentof pages 2-4, campanini2023themolecularpathogenesis pages 4-6) | Standard management remains maximal safe surgery ± radiotherapy. No single established targeted therapy yet. Emerging/experimental strategies include **MEK inhibition** (especially inflammatory/ImA subtype), **IL-6/IL-6R blockade** (e.g., tocilizumab), **bevacizumab** combinations, immunotherapy for inflammatory subgroups, and intracystic interferon/peginterferon for cystic disease (wang2024multiomicsanalysisof pages 8-10, wang2024multiomicsanalysisof pages 1-2, NCT05286788 chunk 1, wang2024multiomicsanalysisof pages 3-5) |
| Papillary craniopharyngioma (PCP) | ~10% of craniopharyngiomas (jannelli2023currentadvancesin pages 1-2, campanini2023themolecularpathogenesis pages 2-3) | **BRAF p.V600E** in ~**90-95%** of cases; reviews also report **81-100%** or near-universal prevalence; activates MAPK/ERK signaling (jannelli2023currentadvancesin pages 1-2, campanini2023themolecularpathogenesis pages 2-3, campanini2023themolecularpathogenesis pages 1-2, NCT05525273 chunk 1) | Predominantly **adult-onset**; typically 4th-6th decade / **40-53 years**, mean ~44.7 years; often 5th-6th decades (neto2025recentadvancesin pages 1-2, jannelli2023currentadvancesin pages 1-2, campanini2023themolecularpathogenesis pages 2-3, NCT05525273 chunk 1) | Typically **solid** or uniloculated, **non-calcified** suprasellar/tuberoinfundibular mass; CT/MRI often isodense and noncalcified with hyperintense T2 signal. Histology: mature squamous epithelium over fibrovascular cores; lacks ACP palisading, stellate reticulum, and wet keratin (alboqami2024craniopharyngiomaacomprehensive pages 2-5, javidialsaadi2025advancesinthe pages 6-8, gonzalezgallego2025moderntreatmentof pages 2-4) | Strong precision-oncology signal: **BRAF/MEK inhibition** produces major shrinkage. In prospective phase 2 data, **15/16 (94%)** responded, median tumor-volume reduction **91%**, 12-month PFS **87%**, 24-month PFS **58%** with vemurafenib+cobimetinib; neoadjuvant/adjuvant regimens often allow less morbid surgery/radiation and in some cases no further therapy (brastianos2023brafmekinhibitionin pages 1-4, cossu2024updateonneoadjuvant pages 1-2, NCT03224767 chunk 1, NCT05525273 chunk 1) |


*Table: This table compares adamantinomatous and papillary craniopharyngioma across frequency, molecular drivers, age distribution, imaging and histopathologic features, and current therapeutic implications. It is useful for quickly linking subtype biology to diagnostic expectations and treatment strategy.*

---

## Key Clinical Trials (selected)

- **NCT03224767 (Alliance A071601)** — Adults (≥18) with BRAF V600E papillary CP; **vemurafenib + cobimetinib**; phase II; primary endpoint objective response at 4 months; includes two cohorts (no prior RT vs prior RT) (NCT03224767 chunk 1). This trial is the basis for the NEJM 2023 phase II results summarized above (brastianos2023brafmekinhibitionin pages 1-4).
- **NCT05525273 (Swecranio)** — Adults with BRAF V600E papillary CP; **dabrafenib + trametinib**; phase II; primary endpoint maximal tumor-volume reduction on MRI and QoL/visual/endocrine outcomes as secondary endpoints (NCT05525273 chunk 1).
- **NCT05286788 (CONNECT2108)** — Pediatric/young adult ACP; **binimetinib**; phase II; objective response endpoints stratified by prior radiation (NCT05286788 chunk 1).

ClinicalTrials.gov URLs:
- NCT03224767: https://clinicaltrials.gov/study/NCT03224767 (NCT03224767 chunk 1)
- NCT05525273: https://clinicaltrials.gov/study/NCT05525273 (NCT05525273 chunk 1)
- NCT05286788: https://clinicaltrials.gov/study/NCT05286788 (NCT05286788 chunk 1)

---

## Notes on evidence gaps / limitations
1) **Ontology identifier codes** (MONDO, Orphanet, ICD-10/11, MeSH, OMIM) were not accessible through the current scholarly-literature and ClinicalTrials.gov toolchain and therefore are not included as authoritative code assertions in this report.
2) Some requested elements (detailed differential diagnosis list; population prevalence; long-term endocrine/visual outcome rates by treatment modality) require additional dedicated sources or full-text extraction beyond the available evidence snippets.

---

## Reference list (URLs and publication dates)
The citations above already embed URLs and publication months/years in the evidence source metadata; key recent/high-authority sources include:
- Brastianos PK et al. *N Engl J Med*. July 2023. DOI: https://doi.org/10.1056/NEJMoa2213329 (brastianos2023brafmekinhibitionin pages 1-4)
- Alboqami MN et al. *Heliyon*. June 2024. DOI: https://doi.org/10.1016/j.heliyon.2024.e32112 (alboqami2024craniopharyngiomaacomprehensive pages 2-5)
- Biswas C et al. *Front Endocrinol*. Nov 2024. DOI: https://doi.org/10.3389/fendo.2024.1488958 (biswas2024practicalapplicationof pages 1-2)
- Cossu G et al. *Cancers (Basel)*. Oct 2024. DOI: https://doi.org/10.3390/cancers16203479 (cossu2024updateonneoadjuvant pages 1-2)
- Wang X et al. *Chinese Medical Journal*. Aug 2024. DOI: https://doi.org/10.1097/CM9.0000000000002774 (wang2024multiomicsanalysisof pages 1-2)
- Campanini ML et al. *Arch Endocrinol Metab*. Feb 2023. DOI: https://doi.org/10.20945/2359-3997000000600 (campanini2023themolecularpathogenesis pages 1-2)


References

1. (campanini2023themolecularpathogenesis pages 1-2): Marina Lanciotti Campanini, João Paulo Almeida, Clarissa Silva Martins, and Margaret de Castro. The molecular pathogenesis of craniopharyngiomas. Archives of Endocrinology and Metabolism, 67:266-275, Feb 2023. URL: https://doi.org/10.20945/2359-3997000000600, doi:10.20945/2359-3997000000600. This article has 13 citations.

2. (jannelli2023currentadvancesin pages 1-2): Gianpaolo Jannelli, Francesco Calvanese, Luca Paun, Gerald Raverot, and Emmanuel Jouanneau. Current advances in papillary craniopharyngioma: state-of-the-art therapies and overview of the literature. Brain Sciences, 13:515, Mar 2023. URL: https://doi.org/10.3390/brainsci13030515, doi:10.3390/brainsci13030515. This article has 28 citations.

3. (neto2025recentadvancesin pages 1-2): Clariano Pires de Oliveira Neto, Gilvan Cortês Nascimento, Sabrina da Silva Pereira Damianse, and Manuel dos Santos Faria. Recent advances in craniopharyngioma pathophysiology and emerging therapeutic approaches. Frontiers in Endocrinology, May 2025. URL: https://doi.org/10.3389/fendo.2025.1562942, doi:10.3389/fendo.2025.1562942. This article has 2 citations.

4. (neubecker2026systemicmolecularlytargeted pages 1-2): Joseph J. Neubecker, Daniel W. Griepp, Jeffrey P. Turnbull, Joshua Caskey, Shivum Desai, Adam Mansour, Rabia Ahmed, Andrew Beggs, Annie T. K. Griepp, Heather Heitkotter, Chad F. Claus, Boyd F. Richards, and Prashant S. Kelkar. Systemic molecularly targeted therapies for neoadjuvant and salvage craniopharyngioma: a contemporary narrative review. Biomedicines, 14:499, Feb 2026. URL: https://doi.org/10.3390/biomedicines14030499, doi:10.3390/biomedicines14030499. This article has 0 citations.

5. (campanini2023themolecularpathogenesis pages 2-3): Marina Lanciotti Campanini, João Paulo Almeida, Clarissa Silva Martins, and Margaret de Castro. The molecular pathogenesis of craniopharyngiomas. Archives of Endocrinology and Metabolism, 67:266-275, Feb 2023. URL: https://doi.org/10.20945/2359-3997000000600, doi:10.20945/2359-3997000000600. This article has 13 citations.

6. (biswas2024practicalapplicationof pages 1-2): Chandrima Biswas, Guilherme Mansur, Kyle C. Wu, Daniel M. Prevedello, and Luma Ghalib. Practical application of precision oncology in adult onset craniopharyngiomas. Frontiers in Endocrinology, Nov 2024. URL: https://doi.org/10.3389/fendo.2024.1488958, doi:10.3389/fendo.2024.1488958. This article has 4 citations.

7. (brastianos2023brafmekinhibitionin pages 1-4): Priscilla K. Brastianos, Erin Twohy, Susan Geyer, Elizabeth R. Gerstner, Timothy J. Kaufmann, Shervin Tabrizi, Brian Kabat, Julia Thierauf, Michael W. Ruff, Daniela A. Bota, David A. Reardon, Adam L. Cohen, Macarena I. De La Fuente, Glenn J. Lesser, Jian Campian, Pankaj K. Agarwalla, Priya Kumthekar, Bhupinder Mann, Shivangi Vora, Michael Knopp, A. John Iafrate, William T. Curry, Daniel P. Cahill, Helen A. Shih, Paul D. Brown, Sandro Santagata, Fred G. Barker, and Evanthia Galanis. Braf-mek inhibition in newly diagnosed papillary craniopharyngiomas. The New England journal of medicine, 389 2:118-126, Jul 2023. URL: https://doi.org/10.1056/nejmoa2213329, doi:10.1056/nejmoa2213329. This article has 127 citations and is from a highest quality peer-reviewed journal.

8. (apps2018tumourcompartmenttranscriptomics pages 1-2): John R. Apps, Gabriela Carreno, Jose Mario Gonzalez-Meljem, Scott Haston, Romain Guiho, Julie E. Cooper, Saba Manshaei, Nital Jani, Annett Hölsken, Benedetta Pettorini, Robert J. Beynon, Deborah M. Simpson, Helen C. Fraser, Ying Hong, Shirleen Hallang, Thomas J. Stone, Alex Virasami, Andrew M. Donson, David Jones, Kristian Aquilina, Helen Spoudeas, Abhijit R. Joshi, Richard Grundy, Lisa C. D. Storer, Márta Korbonits, David A. Hilton, Kyoko Tossell, Selvam Thavaraj, Mark A. Ungless, Jesus Gil, Rolf Buslei, Todd Hankinson, Darren Hargrave, Colin Goding, Cynthia L. Andoniadou, Paul Brogan, Thomas S. Jacques, Hywel J. Williams, and Juan Pedro Martinez-Barbera. Tumour compartment transcriptomics demonstrates the activation of inflammatory and odontogenic programmes in human adamantinomatous craniopharyngioma and identifies the mapk/erk pathway as a novel therapeutic target. Acta Neuropathologica, 135:757-777, Mar 2018. URL: https://doi.org/10.1007/s00401-018-1830-2, doi:10.1007/s00401-018-1830-2. This article has 169 citations and is from a highest quality peer-reviewed journal.

9. (wang2024multiomicsanalysisof pages 1-2): Xianlong Wang, Chuan Zhao, Jincheng Lin, Hongxing Liu, Qiuhong Zeng, Hua-Qing Chen, Ye Wang, Dapeng Xu, Wen Chen, Moping Xu, En Zhang, Da Lin, and Zhixiong Lin. Multi-omics analysis of adamantinomatous craniopharyngiomas reveals distinct molecular subgroups with prognostic and treatment response significance. Chinese Medical Journal, 137:859-870, Aug 2024. URL: https://doi.org/10.1097/cm9.0000000000002774, doi:10.1097/cm9.0000000000002774. This article has 21 citations and is from a peer-reviewed journal.

10. (campanini2023themolecularpathogenesis pages 4-6): Marina Lanciotti Campanini, João Paulo Almeida, Clarissa Silva Martins, and Margaret de Castro. The molecular pathogenesis of craniopharyngiomas. Archives of Endocrinology and Metabolism, 67:266-275, Feb 2023. URL: https://doi.org/10.20945/2359-3997000000600, doi:10.20945/2359-3997000000600. This article has 13 citations.

11. (an2025molecularsubtypesof pages 1-2): Wenhao An, Shouwei Li, Yihua An, and Zhixiong Lin. Molecular subtypes of adamantinomatous craniopharyngiomas. Neuro-Oncology, 27:1180-1192, Feb 2025. URL: https://doi.org/10.1093/neuonc/noaf030, doi:10.1093/neuonc/noaf030. This article has 9 citations and is from a domain leading peer-reviewed journal.

12. (javidialsaadi2025advancesinthe pages 2-4): Mousa Javidialsaadi, Diego D. Luy, Heather L. Smith, Arba Cecia, Seunghyuk Daniel Yang, and Anand V. Germanwala. Advances in the management of craniopharyngioma: a narrative review of recent developments and clinical strategies. Journal of Clinical Medicine, 14:1101, Feb 2025. URL: https://doi.org/10.3390/jcm14041101, doi:10.3390/jcm14041101. This article has 7 citations.

13. (javidialsaadi2025advancesinthe pages 4-6): Mousa Javidialsaadi, Diego D. Luy, Heather L. Smith, Arba Cecia, Seunghyuk Daniel Yang, and Anand V. Germanwala. Advances in the management of craniopharyngioma: a narrative review of recent developments and clinical strategies. Journal of Clinical Medicine, 14:1101, Feb 2025. URL: https://doi.org/10.3390/jcm14041101, doi:10.3390/jcm14041101. This article has 7 citations.

14. (alboqami2024craniopharyngiomaacomprehensive pages 2-5): Maryam Nashi Alboqami, Arwa Khalid S Albaiahy, Bushra Hatim Bukhari, Ali Alkhaibary, Ahoud Alharbi, Sami Khairy, Ali H. Alassiri, Fahd AlSufiani, Ahmed Alkhani, and Ahmed Aloraidi. Craniopharyngioma: a comprehensive review of the clinical presentation, radiological findings, management, and future perspective. Heliyon, 10:e32112, Jun 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e32112, doi:10.1016/j.heliyon.2024.e32112. This article has 33 citations.

15. (gonzalezgallego2025moderntreatmentof pages 2-4): Carlos González-Gallego, Pedro Molina, Cristina Hostalot, Anna Oliva, Alberto Blanco, Paloma Puyalto de Pablo, Silvia Comas, Cristina Carrato, Elena Valassi, and Manel Puig-Domingo. Modern treatment of craniopharyngioma to improve outcomes: evidence of a change of paradigm. Endocrine, 89:20-29, May 2025. URL: https://doi.org/10.1007/s12020-025-04216-9, doi:10.1007/s12020-025-04216-9. This article has 3 citations and is from a peer-reviewed journal.

16. (javidialsaadi2025advancesinthe pages 6-8): Mousa Javidialsaadi, Diego D. Luy, Heather L. Smith, Arba Cecia, Seunghyuk Daniel Yang, and Anand V. Germanwala. Advances in the management of craniopharyngioma: a narrative review of recent developments and clinical strategies. Journal of Clinical Medicine, 14:1101, Feb 2025. URL: https://doi.org/10.3390/jcm14041101, doi:10.3390/jcm14041101. This article has 7 citations.

17. (wang2024multiomicsanalysisof pages 8-10): Xianlong Wang, Chuan Zhao, Jincheng Lin, Hongxing Liu, Qiuhong Zeng, Hua-Qing Chen, Ye Wang, Dapeng Xu, Wen Chen, Moping Xu, En Zhang, Da Lin, and Zhixiong Lin. Multi-omics analysis of adamantinomatous craniopharyngiomas reveals distinct molecular subgroups with prognostic and treatment response significance. Chinese Medical Journal, 137:859-870, Aug 2024. URL: https://doi.org/10.1097/cm9.0000000000002774, doi:10.1097/cm9.0000000000002774. This article has 21 citations and is from a peer-reviewed journal.

18. (NCT05286788 chunk 1):  MEKTOVI® for the Treatment of Pediatric Adamantinomatous Craniopharyngioma. Nationwide Children's Hospital. 2023. ClinicalTrials.gov Identifier: NCT05286788

19. (ng2020anepidemiologyreport pages 8-9): Sam Ng, Sonia Zouaoui, Faiza Bessaoud, Valérie Rigau, Alexandre Roux, Amélie Darlix, Fabienne Bauchet, Hélène Mathieu-Daudé, Brigitte Trétarre, Dominique Figarella-Branger, Johan Pallud, Didier Frappaz, Thomas Roujeau, and Luc Bauchet. An epidemiology report for primary central nervous system tumors in adolescents and young adults: a nationwide population-based study in france, 2008-2013. Neuro-oncology, 22:851-863, Dec 2020. URL: https://doi.org/10.1093/neuonc/noz227, doi:10.1093/neuonc/noz227. This article has 28 citations and is from a domain leading peer-reviewed journal.

20. (NCT05525273 chunk 1): Eva Marie Erfurth, MD, PhD. Treatment of BRAF ( B-Rapidly Accelerated Fibrosarcoma) Mutated Papillary Craniopharyngioma. Eva Marie Erfurth, MD, PhD. 2023. ClinicalTrials.gov Identifier: NCT05525273

21. (cossu2024updateonneoadjuvant pages 1-2): Giulia Cossu, Daniele S. C. Ramsay, Roy T. Daniel, Ahmed El Cadhi, Luc Kerherve, Edouard Morlaix, Sayda A. Houidi, Clément Millot-Piccoli, Renan Chapon, Tuan Le Van, Catherine Cao, Walid Farah, Maxime Lleu, Olivier Baland, Jacques Beaurain, Jean Michel Petit, Brivaël Lemogne, Mahmoud Messerer, and Moncef Berhouma. Update on neoadjuvant and adjuvant braf inhibitors in papillary craniopharyngioma: a systematic review. Cancers, 16:3479, Oct 2024. URL: https://doi.org/10.3390/cancers16203479, doi:10.3390/cancers16203479. This article has 4 citations.

22. (biswas2024practicalapplicationof pages 2-3): Chandrima Biswas, Guilherme Mansur, Kyle C. Wu, Daniel M. Prevedello, and Luma Ghalib. Practical application of precision oncology in adult onset craniopharyngiomas. Frontiers in Endocrinology, Nov 2024. URL: https://doi.org/10.3389/fendo.2024.1488958, doi:10.3389/fendo.2024.1488958. This article has 4 citations.

23. (zhang2024brachytherapyincraniopharyngiomas pages 1-2): Li-Yuan Zhang, Wei Guo, Han-Ze Du, Hui Pan, Yun-Chuan Sun, Hui-Juan Zhu, Shuai-Hua Song, Xiao-Yuan Guo, Yue Jiang, and Qian-Qian Sun. Brachytherapy in craniopharyngiomas: a systematic review and meta-analysis of long-term follow-up. BMC Cancer, May 2024. URL: https://doi.org/10.1186/s12885-024-12397-1, doi:10.1186/s12885-024-12397-1. This article has 4 citations and is from a peer-reviewed journal.

24. (apps2017geneticallyengineeredmouse pages 3-5): John Richard Apps and Juan Pedro Martinez‐Barbera. Genetically engineered mouse models of craniopharyngioma: an opportunity for therapy development and understanding of tumor biology. Brain Pathology, 27:364-369, Apr 2017. URL: https://doi.org/10.1111/bpa.12501, doi:10.1111/bpa.12501. This article has 17 citations and is from a domain leading peer-reviewed journal.

25. (wang2024multiomicsanalysisof pages 3-5): Xianlong Wang, Chuan Zhao, Jincheng Lin, Hongxing Liu, Qiuhong Zeng, Hua-Qing Chen, Ye Wang, Dapeng Xu, Wen Chen, Moping Xu, En Zhang, Da Lin, and Zhixiong Lin. Multi-omics analysis of adamantinomatous craniopharyngiomas reveals distinct molecular subgroups with prognostic and treatment response significance. Chinese Medical Journal, 137:859-870, Aug 2024. URL: https://doi.org/10.1097/cm9.0000000000002774, doi:10.1097/cm9.0000000000002774. This article has 21 citations and is from a peer-reviewed journal.

26. (NCT03224767 chunk 1):  Vemurafenib and Cobimetinib in Treating Patients With BRAF V600E Mutation Positive Craniopharyngioma. Alliance for Clinical Trials in Oncology. 2018. ClinicalTrials.gov Identifier: NCT03224767
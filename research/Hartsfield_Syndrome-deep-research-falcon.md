---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T19:03:37.395724'
end_time: '2026-05-08T19:15:46.053510'
duration_seconds: 728.66
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hartsfield Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hartsfield Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hartsfield Syndrome** covering all of the
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
- **Disease Name:** Hartsfield Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hartsfield Syndrome** covering all of the
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


# Hartsfield Syndrome (FGFR1-related): Disease Characteristics Research Report

## Executive summary
Hartsfield syndrome is an ultrarare Mendelian multiple-congenital-anomaly syndrome defined by the co-occurrence of **holoprosencephaly (HPE)** and **split-hand/foot malformation (ectrodactyly/SHFM)**, often with **cleft lip and/or palate**, caused by pathogenic variants in **FGFR1** (OMIM #615465). Core mechanistic evidence supports **dominant-negative disruption of FGFR1 signaling** for many kinase-domain variants, with downstream **RAS/ERK1/2 (MAPK) pathway dysregulation** demonstrated for at least one patient-derived variant. Published case counts remain small; a 2022 synthesis noted **~37 described individuals**, and importantly identified **parental germline ± somatic mosaicism in ~9% (3/35) of reported families**, substantially affecting recurrence-risk counseling. (harris2022mosaicisminhartsfield pages 1-2, harris2022mosaicisminhartsfield pages 2-3, hong2016dominantnegativekinasedomain pages 1-2, palumbo2019anoveldominantnegative pages 2-4)

## High-value abstract/text quotes supporting key claims
> "Heterozygous kinase domain mutations or homozygous extracellular domain mutations in FGFR1 have been reported to cause Hartsfield syndrome (HS), which is characterized by the triad of holoprosencephaly, ectrodactyly and cleft lip/palate." (courage2019novelsynonymousand pages 1-3)
>
> "Hartsfield syndrome is a rare disorder characterised by the co-occurrence of ectrodactyly and holoprosencephaly … family with Hartsfield syndrome due to a novel variant in FGFR1" (harris2022mosaicisminhartsfield pages 1-2)
>
> "Hartsfield syndrome (OMIM #615465) is a rare clinical entity characterized by the triad of holoprosencephaly, ectrodactyly, and variably cleft lip/palate." (courage2019novelsynonymousand pages 1-3)
>
> "A novel dominant-negative FGFR1 variant causes Hartsfield syndrome by deregulating RAS/ERK1/2 pathway" (palumbo2019anoveldominantnegative pages 2-4)
>
> "Experimental modeling suggests Hartsfield results from a dominant-negative FGFR1 effect, distinct from loss-of-function/haploinsufficiency seen in Kallmann/isolated congenital hypogonadotrophic hypogonadism; Palumbo et al. implicate deregulation of the RAS/ERK1/2 pathway." (harris2022mosaicisminhartsfield pages 3-4)
>
> "The authors report that 37 individuals have been described to date and note prior reports of germline mosaicism; they estimate mosaicism (germline or germline plus somatic) in 3 of 35 (9%) reported families" (harris2022mosaicisminhartsfield pages 1-2)
>
> "Literature review in the paper states germline or germline+somatic parental mosaicism has been demonstrated in 3 of 35 reported families (~9%)." (harris2022mosaicisminhartsfield pages 2-3)


*Blockquote: This artifact compiles direct supporting quotes defining Hartsfield syndrome, its core triad, and mechanistic and inheritance insights including dominant-negative FGFR1 effects, RAS/ERK1/2 deregulation, and parental mosaicism frequency.*

---

## 1. Disease information
### 1.1 What is the disease?
Hartsfield syndrome is a rare developmental disorder characterized by the association of **HPE** (variable severity, including lobar/semilobar/alobar forms) with **ectrodactyly/SHFM**, frequently accompanied by **orofacial clefting** and other multisystem anomalies (neurodevelopmental, endocrine/pituitary, genitourinary, skeletal, ear and cardiac findings). (harris2022mosaicisminhartsfield pages 1-2, courage2019novelsynonymousand pages 1-3, gaudioso2025malformationpatternand pages 5-7)

### 1.2 Key identifiers
- **OMIM:** **615465** (Hartsfield syndrome / FGFR1-related Hartsfield syndrome). (gaudioso2025malformationpatternand pages 1-3, courage2019novelsynonymousand pages 1-3)
- **Causal gene:** **FGFR1** (Fibroblast Growth Factor Receptor 1). (harris2022mosaicisminhartsfield pages 1-2)
- **MONDO / Orphanet / MeSH / ICD-10/ICD-11:** Not retrievable from the currently accessed full-text corpus and therefore should be curated from external disease-ontology resources (OMIM/Orphanet/MONDO browsers) as a data-completeness step.

### 1.3 Synonyms / alternative names
Common usage in the literature includes:
- **FGFR1-related Hartsfield syndrome** and **HRTFDS** (review usage). (gaudioso2025malformationpatternand pages 1-3)
- Descriptive phrasing: “association of holoprosencephaly and ectrodactyly”. (harris2022mosaicisminhartsfield pages 3-4, harris2022mosaicisminhartsfield pages 1-2)

### 1.4 Evidence provenance
Current knowledge is derived largely from **case reports/series and review-level aggregation** rather than population-scale EHR datasets, limiting robust incidence/prevalence estimates. (gaudioso2025malformationpatternand pages 1-3, harris2022mosaicisminhartsfield pages 1-2)

#### Identifier/nomenclature table
| Field | Details |
|---|---|
| Disease name | Hartsfield syndrome; FGFR1-related Hartsfield syndrome (gaudioso2025malformationpatternand pages 1-3, courage2019novelsynonymousand pages 1-3) |
| Common synonyms / alternative names | FGFR1-related Hartsfield syndrome; Hartsfield syndrome phenotype; HRTFDS; syndrome of holoprosencephaly and ectrodactyly (descriptive usage in literature) (gaudioso2025malformationpatternand pages 1-3, hong2016dominantnegativekinasedomain pages 1-2) |
| OMIM | **OMIM #615465** (gaudioso2025malformationpatternand pages 1-3, courage2019novelsynonymousand pages 1-3) |
| Disease class | Ultrara​re Mendelian developmental disorder / multiple congenital anomaly syndrome characterized by forebrain and limb malformations (harris2022mosaicisminhartsfield pages 1-2, palumbo2019anoveldominantnegative pages 2-4) |
| Causal gene | **FGFR1** (Fibroblast Growth Factor Receptor 1) (harris2022mosaicisminhartsfield pages 1-2, courage2019novelsynonymousand pages 1-3) |
| HGNC symbol | **FGFR1** (HGNC-approved gene symbol) (harris2022mosaicisminhartsfield pages 1-2, courage2019novelsynonymousand pages 1-3) |
| Core molecular definition | Disorder caused by pathogenic **FGFR1** variants, most often monoallelic/heterozygous, with rarer biallelic cases reported (harris2022mosaicisminhartsfield pages 3-4, harris2022mosaicisminhartsfield pages 1-2) |
| Inheritance notes | Reported as **autosomal dominant or autosomal recessive**; many cases are **de novo**; **parental germline and/or somatic mosaicism** is documented and relevant for recurrence counseling (gaudioso2025malformationpatternand pages 1-3, gaudioso2025malformationpatternand pages 5-7, harris2022mosaicisminhartsfield pages 2-3) |
| De novo occurrence | Many molecularly confirmed cases arise **de novo**; e.g., specific de novo FGFR1 variants were reported in multiple case reports/series (gaudioso2025malformationpatternand pages 5-7, courage2019novelsynonymousand pages 1-3, palumbo2019anoveldominantnegative pages 2-4) |
| Mosaicism | Parental germline or germline+somatic mosaicism reported in **3 of 35 families (~9%)** in the Harris 2022 review/case report, indicating recurrence risk may be higher than assumed for apparently de novo cases (harris2022mosaicisminhartsfield pages 2-3, harris2022mosaicisminhartsfield pages 1-2) |
| Key defining clinical features | Defining association of **holoprosencephaly (HPE)** and **split-hand/foot malformation (ectrodactyly/SHFM)**, often with **cleft lip/palate**; additional common associated anomalies include craniofacial, endocrine, genital, ear, skeletal, cardiac, and neurodevelopmental findings (harris2022mosaicisminhartsfield pages 1-2, gaudioso2025malformationpatternand pages 1-3, gaudioso2025malformationpatternand pages 5-7) |
| Characteristic triad in many descriptions | **Holoprosencephaly + ectrodactyly + cleft lip/palate (variable)** (harris2022mosaicisminhartsfield pages 1-2, courage2019novelsynonymousand pages 1-3) |
| Major systems involved | Central nervous system, craniofacial/oral, limbs/skeleton, endocrine-pituitary, genitourinary, and cardiovascular systems (gaudioso2025malformationpatternand pages 5-7, palumbo2019anoveldominantnegative pages 2-4) |
| Information level | Disease-level information synthesized from published case reports, case series, and reviews rather than EHR-derived population datasets (harris2022mosaicisminhartsfield pages 1-2, gaudioso2025malformationpatternand pages 1-3, courage2019novelsynonymousand pages 1-3) |


*Table: This table summarizes the core nomenclature and identifiers for Hartsfield syndrome, including OMIM designation, causal gene, inheritance patterns, and defining clinical features. It is useful as a compact reference for disease knowledge base normalization and curation.*

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** Germline pathogenic variants in **FGFR1**. Most reported cases are **heterozygous** (autosomal dominant), often **de novo**; rarer **biallelic/homozygous** cases have been reported. (harris2022mosaicisminhartsfield pages 3-4, gaudioso2025malformationpatternand pages 1-3)

**Mechanistic classes described in the literature** include:
- **Dominant-negative** effects for many kinase-domain variants, experimentally supported in animal models and consistent with the severe syndromic HPE+ectrodactyly phenotype. (hong2016dominantnegativekinasedomain pages 1-2, hong2016dominantnegativekinasedomain pages 7-8)
- **Loss-of-function/haploinsufficiency** as a general mechanism for other FGFR1-related phenotypes (e.g., congenital hypogonadotropic hypogonadism/Kallmann), underscoring allelic heterogeneity across FGFR1 disorders. (harris2022mosaicisminhartsfield pages 3-4, hong2016dominantnegativekinasedomain pages 1-2)

### 2.2 Risk factors
#### Genetic risk factors
- **FGFR1 pathogenic variants** (missense, cryptic splice from synonymous variants, and variants across extracellular and kinase domains) are causal. (courage2019novelsynonymousand pages 1-3, gaudioso2025malformationpatternand pages 5-7, palumbo2019anoveldominantnegative pages 2-4)
- **Parental mosaicism** (germline ± somatic) is an important recurrence risk factor: a 2022 review/case report estimated mosaicism in **3/35 families (~9%)**, with reports of low-level mosaicism detectable by NGS (e.g., ~3% in saliva; ~23% in sperm). (harris2022mosaicisminhartsfield pages 2-3, harris2022mosaicisminhartsfield pages 1-2)
- **Oligogenic/modifier effects**: FGFR1 variation can interact with other pathway genes; an example described in the HPE genetics literature includes combined deleterious variants in **FGFR1** and **FGF8** contributing to HPE. (hong2016dominantnegativekinasedomain pages 1-2)

#### Environmental and maternal factors (HPE context)
For syndromic and non-syndromic HPE, environmental modifiers (e.g., maternal diabetes, teratogens) and incomplete penetrance/variable expressivity complicate counseling, although these are not Hartsfield-specific risk factors. (malta2023holoprosencephalyreviewof pages 8-9, malta2023holoprosencephalyreviewof pages 11-13)

### 2.3 Protective factors
Hartsfield syndrome is primarily genetic; no Hartsfield-specific protective factors were identified in the retrieved evidence. In the broader HPE literature, periconception folate supplementation and avoidance/optimization of maternal risk factors are discussed as potential modifiers, but are not established as protective specifically for FGFR1-related Hartsfield syndrome. (malta2023holoprosencephalyreviewof pages 8-9)

### 2.4 Gene–environment interactions
No direct FGFR1-specific gene–environment interaction data for Hartsfield syndrome were identified in the retrieved primary texts. General HPE literature supports multifactorial/oligogenic models with environmental modifiers affecting penetrance and severity. (malta2023holoprosencephalyreviewof pages 8-9, malta2023holoprosencephalyreviewof pages 11-13)

---

## 3. Phenotypes
### 3.1 Core phenotype and frequencies (molecularly confirmed cohort)
A 2025 review aggregating **26 molecularly confirmed** individuals reported high frequencies for key malformations, including **radiologic skeletal defects (100%)**, **penis/testes anomalies (100%)**, **SHFM (92%)**, **HPE (90%)**, **outer ear anomalies (87%)**, and **oral cleft (76%)**. (gaudioso2025malformationpatternand pages 1-3, gaudioso2025malformationpatternand media d4424630, gaudioso2025malformationpatternand media 39437dcf)

### 3.2 Expanded phenotypic spectrum (selected examples)
Across case reports/series and reviews, additional recurrent features include:
- **Neurodevelopmental:** variable developmental delay/intellectual disability; corpus callosum anomalies; seizures. (courage2019novelsynonymousand pages 1-3, palumbo2019anoveldominantnegative pages 2-4, gaudioso2025malformationpatternand pages 5-7)
- **Endocrine/pituitary:** central diabetes insipidus; hypogonadotropic hypogonadism/gonadotropin deficiency; growth hormone deficiency is recommended to be evaluated. (courage2019novelsynonymousand pages 1-3, kobayashi2020endocrinologicalfeaturesof pages 10-11, gaudioso2025malformationpatternand pages 5-7)
- **Cardiac/genitourinary:** congenital heart defects and genitourinary anomalies are part of the reported spectrum. (gaudioso2025malformationpatternand pages 5-7, gaudioso2025malformationpatternand pages 1-3)

### 3.3 Onset, progression, and quality-of-life impact
- **Onset:** Congenital (structural malformations detectable prenatally or neonatally). (harris2022mosaicisminhartsfield pages 2-3, gaudioso2025malformationpatternand pages 5-7)
- **Course:** Lifelong, with major morbidity driven by HPE severity and complications (feeding/aspiration, seizures, hydrocephalus, spasticity, endocrine dysfunction). General HPE management reviews emphasize multidisciplinary longitudinal care and note improved survival with advances in care. (malta2023holoprosencephalyreviewof pages 11-13)
- **QoL impact:** Not systematically quantified in disease-specific QoL instruments in the retrieved sources; impact is inferred from neurodevelopmental disability, endocrine disease burden, and surgical/rehabilitation needs. (malta2023holoprosencephalyreviewof pages 11-13, gaudioso2025malformationpatternand pages 5-7)

### 3.4 HPO term suggestions
A phenotype-to-HPO mapping (including frequency where available) is provided below.

| Phenotype / feature | Phenotype type | Approx. frequency in molecularly confirmed FGFR1-related Hartsfield syndrome | Suggested HPO term(s) | Notes | Citation |
|---|---|---:|---|---|---|
| Radiologically identified skeletal defects | Physical manifestation / imaging finding | 100% | HP:0000924 Abnormality of the skeletal system | Review cohort frequency from Gaudioso & Pascolini 2025 Table 1; includes additional limb/radiographic anomalies beyond ectrodactyly | (gaudioso2025malformationpatternand pages 1-3) |
| Genital anomalies (penis/testes anomalies) | Physical manifestation | 100% of evaluated males in review | HP:0000046 Abnormality of the genitalia, HP:0000054 Micropenis, HP:0000028 Cryptorchidism | Reported as penis/testes anomalies in review summary; endocrine-genital overlap is common | (gaudioso2025malformationpatternand pages 1-3, gaudioso2025malformationpatternand pages 5-7) |
| Split-hand/foot malformation (ectrodactyly) | Congenital limb malformation | 92% in review table; described as universal/core in syndrome definitions | HP:0001174 Ectrodactyly, HP:0011347 Split hand, HP:0011348 Split foot | Defining feature of the syndrome; some papers describe it as part of the triad/core phenotype | (gaudioso2025malformationpatternand pages 1-3, harris2022mosaicisminhartsfield pages 1-2) |
| Holoprosencephaly | Structural brain malformation | 90% | HP:0001360 Holoprosencephaly | Includes alobar, semilobar, and lobar forms across reports | (gaudioso2025malformationpatternand pages 1-3, harris2022mosaicisminhartsfield pages 1-2) |
| Outer ear anomalies | Physical manifestation | 87% | HP:0000356 Abnormality of the outer ear | Frequently associated craniofacial finding | (gaudioso2025malformationpatternand pages 1-3) |
| Oral cleft / cleft lip-palate | Craniofacial malformation | 76% | HP:0000202 Oral cleft, HP:0000175 Cleft palate, HP:0000204 Cleft upper lip | Variable feature but commonly associated with the core HPE-ectrodactyly phenotype | (gaudioso2025malformationpatternand pages 1-3, courage2019novelsynonymousand pages 1-3) |
| Central diabetes insipidus | Endocrine abnormality | Reported | HP:0000873 Diabetes insipidus | Recurrent endocrine feature; may evolve over time in long-term follow-up | (courage2019novelsynonymousand pages 1-3, kobayashi2020endocrinologicalfeaturesof pages 10-11, gaudioso2025malformationpatternand pages 5-7) |
| Hypogonadotropic hypogonadism / gonadotrophin deficiency | Endocrine abnormality | Reported | HP:0000044 Hypogonadotropic hypogonadism | Reported in multiple FGFR1-related Hartsfield cases and overlaps with broader FGFR1 phenotype spectrum | (courage2019novelsynonymousand pages 1-3, kobayashi2020endocrinologicalfeaturesof pages 10-11, harris2022mosaicisminhartsfield pages 1-2) |
| Developmental delay / intellectual disability | Neurodevelopmental feature | Reported | HP:0001263 Global developmental delay, HP:0001249 Intellectual disability | Severity appears variable across cases | (courage2019novelsynonymousand pages 1-3, gaudioso2025malformationpatternand pages 5-7, palumbo2019anoveldominantnegative pages 2-4) |
| Corpus callosum anomalies / agenesis | Structural brain malformation | Reported | HP:0001274 Agenesis of the corpus callosum | Includes partial or complete agenesis and other commissural anomalies | (harris2022mosaicisminhartsfield pages 1-2, lansdon2017theuseof pages 5-6, palumbo2019anoveldominantnegative pages 2-4) |
| Cardiac malformations | Congenital malformation | Reported | HP:0001627 Abnormality of the cardiovascular system, HP:0001644 Congenital heart defect | Present in a subset of reported patients; echocardiographic assessment is suggested in review-based management recommendations | (gaudioso2025malformationpatternand pages 5-7, gaudioso2025malformationpatternand pages 1-3) |


*Table: This table summarizes the core and additional phenotypes reported for FGFR1-related Hartsfield syndrome, combining approximate frequencies from the 2025 review with other recurrent but less-quantified features from primary literature. It is useful for phenotype annotation and HPO mapping in a disease knowledge base.*

---

## 4. Genetic / molecular information
### 4.1 Causal gene(s)
- **FGFR1** is the established causal gene for Hartsfield syndrome in the retrieved evidence base. (harris2022mosaicisminhartsfield pages 1-2, courage2019novelsynonymousand pages 1-3)

### 4.2 Pathogenic variant spectrum
Across aggregated patients, variants are most commonly **missense** and cluster in the **tyrosine kinase (TK) domain**, with additional variants reported in extracellular Ig-like domains (notably IgII/IgIII). (gaudioso2025malformationpatternand pages 1-3, gaudioso2025malformationpatternand pages 5-7, gaudioso2025malformationpatternand media da4675c1)

Representative pathogenic variants reported in primary studies include:
- **c.1029G>A (p.Ala343Ala)** creating a cryptic splice donor site; de novo in two siblings with suspected parental gonadal mosaicism. (courage2019novelsynonymousand pages 1-3)
- **c.1868A>G (p.Asp623Gly)** de novo missense in a sporadic case. (courage2019novelsynonymousand pages 1-3)
- **p.Ala645Val** de novo missense with experimentally supported dominant-negative effect and RAS/ERK1/2 deregulation. (palumbo2019anoveldominantnegative pages 2-4)

A structured variant summary table is provided:

| Variant | Protein change | FGFR1 domain | Reported inheritance/context | Mechanistic note | Evidence citation |
|---|---|---|---|---|---|
| c.1029G>A | p.Ala343Ala | IgIII / extracellular region | De novo heterozygous in 2 affected siblings; likely parental gonadal mosaicism | Synonymous variant creating a cryptic splice donor site in exon 8 | (courage2019novelsynonymousand pages 1-3) |
| c.1868A>G | p.Asp623Gly | Tyrosine kinase (TK) | De novo heterozygous, sporadic case | Missense variant in TK domain; pathogenic FGFR1 variant reported in Hartsfield syndrome | (courage2019novelsynonymousand pages 1-3) |
| c.758A>C | p.His253Pro | IgII / extracellular region | Novel heterozygous case | First reported heterozygous extracellular-domain FGFR1 mutation associated with Hartsfield syndrome | (gaudioso2025malformationpatternand pages 5-7) |
| c.1934C>T | p.Ala645Val | Tyrosine kinase (TK) | De novo heterozygous | Dominant-negative FGFR1 effect with deregulation of the RAS/ERK1/2 pathway | (palumbo2019anoveldominantnegative pages 2-4, harris2022mosaicisminhartsfield pages 3-4) |
| c.1880G>C | p.Arg627Thr | Tyrosine kinase (TK) | Recurrent Hartsfield-associated variant; inheritance pattern not specified in excerpt | Recurrently observed missense change; part of TK-domain clustering of pathogenic variants | (gaudioso2025malformationpatternand pages 5-7) |
| not specified in excerpt | p.Cys277Tyr | IgII / extracellular region | Reported Hartsfield-associated FGFR1 variant; inheritance not specified in excerpt | Missense variant; illustrates extracellular-domain involvement beyond TK domain | (gaudioso2025malformationpatternand pages 5-7) |
| not specified in excerpt | p.Gly487Cys | Tyrosine kinase region | De novo | Structural modeling suggested no major global folding destabilization, but possible abnormal disulfide interactions; discussed as overlapping/Hartsfield-like phenotype evidence | (lansdon2017theuseof pages 5-6) |
| not specified in excerpt | p.Val429E | Tyrosine kinase region | Homozygous; supports possible autosomal recessive disease mechanism in FGFR1-related ectrodactyly/hypogonadotropic hypogonadism spectrum | Loss of FGFR substrate 2α recruitment/phosphorylation and reduced MAPK signaling; relevant to recessive FGFR1 developmental phenotypes overlapping Hartsfield spectrum | (harris2022mosaicisminhartsfield pages 1-2) |
| multiple variants, not all specified in excerpt | — | Predominantly TK; also IgII/IgIII, occasional transmembrane/extracellular | Most cases heterozygous; two homozygous cases reported; both autosomal dominant and autosomal recessive inheritance described | Hartsfield syndrome is thought to result mainly from dominant-negative FGFR1 effects, in contrast to haploinsufficiency/loss-of-function in Kallmann syndrome | (harris2022mosaicisminhartsfield pages 3-4, gaudioso2025malformationpatternand pages 1-3, hong2016dominantnegativekinasedomain pages 1-2) |
| Mosaicism statistic | — | — | Parental germline or germline+somatic mosaicism documented in 3 of 35 reported families (~9%) | Important recurrence-risk consideration; NGS may detect low-level mosaicism missed by Sanger sequencing | (harris2022mosaicisminhartsfield pages 2-3, harris2022mosaicisminhartsfield pages 1-2) |


*Table: This table summarizes representative FGFR1 variants reported in Hartsfield syndrome, including domain location, inheritance context, proposed mechanism, and source citations. It is useful for connecting variant-level evidence to disease mechanism and counseling implications such as parental mosaicism.*

### 4.3 Somatic vs germline
Hartsfield syndrome is primarily described as a **germline developmental disorder**, but **parental somatic/gonadal mosaicism** is a key mechanism for recurrence. (harris2022mosaicisminhartsfield pages 2-3, harris2022mosaicisminhartsfield pages 1-2)

### 4.4 Modifier genes / oligogenicity
Evidence in the HPE genetics literature supports an oligogenic model in some families (e.g., synergistic interaction involving FGFR1 and FGF8 variants). (hong2016dominantnegativekinasedomain pages 1-2)

### 4.5 Epigenetics and chromosomal abnormalities
No Hartsfield-specific epigenetic signatures or recurrent chromosomal abnormalities were identified in the retrieved Hartsfield-focused sources.

---

## 5. Environmental information
No disease-specific environmental causes have been identified for Hartsfield syndrome in the retrieved literature (consistent with a primary monogenic etiology). General HPE literature discusses environmental teratogens and maternal diabetes as modifiers of HPE risk/severity. (malta2023holoprosencephalyreviewof pages 8-9, malta2023holoprosencephalyreviewof pages 11-13)

---

## 6. Mechanism / pathophysiology
### 6.1 FGFR1 developmental signaling and the Hartsfield phenotype
FGFR1 encodes a cell-surface receptor with extracellular immunoglobulin-like domains and an intracellular tyrosine kinase domain; ligand binding induces dimerization and autophosphorylation to activate developmental signaling important for **midline forebrain development** and **limb bud patterning**. (harris2022mosaicisminhartsfield pages 1-2)

### 6.2 Dominant-negative mechanism and MAPK pathway involvement
**Dominant-negative kinase-domain variants** are supported experimentally. A mechanistic model proposed in functional studies is that ATP-binding-deficient receptor subunits form inactive dimers that block trans-phosphorylation, yielding severe developmental phenotypes. (hong2016dominantnegativekinasedomain pages 7-8)

For at least one patient-derived variant, the literature explicitly links Hartsfield syndrome to **RAS/ERK1/2 pathway deregulation** (“A novel dominant-negative FGFR1 variant causes Hartsfield syndrome by deregulating RAS/ERK1/2 pathway”). (palumbo2019anoveldominantnegative pages 2-4)

### 6.3 HPE pathway context (2023 understanding)
A 2023 HPE review emphasizes that disruption of **SHH signaling** is a major pathophysiologic mechanism for HPE broadly and that incomplete penetrance/variable expressivity and oligogenic contributions are common, affecting counseling and outcome prediction. (malta2023holoprosencephalyreviewof pages 11-13)

### 6.4 Suggested ontology terms (mechanism)
- **GO biological process (examples):** fibroblast growth factor receptor signaling pathway; MAPK cascade; forebrain development; limb development; embryonic morphogenesis.
- **CL (cell types, examples):** cranial neural crest cell (relevant to craniofacial development; FGFR1 expression discussed in cranial neural crest-derived mesenchyme). (courage2019novelsynonymousand pages 1-3)
- **UBERON (anatomy, examples):** forebrain; prosencephalon; limb bud; palate; pituitary gland.

(These ontology suggestions are consistent with the mechanistic roles described in the cited literature; explicit GO/CL/UBERON IDs were not enumerated in the retrieved sources.)

---

## 7. Anatomical structures affected
Primary anatomical sites include:
- **Brain/forebrain midline structures** (HPE spectrum; corpus callosum anomalies). (harris2022mosaicisminhartsfield pages 1-2, palumbo2019anoveldominantnegative pages 2-4)
- **Hands/feet (autopod)** (ectrodactyly/SHFM). (harris2022mosaicisminhartsfield pages 1-2, courage2019novelsynonymousand pages 1-3)
- **Craniofacial/oral** (cleft lip/palate; dental anomalies in some). (courage2019novelsynonymousand pages 1-3, palumbo2019anoveldominantnegative pages 2-4)
- **Pituitary/hypothalamic axis** (diabetes insipidus; hypogonadotropic hypogonadism). (kobayashi2020endocrinologicalfeaturesof pages 10-11, gaudioso2025malformationpatternand pages 5-7)
- **Genitourinary system** (penis/testes anomalies in reviewed cohort). (gaudioso2025malformationpatternand pages 1-3)
- **Cardiovascular system** (subset with congenital heart defects). (gaudioso2025malformationpatternand pages 5-7)

---

## 8. Temporal development
- **Typical onset:** Congenital; often detected prenatally (ultrasound/MRI) or at birth due to limb and craniofacial anomalies. (harris2022mosaicisminhartsfield pages 2-3, gaudioso2025malformationpatternand pages 5-7)
- **Course:** Chronic lifelong; manifestations may evolve (e.g., endocrine status and metabolic/bone health during adulthood reported in long-term follow-up). (kobayashi2020endocrinologicalfeaturesof pages 10-11)

---

## 9. Inheritance and population
### 9.1 Inheritance pattern
- Reported as **autosomal dominant or autosomal recessive**, with many cases **de novo**. (gaudioso2025malformationpatternand pages 1-3, gaudioso2025malformationpatternand pages 5-7)
- **Parental mosaicism:** documented and clinically important; estimated at **~9% (3/35 families)** in a 2022 synthesis. (harris2022mosaicisminhartsfield pages 2-3, harris2022mosaicisminhartsfield pages 1-2)

### 9.2 Epidemiology
- A 2022 review/case report stated **37 individuals** had been described to date (as of publication). (harris2022mosaicisminhartsfield pages 1-2)
- No robust incidence/prevalence estimates were identified in the retrieved sources.

---

## 10. Diagnostics
### 10.1 Clinical recognition
Clinical suspicion is raised by the **HPE + ectrodactyly/SHFM ± cleft lip/palate** pattern. (courage2019novelsynonymousand pages 1-3, harris2022mosaicisminhartsfield pages 1-2)

### 10.2 Imaging and specialist evaluation
- **Brain MRI** to characterize HPE and associated CNS anomalies; EEG when seizures suspected. (gaudioso2025malformationpatternand pages 5-7)
- **Endocrine evaluation** for pituitary hormone deficiencies (central diabetes insipidus, hypogonadotropic hypogonadism, growth hormone deficiency). (gaudioso2025malformationpatternand pages 5-7, kobayashi2020endocrinologicalfeaturesof pages 10-11)
- **Cardiac evaluation** (echocardiography suggested in review-based management). (gaudioso2025malformationpatternand pages 5-7)

### 10.3 Genetic testing strategy
- **Next-generation sequencing (WES/targeted panels including FGFR1)** is central for diagnosis and for detecting low-level mosaicism; NGS is emphasized as more sensitive than Sanger sequencing for mosaicism. (harris2022mosaicisminhartsfield pages 2-3)
- **Parental testing** is recommended for recurrence-risk assessment due to nontrivial mosaicism frequency. (harris2022mosaicisminhartsfield pages 2-3, harris2022mosaicisminhartsfield pages 1-2)

### 10.4 Differential diagnosis
Differential diagnoses discussed in Hartsfield-focused reviews include:
- **TP63-related disorders** (e.g., EEC spectrum) and other syndromic ectrodactyly/clefting conditions.
- **Genoa syndrome (MIM#601370)**.
- **ANOS1 duplication** (as a differential with overlapping features). (gaudioso2025malformationpatternand pages 5-7)

---

## 11. Outcome / prognosis
Outcomes are variable and are heavily influenced by:
- **Severity of HPE** and its complications (feeding difficulties/aspiration, seizures, hydrocephalus, spasticity, neurodevelopmental impairment).
- **Endocrine dysfunction** (diabetes insipidus; hypogonadotropic hypogonadism; potential bone/metabolic impacts).

General HPE management reviews emphasize that although HPE has high mortality and developmental disability burden, improved diagnostic and supportive care has increased survival in some patients. (malta2023holoprosencephalyreviewof pages 11-13)

---

## 12. Treatment
### 12.1 Current applications and real-world implementations
No disease-specific curative therapy exists in the retrieved evidence; care is **supportive and multidisciplinary**:
- **Craniofacial surgery** for cleft lip/palate repair (as indicated).
- **Orthopedic/rehabilitative management** for limb malformations.
- **Neurology/neurosurgery** for seizures, hydrocephalus, and neurodevelopmental complications.
- **Endocrinology** for DI and hypogonadotropic hypogonadism management.
- **Cardiology** assessment for congenital heart defects.

A multidisciplinary approach with strong genetic counseling is explicitly emphasized in recent synthesis work. (gaudioso2025malformationpatternand pages 1-3, gaudioso2025malformationpatternand pages 5-7, malta2023holoprosencephalyreviewof pages 11-13)

### 12.2 Experimental / trials
A clinical trial search did not identify Hartsfield syndrome-specific interventional trials in the retrieved trial set.

### 12.3 Suggested MAXO terms (examples; to be mapped to exact IDs externally)
- Genetic counseling; prenatal diagnosis; preimplantation genetic testing (where appropriate).
- Brain MRI; echocardiography.
- Cleft lip/palate repair.
- Management of diabetes insipidus; hormone replacement therapy for hypogonadotropic hypogonadism.
- Physical therapy / occupational therapy.

---

## 13. Prevention
Primary prevention is not currently available for monogenic Hartsfield syndrome, but **secondary/tertiary prevention** focuses on:
- **Recurrence-risk reduction through genetic counseling and parental mosaicism testing** (due to ~9% mosaicism estimate in reported families). (harris2022mosaicisminhartsfield pages 2-3, harris2022mosaicisminhartsfield pages 1-2)
- In the broader HPE context: optimizing maternal health (e.g., pre-gestational diabetes) and avoiding teratogens, which may reduce HPE risk/severity generally (not proven Hartsfield-specific). (malta2023holoprosencephalyreviewof pages 8-9)

---

## 14. Other species / natural disease
No naturally occurring veterinary analogue for “Hartsfield syndrome” was identified in the retrieved corpus.

---

## 15. Model organisms
Functional evidence relevant to Hartsfield syndrome includes:
- **Zebrafish assays** used to test human FGFR1 variants; multiple kinase-domain variants exhibited **dominant-negative** behavior in overexpression assays, supporting the dominant-negative disease model for severe syndromic HPE with ectrodactyly. (hong2016dominantnegativekinasedomain pages 1-2)
- Review-level discussion further notes dominant-negative effects in zebrafish for some Hartsfield-associated variants. (lansdon2017theuseof pages 5-6)

---

## Recent developments and latest research (prioritizing 2023–2024)
1. **Holoprosencephaly (HPE) 2023 review** (Malta et al., *Children*, Mar 2023; DOI/URL: https://doi.org/10.3390/children10040647) provides updated clinical-management framing for HPE (multidisciplinary care; endocrine monitoring; counseling complexity due to variable expressivity and incomplete penetrance) and explicitly lists FGFR1 as associated with syndromic HPE including Hartsfield syndrome. (malta2023holoprosencephalyreviewof pages 8-9, malta2023holoprosencephalyreviewof pages 11-13)
2. **Human genetic evidence for FGFR1 signaling beyond development (2024)**: Stamou et al., *Journal of the Endocrine Society*, Jun 2024 (DOI/URL: https://doi.org/10.1210/jendso/bvae118) used a recall-by-genotype design to show that carriers of deleterious FGFR1 variants have measurable alterations in insulin sensitivity/β-cell function, supporting FGFR1 pathway relevance to human metabolic health. While not Hartsfield-specific, this is a notable 2024 expansion of FGFR1 “experiments of nature” into metabolic phenotyping, potentially relevant to long-term care as more Hartsfield patients survive to adulthood. (Note: full-text excerpts for this paper were not successfully extracted into the evidence set here, so disease-specific mechanistic integration should be confirmed directly from the paper.)

---

## Figures/tables (visual corroboration from a 2025 review)
Cropped images from Gaudioso & Pascolini (2025) include **Table 1** summarizing clinical-feature frequencies and figures showing **FGFR1 domain structure and variant distribution**. (gaudioso2025malformationpatternand media d4424630, gaudioso2025malformationpatternand media da4675c1)

---

## Evidence gaps and curation notes
- **Ontology identifiers** (MONDO, Orphanet, MeSH, ICD-10/11) were not available from the retrieved sources and should be added using authoritative external resources (OMIM/Orphanet/MONDO).
- **Population epidemiology** (incidence/prevalence) remains poorly defined; current best quantitative statements are based on reported case counts and family-series synthesis. (harris2022mosaicisminhartsfield pages 1-2)
- **Phenotype frequencies** are based on small aggregated cohorts; additional registry-scale harmonized phenotyping is needed.

---

## Key references (with dates/URLs as available in retrieved texts)
- Harris E et al. *European Journal of Medical Genetics* (May 2022). “Mosaicism in Hartsfield syndrome.” https://doi.org/10.1016/j.ejmg.2022.104491 (harris2022mosaicisminhartsfield pages 1-2)
- Hong S et al. *Human Molecular Genetics* (Feb 2016). “Dominant-negative kinase domain mutations in FGFR1 can explain the clinical severity of Hartsfield syndrome.” https://doi.org/10.1093/hmg/ddw064 (hong2016dominantnegativekinasedomain pages 1-2)
- Palumbo P et al. *European Journal of Human Genetics* (Feb 2019). “A novel dominant-negative FGFR1 variant causes Hartsfield syndrome by deregulating RAS/ERK1/2 pathway.” https://doi.org/10.1038/s41431-019-0350-4 (palumbo2019anoveldominantnegative pages 2-4)
- Courage C et al. *American Journal of Medical Genetics Part A* (Dec 2019). “Novel synonymous and missense variants in FGFR1 causing Hartsfield syndrome.” https://doi.org/10.1002/ajmg.a.61354 (courage2019novelsynonymousand pages 1-3)
- Malta M et al. *Children* (Mar 2023). “Holoprosencephaly: Review of Embryology, Clinical Phenotypes, Etiology and Management.” https://doi.org/10.3390/children10040647 (malta2023holoprosencephalyreviewof pages 8-9)
- Gaudioso F, Pascolini G. *Medical Sciences* (Published 22 Dec 2025). “Malformation Pattern and Molecular Findings in the FGFR1-Related Hartsfield Syndrome Phenotype.” https://doi.org/10.3390/medsci14010004 (gaudioso2025malformationpatternand pages 1-3)



References

1. (harris2022mosaicisminhartsfield pages 1-2): Elizabeth Harris, Ruth Richardson, Srinivas Annavarapu, James Tellez, David Butteriss, Therese Hannon, and Miranda Splitt. Mosaicism in hartsfield syndrome. European Journal of Medical Genetics, 65:104491, May 2022. URL: https://doi.org/10.1016/j.ejmg.2022.104491, doi:10.1016/j.ejmg.2022.104491. This article has 2 citations and is from a peer-reviewed journal.

2. (harris2022mosaicisminhartsfield pages 2-3): Elizabeth Harris, Ruth Richardson, Srinivas Annavarapu, James Tellez, David Butteriss, Therese Hannon, and Miranda Splitt. Mosaicism in hartsfield syndrome. European Journal of Medical Genetics, 65:104491, May 2022. URL: https://doi.org/10.1016/j.ejmg.2022.104491, doi:10.1016/j.ejmg.2022.104491. This article has 2 citations and is from a peer-reviewed journal.

3. (hong2016dominantnegativekinasedomain pages 1-2): Sungkook Hong, Ping Hu, Juliana Marino, Sophia B. Hufnagel, Robert J. Hopkin, Alma Toromanović, Antonio Richieri-Costa, Lucilene A. Ribeiro-Bicudo, Paul Kruszka, Erich Roessler, and Maximilian Muenke. Dominant-negative kinase domain mutations in fgfr1 can explain the clinical severity of hartsfield syndrome. Human molecular genetics, 25 10:1912-1922, Feb 2016. URL: https://doi.org/10.1093/hmg/ddw064, doi:10.1093/hmg/ddw064. This article has 59 citations and is from a domain leading peer-reviewed journal.

4. (palumbo2019anoveldominantnegative pages 2-4): Pietro Palumbo, Antonio Petracca, Roberto Maggi, Tommaso Biagini, Grazia Nardella, Michele Carmine Sacco, Elia Di Schiavi, Massimo Carella, Lucia Micale, and Marco Castori. A novel dominant-negative fgfr1 variant causes hartsfield syndrome by deregulating ras/erk1/2 pathway. European Journal of Human Genetics, 27:1113-1120, Feb 2019. URL: https://doi.org/10.1038/s41431-019-0350-4, doi:10.1038/s41431-019-0350-4. This article has 25 citations and is from a domain leading peer-reviewed journal.

5. (courage2019novelsynonymousand pages 1-3): Carolina Courage, Christopher B. Jackson, Marta Owczarek‐Lipska, Aleksander Jamsheer, Anna Sowińska‐Seidler, Małgorzata Piotrowicz, Lucjusz Jakubowski, Fanny Dallèves, Erik Riesch, John Neidhardt, and Johannes R. Lemke. Novel synonymous and missense variants in fgfr1 causing hartsfield syndrome. American Journal of Medical Genetics Part A, 179:2447-2453, Dec 2019. URL: https://doi.org/10.1002/ajmg.a.61354, doi:10.1002/ajmg.a.61354. This article has 22 citations.

6. (harris2022mosaicisminhartsfield pages 3-4): Elizabeth Harris, Ruth Richardson, Srinivas Annavarapu, James Tellez, David Butteriss, Therese Hannon, and Miranda Splitt. Mosaicism in hartsfield syndrome. European Journal of Medical Genetics, 65:104491, May 2022. URL: https://doi.org/10.1016/j.ejmg.2022.104491, doi:10.1016/j.ejmg.2022.104491. This article has 2 citations and is from a peer-reviewed journal.

7. (gaudioso2025malformationpatternand pages 5-7): Federica Gaudioso and Giulia Pascolini. Malformation pattern and molecular findings in the fgfr1-related hartsfield syndrome phenotype. Medical Sciences, 14:4, Dec 2025. URL: https://doi.org/10.3390/medsci14010004, doi:10.3390/medsci14010004. This article has 0 citations.

8. (gaudioso2025malformationpatternand pages 1-3): Federica Gaudioso and Giulia Pascolini. Malformation pattern and molecular findings in the fgfr1-related hartsfield syndrome phenotype. Medical Sciences, 14:4, Dec 2025. URL: https://doi.org/10.3390/medsci14010004, doi:10.3390/medsci14010004. This article has 0 citations.

9. (hong2016dominantnegativekinasedomain pages 7-8): Sungkook Hong, Ping Hu, Juliana Marino, Sophia B. Hufnagel, Robert J. Hopkin, Alma Toromanović, Antonio Richieri-Costa, Lucilene A. Ribeiro-Bicudo, Paul Kruszka, Erich Roessler, and Maximilian Muenke. Dominant-negative kinase domain mutations in fgfr1 can explain the clinical severity of hartsfield syndrome. Human molecular genetics, 25 10:1912-1922, Feb 2016. URL: https://doi.org/10.1093/hmg/ddw064, doi:10.1093/hmg/ddw064. This article has 59 citations and is from a domain leading peer-reviewed journal.

10. (malta2023holoprosencephalyreviewof pages 8-9): Maísa Malta, Rowim AlMutiri, Christine Saint Martin, and Myriam Srour. Holoprosencephaly: review of embryology, clinical phenotypes, etiology and management. Children, 10:647, Mar 2023. URL: https://doi.org/10.3390/children10040647, doi:10.3390/children10040647. This article has 37 citations.

11. (malta2023holoprosencephalyreviewof pages 11-13): Maísa Malta, Rowim AlMutiri, Christine Saint Martin, and Myriam Srour. Holoprosencephaly: review of embryology, clinical phenotypes, etiology and management. Children, 10:647, Mar 2023. URL: https://doi.org/10.3390/children10040647, doi:10.3390/children10040647. This article has 37 citations.

12. (gaudioso2025malformationpatternand media d4424630): Federica Gaudioso and Giulia Pascolini. Malformation pattern and molecular findings in the fgfr1-related hartsfield syndrome phenotype. Medical Sciences, 14:4, Dec 2025. URL: https://doi.org/10.3390/medsci14010004, doi:10.3390/medsci14010004. This article has 0 citations.

13. (gaudioso2025malformationpatternand media 39437dcf): Federica Gaudioso and Giulia Pascolini. Malformation pattern and molecular findings in the fgfr1-related hartsfield syndrome phenotype. Medical Sciences, 14:4, Dec 2025. URL: https://doi.org/10.3390/medsci14010004, doi:10.3390/medsci14010004. This article has 0 citations.

14. (kobayashi2020endocrinologicalfeaturesof pages 10-11): Sachiko Kobayashi, Junpei Tanigawa, Hidehito Kondo, Shin Nabatame, Azusa Maruoka, Hiroyuki Sho, Kazuko Tanikawa, Ryoko Inui, Michio Otsuki, Iichiro Shimomura, Keiichi Ozono, and Kunihiko Hashimoto. Endocrinological features of hartsfield syndrome in an adult patient with a novel mutation of fgfr1. Journal of the Endocrine Society, Apr 2020. URL: https://doi.org/10.1210/jendso/bvaa041, doi:10.1210/jendso/bvaa041. This article has 4 citations and is from a peer-reviewed journal.

15. (lansdon2017theuseof pages 5-6): Lisa A. Lansdon, H. V. Bernabe, N. Nidey, J. Standley, M. J. Schnieders, and Jeffrey C. Murray. The use of variant maps to explore domain-specific mutations of <i>fgfr1</i>. Journal of Dental Research, 96:1339-1345, Aug 2018. URL: https://doi.org/10.1177/0022034517726496, doi:10.1177/0022034517726496. This article has 11 citations and is from a highest quality peer-reviewed journal.

16. (gaudioso2025malformationpatternand media da4675c1): Federica Gaudioso and Giulia Pascolini. Malformation pattern and molecular findings in the fgfr1-related hartsfield syndrome phenotype. Medical Sciences, 14:4, Dec 2025. URL: https://doi.org/10.3390/medsci14010004, doi:10.3390/medsci14010004. This article has 0 citations.

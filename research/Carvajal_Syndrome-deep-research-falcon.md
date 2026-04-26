---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:09.589475'
end_time: '2026-04-25T22:24:14.697653'
duration_seconds: 545.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Carvajal Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Carvajal Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Carvajal Syndrome** covering all of the
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
- **Disease Name:** Carvajal Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Carvajal Syndrome** covering all of the
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


# Carvajal Syndrome (Carvajal–Huerta syndrome): Disease Characteristics Research Report

## 1. Disease Information

### 1.1 Concise overview
Carvajal syndrome is a rare **cardiocutaneous** disorder classically defined by a triad of **woolly/curly hair**, **palmoplantar keratoderma (PPK)** (often described as epidermolytic/striate), and **arrhythmogenic cardiomyopathy** that commonly has prominent **left‑ventricular involvement** and may present as dilated cardiomyopathy or left‑dominant arrhythmogenic cardiomyopathy. (arıcı2024acaseof pages 1-2, prompona2007magneticresonanceimaging pages 1-2)

### 1.2 Key identifiers (disease database identifiers)
* **OMIM phenotype:** Carvajal syndrome is cited in the DSP literature as **MIM/OMIM #605676**. (pantou2023atruncatingvariant pages 1-2)
* **MONDO / Orphanet / MeSH / ICD-10/11:** These identifiers were **not retrievable from the available evidence corpus** used in this run; therefore they are not asserted here.

### 1.3 Synonyms and alternative names
* **Carvajal–Huerta syndrome** (common synonym). (tosun2025noncompactionanddilated pages 1-2)
* **“Naxos disease variant” / “Naxos–Carvajal phenotype”**: historical overlap terminology; Carvajal is often described as a Naxos-like cardiocutaneous phenotype with more left‑sided disease. (prompona2007magneticresonanceimaging pages 1-2)

### 1.4 Evidence source type
The clinical disease characterization in the retrieved sources is derived primarily from **case reports/series** and **systematic reviews** (human clinical evidence), plus **animal and human iPSC-engineered tissue models** for mechanisms. (arıcı2024acaseof pages 1-2, polivka2016combinationofpalmoplantar pages 1-2, pratt2015dsprulaspontaneous pages 1-2, selgrade2024susceptibilitytoinnate pages 1-2)


## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** pathogenic variants in **DSP (desmoplakin)**, a desmosomal protein essential for cell–cell adhesion and intermediate filament anchoring, are repeatedly reported as causal in Carvajal syndrome. (arıcı2024acaseof pages 1-2, krishnamurthy2011arrhythmogenicdilatedcardiomyopathy pages 1-3, ziołkowska2024carvajalsyndromerelated pages 1-2)

**Inheritance:** typically **autosomal recessive**, often in the setting of consanguinity; rare dominant or de novo presentations with overlapping cardiocutaneous phenotypes have been described in the broader DSP spectrum. (arıcı2024acaseof pages 1-2, arıcı2024acaseof pages 2-3)

### 2.2 Genetic risk factors (causal variants; variant classes)
Carvajal syndrome is most often associated with **biallelic DSP loss-of-function / truncating variants**, frequently in the **C-terminal region** (including exon 24 in many reports), consistent with a loss of desmoplakin function and impaired intermediate filament binding. (arıcı2024acaseof pages 1-2, pantou2023atruncatingvariant pages 1-2)

Concrete examples from recent and classic cases include:
* **DSP c.4297C>T (p.Gln1433\*) homozygous** in a 7‑year‑old with severe biventricular dilatation and LVEF 22%. (arıcı2024acaseof pages 1-2)
* **DSP c.3901C>T (p.Gln1301X) homozygous** in an 11‑year‑old with woolly hair, PPK, and arrhythmogenic dilated cardiomyopathy. (krishnamurthy2011arrhythmogenicdilatedcardiomyopathy pages 1-3)
* **Compound/dual-allele case** (2024): de novo **DSP c.1339C>T p.(Gln447\*)** (predicted nonsense-mediated decay) plus a paternal **DSP c.8204G>C p.(Gly2735Ala)** missense variant; severe arrhythmogenic cardiomyopathy and cardiocutaneous signs. (ziołkowska2024carvajalsyndromerelated pages 1-2)

**Allele frequency example:** in the 2024 Polish Heart Journal vignette, the novel missense allele **p.(Gly2735Ala)** is reported at **~7×10⁻⁷** in gnomAD. (ziołkowska2024carvajalsyndromerelated pages 1-2)

### 2.3 Environmental risk factors / protective factors
No disease-specific, validated environmental risk or protective factors were identified in the retrieved Carvajal-specific clinical evidence. However, in the broader DSP cardiomyopathy literature, disease exacerbation can occur with **physiologic stress/strain**; in engineered and animal models, **mechanical strain** increases functional deficits. (selgrade2024susceptibilitytoinnate pages 1-2, bona2025dsps311aknockinmice pages 13-16)

### 2.4 Gene–environment interaction (current understanding)
**Current concept:** DSP deficiency creates a myocardium that is more vulnerable to inflammatory/innate immune activation and mechanical strain.
* In 2024, a human iPSC engineered heart tissue (EHT) model showed **DSP reduction** increases baseline immune activation and causes **hypersensitivity to Toll-like receptor stimulation**, with worsened contractile impairment, supporting a gene–environment/stressor interaction model for myocarditis-like episodes in DSP disease. (selgrade2024susceptibilitytoinnate pages 1-2)


## 3. Phenotypes (with ontology suggestions)

### 3.1 Core phenotypes
**A. Hair phenotype (woolly/curly hair)**
* Typical onset: **from birth** (woolly hair is repeatedly described as congenital/early). (prompona2007magneticresonanceimaging pages 1-2)
* HPO suggestions: **Woolly hair (HP:0002210)**; **Abnormal hair texture (HP:0011357)**.

**B. Palmoplantar keratoderma (PPK)**
* Typical onset: **first year of life** (described in the Naxos/Carvajal cardiocutaneous spectrum). (prompona2007magneticresonanceimaging pages 1-2)
* HPO suggestions: **Palmoplantar keratoderma (HP:0000972)**; **Epidermolytic palmoplantar keratoderma (HP:0031882)** (if epidermolytic features are present);

**C. Cardiomyopathy and arrhythmias**
* Cardiac phenotype in Carvajal is commonly **left-dominant / dilated cardiomyopathy** with arrhythmias and myocardial fibrosis. (prompona2007magneticresonanceimaging pages 1-2, arıcı2024acaseof pages 1-2)
* HPO suggestions: **Dilated cardiomyopathy (HP:0001644)**; **Arrhythmogenic right ventricular cardiomyopathy (HP:0001658)** (when RV phenotype is emphasized); **Ventricular tachycardia (HP:0004756)**; **Premature ventricular contractions (HP:0011700)**; **Syncope (HP:0001279)**; **Sudden cardiac death (HP:0001645)**.

### 3.2 Phenotype frequencies and notable statistics
Because Carvajal syndrome is rare, frequency data are often aggregated across related desmosomal cardiocutaneous disorders.

* In a systematic review of **458 patients** with inherited desmosomal diseases, the combination of **PPK + hair shaft anomalies** occurred in **161 patients** and was associated with cardiac disease in **129/161 (80.1%)**; nevertheless, skin findings led to cardiac monitoring in only **2.3%** of these patients, indicating major under-recognition of the dermatologic “red flag.” (polivka2016combinationofpalmoplantar pages 1-2)
* In DSP cardiomyopathy cohorts (broader than classic Carvajal), a recognizable cutaneous phenotype (woolly hair and/or PPK) has been reported in **~44–55%** of affected individuals. (brandao2023desmoplakincardiomyopathycomprehensive pages 2-4)

### 3.3 Disease severity, progression, quality-of-life impact
* Carvajal syndrome can progress to **severe heart failure** and life-threatening arrhythmias; a 2024 pediatric case died two years after diagnosis following non-compliance with therapy, underscoring the potential for rapid progression in childhood. (arıcı2024acaseof pages 1-2)
* A 2024 Carvajal case required escalation to **ICD**, **ablation**, and ultimately **orthotopic heart transplantation**. (ziołkowska2024carvajalsyndromerelated pages 1-2)

Quality-of-life instruments (e.g., SF-36, PROMIS) were not identified in the retrieved Carvajal-specific evidence; QOL burden is inferred from severe cardiomyopathy, hospitalizations, device therapy, and transplant. (ziołkowska2024carvajalsyndromerelated pages 1-2)


## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
* **DSP (desmoplakin)** is the primary causal gene supported by multiple Carvajal cases with homozygous or compound variants. (arıcı2024acaseof pages 1-2, krishnamurthy2011arrhythmogenicdilatedcardiomyopathy pages 1-3, ziołkowska2024carvajalsyndromerelated pages 1-2)

### 4.2 Functional role and molecular consequences
Desmoplakin is a core desmosomal protein; a key function is **anchoring intermediate filaments to desmosomes**, which is central to mechanical integrity in both epidermis and myocardium. (pantou2023atruncatingvariant pages 1-2)

Carvajal-associated DSP variants often disrupt the C-terminus (intermediate filament–binding region), and are interpreted mechanistically as reducing effective desmoplakin at junctions and weakening tissue resilience under mechanical stress. (pantou2023atruncatingvariant pages 1-2, prompona2007magneticresonanceimaging pages 1-2)

### 4.3 Variant types and interpretation
* Commonly: **nonsense/frameshift truncating variants** consistent with loss-of-function, often biallelic in Carvajal. (arıcı2024acaseof pages 1-2, krishnamurthy2011arrhythmogenicdilatedcardiomyopathy pages 1-3)
* Missense alleles can contribute in compound states; one recent case combines a de novo nonsense and paternal missense allele with severe phenotype. (ziołkowska2024carvajalsyndromerelated pages 1-2)

Variant classification per ACMG/AMP was not directly extractable from the cited text snippets; the 2024 vignette describes the missense as “likely pathogenic.” (ziołkowska2024carvajalsyndromerelated pages 1-2)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes, epigenetic mechanisms, or chromosomal abnormalities specific to Carvajal syndrome were identified in the retrieved evidence set.


## 5. Environmental Information
No Carvajal-specific environmental toxin/lifestyle/infectious etiology was identified. Within DSP cardiomyopathy, **stressors that activate innate immunity (e.g., inflammatory triggers)** and **mechanical strain** are increasingly discussed as modifiers of “hot phase”/myocarditis-like episodes. (selgrade2024susceptibilitytoinnate pages 1-2)


## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (genotype → tissue dysfunction → clinical phenotype)
1. **DSP pathogenic variants** reduce functional desmoplakin at desmosomes, impairing intermediate filament anchoring and junctional integrity. (pantou2023atruncatingvariant pages 1-2)
2. In myocardium, defective desmosomes predispose to **myocyte dissociation and death**, followed by **fibrous and/or adipose tissue infiltration** and scar formation. (arıcı2024acaseof pages 2-3)
3. Myocardial remodeling plus scar provides substrate for **ventricular arrhythmias** and progressive systolic dysfunction, leading to **heart failure, syncope, sudden cardiac death**, and sometimes the need for transplantation. (prompona2007magneticresonanceimaging pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2)

### 6.2 Inflammation and myocarditis-like episodes (recent development, 2024)
A major recent direction is the concept of **DSP-associated “genetically mediated myocarditis”** (sometimes described clinically as a sterile myocarditis-like process) contributing to injury episodes and progression.

In 2024 (JCI), Selgrade et al. modeled DSP-associated myocarditis using **human iPSC-derived engineered heart tissues**:
* **DSP−/− EHTs** showed baseline transcriptomic immune activation and cytokine release and were **hypersensitive to TLR stimulation**, with greater impairment of contractile function; heterozygous DSP truncation EHTs also showed heightened TLR sensitivity and strain-induced deficits. (selgrade2024susceptibilitytoinnate pages 1-2)
* **Therapeutic implications in vitro:** **colchicine** or **NF‑κB inhibitors** improved baseline/strain-induced force deficits, and **adenine base editing** correction of a DSP truncation reduced inflammatory biomarker release—supporting innate immunity as a potentially targetable downstream pathway. (selgrade2024susceptibilitytoinnate pages 1-2)

### 6.3 Pathways and ontology suggestions
* GO biological processes (suggested): **cell–cell adhesion (GO:0098609)**; **intermediate filament organization (GO:0045104)**; **cardiac muscle cell death (GO:0097285)**; **extracellular matrix organization (GO:0030198)**; **inflammatory response (GO:0006954)**; **NF‑κB signaling (GO:0043122)**.
* Cell types (CL suggestions): **cardiac muscle cell / cardiomyocyte (CL:0000746)**; **cardiac fibroblast (CL:0002548)**; **macrophage (CL:0000235)** (inflammatory infiltrates are emphasized in models and DSP cardiomyopathy). (bona2025dsps311aknockinmice pages 16-19, risato2024invivoapproaches pages 6-7)


## 7. Anatomical Structures Affected

### 7.1 Organ level
* **Heart** (primary): ventricular myocardium with fibrotic replacement and dysfunction; often with prominent LV involvement. (prompona2007magneticresonanceimaging pages 1-2)
* **Skin/hair** (primary): palmoplantar keratoderma and woolly hair. (arıcı2024acaseof pages 1-2)

### 7.2 Tissue and cell level (suggestions)
* UBERON suggestions: **heart (UBERON:0000948)**; **left ventricle (UBERON:0002084)**; **right ventricle (UBERON:0002083)**; **palm skin (UBERON:0001463)**; **sole of foot (UBERON:0001467)**; **hair follicle (UBERON:0002070)**.


## 8. Temporal Development

### 8.1 Onset
Within the cardiocutaneous (Naxos/Carvajal) spectrum:
* **Woolly hair**: present **from birth**. (prompona2007magneticresonanceimaging pages 1-2)
* **PPK**: develops in the **first year of life**. (prompona2007magneticresonanceimaging pages 1-2)
* **Cardiomyopathy**: clinically manifests **in childhood/adolescence**, with Carvajal tending to manifest earlier and with more heart-failure presentations. (prompona2007magneticresonanceimaging pages 1-2)

### 8.2 Progression and stages
Carvajal syndrome can follow a progressive course from early dermatologic signs to myocardial scarring, arrhythmias, and end-stage heart failure requiring transplant. Severe pediatric presentations can occur (e.g., LVEF 22% at age 7). (arıcı2024acaseof pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2)


## 9. Inheritance and Population

### 9.1 Inheritance pattern
Carvajal syndrome is primarily **autosomal recessive**, commonly reported in consanguineous families. (arıcı2024acaseof pages 1-2)

### 9.2 Epidemiology
Population prevalence/incidence were not identified in the retrieved Carvajal-specific sources.

However, outcome-related epidemiologic statements are reported in classic imaging literature:
* Carvajal syndrome can manifest with childhood dilated cardiomyopathy; one Circulation imaging report states that **~50% develop heart failure and most die during adolescence** (historical summary within that report). (prompona2007magneticresonanceimaging pages 1-2)

Founder effects and carrier frequencies were not extractable from the cited sources, except for the gnomAD frequency note above for one missense allele. (ziołkowska2024carvajalsyndromerelated pages 1-2)


## 10. Diagnostics

### 10.1 Clinical recognition
A key clinical diagnostic clue is that **hair + palmoplantar keratoderma** may precede cardiac symptoms; dermatologic recognition should trigger **cardiac evaluation** and **genetic testing**. (polivka2016combinationofpalmoplantar pages 1-2)

### 10.2 Cardiac testing (real-world implementation)
Commonly implemented diagnostics in reported cases include:
* **Echocardiography**: ventricular dilation, impaired systolic function (e.g., LVEF 22% in a 7‑year‑old). (arıcı2024acaseof pages 1-2)
* **24‑hour Holter monitoring**: ventricular ectopy/arrhythmias. (arıcı2024acaseof pages 1-2)
* **Cardiac MRI (CMR)**: myocardial fibrosis/late gadolinium enhancement; non-ischemic scarring; sometimes noncompaction-like trabeculation. (prompona2007magneticresonanceimaging pages 1-2, arıcı2024acaseof pages 1-2)

### 10.3 Genetic testing
* **DSP sequencing** (single gene or cardiomyopathy/arrhythmia panels using NGS) is used for confirmation; homozygous truncating variants and compound genotypes have been diagnosed by molecular genetic evaluation in multiple cases. (arıcı2024acaseof pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2)

### 10.4 Differential diagnosis
Clinical reports note overlap with other syndromes featuring cardiomyopathy and ectodermal findings (e.g., Naxos disease and other RASopathies), emphasizing the need for genotype-guided differentiation. (krishnamurthy2011arrhythmogenicdilatedcardiomyopathy pages 1-3)


## 11. Outcomes / Prognosis

Carvajal syndrome is associated with high morbidity from heart failure and arrhythmias and can lead to death in childhood/adolescence without timely advanced management.

Illustrative data:
* A pediatric case report (2024) documents death two years after diagnosis due to acute heart failure exacerbation after non-compliance. (arıcı2024acaseof pages 1-2)
* Historical summary within a Circulation MRI report describes frequent progression to heart failure and high adolescent mortality. (prompona2007magneticresonanceimaging pages 1-2)
* A modern (2024) vignette documents progression from initial childhood presentation to ICD, ablation, stroke, and eventual successful heart transplant at age 19. (ziołkowska2024carvajalsyndromerelated pages 1-2)

Prognostic biomarkers beyond imaging scar and arrhythmic history were not identified in the Carvajal-specific evidence set.


## 12. Treatment

### 12.1 Standard-of-care cardiology (real-world implementations)
Management follows advanced heart-failure and arrhythmia prevention principles:
* **Guideline-directed medical therapy for heart failure** is used in pediatric and adolescent cases (e.g., diuretics and neurohormonal blockade are described in case reports). (krishnamurthy2011arrhythmogenicdilatedcardiomyopathy pages 1-3, arıcı2024acaseof pages 1-2)
* **ICD implantation** is emphasized as the effective prevention for sudden cardiac death in severe arrhythmogenic disease, and is used in Carvajal/DSP cases. (arıcı2024acaseof pages 2-3, ziołkowska2024carvajalsyndromerelated pages 1-2)
* **Catheter ablation** may be used for refractory ventricular arrhythmias but is not considered reliably protective against sudden death by itself. (arıcı2024acaseof pages 2-3, ziołkowska2024carvajalsyndromerelated pages 1-2)
* **Heart transplantation** is pursued in end-stage disease and has been successful in multiple Carvajal reports. (prompona2007magneticresonanceimaging pages 1-2, ziołkowska2024carvajalsyndromerelated pages 1-2)

MAXO suggestions:
* **Implantation of cardioverter-defibrillator (MAXO:0000479)**
* **Heart transplantation (MAXO:0001193)**
* **Pharmacotherapy for heart failure (MAXO:0000745)**

### 12.2 Experimental / emerging approaches (2024)
Mechanism-driven therapeutic hypotheses are emerging from iPSC engineered tissue models:
* In DSP-reduced EHTs, **colchicine** and **NF‑κB inhibition** improved functional deficits, and **adenine base editing** correction reduced inflammatory biomarker release—supporting anti-inflammatory and gene-editing strategies as investigational directions for DSP-mediated inflammatory injury. (selgrade2024susceptibilitytoinnate pages 1-2)

### 12.3 Clinical trials
No Carvajal syndrome–specific interventional trials were identified in the retrieved ClinicalTrials.gov search results for this run.


## 13. Prevention

Primary prevention is not applicable because Carvajal syndrome is genetic; however:
* **Secondary/tertiary prevention** focuses on **early recognition** of hair/PPK signs, **cascade family screening**, longitudinal cardiac surveillance, and timely ICD/transplant evaluation. (polivka2016combinationofpalmoplantar pages 1-2, arıcı2024acaseof pages 2-3)


## 14. Other Species / Natural Disease
No naturally occurring Carvajal syndrome outside humans was identified in the retrieved veterinary literature in this run. Mouse spontaneous mutations in Dsp serve as disease models rather than natural disease in domestic species. (pratt2015dsprulaspontaneous pages 1-2)


## 15. Model Organisms and Experimental Models

### 15.1 Mouse models
**Dsp^rul (ruffled) spontaneous mouse model (2015)**
* A spontaneous autosomal recessive frameshift mutation in mouse **Dsp** truncates the C-terminus and produces a cardiocutaneous phenotype (abnormal hair coat, epidermal blistering, hair shaft defects, and age-dependent ventricular fibrosis with ECG defects). Authors state the phenotype closely models **Carvajal–Huerta syndrome**. (pratt2015dsprulaspontaneous pages 1-2, pratt2015dsprulaspontaneous pages 4-6, pratt2015dsprulaspontaneous pages 3-4)

### 15.2 Broader in vivo ACM/DSP modeling (review, 2024)
A 2024 review of arrhythmogenic cardiomyopathy animal models highlights multiple DSP perturbation strategies (conduction-system knockout, cardiomyocyte-restricted knockout, C-terminal mutant overexpression) producing desmosomal defects, inflammation, fibrosis/adiposis, and ventricular arrhythmias, and it explicitly notes the relevance of the **Dsp^rul** model for Carvajal–Huerta-like disease. (risato2024invivoapproaches pages 6-7)

### 15.3 Human iPSC engineered heart tissue models (2024)
A 2024 JCI study used patient-derived and gene-edited hiPSC cardiomyocytes to build engineered heart tissues demonstrating innate immune hypersensitivity and strain-dependent functional deficits with DSP reduction, providing a platform for testing anti-inflammatory interventions and gene editing. (selgrade2024susceptibilitytoinnate pages 1-2)


---

## Structured identifier/nomenclature summary

| Item | Value | Evidence (with citation id) | URL | Publication date |
|---|---|---|---|---|
| Disease overview | Rare cardiocutaneous disorder characterized by woolly hair, palmoplantar keratoderma, and cardiomyopathy; classically left-ventricular-predominant/dilated cardiomyopathy in the Carvajal form | Carvajal syndrome is described as a “very rare autosomal recessive cardiocutaneous disorder” with the triad of “woolly hair, epidermolytic palmoplantar keratoderma, and arrhythmogenic cardiomyopathy” (arıcı2024acaseof pages 1-2); Carvajal syndrome is also described as a syndrome with the “same cutaneous phenotype and predominantly left ventricular involvement” compared with Naxos disease (prompona2007magneticresonanceimaging pages 1-2) | https://doi.org/10.1017/s1047951124000222; https://doi.org/10.1161/circulationaha.107.704742 | 2024-03; 2007-11 |
| Preferred disease name | Carvajal syndrome | Multiple reports use “Carvajal syndrome” as the primary disease name (arıcı2024acaseof pages 1-2, krishnamurthy2011arrhythmogenicdilatedcardiomyopathy pages 1-3, ziołkowska2024carvajalsyndromerelated pages 1-2) | https://doi.org/10.1017/s1047951124000222; https://doi.org/10.1007/s12098-010-0319-3; https://doi.org/10.33963/v.phj.101664 | 2024-03; 2011-07; 2024-09 |
| Common synonym | Carvajal-Huerta syndrome | A spontaneous mouse model paper states the phenotype closely models the rare human disorder “Carvajal-Huerta syndrome” (supported in search results); a 2025 case report uses “Carvajal–Huerta” for the same disorder (tosun2025noncompactionanddilated pages 1-2) | https://doi.org/10.1016/j.yexmp.2015.01.015; https://doi.org/10.1017/S1047951125001532 | 2015-04; 2025-04 |
| Related nomenclature | Naxos disease variant / Naxos-Carvajal phenotype (historical/overlap terminology) | Carvajal syndrome is presented as a variant of Naxos disease with similar cutaneous findings but predominantly left-ventricular disease (prompona2007magneticresonanceimaging pages 1-2); overlapping “Naxos-Carvajal” terminology has been used for mixed cardiocutaneous phenotypes (polivka2016combinationofpalmoplantar pages 1-2) | https://doi.org/10.1161/circulationaha.107.704742; https://doi.org/10.1136/jmedgenet-2015-103403 | 2007-11; 2016-09 |
| OMIM identifier | OMIM 605676 | Review/case literature explicitly cites “Carvajal syndrome (OMIM 605676)” (pantou2023atruncatingvariant pages 1-2) | https://doi.org/10.15829/1560-4071-2018-10-151-158 | 2018-11 |
| Inheritance | Usually autosomal recessive; rare autosomal dominant presentations have been reported | 2024 case report: “very rare autosomal recessive cardiocutaneous disorder” (arıcı2024acaseof pages 1-2); companion excerpt notes the condition is “primarily an autosomal recessive hereditary disease, though rare autosomal dominant forms have been reported” (arıcı2024acaseof pages 2-3) | https://doi.org/10.1017/s1047951124000222 | 2024-03 |
| Primary causal gene | DSP (desmoplakin) | Homozygous/compound DSP variants are repeatedly reported as causal in Carvajal syndrome (arıcı2024acaseof pages 1-2, krishnamurthy2011arrhythmogenicdilatedcardiomyopathy pages 1-3, ziołkowska2024carvajalsyndromerelated pages 1-2) | https://doi.org/10.1017/s1047951124000222; https://doi.org/10.1007/s12098-010-0319-3; https://doi.org/10.33963/v.phj.101664 | 2024-03; 2011-07; 2024-09 |
| Gene/protein function relevant to nomenclature | DSP encodes desmoplakin, a desmosomal protein that anchors intermediate filaments to desmosomes | DSP’s “main function is the anchoring of intermediate filaments to desmosomes” (pantou2023atruncatingvariant pages 1-2); defective desmosomal proteins lead to myocyte dissociation/death and fibrofatty/fibrotic myocardial change (arıcı2024acaseof pages 2-3) | https://doi.org/10.1186/s12920-023-01527-6; https://doi.org/10.1017/s1047951124000222 | 2023-05; 2024-03 |
| Key distinguishing clinical nomenclature point vs Naxos disease | Carvajal syndrome is associated more often with left ventricular/biventricular cardiomyopathy, whereas Naxos disease is classically right-ventricular | Circulation MRI paper distinguishes Carvajal by “predominantly left ventricular involvement” (prompona2007magneticresonanceimaging pages 1-2); review systematic data support the Carvajal phenotype as part of DSP-related cardiocutaneous disease (polivka2016combinationofpalmoplantar pages 1-2) | https://doi.org/10.1161/circulationaha.107.704742; https://doi.org/10.1136/jmedgenet-2015-103403 | 2007-11; 2016-09 |
| Key recent citations | 2023-2024 literature continues to define Carvajal syndrome within the broader DSP cardiomyopathy spectrum | Recent reports/reviews include Brandão et al. 2023 on desmoplakin cardiomyopathy (brandao2023desmoplakincardiomyopathycomprehensive pages 2-4), Arıcı et al. 2024 case report (arıcı2024acaseof pages 1-2), and Ziółkowska et al. 2024 case report (ziołkowska2024carvajalsyndromerelated pages 1-2) | https://doi.org/10.3390/jcm12072660; https://doi.org/10.1017/s1047951124000222; https://doi.org/10.33963/v.phj.101664 | 2023-04; 2024-03; 2024-09 |


*Table: This table summarizes the core nomenclature and identifier-related facts for Carvajal syndrome/Carvajal-Huerta syndrome, including the disease concept, inheritance, causal gene, and historical naming context. It is useful as a compact reference for disease knowledge base normalization and synonym mapping.*


## Direct abstract quotes supporting key statements (selected)

* Systematic review (desmosomal diseases; clinical red flags): “The combination of PPK and hair shaft anomalies was recorded in 161 patients, and this association is at high risk of cardiac disease (129/161, 80.1%). Skin features had led to cardiac monitoring in only 2.3% of those patients.” (polivka2016combinationofpalmoplantar pages 1-2)
* 2024 mechanistic advance (genetically mediated myocarditis model): “Genetic reduction of DSP renders cardiomyocytes susceptible to innate immune activation and strain-dependent contractile deficits.” (selgrade2024susceptibilitytoinnate pages 1-2)


## Notes on evidence gaps
* MONDO/Orphanet/MeSH/ICD codes and population prevalence/incidence could not be asserted from the retrieved evidence set.
* Phenotype frequencies specific to Carvajal syndrome (as distinct from broader DSP cardiomyopathy or desmosomal disease) remain sparse in the case-report-dominated literature.


References

1. (arıcı2024acaseof pages 1-2): Sule Arıcı, Figen Akalın, and Bilgen Bilge Geckinli. A case of carvajal syndrome presenting with dilated cardiomyopathy. Cardiology in the young, 34:1-3, Mar 2024. URL: https://doi.org/10.1017/s1047951124000222, doi:10.1017/s1047951124000222. This article has 0 citations and is from a peer-reviewed journal.

2. (prompona2007magneticresonanceimaging pages 1-2): Maria Prompona, Rainer Kozlik-Feldmann, Josef Mueller-Hoecker, Maximilian Reiser, and Armin Huber. Magnetic resonance imaging characteristics in carvajal syndrome (variant of naxos disease). Circulation, Nov 2007. URL: https://doi.org/10.1161/circulationaha.107.704742, doi:10.1161/circulationaha.107.704742. This article has 18 citations and is from a highest quality peer-reviewed journal.

3. (pantou2023atruncatingvariant pages 1-2): Malena P. Pantou, Polyxeni Gourzi, Vasiliki Vlagkouli, Efstathios Papatheodorou, Alexandros Tsoutsinos, Eva Nyktari, Dimitrios Degiannis, and Aris Anastasakis. A truncating variant altering the extreme c-terminal region of desmoplakin (dsp) suggests the crucial functional role of the region: a case report study. BMC Medical Genomics, May 2023. URL: https://doi.org/10.1186/s12920-023-01527-6, doi:10.1186/s12920-023-01527-6. This article has 4 citations and is from a peer-reviewed journal.

4. (tosun2025noncompactionanddilated pages 1-2): Demet Tosun, Nihal Akçay, İlyas Bingöl, and Damla Gökçeer Akbulut. Noncompaction and dilated cardiomyopathy in carvajal syndrome. Cardiology in the Young, 35:1073-1075, Apr 2025. URL: https://doi.org/10.1017/s1047951125001532, doi:10.1017/s1047951125001532. This article has 0 citations and is from a peer-reviewed journal.

5. (polivka2016combinationofpalmoplantar pages 1-2): Laura Polivka, Christine Bodemer, and Smail Hadj-Rabia. Combination of palmoplantar keratoderma and hair shaft anomalies, the warning signal of severe arrhythmogenic cardiomyopathy: a systematic review on genetic desmosomal diseases. Journal of Medical Genetics, 53:289-295, Sep 2016. URL: https://doi.org/10.1136/jmedgenet-2015-103403, doi:10.1136/jmedgenet-2015-103403. This article has 45 citations and is from a domain leading peer-reviewed journal.

6. (pratt2015dsprulaspontaneous pages 1-2): C. Herbert Pratt, Christopher S. Potter, Heather Fairfield, Laura G. Reinholdt, David E. Bergstrom, Belinda S. Harris, Ian Greenstein, Soheil S. Dadras, Bruce T. Liang, Paul N. Schofield, and John P. Sundberg. Dsprul: a spontaneous mouse mutation in desmoplakin as a model of carvajal-huerta syndrome. Experimental and Molecular Pathology, 98:164-172, Apr 2015. URL: https://doi.org/10.1016/j.yexmp.2015.01.015, doi:10.1016/j.yexmp.2015.01.015. This article has 17 citations and is from a peer-reviewed journal.

7. (selgrade2024susceptibilitytoinnate pages 1-2): Daniel F. Selgrade, Dominic E. Fullenkamp, Ivana A. Chychula, Binjie Li, Lisa Dellefave-Castillo, Adi D. Dubash, Joyce Ohiri, Tanner O. Monroe, Malorie Blancard, Garima Tomar, Cory Holgren, Paul W. Burridge, Alfred L. George, Alexis R. Demonbreun, Megan J. Puckelwartz, Sharon A. George, Igor R. Efimov, Kathleen J. Green, and Elizabeth M. McNally. Susceptibility to innate immune activation in genetically mediated myocarditis. The Journal of Clinical Investigation, May 2024. URL: https://doi.org/10.1172/jci180254, doi:10.1172/jci180254. This article has 27 citations.

8. (krishnamurthy2011arrhythmogenicdilatedcardiomyopathy pages 1-3): Sriram Krishnamurthy, B. Adhisivam, Robert M. Hamilton, Berivan Baskin, Niranjan Biswal, and Manish Kumar. Arrhythmogenic dilated cardiomyopathy due to a novel mutation in the desmoplakin gene. The Indian Journal of Pediatrics, 78:866-869, Jul 2011. URL: https://doi.org/10.1007/s12098-010-0319-3, doi:10.1007/s12098-010-0319-3. This article has 20 citations.

9. (ziołkowska2024carvajalsyndromerelated pages 1-2): Lidia Ziółkowska, Dorota Piekutowska-Abramczuk, Karolina Borowiec, Elżbieta Ciara, Maciej Sterliński, and Elżbieta Katarzyna Biernacka. Carvajal syndrome related to two distinct molecular variants in desmoplakin gene. Polish Heart Journal, 82:914-915, Sep 2024. URL: https://doi.org/10.33963/v.phj.101664, doi:10.33963/v.phj.101664. This article has 1 citations.

10. (arıcı2024acaseof pages 2-3): Sule Arıcı, Figen Akalın, and Bilgen Bilge Geckinli. A case of carvajal syndrome presenting with dilated cardiomyopathy. Cardiology in the young, 34:1-3, Mar 2024. URL: https://doi.org/10.1017/s1047951124000222, doi:10.1017/s1047951124000222. This article has 0 citations and is from a peer-reviewed journal.

11. (bona2025dsps311aknockinmice pages 13-16): Anna Di Bona, Anna Guazzo, Induja Perumal Vanaja, Riccardo Bariani, Maria C. Disalvo, Mattia Albiero, Nicolas Kuperwasser, Pierre David, Rudy Celeghin, Vittoria Di Mauro, Arianna Scalco, María López-Moreno, Monica De Gaspari, Mila Della Barbera, Stefania Rizzo, Domenico Corrado, Barbara Bauce, Giuseppe Zanotti, Gaetano Thiene, Kalliopi Pilichou, José Maria Perez Pomares, Mario Pende, Cristina Basso, Marco Mongillo, and Tania Zaglia. Dsps311a knock-in mice replicate the clinical-pathological features of dominant and recessive forms of desmoplakin-related cardiomyopathies. MedRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.14.24319713, doi:10.1101/2025.01.14.24319713. This article has 0 citations.

12. (brandao2023desmoplakincardiomyopathycomprehensive pages 2-4): Mariana Brandão, Riccardo Bariani, Ilaria Rigato, and Barbara Bauce. Desmoplakin cardiomyopathy: comprehensive review of an increasingly recognized entity. Journal of Clinical Medicine, 12:2660, Apr 2023. URL: https://doi.org/10.3390/jcm12072660, doi:10.3390/jcm12072660. This article has 54 citations.

13. (bona2025dsps311aknockinmice pages 16-19): Anna Di Bona, Anna Guazzo, Induja Perumal Vanaja, Riccardo Bariani, Maria C. Disalvo, Mattia Albiero, Nicolas Kuperwasser, Pierre David, Rudy Celeghin, Vittoria Di Mauro, Arianna Scalco, María López-Moreno, Monica De Gaspari, Mila Della Barbera, Stefania Rizzo, Domenico Corrado, Barbara Bauce, Giuseppe Zanotti, Gaetano Thiene, Kalliopi Pilichou, José Maria Perez Pomares, Mario Pende, Cristina Basso, Marco Mongillo, and Tania Zaglia. Dsps311a knock-in mice replicate the clinical-pathological features of dominant and recessive forms of desmoplakin-related cardiomyopathies. MedRxiv, Jan 2025. URL: https://doi.org/10.1101/2025.01.14.24319713, doi:10.1101/2025.01.14.24319713. This article has 0 citations.

14. (risato2024invivoapproaches pages 6-7): Giovanni Risato, Raquel Brañas Casas, Marco Cason, Maria Bueno Marinas, Serena Pinci, Monica De Gaspari, Silvia Visentin, Stefania Rizzo, Gaetano Thiene, Cristina Basso, Kalliopi Pilichou, Natascia Tiso, and Rudy Celeghin. In vivo approaches to understand arrhythmogenic cardiomyopathy: perspectives on animal models. Cells, Jul 2024. URL: https://doi.org/10.3390/cells13151264, doi:10.3390/cells13151264. This article has 3 citations.

15. (pratt2015dsprulaspontaneous pages 4-6): C. Herbert Pratt, Christopher S. Potter, Heather Fairfield, Laura G. Reinholdt, David E. Bergstrom, Belinda S. Harris, Ian Greenstein, Soheil S. Dadras, Bruce T. Liang, Paul N. Schofield, and John P. Sundberg. Dsprul: a spontaneous mouse mutation in desmoplakin as a model of carvajal-huerta syndrome. Experimental and Molecular Pathology, 98:164-172, Apr 2015. URL: https://doi.org/10.1016/j.yexmp.2015.01.015, doi:10.1016/j.yexmp.2015.01.015. This article has 17 citations and is from a peer-reviewed journal.

16. (pratt2015dsprulaspontaneous pages 3-4): C. Herbert Pratt, Christopher S. Potter, Heather Fairfield, Laura G. Reinholdt, David E. Bergstrom, Belinda S. Harris, Ian Greenstein, Soheil S. Dadras, Bruce T. Liang, Paul N. Schofield, and John P. Sundberg. Dsprul: a spontaneous mouse mutation in desmoplakin as a model of carvajal-huerta syndrome. Experimental and Molecular Pathology, 98:164-172, Apr 2015. URL: https://doi.org/10.1016/j.yexmp.2015.01.015, doi:10.1016/j.yexmp.2015.01.015. This article has 17 citations and is from a peer-reviewed journal.

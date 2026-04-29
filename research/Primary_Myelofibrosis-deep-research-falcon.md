---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T21:53:47.908780'
end_time: '2026-04-05T22:00:13.125717'
duration_seconds: 385.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Myelofibrosis
  mondo_id: ''
  category: ''
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
- **Disease Name:** Primary Myelofibrosis
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Primary Myelofibrosis** covering all of the
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
- **Disease Name:** Primary Myelofibrosis
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Primary Myelofibrosis** covering all of the
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


# Primary Myelofibrosis (PMF): Disease Characteristics Research Report

## Target Disease
- **Disease name:** Primary myelofibrosis (PMF)  
- **Category:** Philadelphia chromosome–negative (BCR::ABL1-negative) *myeloproliferative neoplasm (MPN)* (martino2024treatmentstrategiesused pages 1-2, wang2025currentadvancesin pages 5-7)
- **MONDO ID:** Not reliably retrievable from the currently gathered evidence set (see “Identifiers” below). The MONDO ontology framework and identifier conventions are described in a general MONDO paper, but it does not provide a PMF-specific code in the retrieved text (vasilevsky2022; https://doi.org/10.1101/2022.04.13.22273750) (martino2024treatmentstrategiesused pages 2-4).

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Primary myelofibrosis is a clonal hematopoietic stem/progenitor cell neoplasm characterized by atypical megakaryocytic (and granulocytic) proliferation, progressive bone marrow (BM) fibrosis, and extramedullary hematopoiesis (EMH), which collectively drive cytopenias, splenomegaly, constitutional symptoms, and risk of leukemic transformation (martino2024treatmentstrategiesused pages 1-2, wang2025currentadvancesin pages 5-7). A recent pathologic review describes PMF as a Ph-negative MPN featuring “clonal proliferation of atypical megakaryocytes and myeloid cells, fibrosis of the bone marrow, extramedullary hematopoiesis, and increased risk of leukemic transformation to acute myeloid leukemia (AML)” (abstract) (https://doi.org/10.3390/cancers18010050; 2025-12) (shao2025areviewof pages 4-6).

PMF includes a **prefibrotic/early PMF** stage (hypercellular marrow with minimal fibrosis) and **overt/fibrotic-stage PMF** with advanced fibrosis and leukoerythroblastosis (wang2025currentadvancesin pages 4-5, wang2025currentadvancesin pages 5-7).

### 1.2 Key identifiers and classifications
Because the current tool runs retrieved mostly primary literature and guideline-style reviews, ontology/administrative identifiers (ICD-10/ICD-11, MeSH, OMIM, Orphanet, MONDO) are **not fully populated** from the evidence captured here.

What can be stated from evidence:
- **Classification systems used clinically:** WHO and ICC frameworks (WHO 5th edition/WHO-HAEM5; ICC 2022) are explicitly referenced in multiple sources for PMF/pre-PMF diagnosis and classification (https://doi.org/10.1007/s00277-025-06191-7; 2025-01) (wang2025currentadvancesin pages 5-7), and are discussed as contemporaneous classification systems (https://doi.org/10.1186/s13045-024-01571-4; 2024-07) (stuckey2025myelofibrosistreatmentoptions pages 8-10).

### 1.3 Common synonyms / alternative names
- Primary myelofibrosis
- PMF
- “Overt PMF” (fibrotic stage) vs “prefibrotic PMF (pre-PMF)” (wang2025currentadvancesin pages 5-7, mora2024prognosticandpredictive pages 1-2)

### 1.4 Evidence provenance: individual vs aggregated resources
- Many statements in this report derive from **aggregated disease-level resources** (reviews/guidelines) (martino2024treatmentstrategiesused pages 1-2, mora2024prognosticandpredictive pages 1-2, mclornan2023diagnosisandevaluation pages 6-6).
- Real-world analyses explicitly use aggregated patient-level EHR/claims repositories (TriNetX; US payer claims). TriNetX analysis notes the database “includes more than 64,000 myelofibrosis patients” (https://doi.org/10.3390/cancers16071416; 2024-04) (martino2024treatmentstrategiesused pages 1-2). US claims analysis included “2830 patients with an MF diagnosis” and 1191 eligible for utilization/cost analysis (https://doi.org/10.1093/oncolo/oyab058; 2022-02) (martino2024treatmentstrategiesused pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors (genetic/mechanistic)
PMF is driven by constitutive activation of the JAK–STAT signaling axis, typically via somatic **driver mutations** in **JAK2**, **CALR**, or **MPL** (chifotides2023associationofmyelofibrosis pages 2-4, wang2025currentadvancesin pages 5-7). A 2022 ASH Education review states MF is “universally driven by Jak/STAT pathway activation” (https://doi.org/10.1182/hematology.2022000340; 2022-12) (reynolds2022newapproachesto pages 1-3).

### 2.2 Risk factors
#### Genetic risk factors
- **Driver mutations and approximate frequencies (PMF):**  
  A 2023 phenotype-focused review reports PMF driver frequencies of ~60% **JAK2 V617F**, ~25–30% **CALR exon 9**, and ~5–10% **MPL** (W515L/K) (https://doi.org/10.3390/cancers15133331; 2023-06) (chifotides2023associationofmyelofibrosis pages 2-4).  
  A 2024 prognostic review provides another commonly cited distribution: “Two-thirds of patients with PMF harbor JAK2V617F, 25% CALR, and 10% each MPL or no driver mutation (‘triple negative’ status, TN)” (abstract) (https://doi.org/10.1007/s11899-024-00739-6; 2024-08) (mora2024prognosticandpredictive pages 1-2).
- **High molecular risk (HMR) mutations:** HMR mutations commonly include **ASXL1, EZH2, IDH1, IDH2, SRSF2** and **U2AF1 Q157** (chifotides2023associationofmyelofibrosis pages 2-4, mclornan2023diagnosisandevaluation pages 6-6). The 2024 prognostic review defines HMR as “ASXL1, SRSF2, EZH2, and IDH1/IDH2” and links them to worse OS/blast-phase risk (mora2024prognosticandpredictive pages 1-2).

#### Environmental/host risk factors
Specific exogenous environmental causes (toxins, infections, etc.) were **not identified** in the retrieved evidence snippets. Host factors associated with outcomes/complications in real-world datasets include age and blood count abnormalities (martino2024treatmentstrategiesused pages 1-2, reynolds2022newapproachesto pages 1-3).

### 2.3 Protective factors
No specific genetic or environmental protective factors were captured in the current evidence set.

### 2.4 Gene–environment interactions
No PMF-specific gene–environment interaction evidence was captured in the current evidence set.

---

## 3. Phenotypes

### 3.1 Core clinical manifestations and laboratory abnormalities
PMF exhibits heterogeneous presentation; ~25–33% can be asymptomatic initially (shao2025areviewof pages 4-6). Common manifestations include:
- **Splenomegaly** (often marked), due to EMH (shao2025areviewof pages 4-6, wang2025currentadvancesin pages 5-7)
- **Anemia** and progressive cytopenias (shao2025areviewof pages 4-6, wang2025currentadvancesin pages 5-7)
- **Leukoerythroblastosis** and teardrop RBCs (peripheral smear) (shao2025areviewof pages 4-6)
- **Constitutional symptoms** (fever, weight loss, night sweats) and cachexia (wang2025currentadvancesin pages 5-7)
- **Thrombosis/bleeding:** a pathology review reports “Thromboembolic events occur in ~10–20% of patients” (https://doi.org/10.3390/cancers18010050; 2025-12) (shao2025areviewof pages 4-6).

### 3.2 Phenotype subtypes (proliferative vs cytopenic)
Two clinically meaningful ends of a spectrum are highlighted:
- **Myeloproliferative phenotype:** larger spleens, leukocytosis, normal/higher counts or mild anemia; fewer non-driver mutations and higher JAK2 allele burden; generally better response to ruxolitinib (chifotides2023associationofmyelofibrosis pages 2-4).
- **Myelodepletive/cytopenic phenotype:** ≥2 cytopenias, transfusion dependence, modest splenomegaly; more HMR mutations and genomic complexity; inferior outcomes; emphasizes less myelosuppressive JAK inhibitors (momelotinib/pacritinib) (chifotides2023associationofmyelofibrosis pages 2-4, reynolds2022newapproachesto pages 1-3).

### 3.3 Phenotype characteristics (age of onset, progression, frequency)
- **Typical onset:** older adults; median age around the 7th decade (mora2024prognosticandpredictive pages 1-2). One review reports median age at diagnosis ~65 (martino2024treatmentstrategiesused pages 1-2).
- **Progression:** prefibrotic → overt fibrotic stage with worsening cytopenias and EMH; risk of accelerated/blast phase exists (wang2025currentadvancesin pages 4-5, wang2025currentadvancesin pages 5-7).

### 3.4 Quality-of-life impact
Quality of life is impacted by anemia, constitutional symptoms, and splenomegaly; treatment goals emphasize symptom and spleen improvement (martino2024treatmentstrategiesused pages 1-2, wang2025currentadvancesin pages 5-7).

### 3.5 Suggested HPO terms (examples)
- Splenomegaly **HP:0001744**
- Anemia **HP:0001903**
- Thrombocytopenia **HP:0001873**
- Leukocytosis **HP:0001974**
- Leukoerythroblastosis **HP:0032465** (term exists in HPO; verify exact ID in implementation)
- Constitutional symptoms: Fever **HP:0001945**, Weight loss **HP:0001824**, Night sweats **HP:0030166**, Fatigue **HP:0012378**
- Bone marrow fibrosis **HP:0010984** (term exists; verify in implementation)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes (somatic driver genes)
- **JAK2**, **CALR**, **MPL** are canonical driver genes activating JAK–STAT signaling in PMF (chifotides2023associationofmyelofibrosis pages 2-4, wang2025currentadvancesin pages 5-7).

### 4.2 Pathogenic variants (typical PMF)
- **JAK2 p.V617F** (somatic), and **MPL W515** variants (e.g., W515L/K), and **CALR exon 9** frameshift variants are repeatedly referenced as drivers (chifotides2023associationofmyelofibrosis pages 2-4, mora2024prognosticandpredictive pages 1-2).

### 4.3 Modifier/cooperating mutations and prognostic genomics
- **Non-driver myeloid gene variants** are common: “About 80% of PMF … cases carry [myeloid gene variants]” (https://doi.org/10.1007/s11899-024-00739-6; 2024-08) (mora2024prognosticandpredictive pages 1-2).
- Frequently discussed genes include epigenetic regulators and splicing factors (DNMT3A, TET2, ASXL1, SRSF2, U2AF1, EZH2, IDH1/2, TP53) (mora2024prognosticandpredictive pages 1-2).

### 4.4 Epigenetic information
The current evidence set supports that epigenetic regulators (e.g., ASXL1, DNMT3A, EZH2, TET2) are common co-mutations and carry prognostic relevance, but does not provide direct disease-specific methylation/histone profiling datasets (mora2024prognosticandpredictive pages 1-2).

### 4.5 Chromosomal abnormalities
A pathology review notes karyotypic abnormalities in up to ~45% of cases; common abnormalities include del(20q), del(13q), +8, +9 (shao2025areviewof pages 4-6). Another review gives a similar range (~30–50%) and lists del(13q), del(20q), +8, +9, del(12p), trisomy 1q (ozygała2024biologicalmarkersof pages 10-12).

---

## 5. Environmental Information

- **Environmental factors / lifestyle / infectious agents:** Not specifically identified in the retrieved evidence snippets for PMF etiology. PMF is primarily characterized in the retrieved literature as a clonal neoplasm with somatic driver mutations and inflammatory/fibrotic microenvironment changes (shao2025areviewof pages 4-6, chifotides2023associationofmyelofibrosis pages 2-4).

---

## 6. Mechanism / Pathophysiology

### 6.1 Core causal chain (integrated)
1) **Somatic driver mutation** (JAK2/CALR/MPL) in hematopoietic stem/progenitor cells → **constitutive JAK–STAT signaling** (chifotides2023associationofmyelofibrosis pages 2-4, reynolds2022newapproachesto pages 1-3).  
2) Expansion/dysregulation of myeloid lineages with **atypical megakaryocytes** → secretion of pro-inflammatory/pro-fibrotic mediators (IL-1β, TGF-β; PDGF, VEGF, b-FGF) (wang2025currentadvancesin pages 5-7).  
3) **Bone marrow microenvironment remodeling** and activation of stromal programs → progressive **reticulin/collagen fibrosis** and ineffective hematopoiesis (martino2024treatmentstrategiesused pages 1-2, wang2025currentadvancesin pages 5-7).  
4) BM failure drives **EMH** in spleen/liver and systemic symptoms (shao2025areviewof pages 4-6, wang2025currentadvancesin pages 5-7).

### 6.2 Fibrosis biology and cell types
A pathology review states fibrosis is driven by profibrotic cytokines including “TGF-β, PDGF, VEGF” and implicates Gli1+ and Lepr+ mesenchymal stem cell populations in fibrotic remodeling, alongside pathways such as BMP/Wnt (shao2025areviewof pages 4-6).

### 6.3 Anemia biology and hepcidin/ACVR1 axis (therapeutically actionable)
Anemia is a hallmark and negative prognostic factor (mora2024prognosticandpredictive pages 1-2, reynolds2022newapproachesto pages 1-3). ACVR1 (ALK2) inhibition is used therapeutically to suppress hepcidin signaling and improve iron-restricted anemia; momelotinib is a JAK1/2 and ACVR1 inhibitor whose “dual inhibition mechanism addresses anemia by suppressing hepcidin production” (review abstract) (https://doi.org/10.3389/fonc.2024.1411972; 2024-06) (chifotides2023associationofmyelofibrosis pages 2-4).

### 6.4 Suggested ontology terms
**GO Biological Process (examples):**
- “JAK-STAT cascade” (GO term; verify exact ID in implementation)
- “Cytokine-mediated signaling pathway”
- “Extracellular matrix organization”
- “Collagen fibril organization”
- “Hepcidin metabolic process”
- “Inflammatory response”

**Cell Ontology (CL) (examples):**
- Megakaryocyte (CL:0000554)
- Hematopoietic stem cell (CL:0000037)
- Mesenchymal stromal cell / mesenchymal stem cell (term exists; verify exact CL ID)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue targets
- **Primary:** bone marrow (site of clonal proliferation and fibrosis) (martino2024treatmentstrategiesused pages 1-2, wang2025currentadvancesin pages 5-7)
- **Secondary:** spleen and liver (EMH causing hepatosplenomegaly) (shao2025areviewof pages 4-6, wang2025currentadvancesin pages 5-7)

### 7.2 Suggested anatomy ontology (UBERON examples)
- Bone marrow **UBERON:0002371**
- Spleen **UBERON:0002106**
- Liver **UBERON:0002107**

---

## 8. Temporal Development

### 8.1 Onset
- Typically **adult/older adult onset** (median onset in 7th decade) (mora2024prognosticandpredictive pages 1-2).

### 8.2 Progression patterns
- **Prefibrotic PMF → overt PMF** (fibrotic stage) is a recognized evolution in WHO/ICC conceptualization (wang2025currentadvancesin pages 4-5, wang2025currentadvancesin pages 5-7).
- **Accelerated phase** (10–19% blasts) and **blast phase** (≥20% blasts) define progression to high-grade disease; blast-phase MPN incidence estimates include 9–13% for PMF in a contemporary review (https://doi.org/10.1038/s41408-023-00878-8; 2023-07) (wang2025currentadvancesin pages 4-5).

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- **Incidence:**
  - A 2024 review reports annual incidence range **0.22–0.99 per 100,000** (with regional examples North America 0.33–0.46; Europe 0.1–1) and male predominance (martino2024treatmentstrategiesused pages 1-2).
  - A 2024 prognostic review gives a US incidence estimate of **0.44 per 100,000 per year** (mora2024prognosticandpredictive pages 1-2).
- **Age/sex:** median diagnosis around 65 and onset commonly in 7th decade; incidence higher in men than women in one review (martino2024treatmentstrategiesused pages 1-2, mora2024prognosticandpredictive pages 1-2).

### 9.2 Inheritance
PMF is principally a **somatic** clonal neoplasm in the retrieved evidence set; germline Mendelian inheritance patterns are not emphasized in these sources.

---

## 10. Diagnostics

### 10.1 Diagnostic criteria (WHO/ICC-aligned) and key concepts
Multiple sources converge on a **major + minor** criteria framework:
- A 2023 British Society for Haematology guideline states: “Diagnosis requires all three major criteria and at least one minor criterion confirmed in two consecutive determinations.” (https://doi.org/10.1111/bjh.19164; 2023-11) (mclornan2023diagnosisandevaluation pages 6-6).
- A 2024 review similarly summarizes diagnostic structure and provides a detailed minor-criteria list (anemia not due to comorbidity, leukocytosis ≥11×10^9/L, palpable splenomegaly, elevated LDH, leukoerythroblastosis) (martino2024treatmentstrategiesused pages 2-4).

Core diagnostic elements supported by evidence:
- **Bone marrow morphology**: megakaryocytic proliferation/atypia and grading of fibrosis (pre-PMF ≤MF-1; overt PMF MF-2/3) (shao2025areviewof pages 4-6, wang2025currentadvancesin pages 5-7).
- **Clonality evidence**: JAK2/CALR/MPL driver mutation or other clonal marker (martino2024treatmentstrategiesused pages 2-4, mclornan2023diagnosisandevaluation pages 6-6).
- **Exclusion of other myeloid neoplasms** (including BCR::ABL1-positive CML) (martino2024treatmentstrategiesused pages 2-4, wang2025currentadvancesin pages 5-7).

### 10.2 Testing modalities
- Driver mutation detection and broader NGS panels are integral; ICC-oriented review emphasizes sensitive techniques and notes “high sensitive single target (RT-qPCR, ddPCR) or multi-target next-generation sequencing assays with a minimal sensitivity of VAF 1% are now important for a proper diagnostic identification of MPN cases with low allelic frequencies at initial presentation” (https://doi.org/10.1007/s00428-022-03480-8; 2023-12) (wang2025currentadvancesin pages 5-7).

### 10.3 Differential diagnosis (high level)
- Essential thrombocythemia (ET), polycythemia vera (PV), secondary myelofibrosis (post-PV/post-ET), and other myeloid neoplasms must be excluded; this is explicitly embedded in major criteria summaries (martino2024treatmentstrategiesused pages 2-4, wang2025currentadvancesin pages 5-7).

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality (risk-stratified)
Prognosis is heterogeneous and is commonly modeled using clinical, cytogenetic, and molecular risk systems.
- A 2024 prognostic review provides median OS estimates by MF subtype: “Median overall survival (OS) of pre-PMF, overt-PMF and SMF patients is around 14 years, seven and nine years, respectively.” (abstract) (https://doi.org/10.1007/s11899-024-00739-6; 2024-08) (mora2024prognosticandpredictive pages 1-2).
- Risk scores (IPSS/DIPSS/DIPSS-plus) span median OS approximately from **~11.3 years (low risk) to ~2.3 years (high risk)** in one review summary (mora2024prognosticandpredictive pages 1-2). Another review provides representative medians by IPSS and DIPSS-plus categories (martino2024treatmentstrategiesused pages 2-4).

### 11.2 Prognostic factors
Common adverse features include older age, leukocytosis, anemia, thrombocytopenia, circulating blasts, constitutional symptoms, unfavorable karyotype, and HMR mutations (martino2024treatmentstrategiesused pages 2-4, mora2024prognosticandpredictive pages 1-2).

### 11.3 Prognostic models used clinically
- **IPSS** (at diagnosis), **DIPSS** (dynamic), **DIPSS-plus** (adds transfusion dependence, platelet count, karyotype), and molecularly informed models **MIPSS70+ v2.0** and **GIPSS** are described across sources (martino2024treatmentstrategiesused pages 2-4, mora2024prognosticandpredictive pages 1-2, mclornan2023diagnosisandevaluation pages 6-6).
- BSH highlights MIPSS70+ v2.0 integration of karyotype and mutations including U2AF1 Q157 and notes it is “more accurate than IPSS” in its derivation cohort (mclornan2023diagnosisandevaluation pages 6-6).

---

## 12. Treatment

### 12.1 Treatment goals and real-world implementation
Goals emphasize symptom control and spleen volume reduction; transplantation is reserved for selected higher-risk patients (martino2024treatmentstrategiesused pages 1-2, martino2024treatmentstrategiesused pages 2-4). A 2024 review states: “Current drug therapy for myelofibrosis does not alter the natural course of the disease or prolong survival, and allogeneic stem cell transplantation is the only curative treatment modality.” (abstract) (https://doi.org/10.3390/hematolrep16040067; 2024-10) (martino2024treatmentstrategiesused pages 1-2).

### 12.2 Pharmacotherapy (JAK inhibitors and anemia-directed strategies)

#### Ruxolitinib (JAK1/2 inhibitor)
- Standard-of-care for intermediate/high-risk MF for spleen and symptom benefit (martino2024treatmentstrategiesused pages 1-2, stuckey2025myelofibrosistreatmentoptions pages 8-10).
- Real-world discontinuation is common: a 2023 Italian real-world analysis states in its abstract, “50% to 70% of patients discontinue ruxolitinib within 3 to 5 years” (https://doi.org/10.3390/cancers15205027; 2023-10) (wang2025currentadvancesin pages 5-7).

#### Momelotinib (JAK1/2 + ACVR1/ALK2 inhibitor; anemia benefit; FDA approval 2023-09-15)
- A 2024 expert commentary notes momelotinib was “recently approved (September 15, 2023) for use in anemic patients with high/intermediate risk myelofibrosis (MF), including primary (PMF)” (https://doi.org/10.1038/s41408-024-01029-3; 2024-03) (chifotides2023associationofmyelofibrosis pages 2-4).
- **SIMPLIFY-2 subgroup analysis (JAK inhibitor-experienced, anemia focus):** week-24 transfusion independence (TI) was higher with momelotinib vs best available therapy/continued ruxolitinib: 33.3% vs 12.8% in baseline Hb <100 g/L subgroup, and 34.7% vs 3.0% in baseline non–transfusion-independent subgroup (https://doi.org/10.1007/s12325-024-02928-4; 2024-07) (wang2025currentadvancesin pages 5-7).

#### Pacritinib (JAK2/IRAK1/ACVR1; JAK1-sparing; thrombocytopenic MF)
- ASH Education Program review: “Pacritinib, selective Jak2 inhibitor, was approved in 2022 to treat patients with symptomatic MF and a platelet count lower than 50 × 10^9/L.” (https://doi.org/10.1182/hematology.2022000340; 2022-12) (reynolds2022newapproachesto pages 1-3).
- **Real-world effectiveness in bicytopenic MF (community oncology EHR, 2022–2023):** Among bicytopenic patients, median platelets improved from 61.0×10^9/L at index to 68.0×10^9/L at day 90; median hemoglobin improved from 7.2 g/dL at index to 8.0 g/dL at day 90; 6-month OS 77.8% (Blood 2024 abstract; https://doi.org/10.1182/blood-2024-210274) (stuckey2025myelofibrosistreatmentoptions pages 8-10).

### 12.3 Allogeneic hematopoietic stem cell transplantation (allo-HSCT)
Allo-HSCT is repeatedly stated as the only curative option, generally for transplant-eligible higher-risk patients (martino2024treatmentstrategiesused pages 1-2, stuckey2025myelofibrosistreatmentoptions pages 8-10). (A detailed 2024 EBMT/ELN transplant guideline was not obtainable in this run, so granular transplant outcome statistics cannot be quoted here.)

### 12.4 Supportive care and symptom measurement implementation
- Symptom endpoints in pivotal trials often use MPN-SAF / MFSAF Total Symptom Score (TSS) reduction thresholds (TSS50), which have become regulatory endpoints and are used increasingly in practice (https://doi.org/10.1007/s10238-025-01830-9; 2025) (wang2025currentadvancesin pages 5-7).

### 12.5 MAXO (Medical Action Ontology) suggestions (examples)
- JAK inhibitor therapy (e.g., ruxolitinib, fedratinib, momelotinib, pacritinib)
- Allogeneic hematopoietic stem cell transplantation
- Red blood cell transfusion
- Symptom assessment/monitoring with validated PRO instruments

---

## 13. Prevention
No established primary prevention strategies are identified in the retrieved evidence, consistent with PMF being largely a sporadic somatic neoplasm in most clinical contexts. Secondary/tertiary prevention focuses on monitoring, symptom control, transfusion support, thrombosis/bleeding management, and preventing/mitigating progression via risk-adapted therapy (martino2024treatmentstrategiesused pages 2-4, mclornan2023diagnosisandevaluation pages 6-6).

---

## 14. Other Species / Natural Disease
No naturally occurring PMF in non-human species was captured in the retrieved evidence snippets.

---

## 15. Model Organisms
The retrieved evidence references stromal-cell involvement and fibrosis pathways (e.g., Gli1+ and Lepr+ mesenchymal stem cells) as part of mechanistic understanding, but does not provide specific PMF model organism systems in the captured snippets (shao2025areviewof pages 4-6).

---

## Recent developments (2023–2024 highlights)
1) **Expanded therapeutic landscape for cytopenic/anemic MF:** momelotinib approval (2023-09-15) and anemia-focused evidence (SIMPLIFY-2 subgroup TI improvements) (chifotides2023associationofmyelofibrosis pages 2-4, wang2025currentadvancesin pages 5-7).  
2) **Real-world data scaling using EHR networks:** TriNetX-based MF studies spanning >64,000 MF patients to validate risk factors and simplified IPSS approaches (https://doi.org/10.3390/cancers16071416; 2024-04) (martino2024treatmentstrategiesused pages 1-2).  
3) **Modern prognostication:** emphasis on mutation-informed models (MIPSS70+ v2.0) and integrated risk modeling (mora2024prognosticandpredictive pages 1-2, mclornan2023diagnosisandevaluation pages 6-6).  
4) **Recognition of phenotypic heterogeneity (proliferative vs cytopenic):** linking clinical phenotype with allele burden and co-mutation architecture to tailor therapy (chifotides2023associationofmyelofibrosis pages 2-4, reynolds2022newapproachesto pages 1-3).

---

## Key statistics (selected, recent)
- PMF incidence range **0.22–0.99 per 100,000 per year** (review) (martino2024treatmentstrategiesused pages 1-2).
- US incidence estimate **0.44 per 100,000 per year** (mora2024prognosticandpredictive pages 1-2).
- Driver distribution in PMF: ~60% JAK2 / 25–30% CALR / 5–10% MPL (chifotides2023associationofmyelofibrosis pages 2-4) or ~two-thirds JAK2 / 25% CALR / 10% MPL / 10% triple-negative (mora2024prognosticandpredictive pages 1-2).
- Thromboembolic events ~**10–20%** (shao2025areviewof pages 4-6).
- Ruxolitinib discontinuation: **50–70% within 3–5 years** (abstract statement) (wang2025currentadvancesin pages 5-7).
- SIMPLIFY-2 anemia-focused subgroup: TI at week 24 up to **33.3% vs 12.8%** (Hb<100 g/L) and **34.7% vs 3.0%** (baseline non-TI) for momelotinib vs BAT/ruxolitinib (wang2025currentadvancesin pages 5-7).

---

## Embedded summary table: molecular hallmarks
| Feature category | PMF finding | Approximate frequency / definition | Clinical or biologic association |
|---|---|---|---|
| Driver mutation | **JAK2 V617F** | ~60% of PMF; alternatively described as about two-thirds of PMF (chifotides2023associationofmyelofibrosis pages 2-4, mora2024prognosticandpredictive pages 1-2) | Higher allele burden is associated with the **myeloproliferative phenotype**; lower burden with **myelodepletive/cytopenic phenotype** (chifotides2023associationofmyelofibrosis pages 2-4) |
| Driver mutation | **CALR exon 9** | ~25–30% of PMF; another source gives ~25% (chifotides2023associationofmyelofibrosis pages 2-4, mora2024prognosticandpredictive pages 1-2) | CALR is a major clonal driver used in diagnosis; type 1/like CALR is incorporated in molecular prognostic models such as MIPSS70 (martino2024treatmentstrategiesused pages 2-4, mora2024prognosticandpredictive pages 1-2) |
| Driver mutation | **MPL** (classically W515L/K) | ~5–10% of PMF; another source gives ~10% (chifotides2023associationofmyelofibrosis pages 2-4, mora2024prognosticandpredictive pages 1-2) | Canonical MPN driver used in WHO/ICC-style diagnostic workup (martino2024treatmentstrategiesused pages 2-4, mclornan2023diagnosisandevaluation pages 6-6) |
| Driver-negative subset | **Triple-negative PMF** | ~10% in one review; ~10–15% in another broader MPN review (mora2024prognosticandpredictive pages 1-2, ozygała2024biologicalmarkersof pages 10-12) | Generally considered biologically adverse in PMF literature; requires other clonal evidence/exclusion of reactive fibrosis in diagnostic frameworks (mclornan2023diagnosisandevaluation pages 6-6, ozygała2024biologicalmarkersof pages 10-12) |
| High molecular risk (HMR) definition | **ASXL1, EZH2, IDH1, IDH2, SRSF2, U2AF1 Q157** | HMR genes are the adverse mutation set used in contemporary prognostic models; BSH notes MIPSS70+ v2.0 incorporates HMR genes plus **U2AF1 Q157** (chifotides2023associationofmyelofibrosis pages 2-4, mclornan2023diagnosisandevaluation pages 6-6) | Associated with worse overall survival, higher blast-phase risk, and more aggressive biology (chifotides2023associationofmyelofibrosis pages 2-4, mora2024prognosticandpredictive pages 1-2) |
| Common co-mutations | **ASXL1, DNMT3A, TET2** | Co-mutations occur in ~50% of patients; ASXL1, DNMT3A, and TET2 are repeatedly cited as common examples (martino2024treatmentstrategiesused pages 2-4) | Reflect clonal complexity and are relevant to prognosis beyond driver status (martino2024treatmentstrategiesused pages 2-4, mora2024prognosticandpredictive pages 1-2) |
| Additional recurrent co-mutations | **SRSF2, EZH2, IDH1/2, SF3B1, U2AF1, TP53** | About 80% of PMF cases carry non-driver myeloid gene variants in one 2024 review (mora2024prognosticandpredictive pages 1-2) | Splicing/epigenetic mutations are enriched in advanced or cytopenic disease and shorten survival (chifotides2023associationofmyelofibrosis pages 2-4, mora2024prognosticandpredictive pages 1-2) |
| Mutations linked to advanced disease | **ASXL1, U2AF1-Q157, SRSF2** | Not primarily frequency-defined here, but identified as enriched in MF/advanced disease (martino2024treatmentstrategiesused pages 2-4) | Poorer survival and adverse-risk enrichment (martino2024treatmentstrategiesused pages 2-4, wang2025currentadvancesin pages 5-7) |
| Mutations linked to treatment resistance | **RAS/CBL pathway mutations** | Defined as non-driver adverse co-mutations rather than frequent drivers (martino2024treatmentstrategiesused pages 2-4, wang2025currentadvancesin pages 5-7) | Associated with **ruxolitinib resistance/failure** (martino2024treatmentstrategiesused pages 2-4, wang2025currentadvancesin pages 5-7) |
| Phenotype association | **Myeloproliferative phenotype** | Molecular profile tends to show **higher JAK2 V617F burden** and **fewer non-driver mutations** (chifotides2023associationofmyelofibrosis pages 2-4) | Typical features: larger spleen, leukocytosis, normal/mild anemia, lower fibrosis grade, better response to ruxolitinib (chifotides2023associationofmyelofibrosis pages 2-4) |
| Phenotype association | **Myelodepletive / cytopenic phenotype** | More often shows **lower JAK2 V617F burden**, **greater genomic complexity**, and more HMR/splicing-epigenetic mutations (chifotides2023associationofmyelofibrosis pages 2-4, reynolds2022newapproachesto pages 1-3) | Typical features: ≥2 cytopenias, transfusion dependence, moderate/severe thrombocytopenia, higher fibrosis grade, inferior survival, limited ruxolitinib response; non-myelosuppressive JAK inhibitors (momelotinib/pacritinib) are emphasized for this phenotype (chifotides2023associationofmyelofibrosis pages 2-4, reynolds2022newapproachesto pages 1-3) |


*Table: This table summarizes the core genetic and molecular hallmarks of primary myelofibrosis, including driver mutation frequencies, adverse co-mutation profiles, and how molecular features map to myeloproliferative versus myelodepletive phenotypes. It is useful as a compact reference for diagnosis, prognosis, and treatment stratification.*

---

## Source URLs (selected)
- Martino et al., *Hematology Reports* (2024-10): https://doi.org/10.3390/hematolrep16040067 (martino2024treatmentstrategiesused pages 1-2)  
- Mora et al., *Curr Hematol Malig Rep* (2024-08): https://doi.org/10.1007/s11899-024-00739-6 (mora2024prognosticandpredictive pages 1-2)  
- Chifotides et al., *Cancers* (2023-06): https://doi.org/10.3390/cancers15133331 (chifotides2023associationofmyelofibrosis pages 2-4)  
- McLornan et al., BSH Guideline (*Br J Haematol*) (2023-11): https://doi.org/10.1111/bjh.19164 (mclornan2023diagnosisandevaluation pages 6-6)  
- Harrison et al., SIMPLIFY-2 subgroup (*Adv Ther*) (2024-07): https://doi.org/10.1007/s12325-024-02928-4 (wang2025currentadvancesin pages 5-7)  
- Reynolds & Pettit, ASH Education (2022-12): https://doi.org/10.1182/hematology.2022000340 (reynolds2022newapproachesto pages 1-3)


References

1. (martino2024treatmentstrategiesused pages 1-2): Massimo Martino, Martina Pitea, Annalisa Sgarlata, Ilaria Maria Delfino, Francesca Cogliandro, Anna Scopelliti, Violetta Marafioti, Simona Polimeni, Gaetana Porto, Giorgia Policastro, Giovanna Utano, Maria Pellicano, Giovanni Leanza, and Caterina Alati. Treatment strategies used in treating myelofibrosis: state of the art. Hematology Reports, 16:698-713, Oct 2024. URL: https://doi.org/10.3390/hematolrep16040067, doi:10.3390/hematolrep16040067. This article has 4 citations.

2. (wang2025currentadvancesin pages 5-7): Le Wang, Julie Li, Leah Arbitman, Hailing Zhang, Haipeng Shao, Michael Martin, Lynn Moscinski, and Jinming Song. Current advances in the diagnosis and treatment of major myeloproliferative neoplasms. Cancers, 17:1834, May 2025. URL: https://doi.org/10.3390/cancers17111834, doi:10.3390/cancers17111834. This article has 5 citations.

3. (martino2024treatmentstrategiesused pages 2-4): Massimo Martino, Martina Pitea, Annalisa Sgarlata, Ilaria Maria Delfino, Francesca Cogliandro, Anna Scopelliti, Violetta Marafioti, Simona Polimeni, Gaetana Porto, Giorgia Policastro, Giovanna Utano, Maria Pellicano, Giovanni Leanza, and Caterina Alati. Treatment strategies used in treating myelofibrosis: state of the art. Hematology Reports, 16:698-713, Oct 2024. URL: https://doi.org/10.3390/hematolrep16040067, doi:10.3390/hematolrep16040067. This article has 4 citations.

4. (shao2025areviewof pages 4-6): Richard Shao, Christopher Ryder, Le Wang, Hailing Zhang, Lynn Moscinski, Michael Martin, Mac Shebes, Julie Y. Li, and Jinming Song. A review of the pathological and molecular diagnosis of primary myelofibrosis. Cancers, 18:50, Dec 2025. URL: https://doi.org/10.3390/cancers18010050, doi:10.3390/cancers18010050. This article has 0 citations.

5. (wang2025currentadvancesin pages 4-5): Le Wang, Julie Li, Leah Arbitman, Hailing Zhang, Haipeng Shao, Michael Martin, Lynn Moscinski, and Jinming Song. Current advances in the diagnosis and treatment of major myeloproliferative neoplasms. Cancers, 17:1834, May 2025. URL: https://doi.org/10.3390/cancers17111834, doi:10.3390/cancers17111834. This article has 5 citations.

6. (stuckey2025myelofibrosistreatmentoptions pages 8-10): Ruth Stuckey, Adrián Segura Díaz, and María Teresa Gómez-Casares. Myelofibrosis: treatment options after ruxolitinib failure. Current Oncology, 32:339, Jun 2025. URL: https://doi.org/10.3390/curroncol32060339, doi:10.3390/curroncol32060339. This article has 2 citations.

7. (mora2024prognosticandpredictive pages 1-2): Barbara Mora, Cristina Bucelli, Daniele Cattaneo, Valentina Bellani, Francesco Versino, Kordelia Barbullushi, Nicola Fracchiolla, Alessandra Iurlo, and Francesco Passamonti. Prognostic and predictive models in myelofibrosis. Current Hematologic Malignancy Reports, 19:223-235, Aug 2024. URL: https://doi.org/10.1007/s11899-024-00739-6, doi:10.1007/s11899-024-00739-6. This article has 16 citations.

8. (mclornan2023diagnosisandevaluation pages 6-6): Donal P. McLornan, Anna L. Godfrey, Anna Green, Rebecca Frewin, Siamak Arami, Jessica Brady, Nauman M. Butt, Catherine Cargo, Joanne Ewing, Sebastian Francis, Mamta Garg, Claire Harrison, Andrew Innes, Alesia Khan, Steve Knapper, Jonathan Lambert, Adam Mead, Andrew McGregor, Pratap Neelakantan, Bethan Psaila, Tim C. P. Somervaille, Claire Woodley, Jyoti Nangalia, Nicholas C. P. Cross, and Mary Frances McMullin. Diagnosis and evaluation of prognosis of myelofibrosis: a british society for haematology guideline. British Journal of Haematology, 204:127-135, Nov 2023. URL: https://doi.org/10.1111/bjh.19164, doi:10.1111/bjh.19164. This article has 6 citations and is from a domain leading peer-reviewed journal.

9. (chifotides2023associationofmyelofibrosis pages 2-4): Helen T. Chifotides, Srdan Verstovsek, and Prithviraj Bose. Association of myelofibrosis phenotypes with clinical manifestations, molecular profiles, and treatments. Cancers, 15:3331, Jun 2023. URL: https://doi.org/10.3390/cancers15133331, doi:10.3390/cancers15133331. This article has 27 citations.

10. (reynolds2022newapproachesto pages 1-3): Samuel B. Reynolds and Kristen Pettit. New approaches to tackle cytopenic myelofibrosis. Hematology. American Society of Hematology. Education Program, 2022 1:235-244, Dec 2022. URL: https://doi.org/10.1182/hematology.2022000340, doi:10.1182/hematology.2022000340. This article has 17 citations.

11. (ozygała2024biologicalmarkersof pages 10-12): Aleksandra Ozygała, Joanna Rokosz-Mierzwa, Paulina Widz, Paulina Skowera, Mateusz Wiliński, Borys Styka, and Monika Lejman. Biological markers of myeloproliferative neoplasms in children, adolescents and young adults. Cancers, 16:4114, Dec 2024. URL: https://doi.org/10.3390/cancers16234114, doi:10.3390/cancers16234114. This article has 3 citations.

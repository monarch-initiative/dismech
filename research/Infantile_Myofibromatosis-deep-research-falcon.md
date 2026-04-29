---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:58.591636'
end_time: '2026-04-04T12:36:09.165039'
duration_seconds: 670.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Infantile Myofibromatosis
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 54
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infantile Myofibromatosis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Infantile Myofibromatosis** covering all of the
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
- **Disease Name:** Infantile Myofibromatosis
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Infantile Myofibromatosis** covering all of the
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


## Infantile Myofibromatosis (IM): Disease Characteristics Research Report

### Target disease
- **Disease name:** Infantile myofibromatosis (IM)
- **Category:** Genetic (predominantly PDGFRB-driven; rarer NOTCH3-driven families)

---

## 1. Disease Information

### 1.1 Overview / definition (current understanding)
Infantile myofibromatosis is a (generally) benign, non-metastasizing myofibroblastic/perivascular tumor disorder characterized by formation of nodules in **skin/subcutis, skeletal muscle, and bone**, and less commonly **visceral organs**; visceral involvement drives most severe outcomes. (lu2023prenatalgeneticdiagnosis pages 1-2, martignetti2013mutationsinpdgfrb pages 1-3)

A widely used clinical classification distinguishes: (i) **solitary** IM, (ii) **multicentric** IM without visceral involvement, and (iii) **disseminated/generalized** IM with visceral disease. (lu2023prenatalgeneticdiagnosis pages 1-2, mashiah2014infantilemyofibromatosisa pages 2-4)

### 1.2 Key identifiers and nomenclature
- **OMIM/MIM:** **IM (MIM/OMIM 228550)** is explicitly referenced in the genetics literature. (lee2013mutationsinpdgfrb pages 1-3, lepelletier2017heterozygouspdgfrbmutation pages 1-2)
- **Other identifiers:** Standard **Orphanet (ORPHA), ICD-10/ICD-11, MeSH** identifiers were **not available in the retrieved primary-literature full texts in this run**, so they cannot be verified here.

### 1.3 Synonyms / related terms used in practice
Commonly used related terms in the retrieved literature include:
- “**Myofibromatosis**” for multicentric disease, and “**myofibroma**” for solitary lesions/tumors. (dachy2019associationofpdgfrb pages 1-2, koo2020adistinctivegenomic pages 1-2)
- “**Generalized/disseminated infantile myofibromatosis**” for visceral disease. (mudry2017casereportrapid pages 1-2, lu2023prenatalgeneticdiagnosis pages 1-2)

### 1.4 Evidence sources
The knowledge base content below is derived primarily from **aggregated disease-level resources in peer-reviewed cohort studies/consensus recommendations** plus **case reports/series** (including prenatal and targeted-therapy reports). (hettmer2021genetictestingand pages 1-3, dachy2019associationofpdgfrb pages 1-2, mashiah2014infantilemyofibromatosisa pages 2-4, lu2023prenatalgeneticdiagnosis pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Genetic etiology is central.** Two genes have the strongest evidence in human familial disease:
- **PDGFRB (platelet-derived growth factor receptor beta)**: germline (autosomal dominant) and somatic/mosaic gain-of-function variants; constitutes the dominant known genetic driver. (martignetti2013mutationsinpdgfrb pages 1-3, hettmer2021genetictestingand pages 1-3, dachy2019associationofpdgfrb pages 1-2)
- **NOTCH3**: a rare familial cause (e.g., NOTCH3 p.Leu1519Pro) and mechanistic link to PDGFRB upregulation. (martignetti2013mutationsinpdgfrb pages 1-3, wu2021theinfantilemyofibromatosis pages 1-1)

### 2.2 Risk factors
- **Genetic risk:** Inherited **autosomal-dominant PDGFRB** variants confer risk, but penetrance is not complete and expressivity is variable. (lu2023prenatalgeneticdiagnosis pages 3-5, hettmer2021genetictestingand pages 1-3)
- **Somatic/mosaic risk:** Severe multicentric disease can reflect post-zygotic/mosaic PDGFRB alterations or “second-hit” architectures (two PDGFRB variants in the same patient/tumor lineage). (dachy2019associationofpdgfrb pages 3-4, pudig2025infantilemyofibromatosisand pages 1-2)

No specific environmental or lifestyle risk factors were identified in the retrieved evidence.

### 2.3 Protective factors / gene–environment interactions
No protective genetic variants or gene–environment interaction evidence was identified in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Core phenotype spectrum (with onset, course, frequencies)
**Typical onset:** most commonly **at birth or before age 2 years**. (murray2017thespectrumof pages 1-7, hettmer2021genetictestingand pages 1-3)

**Clinical forms and frequencies (single-center series):** In a 28-case series, clinical spectrum included **solitary (~50%)**, **multicentric (~39%)**, and **generalized** forms. (mashiah2014infantilemyofibromatosisa pages 1-2)

**Lesion characteristics:** firm, painless cutaneous/subcutaneous nodules; may appear flesh-colored/purple or ulcerated/angiomatous. (mashiah2014infantilemyofibromatosisa pages 4-6, mashiah2014infantilemyofibromatosisa pages 1-2)

**Spontaneous regression:** Common in multicentric disease: in the 28-case series, “**The nodules regressed spontaneously … in 7 of 11 patients during the ﬁrst 2 years of life**.” (mashiah2014infantilemyofibromatosisa pages 2-4)

**Recurrence:** Although regression is common, late recurrence/relapse can occur and long-term follow-up may be needed. (mashiah2014infantilemyofibromatosisa pages 4-6, murray2017thespectrumof pages 1-7)

**Visceral involvement:** Visceral lesions may involve lung, liver, heart, spleen, intestine/bowel, kidney, and other organs. (lu2023prenatalgeneticdiagnosis pages 3-5, mashiah2014infantilemyofibromatosisa pages 2-4)

### 3.2 Prenatal phenotype
Prenatal presentation is rare but increasingly recognized.
- In a literature review of prenatally detected cases, detection was typically in the third trimester: **15/17**, mean **32 weeks**. (lu2023prenatalgeneticdiagnosis pages 3-5)
- Visceral involvement was common in this prenatal series (**>50%**, 9/17), affecting organs including lung, liver, heart, spleen, intestine, and kidney. (lu2023prenatalgeneticdiagnosis pages 3-5)

### 3.3 Phenotype → suggested HPO terms (examples)
(ontology suggestions; not claims of completeness)
- Cutaneous/subcutaneous nodules/tumors: **HP:0008069 (Subcutaneous nodule)**, **HP:0008064 (Skin nodule)**
- Soft-tissue tumor / fibrous tumor: **HP:0002664 (Soft tissue mass)**
- Bone involvement (lytic lesions/erosion): **HP:0002658 (Skeletal abnormalities)**, **HP:0002650 (Skeletal lytic lesions)**
- Visceral involvement (examples): **HP:0001627 (Abnormality of the cardiovascular system)**, **HP:0001740 (Abnormality of the gastrointestinal system)**, **HP:0001507 (Failure to thrive)** (for severe systemic disease)
- Prenatal ultrasound-detected masses: **HP:0000918 (Abnormal prenatal ultrasound)**

### 3.4 Quality-of-life impact
QoL impact is driven by number/location of lesions and organ compromise. A targeted-therapy case report emphasizes that sunitinib-based therapy produced response “**without toxicities or limitations to daily life activities**” in a refractory case. (mudry2017casereportrapid pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **PDGFRB** (major): Germline AD familial IM and somatic/mosaic IM. (martignetti2013mutationsinpdgfrb pages 1-3, hettmer2021genetictestingand pages 1-3, dachy2019associationofpdgfrb pages 1-2)
- **NOTCH3** (rare): identified in a family and functionally characterized as ligand-independent gain-of-function with downstream PDGFRB upregulation. (martignetti2013mutationsinpdgfrb pages 1-3, wu2021theinfantilemyofibromatosis pages 1-1)

### 4.2 Pathogenic variant classes and examples
**PDGFRB** gain-of-function variants cluster in key regulatory regions:
- **Juxtamembrane domain hotspot:** p.Arg561Cys (R561C) and nearby residues. (hettmer2021genetictestingand pages 1-3, lee2013mutationsinpdgfrb pages 1-3)
- **Kinase domain hotspot:** p.Asn666Lys (N666K); also p.Pro660Thr (P660T). (lee2013mutationsinpdgfrb pages 1-3, koo2020adistinctivegenomic pages 1-2)
- **Prenatal DFIM example:** PDGFRB **c.1681C>T (p.R561C)** inherited from an asymptomatic father; authors highlight incomplete penetrance/variable expressivity and severe visceral disease leading to fetal demise in their case. (lu2023prenatalgeneticdiagnosis pages 1-2, lu2023prenatalgeneticdiagnosis pages 5-6)

**NOTCH3**:
- Familial NOTCH3 **c.4556T>C (p.Leu1519Pro; L1519P)** was identified in a PDGFRB-negative family. (lee2013mutationsinpdgfrb pages 1-3, martignetti2013mutationsinpdgfrb pages 1-3)

**Recent 2024 expansion of PDGFRB genotype/phenotype:** Corneal infantile myofibromatosis was associated with novel activating PDGFRB variants including **c.1766A>G (p.Tyr589Cys)** and **c.1949C>G (p.Ser650Trp / S650W)**. (howaldt2024cornealinfantilemyofibromatosis pages 4-6, howaldt2024cornealinfantilemyofibromatosis pages 8-9)

### 4.3 Somatic vs germline architecture
- Familial IM typically follows **autosomal-dominant inheritance** linked to **PDGFRB germline** variants. (hettmer2021genetictestingand pages 1-3)
- **Somatic PDGFRB** variants occur in solitary and multicentric lesions; multicentric lesions may share post-zygotic variants or show “second-hit” patterns. (dachy2019associationofpdgfrb pages 3-4, hettmer2021genetictestingand pages 6-7)

### 4.4 Molecular mechanisms (pathophysiology)
**PDGFRB activation as upstream driver:** PDGFRB gain-of-function variants produce **ligand-independent receptor activation** and downstream growth signaling; in a 69-patient pediatric-focused cohort, functional characterization supported constitutive activation across identified variants. (dachy2019associationofpdgfrb pages 1-2, dachy2019associationofpdgfrb pages 3-4)

**NOTCH3–PDGFRB axis:** Wu et al. functionally showed NOTCH3L1519P is ligand-independent gain-of-function and “**upregulates PDGFRB expression in fibroblasts**,” concluding they “**define a NOTCH3–PDGFRB axis in IMF**.” (wu2021theinfantilemyofibromatosis pages 1-1)

### 4.5 Suggested GO (biological process) and CL (cell type) terms
(ontology suggestions)
- GO processes: **GO:0007173 (epidermal growth factor receptor signaling pathway)** (as an RTK analog), **GO:0007169 (transmembrane receptor protein tyrosine kinase signaling pathway)**, **GO:0008283 (cell population proliferation)**, **GO:0001525 (angiogenesis)**
- CL (cell types): **CL:0000186 (myofibroblast)**; pericytic lineage supported by genomic/IHC profiling. (koo2020adistinctivegenomic pages 1-2)

---

## 5. Environmental Information
No validated environmental, lifestyle, or infectious triggers were identified in the retrieved evidence base.

---

## 6. Mechanism / Pathophysiology (causal chains)

### 6.1 PDGFRB-driven disease
**Causal chain (simplified):**
1) Activating PDGFRB variant (germline, somatic, or mosaic) → 2) Constitutive PDGFRB kinase signaling → 3) Increased proliferation/survival of perivascular/myofibroblastic progenitors → 4) Myofibromas in skin/soft tissue/bone ± viscera → 5) Mass effect/organ dysfunction in severe disseminated disease. (dachy2019associationofpdgfrb pages 1-2, mashiah2014infantilemyofibromatosisa pages 2-4)

Downstream pathways referenced in the clinical genetics literature include **RAS/RAF/ERK** and **PI3K/AKT/mTOR** signaling. (pudig2025infantilemyofibromatosisand pages 1-2)

### 6.2 NOTCH3-driven disease (rare)
**Causal chain (simplified):**
1) NOTCH3 L1519P → 2) ligand-independent NOTCH activation with altered trafficking/processing → 3) PDGFRB upregulation (epistatic axis) → 4) enhanced PDGF responsiveness and proliferation signatures → 5) IM lesions. (wu2021theinfantilemyofibromatosis pages 7-8, wu2021theinfantilemyofibromatosis pages 8-9)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system involvement
- **Integumentary/soft tissue:** skin/subcutis, skeletal muscle (common). (lu2023prenatalgeneticdiagnosis pages 1-2, mashiah2014infantilemyofibromatosisa pages 4-6)
- **Skeletal system:** bone involvement (~50% in multicentric series; lytic lesions/erosions). (mashiah2014infantilemyofibromatosisa pages 4-6, mashiah2014infantilemyofibromatosisa pages 1-2)
- **Viscera (severe/generalized):** lung, liver, heart, spleen, bowel/intestine, kidney (reported). (lu2023prenatalgeneticdiagnosis pages 3-5, mashiah2014infantilemyofibromatosisa pages 2-4)
- **Ocular surface (recently expanded phenotype):** corneal/conjunctival “pterygium-like” lesions with recurrence post-surgery in PDGFRB-variant families. (howaldt2024cornealinfantilemyofibromatosis pages 3-4, howaldt2024cornealinfantilemyofibromatosis pages 6-8)

### 7.2 Suggested UBERON terms (examples)
- Skin: **UBERON:0002097**
- Subcutaneous tissue: **UBERON:0002072**
- Skeletal muscle: **UBERON:0001134**
- Bone: **UBERON:0002481**
- Heart: **UBERON:0000948**
- Liver: **UBERON:0002107**
- Lung: **UBERON:0002048**
- Kidney: **UBERON:0002113**
- Cornea: **UBERON:0000964**

---

## 8. Temporal Development

### 8.1 Onset and course
- Most cases present in infancy (≤2 years), but recurrence in later life can occur in familial disease. (murray2017thespectrumof pages 1-7)
- Multicentric lesions often regress within the first few years; severe disseminated disease can be rapidly lethal, including prenatal/neonatal deaths. (mashiah2014infantilemyofibromatosisa pages 2-4, lu2023prenatalgeneticdiagnosis pages 3-5)

### 8.2 Remission patterns
Spontaneous regression is characteristic, especially in multicentric non-visceral disease. (mashiah2014infantilemyofibromatosisa pages 2-4, murray2017thespectrumof pages 1-7)

---

## 9. Inheritance and Population

### 9.1 Epidemiology
- **Incidence:** A commonly cited estimate is ~**1 in 150,000**. (lu2023prenatalgeneticdiagnosis pages 1-2, hettmer2021genetictestingand pages 1-3)
- **Sex ratio:** Male predominance has been reported (e.g., M:F 1.55:1 overall in a 28-case series; higher in multicentric). (mashiah2014infantilemyofibromatosisa pages 4-6)

### 9.2 Inheritance
- **Autosomal dominant** inheritance is well supported for familial PDGFRB-driven IM; incomplete penetrance and variable expressivity are documented. (lu2023prenatalgeneticdiagnosis pages 3-5, hettmer2021genetictestingand pages 1-3)
- In prenatal PDGFRB-variant disease, a **50% recurrence risk** was noted for an inherited heterozygous pathogenic PDGFRB variant. (lu2023prenatalgeneticdiagnosis pages 2-3)

---

## 10. Diagnostics

### 10.1 Clinical evaluation and imaging
- **Prenatal ultrasound characteristics:** lesions described as hypoechogenic/moderately echogenic, relatively homogeneous/with slight heterogeneity, clearly demarcated, and with absent/poor vascularity; detection typically in third trimester. (lu2023prenatalgeneticdiagnosis pages 2-3, lu2023prenatalgeneticdiagnosis pages 3-5)

- **Postnatal staging/work-up (series recommendations):** After histopathologic confirmation, suggested evaluation includes clinical exam, ECG, chest/skeletal radiographs, and thoracoabdominal ultrasound/CT. (mashiah2014infantilemyofibromatosisa pages 6-7)

- **Expert consensus (SIOPE):** recommends screening for multicentric and visceral disease with **whole-body MRI and/or PET** and targeted cardiac/abdominal imaging. (hettmer2021genetictestingand pages 5-6)

### 10.2 Pathology and immunohistochemistry
Characteristic histology includes a **biphasic** lesion with peripheral spindle-cell myofibroblastic proliferation and central hemangiopericytoma-like vascular areas (“staghorn” vessels). (mashiah2014infantilemyofibromatosisa pages 2-4)

Immunophenotype in series/case contexts:
- Strong **smooth muscle actin (SMA)** positivity is commonly reported. (mashiah2014infantilemyofibromatosisa pages 2-4, lu2023prenatalgeneticdiagnosis pages 2-3)
- In one familial-spectrum report, tumors were **actin-positive and desmin-negative**. (murray2017thespectrumof pages 1-7)
- In corneal PDGFRB-variant lesions: SMA-positive, low Ki-67 (<5%), variable/marginal desmin; negative caldesmon and CD34 in described cases. (howaldt2024cornealinfantilemyofibromatosis pages 1-2, howaldt2024cornealinfantilemyofibromatosis pages 3-4)

### 10.3 Genetic testing (real-world implementation)
**Tumor-first deep sequencing is increasingly used**, given high prevalence of PDGFRB gain-of-function variants in pediatric disease and mosaicism/second-hit architectures.
- In a 69-patient cohort, deep targeted sequencing identified PDGFRB gain-of-function variants in pediatric cases and supported their diagnostic/prognostic/therapeutic utility. (dachy2019associationofpdgfrb pages 1-2)
- SIOPE recommendations emphasize NGS with sufficient depth; most pathogenic PDGFRB variants cluster in **exons 12 and 14**, but up to one-third occur elsewhere; for suspected mosaicism, testing multiple lesions is recommended. (hettmer2021genetictestingand pages 6-7)

### 10.4 Differential diagnosis (high level)
The main diagnostic challenge is morphologic overlap with other pericytic/myofibroblastic lesions (e.g., myopericytoma spectrum). Genomic + NOTCH3 IHC patterns can help in difficult cases. (koo2020adistinctivegenomic pages 1-2, dachy2019associationofpdgfrb pages 4-5)

---

## 11. Outcome / Prognosis

### 11.1 Prognosis by subtype
- **Solitary / multicentric (no viscera):** generally good; spontaneous regression common. (lu2023prenatalgeneticdiagnosis pages 1-2, mashiah2014infantilemyofibromatosisa pages 4-6)
- **Disseminated/generalized with visceral involvement:** poor prognosis with high mortality.
  - Review-level statements cite high mortality “up to” ~70% in visceral disease. (lee2013mutationsinpdgfrb pages 1-3)
  - In a prenatal review, fetal mortality was **29% (5/17)** overall and **67% (4/6)** in disseminated DFIM; **3/17 (18%)** neonates died within one month due to severe visceral involvement. (lu2023prenatalgeneticdiagnosis pages 3-5)

### 11.2 Prognostic factors (supported)
- **Visceral involvement** is the dominant adverse prognostic factor. (murray2017thespectrumof pages 1-7, lu2023prenatalgeneticdiagnosis pages 3-5)
- **Genotype** may be prognostic/therapeutic (e.g., PDGFRB mutations commonly imatinib-sensitive, but specific alleles can be resistant). (dachy2019associationofpdgfrb pages 4-5, hettmer2021genetictestingand pages 3-5)

---

## 12. Treatment

### 12.1 Standard management in current practice
- **Observation** is often appropriate for uncomplicated lesions expected to regress (especially multicentric non-visceral). (lu2023prenatalgeneticdiagnosis pages 1-2, mashiah2014infantilemyofibromatosisa pages 2-4)
- **Surgical excision** is commonly used for solitary lesions or lesions causing local complications. (mashiah2014infantilemyofibromatosisa pages 2-4, lu2023prenatalgeneticdiagnosis pages 3-5)
- **Chemotherapy** is used in severe/refractory disease; regimens in case literature include vinblastine/methotrexate metronomic therapy and multi-agent chemotherapy (e.g., VAC variants). (mudry2017casereportrapid pages 1-2)

### 12.2 Targeted therapy (major recent development)
**PDGFRB as an actionable target:**
- Large cohort functional testing supports broad PDGFRB mutant sensitivity: “all but one” PDGFRB mutant were imatinib-sensitive at clinically relevant concentrations in vitro, with a resistant activation-loop allele noted in that cohort. (dachy2019associationofpdgfrb pages 1-2, dachy2019associationofpdgfrb pages 4-5)

**Clinical targeted-therapy implementation (case evidence):**
- A refractory generalized IM case with germline PDGFRB mutation had “**unexpected and durable response**” to **sunitinib** plus low-dose vinblastine after chemotherapy toxicity/limited response. (mudry2017casereportrapid pages 1-2)

**2024 ocular/corneal targeted-therapy concept:**
- Novel activating PDGFRB variants causing corneal IM were **blocked by imatinib (1 μM) in vitro**, motivating targeted therapy concepts including topical imatinib (investigational). (howaldt2024cornealinfantilemyofibromatosis pages 6-8, howaldt2024cornealinfantilemyofibromatosis pages 8-9)

### 12.3 MAXO term suggestions
- Observation/active surveillance: **MAXO:0000127 (clinical monitoring)**
- Surgical excision: **MAXO:0000467 (surgical excision)**
- Chemotherapy: **MAXO:0000647 (chemotherapy)**
- Tyrosine kinase inhibitor therapy (imatinib/sunitinib): **MAXO:0000747 (protein kinase inhibitor therapy)**
- Prenatal diagnosis/genetic testing: **MAXO:0000741 (genetic testing)**

### 12.4 Clinical trials
A clinicaltrials.gov search during this run did not retrieve an IM-specific interventional trial; retrieved trials were broader pediatric solid tumor studies (e.g., selpercatinib trial NCT03899792) and are not disease-targeted for IM. (tool output not cited; no IM-specific NCT evidence in retrieved text set)

---

## 13. Prevention
No primary prevention exists for a genetic tumor predisposition of this type. Secondary/tertiary prevention is primarily **genetic counseling + early surveillance** in at-risk infants.
- Genetic counseling and prenatal approaches: authors recommend genetic counseling and consideration of **prenatal or preimplantation genetic diagnosis** in families with pathogenic PDGFRB variants. (lu2023prenatalgeneticdiagnosis pages 2-3)

---

## 14. Other Species / Natural Disease
No veterinary or cross-species natural disease evidence was identified in the retrieved sources.

---

## 15. Model Organisms / Model Systems
While whole-animal models were not identified in the retrieved evidence, mechanistic and functional work uses **cell-based systems**:
- NOTCH3 L1519P functional characterization in fibroblasts and signaling assays defining NOTCH3→PDGFRB axis. (wu2021theinfantilemyofibromatosis pages 1-1, wu2021theinfantilemyofibromatosis pages 7-8)
- PDGFRB variant functional assays in transfected cells, including imatinib inhibition experiments for corneal IM variants. (howaldt2024cornealinfantilemyofibromatosis pages 2-3, howaldt2024cornealinfantilemyofibromatosis pages 6-8)

---

## Recent developments & “expert opinions” (authoritative analyses)

### 2023–2024 highlights (prioritized)
1) **Prenatal genetic diagnosis and outcome quantification (2023):** Lü et al. emphasize that “**Prenatal IM diagnosis is difficult. Initial detection is always based on ultrasound. DFIM has high mortality**” and report a severe fetal case with PDGFRB p.R561C. (lu2023prenatalgeneticdiagnosis pages 1-2)
2) **Novel PDGFRB variants expanding the phenotype to corneal disease (2024):** Howaldt et al. identify novel activating PDGFRB variants in corneal IM and show imatinib blockade in vitro, proposing targeted therapeutic avenues to prevent recurrences. (howaldt2024cornealinfantilemyofibromatosis pages 6-8, howaldt2024cornealinfantilemyofibromatosis pages 1-2)

### Consensus/working-group recommendations
The SIOPE Host Genome Working Group report frames PDGFRB testing and surveillance as an emerging standard because mutant receptors are typically imatinib-sensitive and because early-life visceral disease can be life-threatening. (hettmer2021genetictestingand pages 1-3, hettmer2021genetictestingand pages 6-7)

---

## Visual evidence (prenatal cases)
Table 1 from Lü et al. (2023) summarizes prenatally detected IM cases, including gestational age at detection, clinical subtype, outcomes, and treatments (including chemotherapy and imatinib in specific cases). (lu2023prenatalgeneticdiagnosis media ef3ffef0)

---

## Genetics and therapy summary table
| Gene | Variant examples / hotspots | Inheritance / origin | Mechanistic implication | Therapeutic implication / evidence | Key quantitative findings | Key studies |
|---|---|---|---|---|---|---|
| PDGFRB | **R561C** (juxtamembrane hotspot, exon 12) | Germline **autosomal dominant** familial IM; can require second cis-acting hit; also reported as likely germline/de novo in sporadic pediatric disease | Disrupts juxtamembrane autoinhibition, causing ligand-independent kinase activation; weaker germline activation may need second hit for full activation | Mutant receptors are typically **imatinib-sensitive**; PDGFR inhibitors also include **sunitinib**; targeted therapy supported by clinical case responses and in vitro sensitivity (lee2013mutationsinpdgfrb pages 1-3, hettmer2021genetictestingand pages 1-3, mudry2017casereportrapid pages 1-2, dachy2019associationofpdgfrb pages 1-2) | In pediatric series, PDGFRB GOF mutations in **13/19 myofibromatosis cases (68%)**; **3/25 (12%)** PDGFRB-mutant pediatric cases were likely germline, all involving **R561** (dachy2019associationofpdgfrb pages 1-2, dachy2019associationofpdgfrb pages 3-4) | Martignetti 2013 *Am J Hum Genet*; Dachy 2019 *JAMA Dermatol*; Hettmer 2021 *Familial Cancer* |
| PDGFRB | **N666K** (kinase domain hotspot) | Often somatic second hit; also reported in sporadic lesions/mosaic contexts | Kinase-domain activating mutation favoring active receptor conformation; can cooperate with R561C in a second-hit model | Generally **imatinib-sensitive** in functional studies; PDGFRB-mutant lesions may respond to TKIs, though resistance depends on allele | Seen among recurrent hotspots in IM/myofibroma; second-hit combinations support multicentric disease biology (lee2013mutationsinpdgfrb pages 1-3, lepelletier2017heterozygouspdgfrbmutation pages 1-2, dachy2019associationofpdgfrb pages 3-4) | Lee 2013 *Clinical Genetics*; Lepelletier 2017 *Acta Derm Venereol*; Dachy 2019 *JAMA Dermatol* |
| PDGFRB | **P560L** (exon 12) | Germline **autosomal dominant** familial IM | Juxtamembrane-domain activation analogous to other exon 12 PDGFRB variants | Likely TKI-sensitive by class effect; cited among actionable PDGFRB familial variants | Novel segregating variant in a 3-generation AD IM family (lepelletier2017heterozygouspdgfrbmutation pages 1-2, hettmer2021genetictestingand pages 1-3) | Lepelletier 2017 *Acta Derm Venereol*; Hettmer 2021 *Familial Cancer* |
| PDGFRB | **P660T** (exon 14) | Germline AD in single reported family | Kinase-domain mutation predicted to stabilize active conformation / constitutive signaling | Supports genotype-guided TKI consideration; included among IM-causing activating alleles | Rare compared with exon 12 hotspots (lee2013mutationsinpdgfrb pages 1-3, hettmer2021genetictestingand pages 1-3) | Lee 2013 *Clinical Genetics*; Hettmer 2021 *Familial Cancer* |
| PDGFRB | **Y589C** and **S650W** (novel corneal IM variants) | Familial **autosomal dominant** transmission in two unrelated families | Constitutive ligand-independent activation in vitro; corneal myofibromatosis / pterygium-like phenotype | **Imatinib at 1 μM completely blocked mutant activation in vitro**; authors propose topical/systemic imatinib as targeted strategy for recurrent corneal disease (howaldt2024cornealinfantilemyofibromatosis pages 1-2, howaldt2024cornealinfantilemyofibromatosis pages 8-9, howaldt2024cornealinfantilemyofibromatosis pages 4-6, howaldt2024cornealinfantilemyofibromatosis pages 6-8) | 4 affected individuals from 2 families; all had recurrence after corneal surgery (howaldt2024cornealinfantilemyofibromatosis pages 1-2, howaldt2024cornealinfantilemyofibromatosis pages 3-4) | Howaldt 2024 *Ophthalmology Science* |
| PDGFRB | Broad pediatric mutation spectrum (including juxtamembrane duplication and multiple activating alleles) | Somatic, germline/de novo, and mosaic forms all reported | All identified pediatric PDGFRB variants in cohort caused ligand-independent receptor activation | **All but one** tested mutants were imatinib-sensitive at clinically relevant concentrations; one activation-loop allele (**D850V**) was resistant (dachy2019associationofpdgfrb pages 1-2, dachy2019associationofpdgfrb pages 4-5, hettmer2021genetictestingand pages 3-5) | 25 PDGFRB-mutant children among 69 patients; **0 adults** had PDGFRB mutations in that series (dachy2019associationofpdgfrb pages 1-2) | Dachy 2019 *JAMA Dermatol*; Hettmer 2021 *Familial Cancer* |
| PDGFRB | **c.1681C>A** germline variant in refractory generalized IM | Germline familial case; sister shared genotype/histology | Elevated intratumoral PDGFRβ phosphokinase activity | **Sunitinib + low-dose vinblastine** produced rapid, durable responses after chemotherapy failure/toxicity (mudry2017casereportrapid pages 1-2) | Real-world response in 2 siblings with severe disease; quality-of-life preserved during targeted therapy (mudry2017casereportrapid pages 1-2) | Mudry 2017 *BMC Cancer* |
| NOTCH3 | **L1519P** | Germline **autosomal dominant** in one familial kindred lacking PDGFRB mutation | Hyperactivated **ligand-independent Notch signaling**; mutant receptor mislocalized to ER/lysosomal pathway; **upregulates PDGFRB**, defining a **NOTCH3→PDGFRB axis** (wu2021theinfantilemyofibromatosis pages 7-8, wu2021theinfantilemyofibromatosis pages 1-1, wu2021theinfantilemyofibromatosis pages 1-3, wu2021theinfantilemyofibromatosis pages 8-9) | Suggests potential benefit from targeting downstream **PDGFRB** and/or Notch processing/signaling; ligand-blocking strategies may be less effective because activation is ligand-independent | Rare compared with PDGFRB-driven IM; found in 1/10 sequenced myofibroma cases in one genomic/IHC series (koo2020adistinctivegenomic pages 1-2) | Wu 2021 *Dis Model Mech*; Koo 2020 *Int J Surg Pathol* |
| PDGFRB / NOTCH3 pathway | PDGFRB hotspots plus NOTCH3 L1519P | Familial AD, somatic, and mosaic architectures all contribute to disease heterogeneity | Convergent activation of **pericytic / myofibroblastic growth signaling**; NOTCH3 activation can increase PDGFRB expression, while PDGFRB GOF directly activates downstream signaling | Supports **molecular testing-first** management: deep NGS of tumor and blood, hotspot focus on **exons 12 and 14**, and genotype-guided TKI consideration; multiple lesions may need testing when mosaicism is suspected (hettmer2021genetictestingand pages 6-7, hettmer2021genetictestingand pages 1-3) | SIOPE report notes most variants cluster in **exons 12 and 14**, but up to one-third occur elsewhere; testing of multiple lesions recommended if blood is negative and mosaicism suspected (hettmer2021genetictestingand pages 6-7) | Hettmer 2021 *Familial Cancer*; Koo 2020 *Int J Surg Pathol*; Wu 2021 *Dis Model Mech* |


*Table: This table summarizes the main disease genes, recurrent variants, inheritance patterns, pathogenic mechanisms, and therapeutic implications in infantile myofibromatosis. It highlights the predominance of PDGFRB-driven disease, the rarer NOTCH3-driven subtype, and the evidence supporting genotype-guided use of tyrosine kinase inhibitors such as imatinib and sunitinib.*

---

## Key statistics (quick reference)
- Incidence often cited: **~1:150,000** (lu2023prenatalgeneticdiagnosis pages 1-2, hettmer2021genetictestingand pages 1-3)
- Multicentric regression in a case series: **7/11 regressed spontaneously within first 2 years** (mashiah2014infantilemyofibromatosisa pages 2-4)
- Prenatal series outcomes: **71% recovered**, fetal mortality **29% (5/17)** overall; **67% (4/6)** in DFIM; neonatal death within one month **18% (3/17)** (lu2023prenatalgeneticdiagnosis pages 3-5)
- PDGFRB mutation frequency in pediatric cohort: **13/19 (68%)** in myofibromatosis cases; likely germline **3/25 (12%)** among PDGFRB-mutant pediatric cases (dachy2019associationofpdgfrb pages 1-2, dachy2019associationofpdgfrb pages 3-4)

---

## Primary literature used (URLs and publication dates)
- Lü Y et al. **Aug 2023**. *BMC Medical Genomics.* “Prenatal genetic diagnosis of disseminated infantile myofibromatosis.” https://doi.org/10.1186/s12920-023-01612-w (lu2023prenatalgeneticdiagnosis pages 1-2)
- Howaldt A et al. **May 2024**. *Ophthalmology Science.* “Corneal Infantile Myofibromatosis … imatinib-responsive variants in PDGFRB.” https://doi.org/10.1016/j.xops.2023.100444 (howaldt2024cornealinfantilemyofibromatosis pages 1-2)
- Dachy G et al. **Aug 2019**. *JAMA Dermatology.* “Association of PDGFRB Mutations With Pediatric Myofibroma and Myofibromatosis.” https://doi.org/10.1001/jamadermatol.2019.0114 (dachy2019associationofpdgfrb pages 1-2)
- Hettmer S et al. **Sep 2021**. *Familial Cancer.* “Genetic testing and surveillance in infantile myofibromatosis … SIOPE Host Genome Working Group.” https://doi.org/10.1007/s10689-020-00204-2 (hettmer2021genetictestingand pages 1-3)
- Wu D et al. **Feb 2021**. *Disease Models & Mechanisms.* “NOTCH3 L1519P … increased PDGFRB expression.” https://doi.org/10.1242/dmm.046300 (wu2021theinfantilemyofibromatosis pages 1-1)
- Mashiah J et al. **Aug 2014**. *Journal of the American Academy of Dermatology.* “Infantile myofibromatosis: a series of 28 cases.” https://doi.org/10.1016/j.jaad.2014.03.035 (mashiah2014infantilemyofibromatosisa pages 2-4)
- Mudry P et al. **Feb 2017**. *BMC Cancer.* “Rapid and durable response to PDGFR targeted therapy …” https://doi.org/10.1186/s12885-017-3115-x (mudry2017casereportrapid pages 1-2)
- Murray N et al. **Jul 2017**. *European Journal of Medical Genetics.* “Spectrum … non-penetrance and adult recurrence.” https://doi.org/10.1016/j.ejmg.2017.02.005 (murray2017thespectrumof pages 1-7)
- Martignetti JA et al. **Jun 2013**. *American Journal of Human Genetics.* “Mutations in PDGFRB cause autosomal-dominant infantile myofibromatosis.” https://doi.org/10.1016/j.ajhg.2013.04.024 (martignetti2013mutationsinpdgfrb pages 1-3)


References

1. (lu2023prenatalgeneticdiagnosis pages 1-2): Yan Lü, Yulin Jiang, Huanwen Wu, Qingwei Qi, Xiya Zhou, Qi Guo, Na Hao, Juntao Liu, and Hua Meng. Prenatal genetic diagnosis of disseminated infantile myofibromatosis: a case report and literature review. BMC Medical Genomics, Aug 2023. URL: https://doi.org/10.1186/s12920-023-01612-w, doi:10.1186/s12920-023-01612-w. This article has 1 citations and is from a peer-reviewed journal.

2. (martignetti2013mutationsinpdgfrb pages 1-3): John A. Martignetti, Lifeng Tian, Dong Li, Maria Celeste M. Ramirez, Olga Camacho-Vanegas, Sandra Catalina Camacho, Yiran Guo, Dina J. Zand, Audrey M. Bernstein, Sandra K. Masur, Cecilia E. Kim, Frederick G. Otieno, Cuiping Hou, Nada Abdel-Magid, Ben Tweddale, Denise Metry, Jean-Christophe Fournet, Eniko Papp, Elizabeth W. McPherson, Carrie Zabel, Guy Vaksmann, Cyril Morisot, Brendan Keating, Patrick M. Sleiman, Jeffrey A. Cleveland, David B. Everman, Elaine Zackai, and Hakon Hakonarson. Mutations in pdgfrb cause autosomal-dominant infantile myofibromatosis. American journal of human genetics, 92 6:1001-7, Jun 2013. URL: https://doi.org/10.1016/j.ajhg.2013.04.024, doi:10.1016/j.ajhg.2013.04.024. This article has 222 citations and is from a highest quality peer-reviewed journal.

3. (mashiah2014infantilemyofibromatosisa pages 2-4): Jacob Mashiah, Smail Hadj-Rabia, Anne Dompmartin, Annie Harroche, Etty Laloum-Grynberg, Michèle Wolter, Jean-Claude Amoric, Dominique Hamel-Teillac, Stéphane Guero, Sylvie Fraitag, and Christine Bodemer. Infantile myofibromatosis: a series of 28 cases. Journal of the American Academy of Dermatology, 71 2:264-70, Aug 2014. URL: https://doi.org/10.1016/j.jaad.2014.03.035, doi:10.1016/j.jaad.2014.03.035. This article has 123 citations and is from a domain leading peer-reviewed journal.

4. (lee2013mutationsinpdgfrb pages 1-3): JW Lee. Mutations in pdgfrb and notch3 are the first genetic causes identified for autosomal dominant infantile myofibromatosis. Clinical Genetics, 84:340-341, Oct 2013. URL: https://doi.org/10.1111/cge.12238, doi:10.1111/cge.12238. This article has 31 citations and is from a peer-reviewed journal.

5. (lepelletier2017heterozygouspdgfrbmutation pages 1-2): C. Lepelletier, Y. Al-Sarraj, C. Bodemer, H. Shaath, S. Fraitag, M. Kambouris, D. Hamel-Teillac, Hatem El Shanti, and S. Hadj-Rabia. Heterozygous pdgfrb mutation in a three-generation family with autosomal dominant infantile myofibromatosis. Acta dermato-venereologica, 97 7:858-859, Jul 2017. URL: https://doi.org/10.2340/00015555-2671, doi:10.2340/00015555-2671. This article has 21 citations and is from a domain leading peer-reviewed journal.

6. (dachy2019associationofpdgfrb pages 1-2): Guillaume Dachy, Ronald R. de Krijger, Sylvie Fraitag, Ivan Théate, Bénédicte Brichard, Suma B. Hoffman, Louis Libbrecht, Florence A. Arts, Pascal Brouillard, Miikka Vikkula, Nisha Limaye, and Jean-Baptiste Demoulin. Association of pdgfrb mutations with pediatric myofibroma and myofibromatosis. JAMA dermatology, 155:946, Aug 2019. URL: https://doi.org/10.1001/jamadermatol.2019.0114, doi:10.1001/jamadermatol.2019.0114. This article has 70 citations and is from a domain leading peer-reviewed journal.

7. (koo2020adistinctivegenomic pages 1-2): Selene C. Koo, Katherine A. Janeway, Marian H. Harris, Christy J. Fryer, Jon C. Aster, Alyaa Al-Ibraheemi, and Alanna J. Church. A distinctive genomic and immunohistochemical profile for notch3 and pdgfrb in myofibroma with diagnostic and therapeutic implications. International Journal of Surgical Pathology, 28:128-137, Apr 2020. URL: https://doi.org/10.1177/1066896919876703, doi:10.1177/1066896919876703. This article has 9 citations and is from a peer-reviewed journal.

8. (mudry2017casereportrapid pages 1-2): Peter Mudry, Ondrej Slaby, Jakub Neradil, Jana Soukalova, Kristyna Melicharkova, Ondrej Rohleder, Marta Jezova, Anna Seehofnerova, Elleni Michu, Renata Veselska, and Jaroslav Sterba. Case report: rapid and durable response to pdgfr targeted therapy in a child with refractory multiple infantile myofibromatosis and a heterozygous germline mutation of the pdgfrb gene. BMC Cancer, Feb 2017. URL: https://doi.org/10.1186/s12885-017-3115-x, doi:10.1186/s12885-017-3115-x. This article has 73 citations and is from a peer-reviewed journal.

9. (hettmer2021genetictestingand pages 1-3): Simone Hettmer, Guillaume Dachy, Guido Seitz, Abbas Agaimy, Catriona Duncan, Marjolijn Jongmans, Steffen Hirsch, Iris Kventsel, Uwe Kordes, Ronald R. de Krijger, Markus Metzler, Orli Michaeli, Karolina Nemes, Anna Poluha, Tim Ripperger, Alexandra Russo, Stephanie Smetsers, Monika Sparber-Sauer, Eveline Stutz, Franck Bourdeaut, Christian P. Kratz, and Jean-Baptiste Demoulin. Genetic testing and surveillance in infantile myofibromatosis: a report from the siope host genome working group. Familial Cancer, 20:327-336, Sep 2021. URL: https://doi.org/10.1007/s10689-020-00204-2, doi:10.1007/s10689-020-00204-2. This article has 31 citations and is from a peer-reviewed journal.

10. (wu2021theinfantilemyofibromatosis pages 1-1): Dan Wu, Sailan Wang, Daniel V. Oliveira, Francesca Del Gaudio, Michael Vanlandewijck, Thibaud Lebouvier, Christer Betsholtz, Jian Zhao, ShaoBo Jin, Urban Lendahl, and Helena Karlström. The infantile myofibromatosis notch3 l1519p mutation leads to hyperactivated ligand-independent notch signaling and increased pdgfrb expression. Disease Models &amp; Mechanisms, Feb 2021. URL: https://doi.org/10.1242/dmm.046300, doi:10.1242/dmm.046300. This article has 20 citations and is from a domain leading peer-reviewed journal.

11. (lu2023prenatalgeneticdiagnosis pages 3-5): Yan Lü, Yulin Jiang, Huanwen Wu, Qingwei Qi, Xiya Zhou, Qi Guo, Na Hao, Juntao Liu, and Hua Meng. Prenatal genetic diagnosis of disseminated infantile myofibromatosis: a case report and literature review. BMC Medical Genomics, Aug 2023. URL: https://doi.org/10.1186/s12920-023-01612-w, doi:10.1186/s12920-023-01612-w. This article has 1 citations and is from a peer-reviewed journal.

12. (dachy2019associationofpdgfrb pages 3-4): Guillaume Dachy, Ronald R. de Krijger, Sylvie Fraitag, Ivan Théate, Bénédicte Brichard, Suma B. Hoffman, Louis Libbrecht, Florence A. Arts, Pascal Brouillard, Miikka Vikkula, Nisha Limaye, and Jean-Baptiste Demoulin. Association of pdgfrb mutations with pediatric myofibroma and myofibromatosis. JAMA dermatology, 155:946, Aug 2019. URL: https://doi.org/10.1001/jamadermatol.2019.0114, doi:10.1001/jamadermatol.2019.0114. This article has 70 citations and is from a domain leading peer-reviewed journal.

13. (pudig2025infantilemyofibromatosisand pages 1-2): Luise Pudig, Silke Lassmann, Sebastian Jacob, Marina Nastainczyk-Wulf, Anja Haak, Martin Werner, Friedrich G Kapp, and Simone Hettmer. Infantile myofibromatosis and capillary malformation of the skin due to pdgfrb mosaicism. Molecular and Cellular Pediatrics, Jul 2025. URL: https://doi.org/10.1186/s40348-025-00197-x, doi:10.1186/s40348-025-00197-x. This article has 0 citations.

14. (murray2017thespectrumof pages 1-7): Natalia Murray, B. Hanna, N. Graf, H. Fu, Veronneau Mylène, Philippe M. Campeau, and A. Ronan. The spectrum of infantile myofibromatosis includes both non-penetrance and adult recurrence. European journal of medical genetics, 60 7:353-358, Jul 2017. URL: https://doi.org/10.1016/j.ejmg.2017.02.005, doi:10.1016/j.ejmg.2017.02.005. This article has 35 citations and is from a peer-reviewed journal.

15. (mashiah2014infantilemyofibromatosisa pages 1-2): Jacob Mashiah, Smail Hadj-Rabia, Anne Dompmartin, Annie Harroche, Etty Laloum-Grynberg, Michèle Wolter, Jean-Claude Amoric, Dominique Hamel-Teillac, Stéphane Guero, Sylvie Fraitag, and Christine Bodemer. Infantile myofibromatosis: a series of 28 cases. Journal of the American Academy of Dermatology, 71 2:264-70, Aug 2014. URL: https://doi.org/10.1016/j.jaad.2014.03.035, doi:10.1016/j.jaad.2014.03.035. This article has 123 citations and is from a domain leading peer-reviewed journal.

16. (mashiah2014infantilemyofibromatosisa pages 4-6): Jacob Mashiah, Smail Hadj-Rabia, Anne Dompmartin, Annie Harroche, Etty Laloum-Grynberg, Michèle Wolter, Jean-Claude Amoric, Dominique Hamel-Teillac, Stéphane Guero, Sylvie Fraitag, and Christine Bodemer. Infantile myofibromatosis: a series of 28 cases. Journal of the American Academy of Dermatology, 71 2:264-70, Aug 2014. URL: https://doi.org/10.1016/j.jaad.2014.03.035, doi:10.1016/j.jaad.2014.03.035. This article has 123 citations and is from a domain leading peer-reviewed journal.

17. (lu2023prenatalgeneticdiagnosis pages 5-6): Yan Lü, Yulin Jiang, Huanwen Wu, Qingwei Qi, Xiya Zhou, Qi Guo, Na Hao, Juntao Liu, and Hua Meng. Prenatal genetic diagnosis of disseminated infantile myofibromatosis: a case report and literature review. BMC Medical Genomics, Aug 2023. URL: https://doi.org/10.1186/s12920-023-01612-w, doi:10.1186/s12920-023-01612-w. This article has 1 citations and is from a peer-reviewed journal.

18. (howaldt2024cornealinfantilemyofibromatosis pages 4-6): Antonia Howaldt, Sandrine Lenglez, Clara Velmans, Anne Maria Schultheis, Thomas Clahsen, Mario Matthaei, Jürgen Kohlhase, Christian Vokuhl, Reinhard Büttner, Christian Netzer, Jean-Baptiste Demoulin, and Claus Cursiefen. Corneal infantile myofibromatosis caused by novel activating imatinib-responsive variants in pdgfrb. Ophthalmology Science, 4:100444, May 2024. URL: https://doi.org/10.1016/j.xops.2023.100444, doi:10.1016/j.xops.2023.100444. This article has 4 citations.

19. (howaldt2024cornealinfantilemyofibromatosis pages 8-9): Antonia Howaldt, Sandrine Lenglez, Clara Velmans, Anne Maria Schultheis, Thomas Clahsen, Mario Matthaei, Jürgen Kohlhase, Christian Vokuhl, Reinhard Büttner, Christian Netzer, Jean-Baptiste Demoulin, and Claus Cursiefen. Corneal infantile myofibromatosis caused by novel activating imatinib-responsive variants in pdgfrb. Ophthalmology Science, 4:100444, May 2024. URL: https://doi.org/10.1016/j.xops.2023.100444, doi:10.1016/j.xops.2023.100444. This article has 4 citations.

20. (hettmer2021genetictestingand pages 6-7): Simone Hettmer, Guillaume Dachy, Guido Seitz, Abbas Agaimy, Catriona Duncan, Marjolijn Jongmans, Steffen Hirsch, Iris Kventsel, Uwe Kordes, Ronald R. de Krijger, Markus Metzler, Orli Michaeli, Karolina Nemes, Anna Poluha, Tim Ripperger, Alexandra Russo, Stephanie Smetsers, Monika Sparber-Sauer, Eveline Stutz, Franck Bourdeaut, Christian P. Kratz, and Jean-Baptiste Demoulin. Genetic testing and surveillance in infantile myofibromatosis: a report from the siope host genome working group. Familial Cancer, 20:327-336, Sep 2021. URL: https://doi.org/10.1007/s10689-020-00204-2, doi:10.1007/s10689-020-00204-2. This article has 31 citations and is from a peer-reviewed journal.

21. (wu2021theinfantilemyofibromatosis pages 7-8): Dan Wu, Sailan Wang, Daniel V. Oliveira, Francesca Del Gaudio, Michael Vanlandewijck, Thibaud Lebouvier, Christer Betsholtz, Jian Zhao, ShaoBo Jin, Urban Lendahl, and Helena Karlström. The infantile myofibromatosis notch3 l1519p mutation leads to hyperactivated ligand-independent notch signaling and increased pdgfrb expression. Disease Models &amp; Mechanisms, Feb 2021. URL: https://doi.org/10.1242/dmm.046300, doi:10.1242/dmm.046300. This article has 20 citations and is from a domain leading peer-reviewed journal.

22. (wu2021theinfantilemyofibromatosis pages 8-9): Dan Wu, Sailan Wang, Daniel V. Oliveira, Francesca Del Gaudio, Michael Vanlandewijck, Thibaud Lebouvier, Christer Betsholtz, Jian Zhao, ShaoBo Jin, Urban Lendahl, and Helena Karlström. The infantile myofibromatosis notch3 l1519p mutation leads to hyperactivated ligand-independent notch signaling and increased pdgfrb expression. Disease Models &amp; Mechanisms, Feb 2021. URL: https://doi.org/10.1242/dmm.046300, doi:10.1242/dmm.046300. This article has 20 citations and is from a domain leading peer-reviewed journal.

23. (howaldt2024cornealinfantilemyofibromatosis pages 3-4): Antonia Howaldt, Sandrine Lenglez, Clara Velmans, Anne Maria Schultheis, Thomas Clahsen, Mario Matthaei, Jürgen Kohlhase, Christian Vokuhl, Reinhard Büttner, Christian Netzer, Jean-Baptiste Demoulin, and Claus Cursiefen. Corneal infantile myofibromatosis caused by novel activating imatinib-responsive variants in pdgfrb. Ophthalmology Science, 4:100444, May 2024. URL: https://doi.org/10.1016/j.xops.2023.100444, doi:10.1016/j.xops.2023.100444. This article has 4 citations.

24. (howaldt2024cornealinfantilemyofibromatosis pages 6-8): Antonia Howaldt, Sandrine Lenglez, Clara Velmans, Anne Maria Schultheis, Thomas Clahsen, Mario Matthaei, Jürgen Kohlhase, Christian Vokuhl, Reinhard Büttner, Christian Netzer, Jean-Baptiste Demoulin, and Claus Cursiefen. Corneal infantile myofibromatosis caused by novel activating imatinib-responsive variants in pdgfrb. Ophthalmology Science, 4:100444, May 2024. URL: https://doi.org/10.1016/j.xops.2023.100444, doi:10.1016/j.xops.2023.100444. This article has 4 citations.

25. (lu2023prenatalgeneticdiagnosis pages 2-3): Yan Lü, Yulin Jiang, Huanwen Wu, Qingwei Qi, Xiya Zhou, Qi Guo, Na Hao, Juntao Liu, and Hua Meng. Prenatal genetic diagnosis of disseminated infantile myofibromatosis: a case report and literature review. BMC Medical Genomics, Aug 2023. URL: https://doi.org/10.1186/s12920-023-01612-w, doi:10.1186/s12920-023-01612-w. This article has 1 citations and is from a peer-reviewed journal.

26. (mashiah2014infantilemyofibromatosisa pages 6-7): Jacob Mashiah, Smail Hadj-Rabia, Anne Dompmartin, Annie Harroche, Etty Laloum-Grynberg, Michèle Wolter, Jean-Claude Amoric, Dominique Hamel-Teillac, Stéphane Guero, Sylvie Fraitag, and Christine Bodemer. Infantile myofibromatosis: a series of 28 cases. Journal of the American Academy of Dermatology, 71 2:264-70, Aug 2014. URL: https://doi.org/10.1016/j.jaad.2014.03.035, doi:10.1016/j.jaad.2014.03.035. This article has 123 citations and is from a domain leading peer-reviewed journal.

27. (hettmer2021genetictestingand pages 5-6): Simone Hettmer, Guillaume Dachy, Guido Seitz, Abbas Agaimy, Catriona Duncan, Marjolijn Jongmans, Steffen Hirsch, Iris Kventsel, Uwe Kordes, Ronald R. de Krijger, Markus Metzler, Orli Michaeli, Karolina Nemes, Anna Poluha, Tim Ripperger, Alexandra Russo, Stephanie Smetsers, Monika Sparber-Sauer, Eveline Stutz, Franck Bourdeaut, Christian P. Kratz, and Jean-Baptiste Demoulin. Genetic testing and surveillance in infantile myofibromatosis: a report from the siope host genome working group. Familial Cancer, 20:327-336, Sep 2021. URL: https://doi.org/10.1007/s10689-020-00204-2, doi:10.1007/s10689-020-00204-2. This article has 31 citations and is from a peer-reviewed journal.

28. (howaldt2024cornealinfantilemyofibromatosis pages 1-2): Antonia Howaldt, Sandrine Lenglez, Clara Velmans, Anne Maria Schultheis, Thomas Clahsen, Mario Matthaei, Jürgen Kohlhase, Christian Vokuhl, Reinhard Büttner, Christian Netzer, Jean-Baptiste Demoulin, and Claus Cursiefen. Corneal infantile myofibromatosis caused by novel activating imatinib-responsive variants in pdgfrb. Ophthalmology Science, 4:100444, May 2024. URL: https://doi.org/10.1016/j.xops.2023.100444, doi:10.1016/j.xops.2023.100444. This article has 4 citations.

29. (dachy2019associationofpdgfrb pages 4-5): Guillaume Dachy, Ronald R. de Krijger, Sylvie Fraitag, Ivan Théate, Bénédicte Brichard, Suma B. Hoffman, Louis Libbrecht, Florence A. Arts, Pascal Brouillard, Miikka Vikkula, Nisha Limaye, and Jean-Baptiste Demoulin. Association of pdgfrb mutations with pediatric myofibroma and myofibromatosis. JAMA dermatology, 155:946, Aug 2019. URL: https://doi.org/10.1001/jamadermatol.2019.0114, doi:10.1001/jamadermatol.2019.0114. This article has 70 citations and is from a domain leading peer-reviewed journal.

30. (hettmer2021genetictestingand pages 3-5): Simone Hettmer, Guillaume Dachy, Guido Seitz, Abbas Agaimy, Catriona Duncan, Marjolijn Jongmans, Steffen Hirsch, Iris Kventsel, Uwe Kordes, Ronald R. de Krijger, Markus Metzler, Orli Michaeli, Karolina Nemes, Anna Poluha, Tim Ripperger, Alexandra Russo, Stephanie Smetsers, Monika Sparber-Sauer, Eveline Stutz, Franck Bourdeaut, Christian P. Kratz, and Jean-Baptiste Demoulin. Genetic testing and surveillance in infantile myofibromatosis: a report from the siope host genome working group. Familial Cancer, 20:327-336, Sep 2021. URL: https://doi.org/10.1007/s10689-020-00204-2, doi:10.1007/s10689-020-00204-2. This article has 31 citations and is from a peer-reviewed journal.

31. (howaldt2024cornealinfantilemyofibromatosis pages 2-3): Antonia Howaldt, Sandrine Lenglez, Clara Velmans, Anne Maria Schultheis, Thomas Clahsen, Mario Matthaei, Jürgen Kohlhase, Christian Vokuhl, Reinhard Büttner, Christian Netzer, Jean-Baptiste Demoulin, and Claus Cursiefen. Corneal infantile myofibromatosis caused by novel activating imatinib-responsive variants in pdgfrb. Ophthalmology Science, 4:100444, May 2024. URL: https://doi.org/10.1016/j.xops.2023.100444, doi:10.1016/j.xops.2023.100444. This article has 4 citations.

32. (lu2023prenatalgeneticdiagnosis media ef3ffef0): Yan Lü, Yulin Jiang, Huanwen Wu, Qingwei Qi, Xiya Zhou, Qi Guo, Na Hao, Juntao Liu, and Hua Meng. Prenatal genetic diagnosis of disseminated infantile myofibromatosis: a case report and literature review. BMC Medical Genomics, Aug 2023. URL: https://doi.org/10.1186/s12920-023-01612-w, doi:10.1186/s12920-023-01612-w. This article has 1 citations and is from a peer-reviewed journal.

33. (wu2021theinfantilemyofibromatosis pages 1-3): Dan Wu, Sailan Wang, Daniel V. Oliveira, Francesca Del Gaudio, Michael Vanlandewijck, Thibaud Lebouvier, Christer Betsholtz, Jian Zhao, ShaoBo Jin, Urban Lendahl, and Helena Karlström. The infantile myofibromatosis notch3 l1519p mutation leads to hyperactivated ligand-independent notch signaling and increased pdgfrb expression. Disease Models &amp; Mechanisms, Feb 2021. URL: https://doi.org/10.1242/dmm.046300, doi:10.1242/dmm.046300. This article has 20 citations and is from a domain leading peer-reviewed journal.
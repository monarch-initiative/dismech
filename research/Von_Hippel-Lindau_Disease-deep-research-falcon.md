---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T23:17:20.022257'
end_time: '2026-04-05T23:24:59.252007'
duration_seconds: 459.23
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Von Hippel-Lindau Disease
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 36
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Von Hippel-Lindau Disease
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Von Hippel-Lindau Disease** covering all of the
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
- **Disease Name:** Von Hippel-Lindau Disease
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Von Hippel-Lindau Disease** covering all of the
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


# Von Hippel–Lindau (VHL) Disease — Comprehensive Disease Characteristics Report (focus on 2023–2024)

## Target Disease
- **Disease name:** Von Hippel–Lindau disease / Von Hippel–Lindau syndrome (VHL disease)
- **Category:** Autosomal-dominant hereditary tumor predisposition syndrome / multiple neoplasia syndrome (hereditary cancer syndrome) (gomezvirgilio2024geneticspathophysiologyand pages 1-2, alvarez2024germlinevariantsin pages 1-2)

## Executive summary (current understanding)
Von Hippel–Lindau (VHL) disease is an autosomal-dominant, multisystem tumor predisposition syndrome caused by germline pathogenic variants in **VHL**, followed by somatic inactivation of the remaining allele in susceptible tissues (two-hit tumor suppressor model). Loss of pVHL function stabilizes hypoxia-inducible factor α (HIFα), especially HIF2α, activating angiogenic and metabolic programs that drive characteristic tumors (e.g., CNS/retinal hemangioblastomas, clear-cell renal cell carcinoma, pheochromocytoma/paraganglioma, pancreatic lesions). (gomezvirgilio2024geneticspathophysiologyand pages 1-2, kaelin2022vonhippel–lindaudisease pages 1-2)

Recent developments relevant to 2023–2024 include: (i) expanded **real-world epidemiology and cost** estimates from U.S. claims data for VHL-CNS hemangioblastoma and VHL-pNET (Feb 2024) (jonasch2024epidemiologyandeconomic pages 1-2); (ii) continued maturation of **HIF-2α inhibition** with belzutifan, including detailed pancreatic lesion outcomes from LITESPARK-004 (Feb 2024) (else2024belzutifanforvon pages 5-6); and (iii) mechanistic expansion of pVHL biology beyond canonical HIF regulation, including a **HIF-independent m6A RNA methylation mechanism** impacting PI3K/AKT signaling (Apr 2024) (zhang2024vonhippellindau pages 1-2).

---

## 1. Disease Information

### 1.1 Definition/overview
VHL disease is a rare, inherited tumor predisposition syndrome characterized by development of benign and malignant tumors and cysts across multiple organs (CNS, retina, kidneys, pancreas, adrenals, and others). (gomezvirgilio2024geneticspathophysiologyand pages 1-2, kaelin2022vonhippel–lindaudisease pages 1-2)

### 1.2 Key identifiers (as explicitly available in retrieved sources)
- **OMIM (disease):** *Von Hippel-Lindau syndrome* **OMIM #193300** (alvarez2024germlinevariantsin pages 1-2)
- **OMIM (gene):** **VHL** tumor suppressor gene **OMIM *608537** (alvarez2024germlinevariantsin pages 1-2)
- **ICD-10:** **Q85.83** (as used to define a cohort in a TriNetX real-world analysis) (hochberg2024isthetrinetx pages 1-2)

**Not available from the retrieved evidence excerpts:** Orphanet ORPHA code, MeSH unique ID, MONDO ID, ICD-11 code. These would normally be sourced from Orphanet/MeSH/MONDO directly, but they were not present in the accessible text segments used here (alvarez2024germlinevariantsin pages 1-2, gomezvirgilio2024geneticspathophysiologyand pages 1-2, hochberg2024isthetrinetx pages 1-2).

### 1.3 Synonyms/alternative names
Explicitly used name variants in retrieved sources include:
- “Von Hippel–Lindau disease” / “von Hippel–Lindau (VHL) disease” / “VHL disease” / “VHL” (gomezvirgilio2024geneticspathophysiologyand pages 1-2)
- “Von Hippel-Lindau syndrome” / “VHL syndrome” (alvarez2024germlinevariantsin pages 1-2)
- “Von Hippel–Lindau (vHL) disease” / “vHL” (hochberg2024isthetrinetx pages 1-2)

### 1.4 Evidence provenance
The report synthesizes **aggregated disease-level reviews** (e.g., 2024 Diagnostics review; 2022 JCI review) and **primary/real-world studies** (claims-based epidemiology; clinical trial report; cohort analyses). (jonasch2024epidemiologyandeconomic pages 1-2, else2024belzutifanforvon pages 5-6, gomezvirgilio2024geneticspathophysiologyand pages 1-2, kaelin2022vonhippel–lindaudisease pages 1-2, zhang2024vonhippellindau pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
- **Primary cause:** Germline pathogenic variants in **VHL**, consistent with autosomal-dominant tumor predisposition; pVHL is a tumor suppressor that regulates HIFα stability via a Cullin2-based E3 ubiquitin ligase complex. (gomezvirgilio2024geneticspathophysiologyand pages 1-2, kaelin2022vonhippel–lindaudisease pages 1-2)
- **Mechanistic core:** Under normoxia, prolyl hydroxylases (PHD/EglN family) hydroxylate HIFα, enabling pVHL recognition and proteasomal degradation; VHL loss leads to HIF accumulation and transcriptional activation of pro-tumor programs. (gomezvirgilio2024geneticspathophysiologyand pages 11-13, kaelin2022vonhippel–lindaudisease pages 1-2)

### 2.2 Risk factors
- **Genetic:** Carrying a germline VHL pathogenic variant is the dominant risk factor; penetrance of manifestations is reported as ~97% by age 65 in a 2024 review. (gomezvirgilio2024geneticspathophysiologyand pages 1-2)
- **De novo mutations:** Up to ~20% of cases may arise from new (de novo) mutations (review-level estimate). (gomezvirgilio2024geneticspathophysiologyand pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No explicit protective factors or gene–environment interaction data were identifiable in the retrieved evidence excerpts.

### 2.4 Modifier genes (emerging)
A 2023 case-based genetic analysis suggests that additional germline variants (e.g., **CHEK2**) may contribute to unusually severe hemangioblastoma burden in some families, consistent with a modifier model; however, this is currently case-report level and not established for broad risk stratification. (gomezvirgilio2024geneticspathophysiologyand pages 11-13)

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Major tumor/lesion types (with frequencies where available)
From a 2024 U.S. claims-based study (background frequencies drawn from prior literature in that paper):
- **CNS hemangioblastoma:** occurs in ~**70–80%** of cases; described as “typically the first manifestation.” (jonasch2024epidemiologyandeconomic pages 1-2)
- **Pancreatic neuroendocrine tumors (pNET):** occur in ~**9–17%** of cases. (jonasch2024epidemiologyandeconomic pages 1-2)

From a 2023 cohort/review focused on VHL-related pancreatic neuroendocrine tumor and diagnostic criteria:
- vPNET prevalence across cohorts reported as **~5% on average**, up to **17%** in some cohorts. (halperin2023uniquecharacteristicsof pages 1-2)

Additional classic manifestations described across sources include retinal hemangioblastomas, clear-cell RCC, pheochromocytoma/paraganglioma (PPGL), pancreatic cystic lesions, endolymphatic sac tumors, and reproductive-tract cystadenomas. (gomezvirgilio2024geneticspathophysiologyand pages 1-2, halperin2023uniquecharacteristicsof pages 1-2)

### 3.2 Onset and progression (selected quantitative data)
- Review-level estimate: **median age of onset 26 years**. (gomezvirgilio2024geneticspathophysiologyand pages 1-2)
- Pediatric PPGL registry data: mean age at first PPGL **12.4 ± 0.41 years** (range **4–18**); recurrences were common (**46%**). (kotsis2024surveillanceinchildren pages 1-2)

### 3.3 Quality-of-life impacts
While the excerpts do not include validated QoL scales (e.g., SF-36/EQ-5D), the 2024 claims-based analysis and pediatric registry data emphasize high healthcare utilization, repeated procedures, and recurrence (especially PPGL), implying significant burden and care intensity. (jonasch2024epidemiologyandeconomic pages 1-2, kotsis2024surveillanceinchildren pages 1-2)

### 3.4 Suggested HPO terms (non-exhaustive; based on explicitly mentioned manifestations)
- CNS hemangioblastoma (HP term suggestion): **Hemangioblastoma**
- Retinal hemangioblastoma: **Retinal hemangioblastoma / retinal capillary hemangioma**
- Clear cell renal cell carcinoma: **Renal cell carcinoma**
- Pheochromocytoma/paraganglioma: **Pheochromocytoma**, **Paraganglioma**
- Pancreatic neuroendocrine tumor: **Pancreatic neuroendocrine tumor**

Note: Specific HPO IDs were not present in the retrieved excerpts; mapping to exact HP identifiers would require HPO lookup outside the retrieved papers.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **VHL** (tumor suppressor); gene OMIM *608537 (alvarez2024germlinevariantsin pages 1-2).

### 4.2 Variant spectrum and inheritance
- **Inheritance:** autosomal dominant (explicitly stated in multiple sources). (gomezvirgilio2024geneticspathophysiologyand pages 1-2, alvarez2024germlinevariantsin pages 1-2)
- **Variant classes:** reviews describe deletions and mutations and emphasize two-hit inactivation as the tumorigenic mechanism. (gomezvirgilio2024geneticspathophysiologyand pages 1-2, gomezvirgilio2024geneticspathophysiologyand pages 11-13)

### 4.3 Penetrance and expressivity
- Review-level estimate: ~**97% penetrance** by age 65. (gomezvirgilio2024geneticspathophysiologyand pages 1-2)

### 4.4 Somatic vs germline
- Germline VHL alteration defines inherited VHL disease; tumors typically arise after somatic inactivation of the remaining allele (loss of heterozygosity concept is discussed in mechanistic reviews). (ohh2022hypoxiainduciblefactorunderlies pages 1-2)

---

## 5. Environmental Information
No clear environmental/lifestyle/infectious triggers were identified in the retrieved evidence excerpts as causal or modifying factors for VHL disease.

---

## 6. Mechanism / Pathophysiology (causal chains; upstream→downstream)

### 6.1 Canonical pVHL–HIF axis (core mechanism)
**Upstream trigger:** germline VHL loss-of-function variant + somatic “second hit” in susceptible cells (tumor suppressor model). (kaelin2022vonhippel–lindaudisease pages 1-2, ohh2022hypoxiainduciblefactorunderlies pages 1-2)

**Core molecular mechanism:** pVHL is the substrate-recognition subunit of a Cullin2-based E3 ubiquitin ligase that targets hydroxylated HIFα for proteasomal degradation in oxygen-dependent fashion; VHL loss stabilizes HIFα, especially HIF2α. (kaelin2022vonhippel–lindaudisease pages 1-2, gomezvirgilio2024geneticspathophysiologyand pages 11-13)

**Downstream consequences:** stabilized HIFα translocates to the nucleus, dimerizes with HIFβ, and activates gene expression programs promoting angiogenesis, altered metabolism, and tumor growth, helping explain the vascular nature of many VHL-associated tumors. (gomezvirgilio2024geneticspathophysiologyand pages 11-13)

**Therapeutic connection:** VEGF pathway inhibitors are a mainstay of ccRCC treatment; an allosteric HIF2 inhibitor (belzutifan) is approved for VHL-associated ccRCC based on this mechanistic dependency. (kaelin2022vonhippel–lindaudisease pages 1-2)

### 6.2 mTORC1 activation via pVHL loss (HIF-independent link)
A review and supporting primary data describe a **HIF-independent** mechanism: VHL can repress **RAPTOR** and thereby inhibit **mTORC1** signaling; loss of VHL derepresses mTORC1, which is frequently hyperactivated in ccRCC. (ganner2021vhlsuppressesraptor pages 1-2, gomezvirgilio2024geneticspathophysiologyand pages 11-13)

### 6.3 2024 mechanistic development: VHL control of m6A RNA methylation (HIF-independent)
A 2024 JCI mechanistic study reports that VHL binds and promotes **METTL3/METTL14** complex formation; VHL depletion suppresses m6A modification. The study identifies **PIK3R3** as a VHL–m6A-regulated target whose mRNA stability is controlled in an **m6A-dependent but HIF-independent** manner; PIK3R3 suppresses renal tumor growth by restraining **PI3K/AKT** signaling. (zhang2024vonhippellindau pages 1-2)

### 6.4 Suggested pathway/ontology terms (based on mechanisms described)
- **GO Biological Process (suggestions):** hypoxia response / oxygen sensing; ubiquitin-dependent protein catabolic process; regulation of angiogenesis; regulation of mTOR signaling; RNA methylation (m6A); PI3K/AKT signaling regulation.
- **Cell types (CL suggestions):** renal tubular epithelial cells; chromaffin cells (for PPGL); retinal vascular-associated cells; CNS vascular-associated stromal cells.

Exact GO/CL identifiers were not present in the retrieved excerpts and would require ontology lookup.

---

## 7. Anatomical Structures Affected (multi-organ)
Across sources, VHL disease affects:
- **CNS (brain/spinal cord):** CNS hemangioblastomas (jonasch2024epidemiologyandeconomic pages 1-2)
- **Eye/retina:** retinal hemangioblastomas (halperin2023uniquecharacteristicsof pages 1-2)
- **Kidney:** cysts and clear-cell RCC (halperin2023uniquecharacteristicsof pages 1-2)
- **Pancreas:** pancreatic lesions including pNETs and serous cystadenomas (else2024belzutifanforvon pages 5-6)
- **Adrenal/paraganglia:** pheochromocytoma/paraganglioma (halperin2023uniquecharacteristicsof pages 1-2)

---

## 8. Temporal Development (onset, course)
- Manifestations may begin in childhood/adolescence (e.g., PPGL, CNS lesions), with progressive emergence of additional lesions over time and frequent need for serial interventions. (kotsis2024surveillanceinchildren pages 1-2, knoblauch2024screeningandsurveillance pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent data and statistics)
**Disease-level prevalence estimates (review):** prevalence described as approximately **1 in 36,000** worldwide in a 2024 review; another estimate range given is **1 in 39,000 to 1 in 91,000**. (gomezvirgilio2024geneticspathophysiologyand pages 1-2, gomezvirgilio2024geneticspathophysiologyand pages 22-24)

**U.S. real-world prevalence for selected VHL manifestations (claims-based, 2019):**
- VHL-associated CNS hemangioblastoma: **1.12 per 100,000** (estimated **3,678** patients)
- VHL-associated pancreatic NET: **0.12 per 100,000** (estimated **389** patients) (jonasch2024epidemiologyandeconomic pages 1-2)

### 9.2 Penetrance
- **~97%** by age 65 (review-level). (gomezvirgilio2024geneticspathophysiologyand pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical diagnostic criteria (recent comparative analysis)
A 2023 study highlights that VHL can be clinically diagnosed via differing criteria sets (International vs Danish) and argues for **genetic testing** to improve diagnostic accuracy, especially in visceral-only presentations. In their cohort, vPNET patients meeting International Criteria had **90%** germline VHL PV and **70%** family history vs **20%** and **10%** in Danish-only cases. (halperin2023uniquecharacteristicsof pages 1-2)

### 10.2 Imaging and screening/surveillance (recent consensus and cohorts)

#### Updated pediatric/adolescent surveillance recommendations (2023 AACR workshop update summarized in 2025)
- **Blood pressure:** at all visits starting at **2 years** (rednam2025updateonsurveillance pages 8-10)
- **PPGL biochemistry:** annual fractionated metanephrines starting at **5 years** (plasma or 24-hour urine) (rednam2025updateonsurveillance pages 8-10, rednam2025updateonsurveillance pages 11-13)
- **Abdominal MRI (RCC/PanNET):** contrast MRI **every 2 years** starting at **15 years** (rednam2025updateonsurveillance pages 11-13, rednam2025updateonsurveillance pages 13-13)
- **Brain/spine MRI:** recommendations vary by consensus group; once started, **biennial** imaging is consistently supported (rednam2025updateonsurveillance pages 8-10)
- **Ophthalmology:** at least annual examinations from diagnosis; in younger children, as often as every 6 months may be considered (rednam2025updateonsurveillance pages 8-10)
- **Audiology:** strategies differ (e.g., biennial from 11 years vs annual age 5–13 then biennial) (rednam2025updateonsurveillance pages 8-10)

#### 2024 pediatric CNS cohort evidence
A 2024 pediatric cohort recommends starting CNS MRI at **12 years** with intervals every **(1–)2 years** depending on involvement; truncating variants showed higher manifestation and surgery rates (HR 3.7 and 3.3). (knoblauch2024screeningandsurveillance pages 1-2)

### 10.3 Biomarkers/labs
The surveillance update explicitly uses **fractionated metanephrines** (plasma or urine) as screening biochemistry for PPGL beginning at age 5. (rednam2025updateonsurveillance pages 11-13)

---

## 11. Outcome / Prognosis
- A 2023 clinical/review source notes leading causes of death as CNS hemangioblastoma followed by RCC (cohort/review-level statement). (halperin2023uniquecharacteristicsof pages 1-2)
- The 2024 U.S. claims study demonstrates substantial healthcare utilization and higher annual costs relative to controls, reflecting chronic morbidity and repeated interventions. (jonasch2024epidemiologyandeconomic pages 1-2)

Survival curves and life expectancy estimates were not present in the retrieved excerpts.

---

## 12. Treatment

### 12.1 Standard interventions (real-world implementation)
For selected lesion types, management commonly involves surveillance with intervention thresholds:
- CNS hemangioblastoma: active surveillance for asymptomatic lesions; surgery for symptomatic or CSF-obstructing lesions (as summarized in the 2024 claims-based study background). (jonasch2024epidemiologyandeconomic pages 1-2)
- pNET: lesions **>2–3 cm** recommended for surgical removal (background statement in 2024 claims-based study). (jonasch2024epidemiologyandeconomic pages 1-2)

### 12.2 Targeted systemic therapy — HIF-2α inhibition (belzutifan)
**Mechanistic rationale:** HIF2 drives VHL-defective ccRCC growth; HIF2 inhibition is mechanistically aligned with the central VHL pathway. (kaelin2022vonhippel–lindaudisease pages 1-2)

**Key 2024 clinical trial evidence (pancreatic lesions, LITESPARK-004):**
- Study: single-arm phase 2 **LITESPARK-004 (NCT03401788)**, belzutifan 120 mg once daily. (else2024belzutifanforvon pages 5-6)
- Pancreatic lesion population: **61/61 (100%)** had ≥1 pancreatic lesion; **22/61 (36%)** had measurable pNET at baseline; median follow-up **37.8 months**. (else2024belzutifanforvon pages 5-6)
- **Objective response rate (ORR):** pancreatic lesions **84% (51/61)** with **17 complete responses**; pNETs **91% (20/22)** with **7 complete responses**. (else2024belzutifanforvon pages 5-6)
- Safety: **18%** had ≥1 grade 3 treatment-related AE; **no grade 4/5** treatment-related AEs reported. (else2024belzutifanforvon pages 5-6)

**Real-world relevance:** A 2024 U.S. claims analysis highlights the high costs of surgery for VHL-CNS hemangioblastoma and VHL-pNET, providing a health-economic rationale for effective medical therapies that could reduce surgical frequency/burden. (jonasch2024epidemiologyandeconomic pages 1-2)

### 12.3 Suggested treatment ontology terms
- **CHEBI (example):** belzutifan (small-molecule HIF-2α inhibitor; CHEBI ID not provided in excerpts)
- **MAXO (suggestions):** MRI surveillance; surgical resection; tumor ablation; targeted molecular therapy (HIF-2α inhibition); biochemical screening (metanephrines).

---

## 13. Prevention

### 13.1 Primary prevention
Not applicable in the classic infectious/toxic exposure sense; VHL is a genetic condition.

### 13.2 Secondary prevention (surveillance as prevention of complications)
The updated pediatric/adolescent surveillance framework (blood pressure, metanephrines, eye exams, MRIs) is a central preventive strategy intended to enable early detection and timely intervention. (rednam2025updateonsurveillance pages 8-10, rednam2025updateonsurveillance pages 11-13, rednam2025updateonsurveillance pages 13-13, knoblauch2024screeningandsurveillance pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring non-human VHL disease analogs were identified in the retrieved excerpts.

---

## 15. Model organisms
Evidence excerpts supporting models/mechanistic conservation include:
- **C. elegans:** loss of vhl-1 increased mTORC1 activity, supporting evolutionary conservation of VHL–mTORC1 regulation. (ganner2021vhlsuppressesraptor pages 1-2)

Detailed mouse/zebrafish models for VHL-associated tumor phenotypes were not available in the retrieved evidence excerpts used for citations in this report.

---

## Recent developments (2023–2024 highlights)
1. **Claims-based U.S. epidemiology and economic burden (Feb 2024):** prevalence estimates for VHL-CNS hemangioblastoma and VHL-pNET in 2019 and quantification of excess annual costs (+$49,645 and +$56,580, respectively). (jonasch2024epidemiologyandeconomic pages 1-2)
2. **Belzutifan efficacy in VHL pancreatic lesions (Feb 2024):** high ORR/CR rates in pancreatic lesions and measurable pNETs with long follow-up and manageable safety. (else2024belzutifanforvon pages 5-6)
3. **HIF-independent pVHL mechanism via m6A (Apr 2024):** VHL regulation of METTL3/METTL14 complex formation and m6A-dependent stabilization of PIK3R3 as a brake on PI3K/AKT-driven tumorigenesis. (zhang2024vonhippellindau pages 1-2)

---

## Embedded quantitative summary table
| Topic | Key data (numbers) | Population/setting | Source (first author, year, journal) | DOI/URL |
|---|---|---|---|---|
| Population prevalence / penetrance / onset | Worldwide prevalence ≈ **1 in 36,000**; median age of onset **26 years**; penetrance of manifestations **~97% by age 65**; **up to 20%** de novo cases (gomezvirgilio2024geneticspathophysiologyand pages 1-2) | Disease-level review of VHL syndrome | Gómez-Virgilio, 2024, *Diagnostics* | https://doi.org/10.3390/diagnostics14171909 |
| Alternative prevalence estimates | Prevalence estimated **1 in 39,000 to 1 in 91,000** (gomezvirgilio2024geneticspathophysiologyand pages 22-24) | Disease-level review | Gómez-Virgilio, 2024, *Diagnostics* | https://doi.org/10.3390/diagnostics14171909 |
| Major phenotype frequencies | CNS hemangioblastoma occurs in **70–80%** of cases; pancreatic NETs in **9–17%** (jonasch2024epidemiologyandeconomic pages 1-2) | U.S. claims-based epidemiology background summary | Jonasch, 2024, *Orphanet Journal of Rare Diseases* | https://doi.org/10.1186/s13023-024-03060-w |
| vPNET frequency and mortality context | vPNET prevalence averages **~5%**, up to **17%** in some cohorts; leading causes of death reported as CNS hemangioblastoma then RCC (halperin2023uniquecharacteristicsof pages 1-2) | Cohort and review of diagnostic criteria in VHL patients with pNET comparison | Halperin, 2023, *Cancers* | https://doi.org/10.3390/cancers15061657 |
| U.S. real-world prevalence of VHL manifestations | 2019 prevalence: VHL-associated CNS hemangioblastoma **1.12/100,000** (**3,678** patients); VHL-associated pNET **0.12/100,000** (**389** patients) (jonasch2024epidemiologyandeconomic pages 1-2) | Optum Clinformatics claims, United States | Jonasch, 2024, *Orphanet Journal of Rare Diseases* | https://doi.org/10.1186/s13023-024-03060-w |
| Economic burden | Annual healthcare costs vs controls: VHL-CNS-Hb **+$49,645**; VHL-pNET **+$56,580** (jonasch2024epidemiologyandeconomic pages 1-2) | U.S. matched claims cohorts: VHL-CNS-Hb **N=220**; VHL-pNET **N=20** | Jonasch, 2024, *Orphanet Journal of Rare Diseases* | https://doi.org/10.1186/s13023-024-03060-w |
| Diagnostic criteria cohort data | Among vPNET patients meeting International Criteria: germline VHL pathogenic variant **90%** and family history **70%** vs Danish-only group **20%** and **10%**; vPNET diagnosis age **51.6 ± 4.1** vs sporadic PNET **62.8 ± 1.5** years (halperin2023uniquecharacteristicsof pages 1-2) | 33 VHL patients (20 vPNET) and 65 sporadic PNET comparators | Halperin, 2023, *Cancers* | https://doi.org/10.3390/cancers15061657 |
| Pediatric PPGL timing / recurrence | Mean age at first PPGL **12.4 ± 0.41 years** (range **4–18**); recurrence **46%**; other tumors during follow-up: hemangioblastomas **73%**, retinal angiomas **58%**, RCC **21%**, pNET **12%** (kotsis2024surveillanceinchildren pages 1-2) | German pediatric/adolescent VHL registries, **75** patients | Kotsis, 2024, *Journal of Kidney Cancer and VHL* | https://doi.org/10.15586/jkcvhl.v11i4.362 |
| Pediatric CNS hemangioblastoma surveillance | Start MRI at age **12 years**; repeat every **1–2 years** depending on CNS involvement; truncating variants had higher manifestation rate (**HR 3.7**, 95% CI 1.9–7.4) and surgery rate (**HR 3.3**, 95% CI 1.2–8.9) (knoblauch2024screeningandsurveillance pages 1-2) | Monocentric pediatric cohort, **99** VHL patients | Knoblauch, 2024, *Journal of Neuro-Oncology* | https://doi.org/10.1007/s11060-024-04676-5 |
| Updated pediatric/adolescent surveillance: blood pressure & PCC biochemistry | Blood pressure at all visits starting at **2 years**; annual fractionated metanephrines starting at **5 years**; test for PCC before major surgery (rednam2025updateonsurveillance pages 8-10, rednam2025updateonsurveillance pages 11-13) | 2023 AACR Childhood Cancer Predisposition Workshop update summarized in 2025 perspective | Rednam, 2025, *Clinical Cancer Research* | https://doi.org/10.1158/1078-0432.CCR-24-3525 |
| Updated surveillance: ophthalmology / audiology / neuroimaging | Eye exams at least **annually from diagnosis**; in younger children, every **6 months** may be considered. Audiograms: **biennial from 11 years** (Daniels) or **annual age 5–13 then biennial** (Binderup). Brain/spine MRI: baseline at **10 years** then, if negative, resume at **15 years** and continue **biennially**, or begin **biennial MRI at 11 years** depending on guideline set (rednam2025updateonsurveillance pages 8-10) | Comparative consensus recommendations summarized in AACR update | Rednam, 2025, *Clinical Cancer Research* | https://doi.org/10.1158/1078-0432.CCR-24-3525 |
| Updated surveillance: abdominal MRI | Contrast abdominal MRI for RCC/PanNET every **2 years** starting at **15 years** (rednam2025updateonsurveillance pages 11-13, rednam2025updateonsurveillance pages 13-13) | Pediatric/adolescent surveillance update | Rednam, 2025, *Clinical Cancer Research* | https://doi.org/10.1158/1078-0432.CCR-24-3525 |
| Local pediatric registry surveillance practice | Annual hormone measurements; eye exam starting at **6 years**; CNS/abdominal MRI starting at **12 years**; regular screening may begin at **5 years** in known variant families; intervals **1–2 years** depending on stage/risk (kotsis2024surveillanceinchildren pages 1-2) | Freiburg-VHL screening/surveillance program | Kotsis, 2024, *Journal of Kidney Cancer and VHL* | https://doi.org/10.15586/jkcvhl.v11i4.362 |
| Belzutifan phase 2 trial design | LITESPARK-004 / **NCT03401788**; adults with germline VHL alteration; **61** patients enrolled; belzutifan **120 mg once daily**; endpoints included ORR, DOR, PFS, linear growth rate, safety (else2024belzutifanforvon pages 5-6) | Single-arm phase 2 VHL disease study | Else, 2024, *Clinical Cancer Research* | https://doi.org/10.1158/1078-0432.CCR-23-2592 |
| Belzutifan pancreatic lesion efficacy | All **61/61 (100%)** had ≥1 pancreatic lesion; **22/61 (36%)** had measurable pNET at baseline; median follow-up **37.8 months**; ORR **84% (51/61)** in pancreatic lesions with **17 complete responses**; ORR **91% (20/22)** in pNETs with **7 complete responses**; median pNET linear growth rate **−4.2 mm/year**; grade 3 treatment-related AEs **18%**; no grade 4/5 treatment-related AEs (else2024belzutifanforvon pages 5-6) | Pancreatic lesion population of LITESPARK-004 | Else, 2024, *Clinical Cancer Research* | https://doi.org/10.1158/1078-0432.CCR-23-2592 |


*Table: This table compiles the key 2023-2025 quantitative findings and surveillance recommendations extracted so far for von Hippel–Lindau disease. It emphasizes epidemiology, phenotype frequency, pediatric surveillance timing, and belzutifan phase 2 efficacy data relevant for a disease knowledge base.*

---

## Notes on evidence limitations (for knowledge base curation)
- Many requested ontology IDs (MONDO, MeSH, Orphanet) and some phenotype-specific HPO IDs were not explicitly present in the accessible excerpts and therefore could not be safely asserted here.
- Survival/life expectancy statistics and standardized QoL instrument outcomes were not present in the retrieved excerpts.
- While belzutifan and surveillance are strongly supported with recent data, quantitative outcomes for many local interventions (e.g., stereotactic radiosurgery, ablation modalities) were not available in the extracted evidence.


References

1. (gomezvirgilio2024geneticspathophysiologyand pages 1-2): Laura Gómez-Virgilio, Mireya Velazquez-Paniagua, Lucero Cuazozon-Ferrer, Maria-del-Carmen Silva-Lucero, Andres-Ivan Gutierrez-Malacara, Juan-Ramón Padilla-Mendoza, Jessica Borbolla-Vázquez, Job-Alí Díaz-Hernández, Fausto-Alejandro Jiménez-Orozco, and Maria-del-Carmen Cardenas-Aguayo. Genetics, pathophysiology, and current challenges in von hippel–lindau disease therapeutics. Diagnostics, 14:1909, Aug 2024. URL: https://doi.org/10.3390/diagnostics14171909, doi:10.3390/diagnostics14171909. This article has 8 citations.

2. (alvarez2024germlinevariantsin pages 1-2): Antonio Alejandro Esperón Álvarez, Inés Virginia Noa Hechavarría, Ixchel López Reyes, and Teresa Collazo Mesa. Germline variants in the von hippel-lindau tumor suppressor gene in cuban patients. Egyptian Journal of Medical Human Genetics, Mar 2024. URL: https://doi.org/10.1186/s43042-024-00506-5, doi:10.1186/s43042-024-00506-5. This article has 0 citations and is from a peer-reviewed journal.

3. (kaelin2022vonhippel–lindaudisease pages 1-2): William G. Kaelin. Von hippel–lindau disease: insights into oxygen sensing, protein degradation, and cancer. The Journal of Clinical Investigation, Sep 2022. URL: https://doi.org/10.1172/jci162480, doi:10.1172/jci162480. This article has 151 citations.

4. (jonasch2024epidemiologyandeconomic pages 1-2): Eric Jonasch, Yan Song, Jonathan Freimark, Richard Berman, Ha Nguyen, James Signorovitch, and Murali Sundaram. Epidemiology and economic burden of von hippel-lindau disease-associated central nervous system hemangioblastomas and pancreatic neuroendocrine tumors in the united states. Orphanet Journal of Rare Diseases, Feb 2024. URL: https://doi.org/10.1186/s13023-024-03060-w, doi:10.1186/s13023-024-03060-w. This article has 7 citations and is from a peer-reviewed journal.

5. (else2024belzutifanforvon pages 5-6): Tobias Else, Eric Jonasch, Othon Iliopoulos, Kathryn E. Beckermann, Vivek Narayan, Benjamin L. Maughan, Stephane Oudard, Jodi K. Maranchie, Ane B. Iversen, Cynthia M. Goldberg, Wei Fu, Rodolfo F. Perini, Yanfang Liu, W. Marston Linehan, and Ramaprasad Srinivasan. Belzutifan for von hippel-lindau disease: pancreatic lesion population of the phase 2 litespark-004 study. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:1750-1757, Feb 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-2592, doi:10.1158/1078-0432.ccr-23-2592. This article has 26 citations.

6. (zhang2024vonhippellindau pages 1-2): Cheng Zhang, Miaomiao Yu, Austin J. Hepperla, Zhao Zhang, Rishi Raj, Hua Zhong, Jin Zhou, Lianxin Hu, Jun Fang, Hongyi Liu, Qian Liang, Liwei Jia, Chengheng Liao, Sichuan Xi, Jeremy M. Simon, Kexin Xu, Zhijie Liu, Yunsun Nam, Payal Kapur, and Qing Zhang. Von hippel lindau tumor suppressor controls m6a-dependent gene expression in renal tumorigenesis. The Journal of Clinical Investigation, Apr 2024. URL: https://doi.org/10.1172/jci175703, doi:10.1172/jci175703. This article has 13 citations.

7. (hochberg2024isthetrinetx pages 1-2): Aaron R. Hochberg, Patrick T. Gomella, Brian Im, Anushka Ghosh, Sohan Shah, Rasheed A.M. Thompson, Kevin K. Zarrabi, Mihir S. Shah, J. Ryan Mark, Joseph K. Izes, Costas D. Lallas, Leonard G. Gomella, and Adam R. Metwalli. Is the trinetx database a good tool for investigation of real-world management of von hippel–lindau? Journal of Kidney Cancer and VHL, 11:28-38, Dec 2024. URL: https://doi.org/10.15586/jkcvhl.v11i4.324, doi:10.15586/jkcvhl.v11i4.324. This article has 4 citations.

8. (gomezvirgilio2024geneticspathophysiologyand pages 11-13): Laura Gómez-Virgilio, Mireya Velazquez-Paniagua, Lucero Cuazozon-Ferrer, Maria-del-Carmen Silva-Lucero, Andres-Ivan Gutierrez-Malacara, Juan-Ramón Padilla-Mendoza, Jessica Borbolla-Vázquez, Job-Alí Díaz-Hernández, Fausto-Alejandro Jiménez-Orozco, and Maria-del-Carmen Cardenas-Aguayo. Genetics, pathophysiology, and current challenges in von hippel–lindau disease therapeutics. Diagnostics, 14:1909, Aug 2024. URL: https://doi.org/10.3390/diagnostics14171909, doi:10.3390/diagnostics14171909. This article has 8 citations.

9. (halperin2023uniquecharacteristicsof pages 1-2): Reut Halperin, Liat Arnon, Yehudit Eden-Friedman, and Amit Tirosh. Unique characteristics of patients with von hippel–lindau disease defined by various diagnostic criteria. Cancers, 15:1657, Mar 2023. URL: https://doi.org/10.3390/cancers15061657, doi:10.3390/cancers15061657. This article has 9 citations.

10. (kotsis2024surveillanceinchildren pages 1-2): Fruzsina Kotsis, Marina Kunstreich, Antje Redlich, Kilian Rhein, Athina Ganner, Gerd Walz, Michaela Kuhlen, and Elke Neumann-Haefelin. Surveillance in children and adolescents with von hippel-lindau (vhl)-related pheochromocytomas and paragangliomas: a survey of met and freiburg-vhl registries in germany. Journal of Kidney Cancer, 11:15-27, Nov 2024. URL: https://doi.org/10.15586/jkcvhl.v11i4.362, doi:10.15586/jkcvhl.v11i4.362. This article has 0 citations.

11. (ohh2022hypoxiainduciblefactorunderlies pages 1-2): Michael Ohh, Cassandra C Taber, Fraser G Ferens, and Daniel Tarade. Hypoxia-inducible factor underlies von hippel-lindau disease stigmata. eLife, Aug 2022. URL: https://doi.org/10.7554/elife.80774, doi:10.7554/elife.80774. This article has 34 citations and is from a domain leading peer-reviewed journal.

12. (ganner2021vhlsuppressesraptor pages 1-2): Athina Ganner, Christina Gehrke, Marinella Klein, Lena Thegtmeier, Tanja Matulenski, Laura Wingendorf, Lu Wang, Felicitas Pilz, Lars Greidl, Lisa Meid, Fruzsina Kotsis, Gerd Walz, Ian J. Frew, and Elke Neumann-Haefelin. Vhl suppresses raptor and inhibits mtorc1 signaling in clear cell renal cell carcinoma. Scientific Reports, Jul 2021. URL: https://doi.org/10.1038/s41598-021-94132-5, doi:10.1038/s41598-021-94132-5. This article has 40 citations and is from a peer-reviewed journal.

13. (knoblauch2024screeningandsurveillance pages 1-2): Anna Laura Knoblauch, Bianca-Ioana Blaß, C. Steiert, N. Neidert, A. Puzik, E. Neumann-Haefelin, A. Ganner, F. Kotsis, T. Schäfer, H.P.H. Neumann, S. Elsheikh, J. Beck, and Jan-Helge Klingler. Screening and surveillance recommendations for central nervous system hemangioblastomas in pediatric patients with von hippel-lindau disease. Journal of Neuro-Oncology, 168:537-545, Apr 2024. URL: https://doi.org/10.1007/s11060-024-04676-5, doi:10.1007/s11060-024-04676-5. This article has 5 citations and is from a peer-reviewed journal.

14. (gomezvirgilio2024geneticspathophysiologyand pages 22-24): Laura Gómez-Virgilio, Mireya Velazquez-Paniagua, Lucero Cuazozon-Ferrer, Maria-del-Carmen Silva-Lucero, Andres-Ivan Gutierrez-Malacara, Juan-Ramón Padilla-Mendoza, Jessica Borbolla-Vázquez, Job-Alí Díaz-Hernández, Fausto-Alejandro Jiménez-Orozco, and Maria-del-Carmen Cardenas-Aguayo. Genetics, pathophysiology, and current challenges in von hippel–lindau disease therapeutics. Diagnostics, 14:1909, Aug 2024. URL: https://doi.org/10.3390/diagnostics14171909, doi:10.3390/diagnostics14171909. This article has 8 citations.

15. (rednam2025updateonsurveillance pages 8-10): Surya P. Rednam, Kerri D. Becktell, Anita Villani, Garrett M. Brodeur, Lisa J. States, Andrea S. Doria, Junne Kamihara, Kami Wolfe Schneider, Stephan D. Voss, Elysa Widjaja, Kristin Zelley, Yoshiko Nakano, Kristian W. Pajtler, Maria Isabel Achatz, David Malkin, Lisa R. Diller, Bailey Gallinger, Chieko Tamura, and Jonathan D. Wasserman. Update on surveillance in von hippel-lindau disease. Clinical cancer research : an official journal of the American Association for Cancer Research, 31:2271-2277, Apr 2025. URL: https://doi.org/10.1158/1078-0432.ccr-24-3525, doi:10.1158/1078-0432.ccr-24-3525. This article has 8 citations.

16. (rednam2025updateonsurveillance pages 11-13): Surya P. Rednam, Kerri D. Becktell, Anita Villani, Garrett M. Brodeur, Lisa J. States, Andrea S. Doria, Junne Kamihara, Kami Wolfe Schneider, Stephan D. Voss, Elysa Widjaja, Kristin Zelley, Yoshiko Nakano, Kristian W. Pajtler, Maria Isabel Achatz, David Malkin, Lisa R. Diller, Bailey Gallinger, Chieko Tamura, and Jonathan D. Wasserman. Update on surveillance in von hippel-lindau disease. Clinical cancer research : an official journal of the American Association for Cancer Research, 31:2271-2277, Apr 2025. URL: https://doi.org/10.1158/1078-0432.ccr-24-3525, doi:10.1158/1078-0432.ccr-24-3525. This article has 8 citations.

17. (rednam2025updateonsurveillance pages 13-13): Surya P. Rednam, Kerri D. Becktell, Anita Villani, Garrett M. Brodeur, Lisa J. States, Andrea S. Doria, Junne Kamihara, Kami Wolfe Schneider, Stephan D. Voss, Elysa Widjaja, Kristin Zelley, Yoshiko Nakano, Kristian W. Pajtler, Maria Isabel Achatz, David Malkin, Lisa R. Diller, Bailey Gallinger, Chieko Tamura, and Jonathan D. Wasserman. Update on surveillance in von hippel-lindau disease. Clinical cancer research : an official journal of the American Association for Cancer Research, 31:2271-2277, Apr 2025. URL: https://doi.org/10.1158/1078-0432.ccr-24-3525, doi:10.1158/1078-0432.ccr-24-3525. This article has 8 citations.

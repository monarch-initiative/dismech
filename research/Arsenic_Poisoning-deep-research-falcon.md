---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T08:50:59.673613'
end_time: '2026-05-08T09:19:48.807697'
duration_seconds: 1729.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Arsenic Poisoning
  mondo_id: ''
  category: Environmental
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Arsenic Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Arsenic Poisoning** covering all of the
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
- **Disease Name:** Arsenic Poisoning
- **MONDO ID:**  (if available)
- **Category:** Environmental

## Research Objectives

Please provide a comprehensive research report on **Arsenic Poisoning** covering all of the
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


# Arsenic Poisoning (Arsenicosis): Disease Characteristics Research Report (Environmental)

## 0. Scope and evidence base
This report synthesizes recent peer‑reviewed literature (prioritizing 2023–2024 where available) on **acute arsenic poisoning** and **chronic arsenic toxicity (arsenicosis)**, focusing on definitions, phenotypes, mechanisms, diagnostics, treatment, prevention, and quantitative risk/outcome data. Evidence is primarily from recent reviews, regulatory risk assessments, and systematic reviews/meta-analyses; where mechanistic details are needed, cellular and model-organism studies are included.

**Important limitation:** Using the available tool-based literature retrieval, explicit **ICD-10/ICD‑11**, **MeSH**, and **MONDO** identifiers were *not present in the retrieved full texts*. Therefore, identifiers are reported as “not found in retrieved sources” rather than inferred.

## 1. Disease Information
### 1.1 Concise overview
**Arsenic poisoning** refers to adverse clinical outcomes resulting from exposure to arsenic compounds, most importantly **inorganic arsenic (iAs)**. Acute intoxication often follows ingestion of iAs and can present within **~30 minutes to 2 hours** with severe gastroenteritis, hypotension, cardiac conduction abnormalities (including QT prolongation), neurologic toxicity (delirium, seizures), and acute kidney injury. (balalimood2025recentadvancesin pages 12-13)

**Chronic arsenic poisoning** is commonly termed **arsenicosis** and results from long-term low-dose exposure, typically via contaminated drinking water and/or diet. It features characteristic dermatologic findings (hyperpigmentation with “raindrop” pattern, palmoplantar hyperkeratosis), peripheral neuropathy, vascular disease, and increased risk of cancers (skin, bladder, lung, and others). (ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13)

### 1.2 Synonyms and alternative names
Chronic arsenic toxicity is explicitly described as **arsenicosis**, historically also called **arseniasis, arsenism, arsenicism**. (ganie2024arsenictoxicitysources pages 2-3)

### 1.3 Key identifiers (ontology/terminology)
- **ICD-10/ICD-11:** Not found in retrieved sources.
- **MeSH:** Not found in retrieved sources.
- **MONDO:** Not found in retrieved sources.

### 1.4 Evidence provenance
The information summarized here is derived from **aggregated disease-level resources** (systematic reviews, regulatory assessments, narrative reviews) and mechanistic/model-system studies, rather than individual EHR extractions. (balalimood2025recentadvancesin pages 12-13, visciano2025arsenicinwater pages 10-12, issanov2023arsenicindrinking pages 1-2)

## 2. Etiology
### 2.1 Causal factors
- **Environmental/toxic exposure:** Exposure to inorganic arsenic species—especially **As(III) (arsenite)** and **As(V) (arsenate)**—from groundwater, food, industrial sources, and in some circumstances inhalational exposures (including **arsine gas**). (balalimood2025recentadvancesin pages 12-13, ganie2024arsenictoxicitysources pages 1-2)
- **Chemical species matter:** Trivalent arsenicals are emphasized as more toxic due to strong interactions with sulfur-containing proteins/thiols. (ganie2024arsenictoxicitysources pages 1-2)

### 2.2 Risk factors
#### Environmental/occupational
- **Drinking-water contamination** is repeatedly highlighted as a principal route in high-burden regions (e.g., South Asia). (ganie2024arsenictoxicitysources pages 1-2)
- **Global burden:** An opinion/global scenario paper reports groundwater arsenic contamination affecting **106 countries** and exposing **~230 million** people (ATSDR 2022 ranking and WHO “top 10 chemicals” framing also noted). (bhat2024arseniccontaminationneeds pages 1-2)

#### Host and contextual risk modifiers
- **Genetic susceptibility:** Inter-individual differences in arsenic metabolism (methylation phenotype) are linked to susceptibility; methylation depends on **AS3MT** and related pathways. (ganie2024arsenictoxicitysources pages 2-3, pullella2024elucidatingtherelationship pages 37-41)
- **Nutritional status / one‑carbon metabolism:** Methyl-donor availability (folate and related nutrients) modifies arsenic methylation capacity and may influence toxicity. (pereira2025arsenomearsenobolomeand pages 20-22, abuawad2023thefolicacid pages 7-8)

### 2.3 Protective factors
- **Nutritional supplementation improving methylation indices (human evidence):** In the FACT trial (Bangladesh; randomized, double-blind, placebo-controlled), folic acid supplementation improved blood arsenic methylation indices and metabolite profiles (increased SMI and %DMAs, decreased %MMAs), suggesting improved detoxification via enhanced methylation. (abuawad2023thefolicacid pages 7-8, abuawad2023thefolicacid pages 1-2)

### 2.4 Gene–environment interactions
- **Mechanistic G×E framing:** Variation in response to arsenic metabolites is genetically regulated in model systems; QTL mapping under MMA(III) exposure implicated detoxification and DNA repair loci (e.g., **Abcc4, Txnrd1, Xrcc2**), supporting gene-by-environment modulation of oxidative stress response and cell death trajectories. (o’connor2024unravelingthegenetics pages 1-2)

## 3. Phenotypes (clinical manifestations)
A structured phenotype-to-HPO mapping is provided in Artifact-01.

| Clinical feature | Acute/Chronic | Description/onset notes | Suggested HPO term(s) | Evidence (citation IDs) |
|---|---|---|---|---|
| Nausea and vomiting | Acute | Common early gastrointestinal manifestations; acute symptoms may begin within ~30 minutes to 2 hours after ingestion | Nausea (HP:0002018); Vomiting (HP:0002013) | (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) |
| Diarrhea | Acute | Prominent early gastroenteritis in acute inorganic arsenic ingestion | Diarrhea (HP:0002014) | (balalimood2025recentadvancesin pages 12-13, balalimood2025recentadvancesin pages 13-14) |
| Abdominal pain | Acute | Early abdominal pain/cramping as part of acute gastroenteritis syndrome | Abdominal pain (HP:0002027) | (balalimood2025recentadvancesin pages 12-13) |
| Dehydration / hypovolemia | Acute | Follows severe vomiting and diarrhea; contributes to shock and mortality | Dehydration (HP:0001944); Hypovolemia | (balalimood2025recentadvancesin pages 12-13, balalimood2025recentadvancesin pages 13-14) |
| Hypotension | Acute | Reported in severe poisoning, often secondary to fluid loss and systemic toxicity | Hypotension (HP:0002615) | (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) |
| QT prolongation / arrhythmia | Acute | ECG abnormalities include prolonged QT and other conduction disturbances; can progress to torsades/serious arrhythmia | Prolonged QT interval (HP:0005184); Cardiac arrhythmia (HP:0011675) | (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13, pereira2025arsenomearsenobolomeand pages 19-20) |
| Tremor | Acute | Neurologic sign reported in acute intoxication | Tremor (HP:0001337) | (balalimood2025recentadvancesin pages 12-13) |
| Delirium / encephalopathy | Acute | Severe neurotoxicity may include delirium and central nervous system dysfunction | Delirium (HP:0031258); Encephalopathy (HP:0001298) | (balalimood2025recentadvancesin pages 12-13, pereira2025arsenomearsenobolomeand pages 19-20) |
| Seizures | Acute | Can occur in severe poisoning as part of CNS involvement | Seizure (HP:0001250) | (balalimood2025recentadvancesin pages 12-13, balalimood2025recentadvancesin pages 13-14) |
| Proteinuria / hematuria | Acute | Renal involvement in acute poisoning may include urinary abnormalities and acute tubular injury | Proteinuria (HP:0000093); Hematuria (HP:0000790) | (balalimood2025recentadvancesin pages 12-13) |
| Acute kidney injury | Acute | Severe poisoning may cause acute tubular necrosis/renal failure | Acute kidney injury (HP:0031270) | (balalimood2025recentadvancesin pages 12-13, balalimood2025recentadvancesin pages 13-14) |
| Peripheral neuropathy | Subacute/Chronic | Characteristic sensory > motor neuropathy; may appear 2-4 weeks after acute exposure or develop with chronic exposure | Peripheral neuropathy (HP:0009830); Sensory neuropathy (HP:0000763); Motor neuropathy | (balalimood2025recentadvancesin pages 12-13, ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13, pereira2025arsenomearsenobolomeand pages 20-22) |
| Hyperpigmentation | Chronic | Classic skin manifestation, often diffuse or spotted; chronic arsenicosis hallmark | Hyperpigmentation of the skin (HP:0000953) | (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13, pereira2025arsenomearsenobolomeand pages 20-22) |
| Raindrop-pattern pigmentation | Chronic | Characteristic mottled hyper/hypopigmented skin change in chronic arsenic toxicity | Mottled pigmentation | (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) |
| Palmoplantar hyperkeratosis | Chronic | Typical chronic dermal lesion; affects palms and soles | Palmoplantar hyperkeratosis (HP:0000982) | (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13, pereira2025arsenomearsenobolomeand pages 20-22) |
| Desquamation | Chronic | Reported with chronic arsenic-related dermal injury | Desquamation (HP:0001029) | (pereira2025arsenomearsenobolomeand pages 20-22) |
| Mees lines | Chronic | Transverse white nail bands associated with chronic exposure | Leukonychia striata / Mees lines | (balalimood2025recentadvancesin pages 12-13) |
| Cognitive / attention impairment | Chronic | Chronic exposure linked to learning, memory, and attention deficits | Cognitive impairment (HP:0100543); Abnormality of attention | (ganie2024arsenictoxicitysources pages 2-3) |
| Hypertension / vascular disease | Chronic | Chronic exposure associated with peripheral vascular disease and hypertension; Blackfoot disease is a classic severe vascular manifestation | Hypertension (HP:0000822); Peripheral vascular disease; Blackfoot disease | (ganie2024arsenictoxicitysources pages 1-2, pereira2025arsenomearsenobolomeand pages 20-22) |
| Skin cancer | Chronic complication | Chronic inorganic arsenic exposure increases skin cancer risk | Skin neoplasm (HP:0012126) | (balalimood2025recentadvancesin pages 12-13, ganie2024arsenictoxicitysources pages 1-2) |
| Bladder cancer | Chronic complication | Strong epidemiologic association with long-term exposure | Bladder neoplasm (HP:0100747) | (chakif2026heavymetaltoxicity pages 12-13, pereira2025arsenomearsenobolomeand pages 20-22) |
| Lung cancer | Chronic complication | Established chronic carcinogenic outcome of inorganic arsenic exposure | Lung neoplasm (HP:0100526) | (chakif2026heavymetaltoxicity pages 12-13, ganie2024arsenictoxicitysources pages 1-2, pereira2025arsenomearsenobolomeand pages 20-22) |
| Kidney or liver cancer | Chronic complication | Reported among internal malignancies linked to chronic exposure | Renal neoplasm; Hepatic neoplasm | (ganie2024arsenictoxicitysources pages 1-2, pereira2025arsenomearsenobolomeand pages 20-22) |


*Table: This table maps major acute and chronic clinical manifestations of arsenic poisoning to suggested HPO terms for knowledge-base annotation. It emphasizes timing, characteristic arsenicosis features, and long-term cancer complications supported by recent review evidence.*

Key time-course features:
- **Acute:** Symptoms begin ~30 min–2 h after ingestion (GI symptoms prominent) with possible cardiovascular collapse and multi-organ injury. (balalimood2025recentadvancesin pages 12-13)
- **Subacute neurologic:** Sensory deficits may appear **2–4 weeks** post-exposure. (balalimood2025recentadvancesin pages 12-13)
- **Chronic:** Dermatologic and neurologic manifestations plus long-term cancer risks. (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13)

## 4. Genetic/Molecular Information
### 4.1 Causal genes
Arsenic poisoning is not a Mendelian genetic disease; however, **genes that govern arsenic metabolism and response** modify susceptibility. Strongly implicated genes/pathways include:
- **AS3MT** (arsenic methyltransferase) for methylation of iAs to methylated metabolites. (ganie2024arsenictoxicitysources pages 2-3, singh2024arsenicexposurein pages 1-5)
- Detoxification/transport and oxidative stress response genes highlighted in genetic mapping screens under MMA(III) exposure (**Abcc4, Txnrd1**) and DNA repair candidates (**Xrcc2**). (o’connor2024unravelingthegenetics pages 1-2)

### 4.2 Pathogenic variants
Specific human variant pathogenicity classifications (ACMG/ClinVar) were not present in retrieved sources.

### 4.3 Epigenetic information
Chronic iAs exposure is described as producing **epigenetic alterations**, including promoter hypermethylation (e.g., **MLH1/MSH2**), altered DNMT expression (↑DNMT1/DNMT3B, ↓DNMT3A), and global methylation changes linked to SAM depletion. (pereira2025arsenomearsenobolomeand pages 20-22, pullella2024elucidatingtherelationship pages 37-41)

## 5. Environmental Information
### 5.1 Environmental factors
- Major exposure is via **contaminated groundwater** and diet; mining/manufacturing and geogenic sources are emphasized in recent reviews. (ganie2024arsenictoxicitysources pages 1-2)

### 5.2 Lifestyle factors
- Dietary contributions can be substantial; risk assessments distinguish **organic arsenic** from seafood versus **inorganic arsenic** from water/food sources, requiring speciation for interpretation. (chakif2026heavymetaltoxicity pages 12-13, pullella2024elucidatingtherelationship pages 37-41)

## 6. Mechanism / Pathophysiology
A structured mechanism table with ontology mapping is provided in Artifact-03.

| Mechanism (high level) | Molecular details/chain | Example genes/proteins | Suggested GO biological process terms | Suggested CL cell types | Suggested UBERON organs/tissues | Suggested CHEBI entities/arsenic species | Evidence (citation IDs) |
|---|---|---|---|---|---|---|---|
| Toxicokinetic uptake, biotransformation, and distribution | Ingested/inhaled inorganic arsenic is absorbed, distributed systemically, and methylated mainly in liver to MMA and DMA; As(V) enters via phosphate transporters, As(III) via aquaglyceroporins, then binds thiols and undergoes reduction/methylation using GSH, thioredoxin systems, SAM, and AS3MT. Urinary excretion is the main clearance route; skin, hair, nails, bone, and teeth can accumulate arsenic. | **AS3MT**, **TXNRD1**, thioredoxin, glutathione-related proteins, aquaglyceroporins, phosphate transporters | GO:0006730 one-carbon metabolic process; GO:0017144 drug metabolic process; GO:0042493 response to drug; GO:0055085 transmembrane transport | hepatocyte; erythrocyte; renal tubular epithelial cell | liver (UBERON:0002107); kidney (UBERON:0002113); skin (UBERON:0002097); blood (UBERON:0000178) | inorganic arsenic; arsenite(3+) / As(III); arsenate(V) / As(V); monomethylarsonous acid (MMAIII); dimethylarsinic acid (DMA) | (ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13, ganie2024arsenictoxicitysources pages 1-2, pullella2024elucidatingtherelationship pages 37-41) |
| Thiol binding and enzyme inhibition | Trivalent arsenicals bind sulfhydryl/lipoic-acid–dependent enzymes, disrupting central metabolism and redox homeostasis. MMA(III) binds lipoic acid and inhibits pyruvate dehydrogenase; As(V) can substitute for phosphate in metabolic intermediates, impairing ATP-generating reactions. | pyruvate dehydrogenase complex, lipoic acid–dependent enzymes, glyceraldehyde-3-phosphate dehydrogenase | GO:0006099 tricarboxylic acid cycle; GO:0006096 glycolytic process; GO:0046034 ATP metabolic process; GO:0055114 oxidation-reduction process | hepatocyte; cardiomyocyte; neuron | liver (UBERON:0002107); heart (UBERON:0000948); nervous system (UBERON:0001016) | arsenite(3+); arsenate(V); MMAIII; ADP-arsenate; glucose-6-arsenate | (pereira2025arsenomearsenobolomeand pages 19-20, ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13) |
| Oxidative and nitrosative stress | A central initiating event is ROS/RNS generation with lipid, protein, and DNA oxidation; reported biomarkers include MDA, protein carbonyls, and 8-hydroxydeoxyguanosine. MMA(III) and As(III) also interfere with nitric oxide biology, including NOS inhibition and peroxynitrite-related injury. | **TXNRD1**, Nrf2 pathway components, nitric oxide synthase, heme oxygenase, ferritin, metallothionein | GO:0006979 response to oxidative stress; GO:1903409 reactive oxygen species metabolic process; GO:0051409 response to nitrosative stress; GO:0034599 cellular response to oxidative stress | fibroblast; endothelial cell; keratinocyte; neuron | skin (UBERON:0002097); vasculature (UBERON:0004535); lung (UBERON:0002048); kidney (UBERON:0002113) | arsenite(3+); MMAIII; inorganic arsenic | (balalimood2025recentadvancesin pages 12-13, pereira2025arsenomearsenobolomeand pages 19-20, pereira2025arsenomearsenobolomeand pages 20-22, pullella2024elucidatingtherelationship pages 37-41, ganie2024arsenictoxicitysources pages 2-3) |
| NRF2-mediated antioxidant response and detoxification | Genetic and experimental studies identify NRF2-linked antioxidant defense, detoxification, and stress-response programs as major regulated responses to arsenic metabolites. Cellular morphology QTL mapped loci including **Abcc4** and **Txnrd1**, supporting genetically controlled variability in response to MMAIII. | **ABCC4**, **TXNRD1**, NRF2 pathway genes, metallothioneins | GO:0034599 cellular response to oxidative stress; GO:0042744 hydrogen peroxide catabolic process; GO:0006805 xenobiotic metabolic process; GO:0046677 response to antibiotic | fibroblast; hepatocyte; renal epithelial cell | liver (UBERON:0002107); kidney (UBERON:0002113); skin (UBERON:0002097) | MMAIII; inorganic arsenic; arsenite(3+) | (pullella2024elucidatingtherelationship pages 37-41, ganie2024arsenictoxicitysources pages 2-3) |
| DNA damage and impaired DNA repair | Arsenic increases chromosomal abnormalities, sister chromatid exchange, oxidative DNA damage, and genomic instability. It inhibits DNA mismatch repair and broader DNA repair responses; cmQTL work highlighted DNA repair candidate **Xrcc2**. Chronic exposure is linked to 8-oxo-dG elevation and repair gene dysregulation. | **XRCC2**, **MLH1**, **MSH2**, p53-related pathways | GO:0006281 DNA repair; GO:0006974 cellular response to DNA damage stimulus; GO:0036297 interstrand cross-link repair; GO:0006302 double-strand break repair | fibroblast; keratinocyte; urothelial cell | skin (UBERON:0002097); urinary bladder (UBERON:0001255); lung (UBERON:0002048) | inorganic arsenic; arsenite(3+); MMAIII | (pereira2025arsenomearsenobolomeand pages 19-20, pereira2025arsenomearsenobolomeand pages 20-22, pullella2024elucidatingtherelationship pages 37-41, ganie2024arsenictoxicitysources pages 2-3) |
| Epigenetic dysregulation and methyl-donor depletion | Arsenic perturbs epigenetic control through SAM depletion, global hypomethylation, locus-specific hypermethylation (e.g., **MLH1**, **MSH2**), altered DNMT expression, mitochondrial D-loop hypomethylation, miRNA changes, and m6A-related signaling. Nutritional methyl-donor status (folate, choline, methionine, betaine, B vitamins) modifies toxicity. | **DNMT1**, **DNMT3A**, **DNMT3B**, **MLH1**, **MSH2**, **METTL3**, **YTHDF2**, **JAK2**, **STAT3**, **AS3MT** | GO:0006306 DNA methylation; GO:0016573 histone acetylation; GO:0032776 DNA methylation on cytosine; GO:0010608 post-transcriptional regulation of gene expression | keratinocyte; hepatocyte; stem/progenitor-like epithelial cell | skin (UBERON:0002097); liver (UBERON:0002107); urinary bladder (UBERON:0001255) | inorganic arsenic; arsenite(3+); methylated arsenicals | (pereira2025arsenomearsenobolomeand pages 20-22, pereira2025arsenomearsenobolomeand pages 19-20, pullella2024elucidatingtherelationship pages 37-41, abuawad2023thefolicacid pages 6-7, abuawad2023thefolicacid pages 7-8, abuawad2023thefolicacid pages 1-2) |
| Mitochondrial dysfunction and apoptosis | Arsenic disrupts mitochondrial respiration and oxidative phosphorylation, lowers ATP production, activates JNK/ERK and GRP78/CHOP stress pathways, and promotes apoptosis/cell death trajectories. These events link upstream redox injury to organ dysfunction and neuro/cardiotoxicity. | **JNK**, **ERK**, **GRP78**, **CHOP**, pyruvate dehydrogenase complex | GO:0007005 mitochondrion organization; GO:0008635 activation of apoptotic process; GO:1902600 proton transmembrane transport; GO:0070059 intrinsic apoptotic signaling pathway in response to endoplasmic reticulum stress | neuron; cardiomyocyte; hepatocyte | brain (UBERON:0000955); heart (UBERON:0000948); liver (UBERON:0002107) | MMAIII; arsenite(3+); inorganic arsenic | (pereira2025arsenomearsenobolomeand pages 19-20, ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13) |
| Inflammation, angiogenesis, and malignant transformation | Chronic exposure activates inflammatory signaling (including NF-kB-related and CD14-linked profiles), VEGF/angiogenesis, EMT-like programs, and altered signal transduction, helping connect long-term exposure to skin, bladder, lung, kidney, and liver cancers. | **NFkB**, **VEGF**, **EGFR**, **CD14**, p38 MAPK pathway components | GO:0006954 inflammatory response; GO:0001525 angiogenesis; GO:0001837 epithelial to mesenchymal transition; GO:0008284 positive regulation of cell population proliferation | endothelial cell; macrophage/monocyte; keratinocyte; urothelial cell | skin (UBERON:0002097); lung (UBERON:0002048); urinary bladder (UBERON:0001255); kidney (UBERON:0002113) | inorganic arsenic; arsenite(3+); methylated arsenicals | (pereira2025arsenomearsenobolomeand pages 20-22, pullella2024elucidatingtherelationship pages 37-41, chakif2026heavymetaltoxicity pages 12-13, ganie2024arsenictoxicitysources pages 1-2) |
| Electrophysiologic cardiotoxicity | Arsenic blocks repolarizing potassium currents (IKr, IKs), prolonging QT and predisposing to torsades/arrhythmias; this is a key downstream mechanism in acute severe poisoning. | IKr channel, IKs channel | GO:0086001 cardiac muscle cell action potential; GO:1903779 regulation of cardiac conduction; GO:0006813 potassium ion transport | cardiomyocyte | heart (UBERON:0000948) | arsenite(3+); inorganic arsenic | (pereira2025arsenomearsenobolomeand pages 19-20, balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) |
| Population genetic susceptibility and gene-by-environment interaction | Toxic response varies with arsenic methylation phenotype and genetic background. Human and model-system evidence implicates **AS3MT** genotype in methylation/toxicity variability, while cell-based QTL mapping identified response loci including **Abcc4**, **Txnrd1**, and **Xrcc2** under MMAIII exposure. | **AS3MT**, **ABCC4**, **TXNRD1**, **XRCC2** | GO:0006805 xenobiotic metabolic process; GO:0042221 response to chemical; GO:0006974 cellular response to DNA damage stimulus | fibroblast; hepatocyte | liver (UBERON:0002107); skin (UBERON:0002097); kidney (UBERON:0002113) | MMAIII; inorganic arsenic; arsenite(3+) | (ganie2024arsenictoxicitysources pages 2-3, pullella2024elucidatingtherelationship pages 37-41, abuawad2023thefolicacid pages 8-9, abuawad2023thefolicacid pages 1-2) |


*Table: This table summarizes major molecular and cellular mechanisms of arsenic poisoning and links them to suggested ontology terms for knowledge-base curation. It integrates toxicokinetics, oxidative stress, DNA damage, epigenetic dysregulation, mitochondrial injury, carcinogenic signaling, and genetic susceptibility.*

### 6.1 Current mechanistic understanding (high-level causal chain)
1. **Exposure and uptake** (water/food/air) → systemic distribution and hepatic biotransformation to MMA/DMA. (ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13)
2. **Molecular initiating events**: thiol binding and inhibition of lipoic-acid–dependent enzymes; phosphate mimicry by arsenate; redox disruption. (pereira2025arsenomearsenobolomeand pages 19-20)
3. **Cellular injury pathways**: oxidative/nitrosative stress, mitochondrial dysfunction, ER stress, apoptosis, impaired DNA repair, and epigenetic dysregulation. (pereira2025arsenomearsenobolomeand pages 19-20, pereira2025arsenomearsenobolomeand pages 20-22)
4. **Organ-level outcomes**: GI injury/shock in acute poisoning; skin lesions/neuropathy/vascular disease and carcinogenesis in chronic exposure. (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13)

## 7. Anatomical Structures Affected
- **Acute toxicity:** gastrointestinal tract, cardiovascular system (cardiac conduction), kidney (acute tubular necrosis/AKI), liver, nervous system. (balalimood2025recentadvancesin pages 12-13)
- **Chronic toxicity:** skin (hyperpigmentation, hyperkeratosis), peripheral nerves, vasculature (e.g., Blackfoot disease), and carcinogenesis in bladder, lung, and skin. (chakif2026heavymetaltoxicity pages 12-13, pereira2025arsenomearsenobolomeand pages 20-22)

Suggested UBERON targets are included in Artifact-03.

## 8. Temporal Development
- **Acute onset:** minutes to hours after ingestion (30 min–2 h), with death possible within days if severe. (balalimood2025recentadvancesin pages 12-13)
- **Subacute stage:** neuropathy may develop 2–4 weeks after exposure. (balalimood2025recentadvancesin pages 12-13)
- **Chronic course:** prolonged exposure leads to arsenicosis; recovery can be prolonged and incomplete, particularly neuropathy. (balalimood2025recentadvancesin pages 13-14)

## 9. Inheritance and Population
### 9.1 Epidemiology and exposure burden
- A global scenario/opinion report estimates arsenic-contaminated groundwater affects **~106 countries** and exposes **~230 million** people; WHO, EPA, and EU drinking-water limits are cited as **10 µg/L**. (bhat2024arseniccontaminationneeds pages 1-2)

### 9.2 Regulatory coverage and inequity
- WHO drinking-water guideline value for arsenic is **10 µg/L (0.01 mg/L)** and is explicitly labeled **“Provisional”**, with rationale including **treatment performance and analytical achievability** rather than purely health-based derivation. (mitchell2023acomprehensivesurvey pages 6-8)
- An international survey reports that **32% of the world’s population** live in countries where the national arsenic standard is less protective than the WHO GV of 10 µg/L. (mitchell2023acomprehensivesurvey pages 2-4)

## 10. Diagnostics
A structured diagnostics table is provided in Artifact-02.

| Category | Item | What it indicates/when used | Key quantitative thresholds or notes | Evidence |
|---|---|---|---|---|
| Diagnostic | Urine total arsenic (24-hour) | Main biomarker for recent arsenic exposure; used in suspected acute or ongoing exposure | 24-hour urinary arsenic >100 µg/L reported as elevated/toxic in retrieved evidence; chelation follow-up target <50 µg/L in 24-hour urine; seafood can confound total urinary arsenic unless speciation is done (pullella2024elucidatingtherelationship pages 37-41, balalimood2025recentadvancesin pages 13-14, pullella2024elucidatingtherelationship pages 41-44) | (pullella2024elucidatingtherelationship pages 37-41, balalimood2025recentadvancesin pages 13-14, pullella2024elucidatingtherelationship pages 41-44) |
| Diagnostic | Spot urine arsenic | Practical alternative to 24-hour collection for recent exposure assessment | Spot urine >50 µg/L reported as elevated in retrieved evidence; should be interpreted with hydration correction (e.g., creatinine adjustment) and ideally with speciation (balalimood2025recentadvancesin pages 12-13, pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) | (balalimood2025recentadvancesin pages 12-13, pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) |
| Diagnostic | Urine arsenic speciation (iAs, MMA, DMA) | Best test to distinguish toxic inorganic exposure from seafood-derived organic arsenic; also used to assess methylation phenotype and susceptibility | Requires seafood avoidance before testing; elevated urinary MMA or higher MMA/DMA ratio suggests less complete methylation and potentially higher cancer susceptibility; recent exposure window roughly several days because biologic half-life is about 2-4 days (chakif2026heavymetaltoxicity pages 12-13, pullella2024elucidatingtherelationship pages 37-41) | (chakif2026heavymetaltoxicity pages 12-13, pullella2024elucidatingtherelationship pages 37-41) |
| Diagnostic | Blood arsenic | Reflects very recent exposure and acute poisoning; less useful after rapid clearance | Blood arsenic >130 nmol/L reported as elevated/toxic in retrieved evidence; blood half-life about 2-6 h, so sensitivity falls quickly after exposure (pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) | (pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) |
| Diagnostic | Serum arsenic | Limited clinical utility because arsenic clears rapidly from blood | Not considered reliable for diagnosis once time has elapsed after exposure (balalimood2025recentadvancesin pages 12-13) | (balalimood2025recentadvancesin pages 12-13) |
| Diagnostic | Hair arsenic | Marker of longer-term past exposure | Can become positive about 30 h after exposure; reflects longer-term exposure but is nondiscriminatory for source/species and is not ideal for acute decision-making (balalimood2025recentadvancesin pages 12-13, pullella2024elucidatingtherelationship pages 37-41) | (balalimood2025recentadvancesin pages 12-13, pullella2024elucidatingtherelationship pages 37-41) |
| Diagnostic | Nail arsenic (especially toenail) | Marker of chronic exposure over prior months | Toenail arsenic >0.5 µg/g reported as elevated in retrieved evidence; nails reflect long-term exposure over about 3-6 months (pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) | (pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) |
| Diagnostic | Imaging (abdominal/chest X-ray) | Supportive test in acute poisoning to identify radiopaque ingested arsenic material or evaluate complications | Used selectively in acute ingestion; not a biomarker of body burden (balalimood2025recentadvancesin pages 12-13) | (balalimood2025recentadvancesin pages 12-13) |
| Diagnostic | ECG monitoring | Detects cardiotoxicity in acute poisoning | Important because acute arsenic can prolong QT/QRS and trigger torsades/arrhythmias (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) | (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) |
| Treatment | Exposure cessation/source removal | First-line intervention in all cases, especially chronic/subacute arsenicosis | Removal from contaminated water/food/occupational source is the primary treatment for chronic poisoning (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Succimer / DMSA | Oral chelator used for arsenic poisoning, especially when prolonged treatment is needed or less invasive therapy is preferred | Named as a key chelator; preferred for prolonged chronic/subacute cases in retrieved evidence; most effective when started minutes to hours after exposure (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | DMPS | Water-soluble chelator used in arsenic poisoning | Named as a key arsenic chelator; most useful early after exposure; use varies by region/regulatory approval (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Dimercaprol / BAL | Traditional parenteral chelator for severe acute arsenic poisoning | Named as a key chelator; most effective when given soon after exposure, typically minutes to hours (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | IV fluids and electrolyte replacement | Core supportive therapy for acute poisoning with severe vomiting/diarrhea and shock | Critical because deaths often result from hypovolemia, renal failure, or cardiac complications (balalimood2025recentadvancesin pages 12-13, balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 12-13, balalimood2025recentadvancesin pages 13-14) |
| Treatment | GI decontamination / bowel irrigation / NG suction | Used in selected acute ingestions, especially if arsenic is still in the GI tract or radiopaque material is seen | Activated charcoal adsorbs arsenic poorly; whole-bowel irrigation or continued NG suction may be considered in severe ingestion (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Antiarrhythmic management and magnesium | Supportive management for QT prolongation/torsades and other arrhythmias | Magnesium sulfate, amiodarone, or lidocaine reported as options; avoid class IA/IC/III antiarrhythmics in this context per retrieved review (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Benzodiazepines for seizures | Symptom-directed treatment in acute neurotoxicity | Used when seizures occur during severe intoxication (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Hemodialysis | Adjunctive/supportive therapy in severe poisoning with kidney failure or oliguria | Recommended in acute kidney injury/oliguria; supportive rather than stand-alone antidotal therapy (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Exchange transfusion | Special situation therapy for arsine gas poisoning with massive hemolysis | Can help remove arsine-related toxic burden in severe hemolytic presentations (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Antioxidant/nutritional adjuncts | Investigational or supportive approaches to mitigate toxicity or improve methylation/detoxification | Selenium, zinc, folate, vitamins A/C/E, and phytochemicals have been proposed; clinical evidence remains limited (balalimood2025recentadvancesin pages 13-14, abuawad2023thefolicacid pages 6-7, abuawad2023thefolicacid pages 7-8, abuawad2023thefolicacid pages 1-2) | (balalimood2025recentadvancesin pages 13-14, abuawad2023thefolicacid pages 6-7, abuawad2023thefolicacid pages 7-8, abuawad2023thefolicacid pages 1-2) |


*Table: This table summarizes clinically relevant diagnostic biomarkers and current treatment approaches for arsenic poisoning, including practical interpretation notes and quantitative thresholds reported in the retrieved evidence. It is useful for distinguishing recent versus chronic exposure and for mapping acute management options to the evidence base.*

Key points:
- **Urine arsenic speciation (iAs/MMA/DMA)** is emphasized as essential to distinguish inorganic exposure from seafood-related organic arsenic and to evaluate methylation phenotype. (chakif2026heavymetaltoxicity pages 12-13, pullella2024elucidatingtherelationship pages 37-41)
- Quantitative cutoffs reported in retrieved sources include **blood arsenic >130 nmol/L**, **24‑h urinary total arsenic >100 µg/L**, **spot urine >50 µg/L**, and **toenail As >0.5 µg/g** (noting these are presented in a review context and should be interpreted clinically). (pullella2024elucidatingtherelationship pages 41-44)

## 11. Outcome / Prognosis
### 11.1 Acute poisoning outcomes
- **Minimal lethal dose** reported as **1–3 mg/kg**, with an estimated lethal inorganic exposure around **0.6 mg/kg**; death may occur **within 1–4 days** after ingestion. (balalimood2025recentadvancesin pages 12-13)
- **Arsine gas** exposures above **~10 ppm** are described as lethal. (balalimood2025recentadvancesin pages 12-13)

### 11.2 Long-term complications and quantitative cancer risks
- A 2023 systematic review/meta-analysis update reported Bayesian pooled RRs for **bladder cancer incidence** of **1.25** at 10 µg/L, **2.11** at 50 µg/L, and **3.01** at 150 µg/L; and for **kidney cancer** of **1.37** at 10 µg/L, **1.95** at 50 µg/L, and **2.47** at 150 µg/L. (issanov2023arsenicindrinking pages 1-2)

## 12. Treatment
### 12.1 Acute management (real-world implementation)
- Core management includes **aggressive IV fluids/electrolytes**, symptom control (antiemetics), arrhythmia and seizure management, and renal support including **hemodialysis for AKI/oliguria**. (balalimood2025recentadvancesin pages 13-14)
- **Chelation:** key agents named include **succimer (DMSA)**, **DMPS**, and **dimercaprol (BAL)**; chelators are described as most effective **minutes to hours** after exposure. A suggested chelation target is **24‑h urinary arsenic <50 µg/L**. (balalimood2025recentadvancesin pages 13-14)
- Chronic/subacute arsenicosis: **exposure cessation is primary**, chelation has **limited efficacy**, and succimer is noted as preferred for prolonged cases with monitoring. (balalimood2025recentadvancesin pages 13-14)

### 12.2 Nutritional intervention evidence (human trial)
- **FACT trial (NCT01050556; Bangladesh; 2023 EHP):** folic acid (400–800 µg/day) improved blood methylation profiles (increased SMI and %DMAs, decreased %MMAs), with partial reversal upon stopping supplementation, supporting sustained methyl-donor strategies (e.g., fortification) as a plausible mitigation adjunct. (abuawad2023thefolicacid pages 1-2, abuawad2023thefolicacid pages 7-8)

**Suggested MAXO terms (names only):** chelation therapy; hemodialysis; gastrointestinal decontamination; nutritional supplementation; exposure avoidance/remediation.

## 13. Prevention
- **Primary prevention:** reduce iAs exposure through enforcement of drinking-water standards and mitigation/removal technologies; WHO GV is 10 µg/L (provisional) and set with feasibility constraints. (mitchell2023acomprehensivesurvey pages 6-8)
- **Population-scale mitigation urgency:** global scenario evidence supports the large exposed population and multi-country distribution, motivating monitoring and remediation prioritization. (bhat2024arseniccontaminationneeds pages 1-2)

## 14. Other Species / Natural Disease
The retrieved sources did not provide well-documented naturally occurring “arsenicosis” case series in companion animals; however, the toxicant is relevant across species and arsenic exposure is discussed in livestock contexts in broader heavy-metal reviews (not specific to arsenic-only disease characterization).

## 15. Model Organisms
- **Humanized AS3MT mouse model (C57BL/6):** A 2024 study used C57BL/6 mice carrying the human BORCS7/AS3MT locus; with **200 ppb arsenite** exposures during different developmental windows, the model showed sex- and window-specific increases in fasting glycemia and impaired β-cell function (lower HOMA‑β in in utero exposed males), and it is presented as more human-relevant because standard mice methylate/detoxify iAs more efficiently than humans. (singh2024arsenicexposurein pages 1-5)
- **Genetically diverse in vitro model (Diversity Outbred fibroblasts):** A 2024 PLOS Genetics study derived fibroblast lines from DO mice and exposed them to **MMA(III)**, using high-content imaging to map **cell morphology QTLs**; loci included known detox genes (**Abcc4, Txnrd1**) and DNA repair (**Xrcc2**), enabling gene–environment mapping of arsenic sensitivity/resilience. (o’connor2024unravelingthegenetics pages 2-3, o’connor2024unravelingthegenetics pages 1-2)

## Recent developments and expert analysis (2023–2024 emphasis)
- **Regulatory science update:** WHO’s arsenic GV remains **10 µg/L (provisional)** and is explicitly constrained by treatment/analytical feasibility, highlighting a persistent gap between health-based values and implementable standards. (mitchell2023acomprehensivesurvey pages 6-8)
- **Quantitative cancer risk at low-to-moderate exposures:** Updated systematic review evidence supports elevated bladder and kidney cancer risk even at **10 µg/L**, albeit with uncertainty, with increasing risks at 50 and 150 µg/L. (issanov2023arsenicindrinking pages 1-2)
- **Global public-health framing (expert opinion):** Recent global scenario/opinion work emphasizes urgent mitigation given widespread exposure (230 million) and broad geographic footprint (106 countries). (bhat2024arseniccontaminationneeds pages 1-2)

## Key concepts and definitions (summary tables)
| Concept | Definition/notes | Synonyms | Key exposure route(s) | Identifier(s) explicitly available in retrieved evidence | Key citation ID |
|---|---|---|---|---|---|
| Acute arsenic poisoning | Rapid-onset toxicity, usually after ingestion of inorganic arsenic; symptoms may begin within ~30 min to 2 h and commonly include severe gastroenteritis, hypotension, QT prolongation/arrhythmia, neurologic toxicity, renal injury, and hepatic/hematologic abnormalities. | Acute arsenic toxicity | Ingestion; less commonly inhalation in occupational settings | Not found in retrieved sources | (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) |
| Chronic arsenic poisoning / arsenicosis | Slow accumulation of low-dose exposure over time causing multisystem disease, especially skin lesions, peripheral neuropathy, vascular disease, and elevated cancer risk; explicitly named “arsenicosis.” | Arsenicosis; arseniasis; arsenism; arsenicism | Chronic ingestion via drinking water/food; inhalation in some occupational settings | Not found in retrieved sources | (ganie2024arsenictoxicitysources pages 2-3, ganie2024arsenictoxicitysources pages 1-2, pereira2025arsenomearsenobolomeand pages 20-22) |
| Inorganic arsenic (iAs) | Toxicologically most important arsenic category; includes pentavalent arsenate and trivalent arsenite, undergoes hepatic methylation to MMA and DMA, and is associated with carcinogenic, vascular, neurologic, and dermatologic effects. | iAs; inorganic As | Ingestion from contaminated water/food; inhalation | Not found in retrieved sources | (ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13, ganie2024arsenictoxicitysources pages 1-2) |
| Arsenite As(III) | Trivalent inorganic arsenic; generally more toxic than As(V), strongly interacts with sulfhydryl-containing proteins and key enzymes, and is central to oxidative stress and mitochondrial dysfunction mechanisms. | Arsenite; As3+; trivalent arsenic; meta-arsenite | Ingestion; inhalation; some dermal absorption of trivalent forms | Not found in retrieved sources | (ganie2024arsenictoxicitysources pages 2-3, ganie2024arsenictoxicitysources pages 1-2, pereira2025arsenomearsenobolomeand pages 19-20) |
| Arsenate As(V) | Pentavalent inorganic arsenic; enters cells via phosphate transporters and can substitute for phosphate in biochemical reactions, disrupting cellular energetics before reduction/methylation. | Arsenate; As5+; pentavalent arsenic | Ingestion; inhalation | Not found in retrieved sources | (ganie2024arsenictoxicitysources pages 2-3, ganie2024arsenictoxicitysources pages 1-2, pereira2025arsenomearsenobolomeand pages 19-20) |
| Arsine gas AsH3 | Extremely toxic gaseous arsenic species; inhalational exposure is a classic occupational hazard and can be rapidly lethal, with reported lethality above ~10 ppm in retrieved evidence. | Arsine; arsenic hydride | Inhalation | Not found in retrieved sources | (balalimood2025recentadvancesin pages 12-13) |


*Table: This table summarizes the main clinical and chemical concepts relevant to arsenic poisoning, including acute and chronic disease forms and major inorganic arsenic species. It is useful as a compact reference for terminology, exposure routes, and evidence-backed definitions from the retrieved literature.*

## Diagnostics and treatments (summary table)
| Category | Item | What it indicates/when used | Key quantitative thresholds or notes | Evidence |
|---|---|---|---|---|
| Diagnostic | Urine total arsenic (24-hour) | Main biomarker for recent arsenic exposure; used in suspected acute or ongoing exposure | 24-hour urinary arsenic >100 µg/L reported as elevated/toxic in retrieved evidence; chelation follow-up target <50 µg/L in 24-hour urine; seafood can confound total urinary arsenic unless speciation is done (pullella2024elucidatingtherelationship pages 37-41, balalimood2025recentadvancesin pages 13-14, pullella2024elucidatingtherelationship pages 41-44) | (pullella2024elucidatingtherelationship pages 37-41, balalimood2025recentadvancesin pages 13-14, pullella2024elucidatingtherelationship pages 41-44) |
| Diagnostic | Spot urine arsenic | Practical alternative to 24-hour collection for recent exposure assessment | Spot urine >50 µg/L reported as elevated in retrieved evidence; should be interpreted with hydration correction (e.g., creatinine adjustment) and ideally with speciation (balalimood2025recentadvancesin pages 12-13, pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) | (balalimood2025recentadvancesin pages 12-13, pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) |
| Diagnostic | Urine arsenic speciation (iAs, MMA, DMA) | Best test to distinguish toxic inorganic exposure from seafood-derived organic arsenic; also used to assess methylation phenotype and susceptibility | Requires seafood avoidance before testing; elevated urinary MMA or higher MMA/DMA ratio suggests less complete methylation and potentially higher cancer susceptibility; recent exposure window roughly several days because biologic half-life is about 2-4 days (chakif2026heavymetaltoxicity pages 12-13, pullella2024elucidatingtherelationship pages 37-41) | (chakif2026heavymetaltoxicity pages 12-13, pullella2024elucidatingtherelationship pages 37-41) |
| Diagnostic | Blood arsenic | Reflects very recent exposure and acute poisoning; less useful after rapid clearance | Blood arsenic >130 nmol/L reported as elevated/toxic in retrieved evidence; blood half-life about 2-6 h, so sensitivity falls quickly after exposure (pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) | (pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) |
| Diagnostic | Serum arsenic | Limited clinical utility because arsenic clears rapidly from blood | Not considered reliable for diagnosis once time has elapsed after exposure (balalimood2025recentadvancesin pages 12-13) | (balalimood2025recentadvancesin pages 12-13) |
| Diagnostic | Hair arsenic | Marker of longer-term past exposure | Can become positive about 30 h after exposure; reflects longer-term exposure but is nondiscriminatory for source/species and is not ideal for acute decision-making (balalimood2025recentadvancesin pages 12-13, pullella2024elucidatingtherelationship pages 37-41) | (balalimood2025recentadvancesin pages 12-13, pullella2024elucidatingtherelationship pages 37-41) |
| Diagnostic | Nail arsenic (especially toenail) | Marker of chronic exposure over prior months | Toenail arsenic >0.5 µg/g reported as elevated in retrieved evidence; nails reflect long-term exposure over about 3-6 months (pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) | (pullella2024elucidatingtherelationship pages 37-41, pullella2024elucidatingtherelationship pages 41-44) |
| Diagnostic | Imaging (abdominal/chest X-ray) | Supportive test in acute poisoning to identify radiopaque ingested arsenic material or evaluate complications | Used selectively in acute ingestion; not a biomarker of body burden (balalimood2025recentadvancesin pages 12-13) | (balalimood2025recentadvancesin pages 12-13) |
| Diagnostic | ECG monitoring | Detects cardiotoxicity in acute poisoning | Important because acute arsenic can prolong QT/QRS and trigger torsades/arrhythmias (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) | (balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) |
| Treatment | Exposure cessation/source removal | First-line intervention in all cases, especially chronic/subacute arsenicosis | Removal from contaminated water/food/occupational source is the primary treatment for chronic poisoning (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Succimer / DMSA | Oral chelator used for arsenic poisoning, especially when prolonged treatment is needed or less invasive therapy is preferred | Named as a key chelator; preferred for prolonged chronic/subacute cases in retrieved evidence; most effective when started minutes to hours after exposure (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | DMPS | Water-soluble chelator used in arsenic poisoning | Named as a key arsenic chelator; most useful early after exposure; use varies by region/regulatory approval (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Dimercaprol / BAL | Traditional parenteral chelator for severe acute arsenic poisoning | Named as a key chelator; most effective when given soon after exposure, typically minutes to hours (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | IV fluids and electrolyte replacement | Core supportive therapy for acute poisoning with severe vomiting/diarrhea and shock | Critical because deaths often result from hypovolemia, renal failure, or cardiac complications (balalimood2025recentadvancesin pages 12-13, balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 12-13, balalimood2025recentadvancesin pages 13-14) |
| Treatment | GI decontamination / bowel irrigation / NG suction | Used in selected acute ingestions, especially if arsenic is still in the GI tract or radiopaque material is seen | Activated charcoal adsorbs arsenic poorly; whole-bowel irrigation or continued NG suction may be considered in severe ingestion (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Antiarrhythmic management and magnesium | Supportive management for QT prolongation/torsades and other arrhythmias | Magnesium sulfate, amiodarone, or lidocaine reported as options; avoid class IA/IC/III antiarrhythmics in this context per retrieved review (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Benzodiazepines for seizures | Symptom-directed treatment in acute neurotoxicity | Used when seizures occur during severe intoxication (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Hemodialysis | Adjunctive/supportive therapy in severe poisoning with kidney failure or oliguria | Recommended in acute kidney injury/oliguria; supportive rather than stand-alone antidotal therapy (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Exchange transfusion | Special situation therapy for arsine gas poisoning with massive hemolysis | Can help remove arsine-related toxic burden in severe hemolytic presentations (balalimood2025recentadvancesin pages 13-14) | (balalimood2025recentadvancesin pages 13-14) |
| Treatment | Antioxidant/nutritional adjuncts | Investigational or supportive approaches to mitigate toxicity or improve methylation/detoxification | Selenium, zinc, folate, vitamins A/C/E, and phytochemicals have been proposed; clinical evidence remains limited (balalimood2025recentadvancesin pages 13-14, abuawad2023thefolicacid pages 6-7, abuawad2023thefolicacid pages 7-8, abuawad2023thefolicacid pages 1-2) | (balalimood2025recentadvancesin pages 13-14, abuawad2023thefolicacid pages 6-7, abuawad2023thefolicacid pages 7-8, abuawad2023thefolicacid pages 1-2) |


*Table: This table summarizes clinically relevant diagnostic biomarkers and current treatment approaches for arsenic poisoning, including practical interpretation notes and quantitative thresholds reported in the retrieved evidence. It is useful for distinguishing recent versus chronic exposure and for mapping acute management options to the evidence base.*

## Mechanisms and ontology mapping (summary table)
| Mechanism (high level) | Molecular details/chain | Example genes/proteins | Suggested GO biological process terms | Suggested CL cell types | Suggested UBERON organs/tissues | Suggested CHEBI entities/arsenic species | Evidence (citation IDs) |
|---|---|---|---|---|---|---|---|
| Toxicokinetic uptake, biotransformation, and distribution | Ingested/inhaled inorganic arsenic is absorbed, distributed systemically, and methylated mainly in liver to MMA and DMA; As(V) enters via phosphate transporters, As(III) via aquaglyceroporins, then binds thiols and undergoes reduction/methylation using GSH, thioredoxin systems, SAM, and AS3MT. Urinary excretion is the main clearance route; skin, hair, nails, bone, and teeth can accumulate arsenic. | **AS3MT**, **TXNRD1**, thioredoxin, glutathione-related proteins, aquaglyceroporins, phosphate transporters | GO:0006730 one-carbon metabolic process; GO:0017144 drug metabolic process; GO:0042493 response to drug; GO:0055085 transmembrane transport | hepatocyte; erythrocyte; renal tubular epithelial cell | liver (UBERON:0002107); kidney (UBERON:0002113); skin (UBERON:0002097); blood (UBERON:0000178) | inorganic arsenic; arsenite(3+) / As(III); arsenate(V) / As(V); monomethylarsonous acid (MMAIII); dimethylarsinic acid (DMA) | (ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13, ganie2024arsenictoxicitysources pages 1-2, pullella2024elucidatingtherelationship pages 37-41) |
| Thiol binding and enzyme inhibition | Trivalent arsenicals bind sulfhydryl/lipoic-acid–dependent enzymes, disrupting central metabolism and redox homeostasis. MMA(III) binds lipoic acid and inhibits pyruvate dehydrogenase; As(V) can substitute for phosphate in metabolic intermediates, impairing ATP-generating reactions. | pyruvate dehydrogenase complex, lipoic acid–dependent enzymes, glyceraldehyde-3-phosphate dehydrogenase | GO:0006099 tricarboxylic acid cycle; GO:0006096 glycolytic process; GO:0046034 ATP metabolic process; GO:0055114 oxidation-reduction process | hepatocyte; cardiomyocyte; neuron | liver (UBERON:0002107); heart (UBERON:0000948); nervous system (UBERON:0001016) | arsenite(3+); arsenate(V); MMAIII; ADP-arsenate; glucose-6-arsenate | (pereira2025arsenomearsenobolomeand pages 19-20, ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13) |
| Oxidative and nitrosative stress | A central initiating event is ROS/RNS generation with lipid, protein, and DNA oxidation; reported biomarkers include MDA, protein carbonyls, and 8-hydroxydeoxyguanosine. MMA(III) and As(III) also interfere with nitric oxide biology, including NOS inhibition and peroxynitrite-related injury. | **TXNRD1**, Nrf2 pathway components, nitric oxide synthase, heme oxygenase, ferritin, metallothionein | GO:0006979 response to oxidative stress; GO:1903409 reactive oxygen species metabolic process; GO:0051409 response to nitrosative stress; GO:0034599 cellular response to oxidative stress | fibroblast; endothelial cell; keratinocyte; neuron | skin (UBERON:0002097); vasculature (UBERON:0004535); lung (UBERON:0002048); kidney (UBERON:0002113) | arsenite(3+); MMAIII; inorganic arsenic | (balalimood2025recentadvancesin pages 12-13, pereira2025arsenomearsenobolomeand pages 19-20, pereira2025arsenomearsenobolomeand pages 20-22, pullella2024elucidatingtherelationship pages 37-41, ganie2024arsenictoxicitysources pages 2-3) |
| NRF2-mediated antioxidant response and detoxification | Genetic and experimental studies identify NRF2-linked antioxidant defense, detoxification, and stress-response programs as major regulated responses to arsenic metabolites. Cellular morphology QTL mapped loci including **Abcc4** and **Txnrd1**, supporting genetically controlled variability in response to MMAIII. | **ABCC4**, **TXNRD1**, NRF2 pathway genes, metallothioneins | GO:0034599 cellular response to oxidative stress; GO:0042744 hydrogen peroxide catabolic process; GO:0006805 xenobiotic metabolic process; GO:0046677 response to antibiotic | fibroblast; hepatocyte; renal epithelial cell | liver (UBERON:0002107); kidney (UBERON:0002113); skin (UBERON:0002097) | MMAIII; inorganic arsenic; arsenite(3+) | (pullella2024elucidatingtherelationship pages 37-41, ganie2024arsenictoxicitysources pages 2-3) |
| DNA damage and impaired DNA repair | Arsenic increases chromosomal abnormalities, sister chromatid exchange, oxidative DNA damage, and genomic instability. It inhibits DNA mismatch repair and broader DNA repair responses; cmQTL work highlighted DNA repair candidate **Xrcc2**. Chronic exposure is linked to 8-oxo-dG elevation and repair gene dysregulation. | **XRCC2**, **MLH1**, **MSH2**, p53-related pathways | GO:0006281 DNA repair; GO:0006974 cellular response to DNA damage stimulus; GO:0036297 interstrand cross-link repair; GO:0006302 double-strand break repair | fibroblast; keratinocyte; urothelial cell | skin (UBERON:0002097); urinary bladder (UBERON:0001255); lung (UBERON:0002048) | inorganic arsenic; arsenite(3+); MMAIII | (pereira2025arsenomearsenobolomeand pages 19-20, pereira2025arsenomearsenobolomeand pages 20-22, pullella2024elucidatingtherelationship pages 37-41, ganie2024arsenictoxicitysources pages 2-3) |
| Epigenetic dysregulation and methyl-donor depletion | Arsenic perturbs epigenetic control through SAM depletion, global hypomethylation, locus-specific hypermethylation (e.g., **MLH1**, **MSH2**), altered DNMT expression, mitochondrial D-loop hypomethylation, miRNA changes, and m6A-related signaling. Nutritional methyl-donor status (folate, choline, methionine, betaine, B vitamins) modifies toxicity. | **DNMT1**, **DNMT3A**, **DNMT3B**, **MLH1**, **MSH2**, **METTL3**, **YTHDF2**, **JAK2**, **STAT3**, **AS3MT** | GO:0006306 DNA methylation; GO:0016573 histone acetylation; GO:0032776 DNA methylation on cytosine; GO:0010608 post-transcriptional regulation of gene expression | keratinocyte; hepatocyte; stem/progenitor-like epithelial cell | skin (UBERON:0002097); liver (UBERON:0002107); urinary bladder (UBERON:0001255) | inorganic arsenic; arsenite(3+); methylated arsenicals | (pereira2025arsenomearsenobolomeand pages 20-22, pereira2025arsenomearsenobolomeand pages 19-20, pullella2024elucidatingtherelationship pages 37-41, abuawad2023thefolicacid pages 6-7, abuawad2023thefolicacid pages 7-8, abuawad2023thefolicacid pages 1-2) |
| Mitochondrial dysfunction and apoptosis | Arsenic disrupts mitochondrial respiration and oxidative phosphorylation, lowers ATP production, activates JNK/ERK and GRP78/CHOP stress pathways, and promotes apoptosis/cell death trajectories. These events link upstream redox injury to organ dysfunction and neuro/cardiotoxicity. | **JNK**, **ERK**, **GRP78**, **CHOP**, pyruvate dehydrogenase complex | GO:0007005 mitochondrion organization; GO:0008635 activation of apoptotic process; GO:1902600 proton transmembrane transport; GO:0070059 intrinsic apoptotic signaling pathway in response to endoplasmic reticulum stress | neuron; cardiomyocyte; hepatocyte | brain (UBERON:0000955); heart (UBERON:0000948); liver (UBERON:0002107) | MMAIII; arsenite(3+); inorganic arsenic | (pereira2025arsenomearsenobolomeand pages 19-20, ganie2024arsenictoxicitysources pages 2-3, chakif2026heavymetaltoxicity pages 12-13) |
| Inflammation, angiogenesis, and malignant transformation | Chronic exposure activates inflammatory signaling (including NF-kB-related and CD14-linked profiles), VEGF/angiogenesis, EMT-like programs, and altered signal transduction, helping connect long-term exposure to skin, bladder, lung, kidney, and liver cancers. | **NFkB**, **VEGF**, **EGFR**, **CD14**, p38 MAPK pathway components | GO:0006954 inflammatory response; GO:0001525 angiogenesis; GO:0001837 epithelial to mesenchymal transition; GO:0008284 positive regulation of cell population proliferation | endothelial cell; macrophage/monocyte; keratinocyte; urothelial cell | skin (UBERON:0002097); lung (UBERON:0002048); urinary bladder (UBERON:0001255); kidney (UBERON:0002113) | inorganic arsenic; arsenite(3+); methylated arsenicals | (pereira2025arsenomearsenobolomeand pages 20-22, pullella2024elucidatingtherelationship pages 37-41, chakif2026heavymetaltoxicity pages 12-13, ganie2024arsenictoxicitysources pages 1-2) |
| Electrophysiologic cardiotoxicity | Arsenic blocks repolarizing potassium currents (IKr, IKs), prolonging QT and predisposing to torsades/arrhythmias; this is a key downstream mechanism in acute severe poisoning. | IKr channel, IKs channel | GO:0086001 cardiac muscle cell action potential; GO:1903779 regulation of cardiac conduction; GO:0006813 potassium ion transport | cardiomyocyte | heart (UBERON:0000948) | arsenite(3+); inorganic arsenic | (pereira2025arsenomearsenobolomeand pages 19-20, balalimood2025recentadvancesin pages 12-13, chakif2026heavymetaltoxicity pages 12-13) |
| Population genetic susceptibility and gene-by-environment interaction | Toxic response varies with arsenic methylation phenotype and genetic background. Human and model-system evidence implicates **AS3MT** genotype in methylation/toxicity variability, while cell-based QTL mapping identified response loci including **Abcc4**, **Txnrd1**, and **Xrcc2** under MMAIII exposure. | **AS3MT**, **ABCC4**, **TXNRD1**, **XRCC2** | GO:0006805 xenobiotic metabolic process; GO:0042221 response to chemical; GO:0006974 cellular response to DNA damage stimulus | fibroblast; hepatocyte | liver (UBERON:0002107); skin (UBERON:0002097); kidney (UBERON:0002113) | MMAIII; inorganic arsenic; arsenite(3+) | (ganie2024arsenictoxicitysources pages 2-3, pullella2024elucidatingtherelationship pages 37-41, abuawad2023thefolicacid pages 8-9, abuawad2023thefolicacid pages 1-2) |


*Table: This table summarizes major molecular and cellular mechanisms of arsenic poisoning and links them to suggested ontology terms for knowledge-base curation. It integrates toxicokinetics, oxidative stress, DNA damage, epigenetic dysregulation, mitochondrial injury, carcinogenic signaling, and genetic susceptibility.*


References

1. (balalimood2025recentadvancesin pages 12-13): Mahdi Balali-Mood, Nastaran Eizadi-Mood, Hossein Hassanian-Moghaddam, Leila Etemad, Mohammad Moshiri, Maryam Vahabzadeh, and Mahmood Sadeghi. Recent advances in the clinical management of intoxication by five heavy metals: mercury, lead, chromium, cadmium and arsenic. Heliyon, 11:e42696, Feb 2025. URL: https://doi.org/10.1016/j.heliyon.2025.e42696, doi:10.1016/j.heliyon.2025.e42696. This article has 65 citations.

2. (ganie2024arsenictoxicitysources pages 2-3): Shahid Yousuf Ganie, Darakhshan Javaid, Younis Ahmad Hajam, and Mohd Salim Reshi. Arsenic toxicity: sources, pathophysiology and mechanism. Toxicology research, 13 1:tfad111, Dec 2024. URL: https://doi.org/10.1093/toxres/tfad111, doi:10.1093/toxres/tfad111. This article has 170 citations.

3. (chakif2026heavymetaltoxicity pages 12-13): Dib Chakif and Julien Furrer. Heavy metal toxicity in clinical and environmental health: sources, mechanisms, diagnostics, and evidence-based management of mercury, lead, cadmium, and arsenic. International Journal of Molecular Sciences, 27:3513, Apr 2026. URL: https://doi.org/10.3390/ijms27083513, doi:10.3390/ijms27083513. This article has 0 citations.

4. (visciano2025arsenicinwater pages 10-12): Pierina Visciano. Arsenic in water and food: toxicity and human exposure. Foods, 14:2229, Jun 2025. URL: https://doi.org/10.3390/foods14132229, doi:10.3390/foods14132229. This article has 11 citations.

5. (issanov2023arsenicindrinking pages 1-2): Alpamys Issanov, Betty Adewusi, Trevor J. B. Dummer, and Nathalie Saint-Jacques. Arsenic in drinking water and urinary tract cancers: a systematic review update. Water, Jun 2023. URL: https://doi.org/10.3390/w15122185, doi:10.3390/w15122185. This article has 17 citations.

6. (ganie2024arsenictoxicitysources pages 1-2): Shahid Yousuf Ganie, Darakhshan Javaid, Younis Ahmad Hajam, and Mohd Salim Reshi. Arsenic toxicity: sources, pathophysiology and mechanism. Toxicology research, 13 1:tfad111, Dec 2024. URL: https://doi.org/10.1093/toxres/tfad111, doi:10.1093/toxres/tfad111. This article has 170 citations.

7. (bhat2024arseniccontaminationneeds pages 1-2): Abhijnan Bhat, Kamna Ravi, Furong Tian, and Baljit Singh. Arsenic contamination needs serious attention: an opinion and global scenario. Pollutants, 4:196-211, Apr 2024. URL: https://doi.org/10.3390/pollutants4020013, doi:10.3390/pollutants4020013. This article has 76 citations.

8. (pullella2024elucidatingtherelationship pages 37-41): K Pullella. Elucidating the relationship between arsenic exposure and cancer risk in canada. Unknown journal, 2024.

9. (pereira2025arsenomearsenobolomeand pages 20-22): Fernando J. Pereira, Roberto López, and A. Javier Aller. Arsenome, arsenobolome, and arsenobiolome. International Journal of Molecular Sciences, 26:10761, Nov 2025. URL: https://doi.org/10.3390/ijms262110761, doi:10.3390/ijms262110761. This article has 0 citations.

10. (abuawad2023thefolicacid pages 7-8): Ahlam K. Abuawad, Anne K. Bozack, Ana Navas-Acien, Jeff Goldsmith, Xinhua Liu, Megan N. Hall, Vesna Ilievski, Angela M. Lomax-Luu, Faruque Parvez, Hasan Shahriar, Mohammad N. Uddin, Tariqul Islam, Joseph H. Graziano, and Mary V. Gamble. The folic acid and creatine trial: treatment effects of supplementation on arsenic methylation indices and metabolite concentrations in blood in a bangladeshi population. Environmental Health Perspectives, Mar 2023. URL: https://doi.org/10.1289/ehp11270, doi:10.1289/ehp11270. This article has 16 citations and is from a highest quality peer-reviewed journal.

11. (abuawad2023thefolicacid pages 1-2): Ahlam K. Abuawad, Anne K. Bozack, Ana Navas-Acien, Jeff Goldsmith, Xinhua Liu, Megan N. Hall, Vesna Ilievski, Angela M. Lomax-Luu, Faruque Parvez, Hasan Shahriar, Mohammad N. Uddin, Tariqul Islam, Joseph H. Graziano, and Mary V. Gamble. The folic acid and creatine trial: treatment effects of supplementation on arsenic methylation indices and metabolite concentrations in blood in a bangladeshi population. Environmental Health Perspectives, Mar 2023. URL: https://doi.org/10.1289/ehp11270, doi:10.1289/ehp11270. This article has 16 citations and is from a highest quality peer-reviewed journal.

12. (o’connor2024unravelingthegenetics pages 1-2): Callan O’Connor, Gregory R. Keele, Whitney Martin, Timothy Stodola, Daniel Gatti, Brian R. Hoffman, Ron Korstanje, Gary A. Churchill, and Laura G. Reinholdt. Unraveling the genetics of arsenic toxicity with cellular morphology qtl. PLOS Genetics, 20:e1011248, Apr 2024. URL: https://doi.org/10.1371/journal.pgen.1011248, doi:10.1371/journal.pgen.1011248. This article has 6 citations and is from a domain leading peer-reviewed journal.

13. (balalimood2025recentadvancesin pages 13-14): Mahdi Balali-Mood, Nastaran Eizadi-Mood, Hossein Hassanian-Moghaddam, Leila Etemad, Mohammad Moshiri, Maryam Vahabzadeh, and Mahmood Sadeghi. Recent advances in the clinical management of intoxication by five heavy metals: mercury, lead, chromium, cadmium and arsenic. Heliyon, 11:e42696, Feb 2025. URL: https://doi.org/10.1016/j.heliyon.2025.e42696, doi:10.1016/j.heliyon.2025.e42696. This article has 65 citations.

14. (pereira2025arsenomearsenobolomeand pages 19-20): Fernando J. Pereira, Roberto López, and A. Javier Aller. Arsenome, arsenobolome, and arsenobiolome. International Journal of Molecular Sciences, 26:10761, Nov 2025. URL: https://doi.org/10.3390/ijms262110761, doi:10.3390/ijms262110761. This article has 0 citations.

15. (singh2024arsenicexposurein pages 1-5): N Singh. Arsenic exposure in c57bl/6 mice carrying human as3mt elevates fasting glycemia and impairs beta cell function according to sex and developmental window …. Unknown journal, 2024.

16. (abuawad2023thefolicacid pages 6-7): Ahlam K. Abuawad, Anne K. Bozack, Ana Navas-Acien, Jeff Goldsmith, Xinhua Liu, Megan N. Hall, Vesna Ilievski, Angela M. Lomax-Luu, Faruque Parvez, Hasan Shahriar, Mohammad N. Uddin, Tariqul Islam, Joseph H. Graziano, and Mary V. Gamble. The folic acid and creatine trial: treatment effects of supplementation on arsenic methylation indices and metabolite concentrations in blood in a bangladeshi population. Environmental Health Perspectives, Mar 2023. URL: https://doi.org/10.1289/ehp11270, doi:10.1289/ehp11270. This article has 16 citations and is from a highest quality peer-reviewed journal.

17. (abuawad2023thefolicacid pages 8-9): Ahlam K. Abuawad, Anne K. Bozack, Ana Navas-Acien, Jeff Goldsmith, Xinhua Liu, Megan N. Hall, Vesna Ilievski, Angela M. Lomax-Luu, Faruque Parvez, Hasan Shahriar, Mohammad N. Uddin, Tariqul Islam, Joseph H. Graziano, and Mary V. Gamble. The folic acid and creatine trial: treatment effects of supplementation on arsenic methylation indices and metabolite concentrations in blood in a bangladeshi population. Environmental Health Perspectives, Mar 2023. URL: https://doi.org/10.1289/ehp11270, doi:10.1289/ehp11270. This article has 16 citations and is from a highest quality peer-reviewed journal.

18. (mitchell2023acomprehensivesurvey pages 6-8): Erika J. Mitchell and Seth H. Frisbie. A comprehensive survey and analysis of international drinking water regulations for inorganic chemicals with comparisons to the world health organization’s drinking-water guidelines. PLOS ONE, 18:e0287937, Nov 2023. URL: https://doi.org/10.1371/journal.pone.0287937, doi:10.1371/journal.pone.0287937. This article has 33 citations and is from a peer-reviewed journal.

19. (mitchell2023acomprehensivesurvey pages 2-4): Erika J. Mitchell and Seth H. Frisbie. A comprehensive survey and analysis of international drinking water regulations for inorganic chemicals with comparisons to the world health organization’s drinking-water guidelines. PLOS ONE, 18:e0287937, Nov 2023. URL: https://doi.org/10.1371/journal.pone.0287937, doi:10.1371/journal.pone.0287937. This article has 33 citations and is from a peer-reviewed journal.

20. (pullella2024elucidatingtherelationship pages 41-44): K Pullella. Elucidating the relationship between arsenic exposure and cancer risk in canada. Unknown journal, 2024.

21. (o’connor2024unravelingthegenetics pages 2-3): Callan O’Connor, Gregory R. Keele, Whitney Martin, Timothy Stodola, Daniel Gatti, Brian R. Hoffman, Ron Korstanje, Gary A. Churchill, and Laura G. Reinholdt. Unraveling the genetics of arsenic toxicity with cellular morphology qtl. PLOS Genetics, 20:e1011248, Apr 2024. URL: https://doi.org/10.1371/journal.pgen.1011248, doi:10.1371/journal.pgen.1011248. This article has 6 citations and is from a domain leading peer-reviewed journal.

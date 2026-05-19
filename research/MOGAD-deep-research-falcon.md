---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-03T17:22:06.867394'
end_time: '2026-05-03T17:36:05.472614'
duration_seconds: 838.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MOGAD
  mondo_id: MONDO:1040024
  category: Neurological Disorder
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
- **Disease Name:** MOGAD
- **MONDO ID:** MONDO:1040024 (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **MOGAD** covering all of the
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
- **Disease Name:** MOGAD
- **MONDO ID:** MONDO:1040024 (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **MOGAD** covering all of the
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


# Comprehensive Research Report: Myelin Oligodendrocyte Glycoprotein Antibody–Associated Disease (MOGAD)

**Target disease:** MOGAD (myelin oligodendrocyte glycoprotein antibody–associated disease)  
**Category:** Neurological disorder; autoimmune inflammatory demyelinating disease of the CNS  
**MONDO:** MONDO:1040024 (provided by requester; not re-verified in this tool run)

**Evidence note (PMIDs):** The retrieved full texts/records in this run provided DOIs/URLs and journal metadata but did not expose PMIDs in the extracted snippets; therefore, PMID-first citation could not be satisfied from tool-accessible context. All major claims are still cited to the retrieved sources.

---

## 1. Disease Information

### 1.1 Overview (current understanding)
MOGAD is a rare, antibody-mediated inflammatory demyelinating disorder of the central nervous system (CNS) associated with serum (and sometimes CSF) **MOG-IgG** detected by cell-based assays, and is considered distinct from multiple sclerosis (MS) and aquaporin-4 (AQP4)-IgG neuromyelitis optica spectrum disorder (NMOSD). (voase2024diagnosticcriteriafor pages 1-2, alani2023myelinoligodendrocyteglycoprotein pages 3-4, jeyakumar2024mogantibodyassociatedoptic pages 1-2)

**Direct abstract quote (definition/distinct entity):**
- Gklinos & Dobson (2024-05-xx) state: “Clinical syndromes associated with antibodies against myelin oligodendrocyte glycoprotein (MOG) are now recognized as a distinct neurological disease entity…” (Antibodies; https://doi.org/10.3390/antib13020043) (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3)

### 1.2 Key identifiers and terminologies
- **Preferred name:** Myelin oligodendrocyte glycoprotein antibody–associated disease (MOGAD). (alani2023myelinoligodendrocyteglycoprotein pages 3-4)
- **Common synonyms:** MOG antibody disease; MOG-IgG–associated disease; MOG-IgG–associated disorder(s); MOG encephalomyelitis (legacy terminology). (alani2023myelinoligodendrocyteglycoprotein pages 3-4, forcadela2024timingofmogigg pages 1-2)
- **ICD/MeSH/Orphanet/OMIM codes:** Not extractable from the retrieved evidence snippets in this run; a 2025 review notes existence of “unique international classification of diseases code (ICD-10-…)” but the code string was not present in accessible text. (NCT05271409 chunk 3)

### 1.3 Evidence provenance
Most knowledge summarized here is derived from aggregated disease-level resources (multi-center cohorts, registries, systematic reviews, consensus criteria, and clinical trial registries), not single-patient EHR-derived datasets. (alani2023myelinoligodendrocyteglycoprotein pages 3-4, forcadela2024timingofmogigg pages 1-2, varley2024validationofthe pages 1-2, NCT05063162 chunk 1, NCT05271409 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic)
MOGAD is primarily an **autoantibody-associated** disease targeting MOG (a surface myelin/oligodendrocyte protein). Pathogenesis likely requires cooperation between humoral immunity (MOG-IgG) and cellular immune processes, as well as CNS barrier dysfunction permitting antibody/immune cell access. (abraham2024myelinoligodendrocyteantibody pages 10-13, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3, abraham2024myelinoligodendrocyteantibody pages 8-10)

### 2.2 Risk factors
**Demographic risk context (not causal):** disease occurs in both children and adults with a biphasic age distribution (see Epidemiology). (jeyakumar2024mogantibodyassociatedoptic pages 1-2)

**Potential triggers (environment/infectious):** initiating events proposed include infections leading to autoimmunity (molecular mimicry, bystander activation, polyclonal B-cell activation). (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3)

**Risk factors for relapsing course (prognostic):** higher MOG-IgG titers and persistence of seropositivity are associated with relapsing disease; relapses cluster early and can follow steroid taper/cessation. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 10-11, alani2023myelinoligodendrocyteglycoprotein pages 10-11)

### 2.3 Protective factors
Seroconversion to MOG-IgG negativity is associated with a lower relapse likelihood (e.g., ~90% likelihood of monophasic course in one 2024 review). (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 10-11)

### 2.4 Gene–environment interactions
No robust gene–environment interaction evidence was extractable from the retrieved sources in this run.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (with frequency/characteristics)
MOGAD is defined by a compatible **core demyelinating event**, commonly including optic neuritis, myelitis, ADEM, brain/brainstem syndromes, and cortical encephalitis (often with seizures). (alani2023myelinoligodendrocyteglycoprotein pages 8-9, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10)

**Optic neuritis (ON)**
- Frequency: most common initial adult manifestation ~30–60%. (jeyakumar2024mogantibodyassociatedoptic pages 1-2)
- Common distinguishing features: bilateral involvement, disc swelling, longitudinally extensive optic nerve hyperintensity, optic perineuritis. (jeyakumar2024mogantibodyassociatedoptic pages 1-2, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10)

**Transverse myelitis (TM)**
- Frequency: ~10–25% (one review) to ~30% (another review) in adults. (jeyakumar2024mogantibodyassociatedoptic pages 1-2, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 4-5)
- Spinal cord features include LETM and gray-matter–predominant “H-sign” lesions; conus involvement is common. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 5-7, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 7-8)

**Acute disseminated encephalomyelitis (ADEM)**
- Frequency: common in children, ~45% in children <11 years in one review; >50% in children <11 in another review. (jeyakumar2024mogantibodyassociatedoptic pages 1-2, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 4-5)

**Cortical encephalitis / FLAMES**
- Reported phenotype characterized by unilateral cortical FLAIR hyperintensity and focal seizures that may generalize. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 3-4, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 5-7)

### 3.2 Suggested HPO terms (examples; not exhaustive)
(Provided as ontology suggestions; not verified against HPO database during this run.)
- Optic neuritis: **HP:0000648** (Optic neuritis)
- Visual impairment: **HP:0000505** (Visual impairment)
- Transverse myelitis / myelitis: **HP:0002303** (Myelitis) / **HP:0002375** (Transverse myelitis)
- Paraparesis/quadriparesis: **HP:0003401** (Paraparesis) / **HP:0002376** (Quadriplegia)
- Bladder dysfunction: **HP:0000010** (Neurogenic bladder)
- Seizures: **HP:0001250** (Seizures)
- Encephalopathy: **HP:0001298** (Encephalopathy)
- Headache: **HP:0002315** (Headache)

### 3.3 Quality of life impact
Direct QoL instruments/results specific to MOGAD were not extractable from the obtained papers; however, relapse-driven disability is repeatedly emphasized, and QoL is an endpoint in ongoing interventional trials (e.g., EQ-5D-3L in NCT05349006). (NCT05349006 chunk 1)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes / inheritance
MOGAD is not established as a monogenic disorder; no causal germline variants were supported by retrieved evidence in this run. (alani2023myelinoligodendrocyteglycoprotein pages 3-4, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3)

### 4.2 Pathogenic variants, modifier genes, epigenetics
No validated pathogenic variants, modifier genes, or epigenetic drivers were extractable from the retrieved evidence in this run.

### 4.3 Molecular target
**MOG** is a CNS myelin/oligodendrocyte surface protein with an extracellular Ig-like domain that is immunogenic and accessible to antibodies. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3)

---

## 5. Environmental Information

### 5.1 Environmental/lifestyle factors
No specific toxins/pollution/lifestyle factors were supported by retrieved evidence in this run.

### 5.2 Infectious agents (triggering)
Infections are proposed triggers via immune activation/molecular mimicry; specific pathogen-level causality remains uncertain in the retrieved evidence. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (current model)
A convergent contemporary model is:
1) Peripheral activation of MOG-reactive B cells/plasma cells (sometimes after systemic inflammation/infection) → generation of MOG-IgG (often IgG1). (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3, abraham2024myelinoligodendrocyteantibody pages 29-31)
2) CNS barrier dysfunction (BBB/blood–CSF barrier) enables entry of MOG-IgG and immune cells. (abraham2024myelinoligodendrocyteantibody pages 8-10, abraham2024myelinoligodendrocyteantibody pages 5-8)
3) Antibody binds conformational extracellular epitopes of MOG on myelin/oligodendrocytes and triggers effector mechanisms including complement activation, ADCC/ADCP, and downstream oligodendrocyte signaling/cytoskeletal disruption → inflammatory demyelination with perivenous/confluent lesion architecture. (abraham2024myelinoligodendrocyteantibody pages 10-13, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3, abraham2024myelinoligodendrocyteantibody pages 5-8, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 3-4)
4) Clinical manifestations depend on site of demyelination (optic nerve, spinal cord, brain/cortex). (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 5-7)

### 6.2 Key pathways and processes
- **Complement-dependent cytotoxicity (CDC)** and **antibody-dependent cellular cytotoxicity/phagocytosis (ADCC/ADCP)** are described as candidate effector mechanisms. (abraham2024myelinoligodendrocyteantibody pages 10-13, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3)
- Intracellular signaling perturbations in oligodendrocytes (e.g., MAPK/AKT) and cytoskeletal disruption are described as possible downstream mechanisms. (abraham2024myelinoligodendrocyteantibody pages 10-13)

### 6.3 Suggested GO biological process terms (examples)
(Ontology suggestions; not database-validated in this run.)
- **GO:0006955** immune response
- **GO:0006954** inflammatory response
- **GO:0002443** leukocyte mediated immunity
- **GO:0002250** adaptive immune response
- **GO:0002252** immune effector process
- **GO:0002479** antigen processing and presentation
- **GO:0002526** acute inflammatory response
- **GO:0006935** chemotaxis (for recruited myeloid cells)
- **GO:0006898** receptor-mediated endocytosis / phagocytosis-related terms (for ADCP)

### 6.4 Cell types involved (suggested CL terms)
(Ontology suggestions; not database-validated in this run.)
- Oligodendrocyte: **CL:0000128**
- Microglia: **CL:0000129**
- Macrophage: **CL:0000235**
- CD4-positive T cell: **CL:0000624**
- B cell / plasma cell: **CL:0000236** / **CL:0000786**

---

## 7. Anatomical Structures Affected

### 7.1 Organ and system level
Primary: **central nervous system**—optic nerves, spinal cord, brain (including cortex in FLAMES), brainstem/cerebellar pathways. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 5-7)

### 7.2 Suggested UBERON terms (examples)
(Ontology suggestions; not database-validated in this run.)
- Optic nerve: **UBERON:0000940**
- Spinal cord: **UBERON:0002240**
- Brain: **UBERON:0000955**
- Cerebral cortex: **UBERON:0000956**

### 7.3 Subcellular localization
Pathogenic binding occurs at the **cell surface** of myelin/oligodendrocytes (MOG is on outermost myelin). (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3)

---

## 8. Temporal Development

### 8.1 Onset
MOGAD can present in childhood or adulthood with acute/subacute demyelinating attacks; age distribution is biphasic (5–10 years; 20–45 years). (jeyakumar2024mogantibodyassociatedoptic pages 1-2)

### 8.2 Progression and course
MOGAD can be monophasic or relapsing; a 2024 review summarized **~65% monophasic and ~35% relapsing**. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10)

Relapses tend to occur early (often within 6–12 months) and are frequently temporally associated with steroid taper/cessation. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 10-11, wolf2023emergingprinciplesfor pages 4-6)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent estimates)
From a 2024 neuro-ophthalmology review:
- Annual incidence: **~1.6–4.8 per million**
- Prevalence: **~1.3–2.5 per 100,000**
- Biphasic age peaks: **5–10 years** and **20–45 years**; median onset **~20–30 years**
- Sex ratio: approximately **F:M 1:1** (with another review suggesting slight female predominance ~1.5:1). (jeyakumar2024mogantibodyassociatedoptic pages 1-2, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 7-8)

---

## 10. Diagnostics

### 10.1 Diagnostic criteria (2023 International MOGAD Panel)
Multiple 2024 validation studies and reviews summarize a **three-step** diagnostic logic:
1) Identify a **core clinical demyelinating event** (e.g., ON, TM, ADEM, brain/brainstem/cerebellar syndrome, cortical encephalitis with seizures). (alani2023myelinoligodendrocyteglycoprotein pages 8-9, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10)
2) Demonstrate **MOG-IgG positivity** (preferably in serum) using a **cell-based assay**, ideally a live CBA using full-length human MOG. (alani2023myelinoligodendrocyteglycoprotein pages 3-4, forcadela2024timingofmogigg pages 1-2)
3) **Exclude** alternative diagnoses (especially MS and AQP4-IgG NMOSD). (voase2024diagnosticcriteriafor pages 1-2, forcadela2024timingofmogigg pages 1-2)

Low-positive or ambiguous serology requires supportive clinical/MRI evidence. (alani2023myelinoligodendrocyteglycoprotein pages 8-9, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10)

A cropped table from a 2023 review that reproduces the criteria is provided in the evidence base. (alani2023myelinoligodendrocyteglycoprotein media 796e2466)

### 10.2 Assay methodology and interpretation (titer/PPV)
- Cell-based assays are emphasized; ELISA is discouraged due to lower specificity and discordance. (alani2023myelinoligodendrocyteglycoprotein pages 3-4)
- PPV varies strongly by titer and by testing population. One 2024 study reported PPV of MOG-IgG “at any time” **78.3% overall**, **52.6% for low titer**, **90.1% for high titer**, and much higher PPV in children vs adults. (varley2024validationofthe pages 1-2)
- Reviews summarize that low titers can generate false positives and require careful clinical/MRI correlation. (alani2023myelinoligodendrocyteglycoprotein pages 3-4, rechtman2024assessingtheapplicability pages 1-2, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 7-8)

### 10.3 Supportive MRI/CSF features
Supportive imaging features (particularly important for low-positive results) include: bilateral ON, >50% optic nerve involvement, optic disc edema, optic perineuritis; LETM, central cord/H-sign, conus involvement; fluffy, poorly demarcated deep gray/cortical/brainstem lesions. (alani2023myelinoligodendrocyteglycoprotein pages 8-9, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 5-7, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 7-8)

CSF: pleocytosis and elevated protein in ~50%; oligoclonal bands uncommon (<10–15%). (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 7-8)

### 10.4 Diagnostic accuracy and validation (2024)
- Varley et al. (Neurology; 2024-07) reported high performance of the 2023 criteria in a selected cohort: sensitivity **96.5%**, specificity **98.9%**, PPV **94.3%**, NPV **99.3%**, accuracy **98.5%**. (https://doi.org/10.1212/WNL.0000000000209321) (varley2024validationofthe pages 1-2)
- Forcadela et al. (NNI; 2024-01) emphasized timing: low-positive results correlate with delayed sampling and criteria can miss cases if testing is delayed or investigations are incomplete; they report sensitivity **97%** and specificity **100%** in their cohort. (https://doi.org/10.1212/nxi.0000000000200183) (forcadela2024timingofmogigg pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Disability and relapse contribution
Reviews emphasize that relapses are a major driver of disability and that predicting relapse at diagnosis remains difficult; persistent seropositivity and high titers support higher relapse risk. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 10-11, alani2023myelinoligodendrocyteglycoprotein pages 10-11)

### 11.2 Prognostic biomarkers (candidate)
A 2024 review summarizes multiple candidate predictors (none fully validated): persistent seropositivity at 3 months, higher titers, certain epitope specificities, CSF protein/leukocytes, PLR, serum neurofilament light chain, polyphasic first attack, comorbid immunologic disease. (abraham2024myelinoligodendrocyteantibody pages 27-29)

---

## 12. Treatment

### 12.1 Acute relapse treatment (real-world implementation)
**Corticosteroids** are first-line and MOGAD attacks are typically highly steroid responsive; an extended taper is commonly used to mitigate early relapse risk. (alani2023myelinoligodendrocyteglycoprotein pages 9-10, wolf2023emergingprinciplesfor pages 4-6)

Quantitative observational outcomes:
- A retrospective dataset summarized in Wolf et al. (2023-11) reported outcomes after IVMP across 122 relapses: **50% complete/nearly complete recovery**, **44.3% partial recovery**, **7% minimal/no recovery**. (https://doi.org/10.1007/s11940-023-00776-1) (wolf2023emergingprinciplesfor pages 3-4)
- A review summarized a retrospective comparison with response rates **96% IVMP**, **90% PLEX**, **91% IVIG**. (abraham2024myelinoligodendrocyteantibody pages 17-20)

Second-line/adjunct in refractory or severe attacks: **plasma exchange (PLEX)** and **IVIG**. (wolf2023emergingprinciplesfor pages 3-4)

### 12.2 Maintenance (relapse prevention; off-label practice)
Commonly considered after ≥2 attacks, with some experts considering earlier in severe poor-recovery cases. (wolf2023emergingprinciplesfor pages 4-6)

Evidence synthesis (observational):
- **IVIG**: multicenter cohort summarized by Wolf et al. shows ARR reduction **1.4 → 0.39**; relapse occurred in **34% overall** but **17%** with ≥1 g/kg every 4 weeks; only **3%** discontinued due to adverse events. (wolf2023emergingprinciplesfor pages 6-8)
- **Azathioprine (AZA) / Mycophenolate mofetil (MMF)**: may reduce ARR in some retrospective series but up to ~50% relapse; delayed onset (3–6 months) often requires bridging with steroids; notable safety monitoring needs (e.g., TPMT testing for AZA). (wolf2023emergingprinciplesfor pages 6-8, wolf2023emergingprinciplesfor pages 4-6)
- **Rituximab (anti-CD20)**: meta-analytic support for ARR reduction, but potentially less effective than in AQP4+ NMOSD; relapses may occur without link to B-cell repletion. (wolf2023emergingprinciplesfor pages 6-8)
- **IL-6 receptor blockade (tocilizumab/satralizumab)**: biologically plausible with supportive retrospective series; Wolf et al. note retrospective series with relapse reduction and report (largest series) **73% relapse-free >1 year**. (wolf2023emergingprinciplesfor pages 8-9)
- **FcRn inhibition (rozanolixizumab)**: rationale is reducing pathogenic IgG by blocking FcRn-mediated IgG recycling; now being tested in phase 3. (wolf2023emergingprinciplesfor pages 8-9, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 11-13)

### 12.3 Treatment ontology suggestions (MAXO; examples)
(Ontology suggestions; not database-validated in this run.)
- High-dose corticosteroid therapy: MAXO term for systemic glucocorticoid therapy
- Plasma exchange: MAXO term for therapeutic plasma exchange
- Intravenous immunoglobulin therapy: MAXO term for IVIG administration
- Anti-CD20 monoclonal antibody therapy (rituximab)
- Immunosuppressive therapy (azathioprine, mycophenolate)
- Anti–IL-6 receptor therapy (tocilizumab, satralizumab)
- FcRn inhibitor therapy (rozanolixizumab)

---

## 13. Prevention
No established primary prevention exists; secondary/tertiary prevention focuses on:
- Accurate diagnosis (avoid false positives/overdiagnosis due to low titers and non-specific testing). (alani2023myelinoligodendrocyteglycoprotein pages 3-4, varley2024validationofthe pages 1-2, rechtman2024assessingtheapplicability pages 1-2)
- Relapse prevention using prolonged steroid taper and/or maintenance immunotherapy in relapsing disease. (wolf2023emergingprinciplesfor pages 4-6, wolf2023emergingprinciplesfor pages 6-8)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary MOGAD analog evidence was retrieved in this run.

---

## 15. Model Organisms
Mechanistic work includes animal model evidence that anti-MOG antibodies can be pathogenic in the presence of myelin-reactive T cells; translation is complicated because many human MOG antibodies do not bind rodent MOG. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3)

---

## Recent developments (2023–2024 emphasis)

1) **Formal diagnostic criteria (2023) and real-world validation (2024):** Multiple 2024 studies report high sensitivity/specificity and highlight timing and supportive-feature requirements for low-positive titers. (forcadela2024timingofmogigg pages 1-2, varley2024validationofthe pages 1-2, rechtman2024assessingtheapplicability pages 1-2)
2) **Quantitative emphasis on test interpretation:** 2024 PPV analysis shows marked drop in PPV for low titers and for patients lacking a core demyelinating attack. (varley2024validationofthe pages 1-2)
3) **Shift toward targeted relapse-prevention trials:** Phase 3 trials are actively evaluating FcRn inhibition (rozanolixizumab) and IL-6 blockade (satralizumab); a phase 3 immunosuppressant strategy trial (azathioprine) and a randomized tocilizumab trial are ongoing. (NCT05063162 chunk 1, NCT05271409 chunk 1, NCT05349006 chunk 1, NCT06452537 chunk 1)

---

## Current applications and real-world implementations
- **Standard of care** in most centers uses high-dose steroids for acute attacks, early escalation to IVIG/PLEX if poor response, and individualized relapse-prevention therapy (often IVIG, AZA/MMF, rituximab, with increasing interest in IL-6 blockade). (wolf2023emergingprinciplesfor pages 3-4, wolf2023emergingprinciplesfor pages 6-8, wolf2023emergingprinciplesfor pages 8-9)
- **Monitoring**: serial MOG-IgG titers are sometimes followed; seronegativity by ~12 months is associated with monophasic course in one review (but later re-positivity can occur). (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 10-11)

---

## Expert opinion / analysis (authoritative sources)
- Diagnostic caution is repeatedly stressed: **testing is meaningful only with compatible phenotype and imaging**, and low titers require careful weighting because PPV depends on pretest probability and population prevalence. (alani2023myelinoligodendrocyteglycoprotein pages 3-4, varley2024validationofthe pages 1-2)
- Treatment evidence remains dominated by retrospective cohorts; expert reviews emphasize the urgent need for RCTs and biomarkers to guide long-term immunotherapy decisions. (wolf2023emergingprinciplesfor pages 8-9, abraham2024myelinoligodendrocyteantibody pages 20-22)

---

## Key statistics (selected)
- Incidence: **1.6–4.8 per million/year**; prevalence: **1.3–2.5 per 100,000**. (jeyakumar2024mogantibodyassociatedoptic pages 1-2)
- Biphasic age peaks: **5–10 years** and **20–45 years**; median onset ~**20–30 years**. (jeyakumar2024mogantibodyassociatedoptic pages 1-2)
- Course: **~65% monophasic / 35% relapsing** (review summary). (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10)
- CSF: pleocytosis ~**50%**; oligoclonal bands **<10–15%**. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 7-8)
- Diagnostic criteria validation (2024): sensitivity **96.5%**, specificity **98.9%** (selected cohort). (varley2024validationofthe pages 1-2)
- Acute IVMP outcomes (retrospective): **50%** complete/nearly complete recovery, **44.3%** partial, **7%** minimal/no recovery. (wolf2023emergingprinciplesfor pages 3-4)
- IVIG maintenance (multicenter cohort summary): ARR **1.4 → 0.39**; relapse on IVIG **34% overall**, **17%** with ≥1 g/kg q4w; AE discontinuation **3%**. (wolf2023emergingprinciplesfor pages 6-8)

---

## Visual evidence: 2023 criteria table
A cropped table summarizing the 2023 International MOGAD Panel diagnostic criteria (core clinical events, titer thresholds, and supportive features) is available from Al-Ani et al. (2023). (alani2023myelinoligodendrocyteglycoprotein media 796e2466)

---

## Structured summary artifact
| Domain | Key points | Key citations |
|---|---|---|
| Definition/IDs | • MOGAD = myelin oligodendrocyte glycoprotein antibody-associated disease, a distinct autoimmune inflammatory demyelinating CNS disorder recognized as separate from MS and AQP4-NMOSD. • 2023 international criteria use a 3-step framework: (1) core clinical demyelinating event, (2) positive serum MOG-IgG by cell-based assay, (3) exclusion of a better diagnosis. • Recommended serology: full-length human MOG cell-based assay; live CBA preferred/most specific in reviews. | (voase2024diagnosticcriteriafor pages 1-2, alani2023myelinoligodendrocyteglycoprotein pages 3-4, varley2024validationofthe pages 1-2) |
| Core phenotypes | • Adults: optic neuritis is most common initial phenotype (~30–60%; ~50% in some adult cohorts), transverse myelitis ~10–30%. • Children: ADEM is common, especially age <11 years (~45% to >50% initial presentations); cortical encephalitis/FLAMES with seizures is a recognized phenotype. • Disease course may be monophasic or relapsing; one 2024 review summarizes ~65% monophasic and ~35% relapsing overall. | (jeyakumar2024mogantibodyassociatedoptic pages 1-2, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 4-5, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 3-4) |
| Diagnostics | • 2023 criteria: clear-positive serum titer ≥1:100 on fixed CBA can support diagnosis without extra supportive features; low-positive titers ≥1:10 and <1:100 require AQP4-IgG negativity plus ≥1 supporting clinical/MRI feature. • Supportive MRI features: ON—bilateral simultaneous involvement, >50% optic nerve length involvement, optic disc edema, perineural sheath enhancement; myelitis—LETM, central/H-sign lesion, conus lesion; brain—fluffy deep gray/brainstem/cortical lesions. • PPV of MOG-IgG testing varies by titer and population: overall 78.3%; low titer 52.6%; high titer 90.1%; live CBA PPV reported ~51% at 1:20–1:40, 82% at 1:100, 100% at 1:1000; low-positive results and delayed sampling need caution. | (alani2023myelinoligodendrocyteglycoprotein pages 8-9, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10, alani2023myelinoligodendrocyteglycoprotein pages 3-4, forcadela2024timingofmogigg pages 1-2, varley2024validationofthe pages 1-2) |
| Epidemiology | • Annual incidence ~1.6–4.8 per million; prevalence ~1.3–2.5 per 100,000. • Age is biphasic: peaks at 5–10 years and 20–45 years; median onset ~20–30 years. • Sex ratio is near equal in one 2024 review (F:M ~1:1), though another review notes slight female predominance (~1.5:1). | (jeyakumar2024mogantibodyassociatedoptic pages 1-2, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 7-8) |
| Pathophysiology | • Target antigen MOG is on the outermost myelin/oligodendrocyte surface; pathogenic MOG-IgG1 binds conformational extracellular epitopes. • Proposed mechanism: peripheral B-cell/antibody response + T-cell cooperation, BBB disruption, then antibody-mediated injury via complement-dependent cytotoxicity, ADCC, ADCP/opsonization and oligodendrocyte signaling/cytoskeletal disruption. • Pathology often shows perivenous/confluent demyelination, gray + white matter involvement, CD4+/granulocytic inflammation, relative astrocyte sparing, and frequent remyelination/shrinking lesions after attacks. | (abraham2024myelinoligodendrocyteantibody pages 10-13, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3, abraham2024myelinoligodendrocyteantibody pages 1-5, abraham2024myelinoligodendrocyteantibody pages 5-8, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 3-4) |
| Key MRI/CSF findings | • Optic neuritis MRI: bilateral/anterior optic pathway involvement, enhancement in almost all ON cases, often extending >50% of nerve length; optic perineuritis and disc edema are characteristic. • Spinal MRI: LETM common, but >50% of spinal lesions may be short; gray-matter-predominant H-sign and conus involvement are typical. • CSF: pleocytosis in ~50%, elevated protein in ~50%, oligoclonal bands uncommon (<10–15%). | (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 5-7, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 7-8) |
| Prognosis/relapse predictors | • Persistent MOG-IgG seropositivity and high titers predict relapsing course; seroconversion to negativity by 12 months is associated with ~90% likelihood of a monophasic course/90% NPV for relapse. • Relapses cluster in first 6–12 months and often follow steroid taper/cessation; early relapse within 12 months raises future relapse risk. • Other reported risk factors: initial TM or encephalitis, incomplete recovery, higher CSF protein/leukocytes, polyphasic first attack, higher PLR/sNfL; prediction remains imperfect. | (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 10-11, alani2023myelinoligodendrocyteglycoprotein pages 10-11, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 11-13, abraham2024myelinoligodendrocyteantibody pages 27-29) |
| Acute treatment | • First-line: high-dose corticosteroids (commonly IV methylprednisolone ~1 g/day for 3–5 days), usually followed by prolonged taper; attacks are typically highly steroid responsive. • Retrospective data: IVMP complete/nearly complete recovery 50%, partial 44.3%, minimal/no recovery 7%; another comparison reported response rates 96% IVMP, 90% PLEX, 91% IVIG. • PLEX/IVIG used for steroid-refractory or severe attacks; in one multicenter ON series treated with PLEX, significant improvement occurred in nearly all cases. | (alani2023myelinoligodendrocyteglycoprotein pages 9-10, wolf2023emergingprinciplesfor pages 3-4, abraham2024myelinoligodendrocyteantibody pages 17-20) |
| Maintenance treatment | • Usually considered after ≥2 attacks; extended oral steroid taper lowers early relapse risk, and most relapses occur within 2 months of steroid cessation. • IVIG has strongest observational support: multicenter cohort ARR 1.4 to 0.39; relapse on IVIG 34% overall but 17% with ≥1 g/kg every 4 weeks; another review summarizes ~70% remission/majority relapse-free. • Off-label steroid-sparing agents have mixed efficacy: rituximab ~50% relapse-free in one review; mycophenolate ~47%; azathioprine ~39%; IL-6 blockers show promise, with a retrospective tocilizumab series reporting 73% relapse-free >1 year. | (wolf2023emergingprinciplesfor pages 6-8, wolf2023emergingprinciplesfor pages 8-9, gklinos2024myelinoligodendrocyteglycoproteinantibody pages 11-13, abraham2024myelinoligodendrocyteantibody pages 20-22, wolf2023emergingprinciplesfor pages 4-6) |
| Trials | • Satralizumab METEOROID (NCT05271409): Phase 3, randomized double-blind placebo-controlled, recruiting, n≈152; primary endpoint time to first adjudicated relapse. • Rozanolixizumab cosMOG (NCT05063162): Phase 3, randomized double-blind with OLE, active not recruiting, enrolled 113; primary endpoint time to first centrally adjudicated relapse. • Azathioprine in MOGAD (NCT05349006): Phase 3, placebo-controlled, recruiting, n=126, first-attack adults; Tocilizumab trial (NCT06452537): Phase 2/3, randomized open-label, active not recruiting, n≈102; primary endpoint time to first adjudicated relapse. | (NCT05271409 chunk 1, NCT05063162 chunk 1, NCT05349006 chunk 1, NCT06452537 chunk 1) |


*Table: This table condenses high-yield disease characteristics of MOGAD for knowledge-base use, including 2023 diagnostic criteria, major phenotypes, epidemiology, pathophysiology, treatment evidence, and ongoing interventional trials.*

---

## Ongoing interventional trials (ClinicalTrials.gov; real-world implementation pipeline)
- **NCT05271409 (METEOROID; satralizumab)** – Phase 3, randomized double-blind placebo-controlled, recruiting; primary endpoint: time to first adjudicated relapse; estimated n≈152; ages ≥12. (Record sponsor: Hoffmann-La Roche; start 2022; URL: https://clinicaltrials.gov/study/NCT05271409) (NCT05271409 chunk 1)
- **NCT05063162 (cosMOG; rozanolixizumab)** – Phase 3, randomized double-blind with open-label extension; **ACTIVE_NOT_RECRUITING**; enrolled 113; primary endpoint: time to first centrally adjudicated relapse. (Sponsor: UCB Biopharma SRL; start 2022-02-02; URL: https://clinicaltrials.gov/study/NCT05063162) (NCT05063162 chunk 1)
- **NCT05349006 (Azathioprine in MOGAD)** – Phase 3, placebo-controlled, recruiting; first-attack adults; primary endpoint: time to first relapse up to 3 years; includes EQ-5D-3L QoL endpoint. (Sponsor: Hospices Civils de Lyon; start 2023-12-12; URL: https://clinicaltrials.gov/study/NCT05349006) (NCT05349006 chunk 1)
- **NCT06452537 (Tocilizumab in MOGAD)** – Phase 2/3, randomized open-label, **ACTIVE_NOT_RECRUITING**; n≈102; primary endpoint: time to first adjudicated relapse. (Sponsor: Tianjin Medical University General Hospital; start 2024-07-09; URL: https://clinicaltrials.gov/study/NCT06452537) (NCT06452537 chunk 1)

---

## Limitations of this report (data availability)
- ICD/MeSH/Orphanet/OMIM identifiers and PMIDs were not directly retrievable from the tool-accessible snippets, so these could not be exhaustively enumerated. (NCT05271409 chunk 3)
- Several mechanistic/pathology statements are based on 2024 narrative reviews (including one with incomplete bibliographic metadata in the retrieved record), and should be cross-checked against primary pathology papers for formal knowledge-base curation. (abraham2024myelinoligodendrocyteantibody pages 10-13, abraham2024myelinoligodendrocyteantibody pages 1-5)

References

1. (voase2024diagnosticcriteriafor pages 1-2): Sophie Voase and Neil P. Robertson. Diagnostic criteria for mogad. Journal of Neurology, 271:3690-3692, May 2024. URL: https://doi.org/10.1007/s00415-024-12405-1, doi:10.1007/s00415-024-12405-1. This article has 4 citations and is from a domain leading peer-reviewed journal.

2. (alani2023myelinoligodendrocyteglycoprotein pages 3-4): Abdullah Al-Ani, John J. Chen, and Fiona Costello. Myelin oligodendrocyte glycoprotein antibody-associated disease (mogad): current understanding and challenges. Journal of Neurology, 270:1-19, May 2023. URL: https://doi.org/10.1007/s00415-023-11737-8, doi:10.1007/s00415-023-11737-8. This article has 72 citations and is from a domain leading peer-reviewed journal.

3. (jeyakumar2024mogantibodyassociatedoptic pages 1-2): Niroshan Jeyakumar, Magdalena Lerch, Russell C. Dale, and Sudarshini Ramanathan. Mog antibody-associated optic neuritis. Eye, 38:2289-2301, May 2024. URL: https://doi.org/10.1038/s41433-024-03108-y, doi:10.1038/s41433-024-03108-y. This article has 67 citations and is from a peer-reviewed journal.

4. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 1-3): Panagiotis Gklinos and Ruth Dobson. Myelin oligodendrocyte glycoprotein-antibody associated disease: an updated review of the clinical spectrum, pathogenetic mechanisms and therapeutic management. Antibodies, 13:43, May 2024. URL: https://doi.org/10.3390/antib13020043, doi:10.3390/antib13020043. This article has 24 citations.

5. (forcadela2024timingofmogigg pages 1-2): Mirasol Forcadela, Chiara Rocchi, Daniel San Martin, Emily L. Gibbons, Daniel Wells, Mark R. Woodhall, Patrick J. Waters, Saif Huda, and Shahd Hamid. Timing of mog-igg testing is key to 2023 mogad diagnostic criteria. Neurology Neuroimmunology &amp; Neuroinflammation, Jan 2024. URL: https://doi.org/10.1212/nxi.0000000000200183, doi:10.1212/nxi.0000000000200183. This article has 54 citations.

6. (NCT05271409 chunk 3):  A Study to Evaluate the Efficacy, Safety, Pharmacokinetics, and Pharmacodynamics of Satralizumab in Participants With Myelin Oligodendrocyte Glycoprotein Antibody-associated Disease. Hoffmann-La Roche. 2022. ClinicalTrials.gov Identifier: NCT05271409

7. (varley2024validationofthe pages 1-2): James A. Varley, Dimitrios Champsas, Timothy Prossor, Giuseppe Pontillo, Omar Abdel-Mannan, Zhaleh Khaleeli, Axel Petzold, Ahmed T. Toosy, Sachid A. Trip, Heather Wilson, Dermot H. Mallon, Cheryl Hemingway, Kshitij Mankad, Michael Kin Loon Chou, Andrew J. Church, Melanie S. Hart, Michael P. Lunn, Wallace Brownlee, Yael Hacohen, and Olga Ciccarelli. Validation of the 2023 international diagnostic criteria for mogad in a selected cohort of adults and children. Neurology, Jul 2024. URL: https://doi.org/10.1212/wnl.0000000000209321, doi:10.1212/wnl.0000000000209321. This article has 33 citations and is from a highest quality peer-reviewed journal.

8. (NCT05063162 chunk 1):  A Study to Evaluate the Efficacy and Safety of Rozanolixizumab in Adult Participants With Myelin Oligodendrocyte Glycoprotein (MOG) Antibody-associated Disease (MOGAD). UCB Biopharma SRL. 2022. ClinicalTrials.gov Identifier: NCT05063162

9. (NCT05271409 chunk 1):  A Study to Evaluate the Efficacy, Safety, Pharmacokinetics, and Pharmacodynamics of Satralizumab in Participants With Myelin Oligodendrocyte Glycoprotein Antibody-associated Disease. Hoffmann-La Roche. 2022. ClinicalTrials.gov Identifier: NCT05271409

10. (abraham2024myelinoligodendrocyteantibody pages 10-13): F Abraham. Myelin oligodendrocyte antibody associated disease (mogad): a review of mechanisms, clinical features, pathology, and new …. Unknown journal, 2024.

11. (abraham2024myelinoligodendrocyteantibody pages 8-10): F Abraham. Myelin oligodendrocyte antibody associated disease (mogad): a review of mechanisms, clinical features, pathology, and new …. Unknown journal, 2024.

12. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 10-11): Panagiotis Gklinos and Ruth Dobson. Myelin oligodendrocyte glycoprotein-antibody associated disease: an updated review of the clinical spectrum, pathogenetic mechanisms and therapeutic management. Antibodies, 13:43, May 2024. URL: https://doi.org/10.3390/antib13020043, doi:10.3390/antib13020043. This article has 24 citations.

13. (alani2023myelinoligodendrocyteglycoprotein pages 10-11): Abdullah Al-Ani, John J. Chen, and Fiona Costello. Myelin oligodendrocyte glycoprotein antibody-associated disease (mogad): current understanding and challenges. Journal of Neurology, 270:1-19, May 2023. URL: https://doi.org/10.1007/s00415-023-11737-8, doi:10.1007/s00415-023-11737-8. This article has 72 citations and is from a domain leading peer-reviewed journal.

14. (alani2023myelinoligodendrocyteglycoprotein pages 8-9): Abdullah Al-Ani, John J. Chen, and Fiona Costello. Myelin oligodendrocyte glycoprotein antibody-associated disease (mogad): current understanding and challenges. Journal of Neurology, 270:1-19, May 2023. URL: https://doi.org/10.1007/s00415-023-11737-8, doi:10.1007/s00415-023-11737-8. This article has 72 citations and is from a domain leading peer-reviewed journal.

15. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 8-10): Panagiotis Gklinos and Ruth Dobson. Myelin oligodendrocyte glycoprotein-antibody associated disease: an updated review of the clinical spectrum, pathogenetic mechanisms and therapeutic management. Antibodies, 13:43, May 2024. URL: https://doi.org/10.3390/antib13020043, doi:10.3390/antib13020043. This article has 24 citations.

16. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 4-5): Panagiotis Gklinos and Ruth Dobson. Myelin oligodendrocyte glycoprotein-antibody associated disease: an updated review of the clinical spectrum, pathogenetic mechanisms and therapeutic management. Antibodies, 13:43, May 2024. URL: https://doi.org/10.3390/antib13020043, doi:10.3390/antib13020043. This article has 24 citations.

17. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 5-7): Panagiotis Gklinos and Ruth Dobson. Myelin oligodendrocyte glycoprotein-antibody associated disease: an updated review of the clinical spectrum, pathogenetic mechanisms and therapeutic management. Antibodies, 13:43, May 2024. URL: https://doi.org/10.3390/antib13020043, doi:10.3390/antib13020043. This article has 24 citations.

18. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 7-8): Panagiotis Gklinos and Ruth Dobson. Myelin oligodendrocyte glycoprotein-antibody associated disease: an updated review of the clinical spectrum, pathogenetic mechanisms and therapeutic management. Antibodies, 13:43, May 2024. URL: https://doi.org/10.3390/antib13020043, doi:10.3390/antib13020043. This article has 24 citations.

19. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 3-4): Panagiotis Gklinos and Ruth Dobson. Myelin oligodendrocyte glycoprotein-antibody associated disease: an updated review of the clinical spectrum, pathogenetic mechanisms and therapeutic management. Antibodies, 13:43, May 2024. URL: https://doi.org/10.3390/antib13020043, doi:10.3390/antib13020043. This article has 24 citations.

20. (NCT05349006 chunk 1):  Azathioprine in MOGAD. Hospices Civils de Lyon. 2023. ClinicalTrials.gov Identifier: NCT05349006

21. (abraham2024myelinoligodendrocyteantibody pages 29-31): F Abraham. Myelin oligodendrocyte antibody associated disease (mogad): a review of mechanisms, clinical features, pathology, and new …. Unknown journal, 2024.

22. (abraham2024myelinoligodendrocyteantibody pages 5-8): F Abraham. Myelin oligodendrocyte antibody associated disease (mogad): a review of mechanisms, clinical features, pathology, and new …. Unknown journal, 2024.

23. (wolf2023emergingprinciplesfor pages 4-6): Andrew B. Wolf, Jacqueline Palace, and Jeffrey L. Bennett. Emerging principles for treating myelin oligodendrocyte glycoprotein antibody-associated disease (mogad). Current Treatment Options in Neurology, 25:437-453, Nov 2023. URL: https://doi.org/10.1007/s11940-023-00776-1, doi:10.1007/s11940-023-00776-1. This article has 5 citations and is from a peer-reviewed journal.

24. (alani2023myelinoligodendrocyteglycoprotein media 796e2466): Abdullah Al-Ani, John J. Chen, and Fiona Costello. Myelin oligodendrocyte glycoprotein antibody-associated disease (mogad): current understanding and challenges. Journal of Neurology, 270:1-19, May 2023. URL: https://doi.org/10.1007/s00415-023-11737-8, doi:10.1007/s00415-023-11737-8. This article has 72 citations and is from a domain leading peer-reviewed journal.

25. (rechtman2024assessingtheapplicability pages 1-2): Ariel Rechtman, Tal Freidman-Korn, Omri Zveik, Lyne Shweiki, Garrick Hoichman, and Adi Vaknin-Dembinsky. Assessing the applicability of the 2023 international mogad panel criteria in real-world clinical settings. Journal of Neurology, 271:5102-5108, May 2024. URL: https://doi.org/10.1007/s00415-024-12438-6, doi:10.1007/s00415-024-12438-6. This article has 10 citations and is from a domain leading peer-reviewed journal.

26. (abraham2024myelinoligodendrocyteantibody pages 27-29): F Abraham. Myelin oligodendrocyte antibody associated disease (mogad): a review of mechanisms, clinical features, pathology, and new …. Unknown journal, 2024.

27. (alani2023myelinoligodendrocyteglycoprotein pages 9-10): Abdullah Al-Ani, John J. Chen, and Fiona Costello. Myelin oligodendrocyte glycoprotein antibody-associated disease (mogad): current understanding and challenges. Journal of Neurology, 270:1-19, May 2023. URL: https://doi.org/10.1007/s00415-023-11737-8, doi:10.1007/s00415-023-11737-8. This article has 72 citations and is from a domain leading peer-reviewed journal.

28. (wolf2023emergingprinciplesfor pages 3-4): Andrew B. Wolf, Jacqueline Palace, and Jeffrey L. Bennett. Emerging principles for treating myelin oligodendrocyte glycoprotein antibody-associated disease (mogad). Current Treatment Options in Neurology, 25:437-453, Nov 2023. URL: https://doi.org/10.1007/s11940-023-00776-1, doi:10.1007/s11940-023-00776-1. This article has 5 citations and is from a peer-reviewed journal.

29. (abraham2024myelinoligodendrocyteantibody pages 17-20): F Abraham. Myelin oligodendrocyte antibody associated disease (mogad): a review of mechanisms, clinical features, pathology, and new …. Unknown journal, 2024.

30. (wolf2023emergingprinciplesfor pages 6-8): Andrew B. Wolf, Jacqueline Palace, and Jeffrey L. Bennett. Emerging principles for treating myelin oligodendrocyte glycoprotein antibody-associated disease (mogad). Current Treatment Options in Neurology, 25:437-453, Nov 2023. URL: https://doi.org/10.1007/s11940-023-00776-1, doi:10.1007/s11940-023-00776-1. This article has 5 citations and is from a peer-reviewed journal.

31. (wolf2023emergingprinciplesfor pages 8-9): Andrew B. Wolf, Jacqueline Palace, and Jeffrey L. Bennett. Emerging principles for treating myelin oligodendrocyte glycoprotein antibody-associated disease (mogad). Current Treatment Options in Neurology, 25:437-453, Nov 2023. URL: https://doi.org/10.1007/s11940-023-00776-1, doi:10.1007/s11940-023-00776-1. This article has 5 citations and is from a peer-reviewed journal.

32. (gklinos2024myelinoligodendrocyteglycoproteinantibody pages 11-13): Panagiotis Gklinos and Ruth Dobson. Myelin oligodendrocyte glycoprotein-antibody associated disease: an updated review of the clinical spectrum, pathogenetic mechanisms and therapeutic management. Antibodies, 13:43, May 2024. URL: https://doi.org/10.3390/antib13020043, doi:10.3390/antib13020043. This article has 24 citations.

33. (NCT06452537 chunk 1): Chao Zhang. Safety and Efficacy of Tocilizumab in Patients With Myelin Oligodendrocyte Glycoprotein Antibody-associated Disease. Tianjin Medical University General Hospital. 2024. ClinicalTrials.gov Identifier: NCT06452537

34. (abraham2024myelinoligodendrocyteantibody pages 20-22): F Abraham. Myelin oligodendrocyte antibody associated disease (mogad): a review of mechanisms, clinical features, pathology, and new …. Unknown journal, 2024.

35. (abraham2024myelinoligodendrocyteantibody pages 1-5): F Abraham. Myelin oligodendrocyte antibody associated disease (mogad): a review of mechanisms, clinical features, pathology, and new …. Unknown journal, 2024.

---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T12:36:23.697002'
end_time: '2026-05-08T12:54:22.727995'
duration_seconds: 1079.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Diabetes mellitus
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diabetes mellitus
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Diabetes mellitus** covering all of the
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
- **Disease Name:** Diabetes mellitus
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Diabetes mellitus** covering all of the
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


## Comprehensive Disease Characteristics Report: Diabetes Mellitus (Complex disease)

### Executive summary (current understanding)
Diabetes mellitus (DM) is a group of chronic metabolic disorders characterized by persistent hyperglycemia due to defects in insulin secretion, insulin action, or both, and it is conventionally classified into type 1 diabetes (T1D), type 2 diabetes (T2D), gestational diabetes mellitus (GDM), and other specific types (e.g., monogenic diabetes, exocrine pancreatic disease, drug/chemical-induced diabetes). (yameny2024diabetesmellitusoverview pages 1-2, care20242.diagnosisand pages 4-5)

In modern clinical practice, diabetes is increasingly viewed as heterogeneous with overlapping phenotypes and endotypes; misclassification at diagnosis is common (e.g., adults with new T1D misdiagnosed as T2D). (care20242.diagnosisand pages 4-5, care20242.diagnosisand pages 5-6)

Recent (2024) evidence syntheses show that two glucose-lowering drug classes—SGLT2 inhibitors and GLP-1 receptor agonists—provide clinically meaningful reductions in cardiovascular and kidney outcomes beyond glycemic control in high-risk adults, with partially distinct benefits (e.g., stronger heart failure benefit for SGLT2 inhibitors; stroke benefit for GLP-1 RAs). (diabetology2024theeffectivenessof pages 1-2, diabetology2024theeffectivenessof pages 5-7)

### Evidence and citation note
This report is constrained to sources retrievable via the provided tools in this run. Several ontology/identifier items (e.g., MONDO, MeSH tree, ICD-11 details, OMIM disease records) were not directly retrievable in the current tool outputs, so those elements are flagged as “not retrieved in tool-accessed sources” rather than inferred.

---

## 1. Disease information

### 1.1 What is the disease?
Diabetes mellitus is defined as persistent hyperglycemia caused by impaired insulin secretion and/or impaired insulin action, with chronic microvascular and macrovascular complications risk across types. (yameny2024diabetesmellitusoverview pages 1-2, care20242.diagnosisand pages 5-6)

### 1.2 Key identifiers
- MONDO ID: not retrieved in the tool-accessed sources for this run.
- ICD-10/ICD-11, MeSH, OMIM/Orphanet identifiers: not retrieved in the tool-accessed sources for this run.

### 1.3 Common synonyms / alternative names
Common clinical labels embedded in ADA classification include: type 1 diabetes (including latent autoimmune diabetes in adults, LADA), type 2 diabetes, gestational diabetes mellitus, and “specific types due to other causes” (including monogenic diabetes syndromes). (care20242.diagnosisand pages 4-5, care20242.diagnosisand pages 5-6)

### 1.4 Data provenance
Information used here is derived from aggregated, disease-level resources (e.g., ADA Standards of Care, meta-analyses, population surveys, and clinical trials), not individual EHR records. (care20242.diagnosisanda pages 2-2, diabetology2024theeffectivenessof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors (high level)
- **T1D**: autoimmune destruction of pancreatic β cells leading to absolute insulin deficiency, mediated largely by autoreactive T cells (including cytotoxic CD8+ T cells) and characterized by islet autoantibodies appearing before clinical onset. (thakkar2023teplizumabintype pages 1-2)
- **T2D**: progressive loss of adequate β-cell insulin secretion, frequently on a background of insulin resistance; the “paths to β-cell demise and dysfunction” are heterogeneous. (care20242.diagnosisand pages 5-6, care20242.diagnosisand pages 4-5)

Direct abstract quote supporting T1D autoimmune etiology: the teplizumab review describes T1D as “a chronic autoimmune condition characterized by the irreversible destruction of the β cells of the pancreas.” (thakkar2023teplizumabintype pages 1-2)

### 2.2 Risk factors
#### Genetic risk factors (examples)
- T1D familial aggregation and genetic susceptibility are strongly influenced by the HLA region (e.g., DR3-DQ2, DR4-DQ8), and identical-twin concordance is substantial. (thakkar2023teplizumabintype pages 1-2)
- A major diagnostic/etiologic signal for T1D risk is persistent multiple islet autoantibodies; ADA notes that “persistent presence of two or more islet autoantibodies is a near-certain predictor of clinical diabetes” in at-risk cohorts. (care20242.diagnosisand pages 5-6)

#### Environmental/lifestyle risk factors (T2D)
Large prospective evidence supports lifestyle exposures as major determinants of incident T2D:
- **Physical activity** (device-measured): In UK Biobank (n=40,431; 591 incident T2D cases over median 6.3 years), compared with <150 min/week of moderate PA, 150–300, 300–600, and >600 min/week were associated with **49%**, **62%**, and **71% lower** T2D risk, respectively. (boonpor2023dose–responserelationshipbetween pages 1-2)
- **Combined lifestyle pattern**: A 2023 Diabetes Care systematic review/meta-analysis pooling 30 cohort comparisons (n=1,693,753; 75,669 incident cases) found highest vs lowest adherence to combined low-risk lifestyle behaviors (healthy weight, healthy diet, regular exercise, non-smoking, light alcohol) associated with **80% lower** T2D risk (RR 0.20; 95% CI 0.17–0.23). (khan2023combinationofmultiple pages 1-3)

### 2.3 Protective factors
- **Multiple combined low-risk lifestyle behaviors** show strong protective association, with a graded dose–response: each additional low-risk behavior associated with ~33% lower risk (RR 0.67; 95% CI 0.64–0.70), and maximum adherence estimated RR 0.15 (95% CI 0.12–0.18). (khan2023combinationofmultiple pages 8-10)
- **Moderate-to-high physical activity** shows graded protection and only partially mediated by BMI (12–20% mediation), suggesting benefits beyond weight reduction alone. (boonpor2023dose–responserelationshipbetween pages 1-2)

### 2.4 Gene–environment interactions
Specific gene–environment interaction mechanisms were not directly retrievable in the tool-accessed sources for this run. However, the ADA Standards emphasize that both genetic and environmental factors contribute to progressive β-cell loss/dysfunction across diabetes types. (care20242.diagnosisand pages 5-6)

---

## 3. Phenotypes

### 3.1 Core phenotypes (symptoms/signs/lab abnormalities)
- **Hyperglycemia** (laboratory abnormality) defining phenotype across DM types. (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 2-2)
- **Classic hyperglycemia symptoms** (clinical phenotype) support diagnosis when random plasma glucose ≥200 mg/dL occurs with symptoms or hyperglycemic crisis. (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 2-2)
- **Diabetic ketoacidosis (DKA)** is a key acute presentation risk, especially in insulinopenic states; ADA highlights DKA prevention benefit from earlier identification/follow-up in at-risk children. (care20242.diagnosisand pages 8-9)

### 3.2 Chronic complications (high level)
All diabetes forms confer risk for chronic complications once hyperglycemia occurs, with potentially different rates of progression by diabetes subtype. (care20242.diagnosisand pages 5-6)

### 3.3 Suggested HPO terms (non-exhaustive, for knowledge base population)
Not all HPO terms were validated against HPO in this tool run; below are reasonable mapping suggestions based on standard clinical phenotype structure:
- Hyperglycemia: HP:0003074 (suggested)
- Polydipsia: HP:0001959 (suggested)
- Polyuria: HP:0000103 (suggested)
- Diabetic ketoacidosis: HP:0001953 (suggested)
- Abnormal glycated hemoglobin: HP:0030663 (suggested)

Frequency/severity estimates for symptoms/complications were not directly extractable from the tool-accessed sources for this run.

---

## 4. Genetic / molecular information

### 4.1 Causal genes
- For **polygenic T1D/T2D**, specific causal genes were not enumerated in the retrievable sources here; HLA risk is emphasized for T1D (thakkar2023teplizumabintype pages 1-2).
- For **monogenic diabetes**, ADA explicitly recognizes “monogenic diabetes syndromes” within the “specific types of diabetes due to other causes” category and provides clinical features that raise suspicion (e.g., family history, A1C <7.5% at diagnosis, syndromic features), but does not list a gene set in the extracted pages. (care20242.diagnosisand pages 4-5, care20242.diagnosisand pages 5-6)

### 4.2 Pathogenic variants / allele frequency / somatic vs germline
Not retrievable in the tool-accessed sources for this run.

### 4.3 Epigenetic information
Not retrievable in the tool-accessed sources for this run.

---

## 5. Environmental information

### 5.1 Lifestyle factors
Lifestyle determinants with strong cohort evidence are summarized above (Section 2) with quantitative risk reductions for physical activity and combined lifestyle patterns. (boonpor2023dose–responserelationshipbetween pages 1-2, khan2023combinationofmultiple pages 1-3)

### 5.2 Infectious agents
ADA notes enteroviruses (e.g., Coxsackievirus B) as associated with T1D and discusses mixed evidence regarding COVID-19 as a trigger/accelerator in susceptible individuals during the early pandemic, with later cohorts showing mixed findings and possible confounding by delayed diagnosis/access. (care20242.diagnosisand pages 8-9)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chains (simplified)
#### T1D
Genetic susceptibility and environmental triggers → loss of immune tolerance → appearance of islet autoantibodies → autoreactive T cell infiltration/β-cell killing (CD8+ T cells; impaired regulation by Tregs) → progressive β-cell loss → absolute insulin deficiency → hyperglycemia and risk of acute metabolic decompensation (e.g., DKA). (thakkar2023teplizumabintype pages 1-2, care20242.diagnosisand pages 5-6)

#### T2D
Obesogenic environment + genetic susceptibility → insulin resistance in metabolic tissues with compensatory hyperinsulinemia → progressive β-cell dysfunction and inadequate insulin secretion → chronic hyperglycemia → vascular and other tissue injury → microvascular and macrovascular complications. (care20242.diagnosisand pages 5-6, yameny2024diabetesmellitusoverview pages 1-2)

### 6.2 Key pathways/processes (ontology-mappable suggestions)
The specific pathway names (e.g., PI3K-AKT, mTOR) were not explicitly provided in the tool-accessed sources for this run, but standard disease mapping for diabetes commonly includes:
- GO biological process suggestions: “regulation of insulin secretion”, “glucose homeostasis”, “inflammatory response”, “T cell activation” (suggested; not directly validated in retrieved text).

### 6.3 Key cell types (CL suggestions)
- Pancreatic β cell (CL:0000169; suggested)
- CD8-positive, alpha-beta T cell (CL:0000625; suggested)
- Regulatory T cell (CL:0000815; suggested)

Evidence for CD8+ T cell cytotoxicity and Treg involvement in T1D is explicit in retrieved sources. (thakkar2023teplizumabintype pages 1-2)

### 6.4 Key anatomical sites (UBERON suggestions)
- Pancreas (UBERON:0001264; suggested)
- Pancreatic islet of Langerhans (UBERON:0000007; suggested)

---

## 7. Anatomical structures affected
Primary: endocrine pancreas/islets (β cells) in T1D; systemic metabolic tissues involved in insulin resistance in T2D; multi-organ vascular beds underlying chronic complications across types once hyperglycemia occurs. (care20242.diagnosisand pages 5-6, thakkar2023teplizumabintype pages 1-2)

---

## 8. Temporal development
- T1D: autoantibody seroconversion can occur early in life; ADA notes peak seroconversion between 9–24 months and that glycemic changes can precede diagnosis by months. (care20242.diagnosisand pages 5-6)
- Both T1D and T2D occur across age groups; “traditional paradigms” (T2D only adults, T1D only children) are inaccurate. (care20242.diagnosisand pages 3-4)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
- **Global**: 537 million adults (20–79) living with diabetes in 2021 (10.5%), projected to 643 million by 2030 and 783 million by 2045 (IDF-based figures cited in multiple 2024–2025 sources). (elmusharaf2025acostof pages 1-2, yameny2024diabetesmellitusoverview pages 1-2)
- **Diabetes-attributable mortality and expenditures (global, 2021)**: 6.7 million deaths and US$ 966 billion in health expenditures are cited from IDF/2021-based estimates. (elmusharaf2025acostof pages 1-2)
- **Regional example (Eastern Mediterranean Region, EMR)**: >74 million people with diabetes and ~833,000 deaths in 2023, projected to 150 million cases and 2 million deaths by 2050. (elmusharaf2025acostof pages 1-2)
- **Country example (Korea)**: adult prevalence (≥30 years) 15.5% in 2021–2022, with only 32.4% achieving HbA1c <6.5% and 15.9% achieving integrated HbA1c/BP/LDL targets. (park2025diabetesfactsheets pages 1-3)

### 9.2 Genetic architecture
The tool-accessed sources emphasize multifactorial/polygenic inheritance for common forms and highlight HLA contribution for T1D susceptibility. (thakkar2023teplizumabintype pages 1-2, care20242.diagnosisand pages 5-6)

---

## 10. Diagnostics

### 10.1 Guideline diagnostic criteria (ADA Standards of Care)
Diagnostic and prediabetes thresholds are shown in ADA tables (images extracted) and text:
- Diabetes: A1C ≥6.5%; FPG ≥126 mg/dL; 2-h OGTT ≥200 mg/dL; random plasma glucose ≥200 mg/dL with classic symptoms or crisis. (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 2-2, care20242.diagnosisand media a404318a)
- Prediabetes: A1C 5.7–6.4%; FPG 100–125 mg/dL; 2-h OGTT 140–199 mg/dL. (care20242.diagnosisand pages 2-3, care20242.diagnosisand media aa0d0872)
- Confirmation: in absence of unequivocal hyperglycemia, diagnosis requires two abnormal results (repeat or different test). (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 3-4)
- A1C caveats: use plasma glucose criteria when A1C–glycemia relationship is altered (e.g., pregnancy, hemoglobin variants, anemia/altered RBC turnover, HIV, kidney failure/dialysis). (care20242.diagnosisand pages 2-3, care20242.diagnosisand pages 3-4)

### 10.2 Biomarkers for classification
- Islet autoantibodies (e.g., GAD, IA-2, ZnT8) and C-peptide are used to support classification in adults with suspected T1D and to consider monogenic diabetes when clinical features suggest. (care20242.diagnosisand pages 4-5, care20242.diagnosisand pages 5-6)

---

## 11. Outcome / prognosis

### 11.1 Complications risk and outcomes
Once hyperglycemia occurs, all diabetes types confer risk of chronic complications; contemporary management emphasizes preventing acute complications (e.g., DKA) and reducing cardiorenal morbidity using therapies with outcomes evidence. (care20242.diagnosisand pages 5-6, diabetology2024theeffectivenessof pages 1-2)

### 11.2 Recent quantitative outcomes evidence (cardiorenal protection)
- A 2024 updated meta-analysis pooling 151,023 adults (90,943 in SGLT2 inhibitor trials; 60,080 in GLP-1RA trials) reports reductions vs standard care: CV mortality (SGLT2i 14%; GLP-1RA 13%), all-cause mortality (12% both), MACE (SGLT2i 11%; GLP-1RA 14%), HF hospitalization (SGLT2i 30%; GLP-1RA 9%), and kidney composite outcomes (SGLT2i 32%; GLP-1RA 22%). (diabetology2024theeffectivenessof pages 1-2)

---

## 12. Treatment

### 12.1 Standard of care categories (high level)
Management includes lifestyle interventions, pharmacotherapy (including insulin, GLP-1 receptor agonists, SGLT2 inhibitors), and in selected cases metabolic surgery or advanced biologic/cell therapies. (yameny2024diabetesmellitusoverview pages 1-2, care20242.diagnosisand pages 5-6)

### 12.2 Cardiorenal outcome–directed pharmacotherapy (2023–2024 emphasis)
- **SGLT2 inhibitors and GLP-1 RAs (outcomes evidence)**: the 2024 meta-analysis indicates class-level reductions across major outcomes, with differential signals (SGLT2i stronger HF hospitalization benefit; GLP-1RA stroke benefit). (diabetology2024theeffectivenessof pages 1-2, diabetology2024theeffectivenessof pages 5-7)
- **GLP-1RA CV/kidney outcomes meta-analysis (2024)**: A June 2024 meta-analysis of 13 placebo-controlled GLP-1RA CVOTs (83,258 patients) reported MACE reduction (OR 0.86, 95% CI 0.80–0.94) and kidney composite reduction (OR 0.76, 95% CI 0.67–0.85), among other endpoints. (rivera2024cardiovascularandrenal pages 1-2)
- **Semaglutide kidney outcomes in SELECT (2024, real-world adjacent implications)**: In SELECT (overweight/obesity with established CVD without diabetes), semaglutide lowered a prespecified kidney composite (1.8% vs 2.2%; HR 0.78; 95% CI 0.63–0.96) and improved eGFR slope at 104 weeks. (colhoun2024longtermkidneyoutcomes pages 1-2)

### 12.3 Advanced therapeutics (latest research; real-world implementation status varies)
- **Disease-modifying immunotherapy to delay T1D**: Teplizumab (anti-CD3) is described as FDA-licensed (Nov 2022) to delay onset of clinical T1D in high-risk individuals ≥8 years (stage 2 T1D), with proposed mechanisms including enhancement of regulatory T-cell activity and promotion of immune tolerance. (thakkar2023teplizumabintype pages 1-2)
- **β-cell replacement / stem-cell–derived islet therapy (2025, pivotal clinical development)**: A phase 1–2 study of zimislecel (VX-880; allogeneic stem cell–derived fully differentiated islets) reported detectable C-peptide after infusion in all 14 participants (all had undetectable baseline C-peptide), and among 12 full-dose recipients, 83% were insulin independent at day 365, with HbA1c <7% and >70% time in range; safety signals included neutropenia and two deaths. (reichman2025stemcellderivedfully pages 1-2)

### 12.4 MAXO term suggestions (non-exhaustive)
Not validated against MAXO in this run; suggested mappings:
- Insulin therapy; glucose monitoring; lifestyle intervention; bariatric surgery/metabolic surgery; immunotherapy (anti-CD3); islet cell transplantation/cell therapy.

---

## 13. Prevention

### 13.1 Primary prevention (T2D)
- **Physical activity**: graded dose-response protection against incident T2D in device-measured cohort data. (boonpor2023dose–responserelationshipbetween pages 1-2)
- **Multi-behavior lifestyle pattern**: very large risk reductions associated with combined low-risk lifestyle behaviors in prospective cohorts, with strong dose-response. (khan2023combinationofmultiple pages 1-3, khan2023combinationofmultiple pages 8-10)

### 13.2 Secondary prevention (screening/early detection)
ADA provides risk-based screening and emphasizes accurate use of diagnostic criteria, confirmatory testing, and appropriate selection of A1C vs plasma glucose tests depending on clinical context. (care20242.diagnosisand pages 2-3, care20242.diagnosisanda pages 2-2)

### 13.3 Tertiary prevention (prevent complications)
Outcomes-focused therapy with SGLT2 inhibitors and/or GLP-1 RAs for appropriate patients is supported by 2024 evidence synthesis showing reductions in MACE, HF hospitalization, and kidney composites. (diabetology2024theeffectivenessof pages 1-2)

---

## 14. Other species / natural disease
Not retrievable in the tool-accessed sources for this run.

---

## 15. Model organisms
Not retrievable in the tool-accessed sources for this run.

---

## Consolidated evidence table (diagnosis + key 2024–2025 outcomes)
| Domain | Measure/Endpoint | Quantitative result | Population/Context | Source (paper + year) |
|---|---|---|---|---|
| Diagnosis | Diabetes: A1C | ≥6.5% (≥48 mmol/mol) | ADA diagnostic threshold for diabetes in nonpregnant individuals; laboratory NGSP-certified assay recommended | ADA Standards of Care 2024 (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 2-2) |
| Diagnosis | Diabetes: Fasting plasma glucose | ≥126 mg/dL (≥7.0 mmol/L) | Fasting defined as no caloric intake for at least 8 h | ADA Standards of Care 2024 (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 2-2, care20242.diagnosisand pages 1-2) |
| Diagnosis | Diabetes: 2-h plasma glucose during 75-g OGTT | ≥200 mg/dL (≥11.1 mmol/L) | ADA diagnostic threshold; OGTT more sensitive than A1C in some settings | ADA Standards of Care 2024 (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 2-2) |
| Diagnosis | Diabetes: Random plasma glucose | ≥200 mg/dL (≥11.1 mmol/L) | Requires classic hyperglycemia symptoms or hyperglycemic crisis | ADA Standards of Care 2024 (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 2-2) |
| Diagnosis | Prediabetes: A1C | 5.7–6.4% (39–47 mmol/mol) | ADA high-risk/prediabetes range | ADA Standards of Care 2024 (care20242.diagnosisand pages 2-3, care20242.diagnosisanda pages 2-3, care20242.diagnosisand pages 10-10) |
| Diagnosis | Prediabetes: Fasting plasma glucose | 100–125 mg/dL (5.6–6.9 mmol/L) | Impaired fasting glucose | ADA Standards of Care 2024 (care20242.diagnosisand pages 2-3, care20242.diagnosisanda pages 2-3, care20242.diagnosisand pages 10-10) |
| Diagnosis | Prediabetes: 2-h plasma glucose during 75-g OGTT | 140–199 mg/dL (7.8–11.0 mmol/L) | Impaired glucose tolerance | ADA Standards of Care 2024 (care20242.diagnosisand pages 2-3, care20242.diagnosisanda pages 2-3, care20242.diagnosisand pages 10-10) |
| Diagnosis | Confirmation requirement | 2 abnormal results from the same or different tests unless unequivocal hyperglycemia is present | Repeat/confirmatory testing recommended when no classic symptoms | ADA Standards of Care 2024 (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 2-2, care20242.diagnosisand pages 3-4) |
| Diagnosis | Key A1C caveats | Use plasma glucose criteria instead when A1C-glycemia relationship is altered | Examples: hemoglobin variants, pregnancy, G6PD deficiency, anemia/altered RBC turnover, erythropoietin use, hemodialysis/kidney failure, HIV, transfusion/hemolysis | ADA Standards of Care 2024 (care20242.diagnosisand pages 2-3, care20242.diagnosisand pages 3-4, care20242.diagnosisanda pages 2-3) |
| Diagnosis | OGTT pre-test preparation | ≥150 g carbohydrate/day for 3 days before test | Helps avoid false-positive postchallenge glucose results | ADA Standards of Care 2024 (care20242.diagnosisand pages 2-3, care20242.diagnosisanda pages 2-3) |
| Treatment/Outcomes | SGLT2 inhibitors: CV mortality | 14% reduction | Pooled RCT meta-analysis across cardiorenal trials; total n=151,023 adults overall (90,943 in SGLT2i trials) | Sherifali et al., 2024 (diabetology2024theeffectivenessof pages 1-2) |
| Treatment/Outcomes | GLP-1 receptor agonists: CV mortality | 13% reduction | Pooled RCT meta-analysis across cardiorenal trials; total n=151,023 adults overall (60,080 in GLP-1RA trials) | Sherifali et al., 2024 (diabetology2024theeffectivenessof pages 1-2) |
| Treatment/Outcomes | SGLT2 inhibitors: MACE | 11% reduction | Pooled RCT meta-analysis | Sherifali et al., 2024 (diabetology2024theeffectivenessof pages 1-2) |
| Treatment/Outcomes | GLP-1 receptor agonists: MACE | 14% reduction | Pooled RCT meta-analysis | Sherifali et al., 2024 (diabetology2024theeffectivenessof pages 1-2) |
| Treatment/Outcomes | SGLT2 inhibitors: HF hospitalization | 30% reduction | Pooled RCT meta-analysis; in T2D subgroup, SGLT2i uniquely reduced HF hospitalization | Sherifali et al., 2024 (diabetology2024theeffectivenessof pages 1-2) |
| Treatment/Outcomes | GLP-1 receptor agonists: HF hospitalization | 9% reduction | Pooled RCT meta-analysis | Sherifali et al., 2024 (diabetology2024theeffectivenessof pages 1-2) |
| Treatment/Outcomes | SGLT2 inhibitors: Kidney composite | 32% reduction overall; 33% reduction in T2D subgroup (HR 0.67, 95% CI 0.59–0.75) | Pooled RCT meta-analysis/update | Sherifali et al., 2024 (diabetology2024theeffectivenessof pages 5-7, diabetology2024theeffectivenessof pages 1-2) |
| Treatment/Outcomes | GLP-1 receptor agonists: Kidney composite | 22% reduction overall; HR 0.78 (95% CI 0.70–0.87) in T2D subgroup | Pooled RCT meta-analysis/update | Sherifali et al., 2024 (diabetology2024theeffectivenessof pages 5-7, diabetology2024theeffectivenessof pages 1-2) |
| Treatment/Outcomes | GLP-1 receptor agonists: nonfatal stroke | 16% reduction; HR 0.84 (95% CI 0.76–0.94) | T2D subgroup meta-analysis; GLP-1RA showed stroke benefit not seen with SGLT2i | Sherifali et al., 2024 (diabetology2024theeffectivenessof pages 5-7) |
| Treatment/Outcomes | SELECT semaglutide kidney composite | 1.8% vs 2.2%; HR 0.78 (95% CI 0.63–0.96), P=0.02 | Overweight/obesity with established CVD, without diabetes; semaglutide n=8,803 vs placebo n=8,801 | Colhoun et al., 2024 (colhoun2024longtermkidneyoutcomes pages 1-2) |
| Treatment/Outcomes | SELECT semaglutide eGFR benefit at 104 weeks | +0.75 mL/min/1.73 m² overall; +2.19 mL/min/1.73 m² if baseline eGFR <60 | Prespecified kidney analysis in SELECT | Colhoun et al., 2024 (colhoun2024longtermkidneyoutcomes pages 1-2) |
| Advanced therapy | Zimislecel (VX-880): insulin independence at day 365 | 10/12 (83%) | Full-dose recipients with type 1 diabetes in phase 1–2 study; all 12/12 also free of severe hypoglycemic events and HbA1c <7% | Reichman et al., 2025 (reichman2025stemcellderivedfully pages 1-2) |
| Advanced therapy | Zimislecel (VX-880): engraftment/islet function | Detectable C-peptide in all 14 participants after infusion | Type 1 diabetes; C-peptide undetectable at baseline in all 14 | Reichman et al., 2025 (reichman2025stemcellderivedfully pages 1-2) |


*Table: This table compiles ADA diagnostic thresholds for diabetes and prediabetes, including key testing caveats, alongside recent quantitative treatment and outcome findings for SGLT2 inhibitors, GLP-1 receptor agonists, semaglutide in SELECT, and stem-cell derived islet therapy. It is useful as a compact evidence summary for diagnosis and current therapeutic impact.*

---

## Key visual evidence (guideline tables)
Images extracted from the ADA Standards include the diagnostic criteria for diabetes and prediabetes (Table 2.1/2.2) and can be used as visual support for threshold values. (care20242.diagnosisand media a404318a, care20242.diagnosisand media aa0d0872)

---

## References (URLs and publication dates available in retrieved sources)
- ADA Standards of Care (Diagnosis & Classification): “2. Diagnosis and classification of diabetes: Standards of care in diabetes—2024” (retrieved text excerpts include criteria and caveats; URL indicated in document as https://diabetesjournals.org/care). (care20242.diagnosisanda pages 2-2, care20242.diagnosisand pages 2-3)
- Sherifali et al. “The effectiveness of sodium-glucose co-transporter 2 inhibitors on cardiorenal outcomes: an updated systematic review and meta-analysis.” *Cardiovascular Diabetology*, Feb 2024. https://doi.org/10.1186/s12933-024-02154-w (diabetology2024theeffectivenessof pages 1-2)
- Rivera et al. “Cardiovascular and renal outcomes of GLP-1 receptor agonists…” *American Journal of Preventive Cardiology*, Jun 2024 (online 7 May 2024). https://doi.org/10.1016/j.ajpc.2024.100679 (rivera2024cardiovascularandrenal pages 1-2)
- Colhoun et al. “Long-term kidney outcomes of semaglutide in obesity and cardiovascular disease in the SELECT trial.” *Nature Medicine*, May 2024 (online 25 May 2024). https://doi.org/10.1038/s41591-024-03015-5 (colhoun2024longtermkidneyoutcomes pages 1-2)
- Thakkar et al. “Teplizumab in Type 1 Diabetes Mellitus: An Updated Review.” *touchREVIEWS in Endocrinology*, Oct 2023. https://doi.org/10.17925/ee.2023.19.2.7 (thakkar2023teplizumabintype pages 1-2)
- Reichman et al. “Stem Cell-Derived, Fully Differentiated Islets for Type 1 Diabetes.” *NEJM*, Jun 2025. https://doi.org/10.1056/NEJMoa2506549 (reichman2025stemcellderivedfully pages 1-2)
- Khan et al. “Combination of Multiple Low-Risk Lifestyle Behaviors and Incident Type 2 Diabetes.” *Diabetes Care*, Feb 2023. https://doi.org/10.2337/dc22-1024 (khan2023combinationofmultiple pages 1-3)
- Boonpor et al. “Dose–response relationship between device-measured physical activity and incident type 2 diabetes.” *BMC Medicine*, May 2023. https://doi.org/10.1186/s12916-023-02851-5 (boonpor2023dose–responserelationshipbetween pages 1-2)
- Elmusharaf et al. “A cost of illness study of the economic burden of diabetes in the Eastern Mediterranean Region.” *Eastern Mediterranean Health Journal*, Aug 2025 (contains IDF-based global 2021 prevalence/mortality/expenditure and EMR 2023 estimates). https://doi.org/10.26719/2025.31.7.426 (elmusharaf2025acostof pages 1-2)
- Park et al. “Diabetes Fact Sheets in Korea 2024.” *Diabetes & Metabolism Journal*, Jan 2025. https://doi.org/10.4093/dmj.2024.0818 (park2025diabetesfactsheets pages 1-3)



References

1. (yameny2024diabetesmellitusoverview pages 1-2): Ahmed Abdelhalim Yameny. Diabetes mellitus overview 2024. Journal of Bioscience and Applied Research, 10:641-645, Sep 2024. URL: https://doi.org/10.21608/jbaar.2024.382794, doi:10.21608/jbaar.2024.382794. This article has 203 citations.

2. (care20242.diagnosisand pages 4-5): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

3. (care20242.diagnosisand pages 5-6): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

4. (diabetology2024theeffectivenessof pages 1-2): Cardiovascular Diabetology, D. Sherifali, Muhammad Usman Ali, G. B. J. Mancini, D. Fitzpatrick-Lewis, Kim A. Connelly, E. O’Meara, and Shelley Zieroth. The effectiveness of sodium-glucose co-transporter 2 inhibitors on cardiorenal outcomes: an updated systematic review and meta-analysis. Cardiovascular Diabetology, Feb 2024. URL: https://doi.org/10.1186/s12933-024-02154-w, doi:10.1186/s12933-024-02154-w. This article has 21 citations and is from a peer-reviewed journal.

5. (diabetology2024theeffectivenessof pages 5-7): Cardiovascular Diabetology, D. Sherifali, Muhammad Usman Ali, G. B. J. Mancini, D. Fitzpatrick-Lewis, Kim A. Connelly, E. O’Meara, and Shelley Zieroth. The effectiveness of sodium-glucose co-transporter 2 inhibitors on cardiorenal outcomes: an updated systematic review and meta-analysis. Cardiovascular Diabetology, Feb 2024. URL: https://doi.org/10.1186/s12933-024-02154-w, doi:10.1186/s12933-024-02154-w. This article has 21 citations and is from a peer-reviewed journal.

6. (care20242.diagnosisanda pages 2-2): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

7. (thakkar2023teplizumabintype pages 1-2): Simran Thakkar, Aditi Chopra, Lakshmi Nagendra, Sanjay Kalra, and Saptarshi Bhattacharya. Teplizumab in type 1 diabetes mellitus: an updated review. touchREVIEWS in Endocrinology, 19:22-30, Oct 2023. URL: https://doi.org/10.17925/ee.2023.19.2.7, doi:10.17925/ee.2023.19.2.7. This article has 40 citations.

8. (boonpor2023dose–responserelationshipbetween pages 1-2): Jirapitcha Boonpor, Solange Parra-Soto, Fanny Petermann-Rocha, Nathan Lynskey, Verónica Cabanas-Sánchez, Naveed Sattar, Jason M. R. Gill, Paul Welsh, Jill P. Pell, Stuart R. Gray, Frederick K. Ho, and Carlos Celis-Morales. Dose–response relationship between device-measured physical activity and incident type 2 diabetes: findings from the uk biobank prospective cohort study. BMC Medicine, May 2023. URL: https://doi.org/10.1186/s12916-023-02851-5, doi:10.1186/s12916-023-02851-5. This article has 38 citations and is from a domain leading peer-reviewed journal.

9. (khan2023combinationofmultiple pages 1-3): Tauseef A. Khan, David Field, Victoria Chen, Suleman Ahmad, Sonia Blanco Mejia, Hana Kahleová, Dario Rahelić, Jordi Salas-Salvadó, Lawrence A. Leiter, Matti Uusitupa, Cyril W.C. Kendall, and John L. Sievenpiper. Combination of multiple low-risk lifestyle behaviors and incident type 2 diabetes: a systematic review and dose-response meta-analysis of prospective cohort studies. Diabetes Care, 46:643-656, Feb 2023. URL: https://doi.org/10.2337/dc22-1024, doi:10.2337/dc22-1024. This article has 77 citations and is from a highest quality peer-reviewed journal.

10. (khan2023combinationofmultiple pages 8-10): Tauseef A. Khan, David Field, Victoria Chen, Suleman Ahmad, Sonia Blanco Mejia, Hana Kahleová, Dario Rahelić, Jordi Salas-Salvadó, Lawrence A. Leiter, Matti Uusitupa, Cyril W.C. Kendall, and John L. Sievenpiper. Combination of multiple low-risk lifestyle behaviors and incident type 2 diabetes: a systematic review and dose-response meta-analysis of prospective cohort studies. Diabetes Care, 46:643-656, Feb 2023. URL: https://doi.org/10.2337/dc22-1024, doi:10.2337/dc22-1024. This article has 77 citations and is from a highest quality peer-reviewed journal.

11. (care20242.diagnosisand pages 2-2): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

12. (care20242.diagnosisand pages 8-9): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

13. (care20242.diagnosisand pages 3-4): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

14. (elmusharaf2025acostof pages 1-2): Khalifa Elmusharaf, Maisoon Mairghani, Sébastien Poix, Emil Scaria, P. Phyo, Win Thu, S. Slama, Matilda Byström, Hicham El Berri, and A. Hammerich. A cost of illness study of the economic burden of diabetes in the eastern mediterranean region. Eastern Mediterranean Health Journal, Aug 2025. URL: https://doi.org/10.26719/2025.31.7.426, doi:10.26719/2025.31.7.426. This article has 6 citations and is from a peer-reviewed journal.

15. (park2025diabetesfactsheets pages 1-3): Se Eun Park, Seung-Hyun Ko, Ji Yoon Kim, Kyuho Kim, Joon Ho Moon, Nam Hoon Kim, Kyung Do Han, Sung Hee Choi, and Bong Soo Cha. Diabetes fact sheets in korea 2024. Diabetes & Metabolism Journal, 49:24-33, Jan 2025. URL: https://doi.org/10.4093/dmj.2024.0818, doi:10.4093/dmj.2024.0818. This article has 92 citations and is from a peer-reviewed journal.

16. (care20242.diagnosisand media a404318a): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

17. (care20242.diagnosisand pages 2-3): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

18. (care20242.diagnosisand media aa0d0872): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

19. (rivera2024cardiovascularandrenal pages 1-2): Frederick Berro Rivera, Linnaeus Louisse A. Cruz, John Vincent Magalong, Jade Monica Marie J. Ruyeras, John Paul Aparece, Nathan Ross B. Bantayan, Kyla Lara-Breitinger, and Martha Gulati. Cardiovascular and renal outcomes of glucagon-like peptide 1 receptor agonists among patients with and without type 2 diabetes mellitus: a meta-analysis of randomized placebo-controlled trials. American Journal of Preventive Cardiology, 18:100679, Jun 2024. URL: https://doi.org/10.1016/j.ajpc.2024.100679, doi:10.1016/j.ajpc.2024.100679. This article has 126 citations and is from a peer-reviewed journal.

20. (colhoun2024longtermkidneyoutcomes pages 1-2): Helen M. Colhoun, Ildiko Lingvay, Paul M. Brown, John Deanfield, Kirstine Brown-Frandsen, Steven E. Kahn, Jorge Plutzky, Koichi Node, Alexander Parkhomenko, Lars Rydén, John P. H. Wilding, Johannes F. E. Mann, Katherine R. Tuttle, Thomas Idorn, Naveen Rathor, and A. Michael Lincoff. Long-term kidney outcomes of semaglutide in obesity and cardiovascular disease in the select trial. Nature Medicine, 30:2058-2066, May 2024. URL: https://doi.org/10.1038/s41591-024-03015-5, doi:10.1038/s41591-024-03015-5. This article has 238 citations and is from a highest quality peer-reviewed journal.

21. (reichman2025stemcellderivedfully pages 1-2): Trevor W. Reichman, James F. Markmann, Jon Odorico, Piotr Witkowski, John J. Fung, Martin Wijkstrom, Fouad Kandeel, Eelco J.P. de Koning, Anne L. Peters, Chantal Mathieu, Leslie S. Kean, Bote G. Bruinsma, Chenkun Wang, Molly Mascia, Bastiano Sanna, Gautham Marigowda, Felicia Pagliuca, Doug Melton, Camillo Ricordi, and Michael R. Rickels. Stem cell-derived, fully differentiated islets for type 1 diabetes. The New England journal of medicine, Jun 2025. URL: https://doi.org/10.1056/nejmoa2506549, doi:10.1056/nejmoa2506549. This article has 129 citations and is from a highest quality peer-reviewed journal.

22. (care20242.diagnosisand pages 1-2): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

23. (care20242.diagnosisanda pages 2-3): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

24. (care20242.diagnosisand pages 10-10): D Care. 2. diagnosis and classification of diabetes: standards of care in diabetes—2024. Unknown journal, 2024.

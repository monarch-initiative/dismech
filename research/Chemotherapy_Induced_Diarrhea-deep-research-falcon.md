---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T11:25:55.647974'
end_time: '2026-05-08T11:46:40.473919'
duration_seconds: 1244.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chemotherapy-Induced Diarrhea
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chemotherapy-Induced Diarrhea
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Chemotherapy-Induced Diarrhea** covering all of the
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
- **Disease Name:** Chemotherapy-Induced Diarrhea
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Chemotherapy-Induced Diarrhea** covering all of the
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


# Chemotherapy-Induced Diarrhea (CID): Comprehensive Disease Characteristics Report (2023–2025 prioritized)

## Target disease
- **Disease name:** Chemotherapy-Induced Diarrhea (CID)
- **Category:** Complex (treatment-related toxicity syndrome)
- **MONDO ID / MeSH / ICD-10/ICD-11:** Not recovered from the retrieved full-text sources in this tool run (should be added from MONDO/MeSH/ICD lookups in a follow-on curation step).

---

## 1. Disease information
### Overview / definition
Chemotherapy-induced diarrhea (CID) is diarrhea occurring during or after systemic cytotoxic therapy and is a major manifestation of chemotherapy-induced gastrointestinal toxicity (often framed as intestinal mucositis), which can impair quality of life, threaten patient safety (e.g., dehydration/electrolyte derangements), and force chemotherapy dose modifications or discontinuation. (chen2025restoreintestinalsteadystate pages 1-3, jiang2025importantroleof pages 1-2)

CID is commonly evaluated using **NCI CTCAE v5.0** severity grading (grade 1 mild → grade 5 fatal). (jiang2025importantroleof pages 1-2)

### Synonyms / alternative names
- Chemotherapy-associated diarrhea (chen2025restoreintestinalsteadystate pages 6-7)
- Cancer-therapy–related diarrhea / cancer-related diarrhea (broader umbrella including targeted therapy, immunotherapy, other causes) (aleem2024theimpactof pages 1-3)
- Chemotherapy-induced gastrointestinal toxicity (CIGT) with diarrhea phenotype (chen2025restoreintestinalsteadystate pages 6-7, cheatham2025butyratepreventschemotherapyinduced pages 24-28)

### Evidence source type
Evidence here is aggregated from **clinical trials**, **observational claims data**, **clinical practice guidance**, and **preclinical animal/in vitro studies** (see citations per section).

---

## 2. Etiology
### Primary causal factors (mechanistic)
CID is primarily caused by **treatment-related injury to intestinal epithelium and barrier function** (mucositis), coupled with changes in secretion/absorption and motility; clinically it can be conceptualized as **secretory vs osmotic** diarrhea. (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4)

Key high-risk cytotoxic agents highlighted across recent reviews/guidance include:
- **Irinotecan (topoisomerase I inhibitor)** and **fluoropyrimidines** (5-FU, capecitabine), repeatedly emphasized as high-risk drugs for CID. (andreyev2025britishsocietyof pages 15-15, venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 1-3)
- **Docetaxel** is also associated with diarrhea at meaningful rates. (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4)

### Drug-specific mechanisms
**Irinotecan (CPT-11):** a central mechanism for delayed-onset diarrhea is biotransformation to active **SN-38**, hepatic glucuronidation to **SN-38G**, and **reconversion of SN-38G to toxic SN-38 in the intestine** by microbial enzymes (β-glucuronidase in multiple sources), leading to mucosal damage. (deng2024efficacyandsafety pages 1-2, cheatham2025butyratepreventschemotherapyinduced pages 24-28)

**Fluoropyrimidines (5-FU/capecitabine):** associated with small-bowel mucosal breakdown/crypt apoptosis driven by inflammatory cytokines and oxidative stress pathways; more severe mucosal breakdown is reported with IV vs oral administration in one recent review. (chen2025restoreintestinalsteadystate pages 6-7)

### Risk factors
**Host/clinical risk factors (irinotecan delayed diarrhea):** weekly dosing schedule, poor performance status, elevated creatinine, prior abdominal/pelvic irradiation, leukopenia, age >70 years, and Gilbert syndrome/Crigler–Najjar type 1 were summarized as predictors. (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4)

**Pharmacogenomics (PGx) – irinotecan:** reduced-function **UGT1A1** genotypes (e.g., *28 in reviews) are associated with reduced SN-38 detoxification and higher toxicity risk. (chen2025restoreintestinalsteadystate pages 6-7)

**Pharmacogenomics (PGx) – fluoropyrimidines:** inherited **DPYD** variants reduce DPD activity, increasing severe fluoropyrimidine toxicity including diarrhea. In an umbrella review synthesizing 8 systematic reviews (125 primary studies), key variants repeatedly implicated were **DPYD*2A (c.1905+1G>A), DPYD*13 (c.1679T>G), c.2846A>T (p.D949V), and HapB3 (c.1236G>A)**. (oterotorres2025dpydgenotypingfluoropyrimidine pages 1-2)

Diarrhea-specific associations from the umbrella review include:
- DPYD*2A carrier diarrhea 12.0%–100% vs 1.4%–27.5% in wild-type; infusional 5-FU diarrhea OR 7.7 (95% CI 1.6–36.9). (oterotorres2025dpydgenotypingfluoropyrimidine pages 9-10)
- DPYD*13 carrier diarrhea 50%–100% vs 5.8%–22% in wild-type. (oterotorres2025dpydgenotypingfluoropyrimidine pages 9-10)
- c.2846A>T pooled OR for diarrhea 6.0 (95% CI 1.8–20.7). (oterotorres2025dpydgenotypingfluoropyrimidine pages 9-10)

### Protective factors / mitigating factors
Evidence in this retrieved set is strongest for *candidate protective interventions* rather than established protective factors:
- **Microbiome/SCFA (butyrate):** in a mouse model, butyrate supplementation prevented irinotecan-associated microbial dysbiosis and reduced features of GI toxicity, supporting a protective mechanism via barrier preservation and suppression of β-glucuronidase activity. (cheatham2025butyratepreventschemotherapyinduced pages 1-6)
- **Genotype-guided dosing:** DPYD-guided fluoropyrimidine dose reduction and titration reduces severe toxicity overall and is positioned as a patient-safety strategy; one synthesis reported reduced diarrhea with pharmacogenetics-guided dosing (RR 0.4, 95% CI 0.2–0.6). (oterotorres2025dpydgenotypingfluoropyrimidine pages 10-12, oterotorres2025dpydgenotypingfluoropyrimidine pages 1-2)

### Gene–environment (microbiome) interactions
CID risk and severity are modulated by **chemotherapy-induced dysbiosis** and host–microbe metabolism of xenobiotics. A 2025 review emphasizes that chemotherapy can decrease beneficial taxa (e.g., Bifidobacterium/Lactobacillus) and increase Proteobacteria/gram-negative organisms, promoting inflammation and barrier dysfunction; standard antidiarrheals address motility rather than these upstream drivers. (jiang2025importantroleof pages 1-2)

---

## 3. Phenotypes
### Core phenotypes and clinical characteristics
- **Diarrhea** (severity graded by CTCAE; can be acute or delayed; can persist for years in some survivors). (jiang2025importantroleof pages 1-2, chen2025restoreintestinalsteadystate pages 1-3)
- **Acute cholinergic irinotecan syndrome:** acute diarrhea with cramps and autonomic symptoms (rhinitis, lacrimation, salivation) lasting ~30 minutes and responsive to atropine. (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4)
- **Delayed-onset irinotecan diarrhea:** onset >24 hours after irinotecan. (deng2024efficacyandsafety pages 1-2)

### Complications (downstream phenotypes)
Complications emphasized include dehydration, electrolyte disorders, malnutrition, and acute kidney injury/renal dysfunction (not all with quantified rates in retrieved excerpts). (chen2025restoreintestinalsteadystate pages 1-3, aleem2024theimpactof pages 1-3)

### Frequency / burden (selected)
- For irinotecan: 50–80% all-grade diarrhea; 11–32% grade ≥3. (deng2024efficacyandsafety pages 1-2)
- Docetaxel: 20–40% diarrhea; severe ~5–6%. (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4)

### Suggested HPO terms (for knowledge base annotation; ontology suggestions)
- Diarrhea: **HP:0002014**
- Abdominal pain: **HP:0002027**
- Dehydration: **HP:0001944**
- Hypokalemia/electrolyte imbalance (as applicable): **HP:0002900**
- Weight loss/malnutrition: **HP:0001824 / HP:0004395**
- Acute kidney injury (complication): **HP:0001919**

(These are standard HPO suggestions; not directly asserted in the retrieved texts beyond phenotype descriptions.)

---

## 4. Genetic / molecular information
### Causal genes
CID is not a Mendelian disease; however, clinically actionable **host PGx genes** influence susceptibility:
- **UGT1A1** (irinotecan SN-38 glucuronidation; reduced function increases risk). (chen2025restoreintestinalsteadystate pages 6-7)
- **DPYD** (fluoropyrimidine catabolism; reduced function increases severe toxicity including diarrhea). (oterotorres2025dpydgenotypingfluoropyrimidine pages 1-2)

### Pathogenic / risk variants (PGx)
**DPYD key variants** summarized as consistently associated with severe fluoropyrimidine toxicity: **DPYD*2A, DPYD*13, c.2846A>T, HapB3**. (oterotorres2025dpydgenotypingfluoropyrimidine pages 1-2)

Variant frequencies (Caucasian populations) summarized in the umbrella review: DPYD*2A ~1%, DPYD*13 0.07–0.1%, c.2846A>T 1.1%, HapB3 2.6–6.3%. (oterotorres2025dpydgenotypingfluoropyrimidine pages 1-2)

### Evidence for genotype-guided dosing
In colorectal cancer, DPYD-guided dosing (vs non-guided) was associated with lower severe FP-related adverse events (12% vs 50%) and lower discontinuation due to severe toxicity (6% vs 50%). (rosasalonso2025dpydguidedfluoropyrimidinedose pages 1-2)

**Expert/regulatory position (implementation):** an ASCO Educational Book article describes regulatory/guideline alignment for pretreatment DPYD genotyping (FDA boxed warnings; NCCN/ASCO alignment) to prevent severe toxicity and mortality. (kratz2026importanceofand pages 1-2)

### Suggested GO / CL terms (mechanism annotation; suggestions)
- GO: epithelial cell apoptotic process; inflammatory response; regulation of intestinal epithelial barrier; response to oxidative stress.
- CL: intestinal epithelial cell; goblet cell; Paneth cell; enteric neuron (myenteric neuron).

---

## 5. Environmental information
CID is strongly influenced by **exposures related to treatment course**, including concurrent antibiotics, diet, and microbiome-altering factors that can shift microbial metabolism and barrier function; recent opinion/review work emphasizes that diet/lifestyle/xenobiotics and antibiotics can influence microbiota composition, which in turn modulates chemotherapy GI toxicity. (fernandes2024istherean pages 7-8)

---

## 6. Mechanism / pathophysiology
### Causal chain (illustrative, irinotecan)
1) Irinotecan administration → 2) hepatic conversion to **SN-38** → 3) glucuronidation to **SN-38G** → 4) biliary/intestinal exposure and microbial deconjugation → 5) renewed SN-38 exposure to mucosa → 6) epithelial apoptosis, barrier disruption, inflammation and altered motility/secretion → 7) delayed diarrhea (>24 h). (deng2024efficacyandsafety pages 1-2, cheatham2025butyratepreventschemotherapyinduced pages 24-28)

### Microbiome and barrier mechanisms
A 2025 review identifies dysbiosis and compromised intestinal barrier integrity as key factors contributing to CID due to mucositis and highlights that microbiota-driven immune activation contributes to mucosal inflammation. (jiang2025importantroleof pages 1-2)

### Enteric nervous system involvement (preclinical)
In a murine irinotecan model, irinotecan increased GI motility and altered enteric neuronal excitability, consistent with a neuro-epithelial contribution to diarrhea. (cheatham2025butyratepreventschemotherapyinduced pages 1-6)

### Molecular profiling / biomarkers (emerging)
- **Fecal β-glucuronidase activity** is repeatedly implicated as a mechanistic driver and candidate predictive biomarker in irinotecan models/reviews. (cheatham2025butyratepreventschemotherapyinduced pages 1-6, fernandes2024istherean pages 7-8)

### Suggested UBERON / GO cellular component terms (suggestions)
- UBERON: small intestine; colon; intestinal mucosa
- GO CC: apical plasma membrane; tight junction; mitochondrion (oxidative stress)

---

## 7. Anatomical structures affected
- **Primary organs:** small intestine and colon (intestinal mucosa/crypt–villus axis; barrier). (chen2025restoreintestinalsteadystate pages 6-7, venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4)
- **Cell/tissue targets:** intestinal epithelial cells/crypt compartment and barrier structures; enteric neurons implicated in motility changes in preclinical models. (cheatham2025butyratepreventschemotherapyinduced pages 1-6)

---

## 8. Temporal development
- **Onset patterns:** CID may occur during or after chemotherapy (acute vs delayed). (jiang2025importantroleof pages 1-2)
- **Irinotecan:** acute cholinergic diarrhea (minutes, responsive to atropine) vs delayed diarrhea (>24 h). (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4, deng2024efficacyandsafety pages 1-2)
- **Long-term:** some patients report CID symptoms persisting up to 10 years post-treatment (survivorship burden). (chen2025restoreintestinalsteadystate pages 1-3)

---

## 9. Inheritance and population
CID itself is not inherited, but susceptibility is influenced by inherited PGx variants.

### Epidemiology / burden (selected data)
CID incidence is regimen-dependent. Reported summary estimates include:
- 50–80% incidence with irinotecan or fluorouracil in reviews; a “significant portion” may be severe (grade 3–4). (jiang2025importantroleof pages 1-2)
- Severe CID leads to treatment dose reductions/delays/cessation in ~60% and contributes to ~1% mortality in one 2025 review summary. (jiang2025importantroleof pages 1-2)
- In one 2025 review, grade 3–4 CID incidence was summarized as ~40%, and ~60% of patients modify therapy (22% dose reduction, 28% delay, 15% discontinuation). (chen2025restoreintestinalsteadystate pages 1-3)

### Real-world implementation impact (claims)
A large matched claims analysis of cancer-related diarrhea found markedly higher treatment discontinuation in those with diarrhea (chemotherapy subgroup: 81.5% vs 62.3%) and higher hazard of discontinuation (HR 1.40). (aleem2024theimpactof pages 1-3)

---

## 10. Diagnostics
### Clinical evaluation and workup (BSG practice guidance, 2025)
The British Society of Gastroenterology (BSG) guidance emphasizes early investigation of troublesome diarrhea during cancer therapy when empirical measures fail, because symptom clusters are poor at distinguishing underlying causes. (andreyev2025britishsocietyof pages 8-8)

Key diagnostic elements and differentials explicitly highlighted include:
- **Stool microbiology testing** in acute diarrhea; it is generally safe to start loperamide while awaiting results, with cautions in neutropenia/C. difficile. (andreyev2025britishsocietyof pages 13-13)
- Blood tests referenced within algorithms include **FBC, LFTs, U&E**, and stool **MC&S**; endoscopy/OGD may be needed. (andreyev2025britishsocietyof pages 15-15)
- Consider non-infectious contributors common in cancer populations: **lactose intolerance, SIBO, bile acid diarrhea (BAD), pancreatic exocrine insufficiency (PEI)**; BAD and PEI are explicitly identified as common causes of GI symptoms in some drug contexts. (andreyev2025britishsocietyof pages 14-15, andreyev2025britishsocietyof pages 15-15)
- **PEI testing and empiric therapy:** fecal elastase-1 is cited, with “faecal elastase level <500 µg/g” suggesting PEI; empiric pancreatic enzyme replacement therapy (PERT) is endorsed in some contexts. (andreyev2025britishsocietyof pages 11-11)
- For severe fluoropyrimidine toxicity, urgent imaging (CT) to exclude enterocolitis is advised. (andreyev2025britishsocietyof pages 13-13)
- The guidance highlights **DPD deficiency** consideration after severe capecitabine/5-FU toxicity. (andreyev2025britishsocietyof pages 14-15)

**Visual clinical algorithms from the BSG guidance** (cropped figures/tables retrieved): Table/pathway and acute-severe diarrhea algorithm (andreyev2025britishsocietyof media 677c2d7d, andreyev2025britishsocietyof media 763cd06e, andreyev2025britishsocietyof media adbbc39b, andreyev2025britishsocietyof media f43c1d78).

### Suggested lab concepts (LOINC-like; suggestions)
- CBC (FBC), CMP (electrolytes/U&E, LFTs), CRP, stool culture/ova/parasite as indicated.
- Fecal elastase-1 (PEI evaluation).

---

## 11. Outcome / prognosis
CID can cause direct morbidity (dehydration, electrolyte disturbances, malnutrition, AKI) and indirect oncologic harm via dose reduction/delay/discontinuation and reduced adherence/persistence. (chen2025restoreintestinalsteadystate pages 1-3, aleem2024theimpactof pages 1-3)

Mortality attributable to severe CID is summarized around ~1% in a 2025 review. (jiang2025importantroleof pages 1-2)

---

## 12. Treatment
### Guideline-based acute management (severity-based)
BSG practice guidance (Gut, 2025) indicates that mild diarrhea may be managed initially without tests, whereas severe diarrhea (e.g., >6 stools/day over baseline or severe abdominal pain) typically requires **hospital admission**, **IV corticosteroids**, and urgent investigation (with escalation to biologics for immune-related enterocolitis when applicable). (andreyev2025britishsocietyof pages 14-15)

### Antidiarrheal pharmacotherapy (stepwise)
- **Loperamide:** commonly used; BSG notes it can be started while awaiting stool microbiology results, with caution for toxic dilatation risk in neutropenic patients and in C. difficile. (andreyev2025britishsocietyof pages 13-13)
- **Octreotide (second-line for refractory CID):** dosing summarized in a 2024 review: start 100–150 µg SC/IV three times daily; can escalate to 500 µg three times daily or continuous infusion (25–50 µg/h). (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 6-9)
- **Atropine** for acute cholinergic irinotecan diarrhea (IV/SC dosing range summarized in 2024 review). (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 6-9)

### Supportive care
For grade 3–4 irinotecan diarrhea, consensus guidance summarized in a 2024 RCT report indicates escalation to **octreotide, antibiotics, and fluid/electrolyte replenishment** (often inpatient). (deng2024efficacyandsafety pages 1-2)

### Antibiotics (when infectious diarrhea suspected)
A 2024 review summarizes guideline-consistent use of **fluoroquinolones** when infection is suspected, and standard agents for **C. difficile** (metronidazole or vancomycin). (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 6-9)

### Mechanism-targeted and emerging interventions
- **Microbiome/SCFA (butyrate):** preclinical evidence supports butyrate as a protective adjunct that suppresses β-glucuronidase activity and preserves barrier and stem-cell compartments in irinotecan models. (cheatham2025butyratepreventschemotherapyinduced pages 24-28)
- **β-glucuronidase inhibition / microbiome targeting:** mechanistic studies support inhibition of microbial β-glucuronidase and suppression of E. coli as strategies to reduce irinotecan diarrhea; one 2024 mechanistic paper describes dual targeting of E. coli and bacterial β-glucuronidase by HQD components (baicalein/baicalin/paeoniflorin). (teng2024threebioactivecompounds pages 1-2)

### Real-world implementation: DPYD testing
BSG guidance highlights DPD deficiency (~3–5% population) and suggests dose reduction for heterozygous DPYD variants (50% starting dose for first cycle with escalation if tolerated); homozygous variants prompt reconsideration of using capecitabine/5-FU. (andreyev2025britishsocietyof pages 14-15)

An observational colorectal cancer study reported DPYD-guided dosing associated with fewer severe adverse events (12% vs 50%) and fewer discontinuations (6% vs 50%). (rosasalonso2025dpydguidedfluoropyrimidinedose pages 1-2)

### Suggested MAXO terms (treatment action ontology; suggestions)
- Antidiarrheal therapy; fluid resuscitation; electrolyte replacement; antimicrobial therapy; dose reduction; hospitalization; diagnostic imaging; stool testing; corticosteroid therapy.

---

## 13. Prevention
### Primary/secondary/tertiary prevention strategies
- **PGx-guided prevention (fluoropyrimidines):** DPYD genotyping before therapy and genotype-guided starting dose reduction is recommended in multiple sources (BSG guidance; umbrella review framework). (andreyev2025britishsocietyof pages 14-15, oterotorres2025dpydgenotypingfluoropyrimidine pages 1-2)
- **PGx-guided prevention (irinotecan):** a review describes genotype-guided irinotecan dosing (e.g., ~30% dose reduction in UGT1A1 poor metabolizers) as reducing febrile neutropenia and helping alleviate CID. (chen2025restoreintestinalsteadystate pages 6-7)
- **Microbiome-targeted prevention (experimental):** butyrate supplementation and β-glucuronidase inhibition are supported in animal models; these are not yet established standard-of-care preventatives for CID. (cheatham2025butyratepreventschemotherapyinduced pages 1-6, cheatham2025butyratepreventschemotherapyinduced pages 24-28)

**Direct trial prevention example (irinotecan, 2024):** A multicenter RCT of Shengjiang Xiexin decoction prophylaxis reported lower diarrhea incidence vs placebo (26.42% vs 52.08%), with pronounced benefit in UGT1A1 high-risk patients (9.09% vs 66.67%). Abstract quote: “The incidence of diarrhea in SXD group and placebo group were 26.42% (14/53) and 52.08% (25/48), respectively (P < 0.05)… In UGT1A1 high-risk population, the incidence of diarrhea in two groups were 9.09% and 66.67% (P < 0.05)”. (deng2024efficacyandsafety pages 1-2)

---

## 14. Other species / natural disease
Not applicable as a naturally occurring disease entity; however, CID is modeled extensively in animals (see next section).

---

## 15. Model organisms
### Common models and what they recapitulate
- **Mouse irinotecan-induced GI toxicity models**: reproduce diarrhea phenotype (increased fecal water content, altered motility), mucosal injury, dysbiosis, and mechanistic links to β-glucuronidase and barrier disruption; used for testing interventions such as butyrate. (cheatham2025butyratepreventschemotherapyinduced pages 1-6, cheatham2025butyratepreventschemotherapyinduced pages 24-28)
- **Germ-free / gnotobiotic systems**: used to causally implicate microbiota composition and β-glucuronidase-producing organisms in mucositis/diarrhea severity. (fernandes2024istherean pages 7-8)
- **In vitro intestinal epithelial cell systems** for fluoropyrimidine injury and ROS/cytokine pathways. (chen2025restoreintestinalsteadystate pages 6-7)

---

## Recent developments (2023–2025 emphasis) and expert analysis
1) **Shift toward mechanism-informed supportive care**: Recent reviews emphasize that symptom-only control (loperamide, atropine, octreotide) does not address dysbiosis/barrier injury, motivating microbiome-directed adjuncts (e.g., SCFA/butyrate; β-glucuronidase targeting). (jiang2025importantroleof pages 1-2, cheatham2025butyratepreventschemotherapyinduced pages 24-28)

2) **Operationalization of PGx safety programs**: The 2025 umbrella review consolidates evidence that DPYD variants are reproducibly associated with severe fluoropyrimidine toxicity and outlines activity-score guided dosing (e.g., intermediate metabolizers start ~50–75% dose; poor metabolizers typically avoid fluoropyrimidines). (oterotorres2025dpydgenotypingfluoropyrimidine pages 1-2)

3) **Real-world evidence of therapy disruption**: Claims analyses quantify the downstream effect of diarrhea on cancer therapy discontinuation and adherence, underscoring that CID management has survival/cost implications beyond symptom relief. (aleem2024theimpactof pages 1-3)

---

## Key statistics summary table
| Setting / agent | All-grade incidence | Grade ≥3 incidence | Key quantitative risk factors / notes |
|---|---:|---:|---|
| Irinotecan | 50–80% (deng2024efficacyandsafety pages 1-2) | 11–32% (deng2024efficacyandsafety pages 1-2) | Acute cholinergic diarrhea may occur early and respond to atropine; delayed diarrhea occurs >24 h and is linked to SN-38 reactivation by gut bacterial β-glucuronidase (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4, cheatham2025butyratepreventschemotherapyinduced pages 24-28). Risk factors include weekly dosing schedule, poor performance status, elevated creatinine, prior abdominal/pelvic irradiation, leukopenia, age >70 years, Gilbert syndrome/Crigler–Najjar type 1, and high-risk UGT1A1 genotype; UGT1A1*28/reduced UGT1A1 activity increases SN-38 exposure and toxicity risk (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4, chen2025restoreintestinalsteadystate pages 6-7). |
| Fluoropyrimidines (5-FU/capecitabine) | Up to ~80% reported for 5-FU in some regimens; reviews also cite 50–80% for fluorouracil-associated CID (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 1-3, jiang2025importantroleof pages 1-2) | Not well quantified in the provided excerpts for all regimens; overall CID grade 3–4 burden contributes substantially, and fluoropyrimidines are among the main high-risk agents (jiang2025importantroleof pages 1-2, chen2025restoreintestinalsteadystate pages 1-3) | Major pharmacogenomic risk is reduced DPD activity due to DPYD variants. Key variants: DPYD*2A, DPYD*13, c.2846A>T, HapB3; heterozygous frequencies in Caucasians are ~1%, 0.07–0.1%, 1.1%, and 2.6–6.3%, respectively (oterotorres2025dpydgenotypingfluoropyrimidine pages 1-2). Diarrhea-specific associations include DPYD*2A carrier diarrhea 12.0–100% vs 1.4–27.5% in wild type; DPYD*13 50–100% vs 5.8–22%; c.2846A>T pooled OR 6.0; HapB3 carrier diarrhea 14.3–50% vs 12.5–23.1% (oterotorres2025dpydgenotypingfluoropyrimidine pages 9-10, oterotorres2025dpydgenotypingfluoropyrimidine pages 7-9). Genotype-guided dosing reduced overall severe toxicity and reduced diarrhea RR 0.4 (95% CI 0.2–0.6) in one review synthesis (oterotorres2025dpydgenotypingfluoropyrimidine pages 10-12). |
| Docetaxel | 20–40% (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4) | ~5–6% severe diarrhea (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4) | Recognized cytotoxic cause of CID; burden is lower than irinotecan in the provided evidence but still clinically meaningful, especially in combination regimens and vulnerable patients (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4, venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 1-3). |
| Overall CID burden | Common across regimens; 50–80% reported for irinotecan/fluorouracil in reviews, and grade 3–4 CID is reported at about 40% in one review summary (jiang2025importantroleof pages 1-2, chen2025restoreintestinalsteadystate pages 1-3) | About 40% grade 3–4 in one aggregate review; regimen-specific severe-event rates vary widely (chen2025restoreintestinalsteadystate pages 1-3) | Severe CID leads to dose reduction, delay, or discontinuation in ~60% of affected patients and is associated with ~1% mortality (jiang2025importantroleof pages 1-2). In a large claims study of cancer-related diarrhea, treatment discontinuation was higher with diarrhea: overall 82.4% vs 64.6%, chemotherapy subgroup 81.5% vs 62.3%, HR for discontinuation 1.40 (aleem2024theimpactof pages 1-3). Clinical complications include dehydration, electrolyte imbalance, malnutrition, and acute kidney injury (aleem2024theimpactof pages 1-3, chen2025restoreintestinalsteadystate pages 1-3). |


*Table: This table summarizes the best available quantitative data from the provided evidence for chemotherapy-induced diarrhea across major implicated agents. It highlights incidence, severe-event burden, and key clinical and pharmacogenomic risk factors relevant for disease characterization and supportive-care decision making.*

---

## Visual evidence (clinical algorithms)
- BSG guidance includes visual algorithms for investigation and management of diarrhea during cancer treatment, including an acute severe diarrhea during chemotherapy algorithm and a table-based pathway for diarrhea workup. (andreyev2025britishsocietyof media 677c2d7d, andreyev2025britishsocietyof media 763cd06e, andreyev2025britishsocietyof media adbbc39b, andreyev2025britishsocietyof media f43c1d78)

---

## Notes on PMID requirement
Many retrieved full texts in this run provided DOIs and journal metadata but not PubMed identifiers in the extracted evidence. Where PMIDs are required for a knowledge base, they should be added during a dedicated PubMed crosswalk step using DOI→PMID mapping.


References

1. (chen2025restoreintestinalsteadystate pages 1-3): Miaoqi Chen, Yamao Li, and Peijun Chen. Restore intestinal steady-state: new advances in the clinical management of chemotherapy-associated diarrhea and constipation. Journal of Molecular Histology, Mar 2025. URL: https://doi.org/10.1007/s10735-025-10367-w, doi:10.1007/s10735-025-10367-w. This article has 5 citations and is from a peer-reviewed journal.

2. (jiang2025importantroleof pages 1-2): Wanrou Jiang, Yongjun Wu, Xiuyun He, Ling Jiang, Wanyi Zhang, Wenjuan Zheng, Min Hu, and Chaofu Zhu. Important role of intestinal microbiota in chemotherapy-induced diarrhea and therapeutics. Journal of Cancer, 16:648-659, Jan 2025. URL: https://doi.org/10.7150/jca.99421, doi:10.7150/jca.99421. This article has 9 citations and is from a peer-reviewed journal.

3. (chen2025restoreintestinalsteadystate pages 6-7): Miaoqi Chen, Yamao Li, and Peijun Chen. Restore intestinal steady-state: new advances in the clinical management of chemotherapy-associated diarrhea and constipation. Journal of Molecular Histology, Mar 2025. URL: https://doi.org/10.1007/s10735-025-10367-w, doi:10.1007/s10735-025-10367-w. This article has 5 citations and is from a peer-reviewed journal.

4. (aleem2024theimpactof pages 1-3): Abdullah Aleem, Maya Charuni Sarihan, Pablo C. Okhuysen, Eric J. Roeland, Lee Schwartzberg, Yinghong Wang, and Pravin Chaturvedi. The impact of cancer-related diarrhea on changes in cancer therapy. Supportive care in cancer : official journal of the Multinational Association of Supportive Care in Cancer, 32 10:668, Sep 2024. URL: https://doi.org/10.1007/s00520-024-08871-y, doi:10.1007/s00520-024-08871-y. This article has 2 citations.

5. (cheatham2025butyratepreventschemotherapyinduced pages 24-28): Stanley M. Cheatham, Zayd Rehman, Mahshid Arastonejad, Ryan Kane, Naeem Ahmad, Natalie Luffman, Hisashi Harada, Yuesheng Zhang, Katarzyna M. Tyc, David A. Gewirtz, and Hamid I. Akbarali. Butyrate prevents chemotherapy-induced gastrointestinal toxicity and microbial dysbiosis. Scientific Reports, Dec 2025. URL: https://doi.org/10.1038/s41598-025-30385-8, doi:10.1038/s41598-025-30385-8. This article has 1 citations and is from a peer-reviewed journal.

6. (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 3-4): N. Venkateswaramurthy, Aravindhan S, and Elavarasan P R. Managing chemotherapy-induced diarrhea: efficacy of interventions for cancer patients. Biosciences Biotechnology Research Asia, 21:391-404, Jul 2024. URL: https://doi.org/10.13005/bbra/3233, doi:10.13005/bbra/3233. This article has 9 citations.

7. (andreyev2025britishsocietyof pages 15-15): Jervoise Andreyev, Richard Adams, Jan Bornschein, Mark Chapman, Dave Chuter, Sally Darnborough, Andrew Davies, Fiona Dignan, Clare Donnellan, Darren Fernandes, Robert Flavel, Georgina Giebner, Alexandra Gilbert, Fiona Huddy, Mohid Shakil S Khan, Pauline Leonard, Shameer Mehta, Ollie Minton, Christine Norton, Louise Payton, Gill McGuire, D Mark Pritchard, Claire Taylor, Susan Vyoral, Ana Wilson, and Linda Wedlake. British society of gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. Gut, 74:1040-1067, Mar 2025. URL: https://doi.org/10.1136/gutjnl-2024-333812, doi:10.1136/gutjnl-2024-333812. This article has 22 citations and is from a highest quality peer-reviewed journal.

8. (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 1-3): N. Venkateswaramurthy, Aravindhan S, and Elavarasan P R. Managing chemotherapy-induced diarrhea: efficacy of interventions for cancer patients. Biosciences Biotechnology Research Asia, 21:391-404, Jul 2024. URL: https://doi.org/10.13005/bbra/3233, doi:10.13005/bbra/3233. This article has 9 citations.

9. (deng2024efficacyandsafety pages 1-2): Chao Deng, Qing Liu, Meng Yang, Hui-juan Cui, Yang Ge, Qin Li, Shi-jie Zhu, Guo-wang Yang, Zhi-guo Zhang, Yu Gao, Yan-ni Lou, and Li-qun Jia. Efficacy and safety of shengjiang xiexin decoction on irinotecan-induced diarrhea in small cell lung cancer patients: a multicenter, randomized, double-blind, placebo-controlled trial. Chinese Medicine, Nov 2024. URL: https://doi.org/10.1186/s13020-024-01025-6, doi:10.1186/s13020-024-01025-6. This article has 4 citations.

10. (oterotorres2025dpydgenotypingfluoropyrimidine pages 1-2): Sara Otero-Torres, Rosa Rodríguez-Mauriz, Eduard Fort-Casamartina, Ana Clopés-Estela, Francesc Soler-Rotllant, Sandra Fontanals-Martínez, and Olalla Montero-Pérez. Dpyd genotyping, fluoropyrimidine dosage and toxicity: an umbrella review of systematic reviews. Pharmaceuticals, 18:727, May 2025. URL: https://doi.org/10.3390/ph18050727, doi:10.3390/ph18050727. This article has 4 citations.

11. (oterotorres2025dpydgenotypingfluoropyrimidine pages 9-10): Sara Otero-Torres, Rosa Rodríguez-Mauriz, Eduard Fort-Casamartina, Ana Clopés-Estela, Francesc Soler-Rotllant, Sandra Fontanals-Martínez, and Olalla Montero-Pérez. Dpyd genotyping, fluoropyrimidine dosage and toxicity: an umbrella review of systematic reviews. Pharmaceuticals, 18:727, May 2025. URL: https://doi.org/10.3390/ph18050727, doi:10.3390/ph18050727. This article has 4 citations.

12. (cheatham2025butyratepreventschemotherapyinduced pages 1-6): Stanley M. Cheatham, Zayd Rehman, Mahshid Arastonejad, Ryan Kane, Naeem Ahmad, Natalie Luffman, Hisashi Harada, Yuesheng Zhang, Katarzyna M. Tyc, David A. Gewirtz, and Hamid I. Akbarali. Butyrate prevents chemotherapy-induced gastrointestinal toxicity and microbial dysbiosis. Scientific Reports, Dec 2025. URL: https://doi.org/10.1038/s41598-025-30385-8, doi:10.1038/s41598-025-30385-8. This article has 1 citations and is from a peer-reviewed journal.

13. (oterotorres2025dpydgenotypingfluoropyrimidine pages 10-12): Sara Otero-Torres, Rosa Rodríguez-Mauriz, Eduard Fort-Casamartina, Ana Clopés-Estela, Francesc Soler-Rotllant, Sandra Fontanals-Martínez, and Olalla Montero-Pérez. Dpyd genotyping, fluoropyrimidine dosage and toxicity: an umbrella review of systematic reviews. Pharmaceuticals, 18:727, May 2025. URL: https://doi.org/10.3390/ph18050727, doi:10.3390/ph18050727. This article has 4 citations.

14. (rosasalonso2025dpydguidedfluoropyrimidinedose pages 1-2): Rocío Rosas-Alonso, Nuria Rodríguez Salas, Pablo Perez Wert, Angela Hoyo, Susana Martin-López, Daniel Martínez-Pérez, Iciar Ruiz-Gutiérrez, Diego Jiménez-Bou, Jesús Peña, Pedro Arias, Ana Custodio, Itsaso Losantos-García, Alberto M. Borobia, Jaime Feliu, and Ismael Ghanem. Dpyd-guided fluoropyrimidine dose adjustment in colorectal cancer dpyd carriers: start slower to finish stronger. Frontiers in Pharmacology, Sep 2025. URL: https://doi.org/10.3389/fphar.2025.1645188, doi:10.3389/fphar.2025.1645188. This article has 1 citations.

15. (kratz2026importanceofand pages 1-2): Jeremy Kratz, Karen Merritt, Jessica Jorgensen, Comfort Kanji, Luis Abel Quiñones, and Daniel L. Hertz. Importance of and strategies for implementing <i>dpyd</i> testing to prevent severe fluoropyrimidine chemotherapy toxicity in health care systems. American Society of Clinical Oncology Educational Book, Jun 2026. URL: https://doi.org/10.1200/edbk-26-521184, doi:10.1200/edbk-26-521184. This article has 0 citations.

16. (fernandes2024istherean pages 7-8): Camila Fernandes, Mahara Coelho Crisostomo Miranda, Cássia Rodrigues Roque, Ana Lizeth Padilla Paguada, Carlos Adrian Rodrigues Mota, Katharine Gurgel Dias Florêncio, Anamaria Falcão Pereira, Deysi Viviana Tenazoa Wong, Reinaldo Barreto Oriá, and Roberto César Pereira Lima-Júnior. Is there an interplay between environmental factors, microbiota imbalance, and cancer chemotherapy-associated intestinal mucositis? Pharmaceuticals, 17:1020, Aug 2024. URL: https://doi.org/10.3390/ph17081020, doi:10.3390/ph17081020. This article has 14 citations.

17. (andreyev2025britishsocietyof pages 8-8): Jervoise Andreyev, Richard Adams, Jan Bornschein, Mark Chapman, Dave Chuter, Sally Darnborough, Andrew Davies, Fiona Dignan, Clare Donnellan, Darren Fernandes, Robert Flavel, Georgina Giebner, Alexandra Gilbert, Fiona Huddy, Mohid Shakil S Khan, Pauline Leonard, Shameer Mehta, Ollie Minton, Christine Norton, Louise Payton, Gill McGuire, D Mark Pritchard, Claire Taylor, Susan Vyoral, Ana Wilson, and Linda Wedlake. British society of gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. Gut, 74:1040-1067, Mar 2025. URL: https://doi.org/10.1136/gutjnl-2024-333812, doi:10.1136/gutjnl-2024-333812. This article has 22 citations and is from a highest quality peer-reviewed journal.

18. (andreyev2025britishsocietyof pages 13-13): Jervoise Andreyev, Richard Adams, Jan Bornschein, Mark Chapman, Dave Chuter, Sally Darnborough, Andrew Davies, Fiona Dignan, Clare Donnellan, Darren Fernandes, Robert Flavel, Georgina Giebner, Alexandra Gilbert, Fiona Huddy, Mohid Shakil S Khan, Pauline Leonard, Shameer Mehta, Ollie Minton, Christine Norton, Louise Payton, Gill McGuire, D Mark Pritchard, Claire Taylor, Susan Vyoral, Ana Wilson, and Linda Wedlake. British society of gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. Gut, 74:1040-1067, Mar 2025. URL: https://doi.org/10.1136/gutjnl-2024-333812, doi:10.1136/gutjnl-2024-333812. This article has 22 citations and is from a highest quality peer-reviewed journal.

19. (andreyev2025britishsocietyof pages 14-15): Jervoise Andreyev, Richard Adams, Jan Bornschein, Mark Chapman, Dave Chuter, Sally Darnborough, Andrew Davies, Fiona Dignan, Clare Donnellan, Darren Fernandes, Robert Flavel, Georgina Giebner, Alexandra Gilbert, Fiona Huddy, Mohid Shakil S Khan, Pauline Leonard, Shameer Mehta, Ollie Minton, Christine Norton, Louise Payton, Gill McGuire, D Mark Pritchard, Claire Taylor, Susan Vyoral, Ana Wilson, and Linda Wedlake. British society of gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. Gut, 74:1040-1067, Mar 2025. URL: https://doi.org/10.1136/gutjnl-2024-333812, doi:10.1136/gutjnl-2024-333812. This article has 22 citations and is from a highest quality peer-reviewed journal.

20. (andreyev2025britishsocietyof pages 11-11): Jervoise Andreyev, Richard Adams, Jan Bornschein, Mark Chapman, Dave Chuter, Sally Darnborough, Andrew Davies, Fiona Dignan, Clare Donnellan, Darren Fernandes, Robert Flavel, Georgina Giebner, Alexandra Gilbert, Fiona Huddy, Mohid Shakil S Khan, Pauline Leonard, Shameer Mehta, Ollie Minton, Christine Norton, Louise Payton, Gill McGuire, D Mark Pritchard, Claire Taylor, Susan Vyoral, Ana Wilson, and Linda Wedlake. British society of gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. Gut, 74:1040-1067, Mar 2025. URL: https://doi.org/10.1136/gutjnl-2024-333812, doi:10.1136/gutjnl-2024-333812. This article has 22 citations and is from a highest quality peer-reviewed journal.

21. (andreyev2025britishsocietyof media 677c2d7d): Jervoise Andreyev, Richard Adams, Jan Bornschein, Mark Chapman, Dave Chuter, Sally Darnborough, Andrew Davies, Fiona Dignan, Clare Donnellan, Darren Fernandes, Robert Flavel, Georgina Giebner, Alexandra Gilbert, Fiona Huddy, Mohid Shakil S Khan, Pauline Leonard, Shameer Mehta, Ollie Minton, Christine Norton, Louise Payton, Gill McGuire, D Mark Pritchard, Claire Taylor, Susan Vyoral, Ana Wilson, and Linda Wedlake. British society of gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. Gut, 74:1040-1067, Mar 2025. URL: https://doi.org/10.1136/gutjnl-2024-333812, doi:10.1136/gutjnl-2024-333812. This article has 22 citations and is from a highest quality peer-reviewed journal.

22. (andreyev2025britishsocietyof media 763cd06e): Jervoise Andreyev, Richard Adams, Jan Bornschein, Mark Chapman, Dave Chuter, Sally Darnborough, Andrew Davies, Fiona Dignan, Clare Donnellan, Darren Fernandes, Robert Flavel, Georgina Giebner, Alexandra Gilbert, Fiona Huddy, Mohid Shakil S Khan, Pauline Leonard, Shameer Mehta, Ollie Minton, Christine Norton, Louise Payton, Gill McGuire, D Mark Pritchard, Claire Taylor, Susan Vyoral, Ana Wilson, and Linda Wedlake. British society of gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. Gut, 74:1040-1067, Mar 2025. URL: https://doi.org/10.1136/gutjnl-2024-333812, doi:10.1136/gutjnl-2024-333812. This article has 22 citations and is from a highest quality peer-reviewed journal.

23. (andreyev2025britishsocietyof media adbbc39b): Jervoise Andreyev, Richard Adams, Jan Bornschein, Mark Chapman, Dave Chuter, Sally Darnborough, Andrew Davies, Fiona Dignan, Clare Donnellan, Darren Fernandes, Robert Flavel, Georgina Giebner, Alexandra Gilbert, Fiona Huddy, Mohid Shakil S Khan, Pauline Leonard, Shameer Mehta, Ollie Minton, Christine Norton, Louise Payton, Gill McGuire, D Mark Pritchard, Claire Taylor, Susan Vyoral, Ana Wilson, and Linda Wedlake. British society of gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. Gut, 74:1040-1067, Mar 2025. URL: https://doi.org/10.1136/gutjnl-2024-333812, doi:10.1136/gutjnl-2024-333812. This article has 22 citations and is from a highest quality peer-reviewed journal.

24. (andreyev2025britishsocietyof media f43c1d78): Jervoise Andreyev, Richard Adams, Jan Bornschein, Mark Chapman, Dave Chuter, Sally Darnborough, Andrew Davies, Fiona Dignan, Clare Donnellan, Darren Fernandes, Robert Flavel, Georgina Giebner, Alexandra Gilbert, Fiona Huddy, Mohid Shakil S Khan, Pauline Leonard, Shameer Mehta, Ollie Minton, Christine Norton, Louise Payton, Gill McGuire, D Mark Pritchard, Claire Taylor, Susan Vyoral, Ana Wilson, and Linda Wedlake. British society of gastroenterology practice guidance on the management of acute and chronic gastrointestinal symptoms and complications as a result of treatment for cancer. Gut, 74:1040-1067, Mar 2025. URL: https://doi.org/10.1136/gutjnl-2024-333812, doi:10.1136/gutjnl-2024-333812. This article has 22 citations and is from a highest quality peer-reviewed journal.

25. (venkateswaramurthy2024managingchemotherapyinduceddiarrhea pages 6-9): N. Venkateswaramurthy, Aravindhan S, and Elavarasan P R. Managing chemotherapy-induced diarrhea: efficacy of interventions for cancer patients. Biosciences Biotechnology Research Asia, 21:391-404, Jul 2024. URL: https://doi.org/10.13005/bbra/3233, doi:10.13005/bbra/3233. This article has 9 citations.

26. (teng2024threebioactivecompounds pages 1-2): Xiaojun Teng, Bingxin Wu, Zuhui Liang, Lisheng Zhang, Maolin Yang, Zhongqiu Liu, Qi Liang, and Caiyan Wang. Three bioactive compounds from huangqin decoction ameliorate irinotecan-induced diarrhea via dual-targeting of escherichia coli and bacterial β-glucuronidase. Cell Biology and Toxicology, Oct 2024. URL: https://doi.org/10.1007/s10565-024-09922-0, doi:10.1007/s10565-024-09922-0. This article has 12 citations and is from a peer-reviewed journal.

27. (oterotorres2025dpydgenotypingfluoropyrimidine pages 7-9): Sara Otero-Torres, Rosa Rodríguez-Mauriz, Eduard Fort-Casamartina, Ana Clopés-Estela, Francesc Soler-Rotllant, Sandra Fontanals-Martínez, and Olalla Montero-Pérez. Dpyd genotyping, fluoropyrimidine dosage and toxicity: an umbrella review of systematic reviews. Pharmaceuticals, 18:727, May 2025. URL: https://doi.org/10.3390/ph18050727, doi:10.3390/ph18050727. This article has 4 citations.

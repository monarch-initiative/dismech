---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-06T18:22:51.305386'
end_time: '2026-05-06T18:34:55.281502'
duration_seconds: 723.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pontiac Fever
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pontiac Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Pontiac Fever** covering all of the
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
- **Disease Name:** Pontiac Fever
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Pontiac Fever** covering all of the
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


## Comprehensive Disease Characteristics Research Report: Pontiac Fever (Infectious)

### Target disease
- **Disease name:** Pontiac fever  
- **Category:** Infectious (environmentally acquired legionellosis)  
- **MONDO ID:** Not identified in the retrieved evidence (additional ontology lookup would be needed). (graham2024astudyofa pages 134-137)

---

## 1. Disease Information

### 1.1 Overview (what is Pontiac fever?)
Pontiac fever is the **non-pneumonic** (no pneumonia) and typically **self-limited, influenza-like** clinical form of **legionellosis** caused by *Legionella* spp. (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6, piedade2020analysisoflegionellas pages 30-33). In practical surveillance and outbreak settings, Pontiac fever is frequently recognized as **clusters of acute febrile illness** after a shared environmental exposure rather than as sporadic, individually diagnosed illness, because mild cases may not seek care and diagnostic approaches are often geared toward pneumonia. (currie2023theecologyof pages 20-23, hamilton2018outbreaksoflegionnaires’ pages 2-4)

**Abstract-supported definition (direct quote):** A hospital-based epidemiology paper explicitly frames the two forms of disease as: “pneumonic legionnaires’ disease and non-pneumonic legionnaires’ disease (Pontiac fever)” (kosinska2018useofhospital pages 1-2).

### 1.2 Key identifiers
- **ICD-10:** 
  - **A48.2** = non-pneumonic legionellosis / **Pontiac fever** (graham2024astudyofa pages 134-137, wade2024weatherconditionsand pages 2-3, kosinska2018useofhospital pages 1-2)  
  - **A48.1** = Legionnaires’ disease (pneumonic legionellosis) (graham2024astudyofa pages 134-137, kosinska2018useofhospital pages 1-2)
- **ICD-11:** not identified in retrieved evidence. (graham2024astudyofa pages 134-137)
- **MeSH:** not identified in retrieved evidence. (graham2024astudyofa pages 134-137)
- **Orphanet/OMIM/MONDO:** not identified in retrieved evidence. (graham2024astudyofa pages 134-137)

### 1.3 Synonyms / alternative names
- **Non-pneumonic legionellosis** (explicitly used in ICD-10-context literature) (kosinska2018useofhospital pages 1-2)
- Sometimes referred to as the **mild, flu-like illness** form of legionellosis in reviews and guidance documents. (sylvestre2023module16legionella pages 10-14, piedade2020analysisoflegionellas pages 30-33)

### 1.4 Evidence type note (individual vs aggregated)
Evidence available in this retrieval set is primarily **aggregated** (outbreak reviews; administrative hospital datasets; surveillance methodology and environmental control guidance), rather than prospective, patient-level clinical cohorts. (hamilton2018outbreaksoflegionnaires’ pages 2-4, wade2024weatherconditionsand pages 2-3, kosinska2018useofhospital pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
Pontiac fever is caused by **exposure to pathogenic *Legionella* bacteria**, typically via **inhalation of contaminated aerosols** generated from built-environment water systems (e.g., cooling towers, spas, fountains, building water distribution systems). (sylvestre2023module16legionella pages 10-14, hamilton2018outbreaksoflegionnaires’ pages 2-4)

### 2.2 Infectious agents implicated
While *Legionella pneumophila* is often the dominant species in reported legionellosis, Pontiac-fever outbreaks can involve multiple species, including non-*pneumophila* species.
- Reported Pontiac-fever–associated species in the retrieved evidence include: **L. pneumophila, L. anisa, L. micdadei, L. feeleii, L. longbeachae**. (currie2023theecologyof pages 17-20, piedade2020analysisoflegionellas pages 30-33)
- A Legionella ecology review notes the genus includes “>72 species” and that “at least 30 species are known to cause human infections,” with most reported cases attributed to *L. pneumophila*. (sylvestre2023module16legionella pages 10-14)

### 2.3 Risk factors
Pontiac fever risk is dominated by **environmental exposure intensity** and conditions favoring *Legionella* growth and aerosolization.

**Environmental/built environment risk factors:**
- Colonization of man-made water systems, where growth is favored by **warm temperatures, stagnation, biofilms, nutrients, and low disinfectant levels**. (sylvestre2023module16legionella pages 10-14)
- Temperature dependence: growth favored around **25–43°C**, with an “optimal 30–40°C,” and die-off above **~60°C**. (sylvestre2023module16legionella pages 10-14)

**Exposure setting risk factors (outbreak-relevant):**
A large outbreak review (2006–2017) showed most reported Pontiac-fever outbreak cases were associated with engineered water/aerosol sources (Table 1 image). (hamilton2018outbreaksoflegionnaires’ media e7cee3af)

**Host factors:**
In the retrieved evidence, Pontiac fever is described as not strongly discriminating by age or immune status compared with Legionnaires’ disease (suggesting broader susceptibility once exposed), although rigorous comparative risk estimates were not available. (currie2023theecologyof pages 17-20)

### 2.4 Protective factors
Protective factors were not directly quantified for Pontiac fever in the retrieved literature. Preventive measures are largely environmental (see Prevention section). (sylvestre2023module16legionella pages 10-14)

### 2.5 Gene–environment interactions
No host genetic susceptibility loci, causal variants, or modifier genes were identified in the retrieved evidence; Pontiac fever is best supported here as an **environmentally acquired infectious syndrome**. (currie2023theecologyof pages 17-20, graham2024astudyofa pages 134-137)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype (symptoms/signs)
Pontiac fever typically presents as an **influenza-like illness** with:
- **Fever** (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6)
- **Headache** (sylvestre2023module16legionella pages 10-14, currie2023theecologyof pages 17-20, khairullah2025legionnaires’diseasea pages 4-6)
- **Myalgia/muscle aches** (sylvestre2023module16legionella pages 10-14, currie2023theecologyof pages 17-20, khairullah2025legionnaires’diseasea pages 4-6)
- **Malaise/lethargy** (currie2023theecologyof pages 17-20, khairullah2025legionnaires’diseasea pages 4-6)
- **Dry cough** (reported in building-water guidance) (sylvestre2023module16legionella pages 10-14)

### 3.2 Phenotype characteristics
- **Age at onset:** typically adult in outbreak reports, but the syndrome itself is not presented as age-restricted in the retrieved evidence. (currie2023theecologyof pages 17-20)
- **Severity:** usually mild/moderate. (sylvestre2023module16legionella pages 10-14, piedade2020analysisoflegionellas pages 30-33)
- **Progression:** acute, self-limited; not progressive. (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6)
- **Frequency among exposed:** high attack rate is a distinguishing feature in outbreaks (see statistics below). (currie2023theecologyof pages 17-20, piedade2020analysisoflegionellas pages 30-33)

### 3.3 Timing
- **Incubation period:** often **~24–48 hours**, or broadly “hours to several days.” (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6, piedade2020analysisoflegionellas pages 30-33)
- **Duration:** typically **2–5 days**, with most recovering “within a week.” (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6, piedade2020analysisoflegionellas pages 30-33)

### 3.4 Quality of life impact
No validated quality-of-life metrics (e.g., EQ-5D, SF-36) specific to Pontiac fever were identified in the retrieved evidence. (hamilton2018outbreaksoflegionnaires’ pages 2-4)

### 3.5 Suggested HPO terms (phenotype ontology)
Suggested mapping (terms provided as suggestions; IDs not validated within this tool run):
- Fever (HP:0001945)
- Headache (HP:0002315)
- Myalgia (HP:0003326)
- Malaise/Fatigue (HP:0012378 / HP:0012378-like)
- Cough (HP:0012735)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and pathogenic variants
Not applicable based on retrieved evidence. Pontiac fever is not supported here as a Mendelian/genetic disorder, and no host causal gene/variant associations were identified. (currie2023theecologyof pages 17-20, graham2024astudyofa pages 134-137)

### 4.2 Pathogen-side molecular context (relevant to diagnostics and surveillance)
A major molecular diagnostic limitation is that the commonly used **urinary antigen test (UAT)** detects only ***L. pneumophila* serogroup 1**, creating a “blind spot” for other species/serogroups that can cause legionellosis and potentially Pontiac-fever outbreaks. (hamilton2018outbreaksoflegionnaires’ pages 2-4, graham2024astudyofa pages 134-137)

---

## 5. Environmental Information

### 5.1 Environmental factors
Key environmental factors include colonization of **engineered water systems** and conditions enabling aerosol generation.
- Reservoirs and sources include cooling towers, hot tubs/spas, fountains, and building water distribution systems. (sylvestre2023module16legionella pages 10-14, hamilton2018outbreaksoflegionnaires’ pages 2-4)
- *Legionella* ecology includes natural aquatic habitats and association with **biofilms** and likely protozoan hosts (not fully elaborated for PF in this evidence set). (sylvestre2023module16legionella pages 10-14, currie2023theecologyof pages 20-23)

### 5.2 Lifestyle factors
No direct lifestyle risk factors for Pontiac fever were quantified in the retrieved evidence; lifestyle risks are more often discussed for Legionnaires’ disease (e.g., smoking), not specifically for PF. (khairullah2025legionnaires’diseasea pages 2-3)

### 5.3 Infectious agents
- *Legionella* spp., including *L. pneumophila* and non-*pneumophila* species (see Etiology). (currie2023theecologyof pages 17-20, piedade2020analysisoflegionellas pages 30-33)

---

## 6. Mechanism / Pathophysiology

### 6.1 Current mechanistic understanding
A mechanistic hypothesis described in a 2023 ecology-focused review distinguishes Pontiac fever from Legionnaires’ disease: Pontiac fever may represent a **hypersensitivity/inflammatory response** to an “unknown bacterial/amoebal-host component,” rather than an invasive infection with intracellular replication typical of Legionnaires’ disease. (currie2023theecologyof pages 17-20)

### 6.2 Causal chain (trigger → symptoms)
1. **Upstream trigger:** aerosol exposure to *Legionella*-containing droplets from colonized water systems (cooling towers, spas, etc.). (sylvestre2023module16legionella pages 10-14, hamilton2018outbreaksoflegionnaires’ pages 2-4)
2. **Intermediate steps:** short incubation (often 24–48 h) consistent with a brisk inflammatory response. (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6)
3. **Downstream manifestation:** systemic flu-like symptoms (fever, headache, myalgia, malaise), typically without pneumonia and self-resolving. (sylvestre2023module16legionella pages 10-14, piedade2020analysisoflegionellas pages 30-33)

### 6.3 Suggested GO and CL terms (mechanism annotation)
Suggested (not validated in this run):
- GO:0006954 inflammatory response
- GO:0006955 immune response
- GO:0032496 response to lipopolysaccharide (relevant for Gram-negative exposures, hypothesis-level)
- CL:0000540 macrophage (relevant in legionellosis generally; PF-specific cell evidence not identified) (currie2023theecologyof pages 17-20)

---

## 7. Anatomical Structures Affected

Pontiac fever is primarily a **systemic febrile illness** after respiratory exposure; unlike Legionnaires’ disease it is **non-pneumonic**.
- Primary system involved: **respiratory exposure route** (inhalation of aerosols), with systemic symptoms. (sylvestre2023module16legionella pages 10-14, piedade2020analysisoflegionellas pages 30-33)
- Suggested UBERON terms (not validated in this run): lung (UBERON:0002048) as exposure/portal; respiratory tract (UBERON:0000065).

---

## 8. Temporal Development

- **Onset pattern:** acute (sylvestre2023module16legionella pages 10-14)
- **Typical incubation:** ~24–48 h (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6)
- **Course:** self-limited, typically resolves in 2–5 days or within ~1 week (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6, piedade2020analysisoflegionellas pages 30-33)
- **Remission:** spontaneous (sylvestre2023module16legionella pages 10-14, piedade2020analysisoflegionellas pages 30-33)

---

## 9. Inheritance and Population

### 9.1 Epidemiology and outbreak statistics
Pontiac fever is mainly characterized in the literature through outbreaks; surveillance and case definitions are inconsistent.

**No universal case definition:** A major outbreak review states that “there is currently no agreed-upon case definition for Pontiac fever.” (hamilton2018outbreaksoflegionnaires’ pages 2-4)

**Outbreak burden (2006–2017):** A review of outbreaks reported **725 Pontiac fever cases** in the period 2006–2017. (hamilton2018outbreaksoflegionnaires’ pages 2-4)

**Outbreak sources:** The same review provides source-specific totals, showing Pontiac-fever cases were mostly associated with pools/spas and aerosol-generating systems; these data are summarized in Table 1 (image). (hamilton2018outbreaksoflegionnaires’ media e7cee3af)

**Attack rate:** Pontiac fever is described as having a **very high attack rate** in outbreak settings, reported “up to 100% of those exposed,” and another review excerpt cites PF sources where “>90% become ill” contrasted with LD sources “<5%.” (currie2023theecologyof pages 17-20, piedade2020analysisoflegionellas pages 30-33)

### 9.2 Demographics (from administrative datasets)
PF-specific demographic statistics are sparse; however, legionellosis hospitalization datasets provide context:
- **US Medicare hospitalization case-crossover study (1999–2020):** 37,883 legionellosis hospitalizations (after exclusions), 58% male, median age 73 (range 13–106); authors caution that few PF-only cases existed in this dataset, limiting PF-specific inference. (wade2024weatherconditionsand pages 2-3)
- **Poland hospital morbidity analysis (2008–2015):** 84 first-time hospitalizations coded as A48.1/A48.2, more frequent in men and urban residents; mean hospital stay 14.68 days (this largely reflects hospitalized legionellosis, not necessarily typical PF). (kosinska2018useofhospital pages 1-2)

### 9.3 Inheritance
Not applicable (infectious disease; no genetic inheritance pattern identified). (currie2023theecologyof pages 17-20)

---

## 10. Diagnostics

### 10.1 Clinical approach
Pontiac fever is often diagnosed by:
- compatible clinical syndrome (acute flu-like illness, no pneumonia),
- short incubation after a shared exposure,
- and outbreak linkage to *Legionella*-contaminated sources. (hamilton2018outbreaksoflegionnaires’ pages 2-4)

### 10.2 Laboratory testing
Tests used in legionellosis outbreak investigations include:
- **Urinary antigen test (UAT)** (limited to *L. pneumophila* serogroup 1) (hamilton2018outbreaksoflegionnaires’ pages 2-4, graham2024astudyofa pages 134-137)
- **Serology** (e.g., IFA/ELISA) (hamilton2018outbreaksoflegionnaires’ pages 2-4)
- **Culture** (may have poor sensitivity) (graham2024astudyofa pages 134-137)
- **PCR/NAAT** (broader detection; increasing adoption) (currie2023theecologyof pages 20-23, graham2024astudyofa pages 134-137)

Diagnostic blind spot: reliance on UAT biases detection toward *L. pneumophila* serogroup 1 and may under-detect non-*pneumophila* species that can be associated with Pontiac fever. (currie2023theecologyof pages 20-23, graham2024astudyofa pages 134-137)

### 10.3 Environmental testing
Environmental sampling and linkage of clinical and environmental isolates is a common outbreak method; one outbreak review reported matching of clinical and environmental isolates in ~35% of outbreaks. (hamilton2018outbreaksoflegionnaires’ pages 2-4)

---

## 11. Outcome / Prognosis

Pontiac fever is typically **self-resolving** and **not associated with mortality** in the retrieved evidence. (piedade2020analysisoflegionellas pages 30-33)

---

## 12. Treatment

### 12.1 Standard care
Pontiac fever generally requires **supportive/symptomatic care only**, and “most affected people recover within a week and usually do not require medical treatment.” (sylvestre2023module16legionella pages 10-14, piedade2020analysisoflegionellas pages 30-33)

### 12.2 Antibiotics
Antibiotics (e.g., macrolides, fluoroquinolones) are commonly discussed for Legionnaires’ disease and severe legionellosis; their routine use for typical Pontiac fever is not supported in the retrieved evidence, given self-limited course. (hongUnknownyearthebodysystem pages 12-21, piedade2020analysisoflegionellas pages 30-33)

### 12.3 Suggested MAXO terms (treatment/prevention action ontology)
Suggested (not validated in this run):
- Supportive care (MAXO:0000747-like)
- Symptomatic treatment (MAXO:0000746-like)
- Environmental disinfection / water system remediation (MAXO terms likely exist but not retrieved here)

---

## 13. Prevention

Prevention of Pontiac fever aligns with prevention of legionellosis generally and is centered on **water management and aerosol source control**.

### 13.1 Primary prevention (built environment)
A 2023 guide for building managers/operators emphasizes that *Legionella* colonizes engineered water systems and that growth is promoted by warm temperatures, biofilms, stagnation, and low disinfectant levels; controlling these conditions is fundamental to prevention. (sylvestre2023module16legionella pages 10-14)

Practical control levers include:
- **Temperature control** (keeping hot water sufficiently hot; thresholds discussed in environmental contexts) (sylvestre2023module16legionella pages 10-14)
- **Reducing stagnation** and maintaining flow (sylvestre2023module16legionella pages 10-14)
- **Biofilm control** and maintaining disinfectant residuals (sylvestre2023module16legionella pages 10-14)

### 13.2 Secondary/tertiary prevention (outbreak response)
Outbreak investigations commonly use clinical case finding plus environmental investigation and targeted remediation of implicated sources (e.g., cooling towers/spas) as documented in outbreak-review contexts. (hamilton2018outbreaksoflegionnaires’ pages 2-4)

---

## 14. Other Species / Natural Disease

No naturally occurring Pontiac-fever syndrome in non-human species was identified in the retrieved evidence. (currie2023theecologyof pages 17-20)

---

## 15. Model Organisms

Pontiac-fever–specific experimental models were not identified in the retrieved evidence. However, *Legionella* research broadly uses host–pathogen systems (e.g., protozoa and mammalian phagocytes) to study mechanisms of infection and host interaction; PF-specific translation of these models was not established in the retrieved set. (currie2023theecologyof pages 17-20)

---

## Recent developments and latest research (prioritizing 2023–2024)

1. **Surveillance and coding improvements:** A 2024 New Zealand analysis explicitly uses ICD-10 coding (A48.1/A48.2) and discusses diagnostic evolution and limitations of culture and urinary antigen testing, with increasing use of NAAT/PCR; this is directly relevant to recognizing under-detected, non-pneumonic presentations such as Pontiac fever. (graham2024astudyofa pages 134-137, graham2024astudyof pages 134-137)
2. **Weather/climate associations (context for legionellosis trends):** A large 2024 US Medicare analysis (37,883 hospitalizations) links precipitation/humidity to legionellosis hospitalization risk at lags consistent with incubation; while not PF-specific, it supports the broader environmental sensitivity of *Legionella* disease risk. (wade2024weatherconditionsand pages 2-3)
3. **Built-environment implementation guidance (2023):** Practical building water system control guidance provides operationally relevant parameters (growth temperature ranges; system types implicated) and provides accessible definitions of Pontiac fever for non-clinical stakeholders managing risk. (sylvestre2023module16legionella pages 10-14)

---

## Key quantitative data highlights
- **Incubation:** typically **24–48 h** (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6)
- **Duration:** typically **2–5 days**, recovery often within **~1 week** (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6, piedade2020analysisoflegionellas pages 30-33)
- **Attack rate:** reported **>90%** to **up to 100%** among exposed in some outbreak contexts (currie2023theecologyof pages 17-20, piedade2020analysisoflegionellas pages 30-33)
- **Outbreak cases (2006–2017 review):** **725 PF cases**, with many linked to pools/spas and cooling towers (hamilton2018outbreaksoflegionnaires’ pages 2-4, hamilton2018outbreaksoflegionnaires’ media e7cee3af)
- **ICD-10 code:** **A48.2** (Pontiac fever) (graham2024astudyofa pages 134-137, kosinska2018useofhospital pages 1-2)

---

## Evidence summary table
| Domain | Key points | Quantitative/statistical data | Key sources (with citation ids) | URLs/publication dates if in evidence |
|---|---|---|---|---|
| Definition / current understanding | Pontiac fever is the non-pneumonic, acute, self-limited influenza-like form of legionellosis caused by Legionella spp.; unlike Legionnaires’ disease, pneumonia is absent. Recognition is often outbreak-based because mild cases may be missed. | Illness duration usually 2–5 days or recovery within about 1 week; no mortality typically expected in uncomplicated cases. | (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6, currie2023theecologyof pages 20-23, piedade2020analysisoflegionellas pages 30-33) | Sylvestre & Julian, 2023; Khairullah et al., Mar 2025, https://doi.org/10.14202/ijoh.2025.62-77; Piedade, 2020 |
| Identifiers / codes | Standardized coding is available at the disease-group level as non-pneumonic legionellosis. ICD-10 code A48.2 is used for Pontiac fever; ICD-10 A48.1 is Legionnaires’ disease. Earlier ICD-9 datasets often lacked a distinct PF code, complicating surveillance. No explicit ICD-11 or MeSH identifier was found in the retrieved evidence. | ICD-10: A48.2 (Pontiac fever); A48.1 (Legionnaires’ disease). | (graham2024astudyofa pages 134-137, wade2024weatherconditionsand pages 2-3, kosinska2018useofhospital pages 1-2) | Wade & Herbert, Oct 2024, https://doi.org/10.1017/S0950268824000979; Kosińska et al., Dec 2018, https://doi.org/10.26444/monz/101676 |
| Clinical characteristics | Typical symptoms include fever, headache, myalgia, malaise/lethargy, and often dry cough; disease is mild to moderate and self-resolving. | Average incubation 24–48 h; can be described more broadly as hours to several days; symptoms usually last 2–5 days, with most recovering within 1 week. | (sylvestre2023module16legionella pages 10-14, currie2023theecologyof pages 17-20, khairullah2025legionnaires’diseasea pages 4-6, piedade2020analysisoflegionellas pages 30-33) | Sylvestre & Julian, 2023; Khairullah et al., Mar 2025, https://doi.org/10.14202/ijoh.2025.62-77; Piedade, 2020 |
| Attack rate / severity | PF is epidemiologically distinct from Legionnaires’ disease by its very high attack rate and low severity; many exposed persons may become ill, but illness is usually not life-threatening. | Attack rate reported as up to 100% among exposed persons; CDC-sourced comparison cited in one review: PF sources >90% ill vs LD sources <5%. | (currie2023theecologyof pages 17-20, piedade2020analysisoflegionellas pages 30-33) | Currie, 2023; Piedade, 2020 |
| Etiology / infectious agents | Caused by Legionella species; L. pneumophila is the dominant species overall, but PF outbreaks have also involved non-pneumophila species. Reported PF-associated species include L. anisa, L. micdadei, L. feeleii, and L. longbeachae. | Legionella genus noted as >72 species overall; at least 30 species known to cause human infection; most reported human cases attributed to L. pneumophila. | (sylvestre2023module16legionella pages 10-14, currie2023theecologyof pages 17-20, piedade2020analysisoflegionellas pages 30-33, hamilton2018outbreaksoflegionnaires’ pages 2-4) | Sylvestre & Julian, 2023; Hamilton et al., May 2018, https://doi.org/10.1007/s40572-018-0201-4 |
| Exposure sources / real-world settings | Exposure is primarily environmental through inhalation of contaminated aerosols from engineered water systems; non-pneumophila disease can also follow exposure to soil/compost or dust. Common sources include cooling towers, pools/spas/hot tubs, fountains, potable building water systems, wastewater systems, and gardening/potting soils for L. longbeachae. No person-to-person transmission evidence was identified in the retrieved PF-focused evidence. | Outbreak review 2006–2017 recorded PF cases by source: pools/spas 433; cooling towers/AC/evaporative condensers 146; non-potable water systems 139; potable/building water systems 7. | (sylvestre2023module16legionella pages 10-14, khairullah2025legionnaires’diseasea pages 4-6, currie2023theecologyof pages 20-23, hamilton2018outbreaksoflegionnaires’ pages 2-4, hamilton2018outbreaksoflegionnaires’ media e7cee3af) | Hamilton et al., May 2018, https://doi.org/10.1007/s40572-018-0201-4; Sylvestre & Julian, 2023 |
| Environmental growth factors | Legionella is naturally aquatic and colonizes man-made water systems; growth is promoted by warm water, stagnation, biofilms, nutrients, and inadequate disinfectant residuals. | Growth favored at 25–43°C; optimal 30–40°C; die-off above 60°C. Warm-water reservoir often described as 25–40°C. | (sylvestre2023module16legionella pages 10-14, hongUnknownyearthebodysystem pages 12-21) | Sylvestre & Julian, 2023 |
| Pathophysiology / expert analysis | Evidence supports PF as a host inflammatory/hypersensitivity-like response to Legionella or amoebal-host components rather than the invasive intracellular replication pattern typical of Legionnaires’ disease. This explains short incubation, high attack rate, and absence of pneumonia. | Qualitative rather than numeric; proposed mechanism distinguishes PF from LD. | (currie2023theecologyof pages 17-20) | Currie, 2023 |
| Epidemiology / burden | PF is underrecognized because surveillance emphasizes pneumonia and urinary antigen testing; sporadic PF is likely substantially underdetected. Outbreak summaries provide the clearest counts. | International outbreak review (2006–2017): 725 PF cases identified; no universally agreed PF case definition noted in that review. | (hamilton2018outbreaksoflegionnaires’ pages 2-4, hamilton2018outbreaksoflegionnaires’ media e7cee3af) | Hamilton et al., May 2018, https://doi.org/10.1007/s40572-018-0201-4 |
| Demographics / distribution | Legionellosis overall shows male predominance, older age skew for hospitalization datasets, summer seasonality, and urban concentration in some datasets; PF-specific demographic data are much sparser. | Medicare legionellosis hospital dataset: 37,883 cases after exclusions, 58% male, median age 73 years; Poland hospital dataset: 84 first-time hospitalizations with male and urban predominance and summer peak. | (wade2024weatherconditionsand pages 2-3, kosinska2018useofhospital pages 1-2) | Wade & Herbert, Oct 2024, https://doi.org/10.1017/S0950268824000979; Kosińska et al., Dec 2018, https://doi.org/10.26444/monz/101676 |
| Diagnostics | PF diagnosis is mainly clinical plus exposure/outbreak context; tests used across legionellosis investigations include urinary antigen testing, serology, culture, PCR/NAAT, and epidemiologic linkage. UAT is a major surveillance blind spot because it detects only L. pneumophila serogroup 1. PCR/culture improve breadth of detection; PF may be missed if only UAT is used. | UAT used in 88.6% of European legionellosis cases in one cited discussion; PCR implementation associated with a fourfold increase in detection in one review excerpt. Matching clinical/environmental isolates occurred in ~35% of outbreaks. | (currie2023theecologyof pages 17-20, currie2023theecologyof pages 20-23, hamilton2018outbreaksoflegionnaires’ pages 2-4, graham2024astudyofa pages 134-137) | Hamilton et al., May 2018, https://doi.org/10.1007/s40572-018-0201-4; Wade & Herbert, Oct 2024, https://doi.org/10.1017/S0950268824000979 |
| Case definitions | There is no universally agreed PF case definition in the outbreak review literature; surveillance case definitions have evolved over time and differ by jurisdiction. | Review explicitly states no agreed-upon PF case definition; NZ surveillance criteria historically relied on serology, DFA, or isolation. | (hamilton2018outbreaksoflegionnaires’ pages 2-4, graham2024astudyofa pages 81-84) | Hamilton et al., May 2018, https://doi.org/10.1007/s40572-018-0201-4 |
| Treatment / management | Standard management is supportive/symptomatic care; most patients do not require specific antimicrobial therapy. Antibiotics listed in legionellosis guidance (macrolides, fluoroquinolones) are mainly for Legionnaires’ disease or severe invasive infection rather than typical PF. | Recovery without treatment is typical; supportive care only in uncomplicated PF. | (sylvestre2023module16legionella pages 10-14, currie2023theecologyof pages 20-23, piedade2020analysisoflegionellas pages 30-33) | Sylvestre & Julian, 2023; Piedade, 2020 |
| Prevention / public health implementation | Prevention focuses on source control in building and environmental water systems: water management programs, temperature control, minimizing stagnation, biofilm control, maintaining disinfectant residuals, regular monitoring, corrective actions during outbreaks, and special attention to high-risk sources such as pools/spas, cooling towers, hot-water systems, and wastewater processes. For L. longbeachae risk, avoiding inhalation of dust/aerosols from potting soil/compost and use of masks/gloves are advised, though effectiveness evidence is limited. | Facilities without water management programs accounted for 72% of LD cases and 81% of fatalities in one CDC-led outbreak root-cause analysis (legionellosis control relevance). Tap temperatures >54°C and central tank temperatures >59°C were associated with lower Legionella levels in one recent school-water study. | (sylvestre2023module16legionella pages 10-14, hongUnknownyearthebodysystem pages 12-21, currie2023theecologyof pages 20-23) | Sylvestre & Julian, 2023; Nielsen et al., Oct 2024, https://doi.org/10.3390/microorganisms12102074 |
| Recent developments (2023–2024) | Recent work emphasizes environmental surveillance, broader molecular diagnostics beyond UAT, climate/weather associations, and built-environment risk modeling. These developments are directly relevant to PF recognition because PF is often missed in pneumonia-centered surveillance systems. | 2024 Medicare weather study: 37,883 legionellosis hospitalizations; precipitation at lag day 10 OR 1.08 (95% CI 1.05–1.11) per 1 cm; over 20 days, 3 cm precipitation increased odds >4-fold for legionellosis hospitalizations. | (wade2024weatherconditionsand pages 2-3, graham2024astudyof pages 134-137) | Wade & Herbert, Oct 2024, https://doi.org/10.1017/S0950268824000979; Graham, 2024 |
| Data limitations | Many PF data derive from aggregated outbreak investigations rather than individual patient-level natural history cohorts; PF-specific prevalence/incidence, QoL, genetic susceptibility, biomarkers, and formal ontology mappings were not available in the retrieved evidence. | Surveillance underascertainment likely substantial because mild cases may not seek care and UAT misses many non-LpSG1 infections. | (currie2023theecologyof pages 17-20, hamilton2018outbreaksoflegionnaires’ pages 2-4, graham2024astudyofa pages 134-137) | Hamilton et al., May 2018, https://doi.org/10.1007/s40572-018-0201-4; Graham, 2024 |


*Table: This table consolidates the most actionable evidence on Pontiac fever across clinical presentation, coding, causative species, exposure settings, diagnostics, management, prevention, and recent epidemiologic findings. It is useful as a compact knowledge-base-ready summary grounded in the cited evidence contexts.*

---

## Supporting visual evidence
A key summary table of outbreak sources and case counts (Pontiac fever and Legionnaires’ disease, 2006–2017) is provided as a cropped figure. (hamilton2018outbreaksoflegionnaires’ media e7cee3af)

References

1. (graham2024astudyofa pages 134-137): FF Graham. A study of legionellosis epidemiology and alternative environmental risk factors for the disease in new zealand. Unknown journal, 2024.

2. (sylvestre2023module16legionella pages 10-14): É Sylvestre and TR Julian. Module 16 legionella control in building water systems: a guide for building managers and operators. Unknown journal, 2023.

3. (khairullah2025legionnaires’diseasea pages 4-6): Aswin Rafif Khairullah, Harimurti Nuradji, Diana Nurjanah, Ni Luh Putu Indi Dharmayanti, Bantari Wisynu Kusuma Wardhani, Syahputra Wibowo, Ikechukwu Benjamin Moses, Dea Anita Ariani Kurniasih, Ima Fauziah, Muhammad Khaliim Jati Kusala, and Kartika Afrida Fauzia. Legionnaires’ disease: a review of emerging public health threats. International Journal of One Health, pages 62-77, Mar 2025. URL: https://doi.org/10.14202/ijoh.2025.62-77, doi:10.14202/ijoh.2025.62-77. This article has 2 citations.

4. (piedade2020analysisoflegionellas pages 30-33): SBL Piedade. Analysis of legionella's presence and concentration in water systems control. Unknown journal, 2020.

5. (currie2023theecologyof pages 20-23): S Currie. The ecology of legionella spp in compost. Unknown journal, 2023.

6. (hamilton2018outbreaksoflegionnaires’ pages 2-4): K. A. Hamilton, A. J. Prussin, W. Ahmed, and C. N. Haas. Outbreaks of legionnaires’ disease and pontiac fever 2006–2017. Current Environmental Health Reports, 5:263-271, May 2018. URL: https://doi.org/10.1007/s40572-018-0201-4, doi:10.1007/s40572-018-0201-4. This article has 118 citations and is from a peer-reviewed journal.

7. (kosinska2018useofhospital pages 1-2): Irena Kosińska, Aneta Nitsch-Osuch, Krzysztof Kanecki, Paweł Goryński, and Piotr Tyszko. Use of hospital morbidity data in an epidemiological analysis of diseases caused by legionella pneumophila. Medycyna Ogólna i Nauki o Zdrowiu, 24:251-256, Dec 2018. URL: https://doi.org/10.26444/monz/101676, doi:10.26444/monz/101676. This article has 2 citations.

8. (wade2024weatherconditionsand pages 2-3): Timothy J. Wade and Carly Herbert. Weather conditions and legionellosis: a nationwide case-crossover study among medicare recipients. Epidemiology and Infection, Oct 2024. URL: https://doi.org/10.1017/s0950268824000979, doi:10.1017/s0950268824000979. This article has 7 citations and is from a peer-reviewed journal.

9. (currie2023theecologyof pages 17-20): S Currie. The ecology of legionella spp in compost. Unknown journal, 2023.

10. (hamilton2018outbreaksoflegionnaires’ media e7cee3af): K. A. Hamilton, A. J. Prussin, W. Ahmed, and C. N. Haas. Outbreaks of legionnaires’ disease and pontiac fever 2006–2017. Current Environmental Health Reports, 5:263-271, May 2018. URL: https://doi.org/10.1007/s40572-018-0201-4, doi:10.1007/s40572-018-0201-4. This article has 118 citations and is from a peer-reviewed journal.

11. (khairullah2025legionnaires’diseasea pages 2-3): Aswin Rafif Khairullah, Harimurti Nuradji, Diana Nurjanah, Ni Luh Putu Indi Dharmayanti, Bantari Wisynu Kusuma Wardhani, Syahputra Wibowo, Ikechukwu Benjamin Moses, Dea Anita Ariani Kurniasih, Ima Fauziah, Muhammad Khaliim Jati Kusala, and Kartika Afrida Fauzia. Legionnaires’ disease: a review of emerging public health threats. International Journal of One Health, pages 62-77, Mar 2025. URL: https://doi.org/10.14202/ijoh.2025.62-77, doi:10.14202/ijoh.2025.62-77. This article has 2 citations.

12. (hongUnknownyearthebodysystem pages 12-21): A Hong. The body system in legionellosis. Unknown journal, Unknown year.

13. (graham2024astudyof pages 134-137): FF Graham. A study of legionellosis epidemiology and alternative environmental risk factors for the disease in new zealand. Unknown journal, 2024.

14. (graham2024astudyofa pages 81-84): FF Graham. A study of legionellosis epidemiology and alternative environmental risk factors for the disease in new zealand. Unknown journal, 2024.
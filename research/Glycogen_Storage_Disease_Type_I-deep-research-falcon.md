---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T19:29:59.746152'
end_time: '2026-05-08T19:56:57.797473'
duration_seconds: 1618.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glycogen Storage Disease Type I
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glycogen Storage Disease Type I
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glycogen Storage Disease Type I** covering all of the
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
- **Disease Name:** Glycogen Storage Disease Type I
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Glycogen Storage Disease Type I** covering all of the
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


# Glycogen Storage Disease Type I (GSD I): Disease Characteristics Report (2023–2024–prioritized)

## Executive summary
Glycogen storage disease type I (GSD I; “von Gierke disease”) is a Mendelian, autosomal-recessive disorder of hepatic (and renal) glucose production caused by defects in the endoplasmic-reticulum (ER) glucose-6-phosphatase system, leading to fasting hypoglycemia and characteristic secondary metabolic derangements (lactic acidosis, hypertriglyceridemia, hyperuricemia) with progressive hepatorenal complications. GSD Ia is caused by deficiency of the catalytic phosphatase (G6PC1), whereas GSD Ib is caused by deficiency of the ER glucose-6-phosphate transporter (SLC37A4/G6PT) and uniquely features chronic neutropenia/neutrophil dysfunction and inflammatory bowel disease (IBD). Recent (2023–2024) advances include broader clinical implementation of SGLT2 inhibition (empagliflozin) for GSD Ib immune complications and continuing late-stage clinical development of liver-directed AAV gene therapy for GSD Ia, alongside early clinical mRNA therapy and rapidly maturing genome-editing preclinical programs. (hannah2023glycogenstoragediseases pages 7-9, veigadacunha2023treatmentofthe pages 1-2, li2024empagliflozininchildren pages 1-2, NCT05139316 chunk 1, NCT05095727 chunk 1, koeberl2024genetherapyfor pages 1-3)

## 1. Disease information
### 1.1 Disease overview
GSD I is an inborn error of carbohydrate metabolism in which both glycogenolysis and gluconeogenesis fail to produce free glucose during fasting, causing severe fasting hypoglycemia and shunting of glucose-6-phosphate into alternative pathways that raise lactate, triglycerides, and uric acid. (weinstein2024shortandlongterm pages 1-2, hannah2023glycogenstoragediseases pages 1-3)

A concise clinical phenotype summary from a 2023 authoritative review includes: “Fasting hypoglycaemia, lactic acidosis, high triglycerides, elevated uric acid (tendency for gout), hepatomegaly, HCAs … with malignant potential, nephromegaly, renal tubular and glomerular disease, osteoporosis, pulmonary hypertension, anemia, bleeding disorder,” with GSD Ib additionally showing “neutropenia, neutrophil dysfunction, and IBD.” (hannah2023glycogenstoragediseases pages 1-3)

### 1.2 Key identifiers and synonyms
* **Synonyms:** von Gierke disease; glycogenosis type I; hepatorenal glycogenosis. (hannah2023glycogenstoragediseases pages 1-3, veigadacunha2023treatmentofthe pages 1-2)
* **MeSH (trial-linked):** “Glycogen Storage Disease Type I” (as condition browse term in ClinicalTrials.gov record). (NCT05139316 chunk 2)
* **OMIM:**
  * **GSD Ia:** OMIM **#232200** (G6PC1). (veigadacunha2023treatmentofthe pages 1-2)
  * **GSD Ib:** OMIM **#232220** (SLC37A4). (veigadacunha2023treatmentofthe pages 1-2)
* **MONDO / Orphanet / ICD-10/ICD-11:** Not retrievable from the currently ingested sources in this tool run; should be populated from OMIM/Orphanet/MONDO cross-references in downstream curation.

### 1.3 Evidence source type
Most identifier and phenotype statements here are derived from **aggregated disease-level resources (reviews, guidelines, clinical trials records)**, supplemented by **clinical cohorts** and **interventional studies** (human trials) and **animal model experiments**. (hannah2023glycogenstoragediseases pages 10-12, hannah2023glycogenstoragediseases pages 9-10, weinstein2024shortandlongterm pages 1-2, li2024empagliflozininchildren pages 1-2, koeberl2024genetherapyfor pages 3-4)

| Item | Value | Notes/Evidence |
|---|---|---|
| Disease name | Glycogen storage disease type I (GSD I) | Also referred to as the hepatorenal form of glycogen storage disease in MeSH-linked trial metadata; a hepatic glycogenosis affecting glucose production (NCT05139316 chunk 2, zhong2023glycogenstoragedisease pages 1-3) |
| Synonyms | Von Gierke disease; glycogenosis type I; hepatorenal glycogenosis | Recent reviews explicitly identify GSD I as “von Gierke disease” (veigadacunha2023treatmentofthe pages 1-2, zhong2023glycogenstoragedisease pages 1-3, hannah2023glycogenstoragediseases pages 1-3) |
| OMIM ID: GSD Ia | OMIM #232200 | Reported for GSD1a in recent 2023 review of neutropenia treatment and GSD I review material (veigadacunha2023treatmentofthe pages 1-2) |
| OMIM ID: GSD Ib | OMIM #232220 | Reported for GSD1b in recent 2023 review of neutropenia treatment and variant reviews (veigadacunha2023treatmentofthe pages 1-2) |
| Causal gene: GSD Ia | **G6PC1** (glucose-6-phosphatase catalytic subunit 1; G6Pase-α) | GSD Ia is caused by deficiency of glucose-6-phosphatase/G6PC1, the ER luminal enzyme catalyzing the terminal step of glycogenolysis and gluconeogenesis (zhong2023glycogenstoragedisease pages 18-21, zhong2023glycogenstoragedisease pages 1-3, maiorana2023currentunderstandingon pages 1-2) |
| Causal gene: GSD Ib | **SLC37A4** (glucose-6-phosphate transporter; G6PT) | GSD Ib is caused by deficiency of the glucose-6-phosphate transporter encoded by **SLC37A4**; unlike GSD Ia, it also causes neutropenia/neutrophil dysfunction (zhong2023glycogenstoragedisease pages 18-21, veigadacunha2023treatmentofthe pages 1-2, maiorana2023currentunderstandingon pages 1-2) |
| Inheritance | Autosomal recessive | Both GSD Ia and GSD Ib are described as autosomal recessive disorders (zhong2023glycogenstoragedisease pages 18-21, zhong2023glycogenstoragedisease pages 1-3) |
| Epidemiology | Incidence/prevalence about **1 in 100,000** live births | Recent reviews and summary tables report GSD I frequency around 1/100,000 (hannah2023glycogenstoragediseases pages 7-9, zhong2023glycogenstoragedisease pages 1-3) |
| High-prevalence population | Ashkenazi Jewish population: prevalence about **1 in 20,000** | Elevated prevalence and founder enrichment are summarized in recent epidemiology tables (hannah2023glycogenstoragediseases pages 7-9) |
| Subtype proportions | **~80% GSD Ia / ~20% GSD Ib** | Consistently reported across recent reviews and epidemiology summaries (hannah2023glycogenstoragediseases pages 7-9, zhong2023glycogenstoragedisease pages 18-21, zhong2023glycogenstoragedisease pages 1-3) |
| Example population-specific variant | **G6PC1 c.247C>T (p.Arg83Cys)** | Reported as 32% of variants in the European population and 96% of variants in the Jewish population; carrier frequency 1.4% in Ashkenazi Jewish population (hannah2023glycogenstoragediseases pages 7-9) |
| Example population-specific variant | **G6PC1 c.648G>T** | Common East Asian splice variant; approximately 85–88% of variants in Japanese population and 36–40% in Chinese population (hannah2023glycogenstoragediseases pages 7-9) |
| Example population-specific variant | **SLC37A4 c.352T>C (p.Trp118Arg)** | Reported as 37–50% of variants in the Japanese population (hannah2023glycogenstoragediseases pages 7-9) |
| Example population-specific variant | **SLC37A4 c.1042_1043delCT** | Reported as ~27–31% of variants in mixed European populations and ~32% in German patients (hannah2023glycogenstoragediseases pages 7-9) |
| Mechanistic distinction | GSD Ia: impaired G6P hydrolysis; GSD Ib: impaired ER G6P transport plus neutrophil toxicity from **1,5-AG6P** accumulation | The neutropenia mechanism in GSD Ib is linked to intracellular 1,5-anhydroglucitol-6-phosphate accumulation, a hexokinase inhibitor; this is not a feature of GSD Ia (veigadacunha2023treatmentofthe pages 1-2, maiorana2023currentunderstandingon pages 1-2) |


*Table: This table summarizes the core disease identifiers, causal genes, inheritance, epidemiology, and representative founder/population-enriched variants for glycogen storage disease type I. It is useful as a compact metadata and genetics reference for a disease knowledge base entry.*

## 2. Etiology
### 2.1 Disease causal factors
* **Primary cause (genetic):** autosomal-recessive loss of function in the ER glucose-6-phosphatase system.
  * **GSD Ia:** deficiency of **glucose-6-phosphatase-α (G6PC1)**. (zhong2023glycogenstoragedisease pages 1-3, zhong2023glycogenstoragedisease pages 18-21)
  * **GSD Ib:** deficiency of **glucose-6-phosphate transporter (G6PT; SLC37A4)**. (zhong2023glycogenstoragedisease pages 1-3, veigadacunha2023treatmentofthe pages 1-2)

**Mechanistic coupling definition (authoritative, mechanistic review):** “Glycogen storage disease type Ib (GSD1b) is due to a defect in the glucose-6-phosphate transporter (G6PT) of the endoplasmic reticulum (ER), which is encoded by the SLC37A4 gene… [which] allows the glucose-6-phosphate… to cross the endoplasmic reticulum (ER) membrane and be hydrolyzed by glucose-6-phosphatase (G6PC1).” (veigadacunha2023treatmentofthe pages 1-2)

### 2.2 Risk and protective factors
For this Mendelian disorder, “risk factors” are primarily **biallelic pathogenic variants** and population-enriched founder variants rather than environmental exposures. (hannah2023glycogenstoragediseases pages 7-9, zhong2023glycogenstoragedisease pages 18-21)

**Potential protective/modifier factors:** Not well established in the retrieved primary texts; however, genetic variation in renal 1,5-anhydroglucitol handling is a plausible modifier for neutropenia severity in GSD Ib (see gene–environment interaction section). (veigadacunha2023treatmentofthe pages 1-2, maiorana2023currentunderstandingon pages 1-2)

### 2.3 Gene–environment interactions
For GSD Ib neutropenia, the toxic metabolite **1,5-anhydroglucitol-6-phosphate (1,5-AG6P)** is derived from the **dietary/blood polyol 1,5-anhydroglucitol (1,5-AG)**; pharmacologic induction of glycosuria (SGLT2 inhibition) indirectly lowers circulating 1,5-AG and thereby reduces neutrophil 1,5-AG6P accumulation. (veigadacunha2023treatmentofthe pages 1-2)

## 3. Phenotypes
| Domain | Phenotype (plain language) | Suggested HPO term(s) | Typical onset/course | Notes/frequency/statistics with citations |
|---|---|---|---|---|
| Metabolic | Fasting hypoglycemia | HP:0001943 Hypoglycemia; HP:0001998 Fasting hypoglycemia | Usually infancy/early childhood; episodic with fasting; lifelong without treatment | Hallmark feature of GSD I due to failure of endogenous glucose production; Hannah et al. list “Fasting hypoglycaemia” among core GSD I features. In a 2024 Jordan trial of 38 children with GSD-1 on diet + MCT oil, proportion with hypoglycemia fell from 94.7% to 7.9% after 3 months (p<0.0001) (hannah2023glycogenstoragediseases pages 1-3, subih2024mediumchaintriglycerideoil pages 1-2) |
| Metabolic | Lactic acidosis / hyperlactatemia | HP:0002151 Increased serum lactate; HP:0001942 Metabolic acidosis; HP:0003128 Lactic acidosis | Early onset; worsens with fasting/poor metabolic control; chronic biochemical abnormality | GSD I tables/reviews consistently list lactic acidosis or hyperlactatemia as a core feature; Hannah notes “Blood lactate rises quickly with hypoglycemia” (hannah2023glycogenstoragediseases pages 1-3, veigadacunha2023treatmentofthe pages 1-2, maiorana2023currentunderstandingon pages 1-2) |
| Metabolic | Hypertriglyceridemia / hyperlipidemia | HP:0002155 Hyperlipidemia; HP:0003212 Hypertriglyceridemia | Early childhood onward; chronic; severity tracks metabolic control | Core laboratory abnormality in both Ia and Ib. In the Jordan 2024 intervention study, elevated triglycerides and cholesterol decreased significantly over 3 months; hypertriglyceridemia is also highlighted as a risk marker for later hepatic adenomas in GSD Ia cohorts (hannah2023glycogenstoragediseases pages 1-3, subih2024mediumchaintriglycerideoil pages 1-2, hannah2023glycogenstoragediseases pages 9-10) |
| Metabolic | Hyperuricemia / gout tendency | HP:0002149 Hyperuricemia; HP:0001997 Gout | Often childhood biochemical abnormality; gout tends to emerge later/adulthood | Hannah 2023 lists “elevated uric acid (tendency for gout)” among defining GSD I manifestations; low-purine diet and allopurinol are guideline-supported adjuncts (hannah2023glycogenstoragediseases pages 1-3, hannah2023glycogenstoragediseases pages 10-12) |
| Hepatic | Hepatomegaly | HP:0002240 Hepatomegaly | Infancy/early childhood; persistent; may improve but often chronic | One of the classic presenting signs in both Ia and Ib. Hannah 2023 lists hepatomegaly as core; the Jordan trial showed liver span reduction from 16.01 ± 2.65 cm to 14.85 ± 2.26 cm after intervention (p<0.0001) (hannah2023glycogenstoragediseases pages 1-3, subih2024mediumchaintriglycerideoil pages 1-2) |
| Renal | Nephromegaly and progressive renal disease | HP:0000105 Enlarged kidney; HP:0000077 Abnormality of the kidney; HP:0000093 Proteinuria | Renomegaly may present early; nephropathy/hyperfiltration progresses over years | Hannah 2023 lists “nephromegaly, renal tubular and glomerular disease” in GSD I. Long-term adult follow-up found nephropathy with hypertension in 10/14 GSD I adults (71%) in one center (hannah2023glycogenstoragediseases pages 1-3, hannah2023glycogenstoragediseases pages 10-12, hannah2023glycogenstoragediseases pages 9-10) |
| Hepatic neoplasia | Hepatocellular adenoma (HCA) risk | HP:0034249 Hepatocellular adenoma | Usually later childhood to adulthood; progressive complication with long-term survival | Major long-term complication of GSD I, especially Ia. In a Korean cohort of 72 GSD patients, 32/72 (44.4%) developed hepatic adenoma, median age 14.3 years; GSD type I was a risk factor. In a >20-year follow-up study, HCA occurred in 5/14 GSD I adults (35.7%) (hannah2023glycogenstoragediseases pages 9-10, hannah2023glycogenstoragediseases pages 10-12, hannah2023glycogenstoragediseases pages 1-3) |
| Hepatic neoplasia | Hepatocellular carcinoma (HCC) risk / malignant transformation | HP:0001402 Hepatocellular carcinoma | Usually after adenoma development; long-latency complication | In the Korean cohort, 4/32 patients with adenoma (12.5%) progressed to HCC after a mean interval of 6.7 years; Hannah notes HCAs “with malignant potential” in GSD I (hannah2023glycogenstoragediseases pages 9-10, hannah2023glycogenstoragediseases pages 1-3) |
| Skeletal | Low bone mineral density / osteoporosis | HP:0000939 Osteoporosis; HP:0004349 Reduced bone mineral density | Develops over years; chronic complication | Osteoporosis is listed in the GSD I phenotype summary; reduced bone health is a recognized long-term burden in both Ia and Ib, especially with chronic metabolic imbalance and dietary restriction (hannah2023glycogenstoragediseases pages 1-3, koeberl2024genetherapyfor pages 3-4, maiorana2023currentunderstandingon pages 1-2) |
| Hematologic | Anemia and bleeding tendency | HP:0001903 Anemia; HP:0001892 Abnormal bleeding; HP:0011890 Epistaxis | Variable; chronic or complication-related | Hannah 2023 lists “anemia, bleeding disorder” among GSD I manifestations. Anemia in GSD Ib may be exacerbated by enterocolitis; epistaxis is reported in clinical cohorts and case literature (hannah2023glycogenstoragediseases pages 1-3, maiorana2023currentunderstandingon pages 1-2) |
| Cardiopulmonary | Pulmonary hypertension | HP:0002092 Pulmonary hypertension | Usually later/complication phenotype; not universal | Included in Hannah 2023 summary of GSD I complications; echocardiographic surveillance is recommended in guidelines beginning around age 10 for pulmonary HTN screening (hannah2023glycogenstoragediseases pages 1-3, hannah2023glycogenstoragediseases pages 10-12) |
| Immuno-hematologic (GSD Ib) | Neutropenia | HP:0001875 Neutropenia | Usually infancy/childhood; chronic/fluctuating | Defining distinction of GSD Ib versus Ia. Caused by toxic 1,5-AG6P accumulation in neutrophils; empagliflozin studies show marked ANC improvement and reduced need for G-CSF (veigadacunha2023treatmentofthe pages 1-2, maiorana2023currentunderstandingon pages 1-2, li2024empagliflozininchildren pages 1-2) |
| Immuno-hematologic (GSD Ib) | Neutrophil dysfunction | HP:0012649 Abnormal neutrophil physiology | Childhood onward; chronic; infection-prone | Hannah specifically notes “neutropenia, neutrophil dysfunction” in GSD Ib. Mechanistically linked to intracellular 1,5-AG6P, a hexokinase inhibitor; Blood Advances 2024 reported significant improvement in neutrophil population and function with empagliflozin (hannah2023glycogenstoragediseases pages 1-3, veigadacunha2023treatmentofthe pages 1-2) |
| Infectious (GSD Ib) | Recurrent infections | HP:0002719 Recurrent infections | Childhood onward; recurrent/relapsing | Common consequence of neutropenia/neutrophil dysfunction. Empagliflozin literature reports fewer hospitalizations/infections and improved mucosal/skin lesions after therapy (maiorana2023currentunderstandingon pages 1-2, li2024empagliflozininchildren pages 1-2) |
| Gastrointestinal (GSD Ib) | Inflammatory bowel disease / enterocolitis | HP:0100279 Inflammatory bowel disease; HP:0002037 Diarrhea; HP:0002014 Diarrhea, chronic | Often emerges in later childhood; chronic/relapsing | A major GSD Ib complication. Recent trial/review literature notes IBD in up to 80% of patients with GSD Ib; in a 2024 open-label trial, 6/8 children completed 48 weeks of empagliflozin with significant endoscopic improvement/healing and no life-threatening adverse events (li2024empagliflozininchildren pages 1-2, maiorana2023currentunderstandingon pages 1-2, hannah2023glycogenstoragediseases pages 1-3) |
| Mucocutaneous (GSD Ib) | Oral ulcers, skin/perianal lesions, poor wound healing | HP:0000155 Oral ulcer; HP:0000988 Skin rash/lesion; HP:0033494 Abnormal wound healing | Childhood onward; chronic/recurrent | Characteristic of GSD Ib neutrophil dysfunction. Case reports document healing of chronic wounds and oral lesions after empagliflozin; one patient’s chronic abdominal wound nearly closed within 12 weeks and mucosal/skin lesions often improve rapidly (li2024empagliflozininchildren pages 1-2, maiorana2023currentunderstandingon pages 1-2) |


*Table: This table summarizes the core clinical and laboratory phenotype spectrum of glycogen storage disease type I, separating shared Ia/Ib manifestations from GSD Ib-specific immune complications. It is useful for knowledge-base curation because it links plain-language features to suggested HPO terms, onset/course patterns, and recent quantitative evidence.*

## 4. Genetic/molecular information
### 4.1 Causal genes and functional consequences
* **G6PC1 (GSD Ia):** loss of ER luminal catalytic hydrolysis of glucose-6-phosphate to glucose + Pi, preventing endogenous glucose output during fasting. (zhong2023glycogenstoragedisease pages 1-3, zhong2023glycogenstoragedisease pages 18-21)
* **SLC37A4 (GSD Ib):** loss of ER transport of glucose-6-phosphate (and, in neutrophils, transport enabling detoxification of 1,5-AG6P), causing the same metabolic phenotype as Ia plus immune dysfunction. (veigadacunha2023treatmentofthe pages 1-2, maiorana2023currentunderstandingon pages 1-2)

### 4.2 Pathogenic variants (representative; population enriched)
A 2023 epidemiology/variant summary provides multiple **population-enriched variants** and frequencies, e.g.:
* **G6PC1 c.247C>T (p.Arg83Cys):** 32% of variants in European populations and 96% in Jewish populations; carrier frequency 1.4% in Ashkenazi Jewish population. (hannah2023glycogenstoragediseases pages 7-9)
* **G6PC1 c.648G>T:** ~85–88% of variants in Japanese population; 36–40% in Chinese population. (hannah2023glycogenstoragediseases pages 7-9)
* **SLC37A4 c.352T>C (p.Trp118Arg):** 37–50% of variants in Japanese population. (hannah2023glycogenstoragediseases pages 7-9)
* **SLC37A4 c.1042_1043delCT:** ~27–31% of variants in mixed European populations; ~32% in German population. (hannah2023glycogenstoragediseases pages 7-9)

Variant class spectrum includes missense, frameshift, splice-altering variants, and whole-gene deletions (Ib), with autosomal-recessive inheritance. (hannah2023glycogenstoragediseases pages 7-9, wang2023threenovelslc37a4 pages 10-11)

### 4.3 Modifier genes / protective alleles (limited evidence)
In the context of GSD Ib neutropenia, heterozygous variants in the renal 1,5-AG transporter pathway have been hypothesized to reduce blood 1,5-AG and thereby “favourably influenc[e] neutropenia” (modifier concept). (veigadacunha2023treatmentofthe pages 1-2)

## 5. Environmental information
No infectious cause is implicated. Environmental/lifestyle factors mainly influence **metabolic control and complication risk** through fasting tolerance, dietary adherence, and intercurrent illness (which can precipitate hypoglycemia/lactic acidosis). (hannah2023glycogenstoragediseases pages 10-12, weinstein2024shortandlongterm pages 1-2)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (core metabolic defect)
**Upstream defect:** loss of ER glucose-6-phosphate hydrolysis (Ia) or transport (Ib). (zhong2023glycogenstoragedisease pages 1-3, veigadacunha2023treatmentofthe pages 1-2)

**Immediate biochemical consequence:** failure of hepatic endogenous glucose production during fasting → **severe fasting hypoglycemia**; glucose-6-phosphate accumulates and is diverted into pathways generating **lactate**, **lipids/triglycerides**, and **uric acid**. (weinstein2024shortandlongterm pages 1-2, hannah2023glycogenstoragediseases pages 1-3)

**Downstream organ disease:** chronic metabolic stress and substrate overload drives hepatomegaly, nephromegaly/progressive nephropathy, and—over time—risk of hepatic adenomas and malignant transformation. (hannah2023glycogenstoragediseases pages 9-10, derks2021glycogenstoragedisease pages 2-3)

### 6.2 GSD Ib neutropenia mechanism (cell-type specific)
A 2023 mechanistic review states: “Neutrophil dysfunction is… due to the accumulation of 1,5-anhydroglucitol-6-phosphate (1,5-AG6P), a potent inhibitor of hexokinases… Healthy neutrophils prevent the accumulation of 1,5-AG6P due to its hydrolysis by G6PC3 following transport into the ER by G6PT.” This mechanism directly motivated SGLT2 inhibitor therapy to lower blood 1,5-AG and reverse neutrophil dysfunction. (veigadacunha2023treatmentofthe pages 1-2)

### 6.3 Tissue/cell-type involvement (ontology suggestions)
* **Key tissues (UBERON):** liver (UBERON:0002107), kidney (UBERON:0002113), small intestine (UBERON:0002108). (zhong2023glycogenstoragedisease pages 1-3, weinstein2024shortandlongterm pages 1-2)
* **Key cell types (Cell Ontology):** hepatocyte (CL:0000182), renal proximal tubule epithelial cell (CL:0000066; for tubular disease), neutrophil (CL:0000775; GSD Ib). (hannah2023glycogenstoragediseases pages 1-3, veigadacunha2023treatmentofthe pages 1-2)

### 6.4 GO biological process suggestions
* Glucose homeostasis (GO:0042593)
* Gluconeogenesis (GO:0006094)
* Glycogen catabolic process (GO:0005980)
* Lipid metabolic process (GO:0006629)
* Neutrophil-mediated immunity (GO:0002446) and neutrophil chemotaxis (GO:0030593) (Ib)

### 6.5 Recent mechanistic developments (2023–2024)
* **Liver disease progression pathways:** In a hepatocyte-specific G6pc knockout model, attempted “normalization” of hepatic ChREBP activity via AAV-shRNA induced dysplastic growth, hepatocyte hypertrophy, increased inflammation, YAP activation, DNA damage, chromosomal instability and cGAS–STING pathway signatures; authors concluded ChREBP silencing is not a suitable liver-disease therapy in this context. (rutten2023normalizationofhepatic pages 1-2, rutten2023normalizationofhepatic pages 7-9)
* **Mitochondrial dysfunction:** A 2024 review summarizes mitochondrial abnormalities in G6pc−/− mice and supportive human data (e.g., altered respiratory chain enzyme activities, NAD+/NADH ratio, acylcarnitines and TCA metabolites), implicating impaired oxidative metabolism and mitophagy in systemic manifestations. (mishra2024mitochondrialdysfunctionin pages 5-6)

## 7. Anatomical structures affected
**Primary organs:** liver and kidney (hepatorenal form), with intestinal involvement; in GSD Ib, immune and gastrointestinal tract involvement (enterocolitis/IBD). (hannah2023glycogenstoragediseases pages 1-3, zhong2023glycogenstoragedisease pages 1-3, li2024empagliflozininchildren pages 1-2)

**Subcellular localization:** ER membrane/lumen (G6PT transporter; G6PC1 catalytic site faces ER lumen). (veigadacunha2023treatmentofthe pages 1-2)

## 8. Temporal development
Typical onset is **infancy/early childhood**, with episodic decompensation during fasting and progressive long-term complications (hepatic adenomas, renal disease) emerging in later childhood/adolescence/adulthood. HCAs are often detected around adolescence/young adulthood in reported cohorts (median ~14.8 years in one review summary). (derks2021glycogenstoragedisease pages 2-3, hannah2023glycogenstoragediseases pages 9-10)

## 9. Inheritance and population
### 9.1 Inheritance
**Autosomal recessive** for GSD Ia and Ib. (zhong2023glycogenstoragedisease pages 1-3)

### 9.2 Epidemiology and population genetics
A 2023 comprehensive epidemiology table reports:
* **Incidence:** ~**1 in 100,000**, with **~80% GSD Ia** and **~20% GSD Ib**. (hannah2023glycogenstoragediseases pages 7-9)
* **Ashkenazi Jewish prevalence:** ~**1 in 20,000** with enriched founder variants and a reported carrier frequency for G6PC1 p.Arg83Cys of 1.4% in this population. (hannah2023glycogenstoragediseases pages 7-9)

## 10. Diagnostics
### 10.1 Clinical/laboratory diagnosis
Characteristic laboratory profile: fasting hypoglycemia with hyperlactatemia/lactic acidosis, hypertriglyceridemia/hyperlipidemia, and hyperuricemia, with hepatomegaly and renomegaly. (subih2024mediumchaintriglycerideoil pages 1-2, hannah2023glycogenstoragediseases pages 1-3)

### 10.2 Confirmatory testing
* **Genetic testing:** recommended/used to confirm subtype (G6PC for Ia; SLC37A4 for Ib). (subih2024mediumchaintriglycerideoil pages 1-2, NCT05095727 chunk 1)
* **Liver biopsy/enzyme assays:** historically used; biopsy can show excess glycogen and fat in hepatocytes; however, noninvasive molecular diagnosis is increasingly emphasized. (subih2024mediumchaintriglycerideoil pages 1-2, samanta2025hepaticglycogenstorage pages 4-5)

### 10.3 Surveillance and monitoring
Guideline-oriented surveillance includes:
* Abdominal ultrasound in pediatrics; CT/MRI with contrast for adenoma surveillance/characterization. (hannah2023glycogenstoragediseases pages 10-12)
* Renal ultrasound; consideration of echocardiography starting around age 10 for pulmonary hypertension surveillance. (hannah2023glycogenstoragediseases pages 10-12)
* Routine labs: liver/kidney function, MELD, lipids, uric acid, CBC/iron studies; in GSD Ib specifically, evaluation of neutrophils. (hannah2023glycogenstoragediseases pages 10-12)
* Consideration of continuous glucose monitoring (CGM). (hannah2023glycogenstoragediseases pages 10-12, samanta2025hepaticglycogenstorage pages 4-5)

### 10.4 Differential diagnosis (brief)
Other hepatic GSDs (III, VI, IX) and broader inborn errors presenting with hypoglycemia and hepatomegaly; genetic testing is emphasized to disambiguate subtypes because clinical “gestalt” can be inaccurate (expert correctness ~47% across hepatic GSD cases in one study). (hannah2023glycogenstoragediseases pages 10-12)

## 11. Outcome / prognosis
### 11.1 Long-term complications and statistics
* **Hepatic adenomas:** In a long-term Korean cohort of 72 GSD patients, **32/72 (44.4%)** developed hepatic adenomas (median age 14.3 years). (hannah2023glycogenstoragediseases pages 9-10)
* **Malignant transformation:** Among those with adenomas in the same cohort, **4/32 (12.5%)** developed hepatocellular carcinoma after a mean 6.7-year interval; 10-year HCC-free survival from adenoma development was 82%. (hannah2023glycogenstoragediseases pages 9-10)
* **Renal disease:** In one >20-year follow-up series of hepatic GSD, nephropathy with hypertension occurred in **10/14** GSD I adults. (hannah2023glycogenstoragediseases pages 9-10)

### 11.2 Quality of life
Quality of life is strongly influenced by the burden of overnight/daytime dosing schedules and fear of hypoglycemia; extended-release starch aims to reduce dosing frequency and improve adherence and QoL. (weinstein2024shortandlongterm pages 1-2)

## 12. Treatment
### 12.1 Standard of care (real-world implementation)
* **Dietary therapy:** strict avoidance of fasting, frequent complex-carbohydrate feeds, cornstarch dosing; sucrose/lactose often limited; CGM is increasingly used in some settings. (hannah2023glycogenstoragediseases pages 10-12)
* **Supportive pharmacotherapy:** allopurinol for hyperuricemia/gout; ACEi/ARB for hyperfiltration/proteinuria; citrate/thiazide for hypocitraturia/hypercalciuria. (hannah2023glycogenstoragediseases pages 10-12)

### 12.2 2024 dietary trials / implementations
* **Extended-release cornstarch (Glycosade):** In the 2024 Glyde randomized double-blind cross-over study across hepatic GSDs, Glycosade improved fasting duration; **in GSD I**, median fasting duration was **6.5 h** vs **6.0 h** on UCCS (p=0.032) (Table 2), and 69% chose chronic Glycosade over 2-year follow-up. (weinstein2024shortandlongterm media e66ee9e8, weinstein2024shortandlongterm pages 1-2)
* **MCT oil adjunct (Jordan trial):** 38 children receiving UCCS + dietary restrictions plus MCT showed hypoglycemia prevalence reduction **94.7% → 7.9%** over 3 months (p<0.0001) and reduced liver span. (subih2024mediumchaintriglycerideoil pages 1-2)

### 12.3 GSD Ib immune-targeted therapy (2023–2024)
A 2024 prospective single-arm open-label trial of empagliflozin in **8** children with GSD-associated IBD reported: “The SES-CD score significantly decreased at week 48,” and “Six patients completed 48 weeks… and endoscopy showed significant improvement or healing,” with safety events including sweating/rehydration and UTI and “No serious or life-threatening adverse events.” (li2024empagliflozininchildren pages 1-2)

### 12.4 Advanced therapeutics and clinical trials (2023–2024)
* **AAV8 gene therapy (DTX401; pariglasgene brecaparvovec) Phase 3:** NCT05139316 (started 2021-11-08; primary completion 2024-02-20) is a randomized, quadruple-masked, crossover Phase 3 trial in patients ≥8 years (n=49). The **primary endpoint** is “Percent Change from Baseline to Week 48 in Daily Cornstarch Intake,” aligning with real-world clinical burden reduction. (NCT05139316 chunk 1)
* **AAV8 gene therapy (DTX401) Phase 1/2:** NCT03517085 enrolled 12 adults and tested single IV doses of 2.0×10^12 and 6.0×10^12 GC/kg with steroid regimens to mitigate hepatitis; included long-term extension and hypoglycemia-related endpoints. (NCT03517085 chunk 1)
* **mRNA therapy (mRNA-3745):** NCT05095727 is a Phase 1/2 adaptive SAD/MAD trial (start 2022-06-01; n=15) assessing safety and fasting-challenge outcomes; requires biallelic G6PC variants. (NCT05095727 chunk 1)

### 12.5 Cutting-edge preclinical (2024)
**Base editing:** A 2024 Nature Communications study reported: “BEAM-301 can correct up to ~60% of the G6PC1-R83C variant in liver cells… Interestingly, just ~10% base correction is therapeutic,” restoring blood glucose control and long-term survival in a humanized knock-in mouse model. (koeberl2024genetherapyfor pages 1-3)

### 12.6 MAXO suggestions (selected)
* Dietary therapy / cornstarch therapy (MAXO term suggestion: dietary supplementation/medical nutrition therapy)
* Continuous glucose monitoring (MAXO: glucose monitoring)
* Allopurinol therapy (MAXO: xanthine oxidase inhibitor therapy)
* ACE inhibitor therapy / ARB therapy (MAXO: renin–angiotensin system inhibitor therapy)
* Empagliflozin therapy (MAXO: SGLT2 inhibitor therapy)
* Gene therapy (MAXO: gene replacement therapy)
* mRNA therapy (MAXO: mRNA-based therapy)

## 13. Prevention
### 13.1 Primary prevention
Not applicable in the usual sense for Mendelian AR disorders; prevention is achieved via **carrier screening** and **reproductive genetic counseling** using known genes (G6PC1, SLC37A4). (zhong2023glycogenstoragedisease pages 1-3, veigadacunha2023treatmentofthe pages 1-2)

### 13.2 Secondary/tertiary prevention
* Prevention of metabolic crises via strict fasting avoidance and emergency planning. (hannah2023glycogenstoragediseases pages 10-12)
* Prevention/mitigation of long-term complications via surveillance imaging (adenomas), renal monitoring, and early treatment optimization. (hannah2023glycogenstoragediseases pages 10-12)

## 14. Other species / natural disease
A naturally occurring **GSD Ia dog model** carries a missense G6PC variant (Met→Ile at codon 121) and recapitulates hepatomegaly, hypoglycemia, dyslipidemia, renal disease, and hepatocellular carcinoma, supporting translational testing of therapies. (koeberl2024genetherapyfor pages 3-4)

## 15. Model organisms
Multiple **mouse models** exist:
* Germline G6pc1 disruption causing hypoglycemia, hyperlipidemia, hepatomegaly, renomegaly, and growth defects.
* Tissue-specific inducible G6pc−/− models (liver, kidney, intestine).
* G6pt−/− models recapitulating neutropenia (Ib) and inducible G6pt−/− with milder phenotype/increased survival.
These models are used to test gene therapy/genome editing and to study liver disease progression mechanisms. (koeberl2024genetherapyfor pages 3-4, rutten2023normalizationofhepatic pages 1-2)

## Expert opinions and authoritative analysis (selected)
* A 2023 Nature Reviews Disease Primers guideline-style summary emphasizes structured dietary therapy, broad surveillance, and complication-directed pharmacotherapy (allopurinol, ACEi/ARB, citrate/thiazide), and flags empagliflozin as an emerging consideration in GSD Ib. (hannah2023glycogenstoragediseases pages 10-12)
* A 2023 mechanistic review argues that a clear mechanistic understanding (1,5-AG6P toxicity) provides a rational, disease-modifying approach for GSD Ib neutropenia using SGLT2 inhibitors to lower blood 1,5-AG. (veigadacunha2023treatmentofthe pages 1-2)

## Limitations of this report
Some requested identifiers (e.g., MONDO ID, Orphanet ID, ICD-10/ICD-11 codes) and certain “PMID-preferred” citations are not present in the currently retrievable excerpts; they should be added by consulting OMIM/Orphanet/MONDO directly or GeneReviews and then crosslinking to PubMed records. All major biomedical claims included above are supported by the cited context IDs.


References

1. (hannah2023glycogenstoragediseases pages 7-9): William B. Hannah, Terry G. J. Derks, Mitchell L. Drumm, Sarah C. Grünert, Priya S. Kishnani, and John Vissing. Glycogen storage diseases. Nature Reviews Disease Primers, 9:1-23, Sep 2023. URL: https://doi.org/10.1038/s41572-023-00456-z, doi:10.1038/s41572-023-00456-z. This article has 107 citations.

2. (veigadacunha2023treatmentofthe pages 1-2): Maria Veiga-da-Cunha, Saskia B. Wortmann, Sarah C. Grünert, and Emile Van Schaftingen. Treatment of the neutropenia associated with gsd1b and g6pc3 deficiency with sglt2 inhibitors. Diagnostics, 13:1803, May 2023. URL: https://doi.org/10.3390/diagnostics13101803, doi:10.3390/diagnostics13101803. This article has 33 citations.

3. (li2024empagliflozininchildren pages 1-2): Zhiling Li, Xiaoyan Zhang, Huan Chen, Hanshi Zeng, Jiaxing Wu, Ying Wang, Ni Ma, Jiaoli Lan, Yuxin Zhang, Huilin Niu, Lei Shang, Xun Jiang, and Min Yang. Empagliflozin in children with glycogen storage disease-associated inflammatory bowel disease: a prospective, single-arm, open-label clinical trial. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-59320-z, doi:10.1038/s41598-024-59320-z. This article has 12 citations and is from a peer-reviewed journal.

4. (NCT05139316 chunk 1):  A Study of Adeno-Associated Virus Serotype 8-Mediated Gene Transfer of Glucose-6-Phosphatase in Patients With Glycogen Storage Disease Type Ia (GSDIa). Ultragenyx Pharmaceutical Inc. 2021. ClinicalTrials.gov Identifier: NCT05139316

5. (NCT05095727 chunk 1):  A Study of mRNA-3745 in Adult and Pediatric Participants With Glycogen Storage Disease Type 1a (GSD1a). ModernaTX, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05095727

6. (koeberl2024genetherapyfor pages 1-3): Dwight D. Koeberl, Rebecca L. Koch, Jeong‐A. Lim, Elizabeth D. Brooks, Benjamin D. Arnson, Baodong Sun, and Priya S. Kishnani. Gene therapy for glycogen storage diseases. Journal of Inherited Metabolic Disease, 47:93-118, Jul 2024. URL: https://doi.org/10.1002/jimd.12654, doi:10.1002/jimd.12654. This article has 31 citations and is from a peer-reviewed journal.

7. (weinstein2024shortandlongterm pages 1-2): DA Weinstein, RJ Jackson, EA Brennan, M Williams, JE Davison, F de Boer, TGJ Derks, C Ellerton, B Faragher, J Gribben, P Labrune, KM McKittrick, E Murphy, KM Ross, U Steuerwald, C Voillot, AJM Woodward, and HR Mundy. Short and long-term acceptability and efficacy of extended-release cornstarch in the hepatic glycogen storage diseases: results from the glyde study. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03274-y, doi:10.1186/s13023-024-03274-y. This article has 9 citations and is from a peer-reviewed journal.

8. (hannah2023glycogenstoragediseases pages 1-3): William B. Hannah, Terry G. J. Derks, Mitchell L. Drumm, Sarah C. Grünert, Priya S. Kishnani, and John Vissing. Glycogen storage diseases. Nature Reviews Disease Primers, 9:1-23, Sep 2023. URL: https://doi.org/10.1038/s41572-023-00456-z, doi:10.1038/s41572-023-00456-z. This article has 107 citations.

9. (NCT05139316 chunk 2):  A Study of Adeno-Associated Virus Serotype 8-Mediated Gene Transfer of Glucose-6-Phosphatase in Patients With Glycogen Storage Disease Type Ia (GSDIa). Ultragenyx Pharmaceutical Inc. 2021. ClinicalTrials.gov Identifier: NCT05139316

10. (hannah2023glycogenstoragediseases pages 10-12): William B. Hannah, Terry G. J. Derks, Mitchell L. Drumm, Sarah C. Grünert, Priya S. Kishnani, and John Vissing. Glycogen storage diseases. Nature Reviews Disease Primers, 9:1-23, Sep 2023. URL: https://doi.org/10.1038/s41572-023-00456-z, doi:10.1038/s41572-023-00456-z. This article has 107 citations.

11. (hannah2023glycogenstoragediseases pages 9-10): William B. Hannah, Terry G. J. Derks, Mitchell L. Drumm, Sarah C. Grünert, Priya S. Kishnani, and John Vissing. Glycogen storage diseases. Nature Reviews Disease Primers, 9:1-23, Sep 2023. URL: https://doi.org/10.1038/s41572-023-00456-z, doi:10.1038/s41572-023-00456-z. This article has 107 citations.

12. (koeberl2024genetherapyfor pages 3-4): Dwight D. Koeberl, Rebecca L. Koch, Jeong‐A. Lim, Elizabeth D. Brooks, Benjamin D. Arnson, Baodong Sun, and Priya S. Kishnani. Gene therapy for glycogen storage diseases. Journal of Inherited Metabolic Disease, 47:93-118, Jul 2024. URL: https://doi.org/10.1002/jimd.12654, doi:10.1002/jimd.12654. This article has 31 citations and is from a peer-reviewed journal.

13. (zhong2023glycogenstoragedisease pages 1-3): Jiamin Zhong, Yannian Gou, Piao Zhao, Xiangyu Dong, Meichun Guo, Aohua Li, Ailing Hao, Hue H. Luu, Tong‐Chuan He, Russell R. Reid, and Jiaming Fan. Glycogen storage disease type i: genetic etiology, clinical manifestations, and conventional and gene therapies. Pediatric Discovery, Jul 2023. URL: https://doi.org/10.1002/pdi3.3, doi:10.1002/pdi3.3. This article has 10 citations.

14. (zhong2023glycogenstoragedisease pages 18-21): Jiamin Zhong, Yannian Gou, Piao Zhao, Xiangyu Dong, Meichun Guo, Aohua Li, Ailing Hao, Hue H. Luu, Tong‐Chuan He, Russell R. Reid, and Jiaming Fan. Glycogen storage disease type i: genetic etiology, clinical manifestations, and conventional and gene therapies. Pediatric Discovery, Jul 2023. URL: https://doi.org/10.1002/pdi3.3, doi:10.1002/pdi3.3. This article has 10 citations.

15. (maiorana2023currentunderstandingon pages 1-2): Arianna Maiorana, Francesco Tagliaferri, and Carlo Dionisi-Vici. Current understanding on pathogenesis and effective treatment of glycogen storage disease type ib with empagliflozin: new insights coming from diabetes for its potential implications in other metabolic disorders. Frontiers in Endocrinology, Apr 2023. URL: https://doi.org/10.3389/fendo.2023.1145111, doi:10.3389/fendo.2023.1145111. This article has 25 citations.

16. (subih2024mediumchaintriglycerideoil pages 1-2): Hadil S. Subih, Reem A. Qudah, Sana Janakat, Hanadi Rimawi, Nour Amin Elsahoryi, and Linda Alyahya. Medium-chain triglyceride oil and dietary intervention improved body composition and metabolic parameters in children with glycogen storage disease type 1 in jordan: a clinical trial. Foods, 13:1091, Apr 2024. URL: https://doi.org/10.3390/foods13071091, doi:10.3390/foods13071091. This article has 4 citations.

17. (wang2023threenovelslc37a4 pages 10-11): Zhuolin Wang, Ruiqin Zhao, Xiaoyun Jia, Xiaolei Li, Li Ma, and Haiyan Fu. Three novel slc37a4 variants in glycogen storage disease type 1b and a literature review. The Journal of International Medical Research, Dec 2023. URL: https://doi.org/10.1177/03000605231216633, doi:10.1177/03000605231216633. This article has 4 citations.

18. (derks2021glycogenstoragedisease pages 2-3): Terry G. J. Derks, David F. Rodriguez-Buritica, Ayesha Ahmad, Foekje de Boer, María L. Couce, Sarah C. Grünert, Philippe Labrune, Nerea López Maldonado, Carolina Fischinger Moura de Souza, Rebecca Riba-Wolman, Alessandro Rossi, Heather Saavedra, Rupal Naik Gupta, Vassili Valayannopoulos, and John Mitchell. Glycogen storage disease type ia: current management options, burden and unmet needs. Nutrients, 13:3828, Oct 2021. URL: https://doi.org/10.3390/nu13113828, doi:10.3390/nu13113828. This article has 83 citations.

19. (rutten2023normalizationofhepatic pages 1-2): Martijn G. S. Rutten, Yu Lei, Joanne H. Hoogerland, Vincent W. Bloks, Hong Yang, Trijnie Bos, Kishore A. Krishnamurthy, Aycha Bleeker, Mirjam H. Koster, Rachel E. Thomas, Justina C. Wolters, Hilda van den Bos, Gilles Mithieux, Fabienne Rajas, Adil Mardinoglu, Diana C. J. Spierings, Alain de Bruin, Bart van de Sluis, and Maaike H. Oosterveer. Normalization of hepatic chrebp activity does not protect against liver disease progression in a mouse model for glycogen storage disease type ia. Cancer & Metabolism, Apr 2023. URL: https://doi.org/10.1186/s40170-023-00305-3, doi:10.1186/s40170-023-00305-3. This article has 2 citations and is from a peer-reviewed journal.

20. (rutten2023normalizationofhepatic pages 7-9): Martijn G. S. Rutten, Yu Lei, Joanne H. Hoogerland, Vincent W. Bloks, Hong Yang, Trijnie Bos, Kishore A. Krishnamurthy, Aycha Bleeker, Mirjam H. Koster, Rachel E. Thomas, Justina C. Wolters, Hilda van den Bos, Gilles Mithieux, Fabienne Rajas, Adil Mardinoglu, Diana C. J. Spierings, Alain de Bruin, Bart van de Sluis, and Maaike H. Oosterveer. Normalization of hepatic chrebp activity does not protect against liver disease progression in a mouse model for glycogen storage disease type ia. Cancer & Metabolism, Apr 2023. URL: https://doi.org/10.1186/s40170-023-00305-3, doi:10.1186/s40170-023-00305-3. This article has 2 citations and is from a peer-reviewed journal.

21. (mishra2024mitochondrialdysfunctionin pages 5-6): Kumudesh Mishra and Or Kakhlon. Mitochondrial dysfunction in glycogen storage disorders (gsds). Biomolecules, 14:1096, Sep 2024. URL: https://doi.org/10.3390/biom14091096, doi:10.3390/biom14091096. This article has 10 citations.

22. (samanta2025hepaticglycogenstorage pages 4-5): Arghya Samanta and Gautam Ray. Hepatic glycogen storage disease: deciphering the genotype-phenotype conundrum. World Journal of Clinical Pediatrics, Sep 2025. URL: https://doi.org/10.5409/wjcp.v14.i3.103415, doi:10.5409/wjcp.v14.i3.103415. This article has 0 citations.

23. (weinstein2024shortandlongterm media e66ee9e8): DA Weinstein, RJ Jackson, EA Brennan, M Williams, JE Davison, F de Boer, TGJ Derks, C Ellerton, B Faragher, J Gribben, P Labrune, KM McKittrick, E Murphy, KM Ross, U Steuerwald, C Voillot, AJM Woodward, and HR Mundy. Short and long-term acceptability and efficacy of extended-release cornstarch in the hepatic glycogen storage diseases: results from the glyde study. Orphanet Journal of Rare Diseases, Jul 2024. URL: https://doi.org/10.1186/s13023-024-03274-y, doi:10.1186/s13023-024-03274-y. This article has 9 citations and is from a peer-reviewed journal.

24. (NCT03517085 chunk 1):  Safety and Dose-Finding Study of DTX401 (AAV8G6PC) in Adults With Glycogen Storage Disease Type Ia (GSDIa). Ultragenyx Pharmaceutical Inc. 2018. ClinicalTrials.gov Identifier: NCT03517085

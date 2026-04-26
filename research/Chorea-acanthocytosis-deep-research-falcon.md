---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:35.005920'
end_time: '2026-04-25T22:31:10.104172'
duration_seconds: 935.1
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chorea-acanthocytosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chorea-acanthocytosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chorea-acanthocytosis** covering all of the
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
- **Disease Name:** Chorea-acanthocytosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chorea-acanthocytosis** covering all of the
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


## Chorea-acanthocytosis (VPS13A disease) — Comprehensive Disease Characteristics Report

**Target disease:** Chorea-acanthocytosis (ChAc), increasingly referred to as **“VPS13A disease”**. (lin2024exploringthepathophysiological pages 1-2)

**Evidence-note:** The report synthesizes *human clinical cohorts/case reports*, *human biomarker/diagnostic studies*, and *model-organism/cell-model mechanistic work*. For several ontology identifiers (e.g., MeSH, ICD-10/11), no explicit codes appeared in the retrieved full text; these are flagged as not available from the present evidence set.

| Disease | Identifiers | Gene / inheritance | Typical onset | Key phenotypes (approx. frequency) | Key diagnostics / biomarkers | Emerging disease-modifying approaches |
|---|---|---|---|---|---|---|
| Chorea-acanthocytosis (VPS13A disease; ChAc) | MONDO: MONDO_0008695; OMIM: 200150; Orphanet: ORPHA2388 | **VPS13A**; autosomal recessive; loss-of-function / biallelic variants | Usually 20–40 y; mean ~30–35 y; broader reported range 20–50 y | Seizures ~33–45%; psychiatric symptoms in >50%; acanthocytes often ~5–50% in blood, but may be absent/variable; movement disorder, orolingual dystonia/self-biting, neuropathy common (lin2024exploringthepathophysiological pages 3-4, perrone2025anovelvps13a pages 1-2, lin2024exploringthepathophysiological pages 1-2) | Peripheral smear for acanthocytes (repeat/wet prep may help); CK usually mildly elevated / hyperCKemia; chorein (VPS13A) Western blot in RBCs often absent/low; MRI may show caudate/striatal atrophy; FDG-PET striatal hypometabolism; DaTscan presynaptic dopaminergic deficit; sNfL increased in small studies (lin2024exploringthepathophysiological pages 3-4, lin2024exploringthepathophysiological pages 4-6, niemela2020phenotypicvariabilityin pages 1-2, lin2024exploringthepathophysiological pages 6-7, dobson‐stone2004choreindetectionfor pages 1-2) | Lyn kinase pathway is a leading target; **nilotinib** improved hematologic/neurologic phenotypes in **Vps13a−/−** mice and crosses BBB; **dasatinib** off-label in 3 patients showed RBC target engagement (↓ active Lyn, improved autophagy/actin markers) but no clear short-term CNS benefit; symptomatic care/DBS still standard (lin2024exploringthepathophysiological pages 3-4, peikert2021targetinglynkinase pages 1-2, lin2024exploringthepathophysiological pages 4-6, peikert2021targetinglynkinase pages 8-10) |


*Table: This table condenses the most actionable disease-characteristic facts for chorea-acanthocytosis/VPS13A disease, including identifiers, genetics, onset, phenotype frequencies, diagnostics, and emerging disease-modifying strategies. It is designed for direct embedding in a knowledge-base style report.*

---

### 1. Disease Information

#### 1.1 Concise overview (what is the disease?)
Chorea-acanthocytosis is an **ultra-rare, progressive neurodegenerative disorder** in the neuroacanthocytosis spectrum, characterized by **basal ganglia/striatal degeneration** and **acanthocytosis** (spiculated red blood cells) in peripheral blood, with prominent hyperkinetic movement disorder, psychiatric/cognitive features, seizures, and neuromuscular involvement. (jung2011neuroacanthocytosissyndromes pages 1-2, lin2024exploringthepathophysiological pages 1-2)

A key framing in recent literature is that the disorder reflects **loss-of-function of VPS13A (chorein)**, a lipid-transfer protein at membrane contact sites, and that the clinical phenotype may occur even when acanthocytosis is subtle or intermittently undetectable—supporting the “VPS13A disease” term. (lin2024exploringthepathophysiological pages 3-4, lin2024exploringthepathophysiological pages 1-2)

#### 1.2 Key identifiers (as available)
- **OMIM:** **200150** (explicitly stated). (dobson‐stone2004choreindetectionfor pages 1-2, weber2019choreaacanthocytosispresentingas pages 1-3)
- **Orphanet:** **ORPHA2388** (explicitly stated). (jung2011neuroacanthocytosissyndromes pages 1-2)
- **MONDO:** Not present in the retrieved papers’ text excerpts; however, OpenTargets disease object returned **MONDO_0008695** for “chorea-acanthocytosis.” (sharma2024identificationofpivotal pages 1-2)
- **MeSH / ICD-10 / ICD-11:** Not found in retrieved full-text excerpts (not inferable from current evidence set). (perrone2025anovelvps13a pages 1-2, jung2011neuroacanthocytosissyndromes pages 1-2)

#### 1.3 Synonyms / alternative names
- **Chorea-acanthocytosis** (ChAc) (jung2011neuroacanthocytosissyndromes pages 1-2)
- **VPS13A disease** (increasingly used in recent reviews) (lin2024exploringthepathophysiological pages 1-2)
- **Neuroacanthocytosis syndrome** (as a group context) (jung2011neuroacanthocytosissyndromes pages 1-2)

#### 1.4 Source type of disease information
Most structured disease information here derives from **aggregated disease-level resources and cohorts** (Orphanet Journal of Rare Diseases review; Spanish and Swedish cohorts), supplemented with **individual case reports** and mechanistic reviews. (jung2011neuroacanthocytosissyndromes pages 1-2, estevezfraga2018phenomenologyanddisease pages 1-2, niemela2020phenotypicvariabilityin pages 1-2, chen2023novelheterozygousvps13a pages 1-2)

**URLs & dates (examples):**
- Jung et al., *Orphanet J Rare Dis* (Published 2011-10-25): https://doi.org/10.1186/1750-1172-6-68 (jung2011neuroacanthocytosissyndromes pages 1-2)
- Lin et al., *Frontiers in Neurology* (2024-11): https://doi.org/10.3389/fneur.2024.1482936 (lin2024exploringthepathophysiological pages 1-2)

---

### 2. Etiology

#### 2.1 Disease causal factors
**Primary cause:** **biallelic (autosomal recessive) VPS13A pathogenic variants** leading to **loss of VPS13A protein (“chorein”)** or functional deficiency. (dobson‐stone2004choreindetectionfor pages 1-2, lin2024exploringthepathophysiological pages 1-2)

**Definition-level quote (abstract-based) supporting causality:** The 2024 Frontiers review states: *“VPS13A disease (also known as Chorea-Acanthocytosis, ChAc) … is a rare autosomal recessive genetic disorder caused by loss-of-function variants in the VPS13A gene.”* (lin2024exploringthepathophysiological pages 1-2)

#### 2.2 Risk factors
- **Genetic:** autosomal recessive inheritance; familial clustering and founder effects in certain populations are reported. (jung2011neuroacanthocytosissyndromes pages 1-2)
- **Environmental:** no validated environmental risk factors were identified in the retrieved evidence set; the disorder is presented as monogenic. (lin2024exploringthepathophysiological pages 1-2)

#### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved evidence set. (jung2011neuroacanthocytosissyndromes pages 1-2, lin2024exploringthepathophysiological pages 1-2)

#### 2.4 Gene–environment interactions
No gene–environment interactions were identified in the retrieved evidence set. (lin2024exploringthepathophysiological pages 1-2)

---

### 3. Phenotypes

#### 3.1 Core phenotype domains (with HPO suggestions)
Below are high-yield phenotypes, typical characteristics, and suggested **HPO** terms (term labels given; exact IDs should be validated against HPO database when populating a KB).

1) **Hyperkinetic movement disorder** (symptom/sign)
- Features: chorea, dystonia, tics; some cases show parkinsonism later/less frequent. (estevezfraga2018phenomenologyanddisease pages 1-2)
- HPO suggestions: *Chorea*, *Dystonia*, *Tic*, *Parkinsonism*, *Hyperkinesia*.

2) **Orofacial/orolingual dyskinesia and feeding dystonia**
- Hallmark clinical signs include tongue/lip biting and feeding dystonia. (peikert2021targetinglynkinase pages 1-2, estevezfraga2018phenomenologyanddisease pages 1-2)
- HPO suggestions: *Orofacial dyskinesia*, *Self-injurious behavior* (for self-biting), *Dysphagia*.

3) **Epilepsy / seizures**
- Frequency: seizures reported around **~45%** in the 2024 review; other sources emphasize seizures as common and sometimes presenting symptom. (lin2024exploringthepathophysiological pages 1-2, estevezfraga2018phenomenologyanddisease pages 1-2)
- Cohort statistic (Spain): **9/12** had seizures; one presented with **status epilepticus**; all but one became seizure-free on a single antiepileptic. (estevezfraga2018phenomenologyanddisease pages 1-2)
- HPO suggestions: *Seizure*, *Epilepsy*, *Status epilepticus*.

4) **Psychiatric symptoms and cognitive/behavioral change**
- Psychiatric symptoms reported in **>50%** in the 2024 review; Spanish cohort **10/12**. (lin2024exploringthepathophysiological pages 1-2, estevezfraga2018phenomenologyanddisease pages 1-2)
- HPO suggestions: *Obsessive-compulsive behavior*, *Depression*, *Anxiety*, *Cognitive impairment*, *Dementia*.

5) **Neuromuscular involvement (peripheral neuropathy / areflexia / myopathy)**
- Areflexia and axonal neuropathy are repeatedly noted in NA syndromes; Spanish cohort had neuropathy in all but one. (jung2011neuroacanthocytosissyndromes pages 1-2, estevezfraga2018phenomenologyanddisease pages 1-2)
- HPO suggestions: *Areflexia*, *Peripheral neuropathy*, *Muscle weakness*, *Elevated serum creatine kinase*.

6) **Hematologic abnormality: acanthocytosis** (laboratory)
- Acanthocytes are variable; reported as **commonly ~5–50%**, and detection is method-dependent; false negatives occur. (lin2024exploringthepathophysiological pages 3-4, spieler2020identificationoftwo pages 2-4)
- HPO suggestions: *Acanthocytosis*.

#### 3.2 Phenotype characteristics (onset, progression)
- **Onset:** typically adult onset; the 2024 review describes onset usually **20–40 years** with mean onset around **~35 years**. (lin2024exploringthepathophysiological pages 1-2)
- **Spanish cohort (n=12):** mean onset **24 years** (range **6–34**) with mean diagnosis age **34** (26–42) and mean follow-up **18 years**. (estevezfraga2018phenomenologyanddisease pages 1-2)
- **Swedish cohort (n=4):** mean onset **34** (range **30–38**) years; disease duration **9.5** years (range **2–17**). (niemela2020phenotypicvariabilityin pages 1-2)

#### 3.3 Quality-of-life impact (evidence-based description)
Cohort data indicate major functional decline over time. In the Spanish progression study, **after 10 years every patient needed 24-h supervision**. (estevezfraga2018phenomenologyanddisease pages 2-2)

---

### 4. Genetic / Molecular Information

#### 4.1 Causal gene(s)
- **VPS13A** (protein: VPS13A / chorein) is presented as the **only known pathogenic gene for ChAc** in recent reviews. (lin2024exploringthepathophysiological pages 1-2)

#### 4.2 Pathogenic variant spectrum (types + examples)
The disorder is typically associated with **loss-of-function** mechanisms (truncating, frameshift, splice, and structural variants), though some missense variants may impair function without eliminating protein. (lin2024exploringthepathophysiological pages 1-2, lin2024exploringthepathophysiological pages 4-6)

Examples explicitly reported in retrieved clinical genetics papers:
- **Nonsense:** NM_033305.2 **c.8215G>T (p.Glu2739Ter)** (reported as pathogenic). (chen2023novelheterozygousvps13a pages 1-2)
- **Large multi-exon deletion:** deletion of **exons 25–31** (reported pathogenic/expected LoF). (chen2023novelheterozygousvps13a pages 1-2)
- **Frameshift (case report):** novel homozygous **c.2061dup** (frameshift) plus **c.6796A>T** dual mutations in one patient. (chen2023novelheterozygousvps13a pages 1-2)

Diagnostic caveat: **genomic DNA sequencing alone may miss large deletions/duplications**, motivating the integration of protein testing (chorein Western blot) and quantitative DNA assays (e.g., MLPA/qPCR approaches). (spieler2020identificationoftwo pages 2-4)

#### 4.3 Molecular function and key mechanistic concepts (current understanding)
**Key concept (2023–2024 framing):** VPS13A is a **“bridge-like” lipid-transfer protein** localized to **membrane contact sites** and capable of **bulk lipid transport between organelles**, including ER–mitochondria interfaces. (kaestner2023proceedingsofthe pages 6-7, lin2024exploringthepathophysiological pages 3-4)

The 2024 mechanistic review highlights organellar and cellular consequences of VPS13A deficiency including **ER–mitochondria contact disruption**, **mitochondrial fragmentation**, and **reduced mitochondrial autophagy**, consistent with mitochondrial dysfunction. (lin2024exploringthepathophysiological pages 3-4)

#### 4.4 Interactors / modifier evidence (emerging)
- **XK scramblase:** interaction between VPS13A and XK is described as important for VPS13A function in humans. (lin2024exploringthepathophysiological pages 4-6)
- **Ubiquitin-ligase pathway in yeast model:** RSP5 binding partner evidence in yeast (meeting proceedings), suggesting regulation of lipid biosynthesis pathways as a modifier-like mechanism in model systems. (kaestner2023proceedingsofthe pages 8-10)

Evidence for true human clinical “modifier genes” remains limited in the retrieved set; case-level co-variant discussions exist but are not yet definitive. (perrone2025anovelvps13a pages 9-10)

#### 4.5 Ontology suggestions (for KB mapping)
**GO Biological Process (suggested):**
- *lipid transport* / *intermembrane lipid transfer* (kaestner2023proceedingsofthe pages 6-7)
- *autophagy* / *mitophagy* (kaestner2023proceedingsofthe pages 8-10)
- *actin cytoskeleton organization* (lin2024exploringthepathophysiological pages 3-4)
- *regulation of kinase activity* / *Src-family kinase signaling* (Lyn) (lin2024exploringthepathophysiological pages 3-4)
- *PI3K signaling* / *Rac1–PAK signaling* (lin2024exploringthepathophysiological pages 4-6)

**Cell Ontology (CL) suggestions:**
- *medium spiny neuron* (striatal vulnerability; discussed as loss of striatal neurons and MSN-related models) (peikert2021targetinglynkinase pages 1-2)
- *erythrocyte* (RBC acanthocytosis; RBC biomarkers) (peikert2021targetinglynkinase pages 8-10)

---

### 5. Environmental Information
No consistent non-genetic environmental or infectious contributors were identified in the retrieved evidence set. The disease is consistently framed as Mendelian/monogenic. (lin2024exploringthepathophysiological pages 1-2)

---

### 6. Mechanism / Pathophysiology

#### 6.1 Causal chain (high-level)
1) **VPS13A loss-of-function** → impaired **bulk lipid transport at membrane contact sites** (ER–mitochondria and other organelle contacts). (kaestner2023proceedingsofthe pages 6-7, lin2024exploringthepathophysiological pages 3-4)
2) Disrupted membrane/organelle lipid homeostasis and trafficking → **mitochondrial abnormalities** and **autophagy/mitophagy defects** (mitochondrial fragmentation; reduced mitochondrial autophagy; altered autophagy markers). (lin2024exploringthepathophysiological pages 3-4, kaestner2023proceedingsofthe pages 8-10)
3) Downstream cellular dysfunction in neurons and RBCs → **striatal neurodegeneration** and **RBC membrane/cytoskeletal defects** causing acanthocytosis. (peikert2021targetinglynkinase pages 1-2, lin2024exploringthepathophysiological pages 3-4)

#### 6.2 Lyn kinase / cytoskeletal axis (translationally actionable mechanism)
A central translational hypothesis is that **aberrant accumulation of activated Lyn kinase** contributes to RBC membrane/cytoskeletal abnormalities and potentially neuronal phenotypes, and that Src-family kinase inhibition can reverse some cellular readouts in models. (lin2024exploringthepathophysiological pages 3-4, peikert2021targetinglynkinase pages 1-2)

**Visual evidence (human off-label treatment biomarker readouts):** Peikert et al. show that **dasatinib suppressed overactive Lyn** and modulated downstream RBC autophagy markers (ULK1, p62) and actin features; Lyn activity rebounded after withdrawal. (peikert2021targetinglynkinase media 79551084, peikert2021targetinglynkinase media 70826a04)

#### 6.3 Candidate “wet biomarkers” under investigation (2024 review)
Because acanthocyte detection is inconsistent, recent work highlights exploratory biomarkers including **serum neurofilament light chain (sNfL)** and **plasma PRX5** (noted in mouse work and modulated by nilotinib in preclinical context). (lin2024exploringthepathophysiological pages 4-6)

---

### 7. Anatomical Structures Affected

#### 7.1 Organ and system level
- **Central nervous system:** basal ganglia/striatal degeneration with MRI evidence of caudate/putamen atrophy and functional imaging evidence of striatal hypometabolism. (estevezfraga2018phenomenologyanddisease pages 1-2, niemela2020phenotypicvariabilityin pages 1-2)
- **Peripheral blood (RBC morphology):** acanthocytosis and RBC cytoskeletal alterations. (lin2024exploringthepathophysiological pages 3-4, peikert2021targetinglynkinase pages 8-10)
- **Peripheral nervous system / muscle:** axonal neuropathy, areflexia, hyperCKemia and muscle involvement reported in NA syndromes and cohorts. (jung2011neuroacanthocytosissyndromes pages 1-2, estevezfraga2018phenomenologyanddisease pages 1-2)

#### 7.2 UBERON suggestions
- *striatum*, *caudate nucleus*, *putamen* (estevezfraga2018phenomenologyanddisease pages 1-2)
- *blood*, *erythrocyte* (as cell type; CL) (lin2024exploringthepathophysiological pages 3-4)

---

### 8. Temporal Development

#### 8.1 Onset
- Typical onset is early adult; reviews describe most commonly **20–40 years** with mean around **~35 years**. (lin2024exploringthepathophysiological pages 1-2)

#### 8.2 Progression and stages
The disease is **relentlessly progressive**. Orphanet review characterizes NA syndromes as progressing over **two to three decades**. (jung2011neuroacanthocytosissyndromes pages 1-2)

Functional decline metrics from Spain: **after 10 years every patient required 24-hour supervision**. (estevezfraga2018phenomenologyanddisease pages 2-2)

---

### 9. Inheritance and Population

#### 9.1 Inheritance
- **Autosomal recessive** inheritance is repeatedly emphasized. (lin2024exploringthepathophysiological pages 1-2, dobson‐stone2004choreindetectionfor pages 1-2)

#### 9.2 Epidemiology / prevalence
ChAc is exceptionally rare. Estimates from the Orphanet review:
- Prevalence for each NA disorder: **<1 to 5 per 1,000,000 inhabitants**. (jung2011neuroacanthocytosissyndromes pages 1-2)
- Total known/estimated ChAc cases worldwide: **~1,000**. (jung2011neuroacanthocytosissyndromes pages 1-2)

The Spanish cohort paper similarly notes ~1,000 cases worldwide and discusses higher local prevalence in Japan and French-Canadian communities (consistent with founder effects). (estevezfraga2018phenomenologyanddisease pages 1-2)

#### 9.3 Population genetics notes
Founder-effect language appears in Japan and French-Canadian clusters. (jung2011neuroacanthocytosissyndromes pages 1-2)

Carrier frequency and penetrance were not quantified in the retrieved evidence set. (jung2011neuroacanthocytosissyndromes pages 1-2)

---

### 10. Diagnostics

#### 10.1 Clinical tests and biomarkers (real-world implementation)
Core tests repeatedly used in practice include:
- **Peripheral blood smear** for acanthocytes (variable; method dependent; repeat testing helpful). (lin2024exploringthepathophysiological pages 3-4, spieler2020identificationoftwo pages 2-4)
- **Serum creatine kinase (CK):** often elevated/hyperCKemia and may be a useful indicator, though it can fluctuate (exercise, seizures). (peikert2021targetinglynkinase pages 8-10, spieler2020identificationoftwo pages 2-4)
- **Chorein (VPS13A) Western blot** on RBCs: often absent/low and highly informative. (dobson‐stone2004choreindetectionfor pages 1-2, jung2011neuroacanthocytosissyndromes pages 1-2)
- **Neuroimaging:** MRI caudate/striatal atrophy; FDG-PET striatal hypometabolism; DaTscan dopaminergic deficiency; MRS metabolic ratios in striatum. (niemela2020phenotypicvariabilityin pages 1-2, weber2019choreaacanthocytosispresentingas pages 1-3)

#### 10.2 Genetic testing strategy
Given VPS13A size and variant heterogeneity, multiple modalities may be required:
- sequencing for SNVs/indels (WES/WGS/panels)
- **copy-number detection** (MLPA/qPCR) for large deletions/duplications
- protein-level confirmation (chorein Western blot)
This multi-assay strategy is highlighted by evidence that some variants may be missed by routine sequencing and that acanthocytosis may not be consistently detectable. (spieler2020identificationoftwo pages 2-4, lin2024exploringthepathophysiological pages 4-6)

#### 10.3 Differential diagnosis
NA syndromes should be considered in the differential for **Huntington disease phenocopies**, including Huntington disease-like syndromes and McLeod syndrome; Orphanet review highlights that NA disorders must be included particularly if Huntington testing is negative. (jung2011neuroacanthocytosissyndromes pages 7-8)

---

### 11. Outcome / Prognosis

#### 11.1 Course and mortality
- NA syndromes are described as **eventually fatal**, with possible sudden death due to seizure or autonomic dysfunction, and late complications such as aspiration pneumonia/infections. (jung2011neuroacanthocytosissyndromes pages 7-8)
- In the Swedish cohort, one patient died during sleep at 42 years (noted as sudden death in a case series context). (niemela2020phenotypicvariabilityin pages 1-2)

#### 11.2 Disability trajectory
Spanish progression metrics indicate profound disability accumulation: **every patient required 24-hour supervision by 10 years**. (estevezfraga2018phenomenologyanddisease pages 2-2)

---

### 12. Treatment

#### 12.1 Current standard of care (symptomatic/supportive)
No curative therapies are established; management is largely **symptomatic**. (jung2011neuroacanthocytosissyndromes pages 1-2, lin2024exploringthepathophysiological pages 4-6)

Common symptomatic approaches include:
- **Movement disorder management** similar to Huntington disease (dopamine antagonists or depleters are described in NA review). (jung2011neuroacanthocytosissyndromes pages 7-8)
- **Seizure control:** generally responsive to standard anticonvulsants; the NA review warns that some anticonvulsants may worsen involuntary movements. (jung2011neuroacanthocytosissyndromes pages 7-8)
- **Multidisciplinary supportive care:** swallowing/nutrition support (including feeding tube when necessary) and PT/OT are recommended in NA review. (jung2011neuroacanthocytosissyndromes pages 7-8)

Spanish cohort real-world prescribing patterns included antiepileptics, atypical antipsychotics, benzodiazepines; tetrabenazine and other agents were also used. (estevezfraga2018phenomenologyanddisease pages 2-2)

**MAXO suggestions:**
- Symptomatic pharmacotherapy (*pharmacotherapy*)
- Antiseizure therapy (*anticonvulsant therapy*)
- Botulinum toxin injection (*botulinum toxin therapy*)
- Deep brain stimulation (*deep brain stimulation*)
- Enteral feeding (*gastrostomy tube placement* / *enteral nutrition*)
- Physical/occupational therapy (*rehabilitation therapy*)

#### 12.2 Deep brain stimulation (DBS)
- Swedish case series: bilateral GPi DBS **transiently attenuated feeding dystonia** but did not improve gait/chorea. (niemela2020phenotypicvariabilityin pages 1-2)
- Spanish cohort: 3 patients underwent GPi DBS with follow-up ~6 years; **progressive lack of efficacy** was noted in all cases and stimulation could worsen akinesia/gait in some settings. (estevezfraga2018phenomenologyanddisease pages 2-2)

#### 12.3 Experimental / disease-modifying approaches (Lyn kinase targeting)
**Dasatinib (off-label, human case series; translational biomarker approach):** In 3 patients, dasatinib treatment appeared **reasonably safe** and showed **RBC target engagement** (reduced Lyn activity, reduced accumulated autophagy-related proteins, partial restoration of actin cytoskeleton), but **clinical CNS effects were not proven** over the short treatment period. (peikert2021targetinglynkinase pages 8-10)

**Nilotinib (preclinical; repurposing rationale):** The 2024 review summarizes that nilotinib crosses the BBB in mice and ameliorated hematological and neurological phenotypes in Vps13a−/− models, supporting repurposing rationale. (lin2024exploringthepathophysiological pages 3-4)

**Figure-based evidence of target engagement (dasatinib):** the extracted Figure 4 panels demonstrate suppression of active Lyn under dasatinib and changes in RBC autophagy markers and actin staining. (peikert2021targetinglynkinase media 79551084, peikert2021targetinglynkinase media 70826a04)

---

### 13. Prevention
No primary prevention is currently available beyond **genetic counseling, carrier testing in affected families, and reproductive options**, consistent with monogenic autosomal recessive inheritance; explicit screening guideline statements were not present in the retrieved evidence set. (lin2024exploringthepathophysiological pages 1-2)

---

### 14. Other Species / Natural Disease
Natural disease in non-human species was not identified in the retrieved evidence set.

---

### 15. Model Organisms
Multiple experimental systems are described:
- **Vps13a−/− mouse models** that phenocopy aspects of human disease and are used for mechanistic and therapeutic (nilotinib) testing. (lin2024exploringthepathophysiological pages 3-4)
- **Human iPSC-derived neuronal models** (including medium spiny neuron–relevant models) used to study hyperexcitability and response to Src inhibition in mechanistic review. (lin2024exploringthepathophysiological pages 3-4)
- **Yeast and Dictyostelium** models for VPS13 biology and autophagy-related functions (discussed in meeting proceedings). (kaestner2023proceedingsofthe pages 8-10)

---

## Recent developments and “latest research” highlights (2023–2024 prioritized)

1) **Mechanistic consolidation around VPS13A as a bridge-like lipid transfer protein at membrane contact sites**, connecting lipid transport defects to downstream mitochondrial/autophagy/cytoskeletal phenotypes. (Frontiers review, 2024) (lin2024exploringthepathophysiological pages 3-4)
2) **Biomarker emphasis (“wet biomarkers”)**: recognition that acanthocytosis is variably detected and increasing interest in sNfL and red-cell functional readouts. (lin2024exploringthepathophysiological pages 4-6, peikert2021targetinglynkinase pages 8-10)
3) **Clinical trial readiness gaps**: off-label Lyn kinase inhibition demonstrates target engagement in RBCs but highlights the need for robust biomarkers and longitudinal natural history to power trials. (peikert2021targetinglynkinase pages 8-10)
4) **Registry/consortium momentum**: 2023 international meeting proceedings emphasize registries and future perspectives for NA syndromes research. (kaestner2023proceedingsofthe pages 6-7)

---

## Limitations of this report (evidence availability)
- **ICD/MeSH codes and some ontology identifiers** were not present in retrieved full-text excerpts; they should be filled from curated coding resources directly (OMIM/Orphanet/MeSH/ICD registries) during KB ingestion. (perrone2025anovelvps13a pages 1-2, jung2011neuroacanthocytosissyndromes pages 1-2)
- Some mechanistic and therapeutic claims (e.g., nilotinib efficacy) are summarized in review-level evidence; direct primary mouse-study full text was not retrieved here. (lin2024exploringthepathophysiological pages 3-4)


References

1. (lin2024exploringthepathophysiological pages 1-2): Jingqi Lin, Hongmei Meng, Nilupaer Shafeng, Jiaai Li, Huaiyu Sun, Xi Yang, Zhiqing Chen, and Shuai Hou. Exploring the pathophysiological mechanisms and wet biomarkers of vps13a disease. Frontiers in Neurology, Nov 2024. URL: https://doi.org/10.3389/fneur.2024.1482936, doi:10.3389/fneur.2024.1482936. This article has 3 citations and is from a peer-reviewed journal.

2. (lin2024exploringthepathophysiological pages 3-4): Jingqi Lin, Hongmei Meng, Nilupaer Shafeng, Jiaai Li, Huaiyu Sun, Xi Yang, Zhiqing Chen, and Shuai Hou. Exploring the pathophysiological mechanisms and wet biomarkers of vps13a disease. Frontiers in Neurology, Nov 2024. URL: https://doi.org/10.3389/fneur.2024.1482936, doi:10.3389/fneur.2024.1482936. This article has 3 citations and is from a peer-reviewed journal.

3. (perrone2025anovelvps13a pages 1-2): Benedetta Perrone, Viviana Mosca, Martina Pecoraro, Paola Ruffo, Elda Del Giudice, Alberta Leon, Martina Maino, Vincenzo La Bella, Rossella Spataro, and Francesca Luisa Conforti. A novel vps13a deletion in vps13a disease (chorea-acanthocytosis): a case report with brief literature summary. International Journal of Molecular Sciences, 26:11521, Nov 2025. URL: https://doi.org/10.3390/ijms262311521, doi:10.3390/ijms262311521. This article has 0 citations.

4. (lin2024exploringthepathophysiological pages 4-6): Jingqi Lin, Hongmei Meng, Nilupaer Shafeng, Jiaai Li, Huaiyu Sun, Xi Yang, Zhiqing Chen, and Shuai Hou. Exploring the pathophysiological mechanisms and wet biomarkers of vps13a disease. Frontiers in Neurology, Nov 2024. URL: https://doi.org/10.3389/fneur.2024.1482936, doi:10.3389/fneur.2024.1482936. This article has 3 citations and is from a peer-reviewed journal.

5. (niemela2020phenotypicvariabilityin pages 1-2): Valter Niemelä, Ammar Salih, Daniela Solea, Björn Lindvall, Jan Weinberg, Gabriel Miltenberger, Tobias Granberg, Aikaterini Tzovla, Love Nordin, Torsten Danfors, Irina Savitcheva, Niklas Dahl, and Martin Paucar. Phenotypic variability in chorea-acanthocytosis associated with novel <i>vps13a</i> mutations. Neurology Genetics, Jun 2020. URL: https://doi.org/10.1212/nxg.0000000000000426, doi:10.1212/nxg.0000000000000426. This article has 15 citations.

6. (lin2024exploringthepathophysiological pages 6-7): Jingqi Lin, Hongmei Meng, Nilupaer Shafeng, Jiaai Li, Huaiyu Sun, Xi Yang, Zhiqing Chen, and Shuai Hou. Exploring the pathophysiological mechanisms and wet biomarkers of vps13a disease. Frontiers in Neurology, Nov 2024. URL: https://doi.org/10.3389/fneur.2024.1482936, doi:10.3389/fneur.2024.1482936. This article has 3 citations and is from a peer-reviewed journal.

7. (dobson‐stone2004choreindetectionfor pages 1-2): Carol Dobson‐Stone, Antonio Velayos‐Baeza, Lea A. Filippone, Sarah Westbury, Alexander Storch, Torsten Erdmann, Stephen J. Wroe, Klaus L. Leenders, Anthony E. Lang, Maria Teresa Dotti, Antonio Federico, Saidi A. Mohiddin, Lameh Fananapazir, Geoff Daniels, Adrian Danek, and Anthony P. Monaco. Chorein detection for the diagnosis of chorea‐acanthocytosis. Annals of Neurology, 56:299-302, Aug 2004. URL: https://doi.org/10.1002/ana.20200, doi:10.1002/ana.20200. This article has 197 citations and is from a highest quality peer-reviewed journal.

8. (peikert2021targetinglynkinase pages 1-2): K. Peikert, Hannes Glaß, E. Federti, A. Matte, L. Pelzl, K. Akgün, T. Ziemssen, R. Ordemann, Florian Lang, The Lung Study Foch Hospital Group for Immunosuppresse Patients, L. De Franceschi, and A. Hermann. Targeting lyn kinase in chorea-acanthocytosis: a translational treatment approach in a rare disease. Journal of Personalized Medicine, 11:392, May 2021. URL: https://doi.org/10.3390/jpm11050392, doi:10.3390/jpm11050392. This article has 15 citations.

9. (peikert2021targetinglynkinase pages 8-10): K. Peikert, Hannes Glaß, E. Federti, A. Matte, L. Pelzl, K. Akgün, T. Ziemssen, R. Ordemann, Florian Lang, The Lung Study Foch Hospital Group for Immunosuppresse Patients, L. De Franceschi, and A. Hermann. Targeting lyn kinase in chorea-acanthocytosis: a translational treatment approach in a rare disease. Journal of Personalized Medicine, 11:392, May 2021. URL: https://doi.org/10.3390/jpm11050392, doi:10.3390/jpm11050392. This article has 15 citations.

10. (jung2011neuroacanthocytosissyndromes pages 1-2): Hans H Jung, Adrian Danek, and Ruth H Walker. Neuroacanthocytosis syndromes. Orphanet Journal of Rare Diseases, 6:68-68, Oct 2011. URL: https://doi.org/10.1186/1750-1172-6-68, doi:10.1186/1750-1172-6-68. This article has 255 citations and is from a peer-reviewed journal.

11. (weber2019choreaacanthocytosispresentingas pages 1-3): Juliane Weber, Lars Frings, Michel Rijntjes, Horst Urbach, Judith Fischer, Cornelius Weiller, Philipp T. Meyer, and Stephan Klebe. Chorea-acanthocytosis presenting as autosomal recessive epilepsy in a family with a novel vps13a mutation. Frontiers in Neurology, Jan 2019. URL: https://doi.org/10.3389/fneur.2018.01168, doi:10.3389/fneur.2018.01168. This article has 15 citations and is from a peer-reviewed journal.

12. (sharma2024identificationofpivotal pages 1-2): Ravinder Sharma, Kiran Yadav, Leeza Monga, Vikas Gupta, and Vikas Yadav. Identification of pivotal genes and pathways in chorea-acanthocytosis using comprehensive bioinformatic analysis. PLOS ONE, 19:e0309594, Sep 2024. URL: https://doi.org/10.1371/journal.pone.0309594, doi:10.1371/journal.pone.0309594. This article has 2 citations and is from a peer-reviewed journal.

13. (estevezfraga2018phenomenologyanddisease pages 1-2): Carlos Estévez-Fraga, Jose Luis López-Sendón Moreno, Juan Carlos Martínez-Castrillo, Jesus Perez-Perez, Michele Matarazzo, Pedro Garcia-Ruiz Espiga, Agustin Querejeta, Ricardo Rigual, Ignacio J. Posada Rodríguez, Monica Kurtis, Maria Cruz Rodriguez-Oroz, Maria Rosario Isabel Luquin, Maria-Mar Carmona-Abellan, and Justo García-Yébenes. Phenomenology and disease progression of chorea-acanthocytosis patients in spain. Parkinsonism &amp; Related Disorders, 49:17-21, Apr 2018. URL: https://doi.org/10.1016/j.parkreldis.2017.10.016, doi:10.1016/j.parkreldis.2017.10.016. This article has 10 citations and is from a peer-reviewed journal.

14. (chen2023novelheterozygousvps13a pages 1-2): Xi Chen, Piao Zhang, Lijuan Wang, and Yuhu Zhang. Novel heterozygous vps13a pathogenic variants in chorea-neuroacanthocytosis: a case report. BMC Neurology, Oct 2023. URL: https://doi.org/10.1186/s12883-023-03398-x, doi:10.1186/s12883-023-03398-x. This article has 3 citations and is from a peer-reviewed journal.

15. (spieler2020identificationoftwo pages 2-4): Derek Spieler, Antonio Velayos‐Baeza, Alžbeta Mühlbäck, Florian Castrop, Christian Maegerlein, Julia Slotta‐Huspenina, Benedikt Bader, Bernhard Haslinger, and Adrian Danek. Identification of two compound heterozygous vps13a large deletions in chorea‐acanthocytosis only by protein and quantitative dna analysis. Molecular Genetics & Genomic Medicine, Feb 2020. URL: https://doi.org/10.1002/mgg3.1179, doi:10.1002/mgg3.1179. This article has 10 citations and is from a peer-reviewed journal.

16. (estevezfraga2018phenomenologyanddisease pages 2-2): Carlos Estévez-Fraga, Jose Luis López-Sendón Moreno, Juan Carlos Martínez-Castrillo, Jesus Perez-Perez, Michele Matarazzo, Pedro Garcia-Ruiz Espiga, Agustin Querejeta, Ricardo Rigual, Ignacio J. Posada Rodríguez, Monica Kurtis, Maria Cruz Rodriguez-Oroz, Maria Rosario Isabel Luquin, Maria-Mar Carmona-Abellan, and Justo García-Yébenes. Phenomenology and disease progression of chorea-acanthocytosis patients in spain. Parkinsonism &amp; Related Disorders, 49:17-21, Apr 2018. URL: https://doi.org/10.1016/j.parkreldis.2017.10.016, doi:10.1016/j.parkreldis.2017.10.016. This article has 10 citations and is from a peer-reviewed journal.

17. (kaestner2023proceedingsofthe pages 6-7): Lars Kaestner. Proceedings of the eleventh international meeting on neuroacanthocytosis syndromes. Collection, Dec 2023. URL: https://doi.org/10.22028/d291-41331, doi:10.22028/d291-41331. This article has 4 citations.

18. (kaestner2023proceedingsofthe pages 8-10): Lars Kaestner. Proceedings of the eleventh international meeting on neuroacanthocytosis syndromes. Collection, Dec 2023. URL: https://doi.org/10.22028/d291-41331, doi:10.22028/d291-41331. This article has 4 citations.

19. (perrone2025anovelvps13a pages 9-10): Benedetta Perrone, Viviana Mosca, Martina Pecoraro, Paola Ruffo, Elda Del Giudice, Alberta Leon, Martina Maino, Vincenzo La Bella, Rossella Spataro, and Francesca Luisa Conforti. A novel vps13a deletion in vps13a disease (chorea-acanthocytosis): a case report with brief literature summary. International Journal of Molecular Sciences, 26:11521, Nov 2025. URL: https://doi.org/10.3390/ijms262311521, doi:10.3390/ijms262311521. This article has 0 citations.

20. (peikert2021targetinglynkinase media 79551084): K. Peikert, Hannes Glaß, E. Federti, A. Matte, L. Pelzl, K. Akgün, T. Ziemssen, R. Ordemann, Florian Lang, The Lung Study Foch Hospital Group for Immunosuppresse Patients, L. De Franceschi, and A. Hermann. Targeting lyn kinase in chorea-acanthocytosis: a translational treatment approach in a rare disease. Journal of Personalized Medicine, 11:392, May 2021. URL: https://doi.org/10.3390/jpm11050392, doi:10.3390/jpm11050392. This article has 15 citations.

21. (peikert2021targetinglynkinase media 70826a04): K. Peikert, Hannes Glaß, E. Federti, A. Matte, L. Pelzl, K. Akgün, T. Ziemssen, R. Ordemann, Florian Lang, The Lung Study Foch Hospital Group for Immunosuppresse Patients, L. De Franceschi, and A. Hermann. Targeting lyn kinase in chorea-acanthocytosis: a translational treatment approach in a rare disease. Journal of Personalized Medicine, 11:392, May 2021. URL: https://doi.org/10.3390/jpm11050392, doi:10.3390/jpm11050392. This article has 15 citations.

22. (jung2011neuroacanthocytosissyndromes pages 7-8): Hans H Jung, Adrian Danek, and Ruth H Walker. Neuroacanthocytosis syndromes. Orphanet Journal of Rare Diseases, 6:68-68, Oct 2011. URL: https://doi.org/10.1186/1750-1172-6-68, doi:10.1186/1750-1172-6-68. This article has 255 citations and is from a peer-reviewed journal.

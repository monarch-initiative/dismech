---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T11:05:45.843846'
end_time: '2026-05-10T11:21:10.662689'
duration_seconds: 924.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Central Congenital Hypothyroidism
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Central Congenital Hypothyroidism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Central Congenital Hypothyroidism** covering all of the
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
- **Disease Name:** Central Congenital Hypothyroidism
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Central Congenital Hypothyroidism** covering all of the
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


## Central Congenital Hypothyroidism (CCH) — Comprehensive Research Report

### 1. Disease information
**Overview / definition.** Central congenital hypothyroidism (CCH; also written “central CH”) is thyroid hormone deficiency present at birth due to insufficient hypothalamic and/or pituitary stimulation of an otherwise normal thyroid gland. It is **biochemically characterized by low serum free thyroxine (FT4) with a low, normal, or mildly elevated thyroid-stimulating hormone (TSH)** (“inappropriately” non-elevated for the degree of hypothyroxinemia). (garrelfs2025newbornscreeningfor pages 1-2, peters2026retrospectivemulticentreevaluation pages 14-17)

**Key identifiers (knowledgebase note).** This run did not retrieve OMIM/Orphanet/MONDO identifier records directly (no OMIM/Orphanet/MONDO pages were ingested), so these identifiers cannot be asserted from tool-evidence. Disease characterization below is derived from **aggregated literature resources** (guidelines/reviews) and **patient-level clinical cohorts/case reports**. (nagasaki2023guidelinesfornewborn pages 25-26, garrelfs2025newbornscreeningfor pages 1-2, peters2026retrospectivemulticentreevaluation pages 1-4, shibata2024clinicalandmolecular pages 1-2, yamamura2024anovelvariant pages 7-12)

**Common synonyms.** “Central CH”, “central congenital hypothyroidism”, “congenital central hypothyroidism”, and in some papers “CeCHT/CeCH” or “C-CH”. (garrelfs2025newbornscreeningfor pages 1-2, peters2026retrospectivemulticentreevaluation pages 1-4, yamamura2024anovelvariant pages 7-12)

**Direct abstract quote (definition).** Garrelfs et al. (European Thyroid Journal; 2025-02-01; https://doi.org/10.1530/etj-24-0329) states: “Central CH is caused by insufficient pituitary or hypothalamic control of thyroid function, biochemically characterized by a low serum free thyroxine (fT4), in combination with a low, normal or mildly elevated thyroid-stimulating hormone (TSH).” (garrelfs2025newbornscreeningfor pages 1-2)

---

### 2. Etiology
#### 2.1 Disease causal factors
**Genetic (Mendelian) causes—isolated CCH.** A 2025 focused review states that **isolated CCH is commonly monogenic**, with **five established genes**: **TSHB, TRHR, IGSF1, TBL1X, IRS4**. (garrelfs2025newbornscreeningfor pages 2-4, garrelfs2025newbornscreeningfor pages 1-2)

**Secondary/physiologic causes—transient central hypothyroidism.** The same review notes that **maternal thyrotoxicosis** can lead to **transient** central CH due to **in utero suppression of the fetal hypothalamic–pituitary–thyroid (HPT) axis**. (garrelfs2025newbornscreeningfor pages 2-4)

#### 2.2 Risk factors
**Clinical risk context for missed/delayed diagnosis.** In a UK multicentre cohort of clinically diagnosed cases (1996–2022), CCH often presented with **non-specific neonatal concerns** (hypoglycaemia, jaundice, weight concerns) and diagnostic uncertainty due to reference-range issues and confounders (e.g., prematurity, non-thyroidal illness). (peters2026retrospectivemulticentreevaluation pages 1-4, peters2026retrospectivemulticentreevaluation pages 14-17)

**Inheritance risk.** Several isolated CCH causes are X-linked (IGSF1, TBL1X, IRS4), so male sex and family history can be relevant in those families. (garrelfs2025newbornscreeningfor pages 2-4, shibata2024clinicalandmolecular pages 2-4)

#### 2.3 Protective factors / gene–environment interactions
No specific protective factors or gene–environment interactions were retrieved in the present evidence corpus.

---

### 3. Phenotypes (clinical presentation)
#### 3.1 Core laboratory phenotype (diagnostic pattern)
- **Low FT4** with **inappropriately low/normal TSH**; T3 may be normal. (garrelfs2025newbornscreeningfor pages 1-2, peters2026retrospectivemulticentreevaluation pages 14-17)

**Ontology suggestions (laboratory):**
- HPO: **Low circulating free thyroxine concentration** (e.g., “Low free T4”); **Inappropriately normal TSH** / **Low TSH** (use appropriate HPO terms depending on case).
- LOINC examples (test concepts): FT4, TSH, FT3; also **TBG** when screening algorithms require it. (nagasaki2023guidelinesfornewborn pages 25-26)

#### 3.2 Clinical phenotypes and frequencies (selected evidence)
**CCH with multiple pituitary hormone deficiency (MPHD/CPHD).** CCH is frequently part of MPHD (“congenital hypopituitarism”) and may be life-threatening due to coexisting ACTH and GH deficiency. Reviews cite **additional pituitary deficiencies in 61–98%** of CCH cases. (garrelfs2025newbornscreeningfor pages 1-2)

**UK clinically detected cohort (n=118).**
- Median age at diagnosis: **68 days** (range 1–5056). (peters2026retrospectivemulticentreevaluation pages 1-4)
- **96%** had combined pituitary hormone deficiencies. (peters2026retrospectivemulticentreevaluation pages 1-4)
- **Non-specific neonatal concerns** occurred in **83%** (hypoglycaemia/jaundice/weight concerns). (peters2026retrospectivemulticentreevaluation pages 1-4)
- **Neurodevelopmental defects** were reported in **34%**. (peters2026retrospectivemulticentreevaluation pages 1-4)

**Isolated CCH—Japan survey (isolated n=14).**
- Genotype-associated patterns: median diagnosis age **1–2 months** for IGSF1/TBL1X vs **14 months** for variant-negative. (shibata2024clinicalandmolecular pages 2-4)
- Reported associated findings include **obesity**, **intellectual disability**, and **pituitary hypoplasia** in subsets. (shibata2024clinicalandmolecular pages 1-2, shibata2024clinicalandmolecular pages 4-6)

**Isolated CCH—IGSF1 siblings case report (Japan).** Two brothers were diagnosed later in childhood after **school growth monitoring**, with a novel nonsense variant **IGSF1 NM_001555.5:c.3056G>A (p.Trp1019Ter)** and biochemical profile of low FT4 with normal TSH; additional features included overweight/obesity, dyslipidaemia (improved after levothyroxine), and in one brother prolactin deficiency with dissociated pubertal findings (testicular enlargement without testosterone rise). (yamamura2024anovelvariant pages 7-12)

**Ontology suggestions (selected):**
- HPO: **Congenital hypothyroidism**, **Hypothyroxinemia**, **Hypoglycemia**, **Neonatal jaundice**, **Failure to thrive / Poor weight gain** (or weight concerns), **Obesity**, **Intellectual disability**, **Short stature / Decreased growth rate**, **Prolactin deficiency**, **Macroorchidism**. (peters2026retrospectivemulticentreevaluation pages 1-4, shibata2024clinicalandmolecular pages 1-2, yamamura2024anovelvariant pages 7-12)

---

### 4. Genetic / molecular information
#### 4.1 Causal genes (isolated CCH)
**Established genes.** Reviews identify **TSHB, TRHR, IGSF1, TBL1X, IRS4** as established monogenic causes of isolated CCH. (garrelfs2025newbornscreeningfor pages 1-2, garrelfs2025newbornscreeningfor pages 2-4)

**Inheritance notes (from review/guidelines context).** IGSF1, TBL1X, and IRS4 are described as **X-linked** causes; TSHB and TRHR are rare causes and are commonly considered autosomal recessive in clinical genetics practice (inheritance mode not explicitly enumerated in all retrieved snippets). (garrelfs2025newbornscreeningfor pages 2-4, boelen2023neonatalscreeningfor pages 2-4)

#### 4.2 Pathogenic variants (examples from 2024 literature)
- **IGSF1**: nonsense variant **NM_001555.5:c.3056G>A (p.Trp1019Ter)** in two affected brothers; reported as absent from population databases and predicted loss-of-function, consistent with ACMG PVS1/PM1/PP1. (yamamura2024anovelvariant pages 7-12)

#### 4.3 Gene frequencies in recent cohorts
- Japan survey: among 14 isolated CCH patients, sequencing across known genes found **IGSF1 variants in 9** and **TBL1X variant in 1**; remaining 4 were variant-negative. (shibata2024clinicalandmolecular pages 2-4)

**Direct abstract quote (gene frequency).** Shibata et al. (Endocrine Journal; 2024-03-01; https://doi.org/10.1507/endocrj.ej23-0391) concludes: “The study revalidated that IGSF1 variants comprise the most frequent pathogenic variant in patients with isolated central CH in Japan.” (shibata2024clinicalandmolecular pages 1-2)

---

### 5. Environmental information
No consistent non-genetic environmental causes beyond maternal thyroid status–related transient cases were retrieved here. Maternal thyrotoxicosis-related fetal axis suppression is highlighted as a transient cause. (garrelfs2025newbornscreeningfor pages 2-4)

---

### 6. Mechanism / pathophysiology
#### 6.1 Causal chain (high-level)
1) **Upstream defect**: impaired hypothalamic TRH signaling or pituitary thyrotrope function (genetic defects in TSHB/TRHR/IGSF1/TBL1X/IRS4; or transient fetal suppression from maternal thyrotoxicosis). (garrelfs2025newbornscreeningfor pages 2-4, garrelfs2025newbornscreeningfor pages 1-2)
2) **Hormone output**: insufficient/ineffective TSH drive → reduced thyroid hormone secretion → **low FT4** with **non-elevated TSH**. (garrelfs2025newbornscreeningfor pages 1-2, peters2026retrospectivemulticentreevaluation pages 14-17)
3) **Downstream outcomes**: thyroid hormone deficiency in a critical developmental window contributes to neurodevelopmental risk; in MPHD, concurrent **ACTH/GH deficiencies** can add risk through **hypoglycaemia** and adrenal crisis that levothyroxine alone cannot prevent. (garrelfs2025newbornscreeningfor pages 1-2, garrelfs2025newbornscreeningfor pages 2-4)

#### 6.2 Cell types and processes (ontology suggestions)
- **Cell Ontology (CL)**: pituitary **thyrotroph** (TSH-producing cell), hypothalamic **TRH neuron**, pituitary **corticotroph** (ACTH) and **somatotroph** (GH) for MPHD context.
- **GO biological processes** (suggested): hypothalamus–pituitary–thyroid axis development/regulation; regulation of hormone secretion; thyroid hormone mediated signaling pathway; neurodevelopmental processes influenced by thyroid hormone.

---

### 7. Anatomical structures affected
- **Primary axis**: hypothalamus and pituitary regulation of thyroid function (HPT axis). (garrelfs2025newbornscreeningfor pages 1-2)
- **Secondary/complication-related systems**: brain/neurodevelopmental outcomes; risk driven both by hypothyroxinemia and by hypoglycaemia/adrenal crisis in MPHD. (garrelfs2025newbornscreeningfor pages 1-2, peters2026retrospectivemulticentreevaluation pages 1-4)

**UBERON suggestions:** hypothalamus; pituitary gland (anterior pituitary); thyroid gland.

---

### 8. Temporal development
- **Onset**: congenital (present at birth). (garrelfs2025newbornscreeningfor pages 1-2)
- **Diagnosis timing varies by screening strategy**: screening-capable programs can identify within the first weeks; clinically diagnosed cohorts may be delayed (median 68 days in a UK cohort, with long tail to years). (peters2026retrospectivemulticentreevaluation pages 1-4)

---

### 9. Inheritance and population
#### 9.1 Epidemiology
**Incidence.** Reviews/guidelines estimate incidence around **~1:13,000–1:30,000** live births, with country reports around **1:13,000–16,000** in settings using screening strategies that can detect CCH. (garrelfs2025newbornscreeningfor pages 1-2, nagasaki2023guidelinesfornewborn pages 25-26, olivieri2025isittime pages 4-5)

**Direct abstract quote (incidence).** Peters et al. (European Thyroid Journal; 2026-04-01; https://doi.org/10.1530/etj-26-0014) notes: “Central congenital hypothyroidism (incidence ∼1:13,000) occurs in isolation (40% cases) or with additional pituitary hormone deficiencies.” (peters2026retrospectivemulticentreevaluation pages 1-4)

#### 9.2 Inheritance
- **X-linked**: IGSF1, TBL1X, IRS4. (garrelfs2025newbornscreeningfor pages 2-4)
- **Other genetic forms**: TSHB and TRHR are described as rare causes of isolated CCH in reviews; inheritance is commonly autosomal recessive in clinical genetics (not explicitly stated in all retrieved text). (boelen2023neonatalscreeningfor pages 2-4, nagasaki2023guidelinesfornewborn pages 25-26)

---

### 10. Diagnostics
#### 10.1 Clinical tests / biomarkers
- Core: serum **FT4** and **TSH**; consider **FT3**, and in screening contexts **TBG** to interpret low total T4 and reduce false positives. (garrelfs2025newbornscreeningfor pages 1-2, nagasaki2023guidelinesfornewborn pages 25-26)

**Diagnostic challenge (expert analysis).** UK experience highlights that FT4 may require separate ordering and that lack of pediatric age-specific FT4 reference ranges can cause misclassification; central CH may be masked by non-thyroidal illness, transient hypothyroxinaemia of prematurity, or later “unmasking” after GH therapy. (peters2026retrospectivemulticentreevaluation pages 14-17)

#### 10.2 Pituitary evaluation (MPHD risk)
Recommended evaluations include pituitary hormone assessment (e.g., TRH/CRH stimulation tests) and pituitary MRI when possible, reflecting the frequent MPHD association. (nagasaki2023guidelinesfornewborn pages 25-26)

#### 10.3 Screening (newborn screening; real-world implementations)
**Why TSH-only screening misses CCH.** Because TSH can be normal/non-elevated despite low FT4, **TSH-only dried blood spot (DBS) newborn screening detects primary CH but misses many CCH cases**. In the Japanese survey, eight patients had TSH-only NBS with normal results, whereas six detected by low FT4 on NBS all carried IGSF1 variants. (shibata2024clinicalandmolecular pages 2-4, shibata2024clinicalandmolecular pages 1-2)

**Dutch stepwise T4–TSH–TBG algorithm.** The Netherlands uses a **stepwise total T4 → reflex TSH → reflex TBG** newborn screening approach to detect both primary and central CH while mitigating false positives from TBG deficiency. A figure of this algorithm is available from Boelen et al. (2023-06-01; https://doi.org/10.1530/etj-23-0041). (boelen2023neonatalscreeningfor pages 2-4, boelen2023neonatalscreeningfor media e737b93b)

**Machine-learning refinement (2023 development).** A Dutch study (Jansen et al., European Thyroid Journal; 2023-10-01; https://doi.org/10.1530/etj-23-0141) trained a random-forest model using **1,079 false-positive referrals**, **515 CH cases (431 primary; 84 central)** and **1,842 controls**; at enforced sensitivity 1.00, it achieved **PPV 0.48** and **AUROC 0.99**, highlighting **tyrosine** and **succinylacetone** (among others) as additional informative analytes. (jansen2023optimizingthedutch pages 1-2, jansen2023optimizingthedutch pages 5-7)

---

### 11. Outcome / prognosis
**Neurodevelopmental burden with delayed detection.** A 2025 review summarizes multiple datasets reporting high rates of impairment when detection is late (e.g., developmental delay in **51%** of 42 late-detected patients; neurologic sequelae in **37%** of 94 patients; and higher sequelae in isolated CCH vs MPHD in one dataset). (garrelfs2025newbornscreeningfor pages 2-4)

**UK cohort outcomes.** In the 118-case UK cohort, **34%** had neurodevelopmental defects and late-diagnosed cases experienced substantial treatment delays (mean delay 208 ± 486 days). (peters2026retrospectivemulticentreevaluation pages 1-4)

---

### 12. Treatment
#### 12.1 Standard of care
**Thyroid hormone replacement.** Levothyroxine (L‑T4) is the core therapy; dosing targets should be based on FT4 because TSH is unreliable in CCH. (nagasaki2023guidelinesfornewborn pages 25-26)

**Hydrocortisone-first precaution (MPHD context).** Guidelines emphasize that **hydrocortisone should be replaced before starting L‑T4** if ACTH deficiency is possible, because initiating L‑T4 can precipitate adrenal insufficiency; monitoring for adrenal insufficiency is advised, particularly around 7–10 days after starting L‑T4. (nagasaki2023guidelinesfornewborn pages 25-26)

**Dose recommendations (guideline).** For NBS-detected CCH, starting L‑T4 dose recommendations include **10–15 μg/kg/day for severe CCH (FT4 <0.4 ng/dL)** and **5–10 μg/kg/day for moderate-to-severe CCH (FT4 0.4–1.2 ng/dL)**, aiming for FT4 in the average-to-upper age-specific reference range. (nagasaki2023guidelinesfornewborn pages 25-26)

**MAXO suggestions:**
- Levothyroxine replacement therapy; adrenal hormone replacement (hydrocortisone) when indicated; newborn screening; pituitary MRI; endocrine function testing.

#### 12.2 Clinical trials / experimental therapies
No CCH-specific interventional clinical trials were retrieved by the tools in this run.

---

### 13. Prevention
**Secondary prevention is key:** newborn screening strategies capable of detecting low T4/FT4 with non-elevated TSH, plus confirmatory testing and early initiation of therapy. (garrelfs2025newbornscreeningfor pages 1-2, olivieri2025isittime pages 2-4)

**Expert opinion on screening expansion.** A 2025 review notes European guideline support for adding TT4/FT4 to TSH for detecting central CH and recommends optimization (e.g., TBG measurement; repeat screens in preterm/sick neonates) to manage false positives and cost. (olivieri2025isittime pages 2-4)

---

### 14. Other species / natural disease
No naturally occurring veterinary analogs were retrieved in the present evidence corpus.

---

### 15. Model organisms
A 2024 study assessed Irs4 knockout mice and found the murine HPT axis remained intact under tested conditions, suggesting compensation and potential limitations of this model for human IRS4-related CCH. (garrelfs2025newbornscreeningfor pages 2-4)

---

## Recent developments (prioritizing 2023–2024)
1) **National/genotype-focused characterization (Japan, 2024).** A Japanese survey revalidated IGSF1 as the most frequent known cause of isolated CCH and illustrated how FT4-inclusive screening strategies preferentially identify IGSF1 cases early. (shibata2024clinicalandmolecular pages 1-2, shibata2024clinicalandmolecular pages 2-4)
2) **Real-world delayed detection pathway evidence (UK cohort; 2026, but provides contemporary system-level evidence).** The UK multicentre cohort quantified delayed diagnosis and morbidity in TSH-only screening settings. (peters2026retrospectivemulticentreevaluation pages 1-4)
3) **Screening-analytics innovation (Netherlands, 2023).** Machine-learning use of amino acids/acylcarnitines improved modeled PPV for Dutch screening while preserving high sensitivity, suggesting feasible laboratory augmentations where these analytes are already measured for metabolic screening. (jansen2023optimizingthedutch pages 1-2, jansen2023optimizingthedutch pages 5-7)

---

## Current applications and real-world implementations
- **Dutch national screening algorithm** (T4–TSH–TBG) is an operational example that detects both primary and central CH using DBS measurements and TBG-based discrimination of binding-protein effects. (boelen2023neonatalscreeningfor pages 2-4, boelen2023neonatalscreeningfor media e737b93b)
- **Clinical pathway emphasis in TSH-only programs**: need for clinician vigilance and FT4 measurement in symptomatic neonates/infants, given that TSH can be misleadingly normal in CCH. (peters2026retrospectivemulticentreevaluation pages 14-17)

---

## Summary table (evidence synthesis)
| Topic | Key findings | Main supporting citation context IDs |
|---|---|---|
| Definition / biochemical criteria | Central congenital hypothyroidism (CCH) is thyroid hormone deficiency present at birth due to insufficient hypothalamic and/or pituitary stimulation of the thyroid; the characteristic biochemical pattern is low serum free T4 (FT4) with a low, normal, or only mildly elevated TSH, so TSH is “inappropriately” non-elevated for the degree of hypothyroxinemia. | (garrelfs2025newbornscreeningfor pages 1-2, nagasaki2023guidelinesfornewborn pages 25-26, peters2026retrospectivemulticentreevaluation pages 14-17) |
| Estimated incidence | Recent reviews/guidelines place incidence at roughly 1:13,000–1:30,000 live births overall; country-specific estimates include ~1:13,000 in Japan/UK-centered discussions and ~1:16,404 in the Dutch screening program. | (garrelfs2025newbornscreeningfor pages 1-2, nagasaki2023guidelinesfornewborn pages 25-26, peters2026retrospectivemulticentreevaluation pages 1-4, olivieri2025isittime pages 4-5) |
| MPHD vs isolated disease | CCH is most often part of multiple pituitary hormone deficiency (MPHD/CPHD), with reported additional pituitary deficiencies in 61%–98% of cases; one review states about one-third are isolated, whereas a UK clinically ascertained cohort found 96% had additional pituitary hormone deficiencies and estimated isolated disease may account for ~40% overall in broader populations. | (garrelfs2025newbornscreeningfor pages 1-2, boelen2023neonatalscreeningfor pages 2-4, peters2026retrospectivemulticentreevaluation pages 1-4) |
| Established monogenic causes: overview | Five established genes for isolated monogenic CCH are TSHB, TRHR, IGSF1, TBL1X, and IRS4. TSHB and TRHR were recognized earlier as rare causes; IGSF1, TBL1X, and IRS4 were identified more recently and explain many isolated cases found by modern sequencing approaches. | (garrelfs2025newbornscreeningfor pages 2-4, garrelfs2025newbornscreeningfor pages 1-2, boelen2023neonatalscreeningfor pages 2-4, nagasaki2023guidelinesfornewborn pages 25-26) |
| TSHB | TSHB causes isolated central hypothyroidism/isolated TSH deficiency; inheritance is typically autosomal recessive. Clinically important because immunoreactive TSH can be low/normal or sometimes biologically weak despite measurable concentrations. | (nagasaki2023guidelinesfornewborn pages 25-26, boelen2023neonatalscreeningfor pages 2-4, peters2026retrospectivemulticentreevaluation pages 14-17) |
| TRHR | TRHR is an established but very rare cause of isolated CCH; inheritance is typically autosomal recessive. It disrupts hypothalamic TRH signaling to pituitary thyrotropes. | (garrelfs2025newbornscreeningfor pages 2-4, boelen2023neonatalscreeningfor pages 2-4, nagasaki2023guidelinesfornewborn pages 25-26) |
| IGSF1 | IGSF1 is an X-linked cause and appears to be the most frequent known monogenic cause of isolated CCH in several series. Associated features can include obesity, macroorchidism/dissociated testicular enlargement, prolactin deficiency, and occasional intellectual disability. In the Japanese survey, 9/14 isolated cases carried IGSF1 variants; all 6 cases detected by low FT4 on NBS had IGSF1 variants. | (garrelfs2025newbornscreeningfor pages 2-4, boelen2023neonatalscreeningfor pages 2-4, shibata2024clinicalandmolecular pages 1-2, shibata2024clinicalandmolecular pages 2-4, yamamura2024anovelvariant pages 7-12) |
| TBL1X | TBL1X is an X-linked cause of isolated CCH, often associated with hearing-related or visual/neurodevelopmental findings in some reports. In the Japanese survey, 1/14 isolated cases carried a TBL1X variant; a TBL1X-related form has also been linked mechanistically to altered thyroid hormone action/gene regulation. | (garrelfs2025newbornscreeningfor pages 2-4, shibata2024clinicalandmolecular pages 1-2, shibata2024clinicalandmolecular pages 4-6) |
| IRS4 | IRS4 is an X-linked cause of isolated CCH. Human patients show reduced TSH secretion, but a 2024 mouse knockout study did not reproduce central hypothyroidism, suggesting species differences or compensation by other IRS proteins. | (garrelfs2025newbornscreeningfor pages 2-4) |
| Why TSH-only screening misses CCH | Standard DBS TSH-only newborn screening misses many CCH cases because TSH is often normal or not appropriately elevated despite low FT4. In one Japanese survey, 8 patients had TSH-only NBS and normal results, whereas low FT4-based detection identified cases. | (garrelfs2025newbornscreeningfor pages 1-2, shibata2024clinicalandmolecular pages 1-2, shibata2024clinicalandmolecular pages 2-4, yamamura2024anovelvariant pages 7-12) |
| T4-based screening | Earlier T4-based newborn screening could detect both primary CH and CCH, but many programs moved away from it because of high false-positive rates and confounding from TBG deficiency, prematurity, and illness. | (garrelfs2025newbornscreeningfor pages 1-2, garrelfs2025newbornscreeningfor pages 2-4, peters2026retrospectivemulticentreevaluation pages 4-6) |
| Dutch T4–TSH–TBG algorithm | The Dutch program uses a stepwise T4–TSH–TBG algorithm: total T4 for all newborns, reflex TSH in low-T4 samples, and TBG to help distinguish true hypothyroxinemia from TBG deficiency. This approach detects both primary CH and CCH while improving specificity; reported PPV for the Dutch program over 2007–2017 was ~21%, and Dutch incidence of detected CCH was ~1:16,404. | (boelen2023neonatalscreeningfor pages 2-4, olivieri2025isittime pages 4-5, boelen2023neonatalscreeningfor media e737b93b) |
| Machine-learning enhancement of Dutch screening | A 2023 Dutch random-forest model incorporating amino acids and acylcarnitines used 1,079 false-positive referrals, 515 CH cases (431 primary, 84 central), and 1,842 controls. With artificial sensitivity of 100%, PPV improved from 26% in a prior ML model to 48%, with AUROC 0.99. Key added contributors included tyrosine and succinylacetone, alongside T4, TSH, TBG, and T4/TBG ratio. | (jansen2023optimizingthedutch pages 1-2, jansen2023optimizingthedutch pages 5-7, jansen2023optimizingthedutch pages 8-9) |
| Diagnostic timing / real-world detection | Without central-sensitive screening, diagnosis is often delayed by months to years. In a UK multicenter cohort, median age at diagnosis was 68 days (range 1–5056), despite many neonatal symptoms. In the Japanese survey, median age at diagnosis was 1–2 months in IGSF1/TBL1X-positive cases versus 14 months in variant-negative patients. | (peters2026retrospectivemulticentreevaluation pages 1-4, shibata2024clinicalandmolecular pages 2-4) |
| Selected prognosis / outcome statistics | Reported adverse neurodevelopmental outcomes remain substantial when diagnosis is delayed: developmental delay in 51% of 42 late-detected patients; neurologic sequelae in 37% of 94 patients; higher neurologic sequelae in isolated CCH vs MPHD (60% vs 32%) in one series. In the UK cohort, neurodevelopmental defects were reported in 34%, and treatment delays in late-diagnosed cases averaged 208 ± 486 days. | (garrelfs2025newbornscreeningfor pages 2-4, peters2026retrospectivemulticentreevaluation pages 1-4, peters2026retrospectivemulticentreevaluation pages 14-17) |
| Treatment / management implications | Because MPHD and ACTH deficiency may coexist, hydrocortisone should be given before levothyroxine when adrenal insufficiency is possible. Guideline-recommended starting levothyroxine doses are 10–15 µg/kg/day for severe CCH and 5–10 µg/kg/day for moderate CCH, targeting FT4 in the upper reference range because TSH is unreliable for titration. | (nagasaki2023guidelinesfornewborn pages 25-26, garrelfs2025newbornscreeningfor pages 1-2) |


*Table: This table summarizes central congenital hypothyroidism across definition, epidemiology, genetics, screening, and prognosis. It highlights why TSH-only screening misses cases and how Dutch T4–TSH–TBG and machine-learning approaches improve detection.*

---

## Key screening algorithm figure (Dutch strategy)
The following figure region summarizes the Dutch stepwise T4–TSH–TBG screening algorithm used to detect central CH in addition to primary CH. (boelen2023neonatalscreeningfor media e737b93b, boelen2023neonatalscreeningfor media 77a8ab01)

---

## Evidence gaps / limitations of this run
- **Ontology identifiers (MONDO/Orphanet/OMIM/MeSH/ICD)** were not retrieved in the tool evidence and therefore cannot be asserted here.
- Evidence in this run is strong for **definition, screening, and selected genetic etiologies** (especially IGSF1), but less complete for rare gene-specific penetrance/expressivity, population-specific variant frequencies, and comprehensive non-genetic contributors.


References

1. (garrelfs2025newbornscreeningfor pages 1-2): Mark R Garrelfs, Christiaan F Mooij, Anita Boelen, A S Paul van Trotsenburg, and Nitash Zwaveling-Soonawala. Newborn screening for central congenital hypothyroidism: past, present and future. European Thyroid Journal, Feb 2025. URL: https://doi.org/10.1530/etj-24-0329, doi:10.1530/etj-24-0329. This article has 6 citations and is from a peer-reviewed journal.

2. (peters2026retrospectivemulticentreevaluation pages 14-17): Catherine Peters, Claire Wood, James M. Law, Chloe Stevens, Fatemah Alhusaini, Darla Rigby, Hannah Hornby, Tim Cheetham, and Nadia Schoenmakers. Retrospective, multicentre evaluation of central congenital hypothyroidism in the uk. European Thyroid Journal, Apr 2026. URL: https://doi.org/10.1530/etj-26-0014, doi:10.1530/etj-26-0014. This article has 0 citations and is from a peer-reviewed journal.

3. (nagasaki2023guidelinesfornewborn pages 25-26): Keisuke Nagasaki, Kanshi Minamitani, Akie Nakamura, Hironori Kobayashi, Chikahiko Numakura, Masatsune Itoh, Yuichi Mushimoto, Kaori Fujikura, Masaru Fukushi, and Toshihiro Tajima. Guidelines for newborn screening of congenital hypothyroidism (2021 revision). Clinical Pediatric Endocrinology, 32:26-51, Jan 2023. URL: https://doi.org/10.1297/cpe.2022-0063, doi:10.1297/cpe.2022-0063. This article has 33 citations and is from a peer-reviewed journal.

4. (peters2026retrospectivemulticentreevaluation pages 1-4): Catherine Peters, Claire Wood, James M. Law, Chloe Stevens, Fatemah Alhusaini, Darla Rigby, Hannah Hornby, Tim Cheetham, and Nadia Schoenmakers. Retrospective, multicentre evaluation of central congenital hypothyroidism in the uk. European Thyroid Journal, Apr 2026. URL: https://doi.org/10.1530/etj-26-0014, doi:10.1530/etj-26-0014. This article has 0 citations and is from a peer-reviewed journal.

5. (shibata2024clinicalandmolecular pages 1-2): Nao Shibata, Chikahiko Numakura, Takashi Hamajima, Kenichi Miyako, Ikuma Fujiwara, Jun Mori, Akihiko Saitoh, and Keisuke Nagasaki. Clinical and molecular analyses of isolated central congenital hypothyroidism based on a survey conducted in japan. Endocrine journal, 71:471-480, Mar 2024. URL: https://doi.org/10.1507/endocrj.ej23-0391, doi:10.1507/endocrj.ej23-0391. This article has 3 citations and is from a peer-reviewed journal.

6. (yamamura2024anovelvariant pages 7-12): Yoshiko Yamamura, Maki Fukami, Misayo Matsuyama, and Hirotake Sawada. A novel variant of &lt;i&gt;igsf1&lt;/i&gt; in siblings with congenital central hypothyroidism whose diagnosis was prompted by school health checkups. Clinical Pediatric Endocrinology, 33:17-22, Jan 2024. URL: https://doi.org/10.1297/cpe.2023-0046, doi:10.1297/cpe.2023-0046. This article has 0 citations and is from a peer-reviewed journal.

7. (garrelfs2025newbornscreeningfor pages 2-4): Mark R Garrelfs, Christiaan F Mooij, Anita Boelen, A S Paul van Trotsenburg, and Nitash Zwaveling-Soonawala. Newborn screening for central congenital hypothyroidism: past, present and future. European Thyroid Journal, Feb 2025. URL: https://doi.org/10.1530/etj-24-0329, doi:10.1530/etj-24-0329. This article has 6 citations and is from a peer-reviewed journal.

8. (shibata2024clinicalandmolecular pages 2-4): Nao Shibata, Chikahiko Numakura, Takashi Hamajima, Kenichi Miyako, Ikuma Fujiwara, Jun Mori, Akihiko Saitoh, and Keisuke Nagasaki. Clinical and molecular analyses of isolated central congenital hypothyroidism based on a survey conducted in japan. Endocrine journal, 71:471-480, Mar 2024. URL: https://doi.org/10.1507/endocrj.ej23-0391, doi:10.1507/endocrj.ej23-0391. This article has 3 citations and is from a peer-reviewed journal.

9. (shibata2024clinicalandmolecular pages 4-6): Nao Shibata, Chikahiko Numakura, Takashi Hamajima, Kenichi Miyako, Ikuma Fujiwara, Jun Mori, Akihiko Saitoh, and Keisuke Nagasaki. Clinical and molecular analyses of isolated central congenital hypothyroidism based on a survey conducted in japan. Endocrine journal, 71:471-480, Mar 2024. URL: https://doi.org/10.1507/endocrj.ej23-0391, doi:10.1507/endocrj.ej23-0391. This article has 3 citations and is from a peer-reviewed journal.

10. (boelen2023neonatalscreeningfor pages 2-4): Anita Boelen, Nitash Zwaveling-Soonawala, Annemieke C Heijboer, and A S Paul van Trotsenburg. Neonatal screening for primary and central congenital hypothyroidism: is it time to go dutch? European Thyroid Journal, Jun 2023. URL: https://doi.org/10.1530/etj-23-0041, doi:10.1530/etj-23-0041. This article has 26 citations and is from a peer-reviewed journal.

11. (olivieri2025isittime pages 4-5): Antonella Olivieri, Maria Cristina Vigone, Mariacarolina Salerno, and Luca Persani. Is it time to expand newborn screening for congenital hypothyroidism to other rare thyroid diseases? International Journal of Neonatal Screening, 11:65, Aug 2025. URL: https://doi.org/10.3390/ijns11030065, doi:10.3390/ijns11030065. This article has 0 citations.

12. (boelen2023neonatalscreeningfor media e737b93b): Anita Boelen, Nitash Zwaveling-Soonawala, Annemieke C Heijboer, and A S Paul van Trotsenburg. Neonatal screening for primary and central congenital hypothyroidism: is it time to go dutch? European Thyroid Journal, Jun 2023. URL: https://doi.org/10.1530/etj-23-0041, doi:10.1530/etj-23-0041. This article has 26 citations and is from a peer-reviewed journal.

13. (jansen2023optimizingthedutch pages 1-2): Heleen I Jansen, Marije van Haeringen, Marelle J Bouva, Wendy P J den Elzen, Eveline Bruinstroop, Catharina P B van der Ploeg, A S Paul van Trotsenburg, Nitash Zwaveling-Soonawala, Annemieke C Heijboer, Annet M Bosch, Robert de Jonge, Mark Hoogendoorn, and Anita Boelen. Optimizing the dutch newborn screening for congenital hypothyroidism by incorporating amino acids and acylcarnitines in a machine learning-based model. European Thyroid Journal, Oct 2023. URL: https://doi.org/10.1530/etj-23-0141, doi:10.1530/etj-23-0141. This article has 13 citations and is from a peer-reviewed journal.

14. (jansen2023optimizingthedutch pages 5-7): Heleen I Jansen, Marije van Haeringen, Marelle J Bouva, Wendy P J den Elzen, Eveline Bruinstroop, Catharina P B van der Ploeg, A S Paul van Trotsenburg, Nitash Zwaveling-Soonawala, Annemieke C Heijboer, Annet M Bosch, Robert de Jonge, Mark Hoogendoorn, and Anita Boelen. Optimizing the dutch newborn screening for congenital hypothyroidism by incorporating amino acids and acylcarnitines in a machine learning-based model. European Thyroid Journal, Oct 2023. URL: https://doi.org/10.1530/etj-23-0141, doi:10.1530/etj-23-0141. This article has 13 citations and is from a peer-reviewed journal.

15. (olivieri2025isittime pages 2-4): Antonella Olivieri, Maria Cristina Vigone, Mariacarolina Salerno, and Luca Persani. Is it time to expand newborn screening for congenital hypothyroidism to other rare thyroid diseases? International Journal of Neonatal Screening, 11:65, Aug 2025. URL: https://doi.org/10.3390/ijns11030065, doi:10.3390/ijns11030065. This article has 0 citations.

16. (peters2026retrospectivemulticentreevaluation pages 4-6): Catherine Peters, Claire Wood, James M. Law, Chloe Stevens, Fatemah Alhusaini, Darla Rigby, Hannah Hornby, Tim Cheetham, and Nadia Schoenmakers. Retrospective, multicentre evaluation of central congenital hypothyroidism in the uk. European Thyroid Journal, Apr 2026. URL: https://doi.org/10.1530/etj-26-0014, doi:10.1530/etj-26-0014. This article has 0 citations and is from a peer-reviewed journal.

17. (jansen2023optimizingthedutch pages 8-9): Heleen I Jansen, Marije van Haeringen, Marelle J Bouva, Wendy P J den Elzen, Eveline Bruinstroop, Catharina P B van der Ploeg, A S Paul van Trotsenburg, Nitash Zwaveling-Soonawala, Annemieke C Heijboer, Annet M Bosch, Robert de Jonge, Mark Hoogendoorn, and Anita Boelen. Optimizing the dutch newborn screening for congenital hypothyroidism by incorporating amino acids and acylcarnitines in a machine learning-based model. European Thyroid Journal, Oct 2023. URL: https://doi.org/10.1530/etj-23-0141, doi:10.1530/etj-23-0141. This article has 13 citations and is from a peer-reviewed journal.

18. (boelen2023neonatalscreeningfor media 77a8ab01): Anita Boelen, Nitash Zwaveling-Soonawala, Annemieke C Heijboer, and A S Paul van Trotsenburg. Neonatal screening for primary and central congenital hypothyroidism: is it time to go dutch? European Thyroid Journal, Jun 2023. URL: https://doi.org/10.1530/etj-23-0041, doi:10.1530/etj-23-0041. This article has 26 citations and is from a peer-reviewed journal.
---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T15:02:01.989162'
end_time: '2026-04-04T15:12:41.506324'
duration_seconds: 639.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lymphatic filariasis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 47
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lymphatic filariasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Lymphatic filariasis** covering all of the
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
- **Disease Name:** Lymphatic filariasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Lymphatic filariasis** covering all of the
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


# Lymphatic filariasis (LF): Disease characteristics research report (2023–2024 emphasis)

## Executive summary (current understanding)
Lymphatic filariasis (LF) is a mosquito-borne neglected tropical disease caused by filarial nematodes that reside in and damage the lymphatic system, producing a spectrum from asymptomatic infection to chronic morbidity such as lymphedema/elephantiasis and hydrocele. The global elimination strategy relies on (i) interrupting transmission through repeated mass drug administration (MDA) and (ii) morbidity management and disability prevention (MMDP), including the WHO Essential Package of Care (EPC) for lymphedema. Recent (2023–2024) work emphasizes (a) program “endgame” challenges (persistent hotspots, stopping criteria, and never-treated subpopulations), (b) real-world effectiveness gaps between microfilaria clearance and persistent antigenemia, (c) pharmacovigilance and safety surveillance for triple-drug MDA (IDA), (d) improved/alternative rapid antigen tests (QFAT vs FTS), and (e) short-course anti-*Wolbachia* macrofilaricide discovery using rodent models.

## 1. Disease information
### 1.1 Concise overview
LF is a mosquito-borne disease caused by *Wuchereria bancrofti*, *Brugia malayi*, and *Brugia timori*; adult worms live in the lymphatics and produce microfilariae that circulate in blood and are taken up by mosquitoes to continue transmission. LF is a major cause of acquired (non-hereditary) lymphedema and can be visualized by ultrasound (“filarial dance sign”) in some settings. (dietrich2019reviewofdancing pages 1-2, kura2024howdoesthe pages 1-2)

### 1.2 Synonyms and alternative names
Common alternative names include **elephantiasis** and **Bancroftian filariasis** (for *W. bancrofti* infection). The term “elephantiasis” is widely used but recognized as stigmatizing in patient-centered care contexts. (khaemba2023comparativesafetysurveillance pages 1-2, mackenzie2024managinglymphedemainduced pages 1-2)

### 1.3 Key identifiers (ontology and coding)
*Not recovered from the tool-retrieved full texts in this run:* ICD-10, ICD-11, MeSH, MONDO, Orphanet, OMIM identifiers.

In the retrieved evidence, LF is consistently described as a **neglected tropical disease** targeted for elimination as a **public health problem** by WHO’s Global Programme to Eliminate Lymphatic Filariasis (GPELF). (freitas2024thelymphaticfilariasis pages 1-2, sharma2023evaluatingeliminationthresholds pages 1-2)

### 1.4 Evidence source type
Most disease-level information below is from **aggregated programmatic and research resources** (systematic reviews, multi-country modeling, and national surveillance studies), supplemented with **human clinical trials** for morbidity management and **field studies** for diagnostics and MDA effectiveness/safety. (freitas2024thelymphaticfilariasis pages 1-2, kura2024howdoesthe pages 1-2, debrah2024adherencetohygiene pages 1-2, krishnasastry2024efficacyandsafety pages 1-2)

## 2. Etiology
### 2.1 Primary causes
**Causal infectious agents:** *Wuchereria bancrofti*, *Brugia malayi*, and *Brugia timori*. (dietrich2019reviewofdancing pages 1-2, kura2024howdoesthe pages 1-2)

**Transmission:** by multiple mosquito genera (including *Culex*, *Anopheles*, *Aedes*, among others), varying by region/ecology. (dietrich2019reviewofdancing pages 1-2, shaw2023lymphaticfilariasisendgame pages 1-2)

**Key mechanistic cofactor (endosymbiont):** many filarial worms harbor the bacterial endosymbiont *Wolbachia*, which is a major therapeutic target (e.g., doxycycline and experimental anti-*Wolbachia* agents). (krishnasastry2024efficacyandsafety pages 1-2, hegde2024combinationsofthe pages 1-2)

### 2.2 Risk factors (evidence-supported)
**Environmental/exposure risk:** living in endemic areas with competent mosquito vectors; programmatically, the “never treated” fraction in MDA campaigns is a critical determinant of elimination feasibility. (kura2024howdoesthe pages 1-2, sharma2023evaluatingeliminationthresholds pages 1-2)

**Programmatic risk factors:** delayed MDA rounds or insufficient rounds/coverage can permit persistence or resurgence. In Samoa, a long gap after a single national IDA round was associated with persistent transmission signals years later. (mayfield2024ongoingtransmissionof pages 1-2)

**Host factors for adverse events (AEs) during MDA:** female sex, obesity, higher tablet counts, and pre-existing clinical symptoms were predictors of AEs after IDA in Kenya. (khaemba2023comparativesafetysurveillance pages 1-2)

### 2.3 Protective factors
**High and repeated MDA coverage** (and minimizing never-treated persons) is protective at the population level, reducing infection prevalence and likelihood of sustained transmission. Modeling indicates achieving elimination thresholds depends strongly on the “never treated” proportion. (kura2024howdoesthe pages 1-2)

### 2.4 Gene–environment interactions
The retrieved corpus did not provide robust, specific **host genetic susceptibility loci** or explicit gene–environment interaction analyses for LF (e.g., GWAS or candidate gene associations). This remains a gap in the evidence retrieved here.

## 3. Phenotypes (clinical spectrum)
LF manifests across an infection-to-disease continuum:

### 3.1 Core clinical phenotypes (with ontology term suggestions)
1) **Lymphedema (limb swelling), chronic progressive**  
   * Evidence: described as a major LF morbidity and a focus of EPC/MMDP. (mackenzie2024managinglymphedemainduced pages 1-2, krishnasastry2024efficacyandsafety pages 1-2)  
   * HPO suggestions: **HP:0001004 Lymphedema**, **HP:0012378 Edema**, **HP:0000924 Swelling**.

2) **Elephantiasis (severe chronic lymphedema with dermal changes)**  
   * Evidence: highlighted as hallmark, disfiguring clinical disease. (mackenzie2024managinglymphedemainduced pages 1-2)  
   * HPO suggestions: **HP:0002607 Elephantiasis** (if available), otherwise model as severe **HP:0001004** with skin thickening terms.

3) **Hydrocele**  
   * Evidence: cited as a chronic morbidity; directly addressable via surgery. (khaemba2023comparativesafetysurveillance pages 1-2, mackenzie2024managinglymphedemainduced pages 1-2)  
   * HPO suggestion: **HP:0000034 Hydrocele**.

4) **Acute adenolymphangitis (ADL) / acute attacks**  
   * Evidence: EPC trials measure ADL frequency and QOL; doxycycline hypothesized to reduce attacks. (debrah2024adherencetohygiene pages 1-2, krishnasastry2024efficacyandsafety pages 1-2)  
   * HPO suggestions: **HP:0001945 Fever**, **HP:0011134 Lymphangitis**, **HP:0002716 Lymphadenitis**.

5) **Microfilaremia / antigenemia as infection phenotypes**  
   * Evidence: used as elimination metrics (e.g., mf prevalence thresholds, antigen tests). (fimbo2024efficacyofivermectin pages 1-2, kura2024howdoesthe pages 1-2)  
   * Not strictly HPO; better captured as laboratory abnormality terms; e.g., “microfilariae present in blood smear.”

### 3.2 Phenotype characteristics (onset, progression, frequency)
* **Chronic lymphedema/hydrocele**: typically develops after prolonged infection; can be progressive and associated with stigma and reduced productivity. (kura2024howdoesthe pages 1-2, mackenzie2024managinglymphedemainduced pages 1-2)
* **ADL attacks**: episodic inflammatory episodes that EPC aims to reduce. (krishnasastry2024efficacyandsafety pages 1-2)

Quantitative, phenotype-specific frequencies in infected populations were not comprehensively available from the retrieved texts, except program-level statements (e.g., LF as a major disability cause) and trial cohorts for lymphedema management. (khaemba2023comparativesafetysurveillance pages 1-2, krishnasastry2024efficacyandsafety pages 1-2)

### 3.3 Quality-of-life (QoL) impact
The modeling paper explicitly notes chronic morbidity (hydrocele/lymphedema) is associated with “disability, pain, mental health problems, reduced productivity, and social stigmatisation.” (kura2024howdoesthe pages 1-2)

Recent MMDP trials in 2024 emphasize QoL as an outcome and conclude that EPC improves QoL and clinical condition, while adding doxycycline did not outperform placebo in the Kerala RCT. (krishnasastry2024efficacyandsafety pages 1-2)

## 4. Genetic / molecular information
### 4.1 Causal genes and pathogenic variants
LF is **not a monogenic inherited disorder**; causal “genes” are those of the parasites (and possibly *Wolbachia*) rather than human germline pathogenic variants.

The retrieved evidence base did not provide specific human causal variants, modifier genes, or population allele frequencies relevant to LF susceptibility.

### 4.2 Molecular targets relevant to disease biology and treatment
* **Anti-*Wolbachia* targeting** is a major molecular strategy (e.g., doxycycline; experimental AWZ1066S). (krishnasastry2024efficacyandsafety pages 1-2, hegde2024combinationsofthe pages 1-2)
* **Type 2 immunity / IL-4R signaling / CCR2+ monocytes and alternatively activated macrophages** are implicated in lymphatic remodeling and dysfunction in experimental models. (furlongsilva2021tetracyclinesimproveexperimental pages 1-3)

## 5. Environmental information
### 5.1 Environmental and lifestyle factors
Core environmental determinant is **mosquito exposure** in endemic regions. (dietrich2019reviewofdancing pages 1-2, kura2024howdoesthe pages 1-2)

The retrieved evidence did not provide strong causal links for lifestyle exposures (e.g., smoking, diet) specific to LF acquisition; however, obesity was an AE predictor in IDA safety surveillance. (khaemba2023comparativesafetysurveillance pages 1-2)

### 5.2 Infectious agents
Primary pathogens: *W. bancrofti*, *B. malayi*, *B. timori*. (dietrich2019reviewofdancing pages 1-2, kura2024howdoesthe pages 1-2)

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (infection → morbidity)
1) Mosquito inoculation introduces infective larvae, which mature to adult worms in lymphatic vessels. (dietrich2019reviewofdancing pages 1-2)
2) Adult worms and host responses drive lymphatic dysfunction and remodeling; microfilariae facilitate ongoing transmission. (shaw2023lymphaticfilariasisendgame pages 1-2)
3) Progressive lymphatic impairment predisposes to chronic lymphedema and episodes of acute inflammation (ADL). (mackenzie2024managinglymphedemainduced pages 1-2, krishnasastry2024efficacyandsafety pages 1-2)

### 6.2 Immune and cellular mechanisms (selected evidence)
An experimental LF model showed *Brugia malayi* infection induces **lymphatic remodeling and impaired lymphatic drainage**, with lymphatic insufficiency dependent on **type 2 adaptive immunity**, **IL-4 receptor**, and recruitment of **CCR2+ monocytes** and **alternatively activated macrophages** with a pro-lymphangiogenic phenotype; tetracycline-class drugs improved lymphatic function and modulated these immune pathways. (furlongsilva2021tetracyclinesimproveexperimental pages 1-3)

**Suggested GO biological process terms (examples):** lymphangiogenesis; inflammatory response; regulation of macrophage polarization; T cell activation; cytokine-mediated signaling pathway.

**Suggested Cell Ontology (CL) terms (examples):** monocyte (CCR2+), macrophage (alternatively activated), T cell (CD4+), lymphatic endothelial cell.

### 6.3 *Wolbachia*-targeted mechanisms
Doxycycline is used as an anti-*Wolbachia* therapy strategy; large recent RCTs for lymphedema management evaluated adjunctive doxycycline on top of EPC and found EPC benefits, while doxycycline showed limited/no additional effect on lymphedema stage progression in Ghana and Kerala. (debrah2024adherencetohygiene pages 1-2, krishnasastry2024efficacyandsafety pages 1-2)

### 6.4 Advanced technologies and omics
The retrieved texts did not provide LF-specific single-cell/spatial multi-omics findings. However, LF transmission modeling and programmatic surveillance analytics are prominent “advanced methods” in the 2023–2024 literature (e.g., endgame modeling and stopping criteria). (shaw2023lymphaticfilariasisendgame pages 1-2, sharma2023evaluatingeliminationthresholds pages 1-2)

## 7. Anatomical structures affected
### 7.1 Primary organs/systems
**Lymphatic system** (lymphatic vessels and nodes) is the primary site of adult worm infection and pathology. (dietrich2019reviewofdancing pages 1-2, mackenzie2024managinglymphedemainduced pages 1-2)

### 7.2 Tissue/cell level
Key affected tissues include lymphatic endothelium and surrounding connective tissue, with inflammatory infiltrates (monocytes/macrophages, T cells) implicated in remodeling in experimental models. (furlongsilva2021tetracyclinesimproveexperimental pages 1-3)

**Suggested UBERON terms (examples):** lymphatic vessel, lymph node, lower limb, scrotum.

## 8. Temporal development (onset and progression)
LF programs operationalize time in terms of repeated annual MDA rounds and post-MDA surveillance windows.

* WHO pre-TAS framework described in modeling work: after ≥5 effective rounds (>65% coverage), evaluate if mf <1% and/or CFA <2%; then proceed to TAS in children to decide stopping MDA and monitor post-MDA transmission. (sharma2023evaluatingeliminationthresholds pages 1-2)
* In Tanzania field data, microfilariae cleared quickly after IA MDA (day 7), whereas antigenemia persisted at 6 months, highlighting temporal mismatch between infection indicators. (fimbo2024efficacyofivermectin pages 1-2)

## 9. Inheritance and population
### 9.1 Epidemiology and burden (recent quantitative data)
Key global program/burden indicators in recent sources:
* Freitas et al. (Published **2024-01-16**, PLOS NTDs; URL: https://doi.org/10.1371/journal.pntd.0011882) states: “Since 2000, more than **9 billion treatments** of antifilarial medicines have been distributed through MDA programmes in **72 endemic countries** and **17 countries have reached EPHP**. Yet in **2021, nearly 900 million people still required MDA** …” (freitas2024thelymphaticfilariasis pages 1-2)
* Fimbo et al. (Published **2024-06**, Infectious Diseases of Poverty; URL: https://doi.org/10.1186/s40249-024-01214-3) reports that in **2021 about 882 million people in 44 countries** lived in areas requiring preventive chemotherapy. (fimbo2024efficacyofivermectin pages 1-2)

Illustrative country examples (program surveillance):
* Zambia post-MDA pre-TAS (2021–2022): Wb antigen prevalence **0.14%** and mf **0.0%** across 79/80 districts after five rounds of DA MDA (with one district exception). (matapo2023lymphaticfilariasiselimination pages 1-2)
* Samoa persistence after one round IDA: antigen prevalence above a **1% threshold** in multiple PSUs and Mf positives present, indicating residual active infection years later. (mayfield2024ongoingtransmissionof pages 1-2)

### 9.2 Demographics and geography
The retrieved corpus includes Africa (Kenya, Tanzania, Zambia, Ghana), South Asia (India), and Pacific (Samoa) program and trial evidence. (fimbo2024efficacyofivermectin pages 1-2, khaemba2023comparativesafetysurveillance pages 1-2, mayfield2024ongoingtransmissionof pages 1-2, debrah2024adherencetohygiene pages 1-2, krishnasastry2024efficacyandsafety pages 1-2)

## 10. Diagnostics
### 10.1 Core diagnostic modalities (current practice)
* **Antigen detection** (circulating filarial antigen/CFA) using rapid tests such as the WHO-recommended Filariasis Test Strip (FTS) is central for mapping/monitoring and surveillance. (fimbo2024efficacyofivermectin pages 1-2, scott2024fieldlaboratorycomparison pages 5-7)
* **Microfilaria detection by microscopy** (blood slides) remains important, including for elimination thresholds and confirmatory testing. (fimbo2024efficacyofivermectin pages 1-2, sharma2023evaluatingeliminationthresholds pages 1-2)
* **Ultrasound** can visualize adult worms (“filarial dance sign”). (dietrich2019reviewofdancing pages 1-2)

### 10.2 Recent developments (2024): QFAT vs FTS
Two 2024 studies provide quantitative performance/operational evidence for the **STANDARD Q Filariasis Antigen Test (QFAT)** as an alternative to FTS.

**India field performance (Published 2024-09, PLOS NTDs; URL: https://doi.org/10.1371/journal.pntd.0012538):** In Karnataka, QFAT compared with FTS in 1,227 adults showed sensitivity **95.5%**, specificity **99.7%**, PPV **99.0%**, NPV **98.5%**, and near-perfect agreement (kappa **0.97**). Both tests were positive for all 68 mf-positive samples, and QFAT had fewer invalid tests and was operationally easier per technicians. (dinesh2024performancecharacteristicsof pages 1-2)

**Samoa field-laboratory comparison (Published 2024-08, PLOS NTDs; URL: https://doi.org/10.1371/journal.pntd.0012386):** Concordance between QFAT and FTS reached **98.5%** (kappa **0.96**) after excluding invalid/indeterminate results; all 40 Mf-positive samples were Ag-positive by both tests. QFAT required a smaller blood volume and was preferred for usability/readability, but showed more result changes on delayed re-reading (next day). (scott2024fieldlaboratorycomparison pages 7-8, scott2024fieldlaboratorycomparison pages 5-7)

### 10.3 Differential diagnosis
The retrieved evidence base did not provide a structured differential diagnosis list (e.g., podoconiosis, chronic venous insufficiency, heart/renal failure edema). However, LF lymphedema management papers emphasize that lymphedema can occur from diverse causes and that EPC-like care focuses on hygiene/infection prevention in affected limbs. (mackenzie2024managinglymphedemainduced pages 1-2, krishnasastry2024efficacyandsafety pages 1-2)

## 11. Outcome / prognosis
LF is primarily a chronic morbidity and disability condition rather than a high-mortality disease; burden is dominated by disability, stigma, and recurrent inflammatory episodes.

Programmatically, key “success” outcomes include reduction of mf prevalence below **1%** and antigenemia below operational thresholds used for TAS decisions and post-MDA surveillance. Modeling cautions that operational stopping thresholds may not reliably reflect transmission interruption across heterogeneous settings. (kura2024howdoesthe pages 1-2, sharma2023evaluatingeliminationthresholds pages 1-2)

## 12. Treatment
### 12.1 Pharmacotherapy for transmission interruption (MDA)
WHO/GPELF uses preventive chemotherapy (annual MDA) with regimens determined by co-endemicity:
* **IA (ivermectin + albendazole)** in onchocerciasis co-endemic areas (noting IDA restrictions where onchocerciasis/loiasis risks exist). (kura2024howdoesthe pages 1-2)
* **DA (diethylcarbamazine + albendazole)** elsewhere. (kura2024howdoesthe pages 1-2, sharma2023evaluatingeliminationthresholds pages 1-2)
* **IDA (ivermectin + diethylcarbamazine + albendazole)** recommended in eligible settings to accelerate elimination. (khaemba2023comparativesafetysurveillance pages 1-2, mayfield2024ongoingtransmissionof pages 1-2)

**Real-world effectiveness gap (Tanzania, 2024):** IA cleared microfilariae quickly (90% day-7 clearance among mf-positive follow-ups) but antigenemia persisted at 6 months (CFA clearance 12.6%), supporting concern that adult-worm/antigen clearance lags and may require alternative approaches. (fimbo2024efficacyofivermectin pages 1-2)

### 12.2 Pharmacovigilance and safety (IDA vs DA)
Kenya community safety surveillance (Published online **2023-08-08**, Drug Safety; URL: https://doi.org/10.1007/s40264-023-01338-9) found higher overall AE incidence with IDA than DA (27.3% vs 16.2%), but severe events were very rare and there were no serious life-threatening AEs; authors recommend integrating pharmacovigilance into MDA programs. (khaemba2023comparativesafetysurveillance pages 1-2)

### 12.3 Morbidity management and disability prevention (MMDP): EPC for lymphedema
A 2024 RCT and a 2024 field-experience report emphasize that EPC is beneficial and central to LF morbidity care.

**EPC components (direct quote):** The Kerala RCT abstract states “The WHO-recommended Essential Package of Care (EPC) consists of **skin hygiene, elevation of affected limbs, exercise, protective shoe ware, wound care, and supportive therapy for acute phases**.” (krishnasastry2024efficacyandsafety pages 1-2)

**EPC outcomes:** In the Kerala double-blind trial, adding 6 weeks of doxycycline did not improve outcomes versus placebo, but the study concludes: “Importantly, this rigorous trial confirmed that the EPC is of substantial benefit to lymphedema patients by **reducing acute ADL and improving their QOL and clinical condition**.” (krishnasastry2024efficacyandsafety pages 1-2)

**Ghana RCT (2018–2020, published 2024-10, AJTMH; URL: https://doi.org/10.4269/ajtmh.24-0313):** The abstract reports that doxycycline showed “no effect on LE stage progression,” while emphasizing “a strong benefit from adherence to a strict hygiene protocol,” with potential added benefit for preventing acute attacks. (debrah2024adherencetohygiene pages 1-2)

### 12.4 Pipeline / experimental therapeutics (2024)
**Anti-*Wolbachia* short-course combinations:** A 2024 preclinical study tested the anti-*Wolbachia* small molecule AWZ1066S with benzimidazoles (albendazole or oxfendazole) across multiple rodent filariasis models (including *Brugia* and *Litomosoides* models). Combinations produced >90% *Wolbachia* depletion in 5 days and achieved sterilizing/curative effects and transmission blockade in some models. (hegde2024combinationsofthe pages 1-2)

### 12.5 MAXO suggestions (treatments/actions; examples)
* Mass drug administration (preventive chemotherapy)
* Anthelmintic therapy (albendazole, ivermectin, diethylcarbamazine)
* Antibiotic therapy targeting *Wolbachia* (doxycycline; investigational anti-*Wolbachia*)
* Lymphedema hygiene and skin care
* Limb elevation/exercise therapy
* Hydrocelectomy (surgical correction)

## 13. Prevention
Primary prevention is achieved via **community-wide MDA** and vector-related measures; secondary/tertiary prevention includes surveillance (TAS/pre-TAS) and morbidity care.

Modeling highlights that elimination success depends on sustained high annual coverage and limiting the “never treated” proportion; e.g., in Anopheles settings with 10% baseline mf, annual 80% coverage with IA could reach the 1% mf threshold within 10 years if NT <10%. (kura2024howdoesthe pages 1-2)

## 14. Other species / natural disease
Filarial nematodes are important in both human and veterinary disease contexts (e.g., *Dirofilaria* in animals). In the retrieved evidence, the most relevant “other species” context is the use of non-human/rodent filariae for modeling LF biology and treatment development rather than naturally occurring LF disease in companion animals. (hegde2024combinationsofthe pages 1-2, lenz2024…onthe pages 28-32)

## 15. Model organisms and model systems (research and translational relevance)
Because human LF parasites are not viable in immunocompetent mice, rodent models are essential for mechanistic and drug-development work. (arndts2024differencesofin pages 1-2)

### 15.1 Key models
* **Litomosoides sigmodontis in BALB/c mice**: permits a complete life cycle including patent microfilaremia; infection dynamics differ by strain (BALB/c can develop microfilaremia; C57BL/6 typically clears earlier without microfilaremia). (lenz2024…onthe pages 28-32, arndts2024differencesofin pages 1-2)
* **Brugia malayi experimental limb lymphatics model (mouse)**: used to study lymphatic remodeling/immune mechanisms and to test antimorbidity interventions (e.g., tetracyclines). (furlongsilva2021tetracyclinesimproveexperimental pages 1-3)
* **Gerbil/jird models** for *Brugia* and *Litomosoides* are widely used for transmission biology and drug testing; AWZ1066S combination experiments leveraged multiple gerbil/*Brugia* models. (hegde2024combinationsofthe pages 1-2)

### 15.2 Applications and limitations
* Applications: immune mechanisms (type 2 immunity, macrophage polarization), lymphangiogenesis/lymphatic function, and preclinical screening of macrofilaricidal strategies. (furlongsilva2021tetracyclinesimproveexperimental pages 1-3, hegde2024combinationsofthe pages 1-2)
* Limitations: human filariae often require immunocompromised hosts; strain-specific differences in microfilaremia and immune responses must be considered when translating findings. (arndts2024differencesofin pages 1-2, lenz2024…onthe pages 28-32)

## Visual evidence: WHO EPC components
Figure evidence supporting EPC composition and its organization into urgent/essential/important/selective components is shown in the retrieved EPC figure. (mackenzie2024managinglymphedemainduced media bc4ce439)

## High-value quantitative snapshot (2023–2024 emphasis)
| Topic | Study/location | Design | Key numeric findings | Citations |
|---|---|---|---|---|
| Global LF program metrics | Freitas et al. 2024, global | Systematic review of LF treatment/MMDP studies | Since 2000, **>9 billion** antifilarial treatments distributed through MDA in **72 endemic countries**; **17 countries** had reached elimination as a public health problem (EPHP); in **2021 nearly 900 million people** still required MDA | (freitas2024thelymphaticfilariasis pages 1-2) |
| IA effectiveness after MDA | Fimbo et al. 2024, Mkinga district, Tanzania | Community-based prospective cohort after ivermectin + albendazole (IA) MDA | **4,115** screened; baseline **CFA positivity 5.8%** (239/4115); among CFA+ individuals, **11/239 (4.6%)** were mf+; day-7 mf clearance **90%** (9/10; 95% CI 59.6–98.2%); 6-month CFA clearance **12.6%** (23/183 became CFA−; 160/183, 87.4%, remained CFA+) | (fimbo2024efficacyofivermectin pages 1-2) |
| IDA vs DA safety | Khaemba et al. 2023, Kenya (Mombasa IDA; Kilifi DA) | Community-based observational cohort event-monitoring study during MDA | **20,421** eligible residents; ≥1 adverse event: **27.3%** with IDA vs **16.2%** with DA (p<0.0001); severe AEs were rare: **0.05%** IDA vs **0.03%** DA; most AEs mild/moderate; common AEs included dizziness **15.9% vs 5.9%** and drowsiness **10.1% vs 2.6%** | (khaemba2023comparativesafetysurveillance pages 1-2) |
| pre-TAS thresholds and post-MDA status | Matapo et al. 2023, Zambia | Post-MDA pre-transmission assessment survey after 5 effective annual DA rounds | WHO pre-TAS thresholds: **<2% antigenaemia** and **<1% microfilaraemia** after ≥5 effective MDA rounds; **47,235** tested (**47,052** valid); observed W. bancrofti Ag prevalence **0.14%** and mf prevalence **0.0%** across **79/80** districts; all districts below Ag threshold except **Chibombo** | (matapo2023lymphaticfilariasiselimination pages 1-2) |
| Persistence after one round of IDA | Mayfield et al. 2024, Samoa | Community surveys in 8 PSUs, 4.5 years after one round of triple-drug MDA | Ag-positive participants found in **6/8 PSUs**; Ag prevalence remained **significantly above the 1% threshold in 4/8 PSUs**; mf-positive participants detected in **5/8 PSUs**, confirming residual active infection | (mayfield2024ongoingtransmissionof pages 1-2) |
| Never-treated proportion and elimination feasibility | Kura et al. 2024, modelled Anopheles/Culex settings | Individual-based stochastic transmission modelling | For **Anopheles** settings with baseline mf **10%**, annual **80%** eligible coverage with IA could reach **1% mf threshold within 10 years** if never-treated (NT) proportion **<10%**; for **Culex** settings with baseline mf **5%**, DA or IDA could achieve elimination if eligible coverage **≥80%**; with baseline mf **10%**, target achievable when annual coverage **80%** and **NT ≤15%** | (kura2024howdoesthe pages 1-2) |


*Table: This table summarizes high-value lymphatic filariasis program metrics and selected recent field and modelling results relevant to elimination, treatment effectiveness, and safety. It is useful as a compact evidence snapshot for knowledge-base population and comparative interpretation.*

## Expert opinions and authoritative analyses (from recent authoritative sources)
* A 2024 systematic review argues that despite extensive MDA distribution, “there remain gaps in understanding of variation in responses to treatment” and proposes an individual participant data (IPD) platform to address unresolved questions. (freitas2024thelymphaticfilariasis pages 1-2)
* 2023 modeling cautions that operational TAS stopping criteria may undermine elimination if parasite extinction dynamics and site-to-site variation are not adequately considered. (sharma2023evaluatingeliminationthresholds pages 1-2)
* 2024 Samoa field evidence supports WHO guidance that multiple rounds of triple-drug MDA are needed, and that delays between rounds can lead to resurgence/persistence. (mayfield2024ongoingtransmissionof pages 1-2)

## Evidence gaps in this tool run (important for knowledge-base completeness)
* Standard identifiers (ICD-10/11, MeSH, MONDO, Orphanet, OMIM) were not present in the retrieved full texts and should be populated via ontology lookups outside this corpus.
* Host genetic susceptibility/protective variants and gene–environment interactions were not identified in the retrieved evidence.
* Comprehensive phenotype frequency estimates (e.g., percent with hydrocele/lymphedema among infected) were not extracted from the available texts.

## Key cited sources (with URLs and publication dates from retrieved texts)
* Freitas LT et al. **2024-01-16**. PLOS Neglected Tropical Diseases. https://doi.org/10.1371/journal.pntd.0011882 (freitas2024thelymphaticfilariasis pages 1-2)
* Fimbo AM et al. **2024-06**. Infectious Diseases of Poverty. https://doi.org/10.1186/s40249-024-01214-3 (fimbo2024efficacyofivermectin pages 1-2)
* Khaemba C et al. **2023-08-08 (online)**. Drug Safety. https://doi.org/10.1007/s40264-023-01338-9 (khaemba2023comparativesafetysurveillance pages 1-2)
* Mayfield HJ et al. **2024-06-27**. PLOS Neglected Tropical Diseases. https://doi.org/10.1371/journal.pntd.0012236 (mayfield2024ongoingtransmissionof pages 1-2)
* Kura K et al. **2024-04**. Clinical Infectious Diseases (Suppl). https://doi.org/10.1093/cid/ciae021 (kura2024howdoesthe pages 1-2)
* Sharma S et al. **2023-02**. Communications Biology. https://doi.org/10.1038/s42003-022-04391-9 (sharma2023evaluatingeliminationthresholds pages 1-2)
* Scott JL et al. **2024-08**. PLOS Neglected Tropical Diseases. https://doi.org/10.1371/journal.pntd.0012386 (scott2024fieldlaboratorycomparison pages 7-8, scott2024fieldlaboratorycomparison pages 5-7)
* Dinesh RJ et al. **2024-09**. PLOS Neglected Tropical Diseases. https://doi.org/10.1371/journal.pntd.0012538 (dinesh2024performancecharacteristicsof pages 1-2)
* Mackenzie CD et al. **2024-07**. American Journal of Tropical Medicine and Hygiene. https://doi.org/10.4269/ajtmh.23-0905 (mackenzie2024managinglymphedemainduced pages 1-2, mackenzie2024managinglymphedemainduced media bc4ce439)
* Debrah LB et al. **2024-10**. American Journal of Tropical Medicine and Hygiene. https://doi.org/10.4269/ajtmh.24-0313 (debrah2024adherencetohygiene pages 1-2)
* Krishnasastry S et al. **2024-10**. American Journal of Tropical Medicine and Hygiene. https://doi.org/10.4269/ajtmh.24-0337 (krishnasastry2024efficacyandsafety pages 1-2)
* Hegde S et al. **2024-02**. Frontiers in Microbiology. https://doi.org/10.3389/fmicb.2024.1346068 (hegde2024combinationsofthe pages 1-2)


References

1. (dietrich2019reviewofdancing pages 1-2): Christoph F. Dietrich, Nitin Chaubal, Achim Hoerauf, Kerstin Kling, Markus Schindler Piontek, Ludwig Steffgen, Sabine Mand, and Yi Dong. Review of dancing parasites in lymphatic filariasis. Ultrasound International Open, 5:E65-E74, Mar 2019. URL: https://doi.org/10.1055/a-0918-3678, doi:10.1055/a-0918-3678. This article has 47 citations.

2. (kura2024howdoesthe pages 1-2): Klodeta Kura, Wilma A Stolk, Maria-Gloria Basáñez, Benjamin S Collyer, Sake J de Vlas, Peter J Diggle, Katherine Gass, Matthew Graham, T Déirdre Hollingsworth, Jonathan D King, Alison Krentel, Roy M Anderson, and Luc E Coffeng. How does the proportion of never treatment influence the success of mass drug administration programs for the elimination of lymphatic filariasis? Clinical Infectious Diseases, 78:S93-S100, Apr 2024. URL: https://doi.org/10.1093/cid/ciae021, doi:10.1093/cid/ciae021. This article has 14 citations and is from a highest quality peer-reviewed journal.

3. (khaemba2023comparativesafetysurveillance pages 1-2): Christabel Khaemba, Abbie Barry, Wyckliff P. Omondi, Elvis Kirui, Margaret Oluka, Gurumurthy Parthasarathi, Sammy M. Njenga, Anastacia Guantai, and Eleni Aklillu. Comparative safety surveillance of triple (ida) versus dual therapy (da) in mass drug administration for elimination of lymphatic filariasis in kenya: a cohort event monitoring study. Drug Safety, 46:961-974, Aug 2023. URL: https://doi.org/10.1007/s40264-023-01338-9, doi:10.1007/s40264-023-01338-9. This article has 7 citations and is from a peer-reviewed journal.

4. (mackenzie2024managinglymphedemainduced pages 1-2): Charles D. Mackenzie, D Ramaiah Kapa, Suma Krishnasastry, Jan Douglass, Achim Hoerauf, and Eric A. Ottesen. Managing lymphedema induced by lymphatic filariasis: implementing and improving care at the individual and programmatic levels. The American Journal of Tropical Medicine and Hygiene, 111:3-21, Jul 2024. URL: https://doi.org/10.4269/ajtmh.23-0905, doi:10.4269/ajtmh.23-0905. This article has 18 citations.

5. (freitas2024thelymphaticfilariasis pages 1-2): Luzia T. Freitas, Mashroor Ahmad Khan, Azhar Uddin, Julia B. Halder, Sauman Singh-Phulgenda, Jeyapal Dinesh Raja, Vijayakumar Balakrishnan, Eli Harriss, Manju Rahi, Matthew Brack, Philippe J. Guérin, Maria-Gloria Basáñez, Ashwani Kumar, Martin Walker, and Adinarayanan Srividya. The lymphatic filariasis treatment study landscape: a systematic review of study characteristics and the case for an individual participant data platform. PLOS Neglected Tropical Diseases, 18:e0011882, Jan 2024. URL: https://doi.org/10.1371/journal.pntd.0011882, doi:10.1371/journal.pntd.0011882. This article has 13 citations and is from a domain leading peer-reviewed journal.

6. (sharma2023evaluatingeliminationthresholds pages 1-2): Swarnali Sharma, Morgan E. Smith, Shakir Bilal, and Edwin Michael. Evaluating elimination thresholds and stopping criteria for interventions against the vector-borne macroparasitic disease, lymphatic filariasis, using mathematical modelling. Communications Biology, Feb 2023. URL: https://doi.org/10.1038/s42003-022-04391-9, doi:10.1038/s42003-022-04391-9. This article has 15 citations and is from a peer-reviewed journal.

7. (debrah2024adherencetohygiene pages 1-2): Linda Batsa Debrah, Ute Klarmann-Schulz, Jubin Osei-Mensah, Janina M. Kuehlwein, Yusif Mubarik, Jennifer Nadal, Nana Kwame Ayisi-Boateng, Arcangelo Ricchiuto, Vera Serwaa Opoku, Sarah M. Sullivan, Derrick Adu Mensah, John Horton, Abu Abudu Rahamani, Philip J. Budge, Stephen Gbedema, Patricia Jebett Korir, John Opoku, Kenneth Pfarr, Derrick Boateng Kontoh, Angelika Kellings, Charles Gyasi, Michael Agyemang Obeng, Barbara Gruetzmacher, Fatima Amponsah Fordjour, Inge Kroidl, Sacha Horn, Eunice Kyaakyile Kuutiero, Caroline Wauschkuhn, Abdallah Ngenya, Charles Mackenzie, Samuel Wanji, Akili Kalinga, Eric A. Ottesen, Achim Hoerauf, and Alexander Yaw Debrah. Adherence to hygiene protocols and doxycycline therapy in ameliorating lymphatic filariasis morbidity in an endemic area post-interruption of disease transmission in ghana. The American Journal of Tropical Medicine and Hygiene, 111:66-82, Oct 2024. URL: https://doi.org/10.4269/ajtmh.24-0313, doi:10.4269/ajtmh.24-0313. This article has 10 citations.

8. (krishnasastry2024efficacyandsafety pages 1-2): Suma Krishnasastry, Anuja Ashok, Ammu Devidas, Sarah Sullivan, Mariana Stephens, Jayla Norman, Elianna Paljug, Andrew Deathe, Andrew Majewski, John Horton, Joseph P. Shott, Ute Klarmann-Schultz, Achim Hoerauf, Eric Ottesen, and Charles D. Mackenzie. Efficacy and safety of adding 6 weeks of doxycycline to the essential package of care to treat filarial lymphedema: a double-blind, randomized, controlled trial in southern india. The American Journal of Tropical Medicine and Hygiene, 111:83-93, Oct 2024. URL: https://doi.org/10.4269/ajtmh.24-0337, doi:10.4269/ajtmh.24-0337. This article has 7 citations.

9. (shaw2023lymphaticfilariasisendgame pages 1-2): Callum Shaw, Angus McLure, Patricia M. Graves, Colleen L. Lau, and Kathryn Glass. Lymphatic filariasis endgame strategies: using geofil to model mass drug administration and targeted surveillance and treatment strategies in american samoa. PLOS Neglected Tropical Diseases, 17:e0011347, May 2023. URL: https://doi.org/10.1371/journal.pntd.0011347, doi:10.1371/journal.pntd.0011347. This article has 8 citations and is from a domain leading peer-reviewed journal.

10. (hegde2024combinationsofthe pages 1-2): Shrilakshmi Hegde, Amy E. Marriott, Nicolas Pionnier, Andrew Steven, Christina Bulman, Emma Gunderson, Ian Vogel, Marianne Koschel, Alexandra Ehrens, Sara Lustigman, Denis Voronin, Nancy Tricoche, Achim Hoerauf, Marc P. Hübner, Judy Sakanari, Ghaith Aljayyoussi, Fabian Gusovsky, Jessica Dagley, David W. Hong, Paul O'Neill, Steven A. Ward, Mark J. Taylor, and Joseph D. Turner. Combinations of the azaquinazoline anti-wolbachia agent, awz1066s, with benzimidazole anthelmintics synergise to mediate sub-seven-day sterilising and curative efficacies in experimental models of filariasis. Frontiers in Microbiology, Feb 2024. URL: https://doi.org/10.3389/fmicb.2024.1346068, doi:10.3389/fmicb.2024.1346068. This article has 9 citations and is from a peer-reviewed journal.

11. (mayfield2024ongoingtransmissionof pages 1-2): Helen J. Mayfield, Benn Sartorius, Sarah Sheridan, Maddison Howlett, Beatris Mario Martin, Robert Thomsen, Rossana Tofaeono-Pifeleti, Satupaitea Viali, Patricia M. Graves, and Colleen L. Lau. Ongoing transmission of lymphatic filariasis in samoa 4.5 years after one round of triple-drug mass drug administration. PLOS Neglected Tropical Diseases, 18:e0012236, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012236, doi:10.1371/journal.pntd.0012236. This article has 13 citations and is from a domain leading peer-reviewed journal.

12. (fimbo2024efficacyofivermectin pages 1-2): Adam M. Fimbo, Rajabu Hussein Mnkugwe, Eulambius Mathias Mlugu, Peter P. Kunambi, Alpha Malishee, Omary M.S. Minzi, Appolinary A. R. Kamuhabwa, and Eleni Aklillu. Efficacy of ivermectin and albendazole combination in suppressing transmission of lymphatic filariasis following mass administration in tanzania: a prospective cohort study. Infectious Diseases of Poverty, Jun 2024. URL: https://doi.org/10.1186/s40249-024-01214-3, doi:10.1186/s40249-024-01214-3. This article has 7 citations and is from a domain leading peer-reviewed journal.

13. (furlongsilva2021tetracyclinesimproveexperimental pages 1-3): Julio Furlong-Silva, Stephen D. Cross, Amy E. Marriott, Nicolas Pionnier, John Archer, Andrew Steven, Stefan Schulte Merker, Matthias Mack, Young-Kwon Hong, Mark J. Taylor, and Joseph D. Turner. Tetracyclines improve experimental lymphatic filariasis pathology by disrupting interleukin-4 receptor–mediated lymphangiogenesis. Journal of Clinical Investigation, Mar 2021. URL: https://doi.org/10.1172/jci140853, doi:10.1172/jci140853. This article has 39 citations and is from a highest quality peer-reviewed journal.

14. (matapo2023lymphaticfilariasiselimination pages 1-2): Belem Blamwell Matapo, Evans Mwila Mpabalwani, Patrick Kaonga, Martin Chitolongo Simuunza, Nathan Bakyaita, Freddie Masaninga, Namasiku Siyumbwa, Seter Siziya, Frank Shamilimo, Chilweza Muzongwe, Enala T. Mwase, and Chummy Sikalizyo Sikasunge. Lymphatic filariasis elimination status: wuchereria bancrofti infections in human populations after five effective rounds of mass drug administration in zambia. Tropical Medicine and Infectious Disease, 8:333, Jun 2023. URL: https://doi.org/10.3390/tropicalmed8070333, doi:10.3390/tropicalmed8070333. This article has 8 citations.

15. (scott2024fieldlaboratorycomparison pages 5-7): Jessica L. Scott, Helen J. Mayfield, Jane E. Sinclair, Beatris Mario Martin, Maddison Howlett, Ramona Muttucumaru, Kimberly Y. Won, Robert Thomsen, Satupaitea Viali, Rossana Tofaeono-Pifeleti, Patricia M. Graves, and Colleen L. Lau. Field laboratory comparison of standard q filariasis antigen test (qfat) with bioline filariasis test strip (fts) for the detection of lymphatic filariasis in samoa, 2023. PLOS Neglected Tropical Diseases, 18:e0012386, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012386, doi:10.1371/journal.pntd.0012386. This article has 10 citations and is from a domain leading peer-reviewed journal.

16. (dinesh2024performancecharacteristicsof pages 1-2): Raja Jeyapal Dinesh, Kaliannagounder Krishnamoorthy, Rajendran Dhanalakshmi, Priskilla Johnson Jency, Palappurath Maliyakkal Azad, Sugeerappa Laxmanappa Hoti, and Ashwani Kumar. Performance characteristics of standard q filariasis antigen test (qfat) to detect filarial antigens of wuchereria bancrofti in the field. PLOS Neglected Tropical Diseases, 18:e0012538, Sep 2024. URL: https://doi.org/10.1371/journal.pntd.0012538, doi:10.1371/journal.pntd.0012538. This article has 10 citations and is from a domain leading peer-reviewed journal.

17. (scott2024fieldlaboratorycomparison pages 7-8): Jessica L. Scott, Helen J. Mayfield, Jane E. Sinclair, Beatris Mario Martin, Maddison Howlett, Ramona Muttucumaru, Kimberly Y. Won, Robert Thomsen, Satupaitea Viali, Rossana Tofaeono-Pifeleti, Patricia M. Graves, and Colleen L. Lau. Field laboratory comparison of standard q filariasis antigen test (qfat) with bioline filariasis test strip (fts) for the detection of lymphatic filariasis in samoa, 2023. PLOS Neglected Tropical Diseases, 18:e0012386, Aug 2024. URL: https://doi.org/10.1371/journal.pntd.0012386, doi:10.1371/journal.pntd.0012386. This article has 10 citations and is from a domain leading peer-reviewed journal.

18. (lenz2024…onthe pages 28-32): B Lenz. … on the metabolic and immunological profile and characterization of filariae-induced tropical pulmonary eosinophilia using a newly established mouse model. Unknown journal, 2024.

19. (arndts2024differencesofin pages 1-2): Kathrin Arndts, Anna Wiszniewsky, Anna-Lena Neumann, Katharina Wiszniewsky, Gnatoulma Katawa, Achim Hoerauf, Laura E. Layland-Heni, Manuel Ritter, and Marc P. Hübner. Differences of in vitro immune responses between patent and pre-patent litomosoides sigmodontis–infected mice are independent of the filarial antigenic stimulus used. Parasitology Research, Oct 2024. URL: https://doi.org/10.1007/s00436-024-08365-0, doi:10.1007/s00436-024-08365-0. This article has 0 citations and is from a peer-reviewed journal.

20. (mackenzie2024managinglymphedemainduced media bc4ce439): Charles D. Mackenzie, D Ramaiah Kapa, Suma Krishnasastry, Jan Douglass, Achim Hoerauf, and Eric A. Ottesen. Managing lymphedema induced by lymphatic filariasis: implementing and improving care at the individual and programmatic levels. The American Journal of Tropical Medicine and Hygiene, 111:3-21, Jul 2024. URL: https://doi.org/10.4269/ajtmh.23-0905, doi:10.4269/ajtmh.23-0905. This article has 18 citations.

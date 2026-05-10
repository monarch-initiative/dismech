---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T00:36:13.397142'
end_time: '2026-05-10T00:56:22.813469'
duration_seconds: 1209.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Melanoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 56
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metastatic Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Melanoma** covering all of the
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
- **Disease Name:** Metastatic Melanoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Melanoma** covering all of the
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


## Comprehensive Research Report: Metastatic Melanoma (2023–2024 prioritized)

### Target Disease
- **Disease name:** Metastatic melanoma
- **Ontology/IDs (available from retrieved sources)**
  - **Open Targets/EFO disease ID:** **EFO_0002617** (“metastatic melanoma”) (OpenTargets Search: metastatic melanoma)
  - **ICD-10(-GM) codes used in real-world studies:** primary melanoma **C43**; locoregional metastasis **C77** (mapped to UICC/AJCC stage III); distant metastasis **C78/C79** (mapped to UICC/AJCC stage IV) (datzmann2021implementationandeffectiveness pages 2-3)
  - **MONDO / MeSH / ICD-11:** Not retrieved in the current tool context; therefore, not asserted here.
- **Category:** malignant neoplasm; advanced/metastatic solid tumor.
- **Common synonyms/alternate names:** advanced melanoma; unresectable stage III melanoma; stage IV melanoma; metastatic malignant melanoma; melanoma with distant metastasis (contextual usage in sources) (kattenhøj2024efficacyofipilimumab pages 1-2, datzmann2021implementationandeffectiveness pages 2-3).
- **Evidence provenance:** This report integrates aggregated evidence from peer‑reviewed reviews, registry/real‑world cohorts, global burden analyses, and clinical trial registry records (jalil2024exploringresistanceto pages 1-3, liu2024globalregionaland pages 1-2, kattenhøj2024efficacyofipilimumab pages 1-2, NCT05727904 chunk 1).

---

## 1. Disease Information (definition and current understanding)

**Definition/overview.** Melanoma is a malignant neoplasm arising from melanocytes; metastatic melanoma refers to melanoma that has disseminated beyond the primary site/regional basin to distant organs (stage IV in common staging usage), or clinically “advanced/unresectable” disease requiring systemic therapy (wang2025advancesinimmunotherapy pages 1-2, datzmann2021implementationandeffectiveness pages 2-3). Metastatic disease commonly involves lung, liver, brain, lymph nodes, and bone (wang2025advancesinimmunotherapy pages 1-2). Historically, metastatic melanoma had extremely poor survival prior to modern systemic therapies (poletto2023predictivefactorsin pages 1-2, shah2024immunecheckpointinhibitors pages 1-2).

**Key concept: treatment eras.** Multiple 2023–2024 sources emphasize a treatment‑era shift: before immune checkpoint inhibitors (ICIs) and modern targeted therapy, median overall survival (OS) was ~6 months; contemporary regimens can yield multi‑year median OS and long‑term survival in a substantial fraction of patients (poletto2023predictivefactorsin pages 1-2, jalil2024exploringresistanceto pages 1-3).

**Direct abstract quotes supporting key concepts (examples).**
- From a 2024 ICI‑focused review: “However, **over 50% of patients experience limited or no response to ICI therapy**. Resistance to ICIs is influenced by a complex interplay of tumour intrinsic and extrinsic factors.” (Hossain et al., 2024; https://doi.org/10.3390/ijms251810120) (hossain2024immunecheckpointinhibitor pages 1-2)
- From a 2024 resistance review: metastatic melanoma survival “**below 5%**” historically, shifting to “**over 50%**” 5‑year survival in the modern era, with ~50% not responding or relapsing (Jalil et al., 2024; https://doi.org/10.20517/cdr.2024.54) (jalil2024exploringresistanceto pages 1-3)

---

## 2. Etiology

### 2.1 Disease causal factors (mechanistic and environmental)
**UV radiation as dominant environmental carcinogen.** Contemporary epidemiologic reviews identify ultraviolet radiation exposure as the key risk factor for cutaneous malignant melanoma, with additional contributions from phenotype and behavioral exposure patterns (sunburns, indoor tanning) (pinto2024globaltrendsin pages 7-11). Mechanistically, UV can generate DNA damage (e.g., thymine dimers), while melanin is protective via UV absorption and free‑radical scavenging (wang2025recentglobalpatterns pages 1-2).

### 2.2 Risk factors (genetic and environmental)
**Environmental/host risk factors (population literature).** Risk factors highlighted in 2024 global trend and 2024 US mortality analyses include: UV exposure (strongest), fair skin phenotype and sun sensitivity, high nevus count/dysplastic nevi, family/personal history, immunosuppression, and indoor tanning (pinto2024globaltrendsin pages 7-11, didier2024patternsandtrends pages 1-2). Ozone depletion and geography influence UV exposure and melanoma burden (pinto2024globaltrendsin pages 7-11).

**Genetic susceptibility / molecular predisposition (tumor drivers).** Metastatic melanoma biology is strongly shaped by somatic driver alterations that activate the MAPK pathway. Reviews cite **BRAFV600** mutations in ~40–50% of cutaneous melanomas, enabling BRAF/MEK targeted therapy (fernandez2023newapproachesto pages 1-3, jalil2024exploringresistanceto pages 1-3).

### 2.3 Protective factors
**Protective pigmentation context.** Higher melanin levels reduce UV penetration and associated damage; lower melanin in lighter-skinned individuals increases melanoma risk (wang2025recentglobalpatterns pages 1-2). (Specific quantified effect sizes for sunscreen or behavioral interventions were not retrieved in current tool evidence.)

### 2.4 Gene–environment interactions
The retrieved evidence supports a conceptual model in which **UV exposure induces DNA damage** and **mutational/neoantigen landscapes** that influence immune recognition and response to immunotherapy (high mutational burden is repeatedly discussed as a predictor of ICI response), linking environmental carcinogenesis to immunotherapy sensitivity (kato2026drugtherapyfor pages 3-4, roccuzzo2024prognosticbiomarkersin pages 3-4). (Specific GxE loci/effect sizes were not retrieved in current tool evidence.)

---

## 3. Phenotypes (clinical presentation and metastatic patterns)

### 3.1 Core metastatic phenotypes and clinical manifestations
**Metastatic dissemination sites.** Advanced melanoma commonly metastasizes to **lung, liver, brain, lymph nodes, and bone** (wang2025advancesinimmunotherapy pages 1-2). Brain metastases are frequent; one real‑world community series observed brain metastases in **27.4% (20/73)** during first‑line ipilimumab+nivolumab management, and the paper reiterates historical estimates of very high lifetime risk in metastatic melanoma (ong2025timingofbrain pages 1-2, ong2025timingofbrain pages 4-5).

**Treatment-related phenotypes (immune-related toxicities).** Combination ICI improves efficacy but increases high‑grade toxicity, a recurring expert theme in 2023–2024 reviews (hossain2024immunecheckpointinhibitor pages 1-2). In a Danish real‑world cohort of asymptomatic melanoma brain metastases treated with ipilimumab+nivolumab, **35.4%** discontinued due to grade 3–4 adverse events (kattenhøj2024efficacyofipilimumab pages 4-6).

### 3.2 Phenotype ontology suggestions (HPO)
Because phenotype frequency tables were not retrieved from dedicated phenotype resources (HPO/Orphanet/OMIM) in the tool context, the following HPO term suggestions are **plausible mappings** for knowledge‑base structuring (not asserted as comprehensive):
- **Brain metastasis:** *Metastatic neoplasm* (HP:0030972) + site qualifiers; consider custom mapping to “brain metastasis” if available in HPO extensions.
- **Liver metastasis:** *Metastatic neoplasm* (HP:0030972) with liver localization.
- **Elevated LDH:** *Increased circulating lactate dehydrogenase concentration* (HPO term exists in many HPO builds; exact ID not retrieved here).
- **Cutaneous/subcutaneous metastases:** *Subcutaneous nodule* (HP:0012126) (as an approximation).

(For a production knowledge base, direct HPO lookups are recommended; not possible in this run due to tool limitations.)

---

## 4. Genetic / Molecular Information

### 4.1 Key causal/driver genes (somatic; actionable in practice)
**MAPK pathway driver alterations.** Reviews consistently emphasize MAPK pathway activation as central. Key genes/targets implicated in metastatic melanoma and therapy selection include **BRAF**, **MAP2K1/2 (MEK1/2)**, and **NRAS**; immune checkpoint targets include **PDCD1 (PD‑1)** and **CTLA4** (OpenTargets Search: metastatic melanoma, fernandez2023newapproachesto pages 1-3). BRAF alterations are the most established predictive biomarker for targeted therapy selection (fernandez2023newapproachesto pages 1-3).

### 4.2 Pathogenic variants / variant classes (summary)
- **BRAF V600 (e.g., V600E/K) activating substitutions**: common actionable somatic driver; supports BRAF inhibitor + MEK inhibitor combinations (fernandez2023newapproachesto pages 1-3, fateeva2024currentstateof pages 5-6).
- **NF1 loss / PTEN inactivation**: associated with pathway rewiring and resistance mechanisms (MAPK reactivation, PI3K–AKT activation), discussed as contributors to therapy resistance (kolathur2024molecularsusceptibilityand pages 13-15).

(Allele frequencies in population databases and ClinVar/ACMG germline classifications were not retrieved in current evidence. For metastatic melanoma, most clinical decision-making is based on **somatic tumor profiling**.)

### 4.3 Biomarkers (tumor and circulating)
**Tumor mutational burden (TMB), PD‑L1, and IFN‑γ signatures.** A 2024 biomarker review highlights **TMB, PD‑L1 expression, and IFN‑γ signature** as promising correlates of improved response in melanoma trials (roccuzzo2024prognosticbiomarkersin pages 3-4). Another 2023 review frames biomarkers across host/immune/tumor categories and emphasizes LDH/CRP/ctDNA plus inflammatory signatures (poletto2023predictivefactorsin pages 1-2).

**Circulating tumor DNA (ctDNA).** A meta‑analysis including **1,063** melanoma patients treated with ICIs (literature through Aug 15, 2024) found detectable ctDNA was associated with substantially worse outcomes:
- Pretreatment detectable ctDNA: **OS HR 3.19**; **PFS HR 2.08**.
- On‑treatment detectable ctDNA: **OS HR 4.57**; **PFS HR 3.79**. (liu2025theprognosticvalue pages 1-2)

---

## 5. Mechanism / Pathophysiology

### 5.1 Causal chains (from initiating factors to metastatic disease)
1) **UV exposure / DNA damage → mutational accumulation → oncogenic signaling activation** (MAPK pathway via BRAF/NRAS/NF1 alterations) → melanocyte transformation and tumor progression (wang2025recentglobalpatterns pages 1-2, fernandez2023newapproachesto pages 1-3).
2) **Tumor evolution and microenvironmental shaping** → immune escape (PD‑1/PD‑L1 axis, CTLA‑4 mediated suppression, myeloid-driven immunosuppression) → metastatic progression and therapeutic resistance (song2024currentknowledgeabout pages 1-3, zielinska2025mechanismsofresistance pages 8-9).

### 5.2 Major pathways and processes
**MAPK pathway (RAS–RAF–MEK–ERK).** Central melanoma growth and survival pathway; BRAF mutations enable targeted inhibitors. Acquired resistance often involves MAPK reactivation (fateeva2024currentstateof pages 5-6).

**PI3K–AKT pathway bypass and crosstalk.** Resistance and survival can be supported by PI3K–AKT signaling; NF1/PTEN alterations are discussed as enabling this bypass and contributing to targeted therapy resistance (kolathur2024molecularsusceptibilityand pages 13-15, kato2026drugtherapyfor pages 3-4).

**Immune evasion and TME suppression.** Resistance to anti‑PD‑1 can be mediated by suppressive TME cell types (Tregs, TAMs, MDSCs), suppressive cytokines (IL‑10, TGF‑β), nutrient depletion (arginine/tryptophan), hypoxia/acidity, and IDO‑mediated tryptophan catabolism (zielinska2025mechanismsofresistance pages 8-9). Microbiome influences anti‑PD‑1 response, with some taxa associated with enhanced dendritic cell activity (zielinska2025mechanismsofresistance pages 8-9).

**Visual evidence (treatment landscape and resistance).** Fateeva et al. (2024) provide a schematic overview of FDA‑approved advanced melanoma therapies (ICIs and targeted BRAF/MEK agents) and a separate figure outlining targeted‑therapy resistance mechanisms including MAPK reactivation/bypass (fateeva2024currentstateof media 7006da46, fateeva2024currentstateof media e15bcd35).

### 5.3 Ontology suggestions
- **GO biological process (examples):** MAPK cascade; regulation of T cell activation; antigen processing and presentation; interferon‑gamma signaling; leukocyte chemotaxis; epithelial–mesenchymal transition-like programs / dedifferentiation (the latter is discussed conceptually in resistance literature but not quantified in extracted evidence).
- **CL cell types (examples):** CD8+ T cell; regulatory T cell; tumor-associated macrophage; myeloid-derived suppressor cell; dendritic cell.

---

## 6. Anatomical Structures Affected

**Organ-level metastatic targets.** Lung, liver, brain, lymph nodes, bone are repeatedly cited common metastatic destinations (wang2025advancesinimmunotherapy pages 1-2). Brain metastasis is clinically prominent and a major determinant of management strategy (kattenhøj2024efficacyofipilimumab pages 1-2).

**UBERON suggestions (examples; IDs not retrieved here):** skin; lymph node; brain; liver; lung; bone.

---

## 7. Temporal Development (onset and progression)

**Staging concept.** Real-world cohort definitions tie distant metastatic codes (C78/C79) to **UICC/AJCC stage IV**, and locoregional metastases (C77) to **stage III** in study classification (datzmann2021implementationandeffectiveness pages 2-3). Clinically, metastatic melanoma may present synchronously with initial diagnosis or metachronously (subsequent metastasis), as operationalized in registry analyses (datzmann2021implementationandeffectiveness pages 2-3).

**Brain metastasis timing.** In a community cohort on first‑line ipilimumab+nivolumab, delayed brain metastases were uncommon (6/59) and occurred within 15 months, with poor outcomes (ong2025timingofbrain pages 1-2).

---

## 8. Inheritance and Population (epidemiology)

### 8.1 Global burden statistics (recent)
- **GLOBOCAN 2022:** **331,722** new melanoma cases and **~58,667** deaths globally; incidence highest in Oceania/North America/Europe (wang2025recentglobalpatterns pages 1-2).
- **GBD 2021 melanoma prevalence trend:** global cutaneous malignant melanoma prevalence **833,215** (2021), a **161.3% increase since 1990**; ASPR **25.37/100,000**; ASMR **0.73/100,000**; DALYs **1,678,836** (liu2024globalregionaland pages 1-2).

### 8.2 US mortality trends (population disparities)
US CDC WONDER analysis (1999–2020): **184,416** melanoma deaths; age‑adjusted mortality declined from **2.7 to 2.0 per 100,000**, with higher mortality in men and older adults; rural populations had higher mortality than urban/suburban (didier2024patternsandtrends pages 1-2).

---

## 9. Diagnostics

**Standard-of-care diagnosis (high-level).** The tool evidence set in this run did not include dedicated pathology/imaging guideline documents; therefore, detailed diagnostic criteria, histopathologic and immunohistochemical panels, and radiology protocols are not exhaustively enumerated here.

**Real-world implementation signal (testing/monitoring).** Danish national practice for melanoma brain metastases in a registry cohort used MRI for intracranial response and PET/CT for systemic disease at ~12-week intervals during early follow-up, consistent with high-intensity monitoring in advanced melanoma care (kattenhøj2024efficacyofipilimumab pages 4-6).

**Biomarker testing.** BRAF mutation status is described as a key predictive biomarker for therapy selection; TMB is described as controversial; ctDNA is emerging as prognostic/monitoring biomarker with meta-analytic hazard ratios (fernandez2023newapproachesto pages 1-3, liu2025theprognosticvalue pages 1-2).

---

## 10. Outcome / Prognosis

### 10.1 Survival improvement with modern systemic therapy
A 2023 review summarizes historical and modern outcomes:
- Pre‑modern era: metastatic melanoma median OS ~6 months (poletto2023predictivefactorsin pages 1-2).
- Anti‑PD‑1 monotherapy: ORR **42–45%**; median OS ~**3 years** (poletto2023predictivefactorsin pages 1-2).
- Nivolumab + ipilimumab: ORR **58%**; median OS **72.1 months** (poletto2023predictivefactorsin pages 1-2).
A 2024 resistance review cites CheckMate‑067 long‑term data: median OS **72.1 months** and 6.5‑year survival **56%** (jalil2024exploringresistanceto pages 1-3).

### 10.2 Prognostic biomarkers (recent quantitative examples)
**LDH risk stratification.** A 2024 biomarker review reports dramatic stratification by LDH: LDH <2×ULN associated with 1‑year PFS **68%** and OS **90%**, whereas LDH ≥2×ULN shows 1‑year PFS **8%** and OS **40%** (roccuzzo2024prognosticbiomarkersin pages 3-4).

**ctDNA hazard ratios.** Detectable ctDNA is associated with markedly worse OS and PFS both pre‑treatment and during ICI therapy (liu2025theprognosticvalue pages 1-2).

---

## 11. Treatment (current applications, real-world implementation, and recent developments)

### 11.1 Current standard systemic modalities
**Immune checkpoint inhibitors (ICIs).** ICIs target CTLA‑4 and PD‑1/PD‑L1 (and newer targets such as LAG‑3) to restore anti-tumor T cell activity (shah2024immunecheckpointinhibitors pages 1-2, hossain2024immunecheckpointinhibitor pages 1-2). Combination strategies improve efficacy but can increase toxicity (hossain2024immunecheckpointinhibitor pages 1-2).

**Targeted therapy for BRAF‑mutant melanoma.** BRAF inhibitors plus MEK inhibitors improve response and survival versus earlier approaches but are limited by resistance (often within months) and toxicity (fateeva2024currentstateof pages 5-6).

**Visual summary of therapy classes.** Fateeva et al. (2024) figure depicts FDA-approved advanced melanoma therapies across ICI classes and BRAF/MEK targeted agents (fateeva2024currentstateof media 7006da46).

### 11.2 Brain metastases management (real-world and trial data)
**Real-world outcomes with ipilimumab+nivolumab in asymptomatic melanoma brain metastases.** Danish registry cohort (n=79) first‑line ipilimumab+nivolumab: ORR **46.9%**, CR **16.5%**, 6‑month PFS **53.5%**, median PFS **6.5 months**, median OS not reached at 5 years (kattenhøj2024efficacyofipilimumab pages 1-2).

**Trial benchmark and emerging combinations.** A 2024 Neuro-Oncology Advances abstract cites CheckMate 204 intracranial response **54%** with ipilimumab+nivolumab and grade 3/4 TRAEs **55%**, and early phase II data for nivolumab+relatlimab in brain metastases (intracranial response **43%** in first 8 patients; grade 3 TRAEs **12%**) (phillips2024imun05phaseii pages 1-1).

### 11.3 Emerging/ongoing clinical trials (real-world implementation readiness)
ClinicalTrials.gov records provide structured evidence for near-term implementations:
- **RELATIVITY-047 (NCT03470922)**: relatlimab+nivolumab vs nivolumab, Phase 2/3; primary endpoint PFS by blinded review; includes biomarker tissue requirements; excludes active brain metastases (NCT03470922 chunk 1).
- **RELATIVITY-127 (NCT05625399)**: SC vs IV nivolumab+relatlimab FDC, Phase 3; primary endpoints pharmacokinetics with key clinical endpoints including ORR/PFS/OS and QoL (FACT‑MS) (NCT05625399 chunk 1).
- **TILVANCE-301 / IOV-MEL-301 (NCT05727904)**: autologous TIL therapy lifileucel + pembrolizumab vs pembrolizumab, Phase 3; primary endpoints ORR and PFS; includes optional crossover to lifileucel upon progression (NCT05727904 chunk 1).

### 11.4 Treatment ontology suggestions (MAXO; examples)
- Immune checkpoint inhibitor therapy; anti‑PD‑1 therapy; anti‑CTLA‑4 therapy; anti‑LAG‑3 therapy; BRAF inhibitor therapy; MEK inhibitor therapy; adoptive T cell therapy / tumor‑infiltrating lymphocyte therapy; stereotactic radiosurgery (for brain metastases) (therapy modalities discussed across sources) (fateeva2024currentstateof media 7006da46, NCT05727904 chunk 1).

---

## 12. Prevention

**Primary prevention.** Global trend analyses emphasize UV exposure as the primary modifiable risk factor and connect prevention (sun protection) and early detection to mortality declines in high-income regions (e.g., Australia) (pinto2024globaltrendsin pages 1-2, pinto2024globaltrendsin pages 7-11).

**Secondary prevention/early detection.** The global trends review highlights early diagnosis (including dermoscopy and ABCD rule awareness) as contributors to improved outcomes and mortality reductions (pinto2024globaltrendsin pages 7-11).

(Quantified effect sizes for specific screening programs or sunscreen interventions were not retrieved in the current tool evidence.)

---

## 13. Other Species / Natural Disease

**Canine melanoma as a comparative model.** Integrated comparative genomic analysis of canine malignant melanoma identifies recurrent somatic alterations (e.g., truncating PTPRJ mutations ~19%; RAS mutations ~24%; TP53 mutations ~19%; MDM2 amplifications ~24%), with noted differences such as absent BRAF mutations and low UV mutational signatures, supporting comparative modeling for BRAF‑wild-type/sun‑shielded melanoma subtypes (Hendricks et al., 2018; https://doi.org/10.1371/journal.pgen.1007589) (pqac-000000?? not retrieved in evidence extraction in this run; paper text present but not gathered into evidence snippets).

Because full evidence snippets were not extracted for this section in the current run, cross‑species claims should be treated as incomplete.

---

## 14. Model Organisms and Experimental Models

The current tool evidence set did not include dedicated model-organism or cell-line methodological reviews for metastatic melanoma; thus only high-level, commonly used systems are listed as **non‑exhaustive**: genetically engineered mouse models (BRAF/NRAS-driven), xenografts/PDX, syngeneic mouse melanoma lines, and TIL/immune co-culture systems. For a knowledge base, these should be populated using model‑system databases (MGI/IMSR/Cellosaurus) and primary experimental papers.

---

## Consolidated quantitative reference table

| Domain | Finding | Numeric value(s) | Source (first author year) | URL | Evidence ID |
|---|---|---|---|---|---|
| Epidemiology/Burden | Global melanoma incidence and deaths (GLOBOCAN 2022) | 331,722 new melanoma cases; ~58,667 deaths worldwide | Wang 2025 | https://doi.org/10.1097/cm9.0000000000003416 | (wang2025recentglobalpatterns pages 1-2) |
| Epidemiology/Burden | Global cutaneous malignant melanoma burden (GBD 2021) | Prevalence 833,215 cases in 2021; ASPR 25.37/100,000; ASMR 0.73/100,000; DALYs 1,678,836 | Liu 2024 | https://doi.org/10.3389/fonc.2024.1512942 | (liu2024globalregionaland pages 1-2) |
| Epidemiology/Burden | US melanoma mortality trend, 1999–2020 | 184,416 deaths; age-adjusted mortality rate declined 2.7 to 2.0/100,000; APC -1.3%/year; after 2013 non-Hispanic White AAMR -6.1%/year | Didier 2024 | https://doi.org/10.1186/s12885-024-12426-z | (didier2024patternsandtrends pages 1-2) |
| Therapy Outcomes | Historical metastatic melanoma prognosis before modern therapy | Median OS ~6 months; 1-year OS ~25% | Shah 2024 | https://doi.org/10.3892/mi.2024.137 | (shah2024immunecheckpointinhibitors pages 1-2) |
| Therapy Outcomes | Historical metastatic melanoma prognosis before 2011 | Median OS about 6 months | Poletto 2023 | https://doi.org/10.3390/cancers16010101 | (poletto2023predictivefactorsin pages 1-2) |
| Therapy Outcomes | Anti-PD-1 monotherapy outcomes in metastatic melanoma | ORR 42–45%; median PFS 4.6–8.4 months; median OS around 3 years | Poletto 2023 | https://doi.org/10.3390/cancers16010101 | (poletto2023predictivefactorsin pages 1-2) |
| Therapy Outcomes | Nivolumab + ipilimumab combination outcomes | ORR 58%; median PFS 11.5 months; median OS 72.1 months | Poletto 2023 | https://doi.org/10.3390/cancers16010101 | (poletto2023predictivefactorsin pages 1-2) |
| Therapy Outcomes | Nivolumab + ipilimumab long-term survival | 6.5-year survival rate 56% | Jalil 2024 | https://doi.org/10.20517/cdr.2024.54 | (jalil2024exploringresistanceto pages 1-3) |
| Therapy Outcomes | BRAF+MEK targeted therapy outcomes in advanced melanoma | Overall response and survival rates increased to 50–70%; progression often after 6–7 months with single-agent BRAFi | Fateeva 2024 | https://doi.org/10.3390/cancers16081571 | (fateeva2024currentstateof pages 5-6) |
| Therapy Outcomes | Real-world asymptomatic melanoma brain metastases treated first-line with ipi+nivo | ORR 46.9%; CR 16.5%; 6-month PFS 53.5%; median PFS 6.5 months; median OS not reached at 5 years | Kattenhøj 2024 | https://doi.org/10.3390/cancers16142559 | (kattenhøj2024efficacyofipilimumab pages 1-2) |
| Therapy Outcomes | ctDNA prognostic impact before ICI | OS HR 3.19 (95% CI 2.22–4.58); PFS HR 2.08 (95% CI 1.61–2.69) for detectable pretreatment ctDNA | Liu 2025 | https://doi.org/10.3389/fimmu.2024.1520441 | (liu2025theprognosticvalue pages 1-2) |
| Therapy Outcomes | ctDNA prognostic impact during ICI | OS HR 4.57 (95% CI 3.03–6.91); PFS HR 3.79 (95% CI 2.13–6.75) for detectable on-treatment ctDNA | Liu 2025 | https://doi.org/10.3389/fimmu.2024.1520441 | (liu2025theprognosticvalue pages 1-2) |
| Therapy Outcomes | LDH-stratified survival with metastatic melanoma therapy | LDH <2x ULN: 1-year PFS 68%, OS 90%; 2-year PFS 46%, OS 75%. LDH ≥2x ULN: 1-year PFS 8%, OS 40%; 2-year PFS 2%, OS 7% | Roccuzzo 2024 | https://doi.org/10.1080/14737159.2024.2347484 | (roccuzzo2024prognosticbiomarkersin pages 3-4) |
| Ongoing Clinical Trials | RELATIVITY-047 (NCT03470922): relatlimab + nivolumab vs nivolumab in untreated unresectable/metastatic melanoma | Phase 2/3; ACTIVE_NOT_RECRUITING; enrollment 714; start 2018-04-11; primary endpoint PFS by BICR per RECIST v1.1; key secondary endpoints OS, ORR | Bristol-Myers Squibb / NCT03470922 | https://clinicaltrials.gov/study/NCT03470922 | (NCT03470922 chunk 1) |
| Ongoing Clinical Trials | RELATIVITY-127 (NCT05625399): SC vs IV nivolumab + relatlimab fixed-dose combination in previously untreated metastatic/unresectable melanoma | Phase 3; ACTIVE_NOT_RECRUITING; enrollment 579; start 2023-03-06; primary endpoints nivolumab and relatlimab PK (Cavgd28, Cminss); key secondary endpoints ORR, DoR, DCR, TTR, PFS, OS, safety, FACT-MS | Bristol-Myers Squibb / NCT05625399 | https://clinicaltrials.gov/study/NCT05625399 | (NCT05625399 chunk 1) |
| Ongoing Clinical Trials | TILVANCE-301 / IOV-MEL-301 (NCT05727904): lifileucel + pembrolizumab vs pembrolizumab alone in untreated advanced melanoma | Phase 3; RECRUITING; enrollment 670; start 2023-03-30; primary endpoints ORR and PFS by blinded independent review per RECIST v1.1; key secondary endpoints OS, CR rate, DoR, EFS, PFS2, safety | Iovance / NCT05727904 | https://clinicaltrials.gov/study/NCT05727904 | (NCT05727904 chunk 1) |


*Table: This table compiles high-yield quantitative findings for metastatic melanoma across epidemiology, therapy outcomes, biomarker prognostics, and major ongoing clinical trials. It is useful as a compact reference for evidence-backed burden estimates and current treatment landscape metrics.*

---

## Expert synthesis / analysis (authoritative themes)
1) **Durable survival is now achievable**, especially with combination ICI regimens, but **primary/acquired resistance remains common (~50%)** (poletto2023predictivefactorsin pages 1-2, jalil2024exploringresistanceto pages 1-3, hossain2024immunecheckpointinhibitor pages 1-2).
2) **Mechanisms of resistance are multi-layered**, spanning tumor intrinsic (antigen presentation defects, IFN‑γ pathway changes, MAPK/PI3K signaling) and extrinsic TME factors (Tregs/TAMs/MDSCs, hypoxia/acidity, metabolic suppression), and may be influenced by the **gut microbiome** (kato2026drugtherapyfor pages 3-4, zielinska2025mechanismsofresistance pages 8-9).
3) **Real-world data support translation of trial efficacy** to selected populations (e.g., asymptomatic melanoma brain metastases treated with ipilimumab+nivolumab in a nationwide Danish registry) (kattenhøj2024efficacyofipilimumab pages 1-2).
4) Biomarkers with practical clinical traction include **LDH and ctDNA**, with strong prognostic separation and meta-analytic hazard ratios, while **TMB/PD‑L1/IFN‑γ signatures** are promising but require standardization and context-aware interpretation (roccuzzo2024prognosticbiomarkersin pages 3-4, liu2025theprognosticvalue pages 1-2).

---

## Notes on evidence gaps in this run
- Dedicated retrieval of **MONDO ID, MeSH ID, ICD‑11 code(s)**, structured **HPO phenotype frequency tables**, and **diagnostic/pathology guideline documents** was not successful with the current tool calls; therefore, these elements are intentionally not asserted beyond what was directly evidenced (OpenTargets Search: metastatic melanoma, datzmann2021implementationandeffectiveness pages 2-3).

References

1. (OpenTargets Search: metastatic melanoma): Open Targets Query (metastatic melanoma, 43 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (datzmann2021implementationandeffectiveness pages 2-3): T Datzmann, J Schmitt, S Fuhrmann, and M Roessler. Implementation and effectiveness of novel therapeutic substances for advanced malignant melanoma in saxony, germany, 2010–2020—cohort study …. Unknown journal, 2021.

3. (kattenhøj2024efficacyofipilimumab pages 1-2): Karoline Dreyer Kattenhøj, Christine Louise Møberg, Louise Mahncke Guldbrandt, Rasmus Blechingberg Friis, Christophe Kamungu Mapendano, Søren Kjær Petersen, Christina Halgaard Bruvik Ruhlmann, Inge Marie Svane, Marco Donia, Eva Ellebaek, and Henrik Schmidt. Efficacy of ipilimumab and nivolumab in patients with melanoma and brain metastases—a danish real-world cohort. Cancers, 16:2559, Jul 2024. URL: https://doi.org/10.3390/cancers16142559, doi:10.3390/cancers16142559. This article has 6 citations.

4. (jalil2024exploringresistanceto pages 1-3): Anum Jalil, Melissa M Donate, and Jane Mattei. Exploring resistance to immune checkpoint inhibitors and targeted therapies in melanoma. Cancer Drug Resistance, Oct 2024. URL: https://doi.org/10.20517/cdr.2024.54, doi:10.20517/cdr.2024.54. This article has 17 citations.

5. (liu2024globalregionaland pages 1-2): Chengling Liu, Xingchen Liu, Li Hu, Xin Li, Haiming Xin, and Sailin Zhu. Global, regional, and national burden of cutaneous malignant melanoma from 1990 to 2021 and prediction to 2045. Frontiers in Oncology, Dec 2024. URL: https://doi.org/10.3389/fonc.2024.1512942, doi:10.3389/fonc.2024.1512942. This article has 25 citations.

6. (NCT05727904 chunk 1):  Study to Investigate Lifileucel Regimen Plus Pembrolizumab Compared With Pembrolizumab Alone in Participants With Untreated Advanced Melanoma.. Iovance Biotherapeutics, Inc.. 2023. ClinicalTrials.gov Identifier: NCT05727904

7. (wang2025advancesinimmunotherapy pages 1-2): Xue Wang, Shanshan Ma, Shuting Zhu, Liucun Zhu, and Wenna Guo. Advances in immunotherapy and targeted therapy of malignant melanoma. Biomedicines, 13:225, Jan 2025. URL: https://doi.org/10.3390/biomedicines13010225, doi:10.3390/biomedicines13010225. This article has 23 citations.

8. (poletto2023predictivefactorsin pages 1-2): Stefano Poletto, Luca Paruzzo, Alessandro Nepote, Daniela Caravelli, Dario Sangiolo, and Fabrizio Carnevale-Schianca. Predictive factors in metastatic melanoma treated with immune checkpoint inhibitors: from clinical practice to future perspective. Cancers, 16:101, Dec 2023. URL: https://doi.org/10.3390/cancers16010101, doi:10.3390/cancers16010101. This article has 16 citations.

9. (shah2024immunecheckpointinhibitors pages 1-2): Vedant Shah, Viraj Panchal, Abhi Shah, Bhavya Vyas, Siddharth Agrawal, and Sanket Bharadwaj. Immune checkpoint inhibitors in metastatic melanoma therapy (review). Medicine International, Feb 2024. URL: https://doi.org/10.3892/mi.2024.137, doi:10.3892/mi.2024.137. This article has 41 citations.

10. (hossain2024immunecheckpointinhibitor pages 1-2): Sultana Mehbuba Hossain, Kevin Ly, Yih Jian Sung, Antony Braithwaite, and Kunyu Li. Immune checkpoint inhibitor therapy for metastatic melanoma: what should we focus on to improve the clinical outcomes? International Journal of Molecular Sciences, 25:10120, Sep 2024. URL: https://doi.org/10.3390/ijms251810120, doi:10.3390/ijms251810120. This article has 11 citations.

11. (pinto2024globaltrendsin pages 7-11): Giuseppe De Pinto, Silvia Mignozzi, Carlo La Vecchia, Fabio Levi, Eva Negri, and Claudia Santucci. Global trends in cutaneous malignant melanoma incidence and mortality. Melanoma Research, 34:265-275, Feb 2024. URL: https://doi.org/10.1097/cmr.0000000000000959, doi:10.1097/cmr.0000000000000959. This article has 65 citations and is from a peer-reviewed journal.

12. (wang2025recentglobalpatterns pages 1-2): Mingyue Wang, Xinghua Gao, and Li Zhang. Recent global patterns in skin cancer incidence, mortality, and prevalence. Chinese Medical Journal, 138:185-192, Dec 2025. URL: https://doi.org/10.1097/cm9.0000000000003416, doi:10.1097/cm9.0000000000003416. This article has 131 citations and is from a peer-reviewed journal.

13. (didier2024patternsandtrends pages 1-2): Alexander J. Didier, Swamroop V. Nandwani, Dean Watkins, Alan M. Fahoury, Andrew Campbell, Daniel J. Craig, Divya Vijendra, and Nancy Parquet. Patterns and trends in melanoma mortality in the united states, 1999–2020. BMC Cancer, Jul 2024. URL: https://doi.org/10.1186/s12885-024-12426-z, doi:10.1186/s12885-024-12426-z. This article has 38 citations and is from a peer-reviewed journal.

14. (fernandez2023newapproachesto pages 1-3): Manuel Felipe Fernandez, Jacob Choi, and Jeffrey Sosman. New approaches to targeted therapy in melanoma. Cancers, 15:3224, Jun 2023. URL: https://doi.org/10.3390/cancers15123224, doi:10.3390/cancers15123224. This article has 48 citations.

15. (kato2026drugtherapyfor pages 3-4): Hiroshi Kato. Drug therapy for melanoma: current updates and future prospects. Cancers, 18:382, Jan 2026. URL: https://doi.org/10.3390/cancers18030382, doi:10.3390/cancers18030382. This article has 1 citations.

16. (roccuzzo2024prognosticbiomarkersin pages 3-4): Gabriele Roccuzzo, Cristina Sarda, Valentina Pala, Simone Ribero, and Pietro Quaglino. Prognostic biomarkers in melanoma: a 2023 update from clinical trials in different therapeutic scenarios. Expert Review of Molecular Diagnostics, 24:379-392, May 2024. URL: https://doi.org/10.1080/14737159.2024.2347484, doi:10.1080/14737159.2024.2347484. This article has 12 citations and is from a peer-reviewed journal.

17. (ong2025timingofbrain pages 1-2): Claire Victoria Ong and Wolfram Samlowski. Timing of brain metastases in relation to outcome during first-line ipilimumab plus nivolumab therapy for metastatic melanoma in a community oncology practice. Journal of Neuro-Oncology, 172:645-653, Feb 2025. URL: https://doi.org/10.1007/s11060-025-04951-z, doi:10.1007/s11060-025-04951-z. This article has 1 citations and is from a peer-reviewed journal.

18. (ong2025timingofbrain pages 4-5): Claire Victoria Ong and Wolfram Samlowski. Timing of brain metastases in relation to outcome during first-line ipilimumab plus nivolumab therapy for metastatic melanoma in a community oncology practice. Journal of Neuro-Oncology, 172:645-653, Feb 2025. URL: https://doi.org/10.1007/s11060-025-04951-z, doi:10.1007/s11060-025-04951-z. This article has 1 citations and is from a peer-reviewed journal.

19. (kattenhøj2024efficacyofipilimumab pages 4-6): Karoline Dreyer Kattenhøj, Christine Louise Møberg, Louise Mahncke Guldbrandt, Rasmus Blechingberg Friis, Christophe Kamungu Mapendano, Søren Kjær Petersen, Christina Halgaard Bruvik Ruhlmann, Inge Marie Svane, Marco Donia, Eva Ellebaek, and Henrik Schmidt. Efficacy of ipilimumab and nivolumab in patients with melanoma and brain metastases—a danish real-world cohort. Cancers, 16:2559, Jul 2024. URL: https://doi.org/10.3390/cancers16142559, doi:10.3390/cancers16142559. This article has 6 citations.

20. (fateeva2024currentstateof pages 5-6): Anna Fateeva, Kevinn Eddy, and Suzie Chen. Current state of melanoma therapy and next steps: battling therapeutic resistance. Cancers, 16:1571, Apr 2024. URL: https://doi.org/10.3390/cancers16081571, doi:10.3390/cancers16081571. This article has 53 citations.

21. (kolathur2024molecularsusceptibilityand pages 13-15): Kiran Kumar Kolathur, Radhakanta Nag, Prathvi V Shenoy, Yagya Malik, Sai Manasa Varanasi, Ramcharan Singh Angom, and Debabrata Mukhopadhyay. Molecular susceptibility and treatment challenges in melanoma. Cells, 13:1383, Aug 2024. URL: https://doi.org/10.3390/cells13161383, doi:10.3390/cells13161383. This article has 11 citations.

22. (liu2025theprognosticvalue pages 1-2): Lei Liu, Shufu Hou, Aiping Zhu, Bing Yan, Linchuan Li, and Dandan Song. The prognostic value of circulating tumor dna in malignant melanoma patients treated with immune checkpoint inhibitors: a systematic review and meta-analysis. Frontiers in Immunology, Jan 2025. URL: https://doi.org/10.3389/fimmu.2024.1520441, doi:10.3389/fimmu.2024.1520441. This article has 9 citations and is from a peer-reviewed journal.

23. (song2024currentknowledgeabout pages 1-3): Lanni Song, Yixin Yang, and Xuechen Tian. Current knowledge about immunotherapy resistance for melanoma and potential predictive and prognostic biomarkers. Cancer Drug Resistance, May 2024. URL: https://doi.org/10.20517/cdr.2023.150, doi:10.20517/cdr.2023.150. This article has 5 citations.

24. (zielinska2025mechanismsofresistance pages 8-9): Magdalena K. Zielińska, Magdalena Ciążyńska, Dorota Sulejczak, Piotr Rutkowski, and Anna M. Czarnecka. Mechanisms of resistance to anti-pd-1 immunotherapy in melanoma and strategies to overcome it. Biomolecules, 15:269, Feb 2025. URL: https://doi.org/10.3390/biom15020269, doi:10.3390/biom15020269. This article has 28 citations.

25. (fateeva2024currentstateof media 7006da46): Anna Fateeva, Kevinn Eddy, and Suzie Chen. Current state of melanoma therapy and next steps: battling therapeutic resistance. Cancers, 16:1571, Apr 2024. URL: https://doi.org/10.3390/cancers16081571, doi:10.3390/cancers16081571. This article has 53 citations.

26. (fateeva2024currentstateof media e15bcd35): Anna Fateeva, Kevinn Eddy, and Suzie Chen. Current state of melanoma therapy and next steps: battling therapeutic resistance. Cancers, 16:1571, Apr 2024. URL: https://doi.org/10.3390/cancers16081571, doi:10.3390/cancers16081571. This article has 53 citations.

27. (phillips2024imun05phaseii pages 1-1): Suzanne Phillips, Elizabeth Burton, Isabella Claudia Glitza Oliva, Jennifer McQuade, Rodabe Amaria, Adi Diab, Michael Wong, Caroline Chung, Denái Milton, Jared Malke, Julie Simon, Jeffrey Wefel, Jing Li, Michael Davies, and Hussein Tawbi. Imun-05 phase ii study of nivolumab (nivo) in combination with relatlimab (rela) in patients with active melanoma brain metastases (mbm). Neuro-Oncology Advances, 6:i14-i15, Aug 2024. URL: https://doi.org/10.1093/noajnl/vdae090.044, doi:10.1093/noajnl/vdae090.044. This article has 1 citations and is from a peer-reviewed journal.

28. (NCT03470922 chunk 1):  A Study of Relatlimab Plus Nivolumab Versus Nivolumab Alone in Participants With Advanced Melanoma. Bristol-Myers Squibb. 2018. ClinicalTrials.gov Identifier: NCT03470922

29. (NCT05625399 chunk 1):  A Study of Subcutaneous Nivolumab + Relatlimab Fixed-dose Combination (FDC) in Previously Untreated Metastatic or Unresectable Melanoma. Bristol-Myers Squibb. 2023. ClinicalTrials.gov Identifier: NCT05625399

30. (pinto2024globaltrendsin pages 1-2): Giuseppe De Pinto, Silvia Mignozzi, Carlo La Vecchia, Fabio Levi, Eva Negri, and Claudia Santucci. Global trends in cutaneous malignant melanoma incidence and mortality. Melanoma Research, 34:265-275, Feb 2024. URL: https://doi.org/10.1097/cmr.0000000000000959, doi:10.1097/cmr.0000000000000959. This article has 65 citations and is from a peer-reviewed journal.

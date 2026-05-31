---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T01:25:01.101026'
end_time: '2026-05-10T01:48:14.012620'
duration_seconds: 1392.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Ovarian Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metastatic Ovarian Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Ovarian Cancer** covering all of the
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
- **Disease Name:** Metastatic Ovarian Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Ovarian Cancer** covering all of the
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


# Metastatic Ovarian Cancer (advanced epithelial ovarian cancer; FIGO stage IV) — Disease Characteristics Research Report

## Scope and terminology
This report focuses on **advanced/metastatic epithelial ovarian cancer (EOC)**, including ovarian, fallopian tube, and primary peritoneal carcinomas with **advanced-stage dissemination (commonly FIGO III–IV)**, and particularly **metastatic disease corresponding to FIGO stage IV**. In contemporary clinical guidance, “advanced EOC” is often used operationally for **stage III–IV disease** and drives shared diagnostic and treatment pathways. (ghirardi2023diagnosticandtherapeutic pages 1-2, perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

### Key concept definitions (current understanding)
* **Peritoneal metastasis / carcinomatosis**: the most common route of spread in ovarian cancer at diagnosis or recurrence (transcoelomic spread in the peritoneal cavity). (tsili2024imagingofperitoneal pages 1-2)
* **Primary debulking surgery (PDS)** vs **neoadjuvant chemotherapy followed by interval debulking surgery (NACT-IDS)**: two standard first-line strategies for advanced disease; the clinical goal is **no gross residual disease** when surgery is undertaken. (ghirardi2023diagnosticandtherapeutic pages 1-2, ghirardi2023diagnosticandtherapeutic pages 5-7)
* **Platinum resistance** (clinical concept): commonly defined by **platinum-free interval <6 months** (vs platinum-sensitive ≥6 months), influencing subsequent-line strategy and trial eligibility. (caruso2025ovariancancera pages 8-9)
* **Biomarker-selected therapy**: treatment selection based on **BRCA/HRD** (PARP inhibitor sensitivity) and **FRα (FOLR1) expression** (eligibility for mirvetuximab soravtansine in platinum-resistant disease). (ghirardi2023diagnosticandtherapeutic pages 7-8, perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

## Target disease identifiers and synonyms
### Ontology/identifier snapshot
* **MONDO**: Ovarian cancer **MONDO:0008170** (used as the nearest disease-level ontology concept in Open Targets; metastatic subtype was not available as a distinct MONDO term in retrieved evidence). (OpenTargets Search: metastatic ovarian cancer,ovarian carcinoma)
* **MeSH / ICD**: In practice, metastatic ovarian cancer is commonly coded under ovarian malignancy (e.g., ICD-10 **C56**), while metastatic status is captured by staging (FIGO) rather than a distinct ICD code in many workflows (not uniquely resolved in retrieved evidence). (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

### Common synonyms and alternative names
* Metastatic ovarian cancer; **stage IV epithelial ovarian cancer**; advanced ovarian cancer; ovarian cancer with peritoneal metastases; advanced epithelial ovarian cancer; advanced tubo-ovarian carcinoma; ovarian/fallopian tube/primary peritoneal cancer (advanced). (ghirardi2023diagnosticandtherapeutic pages 1-2, perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

### Evidence source type
Information here is derived primarily from **aggregated disease-level resources and guidelines** (e.g., ASCO, SEOM–GEICO; systematic reviews), plus **multicenter retrospective cohorts** and **phase II/III clinical trials** in advanced/metastatic settings. (ghirardi2023diagnosticandtherapeutic pages 1-2, ghirardi2023diagnosticandtherapeutic pages 5-7, perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

## 1. Disease information (overview)
Ovarian cancer is a leading cause of gynecologic cancer mortality and **most patients present at advanced stage**. In a diagnostic/treatment pathway review focused on advanced ovarian cancer with peritoneal metastases, the authors state: **“Over two thirds of ovarian cancer patients present with advanced stage disease”** and standard treatment includes **cytoreductive surgery plus carboplatin–paclitaxel chemotherapy**. (ghirardi2023diagnosticandtherapeutic pages 1-2)

## 2. Etiology
### 2.1 Disease causal factors (mechanistic, genetic)
**Inherited DNA repair defects** are a major causal contributor to a clinically actionable subset of EOC. Open Targets disease–gene associations for ovarian cancer highlight DNA repair genes and other cancer genes, including **BRCA1, BRCA2, RAD51C, RAD51D, BRIP1, PALB2, MSH2, MSH6, and TP53**. (OpenTargets Search: metastatic ovarian cancer,ovarian carcinoma)

A contemporary clinical review summarizing risk and prevention reports: **“Approximately one-quarter of ovarian cancers are hereditary”** and that BRCA1/2 account for a substantial fraction of hereditary cases. (caruso2025ovariancancera pages 3-3)

### 2.2 Risk factors (genetic, environmental, reproductive)
Quantitative associations reported in a large contemporary review include:
* **Endometriosis**: hazard ratio **4.20** (95% CI 3.59–4.91) in one cited analysis. (caruso2025ovariancancera pages 3-3)
* **Infertility**: standardized incidence ratio **2.0** (95% CI 1.8–4.0). (caruso2025ovariancancera pages 3-3)
* **Postmenopausal estrogen therapy**: relative risk **1.31** (95% CI 1.21–1.41). (caruso2025ovariancancera pages 3-3)
* **Familial/genetic risk**: BRCA carrier lifetime ovarian cancer risk estimated broadly as **20%–70%** in one clinical synthesis. (caruso2025ovariancancera pages 3-3)

A clinical risk assessment review provides genotype-stratified absolute lifetime risks:
* **BRCA1**: **39%–58%**; **BRCA2**: **13%–29%**. (days2025ovariancancerrisk pages 2-4)

### 2.3 Protective factors
Protective reproductive/hormonal factors with quantitative effect estimates include:
* **Multiparity**: OR per additional birth **0.81** (95% CI 0.75–0.85). (caruso2025ovariancancera pages 3-3)
* **Breastfeeding**: OR **0.72** (95% CI 0.68–0.76). (caruso2025ovariancancera pages 3-3)
* **Oral contraceptive use**: OR **0.66** (95% CI 0.52–0.83). (caruso2025ovariancancera pages 3-3)

A global epidemiology review quantifies similar protective associations:
* **Ever vs never oral contraceptives**: OR **0.73** (95% CI 0.70–0.76); each 5 years of use associated with ~20% lower risk (95% CI 18–23%). (li2026globalepidemiologyof pages 5-7)
* **Breastfeeding**: ~10% lower risk per 12 months (RR **0.89**, 95% CI 0.84–0.94). (li2026globalepidemiologyof pages 5-7)

### 2.4 Gene–environment interactions
Robust, clinically used gene–environment interaction models specific to metastatic presentation were not identifiable from the retrieved evidence; however, available clinical syntheses emphasize that inherited BRCA-associated risk intersects with reproductive/hormonal exposures (e.g., oral contraceptives) relevant to prevention decisions. (days2025ovariancancerrisk pages 2-4, caruso2025ovariancancera pages 3-3)

## 3. Phenotypes (clinical presentation)
### 3.1 Common clinical phenotypes in metastatic/advanced disease
Advanced EOC frequently presents with extensive intraperitoneal tumor burden and/or pleural involvement, driving symptoms such as abdominal distension and respiratory symptoms. A prevention/early-detection implementation review notes that **CA-125 is elevated in ~80% of advanced ovarian cancer**, reflecting the frequent high tumor burden at advanced presentation. (masouleh2024exploringopportunisticsalpingectomy pages 19-23)

#### Suggested HPO terms (phenotype mapping; typical in advanced disease)
Because the retrieved evidence base emphasizes diagnostic pathways rather than symptom prevalence tables, the following HPO mappings are proposed as standard phenotype representations for advanced/metastatic EOC, without frequency claims:
* Ascites — **HP:0001541**
* Abdominal distension — **HP:0003270**
* Abdominal pain — **HP:0002027**
* Pleural effusion — **HP:0002202**
* Dyspnea — **HP:0002094**
* Elevated CA-125 — **HP:0032943** (as a biomarker abnormality)

### 3.2 Quality-of-life impact
Peritoneal dissemination is repeatedly highlighted as clinically consequential because it complicates resectability and contributes to morbidity and recurrence risk; peritoneal metastasis mapping is positioned as crucial for planning therapy and predicting feasibility of complete cytoreduction. (tsili2024imagingofperitoneal pages 1-2)

## 4. Genetic / molecular information
### 4.1 Major causal/driver genes and biomarker concepts
Key clinically actionable molecular concepts for metastatic/advanced EOC include:
* **BRCA1/BRCA2 alterations** (germline and somatic) and broader **homologous recombination deficiency (HRD)**, which predict benefit from PARP inhibitors. (ghirardi2023diagnosticandtherapeutic pages 7-8, caruso2025ovariancancera pages 3-3)
* **TP53 alterations**: a hallmark of high-grade serous ovarian cancer (frequently referenced in epidemiology and molecular summaries and in Open Targets associations), though not typically used alone to select current approved therapies. (OpenTargets Search: metastatic ovarian cancer,ovarian carcinoma, masouleh2024exploringopportunisticsalpingectomy pages 19-23)
* **FRα (FOLR1) expression**: predictive biomarker for mirvetuximab soravtansine benefit in platinum-resistant disease; MIRASOL required **≥75% of cells with ≥2+ staining intensity**. (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

### 4.2 Biomarker-linked treatment selection (real-world implementation)
The SEOM–GEICO 2023 guideline summary emphasizes that new predictive biomarkers enable selection for targeted agents, and that diagnostics should enable biomarker analysis (adequate tissue sampling, cytology for effusions/ascites when present, and molecular profiling). (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

## 5. Mechanism / pathophysiology (metastasis-focused)
A metastasis-relevant mechanistic chain supported directly by the retrieved evidence is:
1) Primary tubo-ovarian/peritoneal carcinoma develops and sheds tumor into peritoneal cavity →
2) **Peritoneal metastases** become the predominant spread pattern at diagnosis/recurrence →
3) Peritoneal tumor distribution determines feasibility of complete cytoreduction and drives selection between PDS and NACT-IDS →
4) Residual disease after surgery strongly predicts outcomes. (ghirardi2023diagnosticandtherapeutic pages 1-2, tsili2024imagingofperitoneal pages 1-2)

**Ontology suggestions (mechanism mapping):**
* GO biological processes (suggested): epithelial cell proliferation (GO:0050673), cell adhesion (GO:0007155), extracellular matrix organization (GO:0030198), angiogenesis (GO:0001525), DNA repair (GO:0006281).
* CL cell types (suggested): epithelial cell (CL:0000066), fibroblast (CL:0000057), macrophage (CL:0000235), mesothelial cell (CL:0000077).

## 6. Anatomical structures affected
### Organ/tissue distribution relevant to metastatic disease
Peritoneal spread involves structures of the peritoneal cavity and abdominopelvic regions. Imaging meta-analysis emphasizes mapping peritoneal disease extent for surgical planning. (tsili2024imagingofperitoneal pages 1-2)

**Stage IV subclassification** highlights thoracic involvement:
* A multicenter stage IV cohort described FIGO IVA vs IVB outcomes, consistent with pleural involvement defining a distinct stage IV group (IVA) with worse prognosis than IVB in that dataset. (metairie2023asuggestedmodification pages 11-12)

**UBERON term suggestions:**
* Ovary — UBERON:0000992
* Fallopian tube — UBERON:0003889
* Peritoneum — UBERON:0002358
* Greater omentum — UBERON:0003688
* Pleural cavity/pleura — UBERON:0000175 / UBERON:0002097

## 7. Temporal development (onset and progression)
Advanced EOC typically presents after an insidious course; in one implementation-focused prevention review, the authors emphasize that early symptoms can be vague and that disease may progress rapidly, contributing to late-stage diagnosis. (masouleh2024exploringopportunisticsalpingectomy pages 19-23)

## 8. Inheritance and population
### 8.1 Epidemiology (recent statistics)
**US burden (2024)**: an imaging systematic review reports that in the United States **~19,680 cases and 12,740 deaths were expected in 2024**, and cites an overall **5-year relative survival ~48%** for ovarian cancer. (tsili2024imagingofperitoneal pages 1-2)

**Global burden and trends (2022–2021)**:
* A contemporary review reports **~324,398 new cases and 206,839 deaths** globally (2022). (caruso2025ovariancancera pages 2-3)
* Global age-standardized incidence decreased from **7.22 to 6.71 per 100,000 (1990–2021)**; global mortality decreased from **4.73 to 4.06 per 100,000 (1999–2021)**. (li2026globalepidemiologyof pages 1-2)

### 8.2 Inheritance patterns
Risk is substantially elevated in hereditary cancer syndromes (e.g., BRCA1/2). Clinical risk review notes that **10%–15% of ovarian cancers have a germline BRCA mutation** and provides BRCA1/2 lifetime risk ranges. (days2025ovariancancerrisk pages 2-4)

## 9. Diagnostics
### 9.1 Diagnostic pathway (guideline-aligned; real-world implementation)
The diagnostic process in advanced disease is designed to (i) confirm malignancy and histotype, (ii) stage and map disease, and (iii) determine likelihood of complete cytoreduction.

**ASCO guideline update (published 2025-03-??; DOI available)** explicitly recommends that patients with suspected stage III–IV disease be evaluated by a gynecologic oncologist and that evaluation includes **CA-125, CT abdomen/pelvis, and chest imaging**, and that **all patients be offered germline genetic and somatic testing at diagnosis**. In addition, ASCO specifies histologic confirmation before starting NACT and recommends a platinum–taxane doublet for NACT. (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

**SEOM–GEICO 2023 guideline (published 2024-07; https://doi.org/10.1007/s12094-024-03531-3)** emphasizes:
* Physical examination and labs including **CA-125**, plus pelvic ultrasound.
* CT chest/abdomen/pelvis for disease extent; MRI and PET-CT as adjuncts in advanced disease.
* **Initial laparoscopy** to obtain histopathology and evaluate feasibility of complete cytoreduction; use of peritoneal extension scoring (e.g., PCI, Fagotti score) for surgical planning. (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

### 9.2 Imaging for peritoneal metastases (systematic review evidence)
A 2024 systematic review/meta-analysis (33 studies; 487 women) concludes MRI and FDG PET/CT have higher per-patient sensitivity than MDCT for detecting peritoneal metastases, and reiterates the clinical importance of mapping peritoneal disease distribution. (tsili2024imagingofperitoneal pages 1-2)

### 9.3 Laparoscopy and tumor burden scoring
In a pathway review, the authors note that CT and CA-125 have limitations for predicting optimal cytoreduction, whereas **laparoscopic assessment using validated scoring** provides the highest specificity for identifying patients likely to undergo suboptimal cytoreduction and thus best suited to NACT-IDS. (ghirardi2023diagnosticandtherapeutic pages 1-2)

### 9.4 Liquid biopsy (emerging; advanced disease monitoring)
While not standard-of-care for primary diagnosis in advanced EOC in the retrieved guideline excerpts, evolving studies suggest ctDNA/cfDNA may correlate with CA-125 and potentially identify recurrence earlier than CT/CA-125 changes in small cohorts; however, broad clinical implementation remains investigational. (tsili2024imagingofperitoneal pages 1-2)

## 10. Treatment
### 10.1 First-line backbone and surgical strategy
Standard first-line management consists of **cytoreductive surgery** (with the goal of **no gross residual disease**) plus **carboplatin–paclitaxel chemotherapy**. (ghirardi2023diagnosticandtherapeutic pages 1-2, ghirardi2023diagnosticandtherapeutic pages 7-8)

#### Choosing PDS vs NACT-IDS (trial evidence summarized in 2023 review)
Randomized evidence summarized for advanced disease includes:
* EORTC-55971: median OS **29 vs 30 months** (PDS vs NACT-IDS). (ghirardi2023diagnosticandtherapeutic pages 5-7)
* CHORUS: median OS **22.8 vs 24.5 months** (PDS vs NACT-IDS). (ghirardi2023diagnosticandtherapeutic pages 5-7)
* Pooled analysis (FIGO stage IV subgroup): median OS **21.2 vs 24.3 months** and median PFS **9.7 vs 10.6 months**, favoring NACT-IDS in that analysis. (ghirardi2023diagnosticandtherapeutic pages 5-7)

### 10.2 Anti-angiogenic therapy (bevacizumab)
A review excerpt summarizes two major phase 3 trials:
* GOG-0218: bevacizumab strategy PFS **14.1 vs 10.3 months**.
* ICON7: PFS **24.1 vs 22.4 months**.
These results support modest PFS improvements when bevacizumab is added to chemotherapy and continued as maintenance in selected advanced settings. (caruso2025ovariancancera pages 8-8)

### 10.3 PARP inhibitor maintenance (HRD/BRCA-guided)
In a pathway review, SOLO-1 is summarized as showing **HR 0.30 (95% CI 0.23–0.41)** for progression/death with olaparib maintenance, and median PFS not reached vs 13.8 months at 41-month follow-up in that trial context. (ghirardi2023diagnosticandtherapeutic pages 7-8)

### 10.4 Antibody–drug conjugate targeting FRα: mirvetuximab soravtansine
**SORAYA (phase II; JCO 2023-05; https://doi.org/10.1200/JCO.22.01900)** abstract states:
* ORR **32.4%** (95% CI 23.6–42.2); median duration of response **6.9 months**.
* Common adverse events included blurred vision (41%) and keratopathy (29%). (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

**MIRASOL (phase 3; NEJM 2023-12; https://doi.org/10.1056/NEJMoa2309169)** abstract states:
* Median PFS **5.62 vs 3.98 months**; ORR **42.3% vs 15.9%**.
* Median OS **16.46 vs 12.75 months**.
* Grade ≥3 adverse events **41.7% vs 54.1%**. (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

A 2024 update on SORAYA reports **final median OS 15.0 months** (95% CI 11.5–18.7) at data cut-off 2022-12-22, supporting clinically meaningful activity in FRα-high platinum-resistant disease. (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

### Suggested MAXO terms (treatments)
* Cytoreductive surgery — **MAXO:0001175** (suggested)
* Neoadjuvant chemotherapy — **MAXO:0000748** (suggested)
* Platinum-based chemotherapy — **MAXO:0000058** (suggested)
* PARP inhibitor therapy — **MAXO:0001021** (suggested)
* Anti-VEGF therapy — **MAXO:0000625** (suggested)
* Antibody–drug conjugate therapy — **MAXO:0001301** (suggested)

## 11. Outcome / prognosis
### Stage IV heterogeneity
A multicenter retrospective study of FIGO stage IV epithelial ovarian cancer (n=307) reported worse outcomes for stage IVA vs IVB:
* Median OS **31 vs 45 months** and median PFS **18 vs 25 months** (IVA vs IVB), suggesting meaningful prognostic heterogeneity within stage IV and supporting efforts to refine stage IV subclassification. (metairie2023asuggestedmodification pages 11-12)

### Peritoneal tumor burden and outcomes
Disease mapping and completeness of cytoreduction are repeatedly emphasized as prognostically critical; the pathway review notes that achieving no gross residual disease is the surgical goal and that residual disease volume strongly predicts survival. (ghirardi2023diagnosticandtherapeutic pages 1-2, ghirardi2023diagnosticandtherapeutic pages 5-7)

## 12. Prevention
### 12.1 Primary prevention and risk reduction (high-risk genetics)
A clinical review reports that **bilateral salpingo-oophorectomy** is the most effective preventive option for high-risk women; a pooled analysis of **9,192 BRCA1/2 carriers** found an **81% risk reduction over 4 years** (HR **0.19**, 95% CI 0.13–0.27). (caruso2025ovariancancera pages 3-3)

### 12.2 Opportunistic salpingectomy (average-risk prevention strategy)
A global epidemiology review reports **unilateral or bilateral salpingectomy** associated with reduced ovarian cancer risk (HR **0.65**, 95% CI 0.52–0.81). (li2026globalepidemiologyof pages 5-7)

A feasibility/safety synthesis of opportunistic salpingectomy in general surgery settings suggests relative safety in limited data (no complications attributable to the procedure in 140 patients across included studies) and reports feasibility in selected procedures (e.g., successful in 98/105 cholecystectomies in one study). (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

### 12.3 Screening limitations (secondary prevention)
A prevention/implementation review reports that large screening trials have not demonstrated clear mortality benefit:
* PLCO (78,286 women): CA-125 + transvaginal ultrasound had PPV **26.5%** and no survival benefit at 15 years.
* UKCTOCS: no significant survival improvement. (masouleh2024exploringopportunisticsalpingectomy pages 19-23)

## 13. Model organisms and experimental systems
Direct evidence on specific ovarian cancer animal models and organoid/PDX systems was not extracted into the citable evidence set for this report. As a result, this section is not populated with model-specific performance claims.

## Recent developments (2023–2024 prioritized highlights)
1) **Imaging evidence base update (2024)**: systematic review/meta-analysis supports MRI and FDG PET/CT as preferred modalities (vs MDCT) for detecting peritoneal metastases in ovarian cancer, emphasizing the need for disease mapping to guide surgery. (tsili2024imagingofperitoneal pages 1-2)
2) **Guideline-driven diagnostic pathway emphasis (2024)**: SEOM–GEICO (2023 guideline published 2024) highlights structured workup including CA-125, CT chest/abdomen/pelvis, and the increasing role of laparoscopy-based scoring and biomarker-informed therapy selection. (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)
3) **Targeted therapy implementation**: mirvetuximab soravtansine demonstrates clinically meaningful benefit in FRα-high platinum-resistant ovarian cancer (SORAYA 2023; MIRASOL 2023), supporting routine FRα testing in this setting. (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)

## Key diagnostic/treatment pathway figure (evidence-supported visual)
A diagnostic/therapeutic pathway algorithm figure (Figure 1) from a 2023 review illustrates how clinical assessment, biopsy confirmation, and laparoscopic scoring guide selection between PDS and NACT-IDS in advanced disease. (ghirardi2023diagnosticandtherapeutic media b74131ac)

## Structured summary table (for knowledge base ingestion)
| Domain | Summary | Key sources |
|---|---|---|
| Disease definition, identifiers, synonyms | Advanced/metastatic epithelial ovarian cancer refers to epithelial ovarian, fallopian tube, or primary peritoneal carcinoma presenting with disseminated intra-abdominal disease and/or distant metastasis; advanced disease is commonly stage III–IV, and metastatic disease generally corresponds to FIGO stage IV. Common synonyms used in the literature include advanced ovarian cancer, stage IV epithelial ovarian cancer, metastatic ovarian cancer, ovarian cancer with peritoneal metastases, and advanced epithelial ovarian cancer. Disease-level aggregated resources/tools referenced include Open Targets association data for ovarian cancer (MONDO_0008170). MeSH/ICD-10 identifiers are variably applied in practice to ovarian malignancy rather than a unique metastatic subtype; ICD-10 commonly maps ovarian cancer to C56. | Open Targets context (ovarian cancer MONDO_0008170); Ghirardi 2023 https://doi.org/10.3390/cancers15020407; Métairie 2023 https://doi.org/10.3390/cancers15030706 |
| Key clinical characteristics and spread pattern | Peritoneal metastases are the most common route of spread at diagnosis and recurrence. FIGO stage IVA denotes pleural effusion/pleural involvement; stage IVB denotes parenchymal metastases and/or extra-abdominal lymph node metastases. In one multicenter stage IV cohort (n=307), median OS was 31 months for stage IVA versus 45 months for stage IVB; median PFS 18 versus 25 months. | Tsili 2024 https://doi.org/10.3390/cancers16081467; Métairie 2023 https://doi.org/10.3390/cancers15030706 |
| Diagnostic workup | Guideline-level workup includes gynecologic oncologist assessment, CA-125, CT abdomen/pelvis plus chest imaging, and germline and somatic testing at diagnosis. Cross-sectional imaging maps disease burden and unresectable sites. MRI and FDG PET/CT showed higher per-patient sensitivity than MDCT in a meta-analysis (33 studies, 487 women); MRI vs MDCT p=0.03, PET/CT vs MDCT p<0.01; MRI vs PET/CT p=0.84. Histologic confirmation is recommended before neoadjuvant chemotherapy. Diagnostic laparoscopy with Fagotti/laparoscopic predictive index assessment is highlighted as the most specific approach to identify patients unlikely to achieve optimal cytoreduction. The Peritoneal Cancer Index (PCI; 13 abdominopelvic regions) quantifies tumor burden and has prognostic value. CA-125 is useful but limited alone for predicting resectability. | ASCO update 2025 https://doi.org/10.1200/jco-24-02589; Perez-Fidalgo 2024 https://doi.org/10.1007/s12094-024-03531-3; Tsili 2024 https://doi.org/10.3390/cancers16081467; Ghirardi 2023 https://doi.org/10.3390/cancers15020407; Rizzo 2025 https://doi.org/10.1007/s00330-024-11300-7 |
| Molecular biomarkers and clinical use | BRCA1/2: predictive for platinum/PARP inhibitor benefit; maintenance selection. HRD: central biomarker for PARP inhibitor maintenance; prevalence varies across trials and assays; clinically relevant in first-line maintenance selection. TP53: near-ubiquitous hallmark of high-grade serous disease and useful as a molecular disease-defining feature rather than a routine therapy-selection biomarker. FRα: biomarker for mirvetuximab eligibility in platinum-resistant disease; MIRASOL required ≥75% of cells with ≥2+ staining intensity, and SORAYA enrolled FRα-high tumors. Open Targets disease associations prominently include BRCA1, BRCA2, RAD51C, TP53, RAD51D, BRIP1, PALB2, MSH2, and MSH6. | Paik 2023 https://doi.org/10.3390/cancers15123095; Moore 2023 https://doi.org/10.1056/NEJMoa2309169; Matulonis 2023 https://doi.org/10.1200/jco.22.01900; Open Targets context |
| Standard first-line treatment backbone | Standard treatment combines cytoreductive surgery and platinum-taxane chemotherapy. Typical first-line regimen is carboplatin plus paclitaxel every 3 weeks for 6 cycles. Goal of surgery is no gross residual disease. | Ghirardi 2023 https://doi.org/10.3390/cancers15020407; Caruso 2025 review excerpt |
| Primary debulking surgery (PDS) vs neoadjuvant chemotherapy (NACT-IDS) | PDS is preferred when complete or near-complete cytoreduction is feasible with acceptable morbidity; NACT followed by interval debulking is favored when complete upfront cytoreduction is unlikely or perioperative risk is high. EORTC-55971 (670 patients): median OS 29 vs 30 months (PDS vs NACT-IDS). CHORUS (550 patients): median OS 22.8 vs 24.5 months. Pooled analysis in FIGO stage IV: median OS 21.2 vs 24.3 months and median PFS 9.7 vs 10.6 months, favoring NACT-IDS. SCORPION (171 patients): median PFS 15 vs 14 months and median OS 41 vs 43 months, with less morbidity for NACT-IDS. | Ghirardi 2023 https://doi.org/10.3390/cancers15020407; ASCO update 2025 https://doi.org/10.1200/jco-24-02589 |
| HIPEC | In selected stage III patients treated with NACT/interval surgery, HIPEC may be offered in experienced centers. Randomized data cited in review: cisplatin 100 mg/m2 at IDS improved PFS 14.2 vs 10.7 months and OS 45.7 vs 33.9 months; meta-analysis HR 0.585 for PFS and HR 0.519 for OS. | Ghirardi 2023 https://doi.org/10.3390/cancers15020407; ASCO update 2025 https://doi.org/10.1200/jco-24-02589 |
| Bevacizumab | Added to chemotherapy then continued as maintenance, bevacizumab prolonged PFS in major first-line trials: GOG-0218 14.1 vs 10.3 months; ICON7 24.1 vs 22.4 months. In a high-risk subgroup, ICON7 OS was 39.3 vs 34.5 months (HR 0.78). | Caruso 2025 review excerpt; Ghirardi 2023 https://doi.org/10.3390/cancers15020407 |
| PARP inhibitor maintenance | PARP inhibitors are central maintenance options after response to first-line platinum, particularly in BRCA-mutated/HRD-positive disease. SOLO-1: olaparib reduced risk of progression/death by 70% (HR 0.30, 95% CI 0.23–0.41); median PFS not reached vs 13.8 months at 41-month follow-up. Seven-year SOLO-1 OS data reported in review excerpt: 67.0% vs 46.5%; median OS not reached vs 75.2 months; HR 0.55 (95% CI 0.40–0.76). | Ghirardi 2023 https://doi.org/10.3390/cancers15020407; Caruso 2025 review excerpt; Paik 2023 https://doi.org/10.3390/cancers15123095 |
| Mirvetuximab soravtansine: SORAYA | Biomarker-selected option for FRα-high platinum-resistant ovarian cancer after prior bevacizumab. SORAYA enrolled 106 patients; 105 efficacy-evaluable; 51% had 3 prior lines; 48% prior PARP inhibitor. ORR 32.4% (95% CI 23.6–42.2), including 5 complete and 29 partial responses; median duration of response 6.9 months (95% CI 5.6–9.7); final median OS 15.0 months (95% CI 11.5–18.7). Common treatment-related adverse events: blurred vision 41% (grade 3–4: 6%), keratopathy 29% (grade 3–4: 9%), nausea 29% (grade 3–4: 0%). | Matulonis 2023 https://doi.org/10.1200/jco.22.01900; Coleman 2024 https://doi.org/10.1136/ijgc-2024-005401 |
| Mirvetuximab soravtansine: MIRASOL | Phase 3 confirmatory trial in FRα-positive platinum-resistant high-grade serous ovarian cancer (453 randomized; 227 MIRV, 226 chemotherapy). Median PFS 5.62 vs 3.98 months; ORR 42.3% vs 15.9%; median OS 16.46 vs 12.75 months; grade ≥3 adverse events 41.7% vs 54.1%; serious adverse events 23.9% vs 32.9%; discontinuations 9.2% vs 15.9%. | Moore 2023 https://doi.org/10.1056/NEJMoa2309169 |
| Prognosis / survival context | Most ovarian cancers present at advanced stage; approximately 75% present advanced and advanced-stage 5-year survival is generally poor. Review excerpts cite overall 5-year survival of roughly 10–40% for advanced-stage disease; stage-specific SEER-derived figures in one study were 17% 5-year relative survival for stage IV. High PCI predicts worse survival with pooled HR 2.79 for OS and 1.89 for PFS in advanced disease. | Ghirardi 2023 https://doi.org/10.3390/cancers15020407; Zhang 2024 https://doi.org/10.1186/s12905-024-03199-5; Wang 2024 https://doi.org/10.3389/fonc.2024.1421828; Caruso 2025 review excerpt |


*Table: This table condenses identifiers, staging, diagnostic workup, biomarkers, and major treatment trial metrics for metastatic/advanced epithelial ovarian cancer. It is designed as a quick-reference artifact for knowledge base population and narrative synthesis.*

## References (URLs and publication dates)
* Ghirardi V, et al. **Diagnostic and Therapeutic Pathway of Advanced Ovarian Cancer with Peritoneal Metastases**. *Cancers*. 2023-01. https://doi.org/10.3390/cancers15020407 (ghirardi2023diagnosticandtherapeutic pages 1-2)
* Tsili AC, et al. **Imaging of Peritoneal Metastases in Ovarian Cancer Using MDCT, MRI, and FDG PET/CT: A Systematic Review and Meta-Analysis**. *Cancers*. 2024-04. https://doi.org/10.3390/cancers16081467 (tsili2024imagingofperitoneal pages 1-2)
* Pérez-Fidalgo JA, et al. **SEOM–GEICO clinical guideline on epithelial ovarian cancer (2023)**. *Clin Transl Oncol*. 2024-07. https://doi.org/10.1007/s12094-024-03531-3 (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)
* Métairie M, et al. **A Suggested Modification to FIGO Stage IV Epithelial Ovarian Cancer**. *Cancers*. 2023-01. https://doi.org/10.3390/cancers15030706 (metairie2023asuggestedmodification pages 11-12)
* Matulonis UA, et al. **SORAYA** results. *J Clin Oncol*. 2023-05. https://doi.org/10.1200/JCO.22.01900 (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)
* Moore KN, et al. **MIRASOL**. *N Engl J Med*. 2023-12. https://doi.org/10.1056/NEJMoa2309169 (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)
* Coleman RL, et al. SORAYA final OS. *Int J Gynecol Cancer*. 2024-06. https://doi.org/10.1136/ijgc-2024-005401 (perezfidalgo2024seom–geicoclinicalguideline pages 1-2)
* Li R, et al. **Global epidemiology of ovarian cancer: patterns, trends, and risk factors**. *Cancer Biol Med*. 2026-03. https://doi.org/10.20892/j.issn.2095-3941.2025.0619 (li2026globalepidemiologyof pages 1-2)
* Open Targets disease–gene associations for ovarian cancer (MONDO_0008170). https://platform.opentargets.org/ (OpenTargets Search: metastatic ovarian cancer,ovarian carcinoma)


References

1. (ghirardi2023diagnosticandtherapeutic pages 1-2): Valentina Ghirardi, Anna Fagotti, Luca Ansaloni, Mario Valle, Franco Roviello, Lorena Sorrentino, Fabio Accarpio, Gianluca Baiocchi, Lorenzo Piccini, Michele De Simone, Federico Coccolini, Mario Visaloco, Stefano Bacchetti, Giovanni Scambia, and Daniele Marrelli. Diagnostic and therapeutic pathway of advanced ovarian cancer with peritoneal metastases. Cancers, 15:407, Jan 2023. URL: https://doi.org/10.3390/cancers15020407, doi:10.3390/cancers15020407. This article has 18 citations.

2. (perezfidalgo2024seom–geicoclinicalguideline pages 1-2): Jose Alejandro Perez-Fidalgo, Fernando Gálvez-Montosa, Eva María Guerra, Ainhoa Madariaga, Aranzazu Manzano, Cristina Martin-Lorente, Maria Jesús Rubio-Pérez, Jesus Alarcón, María Pilar Barretina-Ginesta, and Lydia Gaba. Seom–geico clinical guideline on epithelial ovarian cancer (2023). Clinical & Translational Oncology, 26:2758-2770, Jul 2024. URL: https://doi.org/10.1007/s12094-024-03531-3, doi:10.1007/s12094-024-03531-3. This article has 18 citations and is from a peer-reviewed journal.

3. (tsili2024imagingofperitoneal pages 1-2): Athina C. Tsili, George Alexiou, Martha Tzoumpa, Timoleon Siempis, and Maria I. Argyropoulou. Imaging of peritoneal metastases in ovarian cancer using mdct, mri, and fdg pet/ct: a systematic review and meta-analysis. Cancers, 16:1467, Apr 2024. URL: https://doi.org/10.3390/cancers16081467, doi:10.3390/cancers16081467. This article has 17 citations.

4. (ghirardi2023diagnosticandtherapeutic pages 5-7): Valentina Ghirardi, Anna Fagotti, Luca Ansaloni, Mario Valle, Franco Roviello, Lorena Sorrentino, Fabio Accarpio, Gianluca Baiocchi, Lorenzo Piccini, Michele De Simone, Federico Coccolini, Mario Visaloco, Stefano Bacchetti, Giovanni Scambia, and Daniele Marrelli. Diagnostic and therapeutic pathway of advanced ovarian cancer with peritoneal metastases. Cancers, 15:407, Jan 2023. URL: https://doi.org/10.3390/cancers15020407, doi:10.3390/cancers15020407. This article has 18 citations.

5. (caruso2025ovariancancera pages 8-9): G Caruso, SJ Weroha, and W Cliby. Ovarian cancer: a review. Unknown journal, 2025.

6. (ghirardi2023diagnosticandtherapeutic pages 7-8): Valentina Ghirardi, Anna Fagotti, Luca Ansaloni, Mario Valle, Franco Roviello, Lorena Sorrentino, Fabio Accarpio, Gianluca Baiocchi, Lorenzo Piccini, Michele De Simone, Federico Coccolini, Mario Visaloco, Stefano Bacchetti, Giovanni Scambia, and Daniele Marrelli. Diagnostic and therapeutic pathway of advanced ovarian cancer with peritoneal metastases. Cancers, 15:407, Jan 2023. URL: https://doi.org/10.3390/cancers15020407, doi:10.3390/cancers15020407. This article has 18 citations.

7. (OpenTargets Search: metastatic ovarian cancer,ovarian carcinoma): Open Targets Query (metastatic ovarian cancer,ovarian carcinoma, 43 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (caruso2025ovariancancera pages 3-3): G Caruso, SJ Weroha, and W Cliby. Ovarian cancer: a review. Unknown journal, 2025.

9. (days2025ovariancancerrisk pages 2-4): Flora Days and Edith Caroline Smith. Ovarian cancer risk assessment, risk reduction, and early detection. Clinical Journal for Nurse Practitioners in Women's Health, 2:6-12, Jan 2025. URL: https://doi.org/10.1891/cjnpwh-2506, doi:10.1891/cjnpwh-2506. This article has 0 citations.

10. (li2026globalepidemiologyof pages 5-7): Ruyuan Li, Anqi Zhao, Meicen Liu, Lingeng Lu, Bin Li, and Hongmei Zeng. Global epidemiology of ovarian cancer: patterns, trends, and risk factors. Cancer Biology &amp; Medicine, pages 1-16, Mar 2026. URL: https://doi.org/10.20892/j.issn.2095-3941.2025.0619, doi:10.20892/j.issn.2095-3941.2025.0619. This article has 0 citations.

11. (masouleh2024exploringopportunisticsalpingectomy pages 19-23): Z Masouleh. Exploring opportunistic salpingectomy as a preventive strategy for ovarian cancer: uptake in newfoundland and labrador, canada. Unknown journal, 2024.

12. (metairie2023asuggestedmodification pages 11-12): Marie Métairie, Louise Benoit, Meriem Koual, Enrica Bentivegna, Henri Wohrer, Pierre-Adrien Bolze, Yohan Kerbage, Emilie Raimond, Cherif Akladios, Xavier Carcopino, Geoffroy Canlorbe, Jennifer Uzan, Vincent Lavoué, Camille Mimoun, Cyrille Huchon, Martin Koskas, Hélène Costaz, François Margueritte, Yohann Dabi, Cyril Touboul, Sofiane Bendifallah, Lobna Ouldamer, Nicolas Delanoy, Huyen-Thu Nguyen-Xuan, Anne-Sophie Bats, and Henri Azaïs. A suggested modification to figo stage iv epithelial ovarian cancer. Cancers, 15:706, Jan 2023. URL: https://doi.org/10.3390/cancers15030706, doi:10.3390/cancers15030706. This article has 8 citations.

13. (caruso2025ovariancancera pages 2-3): G Caruso, SJ Weroha, and W Cliby. Ovarian cancer: a review. Unknown journal, 2025.

14. (li2026globalepidemiologyof pages 1-2): Ruyuan Li, Anqi Zhao, Meicen Liu, Lingeng Lu, Bin Li, and Hongmei Zeng. Global epidemiology of ovarian cancer: patterns, trends, and risk factors. Cancer Biology &amp; Medicine, pages 1-16, Mar 2026. URL: https://doi.org/10.20892/j.issn.2095-3941.2025.0619, doi:10.20892/j.issn.2095-3941.2025.0619. This article has 0 citations.

15. (caruso2025ovariancancera pages 8-8): G Caruso, SJ Weroha, and W Cliby. Ovarian cancer: a review. Unknown journal, 2025.

16. (ghirardi2023diagnosticandtherapeutic media b74131ac): Valentina Ghirardi, Anna Fagotti, Luca Ansaloni, Mario Valle, Franco Roviello, Lorena Sorrentino, Fabio Accarpio, Gianluca Baiocchi, Lorenzo Piccini, Michele De Simone, Federico Coccolini, Mario Visaloco, Stefano Bacchetti, Giovanni Scambia, and Daniele Marrelli. Diagnostic and therapeutic pathway of advanced ovarian cancer with peritoneal metastases. Cancers, 15:407, Jan 2023. URL: https://doi.org/10.3390/cancers15020407, doi:10.3390/cancers15020407. This article has 18 citations.

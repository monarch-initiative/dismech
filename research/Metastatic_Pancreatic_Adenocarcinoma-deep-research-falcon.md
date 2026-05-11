---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T01:48:52.671814'
end_time: '2026-05-10T02:08:35.525254'
duration_seconds: 1182.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Pancreatic Adenocarcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metastatic Pancreatic Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Pancreatic Adenocarcinoma** covering all of the
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
- **Disease Name:** Metastatic Pancreatic Adenocarcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Pancreatic Adenocarcinoma** covering all of the
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


## Comprehensive Research Report: Metastatic Pancreatic Adenocarcinoma (Metastatic PDAC)

### Target disease
Metastatic pancreatic adenocarcinoma typically refers to **pancreatic ductal adenocarcinoma (PDAC)** with **distant metastasis (stage IV; M1)**—most commonly to liver, but also peritoneum, lung, and other sites. PDAC is the dominant pancreatic cancer histology (often cited as ~90–95% of pancreatic cancers) and is characterized by late diagnosis and very poor prognosis. (dalessandro2024newapproachesto pages 6-10)

**Evidence type note:** Much of the definitional/overview content here comes from aggregated disease-level reviews and large registries (e.g., SEER/ACS statistics). Some mechanistic and microenvironment findings derive from primary human single-cell studies and from model systems. (park2024singlecelltranscriptomeanalysis pages 1-2, zhang2023singlecelltranscriptomic pages 1-2, siegel2024cancerstatistics2024 pages 12-12)

### 1. Disease Information
#### Concise overview
PDAC is described as highly lethal, with most patients presenting with advanced (unresectable/metastatic) disease and limited durable responses to systemic therapy, in part due to tumor heterogeneity and an immunosuppressive microenvironment. (netto2024systemictherapyfor pages 1-2, zhang2023singlecelltranscriptomic pages 1-2)

#### Key identifiers (available from retrieved sources)
* **ICD-10:** C25 (pancreas) is used in registry studies for pancreatic cancer (not PDAC-specific in all registries). (siegel2024cancerstatistics2024 pages 30-31)

> Limitation: In the retrieved corpus for this run, I did not obtain authoritative mappings for **MONDO** and **MeSH** identifiers specific to *metastatic PDAC*; these should be added from MONDO/MeSH/ICD-11 lookups in a subsequent curation pass.

#### Common synonyms / alternative names
* Pancreatic ductal adenocarcinoma (PDAC)
* Pancreatic adenocarcinoma (when histology is ductal)
* Metastatic pancreatic cancer (commonly PDAC)

### 2. Etiology
#### Primary causal factors (mechanistic)
PDAC evolves through precursor lesions (e.g., PanIN) with stepwise accumulation of oncogenic and tumor suppressor alterations, classically involving **KRAS activation** early, followed by alterations such as **CDKN2A**, and later **TP53, SMAD4, BRCA2** in progression toward invasive cancer. (dalessandro2024newapproachesto pages 10-13, paton2019computationalapproachesfor pages 30-33)

#### Risk factors (selected quantitative recent synthesis)
A 2024 metastatic-PDAC systemic therapy review summarizes epidemiologic risk associations (citing meta-analyses) including:
* **Cigarette smoking**: RR ~ **3.0** vs never smokers. (netto2024systemictherapyfor pages 1-2)
* **Type 2 diabetes mellitus**: OR ~ **2.39** in one meta-analysis (noting variability/confounding). (netto2024systemictherapyfor pages 1-2)
* **Obesity**: risk highest at **BMI > 35**, OR ~ **1.62**. (netto2024systemictherapyfor pages 1-2)
* **Familial pancreatic cancer**: two first-degree relatives RR ~ **6.4**. (netto2024systemictherapyfor pages 1-2)
* **Lynch syndrome / MMR deficiency**: RR ~ **8.6** by age 70 (as summarized). (netto2024systemictherapyfor pages 1-2)

#### Protective factors
A large, 2024 systematic review/meta-analysis found higher physical activity associated with lower pancreatic cancer risk (e.g., cohort summary estimate 0.91 for highest vs lowest activity), suggesting lifestyle-level protective association; however, this is not metastatic-specific and was not retrieved in full-text evidence snippets in this run. (not in evidence excerpts)

#### Gene–environment interactions
Direct gene–environment interaction quantification was not captured in the retrieved evidence set for this run; nevertheless, the co-occurrence of inherited predisposition (e.g., BRCA2/Lynch) with modifiable exposures (smoking/obesity/diabetes) is widely recognized as clinically relevant for risk stratification. (netto2024systemictherapyfor pages 1-2)

### 3. Phenotypes
#### Core clinical phenotypes (metastatic PDAC)
Patients may present with sequelae including **jaundice**, **biliary sepsis**, **abdominal pain** (including celiac plexus-related pain), and **malnourishment**, which can limit ability to deliver systemic therapy. (netto2024systemictherapyfor pages 1-2)

#### Metastatic patterns
* **Liver** is repeatedly highlighted as a predominant/most common metastatic site in PDAC, and liver metastasis is a key driver of mortality. (zhang2023singlecelltranscriptomic pages 1-2, bojmar2024multiparametricatlasof pages 7-9)
* In a treatment-naïve single-cell cohort including stage IV patients, liver metastasis predominated among metastatic cases (13/15 stage IV had liver metastasis). (park2024singlecelltranscriptomeanalysis pages 1-2)

#### Suggested HPO terms (examples)
* Jaundice — **HP:0000952**
* Abdominal pain — **HP:0002027**
* Weight loss — **HP:0001824**
* Malnutrition — **HP:0004395**
* Biliary tract infection / cholangitis (if present) — consider **HP:0006588** (Cholangitis)
* Liver metastasis (as a phenotype/clinical finding) — can be represented via disease extension terms in oncology ontologies; HPO has metastatic neoplasm terms (e.g., **HP:0030970 Metastatic neoplasm**) plus anatomic context.

> Limitation: Phenotype frequencies (e.g., % jaundice) were not available from the retrieved primary sources in this run.

### 4. Genetic / Molecular Information
#### Major somatic drivers (current understanding)
PDAC is commonly driven by **KRAS** mutation with frequent tumor suppressor inactivation (**TP53**, **CDKN2A**, **SMAD4**). (dalessandro2024newapproachesto pages 6-10)

#### Actionable / clinically relevant molecular subsets (examples)
1. **Homologous recombination repair deficiency (HRD), germline BRCA1/2**
   * Maintenance **olaparib** after platinum response improves **PFS** in germline BRCA-mutated metastatic pancreatic cancer: median PFS **7.4 vs 3.8 months**; HR **0.53**; P=0.004. (golan2019maintenanceolaparibfor pages 4-5)
   * Final OS analysis reported no statistically significant OS difference; interim OS analysis cited median OS **18.9 vs 18.1 months**, HR 0.91. (kindler2022overallsurvivalresults pages 2-3, roth2020recentadvancesin pages 4-5)
2. **Mismatch repair deficiency / MSI-H (rare, but important)**
   * In a Guardant360 ctDNA cohort, MSI-H was detected in **0.8%** (52/>6000) PDAC cases; among MSI-H PDAC patients treated with immune checkpoint inhibitor, RECIST ORR was **77%** (7/9) and median PFS/OS were not reached. (chakrabarti2022detectionofmicrosatellite pages 2-3)
   * Tissue-agnostic approval context for pembrolizumab in MSI-H/dMMR tumors is summarized in treatment review evidence. (roth2020recentadvancesin pages 4-5)

#### Molecular subtypes and prognosis (single-cell evidence)
Single-cell profiling of primary tumors with paired liver metastases indicates that **basal-like malignant ductal cells** can be prognostically important: even ~**22% basal-like** fraction was associated with poor chemotherapy response and survival, and basal-like fraction correlated negatively with cytotoxic T cells and positively with Tregs. (park2024singlecelltranscriptomeanalysis pages 1-2, park2024singlecelltranscriptomeanalysis pages 2-5)

#### Suggested variant examples (illustrative; from retrieved evidence)
* Germline **BRCA1/2** deleterious variants (POLO eligibility) (kindler2022overallsurvivalresults pages 2-3)

> Limitation: Specific HGVS variant nomenclature and allele frequencies (gnomAD) were not captured in retrieved evidence snippets.

### 5. Environmental Information
Key environmental/lifestyle factors implicated in PDAC risk include smoking and metabolic factors (obesity/diabetes). (netto2024systemictherapyfor pages 1-2)

### 6. Mechanism / Pathophysiology
#### Tumor microenvironment (TME) and immune evasion
A central theme across multiple sources is that PDAC has a **highly immunosuppressive TME** that contributes to resistance to immunotherapy and progression, and that metastatic lesions (e.g., liver metastases) have distinct immune/stromal cell programs. (zhang2023singlecelltranscriptomic pages 1-2, dalessandro2024newapproachesto pages 6-10)

Single-cell analysis of matched primary tumors and liver metastases identified immunosuppressive stromal/immune populations in metastases, including (verbatim from abstract) **“RGS5+ cancer-associated fibroblasts, CCL18+ lipid-associated macrophages, S100A8+ neutrophils and FOXP3+ regulatory T cells”**, and suggested that reduced tumor–immune interactions contribute to immunosuppression in metastases. (zhang2023singlecelltranscriptomic pages 1-2)

In Park et al. 2024, immunosuppressive Treg states (SELLhi and TIGIThi) and subtype-linked immune patterns were implicated in metastatic evolution. (park2024singlecelltranscriptomeanalysis pages 1-2)

#### Pre-metastatic niche (liver)
A multi-omics atlas of pre-metastatic liver biopsies in localized pancreatic cancer showed liver inflammatory/immune and metabolic signatures that could predict recurrence patterns, with a machine-learning model reporting **78% overall accuracy** and **90% accuracy for early liver metastasis**. (bojmar2024multiparametricatlasof pages 1-2, bojmar2024multiparametricatlasof pages 7-9)

#### Suggested ontology mappings (examples)
* **GO biological process**
  * epithelial–mesenchymal transition — GO:0001837
  * immune evasion / negative regulation of immune response — GO:0050777 (negative regulation of immune response)
  * extracellular matrix organization — GO:0030198
* **Cell Ontology (CL) cell types**
  * regulatory T cell — CL:0000815
  * cytotoxic T cell — CL:0000910
  * macrophage — CL:0000235
  * neutrophil — CL:0000775
  * cancer-associated fibroblast — (not always a single CL term; map to fibroblast CL:0000057 with CAF context)
* **UBERON**
  * pancreas — UBERON:0001264
  * liver — UBERON:0002107

### 7. Diagnostics
#### Imaging and biopsy
Metastatic PDAC diagnosis relies on imaging (CT/MRI/PET as clinically indicated) with histopathologic confirmation when needed; this is standard practice but not detailed quantitatively in the retrieved evidence.

#### Biomarkers
* **CA19-9**: Not validated for screening, but may support diagnosis in the context of suspicious imaging (summarized in review). (mack2025pancreaticcancerepidemiology pages 10-12)
* **ctDNA / liquid biopsy for MSI-H**: Plasma MSI-H detection can identify PDAC patients likely to respond to immune checkpoint inhibitors; in the Guardant360 cohort described above, plasma MSI-H detection was clinically predictive of robust responses. (chakrabarti2022detectionofmicrosatellite pages 2-3)

#### Molecular testing (precision oncology)
Contemporary guideline-aligned practice increasingly emphasizes germline testing and tumor molecular profiling in advanced/unresectable PDAC to identify actionable subgroups (e.g., BRCA/HRD; MSI-H). (mack2025pancreaticcancerepidemiology pages 10-12, roth2020recentadvancesin pages 4-5)

### 8. Treatment
#### Current standard first-line cytotoxic options (metastatic PDAC)
Chemotherapy remains the backbone of care, with widely used regimens including **FOLFIRINOX** and **gemcitabine + nab-paclitaxel**. (mack2025pancreaticcancerepidemiology pages 10-12)

#### Recent developments (prioritizing 2023–2024)
**NALIRIFOX (liposomal irinotecan + oxaliplatin + leucovorin + fluorouracil)**
* A 2024 review notes: “**The NAPOLI-3 trial has reported data supporting consideration of NALIRIFOX as a new first-line standard of care**.” (netto2024systemictherapyfor pages 1-2)
* A 2025 plain-language summary of NAPOLI-3 states the study “**showed that NALIRIFOX increased survival time and the length of time it took for the cancer to worsen compared with GemNabPac**” and that “**In early 2024, NALIRIFOX was approved**” by FDA and EMA for untreated metastatic PDAC. (park2024singlecelltranscriptomeanalysis pages 1-2)

**Biomarker-driven therapies**
1) **Maintenance olaparib** (gBRCA metastatic PDAC after platinum response)
* Median PFS **7.4 vs 3.8 months**, HR 0.53. (golan2019maintenanceolaparibfor pages 4-5)
* OS not significantly different in final report; interim OS **18.9 vs 18.1 months** (as cited). (kindler2022overallsurvivalresults pages 2-3, roth2020recentadvancesin pages 4-5)

2) **Immune checkpoint inhibitors (pembrolizumab) for MSI-H/dMMR PDAC (rare subset)**
* Plasma MSI-H PDAC case series with ICIs showed ORR **77%**, durable responses in many responders, and MSI-H prevalence ~0.8% in tested PDAC. (chakrabarti2022detectionofmicrosatellite pages 2-3)
* A treatment review summarizes KEYNOTE-158 pancreatic subgroup: among 22 PDAC patients, ORR **18.2%**, mPFS **2.1 months**, mOS **4.0 months** (illustrating that MSI-H PDAC remains uncommon and outcomes vary by cohort). (roth2020recentadvancesin pages 4-5)

#### Supportive/palliative care
For advanced solid tumors, early specialized palliative care involvement is recommended by ASCO guideline update (not PDAC-specific but applicable to metastatic PDAC). (roth2020recentadvancesin pages 5-6)

#### Suggested MAXO terms (examples)
* Combination chemotherapy regimen — MAXO:0000058 (chemotherapy; map regimen as a combination)
* Maintenance therapy with PARP inhibitor — MAXO: (PARP inhibitor therapy; ontology mapping needs curation)
* Immune checkpoint inhibitor therapy — MAXO:0001270 (immunotherapy; checkpoint inhibitor subterm may exist)
* Palliative care — MAXO:0000603

> Limitation: This run’s retrieved corpus did not include the primary NAPOLI-3 Lancet paper full text; therefore, specific OS/PFS hazard ratios and medians for NALIRIFOX vs Gem+nab-paclitaxel are not quoted numerically here.

### 9. Prevention
#### High-risk surveillance (2024 primary evidence)
Population screening is not recommended for average-risk individuals, but surveillance for high-risk cohorts can shift stage at diagnosis and improve outcomes.

In a multi-center CAPS-associated cohort study comparing **26 surveillance-detected high-risk PDACs** with **1504 SEER matched controls**, surveillance was associated with:
* More stage I cancers (**38.5% vs 10.3%**) and fewer distant metastases at diagnosis (**26.9% vs 53.8%**). (blackford2024pancreaticcancersurveillance pages 1-2, blackford2024pancreaticcancersurveillance pages 5-6)
* Markedly longer median OS (**61.7 vs 8.0 months**) and higher 5-year OS (**50% vs 9%**), with lower 5-year PDAC-specific mortality (**43% vs 86%**). (blackford2024pancreaticcancersurveillance pages 1-2, blackford2024pancreaticcancersurveillance media 731b7f36)

#### New-onset diabetes as an early-detection signal
Review evidence notes that new-onset diabetes in adults >50 years may warrant evaluation because a subset will be diagnosed with PDAC within ~3 years (reported ~0.4–0.8% in the cited review). (mack2025pancreaticcancerepidemiology pages 10-12)

### 10. Other species / natural disease
Not evaluated in the retrieved evidence set for this run.

### 11. Model organisms / model systems
PDAC mechanistic work often relies on genetically engineered mouse models (e.g., KPC) and patient-derived systems.

**Organoids (patient-derived organoids; PDOs)** are highlighted as a clinically relevant precision-medicine platform; PDO “pharmacotyping” and sequencing after biomass expansion can improve mutation detection and predict chemotherapy response (e.g., declines in CA19-9 and RECIST responses in neoadjuvant settings). (roth2020recentadvancesin pages 5-6)

### 12. Recent statistics and data (quick-reference table)
| Topic | Finding (numeric) | Population/Setting | Source (first author, year, journal) | URL | Notes (e.g., biomarker subset) |
|---|---:|---|---|---|---|
| surveillance | Stage I 38.5% (10/26); Stage II 30.8% (8/26) vs matched SEER Stage I 10.3% (155/1504); Stage II 25.1% (377/1504) | High-risk individuals under CAPS surveillance vs matched SEER PDAC controls | Blackford, 2024, *JAMA Oncology* | https://doi.org/10.1001/jamaoncol.2024.1930 | Lower stage at diagnosis in surveillance cohort (blackford2024pancreaticcancersurveillance pages 1-2, blackford2024pancreaticcancersurveillance pages 5-6) |
| surveillance | Distant metastasis at diagnosis 26.9% (7/26) vs 53.8% (809/1504) | High-risk surveillance cohort vs matched SEER controls | Blackford, 2024, *JAMA Oncology* | https://doi.org/10.1001/jamaoncol.2024.1930 | Fewer M1 cases with surveillance (blackford2024pancreaticcancersurveillance pages 5-6) |
| surveillance | Median OS 61.7 months vs 8.0 months; 5-year OS 50% vs 9% | High-risk surveillance cohort vs matched SEER controls | Blackford, 2024, *JAMA Oncology* | https://doi.org/10.1001/jamaoncol.2024.1930 | Overall survival advantage with selective surveillance (blackford2024pancreaticcancersurveillance pages 1-2, blackford2024pancreaticcancersurveillance pages 5-6, blackford2024pancreaticcancersurveillance media 731b7f36) |
| surveillance | 5-year PDAC-specific mortality 43% vs 86% | High-risk surveillance cohort vs matched SEER controls | Blackford, 2024, *JAMA Oncology* | https://doi.org/10.1001/jamaoncol.2024.1930 | Cancer-specific mortality lower in surveillance cohort (blackford2024pancreaticcancersurveillance pages 1-2, blackford2024pancreaticcancersurveillance pages 5-6, blackford2024pancreaticcancersurveillance media 731b7f36) |
| therapy | MSI-H prevalence 0.8% (52/>6000 tested); ORR 77% (7/9); 78% alive at cutoff (7/9) | PDAC patients with MSI-H detected by Guardant360 liquid biopsy; 9 treated with ICI | Chakrabarti, 2022, *Journal for ImmunoTherapy of Cancer* | https://doi.org/10.1136/jitc-2021-004485 | Plasma-detected MSI-H subset; median PFS and OS not reached; metastatic disease in 80% of cohort (chakrabarti2022detectionofmicrosatellite pages 2-3) |
| therapy | Median PFS 7.4 vs 3.8 months; HR 0.53 (95% CI 0.35-0.82); P=0.004 | gBRCA-mutated metastatic pancreatic cancer without progression after ≥16 weeks first-line platinum | Golan, 2019, *New England Journal of Medicine* | https://doi.org/10.1056/NEJMoa1903387 | POLO maintenance olaparib vs placebo (golan2019maintenanceolaparibfor pages 4-5) |
| therapy | Interim median OS 18.9 vs 18.1 months; HR 0.91 (95% CI 0.56-1.46); P=.68 | Same POLO randomized population at primary PFS data cutoff | Kindler, 2022, *Journal of Clinical Oncology* | https://doi.org/10.1200/JCO.21.01604 | Final OS paper reporting prior interim OS analysis (kindler2022overallsurvivalresults pages 2-3) |
| risk factor | Smoking RR 3.0 | Pancreatic cancer risk factors review | Netto, 2024, *Current Oncology* | https://doi.org/10.3390/curroncol31090385 | Most significant modifiable risk factor listed in review (netto2024systemictherapyfor pages 1-2) |
| risk factor | Type 2 diabetes OR 2.39 | Pancreatic cancer risk factors review | Netto, 2024, *Current Oncology* | https://doi.org/10.3390/curroncol31090385 | Meta-analysis estimate cited in review (netto2024systemictherapyfor pages 1-2) |
| risk factor | BMI >35 OR 1.62 | Pancreatic cancer risk factors review | Netto, 2024, *Current Oncology* | https://doi.org/10.3390/curroncol31090385 | Obesity-associated risk estimate (netto2024systemictherapyfor pages 1-2) |
| risk factor | Family history RR 6.4 | Two first-degree relatives with PDAC | Netto, 2024, *Current Oncology* | https://doi.org/10.3390/curroncol31090385 | Familial pancreatic cancer risk estimate (netto2024systemictherapyfor pages 1-2) |
| risk factor | Lynch syndrome RR 8.6 by age 70 | Inherited susceptibility setting | Netto, 2024, *Current Oncology* | https://doi.org/10.3390/curroncol31090385 | MMR-deficient hereditary risk estimate (netto2024systemictherapyfor pages 1-2) |
| epidemiology/prognosis | 80% present with metastatic or unresectable disease | PDAC overall presentation pattern | Netto, 2024, *Current Oncology* | https://doi.org/10.3390/curroncol31090385 | Review framing advanced disease burden (netto2024systemictherapyfor pages 1-2) |
| epidemiology/prognosis | 5-year survival rate ~10% | PDAC overall | Netto, 2024, *Current Oncology* | https://doi.org/10.3390/curroncol31090385 | Review summary statistic (netto2024systemictherapyfor pages 1-2) |
| epidemiology/prognosis | Stage III 29% (6/21); Stage IV 71% (15/21); liver metastasis in 13/15 stage IV; median OS 9.7 months (range 0.6-47.8) | Treatment-naive primary PDAC with and without paired liver metastasis samples | Park, 2024, *Molecular Cancer* | https://doi.org/10.1186/s12943-024-02003-0 | Single-cell cohort informing metastatic evolution and TME (park2024singlecelltranscriptomeanalysis pages 1-2) |
| epidemiology/prognosis | Basal-like malignant ductal cell proportion as low as 22% associated with poor survival; multivariable HR 24.9 (95% CI 2.02-310), P=0.012 | Combined scRNA-seq cohorts / deconvoluted TCGA PDAC data | Park, 2024, *Molecular Cancer* | https://doi.org/10.1186/s12943-024-02003-0 | Prognostic molecular subtype signal, relevant to metastatic behavior and chemotherapy response (park2024singlecelltranscriptomeanalysis pages 2-5) |
| epidemiology/prognosis | 5-year survival below 10%; distant metastasis at initial diagnosis >80% | PDAC with matched primary tumors and liver metastases | Zhang, 2023, *Nature Communications* | https://doi.org/10.1038/s41467-023-40727-7 | Single-cell liver metastasis study describing metastatic burden (zhang2023singlecelltranscriptomic pages 1-2) |
| epidemiology/prognosis | Incident pancreatic cancer cases projected in US 2024: 66,440; deaths: 51,750 | United States, all pancreatic cancer | Siegel, 2024, *CA: A Cancer Journal for Clinicians* | https://doi.org/10.3322/caac.21820 | Broader population context for burden; not metastatic-specific (siegel2024cancerstatistics2024 pages 12-12, siegel2024cancerstatistics2024 pages 30-31) |
| epidemiology/prognosis | Pancreas incidence rising 0.6%-1.0% annually during 2015-2019 | United States incidence trends | Siegel, 2024, *CA: A Cancer Journal for Clinicians* | https://doi.org/10.3322/caac.21820 | Population trend relevant to rising PDAC burden (siegel2024cancerstatistics2024 pages 12-12) |
| mechanism/prognosis | Prediction model accuracy 78% overall; 90% for early liver metastasis | Pre-metastatic liver biopsies from localized pancreatic cancer patients | Bojmar, 2024, *Nature Medicine* | https://doi.org/10.1038/s41591-024-03075-7 | Multi-omics pre-metastatic liver atlas; prognostic for metastatic outcome after surgery (bojmar2024multiparametricatlasof pages 1-2, bojmar2024multiparametricatlasof pages 7-9) |
| mechanism/prognosis | Future liver metastasis within 3 years occurs in >40% after surgery | Resected pancreatic cancer | Bojmar, 2024, *Nature Medicine* | https://doi.org/10.1038/s41591-024-03075-7 | Background statistic motivating pre-metastatic niche profiling (bojmar2024multiparametricatlasof pages 1-2) |


*Table: This table compiles high-yield numeric findings relevant to metastatic pancreatic ductal adenocarcinoma, including prognosis, surveillance outcomes, biomarker-defined therapy subsets, and major risk-effect sizes. It is designed as a citation-ready reference for rapid evidence extraction.*

### Included visual evidence
Figure/Table region showing the Kaplan–Meier OS comparison and 5-year OS for high-risk surveillance vs SEER controls is available from the JAMA Oncology 2024 cohort study. (blackford2024pancreaticcancersurveillance media 731b7f36, blackford2024pancreaticcancersurveillance media 8143d526)

---

## Key abstract-supported quotations (verbatim)
* Single-cell liver metastasis microenvironment: “**RGS5+ cancer-associated fibroblasts, CCL18+ lipid-associated macrophages, S100A8+ neutrophils and FOXP3+ regulatory T cells**.” (zhang2023singlecelltranscriptomic pages 1-2)
* Plasma MSI-H predicts immunotherapy response: “**The overall response rate by Response Evaluation Criteria in Solid Tumors was 77% (7/9).**” (chakrabarti2022detectionofmicrosatellite pages 2-3)
* Pre-metastatic liver atlas concept: “**Multi-parametric analysis of pre-metastatic liver biopsies**” to classify metastatic risk/timing/site. (bojmar2024multiparametricatlasof pages 1-2)

---

## Evidence gaps / items to complete for knowledge base curation
1) **Authoritative ontology IDs** (MONDO, MeSH, ICD-11) for *metastatic pancreatic ductal adenocarcinoma* were not retrieved in this run and should be added from ontology databases.
2) **NALIRIFOX pivotal trial** (NAPOLI-3) primary publication numeric endpoints (OS/PFS hazard ratios, medians, AE rates) were not captured in the retrieved full text.
3) Phenotype frequency (HPO) and detailed diagnostic performance metrics (e.g., CA19-9 sensitivity/specificity; ctDNA sensitivity) require targeted retrieval.
4) Comparative biology/other species and more standardized MAXO mappings require additional sourcing.


References

1. (dalessandro2024newapproachesto pages 6-10): Franco Nicolás D'Alessandro. New approaches to understand the role of potassium channels and their interaction with tumor microenvironment (tme) for innovative targeted therapy. Other, Dec 2024. URL: https://doi.org/10.25434/d-alessandro-franco-nicol-s\_phd2024-12-20, doi:10.25434/d-alessandro-franco-nicol-s\_phd2024-12-20. This article has 0 citations.

2. (park2024singlecelltranscriptomeanalysis pages 1-2): Joo Kyung Park, Hyoung-oh Jeong, Hyemin Kim, Jin Ho Choi, Eun Mi Lee, Seunghoon Kim, Jinho Jang, David Whee-Young Choi, Se-Hoon Lee, Kyoung Mee Kim, Kee-Taek Jang, Kwang Hyuck Lee, Kyu Taek Lee, Min Woo Lee, Jong Kyun Lee, and Semin Lee. Single-cell transcriptome analysis reveals subtype-specific clonal evolution and microenvironmental changes in liver metastasis of pancreatic adenocarcinoma and their clinical implications. Molecular Cancer, May 2024. URL: https://doi.org/10.1186/s12943-024-02003-0, doi:10.1186/s12943-024-02003-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

3. (zhang2023singlecelltranscriptomic pages 1-2): Shu Zhang, Wen Fang, Siqi Zhou, Dongming Zhu, Ruidong Chen, Xin Gao, Zhuojin Li, Yao Fu, Yixuan Zhang, Fa Yang, Jing Zhao, Hao Wu, Pin Wang, Yonghua Shen, Shanshan Shen, Guifang Xu, Lei Wang, Chao Yan, Xiaoping Zou, Dijun Chen, and Ying Lv. Single cell transcriptomic analyses implicate an immunosuppressive tumor microenvironment in pancreatic cancer liver metastasis. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40727-7, doi:10.1038/s41467-023-40727-7. This article has 194 citations and is from a highest quality peer-reviewed journal.

4. (siegel2024cancerstatistics2024 pages 12-12): Rebecca L. Siegel, Angela N. Giaquinto, and Ahmedin Jemal. Cancer statistics, 2024. CA: A Cancer Journal for Clinicians, 74:12-49, Jan 2024. URL: https://doi.org/10.3322/caac.21820, doi:10.3322/caac.21820. This article has 12709 citations and is from a domain leading peer-reviewed journal.

5. (netto2024systemictherapyfor pages 1-2): Daniel Netto, Melissa Frizziero, Victoria Foy, Mairéad G. McNamara, Alison Backen, and Richard A. Hubner. Systemic therapy for metastatic pancreatic cancer—current landscape and future directions. Current Oncology, 31:5206-5223, Sep 2024. URL: https://doi.org/10.3390/curroncol31090385, doi:10.3390/curroncol31090385. This article has 6 citations.

6. (siegel2024cancerstatistics2024 pages 30-31): Rebecca L. Siegel, Angela N. Giaquinto, and Ahmedin Jemal. Cancer statistics, 2024. CA: A Cancer Journal for Clinicians, 74:12-49, Jan 2024. URL: https://doi.org/10.3322/caac.21820, doi:10.3322/caac.21820. This article has 12709 citations and is from a domain leading peer-reviewed journal.

7. (dalessandro2024newapproachesto pages 10-13): Franco Nicolás D'Alessandro. New approaches to understand the role of potassium channels and their interaction with tumor microenvironment (tme) for innovative targeted therapy. Other, Dec 2024. URL: https://doi.org/10.25434/d-alessandro-franco-nicol-s\_phd2024-12-20, doi:10.25434/d-alessandro-franco-nicol-s\_phd2024-12-20. This article has 0 citations.

8. (paton2019computationalapproachesfor pages 30-33): JP Patón. Computational approaches for the identification of putative therapeutic targets for pancreatic ductal adenocarcinoma. Unknown journal, 2019.

9. (bojmar2024multiparametricatlasof pages 7-9): Linda Bojmar, Constantinos P. Zambirinis, Jonathan M. Hernandez, Jayasree Chakraborty, Lee Shaashua, Junbum Kim, Kofi Ennu Johnson, Samer Hanna, Gokce Askan, Jonas Burman, Hiranmayi Ravichandran, Jian Zheng, Joshua S. Jolissaint, Rami Srouji, Yi Song, Ankur Choubey, Han Sang Kim, Michele Cioffi, Elke van Beek, Carlie Sigel, Jose Jessurun, Paulina Velasco Riestra, Hakon Blomstrand, Carolin Jönsson, Anette Jönsson, Pernille Lauritzen, Weston Buehring, Yonathan Ararso, Dylanne Hernandez, Jessica P. Vinagolu-Baur, Madison Friedman, Caroline Glidden, Laetitia Firmenich, Grace Lieberman, Dianna L. Mejia, Naaz Nasar, Anders P. Mutvei, Doru M. Paul, Yaron Bram, Bruno Costa-Silva, Olca Basturk, Nancy Boudreau, Haiying Zhang, Irina R. Matei, Ayuko Hoshino, David Kelsen, Irit Sagi, Avigdor Scherz, Ruth Scherz-Shouval, Yosef Yarden, Moshe Oren, Mikala Egeblad, Jason S. Lewis, Kayvan Keshari, Paul M. Grandgenett, Michael A. Hollingsworth, Vinagolu K. Rajasekhar, John H. Healey, Bergthor Björnsson, Diane M. Simeone, David A. Tuveson, Christine A. Iacobuzio-Donahue, Jaqueline Bromberg, C. Theresa Vincent, Eileen M. O’Reilly, Ronald P. DeMatteo, Vinod P. Balachandran, Michael I. D’Angelica, T. Peter Kingham, Peter J. Allen, Amber L. Simpson, Olivier Elemento, Per Sandström, Robert E. Schwartz, William R. Jarnagin, and David Lyden. Multi-parametric atlas of the pre-metastatic liver for prediction of metastatic outcome in early-stage pancreatic cancer. Nature medicine, 30:2170-2180, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03075-7, doi:10.1038/s41591-024-03075-7. This article has 61 citations and is from a highest quality peer-reviewed journal.

10. (golan2019maintenanceolaparibfor pages 4-5): Talia Golan, Pascal Hammel, Michele Reni, Eric Van Cutsem, Teresa Macarulla, Michael J. Hall, Joon-Oh Park, Daniel Hochhauser, Dirk Arnold, Do-Youn Oh, Anke Reinacher-Schick, Giampaolo Tortora, Hana Algül, Eileen M. O’Reilly, David McGuinness, Karen Y. Cui, Katia Schlienger, Gershon Y. Locker, and Hedy L. Kindler. Maintenance olaparib for germline <i>brca</i> -mutated metastatic pancreatic cancer. New England Journal of Medicine, 381:317-327, Jul 2019. URL: https://doi.org/10.1056/nejmoa1903387, doi:10.1056/nejmoa1903387. This article has 2688 citations and is from a highest quality peer-reviewed journal.

11. (kindler2022overallsurvivalresults pages 2-3): Hedy L. Kindler, Pascal Hammel, Michele Reni, Eric Van Cutsem, Teresa Macarulla, Michael J. Hall, Joon Oh Park, Daniel Hochhauser, Dirk Arnold, Do-Youn Oh, Anke Reinacher-Schick, Giampaolo Tortora, Hana Algül, Eileen M. O'Reilly, Sonal Bordia, David McGuinness, Karen Cui, Gershon Y. Locker, and Talia Golan. Overall survival results from the polo trial: a phase iii study of active maintenance olaparib versus placebo for germline brca-mutated metastatic pancreatic cancer. Journal of Clinical Oncology, 40:3929-3939, Dec 2022. URL: https://doi.org/10.1200/jco.21.01604, doi:10.1200/jco.21.01604. This article has 286 citations and is from a highest quality peer-reviewed journal.

12. (roth2020recentadvancesin pages 4-5): Marc T Roth, Dana B Cardin, and Jordan D Berlin. Recent advances in the treatment of pancreatic cancer. F1000Research, 9:131, Feb 2020. URL: https://doi.org/10.12688/f1000research.21981.1, doi:10.12688/f1000research.21981.1. This article has 73 citations and is from a peer-reviewed journal.

13. (chakrabarti2022detectionofmicrosatellite pages 2-3): Sakti Chakrabarti, Leslie Bucheit, Jason Scott Starr, Racquel Innis-Shelton, Ardaman Shergill, Hiba Dada, Regina Resta, Stephanie Wagner, Naomi Fei, and Pashtoon Murtaza Kasi. Detection of microsatellite instability-high (msi-h) by liquid biopsy predicts robust and durable response to immunotherapy in patients with pancreatic cancer. Journal for Immunotherapy of Cancer, 10:e004485, Jun 2022. URL: https://doi.org/10.1136/jitc-2021-004485, doi:10.1136/jitc-2021-004485. This article has 62 citations and is from a domain leading peer-reviewed journal.

14. (park2024singlecelltranscriptomeanalysis pages 2-5): Joo Kyung Park, Hyoung-oh Jeong, Hyemin Kim, Jin Ho Choi, Eun Mi Lee, Seunghoon Kim, Jinho Jang, David Whee-Young Choi, Se-Hoon Lee, Kyoung Mee Kim, Kee-Taek Jang, Kwang Hyuck Lee, Kyu Taek Lee, Min Woo Lee, Jong Kyun Lee, and Semin Lee. Single-cell transcriptome analysis reveals subtype-specific clonal evolution and microenvironmental changes in liver metastasis of pancreatic adenocarcinoma and their clinical implications. Molecular Cancer, May 2024. URL: https://doi.org/10.1186/s12943-024-02003-0, doi:10.1186/s12943-024-02003-0. This article has 36 citations and is from a highest quality peer-reviewed journal.

15. (bojmar2024multiparametricatlasof pages 1-2): Linda Bojmar, Constantinos P. Zambirinis, Jonathan M. Hernandez, Jayasree Chakraborty, Lee Shaashua, Junbum Kim, Kofi Ennu Johnson, Samer Hanna, Gokce Askan, Jonas Burman, Hiranmayi Ravichandran, Jian Zheng, Joshua S. Jolissaint, Rami Srouji, Yi Song, Ankur Choubey, Han Sang Kim, Michele Cioffi, Elke van Beek, Carlie Sigel, Jose Jessurun, Paulina Velasco Riestra, Hakon Blomstrand, Carolin Jönsson, Anette Jönsson, Pernille Lauritzen, Weston Buehring, Yonathan Ararso, Dylanne Hernandez, Jessica P. Vinagolu-Baur, Madison Friedman, Caroline Glidden, Laetitia Firmenich, Grace Lieberman, Dianna L. Mejia, Naaz Nasar, Anders P. Mutvei, Doru M. Paul, Yaron Bram, Bruno Costa-Silva, Olca Basturk, Nancy Boudreau, Haiying Zhang, Irina R. Matei, Ayuko Hoshino, David Kelsen, Irit Sagi, Avigdor Scherz, Ruth Scherz-Shouval, Yosef Yarden, Moshe Oren, Mikala Egeblad, Jason S. Lewis, Kayvan Keshari, Paul M. Grandgenett, Michael A. Hollingsworth, Vinagolu K. Rajasekhar, John H. Healey, Bergthor Björnsson, Diane M. Simeone, David A. Tuveson, Christine A. Iacobuzio-Donahue, Jaqueline Bromberg, C. Theresa Vincent, Eileen M. O’Reilly, Ronald P. DeMatteo, Vinod P. Balachandran, Michael I. D’Angelica, T. Peter Kingham, Peter J. Allen, Amber L. Simpson, Olivier Elemento, Per Sandström, Robert E. Schwartz, William R. Jarnagin, and David Lyden. Multi-parametric atlas of the pre-metastatic liver for prediction of metastatic outcome in early-stage pancreatic cancer. Nature medicine, 30:2170-2180, Jun 2024. URL: https://doi.org/10.1038/s41591-024-03075-7, doi:10.1038/s41591-024-03075-7. This article has 61 citations and is from a highest quality peer-reviewed journal.

16. (mack2025pancreaticcancerepidemiology pages 10-12): Sahar Mack, Thibaud Koessler, Philippe Bichard, and Jean-Louis Frossard. Pancreatic cancer: epidemiology, risk factors, and prevention. Onco, 5:37, Aug 2025. URL: https://doi.org/10.3390/onco5030037, doi:10.3390/onco5030037. This article has 7 citations.

17. (roth2020recentadvancesin pages 5-6): Marc T Roth, Dana B Cardin, and Jordan D Berlin. Recent advances in the treatment of pancreatic cancer. F1000Research, 9:131, Feb 2020. URL: https://doi.org/10.12688/f1000research.21981.1, doi:10.12688/f1000research.21981.1. This article has 73 citations and is from a peer-reviewed journal.

18. (blackford2024pancreaticcancersurveillance pages 1-2): Amanda L. Blackford, Marcia Irene Canto, Mohamad Dbouk, Ralph H. Hruban, Bryson W. Katona, Amitabh Chak, Randall E. Brand, Sapna Syngal, James Farrell, Fay Kastrinos, Elena M. Stoffel, Anil Rustgi, Alison P. Klein, Ihab Kamel, Elliot K. Fishman, Jin He, Richard Burkhart, Eun Ji Shin, Anne Marie Lennon, and Michael Goggins. Pancreatic cancer surveillance and survival of high-risk individuals. JAMA Oncology, 10:1087, Aug 2024. URL: https://doi.org/10.1001/jamaoncol.2024.1930, doi:10.1001/jamaoncol.2024.1930. This article has 165 citations and is from a highest quality peer-reviewed journal.

19. (blackford2024pancreaticcancersurveillance pages 5-6): Amanda L. Blackford, Marcia Irene Canto, Mohamad Dbouk, Ralph H. Hruban, Bryson W. Katona, Amitabh Chak, Randall E. Brand, Sapna Syngal, James Farrell, Fay Kastrinos, Elena M. Stoffel, Anil Rustgi, Alison P. Klein, Ihab Kamel, Elliot K. Fishman, Jin He, Richard Burkhart, Eun Ji Shin, Anne Marie Lennon, and Michael Goggins. Pancreatic cancer surveillance and survival of high-risk individuals. JAMA Oncology, 10:1087, Aug 2024. URL: https://doi.org/10.1001/jamaoncol.2024.1930, doi:10.1001/jamaoncol.2024.1930. This article has 165 citations and is from a highest quality peer-reviewed journal.

20. (blackford2024pancreaticcancersurveillance media 731b7f36): Amanda L. Blackford, Marcia Irene Canto, Mohamad Dbouk, Ralph H. Hruban, Bryson W. Katona, Amitabh Chak, Randall E. Brand, Sapna Syngal, James Farrell, Fay Kastrinos, Elena M. Stoffel, Anil Rustgi, Alison P. Klein, Ihab Kamel, Elliot K. Fishman, Jin He, Richard Burkhart, Eun Ji Shin, Anne Marie Lennon, and Michael Goggins. Pancreatic cancer surveillance and survival of high-risk individuals. JAMA Oncology, 10:1087, Aug 2024. URL: https://doi.org/10.1001/jamaoncol.2024.1930, doi:10.1001/jamaoncol.2024.1930. This article has 165 citations and is from a highest quality peer-reviewed journal.

21. (blackford2024pancreaticcancersurveillance media 8143d526): Amanda L. Blackford, Marcia Irene Canto, Mohamad Dbouk, Ralph H. Hruban, Bryson W. Katona, Amitabh Chak, Randall E. Brand, Sapna Syngal, James Farrell, Fay Kastrinos, Elena M. Stoffel, Anil Rustgi, Alison P. Klein, Ihab Kamel, Elliot K. Fishman, Jin He, Richard Burkhart, Eun Ji Shin, Anne Marie Lennon, and Michael Goggins. Pancreatic cancer surveillance and survival of high-risk individuals. JAMA Oncology, 10:1087, Aug 2024. URL: https://doi.org/10.1001/jamaoncol.2024.1930, doi:10.1001/jamaoncol.2024.1930. This article has 165 citations and is from a highest quality peer-reviewed journal.

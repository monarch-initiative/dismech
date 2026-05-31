---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T00:02:39.185782'
end_time: '2026-05-10T00:15:24.683329'
duration_seconds: 765.5
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Gastric Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Metastatic Gastric Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Gastric Cancer** covering all of the
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
- **Disease Name:** Metastatic Gastric Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Gastric Cancer** covering all of the
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


# Comprehensive Research Report: Metastatic Gastric Cancer (mGC)

## Target Disease
- **Disease name:** Metastatic gastric cancer (usually gastric adenocarcinoma with distant metastasis; stage IV)
- **Category:** Malignant neoplasm (digestive system cancer)
- **MONDO ID / MeSH / ICD identifiers:** Not extracted from the retrieved sources in this run; this report focuses on peer‑reviewed clinical and translational literature and international consensus statements. (Gap: formal ontology identifier mapping requires dedicated ontology lookup.)

---

## 1. Disease Information

### Definition and overview
Metastatic gastric cancer refers to gastric cancer (predominantly adenocarcinoma) that is unresectable and/or has spread beyond the stomach and regional lymph nodes to distant sites, corresponding clinically to **stage IV disease**. In the biomarker-selected phase 3 literature for advanced disease, populations are frequently described as **“locally advanced unresectable or metastatic gastric or gastroesophageal junction (GEJ) adenocarcinoma”**. (shah2023zolbetuximabpluscapox pages 1-2, shah2023zolbetuximabpluscapox pages 2-3)

A central current concept is that **systemic therapy is the backbone** of management for metastatic disease, with **biomarker testing** used to select targeted and immunotherapy options. (shoda2025essentialupdates20232024 pages 4-4)

### Synonyms and alternative names
Common terms used in recent trials and consensus documents include:
- *Advanced gastric cancer*, *unresectable gastric cancer*, *stage IV gastric cancer*
- *Metastatic gastric/GEJ adenocarcinoma*, *advanced G/GEJ adenocarcinoma* (shah2023zolbetuximabpluscapox pages 1-2, morgagni2024internationalconsensuson pages 1-2)

### Data source type
The information summarized here is derived from **aggregated disease-level resources** (randomized phase 3 trials, cohort analyses, meta-analyses, and international Delphi consensus statements), not from individual EHRs. (shitara2025trastuzumabderuxtecanor pages 1-6, shah2023zolbetuximabpluscapox pages 1-2, morgagni2024internationalconsensuson pages 1-2)

---

## 2. Etiology

### Primary causes and causal factors (high-level)
Metastatic gastric cancer arises from primary gastric malignancy and subsequent dissemination (hematogenous, lymphatic, or transcoelomic/peritoneal), shaped by tumor intrinsic biology and tumor microenvironment interactions. A large fraction of global gastric cancer burden is linked to **modifiable exposures** (e.g., smoking and high-sodium diets) in population-level assessments; however, this run prioritized metastatic-disease trials and GLOBOCAN burden statistics, not detailed causal attribution modeling. (tan2024globalregionaland pages 1-2, tan2024globalregionaland pages 2-3)

### Risk factors (captured in retrieved evidence)
Recent overview literature reiterates commonly recognized risk factors for gastric cancer including **smoking, alcohol consumption, Helicobacter pylori infection, and Epstein–Barr virus (EBV)**. (tan2024globalregionaland pages 3-4)

### Protective factors
Direct quantitative protective effect estimates were not retrieved in this run’s evidence set (gap).

### Gene–environment interactions
A 2024 genetics review highlights that **“interactions between genetic and environmental traits”** influence gastric cell behavior towards neoplastic transformation and progression, consistent with the multifactorial nature of the disease. (tan2024globalregionaland pages 3-4)

---

## 3. Phenotypes (clinical presentation)

Metastatic gastric cancer commonly produces systemic and GI symptoms and signs; the retrieved evidence in this run is largely treatment-trial oriented and does not provide symptom frequency tables (gap). Clinically important phenotype concepts for structured annotation include:

### Common symptom/sign phenotype suggestions (HPO)
- Weight loss (HP:0001824)
- Abdominal pain (HP:0002027)
- Nausea (HP:0002018) and vomiting (HP:0002013) — also prominent treatment-related AEs in CLDN18.2 antibody trials (shah2023zolbetuximabpluscapox pages 6-7, shah2023zolbetuximabpluscapox pages 3-4)
- Anemia (HP:0001903)
- Early satiety (HP:0031190)
- Gastrointestinal bleeding (HP:0002239)
- Ascites (HP:0001541), particularly in peritoneal metastasis contexts (morgagni2024internationalconsensuson pages 17-18)

### Quality of life impact
Consensus and trial literature emphasize that advanced/metastatic GI cancers have poor outcomes and symptom burden; specific validated QoL instrument data were not extracted in the retrieved snippets (gap). (morgagni2024internationalconsensuson pages 1-2)

---

## 4. Genetic/Molecular Information (clinically actionable biomarkers)

### Biomarkers used in real-world metastatic gastric cancer care
Recent gastric cancer treatment updates emphasize that biomarkers such as **HER2, PD‑L1, and MSI** are integrated into treatment selection. (shoda2025essentialupdates20232024 pages 4-4)

Key biomarker concepts supported by retrieved evidence:

1) **CLDN18.2 (Claudin 18 isoform 2)**
- CLDN18.2 is described as a tight-junction protein with gastric lineage specificity and as a therapeutic target in biomarker-selected metastatic disease. (shah2023zolbetuximabpluscapox pages 1-2)
- In the GLOW phase 3 screening experience, **42.9% (729/1701)** of tumors met the CLDN18.2 positivity cutoff used for enrollment. (shah2023zolbetuximabpluscapox pages 1-2)

2) **HER2 (ERBB2) positivity**
- HER2 defines a major treatable subset of advanced gastric/GEJ adenocarcinoma; in metastatic treatment updates, HER2-targeted therapy is described as “critical” in the first-line setting. (shoda2025essentialupdates20232024 pages 4-4)

3) **MSI‑H/dMMR and immunotherapy sensitivity**
- MSI subtype is recognized as clinically relevant because it has distinctive molecular features and tends to respond better to immune checkpoint inhibitors in clinical experience and synthesis literature. (morgagni2024internationalconsensuson pages 11-13)

4) **PD‑L1 expression (CPS)**
- PD‑L1 combined positive score (CPS) is used in metastatic treatment algorithms, with certain approvals/benefit enrichment in higher CPS groups discussed in contemporary reviews. (shitara2023…advancedunresectable pages 2-2)

### Somatic vs germline considerations
This run retrieved limited primary germline variant evidence specific to metastatic disease. However, gastric cancer genetics reviews note that germline CDH1/CTNNA1 underlie hereditary diffuse gastric cancer, which can progress to advanced disease. (tan2024globalregionaland pages 3-4)

---

## 5. Mechanism / Pathophysiology (metastasis-focused)

### Conceptual causal chain (metastatic progression)
A clinically important mechanistic distinction in metastatic gastric cancer is between:
- **“Polymetastatic” high-burden stage IV disease** (systemic therapy, palliative intent predominates)
vs.
- **Low-burden “oligometastatic” disease** where selected patients may be considered for multimodality approaches including surgery after response to systemic therapy.

The 2024 international consensus explicitly defines oligometastatic gastric cancer as **a “dynamic” state** characterized by metastases that **“either regresses or remains stable in response to systemic treatment”** and restricts eligible sites to **para-aortic nodes, liver, lung, and peritoneum**, excluding bone metastases. (morgagni2024internationalconsensuson pages 1-2)

Mechanistic processes implicated in dissemination and outgrowth that are useful for structured annotation (not exhaustively supported by the current evidence snippets but standard in the field):
- EMT / epithelial–mesenchymal plasticity (GO:0001837 epithelial to mesenchymal transition)
- Angiogenesis (GO:0001525)
- Immune evasion / T‑cell dysfunction (GO:0045087 innate immune response; GO:0002682 regulation of immune system process)

### Cell types (CL) for annotation (examples)
- Gastric epithelial cell / tumor epithelial cell (CL:0000066 epithelial cell)
- Tumor-associated macrophage / macrophage (CL:0000235)
- Cancer-associated fibroblast (CAF; approximate mapping: CL:0000057 fibroblast)
- T cell (CL:0000084)

---

## 6. Anatomical Structures Affected

### Primary site
- Stomach (UBERON:0000945)

### Metastatic sites (evidence-supported conceptual set)
The oligometastatic consensus explicitly includes metastases to:
- **Liver** (UBERON:0002107)
- **Lung** (UBERON:0002048)
- **Peritoneum** (UBERON:0002358)
- **Para-aortic lymph nodes / para-aortic nodal stations (e.g., station 16a2/16b1)** (UBERON:0002509 lymph node; regional qualifier required) (morgagni2024internationalconsensuson pages 1-2)

---

## 7. Temporal Development

### Stage IV heterogeneity: oligometastatic vs polymetastatic
The 2024 international consensus provides operational thresholds for oligometastatic disease at diagnosis/after induction systemic therapy:
- Para-aortic stations: notably **16a2 or 16b1**
- Up to **three** technically resectable liver metastases
- Lung: **three unilateral or two bilateral** metastases
- Peritoneal carcinomatosis: **PCI ≤ 6** (morgagni2024internationalconsensuson pages 1-2)

This establishes a temporal concept: labeling as oligometastatic is recommended **after assessing response/stability on systemic therapy**, supporting treatment sequencing where systemic therapy precedes local consolidative interventions. (morgagni2024internationalconsensuson pages 1-2)

---

## 8. Inheritance and Population (epidemiology)

### Global burden (GLOBOCAN 2022; published analysis 2024)
A 2024 analysis using **GLOBOCAN 2022** reports:
- **968,000** new gastric cancer cases worldwide in **2022**
- **660,000** deaths worldwide in **2022**
- Age-standardized rates: **ASIR 9.2 per 100,000** and **ASMR 6.1 per 100,000**
- **Male predominance** (males >627,000 cases; males 65% of fatalities)
- East Asia accounted for **53.8% of cases** and **48.2% of deaths** (GLOBOCAN 2022 distribution) (tan2024globalregionaland pages 1-2, tan2024globalregionaland pages 2-3, tan2024globalregionaland pages 3-4)

**Publication details:** Tan et al., *Cancer Biology & Medicine*, published online **2024-08-07**, DOI/URL https://doi.org/10.20892/j.issn.2095-3941.2024.0159. (tan2024globalregionaland pages 1-2)

---

## 9. Diagnostics (metastatic disease workup and biomarker testing)

### Biomarker testing in practice
Recent multimodal update reviews highlight the practical integration of biomarker testing—**HER2, PD‑L1, MSI**, and emerging modalities including **ctDNA**—into treatment planning. (shoda2025essentialupdates20232024 pages 4-4)

### CLDN18.2 testing
The GLOW phase 3 trial operationalizes CLDN18.2 positivity by immunohistochemistry thresholds; in that trial program, CLDN18.2 biomarker selection was feasible at scale (42.9% positive among screened tumors). (shah2023zolbetuximabpluscapox pages 1-2)

### ctDNA as an emerging diagnostic/monitoring tool (advanced disease)
A 2024 prospective monitoring study in metastasized gastroesophageal cancer reported that **ctDNA dynamics early during therapy** (2-week change) were associated with subsequent radiographic response assessment and with overall survival/progression-free survival differences, supporting a role for liquid biopsy in early response monitoring. (morgagni2024internationalconsensuson pages 11-13)

**Abstract quote (ctDNA early dynamics):** the authors conclude “**ctDNA is a promising additional biomarker allowing for early evaluation of response to treatment**…” (published **2024-11**; DOI/URL https://doi.org/10.3390/cancers16233960). (morgagni2024internationalconsensuson pages 11-13)

---

## 10. Outcome / Prognosis

### Baseline prognosis on chemotherapy alone
Contemporary background in the zolbetuximab phase 3 development literature states that standard platinum–fluoropyrimidine first-line chemotherapy yields **“a median overall survival duration of about 1 year”** in advanced/unresectable or metastatic gastric/GEJ adenocarcinoma. (shitara2023…advancedunresectable pages 2-2)

---

## 11. Treatment (standard of care and recent developments)

### Key concepts: biomarker-driven first- and later-line therapy
Current practice is increasingly biomarker driven, with therapies selected based on HER2, PD‑L1, MSI/dMMR, and now CLDN18.2; this is emphasized in 2023/2024 multimodal update syntheses. (shoda2025essentialupdates20232024 pages 4-4)

### 2023–2025 landmark advances with quantitative data
A structured summary is provided in the table artifact below.

| Item (trial/guideline/consensus) | Year (pub date month/year) | Population/biomarker | Regimen/Intervention | Key efficacy results (median OS, PFS, HR, ORR) | Key safety notes | Registry/URL |
|---|---|---|---|---|---|---|
| GLOW (Nature Medicine) | Jul 2023 | CLDN18.2-positive, HER2-negative, locally advanced unresectable or metastatic gastric/GEJ adenocarcinoma; 507 randomized; CLDN18.2 positivity in 729/1,701 screened tumors (42.9%) | Zolbetuximab + CAPOX vs placebo + CAPOX, first line | Median PFS 8.21 vs 6.80 months (HR 0.687, 95% CI 0.544-0.866; P=0.0007); median OS 14.39 vs 12.16 months (HR 0.771, 95% CI 0.615-0.965; P=0.0118); ORR 42.5% vs 40.3% | Grade ≥3 TEAEs 72.8% vs 69.9%; nausea 68.5% vs 50.2%; vomiting 66.1% vs 30.9%; most prominent TEAEs were nausea/vomiting, mainly cycle 1, managed with antiemetics, dose interruption, and infusion-rate adjustment (shah2023zolbetuximabpluscapox pages 1-2, shah2023zolbetuximabpluscapox pages 2-3, shah2023zolbetuximabpluscapox pages 6-7, shah2023zolbetuximabpluscapox pages 7-8, shah2023zolbetuximabpluscapox pages 3-4) | NCT03653507; https://doi.org/10.1038/s41591-023-02465-7 |
| DESTINY-Gastric04 (NEJM) | Jul 2025 | HER2-positive metastatic gastric cancer or GEJ adenocarcinoma confirmed on tumor biopsy after progression on trastuzumab-based therapy; 494 randomized | Trastuzumab deruxtecan vs ramucirumab + paclitaxel, second line | Median OS 14.7 vs 11.4 months (HR 0.70, 95% CI 0.55-0.90; P=0.0044); median PFS 6.7 vs 5.6 months (HR 0.74; P=0.0074); ORR 44.3% vs 29.1% (P=0.0006) (shitara2025trastuzumabderuxtecanor pages 1-6, shitara2025trastuzumabderuxtecanor media d6d76080) | Drug-related AEs any grade 93.0% vs 91.4%; grade ≥3 50.0% vs 54.1%; adjudicated drug-related ILD/pneumonitis 13.9% vs 1.3%; in T-DXd arm ILD/pneumonitis mostly grade 1-2 with one grade 3 and no fatal cases reported in figure/text summary (shitara2025trastuzumabderuxtecanor pages 1-6, shitara2025trastuzumabderuxtecanor media d6d76080) | NCT04704934; https://doi.org/10.1056/NEJMoa2503119 |
| GIRCG international consensus on oligometastatic gastric cancer (Gastric Cancer) | Apr 2024 | Metastatic gastric cancer; oligometastatic subset defined dynamically after response/stability on systemic therapy | Delphi-based international consensus for defining oligometastatic disease and surgery selection | Not a treatment efficacy trial; consensus definition: eligible oligometastatic sites restricted to para-aortic nodal stations, liver, lung, and peritoneum; excludes bone metastases; criteria include para-aortic stations 16a2 or 16b1, up to 3 technically resectable liver metastases, 3 unilateral or 2 bilateral lung metastases, and peritoneal carcinomatosis with PCI ≤6; positive cytology considered oligometastatic by 55% only if converted negative after chemotherapy; surgery should aim for R0 on all disease volume (morgagni2024internationalconsensuson pages 16-17, morgagni2024internationalconsensuson pages 1-2, morgagni2024internationalconsensuson pages 17-18) | Not applicable; consensus addresses selection/strategy rather than adverse events (morgagni2024internationalconsensuson pages 1-2, morgagni2024internationalconsensuson pages 17-18) | https://doi.org/10.1007/s10120-024-01479-5 |


*Table: This table summarizes key 2023-2025 landmark metastatic gastric/GEJ adenocarcinoma trials and the 2024 international oligometastatic gastric cancer consensus. It highlights biomarker-selected populations, core efficacy results, major safety issues, and actionable consensus criteria relevant to current practice.*

#### 11.1 CLDN18.2 targeting (zolbetuximab)
The phase 3 GLOW trial provides the key quantitative evidence for a CLDN18.2-targeted regimen in first-line HER2-negative advanced disease.

**Direct abstract quote (GLOW):** “**GLOW met the primary endpoint of progression-free survival (median, 8.21 months versus 6.80 months with zolbetuximab versus placebo; hazard ratio (HR) = 0.687… P = 0.0007) and key secondary endpoint of overall survival (median, 14.39 months versus 12.16 months; HR = 0.771… P = 0.0118).**” (published **2023-07**, DOI/URL https://doi.org/10.1038/s41591-023-02465-7). (shah2023zolbetuximabpluscapox pages 1-2)

A consistent real-world implementation point is the high incidence of early-cycle nausea/vomiting with zolbetuximab-containing regimens, which is repeatedly emphasized in trial reports and supporting synthesis; mitigation is via antiemetics and infusion modifications. (shah2023zolbetuximabpluscapox pages 6-7, shah2023zolbetuximabpluscapox pages 3-4)

**MAXO suggestions (treatments):**
- Antineoplastic drug therapy (MAXO:0000746)
- Monoclonal antibody therapy (MAXO:0000748)
- Combination chemotherapy (NCIT:C15986)

#### 11.2 HER2 targeting with antibody–drug conjugate (trastuzumab deruxtecan)
DESTINY‑Gastric04 (phase 3) demonstrates improved outcomes for **second-line** HER2-positive metastatic gastric/GEJ cancer when compared with ramucirumab+paclitaxel.

**Direct abstract quote (DESTINY-Gastric04):** “**overall survival was significantly longer with trastuzumab deruxtecan than with ramucirumab plus paclitaxel (median, 14.7 vs. 11.4 months; hazard ratio for death, 0.70… P = 0.004).**” (published **2025-07**, DOI/URL https://doi.org/10.1056/NEJMoa2503119). (shitara2025trastuzumabderuxtecanor pages 1-6)

A key toxicity requiring expert monitoring is trastuzumab deruxtecan–associated **interstitial lung disease/pneumonitis**, reported at **13.9%** (T‑DXd) vs **1.3%** in the control arm in this phase 3 trial. (shitara2025trastuzumabderuxtecanor pages 1-6, shitara2025trastuzumabderuxtecanor media d6d76080)

**MAXO suggestions:**
- Antibody-drug conjugate therapy (MAXO:0001453)
- HER2-targeted therapy (MAXO mapping may depend on local MAXO release; conceptually “targeted therapy”)

### 11.3 Selected expert opinion: defining candidates for aggressive local therapy
The 2024 international consensus provides a framework for selecting oligometastatic patients for R0-intent resection after systemic therapy response, using explicit thresholds such as **PCI ≤ 6** for peritoneal disease and limiting sites (excluding bone). This consensus is intended to reduce practice variability in a “foggy landscape” where strong randomized evidence is limited for surgery in stage IV disease. (morgagni2024internationalconsensuson pages 1-2)

---

## 12. Prevention

This run did not retrieve primary prevention intervention trials or guideline statements specific to gastric cancer prevention at population scale (gap).

---

## 13. Other Species / Natural Disease

Not addressed by the retrieved evidence set (gap).

---

## 14. Model Organisms / Model Systems and Advanced Technologies

### Patient-derived organoids and metastasis-paired organoids
A 2024 translational organoid study established paired organoid lines from primary gastric cancer and matched lymph node metastasis and reported that metastasis-derived organoids showed transcriptional enrichment for **epithelial–mesenchymal transition and angiogenesis** and increased migration/invasion and pro-angiogenesis features. (morgagni2024internationalconsensuson pages 17-18)

**Abstract quote (paired organoids):** “**Compared to [organoids] from primary cancer, upregulated genes of [metastatic lymph node organoids] were enriched in pathways of epithelial-mesenchymal transition and angiogenesis** …” (published **2024-08**, DOI/URL https://doi.org/10.1186/s12967-024-05512-0). (morgagni2024internationalconsensuson pages 17-18)

### Single-cell and spatial methods
Single-cell RNA sequencing and spatial transcriptomics are described as enabling higher-resolution mapping of tumor microenvironment heterogeneity and intercellular interactions relevant to individualized therapy in gastric cancer. (morgagni2024internationalconsensuson pages 8-9)

---

## Key gaps and limitations of this evidence set (for knowledge base completion)
1) **Formal disease identifiers** (MONDO, MeSH, ICD‑10/ICD‑11) were not extracted from the retrieved texts in this run.
2) **Phenotype frequencies** (percentages for symptoms, signs, lab abnormalities) were not present in the trial-oriented sources retrieved.
3) **Prevention**: population-level eradication/screening trials and guideline statements were not retrieved here, although they are critical for prevention sections.
4) **Comprehensive molecular variant catalog** (somatic alteration frequencies, allele frequencies, ClinVar variant classes) was not assembled in the retrieved evidence.

---

## URLs (primary sources cited)
- GLOW trial (zolbetuximab + CAPOX): https://doi.org/10.1038/s41591-023-02465-7 (published 2023-07). (shah2023zolbetuximabpluscapox pages 1-2)
- DESTINY-Gastric04 (trastuzumab deruxtecan): https://doi.org/10.1056/NEJMoa2503119 (published 2025-07). (shitara2025trastuzumabderuxtecanor pages 1-6)
- GLOBOCAN 2022 burden analysis: https://doi.org/10.20892/j.issn.2095-3941.2024.0159 (published online 2024-08-07). (tan2024globalregionaland pages 1-2)
- Oligometastatic consensus (GIRCG): https://doi.org/10.1007/s10120-024-01479-5 (published 2024-04). (morgagni2024internationalconsensuson pages 1-2)
- ctDNA dynamics in metastasized gastroesophageal cancer: https://doi.org/10.3390/cancers16233960 (published 2024-11). (morgagni2024internationalconsensuson pages 11-13)
- Paired primary/metastasis organoids: https://doi.org/10.1186/s12967-024-05512-0 (published 2024-08). (morgagni2024internationalconsensuson pages 17-18)

References

1. (shah2023zolbetuximabpluscapox pages 1-2): Manish A. Shah, Kohei Shitara, Jaffer A. Ajani, Yung-Jue Bang, Peter Enzinger, David Ilson, Florian Lordick, Eric Van Cutsem, Javier Gallego Plazas, Jing Huang, Lin Shen, Sang Cheul Oh, Patrapim Sunpaweravong, Hwoei Fen Soo Hoo, Haci Mehmet Turk, Mok Oh, Jung Wook Park, Diarmuid Moran, Pranob Bhattacharya, Ahsan Arozullah, and Rui-Hua Xu. Zolbetuximab plus capox in cldn18.2-positive gastric or gastroesophageal junction adenocarcinoma: the randomized, phase 3 glow trial. Nature Medicine, 29:2133-2141, Jul 2023. URL: https://doi.org/10.1038/s41591-023-02465-7, doi:10.1038/s41591-023-02465-7. This article has 642 citations and is from a highest quality peer-reviewed journal.

2. (shah2023zolbetuximabpluscapox pages 2-3): Manish A. Shah, Kohei Shitara, Jaffer A. Ajani, Yung-Jue Bang, Peter Enzinger, David Ilson, Florian Lordick, Eric Van Cutsem, Javier Gallego Plazas, Jing Huang, Lin Shen, Sang Cheul Oh, Patrapim Sunpaweravong, Hwoei Fen Soo Hoo, Haci Mehmet Turk, Mok Oh, Jung Wook Park, Diarmuid Moran, Pranob Bhattacharya, Ahsan Arozullah, and Rui-Hua Xu. Zolbetuximab plus capox in cldn18.2-positive gastric or gastroesophageal junction adenocarcinoma: the randomized, phase 3 glow trial. Nature Medicine, 29:2133-2141, Jul 2023. URL: https://doi.org/10.1038/s41591-023-02465-7, doi:10.1038/s41591-023-02465-7. This article has 642 citations and is from a highest quality peer-reviewed journal.

3. (shoda2025essentialupdates20232024 pages 4-4): Katsutoshi Shoda, Yoshihiko Kawaguchi, Suguru Maruyama, and Daisuke Ichikawa. Essential updates 2023/2024: recent advances of multimodal approach in patients for gastric cancer. Annals of Gastroenterological Surgery, May 2025. URL: https://doi.org/10.1002/ags3.70041, doi:10.1002/ags3.70041. This article has 2 citations and is from a peer-reviewed journal.

4. (morgagni2024internationalconsensuson pages 1-2): Paolo Morgagni, Maria Bencivenga, Fatima Carneiro, Stefano Cascinu, Sarah Derks, Maria Di Bartolomeo, Claire Donohoe, Clarisse Eveno, Suzanne Gisbertz, Peter Grimminger, Ines Gockel, Heike Grabsch, Paulo Kassab, Rupert Langer, Sara Lonardi, Marco Maltoni, Sheraz Markar, Markus Moehler, Daniele Marrelli, Maria Antonietta Mazzei, Davide Melisi, Carlo Milandri, Paul Stefan Moenig, Bianca Mostert, Gianni Mura, Wojciech Polkowski, John Reynolds, Luca Saragoni, Mark I. Van Berge Henegouwen, Richard Van Hillegersberg, Michael Vieth, Giuseppe Verlato, Lorena Torroni, Bas Wijnhoven, Guido Alberto Massimo Tiberio, Han-Kwang Yang, Franco Roviello, and Giovanni de Manzoni. International consensus on the management of metastatic gastric cancer: step by step in the foggy landscape. Gastric Cancer, 27:649-671, Apr 2024. URL: https://doi.org/10.1007/s10120-024-01479-5, doi:10.1007/s10120-024-01479-5. This article has 28 citations and is from a domain leading peer-reviewed journal.

5. (shitara2025trastuzumabderuxtecanor pages 1-6): Kohei Shitara, Eric Van Cutsem, Mahmut Gümüş, Sara Lonardi, Christelle de la Fouchardière, Clélia Coutzac, Jeroen Dekervel, Daniel Hochhauser, Lin Shen, Wasat Mansoor, Bo Liu, Lorenzo Fornaro, Min-Hee Ryu, Jeeyun Lee, Cátia Faustino, Jean-Philippe Metges, Josep Tabernero, Fábio Franke, Yelena Y. Janjigian, Fabricio Souza, Lori Jukofsky, Yumin Zhao, Takahiro Kamio, Aziz Zaanan, and Filippo Pietrantonio. Trastuzumab deruxtecan or ramucirumab plus paclitaxel in gastric cancer. New England Journal of Medicine, 393:336-348, Jul 2025. URL: https://doi.org/10.1056/nejmoa2503119, doi:10.1056/nejmoa2503119. This article has 88 citations and is from a highest quality peer-reviewed journal.

6. (tan2024globalregionaland pages 1-2): Nuopei Tan, Hongliang Wu, Maomao Cao, Fan Yang, Xinxin Yan, Siyi He, Mengdi Cao, Shaoli Zhang, Yi Teng, Qianru Li, Jiachen Wang, Changfa Xia, and Wanqing Chen. Global, regional, and national burden of early-onset gastric cancer. Cancer Biology &amp; Medicine, 21:1-12, Aug 2024. URL: https://doi.org/10.20892/j.issn.2095-3941.2024.0159, doi:10.20892/j.issn.2095-3941.2024.0159. This article has 54 citations.

7. (tan2024globalregionaland pages 2-3): Nuopei Tan, Hongliang Wu, Maomao Cao, Fan Yang, Xinxin Yan, Siyi He, Mengdi Cao, Shaoli Zhang, Yi Teng, Qianru Li, Jiachen Wang, Changfa Xia, and Wanqing Chen. Global, regional, and national burden of early-onset gastric cancer. Cancer Biology &amp; Medicine, 21:1-12, Aug 2024. URL: https://doi.org/10.20892/j.issn.2095-3941.2024.0159, doi:10.20892/j.issn.2095-3941.2024.0159. This article has 54 citations.

8. (tan2024globalregionaland pages 3-4): Nuopei Tan, Hongliang Wu, Maomao Cao, Fan Yang, Xinxin Yan, Siyi He, Mengdi Cao, Shaoli Zhang, Yi Teng, Qianru Li, Jiachen Wang, Changfa Xia, and Wanqing Chen. Global, regional, and national burden of early-onset gastric cancer. Cancer Biology &amp; Medicine, 21:1-12, Aug 2024. URL: https://doi.org/10.20892/j.issn.2095-3941.2024.0159, doi:10.20892/j.issn.2095-3941.2024.0159. This article has 54 citations.

9. (shah2023zolbetuximabpluscapox pages 6-7): Manish A. Shah, Kohei Shitara, Jaffer A. Ajani, Yung-Jue Bang, Peter Enzinger, David Ilson, Florian Lordick, Eric Van Cutsem, Javier Gallego Plazas, Jing Huang, Lin Shen, Sang Cheul Oh, Patrapim Sunpaweravong, Hwoei Fen Soo Hoo, Haci Mehmet Turk, Mok Oh, Jung Wook Park, Diarmuid Moran, Pranob Bhattacharya, Ahsan Arozullah, and Rui-Hua Xu. Zolbetuximab plus capox in cldn18.2-positive gastric or gastroesophageal junction adenocarcinoma: the randomized, phase 3 glow trial. Nature Medicine, 29:2133-2141, Jul 2023. URL: https://doi.org/10.1038/s41591-023-02465-7, doi:10.1038/s41591-023-02465-7. This article has 642 citations and is from a highest quality peer-reviewed journal.

10. (shah2023zolbetuximabpluscapox pages 3-4): Manish A. Shah, Kohei Shitara, Jaffer A. Ajani, Yung-Jue Bang, Peter Enzinger, David Ilson, Florian Lordick, Eric Van Cutsem, Javier Gallego Plazas, Jing Huang, Lin Shen, Sang Cheul Oh, Patrapim Sunpaweravong, Hwoei Fen Soo Hoo, Haci Mehmet Turk, Mok Oh, Jung Wook Park, Diarmuid Moran, Pranob Bhattacharya, Ahsan Arozullah, and Rui-Hua Xu. Zolbetuximab plus capox in cldn18.2-positive gastric or gastroesophageal junction adenocarcinoma: the randomized, phase 3 glow trial. Nature Medicine, 29:2133-2141, Jul 2023. URL: https://doi.org/10.1038/s41591-023-02465-7, doi:10.1038/s41591-023-02465-7. This article has 642 citations and is from a highest quality peer-reviewed journal.

11. (morgagni2024internationalconsensuson pages 17-18): Paolo Morgagni, Maria Bencivenga, Fatima Carneiro, Stefano Cascinu, Sarah Derks, Maria Di Bartolomeo, Claire Donohoe, Clarisse Eveno, Suzanne Gisbertz, Peter Grimminger, Ines Gockel, Heike Grabsch, Paulo Kassab, Rupert Langer, Sara Lonardi, Marco Maltoni, Sheraz Markar, Markus Moehler, Daniele Marrelli, Maria Antonietta Mazzei, Davide Melisi, Carlo Milandri, Paul Stefan Moenig, Bianca Mostert, Gianni Mura, Wojciech Polkowski, John Reynolds, Luca Saragoni, Mark I. Van Berge Henegouwen, Richard Van Hillegersberg, Michael Vieth, Giuseppe Verlato, Lorena Torroni, Bas Wijnhoven, Guido Alberto Massimo Tiberio, Han-Kwang Yang, Franco Roviello, and Giovanni de Manzoni. International consensus on the management of metastatic gastric cancer: step by step in the foggy landscape. Gastric Cancer, 27:649-671, Apr 2024. URL: https://doi.org/10.1007/s10120-024-01479-5, doi:10.1007/s10120-024-01479-5. This article has 28 citations and is from a domain leading peer-reviewed journal.

12. (morgagni2024internationalconsensuson pages 11-13): Paolo Morgagni, Maria Bencivenga, Fatima Carneiro, Stefano Cascinu, Sarah Derks, Maria Di Bartolomeo, Claire Donohoe, Clarisse Eveno, Suzanne Gisbertz, Peter Grimminger, Ines Gockel, Heike Grabsch, Paulo Kassab, Rupert Langer, Sara Lonardi, Marco Maltoni, Sheraz Markar, Markus Moehler, Daniele Marrelli, Maria Antonietta Mazzei, Davide Melisi, Carlo Milandri, Paul Stefan Moenig, Bianca Mostert, Gianni Mura, Wojciech Polkowski, John Reynolds, Luca Saragoni, Mark I. Van Berge Henegouwen, Richard Van Hillegersberg, Michael Vieth, Giuseppe Verlato, Lorena Torroni, Bas Wijnhoven, Guido Alberto Massimo Tiberio, Han-Kwang Yang, Franco Roviello, and Giovanni de Manzoni. International consensus on the management of metastatic gastric cancer: step by step in the foggy landscape. Gastric Cancer, 27:649-671, Apr 2024. URL: https://doi.org/10.1007/s10120-024-01479-5, doi:10.1007/s10120-024-01479-5. This article has 28 citations and is from a domain leading peer-reviewed journal.

13. (shitara2023…advancedunresectable pages 2-2): K Shitara, F Lordick, YJ Bang, P Enzinger, and D Ilson. … advanced unresectable or metastatic gastric or gastro-oesophageal junction adenocarcinoma (spotlight): a multicentre, randomised, double-blind, phase 3 trial. Unknown journal, 2023.

14. (shah2023zolbetuximabpluscapox pages 7-8): Manish A. Shah, Kohei Shitara, Jaffer A. Ajani, Yung-Jue Bang, Peter Enzinger, David Ilson, Florian Lordick, Eric Van Cutsem, Javier Gallego Plazas, Jing Huang, Lin Shen, Sang Cheul Oh, Patrapim Sunpaweravong, Hwoei Fen Soo Hoo, Haci Mehmet Turk, Mok Oh, Jung Wook Park, Diarmuid Moran, Pranob Bhattacharya, Ahsan Arozullah, and Rui-Hua Xu. Zolbetuximab plus capox in cldn18.2-positive gastric or gastroesophageal junction adenocarcinoma: the randomized, phase 3 glow trial. Nature Medicine, 29:2133-2141, Jul 2023. URL: https://doi.org/10.1038/s41591-023-02465-7, doi:10.1038/s41591-023-02465-7. This article has 642 citations and is from a highest quality peer-reviewed journal.

15. (shitara2025trastuzumabderuxtecanor media d6d76080): Kohei Shitara, Eric Van Cutsem, Mahmut Gümüş, Sara Lonardi, Christelle de la Fouchardière, Clélia Coutzac, Jeroen Dekervel, Daniel Hochhauser, Lin Shen, Wasat Mansoor, Bo Liu, Lorenzo Fornaro, Min-Hee Ryu, Jeeyun Lee, Cátia Faustino, Jean-Philippe Metges, Josep Tabernero, Fábio Franke, Yelena Y. Janjigian, Fabricio Souza, Lori Jukofsky, Yumin Zhao, Takahiro Kamio, Aziz Zaanan, and Filippo Pietrantonio. Trastuzumab deruxtecan or ramucirumab plus paclitaxel in gastric cancer. New England Journal of Medicine, 393:336-348, Jul 2025. URL: https://doi.org/10.1056/nejmoa2503119, doi:10.1056/nejmoa2503119. This article has 88 citations and is from a highest quality peer-reviewed journal.

16. (morgagni2024internationalconsensuson pages 16-17): Paolo Morgagni, Maria Bencivenga, Fatima Carneiro, Stefano Cascinu, Sarah Derks, Maria Di Bartolomeo, Claire Donohoe, Clarisse Eveno, Suzanne Gisbertz, Peter Grimminger, Ines Gockel, Heike Grabsch, Paulo Kassab, Rupert Langer, Sara Lonardi, Marco Maltoni, Sheraz Markar, Markus Moehler, Daniele Marrelli, Maria Antonietta Mazzei, Davide Melisi, Carlo Milandri, Paul Stefan Moenig, Bianca Mostert, Gianni Mura, Wojciech Polkowski, John Reynolds, Luca Saragoni, Mark I. Van Berge Henegouwen, Richard Van Hillegersberg, Michael Vieth, Giuseppe Verlato, Lorena Torroni, Bas Wijnhoven, Guido Alberto Massimo Tiberio, Han-Kwang Yang, Franco Roviello, and Giovanni de Manzoni. International consensus on the management of metastatic gastric cancer: step by step in the foggy landscape. Gastric Cancer, 27:649-671, Apr 2024. URL: https://doi.org/10.1007/s10120-024-01479-5, doi:10.1007/s10120-024-01479-5. This article has 28 citations and is from a domain leading peer-reviewed journal.

17. (morgagni2024internationalconsensuson pages 8-9): Paolo Morgagni, Maria Bencivenga, Fatima Carneiro, Stefano Cascinu, Sarah Derks, Maria Di Bartolomeo, Claire Donohoe, Clarisse Eveno, Suzanne Gisbertz, Peter Grimminger, Ines Gockel, Heike Grabsch, Paulo Kassab, Rupert Langer, Sara Lonardi, Marco Maltoni, Sheraz Markar, Markus Moehler, Daniele Marrelli, Maria Antonietta Mazzei, Davide Melisi, Carlo Milandri, Paul Stefan Moenig, Bianca Mostert, Gianni Mura, Wojciech Polkowski, John Reynolds, Luca Saragoni, Mark I. Van Berge Henegouwen, Richard Van Hillegersberg, Michael Vieth, Giuseppe Verlato, Lorena Torroni, Bas Wijnhoven, Guido Alberto Massimo Tiberio, Han-Kwang Yang, Franco Roviello, and Giovanni de Manzoni. International consensus on the management of metastatic gastric cancer: step by step in the foggy landscape. Gastric Cancer, 27:649-671, Apr 2024. URL: https://doi.org/10.1007/s10120-024-01479-5, doi:10.1007/s10120-024-01479-5. This article has 28 citations and is from a domain leading peer-reviewed journal.

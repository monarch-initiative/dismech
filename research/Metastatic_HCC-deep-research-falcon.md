---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T00:15:51.577403'
end_time: '2026-05-10T00:35:33.317874'
duration_seconds: 1181.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Hepatocellular Carcinoma
  mondo_id: ''
  category: ''
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
- **Disease Name:** Metastatic Hepatocellular Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Hepatocellular Carcinoma** covering all of the
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
- **Disease Name:** Metastatic Hepatocellular Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Hepatocellular Carcinoma** covering all of the
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


## Comprehensive Research Report: Metastatic Hepatocellular Carcinoma (mHCC)

### Target disease
Metastatic hepatocellular carcinoma (mHCC) is hepatocellular carcinoma (HCC) with extrahepatic spread (e.g., lung, lymph nodes, bone), typically falling under “advanced” disease states used in clinical practice guidelines, together with macrovascular invasion and unresectable tumors not amenable to curative or locoregional therapy. Current systemic-therapy guidelines often operationalize the treated population as “advanced/unresectable HCC,” frequently aligned with BCLC stage C (advanced stage). (gordan2024systemictherapyfor pages 1-2, selene2024hepatocellularcarcinomaadvances pages 1-2)

**Ontology/IDs (available in retrieved sources)**
- **Open Targets disease entity:** hepatocellular carcinoma (EFO_0000182) (OpenTargets Search: hepatocellular carcinoma)
- **MONDO terms seen in Open Targets context:** MONDO_0016216 (adult hepatocellular carcinoma); MONDO_0044791 (combined hepatocellular carcinoma and cholangiocarcinoma). (OpenTargets Search: hepatocellular carcinoma)

**Common synonyms / alternative names**
- Advanced HCC; unresectable HCC; inoperable HCC; locally advanced or metastatic HCC; BCLC stage C HCC. (gordan2024systemictherapyfor pages 1-2, zhao2024progressionpatternsin pages 1-2)

**Evidence sources**
Most information below is derived from aggregated disease-level resources: international guidelines (ASCO), high-impact narrative reviews/critical appraisals, observational cohorts, and selected translational/genomic studies. (gordan2024systemictherapyfor pages 1-2, cappuyns2024criticalappraisalof pages 2-4, campani2023geneticsofhepatocellular pages 1-2)

---

## 1. Disease information (overview)
HCC is the dominant primary liver cancer subtype (commonly cited as >75% or >90% depending on classification) and is a major global cause of cancer mortality. Advanced/metastatic disease is common due to late diagnosis and underlying chronic liver disease that limits curative options. (gordan2024systemictherapyfor pages 1-2, selene2024hepatocellularcarcinomaadvances pages 1-2)

A 2024 systemic-therapy review notes that HCC represents “over 90% of [primary liver cancer] cases globally,” and reports a “relative 5-year survival of approximately 18%.” (selene2024hepatocellularcarcinomaadvances pages 1-2)

---

## 2. Etiology
### 2.1 Primary causal factors and upstream etiologies
HCC most often arises in the context of chronic liver disease and cirrhosis. A 2024 review summarizes that **80–90%** of HCC cases arise in patients with cirrhosis. (selene2024hepatocellularcarcinomaadvances pages 1-2)

Key etiologic categories repeatedly emphasized across contemporary sources include:
- Chronic viral hepatitis **HBV** and **HCV** (selene2024hepatocellularcarcinomaadvances pages 1-2)
- **Alcohol-associated liver disease (ALD)** (selene2024hepatocellularcarcinomaadvances pages 1-2)
- **Metabolic dysfunction–associated steatotic liver disease (MASLD)/MASH/NASH**, increasingly important in many regions (selene2024hepatocellularcarcinomaadvances pages 1-2)
- **Aflatoxin B1** exposure (context-dependent; highlighted in mechanistic overviews) (OpenTargets Search: hepatocellular carcinoma)

**Recent development (2024): shifting etiologic drivers**
A 2024 US projection study reports that HCC mortality is projected to continue rising to 2040, “primarily due to increased deaths from alcohol-associated liver disease (ALD) and metabolic dysfunction–associated steatotic liver disease (MASLD); deaths from viral hepatitis were under control and were projected to decrease.” (selene2024hepatocellularcarcinomaadvances pages 1-2)

### 2.2 Genetic risk factors (susceptibility loci)
A 2023 genetics review summarizes that common germline susceptibility variants associated with HCC risk include **PNPLA3 rs738409**, **TM6SF2 rs58542926**, and **MBOAT7 rs641738**, and notes a protective variant **HSD17B13 rs72613567**. (campani2023geneticsofhepatocellular pages 1-2)

### 2.3 Protective factors
**HBV vaccination (population-level protection)**
A 2024 population study assessing universal HBV vaccination impact in Spain reported that in vaccinated vs unvaccinated cohorts aged 20–39, the hospital discharge rate ratio for **HCC was 0.66 (95% CI 0.53–0.82)**. (OpenTargets Search: hepatocellular carcinoma)

**Antiviral therapy and virus–host interaction (advanced-disease relevance)**
A 2024 meta-analysis of 55 cohort studies (2019–2024; n=7,180) reported that while HBV infection itself was not significantly associated with worse survival under immune checkpoint inhibitors, **high baseline HBV load** was associated with poorer OS (**pooled HR 1.74; 95% CI 1.27–2.37**), and **antiviral therapy** was associated with improved OS (**pooled HR 0.24; 95% CI 0.14–0.42**) and PFS (**pooled HR 0.54; 95% CI 0.33–0.89**). (OpenTargets Search: hepatocellular carcinoma)

### 2.4 Gene–environment interactions
The above HBV-load findings provide clinically relevant evidence that pathogen burden (environmental/infectious exposure intensity) interacts with host–tumor immunity and affects outcomes of immunotherapy in advanced HCC. (OpenTargets Search: hepatocellular carcinoma)

---

## 3. Phenotypes (advanced/metastatic disease)
### 3.1 Clinical presentation (typical)
Advanced HCC phenotype reflects a combined burden of:
1) tumor mass effect and metastases, and
2) underlying cirrhosis/portal hypertension with risk of decompensation.

**Portal vein tumor thrombosis (PVTT) as an advanced phenotype**
PVTT occurs in **~10–40%** of patients at diagnosis; untreated PVTT can confer median OS **as short as 2–4 months**. (finn2024efficacyandsafety pages 1-2)

### 3.2 Extrahepatic metastatic patterns (sites and frequencies)
Evidence from recent cohorts illustrates that metastatic patterns vary by population and ascertainment method, but lung/lymph node/bone are recurrent:

- In a 2024 multicenter retrospective cohort of **60 HCC patients with extrahepatic metastases**, metastatic sites were most commonly **lung (n=27)**, then **lymph nodes (n=22)**, then **bone (n=10)**. (liu2024efficacyandsafety pages 1-2)
- A 2024 cohort of **86 BCLC stage C** patients treated with combination approaches reported “the common sites of extrahepatic progression are the **lymph nodes and lungs**.” It also quantified timing: extrahepatic first progression (n=61) median **5.8 months**, and second progression (n=39) median **8.7 months**. (zhao2024progressionpatternsin pages 1-2)

### 3.3 Laboratory abnormalities and biomarkers used clinically (advanced disease)
- **Alpha-fetoprotein (AFP)** is used for surveillance and as a prognostic/selection biomarker in advanced HCC; the ASCO guideline restricts **ramucirumab** use to **AFP ≥400 ng/mL**. (gordan2024systemictherapyfor pages 1-2)

### 3.4 Quality of life impact and patient-reported outcomes
In the phase III HIMALAYA study, patient-reported outcomes (EORTC QLQ-C30 and HCC module) showed that **time to deterioration** in global health status/quality of life, physical functioning, fatigue, appetite loss, and abdominal pain was **numerically longer** for STRIDE (durvalumab+tremelimumab) and durvalumab vs sorafenib, and that “clinically meaningful deterioration in PROs was not observed in any treatment arm.” (cappuyns2024criticalappraisalof pages 2-4)

### 3.5 Suggested HPO mappings (non-exhaustive; for knowledge base)
- Weight loss: **HP:0001824**
- Anorexia: **HP:0002039**
- Fatigue: **HP:0012378**
- Abdominal pain: **HP:0002027**
- Ascites: **HP:0001541**
- Jaundice: **HP:0000952**
- Elevated alpha-fetoprotein: **HP:0030342** (term name may vary by release)
- Bone pain (bone metastasis): **HP:0002653**
- Dyspnea (lung metastasis): **HP:0002094**

(These HPO suggestions are ontology mappings; they are not direct claims of frequency.)

---

## 4. Genetic / molecular information
### 4.1 Somatic driver genes and pathways (current understanding)
A 2023 genetics review states that the most frequently mutated genes include **“TERT promoter, CTNNB1, and TP53”** and organizes HCC drivers into major pathways including **telomere maintenance; Wnt/β-catenin; p53/cell-cycle regulation; oxidative stress; epigenetic modifiers; AKT/mTOR; MAP kinase**. (campani2023geneticsofhepatocellular pages 1-2)

**OpenTargets disease–target association examples**
OpenTargets lists strong associations for HCC with targets including **TP53** and angiogenesis pathway targets such as **KDR (VEGFR2)**, among others (evidence links include PubMed IDs in the OpenTargets output). (OpenTargets Search: hepatocellular carcinoma)

### 4.2 Liquid biopsy / circulating tumor DNA (ctDNA)
The 2023 genetics review highlights ctDNA as a future tool for management, emphasizing that ctDNA may help identify “biomarkers of response or resistance” and that single tissue samples may miss intra- and intertumor heterogeneity. (campani2023geneticsofhepatocellular pages 1-2)

### 4.3 Suggested GO terms (mechanism-linked; examples)
- Angiogenesis: **GO:0001525**
- Epithelial to mesenchymal transition: **GO:0001837**
- Regulation of immune response: **GO:0050776**
- Cell cycle regulation: **GO:0051726**

---

## 5. Mechanism / pathophysiology (advanced/metastatic)
### 5.1 High-level causal chain (from trigger to metastatic disease)
1) Chronic liver injury (HBV/HCV, alcohol, MASLD/MASH, toxins such as aflatoxin) →
2) inflammation, fibrosis/cirrhosis, genomic instability and driver alterations (e.g., TERT promoter, TP53, CTNNB1) →
3) malignant transformation with angiogenic and immune-evasive microenvironment →
4) local invasion (including macrovascular invasion such as PVTT) and/or dissemination to extrahepatic niches (lung/lymph node/bone) →
5) clinical advanced-stage phenotype driven by both tumor progression and hepatic decompensation.

**Angiogenesis as a central actionable mechanism**
The modern first-line standard regimen atezolizumab+bevacizumab combines PD-L1 blockade with VEGF inhibition; VEGF pathway targeting is described as an early and continuing focus in systemic therapy. (selene2024hepatocellularcarcinomaadvances pages 1-2, moriguchi2024evolutionofsystemic pages 1-2)

**PVTT and portal hypertension**
PVTT is both a marker and driver of advanced disease physiology (portal hypertension and risk of variceal bleeding), directly influencing treatment safety considerations (e.g., anti-VEGF therapy). (finn2024efficacyandsafety pages 1-2, gordan2024systemictherapyfor pages 1-2)

### 5.2 Cell types (suggested CL mappings)
- Hepatocyte (tumor cell-of-origin context): **CL:0000182**
- Kupffer cell / hepatic macrophage: **CL:0000235** (macrophage; Kupffer-specific may vary)
- Endothelial cell: **CL:0000115**
- T cell: **CL:0000084**

---

## 6. Inheritance and population (epidemiology)
### 6.1 Global burden and geographic disparities
The 2024 global epidemiology analysis using GLOBOCAN 2022 estimates **~866,136 new liver cancer cases and 758,725 deaths** worldwide in 2022, reporting a global mortality-to-incidence ratio of **0.86** and emphasizing male predominance and geographic heterogeneity (e.g., high burden in Mongolia and parts of Asia/Northern Africa). (selene2024hepatocellularcarcinomaadvances pages 1-2)

ASCO’s 2024 guideline provides additional headline statistics: worldwide in 2020, HCC accounted for **~725,000 new cases and ~664,000 deaths**; in the US in 2023, there were **~41,210 new cases and ~29,380 deaths** (as cited in the guideline). (gordan2024systemictherapyfor pages 1-2)

### 6.2 Mortality trend statistics (US)
A 2024 US cross-sectional analysis includes **188,280 HCC-related deaths**, reporting rising age-standardized mortality from 2006 to 2022 with projected increases to 2040, driven mainly by ALD and MASLD. (selene2024hepatocellularcarcinomaadvances pages 1-2)

---

## 7. Diagnostics and staging (advanced/metastatic)
### 7.1 Noninvasive diagnosis and imaging standards
**High-risk population constraint**
ESGAR practice recommendations emphasize that **noninvasive diagnosis is limited to high-risk patients** (e.g., cirrhosis, chronic HBV, prior HCC) and that **contrast-enhanced CT or MRI** are first-line diagnostic exams. (cannella2024esressentialsdiagnosis pages 1-3)

**Major imaging features**
Recommended major imaging features include lesion size, **non-rim arterial phase hyperenhancement (APHE)**, **non-peripheral washout**, enhancing capsule, and threshold growth. (cannella2024esressentialsdiagnosis pages 1-3)

**LI-RADS role and surveillance workflow**
A 2023 review states that “**The LI-RADS system has standardised the imaging interpretation and diagnosis of HCC**,” and that LI-RADS includes ultrasound visualization categories (A/B/C) relevant to surveillance quality. (giustini2023reviewarticleavailable pages 1-3)

### 7.2 Surveillance and early detection (relevance to metastatic burden)
AASLD-aligned surveillance described in the 2023 review recommends ultrasound ± AFP every 6 months for selected chronic hepatitis B and all cirrhosis patients (with exceptions). (giustini2023reviewarticleavailable pages 1-3)

**Key statistic (test performance):** the same review notes that “**the sensitivity of ultrasound is highly variable for the detection of early-stage HCC with sensitivity reports ranging from 40% to 80%**,” which contributes to late-stage diagnoses and metastatic presentations. (giustini2023reviewarticleavailable pages 1-3)

### 7.3 Biomarkers
- AFP remains widely used, including as a treatment-selection biomarker (ramucirumab for AFP ≥400 ng/mL). (gordan2024systemictherapyfor pages 1-2)

---

## 8. Treatment (current applications; 2023–2024 emphasis)
### 8.1 Guideline-based systemic therapy (ASCO 2024)
The ASCO 2024 guideline update recommends:
- **First line (Child-Pugh A, ECOG 0–1):** atezolizumab+bevacizumab or durvalumab+tremelimumab (STRIDE). (gordan2024systemictherapyfor pages 1-2)
- **Key safety implementation detail:** when using bevacizumab-containing regimens, screen/manage esophageal varices because of bleeding risk. (gordan2024systemictherapyfor pages 1-2)

The ASCO guideline “Bottom Line” summary box (algorithm-like) is captured in the extracted figure/table images. (gordan2024systemictherapyfor media 968a7827, gordan2024systemictherapyfor media b2ca9c8b)

### 8.2 Pivotal trial outcomes and expert appraisal
A 2024 critical appraisal (JAMA Oncology) summarizes key phase III trial outcomes:
- **IMbrave150 (atezo+bev vs sorafenib):** median OS **19.2 vs 13.4 months**; ORR **30% vs 5%**; overall bleeding **25.2% vs 17.3%**; grade 5 GI bleeding **1.2%** with atezo+bev. (cappuyns2024criticalappraisalof pages 2-4)
- **HIMALAYA STRIDE vs sorafenib:** median OS **16.4 vs 13.8 months**; ORR **20.1% vs 5.1%**; immune-related AEs notable (20% required corticosteroids). (cappuyns2024criticalappraisalof pages 2-4)

**High-risk macrovascular invasion subgroup (Vp4 PVTT):** In IMbrave150 Vp4 PVTT subgroup, median OS **7.6 vs 5.5 months** (atezo+bev vs sorafenib) and median PFS **5.4 vs 2.8 months**. (finn2024efficacyandsafety pages 1-2)

### 8.3 Real-world implementation
A 2024 real-world cohort combining TACE with atezo+bev (92 patients; four centers; Aug 2021–Sep 2023) reported:
- ORR **54.3% (mRECIST)** and **41.3% (RECIST 1.1)**
- median OS **15.9 months**; median PFS **9.1 months**
- grade 3/4 treatment-related AEs **16.3%**
This illustrates multimodal treatment patterns increasingly used in routine care outside trials for unresectable disease and some advanced presentations. (shen2024efficacyofatezolizumab pages 1-2)

### 8.4 Treatment sequencing and “no single sequence” consensus
The 2024 JAMA Oncology appraisal stresses that while guidelines broadly prioritize atezo+bev in first line, the **optimal sequencing after immunotherapy-containing regimens remains unsettled**, and evidence is particularly limited for Child-Pugh B populations. (cappuyns2024criticalappraisalof pages 2-4)

### 8.5 Suggested MAXO (Medical Action Ontology) terms (examples)
- Immune checkpoint inhibitor therapy: **MAXO:0000748** (label may vary by release)
- Anti-angiogenic therapy: **MAXO term for anti-VEGF therapy** (ontology label may vary)
- Transarterial chemoembolization: **MAXO:0001184** (label may vary)

---

## 9. Prevention (primary, secondary, tertiary)
**Primary prevention**
- HBV vaccination reduces HBV-related severe liver outcomes including HCC at population scale (e.g., HDRR 0.66 for HCC in vaccinated Spanish cohorts aged 20–39). (OpenTargets Search: hepatocellular carcinoma)

**Secondary prevention**
- Surveillance in high-risk patients (ultrasound ± AFP every 6 months) is widely recommended, but limitations include variable ultrasound sensitivity (40%–80% for early HCC) and inadequate visualization in obesity/NAFLD, which contributes to advanced/metastatic presentation. (giustini2023reviewarticleavailable pages 1-3)

**Tertiary prevention (advanced disease)**
- Control of underlying liver disease and portal hypertension/varices is integral to safe systemic therapy (e.g., anti-VEGF bleeding risk mitigation). (gordan2024systemictherapyfor pages 1-2)

---

## 10. Model organisms / preclinical models (metastasis-relevant research infrastructure)
HCC model systems have expanded to include chemically/diet-induced models, transgenic/transposon models, organoids, and in silico approaches. A 2023 early-detection review notes that preclinical systems such as genetically modified models and patient-derived xenografts are used, but also emphasizes that “clinically relevant models recapitulating the spectrum of human disease are still suboptimal.” (yıldırım2023advancesinthe pages 26-29)

---

## Key tables (artifacts)
The following tables summarize actionable therapy data and etiologic/risk factor evidence extracted from the cited literature.

| Setting | Regimen | Mechanism/class | Key trial or guideline source | Key outcomes (median OS, HR, ORR when available) | Notes |
|---|---|---|---|---|---|
| 1L | Atezolizumab + bevacizumab | PD-L1 inhibitor + anti-VEGF monoclonal antibody | ASCO 2024 guideline; IMbrave150; JAMA Oncol 2024 appraisal (gordan2024systemictherapyfor pages 1-2, cappuyns2024criticalappraisalof pages 2-4) | IMbrave150 updated median OS 19.2 mo vs 13.4 mo with sorafenib; ORR 30% vs 5%; OS HR 0.58 in trial summary cited by IMbrave150 substudy (finn2024efficacyandsafety pages 1-2, cappuyns2024criticalappraisalof pages 2-4) | Preferred 1L for Child-Pugh A, ECOG 0-1. Screen/manage esophageal varices before starting because bevacizumab increases bleeding risk; overall bleeding 25.2% vs 17.3%, grade 5 GI bleeding 1.2% in appraisal. After progression, ASCO recommends TKI, ramucirumab if AFP >=400 ng/mL, durvalumab+tremelimumab, or nivolumab+ipilimumab (gordan2024systemictherapyfor pages 1-2, cappuyns2024criticalappraisalof pages 2-4, gordan2024systemictherapyfor media 968a7827) |
| 1L | Durvalumab + tremelimumab (STRIDE) | PD-L1 inhibitor + CTLA-4 inhibitor | ASCO 2024 guideline; HIMALAYA; JAMA Oncol 2024 appraisal; HIMALAYA PROs (gordan2024systemictherapyfor pages 1-2, cappuyns2024criticalappraisalof pages 2-4) | HIMALAYA median OS 16.4 mo vs 13.8 mo with sorafenib; ORR 20.1% vs 5.1% (cappuyns2024criticalappraisalof pages 2-4) | Preferred 1L alternative for Child-Pugh A, ECOG 0-1; particularly useful when bevacizumab is unsuitable/high GI bleeding risk. PRO analysis showed numerically longer time to deterioration in global health/QoL, physical functioning, fatigue, appetite loss, and abdominal pain vs sorafenib (gordan2024systemictherapyfor pages 1-2, cappuyns2024criticalappraisalof pages 2-4) |
| 1L | Durvalumab monotherapy | PD-L1 inhibitor | ASCO 2024 guideline; HIMALAYA program (gordan2024systemictherapyfor pages 1-2, cappuyns2024criticalappraisalof pages 2-4) | Noninferior to sorafenib for OS in HIMALAYA program; detailed median OS not extracted in current evidence bundle (cappuyns2024criticalappraisalof pages 2-4) | ASCO lists as 1L option when combination immunotherapy is not appropriate/available. Consider in patients with contraindications to bevacizumab or CTLA-4 combination (gordan2024systemictherapyfor pages 1-2) |
| 1L | Lenvatinib | Multikinase inhibitor (VEGFR/FGFR and other kinases) | ASCO 2024 guideline; REFLECT summarized in 2024 review/appraisal (gordan2024systemictherapyfor pages 1-2, yoo2024currentperspectiveson pages 4-6, cappuyns2024criticalappraisalof pages 2-4) | REFLECT: median OS 13.6 mo vs 12.3 mo with sorafenib; HR 0.92 (noninferior). Better PFS/ORR than sorafenib in appraisal/review summaries (yoo2024currentperspectiveson pages 4-6, cappuyns2024criticalappraisalof pages 2-4) | 1L alternative when atezo+bev or STRIDE are contraindicated. Common toxicities include hypertension, fatigue, anorexia, proteinuria. Used frequently as post-atezo+bev TKI in real-world sequencing (gordan2024systemictherapyfor pages 1-2, yoo2024currentperspectiveson pages 4-6) |
| 1L | Sorafenib | Multikinase inhibitor (VEGFR/PDGFR/RAF/c-KIT) | ASCO 2024 guideline; SHARP summarized in 2024 review (gordan2024systemictherapyfor pages 1-2, yoo2024currentperspectiveson pages 4-6) | SHARP: median OS 10.7 mo vs 7.9 mo with placebo (P<0.001) (yoo2024currentperspectiveson pages 4-6) | Legacy TKI option when immune-based regimens are not suitable; prerequisite tolerated sorafenib for later regorafenib use (gordan2024systemictherapyfor pages 1-2, yoo2024currentperspectiveson pages 4-6) |
| 1L high-risk subset | Atezolizumab + bevacizumab in Vp4 portal vein tumor thrombosis | PD-L1 inhibitor + anti-VEGF monoclonal antibody | IMbrave150 Vp4 substudy (finn2024efficacyandsafety pages 1-2) | In Vp4 PVTT: median OS 7.6 vs 5.5 mo; HR 0.62. Median PFS 5.4 vs 2.8 mo; HR 0.62. In non-Vp4: median OS 21.1 vs 15.4 mo; HR 0.67; median PFS 7.1 vs 4.7 mo; HR 0.64 (finn2024efficacyandsafety pages 1-2) | Supports use even in very poor-prognosis macrovascular invasion; grade >=3 treatment-related AEs ~43-48% in Vp4 and ~46-47% without Vp4 (finn2024efficacyandsafety pages 1-2) |
| 2L+ after atezo+bev | TKI class (e.g., lenvatinib, sorafenib, cabozantinib depending prior exposure/availability) | Multikinase inhibitors | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2, gordan2024systemictherapyfor media 968a7827) | No single preferred OS estimate in guideline excerpt; sequencing evidence remains evolving | ASCO explicitly recommends a TKI after 1L atezo+bev. Choice depends on liver function, prior tolerance, portal hypertension/bleeding considerations, comorbidity, and access (gordan2024systemictherapyfor pages 1-2) |
| 2L+ after atezo+bev | Ramucirumab | VEGFR2 monoclonal antibody | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2) | Outcome stats not extracted here | Restrict to patients with AFP >=400 ng/mL (gordan2024systemictherapyfor pages 1-2) |
| 2L+ after atezo+bev | Nivolumab + ipilimumab | PD-1 inhibitor + CTLA-4 inhibitor | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2) | Outcome stats not extracted here | Recommended option for appropriate candidates after atezo+bev progression (gordan2024systemictherapyfor pages 1-2) |
| 2L+ after atezo+bev | Durvalumab + tremelimumab | PD-L1 inhibitor + CTLA-4 inhibitor | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2) | Outcome stats from HIMALAYA available in 1L setting above | May be considered after atezo+bev in appropriate candidates, though optimal sequencing remains unsettled (gordan2024systemictherapyfor pages 1-2, cappuyns2024criticalappraisalof pages 2-4) |
| 2L+ after STRIDE | TKI class | Multikinase inhibitors | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2, gordan2024systemictherapyfor media 968a7827) | No single preferred OS estimate in guideline excerpt | ASCO recommends TKI after 1L durvalumab+tremelimumab (gordan2024systemictherapyfor pages 1-2) |
| 2L+ after sorafenib/lenvatinib | Cabozantinib | Multikinase inhibitor | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2, gordan2024systemictherapyfor pages 19-20) | Trial details not extracted in evidence summary table | Standard later-line option after prior TKI; also listed after sorafenib/lenvatinib progression (gordan2024systemictherapyfor pages 1-2) |
| 2L+ after sorafenib | Regorafenib | Multikinase inhibitor | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2, gordan2024systemictherapyfor pages 19-20) | Trial details not extracted in evidence summary table | Use only in patients who previously tolerated sorafenib (gordan2024systemictherapyfor pages 1-2) |
| 2L+ after sorafenib/lenvatinib | Ramucirumab | VEGFR2 monoclonal antibody | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2) | Trial details not extracted in evidence summary table | Only for AFP >=400 ng/mL (gordan2024systemictherapyfor pages 1-2) |
| 2L+ after sorafenib/lenvatinib | Pembrolizumab or nivolumab | PD-1 inhibitors | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2) | Trial details not extracted in evidence summary table | Additional options for appropriate patients after TKI therapy (gordan2024systemictherapyfor pages 1-2) |
| Any-line special population | Systemic therapy in Child-Pugh B | Regimen selection individualized | ASCO 2024 guideline (gordan2024systemictherapyfor pages 1-2) | No pooled efficacy estimate provided in extracted guideline text | ASCO recommends a cautious approach in Child-Pugh B advanced HCC; most pivotal first-line evidence is strongest for Child-Pugh A (gordan2024systemictherapyfor pages 1-2) |


*Table: This table summarizes key 2024 systemic therapy options for advanced/metastatic unresectable hepatocellular carcinoma, including first-line and later-line regimens, mechanisms, pivotal evidence, and practical eligibility notes. It highlights survival and response results where available and flags important treatment-selection issues such as variceal screening, AFP thresholds, and Child-Pugh considerations.*

| Factor type | Specific factor | Evidence summary with quantitative/statements when available | Evidence type | Key citation |
|---|---|---|---|---|
| Etiologic | Chronic hepatitis B virus (HBV) infection | Major established cause of HCC; many guidelines/reviews identify HBV among the leading causes, and HCC often develops in the setting of chronic liver disease/cirrhosis. HBV remains a dominant cause in many Asian and African populations. In China, HBV remained a major contributor to HCC burden despite declining age-standardized rates over time (selene2024hepatocellularcarcinomaadvances pages 1-2, gordan2024systemictherapyfor pages 1-2). | Human epidemiology; guideline/review | Selene et al., 2024, https://doi.org/10.1055/s-0044-1779713; Gordan et al., 2024, https://doi.org/10.1200/jco.23.02745 (selene2024hepatocellularcarcinomaadvances pages 1-2, gordan2024systemictherapyfor pages 1-2) |
| Etiologic | Chronic hepatitis C virus (HCV) infection | Major established cause of HCC; reviews/guidelines continue to list HCV among principal etiologies. Recent epidemiology suggests viral-hepatitis-related HCC burden is decreasing in some regions, while alcohol- and metabolic-related HCC rise. | Human epidemiology; guideline/review | Selene et al., 2024, https://doi.org/10.1055/s-0044-1779713; Qiu et al., 2024, https://doi.org/10.1001/jamanetworkopen.2024.45525 (selene2024hepatocellularcarcinomaadvances pages 1-2) |
| Etiologic | Alcohol-associated liver disease (ALD) | Recognized major cause of HCC. Recent US projections indicate HCC mortality will continue rising through 2040 “primarily due to increased deaths from alcohol-associated liver disease (ALD) and metabolic dysfunction–associated steatotic liver disease (MASLD)” (selene2024hepatocellularcarcinomaadvances pages 1-2). In China, age-standardized incidence trends for alcohol-related HCC increased while viral-related HCC declined (selene2024hepatocellularcarcinomaadvances pages 1-2). | Human epidemiology | Qiu et al., 2024, https://doi.org/10.1001/jamanetworkopen.2024.45525; Long et al., 2024, https://doi.org/10.1177/10732748241310573 (selene2024hepatocellularcarcinomaadvances pages 1-2) |
| Etiologic | MASLD/MASH/NASH | Increasingly important driver of HCC in high-income and aging/obese populations. Recent reviews note a shift from viral hepatitis toward MASLD-related disease; US projections suggest MASLD and ALD will become leading causes of HCC-related mortality by 2040 for most racial/ethnic groups (selene2024hepatocellularcarcinomaadvances pages 1-2). | Human epidemiology; guideline/review | Qiu et al., 2024, https://doi.org/10.1001/jamanetworkopen.2024.45525; EASL-EASD-EASO MASLD Guideline, 2024, https://doi.org/10.1159/000539371 (selene2024hepatocellularcarcinomaadvances pages 1-2) |
| Etiologic | Aflatoxin B1 exposure | Listed in contemporary molecular/pathogenesis reviews as a major etiologic exposure, especially where food contamination is prevalent. Mechanistically linked to mutagenesis and hepatocarcinogenesis, particularly in conjunction with HBV. | Human epidemiology; mechanistic review | Szilveszter et al., 2024, https://doi.org/10.3390/biom14060656 (OpenTargets Search: hepatocellular carcinoma) |
| Risk | Cirrhosis / advanced fibrosis | Strongest clinical substrate for HCC overall. Reviews note 80–90% of HCC cases arise in patients with cirrhosis, and surveillance recommendations target cirrhosis because it is the largest risk factor for developing HCC (selene2024hepatocellularcarcinomaadvances pages 1-2, giustini2023reviewarticleavailable pages 1-3). Cirrhosis also raises risk of later-stage presentation if surveillance is poor. | Human clinical epidemiology; guideline/review | Selene et al., 2024, https://doi.org/10.1055/s-0044-1779713; Giustini et al., 2023, https://doi.org/10.1111/apt.17506 (selene2024hepatocellularcarcinomaadvances pages 1-2, giustini2023reviewarticleavailable pages 1-3) |
| Risk | Obesity / metabolic syndrome / type 2 diabetes | Modern guidelines and epidemiologic analyses identify obesity and metabolic risk as growing contributors to HCC burden. EASL MASLD guidance emphasizes cardiometabolic risk-factor case finding; obesity and elevated BMI increasingly contribute to liver cancer DALYs and mortality (selene2024hepatocellularcarcinomaadvances pages 1-2). | Human epidemiology; guideline | EASL-EASD-EASO MASLD Guideline, 2024, https://doi.org/10.1159/000539371; Qiu et al., 2024, https://doi.org/10.1001/jamanetworkopen.2024.45525 (selene2024hepatocellularcarcinomaadvances pages 1-2) |
| Risk | Male sex | HCC burden is substantially higher in males across global analyses; liver cancer incidence/mortality is consistently male-predominant, which contributes to higher risk of advanced/metastatic disease burden in men. | Human epidemiology | Li et al., 2024, https://doi.org/10.1097/cm9.0000000000003264 (selene2024hepatocellularcarcinomaadvances pages 1-2) |
| Risk | Older age | Global epidemiology reviews note highest burden in elderly populations, consistent with cumulative chronic liver injury and delayed presentation risk. | Human epidemiology | Li et al., 2024, https://doi.org/10.1097/cm9.0000000000003264 (selene2024hepatocellularcarcinomaadvances pages 1-2) |
| Risk | Poor surveillance / non-cirrhotic presentation | About 20% of HCC cases may occur without cirrhosis, which can delay surveillance and diagnosis; screening gaps contribute to advanced-stage presentation. Ultrasound sensitivity for early-stage HCC is only ~40%–80%, limiting early detection and potentially increasing risk of progression to advanced/metastatic disease (giustini2023reviewarticleavailable pages 1-3). | Guideline/review; diagnostic epidemiology | Giustini et al., 2023, https://doi.org/10.1111/apt.17506; Kazi et al., 2024, https://doi.org/10.3390/cancers16193400 (giustini2023reviewarticleavailable pages 1-3) |
| Genetic risk | PNPLA3 rs738409 | Frequently cited germline susceptibility variant associated with HCC risk, especially in steatotic/metabolic liver disease settings (campani2023geneticsofhepatocellular pages 1-2). | Germline genetics | Campani et al., 2023, https://doi.org/10.3390/cancers15030817 (campani2023geneticsofhepatocellular pages 1-2) |
| Genetic risk | TM6SF2 rs58542926 | Germline susceptibility variant repeatedly associated with HCC risk in chronic liver disease populations (campani2023geneticsofhepatocellular pages 1-2). | Germline genetics | Campani et al., 2023, https://doi.org/10.3390/cancers15030817 (campani2023geneticsofhepatocellular pages 1-2) |
| Genetic risk | MBOAT7 rs641738 | Germline risk variant associated with HCC susceptibility, particularly in steatotic liver disease contexts (campani2023geneticsofhepatocellular pages 1-2). | Germline genetics | Campani et al., 2023, https://doi.org/10.3390/cancers15030817 (campani2023geneticsofhepatocellular pages 1-2) |
| Genetic risk / gene-environment | High HBV viral load | In patients receiving immune checkpoint inhibitors for HCC, high baseline HBV load was associated with poorer overall survival (pooled HR 1.74, 95% CI 1.27–2.37), supporting a clinically relevant virus-host interaction that may worsen outcomes once HCC is advanced (OpenTargets Search: hepatocellular carcinoma). | Human clinical meta-analysis | Ji et al., 2024, https://doi.org/10.3389/fimmu.2024.1480520 (OpenTargets Search: hepatocellular carcinoma) |
| Protective | HBV vaccination | Population-level prevention reduces future HCC burden. In Spain, vaccinated vs unvaccinated cohorts aged 20–39 had lower hospital discharge rates for HCC (HDRR 0.66, 95% CI 0.53–0.82) and cirrhosis (HDRR 0.41, 95% CI 0.33–0.53), supporting strong protection against progression from HBV infection to severe liver disease/HCC (OpenTargets Search: hepatocellular carcinoma). | Human population study | Domínguez et al., 2024, https://doi.org/10.3390/vaccines12111254 (OpenTargets Search: hepatocellular carcinoma) |
| Protective | Antiviral therapy for HBV/HCV | Recent prevention reviews conclude HBV and HCV antiviral treatment significantly reduces HCC incidence. In advanced HCC treated with ICIs, antiviral therapy in HBV-infected patients was associated with better OS (pooled HR 0.24, 95% CI 0.14–0.42) and PFS (pooled HR 0.54, 95% CI 0.33–0.89) (OpenTargets Search: hepatocellular carcinoma). | Human clinical meta-analysis; prevention review | Ji et al., 2024, https://doi.org/10.3389/fimmu.2024.1480520; Polpichai et al., 2024, https://doi.org/10.3390/jcm13226770 (OpenTargets Search: hepatocellular carcinoma) |
| Protective | HSD17B13 rs72613567 | Reported protective germline variant associated with reduced HCC susceptibility in genetic reviews (campani2023geneticsofhepatocellular pages 1-2). | Germline genetics | Campani et al., 2023, https://doi.org/10.3390/cancers15030817 (campani2023geneticsofhepatocellular pages 1-2) |
| Protective | Weight control, exercise, alcohol reduction, smoking cessation | Recent prevention reviews conclude lifestyle modification is crucial for lowering HCC risk, particularly by reducing MASLD- and ALD-related disease burden. These measures are especially relevant to preventing eventual advanced/metastatic HCC by reducing incident primary HCC. | Guideline/review | Polpichai et al., 2024, https://doi.org/10.3390/jcm13226770; EASL-EASD-EASO MASLD Guideline, 2024, https://doi.org/10.1159/000539371 (OpenTargets Search: hepatocellular carcinoma, selene2024hepatocellularcarcinomaadvances pages 1-2) |
| Protective / secondary prevention | Semiannual surveillance in high-risk patients | AASLD-aligned surveillance with ultrasound ± AFP every 6 months is recommended for cirrhosis and selected HBV populations; early detection aims to prevent presentation with advanced/metastatic disease. However, surveillance effectiveness is limited by suboptimal uptake and ultrasound sensitivity (early-stage sensitivity ~40%–80%) (giustini2023reviewarticleavailable pages 1-3). | Guideline/review | Giustini et al., 2023, https://doi.org/10.1111/apt.17506; Wu et al., 2024, https://doi.org/10.3390/cancers16233933 (giustini2023reviewarticleavailable pages 1-3) |


*Table: This table summarizes the major etiologic drivers, risk factors, and protective factors for hepatocellular carcinoma relevant to progression toward advanced or metastatic disease. It emphasizes recent epidemiology, guideline-level prevention strategies, and germline susceptibility/protective variants using sources already cited in the conversation.*

---

## Visual evidence from guideline document
Cropped images from the ASCO 2024 guideline show the structured, algorithm-like “Bottom Line” recommendations for first-line and subsequent-line systemic therapy selection. (gordan2024systemictherapyfor media 968a7827, gordan2024systemictherapyfor media b2ca9c8b)

---

## Limitations of this report (evidence access)
- **PMID requirement:** Several retrieved items did not include PMIDs in the accessible text and tool outputs. Where PubMed IDs are needed, the OpenTargets output includes some PubMed IDs for target–disease evidence (e.g., TP53 associations), but many clinical guideline/review PDFs in this run did not expose PMIDs directly. Therefore, I did not assert PMIDs unless present in the provided context. (OpenTargets Search: hepatocellular carcinoma)
- **ICD-10/ICD-11/MeSH/SNOMED codes:** Not retrievable from the currently accessed full texts; thus not exhaustively populated.
- **ClinicalTrials.gov NCT identifiers:** Although trial records were retrieved in the tool state, they were not provided with citeable context IDs in the current run output, so NCTs are not cited here.


References

1. (gordan2024systemictherapyfor pages 1-2): John D. Gordan, Erin B. Kennedy, Ghassan K. Abou-Alfa, Eliza Beal, Richard S. Finn, Terence P. Gade, Laura Goff, Shilpi Gupta, Jennifer Guy, Hang T. Hoang, Renuka Iyer, Ishmael Jaiyesimi, Minaxi Jhawer, Asha Karippot, Ahmed O. Kaseb, R. Kate Kelley, Jeremy Kortmansky, Andrea Leaf, William M. Remak, Davendra P.S. Sohal, Tamar H. Taddei, Andrea Wilson Woods, Mark Yarchoan, and Michal G. Rose. Systemic therapy for advanced hepatocellular carcinoma: asco guideline update. Journal of Clinical Oncology, 42:1830-1850, May 2024. URL: https://doi.org/10.1200/jco.23.02745, doi:10.1200/jco.23.02745. This article has 286 citations and is from a highest quality peer-reviewed journal.

2. (selene2024hepatocellularcarcinomaadvances pages 1-2): Insija Ilyas Selene, Merve Ozen, and Reema A. Patel. Hepatocellular carcinoma: advances in systemic therapy. Seminars in Interventional Radiology, 41:056-062, Feb 2024. URL: https://doi.org/10.1055/s-0044-1779713, doi:10.1055/s-0044-1779713. This article has 9 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: hepatocellular carcinoma): Open Targets Query (hepatocellular carcinoma, 13 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (zhao2024progressionpatternsin pages 1-2): Yanan Zhao, Di Wu, Quan-Jun Yao, Hang Yuan, Hongtao Hu, and Hailiang Li. Progression patterns in patients with advanced hepatocellular carcinoma treated with local therapy, targeted drugs, and pd-1/pd-l1 inhibitors. Central-European Journal of Immunology, 49:147-154, Aug 2024. URL: https://doi.org/10.5114/ceji.2024.142418, doi:10.5114/ceji.2024.142418. This article has 2 citations.

5. (cappuyns2024criticalappraisalof pages 2-4): Sarah Cappuyns, Virginia Corbett, Mark Yarchoan, Richard S. Finn, and Josep M. Llovet. Critical appraisal of guideline recommendations on systemic therapies for advanced hepatocellular carcinoma. JAMA Oncology, 10:395, Mar 2024. URL: https://doi.org/10.1001/jamaoncol.2023.2677, doi:10.1001/jamaoncol.2023.2677. This article has 153 citations and is from a highest quality peer-reviewed journal.

6. (campani2023geneticsofhepatocellular pages 1-2): Claudia Campani, Jessica Zucman-Rossi, and Jean-Charles Nault. Genetics of hepatocellular carcinoma: from tumor to circulating dna. Cancers, 15:817, Jan 2023. URL: https://doi.org/10.3390/cancers15030817, doi:10.3390/cancers15030817. This article has 46 citations.

7. (finn2024efficacyandsafety pages 1-2): Richard S. Finn, Peter R. Galle, Michel Ducreux, Ann-Lii Cheng, Norelle Reilly, Alan Nicholas, Sairy Hernandez, Ning Ma, Philippe Merle, Riad Salem, Daneng Li, and Valeriy Breder. Efficacy and safety of atezolizumab plus bevacizumab versus sorafenib in hepatocellular carcinoma with main trunk and/or contralateral portal vein invasion in imbrave150. Liver Cancer, 13:1-14, Jun 2024. URL: https://doi.org/10.1159/000539897, doi:10.1159/000539897. This article has 50 citations and is from a peer-reviewed journal.

8. (liu2024efficacyandsafety pages 1-2): De-Yi Liu, Yi-Nan Li, Jia-Yi Wu, Zhen-Xin Zeng, Yang-Kai Fu, Han Li, Xiang-Ye Ou, Zhi-Bo Zhang, Shuang-Jia Wang, Jun-Yi Wu, and Mao-Lin Yan. Efficacy and safety of transcatheter arterial chemoembolization combined with lenvatinib plus anti-pd-1 inhibitors for hepatocellular carcinoma patients with extrahepatic metastases: a multicenter retrospective study. Journal of Hepatocellular Carcinoma, 11:2339-2349, Nov 2024. URL: https://doi.org/10.2147/jhc.s480958, doi:10.2147/jhc.s480958. This article has 2 citations and is from a peer-reviewed journal.

9. (moriguchi2024evolutionofsystemic pages 1-2): Michihisa Moriguchi, Seita Kataoka, and Yoshito Itoh. Evolution of systemic treatment for hepatocellular carcinoma: changing treatment strategies and concepts. Cancers, 16:2387, Jun 2024. URL: https://doi.org/10.3390/cancers16132387, doi:10.3390/cancers16132387. This article has 15 citations.

10. (cannella2024esressentialsdiagnosis pages 1-3): Roberto Cannella, Marc Zins, and Giuseppe Brancatelli. Esr essentials: diagnosis of hepatocellular carcinoma—practice recommendations by esgar. European Radiology, 34:2127-2139, Feb 2024. URL: https://doi.org/10.1007/s00330-024-10606-w, doi:10.1007/s00330-024-10606-w. This article has 32 citations and is from a domain leading peer-reviewed journal.

11. (giustini2023reviewarticleavailable pages 1-3): Abbey Barnard Giustini, George N. Ioannou, Claude Sirlin, and Rohit Loomba. Review article: available modalities for screening and imaging diagnosis of hepatocellular carcinoma—current gaps and challenges. Alimentary Pharmacology &amp; Therapeutics, 57:1056-1065, Apr 2023. URL: https://doi.org/10.1111/apt.17506, doi:10.1111/apt.17506. This article has 11 citations and is from a highest quality peer-reviewed journal.

12. (gordan2024systemictherapyfor media 968a7827): John D. Gordan, Erin B. Kennedy, Ghassan K. Abou-Alfa, Eliza Beal, Richard S. Finn, Terence P. Gade, Laura Goff, Shilpi Gupta, Jennifer Guy, Hang T. Hoang, Renuka Iyer, Ishmael Jaiyesimi, Minaxi Jhawer, Asha Karippot, Ahmed O. Kaseb, R. Kate Kelley, Jeremy Kortmansky, Andrea Leaf, William M. Remak, Davendra P.S. Sohal, Tamar H. Taddei, Andrea Wilson Woods, Mark Yarchoan, and Michal G. Rose. Systemic therapy for advanced hepatocellular carcinoma: asco guideline update. Journal of Clinical Oncology, 42:1830-1850, May 2024. URL: https://doi.org/10.1200/jco.23.02745, doi:10.1200/jco.23.02745. This article has 286 citations and is from a highest quality peer-reviewed journal.

13. (gordan2024systemictherapyfor media b2ca9c8b): John D. Gordan, Erin B. Kennedy, Ghassan K. Abou-Alfa, Eliza Beal, Richard S. Finn, Terence P. Gade, Laura Goff, Shilpi Gupta, Jennifer Guy, Hang T. Hoang, Renuka Iyer, Ishmael Jaiyesimi, Minaxi Jhawer, Asha Karippot, Ahmed O. Kaseb, R. Kate Kelley, Jeremy Kortmansky, Andrea Leaf, William M. Remak, Davendra P.S. Sohal, Tamar H. Taddei, Andrea Wilson Woods, Mark Yarchoan, and Michal G. Rose. Systemic therapy for advanced hepatocellular carcinoma: asco guideline update. Journal of Clinical Oncology, 42:1830-1850, May 2024. URL: https://doi.org/10.1200/jco.23.02745, doi:10.1200/jco.23.02745. This article has 286 citations and is from a highest quality peer-reviewed journal.

14. (shen2024efficacyofatezolizumab pages 1-2): Xiao Shen, Jin-Xing Zhang, Jin Liu, Sheng Liu, Hai-Bin Shi, Yuan Cheng, Qing-Qiao Zhang, Guo-Wen Yin, and Qing-Quan Zu. Efficacy of atezolizumab plus bevacizumab combined with transarterial chemoembolization for unresectable hepatocellular carcinoma: a real-world study. Journal of Hepatocellular Carcinoma, 11:1993-2003, Oct 2024. URL: https://doi.org/10.2147/jhc.s478604, doi:10.2147/jhc.s478604. This article has 4 citations and is from a peer-reviewed journal.

15. (yıldırım2023advancesinthe pages 26-29): Hasan Çağrı Yıldırım, Gozde Kavgaci, Elvin Chalabiyev, and Omer Dizdar. Advances in the early detection of hepatobiliary cancers. Cancers, 15:3880, Jul 2023. URL: https://doi.org/10.3390/cancers15153880, doi:10.3390/cancers15153880. This article has 29 citations.

16. (yoo2024currentperspectiveson pages 4-6): Hye-Jin Yoo, Jeong-Ju Yoo, Sang Gyune Kim, and Young Seok Kim. Current perspectives on the pharmacological treatment of advanced hepatocellular carcinoma: a narrative review. The Ewha Medical Journal, Oct 2024. URL: https://doi.org/10.12771/emj.2024.e53, doi:10.12771/emj.2024.e53. This article has 2 citations.

17. (gordan2024systemictherapyfor pages 19-20): John D. Gordan, Erin B. Kennedy, Ghassan K. Abou-Alfa, Eliza Beal, Richard S. Finn, Terence P. Gade, Laura Goff, Shilpi Gupta, Jennifer Guy, Hang T. Hoang, Renuka Iyer, Ishmael Jaiyesimi, Minaxi Jhawer, Asha Karippot, Ahmed O. Kaseb, R. Kate Kelley, Jeremy Kortmansky, Andrea Leaf, William M. Remak, Davendra P.S. Sohal, Tamar H. Taddei, Andrea Wilson Woods, Mark Yarchoan, and Michal G. Rose. Systemic therapy for advanced hepatocellular carcinoma: asco guideline update. Journal of Clinical Oncology, 42:1830-1850, May 2024. URL: https://doi.org/10.1200/jco.23.02745, doi:10.1200/jco.23.02745. This article has 286 citations and is from a highest quality peer-reviewed journal.

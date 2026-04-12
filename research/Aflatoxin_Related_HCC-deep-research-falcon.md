---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T12:00:52.419885'
end_time: '2026-04-05T12:09:58.657294'
duration_seconds: 546.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aflatoxin-Related Hepatocellular Carcinoma
  mondo_id: ''
  category: ''
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
- **Disease Name:** Aflatoxin-Related Hepatocellular Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Aflatoxin-Related Hepatocellular Carcinoma** covering all of the
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
- **Disease Name:** Aflatoxin-Related Hepatocellular Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Aflatoxin-Related Hepatocellular Carcinoma** covering all of the
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


# Comprehensive Research Report: Aflatoxin-Related Hepatocellular Carcinoma (HCC)

## Target Disease
- **Disease name:** Aflatoxin-Related Hepatocellular Carcinoma (HCC)
- **MONDO ID:** Not found in the retrieved full-text sources; requires lookup in MONDO/OLS (limitation of current evidence set).
- **Category:** Environment-associated cancer; primary liver cancer (hepatocellular carcinoma) driven in part by food-borne mycotoxin exposure, frequently in synergy with chronic hepatitis B virus (HBV) infection.

## Executive summary (current understanding)
Aflatoxin-related HCC refers to hepatocellular carcinoma in which chronic exposure to aflatoxins—especially **aflatoxin B1 (AFB1)**—has played a causal role, typically evidenced by validated exposure biomarkers and/or a characteristic tumor mutational fingerprint. AFB1 is metabolically activated in hepatocytes to a reactive epoxide that forms DNA adducts and induces a characteristic **G→T transversion** hotspot mutation in **TP53 codon 249 (R249S; AGG→AGT)** that is widely treated as a molecular “fingerprint” of aflatoxin-driven hepatocarcinogenesis. Co-exposure with chronic HBV infection substantially amplifies risk (often supra-multiplicatively), and aflatoxin mitigation is a demonstrably effective public-health strategy in endemic regions. (chen2026aflatoxinandliver pages 1-2, morenoleon2025cooperationbetweenaflatoxininduced pages 1-2, koshiol2026aflatoxinsandhuman pages 1-2, gouas2009theaflatoxininducedtp53 pages 1-2)

## Evidence map (key concepts, biomarkers, and burden)
| Topic | Key finding | Supporting source | Year | Journal | URL | Citation |
|---|---|---|---:|---|---|---|
| Core disease concept / definition | Aflatoxin-related hepatocellular carcinoma is HCC causally linked to chronic dietary exposure to aflatoxins—especially aflatoxin B1 (AFB1), a potent food-borne hepatocarcinogen—with risk amplified where chronic HBV infection co-occurs. | Chen et al. | 2026 | *Toxins* | https://doi.org/10.3390/toxins18020061 | (chen2026aflatoxinandliver pages 1-2) |
| Core disease concept / definition | Aflatoxins are described as “well-established” liver carcinogens; mechanisms include mutagenic DNA adducts, oxidative stress, mitochondrial dysfunction, immune effects, and epigenetic change. | Koshiol et al. | 2026 | *Toxins* | https://doi.org/10.3390/toxins18020090 | (koshiol2026aflatoxinsandhuman pages 1-2) |
| Key causal factors / molecular fingerprint | AFB1 is bioactivated in liver to the 8,9-exo-epoxide, generating AFB1-N7-Gua and FAPY adducts that drive G>T transversions; the hallmark hotspot is TP53 codon 249 AGG→AGT (R249S), regarded as a molecular fingerprint of aflatoxin exposure. | Moreno-León & Aguayo | 2025 | *Journal of Xenobiotics* | https://doi.org/10.3390/jox15040096 | (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2, morenoleon2025cooperationbetweenaflatoxininduced pages 2-4) |
| Key causal factors / HBV synergy | HBV and aflatoxin interact synergistically in hepatocarcinogenesis; HBx functionally suppresses p53 while AFB1 induces TP53 R249S, converging on p53 pathway disruption. | Moreno-León & Aguayo | 2025 | *Journal of Xenobiotics* | https://doi.org/10.3390/jox15040096 | (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2) |
| Key causal factors / tumor frequency | In a Qidong HBV-carrier cohort, TP53 R249S was present in 11/18 available HCC tumors (61%), supporting its strong association with aflatoxin-linked HCC in endemic settings. | Szymańska et al. | 2009 | *Cancer Epidemiology, Biomarkers & Prevention* | https://doi.org/10.1158/1055-9965.EPI-08-1102 | (szymanska2009tp53r249smutations pages 1-2, szymanska2009tp53r249smutations pages 4-5) |
| Exposure biomarker | Urinary AFB1–N7–guanine is a validated biomarker of internal dose and was used in Chinese biomonitoring/prospective studies linking baseline exposure to later HCC risk. | Chen et al. | 2026 | *Toxins* | https://doi.org/10.3390/toxins18020061 | (chen2026aflatoxinandliver pages 2-4, chen2026aflatoxinandliver pages 1-2) |
| Exposure biomarker | AFM1 is listed among validated urinary biomarkers used in population biomonitoring for aflatoxin exposure. | Chen et al. | 2026 | *Toxins* | https://doi.org/10.3390/toxins18020061 | (chen2026aflatoxinandliver pages 2-4, chen2026aflatoxinandliver media 0564ad30) |
| Exposure biomarker | Serum AFB1–lysine albumin adducts are established long-term exposure biomarkers; Guangxi case-control data used high serum AFB1-lysine levels jointly with HBV mutations to stratify elevated HCC risk. | Xu et al. | 2010 | *Journal of Hepatology* | https://doi.org/10.1016/j.jhep.2010.04.032 | (xu2010geneticvariationsof pages 1-2) |
| Early-detection biomarker | Circulating TP53 R249S-mutated cfDNA can be detected in plasma/serum before overt cancer and in asymptomatic HBV carriers, supporting early molecular detection in endemic regions. | Villar et al.; Lleonart et al. | 2011; 2005 | *Environmental Health Perspectives*; *Cancer Epidemiology, Biomarkers & Prevention* | https://doi.org/10.1289/ehp.1103539 ; https://doi.org/10.1158/1055-9965.EPI-05-0612 | (lleonart2005quantitativeanalysisof pages 1-2, villar2012aflatoxininducedtp53r249s pages 1-2) |
| Early-detection biomarker / quantitative detail | In The Gambia, plasma TP53 249Ser-mutated DNA was quantified in 89 HCC cases, 42 cirrhosis cases, and 131 controls; HCC cases had the highest median level (2,800 copies/mL), and >10,000 copies/mL strongly associated with HCC. | Lleonart et al. | 2005 | *Cancer Epidemiology, Biomarkers & Prevention* | https://doi.org/10.1158/1055-9965.EPI-05-0612 | (lleonart2005quantitativeanalysisof pages 1-2) |
| Early-detection biomarker / seasonal interaction | In Gambian asymptomatic subjects, R249S positivity was significantly higher in HBsAg-positive individuals surveyed during high-exposure months (61% vs 32%; OR 3.59, 95% CI 2.05–6.30), indicating temporal interaction among aflatoxin exposure, HBV, and TP53 mutation formation/persistence. | Villar et al. | 2011 | *Environmental Health Perspectives* | https://doi.org/10.1289/ehp.1103539 | (szymanska2009tp53r249smutations pages 1-2) |
| Quantitative burden metric | A systematic review/meta-analysis estimated the population attributable risk (PAR) of aflatoxin-related HCC at 17% overall (14–19%). | Liu et al. | 2012 | *European Journal of Cancer* | https://doi.org/10.1016/j.ejca.2012.02.009 | (liu2012populationattributablerisk pages 1-3) |
| Quantitative burden metric / HBV stratification | The same meta-analysis estimated higher PAR in HBV-positive populations (21%) than HBV-negative populations (8.8%), quantifying the aflatoxin–HBV interaction at the population level. | Liu et al. | 2012 | *European Journal of Cancer* | https://doi.org/10.1016/j.ejca.2012.02.009 | (liu2012populationattributablerisk pages 1-3) |
| Real-world prevention relevance | Long-term exposure reduction through dietary shift (maize to rice), food governance, and chemopreventive interception (e.g., oltipraz, chlorophyllin, broccoli sprout beverages) was associated with major biomarker declines and marked reduction in HCC burden in Qidong. | Chen et al.; Chen et al. | 2025; 2026 | *Toxins*; *Toxins* | https://doi.org/10.3390/toxins17020079 ; https://doi.org/10.3390/toxins18020061 | (chen2026aflatoxinandliver pages 1-2, chen2026aflatoxinandliver media 0564ad30) |


*Table: This table summarizes the core definition, causal mechanism, key biomarkers, and burden estimates for aflatoxin-related hepatocellular carcinoma. It is useful as a compact evidence map linking aflatoxin exposure, HBV synergy, TP53 R249S, biomarker-based detection, and population-level impact.*

---

## 1. Disease information

### 1.1 What is the disease?
**Aflatoxin-related HCC** is hepatocellular carcinoma arising (often on a background of chronic liver disease) in which chronic dietary exposure to aflatoxins—potent mycotoxins produced by *Aspergillus* spp.—is a causal contributor. In high-burden regions, aflatoxin exposure often co-occurs with chronic HBV infection and the combination is a major driver of HCC risk. (chen2026aflatoxinandliver pages 1-2, morenoleon2025cooperationbetweenaflatoxininduced pages 1-2, koshiol2026aflatoxinsandhuman pages 1-2)

### 1.2 Key identifiers (OMIM/Orphanet/ICD-10/ICD-11/MeSH/MONDO)
- **ICD-10/ICD-11, MeSH, MONDO:** Not present in the retrieved full-text excerpts, so cannot be asserted with citations here (limitation).
- **Operational identifiers used in the literature:** tumor fingerprint **TP53 R249S**, aflatoxin exposure biomarkers (urinary **AFB1–N7–guanine**, urinary **AFM1**, serum **AFB1–lysine albumin adducts**), and aflatoxin mutational signatures (“AFB1-type”). (chen2026aflatoxinandliver pages 1-2, chen2026aflatoxinandliver media 0564ad30, chen2026aflatoxinandliver pages 15-16)

### 1.3 Synonyms / alternative names
- “Aflatoxin-associated HCC”
- “AFB1-related HCC”
- “HCC with aflatoxin mutational signature / signature 24-like features”
- “HCC with TP53 R249S aflatoxin signature mutation” (chen2026aflatoxinandliver pages 1-2, morenoleon2025cooperationbetweenaflatoxininduced pages 1-2, gouas2009theaflatoxininducedtp53 pages 1-2)

### 1.4 Evidence type note
The aflatoxin–HCC knowledge base is derived from aggregated evidence: biomarker-enabled human epidemiology, molecular pathology of tumors/circulating DNA, and controlled animal models (rodent, duckling) demonstrating causality and providing mechanistic detail. (chen2026aflatoxinandliver pages 1-2, kensler202465yearson—aflatoxin pages 2-4)

---

## 2. Etiology

### 2.1 Disease causal factors (environmental, infectious, mechanistic)
- **Environmental/toxicant:** Dietary aflatoxins (especially **AFB1**) are described as “well-established” carcinogenic hazards for liver cancer. (koshiol2026aflatoxinsandhuman pages 1-2)
- **Infectious cofactor:** Chronic **HBV infection** is a dominant HCC cause globally and is repeatedly emphasized as synergizing with aflatoxin exposure where both are prevalent. (chen2026aflatoxinandliver pages 1-2, morenoleon2025cooperationbetweenaflatoxininduced pages 1-2)

### 2.2 Risk factors
#### Environmental
- Consumption of staples prone to contamination (e.g., maize, peanuts) in hot/humid climates with inadequate drying/storage is a key upstream determinant of chronic exposure. (chen2026aflatoxinandliver pages 1-2, koshiol2026aflatoxinsandhuman pages 14-15)

#### Infectious
- **HBV positivity** is a key effect modifier: aflatoxin exposure and HBsAg positivity can interact multiplicatively, producing much higher HCC risk than either factor alone. For example, a nested case–control analysis cited in a 2026 review reported very high joint-effect estimates (RR 59.4, 95% CI 16.6–212.0) for combined HBV and aflatoxin exposure (biomarker-defined). (koshiol2026aflatoxinsandhuman pages 9-11)

#### Viral genetic variation interacting with aflatoxin exposure
A Guangxi (China) case–control study (60 HCC cases, 120 matched controls) measured serum AFB1–lysine adducts and found that HBV basal core promoter mutations increased risk and that joint exposure to HBV mutations and **high AFB1–lysine adducts** further increased HCC risk (e.g., OR 6.94 for 1762T/1764A plus high AFB1–lysine). (xu2010geneticvariationsof pages 1-2)

### 2.3 Protective factors
In the retrieved corpus, protective factors are primarily **exposure reduction** and **HBV control**. Chemopreventive/dietary interception strategies that enhance detoxication pathways reduce biomarker burdens in exposed populations (examples in China include **oltipraz**, **chlorophyllin**, and **broccoli sprout beverages**). (chen2026aflatoxinandliver pages 1-2, chen2026aflatoxinandliver pages 2-4)

### 2.4 Gene–environment interactions
The core GxE interaction is between the **aflatoxin mutagenic mechanism** and host context shaped by **HBV infection**, which functionally perturbs p53 signaling via HBV X protein (HBx), amplifying the consequences of aflatoxin-induced TP53 mutations. (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2)

---

## 3. Phenotypes

### 3.1 Clinical phenotypes linked directly to aflatoxin exposure
A recent review describing aflatoxin health effects notes acute aflatoxicosis symptoms including **“jaundice, fever, ascites, pedal edema, and vomiting.”** (direct abstract text) (koshiol2026aflatoxinsandhuman pages 9-11)

### 3.2 Tumor/pathology-associated features linked to aflatoxin-related HCC
- Aflatoxin-associated tumors are characterized by the **TP53 R249S** hotspot mutation (often detectable in tumor DNA and sometimes circulating DNA). (chen2026aflatoxinandliver pages 1-2, gouas2009theaflatoxininducedtp53 pages 1-2)
- Dual-exposure HBV(+)/AFB1(+) tumors are described as molecularly distinct with features including higher PD-L1 expression and microvessel density (review-level evidence). (chen2026aflatoxinandliver pages 15-16)

### 3.3 General HCC clinical, laboratory, imaging phenotypes
Not extractable from the retrieved evidence set (limitation). The current corpus is dominated by exposure biology, molecular fingerprinting, and prevention rather than clinical presentation/imaging guidance.

### 3.4 Suggested ontology terms
Given limited clinical-phenotype detail in retrieved sources, suggestions are necessarily high-level:
- **HPO (tumor/disease):** Hepatocellular carcinoma (HP term exists but not cited from retrieved sources), Ascites, Jaundice (supported as aflatoxicosis manifestations in a review). (koshiol2026aflatoxinsandhuman pages 9-11)
- **LOINC/SNOMED:** Not directly supported by retrieved sources.

---

## 4. Genetic / molecular information

### 4.1 Core causal molecular mechanism (current consensus)
AFB1 is bioactivated in liver by cytochrome P450 enzymes to **AFB1-8,9-exo-epoxide**, which forms **AFB1–N7-guanine** and **FAPY** adducts. If unrepaired, these lesions yield characteristic **G→T transversions**, particularly at **TP53 codon 249**, generating **R249S (AGG→AGT)**—widely considered a molecular fingerprint of aflatoxin exposure in HCC. (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2, morenoleon2025cooperationbetweenaflatoxininduced pages 2-4, gouas2009theaflatoxininducedtp53 pages 1-2)

### 4.2 Key genes and variants
- **TP53 (tumor suppressor):** somatic hotspot **R249S** (Arg→Ser) is repeatedly emphasized as aflatoxin-linked and prevalent in high-exposure regions. (chen2026aflatoxinandliver pages 1-2, gouas2009theaflatoxininducedtp53 pages 1-2)
- **HBV X (HBx):** functional inactivation of p53 described as a synergy mechanism with aflatoxin-induced TP53 damage. (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2)

### 4.3 Circulating tumor DNA / early detection signal
Circulating cell-free DNA carrying TP53 R249S can be quantified in plasma and shows patterns consistent with exposure and disease state:
- In Thailand, plasma R249S-mutated DNA was detectable at low concentrations (≥67 copies/mL) in 53–64% of patients with primary liver cancer or chronic liver disease and 19% of controls; at ≥150 copies/mL it was more frequent in HCC without cirrhosis than with cirrhosis (44% vs 21%). (villar2012aflatoxininducedtp53r249s pages 1-2)
- In a Qidong HBV-carrier cohort study, tumor R249S frequency was 61% (11/18 tumors); aflatoxin–albumin adduct positivity was 67% (168/249), and the authors discuss assay sensitivity differences for detecting low levels of circulating mutant DNA. (szymanska2009tp53r249smutations pages 1-2, szymanska2009tp53r249smutations pages 4-5)

### 4.4 Epigenetic and pathway context
Recent reviews summarize additional mechanisms beyond direct mutagenesis, including oxidative stress, mitochondrial dysfunction, immune effects, and epigenetic changes contributing to carcinogenesis. (koshiol2026aflatoxinsandhuman pages 1-2)

### 4.5 Suggested ontology term mappings
- **CHEBI:** Aflatoxin B1 (chemical entity; not directly cited as CHEBI ID in retrieved text)
- **GO (biological process):** xenobiotic metabolic process; DNA adduct formation; DNA repair; cell cycle regulation; p53-mediated signal transduction (mechanistically implied by AFB1 adducts and p53 disruption). (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2, chen2026aflatoxinandliver pages 15-16)
- **CL (cell types):** hepatocyte; liver sinusoidal endothelial cell (angiogenesis context); immune cells (inflammation/immune effects described broadly). (koshiol2026aflatoxinsandhuman pages 1-2, chen2026aflatoxinandliver pages 15-16)

---

## 5. Environmental information

### 5.1 Environmental factors
- **Source and route:** Aflatoxins are food-borne mycotoxins produced by *Aspergillus* species contaminating staples; exposure is chronic in many tropical/subtropical settings. (koshiol2026aflatoxinsandhuman pages 1-2)
- **Climate sensitivity:** Reviews highlight that climate conditions influence contamination dynamics and may increase exposure volatility. (chen2026aflatoxinandliver pages 1-2, koshiol2026aflatoxinsandhuman pages 9-11)

### 5.2 Infectious agents
- **HBV** is a dominant cofactor and effect modifier; the joint presence of aflatoxin exposure and chronic HBV can produce supra-multiplicative HCC risk. (koshiol2026aflatoxinsandhuman pages 9-11, chen2026aflatoxinandliver pages 2-4)

---

## 6. Mechanism / pathophysiology (causal chain)

### 6.1 Causal chain (trigger → molecular lesion → clinical disease)
1. **Trigger:** chronic dietary exposure to AFB1 from contaminated staples. (chen2026aflatoxinandliver pages 1-2, koshiol2026aflatoxinsandhuman pages 1-2)
2. **Upstream molecular event:** hepatic CYP bioactivation to AFBO (reactive epoxide). (koshiol2026aflatoxinsandhuman pages 14-15)
3. **Biologically effective dose:** formation of DNA adducts (AFB1–N7-Gua; FAPY). (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2)
4. **Mutation formation:** G→T transversions, with characteristic **TP53 R249S** hotspot. (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2, gouas2009theaflatoxininducedtp53 pages 1-2)
5. **Effect modification by infection:** HBV (HBx) disrupts p53 function, amplifying tumorigenic consequences; population studies show strong multiplicative interactions. (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2, koshiol2026aflatoxinsandhuman pages 9-11)
6. **Tumor emergence:** HCC with aflatoxin-associated mutational signature and pathway activation patterns (e.g., Wnt/angiogenesis/cell-cycle proteins in dual-exposure tumors). (chen2026aflatoxinandliver pages 15-16)

### 6.2 Biomarkers along the chain
Validated biomarkers for exposure and early detection include urinary **AFB1–N7–guanine**, urinary **AFM1**, serum **AFB1–lysine albumin adducts**, and circulating TP53 **R249S** mutant DNA. (chen2026aflatoxinandliver media 0564ad30, chen2026aflatoxinandliver pages 15-16)

---

## 7. Anatomical structures affected
- **Primary organ:** liver (hepatocytes as primary target for bioactivation and DNA adduct formation). (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2)
- **Suggested UBERON term:** liver (not provided explicitly in sources).

---

## 8. Temporal development
- **Latency:** Aflatoxin-related carcinogenesis is consistent with long latency; biomarker and mutational-signature work aims to detect “incipient carcinogenesis” before overt tumors in model systems. (kensler202465yearson—aflatoxin pages 2-4)
- **Critical periods:** Not explicitly quantified in retrieved sources.

---

## 9. Inheritance and population

### 9.1 Epidemiology and attributable risk
A systematic review and meta-analysis estimated the **population attributable risk (PAR)** of aflatoxin-related HCC at **17% (14–19%) overall**, higher in HBV-positive populations (**21%**) than HBV-negative (**8.8%**). (liu2012populationattributablerisk pages 1-3)

### 9.2 Geographic distribution
Reviews highlight wide regional variation: aflatoxin–albumin/lysine adduct prevalence ranges from 0% in some European studies to up to 100% in parts of Africa and Asia. (koshiol2026aflatoxinsandhuman pages 1-2)

---

## 10. Diagnostics

### 10.1 Exposure and biologically effective dose biomarkers (real-world use)
- **Urinary AFB1–N7–guanine** and **AFM1** are emphasized as validated biomarkers in field studies and surveillance frameworks. (chen2026aflatoxinandliver pages 1-2, chen2026aflatoxinandliver media 0564ad30)
- **Serum AFB1–lysine albumin adducts** are described as reliable long-term exposure biomarkers and used in risk stratification in endemic regions. (xu2010geneticvariationsof pages 1-2)

### 10.2 Tumor/circulating molecular biomarkers
- **TP53 R249S in tumor DNA** and **circulating R249S-mutated DNA** in plasma/serum as a molecular fingerprint/early-detection signal. (villar2012aflatoxininducedtp53r249s pages 1-2, gouas2009theaflatoxininducedtp53 pages 1-2)

### 10.3 Imaging/pathology diagnostics for HCC
Not available in the retrieved evidence set (limitation).

---

## 11. Outcome / prognosis
Aflatoxin-specific survival statistics were not found in the retrieved full text. One 2026 review notes that dual-exposure tumors can have distinct immune microenvironment markers (e.g., PD-L1, microvessel density), which may plausibly influence outcomes and therapy response, but outcome quantification was not provided in the retrieved excerpts. (chen2026aflatoxinandliver pages 15-16)

---

## 12. Treatment

### 12.1 Treatment of established HCC
Not extractable from retrieved sources (limitation). The retrieved corpus is prevention/biomarker-centric rather than guideline-centric for established HCC.

### 12.2 Chemoprevention / interception strategies (human implementation evidence)
China-focused reviews describe chemoprevention/dietary interception trials using **oltipraz**, **chlorophyllin**, and **broccoli sprout beverages**, with reductions in aflatoxin biomarker burdens, supporting feasibility of biochemical risk reduction. (chen2026aflatoxinandliver pages 1-2, chen2026aflatoxinandliver pages 2-4)

### 12.3 MAXO term suggestions (treatment/prevention actions)
(ontology IDs not provided in sources; suggestions are conceptual)
- HBV vaccination / antiviral management (risk elimination)
- Food decontamination / exposure reduction
- Chemopreventive administration (e.g., oltipraz; chlorophyllin; dietary sulforaphane sources)

### 12.4 Clinical trials (aflatoxin-focused)
A clinical trial record was retrieved titled **“Evaluation of the Role of Aflatoxin as an Environmental Risk Factor Attributable to Liver Cancer in Nile Delta” (NCT02461966)**; the retrieved trial metadata does not provide analyzable results here. (chen2026aflatoxinandliver pages 1-2)

---

## 13. Prevention (real-world implementations)

### 13.1 Multi-level prevention strategy (One Health / value chain)
A recent One Health-focused review emphasizes intervention “beginning at the farm level and continuing through pre-harvest, post-harvest, storage, and the consumer level,” and highlights developing technologies such as electrochemical biosensors and AI methods for detection/decontamination. (koshiol2026aflatoxinsandhuman pages 1-2)

### 13.2 Practical mitigation actions (examples cited in recent reviews)
Interventions described include:
- **Biocontrol:** atoxigenic *Aspergillus* strains.
- **Pre-harvest:** seed/soil management, irrigation, pest control.
- **Post-harvest:** rapid drying, sorting, hermetic storage, moisture control. (koshiol2026aflatoxinsandhuman pages 14-15)

### 13.3 China “5+1” prevention framework and policy-level natural experiment
A China-focused synthesis proposes an integrated “**5+1**” framework (source control; process detoxification; tiered governance; short-course interception; precision follow-up, plus climate-sensitive early warning). This is described visually (table/figure) in the retrieved document. (chen2026aflatoxinandliver media 86dda2b5, chen2026aflatoxinandliver media 6173650a)

In Qidong, a long-term “natural experiment” (dietary shift from maize to rice plus strengthened food governance) was associated with large reductions in internal exposure biomarkers and a sustained decline in HCC burden in that endemic region (review synthesis). (chen2026aflatoxinandliver pages 2-4)

---

## 14. Other species / natural disease
Not directly addressed in the retrieved evidence, except that aflatoxin is emphasized as a potent carcinogen across species and is discussed in the context of animal susceptibility (e.g., ducks). (kensler202465yearson—aflatoxin pages 2-4)

---

## 15. Model organisms / experimental systems

### 15.1 Rodent dietary carcinogenesis models (quantitative)
A 2024 review summarizes classic animal data demonstrating extreme potency of AFB1 as a hepatocarcinogen in rats, including reports that **15 ppb** AFB1 in diet produced **100% hepatocellular carcinomas** in Fischer rats under specific experimental conditions, and provides TD50 comparisons across carcinogens. (kensler202465yearson—aflatoxin pages 2-4)

### 15.2 Model systems referenced in recent synthesis
A China-focused review describes model systems including rats (with RNA-seq showing perturbation of xenobiotic metabolism/redox and transcript processing) and ducklings showing dose–response changes in phase I/II metabolism and cell-cycle/apoptosis prior to tumor development. (chen2026aflatoxinandliver pages 15-16)

---

## Recent developments and latest research (prioritizing 2023–2024 where available)

### 2024: Biomarker paradigm emphasis and modern measurement approaches
A 2024 review (“65 Years on—Aflatoxin Biomarkers Blossoming”) emphasizes continued innovation in aflatoxin biomarkers and provides quantitative context for exposure-to-dose translation and risk framing, underscoring biomarkers as central tools to probe exposure–disease relationships. (kensler202465yearson—aflatoxin pages 2-4)

### 2026: Integrated prevention framework and “AFB1-type” molecular subtype framing
A 2026 synthesis of China’s evidence base highlights biomarker-enabled surveillance, TP53 R249S and mutational signatures, and a structured “5+1” prevention framework suitable for implementation and evaluation. It also notes that ~10% of Chinese HCCs may be classifiable as “AFB1-type” by mutational signatures. (chen2026aflatoxinandliver pages 15-16, chen2026aflatoxinandliver media 6173650a)

---

## Expert opinions / authoritative analysis (from retrieved sources)
- Reviews characterize aflatoxin B1 as a uniquely potent genotoxic carcinogen and frame aflatoxin biomarker science as a template (“paradigm”) for linking exposures to cancer risk in populations. (kensler202465yearson—aflatoxin pages 2-4)
- One Health analyses emphasize integrated, cross-sector approaches (agriculture → storage → consumer; health systems biomonitoring) as essential for reducing current and future aflatoxin-related disease burden. (koshiol2026aflatoxinsandhuman pages 1-2)

---

## Key limitations of this report (evidence availability)
- **PMIDs were not available in the retrieved full-text snippets** for most sources; therefore, this report cites DOIs/URLs and publication months/years instead. (liu2012populationattributablerisk pages 1-3, koshiol2026aflatoxinsandhuman pages 1-2, xu2010geneticvariationsof pages 1-2)
- **ICD-10/ICD-11/MeSH/MONDO identifiers** were not retrievable from the available evidence set.
- Detailed **clinical presentation, imaging criteria, standard-of-care therapies, and prognosis** specific to aflatoxin-related HCC were not covered in the retrieved excerpts and should be supplemented using clinical guidelines (e.g., NCCN/EASL/AASLD) and cancer registry data.


References

1. (chen2026aflatoxinandliver pages 1-2): Jian-Guo Chen, Thomas W. Kensler, Gui-Ju Sun, Jian Zhu, Jian-Hua Lu, Da Pan, Yong-Hui Zhang, and John D. Groopman. Aflatoxin and liver cancer in china: the evolving research landscape. Toxins, 18:61, Jan 2026. URL: https://doi.org/10.3390/toxins18020061, doi:10.3390/toxins18020061. This article has 0 citations.

2. (morenoleon2025cooperationbetweenaflatoxininduced pages 1-2): Carolina Moreno-León and Francisco Aguayo. Cooperation between aflatoxin-induced p53 aberrations and hepatitis b virus in hepatocellular carcinoma. Journal of Xenobiotics, 15:96, Jun 2025. URL: https://doi.org/10.3390/jox15040096, doi:10.3390/jox15040096. This article has 8 citations.

3. (koshiol2026aflatoxinsandhuman pages 1-2): Jill Koshiol, Amit Yadav, John D. Groopman, and Usha Dutta. Aflatoxins and human health: global exposure, disease burden, and one health strategies. Toxins, 18:90, Feb 2026. URL: https://doi.org/10.3390/toxins18020090, doi:10.3390/toxins18020090. This article has 0 citations.

4. (gouas2009theaflatoxininducedtp53 pages 1-2): Doriane Gouas, Hong Shi, and Pierre Hainaut. The aflatoxin-induced tp53 mutation at codon 249 (r249s): biomarker of exposure, early detection and target for therapy. Cancer letters, 286 1:29-37, Dec 2009. URL: https://doi.org/10.1016/j.canlet.2009.02.057, doi:10.1016/j.canlet.2009.02.057. This article has 203 citations and is from a peer-reviewed journal.

5. (morenoleon2025cooperationbetweenaflatoxininduced pages 2-4): Carolina Moreno-León and Francisco Aguayo. Cooperation between aflatoxin-induced p53 aberrations and hepatitis b virus in hepatocellular carcinoma. Journal of Xenobiotics, 15:96, Jun 2025. URL: https://doi.org/10.3390/jox15040096, doi:10.3390/jox15040096. This article has 8 citations.

6. (szymanska2009tp53r249smutations pages 1-2): Katarzyna Szymañska, Jian-Guo Chen, Yan Cui, Yun Yun Gong, Paul Craig Turner, Stéphanie Villar, Christopher Paul Wild, Donald Maxwell Parkin, and Pierre Hainaut. Tp53 r249s mutations, exposure to aflatoxin, and occurrence of hepatocellular carcinoma in a cohort of chronic hepatitis b virus carriers from qidong, china. Cancer Epidemiology Biomarkers & Prevention, 18:1638-1643, May 2009. URL: https://doi.org/10.1158/1055-9965.epi-08-1102, doi:10.1158/1055-9965.epi-08-1102. This article has 72 citations and is from a domain leading peer-reviewed journal.

7. (szymanska2009tp53r249smutations pages 4-5): Katarzyna Szymañska, Jian-Guo Chen, Yan Cui, Yun Yun Gong, Paul Craig Turner, Stéphanie Villar, Christopher Paul Wild, Donald Maxwell Parkin, and Pierre Hainaut. Tp53 r249s mutations, exposure to aflatoxin, and occurrence of hepatocellular carcinoma in a cohort of chronic hepatitis b virus carriers from qidong, china. Cancer Epidemiology Biomarkers & Prevention, 18:1638-1643, May 2009. URL: https://doi.org/10.1158/1055-9965.epi-08-1102, doi:10.1158/1055-9965.epi-08-1102. This article has 72 citations and is from a domain leading peer-reviewed journal.

8. (chen2026aflatoxinandliver pages 2-4): Jian-Guo Chen, Thomas W. Kensler, Gui-Ju Sun, Jian Zhu, Jian-Hua Lu, Da Pan, Yong-Hui Zhang, and John D. Groopman. Aflatoxin and liver cancer in china: the evolving research landscape. Toxins, 18:61, Jan 2026. URL: https://doi.org/10.3390/toxins18020061, doi:10.3390/toxins18020061. This article has 0 citations.

9. (chen2026aflatoxinandliver media 0564ad30): Jian-Guo Chen, Thomas W. Kensler, Gui-Ju Sun, Jian Zhu, Jian-Hua Lu, Da Pan, Yong-Hui Zhang, and John D. Groopman. Aflatoxin and liver cancer in china: the evolving research landscape. Toxins, 18:61, Jan 2026. URL: https://doi.org/10.3390/toxins18020061, doi:10.3390/toxins18020061. This article has 0 citations.

10. (xu2010geneticvariationsof pages 1-2): Li Xu, Guoqing Qian, Lili Tang, Jianjia Su, and Jia-Sheng Wang. Genetic variations of hepatitis b virus and serum aflatoxin-lysine adduct on high risk of hepatocellular carcinoma in southern guangxi, china. Journal of hepatology, 53 4:671-6, Oct 2010. URL: https://doi.org/10.1016/j.jhep.2010.04.032, doi:10.1016/j.jhep.2010.04.032. This article has 47 citations and is from a highest quality peer-reviewed journal.

11. (lleonart2005quantitativeanalysisof pages 1-2): Matilde E. Lleonart, Gregory D. Kirk, Stephanie Villar, Olufunmilayo A. Lesi, Abhijit Dasgupta, James J. Goedert, Maimuna Mendy, Monica C. Hollstein, Ruggero Montesano, John D. Groopman, Pierre Hainaut, and Marlin D. Friesen. Quantitative analysis of plasma tp53 249ser-mutated dna by electrospray ionization mass spectrometry. Cancer Epidemiology, Biomarkers &amp; Prevention, 14:2956-2962, Dec 2005. URL: https://doi.org/10.1158/1055-9965.epi-05-0612, doi:10.1158/1055-9965.epi-05-0612. This article has 41 citations.

12. (villar2012aflatoxininducedtp53r249s pages 1-2): Stephanie Villar, Sandra Ortiz-Cuaran, Behnoush Abedi-Ardekani, Doriane Gouas, Andre Nogueira da Costa, Amelie Plymoth, Thiravud Khuhaprema, Anant Kalalak, Suleeporn Sangrajrang, Marlin D. Friesen, John D. Groopman, and Pierre Hainaut. Aflatoxin-induced tp53 r249s mutation in hepatocellular carcinoma in thailand: association with tumors developing in the absence of liver cirrhosis. PLoS ONE, 7:e37707, Jun 2012. URL: https://doi.org/10.1371/journal.pone.0037707, doi:10.1371/journal.pone.0037707. This article has 70 citations and is from a peer-reviewed journal.

13. (liu2012populationattributablerisk pages 1-3): Yan Liu, Chung-Chou H. Chang, Gary M. Marsh, and Felicia Wu. Population attributable risk of aflatoxin-related liver cancer: systematic review and meta-analysis. European journal of cancer, 48 14:2125-36, Sep 2012. URL: https://doi.org/10.1016/j.ejca.2012.02.009, doi:10.1016/j.ejca.2012.02.009. This article has 474 citations and is from a domain leading peer-reviewed journal.

14. (chen2026aflatoxinandliver pages 15-16): Jian-Guo Chen, Thomas W. Kensler, Gui-Ju Sun, Jian Zhu, Jian-Hua Lu, Da Pan, Yong-Hui Zhang, and John D. Groopman. Aflatoxin and liver cancer in china: the evolving research landscape. Toxins, 18:61, Jan 2026. URL: https://doi.org/10.3390/toxins18020061, doi:10.3390/toxins18020061. This article has 0 citations.

15. (kensler202465yearson—aflatoxin pages 2-4): Thomas W. Kensler and David L. Eaton. 65 years on—aflatoxin biomarkers blossoming: whither next? Toxins, 16:496, Nov 2024. URL: https://doi.org/10.3390/toxins16110496, doi:10.3390/toxins16110496. This article has 17 citations.

16. (koshiol2026aflatoxinsandhuman pages 14-15): Jill Koshiol, Amit Yadav, John D. Groopman, and Usha Dutta. Aflatoxins and human health: global exposure, disease burden, and one health strategies. Toxins, 18:90, Feb 2026. URL: https://doi.org/10.3390/toxins18020090, doi:10.3390/toxins18020090. This article has 0 citations.

17. (koshiol2026aflatoxinsandhuman pages 9-11): Jill Koshiol, Amit Yadav, John D. Groopman, and Usha Dutta. Aflatoxins and human health: global exposure, disease burden, and one health strategies. Toxins, 18:90, Feb 2026. URL: https://doi.org/10.3390/toxins18020090, doi:10.3390/toxins18020090. This article has 0 citations.

18. (chen2026aflatoxinandliver media 86dda2b5): Jian-Guo Chen, Thomas W. Kensler, Gui-Ju Sun, Jian Zhu, Jian-Hua Lu, Da Pan, Yong-Hui Zhang, and John D. Groopman. Aflatoxin and liver cancer in china: the evolving research landscape. Toxins, 18:61, Jan 2026. URL: https://doi.org/10.3390/toxins18020061, doi:10.3390/toxins18020061. This article has 0 citations.

19. (chen2026aflatoxinandliver media 6173650a): Jian-Guo Chen, Thomas W. Kensler, Gui-Ju Sun, Jian Zhu, Jian-Hua Lu, Da Pan, Yong-Hui Zhang, and John D. Groopman. Aflatoxin and liver cancer in china: the evolving research landscape. Toxins, 18:61, Jan 2026. URL: https://doi.org/10.3390/toxins18020061, doi:10.3390/toxins18020061. This article has 0 citations.

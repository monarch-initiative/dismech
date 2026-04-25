---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T13:47:10.200378'
end_time: '2026-04-05T14:01:25.652232'
duration_seconds: 855.45
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Basal Cell Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 59
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Basal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Basal Cell Carcinoma** covering all of the
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
- **Disease Name:** Basal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Basal Cell Carcinoma** covering all of the
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


# Basal Cell Carcinoma (BCC) — Disease Characteristics Research Report (2023–2024 prioritized)

## Target Disease
- **Disease Name:** Basal Cell Carcinoma (Basal cell skin cancer)
- **MONDO ID:** Not available in retrieved sources (not found in the provided full texts).
- **Category:** Cutaneous epithelial (keratinocyte) malignancy / non-melanoma skin cancer (keratinocyte carcinoma).

## Executive overview
Basal cell carcinoma (BCC) is the most common skin cancer and typically behaves as an indolent, locally invasive tumor with very low metastatic potential; therefore, morbidity is driven mainly by local tissue destruction, disfigurement, and functional impairment rather than distant spread. (schmults2023basalcellskin pages 2-4, lang2024s2kguidelinebasal pages 1-2)

---

## 1. Disease Information

### 1.1 Definition and current understanding
BCC is described in recent guidelines and reviews as a slow-growing, locally aggressive cutaneous neoplasm arising from the basal layer of the epidermis, with rare metastasis. (lang2024s2kguidelinebasal pages 1-2, schmults2023basalcellskin pages 2-4, sol2024therapeuticapproachesfor pages 7-8)

### 1.2 Key identifiers and classifications
Because many registries do not systematically record BCC, identifiers are often used indirectly in observational and genetic studies.

- **ICD-10 (commonly used for EHR/claims phenotyping):** A large 2024 GWAS meta-analysis defined BCC cases in one cohort using **ICD-10 codes C44.01–C44.91**. (choquet2024multiancestrygenomewidemetaanalysis pages 7-7)
- **ICD-O-3 topography (registry-based definition):** Japan’s National Cancer Registry analysis defined skin cancers using **ICD-O-3 topography codes** including **C44 (skin)** (and additional genital skin topographies), with in situ lesions included. (ogata2023epidemiologyofskin pages 1-2)
- **MeSH / MONDO / ICD-11:** Not extractable from the retrieved full-text evidence in this run; therefore not asserted here.

### 1.3 Common synonyms / alternative names
- Basal cell carcinoma of the skin
- Basal cell skin cancer (NCCN nomenclature) (schmults2023basalcellskin pages 2-4)
- Keratinocyte cancer / keratinocyte carcinoma (umbrella term often including BCC and cSCC) (vallini2023signalingpathwaysand pages 1-2, yang2023trendsinkeratinocyte pages 1-8)

### 1.4 Evidence sources (patient-level vs aggregated)
- **Aggregated resources/guidelines:** NCCN Clinical Practice Guideline (Version 2.2024; published 2023) and German S2k guideline update 2023 (published 2024). (schmults2023basalcellskin pages 2-4, lang2024s2kguidelinebasal pages 1-2)
- **Population-level registry data:** Japan National Cancer Registry 2016–2017. (ogata2023epidemiologyofskin pages 1-2)
- **Patient-level cohorts:** Prospective recurrence cohort (treated tumors followed for recurrence). (chren2013tumorrecurrence5 pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Ultraviolet (UV) radiation** is consistently highlighted as a principal causal factor, with additional contributions from ionizing radiation and genetic predisposition. (schmults2023basalcellskin pages 2-4, lang2024s2kguidelinebasal pages 1-2, vallini2023signalingpathwaysand pages 2-3)

### 2.2 Risk factors
- **UV exposure** (including indoor tanning) and **ionizing radiation** (including prior radiotherapy) are key environmental risk factors. (schmults2023basalcellskin pages 2-4, vallini2023signalingpathwaysand pages 2-3)
- **Phenotype and demographics:** fair skin, red/blond hair, light eye color; older age; male sex. (schmults2023basalcellskin pages 2-4, dessinioti2023immunotherapyandits pages 1-2)
- **Immunosuppression:** increased risk in solid-organ transplant recipients; one 2023 review reported BCC risk elevated **6- to 16-fold** vs the general population in transplant recipients in summarized literature. (vallini2023signalingpathwaysand pages 2-3)
- **Genetic predisposition / genodermatoses:** basal cell carcinoma syndrome (Gorlin/NBCCS), xeroderma pigmentosum (XP). (lang2024s2kguidelinebasal pages 1-2, schmults2023basalcellskin pages 2-4)
- **Arsenic exposure:** chronic arsenic exposure is listed as a risk factor in the German guideline and is also addressed in molecular profiling work in arsenic-exposed populations. (lang2024s2kguidelinebasal pages 1-2, alkassis2024therapeuticadvancesin pages 2-4)

### 2.3 Protective factors
- **Photoprotection/UV avoidance:** emphasized as the primary prevention strategy for non-melanoma skin cancers. (hyeraci2023systemicphotoprotectionin pages 1-2)
- **Systemic photoprotection agents:** A 2023 review states that among multiple oral photoprotective agents, only a few have demonstrated effectiveness in trials and have been incorporated into international guidance for NMSC prevention, including **nicotinamide** and **retinoids**. (hyeraci2023systemicphotoprotectionin pages 1-2)

### 2.4 Gene–environment interactions
The dominant conceptual interaction is UV-induced DNA damage superimposed on inherited or acquired susceptibility (e.g., pigmentary traits, DNA repair capacity, immune status), consistent with high UV-signature mutational patterns and known susceptibility loci; however, specific interaction effect sizes were not extractable from the retrieved texts. (vallini2023signalingpathwaysand pages 2-3, choquet2024multiancestrygenomewidemetaanalysis pages 7-7)

---

## 3. Phenotypes

### 3.1 Typical clinical phenotypes and presentation
BCC shows clinical heterogeneity; common subtypes include nodular and superficial BCC, with high-risk subtypes including morpheaform/sclerosing and infiltrative patterns. (alkassis2024therapeuticadvancesin pages 2-4, lang2024s2kguidelinebasal pages 1-2)

A structured phenotype/HPO mapping table is provided below.

| Clinical feature | Description | Suggested HPO term(s) | Notes/frequency (if in evidence) | Evidence source (author year) | URL |
|---|---|---|---|---|---|
| Nodular basal cell carcinoma | Classic pearly/translucent papule or nodule, often with surface telangiectasia; may ulcerate as it enlarges | HP:0009726 Skin nodule; HP:0000975 Hyperpigmentation of the skin (if pigmented); HP:0008066 Telangiectasia; HP:0000979 Skin ulcer | Low-risk subtype; reported as the commonest subtype, about 60-80% of BCCs; usually slow-growing and locally invasive rather than metastatic (alkassis2024therapeuticadvancesin pages 2-4, lang2024s2kguidelinebasal pages 1-2) | Alkassis 2024; Lang 2024 | https://doi.org/10.3390/cancers16173075 ; https://doi.org/10.1111/ddg.15566 |
| Superficial basal cell carcinoma | Thin erythematous or scaly patch/plaque, often on trunk; can mimic inflammatory dermatoses | HP:0000989 Pruritic rash; HP:0200034 Erythematous plaque; HP:0001075 Scaly skin | Low-risk subtype; about 20% in one recent review; commonly on trunk and other sun-exposed skin (alkassis2024therapeuticadvancesin pages 2-4, lang2024s2kguidelinebasal pages 1-2) | Alkassis 2024; Lang 2024 | https://doi.org/10.3390/cancers16173075 ; https://doi.org/10.1111/ddg.15566 |
| Pigmented basal cell carcinoma | Brown/black/blue pigmented lesion, sometimes clinically resembling melanoma | HP:0000953 Hypermelanotic macule; HP:0000975 Hyperpigmentation of the skin | Particularly relevant in East Asian populations; Japanese guideline notes 88.3% of BCCs in Japanese patients are pigmented (lang2024s2kguidelinebasal pages 1-2) | Lang 2024 | https://doi.org/10.1111/ddg.15566 |
| Morpheaform / sclerosing BCC | Scar-like, indurated, ill-defined plaque with infiltrative growth pattern | HP:0010783 Scar; HP:0002263 Facial asymmetry (if destructive facial growth); HP:0200034 Plaque | High-risk histologic subtype with greater subclinical extension and recurrence risk; often requires Mohs surgery or wider margin control (alkassis2024therapeuticadvancesin pages 2-4, schmults2023basalcellskin media 73ba3136) | Alkassis 2024; Schmults 2023 | https://doi.org/10.3390/cancers16173075 ; https://doi.org/10.6004/jnccn.2023.0056 |
| Infiltrative / micronodular / basosquamous high-risk BCC | More aggressive growth patterns with deeper tissue infiltration and less obvious borders | HP:0000951 Abnormality of the skin; HP:0008064 Neoplasm of the skin | Considered high-risk subtypes; associated with greater local recurrence risk and need for margin-controlled surgery (alkassis2024therapeuticadvancesin pages 2-4, schmults2023basalcellskin media 73ba3136) | Alkassis 2024; Schmults 2023 | https://doi.org/10.3390/cancers16173075 ; https://doi.org/10.6004/jnccn.2023.0056 |
| Nonhealing lesion | Persistent lesion that fails to resolve over time | HP:0033677 Nonhealing skin ulcer | Common presentation in review literature; clinical suspicion should prompt biopsy (lang2024s2kguidelinebasal pages 1-2) | Baba 2024 | https://doi.org/10.3390/jmp5020010 |
| Bleeding / friable lesion | Lesion may bleed intermittently, especially after minor trauma | HP:0025337 Cutaneous bleeding | Review notes BCC may present as a nonhealing lesion that occasionally bleeds (lang2024s2kguidelinebasal pages 1-2) | Baba 2024 | https://doi.org/10.3390/jmp5020010 |
| Pruritic lesion | Itching can occur, although many lesions are asymptomatic | HP:0000989 Pruritus | Review notes BCC may present as a pruritic lesion with otherwise few symptoms (lang2024s2kguidelinebasal pages 1-2) | Baba 2024 | https://doi.org/10.3390/jmp5020010 |
| Ulcerated lesion (“rodent ulcer”) | Central ulceration developing in a locally destructive lesion | HP:0000979 Skin ulcer | Ulceration is part of the classic clinical heterogeneity described in guidelines; can indicate larger or neglected tumor (lang2024s2kguidelinebasal pages 1-2) | Lang 2024 | https://doi.org/10.1111/ddg.15566 |
| Head and neck distribution | Predominant anatomic distribution on chronically sun-exposed skin, especially face/head/neck | HP:0000286 Epicanthus?; HP:0000154 Abnormality of the neck skin; HP:0011274 Abnormality of the skin of the face | Most BCCs arise on head/neck; S2k guideline states BCCs occur mostly on head/neck, trunk, extremities; review notes lesions usually occur above line joining tragus to angle of mouth (lang2024s2kguidelinebasal pages 1-2) | Lang 2024; Baba 2024 | https://doi.org/10.1111/ddg.15566 ; https://doi.org/10.3390/jmp5020010 |
| Truncal distribution | Especially common for superficial BCC | HP:0011122 Abnormality of skin of trunk | Face, neck, and trunk are common sites in recent review (sol2024therapeuticapproachesfor pages 7-8) | Sol 2024 | https://doi.org/10.3390/ijms25137056 |
| Adult / older-adult onset | Usually presents later in life rather than childhood, except in hereditary syndromes | HP:0003581 Adult onset; HP:0003596 Middle age onset; HP:0003584 Late onset | Mean age of onset in German guideline ~73 years in men and 71 years in women (lang2024s2kguidelinebasal pages 1-2) | Lang 2024 | https://doi.org/10.1111/ddg.15566 |
| Locally aggressive growth | Slow-growing but capable of substantial local invasion, tissue destruction, disfigurement, and functional impairment | HP:0000951 Abnormality of the skin; HP:0012252 Abnormality of facial soft tissue | NCCN: less aggressive than melanoma/SCC but local destruction can cause disfigurement and limitation of function; advanced lesions behave aggressively (schmults2023basalcellskin pages 2-4, alkassis2024therapeuticadvancesin pages 1-2) | Schmults 2023; Alkassis 2024 | https://doi.org/10.6004/jnccn.2023.0056 ; https://doi.org/10.3390/cancers16173075 |
| Very low metastatic potential | Metastatic spread is exceptional compared with other skin cancers | HP:0003002 Neoplasm of the skin?; HP:0002664 Neoplasm metastasis | Metastasis estimated at <0.1% in NCCN and 0.0028%-0.55% in guideline/review estimates (schmults2023basalcellskin pages 2-4, lang2024s2kguidelinebasal pages 1-2, sol2024therapeuticapproachesfor pages 7-8) | Schmults 2023; Lang 2024; Sol 2024 | https://doi.org/10.6004/jnccn.2023.0056 ; https://doi.org/10.1111/ddg.15566 ; https://doi.org/10.3390/ijms25137056 |
| Diagnostic confirmation by biopsy | Histopathology is required to confirm diagnosis and subtype; deep reticular dermis sampling preferred when possible | HP:0034335 Abnormal skin morphology | NCCN recommends biopsy including deep reticular dermis; Baba review states all suspicious lesions should be biopsied (schmults2023basalcellskin pages 2-4, lang2024s2kguidelinebasal pages 1-2) | Schmults 2023; Baba 2024 | https://doi.org/10.6004/jnccn.2023.0056 ; https://doi.org/10.3390/jmp5020010 |
| Diagnostic total-body skin examination | Full skin exam at diagnosis to detect additional keratinocyte cancers or melanoma | HP:0000951 Abnormality of the skin | NCCN states patients are at increased risk for additional lesions and cutaneous melanoma; total-body skin exam recommended (schmults2023basalcellskin pages 2-4) | Schmults 2023 | https://doi.org/10.6004/jnccn.2023.0056 |
| Imaging for suspected deep extension | MRI preferred for perineural disease; CT preferred for possible bone involvement | HP:0012790 Perineural invasion; HP:0000938 Osteolysis | Imaging not routine for all BCC; used when clinical exam is insufficient or advanced extension suspected (schmults2023basalcellskin pages 2-4, schmults2023basalcellskin media 73ba3136) | Schmults 2023 | https://doi.org/10.6004/jnccn.2023.0056 |


*Table: This table summarizes common clinical presentations and diagnostic features of basal cell carcinoma, with best-effort HPO mappings and key notes on distribution, aggressiveness, and metastatic rarity. It is useful for phenotype annotation and disease knowledge-base curation.*

### 3.2 Age of onset, severity, progression
- **Age of onset:** German S2k guideline reports mean age of onset ~**73 years (men)** and **71 years (women)**. (lang2024s2kguidelinebasal pages 1-2)
- **Course:** typically slow-growing and locally invasive; metastasis is rare. (schmults2023basalcellskin pages 2-4, lang2024s2kguidelinebasal pages 1-2)

### 3.3 Quality-of-life impact
Guidelines emphasize that because local therapies (surgery and/or radiotherapy) are common, **disfigurement and limitation of function** are central morbidity concerns. (schmults2023basalcellskin pages 2-4)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes and key molecular drivers (current consensus)
BCC pathogenesis is strongly linked to **Hedgehog (HH) pathway activation**, typically via inactivation of pathway repressors (e.g., PTCH1) or activating alterations in SMO, resulting in downstream activation of GLI transcription factors. (lang2024s2kguidelinebasal pages 1-2, vallini2023signalingpathwaysand pages 2-3, alkassis2024therapeuticadvancesin pages 2-4)

A structured gene/pathway summary is provided below.

| Mechanism/Pathway | Key genes/proteins | Typical alteration (somatic vs germline) | Approx frequency/range in BCC (as stated) | Notes (UV signature, resistance) | Evidence source (author year) | URL |
|---|---|---|---|---|---|---|
| Hedgehog pathway activation | **PTCH1**, **SMO**, **SUFU**, GLI1/2/3 | Mostly somatic in sporadic BCC; germline **PTCH1** in Gorlin syndrome/NBCCS | ~85% of sporadic BCCs carry Hedgehog-pathway mutations; **PTCH** LOF ~73%, **SMO** GOF ~20%, **SUFU** LOF ~8% (vallini2023signalingpathwaysand pages 2-3) | Central driver pathway; basis for SMO-targeted therapy; resistance/toxicity limits long-term HHI use (vallini2023signalingpathwaysand pages 2-3, vallini2023signalingpathwaysand pages 1-2) | Vallini 2023 | https://doi.org/10.3390/cells12212534 |
| Hedgehog pathway activation | **PTCH1**, **SMO** | Somatic in sporadic BCC; germline predisposition in syndromic disease | **PTCH1** mutations ~30%–90% of sporadic BCCs; **SMO** activating mutations ~10% of sporadic BCCs (schmults2023basalcellskin pages 2-4, lang2024s2kguidelinebasal pages 1-2) | NCCN and S2k both identify sonic hedgehog signaling as pivotal in BCC pathogenesis (schmults2023basalcellskin pages 2-4, lang2024s2kguidelinebasal pages 1-2) | Schmults 2023; Lang 2024 | https://doi.org/10.6004/jnccn.2023.0056; https://doi.org/10.1111/ddg.15566 |
| Hedgehog pathway dysregulation in advanced BCC | **PTCH1**, **SMO**, GLI TFs | Somatic | **PTCH1** LOF up to 75%; **SMO** activating mutations 10%–20% (alkassis2024therapeuticadvancesin pages 2-4) | Advanced disease remains Hh-driven; HH inhibitors are effective but resistance emerges clinically (alkassis2024therapeuticadvancesin pages 2-4, alkassis2024therapeuticadvancesin pages 1-2) | Alkassis 2024 | https://doi.org/10.3390/cancers16173075 |
| UV-induced DNA damage / tumor suppressor disruption | **TP53**, **PTCH1** | Somatic | **TP53** altered in 61% in one study summarized by S2k; UV-signature mutations common in **p53** and **PTCH** (lang2024s2kguidelinebasal pages 1-2, vallini2023signalingpathwaysand pages 2-3) | Canonical C>T / CC>TT UV-signature mutagenesis; UVB is the dominant environmental trigger (vallini2023signalingpathwaysand pages 2-3, schmults2023basalcellskin pages 2-4) | Lang 2024; Vallini 2023 | https://doi.org/10.1111/ddg.15566; https://doi.org/10.3390/cells12212534 |
| High tumor mutational burden / immunogenicity | PD-L1, MHC-I, neoantigen burden | Somatic tumor feature | TMB reported as **47.3 mutations/Mb**; PD-L1 expression in one study: **22%** of tumor cells and **82%** of tumor-infiltrating immune cells (vallini2023signalingpathwaysand pages 2-3, dessinioti2023immunotherapyandits pages 1-2) | Provides rationale for PD-1 blockade after HHI failure; predictive biomarkers remain unsettled (dessinioti2023immunotherapyandits pages 1-2, alkassis2024therapeuticadvancesin pages 10-12) | Vallini 2023; Dessinioti 2023 | https://doi.org/10.3390/cells12212534; https://doi.org/10.5826/dpc.1304a252 |
| UV-associated promoter/non-Hedgehog mutations | **TERT**, **DPH3-OXNAD1** | Somatic | **TERT** 39%–74%; **DPH3-OXNAD1** 42% (alkassis2024therapeuticadvancesin pages 2-4) | Reported as UV-associated alterations complementing Hedgehog and TP53 pathway disruption (alkassis2024therapeuticadvancesin pages 2-4) | Alkassis 2024 | https://doi.org/10.3390/cancers16173075 |
| Additional driver/modifier landscape | **NOTCH1/2**, **RAS** family, **MYCN**, **CSMD1/2**, **IFIH1**, **CCR5**, **TPCN2**, **FADS2**, **CDKL1** | Mostly somatic for tumor drivers; germline susceptibility loci from GWAS | 122 BCC-associated loci identified in multi-ancestry GWAS; 36 novel loci (choquet2024multiancestrygenomewidemetaanalysis pages 7-7). Earlier multi-phenotype analysis identified 78 BCC risk loci, including 19 previously unknown (from search results summary) | Supports polygenic susceptibility, pigmentation/immune pathway overlap, and risk stratification beyond HH alone (choquet2024multiancestrygenomewidemetaanalysis pages 7-7) | Choquet 2024; Seviiri 2022 | https://doi.org/10.1038/s42003-023-05753-7; https://doi.org/10.1038/s41467-022-35345-8 |
| Immunosuppressive tumor microenvironment | Tregs, CAFs, IL-6, IL-10, CCL22, LAG-3, PD-1, macrophages, γδ T cells | Tumor microenvironmental state | No single uniform frequency; checkpoint markers LAG-3 and PD-1 expressed on **>1%** of TILs in profiled tumors (alkassis2024therapeuticadvancesin pages 2-4) | Advanced BCC shows macrophage-driven inflammation; low-risk lesions enriched for γδ T cells; supports immunotherapy combinations (alkassis2024therapeuticadvancesin pages 2-4) | Alkassis 2024 | https://doi.org/10.3390/cancers16173075 |
| Cell of origin / developmental programs | Hair follicle stem cells, interfollicular epidermis, bulge stem cells, SHH/SMO | Experimental models; developmental lineage mechanisms | Not a mutation frequency; lineage evidence indicates superficial BCC may arise from interfollicular epidermis, nodular BCC from hair follicle stem cells (nicoletti2024dysembryogeneticpathogenesisof pages 8-10, nicoletti2024dysembryogeneticpathogenesisof pages 11-12) | Mouse and xenograft models support Hedgehog-driven reprogramming; relevant for understanding subtype biology rather than diagnosis (nicoletti2024dysembryogeneticpathogenesisof pages 8-10, cong2025mechanismsandtherapeutic pages 4-5) | Nicoletti 2024; Cong 2025 | https://doi.org/10.3390/ijms25158452; https://doi.org/10.1038/s41420-025-02327-w |
| Therapeutic resistance axis | **SMO**, downstream GLI signaling, non-canonical **RAS-RAF-MEK-ERK** inputs | Acquired somatic/drug-resistance biology | No fixed frequency stated in retrieved text | HHI benefit can be limited by adverse events and resistance; non-canonical GLI activation via MAPK signaling is a proposed bypass mechanism (vallini2023signalingpathwaysand pages 2-3, vallini2023signalingpathwaysand pages 1-2) | Vallini 2023 | https://doi.org/10.3390/cells12212534 |


*Table: This table summarizes the core molecular pathways, genes, and mechanistic features implicated in basal cell carcinoma, with frequencies and notes drawn from the retrieved evidence. It is useful for linking clinical BCC biology to driver alterations, mutational processes, and treatment resistance.*

### 4.2 Pathogenic variants and somatic vs germline
- **Somatic drivers (sporadic BCC):** Hedgehog-pathway mutations are common; one 2023 advanced BCC review summarizes that ~**85%** of sporadic BCCs carry HH-pathway mutations (~**73% PTCH** loss-of-function, ~**20% SMO** gain-of-function, ~**8% SUFU** loss-of-function). (vallini2023signalingpathwaysand pages 2-3)
- **Germline predisposition:** Gorlin syndrome/NBCCS is linked to germline PTCH1; a 2023 review reports a small fraction of BCC is linked to Gorlin syndrome. (vallini2023signalingpathwaysand pages 2-3)

### 4.3 Epigenetic, chromosomal, and multi-omics
The retrieved evidence base emphasizes mutational and transcriptomic/tumor-microenvironment features rather than a consistent epigenetic signature; therefore, no specific DNA methylation/histone-modification markers are asserted here.

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
- **UV radiation** (sunlight and indoor tanning) and **ionizing radiation** are consistently cited contributors to BCC development. (schmults2023basalcellskin pages 2-4, vallini2023signalingpathwaysand pages 2-3)
- **Arsenic exposure** is listed as a risk factor in guideline/review evidence and is associated with NMSC molecular profiling in an arsenic-exposed population. (lang2024s2kguidelinebasal pages 1-2, alkassis2024therapeuticadvancesin pages 2-4)

### 5.2 Infectious agents
No specific infectious agent is established as a direct cause of BCC in the retrieved evidence.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
1. **Trigger/exposure:** chronic UV exposure and/or ionizing radiation (and other modifiers such as immunosuppression). (schmults2023basalcellskin pages 2-4, vallini2023signalingpathwaysand pages 2-3)
2. **DNA damage and mutation acquisition:** UV-signature mutations commonly affect tumor suppressors (e.g., TP53) and Hedgehog pathway components (e.g., PTCH). (schmults2023basalcellskin pages 2-4, lang2024s2kguidelinebasal pages 1-2)
3. **Pathway dysregulation:** loss of PTCH-mediated repression of SMO → activation of GLI transcriptional programs → keratinocyte proliferation and tumor growth. (sol2024therapeuticapproachesfor pages 2-3, vallini2023signalingpathwaysand pages 2-3)
4. **Local invasion and immune modulation:** BCC can show high tumor mutational burden with an “immune excluded”/immunosuppressive microenvironment, providing a rationale for immune checkpoint blockade in advanced disease. (dessinioti2023immunotherapyandits pages 1-2, alkassis2024therapeuticadvancesin pages 2-4)

### 6.2 Suggested ontology mappings
- **GO biological processes (examples):**
  - Hedgehog signaling pathway (GO:0007224)
  - Regulation of cell proliferation (GO:0042127)
  - DNA damage response (GO:0006974)
  - Keratinocyte differentiation (GO:0030216)
- **Cell Ontology (examples):**
  - Keratinocyte (CL:0000312)
  - Epidermal basal cell (best-effort; basal keratinocyte subtype)
  - Hair follicle stem cell (best-effort; stem/progenitor niche implicated in models) (nicoletti2024dysembryogeneticpathogenesisof pages 8-10)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- **Primary organ:** skin (epidermis and adnexal structures), with most lesions on **sun-exposed sites** (face/head/neck; also trunk). (lang2024s2kguidelinebasal pages 1-2, sol2024therapeuticapproachesfor pages 7-8)

### 7.2 Cell level
- **Primary affected cell type:** keratinocytes/basal epidermal lineage. (sol2024therapeuticapproachesfor pages 7-8, sol2024therapeuticapproachesfor pages 2-3)
- **Cell(s) of origin (model-based):** evidence supports contributions from **interfollicular epidermis** (superficial BCC) and **hair follicle stem cells** (nodular BCC) in experimental contexts. (nicoletti2024dysembryogeneticpathogenesisof pages 8-10)

### 7.3 UBERON suggestions (best-effort)
- Skin (UBERON:0002097)
- Epidermis (UBERON:0001003)
- Hair follicle (UBERON:0002074)

---

## 8. Temporal Development

- **Onset pattern:** typically chronic/insidious in older adults; rapid growth and recurrence characterize the minority “difficult-to-treat” subset. (alkassis2024therapeuticadvancesin pages 1-2, lang2024s2kguidelinebasal pages 1-2)
- **Progression:** Most cases are “easy-to-treat”; a review-derived classification estimates **~95%** are easy-to-treat, with **locally advanced** and **metastatic** disease estimated at **0.8%** and **0.0028–0.55%**, respectively. (sol2024therapeuticapproachesfor pages 7-8)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (selected recent statistics)
A data-rich summary table is provided below.

| Metric | Value | Population/Setting | Source (first author year) | PMID if known | URL if available |
|---|---:|---|---|---|---|
| US annual BCC cases estimate | 2 million Americans annually | United States; estimated annual incidence in NCCN guideline | Schmults 2023 (schmults2023basalcellskin pages 2-4) |  | https://doi.org/10.6004/jnccn.2023.0056 |
| US annual BCC cases estimate | 3.6 million cases diagnosed annually | United States; review estimate | Alkassis 2024 (alkassis2024therapeuticadvancesin pages 1-2) |  | https://doi.org/10.3390/cancers16173075 |
| Germany incidence | ≥200 per 100,000/year | Germany | Lang 2024 (lang2024s2kguidelinebasal pages 1-2) |  | https://doi.org/10.1111/ddg.15566 |
| Lifetime prevalence | >10% | Central/Northern European groups | Lang 2024 (lang2024s2kguidelinebasal pages 1-2) |  | https://doi.org/10.1111/ddg.15566 |
| Japan BCC share of skin cancers | 37.2% | Japan National Cancer Registry 2016–2017 | Ogata 2023 (ogata2023epidemiologyofskin pages 1-2) |  | https://doi.org/10.1111/cas.15823 |
| Japan BCC incidence | 3.63 per 100,000 | Japan; WHO standard population model | Ogata 2023 (ogata2023epidemiologyofskin pages 1-2) |  | https://doi.org/10.1111/cas.15823 |
| Metastatic rate / incidence | <0.1% | General BCC; NCCN summary | Schmults 2023 (schmults2023basalcellskin pages 2-4) |  | https://doi.org/10.6004/jnccn.2023.0056 |
| Metastatic rate / incidence | 0.0028%–0.55% | General BCC; guideline/review estimates | Lang 2024 (lang2024s2kguidelinebasal pages 1-2) |  | https://doi.org/10.1111/ddg.15566 |
| Progression to advanced disease | 1%–10% | BCC overall progressing to advanced stage | Alkassis 2024 (alkassis2024therapeuticadvancesin pages 1-2) |  | https://doi.org/10.3390/cancers16173075 |
| laBCC incidence | 0.8% | Difficult-to-treat BCC classification | Sol 2024 (sol2024therapeuticapproachesfor pages 7-8) |  | https://doi.org/10.3390/ijms25137056 |
| mBCC incidence | 0.0028%–0.55% | Difficult-to-treat BCC classification | Sol 2024 (sol2024therapeuticapproachesfor pages 7-8) |  | https://doi.org/10.3390/ijms25137056 |
| 5-year recurrence after Mohs surgery (primary BCC) | 1.0% | Systematic review-weighted average | Schmults 2023 (schmults2023basalcellskin pages 7-9) |  | https://doi.org/10.6004/jnccn.2023.0056 |
| 5-year recurrence after Mohs surgery (recurrent BCC) | 5.6% | Systematic review-weighted average | Schmults 2023 (schmults2023basalcellskin pages 7-9) |  | https://doi.org/10.6004/jnccn.2023.0056 |
| 5-year recurrence after standard excision (primary BCC) | 10.1% | Comparative analyses cited in NCCN | Schmults 2023 (schmults2023basalcellskin pages 7-9) |  | https://doi.org/10.6004/jnccn.2023.0056 |
| 5-year recurrence after standard excision (recurrent BCC) | 17.4% | Comparative analyses cited in NCCN | Schmults 2023 (schmults2023basalcellskin pages 7-9) |  | https://doi.org/10.6004/jnccn.2023.0056 |
| 5-year recurrence after destruction/C&E | 1.2%–40% | Reported range; varies by risk/anatomic site/subtype | Schmults 2023 (schmults2023basalcellskin pages 7-9) |  | https://doi.org/10.6004/jnccn.2023.0056 |
| 5-year recurrence after destruction | 4.9% (95% CI 2.3–7.4) | Prospective cohort of primary NMSC (BCC+SCC) | Chren 2013 (chren2013tumorrecurrence5 pages 1-2) |  | https://doi.org/10.1038/jid.2012.403 |
| 5-year recurrence after excision | 3.5% (95% CI 1.8–5.2) | Prospective cohort of primary NMSC (BCC+SCC) | Chren 2013 (chren2013tumorrecurrence5 pages 1-2) |  | https://doi.org/10.1038/jid.2012.403 |
| 5-year recurrence after Mohs surgery | 2.1% (95% CI 0.6–3.5) | Prospective cohort of primary NMSC (BCC+SCC) | Chren 2013 (chren2013tumorrecurrence5 pages 1-2) |  | https://doi.org/10.1038/jid.2012.403 |
| Adjusted 5-year recurrence after destruction | 3.8% (95% CI 1.4–6.1) | Prospective cohort of primary NMSC (BCC+SCC) | Chren 2013 (chren2013tumorrecurrence5 pages 3-4) |  | https://doi.org/10.1038/jid.2012.403 |
| Adjusted 5-year recurrence after excision | 3.3% (95% CI 1.6–4.9) | Prospective cohort of primary NMSC (BCC+SCC) | Chren 2013 (chren2013tumorrecurrence5 pages 3-4) |  | https://doi.org/10.1038/jid.2012.403 |
| Adjusted 5-year recurrence after Mohs surgery | 1.7% (95% CI 0.4–3.0) | Prospective cohort of primary NMSC (BCC+SCC) | Chren 2013 (chren2013tumorrecurrence5 pages 3-4) |  | https://doi.org/10.1038/jid.2012.403 |
| Cemiplimab ORR after prior HHI | 31% (26/84); CR 6%, PR 25% | Locally advanced BCC after hedgehog inhibitor therapy | Stratigos 2021 (stratigos2021cemiplimabinlocally pages 5-6, stratigos2021cemiplimabinlocally pages 1-1) |  | https://doi.org/10.1016/S1470-2045(21)00126-1 |
| Cemiplimab median PFS | 19 months (95% CI 9–not evaluable) | Locally advanced BCC after hedgehog inhibitor therapy | Stratigos 2021 (stratigos2021cemiplimabinlocally pages 5-6) |  | https://doi.org/10.1016/S1470-2045(21)00126-1 |
| Cemiplimab median duration of response | Not reached; 91% in response at 6 months, 85% at 12 months | Responders with locally advanced BCC after hedgehog inhibitor therapy | Stratigos 2021 (stratigos2021cemiplimabinlocally pages 5-6) |  | https://doi.org/10.1016/S1470-2045(21)00126-1 |


*Table: This table compiles high-yield epidemiology, progression, metastasis, recurrence, and systemic therapy outcome statistics for basal cell carcinoma from the gathered evidence. It is designed to support rapid comparison of population burden and clinically relevant outcome benchmarks.*

Key points from recent guidelines and registry analyses:
- NCCN estimates **~2 million Americans affected annually** (acknowledging under-registration). (schmults2023basalcellskin pages 2-4)
- German S2k guideline reports **≥200/100,000/year** incidence in Germany and lifetime prevalence **>10%** in central/northern Europe. (lang2024s2kguidelinebasal pages 1-2)
- Japan registry analysis (2016–2017) reports BCC incidence **3.63/100,000** (WHO model). (ogata2023epidemiologyofskin pages 1-2)

### 9.2 Genetic architecture
- Rare high-penetrance syndromes (e.g., Gorlin/NBCCS, XP) contribute to susceptibility. (lang2024s2kguidelinebasal pages 1-2, vallini2023signalingpathwaysand pages 2-3)
- Common-variant susceptibility is polygenic; a multi-ancestry GWAS meta-analysis (50,531 cases; 762,234 controls) identified **122 BCC-associated loci (36 novel)**. (choquet2024multiancestrygenomewidemetaanalysis pages 7-7)

---

## 10. Diagnostics

### 10.1 Core diagnostic approach
- **Clinical exam + biopsy confirmation:** NCCN recommends biopsy that includes deep reticular dermis; total body skin exam is recommended because patients are at increased risk of additional lesions and melanoma. (schmults2023basalcellskin pages 2-4)
- **Imaging in selected cases:** MRI preferred for suspected perineural disease; CT preferred for suspected bony involvement. (schmults2023basalcellskin pages 2-4)

### 10.2 Risk stratification and real-world clinical algorithms
NCCN provides operational risk stratification (low vs high risk) based on clinical and pathologic features and provides a treatment flowchart that escalates to Mohs surgery or margin-controlled approaches for high-risk tumors.

- **NCCN risk stratification table and treatment algorithms (visual evidence):** (schmults2023basalcellskin media 73ba3136, schmults2023basalcellskin media 96ea4de3, schmults2023basalcellskin media e102265c)

### 10.3 Differential diagnosis
Not systematically extracted from the retrieved evidence; in practice includes melanoma (especially for pigmented lesions), SCC, sebaceous hyperplasia, adnexal tumors, inflammatory dermatoses (for superficial BCC), and benign ulcer etiologies.

---

## 11. Outcome / Prognosis

### 11.1 Metastasis and advanced disease
- NCCN describes metastatic rate as **<0.1%**. (schmults2023basalcellskin pages 2-4)
- German guideline gives metastatic incidence estimates **0.0028%–0.55%**. (lang2024s2kguidelinebasal pages 1-2)

### 11.2 Local control / recurrence benchmarks
Evidence for 5-year recurrence varies depending on case-mix and treatment selection. Two complementary evidence types are useful:

1) **Prospective cohort (NMSC overall) with CIs:** unadjusted 5-year recurrence after Mohs **2.1% (95% CI 0.6–3.5)**, excision **3.5% (1.8–5.2)**, destruction **4.9% (2.3–7.4)**. (chren2013tumorrecurrence5 pages 1-2)

2) **Systematic-review weighted averages emphasizing BCC recurrence (commonly cited in practice):** 5-year recurrence for primary BCC **1.0%** after Mohs vs **10.1%** after excision; recurrent BCC **5.6%** after Mohs vs **17.4%** after excision. (schmults2023basalcellskin pages 7-9, kauvar2015consensusfornonmelanoma pages 7-8)

---

## 12. Treatment

### 12.1 Treatment landscape and real-world implementation
A structured treatment table (including MAXO suggestions) is provided below.

| Treatment modality | Indication (low-risk/high-risk/locally advanced/metastatic) | Mechanism/approach | Key outcome stats (recurrence or ORR/PFS where available) | Key adverse events/limitations (if stated in evidence) | Suggested MAXO term (best-effort) | Evidence source (author year) | URL |
|---|---|---|---|---|---|---|---|
| Standard surgical excision | Primarily low-risk; also selected high-risk lesions with margin control | Elliptical excision with histopathologic margin assessment | 5-year recurrence for primary BCC reported as 10.1%; recurrent BCC 17.4% in comparative analyses; in a prospective NMSC cohort, unadjusted 5-year recurrence 3.5% (95% CI 1.8-5.2), adjusted 3.3% (95% CI 1.6-4.9) (schmults2023basalcellskin pages 7-9, chren2013tumorrecurrence5 pages 1-2, chren2013tumorrecurrence5 pages 3-4) | Incomplete excision rates reported 3.2%-61.5% depending on site/subtype/provider; may be suboptimal for high-risk facial tumors (schmults2023basalcellskin pages 7-9) | MAXO: surgical excision | Schmults 2023; Chren 2013 | https://doi.org/10.6004/jnccn.2023.0056 ; https://doi.org/10.1038/jid.2012.403 |
| Mohs micrographic surgery (MMS) | High-risk, recurrent, tissue-sparing critical sites; many head/neck tumors | Stage-wise excision with complete peripheral/deep margin assessment | 5-year recurrence 1.0% for primary BCC and 5.6% for recurrent BCC in NCCN-cited meta-analyses; prospective cohort unadjusted 2.1% (95% CI 0.6-3.5), adjusted 1.7% (95% CI 0.4-3.0); Denmark nationwide cohort: overall 5-year recurrence 3.8%, primary 3.1%, recurrent 5.3% (schmults2023basalcellskin pages 7-9, chren2013tumorrecurrence5 pages 1-2, chren2013tumorrecurrence5 pages 3-4) | Resource-intensive; generally reserved for high-risk or anatomically critical tumors (schmults2023basalcellskin media 73ba3136, schmults2023basalcellskin media 96ea4de3, schmults2023basalcellskin media e102265c) | MAXO: Mohs micrographic surgery | Schmults 2023; Chren 2013 | https://doi.org/10.6004/jnccn.2023.0056 ; https://doi.org/10.1038/jid.2012.403 |
| Curettage and electrodesiccation (C&E) / destruction | Selected low-risk superficial or nodular lesions | Physical tumor destruction by curettage plus electrodessication | 5-year recurrence range 1.2%-40% depending on risk/site/subtype; prospective cohort unadjusted 4.9% (95% CI 2.3-7.4), adjusted 3.8% (95% CI 1.4-6.1) for NMSC overall (schmults2023basalcellskin pages 7-9, chren2013tumorrecurrence5 pages 1-2, chren2013tumorrecurrence5 pages 3-4) | No histologic margin assessment; higher recurrence in high-risk locations/aggressive histology; not preferred in terminal hair-bearing sites (schmults2023basalcellskin pages 7-9) | MAXO: curettage of skin lesion; electrodesiccation | Schmults 2023; Chren 2013 | https://doi.org/10.6004/jnccn.2023.0056 ; https://doi.org/10.1038/jid.2012.403 |
| Radiotherapy | Alternative for unresectable tumors, positive margins when re-excision not feasible, or patients unsuitable for surgery; recurrent/high-risk in selected settings | Local ionizing radiation for tumor control | Meta-analytic/guide-level evidence suggests recurrence can be comparable to surgery in selected cases; NCCN and S2k list RT as a major modality, especially when surgery is not feasible (alkassis2024therapeuticadvancesin pages 1-2, lang2024s2kguidelinebasal pages 1-2, sol2024therapeuticapproachesfor pages 7-8) | Cosmetic/functional trade-offs; generally not first choice for most operable cases (alkassis2024therapeuticadvancesin pages 1-2, lang2024s2kguidelinebasal pages 1-2) | MAXO: radiation therapy | Alkassis 2024; Lang 2024; Sol 2024 | https://doi.org/10.3390/cancers16173075 ; https://doi.org/10.1111/ddg.15566 ; https://doi.org/10.3390/ijms25137056 |
| Topical imiquimod | Selected superficial low-risk BCC | Immune response modifier (TLR7 agonist) | Included as topical option in guidelines/reviews for appropriately selected superficial disease; no robust recurrence statistic extracted from retrieved texts (alkassis2024therapeuticadvancesin pages 2-4, lang2024s2kguidelinebasal pages 1-2) | Limited to selected superficial lesions; not appropriate for many high-risk tumors (alkassis2024therapeuticadvancesin pages 2-4, lang2024s2kguidelinebasal pages 1-2) | MAXO: topical immune response modifier therapy | Alkassis 2024; Lang 2024 | https://doi.org/10.3390/cancers16173075 ; https://doi.org/10.1111/ddg.15566 |
| Topical 5-fluorouracil | Selected superficial low-risk BCC | Topical antimetabolite chemotherapy | Listed in guidelines/reviews for superficial disease; no extracted pooled recurrence number in retrieved evidence (alkassis2024therapeuticadvancesin pages 2-4, lang2024s2kguidelinebasal pages 1-2) | Limited role outside superficial disease; lacks margin control (alkassis2024therapeuticadvancesin pages 2-4) | MAXO: topical antimetabolite therapy | Alkassis 2024; Lang 2024 | https://doi.org/10.3390/cancers16173075 ; https://doi.org/10.1111/ddg.15566 |
| Photodynamic therapy (PDT) | Selected superficial facial/scalp or other low-risk superficial BCC | Photosensitizer plus activating light causing local cytotoxicity | Used in real-world management of superficial lesions; no trial-level recurrence figure extracted here (alkassis2024therapeuticadvancesin pages 2-4) | Best suited to superficial disease; not a standard approach for deeply invasive/high-risk BCC (alkassis2024therapeuticadvancesin pages 2-4) | MAXO: photodynamic therapy | Alkassis 2024 | https://doi.org/10.3390/cancers16173075 |
| Vismodegib | Locally advanced/metastatic BCC not amenable to curative surgery/RT; first-line systemic | Small-molecule SMO inhibitor targeting Hedgehog pathway | Guideline-supported first-line systemic option for advanced BCC; advanced disease estimates: laBCC ~0.8%, mBCC 0.0028%-0.55%; no ORR extracted from retrieved primary text here (sol2024therapeuticapproachesfor pages 7-8, lang2024s2kguidelinebasal pages 1-2, dessinioti2023immunotherapyandits pages 1-2) | High discontinuation burden across HHIs: vismodegib discontinuation 88%-92%, with about half stopping after ~8-12 months (dessinioti2023immunotherapyandits pages 1-2) | MAXO: Hedgehog pathway inhibitor therapy | Sol 2024; Lang 2024; Dessinioti 2023 | https://doi.org/10.3390/ijms25137056 ; https://doi.org/10.1111/ddg.15566 ; https://doi.org/10.5826/dpc.1304a252 |
| Sonidegib | Locally advanced/metastatic BCC not amenable to curative surgery/RT; first-line systemic alternative | Small-molecule SMO inhibitor targeting Hedgehog pathway | Guideline-supported first-line systemic option for advanced BCC; no ORR extracted from retrieved primary text here (dessinioti2023immunotherapyandits pages 1-2, lang2024s2kguidelinebasal pages 1-2) | Approximate discontinuation ~92%; resistance and tolerability issues limit long-term use (dessinioti2023immunotherapyandits pages 1-2, vallini2023signalingpathwaysand pages 2-3) | MAXO: Hedgehog pathway inhibitor therapy | Dessinioti 2023; Lang 2024; Vallini 2023 | https://doi.org/10.5826/dpc.1304a252 ; https://doi.org/10.1111/ddg.15566 ; https://doi.org/10.3390/cells12212534 |
| Cemiplimab | Locally advanced or metastatic BCC after HHI intolerance/progression; second-line systemic | Anti-PD-1 immune checkpoint inhibitor | Phase 2 laBCC after HHI: ORR 31% (26/84; 95% CI 21-42), CR 6%, PR 25%; median time to response 4.3 months; median PFS 19 months (95% CI 9-NE); median DOR not reached, 91% in response at 6 months and 85% at 12 months; median DOR 26.2 months reported in later review summary (stratigos2021cemiplimabinlocally pages 5-6, stratigos2021cemiplimabinlocally pages 1-1, dessinioti2023immunotherapyandits pages 4-6) | Grade 3-4 treatment-emergent AEs in 48%; immune-related AEs in 25%, hypothyroidism 10%; discontinuation commonly due to progression or AEs (stratigos2021cemiplimabinlocally pages 1-1, dessinioti2023immunotherapyandits pages 4-6) | MAXO: PD-1 inhibitor immunotherapy | Stratigos 2021; Dessinioti 2023 | https://doi.org/10.1016/S1470-2045(21)00126-1 ; https://doi.org/10.5826/dpc.1304a252 |
| Nivolumab (investigational) | Advanced BCC in clinical trials | Anti-PD-1 immunotherapy | Phase II signal: ORR 50% in 10 patients with nivolumab monotherapy; 10% in 6 patients with nivolumab + relatlimab in one review summary (alkassis2024therapeuticadvancesin pages 10-12) | Early-phase/investigational; very small cohorts (alkassis2024therapeuticadvancesin pages 10-12) | MAXO: PD-1 inhibitor immunotherapy | Alkassis 2024 | https://doi.org/10.3390/cancers16173075 |
| Combined cemiplimab + sonidegib (case-report implementation) | Synchronous advanced cSCC/BCC of head and neck; individualized multidisciplinary use | Combined PD-1 blockade plus SMO inhibition | Two reported cases achieved remarkable clinical benefit and long-term responses without major adverse events (sol2024therapeuticapproachesfor pages 7-8) | Limited to case reports; not standard guideline algorithm (sol2024therapeuticapproachesfor pages 7-8) | MAXO: combination immunotherapy and targeted therapy | Colombo 2023 | https://doi.org/10.3389/fonc.2023.1111146 |


*Table: This table summarizes major basal cell carcinoma treatment options across low-risk, high-risk, and advanced disease, emphasizing real-world implementation and quantitative outcomes where available. It is useful for comparing local therapies, systemic Hedgehog inhibitors, and immunotherapy in a single evidence-linked view.*

### 12.2 Surgery and local therapies
- **Surgery** is widely described as first-line for most BCCs; Mohs is prioritized for high-risk lesions to minimize recurrence and preserve tissue. (lang2024s2kguidelinebasal pages 1-2, schmults2023basalcellskin media 73ba3136)

### 12.3 Targeted therapy: Hedgehog pathway inhibitors (HHIs)
For locally advanced/metastatic BCC not amenable to curative surgery/radiation, **vismodegib** and **sonidegib** are first-line systemic options. High discontinuation rates are emphasized in 2023 expert review evidence: **88–92%** discontinuation for vismodegib and approximately **92%** for sonidegib, with about half discontinuing after **~8–12 months**. (dessinioti2023immunotherapyandits pages 1-2)

### 12.4 Immunotherapy: PD-1 blockade
For advanced BCC after HHI failure/intolerance, **cemiplimab** is supported by phase 2 evidence. In the locally advanced cohort (n=84), independent central review ORR was **31% (26/84; 95% CI 21–42)** with **6% complete** and **25% partial** responses, and **median PFS 19 months (95% CI 9–not evaluable)**. (stratigos2021cemiplimabinlocally pages 1-1, stratigos2021cemiplimabinlocally pages 5-6)

Direct efficacy statement from the trial excerpt (data): ORR and response composition are reported numerically as above; median time to response was **4.3 months (IQR 4.2–7.2)**, and median duration of response was not reached, with **85%** remaining in response at 12 months (Kaplan–Meier). (stratigos2021cemiplimabinlocally pages 5-6)

---

## 13. Prevention

### 13.1 Primary prevention (UV/radiation)
Photoprotection is emphasized as the first-choice prevention strategy for non-melanoma skin cancers given UV’s central role. (hyeraci2023systemicphotoprotectionin pages 1-2)

### 13.2 Chemoprevention (nicotinamide)
Evidence is mixed depending on population and pooling strategy:
- **Mainville et al. meta-analysis (2022)**: oral nicotinamide associated with reduced new skin cancers overall (**rate ratio 0.50; 95% CI 0.29–0.85**) and the authors report significant reduction in BCC and cSCC. (mainville2022effectofnicotinamide pages 1-2)
- **Tosti et al. meta-analysis (2023)**: pooled estimates were not statistically significant for BCC (**RR 0.88; 95% CI 0.50–1.55**) when combining immunocompetent and immunosuppressed cohorts; authors conclude insufficient evidence for significant reduction. (tosti2023theroleof pages 1-2)
- **Guideline inclusion statement (systemic photoprotection review 2023):** only a few oral agents have shown efficacy in trials and have been incorporated into international guidance for NMSC prevention, including **nicotinamide and retinoids**. (hyeraci2023systemicphotoprotectionin pages 1-2)

### 13.3 Secondary prevention (screening/early detection)
- NCCN emphasizes total body skin examination and careful follow-up due to increased risk of additional keratinocyte cancers and melanoma. (schmults2023basalcellskin pages 2-4)

---

## 14. Other Species / Natural Disease
The retrieved evidence focused on mechanistic model systems rather than naturally occurring BCC in non-human populations; therefore, naturally occurring veterinary BCC epidemiology is not asserted here.

---

## 15. Model Organisms
Evidence supports several established experimental approaches:
- **Transgenic mouse models** overexpressing HH mediators (SHH, GLI1/2, oncogenic SMO) develop BCC-like tumors. (cong2025mechanismsandtherapeutic pages 4-5)
- **Human keratinocyte xenograft models:** engineered keratinocytes expressing SHH grafted onto nude mice generate BCC-like structures. (cong2025mechanismsandtherapeutic pages 4-5)
- **Lineage/cell-of-origin models:** data support contributions of interfollicular epidermis vs hair follicle stem cells for different clinical subtypes; neural niche contributions are also described in mouse studies summarized in a 2024 review. (nicoletti2024dysembryogeneticpathogenesisof pages 8-10)
- **Ex vivo models:** ex vivo skin explant culture models are noted as practical for testing therapies when primary BCC cultures are hard to maintain. (vallini2023signalingpathwaysand pages 13-14)

---

## Notes on evidence gaps and compliance with requested identifiers
- **PMIDs:** Many of the retrieved recent guideline/review PDFs did not expose PMID fields in the tool outputs; therefore PMID annotation is incomplete in this run.
- **ICD-11/MONDO/MeSH official IDs:** Not available directly in retrieved full texts; therefore not asserted.

---

## Key NCCN algorithm figures (visual evidence)
- NCCN risk stratification table, initial risk categorization flowchart, and high-risk treatment algorithm were extracted as images from the NCCN guideline PDF. (schmults2023basalcellskin media 73ba3136, schmults2023basalcellskin media 96ea4de3, schmults2023basalcellskin media e102265c)


References

1. (schmults2023basalcellskin pages 2-4): C. Schmults, Rachel Blitzblau, S. Aasi, Murad Alam, Arya Amini, Kristin Bibee, Jeremy S. Bordeaux, Pei-Ling Chen, Carlo M Contreras, D. Dimaio, J. M. Donigan, J. Farma, Karthik Ghosh, Kelly Harms, Alan L Ho, J. N. Lukens, Lawrence Mark, Theresa Medina, K. Nehal, Paul Nghiem, K. Olino, Soo Park, Tejesh Patel, Igor Puzanov, Jason Rich, A. Sekulic, Ashok R. Shaha, Divya Srivastava, Valencia Thomas, Courtney Tomblinson, Puja S Venkat, Y. G. Xu, Siegrid Yu, Mehran Yusuf, Beth McCullough, and Sara Espinosa. Basal cell skin cancer, version 2.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 21 11:1181-1203, Nov 2023. URL: https://doi.org/10.6004/jnccn.2023.0056, doi:10.6004/jnccn.2023.0056. This article has 133 citations.

2. (lang2024s2kguidelinebasal pages 1-2): Berenice M. Lang, Panagiotis Balermpas, Andrea Bauer, Andreas Blum, Thomas Dirschka, Markus Follmann, Jorge Frank, Bernhard Frerich, Klaus Fritz, Axel Hauschild, Ludwig M. Heindl, Hans‐Peter Howaldt, Stephan Ihrler, Vinodh Kakkassery, Bernhard Klumpp, Albrecht Krause‐Bergmann, Christoph Löser, Markus Meissner, Michael M. Sachse, Max Schlaak, Michael P. Schön, Lutz Tischendorf, Michael Tronnier, Dirk Vordermark, Julia Welzel, Michael Weichenthal, Susanne Wiegand, Roland Kaufmann, and Stephan Grabbe. S2k guideline basal cell carcinoma of the skin (update 2023). Journal Der Deutschen Dermatologischen Gesellschaft, 22:1697-1714, Nov 2024. URL: https://doi.org/10.1111/ddg.15566, doi:10.1111/ddg.15566. This article has 10 citations and is from a peer-reviewed journal.

3. (sol2024therapeuticapproachesfor pages 7-8): Stefano Sol, Fabiana Boncimino, Kristina Todorova, Sarah Elizabeth Waszyn, and Anna Mandinova. Therapeutic approaches for non-melanoma skin cancer: standard of care and emerging modalities. International Journal of Molecular Sciences, 25:7056, Jun 2024. URL: https://doi.org/10.3390/ijms25137056, doi:10.3390/ijms25137056. This article has 36 citations.

4. (choquet2024multiancestrygenomewidemetaanalysis pages 7-7): Hélène Choquet, Chen Jiang, Jie Yin, Yuhree Kim, Thomas J. Hoffmann, Stella Aslibekyan, Adam Auton, Elizabeth Babalola, Robert K. Bell, Jessica Bielenberg, Katarzyna Bryc, Emily Bullis, Daniella Coker, Gabriel Cuellar Partida, Devika Dhamija, Sayantan Das, Sarah L. Elson, Teresa Filshtein, Kipper Fletez-Brant, Pierre Fontanillas, Will Freyman, Pooja M. Gandhi, Karl Heilbron, Barry Hicks, David A. Hinds, Ethan M. Jewett, Yunxuan Jiang, Katelyn Kukar, Keng-Han Lin, Maya Lowe, Jey McCreight, Matthew H. McIntyre, Steven J. Micheletti, Meghan E. Moreno, Joanna L. Mountain, Priyanka Nandakumar, Elizabeth S. Noblin, Jared O’Connell, Aaron A. Petrakovitz, G. David Poznik, Morgan Schumacher, Anjali J. Shastri, Janie F. Shelton, Jingchunzi Shi, Suyash Shringarpure, Vinh Tran, Joyce Y. Tung, Xin Wang, Wei Wang, Catherine H. Weldon, Peter Wilton, Alejandro Hernandez, Corinna Wong, Christophe Toukam Tchakouté, Eric Jorgenson, and Maryam M. Asgari. Multi-ancestry genome-wide meta-analysis identifies novel basal cell carcinoma loci and shared genetic effects with squamous cell carcinoma. Communications Biology, Jan 2024. URL: https://doi.org/10.1038/s42003-023-05753-7, doi:10.1038/s42003-023-05753-7. This article has 11 citations and is from a peer-reviewed journal.

5. (ogata2023epidemiologyofskin pages 1-2): Dai Ogata, Kenjiro Namikawa, Eiji Nakano, Maiko Fujimori, Yosuke Uchitomi, Takahiro Higashi, Naoya Yamazaki, and Akira Kawai. Epidemiology of skin cancer based on japan's national cancer registry 2016–2017. Cancer Science, 114:2986-2992, Apr 2023. URL: https://doi.org/10.1111/cas.15823, doi:10.1111/cas.15823. This article has 50 citations and is from a peer-reviewed journal.

6. (vallini2023signalingpathwaysand pages 1-2): Giulia Vallini, Laura Calabrese, Costanza Canino, Emanuele Trovato, Stefano Gentileschi, Pietro Rubegni, and Linda Tognetti. Signaling pathways and therapeutic strategies in advanced basal cell carcinoma. Cells, 12:2534, Oct 2023. URL: https://doi.org/10.3390/cells12212534, doi:10.3390/cells12212534. This article has 13 citations.

7. (yang2023trendsinkeratinocyte pages 1-8): Dorothy D Yang, Kim Borsky, Chinmay Jani, Conor Crowley, Jeremy N Rodrigues, Rubeta N Matin, Dominic C Marshall, Justin D Salciccioli, Joseph Shalhoub, and Richard Goodall. Trends in keratinocyte skin cancer incidence, mortality and burden of disease in 33 countries between 1990 and 2017. The British journal of dermatology, 188 2:237-246, Oct 2023. URL: https://doi.org/10.1093/bjd/ljac064, doi:10.1093/bjd/ljac064. This article has 48 citations.

8. (chren2013tumorrecurrence5 pages 1-2): Mary-Margaret Chren, Eleni Linos, Jeanette S. Torres, Sarah E. Stuart, Rupa Parvataneni, and W. John Boscardin. Tumor recurrence 5 years after treatment of cutaneous basal cell carcinoma and squamous cell carcinoma. Journal of Investigative Dermatology, 133:1188-1196, May 2013. URL: https://doi.org/10.1038/jid.2012.403, doi:10.1038/jid.2012.403. This article has 250 citations and is from a highest quality peer-reviewed journal.

9. (vallini2023signalingpathwaysand pages 2-3): Giulia Vallini, Laura Calabrese, Costanza Canino, Emanuele Trovato, Stefano Gentileschi, Pietro Rubegni, and Linda Tognetti. Signaling pathways and therapeutic strategies in advanced basal cell carcinoma. Cells, 12:2534, Oct 2023. URL: https://doi.org/10.3390/cells12212534, doi:10.3390/cells12212534. This article has 13 citations.

10. (dessinioti2023immunotherapyandits pages 1-2): Clio Dessinioti and Alexander Stratigos. Immunotherapy and its timing in advanced basal cell carcinoma treatment. Dermatology Practical &amp; Conceptual, pages e2023252, Oct 2023. URL: https://doi.org/10.5826/dpc.1304a252, doi:10.5826/dpc.1304a252. This article has 16 citations.

11. (alkassis2024therapeuticadvancesin pages 2-4): Samer Alkassis, Maya Shatta, and Deborah J. Wong. Therapeutic advances in advanced basal cell carcinoma. Cancers, 16:3075, Sep 2024. URL: https://doi.org/10.3390/cancers16173075, doi:10.3390/cancers16173075. This article has 9 citations.

12. (hyeraci2023systemicphotoprotectionin pages 1-2): Mariafrancesca Hyeraci, Elena Sofia Papanikolau, Marta Grimaldi, Francesco Ricci, Sabatino Pallotta, Rosanna Monetta, Ylenia Aura Minafò, Giovanni Di Lella, Giovanna Galdo, Damiano Abeni, Luca Fania, and Elena Dellambra. Systemic photoprotection in melanoma and non-melanoma skin cancer. Biomolecules, 13:1067, Jul 2023. URL: https://doi.org/10.3390/biom13071067, doi:10.3390/biom13071067. This article has 63 citations.

13. (schmults2023basalcellskin media 73ba3136): C. Schmults, Rachel Blitzblau, S. Aasi, Murad Alam, Arya Amini, Kristin Bibee, Jeremy S. Bordeaux, Pei-Ling Chen, Carlo M Contreras, D. Dimaio, J. M. Donigan, J. Farma, Karthik Ghosh, Kelly Harms, Alan L Ho, J. N. Lukens, Lawrence Mark, Theresa Medina, K. Nehal, Paul Nghiem, K. Olino, Soo Park, Tejesh Patel, Igor Puzanov, Jason Rich, A. Sekulic, Ashok R. Shaha, Divya Srivastava, Valencia Thomas, Courtney Tomblinson, Puja S Venkat, Y. G. Xu, Siegrid Yu, Mehran Yusuf, Beth McCullough, and Sara Espinosa. Basal cell skin cancer, version 2.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 21 11:1181-1203, Nov 2023. URL: https://doi.org/10.6004/jnccn.2023.0056, doi:10.6004/jnccn.2023.0056. This article has 133 citations.

14. (alkassis2024therapeuticadvancesin pages 1-2): Samer Alkassis, Maya Shatta, and Deborah J. Wong. Therapeutic advances in advanced basal cell carcinoma. Cancers, 16:3075, Sep 2024. URL: https://doi.org/10.3390/cancers16173075, doi:10.3390/cancers16173075. This article has 9 citations.

15. (alkassis2024therapeuticadvancesin pages 10-12): Samer Alkassis, Maya Shatta, and Deborah J. Wong. Therapeutic advances in advanced basal cell carcinoma. Cancers, 16:3075, Sep 2024. URL: https://doi.org/10.3390/cancers16173075, doi:10.3390/cancers16173075. This article has 9 citations.

16. (nicoletti2024dysembryogeneticpathogenesisof pages 8-10): Giovanni Nicoletti, Marco Saler, Umberto Moro, and Angela Faga. Dysembryogenetic pathogenesis of basal cell carcinoma: the evidence to date. International Journal of Molecular Sciences, 25:8452, Aug 2024. URL: https://doi.org/10.3390/ijms25158452, doi:10.3390/ijms25158452. This article has 2 citations.

17. (nicoletti2024dysembryogeneticpathogenesisof pages 11-12): Giovanni Nicoletti, Marco Saler, Umberto Moro, and Angela Faga. Dysembryogenetic pathogenesis of basal cell carcinoma: the evidence to date. International Journal of Molecular Sciences, 25:8452, Aug 2024. URL: https://doi.org/10.3390/ijms25158452, doi:10.3390/ijms25158452. This article has 2 citations.

18. (cong2025mechanismsandtherapeutic pages 4-5): Ge Cong, Xingyu Zhu, Xin Ru Chen, Hao Chen, and Wei Chong. Mechanisms and therapeutic potential of the hedgehog signaling pathway in cancer. Cell Death Discovery, Feb 2025. URL: https://doi.org/10.1038/s41420-025-02327-w, doi:10.1038/s41420-025-02327-w. This article has 41 citations and is from a peer-reviewed journal.

19. (sol2024therapeuticapproachesfor pages 2-3): Stefano Sol, Fabiana Boncimino, Kristina Todorova, Sarah Elizabeth Waszyn, and Anna Mandinova. Therapeutic approaches for non-melanoma skin cancer: standard of care and emerging modalities. International Journal of Molecular Sciences, 25:7056, Jun 2024. URL: https://doi.org/10.3390/ijms25137056, doi:10.3390/ijms25137056. This article has 36 citations.

20. (schmults2023basalcellskin pages 7-9): C. Schmults, Rachel Blitzblau, S. Aasi, Murad Alam, Arya Amini, Kristin Bibee, Jeremy S. Bordeaux, Pei-Ling Chen, Carlo M Contreras, D. Dimaio, J. M. Donigan, J. Farma, Karthik Ghosh, Kelly Harms, Alan L Ho, J. N. Lukens, Lawrence Mark, Theresa Medina, K. Nehal, Paul Nghiem, K. Olino, Soo Park, Tejesh Patel, Igor Puzanov, Jason Rich, A. Sekulic, Ashok R. Shaha, Divya Srivastava, Valencia Thomas, Courtney Tomblinson, Puja S Venkat, Y. G. Xu, Siegrid Yu, Mehran Yusuf, Beth McCullough, and Sara Espinosa. Basal cell skin cancer, version 2.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 21 11:1181-1203, Nov 2023. URL: https://doi.org/10.6004/jnccn.2023.0056, doi:10.6004/jnccn.2023.0056. This article has 133 citations.

21. (chren2013tumorrecurrence5 pages 3-4): Mary-Margaret Chren, Eleni Linos, Jeanette S. Torres, Sarah E. Stuart, Rupa Parvataneni, and W. John Boscardin. Tumor recurrence 5 years after treatment of cutaneous basal cell carcinoma and squamous cell carcinoma. Journal of Investigative Dermatology, 133:1188-1196, May 2013. URL: https://doi.org/10.1038/jid.2012.403, doi:10.1038/jid.2012.403. This article has 250 citations and is from a highest quality peer-reviewed journal.

22. (stratigos2021cemiplimabinlocally pages 5-6): Alexander J Stratigos, Aleksandar Sekulic, Ketty Peris, Oliver Bechter, Sorilla Prey, Martin Kaatz, Karl D Lewis, Nicole Basset-Seguin, Anne Lynn S Chang, Stèphane Dalle, Almudena Fernandez Orland, Lisa Licitra, Caroline Robert, Claas Ulrich, Axel Hauschild, Michael R Migden, Reinhard Dummer, Siyu Li, Suk-Young Yoo, Kosalai Mohan, Ebony Coates, Vladimir Jankovic, Nathalie Fiaschi, Emmanuel Okoye, Ioannis D Bassukas, Carmen Loquai, Vincenzo De Giorgi, Zeynep Eroglu, Ralf Gutzmer, Jens Ulrich, Susana Puig, Frank Seebach, Gavin Thurston, David M Weinreich, George D Yancopoulos, Israel Lowy, Timothy Bowler, and Matthew G Fury. Cemiplimab in locally advanced basal cell carcinoma after hedgehog inhibitor therapy: an open-label, multi-centre, single-arm, phase 2 trial. The Lancet Oncology, 22:848-857, Jun 2021. URL: https://doi.org/10.1016/s1470-2045(21)00126-1, doi:10.1016/s1470-2045(21)00126-1. This article has 335 citations and is from a highest quality peer-reviewed journal.

23. (stratigos2021cemiplimabinlocally pages 1-1): Alexander J Stratigos, Aleksandar Sekulic, Ketty Peris, Oliver Bechter, Sorilla Prey, Martin Kaatz, Karl D Lewis, Nicole Basset-Seguin, Anne Lynn S Chang, Stèphane Dalle, Almudena Fernandez Orland, Lisa Licitra, Caroline Robert, Claas Ulrich, Axel Hauschild, Michael R Migden, Reinhard Dummer, Siyu Li, Suk-Young Yoo, Kosalai Mohan, Ebony Coates, Vladimir Jankovic, Nathalie Fiaschi, Emmanuel Okoye, Ioannis D Bassukas, Carmen Loquai, Vincenzo De Giorgi, Zeynep Eroglu, Ralf Gutzmer, Jens Ulrich, Susana Puig, Frank Seebach, Gavin Thurston, David M Weinreich, George D Yancopoulos, Israel Lowy, Timothy Bowler, and Matthew G Fury. Cemiplimab in locally advanced basal cell carcinoma after hedgehog inhibitor therapy: an open-label, multi-centre, single-arm, phase 2 trial. The Lancet Oncology, 22:848-857, Jun 2021. URL: https://doi.org/10.1016/s1470-2045(21)00126-1, doi:10.1016/s1470-2045(21)00126-1. This article has 335 citations and is from a highest quality peer-reviewed journal.

24. (schmults2023basalcellskin media 96ea4de3): C. Schmults, Rachel Blitzblau, S. Aasi, Murad Alam, Arya Amini, Kristin Bibee, Jeremy S. Bordeaux, Pei-Ling Chen, Carlo M Contreras, D. Dimaio, J. M. Donigan, J. Farma, Karthik Ghosh, Kelly Harms, Alan L Ho, J. N. Lukens, Lawrence Mark, Theresa Medina, K. Nehal, Paul Nghiem, K. Olino, Soo Park, Tejesh Patel, Igor Puzanov, Jason Rich, A. Sekulic, Ashok R. Shaha, Divya Srivastava, Valencia Thomas, Courtney Tomblinson, Puja S Venkat, Y. G. Xu, Siegrid Yu, Mehran Yusuf, Beth McCullough, and Sara Espinosa. Basal cell skin cancer, version 2.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 21 11:1181-1203, Nov 2023. URL: https://doi.org/10.6004/jnccn.2023.0056, doi:10.6004/jnccn.2023.0056. This article has 133 citations.

25. (schmults2023basalcellskin media e102265c): C. Schmults, Rachel Blitzblau, S. Aasi, Murad Alam, Arya Amini, Kristin Bibee, Jeremy S. Bordeaux, Pei-Ling Chen, Carlo M Contreras, D. Dimaio, J. M. Donigan, J. Farma, Karthik Ghosh, Kelly Harms, Alan L Ho, J. N. Lukens, Lawrence Mark, Theresa Medina, K. Nehal, Paul Nghiem, K. Olino, Soo Park, Tejesh Patel, Igor Puzanov, Jason Rich, A. Sekulic, Ashok R. Shaha, Divya Srivastava, Valencia Thomas, Courtney Tomblinson, Puja S Venkat, Y. G. Xu, Siegrid Yu, Mehran Yusuf, Beth McCullough, and Sara Espinosa. Basal cell skin cancer, version 2.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 21 11:1181-1203, Nov 2023. URL: https://doi.org/10.6004/jnccn.2023.0056, doi:10.6004/jnccn.2023.0056. This article has 133 citations.

26. (kauvar2015consensusfornonmelanoma pages 7-8): Arielle N. B. Kauvar, Terrence Cronin, Randall Roenigk, George Hruza, and Richard Bennett. Consensus for nonmelanoma skin cancer treatment: basal cell carcinoma, including a cost analysis of treatment methods. Dermatologic Surgery, 41:550–571, May 2015. URL: https://doi.org/10.1097/dss.0000000000000296, doi:10.1097/dss.0000000000000296. This article has 219 citations and is from a peer-reviewed journal.

27. (dessinioti2023immunotherapyandits pages 4-6): Clio Dessinioti and Alexander Stratigos. Immunotherapy and its timing in advanced basal cell carcinoma treatment. Dermatology Practical &amp; Conceptual, pages e2023252, Oct 2023. URL: https://doi.org/10.5826/dpc.1304a252, doi:10.5826/dpc.1304a252. This article has 16 citations.

28. (mainville2022effectofnicotinamide pages 1-2): Laurence Mainville, Anne-Sophie Smilga, and Paul R. Fortin. Effect of nicotinamide in skin cancer and actinic keratoses chemoprophylaxis, and adverse effects related to nicotinamide: a systematic review and meta-analysis. Journal of Cutaneous Medicine and Surgery, 26:297-308, Feb 2022. URL: https://doi.org/10.1177/12034754221078201, doi:10.1177/12034754221078201. This article has 50 citations and is from a peer-reviewed journal.

29. (tosti2023theroleof pages 1-2): Giulio Tosti, Francesca Pepe, Patrizia Gnagnarella, Flavia Silvestri, Aurora Gaeta, Paola Queirolo, and Sara Gandini. The role of nicotinamide as chemo-preventive agent in nmscs: a systematic review and meta-analysis. Nutrients, 16:100, Dec 2023. URL: https://doi.org/10.3390/nu16010100, doi:10.3390/nu16010100. This article has 22 citations.

30. (vallini2023signalingpathwaysand pages 13-14): Giulia Vallini, Laura Calabrese, Costanza Canino, Emanuele Trovato, Stefano Gentileschi, Pietro Rubegni, and Linda Tognetti. Signaling pathways and therapeutic strategies in advanced basal cell carcinoma. Cells, 12:2534, Oct 2023. URL: https://doi.org/10.3390/cells12212534, doi:10.3390/cells12212534. This article has 13 citations.

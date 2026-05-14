---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T04:19:51.127115'
end_time: '2026-05-10T04:45:05.153736'
duration_seconds: 1514.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Metastatic Prostate Cancer
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
- **Disease Name:** Metastatic Prostate Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Prostate Cancer** covering all of the
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
- **Disease Name:** Metastatic Prostate Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Metastatic Prostate Cancer** covering all of the
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


## Comprehensive Research Report: Metastatic Prostate Cancer

### Target Disease
- **Disease name:** Metastatic prostate cancer (mPC)
- **Category:** Malignant neoplasm; metastatic solid tumor; genitourinary cancer
- **MONDO ID:** Not available from retrieved sources in this run (would typically be obtained from MONDO/OLS).

---

## 1. Disease Information

### Overview / definition
Metastatic prostate cancer is prostate adenocarcinoma that has disseminated beyond the prostate and regional tissues to distant sites (AJCC **M1** disease), most commonly bone and lymph nodes. Clinically, metastatic disease is often subclassified by response to androgen deprivation therapy (ADT) into:
- **Metastatic hormone-sensitive prostate cancer (mHSPC)**: metastatic disease that has not yet developed resistance to castration-level testosterone.
- **Metastatic castration-resistant prostate cancer (mCRPC)**: metastatic disease with progression despite ongoing ADT and castrate testosterone levels.

A recent review describes the mCRPC state as progression despite castrate testosterone levels (often defined as <50 ng/dL) and diagnosis by biochemical (rising PSA) and/or radiologic progression while on ADT (cicchetti2025therapeuticadvancesin pages 1-2).

### Key identifiers (available in retrieved sources)
- **ICD-10 (primary site):** C61 (Prostate) (inferred as standard coding used in population registries summarized in CA Cancer J Clin; ICD-O site C61 used for incidence statistics) (kratzer2025prostatecancerstatistics pages 2-3).
- **MeSH / OMIM / Orphanet / MONDO:** Not available in retrieved sources in this run.

### Synonyms / alternative names
- Metastatic prostate cancer (mPC)
- Metastatic hormone-sensitive prostate cancer (mHSPC); metastatic castration-sensitive prostate cancer (mCSPC)
- Metastatic castration-resistant prostate cancer (mCRPC)

### Evidence sources
The evidence used here comes from **aggregated disease-level resources** (EAU guideline; CA Cancer J Clin population statistics), **clinical trials and regulatory summaries**, and **real-world claims/registry studies**, rather than single-patient EHR narratives (tilki2024eaueanmestroesurisupsiogguidelineson pages 1-3, kratzer2025prostatecancerstatistics pages 1-2, raval2025realworldevidenceof pages 1-2).

**EAU 2024 guideline resource URL:** https://doi.org/10.1016/j.eururo.2024.04.010 (published online 2024-08) (tilki2024eaueanmestroesurisupsiogguidelineson pages 1-3).

---

## 2. Etiology

### Disease causal factors (mechanistic)
Metastatic progression and castration resistance are strongly driven by androgen receptor (AR) biology and clonal evolution under hormonal selection pressure. A contemporary mCRPC review states: “**The androgen signalling pathway plays a pivotal role in the development of castration resistance**” (kulasegaran2024metastaticcastrationresistantprostate pages 3-5). Mechanisms of AR-driven resistance include alterations such as AR pathway amplification/activation and adaptation to low androgen environments (tisseverasinghe2023advancesinparp pages 2-4).

Genomically, mCRPC frequently harbors tumor suppressor and pathway alterations. One review reports “**40%–60% of mCRPC cases exhibit aberrations in the AR ... tumour protein p53 and PTEN genes**” and that “**Approximately 20% of mCRPC patients harbour abnormalities that affect DNA repair genes**” (kulasegaran2024metastaticcastrationresistantprostate pages 3-5).

### Risk factors (host/demographic; population level)
In the U.S., prostate cancer incidence and mortality show strong demographic disparities that influence metastatic burden. A 2025 CA Cancer J Clin statistics report notes that Black men have **double the prostate cancer mortality** and **67% higher incidence** compared with White men (kratzer2025prostatecancerstatistics pages 1-2).

**Note:** Specific lifestyle/environmental risk factors (diet, smoking, occupational exposures) were not retrieved in the present corpus and therefore are not summarized here.

### Protective factors / gene–environment interactions
Not available from retrieved sources in this run.

---

## 3. Phenotypes

### Common clinical phenotypes in metastatic disease
Metastatic prostate cancer phenotypes are driven by metastatic site(s) and systemic tumor burden. Key, commonly reported manifestations include:
- **Bone metastasis–related pain** (symptom; QoL impact significant; often drives opioid use and palliative radiotherapy).
- **Skeletal-related events (SREs)** such as pathological fracture, spinal cord compression, need for bone radiation/surgery.
- **Laboratory marker:** rising **PSA** in many patients, though lineage plasticity can produce low-PSA aggressive variants (not fully quantified in retrieved sources).

The EAU guideline describes SRE endpoints explicitly (pathological fracture, bone radiation/surgery, spinal cord compression) in the denosumab vs zoledronic acid comparison (tilki2024eaueanmestroesurisupsiogguidelineson pages 14-15).

### Suggested HPO terms (non-exhaustive; for knowledge base mapping)
Because HPO IDs were not provided in retrieved sources, the following are suggested standard terms (IDs should be verified against HPO):
- Bone pain; back pain
- Pathologic fracture
- Spinal cord compression
- Elevated prostate-specific antigen
- Anemia (treatment-related, e.g., PARP inhibitor myelosuppression)

### Quality of life (QoL)
The mCRPC review emphasizes that treatment goals should include symptom relief and QoL preservation, noting focus on “**cancer-related symptoms such as pain**” (kulasegaran2024metastaticcastrationresistantprostate pages 1-3).

---

## 4. Genetic / Molecular Information

### Key genes and pathways (somatic and germline)
**Homologous recombination repair (HRR) / DNA damage repair (DDR)** alterations are clinically actionable in advanced disease. A 2024 mCRPC review states that “**20%–25% [of mCRPC] harbouring somatic or germline alternations in DNA repair genes involved in homologous recombination**,” listing common genes “**BRCA2, CHEK2, ATM and BRCA1**” (kulasegaran2024metastaticcastrationresistantprostate pages 3-5).

A 2023 precision oncology review similarly highlights HRR alterations in metastatic prostate cancer, with frequently altered genes including **BRCA2, ATM, CDK12, CHEK2** (gillette2023managementofadvanced pages 5-6).

### Pathogenic variants and variant classification
Specific variant-level nomenclature (e.g., BRCA2 c.XXXXdel) and allele frequencies from gnomAD/ClinVar were not available in retrieved sources in this run.

### Biomarkers informing therapy
#### HRR gene alterations → PARP inhibitor combinations
The FDA approval summary specifies that HRRm status in TALAPRO-2 was prospectively determined with a **12-gene NGS panel**: “ATM, ATR, BRCA1, BRCA2, CDK12, CHEK2, FANCA, MLH1, MRE11A, NBN, PALB2, and RAD51C” (heiss2024usfoodand pages 2-4).

#### MSI-H/dMMR and TMB-H → immune checkpoint blockade eligibility
A large genomic/clinical study defined:
- “**MSI-H/dMMR prostate cancer was defined as MSIsensor score ≥10 or MSIsensor score ≥3 and <10 with a deleterious MMR alteration**”
- “**TMB-H was defined as ≥10 mutations/megabase**” (lenis2024microsatelliteinstabilitytumor pages 1-3).

---

## 5. Environmental Information
Not available from retrieved sources in this run.

---

## 6. Mechanism / Pathophysiology

### Core molecular mechanism chain (high level)
1. **Androgen signaling dependence** in prostate epithelial tumor cells → response to ADT/AR pathway inhibition.
2. Under treatment pressure, tumors evolve **AR pathway reactivation** or shift to alternative survival programs, driving **castration resistance** (kulasegaran2024metastaticcastrationresistantprostate pages 3-5, tisseverasinghe2023advancesinparp pages 2-4).
3. Subsets acquire/harbor **DDR/HRR defects**; these increase genomic instability and create vulnerabilities to **PARP inhibition** via synthetic lethality (kulasegaran2024metastaticcastrationresistantprostate pages 3-5, tisseverasinghe2023advancesinparp pages 2-4).
4. A small subset develops **MSI-H/dMMR**, increasing neoantigen burden and enabling clinically meaningful responses to immune checkpoint blockade (lenis2024microsatelliteinstabilitytumor pages 1-3).
5. **Bone metastasis** causes osteoclast/osteoblast dysregulation; SRE prevention targets osteoclast signaling (RANKL inhibition) and bone resorption (bisphosphonates) (tilki2024eaueanmestroesurisupsiogguidelineson pages 14-15).

### Immune involvement / immunotherapy biomarker data
In a cohort of 2,257 prostate cancer patients with tumor sequencing, prevalence of immunotherapy-relevant genomic subgroups was:
- **MSI-H/dMMR:** 63/2,257 (2.8%)
- **TMB-H/MSS:** 33/2,257 (1.5%) (lenis2024microsatelliteinstabilitytumor pages 1-3)

Among immune checkpoint blockade–treated patients:
- MSI-H/dMMR: “**45% ... had a RECIST response and 65% had a PSA50 response**”
- TMB-H/MSS: “**No ... had a RECIST response and 50% had a PSA50 response**” (lenis2024microsatelliteinstabilitytumor pages 1-3).

### Suggested GO biological process terms (examples)
- Androgen receptor signaling pathway
- DNA repair; homologous recombination
- Double-strand break repair
- Osteoclast differentiation; bone remodeling

### Suggested Cell Ontology (CL) cell types (examples)
- Prostate epithelial cell / luminal epithelial cell (tumor origin)
- Osteoclast, osteoblast (bone metastasis microenvironment)
- CD8+ T cell (immunotherapy response context)

---

## 7. Anatomical Structures Affected

### Organ/tissue level
- **Primary organ:** prostate gland
- **Common metastatic sites:** bone, lymph nodes; also visceral sites in advanced disease.

### Suggested UBERON terms (examples; IDs not provided in retrieved sources)
- prostate gland
- bone tissue (skeletal system)
- lymph node

### Subcellular
- Nucleus (AR transcription factor function)
- DNA repair machinery compartments (nuclear)

---

## 8. Temporal Development

### Typical onset and course
Prostate cancer is predominantly adult/older-adult onset, with metastatic presentation either de novo or after progression from localized disease.

A real-world cohort defined **de novo mHSPC** operationally as first metastasis within 60 days of first prostate cancer diagnosis (raval2025realworldevidenceof pages 2-4).

### Progression
The transition from mHSPC to mCRPC is clinically defined by progression while maintaining castrate testosterone and ongoing ADT; detailed staging frameworks were not extracted from retrieved sources in this run.

---

## 9. Inheritance and Population

### Epidemiology (recent statistics; U.S.)
A 2025 CA Cancer J Clin report found that overall U.S. prostate cancer incidence trends reversed from “**a decline of 6.4% per year during 2007 through 2014 to an increase of 3.0% annually during 2014 through 2021**” and that “**distant-stage disease has increased by 2.6% annually**” in men <55, and by **6.0%** (55–69) and **6.2%** (≥70) (kratzer2025prostatecancerstatistics pages 1-2).

**Racial disparities:** Black men have “**double the prostate cancer mortality, with 67% higher incidence**” vs White men (kratzer2025prostatecancerstatistics pages 1-2). Distant-stage 5-year survival “**ranges from 36% in Black men to 43% for AAPI men**” (kratzer2025prostatecancerstatistics pages 4-4).

### Inheritance
Germline HRR alterations occur in a minority of metastatic patients (e.g., reported germline HRR prevalence ~11.8% in one summarized dataset) (gillette2023managementofadvanced pages 6-7). Specific Mendelian inheritance patterns are not directly applicable to metastatic status (which is a disease stage), but inherited predisposition variants (e.g., BRCA2) increase risk of aggressive disease.

---

## 10. Diagnostics

### Core clinical tests (metastatic setting)
- **PSA** monitoring and clinical assessment
- **Imaging for staging and response**: historically CT/MRI plus bone scan in pivotal trials; PSMA PET/CT increasingly used.

EAU guidance notes that trial evidence defining M1 disease used CT/MRI plus bone scintigraphy and that the impact of newer imaging such as PSMA PET/CT on outcomes has not yet been tested in randomized trials (tilki2024eaueanmestroesurisupsiogguidelineson pages 7-8).

For biochemical recurrence post-prostatectomy, the EAU guideline table recommends: “**Perform PSMA PET/CT if the PSA level is >0.2 ng/ml and if the results will influence subsequent treatment decisions**” (strength rating weak) (tilki2024eaueanmestroesurisupsiogguidelineson pages 4-5).

### Molecular diagnostics / tumor profiling
For mCRPC and advanced disease, molecular testing is used to identify actionable subgroups:
- **HRR mutations** to guide PARP inhibitor use (heiss2024usfoodand pages 2-4, heiss2024usfoodand pages 1-2).
- **MSI-H/dMMR / TMB-H** for pembrolizumab eligibility (lenis2024microsatelliteinstabilitytumor pages 1-3).

---

## 11. Outcome / Prognosis

### Survival trends at population level
Distant-stage prostate cancer survival has improved over time; the CA Cancer J Clin report indicates distant-stage survival improved “from 55% in the middle 2000s to 66% in 2019–2020” (kratzer2025prostatecancerstatistics pages 4-4).

### Prognostic biomarkers (selected)
- HRR status is prognostic and predictive for PARP inhibitor response; BRCA2 alterations are repeatedly associated with higher PARP inhibitor benefit relative to other HRR genes (heiss2024usfoodand pages 1-2, kulasegaran2024metastaticcastrationresistantprostate pages 3-5).
- MSI-H/dMMR predicts response to immune checkpoint blockade; objective responses in ~45% of treated MSI-H/dMMR patients in one cohort (lenis2024microsatelliteinstabilitytumor pages 1-3).

---

## 12. Treatment

### 12.1 First-line systemic therapy for mHSPC (guidelines; real-world implementation)
The EAU 2024 guideline recommends against ADT monotherapy as initial therapy for de novo M1 patients who are eligible for combination therapy and have sufficient life expectancy (strong) (tilki2024eaueanmestroesurisupsiogguidelineson pages 6-7). It strongly recommends ADT combined with AR pathway inhibitor options (abiraterone acetate plus prednisone, apalutamide, or enzalutamide) for fit patients (tilki2024eaueanmestroesurisupsiogguidelineson pages 7-8).

Triplet therapy evidence is incorporated: in the PEACE-1 subgroup, adding abiraterone to ADT+docetaxel improved rPFS (HR 0.50) and OS (HR 0.75) (tilki2024eaueanmestroesurisupsiogguidelineson pages 7-8).

**Real-world uptake (US 2017–2023):** In a claims-based cohort of 10,717 individuals, ADT+ARPI increased from 13% to 47%, and triplet therapy (ADT+ARPI+docetaxel) increased from 0.8% to 15%, while ADT alone declined from 74% to 36% (raval2025realworldevidenceof pages 1-2).

**Guideline recommendation table (visual evidence):** EAU 2024 Table 6 summarizes first-line mHSPC recommendations with strength ratings (tilki2024eaueanmestroesurisupsiogguidelineson media 3226c7f4).

### 12.2 mCRPC standard therapies (selected clinical trial outcomes)
Examples of established systemic therapies and outcomes summarized in a 2024 mCRPC review include:
- **Docetaxel (TAX-327):** median OS 19.2 vs 16.3 months (p < 0.004) (kulasegaran2024metastaticcastrationresistantprostate pages 1-3).
- **Cabazitaxel (TROPIC):** OS 15.1 vs 12.7 months; HR 0.7 (p ≤ 0.0001) (kulasegaran2024metastaticcastrationresistantprostate pages 1-3, kulasegaran2024metastaticcastrationresistantprostate pages 3-5).
- **Enzalutamide:** AFFIRM OS 18.4 vs 13.6 months (HR 0.63); PREVAIL rPFS at 12 months 65% vs 14% (HR 0.19) and OS 32.4 vs 30.2 months (HR 0.7) (kulasegaran2024metastaticcastrationresistantprostate pages 3-5).
- **Abiraterone:** COU-AA-301 OS 14.8 vs 10.9 months (HR 0.65); COU-AA-302 OS 34.7 vs 30.3 months (HR 0.81) (kulasegaran2024metastaticcastrationresistantprostate pages 3-5).

### 12.3 Biomarker-driven therapy (2023–2024 developments)
#### HRR-mutated mCRPC: talazoparib + enzalutamide (FDA-approved)
The FDA approval summary states: “**The US Food and Drug Administration (FDA) approved talazoparib with enzalutamide for first-line treatment of patients with homologous recombination repair (HRR) gene-mutated metastatic castration-resistant prostate cancer (mCRPC).**” (heiss2024usfoodand pages 1-2). Efficacy in the combined HRRm population: rPFS HR **0.45** (95% CI 0.33–0.61; P < .0001); BRCA-mutated subgroup rPFS HR **0.20** (95% CI 0.11–0.36) (heiss2024usfoodand pages 1-2).

Safety is dominated by myelosuppression: decreased hemoglobin any-grade 79%; grade ≥3 anemia 45%; and RBC transfusion in 39% (heiss2024usfoodand pages 6-8).

#### MSI-H/dMMR metastatic prostate cancer: pembrolizumab (tumor-agnostic)
In a large institutional cohort, MSI-H/dMMR prevalence was 2.8% and responses to ICB were substantial: 45% RECIST response and 65% PSA50 response among treated MSI-H/dMMR patients (lenis2024microsatelliteinstabilitytumor pages 1-3).

### 12.4 Bone-targeted agents to prevent skeletal-related events (SREs)
EAU guideline evidence summary:
- **Zoledronic acid (4 mg):** fewer SREs vs placebo (33% vs 44%; p = 0.021) (tilki2024eaueanmestroesurisupsiogguidelineson pages 14-15).
- **Denosumab vs zoledronic acid:** longer time to first on-study SRE (20.7 vs 17.1 months; HR 0.82; p = 0.008) (tilki2024eaueanmestroesurisupsiogguidelineson pages 14-15).

Key toxicities include osteonecrosis of the jaw (reported 8.2% in mCRPC) and severe hypocalcemia (8% with denosumab vs 5% with zoledronic acid), motivating dental exam prior to therapy and calcium/vitamin D supplementation (tilki2024eaueanmestroesurisupsiogguidelineson pages 14-15).

### Suggested MAXO terms (examples)
- Androgen deprivation therapy
- Androgen receptor pathway inhibitor therapy
- Chemotherapy (taxane)
- Radiotherapy to primary tumor
- PARP inhibitor therapy
- Immune checkpoint inhibitor therapy
- Bisphosphonate therapy
- RANKL inhibitor therapy

---

## 13. Prevention

### Primary prevention
Not addressed in retrieved sources.

### Secondary prevention / screening
Population screening and its association with stage at diagnosis is addressed indirectly via incidence trend analyses. A large multistate cohort found that higher county-level PSA screening prevalence prior to diagnosis was associated with lower odds of advanced stage and lower mortality (kratzer2025prostatecancerstatistics pages 5-6).

**Note:** Specific USPSTF recommendations were not retrieved in full text in this run.

---

## 14. Other Species / Natural Disease
Not available from retrieved sources in this run.

---

## 15. Model Organisms
Not available from retrieved sources in this run.

---

## Recent Developments (2023–2024 prioritized) and Real-World Implementations (summary)

Key 2023–2024 developments and implementation signals include:
- **EAU 2024 guideline updates** integrating ARPI intensification and selective triplet therapy in mHSPC (tilki2024eaueanmestroesurisupsiogguidelineson pages 6-7, tilki2024eaueanmestroesurisupsiogguidelineson pages 7-8).
- **Biomarker-driven first-line mCRPC approval** of talazoparib + enzalutamide for HRR gene–mutated disease, with strongest rPFS benefit in BRCA-mutated subgroup (heiss2024usfoodand pages 1-2).
- **Clarified immunotherapy biomarker performance**: MSI-H/dMMR vs TMB-H/MSS distinction, with durable objective responses concentrated in MSI-H/dMMR (lenis2024microsatelliteinstabilitytumor pages 1-3).
- **Real-world adoption**: by 2023, ADT+ARPI (47%) and ADT+ARPI+docetaxel (15%) increased substantially, though 36% still received ADT alone (raval2025realworldevidenceof pages 1-2).

---

## Evidence Map (recent, high-value sources)

| Topic/Section | Key finding (with numeric data) | Source (first author, year, journal) | Publication date | PMID | URL/DOI |
|---|---|---|---|---|---|
| Definitions/guideline framework for relapsing & metastatic disease | 2024 EAU Part II update summarizes evidence reviewed from 2020-2023; for de novo M1 disease, ADT monotherapy should not be offered if patients are suitable for combination therapy; recommends ADT + ARPI for fit patients and ADT + prostate RT for de novo low-volume disease by CHAARTED criteria; PEACE-1 subgroup cited with rPFS HR 0.50 and OS HR 0.75 for triplet therapy context (tilki2024eaueanmestroesurisupsiogguidelineson pages 1-3, tilki2024eaueanmestroesurisupsiogguidelineson pages 7-8, tilki2024eaueanmestroesurisupsiogguidelineson pages 6-7) | Tilki, 2024, *European Urology* | 2024-08 |  | http://hdl.handle.net/1874/455097 ; https://doi.org/10.1016/j.eururo.2024.04.010 |
| Precision therapy / FDA approval | FDA approved talazoparib + enzalutamide on 2023-06-20 for adult patients with HRR gene-mutated mCRPC; TALAPRO-2 showed rPFS HR 0.45 (95% CI 0.33-0.61) in HRRm population and BRCA subgroup HR 0.20 (95% CI 0.11-0.36); grade ≥3 anemia 45%, neutropenia 18%, thrombocytopenia 8%; RBC transfusion in 39% (heiss2024usfoodand pages 6-8, heiss2024usfoodand pages 2-4, heiss2024usfoodand pages 1-2) | Heiss, 2024, *Journal of Clinical Oncology* | 2024-05 |  | https://doi.org/10.1200/jco.23.02182 |
| Phase 3 HRR-deficient mCRPC trial | In combined HRR-deficient population (N=399), talazoparib + enzalutamide improved rPFS: median not reached vs 13.8 months; HR 0.45 (95% CI 0.33-0.61; P<0.0001); OS immature but favored combination, HR 0.69 (95% CI 0.46-1.03); common AEs were anemia, fatigue, neutropenia (fizazi2024firstlinetalazoparibwith pages 2-3, fizazi2024firstlinetalazoparibwith pages 1-2) | Fizazi, 2024, *Nature Medicine* | 2024-12 |  | https://doi.org/10.1038/s41591-023-02704-x |
| Immunotherapy biomarkers (MSI/TMB) | Among 2,257 patients, MSI-H/dMMR prevalence was 2.8% and TMB-H/MSS 1.5%; definitions: MSI-H/dMMR = MSIsensor ≥10 or 3-10 with deleterious MMR alteration; TMB-H = ≥10 mut/Mb; with ICB, MSI-H/dMMR had 45% RECIST response and 65% PSA50 response, versus 0% RECIST and 50% PSA50 for TMB-H/MSS (lenis2024microsatelliteinstabilitytumor pages 1-3, lenis2024microsatelliteinstabilitytumor pages 3-5) | Lenis, 2024, *Clinical Cancer Research* | 2024-07 |  | https://doi.org/10.1158/1078-0432.ccr-23-3403 |
| Epidemiology / incidence trends / disparities | US prostate cancer incidence reversed from -6.4%/year (2007-2014) to +3.0%/year (2014-2021); distant-stage disease increased annually by 2.6% (<55 y), 6.0% (55-69 y), and 6.2% (≥70 y); Black men had double prostate cancer mortality and 67% higher incidence than White men (kratzer2025prostatecancerstatistics pages 1-2, kratzer2025prostatecancerstatistics pages 3-4) | Kratzer, 2025, *CA: A Cancer Journal for Clinicians* | 2025-09 |  | https://doi.org/10.3322/caac.70028 |
| Real-world mHSPC treatment adoption | In 10,717 US patients with mHSPC (median age 65), 62% had de novo disease; from 2017 to 2023, ADT+ARPI increased from 13% to 47%, ADT+ARPI+docetaxel from 0.8% to 15%, ADT+docetaxel declined from 12% to 3%, and ADT alone from 74% to 36% (raval2025realworldevidenceof pages 1-2, raval2025realworldevidenceof pages 2-4) | Raval, 2025, *JCO Oncology Practice* | 2025-02 |  | https://doi.org/10.1200/op-24-00690 |
| mCRPC treatment landscape / genomics | mCRPC remains incurable but treatment sequencing is increasingly biomarker-informed; docetaxel TAX327 median OS 19.2 vs 16.3 months, cabazitaxel TROPIC OS 15.1 vs 12.7 months (HR 0.7); 20%-25% of mCRPC harbor somatic/germline DNA repair (HRR) alterations, and 40%-60% show AR/TP53/PTEN aberrations (kulasegaran2024metastaticcastrationresistantprostate pages 3-5, kulasegaran2024metastaticcastrationresistantprostate pages 1-3) | Kulasegaran, 2024, *Current Treatment Options in Oncology* | 2024-06 |  | https://doi.org/10.1007/s11864-024-01215-2 |
| Systemic therapy evidence synthesis / sequencing | Living systematic review included 143 randomized trials and 17,523 patients; reported median mCRPC survival 25.6 months; PARPi+ARPI favored for BRCA+ first-line disease, PARPi monotherapy after prior ARPI in BRCA+ disease; for non-HRR-altered disease, active options include abiraterone, enzalutamide, cabazitaxel, docetaxel, and Lu177 if PSMA-positive (naqvi2025systemictreatmentoptions pages 1-5, naqvi2025systemictreatmentoptions pages 18-21) | Naqvi, 2025, *medRxiv* | 2025-04 |  | https://doi.org/10.1101/2025.04.15.25325837 |


*Table: This table summarizes major 2024-2025 evidence sources used for metastatic prostate cancer, spanning guidelines, biomarker-driven therapy, epidemiology, and real-world implementation. It highlights key quantitative findings and links them to authoritative publications for rapid reference.*

---

## Visual Evidence (Guideline Recommendation Table)

EAU 2024 Table 6 (cropped image) includes first-line mHSPC treatment recommendations with strength ratings (tilki2024eaueanmestroesurisupsiogguidelineson media 3226c7f4).

---

## Limitations / data not captured in this run
- Formal ontology identifiers (MONDO, MeSH IDs) were not retrieved.
- Detailed environmental/lifestyle risk factor meta-analyses were not retrieved.
- Model organism and veterinary disease information were not retrieved.
- PMIDs were not provided in the retrieved text snippets; therefore, PMID fields are left blank unless present in-source.


References

1. (cicchetti2025therapeuticadvancesin pages 1-2): Rossella Cicchetti, Martina Basconi, Giulio Litterio, Angelo Orsini, Marco Mascitti, Alessio Digiacomo, Gaetano Salzano, Octavian Sabin Tătaru, Matteo Ferro, Carlo Giulioni, Angelo Cafarelli, Luigi Schips, and Michele Marchioni. Therapeutic advances in metastatic prostate cancer: a journey from standard of care to new emerging treatment. International Journal of Molecular Sciences, 26:11665, Dec 2025. URL: https://doi.org/10.3390/ijms262311665, doi:10.3390/ijms262311665. This article has 5 citations.

2. (kratzer2025prostatecancerstatistics pages 2-3): Tyler B. Kratzer, Natalia Mazzitelli, Jessica Star, William L. Dahut, Ahmedin Jemal, and Rebecca L. Siegel. Prostate cancer statistics, 2025. CA: A Cancer Journal for Clinicians, 75:485-497, Sep 2025. URL: https://doi.org/10.3322/caac.70028, doi:10.3322/caac.70028. This article has 103 citations and is from a domain leading peer-reviewed journal.

3. (tilki2024eaueanmestroesurisupsiogguidelineson pages 1-3): D Tilki, RCN van den Bergh, and E Briers. Eau-eanm-estro-esur-isup-siog guidelines on prostate cancer. part ii—. Unknown journal, 2024.

4. (kratzer2025prostatecancerstatistics pages 1-2): Tyler B. Kratzer, Natalia Mazzitelli, Jessica Star, William L. Dahut, Ahmedin Jemal, and Rebecca L. Siegel. Prostate cancer statistics, 2025. CA: A Cancer Journal for Clinicians, 75:485-497, Sep 2025. URL: https://doi.org/10.3322/caac.70028, doi:10.3322/caac.70028. This article has 103 citations and is from a domain leading peer-reviewed journal.

5. (raval2025realworldevidenceof pages 1-2): Amit D. Raval, Orsolya Lunacsek, Matthew J. Korn, Natasha Littleton, Niculae Constantinovici, and Daniel J. George. Real-world evidence of combination therapy use in metastatic hormone-sensitive prostate cancer in the united states from 2017 to 2023. JCO Oncology Practice, 21:1174-1184, Feb 2025. URL: https://doi.org/10.1200/op-24-00690, doi:10.1200/op-24-00690. This article has 10 citations and is from a peer-reviewed journal.

6. (kulasegaran2024metastaticcastrationresistantprostate pages 3-5): Tivya Kulasegaran and Niara Oliveira. Metastatic castration-resistant prostate cancer: advances in treatment and symptom management. Current Treatment Options in Oncology, 25:914-931, Jun 2024. URL: https://doi.org/10.1007/s11864-024-01215-2, doi:10.1007/s11864-024-01215-2. This article has 75 citations and is from a peer-reviewed journal.

7. (tisseverasinghe2023advancesinparp pages 2-4): Steven Tisseverasinghe, Boris Bahoric, Maurice Anidjar, Stephan Probst, and Tamim Niazi. Advances in parp inhibitors for prostate cancer. Cancers, 15:1849, Mar 2023. URL: https://doi.org/10.3390/cancers15061849, doi:10.3390/cancers15061849. This article has 29 citations.

8. (tilki2024eaueanmestroesurisupsiogguidelineson pages 14-15): D Tilki, RCN van den Bergh, and E Briers. Eau-eanm-estro-esur-isup-siog guidelines on prostate cancer. part ii—. Unknown journal, 2024.

9. (kulasegaran2024metastaticcastrationresistantprostate pages 1-3): Tivya Kulasegaran and Niara Oliveira. Metastatic castration-resistant prostate cancer: advances in treatment and symptom management. Current Treatment Options in Oncology, 25:914-931, Jun 2024. URL: https://doi.org/10.1007/s11864-024-01215-2, doi:10.1007/s11864-024-01215-2. This article has 75 citations and is from a peer-reviewed journal.

10. (gillette2023managementofadvanced pages 5-6): Claire M. Gillette, Gabriel A. Yette, Scott D. Cramer, and Laura S. Graham. Management of advanced prostate cancer in the precision oncology era. Cancers, 15:2552, Apr 2023. URL: https://doi.org/10.3390/cancers15092552, doi:10.3390/cancers15092552. This article has 20 citations.

11. (heiss2024usfoodand pages 2-4): Brian L. Heiss, Elaine Chang, Xin Gao, Tien Truong, Michael H. Brave, Erik Bloomquist, Ankit Shah, Salaheldin Hamed, Jeffrey Kraft, Haw-Jyh Chiu, Tiffany K. Ricks, Amy Tilley, William F. Pierce, Liuya Tang, Abdelrahmman Abukhdeir, Shyam Kalavar, Reena Philip, Shenghui Tang, Richard Pazdur, Laleh Amiri-Kordestani, Paul G. Kluetz, and Daniel L. Suzman. Us food and drug administration approval summary: talazoparib in combination with enzalutamide for treatment of patients with homologous recombination repair gene-mutated metastatic castration-resistant prostate cancer. Journal of Clinical Oncology, 42:1851-1860, May 2024. URL: https://doi.org/10.1200/jco.23.02182, doi:10.1200/jco.23.02182. This article has 30 citations and is from a highest quality peer-reviewed journal.

12. (lenis2024microsatelliteinstabilitytumor pages 1-3): Andrew T. Lenis, Vignesh Ravichandran, Samantha Brown, Syed M. Alam, Andrew Katims, Hong Truong, Peter A. Reisz, Samantha Vasselman, Barbara Nweji, Karen A. Autio, Michael J. Morris, Susan F. Slovin, Dana Rathkopf, Daniel Danila, Sungmin Woo, Hebert A. Vargas, Vincent P. Laudone, Behfar Ehdaie, Victor Reuter, Maria Arcila, Michael F. Berger, Agnes Viale, Howard I. Scher, Nikolaus Schultz, Anuradha Gopalan, Mark T.A. Donoghue, Irina Ostrovnaya, Konrad H. Stopsack, David B. Solit, and Wassim Abida. Microsatellite instability, tumor mutational burden, and response to immune checkpoint blockade in patients with prostate cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:3894-3903, Jul 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-3403, doi:10.1158/1078-0432.ccr-23-3403. This article has 62 citations.

13. (raval2025realworldevidenceof pages 2-4): Amit D. Raval, Orsolya Lunacsek, Matthew J. Korn, Natasha Littleton, Niculae Constantinovici, and Daniel J. George. Real-world evidence of combination therapy use in metastatic hormone-sensitive prostate cancer in the united states from 2017 to 2023. JCO Oncology Practice, 21:1174-1184, Feb 2025. URL: https://doi.org/10.1200/op-24-00690, doi:10.1200/op-24-00690. This article has 10 citations and is from a peer-reviewed journal.

14. (kratzer2025prostatecancerstatistics pages 4-4): Tyler B. Kratzer, Natalia Mazzitelli, Jessica Star, William L. Dahut, Ahmedin Jemal, and Rebecca L. Siegel. Prostate cancer statistics, 2025. CA: A Cancer Journal for Clinicians, 75:485-497, Sep 2025. URL: https://doi.org/10.3322/caac.70028, doi:10.3322/caac.70028. This article has 103 citations and is from a domain leading peer-reviewed journal.

15. (gillette2023managementofadvanced pages 6-7): Claire M. Gillette, Gabriel A. Yette, Scott D. Cramer, and Laura S. Graham. Management of advanced prostate cancer in the precision oncology era. Cancers, 15:2552, Apr 2023. URL: https://doi.org/10.3390/cancers15092552, doi:10.3390/cancers15092552. This article has 20 citations.

16. (tilki2024eaueanmestroesurisupsiogguidelineson pages 7-8): D Tilki, RCN van den Bergh, and E Briers. Eau-eanm-estro-esur-isup-siog guidelines on prostate cancer. part ii—. Unknown journal, 2024.

17. (tilki2024eaueanmestroesurisupsiogguidelineson pages 4-5): D Tilki, RCN van den Bergh, and E Briers. Eau-eanm-estro-esur-isup-siog guidelines on prostate cancer. part ii—. Unknown journal, 2024.

18. (heiss2024usfoodand pages 1-2): Brian L. Heiss, Elaine Chang, Xin Gao, Tien Truong, Michael H. Brave, Erik Bloomquist, Ankit Shah, Salaheldin Hamed, Jeffrey Kraft, Haw-Jyh Chiu, Tiffany K. Ricks, Amy Tilley, William F. Pierce, Liuya Tang, Abdelrahmman Abukhdeir, Shyam Kalavar, Reena Philip, Shenghui Tang, Richard Pazdur, Laleh Amiri-Kordestani, Paul G. Kluetz, and Daniel L. Suzman. Us food and drug administration approval summary: talazoparib in combination with enzalutamide for treatment of patients with homologous recombination repair gene-mutated metastatic castration-resistant prostate cancer. Journal of Clinical Oncology, 42:1851-1860, May 2024. URL: https://doi.org/10.1200/jco.23.02182, doi:10.1200/jco.23.02182. This article has 30 citations and is from a highest quality peer-reviewed journal.

19. (tilki2024eaueanmestroesurisupsiogguidelineson pages 6-7): D Tilki, RCN van den Bergh, and E Briers. Eau-eanm-estro-esur-isup-siog guidelines on prostate cancer. part ii—. Unknown journal, 2024.

20. (tilki2024eaueanmestroesurisupsiogguidelineson media 3226c7f4): D Tilki, RCN van den Bergh, and E Briers. Eau-eanm-estro-esur-isup-siog guidelines on prostate cancer. part ii—. Unknown journal, 2024.

21. (heiss2024usfoodand pages 6-8): Brian L. Heiss, Elaine Chang, Xin Gao, Tien Truong, Michael H. Brave, Erik Bloomquist, Ankit Shah, Salaheldin Hamed, Jeffrey Kraft, Haw-Jyh Chiu, Tiffany K. Ricks, Amy Tilley, William F. Pierce, Liuya Tang, Abdelrahmman Abukhdeir, Shyam Kalavar, Reena Philip, Shenghui Tang, Richard Pazdur, Laleh Amiri-Kordestani, Paul G. Kluetz, and Daniel L. Suzman. Us food and drug administration approval summary: talazoparib in combination with enzalutamide for treatment of patients with homologous recombination repair gene-mutated metastatic castration-resistant prostate cancer. Journal of Clinical Oncology, 42:1851-1860, May 2024. URL: https://doi.org/10.1200/jco.23.02182, doi:10.1200/jco.23.02182. This article has 30 citations and is from a highest quality peer-reviewed journal.

22. (kratzer2025prostatecancerstatistics pages 5-6): Tyler B. Kratzer, Natalia Mazzitelli, Jessica Star, William L. Dahut, Ahmedin Jemal, and Rebecca L. Siegel. Prostate cancer statistics, 2025. CA: A Cancer Journal for Clinicians, 75:485-497, Sep 2025. URL: https://doi.org/10.3322/caac.70028, doi:10.3322/caac.70028. This article has 103 citations and is from a domain leading peer-reviewed journal.

23. (fizazi2024firstlinetalazoparibwith pages 2-3): Karim Fizazi, Arun A. Azad, Nobuaki Matsubara, Joan Carles, Andre P. Fay, Ugo De Giorgi, Jae Young Joung, Peter C. C. Fong, Eric Voog, Robert J. Jones, Neal D. Shore, Curtis Dunshee, Stefanie Zschäbitz, Jan Oldenburg, Dingwei Ye, Xun Lin, Cynthia G. Healy, Nicola Di Santo, A. Douglas Laird, Fabian Zohren, and Neeraj Agarwal. First-line talazoparib with enzalutamide in hrr-deficient metastatic castration-resistant prostate cancer: the phase 3 talapro-2 trial. Nature Medicine, 30:257-264, Dec 2024. URL: https://doi.org/10.1038/s41591-023-02704-x, doi:10.1038/s41591-023-02704-x. This article has 157 citations and is from a highest quality peer-reviewed journal.

24. (fizazi2024firstlinetalazoparibwith pages 1-2): Karim Fizazi, Arun A. Azad, Nobuaki Matsubara, Joan Carles, Andre P. Fay, Ugo De Giorgi, Jae Young Joung, Peter C. C. Fong, Eric Voog, Robert J. Jones, Neal D. Shore, Curtis Dunshee, Stefanie Zschäbitz, Jan Oldenburg, Dingwei Ye, Xun Lin, Cynthia G. Healy, Nicola Di Santo, A. Douglas Laird, Fabian Zohren, and Neeraj Agarwal. First-line talazoparib with enzalutamide in hrr-deficient metastatic castration-resistant prostate cancer: the phase 3 talapro-2 trial. Nature Medicine, 30:257-264, Dec 2024. URL: https://doi.org/10.1038/s41591-023-02704-x, doi:10.1038/s41591-023-02704-x. This article has 157 citations and is from a highest quality peer-reviewed journal.

25. (lenis2024microsatelliteinstabilitytumor pages 3-5): Andrew T. Lenis, Vignesh Ravichandran, Samantha Brown, Syed M. Alam, Andrew Katims, Hong Truong, Peter A. Reisz, Samantha Vasselman, Barbara Nweji, Karen A. Autio, Michael J. Morris, Susan F. Slovin, Dana Rathkopf, Daniel Danila, Sungmin Woo, Hebert A. Vargas, Vincent P. Laudone, Behfar Ehdaie, Victor Reuter, Maria Arcila, Michael F. Berger, Agnes Viale, Howard I. Scher, Nikolaus Schultz, Anuradha Gopalan, Mark T.A. Donoghue, Irina Ostrovnaya, Konrad H. Stopsack, David B. Solit, and Wassim Abida. Microsatellite instability, tumor mutational burden, and response to immune checkpoint blockade in patients with prostate cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:3894-3903, Jul 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-3403, doi:10.1158/1078-0432.ccr-23-3403. This article has 62 citations.

26. (kratzer2025prostatecancerstatistics pages 3-4): Tyler B. Kratzer, Natalia Mazzitelli, Jessica Star, William L. Dahut, Ahmedin Jemal, and Rebecca L. Siegel. Prostate cancer statistics, 2025. CA: A Cancer Journal for Clinicians, 75:485-497, Sep 2025. URL: https://doi.org/10.3322/caac.70028, doi:10.3322/caac.70028. This article has 103 citations and is from a domain leading peer-reviewed journal.

27. (naqvi2025systemictreatmentoptions pages 1-5): Syed Arsalan Ahmed Naqvi, Muhammad Umair Anjum, Arifa Bibi, Muhammad Ali Khan, Kaneez Zahra Rubab Khakwani, Huan He, Manal Imran, Syeda Zainab Kazmi, Ammad Raina, Ewan K. Cobran, R. Bryan Rumble, Thomas K. Oliver, Neeraj Agarwal, Yousef Zakharia, Mary-Ellen Taplin, Oliver Sartor, Parminder Singh, Jacob J. Orme, Daniel S. Childs, Rahul A. Parikh, Rohan Garje, Mohammad Hassan Murad, Alan H. Bryce, and Irbaz Bin Riaz. Systemic treatment options for metastatic castration resistant prostate cancer: a living systematic review. medRxiv, Apr 2025. URL: https://doi.org/10.1101/2025.04.15.25325837, doi:10.1101/2025.04.15.25325837. This article has 5 citations.

28. (naqvi2025systemictreatmentoptions pages 18-21): Syed Arsalan Ahmed Naqvi, Muhammad Umair Anjum, Arifa Bibi, Muhammad Ali Khan, Kaneez Zahra Rubab Khakwani, Huan He, Manal Imran, Syeda Zainab Kazmi, Ammad Raina, Ewan K. Cobran, R. Bryan Rumble, Thomas K. Oliver, Neeraj Agarwal, Yousef Zakharia, Mary-Ellen Taplin, Oliver Sartor, Parminder Singh, Jacob J. Orme, Daniel S. Childs, Rahul A. Parikh, Rohan Garje, Mohammad Hassan Murad, Alan H. Bryce, and Irbaz Bin Riaz. Systemic treatment options for metastatic castration resistant prostate cancer: a living systematic review. medRxiv, Apr 2025. URL: https://doi.org/10.1101/2025.04.15.25325837, doi:10.1101/2025.04.15.25325837. This article has 5 citations.

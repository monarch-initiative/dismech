---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T22:53:42.629231'
end_time: '2026-04-05T23:01:33.820782'
duration_seconds: 471.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Synovial Sarcoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Synovial Sarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Synovial Sarcoma** covering all of the
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
- **Disease Name:** Synovial Sarcoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Synovial Sarcoma** covering all of the
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


## Synovial Sarcoma — Comprehensive Disease Characteristics Report (2023–2024 emphasis)

### Target Disease
- **Disease name:** Synovial sarcoma (SS; also “SyS”)
- **Category:** Rare malignant soft-tissue sarcoma (mesenchymal tumor of uncertain differentiation)
- **Key molecular identifier:** **t(X;18)(p11;q11)** with **SS18::SSX** fusion (historically “SYT-SSX”)
- **MONDO ID:** not found in gathered sources (not inferred)

---

## 1. Disease Information

### 1.1 Concise overview (definition)
Synovial sarcoma is a rare, aggressive soft-tissue sarcoma that typically arises in deep soft tissues (often of extremities) in adolescents and young adults, and is defined molecularly by the pathognomonic chromosomal translocation t(X;18) producing an **SS18::SSX** fusion oncoprotein. (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2)

A contemporary review summarizes SS as a WHO-recognized spindle-cell sarcoma that can show epithelial differentiation, emphasizing that the SS18::SSX fusion is a key diagnostic identifier. (lesovaya2024geneticandmolecular pages 1-2)

### 1.2 Synonyms and alternative names
Common synonyms/aliases and related terminology include:
- **Synovial sarcoma**, **SS**, **SyS** (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2)
- **SYT-SSX** (older name for SS18::SSX) (ferrari2023treatmentatrelapse pages 1-2, louati2025molecularprofilingof pages 12-14)
- **SS18-SSX** (hyphenated form; also written SS18::SSX) (baranov2020anovelss18ssx pages 1-2)

### 1.3 Key identifiers (ontology/coding)
The retrieved full-text evidence did **not** include explicit codes for **OMIM, Orphanet, ICD-10/ICD-11, MeSH, or MONDO**, so these are reported as **not found in gathered sources** rather than guessed.

### 1.4 Evidence source type
The information in this report is derived from:
- **Aggregated disease-level resources**: peer-reviewed reviews and registry/SEER-derived survival analyses (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2, bulski2025synovialsarcomaamong pages 6-7)
- **Primary molecular/pathology studies**: diagnostic antibody validation and mechanistic epigenetics work (baranov2020anovelss18ssx pages 1-2, benabdallah2023aberrantgeneactivation pages 1-2)

---

## 2. Etiology

### 2.1 Primary causal factors (genetic/mechanistic)
**Causal genetic event (somatic):** Synovial sarcoma is driven by the **t(X;18)** translocation producing an **SS18::SSX** fusion (most often SSX1 or SSX2, rarely SSX4). (ferrari2023treatmentatrelapse pages 1-2, baranov2020anovelss18ssx pages 1-2)

**Mechanistic causal model (current understanding):** The fusion oncoprotein acts primarily through **chromatin and transcriptional reprogramming**, notably through interactions with **BAF/SWI–SNF chromatin-remodeling complexes** and **Polycomb-associated chromatin**. (landuzzi2023innovativebreakthroughsfor pages 1-2, benabdallah2023aberrantgeneactivation pages 1-2)

Direct abstract support (primary study): Benabdallah et al. (Nature Structural & Molecular Biology; published online 2023-09-21) states: “**The SS18-SSX fusion drives oncogenic transformation in synovial sarcoma by bridging SS18, a member of the mSWI/SNF (BAF) complex, to Polycomb repressive complex 1 (PRC1) target genes.**” (benabdallah2023aberrantgeneactivation pages 1-2)

### 2.2 Risk factors
**Demographic associations (epidemiologic risk context):** SS is most frequently diagnosed in adolescents and young adults (e.g., 15–35 or 15–40 years) with a slight male predominance reported in reviews. (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2)

**Environmental/lifestyle/infectious risks:** No specific, well-supported environmental or infectious causal exposures were identified in the retrieved evidence.

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes (clinical features) + HPO suggestions

### 3.1 Typical clinical presentation
A large pediatric/AYA-focused review describes SS as typically presenting as a “**painless, gradually enlarging soft-tissue mass**,” most commonly in the extremities. (ferrari2023treatmentatrelapse pages 1-2)

Common primary sites:
- Extremities are most common (e.g., ~66% extremities in one review; ~80% extremities in another review). (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2)

Metastatic presentation:
- **<10%** present with metastases at diagnosis; lung is the most common metastatic site. (ferrari2023treatmentatrelapse pages 1-2)

### 3.2 Imaging phenotype (real-world diagnostic implementation)
A 2023 imaging review emphasizes that imaging can appear non-aggressive early (leading to misclassification), but characteristic MRI/CT patterns exist and may have prognostic value. Its summary tables report classic signs (e.g., “triple sign,” “bowl of grapes”) and note that calcification occurs in up to ~30% of cases; they also list imaging features associated with poor prognosis (e.g., hemorrhage/fluid–fluid levels, intercompartmental extension) and comparatively favorable prognosis (calcification). (cho2023synovialsarcomain media 393c0cbc, cho2023synovialsarcomain media 0aa1424d)

### 3.3 Histopathology phenotype
Histologic subtypes include monophasic and biphasic variants (and poorly differentiated in some series), and SS can show epithelial differentiation consistent with its biphasic morphology. (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2)

### 3.4 HPO term suggestions (non-exhaustive; map as appropriate)
- **Soft tissue mass** (HP:0001412)
- **Pain** (HP:0012531) — often absent early; may appear with growth/compression
- **Abnormality of the lung** / **Pulmonary metastasis** (phenotype mapping in oncology contexts)
- **Calcification** (HP:0004364) — imaging feature

(These are ontology suggestions; frequencies vary by cohort and were not systematically quantified in the retrieved evidence.)

### 3.5 Quality-of-life impact
Quality-of-life (QoL) impacts were not quantitatively extracted from the retrieved sources; however, SS is described as aggressive and management frequently requires multimodal therapy, which typically has substantial functional/QoL implications (surgery, radiotherapy, chemotherapy). (ferrari2023treatmentatrelapse pages 1-2, bulski2025synovialsarcomaamong pages 6-7)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and chromosomal abnormalities
- **Translocation:** t(X;18)(p11;q11)
- **Fusion gene:** **SS18::SSX** (SSX1/SSX2 most common; SSX4 rare)
- **Somatic vs germline:** Predominantly **somatic** driver event (inferred by disease biology; germline predisposition not supported by retrieved evidence)

The 2020 AJSP antibody-development paper explicitly frames SS as characterized by t(X;18) producing SS18-SSX rearrangements and variants, and notes diagnostic challenges due to overlap with other tumor types. (baranov2020anovelss18ssx pages 1-2)

### 4.2 Pathogenic variants (variant classes)
For SS, the key “variant” is the **structural rearrangement** generating the SS18::SSX fusion transcript (structural variant). (ferrari2023treatmentatrelapse pages 1-2, baranov2020anovelss18ssx pages 1-2)

### 4.3 Epigenetic information (key concept)
Multiple 2023–2024/2025 sources emphasize that SS18::SSX causes **genome-wide epigenetic deregulation** via altered chromatin complex targeting and stability, rather than a high burden of recurrent point mutations. (landuzzi2023innovativebreakthroughsfor pages 1-2, benabdallah2023aberrantgeneactivation pages 1-2)

### 4.4 Chromosomal abnormality and fusion protein biology (mechanism)
Benabdallah et al. (2023) provide a mechanistic model in which PRC1.1-mediated H2AK119ub1 supports SS18-SSX chromatin occupancy, and the SSX C-terminus stabilizes PRC1.1 to increase H2AK119ub1, creating high H2AK119ub1 levels in murine and human SS. (benabdallah2023aberrantgeneactivation pages 1-2)

---

## 5. Environmental Information
No specific environmental toxins, lifestyle exposures, or infectious triggers were identified in the retrieved evidence as established causal contributors.

---

## 6. Mechanism / Pathophysiology (with ontology suggestions)

### 6.1 Core upstream driver → downstream phenotypes (causal chain)
**Upstream initiating event:** Somatic chromosomal translocation **t(X;18)** → expression of **SS18::SSX** fusion oncoprotein. (ferrari2023treatmentatrelapse pages 1-2, baranov2020anovelss18ssx pages 1-2)

**Primary mechanistic class:** Chromatin remodeling / epigenetic reprogramming:
- SS18::SSX retargets transcription by interfacing with **mSWI/SNF (BAF)** and **Polycomb** biology (PRC1.1, H2AK119ub1). (benabdallah2023aberrantgeneactivation pages 1-2)

**Transcriptional/pathway consequences:** Multiple downstream pathways are implicated in proliferation, survival, and metastatic phenotypes:
- **Wnt/β-catenin** and **YAP/TAZ–TEAD** activation are described as common patterns and interacting programs in SS. (lesovaya2024geneticandmolecular pages 5-6)
- **Apoptosis evasion** may occur through kinase/transcriptional axes that increase anti-apoptotic gene expression (e.g., TYK2→STAT3→BCL2 axis described as a mechanism of apoptosis evasion, with SS18-SSX enhancing TYK2 transcription). (lesovaya2024geneticandmolecular pages 5-6)

### 6.2 PRC1.1 / H2AK119ub1 specificity (recent advance, 2023)
Benabdallah et al. (2023) emphasize that PRC1.1 is the main depositor of H2AK119ub1 required for SS18-SSX occupancy and that SSX-C increases PRC1.1 stability: “**Variant Polycomb repressive complex 1.1 (PRC1.1) acts as the main depositor of H2AK119ub1 and is therefore required for SS18-SSX occupancy.**” (benabdallah2023aberrantgeneactivation pages 1-2)

### 6.3 Immune microenvironment and cancer-testis antigens (clinical translational mechanism)
SS frequently expresses cancer-testis antigens such as **NY-ESO-1, MAGE-A4, and PRAME**, supporting engineered TCR-T strategies; at the same time, SS is often described as relatively “immune cold,” motivating combination or microenvironment-modifying strategies. (lesovaya2024geneticandmolecular pages 5-6, wang2025molecularandepigenetic pages 7-8)

### 6.4 Suggested GO / CL ontology mappings (examples; adapt to specific evidence items)
**GO Biological Process (examples):**
- Chromatin remodeling
- Histone ubiquitination (related to H2AK119ub1 biology)
- Transcriptional regulation
- Wnt signaling pathway
- Regulation of apoptotic process

**CL Cell types (examples):**
- Fibroblast (often discussed in cell-of-origin contexts for SS)
- Tumor-infiltrating lymphocyte / T cell (for immunotherapy contexts)
- Endothelial cell (angiogenesis/TKI contexts)

(These are ontology suggestions; the exact mappings depend on the evidence model used.)

---

## 7. Anatomical Structures Affected (with UBERON suggestions)

### 7.1 Organ/system level
Primary disease burden is in **deep soft tissues**, most frequently extremities. (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2)

Common metastatic site: **lung**. (ferrari2023treatmentatrelapse pages 1-2)

### 7.2 UBERON suggestions
- **Upper limb / lower limb** (extremity soft tissues)
- **Lung** (metastatic site)
- **Connective tissue**

---

## 8. Temporal Development

### 8.1 Onset and diagnostic delay
SS frequently affects adolescents/young adults and may have an indolent-appearing early course on imaging, contributing to diagnostic delay and misclassification as benign. (cho2023synovialsarcomain media 393c0cbc, cho2023synovialsarcomain media 0aa1424d)

### 8.2 Progression pattern
Localized disease can be controlled with multimodal therapy, but relapse/metastasis remains a major clinical problem; outcomes after relapse are described as poor and relapse treatment is often individualized. (ferrari2023treatmentatrelapse pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (incidence and distribution)
A 2023 review reports annual incidence of approximately **0.8 per million in children** and **1.4 per million in adults**. (ferrari2023treatmentatrelapse pages 1-2)

Age distribution: reviews describe peak diagnosis in adolescents and young adults (e.g., ~15–35 or 15–40). (lesovaya2024geneticandmolecular pages 1-2, cho2023synovialsarcomain media 393c0cbc)

### 9.2 Inheritance
SS is not presented as an inherited Mendelian disorder in the retrieved evidence; its hallmark event is a somatic fusion translocation. (baranov2020anovelss18ssx pages 1-2)

---

## 10. Diagnostics

### 10.1 Standard diagnostic workflow (current practice)
- Imaging (often MRI for extremity masses) informs suspicion and surgical planning; characteristic signs may support diagnosis and prognostic discussion. (cho2023synovialsarcomain media 393c0cbc, cho2023synovialsarcomain media 0aa1424d)
- Tissue biopsy with histopathology and IHC, plus molecular confirmation of **SS18 rearrangement or SS18::SSX** fusion transcript by **FISH/RT-PCR/targeted RNA sequencing**. (qiu2024primaryrenalsynovial pages 6-6, baranov2020anovelss18ssx pages 1-2)

### 10.2 Immunohistochemistry (IHC) markers — performance statistics
A key advance is fusion-specific IHC using SS18::SSX neoepitope antibodies.

Primary study evidence (Baranov et al., AJSP 2020; DOI: https://doi.org/10.1097/PAS.0000000000001447; publication month: 2020-03):
- The abstract reports “**strong diffuse nuclear staining in 95 of 100 (95%) SS cases, whereas none of the 300 control tumors showed any staining**” for the SS18-SSX fusion-specific antibody, and indicates SSX C-terminus staining in all 100 SS cases with some off-target positivity among controls. (baranov2020anovelss18ssx pages 1-2)

Clinical implication: fusion-specific IHC can reduce reliance on FISH/RT-PCR in many cases, while molecular testing remains important for unusual patterns or equivocal cases. (baranov2020anovelss18ssx pages 1-2)

### 10.3 Differential diagnosis considerations
SS can overlap morphologically and immunophenotypically with other sarcomas and carcinomas; IHC markers like TLE1 are helpful but not perfectly specific, supporting continued use of confirmatory molecular testing in challenging cases. (louati2025molecularprofilingof pages 12-14, baranov2020anovelss18ssx pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Survival statistics (recently summarized)
A 2025 review summarizing SEER-derived survival reports survival estimates including **1-, 5-, 10-, and 20-year survival rates of 87.3%, 59.4%, 50.8%, and 42.8%**, with **median overall survival ~138 months**; it also notes worse outcomes with metastatic disease at diagnosis and larger tumors, as well as differences by histologic subtype and age. (bulski2025synovialsarcomaamong pages 6-7)

### 11.2 Prognostic factors
Key prognostic factors reported across reviews include:
- Tumor size, margin status/completeness of resection, site, and metastasis at diagnosis. (ferrari2023treatmentatrelapse pages 1-2, bulski2025synovialsarcomaamong pages 6-7)
- Imaging-associated adverse indicators (triple sign; bowl-of-grapes; hemorrhage/fluid–fluid levels; intercompartmental extension; peritumoral enhancement), with calcification associated with more favorable outcomes in the imaging review’s prognostic table. (cho2023synovialsarcomain media 0aa1424d)

---

## 12. Treatment

### 12.1 Standard-of-care (real-world implementation)
- **Localized SS:** wide surgical resection is the mainstay; radiotherapy and chemotherapy are used in risk-adapted settings (e.g., large tumors, high-risk features, positive margins). (ferrari2023treatmentatrelapse pages 1-2, bulski2025synovialsarcomaamong pages 6-7)
- **Advanced/metastatic SS:** anthracycline-based chemotherapy remains standard; later-line options include TKIs and agents such as trabectedin/pazopanib as summarized in reviews. (fuchs2023emergingtargetedand pages 7-8, lesovaya2024geneticandmolecular pages 5-6)

Suggested MAXO terms (examples):
- Surgical excision of tumor
- External beam radiotherapy
- Anthracycline-based chemotherapy
- Ifosfamide therapy

### 12.2 Recent developments and latest research (prioritize 2023–2024)

#### 12.2.1 Engineered TCR-T cell therapy (major 2023–2024 clinical advance)
A 2025 expert review summarizing SPEARHEAD-1 reports that MAGE-A4-directed engineered TCR therapy **afamitresgene autoleucel** achieved an **objective response rate (ORR) of ~43%** with **median duration of response ~6 months** in advanced synovial sarcoma, and ties this to regulatory approval in the appropriate HLA/antigen context. (wang2025molecularandepigenetic pages 7-8)

Rationale for target selection: SS expresses cancer-testis antigens including MAGE-A4, NY-ESO-1, and PRAME, enabling antigen-directed cellular therapies. (lesovaya2024geneticandmolecular pages 5-6, wang2025molecularandepigenetic pages 7-8)

#### 12.2.2 Epigenetic and chromatin-directed therapeutic vulnerabilities (2023–2024 research)
A 2023 review highlights that improved understanding of SS molecular biology has enabled exploration of newer modalities including PROTAC degraders and other approaches aimed at chromatin/transcriptional dependencies driven by SS18::SSX. (landuzzi2023innovativebreakthroughsfor pages 1-2)

Mechanistic work identifying PRC1.1/H2AK119ub1 as required for SS18-SSX occupancy provides a rationale for therapeutically targeting Polycomb/chromatin dependencies. (benabdallah2023aberrantgeneactivation pages 1-2)

#### 12.2.3 Tyrosine kinase inhibitors (TKIs) and targeted agents
Recent reviews describe ongoing investigation of multikinase inhibitors and other targeted agents in SS, with pazopanib often cited in practice-oriented summaries and additional TKIs under study. (lesovaya2024geneticandmolecular pages 5-6)

---

## 13. Prevention
No established primary prevention strategy is supported by the retrieved evidence. Practical “prevention” is best interpreted as:
- **Secondary prevention:** early recognition of suspicious soft-tissue masses and timely biopsy/molecular testing to avoid misdiagnosis and delay. (cho2023synovialsarcomain media 393c0cbc, cho2023synovialsarcomain media 0aa1424d)
- **Tertiary prevention:** guideline-based multimodal management and surveillance for recurrence/metastasis.

---

## 14. Other Species / Natural Disease
Naturally occurring synovial sarcoma in other species was not identified in the retrieved evidence.

---

## 15. Model Organisms / Preclinical Models
A 2023 review details that SS preclinical modeling includes:
- Conditional transgenic mouse models expressing SS18::SSX that can develop SS, sometimes in combination with cooperating alterations (e.g., BCL2, Wnt/β-catenin, FGFR, PTEN loss, SMARCB1 loss). (landuzzi2023innovativebreakthroughsfor pages 1-2)
- Patient-derived xenografts (PDX) and cell line-derived xenografts.

These models are used to discover vulnerabilities and develop epigenetic and immunotherapeutic strategies. (landuzzi2023innovativebreakthroughsfor pages 1-2)

---

## High-yield structured summary table
The following table is designed for rapid knowledge-base ingestion.

| Domain | Key facts |
|---|---|
| Identifiers / classification | • Rare malignant soft-tissue sarcoma; WHO-recognized mesenchymal spindle-cell tumor that may show epithelial differentiation. • Common aliases include synovial sarcoma, SyS, SS, and older fusion terminology SYT-SSX / SS18-SSX. • MONDO/ICD/Orphanet/OMIM specific codes: not found in gathered sources. (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2, landuzzi2023innovativebreakthroughsfor pages 1-2) |
| Core genetic driver | • Pathognomonic t(X;18)(p11;q11) creates SS18::SSX fusion, most often SSX1 or SSX2 and rarely SSX4. • Fusion is present in >90–95% of cases and is the central diagnostic/molecular hallmark. • SS18::SSX perturbs chromatin-remodeling machinery rather than acting as a classic kinase driver. (ferrari2023treatmentatrelapse pages 1-2, baranov2020anovelss18ssx pages 1-2, benabdallah2023aberrantgeneactivation pages 1-2) |
| Epidemiology | • Accounts for ~8–10% of soft tissue sarcomas in some series/reviews; one review cites 4–10% of STS subtypes. • Incidence is ~0.8 per million/year in children and ~1.4 per million/year in adults; U.S. incidence ~1.42 per million has also been reported. • Predominantly affects adolescents and young adults, especially ages 15–40/15–35; slight male predominance. (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2, bulski2025synovialsarcomaamong pages 6-7) |
| Typical presentation / anatomical sites | • Usually presents as a painless, slowly enlarging deep soft-tissue mass. • Extremities are the dominant site: ~66% in one review; ~80% in soft tissues of extremities in another; near large joints is typical but not required. • Metastases are present in <10% at diagnosis, most commonly to lung. (lesovaya2024geneticandmolecular pages 1-2, ferrari2023treatmentatrelapse pages 1-2, cho2023synovialsarcomain media 393c0cbc) |
| Diagnostics | • Diagnosis relies on biopsy plus molecular confirmation by FISH, RT-PCR, or targeted RNA sequencing for SS18 rearrangement / SS18::SSX transcript. • Fusion-specific IHC is highly useful: E9X9V SS18-SSX antibody showed 95% sensitivity and 100% specificity in a 2020 AJSP study; SSX C-terminus antibody was 100% sensitive but less specific. • TLE1 is useful but imperfectly specific, so unusual cases should trigger molecular testing. (baranov2020anovelss18ssx pages 1-2, qiu2024primaryrenalsynovial pages 6-6, louati2025molecularprofilingof pages 12-14) |
| Prognostic factors | • Worse prognosis is associated with older age, larger tumor size, metastatic disease at diagnosis, higher grade, non-extremity/axial sites, and incomplete resection/positive margins. • Radiologic adverse indicators include triple sign, bowl-of-grapes appearance, hemorrhage/fluid-fluid levels, intercompartment extension, and lack of calcification; calcification can be relatively favorable. • Reported survival estimates include median OS ~138 months in SEER-based analysis and 5-year survival roughly 59–71% across broad cohorts. (bulski2025synovialsarcomaamong pages 6-7, cho2023synovialsarcomain media 393c0cbc, cho2023synovialsarcomain media 0aa1424d) |
| Standard treatment | • Localized disease: wide surgical resection is the mainstay. • Radiotherapy is commonly used for larger tumors, high-grade tumors, or positive/close margins; chemotherapy is considered for high-risk localized or advanced disease. • Advanced/metastatic disease is typically treated with anthracycline-based chemotherapy, often with ifosfamide; later-line options include trabectedin and pazopanib. (fuchs2023emergingtargetedand pages 7-8, bulski2025synovialsarcomaamong pages 6-7, lesovaya2024geneticandmolecular pages 5-6) |
| Emerging therapies 2023–2024 | • Engineered TCR-T therapies targeting cancer-testis antigens are the major advance: MAGE-A4-targeted afamitresgene autoleucel showed ORR ~43% with median response duration ~6 months in SPEARHEAD-1. • NY-ESO-1-, PRAME-, and MAGE-A4-directed TCR approaches remain active areas of development; eligibility depends on antigen expression and HLA type. • Additional investigational strategies include multikinase TKIs (e.g., regorafenib, anlotinib, TAS-115), BRD9/BAF-directed approaches, HDAC/EZH2-directed epigenetic therapy, and combination immune strategies. (wang2025molecularandepigenetic pages 6-7, lesovaya2024geneticandmolecular pages 5-6, wang2025molecularandepigenetic pages 7-8) |
| Key mechanistic pathways / epigenetics | • SS18::SSX rewires BAF/SWI-SNF chromatin complexes and links to Polycomb biology; PRC1.1-mediated H2AK119ub1 deposition is required for fusion occupancy, and the SSX C-terminus increases PRC1.1 stability. • Additional implicated pathways include Wnt/β-catenin, YAP/TAZ-TEAD, CREB/CDK9, and TYK2→STAT3→BCL2 apoptosis-evasion signaling. • Tumors frequently express cancer-testis antigens such as NY-ESO-1, MAGE-A4, and PRAME, while often exhibiting an immune-cold microenvironment. (benabdallah2023aberrantgeneactivation pages 1-2, lesovaya2024geneticandmolecular pages 5-6, wang2025molecularandepigenetic pages 6-7) |
| Model systems | • Available preclinical systems include conditional transgenic mouse models expressing SS18::SSX, synovial sarcoma cell lines, cell line-derived xenografts, and patient-derived xenografts. • Mouse models have been combined with alterations such as BCL2 gain, Wnt/β-catenin activation, FGFR changes, PTEN loss, or SMARCB1 loss to study sarcomagenesis. • These models are used to identify vulnerabilities in chromatin regulation, immune targeting, and combination therapy. (landuzzi2023innovativebreakthroughsfor pages 1-2, benabdallah2023aberrantgeneactivation pages 1-2) |


*Table: This table summarizes high-yield knowledge-base facts on synovial sarcoma across genetics, epidemiology, presentation, diagnosis, prognosis, treatment, mechanisms, and models. It is designed for rapid curation and includes only findings supported by gathered citation contexts.*

---

## Notes on evidence limitations
- **Ontology codes (MONDO/MeSH/ICD/Orphanet/OMIM):** not present in retrieved full-text evidence and therefore not provided.
- **PMIDs:** Many retrieved sources were provided with DOI/URLs; PMIDs were not consistently present in the tool outputs and are therefore not systematically reported here.

---

## Key cited sources (with URLs and publication dates when available)
- Ferrari et al. *Cancer Management and Research* (2023-10). https://doi.org/10.2147/CMAR.S404371 (ferrari2023treatmentatrelapse pages 1-2)
- Landuzzi et al. *Cancers* (2023-07). https://doi.org/10.3390/cancers15153887 (landuzzi2023innovativebreakthroughsfor pages 1-2)
- Benabdallah et al. *Nat Struct Mol Biol* (published online 2023-09-21). https://doi.org/10.1038/s41594-023-01096-3 (benabdallah2023aberrantgeneactivation pages 1-2)
- Lesovaya et al. *Cells* (2024-10). https://doi.org/10.3390/cells13201695 (lesovaya2024geneticandmolecular pages 1-2, lesovaya2024geneticandmolecular pages 5-6)
- Baranov et al. *Am J Surg Pathol* (2020-03). https://doi.org/10.1097/PAS.0000000000001447 (baranov2020anovelss18ssx pages 1-2)
- Cho et al. *Cancers* (2023-10). https://doi.org/10.3390/cancers15194860 (cho2023synovialsarcomain media 393c0cbc, cho2023synovialsarcomain media 0aa1424d)
- Wang et al. *Oncogene* (published online 2025-08-23). https://doi.org/10.1038/s41388-025-03547-1 (wang2025molecularandepigenetic pages 1-2, wang2025molecularandepigenetic pages 7-8)


References

1. (lesovaya2024geneticandmolecular pages 1-2): Ekaterina A. Lesovaya, Timur I. Fetisov, Beniamin Yu. Bokhyan, Varvara P. Maksimova, Evgeny P. Kulikov, Gennady A. Belitsky, Kirill I. Kirsanov, and Marianna G. Yakubovskaya. Genetic and molecular heterogeneity of synovial sarcoma and associated challenges in therapy. Cells, 13:1695, Oct 2024. URL: https://doi.org/10.3390/cells13201695, doi:10.3390/cells13201695. This article has 16 citations.

2. (ferrari2023treatmentatrelapse pages 1-2): Andrea Ferrari, Pablo Berlanga, Susanne Andrea Gatz, Reineke A Schoot, Max M van Noesel, Shushan Hovsepyan, Stefano Chiaravalli, Luca Bergamaschi, Veronique Minard-Colin, Nadege Corradini, Rita Alaggio, Patrizia Gasparini, Bernadette Brennan, Michela Casanova, Sandro Pasquali, and Daniel Orbach. Treatment at relapse for synovial sarcoma of children, adolescents and young adults: from the state of art to future clinical perspectives. Cancer Management and Research, 15:1183-1196, Oct 2023. URL: https://doi.org/10.2147/cmar.s404371, doi:10.2147/cmar.s404371. This article has 8 citations and is from a peer-reviewed journal.

3. (louati2025molecularprofilingof pages 12-14): Sara Louati, Kaoutar Bentayebi, Ibtissam Saad, Yvonne Gloor, Nadia Senhaji, Abdelmajid Elmrini, Lahcen Belyamani, Rachid Eljaoudi, Marc Ansari, Sanae Bennis, and Youssef Daali. Molecular profiling of syt-ssx fusion transcripts for enhanced diagnosis of synovial sarcomas. Journal of Personalized Medicine, 15:455, Sep 2025. URL: https://doi.org/10.3390/jpm15100455, doi:10.3390/jpm15100455. This article has 0 citations.

4. (baranov2020anovelss18ssx pages 1-2): Esther Baranov, Matthew J. McBride, Andrew M. Bellizzi, Azra H. Ligon, Christopher D.M. Fletcher, Cigall Kadoch, and Jason L. Hornick. A novel ss18-ssx fusion-specific antibody for the diagnosis of synovial sarcoma. The American Journal of Surgical Pathology, 44:922-933, Mar 2020. URL: https://doi.org/10.1097/pas.0000000000001447, doi:10.1097/pas.0000000000001447. This article has 234 citations.

5. (bulski2025synovialsarcomaamong pages 6-7): Jakub Bulski, Filip Maj, Karol Sornat, Agata Estreicher, Anna Klasa, Aleksandra Sobaś, Kamil Biedka, Oliwia Ziobro, and Katarzyna Błaszczyk. Synovial sarcoma among adults: from epidemiology to clinical presentation, current diagnostic standards, treatment methods and prognosis. Archiv Euromedica, Apr 2025. URL: https://doi.org/10.35630/2025/15/2.211, doi:10.35630/2025/15/2.211. This article has 0 citations.

6. (benabdallah2023aberrantgeneactivation pages 1-2): Nezha S. Benabdallah, Vineet Dalal, R. Wilder Scott, Fady Marcous, Afroditi Sotiriou, Felix K. F. Kommoss, Anastasija Pejkovska, Ludmila Gaspar, Lena Wagner, Francisco J. Sánchez-Rivera, Monica Ta, Shelby Thornton, Torsten O. Nielsen, T. Michael Underhill, and Ana Banito. Aberrant gene activation in synovial sarcoma relies on ssx specificity and increased prc1.1 stability. Nature Structural &amp; Molecular Biology, 30:1640-1652, Sep 2023. URL: https://doi.org/10.1038/s41594-023-01096-3, doi:10.1038/s41594-023-01096-3. This article has 35 citations and is from a highest quality peer-reviewed journal.

7. (landuzzi2023innovativebreakthroughsfor pages 1-2): Lorena Landuzzi, Maria Cristina Manara, Laura Pazzaglia, Pier-Luigi Lollini, and Katia Scotlandi. Innovative breakthroughs for the treatment of advanced and metastatic synovial sarcoma. Cancers, 15:3887, Jul 2023. URL: https://doi.org/10.3390/cancers15153887, doi:10.3390/cancers15153887. This article has 17 citations.

8. (cho2023synovialsarcomain media 393c0cbc): Eun Byul Cho, Seul Ki Lee, Jee-Young Kim, and Yuri Kim. Synovial sarcoma in the extremity: diversity of imaging features for diagnosis and prognosis. Cancers, 15:4860, Oct 2023. URL: https://doi.org/10.3390/cancers15194860, doi:10.3390/cancers15194860. This article has 34 citations.

9. (cho2023synovialsarcomain media 0aa1424d): Eun Byul Cho, Seul Ki Lee, Jee-Young Kim, and Yuri Kim. Synovial sarcoma in the extremity: diversity of imaging features for diagnosis and prognosis. Cancers, 15:4860, Oct 2023. URL: https://doi.org/10.3390/cancers15194860, doi:10.3390/cancers15194860. This article has 34 citations.

10. (lesovaya2024geneticandmolecular pages 5-6): Ekaterina A. Lesovaya, Timur I. Fetisov, Beniamin Yu. Bokhyan, Varvara P. Maksimova, Evgeny P. Kulikov, Gennady A. Belitsky, Kirill I. Kirsanov, and Marianna G. Yakubovskaya. Genetic and molecular heterogeneity of synovial sarcoma and associated challenges in therapy. Cells, 13:1695, Oct 2024. URL: https://doi.org/10.3390/cells13201695, doi:10.3390/cells13201695. This article has 16 citations.

11. (wang2025molecularandepigenetic pages 7-8): Amy Xueqi Wang, Kevin B. Jones, and Torsten O. Nielsen. Molecular and epigenetic oncogenesis in synovial sarcoma: implications for cancer biology, diagnosis and treatment. Oncogene, 44:3527-3536, Aug 2025. URL: https://doi.org/10.1038/s41388-025-03547-1, doi:10.1038/s41388-025-03547-1. This article has 4 citations and is from a domain leading peer-reviewed journal.

12. (qiu2024primaryrenalsynovial pages 6-6): Hong Qiu, Zhaorong Tang, and Dan Nie. Primary renal synovial sarcomas diagnosed by a novel fusion gene with the fusion site involving exons of ss18 and ssx2: a case report. Oncologie, 26:679-685, May 2024. URL: https://doi.org/10.1515/oncologie-2024-0101, doi:10.1515/oncologie-2024-0101. This article has 2 citations and is from a peer-reviewed journal.

13. (fuchs2023emergingtargetedand pages 7-8): Joseph R. Fuchs, Brian C. Schulte, Jeffrey W. Fuchs, and Mark Agulnik. Emerging targeted and cellular therapies in the treatment of advanced and metastatic synovial sarcoma. Frontiers in Oncology, Jan 2023. URL: https://doi.org/10.3389/fonc.2023.1123464, doi:10.3389/fonc.2023.1123464. This article has 16 citations.

14. (wang2025molecularandepigenetic pages 6-7): Amy Xueqi Wang, Kevin B. Jones, and Torsten O. Nielsen. Molecular and epigenetic oncogenesis in synovial sarcoma: implications for cancer biology, diagnosis and treatment. Oncogene, 44:3527-3536, Aug 2025. URL: https://doi.org/10.1038/s41388-025-03547-1, doi:10.1038/s41388-025-03547-1. This article has 4 citations and is from a domain leading peer-reviewed journal.

15. (wang2025molecularandepigenetic pages 1-2): Amy Xueqi Wang, Kevin B. Jones, and Torsten O. Nielsen. Molecular and epigenetic oncogenesis in synovial sarcoma: implications for cancer biology, diagnosis and treatment. Oncogene, 44:3527-3536, Aug 2025. URL: https://doi.org/10.1038/s41388-025-03547-1, doi:10.1038/s41388-025-03547-1. This article has 4 citations and is from a domain leading peer-reviewed journal.

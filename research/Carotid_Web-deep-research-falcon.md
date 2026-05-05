---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-05T16:49:03.540839'
end_time: '2026-05-05T17:05:45.014046'
duration_seconds: 1001.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Carotid web
  mondo_id: ''
  category: Complex
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
- **Disease Name:** Carotid web
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Carotid web** covering all of the
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
- **Disease Name:** Carotid web
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Carotid web** covering all of the
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


# Carotid web — Comprehensive Disease Characteristics Report

## Target disease
- **Disease name:** Carotid web (carotid artery web)
- **Category:** Complex (vascular anomaly / non-atherosclerotic carotid arteriopathy associated with ischemic stroke)
- **MONDO ID:** Not identified from the retrieved sources in this run (see “Key identifiers”).

---

## Executive summary (current understanding; 2023–2024 emphasized)
Carotid web (CaW) is a **non-atherosclerotic, shelf-like intimal projection** arising classically from the **posterior wall of the carotid bulb/proximal internal carotid artery (ICA)** and is widely considered an **intimal variant of fibromuscular dysplasia (FMD)**. Contemporary reviews and cohort studies support a mechanistic model in which CaW geometry creates **flow separation and stasis in a “web pouch,” promoting local thrombosis and artery-to-artery embolism**, leading to embolic cortical infarctions and large-vessel occlusion (LVO) strokes. Recurrence risk on medical therapy appears substantial in symptomatic webs (commonly summarized as ~10% annualized and ~20% over 2 years), whereas small observational series report low recurrence after carotid endarterectomy (CEA) or carotid artery stenting (CAS), though randomized trial data are lacking. (chen2024carotidwebsa pages 1-2, sayed2024subjectswithcarotid pages 1-2, zedde2025carotidweban pages 9-10)

---

## 1. Disease information

### 1.1 What is the disease? (concise overview)
A carotid web is an **intraluminal, shelf-like intimal flap** in the carotid bulb/proximal ICA. A widely used CTA definition is: **“a thin intraluminal filling defect along the posterior wall of the carotid bulb just beyond the carotid bifurcation… seen as a septum on axial CTA.”** (choi2015carotidwebsand pages 1-3)

Recent narrative reviews similarly define CaW as a **“fibrous, shelf-like intimal flap originating from the posterior wall of the internal carotid bulb projecting into the arterial lumen”** and emphasize its association with cryptogenic/embolic stroke. (chen2024carotidwebsa pages 1-2)

### 1.2 Common synonyms / alternative names
- **Carotid artery web** (CaW) (chen2024carotidwebsa pages 1-2)
- **Carotid web** (CaW/CW) (choi2015carotidwebsand pages 1-3)
- **Carotid diaphragm** (term used in ClinicalTrials.gov study title: “carotid diaphragm responsible for ischemic stroke”) (NCT04442074 chunk 2)
- “Shelf-like intraluminal filling defect” (imaging descriptor) (choi2015carotidwebsand pages 1-3, ahmad2025carotidwebsa pages 1-3)

### 1.3 Key identifiers (OMIM, Orphanet, ICD-10/ICD-11, MeSH, Mondo)
- **MONDO / MeSH / ICD coding:** Not confirmed from the retrieved sources in this run. Carotid web is commonly discussed as an imaging-defined lesion and may be coded under broader carotid/artery anomaly or stenosis/disorder categories in clinical systems; however, a specific code could not be evidenced here.

### 1.4 Evidence source type
The retrieved information is primarily from **aggregated disease-level resources** (narrative reviews and systematic reviews) and **observational human clinical cohorts/series**, plus **ClinicalTrials.gov registries**. (chen2024carotidwebsa pages 1-2, ahmad2025carotidwebsa pages 1-3, NCT04431609 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors (current hypotheses)
- **Non-atherosclerotic arteriopathy / intimal FMD phenotype:** CaW is repeatedly described as an atypical FMD subtype with **pathologic support for intimal fibroplasia/hyperplasia**. (chen2024carotidwebsa pages 1-2, zedde2025carotidweban pages 1-2)
- **Potential congenital/developmental contribution:** Reviews note debated pathogenesis with proposed developmental origins. (chen2024carotidwebsa pages 1-1)
- **Genetic and/or hormonal contributions (hypothesized, not established):** A 2024 review notes “genetic predisposition or hormonal factors” may contribute, but evidence remains limited. (chen2024carotidwebsa pages 1-2)

### 2.2 Risk factors
Evidence is largely observational and heterogeneous.
- **Age:** Often recognized in “young” patients with otherwise cryptogenic/LVO stroke, though CaW can occur across adult ages. (chen2024carotidwebsa pages 1-2, khan2024in‐hospitalrecurrentstroke pages 1-2)
- **Sex:** Female predominance is repeatedly reported in reviews/cohorts. (chen2024carotidwebsa pages 1-1, ahmad2025carotidwebsa pages 3-4)
- **Ancestry/ethnicity:** Associations with African descent/African American or “black population” are reported. (chen2024carotidwebsa pages 1-2, NCT04431609 chunk 1)
- **Traditional vascular risk factors:** Reviews commonly emphasize CaW-associated strokes in patients lacking conventional risk factors, but CaW can coexist with plaque (a distinct subgroup evaluated in multimodal ultrasound cohorts). (khan2024in‐hospitalrecurrentstroke pages 1-2, hou2024thedifferencesbetween pages 1-3)

### 2.3 Protective factors
No protective genetic variants or protective environmental factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
No CaW-specific gene–environment interaction evidence was identified in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes (human)
Carotid web itself is often asymptomatic until thromboembolism occurs; the clinically salient phenotype is **ischemic stroke** (often embolic/LVO) or **TIA** in the ipsilateral carotid territory.

**Ischemic stroke (embolic, often LVO)**
- CaW is linked to embolic strokes and LVO; one review summarizes CaW as contributing to **“2.5% of all large vessel occlusion strokes.”** (chen2024carotidwebsa pages 1-2)
- A thrombectomy cohort study (July 2015–March 2023) found ipsilateral CaW in **27/1463 (1.8%)** thrombectomy patients; CaW patients were younger (median 60 vs 74 years) and often had no competing mechanism. (khan2024in‐hospitalrecurrentstroke pages 1-2)

**Recurrent ischemic stroke**
- A classic CTA-era series reported recurrent stroke in **5/7 (71.4%)** with recurrence occurring 1–97 months. (choi2015carotidwebsand pages 1-3)
- Contemporary summaries cite recurrent events on medical therapy (see Prognosis/Treatment). (chen2024carotidwebsa pages 1-1)

**Transient ischemic attack (TIA)**
- The CAROWEB registry includes patients with “cerebral infarction or transient ischemic attack” downstream of a CaW lesion. (NCT04431609 chunk 1)

### 3.2 Phenotype characteristics (onset, severity, progression)
- **Onset pattern:** Acute neurologic deficits due to ischemic stroke/TIA. (NCT04431609 chunk 1)
- **Severity:** Can be severe; CAROWEB describes association with “severe cerebral infarction in the carotid territory.” (NCT04431609 chunk 1)
- **Course:** High recurrence risk in symptomatic cases, including in-hospital recurrence after thrombectomy. (khan2024in‐hospitalrecurrentstroke pages 1-2)

### 3.3 Suggested HPO terms (examples for a knowledge base)
(Exact mapping may vary by curator policy; these are appropriate candidates.)
- **Ischemic stroke** — *HP:0002140*
- **Transient ischemic attack** — *HP:0002327*
- **Cerebral infarction** — *HP:0002140* (often used for stroke) / consider ontology-specific infarction term if used locally
- **Hemiparesis** — *HP:0001269* (frequently reported in case presentations) (ahmad2025carotidwebsa pages 12-13)
- **Aphasia** — *HP:0002381* (reported in case presentations) (ahmad2025carotidwebsa pages 12-13)
- **Facial weakness** — *HP:0030319* (reported in case presentations) (ahmad2025carotidwebsa pages 12-13)

### 3.4 Quality-of-life impact
QoL instruments (EQ-5D/SF-36/PROMIS) were not reported in the retrieved evidence; functional outcomes in registries are typically captured as modified Rankin Scale (mRS) at 3–6 months (CAROWEB). (NCT04431609 chunk 1)

---

## 4. Genetic / molecular information

### 4.1 Causal genes / pathogenic variants
No CaW-specific causal genes or pathogenic variants were identified from the retrieved primary/clinical literature in this run.

### 4.2 Evidence for genetic contribution (investigational)
- **Registry plans for polymorphism studies:** A prospective CaW registry explicitly includes “detection of genetic polymorphisms associated with CW” as a secondary aim, indicating ongoing investigation rather than established genetics. (NCT05475080 chunk 1)
- **Familial screening study:** Family-WEB (NCT06336083) screens first-degree relatives, motivated by epidemiologic signals and possible genetic contribution, while noting no established familial forms to date. (NCT06336083 chunk 1)

### 4.3 Epigenetics / molecular profiling / multi-omics
No CaW-specific epigenomic/transcriptomic/proteomic/metabolomic signatures were identified in the retrieved sources.

---

## 5. Environmental information
No CaW-specific environmental toxins, lifestyle exposures, or infectious triggers were identified in the retrieved sources. CaW is generally framed as a structural arteriopathy rather than an exposure-driven condition. (chen2024carotidwebsa pages 1-2, sayed2024subjectswithcarotid pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (current mechanistic model)
1. **Anatomical lesion:** A fibrous, shelf-like **intimal flap/projection** at the carotid bulb/proximal ICA (often posterior wall). (chen2024carotidwebsa pages 1-2, zedde2025carotidweban pages 9-10)
2. **Hemodynamic disturbance:** The web creates disturbed flow with **recirculation and stasis** in the web pouch. (sayed2024subjectswithcarotid pages 1-2, chen2024carotidwebsa pages 1-2)
3. **Thrombogenesis:** Stasis and abnormal shear promote thrombus formation; pathology-based reviews describe “small thrombi embedded in the web pouch.” (zedde2025carotidweban pages 1-2)
4. **Embolization:** Thrombus fragments embolize intracranially, producing **embolic ischemic stroke**, including LVO events. (chen2024carotidwebsa pages 1-2, khan2024in‐hospitalrecurrentstroke pages 1-2)

### 6.2 Hemodynamics evidence (2024)
A patient-specific computational fluid dynamics (CFD) study comparing CaW vs mild atherosclerosis vs normal bifurcations reported that CaW patients had significantly larger regions of **low shear rate**, **high oscillatory shear index (OSI)**, **low velocity**, and **flow stasis**, consistent with a pro-thrombotic environment. (sayed2024subjectswithcarotid pages 1-2)

### 6.3 Histopathology evidence (reviewed)
CaW is reviewed as an intimal-FMD-like lesion with intimal hyperplasia/fibroplasia; reviews summarize direct observation of thrombus adherent to or embedded within the lesion. (chen2024carotidwebsa pages 1-2, zedde2025carotidweban pages 3-5)

### 6.4 Suggested ontology terms
**GO biological process (examples):**
- Blood coagulation — *GO:0007596*
- Platelet activation — *GO:0030168*
- Regulation of blood flow — *GO:1903522*
- Thrombus formation — (often modeled via coagulation/platelet activation terms)

**Cell Ontology (CL) candidates (based on thrombosis & intimal remodeling):**
- Vascular smooth muscle cell — *CL:0000192* (implicated by intimal hyperplasia concepts) (chen2024carotidwebsa pages 1-2)
- Endothelial cell — *CL:0000115*
- Platelet — *CL:0000233*

**UBERON anatomy:**
- Internal carotid artery — *UBERON:0001496*
- Common carotid artery — *UBERON:0001644*
- Carotid artery bifurcation / carotid bulb (anatomic region; may require local mapping)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- **Primary site:** Extracranial carotid bifurcation / proximal ICA (posterior wall predilection emphasized in imaging/pathology reviews). (zedde2025carotidweban pages 9-10)
- **Secondary effect:** Brain (ischemic infarction / LVO stroke) downstream of ipsilateral lesion. (khan2024in‐hospitalrecurrentstroke pages 1-2, NCT04431609 chunk 1)

### 7.2 Tissue/cell level
- **Tissue:** Arterial intima (intimal hyperplasia/fibroplasia) (chen2024carotidwebsa pages 1-2)

### 7.3 Subcellular
No CaW-specific subcellular compartment abnormalities were identified.

---

## 8. Temporal development
- **Onset:** Often detected after **acute ischemic stroke/TIA** presentation; can be incidentally found on imaging. (NCT04431609 chunk 1, khan2024in‐hospitalrecurrentstroke pages 1-2)
- **Progression/course:** The main clinically relevant temporal feature is **risk of recurrence** without definitive treatment; in-hospital recurrence after thrombectomy has been quantified (RR estimates). (khan2024in‐hospitalrecurrentstroke pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (key statistics)
- **General/hospital prevalence:** A hospital-based retrospective series estimated period prevalence **1.2% (7/576; 95% CI 0.4–2.5%)**. (choi2015carotidwebsand pages 1-3)
- **Prevalence in cryptogenic stroke:** Reviews summarize wide ranges; one 2024 imaging cohort review cites **2.5–37%** prevalence in cryptogenic stroke literature. (hou2024thedifferencesbetween pages 1-3)
- **Young cryptogenic stroke enrichment:** A 2024 review summarizes **~13%** frequency among patients with stroke of otherwise unknown etiology and “young” patients with otherwise cryptogenic stroke. (chen2024carotidwebsa pages 1-1)

### 9.2 Demographics
- **Sex:** Female predominance is reported in pooled evidence (systematic review and narrative reviews). (ahmad2025carotidwebsa pages 3-4, chen2024carotidwebsa pages 1-1)
- **Ancestry:** Higher prevalence in African descent/black populations is reported in reviews and registries. (chen2024carotidwebsa pages 1-2, NCT04431609 chunk 1)
- **Laterality/bilaterality:** A systematic review reports **bilateral CaW** in 55 patients in pooled data. (ahmad2025carotidwebsa pages 3-4)

### 9.3 Inheritance
No established Mendelian inheritance pattern is supported in the retrieved sources. Familial screening and polymorphism studies are ongoing/in planning. (NCT06336083 chunk 1, NCT05475080 chunk 1)

---

## 10. Diagnostics

### 10.1 Imaging modalities and diagnostic features
**CTA (computed tomography angiography)**
- Key definition (CTA): “thin intraluminal filling defect… posterior wall… seen as a septum on axial CTA.” (choi2015carotidwebsand pages 1-3)
- Oblique/sagittal reconstructions are emphasized in reviews for best visualization. (chen2024carotidwebsa pages 1-2)

**DSA (digital subtraction angiography)**
- Used for diagnostic uncertainty and for intervention planning; reviews describe a linear filling defect with delayed/late contrast retention. (zedde2025carotidweban pages 9-10)

**Ultrasound (DUS), CEUS, and microvascular flow imaging (SMI)**
- A 2024 cohort study used CEUS and SMI to differentiate CaW vs CaW with plaque and to identify typical features (including a thin triangular endoluminal defect on SMI). (hou2024thedifferencesbetween pages 1-3, hou2024thedifferencesbetween media c303a27b)

**MRI / Vessel wall MRI (VW-MRI)**
- A 2025 review summarizes proposed VW-MRI signs (projection, “double lumen sign,” and contrast stasis) and reports improved detection compared with luminal imaging; reported detection advantages include intimal flap detection **42% vs 16%** and **threefold** higher detection vs MRA in one cohort. (zedde2025carotidweban pages 9-10)

### 10.2 Differential diagnosis
Key differentials explicitly listed in a recent review include:
- Arterial dissection
- Non-calcified atherosclerotic plaque
- Intraluminal thrombus
(zedde2025carotidweban pages 9-10)

### 10.3 Diagnostic performance (available quantitative metrics)
A 2025 review reports high inter-modality agreement between CTA and DSA (e.g., **CTA vs DSA κ≈0.92; CTA κ≈0.88** in summarized studies), with lower performance for ultrasound in some comparisons. (zedde2025carotidweban pages 9-10)

### 10.4 Visual diagnostic exemplars
The following retrieved figure set shows multimodal ultrasound appearances of CaW and CaW with plaque (including SMI depiction of a thin triangular endoluminal defect), supporting real-world implementation of ultrasound-based recognition. (hou2024thedifferencesbetween media c303a27b, hou2024thedifferencesbetween media e72308b7, hou2024thedifferencesbetween media 6a447500)

---

## 11. Outcome / prognosis

### 11.1 Recurrence risk
- A 2024 review summarizes symptomatic CaW recurrence rates **up to ~20% over 2 years** and reports an **annualized stroke risk on medical therapy ~10%** in summarized observational evidence. (chen2024carotidwebsa pages 1-1, chen2024carotidwebsa pages 1-2)
- A 2024 thrombectomy cohort reported markedly increased **in-hospital** recurrence risk when an ipsilateral CaW was present (adjusted RR **4.38** for recurrent ischemic stroke; adjusted RR **4.49** for recurrent ipsilateral LVO). (khan2024in‐hospitalrecurrentstroke pages 1-2)

### 11.2 Functional outcomes
CAROWEB tracks modified Rankin Scale (mRS) at 3–6 months, but the trial record excerpt does not provide quantitative outcome distributions. (NCT04431609 chunk 1)

---

## 12. Treatment

### 12.1 Current practice (observational evidence; no RCTs)
A contemporary review states there are **no randomized controlled trials** for CaW therapy, and describes treatment options as **medical therapy (single/dual antiplatelets; sometimes anticoagulation)** versus **intervention (CEA or CAS)**. (zedde2025carotidweban pages 1-2)

### 12.2 Medical therapy
Observational literature summarized in a 2024 review indicates a **~10% annualized** risk on medical therapy in symptomatic webs. (chen2024carotidwebsa pages 1-2)

### 12.3 Carotid endarterectomy (CEA) and carotid artery stenting (CAS)
- A 2024 review table summarizes **0%** recurrent stroke risk after carotid stenting and **0%** after endarterectomy in compiled observational series (recognizing limitations of small samples and selection). (chen2024carotidwebsa pages 1-2)
- A 2025 review summarizing observational pooled data reports **no recurrent strokes** in interventionally treated patients versus **26.8%** recurrent cerebral ischemia in medically treated patients, while cautioning heterogeneity and potential bias. (zedde2025carotidweban pages 9-10)

### 12.4 MAXO term suggestions (examples)
- Antiplatelet therapy — *MAXO:0000767*
- Anticoagulant therapy — *MAXO:0000740*
- Carotid endarterectomy — (MAXO term for endarterectomy / carotid endarterectomy; map per MAXO catalog)
- Carotid artery stenting — (MAXO term for endovascular stent placement)
- Mechanical thrombectomy — (MAXO term for thrombectomy)

### 12.5 Real-world implementations / care pathways
- **Stroke centers:** CaW is increasingly evaluated in young/cryptogenic/LVO stroke workups, and can influence decisions about secondary prevention or revascularization. (chen2024carotidwebsa pages 1-2, khan2024in‐hospitalrecurrentstroke pages 1-2)
- **Imaging practice:** Use of CTA with multiplanar reconstructions, plus confirmatory modality concordance (e.g., CTA + ultrasound/VW-MRI) is emphasized. (zedde2025carotidweban pages 9-10)

### 12.6 Ongoing trials/registries (ClinicalTrials.gov)
- **CAROWEB registry (France):** NCT04431609, prospective multicenter cohort/registry (start 2019-06-19; planned completion 2026-06-30) capturing imaging, management, mRS, and recurrence. (NCT04431609 chunk 1)
- **Carotid Web and Stroke Registry:** NCT05475080 (start 2022-07-15; primary completion estimate 2024-07-15), compares recurrence by preventive treatment and includes genetic polymorphism investigation. (NCT05475080 chunk 1)
- **Familial screening:** NCT06336083 (Family-WEB; start 2024-09-11), ultrasound screening of first-degree relatives. (NCT06336083 chunk 1)
- **Youth prevalence (population DUS):** NCT07495241 (start 2026-01-04), estimates prevalence in ages 15–25; includes CTA validation subset. (NCT07495241 chunk 1)
- **Radiologic classification/incidence (completed):** NCT06058507 (retrospective cohort; completion 2023-08-20). (NCT06058507 chunk 1)

---

## 13. Prevention

### 13.1 Primary prevention
No established primary prevention strategies specific to CaW were identified; CaW is not currently a target of population screening in standard guidelines based on the retrieved evidence.

### 13.2 Secondary/tertiary prevention
Secondary prevention focuses on preventing recurrent embolic events in patients with diagnosed CaW, using antithrombotic therapy and/or definitive revascularization in selected cases, acknowledging the lack of RCTs. (zedde2025carotidweban pages 1-2)

---

## 14. Other species / natural disease
No evidence of CaW as a naturally occurring disease model in non-human species was identified in the retrieved sources.

---

## 15. Model organisms
No established model organisms for CaW were identified in the retrieved sources.

---

## Key quantitative findings table
| Domain | Key finding | Population/study design (n, setting) | Year | Source (journal/registry) | Identifier (DOI or NCT) | URL |
|---|---|---|---|---|---|---|
| Definition | Carotid web defined on CTA as a **thin intraluminal filling defect** along the **posterior wall of the carotid bulb** just beyond the bifurcation, seen as a septum on axial CTA (choi2015carotidwebsand pages 1-3) | Prospective + retrospective hospital-based imaging series; retrospective denominator **576** CTA/MRI patients | 2015 | *American Journal of Neuroradiology* | DOI: 10.3174/ajnr.a4431 | https://doi.org/10.3174/ajnr.a4431 |
| Definition | Carotid web described as a **fibrous, shelf-like intimal flap** from the posterior wall of the ICA bulb; review notes overall incidence largely unknown (chen2024carotidwebsa pages 1-2) | Narrative review of observational literature | 2024 | *Journal of NeuroInterventional Surgery* | DOI: 10.1136/jnis-2023-021243 | https://doi.org/10.1136/jnis-2023-021243 |
| Definition | Carotid web defined as **intimal fibromuscular dysplasia** with a **shelf-like projection of intimal fibrous tissue into the carotid bulb** (hou2024thedifferencesbetween pages 1-3) | Retrospective imaging cohort **n=299** diagnosed by CTA or HRMRI and evaluated by multimodal ultrasound | 2024 | *Insights into Imaging* | DOI: 10.1186/s13244-024-01650-7 | https://doi.org/10.1186/s13244-024-01650-7 |
| Definition / pathology | Review states carotid web was historically described as an atypical FMD subtype with pathological evidence supporting **intimal FMD** (zedde2025carotidweban pages 9-10) | Narrative review of pathology/imaging/therapy literature | 2025 | *Journal of Stroke* | DOI: 10.5853/jos.2025.00626 | https://doi.org/10.5853/jos.2025.00626 |
| Epidemiology | Hospital-based period prevalence **7/576 = 1.2%** (95% CI **0.4%–2.5%**) (choi2015carotidwebsand pages 1-3) | Retrospective hospital series with baseline head/neck CTA followed by brain MRI | 2015 | *American Journal of Neuroradiology* | DOI: 10.3174/ajnr.a4431 | https://doi.org/10.3174/ajnr.a4431 |
| Epidemiology | Prospective series mean age **50 years** (range **41–55**); **5/7 women (71.4%)** (choi2015carotidwebsand pages 1-3) | Prospective single-center case series **n=7** | 2015 | *American Journal of Neuroradiology* | DOI: 10.3174/ajnr.a4431 | https://doi.org/10.3174/ajnr.a4431 |
| Epidemiology | Review table reports prevalence estimates of **<1%** in total population and **13%** among patients with stroke of otherwise unknown etiology (chen2024carotidwebsa pages 1-2) | Review of published observational studies | 2024 | *Journal of NeuroInterventional Surgery* | DOI: 10.1136/jnis-2023-021243 | https://doi.org/10.1136/jnis-2023-021243 |
| Epidemiology | Cryptogenic stroke association reported range **2.5%–37%**; conservative-therapy recurrence range **11.4%–27.3%** (hou2024thedifferencesbetween pages 1-3) | Review statements within retrospective multimodal ultrasound cohort paper | 2024 | *Insights into Imaging* | DOI: 10.1186/s13244-024-01650-7 | https://doi.org/10.1186/s13244-024-01650-7 |
| Epidemiology | Systematic review pooled **771** patients from **123** articles (registry/cohort **559**; case series/reports **212**); higher prevalence reported in younger patients, females, and Afro-Caribbean individuals (ahmad2025carotidwebsa pages 1-3) | PRISMA systematic review | 2025 | *Journal of Vascular Societies Great Britain & Ireland* | DOI: 10.54522/jvsgbi.2025.164 | https://doi.org/10.54522/jvsgbi.2025.164 |
| Recurrence | Recurrent stroke occurred in **5/7 (71.4%)**; time to recurrence **1–97 months** (choi2015carotidwebsand pages 1-3) | Prospective case series **n=7** | 2015 | *American Journal of Neuroradiology* | DOI: 10.3174/ajnr.a4431 | https://doi.org/10.3174/ajnr.a4431 |
| Recurrence / treatment | Review reports symptomatic carotid webs have recurrence rates as high as **20% over 2 years** (chen2024carotidwebsa pages 1-2) | Narrative review of observational data | 2024 | *Journal of NeuroInterventional Surgery* | DOI: 10.1136/jnis-2023-021243 | https://doi.org/10.1136/jnis-2023-021243 |
| Treatment | Review table reports annualized stroke risk on **medical therapy ~10%**, versus **0%** after **carotid stenting** and **0%** after **endarterectomy** in summarized observational literature (chen2024carotidwebsa pages 1-2) | Review of published observational studies | 2024 | *Journal of NeuroInterventional Surgery* | DOI: 10.1136/jnis-2023-021243 | https://doi.org/10.1136/jnis-2023-021243 |
| Treatment | Review cites pooled comparison: **0 recurrent strokes** in **138** interventionally treated patients vs **26.8%** recurrent cerebral ischemia in **151** medically treated patients; authors caution data are heterogeneous and potentially biased (zedde2025carotidweban pages 9-10) | Narrative review pooling observational cohorts | 2025 | *Journal of Stroke* | DOI: 10.5853/jos.2025.00626 | https://doi.org/10.5853/jos.2025.00626 |
| Pathophysiology | CFD study found CaW patients had significantly larger regions of **low shear rate**, **high oscillatory shear index**, **low velocity**, and **flow stasis** than mild atherosclerosis or normal bifurcations (sayed2024subjectswithcarotid pages 1-2) | Patient-specific CFD using CTA geometries + 2D phase-contrast MRI inflow; CaW **n=13**, mild atherosclerosis **n=7**, healthy **n=6** | 2024 | *Scientific Reports* | DOI: 10.1038/s41598-024-60666-7 | https://doi.org/10.1038/s41598-024-60666-7 |
| Pathophysiology | Review summarizes thrombogenic mechanism as disturbed flow with stasis in the web pouch causing artery-to-artery embolism; pathology has identified **small thrombi embedded in the web pouch** (zedde2025carotidweban pages 9-10) | Narrative review of pathology and hemodynamic literature | 2025 | *Journal of Stroke* | DOI: 10.5853/jos.2025.00626 | https://doi.org/10.5853/jos.2025.00626 |
| Diagnostics | CTA is emphasized as primary acute diagnostic tool; diagnosis often requires concordance of **2 non-invasive modalities**, with DSA reserved for diagnostic uncertainty/intervention planning (zedde2025carotidweban pages 9-10) | Narrative review | 2025 | *Journal of Stroke* | DOI: 10.5853/jos.2025.00626 | https://doi.org/10.5853/jos.2025.00626 |
| Diagnostics | VW-MRI diagnostic proposal includes thickness, posterior projection, “value sign,” “double lumen sign,” and **contrast stasis**; one cohort showed **3-fold** higher detection than MRA, and intimal flaps were seen in **42%** of dissections vs **16%** by luminal techniques (zedde2025carotidweban pages 9-10) | Narrative review summarizing imaging studies | 2025 | *Journal of Stroke* | DOI: 10.5853/jos.2025.00626 | https://doi.org/10.5853/jos.2025.00626 |
| Diagnostics | Multimodal ultrasound/clinical cohort included **299** patients, mean age **60.85 ± 8.77** years; web length independently predicted luminal stenosis in isolated CW, while luminal stenosis and plaque length predicted symptoms in CW with plaque (hou2024thedifferencesbetween pages 1-3) | Retrospective cohort; CTA or HRMRI diagnosis plus CEUS and SMI from 2015–2022 | 2024 | *Insights into Imaging* | DOI: 10.1186/s13244-024-01650-7 | https://doi.org/10.1186/s13244-024-01650-7 |
| Trial / registry | Prospective multicenter registry comparing ischemic recurrences by preventive treatment; target enrollment **100**; adults with stroke/TIA and CW diagnosed by angioCT, angioMRI, or arteriography; includes optional genetic polymorphism analysis (NCT05475080 chunk 1) | Multicenter prospective observational registry | 2022 | ClinicalTrials.gov | NCT05475080 | https://clinicaltrials.gov/study/NCT05475080 |
| Trial / registry | CAROWEB French multicenter prospective registry; target enrollment **300**; adults with validated carotid web and downstream cerebral infarction/TIA; outcomes include imaging phenotype, management, mRS, bleeding, and recurrence (NCT04431609 chunk 1) | National prospective observational cohort/registry | 2019 | ClinicalTrials.gov | NCT04431609 | https://clinicaltrials.gov/study/NCT04431609 |
| Trial / familial | Family-WEB pilot screens first-degree relatives of index cases; estimated enrollment **90**; aims to determine prevalence of carotid web in relatives by Doppler ultrasound, motivated by possible familial/genetic contribution (NCT06336083 chunk 1) | Single-center screening study | 2024 | ClinicalTrials.gov | NCT06336083 | https://clinicaltrials.gov/study/NCT06336083 |
| Trial / prevalence | CaWY cross-sectional survey estimates point prevalence in ages **15–25** by duplex sonography; planned sample **829** (minimum calculated **753**); hypothesis prevalence ~**2%**; includes CTA validation subset (NCT07495241 chunk 1, NCT07495241 chunk 2) | Multicenter population-based cross-sectional cohort | 2026 | ClinicalTrials.gov | NCT07495241 | https://clinicaltrials.gov/study/NCT07495241 |
| Trial / incidence | Completed retrospective cohort, enrollment **31**, designed to determine carotid web incidence, radiologic classification, and relationship with ischemic stroke/TIA using CTA and/or DSA (NCT06058507 chunk 1) | Retrospective observational cohort | 2022 | ClinicalTrials.gov | NCT06058507 | https://clinicaltrials.gov/study/NCT06058507 |


*Table: This table compiles the main quantitative findings, standard definitions, diagnostic features, treatment outcomes, and active registry/trial characteristics for carotid web from the cited evidence. It is useful as a quick reference for building a structured disease knowledge base entry.*

---

## Evidence gaps and expert interpretation
1. **No RCT-level evidence for treatment**: Multiple authoritative reviews emphasize that management is based on observational cohorts/series and expert practice rather than randomized trials. (zedde2025carotidweban pages 1-2, zedde2025carotidweban pages 9-10)
2. **Highly variable prevalence estimates**: Reported CaW prevalence depends strongly on case definition, imaging technique (including reconstruction planes), and selection of cryptogenic/LVO cohorts. (hou2024thedifferencesbetween pages 1-3, chen2024carotidwebsa pages 1-1)
3. **Genetics remains investigational**: Ongoing registries and familial screening studies indicate a plausible genetic contribution, but causal genes/variants are not established in the retrieved clinical literature. (NCT05475080 chunk 1, NCT06336083 chunk 1)

---

## URLs and publication dates (selected key sources)
- Chen et al. *J NeuroIntervent Surg* (Jan 2024). https://doi.org/10.1136/jnis-2023-021243 (chen2024carotidwebsa pages 1-2)
- El Sayed et al. *Scientific Reports* (May 2024). https://doi.org/10.1038/s41598-024-60666-7 (sayed2024subjectswithcarotid pages 1-2)
- Hou et al. *Insights into Imaging* (Mar 2024). https://doi.org/10.1186/s13244-024-01650-7 (hou2024thedifferencesbetween pages 1-3)
- Khan et al. *Ann Clin Transl Neurol* (Aug 2024). https://doi.org/10.1002/acn3.52161 (khan2024in‐hospitalrecurrentstroke pages 1-2)
- Choi et al. *AJNR* (Nov 2015). https://doi.org/10.3174/ajnr.a4431 (choi2015carotidwebsand pages 1-3)
- CAROWEB registry: https://clinicaltrials.gov/study/NCT04431609 (NCT04431609 chunk 1)
- Carotid Web and Stroke Registry: https://clinicaltrials.gov/study/NCT05475080 (NCT05475080 chunk 1)
- Family-WEB: https://clinicaltrials.gov/study/NCT06336083 (NCT06336083 chunk 1)
- CaWY youth prevalence: https://clinicaltrials.gov/study/NCT07495241 (NCT07495241 chunk 1)



References

1. (chen2024carotidwebsa pages 1-2): Huanwen Chen, Marco Colasurdo, Matias Costa, Erez Nossek, and Peter Kan. Carotid webs: a review of pathophysiology, diagnostic findings, and treatment options. Journal of NeuroInterventional Surgery, 16:1294-1298, Jan 2024. URL: https://doi.org/10.1136/jnis-2023-021243, doi:10.1136/jnis-2023-021243. This article has 39 citations and is from a domain leading peer-reviewed journal.

2. (sayed2024subjectswithcarotid pages 1-2): Retta El Sayed, Carissa J. Lucas, Hannah L. Cebull, Fadi B. Nahab, Diogo C. Haussen, Jason W. Allen, and John N. Oshinski. Subjects with carotid webs demonstrate pro-thrombotic hemodynamics compared to subjects with carotid atherosclerosis. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-60666-7, doi:10.1038/s41598-024-60666-7. This article has 13 citations and is from a peer-reviewed journal.

3. (zedde2025carotidweban pages 9-10): Marialuisa Zedde, Maria Simona Stoenoiu, Alexandre Persu, and Rosario Pascarella. Carotid web: an update focusing on its relationship with fibromuscular dysplasia and therapeutic strategy. Journal of Stroke, 27:169-183, May 2025. URL: https://doi.org/10.5853/jos.2025.00626, doi:10.5853/jos.2025.00626. This article has 7 citations and is from a domain leading peer-reviewed journal.

4. (choi2015carotidwebsand pages 1-3): P.M.C. Choi, D. Singh, A. Trivedi, E. Qazi, D. George, J. Wong, A.M. Demchuk, M. Goyal, M.D. Hill, and B.K. Menon. Carotid webs and recurrent ischemic strokes in the era of ct angiography. American Journal of Neuroradiology, 36:2134-2139, Nov 2015. URL: https://doi.org/10.3174/ajnr.a4431, doi:10.3174/ajnr.a4431. This article has 273 citations and is from a peer-reviewed journal.

5. (NCT04442074 chunk 2):  Characteristics in Doppler Ultrasound of the Carotid Diaphragm Responsible for an Ischemic Stroke. Fondation Hôpital Saint-Joseph. 2020. ClinicalTrials.gov Identifier: NCT04442074

6. (ahmad2025carotidwebsa pages 1-3): M. Ahmad, M. Tan, M. Abuarqoub, K. Patel, F. Siracusa, J. Shalhoub, and A. Davies. Carotid webs: a review of diagnosis and management strategies in current literature. Journal of Vascular Societies Great Britain &amp; Ireland, 4:99-110, Feb 2025. URL: https://doi.org/10.54522/jvsgbi.2025.164, doi:10.54522/jvsgbi.2025.164. This article has 2 citations.

7. (NCT04431609 chunk 1):  Carotid Web Associated With Cerebral Infarctions. University Hospital, Bordeaux. 2019. ClinicalTrials.gov Identifier: NCT04431609

8. (zedde2025carotidweban pages 1-2): Marialuisa Zedde, Maria Simona Stoenoiu, Alexandre Persu, and Rosario Pascarella. Carotid web: an update focusing on its relationship with fibromuscular dysplasia and therapeutic strategy. Journal of Stroke, 27:169-183, May 2025. URL: https://doi.org/10.5853/jos.2025.00626, doi:10.5853/jos.2025.00626. This article has 7 citations and is from a domain leading peer-reviewed journal.

9. (chen2024carotidwebsa pages 1-1): Huanwen Chen, Marco Colasurdo, Matias Costa, Erez Nossek, and Peter Kan. Carotid webs: a review of pathophysiology, diagnostic findings, and treatment options. Journal of NeuroInterventional Surgery, 16:1294-1298, Jan 2024. URL: https://doi.org/10.1136/jnis-2023-021243, doi:10.1136/jnis-2023-021243. This article has 39 citations and is from a domain leading peer-reviewed journal.

10. (khan2024in‐hospitalrecurrentstroke pages 1-2): Farhan Khan, Narendra Kala, Kelvin Chang, Liqi Shu, Eric D. Goldstein, Radmehr Torabi, Krisztina Moldovan, Mahesh Jayaraman, Nahid Mohammadzadeh, Karen Furie, and Shadi Yaghi. In‐hospital recurrent stroke in ipsilateral carotid web patients undergoing thrombectomy. Annals of Clinical and Translational Neurology, 11:2450-2456, Aug 2024. URL: https://doi.org/10.1002/acn3.52161, doi:10.1002/acn3.52161. This article has 10 citations and is from a peer-reviewed journal.

11. (ahmad2025carotidwebsa pages 3-4): M. Ahmad, M. Tan, M. Abuarqoub, K. Patel, F. Siracusa, J. Shalhoub, and A. Davies. Carotid webs: a review of diagnosis and management strategies in current literature. Journal of Vascular Societies Great Britain &amp; Ireland, 4:99-110, Feb 2025. URL: https://doi.org/10.54522/jvsgbi.2025.164, doi:10.54522/jvsgbi.2025.164. This article has 2 citations.

12. (hou2024thedifferencesbetween pages 1-3): Chao Hou, Shuo Li, Lei Zhang, Wei Zhang, and Wen He. The differences between carotid web and carotid web with plaque: based on multimodal ultrasonic and clinical characteristics. Insights into Imaging, Mar 2024. URL: https://doi.org/10.1186/s13244-024-01650-7, doi:10.1186/s13244-024-01650-7. This article has 7 citations and is from a peer-reviewed journal.

13. (ahmad2025carotidwebsa pages 12-13): M. Ahmad, M. Tan, M. Abuarqoub, K. Patel, F. Siracusa, J. Shalhoub, and A. Davies. Carotid webs: a review of diagnosis and management strategies in current literature. Journal of Vascular Societies Great Britain &amp; Ireland, 4:99-110, Feb 2025. URL: https://doi.org/10.54522/jvsgbi.2025.164, doi:10.54522/jvsgbi.2025.164. This article has 2 citations.

14. (NCT05475080 chunk 1):  Carotid Web and Stroke Registry.. Fundació Institut de Recerca de l'Hospital de la Santa Creu i Sant Pau. 2022. ClinicalTrials.gov Identifier: NCT05475080

15. (NCT06336083 chunk 1):  Familial Form of Carotid Web: a Doppler Ultrasound Study. University Hospital, Toulouse. 2024. ClinicalTrials.gov Identifier: NCT06336083

16. (zedde2025carotidweban pages 3-5): Marialuisa Zedde, Maria Simona Stoenoiu, Alexandre Persu, and Rosario Pascarella. Carotid web: an update focusing on its relationship with fibromuscular dysplasia and therapeutic strategy. Journal of Stroke, 27:169-183, May 2025. URL: https://doi.org/10.5853/jos.2025.00626, doi:10.5853/jos.2025.00626. This article has 7 citations and is from a domain leading peer-reviewed journal.

17. (hou2024thedifferencesbetween media c303a27b): Chao Hou, Shuo Li, Lei Zhang, Wei Zhang, and Wen He. The differences between carotid web and carotid web with plaque: based on multimodal ultrasonic and clinical characteristics. Insights into Imaging, Mar 2024. URL: https://doi.org/10.1186/s13244-024-01650-7, doi:10.1186/s13244-024-01650-7. This article has 7 citations and is from a peer-reviewed journal.

18. (hou2024thedifferencesbetween media e72308b7): Chao Hou, Shuo Li, Lei Zhang, Wei Zhang, and Wen He. The differences between carotid web and carotid web with plaque: based on multimodal ultrasonic and clinical characteristics. Insights into Imaging, Mar 2024. URL: https://doi.org/10.1186/s13244-024-01650-7, doi:10.1186/s13244-024-01650-7. This article has 7 citations and is from a peer-reviewed journal.

19. (hou2024thedifferencesbetween media 6a447500): Chao Hou, Shuo Li, Lei Zhang, Wei Zhang, and Wen He. The differences between carotid web and carotid web with plaque: based on multimodal ultrasonic and clinical characteristics. Insights into Imaging, Mar 2024. URL: https://doi.org/10.1186/s13244-024-01650-7, doi:10.1186/s13244-024-01650-7. This article has 7 citations and is from a peer-reviewed journal.

20. (NCT07495241 chunk 1): Vendula Krcmarova. Prevalence of Carotid Web in Youth. University of Ostrava. 2026. ClinicalTrials.gov Identifier: NCT07495241

21. (NCT06058507 chunk 1): Ekin Öykü Baylam Yirmibeş. "Carotid Web Incidence and Radiological Classification, Determination of Its Relationship With Ischemic Stroke". Suleyman Demirel University. 2022. ClinicalTrials.gov Identifier: NCT06058507

22. (NCT07495241 chunk 2): Vendula Krcmarova. Prevalence of Carotid Web in Youth. University of Ostrava. 2026. ClinicalTrials.gov Identifier: NCT07495241
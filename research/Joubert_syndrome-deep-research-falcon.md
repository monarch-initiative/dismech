---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T18:34:55.627119'
end_time: '2026-04-25T18:46:49.184030'
duration_seconds: 713.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Joubert syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Joubert syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Joubert syndrome** covering all of the
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
- **Disease Name:** Joubert syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Joubert syndrome** covering all of the
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


## Comprehensive Disease Characteristics Report: Joubert syndrome (genetic ciliopathy)

### 1. Disease information
**Overview/definition.** Joubert syndrome (JS; also “Joubert syndrome and related disorders,” JSRD) is a genetically heterogeneous, primary-cilium disorder (ciliopathy) defined clinically by hypotonia and neurodevelopmental impairment and radiologically by the **molar tooth sign (MTS)** reflecting a characteristic mid–hindbrain malformation. In a 2023 genetics report, JS is described as a “Mendelian disorder of the primary cilium defined by the clinical triad of hypotonia, developmental delay, and a distinct cerebellar malformation called the molar tooth sign” (abstract-level definition). (strong2023toporsasa pages 1-3)

**Key identifiers (from available evidence).**
- **OMIM phenotypic series:** Joubert syndrome (JBTS) **OMIM #213300** is explicitly referenced in a 2023 pediatric cohort paper. (dong2023clinicalandgenetic pages 1-2)
- **Subtypes:** multiple numbered JBTS subtypes exist (e.g., JBTS9 with **CC2D2A**, JBTS10 with **OFD1**), as reflected in case reports and molecular literature. (li2023anovelnonsense pages 1-2)
- **Missing in current evidence capture:** MONDO ID, Orphanet/ORPHA code, MeSH ID, ICD-10/ICD-11 codes were not directly retrievable in the tool-collected sources and should be added from OMIM/Orphanet/NCBI MeSH/WHO ICD resources.

**Synonyms/alternative names (in use in recent literature).** Joubert syndrome (JS), JBTS, Joubert syndrome and related disorders (JSRD), “Joubert anomaly,” and “cerebello-oculo-renal syndromes (JS/CORS)” appear in recent sources. (alhashimi2024neuroimagingcharacteristicsas pages 10-11, NCT00873678 chunk 1)

**Evidence origin.** Statements in this report are primarily derived from **aggregated disease-level resources and cohorts** (reviews, cohort studies, ClinicalTrials.gov records) plus **case reports** for variant expansion; not EHR-derived.


### 2. Etiology
#### 2.1 Disease causal factors
**Primary cause:** **Germline pathogenic variants** in genes encoding proteins that function “in and around the primary cilium” (transition zone, basal body/centrosome, intraflagellar transport, ciliary membrane). (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 1-3)

**Genetic heterogeneity:**
- “Over 40” causal genes are widely cited. (strong2023toporsasa pages 1-3, gana2022genotype–phenotypecorrelatesin pages 1-2)
- A 2022 review states “Over 40 causative genes have been identified… explaining up to 94% of cases.” (gana2022genotype–phenotypecorrelatesin pages 1-2)
- Despite this, one 2023 gene-discovery paper notes molecular diagnosis is not made in **~30–40%** of individuals meeting clinical criteria (highlighting missing variant classes, non-coding variants, structural variants, and/or novel genes). (strong2023toporsasa pages 1-3)

**Inheritance patterns:** Most commonly **autosomal recessive**, but **rare X-linked recessive** and **autosomal dominant** JS cases are reported. (strong2023toporsasa pages 1-3, gonzalezgordillo2023joubertsyndromea pages 1-2, li2023anovelnonsense pages 1-2)

#### 2.2 Risk factors
- **Genetic risk:** having biallelic pathogenic variants in JS genes (AR), or hemizygous pathogenic variants in X-linked genes such as **OFD1** (JBTS10). (li2023anovelnonsense pages 1-2)
- **Population founder effects / elevated carrier frequency:**
  - **TOPORS p.(Pro10Gln)** is proposed as a novel JS cause with evidence for elevated carrier frequency in people of **Dominican ancestry** from a large biobank query. (strong2023toporsasa pages 1-3)
  - A North Macedonia early-pregnancy-loss cohort identified a relatively frequent **CPLANE1 “complex allele”** (c.1819delT;c.7817T>A) with markedly higher JS incidence among **Albanian families**. (bozhinovski2024highincidenceof pages 3-5)

**Environmental risk factors:** No credible non-genetic environmental causal factors are established in the provided evidence.

#### 2.3 Protective factors
No validated genetic or environmental protective factors were identified in the tool-retrieved evidence.

#### 2.4 Gene–environment interactions
No specific gene–environment interaction evidence was identified in the retrieved sources.


### 3. Phenotypes (clinical spectrum)
#### 3.1 Core neurologic phenotype (typical early onset)
Core features repeatedly emphasized include **developmental delay**, **hypotonia**, **ataxia**, **oculomotor apraxia/abnormal eye movements**, and **episodic neonatal breathing dysregulation**. (dong2023clinicalandgenetic pages 1-2, alhashimi2024neuroimagingcharacteristicsas pages 10-11, li2023anovelmutation pages 1-2)

**Cohort statistics (human clinical).** In a retrospective cohort of **36 children**:
- **Developmental delay:** **94.44%** (34/36). (dong2023clinicalandgenetic pages 1-2)
- **MTS on imaging:** **86.11%** (31/36) had a “typical molar tooth sign”; 5 had a “bat wing sign.” (dong2023clinicalandgenetic pages 1-2)
- **Abnormal respiratory rhythm:** 7 cases (six neonatal respiratory distress; one neonatal intermittent apnea). (dong2023clinicalandgenetic pages 3-5)
- **Abnormal VEEG:** 7.69% (subset tested). (dong2023clinicalandgenetic pages 1-2)

**Suggested HPO terms (non-exhaustive).**
- Hypotonia: **HP:0001252**
- Global developmental delay: **HP:0001263**
- Ataxia: **HP:0001251**
- Oculomotor apraxia: **HP:0000657**
- Abnormal respiratory pattern / apnea: **HP:0002104** (apnea), **HP:0002793** (irregular breathing)
- Molar tooth sign: **HP:0002419** (commonly used HPO term)

#### 3.2 Multisystem involvement
A large review emphasizes that **~two-thirds** of patients show extra-CNS involvement, commonly affecting **eye/retina**, **kidney**, **liver**, and **skeleton**. (gana2022genotype–phenotypecorrelatesin pages 1-2, li2023anovelmutation pages 1-2)

**Vision/ocular:** In the 36-child cohort, ocular abnormalities included nystagmus/strabismus/retinal abnormalities/optic-nerve anomalies; multiple types could co-occur in a child. (dong2023clinicalandgenetic pages 3-5)

**Kidney/urinary:**
- In the 36-child cohort: urinary system involvement in 7 cases (including mildly abnormal renal function, nephrolithiasis, collecting system abnormality). (dong2023clinicalandgenetic pages 3-5)
- In a 17-child China cohort focused on renal disease: renal involvement was the second most frequent domain, including **ESKD 35%**, hematuria **29%**, proteinuria **29%**, diffuse lesions **24%**, cystic lesions **12%**. (ying2022attentiontorenal pages 1-2)

**Liver:** The 36-child cohort reported liver damage in 4 cases (elevated transaminases; hepatosplenomegaly). (dong2023clinicalandgenetic pages 3-5)

**Hearing:** hearing abnormalities occurred in 8 cases in the 36-child cohort (including cochlear malformation). (dong2023clinicalandgenetic pages 3-5)

**Suggested HPO terms (multisystem examples).**
- Retinal dystrophy: **HP:0000556**
- Chronic kidney disease: **HP:0012622**; nephronophthisis: **HP:0000090**
- Hepatic fibrosis: **HP:0001395**
- Polydactyly: **HP:0010442**
- Sensorineural hearing impairment: **HP:0000407**

#### 3.3 Quality-of-life impact
Direct QoL instrument results (EQ-5D/SF-36/PROMIS) were not captured in the retrieved evidence. Functional impact is indirectly supported by the need for **rehabilitation** and, in severe cases, tracheostomy/G-tube dependence due to apnea and feeding problems. (strong2023toporsasa pages 3-4, wei2024novelcompoundheterozygous pages 6-7)


### 4. Genetic / molecular information
#### 4.1 Causal genes (representative; not exhaustive)
Genes repeatedly referenced in 2021–2024 clinical genetics sources include **CPLANE1, CEP290, TMEM67, AHI1, RPGRIP1L, CC2D2A, CEP120, CSPP1, OFD1**, among many others. (dong2023clinicalandgenetic pages 3-5, juan2024optimalprenatalgenetic pages 4-6, li2023anovelnonsense pages 1-2, wei2024novelcompoundheterozygous pages 6-7)

**New/expanded gene discovery (2023).** **TOPORS** was nominated as a **novel JS gene** based on a Dominican ancestry proband homozygous for **c.29C>A; p.(Pro10Gln)** and supportive biobank carrier-frequency evidence in Dominicans. (strong2023toporsasa pages 1-3)

#### 4.2 Pathogenic variant classes and functional consequences
Observed classes include:
- **Loss-of-function** (nonsense/frameshift/splice) variants (e.g., OFD1 nonsense variant with transcript reduction consistent with nonsense-mediated decay). (li2023anovelnonsense pages 1-2)
- **Copy-number deletions** (e.g., CC2D2A 7.16 kb deletion in a compound genotype). (strong2023toporsasa pages 1-3)
- **Intronic/non-coding splicing variants** are recognized as an important mechanism (reviewed conceptually in non-coding/splicing-focused work), though detailed diagnostic gains were not captured from 2023–2024 primary JS cohorts in the current evidence set. (dabrusco2023exploringthenoncoding pages 106-110)

**ACMG/AMP classification usage:** Case reports and cohorts explicitly classify variants as pathogenic/likely pathogenic/VUS per ACMG criteria. (dong2023clinicalandgenetic pages 3-5, li2023anovelmutation pages 1-2)

#### 4.3 Gene–phenotype correlations (actionable surveillance)
A 2022 genotype–phenotype review highlights clinically actionable correlations:
- **TMEM67:** significantly higher risk of **liver fibrosis**.
- **NPHP1, RPGRIP1L, TMEM237:** frequent **renal involvement**.
- **CEP290 and AHI1:** higher risk of **retinal dystrophy**; **CEP290** also linked to **chronic kidney disease** risk.
These correlations are presented as guiding “personalized management” and organ surveillance. (gana2022genotype–phenotypecorrelatesin pages 1-2)

#### 4.4 Modifier genes / oligogenicity
A kidney genetics review of modifier concepts (not JS-specific) and the JS/MKS/NPH spectrum review discuss the use of zebrafish/C. elegans and other systems to explore genetic interactions/modifiers in ciliopathies; specific validated JS modifier alleles were not captured in the current evidence set. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 13-15, weghe2022thejoubert–meckel–nephronophthisisspectrum pages 15-16)

#### 4.5 Epigenetics / chromosomal abnormalities
No JS-specific epigenetic mechanisms were identified in the retrieved evidence.


### 5. Environmental information
JS is a monogenic ciliopathy in the retrieved evidence; no specific toxins/lifestyle/infectious triggers were supported by the tool-collected sources.


### 6. Mechanism / pathophysiology
#### 6.1 Core concept: primary cilium dysfunction
Primary cilia are near-ubiquitous microtubule-based organelles acting as “cellular antennae” that mediate **Hedgehog (Hh)** and other signaling pathways; JS arises when variants disrupt proteins acting “in and around the primary cilium.” (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 1-3)

#### 6.2 Signaling pathways and ciliary subdomains implicated
Mechanistic work in the JS–MKS–NPH spectrum emphasizes:
- **Transition zone** function and ciliary membrane **phosphoinositides** (e.g., INPP5E localization and PI distribution), which influence localization of Hh regulators (e.g., SMO, GPR161, TULP3). (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 13-15)
- Hh-dependent neurodevelopmental processes contributing to brain malformations (vermian hypoplasia, axon guidance/decussation defects). (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 15-16)
- Zebrafish mechanistic summaries highlight additional signaling: **Wnt** and **prostaglandin/PGE2→cAMP→IFT** and **Hippo/Yap** roles in ciliogenesis/kidney ciliopathy phenotypes. (wang2024zebrafishasa pages 1-2)

#### 6.3 Causal chain (example: neurodevelopment)
Variant in ciliary gene → disrupted cilium structure/transition zone/ciliary trafficking → altered cilium-dependent morphogen signaling (notably Hh; also other pathways) → impaired neural proliferation/fate specification/migration/axon guidance → mid–hindbrain malformation → MTS and hypotonia/ataxia/oculomotor/breathing dysregulation. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 15-16, weghe2022thejoubert–meckel–nephronophthisisspectrum pages 13-15)

#### 6.4 Suggested GO / CL terms
**GO Biological Process (examples):**
- Hedgehog signaling pathway: **GO:0007224**
- Cilium assembly: **GO:0060271**
- Intraflagellar transport: **GO:0030990**
- Neuron migration: **GO:0001764**
- Axon guidance: **GO:0007411**

**GO Cellular Component:**
- Primary cilium: **GO:0072372**
- Ciliary transition zone: **GO:0097546**
- Centrosome: **GO:0005813**

**Cell Ontology (examples):**
- Neuron: **CL:0000540**
- Retinal photoreceptor cell: **CL:0000210**
- Kidney epithelial cell: **CL:0000066**

#### 6.5 Molecular profiling / advanced technologies
A 2021–2024 interventional biomarker study for ciliopathies (including JS) explicitly plans **transcriptome, proteome, metabolome** profiling using urine-derived renal epithelial cells and iPSC-derived renal organoids to develop prognostic renal biomarkers. (NCT04874909 chunk 1)


### 7. Anatomical structures affected (multi-level)
#### 7.1 Organ/system level (UBERON suggestions)
- **Brain (CNS):** cerebellum and brainstem (mid–hindbrain) malformation producing MTS. (alhashimi2024neuroimagingcharacteristicsas pages 10-11, dong2023clinicalandgenetic media e70ab935)
  - UBERON: brain **UBERON:0000955**, cerebellum **UBERON:0002037**, brainstem **UBERON:0002298**, cerebellar vermis **UBERON:0004670**
- **Eye/retina:** retinal dystrophy and other ocular motor abnormalities are frequent. (dong2023clinicalandgenetic pages 3-5, gana2022genotype–phenotypecorrelatesin pages 1-2)
  - UBERON: retina **UBERON:0000966**
- **Kidney:** nephronophthisis/cystic disease/ESKD in a substantial subset. (ying2022attentiontorenal pages 1-2, takagi2021anymodalityof pages 1-2)
  - UBERON: kidney **UBERON:0002113**
- **Liver:** hepatic fibrosis/liver injury in subsets and elevated risk with TMEM67. (gana2022genotype–phenotypecorrelatesin pages 1-2, dong2023clinicalandgenetic pages 3-5)
  - UBERON: liver **UBERON:0002107**

#### 7.2 Subcellular localization
Primary cilium, ciliary transition zone, basal body/centrosome are central sites. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 1-3, weghe2022thejoubert–meckel–nephronophthisisspectrum pages 13-15)


### 8. Temporal development
**Onset:** often congenital/infancy with neonatal respiratory dysregulation and early hypotonia/developmental delay. (gonzalezgordillo2023joubertsyndromea pages 1-2, dong2023clinicalandgenetic pages 3-5)

**Progression:** variable; extra-CNS involvement may present later and requires longitudinal surveillance. (gana2022genotype–phenotypecorrelatesin pages 1-2)


### 9. Inheritance and population
#### 9.1 Epidemiology
- Commonly cited frequency: **1:80,000–1:100,000 live births**. (gonzalezgordillo2023joubertsyndromea pages 1-2, takagi2021anymodalityof pages 1-2)
- Population-based prevalence estimate: **1.7 per 100,000** among ages 0–19 years. (gana2022genotype–phenotypecorrelatesin pages 1-2, li2023anovelmutation pages 1-2)

#### 9.2 Population genetics / founder effects
- **Dominican ancestry:** TOPORS p.(Pro10Gln) variant suggested to have elevated carrier frequency (biobank evidence), raising consideration for ancestry-informed testing. (strong2023toporsasa pages 1-3)
- **Albanian families (North Macedonia):** early pregnancy loss study reports JS incidence **2.03% (5/246)** in euploid products of conception and **6.25% (5/80)** in Albanian families; supports targeted screening for a specific CPLANE1 complex allele. (bozhinovski2024highincidenceof pages 3-5)

**Sex ratio:** a 36-child cohort had 18 male/18 female (1:1) but this is not a population-level estimate. (dong2023clinicalandgenetic pages 1-2)


### 10. Diagnostics
#### 10.1 Clinical criteria and imaging
**MRI hallmark:** MTS is repeatedly emphasized as the diagnostic hallmark; detailed anatomic description includes thickened/elongated superior cerebellar peduncles, deep interpeduncular fossa, and vermian hypoplasia/aplasia. (strong2023toporsasa pages 1-3, alhashimi2024neuroimagingcharacteristicsas pages 10-11)

**Visual evidence (MRI).** Figure panels from a 2023 pediatric cohort show classic MTS and related signs on brain MRI (molar tooth sign and bat-wing sign). (dong2023clinicalandgenetic media e70ab935)

#### 10.2 Genetic testing strategy
**WES/WGS/panels:** Exome sequencing is widely used due to high locus heterogeneity; a 2023 cohort used WES in a subset and identified novel variants in several genes. (dong2023clinicalandgenetic pages 3-5)

**Prenatal diagnosis and diagnostic yield (2024).** In fetuses with posterior fossa malformation, one 2024 cohort reports WES detection rates stratified by phenotype; importantly, the detection rate for fetuses classified as JS was **83.33% (5/6)**, leading the authors to recommend WES as a first-line prenatal test for suspected JS. (juan2024optimalprenatalgenetic pages 4-6)

**Differential diagnosis (high-level).** Related ciliopathy-spectrum disorders include Meckel syndrome and nephronophthisis, with overlapping gene sets and organ involvement. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 1-3)


### 11. Outcome / prognosis
**Prognosis drivers:** presence and severity of extra-CNS involvement (kidney, liver, retina) drive long-term outcomes. (gana2022genotype–phenotypecorrelatesin pages 1-2)

**Cohort evidence (2023):** A 36-child cohort found prognosis after rehabilitation was better in “pure JBTS” than JBTS with multi-organ involvement (statistically significant, P<0.05). (dong2023clinicalandgenetic pages 1-2)

**Renal failure outcomes and survival (RRT series).** In 11 JS patients with ESKD receiving renal replacement therapy: peritoneal dialysis was used in 7 (median duration 5.4 years), hemodialysis in 2, and kidney transplantation performed 9 times in 8 patients; only one graft failed during follow-up and all were alive except one who died of hepatic failure while on PD. (takagi2021anymodalityof pages 1-2)


### 12. Treatment
#### 12.1 Disease-modifying therapy
No specific curative therapy is supported in the retrieved evidence; management is supportive and preventive (organ surveillance). (wei2024novelcompoundheterozygous pages 6-7)

#### 12.2 Supportive/rehabilitative care (real-world implementation)
- **Multidisciplinary care** is consistently emphasized (neurology, nephrology, ophthalmology, etc.). (alhashimi2024neuroimagingcharacteristicsas pages 10-11, gonzalezgordillo2023joubertsyndromea pages 1-2)
- **Rehabilitation therapies** (physical/occupational/speech) are suggested to improve movement and speech impairment; cohort data support better outcomes in “pure JBTS” after formal rehabilitation. (dong2023clinicalandgenetic pages 1-2, wei2024novelcompoundheterozygous pages 6-7)
- **Respiratory management** can include caffeine for central apneas in neonatal presentations (case-level evidence). (gonzalezgordillo2023joubertsyndromea pages 1-2)
- **Renal replacement therapy** options include PD, HD, and transplantation with generally feasible outcomes (small cohort evidence). (takagi2021anymodalityof pages 1-2)

**Suggested MAXO terms (examples):**
- Physical therapy: **MAXO:0000011** (physical therapy)
- Occupational therapy: **MAXO:0000012**
- Speech therapy: **MAXO:0000013**
- Genetic counseling: **MAXO:0000117**
- Kidney transplantation: **MAXO:0001175**
- Peritoneal dialysis: **MAXO:0000555**
- Hemodialysis: **MAXO:0000556**

#### 12.3 Experimental / clinical-trial landscape
- **NCT00873678 (completed; observational; AP-HP):** aimed to assess prevalence and mutational spectrum for **AHI1, NPHP1, CEP290** and evaluate genotype–phenotype correlations in JS. (NCT00873678 chunk 1)
- **NCT04874909 (CILLICORIRCM; interventional diagnostic/biomarker):** aims to identify prognostic biomarkers (multi-omics; patient-derived kidney models such as urine-derived renal epithelial cells and iPSC-derived organoids) to predict renal impairment progression in ciliopathies including JS. (NCT04874909 chunk 1)


### 13. Prevention
**Primary prevention:** not applicable (genetic).

**Secondary/tertiary prevention:**
- Prevention of complications relies on **early diagnosis** and structured multisystem surveillance guided by genotype–phenotype correlations (e.g., closer liver monitoring for TMEM67; renal for RPGRIP1L/NPHP1/TMEM237; retinal for CEP290/AHI1). (gana2022genotype–phenotypecorrelatesin pages 1-2)

**Reproductive options / prenatal diagnosis:**
- Prenatal imaging plus genetic testing (trio-WES) is increasingly used; a 2024 cohort supports first-line WES for prenatal suspected JS based on high detection rate (5/6). (juan2024optimalprenatalgenetic pages 4-6)
- Targeted carrier screening may be warranted in specific populations with enriched alleles (e.g., CPLANE1 complex allele in Albanian couples with recurrent early pregnancy loss; TOPORS p.Pro10Gln in Dominican ancestry). (bozhinovski2024highincidenceof pages 3-5, strong2023toporsasa pages 1-3)


### 14. Other species / natural disease
No naturally occurring non-human JS disease cases were captured in the retrieved evidence. However, comparative biology across species is central to the field because ciliary structure/function is evolutionarily conserved, enabling mechanistic inference from models. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 13-15)


### 15. Model organisms
**Key model systems used in ciliopathy/JS research and phenotypes recapitulated:**
- **Zebrafish:** frequently recapitulate ciliopathy phenotypes relevant to JS–MKS–NPH, including decreased cilia in brain ventricles/kidney structures, retinal degeneration, and pronephric cysts in many models; also laterality and craniofacial phenotypes. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 13-15)
- **Mouse:** primary mammalian model; phenotypes include retinal degeneration, polydactyly, disrupted Hedgehog signaling, laterality defects, fibrocystic kidney disease, craniofacial malformations, and neural developmental defects. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 15-16)
- **C. elegans and Chlamydomonas:** used for genetic screens and foundational intraflagellar transport/ciliary biology discoveries relevant to ciliopathies. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 13-15)


## High-yield evidence map
| Domain | Key data points | Best supporting citations |
|---|---|---|
| Definition | Rare primary ciliopathy/neurodevelopmental disorder defined by hypotonia, developmental delay, and the molar tooth sign (MTS); variable multiorgan involvement | (strong2023toporsasa pages 1-3, dong2023clinicalandgenetic pages 1-2) |
| Epidemiology | Prevalence/incidence commonly cited as 1:80,000–1:100,000 live births; population-based prevalence 1.7/100,000 among ages 0–19 years | (gonzalezgordillo2023joubertsyndromea pages 1-2, gana2022genotype–phenotypecorrelatesin pages 1-2, li2023anovelmutation pages 1-2) |
| Inheritance | Mostly autosomal recessive; rare X-linked recessive and autosomal dominant cases reported | (strong2023toporsasa pages 1-3, gonzalezgordillo2023joubertsyndromea pages 1-2, li2023anovelnonsense pages 1-2) |
| Diagnostic hallmark | MTS = thick/elongated superior cerebellar peduncles + deep interpeduncular fossa + cerebellar vermis hypoplasia/aplasia; MRI hallmark for diagnosis | (strong2023toporsasa pages 1-3, alhashimi2024neuroimagingcharacteristicsas pages 10-11, dong2023clinicalandgenetic media e70ab935) |
| Clinical cohort (36 children) | Developmental delay 94.44% (34/36); typical MTS 86.11% (31/36); ~75% had extra-organ/system involvement; abnormal respiratory rhythm in 7 cases | (dong2023clinicalandgenetic pages 1-2, dong2023clinicalandgenetic pages 3-5) |
| Organ involvement | About two-thirds of patients have extra-CNS involvement; retinal, kidney, liver, and skeletal disease are major non-neurologic domains | (gana2022genotype–phenotypecorrelatesin pages 1-2, li2023anovelmutation pages 1-2, li2023anovelnonsense pages 1-2) |
| Renal involvement cohort (17 cases) | Renal involvement second most common: ESKD 35%, hematuria 29%, proteinuria 29%, diffuse renal lesions 24%, cystic lesions 12%, echogenic parenchyma 12% | (ying2022attentiontorenal pages 1-2) |
| Genetics | >40 causal genes identified; can explain up to 94% of cases, yet 30–40% of clinically diagnosed individuals still lack molecular diagnosis in some series | (gana2022genotype–phenotypecorrelatesin pages 1-2, strong2023toporsasa pages 1-3, dong2023clinicalandgenetic pages 1-2) |
| Recent discovery | TOPORS proposed as novel JBTS gene; homozygous p.Pro10Gln found in Dominican ancestry, with biobank evidence of elevated carrier frequency/founder effect concern | (strong2023toporsasa pages 1-3, strong2023toporsasa pages 3-4) |
| Diagnostic yields | Prenatal posterior fossa malformation cohort: WES diagnostic rate 83.33% (5/6) in fetuses with Joubert syndrome; authors recommend WES first-line for prenatal JS | (juan2024optimalprenatalgenetic pages 4-6) |
| Population/founder signals | Early pregnancy loss products of conception: CPLANE1-related JS incidence 2.03% overall (5/246), 6.25% in Albanian families; targeted screening suggested in this population | (bozhinovski2024highincidenceof pages 3-5) |
| Management & outcomes | No disease-specific cure; multidisciplinary surveillance/rehab recommended. In 11 JS patients on renal replacement therapy: PD in 7, HD in 2, kidney transplant in 8 patients/9 grafts; 1 graft failure; all alive except 1 death from hepatic failure | (wei2024novelcompoundheterozygous pages 6-7, takagi2021anymodalityof pages 1-2, gonzalezgordillo2023joubertsyndromea pages 1-2) |
| Gene–phenotype correlations | TMEM67 → higher liver fibrosis risk; NPHP1/RPGRIP1L/TMEM237 → renal involvement; CEP290 and AHI1 → retinal dystrophy risk, CEP290 also CKD risk | (gana2022genotype–phenotypecorrelatesin pages 1-2) |


*Table: This table summarizes high-yield facts about Joubert syndrome across epidemiology, inheritance, diagnosis, organ involvement, genetics, recent discoveries, and outcomes. It is designed as a compact evidence map with direct links to the strongest supporting context IDs.*


## Notes on evidence gaps (important for knowledge-base curation)
1. **Ontology identifiers (MONDO/Orphanet/MeSH/ICD)** were not directly retrieved by the current tool calls; they should be filled from authoritative resources (OMIM, Orphanet, MeSH, ICD-11 browser) in a subsequent curation pass.
2. **PMIDs** were not available in the retrieved text extracts; therefore, this report cites DOI/URL-bearing sources and ClinicalTrials.gov identifiers as available.
3. Quality-of-life instruments and large prospective natural history survival statistics were not captured in the retrieved evidence; current outcome statements rely on cohorts (36-child clinical cohort; 11-patient renal-replacement cohort; 17-child renal cohort). (dong2023clinicalandgenetic pages 1-2, takagi2021anymodalityof pages 1-2, ying2022attentiontorenal pages 1-2)

References

1. (strong2023toporsasa pages 1-3): Alanna Strong, Hui‐Qi Qu, Sinéad Cullina, Morgan L. McManus, Elaine H. Zackai, Joseph Glessner, Eimear E. Kenny, and Hakon Hakonarson. Topors as a novel causal gene for joubert syndrome. American Journal of Medical Genetics Part A, 191:2156-2163, May 2023. URL: https://doi.org/10.1002/ajmg.a.63303, doi:10.1002/ajmg.a.63303. This article has 5 citations.

2. (dong2023clinicalandgenetic pages 1-2): Yan Dong, Ke Zhang, He Yao, Tianming Jia, Jun Wang, Dengna Zhu, Falin Xu, Meiying Cheng, Shichao Zhao, and Xiaoyi Shi. Clinical and genetic characteristics of 36 children with joubert syndrome. Frontiers in Pediatrics, Jul 2023. URL: https://doi.org/10.3389/fped.2023.1102639, doi:10.3389/fped.2023.1102639. This article has 16 citations.

3. (li2023anovelnonsense pages 1-2): Chen Li, Xingwang Wang, Fake Li, Hongke Ding, Ling Liu, Ying Xiong, Chaoxiang Yang, Yan Zhang, Jing Wu, and Aihua Yin. A novel non-sense variant in the ofd1 gene caused joubert syndrome. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2022.1064762, doi:10.3389/fgene.2022.1064762. This article has 6 citations and is from a peer-reviewed journal.

4. (alhashimi2024neuroimagingcharacteristicsas pages 10-11): Israa Alhashimi, Sohaib Zoghoul, Sondos K Khalil, Zahra B Yousif, Ammar Jumah, and Yaman Alkailani. Neuroimaging characteristics as diagnostic tools in joubert syndrome and related disorders: a case report and literature review. Cureus, Sep 2024. URL: https://doi.org/10.7759/cureus.69872, doi:10.7759/cureus.69872. This article has 4 citations.

5. (NCT00873678 chunk 1):  Assessment of the Prevalence of Genes AHI1, NPHP1 and CEP290 in Joubert Syndrome. Assistance Publique - Hôpitaux de Paris. 2007. ClinicalTrials.gov Identifier: NCT00873678

6. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 1-3): Julie C. Van De Weghe, Arianna Gomez, and Dan Doherty. The joubert–meckel–nephronophthisis spectrum of ciliopathies. Annual Review of Genomics and Human Genetics, 23:301-329, Aug 2022. URL: https://doi.org/10.1146/annurev-genom-121321-093528, doi:10.1146/annurev-genom-121321-093528. This article has 73 citations and is from a domain leading peer-reviewed journal.

7. (gana2022genotype–phenotypecorrelatesin pages 1-2): Simone Gana, Valentina Serpieri, and Enza Maria Valente. Genotype–phenotype correlates in joubert syndrome: a review. American Journal of Medical Genetics. Part C, Seminars in Medical Genetics, 190:72-88, Mar 2022. URL: https://doi.org/10.1002/ajmg.c.31963, doi:10.1002/ajmg.c.31963. This article has 125 citations.

8. (gonzalezgordillo2023joubertsyndromea pages 1-2): Carla I. González-Gordillo, Leslie E. Orozco-Soto, Juan R. Osegueda-Mayen, Alejandra Nava-Tapia, and Dario Martinez-Monreal. Joubert syndrome: a case report of neonatal presentation and early diagnosis. Boletín Médico del Hospital Infantil de México, Jul 2023. URL: https://doi.org/10.24875/bmhim.22000075, doi:10.24875/bmhim.22000075. This article has 3 citations.

9. (bozhinovski2024highincidenceof pages 3-5): Gjorgji Bozhinovski, Marija Terzikj, Katerina Kubelka-Sabit, and Dijana Plaseska-Karanfilska. High incidence of cplane1-related joubert syndrome in the products of conceptions from early pregnancy losses. Balkan Medical Journal, pages 97-104, Mar 2024. URL: https://doi.org/10.4274/balkanmedj.galenos.2024.2023-10-72, doi:10.4274/balkanmedj.galenos.2024.2023-10-72. This article has 6 citations.

10. (li2023anovelmutation pages 1-2): Qian Li, Qianying Liu, Suwen Liu, Lichun Yu, Zhenle Yang, Cong Wang, Jing Wang, and Shuzhen Sun. A novel mutation of the rpgrip1l gene in a chinese boy with joubert syndrome with oculorenal involvement. BMC Pediatrics, Nov 2023. URL: https://doi.org/10.1186/s12887-023-04415-1, doi:10.1186/s12887-023-04415-1. This article has 1 citations and is from a peer-reviewed journal.

11. (dong2023clinicalandgenetic pages 3-5): Yan Dong, Ke Zhang, He Yao, Tianming Jia, Jun Wang, Dengna Zhu, Falin Xu, Meiying Cheng, Shichao Zhao, and Xiaoyi Shi. Clinical and genetic characteristics of 36 children with joubert syndrome. Frontiers in Pediatrics, Jul 2023. URL: https://doi.org/10.3389/fped.2023.1102639, doi:10.3389/fped.2023.1102639. This article has 16 citations.

12. (ying2022attentiontorenal pages 1-2): Liang Ying, Wang Hui, FuQian, Zhou Nan, Jiang Yeping, and Mi Lan. Attention to renal involvement: report of 17 joubert syndrome cases in children of a single center in china. BMC Pediatrics, Jul 2022. URL: https://doi.org/10.1186/s12887-022-03496-8, doi:10.1186/s12887-022-03496-8. This article has 7 citations and is from a peer-reviewed journal.

13. (strong2023toporsasa pages 3-4): Alanna Strong, Hui‐Qi Qu, Sinéad Cullina, Morgan L. McManus, Elaine H. Zackai, Joseph Glessner, Eimear E. Kenny, and Hakon Hakonarson. Topors as a novel causal gene for joubert syndrome. American Journal of Medical Genetics Part A, 191:2156-2163, May 2023. URL: https://doi.org/10.1002/ajmg.a.63303, doi:10.1002/ajmg.a.63303. This article has 5 citations.

14. (wei2024novelcompoundheterozygous pages 6-7): Caichuan Wei, Haiju Zhang, Miaoying Fu, Jingping Ye, and Baozhen Yao. Novel compound heterozygous variants in the cspp1 gene causes joubert syndrome: case report and literature review of the cspp1 gene’s pathogenic mechanism. Frontiers in Pediatrics, Mar 2024. URL: https://doi.org/10.3389/fped.2024.1305754, doi:10.3389/fped.2024.1305754. This article has 4 citations.

15. (juan2024optimalprenatalgenetic pages 4-6): Zhang Juan, Cui-Xia Guo, Yuanjie Cui, Liu Yan, Yao Ling, Tiejuan Zhang, Wang Li, Jijing Han, Guohui Zhang, Yousheng Yan, Qingqing Wu, and Lijuan Sun. Optimal prenatal genetic diagnostic approach for posterior fossa malformation: karyotyping, copy number variant testing, or whole-exome sequencing? European Journal of Medical Research, Jul 2024. URL: https://doi.org/10.1186/s40001-024-01993-3, doi:10.1186/s40001-024-01993-3. This article has 3 citations and is from a peer-reviewed journal.

16. (dabrusco2023exploringthenoncoding pages 106-110): F D'Abrusco. Exploring the non-coding regions of the genome: the contribution of cryptic splicing variants to the onset of joubert syndrome. Unknown journal, 2023.

17. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 13-15): Julie C. Van De Weghe, Arianna Gomez, and Dan Doherty. The joubert–meckel–nephronophthisis spectrum of ciliopathies. Annual Review of Genomics and Human Genetics, 23:301-329, Aug 2022. URL: https://doi.org/10.1146/annurev-genom-121321-093528, doi:10.1146/annurev-genom-121321-093528. This article has 73 citations and is from a domain leading peer-reviewed journal.

18. (weghe2022thejoubert–meckel–nephronophthisisspectrum pages 15-16): Julie C. Van De Weghe, Arianna Gomez, and Dan Doherty. The joubert–meckel–nephronophthisis spectrum of ciliopathies. Annual Review of Genomics and Human Genetics, 23:301-329, Aug 2022. URL: https://doi.org/10.1146/annurev-genom-121321-093528, doi:10.1146/annurev-genom-121321-093528. This article has 73 citations and is from a domain leading peer-reviewed journal.

19. (wang2024zebrafishasa pages 1-2): Fan Wang and Fei Zhao. Zebrafish as a model for studying ciliary development and disease. International Journal of Marine Science, Jan 2024. URL: https://doi.org/10.5376/ijms.2024.14.0037, doi:10.5376/ijms.2024.14.0037. This article has 2 citations.

20. (NCT04874909 chunk 1):  Classification, Functional Stratification and Biomarkers in Ciliopathy (CILLICORIRCM). Assistance Publique - Hôpitaux de Paris. 2021. ClinicalTrials.gov Identifier: NCT04874909

21. (dong2023clinicalandgenetic media e70ab935): Yan Dong, Ke Zhang, He Yao, Tianming Jia, Jun Wang, Dengna Zhu, Falin Xu, Meiying Cheng, Shichao Zhao, and Xiaoyi Shi. Clinical and genetic characteristics of 36 children with joubert syndrome. Frontiers in Pediatrics, Jul 2023. URL: https://doi.org/10.3389/fped.2023.1102639, doi:10.3389/fped.2023.1102639. This article has 16 citations.

22. (takagi2021anymodalityof pages 1-2): Yoko Takagi, Kenichiro Miura, Tomoo Yabuuchi, Naoto Kaneko, Kiyonobu Ishizuka, Mariko Takei, Chikage Yajima, Yuka Ikeuchi, Yasuko Kobayashi, Takumi Takizawa, Masataka Hisano, Yoshinori Tsurusaki, Naomichi Matsumoto, and Motoshi Hattori. Any modality of renal replacement therapy can be a treatment option for joubert syndrome. Scientific Reports, Jan 2021. URL: https://doi.org/10.1038/s41598-020-80712-4, doi:10.1038/s41598-020-80712-4. This article has 6 citations and is from a peer-reviewed journal.
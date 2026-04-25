---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-24T14:44:45.302453'
end_time: '2026-04-24T14:58:31.436379'
duration_seconds: 826.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Episodic Ataxia
  mondo_id: ''
  category: Mendelian
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
- **Disease Name:** Episodic Ataxia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Episodic Ataxia** covering all of the
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
- **Disease Name:** Episodic Ataxia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Episodic Ataxia** covering all of the
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


# Episodic Ataxia (EA) — Comprehensive Disease Characteristics Report (Mendelian)

## Target Disease
- **Disease name:** Episodic ataxia (EA) / Hereditary episodic ataxia
- **Category:** Mendelian (predominantly autosomal dominant)
- **MONDO ID:** **MONDO:0016227** (“hereditary episodic ataxia”) (hassan2023episodicataxiasprimary pages 15-16)

## Executive overview
Episodic ataxia (EA) comprises rare, usually autosomal-dominant disorders characterized by recurrent attacks of cerebellar dysfunction (e.g., gait/limb ataxia, dysarthria, vertigo), with variable attack duration and frequency, and often with interictal findings (e.g., myokymia or nystagmus). (hassan2023episodicataxiasprimary pages 1-2, pilotto2024hereditaryataxiasfrom pages 8-10) A recent classification approach emphasizes describing EA by clinical attack features and interictal signs (Axis 1) plus etiology (Axis 2; inherited vs acquired and neuroimaging features). (hassan2023episodicataxiasprimary pages 15-16)

A key point for real-world practice is that **many primary (genetic) and secondary EA mimics are treatable**, making cause-finding clinically actionable. (hassan2023episodicataxiasprimary pages 12-13, hassan2023episodicataxiasprimary pages 1-2)


---

## 1. Disease information

### 1.1 Definition and current understanding
- EA is described as **“rare autosomal dominant disorders with recurrent attacks of cerebellar dysfunction”**. (hassan2023episodicataxiasprimary pages 1-2)
- A 2024 review similarly defines EA as **“a rare group of autosomal-dominant inherited disorders”** with recurrent cerebellar dysfunction. (pilotto2024hereditaryataxiasfrom pages 8-10)

### 1.2 Key identifiers (as available in retrieved sources)
- **Hereditary episodic ataxia:** MONDO:0016227 (hassan2023episodicataxiasprimary pages 15-16)
- **EA1:** OMIM **#160120** (pilotto2024hereditaryataxiasfrom pages 8-10)
- **EA2:** OMIM **#108500** (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7, pilotto2024hereditaryataxiasfrom pages 8-10)
- **Other ontology/identifier mappings** (Orphanet ID, ICD-10/ICD-11 codes, MeSH): **not found in retrieved sources**.

### 1.3 Synonyms / alternative names (from retrieved sources)
- “Episodic ataxia” and “paroxysmal ataxia” are used as search/descriptor terms in a 2023 systematic review of the topic. (hassan2023episodicataxiasprimary pages 15-16)
- “Familial episodic ataxia with nystagmus” is used in the context of a randomized trial in EA2 and related familial episodic ataxias. (strupp2011arandomizedtrial pages 1-2)

### 1.4 Evidence sources
The retrieved evidence is predominantly **aggregated disease-level resources** (systematic/narrative reviews and trial reports), supplemented by **human clinical cohort** data (e.g., cognition in EA2) and **functional electrophysiology** studies for gene expansion of the episodic ataxia phenotype (e.g., SCN8A). (kim2024intellectualdisabilityin pages 1-2, lyu2023clinicalandelectrophysiological pages 1-2)


---

## 2. Etiology

### 2.1 Disease causal factors
**Primary genetic (Mendelian) causes (core, gene-defined EAs):**
- EA1 — **KCNA1** (Kv1.1 voltage-gated potassium channel). (hassan2023episodicataxiasprimary pages 4-6, pilotto2024hereditaryataxiasfrom pages 8-10)
- EA2 — **CACNA1A** (Cav2.1 P/Q-type voltage-gated calcium channel α1A subunit). (hassan2023episodicataxiasprimary pages 4-6, indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7, pilotto2024hereditaryataxiasfrom pages 8-10)
- Additional gene-defined subtypes highlighted in 2023–2024 reviews: **CACNB4 (EA5)**, **SLC1A3 (EA6)**, **UBR4 (EA8)**. (hassan2023episodicataxiasprimary pages 12-13, pilotto2024hereditaryataxiasfrom pages 8-10)

**Secondary/acquired and mimic etiologies:**
Secondary causes (vascular, inflammatory, toxic–metabolic) and phenocopies can be more common than “primary” EA in general neurology settings, and EA may be misdiagnosed as migraine, vestibular disorders, anxiety, or functional symptoms. (hassan2023episodicataxiasprimary pages 1-2)

### 2.2 Risk factors
- **Genetic:** autosomal dominant inheritance is typical; de novo variants occur (e.g., KCNA1 de novo noted in EA1 context). (hassan2023episodicataxiasprimary pages 2-4)
- **Attack-triggering factors (often acting as precipitants rather than disease-causing risks):** exercise, emotional stress, heat, fever, menstruation, caffeine, alcohol; also reported are sudden movement/kinesigenic triggers and startle. (hassan2023episodicataxiasprimary pages 1-2, hassan2023episodicataxiasprimary pages 2-4)

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
While formal GxE studies were not retrieved, multiple reviews emphasize that physiologic and environmental stressors (exercise, fever/heat, caffeine/alcohol) can trigger attacks, implying that the clinical phenotype emerges from interaction between an underlying channelopathy and state-dependent excitability changes. (hassan2023episodicataxiasprimary pages 1-2, hassan2023episodicataxiasprimary pages 2-4, hassan2023episodicataxiasprimary pages 6-7)


---

## 3. Phenotypes

### 3.1 Core phenotype (umbrella EA)
- Attacks may range from seconds/minutes to hours/days, and frequency may range from multiple per day to monthly; gait impairment may range from mild to inability to walk during attacks. (hassan2023episodicataxiasprimary pages 2-4)

### 3.2 EA1 phenotype (KCNA1)
**Typical features (human clinical):**
- Classical feature: **constant myokymia** affecting “almost all” patients in classic descriptions. (hassan2023episodicataxiasprimary pages 1-2)
- Onset: typically childhood; one review reports mean onset ~7.8 years (not restricted to EA1 only, but presented in EA context with childhood predominance). (hassan2023episodicataxiasprimary pages 1-2)
- Attack duration: typically seconds to minutes. (pilotto2024hereditaryataxiasfrom pages 8-10)
- Triggers: exercise and other physiological stressors. (hassan2023episodicataxiasprimary pages 2-4)

**Suggested HPO terms (examples):**
- Episodic ataxia (HP:0002135), Gait ataxia (HP:0002066), Dysarthria (HP:0001260)
- Myokymia (HP:0002353)

### 3.3 EA2 phenotype (CACNA1A)
**Defining features and frequencies (human clinical):**
- EA2 is described as the most common hereditary EA. (hassan2023episodicataxiasprimary pages 4-6)
- Attacks: “intermittent spells of ataxia and dysarthria lasting several hours, possibly up to 2–3 days.” (hassan2023episodicataxiasprimary pages 4-6)
- Interictal findings: “interictal nystagmus between attacks” is a distinguishing feature and is used diagnostically. (hassan2023episodicataxiasprimary pages 4-6, hassan2023episodicataxiasprimary pages 6-7)
- Triggers: “emotional or physiological stress, exercise, alcohol and caffeine.” (hassan2023episodicataxiasprimary pages 4-6)
- Migraine comorbidity: “reported in up to 50% of cases.” (hassan2023episodicataxiasprimary pages 4-6)

**Neuropsychiatric/cognitive features (2024 cohort):**
A 2019–2023 Korean multicenter cohort of **13 genetically confirmed EA2** patients found substantial cognitive impact: **38.5%** met criteria for intellectual disability (FSIQ ≤69), **7.7%** borderline (70–79), and **38.5%** low average (80–89). (kim2024intellectualdisabilityin pages 1-2)

**Suggested HPO terms (examples):**
- Episodic ataxia (HP:0002135), Vertigo (HP:0002321), Nystagmus (HP:0000639)
- Downbeat nystagmus (HP:0000630), Gaze-evoked nystagmus (HP:0000612)
- Migraine (HP:0002076)
- Intellectual disability (HP:0001249)

### 3.4 Expanded/atypical episodic ataxia phenotypes (gene discovery and pleiotropy)
- EA-like presentations are increasingly recognized across a broader genetic landscape (e.g., epilepsy genes and other ataxia genes), complicating diagnosis but enabling precision treatment when identified. (hassan2023episodicataxiasprimary pages 12-13, hassan2023episodicataxiasprimary pages 1-2)
- Example: **SCN8A** variants can cause episodic or chronic ataxia; in a cohort of **10 individuals from 9 families**, several variants produced loss-of-function electrophysiological profiles, and sodium channel blockers worsened symptoms in 4 individuals. (lyu2023clinicalandelectrophysiological pages 1-2, lyu2023clinicalandelectrophysiological pages 4-6)

### 3.5 Quality of life impact
Direct quality-of-life quantification in EA2 is supported by the randomized trial showing improvement in a vestibular/daily-life score (VDADL) with 4-aminopyridine. (strupp2011arandomizedtrial pages 1-2)


---

## 4. Genetic / molecular information

### 4.1 Causal genes (core)
- **KCNA1 (EA1)** and **CACNA1A (EA2)** are consistently emphasized as the most frequent/encountered genetic causes. (hassan2023episodicataxiasprimary pages 1-2, pilotto2024hereditaryataxiasfrom pages 8-10)
- **CACNB4 (EA5), SLC1A3 (EA6), UBR4 (EA8)** are additional gene-defined EA entities emphasized in 2023–2024 summaries. (hassan2023episodicataxiasprimary pages 12-13, pilotto2024hereditaryataxiasfrom pages 8-10)

### 4.2 Variant types and functional consequences
- **EA1 / KCNA1:** primarily missense variants with **loss-of-function** mechanisms; one review notes “63 KCNA1 pathogenic mutations are reported on OMIM” and that “over half of KCNA1 variants result in EA1.” (hassan2023episodicataxiasprimary pages 4-6)
- **EA2 / CACNA1A:** commonly linked to **loss-of-function** variants; multiple sources emphasize truncating/nonsense/frameshift variants leading to premature stop codons or other frame-interrupting events. (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7, pilotto2024hereditaryataxiasfrom pages 8-10)
- **Penetrance:** CACNA1A mutations in EA2 are reported as having **high but incomplete penetrance (80–90%)**. (hassan2023episodicataxiasprimary pages 4-6)

### 4.3 Modifier genes / protective variants
- A potential modifier was described in a multi-omics ataxia cohort (modifier of an ATXN2 expansion in **ZFYVE26**), illustrating how multi-omics can reveal candidate modifiers in complex ataxia presentations; this was not specific to canonical EA1/EA2. (audet2024integrationofmultiomics pages 2-3)

### 4.4 Epigenetic information / chromosomal abnormalities
Not identified in the retrieved sources.


---

## 5. Environmental information

### 5.1 Environmental and lifestyle factors influencing attacks
Attack triggers commonly include **exercise, emotional stress, heat/fever, menstruation, caffeine, and alcohol**. (hassan2023episodicataxiasprimary pages 1-2, hassan2023episodicataxiasprimary pages 2-4, hassan2023episodicataxiasprimary pages 6-7)

### 5.2 Infectious agents
No infectious causal agents were identified; fever is described as a trigger rather than a cause. (hassan2023episodicataxiasprimary pages 1-2)


---

## 6. Mechanism / pathophysiology

### 6.1 EA as cerebellar channelopathy with network consequences
Most identified EA genes encode ion channels (exception noted for UBR4), supporting EA as a channelopathy-driven cerebellar network disorder. (hassan2023episodicataxiasprimary pages 1-2, pilotto2024hereditaryataxiasfrom pages 8-10)

### 6.2 EA1 (KCNA1) mechanistic concepts
Kv1.1 is abundant in multiple CNS regions including cerebellum, and dysfunction is linked to cerebellar interneuron hyperexcitability with downstream Purkinje cell effects in a review synthesis. (hassan2023episodicataxiasprimary pages 4-6)

### 6.3 EA2 (CACNA1A) mechanistic concepts and causal chain
**Upstream molecular defect:** CACNA1A loss-of-function leading to reduced P/Q-type channel function in the cerebellum. (hassan2023episodicataxiasprimary pages 6-7)

**Cellular physiology:** A key mechanistic model is that P/Q-type Ca2+ channel dysfunction impairs Purkinje cell firing precision/pacemaking, contributing to episodic motor dysfunction. (alvina2010thetherapeuticmode pages 1-2, alvina2010thetherapeuticmode pages 5-6)

**Therapeutic mechanism evidence (4-aminopyridine):**
A mechanistic study in an EA2 mouse model (tg/tg) reports that, contrary to a simplistic “increase firing rate” hypothesis, therapeutic concentrations of 4-aminopyridine do not increase Purkinje firing rate. (alvina2010thetherapeuticmode pages 2-3, alvina2010thetherapeuticmode pages 1-2) Instead, 4-aminopyridine **restores precision of Purkinje pacemaking** by prolonging action potentials and increasing afterhyperpolarization, with Kv1 family channels (possibly Kv1.5) suggested as likely targets at therapeutic doses. (alvina2010thetherapeuticmode pages 1-2, alvina2010thetherapeuticmode pages 5-6)

### 6.4 Suggested ontology terms
**GO biological process (suggested):**
- Regulation of membrane potential; synaptic transmission; regulation of neuron firing; motor coordination

**CL cell types (suggested):**
- Cerebellar Purkinje cell (CL term concept), cerebellar molecular layer interneuron (concept), deep cerebellar nuclei neuron (concept)


---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- Primary: central nervous system; cerebellar dysfunction is core. (hassan2023episodicataxiasprimary pages 1-2, pilotto2024hereditaryataxiasfrom pages 8-10)

### 7.2 Tissue/cell level
- Cerebellar circuitry implicating Purkinje cells is emphasized, particularly for EA2 pathophysiology and treatment mechanism. (alvina2010thetherapeuticmode pages 1-2, alvina2010thetherapeuticmode pages 5-6)

### 7.3 Suggested UBERON terms (examples)
- Cerebellum (UBERON concept), Cerebellar cortex (UBERON concept), Cerebellar vermis (UBERON concept; atrophy mentioned as an imaging feature in phenotype tables). (szymanowicz2024areviewof pages 5-6)


---

## 8. Temporal development

### 8.1 Onset
- EA often begins in childhood; EA1 onset reported around childhood with mean 7.8 years in a review context. (hassan2023episodicataxiasprimary pages 1-2)
- EA2 onset is commonly within the first two decades (reported 2–20 years), though late-onset cases exist. (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7, pilotto2024hereditaryataxiasfrom pages 8-10)

### 8.2 Course/progression
- Although attacks are episodic, reviews note that attacks “may leave permanent cerebellar signs” and that interictal deficits can exist. (hassan2023episodicataxiasprimary pages 12-13)


---

## 9. Inheritance and population

### 9.1 Inheritance
- Most core EA entities are **autosomal dominant**. (hassan2023episodicataxiasprimary pages 1-2, pilotto2024hereditaryataxiasfrom pages 8-10)

### 9.2 Epidemiology (available estimates)
- Incidence/prevalence estimates reported in reviews are consistently **<1 per 100,000** (and likely underestimated). (hassan2023episodicataxiasprimary pages 1-2, pilotto2024hereditaryataxiasfrom pages 8-10)

### 9.3 Population/variant distribution, founder effects
Not identified in the retrieved sources.


---

## 10. Diagnostics

### 10.1 Clinical approach
- Diagnostic evaluation integrates clinical characterization (attack duration, triggers, interictal findings such as myokymia/nystagmus), neuroimaging, and EEG (including EEG during provoked attacks in some contexts). (hassan2023episodicataxiasprimary pages 12-13)
- EA2 is “usually distinguished from other EAs by attack duration and interictal nystagmus.” (hassan2023episodicataxiasprimary pages 6-7)

### 10.2 Genetic testing strategy (current practice trends)
- For “classical” EA1/EA2 phenotypes: **single-gene testing** for KCNA1 or CACNA1A is suggested as a straightforward pathway. (hassan2023episodicataxiasprimary pages 12-13, hassan2023episodicataxiasprimary pages 1-2)
- For atypical cases: **multigene panels/NGS/WES** are emphasized. (hassan2023episodicataxiasprimary pages 12-13, hassan2023episodicataxiasprimary pages 1-2)

### 10.3 Recent developments: multi-omics and long-read sequencing
A 2024 Frontiers in Genetics study applied WGS + RNA-seq + long-read sequencing in a cohort referred for episodic ataxia presentations, highlighting that ataxia-causal variant types can include SNPs, SVs, CNVs, repeat expansions, and splicing defects, and that integrated multi-omics can improve diagnostic yield. (audet2024integrationofmultiomics pages 2-3)

### 10.4 Differential diagnosis
EA has substantial overlap with migraine and peripheral vestibular disorders, and can be misdiagnosed as anxiety or functional disorders; secondary causes (vascular, inflammatory, toxic-metabolic) should be considered. (hassan2023episodicataxiasprimary pages 1-2)


---

## 11. Outcome / prognosis

### 11.1 Attack outcomes and chronic burden
- EA2 and other EAs can show interictal findings and may develop chronic features (e.g., persistent nystagmus/vestibular impairment), but explicit survival or long-term mortality statistics were not available in retrieved sources. (hassan2023episodicataxiasprimary pages 6-7)

### 11.2 Treatment-responsive outcome metrics
- In EA2 and related familial episodic ataxias, 4-aminopyridine improved quality-of-life scores and reduced attack frequency in a randomized crossover trial. (strupp2011arandomizedtrial pages 1-2)


---

## 12. Treatment

### 12.1 Pharmacotherapy (current applications and evidence)

**Acetazolamide (carbonic anhydrase inhibitor; commonly first-line for EA2):**
- Reviews and the RCT background note acetazolamide preventive dosing commonly 250–1000 mg/day. (hassan2023episodicataxiasprimary pages 6-7, strupp2011arandomizedtrial pages 1-2)
- Response: “About 50–75% patients report improvement” with acetazolamide in EA2. (hassan2023episodicataxiasprimary pages 6-7)
- Adverse effects described include nephrolithiasis/nephrocalcinosis, paresthesia, fatigue, and GI disturbances. (hassan2023episodicataxiasprimary pages 6-7, strupp2011arandomizedtrial pages 1-2)

**4-aminopyridine (4-AP; potassium channel blocker) — evidence-based symptomatic prevention in EA2:**
- A 2011 randomized double-blind placebo-controlled crossover trial (Neurology; DOI in retrieved text) tested 4-AP 5 mg three times daily in 10 subjects (7 genetically confirmed EA2). (strupp2011arandomizedtrial pages 1-2)
- Quantitative outcomes:
  - Median monthly attack frequency: **6.50 (placebo) → 1.65 (4-AP)** (p=0.03). (strupp2011arandomizedtrial pages 1-2)
  - Median monthly attack duration: **13.65 h → 4.45 h** (p=0.08). (strupp2011arandomizedtrial pages 1-2)
  - VDADL score: **6.00 → 1.50** (p=0.02). (strupp2011arandomizedtrial pages 1-2)
- Expert interpretation in later review: 4-AP “is also effective, reducing the number of attacks and improving quality of life in an RCT.” (hassan2023episodicataxiasprimary pages 6-7)

**Fampridine / dalfampridine (slow-release 4-AP formulations):**
- A 2023 review highlights slow-release formulations (dalfampridine/fampridine) as effective for EA2 and states: “Fampridine had fewer side effects than acetazolamide.” (hassan2023episodicataxiasprimary pages 6-7)

**EA1 symptomatic management (antiseizure medications):**
- A 2023 review notes that “A variety of antiseizure medications can diminish attacks, including carbamazepine, phenytoin, and lamotrigine,” and that acetazolamide may help in rare cases. (hassan2023episodicataxiasprimary pages 4-6)

### 12.2 MAXO and CHEBI term suggestions (for knowledge base tagging)
- **Acetazolamide therapy** (MAXO concept); CHEBI: acetazolamide (CHEBI concept)
- **4-aminopyridine therapy / potassium channel blocker therapy** (MAXO concept); CHEBI: 4-aminopyridine (CHEBI concept)

### 12.3 Experimental/clinical trials
- ClinicalTrials.gov entry retrieved: **NCT01543750** “4-Aminopyridine in Episodic Ataxia Type 2” (Phase 2), status **Withdrawn**, enrollment 0. (NCT01543750 chunk 1)


---

## 13. Prevention

### 13.1 Primary prevention
No primary prevention exists for inherited EA1/EA2 beyond reproductive/genetic counseling.

### 13.2 Secondary/tertiary prevention
- Reviews emphasize that EA is “highly treatable” and that early recognition and management are important; the 2024 EA2 cognition cohort concludes that early diagnosis/management may help prevent “irreversible brain dysfunction.” (hassan2023episodicataxiasprimary pages 1-2, kim2024intellectualdisabilityin pages 1-2)


---

## 14. Other species / natural disease
No naturally occurring animal disease analogs were identified in the retrieved sources.


---

## 15. Model organisms
A mechanistic EA2 mouse model (tg/tg; described as carrying a spontaneous mutation in the pore-forming P/Q-type Ca2+ channel subunit) is used to study Purkinje pacemaking irregularity and pharmacologic rescue by 4-aminopyridine and chlorzoxazone. (alvina2010thetherapeuticmode pages 5-6)


---

## Summary artifact: identifiers and subtype mapping

| Disease name | Subtype | OMIM number | MONDO | Causal gene(s) | Brief defining features | Key citations |
|---|---|---|---|---|---|---|
| Hereditary episodic ataxia | Umbrella disorder | not found in retrieved sources | MONDO:0016227 | KCNA1, CACNA1A, CACNB4, SLC1A3, UBR4; additional genes proposed/associated in atypical EA presentations | Rare autosomal-dominant group with recurrent attacks of cerebellar dysfunction; estimated prevalence/incidence reported as <1:100,000; EA1 and EA2 are the most common forms (hassan2023episodicataxiasprimary pages 1-2, pilotto2024hereditaryataxiasfrom pages 8-10) | Hassan 2023-03, *Tremor and Other Hyperkinetic Movements*, https://doi.org/10.5334/tohm.747 (hassan2023episodicataxiasprimary pages 1-2); Pilotto et al. 2024-02, *Cells*, https://doi.org/10.3390/cells13040319 (pilotto2024hereditaryataxiasfrom pages 8-10) |
| Episodic ataxia type 1 | EA1 | OMIM:160120 | MONDO:0008047 | KCNA1 | Childhood-onset episodic ataxia with attacks usually lasting seconds to minutes; interictal myokymia is characteristic and affects almost all patients in classic descriptions; most KCNA1 variants are missense loss-of-function (hassan2023episodicataxiasprimary pages 1-2, hassan2023episodicataxiasprimary pages 4-6, pilotto2024hereditaryataxiasfrom pages 8-10) | Pilotto et al. 2024-02, *Cells*, https://doi.org/10.3390/cells13040319 (pilotto2024hereditaryataxiasfrom pages 8-10); Hassan 2023-03, *Tremor and Other Hyperkinetic Movements*, https://doi.org/10.5334/tohm.747 (hassan2023episodicataxiasprimary pages 1-2, hassan2023episodicataxiasprimary pages 4-6) |
| Episodic ataxia type 2 | EA2 | OMIM:108500 | not found in retrieved sources | CACNA1A | Most common hereditary EA; recurrent vertigo/ataxia and dysarthria lasting hours to 2-3 days, often with interictal nystagmus; migraine reported in up to 50%; typically associated with CACNA1A loss-of-function, often truncating/nonsense/frameshift variants (hassan2023episodicataxiasprimary pages 4-6, hassan2023episodicataxiasprimary pages 6-7, indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7, pilotto2024hereditaryataxiasfrom pages 8-10) | Indelicato & Boesch 2023-01, *Handbook of Experimental Pharmacology*, https://doi.org/10.1007/164_2022_625 (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7); Hassan 2023-03, *Tremor and Other Hyperkinetic Movements*, https://doi.org/10.5334/tohm.747 (hassan2023episodicataxiasprimary pages 4-6, hassan2023episodicataxiasprimary pages 6-7); Pilotto et al. 2024-02, *Cells*, https://doi.org/10.3390/cells13040319 (pilotto2024hereditaryataxiasfrom pages 8-10) |
| Episodic ataxia type 3 | EA3 | not found in retrieved sources | MONDO:0011682 | not found in retrieved sources | Reported rare familial episodic ataxia subtype; gene not established in retrieved evidence (hassan2023episodicataxiasprimary pages 6-7) | Hassan 2023-03, *Tremor and Other Hyperkinetic Movements*, https://doi.org/10.5334/tohm.747 (hassan2023episodicataxiasprimary pages 6-7) |
| Episodic ataxia type 5 | EA5 | not found in retrieved sources | MONDO:0013464 | CACNB4 | Rare EA subtype linked to CACNB4 in retrieved reviews; one of the recognized gene-defined EA forms (hassan2023episodicataxiasprimary pages 12-13, pilotto2024hereditaryataxiasfrom pages 8-10, gasser2010efnsguidelineson pages 4-5) | Pilotto et al. 2024-02, *Cells*, https://doi.org/10.3390/cells13040319 (pilotto2024hereditaryataxiasfrom pages 8-10); Hassan 2023-03, *Tremor and Other Hyperkinetic Movements*, https://doi.org/10.5334/tohm.747 (hassan2023episodicataxiasprimary pages 12-13) |
| Episodic ataxia type 6 | EA6 | not found in retrieved sources | not found in retrieved sources | SLC1A3 | Rare EA subtype associated with SLC1A3/EAAT1; included among recognized gene-defined EA disorders in recent reviews (hassan2023episodicataxiasprimary pages 12-13, gasser2010efnsguidelineson pages 4-5) | Hassan 2023-03, *Tremor and Other Hyperkinetic Movements*, https://doi.org/10.5334/tohm.747 (hassan2023episodicataxiasprimary pages 12-13); EFNS guideline 2010-02, *European Journal of Neurology*, https://doi.org/10.1111/j.1468-1331.2009.02873.x (gasser2010efnsguidelineson pages 4-5) |
| Episodic ataxia type 8 | EA8 | not found in retrieved sources | not found in retrieved sources | UBR4 | Rare proposed/recognized subtype; unlike most known EA genes, UBR4 is not an ion-channel gene in retrieved reviews (hassan2023episodicataxiasprimary pages 1-2, pilotto2024hereditaryataxiasfrom pages 8-10) | Hassan 2023-03, *Tremor and Other Hyperkinetic Movements*, https://doi.org/10.5334/tohm.747 (hassan2023episodicataxiasprimary pages 1-2); Pilotto et al. 2024-02, *Cells*, https://doi.org/10.3390/cells13040319 (pilotto2024hereditaryataxiasfrom pages 8-10) |


*Table: This table summarizes the key nomenclature and identifier information for hereditary episodic ataxia and major subtypes, integrating OMIM and available MONDO IDs with causal genes and concise phenotype definitions. It is useful as a compact reference for disease knowledge base curation and cross-resource mapping.*


---

## Notes on evidence gaps vs template requirements
- **Orphanet IDs, ICD-10/ICD-11 codes, and MeSH identifiers** for episodic ataxia/EA1/EA2 were **not present** in the retrieved literature excerpts; additional database-specific queries would be required to populate those fields.
- Several key 2023–2024 sources in the retrieval set provide robust clinical and genetic summaries, but **many excerpts do not include PMIDs**; therefore, citations here are to retrieved full-text evidence snippets (pqac IDs) with DOIs/URLs and publication months/years when provided in the retrieved metadata.


References

1. (hassan2023episodicataxiasprimary pages 15-16): Anhar Hassan. Episodic ataxias: primary and secondary etiologies, treatment, and classification approaches. Tremor and Other Hyperkinetic Movements, Mar 2023. URL: https://doi.org/10.5334/tohm.747, doi:10.5334/tohm.747. This article has 31 citations and is from a peer-reviewed journal.

2. (hassan2023episodicataxiasprimary pages 1-2): Anhar Hassan. Episodic ataxias: primary and secondary etiologies, treatment, and classification approaches. Tremor and Other Hyperkinetic Movements, Mar 2023. URL: https://doi.org/10.5334/tohm.747, doi:10.5334/tohm.747. This article has 31 citations and is from a peer-reviewed journal.

3. (pilotto2024hereditaryataxiasfrom pages 8-10): Federica Pilotto, Andrea Del Bondio, and Hélène Puccio. Hereditary ataxias: from bench to clinic, where do we stand? Cells, 13:319, Feb 2024. URL: https://doi.org/10.3390/cells13040319, doi:10.3390/cells13040319. This article has 23 citations.

4. (hassan2023episodicataxiasprimary pages 12-13): Anhar Hassan. Episodic ataxias: primary and secondary etiologies, treatment, and classification approaches. Tremor and Other Hyperkinetic Movements, Mar 2023. URL: https://doi.org/10.5334/tohm.747, doi:10.5334/tohm.747. This article has 31 citations and is from a peer-reviewed journal.

5. (indelicato2023cacna1arelatedchannelopathiesclinical pages 4-7): Elisabetta Indelicato and Sylvia Boesch. Cacna1a-related channelopathies: clinical manifestations and treatment options. Handbook of experimental pharmacology, pages 227-248, Jan 2023. URL: https://doi.org/10.1007/164\_2022\_625, doi:10.1007/164\_2022\_625. This article has 25 citations and is from a peer-reviewed journal.

6. (strupp2011arandomizedtrial pages 1-2): M. Strupp, R. Kalla, J. Claassen, C. Adrion, U. Mansmann, T. Klopstock, T. Freilinger, H. Neugebauer, R. Spiegel, M. Dichgans, F. Lehmann-Horn, K. Jurkat-Rott, T. Brandt, J.C. Jen, and K. Jahn. A randomized trial of 4-aminopyridine in ea2 and related familial episodic ataxias. Neurology, 77:269-275, Jul 2011. URL: https://doi.org/10.1212/wnl.0b013e318225ab07, doi:10.1212/wnl.0b013e318225ab07. This article has 228 citations and is from a highest quality peer-reviewed journal.

7. (kim2024intellectualdisabilityin pages 1-2): Seoyeon Kim, Ji-Soo Kim, Seung-Han Lee, Jae-Myung Kim, Seunghee Na, Jae-Hwan Choi, and Hyo-Jung Kim. Intellectual disability in episodic ataxia type 2: beyond paroxysmal vertigo and ataxia. Journal of Clinical Neurology (Seoul, Korea), 20:563-570, Oct 2024. URL: https://doi.org/10.3988/jcn.2024.0274, doi:10.3988/jcn.2024.0274. This article has 2 citations.

8. (lyu2023clinicalandelectrophysiological pages 1-2): Hang Lyu, Christian M. Boßelmann, Katrine M. Johannesen, Mahmoud Koko, Juan Dario Ortigoza-Escobar, Sergio Aguilera-Albesa, Deyanira Garcia-Navas Núñez, Tarja Linnankivi, Eija Gaily, Henriette J.A. van Ruiten, Ruth Richardson, Cornelia Betzler, Gabriella Horvath, Eva Brilstra, Niels Geerdink, Daniele Orsucci, Alessandra Tessa, Elena Gardella, Zofia Fleszar, Ludger Schöls, Holger Lerche, Rikke S. Møller, and Yuanyuan Liu. Clinical and electrophysiological features of scn8a variants causing episodic or chronic ataxia. eBioMedicine, 98:104855, Dec 2023. URL: https://doi.org/10.1016/j.ebiom.2023.104855, doi:10.1016/j.ebiom.2023.104855. This article has 16 citations and is from a peer-reviewed journal.

9. (hassan2023episodicataxiasprimary pages 4-6): Anhar Hassan. Episodic ataxias: primary and secondary etiologies, treatment, and classification approaches. Tremor and Other Hyperkinetic Movements, Mar 2023. URL: https://doi.org/10.5334/tohm.747, doi:10.5334/tohm.747. This article has 31 citations and is from a peer-reviewed journal.

10. (hassan2023episodicataxiasprimary pages 2-4): Anhar Hassan. Episodic ataxias: primary and secondary etiologies, treatment, and classification approaches. Tremor and Other Hyperkinetic Movements, Mar 2023. URL: https://doi.org/10.5334/tohm.747, doi:10.5334/tohm.747. This article has 31 citations and is from a peer-reviewed journal.

11. (hassan2023episodicataxiasprimary pages 6-7): Anhar Hassan. Episodic ataxias: primary and secondary etiologies, treatment, and classification approaches. Tremor and Other Hyperkinetic Movements, Mar 2023. URL: https://doi.org/10.5334/tohm.747, doi:10.5334/tohm.747. This article has 31 citations and is from a peer-reviewed journal.

12. (lyu2023clinicalandelectrophysiological pages 4-6): Hang Lyu, Christian M. Boßelmann, Katrine M. Johannesen, Mahmoud Koko, Juan Dario Ortigoza-Escobar, Sergio Aguilera-Albesa, Deyanira Garcia-Navas Núñez, Tarja Linnankivi, Eija Gaily, Henriette J.A. van Ruiten, Ruth Richardson, Cornelia Betzler, Gabriella Horvath, Eva Brilstra, Niels Geerdink, Daniele Orsucci, Alessandra Tessa, Elena Gardella, Zofia Fleszar, Ludger Schöls, Holger Lerche, Rikke S. Møller, and Yuanyuan Liu. Clinical and electrophysiological features of scn8a variants causing episodic or chronic ataxia. eBioMedicine, 98:104855, Dec 2023. URL: https://doi.org/10.1016/j.ebiom.2023.104855, doi:10.1016/j.ebiom.2023.104855. This article has 16 citations and is from a peer-reviewed journal.

13. (audet2024integrationofmultiomics pages 2-3): Sebastien Audet, Valerie Triassi, Myriam Gelinas, Nab Legault-Cadieux, Vincent Ferraro, Antoine Duquette, and Martine Tetreault. Integration of multi-omics technologies for molecular diagnosis in ataxia patients. Frontiers in Genetics, Jan 2024. URL: https://doi.org/10.3389/fgene.2023.1304711, doi:10.3389/fgene.2023.1304711. This article has 4 citations and is from a peer-reviewed journal.

14. (alvina2010thetherapeuticmode pages 1-2): Karina Alviña and Kamran Khodakhah. The therapeutic mode of action of 4-aminopyridine in cerebellar ataxia. The Journal of Neuroscience, 30:7258-7268, May 2010. URL: https://doi.org/10.1523/jneurosci.3582-09.2010, doi:10.1523/jneurosci.3582-09.2010. This article has 232 citations.

15. (alvina2010thetherapeuticmode pages 5-6): Karina Alviña and Kamran Khodakhah. The therapeutic mode of action of 4-aminopyridine in cerebellar ataxia. The Journal of Neuroscience, 30:7258-7268, May 2010. URL: https://doi.org/10.1523/jneurosci.3582-09.2010, doi:10.1523/jneurosci.3582-09.2010. This article has 232 citations.

16. (alvina2010thetherapeuticmode pages 2-3): Karina Alviña and Kamran Khodakhah. The therapeutic mode of action of 4-aminopyridine in cerebellar ataxia. The Journal of Neuroscience, 30:7258-7268, May 2010. URL: https://doi.org/10.1523/jneurosci.3582-09.2010, doi:10.1523/jneurosci.3582-09.2010. This article has 232 citations.

17. (szymanowicz2024areviewof pages 5-6): Oliwia Szymanowicz, Artur Drużdż, Bartosz Słowikowski, Sandra Pawlak, Ewelina Potocka, Ulyana Goutor, Mateusz Konieczny, Małgorzata Ciastoń, Aleksandra Lewandowska, Paweł P. Jagodziński, Wojciech Kozubski, and Jolanta Dorszewska. A review of the cacna gene family: its role in neurological disorders. Diseases, 12:90, May 2024. URL: https://doi.org/10.3390/diseases12050090, doi:10.3390/diseases12050090. This article has 57 citations.

18. (gasser2010efnsguidelineson pages 4-5): T. Gasser, J. Finsterer, J. Baets, C. Van Broeckhoven, S. Di Donato, B. Fontaine, P. De Jonghe, A. Lossos, T. Lynch, C. Mariotti, L. Schöls, A. Spinazzola, Z. Szolnoki, S. J. Tabrizi, C.M.E. Tallaksen, M. Zeviani, J‐M. Burgunder, and H. F. Harbo. Efns guidelines on the molecular diagnosis of ataxias and spastic paraplegias. European Journal of Neurology, 17:179-188, Feb 2010. URL: https://doi.org/10.1111/j.1468-1331.2009.02873.x, doi:10.1111/j.1468-1331.2009.02873.x. This article has 73 citations and is from a domain leading peer-reviewed journal.
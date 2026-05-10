---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T12:57:20.218495'
end_time: '2026-05-10T13:20:41.198536'
duration_seconds: 1400.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Plasma Cell Neoplasm
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 88
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Plasma Cell Neoplasm
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Plasma Cell Neoplasm** covering all of the
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
- **Disease Name:** Plasma Cell Neoplasm
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Plasma Cell Neoplasm** covering all of the
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


## Comprehensive Research Report: Plasma Cell Neoplasm (PCN)

### Scope note
“Plasma cell neoplasm” is an umbrella term covering clonal plasma-cell disorders ranging from premalignant monoclonal gammopathies to overt malignancies and localized plasma-cell tumors, including monoclonal gammopathy of undetermined significance (MGUS), smoldering multiple myeloma (SMM), multiple myeloma (MM), solitary plasmacytoma of bone, extramedullary/extraosseous plasmacytoma, plasma cell leukemia (PCL), and immunoglobulin light-chain (AL) amyloidosis (fend2023plasmacellneoplasms pages 1-3, fend2023plasmacellneoplasms pages 6-8). Much of the high-quality contemporary evidence and criteria are published for MM and its precursors; where the retrieved corpus does not contain a requested identifier or statistic, this report explicitly labels it as unavailable.

---

## 1. Disease Information

### 1.1 Concise overview / definition
Plasma cell neoplasms are terminally differentiated B-cell neoplasms characterized by clonal expansion of plasma cells and typically secretion of a monoclonal immunoglobulin (“M-protein”), with a “stepwise development” from a premalignant clonal stage such as MGUS (fend2023plasmacellneoplasms pages 1-3). A contemporary review states: “Plasma cell neoplasms including multiple myeloma (MM) … are characterized by secretion of monoclonal immunoglobulin and stepwise development from … monoclonal gammopathy of undetermined significance (MGUS).” (Fend et al., 2023, Virchows Archiv; Nov 2023; https://doi.org/10.1007/s00428-022-03431-3) (fend2023plasmacellneoplasms pages 1-3).

### 1.2 Classification and terminology (WHO-HAEM5 / ICC 2022; current understanding)
Key recent classification concepts in the retrieved sources are from ICC 2022 updates summarized by Fend et al. (2023) (Nov 2023; https://doi.org/10.1007/s00428-022-03431-3):
- Terminology: “multiple myeloma” replaces “plasma cell myeloma” (fend2023plasmacellneoplasms pages 1-3).
- Cytogenetic subgrouping: MM is subdivided into mutually exclusive cytogenetic groups (eg, CCND family translocations; MAF family translocations; NSD2 translocation; hyperdiploidy), with remaining cases as MM, NOS (fend2023plasmacellneoplasms pages 1-3).
- IgM MGUS subdivision: IgM MGUS is subdivided into “IgM MGUS of plasma cell type” (precursor to rare IgM MM; MM-type cytogenetics; no clonal B-cells; MYD88 wild-type) versus IgM MGUS, NOS (fend2023plasmacellneoplasms pages 1-3).
- Amyloidosis terminology: systemic “primary AL” renamed immunoglobulin light-chain amyloidosis (AL) and localized AL amyloidosis recognized as distinct (fend2023plasmacellneoplasms pages 1-3).
- Plasmacytoma staging nuance: minimal bone marrow infiltration detected by flow cytometry has major prognostic importance for solitary plasmacytoma of bone (fend2023plasmacellneoplasms pages 1-3).

### 1.3 Key identifiers (MONDO, ICD-10/11, MeSH, OMIM, Orphanet)
The retrieved corpus did not include authoritative identifier crosswalks (MONDO, ICD-10/11, MeSH, OMIM, Orphanet). Therefore, **MONDO ID: not available from retrieved sources**.

### 1.4 Common synonyms / alternative names
- “Multiple myeloma” (preferred) vs historical “plasma cell myeloma” (WHO 2016 term replaced per ICC summary) (fend2023plasmacellneoplasms pages 1-3).
- “Plasma cell dyscrasias” is used as a broad clinical grouping that includes MGUS/MM and related entities (nedal2024dietinducedobesityreduces pages 1-2).

### 1.5 Evidence source type (aggregated vs patient-level)
Most information summarized here comes from aggregated resources including classification reviews and registry/cohort studies (eg, SEER-based incidence trends; national and regional cancer registries; prospective observational cohorts) (mousavi2023apopulationbasedstudy pages 1-2, imounga2023thesingularepidemiology pages 1-2, shibayama2024primaryanalysisof pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors (current understanding)
PCNs arise through multistep clonal evolution from premalignant stages (MGUS → SMM → MM), with genetics and the bone marrow microenvironment shaping progression (fend2023plasmacellneoplasms pages 1-3, kansal2024towardprecisionmedicine pages 3-6).

### 2.2 Risk factors (genetic and environmental)

#### Genetic susceptibility
A large 2023 study using functional annotation and GWAS meta-analysis (Macauda et al., 2023, Leukemia; Sep 2023; https://doi.org/10.1038/s41375-023-02022-8) reiterates that familial aggregation and the MGUS precursor support heritable susceptibility; it analyzed 5,982 MM cases and 266,173 controls and reports a novel locus (rs28199) with OR 1.18 (95% CI 1.11–1.23) (macauda2023identificationofnovel pages 1-2).

Open Targets (retrieved context) highlights MM-associated/therapeutically relevant targets including CRBN, TNFRSF17 (BCMA), CD38, KRAS/NRAS, FGFR3, and XPO1, reflecting the intersection of genetics and druggability in modern MM management (OpenTargets Search: multiple myeloma).

#### Environmental / lifestyle risk factors
- **Obesity:** A 2024 experimental paper states: “Obesity is associated with an increased risk of developing multiple myeloma (MM)” and shows diet-induced obesity promotes tumor growth and reduces bone marrow T and B cells in a transplantable Vk*MYC model (Nedal et al., 2024, Scientific Reports; Feb 2024; https://doi.org/10.1038/s41598-024-54193-8) (nedal2024dietinducedobesityreduces pages 1-2).
- **Pesticide exposures (MGUS-focused evidence):** A 2023 systematic review of MGUS risk factors reports strong associations for several pesticides/chemicals (examples: dieldrin 5.6-fold [95% CI 1.9–16.6]; chlorothalonil 2.4-fold [95% CI 1.1–5.3]; permethrin OR 2.49 [95% CI 1.32–4.69]) (Verma et al., 2023, Hemato; Nov 2023; https://doi.org/10.3390/hemato4040027) (verma2023geographicprevalencepatterns pages 9-11).
- **Chlordecone (organochlorine pesticide) and MM incidence gradient:** A Martinique registry-based spatial study (Houpert et al., 2024, BMC Cancer; Dec 2024; https://doi.org/10.1186/s12885-024-13221-6) reports “a significant increasing gradient in the incidence of multiple myeloma in men, from reference to highly contaminated areas” of chlordecone soil contamination (houpert2024geographicaldisparitiesin pages 1-2).

#### Precursor condition prevalence and progression risk (etiologic context)
MGUS prevalence varies geographically (0.24%–9% across studies), affects ~3% of people >50 years in the US, and progresses to MM at ~1% per year (Verma et al., 2023) (verma2023geographicprevalencepatterns pages 1-2).

### 2.3 Protective factors
Protective factors are incompletely defined. A 2023 MGUS review reports diet associations suggesting higher fruit intake may be protective (eg, adolescent fruit intake 3×/week OR 0.62 [95% CI 0.41–0.95]; midlife whole-wheat bread >5/week OR 0.75 [95% CI 0.57–0.99]) (verma2023geographicprevalencepatterns pages 11-13). No specific genetic protective variants were identified in the retrieved corpus.

### 2.4 Gene–environment interactions
Direct gene–environment interaction analyses were not available in the retrieved corpus. However, MGUS etiology is hypothesized to involve chronic antigenic stimulation and immune/inflammatory context interacting with clonal genetic lesions (verma2023geographicprevalencepatterns pages 1-2, verma2023geographicprevalencepatterns pages 13-14).

---

## 3. Phenotypes

### 3.1 Cardinal clinical phenotype framework (SLiM-CRAB)
IMWG diagnostic framework incorporates “CRAB” end-organ damage and “SLiM” biomarkers to define myeloma-defining events. A 2024 review summarizes SLiM criteria as: “60% of clonal bone marrow plasma cells, involved/uninvolved serum free light chain ratio ≥100 and >1 focal lesion in MRI studies.” (Morè et al., 2024, Cancers; Jun 2024; https://doi.org/10.3390/cancers16122263) (more2024thechallengingapproach pages 1-2). A separate 2024 review similarly lists SLiM-CRAB components and specifies that presence of any CRAB or SLiM event with ≥10% clonal marrow plasma cells (or a biopsy-proven plasmacytoma) defines active MM (Kansal 2024; Jan 2024; https://doi.org/10.33696/haematology.5.058) (kansal2024towardprecisionmedicine pages 3-6).

### 3.2 Precursor-stage phenotype
SMM is defined as asymptomatic disease meeting M-protein and/or marrow plasma-cell thresholds but without SLiM-CRAB features (fend2023plasmacellneoplasms pages 6-8, kansal2024towardprecisionmedicine pages 3-6).

### 3.3 Aggressive phenotype: PCL and PCL-like MM
- IMWG revised PCL criterion: ≥5% circulating plasma cells (kansal2024towardprecisionmedicine pages 3-6, jelinek2023morethan2% pages 1-2).
- A 2023 JCO study proposes a more sensitive flow-cytometry threshold (>2% circulating tumor plasma cells) for an ultra–high-risk “PCL-like” subgroup with markedly worse PFS and OS (Jelinek et al., 2023; Mar 2023; https://doi.org/10.1200/JCO.22.01226) (jelinek2023morethan2% pages 1-2, jelinek2023morethan2% pages 4-5).

### 3.4 Suggested phenotype ontology terms (HPO) (non-exhaustive)
Because the retrieved corpus did not enumerate phenotype frequencies for classic CRAB components, below are **ontology suggestions** aligned to the SLiM-CRAB framework:
- Bone lesions/osteolysis: HP:0002797 (Osteolysis); HP:0002659 (Skeletal abnormalities)
- Hypercalcemia: HP:0003072
- Renal insufficiency: HP:0000083
- Anemia: HP:0001903
- Elevated serum free light chains / monoclonal protein: HP:0030393 (Paraproteinemia; if used) / HP:0030410 (Monoclonal gammopathy; term availability varies)
- Bone marrow plasmacytosis: HP:0030180 (Plasmacytosis; if used)

(These HPO suggestions are provided as a mapping aid; the retrieved corpus did not include HPO annotations.)

---

## 4. Genetic / Molecular Information

### 4.1 Recurrent cytogenetic/genetic classes (MM)
ICC 2022 emphasizes MM cytogenetic subgrouping (CCND family translocations, MAF family translocations, NSD2 translocation, hyperdiploidy) reflecting clinical/prognostic relevance (fend2023plasmacellneoplasms pages 1-3). Primary cytogenetic features such as trisomies/hyperdiploidy may be present already in MGUS and persist through progression (fend2023plasmacellneoplasms pages 6-8).

### 4.2 Core molecular pathways and mechanistic chain (current understanding)
Progression is driven by cumulative genetic lesions and dependence on bone marrow microenvironment signals. A 2024 mouse-model review emphasizes that progression from MGUS to MM is “frequently driven by activation of MYC, RAS/mTOR, or NFkB pathways,” and that BCMA signaling via APRIL/BAFF activates NF-κB and supports survival (du2024immunocompetentmousemodels pages 1-3).

### 4.3 Multi-omics and genomic evolution (model-organism evidence)
The Vk*MYC immunocompetent mouse model credibly recapitulates diverse, spontaneously acquired genomic alterations. A 2024 Nature Communications study reports that analysis of 119 Vk*MYC tumors shows recurrent CNVs, structural variants, chromothripsis, driver mutations, APOBEC activity, and decreasing immunoglobulin transcription with increasing proliferation; it identifies murine-specific insertional mutagenesis activating NF-κB and IL6 signaling pathways shared with human MM (Maura et al., 2024; May 2024; https://doi.org/10.1038/s41467-024-48091-w) (maura2024thegenomiclandscape pages 1-2).

### 4.4 Suggested ontology terms
- **Cell type (CL):** plasma cell (CL:0000786); malignant plasma cell (no single CL term; often modeled as plasma cell with disease context)
- **Biological processes (GO, examples):** NF-κB signaling (eg, GO:0043122), B cell receptor signaling (GO:0050853), plasma cell differentiation (GO:0002313), response to interleukin-6 (GO:0070741), T cell exhaustion (no single GO term; related to regulation of T cell activation)

---

## 5. Diagnostics

### 5.1 Clinical criteria and key diagnostic thresholds (IMWG)
- **SMM definition:** M-protein ≥30 g/L or urinary M-protein ≥500 mg/24 h or 10–60% clonal BM plasma cells, without myeloma-defining events (fend2023plasmacellneoplasms pages 6-8, kansal2024towardprecisionmedicine pages 3-6).
- **Active MM:** ≥10% clonal BM plasma cells or biopsy-proven plasmacytoma plus CRAB and/or SLiM myeloma-defining biomarkers (kansal2024towardprecisionmedicine pages 3-6).

### 5.2 Imaging
Conventional skeletal X-ray is less sensitive; a 2024 review states false-negativity “ranging from 30% to 70%,” and notes whole-body low-dose CT, PET, and whole-body MRI are increasingly central for diagnosis/staging and prognostication (more2024thechallengingapproach pages 1-2).

### 5.3 Pathology and flow cytometry (plasmacytoma)
For localized plasma-cell tumors, ICC 2022 emphasizes that minimal marrow infiltration detected by flow cytometry is of major prognostic importance in solitary plasmacytoma of bone (fend2023plasmacellneoplasms pages 1-3).

### 5.4 MRD (measurable/minimal residual disease): methods, sensitivity, implementation
Two principal MRD methods are widely used: NGS (immunoglobulin gene clonotype tracking) and high-sensitivity flow cytometry (NGF).
- IMWG benchmark: MRD assays should achieve at least 10−5 sensitivity (jevremovic2024reallifesensitivityof pages 1-2).
- FDA-approved MRD test: A 2024 letter notes: “Currently the only FDA approved test for MM MRD is NGS-based clonoSEQ© … with the sensitivity of 10−6.” (Jevremovic et al., 2024; Jul 2024; https://doi.org/10.1038/s41408-024-01113-8) (jevremovic2024reallifesensitivityof pages 1-2). A 2023 MRD review similarly notes clonoSEQ as FDA-approved (krzywdzinska2023roleofflow pages 2-3).
- Real-world NGF performance: the same 2024 letter reports median collected events ~7–8.3×10^6 yielding practical sensitivities ~2.4–2.8×10−6, approaching NGS-level sensitivity in practice (jevremovic2024reallifesensitivityof pages 1-2).
- NGF vs NGS comparison (China cohort): NGS showed LOD ~10−6 and detected MRD in 6/7 pre-ASCT samples vs NGF in 1/7, with 79.1% concordance overall (Zhou et al., 2024; Mar 2024; https://doi.org/10.1007/s12672-024-00938-w) (zhou2024evaluationofnextgeneration pages 1-3).
- Deep MRD for treatment decisions: MRD2STOP (2024; https://doi.org/10.1038/s41408-024-01156-x) used PET, BM flow (LoD 10−5) and BM clonoSEQ (LoD 10−6) for eligibility; CD138+ enrichment enabled ~10−7 sensitivity, and clonoSEQ LoD is reported as 6.8×10−7 with LOQ 1.76×10−6 under specified input conditions (derman2024discontinuationofmaintenance pages 1-2).

### 5.5 Suggested diagnostic ontology terms (examples)
- LOINC examples (not extracted from corpus): serum free light chain assay; serum protein electrophoresis (SPEP); immunofixation; β2-microglobulin.
- MAXO examples: bone marrow biopsy (MAXO term varies), flow cytometry assay, next-generation sequencing assay.

---

## 6. Outcome / Prognosis (including epidemiology)

### 6.1 Epidemiology: incidence and demographic disparities

#### United States (SEER 22; 2000–2020)
A SEER-22 population analysis used ICD-O-3 morphological codes 9731 (solitary plasmacytoma of bone), 9732 (plasma cell myeloma), and 9734 (extraosseous plasmacytoma) (Mousavi et al., 2023; Nov 2023; https://doi.org/10.1038/s41598-023-47906-y) (mousavi2023apopulationbasedstudy pages 1-2).
Key findings include:
- 193,530 plasma cell myeloma cases (2000–2019), with 85.51% age ≥55 and 54.82% male (mousavi2023apopulationbasedstudy pages 1-2).
- Age-standardized incidence (all ages) ~7.8 per 100,000 for both sexes (women 7.86; men 7.84), with small positive AAPCs over 2000–2019 (mousavi2023apopulationbasedstudy pages 8-10).
- Marked racial disparity: Non-Hispanic Black incidence highest (women 11.65; men 15.64 per 100,000) (mousavi2023apopulationbasedstudy pages 8-10).
- Plasmacytomas are rare with low ASIRs (eg, extraosseous plasmacytoma ~0.06 women and ~0.13 men per 100,000 overall) and declining incidence (AAPC negative) (mousavi2023apopulationbasedstudy pages 10-11).

A table containing ASIR/AAPC stratifications is present in the source and was retrieved as images (Tables 4–6) (mousavi2023apopulationbasedstudy media 89dc06ac, mousavi2023apopulationbasedstudy media e0de6d5f, mousavi2023apopulationbasedstudy media a18865ac).

#### French Guiana (registry; 2005–2014)
A cancer registry study reports world-standardized incidence 5.9/100,000 man-years and 7.8/100,000 woman-years with female predominance and younger median age at diagnosis than mainland France (Imounga et al., 2023; Dec 2023; https://doi.org/10.3390/cancers16010178) (imounga2023thesingularepidemiology pages 1-2, imounga2023thesingularepidemiology pages 2-4).

### 6.2 Survival outcomes (recent cohort data)
A prospective Japanese observational cohort in the “novel drug era” (2016–2021; analysis of 2016–2018 diagnoses) reports a 3-year OS of 70.0% among treated symptomatic PCN (n=1284), with much higher 3-year OS among those receiving upfront autologous stem cell transplant (ASCT) (90.3%) vs those not receiving ASCT (61.4%) (Shibayama et al., 2024; Mar 2024; https://doi.org/10.1007/s12185-024-03754-8) (shibayama2024primaryanalysisof pages 1-2).

### 6.3 Ultra–high-risk subgroup outcomes (PCL-like)
Jelinek et al. (2023) report that patients with 2%–20% circulating tumor plasma cells had markedly shorter PFS and OS than those with <2% (example cohort: PFS 3.1 vs 15.6 months; OS 14.6 vs 33.6 months) (https://doi.org/10.1200/JCO.22.01226) (jelinek2023morethan2% pages 1-2).

---

## 7. Treatment (current applications; 2023–2024 developments prioritized)

### 7.1 Current treatment landscape (high-level)
Modern MM outcomes improved through proteasome inhibitors, IMiDs, and anti-CD38 monoclonal antibodies (daratumumab, isatuximab), with newer immunotherapies (CAR-T and bispecific antibodies) producing deep responses but novel toxicities (CRS, neurotoxicity, infections) (more2024thechallengingapproach pages 1-2).

### 7.2 BCMA-directed CAR-T therapies (ide-cel, cilta-cel): real-world and trial outcomes
A 2024 review summarizes:
- KarMMa-3: ide-cel ORR 71% vs 42% control; median PFS 13.3 vs 4.4 months (mirvis2024arewethere pages 3-4).
- CARTITUDE-1: cilta-cel ORR 97%, 67% sCR; median PFS 34.9 months (mirvis2024arewethere pages 3-4).

Real-world sequential BCMA targeting: a multi-center real-world cohort of commercial ide-cel found lower outcomes in patients previously exposed to BCMA-targeted therapy (ORR 74% vs 88%; median PFS 3.2 vs 9.0 months) (Ferreri et al., 2023; Aug 2023; https://doi.org/10.1038/s41408-023-00886-8) (ferreri2023realworldexperienceof pages 1-2).

### 7.3 Bispecific antibodies (T-cell redirectors): teclistamab, elranatamab, talquetamab
A 2024 review reports that these BsAbs achieve ORR exceeding 60% and CR rates ~25–50% with median PFS around 1 year in heavily pretreated RRMM; key toxicities include CRS, cytopenias, hypogammaglobulinemia, and infections (Tacchetti et al., 2024; Jun 2024; https://doi.org/10.3390/cancers16132337) (tacchetti2024bispecificantibodiesfor pages 1-2).

Agent-level examples from the retrieved corpus:
- **Teclistamab (MajesTEC-1):** ORR 63% (updated), ≥CR 45.5%, median PFS 11.3 months, median DoR 21.6 months; hematologic toxicity includes neutropenia 71% (65.5% grade ≥3) (tacchetti2024bispecificantibodiesfor pages 5-6).
- **Infections and CRS (teclistamab):** a 2024 review summarizes teclistamab trial data with CRS ~70–72% (mostly grade 1–2), ICANS ~14.5%, and infections 76.4% (44.8% grade ≥3) (Parrondo et al., 2024; Apr 2024; https://doi.org/10.3389/fonc.2024.1394048) (parrondo2024bispecificantibodiesfor pages 2-3).
- **Regulatory timeline and indications:** elranatamab was FDA-approved Aug 2023 after ≥4 prior lines including PI/IMiD/anti-CD38 (Devasia et al., 2024; Sep 2024; https://doi.org/10.1038/s41408-024-01139-y) (devasia2024bispecificantibodiesin pages 3-4).

### 7.4 Real-world implementation considerations (expert analysis)
Continuous bispecific dosing “until disease progression” raises infection risk, cost, and biologic concerns (T-cell exhaustion). A 2024 perspective argues for strategies such as less-frequent maintenance dosing or fixed-duration therapy after deep remission to improve the toxicity–efficacy balance (van de Donk et al., 2024; Sep 2024; https://doi.org/10.1158/2643-3230.bcd-24-0124) (donk2024tcell–redirectingbispecific pages 1-2).

### 7.5 Suggested treatment ontology terms (MAXO; examples)
- Autologous hematopoietic stem cell transplantation (ASCT)
- Proteasome inhibitor therapy
- Immunomodulatory drug therapy
- Anti-CD38 monoclonal antibody therapy
- CAR-T cell therapy (BCMA-directed)
- Bispecific T-cell engager antibody therapy (BCMA×CD3; GPRC5D×CD3)

(MAXO term IDs were not retrievable from the provided corpus.)

---

## 8. Prevention

### 8.1 Primary prevention
No established primary-prevention interventions exist to prevent transformation to MM. Modifiable risk-factor evidence is strongest for obesity and certain environmental exposures (eg, pesticide-related associations in MGUS literature; chlordecone gradients in Martinique) (nedal2024dietinducedobesityreduces pages 1-2, verma2023geographicprevalencepatterns pages 9-11, houpert2024geographicaldisparitiesin pages 1-2).

### 8.2 Secondary prevention (early detection)
Population screening for MGUS is controversial and was not directly addressed in the retrieved corpus. However, MGUS prevalence (~3% age>50) and progression risk (~1%/year) support risk-stratified monitoring paradigms (verma2023geographicprevalencepatterns pages 1-2).

### 8.3 Tertiary prevention
Infection prevention is particularly relevant with T-cell redirectors and CAR-T due to infection burden and hypogammaglobulinemia; continuous bispecific dosing is explicitly associated with “high risk of infections” (donk2024tcell–redirectingbispecific pages 1-2), and teclistamab trials report high infection rates including grade ≥3 events (parrondo2024bispecificantibodiesfor pages 2-3).

---

## 9. Other Species / Natural Disease and Model Organisms

### 9.1 Widely used immunocompetent mouse models (real-world implementation in research)
A 2024 review of immunocompetent mouse models summarizes key systems used for MM biology and therapy development (Du et al., 2024; Apr 2024; https://doi.org/10.1016/j.hoc.2023.12.014):
- **5TMM family (5T2/5T33/5TGM1; C57BL/KaLwRij):** IgG-secreting, BM-homing, lytic bone lesions; used for homing, dormancy, bone disease and therapeutic studies; strain-dependent constraints (du2024immunocompetentmousemodels pages 3-4).
- **Pristane-induced Balb/c plasmacytomas:** IL-6 dependent; typically harbor MYC translocations (du2024immunocompetentmousemodels pages 3-4).
- **Vk*MYC (C57BL/6):** indolent, progressive, class-switched, somatically hypermutated, BM-restricted monoclonal PC disease traceable by M-spike; long latency enables secondary lesions; many transplantable lines; useful for immunotherapy and evolution studies (du2024immunocompetentmousemodels pages 4-6).

### 9.2 Model strengths and limitations (expert synthesis)
No single model recapitulates all human MM heterogeneity and microenvironment dependence; model choice should match the question (genetic evolution vs immune microenvironment vs bone disease) (du2024immunocompetentmousemodels pages 6-8, du2024immunocompetentmousemodels pages 8-9).

### 9.3 Recent mechanistic insight from advanced models (2023–2024)
- **Genetically heterogeneous GEMMs + immune evasion:** A Nature Medicine study created 15 models by combinatorial activation of eight MM lesions and found a MAPK–MYC axis accelerating progression; timing of MYC activation shaped immune evasion and response to immune checkpoint blockade (Larrayoz et al., 2023; Mar 2023; https://doi.org/10.1038/s41591-022-02178-3) (larrayoz2023preclinicalmodelsfor pages 1-2).
- **Vk*MYC genomic evolution:** multi-omics of Vk*MYC highlights shared NF-κB and IL6 pathway activation mechanisms and sustained MYC dependence even in advanced tumors (Maura et al., 2024; May 2024; https://doi.org/10.1038/s41467-024-48091-w) (maura2024thegenomiclandscape pages 1-2).

---

## 10. Summary Table Artifact
The table below compiles key entity definitions and threshold-based diagnostic/classification updates from ICC 2022/IMWG found in the retrieved corpus.

| Entity | Key defining / classification point | Specific threshold / update | Source | DOI URL |
|---|---|---|---|---|
| IgM MGUS (plasma cell type) | ICC 2022 subdivides IgM MGUS into plasma cell type vs IgM MGUS, NOS | Plasma cell type is precursor to rare IgM MM; characterized by MM-type cytogenetics, absence of clonal B-cells, and absence of MYD88 mutation (fend2023plasmacellneoplasms pages 1-3) | Fend 2023 | https://doi.org/10.1007/s00428-022-03431-3 |
| Smoldering multiple myeloma (SMM) | Asymptomatic clonal plasma-cell disorder without myeloma-defining events | Serum M-protein ≥30 g/L or urinary M-protein ≥500 mg/24 h and/or clonal BM plasma cells 10–60%, without SLiM-CRAB features (fend2023plasmacellneoplasms pages 6-8, kansal2024towardprecisionmedicine pages 3-6) | Fend 2023; Kansal 2024 | https://doi.org/10.1007/s00428-022-03431-3; https://doi.org/10.33696/haematology.5.058 |
| Multiple myeloma (MM) | Active MM defined by clonal plasma-cell burden plus CRAB or biomarker-defined SLiM events | Requires ≥10% clonal BM plasma cells or biopsy-proven plasmacytoma plus CRAB and/or SLiM criteria (kansal2024towardprecisionmedicine pages 3-6, more2024thechallengingapproach pages 1-2) | Kansal 2024; Morè 2024 | https://doi.org/10.33696/haematology.5.058; https://doi.org/10.3390/cancers16122263 |
| Multiple myeloma (MM) — SLiM biomarkers | IMWG 2014 myeloma-defining biomarkers incorporated into current diagnostic framework | S = BM plasma cells ≥60%; Li = involved/uninvolved FLC ratio ≥100; M = >1 focal MRI lesion >5 mm (kansal2024towardprecisionmedicine pages 3-6, more2024thechallengingapproach pages 1-2) | Kansal 2024; Morè 2024 | https://doi.org/10.33696/haematology.5.058; https://doi.org/10.3390/cancers16122263 |
| Multiple myeloma (MM) — ICC 2022 classification | Term “multiple myeloma” replaces “plasma cell myeloma”; formal cytogenetic subgrouping added | Four mutually exclusive cytogenetic groups recognized: CCND family translocations, MAF family translocations, NSD2 translocation, and hyperdiploidy; remainder MM, NOS (fend2023plasmacellneoplasms pages 1-3) | Fend 2023 | https://doi.org/10.1007/s00428-022-03431-3 |
| Solitary plasmacytoma of bone | Diagnosis requires exclusion of systemic marrow disease; ICC emphasizes prognostic value of occult marrow involvement | Minimal BM infiltration detected by flow cytometry is of major prognostic importance (fend2023plasmacellneoplasms pages 1-3) | Fend 2023 | https://doi.org/10.1007/s00428-022-03431-3 |
| Extramedullary / extraosseous plasmacytoma | Localized plasma-cell tumor outside bone marrow; marrow assessment remains important | Minimal BM infiltration by flow cytometry has prognostic importance, though less than for solitary bone plasmacytoma (fend2023plasmacellneoplasms pages 1-3) | Fend 2023 | https://doi.org/10.1007/s00428-022-03431-3 |
| AL amyloidosis | ICC 2022 nomenclature update | “Primary systemic amyloidosis” renamed immunoglobulin light-chain (AL) amyloidosis; localized AL amyloidosis recognized as a distinct entity (fend2023plasmacellneoplasms pages 1-3) | Fend 2023 | https://doi.org/10.1007/s00428-022-03431-3 |
| Plasma cell leukemia (PCL) | Updated IMWG peripheral blood criterion | PCL defined by ≥5% circulating plasma cells in peripheral blood (revised from older 20% threshold) (kansal2024towardprecisionmedicine pages 3-6, jelinek2023morethan2% pages 1-2, kansal2024towardprecisionmedicine pages 8-10) | Kansal 2024; Jelinek 2023 | https://doi.org/10.33696/haematology.5.058; https://doi.org/10.1200/JCO.22.01226 |
| PCL-like multiple myeloma | Flow-cytometry-defined ultra–high-risk MM subset proposed in recent work | >2% circulating tumor plasma cells (CTCs) by flow cytometry identifies PCL-like MM; patients with 2–20% CTCs had markedly inferior outcomes vs <2% (e.g., PFS 3.1 vs 15.6 months; OS 14.6 vs 33.6 months in one cohort) (jelinek2023morethan2% pages 4-5, jelinek2023morethan2% pages 6-7, jelinek2023morethan2% pages 1-2, jelinek2023morethan2% pages 2-3) | Jelinek 2023 | https://doi.org/10.1200/JCO.22.01226 |


*Table: This table summarizes the main plasma cell neoplasm entities and the most important ICC 2022/IMWG diagnostic or classification updates, including threshold-based criteria. It is useful as a compact reference for disease knowledge-base curation and clinical concept mapping.*

---

## 11. Data and Statistics Highlights (recent)
- US SEER (2000–2019): plasma cell myeloma ASIR ~7.8 per 100,000; NHB men ASIR ~15.6 per 100,000; plasmacytomas are rare with ASIR fractions per 100,000 (mousavi2023apopulationbasedstudy pages 8-10, mousavi2023apopulationbasedstudy pages 10-11).
- French Guiana registry (2005–2014): world-standardized incidence 5.9/100,000 men/year and 7.8/100,000 women/year; median diagnosis age younger than mainland France (imounga2023thesingularepidemiology pages 1-2).
- Japanese prospective cohort (2016–2018 diagnoses): 3-year OS 70.0% overall; 90.3% with upfront ASCT vs 61.4% without (shibayama2024primaryanalysisof pages 1-2).
- PCL-like MM: >2% circulating tumor plasma cells by flow identifies ultra–high-risk subset with PFS 3.1 vs 15.6 months and OS 14.6 vs 33.6 months vs <2% in one cohort (jelinek2023morethan2% pages 1-2).
- MRD: FDA-approved clonoSEQ sensitivity ~10−6; real-world NGF in a reference lab can approach ~10−6 (jevremovic2024reallifesensitivityof pages 1-2).

---

## Figures/Tables consulted (visual evidence)
SEER-derived incidence tables for plasma cell myeloma and plasmacytoma subtypes were located in Tables 4–6 of Mousavi et al. (2023) (mousavi2023apopulationbasedstudy media 89dc06ac, mousavi2023apopulationbasedstudy media e0de6d5f, mousavi2023apopulationbasedstudy media a18865ac).

---

## Limitations of this report (due to retrieval constraints)
- **Disease identifiers (MONDO/ICD/MeSH/OMIM/Orphanet)** were not present in the retrieved sources and therefore are not provided.
- **Detailed phenotype frequencies**, **full differential diagnosis lists**, and **comprehensive molecular lesion catalogs** (eg, variant-level COSMIC/ClinVar entries, methylation markers) were not fully available in the retrieved corpus; mechanistic content is therefore focused on high-confidence pathway-level findings and model-system evidence.
- Not all cited papers provide PubMed IDs in the retrieved text chunks; where PMIDs are required, direct PubMed lookup was not possible with the provided toolset in this run.


References

1. (fend2023plasmacellneoplasms pages 1-3): Falko Fend, Ahmet Dogan, and James R. Cook. Plasma cell neoplasms and related entities—evolution in diagnosis and classification. Virchows Archiv, 482:163-177, Nov 2023. URL: https://doi.org/10.1007/s00428-022-03431-3, doi:10.1007/s00428-022-03431-3. This article has 74 citations and is from a peer-reviewed journal.

2. (fend2023plasmacellneoplasms pages 6-8): Falko Fend, Ahmet Dogan, and James R. Cook. Plasma cell neoplasms and related entities—evolution in diagnosis and classification. Virchows Archiv, 482:163-177, Nov 2023. URL: https://doi.org/10.1007/s00428-022-03431-3, doi:10.1007/s00428-022-03431-3. This article has 74 citations and is from a peer-reviewed journal.

3. (nedal2024dietinducedobesityreduces pages 1-2): Tonje Marie Vikene Nedal, Siv Helen Moen, Ingrid Aass Roseth, Synne Stokke Tryggestad, Kristin Roseth Aass, Gunhild Garmo Hov, Hanne Hella, Anne-Marit Sponaas, and Therese Standal. Diet-induced obesity reduces bone marrow t and b cells and promotes tumor progression in a transplantable vk*myc model of multiple myeloma. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-54193-8, doi:10.1038/s41598-024-54193-8. This article has 16 citations and is from a peer-reviewed journal.

4. (mousavi2023apopulationbasedstudy pages 1-2): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Zahra Yekta, and Seyed Aria Nejadghaderi. A population-based study on incidence trends of myeloma in the united states over 2000–2020. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47906-y, doi:10.1038/s41598-023-47906-y. This article has 35 citations and is from a peer-reviewed journal.

5. (imounga2023thesingularepidemiology pages 1-2): Laure Manuella Imounga, Kinan Drak Alsibai, Juliette Plenet, Qiannan Wang, Beatrice Virjophe-Cenciu, Pierre Couppie, Nadia Sabbah, Antoine Adenis, and Mathieu Nacher. The singular epidemiology of plasmacytoma and multiple myeloma in french guiana. Cancers, 16:178, Dec 2023. URL: https://doi.org/10.3390/cancers16010178, doi:10.3390/cancers16010178. This article has 5 citations.

6. (shibayama2024primaryanalysisof pages 1-2): Hirohiko Shibayama, Mitsuhiro Itagaki, Hiroshi Handa, Akihiro Yokoyama, Akio Saito, Satoru Kosugi, Shuichi Ota, Makoto Yoshimitsu, Yasuhiro Tanaka, Shingo Kurahashi, Shin-ichi Fuchida, Masaki Iino, Takayuki Shimizu, Yukiyoshi Moriuchi, Kohtaro Toyama, Kinuko Mitani, Yutaka Tsukune, Akiko Kada, Hideto Tamura, Masahiro Abe, Hiromi Iwasaki, Junya Kuroda, Hiroyuki Takamatsu, Kazutaka Sunami, Masahiro Kizaki, Tadao Ishida, Toshiki Saito, Itaru Matsumura, Koichi Akashi, and Shinsuke Iida. Primary analysis of a prospective cohort study of japanese patients with plasma cell neoplasms in the novel drug era (2016–2021). International Journal of Hematology, 119:707-721, Mar 2024. URL: https://doi.org/10.1007/s12185-024-03754-8, doi:10.1007/s12185-024-03754-8. This article has 11 citations and is from a peer-reviewed journal.

7. (kansal2024towardprecisionmedicine pages 3-6): Rina Kansal. Toward precision medicine for patients with multiple myeloma. Journal of Clinical Haematology, 5:12-33, Jan 2024. URL: https://doi.org/10.33696/haematology.5.058, doi:10.33696/haematology.5.058. This article has 1 citations.

8. (macauda2023identificationofnovel pages 1-2): Angelica Macauda, Klara Briem, Alyssa Clay-Gilmour, Wendy Cozen, Asta Försti, Matteo Giaccherini, Chiara Corradi, Juan Sainz, Yasmeen Niazi, Rob ter Horst, Yang Li, Mihai G. Netea, Ulla Vogel, Kari Hemminki, Susan L. Slager, Judit Varkonyi, Vibeke Andersen, Elzbieta Iskierka-Jazdzewska, Joaquin Mártinez-Lopez, Jan Zaucha, Nicola J. Camp, S. Vincent Rajkumar, Agnieszka Druzd-Sitek, Parveen Bhatti, Stephen J. Chanock, Shaji K. Kumar, Edyta Subocz, Grzegorz Mazur, Stefano Landi, Mitchell J. Machiela, Andrés Jerez, Aaron D. Norman, Michelle A. T. Hildebrandt, Katalin Kadar, Sonja I. Berndt, Elad Ziv, Gabriele Buda, Arnon Nagler, Charles Dumontet, Malgorzata Raźny, Marzena Watek, Aleksandra Butrym, Norbert Grzasko, Marek Dudzinski, Malwina Rybicka-Ramos, Eva-Laure Matera, Ramón García-Sanz, Hartmut Goldschmidt, Krzysztof Jamroziak, Artur Jurczyszyn, Esther Clavero, Graham G. Giles, Matteo Pelosini, Daria Zawirska, Marcin Kruszewski, Herlander Marques, Eva Haastrup, José Manuel Sánchez-Maldonado, Uta Bertsch, Marcin Rymko, Marc-Steffen Raab, Elizabeth E. Brown, Jonathan N. Hofmann, Celine Vachon, Daniele Campa, and Federico Canzian. Identification of novel genetic loci for risk of multiple myeloma by functional annotation. Leukemia, 37:2326-2329, Sep 2023. URL: https://doi.org/10.1038/s41375-023-02022-8, doi:10.1038/s41375-023-02022-8. This article has 7 citations and is from a highest quality peer-reviewed journal.

9. (OpenTargets Search: multiple myeloma): Open Targets Query (multiple myeloma, 25 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (verma2023geographicprevalencepatterns pages 9-11): Karina P. Verma, Rebecca Steuer, and Camille V. Edwards. Geographic prevalence patterns and modifiable risk factors for monoclonal gammopathy of undetermined significance. Hemato, 4:331-349, Nov 2023. URL: https://doi.org/10.3390/hemato4040027, doi:10.3390/hemato4040027. This article has 10 citations.

11. (houpert2024geographicaldisparitiesin pages 1-2): Rémi Houpert, Jacqueline Véronique-Baudin, Thierry Almont, Murielle Beaubrun-Renard, Manon Boullard, Aimée Pierre-Louis, Mylène Vestris, Stephen Ulric-Gervaise, Christelle Montabord, Jonathan Macni, Emmanuelle Sylvestre, and Clarisse Joachim. Geographical disparities in cancer and occupational exposure to pesticides in a french-west indies territory (2006–2019). BMC Cancer, Dec 2024. URL: https://doi.org/10.1186/s12885-024-13221-6, doi:10.1186/s12885-024-13221-6. This article has 2 citations and is from a peer-reviewed journal.

12. (verma2023geographicprevalencepatterns pages 1-2): Karina P. Verma, Rebecca Steuer, and Camille V. Edwards. Geographic prevalence patterns and modifiable risk factors for monoclonal gammopathy of undetermined significance. Hemato, 4:331-349, Nov 2023. URL: https://doi.org/10.3390/hemato4040027, doi:10.3390/hemato4040027. This article has 10 citations.

13. (verma2023geographicprevalencepatterns pages 11-13): Karina P. Verma, Rebecca Steuer, and Camille V. Edwards. Geographic prevalence patterns and modifiable risk factors for monoclonal gammopathy of undetermined significance. Hemato, 4:331-349, Nov 2023. URL: https://doi.org/10.3390/hemato4040027, doi:10.3390/hemato4040027. This article has 10 citations.

14. (verma2023geographicprevalencepatterns pages 13-14): Karina P. Verma, Rebecca Steuer, and Camille V. Edwards. Geographic prevalence patterns and modifiable risk factors for monoclonal gammopathy of undetermined significance. Hemato, 4:331-349, Nov 2023. URL: https://doi.org/10.3390/hemato4040027, doi:10.3390/hemato4040027. This article has 10 citations.

15. (more2024thechallengingapproach pages 1-2): Sonia Morè, Laura Corvatta, Valentina Maria Manieri, Erika Morsia, and Massimo Offidani. The challenging approach to multiple myeloma: from disease diagnosis and monitoring to complications management. Cancers, 16:2263, Jun 2024. URL: https://doi.org/10.3390/cancers16122263, doi:10.3390/cancers16122263. This article has 6 citations.

16. (jelinek2023morethan2% pages 1-2): Tomas Jelinek, Renata Bezdekova, David Zihala, Tereza Sevcikova, Anjana Anilkumar Sithara, Lenka Pospisilova, Sabina Sevcikova, Petra Polackova, Martin Stork, Zdenka Knechtova, Ondrej Venglar, Veronika Kapustova, Tereza Popkova, Ludmila Muronova, Zuzana Chyra, Matous Hrdinka, Michal Simicek, Juan-Jose Garcés, Noemi Puig, Maria-Teresa Cedena, Artur Jurczyszyn, Jorge J. Castillo, Miroslav Penka, Jakub Radocha, Maria Victoria Mateos, Jesús F. San-Miguel, Bruno Paiva, Ludek Pour, Lucie Rihova, and Roman Hajek. More than 2% of circulating tumor plasma cells defines plasma cell leukemia–like multiple myeloma. Journal of Clinical Oncology, 41:1383-1392, Mar 2023. URL: https://doi.org/10.1200/jco.22.01226, doi:10.1200/jco.22.01226. This article has 91 citations and is from a highest quality peer-reviewed journal.

17. (jelinek2023morethan2% pages 4-5): Tomas Jelinek, Renata Bezdekova, David Zihala, Tereza Sevcikova, Anjana Anilkumar Sithara, Lenka Pospisilova, Sabina Sevcikova, Petra Polackova, Martin Stork, Zdenka Knechtova, Ondrej Venglar, Veronika Kapustova, Tereza Popkova, Ludmila Muronova, Zuzana Chyra, Matous Hrdinka, Michal Simicek, Juan-Jose Garcés, Noemi Puig, Maria-Teresa Cedena, Artur Jurczyszyn, Jorge J. Castillo, Miroslav Penka, Jakub Radocha, Maria Victoria Mateos, Jesús F. San-Miguel, Bruno Paiva, Ludek Pour, Lucie Rihova, and Roman Hajek. More than 2% of circulating tumor plasma cells defines plasma cell leukemia–like multiple myeloma. Journal of Clinical Oncology, 41:1383-1392, Mar 2023. URL: https://doi.org/10.1200/jco.22.01226, doi:10.1200/jco.22.01226. This article has 91 citations and is from a highest quality peer-reviewed journal.

18. (du2024immunocompetentmousemodels pages 1-3): Megan Tien Du, Peter Leif Bergsagel, and Marta Chesi. Immunocompetent mouse models of multiple myeloma. Hematology/Oncology Clinics of North America, 38:533-546, Apr 2024. URL: https://doi.org/10.1016/j.hoc.2023.12.014, doi:10.1016/j.hoc.2023.12.014. This article has 3 citations.

19. (maura2024thegenomiclandscape pages 1-2): Francesco Maura, David G. Coffey, Caleb K. Stein, Esteban Braggio, Bachisio Ziccheddu, Meaghen E. Sharik, Megan T. Du, Yuliza Tafoya Alvarado, Chang-Xin Shi, Yuan Xiao Zhu, Erin W. Meermeier, Gareth J. Morgan, Ola Landgren, P. Leif Bergsagel, and Marta Chesi. The genomic landscape of vk*myc myeloma highlights shared pathways of transformation between mice and humans. Nature Communications, May 2024. URL: https://doi.org/10.1038/s41467-024-48091-w, doi:10.1038/s41467-024-48091-w. This article has 18 citations and is from a highest quality peer-reviewed journal.

20. (jevremovic2024reallifesensitivityof pages 1-2): Dragan Jevremovic, Min Shi, Pedro Horna, Gregory E. Otteson, Michael M. Timm, Linda B. Baughn, Patricia T. Greipp, Wilson I. Gonsalves, Prashant Kapoor, Morie A. Gertz, Moritz Binder, Francis K. Buadi, Jiehao Zhou, Angela Dispenzieri, Taxiarchis Kourelis, Eli Muchtar, S. Vincent Rajkumar, Shaji K. Kumar, and Horatiu Olteanu. Real-life sensitivity of flow cytometry minimal residual disease assessment for plasma cell neoplasms. Blood Cancer Journal, Jul 2024. URL: https://doi.org/10.1038/s41408-024-01113-8, doi:10.1038/s41408-024-01113-8. This article has 9 citations and is from a domain leading peer-reviewed journal.

21. (krzywdzinska2023roleofflow pages 2-3): Agnieszka Krzywdzińska, Bartosz Puła, and Krzysztof Jamroziak. Role of flow cytometric measurable residual disease assessment in multiple myeloma. Acta Haematologica Polonica, 54:113-128, Jun 2023. URL: https://doi.org/10.5603/ahp.a2023.0024, doi:10.5603/ahp.a2023.0024. This article has 0 citations.

22. (zhou2024evaluationofnextgeneration pages 1-3): Mo Zhou, Yan Chen, Yanlei Gong, Mingqing Zhu, Jiannong Cen, Jinlan Pan, Lingzhi Yan, Jingjing Shang, Song Jin, Xiaolan Shi, Weiqin Yao, Shuang Yan, Depei Wu, Suning Chen, Chengcheng Fu, and Li Yao. Evaluation of next-generation sequencing versus next-generation flow cytometry for minimal-residual-disease detection in chinese patients with multiple myeloma. Discover. Oncology, Mar 2024. URL: https://doi.org/10.1007/s12672-024-00938-w, doi:10.1007/s12672-024-00938-w. This article has 7 citations.

23. (derman2024discontinuationofmaintenance pages 1-2): Benjamin A. Derman, Ajay Major, Jennifer Cooperrider, Ken Jiang, Aubrianna Ramsland, Theodore Karrison, Tadeusz Kubicki, and Andrzej J. Jakubowiak. Discontinuation of maintenance therapy in multiple myeloma guided by multimodal measurable residual disease negativity (mrd2stop). Blood Cancer Journal, Oct 2024. URL: https://doi.org/10.1038/s41408-024-01156-x, doi:10.1038/s41408-024-01156-x. This article has 40 citations and is from a domain leading peer-reviewed journal.

24. (mousavi2023apopulationbasedstudy pages 8-10): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Zahra Yekta, and Seyed Aria Nejadghaderi. A population-based study on incidence trends of myeloma in the united states over 2000–2020. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47906-y, doi:10.1038/s41598-023-47906-y. This article has 35 citations and is from a peer-reviewed journal.

25. (mousavi2023apopulationbasedstudy pages 10-11): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Zahra Yekta, and Seyed Aria Nejadghaderi. A population-based study on incidence trends of myeloma in the united states over 2000–2020. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47906-y, doi:10.1038/s41598-023-47906-y. This article has 35 citations and is from a peer-reviewed journal.

26. (mousavi2023apopulationbasedstudy media 89dc06ac): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Zahra Yekta, and Seyed Aria Nejadghaderi. A population-based study on incidence trends of myeloma in the united states over 2000–2020. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47906-y, doi:10.1038/s41598-023-47906-y. This article has 35 citations and is from a peer-reviewed journal.

27. (mousavi2023apopulationbasedstudy media e0de6d5f): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Zahra Yekta, and Seyed Aria Nejadghaderi. A population-based study on incidence trends of myeloma in the united states over 2000–2020. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47906-y, doi:10.1038/s41598-023-47906-y. This article has 35 citations and is from a peer-reviewed journal.

28. (mousavi2023apopulationbasedstudy media a18865ac): Seyed Ehsan Mousavi, Mehran Ilaghi, Armin Aslani, Zahra Yekta, and Seyed Aria Nejadghaderi. A population-based study on incidence trends of myeloma in the united states over 2000–2020. Scientific Reports, Nov 2023. URL: https://doi.org/10.1038/s41598-023-47906-y, doi:10.1038/s41598-023-47906-y. This article has 35 citations and is from a peer-reviewed journal.

29. (imounga2023thesingularepidemiology pages 2-4): Laure Manuella Imounga, Kinan Drak Alsibai, Juliette Plenet, Qiannan Wang, Beatrice Virjophe-Cenciu, Pierre Couppie, Nadia Sabbah, Antoine Adenis, and Mathieu Nacher. The singular epidemiology of plasmacytoma and multiple myeloma in french guiana. Cancers, 16:178, Dec 2023. URL: https://doi.org/10.3390/cancers16010178, doi:10.3390/cancers16010178. This article has 5 citations.

30. (mirvis2024arewethere pages 3-4): Eitan Mirvis and Reuben Benjamin. Are we there yet? car‐t therapy in multiple myeloma. British Journal of Haematology, 205:2175-2189, Nov 2024. URL: https://doi.org/10.1111/bjh.19896, doi:10.1111/bjh.19896. This article has 7 citations and is from a domain leading peer-reviewed journal.

31. (ferreri2023realworldexperienceof pages 1-2): Christopher J. Ferreri, Michelle A. T. Hildebrandt, Hamza Hashmi, Leyla O. Shune, Joseph P. McGuirk, Douglas W. Sborov, Charlotte B. Wagner, M. Hakan Kocoglu, Aaron Rapoport, Shebli Atrash, Peter M. Voorhees, Jack Khouri, Danai Dima, Aimaz Afrough, Gurbakhash Kaur, Larry D. Anderson, Gary Simmons, James A. Davis, Nilesh Kalariya, Lauren C. Peres, Yi Lin, Murali Janakiram, Omar Nadeem, Melissa Alsina, Frederick L. Locke, Surbhi Sidana, Doris K. Hansen, Krina K. Patel, and Omar Alexis Castaneda Puglianini. Real-world experience of patients with multiple myeloma receiving ide-cel after a prior bcma-targeted therapy. Blood Cancer Journal, Aug 2023. URL: https://doi.org/10.1038/s41408-023-00886-8, doi:10.1038/s41408-023-00886-8. This article has 127 citations and is from a domain leading peer-reviewed journal.

32. (tacchetti2024bispecificantibodiesfor pages 1-2): Paola Tacchetti, Simona Barbato, Katia Mancuso, Elena Zamagni, and Michele Cavo. Bispecific antibodies for the management of relapsed/refractory multiple myeloma. Cancers, 16:2337, Jun 2024. URL: https://doi.org/10.3390/cancers16132337, doi:10.3390/cancers16132337. This article has 11 citations.

33. (tacchetti2024bispecificantibodiesfor pages 5-6): Paola Tacchetti, Simona Barbato, Katia Mancuso, Elena Zamagni, and Michele Cavo. Bispecific antibodies for the management of relapsed/refractory multiple myeloma. Cancers, 16:2337, Jun 2024. URL: https://doi.org/10.3390/cancers16132337, doi:10.3390/cancers16132337. This article has 11 citations.

34. (parrondo2024bispecificantibodiesfor pages 2-3): Ricardo D. Parrondo, Sikander Ailawadhi, and Claudio Cerchione. Bispecific antibodies for the treatment of relapsed/refractory multiple myeloma: updates and future perspectives. Frontiers in Oncology, Apr 2024. URL: https://doi.org/10.3389/fonc.2024.1394048, doi:10.3389/fonc.2024.1394048. This article has 21 citations.

35. (devasia2024bispecificantibodiesin pages 3-4): Anup Joseph Devasia, Ajai Chari, and Guido Lancman. Bispecific antibodies in the treatment of multiple myeloma. Blood Cancer Journal, Sep 2024. URL: https://doi.org/10.1038/s41408-024-01139-y, doi:10.1038/s41408-024-01139-y. This article has 78 citations and is from a domain leading peer-reviewed journal.

36. (donk2024tcell–redirectingbispecific pages 1-2): Niels W.C.J. van de Donk, Leo Rasche, Surbhi Sidana, Sonja Zweegman, and Alfred L. Garfall. T cell–redirecting bispecific antibodies in multiple myeloma: optimal dosing schedule and duration of treatment. Blood Cancer Discovery, 5:388-399, Sep 2024. URL: https://doi.org/10.1158/2643-3230.bcd-24-0124, doi:10.1158/2643-3230.bcd-24-0124. This article has 17 citations and is from a peer-reviewed journal.

37. (du2024immunocompetentmousemodels pages 3-4): Megan Tien Du, Peter Leif Bergsagel, and Marta Chesi. Immunocompetent mouse models of multiple myeloma. Hematology/Oncology Clinics of North America, 38:533-546, Apr 2024. URL: https://doi.org/10.1016/j.hoc.2023.12.014, doi:10.1016/j.hoc.2023.12.014. This article has 3 citations.

38. (du2024immunocompetentmousemodels pages 4-6): Megan Tien Du, Peter Leif Bergsagel, and Marta Chesi. Immunocompetent mouse models of multiple myeloma. Hematology/Oncology Clinics of North America, 38:533-546, Apr 2024. URL: https://doi.org/10.1016/j.hoc.2023.12.014, doi:10.1016/j.hoc.2023.12.014. This article has 3 citations.

39. (du2024immunocompetentmousemodels pages 6-8): Megan Tien Du, Peter Leif Bergsagel, and Marta Chesi. Immunocompetent mouse models of multiple myeloma. Hematology/Oncology Clinics of North America, 38:533-546, Apr 2024. URL: https://doi.org/10.1016/j.hoc.2023.12.014, doi:10.1016/j.hoc.2023.12.014. This article has 3 citations.

40. (du2024immunocompetentmousemodels pages 8-9): Megan Tien Du, Peter Leif Bergsagel, and Marta Chesi. Immunocompetent mouse models of multiple myeloma. Hematology/Oncology Clinics of North America, 38:533-546, Apr 2024. URL: https://doi.org/10.1016/j.hoc.2023.12.014, doi:10.1016/j.hoc.2023.12.014. This article has 3 citations.

41. (larrayoz2023preclinicalmodelsfor pages 1-2): Marta Larrayoz, Maria J. Garcia-Barchino, Jon Celay, Amaia Etxebeste, Maddalen Jimenez, Cristina Perez, Raquel Ordoñez, Cesar Cobaleda, Cirino Botta, Vicente Fresquet, Sergio Roa, Ibai Goicoechea, Catarina Maia, Miren Lasaga, Marta Chesi, P. Leif Bergsagel, Maria J. Larrayoz, Maria J. Calasanz, Elena Campos-Sanchez, Jorge Martinez-Cano, Carlos Panizo, Paula Rodriguez-Otero, Silvestre Vicent, Giovanna Roncador, Patricia Gonzalez, Satoru Takahashi, Samuel G. Katz, Loren D. Walensky, Shannon M. Ruppert, Elisabeth A. Lasater, Maria Amann, Teresa Lozano, Diana Llopiz, Pablo Sarobe, Juan J. Lasarte, Nuria Planell, David Gomez-Cabrero, Olga Kudryashova, Anna Kurilovich, Maria V. Revuelta, Leandro Cerchietti, Xabier Agirre, Jesus San Miguel, Bruno Paiva, Felipe Prosper, and Jose A. Martinez-Climent. Preclinical models for prediction of immunotherapy outcomes and immune evasion mechanisms in genetically heterogeneous multiple myeloma. Nature Medicine, 29:632-645, Mar 2023. URL: https://doi.org/10.1038/s41591-022-02178-3, doi:10.1038/s41591-022-02178-3. This article has 96 citations and is from a highest quality peer-reviewed journal.

42. (kansal2024towardprecisionmedicine pages 8-10): Rina Kansal. Toward precision medicine for patients with multiple myeloma. Journal of Clinical Haematology, 5:12-33, Jan 2024. URL: https://doi.org/10.33696/haematology.5.058, doi:10.33696/haematology.5.058. This article has 1 citations.

43. (jelinek2023morethan2% pages 6-7): Tomas Jelinek, Renata Bezdekova, David Zihala, Tereza Sevcikova, Anjana Anilkumar Sithara, Lenka Pospisilova, Sabina Sevcikova, Petra Polackova, Martin Stork, Zdenka Knechtova, Ondrej Venglar, Veronika Kapustova, Tereza Popkova, Ludmila Muronova, Zuzana Chyra, Matous Hrdinka, Michal Simicek, Juan-Jose Garcés, Noemi Puig, Maria-Teresa Cedena, Artur Jurczyszyn, Jorge J. Castillo, Miroslav Penka, Jakub Radocha, Maria Victoria Mateos, Jesús F. San-Miguel, Bruno Paiva, Ludek Pour, Lucie Rihova, and Roman Hajek. More than 2% of circulating tumor plasma cells defines plasma cell leukemia–like multiple myeloma. Journal of Clinical Oncology, 41:1383-1392, Mar 2023. URL: https://doi.org/10.1200/jco.22.01226, doi:10.1200/jco.22.01226. This article has 91 citations and is from a highest quality peer-reviewed journal.

44. (jelinek2023morethan2% pages 2-3): Tomas Jelinek, Renata Bezdekova, David Zihala, Tereza Sevcikova, Anjana Anilkumar Sithara, Lenka Pospisilova, Sabina Sevcikova, Petra Polackova, Martin Stork, Zdenka Knechtova, Ondrej Venglar, Veronika Kapustova, Tereza Popkova, Ludmila Muronova, Zuzana Chyra, Matous Hrdinka, Michal Simicek, Juan-Jose Garcés, Noemi Puig, Maria-Teresa Cedena, Artur Jurczyszyn, Jorge J. Castillo, Miroslav Penka, Jakub Radocha, Maria Victoria Mateos, Jesús F. San-Miguel, Bruno Paiva, Ludek Pour, Lucie Rihova, and Roman Hajek. More than 2% of circulating tumor plasma cells defines plasma cell leukemia–like multiple myeloma. Journal of Clinical Oncology, 41:1383-1392, Mar 2023. URL: https://doi.org/10.1200/jco.22.01226, doi:10.1200/jco.22.01226. This article has 91 citations and is from a highest quality peer-reviewed journal.

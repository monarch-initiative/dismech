---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T09:59:23.282955'
end_time: '2026-05-09T10:19:13.544038'
duration_seconds: 1190.26
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Glanders
  mondo_id: ''
  category: Infectious
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 35
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Glanders
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Glanders** covering all of the
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
- **Disease Name:** Glanders
- **MONDO ID:**  (if available)
- **Category:** Infectious

## Research Objectives

Please provide a comprehensive research report on **Glanders** covering all of the
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


# Comprehensive Research Report: Glanders (Infectious disease)

## Executive summary
Glanders is a highly contagious zoonotic disease caused by the Gram-negative, facultative intracellular bacterium *Burkholderia mallei* that primarily affects equids (horses, donkeys, mules) and only rarely infects humans, typically via occupational exposure. Clinically, equine disease classically presents as nasal, pulmonary, and cutaneous/lymphatic forms; the cutaneous form is often called **farcy**. Contemporary control relies on surveillance and early diagnosis (serology plus confirmatory testing) and, in many jurisdictions, euthanasia of infected animals rather than treatment; in humans, aggressive prolonged antibiotic therapy is recommended. Recent (2023–2024) research emphasizes diagnostic challenges from strain genomic variability and demonstrates field-realistic molecular methods (e.g., LAMP) and integrated workflows (culture/PCR/MALDI-TOF/WGS) for confirmation and epidemiologic tracing. (moriya2025detectionofburkholderia pages 1-2, torres2025glandersanancient pages 7-9, charron2023influenceofgenomic pages 1-2, suniga2023glandersdiagnosisin pages 1-2, torres2025glandersanancient pages 9-10)

## Knowledge-base summary table
| Category | Key facts | Citations |
|---|---|---|
| Disease / agent | Glanders is a highly contagious zoonotic disease caused by *Burkholderia mallei*, a nonmotile, facultative intracellular Gram-negative bacterium; cutaneous/lymphatic disease is often termed **farcy**. | (moriya2025detectionofburkholderia pages 1-2, torres2025glandersanancient pages 3-5, burtnick2010burkholderiamalleicluster pages 1-2) |
| Primary hosts / reservoirs | Natural reservoir hosts are mainly equids: horses, donkeys, and mules. Donkeys and mules more often develop acute disease; horses more often have chronic or subclinical infection and may remain occult shedders. Humans are accidental hosts. | (moriya2025detectionofburkholderia pages 1-2, prince2023glandersatreatable pages 1-3, nielsen2022assessmentofthe pages 7-8) |
| Transmission | Spread occurs by direct contact with infected animals/secretions, inoculation through broken skin or harness trauma, inhalation of aerosols/dust, ingestion of contaminated feed/water, and mucosal exposure; human infection is usually occupational and human-to-human transmission is uncommon. | (moriya2025detectionofburkholderia pages 1-2, prince2023glandersatreatable pages 1-3, torres2025glandersanancient pages 7-9) |
| Clinical forms in equids | Main equine presentations: **nasal**, **pulmonary**, and **cutaneous/farcy** forms; acute disease is more common in donkeys/mules and may be rapidly fatal, while horses often show chronic disease with nodules, ulcers, lymphangitis, cough, dyspnea, fever, and weight loss. | (moriya2025detectionofburkholderia pages 1-2, siddique2023burkholderia(malleiand pages 4-7, prince2023glandersatreatable pages 3-5) |
| Clinical forms in humans | Human disease includes cutaneous/localized, pulmonary, chronic/disseminated, and septicemic forms; organ abscesses can involve liver, spleen, and kidneys, and untreated pneumonic disease may be fatal within 10–30 days. | (siddique2023burkholderia(malleiand pages 1-4, siddique2023burkholderia(malleiand pages 4-7, torres2025glandersanancient pages 7-9) |
| Key diagnostics | Standard veterinary diagnosis relies on serology, especially **complement fixation test (CFT)**; confirmatory/adjunct methods include **mallein testing**, ELISA, western blot, culture, PCR, MALDI-TOF, and WGS. Culture is definitive but often insensitive in field samples. | (tikmehdash2024isolationserologicaland pages 1-2, suniga2023glandersdiagnosisin pages 1-2, torres2025glandersanancient pages 7-9) |
| Recent diagnostic development: antigen variation | Integrative genomics/transcriptomics showed major strain-to-strain variability affecting serodiagnostic antigens: **31–715 gene presence/absence differences** (mean 334) and **388 differentially expressed genes** between two reference strains, explaining variable serologic performance across lineages. | (charron2023influenceofgenomic pages 1-2) |
| Recent diagnostic development: Iran field screening | In East Azerbaijan, Iran, **350 horses** were screened: **11 CFT-positive**, of which **6** were confirmed by malleination and **5** were false positives; **1 CFT-negative** horse was positive by mallein/ELISA/PCR, for **7 total diagnosed cases**. Authors recommend ELISA as a complement to CFT. | (tikmehdash2024isolationserologicaland pages 1-2) |
| Recent diagnostic development: Brazil genomic case confirmation | An asymptomatic Brazilian mare was diagnosed by serology, culture, PCR, MALDI-TOF, and WGS; the isolate belonged to **lineage 3, sublineage 2**, with a **5.51 Mb** genome, **65.8% GC**, **5871 genes**, and **5583 CDSs**. | (suniga2023glandersdiagnosisin pages 1-2, suniga2023glandersdiagnosisin pages 5-7) |
| Recent diagnostic development: LAMP / molecular testing | A dried-format LAMP assay targeting the ITS region detected **10 genomic copies** of *B. mallei* DNA and showed **87.5% agreement** with real-time PCR on positive equine swabs and **100% agreement** on negatives, offering a simpler field-deployable alternative where PCR resources are limited. | (nakase2025anovelreadytouse pages 1-2) |
| Quantitative epidemiology | Brazil reported **3385 glanders cases (1999–2022)**, including **715 cases in the most recent 3 years**; a Pará study estimated **1.68% prevalence of infected properties**. In one Brazilian outbreak series, **37.5%** of infected horses were asymptomatic and culture yielded only **8.2%** positivity despite PCR confirmation in all tested animals. | (suniga2023glandersdiagnosisin pages 1-2, torres2025glandersanancient pages 5-7) |
| Geographic distribution | Current endemic/re-emerging areas include Brazil, India, Iran, Iraq, Pakistan, Mongolia, parts of the Middle East, Northern Africa, and South/Central America; many formerly affected regions eradicated glanders during the 20th century. | (torres2025glandersanancient pages 1-3, torres2025glandersanancient pages 5-7, nielsen2022assessmentofthe pages 7-8) |
| Pathophysiology / virulence | Important mechanisms include intracellular survival, vacuolar escape, actin-based motility, multinucleated giant-cell formation, serum resistance, capsule/LPS-mediated immune evasion, and virulence functions mediated by **T3SS**, **T6SS-1**, **VirAG**, **Hcp1**, and **BimA**. | (burtnick2010burkholderiamalleicluster pages 1-2, burtnick2010burkholderiamalleicluster pages 6-7, burtnick2010burkholderiamalleicluster pages 2-3, siddique2023burkholderia(malleiand pages 1-4) |
| Treatment | For animals, treatment is generally discouraged because eradication is unreliable and zoonotic risk persists; policy usually favors euthanasia. For humans, expert reviews support an intensive IV phase (**ceftazidime, imipenem, or meropenem for 10–14 days**) followed by an eradication phase (**doxycycline or trimethoprim–sulfamethoxazole for 3–6 months**). | (torres2025glandersanancient pages 9-10, torres2025glandersanancient pages 7-9, prince2023glandersatreatable pages 5-7) |
| Prevention / control | No licensed vaccine exists for humans or animals. Control depends on surveillance, quarantine, testing of exposed equids, euthanasia of infected animals, carcass/material decontamination, and biosecurity. *B. mallei* is susceptible to common disinfectants, heat, and UV. | (prince2023glandersatreatable pages 7-10, torres2025glandersanancient pages 9-10, torres2025glandersanancient pages 1-3) |
| Vaccine research / notable antigen | **Hcp1** is a leading antigen in diagnostics and vaccine development; experimental platforms include CPS-CRM197 + Hcp1, Hcp1-LPS glycoconjugates, live-attenuated mutants (e.g., ΔtonB, CLH001), and gold nanoparticle vaccines. Protection in animals is promising but partial/variable, and no candidate is licensed. | (badten2024burkholderiapseudomalleicomplex pages 13-14, torres2025glandersanancient pages 9-10, biryukov2022evaluationoftwo pages 1-2, torres2025glandersanancient pages 7-9) |


*Table: This table condenses disease-definition, clinical, epidemiologic, diagnostic, mechanistic, and intervention facts about glanders into a knowledge-base-ready format. It emphasizes recent quantitative findings and links each row to supporting context IDs for traceability.*

---

## 1. Disease information
### 1.1 Definition and overview
Glanders is an infectious zoonosis caused by *B. mallei*; it is historically important (including biothreat concerns) and remains re-emerging/endemic in parts of Asia, the Middle East, Africa, and South America. (torres2025glandersanancient pages 3-5, torres2025glandersanancient pages 1-3)

Key clinical concept: equine glanders is commonly described in **nasal**, **pulmonary**, and **cutaneous** forms; the cutaneous/lymphatic form is termed **farcy**. (moriya2025detectionofburkholderia pages 1-2, torres2025glandersanancient pages 7-9)

### 1.2 Synonyms and alternative names
- **Farcy**: term commonly used for cutaneous/lymphatic glanders. (moriya2025detectionofburkholderia pages 1-2, torres2025glandersanancient pages 7-9)
- **Mormo**: common term in Brazilian/Portuguese veterinary literature (e.g., 2023–2024 Brazilian works indexed under “mormo”). (suniga2023glandersdiagnosisin pages 1-2)

### 1.3 Key identifiers (ontology and classification)
This tool-assisted literature retrieval did **not** return authoritative ontology mappings (MONDO ID, MeSH ID, Orphanet, ICD-10/ICD-11 codes) within the retrieved full-text evidence. Consequently, this report cannot cite those identifiers from primary sources in-context and flags them as **not available in the current evidence set**.

### 1.4 Evidence sources: individual vs aggregated
Most mechanistic assertions here derive from controlled in vitro or animal-model studies (e.g., macrophage infection models) and expert reviews synthesizing multiple sources, while clinical/epidemiologic data include outbreak/case reports and regional surveillance screening studies. (suniga2023glandersdiagnosisin pages 1-2, torres2025glandersanancient pages 9-10, burtnick2010burkholderiamalleicluster pages 1-2)

---

## 2. Etiology
### 2.1 Primary causal factor
Glanders is caused by *Burkholderia mallei*, a nonmotile, facultative intracellular Gram-negative bacillus. (burtnick2010burkholderiamalleicluster pages 1-2)

### 2.2 Transmission and risk factors
**Equids (primary reservoir):** transmission occurs through direct contact with infected animals/secretions, inhalation of aerosols/dust, ingestion of contaminated feed/water, and inoculation via skin trauma (e.g., harness-related). Asymptomatic carriers can intermittently shed bacteria. (moriya2025detectionofburkholderia pages 1-2, prince2023glandersatreatable pages 3-5)

**Humans (accidental host):** exposure is usually occupational (animal handlers, veterinarians, laboratory exposure) via broken skin, inhalation, or mucosal contact; human-to-human transmission is described as uncommon/rare. (prince2023glandersatreatable pages 1-3, torres2025glandersanancient pages 7-9)

### 2.3 Protective factors
No specific host genetic protective variants or validated environmental protective factors were identified in the retrieved evidence corpus.

### 2.4 Gene–environment interactions
Not applicable in the classic human genetics sense; disease is primarily infectious. However, exposure context (animal husbandry, animal movement/importation, and biosecurity) strongly modifies risk. (prince2023glandersatreatable pages 7-10)

---

## 3. Phenotypes (clinical presentation)
### 3.1 Equids: phenotype catalog
**Nasal glanders:** pustules/ulcers of nasal mucosa (conchae/septum), sticky/yellow discharge, and regional lymphadenopathy. (moriya2025detectionofburkholderia pages 1-2)

**Pulmonary glanders:** nodular abscesses in lungs with cough, dyspnea, systemic illness/fever; can progress to pneumonia. (moriya2025detectionofburkholderia pages 1-2)

**Cutaneous/lymphatic glanders (farcy):** nodular lymphangitis with abscess “buds” (~0.5–2.5 cm) that ulcerate and discharge; enlarged lymphatics. (moriya2025detectionofburkholderia pages 1-2, torres2025glandersanancient pages 7-9)

**Course differences by species:** donkeys/mules more often show acute disease that can be rapidly fatal; horses often develop chronic disease and may survive for years, including occult carriage. (moriya2025detectionofburkholderia pages 1-2, torres2025glandersanancient pages 3-5)

**Asymptomatic infection:** an important transmission-relevant state; review evidence reports 37.5% asymptomatic among infected horses in a Brazilian outbreak series. (torres2025glandersanancient pages 5-7)

**Suggested HPO terms (examples):**
- Fever (HP:0001945)
- Cough (HP:0012735)
- Dyspnea (HP:0002094)
- Nasal discharge (HP:0001738)
- Nasal ulceration (HP:0032474) / mucosal ulceration (HP:0001074)
- Pneumonia (HP:0002090)
- Skin ulcer (HP:0001059)
- Lymphangitis (HP:0001045)
- Lymphadenopathy (HP:0002716)

### 3.2 Humans: phenotype catalog
Human presentations include cutaneous/local disease (papular lesions that ulcerate), pulmonary disease (can progress to pneumonia/abscess), disseminated/chronic disease, and septicemic disease with internal organ abscesses (e.g., liver, spleen, kidneys). (siddique2023burkholderia(malleiand pages 4-7, torres2025glandersanancient pages 7-9)

**Temporal note:** incubation is variable; acute cases may occur within 1–14 days and chronic disease can develop over weeks; untreated pneumonic cases may be fatal within 10–30 days. (torres2025glandersanancient pages 7-9)

**Suggested HPO terms (examples):**
- Skin papule (HP:0010011)
- Sepsis (HP:0100806)
- Liver abscess (HP:0031151)
- Splenic abscess (no direct HPO term commonly used; can map to Splenomegaly HP:0001744 and “abscess” phenotypes as appropriate)

### 3.3 Quality-of-life impact
The retrieved evidence set did not include standardized QoL instrument data (e.g., EQ-5D/SF-36) for glanders.

---

## 4. Genetic / molecular information
### 4.1 Human causal genes
Not applicable: glanders is not a monogenic or polygenic inherited disorder.

### 4.2 Pathogen genetic features relevant to disease
Whole-genome sequencing of a Brazilian outbreak isolate (BAC 86/19) yielded a genome size ~5.51 Mb and enabled assignment to lineage 3, sublineage 2. (suniga2023glandersdiagnosisin pages 1-2, suniga2023glandersdiagnosisin pages 5-7)

**Diagnostic relevance of pathogen genome plasticity:** a 2023 integrative genomics/transcriptomics study reported large gene content differences across *B. mallei* isolates and showed that some serodiagnostic antigens may be lost due to structural variation, complicating serologic diagnosis. (charron2023influenceofgenomic pages 1-2)

Abstract-anchored quote supporting this point: Charron et al. reported “differences in gene content ranging from 31 to 715 genes with an average of 334 gene presence-absence variations,” and that affected genes “included some encoded proteins used as serodiagnostic antigens.” (charron2023influenceofgenomic pages 1-2)

### 4.3 Epigenetics / chromosomal abnormalities
Not applicable to host genetics in this evidence set; no pathogen epigenetic mechanisms were retrieved.

---

## 5. Environmental information
Environmental risk factors in the retrieved evidence are primarily **exposure-related** (contact with infected equids or contaminated materials) rather than environmental reservoirs (unlike *B. pseudomallei*). Transmission is supported by inhalation/ingestion/mucosal routes, and control emphasizes disinfection and biosecurity. (moriya2025detectionofburkholderia pages 1-2, prince2023glandersatreatable pages 7-10)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (conceptual)
**Exposure → entry (mucosa, inhalation, broken skin) → intracellular infection → dissemination and suppurative lesions → clinical disease**.

Mechanistic evidence supports that *B. mallei* is facultative intracellular, escapes endocytic vacuoles, enters host cytoplasm, and uses actin-based motility for intra-/intercellular spread—processes that link early infection to tissue lesions and dissemination. (burtnick2010burkholderiamalleicluster pages 1-2)

### 6.2 Virulence factors and pathways
Key virulence determinants include:
- **Type III secretion system (T3SS)**: essential for early vacuolar escape and access to intracellular actin pools, supporting actin-based motility and multinucleated giant cell formation. (burtnick2010burkholderiamalleicluster pages 1-2)
- **Type VI secretion system cluster 1 (T6SS-1)**: required for virulence; mutants (e.g., *tssE*) show intracellular growth defects, impaired actin polymerization, and failure to induce multinucleated giant cell formation in macrophages. (burtnick2010burkholderiamalleicluster pages 1-2, burtnick2010burkholderiamalleicluster pages 6-7)
- **Capsule / LPS-associated immune evasion**: capsule described as preventing immune killing; LPS-associated serum resistance is implicated by survival in normal human serum and loss of LPS in serum-sensitive strains. (siddique2023burkholderia(malleiand pages 1-4)

### 6.3 Immune responses (host)
A 2025 expert review summarizes immunologic observations in naturally infected equids, reporting strong IgG responses and elevated cytokines including IL-1β, MCP-1, IL-17, IL-6, IFN-γ, and TNF-α, and highlights Hcp1 as a prominent antigenic target. (torres2025glandersanancient pages 7-9, torres2025glandersanancient media 41fd19e0)

### 6.4 Suggested ontology terms for mechanisms
**GO Biological Process (examples):**
- GO:0052040 “negative regulation by symbiont of host immune response” (conceptual fit for immune evasion)
- GO:0030260 “bacterial-type flagellum-dependent cell motility” is *not* appropriate for *B. mallei* (non-motile); instead consider actin-based intracellular movement processes (host actin polymerization)
- GO:0075525 “interleukin-17 production” (host response; aligns with reported IL-17 elevation)

**Cell Ontology (CL) cell types (examples):**
- CL:0000236 macrophage (supported by macrophage infection model data) (burtnick2010burkholderiamalleicluster pages 1-2)

---

## 7. Anatomical structures affected
**Primary (equids):**
- Respiratory system: lung (UBERON:0002048), nasal mucosa (UBERON:0001825)
- Integumentary/lymphatic: skin (UBERON:0002097), lymphatic vessel (UBERON:0001986), lymph node (UBERON:0000029) (conceptually consistent with lymphangitis/lymphadenopathy) (moriya2025detectionofburkholderia pages 1-2, torres2025glandersanancient pages 7-9)

**Humans:** pulmonary involvement and systemic organ abscesses (liver, spleen, kidneys). (torres2025glandersanancient pages 7-9)

---

## 8. Temporal development
- **Onset:** acute disease can occur within ~1–14 days post-exposure; chronic disease can develop over weeks (reported up to ~12 weeks). (torres2025glandersanancient pages 7-9)
- **Course:** equids may be acute (especially donkeys/mules) or chronic (often horses); humans may present with pulmonary, chronic/disseminated, or septicemic forms. (torres2025glandersanancient pages 3-5, torres2025glandersanancient pages 7-9)

---

## 9. Inheritance and population
Not applicable (infectious disease). Epidemiology is driven by animal movement, biosecurity, and regional endemicity. (torres2025glandersanancient pages 5-7)

---

## 10. Diagnostics
### 10.1 Current practice and limitations
Diagnosis in animals is “heavily reliant on serological tests” in many settings, and culture can be hazardous and insensitive in field samples. (suniga2023glandersdiagnosisin pages 1-2, tikmehdash2024isolationserologicaland pages 1-2)

### 10.2 Recent developments (prioritized 2023–2024)
1) **Integrated confirmation + genomic epidemiology (Brazil; published Oct 2023)**
- Multi-pronged diagnosis (serology, culture, PCR, MALDI-TOF, WGS) confirmed *B. mallei* from an asymptomatic mare in a 2019 outbreak; WGS provided lineage assignment and genomic parameters. (suniga2023glandersdiagnosisin pages 1-2, suniga2023glandersdiagnosisin pages 5-7)
- Abstract quote: “The diagnosis was established through a multi-pronged approach encompassing microbiological culture, mass spectrometry, and genome sequencing.” (suniga2023glandersdiagnosisin pages 1-2)

2) **Strain variation undermining serodiagnosis (Frontiers in Veterinary Science; Dec 2023)**
- Gene presence/absence variation and differential expression affect antigens used for serology; this is directly relevant to test robustness across endemic regions. (charron2023influenceofgenomic pages 1-2)

3) **Field screening performance and false positives (Iran; May 2024)**
- Screening of 350 horses: 11 CFT-positive, 6 confirmed by mallein, 5 false positives; 1 CFT-negative but positive on mallein/ELISA/PCR; total 7 diagnosed. (tikmehdash2024isolationserologicaland pages 1-2)

4) **Operational molecular diagnostics for resource-limited settings (LAMP; Jan 2025; included due to strong “implementation” relevance)**
- Dried-format LAMP targeting ITS detected 10 genomic copies and matched real-time PCR with 87.5% agreement for positives and 100% for negatives on equine swabs, supporting deployment where PCR is constrained. (nakase2025anovelreadytouse pages 1-2)

### 10.3 Differential diagnosis
The retrieved evidence set did not provide a systematic differential diagnosis list; in practice, differentials include other causes of equine respiratory disease, ulcerative nasal disease, and nodular cutaneous/lymphangitic syndromes.

---

## 11. Outcome / prognosis
- **Humans:** severe disease can have high mortality if untreated; untreated pneumonic cases may be fatal within 10–30 days. (moriya2025detectionofburkholderia pages 1-2, torres2025glandersanancient pages 7-9)
- **Equids:** acute disease can be rapidly fatal; chronic disease may persist for years and can be associated with ongoing shedding. (moriya2025detectionofburkholderia pages 1-2, torres2025glandersanancient pages 3-5)

The evidence set did not provide modern survival curves or population-level case-fatality rates for 2023–2024.

---

## 12. Treatment
### 12.1 Human treatment (expert synthesis)
A 2025 expert review recommends prolonged, aggressive antimicrobial therapy guided by susceptibility testing and experience from melioidosis: an intensive IV phase (10–14 days; ceftazidime, imipenem, or meropenem), followed by a prolonged eradication phase (3–6 months; doxycycline or trimethoprim–sulfamethoxazole). (torres2025glandersanancient pages 9-10)

**Suggested MAXO terms (examples):**
- MAXO:0000746 antibiotic therapy
- NCIT:C15986 intravenous drug administration

### 12.2 Veterinary treatment vs policy
International veterinary policy generally discourages treating infected equids (due to relapse and zoonotic risk) and favors euthanasia plus quarantine/testing for contacts. (torres2025glandersanancient pages 9-10, torres2025glandersanancient pages 7-9)

Nevertheless, a field treatment example cited in a 2023 review describes 23 horses treated over 84 days with oral doxycycline, IV enrofloxacin, and trimethoprim+sulphadiazine, with no relapses reported at end of therapy and negative follow-up indicators (e.g., sentinel horses/foals). (prince2023glandersatreatable pages 5-7)

**Suggested MAXO terms (examples):**
- MAXO:0001084 euthanasia
- MAXO:0000746 antibiotic therapy
- MAXO:0000915 quarantine

---

## 13. Prevention
### 13.1 Vaccine status
No licensed vaccine exists for humans or animals. (torres2025glandersanancient pages 9-10)

### 13.2 Public health / veterinary control measures
Control measures include surveillance and testing, strict quarantine of exposed animals, euthanasia of confirmed cases, and thorough disinfection and disposal of contaminated materials. (prince2023glandersatreatable pages 7-10, torres2025glandersanancient pages 7-9)

### 13.3 Recent vaccine research and expert analysis (including 2023–2024)
A 2024 review of *Burkholderia* pseudomallei complex vaccines highlights Hcp1 (a T6SS component) as an important immunogenic target in natural infection and summarizes mouse data where intranasal Hcp1 with adjuvants produced substantial protection; glycoconjugate approaches (e.g., Hcp1-LPS constructs on gold nanoparticles) can enhance LPS-specific antibody responses and protection. (badten2024burkholderiapseudomalleicomplex pages 13-14)

Expert limitations highlighted across reviews include: safety concerns for live-attenuated vaccines (reversion/persistence), incomplete protection against chronic disease or high-dose exposures, and dependence on immunization route/adjuvant. (torres2025glandersanancient pages 9-10, biryukov2022evaluationoftwo pages 1-2)

---

## 14. Other species / natural disease
Beyond equids and humans, occasional infections have been reported in other mammals (e.g., felids, camels, dogs), while cattle and pigs are described as resistant in an expert review. (torres2025glandersanancient pages 3-5)

Zoonotic acquisition can occur via direct contact and, in carnivores, by consumption of infected meat. (torres2025glandersanancient pages 3-5, prince2023glandersatreatable pages 1-3)

---

## 15. Model organisms and experimental systems
- **In vitro:** murine RAW 264.7 macrophage infection models are used to dissect intracellular survival, secretion-system function, actin polymerization, and cell-to-cell spread. (burtnick2010burkholderiamalleicluster pages 1-2, burtnick2010burkholderiamalleicluster pages 6-7)
- **In vivo (preclinical):** mouse intranasal/aerosol challenge models are widely used for vaccine down-selection and immune correlate discovery for *B. mallei* and related *B. pseudomallei*. (biryukov2022evaluationoftwo pages 1-2)

---

## Recent developments and real-world implementations (2023–2024 focus)
1) **Genomics informing surveillance and diagnostics**: WGS-confirmed Brazilian outbreak isolate lineage assignment (lineage 3, sublineage 2) illustrates how genomics supports tracing and diagnostic development. (Published Oct 2023; https://doi.org/10.3390/pathogens12101250) (suniga2023glandersdiagnosisin pages 1-2)

2) **Evidence-based critique of serodiagnostic robustness**: 2023 genomics/transcriptomics study demonstrates that antigen loss/differential expression can undermine serology across *B. mallei* diversity—an actionable warning for national screening programs. (Published Dec 2023; https://doi.org/10.3389/fvets.2023.1217135) (charron2023influenceofgenomic pages 1-2)

3) **Screening data demonstrating CFT false positives in practice**: Iran screening study highlights how combining CFT with mallein, ELISA, and PCR improves classification (e.g., 5/11 CFT positives were false positives). (Published May 2024; https://doi.org/10.30466/vrf.2024.2010651.4002) (tikmehdash2024isolationserologicaland pages 1-2)

---

## Key quantitative statistics (recent)
- Brazil reported **3,385 cases (1999–2022)** and **715 cases in the last three years**, per Ministry of Agriculture and Livestock data accessed 5 Oct 2023. (suniga2023glandersdiagnosisin pages 1-2)
- In a Brazilian outbreak series summarized in a 2025 review: **37.5% asymptomatic** among infected horses; PCR positive in all tested animals; **culture isolation 8.2%** of samples. (torres2025glandersanancient pages 5-7)
- Iran screening (2020–2022 sampling; published 2024): **350 horses** screened; **7 diagnosed cases**, including a CFT-negative but mallein/ELISA/PCR-positive animal. (tikmehdash2024isolationserologicaland pages 1-2)

---

## Image-based evidence (cropped text from expert review)
The following extracted regions from a 2025 expert review capture compact statements about (i) clinical forms and (ii) immune response markers (Hcp1 and cytokines) and (iii) diagnostic modalities and transmission routes, supporting key summary claims. (torres2025glandersanancient media e5c7470e, torres2025glandersanancient media 41fd19e0, torres2025glandersanancient media 90115587, torres2025glandersanancient media c5f72073)

---

## Gaps and limitations of the current evidence package
- Formal disease identifiers (MONDO, MeSH, ICD-10/ICD-11, Orphanet) were not retrievable from the current document set and therefore cannot be cited here.
- 2023–2024 global incidence/prevalence estimates (beyond Brazil-specific counts accessed in 2023 and regional screening studies) were not available in the retrieved corpus; up-to-date WOAH/WAHIS or national surveillance bulletins would be required for 2023–2024 global statistics.
- Limited information was retrieved on imaging criteria, formal differential diagnosis lists, and standardized quality-of-life outcomes.


References

1. (moriya2025detectionofburkholderia pages 1-2): Jéssica Cristine K. Moriya, P. Suniga, Ana Clara L. Araújo, Maria Goretti Dos Santos, Juliana S. G. Rieger, Cynthia Mantovani, Rodrigo Jardim, Márcio Roberto Silva, Flábio R. Araújo, and L. R. Santos. Detection of burkholderia mallei in microbiological culture: a comparative analysis of pcr primer sets. Pathogens, Aug 2025. URL: https://doi.org/10.3390/pathogens14080766, doi:10.3390/pathogens14080766. This article has 0 citations.

2. (torres2025glandersanancient pages 7-9): Alfredo G. Torres. Glanders: an ancient and emergent disease with no vaccine or treatment on site. PLOS Neglected Tropical Diseases, 19:e0013160, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013160, doi:10.1371/journal.pntd.0013160. This article has 10 citations and is from a domain leading peer-reviewed journal.

3. (charron2023influenceofgenomic pages 1-2): Philippe Charron, Ruimin Gao, John Chmara, Emily Hoover, Susan Nadin-Davis, Danielle Chauvin, Jennifer Hazelwood, Kennedy Makondo, Marc-Olivier Duceppe, and Mingsong Kang. Influence of genomic variations on glanders serodiagnostic antigens using integrative genomic and transcriptomic approaches. Frontiers in Veterinary Science, Dec 2023. URL: https://doi.org/10.3389/fvets.2023.1217135, doi:10.3389/fvets.2023.1217135. This article has 1 citations and is from a peer-reviewed journal.

4. (suniga2023glandersdiagnosisin pages 1-2): Paula Adas Pereira Suniga, Cynthia Mantovani, Maria Goretti dos Santos, Andréa Alves do Egito, Newton Valério Verbisck, Lenita Ramires dos Santos, Alberto Martín Rivera Dávila, Cristina Kraemer Zimpel, Maria Carolina Sisco Zerpa, Daniela Pontes Chiebao, Ana Márcia de Sá Guimarães, Alessandra Figueiredo de Castro Nassar, and Flábio Ribeiro de Araújo. Glanders diagnosis in an asymptomatic mare from brazil: insights from serology, microbiological culture, mass spectrometry, and genome sequencing. Pathogens, 12:1250, Oct 2023. URL: https://doi.org/10.3390/pathogens12101250, doi:10.3390/pathogens12101250. This article has 8 citations.

5. (torres2025glandersanancient pages 9-10): Alfredo G. Torres. Glanders: an ancient and emergent disease with no vaccine or treatment on site. PLOS Neglected Tropical Diseases, 19:e0013160, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013160, doi:10.1371/journal.pntd.0013160. This article has 10 citations and is from a domain leading peer-reviewed journal.

6. (torres2025glandersanancient pages 3-5): Alfredo G. Torres. Glanders: an ancient and emergent disease with no vaccine or treatment on site. PLOS Neglected Tropical Diseases, 19:e0013160, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013160, doi:10.1371/journal.pntd.0013160. This article has 10 citations and is from a domain leading peer-reviewed journal.

7. (burtnick2010burkholderiamalleicluster pages 1-2): Mary N. Burtnick, David DeShazer, Vinod Nair, Frank C. Gherardini, and Paul J. Brett. <i>burkholderia mallei</i> cluster 1 type vi secretion mutants exhibit growth and actin polymerization defects in raw 264.7 murine macrophages. Infection and Immunity, 78:88-99, Jan 2010. URL: https://doi.org/10.1128/iai.00985-09, doi:10.1128/iai.00985-09. This article has 116 citations and is from a peer-reviewed journal.

8. (prince2023glandersatreatable pages 1-3): K Prince, M Uzair, and A Ramay. Glanders: a treatable disease. Unknown journal, 2023.

9. (nielsen2022assessmentofthe pages 7-8): Søren Saxmose Nielsen, Julio Alvarez, Dominique Joseph Bicout, Paolo Calistri, Elisabetta Canali, Julian Ashley Drewe, Bruno Garin‐Bastuji, José Luis Gonzales Rojas, Christian Gortázar Schmidt, Mette Herskin, Virginie Michel, Miguel Ángel Miranda Chueca, Barbara Padalino, Paolo Pasquali, Hans Spoolder, Karl Ståhl, Antonio Velarde, Arvo Viltrop, Christoph Winckler, Simon Gubbins, Karine Laroucau, Sotiria‐Eleni Antoniou, Inma Aznar, Alessandro Broglia, Eliana Lima, Yves Van der Stede, Gabriele Zancanaro, and Helen Clare Roberts. Assessment of the control measures of the category a diseases of animal health law: burkholderia mallei (glanders). EFSA Journal, Jan 2022. URL: https://doi.org/10.2903/j.efsa.2022.7069, doi:10.2903/j.efsa.2022.7069. This article has 7 citations and is from a peer-reviewed journal.

10. (siddique2023burkholderia(malleiand pages 4-7): MH Siddique, MA Samad, and A Memoon. Burkholderia (mallei and pseudomallei) related zoonosis drastic zoonotic and biological warfare potential. International Journal of Agriculture and Biosciences, 2023. URL: https://doi.org/10.47278/book.zoon/2023.140, doi:10.47278/book.zoon/2023.140. This article has 4 citations.

11. (prince2023glandersatreatable pages 3-5): K Prince, M Uzair, and A Ramay. Glanders: a treatable disease. Unknown journal, 2023.

12. (siddique2023burkholderia(malleiand pages 1-4): MH Siddique, MA Samad, and A Memoon. Burkholderia (mallei and pseudomallei) related zoonosis drastic zoonotic and biological warfare potential. International Journal of Agriculture and Biosciences, 2023. URL: https://doi.org/10.47278/book.zoon/2023.140, doi:10.47278/book.zoon/2023.140. This article has 4 citations.

13. (tikmehdash2024isolationserologicaland pages 1-2): H. T. Tikmehdash, Alireza Dehnad, N. Mosavari, Behroz Naghili Hokmabadi, and Sanaz Mahmazi. Isolation, serological and molecular methods in screening of burkholderia mallei in east azerbaijan province, iran. Veterinary Research Forum, 15:231-236, May 2024. URL: https://doi.org/10.30466/vrf.2024.2010651.4002, doi:10.30466/vrf.2024.2010651.4002. This article has 3 citations.

14. (suniga2023glandersdiagnosisin pages 5-7): Paula Adas Pereira Suniga, Cynthia Mantovani, Maria Goretti dos Santos, Andréa Alves do Egito, Newton Valério Verbisck, Lenita Ramires dos Santos, Alberto Martín Rivera Dávila, Cristina Kraemer Zimpel, Maria Carolina Sisco Zerpa, Daniela Pontes Chiebao, Ana Márcia de Sá Guimarães, Alessandra Figueiredo de Castro Nassar, and Flábio Ribeiro de Araújo. Glanders diagnosis in an asymptomatic mare from brazil: insights from serology, microbiological culture, mass spectrometry, and genome sequencing. Pathogens, 12:1250, Oct 2023. URL: https://doi.org/10.3390/pathogens12101250, doi:10.3390/pathogens12101250. This article has 8 citations.

15. (nakase2025anovelreadytouse pages 1-2): Mitsuru Nakase, Jeewan Thapa, Vanaabaatar Batbaatar, Ochirbat Khurtsbaatar, Batchuluun Enkhtuul, Jugderkhorloo Unenbat, Baasansuren Lkham, Sachiho Fujita, Ai Koshikawa, Apichai Tuanyok, Vannarat Saechan, Hideaki Higashi, Kyoko Hayashida, Yasuhiko Suzuki, Chie Nakajima, and Takashi Kimura. A novel ready-to-use loop-mediated isothermal amplification (lamp) method for detection of burkholderia mallei and b. pseudomallei. BMC Microbiology, Jan 2025. URL: https://doi.org/10.1186/s12866-024-03737-z, doi:10.1186/s12866-024-03737-z. This article has 4 citations and is from a peer-reviewed journal.

16. (torres2025glandersanancient pages 5-7): Alfredo G. Torres. Glanders: an ancient and emergent disease with no vaccine or treatment on site. PLOS Neglected Tropical Diseases, 19:e0013160, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013160, doi:10.1371/journal.pntd.0013160. This article has 10 citations and is from a domain leading peer-reviewed journal.

17. (torres2025glandersanancient pages 1-3): Alfredo G. Torres. Glanders: an ancient and emergent disease with no vaccine or treatment on site. PLOS Neglected Tropical Diseases, 19:e0013160, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013160, doi:10.1371/journal.pntd.0013160. This article has 10 citations and is from a domain leading peer-reviewed journal.

18. (burtnick2010burkholderiamalleicluster pages 6-7): Mary N. Burtnick, David DeShazer, Vinod Nair, Frank C. Gherardini, and Paul J. Brett. <i>burkholderia mallei</i> cluster 1 type vi secretion mutants exhibit growth and actin polymerization defects in raw 264.7 murine macrophages. Infection and Immunity, 78:88-99, Jan 2010. URL: https://doi.org/10.1128/iai.00985-09, doi:10.1128/iai.00985-09. This article has 116 citations and is from a peer-reviewed journal.

19. (burtnick2010burkholderiamalleicluster pages 2-3): Mary N. Burtnick, David DeShazer, Vinod Nair, Frank C. Gherardini, and Paul J. Brett. <i>burkholderia mallei</i> cluster 1 type vi secretion mutants exhibit growth and actin polymerization defects in raw 264.7 murine macrophages. Infection and Immunity, 78:88-99, Jan 2010. URL: https://doi.org/10.1128/iai.00985-09, doi:10.1128/iai.00985-09. This article has 116 citations and is from a peer-reviewed journal.

20. (prince2023glandersatreatable pages 5-7): K Prince, M Uzair, and A Ramay. Glanders: a treatable disease. Unknown journal, 2023.

21. (prince2023glandersatreatable pages 7-10): K Prince, M Uzair, and A Ramay. Glanders: a treatable disease. Unknown journal, 2023.

22. (badten2024burkholderiapseudomalleicomplex pages 13-14): Alexander J. Badten and Alfredo G. Torres. Burkholderia pseudomallei complex subunit and glycoconjugate vaccines and their potential to elicit cross-protection to burkholderia cepacia complex. Vaccines, 12:313, Mar 2024. URL: https://doi.org/10.3390/vaccines12030313, doi:10.3390/vaccines12030313. This article has 10 citations.

23. (biryukov2022evaluationoftwo pages 1-2): Sergei S. Biryukov, Christopher K. Cote, Christopher P. Klimko, Jennifer L. Dankmeyer, Nathaniel O. Rill, Jennifer L. Shoe, Melissa Hunter, Zain Shamsuddin, Ivan Velez, Zander M. Hedrick, Raysa Rosario-Acevedo, Yuli Talyansky, Lindsey K. Schmidt, Caitlyn E. Orne, David P. Fetterer, Mary N. Burtnick, Paul J. Brett, Susan L. Welkos, and David DeShazer. Evaluation of two different vaccine platforms for immunization against melioidosis and glanders. Frontiers in Microbiology, Aug 2022. URL: https://doi.org/10.3389/fmicb.2022.965518, doi:10.3389/fmicb.2022.965518. This article has 25 citations and is from a peer-reviewed journal.

24. (torres2025glandersanancient media 41fd19e0): Alfredo G. Torres. Glanders: an ancient and emergent disease with no vaccine or treatment on site. PLOS Neglected Tropical Diseases, 19:e0013160, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013160, doi:10.1371/journal.pntd.0013160. This article has 10 citations and is from a domain leading peer-reviewed journal.

25. (torres2025glandersanancient media e5c7470e): Alfredo G. Torres. Glanders: an ancient and emergent disease with no vaccine or treatment on site. PLOS Neglected Tropical Diseases, 19:e0013160, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013160, doi:10.1371/journal.pntd.0013160. This article has 10 citations and is from a domain leading peer-reviewed journal.

26. (torres2025glandersanancient media 90115587): Alfredo G. Torres. Glanders: an ancient and emergent disease with no vaccine or treatment on site. PLOS Neglected Tropical Diseases, 19:e0013160, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013160, doi:10.1371/journal.pntd.0013160. This article has 10 citations and is from a domain leading peer-reviewed journal.

27. (torres2025glandersanancient media c5f72073): Alfredo G. Torres. Glanders: an ancient and emergent disease with no vaccine or treatment on site. PLOS Neglected Tropical Diseases, 19:e0013160, Jun 2025. URL: https://doi.org/10.1371/journal.pntd.0013160, doi:10.1371/journal.pntd.0013160. This article has 10 citations and is from a domain leading peer-reviewed journal.

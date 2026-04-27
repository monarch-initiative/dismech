---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:47.915882'
end_time: '2026-04-25T22:32:38.128779'
duration_seconds: 1010.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurofibromatosis Type 1
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 51
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurofibromatosis Type 1
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Neurofibromatosis Type 1** covering all of the
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
- **Disease Name:** Neurofibromatosis Type 1
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Neurofibromatosis Type 1** covering all of the
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


# Neurofibromatosis Type 1 (NF1): Disease Characteristics Research Report (2023–2024 emphasis)

## Target Disease
- **Disease name:** Neurofibromatosis type 1 (NF1)
- **MONDO ID:** **MONDO:0018975** (from Open Targets disease record) (lee2023incidenceandprevalence pages 1-2)
- **Category:** Genetic tumor predisposition syndrome / RASopathy (peduto2023neurofibromatosistype1 pages 1-2, park2024recentadvancesin pages 1-2)

## Evidence scope and source types
This report synthesizes **aggregated disease-level resources** (international diagnostic consensus; surveillance guidelines; systematic review/meta-analysis) and **primary clinical trial evidence** (selumetinib phase 2 trial and long-term follow-up), plus mechanistic synthesis from recent reviews. Sources include human clinical cohorts, clinical trials, and preclinical/mouse model insights (especially for NF1 optic pathway glioma). (legius2021reviseddiagnosticcriteria pages 2-3, carton2023erngenturistumour pages 1-2, lee2023incidenceandprevalence pages 2-4, gross2020selumetinibinchildren pages 1-2, tang2023neurofibromatosistype1associated pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
NF1 is a common autosomal dominant, multisystem genetic condition caused by germline pathogenic variants in **NF1**, encoding **neurofibromin**, a negative regulator of Ras signaling (a Ras-GAP). Loss of neurofibromin drives hyperactive Ras pathway output and predisposes to benign peripheral nerve sheath tumors (cutaneous and plexiform neurofibromas) and malignant tumors (e.g., malignant peripheral nerve sheath tumor), as well as neurodevelopmental and skeletal manifestations. (peduto2023neurofibromatosistype1 pages 1-2, park2024recentadvancesin pages 1-2, na2024pastpresentand pages 1-3)

NF1 shows **complete penetrance** with **marked inter- and intrafamilial variable expressivity** and **age-dependent** emergence of manifestations, complicating early diagnosis in children. (peduto2023neurofibromatosistype1 pages 1-2)

### 1.2 Key identifiers and controlled vocabularies
A compact identifier/synonym table is provided below.

| Disease name | Common abbreviation | MONDO ID | OMIM/MIM number(s) reported in available evidence | Inheritance | Common synonyms / alternative names | Key distinguishing related condition | Key references (year; URL) |
|---|---|---|---|---|---|---|---|
| Neurofibromatosis type 1 | NF1 | MONDO:0018975 | OMIM/MIM 162200 reported in 2023 review/meta-analysis; one 2021 consensus excerpt reports “OMIM 613113,” but this appears inconsistent with the standard disease OMIM usage and should be cross-checked before knowledge-base normalization | Autosomal dominant | Neurofibromatosis 1; Neurofibromatosis type I; von Recklinghausen disease / von Recklinghausen neurofibromatosis | Legius syndrome (LGSS), caused by heterozygous pathogenic **SPRED1** variants; may overlap with NF1 pigmentary findings in young children, but LGSS does **not** carry NF1-related tumor risks; molecular testing of **NF1** and **SPRED1** is recommended when presentation is limited to pigmentary findings | Legius et al. 2021, Genetics in Medicine, https://doi.org/10.1038/s41436-021-01170-5; Peduto et al. 2023, Cancers, https://doi.org/10.3390/cancers15041217; Lee et al. 2023, Orphanet Journal of Rare Diseases, https://doi.org/10.1186/s13023-023-02911-2; Park 2024, Journal of Genetic Medicine, https://doi.org/10.5734/jgm.2024.21.2.51 (peduto2023neurofibromatosistype1 pages 1-2, legius2021reviseddiagnosticcriteria pages 1-2, peduto2023neurofibromatosistype1 pages 2-4, lee2023incidenceandprevalence pages 1-2, park2024recentadvancesin pages 1-2) |


*Table: This table summarizes key disease identifiers, inheritance, synonyms, and the most important related differential condition for Neurofibromatosis type 1. It is useful for knowledge-base normalization and for distinguishing NF1 from Legius syndrome in early or pigment-only presentations.*

**Important gap:** ICD-10/ICD-11 codes, MeSH IDs, and Orphanet IDs were **not present in the retrieved evidence corpus** used by the tools in this run; therefore, they are not asserted here. The MONDO ID above is directly supported, and an OMIM/MIM number for the disease (162200) is supported by the 2023 prevalence/incidence meta-analysis. (lee2023incidenceandprevalence pages 1-2)

### 1.3 Synonyms and alternative names
Commonly used names include “neurofibromatosis 1” and “neurofibromatosis type I.” (park2024recentadvancesin pages 1-2, lee2023incidenceandprevalence pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
- **Primary cause:** Germline pathogenic variant in **NF1** (tumor suppressor) (peduto2023neurofibromatosistype1 pages 1-2, park2024recentadvancesin pages 1-2).
- **De novo rate:** Approximately **50%** of cases arise from **de novo** pathogenic variants. (peduto2023neurofibromatosistype1 pages 1-2)

### 2.2 Risk factors
- **Genetic:** Having an affected first-degree relative (autosomal dominant inheritance). (peduto2023neurofibromatosistype1 pages 1-2, legius2021reviseddiagnosticcriteria pages 2-3)
- **Tumor-specific malignant risk factors (NF1 patients):** The ERN GENTURIS guideline highlights groups at higher risk for MPNST, including **NF1 microdeletion affecting SUZ12**, missense variants at **codons 844–848**, prior **ANNUBP**, high internal tumor load/large or multiple plexiform neurofibromas, prior radiotherapy, and family history of MPNST. (carton2023erngenturistumour pages 9-10)
- **Radiation exposure:** For MPNST, prior therapeutic irradiation is a known risk factor and post-radiation MPNST has poor outcomes. (yao2023malignantperipheralnerve pages 2-4)

### 2.3 Protective factors
No specific protective genetic or environmental factors were identified in the retrieved sources.

### 2.4 Gene–environment interactions
The retrieved sources do not provide a clear gene–environment interaction model beyond the general observation that **radiation exposure** can increase risk for MPNST, especially in the context of NF1 tumor predisposition. (yao2023malignantperipheralnerve pages 2-4)

---

## 3. Phenotypes

### 3.1 Core clinical phenotype spectrum and frequencies (examples)
Key frequencies/statistics extracted from recent sources are summarized here and in a table artifact.

| Source | Metric | Value | Notes |
|---|---|---:|---|
| Lee 2023 | Pooled prevalence of NF1 | 3.16 per 10,000 (95% CI 2.12–4.69); ~1 in 3,164 | Meta-analysis of 9 studies, 3,045 cases, pooled population 11,649,059; high heterogeneity (I²=99%) (lee2023incidenceandprevalence pages 2-4, lee2023incidenceandprevalence pages 1-2) |
| Lee 2023 | Pooled birth incidence of NF1 | 3.76 per 10,000 live births (95% CI 2.78–5.08); ~1 in 2,662 | Meta-analysis of 3 studies; 423 cases in 1,170,928 births (lee2023incidenceandprevalence pages 2-4, lee2023incidenceandprevalence pages 1-2) |
| Lee 2023 | Prevalence in screening studies | 4.95 per 10,000 (95% CI 2.47–9.92); ~1 in 2,020 | Higher than record-based estimates, supporting under-recognition in routine data (lee2023incidenceandprevalence pages 2-4, lee2023incidenceandprevalence pages 1-2) |
| Lee 2023 | Prevalence in medical-record studies | 2.31 per 10,000 (95% CI 2.13–2.50); ~1 in 4,329 | Lower ascertainment than screening studies (lee2023incidenceandprevalence pages 2-4, lee2023incidenceandprevalence pages 1-2) |
| Lee 2023 | Sensitivity-analysis estimate (birth incidence + child/adolescent screening) | ~1 in 2,265 (95% CI 1 in 1,497 to 1 in 3,428) | Suggests higher occurrence when age-appropriate screening is considered (lee2023incidenceandprevalence pages 4-7) |
| Carton 2023 | Birth incidence (guideline background) | 1 in 2,000–2,500 | Guideline background estimate; consistent with broader epidemiology (carton2023erngenturistumour pages 1-2) |
| Carton 2023 | Lifetime cancer risk in NF1 | 59.6% | Compared with 30.8% in the general population (carton2023erngenturistumour pages 1-2) |
| Carton 2023 | Lifetime cancer risk in general population | 30.8% | Comparator for NF1-associated cancer burden (carton2023erngenturistumour pages 1-2) |
| Carton 2023 | Plexiform neurofibroma (PN) frequency | ~40–60% | PN associated with risk of malignant transformation (carton2023erngenturistumour pages 10-12) |
| Suppiah 2023 | Plexiform intraneural neurofibroma frequency | ~30–50% | Independent molecular profiling paper; similar range to guideline estimates (suppiah2023multiplatformmolecularprofiling pages 1-2) |
| Carton 2023 | Cutaneous neurofibroma frequency | >95% | Common benign tumor manifestation in NF1 (carton2023erngenturistumour pages 10-12) |
| Carton 2023 | MPNST lifetime risk | 8–16% | Typical presentation between ages 20–40 years (carton2023erngenturistumour pages 10-12) |
| Suppiah 2023 | Lifetime risk of malignant transformation from PN to MPNST | 5–15% | Reported for plexiform intraneural neurofibromas (suppiah2023multiplatformmolecularprofiling pages 1-2) |
| Carton 2023 | OPGs requiring treatment | 15–20% of patients with OPG | Many OPGs are observed; treatment reserved for progressive/symptomatic disease (carton2023erngenturistumour pages 9-10) |
| Carton 2023 | Non-optic pathway glioma frequency | Approximately 4–5% of individuals with NF1 | Refers to non-OPG brain gliomas (carton2023erngenturistumour pages 9-10) |
| Peduto 2023 | Cognitive/behavioral disorders in children with NF1 | Up to 80% | Broad neurodevelopmental burden reported in recent review (park2024recentadvancesin pages 1-2) |
| Peduto 2023 | Café-au-lait macules in infants with NF1 | >95% | Early childhood clinical feature; useful for pediatric recognition (peduto2023neurofibromatosistype1 pages 1-2) |
| Peduto 2023 | Cutaneous neurofibromas in affected adults | About 90% | Age-dependent increase in tumor burden (peduto2023neurofibromatosistype1 pages 1-2) |
| Peduto 2023 | Lisch nodules in children <5 years | <50% | Highlights age-dependent penetrance of diagnostic features (peduto2023neurofibromatosistype1 pages 1-2) |
| Peduto 2023 | Lisch nodules in adults | Almost all adults | Age-dependent diagnostic feature (peduto2023neurofibromatosistype1 pages 1-2) |
| Peduto 2023 | Choroidal abnormalities in children | 60–70% | Common ocular sign in pediatric NF1 (peduto2023neurofibromatosistype1 pages 2-4) |
| Peduto 2023 | Anemic nevus in children | Up to 50% | Supportive but non-diagnostic pediatric feature (peduto2023neurofibromatosistype1 pages 2-4) |


*Table: This table compiles recent quantitative epidemiology and complication frequencies for neurofibromatosis type 1, emphasizing pooled 2023 estimates and clinically relevant tumor risks. It is useful as a compact evidence summary for disease knowledge base fields on prevalence, incidence, and phenotype burden.*

Selected phenotype examples with HPO suggestions (not exhaustive):

1) **Café-au-lait macules (CALMs)**
- Frequency: >95% of infants in one pediatric review (peduto2023neurofibromatosistype1 pages 1-2)
- Typical onset: infancy/early childhood; increase until puberty (peduto2023neurofibromatosistype1 pages 2-4)
- HPO: **Café-au-lait spot (HP:0000957)**

2) **Axillary/inguinal freckling**
- Typical onset: around 6–7 years (peduto2023neurofibromatosistype1 pages 1-2)
- HPO: **Axillary freckling (HP:0000997)**; **Inguinal freckling (HP:0000998)**

3) **Cutaneous neurofibromas**
- Frequency: ~90% of adults in pediatric review; guideline states >95% of people with NF1 have cutaneous neurofibromas (peduto2023neurofibromatosistype1 pages 1-2, carton2023erngenturistumour pages 10-12)
- HPO: **Neurofibroma (HP:0001067)**; **Cutaneous neurofibroma (HP:0012872)**

4) **Plexiform neurofibromas (PN)**
- Frequency: ~40–60% (guideline) (carton2023erngenturistumour pages 10-12)
- Morbidity: disfigurement, pain, neurologic/motor dysfunction; malignant transformation risk (gross2020selumetinibinchildren pages 1-2, carton2023erngenturistumour pages 10-12)
- HPO: **Plexiform neurofibroma (HP:0009732)**

5) **Ophthalmic findings: Lisch nodules and choroidal abnormalities**
- Lisch nodules: almost all adults, <50% under age 5 (peduto2023neurofibromatosistype1 pages 1-2)
- Choroidal abnormalities in children: 60–70% (peduto2023neurofibromatosistype1 pages 2-4)
- HPO: **Lisch nodules (HP:0009737)**

6) **Optic pathway glioma (OPG)**
- Frequency: up to ~20% (“as many as one-fifth”) (tang2023neurofibromatosistype1associated pages 1-2)
- Symptomatic fraction: ~20–30% develop symptoms (progressive vision loss, proptosis, diplopia, precocious puberty) (tang2023neurofibromatosistype1associated pages 1-2)
- HPO: **Optic pathway glioma (HP:0009735)**; **Vision impairment (HP:0000505)**; **Precocious puberty (HP:0000826)**

7) **Neurocognitive/behavioral features**
- One 2024 review states cognitive and behavioral disorders affect up to 80% of children with NF1 (park2024recentadvancesin pages 1-2)
- HPO: **Neurodevelopmental delay (HP:0012758)**; **Learning difficulties (HP:0001328)**; **Attention deficit hyperactivity disorder (HP:0007018)** (where applicable)

### 3.2 Quality of life impact
Adult NF1 has substantial psychosocial burden, especially driven by visibility/disfigurement, stigma, pain, and uncertainty. In a 2023 systematic review of rare genetic skin diseases (including 16 NF1 studies), NF1 was associated with impaired QoL and emotional well-being; severity/visibility predicted QoL burden, and care at NF specialty clinics and genetic counseling were associated with higher self-esteem. (fournier2023psychosocialimplicationsof pages 13-15, fournier2023psychosocialimplicationsof pages 15-16)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
- **NF1 (neurofibromin 1)** is the causal gene for NF1; NF1 encodes neurofibromin, a Ras-GAP regulating Ras/MAPK output. (peduto2023neurofibromatosistype1 pages 1-2, na2024pastpresentand pages 1-3)

### 4.2 Variant spectrum and functional consequences
- Large variant diversity is reported; one 2024 review notes >3,197 constitutional NF1 pathogenic variants, with clinically confirmed genotype–phenotype correlations relevant to ~10–15% of patients, and microdeletions ~4.7–11%. (park2024recentadvancesin pages 1-2)
- A pediatric genotype–phenotype review reports that 90–95% of causative variants are intragenic and <10% are whole-gene deletions including flanking regions. (peduto2023neurofibromatosistype1 pages 11-13)
- Functional consequence is primarily **loss of function** in a tumor suppressor, with many NF1 tumors following a “second hit” model (somatic inactivation of the remaining allele). (na2024pastpresentand pages 1-3)

### 4.3 Modifier genes / related loci
The retrieved evidence emphasizes **SPRED1** as a key differential diagnosis (Legius syndrome). Molecular testing for **NF1 and SPRED1** is recommended when a child has only pigmentary findings, because Legius syndrome lacks NF1-associated oncologic risks. (peduto2023neurofibromatosistype1 pages 2-4)

### 4.4 Epigenetic information
In NF1-associated malignant transformation (MPNST), epigenetic regulators are important: PRC2 components (**EED/SUZ12**) may be inactivated, and **loss of H3K27me3** is described as a marker more common in sporadic/radiation-induced MPNST (and mechanistically linked to PRC2 loss). (yao2023malignantperipheralnerve pages 13-14, yao2023malignantperipheralnerve pages 2-4)

---

## 5. Environmental Information

NF1 is primarily genetic. In the retrieved evidence, the main non-genetic contributor to malignant risk is **radiation exposure** (a risk factor for MPNST), and post-radiation MPNST shows particularly poor survival statistics in one review. (yao2023malignantperipheralnerve pages 2-4)

---

## 6. Mechanism / Pathophysiology

### 6.1 Core causal chain (from mutation to phenotype)
1. **Germline NF1 pathogenic variant → reduced/absent neurofibromin**.
2. Neurofibromin is a Ras-GAP that limits Ras signaling; one recent therapeutic-strategy review states neurofibromin “**is a Ras GTPase-activating protein (RAS-GAP) that converts active GTP-bound Ras into inactive GDP-bound Ras**,” and “**Thus, NF1 loss leads to constitutive Ras activation**.” (na2024pastpresentand pages 1-3)
3. Downstream Ras pathway hyperactivation increases output through **RAF–MEK–ERK (MAPK)** and other axes including **PI3K–AKT–mTOR**, with tumorigenesis typically requiring a **second somatic hit** in the remaining allele. (na2024pastpresentand pages 1-3)
4. Tumor microenvironment cells (e.g., fibroblasts/endothelial cells; immune components) can support tumor growth and are emerging therapeutic targets. (na2024pastpresentand pages 1-3)

Complementary mechanistic detail from a 2023 neurofibromin signaling review emphasizes broad pathway reach beyond MAPK, including **cAMP/PKA**, cytoskeletal signaling, and post-translational regulation of neurofibromin abundance. (baezflores2023thetherapeuticpotential pages 1-2, baezflores2023thetherapeuticpotential pages 3-4, baezflores2023thetherapeuticpotential pages 5-6)

### 6.2 Key pathways and suggested ontology terms
**Pathways (examples):**
- Ras/MAPK cascade; RAF–MEK–ERK signaling (na2024pastpresentand pages 1-3, park2024recentadvancesin pages 1-2)
- PI3K/AKT/mTOR signaling (na2024pastpresentand pages 1-3, park2024recentadvancesin pages 1-2, baezflores2023thetherapeuticpotential pages 5-6)
- cAMP/PKA signaling and neurodevelopmental phenotypes (baezflores2023thetherapeuticpotential pages 3-4, baezflores2023thetherapeuticpotential pages 5-6)
- Rho/ROCK/LIMK/cofilin; cytoskeletal remodeling (park2024recentadvancesin pages 1-2, baezflores2023thetherapeuticpotential pages 5-6)

**GO Biological Process suggestions (examples):**
- **Ras protein signal transduction (GO:0007265)**
- **MAPK cascade (GO:0000165)**
- **Regulation of cell proliferation (GO:0042127)**
- **Regulation of apoptotic process (GO:0042981)**
- **cAMP-mediated signaling (GO:0019933)**

### 6.3 Cell types and suggested CL terms (examples)
Mechanistic and tumor discussions implicate:
- Schwann cell lineage as tumor cell of origin for neurofibromas/MPNST (review emphasis) (na2024pastpresentand pages 5-6)
- Optic glioma models implicate progenitor/oligodendrocyte-lineage tumor cells plus microglia and T cells in a supportive immune niche (tang2023neurofibromatosistype1associated pages 6-8)

**CL term suggestions (examples):**
- **Schwann cell (CL:0000218)**
- **Microglial cell (CL:0000129)**
- **T cell (CL:0000084)**
- **Oligodendrocyte precursor cell (CL:0002453)** (for OPG model context)

---

## 7. Anatomical Structures Affected

NF1 is multisystem; major affected anatomical systems include:
- **Skin/peripheral nerves:** café-au-lait macules, freckling, cutaneous and plexiform neurofibromas (peduto2023neurofibromatosistype1 pages 1-2, carton2023erngenturistumour pages 10-12)
- **Central nervous system/visual system:** optic pathway gliomas; non-optic low-grade gliomas (tang2023neurofibromatosistype1associated pages 1-2, carton2023erngenturistumour pages 9-10)
- **Skeletal system:** distinctive osseous lesions used diagnostically (e.g., tibial bowing/pseudarthrosis; sphenoid dysplasia) (peduto2023neurofibromatosistype1 pages 2-4)
- **Breast tissue:** elevated breast cancer risk prompting early MRI screening in guidelines (carton2023erngenturistumour pages 10-12, carton2023erngenturistumour pages 6-7)

**UBERON suggestions (examples):**
- **Skin (UBERON:0002097)**
- **Peripheral nerve (UBERON:0001021)**
- **Optic nerve (UBERON:0000966)**
- **Brain (UBERON:0000955)**
- **Tibia (UBERON:0001465)**
- **Breast (UBERON:0000310)**

---

## 8. Temporal Development (natural history)

- **Onset:** congenital/genetic; many visible pigmentary findings arise in infancy; other diagnostic features are age-dependent (peduto2023neurofibromatosistype1 pages 2-4, peduto2023neurofibromatosistype1 pages 1-2)
- **Progression:** variable; tumor-related complications may occur from childhood (e.g., OPG) through adulthood (e.g., MPNST) (carton2023erngenturistumour pages 5-6)

Examples of age-dependence:
- Freckling tends to appear around age 6–7 (peduto2023neurofibromatosistype1 pages 1-2)
- OPG is usually detected in early childhood, often before age 7 (tang2023neurofibromatosistype1associated pages 1-2)
- MPNST typically presents between ages 20–40 (guideline) (carton2023erngenturistumour pages 10-12)

---

## 9. Inheritance and Population

### 9.1 Inheritance
- **Autosomal dominant** inheritance is consistently reported. (peduto2023neurofibromatosistype1 pages 1-2, lee2023incidenceandprevalence pages 1-2)
- **Penetrance:** described as complete in pediatric review, with wide expressivity. (peduto2023neurofibromatosistype1 pages 1-2)

### 9.2 Epidemiology (recent quantitative data)
A 2023 systematic review/meta-analysis estimated:
- **Pooled prevalence:** ~**1 in 3,164** (95% CI 1 in 2,132–1 in 4,712). (lee2023incidenceandprevalence pages 1-2)
- **Pooled birth incidence:** ~**1 in 2,662** (95% CI 1 in 1,968–1 in 3,601). (lee2023incidenceandprevalence pages 1-2)
- **Under-recognition:** prevalence was higher in **screening studies** (~1 in 2,020) than in medical-record ascertainment (~1 in 4,329), suggesting under-recognition in routine data. (lee2023incidenceandprevalence pages 2-4, lee2023incidenceandprevalence pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical diagnostic criteria (2021 revised international consensus)
The 2021 international consensus provides revised NF1 criteria incorporating genetic testing and new ophthalmic imaging features; core requirements are summarized below.

| Diagnostic context | Requirement / criterion | Threshold or specification | Notes / differentiation | Citation |
|---|---|---|---|---|
| NF1 diagnosis, individual **without** an affected parent | **Two or more** diagnostic criteria required | Any 2 of the listed NF1 criteria below | 2021 international consensus revision | (legius2021reviseddiagnosticcriteria pages 2-3, legius2021reviseddiagnosticcriteria media 67536eac) |
| NF1 diagnosis, child of an **affected parent** | **One or more** diagnostic criteria required | Any 1 listed NF1 criterion | Applies when a parent meets NF1 diagnostic criteria | (legius2021reviseddiagnosticcriteria pages 2-3, peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria media 67536eac) |
| Café-au-lait macules (CALMs) | Pigmentary criterion | **≥6** CALMs; diameter **>5 mm** in prepubertal individuals and **>15 mm** in postpubertal individuals | Bilateral distribution is typical; isolated pigmentary findings in young children can overlap with Legius syndrome | (legius2021reviseddiagnosticcriteria pages 2-3, peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria media 67536eac) |
| Axillary or inguinal freckling | Pigmentary criterion | Present in axillary and/or inguinal region | Can also occur in Legius syndrome; not sufficient alone to distinguish NF1 | (legius2021reviseddiagnosticcriteria pages 2-3, peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria media 67536eac) |
| Neurofibromas / plexiform neurofibroma | Tumor criterion | **≥2 neurofibromas** of any type **or** **1 plexiform neurofibroma** | Plexiform neurofibroma is highly supportive of NF1 and not a feature of Legius syndrome | (legius2021reviseddiagnosticcriteria pages 2-3, peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria media 67536eac) |
| Optic pathway glioma | Tumor criterion | Presence of **optic pathway glioma** | Included as a standalone diagnostic feature | (legius2021reviseddiagnosticcriteria pages 2-3, peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria media 67536eac) |
| Iris Lisch nodules / choroidal abnormalities | Ophthalmic criterion | **≥2 iris Lisch nodules** identified by slit lamp **or** **≥2 choroidal abnormalities** detected by OCT/NIR imaging | Choroidal abnormalities were added in the revised criteria | (legius2021reviseddiagnosticcriteria pages 2-3, peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria media 67536eac) |
| Distinctive osseous lesion | Skeletal criterion | **Sphenoid dysplasia**, **anterolateral bowing of the tibia**, or **pseudarthrosis of a long bone** | Revised wording emphasizes distinctive NF1-associated osseous lesions | (legius2021reviseddiagnosticcriteria pages 2-3, peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria media 67536eac) |
| Molecular criterion | Genetic criterion | **Heterozygous pathogenic NF1 variant** with approximately **50% variant allele fraction** in apparently normal tissue (e.g., blood) | Allows diagnosis using molecular testing; especially useful in young children or atypical presentations | (legius2021reviseddiagnosticcriteria pages 2-3, peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria media 67536eac) |
| Mosaic NF1 | Special consideration | Separate recommendations proposed | Mosaic forms were specifically addressed by the consensus, but are not captured by the standard simplified rows above | (legius2021reviseddiagnosticcriteria pages 1-2, legius2021reviseddiagnosticcriteria media 67536eac) |
| Legius syndrome differentiation | Distinguishing related condition | **≥6 bilateral CALMs** and no other NF1 diagnostic criteria except possible freckling, **or** heterozygous pathogenic **SPRED1** variant (~50% VAF) | Legius syndrome can mimic early pigmentary NF1 but **does not carry NF1-related oncologic risks** | (legius2021reviseddiagnosticcriteria pages 2-3, peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria media 67536eac) |


*Table: This table summarizes the 2021 international consensus diagnostic criteria for neurofibromatosis type 1, including the different threshold for individuals with and without an affected parent. It also briefly distinguishes Legius syndrome, an important overlapping condition in children with pigmentary findings.*

**Visual primary-source evidence:** Table images of the revised diagnostic criteria were retrieved from the consensus publication (legius2021reviseddiagnosticcriteria media 67536eac, legius2021reviseddiagnosticcriteria media 57806d8a).

### 10.2 Genetic testing approach
The revised criteria explicitly allow diagnosis via identification of a **heterozygous pathogenic NF1 variant (~50% variant allele fraction in normal tissue)** as one diagnostic feature, supporting molecular diagnosis especially in young children or atypical cases. (peduto2023neurofibromatosistype1 pages 2-4, legius2021reviseddiagnosticcriteria pages 2-3)

### 10.3 Imaging / biomarkers
- **Plexiform neurofibroma trials** use **volumetric MRI** and REiNS criteria to define response (≥20% volume reduction). (gross2023longtermsafetyand pages 1-2, gross2020selumetinibinchildren pages 1-2)
- For **OPG monitoring**, OCT measures (RNFL/GCL) and VEP are discussed; VEP is reported to have ~90% sensitivity for detecting presence of an OPG (with specificity limitations), and OCT thinning can precede measurable vision loss. (tang2023neurofibromatosistype1associated pages 4-6)

### 10.4 Differential diagnosis
A critical differential in pigment-only presentations is **Legius syndrome (SPRED1)**, which overlaps with café-au-lait macules ± freckling but lacks NF1 tumor risks; molecular analysis of NF1 and SPRED1 is recommended in such cases. (peduto2023neurofibromatosistype1 pages 2-4)

---

## 11. Outcome / Prognosis

### 11.1 Cancer burden
ERN GENTURIS reports markedly increased cancer burden: lifetime cancer risk **59.6%** in NF1 vs **30.8%** in the general population. (carton2023erngenturistumour pages 1-2)

### 11.2 MPNST prognosis
A 2023 MPNST clinical management review reports overall poor outcomes with a **5-year overall survival ~50–60%** and median survival about **6 years**, noting NF1-associated cases have worse survival than sporadic tumors. (yao2023malignantperipheralnerve pages 11-13)

### 11.3 Quality of life / psychosocial outcomes
A 2023 systematic review synthesizing adult NF1 studies (n≈1,180 across 16 studies) highlights stigma, anxiety/depression, and functional limitations. It reports that severity and visibility predict poorer QoL, and that self-esteem was higher in those receiving care at NF clinics or genetic counseling. (fournier2023psychosocialimplicationsof pages 13-15, fournier2023psychosocialimplicationsof pages 15-16)

---

## 12. Treatment

### 12.1 Pharmacotherapy and targeted therapy (plexiform neurofibromas)
The treatment landscape for symptomatic, inoperable NF1 plexiform neurofibromas has been transformed by MEK inhibition.

| Publication / milestone | Year | Population | Design / setting | Response / efficacy | Clinical outcomes / implementation notes | Key adverse events / monitoring | URL | Citation |
|---|---:|---|---|---|---|---|---|---|
| Gross et al., *NEJM* | 2020 | 50 children with NF1 and symptomatic, inoperable plexiform neurofibromas; median age 10.2 years | Open-label phase 2 trial; selumetinib 25 mg/m² twice daily continuously in 28-day cycles; volumetric MRI and patient-reported/functional outcomes assessed serially | Confirmed partial response in 35/50 (70%); 28/35 responses durable for ≥1 year | Mean child-reported tumor pain intensity decreased by 2 points after 1 year; clinically meaningful improvements in pain interference (child 38%, parent 50%), overall HRQoL (child 48%, parent 58%), strength (56%), and range of motion (38%); established selumetinib as first highly active systemic therapy for pediatric NF1-PN | Most frequent toxicities: nausea/vomiting/diarrhea, asymptomatic creatine phosphokinase increase, acneiform rash, paronychia; 5 discontinued for toxicity; 6 had progression | https://doi.org/10.1056/NEJMoa1912735 | (gross2020selumetinibinchildren pages 1-2) |
| Gross et al., *Neuro-Oncology* long-term follow-up | 2023 | 74 children (phase 1/2 cohort), median age 10.3 years, NF1 with inoperable symptomatic PN | Long-term phase 1/2 follow-up of SPRINT (NCT01362803); continuous selumetinib; safety/efficacy through ~5 additional years | Overall confirmed partial response 52/74 (70%); median treatment duration 57.5 cycles; 59% of responses lasted ≥12 cycles | Durable improvement in tumor pain intensity (P=.015) and pain interference (P=.0059) through 48 cycles; supports long-term use in practice with sustained benefit and need for extended follow-up | No new safety signals, but known AEs may first appear after several years; ongoing labs, echocardiograms, and ophthalmologic monitoring recommended | https://doi.org/10.1093/neuonc/noad086 | (gross2023longtermsafetyand pages 1-2) |
| Casey et al., FDA approval summary, *Clin Cancer Res* | 2021 | Pediatric patients ≥2 years with symptomatic, inoperable NF1-associated PN | Regulatory review of single-arm multicenter trial data supporting approval | Overall response rate 66% (95% CI 51–79); median duration of response not reached; 82% of responders had response duration ≥12 months | FDA approved selumetinib (Koselugo) on April 10, 2020 for pediatric NF1 patients ≥2 years with symptomatic, inoperable PN; supported by radiographic response plus clinical outcome assessments | Class MEK inhibitor toxicities emphasized: ocular, cardiac, musculoskeletal, gastrointestinal, dermatologic | https://doi.org/10.1158/1078-0432.CCR-20-5032 | (casey2021fdaapprovalsummary pages 1-1) |
| Armstrong et al., *BMC Cancer* review | 2023 | Children with NF1-related PN (clinical practice focus) | Narrative clinical decision review on surgery, watchful waiting, and MEK inhibitor use | Summarizes selumetinib activity as ~70% tumor volume reduction response in pivotal pediatric trial | Selumetinib described as the only licensed medical therapy for pediatric symptomatic, inoperable NF1-PN at the time; treatment should be individualized by multidisciplinary teams based on tumor size/location, adjacent tissue effects, symptoms, and family preferences | Review highlights need to balance benefits with MEK inhibitor toxicities and long treatment duration | https://doi.org/10.1186/s12885-023-10996-y | (gross2020selumetinibinchildren pages 1-2) |
| Azizi et al., *Neuro-Oncology Practice* AE consensus | 2024 | Pediatric NF1 patients with PN receiving selumetinib | Modified Delphi expert consensus for prevention/management of selumetinib-associated adverse events in real-world care | Not an efficacy trial; implementation-focused guidance based on accumulated trial and expanded-access experience | Consensus agreement reached for 36 statements; supports practical toxicity management to keep patients on effective therapy when possible | Reported AE frequencies include vomiting 86%, diarrhea 81%, dry skin 65%, elevated CPK 77%, decreased LVEF 28%, increased blood pressure 18%, blurred vision 15%; rare ocular events include central serous retinopathy 0.6% and retinal vein occlusion 0.3% | https://doi.org/10.1093/nop/npae038 | (azizi2024consensusrecommendationson pages 1-2) |


*Table: This table summarizes the pivotal selumetinib evidence base for NF1-associated plexiform neurofibromas, including the landmark pediatric trials, FDA approval, and 2024 adverse-event management guidance. It is useful for quickly linking efficacy, real-world implementation, and safety monitoring considerations.*

Key primary-trial efficacy highlights:
- In the pivotal pediatric phase 2 trial, confirmed partial response occurred in **70% (35/50)** with many durable responses; pain and QoL improved meaningfully. (gross2020selumetinibinchildren pages 1-2)
- Long-term follow-up (up to ~5 additional years) maintained **70%** confirmed partial response in a larger cohort (52/74) with durable pain improvements and no new safety signals, but ongoing monitoring is required because known adverse events may appear later. (gross2023longtermsafetyand pages 1-2)

### 12.2 Treatment adverse events and real-world implementation guidance (2024)
A 2024 European expert panel (modified Delphi) produced consensus recommendations for prevention and management of selumetinib-associated adverse events and reported clinically relevant AE frequencies (e.g., vomiting 86%, diarrhea 81%, elevated CPK 77%, decreased LVEF 28%). (azizi2024consensusrecommendationson pages 1-2)

### 12.3 Surgical and interventional care
Surgery remains important for selected tumors/lesions (e.g., resectable ANNUBP, certain symptomatic gliomas), but is often limited by tumor location and morbidity. For MPNST, ERN GENTURIS states there is no place for watchful waiting and recommends urgent resection when feasible. (carton2023erngenturistumour pages 9-10, carton2023erngenturistumour pages 10-12)

### 12.4 Ongoing and recent clinical trials (real-world pipeline)
Examples of MEK inhibitor trials and post-authorization studies:
- **NCT01362803:** Selumetinib (AZD6244) Phase I/II in children with NF1 PN; ACTIVE_NOT_RECRUITING. (NCT01362803 chunk 1)
- **NCT03962543 (ReNeu):** Mirdametinib Phase 2b single-group in adults and children with inoperable symptomatic NF1 PN; ACTIVE_NOT_RECRUITING; primary completion 2023-09-20. (NCT03962543 chunk 1)
- **NCT05388370:** Selumetinib post-authorisation safety study (PASS) prospective cohort; ACTIVE_NOT_RECRUITING; follow-up to 2028; monitoring includes LVEF reduction, physeal dysplasia, ocular toxicity, pubertal development. (NCT05388370 chunk 1)
- **NCT03231306:** Binimetinib Phase II in children and adults with NF1 PN; COMPLETED with completion date 2024-04-17. (NCT03231306 chunk 1)

**MAXO suggestions (examples):**
- **MEK inhibitor therapy** (MAXO term suggestion; no MAXO ID provided in retrieved evidence)
- **MRI surveillance** (MAXO suggestion)
- **Genetic counseling** (MAXO suggestion; supported as beneficial for self-esteem in adult NF1 systematic review) (fournier2023psychosocialimplicationsof pages 13-15)

---

## 13. Prevention

Primary prevention is not currently available for a germline genetic disorder, but **secondary/tertiary prevention** via surveillance is central.

ERN GENTURIS (2023) provides age-stratified surveillance recommendations, including:
- Regular clinical assessments (at least annually in young children),
- Ophthalmologic surveillance for OPG with OCT when feasible,
- Imaging strategies for internal tumor burden at transition to adulthood (e.g., WB-MRI at least once),
- Breast cancer screening: annual MRI starting as soon after age 30 as feasible until 50. (carton2023erngenturistumour pages 6-7, carton2023erngenturistumour pages 7-8)

---

## 14. Other Species / Natural Disease

The retrieved sources did not include naturally occurring NF1 disease descriptions in non-human species.

---

## 15. Model Organisms

NF1 optic pathway glioma research frequently uses genetically engineered mouse models. These models provide mechanistic insight into gliomagenesis, retinal ganglion cell injury, and the role of immune/microenvironmental cells (microglia and T cells) and neuronal activity factors in tumor initiation and progression. (tang2023neurofibromatosistype1associated pages 1-2, tang2023neurofibromatosistype1associated pages 6-8)

---

## Recent developments and expert analysis (2023–2024 highlights)
- **Epidemiology refresh (2023):** Updated pooled prevalence/incidence with evidence of under-recognition in routine medical records vs screening. (lee2023incidenceandprevalence pages 2-4, lee2023incidenceandprevalence pages 1-2)
- **Practice-changing implementation support (2024):** Consensus adverse-event management for selumetinib in pediatric NF1 PN to facilitate safer long-term use outside trials. (azizi2024consensusrecommendationson pages 1-2)
- **Therapeutic strategy evolution (2024):** Expert synthesis emphasizes that while MEK inhibition has succeeded for PNs and some low-grade gliomas, monotherapy is insufficient for aggressive tumors (e.g., MPNST), motivating combination and microenvironment-targeting approaches. (na2024pastpresentand pages 1-3)

---

## Notes on PMID availability
Within the retrieved full-text excerpts, PMIDs were not consistently provided, so PMID-level indexing could not be verified for every citation in this tool run. All major claims are instead linked to specific retrieved documents via the provided context IDs and include DOIs/URLs and publication months/years as available.


References

1. (lee2023incidenceandprevalence pages 1-2): Tin-Suet Joan Lee, Meera Chopra, Raymond H. Kim, Patricia C. Parkin, and Carolina Barnett-Tapia. Incidence and prevalence of neurofibromatosis type 1 and 2: a systematic review and meta-analysis. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02911-2, doi:10.1186/s13023-023-02911-2. This article has 154 citations and is from a peer-reviewed journal.

2. (peduto2023neurofibromatosistype1 pages 1-2): Cristina Peduto, Mariateresa Zanobio, Vincenzo Nigro, Silverio Perrotta, Giulio Piluso, and Claudia Santoro. Neurofibromatosis type 1: pediatric aspects and review of genotype–phenotype correlations. Cancers, 15:1217, Feb 2023. URL: https://doi.org/10.3390/cancers15041217, doi:10.3390/cancers15041217. This article has 80 citations.

3. (park2024recentadvancesin pages 1-2): Su Jung Park. Recent advances in neurofibromatosis type 1 research: towards tailored therapeutics and treatment strategies. Journal of Genetic Medicine, 21:51-60, Dec 2024. URL: https://doi.org/10.5734/jgm.2024.21.2.51, doi:10.5734/jgm.2024.21.2.51. This article has 2 citations.

4. (legius2021reviseddiagnosticcriteria pages 2-3): Eric Legius, Ludwine Messiaen, Pierre Wolkenstein, Patrice Pancza, Robert A. Avery, Yemima Berman, Jaishri Blakeley, Dusica Babovic-Vuksanovic, Karin Soares Cunha, Rosalie Ferner, Michael J. Fisher, Jan M. Friedman, David H. Gutmann, Hildegard Kehrer-Sawatzki, Bruce R. Korf, Victor-Felix Mautner, Sirkku Peltonen, Katherine A. Rauen, Vincent Riccardi, Elizabeth Schorry, Anat Stemmer-Rachamimov, David A. Stevenson, Gianluca Tadini, Nicole J. Ullrich, David Viskochil, Katharina Wimmer, Kaleb Yohay, Alicia Gomes, Justin T. Jordan, Victor Mautner, Vanessa L. Merker, Miriam J. Smith, David Stevenson, Monique Anten, Arthur Aylsworth, Diana Baralle, Sebastien Barbarot, Fred Barker, Shay Ben-Shachar, Amanda Bergner, Didier Bessis, Ignacio Blanco, Catherine Cassiman, Patricia Ciavarelli, Maurizio Clementi, Thierry Frébourg, Marco Giovannini, Dorothy Halliday, Chris Hammond, C.O. Hanemann, Helen Hanson, Arvid Heiberg, Pascal Joly, Michel Kalamarides, Matthias Karajannis, Daniela Kroshinsky, Margarita Larralde, Conxi Lázaro, Lu Le, Michael Link, Robert Listernick, Mia MacCollin, Conor Mallucci, Christopher Moertel, Amy Mueller, Joanne Ngeow, Rianne Oostenbrink, Roger Packer, Laura Papi, Allyson Parry, Juha Peltonen, Dominique Pichard, Bruce Poppe, Nilton Rezende, Luiz Oswaldo Rodrigues, Tena Rosser, Martino Ruggieri, Eduard Serra, Verena Steinke-Lange, Stavros Michael Stivaros, Amy Taylor, Jaan Toelen, James Tonsgard, Eva Trevisson, Meena Upadhyaya, Ali Varan, Meredith Wilson, Hao Wu, Gelareh Zadeh, Susan M. Huson, D. Gareth Evans, and Scott R. Plotkin. Revised diagnostic criteria for neurofibromatosis type 1 and legius syndrome: an international consensus recommendation. Genetics in Medicine, 23:1506-1513, Aug 2021. URL: https://doi.org/10.1038/s41436-021-01170-5, doi:10.1038/s41436-021-01170-5. This article has 888 citations and is from a highest quality peer-reviewed journal.

5. (carton2023erngenturistumour pages 1-2): Charlotte Carton, D. Gareth Evans, Ignacio Blanco, Reinhard E. Friedrich, Rosalie E. Ferner, Said Farschtschi, Hector Salvador, Amedeo A. Azizi, Victor Mautner, Claas Röhl, Sirkku Peltonen, Stavros Stivaros, Eric Legius, Rianne Oostenbrink, Joan Brunet, Frank Van Calenbergh, Catherine Cassiman, Thomas Czech, María José Gavarrete de León, Henk Giele, Susie Henley, Conxi Lazaro, Vera Lipkovskaya, Eamonn R. Maher, Vanessa Martin, Irene Mathijssen, Enrico Opocher, Ana Elisabete Pires, Thomas Pletschko, Eirene Poupaki, Vita Ridola, Andre Rietman, Thorsten Rosenbaum, Alastair Santhouse, Astrid Sehested, Ian Simmons, Walter Taal, and Anja Wagner. Ern genturis tumour surveillance guidelines for individuals with neurofibromatosis type 1. eClinicalMedicine, 56:101818, Feb 2023. URL: https://doi.org/10.1016/j.eclinm.2022.101818, doi:10.1016/j.eclinm.2022.101818. This article has 129 citations and is from a peer-reviewed journal.

6. (lee2023incidenceandprevalence pages 2-4): Tin-Suet Joan Lee, Meera Chopra, Raymond H. Kim, Patricia C. Parkin, and Carolina Barnett-Tapia. Incidence and prevalence of neurofibromatosis type 1 and 2: a systematic review and meta-analysis. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02911-2, doi:10.1186/s13023-023-02911-2. This article has 154 citations and is from a peer-reviewed journal.

7. (gross2020selumetinibinchildren pages 1-2): Andrea M. Gross, Pamela L. Wolters, Eva Dombi, Andrea Baldwin, Patricia Whitcomb, Michael J. Fisher, Brian Weiss, AeRang Kim, Miriam Bornhorst, Amish C. Shah, Staci Martin, Marie C. Roderick, Dominique C. Pichard, Amanda Carbonell, Scott M. Paul, Janet Therrien, Oxana Kapustina, Kara Heisey, D. Wade Clapp, Chi Zhang, Cody J. Peer, William D. Figg, Malcolm Smith, John Glod, Jaishri O. Blakeley, Seth M. Steinberg, David J. Venzon, L. Austin Doyle, and Brigitte C. Widemann. Selumetinib in children with inoperable plexiform neurofibromas. New England Journal of Medicine, 382:1430-1442, Apr 2020. URL: https://doi.org/10.1056/nejmoa1912735, doi:10.1056/nejmoa1912735. This article has 822 citations and is from a highest quality peer-reviewed journal.

8. (tang2023neurofibromatosistype1associated pages 1-2): Yunshuo Tang and David H Gutmann. Neurofibromatosis type 1-associated optic pathway gliomas: current challenges and future prospects. Cancer Management and Research, 15:667-681, Jul 2023. URL: https://doi.org/10.2147/cmar.s362678, doi:10.2147/cmar.s362678. This article has 36 citations and is from a peer-reviewed journal.

9. (na2024pastpresentand pages 1-3): Brian Na, Shilp R. Shah, and Harish N. Vasudevan. Past, present, and future therapeutic strategies for nf-1-associated tumors. Current Oncology Reports, 26:706-713, May 2024. URL: https://doi.org/10.1007/s11912-024-01527-4, doi:10.1007/s11912-024-01527-4. This article has 20 citations and is from a peer-reviewed journal.

10. (legius2021reviseddiagnosticcriteria pages 1-2): Eric Legius, Ludwine Messiaen, Pierre Wolkenstein, Patrice Pancza, Robert A. Avery, Yemima Berman, Jaishri Blakeley, Dusica Babovic-Vuksanovic, Karin Soares Cunha, Rosalie Ferner, Michael J. Fisher, Jan M. Friedman, David H. Gutmann, Hildegard Kehrer-Sawatzki, Bruce R. Korf, Victor-Felix Mautner, Sirkku Peltonen, Katherine A. Rauen, Vincent Riccardi, Elizabeth Schorry, Anat Stemmer-Rachamimov, David A. Stevenson, Gianluca Tadini, Nicole J. Ullrich, David Viskochil, Katharina Wimmer, Kaleb Yohay, Alicia Gomes, Justin T. Jordan, Victor Mautner, Vanessa L. Merker, Miriam J. Smith, David Stevenson, Monique Anten, Arthur Aylsworth, Diana Baralle, Sebastien Barbarot, Fred Barker, Shay Ben-Shachar, Amanda Bergner, Didier Bessis, Ignacio Blanco, Catherine Cassiman, Patricia Ciavarelli, Maurizio Clementi, Thierry Frébourg, Marco Giovannini, Dorothy Halliday, Chris Hammond, C.O. Hanemann, Helen Hanson, Arvid Heiberg, Pascal Joly, Michel Kalamarides, Matthias Karajannis, Daniela Kroshinsky, Margarita Larralde, Conxi Lázaro, Lu Le, Michael Link, Robert Listernick, Mia MacCollin, Conor Mallucci, Christopher Moertel, Amy Mueller, Joanne Ngeow, Rianne Oostenbrink, Roger Packer, Laura Papi, Allyson Parry, Juha Peltonen, Dominique Pichard, Bruce Poppe, Nilton Rezende, Luiz Oswaldo Rodrigues, Tena Rosser, Martino Ruggieri, Eduard Serra, Verena Steinke-Lange, Stavros Michael Stivaros, Amy Taylor, Jaan Toelen, James Tonsgard, Eva Trevisson, Meena Upadhyaya, Ali Varan, Meredith Wilson, Hao Wu, Gelareh Zadeh, Susan M. Huson, D. Gareth Evans, and Scott R. Plotkin. Revised diagnostic criteria for neurofibromatosis type 1 and legius syndrome: an international consensus recommendation. Genetics in Medicine, 23:1506-1513, Aug 2021. URL: https://doi.org/10.1038/s41436-021-01170-5, doi:10.1038/s41436-021-01170-5. This article has 888 citations and is from a highest quality peer-reviewed journal.

11. (peduto2023neurofibromatosistype1 pages 2-4): Cristina Peduto, Mariateresa Zanobio, Vincenzo Nigro, Silverio Perrotta, Giulio Piluso, and Claudia Santoro. Neurofibromatosis type 1: pediatric aspects and review of genotype–phenotype correlations. Cancers, 15:1217, Feb 2023. URL: https://doi.org/10.3390/cancers15041217, doi:10.3390/cancers15041217. This article has 80 citations.

12. (carton2023erngenturistumour pages 9-10): Charlotte Carton, D. Gareth Evans, Ignacio Blanco, Reinhard E. Friedrich, Rosalie E. Ferner, Said Farschtschi, Hector Salvador, Amedeo A. Azizi, Victor Mautner, Claas Röhl, Sirkku Peltonen, Stavros Stivaros, Eric Legius, Rianne Oostenbrink, Joan Brunet, Frank Van Calenbergh, Catherine Cassiman, Thomas Czech, María José Gavarrete de León, Henk Giele, Susie Henley, Conxi Lazaro, Vera Lipkovskaya, Eamonn R. Maher, Vanessa Martin, Irene Mathijssen, Enrico Opocher, Ana Elisabete Pires, Thomas Pletschko, Eirene Poupaki, Vita Ridola, Andre Rietman, Thorsten Rosenbaum, Alastair Santhouse, Astrid Sehested, Ian Simmons, Walter Taal, and Anja Wagner. Ern genturis tumour surveillance guidelines for individuals with neurofibromatosis type 1. eClinicalMedicine, 56:101818, Feb 2023. URL: https://doi.org/10.1016/j.eclinm.2022.101818, doi:10.1016/j.eclinm.2022.101818. This article has 129 citations and is from a peer-reviewed journal.

13. (yao2023malignantperipheralnerve pages 2-4): Chengjun Yao, Haiying Zhou, Yanzhao Dong, Ahmad Alhaskawi, Sohaib Hasan Abdullah Ezzi, Zewei Wang, Jingtian Lai, Vishnu Goutham Kota, Mohamed Hasan Abdulla Hasan Abdulla, and Hui Lu. Malignant peripheral nerve sheath tumors: latest concepts in disease pathogenesis and clinical management. Cancers, 15:1077, Feb 2023. URL: https://doi.org/10.3390/cancers15041077, doi:10.3390/cancers15041077. This article has 118 citations.

14. (lee2023incidenceandprevalence pages 4-7): Tin-Suet Joan Lee, Meera Chopra, Raymond H. Kim, Patricia C. Parkin, and Carolina Barnett-Tapia. Incidence and prevalence of neurofibromatosis type 1 and 2: a systematic review and meta-analysis. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02911-2, doi:10.1186/s13023-023-02911-2. This article has 154 citations and is from a peer-reviewed journal.

15. (carton2023erngenturistumour pages 10-12): Charlotte Carton, D. Gareth Evans, Ignacio Blanco, Reinhard E. Friedrich, Rosalie E. Ferner, Said Farschtschi, Hector Salvador, Amedeo A. Azizi, Victor Mautner, Claas Röhl, Sirkku Peltonen, Stavros Stivaros, Eric Legius, Rianne Oostenbrink, Joan Brunet, Frank Van Calenbergh, Catherine Cassiman, Thomas Czech, María José Gavarrete de León, Henk Giele, Susie Henley, Conxi Lazaro, Vera Lipkovskaya, Eamonn R. Maher, Vanessa Martin, Irene Mathijssen, Enrico Opocher, Ana Elisabete Pires, Thomas Pletschko, Eirene Poupaki, Vita Ridola, Andre Rietman, Thorsten Rosenbaum, Alastair Santhouse, Astrid Sehested, Ian Simmons, Walter Taal, and Anja Wagner. Ern genturis tumour surveillance guidelines for individuals with neurofibromatosis type 1. eClinicalMedicine, 56:101818, Feb 2023. URL: https://doi.org/10.1016/j.eclinm.2022.101818, doi:10.1016/j.eclinm.2022.101818. This article has 129 citations and is from a peer-reviewed journal.

16. (suppiah2023multiplatformmolecularprofiling pages 1-2): Suganth Suppiah, Sheila Mansouri, Yasin Mamatjan, Jeffrey C. Liu, Minu M. Bhunia, Vikas Patil, Prisni Rath, Bharati Mehani, Pardeep Heir, Severa Bunda, German L. Velez-Reyes, Olivia Singh, Nazanin Ijad, Neda Pirouzmand, Tatyana Dalcourt, Ying Meng, Shirin Karimi, Qingxia Wei, Farshad Nassiri, Trevor J. Pugh, Gary D. Bader, Kenneth D. Aldape, David A. Largaespada, and Gelareh Zadeh. Multiplatform molecular profiling uncovers two subgroups of malignant peripheral nerve sheath tumors with distinct therapeutic vulnerabilities. Nature Communications, May 2023. URL: https://doi.org/10.1038/s41467-023-38432-6, doi:10.1038/s41467-023-38432-6. This article has 49 citations and is from a highest quality peer-reviewed journal.

17. (fournier2023psychosocialimplicationsof pages 13-15): Hugo Fournier, Nicolas Calcagni, Fanny Morice-Picard, and Bruno Quintard. Psychosocial implications of rare genetic skin diseases affecting appearance on daily life experiences, emotional state, self-perception and quality of life in adults: a systematic review. Orphanet Journal of Rare Diseases, Feb 2023. URL: https://doi.org/10.1186/s13023-023-02629-1, doi:10.1186/s13023-023-02629-1. This article has 57 citations and is from a peer-reviewed journal.

18. (fournier2023psychosocialimplicationsof pages 15-16): Hugo Fournier, Nicolas Calcagni, Fanny Morice-Picard, and Bruno Quintard. Psychosocial implications of rare genetic skin diseases affecting appearance on daily life experiences, emotional state, self-perception and quality of life in adults: a systematic review. Orphanet Journal of Rare Diseases, Feb 2023. URL: https://doi.org/10.1186/s13023-023-02629-1, doi:10.1186/s13023-023-02629-1. This article has 57 citations and is from a peer-reviewed journal.

19. (peduto2023neurofibromatosistype1 pages 11-13): Cristina Peduto, Mariateresa Zanobio, Vincenzo Nigro, Silverio Perrotta, Giulio Piluso, and Claudia Santoro. Neurofibromatosis type 1: pediatric aspects and review of genotype–phenotype correlations. Cancers, 15:1217, Feb 2023. URL: https://doi.org/10.3390/cancers15041217, doi:10.3390/cancers15041217. This article has 80 citations.

20. (yao2023malignantperipheralnerve pages 13-14): Chengjun Yao, Haiying Zhou, Yanzhao Dong, Ahmad Alhaskawi, Sohaib Hasan Abdullah Ezzi, Zewei Wang, Jingtian Lai, Vishnu Goutham Kota, Mohamed Hasan Abdulla Hasan Abdulla, and Hui Lu. Malignant peripheral nerve sheath tumors: latest concepts in disease pathogenesis and clinical management. Cancers, 15:1077, Feb 2023. URL: https://doi.org/10.3390/cancers15041077, doi:10.3390/cancers15041077. This article has 118 citations.

21. (baezflores2023thetherapeuticpotential pages 1-2): Juan Báez-Flores, Mario Rodríguez-Martín, and Jesus Lacal. The therapeutic potential of neurofibromin signaling pathways and binding partners. Communications Biology, Apr 2023. URL: https://doi.org/10.1038/s42003-023-04815-0, doi:10.1038/s42003-023-04815-0. This article has 47 citations and is from a peer-reviewed journal.

22. (baezflores2023thetherapeuticpotential pages 3-4): Juan Báez-Flores, Mario Rodríguez-Martín, and Jesus Lacal. The therapeutic potential of neurofibromin signaling pathways and binding partners. Communications Biology, Apr 2023. URL: https://doi.org/10.1038/s42003-023-04815-0, doi:10.1038/s42003-023-04815-0. This article has 47 citations and is from a peer-reviewed journal.

23. (baezflores2023thetherapeuticpotential pages 5-6): Juan Báez-Flores, Mario Rodríguez-Martín, and Jesus Lacal. The therapeutic potential of neurofibromin signaling pathways and binding partners. Communications Biology, Apr 2023. URL: https://doi.org/10.1038/s42003-023-04815-0, doi:10.1038/s42003-023-04815-0. This article has 47 citations and is from a peer-reviewed journal.

24. (na2024pastpresentand pages 5-6): Brian Na, Shilp R. Shah, and Harish N. Vasudevan. Past, present, and future therapeutic strategies for nf-1-associated tumors. Current Oncology Reports, 26:706-713, May 2024. URL: https://doi.org/10.1007/s11912-024-01527-4, doi:10.1007/s11912-024-01527-4. This article has 20 citations and is from a peer-reviewed journal.

25. (tang2023neurofibromatosistype1associated pages 6-8): Yunshuo Tang and David H Gutmann. Neurofibromatosis type 1-associated optic pathway gliomas: current challenges and future prospects. Cancer Management and Research, 15:667-681, Jul 2023. URL: https://doi.org/10.2147/cmar.s362678, doi:10.2147/cmar.s362678. This article has 36 citations and is from a peer-reviewed journal.

26. (carton2023erngenturistumour pages 6-7): Charlotte Carton, D. Gareth Evans, Ignacio Blanco, Reinhard E. Friedrich, Rosalie E. Ferner, Said Farschtschi, Hector Salvador, Amedeo A. Azizi, Victor Mautner, Claas Röhl, Sirkku Peltonen, Stavros Stivaros, Eric Legius, Rianne Oostenbrink, Joan Brunet, Frank Van Calenbergh, Catherine Cassiman, Thomas Czech, María José Gavarrete de León, Henk Giele, Susie Henley, Conxi Lazaro, Vera Lipkovskaya, Eamonn R. Maher, Vanessa Martin, Irene Mathijssen, Enrico Opocher, Ana Elisabete Pires, Thomas Pletschko, Eirene Poupaki, Vita Ridola, Andre Rietman, Thorsten Rosenbaum, Alastair Santhouse, Astrid Sehested, Ian Simmons, Walter Taal, and Anja Wagner. Ern genturis tumour surveillance guidelines for individuals with neurofibromatosis type 1. eClinicalMedicine, 56:101818, Feb 2023. URL: https://doi.org/10.1016/j.eclinm.2022.101818, doi:10.1016/j.eclinm.2022.101818. This article has 129 citations and is from a peer-reviewed journal.

27. (carton2023erngenturistumour pages 5-6): Charlotte Carton, D. Gareth Evans, Ignacio Blanco, Reinhard E. Friedrich, Rosalie E. Ferner, Said Farschtschi, Hector Salvador, Amedeo A. Azizi, Victor Mautner, Claas Röhl, Sirkku Peltonen, Stavros Stivaros, Eric Legius, Rianne Oostenbrink, Joan Brunet, Frank Van Calenbergh, Catherine Cassiman, Thomas Czech, María José Gavarrete de León, Henk Giele, Susie Henley, Conxi Lazaro, Vera Lipkovskaya, Eamonn R. Maher, Vanessa Martin, Irene Mathijssen, Enrico Opocher, Ana Elisabete Pires, Thomas Pletschko, Eirene Poupaki, Vita Ridola, Andre Rietman, Thorsten Rosenbaum, Alastair Santhouse, Astrid Sehested, Ian Simmons, Walter Taal, and Anja Wagner. Ern genturis tumour surveillance guidelines for individuals with neurofibromatosis type 1. eClinicalMedicine, 56:101818, Feb 2023. URL: https://doi.org/10.1016/j.eclinm.2022.101818, doi:10.1016/j.eclinm.2022.101818. This article has 129 citations and is from a peer-reviewed journal.

28. (legius2021reviseddiagnosticcriteria media 67536eac): Eric Legius, Ludwine Messiaen, Pierre Wolkenstein, Patrice Pancza, Robert A. Avery, Yemima Berman, Jaishri Blakeley, Dusica Babovic-Vuksanovic, Karin Soares Cunha, Rosalie Ferner, Michael J. Fisher, Jan M. Friedman, David H. Gutmann, Hildegard Kehrer-Sawatzki, Bruce R. Korf, Victor-Felix Mautner, Sirkku Peltonen, Katherine A. Rauen, Vincent Riccardi, Elizabeth Schorry, Anat Stemmer-Rachamimov, David A. Stevenson, Gianluca Tadini, Nicole J. Ullrich, David Viskochil, Katharina Wimmer, Kaleb Yohay, Alicia Gomes, Justin T. Jordan, Victor Mautner, Vanessa L. Merker, Miriam J. Smith, David Stevenson, Monique Anten, Arthur Aylsworth, Diana Baralle, Sebastien Barbarot, Fred Barker, Shay Ben-Shachar, Amanda Bergner, Didier Bessis, Ignacio Blanco, Catherine Cassiman, Patricia Ciavarelli, Maurizio Clementi, Thierry Frébourg, Marco Giovannini, Dorothy Halliday, Chris Hammond, C.O. Hanemann, Helen Hanson, Arvid Heiberg, Pascal Joly, Michel Kalamarides, Matthias Karajannis, Daniela Kroshinsky, Margarita Larralde, Conxi Lázaro, Lu Le, Michael Link, Robert Listernick, Mia MacCollin, Conor Mallucci, Christopher Moertel, Amy Mueller, Joanne Ngeow, Rianne Oostenbrink, Roger Packer, Laura Papi, Allyson Parry, Juha Peltonen, Dominique Pichard, Bruce Poppe, Nilton Rezende, Luiz Oswaldo Rodrigues, Tena Rosser, Martino Ruggieri, Eduard Serra, Verena Steinke-Lange, Stavros Michael Stivaros, Amy Taylor, Jaan Toelen, James Tonsgard, Eva Trevisson, Meena Upadhyaya, Ali Varan, Meredith Wilson, Hao Wu, Gelareh Zadeh, Susan M. Huson, D. Gareth Evans, and Scott R. Plotkin. Revised diagnostic criteria for neurofibromatosis type 1 and legius syndrome: an international consensus recommendation. Genetics in Medicine, 23:1506-1513, Aug 2021. URL: https://doi.org/10.1038/s41436-021-01170-5, doi:10.1038/s41436-021-01170-5. This article has 888 citations and is from a highest quality peer-reviewed journal.

29. (legius2021reviseddiagnosticcriteria media 57806d8a): Eric Legius, Ludwine Messiaen, Pierre Wolkenstein, Patrice Pancza, Robert A. Avery, Yemima Berman, Jaishri Blakeley, Dusica Babovic-Vuksanovic, Karin Soares Cunha, Rosalie Ferner, Michael J. Fisher, Jan M. Friedman, David H. Gutmann, Hildegard Kehrer-Sawatzki, Bruce R. Korf, Victor-Felix Mautner, Sirkku Peltonen, Katherine A. Rauen, Vincent Riccardi, Elizabeth Schorry, Anat Stemmer-Rachamimov, David A. Stevenson, Gianluca Tadini, Nicole J. Ullrich, David Viskochil, Katharina Wimmer, Kaleb Yohay, Alicia Gomes, Justin T. Jordan, Victor Mautner, Vanessa L. Merker, Miriam J. Smith, David Stevenson, Monique Anten, Arthur Aylsworth, Diana Baralle, Sebastien Barbarot, Fred Barker, Shay Ben-Shachar, Amanda Bergner, Didier Bessis, Ignacio Blanco, Catherine Cassiman, Patricia Ciavarelli, Maurizio Clementi, Thierry Frébourg, Marco Giovannini, Dorothy Halliday, Chris Hammond, C.O. Hanemann, Helen Hanson, Arvid Heiberg, Pascal Joly, Michel Kalamarides, Matthias Karajannis, Daniela Kroshinsky, Margarita Larralde, Conxi Lázaro, Lu Le, Michael Link, Robert Listernick, Mia MacCollin, Conor Mallucci, Christopher Moertel, Amy Mueller, Joanne Ngeow, Rianne Oostenbrink, Roger Packer, Laura Papi, Allyson Parry, Juha Peltonen, Dominique Pichard, Bruce Poppe, Nilton Rezende, Luiz Oswaldo Rodrigues, Tena Rosser, Martino Ruggieri, Eduard Serra, Verena Steinke-Lange, Stavros Michael Stivaros, Amy Taylor, Jaan Toelen, James Tonsgard, Eva Trevisson, Meena Upadhyaya, Ali Varan, Meredith Wilson, Hao Wu, Gelareh Zadeh, Susan M. Huson, D. Gareth Evans, and Scott R. Plotkin. Revised diagnostic criteria for neurofibromatosis type 1 and legius syndrome: an international consensus recommendation. Genetics in Medicine, 23:1506-1513, Aug 2021. URL: https://doi.org/10.1038/s41436-021-01170-5, doi:10.1038/s41436-021-01170-5. This article has 888 citations and is from a highest quality peer-reviewed journal.

30. (gross2023longtermsafetyand pages 1-2): Andrea M Gross, Eva Dombi, Pamela L Wolters, Andrea Baldwin, Anne Dufek, Kailey Herrera, Staci Martin, Joanne Derdak, Kara S Heisey, Patricia M Whitcomb, Seth M Steinberg, David J Venzon, Michael J Fisher, AeRang Kim, Miriam Bornhorst, Brian D Weiss, Jaishri O Blakeley, Malcolm A Smith, and Brigitte C Widemann. Long-term safety and efficacy of selumetinib in children with neurofibromatosis type 1 on a phase 1/2 trial for inoperable plexiform neurofibromas. Neuro-oncology, 25:1883-1894, Apr 2023. URL: https://doi.org/10.1093/neuonc/noad086, doi:10.1093/neuonc/noad086. This article has 117 citations and is from a domain leading peer-reviewed journal.

31. (tang2023neurofibromatosistype1associated pages 4-6): Yunshuo Tang and David H Gutmann. Neurofibromatosis type 1-associated optic pathway gliomas: current challenges and future prospects. Cancer Management and Research, 15:667-681, Jul 2023. URL: https://doi.org/10.2147/cmar.s362678, doi:10.2147/cmar.s362678. This article has 36 citations and is from a peer-reviewed journal.

32. (yao2023malignantperipheralnerve pages 11-13): Chengjun Yao, Haiying Zhou, Yanzhao Dong, Ahmad Alhaskawi, Sohaib Hasan Abdullah Ezzi, Zewei Wang, Jingtian Lai, Vishnu Goutham Kota, Mohamed Hasan Abdulla Hasan Abdulla, and Hui Lu. Malignant peripheral nerve sheath tumors: latest concepts in disease pathogenesis and clinical management. Cancers, 15:1077, Feb 2023. URL: https://doi.org/10.3390/cancers15041077, doi:10.3390/cancers15041077. This article has 118 citations.

33. (casey2021fdaapprovalsummary pages 1-1): Denise Casey, Suzanne Demko, Arup Sinha, Pallavi S. Mishra-Kalyani, Yuan-li Shen, Sachia Khasar, M. Anwar Goheer, Whitney S. Helms, Lili Pan, Yuan Xu, Jianghong Fan, Ruby Leong, Jiang Liu, Yuching Yang, Katherine Windsor, Mei Ou, Olen Stephens, Byeongtaek Oh, Gregory H. Reaman, Abhilasha Nair, Stacy S. Shord, Vishal Bhatnagar, Selena R. Daniels, Sharon Sickafuse, Kirsten B. Goldberg, Marc R. Theoret, Richard Pazdur, and Harpreet Singh. Fda approval summary: selumetinib for plexiform neurofibroma. Clinical Cancer Research, 27:4142-4146, Mar 2021. URL: https://doi.org/10.1158/1078-0432.ccr-20-5032, doi:10.1158/1078-0432.ccr-20-5032. This article has 122 citations and is from a highest quality peer-reviewed journal.

34. (azizi2024consensusrecommendationson pages 1-2): Amedeo A Azizi, Darren Hargrave, João Passos, Pierre Wolkenstein, Thorsten Rosenbaum, Claudia Santoro, Verena Rosenmayr, Thomas Pletschko, Paolo A Ascierto, and Héctor Salvador Hernández. Consensus recommendations on management of selumetinib-associated adverse events in pediatric patients with neurofibromatosis type 1 and plexiform neurofibromas. Neuro-Oncology Practice, 11:515-531, Apr 2024. URL: https://doi.org/10.1093/nop/npae038, doi:10.1093/nop/npae038. This article has 23 citations and is from a peer-reviewed journal.

35. (NCT01362803 chunk 1):  AZD6244 Hydrogen Sulfate for Children With Nervous System Tumors. National Cancer Institute (NCI). 2011. ClinicalTrials.gov Identifier: NCT01362803

36. (NCT03962543 chunk 1):  MEK Inhibitor Mirdametinib (PD-0325901) in Patients With Neurofibromatosis Type 1 Associated Plexiform Neurofibromas. SpringWorks Therapeutics, Inc.. 2019. ClinicalTrials.gov Identifier: NCT03962543

37. (NCT05388370 chunk 1):  PASS of Paediatric Patients Initiating Selumetinib. AstraZeneca. 2022. ClinicalTrials.gov Identifier: NCT05388370

38. (NCT03231306 chunk 1): Bruce Korf, MD. Phase II Study of Binimetinib in Children and Adults With NF1 Plexiform Neurofibromas. University of Alabama at Birmingham. 2017. ClinicalTrials.gov Identifier: NCT03231306

39. (carton2023erngenturistumour pages 7-8): Charlotte Carton, D. Gareth Evans, Ignacio Blanco, Reinhard E. Friedrich, Rosalie E. Ferner, Said Farschtschi, Hector Salvador, Amedeo A. Azizi, Victor Mautner, Claas Röhl, Sirkku Peltonen, Stavros Stivaros, Eric Legius, Rianne Oostenbrink, Joan Brunet, Frank Van Calenbergh, Catherine Cassiman, Thomas Czech, María José Gavarrete de León, Henk Giele, Susie Henley, Conxi Lazaro, Vera Lipkovskaya, Eamonn R. Maher, Vanessa Martin, Irene Mathijssen, Enrico Opocher, Ana Elisabete Pires, Thomas Pletschko, Eirene Poupaki, Vita Ridola, Andre Rietman, Thorsten Rosenbaum, Alastair Santhouse, Astrid Sehested, Ian Simmons, Walter Taal, and Anja Wagner. Ern genturis tumour surveillance guidelines for individuals with neurofibromatosis type 1. eClinicalMedicine, 56:101818, Feb 2023. URL: https://doi.org/10.1016/j.eclinm.2022.101818, doi:10.1016/j.eclinm.2022.101818. This article has 129 citations and is from a peer-reviewed journal.

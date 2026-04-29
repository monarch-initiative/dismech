---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T16:00:45.049951'
end_time: '2026-04-05T16:12:47.071439'
duration_seconds: 722.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: HER2-Positive Gastric Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HER2-Positive Gastric Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **HER2-Positive Gastric Cancer** covering all of the
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
- **Disease Name:** HER2-Positive Gastric Cancer
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **HER2-Positive Gastric Cancer** covering all of the
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


## Comprehensive Research Report: HER2-Positive Gastric Cancer (HER2+ GC)

### Executive summary
HER2-positive gastric/gastroesophageal junction (GEJ) adenocarcinoma is a biomarker-defined subtype of gastric/GEJ adenocarcinoma characterized most commonly by **ERBB2 (HER2) amplification and/or protein overexpression** that is actionable with HER2-directed therapy. HER2+ disease represents roughly **~15–25%** of gastric/GEJ cancers in aggregate estimates, with higher rates in **GEJ/proximal** and **intestinal-type** tumors, and with clinically important **spatial/temporal heterogeneity** that affects testing accuracy and therapeutic durability. First-line therapy historically relied on **trastuzumab + fluoropyrimidine/platinum chemotherapy** (ToGA), and recent practice has incorporated **immune checkpoint inhibition** with trastuzumab/chemotherapy (KEYNOTE-811). After progression on trastuzumab-based therapy, **trastuzumab deruxtecan (T‑DXd)** has demonstrated superior response and overall survival versus chemotherapy (DESTINY-Gastric01). (kawakami2024recentprogressin pages 1-2, nakamura2021biomarkertargetedtherapiesfor pages 4-5, shitara2024trastuzumabderuxtecanin pages 1-2)

---

## 1. Disease information

### 1.1 What is the disease?
**HER2-positive gastric cancer** refers to **gastric or gastroesophageal junction adenocarcinoma** in which tumor cells show **HER2 overexpression (IHC 3+)** and/or **ERBB2 gene amplification** (typically confirmed by in situ hybridization when IHC is equivocal). This is a predictive biomarker state used to select HER2-targeted systemic therapy in advanced/metastatic disease. (bartley2017her2testingand pages 16-16, kawakami2024recentprogressin pages 1-2)

### 1.2 Key identifiers (ontology / classification cross-references)
* **Disease category:** Malignant neoplasm; gastrointestinal cancer; gastric/GEJ adenocarcinoma subtype defined by predictive biomarker (HER2/ERBB2).
* **MeSH / ICD-10 / ICD-11 / MONDO:** A specific MONDO identifier for “HER2-positive gastric cancer” was **not retrieved from the tool-supported evidence** in this run. The closest directly retrieved ontology entity was **gastric adenocarcinoma** (Open Targets disease entity id **EFO_0000503**). (kawakami2024recentprogressin pages 1-2)

### 1.3 Synonyms / alternative names
Commonly used alternatives in the literature and guidelines include:
* **HER2-positive gastric adenocarcinoma**
* **HER2-positive gastroesophageal junction adenocarcinoma**
* **HER2-positive gastroesophageal adenocarcinoma (GEA)**
* **ERBB2-amplified gastric cancer / HER2-overexpressing gastric cancer**
These terms are used at disease-aggregate level and in clinical trial eligibility definitions. (bartley2017her2testingand pages 16-16, nakamura2021biomarkertargetedtherapiesfor pages 4-5)

### 1.4 Evidence source type
The subtype definition and management guidance is derived mainly from **aggregated disease-level resources** (clinical practice guidelines, multicenter trials, systematic reviews), rather than individual EHR case series. (bartley2017her2testingand pages 16-16, kawakami2024recentprogressin pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors and mechanistic drivers
In HER2+ gastric/GEJ adenocarcinoma, the key actionable molecular driver is **ERBB2/HER2 amplification and/or protein overexpression**, enabling HER2 receptor signaling and oncogenic growth/survival programs; however, **co-occurring driver amplifications (e.g., MET/EGFR/FGFR2)** and heterogeneity can attenuate response to HER2-directed agents. (shitara2024trastuzumabderuxtecanin pages 1-2, nakamura2021biomarkertargetedtherapiesfor pages 4-5)

### 2.2 Risk factors (for gastric cancer broadly)
Because HER2 positivity is a biomarker subset within gastric/GEJ adenocarcinoma, most established risk factors are described for **gastric cancer overall** (particularly non-cardia) rather than uniquely for HER2+ disease.

**Global major risk factors (authoritative review, 2023):** Thrift et al. summarize established risk factors including **Helicobacter pylori infection** (dominant contributor for non-cardia disease), **cigarette smoking**, **excess body fat**, and **diets high in salt/processed meats**. They note H. pylori accounts for “almost 90%” of distal/non-cardia gastric cancers. (thrift2023globalburdenof pages 1-2)

**Smoking effect sizes (systematic review/meta-analysis, publication date Jan 2024):** Rota et al. meta-analyzed 205 studies and found **current smokers vs never smokers: RR 1.53 (95% CI 1.44–1.62)** and **former smokers: RR 1.30 (95% CI 1.23–1.37)**; for subsites, **cardia RR 2.08 (95% CI 1.66–2.61)** and **distal RR 1.48 (95% CI 1.33–1.66)** among current smokers. (rota2024doseresponseassociationbetween pages 1-2)

### 2.3 Protective factors
Thrift et al. describe possible protective associations including **high vegetable intake**, and potential chemopreventive associations reported for **NSAIDs/aspirin** and **statins** (observational and some trial-level signals), acknowledging confounding and heterogeneity across studies. (thrift2023globalburdenof pages 1-2, thrift2023globalburdenof pages 8-9)

### 2.4 Gene–environment interactions
Gene–environment interactions are not uniquely established for the HER2+ subtype in the retrieved evidence; however, the broader gastric-cancer literature emphasizes multifactorial etiologies with infection- and lifestyle-related carcinogenesis interacting with tumor genomic evolution. (thrift2023globalburdenof pages 1-2)

---

## 3. Phenotypes

### 3.1 Clinical presentation (gastric/GEJ adenocarcinoma; not unique to HER2+)
This run did not retrieve phenotype-frequency tables specific to HER2+ GC. In practice, presentation overlaps with gastric/GEJ adenocarcinoma generally, including:
* Upper gastrointestinal symptoms (e.g., dyspepsia, early satiety), weight loss, anemia/bleeding, dysphagia when GEJ involved.
* Advanced disease manifestations including metastatic pain, ascites, or obstructive symptoms.

### 3.2 Suggested HPO terms (examples)
Because phenotype frequencies were not retrieved, the following are **candidate** terms commonly applicable to gastric/GEJ adenocarcinoma presentations:
* **Abdominal pain** (HP:0002027)
* **Weight loss** (HP:0001824)
* **Anemia** (HP:0001903)
* **Melena / gastrointestinal bleeding** (HP:0002240)
* **Vomiting** (HP:0002013)
* **Dysphagia** (HP:0002015; particularly GEJ)

(These HPO mappings are provided as ontology suggestions; quantitative frequency attribution is not supported by retrieved evidence in this run.)

---

## 4. Genetic / molecular information

### 4.1 Causal genes / key biomarkers
* **ERBB2 (HER2)** is the defining predictive biomarker gene for HER2+ gastric/GEJ adenocarcinoma, typically altered by **copy-number amplification** and associated **protein overexpression**. (bartley2017her2testingand pages 16-16, bartley2017her2testingand pages 2-4)

### 4.2 Pathogenic variants and alteration types
HER2+ gastric cancer is dominated clinically by **amplification/overexpression** rather than germline pathogenic variants. Reviews also note other ERBB2 alteration classes (e.g., missense mutations, insertions, fusions) in gastroesophageal cancers, but clinical decision-making in routine practice remains driven primarily by **IHC/ISH-defined HER2 positivity**. (scheck2024her2positivegastriccancer pages 1-2, bartley2017her2testingand pages 16-16)

### 4.3 Modifier alterations relevant to resistance
* **ctDNA evidence (DESTINY-Gastric01 biomarker analysis, Nature Medicine 2024):** Baseline co-amplifications **MET, EGFR, FGFR2** in circulating tumor DNA were associated with **numerically lower ORR** to T‑DXd, and tissue–plasma concordance for ERBB2 amplification was **64%**. (shitara2024trastuzumabderuxtecanin pages 1-2)
* **WES paired biopsies under trastuzumab (Oncogenesis 2023):** acquired mutations were commonly observed in **AURKA, MYC, STK11, LRP6** (each in 4 patients), and an “extensive clonal branching pattern” was associated with shorter PFS (HR 4.71). (xu2023exploringpotentialmolecular pages 1-2)

### 4.4 Epigenetic information
Not specifically retrieved for HER2+ GC in this run.

### 4.5 Chromosomal abnormalities
Gastric cancer broadly includes chromosomal instability subtypes; for HER2+ disease, ERBB2 amplification is a copy-number event. Quantitative cytogenetic abnormality catalogs were not retrieved here. (nakamura2021biomarkertargetedtherapiesfor pages 4-5)

---

## 5. Environmental information
For gastric cancer broadly:
* **Infectious agent:** **H. pylori** is a central cause for non-cardia disease and a major prevention target. (thrift2023globalburdenof pages 1-2)
* **Lifestyle:** smoking increases risk with dose–response and reduced risk with cessation over time. (rota2024doseresponseassociationbetween pages 1-2)
* **Diet:** high salt/processed meats are risk factors; dietary changes and food preservation improvements are implicated in secular declines. (thrift2023globalburdenof pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Conceptual causal chain
1. **Initiation and background carcinogenesis**: environmental exposures (H. pylori, smoking, diet) contribute to chronic injury/inflammation and neoplastic transformation in gastric mucosa (especially non-cardia). (thrift2023globalburdenof pages 1-2)
2. **Oncogenic selection**: tumor clones acquire and select for **ERBB2 amplification and HER2 overexpression** in a subset of gastric/GEJ adenocarcinomas, creating a therapeutically actionable dependency. (bartley2017her2testingand pages 16-16)
3. **Therapy response**: HER2-directed antibodies/ADCs (trastuzumab, T‑DXd) target HER2-expressing cells, producing tumor regression in responsive tumors. (kawakami2024recentprogressin pages 1-2, shitara2024trastuzumabderuxtecanin pages 1-2)
4. **Resistance and relapse**: **spatial and temporal heterogeneity** (mixed HER2 expression across regions), **loss of HER2 expression**, and/or emergence of **bypass signaling** or co-drivers (e.g., MET/EGFR/FGFR2 amplifications) contribute to acquired resistance and limited durability. (nakamura2021biomarkertargetedtherapiesfor pages 4-5, shitara2024trastuzumabderuxtecanin pages 1-2)

### 6.2 Heterogeneity and resistance (key current understanding)
* **Heterogeneity drives testing and response variability:** CAP/ASCP/ASCO emphasize “considerable heterogeneity of HER2 protein and gene expression in GEAs,” with basolateral/lateral staining patterns and sampling challenges. (bartley2017her2testingand pages 16-16, bartley2017her2testingand pages 2-4)
* **HER2 loss after therapy:** A Nature Reviews Clinical Oncology review reports that ~30% of initially HER2+ tumors may lose HER2 expression after trastuzumab-containing first-line therapy, supporting reassessment strategies. (nakamura2021biomarkertargetedtherapiesfor pages 4-5)

### 6.3 Suggested ontology terms
* **GO biological processes (suggested):** ERBB2 signaling pathway; receptor tyrosine kinase signaling; regulation of cell proliferation; immune evasion/PD‑1 signaling in combination strategies.
* **CL cell types (suggested):** gastric epithelial cell / adenocarcinoma cell; tumor-associated macrophage; CD8-positive T cell.

(These ontology suggestions are mechanistically consistent but are not enumerated from a dedicated ontology extraction tool in this run.)

---

## 7. Anatomical structures affected

### 7.1 Organ and site
* Primary sites: **stomach** and **gastroesophageal junction** (adenocarcinoma). (bartley2017her2testingand pages 16-16, ruschoff2010her2diagnosticsin pages 1-2)

### 7.2 Suggested UBERON terms (examples)
* **stomach** (UBERON:0000945)
* **gastroesophageal junction** (UBERON:…; identifier not retrieved in this run)

---

## 8. Temporal development
HER2+ gastric/GEJ adenocarcinoma follows the natural history of gastric/GEJ adenocarcinoma, with late presentation common in many regions. The key HER2-specific temporal feature is **temporal biomarker evolution**, including possible HER2 loss after trastuzumab therapy, motivating reassessment. (nakamura2021biomarkertargetedtherapiesfor pages 4-5, xu2023exploringpotentialmolecular pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (gastric cancer overall; GLOBOCAN/GBD-derived)
* **Global burden (2023 review citing 2020):** gastric cancer was the **5th most common cancer** and **4th leading cause of cancer death**, with **1,089,000 cases** and **769,000 deaths** in 2020, and projected **~62% increase** in cases by 2040. (thrift2023globalburdenof pages 1-2)
* **GLOBOCAN 2022 summary (early-onset GC burden paper using GLOBOCAN 2022):** estimated **968,000 new cases** and **660,000 deaths** in 2022; ASIR **9.2** and ASMR **6.1** per 100,000; East Asia accounted for **53.8% of cases** and **48.2% of deaths**. (tan2024globalregionaland pages 1-2)

### 9.2 HER2 positivity frequency
* Reported HER2 positivity varies by cohort and methods. The CAP/ASCP/ASCO guideline cites **7–38%** HER2 amplification/overexpression estimates across studies, with higher frequency at the GEJ and in intestinal-type tumors. (bartley2017her2testingand pages 2-4)
* ToGA screening reported **22.1%** HER2 positivity among screened patients, with higher rates in GEJ and intestinal histology. (ruschoff2010her2diagnosticsin pages 1-2, bartley2017her2testingand pages 5-6)

### 9.3 Inheritance
HER2+ gastric cancer is **not typically an inherited Mendelian disease**; actionable HER2 status is usually **somatic**.

---

## 10. Diagnostics

### 10.1 Standard clinical biomarker testing for HER2
**CAP/ASCP/ASCO guideline (JCO; publication date Feb 2017; URL https://doi.org/10.1200/JCO.2016.69.4836):**
* Begin with **IHC**.
* If IHC is **0/1+ (negative)** or **3+ (positive)**, no further testing is required.
* If IHC is **2+ (equivocal)**, reflex to **ISH**.
* HER2-positive = **IHC 3+** or **IHC 2+ and ISH amplified**.
Direct guideline language (from retrieved excerpt): “**Testing should begin with IHC… If the result is equivocal (2+) by IHC, subsequent testing by ISH should be performed**…” (bartley2017her2testingand pages 16-16)

### 10.2 Gastric/GEJ-specific scoring nuances (biopsy vs resection; basolateral staining)
Rüschoff et al. validated modified gastric scoring aligned with ToGA-era practice, emphasizing that gastric cancer often shows **incomplete (basolateral/lateral) membranous staining**, and that biopsies require different cutoffs. Figure/Table in the retrieved images specify:
* **Biopsy:** minimum focus of **≥5 cohesive stained tumor cells**.
* **Resection specimen:** **≥10%** tumor area cutoff.
These criteria are shown in the retrieved scoring scheme visuals (Figure 2/Table 2). (ruschoff2010her2diagnosticsin media e7198008, ruschoff2010her2diagnosticsin media b116cc28)

### 10.3 Liquid biopsy / ctDNA (emerging diagnostics and monitoring)
ctDNA is increasingly used for **response monitoring** and for addressing tumor heterogeneity limitations of single-site tissue biopsies.

**Serial ctDNA monitoring in HER2+ metastatic GC (Yonsei Med J; publication date Aug 2023; URL https://doi.org/10.3349/ymj.2023.0096):** In 15 HER2+ metastatic gastric cancer patients treated with systemic therapy including PD‑1 inhibitor, baseline ctDNA showed **>1 alteration in 93%**, CNAs in **53.3%**, and **ERBB2 amplification in 40%**; longitudinal ctDNA molecular tumor burden index provided **2–42 weeks lead time** (mean **13.4 weeks**) for detecting progression versus CT imaging. (jung2023monitoringtheoutcomes pages 1-2)

**ddPCR HER2 CNV (Heliyon; publication date Nov 2023; URL https://doi.org/10.1016/j.heliyon.2023.e21339):** ddPCR-based ctDNA HER2 copy-number assessment showed ~**91%** concordance with tissue IHC/FISH in the excerpt and serial changes reflected therapeutic efficacy and resistance. (kleinscory2023liquidbiopsybased pages 1-2)

---

## 11. Outcome / prognosis
Prognosis in advanced gastric cancer remains poor globally, but survival improves with effective biomarker-matched therapy.

* The CAP/ASCP/ASCO guideline notes conflicting evidence for HER2 as a prognostic biomarker and highlights that benefit from trastuzumab depends on accurate HER2 classification. (bartley2017her2testingand pages 5-6)
* In trastuzumab-treated cohorts, heterogeneity and discordant HER2 calls can associate with worse outcomes; reviews report that HER2 heterogeneity is associated with shorter PFS on trastuzumab. (nakamura2021biomarkertargetedtherapiesfor pages 4-5)

---

## 12. Treatment

### 12.1 Current standard systemic therapies (real-world implementation)
A consolidated table of major evidence and implementation notes is provided below.

| Setting/line | Regimen | Key study (trial name, publication year, journal) | Population & HER2 definition | Key efficacy results | Key safety signal(s) | Regulatory/guideline status notes |
|---|---|---|---|---|---|---|
| 1L advanced/metastatic HER2+ gastric/GEJ adenocarcinoma | Trastuzumab + fluoropyrimidine/platinum chemotherapy | **ToGA**, 2010, *Lancet*; outcomes summarized in 2024 review | Untreated advanced gastric/GEJ adenocarcinoma; HER2+ defined in practice/guidelines as **IHC 3+ or IHC 2+/ISH+**; greater benefit in high expressors (IHC2+/ISH+ or IHC3+) (kawakami2024recentprogressin pages 1-2, bartley2017her2testingand pages 16-16, bartley2017her2testingand pages 2-4) | **OS 13.8 vs 11.1 mo** (HR **0.74**, 95% CI **0.60–0.91**); **PFS 6.7 vs 5.5 mo** (HR **0.71**, 95% CI **0.59–0.85**); **ORR 47% vs 35%**; high-HER2 subgroup OS ~**16.0 vs 11.8 mo** (HR **0.65**) (kawakami2024recentprogressin pages 1-2, scheck2024her2positivegastriccancer pages 1-2) | Cardiac adverse events low (~**6%**) with no between-group difference; slightly more diarrhea, stomatitis, cytopenias, fatigue, weight loss; grade 3–4 events broadly similar except diarrhea (bartley2017her2testingand pages 5-6) | Established first HER2-targeted standard of care; CAP/ASCP/ASCO and NCCN recommend HER2 testing in advanced disease and trastuzumab-based chemo for HER2+ tumors (bartley2017her2testingand pages 16-16, bartley2017her2testingand pages 1-2) |
| 1L advanced/metastatic HER2+ gastric/GEJ adenocarcinoma | Pembrolizumab + trastuzumab + chemotherapy | **KEYNOTE-811**, interim analyses reported 2023/*Lancet*; outcomes summarized in 2024 *Cancers* review | HER2+ advanced gastric/GEJ adenocarcinoma; review uses standard HER2+ definition **IHC 3+ or IHC 2+/ISH+** (kawakami2024recentprogressin pages 1-2, bartley2017her2testingand pages 16-16) | **ORR 72.6% vs 59.8%**; **PFS 10.0 vs 8.1 mo** (HR **0.72**, 95% CI **0.60–0.87**); **OS 20.0 vs 16.9 mo** (HR **0.87**, 95% CI **0.72–1.06**) as reported in 2024 review (kawakami2024recentprogressin pages 1-2) | Detailed AE breakdown not provided in gathered evidence here; combination immunotherapy adds immune-related toxicity considerations in practice (cen2024efficacyandsafety pages 10-10) | Review notes FDA **rapid approval** based on marked response benefit before mature survival results; now incorporated into modern first-line treatment landscape/guidelines for eligible HER2+ disease (kawakami2024recentprogressin pages 1-2) |
| ≥2L / trastuzumab-pretreated unresectable or metastatic HER2+ gastric/GEJ adenocarcinoma | Trastuzumab deruxtecan (T-DXd) | **DESTINY-Gastric01**, 2020, *NEJM*; biomarker analysis 2024, *Nature Medicine* | Centrally confirmed HER2+ gastric/GEJ adenocarcinoma after ≥2 prior therapies including trastuzumab; HER2+ defined as **IHC 3+ or IHC 2+/ISH+** (shitara2024trastuzumabderuxtecanin pages 1-2) | **ORR 51% vs 14%**; **OS 12.5 vs 8.4 mo** (HR for death **0.59**, 95% CI **0.39–0.88**); biomarker analysis confirmed benefit and noted ORR **58.3%** in patients with HER2 gain-of-function mutations (7/12) (shitara2024trastuzumabderuxtecanin pages 1-2) | Major grade ≥3 AEs: neutropenia **51%**, anemia **38%**, decreased WBC **21%**; T-DXd-related ILD/pneumonitis in **12** patients, including grade 3–4 in **3**, with **1 drug-related death** from pneumonia (shitara2024trastuzumabderuxtecanin pages 1-2) | Became new later-line standard after trastuzumab failure; benchmark post-trastuzumab HER2-directed option in reviews/guideline discussions (kawakami2024recentprogressin pages 1-2, scheck2024her2positivegastriccancer pages 1-2) |
| Post-trastuzumab setting, Western single-arm confirmation | Trastuzumab deruxtecan (T-DXd) | **DESTINY-Gastric02**, phase II; cited in 2024 reviews and trial registry | Unresectable/metastatic HER2+ gastric/GEJ adenocarcinoma in US/Europe after prior trastuzumab-based regimen; HER2+ status required (shitara2024trastuzumabderuxtecanin pages 1-2) | Quantitative efficacy results not provided in gathered evidence here; reviews state the study **confirmed activity** of T-DXd in Western populations (kawakami2024recentprogressin pages 1-2, scheck2024her2positivegastriccancer pages 1-2) | Safety details not numerically reported in gathered evidence here; ILD remains a class-defining concern with T-DXd (extrapolated from DESTINY-Gastric01 evidence in this chat) (shitara2024trastuzumabderuxtecanin pages 1-2) | Supports real-world Western implementation and underpins ongoing phase III **DESTINY-Gastric04** strategy/validation program (NCT04704934) (shitara2024trastuzumabderuxtecanin pages 1-2) |
| Diagnostic implementation across lines | **HER2 testing workflow:** IHC first, reflex ISH if IHC 2+ | **CAP/ASCP/ASCO HER2 Testing Guideline**, 2017; NCCN 2023 cited | Advanced gastroesophageal adenocarcinoma candidates for HER2 therapy; biopsy or resection acceptable; HER2 positivity = **IHC 3+ or IHC 2+/ISH amplified**; biopsy cutoff **≥5 cohesive tumor cells**, resection cutoff **≥10%** stained tumor cells; gastric scoring differs from breast because of heterogeneity and basolateral/lateral staining (bartley2017her2testingand pages 16-16, bartley2017her2testingand pages 2-4, ruschoff2010her2diagnosticsin media e7198008) | Not an efficacy study; testing accuracy is clinically important because local/central discordance and HER2 heterogeneity affect benefit from trastuzumab-based therapy (ruschoff2010her2diagnosticsin pages 1-2, bartley2017her2testingand pages 5-6) | Key implementation risk is false-negative/discordant classification from heterogeneity, specimen quality, and interpretation differences (ruschoff2010her2diagnosticsin pages 1-2, bartley2017her2testingand pages 2-4) | Testing is standard prerequisite for trastuzumab-based 1L therapy and for selecting later-line HER2-directed options; repeat tissue collection is recommended if prior material is inadequate/uninterpretable (bartley2017her2testingand pages 16-16, bartley2017her2testingand pages 1-2) |
| Real-world/biomarker implementation | ctDNA/liquid biopsy for HER2 and resistance monitoring | 2023–2024 translational/real-world studies | HER2+ metastatic gastric cancer; serial ctDNA captures heterogeneity and evolving resistance better than single-site tissue in some settings (jung2023monitoringtheoutcomes pages 1-2, kleinscory2023liquidbiopsybased pages 1-2) | In one 2023 serial ctDNA study (n=15), progression was detected **2–42 weeks earlier** than CT (mean **13.4 weeks**); baseline ctDNA showed >1 alteration in **93%**, CNAs in **53.3%**, ERBB2 amplification in **40%** (jung2023monitoringtheoutcomes pages 1-2) | Not a treatment safety issue; main limitation is imperfect concordance with tissue and possible false positive/negative findings depending on assay/platform (xu2023exploringpotentialmolecular pages 1-2, kleinscory2023liquidbiopsybased pages 1-2) | Not yet a replacement for guideline-mandated tissue HER2 testing, but increasingly useful for response/resistance monitoring and research stratification (bartley2017her2testingand pages 16-16, jung2023monitoringtheoutcomes pages 1-2) |


*Table: This table summarizes the core clinical evidence, diagnostic implementation, and emerging real-world monitoring approaches for HER2-positive gastric/GEJ adenocarcinoma using only evidence gathered in this chat. It is useful for quickly comparing first-line and later-line standards, trial outcomes, safety issues, and HER2 testing requirements.*

#### First-line (advanced/metastatic)
**Trastuzumab + chemotherapy (ToGA):** In ToGA, trastuzumab + fluoropyrimidine/platinum improved OS (13.8 vs 11.1 months; HR 0.74) and PFS (6.7 vs 5.5 months; HR 0.71) and ORR (47% vs 35%). (kawakami2024recentprogressin pages 1-2)

**Pembrolizumab + trastuzumab + chemotherapy (KEYNOTE-811; contemporary practice):** A 2024 review reports improved ORR (72.6% vs 59.8%) and PFS (10.0 vs 8.1 months; HR 0.72) with OS trend not yet significant at interim analysis. The same review notes FDA rapid approval based on strong response/PFS signals. (kawakami2024recentprogressin pages 1-2)

#### Later-line (after trastuzumab)
**Trastuzumab deruxtecan (T‑DXd; DESTINY-Gastric01):** In centrally confirmed HER2+ patients, T‑DXd achieved ORR **51%** vs **14%** with physician’s choice chemotherapy and improved OS (median **12.5 vs 8.4 months**). ILD/pneumonitis and myelosuppression are key toxicities. (shitara2024trastuzumabderuxtecanin pages 1-2)

### 12.2 Treatment strategy / expert analysis
Recent authoritative reviews emphasize that therapeutic durability is limited by **resistance mechanisms and HER2 heterogeneity**, and that integration of **immunotherapy with HER2-targeted therapy** represents a major ongoing shift in the field. (scheck2024her2positivegastriccancer pages 1-2, kawakami2024recentprogressin pages 1-2)

### 12.3 Suggested MAXO terms (examples; not exhaustively validated here)
* Anti-HER2 monoclonal antibody therapy (trastuzumab)
* Antibody–drug conjugate therapy (trastuzumab deruxtecan)
* Immune checkpoint inhibitor therapy (pembrolizumab)
* Platinum-based chemotherapy

---

## 13. Prevention
Primary prevention for gastric cancer overall centers on **H. pylori control**, tobacco cessation, and dietary risk reduction.

* Thrift et al. highlight H. pylori eradication and screening/surveillance as promising strategies and note WHO-level policy interest in screen-and-treat approaches depending on regional risk and prevalence. (thrift2023globalburdenof pages 10-10, thrift2023globalburdenof pages 1-2)
* Smoking cessation has strong evidence of risk reduction over time since quitting (e.g., RR ~0.65 at 30 years since cessation in dose–response modeling). (rota2024doseresponseassociationbetween pages 1-2)

(HER2 positivity itself is not currently a target for primary prevention; it is a treatment-selection biomarker within established gastric/GEJ adenocarcinoma.)

---

## 14. Other species / natural disease
Not applicable as a “disease” entity (this is a biomarker-defined human cancer subtype). Preclinical xenograft/organoid studies are covered below.

---

## 15. Model organisms / model systems
The most relevant “models” for HER2+ gastric cancer research are **patient-derived xenografts (PDX)** and **patient-derived organoids (PDO)** used to study resistance and test targeted combinations.

* A preclinical gastric cancer PDX resistance model study established trastuzumab-sensitive and acquired-resistant PDXs and found multiple pathways implicated (ERBB family, MAPK, PI3K/AKT, JAK/STAT, cell cycle), with combination strategies (e.g., HER3-targeted antibody or MEK inhibitor) showing activity in the model. (kawakami2024recentprogressin pages 1-2)
* A 2024 preprint describes establishing PDX and PDO models harboring ERBB2 amplification for spatial profiling of resistance mechanisms to trastuzumab and T‑DXd (preprint evidence should be interpreted cautiously). (kawakami2024recentprogressin pages 1-2)

---

## Notes on evidence limitations for this run
1. **Ontology IDs (MONDO/MeSH/ICD) specific to HER2+ gastric cancer** were not fully retrieved; the report therefore provides best-effort mapping and explicitly flags missing identifiers.
2. **Phenotype frequencies** specific to HER2+ disease were not retrieved; HPO terms are suggested without frequency claims.
3. Some KEYNOTE‑811 details and DESTINY‑Gastric02 numeric outcomes were not available in the retrieved full-text evidence snippets and are therefore not asserted beyond what is explicitly captured in the cited sources.

---

## Key source URLs (with publication dates)
* Bartley et al. **HER2 Testing Guideline** (J Clin Oncol; **Feb 2017**): https://doi.org/10.1200/JCO.2016.69.4836 (bartley2017her2testingand pages 16-16)
* Rüschoff et al. **HER2 scoring validation in gastric cancer** (Virchows Arch; **Jul 2010**): https://doi.org/10.1007/s00428-010-0952-2 (ruschoff2010her2diagnosticsin pages 1-2)
* Kawakami & Yamazaki **Treatment progress review** (Cancers; **Apr 2024**): https://doi.org/10.3390/cancers16091747 (kawakami2024recentprogressin pages 1-2)
* Shitara et al. **DESTINY-Gastric01 biomarker analysis** (Nat Med; **May 2024**): https://doi.org/10.1038/s41591-024-02992-x (shitara2024trastuzumabderuxtecanin pages 1-2)
* Thrift et al. **Global burden review** (Nat Rev Clin Oncol; **Mar 2023**): https://doi.org/10.1038/s41571-023-00747-0 (thrift2023globalburdenof pages 1-2)
* Rota et al. **Smoking meta-analysis** (Gastric Cancer; **Jan 2024**): https://doi.org/10.1007/s10120-023-01459-1 (rota2024doseresponseassociationbetween pages 1-2)
* Jung et al. **Serial ctDNA monitoring in HER2+ metastatic GC** (Yonsei Med J; **Aug 2023**): https://doi.org/10.3349/ymj.2023.0096 (jung2023monitoringtheoutcomes pages 1-2)
* Klein‑Scory et al. **ctDNA HER2 CNV ddPCR** (Heliyon; **Nov 2023**): https://doi.org/10.1016/j.heliyon.2023.e21339 (kleinscory2023liquidbiopsybased pages 1-2)

References

1. (kawakami2024recentprogressin pages 1-2): Takeshi Kawakami and Kentaro Yamazaki. Recent progress in treatment for her2-positive advanced gastric cancer. Cancers, 16:1747, Apr 2024. URL: https://doi.org/10.3390/cancers16091747, doi:10.3390/cancers16091747. This article has 11 citations.

2. (nakamura2021biomarkertargetedtherapiesfor pages 4-5): Yoshiaki Nakamura, Akihito Kawazoe, Florian Lordick, Yelena Y. Janjigian, and Kohei Shitara. Biomarker-targeted therapies for advanced-stage gastric and gastro-oesophageal junction cancers: an emerging paradigm. Nature Reviews Clinical Oncology, 18:473-487, Mar 2021. URL: https://doi.org/10.1038/s41571-021-00492-2, doi:10.1038/s41571-021-00492-2. This article has 281 citations and is from a domain leading peer-reviewed journal.

3. (shitara2024trastuzumabderuxtecanin pages 1-2): Kohei Shitara, Yung-Jue Bang, Satoru Iwasa, Naotoshi Sugimoto, Min-Hee Ryu, Daisuke Sakai, Hyun Cheol Chung, Hisato Kawakami, Hiroshi Yabusaki, Yasuhiro Sakamoto, Tomohiro Nishina, Koichiro Inaki, Yusuke Kuwahara, Naoya Wada, Fumitaka Suto, Takeo Arita, Masahiro Sugihara, Zenta Tsuchihashi, Kaku Saito, Akihito Kojima, and Kensei Yamaguchi. Trastuzumab deruxtecan in her2-positive advanced gastric cancer: exploratory biomarker analysis of the randomized, phase 2 destiny-gastric01 trial. Nature Medicine, 30:1933-1942, May 2024. URL: https://doi.org/10.1038/s41591-024-02992-x, doi:10.1038/s41591-024-02992-x. This article has 104 citations and is from a highest quality peer-reviewed journal.

4. (bartley2017her2testingand pages 16-16): Angela N. Bartley, M. Washington, Carol Colasacco, Christina B. Ventura, Nofisat Ismaila, A. Benson, A. Carrato, M. Gulley, D. Jain, S. Kakar, H. Mackay, C. Streutker, Laura H. Tang, M. Troxell, and J. Ajani. Her2 testing and clinical decision making in gastroesophageal adenocarcinoma: guideline from the college of american pathologists, american society for clinical pathology, and the american society of clinical oncology. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 35 4:446-464, Feb 2017. URL: https://doi.org/10.1200/jco.2016.69.4836, doi:10.1200/jco.2016.69.4836. This article has 776 citations.

5. (thrift2023globalburdenof pages 1-2): Aaron P. Thrift, Theresa Nguyen Wenker, and Hashem B. El-Serag. Global burden of gastric cancer: epidemiological trends, risk factors, screening and prevention. Nature Reviews Clinical Oncology, 20:338-349, Mar 2023. URL: https://doi.org/10.1038/s41571-023-00747-0, doi:10.1038/s41571-023-00747-0. This article has 825 citations and is from a domain leading peer-reviewed journal.

6. (rota2024doseresponseassociationbetween pages 1-2): Matteo Rota, Irene Possenti, Valeria Valsassina, Claudia Santucci, Vincenzo Bagnardi, Giovanni Corrao, Cristina Bosetti, Claudia Specchia, Silvano Gallus, and Alessandra Lugo. Dose-response association between cigarette smoking and gastric cancer risk: a systematic review and meta-analysis. Gastric cancer : official journal of the International Gastric Cancer Association and the Japanese Gastric Cancer Association, 27:197-209, Jan 2024. URL: https://doi.org/10.1007/s10120-023-01459-1, doi:10.1007/s10120-023-01459-1. This article has 71 citations.

7. (thrift2023globalburdenof pages 8-9): Aaron P. Thrift, Theresa Nguyen Wenker, and Hashem B. El-Serag. Global burden of gastric cancer: epidemiological trends, risk factors, screening and prevention. Nature Reviews Clinical Oncology, 20:338-349, Mar 2023. URL: https://doi.org/10.1038/s41571-023-00747-0, doi:10.1038/s41571-023-00747-0. This article has 825 citations and is from a domain leading peer-reviewed journal.

8. (bartley2017her2testingand pages 2-4): Angela N. Bartley, M. Washington, Carol Colasacco, Christina B. Ventura, Nofisat Ismaila, A. Benson, A. Carrato, M. Gulley, D. Jain, S. Kakar, H. Mackay, C. Streutker, Laura H. Tang, M. Troxell, and J. Ajani. Her2 testing and clinical decision making in gastroesophageal adenocarcinoma: guideline from the college of american pathologists, american society for clinical pathology, and the american society of clinical oncology. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 35 4:446-464, Feb 2017. URL: https://doi.org/10.1200/jco.2016.69.4836, doi:10.1200/jco.2016.69.4836. This article has 776 citations.

9. (scheck2024her2positivegastriccancer pages 1-2): Magdalena K. Scheck, Ralf D. Hofheinz, and Sylvie Lorenzen. Her2-positive gastric cancer and antibody treatment: state of the art and future developments. Cancers, 16:1336, Mar 2024. URL: https://doi.org/10.3390/cancers16071336, doi:10.3390/cancers16071336. This article has 39 citations.

10. (xu2023exploringpotentialmolecular pages 1-2): Qi Xu, Xiaoqing Xu, Haimeng Tang, Junrong Yan, Jingjing Li, Hua Bao, Xue Wu, Yang Shao, Cong Luo, Haimin Wen, Jianying Jin, and Jieer Ying. Exploring potential molecular resistance and clonal evolution in advanced her2-positive gastric cancer under trastuzumab therapy. Oncogenesis, 12:1-11, Apr 2023. URL: https://doi.org/10.1038/s41389-023-00466-2, doi:10.1038/s41389-023-00466-2. This article has 18 citations and is from a domain leading peer-reviewed journal.

11. (ruschoff2010her2diagnosticsin pages 1-2): Josef Rüschoff, Manfred Dietel, Gustavo Baretton, Susanne Arbogast, Axel Walch, Geneviéve Monges, Marie-Pierre Chenard, Frédérique Penault-Llorca, Iris Nagelmeier, Werner Schlake, H. Höfler, and H. H. Kreipe. Her2 diagnostics in gastric cancer—guideline validation and development of standardized immunohistochemical testing. Virchows Archiv, 457:299-307, Jul 2010. URL: https://doi.org/10.1007/s00428-010-0952-2, doi:10.1007/s00428-010-0952-2. This article has 642 citations and is from a peer-reviewed journal.

12. (tan2024globalregionaland pages 1-2): Nuopei Tan, Hongliang Wu, Maomao Cao, Fan Yang, Xinxin Yan, Siyi He, Mengdi Cao, Shaoli Zhang, Yi Teng, Qianru Li, Jiachen Wang, Changfa Xia, and Wanqing Chen. Global, regional, and national burden of early-onset gastric cancer. Cancer Biology & Medicine, 21:667-678, Aug 2024. URL: https://doi.org/10.20892/j.issn.2095-3941.2024.0159, doi:10.20892/j.issn.2095-3941.2024.0159. This article has 52 citations.

13. (bartley2017her2testingand pages 5-6): Angela N. Bartley, M. Washington, Carol Colasacco, Christina B. Ventura, Nofisat Ismaila, A. Benson, A. Carrato, M. Gulley, D. Jain, S. Kakar, H. Mackay, C. Streutker, Laura H. Tang, M. Troxell, and J. Ajani. Her2 testing and clinical decision making in gastroesophageal adenocarcinoma: guideline from the college of american pathologists, american society for clinical pathology, and the american society of clinical oncology. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 35 4:446-464, Feb 2017. URL: https://doi.org/10.1200/jco.2016.69.4836, doi:10.1200/jco.2016.69.4836. This article has 776 citations.

14. (ruschoff2010her2diagnosticsin media e7198008): Josef Rüschoff, Manfred Dietel, Gustavo Baretton, Susanne Arbogast, Axel Walch, Geneviéve Monges, Marie-Pierre Chenard, Frédérique Penault-Llorca, Iris Nagelmeier, Werner Schlake, H. Höfler, and H. H. Kreipe. Her2 diagnostics in gastric cancer—guideline validation and development of standardized immunohistochemical testing. Virchows Archiv, 457:299-307, Jul 2010. URL: https://doi.org/10.1007/s00428-010-0952-2, doi:10.1007/s00428-010-0952-2. This article has 642 citations and is from a peer-reviewed journal.

15. (ruschoff2010her2diagnosticsin media b116cc28): Josef Rüschoff, Manfred Dietel, Gustavo Baretton, Susanne Arbogast, Axel Walch, Geneviéve Monges, Marie-Pierre Chenard, Frédérique Penault-Llorca, Iris Nagelmeier, Werner Schlake, H. Höfler, and H. H. Kreipe. Her2 diagnostics in gastric cancer—guideline validation and development of standardized immunohistochemical testing. Virchows Archiv, 457:299-307, Jul 2010. URL: https://doi.org/10.1007/s00428-010-0952-2, doi:10.1007/s00428-010-0952-2. This article has 642 citations and is from a peer-reviewed journal.

16. (jung2023monitoringtheoutcomes pages 1-2): Seung-Hyun Jung, Choong-kun Lee, Woo Sun Kwon, Sujin Yun, Minkyu Jung, Hyo Song Kim, Hyun Cheol Chung, Yeun-Jun Chung, and Sun Young Rha. Monitoring the outcomes of systemic chemotherapy including immune checkpoint inhibitor for her2-positive metastatic gastric cancer by liquid biopsy. Yonsei Medical Journal, 64:531-540, Aug 2023. URL: https://doi.org/10.3349/ymj.2023.0096, doi:10.3349/ymj.2023.0096. This article has 8 citations and is from a peer-reviewed journal.

17. (kleinscory2023liquidbiopsybased pages 1-2): Susanne Klein-Scory, Swetlana Ladigan-Badura, Thomas Mika, Berlinda Verdoodt, Andrea Tannapfel, Michael Pohl, Roland Schroers, and Alexander Baraniskin. Liquid biopsy based her2 amplification status in gastric cancer patients indicates clinical response. Heliyon, 9:e21339, Nov 2023. URL: https://doi.org/10.1016/j.heliyon.2023.e21339, doi:10.1016/j.heliyon.2023.e21339. This article has 8 citations.

18. (bartley2017her2testingand pages 1-2): Angela N. Bartley, M. Washington, Carol Colasacco, Christina B. Ventura, Nofisat Ismaila, A. Benson, A. Carrato, M. Gulley, D. Jain, S. Kakar, H. Mackay, C. Streutker, Laura H. Tang, M. Troxell, and J. Ajani. Her2 testing and clinical decision making in gastroesophageal adenocarcinoma: guideline from the college of american pathologists, american society for clinical pathology, and the american society of clinical oncology. Journal of clinical oncology : official journal of the American Society of Clinical Oncology, 35 4:446-464, Feb 2017. URL: https://doi.org/10.1200/jco.2016.69.4836, doi:10.1200/jco.2016.69.4836. This article has 776 citations.

19. (cen2024efficacyandsafety pages 10-10): Shuyi Cen, Meiqin Yuan, Qunan Sun, Guilan Hou, Jieer Ying, Qi Xu, Yu Zheng, Ying Dong, Hongming Pan, and Weidong Han. Efficacy and safety of dual blockade of her2 and pd-1 in patients with her2-positive gastric cancer: a retrospective, multicentre study. Scientific Reports, Oct 2024. URL: https://doi.org/10.1038/s41598-024-76296-y, doi:10.1038/s41598-024-76296-y. This article has 7 citations and is from a peer-reviewed journal.

20. (thrift2023globalburdenof pages 10-10): Aaron P. Thrift, Theresa Nguyen Wenker, and Hashem B. El-Serag. Global burden of gastric cancer: epidemiological trends, risk factors, screening and prevention. Nature Reviews Clinical Oncology, 20:338-349, Mar 2023. URL: https://doi.org/10.1038/s41571-023-00747-0, doi:10.1038/s41571-023-00747-0. This article has 825 citations and is from a domain leading peer-reviewed journal.

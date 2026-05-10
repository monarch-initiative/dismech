---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:54:48.757998'
end_time: '2026-05-09T12:09:03.399641'
duration_seconds: 854.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Medulloblastoma, WNT-Activated
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Medulloblastoma, WNT-Activated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Medulloblastoma, WNT-Activated** covering all of the
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
- **Disease Name:** Medulloblastoma, WNT-Activated
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Medulloblastoma, WNT-Activated** covering all of the
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


# Medulloblastoma, WNT-Activated — Disease Characteristics Research Report

## Target Disease
- **Disease name:** Medulloblastoma, WNT-activated (WNT medulloblastoma; WNT-MB)
- **Category:** Pediatric/AYA embryonal CNS tumor (posterior fossa)
- **MONDO ID:** Not identified from the retrieved evidence in this run (would require direct MONDO lookup outside the current tool outputs).

---

## 1. Disease Information

### Overview / definition
WNT-activated medulloblastoma is a molecularly defined medulloblastoma entity characterized by activation of the canonical WNT/β-catenin pathway, most commonly through **CTNNB1 exon 3 hotspot mutations** with resultant **nuclear β-catenin accumulation**; it comprises roughly **~10%** of medulloblastomas overall. (moreno2023highfrequencyof pages 2-3, shcherbina2023comparativeanalysisof pages 2-4)

**Typical location** is midline/central posterior fossa around the **fourth ventricle**, with potential extension toward the cerebellar peduncle/brainstem; neuroradiology often shows diffusion restriction and typical posterior fossa mass effects. (jackson2023recentadvancesin pages 1-2, rechberger2023exploringthemolecular pages 1-2, shcherbina2023comparativeanalysisof pages 2-4)

### Key identifiers and terminologies (available in evidence)
- **WHO concept:** WNT-activated medulloblastoma is a WHO-recognized molecular subgroup/entity used in integrated diagnosis frameworks. (mani2024clinicoradiologicaloutcomesin pages 1-2, rechberger2023exploringthemolecular pages 1-2)
- **Common synonyms:** WNT medulloblastoma; WNT subgroup medulloblastoma; WNT-pathway medulloblastoma; WNT-MB; WNT-driven medulloblastoma. (mani2023wntpathwaymedulloblastomawhat pages 2-4, NCT02724579a chunk 1)

> **Note on ICD/MeSH/OMIM/Orphanet/MONDO:** Specific numeric identifiers were not present in the retrieved texts; therefore they cannot be reported with citations from this tool run.

### Evidence source type
The disease concept and frequencies are derived from **aggregated disease-level resources** (reviews/cohort series) and **multi-institutional clinical cohorts**, not from EHR-only individual patient sources. (nobre2020patternofrelapse pages 1-3, moreno2023highfrequencyof pages 2-3, shcherbina2023comparativeanalysisof pages 2-4)

---

## 2. Etiology

### Primary causal factors (molecular/genetic)
1. **Somatic CTNNB1 activating mutations (exon 3)** are the dominant driver in WNT-MB (~85–90% in many reports). These mutations prevent normal phosphorylation/degradation of β-catenin and lead to **β-catenin nuclear translocation** and transcriptional activation. (moreno2023highfrequencyof pages 2-3, ntenti2023clinicalhistologicaland pages 4-5)
2. A clinically important minority of WNT-MB cases are **CTNNB1-wild type**, frequently linked to **germline APC pathogenic variants** (familial adenomatous polyposis/Turcot syndrome). (moreno2023highfrequencyof pages 2-3, moreno2023highfrequencyof pages 1-2)
3. Recurrent cooperating alterations commonly include **DDX3X** and **SMARCA4** mutations, with **monosomy 6** as a characteristic copy-number feature (particularly pediatric WNT-α). (shcherbina2023comparativeanalysisof pages 2-4, mani2024clinicoradiologicaloutcomesin pages 10-11)

**Direct abstract quote (molecular definition):** Moreno et al. state that WNT-activated medulloblastomas are “usually caused by mutations in the CTNNB1 gene (85%–90%), and most remaining cases of CTNNB1 wild type are thought to be caused by germline mutations in APC.” (Frontiers in Oncology; Sep 2023; https://doi.org/10.3389/fonc.2023.1237170) (moreno2023highfrequencyof pages 2-3)

### Risk factors
- **Genetic predisposition:** CTNNB1-wildtype WNT-MB should raise suspicion for **germline APC** (FAP/Turcot), and referral for genetic cancer risk assessment and APC sequencing has been explicitly recommended in this setting. (moreno2023highfrequencyof pages 2-3)

**Direct abstract quote (genetic counseling implication):** The same 2023 study concludes: “Considering that CTNNB1 wild-type cases may exhibit APC germline mutations, our study suggests a higher incidence (~30%) of hereditary WNT-activated medulloblastomas in the Latin-Iberian population.” (Frontiers in Oncology; Sep 2023; https://doi.org/10.3389/fonc.2023.1237170) (moreno2023highfrequencyof pages 2-3)

### Protective factors / gene–environment interactions
No protective environmental factors or gene–environment interaction evidence specific to WNT-MB was identified in the retrieved sources.

---

## 3. Phenotypes (clinical presentation, HPO suggestions)

### Typical presentation (symptoms/signs)
Posterior fossa medulloblastoma commonly presents with:
- **Headache** and **vomiting** consistent with raised intracranial pressure (often worse on awakening, progressive). (jackson2023recentadvancesin pages 1-2)
- **Ataxia/gait instability** due to cerebellar dysfunction (particularly midline vermian involvement). (jackson2023recentadvancesin pages 1-2)
- In infants/very young children: **macrocephaly**, fussiness, decreased oral intake (non-localizing symptoms). (jackson2023recentadvancesin pages 1-2)

Dissemination at diagnosis across medulloblastoma overall is reported around **~20–25%** (not WNT-specific), while WNT-MB cohorts often show low metastatic rates at diagnosis (e.g., “very rare <5%” in one cohort table). (jackson2023recentadvancesin pages 1-2, mani2024clinicoradiologicaloutcomesin pages 1-2)

### WNT-MB clinico-anatomic tendencies
WNT-MB is described as centrally located near midline posterior fossa/fourth ventricle with potential extension into peduncle/brainstem. (shcherbina2023comparativeanalysisof pages 2-4, rechberger2023exploringthemolecular pages 1-2)

### HPO term suggestions (for KB population; not claims of frequency unless noted)
- Headache — **HP:0002315**
- Vomiting — **HP:0002013**
- Ataxia — **HP:0001251**
- Gait ataxia — **HP:0002066**
- Hydrocephalus — **HP:0000238** (common mechanism for raised ICP)
- Increased intracranial pressure — **HP:0002516**
- Macrocephaly (infants) — **HP:0000256**

### Quality of life impact
Long-term survivorship issues remain a major challenge in pediatric medulloblastoma, and high-dose craniospinal irradiation is emphasized as associated with long-term neurocognitive harm, motivating de-intensification trials in WNT-MB. (jackson2023recentadvancesin pages 1-2, slika2023theneurodevelopmentaland pages 7-8)

A 2024 WNT cohort report explicitly notes that absence of recorded neurocognitive and late-effect data prevents direct assessment of QoL impact in that series (highlighting a common real-world data gap). (mani2024clinicoradiologicaloutcomesin pages 11-12)

---

## 4. Genetic / Molecular Information

### Causal / hallmark genes and alterations
- **CTNNB1 (β-catenin)**: somatic exon 3 hotspot mutations in most WNT-MB. (moreno2023highfrequencyof pages 2-3, shcherbina2023comparativeanalysisof pages 2-4)
- **APC**: germline pathogenic variants in a subset of CTNNB1-wildtype WNT-MB, associated with FAP/Turcot. (moreno2023highfrequencyof pages 2-3, moreno2023highfrequencyof pages 1-2)
- **DDX3X**, **SMARCA4**: recurrently altered in WNT-MB. (shcherbina2023comparativeanalysisof pages 2-4, slika2023theneurodevelopmentaland pages 2-4)
- **Copy-number:** **monosomy 6** is a supportive hallmark, particularly enriched in pediatric WNT-α compared to WNT-β. (mani2024clinicoradiologicaloutcomesin pages 10-11, slika2023theneurodevelopmentaland pages 2-4)

### Molecular subtypes within WNT
Two WNT subtypes are described:
- **WNT-α**: younger/pediatric, enriched for monosomy 6. (mani2024clinicoradiologicaloutcomesin pages 10-11, slika2023theneurodevelopmentaland pages 2-4)
- **WNT-β**: older/adult-leaning, less monosomy 6, sometimes worse prognosis in adult contexts. (mani2024clinicoradiologicaloutcomesin pages 10-11, slika2023theneurodevelopmentaland pages 2-4)

### Variant classification / allele frequency
ACMG/AMP classifications and population allele frequencies (gnomAD) were not available in the retrieved evidence.

### Epigenetics and methylation-class definition
WNT-MB is part of modern methylation-based CNS tumor classification, and real-world clinical workflows use EPIC methylation arrays and online classifiers to support WHO-recognized diagnoses (including WNT-MB). (green2024wnt‐activatedmyc‐amplifiedmedulloblastoma pages 2-3, wolff2024implementationofmethylation pages 5-8)

---

## 5. Mechanism / Pathophysiology

### Core pathway mechanism (canonical WNT)
A causal chain supported by the retrieved literature:
1. **CTNNB1 exon 3 stabilization mutation** (or APC loss in predisposition) →
2. **β-catenin accumulation and nuclear translocation** →
3. Transcriptional activation of WNT-responsive programs supporting tumorigenesis and defining subgroup biology. (moreno2023highfrequencyof pages 2-3, ntenti2023clinicalhistologicaland pages 4-5)

### Developmental origin and cell-of-origin hypotheses
WNT-MB is proposed to arise from lower rhombic lip / pontine mossy-fiber precursor–related lineages in the dorsal brainstem region (extracerebellar origin), consistent with GEMM data and subgroup developmental mapping. (slika2023theneurodevelopmentaland pages 2-4, manfreda2023wntsignalingin pages 11-12)

### Tumor microenvironment and BBB
WNT-MB is linked to distinctive vasculature and a locally disrupted blood–brain barrier, which has been proposed to facilitate chemotherapy penetration and contribute to favorable outcomes. (slika2023theneurodevelopmentaland pages 7-8, nor2018clinicalandpreclinical pages 20-24)

### GO biological process term suggestions
- Canonical Wnt signaling pathway — **GO:0060070**
- Regulation of cell proliferation — **GO:0042127**
- Neurogenesis — **GO:0022008**
- Brain development — **GO:0007420**

### CL (cell type) term suggestions
Given proposed rhombic lip/pontine precursor origins:
- Neural progenitor cell — **CL:0000673**
- Neuron — **CL:0000540** (tumor cells show neuronal-like differentiation states in subgroup analyses) (slika2023theneurodevelopmentaland pages 2-4)

---

## 6. Anatomical Structures Affected (UBERON suggestions)
- Cerebellum — **UBERON:0002037**
- Fourth ventricle region — (ventricular system context; commonly used in neuroanatomy mapping) (rechberger2023exploringthemolecular pages 1-2, jackson2023recentadvancesin pages 1-2)
- Brainstem / cerebellar peduncle involvement (extension) — (shcherbina2023comparativeanalysisof pages 2-4)

---

## 7. Temporal Development, Inheritance, Population, and Prognosis

### Age at onset
WNT-MB typically affects older children/adolescents (median ~11–12 years), is rare in infants, and comprises a minority of adult medulloblastomas (~10–15% of adult MB in one review summary). (shcherbina2023comparativeanalysisof pages 2-4, mani2024clinicoradiologicaloutcomesin pages 1-2)

### Epidemiology (subgroup frequency)
WNT-MB is typically ~10% of medulloblastomas, though cohort composition varies; a Latin-Iberian multi-institution series reported **15% (40/266)** WNT-activated tumors. (moreno2023highfrequencyof pages 2-3, moreno2023highfrequencyof pages 1-2)

### Inheritance
Most cases are sporadic, but CTNNB1-wildtype WNT-MB has an important association with **germline APC** (FAP/Turcot), motivating genetic counseling and testing. (moreno2023highfrequencyof pages 2-3)

### Prognosis: key statistics
- **Excellent frontline outcomes** are typical, often reported as **>90% 5-year survival** in pediatric WNT-MB. (upadhyay2024riskstratifiedradiotherapyin pages 4-5, slika2023theneurodevelopmentaland pages 7-8)
- A 2024 institutional WNT cohort reported **5-year PFS 87.7%** and **5-year OS 91.2%** at median 72-month follow-up. (Diagnostics; Feb 2024; https://doi.org/10.3390/diagnostics14040358) (mani2024clinicoradiologicaloutcomesin pages 1-2)
- A large international molecularly confirmed cohort (n=93) reported **5-year PFS 0.84** with **15 relapses**. (Cell Reports Medicine; Jun 2020; https://doi.org/10.1016/j.xcrm.2020.100038) (nobre2020patternofrelapse pages 1-3)

### Relapse patterns
Relapses are uncommon but frequently metastatic; in the 93-patient cohort, **12/15 relapses** were metastatic, with a distinctive tendency to involve the **lateral ventricles** (8/12 metastatic relapses). Outcomes after relapse were poor with limited salvage, and relapse risk was strongly influenced by the maintenance chemotherapy regimen (higher cumulative cyclophosphamide/ifosfamide exposure associated with fewer relapses). (nobre2020patternofrelapse pages 1-3)

---

## 8. Diagnostics

### Imaging
Medulloblastomas typically arise near the superior fourth ventricle/inferior medullary velum region, frequently show diffusion restriction, and may show heterogeneous enhancement/cysts/necrosis on MRI. (jackson2023recentadvancesin pages 1-2)

### Histopathology and immunohistochemistry
- WNT-MB is often classic histology. (jackson2023recentadvancesin pages 1-2, shcherbina2023comparativeanalysisof pages 2-4)
- **Nuclear β-catenin** staining is a key diagnostic feature used clinically and in trial screening. (jackson2023recentadvancesin pages 1-2, NCT02724579a chunk 2)

### Molecular testing workflow (real-world implementation)
A pragmatic diagnostic strategy supported by the retrieved sources:
1. **CTNNB1 testing** (e.g., Sanger sequencing) because exon 3 mutations define most WNT-MB. (moreno2023highfrequencyof pages 2-3)
2. **β-catenin IHC** (nuclear positivity) as an accessible diagnostic marker and eligibility screen for WNT-directed trials. (jackson2023recentadvancesin pages 1-2, NCT02724579a chunk 2)
3. **DNA methylation profiling** (Illumina EPIC arrays → MolecularNeuropathology.org/DKFZ classifier) to confirm subgroup and generate CNV plots; multiple real-world implementations show feasibility and typical classifier confidence thresholds.
   - A 2024 case report illustrates EPIC-based methylation classification for WNT-MB with discussion of confidence scores (≥0.9 strongly supporting a WHO-recognized class; an example case had 0.78, highlighting heterogeneity and need for orthogonal confirmation). (green2024wnt‐activatedmyc‐amplifiedmedulloblastoma pages 2-3)
   - A 2024 implementation study in Brazil used EPIC arrays and MolecularNeuropathology.org classifiers, with diagnostic agreement in 94% and classifier scores ≥0.9 in ~81% of cases, showing operational feasibility in a public health center workflow. (Preprint; Nov 2024; https://doi.org/10.21203/rs.3.rs-5332503/v1) (wolff2024implementationofmethylation pages 5-8)
4. **Germline APC testing** is recommended when WNT-MB is CTNNB1-wildtype. (moreno2023highfrequencyof pages 2-3)

---

## 9. Treatment (standard of care, de-escalation, and real-world trials)

### Standard frontline management (context)
Contemporary WNT-MB management is typically **maximal safe resection** followed by **risk-stratified craniospinal irradiation (CSI) + boost** and multi-agent chemotherapy, achieving high cure rates but with substantial late toxicity concerns. (mani2024clinicoradiologicaloutcomesin pages 11-12, slika2023theneurodevelopmentaland pages 7-8)

**MAXO suggestions (for KB mapping; representative):**
- Surgical resection — **MAXO:0000114**
- Craniospinal irradiation — (radiotherapy action term)
- Combination chemotherapy — (chemotherapy action term)
- Audiology monitoring — (monitoring/assessment term)
- Endocrine function monitoring — (monitoring/assessment term)

### De-escalation rationale and caution
Because WNT-MB has excellent outcomes, multiple efforts seek to **reduce CSI dose and/or chemotherapy intensity** to improve long-term quality of survival. (mani2023wntpathwaymedulloblastomawhat pages 2-4, upadhyay2024riskstratifiedradiotherapyin pages 4-5)

However, early attempts at more aggressive de-intensification have been unsafe:
- A 2023 review notes that two prospective de-intensification strategies (including **omission of upfront CSI**) were terminated early due to “unacceptably high relapse rates,” supporting the conclusion that **CSI remains integral** to curative therapy. (mani2023wntpathwaymedulloblastomawhat pages 1-2)
- A 2024 review summary describes a pilot omission-of-CSI approach as inferior, with rapid relapses requiring salvage CSI (reported as all relapsing within <1 year in that summary). (upadhyay2024riskstratifiedradiotherapyin pages 4-5)

### Key ongoing/major clinical trials (ClinicalTrials.gov details)

1. **COG ACNS1422 — NCT02724579** (start 2017; status ACTIVE_NOT_RECRUITING)
   - **Population:** newly diagnosed **WNT-driven, average-risk** medulloblastoma; age **≥3 and <22**; **M0** by brain/spine MRI and **negative CSF cytology**; residual ≤1.5 cm²; classical histology; screening includes **nuclear β-catenin IHC**, **CTNNB1 mutation**, and negative MYC/MYCN FISH. (NCT02724579a chunk 2)
   - **Radiation:** **CSI 18 Gy** plus tumor-bed boost **36 Gy** (total 54 Gy). (NCT02724579a chunk 1)
   - **Chemo:** reduced-intensity maintenance regimens; notably omits vincristine during RT and uses alternating blocks including cisplatin/lomustine/vincristine and cyclophosphamide/vincristine. (NCT02724579a chunk 1)
   - **Endpoints:** PFS (up to 10 years), real-time DNA methylation profiling, longitudinal neurocognitive and QoL outcomes, and toxicity endpoints (audiology/endocrine/neuropathy). (NCT02724579a chunk 1)
   - URL: https://clinicaltrials.gov/study/NCT02724579

2. **SIOP PNET5 — NCT02066220** (start 2014; status ACTIVE_NOT_RECRUITING)
   - **WNT low-risk arm:** **CSI 18.0 Gy** and 54 Gy primary tumor RT, followed by reduced-intensity maintenance chemo (alternating cisplatin/CCNU/vincristine and cyclophosphamide/vincristine). (NCT02066220 chunk 1)
   - URL: https://clinicaltrials.gov/study/NCT02066220

3. **St. Jude SJMB12 — NCT01878617** (start 2013; status ACTIVE_NOT_RECRUITING)
   - Risk- and molecularly directed trial with a WNT stratum receiving **reduced-dose CSI** and reduced-dose cyclophosphamide; primary objective includes PFS estimation versus historical controls. (NCT01878617 chunk 1)
   - URL: https://clinicaltrials.gov/study/NCT01878617

4. **FOR-WNT2 — NCT04474964** (start 2020; status RECRUITING)
   - **Population:** children >3 and <16; WNT-pathway medulloblastoma; M0; residual <1.5 cm²; start within 6 weeks of surgery. (NCT04474964a chunk 2)
   - **Radiation:** **CSI 18 Gy/10 fractions** + tumor-bed boost **36 Gy/20 fractions** (total 54 Gy/30 fractions) without concurrent chemotherapy. (NCT04474964 chunk 1)
   - **Chemo:** 6 cycles alternating adjuvant chemotherapy (per study CET protocol). (NCT04474964 chunk 1)
   - **Endpoints:** 5-year relapse-free survival and overall survival; secondary endpoints include neurocognitive, endocrine, and hearing outcomes. (NCT04474964 chunk 1)
   - URL: https://clinicaltrials.gov/study/NCT04474964

### Real-world outcome data informing de-escalation
Relapse in WNT-MB is influenced by maintenance chemotherapy intensity; in a 93-patient cohort, higher cumulative cyclophosphamide/ifosfamide exposure correlated with fewer relapses, implying that safe radiotherapy reduction must be co-designed with adequate systemic therapy. (nobre2020patternofrelapse pages 1-3)

---

## 10. Prevention

### Primary prevention
No established primary prevention strategies exist for sporadic WNT-MB based on the retrieved evidence.

### Secondary prevention / screening
For hereditary predisposition (APC/FAP/Turcot-associated WNT-MB), the actionable prevention-oriented steps in this context are:
- **Genetic counseling and germline APC testing** when WNT-MB is CTNNB1-wildtype (and/or in the presence of family history consistent with FAP). (moreno2023highfrequencyof pages 2-3)

---

## 11. Other Species / Natural Disease and Model Organisms

### Genetically engineered mouse models (GEMMs)
WNT-MB GEMMs typically require **stabilized Ctnnb1 (exon-3) activation plus cooperating lesions**; Ctnnb1 activation alone is insufficient in some systems.
- A cited GEMM: **Blbp-Cre; Ctnnb1lox(ex3); Trp53flox/+** produces WNT medulloblastoma with ~15% penetrance and ~290-day latency; adding **Pik3caE545K** increases penetrance and shortens latency (reported as 100% penetrance within ~3 months in one summary). (nor2018clinicalandpreclinical pages 20-24, manfreda2023wntsignalingin pages 11-12)

### Patient-derived xenografts (PDX) and translational resources
PDX repositories include medulloblastoma lines characterized by integrated genomics, though available PDX collections can be biased toward Group 3/MYC-amplified tumors; nonetheless, PDX systems remain a key translational platform for subgroup-specific therapy testing. (nor2018clinicalandpreclinical pages 16-20)

### Practical model-selection considerations (2024 perspective)
A 2024 ITCC-P4 framework emphasizes using multiple in vivo models (xenografts and/or transgenic models), orthotopic designs when possible, and reporting PK/PD plus biomarker-linked endpoints to support clinical translation—principles directly applicable to WNT-MB preclinical work. (gopisetty2024itccp4molecularcharacterization pages 70-72)

---

## 12. Summary Artifact (quick reference)

| Domain | Key finding | Specific details | Key citations |
|---|---|---|---|
| Definition / entity | WNT-activated medulloblastoma is a molecularly defined WHO medulloblastoma subgroup with canonical WNT/β-catenin pathway activation | Represents a distinct molecular subgroup recognized in modern WHO CNS classification; often associated with classic histology and favorable-risk biology; integrated diagnosis relies on molecular features rather than histology alone | (mani2024clinicoradiologicaloutcomesin pages 1-2, rechberger2023exploringthemolecular pages 1-2) |
| Core diagnostic markers | Nuclear β-catenin and CTNNB1 alteration are core diagnostic clues | Pathognomonic/characteristic nuclear β-catenin immunostaining is widely used; most tumors harbor CTNNB1 exon 3 hotspot mutations that stabilize β-catenin; methylation profiling can support subgroup assignment in equivocal cases | (moreno2023highfrequencyof pages 2-3, green2024wnt‐activatedmyc‐amplifiedmedulloblastoma pages 2-3, jackson2023recentadvancesin pages 1-2) |
| Molecular alteration | CTNNB1 exon 3 mutation | Reported in ~85–90% of WNT tumors; exon 3 mutations impair β-catenin phosphorylation/degradation, causing nuclear accumulation and WNT pathway activation | (moreno2023highfrequencyof pages 2-3, ntenti2023clinicalhistologicaland pages 4-5, shcherbina2023comparativeanalysisof pages 2-4) |
| Molecular alteration | APC germline variants in CTNNB1-wild-type WNT medulloblastoma | Roughly 10–15% of WNT tumors are CTNNB1-wild-type and many of these are associated with germline APC pathogenic variants/FAP-Turcot syndrome; germline APC testing is recommended in CTNNB1-wild-type cases | (moreno2023highfrequencyof pages 2-3, moreno2023highfrequencyof pages 1-2) |
| Molecular alteration | Monosomy 6 | A hallmark copy-number feature, especially common in pediatric WNT-α; frequency is often >85% in WNT-α and lower in WNT-β/adult cases; useful supportive CNV marker but not universal | (mani2024clinicoradiologicaloutcomesin pages 10-11, slika2023theneurodevelopmentaland pages 2-4, shcherbina2023comparativeanalysisof pages 2-4) |
| Molecular alteration | DDX3X alteration | Recurrently altered in WNT medulloblastoma; reported frequency around ~50% in some summaries/cohorts; included among candidate driver genes | (shcherbina2023comparativeanalysisof pages 2-4, slika2023theneurodevelopmentaland pages 2-4) |
| Molecular alteration | SMARCA4 alteration | Recurrent but less common than CTNNB1/DDX3X; reported around ~26% in one review summary and included among recurrent WNT-associated drivers | (shcherbina2023comparativeanalysisof pages 2-4, slika2023theneurodevelopmentaland pages 2-4) |
| Epidemiology | Share of all medulloblastoma | Usually ~10% of all medulloblastomas; one Latin-Iberian cohort reported 15% (40/266), illustrating population variability | (moreno2023highfrequencyof pages 2-3, mani2024clinicoradiologicaloutcomesin pages 1-2, moreno2023highfrequencyof pages 1-2) |
| Epidemiology | Age distribution / peak | Typically affects older children and adolescents; median age ~10–12 years (reported median 11–12 in several sources); rare in infants; adult WNT cases occur but are less common and may align with WNT-β biology | (shcherbina2023comparativeanalysisof pages 2-4, mani2024clinicoradiologicaloutcomesin pages 1-2, slika2023theneurodevelopmentaland pages 2-4) |
| Epidemiology | Sex distribution | Often described as near-equal sex distribution overall, though individual institutional cohorts may show male predominance | (shcherbina2023comparativeanalysisof pages 2-4, slika2023theneurodevelopmentaland pages 2-4, mani2024clinicoradiologicaloutcomesin pages 1-2) |
| Prognosis | Overall prognostic category | Best-prognosis medulloblastoma subgroup under standard multimodality therapy, with 5-year survival generally >90% in pediatric series | (moreno2023highfrequencyof pages 2-3, upadhyay2024riskstratifiedradiotherapyin pages 4-5, slika2023theneurodevelopmentaland pages 7-8) |
| Prognosis statistic | Single-center 2024 WNT cohort | Median follow-up 72 months; 5-year PFS 87.7% and 5-year OS 91.2% in 61 evaluable molecularly confirmed WNT cases treated with surgery + risk-stratified radio(chemo)therapy | (mani2024clinicoradiologicaloutcomesin pages 1-2) |
| Prognosis statistic | International relapse-pattern cohort | In 93 molecularly confirmed WNT cases, 5-year PFS was 0.84 (84%); 15 relapses occurred, underscoring that prognosis is excellent but relapse is not negligible | (nobre2020patternofrelapse pages 1-3) |
| Prognosis statistic | Published molecularly informed trials/cohorts summarized in 2024 review | Reported examples include HIT2000 nonmetastatic WNT 5-year EFS/OS 100%/100%, SJMB-03 100%/100%, SIOP PNET-4 ~91%/95%, and COG ACNS0331 ~93.3%/95.5% | (mani2024clinicoradiologicaloutcomesin pages 11-12) |
| Relapse pattern | Frequency and distribution | Relapse is uncommon but clinically important; most relapses in the international cohort were metastatic (12/15), with a distinctive tendency for lateral ventricular involvement (8/12 metastatic relapses) rather than only posterior fossa recurrence | (nobre2020patternofrelapse pages 1-3) |
| Relapse pattern | Timing / salvage | Relapse can be early or very late; post-relapse outcomes are generally poor with limited salvage potential despite the favorable frontline prognosis | (mani2024clinicoradiologicaloutcomesin pages 10-11, nobre2020patternofrelapse pages 1-3) |
| Treatment de-escalation relevance | Why this subgroup is targeted for de-intensification | Excellent frontline survival and concern for late neurocognitive/endocrine/ototoxic effects have motivated reduced-CSI trials, but complete omission of CSI proved unsafe in early pilot efforts | (upadhyay2024riskstratifiedradiotherapyin pages 4-5, mani2023wntpathwaymedulloblastomawhat pages 1-2, mani2024clinicoradiologicaloutcomesin pages 11-12) |


*Table: This table condenses the core disease-defining, molecular, epidemiologic, prognostic, and relapse-pattern features of WNT-activated medulloblastoma. It is useful as a quick reference for building a structured disease knowledge base entry with supporting citations.*

---

## 13. Expert synthesis / current understanding (2023–2024 emphasis)

1. **Molecular definition is central**: WNT-MB is best defined by CTNNB1/APC-driven canonical WNT activation with nuclear β-catenin; methylation profiling is increasingly integrated into real-world diagnostics for confirmation and CNV support. (moreno2023highfrequencyof pages 2-3, green2024wnt‐activatedmyc‐amplifiedmedulloblastoma pages 2-3, wolff2024implementationofmethylation pages 5-8)
2. **De-escalation is active but constrained**: evidence and expert reviews highlight that **CSI dose reduction** (15–18 Gy) is being tested in carefully defined low-risk WNT populations, but **complete omission of CSI** has led to rapid relapses in pilot efforts, reinforcing CSI as a necessary curative component. (upadhyay2024riskstratifiedradiotherapyin pages 4-5, mani2023wntpathwaymedulloblastomawhat pages 1-2)
3. **Relapse biology matters**: despite excellent prognosis, relapse—often metastatic with lateral-ventricle predilection—occurs and has poor salvage outcomes; chemotherapy regimen intensity appears to be a key modifiable factor in relapse risk, shaping trial design. (nobre2020patternofrelapse pages 1-3)

---

## References (URLs and publication timing for key cited sources)
- Moreno et al. *Frontiers in Oncology* (Sep 2023). “High frequency of WNT-activated medulloblastomas with CTNNB1 wild type…” https://doi.org/10.3389/fonc.2023.1237170 (moreno2023highfrequencyof pages 2-3)
- Mani et al. *Diagnostics* (Feb 2024). “Clinico-Radiological Outcomes in WNT-Subgroup Medulloblastoma” https://doi.org/10.3390/diagnostics14040358 (mani2024clinicoradiologicaloutcomesin pages 1-2)
- Nobre et al. *Cell Reports Medicine* (Jun 2020). “Pattern of Relapse and Treatment Response in WNT-Activated Medulloblastoma” https://doi.org/10.1016/j.xcrm.2020.100038 (nobre2020patternofrelapse pages 1-3)
- Upadhyay & Paulino. *Cancers* (Oct 2024). “Risk-Stratified Radiotherapy in Pediatric Cancer” https://doi.org/10.3390/cancers16203530 (upadhyay2024riskstratifiedradiotherapyin pages 4-5)
- Wolff et al. preprint (Nov 2024). “Implementation of methylation profiling…” https://doi.org/10.21203/rs.3.rs-5332503/v1 (wolff2024implementationofmethylation pages 5-8)
- ClinicalTrials.gov: NCT02724579, NCT02066220, NCT01878617, NCT04474964 (NCT02724579a chunk 1, NCT02066220 chunk 1, NCT01878617 chunk 1, NCT04474964 chunk 1)


References

1. (moreno2023highfrequencyof pages 2-3): Daniel Antunes Moreno, Murilo Bonatelli, Augusto Perazzolo Antoniazzi, Flávia Escremim de Paula, Leticia Ferro Leal, Felipe Antônio de Oliveira Garcia, André Escremim de Paula, Gustavo Ramos Teixeira, Iara Viana Vidigal Santana, Fabiano Saggioro, Luciano Neder, Elvis Terci Valera, Carlos Alberto Scrideli, João Stavale, Suzana Maria Fleury Malheiros, Matheus Lima, Glaucia Noeli Maroso Hajj, Hernan Garcia-Rivello, Silvia Christiansen, Susana Nunes, Maria João Gil-da-Costa, Jorge Pinheiro, Flavia Delgado Martins, Carlos Almeida Junior, Bruna Minniti Mançano, and Rui Manuel Reis. High frequency of wnt-activated medulloblastomas with ctnnb1 wild type suggests a higher proportion of hereditary cases in a latin-iberian population. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1237170, doi:10.3389/fonc.2023.1237170. This article has 9 citations.

2. (shcherbina2023comparativeanalysisof pages 2-4): Valeriia Shcherbina, Larysa Kovalevska, Eugene Pedachenko, Tetyana Malysheva, and Elena Kashuba. Comparative analysis of the embryonal brain tumors based on their molecular features. Discovery medicine, 35 178:733-749, Oct 2023. URL: https://doi.org/10.24976/discov.med.202335178.69, doi:10.24976/discov.med.202335178.69. This article has 6 citations and is from a peer-reviewed journal.

3. (jackson2023recentadvancesin pages 1-2): Kasey Jackson and Roger J. Packer. Recent advances in pediatric medulloblastoma. Current Neurology and Neuroscience Reports, 23:841-848, Nov 2023. URL: https://doi.org/10.1007/s11910-023-01316-9, doi:10.1007/s11910-023-01316-9. This article has 41 citations and is from a domain leading peer-reviewed journal.

4. (rechberger2023exploringthemolecular pages 1-2): Julian S. Rechberger, Stephanie A. Toll, Wouter J. F. Vanbilloen, David J. Daniels, and Soumen Khatua. Exploring the molecular complexity of medulloblastoma: implications for diagnosis and treatment. Diagnostics, 13:2398, Jul 2023. URL: https://doi.org/10.3390/diagnostics13142398, doi:10.3390/diagnostics13142398. This article has 20 citations.

5. (mani2024clinicoradiologicaloutcomesin pages 1-2): Shakthivel Mani, Abhishek Chatterjee, Archya Dasgupta, Neelam Shirsat, Akash Pawar, Sridhar Epari, Ayushi Sahay, Arpita Sahu, Aliasgar Moiyadi, Maya Prasad, Girish Chinnaswamy, and Tejpal Gupta. Clinico-radiological outcomes in wnt-subgroup medulloblastoma. Diagnostics, 14:358, Feb 2024. URL: https://doi.org/10.3390/diagnostics14040358, doi:10.3390/diagnostics14040358. This article has 5 citations.

6. (mani2023wntpathwaymedulloblastomawhat pages 2-4): Shakthivel Mani, Abhishek Chatterjee, Archya Dasgupta, Neelam Shirsat, Sridhar Epari, Girish Chinnaswamy, and Tejpal Gupta. Wnt-pathway medulloblastoma: what constitutes low-risk and how low can one go? Oncotarget, 14:105-110, Feb 2023. URL: https://doi.org/10.18632/oncotarget.28360, doi:10.18632/oncotarget.28360. This article has 10 citations.

7. (NCT02724579a chunk 1):  Reduced Craniospinal Radiation Therapy and Chemotherapy in Treating Younger Patients With Newly Diagnosed WNT-Driven Medulloblastoma. Children's Oncology Group. 2017. ClinicalTrials.gov Identifier: NCT02724579

8. (nobre2020patternofrelapse pages 1-3): Liana Nobre, Michal Zapotocky, Sara Khan, Kohei Fukuoka, Adriana Fonseca, Tara McKeown, David Sumerauer, Ales Vicha, Wieslawa A. Grajkowska, Joanna Trubicka, Kay Ka Wai Li, Ho-Keung Ng, Luca Massimi, Ji Yeoun Lee, Seung-Ki Kim, Shayna Zelcer, Alexandre Vasiljevic, Cécile Faure-Conter, Peter Hauser, Boleslaw Lach, Marie-Lise van Veelen-Vincent, Pim J. French, Erwin G. Van Meir, William A. Weiss, Nalin Gupta, Ian F. Pollack, Ronald L. Hamilton, Amulya A. Nageswara Rao, Caterina Giannini, Joshua B. Rubin, Andrew S. Moore, Lola B. Chambless, Rajeev Vibhakar, Young Shin Ra, Maura Massimino, Roger E. McLendon, Helen Wheeler, Massimo Zollo, Veronica Ferruci, Toshihiro Kumabe, Claudia C. Faria, Jaroslav Sterba, Shin Jung, Enrique López-Aguilar, Jaume Mora, Carlos G. Carlotti, James M. Olson, Sarah Leary, Jason Cain, Lenka Krskova, Josef Zamecnik, Cynthia E. Hawkins, Uri Tabori, Annie Huang, Ute Bartels, Paul A. Northcott, Michael D. Taylor, Stephen Yip, Jordan R. Hansford, Eric Bouffet, and Vijay Ramaswamy. Pattern of relapse and treatment response in wnt-activated medulloblastoma. Cell Reports Medicine, 1:100038, Jun 2020. URL: https://doi.org/10.1016/j.xcrm.2020.100038, doi:10.1016/j.xcrm.2020.100038. This article has 52 citations and is from a peer-reviewed journal.

9. (ntenti2023clinicalhistologicaland pages 4-5): Charikleia Ntenti, Konstantinos Lallas, and Georgios Papazisis. Clinical, histological, and molecular prognostic factors in childhood medulloblastoma: where do we stand? Diagnostics, 13:1915, May 2023. URL: https://doi.org/10.3390/diagnostics13111915, doi:10.3390/diagnostics13111915. This article has 9 citations.

10. (moreno2023highfrequencyof pages 1-2): Daniel Antunes Moreno, Murilo Bonatelli, Augusto Perazzolo Antoniazzi, Flávia Escremim de Paula, Leticia Ferro Leal, Felipe Antônio de Oliveira Garcia, André Escremim de Paula, Gustavo Ramos Teixeira, Iara Viana Vidigal Santana, Fabiano Saggioro, Luciano Neder, Elvis Terci Valera, Carlos Alberto Scrideli, João Stavale, Suzana Maria Fleury Malheiros, Matheus Lima, Glaucia Noeli Maroso Hajj, Hernan Garcia-Rivello, Silvia Christiansen, Susana Nunes, Maria João Gil-da-Costa, Jorge Pinheiro, Flavia Delgado Martins, Carlos Almeida Junior, Bruna Minniti Mançano, and Rui Manuel Reis. High frequency of wnt-activated medulloblastomas with ctnnb1 wild type suggests a higher proportion of hereditary cases in a latin-iberian population. Frontiers in Oncology, Sep 2023. URL: https://doi.org/10.3389/fonc.2023.1237170, doi:10.3389/fonc.2023.1237170. This article has 9 citations.

11. (mani2024clinicoradiologicaloutcomesin pages 10-11): Shakthivel Mani, Abhishek Chatterjee, Archya Dasgupta, Neelam Shirsat, Akash Pawar, Sridhar Epari, Ayushi Sahay, Arpita Sahu, Aliasgar Moiyadi, Maya Prasad, Girish Chinnaswamy, and Tejpal Gupta. Clinico-radiological outcomes in wnt-subgroup medulloblastoma. Diagnostics, 14:358, Feb 2024. URL: https://doi.org/10.3390/diagnostics14040358, doi:10.3390/diagnostics14040358. This article has 5 citations.

12. (slika2023theneurodevelopmentaland pages 7-8): Hasan Slika, Paolo Alimonti, Divyaansh Raj, Chad Caraway, Safwan Alomari, Eric M. Jackson, and Betty Tyler. The neurodevelopmental and molecular landscape of medulloblastoma subgroups: current targets and the potential for combined therapies. Cancers, 15:3889, Jul 2023. URL: https://doi.org/10.3390/cancers15153889, doi:10.3390/cancers15153889. This article has 25 citations.

13. (mani2024clinicoradiologicaloutcomesin pages 11-12): Shakthivel Mani, Abhishek Chatterjee, Archya Dasgupta, Neelam Shirsat, Akash Pawar, Sridhar Epari, Ayushi Sahay, Arpita Sahu, Aliasgar Moiyadi, Maya Prasad, Girish Chinnaswamy, and Tejpal Gupta. Clinico-radiological outcomes in wnt-subgroup medulloblastoma. Diagnostics, 14:358, Feb 2024. URL: https://doi.org/10.3390/diagnostics14040358, doi:10.3390/diagnostics14040358. This article has 5 citations.

14. (slika2023theneurodevelopmentaland pages 2-4): Hasan Slika, Paolo Alimonti, Divyaansh Raj, Chad Caraway, Safwan Alomari, Eric M. Jackson, and Betty Tyler. The neurodevelopmental and molecular landscape of medulloblastoma subgroups: current targets and the potential for combined therapies. Cancers, 15:3889, Jul 2023. URL: https://doi.org/10.3390/cancers15153889, doi:10.3390/cancers15153889. This article has 25 citations.

15. (green2024wnt‐activatedmyc‐amplifiedmedulloblastoma pages 2-3): Sage Green, Travis Hoover, David Doss, Kimberly A Davidow, Andrew W. Walter, Catherine E. Cottrell, and Sidharth Mahapatra. Wnt‐activated, <i>myc</i>‐amplified medulloblastoma displaying intratumoural heterogeneity. Neuropathology and Applied Neurobiology, Jan 2024. URL: https://doi.org/10.1111/nan.12945, doi:10.1111/nan.12945. This article has 6 citations and is from a peer-reviewed journal.

16. (wolff2024implementationofmethylation pages 5-8): Beatriz Martins Wolff, Yuri Casal, Lucas Liro Vieira, Gleyson Francisco Silva Carvalho, Mariana Ribeiro Costa-Siemann, Rafaela da Silva Mendes, Maria Fernanda Freire Chagas, Lissandro Rolim, Yanca Gasparini, Eder Alencar Moura, Felipe D Almeida Costa, and Leslie Domenici Kulikowski. Implementation of methylation profiling of central nervous system tumors at largest public health center in brazil. Nov 2024. URL: https://doi.org/10.21203/rs.3.rs-5332503/v1, doi:10.21203/rs.3.rs-5332503/v1.

17. (manfreda2023wntsignalingin pages 11-12): Lorenzo Manfreda, Elena Rampazzo, and Luca Persano. Wnt signaling in brain tumors: a challenging therapeutic target. Biology, 12:729, May 2023. URL: https://doi.org/10.3390/biology12050729, doi:10.3390/biology12050729. This article has 20 citations.

18. (nor2018clinicalandpreclinical pages 20-24): Carolina Nör and Vijay Ramaswamy. Clinical and pre-clinical utility of genomics in medulloblastoma. Expert Review of Neurotherapeutics, 18:633-647, Jul 2018. URL: https://doi.org/10.1080/14737175.2018.1503536, doi:10.1080/14737175.2018.1503536. This article has 17 citations and is from a peer-reviewed journal.

19. (upadhyay2024riskstratifiedradiotherapyin pages 4-5): Rituraj Upadhyay and Arnold C. Paulino. Risk-stratified radiotherapy in pediatric cancer. Cancers, 16:3530, Oct 2024. URL: https://doi.org/10.3390/cancers16203530, doi:10.3390/cancers16203530. This article has 2 citations.

20. (NCT02724579a chunk 2):  Reduced Craniospinal Radiation Therapy and Chemotherapy in Treating Younger Patients With Newly Diagnosed WNT-Driven Medulloblastoma. Children's Oncology Group. 2017. ClinicalTrials.gov Identifier: NCT02724579

21. (mani2023wntpathwaymedulloblastomawhat pages 1-2): Shakthivel Mani, Abhishek Chatterjee, Archya Dasgupta, Neelam Shirsat, Sridhar Epari, Girish Chinnaswamy, and Tejpal Gupta. Wnt-pathway medulloblastoma: what constitutes low-risk and how low can one go? Oncotarget, 14:105-110, Feb 2023. URL: https://doi.org/10.18632/oncotarget.28360, doi:10.18632/oncotarget.28360. This article has 10 citations.

22. (NCT02066220 chunk 1):  International Society of Paediatric Oncology (SIOP) PNET 5 Medulloblastoma. Universitätsklinikum Hamburg-Eppendorf. 2014. ClinicalTrials.gov Identifier: NCT02066220

23. (NCT01878617 chunk 1):  A Clinical and Molecular Risk-Directed Therapy for Newly Diagnosed Medulloblastoma. St. Jude Children's Research Hospital. 2013. ClinicalTrials.gov Identifier: NCT01878617

24. (NCT04474964a chunk 2):  Focal Radiotherapy Plus Low Dose Craniospinal Irradiation Followed by Adjuvant Chemotherapy in WNT Medulloblastoma.. Tata Memorial Centre. 2020. ClinicalTrials.gov Identifier: NCT04474964

25. (NCT04474964 chunk 1):  Focal Radiotherapy Plus Low Dose Craniospinal Irradiation Followed by Adjuvant Chemotherapy in WNT Medulloblastoma.. Tata Memorial Centre. 2020. ClinicalTrials.gov Identifier: NCT04474964

26. (nor2018clinicalandpreclinical pages 16-20): Carolina Nör and Vijay Ramaswamy. Clinical and pre-clinical utility of genomics in medulloblastoma. Expert Review of Neurotherapeutics, 18:633-647, Jul 2018. URL: https://doi.org/10.1080/14737175.2018.1503536, doi:10.1080/14737175.2018.1503536. This article has 17 citations and is from a peer-reviewed journal.

27. (gopisetty2024itccp4molecularcharacterization pages 70-72): Apurva Gopisetty. Itcc-p4: molecular characterization and multi-omics analysis of pediatric patient tumor and patient-derived xenograft (pdx) models for preclinical model selection. Text, Jan 2024. URL: https://doi.org/10.11588/heidok.00034239, doi:10.11588/heidok.00034239. This article has 1 citations and is from a peer-reviewed journal.

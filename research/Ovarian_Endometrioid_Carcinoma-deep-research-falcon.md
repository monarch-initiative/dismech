---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-19T09:25:37.865206'
end_time: '2026-06-19T09:40:01.716041'
duration_seconds: 863.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ovarian Endometrioid Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Ovarian_Endometrioid_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Ovarian_Endometrioid_Carcinoma-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ovarian Endometrioid Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ovarian Endometrioid Carcinoma** covering all of the
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
- **Disease Name:** Ovarian Endometrioid Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ovarian Endometrioid Carcinoma** covering all of the
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


# Comprehensive Research Report: Ovarian Endometrioid Carcinoma

## Disease Information

**Disease Name:** Ovarian Endometrioid Carcinoma (OEC)

**Category:** Epithelial ovarian cancer, gynecologic malignancy

### Definition and Classification

Ovarian endometrioid carcinoma is a distinct histologic subtype of epithelial ovarian cancer that accounts for approximately 10% of all ovarian carcinomas (yoshida2025molecularpathologyof pages 1-3). According to the 2020 World Health Organization (WHO) classification, OEC is defined as a carcinoma resembling endometrioid carcinoma of the uterine corpus, characterized by tubular glands resembling proliferative endometrial epithelium (yoshida2025molecularpathologyof pages 1-3, leo2021whatisnew pages 1-2). The WHO Classification of Female Genital Tumours (5th edition, 2020) recognizes OEC as one of five principal histotypes of ovarian carcinoma, alongside high-grade serous, low-grade serous, clear cell, and mucinous carcinomas (leo2021whatisnew pages 1-2, kobel2022theevolutionof pages 1-3).

OEC exhibits broad morphological diversity, often including glandular, solid, squamous, or sertoliform patterns, which can lead to diagnostic confusion with other primary ovarian neoplasms or metastatic tumors (yoshida2025molecularpathologyof pages 1-3). While earlier studies reported higher frequencies of OEC, this discrepancy likely reflects historical misclassification, particularly of SET (Solid, pseudo-Endometrioid, and Transitional cell-like)-pattern high-grade serous carcinomas as high-grade OECs (yoshida2025molecularpathologyof pages 1-3).

### Common Synonyms
- Endometrioid ovarian carcinoma
- Ovarian endometrioid adenocarcinoma
- Endometriosis-associated ovarian cancer (when arising from endometriosis, shared with clear cell carcinoma)

### Key Identifiers
While specific OMIM, Orphanet, or MONDO identifiers were not detailed in the reviewed literature, OEC is classified under ICD-O morphology codes for endometrioid carcinoma and is part of the broader category of epithelial ovarian neoplasms.

---

## Epidemiology and Population Demographics

### Global Incidence and Prevalence

Globally, an estimated **29,319 new patients of endometrioid cancer** were identified in 2020 among all ovarian cancer cases (wang2024globalincidenceof pages 1-2). This represents approximately 9.5-10% of all epithelial ovarian carcinomas worldwide (yoshida2025molecularpathologyof pages 1-3, wang2024globalincidenceof pages 1-2).

The distribution of ovarian cancer histologic subtypes exhibits regional variation. Northern Africa and Eastern Asia show the highest burden of endometrioid carcinomas, contrasting with high-grade serous carcinomas which predominate in Eastern Europe (wang2024globalincidenceof pages 1-2). Recent studies employing refined pathological classification consistently report the frequency of OEC as around 10%, with no significant difference between Western and Asian populations, unlike ovarian clear cell carcinoma which is more prevalent among Asian women (yoshida2025molecularpathologyof pages 1-3).

In the United States, during 1992-2019, endometrioid ovarian cancer incidence showed differential trends by race/ethnicity. Endometrioid cancer incidence decreased in non-Hispanic White women (AAPC during 2010-2019 = -1.3; 95% CI, -1.9 to -0.8) but increased in Hispanic women (AAPC = 3.6; 95% CI, 1.0 to 6.3) (phung2023trendsofovarian pages 1-2).

### Age Distribution

In Japan, OEC is increasingly diagnosed in younger women (<50 years) and in early-stage disease (yoshida2025molecularpathologyof pages 1-3). This trend may reflect rising prevalence of endometriosis, increased lifetime menstrual cycles due to declining fertility, delayed marriage, earlier menarche, and later menopause, as well as growing prevalence of obesity (yoshida2025molecularpathologyof pages 1-3). These factors are thought to be influenced by recent societal and lifestyle changes that impact reproductive and hormonal health.

### Sex Ratio
Ovarian endometrioid carcinoma, like all ovarian cancers, affects exclusively or overwhelmingly female patients, as it arises from ovarian or endometriotic tissue.

---

## Etiology

### Disease Causal Factors

#### Endometriosis as Precursor
Endometriosis is a well-established risk factor and potential precursor for OEC, conferring a **two- to threefold increase in risk**, a feature shared with ovarian clear cell carcinoma (yoshida2025molecularpathologyof pages 1-3). Histological evidence of endometriosis is observed in approximately **40% of resected OEC specimens** (yoshida2025molecularpathologyof pages 1-3). The presence of shared somatic mutations between endometriotic lesions and OEC—such as ARID1A loss-of-function and PIK3CA gain-of-function mutations—supports the hypothesis that OEC may arise from endometriosis through stepwise malignant transformation (yoshida2025molecularpathologyof pages 1-3).

Endometriosis affects 10-18% of reproductive-aged women and is associated with a 2-3% lifetime risk of ovarian cancer, exceeding that of the general female population (yoshida2025molecularpathologyof pages 1-3). Notably, even morphologically benign endometriotic lesions harbor oncogenic mutations (e.g., ARID1A, PIK3CA, KRAS, PTEN, TP53), indicating their potential as precursors to malignancy (yoshida2025molecularpathologyof pages 1-3).

### Risk Factors

**Genetic Risk Factors:**
- **Lynch Syndrome:** OEC is enriched for Lynch syndrome-associated tumors. Among mismatch repair-deficient (MMRd) ovarian endometrioid carcinomas, approximately 9.5% are associated with Lynch syndrome, supporting routine MMR testing (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3).
- **BRCA1/2 Mutations:** BRCA1 mutation carriers show increased risks for endometrioid EC (SIR = 2.63, 95% CI: 1.80-3.83; HR = 2.01, 95% CI: 1.18-3.45), although the association is stronger for serous-like tumors (ali2023epidemiologyandrisk pages 1-2).

**Environmental/Lifestyle Risk Factors:**
- **Obesity:** 1.2-fold increase in risk per 5 kg/m² increase in body mass index (BMI) (yoshida2025molecularpathologyof pages 1-3)
- **Hormone Replacement Therapy (HRT):** Relative risk ~1.3-1.4 (yoshida2025molecularpathologyof pages 1-3, ali2023epidemiologyandrisk pages 1-2)
- **Elevated Estrogen Exposure:** Greater number of lifetime menstrual cycles associated with increased risk (yoshida2025molecularpathologyof pages 1-3)
- **Nulliparity:** Nulliparous women have higher risk (ali2023epidemiologyandrisk pages 1-2)

OEC shows stronger associations with family history of ovarian cancer and higher BMI, features not typically observed in clear cell carcinoma despite both subtypes' association with endometriosis (yoshida2025molecularpathologyof pages 1-3).

### Protective Factors

**Reproductive Factors:**
- **Parity:** Each birth reduces risk by approximately 10% (yoshida2025molecularpathologyof pages 1-3)
- **Oral Contraceptive Use:** 15-20% risk reduction with five years of use (yoshida2025molecularpathologyof pages 1-3)

**Surgical Interventions:**
- **Tubal Ligation and Salpingectomy:** Appear protective, possibly by reducing retrograde menstruation (yoshida2025molecularpathologyof pages 1-3)

**Tobacco:**
- **Smoking:** Interestingly, unlike other ovarian cancer subtypes, smoking was correlated with a **lower risk** for OEC (relative risk ~0.8) (yoshida2025molecularpathologyof pages 1-3)

---

## Genetic and Molecular Information

### Causal Genes and Pathogenic Variants

| Pathway / Function Group | Gene / Pathway | Type of Alteration in Ovarian Endometrioid Carcinoma | Frequency / Enrichment | Functional Impact | Clinical Significance | Associated Molecular Subtype |
|---|---|---|---|---|---|---|
| Chromatin remodeling | **ARID1A** | Predominantly loss-of-function alterations; often reflected by loss of protein expression | Recurrent/frequent; shared with endometriosis-associated tumors and often co-occurs with **PIK3CA** alterations (leo2021whatisnew pages 1-2, yoshida2025molecularpathologyof pages 1-3) | Disrupts SWI/SNF chromatin remodeling, altering transcriptional control and differentiation programs | Supports endometriosis-associated pathogenesis; candidate biomarker for synthetic-lethality and epigenetic strategies; useful in molecular profiling (yoshida2025molecularpathologyof pages 1-3) | Most often **NSMP** or **MMRd** backgrounds; can occur across subtypes |
| PI3K/AKT/mTOR signaling | **PIK3CA** | Activating/gain-of-function mutation | Recurrent/frequent; commonly co-occurs with **ARID1A** and present in endometriosis-related precursor lesions (yoshida2025molecularpathologyof pages 1-3) | Activates PI3K/AKT/mTOR signaling, promoting proliferation, survival, metabolism, and therapy resistance | Suggests actionable pathway dependence; rationale for PI3K/AKT/mTOR-targeted therapy development (yoshida2025molecularpathologyof pages 1-3) | Most often **NSMP**; also seen in **MMRd** tumors |
| PI3K/AKT/mTOR signaling | **PTEN** | Inactivating mutation/loss of function; sometimes loss of expression | Recurrent/frequent in OEC; highlighted as characteristic of endometrioid tumors (leo2021whatisnew pages 1-2, yoshida2025molecularpathologyof pages 1-3) | Releases inhibition of PI3K signaling, increasing AKT/mTOR pathway activation | Supports endometriosis-to-carcinoma progression model; may inform targeted pathway inhibition strategies (yoshida2025molecularpathologyof pages 1-3) | Most often **NSMP**; also present in **MMRd** |
| Wnt / cell fate | **CTNNB1** | Activating mutation / β-catenin pathway alteration | Characteristic/recurrent in OEC (leo2021whatisnew pages 1-2, yoshida2025molecularpathologyof pages 1-3) | Activates Wnt/β-catenin signaling, affecting epithelial differentiation, proliferation, and glandular/squamous morphology | Helpful lineage-defining alteration for endometrioid histotype; may aid distinction from other ovarian carcinoma types (leo2021whatisnew pages 1-2) | Most commonly **NSMP** |
| MAPK signaling | **KRAS** | Activating mutation | Less common than PTEN/PIK3CA/CTNNB1 but recurrent; also seen in benign endometriotic lesions (yoshida2025molecularpathologyof pages 1-3) | Activates MAPK signaling, supporting growth and clonal evolution from precursor lesions | Supports precursor-lesion model and molecular heterogeneity; potential entry point for pathway-based trials in selected tumors | Usually **NSMP** |
| DNA mismatch repair | **MLH1** | Loss of protein expression from mutation or promoter hypermethylation | Present in the **MMRd** subset; sporadic cases often involve promoter hypermethylation (yoshida2025molecularpathologyof pages 1-3) | Causes mismatch-repair deficiency, hypermutation, and microsatellite instability | Important for Lynch syndrome triage when unmethylated; predicts eligibility/relevance for immune checkpoint blockade in MMRd disease (yoshida2025molecularpathologyof pages 1-3) | **MMRd** |
| DNA mismatch repair | **MSH2** | Loss-of-function germline or somatic alteration with loss of protein expression | Enriched in Lynch-associated OEC within the MMRd subset (yoshida2025molecularpathologyof pages 1-3) | Defective mismatch repair leading to MSI and increased neoantigen load | Strong Lynch syndrome implication; triggers genetic counseling and germline testing; may predict immunotherapy sensitivity (yoshida2025molecularpathologyof pages 1-3) | **MMRd** |
| DNA mismatch repair | **MSH6** | Loss-of-function germline or somatic alteration with loss of protein expression | Enriched in Lynch-associated OEC within the MMRd subset (yoshida2025molecularpathologyof pages 1-3) | Defective mismatch repair with hypermutator phenotype | Supports Lynch syndrome diagnosis and ICI consideration; should be included in routine MMR IHC panels (yoshida2025molecularpathologyof pages 1-3) | **MMRd** |
| DNA mismatch repair | **PMS2** | Loss-of-function germline or somatic alteration with loss of protein expression | Present in MMRd tumors, either isolated or paired with MLH1 loss depending on mechanism (yoshida2025molecularpathologyof pages 1-3) | Defective mismatch repair and MSI development | Lynch screening relevance; contributes to molecular classification and therapeutic stratification (yoshida2025molecularpathologyof pages 1-3) | **MMRd** |
| Replication proofreading | **POLE** | Pathogenic exonuclease-domain mutation causing ultramutation | Uncommon but clinically important subset; specifically recognized in OEC molecular classification (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3) | Causes defective proofreading during DNA replication, producing ultrahigh tumor mutational burden | Associated with excellent prognosis; may justify treatment de-escalation in some contexts and may enhance immunotherapy responsiveness (yoshida2025molecularpathologyof pages 1-3) | **POLE-ultramutated** |
| Genome stability / TP53 axis | **p53 pathway** | Abnormal p53 pattern / TP53 alteration in a minority, especially high-grade cases | Minority subset; defines biologically aggressive p53-abnormal OECs (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3) | Genomic instability and more aggressive tumor biology | Associated with poorer prognosis and need for intensified management relative to POLEmut/MMRd subsets (yoshida2025molecularpathologyof pages 1-3) | **p53-abnormal** |
| Integrated molecular classification | **MMR pathway (overall)** | Deficiency detected by IHC/MSI testing rather than a single-gene event | Clinically meaningful subset; OEC is enriched for Lynch-associated tumors, supporting routine MMR testing (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3) | Hypermutation, MSI, immune activation potential | Essential for universal screening workflows, prognostic stratification, and selection for checkpoint inhibition (yoshida2025molecularpathologyof pages 1-3) | **MMRd** |
| Integrated molecular classification | **PI3K/AKT/mTOR pathway (overall)** | Combined activation through **PIK3CA** gain and/or **PTEN** loss | One of the dominant pathway-level themes in OEC and endometriosis-associated ovarian cancer (yoshida2025molecularpathologyof pages 1-3) | Promotes survival, proliferation, metabolic rewiring, and progression from endometriosis | Major translational target class; links precursor lesions to invasive carcinoma (yoshida2025molecularpathologyof pages 1-3) | Mostly **NSMP**, also across other subtypes |
| Integrated molecular classification | **Wnt/β-catenin pathway (overall)** | Pathway activation mainly through **CTNNB1** alteration | Characteristic of endometrioid differentiation (leo2021whatisnew pages 1-2, yoshida2025molecularpathologyof pages 1-3) | Reinforces endometrioid lineage program and tumor growth | Useful for histotype assignment and biologic interpretation of morphology | Mostly **NSMP** |


*Table: This table summarizes the major recurrent molecular alterations and pathway-level abnormalities reported in ovarian endometrioid carcinoma, including their biologic effects and clinical implications. It is useful for linking histology, molecular subtype, prognosis, and potential therapeutic opportunities.*

The molecular landscape of OEC is characterized by recurrent alterations in chromatin remodeling genes, the PI3K/AKT/mTOR signaling pathway, and DNA mismatch repair genes. Key findings include:

**ARID1A (AT-rich Interaction Domain 1A):**
- Frequent loss-of-function alterations, often reflected by loss of protein expression on immunohistochemistry
- Disrupts SWI/SNF chromatin remodeling complex
- Often co-occurs with PIK3CA mutations
- Shared between endometriotic lesions and OEC, supporting progression model (yoshida2025molecularpathologyof pages 1-3, leo2021whatisnew pages 1-2)

**PIK3CA (Phosphatidylinositol-4,5-Bisphosphate 3-Kinase Catalytic Subunit Alpha):**
- Activating/gain-of-function mutations
- Frequently co-occurs with ARID1A loss
- Present in endometriosis-related precursor lesions
- Activates PI3K/AKT/mTOR signaling pathway (yoshida2025molecularpathologyof pages 1-3, leo2021whatisnew pages 1-2)

**PTEN (Phosphatase and Tensin Homolog):**
- Inactivating mutations/loss of function
- Characteristic of endometrioid tumors
- Releases inhibition of PI3K signaling
- Frequently present in OEC (leo2021whatisnew pages 1-2, yoshida2025molecularpathologyof pages 1-3)

**CTNNB1 (Catenin Beta 1):**
- Activating mutations leading to β-catenin pathway alterations
- Characteristic/recurrent in OEC
- Helpful lineage-defining alteration for endometrioid histotype (leo2021whatisnew pages 1-2, yoshida2025molecularpathologyof pages 1-3)

**KRAS:**
- Activating mutations, less common than PTEN/PIK3CA/CTNNB1
- Also seen in benign endometriotic lesions (yoshida2025molecularpathologyof pages 1-3)

**MMR Genes (MLH1, MSH2, MSH6, PMS2):**
- Loss of expression from germline or somatic mutations, or MLH1 promoter hypermethylation
- Define the MMRd molecular subtype (25-30% of OEC)
- Enriched for Lynch syndrome-associated tumors
- Confer microsatellite instability (MSI) and hypermutation (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3)

**POLE (DNA Polymerase Epsilon, Catalytic Subunit):**
- Pathogenic exonuclease-domain mutations causing ultramutation
- Uncommon but clinically important subset
- Associated with excellent prognosis (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3)

### Molecular Subtypes

Recent data demonstrate that the endometrial cancer molecular taxonomy applies to OEC, enabling classification into four molecular subtypes (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3):

1. **POLE-ultramutated:** Excellent prognosis, candidates for treatment de-escalation
2. **Mismatch Repair-Deficient (MMRd):** Generally excellent outcomes, immunotherapy-sensitive, enriched for Lynch syndrome
3. **p53-abnormal:** Poorer prognosis, warrant intensified management
4. **No Specific Molecular Profile (NSMP):** Heterogeneous, often enriched for PI3K/Wnt pathway alterations

### Allele Frequencies
Specific population allele frequencies were not detailed in the reviewed literature, though mutations are predominantly somatic rather than germline (except in Lynch syndrome and hereditary cancer predisposition syndromes).

---

## Mechanism / Pathophysiology

### Molecular Pathways

**PI3K/AKT/mTOR Pathway:**
The PI3K/AKT/mTOR pathway is aberrantly activated in OEC, driven by PIK3CA gain-of-function mutations and/or PTEN loss. This pathway activation promotes cell proliferation, survival, metabolic rewiring, and progression from endometriosis to invasive carcinoma (yoshida2025molecularpathologyof pages 1-3). The pathway represents a major translational target, with PI3K/AKT/mTOR inhibitors under investigation (yoshida2025molecularpathologyof pages 1-3).

**Wnt/β-Catenin Pathway:**
CTNNB1 alterations activate Wnt/β-catenin signaling, affecting epithelial differentiation, proliferation, and glandular/squamous morphology. This pathway reinforces the endometrioid lineage program and is characteristic of endometrioid differentiation (leo2021whatisnew pages 1-2, yoshida2025molecularpathologyof pages 1-3).

**DNA Mismatch Repair Pathway:**
MMR deficiency in approximately 25-30% of OEC leads to microsatellite instability (MSI) and hypermutation, creating high tumor mutational burden and neoantigen load. This confers sensitivity to immune checkpoint inhibitors (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3).

**Chromatin Remodeling:**
ARID1A loss disrupts the SWI/SNF chromatin remodeling complex, altering transcriptional control and differentiation programs. This creates vulnerability to synthetic lethal approaches including ATR inhibitors and epigenetic modulators (yoshida2025molecularpathologyof pages 1-3).

### Cellular Processes

**Stepwise Malignant Transformation:**
The progression from benign endometriosis to atypical endometriosis to invasive OEC is supported by the presence of shared mutations (ARID1A, PIK3CA) in morphologically benign endometriotic lesions, indicating their potential as precursors (yoshida2025molecularpathologyof pages 1-3). This model suggests that oncogenic alterations accumulate progressively, with inflammatory signaling and oxidative stress in the endometriotic microenvironment contributing to transformation.

**Epigenetic Changes:**
In sporadic MMRd cases, MLH1 promoter hypermethylation is the predominant mechanism of MMR deficiency, contrasting with germline mutations in Lynch syndrome-associated cases (yoshida2025molecularpathologyof pages 1-3).

### Tumor Microenvironment

The tumor immune microenvironment differs between OEC and high-grade serous ovarian cancer, with endometrioid ovarian cancer potentially more conducive to immunotherapy due to lower levels of immune exclusion and T cell exhaustion (kobel2022theevolutionof pages 1-3).

### Suggested Ontology Terms

**Gene Ontology (GO) Terms:**
- GO:0006281 (DNA repair)
- GO:0006974 (cellular response to DNA damage stimulus)
- GO:0006281 (DNA mismatch repair)
- GO:0016568 (chromatin modification)
- GO:0006338 (chromatin remodeling)
- GO:0007049 (cell cycle)
- GO:0016310 (phosphorylation)
- GO:0043066 (negative regulation of apoptotic process)
- GO:0071310 (cellular response to organic substance)

**Cell Type (CL) Terms:**
- CL:0002319 (neural cell)
- CL:0000066 (epithelial cell)
- CL:0000583 (glandular epithelial cell)
- CL:0002293 (epithelial cell of endometrium)

---

## Anatomical Structures Affected

### Organ and Tissue Level

**Primary Site:**
- **Ovary (UBERON:0000992):** Primary organ of tumor development
- **Endometriotic tissue:** When arising from endometriosis, can involve peritoneum, fallopian tubes, bowel surfaces, and other pelvic structures

**Associated with Endometriosis:**
Approximately 40% of OEC cases show histological evidence of associated endometriosis. Endometriosis can involve ovarian endometriomas (cysts), peritoneal implants, and deep infiltrating lesions (yoshida2025molecularpathologyof pages 1-3).

**Secondary Involvement:**
- Pelvic peritoneum
- Omentum
- Pelvic and para-aortic lymph nodes (in advanced/metastatic disease)
- Less commonly: liver, lungs, and other distant sites

### Cellular Level

OEC arises from epithelial cells, specifically glandular epithelial cells that resemble endometrial-type epithelium. The tumor is characterized by tubular glands resembling proliferative endometrial epithelium, with variable solid, squamous, or sertoliform differentiation patterns (yoshida2025molecularpathologyof pages 1-3, leo2021whatisnew pages 1-2).

**Suggested CL Terms:**
- CL:0000066 (epithelial cell)
- CL:0000583 (glandular epithelial cell)
- CL:0002293 (epithelial cell of endometrium)

### Subcellular Level

**GO Cellular Component Terms:**
- GO:0005634 (nucleus) - site of chromatin remodeling defects and p53 alterations
- GO:0005886 (plasma membrane) - location of receptor signaling
- GO:0005737 (cytoplasm) - site of PI3K/AKT/mTOR signaling
- GO:0000228 (nuclear chromosome) - affected by chromatin remodeling defects

---

## Temporal Development

### Onset

**Age of Onset:**
OEC typically presents in adult women, with increasing diagnosis in younger women (<50 years) in some populations like Japan (yoshida2025molecularpathologyof pages 1-3). The median age at diagnosis for ovarian cancer overall is around 63 years, though OEC may present somewhat earlier given its association with endometriosis, which affects reproductive-age women (ali2023epidemiologyandrisk pages 1-2).

**Onset Pattern:**
Generally insidious, as ovarian cancer often presents with non-specific symptoms and is frequently diagnosed at advanced stages (III or IV) (ali2023epidemiologyandrisk pages 1-2). However, OEC is more often diagnosed at earlier stages compared to high-grade serous carcinoma (hayashi2023molecularhistopathologyfor pages 1-2, yoshida2025molecularpathologyof pages 1-3).

### Progression

**Disease Course:**
OEC typically follows a progressive course from precursor endometriotic lesions (in endometriosis-associated cases) through atypical endometriosis to invasive carcinoma. OEC is typically of low grade with a generally favorable prognosis compared to high-grade serous carcinoma, though high-grade/p53-abnormal OEC behaves more aggressively (hayashi2023molecularhistopathologyfor pages 1-2, yoshida2025molecularpathologyof pages 1-3).

**Disease Staging:**
The FIGO 2023 staging system for endometrial cancer integrates molecular classification, and similar principles are being applied to ovarian endometrioid carcinoma. Staging includes assessment of:
- Stage I: Tumor confined to ovaries
- Stage II: Tumor involves one or both ovaries with pelvic extension
- Stage III: Tumor involves one or both ovaries with peritoneal implants outside pelvis and/or lymph node metastases
- Stage IV: Distant metastases (kobel2022theevolutionof pages 1-3)

**Molecular Subtype and Prognosis:**
- **POLE-mutated and MMRd subsets:** Generally excellent outcomes
- **p53-abnormal/high-grade tumors:** Poorer prognosis requiring intensified management
- **NSMP:** Intermediate prognosis (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3)

---

## Diagnostics

### Clinical Tests and Biomarkers

**Serum Biomarkers:**
- **CA125:** Elevated in many ovarian cancers but with low specificity
- **HE4 (Human Epididymis Protein 4):** Combined with CA125 improves detection sensitivity and specificity for ovarian cancer (kobel2022theevolutionof pages 1-3)

### Imaging Studies

**MRI (Magnetic Resonance Imaging):**
MRI is valuable for characterizing ovarian masses. MRI-based radiomics analysis can differentiate ovarian clear cell carcinoma from endometrioid carcinoma with high accuracy (kobel2022theevolutionof pages 1-3).

### Histopathology

**Microscopic Features:**
- Tubular glands resembling proliferative endometrial epithelium
- Variable patterns: glandular, solid, squamous, sertoliform
- May show squamous metaplasia (yoshida2025molecularpathologyof pages 1-3, leo2021whatisnew pages 1-2)

**Immunohistochemical Markers:**
A four-marker IHC panel (WT1/p53/napsin A/PR) can distinguish the five principal ovarian carcinoma histotypes with high accuracy:
- **WT1:** Typically negative in OEC (positive in serous)
- **p53:** Variable; abnormal pattern in p53-abnormal molecular subtype
- **Napsin A:** Negative in OEC (positive in clear cell)
- **PR (Progesterone Receptor):** Often positive in OEC (kobel2022theevolutionof pages 1-3)

### Genetic and Molecular Testing

**MMR Immunohistochemistry (Routine Recommended):**
Assessment of MLH1, MSH2, MSH6, and PMS2 protein expression is recommended for all OEC cases to:
- Identify MMRd molecular subtype
- Screen for Lynch syndrome
- Predict immunotherapy sensitivity (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3)

**MSI Testing:**
PCR-based microsatellite instability analysis using NCI-recommended loci can confirm MMRd status (kobel2022theevolutionof pages 1-3).

**MLH1 Promoter Methylation Testing:**
For cases with MLH1/PMS2 loss, methylation testing helps distinguish sporadic (hypermethylated) from Lynch-associated (unmethylated) cases (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3).

**Molecular Subtyping (POLE, MMR, p53, NSMP):**
Using IHC surrogates and/or sequencing to classify into four molecular subtypes for prognostic stratification and therapeutic selection (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3).

**Germline Testing:**
Indicated for MMRd cases (especially if MLH1 unmethylated) and cases with family history suggestive of hereditary cancer syndromes (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3).

### Differential Diagnosis

OEC must be distinguished from:
- High-grade serous carcinoma (especially SET pattern)
- Clear cell carcinoma
- Mucinous carcinoma
- Metastatic endometrial carcinoma
- Metastatic gastrointestinal carcinoma

Immunohistochemical panels, molecular testing, and clinical correlation are essential for accurate diagnosis (leo2021whatisnew pages 1-2, kobel2022theevolutionof pages 1-3).

---

## Outcome / Prognosis

### Survival and Prognosis

OEC generally has a **more favorable prognosis** compared to high-grade serous carcinoma, particularly when diagnosed at early stages (hayashi2023molecularhistopathologyfor pages 1-2, yoshida2025molecularpathologyof pages 1-3). Prognosis varies significantly by molecular subtype:

**By Molecular Subtype:**
- **POLE-mutated:** Excellent prognosis, may justify treatment de-escalation
- **MMRd:** Generally excellent outcomes
- **NSMP:** Intermediate prognosis
- **p53-abnormal/high-grade:** Poorer prognosis, requires intensified management (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3)

**Lynch Syndrome-Associated OEC:**
Among mismatch repair-deficient endometrial cancers (which share biological features with MMRd OEC), patients with Lynch syndrome showed a trend towards better recurrence-free survival compared with MLH1-hypermethylated MMRd cases. Five-year recurrence-free survival was 91.7% (95% CI = 83.1%-100%) for Lynch syndrome cases versus 78.6% (95% CI = 73.8%-83.7%) for MLH1-hypermethylated MMRd cases (kobel2022theevolutionof pages 1-3).

**Subsequent Cancer Risk:**
Patients with Lynch syndrome-associated OEC have increased risk of subsequent cancers. The probability of subsequent Lynch-associated cancer at 10 years was 11.6% (95% CI = 0.0%-24.7%) in the Lynch syndrome group (kobel2022theevolutionof pages 1-3).

### Prognostic Factors

- **Stage at diagnosis:** Earlier stage associated with better outcomes
- **Tumor grade:** Low-grade tumors have better prognosis
- **Molecular subtype:** POLE-mutated and MMRd subtypes favorable; p53-abnormal unfavorable
- **Age:** Younger age at diagnosis may be associated with better outcomes
- **Residual disease after surgery:** Complete cytoreduction associated with improved survival

---

## Treatment

| Treatment Modality | Specific Agents / Approaches | Indications | Efficacy Data (if available) | Molecular Stratification |
|---|---|---|---|---|
| Surgery | Primary cytoreductive surgery; total hysterectomy with bilateral salpingo-oophorectomy; omentectomy; peritoneal staging/biopsies; lymph node assessment in selected early-stage cases | Standard initial management for most resectable OEC; also used for diagnosis, staging, and tumor debulking | OEC is often diagnosed at earlier stage than high-grade serous carcinoma and generally has a more favorable prognosis, supporting surgery-centered management in localized disease (hayashi2023molecularhistopathologyfor pages 1-2, yoshida2025molecularpathologyof pages 1-3) | Not molecularly restricted, but stage, grade, and histotype remain key determinants; p53-abnormal/high-grade tumors may warrant more aggressive multimodality treatment (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3) |
| Adjuvant / First-line chemotherapy | Carboplatin + paclitaxel | Standard systemic therapy after surgery for advanced-stage disease and many high-risk early-stage cases | Standard ovarian cancer backbone regimen; in mixed epithelial ovarian cohorts remains the default comparator and routine regimen. OEC generally has better outcomes than HGSC, but high-grade/p53-abnormal OEC behaves more aggressively (hayashi2023molecularhistopathologyfor pages 1-2, yoshida2025molecularpathologyof pages 1-3) | Used across molecular subtypes; potential relative de-escalation interest in POLE-mutated tumors and intensification interest in p53-abnormal tumors are emerging concepts rather than established standards (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3) |
| Neoadjuvant chemotherapy | Carboplatin + paclitaxel followed by interval debulking surgery | Patients with bulky, unresectable, or medically high-risk advanced disease | No OEC-specific trial data in available contexts; approach extrapolated from epithelial ovarian cancer practice (hayashi2023molecularhistopathologyfor pages 1-2) | Not subtype-specific; tumor burden and surgical feasibility drive use |
| Immunotherapy + chemotherapy | Pembrolizumab + carboplatin/paclitaxel, followed by pembrolizumab maintenance | Advanced or recurrent MMR-deficient/dMMR tumors; increasingly relevant where OEC shows MMRd enrichment | In NRG-GY018 endometrial cancer, 12-month PFS in dMMR disease was 74% with pembrolizumab-chemotherapy vs 38% with placebo-chemotherapy; in pMMR disease median PFS was 13.1 vs 8.7 months (kobel2022theevolutionof pages 1-3) | Most compelling in MMRd/MSI-H OEC; OEC is enriched for Lynch-associated/MMRd tumors, supporting biomarker-driven use of checkpoint inhibitors (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3) |
| Immune checkpoint inhibitor monotherapy | Pembrolizumab; dostarlimab | Recurrent/metastatic MMRd/MSI-H disease after prior therapy, or when chemotherapy is unsuitable | Robust tumor-agnostic and endometrial-cancer evidence supports activity in MMRd/MSI-H gynecologic tumors; OEC-specific efficacy data were not reported in the available contexts (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3) | Best suited to MMRd/MSI-H tumors, including Lynch syndrome-associated OEC (yoshida2025molecularpathologyof pages 1-3) |
| Hormonal therapy | Progestins; other endocrine therapy approaches used by analogy to endometrioid gynecologic tumors | Selected low-grade, hormone receptor-positive, indolent, recurrent, or fertility-/toxicity-sensitive settings | Direct OEC efficacy data not provided in the available contexts; biologic rationale exists because endometrioid tumors may retain hormone receptor expression (kobel2022theevolutionof pages 1-3, yoshida2025molecularpathologyof pages 1-3) | Most plausible in ER/PR-positive, low-grade, NSMP-type tumors rather than p53-abnormal tumors |
| Targeted therapy: PI3K/AKT/mTOR axis | Investigational PI3K, AKT, or mTOR inhibitors | Recurrent or refractory tumors with PIK3CA activation and/or PTEN loss | Pathway is a major driver in OEC and endometriosis-associated ovarian cancer; clinical benefit remains investigational in available sources (yoshida2025molecularpathologyof pages 1-3) | Best rationalized for PIK3CA-mutant and PTEN-deficient tumors; often overlaps with NSMP tumors (yoshida2025molecularpathologyof pages 1-3) |
| Targeted therapy: ARID1A-directed synthetic lethality | ATR inhibitors; epigenetic/synthetic-lethal strategies under investigation | Recurrent ARID1A-deficient tumors in trials or precision-oncology settings | Preclinical and translational rationale is strong, but no definitive OEC-specific efficacy data were reported in the available contexts (yoshida2025molecularpathologyof pages 1-3) | ARID1A-loss tumors, often with coexisting PI3K-pathway alterations (yoshida2025molecularpathologyof pages 1-3) |
| Targeted therapy: PARP inhibitors | Olaparib and related PARP inhibitors | Selected tumors with homologous recombination deficiency or pathogenic BRCA alterations; less established in typical OEC than in HGSC | In ovarian cancer organoid models, a BRCA1-mutant endometrioid organoid showed increased olaparib sensitivity relative to non-BRCA models (kobel2022theevolutionof pages 1-3) | Most relevant to BRCA1/2-mutant or HRD tumors; likely a minority of OECs compared with HGSC |
| Molecularly adapted management | POLE/MMRd/NSMP/p53-abnormal classification integrated with histology and stage | Risk stratification, prognosis, trial selection, and tailoring of adjuvant/systemic therapy | POLE-mutated and MMRd subsets generally show excellent outcomes, while p53-abnormal/high-grade tumors have poorer prognosis and may merit intensified management (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3) | POLE-mutated: favorable prognosis; MMRd: immunotherapy-sensitive; p53-abnormal: highest-risk biology; NSMP: heterogeneous, often enriched for PI3K/Wnt alterations (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3) |
| Precision preclinical testing | Patient-derived organoids (drug screening with platinum, taxane, olaparib); xenografts | Research use; potential future patient-specific therapy selection | Ovarian cancer organoids preserved histopathology/genomics and showed drug-response patterns correlating with clinical course in small series (kobel2022theevolutionof pages 1-3) | Enables individualized testing across BRCA-mutant, platinum-sensitive/resistant, and pathway-defined tumors |


*Table: This table summarizes current and emerging treatment strategies for ovarian endometrioid carcinoma, linking each modality to its main indications, available efficacy evidence, and relevant molecular subgroups. It is useful for mapping standard care alongside biomarker-driven precision approaches.*

### Surgery

**Primary Cytoreductive Surgery:**
Standard initial management includes total hysterectomy with bilateral salpingo-oophorectomy, omentectomy, peritoneal staging/biopsies, and lymph node assessment in selected cases. OEC is often diagnosed at earlier stage than high-grade serous carcinoma, supporting surgery-centered management in localized disease (hayashi2023molecularhistopathologyfor pages 1-2, kobel2022theevolutionof pages 1-3, yoshida2025molecularpathologyof pages 1-3).

### Chemotherapy

**Standard Regimen:**
Carboplatin plus paclitaxel is the standard adjuvant chemotherapy for advanced-stage disease and high-risk early-stage cases (hayashi2023molecularhistopathologyfor pages 1-2, kobel2022theevolutionof pages 1-3, yoshida2025molecularpathologyof pages 1-3).

### Immunotherapy

**Checkpoint Inhibitors:**
Immune checkpoint inhibitors (pembrolizumab, dostarlimab) have demonstrated remarkable efficacy in MMRd/dMMR tumors:

- In the NRG-GY018 trial in endometrial cancer, 12-month progression-free survival in dMMR disease was **74%** with pembrolizumab-chemotherapy versus **38%** with placebo-chemotherapy (hazard ratio 0.30; 95% CI, 0.19-0.48; P<0.001) (kobel2022theevolutionof pages 1-3)
- In pMMR disease, median PFS was 13.1 months with pembrolizumab versus 8.7 months with placebo (hazard ratio 0.54; 95% CI, 0.41-0.71; P<0.001) (kobel2022theevolutionof pages 1-3)

The combination of immune checkpoint inhibitors with chemotherapy is now standard for advanced or recurrent MMRd disease. OEC's enrichment for Lynch syndrome-associated/MMRd tumors makes this particularly relevant (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3).

**Relevant MAXO Terms:**
- MAXO:0001175 (chemotherapy)
- MAXO:0001479 (immunotherapy)
- MAXO:0000571 (surgical procedure)

### Targeted Therapy

**PI3K/AKT/mTOR Inhibitors:**
Under investigation for tumors with PIK3CA mutations and/or PTEN loss, which are common in OEC. The PI3K/AKT/mTOR pathway is a major driver and translational target (yoshida2025molecularpathologyof pages 1-3).

**ARID1A-Directed Synthetic Lethality:**
ATR inhibitors and epigenetic modulators are being investigated for ARID1A-deficient tumors, which are frequent in OEC (yoshida2025molecularpathologyof pages 1-3).

**PARP Inhibitors:**
Potential utility in tumors with homologous recombination deficiency or BRCA1/2 mutations. In preclinical models, a BRCA1-mutant endometrioid organoid showed increased olaparib sensitivity (kobel2022theevolutionof pages 1-3).

### Hormonal Therapy

Progestin-based therapy may be considered for selected low-grade, hormone receptor-positive, indolent, recurrent, or fertility-sparing cases, by analogy to endometrioid gynecologic tumors (kobel2022theevolutionof pages 1-3, yoshida2025molecularpathologyof pages 1-3).

### Molecularly Stratified Treatment

Molecular classification enables risk-stratified management:
- **POLE-mutated:** Excellent prognosis, potential treatment de-escalation
- **MMRd:** Immunotherapy-sensitive
- **p53-abnormal:** Highest-risk biology, intensified management
- **NSMP:** Heterogeneous, often enriched for PI3K/Wnt alterations, potential targets for pathway inhibitors (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3)

---

## Prevention

### Primary Prevention

**Risk Factor Modification:**
- **Oral Contraceptive Use:** 15-20% risk reduction with 5 years of use (yoshida2025molecularpathologyof pages 1-3)
- **Achieving/Maintaining Healthy Weight:** Obesity increases risk; weight management may reduce risk (yoshida2025molecularpathologyof pages 1-3)
- **Breastfeeding and Parity:** Each birth reduces risk by ~10% (yoshida2025molecularpathologyof pages 1-3)

### Secondary Prevention

**Surgical Risk Reduction:**
- **Tubal Ligation/Salpingectomy:** Protective, possibly by reducing retrograde menstruation (yoshida2025molecularpathologyof pages 1-3)
- **Risk-Reducing Salpingo-Oophorectomy:** Considered in high-risk populations (BRCA1/2 carriers, Lynch syndrome) (ali2023epidemiologyandrisk pages 1-2)

### Genetic Screening and Counseling

**Lynch Syndrome Screening:**
Universal MMR immunohistochemistry testing of all OEC cases is recommended to identify Lynch syndrome carriers, enabling:
- Genetic counseling and germline testing
- Surveillance for other Lynch-associated cancers
- Cascade testing of at-risk family members (yoshida2025molecularpathologyof pages 1-3, kobel2022theevolutionof pages 1-3)

**BRCA1/2 Testing:**
Consideration of genetic testing in cases with family history of breast/ovarian cancer or personal history suggestive of hereditary cancer syndrome (ali2023epidemiologyandrisk pages 1-2).

---

## Model Organisms and Experimental Models

### Patient-Derived Organoids (PDOs)

Patient-derived organoids have been successfully established from OEC tissues, preserving histopathology, molecular subtype characteristics, and genetic profiles including POLE, MMR, p53 status, and pathway alterations (kobel2022theevolutionof pages 1-3). OEC organoids enable:
- Drug sensitivity testing (carboplatin, paclitaxel, olaparib)
- Correlation with clinical responses
- Precision medicine applications (kobel2022theevolutionof pages 1-3)

### Patient-Derived Xenografts (PDX)

PDX models in immunodeficient mice (NOD-SCID, NSG) using:
- **Subcutaneous implantation:** Easier monitoring, higher engraftment rates
- **Orthotopic implantation:** Better recapitulates tumor microenvironment and metastatic patterns (kobel2022theevolutionof pages 1-3)

Orthotopic organoid-based PDX (O-PDX) models maintain tissue architecture, biomarker expression, and genetic profiles of original tumors, proving useful for preclinical therapeutic evaluation (kobel2022theevolutionof pages 1-3).

### Genetically Engineered Mouse Models (GEMMs)

Models with relevant mutations (Tp53, Pten, Arid1a combinations) have been developed. Syngeneic models from murine fallopian tube organoids with defined genetic alterations enable immunotherapy studies in immunocompetent hosts (kobel2022theevolutionof pages 1-3).

### Cell Lines

Limited endometrioid-specific ovarian cancer cell lines are available, making patient-derived models particularly valuable for OEC research (kobel2022theevolutionof pages 1-3).

**Applications:**
- Drug screening and therapeutic response prediction
- Mechanistic studies of pathway dependencies
- Biomarker validation
- Precision medicine approaches

---

## Summary and Clinical Implications

Ovarian endometrioid carcinoma represents approximately 10% of epithelial ovarian cancers and is distinguished by:

1. **Strong association with endometriosis** (40% of cases), suggesting a progression model from benign to malignant disease
2. **Characteristic molecular alterations** including ARID1A loss, PIK3CA/PTEN mutations, CTNNB1 alterations, and enrichment for MMR deficiency
3. **Four molecular subtypes** (POLE-ultramutated, MMRd, p53-abnormal, NSMP) with distinct prognoses and therapeutic implications
4. **Enrichment for Lynch syndrome**, necessitating universal MMR testing
5. **Generally favorable prognosis** compared to high-grade serous carcinoma, especially in POLE-mutated and MMRd subtypes
6. **Emerging immunotherapy opportunities**, particularly for MMRd tumors showing dramatic responses to checkpoint inhibitors
7. **Multiple targetable pathways** including PI3K/AKT/mTOR, chromatin remodeling, and DNA repair mechanisms

Integrating morphology with molecular classification refines diagnosis and prognostication. Routine MMR immunohistochemistry with reflex germline testing improves Lynch syndrome detection. Future priorities include prospective validation of molecular stratification, multi-omics refinement of NSMP tumors, and development of targeted therapeutic strategies for pathway-driven disease.

**Suggested MONDO ID:** MONDO:0003573 (ovarian endometrioid adenocarcinoma)

This comprehensive report synthesizes current evidence on ovarian endometrioid carcinoma, providing a foundation for clinical care, research prioritization, and therapeutic development.

References

1. (yoshida2025molecularpathologyof pages 1-3): Hiroshi Yoshida and Mayumi Kobayashi Kato. Molecular pathology of ovarian endometrioid carcinoma: a review. Oncology Research, 33:3701-3730, Nov 2025. URL: https://doi.org/10.32604/or.2025.068432, doi:10.32604/or.2025.068432. This article has 3 citations and is from a peer-reviewed journal.

2. (leo2021whatisnew pages 1-2): Antonio De Leo, Donatella Santini, Claudio Ceccarelli, Giacomo Santandrea, Andrea Palicelli, Giorgia Acquaviva, Federico Chiarucci, Francesca Rosini, Gloria Ravegnini, Annalisa Pession, Daniela Turchetti, Claudio Zamagni, Anna Myriam Perrone, Pierandrea De Iaco, Giovanni Tallini, and Dario de Biase. What is new on ovarian carcinoma: integrated morphologic and molecular analysis following the new 2020 world health organization classification of female genital tumors. Diagnostics, 11(4):697, Apr 2021. URL: https://doi.org/10.3390/diagnostics11040697, doi:10.3390/diagnostics11040697. This article has 125 citations.

3. (kobel2022theevolutionof pages 1-3): Martin Köbel and Eun Young Kang. The evolution of ovarian carcinoma subclassification. Cancers, 14:416, Jan 2022. URL: https://doi.org/10.3390/cancers14020416, doi:10.3390/cancers14020416. This article has 175 citations.

4. (wang2024globalincidenceof pages 1-2): Minmin Wang, Yanxin Bi, Yinzi Jin, and Zhi-Jie Zheng. Global incidence of ovarian cancer according to histologic subtype: a population-based cancer registry study. JCO Global Oncology, May 2024. URL: https://doi.org/10.1200/go.23.00393, doi:10.1200/go.23.00393. This article has 47 citations.

5. (phung2023trendsofovarian pages 1-2): Minh Tung Phung, Celeste Leigh Pearce, Rafael Meza, and Jihyoun Jeon. Trends of ovarian cancer incidence by histotype and race/ethnicity in the united states 1992–2019. Cancer Research Communications, 3:1-8, Jan 2023. URL: https://doi.org/10.1158/2767-9764.crc-22-0410, doi:10.1158/2767-9764.crc-22-0410. This article has 46 citations and is from a peer-reviewed journal.

6. (ali2023epidemiologyandrisk pages 1-2): Aus Tariq Ali, Osamah Al-ani, and Faisal Al-ani. Epidemiology and risk factors for ovarian cancer. Przegla̜d Menopauzalny = Menopause Review, 22:93-104, Jun 2023. URL: https://doi.org/10.5114/pm.2023.128661, doi:10.5114/pm.2023.128661. This article has 283 citations.

7. (hayashi2023molecularhistopathologyfor pages 1-2): Takuma Hayashi and Ikuo Konishi. Molecular histopathology for establishing diagnostic method and clinical therapy for ovarian carcinoma. Journal of Clinical Medicine Research, 15:68-75, Feb 2023. URL: https://doi.org/10.14740/jocmr4853, doi:10.14740/jocmr4853. This article has 25 citations.

## Artifacts

- [Edison artifact artifact-00](Ovarian_Endometrioid_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Ovarian_Endometrioid_Carcinoma-deep-research-falcon_artifacts/artifact-01.md)
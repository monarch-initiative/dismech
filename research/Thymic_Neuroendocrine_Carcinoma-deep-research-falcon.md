---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T23:33:23.336579'
end_time: '2026-07-31T23:40:01.545166'
duration_seconds: 398.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Thymic Neuroendocrine Carcinoma
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Thymic_Neuroendocrine_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thymic Neuroendocrine Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Thymic Neuroendocrine Carcinoma** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Thymic Neuroendocrine Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Thymic Neuroendocrine Carcinoma** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Thymic Neuroendocrine Carcinoma: Disease-Characteristics Report

**Scope and evidence note.** “Thymic neuroendocrine carcinoma” is used inconsistently. Some literature uses it broadly for all thymic neuroendocrine neoplasms (Th-NENs), including typical and atypical carcinoids; modern usage usually reserves **neuroendocrine carcinoma (NEC)** for poorly differentiated small-cell or large-cell carcinoma. This distinction is essential because biology, tempo, imaging phenotype, and treatment differ. Thymus-specific prospective evidence is extremely sparse; therefore, statements extrapolated from pulmonary/extrapulmonary NENs are labeled accordingly.

The following table summarizes ontology-ready findings and the principal uncertainty boundaries.

| domain | evidence-based finding | suggested ontology identifiers/terms | evidence limitations |
|---|---|---|---|
| Nomenclature / disease scope | Thymic neuroendocrine neoplasms are rare thymic epithelial tumors; available evidence groups them into well-differentiated carcinoid tumors and high-grade neuroendocrine carcinomas (small-cell and large-cell types). The exact label “thymic neuroendocrine carcinoma” is used inconsistently across sources, so knowledge-base entries should preserve both the broad thymic NEN umbrella and the high-grade NEC subset (OpenTargets Search: thymic neuroendocrine carcinoma, nicoli2023epigeneticsofthymic pages 2-3). | MONDO: **MONDO_0020516** thymic neuroendocrine carcinoma; MONDO: thymic large cell neuroendocrine carcinoma **MONDO_0003047**; MONDO: thymus small cell carcinoma **MONDO_0004122**; NCIT/MeSH IDs: unavailable here | WHO-class wording is partly inferred from review-level summaries; no directly retrieved WHO monograph text or full thymus-specific pathology paper in context. |
| Resource level | Most facts here are aggregated disease-level literature/guideline/trial-registry findings rather than individual EHR-derived observations (OpenTargets Search: thymic neuroendocrine carcinoma, NCT05061784 chunk 1). | Evidence type tag: aggregated literature / registry / trial registry | Not a patient-level dataset. |
| Anatomy | Primary site is the **thymus** in the **anterior mediastinum**; thymic NETs are described as aggressive mediastinal tumors (nicoli2023epigeneticsofthymic pages 2-3). | UBERON: thymus **UBERON:0002370**; UBERON: mediastinum **UBERON:0003406**; anatomy qualifier: anterior mediastinum ID unavailable here | “Anterior mediastinum” ontology accession not verified in retrieved context. |
| Principal phenotype: mass effect / thoracic presentation | Approximate/extrapolated: anterior mediastinal tumors commonly present with local mass-effect symptoms such as cough, chest pain, dyspnea, or may be incidentally detected; this is consistent with thymic epithelial tumor guidance but not directly quantified for thymic NEC in retrieved context (OpenTargets Search: thymic neuroendocrine carcinoma). | HPO suggestions: Chest pain **HP:0100749**; Cough **HP:0012735**; Dyspnea **HP:0002094**; Mediastinal mass ID unavailable here | Largely extrapolated from thymic epithelial tumor practice and thoracic oncology, not directly enumerated in retrieved thymic NEC abstracts. |
| Principal phenotype: endocrine syndromes | About **50%** of thymic NET manifestations were reported in one review summary as associated with endocrinopathies, including **Cushing syndrome** and acromegaly; endocrine secretion can strongly affect quality of life (nicoli2023epigeneticsofthymic pages 2-3). | HPO: Cushing syndrome **HP:0002664**; Hypercortisolism **HP:0000846**; Ectopic ACTH secretion ID unavailable here | Figure comes from a narrative review summary and may reflect pooled historical literature; not necessarily specific to only high-grade NEC. |
| Principal phenotype: hereditary association | Thymic NETs/carcinoids are associated with **MEN1**; available sources note this association and describe prophylactic thymectomy/surveillance questions in MEN1 populations (nicoli2023epigeneticsofthymic pages 2-3, NCT05061784 chunk 1). | MONDO: multiple endocrine neoplasia type 1 ID unavailable here; OMIM MEN1 syndrome ID not verified here; gene **MEN1** (HGNC:7010) | MEN1 association is strongest for thymic carcinoid / thymic NET broadly, not proven for every thymic NEC subtype. |
| Pathology / neuroendocrine differentiation markers | Neuroendocrine tumors are typically confirmed by neuroendocrine-marker expression; practical markers for ontology-ready annotation include **synaptophysin**, **chromogranin A**, and **INSM1**; cytokeratin supports epithelial nature; **Ki-67** helps grading/proliferation assessment. General NEN reviews also note chromogranin A and synaptophysin as diagnostic markers (nicoli2023epigeneticsofthymic pages 2-3). | Proteins/genes: **SYP**, **CHGA**, **INSM1**, broad-spectrum keratins (**KRT8/KRT18/KRT19** approximate), **MKI67**; NCIT marker terms: unavailable here | Synaptophysin/chromogranin use is strongly standard but not directly enumerated in a thymus-specific primary study in retrieved context; **INSM1** is included as current practice but extrapolated. |
| Pathology / SSTR biology | Somatostatin receptor subtypes are expressed in neuroendocrine neoplasms, with **SSTR2A** particularly prominent; a study across NENs concluded NECs may be candidates for somatostatin-analogue targeting and that SSTR2A can serve as a biomarker of neuroendocrine differentiation (OpenTargets Search: thymic neuroendocrine carcinoma). | Gene/protein: **SSTR2**; IHC marker: SSTR2A; CHEBI class: somatostatin analogues | Not thymus-specific; based on mixed-site NENs/NECs. |
| Molecular distinction | Current understanding supports a biologic split: **MEN1-associated / carcinoid-like** disease for well-differentiated thymic NETs versus **TP53/RB1-altered high-grade NEC-like** biology for poorly differentiated NECs. Open Targets currently shows no direct curated target evidence rows for MONDO_0020516, so TP53/RB1 annotation should be flagged as approximate/extrapolated from large-cell NEC and general NEC biology (OpenTargets Search: thymic neuroendocrine carcinoma, nicoli2023epigeneticsofthymic pages 2-3). | Gene terms: **MEN1**, **TP53**, **RB1**, possibly **CDKN2A**; GO: regulation of cell cycle **GO:0051726**, apoptotic process **GO:0006915** | Strong caveat: TP53/RB1 evidence in context is not thymus-specific primary sequencing for MONDO_0020516; direct molecular data remain sparse. |
| Metastatic pattern | Thymic NETs are described as aggressive and capable of metastasizing to **liver, lymph nodes, bone, lung, and brain** (nicoli2023epigeneticsofthymic pages 2-3). | HPO suggestions: Hepatic metastases **HP:0007340**; Lymph node metastases **HP:0005276**; Bone metastases ID unavailable here; Brain metastases ID unavailable here | Review-level statement; site-specific frequencies not available in retrieved context. |
| Epidemiology / rarity | Thymic neuroendocrine tumors are ultra-rare. In SEER-based analysis of **2000-2018**, **263** thymic NET patients were identified; another recent epidemiology paper confirms thymic NETs are part of the rare TET spectrum (OpenTargets Search: thymic neuroendocrine carcinoma). | MONDO rarity annotation applicable; Orphanet ID unavailable here | No precise population incidence per 100,000 for thymic NET alone in retrieved context. |
| Second malignancy risk | In SEER analysis, thymic NET patients had increased risk of second malignancies with **SIR 1.73 (95% CI 1.13-2.54)**; **19/263** thymic NET patients developed second malignancies and age at diagnosis was a significant risk factor (OpenTargets Search: thymic neuroendocrine carcinoma). | HPO/NCIT terms for second primary malignancy: ID unavailable here | Applies to thymic NET broadly, not only high-grade NEC. |
| Diagnostics / imaging | Approximate/current practice: diagnosis relies on thoracic imaging plus tissue biopsy; functional imaging may include somatostatin-receptor imaging when SSTR-positive disease is suspected, especially for therapeutic selection (OpenTargets Search: thymic neuroendocrine carcinoma). | Rad/biomarker suggestions: CT chest; MRI as needed; SSTR PET/CT (e.g., Ga-68 DOTATATE, CHEBI/NCIT IDs unavailable here) | Imaging workflow is partly extrapolated from general NET and thymic epithelial tumor practice; no thymus-specific imaging trial in retrieved context. |
| Diagnostics / histology | Histologic confirmation should record neuroendocrine morphology, epithelial differentiation, and proliferative index. For ontology curation, capture tumor type (carcinoid vs small-cell NEC vs large-cell NEC), marker panel, necrosis, and Ki-67/mitotic activity (OpenTargets Search: thymic neuroendocrine carcinoma, nicoli2023epigeneticsofthymic pages 2-3). | NCIT disease classes unavailable here; genes/proteins: **MKI67**, **SYP**, **CHGA**, **INSM1**, keratins | Detailed cutoff values and consensus thymus-specific grading text were not present in retrieved context. |
| Treatment classes | **Surgery** remains the principal treatment for resectable thymic epithelial tumors; systemic options across thymic NET/NEN practice may include **chemotherapy**, **somatostatin analogues**, **everolimus**, **temozolomide-based regimens/CAPTEM**, **PRRT**, and occasionally **immunotherapy**, but much of this is extrapolated from non-thymic or mixed thoracic NET literature (OpenTargets Search: thymic neuroendocrine carcinoma). | NCIT intervention suggestions: Surgical Resection; Chemotherapy; Somatostatin Analog Therapy; Everolimus Therapy; Temozolomide Regimen; Capecitabine/Temozolomide Regimen; Peptide Receptor Radionuclide Therapy; Immune Checkpoint Inhibitor Therapy | Direct thymus-specific comparative efficacy data were not retrieved; several treatment labels are extrapolated/current-practice rather than proven in thymic NEC. |
| Current real-world / trial implementations | Ongoing or recent studies relevant to thymic NET include **NCT06121271** (phase II Lu-177 DOTATATE in unlicensed indications; planned enrollment 110), **NCT07429851** (observational comparison of thymic/pulmonary/pancreatic well-differentiated high-grade NETs; enrollment 34), and **NCT05061784** (routine transcervical thymectomy in MEN1; completed, n=7) (NCT05061784 chunk 1). | ClinicalTrials.gov: **NCT06121271**, **NCT07429851**, **NCT05061784** | Trials are not specific to thymic neuroendocrine carcinoma alone; some focus on NETs or MEN1 prevention rather than established NEC treatment. |
| Prevention / MEN1 surveillance | In MEN1, prophylactic or routine **transcervical thymectomy** at time of parathyroid surgery has been used to reduce thymic carcinoid risk, but efficacy data are described as scarce; surveillance remains important (NCT05061784 chunk 1). | Preventive intervention: transcervical thymectomy; genetic counseling; MEN1 surveillance protocol IDs unavailable here | Evidence base is limited, observational, and focused on MEN1-associated thymic carcinoid risk rather than sporadic thymic NEC. |
| Prognosis / natural history | Available sources characterize thymic NETs as **aggressive** with metastatic potential and relatively limited chemotherapy responsiveness (nicoli2023epigeneticsofthymic pages 2-3). | HPO suggestions: Neoplasm metastasis **HP:0002664** approximate broad cancer term unavailable; progressive disease term unavailable here | No robust retrieved survival percentages specific to MONDO_0020516. |
| Cell/tissue ontology suggestions | Tumor likely arises from **thymic epithelial/neuroendocrine differentiated** cells within thymic tissue; annotate epithelial tumor with neuroendocrine differentiation (nicoli2023epigeneticsofthymic pages 2-3). | CL: neuroendocrine cell term approximate **CL:0000165**; thymic epithelial cell term ID unavailable here; GO CC: nucleus/cytoplasm markers not specific | Precise thymic cell-of-origin remains uncertain; CL terms not fully verified in retrieved context. |
| Model systems | No disease-specific validated model organisms or cell-line resources were identified in retrieved context for thymic neuroendocrine carcinoma; use “not established / not retrieved” in the knowledge base. | Model organism/resource IDs unavailable | Important knowledge gap. |


*Table: This table provides an ontology-ready summary of thymic neuroendocrine carcinoma/neoplasms, emphasizing what is directly supported in the retrieved evidence versus what is approximate or extrapolated. It is designed to help populate structured disease knowledge-base fields while preserving uncertainty.*

## 1. Disease information

Th-NENs are malignant epithelial neoplasms arising in the thymus and showing neuroendocrine morphology and marker expression. The family comprises well-differentiated typical/atypical carcinoids and poorly differentiated small-cell/large-cell NECs. They are among the rarest thymic epithelial tumors and account for approximately **0.4% of carcinoid tumors** in one recent review synthesis. They typically occupy the anterior mediastinum and may invade adjacent mediastinal structures or metastasize to lymph nodes, liver, bone, lung, and brain. (nicoli2023epigeneticsofthymic pages 2-3)

**Identifiers and synonyms**

- **MONDO:** MONDO:0020516, *thymic neuroendocrine carcinoma*.
- Subclasses include **MONDO:0003047**, thymic large-cell neuroendocrine carcinoma, and **MONDO:0004122**, thymus small-cell carcinoma. Open Targets returned no directly curated target associations for either thymic-specific entity. (OpenTargets Search: thymic neuroendocrine carcinoma)
- Synonyms: thymic neuroendocrine neoplasm/tumor, neuroendocrine tumor of thymus, thymic carcinoid, thymic typical carcinoid, thymic atypical carcinoid, thymic small-cell carcinoma, thymic large-cell neuroendocrine carcinoma.
- ICD-10 generally requires a site-plus-morphology approach; **C37** denotes malignant neoplasm of thymus but does not encode neuroendocrine histology. A specific ICD-11/OMIM/Orphanet identifier was not verified in the retrieved evidence.
- The evidence is aggregated disease-level literature, registry research, and trial-registry information—not individual-patient EHR data.

## 2. Etiology and risk factors

Most cases are sporadic, and no established environmental, infectious, dietary, smoking, occupational, or radiation cause is known. Consequently, no validated lifestyle-based protective factor or gene–environment interaction has been demonstrated.

The best-established inherited predisposition is **multiple endocrine neoplasia type 1 (MEN1)**, caused by pathogenic germline loss-of-function variants in **MEN1** and inherited autosomal dominantly. The association applies most clearly to thymic carcinoids/well-differentiated Th-NETs, not necessarily to every poorly differentiated NEC. Menin participates in transcriptional and chromatin-regulatory networks, providing a plausible tumor-suppressor mechanism. Thymic NETs are clinically important causes of mortality in MEN1. (nicoli2023epigeneticsofthymic pages 2-3)

For a patient with Th-NEN—particularly a young patient, multifocal endocrine disease, hyperparathyroidism, pituitary or pancreatic NET, or suggestive family history—genetic counseling and germline **MEN1** testing are appropriate. No reproducible protective allele, modifier gene, founder effect, carrier frequency, anticipation, or germline-mosaicism estimate specific to Th-NEN was identified.

## 3. Phenotypes

Presentation is heterogeneous and often insidious.

- **Local mass effects:** cough (HP:0012735), dyspnea (HP:0002094), chest pain (HP:0100749), superior vena cava obstruction, or an incidentally detected anterior mediastinal mass. These manifestations may progress as the lesion enlarges; thymus-specific frequencies were unavailable.
- **Endocrine/paraneoplastic manifestations:** ectopic ACTH secretion can cause hypercortisolism (HP:0000846) and Cushing syndrome (HP:0002664), including hypertension, diabetes, hypokalemia, infections, muscle weakness, and osteoporosis. Acromegaly and other secretory syndromes are reported but less characteristic. One review summarized endocrinopathy associations in approximately **50%** of thymic NET manifestations, although this historical pooled estimate should not be interpreted as the frequency in high-grade NEC alone. (nicoli2023epigeneticsofthymic pages 2-3)
- **Metastatic disease:** lymph-node, liver, skeletal, pulmonary, or cerebral metastases may produce pain, neurologic impairment, respiratory compromise, or organ dysfunction. (nicoli2023epigeneticsofthymic pages 2-3)
- **Quality of life:** thoracic symptoms, hormone excess, treatment toxicity, anxiety about recurrence, and MEN1-related multiple tumors can substantially impair physical and psychosocial functioning. No validated Th-NEN-specific EQ-5D, SF-36, or PROMIS dataset was retrieved.

## 4. Genetic and molecular information

There is no single somatic variant that defines all Th-NENs.

- **MEN1:** germline pathogenic variants cause MEN1 syndrome; tumorigenesis usually follows biallelic tumor-suppressor inactivation. Sporadic well-differentiated NETs may also acquire somatic MEN1-pathway alterations. Exact thymus-specific variant spectra and allele frequencies were not available.
- **High-grade NEC framework:** loss of **TP53** and **RB1** function is a central model for poorly differentiated NEC, causing checkpoint failure, genomic instability, and rapid proliferation. However, Open Targets found **zero direct target-association rows for MONDO:0020516**; TP53/RB1 evidence in the retrieved database pertains to large-cell NEC across sites and must not be represented as proven universal thymic causation. Other cross-site LCNEC-associated genes include **IDH2, SMARCA4, CDKN2A, BRAF, STK11**, and **KEAP1**. (OpenTargets Search: thymic neuroendocrine carcinoma)
- **Variant interpretation:** tumor-panel variants should be classified as somatic oncogenic alterations using AMP/ASCO/CAP criteria, while suspected germline variants require ACMG/AMP interpretation. Tumor-only detection of a MEN1 alteration does not establish hereditary MEN1.
- **Epigenetics/omics:** thymic epithelial tumors show methylation, histone, and noncoding-RNA dysregulation, but neuroendocrine-subtype-specific epigenomic, transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial, and CRISPR-screen datasets remain inadequate. (nicoli2023epigeneticsofthymic pages 2-3)
- No recurrent thymus-specific translocation, aneuploidy, pathogenic structural variant, or validated modifier gene was established.

## 5. Environmental information

No infectious agent or transmissible process is implicated. Evidence does not support smoking, alcohol, diet, exercise, pollution, or occupational toxins as established causal factors. Apparent associations from pulmonary small-cell/large-cell NEC should not be transferred to a primary thymic tumor without site confirmation. Environmental primary prevention is therefore unavailable beyond general cancer-health recommendations.

## 6. Mechanism and pathophysiology

A cautious causal model is:

1. **Upstream initiation:** inherited or somatic tumor-suppressor disruption—MEN1/menin biology particularly in well-differentiated thymic NET, or TP53–RB1 checkpoint loss in the extrapolated high-grade NEC model.
2. **Cellular transformation:** altered chromatin/transcription, defective G1/S control, resistance to apoptosis, genomic instability, and clonal expansion of a thymic epithelial cell with neuroendocrine differentiation.
3. **Tumor phenotype:** expression of synaptophysin, chromogranin A, INSM1, and sometimes somatostatin receptors; increasing mitoses, Ki-67 labeling, and necrosis accompany aggressive disease.
4. **Local/systemic consequences:** mediastinal invasion causes compression; lymphatic/hematogenous spread causes distant disease; secretion of ACTH or other peptides produces endocrine syndromes.

Suggested ontology annotations include regulation of cell cycle (GO:0051726), apoptotic process (GO:0006915), DNA-damage response, chromosome segregation, hormone secretion, epithelial-cell proliferation, and neuroendocrine cell differentiation. Candidate cell terms are neuroendocrine cell (CL:0000165) and thymic epithelial cell; precise cell of origin remains unresolved. SSTR2 expression offers a mechanistic link to somatostatin-receptor imaging, somatostatin analogues, and peptide-receptor radionuclide therapy, although retrieved receptor evidence was derived from mixed-site NENs rather than a thymus-specific cohort.

## 7. Anatomical structures affected

The primary organ is the **thymus** (UBERON:0002370), usually in the anterior mediastinum; mediastinum may be annotated UBERON:0003406. Disease can extend into mediastinal fat, pleura, pericardium, lung, great vessels, or chest wall and spread to regional lymph nodes. Common distant sites include liver, bone, lung, and brain. (nicoli2023epigeneticsofthymic pages 2-3)

At tissue level, this is an epithelial malignancy with neuroendocrine differentiation. Relevant subcellular compartments include the nucleus for menin, p53, RB, and Ki-67; cytoplasm/secretory vesicles for chromogranin and synaptophysin; and plasma membrane for SSTR2. Lateralization is not meaningful.

## 8. Temporal development

Typical onset is in adulthood, although pediatric and young-adult MEN1-associated cases occur. The onset is generally chronic and occult rather than acute; hormone secretion may bring earlier recognition.

Course depends strongly on differentiation and stage. Typical carcinoid is usually more indolent, atypical carcinoid intermediate, and small-/large-cell NEC rapidly progressive. Nevertheless, even well-differentiated thymic carcinoids can recur late. Disease is staged anatomically using contemporary thymic-tumor TNM practice, while older studies often use Masaoka-Koga categories; these systems should not be conflated. Complete resection offers the principal chance of durable remission, but prolonged surveillance is justified because late local or distant recurrence occurs. No spontaneous-remission pattern or validated critical developmental window is known.

## 9. Inheritance, epidemiology, and population

This is an **ultra-rare** cancer. A SEER analysis identified **263 thymic NET patients from 2000–2018**; a reliable standalone population incidence per 100,000 was not available in the retrieved evidence. In that cohort, **19/263** developed a second malignancy. The standardized incidence ratio was **1.73 (95% CI 1.13–2.54)**, and the reported age-adjusted second-cancer incidence was **4,178.46 per 100,000 persons**. Older age at diagnosis was a significant risk factor. These values apply to thymic NET broadly, not exclusively poorly differentiated NEC. (OpenTargets Search: thymic neuroendocrine carcinoma)

MEN1 predisposition is autosomal dominant, with age-dependent and variable expression of the syndrome; Th-NEN itself is not inherited as an isolated Mendelian cancer in most patients. Reliable disease-specific penetrance, ethnic prevalence, geographic gradients, founder variants, and sex ratio were not established in the retrieved evidence.

## 10. Diagnostics

**Imaging.** Contrast-enhanced chest CT is the primary anatomical study; MRI helps assess vascular, cardiac, or spinal involvement. FDG-PET/CT can support staging of aggressive NEC. Somatostatin-receptor PET/CT—such as gallium-68 DOTATATE—is useful when well-differentiated or SSTR-positive disease is suspected and for selecting somatostatin-analogue or PRRT strategies. Brain and bone imaging are symptom/stage directed.

**Pathology.** Diagnosis requires tissue. Record architecture, cytology, mitotic activity, necrosis, Ki-67 index, lymphovascular invasion, and neuroendocrine differentiation. A practical panel includes pancytokeratin, synaptophysin, chromogranin A, and INSM1, with Ki-67 for proliferation. Additional markers help exclude mimics and determine origin; a mediastinal neuroendocrine carcinoma must be distinguished from pulmonary metastasis/direct extension, lymphoma, thymoma, thymic squamous carcinoma, paraganglioma, germ-cell tumor, and metastatic NET from another organ. Serum chromogranin A is nonspecific; ACTH/cortisol and other hormones should be tested when clinically indicated.

**Genetics.** Germline MEN1 sequencing plus deletion/duplication analysis is appropriate when hereditary disease is suspected. Broad tumor NGS may identify actionable alterations in advanced disease, but WES/WGS, RNA-seq, methylation testing, CMA, karyotyping, FISH, mitochondrial, and repeat-expansion tests are not routine diagnostic requirements. No population screening is recommended. MEN1 carriers require syndrome-directed surveillance.

## 11. Outcome and prognosis

Th-NENs are characterized as aggressive, metastasis-prone neoplasms with limited chemotherapy responsiveness, although this generalization spans biologically different subtypes. (nicoli2023epigeneticsofthymic pages 2-3) Major adverse prognostic factors are poorly differentiated/small-cell or large-cell histology, advanced stage, incomplete resection, lymph-node or distant metastasis, high proliferative activity, tumor necrosis, hormone-mediated morbidity, and progression despite systemic therapy.

No sufficiently robust, subtype-specific 5- or 10-year survival estimate was recovered for MONDO:0020516; reporting a pooled percentage would risk mixing carcinoid and NEC. Important complications include mediastinal compression, endocrine crises, metastatic organ dysfunction, recurrence, treatment toxicity, and second primary malignancies. The elevated second-cancer risk supports long-term, individualized follow-up. (OpenTargets Search: thymic neuroendocrine carcinoma)

## 12. Treatment and current applications

Management should occur in a multidisciplinary thymic/NET center.

1. **Localized/resectable disease:** complete en-bloc surgical resection, generally with appropriate regional lymph-node assessment, is the preferred curative strategy. Consider postoperative radiotherapy for incomplete margins, locally advanced disease, or selected high-risk pathology. NCIt suggestions: Surgical Resection; Thymectomy; Lymph-Node Dissection; Adjuvant Radiation Therapy.
2. **High-grade NEC:** platinum plus etoposide is commonly used by extrapolation from pulmonary/extrapulmonary NEC, including neoadjuvant, adjuvant, or metastatic settings. Toxicities include myelosuppression, infection, nausea, renal/neurologic toxicity, and alopecia. Direct thymus-specific comparative trials are lacking.
3. **Well-differentiated/SSTR-positive disease:** somatostatin analogues can control hormone secretion and may stabilize disease; everolimus is used by extrapolation from lung/GEP NET evidence. Temozolomide-based treatment, often CAPTEM, is increasingly reported in advanced thymic NET, but robust randomized thymus-specific response estimates are unavailable.
4. **PRRT:** lutetium-177–labeled somatostatin analogues are a rational option for progressive, strongly SSTR-positive disease. Relevant current studies include **NCT06121271**, a planned phase II study of Lu-177 DOTATATE in unlicensed indications, including thymic NET (planned n=110). A thymus-inclusive Lu-177 DOTATOC study, **NCT04276597**, was withdrawn with no enrollment.
5. **Immunotherapy/targeted therapy:** checkpoint blockade may be considered selectively in refractory high-grade disease, but efficacy is uncertain and thymic-tumor immune toxicities warrant caution. Molecularly matched therapy should depend on a validated actionable alteration rather than histology alone.
6. **Hormonal/supportive care:** control hypercortisolism urgently when present; manage pain, nutrition, infection, thrombosis, cardiopulmonary compromise, and treatment-related disability. Rehabilitation should be individualized.

Other relevant studies include **NCT07429851**, an observational comparison of thymic, pulmonary, and pancreatic well-differentiated high-grade NETs (planned n=34), and **NCT06141369**, an individualized mRNA-neoantigen-vaccine study enrolling advanced endocrine tumors. These are not dedicated randomized Th-NEC trials.

No CPIC or PharmGKB genotype-guided regimen is established for this disease, and gene, cell, or RNA therapies are not standard.

## 13. Prevention

There is no proven primary prevention for sporadic disease, no applicable vaccine, and no population screening program. In MEN1, genetic counseling, cascade testing, and periodic thoracic imaging represent secondary prevention/early detection.

Routine transcervical thymectomy performed during MEN1 parathyroid surgery has been proposed as prophylaxis against thymic carcinoid. **NCT05061784** was a completed seven-person observational study of this approach with follow-up up to 100 months; its registry summary emphasizes that efficacy evidence remains scarce. Thus, prophylactic thymectomy should be represented as a syndrome-specific expert strategy, not proven universal prevention. (NCT05061784 chunk 1)

Tertiary prevention comprises complete initial staging/resection, endocrine control, recurrence surveillance, and age-appropriate screening for second primary cancers. The observed SIR of 1.73 supports prolonged follow-up but does not by itself define a special screening schedule. (OpenTargets Search: thymic neuroendocrine carcinoma)

## 14. Other species and natural disease

No well-characterized naturally occurring homolog of human thymic NEC in a companion animal or wildlife species was identified. Sporadic thymic and neuroendocrine tumors occur in animals, but comparative equivalence is unproven. The disease is noninfectious, nontransmissible, and nonzoonotic. MEN1, TP53, RB1, and core cell-cycle pathways are evolutionarily conserved, but this alone does not establish an animal disease model. NCBI Taxon 9606 applies to the human disease.

## 15. Model organisms and experimental systems

No validated, widely adopted Th-NEN-specific mouse model, patient-derived xenograft, organoid, iPSC model, or canonical cell line was identified in the retrieved evidence. Generic MEN1-deficient endocrine-tumor models can interrogate menin biology, and TP53/RB1-deficient pulmonary NEC models can study high-grade neuroendocrine transformation, but neither fully reproduces the thymic microenvironment or complete histologic spectrum. This is a major research gap affecting biomarker validation, drug screening, and mechanistic inference.

## Recent developments and authoritative interpretation

The most important 2023–2024 developments are improved separation of well-differentiated NET from poorly differentiated NEC, increasing use of molecular profiling and SSTR imaging to select systemic therapy, prospective investigation of PRRT in non-GEP sites, and registry-based quantification of second-malignancy risk. The January 2024 SEER analysis concluded that thymic NET patients have a significantly increased second-cancer risk; its abstract reported 263 patients, 19 second malignancies, and SIR 1.73. (OpenTargets Search: thymic neuroendocrine carcinoma)

The principal expert conclusion is that precision begins with **correct classification**. Combining carcinoid and high-grade NEC creates misleading survival, molecular, and treatment estimates. Current evidence supports surgery for resectable disease, MEN1 assessment where indicated, SSTR-directed approaches for receptor-positive well-differentiated tumors, and platinum-based therapy for poorly differentiated NEC. For many other decisions, referral-center consensus and cross-site extrapolation remain necessary.

## Selected sources and dates

- Nicolì V, Coppedè F. *Epigenetics of Thymic Epithelial Tumors.* **Cancers. Published January 2023.** DOI: https://doi.org/10.3390/cancers15020360. The review states that the neuroendocrine forms are the “rarest and aggressive” thymic epithelial tumors and emphasizes the need for integrated genetic, epigenetic, and expression studies. (nicoli2023epigeneticsofthymic pages 2-3)
- Qiu G, Wang F, Wang Y. *Incidence of second malignancies in patients with thymic carcinoma and thymic neuroendocrine tumor.* **Journal of Cancer Research and Clinical Oncology. Published January 2024.** DOI: https://doi.org/10.1007/s00432-023-05522-3. Its abstract concludes: “The incidence of second malignancies in patients with thymic carcinoma and thymic NET is significantly higher than the patients in the normal population.” (OpenTargets Search: thymic neuroendocrine carcinoma)
- ClinicalTrials.gov. *Routine Transcervical Thymectomy in MEN-1 Patients.* **Completed August 2021.** NCT05061784: https://clinicaltrials.gov/study/NCT05061784. (NCT05061784 chunk 1)
- Open Targets disease record, **MONDO:0020516**, accessed through the current database search; no direct target associations were returned for thymic neuroendocrine carcinoma. (OpenTargets Search: thymic neuroendocrine carcinoma)

**Evidence limitation:** PMID values were not present in the retrieved full-text evidence for the principal recent papers, so DOI and registry identifiers are supplied rather than inferred. Exact survival rates, phenotype frequencies, somatic-variant frequencies, and treatment response rates should remain null/unknown in a knowledge base unless tied to a clearly defined histologic subtype and source cohort.

References

1. (OpenTargets Search: thymic neuroendocrine carcinoma): Open Targets Query (thymic neuroendocrine carcinoma, 18 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (nicoli2023epigeneticsofthymic pages 2-3): Vanessa Nicolì and Fabio Coppedè. Epigenetics of thymic epithelial tumors. Jan 2023. URL: https://doi.org/10.3390/cancers15020360, doi:10.3390/cancers15020360. This article has 12 citations.

3. (NCT05061784 chunk 1): Rajeev Parameswaran. Routine Transcervical Thymectomy in MEN-1 Patients. National University Health System, Singapore. 2021. ClinicalTrials.gov Identifier: NCT05061784

## Artifacts

- [Edison artifact artifact-00](Thymic_Neuroendocrine_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)
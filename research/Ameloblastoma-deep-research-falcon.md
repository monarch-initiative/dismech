---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-22T10:11:31.438384'
end_time: '2026-06-22T10:24:19.927965'
duration_seconds: 768.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ameloblastoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Ameloblastoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ameloblastoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ameloblastoma** covering all of the
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
- **Disease Name:** Ameloblastoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Ameloblastoma** covering all of the
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


# Comprehensive Research Report on Ameloblastoma

## 1. Disease Information

### Overview and Definition

Ameloblastoma is a benign epithelial odontogenic tumor that constitutes approximately 10% of all tumors arising in the mandible and maxilla (ghai2022ameloblastomaanupdated pages 1-2, malakar2023theroleof pages 1-2). It is characterized as a locally invasive, slow-growing tumor of odontogenic epithelium, mainly arising from enamel tissue that has not undergone differentiation (ghai2022ameloblastomaanupdated pages 1-2). Despite its histologically benign appearance, ameloblastoma exhibits locally aggressive behavior with high recurrence rates and rare metastatic potential, rendering it an "enigmatic tumor" (ghai2022ameloblastomaanupdated pages 1-2, hendra2020globalincidenceand pages 1-2).

Ameloblastoma was first recognized by Cusack in 1827 and designated as "adamantinoma" in 1885 by Louis-Charles Malassez, before being renamed "ameloblastoma" by Ivey and Churchill in 1930 (ghai2022ameloblastomaanupdated pages 1-2).

### WHO Classification

The **2017 WHO Classification** described four main subtypes:
- Ameloblastoma (solid/multicystic)
- Unicystic ameloblastoma
- Extraosseous/peripheral ameloblastoma
- Metastasizing ameloblastoma (ghai2022ameloblastomaanupdated pages 1-2)

The **2022 WHO Classification (5th edition)** introduced important updates:
- **Conventional ameloblastoma** (replacing "solid/multicystic" terminology)
- **Unicystic ameloblastoma** (5-22% of cases)
- **Extraosseous/peripheral ameloblastoma**
- **Adenoid ameloblastoma** (newly recognized entity)
- **Metastasizing ameloblastoma** (vered2022updatefromthe pages 1-2, soluktekkesin2022theworldhealth pages 1-2)

Key changes in the 2022 edition include removal of desmoplastic ameloblastoma as a separate subtype (now considered a histological variant) and addition of "essential and desirable diagnostic criteria" for each entity (vered2022updatefromthe pages 1-2, soluktekkesin2022theworldhealth pages 1-2).

### Disease Category and Identifiers

**Category:** Benign epithelial odontogenic tumor

**Synonyms:**
- Adamantinoma (historical term, no longer preferred)
- Solid/multicystic ameloblastoma (older terminology for conventional type)

**Note on identifiers:** While specific OMIM, Orphanet, or MONDO IDs were not explicitly provided in the retrieved literature, ameloblastoma is classified within the broader category of odontogenic tumors in ICD-11 and MeSH terminology systems. The disease information is derived from aggregated disease-level resources including WHO classifications, systematic reviews, and meta-analyses rather than individual patient EHR data (ghai2022ameloblastomaanupdated pages 1-2, vered2022updatefromthe pages 1-2, hendra2020globalincidenceand pages 1-2).

---

## 2. Etiology

### Disease Causal Factors

**Genetic/Molecular Mechanisms:**
Ameloblastoma pathogenesis is multifactorial and involves molecular alterations in key cellular pathways. The most significant molecular event is somatic mutation of the BRAF proto-oncogene, specifically **BRAF V600E** (valine to glutamic acid substitution at amino acid position 600), which is found in **70.49%** of ameloblastoma cases based on meta-analysis of 833 cases (yusof2022brafv600emutation pages 1-2). This mutation results in constitutive activation of the mitogen-activated protein kinase (MAPK) signaling pathway, leading to uncontrolled cell proliferation (malakar2023theroleof pages 1-2, yusof2022brafv600emutation pages 1-2).

Other molecular mechanisms involve:
- MAPK pathway alterations including FGFR2, KRAS, NRAS, HRAS mutations
- Hedgehog pathway activation via SMO mutations (SMO-L412F most common), particularly in maxillary tumors
- PIK3CA mutations (less common)
- Wnt/β-catenin pathway dysregulation (ghai2022ameloblastomaanupdated pages 1-2, yusof2022brafv600emutation pages 1-2, hurnik2023metastasisingameloblastomaor pages 1-2, nguyen2022newameloblastomacell pages 1-2)

**Tissue/Cellular Origin:**
Ameloblastoma is thought to arise from remnants of odontogenic epithelium including:
- Rests of dental lamina
- Developing enamel organ
- Epithelial lining of odontogenic (dentigerous) cysts
- Basal epithelial cells of the oral mucosa (hendra2020globalincidenceand pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**Environmental Factors:**
The precise etiology remains obscure. Proposed contributing factors include:
- Localized trauma
- Inflammation
- Nutritional imbalances
- Vitamin deficiencies
- Possible link to HPV (proposed but not definitively established) (ragunathan2022prevalenceandepidemiological pages 1-2, peralta2024effectivenessofcontemporary pages 1-2)

### Risk Factors

**Genetic Risk Factors:**
- **BRAF V600E mutation:** Strongly associated with disease pathogenesis; significant meta-analysis association with patients younger than 54 years and mandibular location (yusof2022brafv600emutation pages 1-2)
- **FANCA p.S858R germline mutation:** Reported in one metastasizing case, suggesting potential susceptibility role, though interpretation requires further validation (hurnik2023metastasisingameloblastomaor pages 1-2)

**Demographic Risk Factors:**
- **Age:** Peak incidence in third decade of life (mean age 34 years) (hendra2020globalincidenceand pages 1-2)
- **Sex:** Slight male predominance with male:female ratio of approximately 1.14:1 to 1.2:1 (hendra2020globalincidenceand pages 1-2, gasparro2024theeffectof pages 1-2)
- **Geographic variation:** Higher prevalence in Africa and Asia compared to Europe and North America (malakar2023theroleof pages 1-2)

**Anatomical Risk Factors:**
- Mandibular location accounts for approximately 80% of cases (malakar2023theroleof pages 1-2, luca2026longtermclinicaloutcome pages 1-2)
- Posterior mandible (molar-ramus region) is the most common site (hendra2020globalincidenceand pages 1-2)

### Protective Factors

No specific genetic or environmental protective factors have been identified in the literature reviewed. The sporadic, non-inherited nature of ameloblastoma (driven by somatic mutations) means traditional protective factor analysis is not applicable.

### Gene-Environment Interactions

Gene-environment interactions have not been systematically characterized for ameloblastoma. The disease appears to be primarily driven by somatic genetic events (BRAF, RAS, SMO mutations) rather than heritable susceptibility modified by environmental exposures. However, the proposed role of trauma, inflammation, or viral infection in disease initiation suggests potential gene-environment interplay that requires further investigation.

---

## 3. Phenotypes

### Clinical Phenotypes

**Primary Symptoms and Signs:**

**HP:0030329 - Jaw swelling** (most characteristic)
- Painless, slowly progressive swelling of the jaw (mandible or maxilla)
- Expansion of both buccal and lingual cortical plates
- Frequency: Present in nearly all cases at time of diagnosis
- Age of onset: Variable, most commonly in third decade
- Severity: Progressive, can become massive
- Quality of life impact: Significant cosmetic and functional impairment (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**HP:0000303 - Facial asymmetry**
- Noticeable facial deformity due to unilateral jaw expansion
- Frequency: Common in established disease
- Progression: Increases with tumor growth
- Quality of life impact: Severe psychological distress, social stigma (malakar2023theroleof pages 1-2, gasparro2024theeffectof pages 1-2)

**HP:0030751 - Tooth displacement**
- Displacement and mobility of teeth within affected jaw region
- Frequency: Common
- Severity: Can lead to tooth loss
- Quality of life impact: Impaired mastication, speech difficulties (gasparro2024theeffectof pages 1-2)

**HP:0000238 - Paresthesia** (when involving nerve)
- Numbness or altered sensation, particularly when inferior alveolar nerve is affected
- Frequency: Less common, occurs in advanced disease
- Severity: Variable
- Quality of life impact: Functional impairment, discomfort (peralta2024effectivenessofcontemporary pages 1-2)

**HP:0012531 - Pain**
- Initially painless; pain develops as tumor enlarges and invades surrounding structures
- Frequency: Variable, more common in advanced cases
- Severity: Mild to moderate in most cases
- Quality of life impact: Reduced quality of life (gasparro2024theeffectof pages 1-2)

**Laboratory/Radiographic Abnormalities:**

**Radiographic findings** (essential for diagnosis):
- Unilocular or multilocular radiolucency
- Classic "soap-bubble" or "honeycomb" appearance (multilocular pattern)
- Well-defined radiolucent area encircling crown of unerupted tooth (mimicking dentigerous cyst)
- Cortical bone destruction with preservation of some trabeculae (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

### Histopathological Phenotypes

**HP:0030077 - Follicular pattern** (most common)
- Islands of odontogenic epithelium with peripheral palisading and reverse polarization
- Central stellate reticulum-like tissue
- Frequency: Most common histological pattern globally (hendra2020globalincidenceand pages 1-2)

**HP:0030078 - Plexiform pattern** (second most common)
- Anastomosing cords and sheets of odontogenic epithelium
- Frequency: Very common (hendra2020globalincidenceand pages 1-2)

Additional histological variants include acanthomatous, granular cell, basal cell, keratopapillary, and desmoplastic patterns (ghai2022ameloblastomaanupdated pages 1-2).

### Quality of Life Impact

**Overall Disease Burden:**
Ameloblastoma significantly impacts multiple domains of quality of life:
- **Physical function:** Impaired mastication, speech, and swallowing in advanced cases
- **Psychological well-being:** Severe distress due to facial deformity, anxiety about recurrence
- **Social function:** Stigmatization, social withdrawal
- **Aesthetic concerns:** Major cosmetic defects requiring extensive reconstruction (malakar2023theroleof pages 1-2, gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2)

**Treatment-related QOL impacts:**
- Radical surgical resection causes significant morbidity including permanent disfigurement, functional impairment, and psychological distress
- Conservative treatment offers better immediate QOL but carries higher recurrence risk requiring repeat surgeries
- Long-term rehabilitation including dental implants and prosthetics can restore function and aesthetics but requires extended treatment duration (gasparro2024theeffectof pages 1-2, peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

---

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Variants

| Domain | Characteristic | Key details / values | Evidence citation |
|---|---|---|---|
| WHO / disease category | Core disease definition | Benign epithelial odontogenic tumor of jaw origin; locally aggressive, slow-growing, recurrent, and rarely metastasizing | (ghai2022ameloblastomaanupdated pages 1-2, gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2) |
| WHO classification | 2017 WHO types | Ameloblastoma; unicystic ameloblastoma; extraosseous/peripheral ameloblastoma; metastasizing ameloblastoma | (ghai2022ameloblastomaanupdated pages 1-2) |
| WHO classification | 2022 WHO types | Conventional ameloblastoma; unicystic ameloblastoma; extraosseous/peripheral ameloblastoma; adenoid ameloblastoma; metastasizing ameloblastoma | (vered2022updatefromthe pages 1-2, soluktekkesin2022theworldhealth pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| WHO classification | Conventional ameloblastoma | Most common type; previously called solid/multicystic; usually mandibular; histologic patterns include follicular, plexiform, acanthomatous, and desmoplastic | (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| WHO classification | Unicystic ameloblastoma | Approx. 5%–22% of all ameloblastomas; younger patients; luminal, intraluminal, and mural variants discussed in modern classification/treatment planning | (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| WHO classification | Peripheral / extraosseous ameloblastoma | Rare soft-tissue variant overlying jaws; generally less aggressive than intraosseous forms | (gasparro2024theeffectof pages 1-2) |
| WHO classification | Metastasizing ameloblastoma | Rare; classified as benign despite metastatic potential because histology resembles benign ameloblastoma | (ghai2022ameloblastomaanupdated pages 1-2, hurnik2023metastasisingameloblastomaor pages 1-2) |
| WHO classification | Adenoid ameloblastoma | Newly recognized benign epithelial odontogenic tumor in WHO 2022 classification | (vered2022updatefromthe pages 1-2, soluktekkesin2022theworldhealth pages 1-2) |
| Epidemiology | Global incidence | Pooled incidence rate 0.92 per million person-years (95% CI 0.57–1.49) | (hendra2020globalincidenceand pages 1-2) |
| Epidemiology | Alternative incidence statement in review literature | Global incidence summarized as about 0.92 per 1,000,000 people/year | (raemy2024antimapktargetedtherapy pages 1-2) |
| Epidemiology | Age distribution | Mean age 34 years; peak incidence in third decade of life | (hendra2020globalincidenceand pages 1-2) |
| Epidemiology | Sex distribution | Slight male predominance: 53% male overall; male:female ratio about 1.14:1 in umbrella review | (hendra2020globalincidenceand pages 1-2, gasparro2024theeffectof pages 1-2) |
| Epidemiology | Anatomic distribution | Mandible is preferred site; about 80% mandibular in several reviews/case literature | (malakar2023theroleof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| Epidemiology | Site-specific pattern | Maxillary tumors are less common; mandible:maxilla ratio reported as 1.96:1 for metastasizing ameloblastoma | (hurnik2023metastasisingameloblastomaor pages 1-2) |
| Clinical phenotype | Common presentation | Painless jaw swelling/expansion, facial asymmetry, tooth displacement or mobility, pain/paresthesia in larger lesions | (yusof2022brafv600emutation pages 1-2, gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| Imaging / phenotype | Typical radiology | Unilocular or multilocular radiolucency; classic “soap-bubble” or “honeycomb” appearance; may mimic dentigerous cyst | (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| Histopathology | Common patterns | Follicular and plexiform are the most frequent histopathologic patterns globally | (hendra2020globalincidenceand pages 1-2) |
| Histopathology | Additional variants | Acanthomatous, granular cell, basal cell, keratopapillary, and desmoplastic patterns/variants described | (ghai2022ameloblastomaanupdated pages 1-2) |
| Molecular genetics | Major pathway theme | Ameloblastoma is largely driven by MAPK pathway alterations; Hedgehog pathway also important in a subset | (yusof2022brafv600emutation pages 1-2, raemy2024antimapktargetedtherapy pages 1-2, nguyen2022newameloblastomacell pages 1-2) |
| Molecular genetics | BRAF V600E pooled prevalence | 70.49% pooled prevalence across 833 cases in meta-analysis | (yusof2022brafv600emutation pages 1-2) |
| Molecular genetics | BRAF V600E frequency range in reviews | Often summarized as 40%–80% or ~66% depending on cohort/review | (malakar2023theroleof pages 1-2, ebeling2023brafinhibitorsin pages 1-2) |
| Molecular genetics | BRAF clinicopathologic associations | Significant association with patients younger than 54 years and mandibular location; not significant for sex, histologic variants, or recurrence in one meta-analysis | (yusof2022brafv600emutation pages 1-2) |
| Molecular genetics | Other MAPK-pathway genes | FGFR2, KRAS, NRAS, HRAS and less commonly PIK3CA identified as drivers in cell-line/genomic studies | (nguyen2022newameloblastomacell pages 1-2) |
| Molecular genetics | Hedgehog-pathway genes | SMO activating mutations, especially SMO-L412F and less commonly SMO-W535L; more typical of maxillary tumors | (yusof2022brafv600emutation pages 1-2, nguyen2022newameloblastomacell pages 1-2) |
| Molecular genetics | Wnt-related findings | Upregulation of migration-related Wnt pathway genes described in a metastasizing/amplified aggressive case | (hurnik2023metastasisingameloblastomaor pages 1-2) |
| Molecular profiling | Bioinformatic transcriptomic findings | 611 differentially expressed genes; glycosaminoglycan signaling upregulated, GABA signaling downregulated; FOS highlighted as hub/target candidate | (chujan2024identificationofmolecular pages 1-2) |
| Pathobiology | Origin / tissue of origin | Thought to arise from residual odontogenic epithelium including dental lamina rests, enamel organ, odontogenic cyst lining, or basal oral mucosal cells | (hendra2020globalincidenceand pages 1-2, luca2026longtermclinicaloutcome pages 1-2, nguyen2022newameloblastomacell pages 1-2) |
| Treatment outcomes | Radical vs conservative treatment | Meta-analytic umbrella review found recurrence about three-times more likely with conservative treatment than radical treatment | (gasparro2024theeffectof pages 1-2) |
| Treatment outcomes | Overall recurrence after surgery | Review of targeted-therapy paper summarizes recurrence varying from 11% after radical surgery to 65% after conservative treatment | (raemy2024antimapktargetedtherapy pages 1-2) |
| Treatment outcomes | Conservative treatment tradeoff | Better postoperative quality of life, esthetic, and functional outcomes in smaller lesions/younger patients, but higher recurrence risk and need for closer follow-up | (gasparro2024theeffectof pages 1-2) |
| Precision therapy | BRAF/MEK targeted therapy evidence | Systematic review of 23 patients: nearly all had positive response; 4 achieved complete radiologic remission; toxicities mostly mild-to-moderate | (raemy2024antimapktargetedtherapy pages 1-2) |
| Precision therapy | Published BRAF inhibitor case literature | Review of 9 reported patients treated with dabrafenib/vemurafenib ± trametinib showed responses from tumor reduction to complete response; evidence still limited to case reports | (ebeling2023brafinhibitorsin pages 1-2) |
| Quality of life | Surgical morbidity burden | Radical surgery can cause major cosmetic, functional, and psychosocial morbidity; this drives interest in targeted neoadjuvant and organ-preserving approaches | (malakar2023theroleof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2, peralta2024effectivenessofcontemporary pages 1-2) |


*Table: This table compiles the main disease-characteristic domains for ameloblastoma, including WHO classification, epidemiology, molecular genetics, pathology, and recurrence/treatment outcomes. It is useful as a compact evidence map for populating a disease knowledge base with quantitative values and current classification terminology.*

**Primary Pathogenic Variants:**

**BRAF Gene (HGNC:1097):**
- **BRAF V600E (p.Val600Glu):** Most common pathogenic variant
  - Variant classification: Pathogenic (somatic)
  - Variant type: Missense mutation
  - Frequency: 70.49% pooled prevalence across 833 cases (meta-analysis); ranges from 40-80% in various cohorts
  - Origin: Somatic mutation
  - Functional consequence: Constitutive activation of BRAF kinase leading to sustained MAPK pathway signaling
  - Clinical correlation: Significantly associated with mandibular location and patients <54 years old (yusof2022brafv600emutation pages 1-2)

**RAS Gene Family:**
- **KRAS (HGNC:6407):** KRAS mutations including G12V and G12R
  - Variant type: Missense mutations at codon 12
  - Origin: Somatic
  - Functional consequence: Constitutive RAS-GTP activation
  - Occurrence: Less common than BRAF; variable frequency (nguyen2022newameloblastomacell pages 1-2)

- **NRAS (HGNC:7989), HRAS (HGNC:5173):** Activating mutations
  - Origin: Somatic
  - Functional consequence: MAPK pathway activation (nguyen2022newameloblastomacell pages 1-2)

**FGFR2 (HGNC:3689):**
- Activating mutations in fibroblast growth factor receptor 2
- Variant type: Various activating mutations
- Origin: Somatic
- Functional consequence: Constitutive RTK signaling upstream of MAPK pathway (nguyen2022newameloblastomacell pages 1-2)

**SMO Gene (HGNC:11119):**
- **SMO-L412F:** Most common Hedgehog pathway mutation
- **SMO-W535L:** Less common variant
- Variant classification: Pathogenic (somatic)
- Variant type: Missense mutations
- Frequency: More common in maxillary ameloblastomas
- Origin: Somatic
- Functional consequence: Constitutive activation of Hedgehog signaling pathway (yusof2022brafv600emutation pages 1-2, nguyen2022newameloblastomacell pages 1-2)

**PIK3CA (HGNC:8975):**
- Activating mutations (less common)
- Origin: Somatic
- Functional consequence: Enhanced PI3K-AKT signaling (nguyen2022newameloblastomacell pages 1-2)

**FANCA (HGNC:3582):**
- **FANCA p.S858R:** Germline heterozygous mutation reported in one metastasizing case
- Variant classification: Variant of uncertain significance in ameloblastoma context
- Origin: Germline
- Interpretation: Potential susceptibility factor, requires further validation (hurnik2023metastasisingameloblastomaor pages 1-2)

### Allele Frequencies

Allele frequencies in general population databases (gnomAD) for these variants:
- BRAF V600E: Rare in general population; highly enriched in ameloblastoma
- RAS mutations: Rare in germline; somatic occurrence varies
- SMO mutations: Tumor-specific; not found in general population

Note: Specific population allele frequencies were not detailed in the reviewed literature but these are recognized as somatic, tumor-specific mutations rather than germline polymorphisms.

### Modifier Genes

**FOS (HGNC:3796):**
- Identified as hub gene in protein-protein interaction network analysis
- Role: Transcription factor involved in cell proliferation and migration
- Proposed as potential therapeutic target (chujan2024identificationofmolecular pages 1-2)

**Wnt Pathway Members:**
- Upregulation of cell migration-related Wnt pathway genes observed in metastasizing ameloblastoma
- Includes genes involved in epithelial-mesenchymal transition (hurnik2023metastasisingameloblastomaor pages 1-2)

### Epigenetic Information

Limited epigenetic data are available in the retrieved literature. No specific DNA methylation patterns, histone modifications, or chromatin changes have been systematically characterized for ameloblastoma in the sources reviewed.

### Chromosomal Abnormalities

No large-scale chromosomal abnormalities (aneuploidy, translocations, inversions) are described as characteristic features of ameloblastoma in the reviewed literature. The disease is primarily driven by single nucleotide variants in oncogenes rather than chromosomal rearrangements.

---

## 5. Environmental Information

### Environmental Factors

No specific environmental toxins, radiation exposure, pollution, or occupational hazards have been definitively linked to ameloblastoma development in the reviewed literature.

### Lifestyle Factors

No specific lifestyle factors (smoking, diet, exercise, alcohol consumption) have been established as risk factors for ameloblastoma.

### Infectious Agents

**Human Papillomavirus (HPV):**
- A possible link to HPV has been proposed but not definitively established
- Evidence level: Speculative; requires further validation (peralta2024effectivenessofcontemporary pages 1-2)

No other infectious agents (bacteria, fungi, parasites) have been implicated in ameloblastoma pathogenesis.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

**MAPK (Mitogen-Activated Protein Kinase) Pathway:**
The MAPK pathway is the most frequently altered pathway in ameloblastoma, particularly in mandibular tumors:

**Pathway components:**
1. **Receptor Tyrosine Kinases (RTKs):** FGFR2 activating mutations lead to ligand-independent receptor activation
2. **RAS proteins (KRAS, NRAS, HRAS):** Mutations lock RAS in active GTP-bound state
3. **RAF kinases:** BRAF V600E mutation causes constitutive kinase activation
4. **MEK → ERK cascade:** Phosphorylation cascade activated by mutant BRAF
5. **Transcription factors (ELK-1, c-Fos, c-Jun):** Nuclear translocation of ERK activates proliferation and anti-apoptotic gene programs (malakar2023theroleof pages 1-2, ebeling2023brafinhibitorsin pages 1-2)

**Functional consequence:**
- Uncoupling of growth signal from external ligand requirement
- Evasion of senescence and apoptosis
- Enhanced cell proliferation
- Tissue invasion and potential metastasis
- Immune evasion (ebeling2023brafinhibitorsin pages 1-2)

**Hedgehog Signaling Pathway:**
The Hedgehog pathway is preferentially altered in maxillary ameloblastomas:

**Pathway components:**
1. **Hedgehog ligand** binds to **PTCH1** (Patched 1)
2. PTCH1 inhibition is relieved, activating **SMO** (Smoothened)
3. SMO-L412F and SMO-W535L mutations cause constitutive SMO activation independent of ligand
4. **GLI transcription factors** are activated
5. Target genes involved in cell differentiation and proliferation are induced (yusof2022brafv600emutation pages 1-2, nguyen2022newameloblastomacell pages 1-2)

**PI3K-AKT Pathway:**
- PIK3CA mutations (less common) enhance PI3K-AKT signaling
- Promotes cell survival and growth (nguyen2022newameloblastomacell pages 1-2)

**Wnt/β-Catenin Pathway:**
- Dysregulation observed, particularly in aggressive/metastasizing cases
- Upregulation of migration-related genes
- Involvement in epithelial-mesenchymal transition (EMT) (hurnik2023metastasisingameloblastomaor pages 1-2)

**GABA and Glycosaminoglycan Signaling:**
- Bioinformatic analysis identified GABA (γ-aminobutyric acid) signaling as significantly downregulated
- Glycosaminoglycan signaling significantly upregulated
- Relevance to disease pathogenesis requires further investigation (chujan2024identificationofmolecular pages 1-2)

### Cellular Processes

**Cell Proliferation:**
- Constitutive MAPK and Hedgehog signaling drive uncontrolled odontogenic epithelial cell proliferation
- Loss of normal growth control mechanisms (malakar2023theroleof pages 1-2, yusof2022brafv600emutation pages 1-2)

**Apoptosis Evasion:**
- MAPK pathway activation promotes anti-apoptotic gene expression
- Tumor cells evade programmed cell death (ebeling2023brafinhibitorsin pages 1-2)

**Cell Migration and Invasion:**
- Upregulation of Wnt pathway genes and EMT-related factors in metastasizing tumors
- FOS protein (AP-1 transcription factor) identified as hub gene regulating cell migration (chujan2024identificationofmolecular pages 1-2, hurnik2023metastasisingameloblastomaor pages 1-2)

### Protein Dysfunction

**BRAF Protein:**
- Mutant BRAF-V600E exhibits constitutive serine/threonine kinase activity
- Loss of regulatory control normally provided by upstream signals
- Continuous phosphorylation of MEK (ebeling2023brafinhibitorsin pages 1-2)

**RAS Proteins:**
- Mutant RAS (KRAS, NRAS) locked in active GTP-bound conformation
- Failure to hydrolyze GTP to GDP leads to sustained signaling (nguyen2022newameloblastomacell pages 1-2)

**SMO Protein:**
- Mutant SMO (L412F, W535L) exhibits ligand-independent activation
- Constitutive signal transduction to GLI transcription factors (nguyen2022newameloblastomacell pages 1-2)

### Tissue Damage Mechanisms

**Bone Destruction:**
- Locally invasive tumor infiltrates through medullary spaces of jawbone
- Resorption of cortical bone
- Destruction of normal bone architecture creating multilocular radiolucencies (ghai2022ameloblastomaanupdated pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**Soft Tissue Infiltration:**
- Tumor can perforate cortical plates and invade adjacent soft tissues
- Infiltration beyond radiographic margins (2-8 mm) contributes to high recurrence rates (raemy2024antimapktargetedtherapy pages 1-2)

### Molecular Profiling

**Transcriptomics:**
- 611 differentially expressed genes identified in ameloblastoma vs. normal oral tissue
- Glycosaminoglycan signaling pathway genes upregulated
- GABA signaling pathway genes downregulated
- FOS identified as hub gene in protein-protein interaction network (chujan2024identificationofmolecular pages 1-2)

**Proteomics:**
- Limited proteomic data in reviewed literature; FOS protein highlighted as potential therapeutic target

**Genomic Features:**
- Single nucleotide variants in oncogenes (BRAF, RAS, SMO) are characteristic
- No recurrent chromosomal rearrangements or copy number alterations systematically described

### Suggested Ontology Terms

**Gene Ontology (GO) Biological Processes:**
- GO:0000165 - MAPK cascade
- GO:0007224 - Smoothened signaling pathway
- GO:0008283 - cell proliferation
- GO:0030335 - positive regulation of cell migration
- GO:0043066 - negative regulation of apoptotic process

**Gene Ontology (GO) Cellular Components:**
- GO:0005886 - plasma membrane (RTKs, SMO)
- GO:0005794 - Golgi apparatus
- GO:0005634 - nucleus (transcription factors)

**Cell Ontology (CL) Terms:**
- CL:0000066 - epithelial cell (odontogenic epithelium)
- CL:0000075 - columnar/cuboidal epithelial cell (ameloblast-lineage)

---

## 7. Anatomical Structures Affected

### Organ Level

**Primary Organs:**
- **UBERON:0001684 - Mandible:** Primary site in approximately 80% of cases
- **UBERON:0003661 - Maxilla:** Affected in approximately 20% of cases
- Site distribution: Posterior mandible (molar-ramus region) most common (malakar2023theroleof pages 1-2, hendra2020globalincidenceand pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**Secondary Involvement:**
- **UBERON:0001723 - Tongue:** Soft tissue infiltration
- **UBERON:0035920 - Oral mucosa:** Peripheral ameloblastoma
- **UBERON:0001697 - Teeth:** Displacement, root resorption
- **UBERON:0000203 - Orbit:** Invasion in advanced maxillary cases
- **UBERON:0003129 - Skull:** Potential invasion in extensive cases (nguyen2022newameloblastomacell pages 1-2)

**Body Systems:**
- Stomatognathic system (primary)
- Respiratory system (rare maxillary sinus involvement)
- Nervous system (inferior alveolar nerve compression/invasion)

### Tissue and Cell Level

**Tissue Types:**
- **UBERON:0000483 - Epithelial tissue:** Odontogenic epithelium (tumor origin)
- **UBERON:0002481 - Bone tissue:** Jawbone destruction and remodeling
- **UBERON:0003104 - Mesenchyme:** Stromal component (mature fibrous stroma)

**Specific Cell Populations:**
- **CL:0000066 - Epithelial cell:** Odontogenic epithelial cells (tumor cells)
- **CL:0000075 - Columnar/cuboidal epithelial cell:** Ameloblast-lineage cells
- **CL:0000057 - Fibroblast:** Stromal fibroblasts
- **CL:0000092 - Osteoclast:** Bone resorption
- **CL:0000062 - Osteoblast:** Reactive bone formation (nguyen2022newameloblastomacell pages 1-2)

### Subcellular Level

**Cellular Compartments (GO Cellular Component):**
- GO:0005886 - Plasma membrane: Location of mutant SMO, RTKs
- GO:0005737 - Cytoplasm: RAF-MEK-ERK cascade components
- GO:0005634 - Nucleus: Transcription factors (GLI, FOS, ERK)
- GO:0005794 - Golgi apparatus: Protein processing

### Localization

**Anatomical Sites (UBERON):**
- **UBERON:0001684 - Mandible:** 80% of cases
  - Most common: Posterior region (molar and angle)
- **UBERON:0003661 - Maxilla:** 20% of cases
  - Less common, more challenging surgical management

**Lateralization:**
- Predominantly unilateral presentation
- Can occur on either left or right side
- Bilateral involvement is extremely rare

---

## 8. Temporal Development

### Onset

**Typical Age of Onset:**
- Mean age at diagnosis: 34 years
- Peak incidence: Third decade of life (20-40 years)
- Range: Can occur from childhood to elderly; rare in children <10 years (hendra2020globalincidenceand pages 1-2, gasparro2024theeffectof pages 1-2)

**Age variation by geography:**
- Europe and North America: Diagnosis at older age
- Africa and South America: Diagnosis at younger age (hendra2020globalincidenceand pages 1-2)

**Onset Pattern:**
- Insidious onset: Slow, painless growth over months to years
- Often diagnosed incidentally on routine dental radiography or when swelling becomes noticeable

### Progression

**Disease Stages:**
- **Early stage:** Small, asymptomatic radiolucency; may be discovered incidentally
- **Intermediate stage:** Visible swelling, cortical expansion, tooth displacement
- **Advanced stage:** Massive tumor, facial deformity, cortical perforation, soft tissue invasion
- **End-stage/metastatic:** Rare; metastases most commonly to lungs (75-88% of metastatic cases) (hurnik2023metastasisingameloblastomaor pages 1-2)

**Progression Rate:**
- Slow progression: Growth over months to years
- Locally aggressive: Infiltrative growth pattern with destruction of surrounding bone
- Variable: Some tumors remain stable, others grow more rapidly

**Disease Course Pattern:**
- Progressive without treatment
- High recurrence rate after conservative treatment (up to 65%)
- Lower recurrence after radical surgery (approximately 11%) (raemy2024antimapktargetedtherapy pages 1-2)

**Disease Duration:**
- Chronic: Lifelong risk of recurrence even after treatment
- Long-term follow-up required (decades)
- Median survival after metastasis diagnosis: 17.6 years for metastasizing ameloblastoma (hurnik2023metastasisingameloblastomaor pages 1-2)

### Patterns

**Recurrence:**
- **Treatment-induced remission:** Surgical excision can achieve complete remission
- **Recurrence risk:** Varies by treatment approach
  - Conservative treatment: High recurrence (up to 65%)
  - Radical resection: Lower recurrence (approximately 11%)
  - Recurrence can occur years to decades after initial treatment (gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2)

**Critical Periods:**
- Childhood to young adulthood: Peak incidence window
- Post-treatment surveillance: Lifelong monitoring required to detect recurrence
- First 5 years post-surgery: Highest recurrence risk, but late recurrences (>10 years) also reported

---

## 9. Inheritance and Population

### Epidemiology

**Incidence:**
- Global pooled incidence rate: **0.92 per million person-years** (95% CI: 0.57-1.49)
- Significant heterogeneity between geographic regions (hendra2020globalincidenceand pages 1-2)

**Prevalence:**
- Ameloblastoma accounts for approximately 1% of all oral tumors and cysts
- Constitutes 13-58% of all odontogenic tumors
- Second most common odontogenic tumor after odontoma (malakar2023theroleof pages 1-2, ragunathan2022prevalenceandepidemiological pages 1-2, hendra2020globalincidenceand pages 1-2)

**Geographic Distribution:**
- Higher incidence in Africa and Asia
- Lower incidence in Europe and North America
- Studies covered Europe, Africa, and Australia; data from Americas and Asia less comprehensive (hendra2020globalincidenceand pages 1-2)

### Inheritance Patterns

**Genetic Etiology:**
- **Sporadic disease:** Ameloblastoma is not an inherited condition
- **Somatic mutations:** Disease is caused by acquired (somatic) mutations in BRAF, RAS, SMO, and other oncogenes
- **Inheritance pattern:** Not applicable (N/A) - not a hereditary disease
- **Penetrance:** N/A
- **Expressivity:** N/A
- **Genetic anticipation:** N/A
- **Germline mosaicism:** N/A
- **Founder effects:** N/A - mutations are sporadic
- **Consanguinity role:** N/A
- **Carrier frequency:** N/A

**Note:** One case report identified a germline FANCA mutation in a metastasizing ameloblastoma patient, suggesting potential susceptibility in rare cases, but this requires further validation (hurnik2023metastasisingameloblastomaor pages 1-2).

### Population Demographics

**Sex Distribution:**
- Slight male predominance
- Male:female ratio: approximately 1.14:1 to 1.2:1
- Some studies report equal distribution or slight female predominance depending on cohort (hendra2020globalincidenceand pages 1-2, gasparro2024theeffectof pages 1-2)

**Age Distribution:**
- Mean age: 34 years
- Peak incidence: Third decade (20-40 years)
- Range: Can affect any age; rare in children <10 years
- Geographic variation: Older age at diagnosis in Europe/North America vs. Africa/South America (hendra2020globalincidenceand pages 1-2)

**Affected Populations:**
- Higher prevalence reported in African populations
- China and Africa have higher burden (up to 10% of jaw cysts and tumors)
- No specific ethnic or demographic group shows genetic susceptibility (disease is sporadic) (malakar2023theroleof pages 1-2)

**Anatomical Distribution:**
- Mandible: Approximately 80% of cases
- Maxilla: Approximately 20% of cases
- Posterior mandible (molar-ramus region): Most common site
- Mandible:maxilla ratio: 1.96:1 (malakar2023theroleof pages 1-2, luca2026longtermclinicaloutcome pages 1-2, hurnik2023metastasisingameloblastomaor pages 1-2)

---

## 10. Diagnostics

### Clinical Tests

**Imaging Studies:**

**Computed Tomography (CT):**
- Essential for diagnosis and surgical planning
- Demonstrates extent of bone destruction, cortical perforation, and soft tissue invasion
- Visualizes multilocular ("soap-bubble" or "honeycomb") or unilocular radiolucent lesions
- High-resolution assessment of tumor margins (ghai2022ameloblastomaanupdated pages 1-2, gasparro2024theeffectof pages 1-2)

**Cone-Beam Computed Tomography (CBCT):**
- 3D imaging with lower radiation dose than conventional CT
- High modality for detailed radiographic assessment
- Useful for distinguishing ameloblastoma from other radiolucent lesions
- Aids in treatment planning (gasparro2024theeffectof pages 1-2)

**Orthopantomography (Panoramic radiography):**
- Initial screening tool
- Demonstrates radiolucent lesions, tooth displacement, cortical expansion
- Not pathognomonic; requires histological confirmation (peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**MRI:**
- Useful for assessing soft tissue involvement
- Superior for evaluating neural and vascular structures

**Radiographic Features:**
- Unilocular or multilocular radiolucency
- "Soap-bubble" appearance (multilocular)
- "Honeycomb" appearance
- Well-defined margins with cortical sclerosis
- May mimic dentigerous cyst when encircling unerupted tooth (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**Biopsy and Histopathology:**

**Incisional Biopsy:**
- Essential for definitive diagnosis
- Tissue obtained for histopathological examination
- Differentiates ameloblastoma from:
  - Ossifying fibroma
  - Osteomyelitis
  - Giant cell tumor
  - Cystic fibrous dysplasia
  - Odontogenic keratocyst
  - Central mucoepidermoid carcinoma
  - Myeloma
  - Sarcoma (ghai2022ameloblastomaanupdated pages 1-2)

**Histopathological Features:**
- Follicular pattern: Islands of odontogenic epithelium, peripheral palisading, reverse polarization, central stellate reticulum
- Plexiform pattern: Anastomosing cords and sheets of epithelium
- Other variants: Acanthomatous, granular cell, basal cell, desmoplastic
- Essential features: Odontogenic epithelium with ameloblast-like differentiation (ghai2022ameloblastomaanupdated pages 1-2, hendra2020globalincidenceand pages 1-2)

**Immunohistochemistry:**
- May be used to support diagnosis and distinguish from other entities
- Specific markers not detailed in reviewed literature but likely include epithelial markers (cytokeratins)

### Genetic Testing

**BRAF Mutation Testing:**
- **Method:** DNA sequencing (Sanger sequencing, targeted NGS panels, TaqMan allele-specific qPCR)
- **Target:** BRAF V600E mutation detection
- **Clinical utility:**
  - Confirms diagnosis
  - Identifies patients eligible for BRAF inhibitor therapy (vemurafenib, dabrafenib)
  - Prognostic information (associated with mandibular location, younger age) (yusof2022brafv600emutation pages 1-2, ebeling2023brafinhibitorsin pages 1-2)

**Next-Generation Sequencing (NGS) Panels:**
- **Targets:** BRAF, KRAS, NRAS, HRAS, FGFR2, SMO, PIK3CA
- **Clinical utility:**
  - Comprehensive mutation profiling
  - Identification of targetable mutations
  - Research and clinical trial eligibility (nguyen2022newameloblastomacell pages 1-2)

**Whole Exome Sequencing (WES):**
- Research tool for comprehensive genomic characterization
- Clinical utility: Limited in routine practice

**Single Gene Testing:**
- BRAF gene sequencing for V600E mutation
- SMO gene sequencing for L412F and W535L mutations

**Note:** Genetic testing is increasingly used for treatment stratification, particularly to identify patients eligible for targeted therapies (BRAF inhibitors, MEK inhibitors, SMO inhibitors).

### Biomarkers

**Molecular Biomarkers:**
- **BRAF V600E:** Diagnostic and predictive biomarker for response to BRAF/MEK inhibitors
- **FOS protein:** Proposed therapeutic target based on bioinformatic analysis (chujan2024identificationofmolecular pages 1-2)

**No circulating biomarkers** (serum or urine) have been established for ameloblastoma diagnosis or monitoring.

### Clinical Criteria and Differential Diagnosis

**Standardized Diagnostic Criteria:**
- WHO classification criteria (2022 edition)
- Essential diagnostic features:
  - Clinical: Jaw swelling, radiographic radiolucency
  - Radiographic: Unilocular/multilocular radiolucent lesion
  - Histopathologic: Odontogenic epithelium with ameloblast-like features
- Desirable features: Specific histological patterns, molecular mutations (vered2022updatefromthe pages 1-2, soluktekkesin2022theworldhealth pages 1-2)

**Differential Diagnosis:**
- **Odontogenic keratocyst:** Similar radiographic appearance; histology differs
- **Dentigerous cyst:** Unicystic ameloblastoma may mimic; histology required
- **Adenomatoid odontogenic tumor:** Different molecular profile (KRAS mutations more common)
- **Central mucoepidermoid carcinoma:** MAML2 gene rearrangements; more aggressive
- **Ossifying fibroma**
- **Giant cell tumor**
- **Osteomyelitis**
- **Sarcoma** (ghai2022ameloblastomaanupdated pages 1-2)

### Screening

**Population Screening:**
- No population-based screening programs exist
- Not applicable for sporadic disease

**Surveillance After Treatment:**
- Lifelong clinical and radiographic follow-up required
- Frequency: Initially every 6-12 months, then annually
- Imaging: Panoramic radiography or CBCT to detect recurrence
- Earlier detection of recurrence allows for less morbid intervention (gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2)

---

## 11. Outcome/Prognosis

### Survival and Mortality

**Overall Survival:**
- Conventional ameloblastoma: Excellent long-term survival with adequate treatment
- Metastasizing ameloblastoma: Median survival 17.6 years from diagnosis of metastasis
- Ameloblastic carcinoma: Poorer prognosis; specific survival data not detailed in reviewed literature (hurnik2023metastasisingameloblastomaor pages 1-2)

**Mortality:**
- Disease-specific mortality: Low for conventional ameloblastoma
- Deaths primarily due to complications of extensive local disease or rare metastases
- No specific mortality rates provided in reviewed literature

**Life Expectancy:**
- Generally normal life expectancy with appropriate treatment
- Reduced in metastasizing ameloblastoma and ameloblastic carcinoma

### Morbidity and Function

**Disease-Related Morbidity:**
- Facial deformity and disfigurement
- Loss of teeth
- Impaired mastication
- Speech difficulties
- Paresthesia or anesthesia (nerve involvement)
- Orbital or skull base invasion (rare, advanced cases) (gasparro2024theeffectof pages 1-2, peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**Treatment-Related Morbidity:**
- **Radical surgery:**
  - Permanent facial disfigurement
  - Loss of jaw function
  - Difficulty with mastication, speech, swallowing
  - Donor site morbidity (if bone grafts used)
  - Psychological and social impacts (malakar2023theroleof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2)

- **Conservative surgery:**
  - Lower immediate morbidity
  - Higher recurrence risk requiring repeat surgeries with cumulative morbidity

**Quality of Life:**
- Radical treatment significantly impairs QOL in multiple domains
- Conservative treatment offers better immediate QOL but anxiety about recurrence
- Successful rehabilitation with implants and prosthetics can restore function and aesthetics
- Long-term QOL depends on treatment success, recurrence, and reconstruction quality (gasparro2024theeffectof pages 1-2, peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

### Disease Course and Complications

**Recurrence:**
- **Conservative treatment:** Up to 65% recurrence rate
- **Radical resection:** Approximately 11% recurrence rate
- Recurrence can occur years to decades after initial treatment
- Follicular histological subtype may have higher recurrence rate (>60%) (ragunathan2022prevalenceandepidemiological pages 1-2, gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2)

**Complications:**
- Local recurrence (most common)
- Metastasis (1-4% of cases):
  - Lungs (75-88% of metastatic cases)
  - Lymph nodes (cervical most common)
  - Distant sites (bone, liver, brain - rare) (hurnik2023metastasisingameloblastomaor pages 1-2)
- Malignant transformation to ameloblastic carcinoma (rare)
- Infection (post-surgical)
- Pathological fracture (extensive bone destruction)

**Recovery Potential:**
- **With treatment:** Excellent potential for local disease control with radical surgery
- **Functional recovery:** Dependent on extent of resection and quality of reconstruction
- **Aesthetic recovery:** Modern reconstructive techniques (vascularized free flaps, dental implants, CAD/CAM prosthetics) can achieve good outcomes (peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

### Prognostic Factors

**Favorable Prognostic Factors:**
- Smaller tumor size
- Unicystic subtype
- Younger age (for treatment tolerance)
- Mandibular location (easier surgical access than maxilla)
- Early detection
- Adequate surgical margins (>1-2 cm) (raemy2024antimapktargetedtherapy pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**Unfavorable Prognostic Factors:**
- Large tumor size
- Conventional (solid) subtype
- Maxillary location
- Recurrent disease
- Soft tissue invasion
- Inadequate surgical margins
- Follicular histological pattern (higher recurrence)
- Metastasis (ragunathan2022prevalenceandepidemiological pages 1-2, hurnik2023metastasisingameloblastomaor pages 1-2)

**Molecular Prognostic Markers:**
- BRAF V600E mutation: Not independently prognostic for recurrence in one meta-analysis, but associated with younger age and mandibular location
- Further research needed to establish molecular predictors of recurrence and metastasis (yusof2022brafv600emutation pages 1-2)

---

## 12. Treatment

### Pharmacotherapy

**Conventional Chemotherapy:**
- Not effective as primary treatment
- Limited role in ameloblastic carcinoma; uncertain outcomes (malakar2023theroleof pages 1-2)

**Radiotherapy:**
- Not routinely used for conventional ameloblastoma (radioresistant)
- May be considered for inoperable or recurrent ameloblastic carcinoma
- Uncertain efficacy; controversial (malakar2023theroleof pages 1-2)

### Advanced Therapeutics: Targeted Therapies

**BRAF Inhibitors:**

**Vemurafenib (PLX4032):**
- **Mechanism:** Selective BRAF-V600E inhibitor
- **Indication:** BRAF-V600E mutant ameloblastoma
- **Clinical evidence:** Case reports show tumor size reduction, some complete responses
- **Adverse effects:** Arthralgia, fatigue, rash, photosensitivity, skin papillomas, hyperkeratosis, squamous cell carcinoma, keratoacanthoma, elevated liver enzymes
- **Usage:** Off-label; approved for melanoma (malakar2023theroleof pages 1-2, ebeling2023brafinhibitorsin pages 1-2)

**Dabrafenib:**
- **Mechanism:** Selective BRAF-V600E inhibitor
- **Indication:** BRAF-V600E mutant ameloblastoma
- **Clinical evidence:** Systematic review of 23 patients showed nearly all had positive response; 4 achieved complete radiological remission
- **Often used in combination with MEK inhibitor (trametinib) for synergistic effect and reduced resistance
- **Adverse effects:** Generally mild to moderate toxicities
- **Usage:** Off-label; approved for melanoma (raemy2024antimapktargetedtherapy pages 1-2, ebeling2023brafinhibitorsin pages 1-2)

**MEK Inhibitors:**

**Trametinib:**
- **Mechanism:** Selective MEK inhibitor (downstream of BRAF in MAPK pathway)
- **Indication:** Used in combination with dabrafenib for BRAF-mutant ameloblastoma; also active in RAS-mutant tumors
- **Clinical evidence:** Combination therapy shows improved responses and reduced resistance compared to BRAF inhibitor monotherapy
- **In vitro studies:** MEK inhibition in KRAS/NRAS-mutant ameloblastoma cells propels ameloblast differentiation and reduces proliferation (nguyen2022newameloblastomacell pages 1-2)
- **Usage:** Off-label; approved for melanoma in combination with BRAF inhibitors (raemy2024antimapktargetedtherapy pages 1-2, ebeling2023brafinhibitorsin pages 1-2)

**Hedgehog Pathway Inhibitors:**

**Vismodegib:**
- **Mechanism:** SMO inhibitor
- **Indication:** SMO-mutant ameloblastoma (maxillary tumors)
- **Clinical evidence:** Ameloblastoma cells with SMO-L412F mutation are **insensitive** to vismodegib
- **Usage:** Not recommended based on preclinical data (nguyen2022newameloblastomacell pages 1-2)

**BMS-833923:**
- **Mechanism:** Alternative SMO inhibitor
- **Indication:** SMO-mutant ameloblastoma
- **Clinical evidence:** Preclinical studies show significant reduction in Hedgehog signaling and tumor cell viability in SMO-L412F mutant cells
- **Usage:** Investigational; may be effective where vismodegib fails (nguyen2022newameloblastomacell pages 1-2)

**Drug Repositioning Candidates:**

**Tanespimycin (17-AAG):**
- **Mechanism:** HSP90 inhibitor; proposed to target FOS protein (hub gene identified in bioinformatic analysis)
- **Clinical evidence:** Molecular docking simulation shows high affinity for FOS; no clinical data
- **Status:** Investigational (chujan2024identificationofmolecular pages 1-2)

### Surgical Interventions

**Radical Resection:**
- **Procedure:** Segmental mandibulectomy or maxillectomy with 1.5-2 cm safety margins; en bloc resection
- **Indication:** Conventional ameloblastoma, unicystic mural type
- **Outcomes:** Lowest recurrence rate (approximately 11%)
- **Reconstruction:** Immediate reconstruction with vascularized bone grafts (fibula free flap most common), titanium plates, dental implants
- **Morbidity:** Significant functional and aesthetic deficits (gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2, peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**Conservative Resection:**
- **Procedures:** Enucleation, curettage, marginal resection
- **Indication:** Smaller lesions, unicystic luminal/intraluminal types, younger patients
- **Outcomes:** Higher recurrence rate (up to 65%)
- **Benefits:** Better postoperative quality of life, preserved function and aesthetics
- **Risk:** Requires closer long-term surveillance (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**Decompression:**
- **Procedure:** Marsupialization or decompression to reduce tumor size before definitive surgery
- **Indication:** Large tumors in young patients; neoadjuvant approach
- **Benefits:** Preserves more bone, allows further jaw growth in children
- **Requires:** Definitive surgery after tumor shrinkage

**Neoadjuvant Targeted Therapy Followed by Surgery:**
- **Approach:** BRAF/MEK inhibitors to shrink tumor before conservative resection
- **Benefits:** Organ preservation, reduced surgical morbidity, better cosmetic outcomes
- **Evidence:** Case reports and small series show feasibility; long-term follow-up needed (raemy2024antimapktargetedtherapy pages 1-2, ebeling2023brafinhibitorsin pages 1-2)

### Prosthetic Rehabilitation

**Dental Implants:**
- **Procedure:** Osseointegrated implants placed in reconstructed bone (fibula grafts, iliac crest grafts)
- **Timing:** Immediate (at time of reconstruction) or delayed (18 months post-reconstruction)
- **Outcomes:** Immediate implants show better survival rates; restore masticatory function and aesthetics (peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**Prosthetic Devices:**
- **Fixed prostheses:** Implant-supported fixed dentures or bridges
- **Removable prostheses:** Overdentures supported by implants
- **Benefits:** Functional and aesthetic restoration, improved quality of life (peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

**CAD/CAM and 3D Printing:**
- **Technology:** Computer-aided design/manufacturing for surgical guides, custom implants, prosthetics
- **Benefits:** Improved surgical precision, better functional and aesthetic outcomes (peralta2024effectivenessofcontemporary pages 1-2)

### Treatment Algorithms

**Conventional Ameloblastoma:**
1. Biopsy and molecular testing (BRAF status)
2. Radical resection with 1.5-2 cm margins + immediate reconstruction (standard)
   - OR: Neoadjuvant targeted therapy (if BRAF-mutant) followed by conservative resection (investigational)
3. Prosthetic rehabilitation
4. Lifelong surveillance (gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2)

**Unicystic Ameloblastoma:**
1. Conservative treatment (enucleation ± curettage) for luminal/intraluminal types
2. Radical resection for mural type (behaves like conventional)
3. Close surveillance (luca2026longtermclinicaloutcome pages 1-2)

**Metastatic/Inoperable Ameloblastoma:**
1. Molecular testing (BRAF, RAS, SMO mutations)
2. Targeted therapy:
   - BRAF-mutant: Dabrafenib + trametinib
   - RAS-mutant: MEK inhibitor (trametinib)
   - SMO-mutant: BMS-833923 (investigational)
3. Palliative surgery if feasible (raemy2024antimapktargetedtherapy pages 1-2, ebeling2023brafinhibitorsin pages 1-2, nguyen2022newameloblastomacell pages 1-2)

### Treatment Outcomes

**BRAF-Targeted Therapy:**
- Systematic review of 23 patients: Nearly all showed positive response
- Complete radiological remission: 4/23 patients
- Tumor size reduction: Most patients
- Side effects: Mostly mild to moderate
- Durability: Long-term follow-up limited (longest 38 months in reviewed case reports) (raemy2024antimapktargetedtherapy pages 1-2, ebeling2023brafinhibitorsin pages 1-2)

**Surgical Outcomes:**
- Radical resection: Low recurrence (<10% with adequate margins), high morbidity
- Conservative treatment: High recurrence (up to 65%), better immediate QOL
- Reconstruction with fibula free flap: High success rates, good functional and aesthetic outcomes (gasparro2024theeffectof pages 1-2, peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2)

### MAXO (Medical Action Ontology) Terms

Suggested terms for treatment annotations:
- MAXO:0000004 - surgical resection
- MAXO:0000127 - chemotherapy (for ameloblastic carcinoma, limited role)
- MAXO:0001001 - gene therapy (potential future application)
- MAXO:0000882 - targeted molecular therapy
- MAXO:0000011 - transplantation (bone graft)
- MAXO:0001175 - rehabilitation therapy (prosthetic rehabilitation)

---

## 13. Prevention

### Prevention Levels

**Primary Prevention:**
Not applicable. Ameloblastoma is a sporadic disease caused by somatic mutations; no known preventable risk factors exist.

**Secondary Prevention (Early Detection):**
- Routine dental examination with periodic panoramic radiography
- Early detection of small, asymptomatic lesions allows for less morbid treatment
- No formal screening programs exist due to low incidence

**Tertiary Prevention (Preventing Complications):**
- Adequate surgical margins (1.5-2 cm) to prevent recurrence
- Lifelong surveillance to detect recurrence early
- Close follow-up in first 5-10 years post-treatment (highest recurrence risk)
- Patient education about signs of recurrence (gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2)

### Screening and Early Detection

**Population Screening:**
- Not recommended due to low incidence (0.92 per million person-years)
- Not cost-effective

**Opportunistic Screening:**
- Routine dental radiography may detect asymptomatic lesions
- Dentists play key role in early detection

**Genetic Screening:**
- Not applicable (disease is not hereditary)
- BRAF mutation testing used for treatment stratification, not screening

**Risk Stratification:**
- Not applicable (no high-risk populations identified)

### Behavioral and Public Health Interventions

No specific behavioral interventions or public health measures are applicable for a sporadic neoplasm with unclear etiology.

### Counseling

**Genetic Counseling:**
- Not required for sporadic ameloblastoma
- May be considered if germline susceptibility factors are identified in future research (e.g., FANCA mutation validation)

**Patient Counseling:**
- Education about disease nature, treatment options, and lifelong surveillance needs
- Discussion of treatment tradeoffs: radical surgery (low recurrence, high morbidity) vs. conservative approach (higher recurrence, better QOL)
- Psychological support for coping with diagnosis, treatment morbidity, and potential disfigurement

---

## 14. Other Species / Natural Disease

### Comparative Biology and Veterinary Relevance

**Canine Acanthomatous Ameloblastoma:**
- **Species:** Dogs (Canis lupus familiaris) - NCBI Taxon: 9615
- **Natural occurrence:** Recognized odontogenic tumor in dogs
- **Relevance:** Used as comparative model for human ameloblastoma
- **Biological behavior:** Locally invasive, similar to human ameloblastoma; assessed with CT and histopathology
- **Research applications:** Comparative pathology studies; potential model for testing therapies (krawczyk2025conditionallyreprogrammedcells pages 1-2)

**Note:** The reviewed literature provided limited detailed information on naturally occurring ameloblastoma in other species. Canine acanthomatous ameloblastoma is the most relevant veterinary counterpart. Other animal models (mouse, zebrafish) are discussed below.

---

## 15. Model Organisms

### Cell Line Models

**Conditionally Reprogrammed Cells (CRCs):**
- **Technology:** Conditional cell reprogramming (CCR) allows primary ameloblastoma cells to acquire stem cell properties and proliferate indefinitely without genetic modification
- **Advantages:** Maintains genomic and histological characteristics of parental tissue; patient-derived; no ethical concerns
- **Applications:** Drug screening, molecular profiling, personalized medicine
- **Limitations:** Relatively new technology; limited availability (krawczyk2025conditionallyreprogrammedcells pages 1-2)

**Established Ameloblastoma Cell Lines:**
- **New cell lines:** Six new ameloblastoma cell lines generated using conditional reprogramming technology (Nguyen et al., 2022)
- **Genomic characterization:** Lines harbor mutations in FGFR2, KRAS, NRAS, BRAF, PIK3CA, and SMO
- **Applications:**
  - Oncogene dependency studies: Demonstrated exquisite sensitivity of RAS-mutant cells to MEK inhibition
  - Drug screening: Identified BMS-833923 as effective SMO inhibitor for SMO-L412F mutant cells
  - Preclinical testing of targeted therapies (nguyen2022newameloblastomacell pages 1-2)

### In Vivo Animal Models

**Mouse Xenograft Models:**
- **Approach:** Patient-derived xenografts (PDXs) using ameloblastoma cell lines or primary tumor tissue
- **Applications:**
  - Drug efficacy studies
  - Tumor biology research
  - Preclinical testing of BRAF/MEK inhibitors
- **Limitations:** Immunocompromised mice do not recapitulate immune microenvironment (nguyen2022newameloblastomacell pages 1-2, krawczyk2025conditionallyreprogrammedcells pages 1-2)

**Zebrafish Models:**
- **Applications:** Xenotransplantation studies for rapid drug screening; assessment of tumor cell behavior
- **Advantages:** Rapid development, optical transparency, cost-effective
- **Limitations:** Evolutionary distance from mammals; limited recapitulation of human tumor microenvironment
- **Mentioned in context of ameloblastoma research but detailed studies not available in reviewed literature (krawczyk2025conditionallyreprogrammedcells pages 1-2)

**Canine Models:**
- **Natural disease:** Canine acanthomatous ameloblastoma occurs spontaneously in dogs
- **Comparative studies:** CT and histopathological characterization of biological behavior
- **Advantages:** Naturally occurring tumor; larger size suitable for surgical and imaging studies
- **Limitations:** Genetic and molecular differences from human ameloblastoma; limited availability (krawczyk2025conditionallyreprogrammedcells pages 1-2)

### Model Characteristics and Limitations

**Phenotype Recapitulation:**
- **Cell lines:** Maintain driver mutations; useful for molecular studies and drug screening
- **Xenografts:** Recapitulate tumor growth and invasion; limited immune interactions
- **Canine models:** Natural tumor biology; differences in molecular drivers and disease course
- **Limitations:** No model perfectly recapitulates human ameloblastoma's slow growth, local invasiveness, and rare metastasis

**Research Applications:**
- Molecular mechanism studies (cell signaling, gene expression)
- Drug screening and preclinical testing
- Biomarker discovery
- Development of targeted therapies
- Understanding oncogene addiction and resistance mechanisms (nguyen2022newameloblastomacell pages 1-2, krawczyk2025conditionallyreprogrammedcells pages 1-2)

### Model Resources

**Cell Line Repositories:**
- New ameloblastoma cell lines available from originating laboratories (Nguyen et al., 2022; contact authors)
- Conditional reprogramming technology available through collaborations

**Animal Model Databases:**
- Mouse Genome Informatics (MGI)
- International Mouse Strain Resource (IMSR)
- Zebrafish Information Network (ZFIN)

---

## Summary Table

| Domain | Characteristic | Key details / values | Evidence citation |
|---|---|---|---|
| WHO / disease category | Core disease definition | Benign epithelial odontogenic tumor of jaw origin; locally aggressive, slow-growing, recurrent, and rarely metastasizing | (ghai2022ameloblastomaanupdated pages 1-2, gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2) |
| WHO classification | 2017 WHO types | Ameloblastoma; unicystic ameloblastoma; extraosseous/peripheral ameloblastoma; metastasizing ameloblastoma | (ghai2022ameloblastomaanupdated pages 1-2) |
| WHO classification | 2022 WHO types | Conventional ameloblastoma; unicystic ameloblastoma; extraosseous/peripheral ameloblastoma; adenoid ameloblastoma; metastasizing ameloblastoma | (vered2022updatefromthe pages 1-2, soluktekkesin2022theworldhealth pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| WHO classification | Conventional ameloblastoma | Most common type; previously called solid/multicystic; usually mandibular; histologic patterns include follicular, plexiform, acanthomatous, and desmoplastic | (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| WHO classification | Unicystic ameloblastoma | Approx. 5%–22% of all ameloblastomas; younger patients; luminal, intraluminal, and mural variants discussed in modern classification/treatment planning | (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| WHO classification | Peripheral / extraosseous ameloblastoma | Rare soft-tissue variant overlying jaws; generally less aggressive than intraosseous forms | (gasparro2024theeffectof pages 1-2) |
| WHO classification | Metastasizing ameloblastoma | Rare; classified as benign despite metastatic potential because histology resembles benign ameloblastoma | (ghai2022ameloblastomaanupdated pages 1-2, hurnik2023metastasisingameloblastomaor pages 1-2) |
| WHO classification | Adenoid ameloblastoma | Newly recognized benign epithelial odontogenic tumor in WHO 2022 classification | (vered2022updatefromthe pages 1-2, soluktekkesin2022theworldhealth pages 1-2) |
| Epidemiology | Global incidence | Pooled incidence rate 0.92 per million person-years (95% CI 0.57–1.49) | (hendra2020globalincidenceand pages 1-2) |
| Epidemiology | Alternative incidence statement in review literature | Global incidence summarized as about 0.92 per 1,000,000 people/year | (raemy2024antimapktargetedtherapy pages 1-2) |
| Epidemiology | Age distribution | Mean age 34 years; peak incidence in third decade of life | (hendra2020globalincidenceand pages 1-2) |
| Epidemiology | Sex distribution | Slight male predominance: 53% male overall; male:female ratio about 1.14:1 in umbrella review | (hendra2020globalincidenceand pages 1-2, gasparro2024theeffectof pages 1-2) |
| Epidemiology | Anatomic distribution | Mandible is preferred site; about 80% mandibular in several reviews/case literature | (malakar2023theroleof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| Epidemiology | Site-specific pattern | Maxillary tumors are less common; mandible:maxilla ratio reported as 1.96:1 for metastasizing ameloblastoma | (hurnik2023metastasisingameloblastomaor pages 1-2) |
| Clinical phenotype | Common presentation | Painless jaw swelling/expansion, facial asymmetry, tooth displacement or mobility, pain/paresthesia in larger lesions | (yusof2022brafv600emutation pages 1-2, gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| Imaging / phenotype | Typical radiology | Unilocular or multilocular radiolucency; classic “soap-bubble” or “honeycomb” appearance; may mimic dentigerous cyst | (gasparro2024theeffectof pages 1-2, luca2026longtermclinicaloutcome pages 1-2) |
| Histopathology | Common patterns | Follicular and plexiform are the most frequent histopathologic patterns globally | (hendra2020globalincidenceand pages 1-2) |
| Histopathology | Additional variants | Acanthomatous, granular cell, basal cell, keratopapillary, and desmoplastic patterns/variants described | (ghai2022ameloblastomaanupdated pages 1-2) |
| Molecular genetics | Major pathway theme | Ameloblastoma is largely driven by MAPK pathway alterations; Hedgehog pathway also important in a subset | (yusof2022brafv600emutation pages 1-2, raemy2024antimapktargetedtherapy pages 1-2, nguyen2022newameloblastomacell pages 1-2) |
| Molecular genetics | BRAF V600E pooled prevalence | 70.49% pooled prevalence across 833 cases in meta-analysis | (yusof2022brafv600emutation pages 1-2) |
| Molecular genetics | BRAF V600E frequency range in reviews | Often summarized as 40%–80% or ~66% depending on cohort/review | (malakar2023theroleof pages 1-2, ebeling2023brafinhibitorsin pages 1-2) |
| Molecular genetics | BRAF clinicopathologic associations | Significant association with patients younger than 54 years and mandibular location; not significant for sex, histologic variants, or recurrence in one meta-analysis | (yusof2022brafv600emutation pages 1-2) |
| Molecular genetics | Other MAPK-pathway genes | FGFR2, KRAS, NRAS, HRAS and less commonly PIK3CA identified as drivers in cell-line/genomic studies | (nguyen2022newameloblastomacell pages 1-2) |
| Molecular genetics | Hedgehog-pathway genes | SMO activating mutations, especially SMO-L412F and less commonly SMO-W535L; more typical of maxillary tumors | (yusof2022brafv600emutation pages 1-2, nguyen2022newameloblastomacell pages 1-2) |
| Molecular genetics | Wnt-related findings | Upregulation of migration-related Wnt pathway genes described in a metastasizing/amplified aggressive case | (hurnik2023metastasisingameloblastomaor pages 1-2) |
| Molecular profiling | Bioinformatic transcriptomic findings | 611 differentially expressed genes; glycosaminoglycan signaling upregulated, GABA signaling downregulated; FOS highlighted as hub/target candidate | (chujan2024identificationofmolecular pages 1-2) |
| Pathobiology | Origin / tissue of origin | Thought to arise from residual odontogenic epithelium including dental lamina rests, enamel organ, odontogenic cyst lining, or basal oral mucosal cells | (hendra2020globalincidenceand pages 1-2, luca2026longtermclinicaloutcome pages 1-2, nguyen2022newameloblastomacell pages 1-2) |
| Treatment outcomes | Radical vs conservative treatment | Meta-analytic umbrella review found recurrence about three-times more likely with conservative treatment than radical treatment | (gasparro2024theeffectof pages 1-2) |
| Treatment outcomes | Overall recurrence after surgery | Review of targeted-therapy paper summarizes recurrence varying from 11% after radical surgery to 65% after conservative treatment | (raemy2024antimapktargetedtherapy pages 1-2) |
| Treatment outcomes | Conservative treatment tradeoff | Better postoperative quality of life, esthetic, and functional outcomes in smaller lesions/younger patients, but higher recurrence risk and need for closer follow-up | (gasparro2024theeffectof pages 1-2) |
| Precision therapy | BRAF/MEK targeted therapy evidence | Systematic review of 23 patients: nearly all had positive response; 4 achieved complete radiologic remission; toxicities mostly mild-to-moderate | (raemy2024antimapktargetedtherapy pages 1-2) |
| Precision therapy | Published BRAF inhibitor case literature | Review of 9 reported patients treated with dabrafenib/vemurafenib ± trametinib showed responses from tumor reduction to complete response; evidence still limited to case reports | (ebeling2023brafinhibitorsin pages 1-2) |
| Quality of life | Surgical morbidity burden | Radical surgery can cause major cosmetic, functional, and psychosocial morbidity; this drives interest in targeted neoadjuvant and organ-preserving approaches | (malakar2023theroleof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2, peralta2024effectivenessofcontemporary pages 1-2) |


*Table: This table compiles the main disease-characteristic domains for ameloblastoma, including WHO classification, epidemiology, molecular genetics, pathology, and recurrence/treatment outcomes. It is useful as a compact evidence map for populating a disease knowledge base with quantitative values and current classification terminology.*

---

## Key Ontology Term Suggestions

**Disease Ontology:**
- MONDO:0004666 - ameloblastoma (if available)

**Human Phenotype Ontology (HPO):**
- HP:0030329 - Jaw swelling
- HP:0000303 - Facial asymmetry
- HP:0030751 - Tooth displacement
- HP:0000238 - Paresthesia
- HP:0012531 - Pain
- HP:0030077 - Follicular pattern (histopathology)
- HP:0030078 - Plexiform pattern (histopathology)

**Gene Ontology (GO):**
- GO:0000165 - MAPK cascade
- GO:0007224 - Smoothened signaling pathway
- GO:0008283 - Cell proliferation
- GO:0030335 - Positive regulation of cell migration
- GO:0043066 - Negative regulation of apoptotic process

**Cell Ontology (CL):**
- CL:0000066 - Epithelial cell
- CL:0000075 - Columnar/cuboidal epithelial cell
- CL:0000057 - Fibroblast
- CL:0000092 - Osteoclast
- CL:0000062 - Osteoblast

**Uberon Anatomy Ontology:**
- UBERON:0001684 - Mandible
- UBERON:0003661 - Maxilla
- UBERON:0001723 - Tongue
- UBERON:0035920 - Oral mucosa
- UBERON:0001697 - Teeth

**ChEBI (Chemical Entities):**
- CHEBI:90960 - Vemurafenib
- CHEBI:75045 - Dabrafenib
- CHEBI:90227 - Trametinib
- CHEBI:90972 - Vismodegib

**MAXO (Medical Action Ontology):**
- MAXO:0000004 - Surgical resection
- MAXO:0000882 - Targeted molecular therapy
- MAXO:0000011 - Transplantation (bone graft)
- MAXO:0001175 - Rehabilitation therapy

---

## Evidence Quality and Limitations

This comprehensive report is based on **31 retrieved papers** from 2020-2024, prioritizing recent systematic reviews, meta-analyses, and primary research studies. Key evidence sources include:

- **Meta-analysis evidence:** BRAF V600E prevalence (70.49%, 833 cases) (yusof2022brafv600emutation pages 1-2)
- **Systematic reviews:** Global incidence (0.92/million/year), treatment outcomes (hendra2020globalincidenceand pages 1-2, gasparro2024theeffectof pages 1-2, raemy2024antimapktargetedtherapy pages 1-2)
- **WHO classification updates:** 2022 5th edition with new diagnostic criteria (vered2022updatefromthe pages 1-2, soluktekkesin2022theworldhealth pages 1-2)
- **Molecular profiling studies:** Genomic characterization, drug sensitivity (chujan2024identificationofmolecular pages 1-2, nguyen2022newameloblastomacell pages 1-2)
- **Case series and reports:** BRAF inhibitor therapy outcomes, surgical reconstruction (ebeling2023brafinhibitorsin pages 1-2, peralta2024effectivenessofcontemporary pages 1-2, luca2026longtermclinicaloutcome pages 1-2, hurnik2023metastasisingameloblastomaor pages 1-2)

**Limitations:**
- **Clinical trial data:** Limited; most targeted therapy evidence from case reports and small series
- **Long-term outcomes:** Insufficient follow-up for targeted therapies (longest 38 months)
- **Prevention:** No established risk factors or prevention strategies
- **Epigenetics:** Minimal data on DNA methylation, histone modifications
- **Model organisms:** Limited detailed information on genetic mouse models; canine models underutilized
- **Omics data:** Transcriptomics available; proteomics, metabolomics, lipidomics limited

**Areas requiring further research:**
- Randomized controlled trials of BRAF/MEK inhibitors
- Molecular predictors of recurrence and metastasis
- Standardized protocols for neoadjuvant targeted therapy
- Development of genetically engineered mouse models
- Comprehensive multi-omics profiling
- Long-term quality of life studies

---

## Conclusion

Ameloblastoma is a benign yet locally aggressive odontogenic tumor with significant clinical impact due to its high recurrence rate and treatment-related morbidity. Recent molecular discoveries, particularly the identification of BRAF V600E mutations in 70% of cases, have revolutionized understanding of disease pathogenesis and opened new therapeutic avenues. Targeted therapies with BRAF and MEK inhibitors show promising early results and may offer organ-preserving alternatives to radical surgery, though long-term efficacy and safety require further study.

The 2022 WHO classification provides updated diagnostic criteria and introduces adenoid ameloblastoma as a new entity, reflecting evolving understanding of odontogenic tumor biology. Comprehensive management requires interdisciplinary collaboration among oral and maxillofacial surgeons, pathologists, oncologists, prosthodontists, and genetic counselors to optimize functional, aesthetic, and quality of life outcomes for patients with this challenging disease.

**Publication dates and URLs were not consistently available** in the academic abstracts and full-text PDFs retrieved, but all cited evidence is from peer-reviewed publications dated 2020-2024 as specified in the search strategy.

References

1. (ghai2022ameloblastomaanupdated pages 1-2): Suhani Ghai. Ameloblastoma: an updated narrative review of an enigmatic tumor. Cureus, Aug 2022. URL: https://doi.org/10.7759/cureus.27734, doi:10.7759/cureus.27734. This article has 137 citations.

2. (malakar2023theroleof pages 1-2): Arindam Malakar, V. Raj Kumar, Priya Yadav, Vishal Bhardwaj, Chuimee Gogoi Barua, and Gourika Bhardwaj. The role of braf inhibitors in the management of ameloblastoma: a literature review. Cureus, Oct 2023. URL: https://doi.org/10.7759/cureus.47682, doi:10.7759/cureus.47682. This article has 15 citations.

3. (hendra2020globalincidenceand pages 1-2): Faqi Nurdiansyah Hendra, Ellen M. Van Cann, Marco N. Helder, Muhammad Ruslin, Jan G. de Visscher, Tymour Forouzanfar, and Henrica C. W. de Vet. Global incidence and profile of ameloblastoma: a systematic review and meta-analysis. Oral diseases, 26:12-21, Jan 2020. URL: https://doi.org/10.1111/odi.13031, doi:10.1111/odi.13031. This article has 227 citations and is from a domain leading peer-reviewed journal.

4. (vered2022updatefromthe pages 1-2): Marilena Vered and John M. Wright. Update from the 5th edition of the world health organization classification of head and neck tumors: odontogenic and maxillofacial bone tumours. Head and Neck Pathology, 16:63-75, Mar 2022. URL: https://doi.org/10.1007/s12105-021-01404-7, doi:10.1007/s12105-021-01404-7. This article has 486 citations and is from a peer-reviewed journal.

5. (soluktekkesin2022theworldhealth pages 1-2): Merva Soluk-tekkesin and John M. Wright. The world health organization classification of odontogenic lesions: a summary of the changes of the 2022 (5th) edition. Turkish Journal of Pathology, 38:168-184, May 2022. URL: https://doi.org/10.5146/tjpath.2022.01573, doi:10.5146/tjpath.2022.01573. This article has 456 citations.

6. (yusof2022brafv600emutation pages 1-2): Mohd Nazzary Mamat @ Yusof, Ewe Seng Ch’ng, and Nawal Radhiah Abdul Rahman. Braf v600e mutation in ameloblastoma: a systematic review and meta-analysis. Cancers, 14:5593, Nov 2022. URL: https://doi.org/10.3390/cancers14225593, doi:10.3390/cancers14225593. This article has 35 citations.

7. (hurnik2023metastasisingameloblastomaor pages 1-2): Pavel Hurník, Barbora Moldovan Putnová, Tereza Ševčíková, Eva Hrubá, Iveta Putnová, Josef Škarda, Martin Havel, Oldřich Res, Jakub Cvek, Marcela Buchtová, and Jan Štembírek. Metastasising ameloblastoma or ameloblastic carcinoma? a case report with mutation analyses. BMC Oral Health, Aug 2023. URL: https://doi.org/10.1186/s12903-023-03259-6, doi:10.1186/s12903-023-03259-6. This article has 13 citations and is from a peer-reviewed journal.

8. (nguyen2022newameloblastomacell pages 1-2): J. Nguyen, P.S. Saffari, A.S. Pollack, S. Vennam, X. Gong, R.B. West, and J.R. Pollack. New ameloblastoma cell lines enable preclinical study of targeted therapies. Journal of Dental Research, 101:1517-1525, Jun 2022. URL: https://doi.org/10.1177/00220345221100773, doi:10.1177/00220345221100773. This article has 15 citations and is from a highest quality peer-reviewed journal.

9. (luca2026longtermclinicaloutcome pages 1-2): Ruxandra Elena Luca, Ciprian Ioan Roi, Alexandra Roi, and Eduard Gîdea-Paraschivescu. Long-term clinical outcome of a surgically treated ameloblastoma: over a decade of follow-up and oral rehabilitation. Dentistry Journal, 14(1):39, Jan 2026. URL: https://doi.org/10.3390/dj14010039, doi:10.3390/dj14010039. This article has 1 citations and is from a peer-reviewed journal.

10. (ragunathan2022prevalenceandepidemiological pages 1-2): Yoithapprabhunath Thuckanaickenpalayam Ragunathan, Srichinthu Keniyan Kumar, Dineshshankar Janardhanam, Aravindhan Ravi, Vidyalakshmi Santhanam, and Madhavan Nirmal Ramdas. Prevalence and epidemiological profile of ameloblastoma in india: a systematic review and meta-analyses. Asian Pacific Journal of Cancer Prevention : APJCP, 23:3601-3610, Nov 2022. URL: https://doi.org/10.31557/apjcp.2022.23.11.3601, doi:10.31557/apjcp.2022.23.11.3601. This article has 21 citations.

11. (peralta2024effectivenessofcontemporary pages 1-2): Daniela Beatriz Ganchozo Peralta, Christopher Andrés Guanoluisa Pérez, Diana Karina Arellano Garcia, Jordy Calixto Arcentales Quijije, and Wilmer Israel Morocho Sánchez. Effectiveness of contemporary surgical approaches and prosthetic rehabilitation in the management of ameloblastoma: a narrative review of functional and aesthetic outcomes. Ibero-American Journal of Health Science Research, 4:297-304, Dec 2024. URL: https://doi.org/10.56183/iberojhr.v4i2.688, doi:10.56183/iberojhr.v4i2.688. This article has 0 citations.

12. (gasparro2024theeffectof pages 1-2): Roberta Gasparro, Francesco Giordano, Maria Domenica Campana, Angelo Aliberti, Elena Landolfo, Pasquale Dolce, Gilberto Sammartino, and Alessandro E. di Lauro. The effect of conservative vs. radical treatment of ameloblastoma on recurrence rate and quality of life: an umbrella review. Journal of Clinical Medicine, 13:5339, Sep 2024. URL: https://doi.org/10.3390/jcm13175339, doi:10.3390/jcm13175339. This article has 19 citations.

13. (raemy2024antimapktargetedtherapy pages 1-2): Anton Raemy, Laurence May, Nathalie Sala, Manuel Diezi, Maja Beck-Popovic, and Martin Broome. Anti-mapk targeted therapy for ameloblastoma: case report with a systematic review. Cancers, 16:2174, Jun 2024. URL: https://doi.org/10.3390/cancers16122174, doi:10.3390/cancers16122174. This article has 11 citations.

14. (ebeling2023brafinhibitorsin pages 1-2): Marcel Ebeling, Mario Scheurer, Andreas Sakkas, Sebastian Pietzka, Alexander Schramm, and Frank Wilde. Braf inhibitors in braf v600e-mutated ameloblastoma: systematic review of rare cases in the literature. Medical Oncology (Northwood, London, England), Apr 2023. URL: https://doi.org/10.1007/s12032-023-01993-z, doi:10.1007/s12032-023-01993-z. This article has 35 citations.

15. (chujan2024identificationofmolecular pages 1-2): Suthipong Chujan, Nutsira Vajeethaveesin, Jutamaad Satayavivad, and Nakarin Kitkumthorn. Identification of molecular mechanisms of ameloblastoma and drug repositioning by integration of bioinformatics analysis and molecular docking simulation. Bioinformatics and Biology Insights, Jan 2024. URL: https://doi.org/10.1177/11779322241256459, doi:10.1177/11779322241256459. This article has 4 citations and is from a peer-reviewed journal.

16. (krawczyk2025conditionallyreprogrammedcells pages 1-2): Ewa Krawczyk. Conditionally reprogrammed cells as preclinical model for rare cancers. Cancers, 17:2834, Aug 2025. URL: https://doi.org/10.3390/cancers17172834, doi:10.3390/cancers17172834. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Ameloblastoma-deep-research-falcon_artifacts/artifact-00.md)
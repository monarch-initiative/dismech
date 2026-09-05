---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-12T10:09:48.018957'
end_time: '2026-08-12T10:19:53.706474'
duration_seconds: 605.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Non-Syndromic X-Linked Intellectual Disability
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 44
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Non-Syndromic_X-Linked_Intellectual_Disability-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Non-Syndromic X-Linked Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Non-Syndromic X-Linked Intellectual Disability** covering all of the
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
- **Disease Name:** Non-Syndromic X-Linked Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Non-Syndromic X-Linked Intellectual Disability** covering all of the
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


# Non-Syndromic X-Linked Intellectual Disability: Research Report

**Scope note.** Non-syndromic X-linked intellectual disability (NS-XLID) is not one molecularly uniform disease. It is an umbrella category for numerous X-linked neurodevelopmental disorders in which intellectual disability (ID) is the only *consistent* shared feature. Additional neurologic, behavioral, or dysmorphic findings may occur, but do not form a reproducible syndrome. Consequently, prevalence, penetrance, natural history, biomarkers, and treatment should ideally be curated at the causal-gene/variant level rather than assigned uniformly to the umbrella term. The boundary with syndromic XLID is increasingly regarded as blurred or biologically arbitrary. (tejada2020non‐syndromicxlinked pages 1-5, neri2018x‐linkedintellectualdisability pages 3-4, tejada2020non‐syndromicxlinked pages 12-15)

## Executive summary

* **Identifier:** MONDO:0019181. Open Targets associates this record with 25 targets, including **HCFC1, RPS6KA3, ARX, IQSEC2, OGT, BRWD3, IL1RAPL1, AFF2, TSPAN7, SLC9A7, CLCN4, DLG3, GDI1, SYP, HUWE1**, and others. This database list is not equivalent to a fully validated contemporary clinical gene panel. (OpenTargets Search: non-syndromic X-linked intellectual disability)
* **Definition:** ID begins during development and impairs intellectual and adaptive functioning. In NS-XLID, ID is the only common feature across affected individuals; variable speech delay, hypotonia, epilepsy, autistic traits, or minor dysmorphism may coexist. (tejada2020non‐syndromicxlinked pages 1-5)
* **Etiology:** Rare germline X-chromosomal sequence variants, repeat expansions, copy-number/structural variants, or occasionally mosaic variants disrupt diverse but interconnected neuronal pathways. A 2020 review retained 44 NS-XLID genes after excluding questioned associations; 25 of those also caused syndromic presentations. It reported 56 implicated NS-XLID genes under a broader historical definition and 146 XLID genes overall. (tejada2020non‐syndromicxlinked pages 23-25, tejada2020non‐syndromicxlinked pages 1-5)
* **Epidemiology:** XLID broadly is estimated to account for approximately 5–10% of ID in males; one 2023 paper cited a prevalence of 1 in 600–1,000 males. These are **not** reliable prevalence estimates for strict NS-XLID itself, for which no robust population prevalence or incidence was identified. (luca2020challengesinmolecular pages 1-2, mir2023wholeexomesequencing pages 1-2)
* **Diagnosis:** Clinical assessment, three-generation pedigree, Fragile X testing where indicated, copy-number analysis, and preferably trio exome or genome sequencing with segregation and phenotype-aware reinterpretation. RNA or biochemical assays can resolve selected variants. (luca2020challengesinmolecular pages 1-2, ibarluzea2020targetednextgenerationsequencing pages 1-3)
* **Treatment:** No disease-group-level disease-modifying treatment is established. Current implementation is genotype-informed surveillance plus developmental, educational, speech-language, occupational, physical, behavioral, psychiatric, and seizure care. Gene therapy, controlled X-reactivation, and synapse/circuit-directed interventions remain experimental. (martinez2024overcominggeneticand pages 7-8, martinez2024overcominggeneticand pages 8-10, martinez2024overcominggeneticand pages 6-7)

The following ontology-ready summary complements the narrative report.

| Domain | Knowledge-base content | Suggested ontology terms/IDs | Evidence caveat |
|---|---|---|---|
| Disease identity | Non-syndromic X-linked intellectual disability (NS-XLID) is a genetically heterogeneous X-linked neurodevelopmental disease group in which intellectual disability is the only consistent shared feature; additional neurologic, behavioral, or dysmorphic findings may occur but are variable and gene-/family-specific. Exact disease-level knowledge is aggregated from literature/reviews and should not be overgeneralized to every gene-defined subtype. (OpenTargets Search: non-syndromic X-linked intellectual disability, tejada2020non‐syndromicxlinked pages 1-5, neri2018x‐linkedintellectualdisability pages 3-4) | MONDO:0019181; term label: non-syndromic X-linked intellectual disability | “Nonsyndromic” does **not** mean absence of all other findings; rather, no consistent syndromic pattern across cases. Scope overlaps with syndromic XLID for many genes. |
| Synonyms / scope | Non-specific X-linked intellectual disability; nonsyndromal X-linked intellectual disability; NS-XLID; historical: non-syndromic X-linked mental retardation. (tejada2020non‐syndromicxlinked pages 1-5, neri2018x‐linkedintellectualdisability pages 3-4) | term suggestions; verify release | Historical terminology in older papers may use outdated language. |
| Core phenotype | Intellectual disability is the defining phenotype, often mild to severe depending on gene/variant. (tejada2020non‐syndromicxlinked pages 1-5) | HP:0001249 Intellectual disability | Frequency at disease-group level cannot be meaningfully quantified because NS-XLID aggregates many disorders. |
| Core phenotype | Developmental delay / global developmental delay may precede formal ID diagnosis in childhood. (khayat2019arecurrentmissense pages 3-4, mir2023wholeexomesequencing pages 1-2, mir2023wholeexomesequencing pages 2-4) | HP:0001263 Global developmental delay; HP:0011344 Severe global developmental delay | More typical in pediatric case series; adult historical families may be described primarily as ID. |
| Core phenotype | Speech/language delay or poor/absent speech is common in several gene-specific forms. (khayat2019arecurrentmissense pages 3-4, mir2023wholeexomesequencing pages 1-2, mir2023fourfamilieswith pages 9-11, mir2023wholeexomesequencing pages 4-6) | HP:0000750 Delayed speech and language development; HP:0001344 Expressive language delay | Strongly gene-dependent; not universal across all NS-XLID genes. |
| Core phenotype | Hypotonia / muscle weakness reported in subsets, including SLC9A7-related cases. (khayat2019arecurrentmissense pages 3-4) | HP:0001252 Hypotonia; HP:0001324 Muscle weakness | Variable and not specific; may reflect particular gene mechanisms. |
| Core phenotype | Seizures/epilepsy occur in some NS-XLID genes (for example IQSEC2-, GLRA2-, ATP2B3-related cases) but are inconsistent at disease-group level. (tejada2020non‐syndromicxlinked pages 12-15, mir2023wholeexomesequencing pages 1-2, mir2023fourfamilieswith pages 9-11, mir2023wholeexomesequencing pages 4-6) | HP:0001250 Seizure; HP:0002123 Generalized myoclonic seizure (term suggestion; verify release if subtyped) | Presence of seizures can shift some cases toward broader neurodevelopmental syndromes; use gene-level assertion when possible. |
| Core phenotype | Autism spectrum features / autistic traits / behavioral abnormalities / psychiatric problems may occur in subsets. (tejada2020non‐syndromicxlinked pages 12-15, tejada2020non‐syndromicxlinked pages 19-23, mir2023wholeexomesequencing pages 1-2) | HP:0000729 Autism; HP:0000708 Behavioral abnormality | HPO choice should be tailored to reported feature (autism, aggression, hyperactivity, anxiety, etc.). |
| Anatomy | Primary organ/system affected: brain, especially forebrain/cerebral cortex and synaptic networks underlying cognition and behavior. (tejada2020non‐syndromicxlinked pages 5-8, tejada2020non‐syndromicxlinked pages 8-12, martinez2024overcominggeneticand pages 1-2) | UBERON:0000955 brain; UBERON:0000956 cerebral cortex | Disease-level anatomy is inferred from shared neurodevelopmental biology rather than uniform lesion localization. |
| Tissue / cell types | Principal affected tissue: nervous tissue; relevant cell types include excitatory neurons, inhibitory neurons, and broader cortical/hippocampal neuronal populations. (tejada2020non‐syndromicxlinked pages 8-12, martinez2024overcominggeneticand pages 7-8, martinez2024overcominggeneticand pages 11-12, martinez2024overcominggeneticand pages 1-2) | CL:0000540 neuron; term suggestions: excitatory neuron, inhibitory neuron, cortical neuron, hippocampal neuron; verify release | Exact CL subtype should match gene/mechanism-specific evidence; many papers infer rather than directly prove target cell types. |
| Subcellular compartments | Recurrently implicated compartments include synapse, presynaptic vesicle, postsynaptic density, dendritic spine, nucleus/chromatin, Golgi/TGN/post-Golgi vesicles, endosome, and mitochondrion for some genes. (tejada2020non‐syndromicxlinked pages 23-25, tejada2020non‐syndromicxlinked pages 5-8, tejada2020non‐syndromicxlinked pages 8-12, khayat2019arecurrentmissense pages 3-4, khayat2019arecurrentmissense pages 2-3, khayat2019arecurrentmissense pages 8-9) | GO:0045202 synapse; GO:0098793 presynapse; GO:0014069 postsynaptic density; GO:0043197 dendritic spine; GO:0005654 nucleoplasm; GO:0005794 Golgi apparatus; GO:0005802 trans-Golgi network; GO:0005768 endosome; GO:0005739 mitochondrion | Use gene-level annotation for highest confidence; not every compartment applies to every NS-XLID gene. |
| Major mechanism | Synaptic function/plasticity defects: vesicle trafficking, neurotransmitter release, postsynaptic signaling, receptor trafficking, dendritic spine regulation. Representative genes include GDI1, IL1RAPL1, SYN1, SYP, DLG3, GRIA3, IQSEC2, NLGN3, NLGN4, RAB39B, OPHN1, PAK3, TSPAN7. (tejada2020non‐syndromicxlinked pages 23-25, tejada2020non‐syndromicxlinked pages 12-15, tejada2020non‐syndromicxlinked pages 8-12) | GO:0007268 chemical synaptic transmission; GO:0016079 synaptic vesicle exocytosis; GO:0048167 regulation of synaptic plasticity | Shared pathway category is review-derived; representative genes vary in evidence strength. |
| Major mechanism | Cytoskeleton / Rho- and Arf-family GTPase signaling affecting dendrites and spines. Representative genes include IQSEC2, OPHN1, PAK3, FGD1. (tejada2020non‐syndromicxlinked pages 12-15, tejada2020non‐syndromicxlinked pages 8-12) | GO:0032956 regulation of actin cytoskeleton organization; GO:0007015 actin filament organization | Often downstream of synaptic signaling; phenotype correlations remain incomplete. |
| Major mechanism | Transcription, chromatin, RNA processing, translation regulation. Representative genes include HCFC1, KDM5C, MECP2, MED12, PQBP1, RPS6KA3, THOC2, UPF3B, ZNF711, AFF2, ATRX, DDX3X. (tejada2020non‐syndromicxlinked pages 23-25, tejada2020non‐syndromicxlinked pages 5-8, tejada2020non‐syndromicxlinked pages 19-23) | GO:0006357 regulation of transcription by RNA polymerase II; GO:0006338 chromatin remodeling; GO:0000398 mRNA splicing; GO:0000184 nuclear-transcribed mRNA catabolic process, nonsense-mediated decay | Many of these genes also cause syndromic XLID; classify carefully at variant/disorder level. |
| Major mechanism | Ubiquitination / proteostasis dysregulation, including neuronal proliferation/differentiation and substrate turnover. Representative genes include HUWE1, MID2, RLIM, USP9X. (tejada2020non‐syndromicxlinked pages 23-25, tejada2020non‐syndromicxlinked pages 19-23) | GO:0016567 protein ubiquitination; GO:0032436 positive regulation of proteasomal ubiquitin-dependent protein catabolic process | Evidence is stronger for some genes than others; downstream neuronal effects remain incompletely resolved. |
| Major mechanism | Membrane transport / ion homeostasis / metabolism. Representative genes include SLC6A8, CLCN4, SLC16A2, SLC25A5, NDUFA1, ACSL4, ATP2B3, GLRA2. (tejada2020non‐syndromicxlinked pages 25-28, mir2023wholeexomesequencing pages 1-2, mir2023wholeexomesequencing pages 4-6) | GO term suggestions: transmembrane transport, ion homeostasis, creatine transmembrane transporter activity, mitochondrial ATP transport; verify release | Some genes produce broader syndromic/metabolic phenotypes outside strict NS-XLID. |
| Major mechanism | Golgi/TGN pH regulation and glycosylation defects. Best current gene-specific example: SLC9A7 p.Leu515Phe causing altered Golgi acidification and aberrant glycosylation with abnormal transferrin N-glycosylation. (khayat2019arecurrentmissense pages 3-4, khayat2019arecurrentmissense pages 2-3, khayat2019arecurrentmissense pages 8-9) | GO:0051453 regulation of intracellular pH; GO:0006486 protein glycosylation; GO:0005794 Golgi apparatus; GO:0005802 trans-Golgi network | Mechanism currently best established for SLC9A7-related NS-XLID, not the entire disease group. |
| Causal genes / heterogeneity | Highly heterogeneous disorder group. Review-level counts reported ~56 genes implicated in NS-XLID, with many overlapping syndromic genes; 146 total XLID genes reported by 2020 review, and disease-target databases list additional associated genes. (tejada2020non‐syndromicxlinked pages 1-5, tejada2020non‐syndromicxlinked pages 23-25, OpenTargets Search: non-syndromic X-linked intellectual disability) | Gene symbols only; disease-group curation should link to gene-specific disorder records where possible | Gene lists change with reclassification; some historical genes remain uncertain/questioned. |
| Inheritance | Usually X-linked inheritance affecting males more often; female carriers may be unaffected or mildly/variably affected, influenced by X-chromosome inactivation and gene escape status. (tejada2020non‐syndromicxlinked pages 1-5, luca2020challengesinmolecular pages 1-2, martinez2024overcominggeneticand pages 1-2, chaves2023skewedxchromosomeinactivation pages 1-5) | HP:0001417 X-linked inheritance; term suggestion: X-linked recessive inheritance; verify release | Some genes act through dominant, de novo, mosaic, or dosage-sensitive mechanisms in females. |
| Diagnostics | Recommended workup typically includes clinical evaluation/family history, FMR1 testing, chromosomal microarray, and next-generation sequencing (panel, exome, or genome) with segregation analysis and variant interpretation under ACMG/AMP. (luca2020challengesinmolecular pages 1-2, ibarluzea2020targetednextgenerationsequencing pages 1-3) | NCIT term suggestions: Genetic Testing, Chromosomal Microarray Analysis, Whole Exome Sequencing, Whole Genome Sequencing; verify release | No single disease-specific laboratory biomarker exists for NS-XLID as a group. |
| Diagnostics | Exome/genome sequencing now outperforms CMA/panels for unexplained GDD/ID broadly; targeted XLID panels may still help in suggestive pedigrees. In one XLID panel study, 17 candidate variants were identified in 16/61 unrelated males after negative karyotype/FMR1 testing. (ibarluzea2020targetednextgenerationsequencing pages 1-3) | NCIT term suggestions: Whole Exome Sequencing, Next-Generation Sequencing Panel; verify release | Yield figures vary by cohort design and inclusion criteria; many statistics are for GDD/ID broadly, not NS-XLID alone. |
| Diagnostics | Functional follow-up may include RNA studies, biochemical assays, and gene-specific tests; example: urine creatine/creatinine ratio and brain MRS for SLC6A8 deficiency; transferrin glycosylation for SLC9A7-related disease. (tejada2020non‐syndromicxlinked pages 12-15, ibarluzea2020targetednextgenerationsequencing pages 1-3, khayat2019arecurrentmissense pages 2-3) | LOINC/NCIT term suggestions; CHEBI: creatine (verify ontology mapping in KB) | These are gene-specific adjuncts, not universal NS-XLID diagnostics. |
| Diagnostics in females | Extreme skewing of X-inactivation in females with idiopathic ID can enrich for pathogenic findings; in one 2023 cohort, 11/136 informative women (8%) had >=90% skewing and WES found pathogenic variants in 8/11 (73%). (chaves2023skewedxchromosomeinactivation pages 1-5) | term suggestions: skewed X-chromosome inactivation; verify release | Evidence pertains to idiopathic ID in females, not a diagnostic criterion for all NS-XLID. |
| Treatment / management | No disease-modifying therapy is established for NS-XLID as a disease group. Current care is supportive and individualized: developmental therapies, speech-language therapy, special education, behavioral/psychiatric management, and antiseizure treatment when indicated. (luca2020challengesinmolecular pages 1-2, martinez2024overcominggeneticand pages 7-8, martinez2024overcominggeneticand pages 8-10) | NCIT term suggestions: Supportive Care, Speech Therapy, Occupational Therapy, Physical Therapy, Special Education, Anticonvulsant Therapy; verify release | Management is phenotype- and gene-specific; evidence base often extrapolated from broader neurodevelopmental care. |
| Advanced therapeutics | Research directions include gene therapy, selective X-reactivation, dosage-controlled transgene strategies, and circuit/synapse-targeted interventions; these remain experimental and are mostly not NS-XLID-specific. (martinez2024overcominggeneticand pages 7-8, martinez2024overcominggeneticand pages 8-10, martinez2024overcominggeneticand pages 6-7, martinez2024overcominggeneticand pages 11-12) | NCIT term suggestions: Gene Therapy, CRISPR-based Gene Editing, RNA Therapy; verify release | Most therapeutic development is for specific syndromic X-linked NDDs; translation to NS-XLID is unresolved. |
| Prevention / counseling | Genetic counseling, cascade testing, carrier testing, reproductive counseling, and when a familial pathogenic variant is known, options such as prenatal diagnosis or preimplantation genetic testing. (luca2020challengesinmolecular pages 1-2, mir2023wholeexomesequencing pages 1-2, mir2023wholeexomesequencing pages 4-6) | NCIT term suggestions: Genetic Counseling, Carrier Screening, Prenatal Genetic Testing, Preimplantation Genetic Testing; verify release | Prevention is primarily genetic/reproductive rather than environmental because NS-XLID is a monogenic/heterogeneous genetic disease group. |
| Epidemiology | Intellectual disability overall affects ~1% of the population; males are affected more often. XLID accounts for an estimated 5-10% of ID in males, but disease-specific prevalence for NS-XLID is not well established because it comprises many rare gene-defined disorders. (tejada2020non‐syndromicxlinked pages 1-5, luca2020challengesinmolecular pages 1-2, mir2023wholeexomesequencing pages 1-2) | No exact disease-level prevalence ID recommended | Avoid presenting a single prevalence for MONDO:0019181 as if it were a uniform entity. |
| Natural history / prognosis | Usually childhood-onset and lifelong. Course is generally chronic/stable in terms of core cognitive impairment, while associated features (seizures, behavior, speech limitations) depend on the causal gene and comorbidities. (tejada2020non‐syndromicxlinked pages 1-5, khayat2019arecurrentmissense pages 3-4, mir2023wholeexomesequencing pages 1-2) | term suggestions: childhood onset; chronic course; verify release | Prognosis cannot be generalized across all NS-XLID subtypes. |
| Models | Model systems include mouse models, human iPSCs, and cellular assays; current 2024 work emphasizes mosaic female models, reporter-based strategies, dual-eGRASP/synaptic assays, electrophysiology, imaging, and human iPSC approaches to resolve circuit heterogeneity. (martinez2024overcominggeneticand pages 7-8, martinez2024overcominggeneticand pages 8-10, martinez2024overcominggeneticand pages 11-12, martinez2024overcominggeneticand pages 1-2) | NCIT term suggestions: Disease Model, Induced Pluripotent Stem Cell, Mouse Model; CL:0000000 cell (generic, term suggestion for specific derived neurons); verify release | Much model literature is from broader XLID/X-linked NDDs, not exclusively strict NS-XLID. |
| Exemplary gene-specific subtype | SLC9A7-related NS-XLID: recurrent p.Leu515Phe reported in two unrelated families; associated with moderate-severe ID, speech delay, hypotonia/muscle weakness, reserved personality, clinodactyly; mechanism involves TGN/post-Golgi alkalinization and abnormal glycosylation. (khayat2019arecurrentmissense pages 3-4, khayat2019arecurrentmissense pages 2-3, khayat2019arecurrentmissense pages 8-9, khayat2019arecurrentmissense pages 45-45) | Gene: SLC9A7; GO/UBERON/HPO terms above as applicable | Useful exemplar of mechanistic depth, but not representative of all NS-XLID mechanisms. |


*Table: This table provides a compact, ontology-ready summary of nonsyndromic X-linked intellectual disability for knowledge-base use. It emphasizes heterogeneous gene-dependent biology and highlights that intellectual disability is the only consistent shared feature across the disease group.*

## 1. Disease information

### Definition and identifiers

NS-XLID—also called **non-specific XLID**, **nonsyndromal XLID**, or historically **X-linked nonsyndromic mental retardation**—is an early-onset genetic neurodevelopmental disease group. “Non-syndromic” does not mean that every patient has isolated ID; it means no additional feature is consistently shared across the relevant family or disorder definition. The dedicated review states: **“Non-Specific or Non-Syndromic Intellectual Disability (NS-XLID) [is that] where the only common feature is ID.”** (tejada2020non‐syndromicxlinked pages 1-5)

* **MONDO:** MONDO:0019181.
* **OMIM:** No single umbrella OMIM phenotype number was established in the retrieved evidence. Historically, pedigrees were assigned **MRX/IDX locus numbers**; the 2018 update described 105 nonsyndromal families with IDX numbers, 67 with cloned genes, 33 mapped but unresolved, and five reserved numbers. Individual causal genes and phenotypes have separate OMIM records. (neri2018x‐linkedintellectualdisability pages 3-4)
* **Orphanet, MeSH, ICD-10/ICD-11:** No unique, validated NS-XLID-specific code was established from the retrieved literature. Clinical coding usually uses intellectual-developmental-disorder and/or genetic-etiology codes, while the molecular diagnosis is recorded separately. These mappings should be verified directly against the current releases before production use.
* **Data provenance:** The report is principally **aggregated disease-level evidence** from reviews, databases, family studies, and experimental papers—not individual EHR data. Patient counts are stated where primary cohorts were available.

The historical syndromic/non-syndromic division is unstable: different variants in one gene—and sometimes the same familial variant—can produce either label because of variant location, dosage, genetic background, X-inactivation, and other modifiers. (tejada2020non‐syndromicxlinked pages 1-5, tejada2020non‐syndromicxlinked pages 12-15)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factors

The primary cause is a **germline pathogenic or likely pathogenic X-chromosomal variant**. Relevant classes include missense, nonsense, frameshift, splice-altering, repeat-expansion, exon/gene deletion or duplication, and larger structural variants. Pathogenic mechanisms include loss of function, altered dosage, impaired protein interactions, and occasional apparent gain of function. Most variants are constitutionally inherited or de novo; somatic/gonadal mosaicism is possible but not quantified for the umbrella disease.

Representative clinically supported genes include **AFF2, ARX, ATRX, BRWD3, CLCN4, DLG3, FTSJ1, GDI1, HCFC1, HUWE1, IL1RAPL1, IQSEC2, KDM5C, MECP2, MED12, NLGN3, NLGN4X, OGT, OPHN1, PAK3, RAB39B, RPS6KA3, SLC6A8, SLC9A7, SYP, SYN1, TSPAN7, UPF3B**, and **ZNF711**. Gene validity and the “non-syndromic” designation require periodic reassessment; older candidate lists contained associations later questioned by population sequencing. (OpenTargets Search: non-syndromic X-linked intellectual disability, tejada2020non‐syndromicxlinked pages 23-25, tejada2020non‐syndromicxlinked pages 1-5)

A recent human example is the October 2023 WES study of nine affected males from four Iranian families. It identified likely pathogenic **ZDHHC9 c.566T>C (p.Leu189Pro), GLRA2 c.1048C>T (p.Arg350Cys), ATP2B3 c.2541C>G (p.Asp847Glu)** and previously reported pathogenic **L1CAM c.925G>A (p.Glu309Lys)** variants. The three novel variants were classified under ACMG/AMP criteria and segregated in X-linked pedigrees. [BMC Medical Genomics, October 2023, DOI: https://doi.org/10.1186/s12920-023-01680-y]. (mir2023wholeexomesequencing pages 1-2, mir2023fourfamilieswith pages 9-11, mir2023wholeexomesequencing pages 4-6)

### Risk factors

* **Genetic:** male hemizygosity; a carrier mother; affected maternal male relatives; a known familial pathogenic variant; X-chromosome structural rearrangement; or de novo mutation.
* **Female expression:** skewed X-chromosome inactivation (XCI), escape from XCI, dosage sensitivity, mosaicism, and variant mechanism influence risk and severity. Approximately 15–30% of X-linked genes can escape XCI, depending on tissue and cell type. (martinez2024overcominggeneticand pages 1-2)
* **Family history:** absence of family history does not exclude XLID because de novo variants, small families, reduced female expression, and mosaicism are common diagnostic complications. (luca2020challengesinmolecular pages 1-2)
* **Environmental/lifestyle/infectious:** no environmental exposure, lifestyle behavior, toxin, or pathogen is a primary cause of monogenic NS-XLID. General prenatal/perinatal insults remain differential causes of ID, not established causes of genetically confirmed NS-XLID.

### Protective factors and gene–environment interaction

No reproducible protective allele, diet, lifestyle, medication, or environmental exposure has been established for NS-XLID as a group. Favorable XCI that preferentially silences the mutant allele may reduce expression in heterozygous females, but is tissue-specific and is better considered a modifier than a dependable protective factor. The literature suggests environmental or genetic background can modify phenotype even within a family, but no validated quantitative gene–environment interaction was identified. (tejada2020non‐syndromicxlinked pages 1-5)

## 3. Phenotypes

**Defining phenotype:** developmental-onset impairment of intellectual and adaptive functioning (**HP:0001249 Intellectual disability**), ranging from mild to profound. Developmental delay (**HP:0001263**) may be recognized before formal cognitive testing. Onset is congenital/developmental, generally becoming apparent in infancy or childhood; the cognitive disability is chronic and lifelong rather than episodic. (tejada2020non‐syndromicxlinked pages 1-5)

Common but non-universal, gene-dependent findings include:

* speech/language delay (**HP:0000750**), poor or absent speech;
* hypotonia (**HP:0001252**) and occasionally muscle weakness (**HP:0001324**);
* seizures/epilepsy (**HP:0001250**);
* autism (**HP:0000729**), behavioral abnormality (**HP:0000708**), or psychiatric symptoms;
* motor delay, variable reflexes, minor dysmorphism, clinodactyly, micro- or macrocephaly, and occasional structural brain anomalies.

These features cannot be assigned meaningful umbrella-level percentages. For example, early IQSEC2 families showed moderate-to-severe ID, while seizures, autistic traits, and psychiatric problems were inconsistent. More than 70 IQSEC2 variants had been reported by 2020, with severe truncating variants often producing a broader encephalopathy. (tejada2020non‐syndromicxlinked pages 12-15)

In the 2023 Iranian series, severe ID, developmental and speech delay were prominent; seizures, behavioral problems, muscle weakness, dysmorphism, agenesis of the corpus callosum, and colpocephaly varied by family and gene. (mir2023wholeexomesequencing pages 2-4, mir2023fourfamilieswith pages 9-11, mir2023wholeexomesequencing pages 4-6)

**Quality of life:** impairment chiefly affects communication, education, independent living, employment, social participation, and lifelong caregiver needs. Epilepsy, behavioral disorders, and absent speech add substantial morbidity. No NS-XLID-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life estimate was found; quantitative quality-of-life claims should therefore not be imputed from general ID cohorts.

## 4. Genetic and molecular information

### Variant interpretation

Pathogenic variants are generally rare or absent from population databases and evaluated with ACMG/AMP criteria, segregation, phenotype consistency, XCI/escape status, and functional evidence. Healthy carrier mothers do not automatically refute pathogenicity. Conversely, rarity and in-silico prediction alone do not establish causality. RNA sequencing, biochemical assays, deep mutational scanning, and cell models can reclassify variants of uncertain significance. (luca2020challengesinmolecular pages 1-2, ibarluzea2020targetednextgenerationsequencing pages 1-3)

The variant classes and consequences are gene-specific:

* **Loss of function:** truncating/splice/deletion variants in numerous genes; disturbed synaptic, transcriptional, or transport functions.
* **Dosage change:** duplications of XLID genes can produce variable phenotypes; excessive expression may be as harmful as deficiency. (tejada2020non‐syndromicxlinked pages 5-8, martinez2024overcominggeneticand pages 6-7)
* **Missense/domain effects:** IQSEC2 variants in IQ or Sec7 domains can respectively impair calmodulin binding/increase GEF activity or reduce ARF6 GEF activity. (tejada2020non‐syndromicxlinked pages 12-15, tejada2020non‐syndromicxlinked pages 19-23)
* **Gain-of-function-like physiology:** **SLC9A7 p.Leu515Phe** causes alkalinization of trans-Golgi/post-Golgi compartments with abnormal glycosylation, despite broadly preserved localization and trafficking. (khayat2019arecurrentmissense pages 2-3, khayat2019arecurrentmissense pages 8-9)

Allele frequency must be documented per exact HGVS allele and genome build in gnomAD; there is no meaningful group-level allele frequency. Germline inheritance predominates. Somatic origin is not a defining feature, although mosaicism should be considered. No consistently validated modifier gene or anticipation phenomenon was found. Founder effects and carrier frequencies are variant/population-specific and not established for the umbrella entity.

### X-inactivation and epigenetics

Random XCI creates cellular mosaics in females; escape from XCI and tissue-specific skewing complicate penetrance and blood-to-brain inference. In a 2023 study of 194 women with idiopathic ID, 136 were informative for the androgen-receptor methylation assay; 11/136 (8%) had extreme/total skewing of at least 90%. WES diagnosed 8/11 (73%), including X-linked **DDX3X, WDR45, PDHA1** and autosomal **KCNB1, CTNNB1, YY1, ANKRD11** variants. Thus extreme XCI is an enrichment signal, not a standalone NS-XLID diagnostic criterion. [Molecular Neurobiology, March 2023, DOI: https://doi.org/10.1007/s12035-023-03311-0]. (chaves2023skewedxchromosomeinactivation pages 1-5)

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, smoking, alcohol pattern, diet, exercise level, or infectious agent is known to cause genetically defined NS-XLID. These factors may influence general neurodevelopment, health, or seizure control, but evidence for a disease-specific causal interaction is absent. NS-XLID is neither infectious nor transmissible, and vaccination is not etiologic or preventive.

## 6. Mechanism and pathophysiology

The upstream event is a pathogenic X-linked variant. The downstream chain depends on the gene, but several convergent modules emerge:

1. **Synaptic vesicle cycling and neurotransmitter release.** GDI1 regulates Rab GTPases; IL1RAPL1 regulates calcium-dependent secretion; SYN1 and SYP control synaptic-vesicle trafficking/endocytosis. Defects impair presynaptic release and activity-dependent plasticity. Suggested GO terms: **GO:0007268 chemical synaptic transmission**, **GO:0016079 synaptic vesicle exocytosis**. (tejada2020non‐syndromicxlinked pages 8-12)
2. **Postsynaptic organization and receptor trafficking.** DLG3 organizes NMDA-receptor signaling; GRIA3 encodes an AMPA-receptor component; IQSEC2/ARF6 regulates AMPA trafficking and dendritic actin. Disrupted receptor localization and spine plasticity impair learning and memory. Suggested GO: **GO:0048167 regulation of synaptic plasticity**, **GO:0032956 regulation of actin cytoskeleton organization**. (tejada2020non‐syndromicxlinked pages 12-15, tejada2020non‐syndromicxlinked pages 8-12)
3. **Chromatin/transcription/RNA regulation.** ATRX, MECP2, KDM5C, HCFC1, MED12, UPF3B and related proteins alter chromatin organization, RNA-polymerase-II signaling, splicing, export, translation, or nonsense-mediated decay, disturbing developmental neuronal gene programs. MED12 defects can disrupt GLI3-dependent Sonic Hedgehog, REST-dependent epigenetic signaling, and immediate-early-gene expression. Suggested GO: **GO:0006338 chromatin remodeling**, **GO:0006357 regulation of transcription by RNA polymerase II**, **GO:0000184 nonsense-mediated mRNA decay**. (tejada2020non‐syndromicxlinked pages 5-8, tejada2020non‐syndromicxlinked pages 19-23)
4. **Ubiquitin/proteostasis pathways.** HUWE1 and other ubiquitin-system genes alter substrate turnover, neuronal proliferation, differentiation, and stress responses. Suggested GO: **GO:0016567 protein ubiquitination**. (tejada2020non‐syndromicxlinked pages 19-23)
5. **Transport, metabolism, and organelles.** SLC6A8 deficiency impairs brain creatine uptake and energy buffering; CLCN4 alters endosomal ion homeostasis; NDUFA1/SLC25A5 affect mitochondrial function; SLC9A7 alters Golgi pH and glycosylation. (tejada2020non‐syndromicxlinked pages 12-15, tejada2020non‐syndromicxlinked pages 25-28, khayat2019arecurrentmissense pages 3-4)

### Mechanistic exemplar: SLC9A7-related NS-XLID

Khayat and colleagues reported the recurrent **SLC9A7 c.1543C>T (p.Leu515Phe)** allele in two unrelated families: four Australian males aged 65, 58, 56, and 27 years and two American males aged 36 and four years. Clinical findings included moderate-to-severe ID, speech delay, hypotonia/muscle weakness, reserved personality, variable reflexes, and bilateral clinodactyly; carrier females were clinically unaffected. [Human Molecular Genetics, October 2019; PMID **30335141**; DOI: https://doi.org/10.1093/hmg/ddy371]. (khayat2019arecurrentmissense pages 3-4, khayat2019arecurrentmissense pages 45-45)

SLC9A7/NHE7 normally localizes predominantly to the trans-Golgi network (TGN) and post-Golgi vesicles. The mutant retained localization and had a nonsignificantly shorter half-life—2.2 ± 0.43 versus 2.92 ± 1.52 hours—but alkalinized TGN/post-Golgi compartments, impaired N-linked oligosaccharide maturation, and produced abnormal serum-transferrin N-glycosylation. The causal chain is therefore: **missense variant → dysregulated organellar proton/cation exchange → Golgi alkalinization → abnormal cargo glycosylation → altered neuronal protein processing → neurodevelopmental impairment**. Evidence is human genetic plus serum biochemical and transfected-cell functional evidence, not yet proof of every downstream brain step. (khayat2019arecurrentmissense pages 2-3, khayat2019arecurrentmissense pages 8-9)

### Cells, anatomy, immune/tissue injury, and omics

Relevant cells are principally neurons—especially cortical and hippocampal excitatory and inhibitory populations—and their synapses; glia may participate in selected disorders. Suggested terms include **CL:0000540 neuron**, plus release-verified cortical, glutamatergic, GABAergic, and hippocampal neuronal subclasses. The primary organ is the brain (**UBERON:0000955**), particularly cerebral cortex (**UBERON:0000956**) and distributed cognitive circuits. (martinez2024overcominggeneticand pages 7-8, martinez2024overcominggeneticand pages 11-12, martinez2024overcominggeneticand pages 1-2)

There is no common autoimmune, immunodeficiency, inflammatory, ischemic, fibrotic, necrotic, or oxidative-tissue-injury mechanism for NS-XLID as a whole. Likewise, no validated umbrella-level transcriptomic, proteomic, metabolomic, or lipidomic diagnostic signature exists. Gene-specific data include transferrin glycosylation in SLC9A7 and creatine abnormalities in SLC6A8. Single-cell, spatial-transcriptomic, and integrated multi-omic findings remain research-stage and are not sufficiently uniform for disease-group annotation.

## 7. Anatomical structures affected

* **Primary system:** central nervous system.
* **Organ/site:** brain and distributed bilateral neural circuits; no characteristic lateralization.
* **Tissue:** nervous tissue, especially cortical and hippocampal networks.
* **Cellular:** neurons, dendrites, axons, synapses; gene-dependent involvement of glia is possible.
* **Subcellular:** synaptic vesicle, presynapse, postsynaptic density, dendritic spine, nucleus/chromatin, Golgi/TGN, endosome, or mitochondrion according to gene. Suggested GO cellular-component terms include **GO:0045202 synapse, GO:0014069 postsynaptic density, GO:0043197 dendritic spine, GO:0005794 Golgi apparatus, GO:0005802 TGN, GO:0005768 endosome, GO:0005739 mitochondrion**. (tejada2020non‐syndromicxlinked pages 23-25, tejada2020non‐syndromicxlinked pages 25-28, tejada2020non‐syndromicxlinked pages 8-12, khayat2019arecurrentmissense pages 3-4)

Secondary organ involvement is not intrinsic to strict NS-XLID. Consistent extracerebral abnormalities should prompt reconsideration of a gene-specific syndromic diagnosis.

## 8. Temporal development

Onset is developmental, usually recognized through delayed milestones, language delay, learning difficulty, or adaptive impairment in infancy or childhood. ID is chronic and lifelong. The core cognitive deficit is usually relatively stable rather than relapsing-remitting, although developmental gains occur and comorbid epilepsy or behavior may fluctuate. There is no accepted staging system, remission pattern, or end stage for the umbrella disease.

Early childhood is the key period for diagnostic testing and developmental intervention because neuroplasticity and acquisition of communication/adaptive skills are greatest. Evidence does not support spontaneous cure. Gene-specific disorders may be progressive or epileptic-encephalopathic and should not be generalized to strict NS-XLID.

## 9. Inheritance and population

Inheritance is usually X-linked: hemizygous males are more frequently and often more severely affected, while heterozygous females range from unaffected to severely affected depending on XCI, escape, dosage, and variant mechanism. Some genes behave as X-linked dominant disorders with frequent de novo female cases rather than conventional recessive traits. (luca2020challengesinmolecular pages 1-2, martinez2024overcominggeneticand pages 1-2, chaves2023skewedxchromosomeinactivation pages 1-5)

ID overall is reported around 1%, with male prevalence approximately 30% higher than female prevalence in one meta-analytic summary. XLID mutations account for an estimated 5–10% of male ID, but strict NS-XLID prevalence, incidence, carrier frequency, geographic distribution, and male:female ratio are unavailable. (tejada2020non‐syndromicxlinked pages 1-5, luca2020challengesinmolecular pages 1-2)

Penetrance and expressivity are gene- and sex-dependent. Germline mosaicism is relevant for counseling after an apparently de novo result, but no umbrella recurrence percentage is available. Genetic anticipation is not characteristic, except that **AFF2/FMR2**- and **FMR1**-related repeat biology must be handled under their specific disease definitions. Consanguinity is not a primary risk factor for X-linked disease, although it can clarify or complicate pedigrees. Founder alleles and population differences must be assessed variant by variant; the 2023 Iranian family study illustrates the importance of studying underrepresented ancestries but does not establish a general regional excess. (mir2023wholeexomesequencing pages 1-2, mir2023wholeexomesequencing pages 4-6)

## 10. Diagnostics

### Recommended workflow

1. Confirm developmental ID using standardized cognitive and adaptive-behavior assessment; document neurologic, behavioral, growth, dysmorphic, and systemic findings.
2. Obtain prenatal/perinatal history and a three-generation pedigree, specifically maternal male relatives and mildly affected females.
3. Perform hearing/vision assessment and phenotype-directed EEG, brain MRI, metabolic tests, or biochemical assays. EEG and MRI are not universal diagnostic biomarkers.
4. Test **FMR1 CGG expansion** when clinically/family-history indicated. Standard exome sequencing does not reliably exclude repeat expansion.
5. Use **trio exome sequencing or genome sequencing** early, with validated CNV calling. Chromosomal microarray remains useful where sequencing-based CNV detection is unavailable or structural variation is suspected.
6. Analyze a curated ID/XLID gene set but do not restrict interpretation to X-linked genes; apparent XLID pedigrees can have autosomal or de novo causes.
7. Confirm relevant variants orthogonally where required; perform parental/segregation testing, ACMG/AMP classification, and periodic reanalysis.
8. Add RNA studies, methylation/XCI studies, enzyme/transporter assays, metabolomics, or glycosylation testing when a candidate mechanism warrants it. (luca2020challengesinmolecular pages 1-2, ibarluzea2020targetednextgenerationsequencing pages 1-3, chaves2023skewedxchromosomeinactivation pages 1-5)

In a panel study of 61 unrelated males with suggestive NS-XLID after normal karyotype and FMR1 testing, sequencing 82 XLID genes found 17 candidate variants in 16 patients. The authors cited approximately 25% diagnostic yields for panel/X-exome strategies and stressed segregation, RNA, and biochemical follow-up. [Genes, January 2020, DOI: https://doi.org/10.3390/genes11010051]. (ibarluzea2020targetednextgenerationsequencing pages 1-3)

Gene-specific adjuncts include elevated urine creatine/creatinine and reduced brain creatine by proton MRS for **SLC6A8** deficiency, and serum-transferrin N-glycosylation for **SLC9A7**. These are not universal NS-XLID biomarkers. (tejada2020non‐syndromicxlinked pages 12-15, khayat2019arecurrentmissense pages 2-3)

### Differential diagnosis and screening

Differentials include Fragile X syndrome, syndromic XLID, autosomal dominant/recessive ID, chromosomal CNVs, mitochondrial disease, cerebral palsy, fetal alcohol exposure, congenital infection, endocrine/metabolic disorders, autism without ID, and acquired brain injury. There are no universal NS-XLID clinical criteria beyond developmental ID plus a confirmed causal X-linked diagnosis and absence of a consistent defining syndrome.

No population newborn screen exists. Appropriate screening comprises cascade testing after a familial diagnosis, targeted carrier testing, and variant-specific prenatal/preimplantation testing. Broad carrier screening may not capture all genes/variant classes.

## 11. Outcome and prognosis

No NS-XLID-specific survival curves, mortality rates, or life-expectancy estimates were identified. Isolated cognitive disability is not inherently life-limiting, but prognosis varies with epilepsy, aspiration, mobility, congenital anomalies, or gene-specific systemic disease. Functional morbidity is lifelong and may include dependence in communication, education, employment, finances, and daily living.

Recovery to typical cognition is not expected, although developmental, educational, and communication gains can be substantial. Prognostic factors are causal gene/variant, severity of early delay, epilepsy burden, speech acquisition, motor ability, behavior, and access to intervention. No validated molecular prognostic biomarker applies across NS-XLID.

## 12. Treatment and current applications

There is no FDA/EMA-approved pharmacotherapy, surgery, cell therapy, immunotherapy, RNA therapy, or gene therapy for NS-XLID as an umbrella disease. Current real-world management is multidisciplinary:

* early intervention and individualized education;
* speech-language therapy, including augmentative/alternative communication;
* occupational and physical therapy;
* behavioral and psychiatric assessment/intervention;
* standard genotype- and seizure-type-appropriate antiseizure medication;
* treatment of sleep, feeding, gastrointestinal, sensory, orthopedic, or other comorbidities;
* social-work support, respite care, transition planning, and supported decision-making.

Suggested NCIT intervention concepts, with current-release verification, are **Supportive Care, Speech Therapy, Occupational Therapy, Physical Therapy, Behavioral Therapy, Genetic Counseling, Anticonvulsant Therapy, Whole Exome Sequencing**, and **Gene Therapy**.

A ClinicalTrials.gov search did not identify a disease-modifying interventional trial for strict NS-XLID. Relevant research infrastructure includes **NCT02854956**, a broad XLID clinical phenotyping/neural-network study, and **NCT06500260**, an observational CNKSR2 natural-history study. Trials for Fragile X, Rett, or CDKL5-related disease should not be represented as treatments for NS-XLID.

Experimental directions include AAV gene replacement, dosage-controlled transgenes, RNA destabilization/microRNA regulatory elements, and selective reactivation of the healthy inactive X chromosome. Experts emphasize that mosaic females create a central safety problem: indiscriminate expression may rescue mutant cells while overdosing cells already expressing the normal allele. CRISPR/pharmacologic X-reactivation currently lacks adequate cellular specificity. (martinez2024overcominggeneticand pages 7-8, martinez2024overcominggeneticand pages 8-10, martinez2024overcominggeneticand pages 6-7)

## 13. Prevention

Primary prevention through lifestyle modification, vaccination, or environmental avoidance is not applicable to a monogenic disease group. Actionable prevention is reproductive and family-based:

* genetic counseling and precise variant interpretation;
* cascade testing of at-risk relatives;
* carrier testing with discussion of variable female expression;
* prenatal diagnosis by chorionic-villus sampling or amniocentesis for a known familial variant;
* preimplantation genetic testing for monogenic disease;
* counseling about residual recurrence risk from gonadal mosaicism;
* early developmental surveillance of at-risk or diagnosed children.

Secondary/tertiary prevention consists of early diagnosis, timely therapy, seizure recognition, safety planning, and prevention of avoidable complications. There is no prophylactic drug or immunization specific to NS-XLID. (luca2020challengesinmolecular pages 1-2, mir2023wholeexomesequencing pages 1-2)

## 14. Other species and natural disease

No naturally occurring veterinary disease corresponding to the **aggregate** human NS-XLID category was identified. The condition is not infectious, zoonotic, or cross-species transmissible. Orthologous genes are widely conserved in mammals and other vertebrates, but NCBI Gene/Taxonomy identifiers must be attached gene by gene rather than to the umbrella disease. Relevant experimental species include **Homo sapiens (NCBI Taxon 9606)** and **Mus musculus (10090)**; zebrafish, Drosophila, and cultured mammalian cells are also plausible gene-specific systems. No VBO breed association is applicable at group level.

## 15. Model organisms and advanced technologies

Model choice is gene-specific. Available approaches include knockout, knock-in, conditional, reporter, and mosaic mice; transfected mammalian cells; patient-derived fibroblasts; human iPSCs and differentiated neurons; and, for selected genes, zebrafish or invertebrate models.

The 2024 expert review highlights a major limitation: conventional hemizygous knockout mice do not reproduce the cellular mosaicism of heterozygous human females. Proposed F1 crosses combine X-linked reporters with mutant alleles so wild-type and mutant cells can be distinguished while retaining random XCI. **dual-eGRASP**, split-biotin-ligase systems, electrophysiology, calcium/voltage imaging, optogenetics, and chemogenetics can then resolve cell-type-specific synaptic and circuit defects. [Journal of Neurodevelopmental Disorders, February 2024, DOI: https://doi.org/10.1186/s11689-024-09517-0]. (martinez2024overcominggeneticand pages 7-8, martinez2024overcominggeneticand pages 8-10)

Evidence from broader X-linked neurodevelopmental models includes abnormal allele-specific neuronal clustering and circuit development in mosaic PCDH19 models, altered callosal/hippocampal NMDA-receptor circuitry in CDKL5 models, patient-derived CDKL5 iPSCs, and experimental rescue of dendritic-spine instability with IGF-1. These are mechanistically informative but are **not direct treatment evidence for strict NS-XLID**. (martinez2024overcominggeneticand pages 6-7, martinez2024overcominggeneticand pages 11-12)

### Key limitations and knowledge gaps

1. The nonsyndromic/syndromic dichotomy is unstable, and gene counts vary with curation criteria.
2. Most phenotype frequencies, prognoses, and biomarkers are gene-specific; aggregate percentages would be misleading.
3. Blood XCI may not represent brain XCI.
4. Many mechanistic conclusions rely on cells or animals rather than direct human neural tissue.
5. NS-XLID-specific natural-history cohorts, patient-reported outcomes, single-cell/spatial atlases, and therapeutic trials remain scarce.
6. OMIM, Orphanet, ICD, MeSH, HGNC, HPO, GO, CL, UBERON, LOINC, CHEBI, and NCIT mappings should be release-verified before database ingestion.

## Selected authoritative sources

* Tejada MI, Ibarluzea N. **Non-syndromic X-linked intellectual disability: current knowledge in light of recent molecular and functional studies.** *Clinical Genetics*. Published January 2020. DOI: https://doi.org/10.1111/cge.13698. Abstract statement: “the only common feature is ID,” while distinct variants in several genes can cause syndromic or nonsyndromic disease. (tejada2020non‐syndromicxlinked pages 1-5)
* Neri G, Schwartz CE, Lubs HA, Stevenson RE. **X-linked intellectual disability update 2017.** *American Journal of Medical Genetics A*. Published June 2018. DOI: https://doi.org/10.1002/ajmg.a.38710. (neri2018x‐linkedintellectualdisability pages 3-4, neri2018x‐linkedintellectualdisability pages 1-3)
* Mir A et al. **Whole exome sequencing revealed variants in four genes underlying XLID in four Iranian families.** *BMC Medical Genomics*. Published October 2023. DOI: https://doi.org/10.1186/s12920-023-01680-y. (mir2023wholeexomesequencing pages 1-2, mir2023wholeexomesequencing pages 4-6)
* Chaves LD et al. **Skewed X-chromosome inactivation in women with idiopathic ID is indicative of pathogenic variants.** *Molecular Neurobiology*. Published March 2023. DOI: https://doi.org/10.1007/s12035-023-03311-0. (chaves2023skewedxchromosomeinactivation pages 1-5)
* Martinez D, Jiang E, Zhou Z. **Overcoming genetic and cellular complexity to study the pathophysiology of XLIDs.** *Journal of Neurodevelopmental Disorders*. Published February 2024. DOI: https://doi.org/10.1186/s11689-024-09517-0. (martinez2024overcominggeneticand pages 7-8, martinez2024overcominggeneticand pages 1-2)
* Khayat W et al. **A recurrent missense variant in SLC9A7 causes nonsyndromic XLID with alteration of Golgi acidification and aberrant glycosylation.** *Human Molecular Genetics*. Published October 2019; PMID: **30335141**. DOI: https://doi.org/10.1093/hmg/ddy371. Abstract-supported statement: patient serum showed “an abnormal N-glycosylation profile for transferrin,” implicating TGN/post-Golgi pH homeostasis and cargo glycosylation. (khayat2019arecurrentmissense pages 2-3, khayat2019arecurrentmissense pages 45-45)
* De Luca C et al. **Challenges in molecular diagnosis of X-linked intellectual disability.** *British Medical Bulletin*. Published February 2020. DOI: https://doi.org/10.1093/bmb/ldz039. (luca2020challengesinmolecular pages 1-2)
* Ibarluzea N et al. **Targeted next-generation sequencing in patients with suggestive XLID.** *Genes*. Published January 2020. DOI: https://doi.org/10.3390/genes11010051. (ibarluzea2020targetednextgenerationsequencing pages 1-3)

References

1. (tejada2020non‐syndromicxlinked pages 1-5): María Isabel Tejada and Nekane Ibarluzea. Non‐syndromic x linked intellectual disability: current knowledge in light of the recent advances in molecular and functional studies. Jan 2020. URL: https://doi.org/10.1111/cge.13698, doi:10.1111/cge.13698. This article has 32 citations and is from a peer-reviewed journal.

2. (neri2018x‐linkedintellectualdisability pages 3-4): Giovanni Neri, Charles E. Schwartz, Herbert A. Lubs, and Roger E. Stevenson. X‐linked intellectual disability update 2017. American Journal of Medical Genetics Part A, 176:1375-1388, Jun 2018. URL: https://doi.org/10.1002/ajmg.a.38710, doi:10.1002/ajmg.a.38710. This article has 154 citations.

3. (tejada2020non‐syndromicxlinked pages 12-15): María Isabel Tejada and Nekane Ibarluzea. Non‐syndromic x linked intellectual disability: current knowledge in light of the recent advances in molecular and functional studies. Jan 2020. URL: https://doi.org/10.1111/cge.13698, doi:10.1111/cge.13698. This article has 32 citations and is from a peer-reviewed journal.

4. (OpenTargets Search: non-syndromic X-linked intellectual disability): Open Targets Query (non-syndromic X-linked intellectual disability, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (tejada2020non‐syndromicxlinked pages 23-25): María Isabel Tejada and Nekane Ibarluzea. Non‐syndromic x linked intellectual disability: current knowledge in light of the recent advances in molecular and functional studies. Jan 2020. URL: https://doi.org/10.1111/cge.13698, doi:10.1111/cge.13698. This article has 32 citations and is from a peer-reviewed journal.

6. (luca2020challengesinmolecular pages 1-2): Chiara De Luca, Valérie Race, Liesbeth Keldermans, Marijke Bauters, and Hilde Van Esch. Challenges in molecular diagnosis of x-linked intellectual disability. British medical bulletin, Feb 2020. URL: https://doi.org/10.1093/bmb/ldz039, doi:10.1093/bmb/ldz039. This article has 36 citations and is from a peer-reviewed journal.

7. (mir2023wholeexomesequencing pages 1-2): Atefeh Mir, Yongjun Song, Hane Lee, Hossein Khanahmad, Erfan Khorram, Jafar Nasiri, and Mohammad Amin Tabatabaiefar. Whole exome sequencing revealed variants in four genes underlying x-linked intellectual disability in four iranian families: novel deleterious variants and clinical features with the review of literature. BMC Medical Genomics, Oct 2023. URL: https://doi.org/10.1186/s12920-023-01680-y, doi:10.1186/s12920-023-01680-y. This article has 10 citations and is from a peer-reviewed journal.

8. (ibarluzea2020targetednextgenerationsequencing pages 1-3): Nekane Ibarluzea, Ana Belén de la Hoz, Olatz Villate, Isabel Llano, Intzane Ocio, Itxaso Martí, Miriam Guitart, Elisabeth Gabau, Fernando Andrade, Blanca Gener, and María-Isabel Tejada. Targeted next-generation sequencing in patients with suggestive x-linked intellectual disability. Genes, 11:51, Jan 2020. URL: https://doi.org/10.3390/genes11010051, doi:10.3390/genes11010051. This article has 34 citations.

9. (martinez2024overcominggeneticand pages 7-8): Dayne Martinez, Evan Jiang, and Zhaolan Zhou. Overcoming genetic and cellular complexity to study the pathophysiology of x-linked intellectual disabilities. Journal of Neurodevelopmental Disorders, Feb 2024. URL: https://doi.org/10.1186/s11689-024-09517-0, doi:10.1186/s11689-024-09517-0. This article has 9 citations and is from a peer-reviewed journal.

10. (martinez2024overcominggeneticand pages 8-10): Dayne Martinez, Evan Jiang, and Zhaolan Zhou. Overcoming genetic and cellular complexity to study the pathophysiology of x-linked intellectual disabilities. Journal of Neurodevelopmental Disorders, Feb 2024. URL: https://doi.org/10.1186/s11689-024-09517-0, doi:10.1186/s11689-024-09517-0. This article has 9 citations and is from a peer-reviewed journal.

11. (martinez2024overcominggeneticand pages 6-7): Dayne Martinez, Evan Jiang, and Zhaolan Zhou. Overcoming genetic and cellular complexity to study the pathophysiology of x-linked intellectual disabilities. Journal of Neurodevelopmental Disorders, Feb 2024. URL: https://doi.org/10.1186/s11689-024-09517-0, doi:10.1186/s11689-024-09517-0. This article has 9 citations and is from a peer-reviewed journal.

12. (khayat2019arecurrentmissense pages 3-4): Wujood Khayat, Anna Hackett, Marie Shaw, Alina Ilie, Tracy Dudding-Byth, Vera M Kalscheuer, Louise Christie, Mark A Corbett, Jane Juusola, Kathryn L Friend, Brian M Kirmse, Jozef Gecz, Michael Field, and John Orlowski. A recurrent missense variant in slc9a7 causes nonsyndromic x-linked intellectual disability with alteration of golgi acidification and aberrant glycosylation. Human Molecular Genetics, 28:598–614, Oct 2019. URL: https://doi.org/10.1093/hmg/ddy371, doi:10.1093/hmg/ddy371. This article has 45 citations and is from a domain leading peer-reviewed journal.

13. (mir2023wholeexomesequencing pages 2-4): Atefeh Mir, Yongjun Song, Hane Lee, Hossein Khanahmad, Erfan Khorram, Jafar Nasiri, and Mohammad Amin Tabatabaiefar. Whole exome sequencing revealed variants in four genes underlying x-linked intellectual disability in four iranian families: novel deleterious variants and clinical features with the review of literature. BMC Medical Genomics, Oct 2023. URL: https://doi.org/10.1186/s12920-023-01680-y, doi:10.1186/s12920-023-01680-y. This article has 10 citations and is from a peer-reviewed journal.

14. (mir2023fourfamilieswith pages 9-11): Atefeh Mir, Yongjun Song, Hane Lee, Hossein Khanahmad, Erfan Khorram, Jafar Nasiri, and Mohammad-Amin Tabatabaiefar. Four families with x-linked intellectual disability affected males: novel deleterious variants and clinical features with the review of literature. Unknown journal, Apr 2023. URL: https://doi.org/10.21203/rs.3.rs-2833503/v1, doi:10.21203/rs.3.rs-2833503/v1.

15. (mir2023wholeexomesequencing pages 4-6): Atefeh Mir, Yongjun Song, Hane Lee, Hossein Khanahmad, Erfan Khorram, Jafar Nasiri, and Mohammad Amin Tabatabaiefar. Whole exome sequencing revealed variants in four genes underlying x-linked intellectual disability in four iranian families: novel deleterious variants and clinical features with the review of literature. BMC Medical Genomics, Oct 2023. URL: https://doi.org/10.1186/s12920-023-01680-y, doi:10.1186/s12920-023-01680-y. This article has 10 citations and is from a peer-reviewed journal.

16. (tejada2020non‐syndromicxlinked pages 19-23): María Isabel Tejada and Nekane Ibarluzea. Non‐syndromic x linked intellectual disability: current knowledge in light of the recent advances in molecular and functional studies. Jan 2020. URL: https://doi.org/10.1111/cge.13698, doi:10.1111/cge.13698. This article has 32 citations and is from a peer-reviewed journal.

17. (tejada2020non‐syndromicxlinked pages 5-8): María Isabel Tejada and Nekane Ibarluzea. Non‐syndromic x linked intellectual disability: current knowledge in light of the recent advances in molecular and functional studies. Jan 2020. URL: https://doi.org/10.1111/cge.13698, doi:10.1111/cge.13698. This article has 32 citations and is from a peer-reviewed journal.

18. (tejada2020non‐syndromicxlinked pages 8-12): María Isabel Tejada and Nekane Ibarluzea. Non‐syndromic x linked intellectual disability: current knowledge in light of the recent advances in molecular and functional studies. Jan 2020. URL: https://doi.org/10.1111/cge.13698, doi:10.1111/cge.13698. This article has 32 citations and is from a peer-reviewed journal.

19. (martinez2024overcominggeneticand pages 1-2): Dayne Martinez, Evan Jiang, and Zhaolan Zhou. Overcoming genetic and cellular complexity to study the pathophysiology of x-linked intellectual disabilities. Journal of Neurodevelopmental Disorders, Feb 2024. URL: https://doi.org/10.1186/s11689-024-09517-0, doi:10.1186/s11689-024-09517-0. This article has 9 citations and is from a peer-reviewed journal.

20. (martinez2024overcominggeneticand pages 11-12): Dayne Martinez, Evan Jiang, and Zhaolan Zhou. Overcoming genetic and cellular complexity to study the pathophysiology of x-linked intellectual disabilities. Journal of Neurodevelopmental Disorders, Feb 2024. URL: https://doi.org/10.1186/s11689-024-09517-0, doi:10.1186/s11689-024-09517-0. This article has 9 citations and is from a peer-reviewed journal.

21. (khayat2019arecurrentmissense pages 2-3): Wujood Khayat, Anna Hackett, Marie Shaw, Alina Ilie, Tracy Dudding-Byth, Vera M Kalscheuer, Louise Christie, Mark A Corbett, Jane Juusola, Kathryn L Friend, Brian M Kirmse, Jozef Gecz, Michael Field, and John Orlowski. A recurrent missense variant in slc9a7 causes nonsyndromic x-linked intellectual disability with alteration of golgi acidification and aberrant glycosylation. Human Molecular Genetics, 28:598–614, Oct 2019. URL: https://doi.org/10.1093/hmg/ddy371, doi:10.1093/hmg/ddy371. This article has 45 citations and is from a domain leading peer-reviewed journal.

22. (khayat2019arecurrentmissense pages 8-9): Wujood Khayat, Anna Hackett, Marie Shaw, Alina Ilie, Tracy Dudding-Byth, Vera M Kalscheuer, Louise Christie, Mark A Corbett, Jane Juusola, Kathryn L Friend, Brian M Kirmse, Jozef Gecz, Michael Field, and John Orlowski. A recurrent missense variant in slc9a7 causes nonsyndromic x-linked intellectual disability with alteration of golgi acidification and aberrant glycosylation. Human Molecular Genetics, 28:598–614, Oct 2019. URL: https://doi.org/10.1093/hmg/ddy371, doi:10.1093/hmg/ddy371. This article has 45 citations and is from a domain leading peer-reviewed journal.

23. (tejada2020non‐syndromicxlinked pages 25-28): María Isabel Tejada and Nekane Ibarluzea. Non‐syndromic x linked intellectual disability: current knowledge in light of the recent advances in molecular and functional studies. Jan 2020. URL: https://doi.org/10.1111/cge.13698, doi:10.1111/cge.13698. This article has 32 citations and is from a peer-reviewed journal.

24. (chaves2023skewedxchromosomeinactivation pages 1-5): Luiza D. Chaves, Laura M. L. Carvalho, Giovanna C. Tolezano, Sara F. Pires, Silvia S. Costa, Marília O. de Scliar, Liane de R. Giuliani, Debora R. Bertola, Cíntia B. Santos-Rebouças, Go Hun Seo, Paulo A. Otto, Carla Rosenberg, Angela M. Vianna-Morgante, and Ana C. V. Krepischi. Skewed x-chromosome inactivation in women with idiopathic intellectual disability is indicative of pathogenic variants. Molecular Neurobiology, 60:3758-3769, Mar 2023. URL: https://doi.org/10.1007/s12035-023-03311-0, doi:10.1007/s12035-023-03311-0. This article has 11 citations and is from a peer-reviewed journal.

25. (khayat2019arecurrentmissense pages 45-45): Wujood Khayat, Anna Hackett, Marie Shaw, Alina Ilie, Tracy Dudding-Byth, Vera M Kalscheuer, Louise Christie, Mark A Corbett, Jane Juusola, Kathryn L Friend, Brian M Kirmse, Jozef Gecz, Michael Field, and John Orlowski. A recurrent missense variant in slc9a7 causes nonsyndromic x-linked intellectual disability with alteration of golgi acidification and aberrant glycosylation. Human Molecular Genetics, 28:598–614, Oct 2019. URL: https://doi.org/10.1093/hmg/ddy371, doi:10.1093/hmg/ddy371. This article has 45 citations and is from a domain leading peer-reviewed journal.

26. (neri2018x‐linkedintellectualdisability pages 1-3): Giovanni Neri, Charles E. Schwartz, Herbert A. Lubs, and Roger E. Stevenson. X‐linked intellectual disability update 2017. American Journal of Medical Genetics Part A, 176:1375-1388, Jun 2018. URL: https://doi.org/10.1002/ajmg.a.38710, doi:10.1002/ajmg.a.38710. This article has 154 citations.

## Artifacts

- [Edison artifact artifact-00](Non-Syndromic_X-Linked_Intellectual_Disability-deep-research-falcon_artifacts/artifact-00.md)
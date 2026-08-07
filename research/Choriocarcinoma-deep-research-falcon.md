---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T23:33:54.612280'
end_time: '2026-07-31T23:55:07.726167'
duration_seconds: 1273.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Choriocarcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Choriocarcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Choriocarcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Choriocarcinoma** covering all of the
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
- **Disease Name:** Choriocarcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Choriocarcinoma** covering all of the
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


# Choriocarcinoma: comprehensive disease-characteristics report

**Evidence scope.** Choriocarcinoma is biologically heterogeneous. This report distinguishes **gestational choriocarcinoma (GC)**—a pregnancy-derived gestational trophoblastic neoplasia (GTN)—from **nongestational choriocarcinoma (NGC)** arising as an ovarian, testicular, or extragonadal germ-cell tumor. Data labeled “GTD/GTN” may include invasive mole, placental-site trophoblastic tumor (PSTT), and epithelioid trophoblastic tumor (ETT), and therefore are not automatically choriocarcinoma-specific. Most high-quality clinical evidence concerns gestational disease.

The following ontology-oriented table summarizes the most readily computable findings.

| Domain | Key evidence-backed finding | Suggested ontology identifiers/terms | Evidence scope/limitations |
|---|---|---|---|
| Disease identity | **Choriocarcinoma** is a malignant trophoblastic neoplasm; MONDO association available as **MONDO:0005207**. In clinical practice, reports should distinguish **gestational choriocarcinoma** from **nongestational germ-cell choriocarcinoma**, because etiology, molecular origin, and treatment context differ (OpenTargets Search: choriocarcinoma, tempfer2023gestationalandnongestational pages 4-5, shahzadi2023reviewofcurrent pages 2-4) | MONDO:0005207; suggested terms: choriocarcinoma, gestational choriocarcinoma, nongestational choriocarcinoma, uterine corpus choriocarcinoma, ovarian choriocarcinoma, testicular choriocarcinoma | MONDO link is supported; subtype ontologies beyond MONDO:0005207 were not comprehensively validated here. Literature retrieved was much richer for gestational disease than for nongestational germ-cell disease. |
| Major subtypes / taxonomy | Major clinically relevant groupings: **gestational choriocarcinoma** (usually postmolar but may follow any pregnancy), **nongestational ovarian/testicular/extragonadal choriocarcinoma** as a germ-cell tumor component, and **precursor hydatidiform mole** / postmolar GTN, which must not be conflated with frank choriocarcinoma (tempfer2023gestationalandnongestational pages 4-5, gonzalez2024gestationaltrophoblasticdisease pages 5-7, shahzadi2023reviewofcurrent pages 2-4) | Suggested disease terms: gestational trophoblastic neoplasia (GTN), hydatidiform mole, complete hydatidiform mole, partial hydatidiform mole, invasive mole, choriocarcinoma | Much of the molecular literature concerns precursor moles or broader GTN rather than pure choriocarcinoma. Nongestational biology is underrepresented in the retrieved evidence. |
| Etiology / causal factors | Gestational disease arises from abnormal trophoblastic proliferation after pregnancy; complete hydatidiform moles are typically androgenetic and carry higher risk of progression to invasive mole/choriocarcinoma than partial moles. Recurrent molar disease is associated with maternal-effect/imprinting genes such as **NLRP7** and **KHDC3L** in precursor disease (tempfer2023gestationalandnongestational pages 4-5, shibata2020uniquefeaturesand pages 8-9, gonzalez2024gestationaltrophoblasticdisease pages 5-7) | Suggested terms: abnormal fertilization, genomic imprinting defect, androgenetic conceptus, trophoblast neoplasm | Strongest causal evidence is for precursor villous disease, not for a single universal driver mutation of choriocarcinoma itself. |
| Risk factors | Higher GTD incidence/risk is reported at maternal age extremes (10–19 and 40–54 years), prior molar pregnancy, and ethnicity/geography differences; Asian women have about double the incidence reported for women of Caucasian descent in the cited guideline, and Black US women are overrepresented in some registers (tempfer2023gestationalandnongestational pages 4-5, shahzadi2023reviewofcurrent pages 2-4) | Suggested exposure/risk terms: advanced maternal age, teenage pregnancy, prior molar pregnancy, Asian ancestry | Retrieved evidence is disease-group level for GTD/GTN, not choriocarcinoma-only risk quantification. Protective factors were not well established in retrieved sources. |
| Epidemiology | In highly developed countries, hydatidiform mole prevalence was cited as **1 per 591 pregnancies** and GTD prevalence **1 per 714 live births**; Dutch population incidence over 20 years was **1.67 cases/1000 births/year** for GTD (tempfer2023gestationalandnongestational pages 4-5) | Suggested epidemiology terms: incidence, prevalence, reproductive-age female predominance | These are GTD-level figures, not choriocarcinoma-specific incidence. Choriocarcinoma is rarer than GTD overall. |
| Core phenotypes / symptoms | Common clinical manifestations across GTN/choriocarcinoma include abnormal vaginal bleeding, elevated/plateauing/rising **β-hCG**, metastatic symptoms, and hemorrhage from tumor sites; brain, liver, and lung metastases are clinically important in high-risk disease (tempfer2023gestationalandnongestational pages 8-9, tempfer2023gestationalandnongestational pages 10-11, shahzadi2023reviewofcurrent pages 2-4) | Suggested HPO terms: **Abnormal uterine bleeding**, **Elevated circulating human chorionic gonadotropin**, **Pulmonary metastases**, **Brain metastases**, **Liver metastases**, **Anemia**, **Hemorrhage** | Direct HPO numeric IDs were not validated here; terms are suggested labels only. Evidence is strongest for GTN/high-risk cohorts rather than phenotype frequencies specific to choriocarcinoma. |
| Anatomy affected | Primary organ is typically **uterus** in gestational choriocarcinoma; metastatic evaluation routinely targets **lung**, **brain**, **liver**, abdomen/pelvis, and genital tract structures (tempfer2023gestationalandnongestational pages 8-9, shahzadi2023reviewofcurrent pages 2-4) | Suggested UBERON terms: uterus, endometrium, placenta/chorion, lung, brain, liver, vagina, adnexa | UBERON numeric IDs not validated here. Some anatomic staging language is FIGO/TNM rather than ontology-based. |
| Tissue / cell types | Disease involves malignant **trophoblast** lineage cells; trophoblast research models emphasize **cytotrophoblast**, **syncytiotrophoblast**, and **extravillous trophoblast** biology, with markers such as **GATA3**, **TFAP2C**, low HLA class I, and **C19MC** expression in trophoblast stem-cell systems (shibata2020uniquefeaturesand pages 8-9, OpenTargets Search: choriocarcinoma) | Suggested CL terms: trophoblast cell, cytotrophoblast, syncytiotrophoblast, extravillous trophoblast | CL numeric IDs were not validated. Many model findings come from trophoblast stem-cell or placental systems, not directly from tumor tissue. |
| Histopathology / IHC | Choriocarcinoma belongs to non-villous malignant GTD; in the broader differential, **p57** is useful mainly to distinguish **complete mole** from partial mole/non-molar tissue because p57 is lost in androgenetic CHM and retained in PHM/non-molar gestations. Molecular pathology and IHC are guideline-recommended in GTD workup (tempfer2023gestationalandnongestational pages 4-5, gonzalez2024gestationaltrophoblasticdisease pages 5-7) | Suggested pathology terms: p57/CDKN1C immunostain, trophoblastic neoplasm, molecular genotyping, STR analysis, SNP array | p57 is a **precursor-mole differential tool**, not a definitive diagnostic marker for choriocarcinoma itself. Specific choriocarcinoma IHC panels were not comprehensively retrieved. |
| Molecular / genetic features | Recent transcriptomic work comparing complete moles with postmolar choriocarcinoma identified **33 differentially expressed genes** and implicated **TGF-β pathway dysregulation** with strong **SALL4** expression in postmolar choriocarcinoma; Open Targets evidence also links **TP53**, **GATA3**, and **DHFR** to choriocarcinoma-related evidence (OpenTargets Search: choriocarcinoma, jinkai2024prognosticatinggestationaltrophoblastic pages 9-10) | Suggested gene terms: **SALL4**, **TP53**, **GATA3**, **DHFR**; suggested pathway terms: TGF-beta signaling pathway | Molecular evidence remains sparse and is based on small transcriptomic comparisons and disease-target aggregation; no single recurrent causal mutation was established from retrieved data. |
| Epigenetics / imprinting | Abnormal genomic imprinting is central in precursor molar disease; CHM pathogenesis is linked to androgenesis and loss of maternally expressed **p57/CDKN1C**. Reviews also highlight dysregulated p53/apoptosis pathways, BCL-2/caspases, growth factor receptors, and microRNAs such as **miR-196b** and **miR-21** in GTD/CHM (shibata2020uniquefeaturesand pages 8-9, gonzalez2024gestationaltrophoblasticdisease pages 5-7, nasser2024molecularbasisof pages 12-13) | Suggested terms: genomic imprinting, DNA methylation abnormality, microRNA dysregulation, loss of maternal allele expression | Most retrieved epigenetic evidence concerns **hydatidiform mole** rather than established choriocarcinoma. Extrapolation should be cautious. |
| Mechanisms / pathophysiology | Proposed mechanisms include dysregulated trophoblast proliferation/invasion, **TGF-β** signaling changes, angiogenesis imbalance, oxidative stress, EMT-related programs, and marked immune-checkpoint biology with frequent **PD-L1** expression in GTN. A 2024 prognostic review cited **PD-L1 expression at 92.3%** in GTN and described **HLA-G** as a biomarker of chemotherapy resistance in gestational choriocarcinoma (jinkai2024prognosticatinggestationaltrophoblastic pages 9-10, baas2024immunotherapyforgestational pages 2-3, nasser2024molecularbasisof pages 12-13) | Suggested GO terms: trophoblast cell proliferation, cell migration, cell invasion, epithelial to mesenchymal transition, angiogenesis, response to oxidative stress, immune evasion, TGF-beta receptor signaling pathway, programmed cell death ligand 1 pathway | Mechanistic evidence is mixed across gestational choriocarcinoma, other GTN subtypes, and precursor lesions. GO numeric IDs not validated. |
| Immune biology | GTN demonstrates strong **PD-L1** expression and immune infiltration, providing biologic rationale for checkpoint blockade. Anti-PD-1/PD-L1 therapy has become a salvage standard for multidrug-resistant GTN in some expert settings (baas2024immunotherapyforgestational pages 2-3, baas2024immunotherapyforgestational pages 2-2, baas2024immunotherapyforgestational pages 6-7, tempfer2023gestationalandnongestational pages 10-11) | Suggested terms: PD-L1 expression, PD-1 checkpoint pathway, tumor-infiltrating lymphocytes, immune checkpoint inhibitor response | Evidence is strongest in refractory GTN cohorts, not frontline choriocarcinoma-only populations. Biomarker predictors of response remain incompletely defined. |
| Diagnostic biomarkers | **Serial serum β-hCG** is central for diagnosis, monitoring, and remission assessment. Postmolar GTN/choriocarcinoma diagnostic criteria include plateau or rise in hCG over specified intervals; after therapy, remission monitoring requires serial negative hCG measurements (tempfer2023gestationalandnongestational pages 9-10, tempfer2023gestationalandnongestational pages 15-16, tempfer2023gestationalandnongestational pages 8-9, NCT06028672 chunk 1, NCT05635344 chunk 1) | Suggested LOINC/biomarker terms: serum beta-human chorionic gonadotropin (β-hCG), serial quantitative hCG monitoring | Exact thresholds/definitions vary slightly by guideline/trial. hCG criteria are most validated in postmolar GTN. |
| Diagnostic criteria | Guideline criteria for persistent postmolar villous GTD include: **four or more consecutive hCG values with plateau over ≥3 weeks**, **rise in hCG on 2 consecutive measurements (day 0 and 7)**, or **persistent hCG values over 6 months**; trial eligibility criteria similarly define plateau/rise patterns for GTN (tempfer2023gestationalandnongestational pages 15-16, NCT06028672 chunk 1, NCT05635344 chunk 1) | Suggested terms: FIGO 2000 criteria, postmolar GTN, hCG plateau, hCG rise | These criteria chiefly define postmolar GTN rather than all histologically confirmed choriocarcinoma presentations. |
| Imaging / staging | Recommended staging includes gynecologic exam with palpation, **transvaginal ultrasound**, **CT thorax and abdomen**, and **MRI brain**; **FDG-PET/CT** may be used if metastasis is suspected. Postoperative malignant GTD should also follow current **TNM** classification in addition to FIGO staging (tempfer2023gestationalandnongestational pages 4-5, tempfer2023gestationalandnongestational pages 8-9) | Suggested imaging terms: pelvic ultrasound, CT chest, CT abdomen, brain MRI, FDG-PET/CT, TNM stage, FIGO stage | Guidance is strong for gestational trophoblastic neoplasia. Imaging approach for nongestational germ-cell choriocarcinoma may differ by site and oncology service. |
| FIGO stages / risk strata | FIGO stage: **I uterus-confined**, **II genital structures**, **III lungs**, **IV other metastatic sites**. Prognostic score uses age, antecedent pregnancy, interval since pregnancy, pretreatment hCG, metastasis number/site, tumor size, and prior chemotherapy; **0–4 low risk**, **5–6 intermediate risk**, **≥7 high risk** (tempfer2023gestationalandnongestational pages 4-5, shahzadi2023reviewofcurrent pages 2-4) | Suggested terms: FIGO stage I-IV, WHO/FIGO prognostic score, low-risk GTN, intermediate-risk GTN, high-risk GTN | Core evidence is GTN-wide. Some centers now debate refinements beyond classic FIGO 2000 scoring. |
| First-line treatment strata | Guideline: low-risk disease typically receives **methotrexate** with folinic/folic acid rescue; methotrexate-resistant cases may switch to **actinomycin-D** or polychemotherapy. For FIGO **5–6**, methotrexate may be used, but **EMA-CO** is recommended when FIGO 5–6 coexists with distant metastases, hCG >411,000 IU/L, or diagnosis of choriocarcinoma (tempfer2023gestationalandnongestational pages 15-16, shahzadi2023reviewofcurrent pages 2-4) | Suggested NCIT terms: Methotrexate, Actinomycin D, Folic Acid, EMA-CO regimen | Guidance is primarily for gestational disease. Dose/schedule details may vary among regions and centers. |
| High-risk / metastatic treatment | **EMA-CO** remains standard for high-risk GTN; one 2023 review cited **93% complete remission** with EMA-CO in high-risk GTN and noted ~40% salvage of incomplete responses with platinum-based chemotherapy. Brain-metastatic disease may require higher-dose methotrexate-containing regimens (shahzadi2023reviewofcurrent pages 2-4) | Suggested NCIT terms: EMA-CO, EMA-EP, EP/EMA, BEP, platinum-based combination chemotherapy | Numbers are from GTN/high-risk reviews, not pure choriocarcinoma-only prospective datasets. |
| Choriocarcinoma-specific treatment note | A recent review citing historical stage-specific outcomes reported **83% cure in stage I choriocarcinoma with single-agent chemotherapy**, with additional remissions after further chemotherapy or surgery; stage II-IV disease required combined surgery and chemotherapy (gonzalez2024gestationaltrophoblasticdisease pages 10-11, gonzalez2024gestationaltrophoblasticdisease pages 8-10) | Suggested NCIT terms: single-agent chemotherapy, hysterectomy, metastasectomy, combined modality therapy | Source summarizes older outcome series; exact regimen details and cohort era were not fully resolved from retrieved excerpt. |
| Immunotherapy | Checkpoint inhibitors are a major recent development. Across **133 GTN patients** treated with CPI, **85 achieved complete remission**; among **118 high-risk/relapsed/multidrug-resistant** patients, **77** achieved CR; among **15 low-risk** patients, **8** achieved remission. Pembrolizumab, avelumab, camrelizumab, toripalimab, and combinations with apatinib/chemotherapy are reported (baas2024immunotherapyforgestational pages 1-2, baas2024immunotherapyforgestational pages 3-4) | Suggested NCIT terms: Pembrolizumab, Avelumab, Camrelizumab, Toripalimab, immune checkpoint inhibitor therapy, anti-PD-1 therapy, anti-PD-L1 therapy | Data are mostly single-arm, retrospective, or case-based, and encompass GTN broadly, including PSTT/ETT and refractory disease. |
| Fertility / follow-up | After chemotherapy completion with undetectable hCG, guideline follow-up is **monthly hCG for 1 year** with **oral hormonal contraception** during that period. Pregnancy after GTD is generally possible; recurrence risk cited as **0.7–2.6% after one prior GTD** and **~10% after two GTDs**; live birth rate cited as **75%** after GTD history (tempfer2023gestationalandnongestational pages 8-9, tempfer2023gestationalandnongestational pages 10-11) | Suggested terms: fertility preservation, contraception after GTN, hCG surveillance, pregnancy after GTD | Evidence is GTD-wide, not choriocarcinoma-only. Immunotherapy-era fertility data remain limited. |
| Prognosis | A 2023 review states GTN can achieve **near-100% cure with adequate treatment** and emphasizes markedly reduced mortality over time; high-risk disease still requires urgent multi-agent therapy, and ultra-high-risk/refractory disease remains a challenge (shahzadi2023reviewofcurrent pages 2-4, baas2024immunotherapyforgestational pages 6-7) | Suggested prognostic terms: complete remission, overall survival, relapse, chemotherapy resistance, ultra-high-risk disease | Prognosis is excellent in specialized centers for gestational disease, but not necessarily generalizable to nongestational germ-cell choriocarcinoma. |
| Current real-world trials | Recruiting/active studies include **NCT06028672** (toripalimab + actinomycin-D vs actinomycin-D for FIGO 5–6 GTN), **NCT05139095** (camrelizumab + apatinib + chemotherapy for ultra-high-risk or relapsed high-risk GTN), **NCT05635344** (single-dose neoadjuvant pembrolizumab before second evacuation for low-risk postmolar GTN), and **NCT04562558** (biweekly actinomycin-D vs multiday methotrexate in low-risk GTN) (NCT06028672 chunk 1, NCT05139095 chunk 1, NCT05635344 chunk 1) | Suggested NCIT/clinical trial terms: toripalimab, camrelizumab, apatinib, pembrolizumab, actinomycin-D, methotrexate, neoadjuvant immunotherapy | These studies are GTN-focused and often include but are not limited to choriocarcinoma. Most are not specific to nongestational choriocarcinoma. |
| Model systems | Choriocarcinoma-derived cell lines (**JAR, JEG-3, BeWo**) remain widely used as trophoblast surrogates, but reviews caution they differ substantially from normal trophoblast. Newer **human trophoblast stem cells** and **trophoblast organoids** better recapitulate placental biology; xenograft and germ-cell tumor models exist but incompletely model gestational choriocarcinoma (shibata2020uniquefeaturesand pages 8-9) | Suggested model terms: JAR cell line, JEG-3 cell line, BeWo cell line, trophoblast stem cell, trophoblast organoid, xenograft model | Model limitation is important: placental/trophoblast systems are not synonymous with malignant gestational choriocarcinoma, and many animal models do not capture human villous hemochorial placentation. |


*Table: This table condenses the most evidence-supported, ontology-oriented facts for a choriocarcinoma knowledge-base entry. It emphasizes where evidence is strong for gestational trophoblastic neoplasia and where caution is needed when extrapolating to pure choriocarcinoma or nongestational germ-cell disease.*

## 1. Disease information

### Definition and classification

Choriocarcinoma is a highly vascular, malignant trophoblastic neoplasm composed of cytotrophoblast and syncytiotrophoblast, typically without chorionic villi. Gestational tumors arise from placental trophoblast after a complete mole, abortion/ectopic pregnancy, or term/preterm pregnancy. NGC is a germ-cell malignancy and should be managed within ovarian/testicular germ-cell-tumor frameworks rather than assumed to share GC’s pregnancy-derived biology.

**Identifiers and terminology**

- **MONDO:** MONDO:0005207, choriocarcinoma. Related MONDO records found include placental choriocarcinoma (MONDO:0006374), uterine-corpus choriocarcinoma (MONDO:0004491), ovarian choriocarcinoma (MONDO:0003507), and testicular choriocarcinoma (MONDO:0003508). (OpenTargets Search: choriocarcinoma)
- **MeSH:** *Choriocarcinoma*.
- **ICD-10:** C58, malignant neoplasm of placenta; site-specific nongestational tumors may instead be coded under ovary, testis, or other primary site. O01 and D39.2 describe molar/uncertain-behavior placental disease and are not equivalent to choriocarcinoma.
- **Common synonyms:** chorionepithelioma, chorioepithelioma, gestational choriocarcinoma, trophoblastic choriocarcinoma, malignant gestational trophoblastic tumor.
- **Category:** rare malignant neoplasm; reproductive/placental disease; GTN when gestational; germ-cell tumor when nongestational.
- **OMIM/Orphanet:** no single Mendelian OMIM disease entry adequately represents sporadic choriocarcinoma. Maternal-effect genes associated with recurrent hydatidiform mole concern a precursor syndrome, not a universal inherited choriocarcinoma syndrome.

The information synthesized here is **aggregated disease-level evidence** from guidelines, reviews, studies, and trial records—not individual EHR data.

## 2. Etiology, risk, and protective factors

### Causal framework

GC results from malignant transformation/proliferation of pregnancy-derived trophoblast. A complete hydatidiform mole (CHM) is usually androgenetic and lacks a maternal nuclear genome; CHM has substantially greater malignant potential than partial mole. Loss of maternally expressed **CDKN1C/p57** is characteristic of androgenetic CHM, but it is a precursor-lesion mechanism rather than a somatic driver found in every GC. (shibata2020uniquefeaturesand pages 8-9, gonzalez2024gestationaltrophoblasticdisease pages 5-7)

NGC arises through germ-cell-tumor development. Adult germ-cell tumors commonly show chromosome 12p gain, but this cannot be transferred uncritically to GC. Ovarian germ-cell tumors show age- and histology-dependent copy-number changes, with 12p gain among recurrent abnormalities. (pinto2023molecularbiologyof pages 7-9)

### Risk factors

Established or consistently reported GTD/GTN risk correlates include previous molar pregnancy, maternal age at either extreme—especially ≥40 years—and Asian ancestry/geographic setting. A 2023 guideline reported increased incidence at ages 10–19 and 40–54, approximately twice the incidence in Asian versus White women, and overrepresentation of Black American women in some registers. These are primarily **GTD-level**, not choriocarcinoma-only, associations. (tempfer2023gestationalandnongestational pages 4-5, shahzadi2023reviewofcurrent pages 2-4)

A prior term pregnancy, long interval since antecedent pregnancy, high pretreatment hCG, large tumor burden, brain/liver metastasis, and previous failed chemotherapy are **adverse prognostic variables**, not necessarily etiologic risk factors. (tempfer2023gestationalandnongestational pages 4-5)

### Genetics and gene–environment interaction

Biallelic maternal-effect variants in **NLRP7** and **KHDC3L** cause susceptibility to recurrent hydatidiform mole through disturbed imprint establishment. They increase the opportunity for postmolar GTN but are not established as common inherited causes of sporadic GC. No validated population-scale GWAS, protective allele, or clinically actionable germline penetrance estimate was identified for choriocarcinoma itself.

No infectious cause is established. Smoking, alcohol, diet, exercise, occupational toxins, radiation, and pollution are not validated major causal factors. Consequently, no specific dietary, pharmacologic, or genetic protective factor is established beyond effective management and surveillance of precursor GTD. Evidence for a reproducible gene–environment interaction is insufficient.

## 3. Phenotypes

GC usually affects reproductive-age patients and can arise weeks to years after pregnancy. Onset may be acute through hemorrhage or more insidious through persistent hCG elevation. Suggested phenotype annotations include:

- **Abnormal uterine/vaginal bleeding**—common presenting sign; severity ranges from spotting to life-threatening hemorrhage. Suggested HPO: *Abnormal uterine bleeding*, *Vaginal bleeding*.
- **Elevated serum/urine hCG**—central laboratory abnormality; may cause nausea, ovarian theca-lutein cysts, or hyperthyroid manifestations at very high concentrations. Suggested HPO: *Elevated circulating human chorionic gonadotropin level*, *Hyperthyroidism*.
- **Anemia/hemorrhage**—from uterine or metastatic vascular deposits. Suggested HPO: *Anemia*, *Hemorrhage*.
- **Pulmonary disease**—cough, dyspnea, chest pain, or hemoptysis; lung is the most frequent metastatic site. Suggested HPO: *Dyspnea*, *Hemoptysis*, *Pulmonary metastases*.
- **Neurologic disease**—headache, focal deficit, seizure, or intracranial hemorrhage from brain metastasis. A recent GTN review estimated brain metastasis at presentation in about 11% of high-risk cohorts. Suggested HPO: *Headache*, *Seizure*, *Focal neurologic deficit*, *Intracranial hemorrhage*. (shahzadi2023reviewofcurrent pages 2-4)
- **Liver/GI metastasis**—abdominal pain, gastrointestinal bleeding, or catastrophic intra-abdominal hemorrhage; these sites confer adverse FIGO points. (tempfer2023gestationalandnongestational pages 4-5, shahzadi2023reviewofcurrent pages 2-4)
- **Renal manifestations**, reported across mole/choriocarcinoma, include proteinuria, nephrotic syndrome, impaired filtration, glomerulonephritis, and renal-vein thrombosis, but frequencies are poorly quantified.

Symptoms are rapidly progressive if untreated because trophoblast is invasive, angiogenic, and hematogenously disseminating. Quality-of-life burdens include bleeding, treatment toxicity, reproductive uncertainty, anxiety about hCG surveillance, and delayed conception. A recruiting study, NCT06169644, specifically evaluates psychological effects after GTN chemotherapy, reflecting an important evidence gap.

## 4. Genetic and molecular information

### Causal genes and variants

There is **no single validated causal gene or recurrent pathogenic germline variant** for ordinary GC. Routine ACMG-style single-gene testing, carrier frequency, penetrance, anticipation, founder-effect, and germline-mosaicism annotations are therefore not applicable.

Open Targets associates **DHFR**, **TP53**, and **GATA3** with choriocarcinoma. DHFR is also the pharmacologic target of methotrexate. These are disease/therapeutic associations, not proof that pathogenic variants in these genes cause GC. (OpenTargets Search: choriocarcinoma)

Candidate abnormalities reported across GTN include altered TP53, p21, RB, MYC, ERBB3, MDM2, and EGFR expression. A 2023 review notes the absence of activating EGFR kinase-domain mutations and therefore finds no established role for conventional EGFR-targeted therapy. (shahzadi2023reviewofcurrent pages 2-4)

### Epigenetics and chromosomal biology

Gestational tumors retain genetic material from the conceptus and often paternal alleles. STR genotyping or SNP-based analysis can establish gestational origin by demonstrating nonmaternal alleles and can distinguish GC from a maternal somatic carcinoma or NGC. CHM’s androgenetic imprinting pattern and absent p57 expression explain precursor trophoblast overgrowth, but frank GC has a more complex molecular landscape. (gonzalez2024gestationaltrophoblasticdisease pages 5-7)

In molar/GTN tissue, reported epigenetic abnormalities include imprinting disruption, altered microRNAs, and promoter methylation. **miR-196b** is reduced in CHM and inversely linked to MAP3K1, whereas **miR-21** is overexpressed and promotes trophoblast proliferation/invasion. These findings remain investigational and are not validated diagnostic tests for GC. (nasser2024molecularbasisof pages 12-13)

## 5. Environmental information

No toxin, radiation exposure, occupational agent, lifestyle behavior, or pathogen has been established as a direct cause. Geographic/ethnic differences may reflect reproductive patterns, nutrition, ascertainment, access to early ultrasound and hCG testing, or population genetics, but causal decomposition remains uncertain. There is no vaccine-relevant infectious agent.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream reproductive event:** abnormal fertilization and androgenetic CHM, or trophoblast persisting after another pregnancy.
2. **Failure of normal trophoblast control:** imprinting and cell-cycle dysregulation, altered apoptosis, growth-factor signaling, and persistence despite pregnancy resolution.
3. **Malignant trophoblast expansion:** cytotrophoblast proliferates while syncytiotrophoblast produces large quantities of hCG.
4. **Invasion/angiogenesis:** EMT-like programs, extracellular-matrix invasion, TGF-β signaling, and angiogenic factors produce a hemorrhagic uterine mass.
5. **Hematogenous dissemination:** lung first, then brain, liver, kidney, spleen, and GI tract; fragile vascular deposits explain hemoptysis and intracranial or intra-abdominal bleeding.
6. **Immune evasion:** trophoblast’s physiologic maternal–fetal immune-tolerance machinery, including PD-L1 and HLA-G, is co-opted by tumor.

A transcriptomic comparison found **33 differentially expressed genes** between CHM and postmolar GC, implicating TGF-β dysregulation and strong **SALL4** expression in GC. The study’s conclusion was: “the TGF-β pathway appears to be a crucial step in the progression of placental malignancies.” This was a small tumor-series result requiring validation. (jinkai2024prognosticatinggestationaltrophoblastic pages 9-10)

A 2024 prognostic review reported PD-L1 expression in 92.3% of GTN and identified investigational resistance pathways involving DPP4/cholesterol synthesis, RSK2–SOX8, and HLA-G; cfDNA signals involving BMPR1A and MAP3K1 were linked to severity. (jinkai2024prognosticatinggestationaltrophoblastic pages 9-10)

GTD studies also report p53/apoptosis imbalance, BCL-2/caspase dysregulation, EGFR/ERBB2/CD117 changes, oxidative stress, reduced E-cadherin, increased Twist-1, and proangiogenic PlGF. These are plausible contributors but much of the evidence comes from CHM or cell lines rather than causal intervention in human GC. (gonzalez2024gestationaltrophoblasticdisease pages 5-7, nasser2024molecularbasisof pages 12-13)

**Suggested GO processes:** trophoblast-cell proliferation; cell migration; epithelial-to-mesenchymal transition; extracellular-matrix organization; angiogenesis; TGF-β receptor signaling; apoptotic signaling; response to oxidative stress; immune-response inhibition. **Suggested CL cells:** trophoblast, cytotrophoblast, syncytiotrophoblast, extravillous trophoblast, endothelial cell, tumor-infiltrating lymphocyte. Subcellular emphasis includes nucleus/chromatin for imprinting and transcription, plasma membrane for PD-L1/HLA-G and receptors, and mitochondria/cytosol for apoptosis and redox metabolism.

No reproducible GC-specific metabolomic, lipidomic, spatial-transcriptomic, proteomic, or CRISPR-screen signature has yet reached clinical implementation.

## 7. Anatomical structures affected

- **Primary:** uterus/endometrium and antecedent placental implantation site in GC; ovary, testis, mediastinum, retroperitoneum, or CNS in NGC.
- **Secondary:** vagina/adnexa and broad ligament (FIGO II), lung (FIGO III), and brain, liver, kidney, spleen, or GI tract (FIGO IV). (shahzadi2023reviewofcurrent pages 2-4)
- **Suggested UBERON terms:** uterus, endometrium, placenta/chorion, vagina, ovary, testis, lung, brain, liver, kidney, spleen, gastrointestinal tract.
- **Tissue:** malignant trophoblastic epithelium with hemorrhage and necrosis; laterality is generally not meaningful for uterine GC, but ovarian/testicular primaries can be unilateral.

## 8. Temporal development

GC can follow any pregnancy and may present after an interval of months or years. A longer interval is adverse in FIGO scoring: <4, 4–6, 7–12, and >12 months receive progressively higher scores. Disease can progress rapidly because of vascular invasion and early hematogenous spread. (tempfer2023gestationalandnongestational pages 4-5)

FIGO stages are: I, confined to uterus; II, extension to genital structures; III, lung metastasis with or without genital involvement; IV, all other metastatic sites. Clinical course after treatment is tracked through quantitative hCG rather than anatomic imaging alone. Remission is usually treatment-induced; spontaneous normalization after complete surgical evacuation can occur in selected postmolar disease, but routine observation of histologically proven GC is not standard.

The critical intervention window is immediately after an abnormal postpregnancy hCG trend or histologic diagnosis, before high-volume liver/brain disease develops.

## 9. Inheritance and population epidemiology

GC is predominantly sporadic and is not inherited in Mendelian fashion. The relevant “genome” may be conceptus-derived rather than the patient’s constitutional genome. NLRP7/KHDC3L-associated recurrent mole is recessive maternal-effect disease, but progression to GC is not fully penetrant.

A 2023 guideline reported hydatidiform-mole prevalence of **1/591 pregnancies**, GTD prevalence of **1/714 live births**, and Dutch GTD incidence of **1.67/1,000 births/year**. These figures must not be mislabeled as choriocarcinoma-specific incidence. (tempfer2023gestationalandnongestational pages 4-5)

The sex distribution depends on subtype: GC occurs in patients with a pregnancy; NGC affects both sexes. Gestational disease clusters in reproductive years, while ovarian/testicular and extragonadal germ-cell tumors also occur in children, adolescents, and young adults.

## 10. Diagnostics

### Core tests

1. **Quantitative serum β-hCG**, repeated in the same laboratory/assay where possible. Urine hCG and alternative assays help investigate heterophile-antibody “phantom hCG” or unusual hCG forms.
2. **Pelvic examination and transvaginal ultrasound.**
3. **Staging imaging:** CT chest and abdomen plus brain MRI; FDG-PET/CT is optional for unresolved suspected metastasis. (tempfer2023gestationalandnongestational pages 8-9)
4. **Histopathology:** biphasic malignant cytotrophoblast/syncytiotrophoblast, marked atypia, hemorrhage and necrosis, and no chorionic villi. Biopsy of highly vascular metastases should be avoided when diagnosis can be made safely through hCG and clinical context.
5. **IHC:** hCG highlights syncytiotrophoblast; broad cytokeratin, GATA3, inhibin, SALL4 and other trophoblast/germ-cell markers may support the diagnosis. p57 is principally a CHM differential marker, not a stand-alone GC test. In CHM diagnosis, adding p57 increased pathologist sensitivity to approximately 93–96% and specificity to 96–98%. (gonzalez2024gestationaltrophoblasticdisease pages 5-7)
6. **STR/SNP genotyping:** recommended when gestational origin is uncertain, especially for ovarian disease, remote pregnancy, unusual primary site, or distinction from a maternal carcinoma.

### Diagnostic criteria and staging

Postmolar GTN criteria include four hCG values forming a plateau over at least three weeks, serial hCG rise, or persistent detectable hCG beyond six months; exact rise definitions vary slightly among guidelines. Histologically confirmed choriocarcinoma itself establishes GTN even without these serial criteria. (tempfer2023gestationalandnongestational pages 15-16, NCT06028672 chunk 1)

The FIGO/WHO prognostic score includes age, antecedent pregnancy, interval, hCG, largest tumor, number/site of metastases, and prior chemotherapy: 0–4 low, 5–6 intermediate, and ≥7 high risk in the cited guideline. Brain/liver metastasis and multiple failed regimens carry the highest weights. (tempfer2023gestationalandnongestational pages 4-5)

### Differential diagnosis

Important alternatives are retained products/new pregnancy, invasive mole, PSTT/ETT, placental-site nodule, ectopic pregnancy, placental-site exaggerated reaction, hCG-producing germ-cell tumor, poorly differentiated carcinoma, melanoma, sarcoma, and phantom/pituitary hCG. WES/WGS, broad germline panels, CMA, mitochondrial testing, and repeat-expansion testing are **not routine**. Tumor sequencing may be useful only in refractory or diagnostically unresolved disease.

There is no population screening program. Surveillance after molar pregnancy is targeted secondary prevention.

## 11. Outcome and prognosis

Gestational disease is among the most curable metastatic solid tumors when managed in a specialist center. A 2023 review states that adequate treatment can approach 100% overall cure and reports **93% complete remission** with EMA-CO in high-risk GTN; approximately 40% of incomplete responders were salvageable using platinum-based multi-agent chemotherapy. (shahzadi2023reviewofcurrent pages 2-4)

A 2024 review reported stage-I choriocarcinoma cure of **83% with single-agent chemotherapy**, with further remissions after additional treatment; later stages require multi-modality management. The figure derives from earlier series and should not be interpreted as a contemporary population survival estimate. (gonzalez2024gestationaltrophoblasticdisease pages 10-11, gonzalez2024gestationaltrophoblasticdisease pages 8-10)

Adverse factors include liver/brain metastasis, very high hCG, large/multiple tumors, term-pregnancy antecedent, interval >12 months, choriocarcinoma histology, and prior failed chemotherapy. Untreated disease is frequently fatal from hemorrhage or organ involvement.

Reproductive prognosis is generally favorable: one review reported an **86.7% fertility rate** among patients desiring conception after treatment for choriocarcinoma/invasive mole. GTD-wide data report a 75% live-birth rate, recurrence of 0.7–2.6% after one GTD and about 10% after two, with no clear excess of congenital malformations. (gonzalez2024gestationaltrophoblasticdisease pages 10-11, tempfer2023gestationalandnongestational pages 10-11)

Long-term morbidity includes chemotherapy-related myelosuppression, mucositis, alopecia, neuropathy, renal/hepatic injury, premature ovarian impairment, psychological distress, and a dose-related risk of therapy-related myeloid leukemia after etoposide. After MTX and EMA-CO, regular menses were reported in 12/12 and 32/34 women, respectively. (tempfer2023gestationalandnongestational pages 10-11)

## 12. Treatment

### Risk-adapted gestational treatment

- **Low risk:** methotrexate with folinic/folic-acid rescue or actinomycin-D. The cited guideline uses MTX 50 mg IM on days 1, 3, 5 and 7 with folic acid 15 mg orally on days 2, 4, 6 and 8; resistance prompts actinomycin-D 1.25 mg/m² every two weeks or EMA-CO. (tempfer2023gestationalandnongestational pages 15-16)
- Comparative studies summarized in 2023 found complete-remission rates of **80% versus 65%**, **73% versus 58%**, and **90% versus 48%** for actinomycin-D versus alternative MTX schedules. Five-day MTX cured 226/253 patients (89.3%) in one center. MTX remains common because it generally causes less alopecia/toxicity. (shahzadi2023reviewofcurrent pages 2-4)
- **FIGO 5–6/choriocarcinoma:** multi-agent EMA-CO should be considered when distant metastasis, very high hCG, or choriocarcinoma histology is present because single-agent resistance is more likely. (tempfer2023gestationalandnongestational pages 15-16)
- **High risk:** EMA-CO; EP/EMA or EMA-EP are important alternatives/salvage regimens. Ultra-high-risk disease may receive low-dose weekly etoposide/cisplatin induction to reduce fatal hemorrhage/tumor-collapse risk. (tempfer2023gestationalandnongestational pages 9-10)
- **Brain metastasis:** higher-dose MTX with CNS penetration and individualized surgery/radiotherapy. A review reported five-year survival of 81.5% with intensive treatment. (shahzadi2023reviewofcurrent pages 2-4)

Suggested NCIt interventions: Methotrexate; Leucovorin/Folinic Acid; Dactinomycin; Etoposide; Cisplatin; Cyclophosphamide; Vincristine; EMA-CO; EMA-EP; EP/EMA; BEP; Combination Chemotherapy.

### Surgery

Suction evacuation treats molar precursors, not metastatic GC. Hysterectomy can control uterine hemorrhage or isolated chemoresistant disease and is considered when fertility is not desired. Resection of isolated lung, brain, liver, or other resistant deposits can salvage selected patients. Surgery should complement—not replace—systemic therapy for most GC.

### Immunotherapy: major 2023–2024 development

GTN strongly expresses PD-L1, providing unusually compelling biologic rationale for checkpoint blockade. Across 133 checkpoint-inhibitor-treated patients summarized in 2023/2024, **85 achieved complete remission**: 77/118 with high-risk, relapsed, or multidrug-resistant disease and 8/15 with low-risk disease. One complete responder relapsed 22 months after stopping therapy. (baas2024immunotherapyforgestational pages 1-2)

A 66-patient refractory/relapsed cohort had 46 complete and six partial responses; 25 experienced grade 3–4 toxicity. Camrelizumab plus apatinib produced 10 complete responses among 20 high-risk patients, with grade-3 toxicity in 12. High-risk avelumab monotherapy performed poorly in a separate seven-patient study (one complete response), showing that checkpoint agents and settings are not interchangeable. (baas2024immunotherapyforgestational pages 3-4)

UK expert practice cited in the review uses pembrolizumab after failure of at least two multi-agent lines, including EMA-CO, and continues therapy to hCG/radiologic remission followed by consolidation. The review concludes: “anti-PD-1 salvage treatment in multidrug resistant disease is now a standard of care,” while emphasizing cost, fertility uncertainty, and limited long-term data. (baas2024immunotherapyforgestational pages 2-2, baas2024immunotherapyforgestational pages 6-7)

### Current trials and real-world implementation

- **NCT06028672**, recruiting: toripalimab 200 mg IV every two weeks plus actinomycin-D 1.25 mg/m² versus actinomycin-D alone for FIGO 5–6 GTN; estimated n=40; includes AMH, QLQ-C30 and reproductive-concern outcomes. https://clinicaltrials.gov/study/NCT06028672 (NCT06028672 chunk 1)
- **NCT05139095**, recruiting phase II: camrelizumab plus apatinib and chemotherapy for ultra-high-risk or multiply treated high-risk GTN; estimated n=70. https://clinicaltrials.gov/study/NCT05139095 (NCT05139095 chunk 1)
- **NCT05635344/RESOLVE**, recruiting phase II: one 200-mg pembrolizumab dose before second evacuation versus surgery alone for low-risk postmolar GTN; choriocarcinoma is excluded. https://clinicaltrials.gov/study/NCT05635344 (NCT05635344 chunk 1)
- **NCT04562558**, active, not recruiting: biweekly actinomycin-D versus multiday MTX in low-risk GTN; n=228. https://clinicaltrials.gov/study/NCT04562558

No gene, RNA, CAR-T, or approved cell therapy is established. Pharmacogenomic guidance is not standard; DHFR biology is relevant to MTX, but no CPIC genotype-directed regimen exists.

## 13. Prevention

There is no known primary prevention, vaccine, prophylactic medication, or lifestyle program. Prophylactic chemotherapy after a successfully evacuated mole with falling/negative hCG is not recommended in the cited guideline. (tempfer2023gestationalandnongestational pages 15-16)

**Secondary prevention** consists of centralized pathology review, complete evacuation of molar pregnancy, and serial hCG. After mole, the guideline recommends weekly hCG until at least two consecutive negatives, followed by monthly testing for at least six months; higher-risk circumstances may warrant longer monitoring. (tempfer2023gestationalandnongestational pages 15-16)

**Tertiary prevention** includes risk-adapted chemotherapy, prompt evaluation of neurologic/hepatic symptoms, safe management of hemorrhage, and post-treatment hCG monitoring. After chemotherapy, at least three consecutive weekly undetectable values are followed by monthly hCG for one year with hormonal contraception, because pregnancy hCG would obscure relapse detection. (tempfer2023gestationalandnongestational pages 9-10, tempfer2023gestationalandnongestational pages 8-9)

Patients with recurrent moles should receive reproductive-genetics assessment for NLRP7/KHDC3L-related disease. Future pregnancy should include early ultrasound, placental histology when indicated, and postpartum hCG confirmation.

## 14. Other species and natural disease

Naturally occurring choriocarcinoma-like trophoblastic tumors are reported sporadically in domestic and laboratory mammals, but no common veterinary counterpart reproduces human gestational disease sufficiently for direct clinical translation. There is no zoonotic transmission. No breed-specific VBO association or conserved single causal ortholog was established from the retrieved evidence.

Comparative interpretation is limited because human placentation and trophoblast invasion differ markedly from those of common laboratory rodents. Nonhuman primates have closer placental biology, but their use is constrained by cost and ethics.

## 15. Model organisms and experimental systems

**Cell lines:** BeWo, JAR, and JEG-3 choriocarcinoma lines are widely used for hCG secretion, syncytialization, transport, invasion, viral-entry, and drug studies. Their major limitation is that they are transformed, karyotypically abnormal tumor cells and “are quite different from normal trophoblast cells,” as a placental-model review states. (shibata2020uniquefeaturesand pages 8-9)

**Modern models:** human trophoblast stem cells express GATA3/TFAP2C, low HLA class I, hypomethylated ELF5, and C19MC; they differentiate toward syncytiotrophoblast and extravillous trophoblast. First-trimester trophoblast organoids contain cytotrophoblast- and syncytiotrophoblast-like populations and can produce EVT-like cells. These systems better model normal lineage biology but are not full GC models. (shibata2020uniquefeaturesand pages 8-9)

**In vivo:** immunodeficient-mouse xenografts of choriocarcinoma lines can test tumor growth, metastasis and drug response. Germ-cell-tumor patient-derived xenografts preserve some histologic and chemosensitivity features, but pure choriocarcinoma PDX resources are scarce. Mouse placenta differs from human villous hemochorial placenta, limiting developmental inference.

**Priority research needs:** patient-derived GC organoids/PDXs; matched tumor–antecedent-pregnancy sequencing; single-cell and spatial profiling of malignant trophoblast and immune cells; prospective validation of PD-L1, HLA-G and cfDNA; and functional screens for MTX/EMA-CO resistance.

## Key recent sources and expert interpretation

- Tempfer et al., DGGG/OEGGG/SGGG guideline, published **March 2023**, DOI: https://doi.org/10.1055/a-1904-6461. This is the strongest retrieved source for diagnosis, FIGO risk, imaging, treatment and surveillance, but it is an S2k consensus guideline rather than a formally graded systematic guideline. (tempfer2023gestationalandnongestational pages 9-10, tempfer2023gestationalandnongestational pages 4-5, tempfer2023gestationalandnongestational pages 8-9)
- Shahzadi et al., review published **November 2023**, DOI: https://doi.org/10.1186/s43046-023-00195-y. Its abstract states that EMA-CO “leads to complete remission in 93% of high-risk GTN patients.” (shahzadi2023reviewofcurrent pages 2-4)
- Baas et al., immunotherapy review published online **September 2023** and in the 2024 journal volume, DOI: https://doi.org/10.1159/000533972. Its abstract reports 133 CPI-treated patients and 85 complete remissions, establishing checkpoint blockade as the leading contemporary development. (baas2024immunotherapyforgestational pages 1-2)
- Gonzalez et al., published **July 2024**, DOI: https://doi.org/10.3390/diseases12070159, provides current precursor-mole pathology, p57/genotyping, fertility and summarized treatment outcomes. (gonzalez2024gestationaltrophoblasticdisease pages 10-11, gonzalez2024gestationaltrophoblasticdisease pages 5-7)
- Jin-Kai et al., published **November 2024**, DOI: https://doi.org/10.1016/j.eclinm.2024.102890, argues that FIGO 2000 should evolve toward molecular/biomarker-integrated prognostication while retaining its proven clinical utility. (jinkai2024prognosticatinggestationaltrophoblastic pages 9-10)
- Nasser et al., published **August 2024**, DOI: https://doi.org/10.3390/ijms25168739, systematically reviews 71 studies of molecular GTD biology. Its evidence chiefly concerns moles and should not be presented as direct proof in GC. (nasser2024molecularbasisof pages 12-13)

**Overall conclusion.** Gestational choriocarcinoma is a rare, rapidly invasive and hemorrhagic trophoblastic cancer but is exceptionally chemosensitive. Serial quantitative hCG, FIGO/WHO risk stratification, complete metastatic imaging, and specialist-center treatment remain the clinical foundation. The most important recent advance is PD-1/PD-L1 blockade for multidrug-resistant disease. Conversely, claims about causal somatic genes, protective factors, single-cell states, metabolomics, or genotype-guided treatment remain preliminary. Nongestational choriocarcinoma must be separately classified and treated as germ-cell cancer rather than automatically assigned gestational algorithms.

References

1. (OpenTargets Search: choriocarcinoma): Open Targets Query (choriocarcinoma, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (tempfer2023gestationalandnongestational pages 4-5): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

3. (shahzadi2023reviewofcurrent pages 2-4): Mehwish Shahzadi, Saqib Raza Khan, Muhammad Tariq, Sehrish Sarwar Baloch, Aisha Shahid, Munira Moosajee, and Zarka Samon. Review of current literature on gestational trophoblastic neoplasia. Journal of the Egyptian National Cancer Institute, Nov 2023. URL: https://doi.org/10.1186/s43046-023-00195-y, doi:10.1186/s43046-023-00195-y. This article has 16 citations.

4. (gonzalez2024gestationaltrophoblasticdisease pages 5-7): Jeffrey Gonzalez, Meagan Popp, Stephanie Ocejo, Alvaro Abreu, Hisham F. Bahmad, and Robert Poppiti. Gestational trophoblastic disease: complete versus partial hydatidiform moles. Diseases, 12:159, Jul 2024. URL: https://doi.org/10.3390/diseases12070159, doi:10.3390/diseases12070159. This article has 27 citations.

5. (shibata2020uniquefeaturesand pages 8-9): Shun Shibata, Eri H. Kobayashi, Norio Kobayashi, Akira Oike, Hiroaki Okae, and Takahiro Arima. Unique features and emerging in vitro models of human placental development. Reproductive Medicine and Biology, 19:301-313, Sep 2020. URL: https://doi.org/10.1002/rmb2.12347, doi:10.1002/rmb2.12347. This article has 33 citations and is from a peer-reviewed journal.

6. (tempfer2023gestationalandnongestational pages 8-9): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

7. (tempfer2023gestationalandnongestational pages 10-11): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

8. (jinkai2024prognosticatinggestationaltrophoblastic pages 9-10): Lin Jin-Kai, Jiang Fang, and Xiang Yang. Prognosticating gestational trophoblastic neoplasia: from figo 2000 to future models. eClinicalMedicine, 77:102890, Nov 2024. URL: https://doi.org/10.1016/j.eclinm.2024.102890, doi:10.1016/j.eclinm.2024.102890. This article has 13 citations and is from a peer-reviewed journal.

9. (nasser2024molecularbasisof pages 12-13): Shadha Nasser, Mohammed Bahutair, R. Dube, Manjunatha Goud, Bellary Kuruba, Rasha Khougali Abdelrahman Aziz, Attia Salama, Mohamed Anas, Mohamed Anas Mohamed Faruk Patni, Subhranshu Sekhar Kar, and Rakhee Kar. Molecular basis of hydatidiform moles—a systematic review. International Journal of Molecular Sciences, 25:8739, Aug 2024. URL: https://doi.org/10.3390/ijms25168739, doi:10.3390/ijms25168739. This article has 13 citations.

10. (baas2024immunotherapyforgestational pages 2-3): Inge O. Baas, Anneke M. Westermann, Benoit You, Pierre-Adrien Bolze, Michael Seckl, and Ehsan Ghorani. Immunotherapy for gestational trophoblastic neoplasia: a new paradigm. Gynecologic and Obstetric Investigation, 89:230-238, Sep 2023. URL: https://doi.org/10.1159/000533972, doi:10.1159/000533972. This article has 49 citations and is from a peer-reviewed journal.

11. (baas2024immunotherapyforgestational pages 2-2): Inge O. Baas, Anneke M. Westermann, Benoit You, Pierre-Adrien Bolze, Michael Seckl, and Ehsan Ghorani. Immunotherapy for gestational trophoblastic neoplasia: a new paradigm. Gynecologic and Obstetric Investigation, 89:230-238, Sep 2023. URL: https://doi.org/10.1159/000533972, doi:10.1159/000533972. This article has 49 citations and is from a peer-reviewed journal.

12. (baas2024immunotherapyforgestational pages 6-7): Inge O. Baas, Anneke M. Westermann, Benoit You, Pierre-Adrien Bolze, Michael Seckl, and Ehsan Ghorani. Immunotherapy for gestational trophoblastic neoplasia: a new paradigm. Gynecologic and Obstetric Investigation, 89:230-238, Sep 2023. URL: https://doi.org/10.1159/000533972, doi:10.1159/000533972. This article has 49 citations and is from a peer-reviewed journal.

13. (tempfer2023gestationalandnongestational pages 9-10): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

14. (tempfer2023gestationalandnongestational pages 15-16): Clemens Tempfer, Lars-Christian Horn, Sven Ackermann, Ralf Dittrich, Jens Einenkel, Andreas Günthert, Heidemarie Haase, Jürgen Kratzsch, Michael Kreißl, Stephan Polterauer, Andreas Ebert, Eric Steiner, Falk Thiel, Michael Eichbaum, Tanja Fehm, Martin C. Koch, and Paul Gass. Gestational and non-gestational trophoblastic neoplasia. guideline of the dggg, oeggg and sggg (s2k-level, awmf registry no. 032/049, april 2022). Geburtshilfe und Frauenheilkunde, 83:267-288, Mar 2023. URL: https://doi.org/10.1055/a-1904-6461, doi:10.1055/a-1904-6461. This article has 2 citations and is from a peer-reviewed journal.

15. (NCT06028672 chunk 1): xiang yang. Toripalimab Plus Actinomycin-D as Fist-Line Treatment for GTN With FIGO Score 5-6. Peking Union Medical College Hospital. 2023. ClinicalTrials.gov Identifier: NCT06028672

16. (NCT05635344 chunk 1):  A Feasibility Window Study of Pembrolizumab Prior to Second Evacuation for Post-molar Gestational Trophoblastic Neoplasia. Imperial College London. 2024. ClinicalTrials.gov Identifier: NCT05635344

17. (gonzalez2024gestationaltrophoblasticdisease pages 10-11): Jeffrey Gonzalez, Meagan Popp, Stephanie Ocejo, Alvaro Abreu, Hisham F. Bahmad, and Robert Poppiti. Gestational trophoblastic disease: complete versus partial hydatidiform moles. Diseases, 12:159, Jul 2024. URL: https://doi.org/10.3390/diseases12070159, doi:10.3390/diseases12070159. This article has 27 citations.

18. (gonzalez2024gestationaltrophoblasticdisease pages 8-10): Jeffrey Gonzalez, Meagan Popp, Stephanie Ocejo, Alvaro Abreu, Hisham F. Bahmad, and Robert Poppiti. Gestational trophoblastic disease: complete versus partial hydatidiform moles. Diseases, 12:159, Jul 2024. URL: https://doi.org/10.3390/diseases12070159, doi:10.3390/diseases12070159. This article has 27 citations.

19. (baas2024immunotherapyforgestational pages 1-2): Inge O. Baas, Anneke M. Westermann, Benoit You, Pierre-Adrien Bolze, Michael Seckl, and Ehsan Ghorani. Immunotherapy for gestational trophoblastic neoplasia: a new paradigm. Gynecologic and Obstetric Investigation, 89:230-238, Sep 2023. URL: https://doi.org/10.1159/000533972, doi:10.1159/000533972. This article has 49 citations and is from a peer-reviewed journal.

20. (baas2024immunotherapyforgestational pages 3-4): Inge O. Baas, Anneke M. Westermann, Benoit You, Pierre-Adrien Bolze, Michael Seckl, and Ehsan Ghorani. Immunotherapy for gestational trophoblastic neoplasia: a new paradigm. Gynecologic and Obstetric Investigation, 89:230-238, Sep 2023. URL: https://doi.org/10.1159/000533972, doi:10.1159/000533972. This article has 49 citations and is from a peer-reviewed journal.

21. (NCT05139095 chunk 1):  Camrelizumab Plus Apatinib in Patients With High-risk Gestational Trophoblastic Neoplasia. Peking Union Medical College Hospital. 2022. ClinicalTrials.gov Identifier: NCT05139095

22. (pinto2023molecularbiologyof pages 7-9): Mariana Tomazini Pinto, Gisele Eiras Martins, Ana Glenda Santarosa Vieira, Janaina Mello Soares Galvão, Cristiano de Pádua Souza, Carla Renata Pacheco Donato Macedo, and Luiz Fernando Lopes. Molecular biology of pediatric and adult ovarian germ cell tumors: a review. Cancers, 15:2990, May 2023. URL: https://doi.org/10.3390/cancers15112990, doi:10.3390/cancers15112990. This article has 24 citations.

## Artifacts

- [Edison artifact artifact-00](Choriocarcinoma-deep-research-falcon_artifacts/artifact-00.md)
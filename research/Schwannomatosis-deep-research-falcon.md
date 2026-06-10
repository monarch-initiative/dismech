---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-08T18:04:39.921543'
end_time: '2026-06-08T18:17:33.667145'
duration_seconds: 773.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Schwannomatosis
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 42
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Schwannomatosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Schwannomatosis
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Schwannomatosis** covering all of the
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
- **Disease Name:** Schwannomatosis
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Schwannomatosis** covering all of the
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


# Schwannomatosis — Comprehensive Disease Characteristics Report (Neoplastic)

## Target Disease
- **Disease name:** Schwannomatosis
- **Category:** Neoplastic (benign peripheral nerve sheath tumor predisposition syndrome)
- **MONDO ID:** **MONDO:0008075** (schwannomatosis) (OpenTargets Search: Schwannomatosis)

---

## Executive summary (current understanding)
Schwannomatosis is now used as an **umbrella term** (internationally updated in 2022) for inherited tumor-predisposition syndromes characterized by development of multiple schwannomas, and subdivided by the causal gene (e.g., **NF2-related schwannomatosis**, **SMARCB1-related schwannomatosis**, **LZTR1-related schwannomatosis**) rather than older “NF2 vs schwannomatosis” separation. (tamura2024historicaldevelopmentof pages 1-3, nagasaka2025geneticbasisand pages 1-2, rai2025classificationofschwannomas pages 1-2)

Two key clinical axes dominate disease burden and real-world management:
1) **Tumor burden** (schwannomas; plus meningiomas/ependymomas in NF2-related forms). (tamura2024historicaldevelopmentof pages 1-3, evans2025historyandclinical pages 1-2)
2) **Pain and quality-of-life impairment**, often not well correlated with tumor size/burden. (nagasaka2025geneticbasisand pages 1-2, chiassonmackenzie2023cellularmechanismsof pages 1-2)

---

## 1. Disease information

### 1.1 What is the disease?
Schwannomatosis comprises gene-defined tumor predisposition syndromes marked by multiple schwannomas (benign peripheral nerve sheath tumors), often affecting cranial, spinal, and peripheral nerves; NF2-related schwannomatosis also features meningiomas and sometimes ependymomas. (tamura2024historicaldevelopmentof pages 1-3, perrino2025updateoncancer pages 5-7, evans2025historyandclinical pages 1-2)

**Direct abstract quote (definition/nomenclature):**
- Tamura et al. (2024) state that the 2022 expert committee “**recommended the use of ‘schwannomatosis’ as an umbrella term for conditions that predispose to schwannomas**” and that “**Each type of schwannomatosis was classified by the gene containing the disease-causing pathogenic variant**.” (Published online 2024-06-19; Neurologia medico-chirurgica) (tamura2024historicaldevelopmentof pages 1-3)

### 1.2 Key identifiers
**Available from current tool-derived evidence (MONDO/OpenTargets):**
- **MONDO:0008075** schwannomatosis. (OpenTargets Search: Schwannomatosis)
- Related MONDO subtype entities observed: **NF2-related schwannomatosis (MONDO:0007039)**, **SMARCB1-related schwannomatosis (MONDO:0024517)**, **LZTR1-related schwannomatosis (MONDO:0014299)**. (OpenTargets Search: Schwannomatosis)

**Not retrieved in the present evidence set:** OMIM, Orphanet (ORPHA), ICD-10/ICD-11, and MeSH identifiers were not directly retrievable from the documents/tools accessed in this run; these should be added by querying OMIM/Orphanet/MeSH directly in a complementary curation step. (evidence gap)

### 1.3 Synonyms / alternative names
- **NF2-related schwannomatosis**: formerly “neurofibromatosis type 2 (NF2)”. (tamura2024historicaldevelopmentof pages 1-3, rai2025classificationofschwannomas pages 1-2)
- “Schwannomatosis” historically overlapped with terms such as “neurilemmomatosis” and earlier NF2 diagnostic framing, but modern usage is gene-based. (tamura2024historicaldevelopmentof pages 1-3)

### 1.4 Evidence source type
This report is primarily derived from:
- Aggregated **disease-level resources and consensus reviews** (e.g., 2024 diagnostic criteria evolution review). (tamura2024historicaldevelopmentof pages 1-3)
- **Human cohorts** undergoing genetic testing. (smith2024geneticfindingsin pages 1-5)
- **ClinicalTrials.gov trial registry records** (real-world implementations of experimental therapeutics). (NCT05684692 chunk 1, NCT04163419 chunk 1, NCT04374305 chunk 1)
- **Mechanistic preclinical research** (mouse + cell systems) for NF2-mutant schwannoma biology. (chiassonmackenzie2023cellularmechanismsof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** inherited (or mosaic) pathogenic variants predisposing to schwannoma formation, most commonly involving chromosome 22 genes:
- **NF2** (merlin tumor suppressor) → NF2-related schwannomatosis; mosaicism is common in de novo disease. (tamura2024historicaldevelopmentof pages 1-3, evans2025historyandclinical pages 1-2)
- **SMARCB1** and **LZTR1** → non-NF2 schwannomatosis forms, with characteristic multi-hit tumorigenesis involving chromosome 22 loss and somatic NF2 events. (tamura2024historicaldevelopmentof pages 3-4, nagasaka2025geneticbasisand pages 1-2)

**Quantitative contribution (familial vs isolated, from a recent diagnostic criteria review):**
- SMARCB1/LZTR1 “**account for 70%–85% of familial schwannomatosis and 30%–40% of isolated cases**.” (Tamura et al., 2024) (tamura2024historicaldevelopmentof pages 3-4)

### 2.2 Risk factors
#### Genetic risk factors
- Pathogenic/likely pathogenic germline variants in **NF2, SMARCB1, LZTR1** are the major recognized inherited risk factors. (OpenTargets Search: Schwannomatosis, perrino2025updateoncancer pages 5-7)
- **Mosaic NF2** is a frequent explanation for individuals with multiple schwannomas who do not meet classic clinical criteria; tumor-pair testing can reveal shared NF2 variants. (smith2024geneticfindingsin pages 1-5, tamura2024historicaldevelopmentof pages 3-4)

**Cohort statistics (2024 J Med Genet):**
In 154 people with at least one non-vestibular schwannoma (not meeting NF2-SWN clinical criteria at time of testing):
- Germline **SMARCB1** variants: **17/154 (11%)**.
- Germline **LZTR1** variants: **19/154 (12%)**.
- **NF2 variants** in 19 people, **18 mosaic**, and **17 detected only when two tumors were available**.
- Diagnostic yield: **25% blood-only** vs **36% with tumor analysis**. (Smith et al., 2024; published 2024-08; Journal of Medical Genetics) (smith2024geneticfindingsin pages 1-5)

#### Environmental risk factors
No specific environmental exposures were identified in the retrieved evidence as established risk factors for schwannomatosis onset. (evidence gap)

### 2.3 Protective factors
No genetic or environmental protective factors were identified in the retrieved evidence set. (evidence gap)

### 2.4 Gene–environment interactions
No gene–environment interaction evidence was identified in the retrieved evidence set. (evidence gap)

---

## 3. Phenotypes

### 3.1 Core phenotype domains and suggested HPO terms
Below are common phenotype groupings supported by the retrieved evidence, with suggested HPO annotations (HPO terms provided as curation suggestions; exact IDs should be confirmed during ontology mapping):

1) **Schwannomas (multiple)**
- HPO suggestion: Peripheral nerve schwannoma; Cranial nerve schwannoma; Spinal schwannoma.
- Evidence: hallmark across schwannomatosis subtypes; NF2-related often with bilateral vestibular schwannomas. (perrino2025updateoncancer pages 5-7, evans2025historyandclinical pages 1-2)

2) **Vestibular schwannoma / hearing and balance deficits (esp. NF2-related)**
- HPO suggestions: Hearing loss; Vestibular dysfunction; Tinnitus.
- Evidence: NF2-related schwannomatosis commonly presents with bilateral vestibular schwannomas; Freier cohort reports hearing problems affecting activities. (evans2025historyandclinical pages 1-2, freier2024theimpactof pages 3-4)

3) **Pain (chronic, often severe; especially non-NF2 forms)**
- HPO suggestions: Chronic pain; Neuropathic pain; Allodynia (if present); Painful peripheral nerve tumor.
- Evidence: pain is a dominant symptom and may be poorly correlated with tumor burden. (nagasaka2025geneticbasisand pages 1-2, chiassonmackenzie2023cellularmechanismsof pages 1-2)

4) **Meningioma and ependymoma (more typical in NF2-related)**
- HPO suggestions: Meningioma; Ependymoma.
- Evidence: NF2-related syndromic spectrum includes meningiomas and less commonly ependymoma. (perrino2025updateoncancer pages 5-7, evans2025historyandclinical pages 1-2)

5) **Psychological burden / QoL impairment (NF2-related evidence strongest in retrieved set)**
- HPO suggestions: Depressive mood; Anxiety; Reduced quality of life.
- Evidence: depression/anxiety prevalence and QoL correlations in NF2-SWN. (freier2024theimpactof pages 1-2)

### 3.2 Age of onset and progression
- NF2-related schwannomatosis is described as autosomal dominant with complete penetrance and progressive morbidities, with monitoring based on neurologic deficits, imaging, and audiometry. (freier2024theimpactof pages 1-2)
- Schwannomas can have variable natural histories and growth rates, even within the same patient; pain/tumor burden correlation is weak. (chiassonmackenzie2023cellularmechanismsof pages 1-2)

### 3.3 Frequency / statistics for selected phenotypes
#### Pain frequency
- In the tanezumab schwannomatosis pain trial registry record: “**Pain is the most frequent symptom reported by these patients, with 68% experiencing chronic pain**.” (ClinicalTrials.gov NCT04163419; last update posted 2024-03-13) (NCT04163419 chunk 1)

#### NF2-related QoL and mental health statistics (2024 peer-reviewed)
Freier et al. (Scientific Reports; published 2024-03) reported among NF2-SWN patients:
- “**Questionnaires were completed by 77 patients**” and “**Physician-rated disease severity scores were available for 55 patients**.” (freier2024theimpactof pages 1-2)
- “**High prevalence of clinically relevant symptoms of depression (30%), anxiety (16%), and somatic burden (32%)**.” (freier2024theimpactof pages 1-2)
- NF2-SWN-related QoL associated with physician severity **r = 0.614**, and a regression model explained **64%** of variance in QoL. (freier2024theimpactof pages 1-2)

### 3.4 Quality of life impact
- NF2-SWN: substantial psychosocial and functional burden; authors highlight strong association of QoL with depression symptoms and modifiable constructs (personality functioning). (freier2024theimpactof pages 1-2)
- Schwannomatosis pain burden: pain is commonly chronic and treatment-resistant, and surgery can lead to persistent/recurrent pain due to nerve injury or recurrence. (hino2025optimaldeliveryof pages 1-2)

---

## 4. Genetic / molecular information

### 4.1 Causal genes (major)
- **NF2** (merlin tumor suppressor). (tamura2024historicaldevelopmentof pages 1-3)
- **SMARCB1** (SWI/SNF chromatin remodeling complex component). (madison2026schwannomatosistumormodeling pages 1-2)
- **LZTR1** (CUL3 adaptor; RAS ubiquitination regulator). (madison2026schwannomatosistumormodeling pages 1-2)

OpenTargets disease–target associations for schwannomatosis highlight **LZTR1, SMARCB1, NF2**. (OpenTargets Search: Schwannomatosis)

### 4.2 Pathogenic variants and variant spectrum (from retrieved evidence)
- Mosaic NF2 is common and often requires tumor testing to identify; in the Manchester cohort, 18/19 NF2 findings were mosaic and most required testing of two tumors. (smith2024geneticfindingsin pages 1-5)
- Detection quality requirements for somatic variants: neoplastic content ≥20% and deep sequencing (~1000× mean depth) were described for optimum detection. (smith2024geneticfindingsin pages 1-5)

**Variant type examples (2026 case series; illustrates spectrum rather than frequency):**
NF2 alterations can include truncating variants, copy-number changes (whole-gene deletion), and in-frame indels with merlin loss, supporting need for comprehensive testing modalities (e.g., MLPA/WGS). (freier2024theimpactof pages 2-3)

### 4.3 Inheritance and penetrance
- NF2-SWN described as autosomal dominant; Freier et al. describe “complete penetrance” in background. (freier2024theimpactof pages 1-2)
- LZTR1-related schwannomatosis described as incompletely penetrant in surveillance perspective context. (perrino2025updateoncancer pages 5-7)

### 4.4 Multi-hit / tumorigenesis models
- SMARCB1/LZTR1-related SWN: three-step/four-hit model involving retention of germline mutant allele, loss of the wild-type chromosome 22, and somatic NF2 mutation. (nagasaka2025geneticbasisand pages 1-2, tamura2024historicaldevelopmentof pages 3-4)

### 4.5 Epigenetic information
No schwannomatosis-specific epigenetic quantitative data were extracted from the 2023–2024 sources retrieved here; however, vestibular schwannoma reviews (not schwannomatosis-specific cohorts) discuss promoter methylation/transcriptional repression as potential functional “second hits” for NF2 and broader epigenetic regulation. (otaner2026vestibularschwannomagenetic pages 2-4)

---

## 5. Environmental information
No validated environmental, lifestyle, or infectious causal contributors were identified in the retrieved evidence set for schwannomatosis. (evidence gap)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (genotype → cell biology → tumors and symptoms)
A synthesis supported by mechanistic and clinical sources:
1) **Upstream genetic loss**: NF2/merlin loss (constitutional or somatic; often biallelic in tumor) (tamura2024historicaldevelopmentof pages 1-3, chiassonmackenzie2023cellularmechanismsof pages 1-2)
2) **Schwann-cell polarity/signaling dysregulation**: merlin loss yields unstable intrinsic polarity and distinct ErbB-ligand programs (chiassonmackenzie2023cellularmechanismsof pages 1-2)
3) **Downstream pathway activation and heterogeneity**: polarized ErbB signaling, mTOR outputs, and tumor heterogeneity; impacts therapeutic response variability (chiassonmackenzie2023cellularmechanismsof pages 1-2)
4) **Clinical manifestations**: schwannomas on cranial/spinal/peripheral nerves cause neurologic deficits and chronic pain; pain may not correlate with burden, suggesting additional biological drivers (e.g., local signaling, nerve–tumor interface) (chiassonmackenzie2023cellularmechanismsof pages 1-2)

### 6.2 Key pathways (examples) and GO term suggestions
**NF2/merlin loss → heterogeneity mechanism (2023 Nature Communications)**
**Direct abstract quote:**
- “**Virtually all schwannomas result from inactivation of the NF2 tumor suppressor gene with few, if any, cooperating mutations**” and “**loss of…merlin…enables Nf2−/− Schwann cells to adopt distinct programs of ErbB ligand production and polarized signaling**.” (Chiasson‑MacKenzie et al., 2023-03; Nature Communications) (chiassonmackenzie2023cellularmechanismsof pages 1-2)

**GO Biological Process suggestions (curation):**
- Schwann cell differentiation / proliferation
- Regulation of epithelial cell polarity / establishment of cell polarity
- ERBB signaling pathway
- mTOR signaling

### 6.3 Cell types and CL term suggestions
- Primary tumor cell: **Schwann cell** (CL: Schwann cell).
- Tumor microenvironment components: nerve cells, immune cells, stromal cells (general statement from modeling review). (madison2026schwannomatosistumormodeling pages 1-2)

### 6.4 Mechanistic models and experimental systems (model organism evidence)
- Mouse and Schwann-cell systems were used to model NF2-mutant schwannoma heterogeneity; authors “exploited the synchronous development of lesions in a mouse model” to quantify heterogeneity evolution. (chiassonmackenzie2023cellularmechanismsof pages 1-2)

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- Predominantly **nervous system**: cranial nerves (incl. vestibular nerve), spinal nerve roots, peripheral nerves. (smith2024geneticfindingsin pages 1-5, chiassonmackenzie2023cellularmechanismsof pages 1-2)
- CNS tumors in NF2-SWN: meningiomas and sometimes ependymomas. (perrino2025updateoncancer pages 5-7, evans2025historyandclinical pages 1-2)

**UBERON suggestions (curation):**
- Peripheral nerve; spinal nerve root; vestibulocochlear nerve; meninges; spinal cord.

### 7.2 Tissue/cell level
- Tissue: peripheral nerve sheath.
- Cell: Schwann cell. (chiassonmackenzie2023cellularmechanismsof pages 1-2)

---

## 8. Temporal development

### 8.1 Onset
- Clinical presentation can occur with vestibular schwannomas (NF2-related) or with painful peripheral/spinal schwannomas (non-NF2 forms). (evans2025historyandclinical pages 1-2, hino2025optimaldeliveryof pages 1-2)

### 8.2 Progression/course
- NF2-SWN is associated with progressive morbidities and monitored longitudinally by imaging/audiometry/neurologic deficits. (freier2024theimpactof pages 1-2)
- Tumor growth rates and clinical impact can be highly variable; pain does not reliably track burden. (chiassonmackenzie2023cellularmechanismsof pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology (recent statistics)
**NF2-related schwannomatosis prevalence (England):**
- Manchester highly ascertained diagnostic prevalence **1 in 50,500** and calculated birth prevalence **1 in 27,956**; an “updated prevalence across England in 2024…at least **1 in 58,000**.” (Evans et al., 2025; Familial Cancer) (evans2025historyandclinical pages 1-2)

**Schwannomatosis and gene-specific prevalence estimates (UK; 2024 cohort paper background):**
- NF2-related SWN prevalence ~**1 in 61,332** (UK data). (smith2024geneticfindingsin pages 1-5)
- Non-NF2 schwannomatosis ~**1 in 103,700**; germline LZTR1 ~**1 in 527,000**; germline SMARCB1 ~**1 in 1.1 million**. (smith2024geneticfindingsin pages 1-5)

**Population schwannoma risk:**
- “Over one in 500 people in the general population may develop a schwannoma during their lifetime.” (Smith et al., 2024) (smith2024geneticfindingsin pages 1-5)

### 9.2 Inheritance patterns
- NF2-SWN: autosomal dominant (complete penetrance noted in NF2-SWN context). (freier2024theimpactof pages 1-2)
- LZTR1-SWN: autosomal dominant with incomplete penetrance. (perrino2025updateoncancer pages 5-7)
- SMARCB1-SWN: familial tumor predisposition; specific penetrance estimates not extracted from retrieved pages. (perrino2025updateoncancer pages 5-7)

---

## 10. Diagnostics

### 10.1 Clinical criteria and modern classification (2022+)
- Diagnostic criteria have evolved and now integrate molecular findings; 2019 Manchester revisions introduced molecular criteria and 2022 international committee updated terminology and criteria. (tamura2024historicaldevelopmentof pages 1-3)

**Mosaicism definition (key diagnostic concept):**
- Mosaicism can be defined by “clearly <50%” allele fraction in blood/saliva or by a pathogenic NF2 variant found in ≥2 anatomically unrelated tumors but absent from unaffected tissue. (tamura2024historicaldevelopmentof pages 3-4)

### 10.2 Genetic testing strategy (real-world implementation)
- Tumor-inclusive testing improves yield: blood-only 25% vs 36% with tumor analysis; mosaic NF2 often requires testing two tumors. (smith2024geneticfindingsin pages 1-5)
- Deep NGS and adequate neoplastic content (≥20%) improve somatic detection. (smith2024geneticfindingsin pages 1-5)

**Practical interpretation:** for patients with multiple schwannomas not meeting classic NF2 clinical criteria, a modern workflow commonly requires **paired tumor sequencing** and high-depth methods to detect low-level mosaic NF2, alongside germline SMARCB1/LZTR1 testing. (smith2024geneticfindingsin pages 1-5)

### 10.3 Imaging / monitoring
- NF2-SWN progression monitoring includes neurologic deficits, neuroimaging, speech and pure-tone audiometry. (freier2024theimpactof pages 1-2)

### 10.4 Differential diagnosis
Not systematically extracted from the retrieved evidence set; however, misclassification risks exist (e.g., overlap between NF2-related and non-NF2 schwannomatosis; need for genetic testing). (smith2024geneticfindingsin pages 1-5)

---

## 11. Outcome / prognosis

### 11.1 Survival and life expectancy
- A recent management review states that “life expectancy…is nearly normal” in schwannomatosis, while acknowledging malignant transformation risk. (nagasaka2025geneticbasisand pages 1-2)

### 11.2 Morbidity
- Major morbidity drivers include chronic pain and neurologic deficits (hearing loss, facial weakness, balance issues). (freier2024theimpactof pages 1-2, hino2025optimaldeliveryof pages 1-2)

---

## 12. Treatment

### 12.1 Current applications and real-world implementations

#### Surgical management (standard of care for symptomatic tumors)
- Symptomatic lesion surgery is frequently used; however, persistent/recurrent pain may occur due to nerve injury or recurrence; multifocal disease may require repeated operations (average **3.4 surgical procedures in 10 years** reported in a pain-management review). (hino2025optimaldeliveryof pages 4-6)

**MAXO suggestions:** tumor resection; nerve sheath tumor excision; decompression surgery.

#### Symptom-based pharmacotherapy for pain
Commonly used agents include gabapentin/pregabalin, NSAIDs, tricyclic antidepressants (e.g., amitriptyline), SNRIs (e.g., duloxetine), anticonvulsants, and short-acting opioids. (hino2025optimaldeliveryof pages 1-2)

**MAXO suggestions:** analgesic therapy; neuropathic pain pharmacotherapy.

#### Neuromodulation
- Scrambler therapy (transcutaneous stimulation) is described as a noninvasive neuromodulation option in schwannomatosis pain management. (hino2025optimaldeliveryof pages 2-4)

**MAXO suggestions:** neuromodulation therapy; transcutaneous electrical stimulation.

### 12.2 Targeted/advanced therapeutics and experimental trials (2023–2026 registry data)

#### Pain-focused trials (primarily non-NF2 schwannomatosis)
1) **STARFISH — NCT05684692** (ClinicalTrials.gov; first posted 2023-01-13; recruiting as of 2026-04-23)
- Trial description: “placebo-controlled, multi-arm phase II platform screening trial” for “moderate-to-severe pain due to schwannomatosis.” (NCT05684692 chunk 1)
- Agents: **siltuximab** (anti-IL-6) and **erenumab-aooe** (CGRP receptor antibody) embedded sub-studies. (NCT05684692 chunk 1)

2) **Tanezumab — NCT04163419** (ClinicalTrials.gov; last update posted 2024-03-13)
- Direct quote (pain prevalence): “**68% experiencing chronic pain**.” (NCT04163419 chunk 1)
- Primary endpoint: change in worst pain from baseline to week 8 by NRS-11. (NCT04163419 chunk 1)
- Design: randomized, double-blind, placebo-controlled; enrollment 9; 40-week total duration including 24-week safety follow-up. (NCT04163419 chunk 1)

#### Tumor-directed targeted therapy trials in NF2-related schwannomatosis
**INTUITT-NF2 — NCT04374305** (ClinicalTrials.gov; first posted 2020-05-05; recruiting as of 2026-05-06)
- Master study: multi-arm phase II platform/basket trial for NF2-SWN tumors (vestibular and non-vestibular schwannomas, meningiomas, ependymomas). (NCT04374305 chunk 1)
- Sub-studies include **brigatinib**, **neratinib**, and **retifanlimab + bevacizumab**. (NCT04374305 chunk 1)
- Primary on-study evaluation includes radiographic response rate used for interim analyses and arm selection/expansion. (NCT04374305 chunk 1)

### 12.3 Expert opinion / authoritative analysis
- Tamura et al. emphasize that repeated revisions and molecular criteria can make NF2 diagnostic criteria confusing in practice, motivating clinician-facing reviews and highlighting the shift to gene-based schwannomatosis terminology. (tamura2024historicaldevelopmentof pages 1-3)
- Smith et al. conclude “the importance of comprehensive genetic testing” and variant classification, supported by mosaic NF2 detection via tumor testing. (smith2024geneticfindingsin pages 1-5)

---

## 13. Prevention
No primary prevention strategies are established because schwannomatosis is genetic; prevention focuses on **secondary prevention** (early detection, surveillance) and **tertiary prevention** (preventing complications and disability). Surveillance recommendations are referenced in the pediatric surveillance perspective, but detailed schedules were not extractable from the pages retrieved in this run. (perrino2025updateoncancer pages 5-7)

---

## 14. Other species / natural disease
No naturally occurring schwannomatosis analogs in non-human species were identified in the retrieved evidence set. (evidence gap)

---

## 15. Model organisms

### 15.1 Experimental models (NF2-mutant schwannoma)
- **Mouse models** and primary mouse Schwann cells are used to study NF2-loss schwannoma heterogeneity and signaling programs. (chiassonmackenzie2023cellularmechanismsof pages 1-2)

### 15.2 Utility and limitations (from retrieved sources)
- NF2-mutant schwannomas are genetically “cold” with few cooperating mutations, yet highly heterogeneous—these models support study of heterogeneity mechanisms and biomarker development. (chiassonmackenzie2023cellularmechanismsof pages 1-2)

---

## Structured summary table (for knowledge base ingestion)

| Category | Item | Key details | Recent source / year | URL | Evidence |
|---|---|---|---|---|---|
| Disease identifier | Schwannomatosis | Umbrella term adopted in 2022; gene-based subtypes include **NF2-related schwannomatosis**, **SMARCB1-related schwannomatosis**, **LZTR1-related schwannomatosis**, **22q-related schwannomatosis**, **SWN-NOS**, **SWN-NEC** | Nagasaka & Phi, 2025 | https://doi.org/10.3340/jkns.2025.0001 | (nagasaka2025geneticbasisand pages 1-2) |
| Disease identifier | MONDO | **MONDO:0008075** schwannomatosis; related entries include **MONDO:0007039** NF2-related schwannomatosis, **MONDO:0024517** SMARCB1-related schwannomatosis, **MONDO:0014299** LZTR1-related schwannomatosis | Open Targets / MONDO context, accessed via current evidence | https://platform.opentargets.org | (OpenTargets Search: Schwannomatosis) |
| Modern definition | NF2-related schwannomatosis | Formerly “neurofibromatosis type 2”; renamed because neurofibromas are not a defining feature; classically characterized by bilateral vestibular schwannomas with additional meningiomas/ependymomas/schwannomas | Tamura et al., 2024; Rai et al., 2025 | https://doi.org/10.2176/jns-nmc.2024-0067 ; https://doi.org/10.1177/19714009251313510 | (tamura2024historicaldevelopmentof pages 1-3, rai2025classificationofschwannomas pages 1-2) |
| Subtype | NF2-related schwannomatosis | Gene: **NF2**; autosomal dominant; high penetrance/near-certain disease with constitutional pathogenic variant; mosaic disease common, especially de novo cases | Nagasaka & Phi, 2025; Perrino et al., 2025 | https://doi.org/10.3340/jkns.2025.0001 ; https://doi.org/10.1158/1078-0432.ccr-24-3278 | (nagasaka2025geneticbasisand pages 1-2, perrino2025updateoncancer pages 5-7) |
| Subtype | SMARCB1-related schwannomatosis | Gene: **SMARCB1**; autosomal dominant familial tumor predisposition; typically peripheral/spinal schwannomas, no bilateral vestibular schwannomas; meningioma and MPNST risk reported | Perrino et al., 2025 | https://doi.org/10.1158/1078-0432.ccr-24-3278 | (perrino2025updateoncancer pages 5-7) |
| Subtype | LZTR1-related schwannomatosis | Gene: **LZTR1**; autosomal dominant with incomplete penetrance; peripheral schwannomas predominate; unilateral vestibular schwannoma can occur | Perrino et al., 2025; Uliana et al., 2024 | https://doi.org/10.1158/1078-0432.ccr-24-3278 ; https://doi.org/10.3390/genes15070916 | (perrino2025updateoncancer pages 5-7) |
| Major genes | Core causal genes | Principal disease genes across schwannomatosis are **NF2, SMARCB1, LZTR1** | Open Targets association summary; multiple reviews | https://platform.opentargets.org | (OpenTargets Search: Schwannomatosis) |
| Pathogenesis | Non-NF2 three-/four-hit model | For SMARCB1/LZTR1-related disease: germline variant retained in tumor, chromosome 22 loss/LOH removes wild-type allele, followed by somatic **NF2** alteration in tumor | Nagasaka & Phi, 2025; Tamura et al., 2024 | https://doi.org/10.3340/jkns.2025.0001 ; https://doi.org/10.2176/jns-nmc.2024-0067 | (nagasaka2025geneticbasisand pages 1-2, tamura2024historicaldevelopmentof pages 3-4) |
| Hallmark clinical features | Pain | Chronic pain is a major hallmark, often poorly correlated with tumor size/location/burden; symptom-based multidisciplinary pain management is emphasized | Nagasaka & Phi, 2025; Hino et al., 2025 | https://doi.org/10.3340/jkns.2025.0001 ; https://doi.org/10.2147/tcrm.s362794 | (nagasaka2025geneticbasisand pages 1-2, hino2025optimaldeliveryof pages 2-4) |
| Hallmark clinical features | NF2-related phenotype | Bilateral vestibular schwannomas, other cranial/spinal schwannomas, intradermal schwannomas, meningiomas, less commonly ependymomas; may also present with unilateral VS plus other tumors | Perrino et al., 2025; Evans et al., 2025 | https://doi.org/10.1158/1078-0432.ccr-24-3278 ; https://doi.org/10.1007/s10689-025-00504-5 | (perrino2025updateoncancer pages 5-7, evans2025historyandclinical pages 1-2) |
| Hallmark clinical features | SMARCB1/LZTR1 phenotype | Usually multiple **non-vestibular** schwannomas affecting peripheral and spinal nerves; painful tumors common; bilateral VS generally absent in SMARCB1-related disease | Tamura et al., 2024; Perrino et al., 2025 | https://doi.org/10.2176/jns-nmc.2024-0067 ; https://doi.org/10.1158/1078-0432.ccr-24-3278 | (tamura2024historicaldevelopmentof pages 3-4, perrino2025updateoncancer pages 5-7) |
| Diagnostic criteria | NF2-related schwannomatosis | Diagnosis can be made by bilateral VS, or identical **NF2** pathogenic variant in ≥2 anatomically distinct NF2-related tumors, or major/minor criteria combinations; molecular criteria formally incorporated in recent revisions | Tamura et al., 2024; Rai et al., 2025 | https://doi.org/10.2176/jns-nmc.2024-0067 ; https://doi.org/10.1177/19714009251313510 | (tamura2024historicaldevelopmentof pages 3-4, rai2025classificationofschwannomas pages 1-2) |
| Diagnostic testing | Mosaicism and tumor testing | Mosaicism may be inferred by blood/saliva variant allele fraction **<50%** or shared pathogenic variant across ≥2 anatomically unrelated tumors; tumor analysis materially improves diagnostic yield | Tamura et al., 2024; Smith et al., 2024 | https://doi.org/10.2176/jns-nmc.2024-0067 ; https://doi.org/10.1136/jmg-2024-110217 | (tamura2024historicaldevelopmentof pages 3-4, smith2024geneticfindingsin pages 1-5) |
| Diagnostic yield | Blood vs tumor-inclusive testing | In a 154-person cohort with non-vestibular schwannoma(s), overall molecular diagnosis was **25% using blood alone** and **36% when tumor analysis was included**; **18/19 NF2** findings were mosaic, with **17** detected only when 2 tumors were tested | Smith et al., 2024 | https://doi.org/10.1136/jmg-2024-110217 | (smith2024geneticfindingsin pages 1-5) |
| Epidemiology | Lifetime schwannoma risk | Lifetime risk of schwannoma estimated **>1/500**; about **75%** are vestibular schwannomas | Smith et al., 2024 | https://doi.org/10.1136/jmg-2024-110217 | (smith2024geneticfindingsin pages 1-5) |
| Epidemiology | NF2-related prevalence | Diagnostic prevalence in Manchester reported **1 in 50,500**; birth prevalence **1 in 27,956**; updated England prevalence in 2024 at least **1 in 58,000** | Evans et al., 2025 | https://doi.org/10.1007/s10689-025-00504-5 | (evans2025historyandclinical pages 1-2) |
| Epidemiology | Non-NF2 and gene-specific prevalence | UK prevalence estimates: non-NF2 schwannomatosis **1 in 103,700**; germline **LZTR1** variant-related disease **1 in 527,000**; germline **SMARCB1** variant-related disease **1.1 million** | Smith et al., 2024 | https://doi.org/10.1136/jmg-2024-110217 | (smith2024geneticfindingsin pages 1-5) |
| Quality of life | NF2-SWN mental health burden | In 77 surveyed NF2-SWN patients, clinically relevant symptoms: depression **30%**, anxiety **16%**, somatic burden **32%**; QoL correlated with physician-rated severity (**r=0.614**) | Freier et al., 2024 | https://doi.org/10.1038/s41598-024-57401-7 | (freier2024theimpactof pages 1-2) |
| Quality of life | Specific NF2-SWN QoL impacts | In the same cohort, **75% (58/77)** reported disease negatively affected outlook on life and **66% (51/77)** reported hearing problems affecting activities | Freier et al., 2024 | https://doi.org/10.1038/s41598-024-57401-7 | (freier2024theimpactof pages 3-4) |
| Current management | Standard care | Surgical resection for symptomatic/accessible lesions; radiotherapy and bevacizumab used mainly in NF2-related disease; supportive multidisciplinary pain care central | Nagasaka & Phi, 2025 | https://doi.org/10.3340/jkns.2025.0001 | (nagasaka2025geneticbasisand pages 1-2) |
| Active trial | **NCT05684692** STARFISH | Schwannomatosis pain platform trial; interventions: **siltuximab** and **erenumab-aooe** vs placebo; primary endpoint: change in worst pain intensity (NRS-11) from baseline to Day 85; status **Recruiting** | ClinicalTrials.gov record, 2023 | https://clinicaltrials.gov/study/NCT05684692 | (NCT05684692 chunk 2, NCT05684692 chunk 1) |
| Active trial | **NCT04163419** Tanezumab | Phase 2 randomized placebo-controlled trial for **moderate to severe pain due to schwannomatosis**; intervention **tanezumab**; primary endpoint: change in worst pain (NRS-11) at Week 8; enrollment **9**; status listed **Unknown / last known active-not-recruiting** | ClinicalTrials.gov record, 2020 | https://clinicaltrials.gov/study/NCT04163419 | (NCT04163419 chunk 1, NCT04163419 chunk 2) |
| Active trial | **NCT04374305** INTUITT-NF2 | Phase 2 platform trial for **NF2-related schwannomatosis** tumors; interventions: **brigatinib**, **neratinib**, **retifanlimab + bevacizumab**; primary on-study evaluation includes **radiographic response rate**; status **Recruiting** | ClinicalTrials.gov record, 2020 | https://clinicaltrials.gov/study/NCT04374305 | (NCT04374305 chunk 1) |
| Trial landscape note | Pain vs tumor-directed trials | Current active interventional landscape separates **pain-focused trials** (STARFISH, tanezumab) from **tumor-directed NF2 trials** (INTUITT-NF2); pain trials are mainly in non-NF2 schwannomatosis, whereas INTUITT targets NF2-related tumor burden | ClinicalTrials.gov records and review synthesis | https://clinicaltrials.gov | (NCT05684692 chunk 1, NCT04163419 chunk 1, NCT04374305 chunk 1, hino2025optimaldeliveryof pages 2-4) |


*Table: This table condenses current schwannomatosis nomenclature, genetics, clinical features, epidemiology, diagnostics, and actively recruiting or recent interventional trials. It is designed as a quick-reference artifact for disease knowledge base curation and evidence tracking.*

---

## Notes on evidence gaps and recommended curation add-ons
1) **OMIM/Orphanet/ICD/MeSH identifiers** were not directly retrievable in this tool run; add via direct database lookups.
2) **Non-NF2 schwannomatosis natural history**, penetrance estimates by variant class, and malignant transformation rates require additional primary cohort studies and guidelines not fully accessible here.
3) **Environmental/lifestyle modifiers** were not identified in the accessed evidence.

---

## Key URLs (access points in this run)
- Tamura et al., 2024-06-19 (online): https://doi.org/10.2176/jns-nmc.2024-0067 (tamura2024historicaldevelopmentof pages 1-3)
- Smith et al., 2024-08: https://doi.org/10.1136/jmg-2024-110217 (smith2024geneticfindingsin pages 1-5)
- Freier et al., 2024-03: https://doi.org/10.1038/s41598-024-57401-7 (freier2024theimpactof pages 1-2)
- Chiasson‑MacKenzie et al., 2023-03: https://doi.org/10.1038/s41467-023-37226-0 (chiassonmackenzie2023cellularmechanismsof pages 1-2)
- STARFISH (NCT05684692): https://clinicaltrials.gov/study/NCT05684692 (NCT05684692 chunk 1)
- Tanezumab pain trial (NCT04163419): https://clinicaltrials.gov/study/NCT04163419 (NCT04163419 chunk 1)
- INTUITT-NF2 (NCT04374305): https://clinicaltrials.gov/study/NCT04374305 (NCT04374305 chunk 1)


References

1. (OpenTargets Search: Schwannomatosis): Open Targets Query (Schwannomatosis, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (tamura2024historicaldevelopmentof pages 1-3): Ryota TAMURA, Masahiro YO, and Masahiro TODA. Historical development of diagnostic criteria for nf2-related schwannomatosis. Neurologia medico-chirurgica, 64:299-308, Aug 2024. URL: https://doi.org/10.2176/jns-nmc.2024-0067, doi:10.2176/jns-nmc.2024-0067. This article has 12 citations and is from a peer-reviewed journal.

3. (nagasaka2025geneticbasisand pages 1-2): Shohei Nagasaka and Ji Hoon Phi. Genetic basis and clinical management of schwannomatosis. Journal of Korean Neurosurgical Society, 68:286-293, May 2025. URL: https://doi.org/10.3340/jkns.2025.0001, doi:10.3340/jkns.2025.0001. This article has 1 citations and is from a peer-reviewed journal.

4. (rai2025classificationofschwannomas pages 1-2): Pranjal Rai, Girish Bathla, Neetu Soni, Amit Desai, Dinesh Rao, Prasanna Vibhute, and Amit Agarwal. Classification of schwannomas and the new naming convention for "neurofibromatosis-2": genetic updates and international consensus recommendation. The neuroradiology journal, pages 19714009251313510, Jan 2025. URL: https://doi.org/10.1177/19714009251313510, doi:10.1177/19714009251313510. This article has 7 citations and is from a peer-reviewed journal.

5. (evans2025historyandclinical pages 1-2): D. Gareth Evans, Jaishri O. Blakeley, and Scott R. Plotkin. History and clinical epidemiology of nf2-related schwannomatosis. Familial Cancer, Oct 2025. URL: https://doi.org/10.1007/s10689-025-00504-5, doi:10.1007/s10689-025-00504-5. This article has 2 citations and is from a peer-reviewed journal.

6. (chiassonmackenzie2023cellularmechanismsof pages 1-2): Christine Chiasson-MacKenzie, Jeremie Vitte, Ching-Hui Liu, Emily A. Wright, Elizabeth A. Flynn, Shannon L. Stott, Marco Giovannini, and Andrea I. McClatchey. Cellular mechanisms of heterogeneity in nf2-mutant schwannoma. Nature Communications, Mar 2023. URL: https://doi.org/10.1038/s41467-023-37226-0, doi:10.1038/s41467-023-37226-0. This article has 26 citations and is from a highest quality peer-reviewed journal.

7. (perrino2025updateoncancer pages 5-7): Melissa R. Perrino, Marjolijn C. J. Jongmans, Gail E. Tomlinson, Mary-Louise C. Greer, Sarah R. Scollon, Sarah G. Mitchell, Jordan R. Hansford, Kris Ann P. Schultz, Wendy K. Kohlmann, Jennifer M. Kalish, Suzanne P. MacFarland, Anirban Das, Kara N. Maxwell, Stefan M. Pfister, Rosanna Weksberg, Orli Michaeli, Uri Tabori, Gina M. Ney, Philip J. Lupo, Jack J. Brzezinski, Douglas R. Stewart, Emma R. Woodward, and Christian P. Kratz. Update on cancer and central nervous system tumor surveillance in pediatric nf2-, smarcb1-, and lztr1-related schwannomatosis. Clinical cancer research : an official journal of the American Association for Cancer Research, Feb 2025. URL: https://doi.org/10.1158/1078-0432.ccr-24-3278, doi:10.1158/1078-0432.ccr-24-3278. This article has 8 citations.

8. (smith2024geneticfindingsin pages 1-5): Miriam J Smith, Cristina Perez-Becerril, Mwee van der Meer, George J Burghel, Sarah J Waller, Megan Carney, Sancha Bunstone, Katherine Fryer, Naomi L Bowers, Claire L Hartley, Philip T Smith, Scott A Rutherford, Simon R Freeman, Simon K W Lloyd, Omar N Pathmanaban, Andrew Thomas King, Dorothy Halliday, Chris Duff, and D Gareth Evans. Genetic findings in people with schwannomas who do not meet clinical diagnostic criteria for nf2-related schwannomatosis. Journal of Medical Genetics, 61:1011-1015, Aug 2024. URL: https://doi.org/10.1136/jmg-2024-110217, doi:10.1136/jmg-2024-110217. This article has 5 citations and is from a domain leading peer-reviewed journal.

9. (NCT05684692 chunk 1): Scott R. Plotkin, MD, PhD. Screening Trial for Pain Relief in Schwannomatosis (STARFISH). Massachusetts General Hospital. 2023. ClinicalTrials.gov Identifier: NCT05684692

10. (NCT04163419 chunk 1): Scott R. Plotkin, MD, PhD. Phase 2 Study of Tanezumab in Subjects With Moderate to Severe Pain Due to Schwannomatosis. Massachusetts General Hospital. 2020. ClinicalTrials.gov Identifier: NCT04163419

11. (NCT04374305 chunk 1): Scott R. Plotkin, MD, PhD. Innovative Trial for Understanding the Impact of Targeted Therapies in NF2-Related Schwannomatosis (INTUITT-NF2). Scott R. Plotkin, MD, PhD. 2020. ClinicalTrials.gov Identifier: NCT04374305

12. (tamura2024historicaldevelopmentof pages 3-4): Ryota TAMURA, Masahiro YO, and Masahiro TODA. Historical development of diagnostic criteria for nf2-related schwannomatosis. Neurologia medico-chirurgica, 64:299-308, Aug 2024. URL: https://doi.org/10.2176/jns-nmc.2024-0067, doi:10.2176/jns-nmc.2024-0067. This article has 12 citations and is from a peer-reviewed journal.

13. (freier2024theimpactof pages 3-4): Anna Freier, Anna C. Lawson McLean, Denise Loeschner, Steffen K. Rosahl, and Johannes Kruse. The impact of mental health on health-related quality of life in patients with nf2-related schwannomatosis. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-57401-7, doi:10.1038/s41598-024-57401-7. This article has 6 citations and is from a peer-reviewed journal.

14. (freier2024theimpactof pages 1-2): Anna Freier, Anna C. Lawson McLean, Denise Loeschner, Steffen K. Rosahl, and Johannes Kruse. The impact of mental health on health-related quality of life in patients with nf2-related schwannomatosis. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-57401-7, doi:10.1038/s41598-024-57401-7. This article has 6 citations and is from a peer-reviewed journal.

15. (hino2025optimaldeliveryof pages 1-2): Utaro Hino, Ryota Tamura, and Masahiro Toda. Optimal delivery of pain management in schwannomatosis: a literature review. Therapeutics and Clinical Risk Management, 21:61-68, Jan 2025. URL: https://doi.org/10.2147/tcrm.s362794, doi:10.2147/tcrm.s362794. This article has 2 citations and is from a peer-reviewed journal.

16. (madison2026schwannomatosistumormodeling pages 1-2): Mackenzie S. Madison, Huazhen Xu, Yarelis Gonzalez-Vargas, Marybeth G. Yonk, Charee M. Thompson, Hurley Haney, Danielle Babbitt, Yuhong Du, Angela C. Hirbe, Nicholas M. Boulis, Ren-Yuan Bai, and Kecheng Lei. Schwannomatosis tumor modeling: progress and prospects for translational research. Journal of Biological Engineering, Feb 2026. URL: https://doi.org/10.1186/s13036-026-00634-z, doi:10.1186/s13036-026-00634-z. This article has 0 citations and is from a peer-reviewed journal.

17. (freier2024theimpactof pages 2-3): Anna Freier, Anna C. Lawson McLean, Denise Loeschner, Steffen K. Rosahl, and Johannes Kruse. The impact of mental health on health-related quality of life in patients with nf2-related schwannomatosis. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-57401-7, doi:10.1038/s41598-024-57401-7. This article has 6 citations and is from a peer-reviewed journal.

18. (otaner2026vestibularschwannomagenetic pages 2-4): Franciska Otaner, Vratko Himic, Luis O. Vargas, Matthew Abikenari, Neelesh Pandey, Shayndhan Sivanathan, Olivia Kalmanson, Aparna Govindan, Diane Jung, Dagoberto Estevez-Ordonez, Amy Wang, Sanjeeva Jeyaretna, Ashish H. Shah, Ricardo J. Komotar, Bradley Gampel, Christine Dinh, and Michael E. Ivan. Vestibular schwannoma: genetic and epigenetic mechanisms, hearing loss, and emerging therapies. Journal of Neuro-Oncology, May 2026. URL: https://doi.org/10.1007/s11060-026-05621-4, doi:10.1007/s11060-026-05621-4. This article has 0 citations and is from a peer-reviewed journal.

19. (hino2025optimaldeliveryof pages 4-6): Utaro Hino, Ryota Tamura, and Masahiro Toda. Optimal delivery of pain management in schwannomatosis: a literature review. Therapeutics and Clinical Risk Management, 21:61-68, Jan 2025. URL: https://doi.org/10.2147/tcrm.s362794, doi:10.2147/tcrm.s362794. This article has 2 citations and is from a peer-reviewed journal.

20. (hino2025optimaldeliveryof pages 2-4): Utaro Hino, Ryota Tamura, and Masahiro Toda. Optimal delivery of pain management in schwannomatosis: a literature review. Therapeutics and Clinical Risk Management, 21:61-68, Jan 2025. URL: https://doi.org/10.2147/tcrm.s362794, doi:10.2147/tcrm.s362794. This article has 2 citations and is from a peer-reviewed journal.

21. (NCT05684692 chunk 2): Scott R. Plotkin, MD, PhD. Screening Trial for Pain Relief in Schwannomatosis (STARFISH). Massachusetts General Hospital. 2023. ClinicalTrials.gov Identifier: NCT05684692

22. (NCT04163419 chunk 2): Scott R. Plotkin, MD, PhD. Phase 2 Study of Tanezumab in Subjects With Moderate to Severe Pain Due to Schwannomatosis. Massachusetts General Hospital. 2020. ClinicalTrials.gov Identifier: NCT04163419

## Artifacts

- [Edison artifact artifact-00](Schwannomatosis-deep-research-falcon_artifacts/artifact-00.md)
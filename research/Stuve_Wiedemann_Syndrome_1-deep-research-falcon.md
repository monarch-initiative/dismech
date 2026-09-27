---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T20:16:49.229294'
end_time: '2026-08-19T20:26:24.452565'
duration_seconds: 575.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Stuve-Wiedemann Syndrome 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Stuve_Wiedemann_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Stuve-Wiedemann Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Stuve-Wiedemann Syndrome 1** covering all of the
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
- **Disease Name:** Stuve-Wiedemann Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Stuve-Wiedemann Syndrome 1** covering all of the
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


# Stüve–Wiedemann Syndrome 1: Disease-Characteristics Research Report

## Executive summary and scope

Stüve–Wiedemann syndrome (SWS) is a congenital, usually severe **autosomal-recessive bent-bone skeletal dysplasia with dysautonomia**, most often caused by biallelic loss-of-function variants in **LIFR**. The early phenotype combines bowed long bones and contractures with respiratory distress, dysphagia/aspiration, temperature instability, abnormal sweating, and reduced pain sensation. Survivors experience decreasing dysautonomic severity but increasing orthopedic morbidity. In the best available systematic review (69 patients), mortality was **42% before age 2**, compared with **10% after age 2**; pulmonary arterial hypertension (PAH) was associated with **63% mortality**. After age 2, restricted joint mobility, spinal deformity, and fractures were reported in 81%, 77%, and 61%, respectively. These estimates come from published cases and are vulnerable to ascertainment and survival bias. (warnier2022clinicaloverviewand pages 1-3, warnier2022clinicaloverviewand pages 10-11)

**Curation warning:** “Stüve–Wiedemann syndrome 1” should denote classic **LIFR-related SWS**. Biallelic complete loss of **IL6ST/GP130** causes a related but broader entity termed **extended Stüve–Wiedemann syndrome**, with additional immune, hematologic, renal, and cutaneous manifestations. It should not be merged uncritically with classic SWS1. (chen2020absenceofgp130 pages 8-9, chen2020absenceofgp130 pages 1-1)

The compact knowledge-base summary below complements the narrative report.

| Domain | Curated finding | Suggested ontology/identifier | Evidence strength/notes |
|---|---|---|---|
| Disease identity | Classic Stüve-Wiedemann syndrome is a rare congenital bent-bone skeletal dysplasia with prominent dysautonomia; the literature also notes historical overlap with “Schwartz-Jampel syndrome type 2,” now considered the same LIFR-related condition. OMIM numbering is inconsistent across sources: some reviews cite **OMIM #601559**, while at least one review cites **OMIM #610559**; database validation is required before KB ingestion. | Disease label: **Stüve-Wiedemann syndrome**; legacy synonym: **Schwartz-Jampel syndrome type 2**; OMIM ID **requires database validation**; MONDO ID **requires database validation**; Orphanet ID **requires database validation** | Strong disease-definition evidence from landmark genetics and reviews; explicit OMIM ambiguity present in retrieved sources and should be reconciled against OMIM/Orphanet directly (warnier2022clinicaloverviewand pages 1-3, mikelonis2014stüvewiedemannsyndromelifr pages 7-8, bertola2016stüvewiedemannsyndromeupdate pages 1-2) |
| Data provenance | Current summary is derived from aggregated disease-level resources and literature synthesis, especially a 69-patient systematic review, plus primary molecular studies and case reports rather than EHR-scale datasets. | Evidence type labels: **systematic review**, **human clinical case series**, **primary human molecular study**, **model organism** | Useful for KB evidence grading; no large registry or EHR resource identified in retrieved evidence (warnier2022clinicaloverviewand pages 1-3) |
| Etiology | Primary cause is **biallelic loss-of-function pathogenic variants in LIFR** causing defective cytokine receptor signaling. | **LIFR** gene; chromosome **5p13.1**; inheritance term: **autosomal recessive** | Landmark AJHG study mapped disease to 5p13.1 and identified null LIFR mutations in 19 families (bertola2016stüvewiedemannsyndromeupdate pages 5-5, mikelonis2014stüvewiedemannsyndromelifr pages 2-3) |
| Genetic architecture | In 19 SWS/SJS2 families, **14 distinct LIFR mutations** were identified; **12/14** were predicted premature-termination variants, supporting a predominantly truncating/null allelic spectrum. | Variant classes: **frameshift**, **nonsense**, **splice-site**; germline origin: **germline** | Strong primary evidence for null-variant mechanism (bertola2016stüvewiedemannsyndromeupdate pages 5-6) |
| Founder effect / population genetics | An identical **653_654insT / c.653dup** frameshift was reported in families from the **United Arab Emirates**, suggesting a regional founder effect; disease burden is enriched in highly consanguineous populations. | Founder variant label: **LIFR c.653dup**; population note: **UAE founder effect** | Strong for founder effect in specific region; broader carrier frequency remains unavailable in retrieved evidence (bertola2016stüvewiedemannsyndromeupdate pages 5-6, bertola2016stüvewiedemannsyndromeupdate pages 2-2) |
| Inheritance | **Autosomal recessive** inheritance is consistently reported; consanguinity is common in affected families. | Inheritance: **autosomal recessive** | Strong and concordant across reviews and primary genetics papers (warnier2022clinicaloverviewand pages 1-3, bertola2016stüvewiedemannsyndromeupdate pages 1-2, bertola2016stüvewiedemannsyndromeupdate pages 5-5) |
| Core prenatal phenotype | Prenatal ultrasound may show **mild-to-moderate micromelia**, **bowing of lower-limb bones** (tibia more than femur), **talipes**, and **camptodactyly**; later gestation may show **IUGR** and **oligohydramnios**. In one review, **8/10 (80%)** postnatally confirmed fetuses had prenatal skeletal abnormalities. | HPO labels: **Short long bones**, **Bowing of long bones**, **Talipes**, **Camptodactyly**, **Intrauterine growth restriction**, **Oligohydramnios**; IDs require validation | Moderate-strong; based on retrospective prenatal series summarized in review (bertola2016stüvewiedemannsyndromeupdate pages 2-3, bertola2016stüvewiedemannsyndromeupdate pages 2-2) |
| Core neonatal/infant phenotype | Typical early features include **short bowed limbs**, **camptodactyly**, **hypotonia/myotonia**, **feeding and swallowing difficulties**, **respiratory distress**, **hyperthermic episodes**, and **excessive/inappropriate sweating**. | HPO labels: **Bowing of long bones**, **Camptodactyly**, **Respiratory distress**, **Dysphagia**, **Hyperthermia**, **Hyperhidrosis**, **Hypotonia**; IDs require validation | Strong clinical consistency across reviews (bertola2016stüvewiedemannsyndromeupdate pages 1-2, oxford2016neuropathiesofstüvewiedemann pages 6-8, warnier2022clinicaloverviewand pages 1-3) |
| Dysautonomia / neuropathy | Dysautonomia includes temperature dysregulation, abnormal sweating, reduced pain sensation, and loss of reflexes such as **corneal** and **patellar** reflexes. | HPO labels: **Dysautonomia**, **Reduced pain sensation**, **Absent corneal reflex**, **Areflexia**; CL term suggestion: **sympathetic neuron** (ID requires validation) | Moderate-strong; emphasized in neuropathy-focused review (oxford2016neuropathiesofstüvewiedemann pages 6-8, oxford2016neuropathiesofstüvewiedemann pages 5-6) |
| Childhood survivor phenotype | Among survivors >2 years, orthopedic complications increase: **joint mobility restriction 81%**, **spinal deformations 77%**, **fractures 61%**. Dysautonomic symptoms tend to lessen with age, while skeletal morbidity accumulates. | HPO labels: **Joint contracture / restricted joint mobility**, **Scoliosis / spinal deformity**, **Fractures**, **Osteoporosis**; IDs require validation | Strong quantitative evidence from 69-patient systematic review (warnier2022clinicaloverviewand pages 1-3, warnier2022clinicaloverviewand pages 10-11) |
| Mechanism / molecular pathway | LIFR normally transduces signaling from IL-6 family cytokines and activates **JAK/STAT3**, with additional **MAPK** and **PI3K** pathway engagement. Most disease alleles destabilize LIFR mRNA or truncate the receptor, causing absent receptor protein and failure of downstream signaling. | GO/process labels: **JAK-STAT cascade**, **cytokine-mediated signaling pathway**, **regulation of bone development**, **autonomic nervous system development**; pathway labels only, IDs require validation | Strong primary/mechanistic evidence; classic causal chain is null LIFR → absent signaling → skeletal and autonomic defects (bertola2016stüvewiedemannsyndromeupdate pages 5-5, bertola2016stüvewiedemannsyndromeupdate pages 5-6) |
| Distinguishing related disorder | **IL6ST/GP130 deficiency** causes **extended Stüve-Wiedemann syndrome**, not classic SWS1. It shares skeletal/dysautonomic features but has broader GP130-dependent cytokine signaling failure and additional immune/renal/hematologic findings. | Related disease label: **extended Stüve-Wiedemann syndrome**; gene: **IL6ST** | Important curation distinction to avoid conflating classic LIFR disease with IL6ST-related phenotype expansion (chen2020absenceofgp130 pages 8-9, chen2020absenceofgp130 pages 1-1, chen2020absenceofgp130 pages 1-2) |
| Anatomy affected | Primary systems: **skeletal system**, **peripheral/autonomic nervous system**, **respiratory system**, **feeding/swallowing apparatus**, and **eye/cornea** in some survivors. | UBERON labels: **long bone**, **spine**, **lung**, **esophagus/pharynx**, **cornea**; CL labels: **osteoblast**, **osteoclast**, **motor neuron**, **sympathetic neuron**; IDs require validation | Mechanistic-anatomic inference is supported by clinical phenotype and model data (warnier2022clinicaloverviewand pages 10-11, bertola2016stüvewiedemannsyndromeupdate pages 5-5, mikelonis2014stüvewiedemannsyndromelifr pages 2-3) |
| Diagnosis | Diagnosis is clinical-radiographic plus molecular confirmation. Key radiographic findings include **bowed femur/tibia**, **diaphyseal cortical thickening**, **wide metaphyses**, and **decreased bone density**. Genetic confirmation is by **LIFR sequencing**. | Diagnostic labels: **skeletal survey**, **molecular genetic testing**, **LIFR single-gene or panel testing**, **exome/genome sequencing** | Strong for radiographic phenotype and confirmatory genetic testing; no disease-specific biomarker identified (warnier2022clinicaloverviewand pages 1-3, bertola2016stüvewiedemannsyndromeupdate pages 2-3) |
| Differential diagnosis | Main differentials among prenatal/neonatal bent-bone dysplasias include **campomelic dysplasia**, **kyphomelic dysplasia**, and **diastrophic dysplasia**. | Disease labels only; ontology IDs require validation | Moderate evidence from reviews; useful for prenatal and neonatal diagnostic workup (bertola2016stüvewiedemannsyndromeupdate pages 2-2) |
| Prognosis / mortality | Natural history is marked by high early mortality. In the 69-patient review, mortality was **42% before age 2** versus **10% after age 2**; **pulmonary arterial hypertension** was a poor prognostic factor with **63% mortality**. Respiratory failure is the leading cause of death. | Prognostic factor label: **pulmonary arterial hypertension**; HPO label: **Respiratory failure** | Strong quantitative prognosis evidence (warnier2022clinicaloverviewand pages 1-3) |
| Development / cognition | Survivors often have delayed motor development, but **cognitive development is generally normal** in reported cases. | HPO labels: **Motor delay**, **Normal cognition/intellect**; IDs require validation | Moderate-strong consistency across reviews (bertola2016stüvewiedemannsyndromeupdate pages 1-2, warnier2022clinicaloverviewand pages 10-11) |
| Current treatment | No curative or disease-modifying therapy is established; management is **supportive and multidisciplinary**. Core measures include **aspiration prevention**, **nasogastric tube or gastrostomy**, respiratory support/monitoring, and structured fever-management plans. | NCIT labels: **Gastrostomy**, **Nasogastric Intubation**, **Supportive Care**, **Multidisciplinary Care**; IDs require validation | Strong across reviews and 2024 case report (mikelonis2014stüvewiedemannsyndromelifr pages 7-8, bhalla2024anoveltermination pages 5-6) |
| Symptom-directed drugs | Recent case literature describes home protocols using **acetaminophen**, **ibuprofen**, and **bromocriptine** for hyperthermia escalation; these are supportive measures, not validated disease-specific therapies. | CHEBI/NCIT labels: **Acetaminophen**, **Ibuprofen**, **Bromocriptine**; IDs require validation | Limited evidence: case-report level only (2024), no controlled trials (bhalla2024anoveltermination pages 5-6) |
| Orthopedic management | Supportive orthopedic care includes **physiotherapy**, **bracing**, **calcium/vitamin D**, **bisphosphonates** for bone fragility prevention, and corrective surgery; **telescopic intramedullary rodding** has been recommended to limit recurrence of deformity. | NCIT labels: **Physical Therapy**, **Orthotic Device**, **Bisphosphonate Therapy**, **Intramedullary Rod Placement**; IDs require validation | Moderate evidence from systematic review and survivor literature (warnier2022clinicaloverviewand pages 10-11) |
| Ophthalmic / dental issues | Ocular surface problems and corneal reflex loss are reported; dental and ophthalmologic follow-up are part of multidisciplinary care, but evidence is sparse in retrieved sources. | HPO labels: **Corneal opacity**, **Neurotrophic keratopathy**; specialty care labels: **ophthalmology**, **dentistry**; IDs require validation | Low-moderate evidence in retrieved set; requires dedicated literature validation before structured frequency claims (warnier2022clinicaloverviewand pages 10-11, warnier2022clinicaloverviewand pages 11-12) |
| Anesthesia | Historically there were concerns about malignant hyperthermia risk, but recent case literature notes published SWS patients undergoing anesthesia without malignant hyperthermia episodes. | NCIT label: **General Anesthesia**; adverse-event label: **Malignant Hyperthermia** | Low-moderate evidence, mainly case-report/review level; should be interpreted cautiously (bhalla2024anoveltermination pages 5-6) |
| Prevention / screening | Primary prevention is not applicable once genotype is inherited; practical prevention focuses on **genetic counseling**, **carrier screening in at-risk families/populations**, **prenatal diagnosis**, and potentially **preimplantation genetic testing** when familial variants are known. | Prevention labels: **Genetic Counseling**, **Carrier Screening**, **Prenatal Diagnosis**, **Preimplantation Genetic Testing**; IDs require validation | Strong rationale for recessive disease prevention, though disease-specific screening programs were not identified (bertola2016stüvewiedemannsyndromeupdate pages 2-2, warnier2022clinicaloverviewand pages 1-3) |
| Clinical trials / advanced therapeutics | No disease-specific approved targeted therapy, gene therapy, RNA therapy, or interventional clinical trial was identified in the retrieved search. Gentamicin-mediated readthrough has been discussed experimentally for nonsense variants but remains nonstandard and toxicity-limited. | Intervention labels: **Gentamicin readthrough (experimental)**; trial status: **no disease-specific interventional trial identified** | Evidence for absence of standard targeted therapy is consistent; trial search returned no relevant active study in retrieved tooling (bertola2016stüvewiedemannsyndromeupdate pages 2-2, oxford2016neuropathiesofstüvewiedemann pages 6-8) |
| Model organism | **Lifr-null mice** show severe developmental abnormalities with **perinatal lethality**, reduced fetal bone volume, increased osteoclasts, and neural defects, supporting causal roles in bone and nervous-system development. | Model label: **Lifr knockout mouse**; GO labels: **bone development**, **neuron development**; IDs require validation | Strong supportive model evidence, though not all human dysautonomic features are fully modeled (bertola2016stüvewiedemannsyndromeupdate pages 5-5, mikelonis2014stüvewiedemannsyndromelifr pages 2-3) |
| Knowledge gaps | No robust prevalence/incidence estimate for general populations, no validated prognostic biomarker beyond clinical complications like PAH, no confirmed protective factors, no established modifier genes, and no omics-based diagnostic signature were identified in retrieved evidence. | KB flags: **data unavailable / not established** | Important negative curation points to avoid overstatement (warnier2022clinicaloverviewand pages 1-3, warnier2022clinicaloverviewand pages 10-11, oxford2016neuropathiesofstüvewiedemann pages 6-8) |


*Table: This table condenses the main disease-knowledge-base fields for classic LIFR-related Stüve-Wiedemann syndrome, including identity, genetics, phenotype, mechanism, diagnosis, prognosis, treatment, prevention, and model evidence. It also flags key curation issues such as OMIM ambiguity and the need to distinguish classic SWS1 from IL6ST-related extended SWS.*

## 1. Disease information

### Definition

Classic SWS is an inherited osteochondrodysplasia characterized radiographically by congenital bowing of long bones, cortical thickening, widened/flared metaphyses with abnormal trabeculation or reduced density, and clinically by contractures plus severe neonatal autonomic and respiratory dysfunction. The syndrome historically overlapped with “Schwartz–Jampel syndrome type 2”; molecular work established these as the same LIFR-null disorder rather than distinct diseases. (bertola2016stüvewiedemannsyndromeupdate pages 1-2, bertola2016stüvewiedemannsyndromeupdate pages 5-6, warnier2022clinicaloverviewand pages 1-3)

### Identifiers and synonyms

- **Preferred name:** Stüve–Wiedemann syndrome; often written Stuve-Wiedemann syndrome.
- **Synonyms:** Stüve–Wiedemann/Schwartz–Jampel syndrome type 2; Schwartz–Jampel syndrome type 2; SWS; STWS; congenital bent-bone dysplasia with dysautonomia.
- **OMIM:** The contemporary systematic review identifies **OMIM 601559**. One older retrieved review’s abstract instead says 610559, apparently an inconsistency; **601559 should be verified directly against the live OMIM record before ingestion**. (warnier2022clinicaloverviewand pages 1-3, mikelonis2014stüvewiedemannsyndromelifr pages 7-8)
- **Gene locus:** **LIFR**, chromosome **5p13.1**. (bertola2016stüvewiedemannsyndromeupdate pages 5-5, mikelonis2014stüvewiedemannsyndromelifr pages 2-3)
- **MONDO, Orphanet, MeSH, ICD-10/ICD-11:** exact live identifiers were not independently recoverable from the retrieved primary literature. They should be resolved directly through current ontology releases rather than inferred. ICD coding is likely under a broad osteochondrodysplasia/skeletal-dysplasia category because no disease-specific code was established in this evidence set.

### Data provenance

The evidence is **aggregated disease-level literature**, not individual-level EHR data. Its strongest clinical source is a systematic review of 69 published patients; molecular conclusions derive from family studies, patient cells, and animal models. Individual recent developments are mostly case reports or small case series. (warnier2022clinicaloverviewand pages 1-3, bhalla2024anoveltermination pages 5-6)

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary cause

Classic SWS is caused by **biallelic germline loss-of-function LIFR variants**. In the landmark series, disease was mapped to 5p13.1 in 19 families and 14 distinct variants were found; 12 of 14 predicted premature termination. Null alleles destabilized LIFR transcripts, eliminated functional receptor, and impaired JAK/STAT3 signaling in patient cells. (bertola2016stüvewiedemannsyndromeupdate pages 5-5, bertola2016stüvewiedemannsyndromeupdate pages 5-6)

### Genetic risk factors

- Having two pathogenic LIFR alleles is the primary risk factor.
- Consanguinity and known family history substantially increase reproductive risk for this recessive disorder.
- A recurrent **LIFR c.653dup** frameshift was found in multiple United Arab Emirates families, supporting a regional founder effect. Other reported alleles include **c.144_145dup**, **c.756dup**, **p.Trp63\***, **p.Arg418\***, and splice variants. (mikelonis2014stüvewiedemannsyndromelifr pages 2-3, bertola2016stüvewiedemannsyndromeupdate pages 5-6)
- Rare non-truncating variants affecting receptor glycosylation may retain partial function and produce an attenuated phenotype, but robust genotype–phenotype rules have not been established. Identical frameshift alleles can yield different severity, implying residual biological, clinical, or modifier effects. (mikelonis2014stüvewiedemannsyndromelifr pages 7-8, bertola2016stüvewiedemannsyndromeupdate pages 5-6)

### Environmental and protective factors

No toxin, infection, lifestyle, occupational exposure, diet, age, or sex is known to cause SWS. No validated genetic or environmental protective factor has been identified. Environmental conditions nevertheless influence **complications**: heat can worsen hyperthermia; impaired swallowing increases aspiration risk; trauma and low bone density increase fracture risk. These modify morbidity, not Mendelian disease occurrence.

No established gene–environment interaction has been demonstrated. Early airway, feeding, temperature, and PAH management may improve survival, but this is clinical risk mitigation rather than etiologic prevention. (warnier2022clinicaloverviewand pages 10-11, mikelonis2014stüvewiedemannsyndromelifr pages 7-8)

## 3. Phenotypes

### Prenatal and neonatal phenotypes

Prenatal ultrasound can show mild-to-moderate micromelia, lower-limb bowing—often tibia more than femur—talipes and camptodactyly. Later findings may include growth restriction and oligohydramnios. In a reviewed UAE series, **8/10 fetuses (80%)** later diagnosed with SWS had prenatal skeletal abnormalities, whereas across the broader 69-patient review only **46%** had reported antenatal signs. This difference likely reflects referral and family-history effects. (warnier2022clinicaloverviewand pages 1-3, bertola2016stüvewiedemannsyndromeupdate pages 2-3)

Suggested HPO labels include **Abnormality of prenatal development**, **Decreased fetal movement**, **Short long bones**, **Bowing of long bones**, **Micromelia**, **Talipes**, **Camptodactyly**, **Intrauterine growth restriction**, and **Oligohydramnios**.

### Core postnatal phenotype

- **Skeletal/physical signs:** short bowed limbs, progressive bowing, camptodactyly, talipes, restricted elbows/knees, metaphyseal widening, cortical thickening, osteopenia/osteoporosis, fractures, scoliosis or kyphoscoliosis, and femoral-head destruction. Severity is usually marked and orthopedic disease progresses in survivors. Suggested HPO: **Bowing of long bones**, **Cortical thickening of long-bone diaphyses**, **Metaphyseal widening**, **Joint contracture**, **Osteopenia**, **Osteoporosis**, **Recurrent fractures**, **Scoliosis**, **Kyphosis**. (warnier2022clinicaloverviewand pages 1-3, bertola2016stüvewiedemannsyndromeupdate pages 2-3)
- **Respiratory/cardiovascular signs:** neonatal respiratory distress, recurrent infections often secondary to aspiration, respiratory failure, and PAH. These dominate early mortality. Suggested HPO: **Neonatal respiratory distress**, **Recurrent respiratory infections**, **Aspiration**, **Respiratory failure**, **Pulmonary arterial hypertension**. (warnier2022clinicaloverviewand pages 1-3, mikelonis2014stüvewiedemannsyndromelifr pages 7-8)
- **Feeding:** dysphagia and poor feeding, frequently requiring nasogastric feeding or gastrostomy. Swallowing commonly improves by the second or third year in survivors. Suggested HPO: **Dysphagia**, **Feeding difficulties**, **Aspiration pneumonia**, **Failure to thrive**. (warnier2022clinicaloverviewand pages 10-11, mikelonis2014stüvewiedemannsyndromelifr pages 7-8)
- **Autonomic/neurologic:** episodic hyperthermia, paradoxical or excessive sweating, temperature instability, reduced pain perception, absent corneal reflex, reduced patellar reflex, hypotonia and sometimes myotonia. Dysautonomia often becomes less severe with age but may persist. Suggested HPO: **Dysautonomia**, **Hyperthermia**, **Hyperhidrosis**, **Reduced pain sensation**, **Absent corneal reflex**, **Areflexia**, **Hypotonia**, **Myotonia**. (warnier2022clinicaloverviewand pages 10-11, oxford2016neuropathiesofstüvewiedemann pages 6-8)
- **Ocular/oral:** corneal injury/opacification or neurotrophic keratopathy can follow absent corneal sensation; a smooth tongue has been reported. Suggested HPO: **Corneal opacity**, **Neurotrophic keratopathy**, **Absent corneal reflex**, **Smooth tongue**. (oxford2016neuropathiesofstüvewiedemann pages 6-8, bertola2016stüvewiedemannsyndromeupdate pages 2-3)
- **Development:** motor development may be delayed because of skeletal disease and hospitalization, but intellectual development is generally normal; all but one published case in one review had normal cognition. Suggested HPO: **Delayed gross motor development**; avoid annotating intellectual disability as a defining feature. (bertola2016stüvewiedemannsyndromeupdate pages 1-2, warnier2022clinicaloverviewand pages 10-11)

### Frequency, severity, and quality of life

The 69-case review found, among children older than 2 years, restricted joint mobility in **81%**, spinal deformity in **77%**, and fractures in **61%**. Daily-life impact includes impaired mobility, recurrent hospitalization, tube feeding, vulnerability to heat, reduced injury awareness, eye-surface damage, orthopedic procedures, and caregiver burden. No validated SWS-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life dataset was identified. (warnier2022clinicaloverviewand pages 1-3)

## 4. Genetic and molecular information

### Causal gene and alleles

- **Gene:** LIFR, encoding the leukemia inhibitory factor receptor; locus 5p13.1. Retrieved sources describe a 1,097-amino-acid transmembrane cytokine receptor. (mikelonis2014stüvewiedemannsyndromelifr pages 2-3, bertola2016stüvewiedemannsyndromeupdate pages 5-6)
- **Variant spectrum:** predominantly frameshift, nonsense, and splice-disrupting alleles; occasional missense/non-truncating alleles may impair processing or glycosylation.
- **Origin:** inherited constitutional/germline, not somatic.
- **Functional class:** primarily loss of function via nonsense-mediated transcript decay, absent receptor, or severely truncated/nonfunctional protein.
- **Classification:** well-established null variants in affected recessive families are generally compatible with pathogenic/likely pathogenic ACMG classification, but each submitted allele requires transcript-specific ClinVar/ACMG review. The literature summary cannot replace current variant-level classification.
- **Population frequency:** no reliable disease-wide allele frequency or carrier frequency was recovered. Causal variants are expected to be rare; the UAE c.653dup founder allele may be locally enriched. (mikelonis2014stüvewiedemannsyndromelifr pages 2-3, bertola2016stüvewiedemannsyndromeupdate pages 5-6)

No confirmed somatic mechanism, pathogenic repeat expansion, mitochondrial variant, aneuploidy, balanced rearrangement, or recurrent large chromosomal abnormality defines classic SWS. Intragenic deletions can be missed by sequence-only assays, so deletion/duplication analysis remains relevant.

### Modifier genes and epigenetics

Variable severity among patients carrying the same frameshift suggests modifiers, residual signaling, or care effects, but no modifier gene is validated. Earlier candidate-region suggestions—including OSMR and several neighboring genes—are not established causes of classic SWS. No reproducible disease-specific DNA-methylation signature, histone change, chromatin defect, or epigenetic diagnostic assay was identified. (mikelonis2014stüvewiedemannsyndromelifr pages 7-8, mikelonis2014stüvewiedemannsyndromelifr pages 2-3)

### Critical distinction: IL6ST-related extended SWS

A 2020 primary study identified five affected people from three unrelated families with homozygous essential loss-of-function **IL6ST** variants. Complete GP130 deficiency abolished responses to IL-6, IL-11, IL-27, OSM, and LIF; lentiviral restoration of GP130 rescued signaling. The phenotype included SWS-like skeletal dysplasia and neonatal lung disease plus thrombocytopenia, dermatitis, renal abnormalities, and immune dysfunction. Thus IL6ST belongs on a differential or expanded bent-bone/GP130-signaling panel but is not the canonical cause of SWS1. (chen2020absenceofgp130 pages 8-9, chen2020absenceofgp130 pages 1-1)

## 5. Environmental information

No environmental, lifestyle, infectious, radiation, pollution, or occupational cause is applicable. Smoking, alcohol, diet, and exercise do not determine disease occurrence. Avoidance of overheating, aspiration, and preventable skeletal injury is clinically important but does not prevent the genotype or congenital phenotype. Vaccination against routine respiratory pathogens is sensible standard care, not SWS-specific immunization.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream lesion:** biallelic LIFR loss-of-function variants destabilize mRNA or prevent production/trafficking of functional LIFR.
2. **Receptor defect:** LIFR cannot form effective signaling complexes with GP130 for relevant IL-6-family ligands, including LIF, cardiotrophin-1, oncostatin M, CNTF-associated complexes, and CLCF1-associated signaling.
3. **Signal failure:** ligand-induced JAK activation and STAT3 phosphorylation are impaired; MAPK and PI3K signaling may also be reduced.
4. **Developmental consequences:** disturbed bone formation/remodeling, osteoclast imbalance, motor/autonomic neuronal dysfunction, and impaired neuromuscular/respiratory homeostasis.
5. **Clinical output:** congenital bowing and contractures; osteopenia/fractures; impaired swallowing and respiration; abnormal sweating, thermoregulation, nociception, and reflexes. (bertola2016stüvewiedemannsyndromeupdate pages 5-5, bertola2016stüvewiedemannsyndromeupdate pages 5-6, oxford2016neuropathiesofstüvewiedemann pages 5-6)

Suggested GO biological-process terms are **cytokine-mediated signaling pathway**, **JAK–STAT cascade**, **STAT protein phosphorylation**, **skeletal system development**, **bone remodeling**, **osteoclast differentiation**, **motor-neuron development**, **autonomic nervous system development**, and **regulation of body temperature**. Suggested cell types are **osteoblast**, **osteoclast**, **chondrocyte**, **motor neuron**, **sensory neuron**, **sympathetic neuron**, **skeletal myocyte**, and pulmonary vascular cells. These ontology labels should be assigned only at evidence-appropriate granularity.

### Protein, cellular, metabolic, and immune effects

The primary biochemical abnormality is **cytokine-receptor dysfunction**, not an enzyme deficiency or ion-channel defect. Lifr-null mice show reduced fetal bone volume, increased osteoclasts, neural defects, and perinatal death, supporting effects on skeletal and nervous-system development. (bertola2016stüvewiedemannsyndromeupdate pages 5-5, mikelonis2014stüvewiedemannsyndromelifr pages 2-3)

Classic LIFR-SWS is not primarily an immunodeficiency. Recurrent respiratory infections are often attributed to dysphagia and aspiration, although JAK/STAT impairment could contribute. Broad immunodeficiency is much more characteristic of complete IL6ST/GP130 deficiency and should prompt reconsideration of the molecular diagnosis. (chen2020absenceofgp130 pages 1-1, warnier2022clinicaloverviewand pages 11-12)

No validated SWS-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signature was identified. Functional patient-cell assays measuring ligand-induced pSTAT3 are research tools, not routine diagnostics. Recent structural work on GP130-family complexes improves receptor-level understanding, but it has not yet produced an SWS therapy.

## 7. Anatomical structures affected

- **Primary organs/systems:** skeleton—especially femora, tibiae, spine, hips, hands and feet; peripheral autonomic, sensory and motor nervous systems; respiratory tract and lungs; swallowing apparatus; and cornea.
- **Secondary involvement:** pulmonary vasculature in PAH; recurrent lung injury from aspiration; osteoporosis and progressive vertebral/hip damage.
- **Suggested UBERON labels:** long bone, femur, tibia, vertebral column, hip joint, lung, pulmonary artery, pharynx, esophagus, cornea, peripheral nervous system and autonomic nervous system.
- **Suggested Cell Ontology labels:** chondrocyte, osteoblast, osteoclast, motor neuron, sensory neuron, sympathetic neuron, corneal epithelial cell and pulmonary arterial smooth-muscle cell.
- **Subcellular level:** plasma-membrane receptor complex and cytoplasmic JAK/STAT machinery; suggested GO cellular components include **plasma membrane**, **receptor complex**, **cytoplasm**, and **nucleus**.
- Long-bone and ocular findings are generally bilateral/systemic rather than characteristically unilateral. (oxford2016neuropathiesofstüvewiedemann pages 6-8, bertola2016stüvewiedemannsyndromeupdate pages 5-5, warnier2022clinicaloverviewand pages 1-3)

## 8. Temporal development and natural history

Onset is congenital, with an antenatal skeletal phenotype in a subset and acute neonatal respiratory, feeding, and thermoregulatory disease. The critical period is birth through age 2, when respiratory failure, aspiration, hyperthermic crises, and PAH drive mortality. Dysphagia often improves by ages 2–3 and temperature crises tend to become less frequent, but skeletal disease remains chronic and progressive. (warnier2022clinicaloverviewand pages 1-3, warnier2022clinicaloverviewand pages 10-11)

A practical, nonvalidated staging scheme is:

1. **Prenatal:** short/bowed long bones, reduced movement or contractures; sometimes late growth restriction.
2. **Neonatal–2 years:** highest-risk dysautonomic/respiratory phase.
3. **Childhood survivor phase:** improving swallowing and autonomic stability, accumulating fractures, contractures and spinal/hip deformity.
4. **Adolescent/adult phase:** lifelong orthopedic disability and residual autonomic/ocular risk; rare long-term survivors are documented.

There is no true remission of the genetic disorder. Apparent improvement reflects maturation and survival of the early autonomic phase, not molecular correction. (bertola2016stüvewiedemannsyndromeupdate pages 2-2, warnier2022clinicaloverviewand pages 10-11)

## 9. Inheritance and population

Inheritance is autosomal recessive. For two confirmed carriers, each pregnancy has an expected 25% affected, 50% carrier, and 25% non-carrier/non-affected probability. Penetrance of two severe null alleles appears high, but expressivity and survival are variable. No anticipation is expected. Germline mosaicism is not established as a major mechanism, although standard residual recurrence counseling applies when parental testing is incomplete.

General-population prevalence and incidence are unknown. One review cited approximately **0.52 per 10,000 births** in highly inbred populations, which must not be generalized globally. Cases have been reported in Europe, Africa, the Americas, and the Middle East. Both sexes are affected; no validated sex bias exists. Consanguinity and the UAE founder allele explain regional enrichment. (bertola2016stüvewiedemannsyndromeupdate pages 2-2, mikelonis2014stüvewiedemannsyndromelifr pages 2-3)

No robust global carrier frequency, ethnicity-stratified incidence, or national registry estimate was found.

## 10. Diagnostics

### Clinical and imaging diagnosis

Suspect SWS in a fetus or neonate with short, bowed long bones plus contractures and disproportionate dysautonomia, respiratory distress, dysphagia, unexplained hyperthermia or abnormal sweating. A skeletal survey may show bowed femora/tibiae, diaphyseal cortical thickening, widened metaphyses, abnormal trabeculation and reduced density. Echocardiography is important because PAH is a major prognostic marker. Swallow assessment, respiratory evaluation, nutritional assessment, ophthalmologic examination, and bone-density/orthopedic surveillance define complications. (warnier2022clinicaloverviewand pages 1-3, bertola2016stüvewiedemannsyndromeupdate pages 2-3)

There is no validated biochemical biomarker, enzyme assay, characteristic metabolite, pathology stain, EEG/EMG signature, or circulating marker. Laboratory investigations should evaluate complications—blood gases, infection, electrolytes, calcium/vitamin D status, rhabdomyolysis when suspected, and adrenal function if clinically indicated—rather than confirm SWS.

### Molecular strategy

1. **First line:** sequence LIFR with deletion/duplication analysis if phenotype is classic and family history is informative.
2. **Panel:** bent-bone/skeletal-dysplasia or dysautonomia panel including LIFR; include IL6ST, SOX9, SLC26A2 and other phenotype-driven differentials.
3. **WES/WGS:** appropriate for atypical or panel-negative disease, consanguineous families, or suspected structural/noncoding alleles. WGS offers better structural and deep-intronic coverage.
4. **CMA/karyotype/FISH:** not first-line for a classic recessive single-gene phenotype, but CMA is reasonable if congenital anomalies or developmental findings suggest a copy-number disorder.
5. Mitochondrial and repeat-expansion testing are not routinely indicated.

RNA studies can clarify splice variants, while patient-cell pSTAT3 assays can establish functional consequences in research or specialized diagnostic settings. (chen2020absenceofgp130 pages 8-9, bertola2016stüvewiedemannsyndromeupdate pages 5-6)

### Differential diagnosis

Important differentials include campomelic dysplasia, kyphomelic dysplasia, diastrophic dysplasia, osteogenesis imperfecta/severe bone-fragility disorders, and other congenital bowing or arthrogryposis syndromes. Campomelic dysplasia is suggested by SOX9-related scapular/pelvic abnormalities, 11 rib pairs, sex-development differences, and characteristic craniofacial findings. SWS is distinguished by its marked dysautonomia, episodic hyperthermia, sweating disturbance, reduced pain sensation, and LIFR genotype. (bertola2016stüvewiedemannsyndromeupdate pages 2-2)

### Screening

SWS is not part of routine biochemical newborn screening. Targeted carrier/cascade testing is appropriate for relatives after familial variants are known. Prenatal diagnosis may use chorionic-villus sampling or amniocentesis for the familial alleles; ultrasound alone is insufficiently sensitive because only 46% of cases in the systematic review had reported antenatal signs. (warnier2022clinicaloverviewand pages 1-3, bertola2016stüvewiedemannsyndromeupdate pages 2-2)

## 11. Outcomes and prognosis

The systematic-review abstract states: **“Mortality rate is higher during the first 2 years (42% <2 years; 10% >2 years) mainly due to respiratory failure,”** and identifies PAH as a poor prognostic factor with **63% mortality**. These are the most defensible quantitative estimates, but not population survival rates. Five- and ten-year survival and life expectancy are unknown. (warnier2022clinicaloverviewand pages 1-3)

Poor prognostic factors include neonatal respiratory failure, recurrent aspiration/infection, severe dysphagia, frequent hyperthermic crises, and especially PAH. Surviving beyond age 2 is favorable for near-term survival, but fractures, spinal deformity, restricted mobility, chronic pain or unrecognized injury, and ocular damage cause lifelong morbidity. Cognitive prognosis is usually favorable. No validated molecular prognostic biomarker exists. (warnier2022clinicaloverviewand pages 10-11, warnier2022clinicaloverviewand pages 1-3)

## 12. Treatment and current applications

### Standard care

No curative, FDA/EMA-approved disease-modifying, genotype-guided, gene, cell, RNA, or immunotherapy exists. Management is supportive and coordinated through pediatrics, pulmonology, cardiology, clinical genetics, nutrition/gastroenterology, orthopedics, rehabilitation, ophthalmology, dentistry and anesthesia. (warnier2022clinicaloverviewand pages 10-11, bhalla2024anoveltermination pages 5-6)

- **Airway/feeding:** aspiration precautions; swallow evaluation; thickened or modified feeds where safe; nasogastric feeding in the short term and gastrostomy when prolonged enteral support is needed. Respiratory support and prompt treatment of infections are central. Suggested NCIT concepts: *Supportive Care*, *Nasogastric Intubation*, *Gastrostomy*, *Respiratory Therapy*. (mikelonis2014stüvewiedemannsyndromelifr pages 7-8, bhalla2024anoveltermination pages 5-6)
- **Thermoregulation:** cooling plans and hydration, with antipyretic/comfort measures. A 2024 case described escalation using acetaminophen, ibuprofen and bromocriptine; this is case-level practice, not trial-validated therapy, and autonomic hyperthermia may not respond like infectious fever. Suggested CHEBI/NCIT entities: acetaminophen, ibuprofen, bromocriptine. (bhalla2024anoveltermination pages 5-6)
- **Cardiopulmonary:** screen for and manage PAH with specialist protocols; no SWS-specific PAH regimen has been tested.
- **Bone/orthopedic:** physiotherapy, positioning, braces, calcium/vitamin-D sufficiency, consideration of bisphosphonates for bone fragility, fracture treatment, and correction of severe limb/spinal deformity. Telescopic intramedullary rods may reduce recurrent deformity compared with fixed rods. Suggested NCIT concepts: *Physical Therapy*, *Orthotic Device*, *Bisphosphonate Therapy*, *Intramedullary Rod Placement*. (warnier2022clinicaloverviewand pages 10-11)
- **Eyes:** frequent corneal surveillance, lubrication and protection because absent corneal sensation can allow silent injury. Contemporary case literature has explored surgical management of neurotrophic keratopathy, but comparative outcomes are unavailable.
- **Safety/rehabilitation:** daily skin and limb checks for painless injury; physical and occupational therapy; mobility aids; home temperature planning; dental surveillance.

### Anesthesia

Malignant-hyperthermia concern has historically complicated planning, but the 2024 review notes multiple reported anesthetics without malignant hyperthermia. This absence of reported events does not prove no risk; preoperative pulmonary, PAH, airway, aspiration and temperature assessment remains essential. (bhalla2024anoveltermination pages 5-6)

### Experimental approaches

Gentamicin produced experimental premature-stop-codon readthrough and has been proposed only for selected nonsense alleles. Nephrotoxicity, ototoxicity, uncertain tissue exposure and lack of clinical efficacy data prevent routine use. Antisense exon skipping and CRISPR correction remain conceptual/preclinical. No relevant disease-specific interventional ClinicalTrials.gov study was found by the tool search. (bertola2016stüvewiedemannsyndromeupdate pages 2-2, oxford2016neuropathiesofstüvewiedemann pages 6-8)

## 13. Prevention

Because SWS is a congenital Mendelian disorder, diet, lifestyle, vaccination, or exposure avoidance cannot provide primary prevention. Effective reproductive prevention options are:

- preconception genetic counseling;
- cascade carrier testing after identification of familial LIFR variants;
- partner testing in high-risk or founder populations;
- preimplantation genetic testing for monogenic disease;
- prenatal molecular diagnosis by CVS or amniocentesis;
- detailed fetal ultrasonography, recognizing incomplete sensitivity.

Secondary/tertiary prevention consists of early molecular diagnosis, aspiration prevention, PAH screening, thermoregulation plans, corneal protection, fracture prevention and multidisciplinary surveillance. Routine immunization is appropriate to reduce preventable respiratory disease but is not disease-specific prophylaxis. (warnier2022clinicaloverviewand pages 10-11, bertola2016stüvewiedemannsyndromeupdate pages 2-2)

## 14. Other species and natural disease

No well-established naturally occurring veterinary homolog of human LIFR-related SWS was identified; zoonotic transmission is not applicable. Orthologous LIFR genes are evolutionarily conserved across vertebrates, but the evidence base concerns experimentally engineered rather than naturally diseased animals. Suggested taxonomy for the main experimental model is **Mus musculus** (NCBI Taxonomy 10090). Breed-specific VBO annotation is not applicable.

## 15. Model organisms and advanced research

The principal model is the **Lifr-null mouse**. Homozygous knockout causes placental, skeletal, neural and metabolic abnormalities with perinatal lethality. Reported disease-relevant findings include reduced fetal bone volume, increased osteoclasts and reduced astrocytic/neural populations. This recapitulates developmental skeletal and neurologic severity and supports LIFR causality. Its limitations are perinatal death, incomplete modeling of long-term human survivor phenotypes, and species differences in placentation and cytokine redundancy. (bertola2016stüvewiedemannsyndromeupdate pages 5-5, mikelonis2014stüvewiedemannsyndromelifr pages 2-3)

Patient-derived fibroblasts or lymphoblastoid cells are useful for receptor expression and ligand-induced pSTAT3 assays. In the related IL6ST disorder, transfection and lentiviral rescue experiments directly restored GP130 signaling, providing proof that receptor replacement can correct the cellular defect, although this is not yet a therapy. (chen2020absenceofgp130 pages 8-9, chen2020absenceofgp130 pages 1-1)

## Recent developments, 2023–2024

1. **Longer survival is increasingly recognized.** A 2024 report described a 5-year-old survivor and emphasized structured home hyperthermia and respiratory plans rather than assuming universal infant lethality. The abstract summarizes SWS as characterized by “bowing of long bones, dysautonomia, temperature dysregulation, swallowing and feeding difficulties, and frequent respiratory infections.” Published April 2024; DOI: https://doi.org/10.3389/fped.2024.1341841. (bhalla2024anoveltermination pages 5-6)
2. **Survivor-focused care expanded in 2023 literature**, including a UK pediatric survivor series referenced in the 2024 report. Evidence remains small-series level and does not supersede the 69-case systematic review. (bhalla2024anoveltermination pages 6-6)
3. **Ophthalmic implementation:** 2023–2024 reports described surgical treatment of neurotrophic corneal disease, including tarsoconjunctival approaches and corneal neurotization. These are individualized procedures without controlled comparative evidence.
4. **Structural cytokine-receptor biology advanced.** Cryo-EM studies of GP130-family ligand–receptor complexes clarified how LIF, CLCF1 and related cytokines assemble signaling complexes. This improves mechanistic interpretation but has not yielded an SWS-targeted drug.
5. **Variant discovery continues**, but most 2023–2024 reports are single cases. Current expert interpretation remains that prompt recognition and multidisciplinary supportive care offer the clearest near-term benefit; disease-modifying receptor restoration remains an unmet research need. (bhalla2024anoveltermination pages 5-6)

## Evidence limitations and knowledge gaps

There are no population registries large enough to provide reliable incidence, sex ratio, carrier frequency, five- or ten-year survival, or treatment-response rates. Phenotype frequencies derive from reported cases and likely overrepresent severe and unusual presentations. No controlled therapeutic trial, validated clinical guideline, SWS-specific quality-of-life measure, prognostic molecular biomarker, modifier gene, protective allele, epigenetic signature, or diagnostic multi-omics profile was identified. Exact MONDO, Orphanet, MeSH and ICD identifiers require direct validation against live databases. PMID values were not consistently exposed in the retrieved full texts; therefore DOI URLs and publication dates are supplied rather than inventing identifiers.

## Key source list

- Warnier H, et al. **Clinical overview and outcome of the Stuve-Wiedemann syndrome: a systematic review.** *Orphanet Journal of Rare Diseases*. Published April 2022. https://doi.org/10.1186/s13023-022-02323-8. (warnier2022clinicaloverviewand pages 1-3)
- Dagoneau N, et al. **Null leukemia inhibitory factor receptor mutations in Stuve-Wiedemann/Schwartz-Jampel type 2 syndrome.** *American Journal of Human Genetics*. Published February 2004. https://doi.org/10.1086/381715. The retrieved evidence reports 19 families, 14 variants, and functional loss of LIFR/JAK–STAT3 signaling. (bertola2016stüvewiedemannsyndromeupdate pages 5-5, bertola2016stüvewiedemannsyndromeupdate pages 5-6)
- Mikelonis D, et al. **Stüve-Wiedemann syndrome: LIFR and associated cytokines in clinical course and etiology.** *Orphanet Journal of Rare Diseases*. Published March 2014. https://doi.org/10.1186/1750-1172-9-34. (mikelonis2014stüvewiedemannsyndromelifr pages 7-8, mikelonis2014stüvewiedemannsyndromelifr pages 2-3)
- Bertola DR, et al. **Stüve-Wiedemann Syndrome: Update on Clinical and Genetic Aspects.** *Molecular Syndromology*. Published March 2016. https://doi.org/10.1159/000444729. (bertola2016stüvewiedemannsyndromeupdate pages 1-2, bertola2016stüvewiedemannsyndromeupdate pages 2-3)
- Chen Y-H, et al. **Absence of GP130 cytokine receptor signaling causes extended Stüve-Wiedemann syndrome.** *Journal of Experimental Medicine*. Published January 2020. https://doi.org/10.1084/jem.20191306. (chen2020absenceofgp130 pages 8-9, chen2020absenceofgp130 pages 1-1)
- Bhalla DM, et al. **A novel termination site in a case of Stüve–Wiedemann syndrome: case report and review of literature.** *Frontiers in Pediatrics*. Published April 2024. https://doi.org/10.3389/fped.2024.1341841. (bhalla2024anoveltermination pages 5-6)

References

1. (warnier2022clinicaloverviewand pages 1-3): Hélène Warnier, Christophe Barrea, Sarah Bethlen, Isabelle Schrouff, and Julie Harvengt. Clinical overview and outcome of the stuve-wiedemann syndrome: a systematic review. Orphanet Journal of Rare Diseases, Apr 2022. URL: https://doi.org/10.1186/s13023-022-02323-8, doi:10.1186/s13023-022-02323-8. This article has 22 citations and is from a peer-reviewed journal.

2. (warnier2022clinicaloverviewand pages 10-11): Hélène Warnier, Christophe Barrea, Sarah Bethlen, Isabelle Schrouff, and Julie Harvengt. Clinical overview and outcome of the stuve-wiedemann syndrome: a systematic review. Orphanet Journal of Rare Diseases, Apr 2022. URL: https://doi.org/10.1186/s13023-022-02323-8, doi:10.1186/s13023-022-02323-8. This article has 22 citations and is from a peer-reviewed journal.

3. (chen2020absenceofgp130 pages 8-9): Yin-Huai Chen, Giedre Grigelioniene, Phillip T. Newton, Jacob Gullander, Maria Elfving, Anna Hammarsjö, Dominyka Batkovskyte, Hessa S. Alsaif, Wesam I.Y. Kurdi, Firdous Abdulwahab, Veerabahu Shanmugasundaram, Luke Devey, Séverine Bacrot, Jana Brodszki, Celine Huber, Ben Hamel, David Gisselsson, Nikos Papadogiannakis, Katarina Jedrycha, Barbara Gürtl-Lackner, Andrei S. Chagin, Gen Nishimura, Dominik Aschenbrenner, Fowzan S. Alkuraya, Arian Laurence, Valérie Cormier-Daire, and Holm H. Uhlig. Absence of gp130 cytokine receptor signaling causes extended stüve-wiedemann syndrome. The Journal of Experimental Medicine, Jan 2020. URL: https://doi.org/10.1084/jem.20191306, doi:10.1084/jem.20191306. This article has 75 citations.

4. (chen2020absenceofgp130 pages 1-1): Yin-Huai Chen, Giedre Grigelioniene, Phillip T. Newton, Jacob Gullander, Maria Elfving, Anna Hammarsjö, Dominyka Batkovskyte, Hessa S. Alsaif, Wesam I.Y. Kurdi, Firdous Abdulwahab, Veerabahu Shanmugasundaram, Luke Devey, Séverine Bacrot, Jana Brodszki, Celine Huber, Ben Hamel, David Gisselsson, Nikos Papadogiannakis, Katarina Jedrycha, Barbara Gürtl-Lackner, Andrei S. Chagin, Gen Nishimura, Dominik Aschenbrenner, Fowzan S. Alkuraya, Arian Laurence, Valérie Cormier-Daire, and Holm H. Uhlig. Absence of gp130 cytokine receptor signaling causes extended stüve-wiedemann syndrome. The Journal of Experimental Medicine, Jan 2020. URL: https://doi.org/10.1084/jem.20191306, doi:10.1084/jem.20191306. This article has 75 citations.

5. (mikelonis2014stüvewiedemannsyndromelifr pages 7-8): Dawn Mikelonis, Cheryl L Jorcyk, Ken Tawara, and Julia Thom Oxford. Stüve-wiedemann syndrome: lifr and associated cytokines in clinical course and etiology. Orphanet Journal of Rare Diseases, 9:34-34, Mar 2014. URL: https://doi.org/10.1186/1750-1172-9-34, doi:10.1186/1750-1172-9-34. This article has 47 citations and is from a peer-reviewed journal.

6. (bertola2016stüvewiedemannsyndromeupdate pages 1-2): Débora Romeo Bertola, Rachel S. Honjo, and Wagner A.R. Baratela. Stüve-wiedemann syndrome: update on clinical and genetic aspects. Molecular Syndromology, 7:12-18, Mar 2016. URL: https://doi.org/10.1159/000444729, doi:10.1159/000444729. This article has 38 citations and is from a peer-reviewed journal.

7. (bertola2016stüvewiedemannsyndromeupdate pages 5-5): Débora Romeo Bertola, Rachel S. Honjo, and Wagner A.R. Baratela. Stüve-wiedemann syndrome: update on clinical and genetic aspects. Molecular Syndromology, 7:12-18, Mar 2016. URL: https://doi.org/10.1159/000444729, doi:10.1159/000444729. This article has 38 citations and is from a peer-reviewed journal.

8. (mikelonis2014stüvewiedemannsyndromelifr pages 2-3): Dawn Mikelonis, Cheryl L Jorcyk, Ken Tawara, and Julia Thom Oxford. Stüve-wiedemann syndrome: lifr and associated cytokines in clinical course and etiology. Orphanet Journal of Rare Diseases, 9:34-34, Mar 2014. URL: https://doi.org/10.1186/1750-1172-9-34, doi:10.1186/1750-1172-9-34. This article has 47 citations and is from a peer-reviewed journal.

9. (bertola2016stüvewiedemannsyndromeupdate pages 5-6): Débora Romeo Bertola, Rachel S. Honjo, and Wagner A.R. Baratela. Stüve-wiedemann syndrome: update on clinical and genetic aspects. Molecular Syndromology, 7:12-18, Mar 2016. URL: https://doi.org/10.1159/000444729, doi:10.1159/000444729. This article has 38 citations and is from a peer-reviewed journal.

10. (bertola2016stüvewiedemannsyndromeupdate pages 2-2): Débora Romeo Bertola, Rachel S. Honjo, and Wagner A.R. Baratela. Stüve-wiedemann syndrome: update on clinical and genetic aspects. Molecular Syndromology, 7:12-18, Mar 2016. URL: https://doi.org/10.1159/000444729, doi:10.1159/000444729. This article has 38 citations and is from a peer-reviewed journal.

11. (bertola2016stüvewiedemannsyndromeupdate pages 2-3): Débora Romeo Bertola, Rachel S. Honjo, and Wagner A.R. Baratela. Stüve-wiedemann syndrome: update on clinical and genetic aspects. Molecular Syndromology, 7:12-18, Mar 2016. URL: https://doi.org/10.1159/000444729, doi:10.1159/000444729. This article has 38 citations and is from a peer-reviewed journal.

12. (oxford2016neuropathiesofstüvewiedemann pages 6-8): Alexandra E Oxford, C. Jorcyk, and J. Oxford. Neuropathies of stüve-wiedemann syndrome due to mutations in leukemia inhibitory factor receptor (lifr) gene. Journal of neurology & neuromedicine, 1 7:37-44, Oct 2016. URL: https://doi.org/10.29245/2572.942x/2016/7.1068, doi:10.29245/2572.942x/2016/7.1068. This article has 8 citations.

13. (oxford2016neuropathiesofstüvewiedemann pages 5-6): Alexandra E Oxford, C. Jorcyk, and J. Oxford. Neuropathies of stüve-wiedemann syndrome due to mutations in leukemia inhibitory factor receptor (lifr) gene. Journal of neurology & neuromedicine, 1 7:37-44, Oct 2016. URL: https://doi.org/10.29245/2572.942x/2016/7.1068, doi:10.29245/2572.942x/2016/7.1068. This article has 8 citations.

14. (chen2020absenceofgp130 pages 1-2): Yin-Huai Chen, Giedre Grigelioniene, Phillip T. Newton, Jacob Gullander, Maria Elfving, Anna Hammarsjö, Dominyka Batkovskyte, Hessa S. Alsaif, Wesam I.Y. Kurdi, Firdous Abdulwahab, Veerabahu Shanmugasundaram, Luke Devey, Séverine Bacrot, Jana Brodszki, Celine Huber, Ben Hamel, David Gisselsson, Nikos Papadogiannakis, Katarina Jedrycha, Barbara Gürtl-Lackner, Andrei S. Chagin, Gen Nishimura, Dominik Aschenbrenner, Fowzan S. Alkuraya, Arian Laurence, Valérie Cormier-Daire, and Holm H. Uhlig. Absence of gp130 cytokine receptor signaling causes extended stüve-wiedemann syndrome. The Journal of Experimental Medicine, Jan 2020. URL: https://doi.org/10.1084/jem.20191306, doi:10.1084/jem.20191306. This article has 75 citations.

15. (bhalla2024anoveltermination pages 5-6): Deepali M. Bhalla, Sunil K Sati, Donald Basel, and Vijender Karody. A novel termination site in a case of stüve–wiedemann syndrome: case report and review of literature. Frontiers in Pediatrics, Apr 2024. URL: https://doi.org/10.3389/fped.2024.1341841, doi:10.3389/fped.2024.1341841. This article has 2 citations.

16. (warnier2022clinicaloverviewand pages 11-12): Hélène Warnier, Christophe Barrea, Sarah Bethlen, Isabelle Schrouff, and Julie Harvengt. Clinical overview and outcome of the stuve-wiedemann syndrome: a systematic review. Orphanet Journal of Rare Diseases, Apr 2022. URL: https://doi.org/10.1186/s13023-022-02323-8, doi:10.1186/s13023-022-02323-8. This article has 22 citations and is from a peer-reviewed journal.

17. (bhalla2024anoveltermination pages 6-6): Deepali M. Bhalla, Sunil K Sati, Donald Basel, and Vijender Karody. A novel termination site in a case of stüve–wiedemann syndrome: case report and review of literature. Frontiers in Pediatrics, Apr 2024. URL: https://doi.org/10.3389/fped.2024.1341841, doi:10.3389/fped.2024.1341841. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](Stuve_Wiedemann_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

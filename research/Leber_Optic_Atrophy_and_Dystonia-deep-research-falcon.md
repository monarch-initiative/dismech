---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T21:03:44.711820'
end_time: '2026-08-17T21:11:16.524788'
duration_seconds: 451.81
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Leber Optic Atrophy and Dystonia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Leber_Optic_Atrophy_and_Dystonia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leber Optic Atrophy and Dystonia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber Optic Atrophy and Dystonia** covering all of the
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
- **Disease Name:** Leber Optic Atrophy and Dystonia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leber Optic Atrophy and Dystonia** covering all of the
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


# Leber hereditary optic neuropathy with dystonia: disease-characteristics report

## Executive summary and entity clarification

**Leber optic atrophy and dystonia** is best interpreted as **Leber hereditary optic neuropathy with dystonia (LHON-dystonia; LHOND)**, a very rare mitochondrial disorder classically associated with the **MT-ND6 m.14459G>A** mitochondrial-DNA variant. It combines an LHON-like optic neuropathy with dystonia and basal-ganglia disease. It is **not** Mohr–Tranebjærg/deafness-dystonia-optic-neuronopathy syndrome, which is an X-linked nuclear disorder caused by **TIMM8A** variants. Open Targets likewise places MT-ND genes centrally in LHON and associates TIMM8A only with the broader hereditary-optic-neuropathy category. (OpenTargets Search: Leber optic atrophy and dystonia, yuwaiman2009inheritedmitochondrialoptic pages 10-10)

The subtype is so rare that most evidence consists of pedigrees, case reports, small cohorts, and transmitochondrial cybrid experiments. Consequently, prevalence, penetrance, phenotype frequencies, validated prognostic biomarkers, and treatment-response rates specific to LHOND remain unknown.

| domain | established finding | evidence type | key quantitative detail | source/year/DOI or PMID if present | confidence/limitations |
|---|---|---|---|---|---|
| Entity resolution | The requested disease is best resolved as mitochondrial **Leber hereditary optic neuropathy with dystonia** (LHON-dystonia/LHOND), not TIMM8A-related Mohr-Tranebjaerg syndrome. TIMM8A disease is an X-linked nuclear mitochondrial import disorder with hearing-loss–predominant phenotype, whereas LHON-dystonia is a maternal mtDNA disorder centered on optic neuropathy plus movement disorder. (OpenTargets Search: Leber optic atrophy and dystonia, yuwaiman2009inheritedmitochondrialoptic pages 10-10) | Review/database-supported disease distinction | Open Targets links **TIMM8A** to hereditary optic neuropathy only weakly, while classic LHON disease associations center on mtDNA complex I genes; TIMM8A review states pathogenic variants cause Mohr-Tranebjaerg syndrome. | Heinemeyer et al., 2019, DOI: 10.1089/dna.2018.4292; Open Targets context (OpenTargets Search: Leber optic atrophy and dystonia) | Moderate confidence for distinction; exact MONDO/OMIM mapping for the rare LHON-dystonia label not directly retrieved here. |
| Primary causal variant | The canonical variant for LHON-dystonia is **MT-ND6 m.14459G>A**. It has long been reported in maternally inherited families with optic neuropathy and dystonia and remains the main genotype linked to this entity. (yuwaiman2009inheritedmitochondrialoptic pages 10-10, cui2020clinicalfeaturesof pages 6-6) | Primary literature summarized in review; clinical cohort context | In a 2020 Chinese rare-mutation LHON series, **4/16** patients carried **m.14459G>A**; **1** had LHON plus dystonia. | Cui et al., 2020, *J Neuro-Ophthalmol*, DOI: 10.1097/WNO.0000000000000799 | High confidence that m.14459G>A is disease-defining; low sample size for phenotype frequencies. |
| Additional genetic heterogeneity | LHON-plus phenotypes with dystonia can also occur with other mtDNA complex I variants or double mutations, but these are not the classic LHON-dystonia entity. (berardo2020leberhereditaryoptic pages 1-3, yuwaiman2009inheritedmitochondrialoptic pages 10-10) | Case report + review | A 2020 case had double **MT-ND4/MT-ND6** mutations with optic neuropathy, dystonia, and transverse myelitis; not a pure m.14459G>A-only presentation. | Berardo et al., 2020, DOI: 10.1007/s00415-019-09619-z | Moderate confidence; demonstrates phenotypic overlap, not primary disease definition. |
| Inheritance | LHON-dystonia follows **maternal (mitochondrial) inheritance** because the causal variants are in mtDNA. (berardo2020leberhereditaryoptic pages 1-3, yuwaiman2009inheritedmitochondrialoptic pages 10-10) | Review + case report | General LHON shows maternal transmission and incomplete penetrance; most primary LHON mutations are often homoplasmic. | Yu-Wai-Man et al., 2009, DOI: 10.1136/jmg.2007.054270; Berardo et al., 2020, DOI: 10.1007/s00415-019-09619-z | High confidence for inheritance; penetrance estimates specific to m.14459G>A were not retrieved. |
| Heteroplasmy/homoplasmy | Published LHON literature indicates many primary LHON mutations are **homoplasmic**, and review evidence specifically notes homoplasmic inheritance has been described with **m.14459G>A** despite variable clinical expression. (berardo2020leberhereditaryoptic pages 1-3, yuwaiman2009inheritedmitochondrialoptic pages 10-10) | Review/case-based synthesis | No robust disease-specific heteroplasmy percentage retrieved for LHON-dystonia. | Yu-Wai-Man et al., 2009, DOI: 10.1136/jmg.2007.054270 | Moderate confidence; variant-level quantitative heteroplasmy data are sparse in the retrieved evidence. |
| Mechanism: biochemical lesion | MT-ND6 m.14459G>A causes a **respiratory chain complex I defect**. Cybrid experiments were used to assign the defect directly to the mtDNA variant. (yuwaiman2009inheritedmitochondrialoptic pages 10-10) | Functional primary study summarized in review | The key mechanistic assignment was made in transmitochondrial cybrids. | Jun et al., 1996, *Mol Cell Biol*, DOI: 10.1128/MCB.16.3.771 | High confidence for mechanism; original article text was not directly extracted here, but the review cites it specifically. |
| Mechanism: cell injury cascade | General LHON pathophysiology supports that complex I dysfunction drives reduced oxidative phosphorylation, oxidative stress, impaired glutamate handling, and increased apoptotic susceptibility in retinal ganglion cells; these mechanisms are used to explain LHON-dystonia as a complex I neurodegenerative phenotype. (yuwaiman2009inheritedmitochondrialoptic pages 10-10) | Review of cellular/model studies | No LHON-dystonia-specific omics dataset retrieved; mechanism largely extrapolated from LHON/cybrid work. | Yu-Wai-Man et al., 2009, DOI: 10.1136/jmg.2007.054270 | Moderate confidence; strong biological plausibility but limited subtype-specific mechanistic profiling. |
| Core phenotype | The syndrome combines **Leber hereditary optic neuropathy** with **dystonia**; dystonia may precede ocular manifestations by years in mtDNA movement-disorder literature summarized by reviews. (yuwaiman2009inheritedmitochondrialoptic pages 10-10) | Review of case reports/families | No pooled frequency estimate for dystonia among m.14459G>A carriers retrieved. | Yu-Wai-Man et al., 2009, DOI: 10.1136/jmg.2007.054270 | Moderate confidence; based mainly on rare families/case reports. |
| MRI / neuroimaging | In rare-mutation LHON, MRI can show **optic atrophy** and optic pathway signal changes; in the patient with **m.14459G>A plus dystonia**, MRI also showed **basal ganglia T2 signal abnormalities**. (cui2020clinicalfeaturesof pages 6-6) | Clinical cohort | In the 16-patient series: optic atrophy in **62.5% (10/16)**; increased optic-nerve T2 signal in **38% (6/16)**; the single LHON+dystonia patient had basal-ganglia signal change. | Cui et al., 2020, DOI: 10.1097/WNO.0000000000000799 | Moderate confidence; useful radiologic clue, but data come from a small rare-mutation cohort. |
| Visual severity / course | Rare-mutation LHON generally causes substantial visual disability; in the same cohort most eyes were severely impaired. (cui2020clinicalfeaturesof pages 6-6) | Clinical cohort | **75% (24/32 eyes)** had worst Snellen BCVA **≤0.1**; mean onset age in the cohort was **15 ± 6 years**; male:female **15:1**. | Cui et al., 2020, DOI: 10.1097/WNO.0000000000000799 | Moderate confidence for rare-mutation LHON context; not specific to all LHON-dystonia cases. |
| Environmental / modifier factors | General LHON penetrance is modified by **sex**, mtDNA background/haplogroup, and reported environmental triggers such as **tobacco and alcohol**; estrogen has been discussed as potentially protective. (berardo2020leberhereditaryoptic pages 1-3) | Review/case-report background | No LHON-dystonia-specific exposure study retrieved. | Berardo et al., 2020, DOI: 10.1007/s00415-019-09619-z | Moderate confidence for LHON overall; low confidence for direct subtype-specific effect sizes. |
| 2023 diagnostic cohort context | A large 2023 hereditary optic neuropathy diagnostic series provides context for how unusual LHON-dystonia is relative to standard LHON. Among index cases diagnosed with LHON, the vast majority carried the 3 common LHON variants rather than rare variants like m.14459G>A. | Large retrospective diagnostic cohort | Positive LHON diagnosis in **199/1,126 (18%)** index cases; among these, **92% (184/199)** had one of 3 major mtDNA variants: **m.11778G>A 66.5%**, **m.3460G>A 15%**, **m.14484T>C 11%**. | Rocatcher et al., 2023, *Brain*, DOI: 10.1093/brain/awac395 | High confidence for diagnostic context; does not specifically enumerate LHON-dystonia. |
| Diagnostic approach | Diagnosis should integrate neuro-ophthalmic phenotype with **mtDNA testing**, especially for primary LHON variants and rarer complex I variants in atypical/LHON-plus cases; MRI abnormalities do not exclude LHON. (cui2020clinicalfeaturesof pages 6-6) | Clinical cohort + general disease context | MRI optic pathway signal abnormality occurred in **38%** of the rare-mutation cohort, underscoring that inflammatory-appearing imaging can still occur in LHON. | Cui et al., 2020, DOI: 10.1097/WNO.0000000000000799 | Moderate confidence; no formal subtype-specific guideline retrieved. |
| Current management | There is **no established disease-specific therapy for LHON-dystonia**. Management is extrapolated from LHON and movement-disorder care: visual rehabilitation, mitochondrial counseling, and symptomatic dystonia treatment. (berardo2020leberhereditaryoptic pages 1-3, yuwaiman2009inheritedmitochondrialoptic pages 10-10) | Review/case-based practice inference | No controlled trial specific to m.14459G>A LHON-dystonia retrieved. | Berardo et al., 2020, DOI: 10.1007/s00415-019-09619-z; Yu-Wai-Man et al., 2009, DOI: 10.1136/jmg.2007.054270 | Moderate confidence; evidence gap for subtype-directed treatment. |
| Trials / real-world implementation | Recent interventional development is concentrated in **general LHON**, especially **ND4 gene therapy** rather than m.14459G>A LHON-dystonia. Active/completed trials include **NCT07406854**, **NCT05293626**, **NCT03406104**, **NCT03293524**, **NCT03153293**, **NCT02064569**, **NCT01267422**, and nicotinamide/metabolomics studies. (OpenTargets Search: Leber optic atrophy and dystonia) | Clinical trial registry | Example enrollments: **95** (NCT07406854), **98** (NCT03293524), **159** (NCT03153293), **19** (NCT02064569). | ClinicalTrials.gov records via tool context (OpenTargets Search: Leber optic atrophy and dystonia) | High confidence that therapeutic development is active in LHON broadly; none retrieved were specific to MT-ND6 m.14459G>A dystonia. |
| Evidence gaps | Major gaps remain in **epidemiology**, **penetrance**, **natural history**, **modifier genes**, **formal diagnostic criteria**, **biomarkers**, **prognosis**, and **animal/subtype-specific models** for LHON-dystonia. Most evidence derives from isolated families, case reports, or broader LHON reviews. (berardo2020leberhereditaryoptic pages 1-3, yuwaiman2009inheritedmitochondrialoptic pages 10-10, cui2020clinicalfeaturesof pages 6-6) | Evidence synthesis | No robust prevalence/incidence estimate or prospective natural-history cohort specific to LHON-dystonia was retrieved. | Based on retrieved literature set (berardo2020leberhereditaryoptic pages 1-3, yuwaiman2009inheritedmitochondrialoptic pages 10-10, cui2020clinicalfeaturesof pages 6-6) | High confidence that evidence is sparse due to extreme rarity. |


*Table: This compact table summarizes the strongest retrieved evidence for Leber hereditary optic neuropathy with dystonia, emphasizing its distinction from TIMM8A disease, the central role of MT-ND6 m.14459G>A, and what is known versus still missing from the literature.*

## 1. Disease information

### Definition

LHOND is a **Mendelian mitochondrial cytopathy** in which a pathogenic mtDNA complex-I variant causes variable combinations of subacute or progressive bilateral optic neuropathy and dystonia. Other neurological manifestations can include bilateral striatal degeneration, ataxia, dysarthria, pyramidal signs, encephalopathy, and—occasionally—broader “LHON-plus” features. MT-ND6 m.14459G>A has been specifically linked to maternally inherited LHON-dystonia. (yuwaiman2009inheritedmitochondrialoptic pages 10-10)

### Identifiers and names

- **OMIM:** **500001**, historically “Leber optic atrophy and dystonia.”
- **MONDO:** A distinct subtype identifier was not securely recovered. Use **MONDO:0010788, Leber hereditary optic neuropathy**, with an explicit dystonia/LHON-plus qualifier rather than assigning an unverified subtype ID.
- **Broader MONDO term:** **MONDO:0020478, Leber plus disease** may also be relevant, but is broader than m.14459G>A LHOND. Open Targets links this category principally to MT-ND1, MT-ND3, MT-ND4, and MT-ND6. (OpenTargets Search: Leber optic atrophy and dystonia)
- **Orphanet:** No subtype-specific ORPHA identifier was verified from retrieved evidence.
- **ICD-10:** No unique LHOND code. Depending on the coding purpose, broader categories include hereditary optic atrophy/optic-nerve disorders and dystonia; local coding guidance is required.
- **ICD-11/MeSH:** No verified subtype-specific term was retrieved; use LHON plus dystonia as compositional coding.
- **Synonyms:** LHON with dystonia; LHON-dystonia; LHOND; maternally inherited Leber hereditary optic neuropathy and dystonia; Leber optic atrophy and dystonia; m.14459G>A-associated LHON-plus.

This report synthesizes **aggregated disease-level resources and published human families/cases**, not patient-level EHR data.

## 2. Etiology, risk, and protective factors

### Causal factors

The canonical cause is a **germline mitochondrial-DNA variant, MT-ND6 m.14459G>A**, affecting NADH dehydrogenase subunit 6 of respiratory-chain complex I. Functional cybrid work assigned a complex-I defect directly to this mtDNA mutation. (yuwaiman2009inheritedmitochondrialoptic pages 10-10)

Additional mtDNA variants can produce clinically overlapping LHON-plus/dystonia phenotypes. A 2020 report described optic neuropathy, dystonia, ataxia, dysarthria, ptosis, and recurrent transverse myelitis with double **MT-ND4 m.11778G>A** and **MT-ND6 m.14484T>C** mutations; this illustrates genetic heterogeneity but should not be collapsed into classic m.14459G>A LHOND. (berardo2020leberhereditaryoptic pages 1-3)

### Risk and modifier factors

- **Genetic:** mutant load/heteroplasmy, mtDNA haplogroup, nuclear genetic background, sex, and tissue-specific mitochondrial thresholds plausibly modify expression. Most conventional LHON mutations are homoplasmic, and homoplasmic m.14459G>A can still show markedly variable expression, demonstrating that genotype alone does not determine phenotype. (berardo2020leberhereditaryoptic pages 1-3, yuwaiman2009inheritedmitochondrialoptic pages 10-10)
- **Sex:** LHON overall has strong male predominance. A rare-mutation Chinese cohort had a male:female ratio of **15:1**, although this is not a subtype-specific penetrance estimate. (cui2020clinicalfeaturesof pages 6-6)
- **Environment:** smoking and heavy alcohol exposure are recognized general-LHON risk modifiers; mitochondrial toxins and medications should be minimized where clinically feasible. Direct m.14459G>A-specific effect sizes are unavailable. (berardo2020leberhereditaryoptic pages 1-3)
- **Potential protection:** estrogen-associated mitochondrial effects have been proposed to contribute to lower female penetrance in LHON. This is mechanistic/observational evidence, not an established preventive treatment. (berardo2020leberhereditaryoptic pages 1-3)
- **Family history:** maternal relatives may carry the variant even when clinically unaffected because penetrance is incomplete.

No validated protective allele, diet, supplement, or lifestyle intervention has been demonstrated specifically for LHOND. There is no infectious cause.

## 3. Phenotypes

| Phenotype | Clinical characterization | Suggested HPO term |
|---|---|---|
| Optic neuropathy/optic atrophy | Central visual loss, dyschromatopsia and central/cecocentral scotoma; typically bilateral and sequential or simultaneous; may progress to severe permanent visual disability | Optic atrophy **HP:0000648**; Visual loss **HP:0000572**; Central scotoma **HP:0000603**; Dyschromatopsia **HP:0007641** |
| Dystonia | Focal, segmental, or generalized sustained/posturing movements; may precede visual disease by years; severity is highly variable | Dystonia **HP:0001332**; Generalized dystonia **HP:0007325** |
| Basal-ganglia degeneration | T2 signal changes or bilateral striatal lesions; correlates with dystonia and other movement abnormalities | Abnormal basal-ganglia MRI **HP:0012758** |
| Ataxia/gait impairment | Reported in LHON-plus presentations; affects mobility and independence | Ataxia **HP:0001251**; Gait disturbance **HP:0001288** |
| Dysarthria | May accompany generalized dystonia or cerebellar/basal-ganglia involvement | Dysarthria **HP:0001260** |
| Pyramidal signs/weakness | Variable and uncommon; should prompt assessment for broader mitochondrial disease | Hyperreflexia **HP:0001347**; Muscle weakness **HP:0001324** |
| Ptosis | Reported in broader LHON-plus phenotypes, not obligatory for classic LHOND | Ptosis **HP:0000508** |

In 16 Chinese patients with rare primary LHON mutations, mean onset was **15 ± 6 years**, **24/32 eyes (75%)** reached best-corrected visual acuity ≤0.1 (≤20/200), optic atrophy was present in **10/16 (62.5%)**, and optic-nerve T2 hyperintensity in **6/16 (38%)**. Four patients carried m.14459G>A, but only one had documented LHON plus dystonia; therefore these aggregate visual percentages must not be interpreted as m.14459G>A-dystonia frequencies. (cui2020clinicalfeaturesof pages 6-6)

Quality-of-life studies specific to LHOND were not found. Expected burden is substantial: central blindness impairs reading, driving and face recognition, while dystonia can impair walking, hand use, speech, feeding, comfort, and social participation.

## 4. Genetic and molecular information

### Primary gene and variant

- **Gene:** **MT-ND6**, mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 6.
- **Canonical variant:** **m.14459G>A**, a mitochondrial missense variant commonly described as **p.Ala72Val** under the standard mitochondrial code/reference framework.
- **Origin:** constitutional/germline mtDNA; maternal transmission. It is not a somatic cancer variant.
- **Consequence:** altered complex-I membrane-arm function, impaired oxidative phosphorylation, and tissue-selective neuronal degeneration.
- **Population frequency:** no reliable frequency suitable for this report was retrieved from population databases; the pathogenic genotype is extremely rare.

A contemporary diagnostic context comes from 2,186 probands evaluated for hereditary optic neuropathy: only **199/1,126 (18%)** referred for LHON testing received a molecular diagnosis, and **184/199 (92%)** diagnosed cases carried one of the three common variants—m.11778G>A (66.5%), m.3460G>A (15%), or m.14484T>C (11%). Thus rare variants such as m.14459G>A form a small residual fraction. Publication: February 2023, DOI: https://doi.org/10.1093/brain/awac395.

### Other genetic findings

- Rare **MT-ND1**, **MT-ND3**, **MT-ND4**, and other **MT-ND6** variants can cause LHON-plus or dystonia-overlap phenotypes. Open Targets records associations of MT-ND1, MT-ND3, MT-ND4 and MT-ND6 with Leber-plus disease. (OpenTargets Search: Leber optic atrophy and dystonia)
- No reproducible nuclear **modifier gene** specific to m.14459G>A LHOND is established.
- No disease-specific methylation signature, chromatin abnormality, aneuploidy, translocation, or repeat expansion is established.
- Large mtDNA deletions and nuclear copy-number variants are not the canonical mechanism.

## 5. Environmental and lifestyle information

There is no evidence that environmental exposure alone causes LHOND. Rather, environment may alter penetrance in a genetically susceptible carrier. Avoidance of tobacco, excessive alcohol, and unnecessary mitochondrial-toxic exposures is biologically reasonable and standard LHON counseling, but subtype-specific prevention trials are absent. (berardo2020leberhereditaryoptic pages 1-3)

Regular nutrition and exercise within neurological limitations support general health but are not proven to prevent conversion. No pathogen, zoonosis, radiation exposure, occupational agent, or pollution exposure has been causally established.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** maternal MT-ND6 m.14459G>A.
2. **Primary biochemical defect:** altered ND6 impairs mitochondrial respiratory-chain **complex I**. Transmitochondrial cybrids demonstrated that the variant itself produces the complex-I defect, separating mtDNA causation from nuclear background. (yuwaiman2009inheritedmitochondrialoptic pages 10-10)
3. **Metabolic consequences:** impaired electron transport and proton pumping reduce respiratory efficiency/ATP reserve and increase redox imbalance and reactive oxygen species.
4. **Cellular stress:** altered mitochondrial membrane potential, calcium handling, glutamate transport, and apoptotic susceptibility promote neuronal injury. General LHON cybrid and retinal models show oxidative injury and enhanced death-signaling susceptibility. (yuwaiman2009inheritedmitochondrialoptic pages 10-10)
5. **Tissue selectivity:** small-caliber retinal ganglion cells of the papillomacular bundle and basal-ganglia neurons have high energy demands and long axons, making them vulnerable to limited mitochondrial reserve.
6. **Clinical manifestation:** retinal-ganglion-cell and optic-nerve axonal loss produces central blindness; striatal/basal-ganglia injury disrupts motor circuits and produces dystonia.

### Suggested ontology annotations

- **GO biological process:** mitochondrial electron transport, NADH to ubiquinone (**GO:0006120**); oxidative phosphorylation (**GO:0006119**); ATP metabolic process (**GO:0046034**); response to oxidative stress (**GO:0006979**); neuron apoptotic process (**GO:0051402**).
- **GO cellular component:** mitochondrion (**GO:0005739**); mitochondrial inner membrane (**GO:0005743**); respiratory-chain complex I (**GO:0005747**).
- **Cell Ontology:** retinal ganglion cell (**CL:0000740**); neuron (**CL:0000540**); astrocyte (**CL:0000127**) as a plausible secondary participant.
- **CHEBI:** ATP (**CHEBI:15422**); reactive oxygen species (**CHEBI:26523**); ubiquinone (**CHEBI:16389**).

No subtype-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, epigenomic, or multi-omic dataset was identified. Mechanistic inference therefore rests chiefly on biochemical assays, cybrids, general LHON models, imaging, and neuropathology.

## 7. Anatomical structures affected

- **Primary organ/system:** eye and central nervous system.
- **Primary site:** retinal ganglion-cell layer, papillomacular bundle, optic nerve, optic chiasm and tracts.
- **Motor site:** striatum/basal ganglia, particularly caudate-putamen circuitry; broader brain involvement can occur in LHON-plus disease.
- **Laterality:** optic neuropathy is usually bilateral, although onset may be sequential. Basal-ganglia abnormalities are often bilateral.
- **Subcellular site:** mitochondrial inner membrane and complex I.

Suggested anatomy terms include retina (**UBERON:0000966**), optic nerve (**UBERON:0000941**), optic chiasm (**UBERON:0001892**), basal ganglion (**UBERON:0002420**), and mitochondrion (**GO:0005739**). In the rare-mutation cohort, the m.14459G>A patient with dystonia had optic atrophy and increased basal-ganglia T2 signal. (cui2020clinicalfeaturesof pages 6-6)

## 8. Temporal development

Onset ranges from childhood through adulthood and varies within maternal pedigrees. Either dystonia or visual loss can occur first; movement disease may precede optic neuropathy by years. Visual loss is usually subacute and subsequently evolves to chronic optic atrophy, whereas dystonia commonly follows a chronic progressive course. (yuwaiman2009inheritedmitochondrialoptic pages 10-10)

A practical—not formally validated—staging framework is:

1. **Carrier/presymptomatic:** mtDNA variant present without functional deficits.
2. **Early neurological or ophthalmic disease:** dystonia, gait change, dyschromatopsia, central scotoma, or unilateral visual loss.
3. **Established bilateral disease:** severe bilateral central visual impairment with persistent or progressive dystonia.
4. **Advanced LHON-plus:** generalized dystonia, major mobility/speech impairment, and broader neurological involvement.

Spontaneous visual improvement is possible in LHON generally and varies by genotype, but recovery data specific to m.14459G>A LHOND are insufficient. There is no established remission pattern for the dystonia.

## 9. Inheritance and population

### Inheritance

- **Pattern:** mitochondrial/maternal.
- A carrier mother may transmit the variant to all children; only daughters transmit their mtDNA onward.
- **Penetrance:** incomplete, sex- and age-dependent, but no reliable m.14459G>A-specific percentage is available.
- **Expressivity:** markedly variable—from asymptomatic carrier, isolated optic neuropathy, or isolated dystonia to combined severe disease.
- **Anticipation:** not established.
- **Germline mosaicism:** mtDNA heteroplasmy and the mitochondrial bottleneck are more relevant concepts than conventional nuclear germline mosaicism.
- **Consanguinity:** not a recognized risk because inheritance is maternal, not autosomal recessive.

### Epidemiology

No defensible prevalence, incidence, carrier-frequency, or sex ratio has been established specifically for LHOND. Cases and pedigrees have been reported in multiple ancestries, including Native American, Asian, and European families, arguing against restriction to one population. A founder m.14459G>A variant has been described in some Japanese families, but a global founder effect cannot be assumed.

## 10. Diagnostics

### Clinical evaluation

1. **Neuro-ophthalmology:** best-corrected acuity, color vision, pupils, automated perimetry, fundus photography, OCT retinal-nerve-fiber/ganglion-cell analysis, and visual evoked potentials as needed.
2. **Movement-disorder examination:** dystonia distribution/severity, gait, ataxia, pyramidal signs, speech and swallowing.
3. **MRI brain and orbits:** optic-nerve/chiasmal signal and atrophy; basal-ganglia lesions or striatal atrophy. Optic-pathway T2 hyperintensity does not exclude LHON: it occurred in **38%** of the small rare-mutation cohort. (cui2020clinicalfeaturesof pages 6-6)
4. **Laboratory assessment:** lactate, pyruvate, creatine kinase, metabolic panel and blood count may identify broader mitochondrial involvement but can be normal and are not diagnostic biomarkers.
5. **Cardiac/auditory assessment:** considered when broader LHON-plus symptoms or family history suggest multisystem disease.

### Genetic testing

- Begin with targeted testing for common LHON variants plus **MT-ND6 m.14459G>A** when dystonia/basal-ganglia disease accompanies optic neuropathy.
- If negative or atypical, perform **complete mtDNA sequencing with heteroplasmy quantification and deletion analysis**. Testing blood is convenient, but urine epithelial cells, buccal cells, or muscle may better detect low-level/tissue-variable heteroplasmy.
- A nuclear optic-neuropathy/mitochondrial panel, WES or WGS is appropriate when mtDNA testing is negative or the phenotype is atypical. WGS can assess nuclear genes and mtDNA, but laboratories differ in mtDNA coverage and heteroplasmy validation.
- CMA, karyotyping, FISH, and repeat-expansion tests have low first-line utility unless another diagnosis is suspected.

### Differential diagnosis

Important alternatives are conventional LHON; OPA1-related dominant optic atrophy/“DOA-plus”; **TIMM8A**-related Mohr–Tranebjærg syndrome; WFS1 disease; OPA3/Costeff syndrome; ATP1A3 disease; mitochondrial Leigh/Leigh-like syndromes; Wilson disease; NBIA; dopa-responsive dystonia; multiple sclerosis/NMOSD/MOGAD; toxic-nutritional optic neuropathy; and compressive or inflammatory optic neuropathy. Early deafness plus X-linked inheritance favors TIMM8A disease, whereas maternal transmission plus an MT-ND6 variant favors LHOND.

There are no validated population or newborn-screening programs. **Maternal-family cascade testing** is appropriate after genetic counseling.

## 11. Outcome and prognosis

No subtype-specific survival curves, mortality rates, or life-expectancy estimates exist. The major burden is neurological disability rather than a demonstrated uniform reduction in survival. Visual loss is often severe and chronic; in the broader rare-mutation cohort, 75% of eyes reached ≤20/200 at their worst point. (cui2020clinicalfeaturesof pages 6-6)

Prognosis is heterogeneous and depends on visual severity, dystonia distribution, bulbar involvement, mobility, broader encephalopathy, mutant load, and environmental exposures. Neither a validated prognostic score nor a molecular biomarker exists for m.14459G>A LHOND. Complications include blindness, falls, contractures, pain, dysphagia/aspiration, loss of independence, anxiety and depression.

## 12. Treatment

### Current strategy

There is **no approved treatment specifically for m.14459G>A LHOND**, and no controlled subtype-specific therapeutic trial was identified.

- **Optic neuropathy:** early referral to a mitochondrial neuro-ophthalmology service; consider **idebenone** according to regional LHON authorization and specialist judgment. Evidence and approvals concern LHON broadly, especially common variants, not proven neurological benefit in m.14459G>A dystonia.
- **Dystonia:** individualized oral therapy such as anticholinergic agents, baclofen, clonazepam, or other standard dystonia medicines; levodopa trial when dopa-responsive dystonia remains plausible; botulinum toxin for focal/segmental dystonia. Evidence is symptomatic and extrapolated.
- **Severe medication-refractory dystonia:** globus-pallidus-internus deep-brain stimulation may be considered case by case, but no robust LHOND response rate is available.
- **Rehabilitation:** low-vision services, orientation/mobility training, assistive technology, physical and occupational therapy, speech/swallowing therapy, nutrition, contracture prevention, and psychosocial support.

Suggested NCIt intervention concepts include genetic counseling, physical therapy, occupational therapy, speech therapy, low-vision rehabilitation, botulinum toxin therapy, and deep-brain stimulation; exact NCIt codes should be validated against the current release before database ingestion.

### Experimental landscape

Current LHON trials overwhelmingly target **MT-ND4 m.11778G>A**, not MT-ND6 m.14459G>A. Registry examples include NCT07406854 (phase 3; 95 participants), NCT05293626 (phase 1/2; 12), NCT03406104 (phase 3 follow-up; 62), NCT03293524 (phase 3; 98), NCT03153293 (phase 2/3; 159), NCT02064569 (phase 1/2; 19), and NCT01267422 (9). An ND1 gene-therapy trial, NCT05820152, was terminated after enrolling 11. None establishes efficacy for LHOND. Mitochondrial base editing, heteroplasmy shifting, allotopic expression, and iPSC-derived retinal-ganglion-cell replacement remain investigational. (OpenTargets Search: Leber optic atrophy and dystonia)

## 13. Prevention

- **Primary prevention in carriers:** avoid smoking, heavy alcohol use and avoidable mitochondrial toxins; maintain general health. Evidence is stronger for LHON overall than for LHOND. (berardo2020leberhereditaryoptic pages 1-3)
- **Secondary prevention:** educate maternal relatives about early dyschromatopsia, central blur, involuntary posturing, gait change, and the need for urgent specialist review. Baseline and periodic ophthalmic/neurological examination may be reasonable, although no validated surveillance interval exists.
- **Tertiary prevention:** early low-vision rehabilitation, dystonia treatment, fall/contracture prevention, swallowing assessment and mental-health support.
- **Reproductive counseling:** discuss maternal transmission, heteroplasmy/bottleneck uncertainty, prenatal diagnosis, preimplantation genetic testing where technically appropriate, donor oocytes, adoption, and—where legal and available—mitochondrial-donation approaches. Prediction of phenotype from prenatal mutant load may remain uncertain.

Vaccination, antimicrobial prophylaxis, and infectious-disease public-health measures are not disease-specific interventions.

## 14. Other species and natural disease

No well-validated, naturally occurring veterinary equivalent of human m.14459G>A LHOND was identified. The orthologous mitochondrial ND6 gene is evolutionarily conserved across vertebrates, but naturally occurring optic-atrophy-plus-dystonia disease in a defined animal breed has not been established. There is no zoonotic potential or cross-species transmission because this is an inherited mitochondrial disorder.

## 15. Model organisms and experimental systems

The strongest disease-specific model is the **transmitochondrial cybrid**: patient mitochondria carrying m.14459G>A are placed into a standardized nuclear background. This assigned the respiratory complex-I defect to mutant mtDNA and is particularly valuable for separating mtDNA effects from nuclear modifiers. (yuwaiman2009inheritedmitochondrialoptic pages 10-10)

Other useful but predominantly general-LHON systems include patient fibroblasts, iPSCs, iPSC-derived retinal ganglion cells, retinal organoids, and engineered cells or animals carrying related complex-I mutations. These permit study of bioenergetics, ROS, apoptosis, heteroplasmy manipulation, neuroprotection and gene delivery. Their limitations are incomplete recapitulation of the human papillomacular bundle, mtDNA segregation, maternal-pedigree modifiers, and combined optic/basal-ganglia disease. No robust m.14459G>A animal model reproducing both human optic neuropathy and dystonia was verified.

## Current understanding and evidence gaps

The best-supported model is that **MT-ND6 m.14459G>A → complex-I dysfunction → deficient energetic reserve/redox stress → selective retinal-ganglion-cell and striatal neuronal injury → optic neuropathy plus dystonia**. The cybrid evidence supports causality, but clinical prediction remains poor because homoplasmic relatives can differ dramatically. (yuwaiman2009inheritedmitochondrialoptic pages 10-10)

Priority research needs are an international genotype-defined registry; prospective OCT, MRI and movement-disorder natural history; tissue-level heteroplasmy studies; patient-derived striatal and retinal neuronal models; biomarkers of conversion; and trials that enroll rare non-ND4 LHON genotypes. Recent diagnostic work has improved broad hereditary-optic-neuropathy testing, but 2023–2024 therapeutic development remains concentrated on common LHON variants rather than LHOND.

## Key references and supporting abstract language

- **Jun et al., 1996**, *Molecular and Cellular Biology*, DOI: https://doi.org/10.1128/MCB.16.3.771. The title itself states that transmitochondrial cybrids “assign a complex I defect” to the ND6 nucleotide-14459 mutation causing LHON and dystonia; this is the pivotal functional study summarized in the retrieved review. (yuwaiman2009inheritedmitochondrialoptic pages 10-10)
- **Yu-Wai-Man et al., 2009**, *Journal of Medical Genetics*, published March 2009, DOI: https://doi.org/10.1136/jmg.2007.054270. Abstract: “Additional genetic and environmental factors modulate the penetrance of LHON,” and “The selective vulnerability of retinal ganglion cells (RGCs) is a key pathological feature.” (yuwaiman2009inheritedmitochondrialoptic pages 10-10)
- **Cui et al., 2020**, *Journal of Neuro-Ophthalmology*, published March 2020, DOI: https://doi.org/10.1097/WNO.0000000000000799. Abstract: “Patients with LHON and rare primary mutations have diverse clinical phenotypes,” and optic-nerve MRI signal “should not exclude LHON as the potential cause for optic neuropathy.” (cui2020clinicalfeaturesof pages 6-6)
- **Berardo et al., 2020**, *Journal of Neurology*, DOI: https://doi.org/10.1007/s00415-019-09619-z. This case expands the LHON-plus spectrum through combined MT-ND4/MT-ND6 mutations and illustrates that optic neuropathy with dystonia is genetically heterogeneous. (berardo2020leberhereditaryoptic pages 1-3)
- **Rocatcher et al., 2023**, *Brain*, DOI: https://doi.org/10.1093/brain/awac395. Abstract: “The positive diagnosis rate in individuals referred for Leber hereditary optic neuropathy testing was 18%,” with 92% of diagnosed cases carrying one of the three common mtDNA variants.

**Evidence-quality note:** primary functional evidence is strong for m.14459G>A causing complex-I dysfunction, but almost every clinical-domain estimate is limited by very small samples. General-LHON management, environmental, and trial findings have therefore been explicitly labeled as extrapolations rather than subtype-specific facts.

References

1. (OpenTargets Search: Leber optic atrophy and dystonia): Open Targets Query (Leber optic atrophy and dystonia, 34 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (yuwaiman2009inheritedmitochondrialoptic pages 10-10): P Yu-Wai-Man, P G Griffiths, G Hudson, and P F Chinnery. Inherited mitochondrial optic neuropathies. Journal of Medical Genetics, 46:145-158, Nov 2009. URL: https://doi.org/10.1136/jmg.2007.054270, doi:10.1136/jmg.2007.054270. This article has 568 citations and is from a domain leading peer-reviewed journal.

3. (cui2020clinicalfeaturesof pages 6-6): Shilei Cui, Ling Yang, Hanqiu Jiang, Jingting Peng, Jun Shang, Jiawei Wang, and Xiaojun Zhang. Clinical features of chinese sporadic leber hereditary optic neuropathy caused by rare primary mtdna mutations. Journal of Neuro-Ophthalmology, 40:30-36, Mar 2020. URL: https://doi.org/10.1097/wno.0000000000000799, doi:10.1097/wno.0000000000000799. This article has 24 citations and is from a peer-reviewed journal.

4. (berardo2020leberhereditaryoptic pages 1-3): Andres Berardo, Valentina Emmanuele, Wendy Vargas, Kurenai Tanji, Ali Naini, and Michio Hirano. Leber hereditary optic neuropathy plus dystonia, and transverse myelitis due to double mutations in mt-nd4 and mt-nd6. Journal of Neurology, 267:823-829, Nov 2020. URL: https://doi.org/10.1007/s00415-019-09619-z, doi:10.1007/s00415-019-09619-z. This article has 30 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Leber_Optic_Atrophy_and_Dystonia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.
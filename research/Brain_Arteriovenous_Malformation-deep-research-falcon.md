---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T22:55:52.476606'
end_time: '2026-08-19T23:06:12.762912'
duration_seconds: 620.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Brain arteriovenous malformation
  mondo_id: ''
  category: Vascular Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
reference_validation:
  total_references: 13
  verified: 12
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Brain_Arteriovenous_Malformation-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brain arteriovenous malformation
- **MONDO ID:**  (if available)
- **Category:** Vascular Disease

## Research Objectives

Please provide a comprehensive research report on **Brain arteriovenous malformation** covering all of the
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
- **Disease Name:** Brain arteriovenous malformation
- **MONDO ID:**  (if available)
- **Category:** Vascular Disease

## Research Objectives

Please provide a comprehensive research report on **Brain arteriovenous malformation** covering all of the
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


# Brain arteriovenous malformation: disease-characteristics report

**Scope.** This report summarizes disease-level evidence rather than individual EHR records. Evidence is labeled as human clinical, human tissue/omics, animal, or expert synthesis. PMID values are supplied where available in the retrieved evidence; DOI links are used otherwise. Most recent evidence was prioritized, but landmark older studies remain necessary for natural history and randomized treatment evidence.

## Executive summary

Brain arteriovenous malformation (bAVM) is a rare, high-flow cerebrovascular lesion in which a vascular nidus connects arteries directly to veins without an intervening capillary bed. The shunt exposes veins to arterial pressure and creates risks of intracranial hemorrhage, seizures, focal deficits, headache, and death or disability. Modern evidence no longer supports a purely static congenital-lesion model: most bAVMs are sporadic, endothelial mosaic disorders commonly involving activating **KRAS–RAF–MEK–ERK** signaling, with ongoing angiogenesis, mural-cell instability, inflammation, and vascular remodeling. Familial disease is uncommon and is principally associated with hereditary hemorrhagic telangiectasia (HHT) or capillary-malformation–AVM syndromes. (prado2019recentadvancesin pages 1-3, chen2023developmentandvalidation pages 1-2, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

No medication is proven to eradicate sporadic bAVM. Current care combines observation and symptom treatment with microsurgical resection, endovascular embolization, stereotactic radiosurgery (SRS), or multimodal therapy. Selection should be individualized by a multidisciplinary cerebrovascular team because the delayed natural-history risk must be balanced against immediate procedural risk. ARUBA found better approximately four-year outcomes with medical management than intervention for trial-eligible unruptured AVMs, but longer-term and lesion-specific uncertainty remains; TOBAS is designed to address that uncertainty. (mohr2020medicalmanagementwith pages 1-2, NCT02098252 chunk 1)

| Domain | Core fact | Suggested ontology terms/IDs | Evidence type |
|---|---|---|---|
| Definition/identifiers | Brain arteriovenous malformation (brain AVM, bAVM) is a high-flow vascular malformation with direct artery-to-vein shunting and no intervening capillary bed; MONDO and OMIM identifiers are available. (OpenTargets Search: brain arteriovenous malformation, chen2023developmentandvalidation pages 1-2, saito2024crisprcasrxsuppresseskrasinduced pages 1-2) | MONDO:0007154; OMIM:108010; MeSH: Arteriovenous Malformations | Aggregated disease ontology + human clinical |
| Synonyms | Common names include brain AVM, cerebral arteriovenous malformation, intracranial arteriovenous malformation, bAVM. (prado2019recentadvancesin pages 1-3, NCT02098252 chunk 1) | Labels only | Aggregated disease-level resources + human clinical |
| Epidemiology | bAVM is uncommon; symptomatic discovery incidence is about 1.1 per 100,000 population, and prevalence estimates around 10 per 100,000 are cited in reviews. (NCT02098252 chunk 1, saito2024crisprcasrxsuppresseskrasinduced pages 1-2) | Label only: rare vascular disease | Human clinical/epidemiology |
| Major phenotype | Intracranial hemorrhage is a major presentation and complication; natural-history rupture risk is commonly estimated around 1%–4% per year depending on cohort and lesion features. (rutledge2014hemorrhageratesand pages 4-6, chen2023developmentandvalidation pages 1-2, NCT02098252 chunk 1) | HPO: HP:0002170 intracranial hemorrhage | Human clinical |
| Major phenotype | Seizures are a common presenting manifestation. (prado2019recentadvancesin pages 1-3, NCT02098252 chunk 1) | HPO: HP:0001250 seizures | Human clinical |
| Major phenotype | Headache is a recognized presenting symptom. (NCT02098252 chunk 1) | HPO: HP:0002315 headache | Human clinical |
| Major phenotype | Focal neurologic deficit can occur at presentation or after hemorrhage/treatment. (prado2019recentadvancesin pages 1-3, NCT02098252 chunk 1) | HPO label: focal neurologic deficit | Human clinical |
| Anatomy | Primary affected structure is the brain vasculature, with a nidus connecting cerebral arteries and veins. (chen2023developmentandvalidation pages 1-2, saito2024crisprcasrxsuppresseskrasinduced pages 1-2) | UBERON:0000955 brain; UBERON label: cerebral blood vessel | Human clinical + human tissue |
| Key cell type | Endothelial cells are the principal disease-driving cell type in both sporadic and familial forms. (saito2024crisprcasrxsuppresseskrasinduced pages 1-2, winkler2022asinglecellatlas pages 1-3, walchli2024singlecellatlasof pages 1-2) | CL:0000115 endothelial cell | Human tissue/omics + animal model |
| Key cell type | Pericytes participate in neurovascular-unit dysfunction and vessel instability. (winkler2022asinglecellatlas pages 1-3, walchli2024singlecellatlasof pages 1-2) | CL:0000669 pericyte | Human tissue/omics |
| Key cell type | Vascular smooth muscle cells/mural cells contribute to vessel maturation failure and hemorrhagic vulnerability. (pan2021theroleof pages 5-6, scimone2024methylomeanalysisof pages 1-2) | Cell label: vascular smooth muscle cell | Human tissue + review |
| Key cell type | Monocyte/macrophage infiltration is part of the inflammatory lesion microenvironment and may contribute to rupture biology. (winkler2022asinglecellatlas pages 1-3, hauer2020rnasequencinghighlightsinflammation pages 1-2) | Cell label: monocyte/macrophage | Human tissue/omics |
| Mechanism | Pathologic angiogenesis and loss of vascular quiescence are central features. (hauer2020rnasequencinghighlightsinflammation pages 1-2, winkler2022asinglecellatlas pages 1-3) | GO:0001525 angiogenesis | Human tissue/omics |
| Mechanism | Somatic RAS/MAPK activation is a key upstream driver in sporadic bAVM. (saito2024crisprcasrxsuppresseskrasinduced pages 1-2, tu2024somaticbrafv600emutation pages 1-6) | GO:0000165 MAPK cascade | Human tissue genetics + animal model |
| Mechanism | Inflammatory signaling and immune-cell cross-talk are enriched in lesional tissue. (winkler2022asinglecellatlas pages 1-3, hauer2020rnasequencinghighlightsinflammation pages 1-2) | GO:0006954 inflammatory response | Human tissue/omics |
| Mechanism | Endothelial migration/cytoskeletal remodeling is dysregulated in bAVM tissue. (hauer2020rnasequencinghighlightsinflammation pages 1-2) | GO label: endothelial cell migration | Human bulk RNA-seq |
| Mechanism | Abnormal arteriovenous specification/differentiation is a recurrent theme across transcriptomic and developmental studies. (walchli2024singlecellatlasof pages 1-2, scimone2024methylomeanalysisof pages 1-2) | GO label: arteriovenous specification | Human tissue/omics |
| Somatic genes | Sporadic bAVMs frequently harbor activating somatic mutations in KRAS; BRAF is also implicated. (saito2024crisprcasrxsuppresseskrasinduced pages 1-2, tu2024somaticbrafv600emutation pages 1-6, prado2019recentadvancesin pages 1-3) | HGNC labels: KRAS; BRAF | Human lesion genetics + animal model |
| Germline genes | Familial/syndromic AVM predisposition includes HHT genes ENG, ACVRL1, SMAD4, GDF2 and CM-AVM genes RASA1, EPHB4. (saito2024crisprcasrxsuppresseskrasinduced pages 1-2, prado2019recentadvancesin pages 1-3, OpenTargets Search: brain arteriovenous malformation) | HGNC labels: ENG; ACVRL1; SMAD4; GDF2; RASA1; EPHB4 | Human inherited disease genetics |
| Epigenetics | Endothelial-cell methylome studies implicate differential methylation in KRAS, RBPJ, EPHB1 and pathways involving EC–VSMC crosstalk. (scimone2024methylomeanalysisof pages 1-2) | Label only: DNA methylation | Human tissue/epigenomics |
| Transcriptomics | Bulk RNA-seq of resected bAVMs showed 736 upregulated and 498 downregulated genes, highlighting inflammation, cytoskeletal remodeling, reduced ECM integrity, angiopoietin-TIE, and TGF-β signaling changes. (hauer2020rnasequencinghighlightsinflammation pages 1-2) | GO labels: extracellular matrix organization; cell migration | Human bulk RNA-seq |
| Single-cell profiling | Single-cell atlases identified abnormal endothelial states, altered arteriovenous zonation, immune crosstalk, and atypical endothelial MHC class II upregulation in brain vascular malformations. (winkler2022asinglecellatlas pages 1-3, walchli2024singlecellatlasof pages 1-2) | CL:0000115 endothelial cell; GO label: antigen presentation | Human single-cell RNA-seq |
| Diagnostics | Digital subtraction angiography remains the reference standard for diagnosis and angioarchitectural characterization. (chauvet2024diagnosticaccuracyof pages 1-2, chen2023developmentandvalidation pages 2-3) | Procedure label: digital subtraction angiography | Human clinical imaging |
| Diagnostics | MRI/MRA are widely used; 2024 data support non-contrast 4D MRA for follow-up/characterization with accuracy comparable to contrast-enhanced 4D MRA in one retrospective cohort. (chauvet2024diagnosticaccuracyof pages 1-2, chauvet2024diagnosticaccuracyof pages 2-5) | Procedure labels: MRI; MRA | Human clinical imaging |
| Prognostic tools | Imaging-based hemorrhage stratification includes the VALE score: ventricular system involvement, venous aneurysm, deep location, exclusively deep drainage. (chen2023developmentandvalidation pages 1-2) | Labels only: ventricular involvement; venous aneurysm; deep drainage | Human clinical prognostic model |
| Interventions | Standard interventions include microsurgical resection, endovascular embolization, stereotactic radiosurgery, or multimodality therapy; conservative management remains important for selected unruptured lesions. (NCT02098252 chunk 1, mohr2020medicalmanagementwith pages 1-2, NCT04572568 chunk 1) | NCIT labels: surgical resection; embolization; stereotactic radiosurgery; conservative management | Human clinical + registry/trial |
| Current trials/implementation | Ongoing real-world and interventional studies include TOBAS (NCT02098252), MATCH registry (NCT04572568), and a liquid embolic agent randomized trial (PARTNER; NCT07314047). (NCT02098252 chunk 1, NCT04572568 chunk 1, NCT07314047 chunk 1) | ClinicalTrials.gov: NCT02098252; NCT04572568; NCT07314047 | Clinical trials/registry |
| Experimental therapeutics | Preclinical targeted approaches include MEK/ERK-pathway inhibition, BRAF inhibition, and CRISPR/CasRx knockdown of mutant KRAS in endothelial-driven mouse models. (saito2024crisprcasrxsuppresseskrasinduced pages 2-4, tu2024somaticbrafv600emutation pages 1-6, saito2024crisprcasrxsuppresseskrasinduced pages 1-2) | Intervention labels: MEK inhibitor; BRAF inhibitor; CRISPR/CasRx | Animal model/preclinical |
| Prevention/screening | No established primary prevention exists for sporadic bAVM; secondary prevention is focused on risk stratification, imaging surveillance, and genetic/syndromic evaluation when HHT or CM-AVM is suspected. (NCT02098252 chunk 1, prado2019recentadvancesin pages 1-3, saito2024crisprcasrxsuppresseskrasinduced pages 1-2) | Label only: genetic counseling; surveillance imaging | Human clinical + inherited disease context |


*Table: This table condenses ontology-ready facts for brain arteriovenous malformation, spanning identifiers, phenotypes, cells, mechanisms, diagnostics, and interventions. It is designed to support direct knowledge-base population while keeping uncertain ontology IDs as labels only.*

## 1. Disease information

### Definition and identifiers

A bAVM is a tangle of abnormally dilated cerebral vessels with direct arteriovenous shunting, high flow, low resistance, and no normal capillary interface. The central tangle is the **nidus**; feeding arteries, the nidus, and draining veins form the lesion’s angioarchitecture. (chen2023developmentandvalidation pages 2-3, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

* **MONDO:** MONDO:0007154, *arteriovenous malformations of the brain*.
* **OMIM:** 108010, *Arteriovenous malformations of brain*.
* **MeSH:** the broad indexed concept is *Arteriovenous Malformations*; “brain/cerebral AVM” supplies anatomical qualification.
* **ICD:** coding varies by jurisdiction and whether congenital status, rupture, or hemorrhage is being represented. ICD-10-CM commonly uses **Q28.2** for arteriovenous malformation of cerebral vessels; associated intracranial hemorrhage should be coded separately. ICD-11 mapping should be verified against the deployment’s current browser/version rather than inferred from ICD-10.
* **Synonyms:** brain AVM, bAVM, cerebral AVM, cerebral arteriovenous malformation, intracranial AVM, pial AVM. “Dural arteriovenous fistula,” “cavernous malformation,” and “vein of Galen malformation” are distinct entities and should not be merged.

Open Targets identifies **ENG** as a disease-associated target for MONDO:0007154 and separately links ENG and ACVRL1 to HHT1 and HHT2, respectively. (OpenTargets Search: brain arteriovenous malformation)

## 2. Etiology, risk factors, protective factors, and gene–environment interaction

### Causal architecture

**Sporadic bAVM (>95%).** The strongest current model is a postzygotic, endothelial mosaic activating variant—most often **KRAS**, less often **BRAF** or another RAS/MAPK component—arising in a permissive vascular-development or remodeling context. The mutant clone perturbs endothelial proliferation, identity, migration, and interaction with mural and immune cells. Reported somatic-variant detection varies substantially, approximately 28%–87%, because tissue sampling, endothelial enrichment, sequencing depth, and variant allele fraction differ. (prado2019recentadvancesin pages 1-3, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

**Familial/syndromic bAVM (<5%).** The major predisposition is HHT, an autosomal-dominant disorder caused mainly by loss-of-function variants in **ENG** or **ACVRL1**, and less often **SMAD4** or **GDF2**. CM-AVM syndromes involve **RASA1** or **EPHB4**. HHT-related endothelial BMP9/10–ENG–ACVRL1–SMAD1/5/8 insufficiency interacts with angiogenic and hemodynamic cues; a local “second hit” or mosaic event may help determine where a lesion forms. (prado2019recentadvancesin pages 1-3, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

### Risk factors

Established or repeatedly supported **hemorrhage-risk** factors include previous hemorrhage—the most reproducible predictor—deep location, exclusively deep venous drainage, ventricular-system involvement, and venous aneurysm. Silent microhemorrhage and tissue hemosiderin have also been associated with subsequent hemorrhage. The 2023 VALE model formalized ventricular involvement, venous aneurysm, deep location, and exclusively deep drainage. (rutledge2014hemorrhageratesand pages 4-6, chen2023developmentandvalidation pages 1-2)

Candidate modifiers include inflammatory polymorphisms in **IL6** and **TNF**, **APOE ε2**, and EPHB4 variants, but these associations require independent replication before clinical genetic prediction. Reported effect estimates include OR 2.4 for IL6 −174G>C, HR 4.0 for TNF −238G>A, and HR 5.1 for APOE ε2. (rutledge2014hemorrhageratesand pages 4-6)

Age is not a simple causal exposure: lesions can exist from development, form or enlarge postnatally, and present at any age, but symptomatic diagnosis is concentrated in children and young-to-middle-aged adults. Sex differences are inconsistent across cohorts; a large Chinese series was 58.3% male, but that should not be treated as a universal biological ratio. (chen2023developmentandvalidation pages 1-2, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

### Environmental/lifestyle factors and protection

No toxin, pollutant, diet, infection, occupation, smoking pattern, alcohol exposure, or exercise level is established as a primary cause of sporadic bAVM. Pregnancy-related hemodynamic and hormonal effects remain clinically debated rather than proven causes of lesion formation. Hypertension may worsen consequences of hemorrhage and is treated as part of general vascular care, but it is not an established origin of the malformation.

No validated genetic protective allele or lifestyle intervention prevents bAVM formation. Practical “protective” management therefore means blood-pressure control, avoidance of illicit sympathomimetics, appropriate seizure treatment, and individualized avoidance of activities or medications judged to create unacceptable bleeding consequences—not proven lesion-prevention strategies.

### Gene–environment interaction

The best-supported interaction is **gene × angiogenic/hemodynamic context**: endothelial RAS/MAPK activation or HHT-pathway loss alters responses to VEGF, shear stress, flow direction, and vessel injury. High-flow shunting then becomes a feed-forward stimulus for remodeling, venous hypertension, inflammation, and wall failure. Direct human evidence for conventional environmental G×E interactions is limited.

## 3. Phenotypes

* **Intracranial hemorrhage—HP:0002170.** Usually acute and potentially severe; it may be intraparenchymal, intraventricular, or subarachnoid. More than half of symptomatic historical cohorts presented with hemorrhage, although incidentally detected lesions are increasing. First-hemorrhage mortality has been reported at 10%–30%; approximately 10%–20% of survivors may have long-term disability, with estimates dependent on cohort and era. (NCT02098252 chunk 1)
* **Seizures—HP:0001250.** Episodic and variable in severity; approximately 20%–25% present with seizures. Some respond to antiseizure medication, whereas others become drug resistant. Seizure restrictions affect driving, education, employment, and independence. (NCT02098252 chunk 1)
* **Headache—HP:0002315.** Episodic or chronic, often nonspecific; phenotype frequency and causal attribution vary. Sudden severe headache requires emergency assessment for hemorrhage.
* **Focal neurologic deficit.** Weakness, sensory loss, aphasia, visual-field deficit, ataxia, or cranial-nerve dysfunction may reflect hemorrhage, venous congestion, ischemic steal, mass effect, seizure/postictal change, or treatment injury. Suggested HPO concepts include hemiparesis (HP:0001269), aphasia (HP:0002381), visual-field defect, ataxia (HP:0001251), and cognitive impairment (HP:0100543), selected according to the actual manifestation.
* **Incidental/asymptomatic lesion.** Increasingly identified by MRI performed for another reason; not equivalent to biologically inactive disease.
* **Pediatric presentation.** bAVM is the dominant vascular cause of spontaneous pediatric intracranial hemorrhage: one meta-analysis found AVMs constituted 68.3% of detailed vascular causes; another systematic review found 1,226 AVMs, 70.99% of reported vascular causes. These are proportions among hemorrhagic pediatric cohorts, not population prevalence. 

Quality-of-life loss is driven by fear of rupture, headache and epilepsy, neurologic disability, treatment recovery, and uncertainty. Standard instruments include EQ-5D, SF-36, PROMIS, modified Rankin Scale (mRS), seizure-specific measures, and neuropsychological testing. High-quality phenotype-specific QOL percentages remain limited.

## 4. Genetic and molecular information

### Genes and variant classes

* **KRAS**: activating somatic missense variants, commonly codon 12 substitutions such as p.Gly12Val and p.Gly12Asp; constitutive GTP-bound signaling activates RAF–MEK–ERK and can also affect PI3K–AKT–mTOR. Lesional variant allele fractions are often low because the mutation is mosaic and endothelial restricted; population frequency is therefore not meaningfully represented by germline gnomAD frequency. (saito2024crisprcasrxsuppresseskrasinduced pages 1-2)
* **BRAF**: somatic activating variants, including p.Val600Glu, occur in a minority. Endothelial BrafV600E was sufficient to produce AVM-like lesions, hemorrhage, seizures, and motor deficits in mice. (tu2024somaticbrafv600emutation pages 1-6)
* **ENG, ACVRL1, SMAD4, GDF2**: heterozygous germline loss-of-function variants causing HHT-related predisposition; inheritance is autosomal dominant with age-dependent and variable expression.
* **RASA1, EPHB4**: heterozygous germline loss-of-function variants causing CM-AVM spectrum; EPHB4 is especially relevant to arterial–venous identity.
* Other proposed genes and susceptibility variants should be considered research-level unless supported by a recognizable syndrome and clinically curated variant evidence.

Variant interpretation must distinguish (1) germline constitutional testing from blood/saliva and (2) low-frequency somatic testing of resected or endovascularly sampled lesion material. A negative blood panel does not exclude a lesion-restricted driver. ACMG/AMP classification applies most directly to germline findings; somatic variants require disease-specific functional and mosaic evidence. No recurrent large chromosomal abnormality, repeat expansion, mitochondrial variant, or aneuploidy defines isolated bAVM.

### Modifier and epigenetic evidence

Human endothelial methylome analysis reported differential methylation of **RBPJ, KRAS, EPHB1**, adhesion/cytoskeletal loci, EC–vascular-smooth-muscle crosstalk genes, and long noncoding RNAs. The authors also implicated non-CpG CHG methylation in neurovascular-development pathways. This is discovery-level evidence from a small tissue study, not a validated diagnostic signature. (scimone2024methylomeanalysisof pages 1-2)

## 5. Environmental information

There is no established infectious agent and no zoonotic or transmissible mechanism. No environmental toxicant or radiation exposure has been established as causal. Radiation is a treatment modality, not a known cause of ordinary bAVM. Lifestyle exposures do not currently support causal annotation in CTD-like knowledge bases. General cerebrovascular risk reduction remains advisable because comorbidity can worsen treatment and hemorrhage outcomes.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** endothelial somatic RAS/MAPK activation, or germline BMP/TGF-β/RASA1–EPHB4 pathway insufficiency with local permissive events.
2. **Endothelial transformation:** ERK-driven proliferation and EndMT-like change, disturbed arterial–venous zonation, altered Notch/ephrin signaling, loss of BBB/CNS-specific properties, and abnormal response to flow.
3. **Malformed shunt:** capillary specification fails or regresses, producing direct arterial-to-venous channels and a nidus.
4. **Neurovascular-unit failure:** defective endothelial–pericyte–smooth-muscle crosstalk, reduced vessel maturation, extracellular-matrix disruption, and inadequate mural coverage.
5. **Feed-forward remodeling:** high flow and venous hypertension stimulate VEGF/angiogenesis, cytoskeletal remodeling, and inflammatory recruitment.
6. **Tissue injury:** fragile vessels leak or rupture; hemorrhage causes mechanical injury, edema, inflammation, ischemia, neuronal loss, seizures, and focal deficits.

### Human transcriptomic and single-cell evidence

Bulk RNA sequencing of 12 bAVMs versus 16 control intracranial arteries found **736 upregulated genes**, including cytoskeletal, migration, inflammatory-cytokine, neutrophil, and macrophage programs, and **498 downregulated genes**, including extracellular-matrix, angiopoietin–TIE, and TGF-β programs. Forty-seven GO terms were enriched, supporting inflammation, loss of vascular quiescence, and impaired wall integrity. (hauer2020rnasequencinghighlightsinflammation pages 1-2)

The 2022 human cerebrovascular atlas profiled **181,388 cells** and found loss of normal endothelial arteriovenous zonation, a nidus-associated angiogenic state, and vascular–immune crosstalk. Its abstract states: “We illustrated an interplay between vascular and immune cells contributory to brain hemorrhage.” GPNMB-positive monocytes were associated with depletion of stabilizing smooth-muscle cells in bAVMs that had bled. (winkler2022asinglecellatlas pages 1-3)

A larger 2024 Nature atlas analyzed **606,380 cells from 117 samples and 68 human fetuses/adult patients**. Diseased vasculature showed altered arteriovenous differentiation, reactivated fetal programs, loss of CNS-specific endothelial properties, MHC-class-II upregulation, and immune/angiogenic endothelial-to-perivascular signaling. These findings are shared across several vascular-dependent CNS diseases and are not all bAVM-specific. (walchli2024singlecellatlasof pages 1-2)

### Suggested mechanistic annotations

* **GO:** angiogenesis (GO:0001525), MAPK cascade (GO:0000165), inflammatory response (GO:0006954), endothelial-cell migration, extracellular-matrix organization, blood-vessel remodeling, regulation of vascular permeability, response to fluid shear stress, and endothelial-to-mesenchymal transition.
* **CL:** endothelial cell (CL:0000115), pericyte (CL:0000669), vascular smooth-muscle cell, perivascular fibroblast, monocyte, macrophage, neutrophil, astrocyte, neuron, and microglial cell.
* **Subcellular:** plasma membrane receptor complexes, cytosol and nucleus for MAPK signaling, adherens/tight junctions, actin cytoskeleton, extracellular matrix, and endoplasmic reticulum. No defining mitochondrial, lysosomal, or protein-aggregation defect is known.
* **Metabolism/proteomics/lipidomics:** inflammatory and hypoxic metabolic remodeling is plausible, but no clinically validated metabolomic, proteomic, or lipidomic signature exists.

## 7. Anatomical structures affected

The primary organ is the **brain** (UBERON:0000955), particularly cerebral arteries, arterioles, veins, and intervening parenchyma. Lesions may be cortical/lobar, deep (basal ganglia, thalamus, corpus callosum, insula), brainstem, or cerebellar; they may be superficial or deep and drain superficially, deeply, or both. Lateralization is usually unilateral/asymmetric, although multiple or bilateral lesions occur, especially in HHT. Secondary structures include ventricles and subarachnoid spaces when hemorrhage extends, and remote cortex involved in epileptic networks.

At tissue level, affected components are vascular endothelium, basement membrane/extracellular matrix, pericytes, smooth muscle, perivascular fibroblasts, and adjacent neural/glial tissue. The defining subcellular systems are endothelial junctions, cytoskeleton, receptor signaling complexes, and transcriptional machinery.

## 8. Temporal development

The lesion may originate during vascular development, but de novo postnatal formation and interval growth are documented; therefore “congenital” should not be interpreted as invariably complete and static at birth. Presentation may occur from infancy through old age, most often before age 40 in symptomatic cohorts. (NCT02098252 chunk 1, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

Clinical onset is frequently **acute** with hemorrhage or seizure; incidental detection is asymptomatic/insidious. Untreated disease is chronic and lifelong, with a persistent annual hemorrhage hazard commonly estimated around **1%–3%** for unruptured lesions and **2%–4% overall**, modified substantially by prior rupture and angioarchitecture. Spontaneous complete obliteration is rare. SRS produces delayed involution over years, during which hemorrhage risk persists; surgery can provide immediate cure if complete, while embolization may be curative in selected anatomy or adjunctive/staged. (rutledge2014hemorrhageratesand pages 4-6, chen2023developmentandvalidation pages 2-3, NCT02098252 chunk 1)

Critical windows include acute hematoma management, post-hemorrhage stabilization and angiographic reassessment, the latency interval after SRS, and long-term surveillance after apparent cure—especially in children, where recurrence is more concerning.

## 9. Inheritance and population epidemiology

Population prevalence is approximately **10 per 100,000** in a recent mechanistic review; an older synthesis cited 0.05%, illustrating methodological variability. Symptomatic discovery incidence is approximately **1.1 per 100,000 person-years**. bAVMs cause roughly 1%–2% of all strokes but a disproportionate fraction of hemorrhagic stroke in children and younger adults. (prado2019recentadvancesin pages 1-3, NCT02098252 chunk 1, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

Most isolated cases are non-Mendelian, lesion-restricted mosaics and have low sibling/offspring recurrence risk. HHT and CM-AVM are autosomal dominant, with incomplete/age-dependent penetrance and variable expressivity. HHT prevalence is approximately 1 in 5,000; one review reported brain AVM in 13.4% of HHT1 versus 2.4% of HHT2. Genetic anticipation, repeat expansion, consanguinity effects, and a defined carrier frequency are not features of sporadic bAVM. Founder variants exist in some HHT populations but are syndrome- and ancestry-specific. (prado2019recentadvancesin pages 1-3)

No consistent high-risk ethnicity or endemic region is established after accounting for ascertainment. The median age in the 3,962-patient Chinese VALE cohort was 26.1 years and 58.3% were male, but external demographic generalization requires caution. (chen2023developmentandvalidation pages 1-2)

## 10. Diagnostics

### Clinical and imaging work-up

Acute suspected hemorrhage is assessed with noncontrast CT, often followed by CT angiography. MRI characterizes nidus location, prior hemorrhage, hemosiderin, edema, eloquent structures, and associated parenchymal injury; MRA evaluates flow noninvasively. **Catheter digital-subtraction angiography (DSA)** remains the reference standard for feeding arteries, nidus, high-flow fistulas, associated aneurysms, venous drainage, stenosis, and treatment planning. (chauvet2024diagnosticaccuracyof pages 2-5, chauvet2024diagnosticaccuracyof pages 1-2)

In a retrospective 2024 study of 54 MRA pairs from 43 patients, noncontrast 4D-MRA had accuracy **0.85** and specificity **95%**, versus 0.83 and 85% for contrast-enhanced 4D-MRA, with DSA as reference. The authors concluded that noncontrast 4D-MRA may support repeated follow-up while avoiding gadolinium, but prospective validation is required. Publication: 31 July 2024; DOI: https://doi.org/10.3390/diagnostics14151656. (chauvet2024diagnosticaccuracyof pages 2-5, chauvet2024diagnosticaccuracyof pages 1-2)

EEG is used for seizure classification, not AVM diagnosis. Routine blood/urine chemistry has no diagnostic signature. Histology shows malformed arterialized and venous vessels with variable wall thickness, gliosis, hemosiderin, inflammation, and absent normal capillary organization, but biopsy solely for diagnosis is generally inappropriate because of bleeding risk.

### Classification and differential diagnosis

Spetzler–Martin grade uses nidus size, eloquence, and deep venous drainage to estimate surgical risk; supplementary surgical, radiosurgical, and embolization scales may be added. Differential diagnoses include dural AV fistula, developmental venous anomaly, cavernous malformation, capillary telangiectasia, aneurysm, moyamoya-associated collaterals, hemorrhagic tumor, and vein of Galen malformation.

### Genetic testing

Routine germline testing is not indicated for every solitary sporadic bAVM. Test when there are multiple AVMs, mucocutaneous telangiectases, recurrent epistaxis, pulmonary/hepatic AVMs, capillary malformations, limb overgrowth, or family history. A panel should include **ENG, ACVRL1, SMAD4, GDF2, RASA1, and EPHB4**, with deletion/duplication analysis. WES/WGS can be used for unresolved syndromic cases. CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing have no routine role.

Somatic testing requires affected tissue or validated endovascular sampling with deep sequencing/digital PCR for low-VAF **KRAS/BRAF/MAP2K1**-pathway variants. It is currently research-oriented and may become relevant for targeted therapy. Blood-based “liquid biopsy,” RNA-seq, methylomics, proteomics, and metabolomics are not validated clinical diagnostics.

## 11. Outcome and prognosis

The major adverse outcome is rupture. Overall untreated hemorrhage risk is approximately 2%–4% annually and around 1%–3% for unruptured lesions; prior hemorrhage raises subsequent risk. (rutledge2014hemorrhageratesand pages 4-6, chen2023developmentandvalidation pages 2-3, NCT02098252 chunk 1)

The 2023 VALE study included **3,962 patients**. In 1,028 conservatively managed patients, 36 hemorrhages occurred over median 4.2 years. AUCs were 0.77 in derivation, 0.85 in external validation, and 0.73 in conservative validation. Ten-year hemorrhage-free survival was **95.5% low risk, 92.8% moderate risk, and 75.8% high risk**. This is promising but should be externally tested across health systems and ancestries. Publication: 1 March 2023; DOI: https://doi.org/10.1001/jamanetworkopen.2023.1070. (chen2023developmentandvalidation pages 1-2)

Functional outcome depends on rupture severity, initial neurologic status, lesion location, complete obliteration, treatment complications, seizures, and rehabilitation. There is no single meaningful five- or ten-year survival figure analogous to cancer survival. Morbidity includes epilepsy, motor/language/cognitive deficits, visual loss, chronic headache, anxiety, educational/employment disruption, and treatment-related stroke or radiation injury.

## 12. Treatment

### Strategy

Management should be decided by a multidisciplinary team including vascular neurosurgery, interventional neuroradiology, radiosurgery/radiation oncology, stroke neurology, epilepsy care, and rehabilitation. The goal of definitive treatment is complete shunt obliteration; partial treatment does not reliably remove lifetime hemorrhage risk.

* **Conservative/medical management:** observation with MRI/angiographic surveillance as appropriate; antihypertensives for comorbid hypertension; antiseizure drugs for epilepsy; headache treatment; and rehabilitation. There is no approved disease-modifying drug.
* **Microsurgical resection:** immediate cure when complete; favored for selected small, superficial, surgically accessible low-grade lesions, particularly after rupture or with an evacuable hematoma. Risks include hemorrhage, ischemia, focal deficit, infection, and death.
* **Endovascular embolization:** liquid embolic agents such as ethylene-vinyl alcohol copolymer (Onyx) or n-butyl cyanoacrylate are delivered through microcatheters. Uses include targeted treatment of aneurysms/high-flow fistulas, flow or volume reduction before surgery/SRS, and cure in selected compact lesions. Risks include hemorrhage, ischemic stroke, catheter complications, and incomplete occlusion.
* **SRS:** focused radiation for small/deep or surgically high-risk lesions. Obliteration is delayed, and radiation edema, necrosis, cyst formation, neurologic deficit, and latency-period hemorrhage can occur.
* **Multimodal therapy:** staged embolization plus resection or SRS is common for complex anatomy, but every added procedure adds risk.

Suggested NCIT labels are *Surgical Resection*, *Endovascular Embolization*, *Stereotactic Radiosurgery*, *Radiation Therapy*, *Anticonvulsant Therapy*, and *Rehabilitation Therapy*. Relevant chemicals include cyanoacrylate and ethylene-vinyl alcohol copolymer; CHEBI mapping should be performed against the exact product/compound.

### Randomized evidence and expert interpretation

ARUBA randomized 226 adults with unruptured, treatment-eligible AVMs. At mean 50-month follow-up, medical management remained superior to medical management plus intervention for stroke or death (**HR 0.31, 95% CI 0.17–0.56**). The investigators advise informing patients of the absolute and relative early risks of intervention, while explicitly noting that outcomes beyond five years remain uncertain. (mohr2020medicalmanagementwith pages 1-2)

This does not mean all unruptured bAVMs should never be treated. Expert criticism concerns selection, heterogeneous interventions, limited representation of optimal microsurgical candidates, and insufficient follow-up to capture lifetime hemorrhage prevention. The defensible conclusion is narrower: routine prophylactic intervention for every unruptured lesion is unsupported; treatment should be lesion-specific and, when uncertainty is material, trial-based.

### Trials and real-world implementation

* **TOBAS—NCT02098252:** recruiting randomized care trial and registry, target n=1,000. It compares conservative versus interventional management and nests randomization of embolization before surgery/SRS. The primary outcome is death or disabling stroke; planned follow-up extends to 2035–2036. https://clinicaltrials.gov/study/NCT02098252 (NCT02098252 chunk 1)
* **MATCH—NCT04572568:** recruiting Chinese multicenter prospective registry, n=2,000, with real-world multidisciplinary pathways and outcomes including mRS, obliteration, hemorrhage, complications, epilepsy, headache, and neurologic function. https://clinicaltrials.gov/study/NCT04572568 (NCT04572568 chunk 1)
* **PARTNER—NCT07314047:** randomized, open-label, noninferiority device trial, n=116, comparing a MicroPort liquid embolic agent with Onyx; primary endpoint is ≥50% target-AVM embolization. Registry posting occurred in 2026, so it is a current development rather than a 2023–2024 source. https://clinicaltrials.gov/study/NCT07314047 (NCT07314047 chunk 1)

### Experimental precision therapy

MEK/ERK inhibitors suppress mutant-KRAS endothelial phenotypes in vitro and reduce malformation burden in fish/mice, but toxicity, blood–brain delivery, mosaic target detection, treatment duration, and rebound remain unresolved. In 2024, endothelial **BrafV600E** mice improved neurologically with dabrafenib, and CRISPR/CasRx knockdown of mutant KRAS suppressed lesion development in another mouse model. Neither constitutes human efficacy evidence. (tu2024somaticbrafv600emutation pages 1-6, saito2024crisprcasrxsuppresseskrasinduced pages 2-4, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

No validated pharmacogenomic algorithm, gene therapy, cell therapy, RNA therapeutic, or immunotherapy is approved for bAVM.

## 13. Prevention

**Primary prevention:** none is established for sporadic mosaic bAVM; vaccination and antimicrobial prophylaxis are not applicable. In familial disease, genetic counseling can inform reproductive options, including prenatal or preimplantation testing for a known pathogenic germline variant, but this prevents transmission rather than treating an existing lesion.

**Secondary prevention:** no population screening is recommended because prevalence is low and intervention has nontrivial risk. Targeted screening is appropriate in HHT/CM-AVM families according to syndrome-specific guidance. Early imaging after suggestive neurologic symptoms and structured rupture-risk assessment are central.

**Tertiary prevention:** seizure control, blood-pressure management, definitive treatment when benefit exceeds risk, surveillance for residual/recurrent shunting, stroke rehabilitation, fall/driving counseling, and management of depression/anxiety. Antibiotic prophylaxis is not routinely indicated merely because a cerebral AVM exists.

## 14. Other species and natural disease

Naturally occurring intracranial AVMs are reported sporadically in dogs and other animals, but evidence is mainly isolated veterinary case reports; there is no well-established breed association, VBO term, carrier frequency, or comparable population natural history. The condition is noninfectious and nonzoonotic. Orthologous RAS/MAPK, ENG–ACVRL1–SMAD, RASA1–EPHB4, VEGF, Notch, and ephrin pathways are strongly conserved across vertebrates.

Relevant taxa are **Homo sapiens** (NCBI Taxon 9606), **Mus musculus** (10090), and **Danio rerio** (7955). Exact orthologous NCBI Gene IDs should be resolved programmatically from current NCBI/Alliance releases rather than inferred here.

## 15. Model organisms

### Mouse

Conditional endothelial **KrasG12D** models, using Cdh5-CreERT2 or brain-endothelium-directed AAV, reproduce dilated plexiform arteriovenous networks, high flow, hemorrhage, ERK activation, and endothelial proliferation. The 2024 JCI Insight model used AAV plus Cdh5-CreERT2, three-dimensional cleared-tissue imaging and scRNA-seq, and demonstrated suppression with mutant-selective CRISPR/CasRx. Exact abstract quote: “CRISPR/CasRx to knock down mutant KRAS expression … efficiently suppressed bAVM development.” Publication: 22 November 2024; DOI: https://doi.org/10.1172/jci.insight.179729. (saito2024crisprcasrxsuppresseskrasinduced pages 2-4, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

Endothelial **BrafV600E** mice developed MRI-visible lesions, brain hemorrhage, seizures, motor/balance deficits, and death; dabrafenib improved behavioral measures and neuronal preservation in small preclinical groups. DOI: https://doi.org/10.1007/s10456-024-09918-8. (tu2024somaticbrafv600emutation pages 1-6)

HHT models delete **Eng** or **Acvrl1** in endothelium, often combined with angiogenic stimulation or injury, and establish abnormal endothelial responses to VEGF and blood flow. Their limitation is that they model syndromic pathway loss rather than the common sporadic KRAS mosaic disease.

### Zebrafish and cellular systems

Zebrafish RAS/MAPK and HHT-pathway perturbations permit live vascular imaging, rapid developmental phenotyping, and drug screening; MEK inhibition can reduce abnormal vascular tangles. Their cerebrovascular anatomy and developmental timing differ from humans. Human bAVM endothelial cultures, iPSC-derived endothelium, organ-on-chip systems, and explants allow pathway and flow studies but do not reproduce full neurovascular-unit architecture or lifetime rupture.

Across models, key limitations are supraphysiologic or widespread recombination, severe early lethality, variant levels exceeding human mosaic VAFs, incomplete representation of lesion heterogeneity, and inability to model decades of human remodeling. Nevertheless, the 2024 studies provide strong causal evidence that endothelial RAS/MAPK activation is sufficient for AVM-like disease and establish tractable platforms for targeted-therapy testing. (tu2024somaticbrafv600emutation pages 1-6, saito2024crisprcasrxsuppresseskrasinduced pages 1-2)

## Evidence gaps and knowledge-base cautions

1. Somatic-driver prevalence depends heavily on lesional sampling and assay sensitivity; absence of a detected variant is not evidence of a non-genetic lesion.
2. No circulating, proteomic, metabolomic, lipidomic, or epigenetic biomarker is validated for diagnosis or rupture prediction.
3. Natural-history estimates are averages and should not replace lesion-specific assessment.
4. ARUBA supports conservative management over heterogeneous intervention in its enrolled unruptured population over approximately four years, not a universal lifetime prohibition against treatment.
5. Targeted RAS/MAPK and gene-editing treatments remain preclinical.
6. Several ontology mappings requested—particularly exact ICD-11, SNOMED, LOINC, NCIT, CL, and UBERON descendants—should be validated against the knowledge base’s licensed/current release before ingestion.

References

1. (prado2019recentadvancesin pages 1-3): Leandro Barbosa Do Prado, Chul Han, S. Paul Oh, and Hua Su. Recent advances in basic research for brain arteriovenous malformation. International Journal of Molecular Sciences, 20:5324, Oct 2019. URL: https://doi.org/10.3390/ijms20215324, doi:10.3390/ijms20215324. This article has 62 citations.

2. (chen2023developmentandvalidation pages 1-2): Yu Chen, Heze Han, Xiangyu Meng, Hengwei Jin, Dezhi Gao, Li Ma, Ruinan Li, Zhipeng Li, Debin Yan, Haibin Zhang, Kexin Yuan, Ke Wang, Yukun Zhang, Yang Zhao, Weitao Jin, Runting Li, Fa Lin, Xiaofeng Chao, Zhengfeng Lin, Qiang Hao, Hao Wang, Xun Ye, Shuai Kang, Youxiang Li, Shibin Sun, Ali Liu, Shuo Wang, Yuanli Zhao, and Xiaolin Chen. Development and validation of a scoring system for hemorrhage risk in brain arteriovenous malformations. JAMA Network Open, 6:e231070, Mar 2023. URL: https://doi.org/10.1001/jamanetworkopen.2023.1070, doi:10.1001/jamanetworkopen.2023.1070. This article has 69 citations and is from a peer-reviewed journal.

3. (saito2024crisprcasrxsuppresseskrasinduced pages 1-2): Shoji Saito, Yuka Nakamura, Satoshi Miyashita, Tokiharu Sato, Kana Hoshina, Masayasu Okada, Hitoshi Hasegawa, Makoto Oishi, Yukihiko Fujii, Jakob Körbelin, Yoshiaki Kubota, Kazuki Tainaka, Manabu Natsumeda, and Masaki Ueno. Crispr/casrx suppresses kras-induced brain arteriovenous malformation developed in postnatal brain endothelial cells in mice. JCI Insight, Nov 2024. URL: https://doi.org/10.1172/jci.insight.179729, doi:10.1172/jci.insight.179729. This article has 11 citations and is from a domain leading peer-reviewed journal.

4. (mohr2020medicalmanagementwith pages 1-2): Jay P Mohr, Jessica R Overbey, Andreas Hartmann, Rüdiger von Kummer, Rustam Al-Shahi Salman, Helen Kim, H Bart van der Worp, Michael K Parides, Marco A Stefani, Emmanuel Houdart, Richard Libman, John Pile-Spellman, Kirsty Harkness, Charlotte Cordonnier, Ellen Moquete, Alessandra Biondi, Catharina J M Klijn, Christian Stapf, and Alan J Moskowitz. Medical management with interventional therapy versus medical management alone for unruptured brain arteriovenous malformations (aruba): final follow-up of a multicentre, non-blinded, randomised controlled trial. The Lancet Neurology, 19:573-581, Jul 2020. URL: https://doi.org/10.1016/s1474-4422(20)30181-2, doi:10.1016/s1474-4422(20)30181-2. This article has 215 citations and is from a highest quality peer-reviewed journal.

5. (NCT02098252 chunk 1):  Treatment of Brain AVMs (TOBAS) Study. Centre hospitalier de l'Université de Montréal (CHUM). 2014. ClinicalTrials.gov Identifier: NCT02098252

6. (OpenTargets Search: brain arteriovenous malformation): Open Targets Query (brain arteriovenous malformation, 10 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (rutledge2014hemorrhageratesand pages 4-6): W. Caleb Rutledge, Nerissa U. Ko, Michael T. Lawton, and Helen Kim. Hemorrhage rates and risk factors in the natural history course of brain arteriovenous malformations. Translational Stroke Research, 5:538-542, Jun 2014. URL: https://doi.org/10.1007/s12975-014-0351-0, doi:10.1007/s12975-014-0351-0. This article has 144 citations and is from a peer-reviewed journal.

8. (winkler2022asinglecellatlas pages 1-3): Ethan A. Winkler, Chang N. Kim, Jayden M. Ross, Joseph H. Garcia, Eugene Gil, Irene Oh, Lindsay Q. Chen, David Wu, Joshua S. Catapano, Kunal Raygor, Kazim Narsinh, Helen Kim, Shantel Weinsheimer, Daniel L. Cooke, Brian P. Walcott, Michael T. Lawton, Nalin Gupta, Berislav V. Zlokovic, Edward F. Chang, Adib A. Abla, Daniel A. Lim, and Tomasz J. Nowakowski. A single-cell atlas of the normal and malformed human brain vasculature. Mar 2022. URL: https://doi.org/10.1126/science.abi7377, doi:10.1126/science.abi7377. This article has 333 citations and is from a highest quality peer-reviewed journal.

9. (walchli2024singlecellatlasof pages 1-2): Thomas Wälchli, Moheb Ghobrial, Marc Schwab, Shigeki Takada, Hang Zhong, Samuel Suntharalingham, Sandra Vetiska, Daymé Rodrigues Gonzalez, Ruilin Wu, Hubert Rehrauer, Anuroopa Dinesh, Kai Yu, Edward L. Y. Chen, Jeroen Bisschop, Fiona Farnhammer, Ann Mansur, Joanna Kalucka, Itay Tirosh, Luca Regli, Karl Schaller, Karl Frei, Troy Ketela, Mark Bernstein, Paul Kongkham, Peter Carmeliet, Taufik Valiante, Peter B. Dirks, Mario L. Suva, Gelareh Zadeh, Viviane Tabar, Ralph Schlapbach, Hartland W. Jackson, Katrien De Bock, Jason E. Fish, Philippe P. Monnier, Gary D. Bader, and Ivan Radovanovic. Single-cell atlas of the human brain vasculature across development, adulthood and disease. Nature, 632:603-613, Jul 2024. URL: https://doi.org/10.1038/s41586-024-07493-y, doi:10.1038/s41586-024-07493-y. This article has 197 citations and is from a highest quality peer-reviewed journal.

10. (pan2021theroleof pages 5-6): Peipei Pan, Sonali S Shaligram, Leandro Barbosa Do Prado, Liangliang He, and Hua Su. The role of mural cells in hemorrhage of brain arteriovenous malformation. Brain Hemorrhages, 2:49-56, Mar 2021. URL: https://doi.org/10.1016/j.hest.2020.10.005, doi:10.1016/j.hest.2020.10.005. This article has 20 citations.

11. (scimone2024methylomeanalysisof pages 1-2): Concetta Scimone, Luigi Donato, Simona Alibrandi, Alfredo Conti, Carlo Bortolotti, Antonino Germanò, Concetta Alafaci, Sergio Lucio Vinci, Rosalia D'Angelo, and Antonina Sidoti. Methylome analysis of endothelial cells suggests new insights on sporadic brain arteriovenous malformation. Heliyon, 10:e35126, Aug 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e35126, doi:10.1016/j.heliyon.2024.e35126. This article has 11 citations.

12. (hauer2020rnasequencinghighlightsinflammation pages 1-2): Allard J. Hauer, Rachel Kleinloog, Fabrizio Giuliani, Gabriël J.E. Rinkel, Gerard A. de Kort, Jan Willem Berkelbach van der Sprenkel, Albert van der Zwan, Peter H. Gosselaar, Peter C. van Rijen, Jelkje J. de Boer-Bergsma, Patrick Deelen, Morris A. Swertz, Louis De Muynck, Philip Van Damme, Jan H. Veldink, Ynte M. Ruigrok, and Catharina J.M. Klijn. Rna-sequencing highlights inflammation and impaired integrity of the vascular wall in brain arteriovenous malformations. Stroke, 51:268-274, Jan 2020. URL: https://doi.org/10.1161/strokeaha.119.025657, doi:10.1161/strokeaha.119.025657. This article has 38 citations and is from a highest quality peer-reviewed journal.

13. (tu2024somaticbrafv600emutation pages 1-6): Tianqi Tu, Jiaxing Yu, Chendan Jiang, Shikun Zhang, Jingwei Li, Jian Ren, Shiju Zhang, Yuan Zhou, Ziwei Cui, Haohan Lu, Xiaosheng Meng, Zhanjing Wang, Dong Xing, Hongqi Zhang, and Tao Hong. Somatic brafv600e mutation in the cerebral endothelium induces brain arteriovenous malformations. Angiogenesis, 27:441-460, May 2024. URL: https://doi.org/10.1007/s10456-024-09918-8, doi:10.1007/s10456-024-09918-8. This article has 17 citations and is from a domain leading peer-reviewed journal.

14. (chauvet2024diagnosticaccuracyof pages 1-2): Grégoire Chauvet, Mourad Cheddad El Aouni, Elsa Magro, Ophélie Sabardu, Douraied Ben Salem, Jean-Christophe Gentric, and Julien Ognard. Diagnostic accuracy of non-contrast-enhanced time-resolved mr angiography to assess angioarchitectural classification features of brain arteriovenous malformations. Jul 2024. URL: https://doi.org/10.3390/diagnostics14151656, doi:10.3390/diagnostics14151656. This article has 8 citations.

15. (chen2023developmentandvalidation pages 2-3): Yu Chen, Heze Han, Xiangyu Meng, Hengwei Jin, Dezhi Gao, Li Ma, Ruinan Li, Zhipeng Li, Debin Yan, Haibin Zhang, Kexin Yuan, Ke Wang, Yukun Zhang, Yang Zhao, Weitao Jin, Runting Li, Fa Lin, Xiaofeng Chao, Zhengfeng Lin, Qiang Hao, Hao Wang, Xun Ye, Shuai Kang, Youxiang Li, Shibin Sun, Ali Liu, Shuo Wang, Yuanli Zhao, and Xiaolin Chen. Development and validation of a scoring system for hemorrhage risk in brain arteriovenous malformations. JAMA Network Open, 6:e231070, Mar 2023. URL: https://doi.org/10.1001/jamanetworkopen.2023.1070, doi:10.1001/jamanetworkopen.2023.1070. This article has 69 citations and is from a peer-reviewed journal.

16. (chauvet2024diagnosticaccuracyof pages 2-5): Grégoire Chauvet, Mourad Cheddad El Aouni, Elsa Magro, Ophélie Sabardu, Douraied Ben Salem, Jean-Christophe Gentric, and Julien Ognard. Diagnostic accuracy of non-contrast-enhanced time-resolved mr angiography to assess angioarchitectural classification features of brain arteriovenous malformations. Jul 2024. URL: https://doi.org/10.3390/diagnostics14151656, doi:10.3390/diagnostics14151656. This article has 8 citations.

17. (NCT04572568 chunk 1):  Registry of Multimodality Treatment for Brain Arteriovenous Malformation in Mainland China. Beijing Tiantan Hospital. 2011. ClinicalTrials.gov Identifier: NCT04572568

18. (NCT07314047 chunk 1):  The Liquid Embolic Agent for the Treatment of Brain Arteriovenous Malformation. MicroPort NeuroTech Co., Ltd.. 2024. ClinicalTrials.gov Identifier: NCT07314047

19. (saito2024crisprcasrxsuppresseskrasinduced pages 2-4): Shoji Saito, Yuka Nakamura, Satoshi Miyashita, Tokiharu Sato, Kana Hoshina, Masayasu Okada, Hitoshi Hasegawa, Makoto Oishi, Yukihiko Fujii, Jakob Körbelin, Yoshiaki Kubota, Kazuki Tainaka, Manabu Natsumeda, and Masaki Ueno. Crispr/casrx suppresses kras-induced brain arteriovenous malformation developed in postnatal brain endothelial cells in mice. JCI Insight, Nov 2024. URL: https://doi.org/10.1172/jci.insight.179729, doi:10.1172/jci.insight.179729. This article has 11 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Brain_Arteriovenous_Malformation-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 12 |
| On topic | 5 |
| Off topic | 0 |

12 of 13 references resolved; the rest could not be looked up either way.
---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T11:31:24.583686'
end_time: '2026-08-28T11:45:45.104506'
duration_seconds: 860.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial Complex I Deficiency Nuclear Type 34
  mondo_id: MONDO:0032910
  category: Mitochondrial Disorders
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 31
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 48
  verified: 47
  not_found: 0
  obsolete: 1
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0032910
    reported_labels:
    - if available
    ontology_label: mitochondrial complex I deficiency, nuclear type 34
  obsolete_terms:
  - term_id: GO:0005747
    ontology_label: obsolete mitochondrial respiratory chain complex I
    replaced_by: GO:0045271
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_34-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency Nuclear Type 34
- **MONDO ID:** MONDO:0032910 (if available)
- **Category:** Mitochondrial Disorders

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency Nuclear Type 34** covering all of the
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
- **Disease Name:** Mitochondrial Complex I Deficiency Nuclear Type 34
- **MONDO ID:** MONDO:0032910 (if available)
- **Category:** Mitochondrial Disorders

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency Nuclear Type 34** covering all of the
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


# Mitochondrial Complex I Deficiency, Nuclear Type 34

## Executive summary and evidence limits

Mitochondrial complex I deficiency, nuclear type 34 (MC1DN34) is an ultra-rare, autosomal-recessive primary mitochondrial disorder caused by biallelic pathogenic variants in **NDUFAF8**, which encodes NADH:ubiquinone oxidoreductase complex assembly factor 8. Its established clinical presentation is an infantile/early-childhood **Leigh syndrome spectrum disorder** with developmental delay or regression, seizures, tone abnormalities, optic-nerve involvement, feeding and respiratory problems, characteristic bilateral brain lesions, and isolated respiratory-chain complex I deficiency. The disease-defining evidence consists of only **three unrelated boys** reported in one 2020 study; accordingly, frequencies calculated from these cases must not be treated as population estimates. Open Targets currently identifies NDUFAF8 as the single associated target for MONDO:0032910. (OpenTargets Search: mitochondrial complex I deficiency nuclear type 34, alston2020pathogenicbiallelicmutations pages 1-2)

The most important recent advance is a 2023 mechanistic study showing that NDUFAF8 undergoes an unusual two-stage mitochondrial import process linking the intermembrane-space disulfide relay to matrix complex-I biogenesis. No additional 2023–2024 clinical NDUFAF8 cohort, genotype-specific treatment trial, or validated disease-specific biomarker was identified. (peker2023atwostepmitochondrial pages 2-3, peker2023atwostepmitochondrial pages 11-13, peker2023atwostepmitochondrial pages 1-2)

| domain | disease-specific finding | evidence strength/limitations |
|---|---|---|
| Identity | Mitochondrial complex I deficiency, nuclear type 34; MONDO:0032910; disease-associated target/gene NDUFAF8 (NADH:ubiquinone oxidoreductase complex assembly factor 8) (OpenTargets Search: mitochondrial complex I deficiency nuclear type 34) | Disease identity and gene-disease link are supported by MONDO/Open Targets and the defining human report; OMIM/Orphanet IDs were not verified in-conversation, so omitted (OpenTargets Search: mitochondrial complex I deficiency nuclear type 34, alston2020pathogenicbiallelicmutations pages 1-2) |
| Inheritance | Autosomal recessive / bi-allelic NDUFAF8 variants (OpenTargets Search: mitochondrial complex I deficiency nuclear type 34, alston2020pathogenicbiallelicmutations pages 1-2) | Strong for inheritance pattern, but based on a very small number of reported families/patients (OpenTargets Search: mitochondrial complex I deficiency nuclear type 34, alston2020pathogenicbiallelicmutations pages 1-2) |
| Reported human cases | Three unrelated pediatric cases, all boys, with clinical Leigh syndrome (alston2020pathogenicbiallelicmutations pages 1-2, alston2020pathogenicbiallelicmutations pages 7-8) | Strong disease-defining evidence, but the cohort is limited to three unrelated boys in one primary report (alston2020pathogenicbiallelicmutations pages 1-2, alston2020pathogenicbiallelicmutations pages 7-8) |
| Pathogenic variants | Four reported disease-associated variants: c.45_52dup p.Phe18Serfs*32; c.195+271C>T; c.1A>G; c.165C>G p.Phe55Leu. Subject 1: compound heterozygous c.45_52dup and c.195+271C>T; Subject 2: compound heterozygous c.1A>G and c.195+271C>T; Subject 3: homozygous c.165C>G p.Phe55Leu (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 8-9) | Exact variant-level evidence is strong from the primary paper; only one recurrent deep intronic variant was seen in two subjects; broad allelic spectrum remains unknown (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 7-8) |
| Variant interpretation | Subjects 1 and 2 each had a single heterozygous class 5 ACMG variant initially recognized; the deep intronic c.195+271C>T variant was uncovered with additional analysis; subject 3 carried an unreported homozygous missense variant affecting invariant Phe55 (alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 7-8) | Strong for the reported cases; ACMG details for every variant were not fully provided in-conversation, and no external classification updates were verified here (alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 7-8) |
| Age at onset | Infantile/early childhood onset. Subject 1 had infantile spasms at 3 months; Subject 2 had spasms at 9 months and regression after viral illness at 2 years 9 months; Subject 3 was developmentally normal until 15 months, then presented acutely (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2) | Strong for early onset, but based on three individuals with variable presentations (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2) |
| Major phenotypes | Leigh syndrome with developmental delay/regression, seizures/infantile spasms, hypotonia or tone abnormalities, feeding difficulties/failure to thrive, respiratory failure, optic involvement (optic atrophy, small optic nerves, visual impairment), and characteristic brain MRI lesions (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2, alston2020pathogenicbiallelicmutations pages 7-8) | Strong disease-specific phenotype evidence from case descriptions, but no frequency estimates beyond 3/3 or 2/3 can be generalized (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2, alston2020pathogenicbiallelicmutations pages 7-8) |
| Neuroimaging | Symmetrical lesions affecting basal ganglia/thalami/brainstem with additional structural abnormalities including corpus callosum dysgenesis, periventricular cysts, gray matter heterotopia, absent septum pellucidum, and hippocampal involvement in some subjects (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2) | Strong for reported individuals; structural malformations may broaden the phenotype but need confirmation in additional cases (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2) |
| Biochemistry | Isolated complex I deficiency. Subject 1: complex I activity 33% of control in muscle and 47% in fibroblasts relative to citrate synthase; Subject 3: residual complex I activity 3% in muscle (alston2020pathogenicbiallelicmutations pages 3-4) | Strong biochemical evidence for disease mechanism; data are tissue-limited and unavailable for all assays in all subjects (alston2020pathogenicbiallelicmutations pages 3-4) |
| Functional validation | Subject 1 fibroblasts showed reduced oxidative capacity and markedly decreased assembled complex I on BN-PAGE; lentiviral re-expression of wild-type NDUFAF8 restored complex I assembly, complex I activity, and NDUFAF5 steady-state levels (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 1-2) | Very strong causal evidence for Subject 1; direct rescue data were not available for all variants, especially the Subject 3 missense change (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 7-8) |
| Assembly/pathophysiology | Complexome profiling in subject fibroblasts showed reduced respirasome, increased free complex III, and stalled complex I assembly intermediates at PD-a and a partly assembled Q-module, supporting a role for NDUFAF8 in early complex I assembly and NDUFAF5 stability (alston2020pathogenicbiallelicmutations pages 7-8, alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 1-2) | Strong mechanistic disease evidence from patient cells, but still derived mainly from one extensively studied subject (alston2020pathogenicbiallelicmutations pages 7-8, alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 1-2) |
| 2023 mechanistic update | NDUFAF8 follows a two-step mitochondrial import route involving transient access to the IMS disulfide relay/CHCHD4 system and subsequent matrix translocation; oxidation promotes NDUFAF8 accumulation/stability, while matrix NDUFAF8 stabilizes/activates NDUFAF5 for Q-module assembly (peker2023atwostepmitochondrial pages 2-3, peker2023atwostepmitochondrial pages 11-13, peker2023atwostepmitochondrial pages 7-8, peker2023atwostepmitochondrial pages 1-2, peker2023atwostepmitochondrial pages 5-7) | Important current mechanistic understanding, but mostly from cellular/biochemical models rather than additional NDUFAF8 patient cohorts (peker2023atwostepmitochondrial pages 2-3, peker2023atwostepmitochondrial pages 11-13, peker2023atwostepmitochondrial pages 7-8, peker2023atwostepmitochondrial pages 1-2, peker2023atwostepmitochondrial pages 5-7) |
| Outcomes | Severe, progressive disease. Subject 1 was alive at age 2 years in the report with slow progress, seizures, and visual impairment; Subject 2 died at 4 years 1 month; Subject 3 died at 18 months during hypertensive crisis after feeding problems/failure to thrive (alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2) | Strong for seriousness and early mortality risk, but the sample is too small for robust prognosis estimates (alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2) |
| Therapy | No disease-specific approved or reported targeted therapy for NDUFAF8-related disease was identified in-conversation; care in the defining report was supportive, and in vitro lentiviral complementation was experimental only (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 1-2) | Strong negative statement only in the sense of absent evidence in the available record; this should not be interpreted as proof that no off-label/supportive treatments are ever used (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 1-2) |
| Epidemiology | No disease-specific prevalence or incidence data were identified for NDUFAF8-related mitochondrial complex I deficiency nuclear type 34 (alston2020pathogenicbiallelicmutations pages 1-2, lim2022naturalhistoryof pages 1-2) | Major evidence gap; only broader Leigh syndrome prevalence context exists, not NDUFAF8-specific epidemiology (alston2020pathogenicbiallelicmutations pages 1-2, lim2022naturalhistoryof pages 1-2) |
| Model organisms | No disease-specific NDUFAF8 natural disease model organism or dedicated animal model was identified in-conversation; mechanistic work used patient cells and cellular systems (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 5-7, peker2023atwostepmitochondrial pages 2-3, peker2023atwostepmitochondrial pages 11-13) | Major evidence gap; absence here reflects lack of identified evidence in the conversation, not definitive nonexistence (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 5-7, peker2023atwostepmitochondrial pages 2-3, peker2023atwostepmitochondrial pages 11-13) |


*Table: This table condenses the disease-defining clinical, genetic, biochemical, and mechanistic evidence for NDUFAF8-related mitochondrial complex I deficiency nuclear type 34. It is useful as a compact knowledge-base summary while clearly marking where evidence is limited to a very small number of reported cases.*

## 1. Disease information

### Definition and nomenclature

MC1DN34 is a nuclear-encoded disorder of mitochondrial oxidative phosphorylation in which defective NDUFAF8 impairs early assembly of respiratory-chain complex I. Clinically, the reported patients met criteria for Leigh syndrome, a progressive mitochondrial encephalopathy characterized by developmental impairment or regression and bilateral lesions of the basal ganglia, thalamus, or brainstem. The defining article states that all three subjects had “a clinical diagnosis of Leigh syndrome” and biallelic pathogenic NDUFAF8 variants. (alston2020pathogenicbiallelicmutations pages 1-2)

**Identifiers and synonyms**

- **MONDO:** MONDO:0032910.
- **Disease name:** mitochondrial complex I deficiency, nuclear type 34.
- **Common abbreviations/synonyms:** MC1DN34; NDUFAF8-related mitochondrial disease; NDUFAF8-related Leigh syndrome; Leigh syndrome due to NDUFAF8 deficiency; isolated mitochondrial complex I deficiency due to NDUFAF8.
- **Leigh syndrome parent concept:** MIM 256000.
- **Gene:** NDUFAF8, formerly **C17orf89**; the defining paper cites gene MIM **618461**. The protein is NADH:ubiquinone oxidoreductase complex assembly factor 8. (OpenTargets Search: mitochondrial complex I deficiency nuclear type 34, alston2020pathogenicbiallelicmutations pages 1-2)
- **ICD/MeSH:** No dedicated ICD-10, ICD-11, or MeSH code for MC1DN34 was verified. It should be coded under the appropriate broader mitochondrial-metabolism/Leigh-syndrome category according to the coding system and jurisdiction rather than assigned an unverified disease-specific code.
- **Orphanet/OMIM disease number:** A distinct disease-level number was not independently verified in the retrieved evidence and should remain null pending direct database curation.

The primary evidence is **individual-patient research/clinical data**, subsequently aggregated into MONDO, Open Targets, ClinVar, and Leigh-syndrome resources. It is not an EHR-derived population study. (OpenTargets Search: mitochondrial complex I deficiency nuclear type 34, alston2020pathogenicbiallelicmutations pages 1-2)

**Key source:** Alston et al., *American Journal of Human Genetics*, online 19 December 2019; issue date 2 January 2020; “Pathogenic Bi-allelic Mutations in NDUFAF8 Cause Leigh Syndrome with an Isolated Complex I Deficiency,” DOI [10.1016/j.ajhg.2019.12.001](https://doi.org/10.1016/j.ajhg.2019.12.001), PMID **31866046**. Its abstract states: “Subject fibroblasts were found to express a complex I deficiency, and lentiviral transduction with wild-type NDUFAF8-cDNA ameliorated both the assembly defect and the biochemical deficiency.” (alston2020pathogenicbiallelicmutations pages 1-2)

## 2. Etiology and risk/protective factors

### Causal factor

The established cause is **germline biallelic loss or dysfunction of NDUFAF8**. Subjects 1 and 2 had predicted null combinations; subject 3 carried a homozygous missense change affecting a conserved aromatic residue. Functional complementation of subject-1 fibroblasts with wild-type NDUFAF8 restored complex-I assembly, activity, and NDUFAF5 abundance, providing strong causal rather than merely associative evidence. (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 7-8)

### Risk factors

- **Genetic:** Having pathogenic variants on both NDUFAF8 alleles is the necessary established risk factor. Each parent of an affected child is ordinarily an unaffected heterozygous carrier.
- **Family history/consanguinity:** All three reported families were non-consanguineous; therefore consanguinity is not required, although it generally increases the probability that both parents carry the same rare recessive allele. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4)
- **Sex:** All three reported patients were male, but NDUFAF8 is autosomal and there is no evidence for a biological male excess; this is likely sampling noise.
- **Environmental/lifestyle/infectious:** No exposure causes the genetic disorder. Febrile, respiratory, gastrointestinal, and viral illnesses preceded acute decompensation or regression in the reported children, consistent with increased energetic demand revealing or worsening mitochondrial dysfunction, but these are **triggers**, not causes. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2)

### Protective factors and gene–environment interaction

No protective NDUFAF8 allele, modifier gene, diet, supplement, or lifestyle intervention has been established. Avoidance of fasting and prompt treatment of infection/dehydration are biologically reasonable mitochondrial-care measures, but they have not been tested specifically in MC1DN34. The available gene–environment pattern is therefore: biallelic NDUFAF8 dysfunction lowers respiratory reserve; infection, fever, vomiting, diarrhea, dehydration, or respiratory stress raises energy demand; ATP/redox failure then precipitates acidosis, neurologic regression, respiratory failure, or crisis. This inference is supported by the temporal case histories but has not been quantified experimentally in patients. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4)

## 3. Phenotypes

Because only three patients are known, counts below describe the original series and are not stable prevalence estimates.

- **Developmental delay/impaired milestones** — all three had delayed or abnormal development; severity ranged from slow acquisition to profound delay. Subject 2 sat at 13–14 months, pulled to stand at 15 months, and at age two could neither crawl nor stand independently and had no speech. Suggested HPO: **Global developmental delay (HP:0001263)**, **Delayed motor development (HP:0001270)**, **Absent speech (HP:0001344)**. (alston2020pathogenicbiallelicmutations pages 2-3)
- **Developmental regression** — documented after viral illness in subject 2, with partial recovery. Suggested HPO: **Developmental regression (HP:0002376)**. Course: episodic decompensation superimposed on progression. (alston2020pathogenicbiallelicmutations pages 2-3)
- **Seizures/infantile spasms** — subjects 1 and 2 had infantile spasms at 3 and 9 months, respectively; subject 1 continued to have fleeting seizures. EEG showed hypsarrhythmia or modified hypsarrhythmia. Suggested HPO: **Seizure (HP:0001250)**, **Infantile spasms (HP:0012469)**, **Hypsarrhythmia (HP:0002521)**. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 1-2)
- **Hypotonia and abnormal tone** — generalized hypotonia was prominent in subject 1, with increased lower-limb tone. Suggested HPO: **Generalized hypotonia (HP:0001290)** and **Hypertonia (HP:0001276)**. (alston2020pathogenicbiallelicmutations pages 1-2)
- **Visual/optic-nerve disease** — subject 1 had optic atrophy and visual impairment; subject 2 had small optic nerves and nystagmus. Suggested HPO: **Optic atrophy (HP:0000648)**, **Optic nerve hypoplasia (HP:0000609)**, **Visual impairment (HP:0000505)**, **Nystagmus (HP:0000639)**. Optic involvement was observed in at least two of three cases. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 1-2, alston2020pathogenicbiallelicmutations pages 7-8)
- **Feeding dysfunction and poor growth** — dysphagia, prolonged feeding, tube dependence, weight loss, failure to thrive, and gastrostomy occurred. Suggested HPO: **Dysphagia (HP:0002015)**, **Feeding difficulties (HP:0011968)**, **Failure to thrive (HP:0001508)**, **Gastrostomy tube feeding (HP:0033454)**. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4)
- **Respiratory dysfunction** — apnea, disrupted respiratory drive, pneumonia-associated respiratory failure, ventilation, and tracheostomy were reported. Suggested HPO: **Apnea (HP:0002104)**, **Respiratory failure (HP:0002878)**. (alston2020pathogenicbiallelicmutations pages 2-3)
- **Hypertensive crisis** — recurrent and fatal in subject 3. Suggested HPO: **Systemic hypertension (HP:0000822)**; a more specific hypertensive-crisis term should be used if available in the target HPO release. (alston2020pathogenicbiallelicmutations pages 3-4)
- **Metabolic abnormalities** — variable metabolic acidosis and lactate elevation. Subject 1 reached lactate 15 mmol/L during acute illness and later had 3.0–6.0 mmol/L; subject 2 had persistent 2.9–6.2 mmol/L and lactate/pyruvate ratio 22; subject 3 had normal blood lactate 1.44 mmol/L but CSF lactate 3 mmol/L. Suggested HPO: **Lactic acidosis (HP:0003128)**, **Elevated CSF lactate (HP:0012402)**, and **Metabolic acidosis (HP:0001942)**. Normal blood lactate therefore does not exclude the disease. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2)
- **Anemia and vitamin deficiencies** — subject 3 had normocytic anemia, low folinic acid, and vitamin B12 deficiency; these single-patient findings may be secondary and are not established core phenotypes. Suggested HPO: **Anemia (HP:0001903)** and **Vitamin B12 deficiency (HP:0100502)**. (alston2020pathogenicbiallelicmutations pages 3-4)
- **Prenatal/neonatal findings** — subject 2 had intrauterine growth restriction, prematurity at 35 weeks, prenatal ventriculomegaly, possible dysplastic kidney, and abnormal placental Doppler flow. Suggested HPO: **Intrauterine growth retardation (HP:0001511)** and **Premature birth (HP:0001622)**. Whether these are consistently NDUFAF8-related is unknown. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 1-2)

### Neuroimaging phenotype

MRI demonstrated bilateral symmetric abnormalities of the globi pallidi, putamina, thalami, dorsal brainstem, hippocampi/hippocampal tails, and optic radiations. Additional developmental or destructive abnormalities included corpus-callosum dysgenesis, absent splenium, periventricular cystic encephalomalacia, absent septum pellucidum, frontal polymicrogyria, and gray-matter heterotopia. Suggested HPO terms include **Abnormality of the basal ganglia (HP:0002134)**, **Brainstem abnormality (HP:0002363)**, **Abnormal corpus callosum morphology (HP:0001273)**, **Polymicrogyria (HP:0002126)**, and **Gray matter heterotopia (HP:0002282)**. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2)

### Quality of life

No EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life data exist. The observed consequences—loss or failure of independent mobility, absent speech, visual impairment, recurrent seizures, prolonged feeding, gastrostomy/tracheostomy, ICU admission, and early death—indicate profound effects on daily function and caregiver burden. Leigh-syndrome cohort data show wheelchair dependence increasing from 31% to 57% and exclusive enteral feeding from 22% to 46% during follow-up, but these are syndrome-level rather than NDUFAF8-specific statistics. (lim2022naturalhistoryof pages 3-5, lim2022naturalhistoryof pages 1-2)

## 4. Genetic and molecular information

### Gene and variants

**NDUFAF8** is a very small nuclear gene; the disease report used transcript **NM_001086521.1** and protein **NP_001079990.1**, encoding a 74-amino-acid protein. Four germline variants were reported:

1. **c.45_52dup, p.(Phe18Serfs*32)** — frameshift, compound heterozygous in subject 1; ACMG class 5 in the report.
2. **c.195+271C>T, p.?** — recurrent deep-intronic/splicing allele in subjects 1 and 2. Subject-1 RNA showed loss of the relevant transcript from this allele, consistent with loss of function.
3. **c.1A>G, p.?** — start-loss variant, compound heterozygous in subject 2; ACMG class 5 in the report.
4. **c.165C>G, p.(Phe55Leu)** — homozygous missense variant in subject 3, affecting an invariant aromatic residue in a predicted interaction/stability helix. Direct rescue of this individual variant was not possible because additional tissue was unavailable. (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 7-8)

ClinVar submissions were **SCV000995081–SCV000995084**, respectively. These are inherited germline variants; no somatic disease mechanism is implicated. (alston2020pathogenicbiallelicmutations pages 8-9)

The exact four disease alleles were not reported as common population variants. Contextually, gnomAD v2.1 contained no nonsynonymous variants at Trp8, Phe18, Tyr32, or Phe62 and only one heterozygote each at Phe50 and Phe55: p.Phe50Leu, 1/31,392 alleles (3.18×10⁻⁵), and p.Phe55Ser, 1/134,102 (7.46×10⁻⁶). These comparison variants are **not** the reported disease alleles. (alston2020pathogenicbiallelicmutations pages 7-8)

### Other genomic domains

No reproducible modifier gene, protective allele, DNA-methylation signature, histone alteration, repeat expansion, aneuploidy, translocation, inversion, or recurrent pathogenic copy-number change has been reported. Penetrance among individuals with two true loss-of-function alleles is presumed high but cannot be numerically estimated from three cases. Anticipation is not expected for a recessive non-repeat disorder. Germline mosaicism remains a generic low residual risk after apparently de novo results but was not observed.

## 5. Environmental information

No toxin, radiation, pollution, occupation, smoking, alcohol, diet, or infectious agent causes MC1DN34. Intercurrent rhinovirus, nonspecific viral illness, fever, gastroenteritis, dehydration, and pneumonia coincided with severe deterioration in the cases. These observations support metabolic vulnerability during catabolic stress but not pathogen specificity. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4)

Practical avoidance of prolonged fasting, dehydration, tobacco smoke, and known mitochondrial-toxic medicines is reasonable as general mitochondrial practice, but no NDUFAF8-specific efficacy data exist. Environmental protective factors and formal gene–environment studies are unavailable.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic NDUFAF8 loss/dysfunction reduces stable, functional NDUFAF8.
2. **Import/folding defect:** NDUFAF8 normally has a weak N-terminal mitochondrial targeting signal and a twin-CX9C cysteine motif. It traverses the outer membrane, transiently encounters the CHCHD4/MIA40 disulfide relay in the intermembrane space, receives two disulfide bonds, and subsequently undergoes TIM23-dependent transfer into the matrix. YME1L limits excess IMS protein, whereas CLPP degrades reduced NDUFAF8 in the matrix. Oxidation is therefore principally important for accumulation/stability rather than the final catalytic interaction itself. (peker2023atwostepmitochondrial pages 11-13, peker2023atwostepmitochondrial pages 7-8, peker2023atwostepmitochondrial pages 1-2, peker2023atwostepmitochondrial pages 5-7)
3. **Assembly-factor failure:** matrix NDUFAF8 binds and stabilizes NDUFAF5. Loss of NDUFAF8 lowers NDUFAF5 abundance and stalls assembly of the complex-I Q module involving NDUFS2, NDUFS3, and NDUFA5; PD-a assembly and later modules are secondarily reduced. (alston2020pathogenicbiallelicmutations pages 5-7, peker2023atwostepmitochondrial pages 2-3, peker2023atwostepmitochondrial pages 11-13)
4. **Respiratory-chain defect:** mature complex I and the CI–CIII₂–CIV respirasome decrease, while free complex III increases. Patient muscle/fibroblasts consequently show isolated complex-I deficiency and reduced oxidative capacity. (alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 7-8)
5. **Downstream bioenergetic injury:** impaired NADH oxidation, proton pumping, membrane-potential support, and ATP production disproportionately injure energy-demanding neurons, optic pathways, brainstem respiratory circuits, and muscle. Acute catabolic stress can overwhelm residual reserve, producing lactate/acidosis, seizures, regression, apnea, and respiratory failure. Oxidative stress is biologically plausible but was not directly quantified in the three patients.

The 2023 study further found that NDUFAF8-knockout cells had isolated complex-I deficiency and abolished ND1 synthesis, connecting NDUFAF8 to early Q-module/ND1 biogenesis. This was cellular evidence, not an additional human natural-history cohort. (peker2023atwostepmitochondrial pages 27-31)

**Recent primary source:** Peker et al., *Journal of Cell Biology*, May 2023, “A two-step mitochondrial import pathway couples the disulfide relay with matrix complex I biogenesis,” DOI [10.1083/jcb.202210019](https://doi.org/10.1083/jcb.202210019). Its summary states that a weak targeting signal lets proteins acquire “stabilizing disulfide bonds in the IMS en route to the matrix.” (peker2023atwostepmitochondrial pages 2-3, peker2023atwostepmitochondrial pages 1-2)

### Suggested ontology annotations

- **GO biological process:** mitochondrial respiratory-chain complex I assembly; oxidative phosphorylation; mitochondrial electron transport, NADH to ubiquinone; mitochondrial protein import; protein oxidation; cellular response to oxidative stress; ATP metabolic process.
- **GO molecular function:** complex-I assembly-factor activity/protein binding; NDUFAF5 binding is mechanistically relevant. Avoid assigning NADH dehydrogenase catalytic activity to NDUFAF8 itself.
- **GO cellular component:** mitochondrial matrix; mitochondrial intermembrane space; mitochondrial inner membrane-associated complex-I assembly intermediates; respiratory-chain complex I/respirasome.
- **Cell Ontology:** neuron (**CL:0000540**), retinal ganglion cell (**CL:0000740**), skeletal muscle cell/myocyte, astrocyte, oligodendrocyte, and cardiomyocyte are biologically relevant high-demand cells, but only neuronal/optic and muscle involvement is directly supported clinically. No single-cell atlas of NDUFAF8 disease exists.

### Molecular profiling and advanced technologies

Disease-specific data include patient-cell respirometry, quantitative muscle immunofluorescence, BN-PAGE, complexome proteomics, RNA analysis of the intronic allele, and lentiviral rescue. The deposited complexome dataset is **ProteomeXchange/PRIDE PXD015749**. No disease-specific metabolomic, lipidomic, epigenomic, single-cell, spatial-transcriptomic, organoid, or multi-omic patient cohort has been published in the retrieved literature. (alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 3-4)

## 7. Anatomical structures affected

- **Primary organ/system:** central nervous system, especially bilateral basal ganglia, thalami, dorsal brainstem, cerebral white/periventricular regions, corpus callosum, hippocampi, and optic pathways.
- **Secondary systems:** skeletal muscle bioenergetics; gastrointestinal/nutritional system through dysphagia and failure to thrive; respiratory system through central apnea and infection-associated failure. Cardiac testing was normal in the surviving subject, so cardiomyopathy is not an established phenotype. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 1-2)
- **Suggested UBERON mappings:** brain (**UBERON:0000955**), brainstem (**UBERON:0002298**), thalamus (**UBERON:0001897**), basal ganglion (**UBERON:0002420**), putamen, globus pallidus, hippocampus (**UBERON:0002421**), corpus callosum (**UBERON:0002336**), optic nerve (**UBERON:0000962**), skeletal muscle tissue (**UBERON:0001134**).
- **Subcellular compartment:** mitochondrion (**GO:0005739**), mitochondrial matrix (**GO:0005759**), intermembrane space (**GO:0005758**), inner membrane (**GO:0005743**), complex I (**GO:0005747**).
- **Lateralization:** characteristic lesions are bilateral/symmetric; heterotopia was right-sided in subject 2. (alston2020pathogenicbiallelicmutations pages 2-3)

## 8. Temporal development

Onset ranged from 3 months to 15 months in the defining series, although one child had prenatal growth restriction and neonatal imaging abnormalities. Presentation could be insidious developmental delay or acute decompensation during illness. The course was chronic and progressive with episodic metabolic/neurologic crises, partial recovery of some skills after an episode, and major risk of early death. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2)

A practical course model is: early developmental/seizure phase; evolving motor, visual, feeding, and brainstem dysfunction; episodic illness-associated regression; advanced tube-feeding/ventilatory dependence or death. This is descriptive, not a validated staging system. The vulnerable intervention windows are before irreversible neurologic injury and at the onset of infection, poor intake, dehydration, seizures, or respiratory change.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Each pregnancy of two confirmed carriers has a 25% affected, 50% carrier, and 25% unaffected/non-carrier probability. Both sexes should be equally susceptible. The three unrelated families were white British, white American, and German and were non-consanguineous; no founder effect, enriched ethnicity, geographic cluster, or sex ratio can be inferred. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2)

No MC1DN34-specific prevalence, incidence, carrier frequency, or birth prevalence is available. Only three published index patients were identified. For context only, Leigh syndrome overall has been estimated at approximately **1 in 40,000 births**, rising to 1 in 2,000 in some isolated populations; this must not be assigned to MC1DN34. (alston2020pathogenicbiallelicmutations pages 1-2, lim2022naturalhistoryof pages 1-2)

## 10. Diagnostics

### Recommended approach

1. **Clinical suspicion:** infantile developmental delay/regression, seizures or infantile spasms, hypotonia/dystonia, optic atrophy/hypoplasia, feeding or respiratory dysfunction, especially after metabolic stress.
2. **MRI/MRS:** seek bilateral basal-ganglia, thalamic, and brainstem lesions; document corpus-callosum and cortical-development abnormalities. MRI pattern plus regression supports Leigh syndrome but is not gene-specific.
3. **Biochemistry:** blood gas, glucose, lactate and pyruvate with ratio, plasma amino acids/acylcarnitines, CK, ammonia, liver/renal tests, urine organic acids; consider CSF lactate/pyruvate where clinically indicated. Normal blood lactate does not exclude the diagnosis. In a 72-child Leigh cohort, serum lactate was elevated in 68% of 50 tested and CSF lactate in 64% of 36. (lim2022naturalhistoryof pages 2-3)
4. **System assessment:** EEG, ophthalmology, swallowing/nutrition, ECG/echocardiography, respiratory/sleep evaluation, hearing, renal and endocrine review as indicated.
5. **Genetics first:** use a comprehensive nuclear mitochondrial/Leigh/complex-I panel or preferably trio WES/WGS with mtDNA analysis and CNV calling. Ensure **NDUFAF8 introns** are adequately covered; if one pathogenic allele is found, specifically interrogate c.195+271C>T and other deep-intronic/structural variants. The original authors emphasized “the importance of evaluating intronic sequence when a single, definitively pathogenic variant is identified.” (alston2020pathogenicbiallelicmutations pages 1-2, alston2020pathogenicbiallelicmutations pages 7-8)
6. **RNA/functional confirmation:** fibroblast RNA-seq or targeted cDNA analysis is valuable for splice variants. Patient fibroblast respirometry, BN-PAGE/complexome profiling, or complementation may resolve a VUS. Muscle biopsy is now generally second-line when genomic/RNA evidence is insufficient or tissue-specific biochemical proof is required. In the Leigh cohort, only 18/37 biopsied children had abnormal respiratory-chain activities; complex I deficiency was the commonest defect. (lim2022naturalhistoryof pages 2-3, lim2022naturalhistorystudy pages 128-131)

Karyotyping, FISH, repeat-expansion testing, and liquid biopsy are not routine for this single-gene disorder. Chromosomal microarray may be appropriate when congenital anomalies suggest a CNV, but it will not reliably detect the reported SNV/indel alleles. Because this is a nuclear disorder, mtDNA testing alone is insufficient, although mtDNA analysis remains necessary in undiagnosed Leigh syndrome.

The major differentials are other nuclear or mtDNA causes of Leigh syndrome, pyruvate-dehydrogenase disorders, biotin-thiamine-responsive basal-ganglia disease, organic acidemias, cerebral folate disorders, hypoxic–ischemic injury, infection, toxic/metabolic encephalopathy, OPA1-related disease, and LHON where optic neuropathy dominates. NDUFAF8 disease is distinguished by biallelic variants plus isolated complex-I assembly deficiency and, when needed, RNA/functional evidence.

## 11. Outcome and prognosis

Disease-specific outcomes are severe but heterogeneous: subject 1 was alive at age two with slow progress, hypotonia, seizures, and visual impairment; subject 2 died at **4 years 1 month** after pneumonia and respiratory failure; subject 3 died at **18 months** during recurrent hypertensive crisis. Thus, two of three reported patients died in early childhood, but three cases cannot define survival probabilities. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2)

Leigh-syndrome-level data provide cautious context. In a 72-child UK cohort followed a median 2.6 years, mortality was 17%; severe disease burden increased from 22% to 42%, wheelchair dependence from 31% to 57%, and exclusive enteral feeding from 22% to 46%. Higher NPMDS scores, rapid annual progression, faltering growth, and caudate/striatal imaging changes predicted poorer outcomes. One child in that cohort had the subject-1 NDUFAF8 genotype, but no genotype-specific estimate was possible. (lim2022naturalhistoryof pages 3-5, lim2022naturalhistorystudy pages 154-157, lim2022naturalhistoryof pages 1-2)

No validated NDUFAF8-specific prognostic biomarker exists. Residual complex-I activity may plausibly relate to severity—subject 3 had 3% muscle activity and rapidly progressive disease—but this observation is insufficient for a predictive threshold. (alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 7-8)

## 12. Treatment and current applications

### Standard clinical management

There is no approved disease-modifying treatment for NDUFAF8 deficiency. Management should be multidisciplinary and individualized:

- rapid treatment of infection, fever, vomiting, dehydration, hypoglycemia, acidosis, and respiratory compromise;
- individualized seizure therapy; prednisolone was used for infantile spasms in subject 1, but it was not a genotype-directed treatment;
- nutrition and swallowing support, high-calorie feeding as tolerated, NG/gastrostomy when required, and avoidance of prolonged fasting;
- respiratory surveillance, airway clearance, oxygen/ventilation, tracheostomy when necessary;
- physical, occupational, speech/communication, visual, and palliative-care services;
- monitoring of growth, hearing, vision, cardiac function, renal function, blood pressure, and endocrine/metabolic status. (alston2020pathogenicbiallelicmutations pages 2-3, alston2020pathogenicbiallelicmutations pages 3-4, alston2020pathogenicbiallelicmutations pages 1-2)

Suggested NCIT intervention concepts include **Genetic Counseling**, **Anticonvulsant Therapy**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Nutritional Support**, **Gastrostomy**, **Mechanical Ventilation**, **Tracheostomy**, and **Palliative Care**; local NCIT release identifiers should be validated before database ingestion.

“mitochondrial cocktail” supplements such as coenzyme Q10/ubiquinone, riboflavin, thiamine, biotin, folinic acid, or L-carnitine are sometimes used empirically. In the broader Leigh cohort, supplement use did not measurably alter course; this is observational and does not prove ineffectiveness for every biochemical genotype. No NDUFAF8 pharmacogenomic rule exists. (lim2022naturalhistoryof pages 3-5)

### Experimental therapy and trials

Wild-type NDUFAF8 lentiviral expression rescued patient fibroblasts, establishing **proof of mechanism**, not a clinically usable gene therapy. No NDUFAF8-specific viral-vector, CRISPR, mRNA, ASO, siRNA, cell, or enzyme therapy trial was identified. (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 5-7)

Broader studies potentially accepting Leigh/mitochondrial patients include:

- **NCT03137355**, International Registry for Leigh Syndrome, recruiting, observational, target n=200.
- **NCT05554835**, global mitochondrial-disorder registry/natural-history study, recruiting, target n=6,000.
- **NCT01721733** and **NCT02352896**, completed phase-2 EPI-743/vatiquinone studies in children with Leigh syndrome, n=35 and n=30.
- **NCT02023866**, completed phase-2 RP103/cysteamine study in mitochondrial disease, n=36.

These studies are not evidence of efficacy in MC1DN34, and eligibility must be confirmed directly at [ClinicalTrials.gov](https://clinicaltrials.gov/). No response rate can appropriately be assigned to NDUFAF8 disease.

## 13. Prevention

The genetic lesion cannot currently be prevented after conception through lifestyle or vaccination.

- **Primary prevention:** carrier testing for relatives, reproductive counseling, partner testing, preimplantation genetic testing for monogenic disease, chorionic-villus sampling, or amniocentesis once familial variants are known.
- **Secondary prevention:** cascade testing of siblings/relatives and early molecular diagnosis in symptomatic infants. Population newborn screening is unavailable; lactate is neither sufficiently sensitive nor specific.
- **Tertiary prevention:** individualized emergency plans, avoidance of fasting/dehydration, prompt infection management, vaccination according to routine schedules to reduce preventable catabolic illness, seizure control, aspiration prevention, nutrition, and respiratory surveillance.

Genetic counseling should explain the 25% recurrence risk for carrier couples, limitations of prenatal phenotype prediction, and the uncertainty created by the very small case series. Mitochondrial replacement therapy is not applicable to this nuclear-gene disorder.

## 14. Other species and natural disease

NDUFAF8 is evolutionarily conserved; the disease-associated Phe55 was reported as invariant from boreoeutherian mammals to at least zebrafish, supporting functional importance. (alston2020pathogenicbiallelicmutations pages 3-4)

No naturally occurring NDUFAF8-deficiency syndrome in a companion animal, livestock breed, or wildlife species was identified, and there is no zoonotic or cross-species transmission. This is an inherited molecular defect, not an infectious disease. Ortholog-specific NCBI Gene and NCBI Taxonomy identifiers should be imported directly from current NCBI/Alliance records rather than inferred here.

## 15. Model organisms and experimental systems

The strongest disease models are **human patient fibroblasts** and engineered human-cell NDUFAF8-knockout/knockdown systems. Patient cells reproduced reduced respiration, isolated complex-I deficiency, loss of assembled complex I/respirasome, reduced NDUFAF5, and stalled Q/PD-a assembly. Wild-type cDNA rescue demonstrated specificity. (alston2020pathogenicbiallelicmutations pages 4-5, alston2020pathogenicbiallelicmutations pages 5-7)

The 2023 mechanistic work used cellular import, redox, localization, knockout, protease, and complementation assays to define the CHCHD4–NDUFAF8–NDUFAF5 pathway. Advantages are direct molecular tractability and measurable rescue; limitations are the absence of tissue architecture, neurodevelopment, whole-body metabolic crises, and long-term clinical phenotypes. (peker2023atwostepmitochondrial pages 2-3, peker2023atwostepmitochondrial pages 11-13, peker2023atwostepmitochondrial pages 27-31)

No dedicated Ndufaf8 mouse, rat, zebrafish, Drosophila, *C. elegans*, yeast disease model, patient-derived iPSC neuron, brain organoid, or knock-in model reproducing a human allele was identified in the retrieved literature. These are important future priorities for studying selective neuronal/optic vulnerability and testing gene replacement.

## Evidence assessment and curation recommendations

The **gene–disease relationship is strong**, because recessive segregation, predicted loss-of-function alleles, patient biochemical defects, transcript disruption, assembly intermediates, and wild-type rescue converge. However, the **phenotypic spectrum, penetrance, prevalence, survival, and treatment response remain poorly characterized** because the clinical evidence is essentially three patients. The 2023 mechanistic study substantially strengthened biological understanding but did not expand the patient cohort. (alston2020pathogenicbiallelicmutations pages 5-7, alston2020pathogenicbiallelicmutations pages 7-8, peker2023atwostepmitochondrial pages 2-3)

For a knowledge base, entries should therefore be tagged as:

- **Human clinical—strong but very limited cohort:** phenotype, MRI, outcomes, inheritance.
- **Human patient-cell—strong functional:** isolated complex-I deficiency, assembly defect, cDNA rescue.
- **Engineered-cell/in vitro—strong mechanistic:** two-stage import, disulfide relay, protease control, NDUFAF5 stabilization.
- **Syndrome-level extrapolation:** epidemiology, natural history, supportive management, and clinical trials.
- **No evidence/unknown:** disease-specific prevalence, environmental cause, protective variants, epigenetic signature, targeted therapy, validated animal model, and quantitative quality-of-life data.

### Core references

1. Alston CL et al. Published online **19 December 2019**; issue date **2 January 2020**. *Pathogenic Bi-allelic Mutations in NDUFAF8 Cause Leigh Syndrome with an Isolated Complex I Deficiency.* **PMID 31866046**. [DOI/URL](https://doi.org/10.1016/j.ajhg.2019.12.001). (alston2020pathogenicbiallelicmutations pages 1-2)
2. Peker E et al. **May 2023**. *A two-step mitochondrial import pathway couples the disulfide relay with matrix complex I biogenesis.* [DOI/URL](https://doi.org/10.1083/jcb.202210019). (peker2023atwostepmitochondrial pages 2-3, peker2023atwostepmitochondrial pages 11-13)
3. Lim AZ et al. **2022**. *Natural History of Leigh Syndrome: A Study of Disease Burden and Progression.* [DOI/URL](https://doi.org/10.1002/ana.26260). This is contextual Leigh-syndrome evidence, not an NDUFAF8-specific cohort. (lim2022naturalhistoryof pages 2-3, lim2022naturalhistoryof pages 1-2)
4. McCormick E et al. **August 2023**. *Expert Panel Curation of 113 Primary Mitochondrial Disease Genes for the Leigh Syndrome Spectrum.* [DOI/URL](https://doi.org/10.1002/ana.26716). This supports the contemporary expert-curation framework for genetically heterogeneous Leigh syndrome.
5. Zarges C, Riemer J. **June 2024**. *Oxidative protein folding in the intermembrane space of human mitochondria.* [DOI/URL](https://doi.org/10.1002/2211-5463.13839). This is a mechanistic review, not primary patient evidence.

References

1. (OpenTargets Search: mitochondrial complex I deficiency nuclear type 34): Open Targets Query (mitochondrial complex I deficiency nuclear type 34, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (alston2020pathogenicbiallelicmutations pages 1-2): Charlotte L. Alston, Mike T. Veling, Juliana Heidler, Lucie S. Taylor, Joseph T. Alaimo, Andrew Y. Sung, Langping He, Sila Hopton, Alexander Broomfield, Julija Pavaine, Jullianne Diaz, Eyby Leon, Philipp Wolf, Robert McFarland, Holger Prokisch, Saskia B. Wortmann, Penelope E. Bonnen, Ilka Wittig, David J. Pagliarini, and Robert W. Taylor. Pathogenic bi-allelic mutations in ndufaf8 cause leigh syndrome with an isolated complex i deficiency. Jan 2020. URL: https://doi.org/10.1016/j.ajhg.2019.12.001, doi:10.1016/j.ajhg.2019.12.001. This article has 67 citations.

3. (peker2023atwostepmitochondrial pages 2-3): Esra Peker, Konstantin Weiss, Jiyao Song, Christine Zarges, Sarah Gerlich, Volker Boehm, Aleksandra Trifunovic, Thomas Langer, Niels H. Gehring, Thomas Becker, and Jan Riemer. A two-step mitochondrial import pathway couples the disulfide relay with matrix complex i biogenesis. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202210019, doi:10.1083/jcb.202210019. This article has 30 citations.

4. (peker2023atwostepmitochondrial pages 11-13): Esra Peker, Konstantin Weiss, Jiyao Song, Christine Zarges, Sarah Gerlich, Volker Boehm, Aleksandra Trifunovic, Thomas Langer, Niels H. Gehring, Thomas Becker, and Jan Riemer. A two-step mitochondrial import pathway couples the disulfide relay with matrix complex i biogenesis. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202210019, doi:10.1083/jcb.202210019. This article has 30 citations.

5. (peker2023atwostepmitochondrial pages 1-2): Esra Peker, Konstantin Weiss, Jiyao Song, Christine Zarges, Sarah Gerlich, Volker Boehm, Aleksandra Trifunovic, Thomas Langer, Niels H. Gehring, Thomas Becker, and Jan Riemer. A two-step mitochondrial import pathway couples the disulfide relay with matrix complex i biogenesis. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202210019, doi:10.1083/jcb.202210019. This article has 30 citations.

6. (alston2020pathogenicbiallelicmutations pages 7-8): Charlotte L. Alston, Mike T. Veling, Juliana Heidler, Lucie S. Taylor, Joseph T. Alaimo, Andrew Y. Sung, Langping He, Sila Hopton, Alexander Broomfield, Julija Pavaine, Jullianne Diaz, Eyby Leon, Philipp Wolf, Robert McFarland, Holger Prokisch, Saskia B. Wortmann, Penelope E. Bonnen, Ilka Wittig, David J. Pagliarini, and Robert W. Taylor. Pathogenic bi-allelic mutations in ndufaf8 cause leigh syndrome with an isolated complex i deficiency. Jan 2020. URL: https://doi.org/10.1016/j.ajhg.2019.12.001, doi:10.1016/j.ajhg.2019.12.001. This article has 67 citations.

7. (alston2020pathogenicbiallelicmutations pages 4-5): Charlotte L. Alston, Mike T. Veling, Juliana Heidler, Lucie S. Taylor, Joseph T. Alaimo, Andrew Y. Sung, Langping He, Sila Hopton, Alexander Broomfield, Julija Pavaine, Jullianne Diaz, Eyby Leon, Philipp Wolf, Robert McFarland, Holger Prokisch, Saskia B. Wortmann, Penelope E. Bonnen, Ilka Wittig, David J. Pagliarini, and Robert W. Taylor. Pathogenic bi-allelic mutations in ndufaf8 cause leigh syndrome with an isolated complex i deficiency. Jan 2020. URL: https://doi.org/10.1016/j.ajhg.2019.12.001, doi:10.1016/j.ajhg.2019.12.001. This article has 67 citations.

8. (alston2020pathogenicbiallelicmutations pages 3-4): Charlotte L. Alston, Mike T. Veling, Juliana Heidler, Lucie S. Taylor, Joseph T. Alaimo, Andrew Y. Sung, Langping He, Sila Hopton, Alexander Broomfield, Julija Pavaine, Jullianne Diaz, Eyby Leon, Philipp Wolf, Robert McFarland, Holger Prokisch, Saskia B. Wortmann, Penelope E. Bonnen, Ilka Wittig, David J. Pagliarini, and Robert W. Taylor. Pathogenic bi-allelic mutations in ndufaf8 cause leigh syndrome with an isolated complex i deficiency. Jan 2020. URL: https://doi.org/10.1016/j.ajhg.2019.12.001, doi:10.1016/j.ajhg.2019.12.001. This article has 67 citations.

9. (alston2020pathogenicbiallelicmutations pages 8-9): Charlotte L. Alston, Mike T. Veling, Juliana Heidler, Lucie S. Taylor, Joseph T. Alaimo, Andrew Y. Sung, Langping He, Sila Hopton, Alexander Broomfield, Julija Pavaine, Jullianne Diaz, Eyby Leon, Philipp Wolf, Robert McFarland, Holger Prokisch, Saskia B. Wortmann, Penelope E. Bonnen, Ilka Wittig, David J. Pagliarini, and Robert W. Taylor. Pathogenic bi-allelic mutations in ndufaf8 cause leigh syndrome with an isolated complex i deficiency. Jan 2020. URL: https://doi.org/10.1016/j.ajhg.2019.12.001, doi:10.1016/j.ajhg.2019.12.001. This article has 67 citations.

10. (alston2020pathogenicbiallelicmutations pages 2-3): Charlotte L. Alston, Mike T. Veling, Juliana Heidler, Lucie S. Taylor, Joseph T. Alaimo, Andrew Y. Sung, Langping He, Sila Hopton, Alexander Broomfield, Julija Pavaine, Jullianne Diaz, Eyby Leon, Philipp Wolf, Robert McFarland, Holger Prokisch, Saskia B. Wortmann, Penelope E. Bonnen, Ilka Wittig, David J. Pagliarini, and Robert W. Taylor. Pathogenic bi-allelic mutations in ndufaf8 cause leigh syndrome with an isolated complex i deficiency. Jan 2020. URL: https://doi.org/10.1016/j.ajhg.2019.12.001, doi:10.1016/j.ajhg.2019.12.001. This article has 67 citations.

11. (alston2020pathogenicbiallelicmutations pages 5-7): Charlotte L. Alston, Mike T. Veling, Juliana Heidler, Lucie S. Taylor, Joseph T. Alaimo, Andrew Y. Sung, Langping He, Sila Hopton, Alexander Broomfield, Julija Pavaine, Jullianne Diaz, Eyby Leon, Philipp Wolf, Robert McFarland, Holger Prokisch, Saskia B. Wortmann, Penelope E. Bonnen, Ilka Wittig, David J. Pagliarini, and Robert W. Taylor. Pathogenic bi-allelic mutations in ndufaf8 cause leigh syndrome with an isolated complex i deficiency. Jan 2020. URL: https://doi.org/10.1016/j.ajhg.2019.12.001, doi:10.1016/j.ajhg.2019.12.001. This article has 67 citations.

12. (peker2023atwostepmitochondrial pages 7-8): Esra Peker, Konstantin Weiss, Jiyao Song, Christine Zarges, Sarah Gerlich, Volker Boehm, Aleksandra Trifunovic, Thomas Langer, Niels H. Gehring, Thomas Becker, and Jan Riemer. A two-step mitochondrial import pathway couples the disulfide relay with matrix complex i biogenesis. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202210019, doi:10.1083/jcb.202210019. This article has 30 citations.

13. (peker2023atwostepmitochondrial pages 5-7): Esra Peker, Konstantin Weiss, Jiyao Song, Christine Zarges, Sarah Gerlich, Volker Boehm, Aleksandra Trifunovic, Thomas Langer, Niels H. Gehring, Thomas Becker, and Jan Riemer. A two-step mitochondrial import pathway couples the disulfide relay with matrix complex i biogenesis. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202210019, doi:10.1083/jcb.202210019. This article has 30 citations.

14. (lim2022naturalhistoryof pages 1-2): Albert Z. Lim, Yi Shiau Ng, Alasdair Blain, Cecilia Jiminez‐Moreno, Charlotte L. Alston, Victoria Nesbitt, Louise Simmons, Saikat Santra, Evangeline Wassmer, Emma L. Blakely, Doug M. Turnbull, Robert W. Taylor, Gráinne S. Gorman, and Robert McFarland. Natural history of leigh syndrome: a study of disease burden and progression. Annals of Neurology, 91:117-130, Nov 2022. URL: https://doi.org/10.1002/ana.26260, doi:10.1002/ana.26260. This article has 57 citations and is from a highest quality peer-reviewed journal.

15. (lim2022naturalhistoryof pages 3-5): Albert Z. Lim, Yi Shiau Ng, Alasdair Blain, Cecilia Jiminez‐Moreno, Charlotte L. Alston, Victoria Nesbitt, Louise Simmons, Saikat Santra, Evangeline Wassmer, Emma L. Blakely, Doug M. Turnbull, Robert W. Taylor, Gráinne S. Gorman, and Robert McFarland. Natural history of leigh syndrome: a study of disease burden and progression. Annals of Neurology, 91:117-130, Nov 2022. URL: https://doi.org/10.1002/ana.26260, doi:10.1002/ana.26260. This article has 57 citations and is from a highest quality peer-reviewed journal.

16. (peker2023atwostepmitochondrial pages 27-31): Esra Peker, Konstantin Weiss, Jiyao Song, Christine Zarges, Sarah Gerlich, Volker Boehm, Aleksandra Trifunovic, Thomas Langer, Niels H. Gehring, Thomas Becker, and Jan Riemer. A two-step mitochondrial import pathway couples the disulfide relay with matrix complex i biogenesis. The Journal of Cell Biology, May 2023. URL: https://doi.org/10.1083/jcb.202210019, doi:10.1083/jcb.202210019. This article has 30 citations.

17. (lim2022naturalhistoryof pages 2-3): Albert Z. Lim, Yi Shiau Ng, Alasdair Blain, Cecilia Jiminez‐Moreno, Charlotte L. Alston, Victoria Nesbitt, Louise Simmons, Saikat Santra, Evangeline Wassmer, Emma L. Blakely, Doug M. Turnbull, Robert W. Taylor, Gráinne S. Gorman, and Robert McFarland. Natural history of leigh syndrome: a study of disease burden and progression. Annals of Neurology, 91:117-130, Nov 2022. URL: https://doi.org/10.1002/ana.26260, doi:10.1002/ana.26260. This article has 57 citations and is from a highest quality peer-reviewed journal.

18. (lim2022naturalhistorystudy pages 128-131): AZ Lim. Natural history study of childhood-onset mitochondrial disorders by using outcome measure assessments. Unknown journal, 2022.

19. (lim2022naturalhistorystudy pages 154-157): AZ Lim. Natural history study of childhood-onset mitochondrial disorders by using outcome measure assessments. Unknown journal, 2022.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_34-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032910` (4 mentions) - the report calls it "if available"; MONDO calls it **mitochondrial complex I deficiency, nuclear type 34**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005747` (obsolete mitochondrial respiratory chain complex I) (1 mention) - replaced by `GO:0045271`
---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T19:01:28.256796'
end_time: '2026-08-28T19:17:27.452485'
duration_seconds: 959.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 98 (DFNB98, TSPEAR-related)
  mondo_id: MONDO:0013929
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 10
  verified: 10
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013929
    reported_labels:
    - if available
    ontology_label: autosomal recessive nonsyndromic hearing loss 98
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_98-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 98 (DFNB98, TSPEAR-related)
- **MONDO ID:** MONDO:0013929 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 98 (DFNB98, TSPEAR-related)** covering all of the
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
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 98 (DFNB98, TSPEAR-related)
- **MONDO ID:** MONDO:0013929 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 98 (DFNB98, TSPEAR-related)** covering all of the
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


# Autosomal Recessive Nonsyndromic Hearing Loss 98 (DFNB98; historically TSPEAR-related)

## Executive assessment

**The central knowledge-base caveat is that DFNB98 should not currently be represented as a firmly established TSPEAR disorder.** It is a historical/provisional autosomal-recessive nonsyndromic sensorineural hearing-loss entity based initially on one consanguineous Iranian family. Larger subsequent cohorts and functional studies support **TSPEAR-related autosomal recessive ectodermal dysplasia 14 (ARED14/ECTD14)**—especially a dental phenotype—much more strongly than isolated deafness. Bowles et al. found that all three hearing-impaired members of a 13-person biallelic-TSPEAR cohort had competing variants in established hearing-loss genes; Jackson et al. subsequently concluded that evidence was insufficient to link TSPEAR to autosomal-recessive hearing loss. Therefore, a biallelic TSPEAR result alone should not be considered a definitive molecular diagnosis of DFNB98. (bowles2021tspearvariantsare pages 1-2, jackson2023clinicalgeneticepidemiologic pages 5-8)

| Evidence/date | Design/sample | Key finding | Implication for gene-disease validity |
|---|---|---|---|
| Delmaghani et al., 2012 | Original discovery report; 3 consanguineous Iranian siblings with profound SNHL; homozygous **TSPEAR c.1726_1728delGTCinsTT, p.Val576Leufs*38** identified by WES | Established the historical DFNB98 claim by linking biallelic TSPEAR to isolated profound hearing loss in one family; no alternative hearing-loss variants were reported in that initial study summary (bowles2021tspearvariantsare pages 2-4) | **Supportive but low-level evidence** for DFNB98 because it rests on a single family and has not been robustly replicated without confounding (bowles2021tspearvariantsare pages 2-4) |
| Bowles et al., 2021 | Cohort study of **13 newly reported individuals** with biallelic TSPEAR variants | **11/13** had tooth agenesis or ectodermal dysplasia; **3/13** had hearing loss, but **all 3** also carried variants in other hearing-loss genes (**TMPRSS3, GJB2, GJB6**). Authors concluded the evidence “creates significant doubt” that TSPEAR is a monogenic hearing-loss gene (bowles2021tspearvariantsare pages 1-2) | **Major evidence against established DFNB98 validity**; strongly shifts interpretation toward **TSPEAR-related ectodermal/dental disease** rather than isolated ARNSHL (bowles2021tspearvariantsare pages 1-2, bowles2021tspearvariantsare pages 10-11) |
| Jackson et al., 2023 | Aggregate human + mechanistic study; **30 affected individuals** analyzed across new and published cases; includes zebrafish double-knockout and mouse scRNA-seq | Human phenotype was **100% dental anomalies**; common findings included conical teeth (77%), hypodontia (50%), oligodontia (37%); **none of their cohort** had SNHL; authors state there is **“insufficient evidence to link TSPEAR variants as a cause of AR hearing loss.”** Functional work supported **ARED14** biology (enamel-knot expression, ECM/WNT-related dental model), not an auditory mechanism (jackson2023clinicalgeneticepidemiologic pages 5-8, jackson2023clinicalgeneticepidemiologic pages 1-2, jackson2023clinicalgeneticepidemiologic pages 11-13, jackson2023clinicalgeneticepidemiologic pages 13-14, jackson2023clinicalgeneticepidemiologic pages 14-15) | **Strongest current evidence hierarchy item**: supports **TSPEAR-related autosomal recessive ectodermal dysplasia 14 (ARED14)** as established; **DFNB98 remains disputed/insufficient** (jackson2023clinicalgeneticepidemiologic pages 5-8, jackson2023clinicalgeneticepidemiologic pages 1-2, jackson2023clinicalgeneticepidemiologic pages 11-13) |
| Shi et al., 2024 | Small supportive case/family report from China; compound heterozygous TSPEAR variants reported with AR hearing loss | Adds **limited supportive case-level evidence** for a hearing-loss association, but on its own does not overcome prior contradictory cohort data or the lack of replicated auditory functional evidence; details were not fully available in retrieved text (mentioned as unobtainable paper in search results) | **Weak supportive evidence only**; does **not resolve** disputed DFNB98 validity |
| Ahmadkhani et al., 2026 | Single case report; **6-year-old Iranian girl**, consanguineous family; profound bilateral SNHL; homozygous **TSPEAR c.668C>T, p.Ser223Leu** by WES | Reported isolated severe/profound bilateral SNHL with normal teeth/skin/hair/nails and absent ABR response; authors note isolated hearing presentation is rare (ahmadkhani2026anovelpathogenic pages 1-2) | **Additional anecdotal support** for possible TSPEAR-related hearing loss, but still **insufficient** to overturn Bowles/Jackson or establish DFNB98 definitively (ahmadkhani2026anovelpathogenic pages 1-2) |
| Current synthesis | Evidence hierarchy across original family reports, larger cohorts, and mechanistic studies | Hearing-loss evidence remains sparse, partly confounded, and mechanistically unvalidated for the ear; by contrast, dental/ectodermal evidence is replicated across cohorts and supported by functional data (bowles2021tspearvariantsare pages 1-2, jackson2023clinicalgeneticepidemiologic pages 5-8, jackson2023clinicalgeneticepidemiologic pages 11-13, peled2016mutationsintspear pages 1-2) | **Current conclusion:** **DFNB98 (TSPEAR-related ARNSHL) = disputed / insufficient evidence**; **TSPEAR-related ARED14 = established gene-disease relationship** (bowles2021tspearvariantsare pages 1-2, jackson2023clinicalgeneticepidemiologic pages 5-8, jackson2023clinicalgeneticepidemiologic pages 1-2) |


*Table: This table ranks the main published evidence bearing on the TSPEAR–DFNB98 relationship. It is useful because it distinguishes the early family-based hearing-loss claim from later larger cohort and functional studies that instead support TSPEAR-related ARED14.*

## 1. Disease information

### Definition and status

DFNB98 denotes a proposed form of **autosomal-recessive nonsyndromic sensorineural hearing loss (ARNSHL)** historically attributed to biallelic variants in **TSPEAR**. The original 2012 report described three consanguineous Iranian siblings with profound SNHL and homozygous **c.1726_1728delGTCinsTT, p.(Val576LeufsTer38)**. No alternative hearing-loss variant was reported at that time. Later observations of hearing-normal individuals with the same genotype materially weakened the claimed association. (bowles2021tspearvariantsare pages 2-4)

The more secure TSPEAR disease association is **ectodermal dysplasia 14, hair/tooth type, with or without hypohidrosis**. In the 2023 aggregate analysis of 30 affected people, every individual had dental anomalies, whereas none of the authors’ newly assembled cohort had SNHL. (jackson2023clinicalgeneticepidemiologic pages 5-8)

### Identifiers and synonyms

- **MONDO:** MONDO:0013929, as supplied in the query; retain with a “disputed/provisional gene association” qualifier.
- **OMIM disease:** Deafness, autosomal recessive 98/DFNB98 is historically catalogued separately from **ECTD14, OMIM 618180**. TSPEAR itself is **OMIM 612920**. The retrieved literature explicitly confirms the latter two numbers. (ahmadkhani2026anovelpathogenic pages 1-2)
- **Gene:** **TSPEAR**, thrombospondin-type laminin G domain and epilepsy-associated repeats; chromosome 21q22 region. Common transcript used in recent reports: **NM_144991.3**. (ahmadkhani2026anovelpathogenic pages 1-2)
- **Synonyms:** DFNB98; deafness, autosomal recessive 98; TSPEAR-related nonsyndromic hearing loss; TSPEAR-associated ARNSHL; historical “EAR/EPTP-domain-containing protein–related deafness.”
- **ICD-10-CM:** no DFNB98-specific code; use phenotype-level codes such as **H90.3** (sensorineural hearing loss, bilateral) where clinically appropriate.
- **ICD-11/MeSH/Orphanet:** no confidently verified disease-specific mapping was found in the retrieved evidence; use broader hereditary or sensorineural hearing-loss concepts rather than asserting an exact code.

The evidence is **aggregated disease-level literature**, not an EHR-derived patient dataset, although the foundational evidence consists of individual pedigrees and case reports.

## 2. Etiology, risk, protection, and gene–environment interaction

### Proposed genetic cause

The proposed cause is **germline biallelic TSPEAR variation**, inherited recessively. Reported candidate alleles include truncating, frameshift, splice-predicted, missense, and in-frame deletion variants. However, pathogenicity for ECTD14 must not be conflated with pathogenicity for hearing loss: the phenotype-specific TSPEAR–DFNB98 relationship remains unproven. In ARED14, 27 reported disease-associated alleles comprised 11 predicted loss-of-function variants (41%) and 16 missense/in-frame variants (59%). Four recurrent founder alleles were p.Arg197Ter, p.Val576LeufsTer38, p.Ser585Ile, and p.Asp639Asn. (jackson2023clinicalgeneticepidemiologic pages 5-8, jackson2023clinicalgeneticepidemiologic pages 8-11)

### Genetic risk factors and confounding

- **Consanguinity/family history** increases the probability of homozygosity for rare recessive alleles but is not specific to TSPEAR.
- Variants in nearby **TMPRSS3** can be coinherited and are a particularly important alternative explanation. Bowles et al.’s hearing-loss cases also had variants involving **GJB2/GJB6**. (bowles2021tspearvariantsare pages 1-2, bowles2021tspearvariantsare pages 2-4)
- The original p.Val576LeufsTer38 allele has been observed in hearing-normal individuals, arguing against simple complete penetrance for deafness. (bowles2021tspearvariantsare pages 2-4)
- No validated modifier gene, protective TSPEAR allele, anticipation, or germline-mosaicism series has been reported.

### Environmental risks and protective factors

DFNB98 is proposed as genetic, so environmental exposure is not considered its primary cause. Nevertheless, congenital CMV, rubella, meningitis, prematurity, noise, and ototoxic medication are alternative or additive causes of SNHL and must be evaluated rather than attributing hearing loss automatically to TSPEAR. Bowles et al. specifically emphasized prenatal/environmental causes such as CMV and rubella. (bowles2021tspearvariantsare pages 2-4)

No disease-specific diet, lifestyle factor, medication, vaccine, or protective variant has been demonstrated. Avoiding preventable noise and ototoxic exposure protects residual hearing generally but does not prevent a congenital Mendelian defect. No TSPEAR-specific gene–environment interaction is established.

## 3. Phenotypes

### Proposed DFNB98 phenotype

The small number of reported patients suggests:

- **Bilateral sensorineural hearing loss** — HPO **HP:0000407** and **HP:0008619**.
- **Congenital/prelingual onset** — **HP:0008527** or **HP:0012715**, where documentation supports it.
- **Severe-to-profound hearing impairment** — **HP:0012714/HP:0012713**, subject to local ontology-version verification.
- **Speech and language impairment secondary to deafness** — **HP:0000750** or more specific speech-development terms.
- Occasionally reported **enlarged vestibular aqueduct** in two siblings with compound-heterozygous TSPEAR candidates, although this is not established as a TSPEAR feature. (bowles2021tspearvariantsare pages 1-2)

In the 2026 case report, a six-year-old girl had prelingual bilateral severe/profound SNHL, flat audiograms, absent bilateral ABR responses, speech disorder, and impaired school performance, with normal teeth, hair, skin, and nails. This is only single-case evidence. (ahmadkhani2026anovelpathogenic pages 1-2)

### Frequency, severity, and natural history

Reliable frequencies cannot be estimated for DFNB98. The original family had three affected siblings; Bowles et al. identified hearing loss in 3/13 newly reported biallelic-TSPEAR individuals, but every hearing-loss case had a competing molecular explanation. Jackson et al.’s 30-person ARED14 synthesis found dental anomalies in 100%, conical teeth in 77%, hypodontia in 50%, oligodontia in 37%, sparse hair in 47%, hypohidrosis in 23%, and hyperhidrosis in 10%; these are **ECTD14 statistics and must not be imported as DFNB98 frequencies**. (bowles2021tspearvariantsare pages 1-2, jackson2023clinicalgeneticepidemiologic pages 5-8)

Onset appears congenital or prelingual and the condition is lifelong. Stable versus progressive course has not been established. No episodic or remitting pattern is documented. Quality-of-life effects are those expected from severe childhood deafness—communication, language acquisition, education, and social participation—but no DFNB98-specific EQ-5D, SF-36, PROMIS, or hearing-related QoL study exists.

## 4. Genetic and molecular information

### Gene and protein

TSPEAR encodes a protein containing an N-terminal laminin-G-like domain and multiple EAR repeats. AlphaFold modeling predicts that the EAR domains form a conserved **β-propeller**, potentially functioning as a ligand-binding surface. Most ARED14-associated missense variants are predicted to destabilize this structure through steric clashes or loss of polar/disulfide interactions. (jackson2023clinicalgeneticepidemiologic pages 5-8)

### Notable variants

- **NM_144991.x:c.1726_1728delGTCinsTT, p.(Val576LeufsTer38):** original DFNB98 allele; predicted loss of function, but also reported in hearing-normal biallelic individuals, making hearing-specific classification uncertain. (bowles2021tspearvariantsare pages 2-4)
- **c.1566G>A, p.(Pro522=)** plus **c.1676_1677delAT, p.(Tyr559CysfsTer134):** reported in siblings with bilateral SNHL and enlarged vestibular aqueduct; replication and exclusion of all alternatives remain limited. (bowles2021tspearvariantsare pages 1-2)
- **NM_144991.3:c.668C>T, p.(Ser223Leu):** homozygous in a 2026 isolated-SNHL case; called pathogenic by the authors, but case-level evidence does not establish phenotype-specific causality. (ahmadkhani2026anovelpathogenic pages 1-2)
- **p.Asp639Asn:** common ARED14 founder/hypomorphic candidate. Frequency was 0.0038 in the 100,000 Genomes Project and 0.0035 in non-Finnish Europeans in gnomAD v2.1.1; 449 heterozygotes were identified among 59,464 100KGP genomes. These frequencies pertain to ectodermal-dysplasia interpretation, not proven deafness risk. (jackson2023clinicalgeneticepidemiologic pages 5-8, jackson2023clinicalgeneticepidemiologic pages 11-13)

All reported constitutional variants are **germline**, not somatic. No recurrent pathogenic chromosomal rearrangement, aneuploidy, repeat expansion, mitochondrial defect, or disease-specific epigenetic signature has been established. No validated modifier genes are known.

### Variant-interpretation recommendation

A laboratory may classify an allele as pathogenic for **TSPEAR-related ECTD14** while the gene–phenotype relationship for **DFNB98 remains disputed**. Accordingly, hearing-loss reports should distinguish:

1. allele-level classification under ACMG/AMP;
2. phase and recessive genotype;
3. phenotype-level gene validity;
4. competing variants in established deafness genes;
5. ectodermal/dental examination and radiography.

Computational structural destabilization is supporting evidence only. A 2023 deafness-proteome study noted that approximately 70% of 128,167 missense entries in the Deafness Variation Database were VUS, illustrating why modeling alone cannot establish clinical causality.

## 5. Environmental information

No toxin, radiation, pollutant, occupation, smoking pattern, diet, alcohol exposure, exercise pattern, or infectious agent is known to cause “TSPEAR-related DFNB98.” Environmental and infectious factors instead belong in the differential diagnosis and may worsen residual auditory function. Congenital CMV and rubella are particularly relevant alternatives in childhood SNHL. (bowles2021tspearvariantsare pages 2-4)

## 6. Mechanism and pathophysiology

### What is demonstrated

**Ectodermal mechanism:** In keratinocytes, TSPEAR knockdown altered Notch-regulated genes and reduced a Notch reporter signal; NOTCH1 protein was reduced in patient scalp, while silencing in mouse hair-follicle organ culture induced epithelial-cell apoptosis and reduced hair-bulb diameter. This supports hair/tooth morphogenesis, not an auditory causal chain. Direct abstract wording states that TSPEAR silencing was “associated with decreased Notch signaling.” (peled2016mutationsintspear pages 1-2)

Jackson et al. proposed a broader extracellular-matrix model. TSPEAR may bind/sequester morphogens through a laminin-G/heparin-binding surface, coordinating spatial and temporal **WNT, FGF, BMP, and NF-κB-related signaling** in ectodermal placodes. Mouse single-cell RNA-seq localized Tspear predominantly to the **enamel knot** and anagen hair-follicle keratinocytes. (jackson2023clinicalgeneticepidemiologic pages 11-13)

### What remains hypothetical for hearing

The proposed auditory chain is:

**biallelic TSPEAR loss → altered ECM/Notch-dependent developmental signaling in cochlear sensory/supporting cells → abnormal hair-cell fate or maintenance → bilateral SNHL.**

Every arrow in this hearing-specific chain remains inadequately validated. Earlier mouse immunohistochemistry suggested protein near the base of inner-ear hair cells, but public cochlear RNA-seq showed extremely low or absent Tspear transcript, and no study directly demonstrated hair-cell structural or physiological dysfunction after TSPEAR loss. (bowles2021tspearvariantsare pages 2-4)

Suggested annotations, with the caveat that several describe established ectodermal rather than proven auditory biology:

- **GO biological process:** extracellular-matrix organization; regulation of Notch signaling; canonical Wnt signaling; epithelial morphogenesis; odontogenesis; hair-follicle development; sensory-organ development; auditory-receptor-cell development.
- **GO cellular component:** extracellular region/extracellular matrix; protein-containing extracellular matrix; putative cell-surface/basal hair-cell localization remains uncertain.
- **Cell Ontology:** keratinocyte; hair-follicle epithelial cell; enamel-knot epithelial cell; ameloblast; cochlear hair cell and supporting cell only as proposed auditory targets.
- **Upstream:** TSPEAR structural loss or destabilization and altered ECM morphogen handling.
- **Downstream:** altered developmental transcription, apoptosis, enamel-matrix/mineralization defects; cochlear dysfunction remains hypothetical.

No replicated disease-specific human inner-ear transcriptomic, proteomic, metabolomic, lipidomic, methylomic, spatial-transcriptomic, iPSC, organoid, or CRISPR-screen signature is available.

## 7. Anatomical structures affected

For the proposed DFNB98 phenotype, the principal organ is the **inner ear**, especially the **cochlea** and organ of Corti; laterality is characteristically bilateral in reported cases. Suggested mappings are **UBERON:0001844** (cochlea), **UBERON:0002227** (organ of Corti; verify release), and broader inner-ear/auditory-system terms. Candidate cells are inner and outer hair cells and cochlear supporting cells, but direct TSPEAR pathology in these populations is not established.

For established ECTD14, the affected structures are teeth/dental epithelium, hair follicles, skin, nails, and sweat glands. The 2023 evidence localizes expression particularly to enamel-knot cells and anagen hair-follicle keratinocytes. (jackson2023clinicalgeneticepidemiologic pages 11-13)

## 8. Temporal development

Reported hearing loss is congenital or recognized during early childhood, often prelingually. It is chronic and lifelong; progression rate and age-dependent penetrance are unknown. There are no recognized stages, attacks, remission, or spontaneous recovery. The critical intervention period is early childhood, because delayed auditory access can impair language acquisition and education, as illustrated by speech and school difficulties in the six-year-old case. (ahmadkhani2026anovelpathogenic pages 1-2)

## 9. Inheritance and population

The proposed inheritance pattern is **autosomal recessive**. If a specific biallelic genotype is eventually shown to be causal and both parents are heterozygous, each pregnancy has the conventional 25% affected, 50% carrier, and 25% non-carrier probability. Because hearing penetrance is uncertain, “affected” should not be predicted solely from a TSPEAR genotype without qualification.

No reliable DFNB98 prevalence, incidence, carrier frequency, sex ratio, or geographic distribution exists. Reports include Iranian/Middle Eastern and more recent Chinese cases, but ascertainment is too sparse for population inference. The 2023 estimate of an approximately **1/140 non-Finnish-European TSPEAR deleterious-allele carrier rate** and ancestry-specific range from 1/287 in Finns to 1/43 in Ashkenazi Jewish individuals concerns **ARED14 alleles**, not validated DFNB98 carriers. (jackson2023clinicalgeneticepidemiologic pages 1-2, jackson2023clinicalgeneticepidemiologic pages 11-13)

Founder effects are documented for ARED14-associated p.Arg197Ter, p.Ser585Ile, p.Asp639Asn, and p.Val576LeufsTer38. Estimated most-recent-common-ancestor ages were approximately 12,000–20,211 years. This is evolutionary/population evidence, not proof of hearing pathogenicity. (jackson2023clinicalgeneticepidemiologic pages 8-11)

No sex bias, anticipation, or established germline mosaicism has been reported. Consanguinity contributed to ascertainment of the original family and the 2026 case. (bowles2021tspearvariantsare pages 2-4, ahmadkhani2026anovelpathogenic pages 1-2)

## 10. Diagnostics

### Clinical evaluation

1. Confirm hearing status with age-appropriate pure-tone/behavioral audiometry, tympanometry, otoacoustic emissions, and ABR when required.
2. Determine sensorineural versus conductive/mixed loss, severity, configuration, symmetry, age at onset, and progression.
3. Review newborn-screen results, congenital infection, prematurity, meningitis, trauma, noise, and ototoxic exposures.
4. Perform otoscopy and consider temporal-bone MRI/CT according to standard pediatric-SNHL indications; enlarged vestibular aqueduct is not TSPEAR-specific.
5. Examine teeth, hair, nails, skin, and sweating; obtain panoramic dental radiography when tooth agenesis is possible.

The 2026 case illustrates flat bilateral pure-tone thresholds and absent ABR responses, but these findings are not molecularly specific. (ahmadkhani2026anovelpathogenic pages 1-2)

### Genetic testing

**Preferred:** a comprehensive hereditary-hearing-loss panel, exome, or genome with SNV/indel, exon-level and larger CNV detection, mitochondrial analysis where indicated, and periodic reanalysis. CNVs are important generally: in one 686-person NSHL cohort, 15.2% carried at least one CNV in a deafness gene and CNVs contributed to 18.7% of solved cases. TSPEAR should not be tested or interpreted in isolation.

Trio WES/WGS can establish phase and identify alternate etiologies. Bowles et al. used exome or panel testing and found competing **TMPRSS3, GJB2, and GJB6** findings in every TSPEAR-biallelic person with hearing loss. (bowles2021tspearvariantsare pages 1-2)

CMA, karyotype, FISH, repeat-expansion testing, biopsy, proteomics, metabolomics, and liquid biopsy are not routine tests for isolated DFNB98. RNA studies may help resolve a suspected splice allele but are not validated diagnostics.

### Differential diagnosis

Priority genetic differentials include **GJB2/GJB6, STRC, OTOF, SLC26A4, TMPRSS3, OTOA, TMC1, MYO15A**, and many other ARNSHL genes. The nearby TMPRSS3 locus deserves special attention. Environmental differentials include congenital CMV/rubella, meningitis, ototoxicity, and noise. If dental/hair/sweat abnormalities are present, evaluate ECTD14 and other ectodermal-dysplasia genes, particularly **WNT10A, EDA, EDAR, and EDARADD**. (bowles2021tspearvariantsare pages 2-4, jackson2023clinicalgeneticepidemiologic pages 5-8)

### Screening

Universal newborn physiologic hearing screening remains appropriate regardless of genotype. At-risk relatives should receive audiology rather than genotype-only prediction. Once a credible familial diagnosis is established, cascade testing can identify carriers, but counseling must disclose disputed TSPEAR hearing validity.

## 11. Outcome and prognosis

No disease-specific mortality or reduced life expectancy is known; survival should be normal for isolated SNHL. Morbidity consists principally of persistent auditory disability and, without timely communication access, secondary speech/language, educational, and psychosocial consequences. No five- or ten-year survival statistics, prognostic biomarkers, validated progression predictors, or DFNB98-specific QoL scores exist.

Recovery of congenital severe/profound SNHL is not expected spontaneously. Functional outcome depends more on severity, age at intervention, communication access, rehabilitation, anatomy, and coexisting conditions than on an unvalidated TSPEAR genotype.

## 12. Treatment

There is **no TSPEAR-specific approved pharmacotherapy, gene therapy, CRISPR therapy, RNA therapy, cell therapy, or immunotherapy**, and the ClinicalTrials.gov search retrieved no relevant TSPEAR/DFNB98 trial.

Management follows standard SNHL practice:

- hearing aids for aidable residual hearing;
- cochlear implantation for appropriately evaluated severe-to-profound loss with inadequate hearing-aid benefit;
- speech-language/auditory rehabilitation;
- sign-language and/or other communication support according to family preference;
- educational accommodations and psychosocial support;
- treatment of middle-ear disease and protection from avoidable ototoxic/noise injury.

Suggested NCIt intervention concepts include **Hearing Aid**, **Cochlear Implantation**, **Audiologic Rehabilitation**, **Speech Therapy**, and **Genetic Counseling**; exact NCIt codes should be verified against the target terminology release. No genotype-specific response rate or adverse-event dataset exists.

## 13. Prevention

- **Primary:** the congenital genotype cannot be prevented after conception. Carrier/couple counseling, reproductive options, and avoidance of preventable auditory injury are relevant. Vaccination and infection prevention reduce non-genetic congenital/acquired deafness but are not TSPEAR-specific.
- **Secondary:** universal newborn hearing screening, rapid diagnostic audiology, and early communication intervention.
- **Tertiary:** hearing technology, rehabilitation, educational support, and monitoring residual hearing.
- **Reproductive genetics:** if a familial causal genotype is well established, prenatal diagnosis or PGT-M may be technically possible. For TSPEAR-only hearing-risk prediction, uncertainty about gene validity and penetrance must be explicit; decisions should not rest on the historical DFNB98 label alone.

## 14. Other species and natural disease

No naturally occurring veterinary TSPEAR deafness syndrome, breed predisposition, zoonosis, or cross-species transmission is established. TSPEAR is conserved across vertebrates. Its inferred Drosophila ortholog **Closca** participates in ECM-dependent sequestration of developmental morphogens; this comparative relationship supports an ectodermal-development function rather than proving auditory disease. (jackson2023clinicalgeneticepidemiologic pages 11-13)

Suggested taxa are **Homo sapiens—NCBI Taxon 9606**, **Mus musculus—10090**, **Danio rerio—7955**, and **Drosophila melanogaster—7227**. The condition is inherited, not infectious, and has no zoonotic potential.

## 15. Model organisms

### Cellular and organ-culture systems

Human keratinocyte knockdown, patient scalp tissue, and mouse hair-follicle organ culture support reduced Notch signaling and increased follicular epithelial apoptosis. These systems model ECTD14 hair/skin biology and do not reproduce hearing loss. (peled2016mutationsintspear pages 1-2)

### Mouse data

Mouse single-cell RNA-seq showed restricted Tspear expression in enamel-knot clusters and anagen hair-follicle keratinocytes. Earlier cochlear immunohistochemistry suggested basal hair-cell localization, but cochlear RNA-seq showed little or no transcript. No convincing Tspear-null mouse auditory phenotype was available in the core evidence. (bowles2021tspearvariantsare pages 2-4, jackson2023clinicalgeneticepidemiologic pages 11-13)

### Zebrafish knockout

Because zebrafish have **tspeara** and **tspearb**, Jackson et al. generated a CRISPR double knockout. Mutants were viable, developed thin, aberrantly mineralized and missing teeth, lacked normal fin branching, and had severely reduced fin regeneration. Tooth/bone expression changes included downregulation of **fgf1b, enam, scpp5, scpp7, mustn1a**, and **kcnk5a**, with upregulation of **dlx2b** and **cdkn1a**. The model recapitulates human ARED14 dental biology and suggests interaction with WNT10A, but no auditory phenotype was demonstrated. (jackson2023clinicalgeneticepidemiologic pages 13-14, jackson2023clinicalgeneticepidemiologic pages 11-13)

## Recent developments and authoritative interpretation

- **2023:** Jackson et al. supplied the strongest recent synthesis, integrating 30 human cases, 100KGP/gnomAD population data, AlphaFold, mouse single-cell expression, and zebrafish knockout experiments. Their direct conclusion was: **“At present, there is insufficient evidence to link TSPEAR variants as a cause of AR hearing loss.”** The same work robustly established ARED14 and quantified its predominantly dental phenotype. Published April 13, 2023; DOI: https://doi.org/10.1016/j.xhgg.2023.100186. (jackson2023clinicalgeneticepidemiologic pages 1-2, jackson2023clinicalgeneticepidemiologic pages 5-8)
- **2024:** Shi et al. reported a Chinese family with novel compound-heterozygous TSPEAR variants and AR hearing loss (Pediatric Investigation 8:313–315; DOI: https://doi.org/10.1002/ped4.12454). This provides limited family-level support but does not overcome contradictory cohorts or supply a validated auditory mechanism.
- **2026:** Ahmadkhani et al. reported one additional Iranian child with homozygous p.Ser223Leu and isolated profound SNHL. The authors themselves characterized an isolated hearing presentation as rare. DOI: https://doi.org/10.1186/s13256-025-05761-7. (ahmadkhani2026anovelpathogenic pages 1-2)

## Knowledge-base recommendation

Represent **MONDO:0013929/DFNB98** as a **historical or provisional disease entity with disputed TSPEAR causality**, not as an established molecular diagnosis. Store reported variants and hearing phenotypes as case-level evidence, with explicit conflicting evidence and alternative-gene review. Represent **TSPEAR–ECTD14/ARED14 (OMIM 618180)** separately as the established association. Key unavailable fields—true prevalence, penetrance, progression, validated cochlear mechanism, biomarkers, omics signatures, prognostic factors, and targeted therapies—should be recorded as **unknown/not established**, not inferred from general hereditary hearing loss.

References

1. (bowles2021tspearvariantsare pages 1-2): Bradley Bowles, Alejandro Ferrer, Carla J. Nishimura, Filippo Pinto e Vairo, Tristan Rey, Bruno Leheup, Jennifer Sullivan, Kelly Schoch, Nicholas Stong, Emanuele Agolini, Dario Cocciadiferro, Abigail Williams, Alex Cummings, Sara Loddo, Silvia Genovese, Chelsea Roadhouse, Kirsty McWalter, Ingrid M. Wentzensen, Chumei Li, Dusica Babovic‐Vuksanovic, Brendan C. Lanpher, Maria Lisa Dentici, Arun Ankala, J. Austin Hamm, Bruno Dallapiccola, Francesca Clementina Radio, Vandana Shashi, Benedicte Gérard, Agnes Bloch‐Zupan, Richard J. Smith, and Eric W. Klee. Tspear variants are primarily associated with ectodermal dysplasia and tooth agenesis but not hearing loss: a novel cohort study. American Journal of Medical Genetics. Part a, 185:2417-2433, May 2021. URL: https://doi.org/10.1002/ajmg.a.62347, doi:10.1002/ajmg.a.62347. This article has 27 citations and is from a peer-reviewed journal.

2. (jackson2023clinicalgeneticepidemiologic pages 5-8): Adam Jackson, Sheng-Jia Lin, Elizabeth A. Jones, Kate E. Chandler, David Orr, Celia Moss, Zahra Haider, Gavin Ryan, Simon Holden, Mike Harrison, Nigel Burrows, Wendy D. Jones, Mary Loveless, Cassidy Petree, Helen Stewart, Karen Low, Deirdre Donnelly, Simon Lovell, Konstantina Drosou, J.C. Ambrose, P. Arumugam, R. Bevers, M. Bleda, F. Boardman-Pretty, C.R. Boustred, H. Brittain, M.A. Brown, M.J. Caulfield, G.C. Chan, A. Giess, J.N. Griffin, A. Hamblin, S. Henderson, T.J.P. Hubbard, R. Jackson, L.J. Jones, D. Kasperaviciute, M. Kayikci, A. Kousathanas, L. Lahnstein, A. Lakey, S.E.A. Leigh, I.U.S. Leong, F.J. Lopez, F. Maleady-Crowe, M. McEntagart, F. Minneci, J. Mitchell, L. Moutsianas, M. Mueller, N. Murugaesu, A.C. Need, P. O‘Donovan, C.A. Odhams, C. Patch, D. Perez-Gil, M.B. Pereira, J. Pullinger, T. Rahim, A. Rendon, T. Rogers, K. Savage, K. Sawant, R.H. Scott, A. Siddiq, A. Sieghart, S.C. Smith, A. Sosinsky, A. Stuckey, M. Tanguy, A.L. Taylor Tavares, E.R.A. Thomas, S.R. Thompson, A. Tucci, M.J. Welland, E. Williams, K. Witkowska, S.M. Wood, M. Zarowiecki, Olaf Riess, Tobias B. Haack, Holm Graessner, Birte Zurek, Kornelia Ellwanger, Stephan Ossowski, German Demidov, Marc Sturm, Julia M. Schulze-Hentrich, Rebecca Schüle, Christoph Kessler, Melanie Wayand, Matthis Synofzik, Carlo Wilke, Andreas Traschütz, Ludger Schöls, Holger Hengel, Peter Heutink, Han Brunner, Hans Scheffer, Nicoline Hoogerbrugge, Alexander Hoischen, Peter A.C. ’t Hoen, Lisenka E.L.M. Vissers, Christian Gilissen, Wouter Steyaert, Karolis Sablauskas, Richarda M. de Voer, Erik-Jan Kamsteeg, Bart van de Warrenburg, Nienke van Os, Iris te Paske, Erik Janssen, Elke de Boer, Marloes Steehouwer, Burcu Yaldiz, Tjitske Kleefstra, Anthony J. Brookes, Colin Veal, Spencer Gibson, Marc Wadsley, Mehdi Mehtarizadeh, Umar Riaz, Greg Warren, Farid Yavari Dizjikan, Thomas Shorter, Ana Töpf, Volker Straub, Chiara Marini Bettolo, Sabine Specht, Jill Clayton-Smith, Siddharth Banka, Elizabeth Alexander, Adam Jackson, Laurence Faivre, Christel Thauvin, Antonio Vitobello, Anne-Sophie Denommé-Pichon, Yannis Duffourd, Emilie Tisserant, Ange-Line Bruel, Christine Peyron, Aurore Pélissier, Sergi Beltran, Ivo Glynne Gut, Steven Laurie, Davide Piscia, Leslie Matalonga, Anastasios Papakonstantinou, Gemma Bullich, Alberto Corvo, Carles Garcia, Marcos Fernandez-Callejo, Carles Hernández, Daniel Picó, Ida Paramonov, Hanns Lochmüller, Gulcin Gumus, Virginie Bros-Facer, Ana Rath, Marc Hanauer, Annie Olry, David Lagorce, Svitlana Havrylenko, Katia Izem, Fanny Rigour, Giovanni Stevanin, Alexandra Durr, Claire-Sophie Davoine, Léna Guillot-Noel, Anna Heinzmann, Giulia Coarelli, Gisèle Bonne, Teresinha Evangelista, Valérie Allamand, Isabelle Nelson, Rabah Ben Yaou, Corinne Metay, Bruno Eymard, Enzo Cohen, Antonio Atalaia, Tanya Stojkovic, Milan Macek, Marek Turnovec, Dana Thomasová, Radka Pourová Kremliková, Vera Franková, Markéta Havlovicová, Vlastimil Kremlik, Helen Parkinson, Thomas Keane, Dylan Spalding, Alexander Senf, Peter Robinson, Daniel Danis, Glenn Robert, Alessia Costa, Christine Patch, Mike Hanna, Henry Houlden, Mary Reilly, Jana Vandrovcova, Francesco Muntoni, Irina Zaharieva, Anna Sarkozy, Vincent Timmerman, Jonathan Baets, Liedewei Van de Vondel, Danique Beijer, Peter de Jonghe, Vincenzo Nigro, Sandro Banfi, Annalaura Torella, Francesco Musacchia, Giulio Piluso, Alessandra Ferlini, Rita Selvatici, Rachele Rossi, Marcella Neri, Stefan Aretz, Isabel Spier, Anna Katharina Sommer, Sophia Peters, Carla Oliveira, Jose Garcia Pelaez, Ana Rita Matos, Celina São José, Marta Ferreira, Irene Gullo, Susana Fernandes, Luzia Garrido, Pedro Ferreira, Fátima Carneiro, Morris A. Swertz, Lennart Johansson, Joeri K. van der Velde, Gerben van der Vries, Pieter B. Neerincx, Dieuwke Roelofs-Prins, Sebastian Köhler, Alison Metcalfe, Alain Verloes, Séverine Drunat, Caroline Rooryck, Aurelien Trimouille, Raffaele Castello, Manuela Morleo, Michele Pinelli, Alessandra Varavallo, Manuel Posada De la Paz, Eva Bermejo Sánchez, Estrella López Martín, Beatriz Martínez Delgado, F. Javier Alonso García de la Rosa, Andrea Ciolfi, Bruno Dallapiccola, Simone Pizzi, Francesca Clementina Radio, Marco Tartaglia, Alessandra Renieri, Elisa Benetti, Peter Balicza, Maria Judit Molnar, Ales Maver, Borut Peterlin, Alexander Münchau, Katja Lohmann, Rebecca Herzog, Martje Pauly, Alfons Macaya, Anna Marcé-Grau, Andres Nascimiento Osorio, Daniel Natera de Benito, Hanns Lochmüller, Rachel Thompson, Kiran Polavarapu, David Beeson, Judith Cossins, Pedro M. Rodriguez Cruz, Peter Hackman, Mridul Johari, Marco Savarese, Bjarne Udd, Rita Horvath, Gabriel Capella, Laura Valle, Elke Holinski-Feder, Andreas Laner, Verena Steinke-Lange, Evelin Schröck, Andreas Rump, Gaurav K. Varshney, and Siddharth Banka. Clinical, genetic, epidemiologic, evolutionary, and functional delineation of tspear-related autosomal recessive ectodermal dysplasia 14. Apr 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100186, doi:10.1016/j.xhgg.2023.100186. This article has 13 citations and is from a peer-reviewed journal.

3. (bowles2021tspearvariantsare pages 2-4): Bradley Bowles, Alejandro Ferrer, Carla J. Nishimura, Filippo Pinto e Vairo, Tristan Rey, Bruno Leheup, Jennifer Sullivan, Kelly Schoch, Nicholas Stong, Emanuele Agolini, Dario Cocciadiferro, Abigail Williams, Alex Cummings, Sara Loddo, Silvia Genovese, Chelsea Roadhouse, Kirsty McWalter, Ingrid M. Wentzensen, Chumei Li, Dusica Babovic‐Vuksanovic, Brendan C. Lanpher, Maria Lisa Dentici, Arun Ankala, J. Austin Hamm, Bruno Dallapiccola, Francesca Clementina Radio, Vandana Shashi, Benedicte Gérard, Agnes Bloch‐Zupan, Richard J. Smith, and Eric W. Klee. Tspear variants are primarily associated with ectodermal dysplasia and tooth agenesis but not hearing loss: a novel cohort study. American Journal of Medical Genetics. Part a, 185:2417-2433, May 2021. URL: https://doi.org/10.1002/ajmg.a.62347, doi:10.1002/ajmg.a.62347. This article has 27 citations and is from a peer-reviewed journal.

4. (bowles2021tspearvariantsare pages 10-11): Bradley Bowles, Alejandro Ferrer, Carla J. Nishimura, Filippo Pinto e Vairo, Tristan Rey, Bruno Leheup, Jennifer Sullivan, Kelly Schoch, Nicholas Stong, Emanuele Agolini, Dario Cocciadiferro, Abigail Williams, Alex Cummings, Sara Loddo, Silvia Genovese, Chelsea Roadhouse, Kirsty McWalter, Ingrid M. Wentzensen, Chumei Li, Dusica Babovic‐Vuksanovic, Brendan C. Lanpher, Maria Lisa Dentici, Arun Ankala, J. Austin Hamm, Bruno Dallapiccola, Francesca Clementina Radio, Vandana Shashi, Benedicte Gérard, Agnes Bloch‐Zupan, Richard J. Smith, and Eric W. Klee. Tspear variants are primarily associated with ectodermal dysplasia and tooth agenesis but not hearing loss: a novel cohort study. American Journal of Medical Genetics. Part a, 185:2417-2433, May 2021. URL: https://doi.org/10.1002/ajmg.a.62347, doi:10.1002/ajmg.a.62347. This article has 27 citations and is from a peer-reviewed journal.

5. (jackson2023clinicalgeneticepidemiologic pages 1-2): Adam Jackson, Sheng-Jia Lin, Elizabeth A. Jones, Kate E. Chandler, David Orr, Celia Moss, Zahra Haider, Gavin Ryan, Simon Holden, Mike Harrison, Nigel Burrows, Wendy D. Jones, Mary Loveless, Cassidy Petree, Helen Stewart, Karen Low, Deirdre Donnelly, Simon Lovell, Konstantina Drosou, J.C. Ambrose, P. Arumugam, R. Bevers, M. Bleda, F. Boardman-Pretty, C.R. Boustred, H. Brittain, M.A. Brown, M.J. Caulfield, G.C. Chan, A. Giess, J.N. Griffin, A. Hamblin, S. Henderson, T.J.P. Hubbard, R. Jackson, L.J. Jones, D. Kasperaviciute, M. Kayikci, A. Kousathanas, L. Lahnstein, A. Lakey, S.E.A. Leigh, I.U.S. Leong, F.J. Lopez, F. Maleady-Crowe, M. McEntagart, F. Minneci, J. Mitchell, L. Moutsianas, M. Mueller, N. Murugaesu, A.C. Need, P. O‘Donovan, C.A. Odhams, C. Patch, D. Perez-Gil, M.B. Pereira, J. Pullinger, T. Rahim, A. Rendon, T. Rogers, K. Savage, K. Sawant, R.H. Scott, A. Siddiq, A. Sieghart, S.C. Smith, A. Sosinsky, A. Stuckey, M. Tanguy, A.L. Taylor Tavares, E.R.A. Thomas, S.R. Thompson, A. Tucci, M.J. Welland, E. Williams, K. Witkowska, S.M. Wood, M. Zarowiecki, Olaf Riess, Tobias B. Haack, Holm Graessner, Birte Zurek, Kornelia Ellwanger, Stephan Ossowski, German Demidov, Marc Sturm, Julia M. Schulze-Hentrich, Rebecca Schüle, Christoph Kessler, Melanie Wayand, Matthis Synofzik, Carlo Wilke, Andreas Traschütz, Ludger Schöls, Holger Hengel, Peter Heutink, Han Brunner, Hans Scheffer, Nicoline Hoogerbrugge, Alexander Hoischen, Peter A.C. ’t Hoen, Lisenka E.L.M. Vissers, Christian Gilissen, Wouter Steyaert, Karolis Sablauskas, Richarda M. de Voer, Erik-Jan Kamsteeg, Bart van de Warrenburg, Nienke van Os, Iris te Paske, Erik Janssen, Elke de Boer, Marloes Steehouwer, Burcu Yaldiz, Tjitske Kleefstra, Anthony J. Brookes, Colin Veal, Spencer Gibson, Marc Wadsley, Mehdi Mehtarizadeh, Umar Riaz, Greg Warren, Farid Yavari Dizjikan, Thomas Shorter, Ana Töpf, Volker Straub, Chiara Marini Bettolo, Sabine Specht, Jill Clayton-Smith, Siddharth Banka, Elizabeth Alexander, Adam Jackson, Laurence Faivre, Christel Thauvin, Antonio Vitobello, Anne-Sophie Denommé-Pichon, Yannis Duffourd, Emilie Tisserant, Ange-Line Bruel, Christine Peyron, Aurore Pélissier, Sergi Beltran, Ivo Glynne Gut, Steven Laurie, Davide Piscia, Leslie Matalonga, Anastasios Papakonstantinou, Gemma Bullich, Alberto Corvo, Carles Garcia, Marcos Fernandez-Callejo, Carles Hernández, Daniel Picó, Ida Paramonov, Hanns Lochmüller, Gulcin Gumus, Virginie Bros-Facer, Ana Rath, Marc Hanauer, Annie Olry, David Lagorce, Svitlana Havrylenko, Katia Izem, Fanny Rigour, Giovanni Stevanin, Alexandra Durr, Claire-Sophie Davoine, Léna Guillot-Noel, Anna Heinzmann, Giulia Coarelli, Gisèle Bonne, Teresinha Evangelista, Valérie Allamand, Isabelle Nelson, Rabah Ben Yaou, Corinne Metay, Bruno Eymard, Enzo Cohen, Antonio Atalaia, Tanya Stojkovic, Milan Macek, Marek Turnovec, Dana Thomasová, Radka Pourová Kremliková, Vera Franková, Markéta Havlovicová, Vlastimil Kremlik, Helen Parkinson, Thomas Keane, Dylan Spalding, Alexander Senf, Peter Robinson, Daniel Danis, Glenn Robert, Alessia Costa, Christine Patch, Mike Hanna, Henry Houlden, Mary Reilly, Jana Vandrovcova, Francesco Muntoni, Irina Zaharieva, Anna Sarkozy, Vincent Timmerman, Jonathan Baets, Liedewei Van de Vondel, Danique Beijer, Peter de Jonghe, Vincenzo Nigro, Sandro Banfi, Annalaura Torella, Francesco Musacchia, Giulio Piluso, Alessandra Ferlini, Rita Selvatici, Rachele Rossi, Marcella Neri, Stefan Aretz, Isabel Spier, Anna Katharina Sommer, Sophia Peters, Carla Oliveira, Jose Garcia Pelaez, Ana Rita Matos, Celina São José, Marta Ferreira, Irene Gullo, Susana Fernandes, Luzia Garrido, Pedro Ferreira, Fátima Carneiro, Morris A. Swertz, Lennart Johansson, Joeri K. van der Velde, Gerben van der Vries, Pieter B. Neerincx, Dieuwke Roelofs-Prins, Sebastian Köhler, Alison Metcalfe, Alain Verloes, Séverine Drunat, Caroline Rooryck, Aurelien Trimouille, Raffaele Castello, Manuela Morleo, Michele Pinelli, Alessandra Varavallo, Manuel Posada De la Paz, Eva Bermejo Sánchez, Estrella López Martín, Beatriz Martínez Delgado, F. Javier Alonso García de la Rosa, Andrea Ciolfi, Bruno Dallapiccola, Simone Pizzi, Francesca Clementina Radio, Marco Tartaglia, Alessandra Renieri, Elisa Benetti, Peter Balicza, Maria Judit Molnar, Ales Maver, Borut Peterlin, Alexander Münchau, Katja Lohmann, Rebecca Herzog, Martje Pauly, Alfons Macaya, Anna Marcé-Grau, Andres Nascimiento Osorio, Daniel Natera de Benito, Hanns Lochmüller, Rachel Thompson, Kiran Polavarapu, David Beeson, Judith Cossins, Pedro M. Rodriguez Cruz, Peter Hackman, Mridul Johari, Marco Savarese, Bjarne Udd, Rita Horvath, Gabriel Capella, Laura Valle, Elke Holinski-Feder, Andreas Laner, Verena Steinke-Lange, Evelin Schröck, Andreas Rump, Gaurav K. Varshney, and Siddharth Banka. Clinical, genetic, epidemiologic, evolutionary, and functional delineation of tspear-related autosomal recessive ectodermal dysplasia 14. Apr 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100186, doi:10.1016/j.xhgg.2023.100186. This article has 13 citations and is from a peer-reviewed journal.

6. (jackson2023clinicalgeneticepidemiologic pages 11-13): Adam Jackson, Sheng-Jia Lin, Elizabeth A. Jones, Kate E. Chandler, David Orr, Celia Moss, Zahra Haider, Gavin Ryan, Simon Holden, Mike Harrison, Nigel Burrows, Wendy D. Jones, Mary Loveless, Cassidy Petree, Helen Stewart, Karen Low, Deirdre Donnelly, Simon Lovell, Konstantina Drosou, J.C. Ambrose, P. Arumugam, R. Bevers, M. Bleda, F. Boardman-Pretty, C.R. Boustred, H. Brittain, M.A. Brown, M.J. Caulfield, G.C. Chan, A. Giess, J.N. Griffin, A. Hamblin, S. Henderson, T.J.P. Hubbard, R. Jackson, L.J. Jones, D. Kasperaviciute, M. Kayikci, A. Kousathanas, L. Lahnstein, A. Lakey, S.E.A. Leigh, I.U.S. Leong, F.J. Lopez, F. Maleady-Crowe, M. McEntagart, F. Minneci, J. Mitchell, L. Moutsianas, M. Mueller, N. Murugaesu, A.C. Need, P. O‘Donovan, C.A. Odhams, C. Patch, D. Perez-Gil, M.B. Pereira, J. Pullinger, T. Rahim, A. Rendon, T. Rogers, K. Savage, K. Sawant, R.H. Scott, A. Siddiq, A. Sieghart, S.C. Smith, A. Sosinsky, A. Stuckey, M. Tanguy, A.L. Taylor Tavares, E.R.A. Thomas, S.R. Thompson, A. Tucci, M.J. Welland, E. Williams, K. Witkowska, S.M. Wood, M. Zarowiecki, Olaf Riess, Tobias B. Haack, Holm Graessner, Birte Zurek, Kornelia Ellwanger, Stephan Ossowski, German Demidov, Marc Sturm, Julia M. Schulze-Hentrich, Rebecca Schüle, Christoph Kessler, Melanie Wayand, Matthis Synofzik, Carlo Wilke, Andreas Traschütz, Ludger Schöls, Holger Hengel, Peter Heutink, Han Brunner, Hans Scheffer, Nicoline Hoogerbrugge, Alexander Hoischen, Peter A.C. ’t Hoen, Lisenka E.L.M. Vissers, Christian Gilissen, Wouter Steyaert, Karolis Sablauskas, Richarda M. de Voer, Erik-Jan Kamsteeg, Bart van de Warrenburg, Nienke van Os, Iris te Paske, Erik Janssen, Elke de Boer, Marloes Steehouwer, Burcu Yaldiz, Tjitske Kleefstra, Anthony J. Brookes, Colin Veal, Spencer Gibson, Marc Wadsley, Mehdi Mehtarizadeh, Umar Riaz, Greg Warren, Farid Yavari Dizjikan, Thomas Shorter, Ana Töpf, Volker Straub, Chiara Marini Bettolo, Sabine Specht, Jill Clayton-Smith, Siddharth Banka, Elizabeth Alexander, Adam Jackson, Laurence Faivre, Christel Thauvin, Antonio Vitobello, Anne-Sophie Denommé-Pichon, Yannis Duffourd, Emilie Tisserant, Ange-Line Bruel, Christine Peyron, Aurore Pélissier, Sergi Beltran, Ivo Glynne Gut, Steven Laurie, Davide Piscia, Leslie Matalonga, Anastasios Papakonstantinou, Gemma Bullich, Alberto Corvo, Carles Garcia, Marcos Fernandez-Callejo, Carles Hernández, Daniel Picó, Ida Paramonov, Hanns Lochmüller, Gulcin Gumus, Virginie Bros-Facer, Ana Rath, Marc Hanauer, Annie Olry, David Lagorce, Svitlana Havrylenko, Katia Izem, Fanny Rigour, Giovanni Stevanin, Alexandra Durr, Claire-Sophie Davoine, Léna Guillot-Noel, Anna Heinzmann, Giulia Coarelli, Gisèle Bonne, Teresinha Evangelista, Valérie Allamand, Isabelle Nelson, Rabah Ben Yaou, Corinne Metay, Bruno Eymard, Enzo Cohen, Antonio Atalaia, Tanya Stojkovic, Milan Macek, Marek Turnovec, Dana Thomasová, Radka Pourová Kremliková, Vera Franková, Markéta Havlovicová, Vlastimil Kremlik, Helen Parkinson, Thomas Keane, Dylan Spalding, Alexander Senf, Peter Robinson, Daniel Danis, Glenn Robert, Alessia Costa, Christine Patch, Mike Hanna, Henry Houlden, Mary Reilly, Jana Vandrovcova, Francesco Muntoni, Irina Zaharieva, Anna Sarkozy, Vincent Timmerman, Jonathan Baets, Liedewei Van de Vondel, Danique Beijer, Peter de Jonghe, Vincenzo Nigro, Sandro Banfi, Annalaura Torella, Francesco Musacchia, Giulio Piluso, Alessandra Ferlini, Rita Selvatici, Rachele Rossi, Marcella Neri, Stefan Aretz, Isabel Spier, Anna Katharina Sommer, Sophia Peters, Carla Oliveira, Jose Garcia Pelaez, Ana Rita Matos, Celina São José, Marta Ferreira, Irene Gullo, Susana Fernandes, Luzia Garrido, Pedro Ferreira, Fátima Carneiro, Morris A. Swertz, Lennart Johansson, Joeri K. van der Velde, Gerben van der Vries, Pieter B. Neerincx, Dieuwke Roelofs-Prins, Sebastian Köhler, Alison Metcalfe, Alain Verloes, Séverine Drunat, Caroline Rooryck, Aurelien Trimouille, Raffaele Castello, Manuela Morleo, Michele Pinelli, Alessandra Varavallo, Manuel Posada De la Paz, Eva Bermejo Sánchez, Estrella López Martín, Beatriz Martínez Delgado, F. Javier Alonso García de la Rosa, Andrea Ciolfi, Bruno Dallapiccola, Simone Pizzi, Francesca Clementina Radio, Marco Tartaglia, Alessandra Renieri, Elisa Benetti, Peter Balicza, Maria Judit Molnar, Ales Maver, Borut Peterlin, Alexander Münchau, Katja Lohmann, Rebecca Herzog, Martje Pauly, Alfons Macaya, Anna Marcé-Grau, Andres Nascimiento Osorio, Daniel Natera de Benito, Hanns Lochmüller, Rachel Thompson, Kiran Polavarapu, David Beeson, Judith Cossins, Pedro M. Rodriguez Cruz, Peter Hackman, Mridul Johari, Marco Savarese, Bjarne Udd, Rita Horvath, Gabriel Capella, Laura Valle, Elke Holinski-Feder, Andreas Laner, Verena Steinke-Lange, Evelin Schröck, Andreas Rump, Gaurav K. Varshney, and Siddharth Banka. Clinical, genetic, epidemiologic, evolutionary, and functional delineation of tspear-related autosomal recessive ectodermal dysplasia 14. Apr 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100186, doi:10.1016/j.xhgg.2023.100186. This article has 13 citations and is from a peer-reviewed journal.

7. (jackson2023clinicalgeneticepidemiologic pages 13-14): Adam Jackson, Sheng-Jia Lin, Elizabeth A. Jones, Kate E. Chandler, David Orr, Celia Moss, Zahra Haider, Gavin Ryan, Simon Holden, Mike Harrison, Nigel Burrows, Wendy D. Jones, Mary Loveless, Cassidy Petree, Helen Stewart, Karen Low, Deirdre Donnelly, Simon Lovell, Konstantina Drosou, J.C. Ambrose, P. Arumugam, R. Bevers, M. Bleda, F. Boardman-Pretty, C.R. Boustred, H. Brittain, M.A. Brown, M.J. Caulfield, G.C. Chan, A. Giess, J.N. Griffin, A. Hamblin, S. Henderson, T.J.P. Hubbard, R. Jackson, L.J. Jones, D. Kasperaviciute, M. Kayikci, A. Kousathanas, L. Lahnstein, A. Lakey, S.E.A. Leigh, I.U.S. Leong, F.J. Lopez, F. Maleady-Crowe, M. McEntagart, F. Minneci, J. Mitchell, L. Moutsianas, M. Mueller, N. Murugaesu, A.C. Need, P. O‘Donovan, C.A. Odhams, C. Patch, D. Perez-Gil, M.B. Pereira, J. Pullinger, T. Rahim, A. Rendon, T. Rogers, K. Savage, K. Sawant, R.H. Scott, A. Siddiq, A. Sieghart, S.C. Smith, A. Sosinsky, A. Stuckey, M. Tanguy, A.L. Taylor Tavares, E.R.A. Thomas, S.R. Thompson, A. Tucci, M.J. Welland, E. Williams, K. Witkowska, S.M. Wood, M. Zarowiecki, Olaf Riess, Tobias B. Haack, Holm Graessner, Birte Zurek, Kornelia Ellwanger, Stephan Ossowski, German Demidov, Marc Sturm, Julia M. Schulze-Hentrich, Rebecca Schüle, Christoph Kessler, Melanie Wayand, Matthis Synofzik, Carlo Wilke, Andreas Traschütz, Ludger Schöls, Holger Hengel, Peter Heutink, Han Brunner, Hans Scheffer, Nicoline Hoogerbrugge, Alexander Hoischen, Peter A.C. ’t Hoen, Lisenka E.L.M. Vissers, Christian Gilissen, Wouter Steyaert, Karolis Sablauskas, Richarda M. de Voer, Erik-Jan Kamsteeg, Bart van de Warrenburg, Nienke van Os, Iris te Paske, Erik Janssen, Elke de Boer, Marloes Steehouwer, Burcu Yaldiz, Tjitske Kleefstra, Anthony J. Brookes, Colin Veal, Spencer Gibson, Marc Wadsley, Mehdi Mehtarizadeh, Umar Riaz, Greg Warren, Farid Yavari Dizjikan, Thomas Shorter, Ana Töpf, Volker Straub, Chiara Marini Bettolo, Sabine Specht, Jill Clayton-Smith, Siddharth Banka, Elizabeth Alexander, Adam Jackson, Laurence Faivre, Christel Thauvin, Antonio Vitobello, Anne-Sophie Denommé-Pichon, Yannis Duffourd, Emilie Tisserant, Ange-Line Bruel, Christine Peyron, Aurore Pélissier, Sergi Beltran, Ivo Glynne Gut, Steven Laurie, Davide Piscia, Leslie Matalonga, Anastasios Papakonstantinou, Gemma Bullich, Alberto Corvo, Carles Garcia, Marcos Fernandez-Callejo, Carles Hernández, Daniel Picó, Ida Paramonov, Hanns Lochmüller, Gulcin Gumus, Virginie Bros-Facer, Ana Rath, Marc Hanauer, Annie Olry, David Lagorce, Svitlana Havrylenko, Katia Izem, Fanny Rigour, Giovanni Stevanin, Alexandra Durr, Claire-Sophie Davoine, Léna Guillot-Noel, Anna Heinzmann, Giulia Coarelli, Gisèle Bonne, Teresinha Evangelista, Valérie Allamand, Isabelle Nelson, Rabah Ben Yaou, Corinne Metay, Bruno Eymard, Enzo Cohen, Antonio Atalaia, Tanya Stojkovic, Milan Macek, Marek Turnovec, Dana Thomasová, Radka Pourová Kremliková, Vera Franková, Markéta Havlovicová, Vlastimil Kremlik, Helen Parkinson, Thomas Keane, Dylan Spalding, Alexander Senf, Peter Robinson, Daniel Danis, Glenn Robert, Alessia Costa, Christine Patch, Mike Hanna, Henry Houlden, Mary Reilly, Jana Vandrovcova, Francesco Muntoni, Irina Zaharieva, Anna Sarkozy, Vincent Timmerman, Jonathan Baets, Liedewei Van de Vondel, Danique Beijer, Peter de Jonghe, Vincenzo Nigro, Sandro Banfi, Annalaura Torella, Francesco Musacchia, Giulio Piluso, Alessandra Ferlini, Rita Selvatici, Rachele Rossi, Marcella Neri, Stefan Aretz, Isabel Spier, Anna Katharina Sommer, Sophia Peters, Carla Oliveira, Jose Garcia Pelaez, Ana Rita Matos, Celina São José, Marta Ferreira, Irene Gullo, Susana Fernandes, Luzia Garrido, Pedro Ferreira, Fátima Carneiro, Morris A. Swertz, Lennart Johansson, Joeri K. van der Velde, Gerben van der Vries, Pieter B. Neerincx, Dieuwke Roelofs-Prins, Sebastian Köhler, Alison Metcalfe, Alain Verloes, Séverine Drunat, Caroline Rooryck, Aurelien Trimouille, Raffaele Castello, Manuela Morleo, Michele Pinelli, Alessandra Varavallo, Manuel Posada De la Paz, Eva Bermejo Sánchez, Estrella López Martín, Beatriz Martínez Delgado, F. Javier Alonso García de la Rosa, Andrea Ciolfi, Bruno Dallapiccola, Simone Pizzi, Francesca Clementina Radio, Marco Tartaglia, Alessandra Renieri, Elisa Benetti, Peter Balicza, Maria Judit Molnar, Ales Maver, Borut Peterlin, Alexander Münchau, Katja Lohmann, Rebecca Herzog, Martje Pauly, Alfons Macaya, Anna Marcé-Grau, Andres Nascimiento Osorio, Daniel Natera de Benito, Hanns Lochmüller, Rachel Thompson, Kiran Polavarapu, David Beeson, Judith Cossins, Pedro M. Rodriguez Cruz, Peter Hackman, Mridul Johari, Marco Savarese, Bjarne Udd, Rita Horvath, Gabriel Capella, Laura Valle, Elke Holinski-Feder, Andreas Laner, Verena Steinke-Lange, Evelin Schröck, Andreas Rump, Gaurav K. Varshney, and Siddharth Banka. Clinical, genetic, epidemiologic, evolutionary, and functional delineation of tspear-related autosomal recessive ectodermal dysplasia 14. Apr 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100186, doi:10.1016/j.xhgg.2023.100186. This article has 13 citations and is from a peer-reviewed journal.

8. (jackson2023clinicalgeneticepidemiologic pages 14-15): Adam Jackson, Sheng-Jia Lin, Elizabeth A. Jones, Kate E. Chandler, David Orr, Celia Moss, Zahra Haider, Gavin Ryan, Simon Holden, Mike Harrison, Nigel Burrows, Wendy D. Jones, Mary Loveless, Cassidy Petree, Helen Stewart, Karen Low, Deirdre Donnelly, Simon Lovell, Konstantina Drosou, J.C. Ambrose, P. Arumugam, R. Bevers, M. Bleda, F. Boardman-Pretty, C.R. Boustred, H. Brittain, M.A. Brown, M.J. Caulfield, G.C. Chan, A. Giess, J.N. Griffin, A. Hamblin, S. Henderson, T.J.P. Hubbard, R. Jackson, L.J. Jones, D. Kasperaviciute, M. Kayikci, A. Kousathanas, L. Lahnstein, A. Lakey, S.E.A. Leigh, I.U.S. Leong, F.J. Lopez, F. Maleady-Crowe, M. McEntagart, F. Minneci, J. Mitchell, L. Moutsianas, M. Mueller, N. Murugaesu, A.C. Need, P. O‘Donovan, C.A. Odhams, C. Patch, D. Perez-Gil, M.B. Pereira, J. Pullinger, T. Rahim, A. Rendon, T. Rogers, K. Savage, K. Sawant, R.H. Scott, A. Siddiq, A. Sieghart, S.C. Smith, A. Sosinsky, A. Stuckey, M. Tanguy, A.L. Taylor Tavares, E.R.A. Thomas, S.R. Thompson, A. Tucci, M.J. Welland, E. Williams, K. Witkowska, S.M. Wood, M. Zarowiecki, Olaf Riess, Tobias B. Haack, Holm Graessner, Birte Zurek, Kornelia Ellwanger, Stephan Ossowski, German Demidov, Marc Sturm, Julia M. Schulze-Hentrich, Rebecca Schüle, Christoph Kessler, Melanie Wayand, Matthis Synofzik, Carlo Wilke, Andreas Traschütz, Ludger Schöls, Holger Hengel, Peter Heutink, Han Brunner, Hans Scheffer, Nicoline Hoogerbrugge, Alexander Hoischen, Peter A.C. ’t Hoen, Lisenka E.L.M. Vissers, Christian Gilissen, Wouter Steyaert, Karolis Sablauskas, Richarda M. de Voer, Erik-Jan Kamsteeg, Bart van de Warrenburg, Nienke van Os, Iris te Paske, Erik Janssen, Elke de Boer, Marloes Steehouwer, Burcu Yaldiz, Tjitske Kleefstra, Anthony J. Brookes, Colin Veal, Spencer Gibson, Marc Wadsley, Mehdi Mehtarizadeh, Umar Riaz, Greg Warren, Farid Yavari Dizjikan, Thomas Shorter, Ana Töpf, Volker Straub, Chiara Marini Bettolo, Sabine Specht, Jill Clayton-Smith, Siddharth Banka, Elizabeth Alexander, Adam Jackson, Laurence Faivre, Christel Thauvin, Antonio Vitobello, Anne-Sophie Denommé-Pichon, Yannis Duffourd, Emilie Tisserant, Ange-Line Bruel, Christine Peyron, Aurore Pélissier, Sergi Beltran, Ivo Glynne Gut, Steven Laurie, Davide Piscia, Leslie Matalonga, Anastasios Papakonstantinou, Gemma Bullich, Alberto Corvo, Carles Garcia, Marcos Fernandez-Callejo, Carles Hernández, Daniel Picó, Ida Paramonov, Hanns Lochmüller, Gulcin Gumus, Virginie Bros-Facer, Ana Rath, Marc Hanauer, Annie Olry, David Lagorce, Svitlana Havrylenko, Katia Izem, Fanny Rigour, Giovanni Stevanin, Alexandra Durr, Claire-Sophie Davoine, Léna Guillot-Noel, Anna Heinzmann, Giulia Coarelli, Gisèle Bonne, Teresinha Evangelista, Valérie Allamand, Isabelle Nelson, Rabah Ben Yaou, Corinne Metay, Bruno Eymard, Enzo Cohen, Antonio Atalaia, Tanya Stojkovic, Milan Macek, Marek Turnovec, Dana Thomasová, Radka Pourová Kremliková, Vera Franková, Markéta Havlovicová, Vlastimil Kremlik, Helen Parkinson, Thomas Keane, Dylan Spalding, Alexander Senf, Peter Robinson, Daniel Danis, Glenn Robert, Alessia Costa, Christine Patch, Mike Hanna, Henry Houlden, Mary Reilly, Jana Vandrovcova, Francesco Muntoni, Irina Zaharieva, Anna Sarkozy, Vincent Timmerman, Jonathan Baets, Liedewei Van de Vondel, Danique Beijer, Peter de Jonghe, Vincenzo Nigro, Sandro Banfi, Annalaura Torella, Francesco Musacchia, Giulio Piluso, Alessandra Ferlini, Rita Selvatici, Rachele Rossi, Marcella Neri, Stefan Aretz, Isabel Spier, Anna Katharina Sommer, Sophia Peters, Carla Oliveira, Jose Garcia Pelaez, Ana Rita Matos, Celina São José, Marta Ferreira, Irene Gullo, Susana Fernandes, Luzia Garrido, Pedro Ferreira, Fátima Carneiro, Morris A. Swertz, Lennart Johansson, Joeri K. van der Velde, Gerben van der Vries, Pieter B. Neerincx, Dieuwke Roelofs-Prins, Sebastian Köhler, Alison Metcalfe, Alain Verloes, Séverine Drunat, Caroline Rooryck, Aurelien Trimouille, Raffaele Castello, Manuela Morleo, Michele Pinelli, Alessandra Varavallo, Manuel Posada De la Paz, Eva Bermejo Sánchez, Estrella López Martín, Beatriz Martínez Delgado, F. Javier Alonso García de la Rosa, Andrea Ciolfi, Bruno Dallapiccola, Simone Pizzi, Francesca Clementina Radio, Marco Tartaglia, Alessandra Renieri, Elisa Benetti, Peter Balicza, Maria Judit Molnar, Ales Maver, Borut Peterlin, Alexander Münchau, Katja Lohmann, Rebecca Herzog, Martje Pauly, Alfons Macaya, Anna Marcé-Grau, Andres Nascimiento Osorio, Daniel Natera de Benito, Hanns Lochmüller, Rachel Thompson, Kiran Polavarapu, David Beeson, Judith Cossins, Pedro M. Rodriguez Cruz, Peter Hackman, Mridul Johari, Marco Savarese, Bjarne Udd, Rita Horvath, Gabriel Capella, Laura Valle, Elke Holinski-Feder, Andreas Laner, Verena Steinke-Lange, Evelin Schröck, Andreas Rump, Gaurav K. Varshney, and Siddharth Banka. Clinical, genetic, epidemiologic, evolutionary, and functional delineation of tspear-related autosomal recessive ectodermal dysplasia 14. Apr 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100186, doi:10.1016/j.xhgg.2023.100186. This article has 13 citations and is from a peer-reviewed journal.

9. (ahmadkhani2026anovelpathogenic pages 1-2): Alireza Ahmadkhani, Erfan Taherifard, Sina Zoghi, Hossein Jafari Khamirani, Mohammadreza Ahmadkhani, and Seyed Alireza Dastgheib. A novel pathogenic mutation in tspear associated with sensorineural hearing loss: a case report and review of the literature. Journal of Medical Case Reports, Jan 2026. URL: https://doi.org/10.1186/s13256-025-05761-7, doi:10.1186/s13256-025-05761-7. This article has 0 citations and is from a peer-reviewed journal.

10. (peled2016mutationsintspear pages 1-2): Alon Peled, Ofer Sarig, Liat Samuelov, Marta Bertolini, Limor Ziv, Daphna Weissglas-Volkov, Marina Eskin-Schwartz, Christopher A. Adase, Natalia Malchin, Ron Bochner, Gilad Fainberg, Ilan Goldberg, Koji Sugawara, Avital Baniel, Daisuke Tsuruta, Chen Luxenburg, Noam Adir, Olivier Duverger, Maria Morasso, Stavit Shalev, Richard L. Gallo, Noam Shomron, Ralf Paus, and Eli Sprecher. Mutations in tspear, encoding a regulator of notch signaling, affect tooth and hair follicle morphogenesis. PLOS Genetics, 12:e1006369, Oct 2016. URL: https://doi.org/10.1371/journal.pgen.1006369, doi:10.1371/journal.pgen.1006369. This article has 70 citations and is from a domain leading peer-reviewed journal.

11. (jackson2023clinicalgeneticepidemiologic pages 8-11): Adam Jackson, Sheng-Jia Lin, Elizabeth A. Jones, Kate E. Chandler, David Orr, Celia Moss, Zahra Haider, Gavin Ryan, Simon Holden, Mike Harrison, Nigel Burrows, Wendy D. Jones, Mary Loveless, Cassidy Petree, Helen Stewart, Karen Low, Deirdre Donnelly, Simon Lovell, Konstantina Drosou, J.C. Ambrose, P. Arumugam, R. Bevers, M. Bleda, F. Boardman-Pretty, C.R. Boustred, H. Brittain, M.A. Brown, M.J. Caulfield, G.C. Chan, A. Giess, J.N. Griffin, A. Hamblin, S. Henderson, T.J.P. Hubbard, R. Jackson, L.J. Jones, D. Kasperaviciute, M. Kayikci, A. Kousathanas, L. Lahnstein, A. Lakey, S.E.A. Leigh, I.U.S. Leong, F.J. Lopez, F. Maleady-Crowe, M. McEntagart, F. Minneci, J. Mitchell, L. Moutsianas, M. Mueller, N. Murugaesu, A.C. Need, P. O‘Donovan, C.A. Odhams, C. Patch, D. Perez-Gil, M.B. Pereira, J. Pullinger, T. Rahim, A. Rendon, T. Rogers, K. Savage, K. Sawant, R.H. Scott, A. Siddiq, A. Sieghart, S.C. Smith, A. Sosinsky, A. Stuckey, M. Tanguy, A.L. Taylor Tavares, E.R.A. Thomas, S.R. Thompson, A. Tucci, M.J. Welland, E. Williams, K. Witkowska, S.M. Wood, M. Zarowiecki, Olaf Riess, Tobias B. Haack, Holm Graessner, Birte Zurek, Kornelia Ellwanger, Stephan Ossowski, German Demidov, Marc Sturm, Julia M. Schulze-Hentrich, Rebecca Schüle, Christoph Kessler, Melanie Wayand, Matthis Synofzik, Carlo Wilke, Andreas Traschütz, Ludger Schöls, Holger Hengel, Peter Heutink, Han Brunner, Hans Scheffer, Nicoline Hoogerbrugge, Alexander Hoischen, Peter A.C. ’t Hoen, Lisenka E.L.M. Vissers, Christian Gilissen, Wouter Steyaert, Karolis Sablauskas, Richarda M. de Voer, Erik-Jan Kamsteeg, Bart van de Warrenburg, Nienke van Os, Iris te Paske, Erik Janssen, Elke de Boer, Marloes Steehouwer, Burcu Yaldiz, Tjitske Kleefstra, Anthony J. Brookes, Colin Veal, Spencer Gibson, Marc Wadsley, Mehdi Mehtarizadeh, Umar Riaz, Greg Warren, Farid Yavari Dizjikan, Thomas Shorter, Ana Töpf, Volker Straub, Chiara Marini Bettolo, Sabine Specht, Jill Clayton-Smith, Siddharth Banka, Elizabeth Alexander, Adam Jackson, Laurence Faivre, Christel Thauvin, Antonio Vitobello, Anne-Sophie Denommé-Pichon, Yannis Duffourd, Emilie Tisserant, Ange-Line Bruel, Christine Peyron, Aurore Pélissier, Sergi Beltran, Ivo Glynne Gut, Steven Laurie, Davide Piscia, Leslie Matalonga, Anastasios Papakonstantinou, Gemma Bullich, Alberto Corvo, Carles Garcia, Marcos Fernandez-Callejo, Carles Hernández, Daniel Picó, Ida Paramonov, Hanns Lochmüller, Gulcin Gumus, Virginie Bros-Facer, Ana Rath, Marc Hanauer, Annie Olry, David Lagorce, Svitlana Havrylenko, Katia Izem, Fanny Rigour, Giovanni Stevanin, Alexandra Durr, Claire-Sophie Davoine, Léna Guillot-Noel, Anna Heinzmann, Giulia Coarelli, Gisèle Bonne, Teresinha Evangelista, Valérie Allamand, Isabelle Nelson, Rabah Ben Yaou, Corinne Metay, Bruno Eymard, Enzo Cohen, Antonio Atalaia, Tanya Stojkovic, Milan Macek, Marek Turnovec, Dana Thomasová, Radka Pourová Kremliková, Vera Franková, Markéta Havlovicová, Vlastimil Kremlik, Helen Parkinson, Thomas Keane, Dylan Spalding, Alexander Senf, Peter Robinson, Daniel Danis, Glenn Robert, Alessia Costa, Christine Patch, Mike Hanna, Henry Houlden, Mary Reilly, Jana Vandrovcova, Francesco Muntoni, Irina Zaharieva, Anna Sarkozy, Vincent Timmerman, Jonathan Baets, Liedewei Van de Vondel, Danique Beijer, Peter de Jonghe, Vincenzo Nigro, Sandro Banfi, Annalaura Torella, Francesco Musacchia, Giulio Piluso, Alessandra Ferlini, Rita Selvatici, Rachele Rossi, Marcella Neri, Stefan Aretz, Isabel Spier, Anna Katharina Sommer, Sophia Peters, Carla Oliveira, Jose Garcia Pelaez, Ana Rita Matos, Celina São José, Marta Ferreira, Irene Gullo, Susana Fernandes, Luzia Garrido, Pedro Ferreira, Fátima Carneiro, Morris A. Swertz, Lennart Johansson, Joeri K. van der Velde, Gerben van der Vries, Pieter B. Neerincx, Dieuwke Roelofs-Prins, Sebastian Köhler, Alison Metcalfe, Alain Verloes, Séverine Drunat, Caroline Rooryck, Aurelien Trimouille, Raffaele Castello, Manuela Morleo, Michele Pinelli, Alessandra Varavallo, Manuel Posada De la Paz, Eva Bermejo Sánchez, Estrella López Martín, Beatriz Martínez Delgado, F. Javier Alonso García de la Rosa, Andrea Ciolfi, Bruno Dallapiccola, Simone Pizzi, Francesca Clementina Radio, Marco Tartaglia, Alessandra Renieri, Elisa Benetti, Peter Balicza, Maria Judit Molnar, Ales Maver, Borut Peterlin, Alexander Münchau, Katja Lohmann, Rebecca Herzog, Martje Pauly, Alfons Macaya, Anna Marcé-Grau, Andres Nascimiento Osorio, Daniel Natera de Benito, Hanns Lochmüller, Rachel Thompson, Kiran Polavarapu, David Beeson, Judith Cossins, Pedro M. Rodriguez Cruz, Peter Hackman, Mridul Johari, Marco Savarese, Bjarne Udd, Rita Horvath, Gabriel Capella, Laura Valle, Elke Holinski-Feder, Andreas Laner, Verena Steinke-Lange, Evelin Schröck, Andreas Rump, Gaurav K. Varshney, and Siddharth Banka. Clinical, genetic, epidemiologic, evolutionary, and functional delineation of tspear-related autosomal recessive ectodermal dysplasia 14. Apr 2023. URL: https://doi.org/10.1016/j.xhgg.2023.100186, doi:10.1016/j.xhgg.2023.100186. This article has 13 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_98-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013929` (3 mentions) - the report calls it "if available"; MONDO calls it **autosomal recessive nonsyndromic hearing loss 98**
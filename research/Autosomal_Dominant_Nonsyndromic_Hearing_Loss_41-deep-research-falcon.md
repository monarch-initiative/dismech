---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T11:30:56.231301'
end_time: '2026-08-28T11:38:18.063067'
duration_seconds: 441.83
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 41
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 7
  validator_version: 0.2.1
term_validation:
  total_terms: 14
  verified: 14
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Nonsyndromic_Hearing_Loss_41-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 41
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 41** covering all of the
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
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 41
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 41** covering all of the
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


# Autosomal Dominant Nonsyndromic Hearing Loss 41 (DFNA41): Research Report

## Executive summary

Autosomal dominant nonsyndromic hearing loss 41 (DFNA41) is an ultrarare, postlingual, progressive sensorineural hearing disorder caused by heterozygous pathogenic variation in **P2RX2**, most convincingly **NM_174873:c.178G>T, p.(Val60Leu)**. In the defining families, hearing loss was bilateral and symmetric, began at 12–20 years, initially emphasized high frequencies, and subsequently involved all frequencies. The original pedigree showed complete reported penetrance, severe thresholds of approximately 60–70 dB by age 20, and relative stabilization by the fourth decade. Occupational noise significantly worsened high-frequency hearing, making DFNA41 an unusually well-supported example of a Mendelian gene–environment interaction. (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3)

P2X2 is an extracellular ATP-gated trimeric cation channel involved in cochlear purinergic adaptation. Val60Leu reaches the plasma membrane but abolishes ATP-evoked current in homomeric receptors and markedly impairs heteromeric-channel permeability. Mouse and cellular models implicate impaired cochlear adaptation, hair-cell and ribbon-synapse pathology, neural degeneration, and reduced resilience to acoustic stress. Current treatment remains audiological and rehabilitative. A 2025 study—beyond the requested 2023–2024 priority window—reported mutation-selective AAV2–SaCas9 editing that rescued auditory, vestibular, and noise-susceptibility phenotypes in adult mice; this remains preclinical. (yan2013mutationofthe pages 4-5, chen2021generationandcharacterization pages 2-3, wei2025singledosegenomeediting pages 2-5, wei2025singledosegenomeediting pages 1-2)

The following table summarizes the principal curation-ready findings.

| domain | evidence-based finding | ontology/identifier suggestions | evidence level/limitations |
|---|---|---|---|
| Disease identity | Autosomal Dominant Nonsyndromic Hearing Loss 41 (DFNA41) is a rare Mendelian hearing-loss subtype defined from aggregated disease-level and pedigree-based human genetics data; OMIM identifier reported as 608224 (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3) | OMIM: 608224; MONDO: not established from retrieved evidence; MeSH/ICD/Orphanet not confirmed in retrieved sources | Human primary evidence for disease existence and mapping; some cross-database identifiers unavailable in retrieved context |
| Causal gene/variant | The best-supported causal lesion is heterozygous P2RX2 c.178G>T, p.Val60Leu (p.V60L; NM_174873), identified in two unrelated Chinese families and absent from >7,000 controls (yan2013mutationofthe pages 2-3) | P2RX2; HGNC gene symbol: P2RX2; variant: c.178G>T, p.Val60Leu | Human primary evidence is strong for this variant; broader allelic spectrum was not directly resolved from retrieved full primary reports |
| Inheritance | Inheritance is autosomal dominant with perfect cosegregation in the index pedigree, LOD score 13.3, and 100% penetrance among reported heterozygous carriers (yan2013mutationofthe pages 2-3) | HP:0000006 Autosomal dominant inheritance | Human pedigree evidence strong, but penetrance estimate is based on a small number of families |
| Core phenotype | Affected individuals have bilateral, symmetrical, progressive sensorineural hearing loss, first detected at 12-20 years, ultimately involving all frequencies; severity reached about 60-70 dB by age 20 in the original family (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3) | HP:0008619 Progressive hearing impairment; HP:0000407 Sensorineural hearing impairment; HP:0011453 Bilateral hearing impairment | Human primary evidence; natural-history estimates remain limited because only a few families are published |
| Audiometric pattern/symptoms | Hearing loss is typically high-frequency early, with high-frequency tinnitus reported; occupational noise exposure worsened high-frequency thresholds in mutation carriers (n=12 exposed vs n=9 unexposed, P=0.001) (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3) | HP:0000366 Hearing impairment; HP:0000358 Tinnitus; HP:0001644 Dilated? not applicable; no exact HPO for noise susceptibility confirmed here | Human evidence for tinnitus/noise interaction comes from small family-based comparisons |
| Gene-environment interaction | DFNA41 shows a documented gene-environment interaction: moderate noise exposure exacerbates hearing loss in carriers, indicating increased susceptibility to noise-induced hearing loss (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3, yan2013mutationofthe pages 5-6) | Exposure concept: occupational noise; phenotype concept: noise-induced hearing loss susceptibility | Human evidence present but based on observational family histories rather than prospective exposure studies |
| Molecular function | P2X2 is an extracellular ATP-gated trimeric cation channel expressed in cochlear sensory and supporting tissues; the p.V60L change abolishes ATP-evoked inward current in homomeric channels and impairs permeability in heteromeric channels (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3, mittal2016molecularstructureand pages 10-11) | GO:0005230 extracellular ligand-gated ion channel activity; GO:0006811 ion transport | Human/in vitro evidence strong for loss of channel function; detailed downstream pathway mapping remains incomplete |
| Pathomechanism | The mutant receptor localizes to plasma membrane but is functionally defective, supporting a loss-of-function/gating defect rather than mislocalization; inferred disease chain is impaired purinergic cochlear adaptation and reduced protection from noise/age-related stress (yan2013mutationofthe pages 4-5, mittal2016molecularstructureand pages 10-11) | GO:0007166 cell surface receptor signaling pathway; GO:0050890 cognition? not applicable; inferred cochlear homeostasis terms | Mixed evidence: human cell assays plus model inference; some mechanistic steps remain inferred rather than directly proven in patients |
| Anatomy/cell types | P2X2 expression/localization has been shown in organ of Corti, inner and outer hair cells, supporting cells, spiral ganglion neurons, and epithelial lining of the cochlea; mouse KI work also found expression in crista ampullaris (chen2021generationandcharacterization pages 2-3, yan2013mutationofthe pages 1-2) | UBERON: cochlea, organ of Corti; CL: hair cell, supporting cell, spiral ganglion neuron | Primarily model/histologic evidence; exact human single-cell localization was not retrieved |
| Diagnostics | Recommended diagnosis is clinical audiologic assessment plus molecular confirmation by hearing-loss gene panel, WES, or targeted P2RX2 testing in the setting of dominant postlingual progressive SNHL and family history; temporal bone CT can be normal (yan2013mutationofthe pages 2-3, wei2025singledosegenomeediting pages 1-2) | NCIT: Genetic Testing; audiology concepts: ABR/audiometry as applicable | Human evidence supports genetic confirmation; no DFNA41-specific formal guideline was retrieved |
| Current treatment | Current management is supportive: longitudinal audiologic follow-up, strict noise avoidance/protection, hearing aids, cochlear implantation when severity/function warrant it, and rehabilitation/genetic counseling (wei2025singledosegenomeediting pages 1-2, alde2023autosomaldominantnonsyndromic pages 16-17) | NCIT: Hearing Aid Device; NCIT: Cochlear Implantation; NCIT: Genetic Counseling | Largely inferred from standard care for dominant progressive SNHL; no DFNA41-specific interventional outcome series retrieved |
| Approved therapies/trials | No approved molecular therapy specific to DFNA41 was identified, and no relevant registered interventional clinical trial was retrieved in the tool search (wei2025singledosegenomeediting pages 1-2) | NCIT: Gene Therapy (experimental only) | Evidence reflects search results, not proof of global absence; trial landscape can change rapidly |
| Mouse models | P2rx2-null mice develop progressive hearing loss and greater noise vulnerability; the P2rx2 V61L knock-in mouse recapitulates DFNA41-related auditory disease, with hearing loss beginning at postnatal day 21 and progressing to deafness by 6 months, plus vestibular dysfunction and inner hair cell/ribbon synapse abnormalities (yan2013mutationofthe pages 1-2, chen2021generationandcharacterization pages 1-2, chen2021generationandcharacterization pages 1-1, chen2021generationandcharacterization pages 2-3) | MGI mouse P2rx2 models; phenotype terms: hearing loss, vestibular dysfunction | Strong model evidence; disease onset is earlier and progression faster than in humans |
| Cellular models | Patient-derived non-integrative hiPSCs from urine samples and CRISPR-engineered homozygous/heterozygous P2RX2 p.V60L hiPSC lines were generated as mechanistic models for hereditary hearing loss (dong2019efficientintroductionof pages 1-3) | iPSC disease model; P2RX2-mutated hiPSC | In vitro model only; no therapeutic efficacy in humans demonstrated |
| Recent translational development | A 2025 preclinical study used AAV2-delivered SaCas9/sgRNA allele-specific editing in adult P2rx2V61L/+ mice, with efficient mutant-selective editing, minimal detected off-target effects, no notable AAV integration in cochlear hair cells, and rescue of long-term auditory/vestibular function plus protection from noise hypersensitivity (wei2025singledosegenomeediting pages 1-2, wei2025singledosegenomeediting pages 2-5, wei2025singledosegenomeediting pages 5-7) | NCIT: CRISPR-Cas9 Genome Editing; NCIT: Adeno-Associated Virus Vector | Model-only, post-2024 preclinical evidence; not yet a human therapy or clinical trial |
| Evidence gaps | No robust disease-specific prevalence/incidence, survival, mortality, protective genetic modifiers, epigenetic biomarkers, or validated prognostic biomarkers were found in retrieved evidence (yan2013mutationofthe pages 1-2, wei2025singledosegenomeediting pages 1-2) | Knowledge-base flag: data not available | Important to distinguish absence of evidence from evidence of absence |


*Table: This table condenses the most actionable evidence on DFNA41 across identity, genetics, phenotype, mechanism, diagnosis, treatment, and models. It distinguishes human primary findings from model-based and inferred information to support knowledge-base curation.*

## 1. Disease information

### Definition

DFNA41 is a Mendelian, autosomal dominant, nonsyndromic sensorineural hearing loss. “Nonsyndromic” means that hearing impairment is the defining human clinical manifestation rather than one component of a reproducible multisystem syndrome. The disease was initially delineated in a six-generation family from Sichuan, China, and later associated with P2RX2 in that family and a second unrelated Chinese family. (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3)

### Identifiers and synonyms

- **Preferred name:** Autosomal dominant nonsyndromic hearing loss 41
- **Common synonyms:** DFNA41; autosomal dominant deafness 41; deafness, autosomal dominant 41; P2RX2-related dominant hearing loss
- **OMIM:** **608224** (DFNA41/deafness, autosomal dominant 41)
- **Causal gene:** **P2RX2**, purinergic receptor P2X 2
- **Locus:** chromosome 12q24–qter; the refined original interval was hg19 chr12:129,051,849–133,851,895. (yan2013mutationofthe pages 1-2)
- **MONDO:** A disease-specific MONDO identifier could not be verified from the retrieved evidence. Use the verified OMIM identifier and parent concepts such as hereditary nonsyndromic sensorineural hearing loss until an ontology release confirms a dedicated MONDO record.
- **Orphanet:** No disease-specific Orphanet identifier was verified.
- **ICD-10/ICD-11:** No DFNA41-specific billing code exists in the retrieved evidence; code the manifest bilateral sensorineural hearing loss and genetic etiology as permitted locally.
- **MeSH:** No uniquely specific DFNA41 heading was verified; broader concepts include *Hearing Loss, Sensorineural* and *Hearing Loss, Hereditary*.

The evidence is principally **aggregated disease-level information derived from published family studies**, not routine EHR-derived patient-level surveillance. The foundational evidence nevertheless consists of individual family members’ genotypes, audiograms, exposure histories, and clinical examinations. (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3)

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The strongest established cause is a **germline heterozygous P2RX2 missense variant, c.178G>T, p.(Val60Leu)**. It cosegregated perfectly with hearing loss in the index pedigree, yielding a LOD score of **13.3**, and penetrance among reported heterozygotes was **100%**. Screening 65 additional dominant nonsyndromic hearing-loss families identified the same variant in another unrelated Chinese family. It was absent from 7,000 controls—4,300 European-ancestry, 2,200 African-American, and 500 Chinese individuals—giving historical estimated frequencies below 0.0001 in the mixed sample and below 0.001 in the Chinese sample. (yan2013mutationofthe pages 2-3)

This variant is germline, not somatic. Published reports describe additional P2RX2 variants in hearing-loss families, including an Italian family and an Iranian stop-loss report, but the retrieved full-text evidence was insufficient to curate their exact HGVS notation, segregation, modern ClinVar assertions, or functional strength confidently. Consequently, **Val60Leu should remain the reference, best-validated DFNA41 allele**, and other alleles should be evaluated individually rather than assumed equivalent. (mittal2016molecularstructureand pages 10-11, wei2025singledosegenomeediting pages 18-18)

### Risk factors

- **Genetic:** A heterozygous pathogenic P2RX2 allele; an affected parent or other vertical family history.
- **Age:** Thresholds worsen with age, particularly from adolescence through early/middle adulthood.
- **Noise:** Occupational/recreational acoustic exposure is the best-supported modifiable factor. In the original family, noise-exposed carriers (**n=12**) had poorer 2–8-kHz thresholds than unexposed carriers (**n=9; P=0.001**). Exposures in construction trades during ages 12–25 were specifically reported. (yan2013mutationofthe pages 3-4, yan2013mutationofthe pages 2-3)
- **Sex:** No sex-specific difference has been established.
- **Tobacco, alcohol, diet, exercise, pollution, infection, or ototoxic drugs:** No DFNA41-specific risk estimates are available. General cochlear-risk counseling remains reasonable but must not be represented as disease-specific evidence.

### Protective factors

No protective P2RX2 alleles, validated modifier genes, diets, drugs, or prophylactic agents have been demonstrated. Practical acoustic protection—avoiding hazardous exposure, reducing duration/intensity, and correctly using hearing protection—is biologically compelling because noise is a demonstrated phenotype modifier, although no prospective prevention trial has quantified benefit in DFNA41.

### Causal gene–environment chain

**P2RX2 Val60Leu → impaired ATP-gated cochlear channel activity → reduced purinergic adaptation during elevated sound → excessive acoustic stress and impaired ionic/homeostatic response → accelerated high-frequency threshold elevation and cochlear cellular injury.** The human exposure association and mouse noise challenge jointly support this chain. (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 4-5, yan2013mutationofthe pages 5-6)

## 3. Phenotypes

### Core human phenotype

| Phenotype | Characteristics | Suggested HPO annotation |
|---|---|---|
| Sensorineural hearing impairment | Defining manifestation; moderate-to-severe or severe with progression | HP:0000407 Sensorineural hearing impairment |
| Bilateral/symmetric hearing impairment | Bilateral and symmetrical in reported families | HP:0011453 Bilateral hearing impairment; symmetry may require a qualifier |
| Progressive hearing impairment | Chronic progression from adolescence, often stabilizing by the fourth decade | HP:0008619 Progressive hearing impairment |
| Postlingual onset | Usually 12–20 years in the defining families | HP:0008504 Late-onset sensorineural hearing impairment or appropriate onset modifier |
| High-frequency hearing impairment | Early sloping/high-frequency predominance, eventually all frequencies | HP:0005101 High-frequency hearing impairment |
| Tinnitus | Generally high-frequency tinnitus in affected members | HP:0000360 Tinnitus |
| Increased noise susceptibility | Acoustic exposure significantly worsens high-frequency thresholds | Use exposure annotation plus noise-induced hearing-loss susceptibility; no exact HPO term was verified |

The original report stated: **“Audiologic evaluation of family members revealed bilateral and symmetrical sensorineural hearing loss, with age at onset ranging from 12 y to 20 y, generally accompanied by high-frequency tinnitus.”** Hearing loss ultimately involved all frequencies. In the index family, it was severe—approximately **60–70 dB—by age 20**, with relatively little subsequent progression; pooled thresholds declined until the fourth decade and then remained approximately stable. (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3)

### Vestibular phenotype

Vestibular dysfunction is prominent in the Val61Leu knock-in mouse, but a consistent vestibular disorder has **not** been established in the defining human families. It should therefore be recorded as a **model phenotype**, not a core human DFNA41 feature. (chen2021generationandcharacterization pages 1-2, chen2021generationandcharacterization pages 1-1)

### Frequency and quality of life

Penetrance was 100% in the reported index pedigree, but exact frequencies of tinnitus, individual audiometric configurations, and vestibular symptoms are not robustly estimable from the few published families. No DFNA41-specific EQ-5D, SF-36, PROMIS, speech-recognition, education, employment, or caregiver-burden study was identified. Likely effects include impaired communication, speech understanding in noise, school/work participation, tinnitus burden, and eventual hearing-device dependence; these are clinically reasonable consequences of progressive sensorineural loss, not measured DFNA41-specific outcomes.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** P2RX2
- **Protein:** P2X purinoceptor 2/P2X2 receptor
- **Reference transcript used in the foundational report:** NM_174873
- **Reference protein cited in the mouse study:** NP_733782
- **Variant:** c.178G>T, p.(Val60Leu)
- **Genomic coordinate in the original report:** hg19 chr12:133,196,029G>T
- **Variant class:** missense SNV
- **Origin:** constitutional/germline
- **Inheritance:** autosomal dominant
- **Population frequency:** absent from the historical 7,000-control dataset; contemporary gnomAD frequency was not independently verified here. (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3, chen2021generationandcharacterization pages 2-3)

The Val60 residue is highly conserved across vertebrates. The variant has strong pathogenic evidence: cosegregation, two unrelated families with concordant phenotype, extreme rarity, functional loss, and matching animal phenotypes. A clinical laboratory should nevertheless apply current ACMG/AMP hearing-loss specifications and report its current ClinVar classification/accession rather than copy a historical label uncritically.

### Functional consequence

Wild-type P2X2 channels responded to ATP with inward current; 1 mM ATP produced a mean current of **2.17 ± 0.46 nA** in wild-type-transfected HEK293 cells (**n=16**), whereas Val60Leu-transfected cells showed no response (**n=15**). Mutant channels also lacked ATP-stimulated FM1-43 permeability. Coexpression of wild-type and mutant subunits—modeling heterozygosity—reduced ATP-activated permeability by approximately **60%**. Both proteins targeted the plasma membrane, arguing for defective gating/channel function rather than simple trafficking failure. (yan2013mutationofthe pages 3-4, yan2013mutationofthe pages 2-3)

The literature uses both “loss of function” and, in a later editing paper, “gain-of-function mutation.” The direct electrophysiology supports **loss of ATP-activated channel function with a dominant interfering effect in heteromeric trimers**. “Dominant-negative” is mechanistically plausible but should be used cautiously unless a variant-specific clinical laboratory or functional study explicitly adopts that classification. (yan2013mutationofthe pages 4-5, wei2025singledosegenomeediting pages 1-2)

### Other genomic and regulatory information

No recurrent CNV, translocation, inversion, aneuploidy, repeat expansion, mitochondrial lesion, somatic mosaicism, or epigenetic signature is established as the cause of DFNA41. No validated modifier gene, methylation biomarker, chromatin abnormality, or disease-specific transcriptomic, proteomic, metabolomic, or lipidomic signature was identified.

## 5. Environmental information

Noise is the only non-genetic exposure with direct DFNA41-specific human evidence. Affected carriers may be harmed by exposure levels tolerated by noncarriers, and the original authors discussed susceptibility even around occupational levels conventionally regarded as acceptable. (yan2013mutationofthe pages 5-6)

There is no evidence that infection causes or triggers DFNA41. Smoking, alcohol, diet, physical activity, radiation, air pollution, and occupational chemicals have not been studied specifically. Ototoxic medications may independently injure hearing, but a P2RX2-specific pharmacogenetic interaction has not been demonstrated.

## 6. Mechanism and pathophysiology

### Upstream molecular defect

P2X2 is a trimeric, extracellular ATP-gated nonselective cation channel. In the inner ear it is implicated in sound-transduction regulation, auditory neurotransmission, outer-hair-cell electromotility, gap-junction-associated homeostasis, and potassium recycling. Extracellular ATP released during acoustic stress activates P2 receptors in sensory, supporting, and neural tissues, reducing cochlear sensitivity and contributing to adaptation. (yan2013mutationofthe pages 1-2, mittal2016molecularstructureand pages 10-11)

### Causal chain

1. **Germline P2RX2 Val60Leu** alters a conserved extracellular/transmembrane-coupled gating region.
2. Mutant subunits reach the membrane but fail to generate normal ATP-evoked current; mixed wild-type/mutant trimers have reduced permeability.
3. Cochlear sensory and supporting cells cannot mount normal ATP-dependent adaptation and ionic shunting during sustained sound.
4. Repeated physiological, age-related, and acoustic stress leads to impaired hair-cell/synaptic function.
5. Model pathology includes abnormal inner-hair-cell morphology, disrupted ribbon-synapse distribution, hair/supporting-cell loss, and spiral-ganglion-neuron loss.
6. Clinically this produces progressive, initially high-frequency sensorineural hearing loss, accelerated by noise. (yan2013mutationofthe pages 4-5, chen2021generationandcharacterization pages 2-3)

### Suggested ontology terms

- **GO molecular function:** extracellular ATP-gated cation channel activity; ligand-gated ion-channel activity; purinergic nucleotide receptor activity.
- **GO biological process:** ion transmembrane transport; cellular response to ATP; potassium-ion homeostasis; sensory perception of sound; auditory receptor-cell development; chemical synaptic transmission; response to acoustic stimulus.
- **GO cellular component:** plasma membrane; stereocilium membrane where supported; Golgi apparatus; mitochondrion; presynaptic ribbon/synaptic region.
- **Cell Ontology:** inner hair cell; outer hair cell; cochlear supporting cell; spiral ganglion neuron; vestibular hair cell.

The organelle localization reported in mouse fibroblasts—plasma membrane, Golgi, and mitochondria—does not by itself establish mitochondrial dysfunction as a human disease mechanism. Likewise, inflammation, apoptosis, oxidative stress, and immune activation are plausible downstream pathways in acoustic injury but have not been specifically demonstrated as primary DFNA41 mechanisms.

### Molecular profiling and advanced technologies

No DFNA41 single-cell atlas, spatial-transcriptomic dataset, unbiased proteome/metabolome, or multi-omics patient cohort was found. Available advanced platforms are targeted: electrophysiology, immunolocalization, patient-derived hiPSCs, CRISPR-engineered isogenic lines, targeted sequencing, and in-vivo allele editing. Patient-derived nonintegrating hiPSCs were generated from urine samples of three family members, and CRISPR plus single-stranded donor oligonucleotides generated homozygous isogenic mutant cells. These are mechanistic models, not diagnostic assays or therapies. (dong2019efficientintroductionof pages 1-3)

## 7. Anatomical structures affected

The primary organ is the **inner ear**, specifically the **cochlea**. Relevant structures include the organ of Corti, inner and outer hair cells, supporting epithelium, spiral ganglion and auditory nerve pathway, lateral-wall homeostatic system, and ribbon synapses. P2X2 expression in the knock-in study was strong in the organ of Corti, spiral ganglion, and crista ampullaris; within the cochlea it was present in inner/outer hair cells, supporting cells, and spiral ganglion neurons. (chen2021generationandcharacterization pages 2-3)

Suggested anatomy annotations include **UBERON: cochlea**, organ of Corti, inner ear, spiral ganglion, auditory hair cell, and crista ampullaris. The human hearing loss is bilateral and symmetric. Temporal-bone CT in one affected person was normal, consistent with a molecular/cellular rather than gross malformation disorder. No secondary systemic-organ involvement has been established. (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3)

## 8. Temporal development

- **Onset:** Insidious, postlingual, usually 12–20 years in the original families.
- **Early stage:** High-frequency threshold elevation and tinnitus; speech understanding in noise may deteriorate before broad-frequency disability.
- **Intermediate stage:** Progressive involvement of additional frequencies; approximately 60–70-dB severity by age 20 in the index pedigree.
- **Later stage:** Mean thresholds declined until approximately the fourth decade and then were comparatively stable, although individual trajectories and noise exposure varied.
- **Course:** Chronic/lifelong; neither episodic nor relapsing-remitting.
- **Remission:** No spontaneous or treatment-induced biological remission documented.
- **Critical period:** Early identification, before extensive cochlear degeneration or hazardous noise exposure, is the rational intervention window. Mouse editing produced broader frequency rescue when delivered earlier, but the human window is unknown. (yan2013mutationofthe pages 2-3, wei2025singledosegenomeediting pages 1-2)

## 9. Inheritance and population

DFNA41 is autosomal dominant: each child of a heterozygous affected individual has a theoretical **50% probability** of inheriting the familial variant. Reported penetrance for Val60Leu was 100% in the index family, but this estimate may not generalize to every P2RX2 allele or age. Expressivity varies with age and noise exposure. No anticipation, repeat expansion, parent-of-origin effect, or established germline mosaicism has been reported. (yan2013mutationofthe pages 2-3)

Prevalence and incidence per 100,000 are unknown. The small number of reported families and absence from 7,000 historical controls indicate an ultrarare disorder. The reference Val60Leu allele was initially found in two Chinese families; this does not prove a founder effect because shared ancestry/haplotype evidence was not established. Other population reports suggest allelic and geographic expansion, but robust ancestry-specific frequencies are unavailable. No sex bias is expected for an autosomal disorder and none has been demonstrated. Consanguinity is not etiologically relevant to the dominant inheritance pattern, although it may coexist incidentally.

## 10. Diagnostics

### Clinical evaluation

Diagnosis requires:

1. Personal and three-generation family history, including age at onset, tinnitus, vestibular symptoms, occupational/recreational noise, and ototoxic exposure.
2. Otoscopy and middle-ear assessment to exclude conductive disease.
3. Bilateral pure-tone audiometry, bone conduction, speech reception/recognition, and serial testing to document progression.
4. Tympanometry; otoacoustic emissions and auditory brainstem responses when age, reliability, or auditory-neuropathy differential warrants them.
5. Vestibular examination/testing only if symptoms are present or for detailed phenotyping.
6. Imaging when cochlear implantation, asymmetry, neurologic signs, or another structural disorder is suspected—not as a molecular confirmation test. One affected carrier had normal temporal bones on CT. (yan2013mutationofthe pages 2-3)

No blood chemistry, urine assay, enzyme assay, biopsy, histopathology, circulating protein, metabolite, or imaging biomarker is diagnostic.

### Genetic testing

A comprehensive hearing-loss NGS panel containing **P2RX2** is generally the most efficient first molecular test. Sequence analysis must detect SNVs and small indels; exon-level CNV analysis is useful for the broader differential, although no recurrent P2RX2 CNV is established. Familial Val60Leu can be confirmed by targeted Sanger sequencing. WES or WGS is appropriate when a panel is negative, phenotype is atypical, structural/noncoding variation is suspected, or reanalysis is anticipated. WGS offers more uniform coverage and noncoding/structural-variant detection but has no proven DFNA41-specific yield advantage.

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine tests for classic DFNA41; deploy them only when the phenotype or family history suggests another diagnosis. RNA sequencing is research-level because no validated P2RX2 splicing biomarker exists.

Pathogenic/likely pathogenic results should be confirmed and segregated in relatives. A VUS must not establish diagnosis or direct predictive testing without additional evidence.

### Differential diagnosis

The principal differential includes other autosomal dominant progressive nonsyndromic hearing losses—particularly KCNQ4/DFNA2, WFS1/DFNA6/14/38, TECTA/DFNA8/12, ACTG1/DFNA20/26, POU4F3/DFNA15, MYO6/DFNA22, EYA4/DFNA10—and acquired noise-induced, ototoxic, infectious, autoimmune, structural, and age-related hearing loss. The combination of adolescent onset, bilateral symmetric progression, vertical inheritance, and disproportionate noise susceptibility suggests but does not uniquely identify DFNA41. A 2023 review emphasized that dominant nonsyndromic loss is usually bilateral, postlingual, high-frequency, and progressive, underscoring the need for molecular rather than phenotype-only diagnosis. (alde2023autosomaldominantnonsyndromic pages 16-17)

### Screening

Universal newborn physiologic hearing screening may be normal because DFNA41 is commonly postlingual. The key strategy is **cascade genetic testing** after identifying a familial pathogenic variant, followed by baseline and serial audiometry in carriers. Predictive testing of minors can be clinically useful because noise avoidance and auditory surveillance are actionable during childhood/adolescence.

## 11. Outcome and prognosis

DFNA41 is not known to reduce survival or life expectancy, and disease-specific mortality is not reported. Morbidity is auditory: progressive communication disability, tinnitus, reduced speech understanding—especially in noise—and possible eventual dependence on amplification or implantation. Human vestibular disability is insufficiently characterized.

Untreated sensorineural loss does not biologically recover. Hearing aids and cochlear implants can improve function but do not correct the underlying channel defect. Prognosis depends on baseline thresholds, age, rate of progression, speech recognition, acoustic exposure, and timely rehabilitation. The familial P2RX2 genotype predicts susceptibility but is not a validated quantitative prognostic biomarker.

## 12. Treatment

### Current standard management

There is no approved DFNA41-specific pharmacotherapy and no established P2RX2-directed pharmacogenomic algorithm. Management is individualized:

- Regular audiology, with shorter intervals during childhood, after threshold change, or after major noise exposure.
- Hearing aids when thresholds or communication needs warrant them.
- Remote microphones, classroom/workplace accommodations, captioning, and auditory/speech-language rehabilitation.
- Tinnitus counseling and evidence-based tinnitus management.
- Cochlear-implant assessment for severe-to-profound loss with inadequate aided speech understanding.
- Genetic counseling and cascade testing.
- Strict acoustic-risk reduction.

Suggested NCIT concepts include **Hearing Aid Device**, **Cochlear Implantation**, **Auditory Rehabilitation**, **Speech Therapy**, **Genetic Counseling**, and **Genetic Testing**. No DFNA41-specific response rate or adverse-event dataset exists; outcomes should be drawn from the applicable device and rehabilitation population rather than attributed to this genotype.

### Experimental genome editing

A 2025 JCI study used local round-window-membrane injection plus canal fenestration to deliver **AAV2–Staphylococcus aureus Cas9–sgRNA** into adult P2rx2Val61Leu/+ mice. The strategy disrupted the mutant allele while preserving wild type. In primary cells, SaCas9–sgRNA-1 produced **75.01% ± 4.55%** mutant-allele indels versus **0.45% ± 0.39%** on the wild-type allele; **85.1%** of indels were frameshifting. In vivo whole-cochlea indels were 2.62% ± 0.64%, while mutant-transcript and isolated-hair-cell analyses indicated approximately **28%** editing of P2rx2-expressing cells and **26.96% ± 4.2%** mutant-allele editing in isolated hair cells. No CIRCLE-seq off-target site beyond the target was found in the reported cell assay, and no notable AAV integration was detected at the cochlear target under the therapeutic conditions. (wei2025singledosegenomeediting pages 5-7, wei2025singledosegenomeediting pages 2-5)

The abstract states that editing **“effectively restores long-term auditory and vestibular function”** and protects mice from the heightened noise-induced phenotype. Juvenile intervention rescued a broader frequency range, and a human-Val60Leu-specific guide was identified. Nevertheless, this is mouse evidence: inner-ear surgical delivery, durability, immune response, off-target detection sensitivity, large rearrangements, human cochlear coverage, and allele specificity require further validation. No DFNA41 human interventional trial or NCT identifier was found in the ClinicalTrials.gov search. (wei2025singledosegenomeediting pages 1-2)

## 13. Prevention

### Primary prevention

The inherited variant cannot presently be prevented in an individual after conception. For carriers, the most important modifiable action is prevention of avoidable acoustic injury: engineering controls, lower volume, shorter exposure, distance from sound sources, correctly fitted hearing protection, and occupational-health review. Avoid unnecessary ototoxic exposure and monitor hearing when an ototoxic drug is medically essential, although no P2RX2-specific drug interaction has been shown.

### Secondary prevention

- Cascade testing of at-risk relatives.
- Baseline audiometry before expected onset.
- Periodic surveillance to detect subtle high-frequency loss.
- Early amplification and educational/work accommodations.
- Prompt reassessment after tinnitus, perceived decline, or significant noise exposure.

### Tertiary prevention

Appropriate hearing technology, communication rehabilitation, tinnitus care, fall/vestibular assessment when symptomatic, and psychosocial/occupational accommodations reduce disability.

### Reproductive counseling

Counsel regarding the 50% transmission probability, variable severity and noise-modified expressivity, natural conception with prenatal diagnosis, and IVF with PGT-M where legally and ethically available. Carrier screening is not the appropriate concept for an autosomal dominant disorder; targeted predictive testing of relatives is more relevant. There is no applicable vaccine, anti-infective prophylaxis, or population-wide DFNA41 screening program.

## 14. Other species and natural disease

P2rx2 is evolutionarily conserved in vertebrates, and Val60/61 lies in a highly conserved region. Relevant taxa include **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, **Rattus norvegicus (10116)**, and **Danio rerio (7955)**. A naturally occurring companion-animal, livestock, or wildlife disorder confidently homologous to human DFNA41 was not identified. There is no zoonotic or cross-species transmission because this is an inherited channelopathy, not an infection.

Comparative work demonstrates conservation of cochlear P2X2-mediated acoustic adaptation, but species differ in cochlear maturation and disease timing. Veterinary breed/VBO annotations are therefore unavailable.

## 15. Model organisms and experimental systems

### P2rx2-null mouse

P2rx2-knockout mice develop progressive hearing loss, particularly in the high-frequency basal cochlea, and exaggerated noise-induced threshold shifts. At advanced age they show degeneration involving hair cells, supporting cells, and spiral ganglion neurons. After early moderate noise exposure, knockout mice had approximately **13-dB greater thresholds at 20–36 kHz** than controls. This model establishes the protective function of P2X2 but models complete loss, not the exact heterozygous human allele. (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 4-5)

### P2rx2Val61Leu knock-in mouse

The mouse homolog of human Val60 is Val61. Heterozygous knock-in mice developed hearing loss by postnatal day 21 and deafness by approximately six months, accompanied by vestibular dysfunction and progressive inner-hair-cell and ribbon-synapse abnormalities. Expression was seen in inner/outer hair cells, supporting cells, spiral ganglion neurons, and crista ampullaris. This is the principal allele-specific model and the platform used for genome editing. Its limitation is substantially earlier and faster progression than the usual human 12–20-year onset. (chen2021generationandcharacterization pages 1-2, chen2021generationandcharacterization pages 1-1, chen2021generationandcharacterization pages 2-3)

### Cellular models

- HEK293 cells: ATP-current electrophysiology.
- MDCK-II cells: ATP-dependent FM1-43 permeability.
- Rat organ-of-Corti cultures: receptor targeting/localization.
- Patient-derived hiPSCs and CRISPR-generated isogenic mutant hiPSCs: human genetic background and differentiation platform.
- HEI-OC1 cochlear cells and mouse fibroblasts: allele-specific editor screening and off-target assessment. (yan2013mutationofthe pages 2-3, dong2019efficientintroductionof pages 1-3, wei2025singledosegenomeediting pages 2-5)

The hiPSCs were described as “good models to investigate the pathological mechanisms,” but they do not reproduce the mature cochlear architecture, tonotopy, acoustic mechanics, or lifelong exposure history. Organoids, single-cell profiling, and spatial assays could help bridge that gap.

## Evidence hierarchy, recent developments, and gaps

The decisive human evidence remains the 2013 genetic-functional study; no 2023–2024 primary study materially redefined the DFNA41 phenotype or causal allele in the retrieved corpus. The most relevant recent review context is the 2023 synthesis of autosomal dominant nonsyndromic hearing loss, while the major disease-specific translational advance was published in **2025**, after submission in October 2024. (alde2023autosomaldominantnonsyndromic pages 16-17, wei2025singledosegenomeediting pages 1-2)

Key unresolved areas are disease prevalence, complete allelic spectrum, contemporary ClinVar/gnomAD curation for each allele, prospective natural history, speech-recognition and quality-of-life outcomes, human vestibular involvement, modifiers other than noise, biomarkers, optimal surveillance intervals, genotype-specific implant outcomes, and human safety/efficacy of allele editing.

## Principal references

1. Yan D, et al. **Mutation of the ATP-gated P2X2 receptor leads to progressive hearing loss and increased susceptibility to noise.** *PNAS*. Published February 5, 2013;110:2228–2233. DOI/URL: https://doi.org/10.1073/pnas.1222285110. The abstract directly states that Val60Leu “abolishes two hallmark features” of P2X2 receptors and that noise worsened hearing in heterozygous relatives. (yan2013mutationofthe pages 1-2, yan2013mutationofthe pages 2-3)
2. Housley GD, et al. **ATP-gated ion channels mediate adaptation to elevated sound levels.** *PNAS*. Published 2013;110:7494–7499. DOI/URL: https://doi.org/10.1073/pnas.1222295110. This supplies complementary model evidence for P2X2-mediated acoustic adaptation. (yan2013mutationofthe pages 1-2)
3. Dong Y, et al. **Efficient introduction of an isogenic homozygous mutation to induced pluripotent stem cells from a hereditary hearing loss family using CRISPR/Cas9 and single-stranded donor oligonucleotides.** *J Int Med Res*. Published 2019;47:1717–1730. DOI/URL: https://doi.org/10.1177/0300060519829990. (dong2019efficientintroductionof pages 1-3)
4. Chen X, et al. **Generation and characterization of a P2rx2 V60L mouse model for DFNA41.** *Human Molecular Genetics*. Published March 2021;30:985–995. DOI/URL: https://doi.org/10.1093/hmg/ddab077. The abstract reports hearing loss at day 21, deafness by six months, vestibular dysfunction, and ribbon-synapse abnormalities. (chen2021generationandcharacterization pages 1-2, chen2021generationandcharacterization pages 2-3)
5. Vlajkovic SM, Thorne PR. **Purinergic Signalling in the Cochlea.** *International Journal of Molecular Sciences*. Published November 2022;23:14874. DOI/URL: https://doi.org/10.3390/ijms232314874. Review evidence for cochlear ATP signaling and acoustic adaptation.
6. Aldè M, et al. **Autosomal Dominant Non-Syndromic Hearing Loss (DFNA): A Comprehensive Narrative Review.** *Biomedicines*. Published June 2023;11:1616. DOI/URL: https://doi.org/10.3390/biomedicines11061616. (alde2023autosomaldominantnonsyndromic pages 16-17)
7. Wei W, et al. **Single-dose genome editing therapy rescues auditory and vestibular functions in adult mice with DFNA41 deafness.** *Journal of Clinical Investigation*. Published August 14, 2025;135:e187872. DOI/URL: https://doi.org/10.1172/JCI187872. Model-only therapeutic evidence; no human efficacy is established. (wei2025singledosegenomeediting pages 5-7, wei2025singledosegenomeediting pages 2-5, wei2025singledosegenomeediting pages 1-2)

References

1. (yan2013mutationofthe pages 1-2): Denise Yan, Yan Zhu, Tom Walsh, Dinghua Xie, Huijun Yuan, Asli Sirmaci, Taro Fujikawa, Ann Chi Yan Wong, Tze L. Loh, Lilin Du, M’hamed Grati, Srdjan M. Vlajkovic, Susan Blanton, Allen F. Ryan, Zheng-Yi Chen, Peter R. Thorne, Bechara Kachar, Mustafa Tekin, Hong-Bo Zhao, Gary D. Housley, Mary-Claire King, and Xue Z. Liu. Mutation of the atp-gated p2x2 receptor leads to progressive hearing loss and increased susceptibility to noise. Proceedings of the National Academy of Sciences, 110:2228-2233, Jan 2013. URL: https://doi.org/10.1073/pnas.1222285110, doi:10.1073/pnas.1222285110. This article has 196 citations and is from a highest quality peer-reviewed journal.

2. (yan2013mutationofthe pages 2-3): Denise Yan, Yan Zhu, Tom Walsh, Dinghua Xie, Huijun Yuan, Asli Sirmaci, Taro Fujikawa, Ann Chi Yan Wong, Tze L. Loh, Lilin Du, M’hamed Grati, Srdjan M. Vlajkovic, Susan Blanton, Allen F. Ryan, Zheng-Yi Chen, Peter R. Thorne, Bechara Kachar, Mustafa Tekin, Hong-Bo Zhao, Gary D. Housley, Mary-Claire King, and Xue Z. Liu. Mutation of the atp-gated p2x2 receptor leads to progressive hearing loss and increased susceptibility to noise. Proceedings of the National Academy of Sciences, 110:2228-2233, Jan 2013. URL: https://doi.org/10.1073/pnas.1222285110, doi:10.1073/pnas.1222285110. This article has 196 citations and is from a highest quality peer-reviewed journal.

3. (yan2013mutationofthe pages 4-5): Denise Yan, Yan Zhu, Tom Walsh, Dinghua Xie, Huijun Yuan, Asli Sirmaci, Taro Fujikawa, Ann Chi Yan Wong, Tze L. Loh, Lilin Du, M’hamed Grati, Srdjan M. Vlajkovic, Susan Blanton, Allen F. Ryan, Zheng-Yi Chen, Peter R. Thorne, Bechara Kachar, Mustafa Tekin, Hong-Bo Zhao, Gary D. Housley, Mary-Claire King, and Xue Z. Liu. Mutation of the atp-gated p2x2 receptor leads to progressive hearing loss and increased susceptibility to noise. Proceedings of the National Academy of Sciences, 110:2228-2233, Jan 2013. URL: https://doi.org/10.1073/pnas.1222285110, doi:10.1073/pnas.1222285110. This article has 196 citations and is from a highest quality peer-reviewed journal.

4. (chen2021generationandcharacterization pages 2-3): Xiaoya Chen, Clemer Abad, Zheng-yi Chen, Juan I Young, Channabasavaiah B Gurumurthy, Katherina Walz, and Xue Zhong Liu. Generation and characterization of a p2rx2 v60l mouse model for dfna41. Human molecular genetics, 30:985-995, Mar 2021. URL: https://doi.org/10.1093/hmg/ddab077, doi:10.1093/hmg/ddab077. This article has 10 citations and is from a domain leading peer-reviewed journal.

5. (wei2025singledosegenomeediting pages 2-5): Wei Wei, Wenliang Zhu, Stewart Silver, Ariel M. Armstrong, Fletcher S. Robbins, Arun Prabhu Rameshbabu, Katherina Walz, Yizhou Quan, Wan Du, Yehree Kim, Artur A. Indzhykulian, Yilai Shu, Xue-Zhong Liu, and Zheng-Yi Chen. Single-dose genome editing therapy rescues auditory and vestibular functions in adult mice with dfna41 deafness. Journal of Clinical Investigation, Aug 2025. URL: https://doi.org/10.1172/jci187872, doi:10.1172/jci187872. This article has 5 citations and is from a highest quality peer-reviewed journal.

6. (wei2025singledosegenomeediting pages 1-2): Wei Wei, Wenliang Zhu, Stewart Silver, Ariel M. Armstrong, Fletcher S. Robbins, Arun Prabhu Rameshbabu, Katherina Walz, Yizhou Quan, Wan Du, Yehree Kim, Artur A. Indzhykulian, Yilai Shu, Xue-Zhong Liu, and Zheng-Yi Chen. Single-dose genome editing therapy rescues auditory and vestibular functions in adult mice with dfna41 deafness. Journal of Clinical Investigation, Aug 2025. URL: https://doi.org/10.1172/jci187872, doi:10.1172/jci187872. This article has 5 citations and is from a highest quality peer-reviewed journal.

7. (yan2013mutationofthe pages 5-6): Denise Yan, Yan Zhu, Tom Walsh, Dinghua Xie, Huijun Yuan, Asli Sirmaci, Taro Fujikawa, Ann Chi Yan Wong, Tze L. Loh, Lilin Du, M’hamed Grati, Srdjan M. Vlajkovic, Susan Blanton, Allen F. Ryan, Zheng-Yi Chen, Peter R. Thorne, Bechara Kachar, Mustafa Tekin, Hong-Bo Zhao, Gary D. Housley, Mary-Claire King, and Xue Z. Liu. Mutation of the atp-gated p2x2 receptor leads to progressive hearing loss and increased susceptibility to noise. Proceedings of the National Academy of Sciences, 110:2228-2233, Jan 2013. URL: https://doi.org/10.1073/pnas.1222285110, doi:10.1073/pnas.1222285110. This article has 196 citations and is from a highest quality peer-reviewed journal.

8. (mittal2016molecularstructureand pages 10-11): Rahul Mittal, Brandon Chan, M'hamed Grati, Jeenu Mittal, Kunal Patel, Luca H. Debs, Amit P. Patel, Denise Yan, Prem Chapagain, and Xue Zhong Liu. Molecular structure and regulation of p2x receptors with a special emphasis on the role of p2x2 in the auditory system. Journal of Cellular Physiology, 231:1656-1670, Aug 2016. URL: https://doi.org/10.1002/jcp.25274, doi:10.1002/jcp.25274. This article has 26 citations and is from a peer-reviewed journal.

9. (alde2023autosomaldominantnonsyndromic pages 16-17): Mirko Aldè, Giovanna Cantarella, Diego Zanetti, Lorenzo Pignataro, Ignazio La Mantia, Luigi Maiolino, Salvatore Ferlito, Paola Di Mauro, Salvatore Cocuzza, Jérôme René Lechien, Giannicola Iannella, Francois Simon, and Antonino Maniaci. Autosomal dominant non-syndromic hearing loss (dfna): a comprehensive narrative review. Biomedicines, 11:1616, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061616, doi:10.3390/biomedicines11061616. This article has 65 citations.

10. (chen2021generationandcharacterization pages 1-2): Xiaoya Chen, Clemer Abad, Zheng-yi Chen, Juan I Young, Channabasavaiah B Gurumurthy, Katherina Walz, and Xue Zhong Liu. Generation and characterization of a p2rx2 v60l mouse model for dfna41. Human molecular genetics, 30:985-995, Mar 2021. URL: https://doi.org/10.1093/hmg/ddab077, doi:10.1093/hmg/ddab077. This article has 10 citations and is from a domain leading peer-reviewed journal.

11. (chen2021generationandcharacterization pages 1-1): Xiaoya Chen, Clemer Abad, Zheng-yi Chen, Juan I Young, Channabasavaiah B Gurumurthy, Katherina Walz, and Xue Zhong Liu. Generation and characterization of a p2rx2 v60l mouse model for dfna41. Human molecular genetics, 30:985-995, Mar 2021. URL: https://doi.org/10.1093/hmg/ddab077, doi:10.1093/hmg/ddab077. This article has 10 citations and is from a domain leading peer-reviewed journal.

12. (dong2019efficientintroductionof pages 1-3): Yunpeng Dong, Tao Peng, Weijing Wu, Donghui Tan, Xuezhong Liu, and Dinghua Xie. Efficient introduction of an isogenic homozygous mutation to induced pluripotent stem cells from a hereditary hearing loss family using crispr/cas9 and single-stranded donor oligonucleotides. The Journal of International Medical Research, 47:1717-1730, Feb 2019. URL: https://doi.org/10.1177/0300060519829990, doi:10.1177/0300060519829990. This article has 12 citations.

13. (wei2025singledosegenomeediting pages 5-7): Wei Wei, Wenliang Zhu, Stewart Silver, Ariel M. Armstrong, Fletcher S. Robbins, Arun Prabhu Rameshbabu, Katherina Walz, Yizhou Quan, Wan Du, Yehree Kim, Artur A. Indzhykulian, Yilai Shu, Xue-Zhong Liu, and Zheng-Yi Chen. Single-dose genome editing therapy rescues auditory and vestibular functions in adult mice with dfna41 deafness. Journal of Clinical Investigation, Aug 2025. URL: https://doi.org/10.1172/jci187872, doi:10.1172/jci187872. This article has 5 citations and is from a highest quality peer-reviewed journal.

14. (wei2025singledosegenomeediting pages 18-18): Wei Wei, Wenliang Zhu, Stewart Silver, Ariel M. Armstrong, Fletcher S. Robbins, Arun Prabhu Rameshbabu, Katherina Walz, Yizhou Quan, Wan Du, Yehree Kim, Artur A. Indzhykulian, Yilai Shu, Xue-Zhong Liu, and Zheng-Yi Chen. Single-dose genome editing therapy rescues auditory and vestibular functions in adult mice with dfna41 deafness. Journal of Clinical Investigation, Aug 2025. URL: https://doi.org/10.1172/jci187872, doi:10.1172/jci187872. This article has 5 citations and is from a highest quality peer-reviewed journal.

15. (yan2013mutationofthe pages 3-4): Denise Yan, Yan Zhu, Tom Walsh, Dinghua Xie, Huijun Yuan, Asli Sirmaci, Taro Fujikawa, Ann Chi Yan Wong, Tze L. Loh, Lilin Du, M’hamed Grati, Srdjan M. Vlajkovic, Susan Blanton, Allen F. Ryan, Zheng-Yi Chen, Peter R. Thorne, Bechara Kachar, Mustafa Tekin, Hong-Bo Zhao, Gary D. Housley, Mary-Claire King, and Xue Z. Liu. Mutation of the atp-gated p2x2 receptor leads to progressive hearing loss and increased susceptibility to noise. Proceedings of the National Academy of Sciences, 110:2228-2233, Jan 2013. URL: https://doi.org/10.1073/pnas.1222285110, doi:10.1073/pnas.1222285110. This article has 196 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Nonsyndromic_Hearing_Loss_41-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.
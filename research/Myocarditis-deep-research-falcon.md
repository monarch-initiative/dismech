---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T15:03:02.030941'
end_time: '2026-08-28T15:12:33.085222'
duration_seconds: 571.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myocarditis
  mondo_id: ''
  category: Immune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 8
  validator_version: 0.2.1
term_validation:
  total_terms: 2
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  unresolvable_prefixes:
  - NCBI
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Myocarditis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myocarditis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Myocarditis** covering all of the
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
- **Disease Name:** Myocarditis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Myocarditis** covering all of the
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


# Myocarditis: comprehensive disease-characteristics report

## Executive summary

Myocarditis is an etiologically heterogeneous inflammatory disease of the myocardium. It ranges from a mild, self-limited chest-pain syndrome to fulminant cardiogenic shock, malignant ventricular arrhythmia, chronic inflammatory cardiomyopathy, transplantation, or death. Modern practice treats myocarditis as a **syndrome requiring etiologic and risk stratification**, rather than as one uniform disease. Cardiac magnetic resonance (CMR) is the principal noninvasive tissue-characterization test, while endomyocardial biopsy (EMB) remains the reference method for histologic, immunophenotypic, and pathogen-directed diagnosis—especially in high-risk disease. Recent work emphasizes overlap with inherited cardiomyopathies, immune-checkpoint-inhibitor toxicity, and inflammatory endotypes potentially amenable to targeted therapy. (lauriero2025acutemyocarditisand pages 1-2, caforio2024…prognosticutility pages 2-3, peretto2023myocardialinflammationas pages 2-3)

**Evidence note.** Human clinical evidence is identified as such below. Mechanistic claims are separated from animal, in-vitro, and computational evidence. The retrieved corpus did not reliably expose PMIDs for every article; therefore, DOI URLs and publication dates are supplied rather than inventing PMIDs. The brief quotations are exact wording available from retrieved abstracts.

## 1. Disease information

### Definition and scope

Acute myocarditis is focal or diffuse myocardial inflammation caused by direct infectious or toxic injury and/or a dysregulated immune response. A practical temporal definition places acute disease within approximately one month of onset; persistent inflammation with cardiac dysfunction can evolve into chronic inflammatory cardiomyopathy. “Inflammatory cardiomyopathy” generally denotes myocarditis accompanied by ventricular dysfunction, often operationalized as LVEF below 50%. (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 2-3)

A recent diagnostic review summarized the clinical reality: **“Most cases of myocarditis can be self-limiting without specific treatment”**, while stressing that early risk identification determines monitoring and escalation. Martens, Cooper, and Tang, *Journal of the American Heart Association*, September 2023, DOI: [10.1161/JAHA.123.031454](https://doi.org/10.1161/jaha.123.031454). (caforio2024…prognosticutility pages 2-3)

### Identifiers and synonyms

- **MONDO:** MONDO:0004496, myocarditis; validate against the current MONDO release before ingestion.
- **MeSH:** D009205, Myocarditis.
- **ICD-10-CM:** I40.-, acute myocarditis; I51.4, myocarditis, unspecified. Specific infectious forms may be coded under infection-plus-manifestation conventions.
- **ICD-11:** myocarditis is represented within inflammatory diseases of the heart; the exact extension/subtype code should be checked against the deployment’s current ICD-11 release.
- **Synonyms:** inflammatory myocardial disease; acute myocarditis; chronic myocarditis; inflammatory cardiomyopathy when dysfunction is present; myopericarditis when myocardial injury accompanies predominant pericarditis; perimyocarditis when myocardial disease predominates.
- **OMIM/Orphanet:** no single identifier adequately represents all myocarditis. Specific inherited cardiomyopathies or rare histologic entities may have separate entries, but generic myocarditis is not one Mendelian disorder.

The information here is aggregated disease-level evidence from registries, cohorts, guidelines, reviews, trials, biopsy series, and experimental studies—not an individual-patient EHR abstraction.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal or triggering factors

1. **Infectious:** enteroviruses including coxsackievirus B, adenovirus, influenza, SARS-CoV-2, HHV-6, EBV, CMV, HSV, parvovirus B19, HIV, hepatitis viruses, and less commonly bacteria, fungi, protozoa, or helminths. Detection of viral nucleic acid—particularly latent/endothelial-tropic viruses—does not by itself prove causal myocardial infection.
2. **Immune-mediated:** systemic lupus erythematosus, systemic sclerosis, vasculitis, inflammatory myopathy, eosinophilic syndromes, giant-cell myocarditis, sarcoidosis, and postinfectious autoimmunity.
3. **Drugs and toxins:** immune checkpoint inhibitors (anti-PD-1/PD-L1 and anti-CTLA-4), hypersensitivity-causing medicines, some chemotherapies, clozapine, cocaine/amphetamines, and other toxic exposures.
4. **Vaccination-associated:** myocarditis occurs rarely after mRNA COVID-19 vaccination, particularly in adolescent and young-adult males and commonly after dose 2. Reviews characterize it as generally milder and more self-limited than infection-associated myocarditis; vaccination also prevents COVID-19 and its cardiac complications. Proposed molecular mimicry and cytokine dysregulation remain hypotheses rather than settled causal mechanisms. Costa and Moniati, *Advances in Medicine*, April 2024, DOI: [10.1155/2024/4470326](https://doi.org/10.1155/2024/4470326). (costa2024theepidemiologyof pages 1-2)

### Genetic susceptibility—not usually simple causation

Myocarditis is usually multifactorial. Rare germline variants in cardiomyopathy genes can create a myocardium vulnerable to inflammatory “hot phases,” recurrent myocarditis, arrhythmias, or adverse remodeling. Repeatedly implicated genes include **DSP, PKP2, DSG2, DSC2, JUP, TTN, BAG3, LMNA, FLNC, DES, DMD, DYSF, MYH7, MYBPC3, RBM20, SCN5A, RYR2, LAMA4, and LDB3**. Desmosomal disease—especially **DSP**—is particularly important when recurrent episodes, ring-like or subepicardial LGE, ventricular arrhythmia, or family history are present. (lutokhina2025incidenceandimpact pages 1-2, peretto2023myocardialinflammationas pages 2-3)

TTN truncating variants illustrate susceptibility rather than a myocarditis-specific allele: they account for approximately 25% of familial and 18% of idiopathic DCM in the cited synthesis. Variant interpretation must follow ACMG/AMP and disease-specific ClinGen rules; the mere presence of a rare variant or VUS does not establish causality. (peretto2023myocardialinflammationas pages 11-13)

**Variant fields:** no universal recurrent pathogenic variant, allele frequency, founder mutation, or carrier frequency exists for myocarditis as a whole. Most relevant variants are rare, germline, heterozygous loss-of-function or missense alleles inherited according to the underlying cardiomyopathy—often autosomal dominant with incomplete, age-dependent penetrance and variable expressivity. Somatic mutation, anticipation, germline mosaicism, chromosomal aneuploidy, and repeat expansion are not established generic myocarditis mechanisms.

### Environmental and lifestyle risks

Male sex, adolescence/young adulthood, recent infection, autoimmune disease, cardiotoxic treatment, and intense exercise during active infection/inflammation are clinically important contexts. In one pre-pandemic estimate, incidence among people aged 35–39 was 6.1/100,000 in men versus 4.4/100,000 in women; one 2020 cohort was 82% male. (costa2024theepidemiologyof pages 1-2)

Smoking, alcohol, diet, and air pollution are important general cardiovascular exposures, but robust myocarditis-specific causal estimates are lacking. Strenuous exercise during acute myocarditis may amplify injury and arrhythmic risk; it should not be confused with habitual moderate exercise after documented recovery.

### Protective factors and gene–environment interactions

There is no validated protective germline allele or diet that prevents myocarditis. Practical protection consists of infection prevention, vaccination according to public-health guidance, avoidance of illicit stimulants and unnecessary cardiotoxic exposure, and refraining from strenuous exercise during systemic infection or active myocarditis. In genetically susceptible myocardium, infection or mechanical/adrenergic stress can act as a second hit. DMD/DYSF-associated membrane fragility has been linked to susceptibility to coxsackievirus injury, while inflammatory episodes may unmask desmosomal or DCM phenotypes. (lutokhina2025incidenceandimpact pages 2-4, peretto2023myocardialinflammationas pages 2-3)

## 3. Phenotypes

Clinical expression is variable across all ages. Pediatric cases may present with nonspecific respiratory or gastrointestinal symptoms; adults more often have chest pain, dyspnea, palpitations, or exercise intolerance. Older adults and patients with comorbidities may have worse hemodynamic tolerance.

- **Infarct-like phenotype:** acute chest pain, ST/T-wave changes, elevated troponin, and unobstructed coronary arteries. Suggested HPO: chest pain, elevated troponin, ST-segment abnormality.
- **Heart-failure phenotype:** dyspnea, fatigue, edema, tachycardia, reduced LVEF, elevated BNP/NT-proBNP. Severity ranges from mild dysfunction to cardiogenic shock. Suggested HPO: dyspnea, fatigue, peripheral edema, left ventricular systolic dysfunction, cardiomegaly, cardiogenic shock.
- **Arrhythmic phenotype:** palpitations, premature ventricular beats, ventricular tachycardia/fibrillation, atrial arrhythmia, high-grade atrioventricular block, syncope, or sudden death. Suggested HPO: palpitations, ventricular arrhythmia, atrioventricular block, syncope, sudden cardiac death.
- **Inflammatory/systemic phenotype:** fever, myalgia, elevated CRP/ESR, leukocytosis or eosinophilia, depending on cause. Suggested HPO: fever, elevated CRP, eosinophilia.
- **Imaging/pathology phenotype:** myocardial edema, nonischemic LGE, inflammatory infiltrates, myocyte necrosis; chronic cases develop fibrosis, ventricular dilation, or nondilated hypokinetic cardiomyopathy.

The ESC registry included biopsy-proven myocarditis (n=233), clinically suspected disease with abnormal CMR (n=222), and suspected disease with normal/inconclusive CMR (n=126), demonstrating that no single phenotype or test captures the whole spectrum. (caforio2024…prognosticutility pages 2-3)

**Frequency and quality of life:** reliable universal percentages for individual symptoms are unavailable because cohorts differ by referral threshold and diagnostic definition. Acute pain, hospitalization, activity restriction, arrhythmia anxiety, and reduced exercise capacity can markedly impair short-term quality of life. Persistent ventricular dysfunction, ICD implantation, or recurrent “hot phases” can produce long-term physical and psychological burden; myocarditis-specific EQ-5D/SF-36 reference norms are not established in the retrieved evidence.

## 4. Genetic and molecular information

### Causal genes and testing interpretation

There is no single “myocarditis gene.” Genes listed above cause inherited cardiomyopathy or membrane/cytoskeletal vulnerability and modify the response to environmental injury. Testing is most informative in recurrent myocarditis, family history of cardiomyopathy/sudden death, persistent dysfunction, extensive or characteristic LGE, malignant arrhythmia, conduction disease, or an arrhythmogenic-cardiomyopathy phenotype. (lutokhina2025incidenceandimpact pages 1-2, peretto2023myocardialinflammationas pages 2-3)

Recommended analysis is a curated cardiomyopathy/arrhythmia panel with copy-number detection; WES/WGS may be appropriate in unresolved familial disease. Results should be classified as pathogenic, likely pathogenic, VUS, likely benign, or benign. Cascade testing is appropriate only for pathogenic/likely pathogenic variants, not for VUS. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine unless syndromic features independently indicate them.

### Modifier and epigenetic evidence

Sex hormones, common genetic background, immune-response loci, and viral receptor expression probably modify penetrance, but clinically actionable modifiers are unvalidated. Altered microRNAs, chromatin state, and DNA methylation have been described experimentally; no epigenetic biomarker is approved for routine diagnosis or treatment selection. Large recurrent chromosomal abnormalities are not characteristic.

## 5. Environmental and infectious information

Cardiotropic pathogens may injure cardiomyocytes directly, activate endothelial and innate immune pathways, or trigger postinfectious autoimmunity. A 2025 cardiomyopathy cohort detected PVB19, HHV-6, EBV, CMV, HSV-1, and SARS-CoV-2 genomes, but its high inflammation prevalence reflects a selected referral population and should not be generalized to community myocarditis. (lutokhina2025incidenceandimpact pages 4-6, lutokhina2025incidenceandimpact pages 11-13, lutokhina2025incidenceandimpact pages 13-14)

Important noninfectious exposures include ICIs, hypersensitivity-provoking medications, stimulants, and selected occupational/toxic agents. Routine broad viral serology is generally less informative than targeted testing driven by clinical context; myocardial PCR is most meaningful when interpreted with histology, viral load/replication, cell localization, and immune findings.

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream trigger** → pathogen-associated or damage-associated molecular recognition → endothelial activation and innate immune recruitment → cytokine and inflammasome amplification → antigen presentation and adaptive T-cell/B-cell responses → cardiomyocyte necrosis/apoptosis and electrical instability → edema and impaired contraction → resolution or persistent immune activation → fibroblast activation, extracellular-matrix deposition, scar, ventricular remodeling, arrhythmia, and chronic inflammatory cardiomyopathy. (lauriero2025acutemyocarditisand pages 1-2, vosko2026giantcellmyocarditis pages 1-2, peretto2023myocardialinflammationas pages 11-13)

Relevant processes include GO inflammatory response, innate immune response, adaptive immune response, leukocyte migration, cytokine production, apoptotic process, necrotic cell death, extracellular-matrix organization, and cardiac muscle contraction.

### Cells and pathways

- **Cardiomyocytes** are the primary injured cells; death releases troponin and danger signals and impairs contraction/conduction.
- **Macrophages/monocytes** clear debris but also generate IL-1, IL-6, TNF, reactive oxygen species, and profibrotic signals.
- **CD4/CD8 T cells** mediate adaptive cytotoxic and autoimmune injury; Th17 biology is prominent in experimental giant-cell disease.
- **B cells/plasma cells** may generate anticardiac antibodies, including antibodies against DSG2 or titin, although direct pathogenicity varies.
- **Fibroblasts** execute downstream scar formation; endothelial cells and pericytes regulate vascular permeability and leukocyte trafficking.

NF-κB is a central inflammatory regulator; downstream TGF-β signaling promotes extracellular-matrix expression and suppresses matrix degradation. NLRP3–caspase-1–IL-1 signaling provides a mechanistic rationale for IL-1 blockade, but broad clinical efficacy is unproven. CVB3 models show abnormal titin phosphorylation, increased IL-6, and fibrosis; IL-6-receptor blockade improved experimental outcomes. (ricci2026severemyocardialinflammation pages 34-37, peretto2023myocardialinflammationas pages 11-13)

Suggested cell terms: cardiomyocyte, cardiac fibroblast, endothelial cell, pericyte, monocyte, macrophage, neutrophil, CD4-positive T cell, CD8-positive T cell, B cell, plasma cell, eosinophil, and multinucleated giant cell.

### Histologic endotypes

- **Lymphocytic:** most common; T-cell-rich infiltrates with associated myocyte injury.
- **Eosinophilic/hypersensitivity:** eosinophils, often associated with drugs or systemic eosinophilic disease.
- **Giant-cell:** destructive T-cell/macrophage inflammation with multinucleated giant cells and extensive necrosis; often rapidly progressive.
- **Granulomatous/cardiac sarcoidosis:** noncaseating granulomas; patchy distribution complicates biopsy.
- **ICI-associated:** frequently CD4/CD8 T-cell-rich injury, sometimes overlapping myositis and myasthenia gravis.

### Omics and advanced technologies

Bulk and single-cell studies support immune activation, altered contraction/conduction programs, fibroblast activation, and metabolic reprogramming. Giant-cell myocarditis profiling found adaptive/innate pathways upregulated and cardiac contraction/conduction genes downregulated; rat single-cell data identified Th17 cells and distinct macrophage states. (vosko2026giantcellmyocarditis pages 1-2)

Spatial transcriptomics and single-cell work in inherited arrhythmogenic cardiomyopathy—relevant to myocarditis-like “hot phases”—identifies regional cardiomyocyte degeneration, inflammatory macrophages, and fibro-inflammatory niches. These results are hypothesis-generating and not yet diagnostic assays. Proteomic, metabolomic, lipidomic, liquid-biopsy, and epigenomic signatures remain investigational; no profile has replaced CMR or EMB.

## 7. Anatomy

- **Primary organ/system:** heart/cardiovascular system; myocardium of one or both ventricles and sometimes atria.
- **Tissue:** cardiac muscle, interstitium, microvasculature, conduction tissue, and—in myopericarditis—the pericardium.
- **Distribution:** focal, multifocal, or diffuse; no fixed lateralization. CMR often shows subepicardial or mid-wall nonischemic injury, commonly inferolateral, but genetic and immune subtypes may differ.
- **Secondary involvement:** pulmonary/systemic congestion, hepatic and renal hypoperfusion, cerebral consequences of embolism or arrest, skeletal muscle/myasthenic overlap in ICI disease.
- **Subcellular compartments:** sarcolemma/desmosomes, sarcomere, mitochondria, cytosol/inflammasome, nucleus, extracellular matrix, and intercalated disc.

Suggested UBERON terms: heart, myocardium, left-ventricular myocardium, right-ventricular myocardium, interventricular septum, cardiac conduction system, coronary microvasculature, and pericardium.

## 8. Temporal development

Onset can be neonatal, pediatric, adult, or geriatric, but recognized disease is enriched in younger males. Presentation may be acute or fulminant over hours to weeks, subacute, recurrent/episodic, or chronic/insidious. Acute disease occurs within roughly one month; persistent hypokinetic disease beyond that interval may be classified as inflammatory cardiomyopathy. (lauriero2025acutemyocarditisand pages 1-2)

A useful conceptual sequence is: trigger/prodrome → acute injury/edema → early recovery or fulminant failure → convalescence with residual scar → complete resolution, recurrent inflammatory episodes, or chronic ventricular remodeling. The first days of shock, malignant arrhythmia, or AV block are the critical treatment window. Follow-up at approximately 3–6 months commonly reassesses symptoms, biomarkers, ECG/rhythm, ventricular function, and CMR where results alter management.

## 9. Inheritance and population epidemiology

Myocarditis itself is usually sporadic and multifactorial. When an underlying cardiomyopathy is found, inheritance follows that disorder—often autosomal dominant with incomplete penetrance and variable expressivity. X-linked inheritance is relevant to DMD-associated disease; recessive or mitochondrial disorders are uncommon contexts. There is no general carrier frequency, anticipation pattern, founder effect, or consanguinity estimate for myocarditis.

True population incidence is underestimated because mild cases escape diagnosis and definitions differ. A contemporary review cited 4.4/100,000 women and 6.1/100,000 men aged 35–39. Male predominance is consistent across conventional and vaccine-associated myocarditis. (costa2024theepidemiologyof pages 1-2)

Selected cardiomyopathy cohorts report much higher inflammation frequencies—ARVC 74.3%, DCM 56.7%, LVNC 54.4%, RCM 37.5%, and HCM 30.9%—but these figures derive from a specialized cohort using biopsy or a noninvasive antibody/CMR algorithm and are **not general-population prevalence estimates**. (lutokhina2025incidenceandimpact pages 16-17, lutokhina2025incidenceandimpact pages 1-2)

## 10. Diagnostics

### Clinical workflow

1. **Recognize a compatible syndrome:** chest pain, new heart failure, arrhythmia/AV block, shock, or unexplained troponin elevation.
2. **Initial tests:** high-sensitivity troponin, BNP/NT-proBNP, CBC with differential, CRP/ESR, metabolic profile, ECG, continuous rhythm monitoring, and echocardiography.
3. **Exclude alternatives:** acute coronary syndrome, Takotsubo syndrome, pulmonary embolism, sepsis-related injury, tachycardia-mediated cardiomyopathy, inherited cardiomyopathy, cardiac sarcoidosis, giant-cell disease, amyloidosis, and pericarditis without myocardial injury.
4. **CMR:** ventricular function, edema, hyperemia/injury, T1/T2 mapping, extracellular volume, and nonischemic LGE. Updated Lake Louise assessment seeks at least one T2-based marker of edema and one T1-based marker of nonischemic injury, interpreted in clinical context.
5. **EMB:** histology, immunohistochemistry, and targeted molecular testing. EMB is especially indicated for cardiogenic shock/fulminant disease, malignant arrhythmia, high-grade AV block, suspected giant-cell/eosinophilic/ICI disease, persistent biomarker elevation or dysfunction, or failure to respond to standard care. (lauriero2025acutemyocarditisand pages 1-2, caforio2024…prognosticutility pages 2-3, peretto2023myocardialinflammationas pages 2-3)

In the ESC registry, biopsy complications occurred in 4.7% of adults and 4.9% of children, with no procedure-related deaths, supporting performance in experienced centers. Sampling error remains important because disease can be patchy. (caforio2024…prognosticutility pages 2-3)

### Biomarkers and emerging diagnostics

Troponin documents injury but neither excludes myocarditis when normal nor defines etiology. BNP/NT-proBNP reflects hemodynamic stress. CRP, eosinophils, CK, autoantibodies, cytokines, microRNAs, cell-free nucleic acids, PET tracers, and AI-assisted imaging are being studied, but none independently establishes generic myocarditis. FDG-PET is useful when sarcoidosis is suspected or CMR is unavailable/contraindicated. (peretto2023myocardialinflammationas pages 2-3)

### Genetic and omics testing

Genetic testing is not universal screening. Use a phenotype-driven cardiomyopathy panel in recurrent/familial/high-risk cases; WES/WGS is second-line. RNA-seq, proteomics, metabolomics, and epigenomics are research tools. Population screening, newborn screening, and routine asymptomatic CMR are not recommended. Cascade screening is appropriate when a pathogenic cardiomyopathy variant is identified.

## 11. Outcomes and prognosis

Many uncomplicated infarct-like cases recover clinically, but residual LGE can persist. Adverse outcomes include recurrent myocarditis, sustained ventricular arrhythmia, AV block, chronic DCM, heart failure, thromboembolism, sudden death, mechanical support, transplantation, and death.

Poor prognostic features include cardiogenic shock, reduced LVEF, biventricular dysfunction, sustained ventricular arrhythmia, high-grade AV block, giant-cell histology, extensive/persistent LGE, ongoing troponin release, failure of early recovery, and pathogenic cardiomyopathy genotype. Reduced LVEF and need for immunomodulatory treatment predicted adverse outcomes in ESC registry data. (caforio2024…prognosticutility pages 2-3)

In a selected LVNC cohort, myocarditis independently predicted mortality (HR 5.8); treated patients improved from mean LVEF 36.8% to 40.3% and had death/transplantation of 20.9% versus 44.0% without immunosuppression. These observational results are confounded and should not justify indiscriminate immunosuppression. (lutokhina2025incidenceandimpact pages 11-13)

For DCM, morphologically verified myocarditis predicted lethal outcome (HR 3.6, 95% CI 1.433–9.249). Again, this is selected-cohort evidence rather than a universal prognostic calculator. (lutokhina2025incidenceandimpact pages 14-16)

## 12. Treatment and real-world implementation

### General strategy

- Hospitalize high-risk patients; monitor rhythm and hemodynamics.
- Treat congestion and ventricular dysfunction with guideline-directed heart-failure therapy as tolerated.
- Manage ventricular arrhythmias and AV block according to standard electrophysiology guidance, recognizing that temporary protection may be preferable while inflammation resolves.
- Treat shock with inotropes/vasopressors and early referral for VA-ECMO, temporary VAD, durable VAD, or transplantation where necessary.
- Avoid NSAIDs in isolated myocarditis with heart failure; they may be used cautiously when clinically significant pericarditis predominates and ventricular function is preserved.

A 2024 treatment review states: **“Treatment of myocarditis is often supportive, and the evidence for immunosuppression is scarce and debated.”** Ferone et al., *Journal of Cardiovascular Pharmacology*, May 2024, DOI: [10.1097/FJC.0000000000001542](https://doi.org/10.1097/fjc.0000000000001542). (ferone2024currenttreatmentand pages 11-11)

### Etiology/endotype-directed treatment

- **Routine presumed viral/idiopathic lymphocytic myocarditis:** supportive therapy; empirical immunosuppression is not universal.
- **Virus-negative, biopsy-proven inflammatory cardiomyopathy:** corticosteroid plus azathioprine has supportive randomized evidence from TIMIC, but requires careful pathogen exclusion and specialist supervision.
- **Giant-cell myocarditis:** urgent combination immunosuppression, commonly high-dose corticosteroid plus a calcineurin inhibitor and another T-cell-directed agent; early mechanical-support/transplant evaluation.
- **Eosinophilic/hypersensitivity myocarditis:** remove the offending agent and begin corticosteroids when clinically significant; treat systemic eosinophilic disease.
- **Cardiac sarcoidosis:** corticosteroid-based immunosuppression with steroid-sparing therapy and arrhythmia/device management.
- **ICI myocarditis:** immediately hold ICI therapy, admit and monitor, and initiate early high-dose intravenous corticosteroids in significant disease. Steroid-refractory options include mycophenolate, abatacept, IVIG, antithymocyte globulin, alemtuzumab, ruxolitinib, or other targeted strategies in expert centers. Evidence remains mainly observational; infliximab is controversial and generally avoided in moderate-to-severe heart failure. (ferone2024currenttreatmentand pages 11-11)
- **IL-1 blockade:** anakinra is biologically plausible, but ARAMIS did not show broad benefit in a largely low-risk cohort; severe hyperinflammatory cases remain an investigational niche.
- **Antiviral/antimicrobial therapy:** only for a demonstrated treatable pathogen or systemic infection; myocardial viral nucleic acid alone does not automatically indicate therapy.

Suggested NCIT concepts include corticosteroid therapy, immunosuppressive therapy, intravenous immunoglobulin, extracorporeal membrane oxygenation, ventricular-assist device therapy, heart transplantation, antiarrhythmic therapy, and cardiac rehabilitation.

### Pharmacogenomics and advanced therapeutics

No CPIC/PharmGKB genotype-guided myocarditis regimen is established. Gene therapy, CRISPR, ASOs, siRNA, and cell therapy are not approved treatments for myocarditis. Precision approaches currently mean identifying infectious, autoimmune, ICI-associated, eosinophilic, giant-cell, sarcoid, or inherited-cardiomyopathy endotypes—not editing a myocarditis gene.

## 13. Prevention

**Primary prevention:** vaccination and infection-control measures; prompt management of systemic infection; avoidance of cocaine/amphetamines and unnecessary cardiotoxic drugs; baseline and early surveillance protocols for selected ICI recipients. The small myocarditis risk after mRNA vaccination must be balanced against protection from COVID-19 and its complications. (costa2024theepidemiologyof pages 1-2)

**Secondary prevention:** rapid evaluation of chest pain, dyspnea, syncope, palpitations, or exercise intolerance after infection, vaccination, or ICI exposure; early troponin/ECG/echo testing; genetic evaluation in recurrent or familial disease.

**Tertiary prevention:** restrict strenuous exercise during active disease—commonly 3–6 months, individualized by phenotype and contemporary guidance. Return requires resolution of symptoms and injury markers, recovered ventricular function, and absence of clinically important arrhythmia; persistent scar or genotype-positive disease may justify stricter assessment. Optimize heart-failure therapy, rhythm surveillance, and family screening where appropriate. (ferone2024currenttreatmentand pages 11-11)

No prophylactic medication, population screening program, prenatal test, or newborn screen exists for generic myocarditis.

## 14. Other species and natural disease

Naturally occurring myocarditis occurs in dogs, cats, cattle, horses, pigs, nonhuman primates, and wildlife from infectious, toxic, parasitic, and immune causes. Examples include canine protozoal/vector-borne or viral myocarditis, feline infectious myocarditis, and enteroviral disease in susceptible animals. Species-specific pathogen ecology makes direct extrapolation hazardous. Generic myocarditis is not ordinarily zoonotically transmitted; zoonotic concern belongs to the causal pathogen, not myocardial inflammation itself.

Suggested taxa include *Homo sapiens* (NCBI:9606), *Mus musculus* (10090), *Rattus norvegicus* (10116), *Canis lupus familiaris* (9615), *Felis catus* (9685), and *Danio rerio* (7955). No universal VBO breed association or single conserved ortholog explains natural myocarditis.

## 15. Model organisms and experimental systems

### Principal models

- **CVB3 mouse myocarditis:** reproduces viral replication, innate/adaptive inflammation, necrosis, sex effects, and later fibrosis. It is valuable for antiviral and immunomodulatory studies but depends strongly on strain, sex, age, inoculum, and viral passage; many human cases are not enteroviral.
- **Experimental autoimmune myocarditis:** cardiac-myosin peptide plus adjuvant in susceptible mice/rats produces T-cell-driven myocarditis and later DCM; useful for autoimmunity and IL-1/IL-6/Th17 biology, but the artificial immunization does not reproduce most human initiating events.
- **Giant-cell myocarditis models:** cardiac-myosin immunization in rats reproduces destructive T-cell/macrophage disease. Rat single-cell data identify Th17 cytokines and macrophage giant-cell contributors, but species and induction differences remain substantial. (vosko2026giantcellmyocarditis pages 1-2)
- **Genetic models:** Dsg2, Pkp2, Dsp, Dmd, Dysf, and related knock-out/knock-in animals model inflammatory “hot phases” in inherited cardiomyopathy.
- **Human iPSC-cardiomyocytes, engineered heart tissue, and organoids:** permit patient-specific viral entry, desmosomal failure, cytokine injury, electrophysiology, and drug screening; limitations include fetal-like maturation, incomplete immune/vascular systems, and absent whole-organ hemodynamics.

The CVB3 literature links infection to impaired titin phosphorylation, IL-6 elevation, and fibrosis, with improvement after IL-6-receptor blockade—strong preclinical support, but not proof of clinical efficacy. (peretto2023myocardialinflammationas pages 11-13)

## Current research and active implementation

Current programs emphasize prognosis, genotype–phenotype overlap, post-vaccine outcomes, CMR/PET molecular imaging, and biomarker-guided follow-up. Examples identified in ClinicalTrials.gov searches include:

- **NCT04844151:** acute myocarditis registry integrating prognostic, histologic, immunologic, biological, imaging, and clinical assessment; recruiting; planned n=1,400.
- **NCT06010199:** biomarker risk stratification; recruiting; planned n=1,000.
- **NCT06189053:** long-term outcomes after myocarditis following Moderna mRNA vaccination; active, not recruiting; n=1,500.
- **NCT05125965:** early CMR diagnosis of immunotherapy-induced myocarditis; active, not recruiting; n=200.
- **NCT05949450:** prognostic role of high-sensitivity troponin during follow-up; not yet recruiting; n=244.

Registry status and enrollment should be verified at [ClinicalTrials.gov](https://clinicaltrials.gov/) before production use.

## Ontology-ready summary

The following compact table is suitable for knowledge-base mapping; accession numbers marked for validation should be checked against live ontology releases.

| Domain | Recommended identifier/ontology term | Meaning/use | Evidence/qualification |
|---|---|---|---|
| Disease | **MONDO:0004496** *(validate in live MONDO release)* | Myocarditis disease concept for cross-ontology mapping and KB normalization | Commonly used MONDO identifier for myocarditis; validate against current ontology release before production use. Myocarditis is a heterogeneous inflammatory myocardial syndrome rather than a single Mendelian disorder (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 2-3) |
| Disease | **MeSH: D009205** | NLM MeSH descriptor for indexing literature on myocarditis | Stable literature-indexing term; useful for PubMed/MeSH harmonization (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 2-3) |
| Disease classification | **ICD-10-CM: I40** | Acute myocarditis diagnosis code family | Appropriate for acute presentations; aligns with clinical spectrum emphasizing recent-onset inflammatory myocardial injury (lauriero2025acutemyocarditisand pages 1-2, caforio2024…prognosticutility pages 2-3) |
| Disease classification | **ICD-10-CM: I51.4** | Myocarditis, unspecified | Use when documentation confirms myocarditis without subclassification; less specific than acute myocarditis coding (lauriero2025acutemyocarditisand pages 1-2) |
| Disease resources | **No single OMIM/Orphanet ID recommended** | Avoid forcing myocarditis into a monogenic rare-disease identifier slot | Do **not** invent OMIM/Orphanet IDs; myocarditis spans infectious, autoimmune, toxic/drug-related, and genetically susceptible forms (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 2-3) |
| Phenotype (symptom) | **HPO: Chest pain** *(validate HP accession in live HPO)* | Common presenting symptom, especially infarct-like/pseudoinfarction phenotype | Frequently reported in acute myocarditis presentations; exact HPO accession should be verified live (caforio2024…prognosticutility pages 2-3, peretto2023myocardialinflammationas pages 2-3) |
| Phenotype (symptom) | **HPO: Dyspnea** *(validate HP accession in live HPO)* | Symptom of heart failure/hemodynamic compromise | Seen across acute and chronic inflammatory cardiomyopathy phenotypes (lauriero2025acutemyocarditisand pages 1-2, caforio2024…prognosticutility pages 2-3) |
| Phenotype (symptom) | **HPO: Fatigue** *(validate HP accession in live HPO)* | Nonspecific constitutional/cardiac symptom | Common but nonspecific; useful as supportive phenotype only (lauriero2025acutemyocarditisand pages 1-2) |
| Phenotype (symptom) | **HPO: Palpitations** *(validate HP accession in live HPO)* | Symptom suggesting atrial/ventricular arrhythmia | Myocarditis may present with arrhythmias even without classic heart-failure syndrome (caforio2024…prognosticutility pages 2-3, peretto2023myocardialinflammationas pages 2-3) |
| Phenotype (symptom) | **HPO: Syncope** *(validate HP accession in live HPO)* | Transient loss of consciousness related to malignant arrhythmia/hemodynamic instability | Important high-risk presentation trigger for urgent workup (caforio2024…prognosticutility pages 2-3) |
| Phenotype (symptom/sign) | **HPO: Fever** *(validate HP accession in live HPO)* | Febrile inflammatory/infectious presentation | Supports inflammatory trigger but is not required for diagnosis (lauriero2025acutemyocarditisand pages 1-2) |
| Phenotype (laboratory) | **HPO: Elevated cardiac troponin level** *(validate HP accession in live HPO)* | Biomarker evidence of cardiomyocyte injury | Acute myocarditis commonly shows elevated high-sensitivity troponin; useful in diagnosis and follow-up (lauriero2025acutemyocarditisand pages 1-2, costa2024theepidemiologyof pages 1-2) |
| Phenotype (imaging/functional) | **HPO: Ventricular dysfunction** *(validate HP accession in live HPO)* | Reduced systolic performance/LV or biventricular dysfunction | Central phenotype in inflammatory cardiomyopathy and prognostic assessment (lauriero2025acutemyocarditisand pages 1-2, caforio2024…prognosticutility pages 2-3) |
| Phenotype (rhythm) | **HPO: Cardiac arrhythmia** *(validate HP accession in live HPO)* | Broad rhythm-disturbance phenotype | Includes atrial and ventricular arrhythmias; a recognized myocarditis presentation (caforio2024…prognosticutility pages 2-3, peretto2023myocardialinflammationas pages 2-3) |
| Phenotype (critical illness) | **HPO: Cardiogenic shock** *(validate HP accession in live HPO)* | Fulminant hemodynamic collapse phenotype | Indicates severe/fulminant myocarditis and is a major biopsy/treatment-escalation trigger (lauriero2025acutemyocarditisand pages 1-2, caforio2024…prognosticutility pages 2-3) |
| Anatomy | **UBERON: heart** *(validate UBERON accession in live release)* | Primary organ affected | Heart-level anatomical anchor for disease localization (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 2-3) |
| Anatomy | **UBERON: myocardium** *(validate UBERON accession in live release)* | Primary tissue targeted by inflammation | Core tissue compartment for pathology, MRI, and biopsy annotation (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 2-3) |
| Cell type | **CL: cardiomyocyte** *(validate CL accession in live release)* | Primary injured parenchymal cell | Cardiomyocyte injury/necrosis drives troponin release and systolic dysfunction (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 11-13) |
| Cell type | **CL: T cell** *(validate CL accession in live release)* | Major adaptive immune effector cell | T-cell infiltrates are central in lymphocytic myocarditis and giant-cell myocarditis biology (peretto2023myocardialinflammationas pages 2-3, vosko2026giantcellmyocarditis pages 1-2) |
| Cell type | **CL: macrophage** *(validate CL accession in live release)* | Major innate immune/injury-response cell | Macrophages contribute to inflammation, cytokine signaling, and remodeling (lutokhina2025incidenceandimpact pages 16-17, vosko2026giantcellmyocarditis pages 1-2) |
| Cell type | **CL: fibroblast** *(validate CL accession in live release)* | Matrix-producing stromal cell in repair/fibrosis | Fibroblast activation links inflammation to fibrosis and adverse remodeling (vosko2026giantcellmyocarditis pages 1-2, peretto2023myocardialinflammationas pages 11-13) |
| Cell type | **CL: endothelial cell** *(validate CL accession in live release)* | Vascular interface cell relevant to trafficking and edema | Important in leukocyte recruitment and myocardial inflammatory niche interactions (peretto2023myocardialinflammationas pages 2-3) |
| Biological process | **GO: inflammatory response** *(validate GO accession in live release)* | General disease-process umbrella term | Captures core inflammatory biology across etiologies (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 2-3) |
| Biological process | **GO: innate immune response** *(validate GO accession in live release)* | Early trigger/amplification program | Supported by inflammasome, macrophage, complement, and cytokine activation evidence (ricci2026severemyocardialinflammation pages 34-37, peretto2023myocardialinflammationas pages 11-13) |
| Biological process | **GO: adaptive immune response** *(validate GO accession in live release)* | Antigen-driven T/B-cell response | Relevant especially in autoimmune, giant-cell, and postinfectious phenotypes (peretto2023myocardialinflammationas pages 2-3, vosko2026giantcellmyocarditis pages 1-2) |
| Biological process | **GO: cell death** *(validate GO accession in live release)* | Cardiomyocyte injury/necrosis/apoptosis | Explains biomarker release and contractile dysfunction; downstream of immune injury or direct infection (vosko2026giantcellmyocarditis pages 1-2, peretto2023myocardialinflammationas pages 11-13) |
| Biological process | **GO: extracellular matrix organization / fibrosis** *(validate GO accession in live release)* | Remodeling/scarring program | Useful for chronic inflammatory cardiomyopathy and arrhythmic risk annotation (vosko2026giantcellmyocarditis pages 1-2, peretto2023myocardialinflammationas pages 11-13) |
| Diagnostic concept | **CMR using updated Lake Louise criteria** *(guideline concept, not ontology ID)* | Noninvasive tissue characterization for edema/injury | Strong diagnostic role, but EMB remains gold standard for definitive etiologic/histologic diagnosis (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 2-3) |
| Diagnostic concept | **Endomyocardial biopsy (EMB)** *(procedure concept)* | Gold-standard histology/immunohistochemistry/molecular testing | Most specific tool for subtype confirmation and therapy guidance in high-risk or unclear cases (caforio2024…prognosticutility pages 2-3, peretto2023myocardialinflammationas pages 2-3) |
| Intervention | **NCIT-style: Corticosteroid therapy** *(map to local NCIT term/live code)* | First-line immunosuppression in selected immune-mediated myocarditis subtypes | Not routine for all cases; subtype- and biopsy-context dependent (e.g., giant-cell, eosinophilic, ICI-associated) (ferone2024currenttreatmentand pages 11-11) |
| Intervention | **NCIT-style: Immunosuppressive therapy** *(map to live NCIT)* | Broad category including azathioprine, mycophenolate, calcineurin inhibitors | Evidence strongest in virus-negative inflammatory cardiomyopathy and specific severe immune phenotypes (ferone2024currenttreatmentand pages 11-11, lutokhina2025incidenceandimpact pages 14-16) |
| Intervention | **NCIT-style: Intravenous immunoglobulin** *(map to live NCIT)* | Immunomodulatory adjunct in selected cases | Used variably; evidence mixed and context-specific (ferone2024currenttreatmentand pages 11-11) |
| Intervention | **NCIT-style: Interleukin-1 inhibition / anakinra therapy** *(map to live NCIT)* | Targeted anti-inflammatory strategy under active investigation | Mechanistically linked to inflammasome/IL-1 signaling; current evidence strongest in selected severe/refractory phenotypes rather than broad low-risk use (peretto2023myocardialinflammationas pages 11-13) |
| Intervention | **NCIT-style: Guideline-directed heart failure therapy** *(map to live NCIT)* | Standard supportive therapy for ventricular dysfunction | Core management across many presentations regardless of etiology (ferone2024currenttreatmentand pages 11-11) |
| Intervention | **NCIT-style: Mechanical circulatory support** *(map to live NCIT)* | Rescue support for fulminant/cardiogenic-shock presentations | Important in fulminant myocarditis and bridge-to-recovery/decision pathways (ferone2024currenttreatmentand pages 11-11) |
| Intervention | **NCIT-style: Exercise restriction / sports disqualification** *(map to local concept if NCIT unavailable)* | Secondary prevention to reduce arrhythmic risk during recovery | Common expert-management principle after acute myocarditis; timing of return depends on recovery and risk reassessment (ferone2024currenttreatmentand pages 11-11) |


*Table: This table provides compact disease, phenotype, anatomy, cell-type, process, and intervention terms suitable for a myocarditis knowledge base. It emphasizes where identifiers should be validated live and avoids inventing single-disease Mendelian IDs for this etiologically heterogeneous condition.*

## Evidence gaps and expert interpretation

The strongest present-day consensus is that myocarditis management should be **risk- and endotype-directed**. CMR has widened noninvasive diagnosis, but EMB remains indispensable when histology changes treatment. Genetics increasingly explains recurrence and inflammatory presentations in cardiomyopathy, yet most detected variants are susceptibility factors—not proof that myocarditis is monogenic. Broad empirical immunosuppression remains unsupported; the clearest indications are giant-cell, eosinophilic, sarcoid, ICI-associated, systemic autoimmune, and carefully characterized virus-negative inflammatory disease. (lauriero2025acutemyocarditisand pages 1-2, peretto2023myocardialinflammationas pages 2-3, ferone2024currenttreatmentand pages 11-11)

Major unresolved needs are validated noninvasive endotyping, harmonized diagnostic definitions, randomized treatment trials in high-risk disease, genotype-informed surveillance, pediatric evidence, and prospective quality-of-life data. Apparent treatment benefits in selected observational cardiomyopathy cohorts—such as lower death/transplantation with immunosuppression—must not be generalized without biopsy/pathogen context and randomized confirmation. (lutokhina2025incidenceandimpact pages 11-13, lutokhina2025incidenceandimpact pages 13-14, lutokhina2025incidenceandimpact pages 14-16)

References

1. (lauriero2025acutemyocarditisand pages 1-2): Francesco Lauriero, Camilla Vittoria Vita, Alessio Perazzolo, Giovanni Sanseverino, Eleonora Moliterno, Giuseppe Rovere, Riccardo Marano, and Luigi Natale. Acute myocarditis and inflammatory cardiomyopathies: insights from cardiac magnetic resonance findings. Echocardiography (Mount Kisco, N.y.), Feb 2025. URL: https://doi.org/10.1111/echo.70099, doi:10.1111/echo.70099. This article has 7 citations.

2. (caforio2024…prognosticutility pages 2-3): ALP Caforio, JP Kaski, and JR Gimeno. … prognostic utility in paediatric and adult myocarditis in the european society of cardiology eurobservational research programme cardiomyopathy and myocarditis …. Unknown journal, 2024.

3. (peretto2023myocardialinflammationas pages 2-3): Giovanni Peretto, Elena Sommariva, Chiara Di Resta, Martina Rabino, Andrea Villatore, Davide Lazzeroni, Simone Sala, Giulio Pompilio, and Leslie T. Cooper. Myocardial inflammation as a manifestation of genetic cardiomyopathies: from bedside to the bench. Apr 2023. URL: https://doi.org/10.3390/biom13040646, doi:10.3390/biom13040646. This article has 36 citations.

4. (costa2024theepidemiologyof pages 1-2): Christos Costa and Foteini Moniati. The epidemiology of covid-19 vaccine-induced myocarditis. Advances in Medicine, 2024:1-17, Apr 2024. URL: https://doi.org/10.1155/2024/4470326, doi:10.1155/2024/4470326. This article has 13 citations.

5. (lutokhina2025incidenceandimpact pages 1-2): Yulia Lutokhina, Elena Zaklyazminskaya, Evgeniya Kogan, Andrei Nartov, Valeriia Nartova, and Olga Blagova. Incidence and impact of myocarditis in genetic cardiomyopathies: inflammation as a potential therapeutic target. Jan 2025. URL: https://doi.org/10.3390/genes16010051, doi:10.3390/genes16010051. This article has 4 citations.

6. (peretto2023myocardialinflammationas pages 11-13): Giovanni Peretto, Elena Sommariva, Chiara Di Resta, Martina Rabino, Andrea Villatore, Davide Lazzeroni, Simone Sala, Giulio Pompilio, and Leslie T. Cooper. Myocardial inflammation as a manifestation of genetic cardiomyopathies: from bedside to the bench. Apr 2023. URL: https://doi.org/10.3390/biom13040646, doi:10.3390/biom13040646. This article has 36 citations.

7. (lutokhina2025incidenceandimpact pages 2-4): Yulia Lutokhina, Elena Zaklyazminskaya, Evgeniya Kogan, Andrei Nartov, Valeriia Nartova, and Olga Blagova. Incidence and impact of myocarditis in genetic cardiomyopathies: inflammation as a potential therapeutic target. Jan 2025. URL: https://doi.org/10.3390/genes16010051, doi:10.3390/genes16010051. This article has 4 citations.

8. (lutokhina2025incidenceandimpact pages 4-6): Yulia Lutokhina, Elena Zaklyazminskaya, Evgeniya Kogan, Andrei Nartov, Valeriia Nartova, and Olga Blagova. Incidence and impact of myocarditis in genetic cardiomyopathies: inflammation as a potential therapeutic target. Jan 2025. URL: https://doi.org/10.3390/genes16010051, doi:10.3390/genes16010051. This article has 4 citations.

9. (lutokhina2025incidenceandimpact pages 11-13): Yulia Lutokhina, Elena Zaklyazminskaya, Evgeniya Kogan, Andrei Nartov, Valeriia Nartova, and Olga Blagova. Incidence and impact of myocarditis in genetic cardiomyopathies: inflammation as a potential therapeutic target. Jan 2025. URL: https://doi.org/10.3390/genes16010051, doi:10.3390/genes16010051. This article has 4 citations.

10. (lutokhina2025incidenceandimpact pages 13-14): Yulia Lutokhina, Elena Zaklyazminskaya, Evgeniya Kogan, Andrei Nartov, Valeriia Nartova, and Olga Blagova. Incidence and impact of myocarditis in genetic cardiomyopathies: inflammation as a potential therapeutic target. Jan 2025. URL: https://doi.org/10.3390/genes16010051, doi:10.3390/genes16010051. This article has 4 citations.

11. (vosko2026giantcellmyocarditis pages 1-2): Ivan Vosko and Markus Wallner. Giant cell myocarditis: from immune pathogenesis to contemporary management. Heart Failure Reviews, Aug 2026. URL: https://doi.org/10.1007/s10741-026-10668-6, doi:10.1007/s10741-026-10668-6. This article has 0 citations and is from a peer-reviewed journal.

12. (ricci2026severemyocardialinflammation pages 34-37): Jacob C Ricci, Logan P Macomb, Emily R Whelan, Katherine Gegoutchadze, Cormac J Davis, Kyra G Ritter, Priya Tomerlin, Ashley A Darakjian, Nick A Farahani, Lauren M Parrow, Danielle J Beetler, Max W Strandes, Damian N Di Florio, Sami Khatib, Jude Elsaygh, Leslie T Cooper, Jack F Price, DeLisa Fairweather, Dipankar Gupta, and Katelyn A Bruno. Severe myocardial inflammation and necrosis in juvenile mice compared with adult mice with coxsackievirus b3 myocarditis. bioRxiv, Aug 2026. URL: https://doi.org/10.64898/2026.08.20.746108, doi:10.64898/2026.08.20.746108. This article has 0 citations.

13. (lutokhina2025incidenceandimpact pages 16-17): Yulia Lutokhina, Elena Zaklyazminskaya, Evgeniya Kogan, Andrei Nartov, Valeriia Nartova, and Olga Blagova. Incidence and impact of myocarditis in genetic cardiomyopathies: inflammation as a potential therapeutic target. Jan 2025. URL: https://doi.org/10.3390/genes16010051, doi:10.3390/genes16010051. This article has 4 citations.

14. (lutokhina2025incidenceandimpact pages 14-16): Yulia Lutokhina, Elena Zaklyazminskaya, Evgeniya Kogan, Andrei Nartov, Valeriia Nartova, and Olga Blagova. Incidence and impact of myocarditis in genetic cardiomyopathies: inflammation as a potential therapeutic target. Jan 2025. URL: https://doi.org/10.3390/genes16010051, doi:10.3390/genes16010051. This article has 4 citations.

15. (ferone2024currenttreatmentand pages 11-11): Emma Ferone, Amitai Segev, Erika Tempo, Piero Gentile, Ahmed Elsanhoury, Chiara Baggio, Jessica Artico, Prashan Bhatti, Paul Scott, Emanuele Bobbio, Marco Merlo, Pietro Ameri, Gianfranco Sinagra, Carsten Tschöpe, Daniel Bromage, and Antonio Cannata. Current treatment and immunomodulation strategies in acute myocarditis. May 2024. URL: https://doi.org/10.1097/fjc.0000000000001542, doi:10.1097/fjc.0000000000001542. This article has 26 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Myocarditis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `NCBI`.

1 of 2 terms resolved to a current term; the rest could not be looked up either way.
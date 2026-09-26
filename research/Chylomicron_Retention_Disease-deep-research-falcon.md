---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:56:35.054381'
end_time: '2026-09-05T18:07:16.471470'
duration_seconds: 641.42
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Chylomicron Retention Disease
  mondo_id: MONDO:0009528
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 2
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0009528
    reported_labels:
    - if available
    ontology_label: chylomicron retention disease
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Chylomicron_Retention_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chylomicron Retention Disease
- **MONDO ID:** MONDO:0009528 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chylomicron Retention Disease** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Chylomicron Retention Disease
- **MONDO ID:** MONDO:0009528 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Chylomicron Retention Disease** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# Chylomicron Retention Disease: Disease-Characteristics Research Report

## Executive summary

Chylomicron retention disease (CRD), or Anderson disease, is an ultra-rare, usually infancy-onset Mendelian disorder in which biallelic pathogenic variants in **SAR1B** impair COPII-dependent export of pre-chylomicrons from the enterocyte endoplasmic reticulum (ER) to the Golgi. Dietary lipid consequently accumulates within enterocytes, postprandial chylomicrons and apolipoprotein B-48 are absent or markedly reduced, and patients develop fat malabsorption, diarrhea, steatorrhea, growth failure, hypocholesterolemia, and fat-soluble-vitamin deficiency. Lifelong dietary and vitamin treatment usually controls gastrointestinal disease and substantially reduces irreversible neurologic, retinal, skeletal, muscular, and cardiac complications, but it does not correct the underlying trafficking defect. Evidence remains dominated by case reports, small cohorts, cell systems, and engineered animals; there are no randomized therapeutic trials or validated survival estimates.

The following table summarizes the principal knowledge-base fields.

| Domain | Key finding/statistic | Evidence type | Ontology suggestions |
|---|---|---|---|
| Identity/etiology | Chylomicron retention disease (CRD; Anderson disease) is an ultra-rare, autosomal-recessive intestinal lipid-malabsorption disorder caused principally by biallelic **SAR1B** loss-of-function variants; estimated prevalence is **<1 per 1,000,000** (OpenTargets Search: chylomicron retention disease-SAR1B, peretti2018lessonsfromchylomicron pages 1-3) | Aggregated disease resource; human molecular evidence | MONDO:0009528; chylomicron retention disease; Anderson disease |
| Core phenotype frequencies | In a molecularly confirmed 16-patient cohort/literature synthesis: diarrhea **100%**, steatorrhea **85%**, failure to thrive **80%**, abdominal distension **65%**, vomiting **60%**, elevated CK **60%**, vitamin E deficiency **95%**, vitamin A deficiency **70%**, and vitamin D and K deficiencies **45% each** (peretti2010guidelinesforthe pages 3-4) | Human clinical cohort and literature review | Chronic diarrhea; steatorrhea; failure to thrive; abdominal distension; vomiting; elevated serum creatine kinase; fat-soluble-vitamin deficiency |
| Lipid signature | Low total cholesterol, LDL-C, and HDL-C occurred in **100%** of the summarized genotyped cases; triglycerides were normal in **90%**, and the oral fat-load response was negative in **100%** (peretti2010guidelinesforthe pages 3-4) | Human biochemical evidence | Hypocholesterolemia; decreased LDL cholesterol; decreased HDL cholesterol; normal circulating triglyceride concentration |
| Diagnostic signature | Typical combination: infancy-onset fat malabsorption, total/LDL cholesterol near **50% of normal**, moderately low HDL, normal triglycerides, absent postprandial chylomicrons/apoB-48, white duodenal mucosa, and enterocytes distended by lipid droplets or membrane-bound chylomicron-like particles; confirm with biallelic **SAR1B** variants (georges2011molecularanalysisand pages 1-2, peretti2018lessonsfromchylomicron pages 1-3, ferreira2018chylomicronretentiondisease pages 6-7) | Human laboratory, endoscopic, histopathologic, and genetic evidence | Absent postprandial chylomicrons; lipid accumulation in enterocytes; white intestinal mucosa; small-intestinal biopsy |
| Mechanism | SEC12-mediated GDP–GTP exchange activates SAR1B at ER exit sites; SAR1B recruits SEC23–SEC24 and SEC13–SEC31 COPII coats. Pathogenic dysfunction blocks pre-chylomicron ER-to-Golgi trafficking and/or Golgi fusion, causing enterocyte lipid retention and reduced intestinal lipid export (tang2023cargoselectionin pages 2-3, levy2024unravelingchylomicronretention pages 7-9) | Human genetics plus biochemical and cell-biological evidence | GO:0006888 ER-to-Golgi vesicle-mediated transport; COPII-coated ER-to-Golgi transport vesicle; GTPase activity; protein transport |
| Secondary mechanisms | SAR1B-deficient Caco-2/15 cells have reduced chylomicron and HDL formation, impaired cholesterol efflux, and increased lipid peroxidation; oxidative stress, inflammation, and ER stress are plausible downstream contributors, but their clinical importance remains incompletely established (sane2017understandingchylomicronretention pages 9-10, levy2024unravelingchylomicronretention pages 10-12, levy2024unravelingchylomicronretention pages 1-2) | In-vitro evidence; review-level inference for human complications | Oxidative stress; endoplasmic-reticulum stress; inflammatory response; cholesterol efflux |
| Genetics/variants | **SAR1B** (formerly **SARA2**; chromosome **5q31.1**) has eight exons. Representative disease variants include frameshift **p.Leu28Argfs*7** and **p.Asp48Thrfs*17**, nonsense **p.Glu122***, exon-2 deletion, and missense **p.Asp137Asn**, **p.Ser179Arg**, and **p.Gly185Val** (charcosset2008andersonorchylomicron pages 1-2, georges2011molecularanalysisand pages 1-2, charcosset2008andersonorchylomicron pages 8-9) | Human germline molecular evidence and functional modeling | SAR1B; secretion-associated Ras-related GTPase 1B; germline pathogenic variant; loss of function |
| Modifiers/expressivity | Clinical severity varies even among variants predicted to abolish function. Increased intestinal **SAR1A** expression does not fully compensate; a co-occurring **PCSK9 p.Leu21dup** variant showed no clear additional effect. Proposed modifiers such as **APOB**, **MTTP**, and **ABCG5/ABCG8** remain unproven (georges2011molecularanalysisand pages 8-11, georges2011molecularanalysisand pages 1-2, charcosset2008andersonorchylomicron pages 8-9) | Human expression data; candidate-modifier inference | Variable expressivity; SAR1A; PCSK9; APOB; MTTP; ABCG5; ABCG8 |
| Treatment doses | Supportive therapy includes restriction of long-chain fat, adequate calories, optional medium-chain triglycerides, omega-6 at **3–5% of energy**, omega-3 at **0.5–1%**, vitamin E **50 IU/kg/day**, vitamin A **15,000 IU/day**, vitamin K **15 mg/week**, and vitamin D **800–1,200 IU/day** or age-adjusted intermittent dosing. Doses require biochemical and toxicity monitoring (peretti2010guidelinesforthe pages 10-11, peretti2010guidelinesforthe pages 9-10) | Expert guideline based on literature and two-center experience | Low-fat diet; medium-chain triglyceride supplementation; vitamin E supplementation; vitamin A supplementation; vitamin D supplementation; vitamin K supplementation; dietary counseling |
| Surveillance | Annual childhood assessment: growth, gastrointestinal and neurologic symptoms, diet, lipid profile, liver enzymes, fat-soluble vitamins, essential fatty acids, CBC, and CK. After age 10, liver ultrasound and neurologic, muscular, ophthalmologic, and bone assessment approximately every three years; adult echocardiography every three years was proposed (peretti2010guidelinesforthe pages 10-11, peretti2010guidelinesforthe pages 9-10) | Expert guideline/clinical practice recommendation | Growth monitoring; liver ultrasonography; ophthalmologic examination; neurologic examination; bone densitometry; echocardiography |
| Models/recent research | CRISPR Sar1b-mutant/deletion mice reproduce steatorrhea, malabsorption, failed chylomicron secretion, hypocholesterolemia, and hypoalphalipoproteinemia; homozygous states are usually embryonic/neonatal lethal. An **8-week, 60%-fat diet** exposed genotype- and sex-dependent lipid, insulin, hepatic-steatosis, fatty-acid, and ER-stress effects; females were relatively protected (auclair2023highfatdietreveals pages 1-2, levy2024unravelingchylomicronretention pages 10-12, auclair2023highfatdietreveals pages 11-13, auclair2023highfatdietreveals pages 9-10) | Genetically engineered mouse models; 2023 experimental study | Mus musculus; high-fat diet; intestinal lipid accumulation; hepatic steatosis; insulin resistance; ER stress |
| Prognosis | Gastrointestinal symptoms often improve rapidly with fat restriction, but fat intolerance persists and steatorrhea did not adapt after about five years. Early treatment was associated with absence of clinical/electrophysiologic neuro-ophthalmologic complications in **12/16** patients; delayed diagnosis can lead to permanent growth, neurologic, retinal, muscular, cardiac, hepatic, or skeletal morbidity (peretti2018lessonsfromchylomicron pages 3-4, peretti2010guidelinesforthe pages 3-4, peretti2010guidelinesforthe pages 9-10) | Longitudinal human cohorts and expert synthesis | Growth delay; peripheral neuropathy; ataxia; retinopathy; myopathy; cardiomyopathy; hepatic steatosis; reduced bone mineralization |


*Table: Compact evidence table summarizing the identity, phenotype frequencies, diagnostic signature, molecular mechanism, genetics, management, models, and prognosis of chylomicron retention disease. Evidence types and suggested ontology concepts are included for knowledge-base annotation.*

---

## 1. Disease information

### Definition and identifiers

CRD is a hereditary disorder of intestinal chylomicron secretion and lipid absorption. Its characteristic biochemical combination is low total cholesterol, LDL cholesterol, and HDL cholesterol, generally normal fasting triglycerides, and absent postprandial chylomicrons/apoB-48. It is distinct from defects that prevent apoB-lipoprotein assembly altogether because circulating LDL and apoB-100 remain detectable, albeit reduced (georges2011molecularanalysisand pages 1-2, peretti2018lessonsfromchylomicron pages 1-3).

**Key identifiers and terminology**

- **MONDO:** MONDO:0009528.
- **OMIM phenotype:** commonly catalogued as **chylomicron retention disease, MIM 246700**. Some older literature used MIM 607689; this inconsistency reflects historical nomenclature and should be checked against the current OMIM release before database ingestion.
- **Causal gene:** **SAR1B**, OMIM *607690; Ensembl ENSG00000152700; former symbol **SARA2**; approved name “secretion associated Ras-related GTPase 1B” (OpenTargets Search: chylomicron retention disease-SAR1B, georges2011molecularanalysisand pages 1-2).
- **Synonyms:** Anderson disease, Anderson’s disease, chylomicron retention disease, chylomicron-retention disease, intestinal hypobetalipoproteinemia, and historically “Anderson syndrome.”
- **Orphanet:** the disease is represented in Orphanet, but an ORPHA number was not independently verified in the retrieved evidence.
- **ICD/MeSH:** no CRD-specific ICD-10 or ICD-11 code was demonstrated in the retrieved literature. Coding generally falls under broader disorders of lipoprotein metabolism or intestinal malabsorption. A dedicated MeSH descriptor was likewise not established here; “Lipid Metabolism, Inborn Errors” and “Malabsorption Syndromes” are appropriate indexing concepts.

The evidence in this report is principally **aggregated disease-level evidence** from published cohorts, reviews, molecular studies, and disease databases. It is not an analysis of individual electronic health records.

---

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Primary cause

The canonical cause is **germline biallelic loss-of-function or function-disrupting variation in SAR1B**, inherited autosomal recessively. Open Targets identifies SAR1B as the sole strongly supported target associated with MONDO:0009528 and links the association to human publications including PMID 12692552, 18786134, 19274794, and 21235735 (OpenTargets Search: chylomicron retention disease-SAR1B).

Rare phenocopies or unresolved cases exist. A Japanese patient with the clinical and histologic phenotype had maternal uniparental disomy of chromosome 7 and a normal SAR1B coding sequence, suggesting that regulatory defects or another lipid-export gene may occasionally produce a CRD-like phenotype. This does not overturn SAR1B as the established cause of typical CRD (georges2011molecularanalysisand pages 1-2).

### Risk factors

- **Genetic:** two pathogenic SAR1B alleles; parental consanguinity increases the probability of homozygosity. Family history may be absent because heterozygotes generally have normal lipid profiles.
- **Environmental/lifestyle:** environmental exposure does not initiate the Mendelian disease. A high intake of long-chain triglycerides increases steatorrhea and enterocyte lipid loading; diarrhea commonly recurs when fat is reintroduced (peretti2018lessonsfromchylomicron pages 3-4, peretti2010guidelinesforthe pages 3-4).
- **Age and sex:** onset is usually during the first six months. No convincing human sex bias is established.
- **Infectious/toxic/occupational factors:** none established.

### Protective factors

No protective SAR1B allele has been validated. Clinically protective measures are early recognition, restriction of long-chain dietary fat, adequate essential fatty acids and calories, and high-dose fat-soluble vitamins—particularly vitamin E. Early therapy was associated with absence of clinical or electrophysiologic neuro-ophthalmologic disease in 12 of 16 patients in the principal two-center experience (peretti2010guidelinesforthe pages 9-10).

### Gene–environment interaction

Diet alters phenotype severity rather than disease occurrence. In Sar1b-mutant mice, an eight-week diet containing 60% fat exposed genotype- and sex-dependent changes in weight, adiposity, insulin resistance, hepatic steatosis, fatty-acid composition, cholesterol regulation, and intestinal ER stress. Female mice were relatively protected, but this sex effect remains a model-organism observation and should not be assumed in humans (levy2024unravelingchylomicronretention pages 10-12, auclair2023highfatdietreveals pages 11-13, auclair2023highfatdietreveals pages 9-10).

---

## 3. Phenotypes

The most useful frequency data derive from a literature synthesis and molecularly confirmed cohort of 16 patients, not a population registry. Therefore, estimates are susceptible to ascertainment and small-sample bias.

| Phenotype | Type, onset/course, reported frequency | Suggested HPO annotation |
|---|---|---|
| Chronic diarrhea | Symptom; usually 1–6 months; improves rapidly with fat restriction but recurs with fat | Chronic diarrhea |
| Steatorrhea/fat malabsorption | Symptom/laboratory; chronic and diet-responsive; **85%** | Steatorrhea; intestinal fat malabsorption |
| Failure to thrive/growth retardation | Clinical sign; infancy onset; **80%**; reported growth deficit −1 to −4 SD | Failure to thrive; growth delay |
| Abdominal distension | Sign; early; **65%** | Abdominal distention |
| Vomiting | Symptom; early and variable; **60%** | Vomiting |
| Hypocholesterolemia | Laboratory; persistent; low total cholesterol and LDL in **100%** | Hypocholesterolemia; decreased LDL cholesterol |
| Low HDL cholesterol | Laboratory; **100%** in summarized genotyped cases | Decreased HDL cholesterol concentration |
| Normal fasting triglycerides | Laboratory discriminator; **90%** | Normal circulating triglyceride concentration |
| Absent postprandial chylomicrons/apoB-48 | Functional laboratory hallmark; negative oral fat load in **100%** | Absent postprandial chylomicrons |
| Vitamin E deficiency | Laboratory; severe and persistent; **95%** | Vitamin E deficiency |
| Vitamins A, D, K deficiency | Laboratory; **70%, 45%, and 45%**, respectively | Vitamin A/D/K deficiency |
| Elevated creatine kinase | Laboratory/muscular sign; **60%**, often 1.5–4× normal | Elevated serum creatine kinase |
| Hepatic steatosis/hepatomegaly | Sign/imaging; approximately **15–20%** in reported series; usually mild | Hepatic steatosis; hepatomegaly |
| Neuropathy, areflexia, ataxia, myopathy | Later complications, particularly if untreated; variable and less severe than in abetalipoproteinemia | Peripheral neuropathy; areflexia; ataxia; myopathy |
| Retinopathy | Late, potentially permanent complication; uncommon at presentation | Pigmentary retinopathy/retinal degeneration |
| Reduced mineralization/delayed bone age | Chronic complication | Osteopenia; delayed skeletal maturation |

These frequencies are supported by the 16-patient synthesis: diarrhea 100%, steatorrhea 85%, growth failure 80%, distension 65%, vomiting and high CK 60%, vitamin E deficiency 95%, and low LDL/HDL 100% (peretti2010guidelinesforthe pages 3-4). Quality-of-life instruments such as EQ-5D, SF-36, or PROMIS have not been validated in CRD. Likely burdens include dietary restriction, recurrent gastrointestinal symptoms, frequent biochemical surveillance, impaired childhood growth, and preventable neurologic disability.

---

## 4. Genetic and molecular information

### Gene and protein

**SAR1B** lies at **5q31.1**, contains eight exons, and has predicted alternative exon-2 splicing. It encodes a 198-amino-acid Ras/ARF-family small GTPase. Human SAR1A and SAR1B differ at only 20 residues, but SAR1B binds SEC23 more strongly, has distinct GTPase-exchange kinetics, and is particularly important for intestinal chylomicron export (georges2011molecularanalysisand pages 1-2, tang2023cargoselectionin pages 2-3).

### Representative pathogenic variants

Reported disease alleles include:

- Frameshift: **p.Leu28Argfs*7**, **p.Asp48Thrfs*17**, and **c.83_84delTG (p.Leu28Argfs*7)**.
- Nonsense: **p.Glu122***.
- Deletion: whole exon 2 deletion, functionally described as **p.Met1_His43del**.
- Missense: **p.Asp137Asn**, **p.Ser179Arg**, and **p.Gly185Val** (charcosset2008andersonorchylomicron pages 1-2, georges2011molecularanalysisand pages 1-2, charcosset2008andersonorchylomicron pages 8-9).

Frameshift/nonsense/deletion alleles generally produce absent or severely truncated proteins and are mechanistically loss-of-function. Missense substitutions can disrupt GTP binding/hydrolysis, SEC12 activation, SEC23 interaction, membrane association, or coat dynamics. The variants are germline, not somatic. The retrieved literature did not provide current gnomAD frequencies or a complete ClinVar classification table; each variant should therefore be rechecked in current ClinVar/gnomAD before assigning an ACMG class.

### Expressivity, modifiers, and other genomic mechanisms

Clinical severity varies even among families carrying variants predicted to cause severe dysfunction, so a simple genotype–phenotype correlation is not established. Intestinal SAR1A rises approximately 1.4–2.7-fold in affected biopsies but does not compensate for a roughly two-thirds reduction in SAR1B. A co-occurring **PCSK9 p.Leu21dup** allele had no demonstrable additional effect. APOB, MTTP, ABCG5/ABCG8, transcriptional regulators, and dietary exposure are candidate modifiers, but none is validated as a CRD modifier (georges2011molecularanalysisand pages 8-11, georges2011molecularanalysisand pages 1-2, charcosset2008andersonorchylomicron pages 8-9).

No reproducible disease-specific DNA methylation, histone, chromatin, repeat-expansion, mitochondrial-DNA, or large chromosomal-abnormality mechanism is established. The chromosome-7 uniparental-disomy case is exceptional rather than the canonical mechanism.

---

## 5. Environmental information

CRD is not caused by toxins, radiation, pollution, smoking, alcohol, occupation, or infection. Dietary long-chain triglyceride is the most important phenotype-modifying exposure. Medium-chain triglycerides bypass chylomicron packaging to a greater extent and can provide calories, although their routine amount must be individualized. Excessively strict fat avoidance can worsen essential-fatty-acid deficiency; treatment therefore balances symptom control against growth and omega-3/omega-6 requirements (peretti2010guidelinesforthe pages 10-11, peretti2010guidelinesforthe pages 1-3).

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic SAR1B pathogenic variants lead to** reduced or dysfunctional SAR1B GTPase in absorptive small-intestinal enterocytes.
2. **Defective SEC12-mediated nucleotide exchange or abnormal GTP hydrolysis/membrane interaction leads to** impaired SAR1B cycling between GDP-bound inactive and GTP-bound active states.
3. **Abnormal active SAR1B leads to** defective recruitment or dynamics of the SEC23–SEC24 inner COPII coat and SEC13–SEC31 outer coat at ER exit sites.
4. **Defective COPII assembly/scission and/or pre-chylomicron-vesicle fusion with Golgi leads to** failed ER-to-Golgi export of unusually large apoB-48-containing pre-chylomicrons.
5. **Failed export leads to** intracellular retention of triglyceride-rich droplets and membrane-bound chylomicron-like particles in villus enterocytes.
6. **Enterocyte retention leads to** absent postprandial chylomicrons, reduced delivery of dietary triglyceride, cholesterol, essential fatty acids, and fat-soluble vitamins to blood and peripheral tissues.
7. **Reduced lipid export leads to** steatorrhea, chronic diarrhea, abdominal distension, hypocholesterolemia, low HDL, malnutrition, and growth failure.
8. **Chronic vitamin E/essential-fatty-acid deficiency leads to** neurologic, retinal, muscular, hematologic, and skeletal complications.
9. **Branch—intracellular lipid accumulation probably leads to** lipid peroxidation, ER stress, and inflammatory signaling; this branch is demonstrated in cell/animal models but remains incompletely validated as a driver of human complications.
10. **Branch—SAR1B expression in liver and muscle may lead to** hepatic, skeletal-muscle, and cardiac manifestations when function is severely impaired; extra-intestinal causality is supported but less firmly characterized than the enterocyte defect (levy2024unravelingchylomicronretention pages 10-12, georges2011molecularanalysisand pages 11-12, tang2023cargoselectionin pages 2-3, levy2024unravelingchylomicronretention pages 7-9).

### Cellular and biochemical detail

SEC12 activates SAR1B at the ER membrane. SAR1B-GTP inserts an amphipathic helix, deforms the membrane, recruits SEC23/SEC24 and subsequently SEC13/SEC31, and helps generate and uncoat COPII carriers. SEC23/SEC31 stimulate GTP hydrolysis, allowing coat disassembly. Disruption at either nucleotide exchange or hydrolysis can therefore block secretion (georges2011molecularanalysisand pages 11-12, levy2024unravelingchylomicronretention pages 7-9).

In healthy duodenum, Sar1 protein is concentrated apically in enterocytes of the upper two-thirds of villi. CRD biopsies show reduced, heterogeneous Sar1 staining around large lipid droplets. SAR1B normally exceeds SAR1A expression approximately 2.5–3-fold in intestine (georges2011molecularanalysisand pages 8-11).

**Suggested GO terms:** ER-to-Golgi vesicle-mediated transport (GO:0006888); COPII-coated vesicle budding; GTPase activity; lipid transport; chylomicron assembly; cholesterol efflux; response to ER stress; response to oxidative stress. **Suggested CL term:** absorptive intestinal epithelial cell/enterocyte. Relevant pathways include Reactome COPII-mediated vesicle transport and intestinal lipoprotein assembly; canonical Wnt, MAPK, mTOR, and PI3K–AKT dysregulation are not established primary mechanisms.

### Molecular profiling and advanced technologies

Patient-biopsy RT-qPCR demonstrated reduced SAR1B and compensatory but inadequate SAR1A expression. Caco-2/15 CRISPR disruption reduced chylomicron output and HDL biogenesis/cholesterol efflux; complete suppression of chylomicron secretion required combined SAR1A/SAR1B disruption, demonstrating paralog redundancy. Increased malondialdehyde supported lipid peroxidation (sane2017understandingchylomicronretention pages 9-10, levy2024unravelingchylomicronretention pages 10-12).

Recent work has integrated lipid profiles, fatty-acid composition, expression of **PCSK9/LDLR, NPC1L1, SCARB1, ABCG8, MTTP, HMGCR, SREBP2, ABCA1**, and **LXRα**, and ER-stress markers **PERK, IRE1, GRP78**, and **ATF6** in engineered mice. No disease-specific human single-cell or spatial-transcriptomic atlas, validated proteomic signature, or clinical multi-omics classifier was identified (levy2024unravelingchylomicronretention pages 10-12, auclair2023highfatdietreveals pages 9-10).

---

## 7. Anatomical structures affected

- **Primary organ/system:** proximal small intestine and digestive system.
- **Tissue/cell:** villus epithelium, especially mature absorptive enterocytes. Suggested terms: UBERON “duodenum,” “jejunum,” “small intestine,” “intestinal villus”; CL “enterocyte.”
- **Subcellular sites:** ER membrane/ER exit sites, COPII-coated transport carriers, pre-chylomicron transport vesicles, Golgi apparatus, and cytoplasmic lipid droplets. Suggested GO-CC terms: endoplasmic reticulum membrane, ER exit site, COPII-coated ER-to-Golgi transport vesicle, Golgi apparatus, lipid droplet.
- **Secondary organs:** liver (steatosis/cytolysis), skeletal muscle (high CK/myopathy), peripheral nervous system, retina, skeleton, and occasionally heart.
- **Localization/lateralization:** diffuse intestinal involvement; no meaningful unilateral or bilateral pattern (peretti2018lessonsfromchylomicron pages 1-3, georges2011molecularanalysisand pages 8-11).

---

## 8. Temporal development

Symptoms usually begin chronically or insidiously between **one and six months**, sometimes neonatally. Only about one-third of reported children in an older synthesis were diagnosed during the first year, illustrating diagnostic delay (peretti2010guidelinesforthe pages 3-4, peretti2018lessonsfromchylomicron pages 1-3).

Early disease consists of diarrhea, steatorrhea, vomiting/distension, and faltering growth. Intermediate disease includes persistent biochemical deficiencies, delayed growth or puberty, hepatic cytolysis/steatosis, and elevated CK. Advanced untreated disease may include neuropathy, areflexia, ataxia, myopathy, retinal disease, poor bone mineralization, and cardiomyopathy. CRD is lifelong: gastrointestinal symptoms improve within days or weeks of fat restriction, but there is no reliable remission or intestinal adaptation, and steatorrhea persisted after approximately five years of observation (peretti2018lessonsfromchylomicron pages 3-4, peretti2010guidelinesforthe pages 3-4, peretti2010guidelinesforthe pages 1-3).

Infancy and early childhood are critical intervention windows because malnutrition affects growth and prolonged vitamin E deficiency may cause irreversible neuro-retinal injury.

---

## 9. Inheritance and population

CRD is autosomal recessive. For two confirmed carrier parents, each pregnancy has the conventional 25% affected, 50% carrier, and 25% unaffected/non-carrier probabilities. Heterozygotes are generally clinically and biochemically normal. Penetrance of clearly pathogenic biallelic variants appears high, but formal age-dependent penetrance estimates do not exist; expressivity is variable (charcosset2008andersonorchylomicron pages 1-2, peretti2018lessonsfromchylomicron pages 1-3).

Estimated prevalence is **<1 per 1,000,000**. Approximately 60 patients, about 40 genotyped and carrying roughly 20 different mutations, had been reported by 2018; underdiagnosis is likely. Published families include French-Canadian, Turkish, Algerian, Portuguese, European, Japanese, and other ancestries. Founder effects have been suggested in clustered families but no global carrier frequency or robust incidence estimate is available. Both sexes are affected. Consanguinity is a recognized enrichment mechanism; anticipation and germline mosaicism are not characteristic (charcosset2008andersonorchylomicron pages 1-2, peretti2018lessonsfromchylomicron pages 1-3, georges2011molecularanalysisand pages 1-2).

---

## 10. Diagnostics

### Practical diagnostic pathway

1. In an infant or child with chronic diarrhea, steatorrhea, or unexplained growth failure, measure fasting total cholesterol, LDL-C, HDL-C, triglycerides, apoB, vitamins A/D/E/K, INR, liver enzymes, CK, blood count, iron, and essential-fatty-acid profile.
2. Suspect CRD when total/LDL cholesterol is approximately 50% of normal, HDL is low, triglycerides remain normal, and vitamin E is markedly low.
3. Demonstrate absent or markedly reduced postprandial chylomicrons/apoB-48 after a supervised fat load where clinically safe. A negative fat load was reported in 100% of summarized genotyped cases.
4. Upper endoscopy after dietary fat exposure may show a white or stippled duodenal/jejunal mucosa.
5. Biopsy shows preserved villus architecture but lipid-distended enterocytes, large cytoplasmic droplets, and membrane-bound lipoprotein-sized particles.
6. Confirm with sequencing and deletion/duplication analysis of **SAR1B**; test parents for phase and enable cascade screening (georges2011molecularanalysisand pages 1-2, peretti2018lessonsfromchylomicron pages 1-3, ferreira2018chylomicronretentiondisease pages 6-7).

A representative abstract states: “The diagnosis is based on a history of chronic diarrhea with fat malabsorption and abnormal lipid profile. Upper endoscopy and histology reveal fat-laden enterocytes whereas vitamin E deficiency is invariably present” (Peretti et al., published 22 September 2010; DOI [10.1186/1750-1172-5-24](https://doi.org/10.1186/1750-1172-5-24)) (peretti2010guidelinesforthe pages 1-3).

### Genetic-test selection

A hypocholesterolemia/fat-malabsorption panel should include at least **SAR1B, MTTP, APOB**, and often **ANGPTL3, PCSK9**, and other lipid genes. Single-gene SAR1B testing is efficient with a classic phenotype. WES/WGS is appropriate when panel testing is negative, the phenotype is syndromic, or regulatory/structural variation is suspected. Copy-number analysis is necessary because exon deletions occur. CMA, karyotyping, FISH, mitochondrial-DNA testing, and repeat-expansion assays are not first-line unless other clinical findings indicate them. RNA sequencing may clarify splice or regulatory variants but is not a routine validated diagnostic assay.

### Differential diagnosis

- **Abetalipoproteinemia (MTTP):** nearly absent apoB-containing lipoproteins, extremely low LDL and triglycerides, prominent acanthocytosis; CRD retains apoB-100/LDL and usually has normal triglycerides.
- **Biallelic APOB familial hypobetalipoproteinemia:** severe apoB deficiency affecting intestinal and hepatic lipoproteins; genotype and lipid pattern distinguish it.
- **Heterozygous APOB/PCSK9 hypobetalipoproteinemia:** usually little or no infantile malabsorption.
- **ANGPTL3 deficiency:** combined hypolipidemia without characteristic fat-loaded enterocytes.
- **Celiac disease, cystic fibrosis/pancreatic insufficiency, congenital diarrheal disorders, cholestasis, food-protein disease:** can cause malabsorption but not the characteristic normal-triglyceride hypocholesterolemia plus absent postprandial apoB-48.

Population newborn screening is not established. Targeted biochemical/genetic testing, sibling cascade testing, and parental carrier testing are appropriate (ferreira2018chylomicronretentiondisease pages 6-7, peretti2018lessonsfromchylomicron pages 1-3).

---

## 11. Outcome and prognosis

No reliable five- or ten-year survival, mortality rate, or life-expectancy estimate exists. Available evidence suggests that treated patients can reach adulthood and that morbidity, rather than early mortality, is the principal concern. Early therapy commonly resolves diarrhea and improves weight, while hypocholesterolemia and vitamin E deficiency may persist (peretti2010guidelinesforthe pages 9-10, ferreira2018chylomicronretentiondisease pages 5-6).

Delayed diagnosis can permanently compromise growth: seven patients in the major clinical experience failed to reach the 20th percentile of predicted growth potential. Potential complications include neuropathy, ataxia, myopathy, retinal degeneration, osteopenia, delayed puberty, coagulopathy, anemia, hepatic steatosis, and cardiomyopathy. Moderate macrovesicular steatosis is reported, but the guideline review found no established progression to steatohepatitis or cirrhosis. Prognostic factors are age at treatment, adequacy/adherence of vitamin E and caloric replacement, dietary control of malabsorption, and baseline neurologic or retinal injury (peretti2018lessonsfromchylomicron pages 3-4, peretti2010guidelinesforthe pages 3-4, peretti2010guidelinesforthe pages 9-10).

---

## 12. Treatment and current applications

### Standard management

There is no approved disease-modifying drug, gene therapy, RNA therapy, cell therapy, or surgery. Treatment is lifelong nutritional therapy:

- Restrict long-chain fat sufficiently to control diarrhea and steatorrhea without causing caloric deprivation.
- Supply essential fatty acids: approximately **3–5% of energy as omega-6** and **0.5–1% as omega-3**; soybean oil and fish were specifically suggested.
- Consider medium-chain triglycerides as a chylomicron-independent energy source.
- **Vitamin E:** approximately **50 IU/kg/day orally**, adjusted to biochemical and safety monitoring.
- **Vitamin A:** approximately **15,000 IU/day**, adjusted to plasma level and toxicity risk.
- **Vitamin D:** approximately **800–1,200 IU/day** or age-adjusted intermittent regimens. Some reproduced guideline tables contain an apparent “IU/kg/day” transcription; the original regimen should be verified before prescribing.
- **Vitamin K:** approximately **15 mg/week**, adjusted to INR and vitamin status.
- Correct iron, calcium, and other deficiencies as indicated (peretti2010guidelinesforthe pages 10-11, peretti2010guidelinesforthe pages 9-10).

These are historical expert-guideline doses, not substitutes for specialist prescribing. Hypervitaminosis A/D and vitamin E–related bleeding are relevant safety considerations. Suggested NCIT intervention concepts include dietary therapy, low-fat diet, nutritional supplementation, vitamin E, vitamin A, vitamin D, vitamin K, medium-chain triglyceride, and genetic counseling.

### Monitoring

Annual childhood assessment should include height/weight, gastrointestinal and neurologic status, diet, lipid profile, liver enzymes, CK, blood count, fat-soluble vitamins, INR, and essential fatty acids. After age ten, liver ultrasound, neurologic/muscular and ophthalmologic examination, electrophysiology where indicated, and bone-density assessment approximately every three years were proposed. Adult echocardiography every three years was also suggested (peretti2010guidelinesforthe pages 10-11, peretti2010guidelinesforthe pages 9-10).

### Experimental and translational applications

No CRD-specific interventional trial was identified. A ClinicalTrials.gov search returned an observational carotenoid study in hypocholesterolemia (**NCT05208879**, completed; n=10), but its direct CRD enrollment and disease-specific utility were not established. Other retrieved “Anderson” trials concerned Anderson–Fabry disease and were irrelevant.

SAR1B biology is being considered as a lipid-lowering target because reducing enterocyte lipoprotein export could lower circulating cholesterol. Experts caution that broad SAR1B inhibition could reproduce malabsorption, vitamin deficiency, liver or muscle effects, and secretory-pathway toxicity. Intestine-restricted, partial, or cargo-selective modulation would therefore be required (peretti2018lessonsfromchylomicron pages 3-4, tang2023cargoselectionin pages 2-3).

---

## 13. Prevention

Primary prevention through lifestyle or vaccination is not applicable to the occurrence of a recessive genetic disorder. Reproductive prevention options include carrier testing of relatives, genetic counseling, partner testing, prenatal diagnosis, and preimplantation genetic testing when familial variants are known. Secondary prevention consists of cascade testing and rapid evaluation of symptomatic siblings; universal newborn screening is not currently established. Tertiary prevention is central: early dietary treatment and vitamin replacement, growth monitoring, and surveillance of liver, nervous system, retina, muscle, heart, coagulation, and bone reduce complications. No infectious prophylaxis, immunization specific to CRD, or environmental public-health intervention is indicated.

---

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart or zoonotic form was identified. SAR1B is evolutionarily conserved across vertebrates, and orthologs exist in mouse and zebrafish. CRD is neither infectious nor transmissible between species. Breed-specific disease and VBO annotations were not found. Comparative importance lies in conserved COPII trafficking rather than animal-health prevalence (charcosset2008andersonorchylomicron pages 1-2, auclair2023highfatdietreveals pages 1-2).

---

## 15. Model organisms and experimental systems

### Cellular models

CRISPR-disrupted human Caco-2/15 intestinal cells show reduced chylomicron secretion, impaired HDL biogenesis and cholesterol efflux, and oxidative stress. Combined SAR1A/SAR1B loss causes a more complete secretory block than SAR1B loss alone, revealing redundancy. Limitations include transformed-cell metabolism, absence of systemic dietary physiology, and incomplete modeling of development (sane2017understandingchylomicronretention pages 9-10, tang2023cargoselectionin pages 2-3).

### Zebrafish

Sar1b-deficient zebrafish reproduce intestinal lipid-absorption and trafficking defects and are useful for developmental imaging and mechanistic screening. Their lipoprotein physiology and early development differ from humans, limiting direct therapeutic extrapolation.

### Mouse

CRISPR mice bearing a targeted deletion or a patient-analogous Sar1b mutation reproduce intestinal lipid accumulation, steatorrhea, malabsorption, failed chylomicron secretion, hypocholesterolemia, and low HDL. Homozygous deletion/mutation is usually embryonic or neonatal lethal, unlike most human patients, so heterozygous mice have been used for metabolic experiments even though human heterozygotes are generally asymptomatic. This genotype mismatch is an important limitation (auclair2023highfatdietreveals pages 1-2, auclair2023highfatdietreveals pages 11-13, lu2020consequencesofmutations pages 2-4).

The 2023 high-fat-diet study demonstrated that diet, sex, and allele type alter the model phenotype. It found changes in hepatic and intestinal steatosis, insulin sensitivity, saturated/polyunsaturated fatty-acid balance, omega-6/omega-3 ratio, and ER-stress responses. These data strengthen the concept that SAR1B regulates broader cholesterol and metabolic homeostasis, but small subgroup and histology sample sizes constrain inference (auclair2023highfatdietreveals pages 11-13, auclair2023highfatdietreveals pages 9-10, auclair2023highfatdietreveals pages 4-5).

---

## Evidence hierarchy, recent developments, and limitations

The most authoritative clinical management evidence remains the 2010 two-center guideline because no newer controlled treatment study exists. Its abstract directly states that treatment includes “fat-soluble vitamin supplements and large amounts of vitamin E” and emphasizes maintaining both calories and essential fatty acids (published 22 September 2010; DOI [10.1186/1750-1172-5-24](https://doi.org/10.1186/1750-1172-5-24)) (peretti2010guidelinesforthe pages 1-3).

The major recent synthesis is Levy et al., **July 2024**, *Biomedicines* 12:1548, DOI [10.3390/biomedicines12071548](https://doi.org/10.3390/biomedicines12071548). Its abstract concludes that SAR1B loss-of-function not only predisposes to CRD but may “exacerbate oxidative stress, inflammation, and ER stress”; these secondary mechanisms are primarily based on cellular and animal evidence rather than prospective human data (levy2024unravelingchylomicronretention pages 1-2).

The principal recent primary mechanistic study is Auclair et al., **September 2023**, *Journal of Lipid Research* 64:100423, DOI [10.1016/j.jlr.2023.100423](https://doi.org/10.1016/j.jlr.2023.100423), which established diet-, sex-, and allele-dependent metabolic effects in engineered mice (auclair2023highfatdietreveals pages 1-2, auclair2023highfatdietreveals pages 9-10).

Overall certainty is high for autosomal-recessive SAR1B causation, impaired COPII-dependent pre-chylomicron trafficking, the biochemical/endoscopic signature, and benefit of early nutritional therapy. Certainty is moderate or low for exact prevalence, phenotype penetrance, genotype–phenotype correlation, human sex effects, secondary inflammatory/ER-stress mechanisms, long-term survival, optimal vitamin doses, and advanced therapeutics because CRD remains exceptionally rare and lacks registries or controlled trials.

References

1. (OpenTargets Search: chylomicron retention disease-SAR1B): Open Targets Query (chylomicron retention disease-SAR1B, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (peretti2018lessonsfromchylomicron pages 1-3): Noel Peretti. Lessons from chylomicron retention disease: a potential new approach for the treatment of hypercholesterolemia? Expert Opinion on Orphan Drugs, 6:163-165, Feb 2018. URL: https://doi.org/10.1080/21678707.2018.1438259, doi:10.1080/21678707.2018.1438259. This article has 4 citations.

3. (peretti2010guidelinesforthe pages 3-4): Noel Peretti, Agnès Sassolas, Claude C Roy, Colette Deslandres, Mathilde Charcosset, Justine Castagnetti, Laurence Pugnet-Chardon, Philippe Moulin, Sylvie Labarge, Lise Bouthillier, Alain Lachaux, and Emile Levy. Guidelines for the diagnosis and management of chylomicron retention disease based on a review of the literature and the experience of two centers. Orphanet Journal of Rare Diseases, 5:24-24, Sep 2010. URL: https://doi.org/10.1186/1750-1172-5-24, doi:10.1186/1750-1172-5-24. This article has 155 citations and is from a peer-reviewed journal.

4. (georges2011molecularanalysisand pages 1-2): Amandine Georges, Jessica Bonneau, Dominique Bonnefont-Rousselot, Jacqueline Champigneulle, Jean P Rabès, Marianne Abifadel, Thomas Aparicio, Jean C Guenedet, Eric Bruckert, Catherine Boileau, Alain Morali, Mathilde Varret, Lawrence P Aggerbeck, and Marie E Samson-Bouma. Molecular analysis and intestinal expression of sar1 genes and proteins in anderson's disease (chylomicron retention disease). Orphanet Journal of Rare Diseases, 6:1-1, Jan 2011. URL: https://doi.org/10.1186/1750-1172-6-1, doi:10.1186/1750-1172-6-1. This article has 89 citations and is from a peer-reviewed journal.

5. (ferreira2018chylomicronretentiondisease pages 6-7): Helena Ferreira, Raquel Nuñez Ramos, Cinthia Flores Quan, Susana Redecillas Ferreiro, Vanessa Cabello Ruiz, Javi Juampérez Goñi, Jesus Quintero Bernabeu, Oscar Segarra Cantón, and Marina Álvarez Beltran. Chylomicron retention disease: a description of a new mutation in a very rare disease. Pediatric Gastroenterology, Hepatology & Nutrition, 21:134-140, Apr 2018. URL: https://doi.org/10.5223/pghn.2018.21.2.134, doi:10.5223/pghn.2018.21.2.134. This article has 14 citations and is from a peer-reviewed journal.

6. (tang2023cargoselectionin pages 2-3): Vi T. Tang and David Ginsburg. Cargo selection in endoplasmic reticulum–to–golgi transport and relevant diseases. The Journal of Clinical Investigation, Jan 2023. URL: https://doi.org/10.1172/jci163838, doi:10.1172/jci163838. This article has 73 citations.

7. (levy2024unravelingchylomicronretention pages 7-9): Emile Levy, Catherine Fallet-Bianco, Nickolas Auclair, Natalie Patey, Valérie Marcil, Alain Théophile Sané, and Schohraya Spahis. Unraveling chylomicron retention disease enhances insight into sar1b gtpase functions and mechanisms of actions, while shedding light of intracellular chylomicron trafficking. Jul 2024. URL: https://doi.org/10.3390/biomedicines12071548, doi:10.3390/biomedicines12071548. This article has 1 citations.

8. (sane2017understandingchylomicronretention pages 9-10): Alain Théophile Sané, Ernest Seidman, Noel Peretti, Marie Laure Kleme, Edgard Delvin, Colette Deslandres, Carole Garofalo, Schohraya Spahis, and Emile Levy. Understanding chylomicron retention disease through sar1b gtpase gene disruption: insight from cell culture. Arteriosclerosis, Thrombosis, and Vascular Biology, 37:2243–2251, Dec 2017. URL: https://doi.org/10.1161/atvbaha.117.310121, doi:10.1161/atvbaha.117.310121. This article has 64 citations and is from a domain leading peer-reviewed journal.

9. (levy2024unravelingchylomicronretention pages 10-12): Emile Levy, Catherine Fallet-Bianco, Nickolas Auclair, Natalie Patey, Valérie Marcil, Alain Théophile Sané, and Schohraya Spahis. Unraveling chylomicron retention disease enhances insight into sar1b gtpase functions and mechanisms of actions, while shedding light of intracellular chylomicron trafficking. Jul 2024. URL: https://doi.org/10.3390/biomedicines12071548, doi:10.3390/biomedicines12071548. This article has 1 citations.

10. (levy2024unravelingchylomicronretention pages 1-2): Emile Levy, Catherine Fallet-Bianco, Nickolas Auclair, Natalie Patey, Valérie Marcil, Alain Théophile Sané, and Schohraya Spahis. Unraveling chylomicron retention disease enhances insight into sar1b gtpase functions and mechanisms of actions, while shedding light of intracellular chylomicron trafficking. Jul 2024. URL: https://doi.org/10.3390/biomedicines12071548, doi:10.3390/biomedicines12071548. This article has 1 citations.

11. (charcosset2008andersonorchylomicron pages 1-2): Mathilde Charcosset, Agnès Sassolas, Noël Peretti, Claude C. Roy, Colette Deslandres, Daniel Sinnett, Emile Levy, and Alain Lachaux. Anderson or chylomicron retention disease: molecular impact of five mutations in the sar1b gene on the structure and the functionality of sar1b protein. Molecular genetics and metabolism, 93 1:74-84, Jan 2008. URL: https://doi.org/10.1016/j.ymgme.2007.08.120, doi:10.1016/j.ymgme.2007.08.120. This article has 95 citations and is from a peer-reviewed journal.

12. (charcosset2008andersonorchylomicron pages 8-9): Mathilde Charcosset, Agnès Sassolas, Noël Peretti, Claude C. Roy, Colette Deslandres, Daniel Sinnett, Emile Levy, and Alain Lachaux. Anderson or chylomicron retention disease: molecular impact of five mutations in the sar1b gene on the structure and the functionality of sar1b protein. Molecular genetics and metabolism, 93 1:74-84, Jan 2008. URL: https://doi.org/10.1016/j.ymgme.2007.08.120, doi:10.1016/j.ymgme.2007.08.120. This article has 95 citations and is from a peer-reviewed journal.

13. (georges2011molecularanalysisand pages 8-11): Amandine Georges, Jessica Bonneau, Dominique Bonnefont-Rousselot, Jacqueline Champigneulle, Jean P Rabès, Marianne Abifadel, Thomas Aparicio, Jean C Guenedet, Eric Bruckert, Catherine Boileau, Alain Morali, Mathilde Varret, Lawrence P Aggerbeck, and Marie E Samson-Bouma. Molecular analysis and intestinal expression of sar1 genes and proteins in anderson's disease (chylomicron retention disease). Orphanet Journal of Rare Diseases, 6:1-1, Jan 2011. URL: https://doi.org/10.1186/1750-1172-6-1, doi:10.1186/1750-1172-6-1. This article has 89 citations and is from a peer-reviewed journal.

14. (peretti2010guidelinesforthe pages 10-11): Noel Peretti, Agnès Sassolas, Claude C Roy, Colette Deslandres, Mathilde Charcosset, Justine Castagnetti, Laurence Pugnet-Chardon, Philippe Moulin, Sylvie Labarge, Lise Bouthillier, Alain Lachaux, and Emile Levy. Guidelines for the diagnosis and management of chylomicron retention disease based on a review of the literature and the experience of two centers. Orphanet Journal of Rare Diseases, 5:24-24, Sep 2010. URL: https://doi.org/10.1186/1750-1172-5-24, doi:10.1186/1750-1172-5-24. This article has 155 citations and is from a peer-reviewed journal.

15. (peretti2010guidelinesforthe pages 9-10): Noel Peretti, Agnès Sassolas, Claude C Roy, Colette Deslandres, Mathilde Charcosset, Justine Castagnetti, Laurence Pugnet-Chardon, Philippe Moulin, Sylvie Labarge, Lise Bouthillier, Alain Lachaux, and Emile Levy. Guidelines for the diagnosis and management of chylomicron retention disease based on a review of the literature and the experience of two centers. Orphanet Journal of Rare Diseases, 5:24-24, Sep 2010. URL: https://doi.org/10.1186/1750-1172-5-24, doi:10.1186/1750-1172-5-24. This article has 155 citations and is from a peer-reviewed journal.

16. (auclair2023highfatdietreveals pages 1-2): Nickolas Auclair, Alain T. Sané, Léna Ahmarani, Nour-El-Houda Ould-Chikh, Nathalie Patey, Jean-François Beaulieu, Edgard Delvin, Schohraya Spahis, and Emile Levy. High-fat diet reveals the impact of sar1b defects on lipid and lipoprotein profile and cholesterol metabolism. Sep 2023. URL: https://doi.org/10.1016/j.jlr.2023.100423, doi:10.1016/j.jlr.2023.100423. This article has 10 citations and is from a peer-reviewed journal.

17. (auclair2023highfatdietreveals pages 11-13): Nickolas Auclair, Alain T. Sané, Léna Ahmarani, Nour-El-Houda Ould-Chikh, Nathalie Patey, Jean-François Beaulieu, Edgard Delvin, Schohraya Spahis, and Emile Levy. High-fat diet reveals the impact of sar1b defects on lipid and lipoprotein profile and cholesterol metabolism. Sep 2023. URL: https://doi.org/10.1016/j.jlr.2023.100423, doi:10.1016/j.jlr.2023.100423. This article has 10 citations and is from a peer-reviewed journal.

18. (auclair2023highfatdietreveals pages 9-10): Nickolas Auclair, Alain T. Sané, Léna Ahmarani, Nour-El-Houda Ould-Chikh, Nathalie Patey, Jean-François Beaulieu, Edgard Delvin, Schohraya Spahis, and Emile Levy. High-fat diet reveals the impact of sar1b defects on lipid and lipoprotein profile and cholesterol metabolism. Sep 2023. URL: https://doi.org/10.1016/j.jlr.2023.100423, doi:10.1016/j.jlr.2023.100423. This article has 10 citations and is from a peer-reviewed journal.

19. (peretti2018lessonsfromchylomicron pages 3-4): Noel Peretti. Lessons from chylomicron retention disease: a potential new approach for the treatment of hypercholesterolemia? Expert Opinion on Orphan Drugs, 6:163-165, Feb 2018. URL: https://doi.org/10.1080/21678707.2018.1438259, doi:10.1080/21678707.2018.1438259. This article has 4 citations.

20. (peretti2010guidelinesforthe pages 1-3): Noel Peretti, Agnès Sassolas, Claude C Roy, Colette Deslandres, Mathilde Charcosset, Justine Castagnetti, Laurence Pugnet-Chardon, Philippe Moulin, Sylvie Labarge, Lise Bouthillier, Alain Lachaux, and Emile Levy. Guidelines for the diagnosis and management of chylomicron retention disease based on a review of the literature and the experience of two centers. Orphanet Journal of Rare Diseases, 5:24-24, Sep 2010. URL: https://doi.org/10.1186/1750-1172-5-24, doi:10.1186/1750-1172-5-24. This article has 155 citations and is from a peer-reviewed journal.

21. (georges2011molecularanalysisand pages 11-12): Amandine Georges, Jessica Bonneau, Dominique Bonnefont-Rousselot, Jacqueline Champigneulle, Jean P Rabès, Marianne Abifadel, Thomas Aparicio, Jean C Guenedet, Eric Bruckert, Catherine Boileau, Alain Morali, Mathilde Varret, Lawrence P Aggerbeck, and Marie E Samson-Bouma. Molecular analysis and intestinal expression of sar1 genes and proteins in anderson's disease (chylomicron retention disease). Orphanet Journal of Rare Diseases, 6:1-1, Jan 2011. URL: https://doi.org/10.1186/1750-1172-6-1, doi:10.1186/1750-1172-6-1. This article has 89 citations and is from a peer-reviewed journal.

22. (ferreira2018chylomicronretentiondisease pages 5-6): Helena Ferreira, Raquel Nuñez Ramos, Cinthia Flores Quan, Susana Redecillas Ferreiro, Vanessa Cabello Ruiz, Javi Juampérez Goñi, Jesus Quintero Bernabeu, Oscar Segarra Cantón, and Marina Álvarez Beltran. Chylomicron retention disease: a description of a new mutation in a very rare disease. Pediatric Gastroenterology, Hepatology & Nutrition, 21:134-140, Apr 2018. URL: https://doi.org/10.5223/pghn.2018.21.2.134, doi:10.5223/pghn.2018.21.2.134. This article has 14 citations and is from a peer-reviewed journal.

23. (lu2020consequencesofmutations pages 2-4): Chung-Ling Lu and Jinoh Kim. Consequences of mutations in the genes of the er export machinery copii in vertebrates. Mar 2020. URL: https://doi.org/10.1007/s12192-019-01062-3, doi:10.1007/s12192-019-01062-3. This article has 25 citations and is from a peer-reviewed journal.

24. (auclair2023highfatdietreveals pages 4-5): Nickolas Auclair, Alain T. Sané, Léna Ahmarani, Nour-El-Houda Ould-Chikh, Nathalie Patey, Jean-François Beaulieu, Edgard Delvin, Schohraya Spahis, and Emile Levy. High-fat diet reveals the impact of sar1b defects on lipid and lipoprotein profile and cholesterol metabolism. Sep 2023. URL: https://doi.org/10.1016/j.jlr.2023.100423, doi:10.1016/j.jlr.2023.100423. This article has 10 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Chylomicron_Retention_Disease-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0009528` (4 mentions) - the report calls it "if available"; MONDO calls it **chylomicron retention disease**
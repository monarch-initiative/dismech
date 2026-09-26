---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-03T16:19:31.342159'
end_time: '2026-09-03T16:32:01.347223'
duration_seconds: 750.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: cardiac, facial, and digital anomalies with developmental delay (CAFDADD),
    caused by germline de novo TRAF7 missense variants (NOT somatic TRAF7 mutations
    in meningioma)
  mondo_id: MONDO:0032572
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 60
  verified: 58
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0032572
    reported_labels:
    - if available
    ontology_label: cardiac, facial, and digital anomalies with developmental delay
  - term_id: GO:0005929
    reported_labels:
    - GO cellular component:** cilium
    ontology_label: cilium
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Cardiac_Facial_And_Digital_Anomalies_With_Developmental_Delay-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** cardiac, facial, and digital anomalies with developmental delay (CAFDADD), caused by germline de novo TRAF7 missense variants (NOT somatic TRAF7 mutations in meningioma)
- **MONDO ID:** MONDO:0032572 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **cardiac, facial, and digital anomalies with developmental delay (CAFDADD), caused by germline de novo TRAF7 missense variants (NOT somatic TRAF7 mutations in meningioma)** covering all of the
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
- **Disease Name:** cardiac, facial, and digital anomalies with developmental delay (CAFDADD), caused by germline de novo TRAF7 missense variants (NOT somatic TRAF7 mutations in meningioma)
- **MONDO ID:** MONDO:0032572 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **cardiac, facial, and digital anomalies with developmental delay (CAFDADD), caused by germline de novo TRAF7 missense variants (NOT somatic TRAF7 mutations in meningioma)** covering all of the
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


# Comprehensive research report: germline TRAF7-related CAFDADD

## Scope and evidence boundary

This report concerns **cardiac, facial, and digital anomalies with developmental delay (CAFDADD) caused by germline heterozygous TRAF7 variants**. It does **not** treat sporadic, somatic TRAF7-mutant meningioma as CAFDADD. Tumor literature is mentioned only where it informs molecular biology or the still-unproven question of tumor surveillance.

The evidence base remains small: a seven-person discovery series in 2018, a 45-person series in 2020 (42-person core phenotype set), several case reports, and a 2024 synthesis totaling 68 reported individuals. Consequently, percentages describe published, clinically ascertained cases—not population risks—and are vulnerable to referral and publication bias. (castillavallmanya2020phenotypicspectrumand pages 2-3, tokita2018denovomissense pages 2-3, palmamilla2023expandingthephenotypic pages 15-17)

| Domain | Established finding | Quantitative evidence | Evidence type | Key limitation |
|---|---|---:|---|---|
| Scope and identifiers | Cardiac, facial, and digital anomalies with developmental delay (CAFDADD), also called TRAF7 syndrome or TRAF7-related neurodevelopmental disorder; MONDO:0032572, OMIM phenotype 618164, ORPHA:592570. The target is the germline developmental syndrome, not TRAF7-mutant meningioma. (OpenTargets Search: cardiac facial and digital anomalies with developmental delay-TRAF7, palmamilla2023expandingthephenotypic pages 1-3) | One associated causal target, **TRAF7**, is recorded for MONDO:0032572. | Aggregated disease resources and literature review | No dedicated ICD-10, ICD-11, or MeSH disease code was identified. |
| Cause and inheritance | Usually caused by a heterozygous germline **TRAF7** missense variant, most often arising de novo; variants cluster in C-terminal WD40 repeats. Rare inherited developmental variants with unaffected carrier parents and postzygotic mosaicism demonstrate exceptions and incomplete penetrance. (palmamilla2023expandingthephenotypic pages 8-10, castillavallmanya2020phenotypicspectrumand pages 2-3, mishragorur2023pleiotropicroleof pages 3-4) | Discovery series: 6/7 confirmed de novo; the seventh lacked paternal testing. In the 45-patient study, 20 amino-acid positions were affected and p.Arg655Gln occurred in 13 index cases. (castillavallmanya2020phenotypicspectrumand pages 2-3, tokita2018denovomissense pages 2-3) | Human genetic cohorts and segregation studies | Penetrance cannot be estimated reliably; inherited variants reported in a congenital-heart-disease study may not reproduce classic CAFDADD fully. |
| Variant spectrum | Recurrent variants include p.Arg655Gln, p.Arg524Trp, p.Phe617Leu, and substitutions at Ser558; most pathogenic syndromic variants alter conserved WD40 residues. The recent cohort added p.Arg653Leu; coiled-coil p.Lys346Glu illustrates a less-certain non-WD40 class. (palmamilla2023expandingthephenotypic pages 8-10, palmamilla2023expandingthephenotypic pages 3-5, castillavallmanya2020phenotypicspectrumand pages 2-3) | Eleven-person series: 8 distinct variants, 7 in WD40 repeats; p.Arg655Gln occurred in 4 unrelated individuals. All were absent from gnomAD v4. (palmamilla2023expandingthephenotypic pages 8-10) | Human sequencing and computational interpretation | Functional validation is unequal across variants; pathogenicity of some coiled-coil variants remains uncertain. |
| Core neurodevelopmental phenotype | Congenital or infantile hypotonia and developmental delay, especially expressive-language and motor delay, are central but variably severe; cognition ranges from normal or near-normal to intellectual disability. (palmamilla2023expandingthephenotypic pages 3-5, palmamilla2023expandingthephenotypic pages 8-10) | Among 68 reported cases: global developmental delay or intellectual disability 90.7%, speech delay 90.4%, motor delay 85.7%, hypotonia 84.8%, autism-spectrum traits 17.7%, seizures 19.0%, and structural neuroimaging abnormalities 79.3%. (palmamilla2023expandingthephenotypic pages 15-17) | Aggregated human case synthesis | Denominators vary by feature; ascertainment and publication bias may inflate frequencies. |
| Craniofacial and sensory phenotype | The recognizable gestalt includes blepharophimosis or ptosis, hypertelorism, abnormal ears and nose, palate or mouth anomalies, micrognathia or retrognathia, and a short or broad neck. Hearing and visual impairment can worsen communication and independence. (palmamilla2023expandingthephenotypic pages 5-8, palmamilla2023expandingthephenotypic pages 10-13) | Among 68 cases: ptosis or blepharophimosis approximately 64–75%, abnormal ears 72.3%, abnormal nose 65.6%, palate or mouth anomalies 74.5%, hearing loss 61.0%, and visual abnormalities 45.5%. (palmamilla2023expandingthephenotypic pages 15-17) | Aggregated human case synthesis | Definitions differ among reports; hearing loss may be conductive, sensorineural, or mixed. |
| Cardiac phenotype | Congenital cardiovascular disease is a major source of early morbidity. Patent ductus arteriosus is characteristic, but septal, valvular, arch, outflow-tract, and complex lesions occur. (tokita2018denovomissense pages 2-3) | Among 68 cases: any cardiovascular involvement 85.1%, patent ductus arteriosus 58.2%, valvular or septal defects 53.7%, coarctation 6.0%, pulmonary-artery stenosis 3.0%, and persistent left superior vena cava 4.5%. (palmamilla2023expandingthephenotypic pages 15-17) | Aggregated human case synthesis | The spectrum is broad, and genotype–cardiac-phenotype correlations are not established. |
| Digital and skeletal phenotype | Digital deviation, brachydactyly, syndactyly or other hand and foot anomalies, pectus carinatum, scoliosis, and pes planus or valgus are common. Craniosynostosis, sinus pericranii, and cranio-cervical anomalies define a reported severe cranial subgroup. (palmamilla2023expandingthephenotypic pages 5-8, palmamilla2023expandingthephenotypic pages 15-17) | Among 68 cases: digital anomalies 76.9%, pectus carinatum 45.5%, scoliosis 20.0%, and pes planus or valgus 33.3%. (palmamilla2023expandingthephenotypic pages 15-17) | Human cohorts and case reports | Craniosynostosis and sinus pericranii were reported in few patients and should not be considered universal. |
| Molecular mechanism | The strongest model is altered TRAF7 function, often dominant-negative rather than simple haploinsufficiency. Mutant proteins can heterodimerize with wild-type TRAF7, interact less with IFT57, and disturb ciliogenesis, intraflagellar transport, and neural-crest development. (mishragorur2023pleiotropicroleof pages 8-8, mishragorur2023pleiotropicroleof pages 8-9) | Zebrafish left-right-organizer ciliary beat frequency fell from 50.5 ± 7.14 Hz in controls to 33.47 ± 19.15 Hz in Traf7 morphants, p=6.5×10⁻⁹. (mishragorur2023pleiotropicroleof pages 6-7) | In vitro biochemistry; Xenopus and zebrafish models | The complete chain has not been demonstrated in patient embryonic tissues; knockdown and overexpression models do not precisely reproduce heterozygous human alleles. |
| Vascular signaling mechanism | TRAF7 supports endothelial integrity through the shear-responsive MEKK3–MEK5–ERK5–KLF2 pathway and interactions with SCRIB; disruption may contribute to cardiovascular abnormalities. (tsitsikov2023traf7isan pages 1-2, tsitsikov2023traf7isan pages 7-9) | Endothelial Traf7-null mice: 0% knockout live births versus 25% expected, N=81, χ²=27, p<0.0001; mutants developed fragmented vessels and died around embryonic day 10. (tsitsikov2023traf7isan pages 7-9) | Mouse knockout, embryonic RNA-seq, and HUVEC or HEK293 assays | Complete mouse deletion is embryonically lethal and substantially more severe than heterozygous human missense disease. |
| Diagnosis | Confirmation should use trio exome or genome sequencing, or an appropriate developmental-disorder or congenital-heart-disease panel, followed by ACMG/AMP interpretation and parental segregation testing. Baseline assessment should include echocardiography, development and speech, audiology, ophthalmology, growth and endocrine review, neurologic examination, and targeted brain or spine imaging. (castillavallmanya2020phenotypicspectrumand pages 2-3, palmamilla2023expandingthephenotypic pages 3-5, tokita2018denovomissense pages 2-3) | A representative p.Arg655Gln case was classified pathogenic using PS2, PM1, PM2, PP1, PP2, and PP3. (kim2024thefirstkorean pages 5-6) | Human clinical sequencing and case-series recommendations | No validated clinical criteria, biochemical biomarker, enzyme assay, or newborn-screening test exists. |
| Management | Care is supportive and phenotype-directed: cardiology intervention, early physical and occupational therapy, speech and feeding therapy, augmentative communication, hearing and vision treatment, plus orthopedic, neurologic, sleep, and endocrine care. (palmamilla2023expandingthephenotypic pages 8-10, palmamilla2023expandingthephenotypic pages 5-8) | In one 11-person cohort, sleep disorders affected 7/10, hearing loss 11/11, heart defects 10/11, and stature below −2 SD 8/11. (palmamilla2023expandingthephenotypic pages 5-8) | Human case-series recommendations | No disease-modifying drug, genotype-guided pharmacotherapy, gene, RNA, or cell therapy, or relevant interventional trial was identified. |
| Tumor boundary and surveillance | Somatic TRAF7-mutant meningioma is not CAFDADD. A few germline or mosaic syndrome cases with tumors prompted suggestions to consider oncology review after puberty, but cancer-risk magnitude and an evidence-based imaging schedule remain unproven. (palmamilla2023expandingthephenotypic pages 10-13, palmamilla2023expandingthephenotypic pages 8-10) | Reports cited two patients with meningioma and one adult with endometrioid adenocarcinoma; these are isolated observations, not incidence estimates. (palmamilla2023expandingthephenotypic pages 10-13, palmamilla2023expandingthephenotypic pages 8-10) | Human case reports and expert opinion | Routine serial tumor imaging is not an established consensus standard; benefits and harms are unknown. |
| Epidemiology and prognosis gaps | CAFDADD is ultra-rare, but prevalence, incidence, sex ratio, life expectancy, mortality, standardized quality-of-life scores, and validated prognostic biomarkers are unknown. Outcomes vary, and some early hypotonia or delay may improve. (palmamilla2023expandingthephenotypic pages 8-10, palmamilla2023expandingthephenotypic pages 1-3) | The recent synthesis tabulated 68 reported cases; this is a literature case count, not prevalence. (palmamilla2023expandingthephenotypic pages 15-17) | Literature synthesis | Published cases are referral- and publication-biased; long-term adult natural-history data are sparse. |
| Experimental models | Systems include patient fibroblasts, HEK293 and HUVEC assays, Xenopus and zebrafish knockdown or mutant-expression models, and global or endothelial conditional mouse knockouts. They support roles in transcriptional regulation, cilia and IFT, neural crest, heart development, and vascular integrity. (mishragorur2023pleiotropicroleof pages 6-7, mishragorur2023pleiotropicroleof pages 3-4, castillavallmanya2020phenotypicspectrumand pages 9-10, tsitsikov2023traf7isan pages 4-7) | Global Traf7-null mice showed significant genotype depletion by E11.5, N=17 and p=0.0047, and at birth, N=352 and p=0.0001. (tsitsikov2023traf7isan pages 4-7) | Patient-derived cells, in vitro systems, fish and amphibian models, and mouse genetics | No validated heterozygous knock-in model of a recurrent CAFDADD allele or naturally occurring homologous veterinary disease was identified. |


*Table: High-confidence knowledge-base summary for germline TRAF7-related CAFDADD, including clinical frequencies, mechanisms, diagnosis, management, evidence gaps, and models. Somatic TRAF7-mutant meningioma is included only as a disease boundary and limited surveillance context.*

## 1. Disease information

### Definition

CAFDADD is an ultra-rare, congenital, multisystem Mendelian neurodevelopmental disorder characterized by a recognizable craniofacial gestalt, developmental and especially speech/motor delay, congenital cardiovascular malformations, and digital or broader skeletal anomalies. Hypotonia, feeding difficulty, hearing impairment, growth deficiency, ophthalmologic abnormalities, sleep disturbance, and nonspecific brain abnormalities are frequent but variably expressed. (palmamilla2023expandingthephenotypic pages 5-8, palmamilla2023expandingthephenotypic pages 1-3, palmamilla2023expandingthephenotypic pages 15-17)

The landmark abstract concluded that de novo missense variants in TRAF7 “cause developmental delay, congenital anomalies, and dysmorphic features.” In its seven individuals, assessed motor and/or speech delay occurred in 5/5, congenital heart disease in 6/7, and digital and facial abnormalities in 7/7. [Tokita et al., published 5 July 2018; PMID: **29961569**; DOI/URL: https://doi.org/10.1016/j.ajhg.2018.06.005]. (tokita2018denovomissense pages 2-3)

### Identifiers and synonyms

- **MONDO:** MONDO:0032572.
- **OMIM phenotype:** **618164**.
- **Orphanet:** **ORPHA:592570**.
- **Causal gene:** TRAF7; Open Targets links MONDO:0032572 to TRAF7/ENSG00000131653 through five evidence records. (OpenTargets Search: cardiac facial and digital anomalies with developmental delay-TRAF7, palmamilla2023expandingthephenotypic pages 1-3)
- **Common names:** CAFDADD; TRAF7 syndrome; TRAF7-related disorder; TRAF7-related neurodevelopmental disorder; TRAF7-related multiple congenital anomalies–intellectual disability syndrome. “Blepharophimosis–mental retardation syndrome” has been used for an overlapping presentation but should not obscure the molecular diagnosis. (palmamilla2023expandingthephenotypic pages 1-3, kim2024thefirstkorean pages 5-6)
- **ICD-10/ICD-11 and MeSH:** no dedicated disease-specific code or descriptor was identified. Coding therefore generally uses manifestations, such as congenital heart defect, developmental delay, or congenital malformation syndrome.

The evidence is primarily **aggregated disease-level literature derived from individually phenotyped patients**, not EHR population surveillance. OMIM, Orphanet, MONDO, and Open Targets aggregate those reports. (OpenTargets Search: cardiac facial and digital anomalies with developmental delay-TRAF7, castillavallmanya2020phenotypicspectrumand pages 2-3)

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is a **heterozygous germline pathogenic or likely pathogenic TRAF7 variant**, predominantly a missense substitution affecting a conserved residue in a C-terminal WD40 repeat. Most classic cases are de novo. In the discovery series, six of seven were confirmed de novo; paternal testing was unavailable in the remaining individual. (palmamilla2023expandingthephenotypic pages 8-10, tokita2018denovomissense pages 2-3)

The disorder is best considered autosomal dominant with predominantly de novo occurrence. Rare inherited p.Val142Met, p.Val442Met, and splice c.1998+2T>G developmental variants were found with apparently unaffected carrier parents, supporting incomplete penetrance for at least some variant classes. Postzygotic mosaic TRAF7 disease has also been reported. These exceptional CHD/mosaic presentations should not be assumed to have the same penetrance or full phenotype as recurrent de novo WD40 variants. (mishragorur2023pleiotropicroleof pages 3-4, mishragorur2023pleiotropicroleof pages 8-9)

### Risk factors

- **Genetic:** a pathogenic germline TRAF7 allele is the principal risk factor. No reproducible modifier gene, susceptibility locus, founder allele, polygenic score, or genotype-specific prognostic marker has been established.
- **Parental age, sex, ancestry, family history:** no reliable associations are known. A de novo disorder usually has a negative family history.
- **Environmental, infectious, lifestyle, occupational:** no causal or modifying exposure has been demonstrated.
- **Protective factors:** no protective allele, diet, medication, behavior, or exposure is known.
- **Gene–environment interaction:** unstudied. Developmental shear stress is biologically relevant to endothelial TRAF7 signaling, but this is a physiological mechanical input—not an established environmental CAFDADD risk factor. (tsitsikov2023traf7isan pages 1-2, tsitsikov2023traf7isan pages 7-9)

## 3. Phenotypes

The most comprehensive recent table combined 68 published cases. Frequencies use differing feature-specific denominators and should be stored with provenance rather than interpreted as unbiased penetrance. (palmamilla2023expandingthephenotypic pages 15-17)

| Phenotype | Type, onset, course and impact | Published frequency | Suggested HPO term |
|---|---|---:|---|
| Global developmental delay/intellectual disability | Neurodevelopmental sign; infancy/childhood; severity variable. Early delay can improve, and a minority attain near-normal cognition, but many require lifelong educational support. | 90.7% | HP:0001263; HP:0001249 |
| Speech/language delay | Developmental/functional; usually early childhood; expressive communication is especially affected and may require augmentative communication. | 90.4% | HP:0000750; HP:0002474 |
| Motor delay | Developmental sign; infancy; sometimes improves with age and therapy. | 85.7% | HP:0001270 |
| Hypotonia | Neurologic sign; commonly neonatal/infantile; variable and potentially improving. Impairs feeding and gross-motor acquisition. | 84.8% | HP:0001252 |
| Autism/autistic traits | Behavioral; childhood; rigidity and reduced cognitive flexibility may occur even without formal ASD. | 17.7% | HP:0000729 |
| Seizures/epilepsy | Neurologic; infancy or childhood; variable. One recent case began at 2 months and was controlled with monotherapy. | 19.0% | HP:0001250 |
| Abnormal brain imaging | Imaging sign; congenital/developmental, often nonspecific—ventriculomegaly, dysgyria, cysts, hydrocephalus, or vermian hypoplasia. | 79.3% | HP:0410263 plus lesion-specific terms |
| Ptosis/blepharophimosis | Physical sign; congenital and generally stable; contributes to the facial gestalt and can obstruct vision. | approximately 64–75% | HP:0000508; HP:0000581 |
| Ear/nose abnormalities | Congenital dysmorphism; usually stable. | 72.3%/65.6% | HP:0000377; HP:0000366; HP:0000431 |
| Palate/mouth abnormalities | Congenital physical/feeding or speech manifestation. | 74.5% | HP:0000175; feature-specific term |
| Hearing loss | Sensory sign; congenital or childhood, conductive and/or sensorineural; worsens language acquisition and participation. | 61.0% | HP:0000365 |
| Visual abnormality | Sensory sign; congenital/childhood; ranges from refractive or ocular anomalies to cortical blindness/optic atrophy. | 45.5% | HP:0000504; HP:0100704; HP:0000648 |
| Congenital cardiovascular defect | Structural sign; prenatal/neonatal; stable unless repaired, but severity ranges from asymptomatic PDA to life-threatening complex disease. | 85.1% | HP:0001627 |
| Patent ductus arteriosus | Congenital cardiac lesion; may cause early morbidity and require closure. | 58.2% | HP:0001643 |
| Valvular/septal defect | Congenital cardiac lesion; variable severity. | 53.7% | HP:0001654 and lesion-specific terms |
| Digital anomaly | Congenital physical sign; generally stable; includes deviations, brachydactyly and syndactyly, affecting dexterity variably. | 76.9% | HP:0011297; HP:0001156; HP:0001166 |
| Pectus carinatum | Skeletal manifestation; congenital/childhood, often more evident with growth. | 45.5% | HP:0000768 |
| Scoliosis | Musculoskeletal sign; childhood/adolescence and potentially progressive. | 20.0% | HP:0002650 |
| Pes planus/valgus | Musculoskeletal sign; childhood, potentially affecting gait. | 33.3% | HP:0001763; HP:0001772 |

These figures are supported by the 68-case synthesis: motor delay 85.7%, speech delay 90.4%, global delay/ID 90.7%, hypotonia 84.8%, autism traits 17.7%, seizures 19.0%, imaging abnormalities 79.3%, cardiovascular involvement 85.1%, PDA 58.2%, valvular/septal defects 53.7%, digital anomalies 76.9%, hearing loss 61.0%, and visual abnormalities 45.5%. (palmamilla2023expandingthephenotypic pages 15-17)

Additional clinically important manifestations include prenatal cystic hygroma, single umbilical artery, polyhydramnios and fetal growth restriction; neonatal poor sucking; tube or gastrostomy feeding in severe dysphagia; short stature/endocrine abnormalities; broad or short neck; pectus deformity; hernia, genitourinary and renal findings; and sleep-disordered breathing. In the recent 11-person cohort, hypotonia was 11/11, poor sucking 7/11, MRI abnormality 9/11, heart defect 10/11, PDA 6/11, sleep disorder 7/10, hearing loss 11/11, visual abnormality 9/11, digital anomaly 11/11, and height below −2 SD 8/11. (palmamilla2023expandingthephenotypic pages 3-5, palmamilla2023expandingthephenotypic pages 5-8)

A cranial subgroup has multiple craniosynostosis, pear-shaped skull, sinus pericranii, skull-base/craniocervical anomalies, dysgyria, and inferior cerebellar-vermis hypoplasia; these are important but not universal findings. [Accogli et al., published 2020; DOI: https://doi.org/10.1002/bdr2.1711]. (palmamilla2023expandingthephenotypic pages 10-13)

No CAFDADD-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or other standardized quality-of-life study was identified. Functional burden is inferred from cardiac procedures, feeding support, sensory loss, communication impairment, developmental disability, sleep disturbance, and orthopedic needs. (palmamilla2023expandingthephenotypic pages 8-10, palmamilla2023expandingthephenotypic pages 5-8)

## 4. Genetic and molecular information

### Gene and protein

**TRAF7** encodes TNF receptor-associated factor 7, a 670-amino-acid intracellular signaling protein and E3 ubiquitin ligase. Its architecture comprises an N-terminal RING finger, adjacent zinc finger, coiled-coil region, and seven C-terminal WD40 repeats. Unlike canonical TRAFs, its C terminus is dominated by WD40 repeats rather than a conventional TRAF-C domain. (palmamilla2023expandingthephenotypic pages 3-5, castillavallmanya2020phenotypicspectrumand pages 1-2)

Useful identifiers are **HGNC:20456**, NCBI Gene **84231**, Ensembl **ENSG00000131653**, and OMIM gene **606692**. The Open Targets disease association independently records ENSG00000131653 as the sole associated target for MONDO:0032572. (OpenTargets Search: cardiac facial and digital anomalies with developmental delay-TRAF7)

### Variant spectrum and classification

Most established variants are **heterozygous missense alleles** clustered in WD40 repeats. Recurrent changes include p.Arg655Gln, p.Arg524Trp, p.Phe617Leu/Phe617Ser, and substitutions at Ser558; p.Arg655Gln occurred in 13 index cases in the 2020 cohort and in four unrelated members of the recent 11-case cohort. The latter added novel p.Arg653Leu; seven of eight variants were in WD40 repeats, while p.Lys346Glu affected the coiled-coil region. (palmamilla2023expandingthephenotypic pages 8-10, castillavallmanya2020phenotypicspectrumand pages 2-3)

The original four disease variants were absent from ExAC and gnomAD. All eight variants in the 2023/2024 cohort were absent from gnomAD v4, affected conserved residues, and were computationally deleterious. Population absence supports PM2 but does not independently prove pathogenicity. (palmamilla2023expandingthephenotypic pages 8-10, tokita2018denovomissense pages 2-3)

A representative NM_032271.3:c.1964G>A, p.Arg655Gln allele was heterozygous and de novo and classified pathogenic using ACMG/AMP PS2, PM1, PM2, PP1, PP2 and PP3. [Kim et al., published March 2024; DOI: https://doi.org/10.3390/ijms25073701]. (kim2024thefirstkorean pages 5-6)

### Functional consequence

The recurrence and regional clustering of missense variants, together with a low reported gnomAD pLI of 0.02 and scarcity of classic truncating CAFDADD alleles, argue against simple haploinsufficiency as the universal mechanism. The leading model is **altered function, commonly dominant-negative**, although mechanism may vary by allele. Mutant TRAF7 can heterodimerize with wild-type protein and interfere with its function; the c.1998+2T>G allele provides evidence that haploinsufficiency can occur in a partially penetrant CHD presentation. (castillavallmanya2020phenotypicspectrumand pages 2-3, castillavallmanya2020phenotypicspectrumand pages 1-2, mishragorur2023pleiotropicroleof pages 8-9)

No validated modifier genes, syndrome-specific episignature, recurrent chromosomal abnormality, DNA-methylation signature, or structural rearrangement causing classic CAFDADD has been established. Somatic TRAF7 tumor variants must not be classified as germline CAFDADD variants solely because they occur in the same gene.

## 5. Environmental information

CAFDADD is a genetic developmental disorder. No toxin, radiation, pollution, occupation, smoking, alcohol, diet, exercise pattern, medication, bacterium, virus, fungus, or parasite is known to cause or trigger it. No lifestyle intervention prevents expression after conception, and there is no evidence for infectious transmission or zoonosis.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous germline TRAF7 missense variant—usually in a WD40 repeat—**leads to** altered TRAF7 folding, partner recognition and/or oligomeric function; for several alleles, a dominant-negative effect is experimentally supported. (castillavallmanya2020phenotypicspectrumand pages 1-2, mishragorur2023pleiotropicroleof pages 8-9)
2. Altered TRAF7 **leads to** impaired interaction with IFT57 and abnormal intraflagellar transport; this is demonstrated in cell and Xenopus assays but not directly in human embryonic tissue. (mishragorur2023pleiotropicroleof pages 8-8, mishragorur2023pleiotropicroleof pages 9-10)
3. Defective intraflagellar transport **results in** shortened, fewer, structurally abnormal or hypomotile cilia and disturbed left–right organizer signaling. (mishragorur2023pleiotropicroleof pages 6-7, mishragorur2023pleiotropicroleof pages 8-8)
4. Ciliary dysfunction **leads to** abnormal neural-crest specification/migration and laterality-dependent morphogenesis—demonstrated in Xenopus and zebrafish and inferred in humans. (mishragorur2023pleiotropicroleof pages 3-4, mishragorur2023pleiotropicroleof pages 8-9)
5. **Branch A:** neural-crest and ciliary disruption **results in** craniofacial, pharyngeal-arch, cardiac-outflow and digital/skeletal maldevelopment; the final human linkage is strongly plausible but incompletely demonstrated. (mishragorur2023pleiotropicroleof pages 3-4)
6. **Branch B:** altered TRAF7/SCRIB/MEKK3–MEK5–ERK5 signaling **leads to** reduced shear-responsive ERK5 phosphorylation and KLF2/KLF4 regulation in endothelium. (tsitsikov2023traf7isan pages 1-2, ihuoma2025reviewofthe pages 6-7)
7. Impaired endothelial developmental signaling **results in** deficient vessel integrity and cardiovascular morphogenesis in knockout mice; contribution to human septal, valvular, arch and ductal lesions is inferred. (tsitsikov2023traf7isan pages 7-9, tsitsikov2023traf7isan pages 4-7)
8. **Branch C:** broader perturbation of MAPK/JNK/p38, NF-κB and transcriptional regulation **may lead to** altered cell survival, apoptosis, proliferation and differentiation; this is biological context, not a fully validated patient-level causal chain. (palmamilla2023expandingthephenotypic pages 3-5, castillavallmanya2020phenotypicspectrumand pages 1-2)
9. These embryonic tissue-patterning abnormalities **result in** the congenital cardiac, facial, digital, skeletal, brain and sensory phenotype, while downstream developmental consequences **lead to** hypotonia, feeding difficulty, delayed motor/language acquisition and variable intellectual/behavioral disability. (palmamilla2023expandingthephenotypic pages 5-8, palmamilla2023expandingthephenotypic pages 15-17)

### Experimental detail

**Cilia/IFT and neural crest.** TRAF7 was identified as an IFT57-binding partner. CHD-associated V442M and T601A and another mutant showed reduced IFT57 interaction. Xenopus Traf7 depletion severely retarded anterograde IFT80-GFP, retrograde IFT43-GFP and IFT57-GFP transport and produced electron-dense ciliary blebs. Zebrafish morphants had reduced or paralyzed left–right-organizer cilia; mean beat frequency decreased from **50.5 ± 7.14 Hz to 33.47 ± 19.15 Hz** (p=6.5×10⁻⁹). Knockdown reduced sox10 and disorganized pharyngeal arches, while Xenopus showed altered Sox10/Twist, abnormal heart looping, edema and craniofacial defects. (mishragorur2023pleiotropicroleof pages 6-7, mishragorur2023pleiotropicroleof pages 8-8, mishragorur2023pleiotropicroleof pages 3-4)

**Endothelium.** Global Traf7-null and Tie2-Cre endothelial-knockout mouse embryos developed discontinuous, fragmented and poorly branched vessels, hemorrhage and death near E10. No endothelial-knockout pups were born—0% observed versus 25% expected (N=81; χ²=27; p<0.0001). RNA-seq identified HIF-1-pathway changes, reduced Klf2, increased Bnip3 and reduced Nppc/Serpina6. TRAF7 associates with SCRIB, MEKK3 and MEK5; TRAF7 or SCRIB reduction suppressed shear-induced ERK5 phosphorylation. (tsitsikov2023traf7isan pages 7-9, tsitsikov2023traf7isan pages 4-7, tsitsikov2023traf7isan pages 2-4)

**Human fibroblast transcriptomics.** Four patient and six control fibroblast lines were analyzed by qRT-PCR and RNA-seq, including TNFα exposure. Differentially expressed genes were found, but available evidence did not establish a reproducible clinical biomarker or complete causal pathway; the authors specifically cautioned that coiled-coil and WD40 variants may require separate functional evaluation. (castillavallmanya2020phenotypicspectrumand pages 2-3, castillavallmanya2020phenotypicspectrumand pages 9-10)

No CAFDADD-specific single-cell atlas, spatial transcriptomic map, metabolomic/lipidomic signature, proteomic biomarker, CRISPR screen, or validated multi-omics classifier is available.

### Suggested ontology annotations

- **GO biological process:** protein ubiquitination (GO:0016567); MAPK cascade (GO:0000165); cilium assembly (GO:0060271); intraciliary transport (GO:0042073); neural crest cell development (GO:0014032); heart morphogenesis (GO:0003007); blood-vessel development (GO:0001568); regulation of apoptotic process (GO:0042981).
- **GO cellular component:** cilium (GO:0005929); intraciliary transport particle (GO:0030990); cytoplasm (GO:0005737); ubiquitin ligase complex (GO:0000151).
- **Cell Ontology:** neural crest cell (CL:0000333); endothelial cell (CL:0000115); vascular endothelial cell (CL:0002139); cardiomyocyte (CL:0000746); fibroblast (CL:0000057). These are mechanistically implicated or experimentally used; they are not all proven primary targets in human tissue.

## 7. Anatomical structures affected

Primary systems are cardiovascular, nervous/neurodevelopmental, craniofacial/sensory and musculoskeletal. Cardiac sites include ductus arteriosus, valves, atrial/ventricular septa, aortic arch and outflow tract. Craniofacial involvement includes eyelids/palpebral fissures, ears, nose, palate, mandible, skull sutures and craniocervical junction. Nervous-system sites include brain ventricles, cortex, cerebellar vermis, optic pathways and spinal cord; hands, feet, digits, sternum and spine are commonly involved. (tokita2018denovomissense pages 2-3, palmamilla2023expandingthephenotypic pages 5-8, palmamilla2023expandingthephenotypic pages 10-13, palmamilla2023expandingthephenotypic pages 15-17)

Suggested UBERON annotations include heart (UBERON:0000948), ductus arteriosus (UBERON:0002092), blood vessel (UBERON:0001981), brain (UBERON:0000955), spinal cord (UBERON:0002240), eye (UBERON:0000970), ear (UBERON:0001690), skull (UBERON:0003129), hand (UBERON:0002398), foot (UBERON:0002387), and digit (UBERON:0002544). Laterality is not a defining feature, although laterality defects/heterotaxy occurred in selected developmental-variant cases. (mishragorur2023pleiotropicroleof pages 3-4)

At the subcellular level, the most relevant compartments are the cilium/IFT apparatus, cytoplasm, and protein complexes containing TRAF7, IFT57, SCRIB, MEKK3 and MEK5. Mitochondrial, lysosomal or ER pathology has not been established.

## 8. Temporal development

The initiating lesion is present from conception. Structural manifestations are congenital and may be detected prenatally through cystic hygroma, single umbilical artery, polyhydramnios, growth restriction or cardiac malformation. Hypotonia, poor feeding and cardiac complications commonly emerge neonatally; motor and language delay become evident in infancy or early childhood. (palmamilla2023expandingthephenotypic pages 3-5, tokita2018denovomissense pages 2-3)

CAFDADD is chronic and lifelong rather than episodic or relapsing. Structural malformations are usually stable unless surgically corrected, while scoliosis, growth deficiency, sleep-disordered breathing and cardiovascular complications can evolve. Hypotonia and developmental delay may improve; expressive-language, hearing and behavioral difficulties can persist. There is no validated stage system, remission definition, progression rate or critical therapeutic window, although early cardiac recognition, hearing correction, feeding support and developmental intervention are clinically important. (palmamilla2023expandingthephenotypic pages 8-10, palmamilla2023expandingthephenotypic pages 5-8)

## 9. Inheritance and population

- **Pattern:** autosomal dominant, usually de novo. (tokita2018denovomissense pages 2-3)
- **Penetrance:** apparently high for recurrent classic de novo WD40 variants among ascertained patients, but not quantifiable. Unaffected parents carrying selected inherited variants demonstrate incomplete penetrance. (mishragorur2023pleiotropicroleof pages 3-4, mishragorur2023pleiotropicroleof pages 8-9)
- **Expressivity:** markedly variable, from severe complex congenital heart disease and intellectual disability to improving development or near-normal cognition. (palmamilla2023expandingthephenotypic pages 8-10)
- **Anticipation:** not reported.
- **Parental germline mosaicism:** theoretically relevant to recurrence counseling but no reliable frequency is established. Postzygotic affected-person mosaicism is documented.
- **Founder effects, consanguinity and carrier frequency:** none established; consanguinity is not mechanistically expected to increase a predominantly de novo dominant disorder.
- **Prevalence/incidence:** unknown. The 68 compiled cases are a literature count, not a prevalence estimate. (palmamilla2023expandingthephenotypic pages 15-17)
- **Sex/ancestry/geography:** no valid sex ratio or enriched population is established. The 11-person Spanish cohort contained eight males and three females, but this is not epidemiologic evidence. Cases have been reported across ancestries, including the first Korean report in 2024. (palmamilla2023expandingthephenotypic pages 3-5, kim2024thefirstkorean pages 5-6)

For an affected individual with a constitutional heterozygous variant, transmission risk is theoretically 50% per conception, modified by reproductive fitness and variant penetrance. For unaffected parents of a proven de novo case, recurrence risk is low but above zero because gonadal mosaicism cannot be excluded.

## 10. Diagnostics

### Clinical and genetic approach

1. Recognize the combination of blepharophimosis/ptosis and characteristic facial morphology, congenital heart disease, digital or pectus abnormalities, hypotonia and developmental/speech delay.
2. Perform **trio exome or genome sequencing**, or a broad developmental-disorder/congenital-heart-disease panel containing TRAF7. Confirm reportable variants and test parents by Sanger sequencing or an equivalent method. The 2020 cohort used exome, targeted capture and Sanger sequencing. (castillavallmanya2020phenotypicspectrumand pages 2-3)
3. Interpret with ACMG/AMP criteria, considering de novo status, WD40 hotspot/domain location, population absence, recurrence and phenotype match. Do not apply tumor-only annotations as germline pathogenic evidence without constitutional interpretation. (palmamilla2023expandingthephenotypic pages 8-10, kim2024thefirstkorean pages 5-6)

**WGS** may identify coding, splice and structural alternatives missed by WES, but no CAFDADD-specific yield comparison exists. **WES** has demonstrated utility and remains a practical first-line test. **Single-gene TRAF7 sequencing** is reasonable when the gestalt is strong, but broad testing is preferable in nonspecific developmental delay. **CMA** remains useful for detecting alternative copy-number diagnoses; karyotype, FISH, mitochondrial and repeat-expansion testing are not tests for CAFDADD unless another diagnosis is suspected.

There is no diagnostic blood/urine biochemical marker, enzyme assay, biopsy pattern, metabolomic signature, epigenetic signature or liquid-biopsy test.

### Baseline phenotyping after diagnosis

Recommended evaluation includes echocardiography and cardiology consultation; growth/endocrine assessment; developmental, cognitive, speech/language and behavioral evaluation; feeding/swallow review; audiology; ophthalmology; neurologic examination with EEG for suspected seizures; sleep assessment; orthopedic/spine examination; and brain/spine imaging when neurologic, cranial or tethered-cord findings warrant it. (palmamilla2023expandingthephenotypic pages 3-5, tokita2018denovomissense pages 2-3, palmamilla2023expandingthephenotypic pages 5-8)

### Differential diagnosis

Important differentials include KAT6B-related disorders/Ohdo syndrome, FAT1-related disease, RASopathies including Costello syndrome, connective-tissue disorders, and other blepharophimosis–developmental-delay or syndromic CHD conditions. Distinguishing evidence is a pathogenic constitutional TRAF7 variant plus the characteristic combined phenotype. (palmamilla2023expandingthephenotypic pages 10-13)

No universally accepted clinical diagnostic criteria, newborn screen, carrier-screening program, or population screening program exists. Prenatal or preimplantation genetic testing is technically possible once a familial pathogenic variant is known.

## 11. Outcome and prognosis

Long-term natural history is poorly defined. No five- or ten-year survival, life-expectancy estimate, mortality rate or disease-specific mortality statistic exists. Early morbidity is driven mainly by severe congenital heart disease, feeding/aspiration risk, sensory impairment and developmental disability. Later burdens may include orthopedic disease, sleep apnea and unresolved cardiovascular complications. (palmamilla2023expandingthephenotypic pages 5-8, palmamilla2023expandingthephenotypic pages 8-10)

The 36-year-old Korean individual demonstrates survival into adulthood and the need for adult cardiology: bicuspid aortic valve, aortic-root aneurysm and regurgitation required a Bentall operation. Persistent dyspnea was subsequently attributed to obstructive sleep apnea and improved with continuous positive airway pressure, illustrating that symptoms may have multiple treatable causes. (kim2024thefirstkorean pages 5-6)

Prognosis is highly variable. Some children show improvement in hypotonia and early psychomotor delay and may achieve normal or near-normal later cognition; others require lifelong communication and daily-living support. No validated prognostic biomarker or genotype-based outcome calculator exists. (palmamilla2023expandingthephenotypic pages 8-10)

A few tumors have been observed in germline/mosaic TRAF7-related individuals, including meningiomas and one endometrioid adenocarcinoma. These isolated reports do not establish incidence, penetrance or causality and should not be conflated with the common somatic TRAF7 alterations in sporadic meningioma. (palmamilla2023expandingthephenotypic pages 10-13, palmamilla2023expandingthephenotypic pages 8-10)

## 12. Treatment

No disease-modifying pharmacotherapy, approved TRAF7-targeted treatment, gene therapy, genome editing, ASO/siRNA, mRNA therapy, cell therapy or syndrome-specific immunotherapy exists. No relevant interventional clinical trial was identified. Tumor-directed TRAF7 research should not be extrapolated to children with germline CAFDADD.

Management is individualized and supportive:

- **Cardiology:** surveillance and lesion-specific medical, catheter or surgical treatment—e.g., PDA closure, repair of septal/outflow/arch disease, or valve/aortic-root surgery. Suggested NCIT concepts: Echocardiography; Cardiac Surgery; Patent Ductus Arteriosus Closure.
- **Development:** early physical therapy, occupational therapy, special education and neuropsychology. NCIT: Physical Therapy; Occupational Therapy; Early Intervention.
- **Communication:** speech/language therapy and augmentative or alternative communication when expressive language is limited. NCIT: Speech Therapy.
- **Feeding:** nutrition, feeding/swallow therapy, aspiration precautions, and nasogastric or gastrostomy support when necessary. NCIT: Nutritional Support; Gastrostomy.
- **Hearing/vision:** periodic audiology; tympanostomy/drainage or hearing devices where indicated; ophthalmic correction and ptosis management. Hearing treatment may improve communication. (palmamilla2023expandingthephenotypic pages 8-10)
- **Neurology:** standard antiseizure therapy for epilepsy; one recent patient achieved control with monotherapy. (palmamilla2023expandingthephenotypic pages 5-8)
- **Sleep/respiratory:** polysomnography for symptoms, sleep-hygiene/medical treatment, and CPAP for obstructive sleep apnea when indicated. (kim2024thefirstkorean pages 5-6)
- **Musculoskeletal:** orthopedic surveillance, physiotherapy, bracing or surgery according to scoliosis, foot deformity, craniosynostosis or craniocervical disease.
- **Growth/endocrine and behavioral care:** longitudinal growth/puberty review and individualized psychological/psychiatric support. (palmamilla2023expandingthephenotypic pages 8-10, palmamilla2023expandingthephenotypic pages 5-8)

There are no disease-specific response rates, adverse-event datasets, pharmacogenomic recommendations or validated treatment algorithm.

## 13. Prevention

**Primary prevention** by lifestyle or vaccination is not applicable. For reproductive prevention, genetic counseling should explain de novo dominant inheritance, residual gonadal-mosaicism risk, and options for prenatal diagnosis or preimplantation genetic testing when the familial variant is known.

**Secondary prevention** consists of early molecular diagnosis and prompt evaluation for cardiac, hearing, vision, feeding, developmental and neurologic complications. Population newborn or carrier screening is not currently justified by available evidence.

**Tertiary prevention** includes cardiology follow-up, hearing correction, developmental and communication intervention, aspiration and sleep-apnea management, orthopedic monitoring and seizure treatment. Some authors propose oncology review after puberty, but no validated cancer-screening modality or interval exists; routine serial MRI should therefore be individualized rather than presented as consensus care. (palmamilla2023expandingthephenotypic pages 10-13, palmamilla2023expandingthephenotypic pages 8-10)

Routine immunization should follow general population guidance; CAFDADD is not an infectious or primary immunodeficiency disorder based on current clinical evidence.

## 14. Other species and natural disease

No naturally occurring CAFDADD-equivalent disease, TRAF7 syndrome, breed predisposition or veterinary transmission syndrome was identified in companion animals, livestock or wildlife. There is no zoonotic potential.

Orthologous TRAF7 genes are evolutionarily conserved in vertebrates, enabling experimental work in mouse (**Mus musculus**, NCBI Taxon 10090), zebrafish (**Danio rerio**, 7955), and western clawed frog (**Xenopus tropicalis**, 8364). Conservation supports comparative developmental biology but does not establish spontaneous disease in those species. (mishragorur2023pleiotropicroleof pages 6-7, mishragorur2023pleiotropicroleof pages 3-4)

## 15. Model organisms and experimental systems

### Mouse

Global Traf7 deletion using E2a-Cre and endothelial deletion using Tie2-Cre cause hemorrhage, fragmented vessels, cardiac abnormalities and embryonic death around E10. Global-knockout genotype depletion became significant by E11.5 (N=17, p=0.0047) and at birth (N=352, p=0.0001). Inducible postnatal endothelial deletion using Cdh5(PAC)-CreERT2 causes focal cerebral hemorrhage. These models establish essential endothelial and vascular functions but are much more severe than heterozygous human missense disease. [Tsitsikov et al., published August 2023; DOI: https://doi.org/10.1016/j.isci.2023.107474]. (tsitsikov2023traf7isan pages 4-7, tsitsikov2023traf7isan pages 21-23, ihuoma2025reviewofthe pages 4-6)

### Zebrafish and Xenopus

Traf7 knockdown/morphant models reproduce abnormal heart looping, edema, pharyngeal-arch disorganization, reduced neural-crest markers, craniofacial skeletal abnormalities, hydrocephalus, renal cysts and defective ciliary motility. Mutant-mRNA expression supports dominant effects for selected variants. These systems are useful for neural crest, cilia, laterality and cardiogenesis, but morpholino depletion and overexpression are imperfect models of a constitutional heterozygous human allele. (mishragorur2023pleiotropicroleof pages 6-7, mishragorur2023pleiotropicroleof pages 3-4, mishragorur2023pleiotropicroleof pages 8-9)

### Cellular systems

Patient fibroblasts have supported transcriptomic investigation; HEK293 cells have been used for protein interaction and mutant-expression assays; HUVECs model endothelial shear responses. These systems implicate IFT57, SCRIB and MEKK3–MEK5–ERK5–KLF2 signaling but do not recreate human embryonic tissue patterning. (mishragorur2023pleiotropicroleof pages 8-8, castillavallmanya2020phenotypicspectrumand pages 9-10, tsitsikov2023traf7isan pages 13-15)

No validated recurrent-variant heterozygous knock-in mouse, patient-derived iPSC cardiac/neural-crest model, organoid model, or high-throughput therapeutic-screening platform was identified.

## Evidence-weighted conclusions

1. **High confidence:** CAFDADD is a germline, usually de novo autosomal-dominant TRAF7 missense disorder with characteristic neurodevelopmental, craniofacial, cardiac and digital/skeletal abnormalities. (OpenTargets Search: cardiac facial and digital anomalies with developmental delay-TRAF7, tokita2018denovomissense pages 2-3, palmamilla2023expandingthephenotypic pages 15-17)
2. **Moderate-to-high confidence:** recurrent WD40 missense alleles act through altered function, often dominant-negative, rather than uniform haploinsufficiency. (castillavallmanya2020phenotypicspectrumand pages 2-3, mishragorur2023pleiotropicroleof pages 8-9)
3. **Moderate mechanistic confidence:** disrupted IFT57-dependent ciliary transport, neural-crest development and endothelial MEKK3–MEK5–ERK5–KLF2 signaling plausibly connect TRAF7 dysfunction to the phenotype; much of this chain rests on cell, fish, amphibian and knockout-mouse models rather than direct human embryonic evidence. (mishragorur2023pleiotropicroleof pages 6-7, mishragorur2023pleiotropicroleof pages 8-8, tsitsikov2023traf7isan pages 7-9)
4. **Clinical practice:** diagnosis is molecular, preferably by trio sequencing; management is multidisciplinary and manifestation-directed. No disease-modifying therapy or relevant trial exists. (palmamilla2023expandingthephenotypic pages 8-10, castillavallmanya2020phenotypicspectrumand pages 2-3, palmamilla2023expandingthephenotypic pages 5-8)
5. **Major gaps:** unbiased epidemiology, penetrance, adult natural history, survival, quality of life, variant-specific functional validation, tumor-risk quantification, validated surveillance guidelines, and faithful heterozygous knock-in models remain unavailable.

References

1. (castillavallmanya2020phenotypicspectrumand pages 2-3): Laura Castilla-Vallmanya, Kaja K. Selmer, Clémantine Dimartino, Raquel Rabionet, Bernardo Blanco-Sánchez, Sandra Yang, Margot R.F. Reijnders, Antonie J. van Essen, Myriam Oufadem, Magnus D. Vigeland, Barbro Stadheim, Gunnar Houge, Helen Cox, Helen Kingston, Jill Clayton-Smith, Jeffrey W. Innis, Maria Iascone, Anna Cereda, Sara Gabbiadini, Wendy K. Chung, Victoria Sanders, Joel Charrow, Emily Bryant, John Millichap, Antonio Vitobello, Christel Thauvin, Frederic Tran Mau-Them, Laurence Faivre, Gaetan Lesca, Audrey Labalme, Christelle Rougeot, Nicolas Chatron, Damien Sanlaville, Katherine M. Christensen, Amelia Kirby, Raymond Lewandowski, Rachel Gannaway, Maha Aly, Anna Lehman, Lorne Clarke, Luitgard Graul-Neumann, Christiane Zweier, Davor Lessel, Bernarda Lozic, Ingvild Aukrust, Ryan Peretz, Robert Stratton, Thomas Smol, Anne Dieux-Coëslier, Joanna Meira, Elizabeth Wohler, Nara Sobreira, Erin M. Beaver, Jennifer Heeley, Lauren C. Briere, Frances A. High, David A. Sweetser, Melissa A. Walker, Catherine E. Keegan, Parul Jayakar, Marwan Shinawi, Wilhelmina S. Kerstjens-Frederikse, Dawn L. Earl, Victoria M. Siu, Emma Reesor, Tony Yao, Robert A. Hegele, Olena M. Vaske, Shannon Rego, Kevin A. Shapiro, Brian Wong, Michael J. Gambello, Marie McDonald, Danielle Karlowicz, Roberto Colombo, Alessandro Serretti, Lynn Pais, Anne O’Donnell-Luria, Alison Wray, Simon Sadedin, Belinda Chong, Tiong Y. Tan, John Christodoulou, Susan M. White, Anne Slavotinek, Deborah Barbouth, Dayna Morel Swols, Mélanie Parisot, Christine Bole-Feysot, Patrick Nitschké, Véronique Pingault, Arnold Munnich, Megan T. Cho, Valérie Cormier-Daire, Susanna Balcells, Stanislas Lyonnet, Daniel Grinberg, Jeanne Amiel, Roser Urreizti, and Christopher T. Gordon. Phenotypic spectrum and transcriptomic profile associated with germline variants in traf7. Jul 2020. URL: https://doi.org/10.1038/s41436-020-0792-7, doi:10.1038/s41436-020-0792-7. This article has 38 citations and is from a highest quality peer-reviewed journal.

2. (tokita2018denovomissense pages 2-3): Mari J. Tokita, Chun-An Chen, David Chitayat, Ellen Macnamara, Jill A. Rosenfeld, Neil Hanchard, Andrea M. Lewis, Chester W. Brown, Ronit Marom, Yunru Shao, Danica Novacic, Lynne Wolfe, Colleen Wahl, Cynthia J. Tifft, Camilo Toro, Jonathan A. Bernstein, Caitlin L. Hale, Julia Silver, Louanne Hudgins, Amitha Ananth, Andrea Hanson-Kahn, Shirley Shuster, Pilar L. Magoulas, Vipulkumar N. Patel, Wenmiao Zhu, Stella M. Chen, Yanjun Jiang, Pengfei Liu, Christine M. Eng, Dominyka Batkovskyte, Alberto di Ronza, Marco Sardiello, Brendan H. Lee, Christian P. Schaaf, Yaping Yang, and Xia Wang. De novo missense variants in traf7 cause developmental delay, congenital anomalies, and dysmorphic features. American journal of human genetics, 103 1:154-162, Jul 2018. URL: https://doi.org/10.1016/j.ajhg.2018.06.005, doi:10.1016/j.ajhg.2018.06.005. This article has 60 citations and is from a highest quality peer-reviewed journal.

3. (palmamilla2023expandingthephenotypic pages 15-17): Carmen Palma-Milla, Aina Prat-Planas, Emma Soengas-Gonda, Mónica Centeno-Pla, Jaime Sánchez-Pozo, Irene Lazaro-Rodriguez, Juan F. Quesada-Espinosa, Ana Arteche-Lopez, Jonathan Olival, Marta Pacio-Miguez, María Palomares-Bralo, Fernando Santos-Simarro, Ramón Cancho-Candela, María Vázquez-López, Veronica Seidel, Antonio F Martinez-Monseny, Didac Casas-Alba, Daniel Grinberg, Susanna Balcells, Mercedes Serrano, Raquel Rabionet, Miguel A. Martin, and Roser Urreizti. Expanding the phenotypic spectrum of traf7 syndrome: report of eleven new cases and literature review. MedRxiv, Dec 2023. URL: https://doi.org/10.1101/2023.12.13.23299272, doi:10.1101/2023.12.13.23299272. This article has 0 citations.

4. (OpenTargets Search: cardiac facial and digital anomalies with developmental delay-TRAF7): Open Targets Query (cardiac facial and digital anomalies with developmental delay-TRAF7, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (palmamilla2023expandingthephenotypic pages 1-3): Carmen Palma-Milla, Aina Prat-Planas, Emma Soengas-Gonda, Mónica Centeno-Pla, Jaime Sánchez-Pozo, Irene Lazaro-Rodriguez, Juan F. Quesada-Espinosa, Ana Arteche-Lopez, Jonathan Olival, Marta Pacio-Miguez, María Palomares-Bralo, Fernando Santos-Simarro, Ramón Cancho-Candela, María Vázquez-López, Veronica Seidel, Antonio F Martinez-Monseny, Didac Casas-Alba, Daniel Grinberg, Susanna Balcells, Mercedes Serrano, Raquel Rabionet, Miguel A. Martin, and Roser Urreizti. Expanding the phenotypic spectrum of traf7 syndrome: report of eleven new cases and literature review. MedRxiv, Dec 2023. URL: https://doi.org/10.1101/2023.12.13.23299272, doi:10.1101/2023.12.13.23299272. This article has 0 citations.

6. (palmamilla2023expandingthephenotypic pages 8-10): Carmen Palma-Milla, Aina Prat-Planas, Emma Soengas-Gonda, Mónica Centeno-Pla, Jaime Sánchez-Pozo, Irene Lazaro-Rodriguez, Juan F. Quesada-Espinosa, Ana Arteche-Lopez, Jonathan Olival, Marta Pacio-Miguez, María Palomares-Bralo, Fernando Santos-Simarro, Ramón Cancho-Candela, María Vázquez-López, Veronica Seidel, Antonio F Martinez-Monseny, Didac Casas-Alba, Daniel Grinberg, Susanna Balcells, Mercedes Serrano, Raquel Rabionet, Miguel A. Martin, and Roser Urreizti. Expanding the phenotypic spectrum of traf7 syndrome: report of eleven new cases and literature review. MedRxiv, Dec 2023. URL: https://doi.org/10.1101/2023.12.13.23299272, doi:10.1101/2023.12.13.23299272. This article has 0 citations.

7. (mishragorur2023pleiotropicroleof pages 3-4): Ketu Mishra-Gorur, Tanyeri Barak, Leon D. Kaulen, Octavian Henegariu, Sheng Chih Jin, Stephanie Marie Aguilera, Ezgi Yalbir, Gizem Goles, Sayoko Nishimura, Danielle Miyagishima, Lydia Djenoune, Selin Altinok, Devendra K. Rai, Stephen Viviano, Andrew Prendergast, Cynthia Zerillo, Kent Ozcan, Burcin Baran, Leman Sencar, Nukte Goc, Yanki Yarman, A. Gulhan Ercan-Sencicek, Kaya Bilguvar, Richard P. Lifton, Jennifer Moliterno, Angeliki Louvi, Shiaulou Yuan, Engin Deniz, Martina Brueckner, and Murat Gunel. Pleiotropic role of traf7 in skull-base meningiomas and congenital heart disease. Proceedings of the National Academy of Sciences of the United States of America, Apr 2023. URL: https://doi.org/10.1073/pnas.2214997120, doi:10.1073/pnas.2214997120. This article has 20 citations and is from a highest quality peer-reviewed journal.

8. (palmamilla2023expandingthephenotypic pages 3-5): Carmen Palma-Milla, Aina Prat-Planas, Emma Soengas-Gonda, Mónica Centeno-Pla, Jaime Sánchez-Pozo, Irene Lazaro-Rodriguez, Juan F. Quesada-Espinosa, Ana Arteche-Lopez, Jonathan Olival, Marta Pacio-Miguez, María Palomares-Bralo, Fernando Santos-Simarro, Ramón Cancho-Candela, María Vázquez-López, Veronica Seidel, Antonio F Martinez-Monseny, Didac Casas-Alba, Daniel Grinberg, Susanna Balcells, Mercedes Serrano, Raquel Rabionet, Miguel A. Martin, and Roser Urreizti. Expanding the phenotypic spectrum of traf7 syndrome: report of eleven new cases and literature review. MedRxiv, Dec 2023. URL: https://doi.org/10.1101/2023.12.13.23299272, doi:10.1101/2023.12.13.23299272. This article has 0 citations.

9. (palmamilla2023expandingthephenotypic pages 5-8): Carmen Palma-Milla, Aina Prat-Planas, Emma Soengas-Gonda, Mónica Centeno-Pla, Jaime Sánchez-Pozo, Irene Lazaro-Rodriguez, Juan F. Quesada-Espinosa, Ana Arteche-Lopez, Jonathan Olival, Marta Pacio-Miguez, María Palomares-Bralo, Fernando Santos-Simarro, Ramón Cancho-Candela, María Vázquez-López, Veronica Seidel, Antonio F Martinez-Monseny, Didac Casas-Alba, Daniel Grinberg, Susanna Balcells, Mercedes Serrano, Raquel Rabionet, Miguel A. Martin, and Roser Urreizti. Expanding the phenotypic spectrum of traf7 syndrome: report of eleven new cases and literature review. MedRxiv, Dec 2023. URL: https://doi.org/10.1101/2023.12.13.23299272, doi:10.1101/2023.12.13.23299272. This article has 0 citations.

10. (palmamilla2023expandingthephenotypic pages 10-13): Carmen Palma-Milla, Aina Prat-Planas, Emma Soengas-Gonda, Mónica Centeno-Pla, Jaime Sánchez-Pozo, Irene Lazaro-Rodriguez, Juan F. Quesada-Espinosa, Ana Arteche-Lopez, Jonathan Olival, Marta Pacio-Miguez, María Palomares-Bralo, Fernando Santos-Simarro, Ramón Cancho-Candela, María Vázquez-López, Veronica Seidel, Antonio F Martinez-Monseny, Didac Casas-Alba, Daniel Grinberg, Susanna Balcells, Mercedes Serrano, Raquel Rabionet, Miguel A. Martin, and Roser Urreizti. Expanding the phenotypic spectrum of traf7 syndrome: report of eleven new cases and literature review. MedRxiv, Dec 2023. URL: https://doi.org/10.1101/2023.12.13.23299272, doi:10.1101/2023.12.13.23299272. This article has 0 citations.

11. (mishragorur2023pleiotropicroleof pages 8-8): Ketu Mishra-Gorur, Tanyeri Barak, Leon D. Kaulen, Octavian Henegariu, Sheng Chih Jin, Stephanie Marie Aguilera, Ezgi Yalbir, Gizem Goles, Sayoko Nishimura, Danielle Miyagishima, Lydia Djenoune, Selin Altinok, Devendra K. Rai, Stephen Viviano, Andrew Prendergast, Cynthia Zerillo, Kent Ozcan, Burcin Baran, Leman Sencar, Nukte Goc, Yanki Yarman, A. Gulhan Ercan-Sencicek, Kaya Bilguvar, Richard P. Lifton, Jennifer Moliterno, Angeliki Louvi, Shiaulou Yuan, Engin Deniz, Martina Brueckner, and Murat Gunel. Pleiotropic role of traf7 in skull-base meningiomas and congenital heart disease. Proceedings of the National Academy of Sciences of the United States of America, Apr 2023. URL: https://doi.org/10.1073/pnas.2214997120, doi:10.1073/pnas.2214997120. This article has 20 citations and is from a highest quality peer-reviewed journal.

12. (mishragorur2023pleiotropicroleof pages 8-9): Ketu Mishra-Gorur, Tanyeri Barak, Leon D. Kaulen, Octavian Henegariu, Sheng Chih Jin, Stephanie Marie Aguilera, Ezgi Yalbir, Gizem Goles, Sayoko Nishimura, Danielle Miyagishima, Lydia Djenoune, Selin Altinok, Devendra K. Rai, Stephen Viviano, Andrew Prendergast, Cynthia Zerillo, Kent Ozcan, Burcin Baran, Leman Sencar, Nukte Goc, Yanki Yarman, A. Gulhan Ercan-Sencicek, Kaya Bilguvar, Richard P. Lifton, Jennifer Moliterno, Angeliki Louvi, Shiaulou Yuan, Engin Deniz, Martina Brueckner, and Murat Gunel. Pleiotropic role of traf7 in skull-base meningiomas and congenital heart disease. Proceedings of the National Academy of Sciences of the United States of America, Apr 2023. URL: https://doi.org/10.1073/pnas.2214997120, doi:10.1073/pnas.2214997120. This article has 20 citations and is from a highest quality peer-reviewed journal.

13. (mishragorur2023pleiotropicroleof pages 6-7): Ketu Mishra-Gorur, Tanyeri Barak, Leon D. Kaulen, Octavian Henegariu, Sheng Chih Jin, Stephanie Marie Aguilera, Ezgi Yalbir, Gizem Goles, Sayoko Nishimura, Danielle Miyagishima, Lydia Djenoune, Selin Altinok, Devendra K. Rai, Stephen Viviano, Andrew Prendergast, Cynthia Zerillo, Kent Ozcan, Burcin Baran, Leman Sencar, Nukte Goc, Yanki Yarman, A. Gulhan Ercan-Sencicek, Kaya Bilguvar, Richard P. Lifton, Jennifer Moliterno, Angeliki Louvi, Shiaulou Yuan, Engin Deniz, Martina Brueckner, and Murat Gunel. Pleiotropic role of traf7 in skull-base meningiomas and congenital heart disease. Proceedings of the National Academy of Sciences of the United States of America, Apr 2023. URL: https://doi.org/10.1073/pnas.2214997120, doi:10.1073/pnas.2214997120. This article has 20 citations and is from a highest quality peer-reviewed journal.

14. (tsitsikov2023traf7isan pages 1-2): Erdyni N. Tsitsikov, Khanh P. Phan, Yufeng Liu, Alla V. Tsytsykova, Mike Kinter, Lauren Selland, Lori Garman, Courtney Griffin, and Ian F. Dunn. Traf7 is an essential regulator of blood vessel integrity during mouse embryonic and neonatal development. Aug 2023. URL: https://doi.org/10.1016/j.isci.2023.107474, doi:10.1016/j.isci.2023.107474. This article has 15 citations and is from a peer-reviewed journal.

15. (tsitsikov2023traf7isan pages 7-9): Erdyni N. Tsitsikov, Khanh P. Phan, Yufeng Liu, Alla V. Tsytsykova, Mike Kinter, Lauren Selland, Lori Garman, Courtney Griffin, and Ian F. Dunn. Traf7 is an essential regulator of blood vessel integrity during mouse embryonic and neonatal development. Aug 2023. URL: https://doi.org/10.1016/j.isci.2023.107474, doi:10.1016/j.isci.2023.107474. This article has 15 citations and is from a peer-reviewed journal.

16. (kim2024thefirstkorean pages 5-6): Kyung Hee Kim, Ji Yoon Han, Joonhong Park, and Jung Sun Cho. The first korean case with cardiac, facial, and digital anomalies with developmental delay caused by de novo traf7 p.arg655gln variant. International Journal of Molecular Sciences, 25:3701, Mar 2024. URL: https://doi.org/10.3390/ijms25073701, doi:10.3390/ijms25073701. This article has 1 citations.

17. (castillavallmanya2020phenotypicspectrumand pages 9-10): Laura Castilla-Vallmanya, Kaja K. Selmer, Clémantine Dimartino, Raquel Rabionet, Bernardo Blanco-Sánchez, Sandra Yang, Margot R.F. Reijnders, Antonie J. van Essen, Myriam Oufadem, Magnus D. Vigeland, Barbro Stadheim, Gunnar Houge, Helen Cox, Helen Kingston, Jill Clayton-Smith, Jeffrey W. Innis, Maria Iascone, Anna Cereda, Sara Gabbiadini, Wendy K. Chung, Victoria Sanders, Joel Charrow, Emily Bryant, John Millichap, Antonio Vitobello, Christel Thauvin, Frederic Tran Mau-Them, Laurence Faivre, Gaetan Lesca, Audrey Labalme, Christelle Rougeot, Nicolas Chatron, Damien Sanlaville, Katherine M. Christensen, Amelia Kirby, Raymond Lewandowski, Rachel Gannaway, Maha Aly, Anna Lehman, Lorne Clarke, Luitgard Graul-Neumann, Christiane Zweier, Davor Lessel, Bernarda Lozic, Ingvild Aukrust, Ryan Peretz, Robert Stratton, Thomas Smol, Anne Dieux-Coëslier, Joanna Meira, Elizabeth Wohler, Nara Sobreira, Erin M. Beaver, Jennifer Heeley, Lauren C. Briere, Frances A. High, David A. Sweetser, Melissa A. Walker, Catherine E. Keegan, Parul Jayakar, Marwan Shinawi, Wilhelmina S. Kerstjens-Frederikse, Dawn L. Earl, Victoria M. Siu, Emma Reesor, Tony Yao, Robert A. Hegele, Olena M. Vaske, Shannon Rego, Kevin A. Shapiro, Brian Wong, Michael J. Gambello, Marie McDonald, Danielle Karlowicz, Roberto Colombo, Alessandro Serretti, Lynn Pais, Anne O’Donnell-Luria, Alison Wray, Simon Sadedin, Belinda Chong, Tiong Y. Tan, John Christodoulou, Susan M. White, Anne Slavotinek, Deborah Barbouth, Dayna Morel Swols, Mélanie Parisot, Christine Bole-Feysot, Patrick Nitschké, Véronique Pingault, Arnold Munnich, Megan T. Cho, Valérie Cormier-Daire, Susanna Balcells, Stanislas Lyonnet, Daniel Grinberg, Jeanne Amiel, Roser Urreizti, and Christopher T. Gordon. Phenotypic spectrum and transcriptomic profile associated with germline variants in traf7. Jul 2020. URL: https://doi.org/10.1038/s41436-020-0792-7, doi:10.1038/s41436-020-0792-7. This article has 38 citations and is from a highest quality peer-reviewed journal.

18. (tsitsikov2023traf7isan pages 4-7): Erdyni N. Tsitsikov, Khanh P. Phan, Yufeng Liu, Alla V. Tsytsykova, Mike Kinter, Lauren Selland, Lori Garman, Courtney Griffin, and Ian F. Dunn. Traf7 is an essential regulator of blood vessel integrity during mouse embryonic and neonatal development. Aug 2023. URL: https://doi.org/10.1016/j.isci.2023.107474, doi:10.1016/j.isci.2023.107474. This article has 15 citations and is from a peer-reviewed journal.

19. (castillavallmanya2020phenotypicspectrumand pages 1-2): Laura Castilla-Vallmanya, Kaja K. Selmer, Clémantine Dimartino, Raquel Rabionet, Bernardo Blanco-Sánchez, Sandra Yang, Margot R.F. Reijnders, Antonie J. van Essen, Myriam Oufadem, Magnus D. Vigeland, Barbro Stadheim, Gunnar Houge, Helen Cox, Helen Kingston, Jill Clayton-Smith, Jeffrey W. Innis, Maria Iascone, Anna Cereda, Sara Gabbiadini, Wendy K. Chung, Victoria Sanders, Joel Charrow, Emily Bryant, John Millichap, Antonio Vitobello, Christel Thauvin, Frederic Tran Mau-Them, Laurence Faivre, Gaetan Lesca, Audrey Labalme, Christelle Rougeot, Nicolas Chatron, Damien Sanlaville, Katherine M. Christensen, Amelia Kirby, Raymond Lewandowski, Rachel Gannaway, Maha Aly, Anna Lehman, Lorne Clarke, Luitgard Graul-Neumann, Christiane Zweier, Davor Lessel, Bernarda Lozic, Ingvild Aukrust, Ryan Peretz, Robert Stratton, Thomas Smol, Anne Dieux-Coëslier, Joanna Meira, Elizabeth Wohler, Nara Sobreira, Erin M. Beaver, Jennifer Heeley, Lauren C. Briere, Frances A. High, David A. Sweetser, Melissa A. Walker, Catherine E. Keegan, Parul Jayakar, Marwan Shinawi, Wilhelmina S. Kerstjens-Frederikse, Dawn L. Earl, Victoria M. Siu, Emma Reesor, Tony Yao, Robert A. Hegele, Olena M. Vaske, Shannon Rego, Kevin A. Shapiro, Brian Wong, Michael J. Gambello, Marie McDonald, Danielle Karlowicz, Roberto Colombo, Alessandro Serretti, Lynn Pais, Anne O’Donnell-Luria, Alison Wray, Simon Sadedin, Belinda Chong, Tiong Y. Tan, John Christodoulou, Susan M. White, Anne Slavotinek, Deborah Barbouth, Dayna Morel Swols, Mélanie Parisot, Christine Bole-Feysot, Patrick Nitschké, Véronique Pingault, Arnold Munnich, Megan T. Cho, Valérie Cormier-Daire, Susanna Balcells, Stanislas Lyonnet, Daniel Grinberg, Jeanne Amiel, Roser Urreizti, and Christopher T. Gordon. Phenotypic spectrum and transcriptomic profile associated with germline variants in traf7. Jul 2020. URL: https://doi.org/10.1038/s41436-020-0792-7, doi:10.1038/s41436-020-0792-7. This article has 38 citations and is from a highest quality peer-reviewed journal.

20. (mishragorur2023pleiotropicroleof pages 9-10): Ketu Mishra-Gorur, Tanyeri Barak, Leon D. Kaulen, Octavian Henegariu, Sheng Chih Jin, Stephanie Marie Aguilera, Ezgi Yalbir, Gizem Goles, Sayoko Nishimura, Danielle Miyagishima, Lydia Djenoune, Selin Altinok, Devendra K. Rai, Stephen Viviano, Andrew Prendergast, Cynthia Zerillo, Kent Ozcan, Burcin Baran, Leman Sencar, Nukte Goc, Yanki Yarman, A. Gulhan Ercan-Sencicek, Kaya Bilguvar, Richard P. Lifton, Jennifer Moliterno, Angeliki Louvi, Shiaulou Yuan, Engin Deniz, Martina Brueckner, and Murat Gunel. Pleiotropic role of traf7 in skull-base meningiomas and congenital heart disease. Proceedings of the National Academy of Sciences of the United States of America, Apr 2023. URL: https://doi.org/10.1073/pnas.2214997120, doi:10.1073/pnas.2214997120. This article has 20 citations and is from a highest quality peer-reviewed journal.

21. (ihuoma2025reviewofthe pages 6-7): Jennifer Ihuoma, Sherwin Tavakol, Sharon Negri, Cade Ballard, Khanh Phan, Albert Orock, Zeke Reyff, Madison Milan, Eva Troyano-Rodriguez, Rakesh Rudraboina, Anna Csiszar, Anthony C. Johnson, Ian F. Dunn, and Stefano Tarantini. Review of the role of traf7 in brain endothelial integrity and cerebrovascular aging. Life, 15(8):1280, Aug 2025. URL: https://doi.org/10.3390/life15081280, doi:10.3390/life15081280. This article has 10 citations.

22. (tsitsikov2023traf7isan pages 2-4): Erdyni N. Tsitsikov, Khanh P. Phan, Yufeng Liu, Alla V. Tsytsykova, Mike Kinter, Lauren Selland, Lori Garman, Courtney Griffin, and Ian F. Dunn. Traf7 is an essential regulator of blood vessel integrity during mouse embryonic and neonatal development. Aug 2023. URL: https://doi.org/10.1016/j.isci.2023.107474, doi:10.1016/j.isci.2023.107474. This article has 15 citations and is from a peer-reviewed journal.

23. (tsitsikov2023traf7isan pages 21-23): Erdyni N. Tsitsikov, Khanh P. Phan, Yufeng Liu, Alla V. Tsytsykova, Mike Kinter, Lauren Selland, Lori Garman, Courtney Griffin, and Ian F. Dunn. Traf7 is an essential regulator of blood vessel integrity during mouse embryonic and neonatal development. Aug 2023. URL: https://doi.org/10.1016/j.isci.2023.107474, doi:10.1016/j.isci.2023.107474. This article has 15 citations and is from a peer-reviewed journal.

24. (ihuoma2025reviewofthe pages 4-6): Jennifer Ihuoma, Sherwin Tavakol, Sharon Negri, Cade Ballard, Khanh Phan, Albert Orock, Zeke Reyff, Madison Milan, Eva Troyano-Rodriguez, Rakesh Rudraboina, Anna Csiszar, Anthony C. Johnson, Ian F. Dunn, and Stefano Tarantini. Review of the role of traf7 in brain endothelial integrity and cerebrovascular aging. Life, 15(8):1280, Aug 2025. URL: https://doi.org/10.3390/life15081280, doi:10.3390/life15081280. This article has 10 citations.

25. (tsitsikov2023traf7isan pages 13-15): Erdyni N. Tsitsikov, Khanh P. Phan, Yufeng Liu, Alla V. Tsytsykova, Mike Kinter, Lauren Selland, Lori Garman, Courtney Griffin, and Ian F. Dunn. Traf7 is an essential regulator of blood vessel integrity during mouse embryonic and neonatal development. Aug 2023. URL: https://doi.org/10.1016/j.isci.2023.107474, doi:10.1016/j.isci.2023.107474. This article has 15 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Cardiac_Facial_And_Digital_Anomalies_With_Developmental_Delay-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 58 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032572` (6 mentions) - the report calls it "if available"; MONDO calls it **cardiac, facial, and digital anomalies with developmental delay**
- `GO:0005929` (1 mention) - the report calls it "GO cellular component:** cilium"; GO calls it **cilium**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0016567` (1 mention) - the report calls it "GO biological process:** protein ubiquitination"; GO calls it **protein ubiquitination**
- `CL:0000333` (1 mention) - the report calls it "Cell Ontology:** neural crest cell"; CL calls it **migratory neural crest cell**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
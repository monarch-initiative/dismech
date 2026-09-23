---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T10:08:18.092363'
end_time: '2026-09-01T10:21:30.910801'
duration_seconds: 792.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth disease type 4C (CMT4C, SH3TC2-related autosomal
    recessive demyelinating neuropathy)
  mondo_id: MONDO:0011113
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
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 9
  validator_version: 0.2.1
term_validation:
  total_terms: 34
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0011113
    reported_labels:
    - if available
    - MONDO
    ontology_label: Charcot-Marie-Tooth disease type 4C
  labels_variant: 1
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
  path: Charcot-Marie-Tooth_Disease_Type_4C-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth disease type 4C (CMT4C, SH3TC2-related autosomal recessive demyelinating neuropathy)
- **MONDO ID:** MONDO:0011113 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease type 4C (CMT4C, SH3TC2-related autosomal recessive demyelinating neuropathy)** covering all of the
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
- **Disease Name:** Charcot-Marie-Tooth disease type 4C (CMT4C, SH3TC2-related autosomal recessive demyelinating neuropathy)
- **MONDO ID:** MONDO:0011113 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease type 4C (CMT4C, SH3TC2-related autosomal recessive demyelinating neuropathy)** covering all of the
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


# Charcot–Marie–Tooth disease type 4C (CMT4C): disease-characteristics research report

## Scope and evidence standard

CMT4C is a rare Mendelian neuropathy, so most quantitative evidence comes from small cohorts, one international natural-history study, and animal or cell models rather than randomized trials. The strongest current clinical dataset is the 2023 Inherited Neuropathy Consortium study of 56 molecularly confirmed patients; the newest therapeutic evidence is preclinical AAV work published in 2023–2024. Database statements below are aggregated disease-level assertions; cohort statistics are patient-level observations aggregated by investigators. No individual EHR data were accessed.

| Evidence/source and date | Evidence type | Sample/model | Key quantitative finding | Exact short abstract quote where actually available | DOI/URL and PMID if known |
|---|---|---|---|---|---|
| Rehbein et al., *Brain* (Mar 2023) (rehbein2023neuropathydueto pages 1-2, rehbein2023neuropathydueto pages 9-10, rehbein2023neuropathydueto pages 2-3) | Human cohort, longitudinal natural history | 56 individuals from 52 families with biallelic **SH3TC2** variants; 28 with longitudinal follow-up | 59% female; median age 27 years (range 2–67); mean CMTES 13; scoliosis 81%; scoliosis surgery 36%; walking difficulty 94%; orthotic aids 59%; wheelchair dependence 21%; CMTES SRM 0.81 and CMTES-R 0.71 over 3 years | “56 individuals (59% female), median age 27 years (range 2-67 years) with homozygous or compound heterozygous variants in SH3TC2 were identified”; “There was a high rate of scoliosis (81%), scoliosis surgery (36%), and walking difficulty (94%) among study participants.” | DOI: 10.1093/brain/awad095; URL: https://doi.org/10.1093/brain/awad095; PMID: not retrieved |
| Ozes et al., *Brain Communications* (Nov 2024) (ozes2024aav1.tmck.nt3genetherapy pages 1-3) | Mouse interventional study | **Sh3tc2−/−** mouse; intramuscular scAAV1.tMCK.NT-3 at 4 weeks; assessed 6 months later | Dose 1×10^11 vg; improved rotarod, grip strength, nerve conduction velocity; improved hypomyelination and NMJ denervation; increased myelinated axons in 3–6 µm range | “NT-3 gene therapy improved functional and electrophysiological outcomes including rotarod, grip strength and nerve conduction velocity.” | DOI: 10.1093/braincomms/fcae394; URL: https://doi.org/10.1093/braincomms/fcae394; PMID: not retrieved |
| Schiza et al., *Brain* (Mar 2019) (schiza2019genereplacementtherapy pages 1-2, schiza2019genereplacementtherapy pages 1-1) | Mouse gene-replacement study plus human disease background | **Sh3tc2−/−** mouse; lentiviral human **SH3TC2** cDNA under **Mpz** promoter, intrathecal injection at 3 weeks | 8 weeks post-injection: improved motor performance, increased motor NCV, improved g-ratios/myelin thickness, fewer demyelinated fibers, improved nodal architecture, reduced blood neurofilament light | No abstract quote available in retrieved context | DOI: 10.1093/brain/awz064; URL: https://doi.org/10.1093/brain/awz064; PMID: not retrieved |
| Piscosquito et al., *J Peripher Nerv Syst* (Sep 2016) (piscosquito2016screeningforsh3tc2 pages 3-4, piscosquito2016screeningforsh3tc2 pages 4-6) | Human cohort, genotype-phenotype study | 12 patients with **SH3TC2** mutations from 43 screened recessive demyelinating CMT cases | Foot deformities/walking difficulties 11/12; scoliosis 11/12 (92%), surgery 4/12; cranial nerve involvement 9/12; hearing loss 7/12; mean onset 7 years; mean duration 33 years; recurrent alleles p.R954* 8/24 and p.R1109* 6/24 | No abstract quote available in retrieved context | DOI: 10.1111/jns.12175; URL: https://doi.org/10.1111/jns.12175; PMID: not retrieved |
| Jerath et al., *Muscle & Nerve* (May 2018) (jerath2018charcot–marie–toothdiseasetype pages 1-3, jerath2018charcot–marie–toothdiseasetype pages 8-10) | Human case series | 5 CMT4C patients with biallelic/private **SH3TC2** variants | All 5 had scoliosis and demyelinating nerve conduction studies; childhood onset; cranial nerve deficits included oculomotor, facial, auditory, and hypoglossal involvement; 3 novel variants reported | No abstract quote available in retrieved context | DOI: 10.1002/mus.25981; URL: https://doi.org/10.1002/mus.25981; PMID: not retrieved |
| Open Targets Genetics/Platform (accessed via context) (OpenTargets Search: Charcot-Marie-Tooth disease type 4C-SH3TC2) | Database / aggregated disease-target evidence | MONDO_0011113 ↔ **SH3TC2** | Disease-target association score 0.8002627934413797; evidence count 5; linked literature includes PMID 14574644, 34193129, 19805030, 20301514 | No abstract quote applicable | URL: https://platform.opentargets.org; MONDO: MONDO_0011113; PMID: literature links include 14574644, 34193129, 19805030, 20301514 |
| Duan et al., *Frontiers in Neurology* (Feb 2021) (piscosquito2016screeningforsh3tc2 pages 3-4, schiza2019genereplacementtherapy pages 1-2) | Human cohort | 465 unrelated Chinese CMT patients, 650 controls; 7 families with **SH3TC2** variants | 12 **SH3TC2** variants identified (8 novel); CMT4C frequency 4.24% among demyelinating/intermediate CMT without PMP22 duplication; R954* present at low frequency in Chinese cohort | “The CMT4C frequency was calculated to be 4.24% in demyelinating or intermediate CMT patients without PMP22 duplication.” | DOI: 10.3389/fneur.2021.598168; URL: https://doi.org/10.3389/fneur.2021.598168; PMID: not retrieved |
| Cipriani et al., *Int J Mol Sci* (Dec 2018) (from retrieved paper context) | Mouse mechanistic/proteomic study | **SH3TC2**-deficient mouse NMJs in gastrocnemius; sciatic nerve proteomics | Increased post-synaptic fragmentation/dispersal; increased AChR gamma subunit expression; altered extracellular matrix proteins; no change in axonal width or axonal inputs | “Together these observations suggest that CMT4C pathology includes a compromised NMJ even in the absence of changes to the innervating axon.” | DOI: 10.3390/ijms19124072; URL: https://doi.org/10.3390/ijms19124072; PMID: not retrieved |
| Arnaud et al., *PNAS* (Oct 2009) (from retrieved paper context) | Mouse mechanistic study | **Sh3tc2** mutant mouse peripheral nerve | Demonstrated requirement for proper myelination and node of Ranvier integrity; model recapitulated neuropathy phenotypes | No abstract quote available in retrieved context | DOI: 10.1073/pnas.0905523106; URL: https://doi.org/10.1073/pnas.0905523106; PMID: not retrieved |
| Stendel et al., *Brain* (Aug 2010) (from retrieved paper context) | In vitro + mouse mechanistic study | Schwann-cell/endosomal recycling studies; **Sh3tc2**-deficient mouse | Linked SH3TC2 to Rab11-positive recycling endosomes and peripheral nerve myelination; established Schwann-cell-specific expression | No abstract quote available in retrieved context | DOI: 10.1093/brain/awq168; URL: https://doi.org/10.1093/brain/awq168; PMID: not retrieved |
| Gouttenoire et al., *Glia* (Jul 2013) (from retrieved paper context) | Mouse mechanistic study | **Sh3tc2**-deficient mouse Schwann cells | Showed altered neuregulin-1/ErbB signaling in deficiency state, supporting disturbed axon-Schwann signaling in hypomyelination | No abstract quote available in retrieved context | DOI: 10.1002/glia.22493; URL: https://doi.org/10.1002/glia.22493; PMID: not retrieved |
| Vijay et al., *BBA Mol Basis Dis* (Jul 2016) (from retrieved paper context) | In vitro / expression-localization study | Schwann-cell expression and trafficking analyses | Established exclusive Schwann-cell expression and linked SH3TC2/Rab11 to integrin-α6 trafficking and myelin maintenance | No abstract quote available in retrieved context | DOI: 10.1016/j.bbadis.2016.04.003; URL: https://doi.org/10.1016/j.bbadis.2016.04.003; PMID: not retrieved |


*Table: This table summarizes the highest-yield evidence for SH3TC2-related Charcot-Marie-Tooth disease type 4C across human cohorts, mouse models, mechanistic studies, and database resources. It highlights quantitative findings, exact abstract quotations when actually available in retrieved context, and traceable source links for rapid knowledge-base curation.*

## 1. Disease information

### Definition

Charcot–Marie–Tooth disease type 4C is an **autosomal-recessive, usually childhood-onset sensorimotor demyelinating polyneuropathy** caused by biallelic pathogenic variants in **SH3TC2**. It is distinguished clinically by early or disproportionate scoliosis, distal weakness and wasting, foot deformity, sensory impairment, areflexia, very slow nerve conduction, and variably cranial-nerve involvement. Phenotypic severity ranges from relatively mild adult ambulatory disease to childhood-onset disability requiring spinal surgery, orthoses, or a wheelchair. The 2023 cohort aptly states: “CMT4C is typically a sensorimotor demyelinating polyneuropathy, marked by early onset spinal deformities, but its clinical characteristics and severity are quite variable.” (rehbein2023neuropathydueto pages 1-2)

### Identifiers and synonyms

- **MONDO:** [MONDO:0011113](https://monarchinitiative.org/disease/MONDO:0011113).
- **OMIM phenotype:** **601596**, Charcot-Marie-Tooth disease, type 4C; **SH3TC2 gene:** OMIM **608206**. These should be verified against the live OMIM record before automated ingestion because OMIM content is versioned.
- **Orphanet:** commonly represented as **ORPHA:99955**; verify against the current Orphanet nomenclature release.
- **ICD-10-CM:** no subtype-specific code; generally **G60.0, hereditary motor and sensory neuropathy**.
- **ICD-11:** classify under hereditary motor and sensory neuropathy/Charcot–Marie–Tooth disease; a stable CMT4C-specific leaf code was not established in the retrieved evidence.
- **MeSH:** Charcot-Marie-Tooth Disease; no separately validated CMT4C MeSH descriptor was retrieved.
- **Synonyms:** CMT4C; SH3TC2-related neuropathy; SH3TC2-related autosomal-recessive demyelinating neuropathy; autosomal-recessive Charcot–Marie–Tooth disease type 4C; hereditary motor and sensory neuropathy type 4C; formerly KIAA1985-related neuropathy.

Open Targets maps MONDO_0011113 specifically to **SH3TC2/ENSG00000169247**, with five evidence records and an association score of 0.8003; linked literature includes PMIDs **14574644, 19805030, 20301514, and 34193129**. This is an aggregated disease–target resource, not a prevalence estimate. (OpenTargets Search: Charcot-Marie-Tooth disease type 4C-SH3TC2)

## 2. Etiology, risk, and protective factors

### Primary cause

The necessary initiating lesion is usually **biallelic germline loss of SH3TC2 function**, either homozygous or compound heterozygous. Pathogenic classes include nonsense, frameshift, canonical splice-site, and functionally damaging missense variants. Premature truncation generally abolishes functional protein; missense alleles may mislocalize SH3TC2 or disrupt protein interactions/endosomal architecture. Examples include recurrent **p.Arg954Ter (R954\*)**, **p.Arg1109Ter (R1109\*)**, p.Tyr680Cys, p.Asn881Ser, and splice variants. (schiza2019genereplacementtherapy pages 2-2, jerath2018charcot–marie–toothdiseasetype pages 8-10, piscosquito2016screeningforsh3tc2 pages 3-4)

### Genetic risk and modifiers

- A child of two heterozygous carriers has a **25% recurrence risk**, 50% carrier probability, and 25% probability of inheriting neither familial allele per pregnancy.
- Consanguinity, endogamy, and founder alleles increase the probability of biallelic inheritance. R1109\* is a recognized Roma/Gypsy founder allele; R954\* is recurrent in European populations and also occurs in Asia. In an Italian series, R954\* accounted for 8/24 and R1109\* for 6/24 disease alleles. (piscosquito2016screeningforsh3tc2 pages 3-4, piscosquito2016screeningforsh3tc2 pages 4-6)
- Protein-truncating versus non-truncating genotype did not significantly separate mean clinical examination scores in the 2023 cohort. However, ulnar CMAP, radial SNAP, and scoliosis prevalence differed, suggesting—but not proving—a milder phenotype when at least one non-truncating allele remains. (rehbein2023neuropathydueto pages 1-2)
- Marked intrafamilial variability implies additional genetic, epigenetic, stochastic, or environmental modifiers, but no reproducible human modifier gene is clinically validated. (jerath2018charcot–marie–toothdiseasetype pages 1-3, jerath2018charcot–marie–toothdiseasetype pages 8-10)

### Environmental, lifestyle, infectious, and protective factors

No toxin, infection, diet, smoking pattern, occupation, radiation exposure, or lifestyle is known to cause CMT4C. No validated protective allele or environmental factor prevents penetrance after biallelic pathogenic variants. General measures—safe aerobic activity, preservation of joint range, fall prevention, weight management, and avoidance of neurotoxic exposure—may reduce secondary disability but are **tertiary management**, not disease prevention. Gene–environment interaction is plausible for functional reserve and acquired neuropathic insults, but CMT4C-specific quantitative evidence is lacking.

## 3. Phenotypes

The best contemporary estimates are from 56 patients (median age 27, range 2–67; 59% female). Mean CMT Examination Score was 13, indicating moderate severity; 94% had walking difficulty, 59% used orthotic aids, and 21% were wheelchair-dependent. Scoliosis affected 81%, 36% had spinal surgery, and hearing loss affected 36%. (rehbein2023neuropathydueto pages 1-2, rehbein2023neuropathydueto pages 2-3)

| Phenotype | Characteristics/frequency | Suggested HPO term |
|---|---|---|
| Distal lower-limb weakness and wasting | Usually childhood onset; progressive; often precedes hand involvement; major determinant of gait impairment | Distal muscle weakness **HP:0002460**; muscular atrophy **HP:0003202** |
| Walking difficulty/delayed walking | 94% in the 2023 cohort; orthoses 59%, wheelchair 21%; chronic progression | Abnormal gait **HP:0001288**; delayed walking **HP:0002060** |
| Sensory loss, sensory ataxia, impaired proprioception | Length-dependent; sensory nerves may be more affected than motor nerves; four of 12 Italian patients lost independent ambulation mainly because of sensory ataxia | Peripheral sensory neuropathy **HP:0007067**; sensory ataxia **HP:0002066** |
| Areflexia/hyporeflexia | Common, progressive peripheral neuropathy sign | Areflexia **HP:0001284** |
| Pes cavus/other foot deformity | 11/12 had foot deformity or walking difficulty in one series; develops through childhood/adolescence and may require surgery | Pes cavus **HP:0001761**; foot deformity **HP:0001760** |
| Scoliosis/kyphoscoliosis | Hallmark but not obligatory; 81% in the largest cohort, 92% in a 12-patient Italian series; often begins in the first two decades; surgery 36% in the 2023 cohort | Scoliosis **HP:0002650**; kyphoscoliosis **HP:0002751** |
| Demyelinating neuropathy | Motor conduction velocity commonly <38 m/s; historical mean approximately 22.6 m/s; secondary axonal loss increases with duration | Demyelinating peripheral neuropathy **HP:0007108** |
| Hearing impairment | 36% in the largest cohort; 7/12 in an Italian series | Sensorineural hearing impairment **HP:0000407** |
| Cranial neuropathy | 9/12 in one series; reported oculomotor, facial, auditory and hypoglossal deficits, slow pupils and tongue fasciculation | Cranial nerve abnormality **HP:0001291**; facial weakness **HP:0007209** |
| Vestibular dysfunction/imbalance | Variable; may compound proprioceptive loss and cause severe imbalance | Bilateral vestibular areflexia **HP:0012105** |
| Rare cerebellar-appearing phenotype | Nystagmus, dysarthria/dysmetria and cerebellar atrophy are exceptional; consider alternative or dual diagnoses | Cerebellar atrophy **HP:0001272**; nystagmus **HP:0000639** |

In the 12-patient Italian series, mean onset was seven years, all began before 15, 11/12 had scoliosis, 9/12 cranial involvement, 7/12 hearing loss, and four lost independent walking. Sural biopsy showed myelinated-fiber loss, thin myelin, onion bulbs and de-/remyelination. (piscosquito2016screeningforsh3tc2 pages 3-4, piscosquito2016screeningforsh3tc2 pages 4-6)

**Quality of life:** no CMT4C-specific EQ-5D or SF-36 population norm was retrieved. Nevertheless, walking difficulty, orthotic dependence, wheelchair use, sensory ataxia, hearing impairment, and repeated orthopedic surgery indicate substantial effects on mobility, education/work, self-care, participation and fatigue. CMTES/CMTNS and CMTPedS are clinician-rated disease measures, not full health-related-QOL instruments. (rehbein2023neuropathydueto pages 2-3, rehbein2023neuropathydueto pages 1-2)

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** SH3TC2, SH3 domain and tetratricopeptide repeats 2; chromosome **5q32**; Ensembl **ENSG00000169247**.
- **Protein:** approximately 1,288 amino acids, containing SH3 and tetratricopeptide-repeat domains; functions as a Rab11-associated trafficking protein in myelinating Schwann cells. (schiza2019genereplacementtherapy pages 2-2)
- Suggested annotations: **HGNC:29427** should be checked against the current HGNC release; UniProt and transcript accession should be locked to the laboratory’s reporting transcript before variant ingestion.

### Variant interpretation

Pathogenic/likely pathogenic variants should satisfy ACMG/AMP criteria in the context of a recessive phenotype, including rarity in population databases, trans configuration, predicted loss of function where applicable, segregation, and phenotype specificity. A single heterozygous pathogenic variant is insufficient for molecular confirmation; search for a second SNV/indel, exon-level deletion/duplication, deep-intronic variant, or other structural lesion. Germline origin is expected; somatic SH3TC2 mutation is not the disease mechanism.

The 2023 cohort contained **34 unique variants, 14 previously unpublished**, illustrating extensive allelic heterogeneity. In a Chinese study, 12 variants in seven families included eight novel variants; seven were considered likely pathogenic and one, p.Ser221Pro, remained a VUS. The CMT4C frequency was 4.24% among demyelinating/intermediate CMT cases lacking PMP22 duplication. (rehbein2023neuropathydueto pages 1-2, piscosquito2016screeningforsh3tc2 pages 3-4)

Population allele frequencies must be retrieved per exact HGVS allele and ancestry from the current gnomAD release; no universal frequency applies. Disease-causing alleles are individually rare, although founder variants can be locally enriched. No consistent epigenetic signature or disease-causing aneuploidy, translocation, or inversion is established. Exonic or larger SH3TC2 copy-number loss remains technically possible and should be assessed when sequencing finds only one allele.

## 5. Environmental information

CMT4C is not infectious, transmissible, occupational, nutritional, or toxic in origin. Environmental factors primarily influence complications: inactivity and contracture can worsen mobility; poorly fitted footwear can promote pressure injury in an insensate foot; neurotoxic chemotherapy or other acquired neuropathy may reduce residual nerve function. Evidence for CMT4C-specific smoking, alcohol, diet, pollution, microbiome, or infectious interactions is absent.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic SH3TC2 variants lead to** absent, reduced, mislocalized, or dysfunctional SH3TC2 in myelinating Schwann cells.  
2. **SH3TC2 dysfunction leads to** impaired Rab11-positive recycling-endosome trafficking and altered delivery/recycling of Schwann-cell surface cargo; integrin-α6 trafficking is implicated, and some receptor-level details remain inferred from cell and mouse studies. (schiza2019genereplacementtherapy pages 2-2, jerath2018charcot–marie–toothdiseasetype pages 8-10)  
3. **Abnormal membrane trafficking leads to** dysregulated axon–Schwann-cell signaling, including altered neuregulin-1/ERBB2 signaling and impaired sensing of axonal caliber. (schiza2019genereplacementtherapy pages 2-2)  
4. **Defective signaling and membrane organization lead to** inadequate myelin maintenance/hypomyelination, segmental de-/remyelination, and disrupted node-of-Ranvier architecture. (schiza2019genereplacementtherapy pages 1-2, rehbein2023neuropathydueto pages 9-10)  
5. **Chronic demyelination leads to** markedly slowed conduction and conduction failure; over time it also **results in** secondary axonal degeneration and reduced CMAP/SNAP amplitudes. (schiza2019genereplacementtherapy pages 1-2, piscosquito2016screeningforsh3tc2 pages 4-6)  
6. **Motor and sensory axon dysfunction leads to** distal weakness, wasting, areflexia, sensory loss, proprioceptive ataxia and gait impairment.  
7. **Chronic neuromuscular imbalance during growth leads to** pes cavus, contractures and scoliosis; the precise link from peripheral neuropathy to severe spinal deformity is clinically strong but mechanistically incompletely resolved.  
8. **Branch:** involvement of auditory, vestibular or other cranial nerves **results in** hearing loss, imbalance and occasional facial/ocular/bulbar signs.  
9. **Branch demonstrated in mice:** altered extracellular-matrix/NMJ organization **leads to** postsynaptic fragmentation and denervation-like NMJ abnormalities, potentially adding to weakness; its quantitative contribution in humans remains unproven.

### Cellular and molecular detail

SH3TC2 is concentrated at the plasma membrane and perinuclear recycling compartment and associates with Rab11. Missense alleles can impair recycling-endosome condensation or protein interactions even when targeting appears preserved. SH3TC2 deficiency perturbs NRG1/ERBB signaling, providing a mechanistic connection between axonal caliber cues and Schwann-cell myelin thickness. (schiza2019genereplacementtherapy pages 1-1, schiza2019genereplacementtherapy pages 2-2, jerath2018charcot–marie–toothdiseasetype pages 8-10)

Nerve pathology includes hypomyelination, thinly myelinated fibers, segmental de-/remyelination, myelinated-fiber loss, onion bulbs, excessive basement membrane and unusual Schwann-cell cytoplasmic extensions. Sh3tc2-null nerves exhibit disrupted nodes/paranodes. (schiza2019genereplacementtherapy pages 1-2, piscosquito2016screeningforsh3tc2 pages 4-6)

Suggested ontology annotations:

- **Processes:** endosomal recycling (GO:0032456); receptor recycling (GO:0001881); peripheral nervous system myelination (GO:0022011); axon ensheathment (GO:0008366); regulation of myelination; node-of-Ranvier organization; Schwann-cell differentiation; neuromuscular-junction organization.
- **Cell types:** myelinating Schwann cell (**CL:0002573**, verify release), peripheral sensory neuron, spinal motor neuron, skeletal-muscle fiber.
- **Compartments:** recycling endosome (**GO:0055037**); endosome; trans-Golgi network; plasma membrane; myelin sheath (**GO:0043209**); node of Ranvier (**GO:0033268**); neuromuscular junction.

No validated CMT4C-specific human metabolomic, lipidomic, methylomic, single-cell, spatial-transcriptomic, or multi-omic diagnostic signature was retrieved. Sciatic-nerve proteomics in knockout mice identified altered extracellular-matrix proteins associated with NMJ integrity, but this is exploratory model evidence.

## 7. Anatomical structures affected

The primary system is the **peripheral nervous system**, especially long motor and sensory nerves of the distal limbs. Myelinating Schwann cells are the initiating cellular compartment; axons are secondarily injured. Roots and cranial nerves may also be involved. Skeletal muscle undergoes neurogenic denervation and atrophy, while feet and spine develop secondary orthopedic deformity. Laterality is generally **bilateral and length-dependent**, although severity can be asymmetric.

Suggested anatomical terms include peripheral nerve (**UBERON:0001021**), sciatic nerve (**UBERON:0001322**), spinal nerve root, sural nerve, skeletal muscle (**UBERON:0001134**), foot (**UBERON:0002387**), and vertebral column (**UBERON:0001130**). Subcellular loci are Rab11-positive recycling endosomes, Schwann-cell plasma membrane, compact/noncompact myelin, and nodal/paranodal regions.

## 8. Temporal development

Onset is usually insidious in the **first decade**, sometimes first recognized through delayed walking, foot deformity, gait difficulty, or scoliosis. Later onset occurs and absence of scoliosis or cranial involvement does not exclude SH3TC2 disease. Progression is chronic, lifelong, and generally slow but variable. (schiza2019genereplacementtherapy pages 1-2, piscosquito2016screeningforsh3tc2 pages 3-4)

In the prospective cohort, significant worsening in CMTES and CMTES-R became detectable from three years and continued through six years; three-year standardized response means were 0.81 and 0.71, respectively. These data support multi-year trials or more sensitive biomarkers. (rehbein2023neuropathydueto pages 1-2, rehbein2023neuropathydueto pages 9-10)

Practical stages are not formally standardized: (1) childhood gait/spinal onset; (2) progressive distal weakness, sensory loss and deformity; (3) orthotic or surgical dependence; and (4) advanced ambulatory limitation or wheelchair use. There is no spontaneous remission. Childhood growth is likely a critical window for preventing fixed scoliosis and contracture, while preclinical gene-replacement results suggest early treatment may preserve myelin and axons; neither proposition has yet been tested in a human CMT4C intervention trial.

## 9. Inheritance and population

Inheritance is autosomal recessive with variable expressivity. Penetrance for convincingly pathogenic biallelic genotypes appears high, but age dependence and mild adult presentations prevent a defensible universal percentage. Anticipation is not expected; repeat expansion is not the mechanism. Germline mosaicism is theoretically possible but not a recognized common contributor.

No reliable population-wide incidence or prevalence estimate for CMT4C was found. It represents approximately 18% of autosomal-recessive CMT in some clinical series and nearly half of molecularly defined CMT4 in selected cohorts, but referral, ethnicity and consanguinity strongly bias these figures. Overall CMT prevalence—often quoted near 1:2,500—must not be assigned to CMT4C. (schiza2019genereplacementtherapy pages 1-2, jerath2018charcot–marie–toothdiseasetype pages 1-3)

Regional enrichment occurs around the Mediterranean and in founder populations. In the Chinese cohort, CMT4C comprised **4.24%** of demyelinating/intermediate CMT after excluding PMP22 duplication. The 2023 international cohort’s 59% female proportion is compatible with no sex-linked risk; there is no established biological sex bias. (rehbein2023neuropathydueto pages 1-2, piscosquito2016screeningforsh3tc2 pages 3-4)

Carrier frequency is ancestry- and allele-specific and should be calculated from current gnomAD data rather than inferred from patient cohorts.

## 10. Diagnostics

### Clinical and physiological diagnosis

Suspect CMT4C in childhood or adult patients with a chronic length-dependent sensorimotor neuropathy, especially when scoliosis is early/severe, inheritance appears recessive, or hearing/cranial involvement accompanies foot deformity. Examination should document strength, wasting, reflexes, sensation, balance, feet and spine; CMTES/CMTNS or CMTPedS facilitates longitudinal measurement.

Nerve-conduction studies usually demonstrate a diffuse demyelinating or occasionally intermediate sensorimotor neuropathy, commonly with upper-limb motor conduction velocity below 38 m/s and secondary amplitude loss. One review of CMT4C data reported mean MNCV around 22.6 m/s. EMG can demonstrate chronic neurogenic change. (schiza2019genereplacementtherapy pages 1-2, piscosquito2016screeningforsh3tc2 pages 3-4)

Standing spinal radiographs quantify scoliosis; foot radiography is used for surgical planning. Audiology is indicated if symptoms or cranial involvement are present. Pulmonary function or sleep evaluation is symptom-driven or appropriate with severe scoliosis/bulbar signs, although CMT4C-specific surveillance intervals are not evidence-based. MRI is not diagnostic but can investigate atypical central signs or alternative diagnoses. Nerve ultrasound was reported as supportive in a 2024 case, but it is not molecular confirmation.

Nerve biopsy is usually unnecessary after genetic confirmation. If performed in an unresolved case, it may show marked fiber loss, thin myelin, onion bulbs, de-/remyelination, basement-membrane proliferation and Schwann-cell extensions. (piscosquito2016screeningforsh3tc2 pages 4-6, schiza2019genereplacementtherapy pages 1-2)

### Genetic workflow

1. Exclude the common **PMP22 duplication** where phenotype and ancestry justify it.
2. Use a comprehensive inherited-neuropathy panel including **SH3TC2**, with SNV/indel and exon-level CNV detection.
3. Use exome or genome sequencing for atypical or panel-negative disease; genome sequencing offers better structural and noncoding coverage.
4. Confirm candidate variants by an orthogonal method where required, phase the two alleles in relatives, apply ACMG/AMP criteria, and test segregation.
5. If only one SH3TC2 pathogenic allele is found, pursue CNV, coverage-gap, deep-intronic/structural, and alternative-gene analysis rather than diagnosing recessive CMT4C.

The 2023 cohort accepted diagnoses established by single-gene testing, panels or exome sequencing. A prior Italian workflow combined exclusion of PMP22 duplication/GJB1/MPZ with 54–94-gene NGS panels and Sanger confirmation. (rehbein2023neuropathydueto pages 2-3, piscosquito2016screeningforsh3tc2 pages 3-4)

CMA, karyotyping, FISH, mitochondrial testing and repeat-expansion testing are not first-line tests for isolated classic CMT4C, but may be appropriate for a syndromic or unresolved phenotype. RNA sequencing may resolve splice variants in research or specialized diagnostics; no routine proteomic, metabolomic, epigenomic, or liquid-biopsy diagnostic exists.

### Differential diagnosis

Important alternatives include PMP22-related CMT1A, MPZ/GJB1 demyelinating CMT, other recessive CMT4 genes, hereditary sensory neuropathy, Friedreich ataxia, hereditary spastic paraplegia, distal spinal muscular atrophy, and acquired CIDP. Early uniform slowing, long-standing deformity, recessive pedigree and biallelic SH3TC2 variants favor CMT4C; subacute progression, conduction block, proximal weakness, elevated CSF protein and treatment response favor CIDP. Rare cerebellar-appearing CMT4C can mimic Friedreich ataxia; absent cardiomyopathy/endocrine abnormalities and lack of dentate iron accumulation were distinguishing findings in one small cohort.

## 11. Outcome and prognosis

CMT4C is generally not considered a primary life-shortening disorder, but robust survival and disease-specific mortality rates do not exist. Most morbidity is chronic motor/sensory disability and orthopedic disease. Many patients remain ambulant into middle age, while a minority lose independent ambulation earlier, particularly with severe sensory ataxia, deformity or axonal loss. In the largest cohort, 21% used wheelchairs and 36% had scoliosis surgery. (piscosquito2016screeningforsh3tc2 pages 4-6, rehbein2023neuropathydueto pages 2-3)

Potential complications include falls, fractures, pressure lesions, fixed foot/ankle contracture, severe scoliosis, chronic pain, hearing impairment, and reduced independence. Recovery of established axonal loss is limited; rehabilitation and surgery can improve function or alignment but do not correct SH3TC2 deficiency. Candidate prognostic factors include baseline axonal amplitudes, age/duration, scoliosis, ambulatory status, and possibly truncating genotype, but none is a validated individual prognostic calculator. Blood neurofilament light responded to therapy in mice, not yet as a validated human CMT4C prognostic biomarker. (schiza2019genereplacementtherapy pages 1-1)

## 12. Treatment and current applications

### Current standard care

There is **no approved disease-modifying pharmacotherapy specifically for CMT4C**. Real-world care is multidisciplinary and individualized:

- Physical therapy: low-to-moderate intensity aerobic and strengthening exercise, balance work, stretching, preservation of ankle range, fall prevention and fatigue-aware pacing.
- Occupational therapy: hand function, energy conservation, adaptive equipment, school/work accommodations.
- Orthoses: ankle-foot orthoses, insoles, supportive footwear, walking aids and wheelchairs as needed; 59% used orthotic aids in the 2023 cohort. (rehbein2023neuropathydueto pages 2-3)
- Orthopedic treatment: serial monitoring during growth; tendon/soft-tissue or bony foot reconstruction for painful rigid deformity; scoliosis bracing or spinal fusion according to curve progression, skeletal maturity, function and respiratory considerations. CMT4C-specific surgical comparative trials are absent.
- Symptom management: neuropathic/nociceptive pain treatment, podiatry and skin protection, audiology/hearing aids, and respiratory assessment when clinically indicated.
- Medication review: minimize avoidable peripheral-neurotoxic agents when alternatives exist; decisions about essential chemotherapy require individualized risk–benefit assessment.

Suggested NCIt intervention concepts include **Physical Therapy (C15300)**, Occupational Therapy, Orthotic Device, Hearing Aid, Spinal Fusion, Scoliosis Surgery, Genetic Counseling, and Gene Therapy; codes other than the explicitly given physical-therapy code should be validated against the current NCIt release.

### Experimental and recent therapeutic developments

**Schwann-cell SH3TC2 replacement:** intrathecal lentiviral expression of human SH3TC2 under an Mpz promoter in three-week-old Sh3tc2-null mice improved motor behavior, motor conduction velocity, myelin thickness/g-ratio, demyelinated-fiber burden and nodal architecture, and reduced blood neurofilament light. This is proof-of-concept mouse evidence, not a human treatment. (schiza2019genereplacementtherapy pages 1-1)

A **2023 AAV9 Schwann-cell-targeted SH3TC2 replacement** study further advanced vector delivery (Georgiou et al., *Molecular Therapy*, November 2023, DOI [10.1016/j.ymthe.2023.08.020](https://doi.org/10.1016/j.ymthe.2023.08.020)); it remains preclinical.

**NT-3 gene therapy:** in 2024, 4-week-old Sh3tc2-null mice received intramuscular scAAV1.tMCK.NT-3 (1×10¹¹ vg). At six months, treatment improved rotarod, grip strength, conduction velocity, hypomyelination and NMJ denervation and increased 3–6-µm myelinated axons. The abstract states: “NT-3 gene therapy improved functional and electrophysiological outcomes including rotarod, grip strength and nerve conduction velocity.” This is a trophic, genotype-nonspecific strategy and does not replace SH3TC2. (ozes2024aav1.tmck.nt3genetherapy pages 1-3)

No CMT4C-specific human response rate, adverse-event profile, pharmacogenomic guideline, CRISPR therapy, ASO, cell therapy, or approved targeted drug is available.

### Trials and readiness

**NCT01193075**, Natural History Evaluation of CMT types including CMT4C, is a recruiting observational study led by the University of Iowa with planned enrollment up to 5,000; the 2023 CMT4C analysis drew from this network. **NCT05902351** is a broader recruiting observational natural-history study planned for up to 10,000 participants. Neither is a CMT4C therapeutic trial. The 2023 longitudinal data support CMTES/CMTES-R as multi-year outcomes, but also show the need for more responsive biomarkers. (rehbein2023neuropathydueto pages 9-10, rehbein2023neuropathydueto pages 2-3)

## 13. Prevention

Primary lifestyle prevention is not possible because the cause is inherited. Primary genetic prevention options, after counseling, include carrier testing of partners/relatives, preimplantation genetic testing for monogenic disease, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and donor gametes. Decisions must remain nondirective.

Secondary prevention consists of cascade testing in relatives and early assessment of genetically affected children—not general-population or newborn screening. Early identification permits surveillance of gait, feet, spine and hearing before fixed complications. Tertiary prevention includes stretching, orthoses, fall and pressure-injury prevention, scoliosis monitoring, hearing support and timely orthopedic intervention. Vaccines and anti-infective prophylaxis have no CMT4C-specific role.

## 14. Other species and natural disease

No well-established naturally occurring SH3TC2-equivalent CMT4C syndrome in companion animals or wildlife was identified in the retrieved literature. There is no zoonotic or cross-species transmission. Orthologues are conserved across vertebrates, supporting experimental modeling, but orthologue IDs should be pulled directly from NCBI Gene/Alliance releases during database ingestion. Relevant taxa include **Homo sapiens (NCBI Taxon 9606)** and **Mus musculus (10090)**.

## 15. Model organisms

### Mouse models

The principal model is the **Sh3tc2−/− mouse**, including exon-1 knockout and spontaneous loss-of-function lines. It recapitulates early progressive peripheral neuropathy, slowed conduction, hypomyelination/demyelination and nodal abnormalities, establishing Schwann-cell SH3TC2 as necessary for myelin maintenance and node integrity. (schiza2019genereplacementtherapy pages 1-2, rehbein2023neuropathydueto pages 9-10)

A detailed NMJ study found postsynaptic fragmentation/dispersal, increased fetal acetylcholine-receptor γ-subunit expression and altered sciatic-nerve extracellular-matrix proteins without altered axonal width or input number. Its conclusion was that “CMT4C pathology includes a compromised NMJ even in the absence of changes to the innervating axon.”

Applications include mechanism discovery, vector biodistribution, myelin/nodal outcome testing, electrophysiology, neurofilament biomarker development and therapeutic proof-of-concept. Limitations include species-specific nerve length and biomechanics, compressed disease timescale, incomplete capture of human scoliosis/cranial phenotypes, and uncertain translation of intrathecal or intramuscular vector dose and immunity.

### Cellular models

Transfected cells and Schwann-cell systems have been used to study plasma-membrane/recycling-endosome localization, Rab11 association and mutant behavior. Human iPSC-derived Schwann cells are conceptually attractive for patient-specific trafficking and therapeutic studies, but no mature CMT4C organoid or validated high-throughput human cellular platform was established in the retrieved evidence.

## Key interpretation and knowledge gaps

Authoritative clinical opinion is converging on three points. First, **scoliosis is a powerful clue but not a requirement**; absence of scoliosis, cranial disease or early onset must not preclude SH3TC2 testing. Second, broad sequencing with rigorous biallelic interpretation is superior to phenotype-only diagnosis because both private variants and dual diagnoses occur. Third, CMT4C is biologically attractive for gene replacement because it is recessive and Schwann-cell restricted, but delivery to the extensive human peripheral nervous system, durability, dose, immunity and treatment timing remain major translational barriers. (rehbein2023neuropathydueto pages 1-2, jerath2018charcot–marie–toothdiseasetype pages 1-3, jerath2018charcot–marie–toothdiseasetype pages 8-10)

Priority gaps are population prevalence/incidence, ancestry-specific carrier frequencies, validated modifiers, patient-reported QOL, respiratory natural history, pediatric progression biomarkers, human biofluid biomarkers, and interventional safety/efficacy data. Claims concerning epigenomics, metabolomics, protective factors, natural animal disease, or treatment response should therefore be represented as **not established**, not as negative biological findings.

## Selected source links and publication dates

1. Rehbein et al. “Neuropathy due to bi-allelic SH3TC2 variants: genotype-phenotype correlation and natural history.” *Brain*. March 2023. [DOI 10.1093/brain/awad095](https://doi.org/10.1093/brain/awad095). (rehbein2023neuropathydueto pages 1-2)
2. Ozes et al. “AAV1.tMCK.NT-3 gene therapy improves phenotype in Sh3tc2−/− mouse model of CMT4C.” *Brain Communications*. November 2024. [DOI 10.1093/braincomms/fcae394](https://doi.org/10.1093/braincomms/fcae394). (ozes2024aav1.tmck.nt3genetherapy pages 1-3)
3. Schiza et al. “Gene replacement therapy in a model of Charcot-Marie-Tooth 4C neuropathy.” *Brain*. March 2019. [DOI 10.1093/brain/awz064](https://doi.org/10.1093/brain/awz064). (schiza2019genereplacementtherapy pages 1-1)
4. Jerath et al. “Charcot–Marie–Tooth Disease type 4C: Novel mutations, clinical presentations, and diagnostic challenges.” *Muscle & Nerve*. May 2018. [DOI 10.1002/mus.25981](https://doi.org/10.1002/mus.25981). (jerath2018charcot–marie–toothdiseasetype pages 1-3)
5. Piscosquito et al. “Screening for SH3TC2 gene mutations in demyelinating recessive CMT.” *Journal of the Peripheral Nervous System*. September 2016. [DOI 10.1111/jns.12175](https://doi.org/10.1111/jns.12175). (piscosquito2016screeningforsh3tc2 pages 3-4)
6. Open Targets disease–target record; literature-linked PMIDs include 14574644, 19805030, 20301514 and 34193129. [Open Targets Platform](https://platform.opentargets.org/). (OpenTargets Search: Charcot-Marie-Tooth disease type 4C-SH3TC2)

**Curation caution:** PMID values are supplied only where recovered from the authoritative linked database. DOI links are provided for the remaining primary studies rather than inferring unverified PMID numbers.

References

1. (rehbein2023neuropathydueto pages 1-2): Tyler Rehbein, Tong Tong Wu, Simona Treidler, Davide Pareyson, Richard Lewis, Sabrina W Yum, Brett A McCray, Sindhu Ramchandren, Joshua Burns, Jun Li, Richard S Finkel, Steven S Scherer, Stephan Zuchner, Michael E Shy, Mary M Reilly, and David N Herrmann. Neuropathy due to bi-allelic sh3tc2 variants: genotype-phenotype correlation and natural history. Brain : a journal of neurology, 146:3826-3835, Mar 2023. URL: https://doi.org/10.1093/brain/awad095, doi:10.1093/brain/awad095. This article has 28 citations.

2. (rehbein2023neuropathydueto pages 9-10): Tyler Rehbein, Tong Tong Wu, Simona Treidler, Davide Pareyson, Richard Lewis, Sabrina W Yum, Brett A McCray, Sindhu Ramchandren, Joshua Burns, Jun Li, Richard S Finkel, Steven S Scherer, Stephan Zuchner, Michael E Shy, Mary M Reilly, and David N Herrmann. Neuropathy due to bi-allelic sh3tc2 variants: genotype-phenotype correlation and natural history. Brain : a journal of neurology, 146:3826-3835, Mar 2023. URL: https://doi.org/10.1093/brain/awad095, doi:10.1093/brain/awad095. This article has 28 citations.

3. (rehbein2023neuropathydueto pages 2-3): Tyler Rehbein, Tong Tong Wu, Simona Treidler, Davide Pareyson, Richard Lewis, Sabrina W Yum, Brett A McCray, Sindhu Ramchandren, Joshua Burns, Jun Li, Richard S Finkel, Steven S Scherer, Stephan Zuchner, Michael E Shy, Mary M Reilly, and David N Herrmann. Neuropathy due to bi-allelic sh3tc2 variants: genotype-phenotype correlation and natural history. Brain : a journal of neurology, 146:3826-3835, Mar 2023. URL: https://doi.org/10.1093/brain/awad095, doi:10.1093/brain/awad095. This article has 28 citations.

4. (ozes2024aav1.tmck.nt3genetherapy pages 1-3): Burcak Ozes, Lingying Tong, Kyle Moss, Morgan Myers, Lilye Morrison, Zayed Attia, and Zarife Sahenk. Aav1.tmck.nt-3 gene therapy improves phenotype in sh3tc2−/− mouse model of charcot–marie–tooth type 4c. Brain Communications, Nov 2024. URL: https://doi.org/10.1093/braincomms/fcae394, doi:10.1093/braincomms/fcae394. This article has 6 citations and is from a peer-reviewed journal.

5. (schiza2019genereplacementtherapy pages 1-2): Natasa Schiza, Elena Georgiou, Alexia Kagiava, Jean-Jacques Médard, Jan Richter, Christina Tryfonos, Irene Sargiannidou, Amanda J Heslegrave, Alexander M Rossor, Henrik Zetterberg, Mary M Reilly, Christina Christodoulou, Roman Chrast, and Kleopas A Kleopa. Gene replacement therapy in a model of charcot-marie-tooth 4c neuropathy. Brain, 142(5):1227-1241, Mar 2019. URL: https://doi.org/10.1093/brain/awz064, doi:10.1093/brain/awz064. This article has 60 citations and is from a highest quality peer-reviewed journal.

6. (schiza2019genereplacementtherapy pages 1-1): Natasa Schiza, Elena Georgiou, Alexia Kagiava, Jean-Jacques Médard, Jan Richter, Christina Tryfonos, Irene Sargiannidou, Amanda J Heslegrave, Alexander M Rossor, Henrik Zetterberg, Mary M Reilly, Christina Christodoulou, Roman Chrast, and Kleopas A Kleopa. Gene replacement therapy in a model of charcot-marie-tooth 4c neuropathy. Brain, 142(5):1227-1241, Mar 2019. URL: https://doi.org/10.1093/brain/awz064, doi:10.1093/brain/awz064. This article has 60 citations and is from a highest quality peer-reviewed journal.

7. (piscosquito2016screeningforsh3tc2 pages 3-4): Giuseppe Piscosquito, Paola Saveri, Stefania Magri, Claudia Ciano, Claudia Gandioli, Michela Morbin, Daniela D. Bella, Isabella Moroni, Franco Taroni, and Davide Pareyson. Screening for sh3tc2 gene mutations in a series of demyelinating recessive charcot‐marie‐tooth disease (cmt4). Journal of the Peripheral Nervous System, 21:142-149, Sep 2016. URL: https://doi.org/10.1111/jns.12175, doi:10.1111/jns.12175. This article has 57 citations and is from a peer-reviewed journal.

8. (piscosquito2016screeningforsh3tc2 pages 4-6): Giuseppe Piscosquito, Paola Saveri, Stefania Magri, Claudia Ciano, Claudia Gandioli, Michela Morbin, Daniela D. Bella, Isabella Moroni, Franco Taroni, and Davide Pareyson. Screening for sh3tc2 gene mutations in a series of demyelinating recessive charcot‐marie‐tooth disease (cmt4). Journal of the Peripheral Nervous System, 21:142-149, Sep 2016. URL: https://doi.org/10.1111/jns.12175, doi:10.1111/jns.12175. This article has 57 citations and is from a peer-reviewed journal.

9. (jerath2018charcot–marie–toothdiseasetype pages 1-3): Nivedita U. Jerath, Ami Mankodi, Thomas O. Crawford, Christopher Grunseich, Hasna Baloui, Chioma Nnamdi‐Emeratom, Alice B. Schindler, Terry Heiman‐Patterson, Roman Chrast, and Michael E. Shy. Charcot–marie–tooth disease type 4c: novel mutations, clinical presentations, and diagnostic challenges. Muscle & Nerve, 57:749-755, May 2018. URL: https://doi.org/10.1002/mus.25981, doi:10.1002/mus.25981. This article has 30 citations and is from a peer-reviewed journal.

10. (jerath2018charcot–marie–toothdiseasetype pages 8-10): Nivedita U. Jerath, Ami Mankodi, Thomas O. Crawford, Christopher Grunseich, Hasna Baloui, Chioma Nnamdi‐Emeratom, Alice B. Schindler, Terry Heiman‐Patterson, Roman Chrast, and Michael E. Shy. Charcot–marie–tooth disease type 4c: novel mutations, clinical presentations, and diagnostic challenges. Muscle & Nerve, 57:749-755, May 2018. URL: https://doi.org/10.1002/mus.25981, doi:10.1002/mus.25981. This article has 30 citations and is from a peer-reviewed journal.

11. (OpenTargets Search: Charcot-Marie-Tooth disease type 4C-SH3TC2): Open Targets Query (Charcot-Marie-Tooth disease type 4C-SH3TC2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

12. (schiza2019genereplacementtherapy pages 2-2): Natasa Schiza, Elena Georgiou, Alexia Kagiava, Jean-Jacques Médard, Jan Richter, Christina Tryfonos, Irene Sargiannidou, Amanda J Heslegrave, Alexander M Rossor, Henrik Zetterberg, Mary M Reilly, Christina Christodoulou, Roman Chrast, and Kleopas A Kleopa. Gene replacement therapy in a model of charcot-marie-tooth 4c neuropathy. Brain, 142(5):1227-1241, Mar 2019. URL: https://doi.org/10.1093/brain/awz064, doi:10.1093/brain/awz064. This article has 60 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Charcot-Marie-Tooth_Disease_Type_4C-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 34 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0011113` (5 mentions) - the report calls it "if available", "MONDO"; MONDO calls it **Charcot-Marie-Tooth disease type 4C**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0032456` (1 mention) - the report calls it "Processes:** endosomal recycling"; GO calls it **endocytic recycling**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0011113` - called "if available", "MONDO"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
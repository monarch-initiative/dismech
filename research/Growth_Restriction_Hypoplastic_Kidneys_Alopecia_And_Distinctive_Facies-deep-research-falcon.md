---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T15:19:08.391492'
end_time: '2026-09-04T15:26:37.099709'
duration_seconds: 448.71
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: HP:0000648
    reported_labels:
    - Ophthalmologic sign
    ontology_label: Optic atrophy
  - term_id: HP:0000407
    reported_labels:
    - Sensory manifestation; onset details unavailable
    ontology_label: Sensorineural hearing impairment
  unresolvable_prefixes:
  - Taxon
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Growth_Restriction_Hypoplastic_Kidneys_Alopecia_And_Distinctive_Facies-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies** covering all of the
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
- **Disease Name:** Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies** covering all of the
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


# Growth Restriction, Hypoplastic Kidneys, Alopecia, and Distinctive Facies

## Executive summary

**Growth restriction, hypoplastic kidneys, alopecia, and distinctive facies** is an exceptionally rare, congenital, autosomal-recessive multisystem disorder caused by biallelic **ZPR1** variants. The disease is indexed as **MONDO:0859146**. The defining report described only **four affected children from three New Mexican Hispanic families**, all associated with homozygous **ZPR1 c.587T>C (p.Ile196Thr), rs368697578**. Consequently, phenotype frequencies, penetrance, survival, and treatment effects cannot yet be estimated reliably. Open Targets independently maps the disorder to ZPR1 (ENSG00000109917) and specifies a biallelic allelic requirement. (OpenTargets Search: Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies, abok2024bioinformaticanalysisof pages 1-4)

The principal primary publication is Ito et al., *Clinical Genetics*, published online June 2018, volume 94, pages 303–312, **PMID: 29851065**, DOI: [10.1111/cge.13388](https://doi.org/10.1111/cge.13388). The most recent disease-focused analysis located was a **March 1, 2024 bioRxiv preprint**, DOI: [10.1101/2024.02.27.582196](https://doi.org/10.1101/2024.02.27.582196); it is computational, not peer reviewed, and must not be treated as an expanded clinical cohort. (abok2024bioinformaticanalysisof pages 1-4, abok2024bioinformaticanalysisof pages 15-19)

| Domain | Established finding | Suggested ontology term(s) | Evidence type/strength | Key source |
|---|---|---|---|---|
| Disease identity | Growth restriction, hypoplastic kidneys, alopecia, and distinctive facies is an ultra-rare congenital multisystem Mendelian syndrome associated with ZPR1 deficiency. | **MONDO:0859146**; suggested synonym: *ZPR1-associated growth-restriction syndrome* | Authoritative disease-level association supported by one small human case series | Open Targets maps the exact disease label to MONDO:0859146 and ZPR1 (OpenTargets Search: Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies) |
| Causal gene and inheritance | Biallelic **ZPR1** variation causes the syndrome; segregation in reported families supports autosomal-recessive inheritance. Parents and unaffected siblings were heterozygous carriers. | Suggested: ZPR1; autosomal recessive inheritance (**HP:0000007**) | Strong human genetic evidence, but based on four affected children from three families | Ito et al., 2018, PMID 29851065; summarized in the 2024 analysis (abok2024bioinformaticanalysisof pages 1-4) |
| Pathogenic variant | Reported causal variant: homozygous **ZPR1 c.587T>C (p.Ile196Thr)**, dbSNP **rs368697578**; germline missense variant in the A-domain involved in eEF1A interaction. | Suggested: sequence variant; missense variant (**SO:0001583**); germline variant | Strong segregation plus patient-cell functional evidence; ClinVar-listed, although current laboratory classification should be verified directly | Ito et al., 2018; variant/domain data (abok2024bioinformaticanalysisof pages 1-4, abok2024bioinformaticanalysisof pages 8-11) |
| Growth phenotype | Prenatal and postnatal growth restriction is a defining manifestation; the cellular phenotype resembles mechanisms implicated in primordial dwarfism. | Suggested HPO: intrauterine growth restriction (**HP:0001511**), postnatal growth retardation (**HP:0008897**), short stature (**HP:0004322**) | Human clinical evidence; exact patient-level frequencies and longitudinal growth curves unavailable in retrieved evidence | Four-child case series summarized in 2024 (abok2024bioinformaticanalysisof pages 1-4) |
| Renal phenotype | Hypoplastic kidneys and kidney dysfunction are core manifestations. Detailed laterality, nephron pathology, laboratory values, chronic-kidney-disease stages, and progression rates were not available. | Suggested HPO: renal hypoplasia (**HP:0000089**), abnormal renal function (exact term to validate); suggested UBERON: kidney | Human clinical evidence; small cohort and incomplete natural history | Ito et al., 2018 title and subsequent summary (abok2024bioinformaticanalysisof pages 1-4) |
| Hair/ectodermal phenotype | Congenital or inborn alopecia is characteristic. Hair-follicle histopathology and progression were not reported in the retrieved evidence. | Suggested HPO: alopecia (**HP:0001596**), congenital alopecia (exact child term to validate); suggested UBERON: hair follicle | Human clinical evidence; frequency not independently quantifiable beyond the defining case-series phenotype | Ito et al., 2018; 2024 summary (abok2024bioinformaticanalysisof pages 1-4) |
| Craniofacial and neurologic phenotype | Distinctive craniofacial features occur; reported associated findings include microcephaly, moderate intellectual disability, developmental delay, optic-nerve atrophy, and sensorineural hearing loss. | Suggested HPO: abnormal facial shape (**HP:0001999**), microcephaly (**HP:0000252**), intellectual disability (**HP:0001249**), global developmental delay (**HP:0001263**), optic atrophy (**HP:0000648**), sensorineural hearing impairment (**HP:0000407**) | Human clinical evidence, but individual-feature denominators are unavailable | Human syndrome findings summarized from Ito et al. (chittilla2021highfatdietassociatedcognitive pages 4-5, abok2024bioinformaticanalysisof pages 1-4) |
| Protein dysfunction | p.Ile196Thr lies in the hydrophobic core/A-domain and destabilizes ZPR1; patient fibroblasts reportedly contained little or no detectable ZPR1 because the misfolded protein was degraded by the proteasome. A 2024 FoldX analysis predicted a destabilizing ΔΔG of approximately 2.3 kcal/mol. | Suggested GO: protein folding, proteasomal protein catabolic process, regulation of protein stability; suggested cellular components: cytoplasm, nucleus, nucleolus | Patient-cell evidence plus computational structural support; degradation mechanism is stronger than purely in-silico predictions but needs replication | Ito et al. functional findings and 2024 modeling (abok2024bioinformaticanalysisof pages 11-15, chittilla2021highfatdietassociatedcognitive pages 4-5, abok2024bioinformaticanalysisof pages 8-11) |
| Cell-cycle mechanism | Mutant patient fibroblasts showed impaired progression beyond G1, with very few cells reaching late S or G2/M. Reduced proliferative capacity is the most direct demonstrated mechanism linking ZPR1 deficiency to generalized developmental growth failure. | Suggested GO: cell-cycle progression (**GO:0007049**), G1/S transition of mitotic cell cycle (**GO:0000082**), cell proliferation (**GO:0008283**); suggested CL: fibroblast (**CL:0000057**) | Direct patient-derived-cell functional evidence; organ-specific causal links remain inferred | Ito et al. findings summarized in the 2024 analysis (abok2024bioinformaticanalysisof pages 11-15, abok2024bioinformaticanalysisof pages 1-4) |
| Molecular pathway | ZPR1 normally participates in eEF1A-, EGFR-, SMN-, and RNA-polymerase-II-related complexes, translocating from cytoplasm to nucleus/nucleolus in proliferating cells. Disruption of ZPR1–eEF1A interaction by p.Ile196Thr is plausible but not directly demonstrated for every affected tissue. | Suggested GO: protein binding, nucleolar localization, transcription regulation, ribonucleoprotein-complex assembly; suggested cellular components: nucleolus (**GO:0005730**), nucleus (**GO:0005634**), cytoplasm (**GO:0005737**) | Established general ZPR1 biology; syndrome-specific pathway assignment remains partly inferred | Structural and localization literature summarized in 2024 (abok2024bioinformaticanalysisof pages 1-4, abok2024bioinformaticanalysisof pages 15-19) |
| Diagnosis | Diagnosis rests on recognition of the congenital phenotype plus molecular confirmation of biallelic ZPR1 variants. Exome or genome sequencing is preferable when the phenotype is nonspecific; targeted familial testing can confirm segregation. Renal ultrasound/function tests, audiology, ophthalmology, growth, and developmental assessments define organ involvement. | Suggested NCIT: Whole Exome Sequencing, Whole Genome Sequencing, Genetic Testing, Ultrasonography, Audiologic Test; suggested HPO-driven phenotyping | Genetic-testing strategy is a rational implementation based on discovery by exome sequencing; no formal syndrome-specific diagnostic criteria or guideline | Proband exome and segregation evidence (abok2024bioinformaticanalysisof pages 1-4); limited formal characterization acknowledged in 2024 (abok2024bioinformaticanalysisof pages 11-15) |
| Epidemiology and population data | Only four affected children from three New Mexican Hispanic ancestral families were initially reported; a Rio Grande Valley founder effect/endogamy was suggested but not proven. A 2024 preprint reported predicted damaging heterozygous ZPR1 variants in 0.04%–0.34% of ancestry groups, but these figures are **not** disease prevalence or validated carrier frequency for p.Ile196Thr. | Suggested epidemiology annotation: ultra-rare disease; founder variant hypothesis | Very limited human ascertainment; population estimates are computational and should not be used as clinical penetrance estimates | Human families and founder hypothesis (abok2024bioinformaticanalysisof pages 1-4); gnomAD-based computational statistics (abok2024bioinformaticanalysisof pages 8-11, abok2024bioinformaticanalysisof pages 21-27) |
| Management and trials | No disease-modifying therapy, syndrome-specific management guideline, or relevant clinical trial was identified. Care is supportive and organ-directed, with renal, growth/nutrition, hearing, vision, neurodevelopmental, and genetic-counseling follow-up. ZPR1 overexpression studies in spinal muscular atrophy are not treatment evidence for this syndrome. | Suggested NCIT: Supportive Care, Genetic Counseling, Audiologic Rehabilitation, Physical Therapy, Occupational Therapy; exact NCIT identifiers to validate | Expert extrapolation from manifestations; no syndrome-specific intervention evidence | Literature and trial-gap assessment (chittilla2021highfatdietassociatedcognitive pages 1-2, abok2024bioinformaticanalysisof pages 1-4, abok2024bioinformaticanalysisof pages 15-19, abok2024bioinformaticanalysisof pages 4-8) |
| Prognosis | The published phenotype includes increased early mortality, but survival rates, causes of death, renal-failure risk, and life expectancy have not been quantified. Lifelong multisystem morbidity is likely, but the course cannot be reliably estimated from four reported patients. | Suggested HPO/course annotations: congenital onset, chronic course, early mortality (exact terms to validate) | Weak-to-moderate natural-history evidence because of extremely small sample and absent longitudinal cohort | Clinical summary of the original families (abok2024bioinformaticanalysisof pages 1-4) |
| Models and comparative evidence | No natural veterinary disease or p.Ile196Thr syndrome-specific knock-in model was identified. Zpr1-deficient mice show neurodegeneration, facial and spinal motor-neuron loss, axon retraction, and microtubule disruption; these models establish biological necessity but incompletely reproduce the human renal–hair–growth syndrome. | Suggested taxa: *Mus musculus* (**NCBI Taxon:10090**); suggested CL: motor neuron (**CL:0000100**); suggested GO: neuron death, axon maintenance, microtubule organization | Experimental mouse evidence, indirect for this syndrome; SMA rescue models are mechanistic comparators only | ZPR1-deficient mouse findings and limitations (chittilla2021highfatdietassociatedcognitive pages 1-2) |


*Table: Compact ontology-ready summary of established findings, evidence strength, and major knowledge gaps for MONDO:0859146. Ontology mappings marked “suggested” require curator validation before database ingestion.*

## 1. Disease information

The disorder is a developmental syndrome combining prenatal and postnatal growth failure, congenital alopecia, renal hypoplasia/dysfunction, and recognizable craniofacial features. Reported additional manifestations include developmental delay, moderate intellectual disability, microcephaly, sensorineural hearing loss, and optic atrophy. Evidence comes principally from a small published family cohort, not from EHR-scale aggregation or a disease registry. (abok2024bioinformaticanalysisof pages 1-4, chittilla2021highfatdietassociatedcognitive pages 4-5)

**Identifiers and nomenclature**

- **MONDO:** MONDO:0859146.
- **Gene:** ZPR1, “ZPR1 zinc finger”; Ensembl **ENSG00000109917**; cytogenetic location **11q23.3**.
- **Synonyms suitable for indexing:** *ZPR1-associated growth-restriction syndrome*; *growth restriction–hypoplastic kidneys–alopecia–distinctive facies syndrome*; and the descriptive title *alopecia–primordial dwarfism–renal syndrome* used in earlier conference literature.
- **OMIM, Orphanet, MeSH, ICD-10, and ICD-11:** no disease-specific identifiers were established in the retrieved authoritative evidence. A 2024 source stated that ZPR1-associated disease was absent from Orphanet at the time assessed. Generic congenital-malformation or genetic-disease codes should not be presented as disease-specific identifiers. (OpenTargets Search: Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies, abok2024bioinformaticanalysisof pages 1-4, abok2024bioinformaticanalysisof pages 11-15)

## 2. Etiology, risk, and protective factors

### Causal factor

The demonstrated cause is a **germline homozygous missense variant in ZPR1**, c.587T>C, p.Ile196Thr. Parents and unaffected siblings were heterozygous, supporting autosomal-recessive segregation. The affected families’ shared Rio Grande Valley ancestry suggested—but did not prove—a founder variant combined with endogamy. (abok2024bioinformaticanalysisof pages 1-4)

### Risk factors

The principal risk is inheriting two pathogenic ZPR1 alleles. For two confirmed heterozygous parents, standard autosomal-recessive counseling predicts, for each pregnancy, a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of an unaffected non-carrier. Consanguinity or shared founder ancestry may increase the chance that partners carry the same rare allele, although consanguinity itself was not established as causal in the reported families.

No sex-, age-, infectious-, occupational-, toxin-, smoking-, dietary-, or lifestyle-related cause of this congenital syndrome has been demonstrated. Common ZPR1-region variants associated with lipids or diabetes, and experiments linking high-fat diets to altered ZPR1 expression, concern complex metabolic traits or experimental neurobiology—not this recessive syndrome. They should not be imported as syndrome risk factors. (chittilla2021highfatdietassociatedcognitive pages 2-3, chittilla2021highfatdietassociatedcognitive pages 1-2, abok2024bioinformaticanalysisof pages 4-8)

### Protective factors and gene–environment interaction

No protective allele, modifier gene, diet, medication, or environmental exposure has been validated. EGF-regulated nuclear translocation, high-fat-diet models, and n-3 PUFA observations concern general ZPR1 biology and do not establish clinically actionable gene–environment interaction in affected children. (chittilla2021highfatdietassociatedcognitive pages 1-2, abok2024bioinformaticanalysisof pages 1-4)

## 3. Phenotypes

Because only four original patients were reported and individual-level denominators were not available in the retrieved text, the defining manifestations should be recorded as **observed/core**, not assigned precise percentages.

| Manifestation | Type, onset, and course | Suggested HPO term |
|---|---|---|
| Prenatal growth restriction | Physical sign; prenatal onset; apparently persistent | Intrauterine growth retardation, **HP:0001511** |
| Postnatal growth failure/short stature | Physical sign; infancy/childhood; chronic | Postnatal growth retardation, **HP:0008897**; short stature, **HP:0004322** |
| Congenital alopecia | Ectodermal manifestation; present from birth | Alopecia, **HP:0001596**; validate a congenital-alopecia child term |
| Hypoplastic kidneys | Structural congenital anomaly; likely bilateral status should be verified patient by patient | Renal hypoplasia, **HP:0000089** |
| Kidney dysfunction | Laboratory/functional abnormality; severity and progression unavailable | Abnormal renal physiology; curator should select the most specific term from patient data |
| Distinctive facies | Dysmorphic sign; congenital | Abnormal facial shape, **HP:0001999** |
| Microcephaly | Growth/neurodevelopmental sign | Microcephaly, **HP:0000252** |
| Developmental delay/intellectual disability | Neurodevelopmental; childhood; at least one patient described as moderately affected | Global developmental delay, **HP:0001263**; intellectual disability, **HP:0001249** |
| Sensorineural hearing impairment | Sensory manifestation; onset details unavailable | **HP:0000407** |
| Optic atrophy | Ophthalmologic sign | **HP:0000648** |

The 2024 summary characterizes the syndrome as including prenatal/postnatal growth restriction, congenital hair loss, kidney dysfunction, developmental delay, hearing impairment, and increased early mortality. A later review quotes the original patient description as including “**moderate intellectual disability**.” (chittilla2021highfatdietassociatedcognitive pages 4-5, abok2024bioinformaticanalysisof pages 1-4)

No validated EQ-5D, SF-36, PROMIS, behavioral, or disease-specific quality-of-life data exist. Nevertheless, chronic renal monitoring, marked short stature, sensory impairment, alopecia, and developmental disability plausibly impose substantial educational, medical, communication, and psychosocial burdens; this is clinical inference rather than measured outcome evidence.

## 4. Genetic and molecular information

**ZPR1** encodes a 459-amino-acid, ubiquitously expressed C4-type zinc-finger protein. It is normally cytoplasmic in quiescent cells and relocates to the nucleus/nucleolus during growth-factor-stimulated proliferation. It interacts with eEF1A, EGFR, SMN, and RNA polymerase II-associated machinery. (chittilla2021highfatdietassociatedcognitive pages 1-2, abok2024bioinformaticanalysisof pages 1-4)

The syndrome-associated allele is:

- **ZPR1 c.587T>C; p.Ile196Thr; rs368697578**.
- Germline, homozygous in affected individuals and heterozygous in available unaffected relatives.
- Missense variant in the A-domain involved in eEF1A interaction.
- Patient-cell evidence supports protein destabilization and loss of functional abundance; the mutant protein was described as misfolded and proteasomally degraded.
- A 2024 FoldX analysis estimated **ΔΔG ≈2.3 kcal/mol**, consistent with destabilization, but that result is computational support rather than an independent functional assay. (abok2024bioinformaticanalysisof pages 11-15, chittilla2021highfatdietassociatedcognitive pages 4-5, abok2024bioinformaticanalysisof pages 8-11)

Open Targets reports ClinVar/EVA support and a biallelic requirement, but the current ClinVar review status and ACMG criteria should be checked directly before clinical reporting. The 2024 preprint’s classification of 60 predicted variants as “pathogenic” using in-silico consensus is not equivalent to expert-panel ACMG classification. No validated modifier gene, disease-associated methylation signature, somatic mechanism, repeat expansion, mitochondrial variant, or pathogenic chromosomal rearrangement has been reported. (OpenTargets Search: Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies, abok2024bioinformaticanalysisof pages 8-11, abok2024bioinformaticanalysisof pages 15-19)

## 5. Environmental information

No environmental, lifestyle, toxicological, infectious, or nutritional cause is known. The disorder is Mendelian and congenital. High-fat-diet studies show altered hippocampal ZPR1 expression and neurobiological effects in rodents, but these do not demonstrate that diet causes, prevents, or changes the pediatric ZPR1 syndrome. There is no evidence for zoonotic or infectious transmission. (chittilla2021highfatdietassociatedcognitive pages 1-2, chittilla2021highfatdietassociatedcognitive pages 5-6)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic ZPR1 p.Ile196Thr leads to** substitution of a buried hydrophobic-core/A-domain residue.
2. The substitution **leads to** ZPR1 destabilization and misfolding, followed by proteasomal degradation in patient fibroblasts.
3. Reduced functional ZPR1 **results in** defective proliferative-cell ZPR1 activity and abnormal subcellular/cell-cycle behavior.
4. This dysfunction **leads to** failure of efficient G1-to-S progression; very few patient fibroblasts reached late S or G2/M.
5. Reduced cell proliferation during development **is inferred to lead to** prenatal/postnatal growth restriction and microcephaly.
6. **Branch A:** impaired proliferation/differentiation in renal developmental lineages **is inferred to result in** hypoplastic kidneys and renal dysfunction.
7. **Branch B:** impaired epithelial/hair-follicle development **is inferred to result in** congenital alopecia.
8. **Branch C:** disturbed neural and sensory development, potentially compounded by ZPR1’s roles in SMN/RNA processing and genome maintenance, **is inferred to result in** developmental disability, hearing impairment, and optic atrophy.
9. Multiorgan developmental disease and renal dysfunction **may lead to** increased early mortality, but causes of death have not been quantified. (abok2024bioinformaticanalysisof pages 11-15, chittilla2021highfatdietassociatedcognitive pages 4-5, abok2024bioinformaticanalysisof pages 1-4)

The strongest syndrome-specific functional evidence is therefore **protein loss plus cell-cycle arrest in patient fibroblasts**. Disruption of the ZPR1–eEF1A interaction is mechanistically plausible because Ile196 lies in the eEF1A-binding A-domain, but direct disruption by p.Ile196Thr was not established in every affected lineage. (abok2024bioinformaticanalysisof pages 11-15)

General ZPR1 studies connect deficiency with altered SMN localization/transcription, R-loop accumulation, impaired DNA repair, MLK3–MKK7–JNK signaling, caspase-3 activation, and neurodegeneration. These pathways provide biological hypotheses for neurologic disease but were primarily demonstrated in SMA or other experimental contexts, not in renal or hair tissue from these patients. (chittilla2021highfatdietassociatedcognitive pages 1-2, chittilla2021highfatdietassociatedcognitive pages 2-3)

**Suggested annotations:** GO:0007049 cell cycle; GO:0000082 G1/S transition of mitotic cell cycle; GO:0008283 cell population proliferation; proteasomal protein catabolic process; protein folding; RNA processing; DNA repair; GO:0005634 nucleus; GO:0005730 nucleolus; GO:0005737 cytoplasm. Suggested cell types include fibroblast (**CL:0000057**), renal epithelial/progenitor cells, hair-follicle epithelial cells, sensory neurons, and motor neurons; only fibroblasts were directly examined in syndrome-specific functional work.

No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, organoid, CRISPR-screen, or multi-omics profile was identified.

## 7. Anatomical structures affected

Primary organs are the **kidneys**, skin appendages/hair follicles, craniofacial structures, and the growth axis/skeleton. Secondary or associated involvement includes brain/head growth, auditory structures, and optic nerves. Suggested anatomical mappings are kidney (**UBERON:0002113**), hair follicle (**UBERON:0002073**, curator validation advised), skin, brain, optic nerve, and inner ear. Available evidence does not establish renal laterality, nephron-segment specificity, histopathology, or a single targeted kidney cell population. (chittilla2021highfatdietassociatedcognitive pages 4-5, abok2024bioinformaticanalysisof pages 1-4)

At the subcellular level, ZPR1 biology implicates the cytoplasm, nucleus, and nucleolus. Misfolded p.Ile196Thr also implicates cytosolic protein-quality-control/proteasomal machinery. (chittilla2021highfatdietassociatedcognitive pages 1-2, abok2024bioinformaticanalysisof pages 1-4)

## 8. Temporal development

Onset is prenatal/congenital: fetal growth restriction, renal hypoplasia, dysmorphism, and alopecia arise during development. Postnatal growth failure and neurodevelopmental disability persist. The syndrome should be considered chronic and lifelong, but no validated staging system, progression rate, remission pattern, or critical treatment window exists. Early childhood appears to be a vulnerable period because increased early mortality was reported, although the number and causes of deaths were not recovered. (abok2024bioinformaticanalysisof pages 1-4)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. The original evidence comprises four affected children in three families of New Mexican Hispanic ancestry. The suggested Rio Grande Valley founder effect remains unconfirmed by haplotype dating or broad population screening. Penetrance for true biallelic loss-of-function genotypes is unknown; expressivity appears multisystemic, but its range cannot be defined from four patients. Anticipation has not been reported. Germline mosaicism is theoretically possible for any Mendelian variant but has not been demonstrated. (abok2024bioinformaticanalysisof pages 1-4)

No incidence, prevalence per 100,000, sex ratio, or validated disease-carrier frequency is available. A 2024 preprint screened **122,678** gnomAD individuals and computationally labeled 60 of 223 ZPR1 missense variants as damaging. It reported **330 heterozygous carriers (0.27%)** and three homozygotes for this pooled predicted-variant set, with heterozygote proportions from **0.04% in Ashkenazi Jewish to 0.34% in African/African American groups**. These values are neither prevalence estimates for MONDO:0859146 nor carrier frequencies for p.Ile196Thr; prediction-based classifications and apparently healthy homozygotes demand cautious interpretation. (abok2024bioinformaticanalysisof pages 8-11, abok2024bioinformaticanalysisof pages 21-27)

## 10. Diagnostics

Diagnosis should combine the congenital phenotype with molecular confirmation:

1. Document prenatal/postnatal growth, head circumference, alopecia, dysmorphology, renal anatomy/function, development, hearing, and vision.
2. Perform renal ultrasonography; serum creatinine/eGFR, electrolytes, urinalysis, urine protein/albumin, and blood pressure should characterize renal involvement.
3. Conduct audiology, ophthalmology, neurodevelopmental assessment, and nutritional/endocrine evaluation tailored to growth failure.
4. Use a growth-disorder, CAKUT, alopecia/ectodermal-dysplasia, or developmental-disorder panel containing **ZPR1**, or preferably trio WES/WGS when the presentation is nonspecific.
5. Confirm candidate variants by an orthogonal method and test parental segregation. Targeted familial testing is appropriate once the allele is known.

Exome sequencing identified the causal allele in the original proband, supporting real-world use of WES. WGS may detect noncoding or structural variants missed by WES, but no syndrome-specific WGS yield has been reported. CMA is reasonable when multiple congenital anomalies remain unexplained but will not detect an ordinary single-nucleotide ZPR1 variant. Karyotyping, FISH, mitochondrial sequencing, repeat-expansion testing, liquid biopsy, proteomics, and metabolomics are not first-line tests for this phenotype unless independently indicated. (abok2024bioinformaticanalysisof pages 1-4)

There are no standardized clinical diagnostic criteria. Differential diagnoses include other primordial dwarfism/cell-cycle disorders, syndromic CAKUT, ectodermal dysplasias, renal–retinal ciliopathies, progeroid disorders, and BRESEK/BRESHECK-like syndromes. Molecular confirmation is decisive because phenotypic overlap is substantial.

## 11. Outcome and prognosis

The available literature indicates **increased early mortality**, but provides no five- or ten-year survival, life expectancy, cause-specific mortality, renal-failure probability, or prognostic biomarker. Potential morbidity includes chronic kidney disease, severe growth impairment, hearing/vision disability, developmental disability, and psychosocial effects of alopecia. Prognosis should therefore be individualized according to renal function, growth/nutrition, neurodevelopment, and sensory involvement. (abok2024bioinformaticanalysisof pages 1-4)

Recovery from congenital structural abnormalities is not expected, although functional outcomes may improve with early supportive interventions. No molecular marker has been validated to predict severity.

## 12. Treatment and current implementation

No approved disease-modifying treatment, genotype-directed drug, gene therapy, RNA therapy, cell therapy, immunotherapy, or disease-specific clinical trial was identified. No response-rate or adverse-event dataset exists. (chittilla2021highfatdietassociatedcognitive pages 1-2, abok2024bioinformaticanalysisof pages 1-4, abok2024bioinformaticanalysisof pages 15-19)

Current care is necessarily multidisciplinary and organ directed:

- Pediatric nephrology: avoid nephrotoxins and dehydration; manage hypertension, proteinuria, electrolyte disturbance, anemia, CKD-mineral/bone disease, and renal failure according to standard pediatric nephrology practice.
- Growth/nutrition: dietitian assessment and evaluation for treatable nutritional or endocrine contributors. Evidence is insufficient to recommend growth hormone specifically for ZPR1 deficiency.
- Audiology/ENT: hearing aids, cochlear-implant assessment, and communication support when indicated.
- Ophthalmology: monitor optic and visual function and provide low-vision services.
- Development: early-intervention services, physical, occupational, speech/language, and educational therapies.
- Dermatology and psychosocial care: scalp protection and optional cosmetic hair prostheses.
- Clinical genetics: family testing, recurrence-risk counseling, and variant reinterpretation.

Suggested NCIT concepts include Genetic Counseling, Supportive Care, Whole Exome Sequencing, Whole Genome Sequencing, Ultrasonography, Audiologic Testing, Physical Therapy, Occupational Therapy, and Speech Therapy; exact NCIT identifiers should be validated by a terminology curator.

ZPR1 overexpression increased SMN and rescued SMA-model phenotypes, but this is **not** evidence that ZPR1 augmentation is safe or effective for children with biallelic ZPR1 deficiency. It remains a conceptual research direction only. (abok2024bioinformaticanalysisof pages 4-8)

## 13. Prevention

There is no lifestyle, vaccine, medication, or public-health intervention that prevents a child with a biallelic pathogenic genotype from developing the syndrome.

Primary genetic prevention options include carrier testing for adult relatives, partner testing, preimplantation genetic testing for monogenic disease, prenatal diagnosis by chorionic-villus sampling or amniocentesis, and use of donor gametes. Secondary prevention consists of early molecular diagnosis and prompt renal, hearing, visual, nutritional, and developmental evaluation. Tertiary prevention targets CKD progression, sensory disability, nutritional complications, and developmental loss. Population-wide newborn or carrier screening is not currently justified by the extremely limited natural-history and variant-classification evidence. (abok2024bioinformaticanalysisof pages 15-19)

## 14. Other species and natural disease

No naturally occurring veterinary counterpart, breed predisposition, zoonotic potential, or cross-species transmission was identified. ZPR1 is evolutionarily conserved, and mouse structural data were used to model the human protein. Relevant taxonomy is *Homo sapiens* (**NCBI Taxon:9606**) and *Mus musculus* (**NCBI Taxon:10090**). (abok2024bioinformaticanalysisof pages 4-8)

## 15. Model organisms

No p.Ile196Thr knock-in mouse, zebrafish, organoid, or patient-derived iPSC model that reproduces the combined renal–hair–growth phenotype was identified. Zpr1-deficient mice show facial and spinal motor-neuron degeneration, axon retraction, microtubule disruption, and other neurodegenerative abnormalities. These experiments demonstrate that ZPR1 is required for neuronal maintenance but do not fully model the human syndrome. (chittilla2021highfatdietassociatedcognitive pages 1-2)

Patient fibroblasts remain the most disease-specific experimental model: they show markedly depleted ZPR1 and impaired cell-cycle progression. Future priority models should include isogenic p.Ile196Thr iPSCs differentiated into nephron progenitors, hair-follicle organoids, neural lineages, and a knock-in animal model to distinguish developmental cell-proliferation failure from tissue-specific RNA-processing or genome-maintenance defects. (abok2024bioinformaticanalysisof pages 11-15)

## Evidence appraisal and research priorities

The present understanding rests on one four-patient clinical report, patient fibroblast experiments, general ZPR1 biology, and a 2024 computational preprint. Major unresolved questions are the full phenotypic spectrum, renal natural history, causes of early mortality, penetrance of other biallelic alleles, founder-variant frequency, genotype–phenotype relationships, growth-hormone biology, and therapeutic reversibility. The most authoritative conclusion is therefore narrow: **biallelic ZPR1 p.Ile196Thr causes a congenital growth–renal–hair–craniofacial syndrome through ZPR1 protein deficiency with defective cellular proliferation; most organ-specific mechanistic links and all treatment claims remain unproven.** (OpenTargets Search: Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies, abok2024bioinformaticanalysisof pages 11-15, abok2024bioinformaticanalysisof pages 1-4)

### Key references

1. Ito YA, Smith AC, Kernohan KD, et al. “A ZPR1 mutation is associated with a novel syndrome of growth restriction, distinct craniofacial features, alopecia, and hypoplastic kidneys.” *Clinical Genetics*. 2018;94:303–312. PMID: **29851065**. DOI: [10.1111/cge.13388](https://doi.org/10.1111/cge.13388). (abok2024bioinformaticanalysisof pages 15-19)
2. Abok JI, Garver WS, Edwards JS. “Bioinformatic analysis of human ZPR1 gene pathogenic exome mutations.” bioRxiv. Posted **March 1, 2024**. DOI: [10.1101/2024.02.27.582196](https://doi.org/10.1101/2024.02.27.582196). The abstract states: “**We examined 223 germline ZPR1 exome variants**” and reports predicted heterozygous harmful-variant frequencies of 0.04%–0.34%; these remain computational findings. (abok2024bioinformaticanalysisof pages 1-4)
3. Chittilla M, Akimbekov NS, Razzaque MS. “High-fat diet-associated cognitive decline: Is zinc finger protein 1 (ZPR1) the molecular connection?” *Current Research in Physiology*. Available online **October 2, 2021**. DOI: [10.1016/j.crphys.2021.09.004](https://doi.org/10.1016/j.crphys.2021.09.004). This is supporting general ZPR1 biology, not syndrome-specific clinical evidence. (chittilla2021highfatdietassociatedcognitive pages 1-2)

References

1. (OpenTargets Search: Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies): Open Targets Query (Growth Restriction Hypoplastic Kidneys Alopecia And Distinctive Facies, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (abok2024bioinformaticanalysisof pages 1-4): Jeremiah I. Abok, William S. Garver, and Jeremy S. Edwards. Bioinformatic analysis of human zpr1 gene pathogenic exome mutations. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.02.27.582196, doi:10.1101/2024.02.27.582196. This article has 0 citations.

3. (abok2024bioinformaticanalysisof pages 15-19): Jeremiah I. Abok, William S. Garver, and Jeremy S. Edwards. Bioinformatic analysis of human zpr1 gene pathogenic exome mutations. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.02.27.582196, doi:10.1101/2024.02.27.582196. This article has 0 citations.

4. (abok2024bioinformaticanalysisof pages 8-11): Jeremiah I. Abok, William S. Garver, and Jeremy S. Edwards. Bioinformatic analysis of human zpr1 gene pathogenic exome mutations. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.02.27.582196, doi:10.1101/2024.02.27.582196. This article has 0 citations.

5. (chittilla2021highfatdietassociatedcognitive pages 4-5): Mythri Chittilla, Nuraly S. Akimbekov, and Mohammed S. Razzaque. High-fat diet-associated cognitive decline: is zinc finger protein 1 (zpr1) the molecular connection? Current Research in Physiology, 4:223-228, Oct 2021. URL: https://doi.org/10.1016/j.crphys.2021.09.004, doi:10.1016/j.crphys.2021.09.004. This article has 5 citations and is from a peer-reviewed journal.

6. (abok2024bioinformaticanalysisof pages 11-15): Jeremiah I. Abok, William S. Garver, and Jeremy S. Edwards. Bioinformatic analysis of human zpr1 gene pathogenic exome mutations. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.02.27.582196, doi:10.1101/2024.02.27.582196. This article has 0 citations.

7. (abok2024bioinformaticanalysisof pages 21-27): Jeremiah I. Abok, William S. Garver, and Jeremy S. Edwards. Bioinformatic analysis of human zpr1 gene pathogenic exome mutations. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.02.27.582196, doi:10.1101/2024.02.27.582196. This article has 0 citations.

8. (chittilla2021highfatdietassociatedcognitive pages 1-2): Mythri Chittilla, Nuraly S. Akimbekov, and Mohammed S. Razzaque. High-fat diet-associated cognitive decline: is zinc finger protein 1 (zpr1) the molecular connection? Current Research in Physiology, 4:223-228, Oct 2021. URL: https://doi.org/10.1016/j.crphys.2021.09.004, doi:10.1016/j.crphys.2021.09.004. This article has 5 citations and is from a peer-reviewed journal.

9. (abok2024bioinformaticanalysisof pages 4-8): Jeremiah I. Abok, William S. Garver, and Jeremy S. Edwards. Bioinformatic analysis of human zpr1 gene pathogenic exome mutations. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.02.27.582196, doi:10.1101/2024.02.27.582196. This article has 0 citations.

10. (chittilla2021highfatdietassociatedcognitive pages 2-3): Mythri Chittilla, Nuraly S. Akimbekov, and Mohammed S. Razzaque. High-fat diet-associated cognitive decline: is zinc finger protein 1 (zpr1) the molecular connection? Current Research in Physiology, 4:223-228, Oct 2021. URL: https://doi.org/10.1016/j.crphys.2021.09.004, doi:10.1016/j.crphys.2021.09.004. This article has 5 citations and is from a peer-reviewed journal.

11. (chittilla2021highfatdietassociatedcognitive pages 5-6): Mythri Chittilla, Nuraly S. Akimbekov, and Mohammed S. Razzaque. High-fat diet-associated cognitive decline: is zinc finger protein 1 (zpr1) the molecular connection? Current Research in Physiology, 4:223-228, Oct 2021. URL: https://doi.org/10.1016/j.crphys.2021.09.004, doi:10.1016/j.crphys.2021.09.004. This article has 5 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Growth_Restriction_Hypoplastic_Kidneys_Alopecia_And_Distinctive_Facies-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000648` (2 mentions) - the report calls it "Ophthalmologic sign"; HP calls it **Optic atrophy**
- `HP:0000407` (2 mentions) - the report calls it "Sensory manifestation; onset details unavailable"; HP calls it **Sensorineural hearing impairment**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.

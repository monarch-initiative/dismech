---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T12:05:54.787508'
end_time: '2026-09-08T12:20:07.781611'
duration_seconds: 852.99
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: FLRT3-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism
    21 with or without anosmia, HH21; FLRT3/fibronectin leucine-rich transmembrane
    protein 3; OMIM 615271)
  mondo_id: MONDO:0014107
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 48
  verified: 47
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 5
  labels_matching: 0
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0014107
    reported_labels:
    - if available
    ontology_label: hypogonadotropic hypogonadism 21 with or without anosmia
  - term_id: HP:0000044
    reported_labels:
    - Laboratory/endocrine abnormality; congenital, recognized in infancy or adolescence;
      usually persistent but variable
    ontology_label: Hypogonadotropic hypogonadism
  - term_id: HP:0000054
    reported_labels:
    - Congenital physical sign in severely affected 46,XY infants
    ontology_label: Micropenis
  - term_id: HP:0000028
    reported_labels:
    - Congenital sign, unilateral or bilateral; may persist and compromise fertility
    ontology_label: Cryptorchidism
  - term_id: HP:0004349
    reported_labels:
    - Secondary complication of delayed or untreated sex-steroid deficiency
    ontology_label: Reduced bone mineral density
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
  path: FLRT3_Hypogonadotropic_Hypogonadism-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** FLRT3-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism 21 with or without anosmia, HH21; FLRT3/fibronectin leucine-rich transmembrane protein 3; OMIM 615271)
- **MONDO ID:** MONDO:0014107 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FLRT3-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism 21 with or without anosmia, HH21; FLRT3/fibronectin leucine-rich transmembrane protein 3; OMIM 615271)** covering all of the
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
- **Disease Name:** FLRT3-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism 21 with or without anosmia, HH21; FLRT3/fibronectin leucine-rich transmembrane protein 3; OMIM 615271)
- **MONDO ID:** MONDO:0014107 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **FLRT3-Related Hypogonadotropic Hypogonadism (hypogonadotropic hypogonadism 21 with or without anosmia, HH21; FLRT3/fibronectin leucine-rich transmembrane protein 3; OMIM 615271)** covering all of the
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


# FLRT3-Related Hypogonadotropic Hypogonadism (HH21): Research Report

## Executive assessment

**Hypogonadotropic hypogonadism 21 with or without anosmia (HH21)** is a catalogued congenital GnRH-deficiency disorder historically attributed to heterozygous variation in **FLRT3**, a neural cell-adhesion and guidance gene. Its defining clinical phenotype is congenital hypogonadotropic hypogonadism (CHH)—low sex steroids with low or inappropriately normal gonadotropins—sometimes accompanied by anosmia/hyposmia, in which case it lies within the Kallmann-syndrome spectrum.

The most important contemporary qualification is that **the FLRT3–HH21 relationship remains weakly supported compared with established CHH genes**. Open Targets links MONDO:0014107 to four ClinVar/EVA records, principally citing **PMID 23643382**, but labels the records “no assertion criteria provided”; accessible evidence did not supply exact variants, segregation, population frequencies, or variant-specific functional studies. A 2023 clinical review of the UK NHS panel framework lists FLRT3 among low/moderate-evidence genes that are not part of the 14 clinically reportable “green” genes. Accordingly, HH21 should be represented as a **provisional/limited-evidence Mendelian gene–disease association**, not as equivalent in validity to ANOS1, FGFR1, CHD7, GNRHR, or PROKR2 disease. (OpenTargets Search: hypogonadotropic hypogonadism 21 with or without anosmia-FLRT3, sayed2023paneltestingfor pages 1-2, sayed2023paneltestingfor pages 3-5)

The following table gives a compact evidence-grade summary.

| Domain | Best-supported finding | Evidence type and strength | Knowledge-base ontology suggestions | Key caveat |
|---|---|---|---|---|
| Identifiers | HH21 is catalogued as **hypogonadotropic hypogonadism 21 with or without anosmia**, associated with **FLRT3**: OMIM disease **615271**, MONDO **MONDO:0014107**, and Ensembl gene **ENSG00000125848**. (OpenTargets Search: hypogonadotropic hypogonadism 21 with or without anosmia-FLRT3) | **Direct database association; limited-to-moderate evidence.** Open Targets aggregates four ClinVar or EVA records principally linked to PMID 23643382. | MONDO:0014107; parent MONDO:0018555; FLRT3 | Disease-specific ICD-10, ICD-11, MeSH, and Orphanet identifiers were not established in the retrieved evidence; broader hypogonadotropic-hypogonadism codes may be required. |
| Gene validity | FLRT3 has a historical human association with HH21, but a 2023 review of the NHS panel framework places it among genes with insufficient evidence for routine clinical reporting rather than among the 14 clinically reportable green genes. (sayed2023paneltestingfor pages 1-2, sayed2023paneltestingfor pages 3-5) | **Direct human reports with limited replication; weak-to-moderate clinical validity.** No recent independent case series or definitive segregation and functional validation was retrieved. | Gene–disease association; ACMG/AMP evidence codes after variant-level reassessment | An OMIM disease number does not establish definitive contemporary validity. Exact variants, segregation, penetrance, functional results, and population frequencies could not be recovered from the available source text. |
| Phenotype | Expected manifestations are congenital GnRH deficiency, low sex steroids with low or inappropriately normal LH and FSH, absent or arrested puberty, and infertility. Anosmia or hyposmia may occur but is not obligatory; neonatal male clues include micropenis and cryptorchidism. (howard2024outcomesandexperiences pages 1-2, sayed2023paneltestingfor pages 1-2, rohayem2024minipubertyphysiologicaland pages 1-2, topaloglu2021geneticetiologyof pages 1-3) | **General-CHH extrapolation; strong syndrome-level evidence but not FLRT3-specific.** | HP:0000044 Hypogonadotropic hypogonadism; HP:0000823 Delayed puberty; HP:0000786 Primary amenorrhea; HP:0000027 Azoospermia; HP:0000054 Micropenis; HP:0000028 Cryptorchidism; HP:0000458 Anosmia; HP:0004409 Hyposmia | FLRT3-specific phenotype frequencies, sex distribution, severity, nonreproductive manifestations, and genotype–phenotype correlations are unknown. |
| Mechanism | FLRT3 is a single-pass cell-surface adhesion and guidance protein containing 10 leucine-rich repeats and an FNIII domain. Models support homophilic adhesion, shed-FLRT–UNC5 repulsion, Rnd-dependent cadherin regulation, and enhancement of FGF–ERK/MAPK signaling. Altered olfactory or GnRH-lineage guidance is a plausible route to HH21. (nagel2015analysisofadhesive pages 36-41, hampel2012functionalanalysisof pages 48-52, xiaofen2019localizationandfunction pages 43-48) | **Direct FLRT3 molecular and model evidence; indirect disease mechanism.** Adhesion, repulsion, and neural migration functions are demonstrated, but the FLRT3-to-GnRH-to-HH21 chain is inferred. | GO:0007155 cell adhesion; GO:0001764 neuron migration; GO:0007411 axon guidance; GO:0000165 MAPK cascade; GO:0005886 plasma membrane; CL:0000540 neuron | No retrieved experiment demonstrated defective GnRH-neuron development caused by a human HH21 variant. Immune, metabolic, tissue-necrosis, and disease-specific epigenetic mechanisms remain unsupported. |
| Anatomy | Inferred primary sites are the embryonic nasal and olfactory placode, GnRH migratory pathway, forebrain and hypothalamus, pituitary gonadotropes, and downstream gonads. Olfactory bulb or sulcus abnormalities may accompany Kallmann-spectrum disease. (cho2019nasalplacodedevelopment pages 1-2, millar2021geneticsofhypogonadotropic pages 1-2) | **General developmental-neuroendocrine evidence; indirect for FLRT3.** | UBERON:0000004 nose; UBERON:0005725 olfactory epithelium; UBERON:0002264 olfactory bulb; UBERON:0001898 hypothalamus; UBERON:0000007 pituitary gland; UBERON:0000473 testis; UBERON:0000992 ovary | Direct localization of pathogenic FLRT3 effects in human olfactory or GnRH tissue has not been demonstrated; characteristic lateralization is not reported. |
| Diagnostics | Evaluate pubertal development, morning sex steroids, LH and FSH, other pituitary hormones, formal olfaction, and pituitary or olfactory anatomy by MRI when indicated. Multigene NGS, exome, or genome analysis is preferable to isolated FLRT3 testing because CHH is genetically heterogeneous and can be oligogenic. (howard2024outcomesandexperiences pages 1-2, sayed2023paneltestingfor pages 1-2, millar2021geneticsofhypogonadotropic pages 1-2, topaloglu2021geneticetiologyof pages 1-3) | **General-CHH clinical evidence; strong. FLRT3 result interpretation remains uncertain.** | Relevant HPO terms; LOINC concepts for LH, FSH, testosterone, estradiol, inhibin B, and AMH; NCIT:C16809 magnetic resonance imaging; NCIT:C17147 genetic testing | A heterozygous FLRT3 VUS alone should not establish HH21. Confirm candidate variants, evaluate segregation and population frequency, and assess established CHH genes and copy-number variants. |
| Treatment | Management is phenotype-based: gradual testosterone induction or replacement in males; estradiol followed by cyclic progestogen in females; pulsatile GnRH or hCG plus FSH for fertility; and orchidopexy for cryptorchidism. Infant mini-puberty replacement remains specialist-led. (sayed2023paneltestingfor pages 1-2, rohayem2024minipubertyphysiologicaland pages 1-2, rohayem2024minipubertyphysiologicaland pages 19-20, rohayem2024minipubertyphysiologicaland pages 22-23, rohayem2024minipubertyphysiologicaland pages 10-11) | **General-CHH evidence; moderate-to-strong. No FLRT3-specific treatment evidence.** Approximately 75% fertility restoration is reported across treated CHH populations; orchidopexy success is about 90%. | NCIT:C2300 testosterone; NCIT:C483 estradiol; NCIT:C2302 progesterone; NCIT:C644 human chorionic gonadotropin; NCIT:C717 follicle-stimulating hormone; NCIT:C614 gonadotropin-releasing hormone; NCIT:C15218 orchidopexy | No approved FLRT3-targeted drug, gene therapy, RNA therapy, cell therapy, immunotherapy, or genotype-guided pharmacogenomic strategy exists. Treatment outcomes cannot be assumed to differ by FLRT3 genotype. |
| Epidemiology and course | CHH overall is estimated at approximately 1 per 15,000–50,000 people, with a male-to-female ratio near 3.6:1. Finnish Kallmann estimates are about 1 per 30,000 males and 1 per 125,000 females. Approximately 10–20% of IHH cases may recover axis function, sometimes followed by relapse. (sayed2023paneltestingfor pages 1-2, abacı2024acurrentperspective pages 1-2, topaloglu2021geneticetiologyof pages 1-3) | **General-CHH epidemiology; moderate evidence. No HH21-specific denominator.** | Rare-disease classification; HP:0003674 Onset in adolescence; HP:0003581 Adult onset for uncommon later presentations | No reliable FLRT3-HH21 prevalence, incidence, carrier frequency, penetrance, founder effect, ancestry distribution, survival, or mortality estimate is available. |
| Models | Flrt3-null mice exhibit early morphogenetic abnormalities and embryonic lethality. Neural studies support migration and repulsion functions, while combined Flrt2 and Flrt3 deletion disrupts cortical interneuron streams through UNC5-related signaling. (fleitas2021flrt2andflrt3 pages 1-2, nagel2015analysisofadhesive pages 36-41, hampel2012functionalanalysisof pages 108-111, hampel2012functionalanalysisof pages 48-52) | **Direct model-organism and in-vitro FLRT biology; moderate mechanistic evidence.** | NCBI Taxon:10090 Mus musculus; GO:0001764 neuron migration; GO:0007411 axon guidance; CL:0000099 interneuron | No model directly reproduces GnRH deficiency, pubertal failure or infertility, and optional anosmia together. FLRT-family redundancy and early lethality complicate interpretation. |
| Omics and advanced technologies | No HH21-specific transcriptomic, single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, methylomic, multi-omic, organoid, iPSC, or CRISPR-screen signature was identified. | **Evidence absent.** | CL:0000540 neuron; GO:0010468 regulation of gene expression; relevant EFO terms for single-cell RNA sequencing and spatial transcriptomics | General tissue-expression and cortical-development findings should not be represented as an HH21 molecular profile without variant-specific patient or engineered-model evidence. |


*Table: Compact assessment of FLRT3-related HH21 across identifiers, validity, clinical features, mechanism, diagnostics, management, epidemiology, and models. It distinguishes direct FLRT3 evidence from broader CHH extrapolation.*

## 1. Disease information

### Definition and identifiers

- **Preferred name:** hypogonadotropic hypogonadism 21 with or without anosmia.
- **Synonyms:** HH21; FLRT3-related hypogonadotropic hypogonadism; FLRT3-related congenital hypogonadotropic hypogonadism; FLRT3-related isolated GnRH deficiency; FLRT3-related Kallmann syndrome when olfactory dysfunction is present.
- **Disease OMIM:** **615271**.
- **MONDO:** **MONDO:0014107**.
- **Gene:** **FLRT3**, fibronectin leucine-rich transmembrane protein 3; OMIM gene **604808**; Ensembl **ENSG00000125848**; cytogenetic location **20p12.1**. (OpenTargets Search: hypogonadotropic hypogonadism 21 with or without anosmia-FLRT3, sayed2023paneltestingfor pages 1-2, sayed2023paneltestingfor pages 3-5)
- **Parent concepts:** congenital/isolated hypogonadotropic hypogonadism and Kallmann syndrome. CHH is defined by deficient GnRH secretion or action, producing low gonadal steroids and deficient pituitary gonadotropin output; Kallmann syndrome denotes CHH accompanied by hyposmia or anosmia. (cho2019nasalplacodedevelopment pages 1-2, sayed2023paneltestingfor pages 1-2, topaloglu2021geneticetiologyof pages 1-3)
- **Orphanet, MeSH, ICD-10 and ICD-11:** no FLRT3-specific identifier was established in the retrieved evidence. Broader coding generally uses hypogonadotropic hypogonadism, other testicular/ovarian dysfunction, delayed puberty, infertility, or Kallmann syndrome concepts. A knowledge base should not invent an HH21-specific ICD or Orphanet code.

This report integrates **aggregated disease-level resources**, published CHH cohorts and reviews, molecular/model experiments, and clinical-trial records. It does **not** derive from patient EHRs. Direct FLRT3 patient-level evidence is sparse and largely traces to the 2013 report indexed as PMID 23643382 and associated ClinVar records. (OpenTargets Search: hypogonadotropic hypogonadism 21 with or without anosmia-FLRT3)

## 2. Etiology, risk and protective factors

### Causal factor

The proposed initiating lesion is a **germline FLRT3 variant**, historically interpreted as autosomal dominant. However, present evidence is insufficient to state that every rare damaging FLRT3 allele is causal. CHH frequently shows incomplete penetrance, variable expressivity, and di-/oligogenic inheritance; over 40 genes are recognized as causing or contributing to CHH, and fewer than half of patients in many series receive a molecular diagnosis. (sayed2023paneltestingfor pages 1-2, millar2021geneticsofhypogonadotropic pages 1-2, topaloglu2021geneticetiologyof pages 1-3)

Open Targets also associates **MACROD2** with HH21 through the same four records, but the retrieved evidence does not establish whether this reflects linkage, overlapping variation, a contiguous event, or an independent causal role. MACROD2 should therefore not be asserted as an HH21 modifier without inspecting the original cases. (OpenTargets Search: hypogonadotropic hypogonadism 21 with or without anosmia-FLRT3)

### Risk factors

- **Genetic:** a convincingly pathogenic FLRT3 allele with phenotype concordance and segregation is the proposed risk factor. Additional CHH-gene variants could modify penetrance or severity, but no specific FLRT3 modifier pair has been validated.
- **Family history:** delayed/absent puberty, infertility, anosmia, micropenis, cryptorchidism, or known CHH increases suspicion.
- **Sex:** CHH overall is diagnosed more often in males, partly because neonatal genital signs and absent testicular enlargement are conspicuous. A 2023 review estimates a male:female ratio of approximately **3.6:1**; this is not FLRT3-specific. (sayed2023paneltestingfor pages 1-2)
- **Environmental/acquired:** no toxin, lifestyle exposure, radiation, occupation, or infectious agent is established as a cause of FLRT3-HH21. Caloric deficit, excessive exercise, severe illness, stress, opioids, glucocorticoids, pituitary disease and iron overload can suppress the HPG axis, but these are differential causes of acquired/functional HH rather than causes of a congenital FLRT3 disorder. (abacı2024acurrentperspective pages 1-2, millar2021geneticsofhypogonadotropic pages 1-2)

### Protective factors and gene–environment interaction

No genetic or environmental protective factor has been demonstrated for HH21. Healthy nutrition, adequate energy availability and avoidance of suppressive drugs may prevent superimposed functional HPG suppression but cannot correct a developmental FLRT3 lesion. A specific FLRT3-by-environment interaction has not been reported. No vaccine or infectious prophylaxis is relevant.

## 3. Phenotypes

Because FLRT3-specific frequencies are unavailable, the entries below are **CHH-spectrum expectations**, not measured HH21 penetrance estimates.

| Phenotype | Type, onset and course | Suggested HPO term |
|---|---|---|
| Hypogonadotropic hypogonadism | Laboratory/endocrine abnormality; congenital, recognized in infancy or adolescence; usually persistent but variable | **HP:0000044** |
| Delayed, absent or arrested puberty | Clinical sign; usually evident by age 13 in girls or 14 in boys; severity ranges from partial arrest to complete absence | **HP:0000823**, delayed puberty |
| Low LH/FSH with low testosterone or estradiol | Laboratory pattern; stable without treatment | Low circulating gonadotropins/sex steroids; use local HPO/LOINC mappings |
| Micropenis | Congenital physical sign in severely affected 46,XY infants | **HP:0000054** |
| Cryptorchidism | Congenital sign, unilateral or bilateral; may persist and compromise fertility | **HP:0000028** |
| Small testes/testicular hypoplasia | Physical sign from absent fetal/infant gonadotropin action | **HP:0008734** or current HPO equivalent |
| Primary amenorrhea/absent breast development | Adolescent female reproductive manifestations | **HP:0000786**, **HP:0000769** |
| Azoospermia/oligozoospermia and infertility | Adult laboratory/functional outcomes | **HP:0000027**, **HP:0000798** |
| Anosmia or hyposmia | Congenital, usually nonprogressive sensory deficit; optional in HH21 | **HP:0000458**, **HP:0004409** |
| Reduced libido, energy or sexual function | Adolescent/adult symptom secondary to sex-steroid deficiency | Relevant HPO sexual-function/fatigue terms |
| Low bone mineral density | Secondary complication of delayed or untreated sex-steroid deficiency | **HP:0004349** |

Normal puberty begins between approximately **8–13 years in girls and 9–14 years in boys**. Delayed puberty is conventionally failure to initiate by age 13 or 14, respectively, or failure to complete by approximately 15–16 years in girls and 16–17 years in boys. About one-third of CHH patients may enter Tanner stage 2–3 and then arrest, illustrating that partial puberty does not exclude disease. (howard2024outcomesandexperiences pages 1-2)

Severe CHH abolishes fetal, infant “mini-puberty,” and adolescent HPG activation. A 2024 Endocrine Reviews article states that fetal deficiency manifests as micropenis and/or cryptorchidism in **around 50% of affected male newborns**; absent mini-puberty reduces Sertoli-cell expansion and later reproductive capacity. This percentage is disease-wide, not FLRT3-specific. (rohayem2024minipubertyphysiologicaland pages 1-2)

### Quality of life

Untreated delayed puberty and hypogonadism can cause negative self-image, anxiety, depression, isolation, low energy, impaired sexual well-being, reduced bone density and infertility. Recent expert commentary emphasizes long diagnostic journeys, nonstandardized care, and adverse consequences of late or incorrect pubertal induction. No HH21-specific EQ-5D, SF-36 or PROMIS study was found. (howard2024outcomesandexperiences pages 1-2, rohayem2024minipubertyphysiologicaland pages 1-2, rohayem2024minipubertyphysiologicaland pages 10-11)

## 4. Genetic and molecular information

### Causal gene and protein

**FLRT3** encodes a type-I, single-pass plasma-membrane protein. Its extracellular portion contains ten leucine-rich repeats, cysteine-rich caps and a fibronectin type-III domain; a metalloprotease-sensitive region permits ectodomain shedding, and its short cytoplasmic tail contains conserved residues involved in Rnd-family binding and signaling. (nagel2015analysisofadhesive pages 36-41, hampel2012functionalanalysisof pages 48-52, xiaofen2019localizationandfunction pages 43-48)

Suggested annotations include **GO:0005886 plasma membrane**, **GO:0007155 cell adhesion**, **GO:0007411 axon guidance**, **GO:0001764 neuron migration**, and **GO:0000165 MAPK cascade**.

### Pathogenic variants and classification

Four ClinVar/EVA records associated with FLRT3 and MONDO:0014107 are described as missense consequences and cite PMID 23643382. However, the retrieved records did not expose HGVS expressions, zygosity, segregation, allele frequencies, patient phenotypes or functional assays, and explicitly reported “no assertion criteria provided.” Consequently:

1. No exact FLRT3 allele can be responsibly listed here as pathogenic/likely pathogenic.
2. Population frequency in gnomAD, TOPMed, ExAC or 1000 Genomes cannot be stated without the HGVS alleles.
3. Germline origin is expected for congenital disease, but de novo versus inherited status was not recovered.
4. Loss-of-function, gain-of-function or dominant-negative action has not been established for an HH21 allele.
5. A rare FLRT3 VUS is **not** diagnostic on its own. (OpenTargets Search: hypogonadotropic hypogonadism 21 with or without anosmia-FLRT3)

No validated FLRT3 modifier gene, protective allele, founder mutation, germline-mosaicism series, somatic disease mechanism, repeat expansion, aneuploidy or recurrent FLRT3 structural rearrangement was identified. No disease-specific DNA methylation, histone or chromatin signature was found.

### Clinical validity interpretation

The 2023 NHS-oriented review describes a 14-gene clinically reportable panel—ANOS1, CHD7, FGF8, FGFR1, FSHB, GNRHR, IL17RD, KISS1R, LHB, PROK2, PROKR2, TAC3, TACR3 and WDR11. FLRT3 appears outside this high-confidence group among genes assigned lower evidence ratings, for which variants are maintained for research rather than routinely returned. This authoritative expert appraisal is a major reason to classify HH21 cautiously. (sayed2023paneltestingfor pages 1-2, sayed2023paneltestingfor pages 3-5)

## 5. Environmental information

No environmental, lifestyle or infectious trigger is known for FLRT3-HH21. Environmental and behavioral factors are clinically important mainly because functional hypothalamic suppression from malnutrition, intense exercise, psychosocial stress, chronic disease or medications can phenocopy or compound CHH. Endocrine-disrupting chemicals affect pubertal timing generally, but no FLRT3-specific interaction has been demonstrated. (abacı2024acurrentperspective pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A putatively damaging germline FLRT3 variant leads to altered FLRT3 abundance, structure or signaling**—the molecular consequence of actual HH21 variants remains unproven.
2. **Altered FLRT3 leads to disturbed balance between homophilic cell adhesion and FLRT–UNC5-mediated repulsion**, and may alter Rnd/cadherin trafficking and FGF–ERK/MAPK signaling; these functions are demonstrated in cellular and animal developmental systems. (nagel2015analysisofadhesive pages 36-41, hampel2012functionalanalysisof pages 48-52)
3. **Disturbed adhesion/guidance leads to abnormal neuronal migration or axon organization**; this is demonstrated for cortical populations, but its extension to human GnRH and olfactory lineages is **inferred**. (fleitas2021flrt2andflrt3 pages 1-2, nagel2015analysisofadhesive pages 86-92)
4. **Inferred branch A:** abnormal olfactory development leads to hyposmia/anosmia and possible olfactory bulb/sulcus hypoplasia.
5. **Inferred branch B:** impaired migration, positioning or connectivity of embryonic GnRH neurons leads to deficient hypothalamic pulsatile GnRH release. Normal GnRH neurons originate in the nasal placode and migrate along olfactory-derived/terminal-nerve pathways into the forebrain and hypothalamus. (cho2019nasalplacodedevelopment pages 1-2, millar2021geneticsofhypogonadotropic pages 1-2)
6. **GnRH deficiency leads to low or inappropriately normal LH and FSH**, while other pituitary axes are generally preserved.
7. **Low LH/FSH leads to deficient fetal, mini-pubertal and adolescent gonadal steroidogenesis and impaired Sertoli/granulosa support.**
8. **Sex-steroid and gonadal maturation failure results in micropenis/cryptorchidism in severe males, delayed or arrested puberty, amenorrhea or impaired virilization, reduced bone accrual and infertility.** (sayed2023paneltestingfor pages 1-2, rohayem2024minipubertyphysiologicaland pages 1-2)

### Molecular and cellular detail

FLRT3 can mediate calcium-dependent homophilic adhesion, bind UNC5-family receptors through its LRR region, and after ectodomain shedding act as a chemorepellent. Model experiments also connect FLRT3 to FGFR1/ERK1/2 signaling and to Rnd1-dependent cadherin internalization. FLRT3 overexpression inhibits cortical radial migration, while disrupting homophilic binding or deleting its intracellular domain partially rescues migration. Double deletion of **Flrt2/Flrt3** in mouse embryos disrupts cortical interneuron streams; UNC5B/UNC5D mutants show related defects, and FLRT proteins repel developing interneurons in vitro. (fleitas2021flrt2andflrt3 pages 1-2, nagel2015analysisofadhesive pages 86-92, nagel2015analysisofadhesive pages 104-108, hampel2012functionalanalysisof pages 48-52)

These findings establish FLRT3 as a credible developmental guidance molecule but **do not demonstrate an HH21 variant disrupting GnRH neurons**. Moreover, nervous-system-specific Flrt3 ablation did not produce gross brain, cortical-layer or major tract abnormalities in some analyses, suggesting redundancy, subtle phenotypes, or context dependence. (hampel2012functionalanalysisof pages 108-111)

Suggested process terms: **GO:0001764 neuron migration; GO:0007411 axon guidance; GO:0007155 cell adhesion; GO:0023052 signaling; GO:0000165 MAPK cascade; GO:0030154 cell differentiation; GO:0050804 modulation of chemical synaptic transmission**. Suggested cell terms include **CL:0000540 neuron**, **CL:0000099 interneuron**, **CL:0000122 GnRH neuron** if available in the target ontology, **CL:0000163 endocrine cell**, **pituitary gonadotroph**, **Leydig cell**, **Sertoli cell**, **granulosa cell**, and **olfactory sensory neuron**.

No disease-specific inflammatory, autoimmune, oxidative, ischemic, fibrotic, necrotic, mitochondrial, metabolic, proteostatic or ion-channel mechanism is supported. Likewise, no HH21-specific transcriptomic, single-cell, spatial, proteomic, metabolomic, lipidomic, epigenomic, organoid, iPSC, multi-omic or CRISPR-screen dataset was identified.

## 7. Anatomical structures affected

- **Primary developmental system:** nasal/olfactory placode and GnRH migratory route; suggested **UBERON:0000004 nose**, olfactory epithelium, terminal nerve and cribriform region.
- **Central nervous system:** olfactory bulb (**UBERON:0002264**), forebrain, preoptic area, arcuate region and hypothalamus (**UBERON:0001898**).
- **Endocrine relay:** anterior pituitary (**UBERON:0000007**) gonadotrophs; usually structurally normal in isolated CHH.
- **Secondary target organs:** testis (**UBERON:0000473**), ovary (**UBERON:0000992**), uterus, external genitalia and skeleton.
- **Subcellular:** plasma membrane, shed extracellular ectodomain, cytoplasmic signaling/trafficking machinery; suggested **GO:0005886**, **GO:0005576 extracellular region**, **GO:0031982 vesicle**.

No consistent lateralization is known. Cryptorchidism may be unilateral or bilateral, and olfactory bulb abnormalities may vary, but this is not FLRT3-specific. (cho2019nasalplacodedevelopment pages 1-2, millar2021geneticsofhypogonadotropic pages 1-2)

## 8. Temporal development

The initiating defect is presumed **embryonic**, during olfactory/GnRH system development. In males with severe deficiency, fetal signs include micropenis or undescended testes, and absence of postnatal mini-puberty accentuates testicular immaturity. Most patients are recognized in adolescence because puberty fails to begin or arrests; some are first diagnosed in adulthood during infertility evaluation or after reduced libido, energy or bone density. (sayed2023paneltestingfor pages 1-2, rohayem2024minipubertyphysiologicaland pages 1-2)

Untreated disease is chronic. Sex-steroid replacement induces secondary sexual characteristics but does not prove recovery of endogenous GnRH function. CHH overall shows reversal in approximately **10–20%**, and relapse may occur; there are no FLRT3-specific reversal data. (topaloglu2021geneticetiologyof pages 1-3, kulvinder2016idiopathichypogonadotropichypogonadism— pages 12-14)

Critical intervention windows are infancy for recognition of mini-puberty failure and cryptorchidism, normal pubertal age for physiological induction and psychosocial/bone health, and reproductive adulthood for fertility induction. (howard2024outcomesandexperiences pages 1-2, rohayem2024minipubertyphysiologicaland pages 1-2)

## 9. Inheritance and population

HH21 has historically been represented as **autosomal dominant**, but penetrance, expressivity and monogenic sufficiency are not adequately quantified. CHH in general can be autosomal dominant, autosomal recessive, X-linked or oligogenic, with incomplete penetrance and variable expression. Oligogenic estimates vary widely—from older estimates around 10–20% to as high as 70% in selected sequencing studies—reflecting cohort and classification differences. (sayed2023paneltestingfor pages 1-2, topaloglu2021geneticetiologyof pages 1-3)

No HH21-specific prevalence, incidence, carrier frequency, founder effect, ancestry enrichment, geographic distribution, consanguinity effect or sex ratio is available. For context only, CHH overall has an estimated incidence of approximately **1:15,000–50,000** and male:female ratio near **3.6:1**. Finnish estimates for Kallmann syndrome are approximately **1:30,000 males** and **1:125,000 females**; a 2024 review stresses that no definitive epidemiological investigation exists. (sayed2023paneltestingfor pages 1-2, abacı2024acurrentperspective pages 1-2, millar2021geneticsofhypogonadotropic pages 1-2)

No anticipation or established germline mosaicism has been reported.

## 10. Diagnostics

### Clinical and laboratory approach

1. Document growth, Tanner stage, testicular volume, genital development, menstrual history, libido, fertility and family history.
2. Seek red flags: micropenis, bilateral cryptorchidism, anosmia/hyposmia, cleft palate, hearing loss, dental agenesis, renal anomalies, synkinesia or broader neurodevelopmental findings. These associated anomalies may point toward alternative CHH genes. (howard2024outcomesandexperiences pages 1-2, millar2021geneticsofhypogonadotropic pages 1-2)
3. Measure morning testosterone in males or estradiol in females with LH and FSH. CHH shows low steroids with low/inappropriately normal gonadotropins.
4. Assess prolactin, thyroid function, cortisol/ACTH and IGF-1 as indicated to exclude combined pituitary disease; add ferritin/iron studies and general tests for chronic illness.
5. Inhibin B and AMH can support severe gonadotropin deficiency, but neither reliably distinguishes CHH from self-limited delayed puberty. GnRH, hCG and other stimulation tests have limited discriminatory power. (howard2024outcomesandexperiences pages 1-2, sayed2023paneltestingfor pages 1-2, vezzoli2023geneticarchitectureof pages 2-3)
6. Perform standardized olfactory testing rather than relying only on self-report.
7. Obtain MRI of the hypothalamic-pituitary region when acquired/structural disease is possible and evaluate olfactory bulbs/sulci when Kallmann syndrome is suspected.
8. Semen analysis assesses adult male fertility; pelvic ultrasound can assess uterine/ovarian maturation; bone-age radiography and DXA may quantify maturational delay and skeletal morbidity.

### Genetic testing

A comprehensive CHH/Kallmann multigene panel with deletion/duplication analysis is preferable to FLRT3-only testing. WES or WGS is appropriate for panel-negative, syndromic, atypical or familial cases; genome sequencing can improve detection of structural and noncoding variants. CHH’s oligogenic architecture requires analysis beyond one candidate gene. (sayed2023paneltestingfor pages 1-2, millar2021geneticsofhypogonadotropic pages 1-2, topaloglu2021geneticetiologyof pages 1-3)

For a candidate FLRT3 finding:

- confirm by an orthogonal method;
- review transcript and HGVS nomenclature;
- assess gnomAD/TOPMed frequency and regional constraint;
- perform parental and extended-family segregation;
- search for pathogenic variants/CNVs in established CHH genes;
- classify using ACMG/AMP criteria without treating phenotype match or OMIM inclusion as sufficient evidence;
- retain as VUS where functional/segregation evidence is inadequate.

CMA, karyotype and FISH are not first-line for isolated HH21 but are appropriate for multiple congenital anomalies or suspected chromosomal disease. Mitochondrial and repeat-expansion testing are not routinely indicated. No validated RNA-seq, proteomic, metabolomic, methylation or liquid-biopsy diagnostic exists.

### Differential diagnosis

Key alternatives are self-limited delayed puberty; functional hypothalamic suppression; pituitary/hypothalamic tumor or infiltrative disease; hyperprolactinemia; hemochromatosis; medication-induced HH; combined pituitary hormone deficiency; CHARGE and other syndromic CHH; primary gonadal failure, which instead raises LH/FSH; and other established monogenic CHH forms. CDGP accounts for approximately **60% of delayed puberty in boys and 30% in girls** in a 2024 review, making longitudinal assessment and genetic interpretation important. (abacı2024acurrentperspective pages 1-2)

### Screening

HH21 is not included in newborn population screening. Targeted early evaluation is justified in male infants with micropenis and/or bilateral cryptorchidism and in relatives of a person with a convincingly pathogenic familial variant. Cascade testing should not be predictive when the familial allele remains a VUS.

## 11. Outcome and prognosis

CHH is generally compatible with normal life expectancy, and no disease-specific mortality signal is established. No HH21 survival, mortality or life-expectancy cohort exists. Major morbidity arises from absent puberty, infertility, sexual dysfunction, low bone density, unfavorable body composition and psychosocial distress. (rohayem2024minipubertyphysiologicaland pages 1-2, rohayem2024minipubertyphysiologicaland pages 10-11)

Sex-steroid replacement usually induces and maintains secondary sexual characteristics. Fertility is often achievable because the gonads can respond to GnRH or gonadotropins; the 2023 clinical review reports restoration in approximately **75%** of treated CHH patients overall. Poorer male fertility predictors include cryptorchidism, very small pretreatment testes, absent prior sexual maturation and low inhibin B. (sayed2023paneltestingfor pages 1-2, kulvinder2016idiopathichypogonadotropichypogonadism— pages 12-14)

Endogenous HPG recovery occurs in a minority and can relapse, so supervised treatment withdrawal and lifelong reassessment are appropriate. No FLRT3 genotype-specific prognostic biomarker exists. (topaloglu2021geneticetiologyof pages 1-3, kulvinder2016idiopathichypogonadotropichypogonadism— pages 12-14)

## 12. Treatment and current implementation

No treatment targets FLRT3 itself; management follows CHH/Kallmann practice.

### Puberty and maintenance

- **Males:** gradually escalating testosterone induces virilization, penile growth, muscle mass, bone accrual, libido and sexual function. Suggested NCIT concept: **Testosterone (NCIT:C2300)**. Testosterone does not induce spermatogenesis and suppresses intratesticular gonadotropin-dependent function.
- **Females:** low-dose estradiol, slowly escalated, induces breast and uterine development; cyclic progesterone is added after adequate estrogenization or breakthrough bleeding. Suggested terms: **Estradiol (NCIT:C483)** and **Progesterone (NCIT:C2302)**. (abacı2024acurrentperspective pages 1-2, rohayem2024minipubertyphysiologicaland pages 10-11)
- Monitor growth and bone age during induction, clinical pubertal progression, testosterone/estradiol, hematocrit and prostate-related parameters where age-appropriate, blood pressure/metabolic health, menstrual response, bone density, adherence and psychosocial well-being.

### Fertility induction

- **Pulsatile GnRH** can restore physiological LH/FSH secretion when pituitary gonadotroph function is intact; suggested **NCIT:C614**.
- **Men:** hCG, commonly combined sequentially or concurrently with recombinant FSH, stimulates Leydig-cell testosterone production and Sertoli-cell/spermatogenic maturation; suggested **NCIT:C644** and **NCIT:C717**. FSH priming may help men with severe CHH and very small testes. (millar2021geneticsofhypogonadotropic pages 1-2, rohayem2024minipubertyphysiologicaland pages 19-20, NCT00064987 chunk 2)
- **Women:** pulsatile GnRH or exogenous gonadotropins can induce follicular maturation and ovulation, with ultrasound and estradiol monitoring to limit multiple pregnancy and ovarian hyperstimulation.

Disease-wide trials include **NCT00064987** (FSH pretreatment before GnRH-induced fertility), **NCT02880280** (hMG plus hCG), **NCT01403532** (sequential therapy), **NCT03687606** (long-term hCG versus hCG+hMG), and **NCT00392756** (IHH/Kallmann natural-history/interventional program). None is FLRT3-stratified. (NCT00392756 chunk 3, NCT00064987 chunk 2)

### Infancy and surgery

Short-course low-dose testosterone or topical DHT can treat micropenis but does not expand Sertoli cells or promote testicular descent. Physiological gonadotropin replacement during mini-puberty may increase penile and testicular size and support descent, but evidence comes from small case series; 2022 Endo-ERN guidance did not recommend routine use, and long-term fertility benefit remains uncertain. Reported adverse effects include injection pain, irritation, scarring, lipohypertrophy, rare abscess/blistering, gynecomastia, increased estradiol and rare anti-hCG antibodies. (rohayem2024minipubertyphysiologicaland pages 19-20, rohayem2024minipubertyphysiologicaland pages 22-23)

Orchidopexy is recommended at approximately 6–12 months for congenital cryptorchidism. Disease-wide data cited in the 2024 review indicate roughly **90% surgical success** and approximately **2% testicular atrophy**; hormonal descent produces only about 15% final success after re-ascent. Suggested intervention term: **NCIT:C15218 Orchidopexy**. (rohayem2024minipubertyphysiologicaland pages 19-20)

### Advanced and experimental therapy

No FLRT3-directed small molecule, gene replacement/editing, ASO, siRNA, mRNA, cell therapy, immunotherapy or validated pharmacogenomic algorithm exists. Kisspeptin and neurokinin-B biology is an active reproductive-neuroendocrine research area, but there is no evidence that these approaches correct a developmental FLRT3 lesion.

## 13. Prevention

Primary prevention of a de novo or inherited developmental allele is not possible through lifestyle or vaccination. Appropriate measures are:

- **Secondary prevention:** early recognition of micropenis, bilateral cryptorchidism, anosmia and pubertal arrest; timely endocrine referral; family cascade evaluation for a proven pathogenic allele.
- **Tertiary prevention:** timely physiological puberty induction, bone-health monitoring, fertility-preserving treatment, orchidopexy, and psychological/sexual-health support.
- **Reproductive counseling:** discuss uncertain penetrance and gene validity; once a familial pathogenic allele is firmly established, prenatal diagnosis or PGT-M may be technically possible. These options should not be based on an unresolved VUS.

No population carrier screening, newborn biochemical screening, public-health environmental intervention or prophylactic medication is indicated.

## 14. Other species and natural disease

The principal comparative species is **Mus musculus**, NCBI Taxon **10090**, carrying the ortholog **Flrt3**. No naturally occurring veterinary syndrome equivalent to FLRT3-HH21 was identified, and no breed-specific VBO association is established. There is no infectious transmission, zoonotic potential or cross-species contagion.

FLRT adhesion/guidance biology is evolutionarily conserved and has also been studied in Xenopus embryos and cultured mammalian cells. These systems illuminate morphogenesis and signaling but do not constitute natural HH21 disease. (nagel2015analysisofadhesive pages 36-41, hampel2012functionalanalysisof pages 48-52)

## 15. Model organisms

### Available systems

- **Conventional Flrt3-null mouse:** early morphogenetic defects, including ventral closure/headfold and endoderm abnormalities, with embryonic lethality around E10.5; useful for morphogenesis but poorly suited to postnatal reproductive phenotyping. (nagel2015analysisofadhesive pages 36-41, hampel2012functionalanalysisof pages 48-52)
- **Conditional nervous-system Flrt3 deletion:** no gross brain, cortical-layer or major tract defect in reported analyses, suggesting subtle functions or redundancy. (hampel2012functionalanalysisof pages 108-111)
- **Flrt2/Flrt3 double conditional deletion:** abnormal cortical interneuron-stream distribution and altered postnatal somatostatin-interneuron layering; mechanistically linked to UNC5-dependent repulsion. This is direct neuronal-migration evidence, not a GnRH model. (fleitas2021flrt2andflrt3 pages 1-2)
- **Embryonic cortical electroporation/overexpression:** FLRT3 overexpression retains neurons in the intermediate zone; homophilic-binding and intracellular-domain mutants partly rescue migration. (nagel2015analysisofadhesive pages 86-92, nagel2015analysisofadhesive pages 104-108)
- **Cell, neuronal-culture and Xenopus assays:** useful for FLRT3–FGFR1, FLRT3–UNC5, Rnd/cadherin, adhesion, ectodomain shedding, repulsion and neurite studies. (nagel2015analysisofadhesive pages 36-41, hampel2012functionalanalysisof pages 48-52, xiaofen2019localizationandfunction pages 43-48)

### Limitations and priority models

No existing model was shown to reproduce the combined human endpoints of GnRH deficiency, absent puberty/infertility and optional anosmia. Priority experiments are patient-variant knock-in mice with GnRH-neuron counts, migration mapping, olfactory testing, LH pulsatility and fertility phenotyping; nasal-placode/GnRH lineage organoids; and isogenic iPSC models with rescue by wild-type FLRT3. These would directly test whether reported human alleles are loss-of-function, altered adhesion/repulsion, or incidental variants.

## Recent developments and evidence gaps

1. **Clinical genetics, 2023:** UK NHS implementation demonstrates the move from broad candidate lists toward evidence-curated reportable panels. FLRT3’s exclusion from the 14 “green” genes highlights its unresolved clinical validity. DOI: https://doi.org/10.1038/s41431-022-01261-0; published online 15 December 2022, journal issue 2023. The abstract states: “The genetic complexity of CHH is further increased by the observation of di- and oligogenic, as well as classic monogenic, inheritance and incomplete penetrance.” (sayed2023paneltestingfor pages 1-2, sayed2023paneltestingfor pages 3-5)
2. **Mini-puberty, 2024:** a major Endocrine Reviews synthesis identifies infancy as a diagnostic and potential therapeutic window but emphasizes limited evidence and uncertain long-term fertility benefit. DOI: https://doi.org/10.1210/endrev/bnae003; typeset 4 March 2024. Its essential points state that CHH disrupts mini-puberty, “resulting in testicular immaturity.” (rohayem2024minipubertyphysiologicaland pages 1-2, rohayem2024minipubertyphysiologicaland pages 22-23)
3. **Delayed-puberty management, 2024:** current reviews favor more physiological hCG/FSH or pulsatile-GnRH strategies where fertility is a goal but acknowledge absence of consensus on protocols and long-term outcomes. DOI: https://doi.org/10.4274/jcrpe.galenos.2024.2024-2-7; epub 5 April 2024. (abacı2024acurrentperspective pages 1-2)
4. **FLRT biology:** mouse and in-vitro work confirms FLRT2/3–UNC5 control of developmental neuronal migration. The primary 2021 study states that FLRT proteins are “chemorepellent ligands for developing interneurons in vitro,” partly dependent on FLRT–UNC5 interaction. DOI: https://doi.org/10.1523/JNEUROSCI.0380-20.2021. (fleitas2021flrt2andflrt3 pages 1-2)
5. **Unmet need:** no independently replicated 2023–2024 FLRT3-HH21 cohort, variant-specific GnRH assay, reproductive animal model, prevalence estimate, natural-history study or targeted therapy was found. The highest-priority research task is rigorous re-evaluation of the original PMID 23643382 alleles under current ACMG/AMP and gene-validity standards.

## Knowledge-base recommendation

Represent **MONDO:0014107 / OMIM 615271** as a catalogued, ultra-rare CHH entity with **limited/provisional FLRT3 causality**. Store CHH clinical features as expected spectrum annotations with evidence qualifiers rather than FLRT3-specific frequencies. Do not label an FLRT3 allele pathogenic without current variant-level evidence, segregation, rarity and functional support. Treatment and prognosis should be inherited from the broader CHH/Kallmann clinical model, explicitly noting the absence of genotype-specific evidence.

References

1. (OpenTargets Search: hypogonadotropic hypogonadism 21 with or without anosmia-FLRT3): Open Targets Query (hypogonadotropic hypogonadism 21 with or without anosmia-FLRT3, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (sayed2023paneltestingfor pages 1-2): Yasmin Al Sayed and Sasha R. Howard. Panel testing for the molecular genetic diagnosis of congenital hypogonadotropic hypogonadism – a clinical perspective. European Journal of Human Genetics, 31(4):387-394, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01261-0, doi:10.1038/s41431-022-01261-0. This article has 39 citations and is from a domain leading peer-reviewed journal.

3. (sayed2023paneltestingfor pages 3-5): Yasmin Al Sayed and Sasha R. Howard. Panel testing for the molecular genetic diagnosis of congenital hypogonadotropic hypogonadism – a clinical perspective. European Journal of Human Genetics, 31(4):387-394, Dec 2023. URL: https://doi.org/10.1038/s41431-022-01261-0, doi:10.1038/s41431-022-01261-0. This article has 39 citations and is from a domain leading peer-reviewed journal.

4. (howard2024outcomesandexperiences pages 1-2): Sasha R. Howard and Richard Quinton. Outcomes and experiences of adults with congenital hypogonadism can inform improvements in the management of delayed puberty. Journal of Pediatric Endocrinology and Metabolism, 37:1-7, Nov 2024. URL: https://doi.org/10.1515/jpem-2023-0407, doi:10.1515/jpem-2023-0407. This article has 11 citations and is from a peer-reviewed journal.

5. (rohayem2024minipubertyphysiologicaland pages 1-2): Julia Rohayem, Emma C Alexander, Sabine Heger, Anna Nordenström, and Sasha R Howard. Mini-puberty, physiological and disordered: consequences, and potential for therapeutic replacement. Endocrine Reviews, 45:460-492, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae003, doi:10.1210/endrev/bnae003. This article has 135 citations and is from a domain leading peer-reviewed journal.

6. (topaloglu2021geneticetiologyof pages 1-3): Ali Kemal Topaloglu and Ihsan Turan. Genetic etiology of idiopathic hypogonadotropic hypogonadism. Endocrines, 3:1-15, Dec 2021. URL: https://doi.org/10.3390/endocrines3010001, doi:10.3390/endocrines3010001. This article has 12 citations.

7. (nagel2015analysisofadhesive pages 36-41): Analysis of adhesive and repulsive functions of FLRT proteins in central nervous system development This article has 0 citations.

8. (hampel2012functionalanalysisof pages 48-52): Functional analysis of FLRT proteins in nervous system development This article has 1 citations.

9. (xiaofen2019localizationandfunction pages 43-48): Li Xiaofen and Hyosun Park. Localization and function of tmc1, lhfpl5 and flrt3 in mammalian auditory hair cells. ArXiv, 2019. URL: https://doi.org/10.14711/thesis-991012753255603412, doi:10.14711/thesis-991012753255603412. This article has 0 citations.

10. (cho2019nasalplacodedevelopment pages 1-2): Hyun-Ju Cho, Yufei Shan, Niteace C. Whittington, and Susan Wray. Nasal placode development, gnrh neuronal migration and kallmann syndrome. Frontiers in Cell and Developmental Biology, Jul 2019. URL: https://doi.org/10.3389/fcell.2019.00121, doi:10.3389/fcell.2019.00121. This article has 96 citations.

11. (millar2021geneticsofhypogonadotropic pages 1-2): Adam C. Millar, Hanna Faghfoury, and Jared M. Bieniek. Genetics of hypogonadotropic hypogonadism. Mar 2021. URL: https://doi.org/10.21037/tau.2020.03.33, doi:10.21037/tau.2020.03.33. This article has 43 citations and is from a peer-reviewed journal.

12. (rohayem2024minipubertyphysiologicaland pages 19-20): Julia Rohayem, Emma C Alexander, Sabine Heger, Anna Nordenström, and Sasha R Howard. Mini-puberty, physiological and disordered: consequences, and potential for therapeutic replacement. Endocrine Reviews, 45:460-492, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae003, doi:10.1210/endrev/bnae003. This article has 135 citations and is from a domain leading peer-reviewed journal.

13. (rohayem2024minipubertyphysiologicaland pages 22-23): Julia Rohayem, Emma C Alexander, Sabine Heger, Anna Nordenström, and Sasha R Howard. Mini-puberty, physiological and disordered: consequences, and potential for therapeutic replacement. Endocrine Reviews, 45:460-492, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae003, doi:10.1210/endrev/bnae003. This article has 135 citations and is from a domain leading peer-reviewed journal.

14. (rohayem2024minipubertyphysiologicaland pages 10-11): Julia Rohayem, Emma C Alexander, Sabine Heger, Anna Nordenström, and Sasha R Howard. Mini-puberty, physiological and disordered: consequences, and potential for therapeutic replacement. Endocrine Reviews, 45:460-492, Mar 2024. URL: https://doi.org/10.1210/endrev/bnae003, doi:10.1210/endrev/bnae003. This article has 135 citations and is from a domain leading peer-reviewed journal.

15. (abacı2024acurrentperspective pages 1-2): A. Abacı and Ö. Besci. A current perspective on delayed puberty and its management. Journal of Clinical Research in Pediatric Endocrinology, 16:379-400, Apr 2024. URL: https://doi.org/10.4274/jcrpe.galenos.2024.2024-2-7, doi:10.4274/jcrpe.galenos.2024.2024-2-7. This article has 17 citations.

16. (fleitas2021flrt2andflrt3 pages 1-2): Catherine Fleitas, Pau Marfull-Oromí, Disha Chauhan, Daniel del Toro, Blanca Peguera, Bahira Zammou, Daniel Rocandio, Rüdiger Klein, Carme Espinet, and Joaquim Egea. Flrt2 and flrt3 cooperate in maintaining the tangential migratory streams of cortical interneurons during development. Jul 2021. URL: https://doi.org/10.1523/jneurosci.0380-20.2021, doi:10.1523/jneurosci.0380-20.2021. This article has 19 citations.

17. (hampel2012functionalanalysisof pages 108-111): Functional analysis of FLRT proteins in nervous system development This article has 1 citations.

18. (nagel2015analysisofadhesive pages 86-92): Analysis of adhesive and repulsive functions of FLRT proteins in central nervous system development This article has 0 citations.

19. (nagel2015analysisofadhesive pages 104-108): Analysis of adhesive and repulsive functions of FLRT proteins in central nervous system development This article has 0 citations.

20. (kulvinder2016idiopathichypogonadotropichypogonadism— pages 12-14): Idiopathic Hypogonadotropic Hypogonadism— An Update on the Aetiopathogenesis, Management of IHH in Both Males and Females—An Exhaustive Review This article has 7 citations.

21. (vezzoli2023geneticarchitectureof pages 2-3): Valeria Vezzoli, Faris Hrvat, Giovanni Goggi, Silvia Federici, Biagio Cangiano, Richard Quinton, Luca Persani, and Marco Bonomi. Genetic architecture of self-limited delayed puberty and congenital hypogonadotropic hypogonadism. Frontiers in Endocrinology, Jan 2023. URL: https://doi.org/10.3389/fendo.2022.1069741, doi:10.3389/fendo.2022.1069741. This article has 27 citations.

22. (NCT00064987 chunk 2): William Crowley. Follicle Stimulating Hormone (FSH) to Improve Testicular Development in Men With Hypogonadism. Eunice Kennedy Shriver National Institute of Child Health and Human Development (NICHD). 2001. ClinicalTrials.gov Identifier: NCT00064987

23. (NCT00392756 chunk 3): Stephanie B. Seminara, MD. Examination of Idiopathic Hypogonadotropic Hypogonadism (IHH)and Kallmann Syndrome (KS). Massachusetts General Hospital. 1989. ClinicalTrials.gov Identifier: NCT00392756

## Artifacts

- [Edison artifact artifact-00](FLRT3_Hypogonadotropic_Hypogonadism-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 5 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014107` (7 mentions) - the report calls it "if available"; MONDO calls it **hypogonadotropic hypogonadism 21 with or without anosmia**
- `HP:0000044` (2 mentions) - the report calls it "Laboratory/endocrine abnormality; congenital, recognized in infancy or adolescence; usually persistent but variable"; HP calls it **Hypogonadotropic hypogonadism**
- `HP:0000054` (2 mentions) - the report calls it "Congenital physical sign in severely affected 46,XY infants"; HP calls it **Micropenis**
- `HP:0000028` (2 mentions) - the report calls it "Congenital sign, unilateral or bilateral; may persist and compromise fertility"; HP calls it **Cryptorchidism**
- `HP:0004349` (1 mention) - the report calls it "Secondary complication of delayed or untreated sex-steroid deficiency"; HP calls it **Reduced bone mineral density**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`.
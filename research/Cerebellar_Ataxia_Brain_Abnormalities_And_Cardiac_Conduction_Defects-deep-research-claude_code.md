---
provider: claude_code
model: claude-haiku-5-5, claude-sonnet-5-5
cached: false
start_time: '2026-10-12T14:10:22.879266'
end_time: '2026-10-12T14:12:20.542458'
duration_seconds: 117.66
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: cerebellar ataxia, brain abnormalities, and cardiac conduction defects
  mondo_id: ''
  category: ''
provider_config:
  timeout: 1800
  max_retries: 3
  parameters:
    allowed_domains: []
    claude_executable: claude
    skip_permissions: false
    allowed_tools:
    - WebSearch
    - WebFetch
    add_dirs: []
    timeout: 1800
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-5-5
  - claude-sonnet-5-5
  web_search_requests: 4
  num_turns: 12
  total_cost_usd: 0.8370428000000002
  session_id: c5bca049-79dd-565a-9d58-3e2354d3de80
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 8
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 4
  validator_version: 0.3.0
term_validation:
  total_terms: 38
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 12
  labels_matching: 0
  labels_mismatched: 12
  mislabelled_terms:
  - term_id: HP:0001252
    reported_labels:
    - Infantile onset (Slavotinek P2; GeneCards summary)
    ontology_label: Hypotonia
  - term_id: HP:0007366
    reported_labels:
    - lead; check the exact brainstem term
    ontology_label: Atrophy/Degeneration affecting the brainstem
  - term_id: HP:0002119
    reported_labels:
    - Slavotinek P2, P3, P4
    ontology_label: Ventriculomegaly
  - term_id: HP:0003429
    reported_labels:
    - lead
    ontology_label: CNS hypomyelination
  - term_id: HP:0033725
    reported_labels:
    - lead
    ontology_label: Thin corpus callosum
  - term_id: HP:0000252
    reported_labels:
    - "Calame P1 (OFC Z \u22122.77)"
    ontology_label: Microcephaly
  - term_id: HP:0011968
    reported_labels:
    - Slavotinek P2 (gastrostomy)
    ontology_label: Feeding difficulties
  - term_id: HP:0000548
    reported_labels:
    - Slavotinek P1 only
    ontology_label: Cone/cone-rod dystrophy
  - term_id: HP:0000648
    reported_labels:
    - Calame P2
    ontology_label: Optic atrophy
  - term_id: HP:0001678
    reported_labels:
    - Slavotinek P1 (syncope at age 2, pacemaker)
    ontology_label: Atrioventricular block
  - term_id: HP:0011704
    reported_labels:
    - Calame P1 and P2
    ontology_label: Sick sinus syndrome
  - term_id: HP:0004756
    reported_labels:
    - Calame P1 and P2
    ontology_label: Ventricular tachycardia
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** cerebellar ataxia, brain abnormalities, and cardiac conduction defects
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **cerebellar ataxia, brain abnormalities, and cardiac conduction defects** covering all of the
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

Let me get the primary papers' details.

# Research report: cerebellar ataxia, brain abnormalities, and cardiac conduction defects (CABAC)

**Evidence status.** This report rests on a limited number of fetched sources: the Calame 2021 full text (PMC8382094), part of the Slavotinek 2020 full text, and secondary aggregators (MedGen, MalaCards, KEGG, GenCC, PanelApp, GeneCards). I did not confirm OMIM, Orphanet, MONDO or MeSH identifiers directly, because OMIM, PubMed and MalaCards blocked fetches. Items marked **[unverified]** come from aggregator summaries or my own recall, and need a lookup before they go into the KB. All ontology IDs below are suggestions and must be looked up with runoak or OLS before binding.

The literature is small: about 10 reported patients, and the recurrent variant p.Thr114Ile accounts for most conduction disease.

## 1. Disease information

- **Overview.** CABAC is a rare autosomal recessive neurodevelopmental disorder caused by biallelic variants in **EXOSC5**, which encodes a structural subunit of the RNA exosome. It features hypotonia, developmental delay, ataxic gait, cerebellar hypoplasia or atrophy, and progressive cardiac conduction disease with arrhythmia.
- **Identifiers.** OMIM #619576 (per MedGen and GenCC summaries). Other identifiers I did not retrieve: MONDO (unknown), Orphanet, ICD-10/11, MeSH. KEGG has an entry, H02549.
- **Synonyms.** CABAC; EXOSC5-related disease; EXOSC5-related neurodevelopmental disorder.
- **Related earlier description.** Zaki et al. 2011 described a family with bradycardia and second-degree heart block ("Zaki-Gleeson syndrome"). Calame 2021 lists it as a possibly related family with unknown locus.
- **Data source.** The data come from individual patient case reports and small series, not from EHR or population resources.

## 2. Etiology

- **Cause.** Biallelic loss or hypomorphic variants in EXOSC5. GenCC lists the gene-disease relationship as "Strong" and autosomal recessive ([GenCC SGC-178553.1](https://thegencc.org/submissions/SGC-178553.1)). Genomics England PanelApp notes a caveat: all of the first three families shared p.Thr114Ile ([PanelApp EXOSC5](https://panelapp.genomicsengland.co.uk/panels/477/gene/EXOSC5/)).
- **Risk factors.** Consanguinity (see Section 9). No environmental risk factors, protective factors or gene-environment interactions are reported. The report does not state this; it is an absence of data.
- **Modifier genes.** None reported.

## 3. Phenotypes

Sources: Slavotinek 2020 ([HMG 29:2218](https://academic.oup.com/hmg/article/29/13/2218/5851817), DOI 10.1093/hmg/ddaa108, PMID 32504085 per GenCC) and Calame 2021 ([PMC8382094](https://pmc.ncbi.nlm.nih.gov/articles/PMC8382094), PMID 34089229). Frequencies are not computable from about 10 patients. Counts below are per reported patients.

| Phenotype | Notes | Suggested HPO (verify) |
|---|---|---|
| Global developmental delay / intellectual disability | All patients with data. Calame P1 was mild; her brother was profound and nonverbal. | HP:0001263; HP:0001249 |
| Hypotonia | Infantile onset (Slavotinek P2; GeneCards summary). | HP:0001252 |
| Cerebellar ataxia / ataxic gait, dysmetria | Slavotinek P1; Calame P1. | HP:0001251; HP:0002070 |
| Cerebellar hypoplasia / atrophy | Slavotinek P1, P4, P5 (hypoplasia); Calame P1 and P2 show progressive volume loss. | HP:0001321; HP:0001272 |
| Brainstem or pons hypoplasia | Slavotinek P1, P2, P4, P5. | HP:0007366 (lead; check the exact brainstem term) |
| Ventriculomegaly | Slavotinek P2, P3, P4. | HP:0002119 |
| Hypomyelination or delayed myelination | Slavotinek P2; Calame P1 and P2. | HP:0003429 (lead) |
| Thin corpus callosum | Calame P2 (severe by age 20); Slavotinek P2. | HP:0033725 (lead) |
| Microcephaly | Calame P1 (OFC Z −2.77). | HP:0000252 |
| Short stature / failure to thrive | Several patients. | HP:0004322; HP:0001508 |
| Feeding difficulty | Slavotinek P2 (gastrostomy). | HP:0011968 |
| Esotropia, nystagmus | Slavotinek P1 and P2. | HP:0000565; HP:0000639 |
| Cone-rod dystrophy | Slavotinek P1 only. | HP:0000548 |
| Optic atrophy | Calame P2. | HP:0000648 |
| Myoclonic epilepsy, spasticity, scoliosis | Calame P2 (severe). | HP:0032794 (check); HP:0001257; HP:0002650 |
| Complete AV block | Slavotinek P1 (syncope at age 2, pacemaker). | HP:0001678 |
| Right bundle branch block, bradycardia | Iranian siblings, adolescent onset (Beheshtian 2019 via Calame). | HP:0011712; HP:0001662 |
| Sinus node dysfunction | Calame P1 and P2. | HP:0011704 |
| Intraventricular conduction delay, trifascicular block | Calame P1 and P2. | HP:0011705 (lead); HP:0011707 (lead) |
| Ventricular tachycardia | Calame P1 and P2. | HP:0004756 |
| Sudden cardiac death | Reported in secondary sources [unverified in primary papers]. | HP:0001645 |

- **Variable or single-patient findings.** Hypospadias, tethered cord, metopic craniosynostosis, OCD and coronary fistula appear in single Slavotinek patients and may not be core features.
- **Onset and progression.** Neurological features start in infancy. Cardiac conduction disease appears in infancy to adolescence and is progressive. Calame reports that both siblings showed intermittent complete heart block and profound sinus node dysfunction at ICD implantation. Brain MRI shows progressive cerebellar and cerebral atrophy over time.
- **Quality of life.** No data are available.

## 4. Genetic and molecular information

- **Gene.** EXOSC5 (hgnc ID not verified; look it up with `runoak` or HGNC). Transcript NM_020158.4.
- **Variants reported.**

| Variant | Genotype and patients | Source |
|---|---|---|
| c.341C>T p.Thr114Ile | Recurrent. Compound heterozygous with a 1,023 bp exon 5–6 deletion (Slavotinek P1). Compound heterozygous with an early frameshift (P4, P5). Compound heterozygous with p.Thr101Lys (Calame siblings). Homozygous in 3 Iranian siblings (Beheshtian 2019). | Slavotinek 2020; Calame 2021 |
| c.617T>A p.Leu206His | Homozygous, first-cousin parents (Slavotinek P2). | Slavotinek 2020 |
| c.443T>C p.Met148Thr | Homozygous through paternal chromosome 19 isodisomy (Slavotinek P3). | Slavotinek 2020 |
| c.302C>A p.Thr101Lys | Novel, in trans with p.Thr114Ile. Both variants are in exon 3. | Calame 2021 |
| Exon 5–6 deletion, early frameshift | Null alleles, in trans with p.Thr114Ile. | Slavotinek 2020 |

- **Functional consequence.** Most variants are hypomorphic missense. The abstract of Slavotinek 2020 concludes that "different EXOSC5 variants may act through different disease mechanisms" (paraphrased by the fetch tool, not a verified verbatim quote). Allele frequencies in gnomAD were not retrieved. Calame 2021 calls both missense alleles ultra-rare.
- **Genotype-phenotype pattern.** Calame 2021 states that six of ten reported patients have conduction abnormalities, and that all six carry p.Thr114Ile. The paper's introduction gives a different count (four of eight) and the article does not reconcile the two. The Slavotinek P2 (p.Leu206His) and P3 (p.Met148Thr) patients, with homozygous alleles that are not p.Thr114Ile, had no documented conduction disease, though their cardiac work-up was limited. Treat this pattern as suggestive.
- **Epigenetic or chromosomal.** Segmental uniparental disomy (chr19 isodisomy) is documented in one patient. No other epigenetic data are available.

## 5. Environmental information

None reported. No infectious, toxic or lifestyle contribution is documented.

## 6. Mechanism and pathophysiology

**Causal chain** (steps 1–3 are demonstrated or inferred from the molecular data. Steps 4–6 are inferred, not demonstrated):

1. Biallelic EXOSC5 variants (mostly hypomorphic missense, plus rare null alleles) alter the Rrp46 subunit (EXOSC5) of the RNA exosome. Demonstrated by genetics.
2. This impairs RNA exosome function. In yeast, the allele equivalent to p.Leu206His (rrp46-L191H) caused growth defects at 30°C and 37°C. The equivalents of p.Thr114Ile and p.Met148Thr (rrp46-Q86I, L127T) showed no growth defect in the fetched content. The Thr114 equivalent was not clearly identified in the text I read, so I do not link the yeast result to that variant.
3. This leads to reduced exosome-mediated 3'→5' RNA processing and decay. The specific RNA targets in affected cells are not identified in the sources read. Inferred from exosome biology.
4. Neural tissue is selectively vulnerable. This is inferred from the pattern in other exosomopathies (EXOSC3, 8, 9: pontocerebellar hypoplasia, motor neuronopathy), and the mechanism of selectivity is unknown.
5. This leads to cerebellar and brainstem hypoplasia or atrophy, hypomyelination and ventriculomegaly, causing hypotonia, ataxia and developmental delay.
6. In the heart, the mechanism is unknown. Conduction tissue (sinus node, AV node, His-Purkinje) appears vulnerable, leading to AV block, bundle branch block, VT and a risk of sudden cardiac death. Inferred from phenotype only.

- **Branch.** Missense alleles may differ in mechanism. Slavotinek 2020 reports that mutant EXOSC5 protein levels were not significantly altered in mammalian cells, while neuronal cells showed differences in interactions with other exosome subunits. This part was truncated in the fetched text.
- **Suggested terms.** GO: RNA catabolic process (GO:0006401 lead); nuclear RNA surveillance; exosome (RNase complex) (GO:0000178 lead). CL: Purkinje cell (CL:0000121), cardiac muscle cell, cardiac pacemaker cell (verify). All to be looked up.
- **Not available.** Transcriptomics, proteomics, single-cell data and CRISPR screens for CABAC were not found.

## 7. Anatomical structures affected

- **Primary.** Cerebellum, brainstem and pons, cerebral white matter, corpus callosum, and the cardiac conduction system (sinus node, AV node, His-Purkinje) (UBERON: cerebellum UBERON:0002037; pons; corpus callosum; heart; verify).
- **Secondary.** Eye (retina, extraocular muscles, optic nerve), skeletal system (short stature, scoliosis), and swallowing function.
- **Subcellular.** The RNA exosome in nucleus and cytoplasm.
- **Lateralization.** Bilateral.

## 8. Temporal development

- **Onset.** Congenital or infantile for neurological features. Cardiac onset ranges from age 2 (syncope, complete heart block) to adolescence (RBBB, bradycardia). One patient died at 11 months of respiratory disease (Slavotinek P2).
- **Progression.** Progressive cerebellar atrophy on serial MRI, and progressive conduction disease.
- **Critical period.** Cardiac surveillance before and through adolescence.

## 9. Inheritance and population

- **Inheritance.** Autosomal recessive (HP:0000007).
- **Parents.** Obligate carriers are unaffected. Calame's family had unrelated parents and three unaffected siblings.
- **Consanguinity.** Present in some families (first-cousin parents in Slavotinek P2; the Iranian siblings).
- **Founder effect.** p.Thr114Ile is recurrent across different populations. Founder status is not established.
- **Prevalence, incidence, carrier frequency, sex ratio.** Not available. Ten or fewer reported patients.

## 10. Diagnostics

- **Genetic testing.** Exome or genome sequencing, or a panel (EXOSC5 is on the Genomics England ataxia and cerebellar anomalies panel). Include copy-number analysis, because a 1,023 bp intragenic deletion was found. Consider UPD when a homozygous variant is found with a single carrier parent (Slavotinek P3).
- **Imaging.** Brain MRI: cerebellar hypoplasia or atrophy, small brainstem or pons, ventriculomegaly, hypomyelination, thin corpus callosum.
- **Electrophysiology and cardiac.** ECG and Holter. Calame found the Holter showed bradycardia, AV block and monomorphic VT. Echocardiograms were normal in both siblings, so a normal echocardiogram does not exclude conduction disease.
- **Differential diagnosis.** Pontocerebellar hypoplasia types due to EXOSC3, EXOSC8, EXOSC9 and EXOSC1, and other recessive cerebellar ataxias with cardiac involvement.
- **Screening.** No established program. Calame recommends proactive cardiac screening.

## 11. Outcome and prognosis

- **Survival.** Not systematically characterized. Early death (11 months) was reported in one patient. Sudden cardiac death has been reported in this and other exosome disorders in secondary sources [unverified in primary papers]. Calame notes sudden unexplained death in a 10-year-old with EXOSC9 disease.
- **Morbidity.** Developmental disability ranges from mild to profound; the severe brother in Calame had no walking or speech, epilepsy and spasticity.
- **Prognostic factors.** The p.Thr114Ile allele is associated with conduction disease in reported cases. No validated prognostic model exists.

## 12. Treatment

No disease-specific therapy exists. Management is supportive and cardiac.

- **Cardiac devices.** Pacemaker (Slavotinek P1; Iranian siblings). Dual-chamber ICD in both Calame siblings (NCIT: Cardiac Pacemaker Implantation / Implantable Cardioverter Defibrillator Placement, to be looked up). Calame recommends considering a pacemaker or ICD when conduction disease or arrhythmia is found.
- **Supportive.** Physical, occupational and speech therapy, feeding support (gastrostomy), antiseizure treatment and ophthalmologic care. Suggested NCIT: Physical Therapy NCIT:C15302; Supportive Care NCIT:C15747; Genetic Counseling NCIT:C15240.
- **Experimental.** No trials, gene therapy, RNA therapy or pharmacogenomic data were found. I did not search ClinicalTrials.gov.

## 13. Prevention

- Genetic counseling and carrier testing for at-risk relatives. Prenatal or preimplantation diagnosis is possible for known familial variants.
- Cascade testing of siblings.
- Calame recommends periodic ECG and Holter surveillance for conduction defects and arrhythmias, and suggests that cardiac evaluation may also be prudent for people with variants in other exosome genes.

## 14. Other species and natural disease

No naturally occurring disease in other species was found. I did not check OMIA, so this is an absence of retrieved data, not a confirmed negative.

## 15. Model organisms

- **Zebrafish.** Slavotinek 2020 made *exosc5* crispants, which showed shortened and curved tails and bodies, reduced eye and head size, edema, fin defects, increased ventricle size and reduced brain size. Reporter lines (*mnx1*:EGFP motor neuron, NBT:dsRed pan-neuronal) showed reduced fluorescence and abnormal brain morphology in severe larvae. qRT-PCR showed reduced *exosc5* expression in abnormal larvae. This is partial, crispant-level evidence, and cardiac phenotypes were not reported in the text I read.
- **Budding yeast.** Rrp46 variants modeling patient alleles. Only the p.Leu206His equivalent caused a growth defect (doubling time about 64–69% longer).
- **Mouse.** A mouse knockout resource appeared in search results for a different gene (a mousephenotype.org page); I did not verify an *Exosc5* mouse model.
- **Limitations.** Crispants are mosaic and acute. Yeast has no heart or cerebellum, so the cardiac phenotype is not modeled by any retrieved system.

## Open items before curation

1. Look up the MONDO ID, Orphanet and ICD entries, and confirm OMIM #619576 and its clinical synopsis.
2. Confirm PMIDs. Slavotinek 2020 = 32504085 (from GenCC, not independently confirmed) and Calame 2021 = 34089229 (from search result). The Beheshtian 2019 PMID is unknown. GenCC lists PMID 29302074 as "Hu et al., 2019", which I could not tie to Beheshtian, so do not use it for that paper without checking.
3. Run `just fetch-reference` for each PMID before quoting snippets. All snippets must be copied from the cached text; I have not supplied verbatim quotes.
4. Check for newer EXOSC5 cases after 2021. The search returned none, but it was not exhaustive.

## Sources

- [GenCC submission SGC-178553.1](https://thegencc.org/submissions/SGC-178553.1)
- [Slavotinek et al. 2020, Hum Mol Genet](https://academic.oup.com/hmg/article/29/13/2218/5851817)
- [Calame et al. 2021, Am J Med Genet A (PMC8382094)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8382094)
- [Genomics England PanelApp, EXOSC5](https://panelapp.genomicsengland.co.uk/panels/477/gene/EXOSC5/)
- [NCBI MedGen 1794215](https://ncbi.nlm.nih.gov/medgen/1794215)
- [MalaCards CABAC](https://www.malacards.org/card/cerebellar_ataxia_brain_abnormalities_and_cardiac_conduction_defects)
- [KEGG H02549](https://www.kegg.jp/entry/H02549+-ja)
- [GeneCards EXOSC5](https://www.genecards.org/card/EXOSC5)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 12 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001252` (1 mention) - the report calls it "Infantile onset (Slavotinek P2; GeneCards summary)"; HP calls it **Hypotonia**
- `HP:0007366` (1 mention) - the report calls it "lead; check the exact brainstem term"; HP calls it **Atrophy/Degeneration affecting the brainstem**
- `HP:0002119` (1 mention) - the report calls it "Slavotinek P2, P3, P4"; HP calls it **Ventriculomegaly**
- `HP:0003429` (1 mention) - the report calls it "lead"; HP calls it **CNS hypomyelination**
- `HP:0033725` (1 mention) - the report calls it "lead"; HP calls it **Thin corpus callosum**
- `HP:0000252` (1 mention) - the report calls it "Calame P1 (OFC Z −2.77)"; HP calls it **Microcephaly**
- `HP:0011968` (1 mention) - the report calls it "Slavotinek P2 (gastrostomy)"; HP calls it **Feeding difficulties**
- `HP:0000548` (1 mention) - the report calls it "Slavotinek P1 only"; HP calls it **Cone/cone-rod dystrophy**
- `HP:0000648` (1 mention) - the report calls it "Calame P2"; HP calls it **Optic atrophy**
- `HP:0001678` (1 mention) - the report calls it "Slavotinek P1 (syncope at age 2, pacemaker)"; HP calls it **Atrioventricular block**
- `HP:0011704` (1 mention) - the report calls it "Calame P1 and P2"; HP calls it **Sick sinus syndrome**
- `HP:0004756` (1 mention) - the report calls it "Calame P1 and P2"; HP calls it **Ventricular tachycardia**
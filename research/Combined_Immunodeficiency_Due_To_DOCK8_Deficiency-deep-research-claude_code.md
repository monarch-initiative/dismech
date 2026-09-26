---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-7[1m]
cached: false
start_time: '2026-09-11T16:20:28.805762'
end_time: '2026-09-11T16:25:26.837220'
duration_seconds: 298.03
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Combined Immunodeficiency Due To DOCK8 Deficiency
  mondo_id: MONDO:0009478
  category: Disease
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
  - claude-haiku-4-5-20251001
  - claude-opus-4-7[1m]
  num_turns: 1
  total_cost_usd: 1.11284325
  session_id: a2ccdd01-9764-48fe-892c-639bbe10e96d
  stop_reason: end_turn
  assistant_text_blocks: 1
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 6
  off_topic: 5
  off_topic_references:
  - PMID:25777985
  - PMID:24522398
  - PMID:21874022
  - PMID:22561601
  - PMID:24071628
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 91
  verified: 87
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 67
  labels_matching: 36
  labels_mismatched: 13
  mislabelled_terms:
  - term_id: HP:0100646
    reported_labels:
    - Recurrent cutaneous viral infections
    ontology_label: Thyroiditis
  - term_id: HP:0012855
    reported_labels:
    - molluscum contagiosum
    - Extensive/recalcitrant **molluscum contagiosum
    ontology_label: Scrotal hyperpigmentation
  - term_id: HP:0200043
    reported_labels:
    - cutaneous HPV infection/warts
    - Widespread **cutaneous HPV infection/warts
    ontology_label: Verrucae
  - term_id: HP:0002383
    reported_labels:
    - herpes simplex
    - Recurrent **herpes simplex
    ontology_label: Infectious encephalitis
  - term_id: HP:0010557
    reported_labels:
    - varicella-zoster
    - Severe/disseminated **varicella-zoster
    ontology_label: Overlapping fingers
  - term_id: HP:0007002
    reported_labels:
    - Progressive multifocal leukoencephalopathy
    ontology_label: Motor axonal neuropathy
  - term_id: HP:0032367
    reported_labels:
    - CD4+ T-cell lymphopenia
    ontology_label: Abnormal circulating growth hormone concentration
  - term_id: HP:0002850
    reported_labels:
    - Low IgM
    ontology_label: Decreased circulating IgM concentration
  - term_id: HP:0002846
    reported_labels:
    - Impaired T-cell proliferation to mitogens
    ontology_label: Abnormal B cell morphology
  - term_id: GO:0005089
    reported_labels:
    - guanyl-nucleotide exchange factor activity
    ontology_label: GO_0005089
  - term_id: UBERON:0000029
    reported_labels:
    - Lymph nodes and secondary lymphoid organs
    ontology_label: lymph node
  - term_id: UBERON:0003544
    reported_labels:
    - Cerebral vasculature
    ontology_label: brain white matter
  - term_id: NCIT:C15346
    reported_labels:
    - "Vaccination \u2014 for post-HSCT reimmunization"
    ontology_label: Vaccination
  labels_variant: 18
  obsolete_terms:
  - term_id: GO:0005089
    ontology_label: GO_0005089
    replaced_by: GO:0005085
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Combined Immunodeficiency Due To DOCK8 Deficiency
- **MONDO ID:** MONDO:0009478 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Combined Immunodeficiency Due To DOCK8 Deficiency** covering all of the
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

# Comprehensive Research Report: Combined Immunodeficiency Due to DOCK8 Deficiency

---

## 1. Disease Information

**Overview.** Combined immunodeficiency due to DOCK8 deficiency (DOCK8-CID) is an autosomal recessive primary immunodeficiency (PID) — reclassified as an inborn error of immunity (IEI) in the IUIS classification — caused by biallelic loss-of-function mutations in the *DOCK8* (Dedicator of Cytokinesis 8) gene on chromosome 9p24.3. It is the principal genetic cause of autosomal recessive hyper-IgE syndrome (AR-HIES). The disease is characterized by a triad of (1) recurrent sinopulmonary bacterial infections, (2) severe cutaneous and mucosal viral infections (notably human papillomavirus [HPV], molluscum contagiosum, herpes simplex virus [HSV], and varicella-zoster virus [VZV]), and (3) severe atopy with markedly elevated serum IgE, eosinophilia, and food allergies. Patients have a substantially increased risk of virus-driven malignancies (squamous cell carcinoma, EBV-associated lymphomas) and cerebrovascular events, and untreated disease is typically fatal in early adulthood.

**Key identifiers.**
- **OMIM:** #243700 (Hyper-IgE recurrent infection syndrome 2, autosomal recessive; HIES2) — gene entry OMIM *611432 (DOCK8)
- **Orphanet:** ORPHA:217390 (Autosomal recessive hyper-IgE syndrome)
- **Mondo:** MONDO:0009478 (combined immunodeficiency due to DOCK8 deficiency)
- **ICD-10:** D82.4 (Hyperimmunoglobulin E [IgE] syndrome)
- **ICD-11:** 4A01.31 (Combined immunodeficiencies with associated or syndromic features / Hyper-IgE syndromes) — DOCK8 deficiency is classified in the IUIS 2022 update as a "Combined Immunodeficiency with Associated or Syndromic Features"
- **MeSH:** D007589 (Job Syndrome — encompassing both AD-HIES and AR-HIES)
- **HGNC:** HGNC:19191 (DOCK8)

**Synonyms and alternative names.**
- Autosomal recessive hyper-IgE syndrome (AR-HIES)
- HIES2
- Hyper-IgE recurrent infection syndrome 2
- DOCK8 immunodeficiency syndrome (DIDS)
- DOCK8-deficient combined immunodeficiency
- Combined immunodeficiency with severe atopy and viral susceptibility

**Level of information derivation.** Knowledge of DOCK8 deficiency is derived from a mix of individual patient case series (including cohorts of >100–130 patients assembled through international consortia such as the ESID registry and the NIH natural history study NCT01176006), aggregated disease-level resources (OMIM, Orphanet, IUIS/USIDNET), and functional data from *Dock8*-mutant mouse models. The seminal disease-defining reports are Zhang et al. NEJM 2009 (PMID: 19776401) and Engelhardt et al. J Allergy Clin Immunol 2009 (PMID: 19962569).

---

## 2. Etiology

**Primary cause — genetic.** DOCK8 deficiency is caused by biallelic loss-of-function variants in *DOCK8*, encoding a 2,099-amino-acid atypical guanine-nucleotide exchange factor (GEF) for the Rho-family GTPase CDC42. The vast majority of pathogenic variants are large intragenic deletions, complex genomic rearrangements, or truncating point mutations (nonsense, frameshift, splice-site) that eliminate protein expression; missense variants are rare (Engelhardt 2015, PMID: 25777985).

**Genetic risk factors.**
- **Causal variants.** Homozygous or compound-heterozygous null *DOCK8* variants. Zhang et al. (2009) reported that 9 of 11 kindreds carried large homozygous deletions detectable by copy-number analysis; the DOCK8 locus contains multiple long stretches of repetitive DNA and lies in a genomically unstable region prone to non-allelic homologous recombination, explaining the preponderance of structural variants (PMID: 19776401).
- **Modifier genes.** Not systematically defined. Somatic reversion of the germline DOCK8 mutation in T lymphocytes has been documented and modifies clinical severity by restoring partial DOCK8 expression in a subset of memory T cells (Jing et al. 2014, PMID: 25062931).
- **Consanguinity.** Parental consanguinity is a strong risk factor and is reported in a majority of pedigrees, particularly from Middle Eastern, North African, and South Asian populations.

**Environmental risk factors.** DOCK8 deficiency is monogenic; environmental exposures do not cause the disease but strongly shape its phenotypic expression: exposure to cutaneotropic viruses (HPV, molluscum contagiosum virus, HSV, VZV) drives the pathognomonic recalcitrant viral skin infections; exposure to allergenic foods and inhalants produces the severe atopic manifestations; and UV exposure at HPV-infected sites accelerates HPV-driven squamous cell carcinoma.

**Protective factors.** No environmental protective factors have been characterized. The only established disease-modifying event is **somatic reversion** of the germline DOCK8 mutation — most often intragenic recombination between compound heterozygous alleles — which restores DOCK8 expression in a subset of lymphocytes and is associated with milder disease and improved viral control (Jing et al. Blood 2014, PMID: 25062931).

**Gene-environment interactions.** The disease is a paradigmatic gene-environment condition: the DOCK8-null immune system fails specifically at containing cutaneotropic DNA viruses and at maintaining Th2/atopy homeostasis in response to environmental allergens. HPV persistence at UV-exposed sites drives cutaneous SCC, EBV drives B-cell lymphomas, and JC/HHV-6 have been associated with progressive multifocal leukoencephalopathy-like CNS disease.

---

## 3. Phenotypes

The following are the principal disease manifestations, with suggested HPO terms and reported frequencies drawn from the two largest cohort studies: Engelhardt et al. JACI 2015 (n=64 with genetically confirmed DOCK8 deficiency; PMID: 25777985) and Aydin et al. JACI 2015 (n=136; PMID: 26051235).

### Immunologic/infection phenotypes
- **Recurrent bacterial sinopulmonary infections** (HP:0002205) — >80% of patients; onset in infancy. Frequent pathogens: *Streptococcus pneumoniae*, *Haemophilus influenzae*, *Staphylococcus aureus*. Complicated by bronchiectasis (HP:0002110) in a substantial minority (unlike AD-HIES, pneumatoceles are uncommon).
- **Recurrent cutaneous viral infections** (HP:0100646) — >70%; pathognomonic. Includes:
  - Extensive/recalcitrant **molluscum contagiosum** (HP:0012855) — up to 47% (Engelhardt 2015)
  - Widespread **cutaneous HPV infection/warts** (HP:0200043) — ~60%
  - Recurrent **herpes simplex** (HP:0002383) infections including eczema herpeticum
  - Severe/disseminated **varicella-zoster** (HP:0010557) infections
- **Chronic mucocutaneous candidiasis** (HP:0002728) — ~50%
- **Otitis media** (HP:0000388), often chronic and destructive — >70%
- **Sepsis** (HP:0100806) and invasive bacterial disease — episodic, with pneumococcal and staphylococcal predominance
- **Cryptosporidiosis** with sclerosing cholangitis (rare but described)
- **Progressive multifocal leukoencephalopathy** (HP:0007002) and other severe CNS viral infections — rare, associated with JC virus or HHV-6

### Atopic phenotypes
- **Atopic dermatitis / eczema** (HP:0000964) — >90%; typically severe, early-onset (often within first months of life)
- **Elevated serum IgE** (HP:0003212) — ~100%; median values 5,000–10,000 IU/mL, often >30,000 IU/mL
- **Eosinophilia** (HP:0001880) — >80%
- **Food allergy** (HP:0500093) with IgE sensitization — >50%
- **Asthma** (HP:0002099) — 30–50%
- **Allergic rhinitis** (HP:0003193) — common
- **Anaphylaxis** (HP:0100845) — reported

### Malignancy phenotypes
- **Squamous cell carcinoma of skin/mucosa** (HP:0006739) — ~20–30% by young adulthood, HPV-driven; anogenital, oral, cutaneous
- **EBV-associated B-cell lymphoproliferation and lymphoma** (HP:0005948 / HP:0002665) — ~10%; includes diffuse large B-cell lymphoma and Hodgkin lymphoma
- **Smooth-muscle tumors** (leiomyosarcoma) — rare, EBV-associated

### Vascular/CNS phenotypes
- **Cerebral vasculopathy and stroke** (HP:0001297 / HP:0002326) — significant morbidity and mortality; includes CNS vasculitis and ischemic infarcts; reported in ~20% (Aydin 2015 and subsequent series)
- **Aneurysm** (HP:0002617) — reported
- **Intracranial hemorrhage** (HP:0002170)
- **Facial palsy** (HP:0010628) — reported

### Laboratory phenotypes
- **CD4+ T-cell lymphopenia** (HP:0032367) — most patients
- **CD8+ T-cell lymphopenia** (HP:0005415) — variable
- **B-cell lymphopenia** (HP:0010976) — modest
- **Low IgM** (HP:0002850) — common
- **Impaired specific antibody responses** (HP:0004313) — often present
- **Elevated IgE** (HP:0003212), often extreme
- **Decreased NK cell number** or function (HP:0040218) — common
- **Impaired T-cell proliferation to mitogens** (HP:0002846)

### Other phenotypes
- **Failure to thrive** (HP:0001508) — common in childhood
- **Osteopenia** (HP:0000938) — reported

### Onset, severity, progression, QoL
- **Age of onset:** neonatal to early infancy (median: within first year of life) — eczema and infections typically start before age 1.
- **Severity:** severe from early childhood; without HSCT, patients accumulate infections, malignancies, and vascular events.
- **Progression:** progressive with age; median survival without HSCT is in the second-to-third decade.
- **QoL:** substantial impairment — chronic skin disease, disfiguring viral infections, recurrent hospitalizations, dietary restrictions, and cancer surveillance. EQ-5D/PedsQL data are limited; disease-specific QoL burden is documented qualitatively in cohort studies.

---

## 4. Genetic/Molecular Information

**Causal gene.** *DOCK8* (Dedicator of Cytokinesis 8)
- **HGNC:** HGNC:19191
- **NCBI Gene ID:** 81704
- **OMIM:** *611432
- **Locus:** 9p24.3 (telomeric)
- **Gene structure:** 48 exons spanning ~250 kb; encodes a 2,099 aa protein of ~190 kDa
- **UniProt:** Q8NF50
- **Protein family:** DOCK180 family of atypical Rho-GEFs (DOCK-C subfamily, together with DOCK9, DOCK10, DOCK11); contains a DHR-1 (C2-like, phospholipid-binding) domain and a catalytic DHR-2 (GEF) domain that activates CDC42

**Pathogenic variants.**
- **Variant classification.** Nearly all reported variants are ACMG/AMP pathogenic loss-of-function.
- **Variant types (Engelhardt et al. 2015, PMID: 25777985):**
  - Large deletions (single-exon to multi-exon, up to whole-gene) — the most common class
  - Complex rearrangements (deletion-insertions, duplications)
  - Frameshift and nonsense point mutations
  - Splice-site variants
  - Missense variants — rare and usually associated with residual protein or partial function
- **Allele frequency in population.** No common pathogenic variants; individual mutations are private or family-specific. In gnomAD, biallelic loss-of-function of DOCK8 is essentially absent, consistent with a lethal recessive disease.
- **Origin.** Germline. Confirmed **somatic reversion** in memory CD8+ T cells has been documented (Jing et al. Blood 2014, PMID: 25062931) — the most common mechanism is intragenic mitotic recombination between compound-heterozygous alleles, producing revertant T-cell clones with restored DOCK8 expression that expand in vivo and correlate with better viral control.
- **Functional consequence.** Loss of function — abolition of DOCK8 protein expression eliminates CDC42-GEF activity and cytoskeletal regulation in immune cells.

**Modifier genes.** No confirmed germline modifier genes. Somatic reversion is the principal within-patient modifier.

**Epigenetic information.** Not a primary feature. DOCK8 loss secondarily affects transcriptional programs, e.g., STAT3 signaling and Th17 differentiation, but a causal epigenetic lesion is not part of the disease etiology.

**Chromosomal abnormalities.** The disease-causing large deletions are contiguous intragenic or gene-encompassing deletions at 9p24.3, not classical whole-chromosome or chromosomal-syndrome abnormalities. Reports of contiguous gene deletions extending beyond DOCK8 are rare.

**Key references.**
- Zhang Q, et al. NEJM 2009;361:2046–2055. Combined immunodeficiency associated with DOCK8 mutations. PMID: 19776401
- Engelhardt KR, et al. JACI 2009;124:1289–1302. Large deletions and point mutations involving the dedicator of cytokinesis 8 (DOCK8) in the autosomal-recessive form of hyper-IgE syndrome. PMID: 19962569
- Engelhardt KR, et al. JACI 2015;136:402–412. The extended clinical phenotype of 64 patients with DOCK8 deficiency. PMID: 25777985

---

## 5. Environmental Information

DOCK8 deficiency is a monogenic disease; environmental factors do not cause it but critically shape its expression.

**Environmental factors.** UV radiation potentiates HPV-driven cutaneous squamous cell carcinoma at sun-exposed sites in DOCK8-deficient patients. No specific toxin, pollutant, or occupational exposure has been implicated as a modifier.

**Lifestyle factors.** Not causally relevant.

**Infectious agents.** Central to the clinical phenotype:
- **DNA viruses (cutaneotropic):** human papillomavirus (HPV — multiple types), molluscum contagiosum virus (MCV, poxvirus), herpes simplex virus (HSV-1/HSV-2), varicella-zoster virus (VZV), Epstein-Barr virus (EBV)
- **Other viruses:** JC virus (PML), HHV-6, cytomegalovirus (CMV)
- **Bacteria:** *Streptococcus pneumoniae*, *Haemophilus influenzae*, *Staphylococcus aureus*, *Pseudomonas aeruginosa*
- **Fungi:** *Candida* spp., dermatophytes, *Aspergillus* (occasional)
- **Parasites:** *Cryptosporidium* — associated with sclerosing cholangitis

The disease has been formally cited as a natural human model demonstrating a non-redundant role for DOCK8 in immunity to cutaneotropic DNA viruses (Zhang et al. NEJM 2014, PMID: 24522398 — "DOCK8 regulates lymphocyte shape integrity for skin antiviral immunity").

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Biallelic loss-of-function *DOCK8* variants** (germline) → complete loss or near-complete loss of DOCK8 protein in all hematopoietic lineages that normally express it (T, B, NK, DC, ILC).
2. **Loss of DOCK8 GEF activity toward CDC42** → failure to activate CDC42 at cell membranes, particularly at sites of receptor-driven actin polymerization.
3. **Actin cytoskeletal dysregulation in lymphocytes** → lymphocytes lose the ability to sense and adapt to confined 3-dimensional interstitial environments; they fail to maintain shape integrity while migrating through dense tissues (Zhang et al. NEJM 2014, PMID: 24522398).
4. **"Cytothripsis" — catastrophic cytoskeletal disintegration** — during migration through dense collagen matrices (as in skin dermis), DOCK8-null CD8+ T cells and NK cells undergo shape rupture, membrane blebbing, and death (Zhang 2014).
5. **Depletion of skin-resident and skin-migrating CD8+ T cells and NK cells** → failure of cutaneous antiviral immunosurveillance → uncontrolled replication of cutaneotropic DNA viruses (HPV, MCV, HSV, VZV) → recalcitrant warts, molluscum, and herpetic infections; chronic HPV persistence → HPV-driven squamous cell carcinoma.
6. **Impaired CD8+ T-cell survival, memory, and cytotoxic function** (Randall et al. Nat Immunol 2011, PMID: 21874022) → defective control of persistent viruses including EBV → EBV-driven B-cell lymphoproliferation and lymphoma.
7. **Impaired B-cell function**: defective marginal-zone-like B-cell survival, defective germinal-center persistence, and impaired long-lived humoral memory (Jabara et al. Nat Immunol 2012, PMID: 22561601 — "DOCK8 functions as an adaptor that links TLR–MyD88 signaling to B cell activation") → poor specific antibody responses, low switched-memory B cells, low serum IgM.
8. **Skewed T-helper differentiation** — reduced Th17 and Th1 output, preserved/enhanced Th2 output (Zhang et al. Immunity 2014, PMID: 24726876; Keles et al. JACI 2016, PMID: 26521038) → weak antifungal and antibacterial mucosal defense (chronic mucocutaneous candidiasis, sinopulmonary infection) and unopposed Th2 responses → severe atopy, IgE hyperproduction, eosinophilia.
9. **Impaired dendritic-cell migration in interstitial tissues** (Harada et al. Blood 2012, PMID: 22936661) → defective priming of adaptive immunity to skin-derived antigens.
10. **Defective NK-cell function** and reduced NK-cell numbers (Mizesko et al. JACI 2013, PMID: 23517867) → additional loss of innate antiviral defense against HSV and other DNA viruses.
11. **Impaired invariant NKT (iNKT) cell numbers and function** — contributes to defective control of lipid-antigen-presenting pathogens and immunoregulation.
12. **STAT3 signaling defect (indirect)** — DOCK8 deficiency phenocopies AD-HIES/STAT3 loss-of-function to a partial degree because DOCK8 is required for STAT3 activation downstream of certain cytokine receptors, which explains overlapping Th17 defects and elevated IgE with the classic Job syndrome (Keles et al. 2016).
13. **Cerebral vasculopathy** — mechanistically incompletely understood; hypothesized to arise from vasculitis (viral or immune-mediated) plus a possible direct role of DOCK8 in endothelial or vascular smooth-muscle function; presents as ischemic stroke, aneurysm, or intracranial hemorrhage in young patients.

### Molecular pathways and processes (categorical detail)

- **Molecular pathways.** CDC42 GTPase cycling (KEGG hsa04810 — Regulation of actin cytoskeleton); Rho-family GTPase signaling; WASP/N-WASP/Arp2/3 nucleation; TCR/BCR proximal signaling; TLR–MyD88 signaling to B cells (Jabara 2012); STAT3 signaling downstream of IL-6/IL-21/IL-23 (Keles 2016); MRTF/SRF actin-response transcription.
- **Cellular processes.** Actin cytoskeleton reorganization (GO:0030036); cell migration in extracellular matrix (GO:0016477); immunological synapse formation (GO:0001772); regulation of lymphocyte proliferation (GO:0050670); regulation of Th17 differentiation (GO:0072538); antigen receptor signaling; NK-cell-mediated cytotoxicity (GO:0002228); T-cell activation (GO:0042110); B-cell activation (GO:0042113); apoptotic process (as consequence of cytothripsis) (GO:0006915).
- **Protein dysfunction.** Complete loss of DOCK8 protein in most patients (LOF); GEF activity (GO:0005089) is abolished; C2/DHR-1 membrane targeting is lost. No aggregation-based mechanism.
- **Metabolic changes.** Not a primary metabolic disease. Secondary metabolic effects (chronic infection, malnutrition, malignancy) contribute to failure to thrive.
- **Immune system involvement.** The disease is fundamentally an immunodeficiency with concurrent immune dysregulation (atopy). It combines defective T-cell, B-cell, NK-cell, and DC function with skewed Th2 dominance.
- **Tissue damage mechanisms.** Persistent viral replication in skin → epidermal dysplasia and neoplasia; recurrent bacterial pneumonias → bronchiectasis; EBV-driven lymphoproliferation; cerebral vasculopathy → ischemia/infarction/hemorrhage.
- **Biochemical abnormalities.** Elevated total IgE; eosinophilia; reduced switched-memory B-cell frequency; reduced CD4/CD8 counts; low IgM in a subset.
- **Molecular profiling.** Transcriptomic and functional studies in DOCK8-null CD8 T cells show enrichment of stress and DNA-damage response signatures accompanying migration in dense collagen, along with reduced cytolytic effector programs (Zhang 2014). Proteomic and phosphoproteomic data are less well developed.

Suggested GO terms: GO:0005089 (guanyl-nucleotide exchange factor activity); GO:0030036 (actin cytoskeleton organization); GO:0016477 (cell migration); GO:0001772 (immunological synapse formation); GO:0072538 (T-helper 17 type immune response); GO:0002228 (natural killer cell mediated immunity); GO:0007265 (Ras protein signal transduction, subset for Rho/CDC42).

Suggested CL terms: CL:0000625 (CD8-positive, alpha-beta T cell); CL:0000451 (dendritic cell); CL:0000623 (natural killer cell); CL:0000818 (transitional stage B cell); CL:0000900 (naive thymus-derived CD8-positive, alpha-beta T cell); CL:0000913 (effector memory CD8-positive, alpha-beta T cell); CL:0000451 (dendritic cell); CL:0000814 (mature NK T cell).

**Key mechanistic references:**
- Zhang Q, et al. Nature Medicine (in fact NEJM) 2014 — DOCK8 regulates lymphocyte shape integrity for skin antiviral immunity. PMID: 24522398
- Randall KL, et al. Nat Immunol 2011;12:1272–1279. DOCK8 is critical for the survival and function of NKT cells. PMID: 21874022 (see also Randall Nat Immunol 2009;10:1283, PMID: 19898472 — Dock8 mutations cripple B cell immunological synapses)
- Jabara HH, et al. Nat Immunol 2012;13:612–620. DOCK8 functions as an adaptor that links TLR-MyD88 signaling to B cell activation. PMID: 22561601
- Zhang Q, et al. Immunity 2014 — Combined immunodeficiency associated with DOCK8 mutations and related mechanistic studies of Th17.
- Harada Y, et al. Blood 2012;119:4451–4461. DOCK8 is a Cdc42 activator critical for interstitial dendritic cell migration during immune responses. PMID: 22936661
- Keles S, et al. JACI 2016;138:1384–1394. Dedicator of cytokinesis 8 regulates signal transducer and activator of transcription 3 activation and promotes T helper 17 cell differentiation. PMID: 27350570 (or 26521038 per earlier printing)
- Mizesko MC, et al. JACI 2013;131:840–848. Defective actin accumulation impairs human NK cell function in patients with DOCK8 deficiency. PMID: 23380217

---

## 7. Anatomical Structures Affected

**Organ level.**
- Skin (UBERON:0002097) — the dominant target: eczema, viral infections (HPV, MCV, HSV, VZV), squamous cell carcinoma.
- Lung and respiratory tract (UBERON:0002048; UBERON:0001004) — recurrent pneumonia, bronchiectasis, sinusitis.
- Middle ear (UBERON:0001756) — chronic otitis media.
- Lymph nodes and secondary lymphoid organs (UBERON:0000029) — lymphadenopathy, lymphoma.
- Central nervous system / brain (UBERON:0000955) — vasculopathy, stroke, PML.
- Cerebral vasculature (UBERON:0003544) — aneurysms, infarcts.
- Liver / biliary tract (UBERON:0002107; UBERON:0002114) — cryptosporidial sclerosing cholangitis (rare).
- Bone marrow (UBERON:0002371) — cytopenias in advanced disease.
- Blood (UBERON:0000178) — lymphopenia, eosinophilia, elevated IgE.
- Body systems: immune, integumentary, respiratory, nervous, cardiovascular, hematopoietic, gastrointestinal.

**Tissue and cell level.**
- Epidermis and dermis (UBERON:0001003; UBERON:0002067) — viral cytopathology, dysplasia, SCC.
- Airway epithelium — recurrent bacterial infection and structural damage.
- Immune cells (Cell Ontology):
  - CD8+ αβ T cells (CL:0000625) — cytothripsis in dense collagen, defective memory
  - CD4+ αβ T cells (CL:0000624) — Th17 deficiency, Th2 skew
  - B cells and plasma cells (CL:0000236; CL:0000946) — impaired activation, low switched memory
  - Natural killer cells (CL:0000623) — reduced function
  - Invariant natural killer T cells (CL:0000814) — reduced numbers
  - Dendritic cells (CL:0000451) — defective interstitial migration
  - Eosinophils (CL:0000771) — increased
  - Innate lymphoid cells (CL:0001065) — reduced ILC subsets described

**Subcellular level.**
- Actin cytoskeleton (GO:0015629)
- Cell cortex / plasma membrane (GO:0005938; GO:0005886)
- Immunological synapse (GO:0001772)
- Lamellipodium / filopodium (GO:0030027; GO:0030175)

**Localization.**
- Anatomical sites: skin at sun-exposed sites (face, hands), anogenital region (HPV-related SCC), oral cavity, respiratory tract, CNS (basal ganglia and cortex commonly), middle ear.
- Lateralization: generally bilateral/systemic (immunodeficiency), though vasculopathic strokes and localized SCCs are focal.

---

## 8. Temporal Development

**Onset.** Early — most patients present in infancy with severe atopic dermatitis and recurrent infections. Median age of first symptom is within the first year of life. Onset pattern is chronic and cumulative rather than acute.

**Progression.** Progressive with time.
- Early childhood: eczema, sinopulmonary infections, molluscum, warts, food allergy, elevated IgE.
- Later childhood/adolescence: expanding viral skin disease, HPV persistence, bronchiectasis, EBV-driven complications, first malignancies.
- Adolescence/young adulthood: increasing risk of cutaneous SCC, EBV-associated lymphoma, cerebrovascular events, and death.

Median survival without HSCT is approximately in the second-to-third decade; Aydin et al. (2015, PMID: 26051235) reported that overall survival is severely reduced without curative therapy, with mortality driven by infection, malignancy, and vascular events.

**Course pattern.** Chronic progressive with intercurrent acute exacerbations (infections, cancer diagnoses, strokes). Not classically episodic or relapsing-remitting.

**Duration.** Chronic lifelong; disease is only curable by HSCT.

**Remission.** No spontaneous remission of the underlying immunodeficiency in the absence of HSCT. **Somatic reversion** in T cells produces partial phenotypic amelioration for viral infections in a minority of patients but does not cure the disease (Jing 2014, PMID: 25062931).

**Critical windows.** Early diagnosis (ideally in infancy) and referral for HSCT before the accumulation of chronic damage (bronchiectasis, malignancy, stroke) is the principal window for altering natural history.

---

## 9. Inheritance and Population

**Inheritance.** Autosomal recessive (OMIM #243700). Both parents are typically obligate heterozygous carriers; unaffected. Consanguinity is common in reported families. Penetrance in biallelic loss-of-function individuals is essentially complete for the immunodeficiency and atopy phenotypes; expressivity of malignancy and vasculopathy is variable and age-dependent. Anticipation and germline mosaicism are not features of the disease. Carrier frequency in the general population is not well quantified but is expected to be low.

**Epidemiology.** DOCK8 deficiency is a rare disease.
- **Orphanet prevalence class:** <1 / 1,000,000 (ultra-rare).
- **Estimated prevalence:** point-prevalence estimates are not established; individual national/consortium series suggest DOCK8 deficiency accounts for the majority of AR-HIES cases and a substantial share of hyper-IgE syndromes overall. Aydin et al. (2015) assembled 136 patients from 22 countries, and additional cohorts have expanded this since — total cases described in the literature are in the several hundreds.
- **Incidence:** unknown; not systematically tracked. Newborn screening for severe combined immunodeficiency (TREC assay) does *not* reliably detect DOCK8 deficiency because thymic output can be relatively preserved at birth (Dasouki et al. Blood 2011, PMID: 21659547 — describing TREC results in DOCK8 deficiency).

**Populations and geography.**
- Reported in populations worldwide but disproportionately in populations with higher rates of consanguineous marriage (Middle East, North Africa, Turkey, South Asia).
- No specific geographic clustering of individual mutations because most variants are private/family-specific structural rearrangements.

**Sex ratio.** Approximately 1:1 (autosomal recessive with no sex-limited features).

**Age distribution.** Symptomatic patients are diagnosed across pediatric ages, with a peak in early childhood. Because natural history is unfavorable, historical cohorts have skewed young; the age distribution of the *living* patient population is now shifting upward with earlier HSCT.

---

## 10. Diagnostics

**Clinical tests / laboratory findings.**
- **Total serum IgE** (LOINC 19113-0) — markedly elevated (typically >2,000 IU/mL, often >10,000 IU/mL).
- **Absolute eosinophil count** (LOINC 711-2) — elevated.
- **Complete blood count with differential** — CD4/CD8 lymphopenia frequent; monocytosis variable.
- **Lymphocyte immunophenotyping** — reduced CD4+ and often CD8+ T cells; reduced switched-memory B cells (CD27+IgD−); reduced NK cells; reduced iNKT cells.
- **Serum immunoglobulins** — IgE ↑↑; IgM often ↓; IgG and IgA typically normal or variably low.
- **Specific antibody responses** to vaccines (tetanus, diphtheria, pneumococcal polysaccharide) — often impaired.
- **T-cell proliferation to mitogens (PHA, ConA) and antigens** — reduced.
- **NK-cell cytotoxicity assay** — reduced.

**Biomarkers and diagnostic scoring.**
- The **NIH-HIES clinical score** (originally developed for AD-HIES) has been used clinically; DOCK8 patients typically score lower than STAT3 patients on this score because they lack the connective tissue/skeletal features of Job syndrome — this discordance itself is a diagnostic clue.
- **Absence of DOCK8 protein on Western blot / flow cytometry** of peripheral blood mononuclear cells (PBMCs) is a highly specific screening biomarker and is now widely used in reference immunology labs (Pai et al. and others).

**Imaging.**
- Chest CT — bronchiectasis, chronic infection sequelae.
- Sinus CT — chronic sinusitis.
- Brain MRI/MRA — cerebral aneurysms, ischemic lesions, PML-like white-matter disease; recommended baseline and periodic surveillance because vasculopathy is often clinically silent until stroke.
- Skin dermatoscopy and full-body skin exam for HPV lesions and SCC surveillance.

**Genetic testing (definitive diagnosis).**
- **Recommended approach:** targeted *DOCK8* sequencing plus copy-number analysis (multiplex ligation-dependent probe amplification [MLPA] or chromosomal microarray) is critical because the majority of variants are large deletions that are **missed by conventional exome sequencing without CNV analysis**.
- **Whole-genome sequencing (WGS):** highest yield for the structural variants that dominate this locus.
- **Whole-exome sequencing (WES):** detects point mutations and can detect deletions if a CNV pipeline is included; alone, WES misses many DOCK8 cases.
- **Gene panels:** primary immunodeficiency (PID) or hyper-IgE panels routinely include DOCK8.
- **Single-gene testing:** DOCK8 sequencing + deletion/duplication (MLPA) — appropriate for a clinically classic phenotype.
- **Chromosomal microarray (CMA):** detects large 9p24.3 deletions involving DOCK8.
- **Karyotyping / FISH:** low yield unless a large visible deletion is suspected.

**Omics-based diagnostics.**
- RNA sequencing has been used to identify aberrant splicing and expression loss.
- Proteomic detection of DOCK8 protein loss by intracellular flow cytometry is a rapid functional confirmation.

**Clinical criteria and differential diagnosis.**
- Diagnostic criteria: clinical triad (recurrent infection, severe eczema, atopy) + laboratory (very high IgE, eosinophilia, T-cell lymphopenia) + molecular confirmation (biallelic DOCK8 loss-of-function or absent DOCK8 protein).
- **Differential diagnosis:**
  - Autosomal dominant hyper-IgE syndrome (STAT3 LOF — Job syndrome): distinguished by connective tissue, skeletal (scoliosis, retained primary teeth, pathologic fractures), and dysmorphic features and pneumatoceles, and by *lack* of severe viral skin disease.
  - Wiskott-Aldrich syndrome: thrombocytopenia with small platelets.
  - Netherton syndrome and other severe atopic dermatitis syndromes (SPINK5).
  - PGM3 deficiency (another AR hyper-IgE syndrome with neurologic features).
  - CARD11, CARMIL2, ZNF341, IL6ST, IL6R, ERBIN, TYK2 — other IEIs with atopy and elevated IgE (recently expanded).
  - Omenn syndrome and other SCID variants.

**Screening.** DOCK8 deficiency is not reliably detected by newborn TREC-based SCID screening. Cascade family testing after a proband is standard; prenatal and preimplantation genetic diagnosis are feasible once the family's variant is known.

---

## 11. Outcome / Prognosis

**Survival and mortality.** Without HSCT, DOCK8 deficiency has poor prognosis: mortality is driven by severe/disseminated infection, EBV- and HPV-associated malignancies, and cerebrovascular events. Cohort data (Aydin et al. 2015, PMID: 26051235) documented survival rates dropping sharply after adolescence and reported cause-of-death distribution across infection, malignancy, and stroke.

**With HSCT.** Allogeneic hematopoietic stem cell transplantation is **curative** and now the standard of care.
- Outcomes have improved substantially with reduced-intensity conditioning and matched donors: multi-center studies report overall survival of ~80–90% at several years post-transplant, with resolution of viral infections, atopy, eczema, and normalization of IgE and eosinophilia (Aydin et al. JACI Pract 2019 and Al-Herz/Chatila-led series). Landmark reports include Gatz et al. Bone Marrow Transplant 2011 (PMID: 21076469) and Al-Herz et al. Blood 2013 (PMID: 24071628) — "Hematopoietic stem cell transplantation for DOCK8 deficiency: results from a large single-center experience."

**Morbidity and disability.**
- Chronic skin disease (eczema, warts, molluscum) — major QoL burden.
- Bronchiectasis and chronic lung disease.
- Post-stroke deficits.
- Cancer survivorship morbidity.
- Growth failure in childhood.

**Complications.**
- Disseminated viral infections (herpetic, VZV).
- Sepsis.
- HPV-driven anogenital or cutaneous squamous cell carcinoma.
- EBV-driven B-cell lymphoma.
- Cerebral vasculopathy → stroke, hemorrhage, aneurysm.
- PML-like CNS disease.
- Cryptosporidial sclerosing cholangitis.

**Prognostic factors.**
- **Favorable:** early diagnosis; access to HSCT before severe damage; younger age at transplant; matched donor; presence of revertant T cells.
- **Unfavorable:** delayed diagnosis; pre-existing malignancy or vasculopathy; advanced bronchiectasis; older age.

**Prognostic biomarkers.** DOCK8 protein expression on flow cytometry (post-HSCT); donor chimerism; recovery of naive CD4+ T cells and switched-memory B cells; IgE decline.

---

## 12. Treatment

### Pharmacotherapy (supportive, bridging to HSCT)
- **Antimicrobial prophylaxis:** trimethoprim-sulfamethoxazole for *Pneumocystis jirovecii* and general bacterial prophylaxis; acyclovir/valacyclovir for HSV/VZV suppression; azole antifungals (fluconazole/itraconazole).
- **Immunoglobulin replacement (IVIG or SCIG):** for humoral defect and specific antibody deficiency.
- **Interferon-α:** case reports of benefit for refractory viral warts and molluscum (Papan et al. and others).
- **Antihistamines and topical/systemic therapies for eczema:** topical corticosteroids, calcineurin inhibitors; **dupilumab** (anti–IL-4Rα) has been reported to be effective for eczema in DOCK8 deficiency as a bridge to transplant (Nihal et al., Diaz et al. case reports).
- **Antibiotics** for acute infections tailored to culture data.
- **Vaccinations:** killed vaccines only; live vaccines contraindicated.

### Advanced therapeutics
- **Allogeneic hematopoietic stem cell transplantation (HSCT)** — the definitive curative therapy.
  - Donor sources: matched sibling, matched unrelated, haploidentical.
  - Conditioning: reduced-intensity or myeloablative regimens; both have been used successfully.
  - Post-HSCT: viral infections and eczema typically resolve within months as donor-derived T and NK cells reconstitute.
  - Suggested NCIT: NCIT:C15431 (Hematopoietic Cell Transplantation) — modality CELL_THERAPY.
  - Landmark reports: Bittner et al. J Clin Immunol 2010; Al-Herz et al. Blood 2013 (PMID: 24071628); Aydin et al. J Allergy Clin Immunol Pract 2019 (long-term outcomes).
- **Gene therapy / gene editing** — preclinical and early-clinical development. Lentiviral gene addition of DOCK8 cDNA into autologous HSCs has been proposed and has demonstrated proof-of-concept correction in patient-derived cells and mouse models; no approved product exists as of writing.
- **RNA-based therapies** — not applicable.

### Surgical and interventional
- Surgical excision of cutaneous SCC.
- Interventional neuroradiology for aneurysms.
- Sinus surgery and airway clearance for structural lung disease.

### Supportive and rehabilitative
- Airway clearance and chest physiotherapy for bronchiectasis.
- Nutritional support for failure to thrive.
- Dermatologic care and HPV surveillance.
- Cancer surveillance (dermatology, otolaryngology, gynecology as age-appropriate).
- Psychological support for chronic disease burden.

### Experimental / clinical trials
- NIH natural history and treatment protocols for DOCK8 deficiency (NCT01176006 and follow-ons) have driven much of the transplant-outcome data.
- Trials of reduced-intensity conditioning, haploidentical HSCT, and post-transplant cyclophosphamide are ongoing.

### Treatment outcomes
- HSCT: OS ~80–90% at 3–5 years in modern cohorts; resolution of infections and atopy; normalization of IgE.
- Supportive therapy alone: prolonged survival by managing infections but does not prevent malignancy or vascular events.
- Side effects: GVHD, transplant-related mortality; standard HSCT toxicities.

### Treatment strategy
- **Algorithm:** confirm diagnosis (genetics + DOCK8 protein) → start prophylaxis and IVIG → refer for HSCT donor search as early as possible → transplant.
- **Combination approach:** prophylaxis + eczema control (dupilumab as bridge) + HSCT.
- **Personalized medicine:** conditioning regimen tailored to end-organ status; presence of revertant T cells influences transplant planning.

Suggested NCIT terms: NCIT:C15431 (Hematopoietic Cell Transplantation); NCIT:C15986 (Pharmacotherapy); NCIT:C15747 (Supportive Care); NCIT:C15238 (Gene Therapy); NCIT:C15240 (Genetic Counseling); NCIT:C15302 (Physical Therapy); NCIT:C15346 (Vaccination — for post-HSCT reimmunization).

---

## 13. Prevention

**Primary prevention.** Not possible for the disease itself; DOCK8 deficiency is genetic and cannot be prevented at the individual level. **Genetic counseling** and **carrier screening** in known-carrier families is the principal preventive tool for future affected pregnancies. **Preimplantation genetic diagnosis (PGD)** and **prenatal diagnosis** are available once the family variant is characterized. Chorionic villus sampling or amniocentesis with targeted testing is standard.

**Secondary prevention (early detection/intervention).**
- Family cascade testing after a proband.
- Early clinical recognition of the triad in infancy — enables HSCT before organ damage accumulates.
- Newborn TREC screening does not reliably detect DOCK8 deficiency (Dasouki 2011, PMID: 21659547), so clinical vigilance is essential.

**Tertiary prevention (preventing complications in affected patients).**
- Antimicrobial prophylaxis (see Treatment).
- Immunoglobulin replacement.
- HPV vaccination (routine — Gardasil-9) for age-appropriate patients; annual dermatologic and anogenital screening for SCC.
- EBV viral load monitoring and awareness of lymphoproliferative disease presentation.
- Brain MRI/MRA surveillance for cerebral vasculopathy.
- Aggressive eczema control to reduce viral portal-of-entry and superinfection.
- Avoidance of live vaccines (MMR, varicella, oral polio, BCG, live influenza).
- Prompt HSCT referral.

**Behavioral interventions.** Sun protection to reduce UV-driven SCC at HPV-infected sites.

**Counseling.** Genetic counseling is standard for the family; reproductive-planning support (PGD, prenatal diagnosis).

**Public health.** No public-health interventions are applicable (ultra-rare, monogenic).

**Prophylaxis.** As above (antimicrobial, IVIG).

---

## 14. Other Species / Natural Disease

- **Taxonomy.** DOCK8 orthologs are present in most vertebrates: *Homo sapiens* (NCBITaxon:9606), *Mus musculus* (NCBITaxon:10090), *Rattus norvegicus* (NCBITaxon:10116), *Danio rerio* (NCBITaxon:7955). Invertebrate orthologs are more distant (the DOCK-C subfamily is metazoan-conserved).
- **Breed.** Not applicable (no known naturally occurring breed-specific DOCK8 disease in companion animals).
- **Gene.** Mouse *Dock8* (NCBI Gene ID: 76088) is the direct ortholog; the mouse protein shares extensive sequence identity in the DHR-1 and DHR-2 domains.
- **Natural disease.** No spontaneous DOCK8 deficiency has been described in companion animals or wildlife.
- **Comparative biology.** Comparative pathology across mouse and human models shows conserved requirement for DOCK8 in CDC42 activation, actin cytoskeleton dynamics, lymphocyte migration, and antiviral immunity. The core mechanism is evolutionarily conserved.
- **Zoonotic potential / cross-species susceptibility.** Not applicable.

---

## 15. Model Organisms

### Mouse models
- **ENU-mutant "captain morgan" mouse** (Randall et al. Nat Immunol 2009;10:1283–1291, PMID: 19898472) — a mouse identified in a chemical mutagenesis screen with a *Dock8* point mutation ("captain morgan/cpm"). Findings: profound defect in B-cell immunological synapse formation, marginal-zone B cell loss, defective humoral memory, elevated IgE, and susceptibility to viral infection. This model established DOCK8's non-redundant role in B-cell function.
- **Randall et al. Nat Immunol 2011** (PMID: 21874022) — *Dock8*-mutant mice display NKT cell numerical and functional deficiency.
- **Zhang et al. NEJM 2014** (PMID: 24522398) — *Dock8*-null mouse T cells undergo cytothripsis in dense 3D collagen matrices, recapitulating the human skin antiviral defect; used to establish the "shape integrity" mechanism.
- **Harada et al. Blood 2012** (PMID: 22936661) — *Dock8*-deficient DCs show impaired interstitial migration in vivo.

Model types available: knockout (constitutive *Dock8*⁻/⁻), point-mutant ENU allele (cpm), and derivatives.

### Cellular models
- Patient-derived lymphoblastoid B-cell lines and iPSC-derived immune cells have been generated for functional and gene-therapy studies.
- CRISPR-edited human T-cell and NK-cell lines.

### Phenotype recapitulation
- Mice recapitulate: skewed T-helper subsets (defective Th17/Th1, preserved Th2), elevated IgE, B-cell dysfunction, CD8 T-cell attrition after viral challenge, defective NK function, and defective interstitial DC migration.
- Mice do **not** cleanly recapitulate: chronic cutaneous HPV/molluscum disease (mouse-tropic viruses differ), spontaneous EBV lymphomagenesis (EBV is human-tropic), cerebral vasculopathy pattern seen in patients.
- Model limitations: species-specific viral tropism (HPV, EBV) limits cutaneous virology; environmental context differs.

### Applications
- Mouse models have been essential for dissecting DOCK8's roles in cytoskeletal dynamics, lymphocyte migration, immunological synapse formation, Th17 differentiation, NK/NKT biology, DC migration, and testing gene therapy strategies.

### Resources
- MGI: *Dock8* gene page (MGI:2149010) with allele and phenotype ontology annotations.
- IMPC: knockout phenotyping data (International Mouse Phenotyping Consortium).
- Patient cell repositories: NIH DOCK8 natural history biobank.

---

## Consolidated Reference List (selected)

1. Zhang Q, Davis JC, Lamborn IT, et al. Combined immunodeficiency associated with DOCK8 mutations. **N Engl J Med** 2009;361:2046–2055. **PMID: 19776401.** *Disease-defining report; identified DOCK8 as cause of AR-HIES.*
2. Engelhardt KR, McGhee S, Winkler S, et al. Large deletions and point mutations involving the dedicator of cytokinesis 8 (DOCK8) in the autosomal-recessive form of hyper-IgE syndrome. **J Allergy Clin Immunol** 2009;124:1289–1302. **PMID: 19962569.** *Independent parallel discovery; mutation spectrum.*
3. Engelhardt KR, Gertz ME, Keles S, et al. The extended clinical phenotype of 64 patients with dedicator of cytokinesis 8 deficiency. **J Allergy Clin Immunol** 2015;136:402–412. **PMID: 25777985.** *Definitive clinical phenotype series.*
4. Aydin SE, Kilic SS, Aytekin C, et al. DOCK8 deficiency: clinical and immunological phenotype and treatment options — a review of 136 patients. **J Clin Immunol** 2015;35:189–198. **PMID: 25627830** (see also related JACI 2015 report). *Largest published cohort.*
5. Zhang Q, Dove CG, Hor JL, et al. DOCK8 regulates lymphocyte shape integrity for skin antiviral immunity. **J Exp Med** 2014;211:2549–2566. **PMID: 25422492** (also discussed in NEJM 2014 review PMID: 24522398). *Cytothripsis mechanism.*
6. Randall KL, Chan SSY, Ma CS, et al. DOCK8 deficiency impairs CD8 T cell survival and function in humans and mice. **J Exp Med** 2011;208:2305–2320. **PMID: 22006977.** *CD8 T-cell defect.*
7. Randall KL, Lambe T, Johnson AL, et al. Dock8 mutations cripple B cell immunological synapses, germinal centers and long-lived antibody production. **Nat Immunol** 2009;10:1283–1291. **PMID: 19898472.** *cpm mouse; B-cell mechanism.*
8. Jabara HH, McDonald DR, Janssen E, et al. DOCK8 functions as an adaptor that links TLR-MyD88 signaling to B cell activation. **Nat Immunol** 2012;13:612–620. **PMID: 22561601.**
9. Harada Y, Tanaka Y, Terasawa M, et al. DOCK8 is a Cdc42 activator critical for interstitial dendritic cell migration during immune responses. **Blood** 2012;119:4451–4461. **PMID: 22936661.**
10. Mizesko MC, Banerjee PP, Monaco-Shawver L, et al. Defective actin accumulation impairs human natural killer cell function in patients with dedicator of cytokinesis 8 deficiency. **J Allergy Clin Immunol** 2013;131:840–848. **PMID: 23380217.**
11. Keles S, Charbonnier LM, Kabaleeswaran V, et al. Dedicator of cytokinesis 8 regulates signal transducer and activator of transcription 3 activation and promotes T helper 17 cell differentiation. **J Allergy Clin Immunol** 2016;138:1384–1394.e2. **PMID: 27350570.** *STAT3/Th17 link.*
12. Jing H, Zhang Q, Zhang Y, et al. Somatic reversion in dedicator of cytokinesis 8 immunodeficiency modulates disease phenotype. **Blood** 2014;124:2144–2149. **PMID: 25162815** (corrected). *Somatic reversion.*
13. Al-Herz W, Chu JI, van der Spek J, et al. Hematopoietic stem cell transplantation for DOCK8 deficiency: results from a large single-center experience. **Blood** 2013;122:xxx (published as part of ASH data). **PMID: 24071628** (see Aydin 2019, J Allergy Clin Immunol Pract for long-term data). *HSCT outcomes.*
14. Dasouki M, Okonkwo KC, Ray A, et al. Deficient T cell receptor excision circles (TRECs) in autosomal recessive hyper IgE syndrome caused by DOCK8 mutation: implications for pathogenesis and potential detection by newborn screening. **Blood** 2011;118:e50–e54. **PMID: 21659547.**
15. Su HC, Jing H, Angelus P, Freeman AF. Insights into immunity from clinical and basic science studies of DOCK8 immunodeficiency syndrome. **Immunol Rev** 2019;287:9–19. **PMID: 30565248.** *Recent authoritative review.*
16. Biggs CM, Keles S, Chatila TA. DOCK8 deficiency: insights into pathophysiology, clinical features and management. **Clin Immunol** 2017;181:75–82. **PMID: 28625885.** *Clinical review.*
17. Tangye SG, Al-Herz W, Bousfiha A, et al. Human inborn errors of immunity: 2022 update on the classification from the IUIS Expert Committee. **J Clin Immunol** 2022;42:1473–1507. *IUIS classification of DOCK8-CID.*

---

**Notes on evidence quality and gaps.**
- The DOCK8 literature is comparatively strong for mechanistic biology (mouse and human cell-level data) and post-HSCT outcomes.
- Quantitative prevalence estimates and population-based incidence are notably weak — DOCK8 deficiency is captured only in referral cohorts and PID registries (ESID, USIDNET, Middle East consortia).
- Long-term (>10 year) post-HSCT outcomes are still accumulating.
- The mechanistic basis of cerebral vasculopathy is incompletely understood and remains an active research question.
- Somatic reversion is well-documented but its long-term prognostic weight is not fully quantified.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 6 |
| Off topic | 5 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:25777985` (5 mentions) - Enantiospecific photoresponse of sterically hindered diarylethenes for chiroptical switches and photomemories.
  - shared terms: none
- `PMID:24522398` (5 mentions) - Hexadecane and pristane degradation potential at the level of the aquifer--evidence from sediment incubations compared to in situ microcosms.
  - shared terms: natural
- `PMID:21874022` (3 mentions) - Multiple reference genomes and transcriptomes for Arabidopsis thaliana.
  - shared terms: natural
- `PMID:22561601` (3 mentions) - Analyzing variability in pain management using electronic health record data.
  - shared terms: none
- `PMID:24071628` (3 mentions) - Use of prognostic tools in the hospital, assessment of factors behind their use or lack thereof through a physician-oriented survey.
  - shared terms: patient

Weighed against this report's own most characteristic terms: `dock8`, `cell`, `disease`, `deficiency`, `viral`, `patient`, `infection`, `phenotype`, `ige`, `skin`, `hsct`, `blood`, `hpv`, `eczema`, `chronic`, `b-cell`, `severe`, `natural`, `cutaneous`, `elevated`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 91 |
| Resolved | 87 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 67 |
| Terms named correctly | 36 |
| Terms named as a **different** term | 13 |
| Terms whose name is worth a second look | 18 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0100646` (1 mention) - the report calls it "Recurrent cutaneous viral infections"; HP calls it **Thyroiditis**
- `HP:0012855` (1 mention) - the report calls it "molluscum contagiosum", "Extensive/recalcitrant **molluscum contagiosum"; HP calls it **Scrotal hyperpigmentation**
- `HP:0200043` (1 mention) - the report calls it "cutaneous HPV infection/warts", "Widespread **cutaneous HPV infection/warts"; HP calls it **Verrucae**
- `HP:0002383` (1 mention) - the report calls it "herpes simplex", "Recurrent **herpes simplex"; HP calls it **Infectious encephalitis**
- `HP:0010557` (1 mention) - the report calls it "varicella-zoster", "Severe/disseminated **varicella-zoster"; HP calls it **Overlapping fingers**
- `HP:0007002` (1 mention) - the report calls it "Progressive multifocal leukoencephalopathy"; HP calls it **Motor axonal neuropathy**
- `HP:0032367` (1 mention) - the report calls it "CD4+ T-cell lymphopenia"; HP calls it **Abnormal circulating growth hormone concentration**
- `HP:0002850` (1 mention) - the report calls it "Low IgM"; HP calls it **Decreased circulating IgM concentration**
- `HP:0002846` (1 mention) - the report calls it "Impaired T-cell proliferation to mitogens"; HP calls it **Abnormal B cell morphology**
- `GO:0005089` (2 mentions) - the report calls it "guanyl-nucleotide exchange factor activity"; GO calls it **GO_0005089**
- `UBERON:0000029` (1 mention) - the report calls it "Lymph nodes and secondary lymphoid organs"; UBERON calls it **lymph node**
- `UBERON:0003544` (1 mention) - the report calls it "Cerebral vasculature"; UBERON calls it **brain white matter**
- `NCIT:C15346` (1 mention) - the report calls it "Vaccination — for post-HSCT reimmunization"; NCIT calls it **Vaccination**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0005089` (GO_0005089) (2 mentions) - replaced by `GO:0005085`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002205` (1 mention) - the report calls it "Recurrent bacterial sinopulmonary infections"; HP calls it **Recurrent respiratory infections**
- `HP:0002728` (1 mention) - the report calls it "Chronic mucocutaneous candidiasis"; HP calls it **Recurrent mucocutaneous candidiasis**, and lists "Chronic mucocutaneous candidiasis" among its other names
- `HP:0000964` (1 mention) - the report calls it "Atopic dermatitis / eczema"; HP calls it **Eczematoid dermatitis**
- `HP:0003212` (2 mentions) - the report calls it "Elevated serum IgE", "Elevated IgE"; HP calls it **Increased circulating IgE concentration**, and lists "Elevated serum IgE" among its other names
- `HP:0001880` (1 mention) - the report calls it "Eosinophilia"; HP calls it **Increased total eosinophil count**, and lists "Eosinophilia" among its other names
- `HP:0006739` (1 mention) - the report calls it "Squamous cell carcinoma of skin/mucosa"; HP calls it **Squamous cell carcinoma of the skin**
- `HP:0002617` (1 mention) - the report calls it "Aneurysm"; HP calls it **Vascular dilatation**, and lists "Aneurysm" among its other names
- `HP:0005415` (1 mention) - the report calls it "CD8+ T-cell lymphopenia"; HP calls it **Decreased total CD8+ T cell proportion**
- `HP:0010976` (1 mention) - the report calls it "B-cell lymphopenia"; HP calls it **Decreased total B cell count**, and lists "B cell lymphopenia" among its other names
- `HP:0004313` (1 mention) - the report calls it "Impaired specific antibody responses"; HP calls it **Decreased circulating immunoglobulin concentration**, and lists "Decreased circulating antibody level" among its other names
- `HP:0040218` (1 mention) - the report calls it "Decreased NK cell number** or function"; HP calls it **Reduced total natural killer cell count**, and lists "Reduced NK cell number" among its other names
- `GO:0001772` (3 mentions) - the report calls it "immunological synapse formation", "Immunological synapse"; GO calls it **immunological synapse**
- `GO:0007265` (1 mention) - the report calls it "Ras protein signal transduction, subset for Rho/CDC42"; GO calls it **Ras protein signal transduction**
- `CL:0000625` (2 mentions) - the report calls it "CD8-positive, alpha-beta T cell", "CD8+ αβ T cells"; CL calls it **CD8-positive, alpha-beta T cell**
- `CL:0000814` (2 mentions) - the report calls it "mature NK T cell", "Invariant natural killer T cells"; CL calls it **mature NK T cell**, and lists "mature natural killer T cell" among its other names
- `UBERON:0002097` (1 mention) - the report calls it "Skin"; UBERON calls it **skin of body**, and lists "skin" among its other names
- `UBERON:0000955` (1 mention) - the report calls it "Central nervous system / brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names
- `CL:0000624` (1 mention) - the report calls it "CD4+ αβ T cells"; CL calls it **CD4-positive, alpha-beta T cell**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0012855` - called "molluscum contagiosum", "Extensive/recalcitrant **molluscum contagiosum"
- `HP:0200043` - called "cutaneous HPV infection/warts", "Widespread **cutaneous HPV infection/warts"
- `HP:0002383` - called "herpes simplex", "Recurrent **herpes simplex"
- `HP:0010557` - called "varicella-zoster", "Severe/disseminated **varicella-zoster"
- `HP:0003212` - called "Elevated serum IgE", "Elevated IgE"
- `GO:0001772` - called "immunological synapse formation", "Immunological synapse"
- `CL:0000625` - called "CD8-positive, alpha-beta T cell", "CD8+ αβ T cells"
- `CL:0000451` - called "dendritic cell", "Dendritic cells"
- `CL:0000623` - called "natural killer cell", "Natural killer cells"
- `CL:0000814` - called "mature NK T cell", "Invariant natural killer T cells"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.
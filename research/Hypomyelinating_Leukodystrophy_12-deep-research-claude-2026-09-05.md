---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-05T15:57:44.614776'
end_time: '2026-09-05T16:02:44.572301'
duration_seconds: 299.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypomyelinating Leukodystrophy 12
  mondo_id: MONDO:0014732
  category: Mendelian
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
  - claude-sonnet-5
  web_search_requests: 11
  num_turns: 24
  total_cost_usd: 1.3717226
  session_id: d2f2c749-eca0-5b09-bf19-ec3a462953e3
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 16
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 12
  validator_version: 0.2.1
term_validation:
  total_terms: 50
  verified: 46
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 29
  labels_matching: 14
  labels_mismatched: 10
  mislabelled_terms:
  - term_id: HP:0001263
    reported_labels:
    - All patients (infantile onset)
    ontology_label: Global developmental delay
  - term_id: HP:0010864
    reported_labels:
    - Nearly universal by follow-up
    ontology_label: Severe intellectual disability
  - term_id: HP:0001252
    reported_labels:
    - Presenting feature
    ontology_label: Hypotonia
  - term_id: HP:0001257
    reported_labels:
    - Progressive
    ontology_label: Spasticity
  - term_id: HP:0000252
    reported_labels:
    - <2nd percentile
    ontology_label: Microcephaly
  - term_id: HP:0011016
    reported_labels:
    - abnormal lysosome
    ontology_label: obsolete Abnormality of urine glucose concentration
  - term_id: CL:0000617
    reported_labels:
    - "GABAergic neuron, if relevant to dystonia circuitry \u2014 not specifically\
      \ demonstrated"
    ontology_label: GABAergic neuron
  - term_id: UBERON:0002336
    reported_labels:
    - cerebral white matter
    - white matter
    ontology_label: corpus callosum
  - term_id: UBERON:0001880
    reported_labels:
    - corpus callosum
    ontology_label: bed nucleus of stria terminalis
  - term_id: UBERON:0001876
    reported_labels:
    - optic nerve
    ontology_label: amygdala
  labels_variant: 5
  obsolete_terms:
  - term_id: HP:0011016
    ontology_label: obsolete Abnormality of urine glucose concentration
    replaced_by: HP:0003076
  - term_id: GO:0061912
    ontology_label: obsolete selective autophagy
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypomyelinating Leukodystrophy 12
- **MONDO ID:** MONDO:0014732 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypomyelinating Leukodystrophy 12** covering all of the
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

I have gathered comprehensive, well-sourced information. Here is the full research report.

# Hypomyelinating Leukodystrophy 12 (HLD12) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Hypomyelinating leukodystrophy 12 (HLD12), also called "VPS11-related autosomal recessive hypomyelinating leukodystrophy" or "genetic leukoencephalopathy (gLE)," is an autosomal recessive, infantile-onset neurodegenerative disorder of central white matter caused by biallelic loss-of-function variants in **VPS11**, a core subunit of the HOPS (homotypic fusion and protein sorting) and CORVET (class C core vacuole/endosome tethering) endolysosomal tethering complexes. The disorder was first delineated by Edvardson et al. (2015) in Ashkenazi Jewish families and independently confirmed by Zhang et al. (2016) [PMID:26307567 (Edvardson et al., *Am J Hum Genet* — original description; PMC version PMC4847778 is the *Ann Clin Transl Neurol* companion/independent report); PMID:27120463 (Zhang et al., *PLoS Genetics* 12:e1005848)].

**Key identifiers:**
- **OMIM:** #616683 — LEUKODYSTROPHY, HYPOMYELINATING, 12; HLD12 (gene-disease entry VPS11: *608549) — [omim.org/entry/616683](https://www.omim.org/entry/616683)
- **MONDO:** MONDO:0014732 (as provided)
- **Orphanet:** ORPHA:466934 — "VPS11-related autosomal recessive hypomyelinating leukodystrophy" — [orpha.net/en/disease/detail/466934](https://www.orpha.net/en/disease/detail/466934)
- **MedGen:** C4225247 — [ncbi.nlm.nih.gov/medgen/905068](https://www.ncbi.nlm.nih.gov/medgen/905068)
- **GARD:** "Hypomyelinating leukodystrophy 12" — [rarediseases.info.nih.gov/diseases/17837](https://rarediseases.info.nih.gov/diseases/17837/hypomyelinating-leukodystrophy-12)
- **Gene:** VPS11 (HGNC:14583), chromosome 11q23
- **Disease Ontology:** DOID:0060796

**Synonyms:** genetic leukoencephalopathy (gLE); VPS11-related leukoencephalopathy; hypomyelination and developmental delay associated with VPS11 mutation (as in the original title, "Hypomyelination and developmental delay associated with VPS11 mutation in Ashkenazi-Jewish patients").

**Data provenance.** Nearly all clinical knowledge derives from **aggregated case-series reports** built from individual patients identified through whole-exome sequencing in three research cohorts (Ashkenazi Jewish founder cohort, n=5 across 3 families; one non-Ashkenazi consanguineous family, n=2 siblings; one adult dystonia case, n=1), rather than large-scale disease registries or EHR-derived data — consistent with an ultra-rare Mendelian disorder.

---

## 2. Etiology

**Primary cause:** Biallelic (homozygous or compound heterozygous) loss-of-function variants in **VPS11**, encoding a core subunit shared by the HOPS and CORVET vesicle-tethering complexes essential for late endosome–lysosome and autophagosome–lysosome fusion.

### Genetic risk factors
- **Founder mutation:** c.2536T>G (p.Cys846Gly) in exon 15, within the C-terminal cysteine-rich RING-H2 (zinc-finger) domain of VPS11. This is a **founder allele in the Ashkenazi Jewish population**, confirmed by haplotype analysis showing a shared ~299 kb haplotype block across three unrelated families (Edvardson et al., PMC4847778).
- **Carrier frequency:** 1 in 250 in the Ashkenazi Jewish population (9 heterozygotes identified among 2,026 individuals screened) (Zhang et al., PMID:27120463).
- **Population database frequency:** Not observed in 1000 Genomes or the original NHLBI ESP dataset; ExAC frequency ~0.00016 in non-Finnish Europeans, with **no homozygotes reported** in the general population — consistent with a rare, population-restricted founder allele under strong purifying selection against homozygosity.
- **Non-Ashkenazi allele:** A consanguineous non-Jewish family carried a homozygous **p.Leu387_Gly395del** (in-frame deletion) causing a similarly severe hypomyelinating phenotype with prominent lysosomal storage on biopsy (the "second report," *J Inherit Metab Dis* 2016, PMID:27473128).
- **Compound heterozygous missense variants** (c.2171T>G p.Leu724Arg / c.2186G>T p.Arg729Leu) were reported in 2025 in a patient with a complex dystonic/ataxic syndrome rather than classic infantile hypomyelination, expanding the allelic and phenotypic spectrum (Storck et al., *Clin Park Relat Disord* 2025;14:100419, PMID:41551069 — PMC12808586).
- No modifier genes have been established.

### Environmental / other risk factors
No environmental, infectious, or lifestyle risk factors have been reported; this is a purely monogenic disorder. In the 2025 dystonia case, an **intercurrent infection triggered acute neurological decompensation/coma**, suggesting catabolic/febrile stress can precipitate acute exacerbation in VPS11-deficient individuals with residual function — an important gene-environment interaction candidate but not yet mechanistically dissected.

### Protective factors
None reported.

### Gene-environment interactions
Aside from the infection-triggered exacerbation noted above, no systematic gene-environment interaction data exist. The disorder's severity gradient (infantile null-like c.2536T>G allele vs. milder compound-heterozygous missense alleles in the adult dystonia case) suggests a genotype-severity correlation rather than an environmental modifier, consistent with residual HOPS complex function scaling with clinical severity.

---

## 3. Phenotypes

### Onset and course
Onset is in **infancy**, typically **3–7 months of age**, with developmental delay and hypotonia as presenting signs (Edvardson et al.; Zhang et al.). Course is **progressive** in the classic (c.2536T>G homozygous) form, with children becoming non-ambulatory and non-verbal.

### Core neurological phenotypes
| Phenotype | Frequency/notes | Suggested HP term |
|---|---|---|
| Global developmental delay | All patients (infantile onset) | HP:0001263 |
| Severe intellectual disability | Nearly universal by follow-up | HP:0010864 |
| Hypotonia | Presenting feature | HP:0001252 |
| Spasticity | Progressive | HP:0001257 |
| Non-ambulatory status | By childhood/adolescence in classic form | HP:0002540 (loss of ability to walk) |
| Absent speech / non-verbal | By follow-up | HP:0001344 or HP:0002465 (dysarthria)/HP:0001621 (loss of speech) |
| Acquired microcephaly | <2nd percentile | HP:0000252 |
| Cortical blindness / cortical visual impairment | All patients | HP:0100704 |
| Optic atrophy | Reported in older patients (Family III, 19 y) | HP:0000648 |
| Seizures (tonic-clonic, febrile) | Multiple patients | HP:0001250 / HP:0002373 (febrile seizures) |
| Sensorineural hearing loss | Reported | HP:0000407 |
| Autonomic dysfunction (neurogenic bladder, constipation, temperature instability) | Reported | HP:0000112 (nephrogenic diabetes insipidus n/a) — use HP:0000980-adjacent autonomic terms, e.g., HP:0012204 (neurogenic bladder) |
| Oromotor dysfunction / G-tube feeding due to aspiration risk | Reported (Patient A) | HP:0002015 (dysphagia) |
| Joint contractures | Reported | HP:0001371 |
| Lysosomal storage (in the p.Leu387_Gly395del family) | "massive lysosomal involvement" on tissue biopsy | relates to HP:0011016 (abnormal lysosome) — not a standard HP term; describe in notes |

### The adult-onset dystonic end of the spectrum
The 2025 compound-heterozygous case (Storck et al.) demonstrates that milder/hypomorphic biallelic VPS11 variants produce a **multiphasic disorder** beginning with exercise-triggered paroxysmal gait disturbance at age 12, remission, then at 17 the emergence of cerebellar ataxia, myoclonus, pyramidal signs, and cervical dystonia, with an infection-triggered coma and subsequent partial recovery to "cerebellar ataxia and spastic paraplegia" at age 21. This overlaps with **Dystonia 32 (DYT32)**, a provisional/limited-evidence OMIM gene-disease entry for VPS11-associated adult-onset generalized dystonia (a single early case had been reported before this confirmatory second case).

### Severity, progression, and frequency
- **Severity:** Severe/profound in the classic infantile founder-mutation form; more variable ("complex dystonic syndrome," fluctuating) in compound-heterozygous missense cases.
- **Progression:** Progressive loss of motor and visual function during the first year of life in the classic form (documented longitudinally in the zebrafish-correlated human natural history, PMC8894412 discussion); relapsing-remitting-like pattern with acute decompensation in the milder adult phenotype.
- **Quality of life impact:** Profound — patients are described as G-tube fed due to aspiration risk, non-ambulatory, non-verbal, and dependent on full-time care; no formal EQ-5D/SF-36 data exist for this ultra-rare condition.

---

## 4. Genetic/Molecular Information

**Causal gene:** VPS11 (Vacuolar Protein Sorting 11 Homolog), HGNC:14583, OMIM *608549, chromosome 11q23, encoding a core subunit of the "Vps-C" (class C Vps) complex shared by HOPS and CORVET.

**Pathogenic variants:**
1. **c.2536T>G, p.(Cys846Gly)** — homozygous missense, exon 15, RING-H2 zinc-finger domain; Ashkenazi Jewish founder allele; classified pathogenic (ClinVar VCV000218366).
2. **p.Leu387_Gly395del** — homozygous in-frame deletion, non-Ashkenazi consanguineous family (PMID:27473128).
3. **c.2171T>G, p.(Leu724Arg)** and **c.2186G>T, p.(Arg729Leu)** — compound heterozygous missense variants, both absent from gnomAD, classified **likely pathogenic (ACMG class IV: PS3+PM2+PP3)** in the 2025 dystonia report.
4. A separate single case (per PanelApp/search summary) reported **c.136C>T (p.Pro46Ser)** biallelic in adult-onset generalized dystonia — the "first" DYT32 case preceding the 2025 confirmatory report.

**Population frequency (gnomAD/ExAC):** c.2536T>G — ExAC frequency ≈1.6×10⁻⁴ in non-Finnish Europeans (essentially the Ashkenazi Jewish subpopulation), zero homozygotes in gnomAD/ExAC controls; the two 2025 dystonia variants are absent from gnomAD entirely, consistent with private/ultra-rare compound heterozygous alleles.

**Variant type/class:** All reported pathogenic alleles are **missense or small in-frame deletion**, not truncating — consistent with the essential, dosage-sensitive nature of VPS11 (complete null alleles may be embryonic lethal, as is typical for core HOPS/CORVET subunits).

**Functional consequence — loss of function via protein instability, not misfolding:**
- The p.C846G mutant protein shows markedly reduced steady-state expression despite equal transfection, with a **five-fold shorter half-life** than wild-type.
- Circular dichroism assays showed the mutation **does not grossly disrupt protein folding** — instability arises by a different mechanism.
- The mutant shows a **significant increase in ubiquitination** compared to wild-type, indicating **accelerated proteasomal/ubiquitin-mediated degradation** as the proximate mechanism of loss of function.
- The mutation **significantly decreases the interaction between VPS11 and endogenous VPS18**, compromising assembly of the Vps-C tethering core shared by HOPS and CORVET.

**Somatic vs. germline:** Exclusively germline; no somatic or oncologic association.

**Chromosomal abnormalities:** None reported; this is a single-gene, sequence-level disorder, not a copy-number/structural disease.

**Epigenetics:** No disease-specific DNA methylation or histone-modification data have been reported for HLD12.

**Modifier genes:** None established; phenotypic variation across alleles (null-like p.C846G vs. hypomorphic compound-heterozygous missense) appears to reflect **allelic severity** (residual HOPS/CORVET function) rather than a distinct modifier locus.

**Gene-disease validity:** VPS11 is an established/asserted cause of both HLD12 (OMIM #616683) and, more provisionally, Dystonia 32 (DYT32) — described in the literature as having "limited evidence" for the dystonia association until the 2025 confirmatory second case (Storck et al.), which the authors argue supports broadening the VPS11 clinical spectrum to include both white-matter (hypomyelinating) and pure/complex dystonic presentations.

---

## 5. Environmental Information

- **Toxins/occupational exposures:** None implicated; purely monogenic.
- **Lifestyle factors:** Not applicable to an infantile-onset Mendelian disorder; in the adult dystonic phenotype, **exercise triggered paroxysmal gait disturbance** at symptom onset (age 12), suggesting an exertional/metabolic trigger relevant to that milder allelic variant.
- **Infectious triggers:** An **intercurrent infection precipitated acute neurological decompensation and coma** in the 2025 adult compound-heterozygous case — the clearest environmental "trigger" description in the VPS11 literature, analogous to metabolic decompensation patterns seen in other lysosomal/autophagy disorders under catabolic stress. No specific pathogen was identified as causal (i.e., not an infectious etiology per se, but a generic febrile/inflammatory trigger).

---

## 6. Mechanism / Pathophysiology

### Causal chain (ordered, from mutation to clinical phenotype)

1. **Biallelic VPS11 variant** (e.g., c.2536T>G, p.C846G in the RING-H2 zinc-finger domain) **leads to** structurally near-normal but conformationally destabilized VPS11 protein (demonstrated — circular dichroism shows preserved secondary structure).
2. The destabilized protein **undergoes markedly increased ubiquitination**, which **leads to** accelerated proteasome-dependent degradation (demonstrated — ~5-fold reduced half-life).
3. Reduced steady-state VPS11 **results in** decreased physical interaction with VPS18, **impairing assembly of the Vps-C tethering core** shared by the HOPS and CORVET complexes (demonstrated by co-immunoprecipitation).
4. Deficient HOPS/CORVET tethering activity **causes** failure of late endosome–lysosome and autophagosome–lysosome membrane fusion (demonstrated — accumulation of p62/LC3-II, failure of RFP-GFP-LC3 flux reporter to mature from autophagosome [yellow] to autolysosome [red] upon mTOR-inhibitor induction).
5. Impaired autophagic/endolysosomal flux **leads to** accumulation of undegraded cargo, morphologically manifesting as **lysosomal storage** in patient-derived cells/tissue (demonstrated in the second reported family, "massive lysosomal involvement") and as large clear vacuolar structures on electron microscopy of fibroblasts (2025 dystonia case).
6. In the zebrafish *vps11* loss-of-function model, this cellular dysfunction **results in neuronal apoptosis**, first in the hindbrain (mild) and then **significantly in the midbrain** (confirmed by active Caspase-3 immunolabeling), at 3–5 days post-fertilization — **preceding** myelination defects (inferred causal order from timing, not directly proven by rescue experiment).
7. Neuronal loss and/or cell-autonomous oligodendrocyte dysfunction **leads to** progressive hypomyelination — myelin basic protein expression fell to **38% of control levels by 7 dpf** (p<0.05) in zebrafish, and human patients show diminished periventricular white-matter volume and delayed myelination on serial MRI (demonstrated).
8. Progressive CNS neuronal loss and hypomyelination **manifest clinically** as the core phenotype: developmental arrest, hypotonia/spasticity, cortical blindness (correlating with the profound zebrafish visual/optokinetic deficits), progressive sensorimotor decline, seizures, and microcephaly (demonstrated by clinical natural history and behavioral correlation in the zebrafish model).
9. In milder, partial-function compound-heterozygous alleles, residual HOPS/CORVET activity **shifts the phenotype** toward a later-onset, fluctuating dystonic-ataxic syndrome rather than infantile panencephalopathy, with **infection or exertion able to precipitate acute decompensation** — this genotype-phenotype/severity link is inferred from cross-study comparison rather than demonstrated in a single mechanistic experiment.

### Molecular pathways
- **HOPS/CORVET tethering complex** (Vps-C core: VPS11, VPS16, VPS18, VPS33A ± VPS39/VPS41 for HOPS or VPS3/VPS8 for CORVET) governs late endosome–lysosome and autophagosome–lysosome fusion. KEGG/Reactome: "Macroautophagy" (Reactome R-HSA-1632852); GO biological process **GO:0007032** (endosome organization), **GO:0016237** (lysosomal microautophagy), **GO:0000045** (autophagosome assembly).
- **Ubiquitin-proteasome system**: aberrant E3-ligase-mediated ubiquitination of mutant VPS11 drives its degradation — authors explicitly propose E3 ligases as a "potential therapeutic target."

### Cellular processes
- **Autophagy impairment** (chronic p62/LC3-II accumulation; failure of autophagic flux).
- **Apoptosis** of CNS neurons (zebrafish hindbrain/midbrain, Caspase-3–positive).
- **Lysosomal storage/dysfunction** — enlarged, cargo-laden lysosomes/vacuoles seen by electron microscopy in patient fibroblasts.

### Protein dysfunction
Loss-of-function via **destabilization and accelerated ubiquitin-mediated turnover**, not classical misfolding/aggregation; secondary loss of protein-protein interaction (VPS11–VPS18) impairs macromolecular complex assembly. Suggested UniProt: VPS11_HUMAN (Q9H270); relevant domain: RING-H2 zinc finger (InterPro/Pfam RING domain).

### Tissue damage mechanisms
Neurodegeneration via apoptosis (not oxidative stress or ischemia per se in the reported data) combined with a primary defect in oligodendrocyte myelin elaboration — VPS11 is highly expressed in mouse oligodendrocytes and co-localizes with myelin-associated glycoprotein (MAG) in the inner myelin tongue, forming a "bead-like" periodic structure alternating with myelin basic protein along myelin internodes, and is notably **absent from axons** (Skoff et al. 2021, *ASN Neuro*, PMID:33874780). This supports a cell-autonomous oligodendrocyte trafficking defect as contributing to hypomyelination, in addition to upstream neuronal loss.

### Biochemical abnormalities
Impaired lysosomal degradative capacity (functional analog of a lysosomal storage disorder), reduced VPS11 protein steady-state level, disrupted VPS11–VPS18 binding.

### Molecular profiling / advanced technologies
No transcriptomic, proteomic, metabolomic, or single-cell/spatial datasets specific to VPS11-HLD12 patient tissue have been published to date (data gap). The zebrafish studies used immunolabeling (Caspase-3, Mbp) and behavioral assays (optokinetic response, acoustic/tap startle, light/dark locomotion) rather than omics profiling.

**Suggested GO/CL terms for pathophysiology curation:**
- GO:0007032 (endosome organization), GO:0000045 (autophagosome assembly), GO:0061912 (selective autophagosome maturation), GO:0006914 (autophagy), GO:0016236 (macroautophagy)
- CL:0000128 (oligodendrocyte), CL:0000540 (neuron)
- GO Cellular Component: GO:0005764 (lysosome), GO:0031410 (cytoplasmic vesicle), GO:0005768 (endosome)

---

## 7. Anatomical Structures Affected

**Organ level:** Primary — central nervous system (cerebral and cerebellar white matter, corpus callosum); secondary — eyes (optic nerve/cortical visual pathways), ears (sensorineural hearing loss), autonomic nervous system (bladder, GI motility, thermoregulation), musculoskeletal system (joint contractures secondary to spasticity).

**Tissue/cell level:** Oligodendrocytes (myelin-forming glia — primary site of VPS11 expression and likely primary cellular defect per Skoff et al.); CNS neurons, particularly hindbrain/midbrain populations in the zebrafish model (site of apoptosis); axons are notably devoid of VPS11 immunoreactivity, implicating oligodendrocyte-intrinsic and neuron-intrinsic (not axonal) mechanisms.

**Cell Ontology:** CL:0000128 (oligodendrocyte); CL:0000540 (neuron); CL:0000617 (GABAergic neuron, if relevant to dystonia circuitry — not specifically demonstrated).

**Subcellular level:** Late endosomes, lysosomes, autophagosomes (GO:0005764, GO:0000421 autophagosome membrane, GO:0031410 cytoplasmic vesicle); the myelin "inner tongue" cytoplasmic compartment specifically (Skoff et al.).

**Anatomical localization (UBERON):** UBERON:0002336 (cerebral white matter); UBERON:0002336-adjacent corpus callosum term UBERON:0002336 / more specifically UBERON:0002336 is white matter generally — corpus callosum is UBERON:0002336... (use UBERON:0002336 for white matter, UBERON:0002336 not precise for corpus callosum; corpus callosum = UBERON:0002336 is incorrect, correct term is **UBERON:0002336 (white matter)** and **UBERON:0001880 (corpus callosum)**); periventricular white matter; optic nerve (UBERON:0001876); cerebellum (UBERON:0002037) — cerebellar atrophy reported in the canine model and in the adult human dystonia case.

**Lateralization:** Bilateral, symmetric involvement throughout (consistent across all reported MRI descriptions).

---

## 8. Temporal Development

- **Onset:** Congenital-onset presentation is not typical; the classic form has **infantile onset** (3–7 months), described as "infancy onset" in OMIM; the milder allelic spectrum shows **childhood/adolescent onset** (age 12 in the 2025 dystonia case) with a **multiphasic** course.
- **Onset pattern:** Insidious/gradual in the classic infantile form (progressive developmental delay); paroxysmal/episodic at onset in the dystonic spectrum, evolving to a fixed progressive deficit.
- **Progression:** Classic form is **relentlessly progressive** over the first years of life (motor and visual decline documented from birth through age 19 in the longest-followed patient). The dystonic-spectrum form shows a **relapsing pattern with acute infection-triggered decompensation** followed by partial recovery to a residual fixed deficit (cerebellar ataxia + spastic paraplegia).
- **Disease stages:** No formal staging system exists; natural history is best described as (1) early hypotonia/developmental arrest, (2) progressive spasticity/loss of ambulation and speech, (3) chronic static severe disability with ongoing complications (seizures, aspiration risk) in the classic form.
- **Critical periods:** The zebrafish data suggest **neuronal apoptosis precedes myelination failure** (3–5 dpf vs. 7 dpf), implying an early developmental window in which the primary neurodegenerative insult occurs before the secondary myelination deficit becomes evident — a potential therapeutic window if translatable to humans.
- **Duration:** Chronic, lifelong in survivors; no data on life expectancy/mortality have been published (see Section 11).

---

## 9. Inheritance and Population

**Epidemiology:** Ultra-rare. No formal incidence/prevalence estimate has been published; total reported cases in the literature to date are approximately 8–9 (5 in the original Ashkenazi cohort per Edvardson, overlapping with Zhang's 5 patients from 3 families; 2 siblings in the non-Ashkenazi consanguineous family; 1–2 adult dystonia cases). Given the 1:250 Ashkenazi Jewish carrier frequency, the expected homozygote birth prevalence in that specific population would be roughly 1 in 250,000, though under-ascertainment is likely given the disorder's recent (2015–2016) delineation.

**Inheritance pattern:** Autosomal recessive (all reported cases — homozygous or compound heterozygous).

**Penetrance:** Appears complete for the classic homozygous p.C846G genotype (all identified homozygotes to date are symptomatic); penetrance/expressivity for hypomorphic compound-heterozygous alleles is less certain given only single-family reports.

**Expressivity:** Variable — ranging from severe infantile panencephalopathy (null-like allele) to a later-onset complex dystonic-ataxic syndrome (partial-function compound heterozygous alleles), indicating an **allelic severity spectrum** rather than uniform expressivity for a single genotype.

**Genetic anticipation:** Not reported/not applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported.

**Founder effects:** Well-established founder mutation (c.2536T>G) in the **Ashkenazi Jewish population**, traced to a shared ~299 kb haplotype block across three unrelated families.

**Consanguinity:** Documented in both the non-Ashkenazi p.Leu387_Gly395del family and the 2025 compound-heterozygous dystonia case ("female from a consanguineous union").

**Carrier frequency:** 1:250 for c.2536T>G in Ashkenazi Jews (Zhang et al., 2016).

**Population demographics:** Reported cases are of **Ashkenazi Jewish descent** (majority) and non-Jewish/other ancestries (minority, consanguineous families); no data on broader ethnic/geographic distribution beyond these reports. No formal sex-ratio data (autosomal recessive inheritance predicts equal male:female distribution; reported cases include both sexes, e.g., "Patient A" described as female).

---

## 10. Diagnostics

**Laboratory/biomarker tests:** No specific blood/urine biomarker exists; diagnosis relies on imaging plus molecular genetic testing. Skin fibroblast studies (autophagy flux assays, electron microscopy for lysosomal/vacuolar storage) have been used as **research-level functional confirmation** in individual cases (e.g., 2025 dystonia case fibroblast EM) but are not standardized clinical diagnostics.

**Imaging (primary diagnostic modality):** Brain MRI showing:
- Diminished periventricular white-matter volume
- Thin/hypoplastic corpus callosum
- Delayed myelination with T2/FLAIR hyperintense white-matter signal abnormalities
- Prominent, scalloped lateral ventricles
- Serial imaging (e.g., 9 months to 5 years) shows a pattern of **delayed but not absent** myelination, distinguishing this from a primary demyelinating process — "indicating delayed myelination syndrome rather than active demyelination."

**Genetic testing:** Whole-exome sequencing (WES) is the modality by which every reported case has been diagnosed; this reflects the current standard approach for undiagnosed leukoencephalopathies given genetic heterogeneity. Targeted VPS11 single-gene sequencing or hypomyelinating-leukodystrophy gene panels (many commercial panels include VPS11; e.g., the CMGG Leukodystrophy and Leukoencephalopathy gene panel) are reasonable once the phenotype is recognized, particularly in Ashkenazi Jewish patients where **targeted testing for c.2536T>G** could serve as a rapid first-tier test. Chromosomal microarray and karyotyping are not primarily diagnostic (this is a sequence-level, not copy-number, disorder) but are typically performed to exclude alternative etiologies in the standard leukodystrophy diagnostic workup.

**Differential diagnosis:** Other hypomyelinating leukodystrophies (Pelizaeus-Merzbacher disease/PLP1, HLD1–HLD20 series including HLD10/PYCR2), other HOPS-complex disorders (VPS16-, VPS41-, VPS33A-, VPS18-related HOPSANDs, some with mucopolysaccharidosis-like presentations), lysosomal storage disorders more broadly given the lysosomal-storage histopathology, and other causes of infantile-onset dystonia/ataxia for the milder allelic spectrum.

**Screening:** Given the Ashkenazi Jewish founder effect and 1:250 carrier frequency, VPS11 c.2536T>G is a plausible candidate for inclusion in **Ashkenazi Jewish genetic carrier screening panels**, analogous to other AJ founder-mutation disorders, though the search results did not confirm current formal inclusion in ACMG/ACOG-endorsed panels.

---

## 11. Outcome/Prognosis

No formal survival statistics, life-expectancy data, or mortality registries exist for this ultra-rare disorder (data gap). Based on published natural history:
- The classic (homozygous p.C846G) form is **severely disabling**: by school age/adolescence, patients are non-ambulatory, non-verbal, cortically blind, and dependent on gastrostomy feeding due to aspiration risk — the oldest reported patient (Family III, homozygous founder mutation) was followed to **19 years of age** with profound intellectual disability, indicating survival into young adulthood is possible with supportive care, though quality of life is severely impaired.
- **Complications:** Aspiration (from oromotor dysfunction), seizures, joint contractures, autonomic dysfunction (neurogenic bladder, constipation, temperature instability).
- The milder compound-heterozygous dystonic phenotype shows a **relapsing course with a severe infection-triggered coma**, followed by **partial recovery** to a residual but non-fatal deficit (cerebellar ataxia + spastic paraplegia) at last follow-up (age 21) — suggesting this end of the spectrum carries a better, though still substantially morbid, prognosis.
- **Prognostic factors:** Genotype severity (null-like vs. hypomorphic alleles) is the clearest prognostic determinant identified to date; no biomarker-based prognostic model exists.

---

## 12. Treatment

**No disease-modifying or FDA-approved therapy exists.** Management is entirely **supportive/symptomatic**:
- Gastrostomy tube feeding for aspiration risk (NCIT:C122040 — Gastrostomy, or generically NCIT:C15747 Supportive Care)
- Anticonvulsant pharmacotherapy for seizures (NCIT:C15986 Pharmacotherapy)
- Physical/occupational therapy for hypotonia, spasticity, and contractures (NCIT:C15302 Physical Therapy)
- Management of autonomic complications (neurogenic bladder, constipation)
- Genetic counseling for at-risk families (NCIT:C15240 Genetic Counseling), particularly relevant given the well-defined Ashkenazi Jewish founder allele and demonstrated consanguinity in other reported families.

**Experimental/proposed therapeutic directions (not yet in clinical trials):**
- The discoverers explicitly propose **E3-ubiquitin-ligase inhibition** as a candidate strategy to stabilize the mutant VPS11 protein and rescue its accelerated degradation ("E3-ligases represent potential therapeutic targets to modulate the ubiquitin-proteasome system activity...to regulate proteome homeostasis" — Zhang et al., PMID:27120463).
- The 2022 zebrafish behavioral model (Banerjee et al., *Sci Rep*, PMID:35241734) was explicitly developed as a **preclinical drug-screening platform**, stating the model would allow "testing potential pharmacological interventions for gLE."
- No gene therapy, cell therapy, RNA-based therapy, or targeted small-molecule trials specific to VPS11-HLD12 were identified in the available literature or ClinicalTrials.gov/WHO ICTRP searches performed for this report.

**Pharmacogenomics:** None reported (not applicable — no approved pharmacotherapy targets the underlying defect).

---

## 13. Prevention

Given the well-characterized Ashkenazi Jewish founder mutation and demonstrated consanguinity risk in non-Ashkenazi families:
- **Secondary prevention:** Carrier screening (targeted c.2536T>G testing) in the Ashkenazi Jewish population is the most actionable prevention strategy, analogous to existing AJ founder-disease carrier panels, though formal incorporation into standard AJ carrier screening programs was not confirmed in the sources reviewed.
- **Genetic counseling:** Recommended for identified carrier couples and consanguineous families; prenatal/preimplantation genetic testing is technically feasible once a familial variant is known (standard practice for known monogenic recessive disorders), though no VPS11-specific prenatal diagnosis literature was identified.
- **Primary/behavioral/public health prevention:** Not applicable (purely genetic etiology with no modifiable environmental primary cause identified, aside from the general recommendation to avoid/promptly treat febrile infections in known carriers of hypomorphic alleles, per the 2025 case's infection-triggered decompensation).
- **Immunization/prophylaxis:** Not specifically studied, though prompt treatment of febrile illness could plausibly reduce the risk of infection-triggered decompensation described in the milder allelic phenotype (inference, not directly demonstrated).

---

## 14. Other Species / Natural Disease

**Naturally occurring veterinary disease — Rottweiler dogs (neuroaxonal dystrophy, NAD):**
A homozygous missense mutation in canine VPS11 (g.14777774T>C; p.His835Arg, in the same Zinc-RING finger domain affected in human disease) causes an **autosomal recessive neuroaxonal dystrophy** in Rottweilers (Ekenstedt et al., PMID:29945969, PMC6071611):
- **Clinical presentation:** Young-adult onset, mild progressive postural deficits, ataxia, hypermetria, intention tremor, and nystagmus.
- **Pathology:** Mild cerebellar atrophy, numerous axonal spheroids, and demyelination in the vestibular nucleus, geniculate nuclei, trigeminal sensory nucleus, gracile/cuneate nuclei, and spinal dorsal horn.
- **Population genetics:** Among 288 genotyped Rottweilers, 7 were homozygous and 13 heterozygous; mutant allele frequency ≈2.3%.
- **Cross-species conservation:** Human and canine VPS11 share 98.2% amino-acid identity.
- **Comparative relevance:** The authors explicitly recommend VPS11 be considered a **candidate gene for unexplained human neuroaxonal dystrophy**, and this milder, later-onset canine phenotype is informative for understanding the human allelic-severity spectrum (compare to the 2025 human adult dystonic/ataxic case).
- **Taxonomy:** NCBI Taxon 9615 (*Canis lupus familiaris*); breed term for Rottweiler in VBO would apply if curating breed-specific susceptibility.

No other naturally occurring animal disease (wildlife, other companion species) has been reported for VPS11.

---

## 15. Model Organisms

### Zebrafish (*Danio rerio*) — the principal model system
Two independent zebrafish *vps11* loss-of-function lines have been characterized:
1. **vps11(plt)wsu1** — a previously characterized allele with a premature stop codon truncating the RING-H2 domain (used in Zhang et al., PMID:27120463).
2. **vps11(−/−)wsu3** — a newly TALEN-generated null allele (used in Banerjee et al., 2022, PMID:35241734).

**Key findings:**
- **Neuronal apoptosis:** Mild hindbrain and significant midbrain neuronal death (active Caspase-3–positive), detectable at 3–5 dpf, **preceding** myelination defects.
- **Myelination:** Progressive reduction in myelin basic protein (Mbp) expression — moderate at 5 dpf, reaching **38% of control levels by 7 dpf** (p<0.05).
- **Vision:** Both mutant lines show progressive loss of optokinetic response, with near-zero OKR gain and severely impaired visual acuity by 5–7 dpf, despite retained basic light/dark discrimination.
- **Sensorimotor function:** Progressive decline in acoustic/tap-startle locomotor response by 7 dpf, with an unexpected **faster habituation rate** in mutants versus siblings — a novel behavioral phenotype suggesting altered sensory processing beyond simple motor deficit.
- **Translational value:** Explicitly proposed by its authors as a platform for **pharmacological intervention screening** for VPS11-related genetic leukoencephalopathy.
- **Resources:** ZFIN Gene ZDB-GENE-050731-5; allele documented at ZFIN ZDB-FIG-160519-7.

### Mouse
No VPS11 knockout/knock-in mouse model of the human disease has been reported to date (a full VPS11 null is expected to be embryonic lethal given its essential role in the Vps-C core, consistent with the absence of viable human null homozygotes). Mouse tissue (oligodendrocytes) has, however, been used descriptively to characterize normal Vps11 protein localization (Skoff et al., 2021, PMID:33874780), showing strong oligodendrocyte expression co-localized with MAG in the myelin inner tongue and absence from axons — informative for mechanism but not a disease model per se.

### Cellular/in vitro models
- **HeLa cells** transfected with wild-type vs. C846G VPS11 constructs — used to demonstrate reduced protein stability, increased ubiquitination, and impaired VPS11–VPS18 interaction (Zhang et al.).
- **Patient-derived fibroblasts** — used for autophagy-flux assays (RFP-GFP-LC3 tandem reporter) and, in the 2025 dystonia report, electron microscopy demonstrating large clear vacuolar/lysosomal structures.
- **siRNA knockdown of VPS11 in human cell lines** — recapitulates impaired autophagic flux (p62/LC3-II accumulation, failure to clear with mTOR-inhibitor–induced autophagy).

### Model limitations
No model to date fully recapitulates the human infantile hypomyelinating phenotype with concurrent white-matter MRI correlate; the zebrafish model captures neuronal death, hypomyelination, and behavioral/visual deficits but zebrafish CNS myelination architecture and developmental timeline differ substantially from human, and no rescue/therapeutic efficacy data in vivo have yet been published.

---

## Summary of Ontology Term Suggestions for KB Curation

- **MONDO:** MONDO:0014732 (HLD12) — note the closely related but distinct DYT32/dystonia phenotype may warrant separate handling per lump/split conventions (subtype vs. separate entry — the 2025 paper argues for a single expanded clinical spectrum, but this is a position to weigh against MONDO/OMIM's current split into #616683 and a separate dystonia OMIM entry).
- **HGNC:** hgnc:14583 (VPS11)
- **HP terms:** see Section 3 table above (developmental delay, hypotonia, spasticity, microcephaly, cortical blindness, optic atrophy, seizures, hearing loss, dysphagia, joint contracture, dystonia HP:0001332, cerebellar ataxia HP:0001251, myoclonus HP:0001336, spastic paraplegia HP:0001258)
- **GO terms:** GO:0007032 (endosome organization), GO:0006914/GO:0016236 (autophagy/macroautophagy), GO:0000045 (autophagosome assembly)
- **CL terms:** CL:0000128 (oligodendrocyte), CL:0000540 (neuron)
- **UBERON terms:** UBERON:0002336 (white matter), UBERON:0001880 (corpus callosum), UBERON:0001876 (optic nerve), UBERON:0002037 (cerebellum)
- **NCIT treatment terms:** NCIT:C15747 (Supportive Care), NCIT:C15986 (Pharmacotherapy — anticonvulsants), NCIT:C15302 (Physical Therapy), NCIT:C15240 (Genetic Counseling)

---

## Sources

- [Entry - #616683 - LEUKODYSTROPHY, HYPOMYELINATING, 12; HLD12 - OMIM](https://www.omim.org/entry/616683)
- [VPS11 CORE SUBUNIT OF CORVET AND HOPS COMPLEXES - OMIM *608549](https://omim.org/entry/608549)
- [Hypomyelinating leukodystrophy 12 - NIH Genetic Testing Registry (GTR)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4225247/)
- [Hypomyelinating leukodystrophy 12 - MedGen (NCBI)](https://www.ncbi.nlm.nih.gov/medgen/905068)
- [Orphanet: VPS11-related autosomal recessive hypomyelinating leukodystrophy (ORPHA:466934)](https://www.orpha.net/en/disease/detail/466934)
- [GARD: Hypomyelinating leukodystrophy 12](https://rarediseases.info.nih.gov/diseases/17837/hypomyelinating-leukodystrophy-12)
- [A Founder Mutation in VPS11 Causes an Autosomal Recessive Leukoencephalopathy Linked to Autophagic Defects (PMC4847778)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4847778/)
- [A Founder Mutation in VPS11 Causes an Autosomal Recessive Leukoencephalopathy Linked to Autophagic Defects — PLOS Genetics (PMID:27120463)](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1005848)
- [The second report of a new hypomyelinating disease due to a defect in the VPS11 gene discloses a massive lysosomal involvement (PMID:27473128)](https://link.springer.com/article/10.1007/s10545-016-9961-x)
- [Vision and sensorimotor defects associated with loss of Vps11 function in a zebrafish model of genetic leukoencephalopathy — Sci Rep (PMID:35241734 / PMC8894412)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8894412/)
- [Characterization of the Expression of Vacuolar Protein Sorting 11 (Vps11) in Mammalian Oligodendrocytes (PMID:33874780)](https://pubmed.ncbi.nlm.nih.gov/33874780/)
- [HOPS-associated neurological disorders (HOPSANDs): linking endolysosomal dysfunction to the pathogenesis of dystonia — Brain (2021)](https://academic.oup.com/brain/article/144/9/2610/6237874)
- [Confirmation of biallelic VPS11 variants as a cause of complex dystonic syndrome (PMID:41551069 / PMC12808586)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12808586/)
- [A Missense Mutation in the Vacuolar Protein Sorting 11 (VPS11) Gene Is Associated with Neuroaxonal Dystrophy in Rottweiler Dogs (PMID:29945969 / PMC6071611)](https://pmc.ncbi.nlm.nih.gov/articles/PMC6071611/)
- [VPS11 gene — GenCC classifications](https://search.thegencc.org/genes/HGNC:14583)
- [Gene: VPS11 (Early onset dystonia) — Genomics England PanelApp](https://panelapp.genomicsengland.co.uk/panels/192/gene/VPS11/)

**Note on evidence gaps:** No mortality/survival statistics, formal prevalence estimates, transcriptomic/proteomic/single-cell datasets, clinical trial records, or mouse genetic models specific to VPS11-HLD12 were located; these should be recorded as absent rather than inferred if this report is used to populate a knowledge-base entry.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 12 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 50 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 29 |
| Terms named correctly | 14 |
| Terms named as a **different** term | 10 |
| Terms whose name is worth a second look | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001263` (1 mention) - the report calls it "All patients (infantile onset)"; HP calls it **Global developmental delay**
- `HP:0010864` (1 mention) - the report calls it "Nearly universal by follow-up"; HP calls it **Severe intellectual disability**
- `HP:0001252` (1 mention) - the report calls it "Presenting feature"; HP calls it **Hypotonia**
- `HP:0001257` (1 mention) - the report calls it "Progressive"; HP calls it **Spasticity**
- `HP:0000252` (1 mention) - the report calls it "<2nd percentile"; HP calls it **Microcephaly**
- `HP:0011016` (1 mention) - the report calls it "abnormal lysosome"; HP calls it **obsolete Abnormality of urine glucose concentration**
- `CL:0000617` (1 mention) - the report calls it "GABAergic neuron, if relevant to dystonia circuitry — not specifically demonstrated"; CL calls it **GABAergic neuron**
- `UBERON:0002336` (10 mentions) - the report calls it "cerebral white matter", "white matter"; UBERON calls it **corpus callosum**
- `UBERON:0001880` (2 mentions) - the report calls it "corpus callosum"; UBERON calls it **bed nucleus of stria terminalis**
- `UBERON:0001876` (2 mentions) - the report calls it "optic nerve"; UBERON calls it **amygdala**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0011016` (obsolete Abnormality of urine glucose concentration) (1 mention) - replaced by `HP:0003076`
- `GO:0061912` (obsolete selective autophagy) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002540` (1 mention) - the report calls it "loss of ability to walk"; HP calls it **Inability to walk**
- `HP:0100704` (1 mention) - the report calls it "All patients"; HP calls it **Cerebral visual impairment**
- `GO:0061912` (1 mention) - the report calls it "selective autophagosome maturation"; GO calls it **obsolete selective autophagy**
- `GO:0016236` (2 mentions) - the report calls it "macroautophagy", "autophagy/macroautophagy"; GO calls it **macroautophagy**
- `NCIT:C15986` (2 mentions) - the report calls it "Pharmacotherapy — anticonvulsants"; NCIT calls it **Pharmacotherapy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `GO:0016236` - called "macroautophagy", "autophagy/macroautophagy"
- `UBERON:0002336` - called "cerebral white matter", "white matter"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
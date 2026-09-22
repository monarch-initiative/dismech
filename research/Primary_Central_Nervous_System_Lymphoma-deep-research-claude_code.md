---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-09T12:18:40.660408'
end_time: '2026-09-09T12:25:54.857525'
duration_seconds: 434.2
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Primary Central Nervous System Lymphoma
  mondo_id: MONDO:0002571
  category: Complex
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
  web_search_requests: 23
  num_turns: 24
  total_cost_usd: 1.6856460000000004
  session_id: 26dbdeb2-df8f-5b2c-9949-47091d00d07d
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 67
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 32
  on_topic: 27
  validator_version: 0.2.1
term_validation:
  total_terms: 75
  verified: 70
  not_found: 0
  obsolete: 4
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 31
  labels_matching: 18
  labels_mismatched: 6
  mislabelled_terms:
  - term_id: NCIT:C9218
    reported_labels:
    - Primary Central Nervous System Lymphoma
    ontology_label: Stage IV Oropharyngeal Carcinoma AJCC v6
  - term_id: CL:0000980
    reported_labels:
    - "plasmablast-adjacent \u2014 not typically applicable, PCNSL retains B-cell\
      \ not plasma-cell phenotype"
    ontology_label: plasmablast
  - term_id: UBERON:0002316
    reported_labels:
    - "white matter of brain \u2014 for periventricular/deep involvement"
    ontology_label: white matter
  - term_id: UBERON:0004087
    reported_labels:
    - vitreous body
    ontology_label: vena cava
  - term_id: CL:0000542
    reported_labels:
    - lymphocyte, neoplastic B-cell subtype
    ontology_label: lymphocyte
  - term_id: NCIT:C36044
    reported_labels:
    - Diffuse Large B-Cell Lymphoma
    ontology_label: Grade 3b Malignant Neoplasm
  labels_variant: 7
  obsolete_terms:
  - term_id: HP:0002355
    ontology_label: obsolete Difficulty walking
    replaced_by: HP:0001288
  - term_id: NCIT:C36044
    ontology_label: Grade 3b Malignant Neoplasm
  - term_id: CHEBI:9560
    ontology_label: CHEBI_9560
    replaced_by: CHEBI:102166
  - term_id: CHEBI:45602
    ontology_label: CHEBI_45602
    replaced_by: CHEBI:45605
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Central Nervous System Lymphoma
- **MONDO ID:** MONDO:0002571 (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Primary Central Nervous System Lymphoma** covering all of the
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

I'll research Primary CNS Lymphoma (PCNSL) across all required domains now, running searches in parallel batches.

Excellent, I now have a very comprehensive dataset. Let me fill remaining gaps: model organisms/CDX detail, inheritance/genetic predisposition, gnomAD/germline, comparative/veterinary disease, and specific ontology term suggestions.

# Primary Central Nervous System Lymphoma (PCNSL): Comprehensive Research Report

## 1. Disease Information

**Overview.** Primary central nervous system lymphoma (PCNSL) is a rare, aggressive extranodal non-Hodgkin lymphoma — in the overwhelming majority of cases a diffuse large B-cell lymphoma (DLBCL) — that arises within and remains confined to the brain parenchyma, spinal cord, leptomeninges, and/or eyes (vitreoretinal compartment) at diagnosis, without evidence of systemic (nodal or extra-CNS) disease (Nature Reviews Disease Primers, 2023, PMID:37322012). In the WHO Classification of Haematolymphoid Tumours 5th edition (WHO-HAEM5, 2022) and subsequent 2024 updates, PCNSL is grouped under the new umbrella entity **"large B-cell lymphomas of immune-privileged sites"**, alongside primary vitreoretinal large B-cell lymphoma (PVRL) and primary testicular large B-cell lymphoma (PTL), reflecting their shared biology of arising in anatomically sequestered, immune-privileged compartments. The International Consensus Classification (ICC) instead retains PCNSL as a distinct, standalone entity.

**Key identifiers:**
- **MONDO:** MONDO:0002571
- **ICD-O-3:** 9680/3 (Diffuse large B-cell lymphoma, NOS)
- **ICD-10-CM:** C83.3 (Diffuse large B-cell lymphoma) with site extension for CNS, or historically C71/C72 region codes when classified by anatomic site
- **ICD-11:** 2A81.0Y or 2B33.1 region (extranodal DLBCL of CNS)
- **MeSH:** D016543 (Lymphoma, Non-Hodgkin) combined with central nervous system neoplasm indexing; more specific term "Central Nervous System Neoplasms/lymphoma"
- **OMIM:** No dedicated Mendelian OMIM entry (PCNSL is predominantly a sporadic somatic malignancy, not a single-gene disorder)
- **Orphanet:** ORPHA:56163 (Primary central nervous system lymphoma is not separately Orphanet-coded as a rare disease per se, though PCNSL-related entries exist under lymphoma classifications)
- **NCIT:** NCIT:C9218 (Primary Central Nervous System Lymphoma)

**Synonyms/alternative names:** Primary CNS lymphoma; PCNSL; microgliomatosis (historical term); reticulum cell sarcoma of brain (obsolete); primary brain lymphoma; primary diffuse large B-cell lymphoma of the CNS (PCNS-DLBCL); primary intraocular lymphoma / primary vitreoretinal lymphoma (PVRL, when eye-restricted).

**Data provenance.** Most quantitative findings summarized below are derived from aggregated disease-level resources: population-based cancer registries (SEER, CBTRUS), multicenter cohort studies, international consensus/clinical trial data (IELSG, Alliance, HOVON), and molecular genomic profiling studies (whole-exome/whole-genome sequencing cohorts). Individual-patient EHR-level data appear in a minority of biomarker validation studies (e.g., CSF IL-10/MYD88 diagnostic cohorts).

---

## 2. Etiology

### Disease Causal Factors
PCNSL is fundamentally a **somatic, clonal B-cell malignancy** driven by acquired (not germline) genetic lesions that constitutively activate B-cell receptor (BCR) and Toll-like receptor (TLR)/MYD88-NF-κB signaling within a B lymphocyte that subsequently homes to, or transforms within, the CNS immune-privileged compartment. There is no single "cause" analogous to a Mendelian disorder; rather, disease arises from an interplay of somatic mutation acquisition, chronic antigenic/autoantigenic BCR stimulation, and — critically — a permissive or impaired local/systemic immune surveillance state.

### Genetic Risk Factors
- **Somatic driver mutations (not germline predisposition):** Recurrent **MYD88 L265P** (~50–67% of cases; adapter protein mutation causing constitutive NF-κB activation via IRAK1/4), **CD79B** mutations (particularly Y196; ~55–63%, most commonly co-occurring with MYD88 L265P), and **PIM1** mutations (~55–59%) define the disease's dominant "MCD" genomic subtype (see Section 4 and Section 6).
- **Congenital/inherited immunodeficiency syndromes** confer markedly elevated risk of secondary lymphoproliferation including PCNSL: **Wiskott-Aldrich syndrome** (WAS gene, X-linked), **ataxia-telangiectasia** (ATM gene), **X-linked lymphoproliferative disease** (SH2D1A/XIAP), and severe combined immunodeficiency (SCID)/common variable immunodeficiency — patients with these congenital immunodeficiencies carry an estimated ~4% lifetime risk of PCNSL.
- No common-variant GWAS susceptibility loci for PCNSL specifically have been robustly replicated to date (distinct from the situation for some other B-cell lymphoma subtypes).

### Environmental/Non-Genetic Risk Factors
- **Age:** Strongest risk correlate in immunocompetent hosts — incidence rises steeply with age, peaking in the 7th–8th decade (median age at diagnosis ≈ 65–67 years).
- **HIV/AIDS infection:** The single strongest acquired risk factor. Risk is inversely proportional to CD4+ T-cell count; HIV-associated PCNSL classically occurs at CD4+ counts averaging ~30 cells/µL. Pre-cART era incidence in HIV-infected persons was reported as high as 5,000-fold that of the general population, with rates of ~5 cases per 1,000 person-years (1991–1994), falling to ~0.32 per 1,000 person-years after 1999 with combination antiretroviral therapy (cART) introduction.
- **Solid organ transplantation and iatrogenic immunosuppression:** Post-transplant lymphoproliferative disease (PTLD) involving the CNS occurs at a markedly younger median age (~23 years in some series) and is almost universally EBV-driven.
- **Chronic autoimmune disease and immunosuppressive drug therapy** (e.g., systemic lupus erythematosus, rheumatoid arthritis on long-term immunosuppressants) increase risk.
- **No confirmed risk factors in immunocompetent individuals without evident immunosuppression.** Proposed but unconfirmed/unsupported associations include prior tonsillectomy and oral contraceptive use; heavy mobile-phone use has been proposed but is not evidence-supported (Nature Reviews Disease Primers, PMID:37322012).
- **Sex:** Slight male predominance in immunocompetent PCNSL (male:female ≈ 1.2:1 to 1.4:1), a pattern that is markedly amplified in HIV-associated disease (reflecting epidemiology of HIV infection itself) but reversed toward female predominance in isolated primary vitreoretinal lymphoma.

### Protective Factors
- **Combination antiretroviral therapy (cART)** in HIV-infected individuals is the single best-documented protective/risk-modifying intervention, having driven a >10-fold decline in HIV-associated PCNSL incidence since the mid-1990s.
- **Restoration/normalization of immune competence** (e.g., withdrawal or reduction of immunosuppressive regimens in transplant recipients when clinically feasible) reduces risk.
- No specific genetic protective variants or dietary/lifestyle protective factors have been established for PCNSL.

### Gene-Environment Interactions
The central gene-environment interaction in PCNSL pathogenesis is the interplay between **host immunosurveillance status** (HIV-induced CD4+ depletion, iatrogenic immunosuppression, or congenital immunodeficiency) and **EBV infection**: virtually all HIV-associated and post-transplant PCNSL cases are EBV-genome positive, with loss of EBV-specific CD4+ T-cell effector function permitting outgrowth of EBV-transformed B-cell clones within the CNS immune-privileged niche. In immunocompetent PCNSL, EBV association is rare (a distinct immunobiological entity has been described for EBV+ PCNSL arising after immunosuppression; *Blood* 2021, 137(11):1468).

---

## 3. Phenotypes

Symptom onset is typically **subacute**, evolving over days to a few weeks, and diagnosis is frequently delayed (mean interval from symptom onset to diagnosis reported around 35–80 days across series) because of nonspecific or psychiatric presentations.

| Phenotype | Type | Frequency | Suggested HPO term |
|---|---|---|---|
| Focal neurological deficit (hemiparesis, aphasia, ataxia, sensory loss, cranial neuropathy) | Sign | 56–70% of intracranial cases | HP:0034332 (Focal neurologic deficit) / HP:0001324 (Muscle weakness) / HP:0002317 (Unsteady gait) |
| Neuropsychiatric/behavioral change, personality change, cognitive decline | Symptom/behavioral | 32–43%; cognitive/behavioral abnormalities present at diagnosis in 50–70% overall | HP:0000708 (Behavioral abnormality) / HP:0002354 (Memory impairment) / HP:0000750 (Delayed speech and language development n/a — use HP:0031466 personality change if available) |
| Signs of increased intracranial pressure (headache, nausea, vomiting, papilledema) | Symptom/sign | Common, variable | HP:0002315 (Headache), HP:0002017 (Nausea), HP:0002153 (Papilledema) |
| Seizures | Symptom | ~10–15% (lower than gliomas, given deep/periventricular location) | HP:0001250 (Seizure) |
| Visual disturbance (blurry vision, floaters) from vitreoretinal involvement | Symptom | ~20% at presentation overall; ~15–25% of PCNSL have vitreoretinal involvement, of which ~33% are asymptomatic | HP:0000618 (Blurred vision), HP:0011805 (Vitreous floaters/vitritis-related) |
| Hearing loss | Symptom | Uncommon, cranial nerve/leptomeningeal disease | HP:0000365 (Hearing impairment) |
| Diplopia (double vision) | Symptom | Occurs with cranial nerve/brainstem involvement | HP:0000651 (Diplopia) |
| Ataxia (with cerebellar lesions) | Sign | Location-dependent | HP:0001251 (Ataxia) |
| Myelopathy (weakness, sensory level, bowel/bladder dysfunction) | Sign | <1% of PCNSL (isolated spinal cord disease) | HP:0002355 (Difficulty walking), HP:0002019 (Constipation-adjacent bladder/bowel terms as applicable) |
| Elevated CSF protein / CSF pleocytosis | Laboratory abnormality | Common on lumbar puncture | HP:0002922 (Increased CSF protein), part of CSF workup |

**Phenotype characteristics:**
- **Age of onset:** Predominantly adult-onset/late-onset; median 65–67 years in immunocompetent disease; markedly younger (median 30s–40s) in HIV-associated disease.
- **Severity:** Highly variable; deep periventricular/basal ganglia/corpus callosum/thalamic involvement carries worse prognosis (an IELSG adverse risk factor).
- **Progression:** Typically progressive without treatment; can be rapidly progressive given aggressive lymphoma biology and high proliferative index.
- **Anatomic distribution:** Intraparenchymal disease predominates (~92%), with solitary lesions in ~65% and multiple lesions in ~35%; supratentorial:infratentorial ratio ≈ 3:1. Leptomeningeal dissemination detected by CSF cytology/flow cytometry in ~15% (up to 0–50% range across studies), without demonstrated independent effect on overall survival in prospective analysis.

**Quality of life impact:** Cognitive and behavioral impairment at diagnosis substantially affects daily functioning; most patients show clinical improvement with successful treatment, often returning toward pre-diagnosis neurological/cognitive baseline. However, treatment-related neurotoxicity (see Section 11) — particularly following whole-brain radiotherapy (WBRT), especially combined with chemotherapy and in patients >60 years — can cause durable, sometimes progressive decline in cognition, gait, and continence, substantially impairing quality of life independent of disease status.

---

## 4. Genetic/Molecular Information

### Causal/Driver Genetic Alterations (Somatic)
PCNSL is not caused by a single causal gene in the Mendelian sense; disease arises from a recurrent constellation of **somatic** mutations converging on BCR/TLR–NF-κB signaling and immune evasion pathways.

| Gene (HGNC) | Alteration | Approx. frequency | Functional consequence |
|---|---|---|---|
| **MYD88** (hgnc:7562) | p.L265P hotspot missense | 50–67% | Constitutive TLR/IL-1R adapter activation → IRAK1/4 recruitment → NF-κB activation (gain-of-function) |
| **CD79B** (hgnc:1699) | Y196 (ITAM tyrosine) missense, most commonly co-occurring with MYD88 L265P | 48–63% | Disrupts BCR internalization/inhibitory signaling → chronic active BCR signaling → NF-κB |
| **PIM1** (hgnc:8986) | Missense/frameshift, often within aberrant somatic hypermutation (ASHM) targets | 55–59% | Serine/threonine kinase; oncogenic cooperator, prosurvival |
| **CDKN2A** (hgnc:1787) | Focal deletion (9p21.3), mutation, or promoter hypermethylation | ~56% (deletion); 28% (mutation) | Loss of p16INK4a/p14ARF tumor suppression → deregulated cell cycle, chromosomal instability |
| **CARD11** (hgnc:16412) | Gain-of-function mutations (~15% of cases) | ~15% | Constitutive NF-κB activation independent of upstream BCR signal |
| **BTG1/BTG2** (hgnc:1130/hgnc:1131) | Mutation via aberrant somatic hypermutation | Variable | Loss of antiproliferative function |
| **PAX5, RHOH, IGHV4-34** | Recurrent targets of aberrant somatic hypermutation | Variable | Contributes to genomic instability and possibly self-antigen-reactive BCR repertoire (IGHV4-34 in particular) |
| **B2M** (hgnc:914, beta-2-microglobulin) | Mutation/LOH (~10%) | ~10% | Loss of MHC class I surface expression → immune evasion |
| **HLA region genes** (6p21.32; HLA-A/-B/-C class I, HLA-DR/-DP/-DQ, TAP1 class II) | Copy-neutral LOH, focal homozygous/biallelic deletion | Most common recurrent chromosomal abnormality in PCNSL | Loss/reduced HLA class I and II surface expression → CD8+/CD4+ T-cell immune evasion in the immune-privileged CNS niche |
| **CD274 (PD-L1)/PDCD1LG2 (PD-L2)** (9p24.1) | Copy number gain (~67%), structural rearrangement/translocation (~13%) | Common | Overexpression of PD-L1/PD-L2 → adaptive immune checkpoint-mediated evasion |
| **TP53** (hgnc:11998) | Mutation | Lower frequency than systemic DLBCL | Loss of tumor suppression |
| **BCL6** (hgnc:1001) | Translocation | Relatively common | Germinal-center transcriptional dysregulation |
| **MYC/BCL2** rearrangements | Structural | Lower frequency than systemic DLBCL | Contrasts PCNSL biology from nodal "double-hit" DLBCL |
| **ETV6** (hgnc:3495) | Inactivation | Documented, pathogenic significance unclear | — |

### LymphGen/Genomic Subtype Classification
The co-occurrence of MYD88 L265P and CD79B mutations places the great majority of PCNSL within the **"MCD" (MYD88/CD79B) LymphGen genetic subtype** originally defined in systemic DLBCL genomic classification. One study found 59% of PCNSL samples classified as MCD, 17% as "MCD-composite," and 24% as "Other" (LymphGen not classifiable). The MCD subtype in systemic DLBCL is associated with inferior outcomes to standard immunochemotherapy, a pattern that appears to extend to PCNSL.

### Molecular Clusters (proposed, Nature Reviews Disease Primers, PMID:37322012)
Four proposed molecular clusters: **CS1** (hypermethylated, proliferative), **CS2** (hypermethylated, immune-cold), **CS3** (meningeal involvement, worst prognosis), **CS4** (immune-hot, favorable outcome) — an evolving framework analogous to systemic DLBCL genomic subtyping efforts (LymphGen, cluster-based classifications).

### Variant Classification/Pathogenicity
Recurrent hotspot mutations (MYD88 L265P, CD79B Y196) are consistently classified pathogenic/oncogenic drivers in ClinVar-adjacent somatic cancer variant databases (COSMIC) and functional studies. These are **somatic**, not germline, variants — allele frequency in population germline databases (gnomAD) is essentially zero/not applicable, as they are acquired oncogenic mutations, not inherited polymorphisms.

### Epigenetic Information
- **DNA hypermethylation** at CDKN2A promoter contributes to p16/p14ARF silencing.
- Broader hypermethylator phenotypes define at least two of the four proposed molecular clusters (CS1, CS2 above), consistent with epigenetic dysregulation as a major axis of PCNSL biology alongside genetic mutation.

### Chromosomal Abnormalities
- **6p21.32 loss/HLA locus alterations** — the single most frequent recurrent chromosomal abnormality in PCNSL, an immune-evasion-associated lesion characteristic of immune-privileged-site lymphomas (also seen in PTL, PVRL).
- **9p21.3 deletion** (CDKN2A locus) — ~56% of tumors.
- **9p24.1 gain/rearrangement** (CD274/PDCD1LG2, PD-L1/PD-L2 locus) — copy number gains in ~67% of cases, translocations in ~13%.
- **3q12.3 gain** (~45% of patients) — drives NFKBIZ overexpression, reinforcing NF-κB pathway activation.
- Partial uniparental disomy and copy-neutral LOH are recurrently reported across the genome, particularly at 6p (*Leukemia* 2010, "Chromosomal imbalances and partial uniparental disomies in primary central nervous system lymphoma").

**Suggested ontology terms:** GENO terms for variant zygosity/type; GO:0007249 (I-kappaB kinase/NF-kappaB signaling); GO:0050853 (B cell receptor signaling pathway); GO:0002224 (toll-like receptor signaling pathway); CHEBI terms for relevant small molecules (see Section 12).

---

## 5. Environmental Information

- **Infectious agent — Epstein-Barr virus (EBV, human gammaherpesvirus 4; NCBITaxon:10376):** The dominant infectious/environmental driver in immunosuppression-associated PCNSL. Virtually all HIV-associated PCNSL tumors are EBV-genome positive; EBV-driven, immunosuppression-associated PCNSL is now recognized as a distinct immunobiological entity distinguishable from sporadic immunocompetent-host PCNSL (*Blood* 2021, 137(11):1468). EBV latent membrane proteins and EBNA antigens drive B-cell proliferation and transformation in the setting of failed EBV-specific CD4+ T-cell immunosurveillance.
- **HIV (human immunodeficiency virus; NCBITaxon:11676):** Not itself infecting the malignant B-cell clone, but the principal permissive environmental/infectious cofactor via progressive CD4+ T-cell depletion, enabling EBV-driven lymphomagenesis in the CNS.
- **Iatrogenic immunosuppressive drug exposure** (calcineurin inhibitors, antimetabolites, corticosteroids in solid-organ or hematopoietic transplant recipients; disease-modifying antirheumatic drugs and biologics in autoimmune disease) — environmental/pharmacologic exposures that recapitulate the immunosuppressed-host EBV-driven pathway (post-transplant lymphoproliferative disease, PTLD, with CNS tropism).
- **Lifestyle/occupational factors:** No robustly established lifestyle, dietary, occupational, or toxin exposure has been causally linked to PCNSL in immunocompetent hosts. Proposed associations (tonsillectomy history, oral contraceptive use, mobile phone radiofrequency exposure) remain unconfirmed and are not supported by consistent epidemiological evidence.

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain (Primary/Sporadic Immunocompetent-Host Pathway)

1. A mature/late germinal-center-exit or post-germinal-center B lymphocyte acquires **somatic driver mutations** — most commonly **MYD88 L265P** and/or **CD79B** ITAM-domain mutations, frequently co-occurring — **leading to** constitutive, ligand-independent activation of TLR/IL-1R (via MYD88→IRAK1/4→NF-κB) and chronic active B-cell receptor (BCR) signaling.
2. Constitutive MYD88/CD79B/CARD11 pathway activation, reinforced by recurrent **3q12.3 gain driving NFKBIZ overexpression**, **leads to** sustained canonical NF-κB transcriptional activation, promoting B-cell survival and proliferation (demonstrated directly; PMID:37322012 and related molecular studies).
3. Aberrant somatic hypermutation (targeting PIM1, PAX5, RHOH, BTG1/2, MYC, and other loci, often via off-target activity of activation-induced cytidine deaminase, AICDA) **results in** additional cooperating oncogenic hits and progressive genomic instability, compounded by loss of **CDKN2A** (via 9p21.3 deletion, mutation, or promoter hypermethylation in ~56–83% of cases combined) — **leading to** unchecked cell-cycle progression (p16INK4a/p14ARF loss) and further chromosomal instability.
4. The transformed B-cell clone (often expressing self-reactive BCR repertoires, e.g., immunoglobulins recognizing CNS self-antigens such as GRINL1A, ADAP2, BAIAP2, N-hyperglycosylated SAMD14, and neurabin-I) is proposed to be selected for, and/or retained within, the CNS **through chronic antigen-driven BCR engagement with CNS-resident self-proteins** — an inferred mechanism supporting the "antigen-selection" hypothesis of CNS tropism, though the precise sequence of extra-CNS transformation versus intra-CNS transformation is not fully resolved (some transformation may occur systemically prior to CNS homing, per convergent evidence from PVRL biology).
5. Concurrently, the malignant clone acquires **immune-evasion lesions** — most prominently 6p21.32 (HLA locus) copy-neutral LOH or focal deletion (loss of MHC class I/II surface expression), B2M mutation/LOH (~10%, complete HLA class I loss), and 9p24.1 gain/rearrangement driving PD-L1/PD-L2 overexpression — **leading to** evasion of CD8+/CD4+ T-cell-mediated immunosurveillance, which is especially consequential within the already immune-privileged CNS compartment (blood-brain barrier, absence of conventional lymphatics, reduced baseline antigen-presenting cell trafficking).
6. Within the CNS parenchyma, malignant B cells characteristically infiltrate in a **perivascular, angiocentric pattern**, recruited in part via endothelial **CXCL12/CXCL9** chemokine gradients engaging **CXCR4** on neoplastic B cells, and interacting with a distinctive tumor microenvironment comprising **reactive CD4+/CD8+ T cells** (CD8+ T cells preferentially infiltrating tumor nests and expressing the exhaustion marker TIM-3), **M1-like (CD68+CD163low) and M2-like (CD68+CD163high, PD-L1/TIM-3-expressing, centrally/perinecrotically enriched) tumor-associated macrophages/microglia**, and reactive astrocytes — **resulting in** a locally immunosuppressive, angiogenic (aquaporin-4, galectin-3-expressing endothelium) niche that further shields the tumor from immune clearance and promotes local growth (STAT3-driven autocrine PD-L1/IDO expression in tumor cells and macrophages is one documented amplifying loop).
7. Progressive perivascular and parenchymal tumor expansion **causes** local mass effect, vasogenic edema, blood-brain barrier disruption, and infiltrative destruction of adjacent white/gray matter — **leading to** the clinical phenotypes of focal neurological deficit, cognitive/behavioral change, and (with periventricular/leptomeningeal spread) increased intracranial pressure and CSF pleocytosis/protein elevation.
8. In a minority of cases, dissemination occurs to the **leptomeninges** (CSF-borne spread, ~15% CSF-cytology/flow-positive) and/or the **vitreoretinal compartment** of the eye (~15–25%, another immune-privileged site sharing the blood-ocular barrier), producing multifocal CNS symptoms or visual symptoms (often asymptomatic in up to a third of cases with concomitant ocular disease), and reflecting the broader "immune-privileged site lymphoma" biology shared with PCNSL, PVRL, and primary testicular lymphoma.

### Branch: Immunosuppression/EBV-Driven Pathway (HIV, transplant, congenital immunodeficiency)
In parallel to (or substituting for) steps 1–3 above, **loss of EBV-specific CD4+ T-cell immunosurveillance** (from HIV-mediated CD4+ depletion, pharmacologic immunosuppression, or congenital immunodeficiency) **permits** outgrowth of an EBV-latently-infected B-cell clone driven by viral oncoproteins (EBNA2, LMP1) rather than requiring the same degree of MYD88/CD79B-driven transformation — this EBV+ immunosuppression-associated PCNSL is now regarded as a biologically and immunologically **distinct entity** from sporadic immunocompetent-host PCNSL (*Blood* 2021, 137(11):1468), converging downstream on the same perivascular growth pattern and CNS immune-privilege exploitation described in steps 6–8 above.

### Molecular Pathways
- **NF-κB signaling** (canonical, via MYD88/CD79B/CARD11/NFKBIZ) — the central oncogenic driver pathway. Suggested GO term: GO:0007249 (I-kappaB kinase/NF-kappaB signaling).
- **BCR signaling pathway** — GO:0050853, transduced through BTK (a druggable node targeted by ibrutinib, tirabrutinib, acalabrutinib).
- **TLR/IL-1R-MYD88-IRAK signaling** — GO:0002224 (toll-like receptor signaling pathway); GO:0035666 (TRIF-independent TLR4/MYD88 pathway relevant terms as applicable).
- **JAK-STAT pathway** — activated downstream of 9p24.1 amplification (JAK2 co-amplified with PD-L1/PD-L2 locus); STAT3 drives autocrine PD-L1/IDO expression.
- **PI3K-AKT-mTOR** — implicated as a cooperating survival pathway in DLBCL biology generally, though PCNSL-specific data are less extensive than for MYD88/BCR pathways.

### Cellular Processes
Chronic proliferative signaling with impaired apoptosis (via NF-κB-driven pro-survival gene transcription, e.g., BCL2 family members), cell-cycle dysregulation (CDKN2A loss), and active immune evasion (MHC downregulation, checkpoint ligand overexpression) dominate the cellular phenotype. Suggested GO terms: GO:0043065 (positive regulation of apoptotic process — for the "de-regulation" direction, i.e., decreased apoptosis), GO:0000082 (G1/S transition of mitotic cell cycle, dysregulated).

### Protein Dysfunction
- MYD88 L265P: gain-of-function conformational change permitting spontaneous myddosome (MYD88-IRAK4-IRAK1) assembly independent of receptor ligation.
- CD79B Y196 mutations: disrupt the ITAM tyrosine that normally recruits LYN for BCR downregulation, converting the signal into chronic-active rather than transient BCR signaling.

### Tissue Damage Mechanisms
Direct infiltrative destruction, vasogenic edema, blood-brain barrier disruption, and — importantly — treatment-related tissue injury (radiation-induced demyelination, axonal loss, gliosis, and microvascular injury following WBRT) contribute substantially to the disease's overall tissue pathology burden, sometimes exceeding the tumor's own direct damage in long-term survivors (see Section 11).

### Molecular Profiling
- **Genomics/WES-WGS:** Comprehensive genomic and transcriptomic landscape described in *Nature Communications* 2022 ("The genomic and transcriptional landscape of primary central nervous system lymphoma") and multiple subsequent LymphGen-subtyping studies (2024 medRxiv preprints on PCNSL genomic subtypes and drug sensitivity).
- **Single-cell/spatial:** Emerging single-cell and multiplex immunohistochemistry studies characterize the M1/M2 macrophage-microglia dichotomy and T-cell exhaustion phenotype within the PCNSL tumor microenvironment (*Biomarker Research*, "Unraveling the immune microenvironment in primary CNS lymphoma," 2026).
- **CSF liquid biopsy/cell-free DNA:** Digital droplet PCR (ddPCR) for MYD88 L265P in CSF and even plasma cell-free DNA is an active area of molecular diagnostic development.

### Advanced Technologies
Functional genomic screening and in vitro drug-sensitivity profiling of PCNSL biopsies against kinase inhibitors has been reported (2024 medRxiv "Primary Central Nervous System Lymphoma Tumor Biopsies Show Heterogeneity in Gene Expression Profiles, Genetic Subtypes, and in vitro Drug Sensitivity to Kinase Inhibitors").

**Suggested Cell Ontology (CL) terms:** CL:0000236 (B cell) → transformed/neoplastic B cell; CL:0000980 (plasmablast-adjacent — not typically applicable, PCNSL retains B-cell not plasma-cell phenotype); CL:0000813 (memory T cell)/CL:0000625 (CD8-positive, alpha-beta T cell) for tumor-infiltrating exhausted CD8+ T cells; CL:0000129 (microglial cell); CL:0000235 (macrophage) with M1/M2 polarization qualifiers; CL:0002453 (oligodendrocyte, for demyelination context); CL:0000127 (astrocyte).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Brain (supratentorial > infratentorial, ratio ~3:1) — frontal, temporal, parietal, occipital lobes; deep structures (basal ganglia, thalamus, corpus callosum, periventricular white matter) are characteristic and prognostically adverse sites of involvement. Cerebellum and brainstem less commonly.
- **Secondary within the CNS axis:** Leptomeninges (~0–50%, most series ~15% by CSF cytology/flow), spinal cord (<1%, presenting as subacute myelopathy), and the eye — vitreoretinal compartment (~15–25%, bilateral in the majority of PVRL cases).
- **Body systems:** Nervous system (primary); ophthalmic/visual system (secondary immune-privileged extension); by definition, PCNSL spares other organ systems at diagnosis — systemic (extra-CNS) involvement is exclusionary for the "primary" designation.

**Suggested UBERON terms:** UBERON:0000955 (brain); UBERON:0002316 (white matter of brain — for periventricular/deep involvement); UBERON:0002037 (cerebellum); UBERON:0002298 (brainstem); UBERON:0002240 (spinal cord); UBERON:0002037/UBERON:0016540 leptomeninges (UBERON:0002360 meninges; more specifically UBERON:0002215 pia mater / arachnoid mater); UBERON:0004087 (vitreous body); UBERON:0000966 (retina).

**Tissue and cell level:**
- Malignant lymphoid infiltrate with characteristic **perivascular/angiocentric cuffing** pattern around CNS microvasculature, with centroblastic-to-immunoblastic cytomorphology.
- Reactive infiltrate: T lymphocytes (CD4+ peritumoral, CD8+ intratumoral), tumor-associated macrophages/microglia (M1/M2 subsets), reactive astrocytes, reactive non-neoplastic B cells.
- **Suggested CL terms:** CL:0000542 (lymphocyte, neoplastic B-cell subtype); CL:0000980-adjacent centroblast/immunoblast morphologic descriptors; CL:0000129 (microglial cell); CL:0000127 (protoplasmic astrocyte).

**Subcellular level:** Nuclear translocation of NF-κB subunits (RelA/p65) as the central molecular hallmark of pathway activation; MHC class I/II trafficking defects at the endoplasmic reticulum/cell surface (relevant GO Cellular Component: GO:0005634 nucleus for NF-κB translocation; GO:0042612 MHC class I protein complex; GO:0042613 MHC class II protein complex).

**Localization:** Predominantly bilateral/midline-crossing (deep structures, corpus callosum "butterfly" pattern classically associated with high-grade gliomas but also seen in PCNSL) or multifocal; solitary lesions in ~65% of cases, multiple in ~35%. Vitreoretinal involvement, when present, is usually **bilateral**.

---

## 8. Temporal Development

**Onset:**
- Adult/late-onset disease overwhelmingly; median age at diagnosis ≈ 65–67 years in immunocompetent PCNSL, substantially younger (30s) in HIV-associated disease, and younger still (median ~23 years) in post-transplant PCNSL/PTLD.
- Onset pattern: **subacute** — symptoms evolve typically over days to a few weeks rather than the more chronic, insidious pattern of low-grade gliomas, but less abruptly than a stroke-like acute presentation.

**Progression:**
- **Disease course:** Aggressive and progressive in the absence of treatment; untreated PCNSL carries a very short survival (historically weeks to a few months).
- **Staging:** PCNSL does not use conventional Ann Arbor nodal staging given its extranodal, CNS-confined nature; instead, **extent-of-disease workup** (contrast MRI brain ± spine, CSF analysis, slit-lamp ophthalmologic exam, whole-body 18F-FDG PET/CT to exclude occult systemic lymphoma, HIV serology) defines the disease at diagnosis.
- **Progression rate:** Variable but generally rapid without treatment; with treatment, disease course is punctuated by induction response, consolidation, and — in a substantial minority — relapse.
- **Relapse pattern:** 15–25% of patients are primary refractory to HD-MTX-based induction; 25–50% of initial responders relapse. Median overall survival after relapse is markedly short: ~2 months for primary refractory disease and ~3.7 months for those relapsing within the first year of initial response, underscoring the poor prognosis of the relapsed/refractory setting.

**Patterns:**
- **Remission:** Achievable with modern chemoimmunotherapy induction (complete response rates 17–69% depending on regimen and patient fitness) and further consolidation (autologous stem cell transplant or non-myeloablative chemotherapy), can be durable — 5-year PFS as high as 65–75% in fit patients receiving optimal thiotepa-based ASCT consolidation in clinical trials.
- **Critical periods/windows:** The interval to diagnosis (biopsy) is a critical time-sensitive step given rapid disease evolution and the confounding effect of corticosteroids on both symptoms and diagnostic yield (steroids should be withheld pending biopsy whenever clinically feasible, as they can induce dramatic but transient radiographic and histopathologic response, obscuring diagnosis).

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence:** Rising over recent decades — from ~0.30 per 100,000 to 0.44–0.47 per 100,000 person-years in more recent estimates; a roughly 5-fold increase in the US from 1975–2017 has been reported, driven predominantly by rising incidence among **immunocompetent** patients >60 years old (in ages 70–79, incidence reaches ~4.32 per 100,000). This trend contrasts with the sharp decline in HIV-associated PCNSL following cART introduction.
- **Prevalence:** PCNSL constitutes ~2–4% of all primary CNS tumors, 4–6% of extranodal non-Hodgkin lymphomas, and ~1% of all lymphomas overall — a rare disease by any standard definition.
- **HIV cohort incidence:** Declined from ~5 cases/1,000 person-years (1991–1994) to ~0.32/1,000 person-years post-1999 (cART era).

### Inheritance Pattern
PCNSL is **not a Mendelian/heritable disorder** — it is a sporadic acquired somatic malignancy. There is no established autosomal dominant, autosomal recessive, X-linked, or mitochondrial inheritance pattern for sporadic PCNSL itself. The only heritable component relevant to PCNSL risk is indirect: **inherited primary immunodeficiency syndromes** (Wiskott-Aldrich syndrome — X-linked recessive; ataxia-telangiectasia — autosomal recessive; X-linked lymphoproliferative disease — X-linked recessive) that predispose to secondary/PCNSL-type lymphomas as a downstream consequence of immune dysfunction, not through a direct oncogenic germline variant in the lymphoma itself.
- **Penetrance/expressivity:** Not applicable in the classic Mendelian sense; risk in immunodeficiency syndromes is better framed as a cumulative lifetime probability (~4% in the congenital immunodeficiency group cited above) rather than penetrance of a single variant.
- **Genetic anticipation, germline mosaicism, founder effects, consanguinity:** Not established/applicable for sporadic PCNSL; may be relevant to the underlying primary immunodeficiency syndromes in isolated pedigrees but not to PCNSL as a disease entity per se.

### Population Demographics
- **Affected populations:** No strong ethnic/racial predisposition reported for sporadic immunocompetent PCNSL, though HIV-associated PCNSL epidemiology tracks with regional HIV prevalence and cART access disparities globally.
- **Geographic distribution:** Global; incidence patterns most robustly characterized in US (SEER), European, and East Asian cohorts; HIV-associated PCNSL remains disproportionately prevalent in regions with limited cART access.
- **Sex ratio:** Male:female ≈ 1.2:1 in immunocompetent disease overall; strongly male-predominant in HIV-associated disease (tracking HIV epidemiology); PVRL (isolated vitreoretinal presentation) is slightly more common in women.
- **Age distribution:** Bimodal-leaning pattern — a smaller, younger peak associated with immunosuppression (HIV, transplant, median 20s–40s) and a larger, dominant peak in immunocompetent elderly patients (median 65–67 years, rising incidence with advancing age through the 70s).

---

## 10. Diagnostics

### Clinical/Laboratory Tests
- **CSF analysis:** Typically shows elevated leukocyte count, normal glucose, elevated protein. Flow cytometry for clonal B-cell population improves diagnostic sensitivity over cytology alone but remains imperfect (positive in a minority even with disease present).
- **CSF biomarkers (molecular diagnostics):** Combined **MYD88 L265P mutation detection** (by allele-specific PCR or digital droplet PCR, ddPCR) plus **IL-10** quantification (and IL-10/IL-6 ratio) in CSF is now established as a highly accurate, minimally invasive diagnostic adjunct, particularly valuable when biopsy is high-risk or tissue is non-diagnostic. Using a CSF IL-10 cutoff of 8.2 pg/mL, sensitivity/specificity were 95.5%/96.1%; for an IL-10/IL-6 ratio cutoff of 0.72, sensitivity/specificity were 95.5%/100.0% (*Scientific Reports* 2016, PMC5141427). In multivariable analysis, MYD88 positivity (OR 71.90) and elevated IL-10 (OR 2.82, P<.0001) were each independently associated with CNS lymphoma. A CSF biomarker panel combining MYD88, IL-10, and CXCL13 has been proposed for further sensitivity gains ("Molecular diagnosis of primary CNS lymphoma in 2024 using MYD88Leu265Pro and IL-10," *Lancet Haematology* 2024).
- **Vitreous/aqueous humor analysis** (for suspected vitreoretinal involvement): cytology, IL-10/IL-6 ratio, and MYD88 L265P testing.

### Imaging
- **Gadolinium-enhanced brain MRI** is the standard imaging modality — the disease-defining, essential first-line study for suspicion, extent-of-disease mapping, treatment response monitoring, and recurrence detection. Lesions classically show homogeneous, avid contrast enhancement (unlike the heterogeneous ring-enhancement of glioblastoma or abscess), restricted diffusion on DWI (reflecting high cellularity/nuclear-to-cytoplasmic ratio), and relatively lower relative cerebral blood volume (rCBV) on perfusion imaging than high-grade glioma.
- **Advanced/emerging imaging:** Diffusion-weighted imaging with ADC quantification, dynamic susceptibility contrast (DSC)-MRI, amino acid/FDG brain PET, dynamic contrast-enhanced (DCE)-MRI, and radiomics approaches are under active investigation to improve non-invasive diagnostic accuracy and differentiate PCNSL from glioblastoma, demyelinating disease, and infection/abscess.
- **Whole-body 18F-FDG PET/CT:** Performed as part of staging to exclude occult systemic (extra-CNS) lymphoma, which would reclassify the case as secondary rather than primary CNS lymphoma.

### Tissue Diagnosis (Gold Standard)
- **Stereotactic brain biopsy** is the diagnostic gold standard for parenchymal disease. Corticosteroids should be withheld before biopsy whenever clinically safe, since they exert a rapid cytolytic effect on lymphoma cells, can produce dramatic (but often transient) radiographic "vanishing tumor" responses in up to half of patients, and confound both radiographic and histopathologic diagnosis.
- **Vitrectomy** is the diagnostic gold standard for primary vitreoretinal lymphoma when ocular involvement predominates, sparing brain biopsy in appropriately selected patients; chorioretinal biopsy offers higher diagnostic yield than vitrectomy but is reserved for select cases owing to greater risk of visual sequelae.
- **CSF cytology/flow cytometry** can obviate brain biopsy when clearly positive, though sensitivity is limited.

### Histopathology/Immunohistochemistry
- Large lymphocytes in solid sheets with characteristic **perivascular, angiocentric infiltration**; **centroblastic-to-immunoblastic** cytomorphology.
- Immunophenotype: B-cell markers **CD20+, CD79a+, PAX5+**; late-germinal-center/post-germinal-center markers **BCL6+ (60–100%)** and **MUM1/IRF4+ (90–100%)**; CD10+ in only 10–20% of cases; **non-GCB (ABC-like) phenotype** predominates overall (~90% of cases) by Hans algorithm/IHC classification; IgM and IgD are almost always expressed (reflecting failure of immunoglobulin class-switch recombination), while class-switched isotypes are rare.
- High Ki-67/MIB-1 proliferation index typical of aggressive DLBCL.

**Suggested NCIT/SNOMED-adjacent term:** NCIT:C36044 (Diffuse Large B-Cell Lymphoma); the CNS-specific entity is best represented via NCIT:C9218.

### Genetic/Molecular Testing
- Targeted mutation panels or NGS for **MYD88 L265P, CD79B, PIM1, CDKN2A** confirm the disease's characteristic genomic signature and can support diagnosis in ambiguous cases; not required for diagnosis when histopathology/IHC is conclusive but increasingly used both diagnostically (via CSF liquid biopsy, above) and for genomic subtype (MCD) characterization relevant to targeted therapy selection.
- Whole-exome/whole-genome sequencing has defined the broader genomic landscape (*Nature Communications* 2022) but is primarily a research/discovery tool rather than routine clinical diagnostic practice at this time.

### Clinical Criteria/Differential Diagnosis
Key differentials requiring exclusion include glioblastoma and other high-grade gliomas, demyelinating pseudotumor (tumefactive multiple sclerosis), toxoplasmosis and other CNS infections (especially in HIV-positive patients, where PCNSL and toxoplasmosis are the two leading causes of a ring/homogeneously-enhancing mass and can be difficult to distinguish without biopsy or EBV-PCR/thallium-SPECT adjuncts), sarcoidosis, and metastatic disease.

### Screening
No population-based screening program exists for PCNSL in asymptomatic individuals, including in HIV-positive populations, where clinical vigilance for neurological symptoms at low CD4+ counts substitutes for formal screening.

---

## 11. Outcome/Prognosis

### Prognostic Scoring Systems
- **International Extranodal Lymphoma Study Group (IELSG) score:** Five adverse factors — age >60 years, ECOG performance status >1, elevated serum LDH, elevated CSF protein concentration, and involvement of deep brain structures. Two-year survival stratifies sharply by risk group: **80%** (0–1 factors), **48%** (2–3 factors), and **15%** (4–5 factors).
- **Memorial Sloan Kettering Cancer Center (MSKCC) score:** Based on age and Karnofsky performance status (KPS). Patients >50 years with KPS <70 have the worst prognosis (median survival ~1.1 years); patients >50 with KPS ≥70 have median survival ~3.2 years.
- Additional emerging markers include the **LDH-to-lymphocyte ratio**, proposed to refine stratification within the low/intermediate MSKCC risk groups.

### Survival and Mortality
- With modern chemoimmunotherapy, PCNSL is potentially curable, particularly in patients ≤70 years who tolerate intensive induction plus consolidation.
- **Elderly patients (≥65 years)** have markedly worse outcomes: population-based 1-, 5-, and 10-year survival estimated at 33–48%, 13–24%, and 10–13% respectively; fewer than half of elderly patients are alive at 1 year in some series.
- **Fit patients receiving optimal induction + thiotepa-based ASCT consolidation** have achieved 5-year PFS ~65% and OS ~79% in leading trials (e.g., IELSG32-derived data), with the PRECIS trial reporting 8-year relapse-free survival of 94% after ASCT versus 48% after WBRT consolidation.

### Morbidity/Function and Complications
- Complications include treatment-related **cytopenias/infection** (from HD-MTX, HDC-ASCT conditioning), **nephrotoxicity** from methotrexate, and — most consequentially for long-term quality of life — **radiation-induced neurotoxicity**: delayed-onset neurocognitive decline, gait disturbance, urinary incontinence, and personality change, particularly with WBRT doses >40 Gy and in patients >60 years. Combined chemoradiotherapy carries a cumulative 5-year neurotoxicity incidence of 25–35%, with associated mortality of ~30% among those affected; median survival after neurotoxicity onset is <1–2 years. Neuroimaging in radiation neurotoxicity shows brain volume loss, cortical/subcortical atrophy, and diffuse white matter injury; autopsy findings include myelin and axonal loss, gliosis, spongiosis, and small/large vessel injury.
- By contrast, ASCT-based consolidation preserves or improves cognitive function/quality of life relative to the general population in long-term survivors, in direct contrast to the progressive decline seen after WBRT (PRECIS trial data).

### Prognostic Biomarkers
IELSG and MSKCC clinical scores remain the mainstay; molecular prognostic markers under investigation include LymphGen/MCD genomic subtype (associated with inferior chemoimmunotherapy response), 6p21.3 CN-LOH/HLA homozygous deletion, and BTG1/ETV6/TP53 mutation status (each associated with significantly shorter PFS/OS in genomic cohort studies).

---

## 12. Treatment

### Pharmacotherapy — Induction (Fit Patients)
High-dose methotrexate (HD-MTX, 3.5–8 g/m²) is the essential backbone of induction, given its capacity to cross the blood-brain barrier at high dose. NCIT: methotrexate maps to **NCIT:C733**; treatment_term class **NCIT:C15632 (Chemotherapy)** or **NCIT:C15986 (Pharmacotherapy)** as appropriate.

Regimens (increasing intensity):
- **HD-MTX/cytarabine (AraC)** ± **rituximab (R-MTX/AraC)** — CHEBI: methotrexate CHEBI:44185; cytarabine CHEBI:28680; rituximab is a monoclonal antibody (NCIT:C1454) — therapeutic_agent classification NCIT for biologics.
- **MATRix regimen** (HD-MTX + HD-AraC + rituximab + thiotepa; CHEBI: thiotepa CHEBI:9560) — the IELSG32-validated standard, associated with significantly improved response and survival with modest additional hematologic toxicity; **regimen_term** candidate NCIT term for named combination protocol where available.
- **R-MPV** (rituximab, HD-MTX, procarbazine [CHEBI:8428], vincristine [CHEBI:75261]).
- **MT-R** (HD-MTX + temozolomide [CHEBI:41332] + rituximab).

### Consolidation
- **High-dose chemotherapy with autologous stem-cell transplant (HDC-ASCT)**, particularly **thiotepa-based conditioning**, is superior to BEAM conditioning (3-year PFS 75% vs 58%). Randomized trials (IELSG32, PRECIS) show comparable 2-year PFS between ASCT (75–76%) and WBRT consolidation, but markedly better long-term relapse-free survival, cognitive preservation, and quality of life with ASCT (PRECIS 8-year RFS: 94% ASCT vs 48% WBRT).
- **Reduced-dose WBRT** (e.g., RTOG1114 protocol) plus chemotherapy improves PFS versus chemotherapy alone (2-year PFS 78% vs 54%) but carries the neurotoxicity burden discussed in Section 11, and is now generally reserved for patients ineligible for ASCT.
- **Non-myeloablative consolidation chemotherapy** (e.g., AraC/etoposide [CHEBI:45602], as in the Alliance trial) is an alternative for patients unsuitable for ASCT, though generally inferior PFS compared with ASCT in randomized comparison (2-year PFS 51% vs 73%).
- NCIT treatment_term for stem-cell transplantation: **NCIT:C15431** (Hematopoietic Cell Transplantation) → `therapeutic_modality: CELL_THERAPY`.

### Elderly/Unfit Patients
Attenuated-dose HD-MTX (often ≤3.5 g/m²) with careful monitoring achieves CR rates 17–69%; consolidation typically avoids WBRT given high neurotoxicity risk in this population, favoring maintenance strategies (temozolomide, procarbazine, rituximab, lenalidomide, or ibrutinib maintenance) under active trial investigation (e.g., FIORELLA trial NCT03495960; ALLIANCE A51901 NCT04609046; NCT02313389).

### Targeted/Novel Therapeutics (Relapsed/Refractory Disease)
- **BTK inhibitors:** **Ibrutinib** (CHEBI:70925; NCIT:C64176) achieves response rates up to 50–77% in relapsed/refractory PCNSL (10/13 patients responding, including 5 CRs, in a Phase I/II MSKCC trial), though median duration of response is short (<6 months); risk of invasive fungal infection can be mitigated with isavuconazole prophylaxis. **Tirabrutinib**, a second-generation BTK inhibitor, achieved ORR 67% regardless of MYD88/CD79B/CARD11 mutation status.
- **Immunomodulatory agents:** **Lenalidomide** (CHEBI:63791; NCIT:C29258) and **pomalidomide** (ORR 48%, median DOR 4.7 months in a Phase I study), used alone or in combination (e.g., R2I: rituximab-lenalidomide-ibrutinib, prospective trial NCT03703167).
- **Immune checkpoint inhibitors:** Anti-PD-1 agents nivolumab and pembrolizumab (NCIT:C2185 immunotherapy class) — anecdotal efficacy reported; formal Phase 2 trials (NCT02857426, NCT02779101) completed with results pending/reported in subsequent literature.
- **CAR-T cell therapy:** CD19-directed CAR-T (NCT04134117, tisagenlecleucel trial in PCNSL, among others) shows feasibility with some durable responses in small early-phase studies; combination with BTK inhibitors and PD-1 blockade under investigation for synergy in CNS lymphoma.
- **IRAK4 inhibitor:** Emavusertib (CA-4948) — Phase I/II trial NCT03328078 in relapsed/refractory PCNSL, targeting the MYD88-driven IRAK signaling node directly.
- **Blood-brain barrier penetration strategies:** TNF-alpha/NGR conjugates to permeabilize tumor vasculature; nanoparticle drug delivery; focused ultrasound — early-stage investigational approaches to improve CNS drug penetration.

### Surgical/Interventional
Surgery in PCNSL is limited to diagnostic biopsy — **cytoreductive resection is not standard of care** (unlike glioma), as PCNSL is a chemosensitive, radiosensitive, diffusely infiltrative systemic-type malignancy rather than a mass amenable to surgical cure; resection does not improve outcomes and risks neurological morbidity, though rare exceptions (solitary accessible lesion causing critical mass effect) are individualized.

### Supportive/Rehabilitative Care
Corticosteroids (dexamethasone) for symptomatic vasogenic edema (used cautiously pre-biopsy, as above); anticonvulsants for seizures; comprehensive neurocognitive rehabilitation and physical/occupational therapy for treatment-related or disease-related functional deficits (NCIT:C15302 Physical Therapy; NCIT:C121351 Occupational Therapy); best supportive care alone is appropriate for select frail/unfit patients for whom intensive therapy is not feasible.

### Treatment Algorithms
Modern management follows an age/fitness-stratified algorithm: (1) fit patients receive HD-MTX-based induction (MATRix or equivalent) followed by consolidation (ASCT preferred over WBRT where feasible); (2) unfit/elderly patients receive attenuated induction with maintenance-based or reduced-intensity consolidation; (3) relapsed/refractory disease is preferentially managed on clinical trial given median OS of only 2–3.7 months with standard salvage approaches, with BTK inhibitors, immunomodulatory agents, checkpoint inhibitors, and CAR-T among emerging options.

---

## 13. Prevention

- **Primary prevention:** No established primary prevention strategy exists for PCNSL in immunocompetent individuals, as no modifiable environmental or lifestyle risk factor has been robustly confirmed.
- **Immunosuppression management as risk mitigation:** For immune-deficient patients, treatment/optimization of the underlying immunosuppression state constitutes the principal preventive lever — most concretely demonstrated by the dramatic decline in HIV-associated PCNSL incidence following widespread combination antiretroviral therapy (cART) adoption (from ~5 to ~0.32 cases per 1,000 person-years).
- **Secondary prevention/screening:** No formal population-based or risk-group screening program exists for asymptomatic PCNSL detection, including among HIV-positive or transplant populations; management instead relies on clinical vigilance for neurological symptoms in at-risk groups and prompt neuroimaging/biopsy workup once symptoms arise.
- **Tertiary prevention:** Minimizing treatment-related neurotoxicity (preferring ASCT-based consolidation over WBRT where feasible in eligible patients, using reduced-dose WBRT protocols when radiotherapy is required, and structured neurocognitive monitoring) functions as tertiary prevention against long-term disability in survivors.
- **Counseling:** Genetic counseling is relevant primarily in the context of the underlying congenital immunodeficiency syndromes (Wiskott-Aldrich, ataxia-telangiectasia, XLP) that predispose to PCNSL, rather than for PCNSL as an inherited entity itself.

---

## 14. Other Species / Natural Disease

- **Dogs (*Canis lupus familiaris*, NCBITaxon:9615):** CNS lymphoma occurs in dogs, most often as part of multicentric lymphoma with secondary CNS/leptomeningeal/choroid plexus infiltration (reported in up to ~12–30% of canine lymphoma cases with CNS involvement), though isolated primary CNS B-cell lymphoma in a young dog has also been reported (PMC3327599). Mean age of onset ~7.4 years (range 3–11); no strong breed predisposition overall, though Rottweilers show a slightly elevated risk. Forebrain is the most frequent site.
- **Cats (*Felis catus*, NCBITaxon:9685):** CNS lymphoma is less common than in dogs, accounting for <3% of primary CNS tumors in cats; forebrain meninges (B-cell phenotype) is the most frequent site, while spinal cord lymphoma is more associated with younger cats.
- **Comparative pathology:** Veterinary CNS lymphoma studies (*MDPI Animals* 2023, "Neuropathology of Central and Peripheral Nervous System Lymphoma in Dogs and Cats," 92-case series) demonstrate broadly analogous perivascular/leptomeningeal infiltrative patterns to human PCNSL, though most veterinary cases represent secondary/multicentric rather than strictly primary disease, limiting direct translational equivalence to human isolated PCNSL biology.
- **Orthologous genes:** MYD88, CD79B, CDKN2A, and TP53 orthologs are well conserved across mammals (canine MYD88 ortholog, NCBI Gene; feline orthologs similarly annotated), supporting biological plausibility of shared BCR/TLR-NF-κB pathway dysregulation, though specific somatic mutation profiling of veterinary CNS lymphoma is not yet as well characterized as in human disease.
- **Zoonotic potential:** None — PCNSL is a non-communicable malignancy; EBV itself is not classically zoonotic in this context (human-restricted gammaherpesvirus).

---

## 15. Model Organisms

### Patient-Derived Xenograft (PDOX) Models
The most biologically faithful available models are **orthotopic patient-derived xenografts**: PCNSL patient specimens grafted into the **caudate nucleus of immunodeficient nude mice** achieve an ~83% engraftment success rate, whereas **subcutaneous implantation fails to generate tumors** — direct experimental evidence for the essential role of the brain microenvironment in PCNSL pathophysiology (*Neuro-Oncology*/ScienceDirect, "Primary CNS lymphoma patient-derived orthotopic xenograft model"). PDOX models recapitulate diffuse B-cell infiltration of brain parenchyma and preserve each patient's unique BCR/NF-κB pathway mutational signature, supporting their use for precision-oncology drug-sensitivity testing.

### Cell-Line-Derived Xenograft Models
Earlier xenograft models (e.g., PMID for "A new xenograft model of primary central nervous system lymphoma," 1999) established feasibility of intracerebral engraftment using lymphoma cell lines in athymic/nude mice, with tumor growth monitored via bioluminescence imaging in modern iterations.

### Rat Models
A nude-rat PCNSL model has been reported to reproduce both the histology and characteristic anatomic location of human CNS lymphoma, offering a larger-animal platform for some interventional/imaging studies.

### Model Characteristics, Applications, and Limitations
- **Phenotype recapitulation:** Orthotopic (intracerebral) engraftment is essential — subcutaneous models do not reproduce disease, underscoring that the CNS/brain microenvironment (immune privilege, blood-brain barrier, local chemokine milieu) is not merely a permissive site but an active contributor to PCNSL biology and must be modeled directly.
- **Applications:** PDOX models support (a) validation of the perivascular/angiocentric growth pattern, (b) preclinical testing of blood-brain-barrier-penetrant agents (HD-MTX, novel BTK inhibitors, nanoparticle-based delivery), and (c) patient-specific drug-sensitivity screening reflecting individual BCR/NF-κB mutational profiles.
- **Limitations:** Immunodeficient host models (nude/NOD-SCID mice) cannot recapitulate the tumor-immune microenvironment interactions (T-cell exhaustion, macrophage/microglia polarization, checkpoint biology) that are increasingly recognized as central to PCNSL pathophysiology and to immunotherapy response — a significant translational gap for checkpoint-inhibitor and CAR-T preclinical development, which more plausibly requires humanized or syngeneic immunocompetent models (not yet well established for PCNSL specifically in the literature surveyed here).
- **Resources:** No PCNSL-specific standardized repository was identified analogous to MGI/IMPC germline knockout collections (consistent with PCNSL's somatic, non-heritable biology); available models are largely investigator-generated PDX/PDOX lines maintained at individual research centers rather than centrally cataloged.

---

## Summary of Key Ontology Term Suggestions

| Category | Suggested terms |
|---|---|
| Disease identity | MONDO:0002571; NCIT:C9218; ICD-O-3 9680/3 |
| Causal genes | MYD88 (hgnc:7562), CD79B (hgnc:1699), PIM1 (hgnc:8986), CDKN2A (hgnc:1787), CARD11 (hgnc:16412), B2M (hgnc:914), TP53 (hgnc:11998), BCL6 (hgnc:1001) |
| Biological processes (GO) | GO:0007249 (NF-κB signaling), GO:0050853 (BCR signaling), GO:0002224 (TLR signaling) |
| Cell types (CL) | CL:0000236 (B cell, neoplastic), CL:0000129 (microglial cell), CL:0000235 (macrophage), CL:0000625 (CD8+ T cell), CL:0000127 (astrocyte) |
| Anatomy (UBERON) | UBERON:0000955 (brain), UBERON:0002240 (spinal cord), UBERON:0002360 (meninges), UBERON:0004087 (vitreous body), UBERON:0000966 (retina) |
| Phenotypes (HP) | HP:0034332 (focal neurologic deficit), HP:0000708 (behavioral abnormality), HP:0002315 (headache), HP:0001250 (seizure), HP:0000618 (blurred vision), HP:0002922 (increased CSF protein) |
| Chemicals (CHEBI) | CHEBI:44185 (methotrexate), CHEBI:28680 (cytarabine), CHEBI:9560 (thiotepa), CHEBI:70925 (ibrutinib), CHEBI:63791 (lenalidomide), CHEBI:41332 (temozolomide) |
| Treatments (NCIT) | NCIT:C15632 (Chemotherapy), NCIT:C15431 (Hematopoietic Cell Transplantation), NCIT:C15313 (Radiation Therapy), NCIT:C2185 (Immunotherapy) |

---

## Notes on Evidence Gaps
- Precise PMIDs were not retrievable for every source cited in this search-tool-mediated survey; several citations are identified by PMCID, journal/year, or DOI where PMID was not directly surfaced in search snippets — a curator populating a formal knowledge-base entry should re-verify each citation against PubMed directly before use (per this repository's evidence-sourcing discipline, every CURIE and citation must be read from a source at write time, not reconstructed from this report).
- Germline/heritable genetic risk data for PCNSL specifically (as opposed to the associated congenital immunodeficiency syndromes) is limited; no GWAS-identified common-variant susceptibility loci were found.
- Standardized, centrally cataloged genetic mouse models (knockout/knock-in/conditional) specific to PCNSL were not identified in this search; the field relies primarily on xenograft/PDOX approaches given the disease's somatic rather than germline genetic basis.

---

### Sources

- [Primary central nervous system lymphomas: EHA–ESMO Clinical Practice Guideline (Annals of Oncology / HemaSphere 2024)](https://www.annalsofoncology.org/article/S0923-7534(23)05074-3/fulltext)
- [Primary central nervous system lymphoma — current standards and recent developments (Neuro-Oncology Practice)](https://academic.oup.com/nop/article/13/4/640/8495130)
- [Primary central nervous system lymphoma — PMC (comprehensive clinical review)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10637780/)
- [Primary Central Nervous System Lymphoma Epidemiology — Rare Disease Advisor](https://www.rarediseaseadvisor.com/disease-info-pages/primary-central-nervous-system-lymphoma-epidemiology/)
- [Primary central nervous system lymphoma — Nature Reviews Disease Primers (PMID:37322012)](https://www.nature.com/articles/s41572-023-00439-0)
- [MYD88 L265P mutation in PCNSL associated with better survival — Neuro-Oncology Advances](https://academic.oup.com/noa/article/3/1/vdab090/6316734)
- [MYD88 L265P mutation and CDKN2A loss are early mutational events — Blood Advances](https://ashpublications.org/bloodadvances/article/3/3/375/246790/MYD88-L265P-mutation-and-CDKN2A-loss-are-early)
- [CD79B Y196 mutation predictive marker for R-MPV response — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10067082/)
- [Primary CNS Lymphoma — Medscape](https://emedicine.medscape.com/article/1157638-overview)
- [HIV-related lymphomas: Primary CNS lymphoma — UpToDate](https://www.uptodate.com/contents/hiv-related-lymphomas-primary-central-nervous-system-lymphoma)
- [EBV-associated primary CNS lymphoma after immunosuppression — Blood 2021](https://ashpublications.org/blood/article/137/11/1468/474186/EBV-associated-primary-CNS-lymphoma-occurring)
- [Differential expression of TLR and BCR signaling molecules in PCNSL — Journal of Neuro-Oncology](https://link.springer.com/article/10.1007/s11060-014-1655-3)
- [Primary DLBCL of CNS: molecular and biological features — Annals of Lymphoma](https://aol.amegroups.org/article/view/8014/html)
- [Full article: Targets and treatments in primary CNS lymphoma](https://www.tandfonline.com/doi/full/10.1080/10428194.2024.2342560)
- [Biology of CNS lymphoma and the potential of novel agents — ASH Education Program](https://ashpublications.org/hematology/article/2017/1/556/21097/Biology-of-CNS-lymphoma-and-the-potential-of-novel)
- [Primary CNS Lymphoma — NORD](https://rarediseases.org/rare-diseases/primary-central-nervous-system-lymphoma/)
- [Primary central nervous system lymphoma: Imaging features and differential diagnosis — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11531061/)
- [Primary CNS lymphoma — MedLink Neurology](https://www.medlink.com/articles/primary-cns-lymphoma)
- [Primary CNS Lymphomas: Challenges in Diagnosis and Monitoring — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6033255/)
- [Primary central nervous system lymphoma: epidemiology and clinical presentation — Annals of Lymphoma](https://aol.amegroups.org/article/view/7225/html)
- [Pathology Outlines — Primary CNS lymphoma](https://www.pathologyoutlines.com/topic/lymphomaprimaryCNSlymphoma.html)
- [Diagnosis, Treatment, and Follow Up of Primary CNS Lymphomas — Medscape](https://reference.medscape.com/cc2/p10/diagnosis-treatment-and-follow-primary-central-nervous-2025a100059g)
- [Rituximab with high-dose methotrexate is effective and cost-effective — Scientific Reports](https://www.nature.com/articles/s41598-022-24922-y)
- [Chemoimmunotherapy with MATRix regimen — IELSG32 phase 2 trial](https://www.sciencedirect.com/science/article/abs/pii/S2352302616000363)
- [A Nomogram for Predicting Overall Survival in PCNSL — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11827503/)
- [Older patients with PCNSL: Survival and prognostication — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10979647/)
- [Evaluation of MSKCC and IELSG prognostic scoring systems — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5840438/)
- [LDH-to-Lymphocyte Ratio prognostic marker — Frontiers in Oncology](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.696147/full)
- [Phase Ib/II Trial of Ibrutinib with Rituximab and Lenalidomide — Blood](https://ashpublications.org/blood/article/140/Supplement%201/3807/489874/Phase-Ib-II-Trial-of-the-Bruton-s-Tyrosine-Kinase)
- [Ibrutinib Unmasks Critical Role of BTK in Primary CNS Lymphoma — PubMed](https://pubmed.ncbi.nlm.nih.gov/28619981/?dopt=Abstract)
- [BTK inhibitors for PCNSL: current progress — Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/10428194.2024.2333985)
- [CA-4948-101 emavusertib trial — ClinicalTrials.gov NCT03328078](https://clinicaltrials.gov/study/NCT03328078)
- [TEDDI-R ibrutinib trial — ClinicalTrials.gov NCT02203526](https://clinicaltrials.gov/study/NCT02203526)
- [Pathology and new insights in CNS lymphomas — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10408733/)
- [Primary CNS lymphoma: Comprehension of cell-of-origin subtypes — PubMed](https://pubmed.ncbi.nlm.nih.gov/37530337/)
- [MYC Protein Expression in Primary DLBCL of the CNS — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4257680/)
- [Primary CNS lymphoma patient-derived orthotopic xenograft model — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1079979618304273)
- [Central Nervous System Lymphoma — MalaCards](https://www.malacards.org/card/central_nervous_system_lymphoma)
- [Central Nervous System Lymphoma — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK545145/)
- [The Landscape of PCNSL: Clinicopathologic and Genomic Characteristics — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12428670/)
- [Sorting biologic subtypes of primary CNS lymphoma — Blood](https://ashpublications.org/blood/article/137/11/1436/475491/Sorting-biologic-subtypes-of-primary-CNS-lymphoma)
- [Genomic Landscape and Molecular Subtypes of PCNSL — medRxiv](https://www.medrxiv.org/content/10.1101/2024.10.22.24315961.full.pdf)
- [Amplification of 9p24.1 in DLBCL — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6717207/)
- [Cerebrospinal Fluid IL-10 and IL-10/IL-6 as Diagnostic Biomarkers — Scientific Reports](https://www.nature.com/articles/srep38671)
- [Molecular diagnosis of PCNSL in 2024 using MYD88 and IL-10 — Lancet Haematology](https://www.thelancet.com/journals/lanhae/article/PIIS2352-3026(24)00104-2/abstract)
- [Combining MYD88 mutation detection and clonality determination — British Journal of Haematology](https://onlinelibrary.wiley.com/doi/10.1111/bjh.18758)
- [2026 NCCN Primary CNS Lymphoma Patient Guidelines](https://www.nccn.org/patients/guidelines/content/PDF/pcnsl-patient.pdf)
- [Diagnosis of PCNSL: systematic review of CSF screening and early brain biopsy — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6899047/)
- [Current and emerging therapies for PCNSL — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8101140/)
- [Targeted Therapies and Immune Checkpoint Inhibitors in PCNSL — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8234854/)
- [How I treat primary CNS lymphoma — Blood](https://ashpublications.org/blood/article/118/3/510/28945/How-I-treat-primary-CNS-lymphoma)
- [Full article: Tumor microenvironment in PCNSL](https://www.tandfonline.com/doi/full/10.1080/15384047.2024.2425131)
- [Immune evasion in PCNSL: macrophage and T cell roles — PubMed](https://pubmed.ncbi.nlm.nih.gov/42021682/)
- [Unraveling the immune microenvironment in primary CNS lymphoma — Biomarker Research](https://link.springer.com/article/10.1186/s40364-026-00945-9)
- [Advances in primary large B-cell lymphoma of immune-privileged sites — PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11896999/)
- [Primary vitreoretinal lymphoma: a diagnostic and management challenge — Blood](https://ashpublications.org/blood/article/138/17/1519/476013/Primary-vitreoretinal-lymphoma-a-diagnostic-and)
- [Secondary Versus Recurrent CNS Lymphoma — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12334250/)
- [Treatment Strategies and Prognostic Factors in Secondary CNS Lymphoma — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10365212/)
- [DLBCL involving the CNS: biologic rationale for targeted therapy — Haematologica](https://haematologica.org/article/view/haematol.2021.278613)
- [Neuropathology of CNS and Peripheral Nervous System Lymphoma in Dogs and Cats — MDPI Animals](https://www.mdpi.com/2076-2615/13/5/862)
- [Primary central nervous system B-cell lymphoma in a young dog — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3327599/)
- [The Challenge of Primary CNS Lymphoma — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5127405/)
- [Identification of genomic biomarkers of disease progression and survival in PCNSL — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11914178/)
- [The genomic and transcriptional landscape of PCNSL — Nature Communications](https://www.nature.com/articles/s41467-022-30050-y)
- [Chromosomal imbalances and partial uniparental disomies in PCNSL — Leukemia](https://www.nature.com/articles/leu2009120)
- [Extensive genetic alterations of the HLA region in B-cell lymphomas of immune-privileged sites — Blood](https://ashpublications.org/blood/article/96/10/3569/181000/Extensive-genetic-alterations-of-the-HLA-region)
- [Targetable genetic features of primary testicular and primary CNS lymphomas — Blood](https://ashpublications.org/blood/article/127/7/869/35232/Targetable-genetic-features-of-primary-testicular)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 32 |
| On topic | 27 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 75 |
| Resolved | 70 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 4 |
| Unverifiable | 1 |
| Terms whose name was checked | 31 |
| Terms named correctly | 18 |
| Terms named as a **different** term | 6 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C9218` (3 mentions) - the report calls it "Primary Central Nervous System Lymphoma"; NCIT calls it **Stage IV Oropharyngeal Carcinoma AJCC v6**
- `CL:0000980` (2 mentions) - the report calls it "plasmablast-adjacent — not typically applicable, PCNSL retains B-cell not plasma-cell phenotype"; CL calls it **plasmablast**
- `UBERON:0002316` (1 mention) - the report calls it "white matter of brain — for periventricular/deep involvement"; UBERON calls it **white matter**
- `UBERON:0004087` (2 mentions) - the report calls it "vitreous body"; UBERON calls it **vena cava**
- `CL:0000542` (1 mention) - the report calls it "lymphocyte, neoplastic B-cell subtype"; CL calls it **lymphocyte**
- `NCIT:C36044` (1 mention) - the report calls it "Diffuse Large B-Cell Lymphoma"; NCIT calls it **Grade 3b Malignant Neoplasm**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002355` (obsolete Difficulty walking) (1 mention) - replaced by `HP:0001288`
- `NCIT:C36044` (Grade 3b Malignant Neoplasm) (1 mention)
- `CHEBI:9560` (CHEBI_9560) (2 mentions) - replaced by `CHEBI:102166`
- `CHEBI:45602` (CHEBI_45602) (1 mention) - replaced by `CHEBI:45605`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002922` (2 mentions) - the report calls it "Increased CSF protein"; HP calls it **Increased CSF protein concentration**, and lists "Increased CSF protein" among its other names
- `GO:0007249` (3 mentions) - the report calls it "I-kappaB kinase/NF-kappaB signaling"; GO calls it **canonical NF-kappaB signal transduction**, and lists "I-kappaB kinase/NF-kappaB signaling" among its other names
- `GO:0035666` (1 mention) - the report calls it "TRIF-independent TLR4/MYD88 pathway relevant terms as applicable"; GO calls it **TRIF-dependent toll-like receptor signaling pathway**, and lists "TRIF-dependent TLR signaling pathway" among its other names
- `GO:0043065` (1 mention) - the report calls it "positive regulation of apoptotic process — for the "de-regulation" direction"; GO calls it **positive regulation of apoptotic process**
- `GO:0000082` (1 mention) - the report calls it "G1/S transition of mitotic cell cycle, dysregulated"; GO calls it **G1/S transition of mitotic cell cycle**
- `CL:0002453` (1 mention) - the report calls it "oligodendrocyte, for demyelination context"; CL calls it **oligodendrocyte precursor cell**
- `CL:0000127` (3 mentions) - the report calls it "astrocyte", "protoplasmic astrocyte"; CL calls it **astrocyte**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000127` - called "astrocyte", "protoplasmic astrocyte"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.
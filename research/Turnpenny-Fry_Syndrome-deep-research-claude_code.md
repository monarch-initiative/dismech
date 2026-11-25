---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-24T01:01:59.355719'
end_time: '2026-11-24T01:07:20.784518'
duration_seconds: 321.43
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Turnpenny-Fry Syndrome
  mondo_id: MONDO:0032707
  category: Mendelian
  causal_genes: PCGF2
  omim_id: OMIM:618371
  synonyms: not recorded
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
  - claude-opus-5-5
  web_search_requests: 8
  num_turns: 16
  total_cost_usd: 0.83714138
  session_id: 5f01151a-9510-4ec0-80e5-3929005a93e8
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  tool_calls: 35
  retrieval_calls: 33
  assistant_text_blocks: 1
citation_count: 14
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 5
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:30343942
  relevance_assessed: 13
  on_topic: 4
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 76
  verified: 72
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 9
  labels_matching: 1
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: MONDO:0032707
    reported_labels:
    - MONDO
    ontology_label: turnpenny-fry syndrome
  - term_id: HP:0001250
    reported_labels:
    - 2/13; one additional adult case (PMID 40502890)
    ontology_label: Seizure
  - term_id: HP:0004322
    reported_labels:
    - most
    ontology_label: Short stature
  - term_id: HP:0002126
    reported_labels:
    - 4 of the 8 MRIs reviewed
    ontology_label: Polymicrogyria
  - term_id: HP:0002500
    reported_labels:
    - 8/8 MRIs
    ontology_label: Abnormal cerebral white matter morphology
  - term_id: HP:0006956
    reported_labels:
    - common
    ontology_label: Lateral ventricle dilatation
  - term_id: HP:0003468
    reported_labels:
    - 3 individuals
    ontology_label: Abnormal vertebral morphology
  - term_id: HP:0000776
    reported_labels:
    - 2/13; one additional case (PMID 38283775)
    ontology_label: Congenital diaphragmatic hernia
  obsolete_terms:
  - term_id: HP:0005111
    ontology_label: obsolete Dilatation of the ascending aorta
    replaced_by: HP:0004970
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
- **Disease Name:** Turnpenny-Fry Syndrome
- **MONDO ID:** MONDO:0032707 (if available)
- **Causal gene(s):** PCGF2
- **OMIM:** OMIM:618371
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Turnpenny-Fry Syndrome** covering all of the
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

# Turnpenny-Fry Syndrome (TPFS): Disease Characteristics Report

**Scope.** This report covers Turnpenny-Fry syndrome, MONDO:0032707 / OMIM #618371. It is caused by heterozygous missense variants at residue Pro65 of **PCGF2** (polycomb group ring finger 2; HGNC:12929; also called MEL-18; chromosome 17q12).

**Sources and limits.**
- The evidence base is small. It is one case series of 13 patients (PMID 30343942) and about four single-case reports from 2022 to 2025. The 2025 report counts its patient as the 16th known case (PMID 40502890).
- PubMed and NCBI Gene pages could not be fetched directly. Facts were taken from PMC full texts, MedGen, the HGNC REST service, EBI OLS, and web search results.
- Some quotes from non-preapproved pages were capped at about 125 characters. Where a quote is a fragment, it is marked as such.
- Where a PMID could not be verified, the report says so.

---

## 1. Disease Information

**Overview.** MedGen (paraphrasing OMIM) describes TPFS as follows. It is characterized by developmental delay, impaired intellectual development and impaired growth. Facial features include frontal bossing, sparse hair, malar hypoplasia, small palpebral fissures and oral stoma, and dysplastic "satyr" ears. Feeding problems, constipation, and brain, cardiac, vascular and skeletal malformations are also common ([MedGen 1683283](https://www.ncbi.nlm.nih.gov/medgen/1683283)).

The defining paper concludes that "heterozygous substitutions of the Pro65 residue of PCGF2 cause a recognizable syndrome" with distinctive craniofacial, neurological, cardiovascular and skeletal features. This is Turnpenny et al., *Am J Hum Genet* 2018;103(5):786–793, PMID 30343942, DOI 10.1016/j.ajhg.2018.09.012 ([PMC6218713](https://pmc.ncbi.nlm.nih.gov/articles/PMC6218713/)). A correction to the facial-features figure followed in *Am J Hum Genet* 2018;103(6):1054 ([PMC6288271](https://pmc.ncbi.nlm.nih.gov/articles/PMC6288271)).

**Identifiers**

| Resource | ID | Source |
|---|---|---|
| OMIM (disease) | 618371 | MedGen; Qi 2022 |
| OMIM (gene) | 600346 (PCGF2) | HGNC REST |
| MONDO | MONDO:0032707 | MedGen; [EBI OLS](https://www.ebi.ac.uk/ols4/api/search?q=Turnpenny-Fry) |
| Orphanet | ORPHA:688642 | EBI OLS (ORDO IRI) |
| UMLS / MedGen | C5193060 / 1683283 | MedGen |
| ICD-10 / ICD-11 / MeSH | No specific code retrieved. It probably falls under generic "multiple congenital anomalies" codes, but this was not verified. | — |

**Synonyms.** TPFS; "Neurocardioskeletal syndrome" ([MedGen](https://www.ncbi.nlm.nih.gov/medgen/1683283)); "PCGF2-related syndrome" ([PhenomeGene/humandiseasegenes.nl](https://humandiseasegenes.nl/pcgf2)).

**Type of data.** All knowledge comes from aggregated case reports and series of individual patients. There are no registry or EHR cohorts.

## 2. Etiology

- **Causal factor.** The cause is genetic: a heterozygous germline missense variant at PCGF2 Pro65, usually de novo. In the series, "All the mutations affected the same highly conserved proline in PCGF2" (PMID 30343942).
- **Genetic risk factors**
  - Parental mosaicism is a recurrence risk. In the 2018 series, individual 11 inherited the variant from an asymptomatic mother who was mosaic (21% in blood) (PMID 30343942).
  - Qi et al. (2022) found the variant "inherited from a mosaic father" (about 10%) (PMID 36105049, [PMC9452349](https://pmc.ncbi.nlm.nih.gov/articles/PMC9452349/)).
- **Environmental risk factors, protective factors, gene–environment interactions.** None are known, and none have been reported.
- **Modifiers.** None are known.

## 3. Phenotypes

Frequencies come from Turnpenny 2018 (n=13, ages 2–21 years, 7 female and 6 male; PMID 30343942) unless noted otherwise. Onset is congenital or in infancy for all features. Severity is variable, and the course is static and developmental.

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Global developmental delay / intellectual disability (mild to severe) | 13/13 | HP:0001263, HP:0001249 |
| Absent speech | 3/13 | HP:0001344 |
| Broad forehead / frontal bossing | 13/13 | HP:0000337, HP:0002007 |
| Sparse, slow-growing scalp hair (frontal/temporal) | 12/12 | HP:0002209 |
| Periorbital fullness | 12/12 | HP:0000629 |
| Malar hypoplasia | 12/12 | HP:0000272 |
| Dysplastic, small, low-set ears, often satyr configuration | 12/12 | HP:0000377, HP:0000369, HP:0011245 (satyr ear; verify ID) |
| Short/narrow palpebral fissures | 11/12 | HP:0012745, HP:0045025 |
| Prominent nasal tip (older individuals) | 10/13 | HP:0005274 |
| Small oral aperture | 7/12 | HP:0000160 |
| Long face | 7/12 | HP:0000276 |
| Mandibular prognathism | 7/13 | HP:0000303 |
| Facial hypotonia, open mouth, drooling | 3/13 (drooling) | HP:0000297, HP:0002307 |
| Muscular hypotonia | 9/13 | HP:0001252 |
| Conductive hearing impairment | 7/13 | HP:0000405 |
| Seizures | 2/13; one additional adult case (PMID 40502890) | HP:0001250 |
| Birth weight below the mean for gestational age; IUGR in 3 | 13/13 (low); 3/13 (IUGR) | HP:0001518, HP:0001511 |
| Feeding difficulties | 9/13 | HP:0011968 |
| Gastro-oesophageal reflux | 6/13 | HP:0002020 |
| Constipation, sometimes severe | 8/12 | HP:0002019 |
| Short stature (generally low height) | most | HP:0004322 |
| Variable head size: relative macrocephaly in 3, OFC below −2 SD in 4 | 3/13 and 4/13 | HP:0004482, HP:0000252 |
| Patent ductus arteriosus | 5/13 | HP:0001643 |
| Atrial septal defect | 3/13 | HP:0001631 |
| Ascending aortic / aortic root dilatation (one case Z>7 at 21 y) | 5/13 | HP:0005111, HP:0002616 |
| Any cardiac abnormality | 11/13 | HP:0001627 |
| Tortuosity / ectasia of intracranial and extracranial vessels on MRA | 3 of the 3 imaged | HP:0005116 (arterial tortuosity) |
| Polymicrogyria (bilateral or perisylvian) | 4 of the 8 MRIs reviewed | HP:0002126 |
| White-matter signal changes | 8/8 MRIs | HP:0002500 |
| Mild lateral ventriculomegaly | "common" | HP:0006956 |
| Thin corpus callosum; cerebellar vermis hypoplasia | 1 each | HP:0033725, HP:0001320 |
| Kyphosis / scoliosis | 6/13 | HP:0002808, HP:0002650 |
| Pectus deformity | 3/13 | HP:0000766 |
| Vertebral anomalies (L1 hypoplasia, small T3, truncated sacrum) | 3 individuals | HP:0003468 |
| Morgagni-type diaphragmatic hernia | 2/13; one additional case (PMID 38283775) | HP:0000776 |
| Minor digital anomalies | 4/13 | HP:0001155 |

**Other HPO-annotated features** listed in MedGen include dental crowding or malocclusion, high palate, joint hypermobility, numerous nevi, obstructive sleep apnea, ADHD and autistic behavior, recurrent respiratory infections, and polyhydramnios ([MedGen](https://www.ncbi.nlm.nih.gov/medgen/1683283)). PhenomeGene notes haemangiomas in 2 individuals and orchidopexy in 2 males ([PhenomeGene](https://humandiseasegenes.nl/pcgf2/professionals/clinical-characteristics)).

**Quality of life.** No EQ-5D, SF-36 or other quality-of-life instrument data exist. The burden is driven mainly by intellectual disability (some patients are non-verbal into adulthood), feeding problems, and cardiovascular surveillance needs.

## 4. Genetic / Molecular Information

**Gene.** PCGF2, HGNC:12929, "polycomb group ring finger 2".
- Previous symbols: ZNF144, RNF110. Alias: MEL-18.
- Entrez 7703; Ensembl ENSG00000277258; UniProt P35227; OMIM 600346.
- MANE Select transcript: NM_007144.3 / ENST00000620225.5 ([HGNC REST](https://rest.genenames.org/fetch/symbol/PCGF2)).

**Pathogenic variants.** All are germline.

| Variant (NM_007144.2) | Type | Cases | ClinVar |
|---|---|---|---|
| c.194C>T p.(Pro65Leu) | missense, recurrent | 11 unrelated in 2018 series; Qi 2022; Rodrigues 2024 | Variation 619193: Pathogenic / Likely pathogenic ([ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/619193)) |
| c.193C>T p.(Pro65Ser) | missense | monozygotic twins (2018) | — |

**Population frequency and constraint**
- "No variants have been reported at this position in the gnomAD database" (PMID 30343942).
- ExAC pLI is 0.55. Several truncating variants appear in gnomAD, no truncating variants were seen in patients, and DECIPHER lists no interstitial deletions of PCGF2. Together these argue against haploinsufficiency (PMID 30343942).

**Functional consequence.** This has not been demonstrated experimentally.
- Turnpenny et al. propose a dominant-negative effect: "Mutant PCGF2 may have dominant-negative effects, sequestering PRC1 components into complexes" that bind histones poorly (abstract fragment, PMID 30343942).
- Qi et al. ran molecular dynamics and reported "a deleterious effect on the intramolecular structural flexibility and stability of PCGF2 protein" (PMID 36105049). This is computational evidence.

**Somatic or cancer relevance.** One child with TPFS developed T-cell ALL at age 5, with a somatic 5q32~33 deletion and TRA/D (14q11) rearrangement in the leukemic cells. Whether TPFS raises cancer risk is unknown (PMID 38283775, [PMC10822196](https://pmc.ncbi.nlm.nih.gov/articles/PMC10822196/)).

**Modifier genes, chromosomal abnormalities, epigenetic signature.**
- No modifier genes have been reported.
- No causal chromosomal abnormalities are known.
- No DNA-methylation episignature for TPFS was retrieved.

## 5. Environmental Information

No environmental, lifestyle or infectious contributors are known. These categories do not apply to this disease.

## 6. Mechanism / Pathophysiology

**Causal chain** (mostly inferred, from modelling and knowledge of PcG biology):

1. A de novo, or mosaic-parent-transmitted, heterozygous missense variant at PCGF2 Pro65 (P65L or P65S) is present in the germline. *(Demonstrated; PMID 30343942.)*
2. The substitution **leads to** destabilization of the N-terminal RING-adjacent loop. Pro65 sits at a loop-to-α-helix junction. FoldX ΔΔG is +8.6 kcal/mol for P65L and +3.9 kcal/mol for P65S. *(Computational, modelled on BMI1–RING1B structures 2h0d and 4r8p; PMID 30343942. MD simulation also supports it; PMID 36105049.)*
3. The altered loop **results in** perturbed contact between the basic patch at Lys62/Arg64 and the acidic patch of histones H3/H4 on the nucleosome. *(Inferred.)* The paper states: "Computer structural modeling suggests the substitutions alter an N-terminal loop of PCGF2 critical for histone biding [sic]" (PMID 30343942).
4. Mutant PCGF2 probably still assembles into canonical PRC1 with RING1A/B, CBX and PHC. This **leads to** a dominant-negative sequestration of PRC1 components into complexes that engage chromatin poorly. *(Hypothesis; PMID 30343942.)*
5. Impaired cPRC1.2 function **results in** misregulated Polycomb-target developmental genes. The evidence for this step is indirect:
   - Canonical PRC1 is recruited via CBX recognition of H3K27me3 and represses targets ([review, PMC7585675](https://pmc.ncbi.nlm.nih.gov/articles/PMC7585675)).
   - In mouse ESCs, Pcgf2 loss, "though not affecting the global level of H2AK119ub1, disrupts these cPRC1.2 loops in ESCs and impairs the transcriptional induction of crucial target genes necessary for neuronal differentiation" (Hanafiah et al., bioRxiv 2024, PMID 39605346, [PMC11601310](https://pmc.ncbi.nlm.nih.gov/articles/PMC11601310/); later published in *EMBO Rep*).
   - This step is *inferred* for the missense variants.
6. The defect branches into several downstream effects:
   - **6a. Hox / axial patterning**: vertebral anomalies, kyphoscoliosis, and sternal or pectus defects. Mel18-null mice show posterior homeotic transformations with ectopic Hox expression (Akasaka et al., *Development* 1996;122:1513–1522; PMID not verified).
   - **6b. Neural development**: ID, polymicrogyria and white-matter changes. The authors speculatively invoke disturbed PI3K–AKT signalling and PCGF2–CCND2 regulation (PMID 30343942).
   - **6c. Cardiac mesoderm and vascular development**: PDA, ASD, aortic dilatation and vessel tortuosity. PCGF2 regulates cardiac mesoderm differentiation, but the link is *inferred* (PMID 30343942).
   - **6d. Growth**: pre- and postnatal growth impairment. Mel18-null mice show "strong growth retardation" (Akasaka 1996).
7. Together these **result in** the clinical syndrome, with variable expressivity.

**Checklist**
- **Pathways.** Polycomb-mediated repression, H3K27me3 reading, and H2AK119 monoubiquitination (Reactome "PRC1/PRC2 Polycomb" pathways); a speculative PI3K-AKT link.
- **Immune involvement.** Mel18- and Bmi1-deficient mice show severe combined immunodeficiency from lymphoid cell death and impaired IL-7 responsiveness (Akasaka et al., *Development* 2001;128:1587; PMID not verified). This has not been reported in patients.
- **Metabolic changes and omics.** No metabolomic, proteomic or patient-derived transcriptomic data exist.

**Suggested GO terms**
- GO:0031519 PcG protein complex
- GO:0035102 PRC1 complex
- GO:0045814 negative regulation of gene expression, epigenetic
- GO:0009952 anterior/posterior pattern specification
- GO:0048704 embryonic skeletal system morphogenesis
- GO:0007420 brain development
- GO:0007507 heart development
- GO:0031491 nucleosome binding

**Suggested CL terms**
- CL:0002322 embryonic stem cell
- CL:0000047 neuronal stem cell
- CL:0000134 mesenchymal stem cell (paraxial mesoderm derivatives)
- CL:0000513 cardiac muscle myoblast

## 7. Anatomical Structures Affected

- **Primary systems**: central nervous system, craniofacial, cardiovascular, skeletal, gastrointestinal (feeding, reflux, constipation) and auditory.
- **UBERON terms**: brain UBERON:0000955, cerebral cortex UBERON:0000956, cerebral white matter UBERON:0002437, face UBERON:0001456, external ear UBERON:0001691, ductus arteriosus UBERON:0003129, atrial septum UBERON:0002085, ascending aorta UBERON:0001496, vertebral column UBERON:0001130, diaphragm UBERON:0001103, scalp hair UBERON:0010166.
- **Secondary effects**: aortic root dilatation progressing into adulthood, and conductive hearing loss.
- **Subcellular**: nucleus GO:0005634 and chromatin GO:0000785.
- **Laterality**: polymicrogyria was bilateral (perisylvian or extensive).

## 8. Temporal Development

- **Onset**: congenital, with prenatal low growth, IUGR in some, and polyhydramnios in one (PMID 38283775). The disorder presents in infancy as hypotonia, feeding difficulties and developmental delay.
- **Course**: a lifelong static neurodevelopmental disorder. The facial gestalt evolves with age, with prominent nasal tip and prognathism appearing in older individuals. Aortic dilatation may progress: one patient had a 4.7 cm aortic root at 21 years.
- **Adult follow-up**: one 35-year-old woman with severe ID had epilepsy from age 5. She became seizure-free on valproate plus lamotrigine (PMID 40502890).
- **Remission**: none.
- **Critical periods**: early developmental intervention, and cardiac surveillance throughout life.

## 9. Inheritance and Population

- **Inheritance**: autosomal dominant. Nearly all cases are de novo, and parental somatic/germline mosaicism is documented twice (PMIDs 30343942, 36105049).
- **Penetrance**: appears complete for constitutional heterozygotes. Mosaic parents were asymptomatic, or their status was not described.
- **Expressivity**: variable. ID ranges from mild to severe, and head size ranges from microcephaly to relative macrocephaly.
- **Anticipation, founder effects, consanguinity, carrier frequency**: none apply or have been reported.
- **Prevalence**: unknown. Only about 16 cases have been reported worldwide (PMID 40502890).
- **Geography**: cases have been reported from the UK/Europe (DDD and others), Australia, Turkey (Ercoskun et al., *Am J Med Genet A* 2022;188:688–691, PMID 34750959), China (PMID 36105049), Portugal (PMID 38283775) and Venezuela/USA (PMID 40502890).
- **Sex ratio**: 7 female to 6 male in the original series.

## 10. Diagnostics

- **Genetic testing is the diagnostic method.** No biochemical test exists.
  - Exome or genome sequencing identified most cases: DDD trio exomes, clinical exome (PMID 38283775), and WES (PMIDs 34750959, 36105049, 40502890).
  - Targeted Sanger sequencing of PCGF2 exon/codon 65 was used once after clinical recognition (PMID 30343942). It is also useful for testing parents, and the mosaicism cases mean deep or sensitive methods are worthwhile.
- **CMA and karyotype**: not diagnostic, because no deletions cause the syndrome.
- **Imaging**
  - Brain MRI: polymicrogyria, white-matter changes, ventriculomegaly.
  - MRA: vascular tortuosity and ectasia.
  - Echocardiography: PDA, ASD, aortic dilatation. The authors recommend periodic echocardiographic surveillance for all patients (PMID 30343942).
  - Spinal radiographs.
  - Audiology.
  - EEG if seizures occur.
- **Clinical criteria**: no formal criteria exist. The diagnosis is suggested by the gestalt of frontal bossing, sparse hair, periorbital fullness, malar hypoplasia and satyr ears.
- **Differential diagnosis**: this was not systematically addressed in the retrieved sources. Reasonable considerations include other chromatin-regulator syndromes, connective-tissue aortopathies (because of aortic dilatation and tortuosity) and polymicrogyria syndromes, but these are not source-verified.
- **Screening**: no newborn or carrier screening exists. Prenatal or preimplantation testing can be offered to families with a known variant or mosaic parent (PMID 36105049).

## 11. Outcome / Prognosis

- **Survival**: no mortality data are available. Patients aged 21 and 35 years have been reported, so survival into adulthood occurs (PMIDs 30343942, 40502890).
- **Morbidity**: lifelong ID, with some patients non-verbal; feeding problems; conductive hearing loss; aortic dilatation; occasional epilepsy; possible malignancy (one case of T-ALL).
- **T-ALL outcome**: the child received Alltogether-1 chemotherapy and was in maintenance with a favorable response at 18 months (PMID 38283775).
- **Prognostic factors and biomarkers**: none are known. The main serious risk under surveillance is aortic root dilatation, although no aneurysms or dissections have been reported.

## 12. Treatment

There is no disease-specific therapy. No clinical trials were found, and there are no gene, RNA or cell therapies.

| Intervention | Evidence | Suggested NCIT term |
|---|---|---|
| Multidisciplinary developmental therapy (physical, occupational, speech) | standard care, implied in reports | Physical Therapy C16996 (verify), Speech Therapy C17069 (verify) |
| Feeding support and reflux/constipation management | case series | Nutritional Support (verify ID) |
| Echocardiographic surveillance; cardiology management of aortic dilatation; PDA/ASD repair when indicated | PMID 30343942 | Echocardiography C16525 (verify) |
| Antiseizure medication (valproic acid, lamotrigine) | single case, seizure-free (PMID 40502890) | Valproic Acid C914; Lamotrigine C47585 (verify) |
| Hearing aids for conductive loss | inferred | — |
| Orchidopexy; diaphragmatic hernia repair | PhenomeGene; case reports | — |
| Chemotherapy for intercurrent T-ALL (Alltogether-1) | PMID 38283775 | — |

Pharmacogenomics is not applicable.

## 13. Prevention

- **Primary prevention**: not possible for de novo events. Genetic counselling should include the recurrence risk from parental mosaicism, testing parents (ideally with sensitive methods), and offering prenatal or preimplantation diagnosis (PMID 36105049).
- **Tertiary prevention**: cardiac and aortic surveillance (PMID 30343942), audiology, spinal monitoring, and oncology vigilance (PMID 38283775 urges "comorbidity surveillance").
- **Vaccination, public-health or environmental measures**: not applicable.

## 14. Other Species / Natural Disease

- **Natural disease**: no naturally occurring animal disease was found in OMIA, based on searches only.
- **Orthologs**: mouse *Pcgf2* (MGI:99161, synonyms Mel18 and Zfp144; [IMPC](https://www.mousephenotype.org/data/genes/MGI:99161)). The Drosophila Polycomb-group homolog Posterior sex combs (Psc), whose loss causes homeotic misexpression, was cited in the 2018 paper.
- **Conservation**: Pro65 is highly conserved across PCGF paralogs and species (PMID 30343942).
- **Zoonotic potential**: not applicable.

## 15. Model Organisms

- **Mel18 (Pcgf2) knockout mouse** (Akasaka et al., *Development* 1996;122(5):1513–1522; PMID not verified)
  - The mice survive to birth, show strong growth retardation, and die around 4 weeks of age.
  - They show posterior transformations of the axial skeleton tied to ectopic Hox expression in paraxial mesoderm.
  - Heterozygotes are normal, and homozygotes lack craniofacial or neurological abnormalities (as summarized in PMID 30343942).
  - **Recapitulation**: partial. The model reproduces growth failure and axial-skeletal patterning defects. It does not reproduce the facial gestalt, ID, polymicrogyria or cardiac defects. This fits the view that a null allele does not model a dominant-negative missense allele.
- **Mel18/Bmi1 double knockout** (Akasaka et al., *Development* 2001;128:1587; PMID not verified): shows synergistic, dose-dependent Hox repression and severe combined immunodeficiency.
- **IMPC Pcgf2 knockout**: significant phenotypes in mortality/aging, reproductive, skeleton and endocrine/exocrine systems, with 6 significant phenotypes. The individual terms could not be retrieved.
- **Cellular model**: CRISPR Pcgf2-knockout mouse ESCs show loss of cPRC1.2-mediated chromatin loops and impaired neuronal-differentiation gene induction (PMID 39605346).
- **Gaps**: no P65L or P65S knock-in mouse, zebrafish or patient-iPSC model was found. Such a model is the key missing experiment for testing the dominant-negative hypothesis.
- **Resources**: MGI, IMPC, MMRRC/IMSR.

---

## Key Evidence Summary

| PMID | Type | Key point |
|---|---|---|
| 30343942 | Human case series (n=13) plus structural modelling | Defines TPFS; Pro65 de novo missense variants; dominant-negative hypothesis |
| 34750959 | Case report (Turkey) | 14th case, diagnosed by WES ([PubMed](https://www.pubmed.gov/34750959/)); abstract not retrieved |
| 36105049 | Case report plus MD simulation (China) | P65L inherited from a mosaic father (about 10%) |
| 38283775 | Case report (Portugal) | First TPFS patient with malignancy (T-ALL) |
| 40502890 | Case report (USA/Venezuela) | Adult with epilepsy; good response to valproate plus lamotrigine |
| 39605346 | In vitro (mouse ESC) | Pcgf2 loss disrupts cPRC1.2 loops and impairs neuronal gene induction |

**Main uncertainties**
- The mechanism has not been tested in a wet lab.
- Prevalence, natural history beyond about 35 years, and cancer risk are unknown.
- The PMIDs for the Akasaka 1996 and 2001 mouse papers, and the ICD and MeSH codes, could not be verified in this session.

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 5 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 13 |
| On topic | 4 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:30343942` *(abstract only)*: "No variants have been reported at this position in the gnomAD database"
  - Text part not found as substring: 'No variants have been reported at this position in the gnomAD database' (note: only abstract available for PMID:30343942, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 76 |
| Resolved | 72 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 9 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0032707` (2 mentions) - the report calls it "MONDO"; MONDO calls it **turnpenny-fry syndrome**
- `HP:0001250` (1 mention) - the report calls it "2/13; one additional adult case (PMID 40502890)"; HP calls it **Seizure**
- `HP:0004322` (1 mention) - the report calls it "most"; HP calls it **Short stature**
- `HP:0002126` (1 mention) - the report calls it "4 of the 8 MRIs reviewed"; HP calls it **Polymicrogyria**
- `HP:0002500` (1 mention) - the report calls it "8/8 MRIs"; HP calls it **Abnormal cerebral white matter morphology**
- `HP:0006956` (1 mention) - the report calls it "common"; HP calls it **Lateral ventricle dilatation**
- `HP:0003468` (1 mention) - the report calls it "3 individuals"; HP calls it **Abnormal vertebral morphology**
- `HP:0000776` (1 mention) - the report calls it "2/13; one additional case (PMID 38283775)"; HP calls it **Congenital diaphragmatic hernia**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0005111` (obsolete Dilatation of the ascending aorta) (1 mention) - replaced by `HP:0004970`

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.
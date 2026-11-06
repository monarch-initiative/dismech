---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-01T07:50:36.837549'
end_time: '2026-11-01T07:53:29.679423'
duration_seconds: 172.84
template_file: templates/disease_pathophysiology_research.md
template_sha: f452f0a9c7e3536175154b9683c45663f686f283
template_variables:
  disease_name: Intellectual Developmental Disorder With Speech Delay And Axonal Peripheral
    Neuropathy
  mondo_id: MONDO:0030849
  category: Mendelian
  causal_genes: NEMF
  omim_id: OMIM:619099
  synonyms: IDDSAPN
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
  web_search_requests: 5
  num_turns: 22
  total_cost_usd: 2.5099844000000004
  session_id: 3cf25424-9b1f-5b79-afff-26bf20e1bed1
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 16
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 7
  off_topic: 1
  off_topic_references:
  - PMID:19196966
  needs_review: true
  validator_version: 0.4.0
term_validation:
  total_terms: 48
  verified: 46
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 2
  mislabelled_terms:
  - term_id: MONDO:0030849
    reported_labels:
    - MONDO
    ontology_label: intellectual developmental disorder with speech delay and axonal
      peripheral neuropathy
  - term_id: GO:1990112
    reported_labels:
    - GO cellular component:** the RQC complex term
    ontology_label: RQC complex
  labels_variant: 1
  unresolvable_prefixes:
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Developmental Disorder With Speech Delay And Axonal Peripheral Neuropathy
- **MONDO ID:** MONDO:0030849 (if available)
- **Causal gene(s):** NEMF
- **OMIM:** OMIM:619099
- **Synonyms:** IDDSAPN
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Intellectual Developmental Disorder With Speech Delay And Axonal Peripheral Neuropathy** covering all of the
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

I'm reading the cached abstracts for the five NEMF papers before I write the report.

The report draft is nearly ready. I'm checking the last few ontology labels against the local caches.

# Intellectual Developmental Disorder With Speech Delay And Axonal Peripheral Neuropathy (IDDSAPN): research report

**Disease:** IDDSAPN · **MONDO:0030849** · **OMIM:619099** · **Causal gene: *NEMF*** (nuclear export mediator factor; hgnc:10663; gene OMIM 608378; chromosome 14q22) · Mendelian, autosomal recessive

## How this report was sourced

- **Read directly (full abstract or full text) from the repository's `references_cache/`:** PMID:32934225 (Martin et al. 2020), PMID:33048237 (Ahmed et al. 2021), PMID:33909987 (Thrun et al. 2021), PMID:35452614 (Filbeck et al. 2022) and PMID:38819420 (Panda et al. 2024). These five are the papers the existing KB entry cites. Every quote below comes from these files.
- **Taken from web search summaries only:** two later mouse papers, PMID:39312574 (Plessis-Belair et al. 2024) and PMID:40377023 (Aging Cell 2025), plus the curation summaries from GenCC, PanelApp, MalaCards and LOVD. **I did not quote any of these.** Fetch them with `just fetch-reference` before they are used as evidence.
- **Recalled, not checked:** PMID:19196966 (Chu et al. 2009, the *Ltn1* mouse) and PMID:25554787 (Shen et al. 2015, CAT tails). Both are marked "unverified" where they appear.
- **Ontology terms:** labels marked ✓ were checked against `cache/<prefix>/terms.csv` in this repository. Anything not marked ✓ is a lead to look up, not a binding to copy.

---

## 1. Disease information

IDDSAPN is a very rare autosomal recessive neurodevelopmental and neuromuscular disorder caused by **biallelic loss-of-function variants in *NEMF***. NEMF is the human Rqc2/RqcH protein of the ribosome-associated quality control (RQC) pathway.

Onset is in infancy or early childhood. The core features are:
- global developmental delay or intellectual disability, usually mild;
- marked speech delay;
- motor delay;
- a length-dependent axonal (motor or sensorimotor) peripheral neuropathy, often with distal atrophy, ataxia, scoliosis or kyphosis, and foot and hand deformities.

The original description is in Martin et al. 2020. Its abstract (PMID:32934225) reports *"NEMF mutations expected to interfere with function in patients from seven families presenting juvenile neuromuscular disease."* The discussion adds: *"patients with NEMF variants can additionally manifest intellectual disability, most notably speech delay."*

**Identifiers:**

| System | Identifier |
|---|---|
| MONDO | MONDO:0030849 |
| OMIM (disease) | 619099 |
| OMIM (gene) | 608378 |
| UMLS | C5436813 (from the DrugMap record) |
| MedGen | 1754849 (from the DrugMap record) |
| HGNC | hgnc:10663 ✓ |
| Orphanet, ICD-10, ICD-11, MeSH | None specific found. The disease would fall under generic intellectual-disability or hereditary-neuropathy codes. |

**Synonyms:** IDDSAPN; NEMF-related neurodevelopmental disorder with axonal neuropathy. "NEMF-related disorder" is an informal label.

**Basis of the information:** all of it comes from individual patient case series. There are about 26 patients from 14 families across 3–4 reports, and no registry or EHR data.

## 2. Etiology

- **Cause:** biallelic germline *NEMF* variants. These are mostly nonsense, frameshift or canonical splice-site variants, plus a few missense variants. Ahmed et al. (PMID:33048237): *"disease-causing biallelic NEMF variants result in central nervous system impairment and other variable features."*
- **Genetic risk:** consanguinity is common in the reported families (Syrian, Turkish, Persian, Saudi Arabian, Pakistani/Chinese-collaboration and Indian kindreds).
- **Possible dominant allele:** one heterozygous de novo missense variant, p.Ile553Thr, was found in a patient whose neuropathy began at age 17. Martin et al. wrote that this *"may suggest potential dominant-negative impacts from variants in NEMF."* GenCC and PanelApp both rate the monoallelic evidence as weak.
- **Environmental triggers:** none established. Panda et al. (PMID:38819420), summarising the earlier reports, note that in one family *"the affected siblings showed episodic deterioration after stress or injury."* This rests on a single anecdotal observation.
- **Protective factors and gene–environment interactions:** none reported.

## 3. Phenotypes

The most useful frequency source is Panda et al. 2024, Table 1, which pools the published cases (n=26, 14 kindreds).

| Phenotype | Frequency (n=26) | Suggested HPO term |
|---|---|---|
| Delayed motor milestones | 25 (96%) | HP:0001270 Motor delay ✓ |
| Intellectual disability (mostly mild) | 25 (96%) | HP:0001249 Intellectual disability ✓; HP:0001263 Global developmental delay ✓ |
| Speech delay | 23 (88%) | HP:0000750 Delayed speech and language development ✓ |
| Ataxia / unsteady gait | 16 (61%) | HP:0001251 Ataxia ✓; HP:0002317 Unsteady gait ✓ |
| Axonal neuropathy (motor or sensorimotor) | 14 (53%); not assessed in many | HP:0003477 Peripheral axonal neuropathy ✓; HP:0007002 Motor axonal neuropathy ✓; HP:0007141 Sensorimotor neuropathy ✓ |
| Distal muscle atrophy | 14 (53%) | HP:0003693 Distal amyotrophy ✓ |
| Hypotonia | 13 (50%) | HP:0001252 Hypotonia ✓ |
| Abnormal neuroimaging (cerebral or cerebellar atrophy in one kindred) | 9 (34%) | HP:0002120 Cerebral cortical atrophy ✓; HP:0001272 Cerebellar atrophy ✓ |
| Dysarthria | 7 (27%) | HP:0001260 Dysarthria ✓ |
| Kyphosis / scoliosis | 7 (27%) | HP:0002650 Scoliosis ✓ |
| Hyporeflexia or areflexia | frequent (no count) | HP:0001284 Areflexia ✓; HP:0002522 Areflexia of lower limbs ✓ |
| Foot drop, equinovarus, toe clawing | some cases | HP:0009027 Foot dorsiflexor weakness ✓; HP:0001762 Talipes equinovarus ✓ |
| Adducted thumbs, contractures, pectus excavatum | AUS1 proband | HP:0001371 Flexion contracture ✓; HP:0000767 Pectus excavatum ✓ |
| Tremor | 2/9 (Martin) | HP:0001337 Tremor ✓ |
| Respiratory distress | 1/9 (Martin) | HP:0002093 Respiratory insufficiency ✓ |
| Autistic features, ADHD | few | HP:0000729 Autistic behavior ✓; HP:0007018 Attention deficit hyperactivity disorder ✓ |
| Preaxial polydactyly, squint, abnormal smooth pursuit or saccades, valgus knees | rare (single kindreds) | look up |

**Key quotes (PMID:38819420):**
- Course: *"Most patients demonstrate progressive distal muscle weakness, lower limb atrophy, foot drop, hyporeflexia, and deformities of the foot or hand, secondary to peripheral neuropathy."*
- Walking: *"Affected patients often learn to walk independently between 3 and 4 years of age, but might have an ataxic or unsteady gait."*

**Onset:** 1–2 years of age in all biallelic cases (Martin Table 1). The heterozygous de novo case began at 17 years.

**Severity:** variable, ranging from mild ID with mild hypotonia (USA2) to spastic paraplegia with severe orthopaedic deformity (AUS1).

**Quality of life:** no formal measures have been published. The burden comes from motor disability (wheelchair use in one kindred), orthopaedic surgery and communication impairment.

## 4. Genetic and molecular information

**Gene:** *NEMF* (hgnc:10663). The protein is about 1,076 amino acids (UniProt O60524; worth confirming). Its domains are NFACT-N, a helix–hairpin–helix, a coiled-coil, a middle domain, NFACT-R and NFACT-C.

> **Error in a cited source:** Panda et al. state *"NEMF … encodes a 362-amino acid protein."* This is inconsistent with the NEMF domain architecture and should not be propagated. Treat that sentence as an error in the source.

**Reported variants** (transcript NM_004713.6 where given):

| Variant | Zygosity | Family | Source |
|---|---|---|---|
| c.2608C>T p.(Arg870\*) | homozygous | AUS1 | PMID:32934225 |
| c.2014A>T p.(Lys672\*) | homozygous | DEU1 (Turkish) | PMID:32934225 |
| c.2451delA p.(Ser817fs\*7) | homozygous | IRN1 | PMID:32934225 |
| c.2871_2875dupTGTAG p.(Asp959fs\*2) | homozygous | SAU1 | PMID:32934225 |
| c.2011C>T p.(Arg671\*) + de novo c.1A>T p.(Met1?) | phase unknown | USA1 | PMID:32934225 |
| c.980G>A p.Arg327Gln + c.2777C>T p.Pro926Leu (maternal, in cis) / c.2768delA p.Lys923Argfs\*27 (paternal) | compound heterozygous | USA2 | PMID:32934225 |
| c.1658T>C p.(Ile553Thr), de novo | heterozygous | USA3 | PMID:32934225 |
| c.2618del (frameshift); LOD 4.5 | homozygous | large consanguineous family | PMID:33048237 |
| c.574+1G>T, c.807-2A>C (splice) | homozygous | GeneMatcher families | PMID:33048237 |
| c.1234_1235insC (frameshift) | homozygous | GeneMatcher family | PMID:33048237 |
| c.507-2A>T (intron 5 acceptor) | homozygous | Indian infant | PMID:38819420 |

- **Classification:** Martin et al. classify the biallelic variants as pathogenic or likely pathogenic under ACMG. The p.Ile553Thr variant *"is absent from gnomAD"* (CADD 28). ClinVar entries were not checked.
- **Variant class and mechanism:** mainly LoF (PTC, splice). The functional consequence is LOSS_OF_FUNCTION; dominant-negative is possible only for p.Ile553Thr.
- **Origin:** germline. No somatic, mosaic or chromosomal-abnormality cases. No modifier genes or epigenetic data. Panda et al. say *"Future research is likely to identify potential modifier genes."*
- **Gene–disease validity:** GenCC lists a **Strong** classification (evaluated 2023-10-04, submitted 2025). PanelApp (Genomics England and Australia) lists NEMF as green, high evidence, for intellectual disability. This is not a ClinGen CGGV record, so it should not be copied into `gene_disease_validity` as `CLINGEN` without the source record.

## 5. Environmental information

There are no known toxic, lifestyle or infectious factors. The single report of deterioration after stress or injury (§2) is the only environmental observation.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic *NEMF* loss-of-function variants** (nonsense, frameshift, splice) cause loss of NEMF protein. Absence of protein is *inferred* from the PTC/NMD nature of the variants. It is *demonstrated* only for the mouse *Nemf* D106\* allele, where western blot showed no protein.
2. **Loss of NEMF** impairs **ribosome-associated quality control**. NEMF normally senses 60S subunits that are still blocked by a peptidyl-tRNA after ribosome splitting. It also stabilises binding of the E3 ligase LTN1/Listerin.
   - Filbeck et al. (PMID:35452614): *"In canonical eukaryotic RQC, NEMF stabilizes the LTN1/Listerin E3 ligase binding to obstructed ribosomal subunits for nascent-chain ubiquitylation."*
3. **Loss of C-terminal alanine tailing** (Ala tails in mammals; CAT tails in yeast). In mammals this has an additional, Listerin-independent role.
   - Thrun et al. (PMID:33909987): *"mammalian NEMF has an additional, Listerin-independent proteolytic role, which, as in bacteria, is mediated by tRNA-Ala binding and Ala tailing."*
   - Ala tails act as C-degrons for CRL2^KLHDC10 and Pirh2/RCHY1.
   - Mouse disease alleles: R86S sits in the NFACT-N domain *"in the vicinity of the universally conserved, catalytic residues D96 and R97."* The equivalent mutations in yeast Rqc2 *"selectively interfere with its ability to modify aberrant translation products with C-terminal tails"* (PMID:32934225).
4. **Failed ubiquitylation and proteasomal clearance of stalled nascent chains.** Stalling products accumulate, and 60S subunits may be sequestered from translation. This step is *inferred in vivo* and shown with in vitro reporters.
5. **Branch (emerging, mouse only):** *Nemf* mutant neurons show an **importin-β-specific nuclear import defect**. Nuclear loss and cytoplasmic gain of NEMF, importin-β and TDP-43, plus collapse of the Ran gradient, are reported (PMID:39312574). A 2025 follow-up reports G1/S cell-cycle re-entry or arrest in motor neurons (PMID:40377023). Whether this is downstream of the RQC defect or a separate NEMF function is **unresolved**. Both papers are known from search summaries only.
6. **Neuronal development defect** (CNS branch): *Nemf* knockdown *"leads to impairment of axonal outgrowth and synapse development in cultured mouse primary cortical neurons"* (PMID:33048237; IN_VITRO). This plausibly underlies the ID and speech delay, but that link is *inferred*.
7. **Progressive motor (and sensory) axon degeneration** (PNS branch). In mice, distal and proximal motor axons are lost, followed by **neuromuscular junction denervation** and **neurogenic muscle atrophy** (PMID:32934225; MODEL_ORGANISM).
8. **Clinical manifestations:** length-dependent axonal neuropathy, distal amyotrophy, foot drop and deformities, areflexia, ataxia, and scoliosis (secondary). Together with the CNS branch, these give ID, speech delay and motor delay.

### Supporting detail

- **GO process terms:** GO:0072344 rescue of stalled cytosolic ribosome ✓; GO:0140708 CAT tailing ✓; GO:1990116 ribosome-associated ubiquitin-dependent protein catabolic process ✓; GO:0006515 protein quality control for misfolded or incompletely synthesized proteins ✓; GO:0006606 protein import into nucleus ✓ (emerging branch); GO:0031175 neuron projection development ✓; GO:0050808 synapse organization ✓.
- **GO cellular component:** the RQC complex term (GO:1990112) is not in the local cache, so look it up before using it. Other compartments are the cytosolic large ribosomal subunit and the nucleus.
- **Cell types:** CL:0000100 motor neuron ✓; CL:0000540 neuron ✓; cortical excitatory neurons (look up a specific CL term). Panda et al. report enriched NEMF expression in excitatory neurons.
- **Pathway context:** a related ribosome-rescue disorder is *GTPBP2* Jaberi–Elahi syndrome (cited in Martin et al.). *Ltn1* mutant mice develop motor neuron degeneration (Chu et al. 2009, PMID:19196966, unverified).
- **Mechanisms not involved:** no immune, metabolic or epigenetic mechanism is described.
- **Omics:** Ahmed et al. used RNA-seq (MeSH tag only; details not in the abstract). No single-cell, spatial, proteomic or metabolomic studies were found.

## 7. Anatomical structures affected

- **Peripheral nerve:** UBERON:0001021 nerve ✓. Lower limbs are affected more than upper limbs.
- **Spinal cord:** UBERON:0002240 spinal cord ✓ (motor neurons and ventral roots in mice).
- **Brain:** UBERON:0000955 brain ✓ and UBERON:0002037 cerebellum ✓ (atrophy in one kindred).
- **Skeletal muscle:** affected secondarily.
- **Spine:** scoliosis and kyphosis.
- **Laterality:** bilateral and symmetric.
- **Subcellular:** cytosolic ribosomes; nucleus and cytoplasm (nuclear transport branch).

## 8. Temporal development

- **Onset:** infancy to early childhood (1–2 years). Onset is insidious.
- **Walking:** independent walking at about 3–4 years.
- **Course:** neuromuscular weakness is often progressive. In one kindred it led to loss of ambulation. Episodic deterioration was seen in another. The ID appears static.
- **Not available:** formal stages, remission data or natural-history studies.
- **Hypothetical intervention window:** early childhood, before axonal loss. In mice, axon counts were normal at 2 weeks, so the process is degenerative rather than developmental.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive (HP:0000007 ✓). A possible dominant-negative allele has been seen once.
- **Penetrance and expressivity:** penetrance appears complete in biallelic carriers. Expressivity is variable between and within families.
- **Not reported:** anticipation and germline mosaicism.
- **Prevalence:** unknown. About 26 cases in 14 kindreds have been published (`CASES_IN_LITERATURE`).
- **Sex ratio:** 17 of 26 male (65%), most likely ascertainment bias.
- **Populations:** Middle Eastern, Turkish, Iranian, Saudi, European/US, Chinese-collaboration and Indian kindreds. No founder variant is known. Carrier frequency has not been estimated (gnomAD not queried).

## 10. Diagnostics

- **Genetic testing:** exome or genome sequencing is the diagnostic route in every published case (WGS in AUS1 and IRN1; ES elsewhere). *NEMF* appears on ID and hereditary-neuropathy panels (PanelApp).
- **Electrophysiology:** NCS shows axonal motor–sensory polyneuropathy with reduced CMAP amplitudes and preserved latency and velocity. Panda et al.: *"Nerve conduction study showed bilateral lower limb-predominant motor–sensory axonal polyneuropathy."* Sural SNAPs were absent.
- **Laboratory tests:** creatine kinase is normal. Metabolic screening is negative.
- **MRI:** usually normal. Cerebral or cerebellar atrophy appears in a minority.
- **Differential diagnosis:** SMA (SMN testing negative), congenital muscular dystrophy, Andermann syndrome (*SLC12A6*), Arts syndrome (*PRPS1*), *TECPR2*-HSAN with ID, *MCM3AP*-related neuropathy, IMNEPD (*PTRH2*), *GTPBP2* Jaberi–Elahi syndrome, and axonal CMT2 genes.
- **Not available:** biomarkers, clinical criteria, newborn screening and omics-based diagnostics.

## 11. Outcome and prognosis

- **Life expectancy:** no deaths reported in humans. Published patients range in age up to 28 years.
- **Morbidity:** progressive motor disability, orthopaedic deformities that need surgery (equinovarus correction in AUS1), wheelchair dependence in one kindred, and communication impairment.
- **Not available:** survival data, QoL measures or prognostic biomarkers.

## 12. Treatment

No disease-specific therapy exists, and no trials were found on ClinicalTrials.gov. Management is supportive:

- **Physiotherapy:** NCIT:C15302 Physical Therapy.
- **Occupational therapy.** In Panda et al.: *"The child was initiated on physiotherapy and occupational therapy."*
- **Speech and language therapy.**
- **Orthotics** for foot drop.
- **Orthopaedic surgery** for foot deformity and scoliosis: NCIT:C16186 Orthopedic Surgical Procedure.
- **Genetic counselling:** NCIT:C15240 Genetic Counseling.
- **Overall approach:** rehabilitation (NCIT:C15315) and supportive care (NCIT:C15747).

The NCIT codes are taken from the repository's CLAUDE.md list. Re-validate them with `just validate-terms`.

**Speculative approaches:** LoF gene replacement (AAV) is hypothetical. No pharmacogenomics data exist.

## 13. Prevention

- Genetic counselling for a 25% recurrence risk.
- Carrier testing of relatives.
- Prenatal or preimplantation diagnosis once the familial variants are known.
- Tertiary prevention through orthopaedic surveillance (spine X-rays, as in Panda et al.) and physiotherapy to limit contractures.
- No primary prevention, vaccination or population screening applies.

## 14. Other species and natural disease

- No naturally occurring animal disease was found (OMIA not searched in depth).
- NEMF is conserved from bacteria to humans: RqcH in *B. subtilis*, Rqc2 in *S. cerevisiae*, Caliban in *Drosophila*.
- Martin et al.: residues *"specifically implicated in the C-terminal tailing modification are strictly conserved."*

## 15. Model organisms

**Mouse (*Mus musculus*; PMID:32934225; MODEL_ORGANISM):**

| Allele | Origin | Phenotype |
|---|---|---|
| *Nemf* R86S | ENU; JAX #19392 | Waddling gait by 2 weeks, growth failure, median survival 20 days, motor and sensory axon loss, NMJ denervation |
| *Nemf* R487G | ENU; JAX #18870 | Milder; abnormal gait and hindlimb wasting by 10 weeks, median survival 601 days |
| *Nemf* D106\* | CRISPR null; JAX #34815 | Severe early wasting, cannot right itself by day 11, reduced SpO2 |

- **Recapitulation:** RECAPITULATES progressive motor axon degeneration and neurogenic atrophy. Martin et al.: *"three independently-generated mouse models with mutations in a different component of the RQC complex, NEMF/Rqc2, develop progressive motor neuron degeneration."*
- **Limitations:**
  - Mouse severity (death at 20 days for R86S; early death for the null) far exceeds the human disease.
  - The ENU alleles are missense hypomorphs, not the human PTC alleles.
  - No cognitive or speech phenotype was assessed, so the ID and speech features are not modelled.
  - *"no motor or sensory peripheral degeneration has been observed in our heterozygous mouse models at one and a half years of age"*. Because of this, the dominant-negative hypothesis remains untested in mice.

**Other models:**
- **Yeast:** Rqc2 R88S/K534G (IN_VITRO-style biochemistry) show a selective CATylation defect.
- **Mammalian cells:** HeLa/RPE1 NEMF knockouts (PMID:33909987); mouse primary cortical neuron knockdown (PMID:33048237).
- **Not found:** zebrafish, *Drosophila* disease models, and patient iPSC models.

---

## Gaps and leads for curation

- **To fetch:** PMID:39312574 and PMID:40377023 before citing the nuclear-import branch. Also confirm Chu et al. 2009 (Ltn1 mouse) and Shen et al. 2015 (CAT tails).
- **Not searched:** ClinVar, gnomAD carrier frequency, OMIA, and a GeneReviews chapter. Run `just check-genereviews` to check for a chapter; none was found.
- **Unresolved hypothesis:** whether the importin-β transport defect lies downstream of RQC failure or reflects an independent NEMF function. This is a good `mechanistic_hypotheses` or `KNOWLEDGE_GAP` candidate.
- **Model mismatch:** no model reproduces the cognitive or speech phenotype. This is a candidate `HUMAN_MODEL_MISMATCH` discussion.

## Sources

- Martin PB et al. *Nat Commun* 2020. PMID:32934225 — [PubMed](https://pubmed.ncbi.nlm.nih.gov/32934225/)
- Ahmed A et al. *Hum Genet* 2021. PMID:33048237
- Thrun A et al. *Mol Cell* 2021. PMID:33909987
- Filbeck S et al. *Mol Cell* 2022. PMID:35452614
- Panda PK et al. *Ann Indian Acad Neurol* 2024. PMID:38819420
- Plessis-Belair J et al. *PLoS Genet* 2024. PMID:39312574 — [PMC11449308](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11449308/) · [bioRxiv](https://www.biorxiv.org/content/10.1101/2024.02.14.580338.full.pdf) · [Stony Brook record](https://researchconnect.stonybrook.edu/en/publications/nemf-mutations-in-mice-illustrate-how-importin-%CE%B2-specific-nuclear/)
- Nuclear import defects and cell-cycle dysregulation, *Aging Cell* 2025. PMID:40377023 — [PMC12341789](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12341789/)
- Curation and summary resources: [GenCC submission](https://thegencc.org/submissions/SGC-104232.2) · [GenCC NEMF](https://thegencc.org/genes/HGNC:10663) · [PanelApp England](https://panelapp.genomicsengland.co.uk/panels/285/gene/NEMF/) · [PanelApp Australia](https://panelapp-aus.org/panels/250/gene/NEMF/) · [VCGS PanelApp](https://panelapp-test.vcgs.org.au/panels/3070/gene/NEMF/) · [MalaCards](https://www.malacards.org/card/intellectual_developmental_disorder_with_speech_delay_and_axonal_peripheral_neuropathy) · [LOVD](https://databases.lovd.nl/shared/diseases/05918) · [DrugMap](https://drugmap.idrblab.net/data/disease/details/DISPZZJY) · [Wikipedia NEMF](https://en.wikipedia.org/wiki/NEMF_(gene)) · [Centogene](https://centogene.com/resources/scientific-publications/expanding-the-genetics-of-impaired-neurodevelopment) · [Scripps press release](https://www.scripps.edu/news-and-events/press-room/2020/20200916-joazeiro-neuron-diseases.html)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 7 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:19196966` (2 mentions) - Oncogenic EGFR signaling cooperates with loss of tumor suppressor gene functions in gliomagenesis.
  - shared terms: gene

Weighed against this report's own most characteristic terms: `nemf`, `motor`, `martin`, `panda`, `speech`, `variant`, `found`, `axonal`, `disease`, `neuropathy`, `atrophy`, `gene`, `kindred`, `biallelic`, `patient`, `panelapp`, `genetic`, `peripheral`, `progressive`, `rqc`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 46 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 2 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0030849` (2 mentions) - the report calls it "MONDO"; MONDO calls it **intellectual developmental disorder with speech delay and axonal peripheral neuropathy**
- `GO:1990112` (1 mention) - the report calls it "GO cellular component:** the RQC complex term"; GO calls it **RQC complex**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCIT:C15315` (1 mention) - the report calls it "Overall approach:** rehabilitation"; NCIT calls it **Rehabilitation**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

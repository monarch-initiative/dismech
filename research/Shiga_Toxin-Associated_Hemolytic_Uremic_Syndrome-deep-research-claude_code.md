---
provider: claude_code
model: claude-haiku-5-5, claude-opus-4-8, claude-opus-5-5
cached: false
start_time: '2026-10-28T14:11:07.249307'
end_time: '2026-10-28T14:15:12.613300'
duration_seconds: 245.36
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Shiga Toxin-Associated Hemolytic Uremic Syndrome
  mondo_id: MONDO:0019536
  category: Infectious Disease
  causal_genes: not recorded
  omim_id: not recorded
  synonyms: STEC-HUS; typical hemolytic uremic syndrome; diarrhea-associated hemolytic
    uremic syndrome
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
  - claude-opus-4-8
  - claude-opus-5-5
  web_search_requests: 5
  num_turns: 17
  total_cost_usd: 3.8146883
  session_id: 6bfbcc68-e2fe-5f88-ba6b-c04d7866873f
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 3
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 15
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 6
  validator_version: 0.4.0
term_validation:
  total_terms: 51
  verified: 51
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 10
  labels_matching: 6
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0030213
    reported_labels:
    - a major determinant of acute mortality
    ontology_label: Emotional dearth
  - term_id: UBERON:0001155
    reported_labels:
    - hemorrhagic colitis
    ontology_label: colon
  - term_id: UBERON:0000955
    reported_labels:
    - "cerebral microvasculature \u2014 CNS TMA"
    ontology_label: brain
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Shiga Toxin-Associated Hemolytic Uremic Syndrome
- **MONDO ID:** MONDO:0019536 (if available)
- **Causal gene(s):** not recorded
- **OMIM:** not recorded
- **Synonyms:** STEC-HUS; typical hemolytic uremic syndrome; diarrhea-associated hemolytic uremic syndrome
- **Category:** Infectious Disease

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Shiga Toxin-Associated Hemolytic Uremic Syndrome** covering all of the
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

There's an existing entry. Let me see which PMIDs it already cites, as verified anchors.

This is an infectious disease entry, not a gene-based one — the causal agent is Shiga toxin-producing *Escherichia coli* (STEC), chiefly O157:H7, via the Shiga toxins Stx1/Stx2. Let me gather current primary literature.

I have enough to produce the report. Writing it now.

---

# Research Report: Shiga Toxin–Associated Hemolytic Uremic Syndrome (STEC-HUS)

**MONDO:0019536 · Category: Infectious Disease**

> **Note on "causal gene."** This disease has no human causal gene. It is an **acquired, toxin-mediated infectious disease**. The initiating cause is infection by **Shiga toxin–producing *Escherichia coli* (STEC/EHEC)** — classically serotype **O157:H7**, with rising non-O157 serogroups (O26, O80, O104, O111, O145) — whose virulence is driven by the **Shiga toxins Stx1 and Stx2**, encoded on lambdoid prophages in the *bacterial* genome (`stx1`, `stx2` genes). The relevant "molecular actors" in the human host are the toxin receptor **globotriaosylceramide (Gb3/CD77)** and the complement/coagulation machinery it engages; rare host complement variants act only as severity *modifiers*, not causes. STEC-HUS must be distinguished from atypical/complement-mediated HUS (aHUS, MONDO-separate) and from TTP (ADAMTS13 deficiency).

---

## 1. Disease Information

STEC-HUS is a **thrombotic microangiopathy (TMA)** defined by the classic triad of **microangiopathic hemolytic anemia** (Coombs-negative, with schistocytes), **thrombocytopenia**, and **acute kidney injury**, arising typically 5–10 days after an episode of (often bloody) diarrhea caused by STEC. It is the prototypical **"typical" / diarrhea-associated (D+) HUS** and is the leading cause of acute kidney injury in young children.

**Identifiers / synonyms:** MONDO:0019536. Synonyms: STEC-HUS; typical HUS; diarrhea-positive (D+) HUS; diarrhea-associated HUS; "classic" HUS; (historically) post-diarrheal HUS. ICD-10 **D59.3** (hemolytic-uremic syndrome); MeSH **D006463** (Hemolytic-Uremic Syndrome). No OMIM entry (acquired disease).

**Information source:** derived chiefly from **aggregated disease-level resources** — surveillance networks (US CDC FoodNet), national pediatric registries (Polish, Italian, French), and clinical cohorts — rather than single-patient EHR data.

---

## 2. Etiology

**Primary cause (infectious):** ingestion of **STEC** producing Shiga toxin(s). Transmission is fecal-oral via contaminated **undercooked ground beef, unpasteurized milk/juice, contaminated produce (leafy greens, sprouts), petting-zoo/farm-animal contact, recreational/drinking water**, and person-to-person spread. **Cattle are the principal reservoir** (asymptomatic carriage). Infectious dose is very low (~10–100 organisms).

**Required virulence determinant:** the **Shiga toxins** (Stx1 and/or Stx2). **Stx2 — particularly subtypes Stx2a — is strongly associated with progression to HUS**, whereas Stx1-only strains more often cause uncomplicated diarrhea. Additional STEC virulence factors: the **LEE pathogenicity island** encoding **intimin (*eae*)** and the type III secretion system that mediates attaching-and-effacing (A/E) lesions on gut epithelium.

**Risk factors:**
- *Host-demographic:* **age < 5 years** (highest risk), extremes of age, bloody diarrhea, elevated WBC, fever.
- *Iatrogenic:* **antibiotic exposure during STEC colitis** (especially bactericidal/fluoroquinolone/β-lactam agents may induce the SOS response and increase phage-mediated Stx release) and **antimotility agents** — both associated with increased HUS risk.
- *Microbial:* **Stx2-producing strains, O157:H7**, strains carrying *stx2a* + *eae*.
- *Genetic modifiers (not causal):* rare variants in **complement regulatory genes** (`CFH`, `CD46/MCP`, `CFI`, `C3`) are reported in a subset with severe/atypical course and may worsen outcome; **Gb3 synthase (`A4GALT`) expression** levels on host endothelium modulate susceptibility.

**Protective factors:** adequate **cooking of meat, pasteurization, hand hygiene, safe water**; these are environmental/public-health, not molecular. No well-established protective genetic allele. **Avoiding antibiotics and antimotility agents** during suspected STEC colitis is protective against HUS progression.

**Gene–environment interaction:** the pathogenic outcome is set by the STEC *stx2* genotype (environmental/microbial) interacting with host **Gb3 tissue distribution** and **complement regulatory reserve** — the same toxin dose produces disparate outcomes depending on host endothelial Gb3 density and complement-regulation capacity.

---

## 3. Phenotypes (with suggested HPO terms)

**Prodrome / GI (preceding):**
- **Diarrhea**, frequently **bloody (hemorrhagic colitis)** — HP:0002014 (Diarrhea), HP:0025085 (Bloody diarrhea); abdominal pain HP:0002027; vomiting HP:0002013.

**Core triad:**
- **Microangiopathic hemolytic anemia** — HP:0001937 (Microangiopathic hemolytic anemia); schistocytes on smear; HP:0001878 (Hemolytic anemia).
- **Thrombocytopenia** — HP:0001873.
- **Acute kidney injury** — HP:0001919; oliguria/anuria HP:0100519; often requiring dialysis.

**Renal / laboratory:**
- Hematuria HP:0000790, proteinuria HP:0000093, elevated creatinine HP:0003259; hypertension HP:0000822; elevated LDH, low haptoglobin, negative direct Coombs.

**Extrarenal (severity markers):**
- **CNS involvement** (~20–25% of severe cases): seizures HP:0001250, encephalopathy HP:0001298, stroke HP:0001297, altered consciousness HP:0030213 — a major determinant of acute mortality.
- **Pancreatic:** hyperglycemia/pancreatitis HP:0001954, HP:0012090.
- **Cardiac** (rare): HP:0001635; **colonic** complications: intussusception, necrosis, perforation.

**Phenotype characteristics:** **acute onset**, predominantly **pediatric (<5 yr)**; **severe but usually self-limited** acute phase; **monophasic** course (vs relapsing aHUS). HUS develops in roughly **5–15% of STEC O157 infections**, higher in young children. Quality-of-life impact is driven by the minority with **CKD/hypertension/proteinuria sequelae** at long-term follow-up.

---

## 4. Genetic / Molecular Information

**No human causal gene.** The operative genetics are **bacterial**: `stx1`, `stx2` (and subtypes stx2a–stx2g) carried on **lambdoid prophages**; `eae` (intimin), *ehxA* (enterohemolysin), LEE locus.

**Host molecular determinants:**
- **`A4GALT`** — encodes Gb3/CD77 synthase; Gb3 is the obligate Stx receptor. Tissue-specific Gb3 expression (high on human **renal glomerular endothelium and podocytes**, cerebral endothelium) explains organ tropism.
- **Complement modifier genes** (`CFH`, `CD46`, `CFI`, `C3`, `CFB`) — rare variants reported in severe STEC-HUS; **modifiers of severity, not disease cause**.

No ACMG-classified pathogenic germline variants define the disease; it is **not inherited**, has no Mendelian inheritance pattern, no penetrance/expressivity/anticipation, and no founder effect. Allele-frequency/somatic-vs-germline sections are **not applicable**. Epigenetic/chromosomal abnormalities: not applicable.

---

## 5. Environmental Information

- **Infectious agent:** *Escherichia coli* (STEC/EHEC) — **NCBITaxon:562** (*E. coli*); O157:H7 lineage. Shiga toxin as the effector (CHEBI/ontology: Shiga toxin is a protein, not a small molecule).
- **Vehicles/exposures:** undercooked beef, unpasteurized dairy, contaminated produce and water, animal/farm contact; large foodborne outbreaks (e.g., the 2011 German **O104:H4** sprout outbreak).
- **Lifestyle/iatrogenic:** antibiotic and antimotility use during STEC colitis (risk-increasing).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **Ingestion of STEC** → colonization of the colon; **intimin-mediated attaching-and-effacing lesions** on colonic epithelium → **hemorrhagic colitis** (bloody diarrhea).
2. **Local Shiga toxin production** by phage-borne *stx* genes → toxin translocates across the gut epithelium into the circulation (transcellular/paracellular; leukocyte- and possibly extracellular-vesicle–associated carriage). *Mechanism of systemic delivery partly inferred.*
3. **Toxin (AB₅ holotoxin) binds Gb3/CD77** on the surface of **Gb3-rich target cells** — chiefly human **renal glomerular microvascular endothelium and podocytes**, and cerebral endothelium. *(Receptor = globotriaosylceramide; GO: receptor binding.)*
4. **Retrograde intracellular transport:** endocytosis → Golgi → endoplasmic reticulum; the **A-subunit is cleaved (furin) and reduced**, releasing the **A1 fragment into the cytosol**.
5. **A1 fragment acts as an RNA N-glycosidase** → **depurinates a single adenine in the 28S rRNA of the 60S ribosomal subunit** → **halts protein synthesis** → cell injury. *(This is the canonical demonstrated enzymatic lesion.)*
6. **Branch A — ribotoxic stress response:** ribosomal damage activates **p38 and JNK MAPK** signaling → **apoptosis** and pro-inflammatory cytokine/chemokine induction (IL-8, IL-6, TNF). *(Demonstrated in intestinal epithelial and endothelial cells.)*
7. **Branch B — endothelial activation (sublethal toxin):** at sublethal doses Stx **reprograms endothelial gene expression** rather than killing → **NF-κB activation** → upregulated adhesion molecules, chemokines, **tissue factor**, and **P-selectin** → loss of thromboresistance → **prothrombogenic endothelium**.
8. **Complement amplification:** Stx2 **binds complement factor H**, impairing regulation, and **induces P-selectin**, which activates **C3 via the alternative pathway** on the endothelial surface → local complement deposition amplifies injury and platelet-thrombus formation. *(Mechanistic link established in vitro; drives the eculizumab rationale.)*
9. **von Willebrand factor axis:** Stx promotes endothelial secretion of **ultra-large VWF multimers** and impairs their ADAMTS13 cleavage → platelet capture → **microvascular platelet-fibrin thrombi**.
10. **Microvascular thrombosis + mechanical RBC shearing** across occluded/fibrin-laden capillaries → **schistocytes, intravascular hemolysis** (↑LDH, ↓haptoglobin) and **platelet consumption (thrombocytopenia)**.
11. **Glomerular TMA** → endothelial swelling, capillary occlusion, podocyte injury → **acute kidney injury** (oliguria/anuria). Extrarenal Gb3-rich beds (brain, pancreas) → **CNS and pancreatic complications**.

### Supporting detail
- **Molecular pathways:** NF-κB; p38/JNK MAPK (ribotoxic stress); alternative complement pathway; VWF–ADAMTS13; coagulation (tissue factor).
- **Cellular processes:** inhibition of translation; apoptosis (GO:0006915); inflammation; endothelial activation; platelet aggregation; thrombosis (GO:0007596 — blood coagulation).
- **Protein dysfunction:** Stx A-subunit RNA N-glycosidase activity (enzymatic, not host-protein misfolding).
- **Cell types (CL):** glomerular endothelial cell (CL:1001005 / CL:0002262 endothelial cell of vascular tree), **podocyte (CL:0000653)**, platelet (CL:0000233), colonic epithelial cell (CL:0011108), monocyte/macrophage (CL:0000235).
- **Immune involvement:** innate inflammatory cytokine storm; complement activation; neutrophil-mediated endothelial injury (Stx bound to neutrophils).
- **Tissue damage mechanisms:** ischemia from microvascular occlusion, apoptosis, oxidative/inflammatory injury, fibrin deposition.

---

## 7. Anatomical Structures Affected (UBERON)

- **Primary organ: kidney** — UBERON:0002113; specifically the **renal glomerulus** (UBERON:0000074) and its **microvascular endothelium**; podocytes. Renal cortex.
- **GI tract (initiating site): colon** — UBERON:0001155 (hemorrhagic colitis).
- **Secondary/extrarenal:** **brain** UBERON:0000955 (cerebral microvasculature — CNS TMA), **pancreas** UBERON:0001264, occasionally **heart** UBERON:0000948.
- **Body systems:** **urinary/renal, hematologic/vascular, gastrointestinal, nervous**.
- **Tissue/cell level:** vascular endothelium (microvascular), glomerular visceral epithelium (podocytes); subcellular — Stx trafficks through **endosome → Golgi (GO:0005794) → ER (GO:0005783) → cytosol/ribosome (GO:0005840)**.
- **Localization:** **bilateral** renal involvement.

---

## 8. Temporal Development

- **Onset:** **acute**, predominantly **pediatric**; HUS emerges **~5–13 days after onset of diarrhea** (median ~1 week), often as diarrhea begins to resolve.
- **Progression:** acute phase over days to a few weeks; **monophasic/self-limited** in most. Oligoanuric AKI may require dialysis for days–weeks.
- **Course pattern:** typically **non-relapsing** (unlike aHUS). Critical intervention window = early **supportive/volume management during the colitis prodrome**, before full TMA.
- **Duration/remission:** most children **recover kidney function** within weeks (treatment-/supportive-care-associated), but a minority progress to **chronic kidney disease**; long-term renal sequelae (hypertension, proteinuria, reduced GFR) reported in ~**25–30%** at ≥5-year follow-up.

---

## 9. Inheritance and Population Epidemiology

- **Inheritance:** **none** — acquired infectious disease (no AD/AR/X-linked pattern; penetrance/expressivity/consanguinity/carrier-frequency sections **not applicable**).
- **Epidemiology (children):**
  - Pediatric STEC-HUS incidence varies by country/surveillance: e.g. **~0.5 per 100,000 children/year**; Polish registry **mean ~3.9 per million** age-related population (rising over 2012–2023); French data: **>4 cases/100,000 in children <3 yr**.
  - **~5–15% of STEC O157 infections** progress to HUS; FoodNet reported **~6.3%** of O157 infections and **15.3%** of HUS among children <5 yr.
- **Mortality / outcome:** **low in modern cohorts — ~2–4% case fatality** (Polish registry 2% for STEC-HUS; Italian network 3.4% STEC-HUS vs 8.3% aHUS; US FoodNet ~3% in <5 yr with HUS). Older surveillance: 3–5% death, 10–30% long-term renal dysfunction.
- **Demographics:** highest in **young children (1–2 yr highest for non-O157 O26/O80; O157 across childhood)**; summer/warm-season peak; **geographic variation** in serogroups (O157 historically dominant in North America/UK; O80/O26 rising in Europe; O104:H4 in the 2011 German outbreak affected mostly adults).
- **Sex:** roughly equal, slight female predominance reported in some series.

---

## 10. Diagnostics

- **Clinical/laboratory triad:** microangiopathic hemolytic anemia (**schistocytes**, ↑LDH, ↓haptoglobin, negative direct Coombs), **thrombocytopenia**, and **acute kidney injury** (↑creatinine). Supportive: hematuria, proteinuria.
- **Microbiologic confirmation of STEC:** stool testing — **PCR for *stx1/stx2* genes** (most sensitive; combined with culture raises detection to ~70%), **Shiga toxin immunoassay (EIA)**, and **stool culture on sorbitol-MacConkey agar** (O157 is sorbitol-nonfermenting; misses non-O157 and sorbitol-fermenting O157). **Send stool/rectal swab early** — absence of STEC in stool does **not** exclude STEC-HUS (toxin may clear by the time HUS presents). **Serology (anti-O157 LPS antibodies)** aids diagnosis when stool is negative.
- **Imaging / other:** renal ultrasound (nonspecific); neuroimaging (MRI) if CNS involvement.
- **Essential differential diagnosis:** **aHUS/complement-mediated HUS** (no diarrhea prodrome, relapsing, complement variants) and **TTP** (severe **ADAMTS13 <10%** activity). Distinguishing STEC-HUS from aHUS/TTP is critical because management differs (STEC-HUS = supportive; aHUS = eculizumab; TTP = plasma exchange). LOINC-codable: stool Shiga toxin EIA, *stx* PCR, ADAMTS13 activity, schistocyte count, LDH, haptoglobin, platelet count, creatinine.
- **Genetic/omics testing:** complement gene panel only when aHUS is suspected (negative STEC workup, atypical/relapsing course).
- **Screening:** public-health STEC surveillance and outbreak investigation; no individual genetic screening applicable.

---

## 11. Outcome / Prognosis

- **Survival:** acute case fatality **~2–4%** (modern pediatric cohorts); death driven mainly by **severe CNS involvement** or multi-organ failure.
- **Recovery:** majority of children **recover kidney function**; acute dialysis common but usually temporary.
- **Long-term morbidity:** **~25–30% of survivors** have renal sequelae at ≥5 yr (hypertension, proteinuria, reduced GFR, CKD); a small fraction progress to ESKD.
- **Prognostic factors (poor):** **early anuria / prolonged dialysis**, high peak WBC, **CNS involvement**, **Stx2 (vs Stx1) genotype**, young age, need for dialysis >2–3 weeks. These predict chronic kidney outcomes.

---

## 12. Treatment (with suggested NCIT terms)

**Mainstay = supportive care; there is no approved antitoxin.**
- **Supportive care** (NCIT:C15747 Supportive Care): careful **IV volume expansion/early isotonic fluids** (NCIT:C15317 Fluid Therapy — early hydration during colitis may be renoprotective), electrolyte and acid-base management, **blood pressure control**, transfusion of packed RBCs for anemia (NCIT:C15280 Blood Transfusion; platelet transfusion generally avoided unless bleeding/procedure).
- **Renal replacement therapy** (NCIT:C15431? — **Dialysis**, NCIT:C15248): hemodialysis/peritoneal dialysis/CKRT for oligoanuric AKI.
- **AVOID:** **antibiotics** (NCIT:C254 Antibiotic) in confirmed/suspected STEC — no proven benefit, possible increased HUS risk (especially bactericidal agents); **antimotility agents**; **NSAIDs**.
- **Plasma exchange** (NCIT:C50111 Plasmapheresis/Therapeutic Plasma Exchange): **not routinely beneficial** in children (reserved, controversially, for severe neurologic disease or adults in outbreak settings).
- **Eculizumab** (NCIT:C64762 Eculizumab; complement C5 inhibitor; **monoclonal antibody**, NCIT:C20401): **controversial and not standard**. A **randomized placebo-controlled trial (100 children)** showed **no benefit** on acute dialysis need, hematologic course, or extrarenal manifestations; systematic review found no definite medium/long-term benefit. Some centers reserve it empirically for **severe CNS involvement**, acknowledging weak evidence.
- **Experimental / investigational:** Stx-neutralizing agents, **Shiga toxin receptor analogs/binders**, anti-Stx monoclonal antibodies, and complement-pathway agents — remain investigational (ClinicalTrials.gov).
- **Pharmacogenomics:** not applicable.

---

## 13. Prevention

- **Primary prevention (public health, dominant):** **thorough cooking of ground beef**, **pasteurization** of milk/juice, **produce and water safety**, **hand hygiene**, exclusion of cases from food handling/childcare, careful **farm/petting-zoo hygiene**. Vector/reservoir control (cattle). NCIT:C15417? Health Education / Hygiene.
- **Secondary prevention:** **early recognition of STEC colitis and early IV hydration**, and **avoidance of antibiotics/antimotility agents** to reduce HUS progression; close hematologic/renal monitoring of children with bloody diarrhea.
- **Tertiary prevention:** BP control and nephroprotection (ACE inhibition) and long-term renal surveillance in survivors to limit CKD progression.
- **Immunization:** **no licensed human vaccine**; STEC/Stx and cattle vaccines are investigational.
- **Counseling/genetic screening:** not applicable (non-genetic).

---

## 14. Other Species / Natural Disease

- **Reservoir:** **cattle (*Bos taurus*, NCBITaxon:9913)** and other ruminants carry STEC asymptomatically in the gut — the principal zoonotic source. Deer, sheep, goats also carry STEC.
- **Natural disease / comparative biology:** classic HUS-like renal TMA is **largely human-specific** because **Gb3 distribution differs by species** — human glomerular endothelium is Gb3-rich, whereas mice express Gb3 mostly extraglomerularly, so animals rarely develop the full human renal phenotype naturally.
- **Zoonotic potential:** **high** — STEC is a foodborne/zoonotic pathogen; animals are carriers rather than HUS patients.

---

## 15. Model Organisms

- **Mouse models** (NCBITaxon:10090): purified Stx injection, STEC gavage, and **streptomycin-treated oral infection** models; reproduce systemic toxicity, renal injury and neurologic signs **but incompletely recapitulate human glomerular TMA** due to different Gb3 tissue distribution. Widely used for toxin trafficking, complement, and therapeutic testing.
- **Rabbit, baboon/non-human primate, piglet (gnotobiotic/neonatal)** models reproduce aspects of gut colonization, systemic Stx effects, and CNS/renal injury (piglet neurologic model notable).
- **In vitro:** **human glomerular microvascular endothelial cells, podocytes, HUVEC, intestinal epithelial (Caco-2/HCT-8), THP-1 macrophages**, and **kidney organoids** — the most faithful systems for the human Gb3-dependent endothelial/podocyte mechanism.
- **Limitations:** species Gb3 differences; most models require supraphysiologic toxin doses; natural monophasic human course hard to model.
- **Resources:** MGI; ATCC/Cellosaurus (cell lines); published organoid protocols.

---

## Key Citations (verify PMIDs with `just fetch-reference` before KB use)

- **MDPI *Toxins* (2020) — "Shiga Toxin-Associated Hemolytic Uremic Syndrome: A Narrative Review"** — [mdpi.com/2072-6651/12/2/67](https://www.mdpi.com/2072-6651/12/2/67) (comprehensive mechanism/clinical review).
- **"Shiga toxin-associated hemolytic uremic syndrome: pathophysiology of endothelial dysfunction"** — [PubMed 20424866](https://pubmed.ncbi.nlm.nih.gov/20424866/).
- **Shiga Toxin Classification, Structure, and Function (ASM, EHEC-0024-2013)** — [PMC4270005](https://pmc.ncbi.nlm.nih.gov/articles/PMC4270005/) (A-subunit RNA N-glycosidase, retrograde transport).
- **Ribotoxic stress response (p38/JNK, apoptosis), *Infect Immun* 2003** — [journals.asm.org/doi/10.1128/iai.71.3.1497-1504.2003](https://journals.asm.org/doi/10.1128/iai.71.3.1497-1504.2003).
- **Stx–VWF–ADAMTS13, *Blood* 2005** — [ashpublications.org/blood/article/106/13/4199](https://ashpublications.org/blood/article/106/13/4199/133277/).
- **Shiga toxin targets the podocyte via endothelial complement activation** — [PMC7617617](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617617/) *(PMID not confirmed — browser block; verify before citing)*.
- **New insights into Stx-mediated endothelial dysfunction, *Virulence* 2013** — [tandfonline.com/doi/full/10.4161/viru.26143](https://www.tandfonline.com/doi/full/10.4161/viru.26143).
- **HUS and death in E. coli O157:H7 infection, FoodNet 2000–2006, *CID* 2009** — [PubMed 19827953](https://pubmed.ncbi.nlm.nih.gov/19827953/).
- **Incidence, risk factors, outcome in children** — [PMC7385025](https://pmc.ncbi.nlm.nih.gov/articles/PMC7385025/).
- **Polish Pediatric HUS Registry prospective cohort (2024)** — [PMC11546500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11546500/).
- **Sporadic pediatric STEC-HUS, France 2012–2021, *Emerg Infect Dis* 2023** — [wwwnc.cdc.gov/eid/article/29/10/23-0382_article](https://wwwnc.cdc.gov/eid/article/29/10/23-0382_article).
- **Eculizumab / supportive-care management review (2025)** — [Frontiers Pharmacol 2025.1535407](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1535407/full).
- **UK Kidney Association — HUS clinician information** — [ukkidney.org/rare-renal](https://www.ukkidney.org/rare-renal/clinician-information/haemolytic-uraemic-syndrome).

**Evidence-type note for KB population:** mechanistic claims (steps 3–9) are predominantly **IN_VITRO**/**MODEL_ORGANISM**; epidemiology and outcome claims are **HUMAN_CLINICAL** (registry/surveillance); eculizumab-ineffectiveness is **HUMAN_CLINICAL** (RCT). A dismech entry for this disease already exists (`kb/disorders/Shiga_Toxin-Associated_Hemolytic_Uremic_Syndrome.yaml`); reconcile against it and verify every PMID/exact snippet with `just fetch-reference` and `just count-verified-snippets` before curating.

**Sources:**
- [MDPI Toxins narrative review](https://www.mdpi.com/2072-6651/12/2/67)
- [Endothelial dysfunction pathophysiology (PubMed 20424866)](https://pubmed.ncbi.nlm.nih.gov/20424866/)
- [Shiga Toxin structure/function PMC4270005](https://pmc.ncbi.nlm.nih.gov/articles/PMC4270005/)
- [Ribotoxic stress response, Infect Immun 2003](https://journals.asm.org/doi/10.1128/iai.71.3.1497-1504.2003)
- [Stx/VWF/ADAMTS13, Blood 2005](https://ashpublications.org/blood/article/106/13/4199/133277/Hemolytic-uremic-syndrome-associated-Shiga-toxins)
- [Podocyte/complement PMC7617617](https://pmc.ncbi.nlm.nih.gov/articles/PMC7617617/)
- [Virulence 2013 endothelial dysfunction](https://www.tandfonline.com/doi/full/10.4161/viru.26143)
- [FoodNet HUS/death CID (PubMed 19827953)](https://pubmed.ncbi.nlm.nih.gov/19827953/)
- [Incidence/risk/outcome children PMC7385025](https://pmc.ncbi.nlm.nih.gov/articles/PMC7385025/)
- [Polish Pediatric HUS Registry PMC11546500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11546500/)
- [France 2012–2021 EID 2023](https://wwwnc.cdc.gov/eid/article/29/10/23-0382_article)
- [Frontiers Pharmacology 2025 management](https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1535407/full)
- [UK Kidney Association HUS](https://www.ukkidney.org/rare-renal/clinician-information/haemolytic-uraemic-syndrome)
- [EHEC diagnosis/management overview](https://ecgwaves.com/articles/ehec-infection-diagnosis-hus-risk-and-management)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 51 |
| Resolved | 51 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 10 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0030213` (1 mention) - the report calls it "a major determinant of acute mortality"; HP calls it **Emotional dearth**
- `UBERON:0001155` (1 mention) - the report calls it "hemorrhagic colitis"; UBERON calls it **colon**
- `UBERON:0000955` (1 mention) - the report calls it "cerebral microvasculature — CNS TMA"; UBERON calls it **brain**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `NCBITaxon:10090` (1 mention) - the report calls it "Mouse models"; NCBITaxon calls it **Mus musculus**, and lists "house mouse" among its other names
---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-24T17:21:46.645882'
end_time: '2026-09-24T17:26:32.228857'
duration_seconds: 285.58
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Microphthalmia Coloboma 13
  mondo_id: MONDO:0975809
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
  web_search_requests: 14
  num_turns: 16
  total_cost_usd: 1.4250230000000002
  session_id: fd65d8eb-852b-5a9d-91de-140beff025e2
  stop_reason: end_turn
  assistant_text_blocks: 3
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderBillingError
  status_code: 402
  remedy: the account is out of credits
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 16
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 4
  validator_version: 0.3.0rc1
term_validation:
  total_terms: 41
  verified: 34
  not_found: 1
  obsolete: 1
  unverifiable: 5
  confabulation_rate: 0.028
  labels_checked: 14
  labels_matching: 6
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0975809
    reported_labels:
    - MONDO
    - Disease
    ontology_label: microphthalmia/coloboma 13
  - term_id: HP:0000568
    reported_labels:
    - Microphthalmia (uni- or bilateral, asymmetric severity)
    ontology_label: Microphthalmia
  - term_id: HP:0000518
    reported_labels:
    - Nuclear/congenital cataract
    ontology_label: Cataract
  - term_id: UBERON:0001789
    reported_labels:
    - optic nerve
    ontology_label: outer nuclear layer of retina
  - term_id: UBERON:0001786
    reported_labels:
    - optic disc
    ontology_label: fovea centralis
  labels_variant: 3
  unresolved_terms:
  - UBERON:0000384
  obsolete_terms:
  - term_id: GO:0007228
    ontology_label: obsolete positive regulation of hh target transcription factor
      activity
    replaced_by: GO:0007224
  unresolvable_prefixes:
  - Taxon
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microphthalmia Coloboma 13
- **MONDO ID:** MONDO:0975809 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Microphthalmia Coloboma 13** covering all of the
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

I'll research this disorder now using web search.

Good — HPO terms confirmed. I now have sufficient sourced material to write the full report.

I have comprehensive, well-sourced material now. Here is the full research report.

---

# Microphthalmia/Coloboma 13 (MCOPCB13) — Comprehensive Research Report

**MONDO ID:** MONDO:0975809 | **OMIM:** [#620968](https://omim.org/entry/620968) | **Category:** Mendelian, autosomal recessive | **Report date:** September 2026

---

## 1. Disease Information

**Overview.** Microphthalmia/Coloboma 13 (MCOPCB13) is a recently delineated (2023), autosomal recessive, non-syndromic member of the microphthalmia–anophthalmia–coloboma (MAC) spectrum of congenital ocular malformations. It is caused not by a coding mutation in a classical eye-development transcription factor but by a **homozygous single-nucleotide variant within a long-range enhancer ("i8") that normally drives *Indian hedgehog* (*IHH*) expression in the developing eye**. The enhancer happens to sit inside an intron of the neighboring, functionally unrelated gene *NHEJ1* (non-homologous end-joining factor 1) on chromosome 2q35 — the variant is a *cis*-regulatory lesion of *IHH*, not a loss-of-function allele of *NHEJ1* itself (Wormser et al., 2023, PMID:[37580330](https://pubmed.ncbi.nlm.nih.gov/37580330/)).

The disorder was described in two consanguineous families of **Jewish Iranian (Mashhad) ancestry**, an historically isolated, highly inbred community with a previously noted elevated rate of isolated MAC.

**Key identifiers:**
| Resource | ID |
|---|---|
| OMIM phenotype | #620968 (MICROPHTHALMIA/COLOBOMA 13; MCOPCB13) |
| OMIM gene/locus | *NHEJ1* enhancer region, chr2q35 (NHEJ1 gene itself: OMIM *611290) |
| MONDO | MONDO:0975809 |
| Causal gene (regulated, not the enhancer's host) | *IHH* — HGNC:5384, OMIM *600726 |
| Host gene of the enhancer | *NHEJ1* — HGNC:25737, OMIM *611290 |
| Suggested MONDO/parent grouping | Microphthalmia, isolated, with coloboma (MCOPCB phenotypic series, OMIM PS251600) |
| HPO parent phenotype terms | HP:0000568 Microphthalmia; HP:0000589 Coloboma; HP:0000528 Anophthalmia; HP:0000588 Coloboma of the optic nerve |

**Synonyms/alternative names:** MCOPCB13; NHEJ1-intronic *IHH*-enhancer-associated microphthalmia/anophthalmia/coloboma; "MAC13" (informal). No ICD-10/ICD-11 code specific to this molecular subtype exists — it would fall under the general **Q11.2** (microphthalmos)/**Q13.0** (coloboma of iris) parent codes.

**Evidence provenance.** All disease-specific information in this report derives from a single aggregated-cohort genetic/functional study (2 pedigrees, n=25 family members, 7 genotyped affecteds) rather than from large-scale EHR data, registries, or population-level aggregation. This is early-stage, single-family-cluster Mendelian disease characterization — not yet independently replicated in an unrelated population as of this writing.

---

## 2. Etiology

**Disease-causal factor:** A single identified **homozygous intronic regulatory variant** — NHEJ1 (NM_024782.2):c.588+18131A>G [alternatively NG_007880.1:g.37317A>G] — located within the conserved core motif "GGGTGA" of the *IHH* enhancer i8 (Will et al. 2017 nomenclature), at chr2:~220.15 Mb (GRCh37), within the shared 2q35 locus. This falls squarely under the **genetic/mechanistic** causal category — there is no reported environmental or infectious contribution.

**Genetic risk factors:**
- **Causal variant:** Homozygosity for the i8 enhancer A>G substitution.
- **phyloP** = extraordinarily conserved (p = 1.4 × 10⁻⁶); **CADD** = 18.68; **MutationTaster** = disease-causing (100% probability); no predicted splicing effect.
- **Linkage:** Maximal multipoint LOD score of 6.82 at marker rs6753739; shared homozygous haplotype of ~0.5 Mb between rs6436102 and rs746233 in all 7 affected individuals across both pedigrees — consistent with a single **founder variant** in this community.
- **Population frequency:** Absent from gnomAD and from 87 ethnically matched Iranian-Jewish controls, supporting rarity/founder status rather than a common polymorphism.
- **Consanguinity:** Both families are first-cousin or closer consanguineous unions; consanguinity is the principal enabling risk factor for manifestation of this recessive founder allele.

**Protective factors:** None reported or plausible for this single-founder-variant Mendelian disorder; no modifier alleles have been proposed.

**Gene–environment interaction:** None described. Unlike syndromic/complex MAC more broadly (where maternal vitamin A deficiency, gestational infection, retinoic acid/isotretinoin, and solvent exposure are recognized environmental contributors — PMID:[18039390](https://pubmed.ncbi.nlm.nih.gov/18039390/)), no environmental modifier has been reported specifically for MCOPCB13; this reflects the small number of cases studied rather than a demonstrated absence of interaction.

---

## 3. Phenotypes

MCOPCB13 shows a wide, even **intra-individual (between the two eyes of the same patient) and intra-family** phenotypic range across the microphthalmia–anophthalmia–coloboma spectrum, despite an identical homozygous genotype in all seven reported affected individuals — a pattern the authors interpret as evidence of variable, dosage-sensitive *IHH* enhancer output rather than genetic heterogeneity.

**Ocular phenotypes documented (Table 1 of PMID:37580330):**

| Phenotype | HPO suggestion | Notes |
|---|---|---|
| Microphthalmia (uni- or bilateral, asymmetric severity) | HP:0000568 | Present in nearly all affected individuals; severity varies eye-to-eye in the same patient |
| Anophthalmia (clinical, one or both eyes) | HP:0000528 | Present in a subset (e.g., proband P1 VI-8, P1 VI-3, P2 II-1) |
| Optic nerve coloboma (uni- or bilateral) | HP:0000588 | Present in most individuals, often bilateral even when microphthalmia is asymmetric |
| High/severe myopia | HP:0011003 (High myopia) | Frequent accompanying refractive finding |
| Nystagmus | HP:0000639 | Frequent, reflecting poor early visual input |
| Nuclear/congenital cataract | HP:0000518 | Reported in at least one individual |
| Retinal detachment | HP:0000541 | Reported, contributing to vision loss |
| Retinal pigmentary changes/atrophy | HP:0000580 (abnormal retinal pigmentation, approximate) | Reported |
| Glaucoma | HP:0000501 | Reported in the most severely affected eye of one patient |
| Strabismus | HP:0000486 | Reported as an accompanying feature |

**Onset:** Congenital in all cases (present from birth; consistent with a failure of optic fissure closure, a first-trimester embryonic event).

**Severity/progression:** Severity is markedly **variable between individuals and between the two eyes of one individual** — ranging from mild coloboma with preserved vision to bilateral anophthalmia/severe microphthalmia with complete, early (by age 8 in one case) blindness requiring bilateral ocular prostheses. Progression beyond the structural malformation itself (e.g., retinal detachment, glaucoma) can add later, acquired vision loss on top of the congenital malformation.

**Systemic features:** Notably, **no skeletal, craniofacial, or other systemic abnormalities were observed** in any of the reported patients — a point the authors specifically highlight as unexpected, since the same i8 enhancer/IHH locus is essential for limb chondrogenesis (its disruption in chickens and dogs, see §14, causes severe limb defects). This supports classifying MCOPCB13 as **non-syndromic/isolated** rather than syndromic MAC, and argues that ocular and limb i8 activity are separable, tissue-specific sub-elements of the enhancer, or that the human variant selectively spares the limb-active sub-module.

**Quality of life impact:** Not formally measured with EQ-5D/SF-36-type instruments in the primary literature; qualitatively, several patients experienced profound early-childhood visual impairment/blindness requiring bilateral ocular prostheses, which — as with MAC broadly — carries substantial functional, psychosocial, and developmental burden (MAC overall causes 3.2–11.2% of childhood blindness, PMID:[18039390](https://pubmed.ncbi.nlm.nih.gov/18039390/)).

---

## 4. Genetic/Molecular Information

**Causal locus:** Not a classical protein-coding gene mutation. The variant lies in a **cis-regulatory element (enhancer)**, physically hosted within an intron of *NHEJ1* but functionally dedicated to controlling expression of the neighboring gene ***IHH*** (Indian hedgehog signaling molecule; HGNC:5384; OMIM *600726).

- **Variant:** NHEJ1(NM_024782.2):c.588+18131A>G; NG_007880.1:g.37317A>G; ClinVar submission SCV002769719.
- **Classification:** Reported as segregating, extremely rare/absent-from-population-databases, and functionally validated (see §6) — consistent with pathogenic/likely pathogenic by ACMG-type criteria, though the variant type (deep intronic regulatory) falls outside standard ACMG coding-variant categories and required custom enhancer-functional evidence for classification.
- **Variant type/class:** Single-nucleotide substitution in a **conserved noncoding regulatory element** (not missense/nonsense/frameshift/splice — predicted to have **no splicing effect**).
- **Allele frequency:** Not present in gnomAD; absent in 87 ethnically matched controls — consistent with a rare founder allele private to the Mashhad Jewish-Iranian community.
- **Origin:** Germline, inherited (both parents obligate heterozygous carriers in each family; all affected individuals homozygous).
- **Functional consequence:** Loss-of-function at the level of enhancer activity — the mutant i8 sequence fails to drive reporter expression in the developing eye in transgenic assays (§6), consistent with reduced/abolished eye-specific *IHH* transcriptional activation rather than a gain-of-function or dominant-negative mechanism.

**Modifier genes:** None identified; the marked intra-/inter-individual phenotypic variability despite an identical genotype is proposed to reflect **quantitative/stochastic variation in residual enhancer output** rather than a discrete modifier locus, though this remains a hypothesis rather than demonstrated modifier genetics.

**Epigenetic information:** The i8 element carries active enhancer chromatin marks — **H3K27ac and H3K4me1** — and is DNase I hypersensitive; ATAC-seq in chicken retinal pigment epithelium (embryonic days 4–5 / Hamburger-Hamilton stages 24–26) shows a sharp chromatin-accessibility peak coinciding precisely with the conserved i8 region and the orthologous variant position, overlapping a predicted **PAX4** binding motif (GEO accession GSE197935).

**Chromosomal abnormalities:** None reported; this is a single-nucleotide regulatory variant, not a structural rearrangement, in the human disease. (Contrast with the **canine and avian orthologous loci**, where deletions spanning IHH/NHEJ1 do cause disease — see §14.)

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributory factor has been reported for MCOPCB13 specifically. This differs from the broader MAC spectrum, where recognized environmental contributors include:
- **Maternal vitamin A deficiency** (retinoic acid signaling is central to optic vesicle/fissure patterning)
- **Gestational infections** (e.g., rubella)
- **Teratogens:** isotretinoin/retinoic acid excess, thalidomide, solvent misuse, ionizing radiation exposure (PMID:[18039390](https://pubmed.ncbi.nlm.nih.gov/18039390/); PMID:[40491727](https://pubmed.ncbi.nlm.nih.gov/40491727/))

For MCOPCB13, the described families' phenotype segregated as a clean Mendelian recessive trait tracking the identified variant, with no report of an environmental co-factor being sought or implicated.

---

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from lesion to clinical phenotype):**

1. A homozygous A>G substitution disrupts the conserved core "GGGTGA" motif of the *IHH* i8 enhancer, an intronic cis-regulatory element of *NHEJ1* on chr2q35 — this **destroys or reduces binding of a transcription factor** (predicted PAX4, with PAX6 also biologically plausible given its established role in the same developmental window) — *inferred from motif overlap and prediction algorithms, not directly demonstrated by ChIP or EMSA in this study*.
2. Loss of transcription-factor engagement **leads to** reduced/abolished i8 enhancer activity, demonstrated directly: the mutant i8 sequence fails to reproducibly drive lacZ reporter expression in the developing mouse eye at E11.5 (only 1/≥5 embryos showed weak, likely positional-artifact staining, versus consistent expression for the wild-type sequence).
3. Reduced enhancer output **results in** diminished/dysregulated *IHH* transcription specifically in the **periocular mesenchyme (POM)** and **retinal pigment epithelium (RPE)** of the developing eye — the tissue domain the wild-type i8 enhancer normally activates (demonstrated by wild-type reporter expression pattern phenocopying endogenous *Ihh*, and by chicken electroporation assays showing i8-driven fluorescence specifically in POM and ocular surface at Hamburger-Hamilton stages ~24–26/days 4–5).
4. Insufficient local *IHH* signaling **leads to** failure of normal POM differentiation and RPE maturation — mechanistically inferred by analogy to the *Ihh⁻/⁻* mouse (§ below), since MCOPCB13 patients were not themselves biopsied; this step is a model-organism-based inference, not directly observed in human tissue.
5. Disrupted RPE/POM differentiation and hedgehog-target-gene expression at the retina–periocular-mesenchyme interface **results in** failure of normal optic fissure/optic cup morphogenesis and closure — the proximate embryological event underlying colobomatous phenotypes.
6. Depending on the degree of local *IHH* deficiency (proposed to vary stochastically or due to unidentified modifiers), this **produces** the clinical spectrum observed: from isolated optic nerve coloboma (mild), through microphthalmia with retinal/scleral involvement, to complete anophthalmia (severe) — explaining the marked inter- and even intra-individual variability in a genetically homogeneous cohort.
7. Secondary/downstream consequences of the primary malformation **lead to**: high myopia and strabismus (abnormal globe geometry/axial length), nystagmus (poor early foveal/visual input), cataract and retinal detachment (structurally abnormal, thin or poorly supported ocular tissue), and ultimately profound early childhood visual impairment/blindness in the more severely affected eyes.

**Branch point — why no skeletal phenotype:** The same *IHH*/i8 regulatory region is essential for limb chondrogenesis in other species (chicken Creeper, canine CEA — §14), yet MCOPCB13 patients showed **no skeletal or cranial abnormalities**. The authors interpret this as evidence that the i8 enhancer (or its human ortholog) is a **tissue-restricted, eye-specific regulatory module**, separable at the sequence level from the limb-specific IHH enhancers in the same broader *cis*-regulatory landscape (a landscape whose limb elements were characterized by Will et al. 2017's multipartite Ihh enhancer cluster study).

**Molecular pathway:** Hedgehog signaling (Indian hedgehog / Hh pathway) — GO term suggestion: **GO:0007228** (positive regulation of hedgehog signaling pathway) or **GO:0007224** (smoothened signaling pathway); more specific to eye morphogenesis: **GO:0060042** (retina morphogenesis in camera-type eye) and **GO:0001654** (eye development).

**Cell types involved:**
- **Periocular mesenchyme cells** — CL suggestion: **CL:0000134** (mesenchymal cell) or a more specific neural-crest-derived periocular mesenchyme population (no single precise CL term exists; periocular mesenchyme is largely cranial-neural-crest-derived).
- **Retinal pigment epithelial (RPE) cells** — **CL:0002586** (retinal pigment epithelial cell) or **CL:0000501** (granular cell/RPE-related, check current CL); canonical RPE CL term is **CL:0002586**.
- Non-pigmented choroidal precursor cells adjacent to RPE (site of endogenous *Ihh* expression in mouse).

**Protein/biochemical mechanism:** IHH is a secreted morphogen of the Hedgehog family; canonical signaling proceeds via **Patched (PTCH1)** de-repression of **Smoothened (SMO)**, activating GLI transcription factors. In the eye, IHH signaling range is restricted to POM and RPE (not neural retina directly), driving target-gene expression required for POM differentiation, scleral condensation, and RPE pigmentation/maturation (PMID:[18582859](https://pubmed.ncbi.nlm.nih.gov/18582859/)).

**Evidence for this mechanism (from the primary study, functional/experimental — animal models, not human tissue):**
- **Mouse transgenic reporter assay:** Wild-type i8 enhancer consistently drove lacZ expression in the POM at E11.5, phenocopying endogenous *Ihh*; the mutant (patient) sequence did not.
- **Chicken embryo electroporation:** Wild-type chicken i8-GFP/mCherry constructs produced punctate POM/ocular-surface fluorescence in 5/5 tested embryos by days 4–5; control plasmid lacking the enhancer produced no signal in 19/19 embryos.
- **ATAC-seq (chicken RPE, E4-5):** Confirmed an open-chromatin accessibility peak precisely at the conserved i8 element, overlapping the variant position and a predicted PAX4 motif.
- **Mouse *Ihh⁻/⁻* knockout phenotype** (independent prior literature, PMID:[18582859](https://pubmed.ncbi.nlm.nih.gov/18582859/)): severe RPE hypopigmentation, abnormal globe shape, scleral/choroidal abnormalities, reduced retinal progenitor proliferation and photoreceptor specification, and high rates of retinal detachment — directly mirroring the human MCOPCB13 phenotype spectrum (RPE pigmentary changes, retinal detachment).

**Authors' own conclusion (direct quote):** *"Through mouse and chicken molecular development studies, we demonstrated that this variant is within an Ihh enhancer that drives gene expression in the developing eye and that the identified variant affects this eye-specific enhancer activity."* And on mechanism: *"given the recessive inheritance pattern, position of the i8 enhancer relative to the Ihh transcription start site, functional enhancer data, and overall parsimony, a loss-of-function enhancer mechanism seems most likely."*

**Note on the "gene name" pitfall:** Because the variant is hosted within an *NHEJ1* intron, it is essential in curation not to conflate MCOPCB13 with **Cernunnos/XLF deficiency** (OMIM #611291, *NHEJ1*-related severe combined immunodeficiency with microcephaly, growth retardation, and radiosensitivity), a completely distinct disease caused by **coding** loss-of-function variants that eliminate NHEJ1/Cernunnos protein function in DNA double-strand-break repair (PMC:[11895763](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11895763/)). MCOPCB13's variant does not appear to affect NHEJ1 protein function; it acts purely at the level of a neighboring gene's enhancer.

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Eye (globe, optic nerve) — UBERON:0000970 (eye)
- No secondary/systemic organ involvement reported (isolated ocular phenotype only, per the primary cohort)
- Body system: visual/sensory system only

**Tissue and cell level:**
- **Periocular mesenchyme** (neural-crest/mesoderm-derived, forms sclera, choroid, extraocular structures) — UBERON:0007037 (periocular mesenchyme is a less standard UBERON term; sclera UBERON:0001773, choroid UBERON:0000384 are established downstream structures)
- **Retinal pigment epithelium** — UBERON:0002385
- **Optic nerve/optic disc** — UBERON:0001789 (optic nerve), UBERON:0001786 (optic disc)
- **Retina** — UBERON:0000966
- **Lens** (cataract) — UBERON:0000965
- **Sclera** — UBERON:0001773

**Subcellular level:** Not specifically investigated in this disorder beyond gene-regulatory (nuclear/chromatin) mechanism — GO Cellular Component: chromatin/enhancer region acting in the nucleus of POM/RPE progenitor cells.

**Localization:** Bilateral involvement is typical, though **markedly asymmetric between the two eyes of the same individual** — a distinctive and repeatedly emphasized feature of this entry, distinguishing it from more uniformly bilateral syndromic MAC forms.

---

## 8. Temporal Development

**Onset:** Congenital — present at birth, as expected for a defect of embryonic optic fissure closure (a first-trimester event, roughly gestational weeks 5–7 in humans).

**Onset pattern:** The structural malformation itself is present from conception/early embryogenesis (not acquired postnatally); however, **secondary complications** (retinal detachment, cataract progression, glaucoma) can manifest or progress later in childhood, contributing to a component of postnatal, progressive visual decline layered on top of the static congenital malformation.

**Disease stages/course:** Not formally staged; reported course across the cohort ranged from stable congenital structural anomaly with preserved partial vision, to progressive loss culminating in complete blindness by age 8 in at least one individual (P1 VI-8), with bilateral prosthesis use in the most severe cases (P1 VI-3, P1 VI-8).

**Progression rate:** Variable — from apparently stable to relatively rapid loss of vision in early childhood in the most severe presentations.

**Critical period:** The relevant embryological critical window is **optic fissure closure**, occurring in the first trimester; this is the developmental period during which the i8 enhancer must be active in POM/RPE progenitors for normal closure to occur. No postnatal therapeutic window is described (the malformation is not preventable postnatally), but **early ocular socket/prosthetic management** represents a critical early-childhood intervention window for functional/cosmetic outcomes (§12).

---

## 9. Inheritance and Population

**Epidemiology:** No disease-specific prevalence/incidence figure exists for MCOPCB13 — it has been reported in exactly 2 families (7 affected individuals) to date. For context, the broader MAC spectrum to which it belongs has an estimated **combined incidence of 6–13 per 100,000 births** (anophthalmia 0.6–4.2/100,000; microphthalmia 2–17/100,000; coloboma 2–14/100,000), with some estimates of combined MAC prevalence as high as 30/100,000 (PMID:[40491727](https://pubmed.ncbi.nlm.nih.gov/40491727/); PMID:[18039390](https://pubmed.ncbi.nlm.nih.gov/18039390/)). Approximately one-third of all MAC is syndromic; MCOPCB13 as described is non-syndromic.

**Inheritance pattern:** **Autosomal recessive.** All affected individuals homozygous for the founder variant; both parents in each family obligate heterozygous carriers with no reported phenotype (consistent with a fully recessive mechanism at the enhancer-dosage level — i.e., one functional copy of the enhancer/IHH allele is sufficient for normal development).

**Penetrance:** Full segregation with disease status was observed in both pedigrees (all homozygotes affected), suggesting high/complete penetrance for *some* point on the MAC severity spectrum, though **expressivity is markedly variable** (see below) — a homozygote is essentially always affected, but the specific phenotype (isolated coloboma vs. bilateral anophthalmia) is unpredictable.

**Expressivity:** **Highly variable**, both between families, between individuals within a family, and — unusually — **between the two eyes of the same individual**. This intra-patient asymmetry despite an identical constitutional genotype is one of the most distinctive features reported and is attributed to presumed stochastic variation in residual enhancer/IHH output during the critical developmental window, rather than to somatic mosaicism or second-hit mutation (neither of which was tested/excluded in the primary study).

**Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically investigated.

**Founder effect:** Strongly supported — a single shared ~0.5 Mb haplotype across both unrelated (or distantly related) pedigrees from the same isolated **Mashhad Jewish-Iranian community**, consistent with a population founder allele rather than recurrent independent mutation.

**Consanguinity role:** Central — both pedigrees are consanguineous, and the Mashhad Jewish-Iranian population is described in the primary literature as having "a very high degree of inbreeding," which is the demographic mechanism by which this otherwise very rare recessive founder allele reaches homozygosity.

**Carrier frequency:** Not formally estimated; the variant's absence from 87 local ethnically matched controls and from gnomAD suggests low, community-restricted carrier frequency, but no precise figure is published.

**Population demographics:** Reported exclusively in the Jewish Iranian population of Mashhad, Iran (a historically endogamous, geographically/religiously isolated community). No other population or ethnic group has yet been reported with this specific variant; whether the i8 enhancer is a recurrent mutational hotspot in other populations is unknown.

**Sex ratio / age distribution:** Not reported as skewed by sex (autosomal recessive, expected 1:1); age at diagnosis in the reported cohort ranged from under 1 year to 30 years, reflecting both new pediatric cases and adult affected relatives identified through family studies.

---

## 10. Diagnostics

**Clinical evaluation:** Standard dilated fundoscopic/ophthalmologic examination to characterize microphthalmia, anophthalmia, and coloboma extent (iris, ciliary body, choroid, retina, optic nerve involvement), axial length measurement (myopia), and assessment for cataract, retinal detachment, and glaucoma.

**Imaging:** Ocular ultrasound (B-scan) and/or orbital MRI to characterize globe size/structure, particularly in anophthalmic or severely microphthalmic orbits where direct visualization is limited.

**Genetic testing:**
- **First-line for isolated/non-syndromic MAC:** A targeted **MAC gene panel** — commercial panels typically include *BCOR, BMP4, GDF3, GDF6, MFRP, OTX2, PAX6, PRSS56, RAX, SHH, SIX6, SOX2, STRA6, VSX2*, and others (GTR test listings referenced above) — though **none of these standard panels would capture the MCOPCB13 variant**, since it lies in a deep intronic/regulatory region outside coding-exon-focused panels.
- **For MCOPCB13 specifically:** Detection requires either (a) **whole-genome sequencing** (the modality that identified the founder variant after whole-exome sequencing was uninformative), or (b) **targeted testing for the specific founder variant** (NHEJ1 c.588+18131A>G) in individuals of Mashhad Jewish-Iranian ancestry with consanguinity and MAC-spectrum findings.
- **Whole-exome sequencing (WES) utility:** Limited for this specific entry — WES in the original families excluded coding variation in known MAC genes and in coding sequences at the 2q35 locus, and it was **whole-genome sequencing** that ultimately identified the causal deep-intronic variant. This is a case example of the diagnostic-yield gap WGS closes over WES for regulatory/noncoding disease.
- **Chromosomal microarray/karyotype/FISH:** Reasonable first-tier tests to exclude chromosomal MAC etiologies (common in broader MAC differential) but would not detect this single-nucleotide regulatory variant.

**Differential diagnosis:** The broader MCOPCB/MAC phenotypic series (OMIM PS251600) includes numerous genetically distinct but clinically overlapping entries, including (non-exhaustive): MCOPCB1 (X-linked, gene unknown), MCOPCB2 (15q12-q15, gene unknown), MCOPCB3/6 (*VSX2*), MCOPCB4 (*SHH*), MCOPCB (*GDF6*), MCOPCB (*RAX*), MCOPCB (*ALDH1A3*), MCOPCB (*YAP1*), MCOPCB12 (OMIM #120200), plus syndromic MAC genes (*PAX6, SOX2, OTX2, STRA6, BCOR, CHD7*) and chromosomal/teratogenic causes. Distinguishing features favoring MCOPCB13 specifically: **non-syndromic presentation with no skeletal/systemic involvement**, autosomal recessive segregation, and Mashhad Jewish-Iranian ancestry with consanguinity.

**Screening:** No population newborn-screening program exists (or would be expected) for this ultra-rare founder variant; **targeted carrier screening / cascade testing within the Mashhad Jewish-Iranian community** would be the logical population-specific screening approach, analogous to other founder-variant carrier screening programs in this population, though no such program has been reported as implemented specifically for this variant.

---

## 11. Outcome/Prognosis

**Survival/mortality:** Not a life-limiting condition; no mortality data relevant (isolated ocular malformation with no reported systemic organ involvement).

**Morbidity/function:** The principal morbidity is **visual impairment ranging from mild to complete blindness**, occurring congenitally and in some cases progressing (via retinal detachment, cataract, glaucoma) to complete loss of vision in early childhood (documented as early as age 8 in one individual). Several individuals required bilateral enucleation-equivalent management with ocular prostheses.

**Complications:** Cataract, retinal detachment, glaucoma, and secondary refractive complications (high myopia) were all documented as complications layered on the primary structural malformation.

**Quality of life:** Not formally quantified in the primary literature; congenital severe visual impairment/blindness in early childhood carries substantial, well-established developmental, educational, and psychosocial impact generally (drawing on broader MAC/childhood-blindness literature, PMID:[18039390](https://pubmed.ncbi.nlm.nih.gov/18039390/)), though disease-specific QOL instrument data (EQ-5D, etc.) do not exist for this entry.

**Prognostic factors:** The degree of anophthalmia/microphthalmia and presence of optic nerve coloboma at presentation appear to correlate with ultimate visual outcome, though given the marked intra-patient (eye-to-eye) variability, **prognosis cannot be reliably predicted from genotype alone**, and must be individualized per-eye based on clinical exam.

---

## 12. Treatment

There is **no disease-modifying or curative treatment** for MCOPCB13 (or for MAC generally) — management is entirely supportive/rehabilitative and directed at maximizing residual vision and managing the anophthalmic/microphthalmic socket.

- **Ocular/socket management (primary intervention):**
  - **Socket expansion with conformers** in anophthalmia/severe microphthalmia — gradually enlarging acrylic conformers, typically changed every 6–8 weeks in the first years of life, achieving good expansion outcomes in ~75% of orbits per case series (PMID:[36257503](https://pubmed.ncbi.nlm.nih.gov/36257503)).
  - Custom **ocular prostheses** fitted and managed by an ocularist, with regular follow-up every 3–6 months, to stimulate/maintain normal orbital and periocular soft-tissue development and for cosmesis.
  - NCIT suggestion for this care pathway: **NCIT:C15747** (Supportive Care); a specific prosthetic-fitting procedure term (e.g., ocular prosthesis fitting) should be sourced from NCIT if binding for KB curation.
- **Surgical:** Management of complications as they arise — cataract extraction, retinal detachment repair, and glaucoma surgery/medical therapy in eyes with sufficient residual structure to warrant intervention. (NCIT:C15329, Surgical Procedure, as a general treatment-action term; specific procedures would need individual NCIT binding.)
- **Low-vision rehabilitation:** Refractive correction for high myopia, low-vision aids, and early intervention/vision-rehabilitation services for visually impaired infants and children (NCIT:C15315, Rehabilitation).
- **Genetic counseling:** Recommended for affected families given the autosomal recessive, founder-variant, highly consanguineous context (NCIT:C15240, Genetic Counseling).
- **Experimental/targeted/gene therapy:** None reported or in development specific to this entry; no ClinicalTrials.gov-registered trial for MCOPCB13 or *IHH*-enhancer-directed therapy was identified in this search. Given the very recent (2023) molecular delineation of this disorder and its extreme rarity (2 families), it is not surprising that no targeted therapeutic pipeline yet exists.

---

## 13. Prevention

**Primary prevention:** Not applicable in the sense of modifiable risk-factor reduction (this is a fixed germline founder variant); the only "primary prevention" avenue is **reproductive/genetic counseling and carrier screening** within the at-risk (Mashhad Jewish-Iranian, consanguineous) population, potentially including preimplantation genetic diagnosis (PGD) or prenatal testing for at-risk couples once carrier status is known.

**Secondary prevention:** Early prenatal or neonatal recognition (e.g., prenatal ultrasound detection of microphthalmia/anophthalmia, or newborn eye exam) allows earlier referral to ophthalmology/adnexal specialists and earlier initiation of socket-expansion conformer therapy — a form of secondary prevention aimed at minimizing downstream orbital/socket underdevelopment and optimizing eventual prosthetic and cosmetic outcomes.

**Tertiary prevention:** Ongoing surveillance for and prompt management of complications (cataract, retinal detachment, glaucoma) in affected eyes to preserve any residual vision.

**Genetic counseling:** Central preventive tool given the recessive, founder-variant, highly consanguineous population context — risk assessment for future pregnancies in carrier couples, and potential cascade carrier testing of extended family members in the Mashhad Jewish-Iranian community.

**Public health:** No population-level screening or public-health program specific to this variant has been reported; the extreme rarity (2 families reported to date) makes population screening premature absent further case ascertainment.

---

## 14. Other Species / Natural Disease — This Is the Most Distinctive Feature of MCOPCB13's Evidence Base

Unusually for a rare human Mendelian disease, MCOPCB13's causal mechanism is supported by **naturally occurring disease at the same genomic locus in two other species**, making this an unusually strong example of cross-species mechanistic convergence:

**Chicken (*Gallus gallus*, NCBI Taxon:9031) — "Creeper" trait:**
- A **25 kb deletion** spanning both *IHH* and *NHEJ1* on chicken chromosome 7 causes the dominant, semi-lethal **Creeper (Cp)** phenotype in Japanese bantam chickens.
- **Cp/+ heterozygotes** (IHH haploinsufficiency) show **microphthalmic and colobomatous eyes** together with phocomelic (short) limbs — directly paralleling the human ocular phenotype, though the chicken also shows the limb phenotype the human patients lack.
- **Cp/Cp homozygotes** show complete loss of IHH and are embryonic lethal with severe chondrodystrophy.
- References: PMID:[27439785](https://pubmed.ncbi.nlm.nih.gov/27439785/) (Scientific Reports 2016); PMID:[32214226](https://pubmed.ncbi.nlm.nih.gov/32214226/) (Communications Biology 2020, combined IHH/NHEJ1 deletion and chondrodystrophy/embryonic lethality).
- This is cited directly in the human paper as prior evidence motivating investigation of the IHH/NHEJ1 locus for human ocular disease.

**Dog (*Canis lupus familiaris*, NCBI Taxon:9615) — Collie Eye Anomaly (CEA):**
- A well-characterized ~7.8 kb intronic deletion at the same general IHH/NHEJ1 regulatory locus (affecting a neighboring enhancer, **"i9"**) causes **Collie Eye Anomaly**, a naturally occurring canine ocular malformation syndrome (choroidal hypoplasia, coloboma, retinal detachment) segregating in Collies and related breeds (Border Collie, Australian Shepherd, Shetland Sheepdog, etc.).
- OMIA (Online Mendelian Inheritance in Animals) catalogs CEA; it is one of the most common inherited canine ocular disorders and is used in veterinary breeding programs for carrier screening.
- The human MCOPCB13 authors explicitly cite CEA as **comparative evidence for a shared IHH-enhancer-driven ocular regulatory mechanism** across the same broader locus, even though the specific enhancer element differs (i8 in humans vs. i9 in dogs) — supporting a model of a **multipartite IHH enhancer cluster** (per Will et al. 2017's foundational characterization) with several tissue/organ-specific sub-elements that can be independently disrupted across species.

**Comparative biology conclusion:** This is a rare instance of an enhancer cluster whose disruption produces **convergent, tissue-specific ocular phenotypes in three species (human, chicken, dog)** via distinct lesions (SNV, large deletion, large deletion respectively) at neighboring but non-identical regulatory elements of the same target gene (*IHH*) — a strong argument for deep evolutionary conservation of *IHH*'s role in optic fissure/RPE/choroid development.

**Zoonotic potential:** Not applicable (non-infectious, genetic disorder).

---

## 15. Model Organisms

**Mouse (*Mus musculus*):**
- ***Ihh⁻/⁻* (Indian hedgehog knockout) mice** (PMID:[18582859](https://pubmed.ncbi.nlm.nih.gov/18582859/)): the key pre-existing genetic model establishing IHH's necessity for normal eye development. Phenotype: severe RPE hypopigmentation, abnormal globe shape/size, sclera and choroid abnormalities (failure of POM mesenchymal condensation/differentiation), reduced retinal progenitor proliferation, reduced photoreceptor specification, and high rates of retinal detachment. This phenotype **substantially recapitulates** the human MCOPCB13 spectrum (RPE pigmentary abnormality, retinal detachment, abnormal globe), supporting **high fidelity** as a mechanistic (though not genetically identical — full knockout vs. partial enhancer hypomorph) model.
- **Transgenic i8-enhancer-lacZ reporter mice** (generated specifically for the MCOPCB13 study, PMID:37580330): used to functionally test wild-type versus mutant i8 sequence activity at E11.5; this is a **perturbation/reporter model**, not a disease model per se, but is the direct functional proof that the human variant abolishes eye-specific enhancer activity.
- **Model limitation:** The mouse knockout is a **complete null**, whereas the human disease variant is a hypomorphic enhancer lesion — the mouse model therefore likely represents the severe end of the human phenotypic spectrum and does not, by itself, explain the marked variable expressivity seen in human patients.

**Chicken (*Gallus gallus*):**
- **Cp (Creeper) chicken**, naturally occurring IHH/NHEJ1-locus deletion (see §14) — a naturally occurring genetic model with direct construct/electroporation validation used in the primary human study itself (i8-GFP/mCherry electroporation into HH stage 9–12 optic vesicles, confirming POM/ocular-surface-restricted enhancer activity by days 4–5).
- Chicken embryos also served as the platform for the **ATAC-seq** experiment defining the chromatin-accessibility signature of the wild-type i8 element in RPE.
- **Applications:** The chicken system's experimental tractability (ex ovo electroporation, rapid embryonic staging) made it the primary platform for direct functional dissection of enhancer activity and chromatin state — complementary to the mouse transgenic (stable, germline-integrated) reporter approach.

**Dog (*Canis lupus familiaris*):** Naturally occurring CEA (§14) — used as **comparative/corroborating evidence** rather than as an experimentally manipulated model in this study; no de novo dog experiments were performed, but existing veterinary genetics literature on the i9 enhancer deletion was cited.

**Cell-based/in vitro models:** None reported specific to this entry (no iPSC, organoid, or optic-vesicle-organoid modeling of the human variant has yet been published as of this literature search).

**Resources:** MGI (mouse *Ihh* alleles), NCBI Gene (orthology: human *IHH* HGNC:5384 ↔ mouse *Ihh* MGI:96549 ↔ chicken *IHH*), OMIA (canine CEA entry).

---

## Summary Table — Suggested Ontology Bindings for KB Curation

| Category | Suggested term | Notes |
|---|---|---|
| Disease | MONDO:0975809 | As given |
| Causal gene (regulated) | hgnc:5384 (IHH) | Note: regulatory variant, not coding |
| Enhancer host gene | hgnc:25737 (NHEJ1) | Do not conflate with Cernunnos/XLF deficiency (OMIM #611291) |
| Inheritance | HP:0000007 Autosomal recessive inheritance | |
| Phenotypes | HP:0000568 Microphthalmia; HP:0000528 Anophthalmia; HP:0000589 Coloboma; HP:0000588 Coloboma of optic nerve; HP:0011003 High myopia; HP:0000639 Nystagmus; HP:0000518 Cataract; HP:0000541 Retinal detachment; HP:0000501 Glaucoma; HP:0000486 Strabismus | Verify exact IDs/labels against current HPO release before binding |
| Biological process | GO:0001654 Eye development; GO:0060042 Retina morphogenesis in camera-type eye | Verify against GO before binding |
| Cell types | Periocular mesenchyme (neural-crest derived); CL:0002586 Retinal pigment epithelial cell | |
| Anatomy | UBERON:0000966 Retina; UBERON:0002385 Retinal pigment epithelium; UBERON:0001789 Optic nerve; UBERON:0000384 Choroid; UBERON:0001773 Sclera | |
| Species (models) | NCBITaxon:10090 Mouse; NCBITaxon:9031 Chicken; NCBITaxon:9615 Dog | |

*All ontology IDs above should be re-verified via `runoak`/live lookup before committing to a KB entry, per standard curation practice — this report is a research lead, not a validated term binding.*

---

## Sources

- [IHH enhancer variant within neighboring NHEJ1 intron causes microphthalmia anophthalmia and coloboma — npj Genomic Medicine (2023)](https://www.nature.com/articles/s41525-023-00364-x) / [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10425348/) / [PubMed PMID:37580330](https://pubmed.ncbi.nlm.nih.gov/37580330/)
- [OMIM #620968 — MICROPHTHALMIA/COLOBOMA 13; MCOPCB13](https://omim.org/entry/620968)
- [OMIM *600726 — INDIAN HEDGEHOG SIGNALING MOLECULE; IHH](https://omim.org/entry/600726)
- [OMIM *611290 — NONHOMOLOGOUS END-JOINING FACTOR 1; NHEJ1](https://omim.org/entry/611290)
- [OMIM #611291 — IMMUNODEFICIENCY 124, SEVERE COMBINED; IMD124 (Cernunnos/XLF deficiency — distinct disease)](https://omim.org/entry/611291)
- [Indian hedgehog signaling from endothelial cells is required for sclera and retinal pigment epithelium development in the mouse eye — PMID:18582859](https://pubmed.ncbi.nlm.nih.gov/18582859/)
- [Deletion of Indian hedgehog gene causes dominant semi-lethal Creeper trait in chicken — PMID:27439785](https://pubmed.ncbi.nlm.nih.gov/27439785/)
- [Combined deletions of IHH and NHEJ1 cause chondrodystrophy and embryonic lethality in the Creeper chicken — PMID:32214226](https://pubmed.ncbi.nlm.nih.gov/32214226/)
- [Anophthalmia and microphthalmia — review, PMID:18039390](https://pubmed.ncbi.nlm.nih.gov/18039390/)
- [Genetic and environmental factors contributing to anophthalmia and microphthalmia — PMID:40491727](https://pubmed.ncbi.nlm.nih.gov/40491727/)
- [Socket expansion with conformers in congenital anophthalmia and microphthalmia — PMID:36257503](https://pubmed.ncbi.nlm.nih.gov/36257503)
- [Severe immunodeficiency spectrum associated with NHEJ1 gene mutation: Cernunnos/XLF deficiency — PMC11895763](https://pmc.ncbi.nlm.nih.gov/articles/PMC11895763/)
- [Curate microphthalmia/coloboma 13 (MONDO:0975809) · dismech Issue #12693](https://github.com/monarch-initiative/dismech/issues/12693) (repository curation-queue context)

**Note on evidence base:** This entire disease entity rests on a single 2023 publication describing 7 affected individuals in 2 related families. No independent replication cohort, no second population, and no clinical trial or long-term natural-history study yet exists. Any KB entry built from this report should cite PMID:37580330 as the essentially sole primary human-clinical/genetic source, supplemented by the independently-published mouse (PMID:18582859) and chicken (PMID:27439785, PMID:32214226) model-organism literature for pathway/mechanism support — and should flag the very thin, single-study evidence base explicitly rather than presenting it as well-established.

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 41 |
| Resolved | 34 |
| Unresolved (possible confabulation) | 1 |
| Obsolete | 1 |
| Unverifiable | 5 |
| Terms whose name was checked | 14 |
| Terms named correctly | 6 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 3 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0975809` (4 mentions) - the report calls it "MONDO", "Disease"; MONDO calls it **microphthalmia/coloboma 13**
- `HP:0000568` (3 mentions) - the report calls it "Microphthalmia (uni- or bilateral, asymmetric severity)"; HP calls it **Microphthalmia**
- `HP:0000518` (2 mentions) - the report calls it "Nuclear/congenital cataract"; HP calls it **Cataract**
- `UBERON:0001789` (2 mentions) - the report calls it "optic nerve"; UBERON calls it **outer nuclear layer of retina**
- `UBERON:0001786` (1 mention) - the report calls it "optic disc"; UBERON calls it **fovea centralis**

### Unresolved terms

These identifiers do not exist in an ontology that resolved other terms from the same prefix, so they were most likely invented:

- `UBERON:0000384` (2 mentions) - UBERON does not contain this term

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0007228` (obsolete positive regulation of hh target transcription factor activity) (1 mention) - replaced by `GO:0007224`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0000528` (3 mentions) - the report calls it "Anophthalmia (clinical, one or both eyes)"; HP calls it **Anophthalmia**, and lists "Anophthalmia, clinical" among its other names
- `HP:0000588` (3 mentions) - the report calls it "Optic nerve coloboma (uni- or bilateral)"; HP calls it **Optic disc coloboma**, and lists "Optic nerve coloboma" among its other names
- `HP:0000580` (1 mention) - the report calls it "abnormal retinal pigmentation, approximate"; HP calls it **Pigmentary retinopathy**, and lists "Retinal pigmentary degeneration" among its other names

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0975809` - called "MONDO", "Disease"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `Taxon`, `MGI`.
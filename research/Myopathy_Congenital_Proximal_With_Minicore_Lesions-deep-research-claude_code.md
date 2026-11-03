---
provider: claude_code
model: claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-10-27T14:28:14.248750'
end_time: '2026-10-27T14:34:05.145644'
duration_seconds: 350.9
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Myopathy Congenital Proximal With Minicore Lesions
  mondo_id: MONDO:0032937
  category: Mendelian
  causal_genes: FXR1
  omim_id: OMIM:618823
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
  web_search_requests: 11
  num_turns: 32
  total_cost_usd: 2.5466997000000005
  session_id: 0864d0da-39e8-41a7-9a82-02e86be78a8e
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 4
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
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 6
  relevance_assessed: 11
  on_topic: 7
  validator_version: 0.4.0
term_validation:
  total_terms: 40
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 1
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: HP:0002091
    reported_labels:
    - "cache \u2713"
    ontology_label: Restrictive ventilatory defect
  - term_id: HP:0002205
    reported_labels:
    - "cache \u2713"
    ontology_label: Recurrent respiratory infections
  - term_id: HP:0000028
    reported_labels:
    - "cache \u2713"
    ontology_label: Cryptorchidism
  - term_id: HP:0003803
    reported_labels:
    - "cache \u2713"
    ontology_label: Type 1 muscle fiber predominance
  - term_id: NCIT:C16186
    reported_labels:
    - CIII:1 had surgery at age 12
    ontology_label: Orthopedic Surgical Procedure
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myopathy Congenital Proximal With Minicore Lesions
- **MONDO ID:** MONDO:0032937 (if available)
- **Causal gene(s):** FXR1
- **OMIM:** OMIM:618823
- **Synonyms:** not recorded
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Myopathy Congenital Proximal With Minicore Lesions** covering all of the
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

Still gathering sources: I have the two main FXR1 papers (PMID 30770808, PMID 35393337) and am now pulling their full text from Europe PMC.

The 2022 paper's full text won't load, so I'm trying other copies of it and checking OMIM and Orphanet for identifiers.

Now checking which HPO terms the local ontology cache already holds, so I can tell which IDs below are confirmed and which still need a lookup.

# FXR1-related congenital myopathy 9B (proximal, with minicore lesions): research report

**Target:** Myopathy, congenital proximal, with minicore lesions. MONDO:0032937; OMIM #618823, which OMIM names "Congenital myopathy 9B, proximal, with minicore lesions; CMYO9B". The causal gene is **FXR1** (FMR1 autosomal homolog 1, OMIM *600819). The disease is caused by biallelic frameshift variants in **exon 15** of FXR1, an exon that is spliced only into the muscle-specific isoforms.

**Scope of the sources:** The disease rests on two primary human papers, about 11 patients from 5 families, plus mouse, zebrafish and Xenopus work.
- I checked abstract sentences against Europe PMC records. Patient-level details come from the PMC full text of PMID 35393337 and the Europe PMC full text of PMID 30770808. I could not open OMIM directly; it returned 403.
- Every CURIE marked **[cache ✓]** has a row in this repository's `cache/hp/terms.csv` with that label. Anything marked **[verify]** was not found in a cache and must be looked up before it is bound.
- FXR1's HGNC ID (believed to be hgnc:4023) is **not** in `cache/hgnc/terms.csv`, and MONDO:0032937 is not in `cache/mondo/terms.csv`. Confirm both with `just validate-terms`.

---

## 1. Disease information

**Overview.** CMYO9B is an autosomal recessive congenital myopathy.
- **Onset and course:** neonatal or infantile hypotonia, delayed motor milestones, then slowly progressive proximal and axial (neck) weakness, with survival into adulthood.
- **Laboratory and imaging:** CK is normal. Muscle imaging shows diffuse atrophy with relative sparing of the quadriceps.
- **Respiratory:** often involved, as obstructive sleep apnoea or nocturnal hypoventilation, sometimes needing BiPAP.
- **Biopsy:** multi-minicores, type 1 fibre predominance and internal nuclei.

**Sibling entity, a likely lump/split question.** OMIM #618822, **CMYO9A** ("Congenital myopathy with respiratory insufficiency and bone fractures"), is caused by a different exon-15 frameshift (c.1764_1767delACAG). It is lethal in infancy, with long-bone fractures and respiratory failure. The 2022 series groups both under the umbrella "FXR1-related congenital myopathy":

> "Biallelic pathogenic variants in FXR1 have recently been associated with two congenital myopathy phenotypes: a severe form associated with hypotonia, long bone fractures, respiratory insufficiency and infantile death and a milder form characterised by proximal muscle weakness with survival into adulthood." (PMID:35393337)

For the KB, either curate CMYO9B alone and reference CMYO9A in notes, or decide on a parent entry with two `has_subtypes`. Check whether the stub queue holds MONDO's CMYO9A term separately; the MONDO ID for CMYO9A is **[verify]**.

**Identifiers**

| Source | Identifier |
|---|---|
| OMIM | 618823 (phenotype); 600819 (gene) |
| MONDO | 0032937 **[verify label in MONDO]** |
| MedGen | 1717569 (reported by a third-party aggregator; **[verify]**) |
| Disease Ontology | DOID:0081344, "congenital myopathy 9B" |
| LOVD | disease #06601, "MYOPMIL" |
| Orphanet | No FXR1-specific ORPHA code found. It probably falls under the multiminicore disease grouping; **[verify]** |
| ICD-10 / ICD-11 | No specific code. The general congenital myopathy code is G71.2 (ICD-10) |
| MeSH | No specific heading. PubMed's supplementary concept on PMID 30770808 is "minicore myopathy with external ophthalmoplegia", which is a mismatch: no FXR1 patient had ophthalmoplegia |

**Synonyms:** CMYO9B; congenital myopathy 9B, proximal, with minicore lesions; FXR1-related congenital myopathy (umbrella term); congenital multi-minicore myopathy, FXR1-related.

**Nature of the data:** all of it comes from individual-patient case series. There is no registry or EHR-level data.

---

## 2. Etiology

- **Cause:** monogenic, through biallelic loss-of-function frameshifts confined to FXR1 exon 15.
  > "We report that recessive mutations in this particular exon of FXR1 cause congenital multi-minicore myopathy in humans and mice." (PMID:30770808; checked against Europe PMC, though the tool truncated the quote output after "myopathy")
- **Genetic risk factors:** parental consanguinity (Families 1, A and C). There are no known modifier genes, susceptibility loci or GWAS signals.
- **Environmental, protective and gene–environment factors:** none reported. The 2022 authors report phenotypic variability even within homozygotes for the same variant, which points to unidentified modifiers.

---

## 3. Phenotypes

The core set comes from Mroczek et al. 2022 (8 patients, Families A–D) and Estañ et al. 2019, Family 2 (3 siblings, who are the same people as Mroczek's Family D). Counts below are out of the 8 Mroczek patients.

| Phenotype | Suggested HPO | Frequency, onset and notes |
|---|---|---|
| Proximal muscle weakness | HP:0003701 Proximal muscle weakness [cache ✓] | 8/8. Childhood onset, slowly progressive; some stable for decades, then decline in the 40s |
| Neck weakness | HP:0000467 Neck muscle weakness; HP:0003722 Neck flexor weakness [cache ✓] | Most patients |
| Neonatal hypotonia | HP:0001319 Neonatal hypotonia; HP:0001252 Hypotonia [cache ✓] | 6/8 congenital; Family A had childhood onset |
| Delayed walking | HP:0031936 Delayed ability to walk; HP:0001270 Motor delay [cache ✓] | Walking at 18 months to 2.25 years; CIII:3 not walking at 2 years 3 months |
| Gowers sign, Trendelenburg gait | HP:0003391 Gowers sign [cache ✓]; Trendelenburg gait **[verify]** | DII:4, DII:5 |
| Difficulty running | HP:0009046 Difficulty running [cache ✓] | Families A and D |
| Foot dorsiflexor weakness (tibialis anterior) | HP:0009027 Foot dorsiflexor weakness [cache ✓] | AII:2 (foot drop), BII:1 |
| Calf pseudohypertrophy | HP:0003707 Calf muscle pseudohypertrophy [cache ✓] | 6/8 |
| Diffuse muscle atrophy, quadriceps spared on MRI | HP:0003202 Skeletal muscle atrophy [cache ✓] | Abstract states this for all patients; MRI was done in a subset |
| Normal CK | Record as a negative or diagnostic feature; do not bind HP:0003236 | 8/8 normal |
| Obstructive sleep apnoea / respiratory involvement | HP:0002870 Obstructive sleep apnea; HP:0002093 Respiratory insufficiency [cache ✓] | About 5/8. BiPAP in BII:1 (FVC 12%) and DII:3. CIII:1 died aged 17 of respiratory infection |
| Restrictive ventilatory defect | HP:0002091 [cache ✓] | BII:1 |
| Recurrent respiratory infections | HP:0002205 [cache ✓] | CIII:1 |
| Scoliosis / kyphoscoliosis, rigid spine | HP:0002650 Scoliosis, HP:0002751 Kyphoscoliosis [cache ✓]; Rigid spine **[verify]** | 3/8 (BII:1, CIII:1 surgical, DII:3) |
| Contractures | Joint contracture **[verify]** | 2/8 (mild) |
| Joint laxity, scapular winging | **[verify]** | Family A |
| Myopathic EMG | HP:0003458 EMG: myopathic abnormalities [cache ✓] | 6/6 tested |
| Cryptorchidism | HP:0000028 [cache ✓] | DII:3 (Estañ: eldest sibling) |
| Psychiatric comorbidity (depression, bipolar disorder, ADHD) | **[verify]** | Family D, all three. Causal link to FXR1 not established; treat with caution |
| Absent in all patients: facial weakness, ophthalmoplegia, ptosis, cardiac involvement | — | Useful for differential diagnosis against RYR1/SELENON |

**Biopsy phenotypes**

| Finding | Suggested HPO |
|---|---|
| Multi-minicores | HP:0003789 Minicore myopathy [cache ✓] |
| Type 1 fibre predominance | HP:0003803 [cache ✓] |
| Internal or central nuclei | HP:0003687 Centrally nucleated skeletal muscle fibers [cache ✓] |
| Fatty replacement, endomysial or perimysial fibrosis, ring fibres, moth-eaten fibres | — |

On electron microscopy, the minicores are 1–2 sarcomeres long, with Z-band streaming and no mitochondria (PMID:30770808, Family 2; PMID:35393337, DII:4).

Snippet for the results paragraph:
> "Muscle biopsy showed multi-minicores and type I fibre predominance with internalised nuclei." (PMID:35393337)

**Quality of life:** most patients stay ambulant and independent in daily living into adulthood. Family A were walking at 58 and 45. Night-time BiPAP dependence and scoliosis surgery are the main burdens. No formal measures such as SF-36 or EQ-5D have been reported.

---

## 4. Genetic and molecular information

**Gene:** FXR1, at 3q26.33.
- Identifiers: HGNC (hgnc:4023 **[verify]**), NCBI Gene 8087 **[verify]**.
- Protein: an RNA-binding protein of the FMRP family. It has KH domains and an RGG/serine- and arginine-rich intrinsically disordered C-terminus.
- Exon 15 adds 27 amino acids to the muscle-specific isoforms P82 and P84 (isoforms e/f):
  > "In contrast to other tissues, cardiac and skeletal muscle express two FXR1P isoforms that incorporate an additional exon-15." (PMID:30770808)

**Pathogenic variants.** All are frameshifts in exon 15, and all are homozygous.

| Variant | Family / ancestry | Phenotype | Source |
|---|---|---|---|
| c.1707delA, p.(Lys569Asnfs\*57) (XM_005247813.3) | Estañ Family 2 = Mroczek Family D; mixed Argentinian/Turkish; non-consanguineous; three siblings | CMYO9B, mild | PMID:30770808; PMID:35393337 |
| c.1707dupA, p.(Pro570Thrfs\*7) | Family A (British, first-cousin parents) and Family B (Spanish/Galician, non-consanguineous) | CMYO9B, mild to moderate; respiratory failure in BII:1 | PMID:35393337 |
| c.1699dupG, p.(Glu567Glyfs\*10) (OMIM allele .0004) | Family C (Turkish, consanguineous) | More severe: wheelchair use from age 7, death at 17 | PMID:35393337 |
| c.1764_1767delACAG, p.(Arg588Serfs\*37) | Estañ Family 1 (Egyptian, first-cousin parents) | **CMYO9A**, not this disease: fractures, death at 5 months | PMID:30770808 |

- **Classification:** ClinVar classifications were not retrieved **[verify in ClinVar]**.
- **ClinGen:** I found no ClinGen gene-disease validity record. Genomics England PanelApp rates FXR1 Green (biallelic) on the Congenital myopathy panel, as does PanelApp Australia. Per CLAUDE.md, a ClinGen tier must not be invented.
- **Population frequency:** not reported; gnomAD should be checked.
- **Origin:** all germline.

**Functional consequence**
- **Loss of function** of the muscle-specific isoforms. The ubiquitous isoforms, which lack exon 15, are spared, which explains why the disease is restricted to muscle and is non-lethal.
- **Position matters.** In mice, an early frameshift (dupA) triggers nonsense-mediated decay. That leaves about 31% of control mRNA, almost no P82/84 protein, and a milder myopathy.
- **The 3′ delACAG allele (the CMYO9A variant)** escapes much of the decay (about 75% of control mRNA) and produces insoluble, aggregation-prone protein. It gives a more severe phenotype (PMID:30770808).
- Human c.1707delA/dupA sit close to the mouse dupA position, which fits a hypomorphic or null mechanism. This mapping is an inference, not a direct measurement in patient muscle.
- Variability is acknowledged directly:
  > "Phenotypic variability associated with variants in FXR1 can result from differences in variant location and type and is also observed between patients homozygous for the same variant, rendering specific genotype-phenotype correlations difficult." (PMID:35393337; the tool split this sentence into parts, so confirm it as one contiguous sentence in the cache)

**Not reported:** modifier genes, epigenetic changes, chromosomal abnormalities. Family 2 had a 5.98 Mb homozygous region on SNP array.

---

## 5. Environmental information

None. There are no environmental, lifestyle or infectious factors. Leave the section empty or omit it.

---

## 6. Mechanism and pathophysiology

**Causal chain**

1. **Biallelic frameshift in FXR1 exon 15** (germline, homozygous) **leads to** loss of the muscle-specific FXR1P isoforms P82 and P84. Ubiquitous isoforms are unaffected because they skip exon 15 (demonstrated in PMID:30770808).
2. **For early exon-15 frameshifts:** the mutant mRNA **undergoes** nonsense-mediated decay, so muscle has little or no P82/84. *Branch:* the 3′ delACAG allele (CMYO9A) escapes decay and makes insoluble protein that forms cytoplasmic granules containing poly(A) mRNA. That is a toxic, aggregation-type gain added to loss of function, and explains the more severe phenotype (shown in mouse; inferred for humans).
3. **Loss of P82/84 removes FXR1P from its costamere-adjacent striated location at the Z-line**, and so **disrupts** FXR1P's job as a translational repressor and mRNA transporter for structural transcripts. In heart, those include desmoplakin and talin2 (PMID:21659647). Its role in skeletal muscle is inferred.
4. **Costamere and Z-disc organization is disturbed.** Fxr1-null embryos mislocalize vinculin, dystrophin and α-actinin (PMID:15128702 **[verify PMID]**). This **results in** focal sarcomere disorganization: minicores with Z-band streaming and loss of mitochondria.
5. **Myofibre changes:** type 1 fibre predominance, internal nuclei, fatty replacement. Mouse delACAG muscle also shows a p53-pathway transcriptional response (Cdkn1a, Trp63/73, Gdf15 up) (PMID:30770808).
6. **Clinical result:** neonatal hypotonia, proximal, axial and respiratory muscle weakness, and calf pseudohypertrophy. Respiratory weakness **leads to** sleep apnoea or hypoventilation, and axial weakness **leads to** scoliosis.

**Condensate biology, which supports step 2.** The serine- and arginine-rich disordered domain is where muscle-specific splicing acts, and isoforms differ in condensate formation:
> "FXR1 isoforms vary in the formation of RNA-dependent biomolecular condensates in cells and in vitro." (PMID:32328638)

**Suggested terms**

| Kind | Terms |
|---|---|
| GO processes | regulation of translation, negative regulation of translation **[verify]**; mRNA transport GO:0051028 **[verify]**; skeletal muscle tissue development GO:0007519 **[verify]**; sarcomere organization GO:0045214 **[verify]** |
| GO components | costamere GO:0043034 **[verify]**; Z disc GO:0030018 **[verify]**; cytoplasmic ribonucleoprotein granule **[verify]** |
| GO function | mRNA binding **[verify]** |
| Cell types | skeletal muscle fiber CL:0008002 **[verify]**; slow muscle fiber / type 1 **[verify]**; cardiomyocyte (model data only) |
| Scale tags | Steps 1–2 MOLECULAR; 3–5 CELLULAR/TISSUE; 6 ORGANISM |

**Molecular profiling:** the only data set is bulk RNA-seq of P15 muscle from delACAG mice: 233 differentially expressed genes, with the p53 pathway enriched (PMID:30770808). There are no human omics, single-cell or spatial data.

---

## 7. Anatomical structures

- **Primary:** skeletal muscle, especially proximal limb-girdle, neck, axial and respiratory muscles, plus tibialis anterior.
  - UBERON: skeletal muscle tissue UBERON:0001134; diaphragm UBERON:0001103; tibialis anterior UBERON:0001385. All **[verify]**.
- **Relatively spared:** quadriceps femoris.
- **Secondary:** spine (scoliosis) and lung function (restrictive defect).
- **Heart:** clinically normal in every patient so far, even though cardiac muscle also expresses exon-15 isoforms. This is a gap worth recording, because the animal knockdowns do show cardiac phenotypes.
- **Subcellular:** costamere, Z-disc, mitochondria (absent in cores), cytoplasmic RNP granules.
- **Distribution:** bilateral and symmetric.

---

## 8. Temporal development

- **Onset:** congenital or neonatal (6/8); Family A had onset in early childhood.
- **Course:** slowly progressive. Some patients plateau for decades and then decline in mid-adulthood (AII:1 in his 40s; AII:2 developed foot drop in her late teens).
- **Respiratory decline:** can arrive in early adulthood (BII:1 needed ventilation at 20).
- **Duration:** lifelong.
- **Critical periods:** infancy (respiratory distress at birth in some patients), and adolescence (scoliosis and respiratory infections).

---

## 9. Inheritance and population

| Item | Finding |
|---|---|
| Inheritance | Autosomal recessive, HP:0000007 **[verify]**. All reported patients are homozygous |
| Penetrance | Complete in reported homozygotes. Heterozygous parents unaffected |
| Expressivity | Variable, including within families sharing one variant |
| Consanguinity | 3 of 5 families |
| Founder effects | None established. c.1707dupA recurs in an unrelated British and a Spanish family; haplotype not reported |
| Prevalence | Unknown. 11 patients in 4 families for CMYO9B (plus one CMYO9A family). Fits `measure_type: CASES_IN_LITERATURE` with `prevalence_class: ULTRA_RARE` or `NOT_YET_DOCUMENTED` |
| Sex ratio | About 1:1 (5 male, 6 female across the CMYO9B families) |
| Geography and ancestry | British, Spanish, Turkish, Argentinian/Turkish |

---

## 10. Diagnostics

- **Laboratory:** CK is normal. That helps separate this disease from dystrophies.
- **EMG:** myopathic, with low amplitudes. Nerve conduction is normal.
- **Muscle MRI:** diffuse atrophy and fatty infiltration with relative quadriceps sparing; sartorius more affected than gracilis.
- **Biopsy:** multi-minicores, type 1 predominance, internal nuclei. Electron microscopy shows minicores 1–2 sarcomeres long without mitochondria.
- **Respiratory:** FVC and polysomnography are indicated, because sleep apnoea can appear even when FVC is normal.
- **Genetic testing:** exome sequencing was the diagnostic route in every family. FXR1 is on the Genomics England and Australian congenital myopathy panels.
  - Note for curation: exon 15 is a muscle-specific exon, and some reference transcripts (for example NM_005087) **[verify]** may not include it. Variant callers and annotators using a canonical non-muscle transcript can miss or mis-annotate these variants.
- **Differential diagnosis:** multi-minicore myopathies due to RYR1 and SELENON. SELENON shares rigid spine, early respiratory failure and normal CK. RYR1 often causes ophthalmoplegia, which FXR1 patients lack. Also MEGF10, TTN, ACTN2, MYH7 and CCDC78; limb-girdle muscular dystrophies (ruled out by normal CK); spinal muscular atrophy (excluded in Family 1).
- **Screening:** no newborn screening. Carrier testing and prenatal or preimplantation diagnosis are possible once the familial variant is known (Family 1 had prenatal diagnosis).

---

## 11. Outcome and prognosis

- **Survival:** most patients survive into adulthood; the oldest was 58.
- **Deaths:** one, CIII:1 at age 17, from respiratory infection with sepsis.
- **Morbidity:** respiratory insufficiency needing BiPAP, scoliosis needing surgery, loss of running and jumping, and in severe cases wheelchair use.
- **Prognostic factors:** not established, given the variability within a single genotype. The variant position effect (NMD-triggering vs aggregation-prone) separates CMYO9B from CMYO9A.

---

## 12. Treatment

There is no disease-specific therapy and there are no clinical trials. Care is supportive and follows congenital myopathy standards of care.

| Treatment | Suggested NCIT term |
|---|---|
| Non-invasive ventilation (BiPAP) | Supportive Care NCIT:C15747; a ventilation term **[verify]** |
| Physiotherapy | Physical Therapy NCIT:C15302 |
| Scoliosis surgery | Orthopedic Surgical Procedure NCIT:C16186 (CIII:1 had surgery at age 12) |
| Respiratory infection management | — |
| Genetic counseling | NCIT:C15240 |

The NCIT IDs for physical therapy, orthopedic surgery, supportive care and genetic counseling come from CLAUDE.md's common-terms list; still confirm them through `just validate-terms`.

**Mechanism-aimed ideas, none tested:**
- Restoring P82/84.
- Reading-frame-restoring exon-15 approaches. These are speculative, and exon skipping would remove the muscle-specific exon itself.

---

## 13. Prevention

- **Primary:** genetic counseling for consanguineous families; carrier or cascade testing; prenatal or preimplantation diagnosis.
- **Tertiary:**
  - Routine respiratory surveillance (FVC, sleep studies) and early non-invasive ventilation.
  - Scoliosis monitoring.
  - Vaccination against respiratory pathogens, which is general congenital myopathy care rather than FXR1-specific.
  - Cardiac surveillance is reasonable given the animal data, but no human cardiac disease has been reported.

---

## 14. Other species

- I found no naturally occurring FXR1 disease in animals (OMIA not checked; **[verify]**).
- FXR1 is conserved across vertebrates, and the muscle-specific splicing is conserved in Xenopus (PMID:32328638).

---

## 15. Model organisms

| Model | Phenotype | Fidelity to CMYO9B | Source |
|---|---|---|---|
| Mouse Fxr1 exon-15 **dupA** (c.1766dupA, p.Pro590Alafs\*10; CRISPR), homozygous | Viable; mild weight, strength and endurance deficits; few cores; NMD with about 31% mRNA | Moderate: probably closest to human CMYO9B (early NMD-triggering frameshift) | PMID:30770808 |
| Mouse Fxr1 exon-15 **delACAG** (orthologue of the CMYO9A allele) | Viable; low body and muscle mass, weak grip, low bone mineral density, multicore myopathy with central nuclei and type 1 predominance; insoluble P82/84 in RNA granules; p53 signature | Models CMYO9A biology, but non-lethal, unlike the human disease | PMID:30770808 |
| Mouse Myf5-Cre conditional Fxr1 knockout (all isoforms) | Neonatal lethal | Shows isoform requirement; not a model of the specific disease | PMID:30770808 |
| Mouse constitutive Fxr1 KO / hypomorph | KO: neonatal death; disrupted skeletal and cardiac muscle; delocalized vinculin, dystrophin and α-actinin. Hypomorph: reduced limb muscle, lifespan about 18 weeks | Mechanistic (costamere) | PMID:15128702 **[verify]** |
| Mouse Fxr1-null heart | Raised desmoplakin and talin2; desmosome and costamere disruption | Mechanistic, cardiac | PMID:21659647 |
| Zebrafish fxr1 morpholino | Striated muscle and heart development defects, reduced cardiac function | Low: morpholino, cardiac-dominant | PMID:19648401 |
| Xenopus fxr1 splice-isoform manipulation | Muscle-specific splicing required for development | Mechanistic | PMID:32328638 |

**Limitations:**
- None of the mouse models reproduces the human cardiac sparing together with respiratory failure.
- The delACAG mouse is not lethal, whereas the human disease is.
- Model data are only partly comparable to the human data.

---

## Key citations

| PMID | Reference |
|---|---|
| 30770808 | Estañ MC et al. Recessive mutations in muscle-specific isoforms of FXR1 cause congenital multi-minicore myopathy. *Nat Commun* 2019;10:797. doi:10.1038/s41467-019-08548-9 |
| 35393337 | Mroczek M et al. FXR1-related congenital myopathy: expansion of the clinical and genetic spectrum. *J Med Genet* 2022;59(11):1069–1074. PMC9537361 |
| 32328638 | Smith JA et al. FXR1 splicing is important for muscle development and biomolecular condensates in muscle cells. *J Cell Biol* 2020;219(4):e201911129 |
| 21659647 | Whitman SA et al. Desmoplakin and talin2 are novel mRNA targets of fragile X-related protein-1 in cardiac muscle. *Circ Res* 2011;109:262–271 |
| 15128702 **[verify]** | Mientjes EJ et al. Fxr1 knockout mice show a striated muscle phenotype. *Hum Mol Genet* 2004 |
| 19648401 **[verify]** | Van't Padje S et al. Reduction in fragile X related 1 protein causes cardiomyopathy and muscular dystrophy in zebrafish. *J Exp Biol* 2009;212:2564 |

**Before any of this goes into the KB:** fetch each PMID with `just fetch-reference` and copy every snippet from the cached abstract. The tool truncated several of the quotes above.

**Sources:**
- [PubMed 30770808](https://pubmed.ncbi.nlm.nih.gov/30770808/)
- [PMC6377633](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6377633/)
- [PMC9537361](https://pmc.ncbi.nlm.nih.gov/articles/PMC9537361/)
- [JMG article](https://jmg.bmj.com/content/59/11/1069)
- [OMIM #618823](https://omim.org/entry/618823)
- [OMIM #618822](https://omim.org/entry/618822)
- [OMIM *600819](https://www.omim.org/entry/600819)
- [Genomics England PanelApp – FXR1](https://panelapp.genomicsengland.co.uk/panels/225/gene/FXR1)
- [PanelApp Australia – FXR1](https://panelapp-aus.org/panels/141/gene/FXR1/)
- [LOVD disease 06601](https://databases.lovd.nl/shared/diseases/06601)
- [Disease Ontology DOID:0081344](https://disease-ontology.org/term/DOID:0081344)
- [Smith 2020 JCB (PMC7147106)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7147106)
- [Whitman 2011 (PMC3163600)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3163600)
- [Mientjes 2004 record](https://hgsc.bcm.edu/biblio/fxr1-knockout-mice-show-striated-muscle-phenotype-implications-fxr1p-function-vivo)
- [ZFIN van't Padje 2009](https://www.zfin.org/ZDB-PUB-090807-7)

## Reference Validation

Checked with `linkml-reference-validator` 0.4.0.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 6 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 11 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 5 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002091` (1 mention) - the report calls it "cache ✓"; HP calls it **Restrictive ventilatory defect**
- `HP:0002205` (1 mention) - the report calls it "cache ✓"; HP calls it **Recurrent respiratory infections**
- `HP:0000028` (1 mention) - the report calls it "cache ✓"; HP calls it **Cryptorchidism**
- `HP:0003803` (1 mention) - the report calls it "cache ✓"; HP calls it **Type 1 muscle fiber predominance**
- `NCIT:C16186` (1 mention) - the report calls it "CIII:1 had surgery at age 12"; NCIT calls it **Orthopedic Surgical Procedure**
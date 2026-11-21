---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5, claude-opus-5-5
cached: false
start_time: '2026-11-18T23:30:21.539108'
end_time: '2026-11-18T23:44:33.834633'
duration_seconds: 852.3
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Sideroblastic Anemia 4
  mondo_id: MONDO:0008422
  category: Mendelian
  causal_genes: HSPA9
  omim_id: OMIM:182170
  synonyms: sideroblastic anemia, autosomal dominant
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
  - claude-fable-5-2
  - claude-haiku-5-5
  - claude-opus-5-5
  web_search_requests: 8
  num_turns: 50
  total_cost_usd: 1.9805138999999998
  session_id: 337a93b6-93f2-405d-92c8-a594e65874bb
  stop_reason: end_turn
  permission_denials: 1
  denied_tools:
  - Bash
  tool_calls: 49
  retrieval_calls: 48
  assistant_text_blocks: 5
fell_back: true
requested_provider: antigravity
provider_attempts:
- provider: antigravity
  succeeded: false
  error_type: ProviderQuotaError
  remedy: the plan's usage limit is spent
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 12
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 7
  quotes_valid: 4
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:26491070
  - PMC:PMC6318428
  quotes_not_checkable: 1
  relevance_assessed: 14
  on_topic: 8
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 39
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 13
  labels_matching: 9
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0001924
    reported_labels:
    - Lab/clinical sign
    ontology_label: Sideroblastic anemia
  - term_id: HP:0004864
    reported_labels:
    - Lab
    ontology_label: Elevated bone marrow ring sideroblast count
  - term_id: HP:0031965
    reported_labels:
    - Lab
    ontology_label: Increased RBC distribution width
  labels_variant: 1
  unresolvable_prefixes:
  - ORPHA
  - MGI
  - RGD
  service_unreachable: 1
  obsolescence_unchecked: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sideroblastic Anemia 4
- **MONDO ID:** MONDO:0008422 (if available)
- **Causal gene(s):** HSPA9
- **OMIM:** OMIM:182170
- **Synonyms:** sideroblastic anemia, autosomal dominant
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Sideroblastic Anemia 4** covering all of the
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

Collecting follow-up case reports (2021–2024) and model-organism data next.

Checking the 2021 Chinese case and UniProt data, then I'll write.

Gathering a few more ontology IDs; then writing the report.

EBI is reachable again. Fetching the remaining CL, UBERON and NCIT terms.

# Sideroblastic Anemia 4 (SIDBA4; MONDO:0008422; OMIM 182170): HSPA9-related congenital sideroblastic anemia

**Scope and caveats.** This report covers the disease at OMIM 182170 / MONDO:0008422, caused by variants in **HSPA9**. HSPA9 (HGNC:5244) encodes mitochondrial HSP70, also called mortalin or GRP75. The disease name and the synonym "sideroblastic anemia, autosomal dominant" do not match the retrieved evidence. The primary paper found that HSPA9 variants "result in CSA inherited as an autosomal recessive trait" (Schmitz-Abe et al., *Blood* 2015, PMID 26491070, PMC4683334). The key-points statement says HSPA9 mutations "may be inherited in a recessive or pseudodominant manner." The apparent dominant pattern usually reflects one severe loss-of-function allele in trans with a common hypomorphic SNP, rs10117T. That association was only marginal: "a phenotype permutation test yielded P < .07." This report therefore does **not** describe the disease as plain autosomal dominant.

The allelic disorder **EVEN-PLUS syndrome** (OMIM 616854, MONDO:0014801) is biallelic and skeletal/malformation-dominant. It is treated separately and its features are not merged into SIDBA4.

**Retrieval limits.**
- omim.org returned HTTP 403, so OMIM text was not read directly.
- The MedGen record could not be fetched; it is known only from a search snippet.
- No Orphanet code specific to HSPA9 was found.
- ICD-10/11, MeSH, ClinVar per-variant classifications, gnomAD frequencies, prevalence data and ClinicalTrials.gov were not retrieved.
- Several PubMed abstracts (PMIDs 33398880, 36094340) were not available in the retrieved records. Details for them come from curator notes or a preprint snippet and are labeled as such.

---

## 1. Disease Information

**Overview.** SIDBA4 is a congenital sideroblastic anemia (CSA) caused by germline partial loss of function of HSPA9. HSPA9 is a mitochondrial HSP70 chaperone "involved in mitochondrial iron-sulfur cluster biogenesis" (PMID 26491070). The CSAs as a group are "inherited and acquired bone marrow disorders defined by pathological iron accumulation in the mitochondria of erythroid precursors" (Ducamp & Fleming, *Blood* 2019;133:59–69, PMID 30401706, PMC6318428). In that review, HSPA9 deficiency is tabulated as childhood-presenting, mild-to-severe, microcytic-to-normocytic nonsyndromic SA. It notes "HSPA9 mutations are most common, having been described in a dozen families" among the Fe-S-related CSA genes (PMC6318428).

**Identifiers**

| System | ID | Source |
|---|---|---|
| MONDO | MONDO:0008422 (SIDBA4); parent group "Sideroblastic anemia" MONDO:0015194 | Task brief; PanelApp HSPA9 page |
| OMIM (phenotype) | 182170 | PanelApp; UniProt P38646 |
| OMIM (gene) | 600548 | HGNC REST |
| MedGen | Record titled "Autosomal dominant sideroblastic anemia (SIDBA4)"; CUI not retrieved | Search snippet only |
| Orphanet | No HSPA9-specific code found. Group entry Sideroblastic anemia ORPHA:1047; AR congenital SA ORPHA:260305 (snippets, unverified on orpha.net) | Search snippets |
| ICD-10/ICD-11, MeSH | Not retrieved | — |
| UniProt | P38646 (GRP75_HUMAN) | rest.uniprot.org |

**Synonyms.** Sideroblastic anemia 4; SIDBA4; sideroblastic anemia, autosomal dominant; HSPA9-related congenital sideroblastic anemia.

**Evidence source type.** All information is aggregated from published case and family reports and from curated resources (OMIM via UniProt and PanelApp, Genomics England PanelApp). No EHR or registry data exist.

## 2. Etiology

**Cause.** The cause is germline HSPA9 variants: nonsense, frameshift, in-frame deletion, missense and splice-region changes. They act as recessive, *incomplete* loss-of-function alleles. The review describes "recessive incomplete loss-of-function variants" that "often appear to segregate in a pseudodominant pattern" (PMC6318428). It adds that the most severe anemia typically involves a null allele in trans with a mild loss-of-function allele, and that homozygous-null patients have not been described.

**Genetic risk and modifier factors**
- **rs10117 (c.1933C>T, p.L645=, synonymous).** The T allele was in trans with the deleterious allele in "14 of 16 affected individuals from 8 different families." It was in trans in 2 of 5 unaffected carriers, and the permutation P value was < .07 (PMID 26491070).
  - PanelApp's curator summary gives this as "9 of 10 affected individuals in dominant pedigrees." This differs from the verbatim count; prefer the primary paper.
  - Homozygous T/T individuals had about 50% of the HSPA9 mRNA and about 80% of the protein of C/C individuals, with substantial overlap between genotype groups (n = 16/23/12 for mRNA). Splice predictors suggest the C allele sits in an exonic splice enhancer (PMID 26491070).
  - The review gives the minor allele frequency as about 30%. It suggests rs10117T "may be in linkage disequilibrium with the true causative variant" (PMC6318428). gnomAD data were not retrieved.
- **Case enrichment.** 9 of 88 unexplained CSA probands carried rare HSPA9 frameshift, nonsense or missense variants, more often than in EVS and ExAC controls (PMID 26491070).

**Environmental risk factors.** None reported. Not applicable based on the current literature.

**Protective factors.** The rs10117C (ancestral) allele in trans may be protective in carriers of a severe allele. This is inferred from the segregation data above and is not proven. No environmental protective factors are known.

**Gene–environment interactions.** None reported. CTD was not searched.

## 3. Phenotypes

All frequencies are qualitative. The published cohort is about 12 families. No per-phenotype percentages were found.

| Phenotype | Type | HPO | Notes and evidence |
|---|---|---|---|
| Sideroblastic anemia | Lab/clinical sign | HP:0001924 | Defining feature. Severity varies from mild (Dutch pedigree "with mild CSA") to transfusion-requiring (PMID 26491070; PMC6318428). |
| Elevated bone marrow ring sideroblast count | Lab | HP:0004864 | Defining feature of CSA (PMC6318428). Per-patient marrow counts were not available in the extracted text of PMID 26491070. |
| Microcytic anemia | Lab | HP:0001935 (or HP:0004840 Hypochromic microcytic anemia) | MCV about 68–77 fL in several probands; others are normocytic (PMID 26491070 table; PMC6318428). |
| Increased RBC distribution width | Lab | HP:0031965 | RDW about 20–38% in several affected individuals (PMID 26491070 table, via extraction). |
| Anemia severity | Lab | — | Hb about 5.6–9 g/dL in severely affected or transfused individuals; about 12–13 g/dL in some untransfused adults (PMID 26491070 table, via extraction). |
| Transfusion requirement | Clinical | — | Recorded in a minority of patients (D-II-1, D-II-2, C-II-1, L-II-2, M-II-1) (PMID 26491070). |
| Retinitis pigmentosa | Sign | Label only (searched IDs were subtypes; HP:0000510 "Rod-cone dystrophy" is the nearest retrieved) | **Two individuals in one family (family B) only**. Tabulated as associated in PMC6318428. Not established as a general feature. |
| Neutropenia, thrombocytopenia, renal calculi | Lab/sign | HP:0001875, HP:0001873; nephrolithiasis label only | One de novo patient (M-II-1, p.E415K) (PMID 26491070). |
| Syndromic features with congenital anomalies | Sign | — | One Japanese boy with c.1639delA (p.Leu553*) plus rs10117 T/T, described as "syndromic congenital sideroblastic anemia" (PMID 36094340; details from preprint snippet and PanelApp). |

**Onset, progression and expressivity.**
- Onset is in childhood per PMC6318428. The primary paper's cohort ranges in age from 1 to 77 years, and age at onset is not stated.
- Course is presumed chronic and lifelong. No natural-history data exist.
- Expressivity is variable (HP:0003828), and penetrance is incomplete in heterozygotes (HP:0003829). For example, the father in PMID 36094340 carried the same genotype but was not anemic.

**Quality of life.** No EQ-5D, SF-36 or other QoL data were found for this disease.

## 4. Genetic/Molecular Information

**Gene.** HSPA9: HGNC:5244, NCBI Gene 3313, Ensembl ENSG00000113013, 5q31.2, OMIM 600548. Aliases are GRP75, PBP74, mot-2 and mthsp75 (HGNC REST).

**Protein (UniProt P38646).** Stress-70 protein, mitochondrial; 679 amino acids.
- Domains: transit peptide 1–46; nucleotide-binding domain 63–431; linker 432–441; substrate-binding domain 442–679.
- Functions include mitochondrial protein import and folding, and iron-sulfur cluster biogenesis "through stabilization of FXN, NFU1, NFS1, and ISCU."
- Interacts with HSCB, ISCU, FXN and TP53.

HSPA9 lies in the 5q33 critical deletion interval of del(5q) MDS (PMID 26491070).

**Reported SIDBA4 variants (PMID 26491070, unless noted)**

| Family / patient | Variants | Notes |
|---|---|---|
| A (Dutch, apparent AD, mild) | c.409_410del p.(Ile137*) | Truncating |
| B (US, apparent AD) | c.1373_1378del p.(Ile458_Asn459del) | Behaves like a null in yeast |
| C (US) | c.1717C>T p.(Arg573Trp) | Unaffected mother is also a carrier |
| D (German, AR) | c.599C>T p.(Ser200Leu) + c.883_884del p.(Val296*) | Compound heterozygous |
| K (Swedish, AR) | c.1456_1457del p.(Cys487Serfs*3) + c.1729G>A p.(Glu577Lys) | Compound heterozygous |
| L (Danish, AR) | c.883_884del p.(Val296*) + c.609+10A>G (predicted de novo donor site) | Compound heterozygous |
| M-II-1 | c.1243G>A p.(Glu415Lys), de novo | Active site; not tested in yeast |
| Singletons | p.V296*, p.T539K, p.S212P, p.G388S | Inheritance unknown |
| Chinese woman (PMID 33398880) | c.1515+1G>A (exon skipping, NMD) + homozygous rs10117T | From PanelApp curator note; abstract not retrieved |
| Japanese boy (PMID 36094340) | c.1639delA p.(Leu553*) + rs10117 T/T | Father had the same genotype but was not anemic |
| Indian cohort (PMID 38360212) | c.1064T>C p.(Val355Ala) and c.866A>C p.(Glu289Ala), each with p.L645= (rs10117T) in trans | PanelApp notes about 1000-fold reduced mRNA in one patient (curator note, unverified in abstract) |

The cis/trans phasing of rs10117 per family came from a table extraction and should be verified against the original paper.

**Variant type and consequence.** Mostly truncating or null alleles combined with hypomorphic missense or regulatory alleles. In yeast (*ssq1Δ*/*ssc1Δ* complementation), the in-frame deletion p.458_459del was indistinguishable from a null. S200L, T539K, R573W and E577K showed weak or no defects, and S212P and G388S were temperature-sensitive. No variant was dominant-negative in diploid yeast. The mechanism is therefore loss of function or hypomorphism (PMID 26491070).

**ACMG/ClinVar classifications.** Not retrieved. UniProt flags several SIDBA4 missense variants as of uncertain significance. PanelApp rates HSPA9 Green on the Mitochondrial disorders panel (v10.23, 2 Sep 2026), with mode of inheritance "BOTH monoallelic and biallelic." Curators also caution that a single heterozygous variant is not sufficient by itself.

**Origin.** All variants are germline. One de novo variant was reported (p.E415K).

**Somatic relevance.** Somatic del(5q) causes HSPA9 haploinsufficiency in MDS. This is a different entity, and ring sideroblasts are "uncommon" in 5q- syndrome (PMID 26491070).

**Modifier genes.** No modifiers outside HSPA9 are known. The cis modifier is rs10117.

**Epigenetics.** No data.

**Chromosomal abnormalities.** None in germline SIDBA4.

## 5. Environmental Information

No toxic, lifestyle or infectious contributors are reported. This section is not applicable on current evidence.

## 6. Mechanism / Pathophysiology

**Causal chain.** [D] = demonstrated for HSPA9; [I] = inferred from other ISC-defect models or general CSA biology.

1. A germline HSPA9 null allele combined in trans with a hypomorphic allele (missense, splice, or rs10117T-linked low expression) leads to reduced mitochondrial HSPA9 chaperone activity or abundance. [D, from genetics, expression and yeast data in PMID 26491070]
2. Reduced HSPA9 impairs the transfer step of mitochondrial [2Fe-2S] cluster biogenesis. Normally HSPA9 and its co-chaperone HSCB "transfer the nascent 2Fe-2S ISC to mitochondrial glutaredoxin 5 (GLRX5)" from the scaffold ISCU. [I for patients; based on yeast Ssq1 biology and HSCB-CSA data, PMC6318428; PMID 32634119]
3. Fe-S deficiency then branches:
   - **3a.** Cytosolic IRP1 stays in its RNA-binding form and represses translation of *ALAS2* mRNA, which carries a 5′-UTR IRE. This reduces erythroid heme synthesis. [I; supported by the GLRX5 zebrafish *shiraz* model, where an IRE-less *alas2* transgene ameliorated anemia (PMC6318428)]
   - **3b.** Ferrochelatase, an Fe-S enzyme, loses activity, which further blocks heme synthesis. [I; PMC6318428]
   - **3c.** Respiratory chain Fe-S enzymes become dysfunctional, causing mitochondrial dysfunction and oxidative stress. [I for humans; shown in zebrafish *crimsonless* hspa9b mutants, ZFIN ZDB-PUB-050120-2]
4. Impaired heme synthesis with continued iron delivery leads to iron accumulation in erythroblast mitochondria, seen as ring sideroblasts. The review notes the ring sideroblast in ISC defects is probably not a direct mitochondrial effect but reflects IRP1–ALAS2–heme interplay. [I; PMC6318428]
5. As a parallel branch, HSPA9 loss raises TP53 activity, which leads to erythroid progenitor apoptosis and maturation arrest. [D in vitro, in human CD34+ knockdown in the del(5q) context: PMID 28178280; PMID 38508444. Not shown in SIDBA4 patient cells.]
6. Steps 4 and 5 together result in ineffective erythropoiesis, giving microcytic or normocytic, hypochromic anemia with raised RDW. Severity depends on residual HSPA9 dosage (null + rs10117T, or null + missense, versus null + rs10117C). [D at the genotype–phenotype level; PMID 26491070; PMID 36094340]
7. Retinal degeneration (retinitis pigmentosa) occurs in rare cases, as do cytopenias in the de novo E415K case. The mechanism is unknown. [Observed in a few cases only]

**Checklist details**
- **Pathways.** The main pathways are mitochondrial ISC assembly, heme biosynthesis (ALAS2, FECH) and IRP/IRE iron regulation. TP53 signaling is involved in vitro.
- **Protein dysfunction.** The disease results from loss of chaperone function. The EVEN-PLUS missense variants (p.126/p.128) impair ATP hydrolysis and thermostability and increase aggregation (UniProt). Equivalent biochemistry has not been reported for the SIDBA4 alleles.
- **Immune involvement.** None in humans. Hspa9+/- mice show reduced B-progenitor colony formation and attenuated IL-7/Stat5 signaling (PMID 25550197).
- **Omics, single-cell and CRISPR data.** None found.

**Suggested GO terms (from UniProt P38646)**
- Iron-sulfur cluster assembly (GO:0016226)
- Erythrocyte differentiation (GO:0030218)
- Protein import into mitochondrial matrix (GO:0030150)
- Negative regulation of apoptotic process (GO:0043066)
- Protein folding chaperone (GO:0044183)
- ATP hydrolysis activity (GO:0016887)

**Suggested CL terms**
- Erythroblast (CL:0000765)
- Basophilic, polychromatophilic and orthochromatic erythroblasts (CL:0000549, CL:0000550, CL:0000552)
- Erythrocyte (CL:0000232)

## 7. Anatomical Structures Affected

- **Primary organ.** Bone marrow (UBERON:0002371), specifically the erythroid lineage. The body system is hematopoietic.
- **Secondary.** Retina (UBERON:0000966) in rare cases. Iron overload from transfusion or ineffective erythropoiesis is expected but was not documented in the retrieved HSPA9 sources.
- **Cells.** Erythroblasts (CL:0000765) and their red cell progeny (CL:0000232).
- **Subcellular.** Mitochondrial matrix (GO:0005759), mitochondrial inner membrane (GO:0005743) and the TIM23 complex (GO:0005744) (UniProt).
- **Lateralization.** Not applicable. Retinitis pigmentosa, where present, was not described as lateralized in the retrieved text.

## 8. Temporal Development

- **Onset.** Childhood (PMC6318428), with a congenital genetic basis. Some carriers are diagnosed in adulthood, and the cohort spans ages 1–77 (PMID 26491070).
- **Pattern.** Chronic and insidious.
- **Progression and stages.** No staging system exists, and no natural-history data were found. Remission has not been reported.

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive (HP:0000007) with pseudodominant segregation. The usual genotype is a severe allele in trans with rs10117T, and some families are true compound heterozygotes (PMID 26491070; PMC6318428). PanelApp lists the mode of inheritance as "BOTH monoallelic and biallelic."
- **Penetrance.** Incomplete for single severe alleles, which depends on the trans allele (example: the unaffected father in PMID 36094340).
- **Expressivity.** Variable.
- **Anticipation, mosaicism, founder effects, consanguinity.** No anticipation. No mosaicism reported. Recurrent c.883_884del p.(Val296*) appears in families D and L and in singleton AM. The EVEN-PLUS literature suggests a related c.882_883delAG may be more common in East Asians (PMID 36052765). No founder effect has been established.
- **Epidemiology.** No prevalence or incidence data were found. About a dozen families are described (PMC6318428). Reported patients are European/White (Dutch, German, Swedish, Danish, US), Asian (Chinese, Japanese) and Indian (PMID 38360212). Sex ratio is not determinable and both sexes are affected.
- **Carrier frequency.** The rs10117T allele is about 30% (PMC6318428). Carrier frequency of rare severe alleles was not retrieved.

## 10. Diagnostics

- **Laboratory.**
  - CBC with MCV and RDW.
  - Bone marrow aspirate with Perls (Prussian blue) stain for ring sideroblasts, which define CSA (PMC6318428).
  - Iron studies (ferritin, transferrin saturation) are standard. No HSPA9-specific data were found.
- **Genetic testing.**
  - Use an NGS CSA or mitochondrial panel or exome. HSPA9 is Green on Genomics England panels (PanelApp 112).
  - Sequencing must also **genotype or phase rs10117 (c.1933C>T)**, because a single heterozygous rare variant is not diagnostic alone (PanelApp curator comment).
  - Large cohort NGS identifies CSA genes efficiently. In one Indian cohort, 23 of 41 cases received a molecular diagnosis, and "Congenital sideroblastic anemia was the most common diagnosis (14/23; 61%)," mostly due to ALAS2, with HSPA9 cases included (PMID 38360212).
- **Functional confirmation.** Yeast *ssq1Δ/ssc1Δ* complementation assays have been used, with acknowledged limitations (PMID 26491070). RT-qPCR of HSPA9 mRNA has been used for splice and NMD alleles (PMID 36094340; PMID 38360212, per PanelApp).
- **Differential diagnosis** (genes per PMC6318428):
  - X-linked SA (ALAS2): pyridoxine-responsive.
  - SLC25A38-SA: severe and transfusion-dependent.
  - GLRX5- and HSCB-CSA: other Fe-S defects (HSCB, PMID 32634119).
  - XLSA with ataxia (ABCB7).
  - Syndromic CSAs (TRNT1/SIFD, SLC19A2/TRMA, Pearson syndrome).
  - Acquired MDS with ring sideroblasts.
  - Iron deficiency anemia, an important confounder in microcytic presentations (PMID 38360212).
- **CMA, karyotype, FISH, repeat-expansion and mtDNA testing.** Not indicated for HSPA9 itself. mtDNA testing is relevant to rule out Pearson syndrome.
- **Screening.** No newborn screening. Cascade testing of relatives is reasonable but no formal guidance was found.

## 11. Outcome/Prognosis

- No survival or mortality data were found.
- Many adults are mildly affected and some have near-normal Hb. A subset is transfusion-requiring (PMID 26491070).
- **Prognostic factors.** The main factor is genotype dosage: a null allele in trans with rs10117T or a hypomorphic missense allele gives more severe disease (PMC6318428). In an Indian cohort spanning CSA genes, frameshift, nonsense and splice variants were associated with younger presentation (PMID 38360212). That observation is not specific to HSPA9.
- No QoL data were found.

## 12. Treatment

No HSPA9-specific treatment studies or trials were found. ClinicalTrials.gov was not searched. Management is extrapolated from CSA generally (PMC6318428). Pyridoxine response is documented for XLSA but **not** reported for HSPA9.

| Intervention | NCIT / CHEBI | Evidence status |
|---|---|---|
| Packed red blood cell transfusion | NCIT:C15409 | Used in some HSPA9 patients (PMID 26491070 table) |
| Iron chelation for transfusional or secondary iron overload | NCIT:C40516 "Iron Chelation"; NCIT:C360 "Chelating Agent" | Standard CSA practice; the retrieved portion of PMC6318428 did not discuss it (last third unread) |
| Pyridoxine trial | CHEBI:16709 | Effective in many XLSA patients; no HSPA9 response data |
| Hematopoietic stem cell transplantation | NCIT ID not retrieved | Not reported for HSPA9 |

Gene, RNA and targeted therapies have not been reported. Pharmacogenomics is not applicable.

## 13. Prevention

- No primary prevention exists.
- Genetic counseling should explain pseudodominant risk. The phenotype of an offspring carrying a familial severe allele depends on the allele (rs10117C or T) inherited from the other parent. This is inferred from PMID 26491070 and PMID 36094340.
- Cascade testing and prenatal or preimplantation testing are technically possible once variants are known. No guidelines were retrieved.
- Tertiary prevention is iron-overload monitoring, which is general CSA practice and not HSPA9-specific in the retrieved sources.

## 14. Other Species / Natural Disease

- No naturally occurring HSPA9 sideroblastic anemia in animals was found (OMIA not searched).
- Orthologs:
  - Mouse *Hspa9*: MGI:96245 (HGNC); also RGD:1311806.
  - Zebrafish *hspa9b*: *crimsonless* (ZFIN ZDB-PUB-050120-2).
  - Yeast *SSQ1* and *SSC1* (PMID 26491070).
- The ISC chaperone function is conserved from yeast to human.

## 15. Model Organisms

| Model | Key findings | Recapitulation |
|---|---|---|
| Zebrafish *crimsonless* (*hspa9b*, Gly→Glu in substrate-binding domain) | Anemia, dysplasia, excess blood-cell apoptosis and multilineage cytopenia. The authors describe it as closely recapitulating "the ineffective hematopoiesis of MDS"; mitochondrial dysfunction causes oxidative stress in blood cells (Craven et al., *Blood* 2005;105:3528–34; ZFIN ZDB-PUB-050120-2; PMID not retrieved) | Models ineffective erythropoiesis. Ring sideroblasts were not reported in the retrieved abstract. |
| Mouse *Hspa9*+/- (PMID 25550197) | "Hspa9(+/-) mice have normal basal hematopoiesis and do not develop MDS"; reduced B-progenitor colonies and Stat5 signaling. PanelApp notes homozygous knockout is embryonic lethal (curator note). | Poor. No anemia or sideroblasts, consistent with heterozygosity alone being insufficient. |
| Yeast *ssq1Δ/ssc1Δ* complementation (PMID 26491070) | Graded allele severity; no dominant-negative effect | Allele-function assay only |
| Human CD34+ HSPA9 knockdown or inhibition (PMID 28178280; PMID 38508444) | TP53-dependent apoptosis and impaired erythroid maturation; partial rescue by TP53 knockdown | Erythroid defect; del(5q) MDS context |

Limitations of current models:
- No compound-heterozygous or hypomorph mouse exists.
- No ring-sideroblast model for HSPA9 has been reported.
- Patient iPSC-derived erythroid models were not found.

---

### Sources
- Schmitz-Abe K et al. *Blood* 2015;126:2734–8. PMID 26491070; [PMC4683334](https://pmc.ncbi.nlm.nih.gov/articles/PMC4683334/)
- Ducamp S, Fleming MD. *Blood* 2019;133:59–69. PMID 30401706; [PMC6318428](https://pmc.ncbi.nlm.nih.gov/articles/PMC6318428/)
- [Genomics England PanelApp, HSPA9 (panel 112)](https://panelapp.genomicsengland.co.uk/panels/112/gene/HSPA9/)
- [UniProt P38646](https://rest.uniprot.org/uniprotkb/P38646.txt); [HGNC HSPA9](https://rest.genenames.org/fetch/symbol/HSPA9)
- Li S et al. *Clin Genet* 2021. PMID 33398880
- Watanabe A et al. *Pediatr Blood Cancer* 2023. PMID 36094340; [Authorea preprint](https://authorea.com/users/320370/articles/565557-hspa9-frameshift-and-loss-of-function-mutations-in-a-patient-manifesting-syndromic-sideroblastic-anemia-and-various-congenital-anomalies)
- Sharma P et al. *J Mol Diagn* 2024. PMID 38360212
- Krysiak K et al. *Exp Hematol* 2015. PMID 25550197
- Liu T et al. *PLoS One* 2017. PMID 28178280; [PMC5298293](https://pmc.ncbi.nlm.nih.gov/articles/PMC5298293/)
- Butler et al. *Cell Stress Chaperones* 2024. PMID 38508444; [PMC10998001](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10998001/)
- Crispin A et al. *J Clin Invest* 2020. PMID 32634119
- Craven SE et al. *Blood* 2005. [ZFIN ZDB-PUB-050120-2](https://zfin.org/ZDB-PUB-050120-2)
- EVEN-PLUS (allelic): PMIDs 26598328, 32869452, 35779070, 36052765
- [MedGen snippet](https://ncbi.nlm.nih.gov/medgen/C0221018)
- Ontology lookups: [JAX HPO API](https://ontology.jax.org/api/hp/search?q=sideroblastic) and [EBI OLS4](https://www.ebi.ac.uk/ols4/)

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 7 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 3 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 14 |
| On topic | 8 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:26491070` *(abstract only)*: "involved in mitochondrial iron-sulfur cluster biogenesis"
  - closest text in source: "Here we demonstrate that mutations in HSPA9, a mitochondrial HSP70 homolog located in the chromosome 5q deletion syndrome 5q33 critical deletion interval and involved in mitochondrial Fe-S biogenesis, result in CSA inherited as an autosomal recessive trait"
- `PMC:PMC6318428` *(abstract only)*: "often appear to segregate in a pseudodominant pattern"
  - Text part not found as substring: 'often appear to segregate in a pseudodominant pattern' (note: only abstract available for PMID:30401706, full text may contain this excerpt)
- `PMC:PMC6318428` *(abstract only)*: "may be in linkage disequilibrium with the true causative variant"
  - Text part not found as substring: 'may be in linkage disequilibrium with the true causative variant' (note: only abstract available for PMID:30401706, full text may contain this excerpt)

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMID:36094340`: "syndromic congenital sideroblastic anemia"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 39 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 13 |
| Terms named correctly | 9 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0001924` (1 mention) - the report calls it "Lab/clinical sign"; HP calls it **Sideroblastic anemia**
- `HP:0004864` (1 mention) - the report calls it "Lab"; HP calls it **Elevated bone marrow ring sideroblast count**
- `HP:0031965` (1 mention) - the report calls it "Lab"; HP calls it **Increased RBC distribution width**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0003828` (1 mention) - the report calls it "Expressivity is variable"; HP calls it **Variable expressivity**

### Terms the ontology service could not be reached for

1 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `CHEBI:16709` (1 mention)

### Terms whose obsolescence could not be checked

1 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `NCIT:C360` (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`, `RGD`.
---
provider: claude_code
model: claude-fable-5-2, claude-haiku-5-5
cached: false
start_time: '2026-11-26T22:30:21.047547'
end_time: '2026-11-26T22:44:12.031149'
duration_seconds: 830.98
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: Hypogonadotropic Hypogonadism 7 With or Without Anosmia
  mondo_id: MONDO:0007794
  category: Mendelian
  causal_genes: GNRHR
  omim_id: OMIM:146110
  synonyms: hypogonadotropic hypogonadism 7 without anosmia
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
  web_search_requests: 10
  num_turns: 1
  total_cost_usd: 3.8042228700000007
  session_id: 99183a91-21ce-4c2a-96b4-98c6b0010f69
  stop_reason: end_turn
  tool_calls: 257
  retrieval_calls: 257
  assistant_text_blocks: 8
citation_count: 9
reference_validation:
  total_references: 73
  verified: 72
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.014
  quotes_checked: 21
  quotes_valid: 20
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:12364481
  relevance_assessed: 72
  on_topic: 60
  unresolved_references:
  - PMID:16968799
  needs_review: true
  validator_version: 0.8.0
term_validation:
  total_terms: 89
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 77
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 0
  labels_mismatched: 8
  mislabelled_terms:
  - term_id: HP:0000044
    reported_labels:
    - hp
    - Lab / clinical
    ontology_label: Hypogonadotropic hypogonadism
  - term_id: HP:0000798
    reported_labels:
    - hp
    ontology_label: Oligozoospermia
  - term_id: HP:0003251
    reported_labels:
    - hp
    ontology_label: Male infertility
  - term_id: HP:0008222
    reported_labels:
    - hp
    ontology_label: Female infertility
  - term_id: HP:0040171
    reported_labels:
    - hp
    ontology_label: Decreased serum testosterone concentration
  - term_id: HP:0030341
    reported_labels:
    - hp
    ontology_label: Decreased circulating follicle stimulating hormone concentration
  - term_id: HP:0008214
    reported_labels:
    - hp
    ontology_label: Decreased serum estradiol
  - term_id: HP:0003187
    reported_labels:
    - hp
    - Sign
    ontology_label: Breast hypoplasia
  service_unreachable: 76
  obsolescence_unchecked: 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypogonadotropic Hypogonadism 7 With or Without Anosmia
- **MONDO ID:** MONDO:0007794 (if available)
- **Causal gene(s):** GNRHR
- **OMIM:** OMIM:146110
- **Synonyms:** hypogonadotropic hypogonadism 7 without anosmia
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **Hypogonadotropic Hypogonadism 7 With or Without Anosmia** covering all of the
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

Core literature and identifiers are retrieved; I'm filling a few remaining gaps (OMIM clinical details, reversal, epidemiology, knockout models) before writing the report.

One last lookup is running (OMIM entry details and exact cohort figures); meanwhile I'm checking a few remaining points on treatment and diagnostics.

**Summary:** Tasks 1, 2, 3 and 6 returned content. Tasks 4 and 5 failed: both PMC pages returned a bot-check page, not the article. Several OMIM details (Clinical Features, .0010 onward, animal model) come only from the fetch tool's model-extracted summaries, and those are marked "(summary)" below.

## 1. OMIM 146110 (HH7), via the mirror

Read: https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/omim/146110 (offsets 0, 39861, 179722). The mirror worked, so the MedGen fallback was not used. Not read: the reference list (only inline PMIDs seen) and roughly the last 100k characters.

- **Title:** "HYPOGONADOTROPIC HYPOGONADISM 7 WITH OR WITHOUT ANOSMIA; HH7". Alternative titles: "HYPOGONADISM, ISOLATED HYPOGONADOTROPIC" and "IDIOPATHIC HYPOGONADOTROPIC HYPOGONADISM; IHH".
- **Phenotype-gene table:** 4q13.2, gene GNRHR (138850), listed as "Hypogonadotropic hypogonadism 7 without anosmia". Mapping key 3 (molecular basis known).
- **Inheritance:** autosomal recessive (HP:0000007).
- **Description (summary):** congenital IHH is absent or incomplete sexual maturation by age 18, with low gonadotropins and testosterone. It is Kallmann syndrome when anosmia is present and normosmic IHH otherwise.
- **Clinical Features (all summary, not verbatim):**
  - de Roux et al. 1997 (PMID 9371856): brother and sister, normosmic. Proband a 22-year-old 46,XY male, puberty at 16, testes 8 mL each. Sister 37 years old, primary amenorrhea and infertility, with two pregnancies after ovulation induction.
  - Caron et al. 1999 (PMID 10084584): three sibs. Two brothers had microphallus, bilateral cryptorchidism and no puberty. Sister had primary amenorrhea and no puberty. Partial resistance to pulsatile GnRH.
  - Pitteloud et al. 2001 (PMID 11397842): 26-year-old male, the "fertile eunuch" variant. Testis volume 17 mL. Four months of chorionic gonadotropin alone produced sperm and his wife conceived. After treatment stopped, testosterone normalized and pulsatile LH appeared (spontaneous reversal).
  - de Roux et al. 1999 (PMID 10022417): proband a 30-year-old male with complete HH. Sisters aged 18 and 24 had partial HH with primary amenorrhea and normal breast development.
  - Kottler et al. 2000 (PMID 10999776): woman with complete HH (see Molecular Genetics).
- **Molecular Genetics (verbatim):**
  - Kottler 2000: Q106R plus L314X (.0007), complete HH in a woman.
  - Pitteloud 2001: homozygous R262Q in a 26-year-old male with mild HH.
  - Costa 2001 (PMID 11397871): 17 Brazilian normosmic patients from 14 families. Homozygous R139H (.0008) in a female with complete HH. Compound heterozygous Q106R plus N10K (.0009) in sibs with partial HH. The mirror text gives "3 sibs" in one passage and "4 sibs" in another.
  - Silveira 2002 (PMID 12050282): homozygous splice-acceptor variant (.0011) in a woman with primary amenorrhea. No spontaneous pulsatility; exogenous gonadotropins gave a normal pregnancy.
  - Meysing 2004 (PMID 15240592): compound heterozygous .0013 and .0014 in a normosmic woman.
  - Lin 2006 (PMID 16968799): homozygous R262Q in two brothers with delayed puberty.
  - Layman 1998 (PMID 9425890), summary: R262Q plus Y284C in one family with four affected sibs.
  - Caron 1999 and de Roux 1999, summary: R262Q plus A129D, and Q106R plus S217R.
  - Kottler 1999, summary: Q106R and R262Q were frequent across regions.
  - Pralong 1999 (PMID 10523035), summary: homozygous S168R in a male with complete HH.
- **Digenic/oligogenic case with FGFR1 (verbatim):** Seminara 2000 (PMID 10690855) described two sisters with primary amenorrhea and no breast development at 25 and 18, compound heterozygous for Q106R and R262Q. Pitteloud 2007 (PMID 17235395) reexamined the family and found a heterozygous FGFR1 variant (136350.0016) in both sisters and their father, who had delayed puberty. An unaffected daughter carried only the FGFR1 variant. Two prepubertal twin sons each carried one GNRHR mutation and no FGFR1 variant. The authors proposed that the two genes synergize.
- **Anosmia:** none of the described molecular cases is anosmic. Costa 2001 states all its patients had a normal sense of smell. Bhagavath 2005 (PMID 16213849) found no GNRHR mutations in hyposmic or anosmic HH patients. Caronia 2011 (PMID 21247312) found one heterozygous GNRHR mutation among women with functional hypothalamic amenorrhea.
- **Population genetics (verbatim):** Beranova 2001 (PMID 11297587): 2 of 5 (40%) in recessive normosmic families and 3 of 18 (16.7%) in sporadic normosmic cases. Bhagavath 2005: 3 of 185 HH patients (1.6%) compound heterozygous. The authors estimated GNRHR accounts for about 3.5% of normosmic HH and 7 to 11% of presumed recessive HH.
- **Clinical Synopsis (verbatim):** inheritance autosomal recessive. Normal sense of smell. Delayed or absent thelarche and gynecomastia. Male: small penis, small testes, cryptorchidism, infertility in some. Female: infertility in some, primary amenorrhea. Sparse to absent male facial, axillary and pubic hair. Puerile voice. Isolated hypogonadotropic hypogonadism, delayed or absent puberty.
- **References:** inline PMIDs seen include 9371856, 10084584, 11397842, 10022417, 10999776, 9425890, 10714361, 10523035, 11397871, 12050282, 15240592, 16968799, 10690855, 17235395, 21247312, 11297587, 16213849 and 12107234 (Janovick 2002, summary). The full list was not read.

## 2. OMIM 138850 (GNRHR)

Read: https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/branch/main/www.ncbi.nlm.nih.gov/omim/138850 (offsets 0, 39897, 79794, 119691, 179794). The animal model section was not found in any part read; the summaries say it is absent from the visible text.

- **Names and location:** alternative titles GNRHR1, GRHR, LUTEINIZING HORMONE-RELEASING HORMONE RECEPTOR; LHRHR. Cytogenetic location 4q13.2; GRCh38 4:67,737,118-67,754,388.
- **Gene structure (verbatim):** Fan 1994 (PMID 7958384): three exons spanning over 18.9 kb, introns of 4.2 and 5.0 kb within the coding region, single copy by Southern blot. Fan 1995 (PMID 7768323): mRNA about 5 kb, coding region 987 bp, large 5' and 3' UTRs with multiple start sites and polyadenylation signals. Grosse 1997 (PMID 9259321): a splice variant from a cryptic 3' site in exon 2 carries a 128-bp deletion. It is incapable of ligand binding and signaling and impairs wildtype receptor signaling when co-expressed.
- **Mapping (verbatim):** Kaiser 1994 (PMID 8034328): 4q13.1-q21.1, mouse chromosome 5. Fan 1994: chromosome 4. Morrison 1994 (PMID 8005601): 4q13.2-q13.3. Leung 1995 (PMID 7613048): 4q21.2. Kottler 1995 (PMID 7557974): between D4S409 and D4S392 and colocalizes with KIT (4q12). Kakar and Neill 1995 (PMID 7789173): 4q13.
- **Gene function (verbatim):** a G protein-coupled receptor on pituitary gonadotropes that transduces GnRH signals and modulates LH and FSH synthesis and secretion. Szende 1991 (PMID 1851995) found high-affinity LHRH binding in pancreatic tumor cell nuclei. Maji 2009 (PMID 19541956) reported peptide hormones, including GnRH, stored in secretory granules in an amyloid-like conformation.
- **Allelic variants:** the entry shows "14 Selected Examples". Headers .0001 to .0009 were read verbatim and all carry "HYPOGONADOTROPIC HYPOGONADISM 7 WITHOUT ANOSMIA". The rest is summary-derived.

| No. | Change | Phenotype and reference |
|---|---|---|
| .0001 | Gln106Arg (Q106R) | Compound het with R262Q; de Roux 1997 (PMID 9371856). Binding markedly reduced but not eliminated. |
| .0002 | Arg262Gln (R262Q) | De Roux 1997; also Layman 1998, Caron 1999, Seminara 2000, Lin 2006 (summary). |
| .0003 | Tyr284Cys (Y284C) | Compound het with R262Q in 4 sibs; Layman 1998 (PMID 9425890). At least one affected female ovulated with exogenous gonadotropins. |
| .0004 | Ala129Asp (A129D) | Compound het with R262Q in 3 sibs with isolated HH; Caron 1999 (PMID 10084584). |
| .0005 | Ser217Arg (S217R) | Same allele as Q106R; de Roux 1999 (PMID 10022417). |
| .0006 | Ser168Arg (S168R) | Homozygous in a male with complete HH; Pralong 1999 (PMID 10523035). |
| .0007 | Leu314Ter (L314X) | Compound het with Q106R in a woman with complete HH; Kottler 2000 (PMID 10999776). |
| .0008 | Arg139His (R139H) | Homozygous in a Brazilian woman with complete HH; Costa 2001 (PMID 11397871). |
| .0009 | Asn10Lys (N10K) | Compound het with Q106R in 4 Brazilian sibs with partial HH; Costa 2001. |
| .0010 | Glu90Lys (E90K) | Summary: 2 sibs with complete HH; Soderlund 2001, Maya-Nunez 2002. |
| .0011 | IVS1 G-A -1 splice | Summary: homozygous woman; Silveira 2002. |
| .0012 | Ala171Thr (A171T) | Summary: compound het with Q106R in 2 brothers with severe HH; Karges 2003. |
| .0013 | Asn10Lys + Gln11Lys | Summary: normosmic woman, compound het with .0014; Meysing 2004 (PMID 15240592). |
| .0014 | Pro320Leu (P320L) | Summary: as .0013. |

- **Animal model:** not located. The summaries report only a See Also entry, Mason et al. 1986, on the hpg mouse (a GnRH gene deletion, not the receptor). Treat this as unconfirmed.

## 3. PubMed search and efetch

The esearch returned Count = 1 and one hit, PMID 20068010.

- **Citation:** Wu S, Wilson MD, Busby ER, Isaac ER, Sherwood NM. Endocrinology. 2010 Mar;151(3):1142-52. doi:10.1210/en.2009-0598.
- **Title:** "Disruption of the single copy gonadotropin-releasing hormone receptor in mice by gene trap: severe reduction of reproductive organs and functions in developing and adult mice."
- **Key findings (abstract):**
  - A gene-trap insertion in intron 1 disrupted exons 2 and 3 and carried a lacZ reporter.
  - Null mice had small sexual organs, low FSH, LH and steroid hormones, failed sexual maturation, were infertile, and did not respond to exogenous GnRH.
  - Morula/blastocyst development, implantation, fetal male masculinization and early pregnancy maintenance were not prevented.
  - The phenotype was more severe than the ENU-induced Gnrhr mutant, Kiss1 knockout and Gpr54 knockout.
  - Adult null mice showed complete cessation of reproduction.

## 4. PMC5527354

Failed. The fetch returned HTTP 200 with a 176-character "Checking your browser - reCAPTCHA" page and no article text. No citation, cohort size, mutation counts, phenotype findings or frequency ranges were obtained. This is a bot check, so repeating the request will likely fail the same way.

## 5. PMC3888824

Failed. Same reCAPTCHA page (HTTP 200, 176 characters). Nothing was obtained.

## 6. Six PubMed abstracts (efetch, one call)

Non-preapproved source. Quotes are under 125 characters.

- **PMID 38196663:** Axiak CJ et al. J Endocr Soc 2023;8(2):bvad172. "High Population Frequency of GNRHR p.Q106R in Malta."
  - Maltese newborn cord-blood minor allele frequency for Q106R was 0.029 (n = 493), about 10 times the global 0.003.
  - Of 978 adults (739 men, 239 women), 43 were heterozygotes (26 men, 17 women). Hormones and fertility were normal except TSH, lower in men aged 50 or older.
  - Quote: "Out of 978 adults, 43 GNRHR p.Q106R heterozygotes (26 men and 17 women) were identified."
  - Quote: "GNRHR p.Q106R is likely a founder variant".
- **PMID 25016926:** Beneduzzi D et al. Fertil Steril 2014;102(3):838-846.e2. "Role of gonadotropin-releasing hormone receptor mutations in patients with a wide spectrum of pubertal delay."
  - 110 normosmic IHH patients (74 male) and 50 with constitutional delay (CDGP).
  - 11 IHH patients (10%) had biallelic GNRHR mutations. Novel p.Y283H and p.V134G were completely inactivating. Brazilian p.R139H carriers shared a haplotype.
  - One CDGP boy was heterozygous for Q106R, not considered pathogenic.
  - Quote: "Eleven IHH patients (10%) carried biallelic GNRHR mutations."
  - Quote: "varied from complete GnRH deficiency to partial and reversible IHH".
- **PMID 22745237:** Gianetti E et al. J Clin Endocrinol Metab 2012;97(9):E1798-807. "When genetic load does not correlate with phenotypic spectrum."
  - 863 probands, 46 family members and 422 controls screened. 70 carriers (32 patients, 38 family members) were grouped G1 to G4.
  - Heterozygous rare variants were more prevalent in probands than controls (P < 0.01). In biallelic G1 to G3, the phenotype tracked genetic load. In monoallelic G4, phenotypes were more diverse.
  - Quote: "The 70 subjects (32 patients and 38 family members) harboring mutations".
  - Quote: "as-yet-unidentified genetic and/or environmental factors may combine with singly mutated GNRHR alleles".
- **PMID 11297587:** Beranova M et al. J Clin Endocrinol Metab 2001;86(4):1580-8. "Prevalence, phenotypic spectrum, and modes of inheritance of gonadotropin-releasing hormone receptor mutations in idiopathic hypogonadotropic hypogonadism."
  - 108 probands: 48 normosmic, 60 anosmic or hyposmic. Five normosmic probands (3 men, 2 women) had changes.
  - 2 of 5 (40%) in a recessive subgroup of 5 kindreds. 3 of 18 (16.7%) in sporadic normosmic cases.
  - Three compound heterozygous and two homozygous. Of 8 sequence changes, 4 were novel.
  - Quote: "establishing a GNRHR mutation frequency of 2 of 5 (40%)".
  - Quote: "indicating a prevalence of 3 of 18 (16.7%) in patients with sporadic IHH".
- **PMID 26194704:** Boehm U et al. Nat Rev Endocrinol 2015;11(9):547-64. European Consensus Statement on congenital hypogonadotropic hypogonadism.
  - More than 25 causal genes. Anosmia or hyposmia in about 50% of CHH (Kallmann syndrome).
  - About 10 to 20% of patients show spontaneous recovery of reproductive function.
  - Quote: "with >25 different causal genes identified to date".
  - Quote: "∼10-20% of patients exhibit a spontaneous recovery of reproductive function".
- **PMID 30698671:** Young J et al. Endocr Rev 2019;40(2):669-710. "Clinical Management of Congenital Hypogonadotropic Hypogonadism."
  - Mutations in more than 30 genes. About 10% to 20% of male patients show spontaneous recovery. Fertility can be induced in most patients.
  - Quote: "mutations in >30 genes identified to date".
  - Quote: "a notable portion of male patients (∼10% to 20%) exhibit a spontaneous recovery".

None of the six abstracts gives a sex ratio or a general prevalence figure.

**URLs read:** the OMIM 146110 mirror (offsets 0, 39861, 179722); the OMIM 138850 mirror (offsets 0, 39897, 79794, 119691, 179794); the esearch URL; the efetch URL for PMID 20068010; the efetch URL for the six PMIDs. The PMC pages (PMC5527354, PMC3888824) were fetched but returned only the bot-check page.

Research is nearly complete; I'm doing one final lookup to verify ontology term IDs, then writing the report.

The ontology-ID verification lookup is running in the background; I'll write the final report once it returns.

Most of this batch resolved. Three URLs returned HTTP 500 (NCIT Testosterone, NCIT Gonadorelin, MONDO Kallmann syndrome), and I won't retry them. Two NCIT searches still need follow-up: "Chorionic Gonadotropin" returned a non-matching label, and "Ovulation Induction" returned 0 exact hits, so I'll run the alternate and the fallback for those.

All requested OLS4 lookups are done. Every ID below comes from an OLS4 response; none is from memory. Five URLs returned HTTP 500 and were not retried, per the failure rules.

## Results

The search pattern was `https://www.ebi.ac.uk/ols4/api/search?q=<label>&ontology=<ont>&exact=true&rows=3&fieldList=obo_id,label`. Fallback and alternate queries are noted where used. "Exact label returned" is the `label` field from the response; where it differs from the request, the row says so.

### HP

| Requested label | Ontology | obo_id | Exact label returned |
|---|---|---|---|
| Delayed puberty | hp | HP:0000823 | Delayed puberty |
| Absent pubertal development | hp | not found | exact: 0 hits; fallback (exact=false, rows=5): 0 hits |
| Pubertal failure (alt) | hp | not found | 0 hits |
| Absence of secondary sex characteristics (alt) | hp | HP:0008187 | Absence of secondary sex characteristics |
| Hypogonadotropic hypogonadism | hp | HP:0000044 | Hypogonadotropic hypogonadism |
| Primary amenorrhea | hp | HP:0000786 | Primary amenorrhea |
| Secondary amenorrhea | hp | HP:0000869 | Secondary amenorrhea |
| Micropenis | hp | HP:0000054 | Micropenis |
| Cryptorchidism | hp | HP:0000028 | Cryptorchidism |
| Decreased testicular size | hp | HP:0008734 | Decreased testicular size |
| Azoospermia | hp | HP:0000027 | Azoospermia |
| Oligozoospermia | hp | HP:0000798 | Oligozoospermia |
| Male infertility | hp | HP:0003251 | Male infertility |
| Female infertility | hp | HP:0008222 | Female infertility |
| Decreased serum testosterone concentration | hp | HP:0040171 | Decreased serum testosterone concentration |
| Decreased circulating luteinizing hormone level | hp | HP:0030344 | Decreased circulating luteinizing hormone level |
| Decreased circulating follicle stimulating hormone level | hp | HP:0030341 | Decreased circulating follicle stimulating hormone concentration (differs: "concentration", not "level") |
| Decreased serum estradiol | hp | HP:0008214 | Decreased serum estradiol |
| Breast hypoplasia | hp | HP:0003187 | Breast hypoplasia |
| Sparse pubic hair | hp | HP:0002225 | Sparse pubic hair |
| Sparse axillary hair | hp | HP:0002215 | Sparse axillary hair |
| Absent facial hair | hp | HP:0002550 | Absent facial hair |
| Gynecomastia | hp | HP:0000771 | Gynecomastia |
| Eunuchoid habitus | hp | HP:0003782 | Eunuchoid habitus |
| Osteoporosis | hp | HP:0000939 | Osteoporosis |
| Reduced bone mineral density | hp | HP:0004349 | Reduced bone mineral density |
| Decreased libido | hp | HP:0046504 | Decreased libido |
| Erectile dysfunction | hp | HP:0100639 | Erectile dysfunction |
| High pitched voice | hp | HP:0001620 | Abnormally high-pitched voice (differs) |
| Hypoplasia of the uterus | hp | HP:0000013 | Hypoplasia of the uterus |
| Anosmia | hp | HP:0000458 | Anosmia |
| Delayed skeletal maturation | hp | HP:0002750 | Delayed skeletal maturation |
| Autosomal recessive inheritance | hp | HP:0000007 | Autosomal recessive inheritance |

### GO

| Requested label | Ontology | obo_id | Exact label returned |
|---|---|---|---|
| gonadotropin-releasing hormone receptor activity | go | GO:0004968 | gonadotropin-releasing hormone receptor activity |
| G protein-coupled receptor signaling pathway | go | GO:0007186 | G protein-coupled receptor signaling pathway |
| phospholipase C-activating G protein-coupled receptor signaling pathway | go | GO:0007200 | phospholipase C-activating G protein-coupled receptor signaling pathway |
| luteinizing hormone secretion | go | GO:0032275 | luteinizing hormone secretion |
| follicle-stimulating hormone secretion | go | not retrieved | HTTP 500 Internal Server Error |
| protein folding in endoplasmic reticulum | go | GO:0034975 | protein folding in endoplasmic reticulum |
| endoplasmic reticulum | go | GO:0005783 | endoplasmic reticulum |
| plasma membrane | go | GO:0005886 | plasma membrane |
| ovulation cycle | go | GO:0042698 | ovulation cycle |
| spermatogenesis | go | GO:0007283 | spermatogenesis |
| ERAD pathway | go | GO:0036503 | ERAD pathway |
| cellular response to gonadotropin-releasing hormone | go | GO:0097211 | cellular response to gonadotropin-releasing hormone |

### CL

| Requested label | Ontology | obo_id | Exact label returned |
|---|---|---|---|
| gonadotroph | cl | CL:0000437 | gonadtroph (the label as stored in OLS; spelled without the second "o") |
| gonadotropin releasing neuron | cl | not found (closest: CL:0011111) | exact: 0 hits. Fallback (exact=false, rows=5) returned "hypothalamic gonadotropin-releasing hormone neuron" CL:0011111 as the closest label, which is not an exact match. Other candidates included CL:4304384 (a species-specific "(Mmus)" variant) and CL:4023125 "KNDy neuron". |
| Leydig cell | cl | CL:0000178 | Leydig cell |
| Sertoli cell | cl | CL:0000216 | Sertoli cell |
| granulosa cell | cl | CL:0000501 | granulosa cell |
| theca cell | cl | CL:0000503 | theca cell |

### UBERON

| Requested label | Ontology | obo_id | Exact label returned |
|---|---|---|---|
| adenohypophysis | uberon | UBERON:0002196 | adenohypophysis |
| pituitary gland | uberon | UBERON:0000007 | pituitary gland |
| hypothalamus | uberon | UBERON:0001898 | hypothalamus |
| testis | uberon | UBERON:0000473 | testis |
| ovary | uberon | UBERON:0000992 | ovary |
| uterus | uberon | UBERON:0000995 | uterus (a second hit, UBERON:0006834 "uterus or analog", is not an exact match) |
| penis | uberon | UBERON:0000989 | penis (a second hit, UBERON:0008811 "intromittent organ", is not an exact match) |
| bone tissue | uberon | UBERON:0002481 | bone tissue |

### CHEBI

| Requested label | Ontology | obo_id | Exact label returned |
|---|---|---|---|
| gonadoliberin | chebi | not found (closest: CHEBI:5520) | exact: 0 hits. Alt "gonadotropin-releasing hormone" (exact) returned CHEBI:5520 "gonadorelin". Fallback (exact=false) also returned CHEBI:80298 "Gonadotropin-releasing hormone II", which is a different entity. |
| testosterone | chebi | CHEBI:17347 | testosterone |
| 17beta-estradiol | chebi | CHEBI:16469 | 17beta-estradiol |
| progesterone | chebi | CHEBI:17026 | progesterone |
| luteinizing hormone | chebi | CHEBI:81568 | Luteinizing hormone (capitalization differs) |
| follicle-stimulating hormone | chebi | not found (closest: CHEBI:81569) | exact: 0 hits. Fallback (exact=false) returned "Follicle stimulating hormone" CHEBI:81569 (hyphen differs). Alt "follitropin" (exact) returned HTTP 500 and was not retried. A separate CHEBI:757385 "follitropin" appeared in the fallback results. |
| inhibin (optional) | chebi | not found | exact: 0 hits; fallback (exact=false, rows=5): 0 hits |

### NCIT

| Requested label | Ontology | obo_id | Exact label returned |
|---|---|---|---|
| Testosterone | ncit | not retrieved | HTTP 500 Internal Server Error |
| Estradiol | ncit | NCIT:C2295 | Estradiol |
| Chorionic Gonadotropin | ncit | NCIT:C2275 (via alt) | Exact query returned only "Recombinant Human Chorionic Gonadotropin" NCIT:C528, which is not an exact match. Alt "Human Chorionic Gonadotropin" (exact) returned "Human Chorionic Gonadotropin" NCIT:C2275. |
| Follitropin Alfa | ncit | NCIT:C203026 | Follitropin Alfa |
| Menotropins | ncit | NCIT:C634 (closest) | "Menotropin" (singular; no exact plural match). The same query also returned NCIT:C2274 "Human Menopausal Gonadotropin". |
| Gonadorelin | ncit | not retrieved | HTTP 500 Internal Server Error |
| Hormone Replacement Therapy | ncit | NCIT:C15599 | Hormone Replacement Therapy |
| Ovulation Induction | ncit | not found | exact: 0 hits. Fallback (exact=false, rows=5) returned only unrelated labels ("Ethinyl Estradiol/Norethindrone" NCIT:C29035, "Estradiol/Norethindrone Acetate Tablet" NCIT:C84875). |
| In Vitro Fertilization | ncit | NCIT:C16580 | In Vitro Fertilization |
| Orchiopexy | ncit | NCIT:C111066 | Orchiopexy |
| Genetic Counseling | ncit | NCIT:C15240 | Genetic Counseling |

### MONDO

| Requested label | Ontology | obo_id | Exact label returned |
|---|---|---|---|
| normosmic congenital hypogonadotropic hypogonadism | mondo | not found | exact query returned only MONDO:0018555 "hypogonadotropic hypogonadism", a broader term that does not match the requested label |
| hypogonadotropic hypogonadism | mondo | MONDO:0018555 | hypogonadotropic hypogonadism (lowercase "h"). This exact query under the mondo filter also returned HP:0000044 "Hypogonadotropic hypogonadism", which is an HP term and not used here. |
| Kallmann syndrome | mondo | not retrieved | HTTP 500 Internal Server Error |

## Failures and notes

- **HTTP 500, not retried (permanent per fetch rules):** GO "follicle-stimulating hormone secretion"; CHEBI "follitropin" (alt); NCIT "Testosterone"; NCIT "Gonadorelin"; MONDO "Kallmann syndrome".
- **Not found after exact and fallback searches:** HP "Absent pubertal development" (and its alt "Pubertal failure"); CL "gonadotropin releasing neuron" (closest CL:0011111 only); CHEBI "gonadoliberin" (closest CHEBI:5520 only), "follicle-stimulating hormone" (closest CHEBI:81569 only), and "inhibin"; NCIT "Ovulation Induction"; MONDO "normosmic congenital hypogonadotropic hypogonadism".
- **Label-text differences to check before use:** HP "Decreased circulating follicle stimulating hormone level" resolved to "...concentration"; HP "High pitched voice" resolved to "Abnormally high-pitched voice"; CL "gonadotroph" is stored as "gonadtroph".
- **Non-exact matches used as the closest result:** NCIT "Chorionic Gonadotropin" resolved via the alt "Human Chorionic Gonadotropin"; NCIT "Menotropins" resolved to the singular "Menotropin".

Queries were sent to `https://www.ebi.ac.uk/ols4/api/search` with the query strings described above, and the alternate and fallback URLs used the same host and path. I did not verify any term beyond the search `label` and `obo_id` fields.

# Hypogonadotropic Hypogonadism 7 With or Without Anosmia (HH7; GNRHR) — Disease Characteristics Report

**Scope and method.** This report covers MONDO:0007794 / OMIM:146110, caused by biallelic variants in **GNRHR** (HGNC:4421).

- **Sources.** PubMed records came from NCBI E-utilities. OMIM was read through a public mirror, because omim.org returned HTTP 403. Other sources were Monarch, HGNC, UniProt, ClinVar counts, MGI, Alliance, ClinicalTrials.gov and EBI OLS4.
- **Quotes.** Quotes are short verbatim fragments of abstracts as returned by the retrieval tool. Full abstracts could not be reproduced, so check each quote against the PubMed record before depositing it as an evidence item.
- **Not retrieved.** The Orphanet page (bot check), two PMC full texts (PMC5527354, PMC3888824), gnomAD, GeneReviews and GTR were not retrieved. Gaps are flagged in the relevant sections.
- **Evidence level.** Much of the management, epidemiology and prognosis evidence is for congenital hypogonadotropic hypogonadism (CHH) as a whole, not for GNRHR specifically. This is marked "CHH-level" throughout.

---

## 1. Disease Information

**Overview.** HH7 is an autosomal recessive form of congenital isolated hypogonadotropic hypogonadism caused by homozygous or compound heterozygous loss-of-function variants in **GNRHR**. GNRHR encodes the gonadotropin-releasing hormone receptor on pituitary gonadotropes.

- Monarch describes it as "A hypogonadotropic hypogonadism that has material basis in homozygous or compound heterozygous mutation in the GNRHR gene on chromosome 4q13, sometimes in association with mutation in another gene. No patients with anosmia have been reported." ([Monarch MONDO:0007794](https://api.monarchinitiative.org/v3/api/entity/MONDO:0007794))
- The defect is pituitary resistance to GnRH. Olfaction is normal, because GnRH-neuron migration is not affected.
- The first molecular description was a brother and sister compound heterozygous for Q106R and R262Q (de Roux 1997, PMID 9371856; Layman 1998, PMID 9425890). Neither PubMed record has an abstract.

**Identifiers**

| Resource | Identifier | Source |
|---|---|---|
| MONDO | MONDO:0007794 | Monarch |
| OMIM (phenotype) | 146110 | Monarch / OMIM mirror |
| OMIM (gene) | 138850 | HGNC |
| DOID | DOID:0090078 | Monarch |
| MeSH | C562785 | Monarch |
| UMLS / MedGen | C0342384 / 87440 | Monarch |
| GARD | 0002897 | Monarch |
| SNOMED CT | 123953004 | Monarch |
| NANDO | 1200382 | Monarch |
| ICD-9 | 253.4 | Monarch |
| Orphanet | ORPHA:432 "Normosmic congenital hypogonadotropic hypogonadism" (parent grouping; no HH7-specific code found) | UniProt P30968 cross-reference |
| ICD-10 / ICD-11 | Not retrieved. Monarch lists no ICD-10/11 cross-reference. A Finnish study used ICD-10 hypogonadotropic hypogonadism codes under E23.0 (PMID 21682876, per search summary). | — |

**Synonyms.** HH7; hypogonadotropic hypogonadism 7 without anosmia; "hypogonadism, isolated hypogonadotropic"; "idiopathic hypogonadotropic hypogonadism; IHH" (OMIM alternative titles). Literature terms include normosmic IHH/CHH due to GNRHR mutation, GnRH resistance, and isolated GnRH deficiency (GNRHR-related).

**Naming note.** The current OMIM and MONDO title says "with or without anosmia", but OMIM's phenotype–gene table still reads "without anosmia". None of the molecularly described cases in the OMIM entry is anosmic. Bhagavath 2005 (PMID 16213849, via OMIM) found no GNRHR mutations in hyposmic or anosmic patients.

**Data provenance.** All information is aggregated disease-level data: OMIM, case reports, family studies and research cohorts. None comes from individual EHR records.

---

## 2. Etiology

**Causal factor.** The cause is genetic: biallelic germline loss-of-function variants in GNRHR at 4q13.2. No environmental or infectious cause exists.

**Genetic risk factors**

- **Recurrent and founder alleles.** Choi 2015 (PMID 26207952) identified eight founder mutations in five genes, three of them in GNRHR: "GNRHR (Q106R, R262Q, R139H)".
- **R139H haplotype.** Brazilian R139H carriers share a haplotype (Beneduzzi 2014, PMID 25016926). R139H is described as a "Polish founder mutation" in Russian patients (Zernov 2016, PMID 27544332).
- **Oligogenic contribution.** In one family, two sisters compound heterozygous for Q106R/R262Q also carried a heterozygous FGFR1 variant (Seminara 2000, PMID 10690855; Pitteloud 2007, PMID 17235395). The authors wrote: "2 different gene defects can synergize to produce a more severe phenotype".
  - CHH-level: oligogenicity was found in 2.5% of 397 patients (Sykiotis 2010, PMID 20696889).
  - CHH-level: "Oligogenic inheritance was detected in 15% of CHH cases, with variants in FGFR1 being most commonly involved" (Wang 2026, PMID 41873429).
- **Monoallelic variants.** Rare heterozygous GNRHR variants were more common in GnRH-deficient probands than controls (P < 0.01), but phenotype did not track genotype. The authors suggest "as-yet-unidentified genetic and/or environmental factors may combine with singly mutated GNRHR alleles" (Gianetti 2012, PMID 22745237).
  - One heterozygous GNRHR variant was found among women with functional hypothalamic amenorrhea (Caronia 2011, PMID 21247312).
  - Heterozygous Q106R carriers in Malta had normal hormones and fertility (Axiak 2023, PMID 38196663).

**Environmental risk factors.** None are established. The only non-genetic risk markers are family history and parental consanguinity, as for any recessive disorder.

**Protective factors.** No protective variants or exposures were retrieved. Partial-function alleles (Q106R, R262Q) are associated with milder or reversible phenotypes (see section 9).

**Gene–environment interaction.** None is demonstrated. The functional hypothalamic amenorrhea data (PMID 21247312) suggest, as a hypothesis, that heterozygous variants in GnRH-pathway genes lower the threshold for stress-, weight- or exercise-induced GnRH suppression.

---

## 3. Phenotypes

Frequencies specific to GNRHR are scarce. OMIM-derived counts in Monarch are tiny (n = 1–2). HPO IDs below were verified through OLS4 or Monarch.

| Phenotype | Type | HPO | Onset | Severity / course | Frequency and evidence |
|---|---|---|---|---|---|
| Hypogonadotropic hypogonadism | Lab / clinical | HP:0000044 | Congenital; recognised at puberty | Complete to partial | Defining; 2/2 (OMIM counts via Monarch) |
| Delayed or absent puberty | Sign | HP:0000823; HP:0008187 (absence of secondary sex characteristics) | Adolescence | Variable; partial forms present as apparent constitutional delay | Core (OMIM synopsis). Homozygous R262Q in two brothers with delayed puberty (PMID 16968799) |
| Primary amenorrhea | Sign | HP:0000786 | Adolescence | Persistent unless treated | "all but two" of 12 biallelic women (PMID 30476149) |
| Secondary amenorrhea / oligomenorrhea | Sign | HP:0000869 | Young adult | Partial forms | Partial-deficiency females (PMID 29182666) |
| Breast hypoplasia / delayed thelarche | Sign | HP:0003187 | Adolescence | Variable; normal breast development reported in partial cases (PMID 10022417) | OMIM synopsis |
| Uterine hypoplasia | Imaging | HP:0000013 | Adolescence | — | Uterine height shorter than controls, P < 0.0001 (PMID 30476149) |
| Micropenis | Sign | HP:0000054 | Neonatal | Marks severe prenatal/minipubertal deficiency | 1/1 (OMIM count); Caron 1999 brothers (PMID 10084584, via OMIM) |
| Cryptorchidism | Sign | HP:0000028 | Neonatal | Often bilateral in severe cases | Caron 1999 (via OMIM); frequency not established |
| Decreased testicular size | Sign | HP:0008734 | Puberty onward | 8 mL (de Roux 1997) to 17 mL in fertile eunuch (PMID 11397842) | Common in males |
| Low testosterone / estradiol | Lab | HP:0040171; HP:0008214 | Puberty onward | — | Defining |
| Low or inappropriately normal LH and FSH | Lab | HP:0030344; HP:0030341 | — | LH pulses absent or of low amplitude | Defining |
| Infertility; azoospermia / oligozoospermia | Sign / lab | HP:0003251; HP:0008222; HP:0000027; HP:0000798 | Adult | Treatable; borderline oligospermia in homozygous R262Q (PMID 16968799) | "Occasional" in the Monarch annotation, which reflects "in some" in OMIM |
| Sparse pubic, axillary and facial hair | Sign | HP:0002225; HP:0002215; HP:0002550 | Puberty | — | OMIM synopsis |
| High-pitched (puerile) voice | Sign | HP:0001620 | Puberty | — | OMIM synopsis |
| Gynecomastia | Sign | HP:0000771 | Adolescence / adult | — | OMIM synopsis lists it; 0/1 in OMIM counts |
| Eunuchoid habitus; delayed bone age | Sign | HP:0003782; HP:0002750 | Adolescence | — | CHH-level |
| Reduced bone mineral density / osteoporosis | Complication | HP:0004349; HP:0000939 | Adult | Worse with treatment gaps | CHH-level (PMID 22248317) |
| Decreased libido, erectile dysfunction | Symptom | HP:0046504; HP:0100639 | Adult | Responds to sex steroids | CHH-level |
| Anosmia | **Excluded** | HP:0000458 | — | — | 0/2 (OMIM counts); normal smell in the synopsis |

**Female-specific findings.** Women with biallelic GNRHR mutations showed "an exaggerated LH response to GnRH stimulation, similar to that seen in women with PCOS" (Maione 2019, PMID 30476149). Ovarian volume, estradiol, AMH and inhibin B were lower than in PCOS.

**Fertile eunuch variant.** One man had preserved testicular volume and spermatogenesis with androgen deficiency, followed by reversal (Pitteloud 2001, PMID 11397842).

**Quality of life (CHH-level).** "Patients with CHH/KS frequently express lasting adverse psychological, emotional, social, and psychosexual effects" and "Unnecessary delays in diagnosis and treatment-initiation can significantly contribute to poor body image" (Dwyer 2019, PMID 31333578). No GNRHR-specific EQ-5D or SF-36 data were found.

---

## 4. Genetic / Molecular Information

**Gene.** GNRHR: HGNC:4421; NCBI Gene 2798; Ensembl ENSG00000109163; UniProt P30968; OMIM 138850; 4q13.2 (GRCh38 chr4:67,737,118–67,754,388).

- The gene has three exons spanning more than 18.9 kb and a 987-bp coding region (Fan 1994, PMID 7958384; Fan 1995, PMID 7768323; via OMIM).
- The protein is 328 amino acids, a multi-pass cell-membrane protein (UniProt).
- A splice isoform with a 128-bp deletion cannot bind ligand and impairs wild-type signalling when co-expressed (Grosse 1997, PMID 9259321, via OMIM).

**Pathogenic variants.** All are germline. Missense variants predominate, with rare nonsense and splice variants.

| Variant | Class | Functional effect | Reference |
|---|---|---|---|
| p.Gln106Arg (Q106R) | Missense, partial loss of function | Binding markedly reduced but not abolished | PMID 9371856; OMIM .0001 |
| p.Arg262Gln (R262Q) | Missense, partial loss of function | Signalling impaired; differential effect on gonadotropin subunit genes | OMIM .0002; PMID 12574221 |
| p.Arg139His (R139H) | Missense, complete loss of function | "The Arg(139)His mutation completely eliminated detectable GnRH-binding activity" (DRS motif) | PMID 11397871 |
| p.Arg139Cys | Missense | "The R139C mutation almost completely abolished plasma membrane expression" | PMID 17179725 |
| p.Glu90Lys (E90K) | Missense, misfolding | Retained in the ER; rescuable by pharmacoperone | PMID 12107234 |
| p.Asn10Lys; p.[Asn10Lys;Gln11Lys] | Missense | Partial phenotype with Q106R | PMID 11397871; PMID 15240592 |
| p.Ala129Asp, p.Ser168Arg, p.Ser217Arg, p.Ala171Thr, p.Tyr284Cys | Missense | Loss of function | OMIM .0003–.0006, .0012 |
| p.Leu314Ter | Nonsense | Truncation | Kottler 2000, PMID 10999776 (OMIM .0007) |
| IVS1 −1 G>A | Splice acceptor | Loss of function | Silveira 2002, PMID 12050282 (OMIM .0011) |
| p.Pro320Leu | Missense | No detectable ligand binding | PMID 15240592 |
| p.Pro282Arg, p.Tyr323Cys | Missense | "The Pro282Arg mutant is unable to bind radiolabeled GnRH analogue." | PMID 22679506 |
| p.Tyr283His, p.Val134Gly | Missense | Completely inactivating | PMID 25016926; PMID 23295295 |
| p.Thr269Met, p.Tyr290Phe | Missense | "complete or partial loss-of-function of the T269M and Y290F mutants" | PMID 30476149 |

- UniProt also lists HH7 variants N18S, I37S, L83V, E90D, P146S and L266R.
- "functional mutations of the GNRHR are distributed widely throughout the protein" (Beranova 2001, PMID 11297587).

**ClinVar (queried 2026-11-26).** 255 GNRHR records: 48 pathogenic, 29 likely pathogenic, 138 VUS. Individual variant classifications were not retrieved.

**Allele frequencies**

- Q106R: global minor allele frequency about 0.003; 0.029 in Maltese newborns (n = 493) (PMID 38196663).
- R262Q: about 0.002 (Choi 2015 full text, per search summary; not confirmed from the abstract).
- gnomAD was not queried directly.

**Functional consequence.** The mechanism is loss of function: reduced ligand binding, impaired Gq coupling, or misfolding with ER retention.

- "mutant GnRHRs have frequently not lost intrinsic functionality and are subject to rescue" (Janovick 2002, PMID 12107234).
- Misfolded mutants are dominant-negative in vitro: "hGnRHR mutants were found to inhibit the function of WT GnRHR" (PMID 12843188), through "WT receptor retention in the endoplasmic reticulum by mislocalized mutants" (PMID 15105440).
- Heterozygotes are nonetheless clinically normal, so the in vitro dominant-negative effect does not produce dominant disease.

**Modifier genes.** FGFR1 (PMID 17235395). Other CHH genes may act through oligogenic load (PMID 20696889; review PMID 32200437).

**Epigenetics and chromosomal abnormalities.** None were identified. No disease-relevant epigenetic data, structural variants or aneuploidy were retrieved. Somatic origin does not apply.

---

## 5. Environmental Information

There are no causal toxins, lifestyle factors or infectious agents. Energy deficit, stress and intense exercise are relevant only as possible modifiers in heterozygous carriers (hypothalamic amenorrhea; PMID 21247312). This link is hypothesised, not demonstrated, for HH7.

---

## 6. Mechanism / Pathophysiology

**Causal chain**

1. Biallelic germline GNRHR variants **result in** a receptor that falls into one of three groups. This is demonstrated in vitro.
   - **Misfolded and ER-retained.** Receptor-misrouting is "an unexpectedly prevalent and rescuable etiology" (PMID 12364481).
   - **Unable to bind GnRH.** Examples are R139H, P320L and P282R.
   - **Impaired in G-protein coupling or signalling.** Examples are R262Q and Y323C.
2. Reduced functional receptor at the gonadotrope plasma membrane **leads to** blunted GnRH-stimulated signalling. Normal signalling "results in the activation of Gq/G(11), phospholipase Cbeta (PLCbetaI), PLA(2), and PLD", with downstream calcium, PKC and MAPK/ERK activity (Naor 2009, PMID 18708085).
3. Blunted signalling **results in** reduced transcription and secretion of LH and FSH.
   - This is demonstrated in vitro: Q106R and R262Q "reduced the sensitivity of the FSH beta gene promoter to a greater extent than LH beta or alpha GSU" (PMID 12574221).
   - It is demonstrated clinically by low-amplitude or apulsatile LH and by variable resistance to exogenous pulsatile GnRH (PMID 10690855; PMID 15240592; PMID 23341491).
4. Gonadotropin deficiency **leads to** failure of gonadal stimulation, with two branches.
   - **Male branch.** Low LH leads to reduced Leydig-cell testosterone, which results in absent virilisation. If the deficiency is fetal or minipubertal, it results in micropenis and cryptorchidism. Low FSH leads to reduced Sertoli-cell proliferation, which results in small testes and azoospermia or oligozoospermia.
   - **Female branch.** Low FSH and LH lead to arrested folliculogenesis and low estradiol, which result in absent thelarche, primary amenorrhea, a small uterus and anovulatory infertility.
5. Chronic sex-steroid deficiency **leads to** delayed epiphyseal closure, eunuchoid proportions, low bone mass and psychosexual morbidity. This step is CHH-level evidence and is inferred for HH7.
6. **Severity branch.** Residual receptor activity determines the phenotype: "genetic burden defined by severity and dose is associated with clinical phenotype" in biallelic cases (PMID 22745237). Partial alleles give partial hypogonadism, the fertile eunuch variant or reversal.
7. **Not involved.** GnRH-neuron migration and olfactory development are intact, so smell is normal. Hypothalamic GnRH output is presumed normal or increased; this is inferred.

**Checklist coverage**

- **Protein dysfunction.** Misfolding and ER quality-control retention of a class A GPCR.
  - "All reported GnRH receptor mutants causing human hypogonadotropic hypogonadism are misfolded and cannot traffic to the plasma membrane" (Conn-group statement, per search summary; other groups show pure binding or coupling defects for some variants).
  - S168R and S217R are reported as non-rescuable. Per search summary, this is because they prevent the Cys14–Cys200 bridge.
  - Structure: "crystal structure of GnRH1R bound to the small-molecule drug elagolix at 2.8 Å resolution" (Yan 2020, PMID 33082324).
- **Metabolic, immune and tissue damage.** There is no primary involvement. Metabolic and bone effects are secondary to hypogonadism.
- **Molecular profiling.** No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial or CRISPR-screen datasets were retrieved.

**Suggested ontology terms (OLS-verified)**

| Category | Terms |
|---|---|
| GO molecular function | GO:0004968 gonadotropin-releasing hormone receptor activity |
| GO biological process | GO:0007186 G protein-coupled receptor signaling pathway; GO:0007200 phospholipase C-activating G protein-coupled receptor signaling pathway; GO:0097211 cellular response to gonadotropin-releasing hormone; GO:0032275 luteinizing hormone secretion; GO:0034975 protein folding in endoplasmic reticulum; GO:0036503 ERAD pathway; GO:0007283 spermatogenesis; GO:0042698 ovulation cycle |
| GO cellular component | GO:0005886 plasma membrane; GO:0005783 endoplasmic reticulum |
| CL | CL:0000437 gonadotroph (stored label "gonadtroph"); CL:0000178 Leydig cell; CL:0000216 Sertoli cell; CL:0000501 granulosa cell; CL:0000503 theca cell |
| CHEBI | CHEBI:5520 gonadorelin; CHEBI:81568 luteinizing hormone; CHEBI:81569 follicle stimulating hormone; CHEBI:17347 testosterone; CHEBI:16469 17beta-estradiol; CHEBI:17026 progesterone |

The GO ID for "follicle-stimulating hormone secretion" was not retrieved. CL:0011111 (hypothalamic GnRH neuron) is not the affected cell type in HH7.

---

## 7. Anatomical Structures Affected

- **Primary organ.** Anterior pituitary (UBERON:0002196 adenohypophysis; UBERON:0000007 pituitary gland), specifically gonadotropes. The hypothalamus (UBERON:0001898) is structurally and functionally spared.
- **Secondary organs.** Testis (UBERON:0000473), ovary (UBERON:0000992), uterus (UBERON:0000995), penis (UBERON:0000989), breast, and bone (UBERON:0002481).
- **Systems.** Endocrine, reproductive and, secondarily, skeletal.
- **Subcellular.** Plasma membrane (site of receptor function) and endoplasmic reticulum (site of mutant retention).
- **Laterality.** Bilateral and symmetric. Cryptorchidism was bilateral in the reported cases.

---

## 8. Temporal Development

- **Onset.** The defect is congenital. It may show in neonates as micropenis or cryptorchidism, but it usually presents in adolescence as absent or stalled puberty. Diagnosis is typically in late adolescence or early adulthood.
- **Course.** Without treatment the condition is chronic and non-progressive. It is not degenerative.
- **Reversal.** Reversal is documented in GNRHR patients (PMID 11397842; PMID 25016926, which describes a spectrum "varied from complete GnRH deficiency to partial and reversible IHH").
  - CHH-level frequency: "∼10-20% of patients exhibit a spontaneous recovery of reproductive function" (PMID 26194704).
  - 44 of 308 patients reversed, a lifetime incidence of 22%, with relapse possible: "Five men did not sustain their reversal and again developed hypogonadotropism." (PMID 24423288)
  - "the incidence of reversal warrants periodic treatment withdrawal" (PMID 26792935).
- **Critical periods (CHH-level).** These are fetal life and minipuberty (penile growth, testicular descent, Sertoli-cell proliferation) and adolescence (bone mass accrual, psychosexual development).

---

## 9. Inheritance and Population

- **Inheritance.** Autosomal recessive (HP:0000007), with occasional digenic or oligogenic modification.
- **Prevalence.** No HH7-specific figure exists.
  - CHH overall is about 1 in 4,000–15,000 males (reviews, per search summary). Finnish Kallmann syndrome minimal incidence is 1:48,000 overall, 1:30,000 in males and 1:125,000 in females (PMID 21682876).
  - GNRHR share of normosmic CHH: 4.7% of 603 (PMID 27094476); 10% of 110 (PMID 25016926); 40% of recessive kindreds and 16.7% of sporadic normosmic cases (PMID 11297587); 3 of 185 (1.6%) of all hypogonadotropic hypogonadism (Bhagavath 2005, PMID 16213849, via OMIM); 7 of 22 Turkish multiplex families, per search summary of the full text (PMID 22766261).
  - Among 22 Turkish multiplex families, "GNRHR and TACR3 mutations were the most common two causative mutations" (PMID 22766261).
- **Penetrance and expressivity.**
  - Biallelic genotypes are highly penetrant.
  - Expressivity is variable, even within families: "The same mutations of the GnRH receptor gene may thus determine different degrees of alteration of gonadotropin function" (PMID 10022417).
  - "Biallelic, partial loss-of-function mutations in GNRHR cause a wide spectrum of reproductive phenotypes" (PMID 29182666).
- **Anticipation and germline mosaicism.** Neither is reported.
- **Founder effects.** Q106R (Malta), R262Q and R139H (Brazil, Poland, Russia); see section 2.
- **Consanguinity.** Homozygous cases are over-represented in consanguineous populations such as the Turkish cohorts.
- **Carrier frequency.** For Q106R, 43 of 978 Maltese adults (4.4%) were heterozygous, and the global minor allele frequency of about 0.003 implies roughly 1 in 170 carriers (PMID 38196663). Heterozygotes are generally asymptomatic.
- **Sex ratio.** CHH overall shows a male predominance of roughly 3–5:1 (PMID 26194704, per search summary). An autosomal recessive form is expected to affect both sexes equally, and the first families included both sexes, so the male excess probably reflects under-ascertainment in females. This is an inference.

---

## 10. Diagnostics

**Laboratory**

- Low testosterone (males) or estradiol (females), with low or inappropriately normal LH and FSH.
- Otherwise normal anterior pituitary function, prolactin and iron studies.
- Inhibin B and AMH as markers of Sertoli-cell or follicular mass.
  - Inhibin B separates CHH from constitutional delay with pooled sensitivity 92% and specificity 92% (AUC 0.96): "INHB exhibits excellent diagnostic efficiency in distinguishing CHH from CDGP" (PMID 33464540).
  - In women with isolated hypogonadotropic hypogonadism, "Serum AMH and AFC should not serve as prognostic markers of fertility in this population." (PMID 28324034)

**Functional tests**

- GnRH stimulation gives variable results. Responses may be blunted, or exaggerated for LH in biallelic women (PMID 30476149).
- A poor LH response to physiological pulsatile GnRH suggests a pituitary (GNRHR) defect. In 37 women, pituitary resistance occurred in 30%, and that subgroup included GNRHR, PROKR2 and FGFR1 mutations (PMID 23341491).
- Formal smell testing should be normal.

**Imaging**

- Pituitary and hypothalamic MRI is normal, with normal olfactory bulbs and sulci.
- Pelvic or testicular ultrasound, bone age and DXA.

**Biopsy and electrophysiology.** Not indicated.

**Genetic testing**

- The recommended approach is a multigene CHH panel or exome/genome with a virtual panel. This is preferred over single-gene testing because of locus heterogeneity (more than 30 genes; PMID 30698671) and oligogenicity (PMID 29330225). "genetic screening should be offered in patients with IGD" (PMID 29108899).
- Targeted GNRHR sequencing is reasonable for normosmic recessive families or founder populations.
- Chromosomal microarray, karyotype and FISH serve only to exclude other diagnoses, such as Klinefelter syndrome or contiguous deletions. Mitochondrial and repeat-expansion testing are not applicable.
- GTR and GeneReviews specifics were not retrieved.

**Omics-based diagnostics.** None are established.

**Differential diagnosis**

- Constitutional delay of growth and puberty. Homozygous R262Q can mimic it (PMID 16968799).
- Functional hypothalamic amenorrhea.
- Other normosmic CHH genes: GNRH1, KISS1R, KISS1, TACR3, TAC3.
- Kallmann syndrome (anosmia).
- Combined pituitary hormone deficiency, hyperprolactinaemia, haemochromatosis, DAX1-related disease and syndromic hypogonadotropic hypogonadism.
- PCOS in women with partial forms (PMID 30476149).

**Screening.** There is no newborn screening. Cascade testing of siblings applies. Neonatal micropenis or cryptorchidism should prompt hormone measurement during minipuberty (CHH-level).

---

## 11. Outcome / Prognosis

- **Survival.** No evidence of reduced life expectancy was retrieved. No disease-specific mortality data exist.
- **Morbidity.** Infertility (treatable), low bone mass, sexual dysfunction and psychosocial effects.
  - Bone density is lower in patients with long treatment pauses or low-dose testosterone history (PMID 22248317).
- **Fertility outcomes.**
  - Spermatogenesis is induced in about 75% of azoospermic hypogonadotropic men (meta-analysis, PMID 25271205).
  - GNRHR-specific pregnancies include two pregnancies after ovulation induction in the index sister (de Roux 1997, via OMIM) and pregnancy with high-dose pulsatile GnRH (PMID 10690855).
  - Both R139H patients had successful IVF: "IVF/ET treatments were successful, with phenotypically healthy offsprings delivered." (PMID 27544332)
  - A spontaneous conception in a Q106R homozygote did not progress (PMID 12057744).
- **Prognostic factors (CHH-level).**
  - Predictors of outcome on long-term GnRH therapy in 76 men were prior pubertal development, baseline inhibin B above 60 pg/mL, and no prior cryptorchidism (PMID 12213860).
  - Cryptorchidism, a positive genetic background and complete CHH predicted a smaller testicular response in 19 men (PMID 33738751).
  - Partial-function genotypes predict a milder course and possible reversal (PMID 22745237).

---

## 12. Treatment

No randomised trials are specific to GNRHR. Evidence comes from CHH cohorts and GNRHR case series.

| Goal | Treatment | Notes | NCIT (verified) |
|---|---|---|---|
| Virilisation / maintenance (males) | Testosterone (injectable or transdermal) | Does not induce spermatogenesis | NCIT:C15599 Hormone Replacement Therapy (Testosterone ID not retrieved) |
| Feminisation / maintenance (females) | Estradiol with gradual escalation, then added progestogen | — | NCIT:C2295 Estradiol |
| Male fertility | hCG with or without FSH or hMG | Sperm and conception after about 4 months of hCG alone in a partial case (PMID 11397842) | NCIT:C2275 Human Chorionic Gonadotropin; NCIT:C203026 Follitropin Alfa; NCIT:C634 Menotropin |
| Female fertility | Gonadotropin ovulation induction, with or without IVF | See genotype-guided note below | NCIT:C16580 In Vitro Fertilization |
| Pulsatile GnRH | Gonadorelin pump | Variable efficacy because of receptor resistance | (Gonadorelin ID not retrieved) |
| Neonatal males | Early gonadotropin therapy for micropenis or cryptorchidism (review PMID 22009162); orchiopexy | CHH-level | NCIT:C111066 Orchiopexy |
| Supportive | Bone health, psychological and sexual counselling, transition care | PMID 31333578 | NCIT:C15240 Genetic Counseling |

**Genotype-guided treatment**

- Because the defect is at the pituitary receptor, gonadotropins bypass it and are the logical first choice for fertility.
- One kindred's authors concluded that patients should be treated with gonadotropins and not pulsatile GnRH (PMID 10523035, per search summary).
- Partial alleles can still respond to higher-dose pulsatile GnRH (PMID 10690855).
- Meysing 2004 (PMID 15240592) documents a poor response to pulsatile GnRH in a compound heterozygous woman.

**Treatment outcomes (CHH-level)**

- Pulsatile GnRH versus gonadotropins in men, across 420 patients: "GnRH therapy was related to a larger testicular volume" and "earlier spermatogenesis (WMD=-5.30 months; p=0.004)". Sperm detection, sperm concentration and pregnancy rate did not differ significantly (PMID 32777865). This may not apply to GNRHR patients.
- Adverse events of gonadotropin ovulation induction include multiple pregnancy and ovarian hyperstimulation (per search summary of a case report; not verified from an abstract).

**Experimental: pharmacoperones**

- Cell-permeant GnRHR antagonists such as IN3 act as folding templates. "this approach rescues 11 of 13 of these GnRHR missense mutants" in vitro (PMID 12364481).
- In an E90K knock-in mouse, pulsatile pharmacoperone therapy restored receptor surface expression, spermatogenesis and androgen levels in mutant males (Janovick 2013, PMID 24324164).
- No human trial was identified.

**Other advanced therapies.** No gene, cell or RNA therapy is in development. No pharmacogenomic guidance (CPIC/PharmGKB) was retrieved.

**Clinical trials (CHH-level; none GNRHR-specific).** Examples from ClinicalTrials.gov:

- NCT02880280: hMG with hCG.
- NCT03687606: hCG versus hCG plus hMG.
- NCT01403532: sequential hCG/FSH.
- NCT00064987: FSH pretreatment (terminated).
- NCT00914823 and NCT01438034: kisspeptin physiology.
- NCT01500447 and NCT01601171: genetics studies (recruiting).

**Algorithm (CHH consensus; PMID 26194704, PMID 30698671).** Confirm the diagnosis, then induce puberty with sex steroids or gonadotropins. Maintain sex steroids in adulthood, switch to gonadotropins or GnRH when fertility is desired, and trial treatment withdrawal periodically to detect reversal.

---

## 13. Prevention

- **Primary.** None, other than reproductive options for known carrier couples: carrier testing of partners, prenatal diagnosis or preimplantation testing. No guideline specific to GNRHR was retrieved.
- **Secondary.** Early recognition (neonatal micropenis or cryptorchidism; absent puberty by about 13–14 years) and sibling cascade testing. Timely pubertal induction limits psychosocial harm (PMID 31333578).
- **Tertiary.** Continuous sex-steroid replacement, avoidance of treatment gaps, and bone-density monitoring (PMID 22248317).
- **Genetic counselling.** Recurrence risk is 25% for siblings. Counselling must cover variable expressivity, possible reversal and oligogenic contributions (PMID 29330225).
- **Founder populations.** High carrier frequency in Malta may justify targeted testing (PMID 38196663).
- **Not applicable.** Immunisation, public-health or environmental measures, and prophylaxis.

---

## 14. Other Species / Natural Disease

**Orthologs** (NCBI Gene / Alliance)

| Species | Gene | Identifier |
|---|---|---|
| Mouse (*Mus musculus*) | Gnrhr | Gene 14715; MGI:95790 |
| Rat (*Rattus norvegicus*) | Gnrhr | Gene 81668; RGD:70513 |
| Cattle (*Bos taurus*) | GNRHR | Gene 281798 |
| Dog (*Canis lupus familiaris*) | GNRHR | Gene 403718 |
| Zebrafish | gnrhr2 | ZFIN:ZDB-GENE-090128-3 |
| Xenopus | gnrhr | Xenbase XB-GENE-5753573 |
| *C. elegans* | gnrr-1 | WBGene00018798 |
| Drosophila | AkhR | FBgn0025595 |

NCBI Taxon IDs were not retrieved.

**Naturally occurring disease.** No spontaneous GNRHR-deficiency disease in companion or farm animals was retrieved. PubMed searches returned no results, and OMIA was not queried. Breed data and zoonotic transmission do not apply.

**Conservation.** The GnRH–GnRHR axis is conserved across vertebrates, with invertebrate homologues in the AKH/GnRH receptor family (Alliance orthology).

---

## 15. Model Organisms

| Model | Type | Phenotype | Recapitulation and limits | Reference |
|---|---|---|---|---|
| Mouse Gnrhr L117P (*Gnrhr^hh*, MGI:3574585) | ENU-induced, recessive | Severe hypogonadotropic hypogonadism; MGI: "Homozygous mutant mice display prepubescent internal reproductive tracts with hypogonadism and hypogonadotrophy." | "This is the first report of a mouse with a Gnrhr loss of function mutation." It is annotated in MGI as a model of HH7. The mutant is not pharmacoperone-rescuable, and L117P is not a human allele. | PMID 15625238 |
| Mouse Gnrhr gene-trap null | Gene trap in intron 1 with lacZ | "Null Gnrhr mice had small sexual organs", low FSH, LH and steroids, infertility, and "inability to respond to exogenous GnRH" | More severe than the ENU, Kiss1 and Gpr54 models. Fetal male masculinisation is preserved. | PMID 20068010 |
| Mouse Gnrhr E90K knock-in | Human-orthologous misfolding allele | "the primary phenotype of mice homozygous for E90K is female infertility due to ovulation failure"; males fertile with smaller testes | Milder than the human E90K phenotype. Used for in vivo pharmacoperone rescue. | PMID 22918878; PMID 24324164 |
| Cell models (COS-7, HeLa) | Transient expression | Binding, inositol phosphate signalling, trafficking, dominant-negative and rescue assays | Standard for variant classification. Overexpression artefacts are possible. | PMID 11297587; PMID 12107234; PMID 15105440 |

- MGI lists 19 Gnrhr alleles: 7 targeted, 6 endonuclease-mediated, 3 chemically induced, and others. Individual allele symbols were not retrieved.
- The hpg mouse is a Gnrh1 deletion. It models ligand deficiency, not receptor deficiency.
- No zebrafish gnrhr knockout, iPSC or organoid model was retrieved.
- Resources: MGI (informatics.jax.org/marker/MGI:95790), Alliance, RGD, ZFIN.

---

## Discrepancies and Gaps to Resolve Before Curation

1. **Pitteloud 2001 genotype (PMID 11397842).** The PubMed abstract fragment reads "associated with a homozygous mutation (Gln106Arg) in the GnRH-R". The OMIM mirror text describes this patient as homozygous for R262Q. Check the primary paper.
2. **HP:0000054 label.** Monarch's entity endpoint showed an inconsistent label for this ID. OLS confirms HP:0000054 is Micropenis.
3. **Not retrieved.** Orphanet prevalence and ICD-10/ICD-11 codes, gnomAD frequencies, per-variant ClinVar classifications, GeneReviews and GTR content, NCBI Taxon IDs, and several ontology IDs (GO follicle-stimulating hormone secretion; NCIT Testosterone, Gonadorelin and Ovulation Induction).
4. **Second-hand items.** Details attributed to "OMIM" or "per search summary" (Caron 1999, Kottler 2000, Pralong 1999, Silveira 2002, Bhagavath 2005, and the Choi allele frequencies) were not confirmed against the primary abstracts.

## Key Sources

- OMIM 146110 and 138850, via public mirror: https://git.lsit.ucsb.edu/publicdata/nih-gov/raw/commit/a3492137cada35c1427e5783c176e4344e6cbb56/www.ncbi.nlm.nih.gov/omim/146110
- Monarch: https://api.monarchinitiative.org/v3/api/entity/MONDO:0007794
- UniProt P30968: https://rest.uniprot.org/uniprotkb/P30968.txt
- HGNC: https://rest.genenames.org/fetch/symbol/GNRHR
- MGI: https://www.informatics.jax.org/marker/MGI:95790
- ClinicalTrials.gov API (condition: congenital hypogonadotropic hypogonadism)
- PubMed records at https://pubmed.ncbi.nlm.nih.gov/PMID/ for: 9371856 (1997), 9425890 (1998), 10022417 (1999), 10690855 (2000), 11297587 (2001), 11397842 (2001), 11397871 (2001), 12057744 (2002), 12107234 (2002), 12364481 (2002), 12213860 (2002), 12574221 (2003), 12843188 (2003), 15105440 (2004), 15240592 (2004), 15625238 (2005), 16968799 (2006), 17179725 (2006), 17235395 (2007), 17761590 (2007), 18708085 (2009), 20068010 (2010), 20696889 (2010), 21247312 (2011), 21645587 (2011), 21682876 (2011), 22009162 (2011), 22248317 (2012), 22679506 (2012), 22745237 (2012), 22766261 (2012), 22918878 (2012), 23295295 (2012), 23341491 (2013), 24324164 (2013), 24423288 (2014), 25016926 (2014), 25271205 (2014), 26194704 (2015), 26207952 (2015), 26792935 (2016), 27094476 (2016), 27544332 (2016), 28324034 (2017), 29182666 (2017), 29108899 (2018), 29330225 (2018), 30476149 (2019), 30698671 (2019), 31333578 (2019), 33082324 (2020), 32200437 (2021), 32777865 (2021), 33464540 (2021), 33738751 (2021), 38196663 (2023), 41873429 (2026).

## Reference Validation

Checked with `linkml-reference-validator` 0.8.0.

| Outcome | Count |
| --- | --- |
| References checked | 73 |
| Resolved | 72 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 21 |
| Quoted claims found in source | 20 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 72 |
| On topic | 60 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:16968799` (4 mentions) - Identifier did not resolve to a record

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:12364481` *(abstract only)*: "an unexpectedly prevalent and rescuable etiology"
  - Text part not found as substring: 'an unexpectedly prevalent and rescuable etiology' (note: only abstract available for PMID:12364481, full text may contain this excerpt)

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 89 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 77 |
| Terms whose name was checked | 8 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 8 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0000044` (3 mentions) - the report calls it "hp", "Lab / clinical"; HP calls it **Hypogonadotropic hypogonadism**
- `HP:0000798` (2 mentions) - the report calls it "hp"; HP calls it **Oligozoospermia**
- `HP:0003251` (2 mentions) - the report calls it "hp"; HP calls it **Male infertility**
- `HP:0008222` (2 mentions) - the report calls it "hp"; HP calls it **Female infertility**
- `HP:0040171` (2 mentions) - the report calls it "hp"; HP calls it **Decreased serum testosterone concentration**
- `HP:0030341` (2 mentions) - the report calls it "hp"; HP calls it **Decreased circulating follicle stimulating hormone concentration**
- `HP:0008214` (2 mentions) - the report calls it "hp"; HP calls it **Decreased serum estradiol**
- `HP:0003187` (2 mentions) - the report calls it "hp", "Sign"; HP calls it **Breast hypoplasia**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `HP:0000007` - called "Inheritance:** autosomal recessive", "hp"
- `HP:0000044` - called "hp", "Lab / clinical"
- `HP:0000786` - called "hp", "Sign"
- `HP:0000869` - called "hp", "Sign"
- `HP:0000054` - called "hp", "Sign"
- `HP:0000028` - called "hp", "Sign"
- `HP:0008734` - called "hp", "Sign"
- `HP:0003187` - called "hp", "Sign"
- `HP:0000771` - called "hp", "Sign"
- `HP:0001620` - called "hp", "Sign"
- `HP:0000013` - called "hp", "Imaging"
- `HP:0000458` - called "hp", "Excluded"

### Terms the ontology service could not be reached for

76 term(s) could not be checked because the ontology service was unreachable (a timeout, 5xx, 408 or 429), not because anything looks wrong with them. Re-run when the service is reachable -- the label cache resumes, so only the unresolved terms are retried:

- `HP:0000823` (2 mentions)
- `HP:0008187` (2 mentions)
- `HP:0000786` (2 mentions)
- `HP:0000869` (2 mentions)
- `HP:0000054` (4 mentions)
- `HP:0008734` (2 mentions)
- `HP:0000027` (2 mentions)
- `HP:0030344` (2 mentions)
- `HP:0002225` (2 mentions)
- `HP:0002215` (2 mentions)
- `HP:0000771` (2 mentions)
- `HP:0003782` (2 mentions)
- `HP:0000939` (2 mentions)
- `HP:0046504` (2 mentions)
- `HP:0100639` (2 mentions)
- `HP:0001620` (2 mentions)
- `HP:0000013` (2 mentions)
- `HP:0000458` (2 mentions)
- `HP:0002750` (2 mentions)
- `GO:0004968` (2 mentions)
- `GO:0007186` (2 mentions)
- `GO:0007200` (2 mentions)
- `GO:0032275` (2 mentions)
- `GO:0034975` (2 mentions)
- `GO:0005783` (2 mentions)
- `GO:0005886` (2 mentions)
- `GO:0042698` (2 mentions)
- `GO:0007283` (2 mentions)
- `GO:0036503` (2 mentions)
- `GO:0097211` (2 mentions)
- `CL:0000437` (2 mentions)
- `CL:0011111` (4 mentions)
- `CL:4304384` (1 mention)
- `CL:4023125` (1 mention)
- `CL:0000178` (2 mentions)
- `CL:0000216` (2 mentions)
- `CL:0000501` (2 mentions)
- `CL:0000503` (2 mentions)
- `UBERON:0002196` (2 mentions)
- `UBERON:0000007` (2 mentions)
- `UBERON:0001898` (2 mentions)
- `UBERON:0000473` (2 mentions)
- `UBERON:0000992` (2 mentions)
- `UBERON:0000995` (2 mentions)
- `UBERON:0006834` (1 mention)
- `UBERON:0000989` (2 mentions)
- `UBERON:0008811` (1 mention)
- `UBERON:0002481` (2 mentions)
- `CHEBI:5520` (4 mentions)
- `CHEBI:80298` (1 mention)
- `CHEBI:17347` (2 mentions)
- `CHEBI:16469` (2 mentions)
- `CHEBI:17026` (2 mentions)
- `CHEBI:81568` (2 mentions)
- `CHEBI:81569` (4 mentions)
- `CHEBI:757385` (1 mention)
- `NCIT:C2295` (2 mentions)
- `NCIT:C2275` (3 mentions)
- `NCIT:C528` (1 mention)
- `NCIT:C203026` (2 mentions)
- `NCIT:C634` (2 mentions)
- `NCIT:C2274` (1 mention)
- `NCIT:C15599` (2 mentions)
- `NCIT:C29035` (1 mention)
- `NCIT:C84875` (1 mention)
- `NCIT:C16580` (2 mentions)
- `NCIT:C111066` (2 mentions)
- `NCIT:C15240` (2 mentions)
- `MONDO:0018555` (2 mentions)
- `MONDO:0007794` (6 mentions)
- `OMIM:146110` (1 mention)
- `DOID:0090078` (1 mention)
- `ORPHA:432` (1 mention)
- `MGI:95790` (4 mentions)
- `RGD:70513` (1 mention)
- `MGI:3574585` (1 mention)

### Terms whose obsolescence could not be checked

4 term(s) resolved, so they exist, but the ontology service was unreachable for the deprecation check -- treat their obsolescence as unknown rather than clean, and re-run to confirm:

- `HP:0000007` (3 mentions)
- `HP:0000028` (2 mentions)
- `HP:0002550` (2 mentions)
- `HP:0004349` (2 mentions)
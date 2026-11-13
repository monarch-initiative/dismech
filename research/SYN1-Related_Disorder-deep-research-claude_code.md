---
provider: claude_code
cached: false
start_time: '2026-11-13T00:08:37.461198'
end_time: '2026-11-13T00:15:54.059929'
duration_seconds: 436.6
template_file: templates/disease_pathophysiology_research.md
template_sha: "f452f0a9c7e3536175154b9683c45663f686f283"
template_variables:
  disease_name: SYN1-Related Neurodevelopmental Disorder
  mondo_id: MONDO:0010339
  category: Mendelian
  causal_genes: SYN1
  omim_id: OMIM:300491
  synonyms: epilepsy, X-linked, with variable learning disabilities and behavior disorders,
    X-linked recessive, X-linked dominant; X-linked epilepsy-learning disabilities-behavior
    disorders syndrome; epilepsy, X-linked, with variable learning disabilities and
    behaviour disorders, X-linked recessive, X-linked dominant
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
  web_search_requests: 3
  num_turns: 31
  total_cost_usd: 5.173822070000002
  session_id: 29daa510-1652-4edc-bae2-c29dff64d294
  stop_reason: end_turn
  permission_denials: 8
  denied_tools:
  - Bash
  assistant_text_blocks: 3
citation_count: 34
reference_validation:
  total_references: 33
  verified: 33
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 47
  quotes_valid: 45
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:36568968
  - PMID:39177219
  relevance_assessed: 33
  on_topic: 26
  needs_review: true
  validator_version: 0.5.1
term_validation:
  total_terms: 60
  verified: 55
  not_found: 0
  obsolete: 1
  unverifiable: 4
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 2
  labels_mismatched: 4
  mislabelled_terms:
  - term_id: MONDO:0100148
    reported_labels:
    - "SYN1 \u2013 X-linked complex neurodevelopmental disorder"
    - Decide whether the ClinGen Definitive assertion
    ontology_label: X-linked complex neurodevelopmental disorder
  - term_id: CHEBI:39867
    reported_labels:
    - Lower than sodium-channel blockers
    ontology_label: valproic acid
  - term_id: CHEBI:7824
    reported_labels:
    - Not stated
    ontology_label: oxcarbazepine
  - term_id: CHEBI:6437
    reported_labels:
    - already in the KB entry
    ontology_label: levetiracetam
  labels_variant: 1
  obsolete_terms:
  - term_id: HP:0002459
    ontology_label: obsolete Dysautonomia
    replaced_by: HP:0012332
  unresolvable_prefixes:
  - OMIM
  - ORPHA
  - MGI
  - RGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SYN1-Related Neurodevelopmental Disorder
- **MONDO ID:** MONDO:0010339 (if available)
- **Causal gene(s):** SYN1
- **OMIM:** OMIM:300491
- **Synonyms:** epilepsy, X-linked, with variable learning disabilities and behavior disorders, X-linked recessive, X-linked dominant; X-linked epilepsy-learning disabilities-behavior disorders syndrome; epilepsy, X-linked, with variable learning disabilities and behaviour disorders, X-linked recessive, X-linked dominant
- **Category:** Mendelian

Many disease names are serial numbers ("... autosomal dominant 64", "... 26") that
do not say which gene the disease is about, and a similarly named disease with a
different gene is easy to research by mistake. Research the disease with the MONDO
ID and causal gene given above, and name its causal gene in your first paragraph.
If the name seems to point to a different gene or OMIM entry, follow the
identifiers above.

## Research Objectives

Please provide a comprehensive research report on **SYN1-Related Neurodevelopmental Disorder** covering all of the
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

Still gathering sources: PubMed pages are cookie-walled here, so I'm reading the abstracts already cached in the repository and trying Europe PMC for the rest.

Reading the three cached abstracts for exact quotes, then writing the report.

# SYN1-Related Neurodevelopmental Disorder: Disease Characteristics Research Report

**Target:** MONDO:0010339 · OMIM:300491 · causal gene **SYN1** (hgnc:11494, Xp11) · Category: Mendelian
**Report date:** 2026-11-13

## How this report was sourced

- **Verbatim quotes** come from abstracts or full text held in this repository's `references_cache/` for PMIDs 21441247, 23406870, 26096837, 28973667, 31906484, 34078716, 34243774, 36568968, 39177219, 40554312, 19020204 and 7568108. The 7568108 quote was read without its file header, so check it against `references_cache/PMID_7568108.md` before reuse.
- **Metadata only** (title, authors, journal, year confirmed through Europe PMC; no quotable text retrieved): PMIDs 14985377, 18057210, 23280234, 7777057, 7568107, 23570901, 29976799, 30390306, 29671924, 32738165, 34616357, 36693418, 36742338, 38576531, 42349827. Statements about these papers' findings are at title or summary level, plus my recall where noted, and need the abstract fetched before use as evidence. For 36693418 and 38576531 the detail comes from an automated summary of the abstract.
- **Not consulted:** OMIM, Orphanet, ClinVar, gnomAD, GeneReviews, ClinicalTrials.gov, MGI and the Alliance were not queried live, because PubMed and NCBI pages were blocked in this session. Anything drawn from them is marked "unverified".
- **Ontology CURIEs are leads from memory, not looked-up bindings**, except the ClinGen row and the terms already present in `kb/disorders/SYN1-Related_Disorder.yaml`. Each must be resolved before it is bound.

---

## 1. Disease Information

**Overview.** SYN1-related neurodevelopmental disorder is an X-linked condition caused by pathogenic variants in **SYN1**, which encodes synapsin I, a neuron-specific presynaptic phosphoprotein that regulates synaptic vesicle clustering, neurotransmitter release and synaptogenesis. It mainly affects hemizygous males. The core picture is epilepsy (often focal, often reflex seizures triggered by contact with water), intellectual disability or learning disability, speech delay, and autism spectrum disorder or ADHD.

> "Pathogenic SYN1 variants are associated with variable X-linked neurodevelopmental disorders mainly affecting males." (PMID:36568968, Parenti et al. 2022; human clinical)

**Identifiers**

| Resource | Identifier | Status |
|---|---|---|
| MONDO | MONDO:0010339 (label in the existing KB entry: "epilepsy, X-linked 1, with variable learning disabilities and behavior disorders") | From repo |
| OMIM phenotype | 300491 | Given; also cited in PMID:36568968 full text |
| OMIM allelic phenotype | 300115 (non-syndromic X-linked intellectual disability, MRX50) | PMID:36568968 full text |
| OMIM gene | 313440 | PMID:34243774 full text |
| HGNC | hgnc:11494 | From repo |
| ClinGen | SYN1 – X-linked complex neurodevelopmental disorder (MONDO:0100148), XL, **Definitive**, Intellectual Disability and Autism GCEP, 2023-04-05, CGGV:assertion_ca5a3e64-5daa-4a2f-876d-4e7648c53ff8-2023-04-05T180000.000Z | Read from `cache/clingen/gene_validity.csv` |
| Orphanet | ORPHA:85294 (X-linked epilepsy-learning disabilities-behavior disorders syndrome) | Unverified, from memory |
| ICD-10 / ICD-11 / MeSH | No disease-specific code known; generic epilepsy codes (e.g. G40.x) | Unverified |

The ClinGen curation is filed under MONDO:0100148, not MONDO:0010339, so it is a broader lumping, not the same disease term.

**Synonyms.** X-linked epilepsy with variable learning disabilities and behavior disorders; X-linked epilepsy-learning disabilities-behavior disorders syndrome; SYN1-related epilepsy; synapsin 1-related epilepsy; X-linked focal epilepsy with reflex bathing seizures; bathing epilepsy (SYN1-related); MRX50 (allelic intellectual-disability-only presentation).

**Source type.** Knowledge is aggregated from family studies, case reports and multicentre case series. No EHR-derived or registry data exist. The literature covers roughly 85 reported individuals:

> "Currently, 85 (73 male and 12 female) cases have been reported in 50 families." (PMID:39177219, full text; human clinical)

---

## 2. Etiology

**Causal factor.** Germline variants in SYN1, with loss of function as the mechanism for truncating variants. The first report was a nonsense variant (recalled as W356X; the abstract was not retrieved) in a four-generation X-linked epilepsy family (PMID:14985377, Garcia et al. 2004). A second nonsense variant then linked the gene to autism:

> "This nonsense mutation was found in all affected individuals from a large French-Canadian family segregating epilepsy and ASDs." (PMID:21441247; human clinical)

**Genetic risk and modifier factors**

- **Variant class.** "Genotype-phenotype correlation revealed that epileptic phenotypes are enriched in individuals with truncating variants." (PMID:36568968)
- **Sex.** Males are predominantly affected. Carrier females are "either unaffected or … display a variable number and severity of clinical signs" (PMID:36568968 full text).
- **X-inactivation** is a hypothesised, unproven modifier in females: "When assessed, X-inactivation analysis of the healthy female carriers within families did not reveal any skewing" in blood (PMID:36568968 full text).
- **Modifier genes.** None established in humans. In mice, loss of additional synapsin genes is additive: "double or triple gene knockouts display additive effects which lead to more severe phenotypes" (PMID:36568968 full text, reviewing mouse work).
- **Candidate interactor.** PRICKLE1 was reported to interact with synapsin I (PMID:24312498, title-level only).

**Environmental factors.** No environmental cause is known. Sensory stimuli act as seizure precipitants (see section 5), and fever is a reported trigger.

**Protective factors.** None identified, genetic or environmental. A second X chromosome is partly protective in heterozygous females.

**Gene–environment interaction.** The reflex-seizure phenotype is the clearest example: a SYN1 genotype combined with a somatosensory or autonomic stimulus (water on skin, towel rubbing, defecation) precipitates seizures. The mechanism linking the stimulus to ictogenesis is not demonstrated.

**Non-genetic phenocopy (separate entity).** Maternal synapsin autoantibodies have been associated with neurodevelopmental delay in offspring (PMID:36742338, title-level). This is not the Mendelian disorder.

---

## 3. Phenotypes

Frequencies are from the Parenti 2022 pooled analysis (71 males and 12 females, new plus published) unless stated:

> "behavioral disturbances such as autism spectrum disorder or attention deficit hyperactivity disorder are observed in 91% of the individuals, epilepsy in 82%, intellectual disability in 77%, and developmental delay in 70%." (PMID:36568968)

| Phenotype | Type | Frequency | Onset, course, severity | Suggested HPO (verify) |
|---|---|---|---|---|
| Epilepsy / seizures | Sign | 82% | Onset "ranges from 6 months to 26 years of life, with a median age of onset of 7 years old" (PMID:36568968 full text); episodic | HP:0001250 Seizure |
| Focal impaired-awareness seizures | Sign | Main seizure type | "Seizure types mainly include tonic-clonic or focal seizures with impaired awareness" (PMID:36568968) | HP:0002384 Focal impaired awareness seizure; HP:0007359 Focal-onset seizure |
| Bilateral tonic-clonic seizures | Sign | Main seizure type | Episodic | HP:0002069 Bilateral tonic-clonic seizure |
| Reflex seizures (water contact, bathing, showering) | Sign | Over 50% of epileptic cases; over 60% in a 19-patient EEG series (PMID:39177219) | Triggered "regardless of the water temperature" (PMID:34078716) | Look up a reflex-seizure term in HPO; none is confidently recalled |
| Autonomic ictal features (pallor, cyanosis, tachycardia, occasional bradycardia or apnoea) | Sign | Common in recorded seizures (PMID:39177219 full text) | Episodic | HP:0002459 Dysautonomia is coarse; look up an autonomic-seizure term |
| Febrile seizures | Sign | 32% (6/19) in PMID:39177219; also in female carriers (PMID:26096837) | Early childhood | HP:0002373 Febrile seizure (within the age range of 3 months to 6 years) |
| Status epilepticus | Sign | Reported; frequency not extracted | Episodic | HP:0002133 Status epilepticus |
| Intellectual disability | Sign | 77% | Borderline to profound; earlier seizure onset tracks with severity | HP:0001249 Intellectual disability |
| Global developmental delay | Sign | 70% | Walking at median 17.5 months (range 12–36); first words at median 24 months (range 12 months–12 years) (PMID:36568968 full text) | HP:0001263 Global developmental delay |
| Speech and language delay / specific language impairment | Sign | Frequent | "SYN1 Q555X male mutation carriers showed specific language impairment and mild autistic spectrum disorder" (PMID:26096837) | HP:0000750 Delayed speech and language development |
| Autism spectrum disorder / autistic behaviour | Behavioural | Part of the 91% behavioural figure; 16% (3/19) formally diagnosed in PMID:39177219 | Childhood, stable | HP:0000729 Autistic behavior |
| ADHD | Behavioural | 32% (6/19) in PMID:39177219 | Childhood | HP:0007018 Attention deficit hyperactivity disorder |
| Learning disability, reading impairment | Behavioural/cognitive | Frequent; reading impairment in female carriers (PMID:26096837) | Childhood | HP:0001328 Specific learning disability; HP:0010522 Dyslexia |
| Aggression, impulsivity, poor eye contact, sleep disorder | Behavioural | "Additional behavioral issues were observed in 65% (17/26)" (PMID:36568968 full text) | Variable | HP:0000718 Aggressive behavior; HP:0002360 Sleep abnormality |
| Developmental regression | Sign | Six individuals; in five it began after epilepsy onset (PMID:36568968 full text) | After seizure onset | HP:0002376 Developmental regression |
| Macrocephaly | Sign | "Five individuals exhibited macrocephaly (>2 SD)" (PMID:36568968 full text) | Congenital or early | HP:0000256 Macrocephaly |
| Hippocampal atrophy on MRI | Imaging | 2 of 5 imaged members of the Q555X family (PMID:26096837) | Not stated | HP:0031883? (look up "Hippocampal atrophy") |
| Psychogenic non-epileptic seizures | Behavioural | Reported (PMID:39177219 full text) | Not stated | Look up |

**Reflex triggers.** Beyond water contact, reported triggers are "rubbing with a towel, fever, toothbrushing, fingernail clipping, falling asleep, and watching others showering or bathing", and also "hyperpnea, emotion, lighting, using a stroboscope, digestive troubles, and defecation" (PMID:36568968). A Chinese family had toothbrushing-triggered seizures (PMID:34616357, title-level).

**Laboratory abnormalities.** None are characteristic. Routine biochemistry and metabolic screens were negative in a reported proband (PMID:34243774 full text).

**Phenotypic range.** At one end is intellectual disability alone: in the MRX50 family, "all affected members display intellectual disability as sole clinical manifestation" (PMID:28973667). At the other is a profound developmental-delay presentation (PMID:34243774).

**Quality of life.** No EQ-5D, SF-36 or PROMIS data were found. Qualitatively, reflex seizures during bathing carry a drowning and injury risk and interfere with hygiene routines (my inference). At the severe end, daily living is fully dependent (PMID:34243774 proband A).

---

## 4. Genetic / Molecular Information

**Gene.** SYN1 (hgnc:11494; OMIM 313440; Xp11; NCBI Gene 6853). It produces two isoforms, Ia (705 aa) and Ib (669 aa), sharing N-terminal domains A–C and differing at the C-terminus (PMID:34243774 and PMID:36568968 full text).

**Variant spectrum.**

> "The molecular spectrum of SYN1 variants is broad and encompasses truncating variants (frameshift, nonsense, splicing and start-loss variants) as well as non-truncating variants (missense substitutions and in-frame duplications)." (PMID:36568968)

| Variant | Class | Phenotype | Functional data | Source |
|---|---|---|---|---|
| W356X (unverified, from memory) | Nonsense | X-linked epilepsy with learning and behaviour problems | Not established | PMID:14985377 (metadata only) |
| p.Q555X | Nonsense | Focal epilepsy with reflex bathing seizures, ASD | Fails to rescue vesicle-pool defects; impaired MAPK/Erk phosphorylation and neurite outgrowth | PMID:21441247, PMID:23406870, PMID:26096837 |
| p.A51G, p.A550T, p.T567A | Missense | Autism and/or epilepsy cohorts | A550T and T567A show "impaired targeting to nerve terminals" | PMID:21441247 |
| c.236C>G p.S79W | Missense (B-domain) | Non-syndromic XLID (MRX50) | Reduced vesicle mobility; increased clustering | PMID:28973667 |
| c.1076C>A p.T359K; c.1444C>T p.Q482X (NM_133499) | Missense; nonsense | Developmental delay, reflex seizures | None | PMID:34243774 |
| 8 P/LP variants plus 2 VUS, 9 novel | Mixed | Bathing epilepsy | None | PMID:34078716 |
| 22 variants in 31 individuals | Mixed | Full spectrum | None | PMID:36568968 |
| Nonsense variant | Nonsense | Toothbrushing epilepsy | None | PMID:34616357 (title-level) |
| In-frame deletion | In-frame | Focal epilepsy in two brothers | None | PMID:36693418 (summary-level) |
| SYN1 duplication variant | Duplication | Variable phenotype in two brothers | None | PMID:38576531 (summary-level) |
| SYN1 candidate variant | Not extracted | Suggestive XLID | Segregation analysis | PMID:31906484 |

**Classification.**

- Truncating variants are generally pathogenic or likely pathogenic.
- Missense and in-frame variants are harder to classify: "Missense substitutions and in-frame duplications fall within the category of VUS, unless functional studies (PS3) or a de novo origin with confirmed maternity and paternity (PS2) are reported" (PMID:36568968 full text).
- The A51G, A550T and T567A cohort variants from the 2011 study should be treated cautiously. I did not check their current ClinVar or gnomAD status.

**Population frequency.** Pathogenic variants are private or ultra-rare. gnomAD carries putatively damaging variants outside domains A and B, more often in females (PMID:36568968 full text). I did not query gnomAD directly.

**Origin.** Germline, mostly maternally inherited: "all reported probands were male in the condition, whose significant SYN1 variants were inherited from their asymptomatic or mild affected mother" (PMID:34243774, as of 2021). De novo occurrence is documented: "Four SYN1 variants arose de novo in the index patient", two of them in females (PMID:36568968 full text). Somatic mosaicism is discussed but not demonstrated.

**Functional consequence.** Loss of function is supported for truncating variants. Some missense variants cause altered function rather than simple loss: S79W increases vesicle clustering and reduces mobility, and the authors "suggest that distinct mutations in SYN1 may lead to distinct brain pathologies" (PMID:28973667).

**Modifier genes, epigenetics, chromosomal abnormalities.** No modifiers or epigenetic signature are established. This is not a chromosomal disorder; karyotype and microarray were used in one report to exclude other causes (PMID:34243774).

---

## 5. Environmental Information

- **Toxins, lifestyle, infectious agents:** not applicable; no evidence found.
- **Seizure precipitants:** contact with water at any temperature, towel rubbing, haircutting, nail clipping, toothbrushing, defecation, fever, falling asleep, emotion, light or strobe stimulation, and watching others bathe (PMID:34078716, PMID:36568968, PMID:39177219).
- **Distinction from hot-water epilepsy:** in a comparison group, "none of the individuals with hot-water epilepsy displayed SYN1 variants" (PMID:34078716).

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

1. **A hemizygous SYN1 variant** (truncating, or missense in domains B–D) **leads to** loss or alteration of synapsin I function in neurons. *Demonstrated genetically in humans (PMID:14985377, 21441247, 36568968). Whether truncated transcripts undergo nonsense-mediated decay in patient neurons is not demonstrated.*
2. Defective synapsin I **results in** disorganised synaptic vesicle clusters and smaller, poorly trafficked vesicle pools. *Demonstrated in knockout mice and in rescue experiments in knockout neurons:* "all the D-domain mutants failed in rescuing the impairment in the size and trafficking of synaptic vesicle pools, whereas the wild-type human SynI fully reverted the KO phenotype" (PMID:21441247; in vitro).
3. The vesicle-pool defect **causes** opposite changes at the two main synapse types.
   - **3a. Inhibitory (GABAergic) terminals:** a smaller readily releasable pool **leads to** weaker evoked inhibition and stronger depression during trains (PMID:19020204, 23406870, 18057210; in vitro).
   - **3b. Excitatory (glutamatergic) terminals:** increased evoked currents or facilitation and more asynchronous release (PMID:19020204, 23406870; in vitro).
4. This excitation/inhibition imbalance **results in** network hyperexcitability and synchronised bursting. *Demonstrated on multi-electrode arrays:* "These changes were associated with higher network excitability and firing/bursting activity" (PMID:23406870).
5. Network hyperexcitability **leads to** seizures, with a temporo-insular and perisylvian predominance in humans. *The network localisation is demonstrated by EEG and SPECT (PMID:26096837, 39177219). Why this network is preferentially affected, and how cutaneous or autonomic input triggers it, is **inferred, not demonstrated**.*
6. **Parallel developmental branch:** altered synapsin I **leads to** impaired neurite outgrowth and delayed synaptogenesis. *Demonstrated in vitro:* Q555X "had a dramatic impact on phosphorylation by MAPK/Erk and neurite outgrowth" (PMID:21441247); axonal development and synaptogenesis are impaired in Syn1-deficient hippocampal neurons (PMID:7568107, title-level).
7. Steps 4 and 6 together **result in** intellectual disability, language impairment and autistic or ADHD behaviour. *This step is **inferred**; the causal link from synaptic defect to cognition is not shown in humans.*
8. **Possible feedback:** early or frequent seizures **may worsen** cognition. *Associational only:* "individuals with early seizures onset tend to present with severe-to-profound intellectual disability" (PMID:36568968).

### Supporting detail

**Protein function and dysfunction.** Synapsin I tethers vesicles in the reserve pool and releases them on phosphorylation. Domain A carries regulatory phosphorylation sites, domain C is essential for activity, and the proline-rich D-domain "is substrate of multiple protein kinases" (PMID:21441247). Synapsin also forms a liquid condensate that captures lipid vesicles (PMID:29976799; in vitro), which is the current biophysical model for vesicle clustering. The S79W variant sits "in the region of the B-domain involved in recognition of highly curved membranes" (PMID:28973667).

**Mouse ultrastructure and physiology.**

> "densely packed vesicles were only present in a narrow rim at active zones, whereas the majority of vesicles were dispersed throughout the terminal area." (PMID:7568108; model organism)

> "Cumulative amplitude analysis revealed that these effects were attributable to opposite changes in the size of the readily releasable pool of SVs." (PMID:19020204; in vitro)

> "A parallel decrease in the SV readily releasable pool in inhibitory synapses and in the release probability in excitatory synapses caused a marked reduction in the evoked synchronous release." (PMID:23406870; in vitro)

**Human network evidence.**

> "Available evidence suggests that impaired SYN1 function is associated with hyperexcitability of the temporoinsular network and disturbance of high mental functions such as language and social interaction." (PMID:26096837; human clinical)

Interictal EEG shows "a shift to lower frequency bands in power spectrum … and an increased connectivity in both temporal regions" (PMID:39177219). Cortical grey-matter microstructure was studied by diffusion MRI in 13 Q555X carriers versus 13 controls (PMID:29671924; findings not extracted).

**Categories with no disease-specific evidence.** Metabolic change, immune involvement, tissue damage (oxidative stress, fibrosis, necrosis), epigenetic change, and patient-derived transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial or CRISPR-screen data: none found. No patient iPSC-derived neuron study of SYN1 was found in the searches run.

**Signalling pathways.** MAPK/Erk phosphorylation of the D-domain is the pathway directly implicated (PMID:21441247). PKA and CaMKII regulation of synapsin is general biology that I did not verify against a source here.

**Suggested ontology terms (verify each)**

| Axis | Terms |
|---|---|
| GO biological process | GO:0097091 synaptic vesicle clustering; GO:0007269 neurotransmitter secretion; GO:0016079 synaptic vesicle exocytosis; GO:0051932 synaptic transmission, GABAergic; GO:0035249 synaptic transmission, glutamatergic; GO:0007416 synapse assembly; GO:0031175 neuron projection development |
| GO cellular component | GO:0008021 synaptic vesicle; GO:0098793 presynapse; GO:0043195 terminal bouton |
| CL | CL:0000540 neuron; CL:0000617 GABAergic neuron; CL:0000679 glutamatergic neuron |
| Already in the KB entry | GO:0140090 membrane curvature sensor activity; GO:0099504; GO:0007268; CL:0000540; UBERON:0000955. The entry also lists `GO:7770062`, which is not a standard GO accession pattern and should be checked. |

---

## 7. Anatomical Structures Affected

- **Organ and system:** brain, central nervous system (UBERON:0000955 brain). No consistent extra-neurological involvement. Synapsins are also expressed in the peripheral nervous system (PMID:36568968 full text), but no peripheral phenotype is reported.
- **Regions:** temporal lobe, insula and perisylvian cortex (ictal EEG and SPECT); hippocampus (atrophy in 2 of 5 imaged; PMID:26096837). Suggested: UBERON:0001871 temporal lobe, UBERON:0002022 insula, UBERON:0002421 hippocampal formation, UBERON:0000956 cerebral cortex.
- **Cells:** inhibitory and excitatory neurons, with distinct effects in each (section 6).
- **Subcellular:** presynaptic terminal and synaptic vesicle clusters. S79W also causes "aberrant accumulation of small clear vesicles in the soma" (PMID:28973667).
- **Lateralisation:** the EEG series reports increased connectivity "in both temporal regions" (PMID:39177219). Brain MRI is usually normal.

---

## 8. Temporal Development

- **Onset.** Developmental delay is evident from infancy or early childhood. Seizure onset ranged from 6 months to 26 years with a median of 7 years in the pooled series (PMID:36568968), and from 6 months to 13 years in the EEG series (PMID:39177219).
- **Severity gradient.** "in individuals with severe-to-profound ID, seizures manifested at a median age of 1 year of life (range: 5 months to 5 years)" (PMID:36568968 full text).
- **Course.** A lifelong, non-degenerative neurodevelopmental disorder with episodic seizures. A minority regress after seizure onset (5 of 6 regressing individuals).
- **Remission.** Treatment-induced seizure control is achievable (section 12). Spontaneous remission is not documented.
- **Critical period.** Early seizure onset marks a worse cognitive outcome. Whether earlier seizure control changes this is untested.
- **Mouse parallel.** "Mice lacking either synapsin I or synapsin II develop handling induced seizures from around two months of age" (PMID:23570901, search-result snippet), paper titled for "sensitive and critical periods".

---

## 9. Inheritance and Population

- **Prevalence and incidence.** Unknown. About 85 individuals in 50 families were reported by 2024 (PMID:39177219), which supports an ultra-rare classification. No Orphanet figure was verified.
- **Inheritance.** X-linked (HP:0001417). OMIM labels it both X-linked recessive and X-linked dominant, reflecting variable expression in heterozygous females. ClinGen records the mode as XL.
- **Penetrance.** High in hemizygous males; incomplete in females: "pointing to the existence of clinical heterogeneity and incomplete penetrance" (PMID:36568968 full text).
- **Expressivity.** Highly variable, including within families: "patients' clinical manifestations vary in genders and individuals, even in the same pedigree" (PMID:34243774). Two brothers with the same duplication had different phenotypes (PMID:38576531).
- **Anticipation:** none (not a repeat disorder). **Consanguinity:** not relevant. **Carrier frequency:** not established.
- **Germline mosaicism:** not specifically documented. An apparently de novo variant in an unaffected mother has been reported (PMID:36568968 full text, citing Accogli et al.).
- **Founder effect.** The Q555X variant segregates in one large French-Canadian kindred (PMID:21441247, 26096837). This is a single family, not a demonstrated population founder allele. The A51G, A550T and T567A variants were "found in 1.0 and 3.5% of French-Canadian individuals with autism and epilepsy, respectively" (PMID:21441247).
- **Geography.** Cases come from Europe and North America, with the first Asian cases reported in 2021 (PMID:34243774, 34616357). This most likely reflects where sequencing was done.
- **Sex ratio.** Strong male excess (73 males to 12 females reported), though "the exact male:female ratio is however difficult to determine due to the paucity of detailed clinical information on female carriers" (PMID:36568968 full text).
- **Age distribution.** Mostly children and adolescents; mean age at last follow-up was about 14 years in the EEG series.

---

## 10. Diagnostics

**Genetic testing (the diagnostic test).**

- Exome or genome sequencing, or an epilepsy/intellectual-disability/XLID gene panel that includes SYN1. A targeted 82-gene XLID panel identified a SYN1 candidate (PMID:31906484).
- Single-gene SYN1 sequencing is reasonable when bathing-triggered seizures are present: all 10 bathing-epilepsy families tested carried SYN1 variants (PMID:34078716).
- Microarray, karyotype and fragile X testing are part of the generic developmental-delay work-up and are expected to be normal. One reported family carried a SYN1 duplication (PMID:38576531), so copy-number analysis has some value.
- Segregation analysis and a three-generation X-linked pedigree support classification. Missense variants often remain VUS without functional or de novo evidence.
- Mitochondrial DNA and repeat-expansion testing are not indicated.

**Electrophysiology.**

> "ictal EEG showed a characteristic rhythmic theta/delta activity predominating in temporo-perisylvian regions at the beginning of most seizures." (PMID:39177219)

Background EEG is "mainly normal" and interictal abnormalities are "often rare or not visible", so a normal routine EEG does not exclude the diagnosis. Video-EEG with a provocation such as bathing can capture events.

**Imaging.** Brain MRI is usually normal; hippocampal atrophy has been seen in a minority (PMID:26096837). Ictal SPECT "showed temporoinsular perfusion changes" (PMID:26096837).

**Laboratory tests, biomarkers, biopsy, omics diagnostics.** None are specific or available.

**Neuropsychology.** Formal assessment of IQ, language, reading, autism and ADHD is warranted in affected males and carrier females (PMID:26096837).

**Diagnostic criteria.** No formal criteria exist. The diagnosis is molecular. A practical clinical flag is a male with water-contact reflex seizures, developmental or language delay, and an X-linked family history.

**Differential diagnosis**

| Condition | Distinguishing feature |
|---|---|
| Hot-water epilepsy | Triggered by hot water on the head; SYN1-negative in the comparison group (PMID:34078716) |
| Other X-linked epilepsy or intellectual disability (e.g. PCDH19, CDKL5, ARX, IQSEC2) | Molecular testing; PCDH19 affects females |
| Other synaptic vesicle cycle disorders (e.g. STXBP1, SNAP25, SYT1, DNM1) | Usually earlier and more severe; reviewed in PMID:32738165 |
| Temporal lobe epilepsy of other cause | Structural lesion, no reflex triggers |
| Psychogenic non-epileptic seizures | Can coexist in SYN1 patients (PMID:39177219) |

**Screening.** No newborn or population screening. Cascade testing of at-risk maternal relatives is appropriate.

---

## 11. Outcome / Prognosis

- **Survival and mortality.** No survival or life-expectancy data exist. Four of ten epileptic members of the Q555X family were deceased at evaluation (PMID:26096837), but cause and age of death were not extracted, so no mortality inference should be drawn. SUDEP and drowning risks are theoretical concerns that have not been quantified.
- **Morbidity.** Dominated by cognitive, language and behavioural disability, ranging from isolated learning difficulty to profound intellectual disability with full dependency.
- **Seizure outcome.** Xiong et al. describe "easily controlled reflex seizure" (PMID:34243774), but drug resistance occurs, and the EEG series analysed drug resistance as a variable (PMID:39177219).
- **Prognostic factors.**
  - Early seizure onset predicts more severe intellectual disability (PMID:36568968).
  - A truncating variant predicts epilepsy (PMID:36568968).
  - Male sex predicts a fuller phenotype.
  - "The age at epilepsy onset was not predictive of response to antiseizure medications" (PMID:39177219 full text).
- **Complications.** Regression after seizure onset in a minority, status epilepticus, ictal bradycardia or apnoea, and psychogenic non-epileptic seizures.
- **Biomarkers and quality-of-life measures.** None available.

---

## 12. Treatment

No disease-modifying therapy exists. Management is symptomatic.

**Antiseizure medication.** The only systematic evidence is a 2025 PRISMA review of 8 studies and 52 patients (PMID:40554312):

| Drug | Use | Seizure-free | Seizure-free or ≥50% reduction | Suggested CHEBI (verify) |
|---|---|---|---|---|
| Valproic acid | 58% (most prescribed) | Not stated | Lower than sodium-channel blockers | CHEBI:39867 |
| Lamotrigine | 35% | Not stated | 63% | CHEBI:6367 |
| Carbamazepine | 35% | 38% | 50% | CHEBI:3387 |
| Oxcarbazepine | Not stated | 44% | Not stated | CHEBI:7824 |
| Lacosamide | Not stated | 50% | 50% | CHEBI:135939 |
| Levetiracetam | Not stated | Not stated | Lower than sodium-channel blockers | CHEBI:6437 (already in the KB entry) |

> "patients with SYN1-related epilepsy show better seizure frequency reduction when treated with LCM, LTG, CBZ, or OXC, compared to VPA and LEV, despite VPA being the most prescribed anti-seizure medication for this syndrome. Hence, sodium channel blockers appear to represent the best therapeutic option for these patients." (PMID:40554312)

Caveats and genotype-guided use:

- The data are retrospective and uncontrolled.
- The seizure-reduction difference was significant (p = 0.028).
- The seizure-freedom difference was significant only "for patients carrying a non-truncating variant (p = 0.047)", a tentative genotype-guided signal.
- A single family reported prompt valproate response (PMID:36693418).
- The existing KB entry lists levetiracetam; the review ranks it below sodium-channel blockers.

**Other modalities**

- **Trigger management:** avoiding or modifying precipitants and supervising bathing (expert practice; no trial).
- **Pharmacogenomics:** nothing SYN1-specific. Generic HLA-B*15:02 and HLA-A*31:01 screening before carbamazepine or oxcarbazepine applies as for any patient (general guidance, not verified here).
- **Gene therapy, antisense, cell therapy, immunotherapy:** none in development that I could find. I did not search ClinicalTrials.gov or ICTRP directly, so the absence of registered trials is unconfirmed. No NCT identifiers are offered.
- **Surgery and neurostimulation:** no SYN1-specific data.
- **Supportive and rehabilitative care:** speech and language therapy, special education, occupational therapy, and behavioural and psychiatric management of autism and ADHD, by standard practice.

**Suggested NCIT terms (verify):** NCIT:C15986 Pharmacotherapy (with `therapeutic_agent` per drug); NCIT:C15747 Supportive Care; NCIT:C15240 Genetic Counseling. The last three are already used in the KB entry. Speech therapy: the repository's guidance cites NCIT:C159273.

---

## 13. Prevention

- **Primary prevention:** none other than reproductive options. Once the familial variant is known, prenatal or preimplantation testing is technically possible.
- **Secondary prevention:** cascade testing of maternal-line relatives; early developmental surveillance and EEG evaluation of variant-positive boys.
- **Tertiary prevention:** seizure control, water-safety measures (supervised bathing, showers rather than baths; my inference), and educational support.
- **Genetic counselling.** A carrier mother has a 50% chance of transmitting the variant at each pregnancy. Sons who inherit it are likely to be affected with variable severity. Daughters who inherit it are carriers with reduced penetrance. De novo variants occur. "A timely molecular diagnosis and genetic counseling are cardinal for appropriate patient management and treatment." (PMID:36568968)
- **Immunisation, public health, environmental interventions, prophylactic medication:** not applicable.

---

## 14. Other Species / Natural Disease

- **Orthologues.** Synapsins are conserved across vertebrates and invertebrates (PMID:36568968 full text). Mouse *Syn1* is X-linked; suggested identifiers MGI:98460 and NCBI Gene 20964, and rat *Syn1* RGD:3797 / NCBI Gene 24949, are all unverified and should be looked up at the Alliance or NCBI. NCBITaxon:10090 (mouse), NCBITaxon:10116 (rat).
- **Naturally occurring disease.** No spontaneous SYN1 disease in companion or farm animals was identified. OMIA was not searched.
- **Conservation of mechanism.** "Mouse and human SynI are highly homologous, and reintroduction of hSynI was found to rescue the defects in SV trafficking of SynI KO neurons" (PMID:23406870 full text).
- **Zoonosis and transmission:** not applicable.

---

## 15. Model Organisms

| Model | Type | Recapitulates | Limitations | Source |
|---|---|---|---|---|
| *Syn1* knockout mouse | Constitutive knockout | Dispersed vesicle clusters, reduced glutamate release, delayed recovery after high-frequency stimulation, "strikingly increased response to electrical stimulation, as measured by electrographic and behavioral seizures" | Seizures are late-onset and stimulus-induced; cognitive effect is mild: "the disruption of a single synapsin gene has only a mild impact on learning and behavior" (PMID:36568968 full text) | PMID:7568108, PMID:7777057 |
| *Syn1* / *Syn2* knockout mice, seizure development | Knockout | Handling-induced seizures from about two months; sensitive periods | Sensory-evoked, not water-specific | PMID:23570901 |
| Synapsin knockout mice, behaviour | Knockout | Autism-related social abnormalities | Stronger in *Syn2* than *Syn1* knockouts (PMID:36568968 full text) | PMID:23280234; PMID:28922833 (*Syn2*) |
| Synapsin triple knockout | Triple knockout | Profound social deficits and cortical dysfunction | Not a single-gene model | PMID:42349827 (2026; summary-level) |
| *Syn1* knockout primary cortical neurons on multi-electrode arrays | In vitro | Hyperexcitable, synchronised networks; opposite readily-releasable-pool changes | Mouse neurons; no circuit context | PMID:19020204 |
| *Syn1* knockout hippocampal neurons re-expressing human wild-type, Q555X, A550T, T567A or S79W | In vitro rescue | Variant-specific vesicle-pool, targeting, plasticity and mobility defects | Lentiviral overexpression; mutant expressed on a null background | PMID:21441247, 23406870, 28973667 |
| *Syn1* knockout inhibitory synapses | In vitro | Reduced readily releasable pool at inhibitory synapses | As above | PMID:18057210 (title-level) |

**Gaps.**

- No patient-variant knock-in mouse was found.
- No patient iPSC-derived neuron model was found.
- No zebrafish or *Drosophila* disease model was retrieved.
- These are search results from this session, not proof of absence.
- The mouse reproduces sensory-evoked seizures in a general sense. It does not reproduce water-specific reflex seizures, the human temporo-insular localisation, or the degree of intellectual disability.

**Suggested gene bindings for mouse models:** mouse *Syn1* on `MGI:` (look up the accession); human SYN1 constructs on `hgnc:11494`.

---

## Evidence gaps to resolve before curation

1. Fetch the abstracts for the metadata-only PMIDs listed at the top before quoting them, especially 14985377 (the founding report), 18057210, 23280234 and 7777057.
2. Verify ORPHA:85294 and extract its Orphanet rows for prevalence, inheritance and HPO phenotypes.
3. Decide whether the ClinGen Definitive assertion (MONDO:0100148) may be recorded on this entry. It names a different MONDO term, so it counts only if the entry's mappings justify it.
4. Check ClinVar and gnomAD for A51G, A550T and T567A before treating them as pathogenic.
5. Search ClinicalTrials.gov and ICTRP to confirm there are no registered interventional trials.
6. Resolve every suggested HP, GO, CL, UBERON, CHEBI and NCIT CURIE against its ontology, and check the existing entry's `GO:7770062`.

---

## Sources

Primary literature (PubMed):

- [PMID:14985377](https://pubmed.ncbi.nlm.nih.gov/14985377/) Garcia CC et al. J Med Genet 2004. Identification of a mutation in synapsin I in a family with epilepsy.
- [PMID:21441247](https://pubmed.ncbi.nlm.nih.gov/21441247/) Fassio A et al. Hum Mol Genet 2011. SYN1 loss-of-function mutations in autism and partial epilepsy.
- [PMID:23406870](https://pubmed.ncbi.nlm.nih.gov/23406870/) Lignani G et al. Hum Mol Genet 2013. Epileptogenic Q555X SYN1 mutant.
- [PMID:26096837](https://pubmed.ncbi.nlm.nih.gov/26096837/) Nguyen DK et al. Epilepsia 2015. X-linked focal epilepsy with reflex bathing seizures.
- [PMID:28973667](https://pubmed.ncbi.nlm.nih.gov/28973667/) Guarnieri FC et al. Hum Mol Genet 2017. S79W in MRX50.
- [PMID:29671924](https://pubmed.ncbi.nlm.nih.gov/29671924/) Cabana JF et al. Hum Brain Mapp 2018. SYN1 Q555X and cortical grey-matter microstructure.
- [PMID:30390306](https://pubmed.ncbi.nlm.nih.gov/30390306/) Peron A et al. Epilepsia 2018. Hot water epilepsy and SYN1 variants (letter).
- [PMID:31906484](https://pubmed.ncbi.nlm.nih.gov/31906484/) Ibarluzea N et al. Genes 2020. Targeted NGS in suggestive XLID.
- [PMID:32738165](https://pubmed.ncbi.nlm.nih.gov/32738165/) John A et al. J Neurochem 2021. Neurodevelopmental spectrum of synaptic vesicle cycling disorders.
- [PMID:34078716](https://pubmed.ncbi.nlm.nih.gov/34078716/) Accogli A et al. Neurology 2021. Reflex bathing epilepsy ([PMC8424500](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8424500/)).
- [PMID:34243774](https://pubmed.ncbi.nlm.nih.gov/34243774/) Xiong J et al. 2021. Familial SYN1 variants in Asian paediatric patients.
- [PMID:34616357](https://pubmed.ncbi.nlm.nih.gov/34616357/) Zhou Q et al. Front Neurol 2021. X-linked toothbrushing epilepsy.
- [PMID:36568968](https://pubmed.ncbi.nlm.nih.gov/36568968/) Parenti I et al. Front Cell Dev Biol 2022 ([PMC9773998](https://pmc.ncbi.nlm.nih.gov/articles/PMC9773998); [publisher PDF](https://www.frontiersin.org/journals/cell-and-developmental-biology/articles/10.3389/fcell.2022.1019715/pdf)).
- [PMID:36693418](https://pubmed.ncbi.nlm.nih.gov/36693418/) Leuschner UV et al. Neuropediatrics 2023. Two brothers responding to valproate.
- [PMID:36742338](https://pubmed.ncbi.nlm.nih.gov/36742338/) Bünger I et al. Front Immunol 2023. Maternal synapsin autoantibodies.
- [PMID:38576531](https://pubmed.ncbi.nlm.nih.gov/38576531/) Ren B et al. Front Neurol 2024. Variable phenotypes in siblings.
- [PMID:39177219](https://pubmed.ncbi.nlm.nih.gov/39177219/) Moya Quiros V et al. Ann Neurol 2025. Electro-clinical features and functional connectivity.
- [PMID:40554312](https://pubmed.ncbi.nlm.nih.gov/40554312/) Van Boxstael E et al. Seizure 2025. Treating seizures in SYN1-related epilepsy: a systematic review.
- [PMID:24312498](https://pubmed.ncbi.nlm.nih.gov/24312498/) Paemka L et al. PLoS One 2013. PRICKLE1 interaction with synapsin I.

Model and mechanism:

- [PMID:7777057](https://pubmed.ncbi.nlm.nih.gov/7777057/) Rosahl TW et al. Nature 1995.
- [PMID:7568108](https://pubmed.ncbi.nlm.nih.gov/7568108/) Li L et al. PNAS 1995.
- [PMID:7568107](https://pubmed.ncbi.nlm.nih.gov/7568107/) Chin LS et al. PNAS 1995.
- [PMID:18057210](https://pubmed.ncbi.nlm.nih.gov/18057210/) Baldelli P et al. J Neurosci 2007.
- [PMID:19020204](https://pubmed.ncbi.nlm.nih.gov/19020204/) Chiappalone M et al. Cereb Cortex 2009.
- [PMID:23280234](https://pubmed.ncbi.nlm.nih.gov/23280234/) Greco B et al. Behav Brain Res 2013.
- [PMID:23570901](https://pubmed.ncbi.nlm.nih.gov/23570901/) Etholm L et al. Exp Neurol 2013.
- [PMID:28922833](https://pubmed.ncbi.nlm.nih.gov/28922833/) Michetti C et al. 2017 (*Syn2* knockout).
- [PMID:29976799](https://pubmed.ncbi.nlm.nih.gov/29976799/) Milovanovic D et al. Science 2018.
- [PMID:42349827](https://pubmed.ncbi.nlm.nih.gov/42349827/) Nicosia N et al. Prog Neuropsychopharmacol Biol Psychiatry 2026.

Structured sources:

- ClinGen Gene-Disease Validity: [CGGV:assertion_ca5a3e64-5daa-4a2f-876d-4e7648c53ff8-2023-04-05T180000.000Z](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_ca5a3e64-5daa-4a2f-876d-4e7648c53ff8-2023-04-05T180000.000Z) (read from the repository's `cache/clingen/gene_validity.csv`).
- Europe PMC REST API (metadata confirmation), queried 2026-11-13.
- Dataset for Accogli et al.: [Dryad doi:10.5061/dryad.w0vt4b8qr](https://doi.org/10.5061/dryad.w0vt4b8qr).

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 33 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 47 |
| Quoted claims found in source | 45 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 33 |
| On topic | 26 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:36568968`: "either unaffected or … display a variable number and severity of clinical signs"
  - closest text in source: "Overall, female carriers have been reported to be either unaffected or to display a variable number and severity of clinical signs, hence pointing to the existence of clinical heterogeneity and incomplete penetrance"
- `PMID:39177219`: "a shift to lower frequency bands in power spectrum … and an increased connectivity in both temporal regions"
  - closest text in source: "Comparing patients with SYN1 to healthy subjects, we observed a shift to lower frequency bands in power spectrum of interictal EEG and an increased connectivity in both temporal regions"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 60 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 4 |
| Terms whose name was checked | 7 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 4 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0100148` (3 mentions) - the report calls it "SYN1 – X-linked complex neurodevelopmental disorder", "Decide whether the ClinGen Definitive assertion"; MONDO calls it **X-linked complex neurodevelopmental disorder**
- `CHEBI:39867` (1 mention) - the report calls it "Lower than sodium-channel blockers"; CHEBI calls it **valproic acid**
- `CHEBI:7824` (1 mention) - the report calls it "Not stated"; CHEBI calls it **oxcarbazepine**
- `CHEBI:6437` (1 mention) - the report calls it "already in the KB entry"; CHEBI calls it **levetiracetam**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `HP:0002459` (obsolete Dysautonomia) (1 mention) - replaced by `HP:0012332`

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0010339` (3 mentions) - the report calls it "label in the existing KB entry: "epilepsy, X-linked 1, with variable learning disabilities and behavior disorders"; MONDO calls it **epilepsy, X-linked 1, with variable learning disabilities and behavior disorders**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0100148` - called "SYN1 – X-linked complex neurodevelopmental disorder", "Decide whether the ClinGen Definitive assertion"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`, `ORPHA`, `MGI`, `RGD`.